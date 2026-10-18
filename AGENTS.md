# AGENTS.md — 给 AI Agent 的工作指引

本文件面向自动化 AI Agent（编码助手、文档机器人、贡献脚本）。人类读者请看 [README.md](README.md)。

## 这个仓库是什么

`synomosai-skills` 是 SynomosAI（诺莫斯 AI）的**官方 Agent Skills 聚合仓**：`skills/` 目录下有 **51 个技能子目录**，每个目录含一份 `SKILL.md`（YAML frontmatter + 正文），遵循 Agent Skills 规范。本仓本身不提供可执行服务程序，资产就是这 51 个技能目录 + 根目录文档。

## 可用的工作命令

```bash
# 克隆
git clone https://github.com/SynomosAI/synomosai-skills.git

# 列出技能（应为 51 个目录）
ls skills/

# 读取某技能头部（frontmatter）
head -20 skills/ai-grader/SKILL.md
```

前置依赖：无。本仓不含需构建的代码，不需要安装任何包。

## 约定（Do）

- 新增 / 修改技能时，保持 `SKILL.md` 的 YAML frontmatter 字段兼容（`name` / `description` 等按既有技能的写法对齐）。
- 新增一个技能目录后，**必须同步**：① README.md「技能清单」对应分类计数与列表；② `llms.txt` / `llms-full.txt` 的技能全景；③ 根目录 README 顶部「51 个」总数。
- 技能署名沿用各技能 frontmatter 既有 `author` 字段口径（如 `诺声(Logos)@SynomosAI` 等品牌大使笔名）。

## 禁止（Don't）

- 不要改动根目录 `LICENSE`、README「署名与版权」段的权属表述——权属字段只由维护者变更。
- 不要在技能目录或根目录提交任何密钥、令牌或真实客户数据。
- 不要绕过组织 ruleset：main 分支禁止直推，任何改动走 Pull Request 并等待 lgd-ci-gate 通过。
- 不要把本仓技能描述成「已认证 / 已商用交付 / 已服务特定客户」——技能为效率工具与方法论沉淀。

## 边界

本仓是**技能索引与分发仓**：它聚合的是提示词 / 方法论 / 工作流，不是可运行软件；技能输出为参考性质，不构成专业咨询结论。
