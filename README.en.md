# SynomosAI Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-SKILL.md-blue.svg)](skills/)
[![skills count](https://img.shields.io/badge/skills-51-brightgreen.svg)](skills/)
[![HF Marketplace](https://img.shields.io/badge/HF%20Marketplace-zhaoxinghua09%2Fskills-ffd21e.svg)](https://huggingface.co/zhaoxinghua09/skills)

**The official skill repository of SynomosAI** — 51 ready-to-use Agent Skills covering AI governance, AI-brain methodology, content operations, medical-device international business, and developer tooling.

> Skills follow the **Agent Skills** convention (`SKILL.md` + YAML frontmatter) and work with Claude Code, Codex, Gemini CLI, Cursor, WorkBuddy, and other mainstream AI agent frameworks.

## Features

- **Zero setup**: each skill is one directory (`skills/<skill-name>/`) with a `SKILL.md`; drop it into your skills directory and your agent can load it.
- **51 skill directories** across five areas: AI governance & security (8), AI-brain / memory & learning (6), development & engineering (28), medical-device international business (4), AI team & brand (5).
- **Cross-framework**: unified `SKILL.md` frontmatter (name / description / triggers) discovered by every supported agent.
- **Multi-channel distribution**: also published to the Hugging Face Skills marketplace, ClawHub / SkillHub, and SkillPie (skillpie.cn).

## Quick start

### Option 1: copy directly (recommended)

Copy a `skills/<skill-name>/` directory into your agent's skills directory:

```bash
# Claude Code
cp -r skills/ai-grader ~/.claude/skills/

# or any agent tool supporting the SKILL.md convention
cp -r skills/ai-grader ~/.agents/skills/
```

### Option 2: Hugging Face Marketplace

```text
/plugin marketplace add zhaoxinghua09/skills
/plugin install <skill-name>@zhaoxinghua09/skills
```

### Option 3: browse locally

```bash
ls skills/                # all 51 skill directories
head -40 skills/ai-grader/SKILL.md
```

## Skill catalog (51)

### AI governance & security (8)
`a3-law-operational` · `ai-governance-audit-chain` · `ai-consciousness` · `ai-grader` · `authz-code-design` · `credential-vault-design` · `premise-and-config-audit` · `traceability-audit-team`

### AI-brain / memory & learning (6)
`ai-brain-learning-memory` · `ai-brain-learning-memory-pro` · `brain-design-benchmark` · `agent-learn-external-skill` · `cross-session-passphrase` · `cross-machine-offline-taskbox`

### Development & engineering (28)
`code-mentor` · `coding-agent` · `debug-pro` · `data-scientist` · `continuous-test-review-loop` · `llm-gateway-hub` · `local-llm-eval-assist` · `rag-eval-harness` · `project-planning-methodology` · `research-methodology` · `research-quality-gate` · `publish-quality-gate` · `content-publish-lifecycle` · `ssot-content-management` · `fingerprint-delivery` · `doc-legacy-extract` · `summarize-file` · `summarize-pro` · `todo-tracker` · `reminder` · `unified-task-ledger` · `local-agent-open` · `tencent-cos-static-site` · `video-watermark-anti-theft` · `wechat-article-full-workflow` · `wechat-qa-checklist` · `wechat-viral-topic` · `lexiang-website-sync`

### Medical-device international business · MedXpert line (4)
`medxpert-llm-library` · `medxpert-l1-batch-study` · `medxpert-skill-panorama` · `offline-knowledge-alignment`

### AI team & brand (5)
`asset-controlled-export-pipeline` · `ardot-mobile-app-multi-screen` · `laopaidang-core` · `identity-verify` · `personal-assistant`

## Attribution & copyright

- Skill author credits: pen names such as `诺声(Logos)@SynomosAI` (see each skill's frontmatter `author` field).
- Copyright: © 2026 SynomosAI.
- License: MIT License (the `LICENSE.md` inside each skill directory governs that skill).

## License

This repository root is released under the **MIT License**, Copyright © 2026 SynomosAI; see [LICENSE](LICENSE) for the full text. Where a skill directory contains its own `LICENSE.md`, that directory's own license terms prevail.

## Security

If you find a security issue, please report it privately as described in [SECURITY.md](SECURITY.md) — do not disclose it in a public issue.

## Contributing

Issues and PRs are welcome. The `main` branch is protected by organization ruleset: open a Pull Request from a personal branch and wait for the lgd-ci-gate checks to pass. Keep `SKILL.md` frontmatter compatible when editing skills.

## Ecosystem

- **ClawHub / SkillHub**: skills are mirrored to the ClawHub ecosystem and its local mirror SkillHub.
- **SkillPie**: published to the skillpie.cn community.
- **Hugging Face**: published as the HF Skills marketplace (`zhaoxinghua09/skills`).

## Disclaimer

The skills in this repository are productivity tools and methodology material; they do not constitute professional advice. Outputs touching regulation, compliance, or medicine are self-assessment references — verify independently before use.

---

© 2026 SynomosAI · MIT License
