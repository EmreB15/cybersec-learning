# Find Tour

**Track:** Bash | **Level:** L1 | **Date Completed:** 2026-05-08 | **Hints Used:** None on `find` content (one Tier 1 reframe was deflected — the patterns were already in the brief, brief-design issue owned tutor-side; one jargon-clarification needed on the word "quote") | **Time Spent:** ~25m

## What This Was

Third Bash challenge, first L1-grade challenge to complete cleanly. Four small queries against a synthetic triage lab (8 files across `home/emre/`, `tmp/`, `var/log/`) using only `find`. No piping, no `ls`, no `grep`. Each task introduced one predicate: `-type f` (files only, scaffolded in), `-mtime -N` (within last N days), `-name "*.sh"` (glob extension match), `-name ".*"` (hidden-file convention).

Re-attempt after the previous session's two L1 attempts collapsed for tutor-side issues (over-packed challenge design, unverified expected counts). Lab data preserved between sessions specifically so this challenge could run cleanly.

## What I Built

I used `find` to filter the files within the entire directory. For example, if something was modified in the last N days I can figure it out. I can find different file extensions by using the `-name` pattern.

## Key Concepts Used

- **`find PATH PREDICATES`** — recursive filesystem search by criteria. Predicates compose; for AND-style filters the order generally doesn't matter.
- **`-type f`** — restrict to regular files. By default `find` returns directories _and_ files, which is the bites-you-by-default behaviour that broke the previous session's expected-count claim. Knowing it's the default is half the value.
- **`-mtime -N` (sign syntax)** — `-N` = within last N days. `+N` = more than N days ago. Bare `N` = exactly N days ago. The sign is load-bearing; flipping it silently returns a different file set.
- **`-name "PATTERN"`** — match filename against a **glob** pattern (not regex). `*` = any sequence, `?` = any single char. Plain literal characters match themselves.
- **Glob quoting** — `"*.sh"` and `".*"` must be quoted to stop the shell from expanding the pattern _before_ `find` ever sees it. Without quotes, `find . -name *.sh` becomes `find . -name old_script.sh suspicious_payload.sh` (the shell pre-expanded the glob into already-found filenames), which produces a syntax error or wrong matches. Same trap on `.*`.

## What I Got Wrong First

I initially used `ls` as a command but after reading the constraints I swapped to `find` exclusively. When using `find` I used `.` for the current working directory and then `-type f` for the file type.

## Weak Points Flagged

None new. WP001 (instruction-precision) and WP002 (frequency-count discipline) were not retriggered by this challenge.

_Session context: the WP001 retest immediately preceding Find Tour passed cleanly. WP002 retest formally failed but the discipline was practiced post-hoc, and the WP002 description in `progress.json` was corrected to remove an unverified claim about `sort -r` lexicographic misranking on raw `uniq -c` output._

## Security Implication Noted

Each of the four queries maps to a real triage step on a host you suspect is compromised:

1. **`find . -type f`** — full file enumeration. Establishes the baseline of _what is on this disk_. Without enumeration there is no anomaly detection.
2. **`find . -type f -mtime -14`** — recently-modified files. After a suspected breach, this is often the first command an analyst runs. Attacker tooling, modified configs, dropped scripts all surface here. The time window is the analyst's call — _since the suspected compromise window_ might be hours or weeks.
3. **`find . -type f -name "*.sh"`** — script-file enumeration. Adversaries persist via cron entries or service hooks pointing at shell scripts in unexpected directories (`/tmp`, `/dev/shm`, user home). Combining this with `-mtime -N` finds _recently-dropped_ scripts — high-signal, low-noise.
4. **`find . -type f -name ".*"`** — hidden-file enumeration. Dotfile invisibility is a UI convention, not a security control. `ls` without `-a` skips dotfiles; `find` doesn't. Adversaries hide payloads in dot-prefixed names precisely because they're invisible to casual inspection.

In this lab, the Task 2 output surfaced exactly the two files deliberately seeded as IOCs: `tmp/suspicious_payload.sh` and `tmp/.hidden_dropper`. In a real triage, that pair of hits is your first lead — and Task 3 (the `*.sh` query) and Task 4 (the `.*` query) each independently re-flag one of them, which is a useful structural property of layered queries.

## What I Would Do Differently

Not much, I guess read the question more in depth.

## Final Solution

**Task 1 — list all files in the lab:**

```bash
$ find . -type f
./home/emre/.bashrc
./home/emre/notes.txt
./home/emre/old_script.sh
./tmp/.hidden_dropper
./tmp/cache.tmp
./tmp/suspicious_payload.sh
./var/log/auth.log
./var/log/syslog
```

**Task 2 — files modified in the last 14 days:**

```bash
$ find . -type f -mtime -14
./home/emre/notes.txt
./tmp/.hidden_dropper
./tmp/suspicious_payload.sh
```

**Task 3 — shell script files (`*.sh`):**

```bash
$ find . -type f -name "*.sh"
./home/emre/old_script.sh
./tmp/suspicious_payload.sh
```

**Task 4 — hidden files (filenames starting with `.`):**

```bash
$ find . -type f -name ".*"
./home/emre/.bashrc
./tmp/.hidden_dropper
```

---

_Part of the OU Cyber Security practical learning portfolio_
