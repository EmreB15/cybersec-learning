# Cybersecurity Training Dashboard
*Last updated: 2026-10-20 — Session 35. **Increment 11 is complete, 136 tests green, and he closed the session done rather than fed up.***

---

## Pickup Here

> ### THE THING THAT WORKED — DO IT AGAIN
> The session opened with **three drill scripts he typed by hand**, before any brief: `args.sh` (`$1`/`$#`, quoted vs unquoted), `compare.sh` (`[ ]` is a command that can fail), `branch.sh` (`if/elif/elif/else` on HTTP status codes). ~15 minutes, ~20 typed lines, each with a **predict-then-run** step.
>
> He then wrote 11b's ten-line branch **unaided, first attempt green**. That is the same language that needed **Tier 6** the night before. **Drills are not a warm-up, they are the mechanism.**

### Two tutor corrections from this session, both his and both right

1. **"what drill? i just asked you to setup the session?"** — the amendment says *offer a choice* of builds at session start. The build was assigned instead. Offer two or three.
2. **"i want to do the drills but you havent even explained me what the drills expect"** — a drill needs its contract stated before he types: what it is (throwaway, ungraded, uncommitted), what it expects (type by hand, predict out loud, paste the real output), how many, how long, and what the exit gate is.

| If he picks | Run this | Notes |
|---|---|---|
| **Bash — the gate** | `loginwatch` **increment 12** (`install.sh`) | **The second of the two script challenges that completes Bash L2** → unlocks Scenarios. **Also the WP006 retest vehicle** (due 10-23). **Not yet specified** — budget ~15 min to write and freeze a criterion first. |
| **Something fresh** | `watch-dir.sh` | Still unstarted. He has now picked it as a stretch **twice**. A legitimate new build, spec written with him. |
| **CTF** | the **09-30 batch cold redo** | **Overdue** (was ~10-21) · Piece by Piece due ~10-23, **graded on `file`-first alone**. Log in [external/cylab-notes.md](external/cylab-notes.md). |
| **Linux gym** | Bandit 16 → 20 | Port scan 31000–32000. Next diversion trigger **~2026-10-25**. |

**Quoting is the one thing to watch.** He fixed `"$CODE"` *inside* the quote pair unprompted — the session-34 mistake — but left `> $REPORT_PATH` and `cat $REPORT_PATH` unquoted. A variable as a **redirect target or command argument** is a position he has not drilled. If increment 12 takes a path as an argument, that is where it bites — **let him hit it, don't warn him.**

> ### ✅ WHAT SHIPPED — increment 11, all three parts, 136 green
> ```
> $ ./run-daily.sh data/auth-sample.log
> SOURCE IP        FAILED
> 203.0.113.45          8
> 198.51.100.22         6
>
> DUAL-ROLE IP
> 192.0.2.55
> 198.51.100.22
> run-daily: report saved to reports/loginwatch-2026-10-20-215710.txt   <- stderr
> run-daily: loginwatch exited with status 1                            <- stderr
> run-daily: FINDINGS - suspicious activity found, review the report    <- stderr
> [exit 1]
> ```

---

## Session 35 (2026-10-20) — increments 11b and 11c

**81 minutes of a stated 80.** Sixth consecutive measured session. Ended at a clean stopping point, by completion.

### 11b — the four-way branch · **no hints, first attempt, 128 green**

Ten lines. Three things were right that were being watched for:

| What | Why it counts |
|---|---|
| **`elif`, not a nested `if/else`** | The flagged control-flow watch item from session 33, on the first task that could test it. Not cosmetic: the mutual-exclusion test ("a clean run must not also claim findings") passes **by construction** — an `elif` chain physically cannot fire twice. A nested version needs a guard he'd have had to remember. |
| **`$CODE` *inside* the quote pair** | The exact by-accident mistake from session 34's line 5, fixed unprompted on the first line where it mattered again. |
| **The branch sits strictly between the frozen lines** | The spec said no sub-increment removes output an earlier one froze. He didn't tidy line 5 into the branch, which was the tempting move. |

### 11c — the report archive · **Tiers 1 → 2 → 3, 136 green**

**What he got unaided from Tier 1 alone** — the reframe was *"you've gone from 5 red to 20 red; what does that tell you about where the problem is?"* plus *run it by hand and read everything it prints.* He found `${date ...}` vs `$(date ...)` himself: **`${}` is parameter expansion, `$()` is command substitution** — two sigils, two different operations.

**Tier 2, the concept:** `>` creates the **file**, not the **directory**. `No such file or directory` was complaining about `reports/`, not the `.txt`.

**Tier 3, in plain English:** one line was on the wrong stream, and — the mental model he was actually stuck on — **a redirect diverts, it does not copy.** The report had gone *into the file instead of* to the terminal, so it had to be read back out.

**The one he was predicted to get wrong and didn't:** `cat` went on the line **after** `CODE=$?`, not between the redirect and the capture. `test_11c_exit_code_is_still_loginwatchs_own` was lying in wait for that — `cat` succeeding would have overwritten loginwatch's status with `0`, and every findings-run would have reported clean. That's `clobber.sh` applied correctly to a case he hadn't seen.

