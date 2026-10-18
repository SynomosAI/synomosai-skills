# SynomosAI Skills 生态

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-SKILL.md-blue.svg)](skills/)
[![skills count](https://img.shields.io/badge/skills-51-brightgreen.svg)](skills/)
[![HF Marketplace](https://img.shields.io/badge/HF%20Marketplace-zhaoxinghua09%2Fskills-ffd21e.svg)](https://huggingface.co/zhaoxinghua09/skills)

**SynomosAI（诺莫斯 AI）官方技能仓库** — 51 个开箱即用的 Agent Skills，覆盖 AI 治理、AI 大脑方法论、内容运营、医疗器械国际业务、开发者工具等场景。

> 技能采用 **Agent Skills 规范**（`SKILL.md` + YAML frontmatter），与 Claude Code、Codex、Gemini CLI、Cursor、WorkBuddy 等主流 AI Agent 框架兼容。

**关键词 / Keywords**：agent skills · AI 治理 · 知识工作自动化 · 内容运营 · AI 大脑 · 本地 LLM · RAG 评测 · 医疗器械合规 · Claude Code · Cursor · WorkBuddy

## ✨ 特性 / Features

- **开箱即用**：每个技能即一个目录（`skills/<技能名>/`），含 `SKILL.md`（YAML frontmatter + 正文），拷进技能目录即可被 Agent 加载。
- **51 个技能目录**：覆盖 AI 治理与安全（8）、AI 大脑 / 记忆与学习（6）、开发与工程（28）、医疗器械国际业务（4）、AI 团队与品牌（5）五大场景。
- **跨框架兼容**：遵循 Agent Skills 规范，Claude Code、Codex、Gemini CLI、Cursor、WorkBuddy 等均可按 `SKILL.md` frontmatter 发现并调用。
- **多渠道分发**：同步发布于 Hugging Face Skills 市场、ClawHub / SkillHub、SkillPie（skillpie.cn），Coze 技能商店等渠道持续接入中。
- **可审计**：本组织仓自带三层机器人审核工作流（见 `.github/workflows/`），合并请求须过 lgd-ci-gate 状态检查。

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

### 方式三：浏览本地清单

```bash
# 列出全部技能目录（共 51 个）
ls skills/

# 查看某个技能的说明头部
head -40 skills/ai-grader/SKILL.md
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

## 仓库结构 / Repository layout

```text
synomosai-skills/
├── README.md            # 本文件
├── README.en.md         # 英文版说明
├── LICENSE              # MIT License（© 2026 SynomosAI）
├── CODEOWNERS           # 代码所有者（@SynomosAI/synomosai-gov）
├── SECURITY.md          # 安全策略
├── AGENTS.md            # 给 AI Agent 的工作指引
├── llms.txt             # 给 AI 的最小索引（llms.txt 标准）
├── llms-full.txt        # 给 AI 的完整文本
├── skills/              # 51 个技能目录（每个含 SKILL.md）
└── .github/workflows/   # lgd-ci-gate / 三层机器人审核工作流
```

## 署名与版权

- 技能作者署名：`诺声(Logos)@SynomosAI` 等品牌大使笔名（详见各技能 frontmatter `author` 字段）
- 版权：© 2026 SynomosAI
- 许可：MIT License（各技能目录内 `LICENSE.md` 为准）

## License / 许可

本仓库根目录以 **MIT License** 许可发布，版权归属 © 2026 SynomosAI；完整条款见根目录 [LICENSE](LICENSE)。各技能目录内如另有 `LICENSE.md`，以该目录内许可口径为准。

## 🔒 安全 / Security

如发现安全问题（如技能提示词含危险指令、技能目录内误提交敏感信息），请按 [SECURITY.md](SECURITY.md) 的方式**私下**报告，不要在公开 issue 中披露。

## 🤝 贡献 / Contributing

欢迎提 Issue / PR 改进技能或补充文档。本仓 main 分支受组织 ruleset 保护，请从个人分支发起 Pull Request，并等待 lgd-ci-gate 与三层机器人审核通过后合并。改动技能时请保持 `SKILL.md` frontmatter 兼容。

## 与生态的关联

- **ClawHub / SkillHub**：本仓库技能同步发布于 ClawHub 生态及其本土镜像 SkillHub
- **SkillPie**：同步发布于 skillpie.cn 社区
- **Hugging Face**：同步发布为 HF Skills Marketplace（`zhaoxinghua09/skills`）
- **更多**：Coze 技能商店、Capafy 海外变现等渠道持续接入中

## 免责声明

本仓库技能为**效率工具与方法论沉淀**，不构成任何专业咨询结论；涉及法规、合规、医疗的技能输出为自评 / 参考性质，正式使用前请独立核实。

---

© 2026 SynomosAI · MIT License
