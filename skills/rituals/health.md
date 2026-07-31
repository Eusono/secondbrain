# Ritual: Health Audit (`skills/rituals/health.md`)

The health audit ritual verifies workspace integrity, checks context budgets, verifies wikilinks, and ensures zero broken references.

---

## Commands

* **Quick Audit:** `python3 _meta/brain-health.py --quick`
* **Full Audit:** `python3 _meta/brain-health.py --full`

---

## Verification Targets

1. **Context Budget:** Ensures always-loaded Expertise Context (`AGENTS.md`, `constraints.md`, `memory/MEMORY.md`) stays under 45,000 bytes.
2. **Conflict Markers:** Checks for unmerged git conflict markers (`<<<<` + `<<<`).
3. **Unrouted Folders:** Checks if top-level folders exist that are missing from the Routing Table in `AGENTS.md`.
4. **Link Integrity:** Verifies all `file:///` and `[[wiki]]` links point to existing files.
