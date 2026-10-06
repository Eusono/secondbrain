# Initial bootstrap prompt

**Filename conventions:** This original prompt uses `CLAUDE.md` as the folder content file, with `AGENTS.md` and `GEMINI.md` aliases, and a separate real `AGENTS.md` at the root. The current template instead uses `AGENTS.md` as the content file with `CLAUDE.md` and `GEMINI.md` symlinks. The original prompt below is preserved unchanged.

Start in a new, empty personal directory, not this template checkout or an existing brain. Open an agent at that target brain root and copy everything below the divider into it.

---

You are setting up a personal knowledge workspace ("the brain") for me, from scratch, in the current
empty directory. Build it exactly to this spec. It is a proven design — don't redesign it, build it.
Where the spec says a script must exist, write the script yourself and verify it runs before moving on.

## First: interview me (keep it short)

Ask me these, then use the answers everywhere:
1. My name (for git config and the docs' voice — everything is written as me, in first person).
2. What I'll use this brain for — 2 or 3 top-level life/work areas (e.g. `personal/`, `work/`, `lab/`).
   If unsure, default to exactly those three.
3. Do I work at a company whose git remotes must NEVER see AI tooling files? (yes/no — drives the AI-guard step)
4. Which agent CLIs I have or plan to use (Claude Code / Codex / Gemini or Antigravity — wire all three regardless;
   extra wiring for an absent agent is harmless).
5. Do I have a private GitHub (or other) remote ready? If yes, take the URL; if no, set up local git only and
   leave a TODO in the dashboard.

## Core principle (write this into the root docs, it is the whole philosophy)

**The chat forgets; files don't.** Conversations compact and vanish — so nothing durable may live only in a
conversation. Everything worth keeping becomes a file in this repo, the same session it happened. Every folder
is a topic; its context file is the topic's living knowledge; dated session-log entries compound into durable
knowledge over time. The repo is the single source of truth and travels through git to every machine and every
AI agent I use.

## Layout to build

```
<root>/
  CLAUDE.md          # the constitution (lean!): how the brain works + imports constraints.md
  AGENTS.md          # tool-neutral brief, REAL file — what any non-Claude agent needs to know
  GEMINI.md          # symlink -> AGENTS.md (legacy name some CLIs read)
  constraints.md     # the living contract (see below)
  README.md          # the dashboard: what's in flight, how the daily loop works
  <area>/            # one folder per area from my interview answers
    CLAUDE.md        # the area's content file (knowledge + ## Session log)
    AGENTS.md        # symlink -> CLAUDE.md
    GEMINI.md        # symlink -> CLAUDE.md
  ideas/  decisions/  runbooks/  incidents/    # under the area they belong to, created WHEN NEEDED — not empty upfront
  skills/
    lessons.md       # the gotchas ledger (the flywheel — see below)
    rituals/         # tool-neutral ritual sources: checkpoint.md · lint.md · grill.md · crossreview.md
  memory/
    MEMORY.md        # one-line index of every memory (this is what loads into context)
    <slug>.md        # one fact per file, frontmatter: name/description/metadata.type
  _meta/             # machinery: brain-lint.py · brain-stats.py · brain-dashboard.py · brain-search.py · ask-agent.sh
  _templates/        # idea.md · adr.md — the shape new files copy
  _inbox/            # catch-all for things that don't have a home yet; triaged later, never dropped silently
  local/             # gitignored secrets overlay — never committed, never printed
  .claude/  .agents/  .gemini/   # per-agent wiring that routes to skills/rituals/ (thin adapters, no copies)
```

**The one-brain, many-agents rule:** `CLAUDE.md` in each folder is the content; `AGENTS.md` and `GEMINI.md`
are symlinks to it, so Claude Code, Codex, and Gemini all read the same knowledge. At the root, `AGENTS.md`
is a real file — the vendor-neutral brief (the agents.md convention) — and it must never address any one
agent by name ("you" is whoever is reading). Edit content once; every agent sees it. Rituals live once in
`skills/rituals/` and each agent's command system (`.claude/skills/<name>/SKILL.md`, `.agents/skills/<name>/SKILL.md`,
`.gemini/commands/<name>.toml`) is a thin pointer to that source — never a copy.

## constraints.md — the living contract

