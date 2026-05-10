# Log Line Reader (log_filter.py)

**Track:** Python | **Level:** L1 | **Date Completed:** 2026-05-10 | **Hints Used:** None | **Time Spent:** ~25m

## What This Was

First Python L1 challenge. Bridge from Bash one-shot log analysis (`grep`) to Python scriptable tooling.

The challenge: open `labs/bash-L1/retest-wp002/auth-snippet.log` (the same 30-line synthetic SSH auth log used in the WP002 Bash retest — 27 Failed lines + 3 Accepted lines), iterate through it, print every line containing the word `Failed`. Scope was deliberately tight: one new concept (file I/O via `with open(...)` context manager), reuse existing skills (loops, conditionals, string `in` operator), no string manipulation (diagnostic flagged that as shaky — to be addressed in a later challenge).

The pedagogical point: same filter as `grep "Failed" file`, expressed in Python so it can become a _building block_ in a larger script (count by IP, alert on threshold, generate a report) rather than a one-shot terminal command.

## What I Built

Built a simple Python script to open a file and read each line, and to output a line based on an if condition.

## Key Concepts Used

- **`with open(...) as f:`** — Python's context manager for file I/O. Closes the file automatically when the block exits, even if an exception is raised. The "right" pattern for any "open file → do thing → done" workflow.
- **Lazy file iteration** — `for line in f:` iterates the file object directly, one line at a time, without loading the whole file into memory. The Pythonic idiom and the operationally-correct pattern for log files of unknown size.
- **String `in` operator** — `if "Failed" in line:` is Python's substring membership test. Same role as `grep "Failed"` in Bash, just expressed differently.
- **`print(..., end="")`** — overrides `print`'s default trailing newline. Useful when the data being printed already carries its own newline (which is the case for lines read from a file — they keep their `\n`).

## What I Got Wrong First

I used `f.readlines()` which loads the entire file but using `f` instead is better as it will only load memory line for line. This will help with future cases if the file to read is very very large to avoid any errors. I also with the output I was forgetting that the lines had a /n at the end so the output was not very clean, I cleaned it up by using the end parameter for the print function.

## Weak Points Flagged

- **WP004 (new).** Python file iteration: defaults to `f.readlines()` (eager — materialises the entire file as a list in memory) instead of iterating the file object directly with `for line in f:` (lazy — one line at a time). Identical output on small files, but `readlines()` crashes on production-scale logs. Real defender concern: a script that crashes silently on a 2GB auth.log at 3am means alerts that depended on it never fire. Stage 0, retest 2026-05-14.

## What I Would Do Differently

Use `f` exclusively and make sure to handle my output properly.

## Final Solution

```python
with open("labs/bash-L1/retest-wp002/auth-snippet.log") as f:
    for line in f:
        if "Failed" in line:
            print(line, end="")
```

**Output:** 27 lines, each a `Failed password for invalid user ... from <IP> port <N> ssh2` entry. The 3 `Accepted password ... emre ...` lines correctly excluded.

**Cross-track equivalent (Bash):**

```bash
grep "Failed" labs/bash-L1/retest-wp002/auth-snippet.log
```

Both produce identical output for this task. Bash version is a one-shot pipe-friendly filter. Python version is the same logic as a _reusable building block_ — extend it later to count, alert, write a report, or feed the next stage of a pipeline. Decision factor: one-off check or reusable tool?
