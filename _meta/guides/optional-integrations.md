# Optional integrations

[Back to the README](../../README.md)

These examples are optional, not prerequisites for using the workspace. The original prompt bodies are preserved below for deliberate use; reading this guide does not require running them or installing an integration.

## SOPS + `age` Encrypted Secret Vault (Optional)

By default, the Second Brain never stores plaintext credentials (`constraints.md`). If you want your assistant to run authenticated read-only API/database queries (Jira, GitHub/GitLab, firewalls, IPAM, etc.) and want those encrypted credentials to travel safely across your machines via Git without exposing plaintext, you can set up a **SOPS + `age` encrypted vault** (`_meta/secrets.enc.yaml`).

> **How it stays safe:**
> - Your private decryption key (`~/.config/sops/age/keys.txt`) lives **outside** the repository in your home directory (`chmod 600`) and is never committed.
> - Only the SOPS-encrypted file (`_meta/secrets.enc.yaml`, where every value is encrypted with `age` + AES-256-GCM and a MAC over the entire file structure) is committed to your private brain repository.
> - Under `constraints.md` (`HC-01`), the assistant may decrypt keys into memory inside a script or child-process wrapper (`bin/with-secret`), but is strictly forbidden from printing, echoing, logging, or writing raw secret values into any file or chat response.

### Step 1: Install `age` and `sops`

- **macOS (Homebrew):**
  ```bash
  brew install age sops
  ```
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt-get update && sudo apt-get install -y age
  # Download latest sops binary from https://github.com/getsops/sops/releases
  ```

### Step 2: Generate Your Local `age` Keypair (Outside the Repo)

Run this once per machine (or copy `keys.txt` securely between your own machines via 1Password/Keeper):

```bash
mkdir -p ~/.config/sops/age
age-keygen -o ~/.config/sops/age/keys.txt
chmod 600 ~/.config/sops/age/keys.txt
```

`age-keygen` will print your **public key** (`# public key: age1...`). Copy that `age1...` string (not the `AGE-SECRET-KEY-1...` line).

### Step 3: Create `.sops.yaml` in Your Brain Root

Create `.sops.yaml` at the root of your brain repository using your `age1...` public key:

```yaml
creation_rules:
  - path_regex: (^|/)_meta/secrets\.enc\.yaml$
    age: age1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 4: Create or Edit `_meta/secrets.enc.yaml`

1. Export `SOPS_AGE_KEY_FILE` in your `~/.zshrc` (or pass it inline):
   ```bash
   export SOPS_AGE_KEY_FILE="$HOME/.config/sops/age/keys.txt"
   ```
2. Open/create the encrypted vault in your `$EDITOR`:
   ```bash
   sops _meta/secrets.enc.yaml
   ```
   *(Or encrypt an existing YAML file in place with `sops --encrypt --in-place _meta/secrets.enc.yaml`, ensuring no plaintext temporary file is ever left on disk.)*

### Step 5: One-Shot Prompt to Wire SOPS + `age` Into Your Brain

Once `~/.config/sops/age/keys.txt` and `_meta/secrets.enc.yaml` exist, paste this prompt into your assistant to wire up the value-silent wrapper and metadata ledger:

````markdown
Set up SOPS + `age` secret consumption and metadata tracking in this Second Brain workspace without ever printing, echoing, or logging a secret value (`HC-01`):

1. Verify Key & Vault Presence (Value-Silent):
   - Confirm `~/.config/sops/age/keys.txt` exists (`0600` permissions) and `.sops.yaml` is present at the repo root.
   - Decrypt `_meta/secrets.enc.yaml` in memory via Python (`subprocess.check_output(["sops", "-d", "_meta/secrets.enc.yaml"])` with `SOPS_AGE_KEY_FILE` set) and print ONLY the top-level and second-level YAML key names (NEVER any values).

2. Create or Update `bin/with-secret`:
   - Ensure `bin/with-secret` disables shell tracing (`set +x`), resolves secrets from `_meta/secrets.enc.yaml` via `sops -d`, injects the requested key into a single child command's environment without offering any flag or mode that prints a value to stdout, and exits non-zero on a missing key.
   - Test the boundary using a non-existent key name (`__nonexistent_probe__`) so denial proves the wrapper works without touching a real credential.

3. Register Secret Metadata in `_meta/environment.json` & `memory/MEMORY.md`:
   - Record `secret_management` (`_meta/secrets.enc.yaml`, `SOPS with age`) and the value-free access register (service name, key path, scope, owner) in `_meta/environment.json`.
   - Add the non-secret `secrets["<service>"]` key paths to the relevant `memory/system_<name>.md` cards (using the label `Vault Pointer:`) so future sessions know where each service's credentials live without guessing.
````

---

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