Create it with three sections and a Log:
- **🚫 Won't do (hard lines):** never print or store secret VALUES (passwords/keys/tokens — knowledge *about*
  secrets is fine, values never); no `git push` unless asked (invoking checkpoint counts as asking for THIS
  repo only); never any AI attribution or Co-Authored-By in commits; no destructive action on things the agent
  didn't create without surfacing first; [if employer-privacy = yes] no AI tells in anything that could reach
  a company remote.
- **⚠️ Shouldn't do (strong preferences):** Conventional Commits (`type(scope): summary`) for every agent, every
  commit; complete files over diffs; no flattery or filler; push back when I'm wrong — "I don't know, let's
  check" beats a confident guess.
- **✋ Needs approval:** destructive deletes (dry-run first), anything irreversible or outward-facing.
- **The co-editing contract** (multiple agents edit this file, so the rules for editing it are themselves rules):
  1. Append, don't overwrite — every change gets a dated `## Log` entry (the Log is how other agents SEE changes).
  2. Never silently delete or reword another rule; superseded rules get a dated Log entry saying what changed and why.
  3. Reconcile contradictions out loud — a body line may change only to a dated pointer at the Log entry.
  4. Neutral voice, dates not agent names.
  5. A machine backstop exists: `brain-lint.py` flags a hard line removed/reworded without a same-dated Log entry.

## The rituals (write each as `skills/rituals/<name>.md`, then wire all three agents)

**checkpoint** — the session-ending sweep. Steps: (0) `git pull --rebase` if clean, inspect first if dirty;
(1) for each thing worked on/decided/learned, append a dated entry (`### YYYY-MM-DD — topic`, newest on top)
to the most relevant folder's `## Session log`; file genuinely new items in ideas/decisions/runbooks/incidents
using `_templates/`; check recent logs first so nothing is double-filed; (2) anything unplaceable → `_inbox/`
with a one-line "why unsure" — never dropped silently; (3) refresh the living body of any file whose current
state changed + the root README "In flight" list; (4) recurring how-I-do-X patterns become files in `skills/`;
(5) **lessons**: anything that surprised me, cost time, or I'd do differently → one block in `skills/lessons.md`
(newest on top); no fabricated lessons — none is a fine answer; (6) cross-cutting facts no folder owns →
`memory/<slug>.md` + a one-liner in `MEMORY.md` (check the index first, consolidate rather than duplicate);
(7) report exactly what was written; (7b) run `brain-lint.py` and FIX findings — and for each file touched,
grep whether anything else still claims the OLD state of what just changed (a memory calling a fixed thing
broken makes the next session fix it twice); (8) run `brain-stats.py` (append growth snapshot) then
`brain-dashboard.py` (regen dashboard); (9) sweep any agent-private memory store into the repo — a private
store must never be the only copy; (10) run the checks, commit (neutral voice, Conventional Commit, no AI
attribution), push THIS repo, verify upstream state — a local-only commit is not a completed checkpoint.

