# Cybersecurity Training Dashboard
*Last updated: 2026-10-19 — Session 33. **`passcheck` is a finished, working tool. Increment 6 closed in 43 minutes on his own method, plus an unplanned 6d that took the password off the command line.***

---

## Pickup Here

> ### ⭐ SESSION 34 IS PROBABLY **CTF OR BASH**, NOT `passcheck`.
> His words at the close of session 33: *"taking a 2-3 hour break and then when i come back we can potentially do some ctf-work or some bash."* Likely still **2026-10-19** — don't re-run the weekly (last 10-17) or head-of-year (next 10-31) gates. Ask how long he has and set a fresh box.

| If he picks | Run this | Why |
|---|---|---|
| **CTF** | the **09-30 batch cold redo** | due ~10-21, so two days early is fine — it's the *graded redo*, not new content. Grade on **self-powered recall**, not flag capture. Log in [external/cylab-notes.md](external/cylab-notes.md). |
| **Bash** | `loginwatch` **increment 11**, `run-daily.sh` | **the Bash L2 gate on Scenario missions**, and the track is 162 days cold. Say it's the gate. Needs a spec + frozen tests locked first — Bash cases are harder to freeze, so budget tutor prep. It branches on loginwatch's exit codes (0/1/2) and both sample logs already exist. |
| **Linux CLI instead** | Bandit 16 — port scan 31000–32000 | not due until ~10-25, but legitimate if he asks for it. |

**Watch for:** session 33's only stall was **control-flow structure** — three mutually exclusive routes came out as a nested `if/else`. Bash is the ideal test of whether that generalises, since `if/elif/else` and `case` are the whole of Bash branching. **If it shows up again, then** consider one small drill. Not a weak point. No ceremony.

