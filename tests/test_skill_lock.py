import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "tools" / "skill_lock.py"


def run(cmd, root):
    return subprocess.run(
        [sys.executable, str(TOOL), cmd, "--root", str(root)],
        capture_output=True, text=True,
    )


def make_tree(root: Path) -> None:
    a = root / "skills" / "alpha"
    b = root / "skills" / "beta"
    a.mkdir(parents=True, exist_ok=True)
    b.mkdir(parents=True, exist_ok=True)
    (a / "SKILL.md").write_text("---\nname: alpha\ndescription: does alpha\n---\n", encoding="utf-8")
    (a / "run.py").write_text("print('a')\n", encoding="utf-8")
    (b / "SKILL.md").write_text("---\nname: beta\ndescription: beta helper\n---\n", encoding="utf-8")


def test_generate_then_verify_passes(tmp_path):
    make_tree(tmp_path)
    assert run("generate", tmp_path).returncode == 0
    assert (tmp_path / "skills.lock.json").exists()
    r = run("verify", tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr


def test_verify_fails_when_byte_changes(tmp_path):
    make_tree(tmp_path)
    run("generate", tmp_path)
    (tmp_path / "skills" / "beta" / "SKILL.md").write_text(
        "---\nname: beta\ndescription: beta helper!\n---\n", encoding="utf-8"
    )
    r = run("verify", tmp_path)
    assert r.returncode == 1
    assert "digest drift" in r.stdout


def test_verify_fails_when_skill_added_unrecorded(tmp_path):
    make_tree(tmp_path)
    run("generate", tmp_path)
    g = tmp_path / "skills" / "gamma"
    g.mkdir()
    (g / "SKILL.md").write_text("---\nname: gamma\ndescription: g\n---\n", encoding="utf-8")
    r = run("verify", tmp_path)
    assert r.returncode == 1
    assert "absent from skills.lock.json" in r.stdout


def test_verify_fails_when_skill_removed(tmp_path):
    make_tree(tmp_path)
    run("generate", tmp_path)
    import shutil
    shutil.rmtree(tmp_path / "skills" / "beta")
    r = run("verify", tmp_path)
    assert r.returncode == 1
    assert "missing on disk" in r.stdout


def test_verify_fails_without_lockfile(tmp_path):
    make_tree(tmp_path)
    r = run("verify", tmp_path)
    assert r.returncode == 1
    assert "missing skills.lock.json" in r.stdout


def test_selftest_has_both_controls(tmp_path):
    make_tree(tmp_path)
    run("generate", tmp_path)
    r = run("selftest", tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "negative control OK" in r.stdout
    assert "positive control OK" in r.stdout


def test_lockfile_is_stable_across_runs(tmp_path):
    make_tree(tmp_path)
    run("generate", tmp_path)
    first = json.loads((tmp_path / "skills.lock.json").read_text(encoding="utf-8"))
    run("generate", tmp_path)
    second = json.loads((tmp_path / "skills.lock.json").read_text(encoding="utf-8"))
    assert first["root_digest"] == second["root_digest"]
