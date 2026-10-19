# Cybersecurity Training Dashboard
*Last updated: 2026-10-19 — Session 34. **`run-daily.sh` exists and works. The session ended early because the tutor designed it wrong, not because he did.***

---

## Pickup Here

> ### ⚠️ READ THE SESSION 34 POST-MORTEM BEFORE PLANNING SESSION 35
> He asked for Bash and was handed a **challenge in a language he had never written a line of**. In 50 minutes he typed about three lines and read roughly eight screens of tutor prose. He ended it early: *"im feeling tired and slightly annoyed at this session. Just commit it for me, and wrap where we are."*
>
> **Bash L1 taught terminal *usage* — grep, pipes, redirection, find. It did not teach *scripting*.** The gap between driving a terminal and authoring a script is a language-acquisition step, and it was briefed as an exercise. It was also his **second session of the same day**, after a 2-hour build, and fatigue was never asked about.

### The one rule from this session

> **When a task needs a language he has not written before, do not brief it as a challenge.** Teach the constructs, then have **him type three or four throwaway five-line scripts** that drill each construct separately, *then* give him the real task. Typing volume is the metric. The demos now exist durably at [labs/bash-L2/scripting-tour/](labs/bash-L2/scripting-tour/) — but he **read** them, and reading is not the mechanism. The next Bash session opens with him writing, not with a brief.

| If he picks | Run this | Notes |
|---|---|---|
| **Bash** | `loginwatch` **increment 11b** — the four-way branch | **Already specified** in `sectools/SPEC.md` with the four exact strings. Frozen tests not yet written — budget ~10 min tutor prep (9 cases, pass condition **128**). Open it with him **typing**. |
| **Bash, and the gate** | `loginwatch` **increment 12** (`install.sh`) | The **second** of the two script challenges that complete Bash L2 — *and* the WP006 retest vehicle. |
| **CTF** | the **09-30 batch cold redo** | now **due** (~10-21). Grade on self-powered recall. Log in [external/cylab-notes.md](external/cylab-notes.md). |
| **Something fresh** | `watch-dir.sh` | He picked it as tonight's stretch ("A into B") and it was never started. Still a legitimate new build. |

**Retest due 2026-10-23 — WP006, Bash script authoring.** Guaranteed by the Tier 6 protocol, not by a demonstrated misconception. **Do not narrate it at him.** Test it by having him write Bash; say nothing unless it surfaces.

> ### ✅ WHAT SHIPPED ANYWAY — `run-daily.sh`, 6 lines, 119 green
> ```
> $ ./run-daily.sh data/auth-sample.log
> SOURCE IP        FAILED
> 203.0.113.45          8
> 198.51.100.22         6
>
> DUAL-ROLE IP
> 192.0.2.55
> 198.51.100.22
> run-daily: loginwatch exited with status 1     <- stderr
> [exit 1]
> ```
> Two commits in `sectools` (`165b198` spec + frozen tests, `b9a076c` the increment). **He typed lines 4, 5 and 6 himself and all three were structurally right first attempt** — including line 6, the one being watched for.

---

## Session 34 (2026-10-19, second session of the day) — increment 11a

**50 minutes of a stated 120 — 22:08 to ~22:58, ended early at his request.** Fifth consecutive measured session.

### Teaching that landed, all of it measured rather than asserted

| What | How it was shown |
|---|---|
| **`PATH` is reserved** | He named his variable `PATH` — *his reasoning was correct and well stated*: "i called it path as that will be what it is holding." Tutor typed it as articulated and ran it: `python3: command not found`, **exit 127**. PATH hijacking in miniature — and a live instance of the `UNEXPECTED` exit code the tutor had called theoretical twelve minutes earlier. |
| **`$?` clobbering** | `clobber.sh` showed `CODE` captured after an `echo` reading `0` instead of `2`. He then put `CODE=$?` on the line **immediately** after the command — against the natural English word order, which runs "say what happened, then record it". |
| **Line 6 is the contract** | Deleted it and reran: **117**, and the two failures were *findings* and *error* while the clean-log test kept passing. A **fail-open** — it breaks only in the direction that hides problems. |
| **Word splitting** | Line 5 was right *by accident*: four quote characters with `$CODE` outside the pair. A measured demo turned one value into three arguments: `[status not] [a] [number]`. |
| **A green test is evidence, not proof** | A shebang-only file already passed `test_clean_log_propagates_exit_0` — a script that runs no commands exits `0`. The suite read **113**, not the 112 predicted. |

