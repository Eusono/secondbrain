# Second Brain

A vendor-neutral, file-based knowledge workspace for working with AI coding assistants. I keep notes, decisions, rules, and lessons in Markdown so they survive a chat reset and remain usable across tools and machines.

> **The chat forgets; files don't.**

## Start here

| Starting point | What to use |
| --- | --- |
| I want to use this template | Make my own copy, then follow the setup steps below. |
| I want an agent to build a brain in an empty directory | Paste the [initial bootstrap prompt](_meta/patches/initial-bootstrap.md), then apply Patch 3. |
| I already have a brain | Read the [Patch 3 guide](_meta/patches/brain-bootstrap-patch-3-guide.md), then paste the [Patch 3 prompt](_meta/patches/brain-bootstrap-patch-3.md). Earlier patches are not required. |

### Set up my own copy

1. **Create a private repository or local workspace** from these files. This public framework is not the place for personal notes, employer material, or credentials. Before pushing employer material, confirm that the destination is approved.
2. **Install the basics:** Python 3.10+, Git 2.x, and ripgrep (`rg`), plus an AI coding assistant. No particular vendor is required.
3. **Start the assistant at my workspace root.** Have it read `AGENTS.md`, `constraints.md`, and `memory/MEMORY.md`, then personalize the template's identity, areas, and rules. See [assistant setup](_meta/guides/assistant-setup.md) for tool-specific loading.
4. **Apply Patch 3 for the current workflow.** Read its [guide](_meta/patches/brain-bootstrap-patch-3-guide.md), then copy everything below the divider in its [prompt](_meta/patches/brain-bootstrap-patch-3.md) into the assistant. Answer its setup questions and review the resulting patch notes.
5. **Check the workspace and open the dashboard:**

   ```sh
   python3 _meta/brain-health.py --quick
   python3 _meta/brain-dashboard.py
   ```

   Open `_meta/brain.html` in a browser. If the upgrade kept different script names, use the names in its patch notes.

**Template vs. upgrade:** this repository includes the baseline files and tools. Publishing a patch here does not apply it to the template or to my copy. Patch 3 builds the newer search, session-history, backup, and audit machinery in the target brain; features dependent on unavailable tools or approvals may be skipped and reported.

## How the workspace works

- **One brain, many assistants.** In this template, `AGENTS.md` holds the context; `CLAUDE.md` and `GEMINI.md` are symlinks to it. Instructions have one owner rather than separate copies per tool.
- **Files own the knowledge.** Topic context holds current state; dated history records events. Patch 3 separates those stores while respecting an existing brain's names and conventions.
- **Rules stay explicit.** `constraints.md` defines boundaries and approval requirements. Access to a tool or credential is not permission to use it.
- **Code stays separate.** Live repositories belong in gitignored `personal/code/` or `work/code/`; notes and runbooks belong in the brain.

| Path | Purpose |
| --- | --- |
| `personal/`, `work/`, `lab/` | Personal knowledge, professional work, and experiments |
| `memory/` | Cross-cutting facts and their index |
| `skills/rituals/`, `skills/lessons.md` | Repeatable workflows and lessons learned |
| `_meta/` | Health checks, stats, dashboard, and machine metadata |
| `_meta/patches/`, `_meta/guides/` | Setup prompts, upgrade prompts, and detailed guides |
| `_templates/`, `_inbox/` | Document shapes and incoming material awaiting a home |

The [constitution](AGENTS.md) owns the routing and precedence tables; the [living contract](constraints.md) owns the operating rules.

## Daily loop

1. Start the assistant at the brain root.
2. Work in the relevant area; record durable decisions and findings in files.
3. Ask it to search existing knowledge before reconstructing something already known. With Patch 3 applied, the [guide](_meta/patches/brain-bootstrap-patch-3-guide.md#finding-things) explains the search commands.
4. Near the end of the session, run `checkpoint` using the [ritual](skills/rituals/checkpoint.md): file the work, refresh current state, run checks, update stats and the dashboard, and commit the session's changes. Push only to an authorized destination.
5. Use `checkpoint and close` only after setting up the approved encrypted-session backup workflow described in the [Patch 3 guide](_meta/patches/brain-bootstrap-patch-3-guide.md#checkpoint-and-close).

## Prompts and guides

Full prompts live in files rather than in this README. Read the usage notes, then copy the prompt body—not the surrounding guide.

| Document | Purpose |
| --- | --- |
| [Initial bootstrap](_meta/patches/initial-bootstrap.md) | Build a new brain in an empty directory; follow with Patch 3 |
| [Patch 3 guide](_meta/patches/brain-bootstrap-patch-3-guide.md) | Applying the current cumulative upgrade and using the result |
| [Patch 3 prompt](_meta/patches/brain-bootstrap-patch-3.md) | Upgrade an existing brain, whether or not earlier patches were applied |
| [Earlier Architecture Upgrade](_meta/patches/architecture-upgrade.md) | Historical reference for P1–P13; use Patch 3 for current upgrades |
| [Assistant setup](_meta/guides/assistant-setup.md) | Shared context and tool-specific loading |
| [Optional integrations](_meta/guides/optional-integrations.md) | SkillSpector-inspired scanning, STORM-inspired research, and Context7 documentation prompts |

Optional integrations are not required to get started. A scan is evidence, not a safety guarantee; review external skills before running them.

## License

[MIT](LICENSE). Free for personal and commercial use.
