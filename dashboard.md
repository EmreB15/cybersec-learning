# Cybersecurity Training Dashboard
*Last updated: 2026-10-12 — Session 30. **The parser stopped lying** — a false all-clear killed, 23 tests green, mypy clean. And the session where he named a pattern the log had already recorded.*

---

## Pickup Here

> ### ⭐ NEXT SESSION IS A NEW PROGRAM. Do not open with `loginwatch`, tests, types, packaging or docs.
> **`loginwatch`'s Python is finished.** Increments 11 and 12 are Bash, 14 is packaging, 15 is docs. No amount of `loginwatch` work will give him the Python building he keeps asking for.

**The build: a blue-team password-strength checker that inverts cupp.** His own idea, parked since July as debt #4. Given a person's own details — name, partner, pet, DOB, employer, postcode — generate every plausible derivation (case variants, leetspeak, appended years, concatenations) and **reject** a candidate password that falls inside that set. Pure stdlib: string manipulation, sets, `itertools`, scoring, argparse. Nothing borrowed from `loginwatch`, and it extends the `sectools` suite.

Real defensive security, not a toy: ⚠️ **Verify** [NIST SP 800-63B §5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html) — screening candidates against context-specific dictionaries is the actual recommendation.

> **How to open it:** hand him an implementation brief for increment 1 and let him **write code in the first ten minutes**. No spec-writing exercise, no test-first exercise, no project-structure discussion — `loginwatch` already proved he can do those and they are not what he's short of. Lock the acceptance criterion in the repo first; pre-write any incidental machinery as labelled scaffolding.

> ### ⭐ HEAD-OF-YEAR REVIEW DUE **2026-10-14** (Fable)
> On or after that date the **Fable agent speaks FIRST**. Brief it on: 11a shipped and debt #2 closed, but **`sectools` still not public** (its priority #2, since July); Bash L2 still the Scenarios gate; and the thing it most needs to see — **the tutor's method is now the programme's main risk, not his pace and not his retention.**

**Uncommitted:** `sectools` → `report.py`, `pyproject.toml`. `cybersec-learning` → `progress.json`, `dashboard.md`.