### His prerequisite fix — and he put it in the right place

`report.py` printed dual-role IPs straight from a `set`, so **output order changed between processes** — eight runs, two different orderings. He put `sorted()` in both loop headers and **left the `set[str]` annotation alone**. That's the correct placement: order is a presentation concern, and the detection function's type honestly describes what it computes (an intersection, where membership is the point and order is meaningless). A daily archived report that reorders itself can't be diffed — which is exactly what increment 11 exists for.

### Tier 6 — the first of the programme

Reached after three escalating asks. Tiers 1–2 were **skipped deliberately and the skip was explained to him**: there is no misconception to reframe when the vocabulary is absent. Tiers 3–4 had already been delivered as the six numbered steps. Tier 5 (`usercheck.sh`, plus grep's measured `0`/`1`/`2`) didn't land. He then asked outright: *"all of it. I would rather you treat this as teaching than expect me to come up with an answer."*

**The tier was not the failure.** Reaching Tier 6 on a first-ever script in an unknown language is the system working. The failure was briefing it as a challenge at all.

---

## Active Build — `loginwatch` increment 11

| # | Sub-increment | Status |
|---|---|---|
| 11a | run, capture `$?`, report on stderr, propagate | ✅ **2026-10-19 · `b9a076c` · 119 green** |
| 11b | the four-way branch on the exit code | ⬜ **specified, tests not written** |
| 11c | timestamped report under `reports/` | ⬜ specified |

`SPEC.md` carries a **RUN-DAILY.SH** section locked before work started (`165b198`): the stream contract, the full three-part shape drawn so no sub-increment forbids a later one, and 11b's four exact strings.

**11b is the ideal test of the control-flow watch item from session 33** — `if/elif/else` is the whole of Bash branching, and the frozen cases include mutual-exclusion guards (a clean run must not *also* claim findings), which is exactly what a nested `if/else` gets wrong.

**Stream contract, settled:** stdout carries loginwatch's report **byte-identically** so the `--format csv` consumer still works through the wrapper · stderr carries the wrapper's own diagnostics · the exit code is **propagated, never invented**.

---

## Previous Build — `passcheck` ✅ finished and running

Increments 1, 2, 4, 5a, 5b, 6a, 6b, 6c, 6d. **88 of its own tests green.** Remaining work all needs a spec written first: increment 3 (`joins`, deferred) · increment 7 (scoring + report) · a 10-minute polish pass. **Never offer the polish pass as "Python work."**

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete 2026-05-11. Last active 2026-10-19 (s33). |
| Bash | **L2 (in progress)** | **Last active 2026-10-19 — the 162-day gap is closed.** 1 of 2 script challenges done, at **half weight** (Tier 6). |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks on Python L2 + Bash L2. **Increment 12 is now the gate.** |

---

## Active Weak Points

| ID | Track | What | Retest | Stage |
|---|---|---|---|---|
| **WP006** | bash | Bash script authoring — the five core constructs and double-quote expansion / word splitting | **2026-10-23** | 0 |

Opened by the **Tier 6 protocol**, not by a demonstrated misconception — he applied every construct correctly once taught. **No ceremony. Do not narrate it.** Vehicle: increment 12.

WP001 retired · WP002 & WP004 mastered · WP003 & WP005 paused with Concepts.

**Watched quietly inside review:** control-flow structure (nested `if/else` where mutually exclusive `elif` routes are needed) — **11b is the test** · read the output you were given (WP002 family) — clean again this session · **identify before you act** (CTF lane, untouched).

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit16** (port scan 31000–32000, not started). Last touched 2026-10-18. Next diversion trigger **~2026-10-25**.
- **Cold redos outstanding:** bandit13→16 ~2026-11-01 (graded on tool recall alone) · bandit12 ~2026-11-06 · bandit0→6 cold, **overdue since ~2026-08-07**.
- Notes: [external/bandit-notes.md](external/bandit-notes.md). Scratch in `overthewire/` — gitignored.

---

## picoCTF / CyLab — CTF Practice

- **Flags captured: 17.** Untouched this session.
- **09-30 batch cold redo is now DUE** (~10-21) · Piece by Piece ~10-23 (graded on `file`-first alone) · 10-03 batch ~10-24 · Printer Shares ~11-05 · Sudo Make Me a Sandwich needs one clean self-powered retest · **Endianness** he self-flagged.
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) · **Rules:** tool-lookups fine, answer-lookups not.

