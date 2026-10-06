# Assistant setup

[Back to the README](../../README.md)

The workspace stores context in plain files so different assistants can use the same knowledge. Tool-specific loading behavior varies by version and configuration; verify what the installed tool actually reads rather than assuming every editor loads the same files automatically.

## Shared context convention

- `AGENTS.md` contains the instructions and context. The root file supplies workspace-wide rules; topic files such as `personal/AGENTS.md`, `work/AGENTS.md`, and `lab/AGENTS.md` hold local context and session logs.
- Existing `CLAUDE.md` and `GEMINI.md` symlinks point to the adjacent `AGENTS.md`. Preserve those links and edit the content file, not a separate copy. No link replacement is needed.
- Load the root and applicable parent/topic `AGENTS.md` files for the active directory. The repository's lean context set also includes `constraints.md` and `memory/MEMORY.md`.
- Root `AGENTS.md` includes `@constraints.md`. If the tool does not expand imports or otherwise load the full context set, explicitly attach or read `constraints.md` and `memory/MEMORY.md`, along with any missing topic context. A shared file does not guarantee that an already-running session has refreshed its contents.

## Tool setup

| Tool | Context setup |
| --- | --- |
| Claude Code | Use the existing `CLAUDE.md` links; confirm the root and relevant topic context are loaded. |
| Gemini CLI | Use the existing `GEMINI.md` links; confirm the configured context filename and loaded scope. |
| Codex | Use its `AGENTS.md` discovery mechanism; explicitly provide any context not loaded by the installed version. The Aider command below is not a Codex command. |
| Google Antigravity | Configure or explicitly attach `AGENTS.md` and the additional context files; verify the installed version's loading behavior. |
| Cursor / Windsurf | Use the editor's supported rules or context attachment mechanism to reference the shared files. Verify loading and import expansion; do not assume legacy `.cursorrules` or `.windsurfrules` behavior applies to every version. |
| Aider | From the repository root, use `aider --read AGENTS.md --read constraints.md --read memory/MEMORY.md`, adding the active topic's `AGENTS.md` with another `--read` flag. |

For post-upgrade harness configuration and additional context wiring, see the [Patch 3 guide](../patches/brain-bootstrap-patch-3-guide.md).
