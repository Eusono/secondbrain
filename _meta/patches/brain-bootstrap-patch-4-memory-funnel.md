# Brain bootstrap: patch 4 (Two-Stage Lesson -> Memory Funnel)

**What this is:** a focused one-shot upgrade prompt for an existing Second Brain (whether or not Patch 3 was already applied). It fixes the "write-only lesson / empty Turn-0 memory index" trap where reusable API contracts, CLI flags, customfield IDs, and system gotchas pile up inside chronological `skills/lessons.md` or local scripts while `memory/MEMORY.md` (the only index loaded at Turn 0 of every session) stays restricted to static people/location notes.

**How to use it:** open a terminal at your brain's root, start your assistant, and paste everything below the line. It works with both architectures:
- **Script-centric brains** (where helper tools live in `bin/*.py` or `work/code/`), and
- **Skill-centric brains** (where domain CLIs and manuals live in `skills/<name>/SKILL.md` and `skills/<name>/scripts/`).

---

You are applying **Brain Bootstrap Patch 4 (The Two-Stage Lesson -> Memory Funnel)** to the Second Brain workspace in the current directory.

## Why this patch exists

Two independent audits of production Second Brains revealed the same failure mode:
1. **`memory/MEMORY.md` is Turn-0 startup context (`portable-core`),** but Step 6 of `/checkpoint` restricted `memory/` to *"only for cross-cutting facts no topic folder owns."* Because almost all technical work starts inside a ticket, project, or skill folder, `memory/` stayed nearly empty (mostly people and location directories) and never indexed the user's core operational systems.
2. **`skills/lessons.md` is NOT loaded at Turn 0,** yet it accumulates dozens of high-value API contracts, CLI quirks, auth requirements, and field mappings (`35–85 KB` of chronological text). On a new chat turn, unless the agent happens to run a search matching the exact words in `skills/lessons.md`, those lessons are invisible—forcing the agent to either reverse-engineer local Python/shell scripts from scratch or re-trigger the exact same `HTTP 400` / wrong-field bugs solved weeks earlier.
3. **Prose rules without a mechanical linter check drift.** Saying *"promote reusable lessons"* in prose fails unless `_meta/brain-lint.py` (or `_meta/brain-health.py`) mechanically requires every dated lesson in `skills/lessons.md` to declare either `- **Promoted to:** [[target]]` or `- **Disposition:** ledger-only`.

## Ground rules

1. **Survey before touching.** Read root `AGENTS.md` / `CLAUDE.md`, `constraints.md`, `memory/MEMORY.md`, `skills/lessons.md`, `skills/rituals/checkpoint.md` (and `skills/rituals/scope.md` if present), `bin/`, `skills/`, and `_meta/`.
2. **Respect Single Source of Truth (do not duplicate manuals):**
   - If this brain already keeps per-tool manuals in `skills/<name>/SKILL.md`, promote tool-specific API/CLI gotchas from `skills/lessons.md` directly into a `## API & CLI Gotchas` section inside the owning `skills/<name>/SKILL.md` (and update any skill manifest hash / run `skillspector` if required by this repo), then create a single `memory/system_skill_router.md` card in `memory/` mapping each core tool to its `SKILL.md` and CLI entrypoint, plus `memory/system_*.md` cards only for cross-cutting contracts that have no single `SKILL.md` owner.
   - If this brain keeps scripts in `bin/` or `work/code/` without per-tool `SKILL.md` manuals, create concise (`30–60` line) `memory/system_<name>.md` cards in `memory/` for the 5–8 core systems/APIs the owner operates.
3. **Never write secret values.** Reference only non-secret vault key paths, environment variable names, or wrapper commands (`Vault Pointer:`), never tokens, passwords, or `.env` values.

## Step 1: Guarantee Turn-0 Kernel Loading

1. Check root `AGENTS.md` / `CLAUDE.md` (and `.cursor/rules/*.mdc` if Cursor is used):
   - Ensure both `@./constraints.md` and `@./memory/MEMORY.md` are imported.
   - Add the explicit fallback rule: *"If the active harness displays `@` imports as literal text instead of expanding them at Turn 0, open `constraints.md` and `memory/MEMORY.md` on Turn 1 before running any tool."*

## Step 2: Distill Reusable Operational Rules from `skills/lessons.md` & Local Scripts

