# Trail in the Logs

**Track:** Bash | **Level:** L0 (scaffolded L1) | **Date Completed:** 2026-04-28 | **Hints Used:** Tier 1 (offered on Task 4) | **Time Spent:** ~30m

## What This Was

Second Bash challenge. Synthetic SSH auth log (25 lines, mixed `Accepted` / `Failed password` events from real-shaped syslog). Four questions to answer using only the shell — no editors, no copy-paste into a tool. Introduced **filtering with `grep`**, **piping (`|`)** to compose tools, **field extraction with `awk`**, and the **`sort | uniq -c | sort -rn` frequency-count idiom** that is the bread-and-butter of log analysis.

## What I Built

Today I built 4 one-line commands that looked through a `.log` file. I was looking for how many unique users had failed password attempts. This is a direct link to security — seeing if a user has an abnormal amount of failed password attempts. From there I looked at the specific IP address that was having these failed password attempts. I used `grep` to find a pattern and I used piping to link commands together to form nice one-line commands. The IP address then, in a real-world scenario, could potentially be blocked or monitored more closely.

## Key Concepts Used

- **`grep PATTERN FILE`** — filter to only matching lines.
- **Pipes (`|`)** — chain tools so one's output becomes another's input. The whole shell-as-analysis-tool philosophy.
- **`wc -l`** — count lines.
- **`awk '{print $N}'`** — extract the Nth whitespace-separated field. Position-based parsing.
- **`sort` + `uniq -c`** — the frequency-count idiom. Sort first (because `uniq` only deduplicates _adjacent_ lines), then `uniq -c` to count.
- **`sort -nr`** — numeric reverse sort. Critical when sorting count columns: default `sort` is **lexicographic**, which silently misranks any count ≥ 10.
- **`--help` / `man` self-service** — used on `head`, `tail`, `sort` to confirm flag behavior without asking for hints.

## What I Got Wrong First

When sorting by the number of failed IP attempts, for example, the number 25 would appear to be smaller than 8 because only the first index is being compared. If we compare numerically with the `-n` flag for `sort`, this avoids that error.

## Weak Points Flagged

- **WP002** — `sort | uniq -c | head` without sorting on the count column; trusts pipeline output without inspecting intermediate state. Stage 0, retest 2026-05-02. _(Self-correcting behavior already observed: the "is this hard-coded?" reflection on the same task is the same instinct that prevents WP002 in future. Worth tracking whether this stays self-corrected.)_

## Security Implication Noted

The Task 4 bug is the textbook case of **a pipeline that returns an answer to the wrong question.** The original `sort -r` flagged `185.220.101.50` (6 attempts) as the top attacker, when the real top attacker was `203.0.113.45` (8 attempts). In an actual incident response, that pipeline would block the second-worst IP and leave the worst one currently hammering the system completely unblocked — the kind of silent miss that ends careers.

The deeper lesson: **pipelines don't fail loudly when they're wrong.** They produce plausible output. The defense is the habit of inspecting intermediate stages before adding `head`/`tail`/`| jq .[0]` and trusting position. This is a recurring SOC-analyst failure mode and worth internalizing now, while the dataset is small enough to verify by eye.

The secondary lesson: **`awk '{print $11}'` is positional and fragile.** If the syslog format ever shifts, the pipeline silently reads the wrong column. Real-world tooling extracts IPs via regex (e.g. `grep -oE '([0-9]+\.){3}[0-9]+'`) so position doesn't matter. Filed for L1.

## What I Would Do Differently

Next time, instead of using `cat`, I would use `head -n 1` to only look at 1 line, because if this is a long log I don't have time looking for which field is where.
Next time, I need to remember to use the `man` command if I'm confused anywhere.

## Final Solution

**Task 1 — total line count:**
```bash
$ wc -l auth.log
25 auth.log
```

**Task 2 — count of failed-password lines:**
```bash
$ grep "Failed password" auth.log | wc -l
18
```

**Task 3 — unique usernames in failed-password lines:**
```bash
$ grep "Failed password" auth.log | awk '{print $9}' | sort -u
admin
backup
invaliduser
postgres
root
ubuntu
```

**Task 4 — IP with most failed attempts:**
```bash
$ grep "Failed password" auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | head -n 1
8 203.0.113.45
```

---

_Part of the OU Cyber Security practical learning portfolio_
