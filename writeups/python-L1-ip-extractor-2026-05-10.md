# Brute Force Source

**Track:** Python | **Level:** L1 | **Date Completed:** 2026-05-10 | **Hints Used:** None | **Time Spent:** ~30m

## What This Was

Second Python L1 challenge — the parsing follow-up to L1 #1 (Log Line Reader). Same data file, different goal: instead of just filtering down to Failed login lines, extract one specific field — the source IP — from each one. Output is a flat list of attacker IPs (with repeats preserved, because the count signal is what matters downstream). Cross-track closing step: redirect Python output to a file using the `>` operator from the Bash L1 redirection challenge run earlier the same session — reinforcing redirection while building the natural Python→Bash workflow real triage scripts use.

## What I Built

The script checks a log file for failed password attempts. It then takes the IP address of each attempt and outputs it to a file. Then that script is run and the stdout is redirected to a .txt file.

## Key Concepts Used

- **`str.split()` with no arguments** — splits a string on any run of whitespace, returning a list of tokens. Tolerates inconsistent whitespace (e.g., the `May  5` two-space gap in syslog format) without special-casing. Different from `.split(" ")` which splits on a single space character only and would treat `"May  5"` as three tokens.
- **List indexing** — `parts[12]` accesses the 13th element (zero-indexed). Knowing the field position requires knowing the log format; here, position 12 is the source IP for the `Failed password for invalid user X from Y port Z ssh2` line shape.
- **Positional field extraction is fragile** — same vulnerability `awk '{print $11}'` has in Bash. If the log format shifts (e.g., the `invalid user` prefix is dropped in a future sshd version), the index now points at the wrong field. The robust fix is regex extraction targeting the _shape_ of the value (`re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)`) — pull on the pattern, not the position. Out of scope for L1 but worth flagging.
- **Filter-then-parse, not parse-then-filter** — the Accepted lines in the same file have the IP at position 10, not 12. Skipping the `if "Failed" in line:` filter would have produced 3 garbage entries (port numbers from Accepted lines treated as IPs). Same trap WP002 exposed in awk; survived in Python because the filter held.
- **Lazy file iteration** — `for line in f:` directly, NOT `f.readlines()`. WP004 reinforcement, applied without prompt. Streams one line at a time; works on files of any size.
- **Cross-track: `>` redirect (overwrite)** — `python3 ip_extractor.py > ips.txt` saves the script output to a file. Used overwrite (not append) because each run produces a complete fresh result; appending would pile stale data on top of the new output. Same reasoning that drove Task 1 of Evidence Trail earlier today.

## What I Got Wrong First

Nothing was wrong here.

## Weak Points Flagged

**None new.** Positive signals on three existing fronts:

- WP004 (file iteration `f.readlines()` footgun): reinforcement landed without prompt — used `for line in f:` directly. Retest still on calendar 2026-05-14 but prognosis is good.
- WP002 family (positional-extraction-on-mixed-formats trap): filter held; Accepted lines correctly skipped despite being the simpler-looking path.
- Diagnostic shaky-string-handling (2026-04-27): the "split admin:password123" task was scored shaky on the diagnostic. Today's `split()` + indexed access is the same skill applied to log lines — addressed through application, not separate drill.

**Cross-track reinforcement note:** redirection refresher scheduled for 2026-05-14 (alongside WP003/WP004 retests) at user's request — proactive recall check, not a WP. Forward-looking metacognition: forecasting forgetting before the retention curve hits.

## What I Would Do Differently

Nothing really.

## Final Solution

```python
with open("labs/bash-L1/retest-wp002/auth-snippet.log") as f:
    for line in f:
        if 'Failed' in line:
            print(line.split()[12])
```

**Closing-step (cross-track redirection reinforcement):**

```bash
$ cd /mnt/d/cybersecurity_learning
$ python3 python/L1/ip_extractor.py > python/L1/ips.txt
$ cat python/L1/ips.txt
```

**Output:** 27 IP addresses, one per line, in file order. Repeats preserved (same IP made multiple Failed attempts — the count signal is what downstream tools want).