> ### ✅ `passcheck` IS FINISHED AND RUNNING — 111 green, repo clean at 30 commits
> ```
> $ printf 'L1v3rp00l1998' | python3 passcheck.py --word liverpool --word rex --year 1998 --password-stdin
> words: liverpool, rex
> years: 1998
> REJECTED: derived from 'liverpool' by case+leet+year
> [exit 1]
> ```
> Remaining, **all needing a spec written first**: increment 3 (`joins`, deferred) · increment 7 (scoring + report, reuses `report.py`'s CSV work) · a 10-minute polish pass (`description=`, `help=` on four options, redundant `else` after `sys.exit`). **Never offer the polish pass as "Python work."**

**Repeat verbatim:** offer two or three builds and let him pick · lock the spec section and frozen tests in the repo **before** he starts, pass condition as a number · **verify tutor tests against a reference in a throwaway copy of the repo** — worked three times today · include adversarial inputs · pytest is the green light, not the tutor · one commit per increment.

**New standing lesson, from three tutor errors today:** **freeze what must be printed *and* that nothing extra is** — and set the halfway check against **the clock**, not the conversation.

---

## Session 33 (2026-10-19) — increment 5b, then the whole of increment 6, then 6d

**120 minutes, measured — 17:12 to 19:12, locked ON TIME.** First session since s31 to finish inside its stated number; fourth consecutive measured one.

| Chunk | Budget | Actual | Outcome |
|---|---|---|---|
| Increment 5b — `screen` | 15 min | **21 min** | 80 green, **no hints** |
| 6a — argparse skeleton | 25 min | **20 min** | 88 green, **no hints** |
| 6b — the wiring | 30 min | **12 min** | 97 green, 3 findings |
| 6c — the explanation | 20 min | **8 min** | 103 green, **tool works end to end** |
| 6d — `--password-stdin` | 25 min | ~30 min | 111 green, Tier 3 + tutor-applied fix |

### His own method change, applied to a new problem, and it worked

**6a → 6b → 6c in 43 minutes.** Three sub-steps, each green before the next, three commits. The split was **his proposal** at the close of session 32 — *"starting off with just case then adding the leet and then the year. So i would understand it better."* Today is the evidence for it, and it was named to him as his.

### Increment 5b — the probe landed

One line, `return candidates.get(password)`. The conditional expression `A if cond else B` was **tutor-applied in 5a**; he reached for it **unaided** here and again in 6a's years line, with no prompting. It's his now, and it's off the watch list.

**His confusion was conceptual and he diagnosed it precisely:** *"is the source word the original password?"* → *"this is like working back... why would rex be returned as case+leet+year?"* He was reading the `(source_word, rule_chain)` tuple as a statement about the **source word** rather than about the **key**. Fixed by printing the real 18-entry map as a labelled table and tracing the forward derivation through his own three functions. **He was also right that screening works backwards** — affirmed as the architecture, not corrected: forwards is the computable direction, backwards is the needed one, and 5a bridges them by keeping receipts.

**Finding he fixed:** the annotation said `tuple[str, str]` while the function returns `None` on every accepted password. Shown rather than asserted — a caller trusting it unpacks the result and **crashes on the ACCEPTED path**, which is the path that runs for almost every password in production, and whoever later wraps that in `try/except` turns the screener into a fail-open.

### ⭐ Solo wins worth naming

1. **He anticipated `args.year` being `None`** rather than an empty list. The obvious `", ".join(args.year)` is a `TypeError` on every run with no year supplied — which is most runs. He handled a value he'd never seen, which is exactly what he *didn't* do in 5a.
2. **Absent vs empty, right first time** in 6b: `--password ""` is screened, not skipped.
3. **The tuple unpack and the f-string, first attempt**, format exact to the character including the quoting.
4. **`", ".join(args.word)` with no `sorted()` and no `set()`** — after two sessions of being told determinism matters, he knew *where* the rule applied and left the command line alone.

### Findings on 6b, two of them measured by deletion

- 🟡 **He imported `screen` and never called it**, inlining `.get()` instead. Deleting the import left **97 passing** — the import was dead, and a security decision existed in two places where only one would ever get hardened.
- 🟡 **`if args.password is None and args.password != ""`** — the second conjunct is dead (`None != ""` is always true). Deleting it left **97 passing**. The behaviour was right by accident of the first condition.
- Needed telling **twice** that the verdict must be *bound* to a name; he satisfied it by re-subscripting `candidate_map[args.password]` — a second lookup, and a guard and a fetch that are different operations and will drift apart.

### Three tutor criterion errors, all amended in the repo with dates and reasons

1. **The 5b pass condition said "57"** — it counted only the two `passcheck` test files and forgot bare `pytest` collects the 23 `loginwatch` tests too. Corrected to **80 before he started**.
2. **Two 6b cases froze stdout exactly equal to a line reading `REJECTED`** — on an interface 6c was always going to extend. *A frozen criterion must not forbid the next increment in the plan.*
3. **The no-password case asserted the right output but not the absence of extra output** — so an implementation that **warned about a password nobody supplied** passed the whole suite.

All three are the same sentence: **freeze what must be printed, and that nothing extra is.**

### 6d — and the escalation traced to the brief for the third session running

`--password-stdin` closed the leak the 6b spec had **deliberately deferred in the same session it recorded it**. `--password` was kept and warns on stderr rather than being removed — the `docker login` pattern — so 23 frozen cases and any existing caller keep working.

The 6d brief gave four input routes as a **table** and never drew how they converge on one value. What moved him: **measured `readline()` output** for four stdin shapes with `repr`, a **drawn control-flow diagram**, and the **parsed namespace printed for all four invocations**. Same shape of failure as session 32's Tier 2. *Draw the shape at brief time* now has three sessions of evidence.

**Concepts that stuck:** `.get()` is the lookup, not `in` plus a subscript · a type annotation that omits `| None` is a lie mypy will name · an option is repeatable with `action="append"`, and a dashed option is read as `args.password_stdin` · `store_true` is `False`/`True`, never `None` · `readline()` keeps its trailing newline and **only that newline comes off** — a trailing space is part of the password · stdout and stderr have different jobs · validate arguments **before** doing work.

---

## Active Build — `passcheck` ✅ running

| # | Increment | Status |
|---|-----------|--------|
| 1 | `case_variants` + `year_variants` | ✅ 2026-10-17 · `68d6d17` |
| 2 | `leet_variants` | ✅ 2026-10-17 · `f66c73e` |
| 3 | `joins` | ⬜ deferred — a candidate for next |
| 4 | `build_candidate_set` | ✅ 2026-10-17 · `ffa1709` |
| 5a | `build_candidate_map` — provenance | ✅ 2026-10-19 · `19a5504` |
| 5b | `screen` — the verdict | ✅ **2026-10-19 · one line, no hints** |
| 6a | argparse skeleton | ✅ **2026-10-19 · `149cc6c`** |
| 6b | the wiring | ✅ **2026-10-19** |
| 6c | the explanation line | ✅ **2026-10-19 — the tool works** |
| 6d | `--password-stdin` | ✅ **2026-10-19 — the leak is closed** |
| 7 | Scoring and the report | ⬜ direction only |

**111 frozen tests:** 49 `test_derive.py` · 8 `test_screen.py` · 8 `test_cli.py` · 9 `test_cli_verdict.py` · 6 `test_cli_explain.py` · 8 `test_cli_stdin.py`. Plus 23 `loginwatch` tests in the same directory, which is what the "57" error forgot.

**Design principles, all settled by argument rather than decree:** over-generation is the safe direction of error (his, 10-17) · a reproducible explanation is part of correctness (tutor, measured, 10-18) · a rejection with no reason gets worked around (⚠️ **Verify** [NIST SP 800-63B §5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html)) · **you don't delete a published option to fix a leak a warning can flag** (10-19).

**Still deliberately unfixed, recorded as decisions:** no `getpass` prompt, and the candidate map sits in process memory in plain text.

---

## Previous Project — `loginwatch` (12/15 + 11a)

**Python work is complete.** Increments 11 and 12 are Bash, 14 is packaging, 15 is docs. **Do not offer any of it as "Python work."** Increment 11 (`run-daily.sh`) is the **Bash L2 gate on Scenario missions**. 23 tests green, mypy strict clean.

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete 2026-05-11. Last active **2026-10-19**. |
| Bash | **L2 (pending)** | L1 complete. Track challenges last active 2026-05-10 — **flagged, 162 days**; Linux fluency carried by Bandit + CTF. **Arrives at `loginwatch` Increment 11.** |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks on Python L2 + Bash L2. **Increment 11 is the gate.** |

---

## Active Weak Points

**None logged.** WP001 retired; WP002 & WP004 mastered; WP003 & WP005 paused with the Concepts track.

**Watched quietly inside review:** read the output you were given (WP002 family) — **clean this session**, he read pytest and mypy output unprompted every time · **control-flow structure** (nested `if/else` where mutually exclusive `elif` routes are needed) — surfaced in 6d, see the pickup note · deciding a value before writing it rather than repairing it after — the module-level `password = None` was an instance.

**Still tracked in the CTF lane: identify before you act.** Untouched.

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit16** (port scan 31000–32000, not started). Last touched **2026-10-18**. Next diversion trigger **~2026-10-25**.
- **Cold redos outstanding:** bandit13→16 **~2026-11-01, graded on tool recall alone** · bandit12 ~2026-11-06 · bandit0→6 cold, **overdue since ~2026-08-07**.
- Notes: [external/bandit-notes.md](external/bandit-notes.md). Scratch in `overthewire/` — gitignored.

---

## picoCTF / CyLab — CTF Practice

- **Flags captured: 17.** Untouched this session.
- **Requeued:** 09-30 batch **~2026-10-21** · Piece by Piece **~2026-10-23** (graded on `file`-first alone) · 10-03 batch ~2026-10-24 · Printer Shares ~2026-11-05 · Sudo Make Me a Sandwich needs one clean self-powered retest · **Endianness** he self-flagged.
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) · **Rules:** tool-lookups fine, answer-lookups not.

