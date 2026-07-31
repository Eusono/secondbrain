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

### Step 5: Log Flywheel Lessons
- If something surprised you or cost time, write one clean dated block in `skills/lessons.md` (newest on top). If everything went as expected, write nothing.

### Step 6: File Cross-Cutting Memories
- Create slug-named files in `memory/<slug>.md` for new cross-cutting facts and register in `memory/MEMORY.md`.

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
