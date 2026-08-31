# SynomosAI Skills 生态

**SynomosAI（诺莫斯 AI）官方技能仓库** — 51 个开箱即用的 Agent Skills，覆盖 AI 治理、AI 大脑方法论、内容运营、医疗器械国际业务、开发者工具等场景。

> 技能采用 **Agent Skills 规范**（`SKILL.md` + YAML frontmatter），与 Claude Code、Codex、Gemini CLI、Cursor、WorkBuddy 等主流 AI Agent 框架兼容。

## 快速开始

### 方式一：直接拷贝（推荐）

将 `skills/<技能名>/` 整个目录放入你的技能目录：

```bash
# Claude Code
cp -r skills/ai-grader ~/.claude/skills/

# 或任意 agent 工具（支持 SKILL.md 规范）
cp -r skills/ai-grader ~/.agents/skills/
```

### 方式二：Hugging Face Marketplace（跨工具标准化发现）

本仓库已同步发布到 Hugging Face Skills 市场：

```
/plugin marketplace add zhaoxinghua09/skills
/plugin install <skill-name>@zhaoxinghua09/skills
```

## 技能清单（51 个）

### AI 治理与安全（8）
`a3-law-operational` · `ai-governance-audit-chain` · `ai-consciousness` · `ai-grader` · `authz-code-design` · `credential-vault-design` · `premise-and-config-audit` · `traceability-audit-team`

### AI 大脑 / 记忆与学习（6）
`ai-brain-learning-memory` · `ai-brain-learning-memory-pro` · `brain-design-benchmark` · `agent-learn-external-skill` · `cross-session-passphrase` · `cross-machine-offline-taskbox`

### 开发与工程（28）
`code-mentor` · `coding-agent` · `debug-pro` · `data-scientist` · `continuous-test-review-loop` · `llm-gateway-hub` · `local-llm-eval-assist` · `rag-eval-harness` · `project-planning-methodology` · `research-methodology` · `research-quality-gate` · `publish-quality-gate` · `content-publish-lifecycle` · `ssot-content-management` · `fingerprint-delivery` · `doc-legacy-extract` · `summarize-file` · `summarize-pro` · `todo-tracker` · `reminder` · `unified-task-ledger` · `local-agent-open` · `tencent-cos-static-site` · `video-watermark-anti-theft` · `wechat-article-full-workflow` · `wechat-qa-checklist` · `wechat-viral-topic` · `lexiang-website-sync`

### 医疗器械国际业务 · MedXpert 线（4）
`medxpert-llm-library` · `medxpert-l1-batch-study` · `medxpert-skill-panorama` · `offline-knowledge-alignment`

### AI 团队与品牌（5）
`asset-controlled-export-pipeline` · `ardot-mobile-app-multi-screen` · `laopaidang-core` · `identity-verify` · `personal-assistant`

## 署名与版权

- 技能作者署名：`诺声(Logos)@SynomosAI` 等品牌大使笔名（详见各技能 frontmatter `author` 字段）
- 版权：© 2026 SynomosAI
- 许可：MIT License（各技能目录内 `LICENSE.md` 为准）

## 与生态的关联

- **ClawHub / SkillHub**：本仓库技能同步发布于 ClawHub 生态及其本土镜像 SkillHub
- **SkillPie**：同步发布于 skillpie.cn 社区
- **Hugging Face**：同步发布为 HF Skills Marketplace（`zhaoxinghua09/skills`）
- **更多**：Coze 技能商店、Capafy 海外变现等渠道持续接入中

---

© 2026 SynomosAI · MIT License
