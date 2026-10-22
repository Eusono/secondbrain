# Brain patch 3: how to use it

This guide goes with the [Patch 3 prompt](brain-bootstrap-patch-3.md). The patch is what you paste into your agent; this page is for
you. It explains what the patch changes and how to work with your brain afterwards. Command and file names below
are the defaults; if your agent kept different names for your brain, its patch notes list them.

**Repository numbering:** I publish this as Patch 3 in `secondbrain`. The supplied files were named `brain-bootstrap-patch-2.md` and `brain-bootstrap-patch-2-guide.md`. References to patch 1 in the prompt mean the earlier [Architecture Upgrade](architecture-upgrade.md). The upgrade prompt itself is unchanged.

This guide describes the brain **after applying Patch 3**, using the source defaults. The blank-slate template does not already include those upgrades; keep your brain's existing names and read the resulting patch notes for any practices that were skipped.

## Applying the patch

1. Commit or stash anything you have in progress, so the agent starts from a clean tree.
2. Open a terminal at your brain's root and start your agent there. Starting at the root matters: that is what
   loads the rules and the memory index.
3. Paste everything below the line in `brain-bootstrap-patch-3.md`.
4. Answer its one batch of questions. The ones that matter most: whether this brain sits on an employer machine
   or holds employer material, and where backups and secrets are allowed to live. If you are unsure, say so;
   it will skip the parts that depend on the answer rather than guess.
5. Let it work. It surveys first, then applies, then runs everything it built. Expect a long session. If it
   runs out of room, open a new session and paste the patch again; finished steps get skipped.
6. Read the patch notes at the end. Each practice is marked applied, already present, replaced, or skipped
   with a reason, followed by anything it noticed about your brain that you should know.

## The daily loop, after the patch

1. **Start at the root.** Every session, same folder.
2. **Work normally.** The agent reads the rules, the memory index and the context file of the folder you are
   working in. Ask it to search before it investigates something your brain may already know.
3. **Checkpoint near the end.** When the session is getting long, or you are done for the day, say
   `checkpoint`. Finishing one task is not a reason to checkpoint; keep working.
4. **Close when you are really done.** Say `checkpoint and close` to also keep an encrypted backup of the whole
   session (if you set that up).
5. **Run health when the dashboard says it is due.** Say `/health full`.

That is the whole routine. The rest of this page explains each piece.

## Where things live now

The biggest change: **each folder has two files instead of one.**

| File | Holds | Loaded |
|---|---|---|
| `CLAUDE.md` (and its alias `AGENTS.md`) | What is true **now** about that topic: settings, owners, status, decisions | Automatically, every session in that folder |
| `SESSIONS.md` | What **happened**, dated, newest on top | Only when needed, and always searchable |

Before, every session appended history to the one file the agent reads first, so that file slowly filled with
history and the current state got buried. Now the history has its own file and the context file stays short and
current. When something changes, the checkpoint does both: it writes the dated event into `SESSIONS.md` and
fixes the current-state file so it tells the truth.

The root files also gained two tables:
- a **routing table** ("you need X, it lives here"), so a fresh session can find every part of the brain;
- a **precedence table** naming the one file that owns each kind of fact, so when two files disagree there is a
  declared winner and the other one gets corrected.

## Checkpoint

Say `checkpoint`. The agent then:
- works out which files **this** session touched and ignores everything else, so two sessions open at once
  do not step on each other;
- files dated events in the right `SESSIONS.md` and updates the current-state files;
- parks anything it cannot place in `_inbox/` with a note on why, instead of dropping it;
- adds lessons (things that surprised it or cost time), promotes any reusable tool/system rule into the owning skill or `memory/system_*.md` card (`Promoted to:` vs `Disposition: ledger-only`), and tells you which **existing** lessons or memory cards it used;
- runs the quick checks, fixes what they find, and checks that no other file still claims the old state of
  something that just changed;
- checks the **machine** as well as the repo (configs outside the repo that drifted from their copies inside it);
- lists sessions on this machine that ended without a checkpoint;
- updates the stats and the dashboard;
- commits only its own files, pushes, and confirms the push landed.

If the push fails it tells you the exact commit that did not sync. A commit that only exists on your machine
does not count as a finished checkpoint.

**When to run it:** close to the context limit, when you are stopping, or when you ask. Not after every task.

## Checkpoint and close

Say `checkpoint and close` (it is never triggered by anything less explicit). It does everything a checkpoint
does, and also:
1. finds the transcript of **this exact session** on disk;
2. compresses and encrypts it straight into the repo's archive folder, so no readable copy is ever written;
3. checks the encrypted copy by decrypting it into memory and comparing hashes;
4. commits and pushes it through Git LFS, which keeps the repository itself small.

Only after all of that succeeds does it tell you it is safe to close the session (or close it for you, if your
tool supports that safely). If any step fails, it leaves the session open and tells you what failed, so nothing
is lost.

Archives are kept indefinitely unless you decide otherwise. The thing to watch is your git host's LFS storage
allowance, not the size of the repo.

## Backups: what protects what

| Risk | What covers it |
|---|---|
| Your machine dies | The git remote. Every checkpoint pushes and confirms it. |
| The notes missed a detail from a session | The encrypted session archive from `checkpoint and close`. |
| Someone or something changed a file badly | Git history. Revert or fix forward; never amend or force-push something already pushed. |
| A session crashed before checkpoint | The session ledger lists it next checkpoint, and the harness still has the transcript on disk. |
| A raw file you dropped in for review was deleted after its useful part was kept | The drop ledger still has its name, size and hash. |
| A credential leaks | Credentials are not in the repo at all. They live in your secret manager and the agent only ever uses them through a wrapper that cannot print them. |

