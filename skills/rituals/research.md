# Ritual: Deep Research & Synthesis (`skills/rituals/research.md`)

Inspired by Stanford STORM ([stanford-oval/storm](https://github.com/stanford-oval/storm)), this ritual executes a grounded, multi-perspective research pass with adversarial refutation before synthesizing findings.

---

## 4-Stage Research Workflow

### Stage 1: Perspective Discovery & Initial Hypotheses
Before opening files or searching external documentation, list 3-5 distinct technical hypotheses or perspectives regarding the problem.

### Stage 2: Primary Source Search & Inspection
Search authoritative sources:
* Primary documentation & API specifications (or [Context7](https://context7.com) snippets).
* Local source code definitions and configuration files.
* Empirical log lines and stack traces.

### Stage 3: Adversarial Refutation Pass
Actively attempt to disprove the leading hypothesis against edge cases, failure modes, and potential regressions. Ask: *"What evidence would prove this assumption wrong?"*

### Stage 4: Grounded Synthesis
Produce a Markdown research report containing:
1. Executive Summary & Verified Root Cause.
2. Evidence Log & Primary Source Citations.
3. Implementation Plan / SOP.
4. Saved Location: `work/runbooks/` or `lab/prototypes/`.
