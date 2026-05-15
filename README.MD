```

╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║   ██████╗ ███╗   ███╗    ███████╗██╗  ██╗██╗██╗     ██╗     ███████╗
║   ██╔══██╗████╗ ████║    ██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝
║   ██████╔╝██╔████╔██║    ███████╗█████╔╝ ██║██║     ██║     ███████╗
║   ██╔═══╝ ██║╚██╔╝██║    ╚════██║██╔═██╗ ██║██║     ██║     ╚════██║
║   ██║     ██║ ╚═╝ ██║    ███████║██║  ██╗██║███████╗███████╗███████║
║   ╚═╝     ╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝
║                                                                    ║
║   47 battle-tested skills + 6 command workflows                    ║
║   Claude Code • Cursor • Codex  • n8n • OpenClaw • and more ...    ║
║                                                                    ║
║   v0.78 • Apr 26, 2026 • CC BY-NC-SA 4.0                            ║
╚════════════════════════════════════════════════════════════════════╝
```


**Help product managers become more awesome at their craft — and help them send the ladder down to others.**

Battle-tested PM frameworks that teach both you and your AI agents how to do product management work at a professional level. You learn the *why*. Your agents execute the *how*. Everyone gets better.

Frame problems, hunt opportunities, scaffold validation experiments, and kill bad bets fast. With frameworks from Teresa Torres, Geoffrey Moore, Amazon, MITRE, and much more from product management's greatest hits.

---

# 🧰 PM Skills

#### 每天在用的一些 AI 技能和 Prompt，都开源在这里