**lint** — the drift check (checkpoint is Ingest; lint keeps what's already here TRUE). Mechanical half =
run `brain-lint.py`. Judgment half = read for contradictions: a memory or README claiming "open/TODO" for
something a later session log says is done; stale hand-maintained lists; `UNVERIFIED` markers >30 days old.
Run occasionally, or when the dashboard says it's due.

**grill** — before building anything non-trivial: stress-test the idea branch by branch (failure modes,
simpler alternatives, what kills it), resolve the tree, THEN build. Write the resolved design down.

**crossreview** — a DIFFERENT model reviews what one model built (the implementer is the worst available
reviewer of its own work). Hand over the falsifiable question, never the conclusion — anchoring buys
agreement, not review. Findings come back as candidates: proven, `UNVERIFIED(date)`, or wrong-about-my-setup.

**The `UNVERIFIED(date)` convention:** any claim written down but not tested gets the marker inline;
lint ages it (stale >30 days). Tag the debt, not the prose.

## The machinery (write these, then RUN each to prove it works)

- **`_meta/brain-lint.py`** (stdlib only): scan all tracked `.md` for (a) `[[wikilinks]]` that resolve to no
  file, (b) memory files not listed in `MEMORY.md` and index lines pointing at no file, (c) dead relative
  paths, (d) unresolved merge-conflict markers, (e) `UNVERIFIED` markers with their age, (f) hard-line
  constraint text removed/changed vs git HEAD without a same-dated Log entry. Exit non-zero on findings.
  Skip code inside backtick fences and inline code correctly.
- **`_meta/brain-stats.py`**: append one timestamped JSON line (files, folders, memories, skills, lessons,
  words, git commit) to `_meta/brain-stats.jsonl`.
- **`_meta/brain-dashboard.py`**: render `_meta/brain.html` — a single self-contained page (no external
  requests): growth curve from the jsonl, what's in flight (parsed from README), ritual list, lint health
  (last run + current findings), area map. Simple beats fancy; it will grow.
- **`_meta/brain-search.py`**: ranked lexical search over all tracked markdown (SQLite FTS5, BM25, mild
  recency boost), `python3 _meta/brain-search.py "query" [-n 8]`. Auto-rebuild index when stale.
- **`_meta/ask-agent.sh`** — phone-a-friend: consult a different model mid-task from a shell call.
  `bash _meta/ask-agent.sh <claude|codex|gemini> '<falsifiable question>'`. Rules: resolve binaries from
  PATH (never hardcoded install paths); consults run read-only/plan mode (a second opinion, not a second
  author); export a loop-guard env var (`ASK_DEPTH=1`) and refuse to run when it's already set — ONE hop,
  a consulted agent answers from what it knows and never delegates onward. Document that answers are
  candidates, not oracles: a probe beats an opinion.

## Git + privacy

- `git init`, sensible `.gitignore` (`local/`, index/cache files, OS junk). Set my name + a no-reply email.
- Every commit: Conventional Commits, neutral first-person voice ("add lint ritual", never "Claude added"),
  ABSOLUTELY no AI attribution trailers.
- [If employer-privacy = yes] create `~/.gitignore_global` (git `core.excludesFile`) hiding `CLAUDE.md`,
  `AGENTS.md`, `GEMINI.md`, `.claude/`, `.agents/`, `.gemini/`, `.codex/` in every OTHER repo on the machine,
  so AI usage never reaches a company remote. This brain repo tracks them explicitly (git add -f is not
  needed — a repo's own .gitignore can un-ignore; verify both directions actually work and show me proof).
- If I gave a remote: add it, push, verify. If not: leave a dashboard TODO "add private remote — the brain
  should survive this machine dying".

## Root docs to write

- **`CLAUDE.md`** (the constitution — keep it LEAN, a screen or two): the core principle, how context works
  (folder files auto-load, one brain many agents, symlink convention), the areas table, the checkpoint
  ritual summary + when to run it (near end of session/day, not constantly), voice rules, `@./constraints.md` import.
- **`AGENTS.md`**: the same brief, tool-neutral, plus: read `memory/MEMORY.md` yourself at session start;
  your private memory store (Codex `~/.codex/memories/`, Gemini's tmp store) is scratch with NO authority —
  the repo wins; follow constraints.md including its co-editing contract.
- **`README.md`** (the dashboard): the daily loop — 1. start from the root so the constitution loads;
  2. just work (context loads itself from the folder you're in); 3. run checkpoint near the end;
  4. verify it reported a clean push. Plus "In flight" (empty now) and a pointer to `_meta/brain.html`.
- **`_templates/idea.md`** and **`_templates/adr.md`**: minimal front-matter + section skeletons.
- **`skills/lessons.md`**: header explaining the format (one dated block per gotcha: what bit, why, the fix,
  newest on top) and that checkpoint step 5 grows it. Start empty — day-one lessons would be fake.

## Build order, and how to behave while building

1. Interview me. 2. Skeleton + symlinks. 3. Root docs + constraints. 4. Rituals + all three agents' wiring.
5. Scripts — write, RUN, fix, prove each (show me brain-lint passing, a stats line landing, the dashboard
rendering, search returning a hit). 6. Git + privacy guard + remote. 7. First commit(s), Conventional style.
8. Finish with a short tour: what exists, the daily loop, and my first three moves (work on something real;
run checkpoint; open `_meta/brain.html`).

Do not invent content for me — no fake memories, no placeholder session logs, no example ideas. The brain
starts empty and true. Where a judgment call is needed, pick the simple option and note it in the dashboard
rather than asking about everything. When you're done, everything you built must actually run — a script
that was never executed is a claim, not a tool.
