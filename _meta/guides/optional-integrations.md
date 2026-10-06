# Optional integrations

[Back to the README](../../README.md)

These examples are optional, not prerequisites for using the workspace. The original prompt bodies are preserved below for deliberate use; reading this guide does not require running them or installing an integration.

## SkillSpector-inspired scanning

[NVIDIA SkillSpector](https://github.com/nvidia/skillspector) is the inspiration for the local [`_meta/skillspector.py`](../skillspector.py) scanner. The local script checks Markdown, shell, and Python skill files against a small set of regular expressions. Its `SAFE` label means no configured pattern matched, not that a skill is safe. Manually review skill instructions, scripts, permissions, and external destinations before use; a regex scan cannot certify safety.

### Original scanner prompt

```markdown
Analyze the repository's `skills/` directory for security vulnerabilities inspired by NVIDIA SkillSpector.
Create or update `_meta/skillspector.py` to inspect all markdown and script files in `skills/` for:
1. Hardcoded API keys, tokens, or private RSA keys.
2. Dangerous shell commands (`rm -rf /`, `curl | bash`, unquoted variables).
3. Prompt injection vulnerabilities or instruction override attempts.
4. Exfiltration risks (sending local file contents to external URLs).
Ensure `python3 _meta/skillspector.py` runs during the `/checkpoint` ritual.
```

## STORM-inspired research

[Stanford STORM](https://github.com/stanford-oval/storm) explores multi-perspective research and article generation. This example asks for a local research workflow inspired by it, not installation of STORM. Check conclusions against primary documentation and source evidence.

### Original research prompt

```markdown
Build a deep technical research skill in `skills/rituals/research.md` inspired by Stanford STORM.
The skill must follow a 4-stage research workflow:
1. Perspective Discovery: Generate 3-5 distinct technical perspectives/hypotheses before reading files or web searching.
2. Multi-Source Search & Inspection: Query primary documentation, source code, and authoritative references.
3. Adversarial Refutation Pass: Actively attempt to disprove the leading hypothesis against edge cases and failure modes.
4. Structured Synthesis: Produce a clear Markdown report with executive summary, technical breakdown, evidence log, and verified conclusions.
```

## Context7 documentation ingestion

[Context7](https://context7.com) supplies documentation snippets and examples for libraries and tools. This example saves a reusable cheat-sheet in `work/runbooks/`. Confirm the target library version and verify API signatures and parameters against its primary documentation; retrieving snippets alone does not guarantee that examples are current or verified.

### Original cheat-sheet prompt

```markdown
I am working with [Target Technology/Library, e.g., Next.js 15 / FastAPI / Fortinet REST API].
Please fetch or reference up-to-date documentation snippets from Context7 (https://context7.com) for this library.
Save the structured cheat-sheet and API definitions in `work/runbooks/<technology>-cheat-sheet.md`.
Ensure all code examples use verified, current API signatures and parameter structures.
```