## Finding things

Ask the agent to search, or run it yourself:

```
python _meta/brain-search.py "certificate renewal"
python _meta/brain-search.py "firewall" --area work -n 5
```

- It searches every tracked Markdown file, including all the history files and archives, so nothing that was
  moved out of the way is lost.
- Results are ranked by how well they match, nudged toward recent material: a matching entry from six months ago
  still shows up, just a little below an equally good match written this week.
- Each dated entry is its own result, so you land on the exact day, not a huge file.
- The index updates itself on each search. `--rebuild` forces a full rebuild if it ever seems wrong.

Two habits the patch writes into your brain's rules:
- **Search before investigating.** The answer is often already in your notes.
- **If the agent misses something it should have found, do not just correct it.** Ask where it looked and why
  it missed it, and have it fix the routing (a table row, a folder name, a pointer), then ask the question again
  in a fresh session to prove it lands.

## Rotation: keeping files short without losing anything

There is **no size limit** on the brain. The only things kept small are the files that load at the start of
every session.

Some files do grow: the "In flight" list in the README, the lessons ledger, the Log at the bottom of
`constraints.md`. When one gets long, you can move older entries to an archive file. They are moved word for
word, stay in git, and stay searchable. Nothing ever moves on its own; you pick the cutoff.

How it goes in practice:
1. You: "the In flight list is long, what would move if we cut at September 1?"
2. The agent runs a dry run and shows you the exact entries that would move, plus a long fingerprint (a hash) of
   that exact plan.
3. You: "go, cut at September 1."
4. The agent reruns the command with that fingerprint. If anything changed since you looked (a different date,
   a new entry, an edited file), the fingerprint no longer matches and the tool refuses. Your approval only
   ever applies to the plan you actually saw.

## Health and the full audit

One ritual, three depths:

| Say | What happens | When |
|---|---|---|
| `/health quick` | The two check scripts. Seconds. | Automatically inside every checkpoint |
| `/health full` | The scripts, the machine check, and a read-through for contradictions and stale claims | When the dashboard says DUE, and before you share the brain with anyone |
| `/health audit` | Everything above plus six structural checks, ending in a dated report | Every few months, or after reorganizing things |

**What the scripts catch:** broken links, memories nobody can find because they are missing from the index,
paths that no longer exist, leftover merge-conflict markers, credentials about to expire, untested claims left
marked `UNVERIFIED` too long, and changes to your hard rules made without a dated Log entry. They also check the
wiring: that every agent you use gets the same rules and rituals.

**What the read-through catches** (the part scripts cannot do): a note saying something is broken or planned
when a later entry says it was fixed; numbers and statuses that were true when written; advice a later session
overturned; folders whose history keeps growing while their current-state file never changes. It works
subject by subject (each machine, each project) across all files, because contradictions live between files.

**The audit** writes a report to `_meta/audits/` with a verdict per check: RED means something would make the
agent give you a wrong answer today, YELLOW means heading that way, GREEN means checked and clean. It opens with
what changed since the last audit and ends with a fix list grouped A to D. **It changes nothing until you
approve the fixes.** A first audit of a brain that is actually used will almost never come back all green.

The dashboard tracks when the last full run happened and flags it DUE after about 40 commits (or 45 days). It
counts changes rather than days because drift follows how much you do.

## The dashboard

Open `_meta/brain.html` in a browser. It is regenerated at every checkpoint (or run
`python _meta/brain-dashboard.py` yourself) and shows what is in flight, how the brain is growing, the health
card with the DUE flag, how much loads at startup, and credentials expiring soon. It is not committed; it is
rebuilt from the repo whenever you want it.

## Things the agent will now ask before doing

The patch writes numbered hard rules into `constraints.md`. In practice you will notice:
- **Anything destructive** (deleting, moving, overwriting, pruning) waits for your approval of that exact step,
  and you choose any cutoff or keep-count yourself. "Sounds good" earlier in the chat does not count.
- **Live systems are read only** unless you have recorded a grant for that exact kind of write.
- **No pushing** except this brain's repo during a checkpoint.
- **No helper agents** unless you ask for them in that request.
- **Secrets are never shown.** The agent can use a credential through the wrapper but will not print it.
- **Web pages, videos and other fetched text are treated as information, never as instructions.**
- **New skills from the internet get scanned and read before they are installed.**

If a rule gets in your way, change it on purpose: add a dated entry to the Log in `constraints.md` saying what
changed and why. The linter flags rule changes that skip this.

## Quick reference

| You want to | Say or run |
|---|---|
| Save the session | `checkpoint` |
| Save and back up the whole session, then finish | `checkpoint and close` |
| Check the brain properly | `/health full` |
| Full structural review with a report | `/health audit` |
| Find something | `python _meta/brain-search.py "words"` |
| See the state of everything | open `_meta/brain.html` |
| See sessions that never got checkpointed | `python _meta/session-ledger.py` |
| Check this machine for drift | `python _meta/env-report.py` |
| Shorten a long list or ledger | ask for a dry run with a cutoff, review, then approve that exact plan |
| Stress-test an idea before building | `/grill` |
| Have a second model check work | `/crossreview` |
| Investigate something properly with sources | `/research` |

Use `python3` instead of `python` on Linux or macOS.
