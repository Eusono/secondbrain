# Lessons Flywheel (`skills/lessons.md`)

This file is a compounding ledger of technical and operational gotchas, unexpected surprises, and hard-learned truths. It represents the "flywheel" of the Second Brain—ensuring that once a mistake or bug is solved, it is documented here so it is never repeated.

---

## Formatting Lessons

Each lesson must be appended to the top of the log (newest on top) under a dated heading in the following format:

```markdown
### YYYY-MM-DD — [Brief title of the gotcha]
- **What bit me:** What unexpected behavior or bug occurred?
- **Why it happened:** What was the underlying root cause?
- **The fix/prevention:** How was it solved, and how do we prevent it in the future?
```

---

## Lessons Log

### 2026-07-31 — Strictly Prohibit Git Commit and Push Outside /Checkpoint
- **What bit me:** Executing `git commit` and `git push` during intermediate script fixes or prompt turns violated user constraints and created unwanted micro-commits.
- **Why it happened:** Assuming code or dashboard edits required immediate remote git synchronization instead of remaining staged/unstaged in the local working tree until session end.
- **The fix/prevention:** Never run `git commit` or `git push` during regular task execution. Leave all working modifications in the local workspace tree; allow the session-ending `/checkpoint` ritual to handle all commits and pushes exclusively.

### 2026-07-31 — Structural Validation is Not Value Validation
- **What bit me:** A configuration file or template that parses cleanly with zero syntax errors can still cause catastrophic operational failure at runtime.
- **Why it happened:** Schema validation verifies formatting and syntax structure, but cannot check if referenced hostnames, IP subnets, or API keys actually exist or are valid.
- **The fix/prevention:** Remember schema-valid ≠ true. Always perform functional or empirical runtime validation beyond static schema parsing.