1. Scan every dated entry in `skills/lessons.md` (and `skills/lessons-archive.md` if present) plus the helper scripts in `bin/` or `skills/*/scripts/`.
2. Classify each dated lesson as either:
   - **Reusable system/API/CLI/architecture contract:** Promote the rule into its owning `skills/<name>/SKILL.md` (if a skill owns that tool) or into a concise, secret-free `memory/system_<name>.md` card (if cross-cutting or script-based), and append `- **Promoted to:** [[path]]` at the bottom of that lesson in `skills/lessons.md`.
   - **One-off incident, UI, document-export, or hardware post-mortem:** Keep it in the ledger and append `- **Disposition:** ledger-only` at the bottom of that lesson in `skills/lessons.md`.
3. Update the `## Formatting Lessons` template at the top of `skills/lessons.md` so the 4th bullet is:
   `- **Promoted to:** [[memory/system_<name>.md]] (or - **Disposition:** ledger-only)`
4. Register every new `memory/*.md` card in `memory/MEMORY.md` with **exactly one line per file** (`- [[memory/<slug>.md]]: <concise 1-line summary>`), verifying that `memory/MEMORY.md` stays well within any configured byte/token budget.

## Step 3: Update `AGENTS.md` and `skills/rituals/checkpoint.md`

1. In root `AGENTS.md` (under `## Retrieval Rules`), add:
   - **Two-Stage Lesson -> Memory Funnel:** `skills/lessons.md` captures chronological post-mortems (*What bit me / Why / Fix*), while `memory/system_*.md` and `skills/<name>/SKILL.md` (indexed via `memory/MEMORY.md`) hold living operational contracts visible from Turn 0.
   - **In-Turn Script-Archeology & Error Trigger:** Whenever you have to inspect `bin/` or skill scripts to rediscover how to call an API/tool, or resolve a non-obvious API/CLI schema, customfield, or transition error (`HTTP 400`), update the owning `memory/system_*.md` card or `skills/<name>/SKILL.md` in the same turn without waiting to be asked.
2. In `skills/rituals/checkpoint.md` (Steps 4–6, and `skills/rituals/scope.md` if present):
   - Require every new lesson in `skills/lessons.md` to include `- **Promoted to:** [[path]]` or `- **Disposition:** ledger-only` in the same checkpoint.
   - Replace the passive *"only for cross-cutting facts no folder owns"* memory rule with an **Active 3-Question Harvest**:
     1. *Did we discover or look up a reusable API/CLI/script contract or customfield/transition rule today?* -> Upsert `memory/system_*.md` (or `skills/<name>/SKILL.md` + router pointer).
     2. *Did we establish a durable architecture, topology, or site fact inside a ticket that outlives the ticket?* -> Upsert the owning `memory/` card.
     3. *Did we learn a new stakeholder role, team boundary, or escalation contact?* -> Upsert the owning `memory/` card and `memory/MEMORY.md` index line.

## Step 4: Add Mechanical Linter Enforcement (`lesson_promotion_missing`)

1. In `_meta/brain-lint.py` (and/or `_meta/brain-health.py`), add a check over `skills/lessons.md` (ignoring fenced code blocks) that inspects every dated `### YYYY-MM-DD — ...` entry and flags `lesson_promotion_missing` if the entry has neither `- **Promoted to:** [[...]]` nor `- **Disposition:** ledger-only` (and verify that any `[[...]]` target on `Promoted to:` resolves to an existing file).
2. If `_meta/rotate-lessons.py` exists, ensure it warns or refuses to archive a lesson that lacks a `Promoted to:` or `Disposition:` line.
3. Add a unit test in `_meta/tests/` verifying that an unannotated lesson fails the linter and an annotated lesson (`Promoted to:` or `Disposition: ledger-only`) passes.

## Step 5: Validate & Report

1. Run `git add -N memory/*.md` on any newly created memory files so `brain-search.py` (which indexes `git ls-files`) indexes them immediately.
2. Run the linter (`_meta/brain-lint.py` / `_meta/brain-health.py`), context budget (`_meta/context-budget.py`), any skill manifest/security checks, and the unit test suite.
3. Run `python3 _meta/brain-search.py` on 3–4 queries covering the promoted system rules and verify that the living `memory/system_*.md` or `skills/<name>/SKILL.md` files rank cleanly.
4. Report the summary of promoted lessons, new memory cards, linter/test results, and 3 example commands the owner can run to see the difference.
