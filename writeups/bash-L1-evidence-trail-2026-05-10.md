# Evidence Trail

**Track:** Bash | **Level:** L1 (close-out) | **Date Completed:** 2026-05-10 | **Hints Used:** Tier 1 (Task 4 only) | **Time Spent:** ~25m

## What This Was

Final Bash L1 challenge — closes the level. Four micro-tasks covering the four shell redirection operators applied against `labs/bash-L1/triage/`: `>` (overwrite stdout to file), `>>` (append stdout to file), `2>` (redirect stderr to file), and `> file 2>&1` (redirect stdout to file AND merge stderr into the same file). Each task produced one evidence file with verifiable content; combined, the three output files (`findings.txt`, `errors.txt`, `full-capture.txt`) form a small triage dossier of the kind real incident response scripts build up.

## What I Built

I used commands to capture stdout and stderr. I was able to use redirection to overwrite or create a file. I was able to append to an existing file without overwriting. I was able to capture stderr on its own using `2>`, and then I was able to capture both stdout and stderr using `> file 2>&1`.

## Key Concepts Used

- **`>` — overwrite stdout to file.** Creates the destination file (truncating if it exists) BEFORE the command runs. Note: if the file is in the directory you're searching, it appears in your own command's output.
- **`>>` — append stdout to file.** Creates if missing, otherwise appends. Used to build up a running log/notes file across multiple commands.
- **`2>` — redirect stderr only.** Stream 2 (stderr) goes to file; stream 1 (stdout) untouched. Used to separate errors from findings, or to suppress noisy errors (`2> /dev/null`).
- **`> file 2>&1` — redirect stdout to file AND merge stderr into stdout.** Order matters: stdout-redirect MUST come before the merge. Reverse order (`2>&1 > file`) silently fails — bash parses left-to-right.
- **File descriptor numbers.** `1` = stdout, `2` = stderr. `2>&1` reads "redirect stream 2 to where stream 1 is currently going." The `&` distinguishes "file descriptor 1" from a literal file named `1`.
- **Shell parses redirection BEFORE the command runs.** That's why `>` creates the destination file before find traverses, and why redirection-operator order in `2>&1` matters.

## What I Got Wrong First

I was struggling with the stdout and stderr as I was unsure how I could have 2 arguments for the `find` command. At first I was using `&&` for "and", but this was wrong.

## Weak Points Flagged

- **No new WP logged.** Task 4 first-pass confusion was driven partly by a tutor-side brief-wording defect (capital "AND" clashing with shell `&&`, owned in session).
- **Cross-track evidence noted under WP002** (frequency-count discipline / inspect-intermediate-output): three failed Task 4 attempts each printed `find .` output to terminal, which would have been hard evidence the `&&` was splitting the command — not noticed before the Tier 1 reframe. Same underlying habit as WP002 (trust visible output without inspecting adjacent evidence). Logged as cross-track signal, no new WP. WP002 retest already scheduled 2026-05-12.

## What I Would Do Differently

Next time, realise that the arguments for the command can just be in order, as long as they are before the flags.

## Final Solution

```bash
$ cd /mnt/d/cybersecurity_learning/labs/bash-L1/triage/

# Task 1 — > (overwrite stdout to file)
$ find . -type f > findings.txt

# Task 2 — >> (append stdout to file)
$ find . -type f -mtime -14 >> findings.txt

# Task 3 — 2> (redirect stderr only)
$ cat var/log/syslog.99 2> errors.txt

# Task 4 — > ... 2>&1 (merge stdout + stderr into one file)
$ find . /nonexistent_path -type f > full-capture.txt 2>&1
```

**Resulting evidence files:**

```
labs/bash-L1/triage/
├── findings.txt        # Task 1's full listing + Task 2's recent-files listing appended
├── errors.txt          # Task 3's stderr capture: "cat: var/log/syslog.99: No such file or directory"
└── full-capture.txt    # Task 4's merged stdout + stderr in one file
```
