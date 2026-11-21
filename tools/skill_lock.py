#!/usr/bin/env python3
"""skill_lock.py — 技能树的完整性锁（对标策展注册表的 checksum + lockfile 模型）。

为什么需要：任何"技能目录 + 提示词"被加载进智能体，就等于把一段可执行意图
送进上下文。没有完整性锁时，上游改一个字节、加一个文件、删一个文件，下游
完全无感。策展注册表（Skills.sh 一类）用"静态分析 + 校验和 + 版本锁定"解决这个，
本工具把同一层能力落到仓库内、不依赖任何外部服务。

设计要点：
  1. 只读、可复算：锁文件是纯文本 JSON，任何人在任何机器上重算应当一致。
  2. 双向可证伪：`--selftest` 会自己改坏一个字节，verify 必须失败；
     只做"必须通过"的锁等于没有锁。
  3. 拒绝静默漂移：多出的技能、消失的技能、改动的字节，三种都报。

用法：
    python tools/skill_lock.py generate --root .
    python tools/skill_lock.py verify   --root .
    python tools/skill_lock.py selftest --root .
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LOCK_NAME = "skills.lock.json"
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "tests", "fixtures", "testdata"}
TEXT_LIMIT = 1_000_000  # 单文件 >1MB 按二进制处理，避免读爆内存


def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _skill_dirs(root: Path) -> list[Path]:
    """任何含 SKILL.md 的目录都算一个技能，跳过明显的非技能目录。"""
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        if "SKILL.md" in filenames:
            found.append(Path(dirpath))
    return sorted(found)


def _tree_digest(skill_dir: Path) -> tuple[str, int]:
    """目录摘要 = sha256( 排序后的 "相对路径\\0文件sha256" 逐行拼接 )。"""
    files: list[tuple[str, str]] = []
    for p in sorted(skill_dir.rglob("*")):
        if not p.is_file():
            continue
        parts = set(p.relative_to(skill_dir).parts)
        if parts & SKIP_DIRS:
            continue
        rel = p.relative_to(skill_dir).as_posix()
        files.append((rel, _sha256_file(p)))
    h = hashlib.sha256()
    for rel, digest in files:
        h.update(f"{rel}\0{digest}\n".encode())
    return h.hexdigest(), len(files)


def _front_matter(skill_md: Path) -> tuple[str, str]:
    name, desc = "", ""
    try:
        lines = skill_md.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    except Exception:
        return name, desc
    if not lines or lines[0].strip() != "---":
        return name, desc
    for line in lines[1:]:
        if line.strip() == "---":
            break
        low = line.strip()
        if low.lower().startswith("name:"):
            name = low.split(":", 1)[1].strip().strip('"\'')
        elif low.lower().startswith("description:"):
            desc = low.split(":", 1)[1].strip().strip('"\'')
    return name, desc


def build_lock(root: Path) -> dict:
    entries = []
    for d in _skill_dirs(root):
        rel = d.relative_to(root).as_posix() or "."
        digest, count = _tree_digest(d)
        fm_name, fm_desc = _front_matter(d / "SKILL.md")
        entries.append(
            {
                "path": rel,
                "declared_name": fm_name,
                "has_description": bool(fm_desc),
                "file_count": count,
                "digest": digest,
            }
        )
    h = hashlib.sha256()
    for e in entries:
        h.update(f"{e['path']}\0{e['digest']}\n".encode())
    return {
        "schema_version": 1,
        "algorithm": "sha256(sorted relpath + NUL + file sha256, per line)",
        "root_digest": h.hexdigest(),
        "skill_count": len(entries),
        "skills": entries,
    }


def diff_lock(root: Path, lock: dict) -> list[str]:
    problems: list[str] = []
    recorded = {e["path"]: e for e in lock.get("skills", [])}
    actual = {d.relative_to(root).as_posix() or ".": d for d in _skill_dirs(root)}

    for path, entry in sorted(recorded.items()):
        d = actual.get(path)
        if d is None:
            problems.append(f"{path}: recorded in {LOCK_NAME} but missing on disk (skill removed)")
            continue
        digest, count = _tree_digest(d)
        if digest != entry["digest"]:
            problems.append(
                f"{path}: digest drift (locked {entry['digest'][:12]}, actual {digest[:12]}); "
                f"files {entry['file_count']} -> {count}"
            )
        if entry["declared_name"] and entry["declared_name"] != path.split("/")[-1] and path != ".":
            problems.append(
                f"{path}: SKILL.md name '{entry['declared_name']}' does not match directory name"
            )
    for path in sorted(actual):
        if path not in recorded:
            problems.append(f"{path}: skill present on disk but absent from {LOCK_NAME}")

    # 根摘要：把"整体一致"也做成一个可比较的量
    if not problems:
        rebuilt = build_lock(root)
        if rebuilt["root_digest"] != lock.get("root_digest"):
            problems.append(
                f"root_digest mismatch (locked {str(lock.get('root_digest'))[:12]}, "
                f"rebuilt {rebuilt['root_digest'][:12]})"
            )
    return problems


def cmd_generate(root: Path, out: Path) -> int:
    lock = build_lock(root)
    out.write_text(json.dumps(lock, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {out} : {lock['skill_count']} skills, root_digest={lock['root_digest'][:16]}")
    return 0


def cmd_verify(root: Path, lock_path: Path) -> int:
    if not lock_path.exists():
        print(f"::error file={lock_path}::missing {LOCK_NAME}; run `python tools/skill_lock.py generate`")
        return 1
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    problems = diff_lock(root, lock)
    for p in problems:
        print(f"::error::{p}")
    if problems:
        print(f"SKILL LOCK FAIL: {len(problems)} problem(s)")
        return 1
    print(f"SKILL LOCK OK: {lock['skill_count']} skills match {lock_path.name}")
    return 0


def cmd_selftest(root: Path) -> int:
    """负控：改坏一个字节必须红，恢复后必须绿。"""
    if not (root / LOCK_NAME).exists():
        print("selftest skipped: no lockfile")
        return 0
    tmp = Path(tempfile.mkdtemp())
    failures = 0
    try:
        work = tmp / "tree"
        shutil.copytree(root, work, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__"))
        lock = json.loads((work / LOCK_NAME).read_text(encoding="utf-8"))
        target = None
        for e in lock["skills"]:
            d = work / e["path"]
            for p in sorted(d.rglob("*")):
                if p.is_file():
                    target = p
                    break
            if target:
                break
        if target is None:
            print("selftest skipped: no files inside any skill")
            return 0

        orig = target.read_bytes()
        target.write_bytes(orig[:-1] + bytes([orig[-1] ^ 0x01]))
        rc1 = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "verify", "--root", str(work)],
            capture_output=True, text=True
        ).returncode
        if rc1 == 0:
            print("::error::negative control failed: a mutated byte still verified clean")
            failures += 1
        else:
            print(f"negative control OK: mutated byte rejected (exit {rc1})")

        target.write_bytes(orig)
        rc2 = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "verify", "--root", str(work)],
            capture_output=True, text=True
        ).returncode
        if rc2 != 0:
            print("::error::positive control failed: restored tree does not verify")
            failures += 1
        else:
            print("positive control OK: restored tree verifies")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["generate", "verify", "selftest"])
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    root = Path(a.root).resolve()
    lock_path = Path(a.out).resolve() if a.out else root / LOCK_NAME
    if a.command == "generate":
        return cmd_generate(root, lock_path)
    if a.command == "verify":
        return cmd_verify(root, lock_path)
    return cmd_selftest(root)


if __name__ == "__main__":
    sys.exit(main())
