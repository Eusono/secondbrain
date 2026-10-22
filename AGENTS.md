# Master Constitution (`AGENTS.md`)

Welcome to the Second Brain workspace. This repository is a unified, vendor-neutral repository of knowledge, rules, and memory that travels with you across devices and AI interfaces.

---

## Core Principle

> **The chat forgets; files don't.**
> Conversations compact and vanish. Nothing durable may live only in a temporary chat thread. Everything worth keeping becomes a file in this repository during the same session in which it occurred. Every folder is a topic; its context file (`AGENTS.md`) is the topic's living knowledge. Dated session-log entries compound into durable knowledge over time. This repository is the single source of truth.

---

## How Context Works

- **One Brain, Many Agents:** This workspace is tool-neutral. Whether using Google Antigravity, Gemini CLI, Claude Code, Codex, or Cursor, every agent reads and writes to the exact same files.
- **The Symlink Convention:** `AGENTS.md` is the primary master content file for every directory. To ensure compatibility, `GEMINI.md` and `CLAUDE.md` in each folder are symlinks pointing directly to `AGENTS.md`. Every agent loads the exact same context. Edit the content once; every agent sees it.
- **Auto-loading Folder Context:** When operating in a specific directory, the agent must load and respect that directory's `AGENTS.md` (and its parent-level constitutions) to obtain the topic's state, boundaries, and session logs.

---

## Routing Table

| Target / Subject | Owning Path | Scope & Routing Purpose |
| :--- | :--- | :--- |
| **Personal Knowledge** | `personal/` | Personal life tracking, projects, logs, health, and aspirations. |
| **Professional Work** | `work/` | Technical tickets, projects, runbooks, incidents, and career notes. |
| **Overlay Code Repos** | `work/code/` & `personal/code/` | Gitignored code repos & scripts; branding-free, no knowledge files. |
| **Lab & Prototypes** | `lab/` | Coding experiments, technical research, and playground activities. |
| **Durable Memories** | `memory/` | Cross-cutting facts, entity indices, and permanent memory logs. |
| **Skills & Rituals** | `skills/` & `skills/rituals/` | Automation rituals, how-to guides, lessons learned, and security scans. |
| **Dashboard & Audit Engine** | `_meta/` | Stats, linter, health audit, environment ledger, and web control center. |

---

## Precedence Table: Single Source of Truth

| Fact Class | Owning Store (Single Source of Truth) | Reconcile & Update Rule |
| :--- | :--- | :--- |
| **Operating Rules & Hard Constraints** | `constraints.md` | Updated exclusively via co-editing contract (`## Log`). |
| **Machine Tools, Ports, Jobs & Credentials** | `_meta/environment.json` | Updated via machine ledger and environment audit scripts. |
| **Current State of a Topic / Project** | That topic's context file (`work/AGENTS.md`, `work/<ticket>.md`) | Updated during active work in that topic folder. |
| **Live Code Repos & Configs** | `work/code/<repo>/` (Git repo itself) | Brain holds pointers & knowledge in `work/`, never copies. |
| **Live Systems & Infrastructure State** | The live system itself (queried read-only) | Live query overrides offline claims. |

---

## Context Split: Expertise vs. Situational

To ensure maximum context efficiency and prevent prompt bloat, context is split into two tiers:

1. **Expertise Context (Always Loaded — Keep Lean):**
   - Root `AGENTS.md`, `constraints.md`, `memory/MEMORY.md`, and the active working folder's `AGENTS.md`.
   - *Target Size:* Stays flat over time (< 45KB).

2. **Situational Context (Fetched On Demand):**
   - Historical archives, runbooks, idea boards, tickets, and detail pages.
   - *Target Size:* Grows without limit as documents accumulate, reached via routing and targeted search.


## Retrieval Rules & The Lesson-to-Memory Funnel

- **Search first:** Before investigating something this brain already tracks, search existing notes and cross-link old and new records in both directions.
- **Two-Stage Lesson $\rightarrow$ Memory Funnel:**
  - **Stage 1 — Lessons (`skills/lessons.md`):** Chronological incident post-mortems and troubleshooting narratives (*What bit me / Why it happened / The fix*). Every lesson must end with either `- **Promoted to:** [[path]]` or `- **Disposition:** ledger-only`.
  - **Stage 2 — Living System Cards & Skills (`memory/system_*.md` or `skills/<name>/SKILL.md`, indexed in `memory/MEMORY.md`):** Standing entity facts, architecture, and reusable operational recipes (how to authenticate, query APIs, use custom fields/transitions, and avoid system-specific gotchas). Because `memory/MEMORY.md` is part of the startup kernel, indexing core systems in `memory/MEMORY.md` prevents repeatedly reverse-engineering scripts or re-triggering known API/CLI errors.
- **In-Turn Script-Archeology & Error Trigger:** Whenever the agent has to inspect local scripts to rediscover how to call an API/tool, or resolves a non-obvious API/CLI schema, field, or transition error, it must update the owning `memory/system_*.md` card (or `skills/<name>/SKILL.md` + `memory/MEMORY.md` pointer) in the same turn without waiting to be asked.
---

## Voice and Prose Rules

- **Write in first person:** Everything in this brain is written in the first person ("I", "my", "me").
- **Neutral, clean voice:** Keep prose simple, declarative, and clear. Avoid fluff, unnecessary adjectives, or robotic AI phrasing.
- **No AI attribution:** Do not attribute changes to specific AI assistants. All commits and file additions represent my own thoughts and actions.

---

## Imports

Adhere to the living contract and permanent memory index defined in:
@./constraints.md
@./memory/MEMORY.md

If a harness displays either `@` import literally instead of expanding it at session start, open both `constraints.md` and `memory/MEMORY.md` on Turn 1 before running any tool.