---

## Open Debts

1. **Push `sectools` to a private GitHub repo** — **32 commits** now exist only on this laptop. ~10 minutes, OPSEC scrub first. **Oldest live debt; he has been told at three consecutive closes.**
2. **`loginwatch` write-up** — none since July. The exit-code contract, the test suite and the false-all-clear bug with measured before/after numbers is still the strongest portfolio material to date. **Separate errand, never the session.**
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
- [x] **First Bash script he has ever written — `run-daily.sh`** *(2026-10-19)*
- [x] **First tool wrapped by another tool he wrote** *(2026-10-19)*
- [x] **First Python test suite whose subject is a Bash script** *(2026-10-19)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] `sectools` backed up to a private GitHub repo
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11.5** *(run-daily.sh at half weight)* · attempted-unfinished: 2
- **CTF flags captured: 17** · cold redos run: 2 (1 partial, 1 fail) · queued: 4
- `loginwatch`: **12.5 / 15 + 11a** · **31 tests**
- `passcheck`: finished and running · **88 tests**
- **Suite total: 119 green** *(corrected — the old "134 between them" double-counted; 88 + 31 = 119)*
- `sectools` repo: **32 commits** — 2 added this session, still no remote
- **Bandit levels cleared: 16**
- Total sessions: **34** · Total hours: **~36.5**
- Weak points mastered: **2** · retired: 1 · **active: 1 (WP006)**
- **Cross-track connections: 22** *(new: the Unix exit-code convention, measured on `grep`; and a Python suite testing a Bash script)*
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**Weekly summary:** not due — last run 2026-10-17, next on or after 2026-10-24.

**Timekeeping:** fifth consecutive measured session. No lock-time miss, because he ended it at 50 minutes. **Two 2-hour boxes set on the same calendar day, back to back, with no check on how the first had left him** — that is the scheduling note to carry forward.

**🎓 Head-of-year priorities to 2026-10-31** *(review #2, AMBER)*:
1. **Two project sessions he closes because he's done, not fed up.** ✅ s31 · s32 a half · ✅ s33 · ❌ **s34 — fed up.** Target was met before this session; the streak is broken and the cause is on record.
2. **Decide `sectools`-public in one sentence.** ✅ answered 2026-10-17.
3. **Retention lane on schedule, outside project time.** ✅ delivered 2026-10-18.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop. `pytest 9.1.1`, `mypy` in `sectools/.venv`. `bash 5.1.16`.
- ⚠️ `pip3` reports a **pre-existing** apt conflict (`pipx 1.0.0` wants `argcomplete>=1.9.4`, Ubuntu shipped `1.8.1`). **Do not** `pip3 install --upgrade argcomplete` over the apt-owned package.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed**.
- `sectools` (`/home/emrebektas/sectools`) — `loginwatch` + `passcheck` + `run-daily.sh`, **119 tests**, no GitHub remote.
- **Bash teaching demos:** [labs/bash-L2/scripting-tour/](labs/bash-L2/scripting-tour/) — `tour.sh`, `clobber.sh`, `usercheck.sh`, README.
- `ctf-work/` and `overthewire/` — scratch, both gitignored.
- Localhost (`127.0.0.1`) — legal Python socket test target.