### Review findings

🟡 **Unquoted variable as a redirect target and command argument** (lines 5 and 7, `shellcheck` SC2086). Works only because `date` generates a path with no spaces. **Security consequence named:** a redirect target that word-splits is how files get written somewhere unintended — the moment a path arrives from an argument, an environment variable or a config file, that becomes an attacker-influenced write.

🟢 `reports` appears as a literal twice (line 3's string, line 4's `mkdir`).

Also raised: the report files hold source IPs and auth outcomes and are created world-readable by default.

---

## Active Build — `loginwatch` increment 11 ✅ COMPLETE

| # | Sub-increment | Status |
|---|---|---|
| 11a | run, capture `$?`, report on stderr, propagate | ✅ 2026-10-19 · `b9a076c` · 119 green · **Tier 6** |
| 11b | the four-way branch on the exit code | ✅ **2026-10-20 · `06ab1a0` · 128 green · no hints** |
| 11c | timestamped report under `reports/` | ✅ **2026-10-20 · 136 green · Tiers 1–3** |

**Two spec amendments, both committed before he wrote a line:**

1. **11b's `UNEXPECTED` route is now tested behaviourally.** It had been specified as "checked by reading the code" because loginwatch only ever returns 0, 1 or 2. Withdrawn: `run-daily.sh` resolves `loginwatch.py` **relative to cwd**, so a stub `loginwatch.py` in a temp dir forces any exit code. Two frozen cases do it.
2. **11c's loose ends pinned** — the stderr string is exactly `run-daily: report saved to <path>`, and a report is written on **every** run including a failed one (empty file), so an absent report and a cron that never fired are distinguishable.

**Latent bug, deliberately not raised with him:** `run-daily.sh` calls `python3 loginwatch.py` with a **relative** path, so it only works with cwd `~/sectools` — a cron job elsewhere fails. He should discover it by running the script from another directory. Hardening it **will break** the two `UNEXPECTED` tests, which is a real and teachable consequence, not an accident.

---

## Previous Build — `passcheck` ✅ finished and running

Increments 1, 2, 4, 5a, 5b, 6a, 6b, 6c, 6d. **88 of its own tests green.** Remaining work all needs a spec written first: increment 3 (`joins`, deferred) · increment 7 (scoring + report) · a 10-minute polish pass. **Never offer the polish pass as "Python work."**

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete 2026-05-11. Last active 2026-10-19 (s33). |
| Bash | **L2 (in progress)** | Last active **2026-10-20**. 1 of 2 script challenges done, still at **half weight** — 11a was the Tier 6 part. **11b at Tier 0 and 11c at Tier 3 are the evidence that `install.sh` can clear the "done cleanly" bar.** |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks on Python L2 + Bash L2. **Increment 12 is the gate.** |

---

## Active Weak Points

| ID | Track | What | Retest | Stage |
|---|---|---|---|---|
| **WP006** | bash | Bash script authoring — the five core constructs and double-quote expansion / word splitting | **2026-10-23** | 0 |

**Mixed evidence this session — not reset, retest stands.** Fixed where previously burned (`"$CODE"` inside the quote pair, unprompted); not generalised to a variable as a redirect target or command argument. **No ceremony. Do not narrate it.** Vehicle: increment 12.

WP001 retired · WP002 & WP004 mastered · WP003 & WP005 paused with Concepts.

**Watched quietly inside review:** control-flow structure — **tested by 11b and clean, `elif` chosen correctly** · read the output you were given (WP002 family) — **clean, and Tier 1 worked because he read the error** · **identify before you act** (CTF lane, untouched).

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit16** (port scan 31000–32000, not started). Last touched 2026-10-18. Next diversion trigger **~2026-10-25**.
- **Cold redos outstanding:** bandit13→16 ~2026-11-01 (graded on tool recall alone) · bandit12 ~2026-11-06 · bandit0→6 cold, **overdue since ~2026-08-07**.
- Notes: [external/bandit-notes.md](external/bandit-notes.md). Scratch in `overthewire/` — gitignored.

---

## picoCTF / CyLab — CTF Practice

- **Flags captured: 17.** Untouched this session.
- **09-30 batch cold redo is OVERDUE** (was ~10-21) · Piece by Piece ~10-23 (**graded on `file`-first alone**) · 10-03 batch ~10-24 · Printer Shares ~11-05 · Sudo Make Me a Sandwich needs one clean self-powered retest · **Endianness** he self-flagged.
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) · **Rules:** tool-lookups fine, answer-lookups not.

---

## Open Debts

1. **Push `sectools` to a private GitHub repo** — **36 commits** now exist only on this laptop. ~10 minutes, OPSEC scrub first. **Told at four consecutive closes.**
2. **`loginwatch` write-up** — none since July. Increment 11 is now a complete three-part story: the exit-code contract, the test suite, the false-all-clear bug, and the fail-open branch, all with measured before/after numbers. **Strongest portfolio material to date. Separate errand, never the session.**
3. Vulnerable target VM (Metasploitable2/DVWA) — not needed until the end of the project arc.

