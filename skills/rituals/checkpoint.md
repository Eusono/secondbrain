# Ritual: Checkpoint (`skills/rituals/checkpoint.md`)

The checkpoint ritual is a thorough, structured, session-ending sweep that transitions active, fluid thoughts into permanent, structured knowledge before disconnecting.

Run this ritual near the end of a session or day.

---

## Checkpoint Checklist

Follow these 11 steps in exact sequence:

### Step 0: Pull Upstream Sync
- Verify the repository status.
- If clean, run `git pull --rebase` to integrate upstream updates.

### Step 1: Log Active Changes & Discoveries
- Append dated log entry under the relevant area folder's `AGENTS.md` (`personal/`, `work/`, `lab/`) under `## Session log`.
- **Format:** `### YYYY-MM-DD — [Topic Title]` followed by concise, bulleted details. Newest logs go on top.

### Step 1b: Report Activation
- Name which existing lessons learned or durable memories were consulted or applied during this session.

### Step 2: Triage the Inbox
- Move stray notes or uncategorized items to `_inbox/` with a one-line explanation.

### Step 3: Refresh Current State
- Update the **"In Flight"** list in root `README.md` to reflect active or completed projects.

### Step 4: Extract Operational Skills
- If a recurring how-to pattern emerged, create or update a runbook under `work/runbooks/` or `skills/`.

### Step 5: Log Flywheel Lessons & Promote Standing Rules
- If something surprised you or cost time, write one clean dated block in `skills/lessons.md` (newest on top). If everything went as expected, write nothing.
- Every dated lesson in `skills/lessons.md` MUST end with either `- **Promoted to:** [[path]]` (when the lesson reveals a reusable API/CLI/system rule that was added to `memory/system_*.md` or `skills/<name>/SKILL.md`) or `- **Disposition:** ledger-only` (for one-off incident/UI/hardware findings). `_meta/brain-health.py` / `_meta/brain-lint.py` enforces this mechanically.

### Step 6: Consolidate Cross-Cutting Memories (Active 3-Question Harvest)
- Re-read `memory/MEMORY.md` first, then run this 3-question harvest across the session's work:
  1. **System & Tooling Recipes (`memory/system_*.md` or `skills/<name>/SKILL.md`):** Did we have to look up how a local script, API endpoint, customfield ID, workflow transition, or CLI flag works today, or solve a non-obvious API/CLI error? If yes, upsert the owning system card and ensure it is indexed in `memory/MEMORY.md`.
  2. **Architecture & Topology:** Did we establish a durable site, service, or architecture fact inside a task/ticket that will still matter after the ticket closes? If yes, upsert the owning `memory/` card.
  3. **People, Teams & Responsibilities:** Did we learn a new stakeholder role, escalation contact, or team boundary? If yes, upsert the owning `memory/` card and register any new file with a single line in `memory/MEMORY.md`.
### Step 7: Report Actions & Perform State Grep
- Report exact files touched and run a search (`grep`) across the repository to verify no file claims obsolete state.

### Step 7b: Run Health Audit & Linter
- Execute the health audit: `python3 _meta/brain-health.py --quick`. Resolve any findings immediately.

### Step 7c: Execute SkillSpector Security Scan
- Run `python3 _meta/skillspector.py` to inspect all AI skills for prompt injection, credential leaks, or exfiltration risks. Ensure all maintain **SAFE** or **LOW** scores.

### Step 8: Capture Growth Statistics & Regenerate Dashboard
- Execute `python3 _meta/brain-stats.py` to log metrics.
- Execute `python3 _meta/brain-dashboard.py` to regenerate the offline control center.

### Step 9: Sweep Agent-Private Memory Store
- Verify no facts live solely inside vendor-private stores.

### Step 10: Routing-Bug Reflex
- If the brain missed something, fix the index or routing table so future sessions find it automatically.

### Step 11: Commit and Push
- Execute a clean git commit:
  - **Format:** Conventional Commits (`type(scope): summary`).
  - **Voice:** First person (`docs(checkpoint): update session logs and dashboard`).
  - **Attribution:** Strictly **no** AI attribution trailers or Co-Authored-By flags.
- Run `git push` to upload changes to origin.