---

## Open Debts

1. **Push `sectools` to a private GitHub repo** — **30 commits** now exist only on this laptop and today added seven. ~10 minutes, OPSEC scrub first. **Oldest live debt, and it grows every session.**
2. **`loginwatch` write-up** — none since July. The exit-code contract, the 23-test suite and the false-all-clear bug with measured before/after numbers is still the strongest portfolio material to date. Raise as a separate errand, never as the session.
3. Vulnerable target VM (Metasploitable2/DVWA) — not needed until the end of the project arc.
4. ~~Ship `sectools` public~~ — CLOSED 2026-10-17 as a decision. Private repo instead.

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
- [x] **`passcheck` runs end to end — a finished CLI that names the fact and the route** *(2026-10-19)*
- [x] **First tool that takes a secret off the command line — `--password-stdin`** *(2026-10-19)*
- [x] **First time his own method change was applied to a new problem and measured** *(2026-10-19)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] `sectools` backed up to a private GitHub repo
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11** · attempted-unfinished: 2
- **CTF flags captured: 17** · cold redos run: 2 (1 partial, 1 fail) · queued: 4
- `loginwatch`: **12 / 15 + 11a**, Python complete · **23 tests**
- **`passcheck`: increments 1, 2, 4, 5a, 5b, 6a, 6b, 6c, 6d · 111 green of 111 frozen · FINISHED AND RUNNING**
- `sectools` repo: **30 commits** — **7 added this session**, still no remote
- **Bandit levels cleared: 16**
- Total sessions: **33** · Total hours: **~35.7** *(33.7 + 2.0 measured, locked on time)*
- Weak points mastered: **2** · retired: 1
- **Cross-track connections: 21** *(new: a shell pipe into his own tool's stdin)*
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**Weekly summary:** not due — last run 2026-10-17, next on or after 2026-10-24.

**Durations are measurable again — four consecutive measured sessions**, and this one **locked on time** against a stated 120 minutes. The single timekeeping miss was tutor-side: the promised 18:36 halfway check on the 6d chunk never fired because the conversation ran through it. Twice in two sessions. **Set the halfway check against the clock, not the conversation.**

**🎓 Head-of-year priorities to 2026-10-31** *(review #2, AMBER)*:
1. **Two project sessions he closes because he's done, not fed up.** ✅ s31 · s32 a half · ✅ **s33 — a finished tool, on time, four commits.** Target met.
2. **Decide `sectools`-public in one sentence.** ✅ answered 2026-10-17.
3. **Retention lane on schedule, outside project time.** ✅ delivered 2026-10-18.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop. `pytest 9.1.1`, `mypy` in `sectools/.venv`.
- ⚠️ `pip3` reports a **pre-existing** apt conflict (`pipx 1.0.0` wants `argcomplete>=1.9.4`, Ubuntu shipped `1.8.1`). **Do not** `pip3 install --upgrade argcomplete` over the apt-owned package.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed**.
- `sectools` (`/home/emrebektas/sectools`) — `loginwatch` + `passcheck`, **134 tests between them (23 + 111)**, no GitHub remote.
- `ctf-work/` and `overthewire/` — scratch, both gitignored.
- Localhost (`127.0.0.1`) — legal Python socket test target.