**Not to be volunteered as "Python work":** ship `sectools` public (debt #1 — worth raising as a separate 10-minute errand) · the `loginwatch` write-up (debt #3) · Increment 11 `run-daily.sh` when he wants **Bash**.

---

## Session 30 (2026-10-11 → 12) — Increment 11a, parser hardening

No time lock (*"not setting an amount of time"*). Ran past midnight. He asked for **Python, implementation focus**, so the pickup note's Increment 11 (Bash) was set aside for the one logged open gap in the Python code.

**The bug that existed and now doesn't.** `parse_line` read the outcome as `words[5]` — a fixed position. Measured on the new fixture:

```
OLD parser: crashed on the truncated line, counted {'203.0.113.45': 2}
NEW parser: {'203.0.113.45': 3}  | skipped: 2
```

Two failure modes in one function. **Loud:** a short line raised `IndexError` and killed the scan — and since an uncaught exception exits `1`, which `SPEC.md` defines as *"findings present"*, `run-daily.sh` would have read a dead tool as a detection. **Quiet, and worse:** an ISO-8601 timestamp has fewer prefix words, so `words[5]` landed on `for`, both detectors compared `'for' == 'Failed'`, got `False`, and the event vanished with no error. At `--threshold 3` that's **a clean report and exit 0 on a live brute force.**

**Shipped:** `parse_line` classifies every line into three exits (not-an-event → `None`; parseable → dict; login event with no recoverable IP → `raise MalformedLoginLine(line)`). `parse_file` returns `(records, skipped_count)`, `try` **inside** the loop so one bad line costs one line. `loginwatch` unpacks both, warns to stderr when nonzero, and an unreadable path exits 2 via an `OSError` handler below the `FileNotFoundError` one. **Suite 14 → 23.** `SPEC.md` gained `INPUT FORMAT` and `SKIPPED LINES`.

**⭐ Solo wins worth naming.** He reached the bounds check `words.index("from") + 1 >= len(words)` from a **single Tier 1 reframe** — and chose to *test the condition* rather than catch `IndexError`, which is strictly better: a blanket `IndexError` catch would relabel genuine coding bugs as bad input and let the skip counter absorb them. He'd also rebuilt the exception class and all of `parse_file` himself while the tutor was still writing the restated brief. And his refactor to one guard / one return was **his first refactor performed under a green suite** — verified in 0.3 seconds, which is the entire reason the suite exists.

**Concepts that stuck:** exactly one handler runs per `try`; handler order matters *only* where handlers overlap, and they overlap only when one is a subclass of the other; `try` **placement** decides how much work is abandoned, not which error is caught (demonstrated on his own fixture — `try` outside the loop lost a whole attacker IP); and **bug vs expected condition** — bad input is permanent, so counting it *is* the complete fix, and a custom exception type is what stops the counter absorbing real bugs. Runnable reference: [exception-handler-order.py](python-track/exception-handler-order.py).

**Second half — and the wrong call.** He asked to carry on with Python; the tutor chose mypy (debt #2). The debt's premise was wrong: there were no incorrect hints, `report.py` simply had none, so mypy had been skipping its bodies while reporting *"checked 3 source files."* Annotating the parameters let it inside `create_csv_report` and surfaced five pre-existing errors with one cause — `record` was a single name holding a tuple, then a list of CSV cells, then a `str` IP, then a list again. Runtime-harmless, invisible to all 23 tests, a real maintenance hazard. Closed out with `pyproject.toml` (`[tool.mypy] strict`, `[tool.pytest.ini_options] pythonpath`) so both tools run bare. **mypy clean, 23 green, CSV byte-identical. Debt #2 closed.**

Then he called it: *"this isnt python. This is some worthless file checker... i want to learn python stop floating around this."*

---

## The finding that matters most: he named a pattern the log had already recorded

> *"These python sessions are always the same for me, i start enthusiastic and then you somehow always find ways to make me want to just close the code editor and go do something else."*

Three of the last four project sessions. And **session 25's own log entry, written 2026-07-31, says it in the tutor's own words:** *"User arrived in a good mood, explicitly enjoying the coding ('ive been enjoying the coding stuff')... Left frustrated"* — ending at *"very close to leaving this session."* The evidence existed for ten weeks and wasn't acted on.

The shared ingredient in the bad sessions is that the headline work was **upkeep rather than building**. Session 30 did it twice: a hardening increment instead of a feature (defensible — it was a real bug), then type-checking config when he'd asked to carry on with Python (not defensible).

> ### 📌 **NEW RULE — PROJECT SESSIONS BUILD, THEY DO NOT MAINTAIN.**
> When he asks for Python work, the answer is **code that does something new.** Tests, type checking, packaging, config and docs happen only when he asks for them by name or when they genuinely block the next build step. At bootstrap, check whether the active project still *has* building work left — and if it doesn't, say so out loud instead of backfilling with quality tasks.

---

## The other finding: the teaching failed, not the code

Four distinct method failures in one session:

| # | Failure | His words |
|---|---|---|
| 1 | Taught a brand-new concept (custom exception classes) **alongside** the objective, so class theory ate the session while `parse_line` sat untouched | *"i dont like learning too many things at once"* |
| 2 | Corrected its own wrong brief **in the middle of** teaching that new concept | *"you mixed an explaination with something YOU got wrong?"* |
| 3 | Reviewed by producing a fresh adversarial log line each round, with no stated acceptance criterion | *"you keep moving the goalposts"* |
| 4 | Asserted twice, confidently, that his custom `__init__` "dropped the message" — **false**; `BaseException.__new__` stores positional args before `__init__` runs | — |

It cost him: *"this project feels ruined now, i feel so lost."* **He was factually right on all four.** That's the **sixth consecutive session** where his pushback on method was correct, and it is now the programme's main risk — not his pace and not his retention.

**The fix, applied mid-session:** reverted the tree to `409c68e` (attempt preserved in `stash@{0}`), then **locked the spec in the repo before he restarted** — 11 frozen inputs in `tests/test_parser.py` under a dated *"nothing is added to this list"* comment, the behaviour written into `SPEC.md`, and a stated pass condition (*23/23, nothing escapes `parse_file` but `FileNotFoundError`*). After the lock he finished all four parts plus the refactor on **one Tier 1 hint**.

> ### 📌 TEACHING RULES — all mandatory
> **NEW — ONE NEW CONCEPT PER TASK.** If the objective is X and reaching X needs machinery he hasn't touched recently, **the tutor writes that machinery**, labels it scaffolding, and gives one sentence on what it does — never how it works internally. It must not run as a second parallel lesson.
>
> **NEW — LOCK THE ACCEPTANCE CRITERION IN THE REPO BEFORE HE STARTS.** Frozen input list with a dated comment, behaviour in `SPEC.md`, pass condition stated up front. The spec changes **by argument**, never by the tutor's whim mid-task. *"You secure them before i start shooting."*
>
> **Carried:** implementation mode is the **default** (tutor decomposes, he codes, trade-offs decided for him with one line of why) · explanations capped at **~one screen** · **quote the line of the brief** a 🔴/🟡 violates, else it's a teaching observation · **no pattern without evidence** · **stop when he says he's solved it.**

Both new rules are mirrored into Claude Code memory so they survive context loss.

---

## Active Project — `loginwatch` (12/15 + 11a)

Blue-team auth-log brute-force detector; first portfolio project and the reference template.

- **Repo:** `/home/emrebektas/sectools` — 11 commits, **dirty at wrap**. **GitHub repo still not created** (open debt #1).
- **Contract:** `0` = clean · `1` = findings · `2` = error. In `SPEC.md`, enforced by tests, and now **actually honest** — a crash can no longer masquerade as a finding.
- **Test suite: 23 passing** — 11 frozen `parse_line` inputs, 2 `parse_file`, 6 end-to-end exit-code, 4 detection.
- **Input format is now documented**, not assumed: two recognised outcome words, the `from` landmark, three line classes, and *no input of any shape may abort a scan.*

| # | Increment | Status |
|---|-----------|--------|
| 0–9 | spec → parse → modules → detect → dual-role → report → CSV → argparse | ✅ |
| 10 | Nonzero exit on findings + error path | ✅ 2026-10-07 |
| **11a** | **Landmark parsing + custom exception + skipped-line counter** | ✅ **2026-10-11** |
| **11** | **`run-daily.sh` (Bash + `$?` + `if` + awk)** | ⬜ **next — recommended** |
| 12 | `install.sh` | ⬜ |
| 13 | pytest with fixtures *(pulled forward)* | ✅ 2026-10-07 |
| 14 | `pyproject.toml` + console entry point | ⬜ |
| 15 | README + MANUAL | ⬜ |

**Five minor items left in the code**, all flagged, none blocking: the `OSError` message says *"The path could not be found"* when that handler means found-but-**unreadable** · dead `outcome = None` initialiser · `raise` in redundant parens · `parse_file` docstring doesn't mention the count · double-space artefacts in both stderr messages.

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete. L2 criteria all demonstrated — argparse, pipeable CSV, `subprocess`. Last active **2026-10-12**. |
| Bash | **L2 (pending)** | L1 complete. Bandit + CTF carry real Linux load. L2 proper arrives at Increment 11–12. Last active **2026-10-09**. |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks when Python L2 + Bash L2 both complete. **Increment 11 is the gate.** |

---

## Active Weak Points

**None.** WP001 retired 2026-07-29; WP002 & WP004 mastered; WP003 & WP005 paused with the Concepts track.

Watched quietly inside review: **read the output you were given** (WP002 family). It did *not* surface against him this session — it surfaced against the tutor, twice, which is the honest record: a demo was mislabelled "payload lost" when its own output showed the payload intact, and a comparison demo was published before noticing it compared nothing. Both caught and retracted in-session.

**Still tracked in the CTF lane: identify before you act.** Unchanged this session — but the Python work was the same axis in a different key: `words[5]` trusts position, `words.index("from")` anchors on a landmark, and `file` reads magic numbers while `gzip` trusts the extension. Three instances of one idea now.

---

## picoCTF / CyLab — CTF Practice

- **Flags captured: 17.** Untouched this session.
- **Requeued, graded on identification alone regardless of flag capture:** Piece by Piece **~2026-10-23** (`file` first? `cat` not `zip`?) · Printer Shares **~2026-11-05** (is `nmap -Pn -sV` the **first** command?) · bandit12 **~2026-11-06** (`xxd -r` first? `file` between every step?)
- **Also queued:** Sudo Make Me a Sandwich needs one clean **self-powered** re-test · 2026-09-30 batch ~2026-10-21 · 2026-10-03 batch ~2026-10-24 · **Endianness** he self-flagged *"i doubt i will remember this"*.
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) · **Rules:** tool-lookups fine, **answer-lookups not**.

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit13** (`sshkey.private`, not started). Last touched **2026-10-09**.
- **Next diversion trigger: 2026-10-16** (7-day rule).
- **Cold-redo outstanding:** wipe notes, redo bandit0→6 cold (overdue since ~2026-08-07).
- Notes: [external/bandit-notes.md](external/bandit-notes.md). Passwords in `overthewire/notes.txt` — gitignored.

---

## Open Debts

1. **Ship `sectools` public** — spellcheck `SPEC.md` + OPSEC scrub + create the repo + push. ~10 minutes, standing since July, head-of-year priority #2. **Now has materially more worth showing.**
2. ~~**Install mypy**~~ — **CLOSED 2026-10-12.** Premise was wrong (no incorrect hints existed); the real gap was `report.py` being unannotated and therefore unchecked. Now `--strict` clean, strictness recorded in `pyproject.toml`.
3. **`loginwatch` write-up** — none since July. The exit-code contract, the 23-test suite and the false-all-clear bug with measured before/after numbers is the strongest portfolio material to date.
4. ~~**Parked idea (his)**~~ — **PROMOTED to the active build.** Blue-team password-strength checker inverting cupp. See the Pickup callout.
5. Vulnerable target VM (Metasploitable2/DVWA) — not needed until the end of the project arc.

---

## Checkpoints

- [x] Diagnostic *(2026-04-27)* · Bash L1 *(2026-05-10)* · Python L1 *(2026-05-11)* · Concepts L1 *(2026-05-18)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] 10+ archived write-ups *(2026-05-18)*
- [x] First L2 challenge *(2026-07-18)* · First multi-file Python program *(2026-07-23)*
- [x] First machine-readable tool output *(2026-07-29)* · First real CLI *(2026-07-30)*
- [x] First Head-of-Year review *(2026-09-30)*
- [x] First automated test suite *(2026-10-07)* · First real bug found by his own tests *(2026-10-07)*
- [x] First cold redos executed and graded honestly *(2026-10-09)*
- [x] **First custom exception type** *(2026-10-11)* · **First refactor under a green suite** *(2026-10-11)*
- [x] **First locked, in-repo acceptance criterion written before work started** *(2026-10-11)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] `loginwatch` public on GitHub
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11** · attempted-unfinished: 2
- **CTF flags captured: 17** · cold redos run: 2 (1 partial, 1 fail)
- `loginwatch` increments: **12 / 15 + 11a** · **tests passing: 23**
- **Bandit levels cleared: 13** (bandit0→13)
- Total sessions: **30** · Total hours: **~29.3** *(session 30 estimated at ~3h from transcript, not measured)*
- Weak points mastered: **2** (WP002, WP004) · retired: 1 (WP001)
- **Cross-track connections: 19**
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

Four touches in the last nine days — 10-03, 10-07, 10-08/09, 10-11/12. **Frequency is being met comfortably.** Durations remain unmeasured for a fifth consecutive session; session 30 is logged as a ~3h transcript estimate rather than a measurement. **Don't ask him mid-session** — estimate at wrap.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop. `pytest 9.1.1`.
- ⚠️ `pip3` reports a **pre-existing** apt conflict (`pipx 1.0.0` wants `argcomplete>=1.9.4`, Ubuntu shipped `1.8.1`). **Do not** `pip3 install --upgrade argcomplete` over the apt-owned package. The real fix is a virtualenv, which lands at Increment 14.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed**.
- `sectools` (`/home/emrebektas/sectools`) — loginwatch 12/15 + 11a, 23 tests, **dirty tree**, **GitHub repo not yet created**.
- `ctf-work/` — CTF solution scratch, **gitignored**.
- Localhost (`127.0.0.1`) — legal Python socket test target.