---

## Checkpoints

- [x] Diagnostic *(2026-04-27)* · Bash L1 *(2026-05-10)* · Python L1 *(2026-05-11)* · Concepts L1 *(2026-05-18)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] 10+ archived write-ups *(2026-05-18)* · First L2 challenge *(2026-07-18)* · First multi-file Python program *(2026-07-23)*
- [x] First machine-readable tool output *(2026-07-29)* · First real CLI *(2026-07-30)*
- [x] First Head-of-Year review *(2026-09-30)*
- [x] First automated test suite *(2026-10-07)* · First real bug found by his own tests *(2026-10-07)*
- [x] First cold redos executed and graded honestly *(2026-10-09)*
- [x] First custom exception type · First refactor under a green suite *(2026-10-11)*
- [x] First locked, in-repo acceptance criterion written before work started *(2026-10-11)*
- [x] Second portfolio tool started — `passcheck`, his own idea, chosen from three *(2026-10-17)*
- [x] First combinatorial Python — `itertools.product` *(2026-10-17)*
- [x] First dict-building code — provenance through a three-deep walk *(2026-10-18)*
- [x] First time he pre-empted a red finding on his own code *(2026-10-18)*
- [x] First time he rejected a hint tier as the wrong rung — and was right *(2026-10-18)*
- [x] First time he specified the method himself — increment sizing, adopted *(2026-10-19)*
- [x] `passcheck` runs end to end · first tool taking a secret off the command line *(2026-10-19)*
- [x] First Bash script he has ever written — `run-daily.sh` *(2026-10-19)*
- [x] First tool wrapped by another tool he wrote *(2026-10-19)*
- [x] First Python test suite whose subject is a Bash script *(2026-10-19)*
- [x] **First Bash written with no hints at all — 11b's ten-line branch, first attempt green** *(2026-10-20)*
- [x] **First multi-part increment carried to completion — 11a, 11b, 11c** *(2026-10-20)*
- [x] **First time he corrected the tutor's session design to his face, twice, and was right both times** *(2026-10-20)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] `sectools` backed up to a private GitHub repo
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11.5** *(`run-daily.sh` still at half weight — 11a was the Tier 6 part)* · attempted-unfinished: 2
- **CTF flags captured: 17** · cold redos run: 2 (1 partial, 1 fail) · queued: 4
- `loginwatch`: **13 / 15 + increment 11 complete** · **48 tests** *(31 + 17 on `run-daily.sh`)*
- `passcheck`: finished and running · **88 tests**
- **Suite total: 136 green**
- `sectools` repo: **36 commits** — 4 added this session, still no remote
- **Bandit levels cleared: 16**
- Total sessions: **35** · Total hours: **~37.8**
- Weak points mastered: **2** · retired: 1 · **active: 1 (WP006)**
- **Cross-track connections: 24** *(new: `$()` vs `${}` as call-vs-lookup, the shell's two sigils for what Python spells one way; and fail-open control flow measured on `[`)*
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**Weekly summary:** not due — last run 2026-10-17, next on or after 2026-10-24.

**Timekeeping:** sixth consecutive measured session. 81 minutes against a stated 80, ended by completion at a clean stopping point. **One session on the day, not two** — which is the scheduling note from session 34 acted on.

**🎓 Head-of-year priorities to 2026-10-31** *(review #2, AMBER)* — next review due **2026-10-31**:
1. **Two project sessions he closes because he's done, not fed up.** ✅ s31 · s32 a half · ✅ s33 · ❌ s34 · ✅ **s35 — closed on completion, 136 green.** Streak restarted.
2. **Decide `sectools`-public in one sentence.** ✅ answered 2026-10-17.
3. **Retention lane on schedule, outside project time.** ✅ delivered 2026-10-18 — **but the CTF redo queue has since slipped: the 09-30 batch is overdue.**

---

## Lab Status

- Host attacker box — native Pop!_OS laptop. `pytest 9.1.1`, `mypy` in `sectools/.venv`. `bash 5.1.16`.
- ⚠️ `pip3` reports a **pre-existing** apt conflict (`pipx 1.0.0` wants `argcomplete>=1.9.4`, Ubuntu shipped `1.8.1`). **Do not** `pip3 install --upgrade argcomplete` over the apt-owned package.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed**.
- `sectools` (`/home/emrebektas/sectools`) — `loginwatch` + `passcheck` + `run-daily.sh`, **136 tests**, no GitHub remote. `reports/` is gitignored generated output.
- **Bash teaching demos:** [labs/bash-L2/scripting-tour/](labs/bash-L2/scripting-tour/) — read, not typed, session 34.
- **Bash drills he typed himself:** [labs/bash-L2/drills/](labs/bash-L2/drills/) — `args.sh`, `compare.sh`, `branch.sh`, session 35. **This is the format that worked.**
- `ctf-work/` and `overthewire/` — scratch, both gitignored.
- Localhost (`127.0.0.1`) — legal Python socket test target.