[![Skills](https://img.shields.io/badge/Skills-4-10B981?style=for-the-badge)](#-skills)
[![Prompts](https://img.shields.io/badge/Prompts-1-F59E0B?style=for-the-badge)](#-prompts)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-8B5CF6?style=for-the-badge)](https://agentskills.io)

![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![OpenCode](https://img.shields.io/badge/OpenCode-Skill-3B82F6?style=flat-square)
![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-8B5CF6?style=flat-square)

</div>

- **Skills** — Agent 能直接加载的结构化指令集，遵循 [Agent Skills](https://agentskills.io) 开放标准。Claude Code、Codex、OpenCode、OpenClaw 都能装
- **Prompts** — 一段提示词，复制粘贴到 ChatGPT / Claude / Gemini 任何对话里就能用，不需要安装

---

## 📋 目录

### Skills

| 名字 | 一句话 |
|---|---|---|
| 🔭 [**hv-analysis（横纵分析法）**](#-hv-analysis横纵分析法) | 想搞懂一个产品/公司/概念是怎么回事，丢给它，给你一份万字 PDF 研究报告 | 
| 🔥 [**aihot（AI HOT 资讯查询）**](#-aihotai-hot-资讯查询) | 让 Agent 用一句话拿到 aihot.virxact.com 每天的 AI HOT 日报和全部 AI 动态，无需 API Key |  

### Prompts

| 名字 | 一句话 | 讲解 |
|---|---|---|
| 🔭 [**横纵分析法（Prompt 版）**](#-横纵分析法prompt-版) | 上面那个 Skill 的轻量版，复制粘贴到任何 Deep Research 模型里就能跑 |

---

## 📦 安装方式

在 Claude Code、Codex、OpenClaw 等支持 Skill 的 Agent 里，直接说：

```
帮我安装这个 skill：项目url 地址
```

把 `<skill-name>` 换成你想装的那个，比如 `hv-analysis`。Agent 会自己 clone 到对应目录，不用你操心路径。

---

### 🔭 hv-analysis（横纵分析法）

> *"纵向追时间深度，横向追同期广度，最终交汇出判断。"*

想搞懂一个产品 / 公司 / 概念 / 人物到底是怎么回事，丢给它就行。

它会同时跑两条线：**纵向**把研究对象从诞生讲到当下，像讲故事一样把演变讲完整；**横向**把同期所有主要竞品摆出来逐一对比。最后两条线一交叉，能看出一些只看现状或只看历史看不出来的东西。

最后给你一份**排版精美的 PDF 研究报告**，10,000–30,000 字。

**适合**

- 调研竞品 / 调研一个新概念 / 调研一个公司
- 写作前期需要系统性的素材准备
- 对一个领域想从零搞懂

**不适合**

- 单纯查个名词解释 — 那种问题用普通对话就行，杀鸡用牛刀

→ [SKILL.md](./hv-analysis/SKILL.md) 


### 🔥 aihot（AI HOT 资讯查询）

> *"AI 圈一天发太多东西，等我反应过来已经过气了——干脆让 Agent 帮我每天扫一遍。"*

让支持 SKILL.md 的 Agent 用最自然的中文一句话拿到 [aihot.virxact.com](https://aihot.virxact.com) 每天的 AI HOT 日报和全部 AI 动态。无需 API Key、无需配 MCP server。

**它能做什么**

- 拉今日 / 指定日期的 AI HOT 日报（按主题打包好的成品）
- 拉精选条目流（每日精编候选池）
- 按分类拉条目（模型 / 产品 / 行业 / 论文 / 技巧）
- 按时间窗口拉（最近 N 天）
- 关键词 / 公司 / 主题搜索（"OpenAI 最近发的"、"Sora 相关"、"RAG 论文"）

**怎么触发**

```
今天 AI 圈有什么新东西
看一下 5 月 6 号的 AI 日报
最近一周的 AI 论文
看下精选条目
最近 OpenAI 有什么发布
```

**🌐 跨平台**：Claude Code · Codex CLI · Cursor · Gemini CLI · OpenCode · Cline · Windsurf

**🇨🇳 国内直链**（无需翻墙）：

```
curl -fsSL https://aihot.virxact.com/aihot-skill/install.sh | bash
```

→ [SKILL.md](./aihot/SKILL.md) · [aihot.virxact.com](https://aihot.virxact.com) · [接入指南](https://aihot.virxact.com/agent)

</td></tr>
</table>

---

## 📝 Prompts

<a id="-prompts"></a>

<table>
<tr><td>

### 🔭 横纵分析法（Prompt 版）

上面那个 hv-analysis Skill 的**轻量版**——一段 prompt，复制粘贴到任何支持 Deep Research 的模型里就能跑（ChatGPT Deep Research、Gemini Deep Research、Grok Deep Search、Claude Research 都行），不需要安装任何东西。

半小时左右出一份万字级研究报告。

适合还没开始用 Claude Code / Codex 这类带 Skill 系统的 Agent，但又想体验一下这个方法论的人。

→ [横纵分析法.md](./prompts/横纵分析法.md) 

</td></tr>
</table>

---

# Superpowers

Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them.

## Quickstart

Give your agent Superpowers: [Claude Code](#claude-code), [Codex CLI](#codex-cli), [Codex App](#codex-app), [Factory Droid](#factory-droid), [Gemini CLI](#gemini-cli), [OpenCode](#opencode), [Cursor](#cursor), [GitHub Copilot CLI](#github-copilot-cli).

## How it works

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do. 

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest. 

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY. 

Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.


## Sponsorship

If Superpowers has helped you do stuff that makes money and you are so inclined, I'd greatly appreciate it if you'd consider [sponsoring my opensource work](https://github.com/sponsors/obra).

Thanks! 

- Jesse


## Installation

Installation differs by harness. If you use more than one, install Superpowers separately for each one.

### Claude Code

Superpowers is available via the [official Claude plugin marketplace](https://claude.com/plugins/superpowers)

#### Official Marketplace

- Install the plugin from Anthropic's official marketplace:

  ```bash
  /plugin install superpowers@claude-plugins-official
  ```

#### Superpowers Marketplace

The Superpowers marketplace provides Superpowers and some other related plugins for Claude Code.

- Register the marketplace:

  ```bash
  /plugin marketplace add obra/superpowers-marketplace
  ```

- Install the plugin from this marketplace:

  ```bash
  /plugin install superpowers@superpowers-marketplace
  ```

### Codex CLI

Superpowers is available via the [official Codex plugin marketplace](https://github.com/openai/plugins).

- Open the plugin search interface:

  ```bash
  /plugins
  ```

- Search for Superpowers:

  ```bash
  superpowers
  ```

- Select `Install Plugin`.

### Codex App

Superpowers is available via the [official Codex plugin marketplace](https://github.com/openai/plugins).

- In the Codex app, click on Plugins in the sidebar.
- You should see `Superpowers` in the Coding section.
- Click the `+` next to Superpowers and follow the prompts.

### Factory Droid

- Register the marketplace:

  ```bash
  droid plugin marketplace add https://github.com/obra/superpowers
  ```

- Install the plugin:

  ```bash
  droid plugin install superpowers@superpowers
  ```

### Gemini CLI

- Install the extension:

  ```bash
  gemini extensions install https://github.com/obra/superpowers
  ```

- Update later:

  ```bash
  gemini extensions update superpowers
  ```

### OpenCode

OpenCode uses its own plugin install; install Superpowers separately even if you
already use it in another harness.

- Tell OpenCode:

  ```
  Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
  ```

- Detailed docs: [docs/README.opencode.md](docs/README.opencode.md)

### Cursor

- In Cursor Agent chat, install from marketplace:

  ```text
  /add-plugin superpowers
  ```

- Or search for "superpowers" in the plugin marketplace.

### GitHub Copilot CLI

- Register the marketplace:

  ```bash
  copilot plugin marketplace add obra/superpowers-marketplace
  ```

- Install the plugin:

  ```bash
  copilot plugin install superpowers@superpowers-marketplace
  ```

## The Basic Workflow

1. **brainstorming** - Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.

2. **using-git-worktrees** - Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.

3. **writing-plans** - Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, verification steps.

4. **subagent-driven-development** or **executing-plans** - Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.

5. **test-driven-development** - Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.

6. **requesting-code-review** - Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.

7. **finishing-a-development-branch** - Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.

**The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.

## What's Inside

### Skills Library

**Testing**
- **test-driven-development** - RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

**Debugging**
- **systematic-debugging** - 4-phase root cause process (includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques)
- **verification-before-completion** - Ensure it's actually fixed

**Collaboration** 
- **brainstorming** - Socratic design refinement
- **writing-plans** - Detailed implementation plans
- **executing-plans** - Batch execution with checkpoints
- **dispatching-parallel-agents** - Concurrent subagent workflows
- **requesting-code-review** - Pre-review checklist
- **receiving-code-review** - Responding to feedback
- **using-git-worktrees** - Parallel development branches
- **finishing-a-development-branch** - Merge/PR decision workflow
- **subagent-driven-development** - Fast iteration with two-stage review (spec compliance, then code quality)

**Meta**
- **writing-skills** - Create new skills following best practices (includes testing methodology)
- **using-superpowers** - Introduction to the skills system

## Philosophy

- **Test-Driven Development** - Write tests first, always
- **Systematic over ad-hoc** - Process over guessing
- **Complexity reduction** - Simplicity as primary goal
- **Evidence over claims** - Verify before declaring success

Read [the original release announcement](https://blog.fsck.com/2025/10/09/superpowers/).


## Start Here

### Install Guides

- Claude Desktop/Web: [`docs/INSTALL-CLAUDE-DESKTOP.md`](docs/INSTALL-CLAUDE-DESKTOP.md)
- Claude Code: [`docs/INSTALL-CLAUDE-CODE.md`](docs/INSTALL-CLAUDE-CODE.md)
- Codex: [`docs/INSTALL-CODEX.md`](docs/INSTALL-CODEX.md)
- Release packaging for maintainers: [`docs/RELEASE-PACKAGING.md`](docs/RELEASE-PACKAGING.md)

---

## 📣 Updates & Announcements

### Apr 26, 2026 — v0.78 Release Packaging: One Download, Then Better PM Work

This release makes Product Manager Skills easier to use outside the repo. The job is simple: when a PM wants to use these skills with Claude or Codex, they should not have to understand GitHub folders, packaging scripts, or agent internals first.

**Who this is for:** nontechnical PMs using Claude Desktop/Web, Claude Code users who prefer the plugin marketplace, Codex users who need `.agents/skills`, and maintainers who want releases to be repeatable instead of handmade.

**What changed in v0.78:**
- Claude Desktop/Web users get easy-button ZIP packs that contain individual upload-ready skill ZIPs, including a small starter pack and themed packs for discovery, strategy, delivery, and AI PM work
- Codex users get a `codex-product-manager-skills.zip` with `.agents/skills` and `AGENTS.md`
- Maintainers get one release command: `./scripts/build-release.sh`
- GitHub Actions now builds release artifacts on PRs, main, and version tags
- New install docs tell each audience which path to use

Why it matters: the repo now has a source, a shelf, a storefront, and a rescue desk. `skills/` remains the source of truth; `dist/` becomes the generated shelf; GitHub Releases becomes the storefront; and the README helps people choose the right path without feeling lost.

Release note: [`docs/announcements/2026-04-26-v0-78-release-packaging.md`](docs/announcements/2026-04-26-v0-78-release-packaging.md)

---

### Mar 17, 2026 — v0.75 Pedagogic-First: Restoring What This Repo Is Actually For

I want to apologize  to a contributor who recently submitted a well-intentioned and well-coded improvement that stripped learning scaffolding in favor of tighter copy. It wasn't their fault — the docs they read never crisply stated that pedagogic value is non-negotiable. We fixed that. I will work with that contribution to bring in its efficiencies while retaining the learning aspects of the skills.

**What this repo is actually for:** As much as this repo is for adding skills to your agent, it's equally tasked to help product managers become more awesome at their craft, and helping them send the ladder down to others. Skills here serve both goals: they make your agent more capable, and they make you more knowledgeable about why the framework works. Neither is a byproduct of the other.

**ABC — Always Be Coaching** is a key governing principle. Every skill should leave the person using it knowing more than when they started. Stripping explanation to tighten output is a defect, not an improvement.

What changed in v0.75:
- `README.md` — Mission statement updated to name both audiences: human PMs and AI agents
- `CLAUDE.md` — Pedagogic-first added to the agent's mandate, not just the style guide
- `AGENTS.md` — New Operating Philosophy section so coding agents don't optimize away the teaching

Release note: [`docs/announcements/2026-03-17-v0-75-pedagogic-first.md`](docs/announcements/2026-03-17-v0-75-pedagogic-first.md)

**Now available:** Install skills directly from Claude Code via the plugin marketplace:
```bash
/plugin marketplace add deanpeters/Product-Manager-Skills
/plugin install jobs-to-be-done@pm-skills
```

---

### Mar 9, 2026 — v0.7 Sharper Skills, Faster Discovery

This release is about making the library easier to trust and easier to use.

As this repo grows, the standard has to rise with it. So v0.7 focuses on the parts users actually feel:
- finding the right skill faster,
- understanding when to use it,
- getting cleaner activation behavior,
- and trusting that the repo is being actively tightened, not just expanded.

#### Why it matters:
1. You spend less time guessing which skill to use.
2. Skills are more likely to show up in the situations where you actually need them.
3. The library becomes easier to navigate as it grows, not more chaotic.
4. Quality becomes a maintained promise, not a one-time cleanup.

#### What shipped:
- Trigger-oriented description updates across the skill library so skills answer both "what it does" and "use this when..."
- New `intent` frontmatter field so every skill can keep a sharp trigger description and a richer deeper-purpose summary
- New trigger-readiness auditing in `scripts/check-skill-triggers.py`
- Trigger checks wired into `scripts/test-library.sh`
- New `find-a-skill.sh --mode trigger` for discovering skills by use-case language, `best_for`, and `scenarios`
- New Streamlit (beta) `Find My Skill` mode so users can describe a situation in plain English and get recommended skills with clear next actions
- Streamlit navigation now separates `Learn`, `Find My Skill`, and `Run Skills` so first-time users can move from confusion to action faster
- Contributor docs updated so future skills follow the same tighter standard
- Cross-checked the tighter standard against Anthropic's [Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

Release note: [`docs/announcements/2026-03-09-v0-7-skill-quality-trigger-clarity.md`](docs/announcements/2026-03-09-v0-7-skill-quality-trigger-clarity.md)

---

### Mar 8, 2026 — v0.65 You Asked, We Listened: Setup + Integration Everywhere

You asked, we listened. We took a moment to create comprehensive instructions on how to install, integrate, or otherwise use any one or all of these skills.

What shipped:
- `docs/Using PM Skills 101.md` as the complete beginner-first guide
- `docs/Platform Guides for PMs.md` as the pick-your-tool index
- `docs/Using PM Skills with Slash Commands 101.md` for Claude `/slash` workflows like `/pm-story` and `/pm-prd`
- New PM-friendly platform docs for Claude Code, Claude Desktop, Claude Cowork, ChatGPT Desktop, OpenClaw, n8n, LangFlow, and Python agents
- Updated `START_HERE.md` with comfort-level paths (chat-first, terminal-first, automation-first)

How to make the best use of this release:
1. Start with [`docs/Using PM Skills 101.md`](docs/Using%20PM%20Skills%20101.md)
2. Choose your platform in [`docs/Platform Guides for PMs.md`](docs/Platform%20Guides%20for%20PMs.md)
3. Run one real task with one skill before scaling to multi-skill workflows

Release note: [`docs/announcements/2026-03-08-v0-65-onboarding-integration-guides.md`](docs/announcements/2026-03-08-v0-65-onboarding-integration-guides.md)

---

### Mar 6, 2026 — v0.6 Navigation + Commands

We added a command layer and fast navigation system while keeping skills as the source of truth.

What shipped:
- `START_HERE.md` for 60-second onboarding
- `commands/` directory with reusable multi-skill workflows
- `catalog/` generated indexes for quick browsing
- New helper scripts: `run-pm.sh`, `find-a-command.sh`, `test-library.sh`, and `generate-catalog.py`
- Command validation with `scripts/check-command-metadata.py`

Release note draft: [`docs/announcements/2026-03-06-v0-6-navigation-commands.md`](docs/announcements/2026-03-06-v0-6-navigation-commands.md)

---

### Feb 27, 2026 — v0.5 Streamlit (beta) Playground

We launched a new **Streamlit (beta)** interface for local skill test-driving.

What shipped:
- Local playground at `app/main.py` with guided browsing and session flows
- Multi-provider support (Anthropic, OpenAI, Ollama) with provider/model picker
- Environment-variable-only API handling (`app/.env.example`) for safer defaults
- Workflow UX upgrades (phase detection fix, per-phase output persistence, run-all phases control)
- Fast-model quality warnings on long workflows (especially PRD-style runs)

Docs:
- [`app/STREAMLIT_INTERFACE.md`](app/STREAMLIT_INTERFACE.md)
- [`app/.env.example`](app/.env.example)

Feedback welcome:
- [GitHub Issues](https://github.com/deanpeters/Product-Manager-Skills/issues)
- [Dean on LinkedIn](https://linkedin.com/in/deanpeters)

---

<a id="leaderskills"></a>
### Feb 27, 2026 — v0.5 Career & Leadership Skills Suite

Four new skills covering the full product leadership career arc — from PM to Director to VP/CPO — distilled from two episodes of [The Product Porch](https://the-product-porch-43ca35c0.simplecast.com) podcast.

**Based on Episode 42 — [From PM to Director: How to Make the Shift (Part 1)](https://the-product-porch-43ca35c0.simplecast.com/episodes/from-product-manager-to-director-how-to-make-the-shift-part-1):**
- [`altitude-horizon-framework`](skills/altitude-horizon-framework/SKILL.md) (Component) — The core mental model: altitude (scope) and horizon (time), the waiter-to-operator shift, four transition zones, named failure modes, and the Cascading Context Map
- [`director-readiness-advisor`](skills/director-readiness-advisor/SKILL.md) (Interactive) — Coaches PMs and new Directors across four situations: preparing, interviewing, newly landed, and recalibrating

**Based on Episode 43 — [Becoming a VP & CPO: Leading Product at the Executive Level (Part 2)](https://the-product-porch-43ca35c0.simplecast.com/episodes/becoming-a-vp-cpo-leading-product-at-the-executive-level-part-2):**
- [`executive-onboarding-playbook`](skills/executive-onboarding-playbook/SKILL.md) (Workflow) — A 30-60-90 day diagnostic playbook for VP/CPO transitions: diagnose before acting, surface unwritten strategy, assess people, act with evidence
- [`vp-cpo-readiness-advisor`](skills/vp-cpo-readiness-advisor/SKILL.md) (Interactive) — Coaches Directors and executives through the VP/CPO transition, including the CEO interview framework for evaluating roles before accepting

---

### Feb 10, 2026 — v0.4 Facilitation Protocol Fix

We found and fixed a facilitation regression in interactive flows.

What happened:
- We expected guided, step-by-step facilitation with progressive context handling.
- In practice, a brevity-focused rewrite path stripped out parts of the original facilitation modality (especially the "walk through questions" behavior).

What we changed in v0.4:
- Standardized a canonical facilitation protocol in [`skills/workshop-facilitation/SKILL.md`](skills/workshop-facilitation/SKILL.md).
- Rolled that source-of-truth linkage across interactive skills and facilitation-heavy workflow skills.
- Added mandatory session heads-up, `Context dump` bypass, and `Best guess` mode.
- Added stronger progress labels, interruption handling, and decision-point recommendation rules.

Credit:
- Codex identified the protocol mismatch and implemented the fix across the repo.

Announcement draft: [`docs/announcements/2026-02-10-v0-4-facilitation-fix.md`](docs/announcements/2026-02-10-v0-4-facilitation-fix.md)

---

### Feb 8, 2026 — LinkedIn Launch

**Post title:** Product Management Skills for Your Agents
**Subtitle:** Because "just prompt better" is not a strategy.

Still rewriting PM prompts and getting generic AI output? I built a reusable PM Skills repo to help you make sharper decisions, docs, and outcomes faster.

- Full announcement draft: [`docs/announcements/2026-02-08-linkedin-launch.md`](docs/announcements/2026-02-08-linkedin-launch.md)
- Substack article draft: [`docs/announcements/2026-02-08-substack-savage-launch.md`](docs/announcements/2026-02-08-substack-savage-launch.md)
- Announcements index: [`docs/announcements/README.md`](docs/announcements/README.md)
- Skills repo: [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills)
- Prior prompts repo: [Product Manager Prompts](https://github.com/deanpeters/product-manager-prompts)

---

## 🎯 What This Is

**47 ready-to-use PM skills + reusable command workflows** that teach both you and your AI agents how to do product management work at a professional level — so the PM understands the *why* and the agent can execute the *how*.

Instead of saying *"Write a PRD"* and hoping for the best, you and your agent both know:
- ✅ How to structure a PRD and why each section earns its place
- ✅ What questions to ask stakeholders and what you're listening for
- ✅ Which prioritization framework to use (and when each one breaks down)
- ✅ How to run customer discovery interviews and what signals matter
- ✅ How to break down epics using proven patterns — and the tradeoffs of each

**Result:** You work faster, with better consistency, at a higher strategic level — and you can explain why.

**Works with:** Claude Code, Cowork, OpenAI Codex, ChatGPT, Gemini, and any AI agent that can read structured knowledge.

---

## 🎓 Design Philosophy — Pedagogic and Practical in Equal Measure

As much as this repo is for adding skills to your agent, it's equally tasked to **help product managers become more awesome at their craft — and to help them send the ladder down to others.**

Skills here serve both goals simultaneously. They equip AI agents to do PM work at a professional level, and they teach the human PM the *why* behind the framework — so they can explain it, adapt it, and pass it on.

**ABC — Always Be Coaching** is a key governing principle. Every skill should leave the person using it knowing more than when they started.

This means:
- Skills explain reasoning, not just steps
- Examples show the thinking, not just the output
- Anti-patterns name the failure mode so you recognize it in the wild
- Interactive skills coach through discovery — they don't just collect answers

**An edit that strips learning scaffolding to tighten copy is a defect, not an improvement.**

---

## ⚡ Start in 60 Seconds

New here? Start with [`START_HERE.md`](START_HERE.md).

```bash
# Run a skill (artifact/analysis)
./scripts/run-pm.sh skill prioritization-advisor "We have 12 requests and one sprint"

# Run a command (multi-skill workflow)
./scripts/run-pm.sh command discover "Reduce onboarding drop-off for self-serve users"
```

Need discovery first?

```bash
./scripts/find-a-skill.sh --keyword onboarding
./scripts/find-a-command.sh --keyword roadmap
```

---

## Why The Command Layer Helps

Commands make using skills easier without replacing skills.

- Skills stay deep and pedagogic: they are the source of truth for frameworks, reasoning, and quality — for humans and agents alike.
- Commands remove stitching work: one command chains the right skills in the right order.
- You start faster: less "which skill should I run first?" and fewer manual handoffs.
- Outputs are more consistent: commands enforce checkpoints, then defer to skill-level rigor.
- Teams onboard quicker: new users can run `/discover` or `/write-prd` and learn the skill system while shipping.

In short: **skills provide expertise; commands provide momentum.**

---

## 🧪 Streamlit (beta)

Want a quick local test-drive before using skills in your agent workflow?

```bash
pip install -r app/requirements.txt
streamlit run app/main.py
```

What you can do in v0.7:
- `Learn` setup and integration paths without leaving the app
- `Find My Skill` by describing your situation in plain English
- `Run Skills` with your own scenario once you know what you want

This beta interface is a feature in flight. Feedback is welcome via [GitHub Issues](https://github.com/deanpeters/Product-Manager-Skills/issues) or [LinkedIn](https://linkedin.com/in/deanpeters).

---

## ✅ Safety and Evaluation

Before using any skill:
- Review the skill file and any linked resources. If it includes `scripts/`, read them before running.
- Prefer least privilege. Skills should not require secrets or network access unless explicitly documented.
- Do a quick dry run with a realistic prompt, then refine `name` and `description` for better discoverability.
- Run `python3 scripts/check-skill-triggers.py --show-cases` before packaging if you want a quick trigger-readiness pass.

---

## 🧰 Optional Scripts (Deterministic Helpers)

Some skills include a `scripts/` folder with deterministic helpers for calculations or formatting. These are optional, should be audited before running, and should avoid network calls or external dependencies.

**Examples:**
- `skills/tam-sam-som-calculator/scripts/market-sizing.py`
- `skills/user-story/scripts/user-story-template.py`

---

## 🤖 Skill Creation Utility

**Want to create your own skills?** Choose one of these utilities:

- `scripts/add-a-skill.sh` - Content-first, AI-assisted generation from notes/frameworks.
- `scripts/build-a-skill.sh` - Guided "build-a-bear" wizard that prompts section-by-section.
- `scripts/find-a-skill.sh` - Search skills by name/type/keyword with ranked results.
- `scripts/find-a-command.sh` - Search commands by name/keyword/used skills.
- `scripts/run-pm.sh` - Fast runner for either a skill or a command.
- `scripts/test-a-skill.sh` - Run strict conformance checks and optional smoke checks.
- `scripts/check-skill-triggers.py` - Audit frontmatter descriptions and scenario prompts for Claude-style triggering.
- `scripts/test-library.sh` - Validate skills, commands, and regenerate catalogs.
- `scripts/zip-a-skill.sh` - Build upload-ready `.zip` files by skill, type, or all skills.
- `scripts/generate-catalog.py` - Regenerate skill/command navigation indexes.

**New to terminals?** See [`scripts/README.md`](scripts/README.md) for a plain-language walkthrough.
**Power users:** These scripts are designed to chain together into fast end-to-end workflows (idea -> prompt -> validation -> packaging).

**What it does:**
1. Analyzes your content and suggests skill types
2. Generates complete skill files with examples
3. Validates metadata for marketplace compliance
4. Updates documentation automatically

**Usage:**
```bash
# From a file
./scripts/add-a-skill.sh research/your-framework.md

# Guided wizard
./scripts/build-a-skill.sh

# Find a skill
./scripts/find-a-skill.sh --keyword pricing --type interactive

# Find a command
./scripts/find-a-command.sh --keyword roadmap

# Run a command workflow
./scripts/run-pm.sh command write-prd "Mobile onboarding redesign"

# Test one skill
./scripts/test-a-skill.sh --skill finance-based-pricing-advisor --smoke

# Test full library surface
./scripts/test-library.sh

# Build Claude upload zip for one skill
./scripts/zip-a-skill.sh --skill finance-based-pricing-advisor

# Build Claude upload zips for all skills
./scripts/zip-a-skill.sh --all --output dist/skill-zips

# Build Claude upload zips for one category (component|interactive|workflow)
./scripts/zip-a-skill.sh --type component --output dist/skill-zips

# Build curated starter pack
./scripts/zip-a-skill.sh --preset core-pm --output dist/skill-zips

# Show available curated presets
./scripts/zip-a-skill.sh --list-presets

# From clipboard
pbpaste | ./scripts/add-a-skill.sh

# Check available adapters
./scripts/add-a-skill.sh --list-agents
```

**Agent support:** Claude Code, Manual mode (works with any CLI), and custom adapters via `scripts/adapters/ADAPTER_TEMPLATE.sh`

**Learn more:** See [`docs/Add-a-Skill Utility Guide.md`](docs/Add-a-Skill%20Utility%20Guide.md) for complete guide.
**Cloning locally?** Start with [`docs/Building PM Skills.md#local-clone-quickstart`](docs/Building%20PM%20Skills.md#local-clone-quickstart).

---

## ✅ Claude Web Upload Checklist

- Keep frontmatter `name` <= 64 chars and `description` <= 200 chars.
- Use `intent` for the richer repo-facing explanation of the skill, while keeping `description` short and trigger-oriented.
- Ensure the skill folder name matches the `name` value.
- Use `scripts/zip-a-skill.sh --skill <skill-name>` (or `--type component`, `--preset core-pm`) to generate upload-ready ZIPs.
- (Advanced) Use `scripts/package-claude-skills.sh` if you need unpacked upload-ready folders.
- Validate metadata with `scripts/check-skill-metadata.py`.
- For GitHub ZIP upload flow, see [`docs/Using PM Skills with Claude.md`](docs/Using%20PM%20Skills%20with%20Claude.md#github-zip-install).

---

## 🏗️ Three-Tier Architecture (How Skills Work Together)

These 47 skills are organized into **three types** that build on each other:

```text
┌───────────────────────────────────────────────────────────┐
│  WORKFLOW SKILLS (6)                                      │
│  Complete end-to-end PM processes                         │
│  Example: "Run a product strategy session"                │
│  Timeline: 2-4 weeks                                      │
└───────────────────────────────────────────────────────────┘
                         ↓ orchestrates
┌───────────────────────────────────────────────────────────┐
│  INTERACTIVE SKILLS (20)                                  │
│  Guided discovery with adaptive questions                 │
│  Example: "Which prioritization framework should I use?"  │
│  Timeline: 30-90 minutes                                  │
└───────────────────────────────────────────────────────────┘
                         ↓ uses
┌───────────────────────────────────────────────────────────┐
│  COMPONENT SKILLS (21)                                    │
│  Templates for specific PM deliverables                   │
│  Example: "Write a user story"                            │
│  Timeline: 10-30 minutes                                  │
└───────────────────────────────────────────────────────────┘
```

### Component Skills (21) — Templates & Artifacts
**What:** Reusable templates for creating specific PM deliverables (user stories, positioning statements, epics, personas, PRDs, etc.)

**When to use:** You need a standard template or format for a specific deliverable.

**Example:** "Write a user story with acceptance criteria" → Use [`user-story.md`](skills/user-story/SKILL.md)

---

### Interactive Skills (20) — Guided Discovery
**What:** Multi-turn conversational flows where AI asks you 3-5 adaptive questions, then offers smart recommendations based on your context.

**When to use:** You need help deciding which approach to take or gathering context before executing.

**Example:** "Which prioritization framework should I use?" → Run [`prioritization-advisor.md`](skills/prioritization-advisor/SKILL.md), which asks about your product stage, team size, data availability, then recommends RICE, ICE, Kano, or other frameworks.

**How they work:**
1. AI asks 3-5 questions about your context
2. You answer (or pick from numbered options)
3. AI offers 3-5 tailored recommendations
4. You choose one (or combine approaches)
5. AI executes using the right component skills

---

### Workflow Skills (6) — End-to-End Processes
**What:** Complete PM processes that orchestrate multiple component and interactive skills over days/weeks.

**When to use:** You need to run a full PM workflow from start to finish (strategy session, discovery cycle, roadmap planning, PRD creation).

**Example:** "Align stakeholders on product strategy" → Run [`product-strategy-session.md`](skills/product-strategy-session/SKILL.md), which guides you through positioning → problem framing → solution exploration → roadmap planning over 2-4 weeks.

---

## 📦 All 47 Skills (Clickable)

Now that you understand the three types, here's the complete catalog:

### 🧱 Component Skills (21)

| Skill | Use When You Need To... |
|-------|-------------------------|
| **[altitude-horizon-framework](skills/altitude-horizon-framework/SKILL.md)** | Understand the PM→Director mindset shift: altitude (scope), horizon (time), four transition zones, failure modes, and the Cascading Context Map. Based on [The Product Porch E42](https://the-product-porch-43ca35c0.simplecast.com/episodes/from-product-manager-to-director-how-to-make-the-shift-part-1) |
| **[company-research](skills/company-research/SKILL.md)** | Deep-dive competitor or company analysis |
| **[customer-journey-map](skills/customer-journey-map/SKILL.md)** | Map customer experience across all touchpoints (NNGroup framework) |
| **[eol-message](skills/eol-message/SKILL.md)** | Communicate product/feature deprecation gracefully |
| **[epic-hypothesis](skills/epic-hypothesis/SKILL.md)** | Turn vague initiatives into testable hypotheses with success metrics |
| **[finance-metrics-quickref](skills/finance-metrics-quickref/SKILL.md)** | Fast lookup table for 32+ SaaS finance metrics with formulas, benchmarks, and when to use each |
| **[jobs-to-be-done](skills/jobs-to-be-done/SKILL.md)** | Understand what customers are trying to accomplish (JTBD framework) |
| **[pestel-analysis](skills/pestel-analysis/SKILL.md)** | Analyze external factors (Political, Economic, Social, Tech, Environmental, Legal) |
| **[pol-probe](skills/pol-probe/SKILL.md)** | Define lightweight, disposable validation experiments to test hypotheses before building (Dean Peters PoL framework) |
| **[positioning-statement](skills/positioning-statement/SKILL.md)** | Define who you serve, what problem you solve, and how you're different (Geoffrey Moore framework) |
| **[press-release](skills/press-release/SKILL.md)** | Write a future press release to clarify product vision (Amazon Working Backwards) |
| **[problem-statement](skills/problem-statement/SKILL.md)** | Frame a customer problem with evidence before jumping to solutions |
| **[product-sense-interview-answer](skills/product-sense-interview-answer/SKILL.md)** | Structure a spoken product-sense answer with assumptions, segmentation, pain-point prioritization, and MVP tradeoffs |
| **[proto-persona](skills/proto-persona/SKILL.md)** | Create hypothesis-driven personas before doing full research |
| **[recommendation-canvas](skills/recommendation-canvas/SKILL.md)** | Document AI-powered product recommendations |
| **[saas-economics-efficiency-metrics](skills/saas-economics-efficiency-metrics/SKILL.md)** | Evaluate unit economics and capital efficiency (CAC, LTV, payback, margins, burn rate, Rule of 40, magic number) |
| **[saas-revenue-growth-metrics](skills/saas-revenue-growth-metrics/SKILL.md)** | Calculate and interpret revenue, retention, and growth metrics (revenue, ARPU, MRR/ARR, churn, NRR, expansion) |
| **[storyboard](skills/storyboard/SKILL.md)** | Visualize user journeys with 6-frame narrative storyboards |
| **[user-story](skills/user-story/SKILL.md)** | Write user stories with proper acceptance criteria (Mike Cohn + Gherkin) |
| **[user-story-mapping](skills/user-story-mapping/SKILL.md)** | Organize stories by user workflow (Jeff Patton framework) |
| **[user-story-splitting](skills/user-story-splitting/SKILL.md)** | Break down large stories using 8 proven patterns |

---

### 🔄 Interactive Skills (20)

| Skill | What It Does |
|-------|--------------|
| **[acquisition-channel-advisor](skills/acquisition-channel-advisor/SKILL.md)** | Evaluate acquisition channels using unit economics, customer quality, and scalability. Recommends scale/test/kill decisions |
| **[ai-shaped-readiness-advisor](skills/ai-shaped-readiness-advisor/SKILL.md)** | Assess if you're "AI-first" (automating tasks) or "AI-shaped" (redesigning how you work). Evaluates 5 competencies and recommends which to build first |
| **[business-health-diagnostic](skills/business-health-diagnostic/SKILL.md)** | Diagnose SaaS business health using key metrics, identify red flags, and prioritize actions. Analyzes growth, retention, efficiency, and capital health |
| **[context-engineering-advisor](skills/context-engineering-advisor/SKILL.md)** | Diagnose context stuffing (volume without intent) vs. context engineering (structure for attention). Guides memory architecture, retrieval strategies, and Research→Plan→Reset→Implement cycle |
| **[customer-journey-mapping-workshop](skills/customer-journey-mapping-workshop/SKILL.md)** | Guides journey mapping with pain point identification |
| **[director-readiness-advisor](skills/director-readiness-advisor/SKILL.md)** | Coaches PMs and new Directors through the transition across four situations: preparing, interviewing, newly landed, recalibrating. Based on [The Product Porch E42](https://the-product-porch-43ca35c0.simplecast.com/episodes/from-product-manager-to-director-how-to-make-the-shift-part-1) |
| **[discovery-interview-prep](skills/discovery-interview-prep/SKILL.md)** | Plans customer interviews (Mom Test style) based on your research goals |
| **[epic-breakdown-advisor](skills/epic-breakdown-advisor/SKILL.md)** | Splits epics into user stories using Richard Lawrence's 9 patterns |
| **[feature-investment-advisor](skills/feature-investment-advisor/SKILL.md)** | Evaluate feature investments using revenue impact, cost structure, ROI, and strategic value. Delivers build/don't build recommendations |
| **[finance-based-pricing-advisor](skills/finance-based-pricing-advisor/SKILL.md)** | Evaluate pricing changes using financial impact analysis (ARPU/ARPA, conversion, churn risk, NRR, payback) |
| **[lean-ux-canvas](skills/lean-ux-canvas/SKILL.md)** | Sets up hypothesis-driven planning (Jeff Gothelf Lean UX Canvas v2) |
| **[opportunity-solution-tree](skills/opportunity-solution-tree/SKILL.md)** | Generates opportunities and solutions, recommends best proof-of-concept to test |
| **[pol-probe-advisor](skills/pol-probe-advisor/SKILL.md)** | Recommends which of 5 prototype types to use based on your hypothesis and risk (Feasibility, Task-Focused, Narrative, Synthetic Data, Vibe-Coded) |
| **[positioning-workshop](skills/positioning-workshop/SKILL.md)** | Guides you through defining your positioning with adaptive questions |
| **[prioritization-advisor](skills/prioritization-advisor/SKILL.md)** | Recommends the right prioritization framework (RICE, ICE, Kano, etc.) for your situation |
| **[problem-framing-canvas](skills/problem-framing-canvas/SKILL.md)** | Leads you through MITRE Problem Framing (Look Inward/Outward/Reframe) |
| **[tam-sam-som-calculator](skills/tam-sam-som-calculator/SKILL.md)** | Projects market size (TAM/SAM/SOM) with real-world data and citations |
| **[user-story-mapping-workshop](skills/user-story-mapping-workshop/SKILL.md)** | Walks you through creating story maps with backbone and release slices |
| **[vp-cpo-readiness-advisor](skills/vp-cpo-readiness-advisor/SKILL.md)** | Coaches Directors and executives through the VP/CPO transition — includes CEO interview framework for evaluating roles before accepting. Based on [The Product Porch E43](https://the-product-porch-43ca35c0.simplecast.com/episodes/becoming-a-vp-cpo-leading-product-at-the-executive-level-part-2) |
| **[workshop-facilitation](skills/workshop-facilitation/SKILL.md)** | Adds one-step-at-a-time facilitation with numbered recommendations for workshop skills |

---

### 🎭 Workflow Skills (6)

| Skill | What It Does | Timeline |
|-------|--------------|----------|
| **[discovery-process](skills/discovery-process/SKILL.md)** | Complete discovery cycle: frame problem → research → synthesize → validate solutions | 3-4 weeks |
| **[executive-onboarding-playbook](skills/executive-onboarding-playbook/SKILL.md)** | 30-60-90 day diagnostic playbook for VP/CPO transitions: diagnose before acting, surface unwritten strategy, assess people, act with evidence. Based on [The Product Porch E43](https://the-product-porch-43ca35c0.simplecast.com/episodes/becoming-a-vp-cpo-leading-product-at-the-executive-level-part-2) | 90 days |
| **[prd-development](skills/prd-development/SKILL.md)** | Structured PRD: problem statement → personas → solution → metrics → user stories | 2-4 days |
| **[product-strategy-session](skills/product-strategy-session/SKILL.md)** | Full strategy: positioning → problem framing → solution exploration → roadmap | 2-4 weeks |
| **[roadmap-planning](skills/roadmap-planning/SKILL.md)** | Strategic roadmap: gather inputs → define epics → prioritize → sequence → communicate | 1-2 weeks |
| **[skill-authoring-workflow](skills/skill-authoring-workflow/SKILL.md)** | Meta workflow: choose add/build path → validate conformance → update docs → package/publish | 30-90 minutes |

<a id="future-skills"></a>
### 🔮 Agent Skills of the Future

**_Possible skills in development:_**

- **Dangerous Animals of Product Management** - Feature hostage negotiations and stakeholder shuttle diplomacy for when you're facing HiPPOs, RHiNOs, and WoLFs (_oh my!_).
- **Pricing for Product Managers** - Value-based pricing, packaging strategy, price increases, and grandfather clause negotiations without the panic spiral and flop sweat.
- **Classic Business Strategy Frameworks** - Ansoff, BCG, Porter's 5 Forces, Blue Ocean, and SWOT in agent-ready format that helps you decide, not decorate slides.
- **Storytelling for Product Managers** - Narrative arc, demo choreography, and pitch structure built on pro-opera lessons and Hakawati orations for commanding the room.
- **Prompt Building for Product Managers** - Industrial-strength prompt engineering: team session starters, multi-turn workflow wizards, and reverse engineering templates for artifacts like PRDs.
- **Nightmares of Product Management** - Telemetry, triage, and tactics for when things don't go as planned: adoption theater, feature graveyards, metric manipulation, launch amnesia, technical debt wildfires. Plus prevention strategies.

Detailed concept notes live in [`PLANS.md`](PLANS.md#future-skill-candidates).

---

## 🚀 How to Use

**Confused by setup options?** Start here: [PM Skills Rule-of-Thumb Guide](docs/PM%20Skills%20Rule-of-Thumb%20Guide.md).

### Fastest Path (Local Repo)

```bash
# Skill mode
./scripts/run-pm.sh skill user-story "Checkout improvements for returning customers"

# Command mode
./scripts/run-pm.sh command plan-roadmap "Q3-Q4 roadmap for enterprise reporting"
```

Command definitions live in [`commands/`](commands/README.md), and generated browse indexes live in [`catalog/`](catalog/README.md).

### With Claude Desktop or Claude.ai

1. Open a conversation with Claude
2. Share the skill file: "Read user-story.md"
3. Ask Claude to apply it: "Using the User Story skill, write stories for our checkout flow"

### With Claude Code (CLI)

```bash
cd product-manager-skills
claude "Using the PRD Development workflow, create a PRD for our mobile feature"
```

You can discover via `npx skills find <query>` and `npx skills add deanpeters/Product-Manager-Skills --list`, then install for Claude Code. See [Using PM Skills with Claude](docs/Using%20PM%20Skills%20with%20Claude.md).

### With OpenAI Codex

Use local workspace paths, GitHub-connected Codex on ChatGPT, or discover/install directly with `npx skills`. See [Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md).

### With ChatGPT

Use GitHub app connections (formerly connectors), Custom GPT Knowledge uploads, or Project files. See [Using PM Skills with ChatGPT](docs/Using%20PM%20Skills%20with%20ChatGPT.md).

### With Cowork or Other Agents

**Cowork:** Import skills as knowledge modules, invoke via natural language.
**Other agents:** Follow your agent's docs for loading custom knowledge.

---

## 📄 Docs

- **[Using PM Skills 101](docs/Using%20PM%20Skills%20101.md)** — Beginner-friendly orientation for PMs who want clear setup without technical overload.
- **[Using PM Skills with Claude](docs/Using%20PM%20Skills%20with%20Claude.md)** — Claude Code usage plus GitHub ZIP upload steps for Claude Desktop/Web.
- **[Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md)** — Local workspace usage plus GitHub-connected Codex on ChatGPT.
- **[Using PM Skills with ChatGPT](docs/Using%20PM%20Skills%20with%20ChatGPT.md)** — GitHub app connection, Custom GPT Knowledge setup, and Project-based usage.
- **[Platform Guides for PMs](docs/Platform%20Guides%20for%20PMs.md)** — Tool-by-tool setup chooser for Claude Code, Codex, OpenClaw, Cowork, Claude Desktop, ChatGPT Desktop, n8n, LangFlow, and Python agents.
- **[Using PM Skills with Claude Code](docs/Using%20PM%20Skills%20with%20Claude%20Code.md)** — PM-focused quickstart for Claude Code users.
- **[Using PM Skills with Slash Commands 101](docs/Using%20PM%20Skills%20with%20Slash%20Commands%20101.md)** — Turn PM skills into reusable Claude slash commands like `/pm-story` and `/pm-prd`.
- **[Using PM Skills with Claude Desktop](docs/Using%20PM%20Skills%20with%20Claude%20Desktop.md)** — Skill upload workflow for non-technical desktop users.
- **[Using PM Skills with ChatGPT Desktop](docs/Using%20PM%20Skills%20with%20ChatGPT%20Desktop.md)** — Project-first setup for desktop-based PM work.
- **[Using PM Skills with n8n](docs/Using%20PM%20Skills%20with%20n8n.md)** — Practical automation patterns for repeatable PM workflows.
- **[Using PM Skills with LangFlow](docs/Using%20PM%20Skills%20with%20LangFlow.md)** — Visual workflow setup using skill-guided prompt templates.
- **Additional harness guides:** [Cursor](docs/Using%20PM%20Skills%20with%20Cursor.md), [Windsurf](docs/Using%20PM%20Skills%20with%20Windsurf.md), [Bolt](docs/Using%20PM%20Skills%20with%20Bolt.md), [Replit Agent](docs/Using%20PM%20Skills%20with%20Replit%20Agent.md), [Make.com](docs/Using%20PM%20Skills%20with%20Make.com.md), [Devin](docs/Using%20PM%20Skills%20with%20Devin.md), [CrewAI](docs/Using%20PM%20Skills%20with%20CrewAI.md), [Gemini](docs/Using%20PM%20Skills%20with%20Gemini.md)
- **[Start Here](START_HERE.md)** — One-page "do this now" onboarding for skills and commands.
- **[Commands](commands/README.md)** — Command format, command list, validation, and discovery.
- **[Catalog Artifacts](catalog/README.md)** — Generated skill/command indexes for fast navigation.
- **[PM Skills Rule-of-Thumb Guide](docs/PM%20Skills%20Rule-of-Thumb%20Guide.md)** — Non-technical setup choices (local repo vs ZIP vs app connections) in plain English.
- **[Marketplace Strategy](MARKETPLACE_STRATEGY.md)** — PM-friendly strategy for distributing skills in marketplaces.
- **[Marketplace Submission Runbook](docs/Marketplace%20Submission%20Runbook.md)** — Step-by-step submission workflow for non-technical teams.
- **[Marketplace Issue Templates](docs/Marketplace%20Issue%20Templates.md)** — Reusable issue templates for marketplace execution and tracking.
- **[PM Tooling Operations Charter](docs/PM%20Tooling%20Operations%20Charter.md)** — Pedagogic operating stack across M365 Copilot, Codex, ChatGPT, VS Code/Copilot, Cursor, n8n, and Lovable.
- **[Add-a-Skill Utility Guide](docs/Add-a-Skill%20Utility%20Guide.md)** — End-to-end automation guide for generating and validating new skills.
- **[Building PM Skills](docs/Building%20PM%20Skills.md)** — How we distill sources into agent-ready PM skills.

---

## 💼 Real-World Use Cases

### "I need to align stakeholders on product strategy"
→ **Workflow:** [`product-strategy-session`](skills/product-strategy-session/SKILL.md) (2-4 weeks, orchestrates positioning → roadmap)

### "I need to validate a customer problem before building"
→ **Workflow:** [`discovery-process`](skills/discovery-process/SKILL.md) (3-4 weeks, interviews → synthesis → validation)

### "I need to test a hypothesis quickly before investing in development"
→ **Interactive:** [`pol-probe-advisor`](skills/pol-probe-advisor/SKILL.md) (recommends which prototype type: Feasibility, Task-Focused, Narrative, Synthetic Data, or Vibe-Coded)
→ **Component:** [`pol-probe`](skills/pol-probe/SKILL.md) (template for documenting validation experiments)

### "I want to know if I'm using AI strategically or just for efficiency"
→ **Interactive:** [`ai-shaped-readiness-advisor`](skills/ai-shaped-readiness-advisor/SKILL.md) (assesses 5 competencies: Context Design, Agent Orchestration, Outcome Acceleration, Team-AI Facilitation, Strategic Differentiation)

### "I'm pasting entire docs into AI and getting vague responses"
→ **Interactive:** [`context-engineering-advisor`](skills/context-engineering-advisor/SKILL.md) (diagnose context stuffing vs. engineering, define boundaries, implement Research→Plan→Reset→Implement cycle)

### "I need to write a PRD for a new feature"
→ **Workflow:** [`prd-development`](skills/prd-development/SKILL.md) (2-4 days, problem → solution → stories)

### "I need to create a Q2 roadmap"
→ **Workflow:** [`roadmap-planning`](skills/roadmap-planning/SKILL.md) (1-2 weeks, epics → prioritization → sequencing)

### "I need to choose a prioritization framework"
→ **Interactive:** [`prioritization-advisor`](skills/prioritization-advisor/SKILL.md) (asks questions, recommends RICE/ICE/Kano)

### "I need to split a large epic"
→ **Interactive:** [`epic-breakdown-advisor`](skills/epic-breakdown-advisor/SKILL.md) (Richard Lawrence's 9 patterns)

### "I need to write a user story"
→ **Component:** [`user-story`](skills/user-story/SKILL.md) (template + examples)

---

## 💡 Why Skills Beat Prompts

| Prompts | Skills |
|---------|--------|
| One-time instructions per task | Reusable frameworks learned once |
| "Write a PRD for X" | Agent knows PRD structure, asks smart questions, handles edge cases |
| You repeat yourself constantly | Agent remembers best practices |
| Inconsistent outputs | Consistent, professional results |

**Skills = Less explaining, more strategic work.**

---

## 🌟 What Makes These Skills Different

### ✅ Battle-Tested Frameworks
Built on proven methods from Geoffrey Moore, Jeff Patton, Teresa Torres, Amazon, Richard Lawrence, MITRE, and more.

### ✅ Real Client Work
Based on decades of PM consulting across healthcare, finance, manufacturing, and tech.

### ✅ Agent-Ready Format
Optimized for AI comprehension—not blog posts, not books, not courses. **Executable frameworks.**

### ✅ Zero Fluff
Every word earns its keep. No filler, no buzzwords, no generic advice.

### ✅ Example-Rich
Shows both "good" and "bad" examples so you know what works and what to avoid.

---

## 📚 Skill Structure (What's Inside Each File)

Every skill follows the same format:

```
## Purpose
What this skill does and when to use it.

## Key Concepts
Core frameworks, definitions, anti-patterns.

## Application
Step-by-step instructions (with examples).

## Examples
Real-world cases (good and bad).

## Common Pitfalls
What to avoid and why.

## References
Related skills and external frameworks.
```

**Clean. Practical. Zero fluff.**

---


## 🎓 Philosophy

**Principles:**
- **Outcome-driven** over output-driven (solve problems, don't just ship features)
- **Evidence over vibes** (validate with data, not opinions)
- **Clarity beats completeness** (simple and usable beats comprehensive and confusing)
- **Examples beat explanations** (show, don't just tell)

**No hype. No buzzwords. Just frameworks that work.**

---
