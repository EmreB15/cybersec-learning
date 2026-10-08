# Cybersecurity Training Dashboard
*Last updated: 2026-10-07 — Session 28. **Heaviest Python session of the programme.** loginwatch 10/15 → 12/15, six commits, 14 passing tests, type hints throughout. Also the session where three method corrections from Emre became standing rules.*

---

## Pickup Here

**RESUME AT — he picks one. All three are small.**

1. **Finish the parser hardening** *(Python, directly continues tonight)* — `outcome` is still read as `words[5]`. On a short line that's an `IndexError`; on a variant line it yields junk like `outcome='ssh2'`, which matches neither `"Failed"` nor `"Accepted"` and so **silently drops the event from both detection functions**. Fix is the anchor pattern he already applied to the IP. Then a **skipped-line counter**, so silent drops become visible — an attacker who can provoke malformed lines is currently invisible and nobody knows.
2. **Increment 11 — `run-daily.sh`** — the Bash wrapper that *consumes* the exit codes he just built. The payoff, and the reason Increment 10 came first. Carries the planted set-order false-positive lesson and the type-it-yourself `awk '!x[$0]++'` task. He asked for Python, so only steer here if he wants Bash.
3. **Stream-separation asserts** — the tests check `returncode` only. Adding `result.stdout == ""` plus a path-in-stderr check would pin the stdout/stderr split permanently.

> ### 📌 TEACHING RULES ADOPTED THIS SESSION — now mandatory
> **Implementation mode is the DEFAULT.** The tutor decomposes work into numbered concrete steps; Emre writes the code; hint tiers address *how to implement*, never "what should happen here"; design trade-offs are **decided by the tutor** with one line of why. **Decomposition mode** (he produces the step list, tutor reviews the plan first) only when explicitly announced. Never mixed in one brief.
> **Explanations capped at ~one screen.** A misreading gets two or three sentences, not two sections.
> **Before writing any 🔴/🟡 — quote the line of my own brief it violates.** If that's impossible it's a teaching observation or the next increment's objective, never a weakness. An under-specified brief is the tutor's defect.
> *His framing: "Its two different skills figuring out what to do and then how to do it." Fourth consecutive session where his pushback on method was correct — treated as data, not mood.*

**Also carried forward:**
- **Expect type hints + docstrings** in his Python from here — his own adopted habit. One slip to watch: **twice he annotated what the body *produces* rather than what it *receives*** (`flag_suspicious` returns `list[tuple]` but was hinted `dict`; `parse_line`'s `line` is a `str` but was hinted `list[str]`). **Tests structurally cannot catch this** — mypy is the tool, not yet installed.
- **Durations null for three sessions running** — the head-of-year's *frequency over volume* call can't be measured. Ask for a rough duration at wrap even when he declines a lock.
- **No write-up this session** (six commits instead), so wrap-publish didn't apply. A loginwatch write-up covering the exit-code contract + test suite is strong portfolio material — worth offering.

> ### ⭐ Head-of-Year Review (Fable) — NEXT DUE 2026-10-14
> Speaks **first** at that session's bootstrap, before the teacher greets. Last review 2026-09-30 (🟡 AMBER). Its priority #2 was *"make loginwatch public + Inc 10"* — **Inc 10 is now done**; the public repo is not.

---

## Session 28 (2026-10-07) — exit codes, a test suite, and a real bug found

No time lock (his call: *"I can have as long as i want. I just want to focus on coding"*). Ran past midnight. Opened on **"i want to focus heavy on python work today"** — which happened to match head-of-year priority #2, Python having been untouched for 68 days.

| # | Work | Commit | Help |
|---|------|--------|------|
| 1 | **Increment 10** — exit-code contract `0`/`1`/`2` + `try`/`except` on an unreadable path | `fc757fb` | Tier 4 (tutor-caused — see below) |
| 2 | **Increment 13** (pulled forward) — 5 end-to-end exit-code tests | `580de5e` | Tier 2 once, on `subprocess` list form |
| 3 | **13b** — 4 unit tests of the detection functions | `f947594` | solo |
| 4 | Type hints + docstrings on the detection functions | `8ee98f8` | solo |
| 5 | `parser.py` tests → **found a real IP-misattribution bug** → anchor fix | `92d669c` | solo |
| 6 | Guard so one malformed line can't abort the scan | `409c68e` | solo |

**⭐ The best teaching moment was a regression.** Narrowing the `try` block as asked dropped the `sys.exit(2)` with it, so the handler printed its message and **fell through** to code that assumed the parse had succeeded — `NameError: records`, exit 1. Lesson landed: **catching an exception does not stop execution**; an `except` block must exit, return, re-raise, or establish valid state. Related: his `except FileNotFoundError` (rather than a bare `except:`) avoided a live landmine — `SystemExit` inherits `BaseException`, so a bare except would have swallowed his own `sys.exit(1)` and reported every detection as a file error.

**⭐ Mutation testing, and it earned its keep.** Rather than eyeballing the new suite, the tutor broke the source in a throwaway copy. First pass: `intersection` → `union` **survived** (his `input_4` held only the both-outcomes IP), and the sort test defended nothing. He fixed both inputs; re-verified — sort removal, `>=` → `>`, and `intersection` → `union` are all now caught. Earlier in the session he'd called the see-it-fail exercise *"pointless in my opinion"* and was **largely right**; this was the version with real information value.

**🔴 He blessed a bug into the spec, and was pulled up on it.** `parse_line` read the IP as `words[-4]`, assuming every line ends `port <N> ssh2`; a truncated line yielded `ip='for'`. He asserted *that* as the expected value. Re-done properly: correct assert → red → anchor on the `from` landmark → green. The anchored version also handles `"Failed password for invalid user admin from ..."` — a case neither of us wrote a test for.

**⭐ He diagnosed the documentation gap himself:** *"i didnt comment when writing up loginwatch... i would know what the outputs would look like without the need to remember from memory."* That produced the type-hints work. Then: *"i like the signatures it might be a good habit to get into."*

**Security thread running through all of it — silent under-counting.** Three separate instances in one session: an unreadable log exiting `1` (indistinguishable from a detection), an IP parsed as `"for"` (failures accumulate under a nonsense key and never cross the threshold), and `outcome='ssh2'` (event dropped by both detection functions). Each one leaves the tool **reporting healthy while blind** — the worst failure mode a detector has.

**Cross-track link (+1 → 18):** **stderr** — banked at Bandit as `2>/dev/null`, a destination for unwanted output; written *to* for the first time here via `print(..., file=sys.stderr)`, with `2>/dev/null` serving as the proof it went to the right stream. Same mechanism, opposite side.

---

## Active Project — `loginwatch` (12/15)

Blue-team auth-log brute-force detector; first portfolio project and the reference template.

- **Repo:** `/home/emrebektas/sectools` — 11 commits, working tree clean. **GitHub repo still not created** (open debt #1).
- **Contract:** `0` = clean · `1` = findings (brute-force or dual-role) · `2` = error. Documented in `SPEC.md` **and enforced by tests**.
- **Test suite: 14 passing** — 5 end-to-end exit-code (`subprocess`), 4 detection unit, 5 parser. Mutation-verified.
- **Parsing:** IP now read by **anchor** (`words.index("from") + 1`), not position. Malformed lines are skipped rather than aborting the run.
- **Known gap, logged in the commit message:** `outcome` is still `words[5]`.
- **🌱 Planted lesson still waiting at Increment 11 — do not pre-empt.** `report.py` loops over a **set**, so output order flips between runs → fires a false positive once `run-daily.sh` diffs day-to-day. Let him build it, let it fire, *then* let him find the cause. Also at Inc 11: make him actually type `awk '!x[$0]++'`.

| # | Increment | Status |
|---|-----------|--------|
| 0–9 | spec → parse → modules → detect → dual-role → report → CSV → argparse | ✅ |
| **10** | **Nonzero exit on findings + error path (`sys.exit`)** | ✅ 2026-10-07 |
| 11 | `run-daily.sh` (Bash + `$?` + `if` + **awk**) | ⬜ next in sequence |
| 12 | `install.sh` | ⬜ |
| **13** | **pytest with fixtures** *(pulled forward)* | ✅ 2026-10-07 |
| 14 | `pyproject.toml` + console entry point | ⬜ |
| 15 | README + MANUAL | ⬜ |

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete. L2 criteria (subprocess, argparse, pipeable output) now **all three demonstrated** — argparse at Inc 9, pipeable CSV at Inc 8, `subprocess` at Inc 13. Last active **2026-10-07**. |
| Bash | **L2 (pending)** | L1 complete. Bandit (11 levels) + CTF forensics carry real Linux load. L2 proper arrives at loginwatch Inc 11–12. |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks when Python L2 + Bash L2 both complete. |

---

## Active Weak Points

**None.** WP001 retired 2026-07-29; WP002 & WP004 mastered; WP003 & WP005 paused with the Concepts track. Carried-forward discipline watched quietly inside review: *verify-don't-proxy* — and this session he applied it himself, fixing the test **input** rather than pasting pytest's actual into the expected slot.

---

## picoCTF / CyLab — CTF Practice

**The CTF lane now runs without the tutor** — which is what freed this session for project work, and exactly the spine/variety split the head of year asked for.

- **Flags captured: 17** (+3 solo on 2026-10-03: Binary Digits, Riddle Registry, Hidden in plainsight — his first **Forensics** work).
- Those notes are genuinely good self-coaching: he caught the `stat` (filesystem) vs `pdfinfo` (embedded) **metadata-layer** distinction himself, flagged his own *Magic-instead-of-recognition* habit twice unprompted, corrected his own "decrypted" → "decoded" slip, and recorded the **verify-tools-an-LLM-hands-you** rule.
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) — includes an Encoding Recognition cheat sheet, a CyberChef setup reference, and a download-zip workflow.
- **Cold-redos overdue:** **Piece by Piece + Printer Shares** (HIGH) · **Sudo Make Me a Sandwich** needs a clean self-powered re-test (the last was Gemini-assisted). 2026-09-30 batch queued ~2026-10-21; 2026-10-03 batch ~2026-10-24. **Hand these over as homework** — don't spend session time unless he asks.

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit11** (ROT13, not started). **Last touched 2026-07-30 — 69 days.** A diversion is overdue on every trigger; deliberately **not** pushed on 2026-10-07 because he asked for Python. **Push it next short or low-energy session.**
- **Cold-redo:** wipe notes, redo bandit0→6 cold (overdue since ~2026-08-07).
- Notes: [external/bandit-notes.md](external/bandit-notes.md). Passwords in `overthewire/notes.txt` — gitignored, never committed.

---

## Open Debts

1. **Ship `sectools` public** — spellcheck SPEC.md + OPSEC scrub + create the GitHub repo + push. ~10 minutes, standing since July, head-of-year priority #2. **There's now substantially more worth showing:** a documented exit-code contract and a 14-test mutation-verified suite.
2. **Install mypy** — two wrong type hints shipped this session that no test can catch.
3. **Parked idea (his):** blue-team password-strength checker that inverts cupp (reject a password derivable from the user's own details — NIST 800-63B). Candidate `sectools` sibling.
4. Vulnerable target VM (Metasploitable2/DVWA) — not needed until the end of the project arc.

---

## Checkpoints

- [x] Diagnostic *(2026-04-27)* · Bash L1 *(2026-05-10)* · Python L1 *(2026-05-11)* · Concepts L1 *(2026-05-18)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] 10+ archived write-ups *(2026-05-18)*
- [x] First L2 challenge *(2026-07-18)* · First multi-file Python program *(2026-07-23)*
- [x] First machine-readable tool output *(2026-07-29)* · First real CLI *(2026-07-30)*
- [x] First Head-of-Year review *(2026-09-30)*
- [x] **First automated test suite — 14 tests, mutation-verified** *(2026-10-07)*
- [x] **First real bug found by his own tests** *(2026-10-07 — `ip='for'`)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] `loginwatch` public on GitHub
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11** · attempted-unfinished: 2
- **CTF flags captured: 17** (3 this fortnight, solo)
- `loginwatch` increments: **12 / 15** · **tests passing: 14**
- Bandit levels cleared: **11** (bandit0→11)
- Total sessions: **28** · Total hours: **~26.3** *(sessions 27 and 28 untracked at his request)*
- Weak points mastered: **2** (WP002, WP004) · retired: 1 (WP001)
- Cross-track connections: **18**
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

Session 27 (2026-09-30) → session 28 (2026-10-07): **one week, two sessions**, plus a solo CTF block on 2026-10-03. That is the head-of-year's *frequency over volume* call being met — three touches in eight days. Hours unmeasured for the third session running; worth starting to log even a rough number.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop. `pytest 9.1.1` installed 2026-10-07.
- ⚠️ `pip3` reports a **pre-existing** apt conflict (`pipx 1.0.0` wants `argcomplete>=1.9.4`, Ubuntu shipped `1.8.1`). Not caused by the pytest install; **do not** `pip3 install --upgrade argcomplete` over the apt-owned package. The real fix is a virtualenv, which lands at Increment 14.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed** (not needed until end of project arc).
- `sectools` (`/home/emrebektas/sectools`) — loginwatch 12/15, 11 commits, clean tree, **GitHub repo not yet created**.
- `ctf-work/` — CTF solution scratch, **gitignored** (keeps the public repo clean and cold-redos honest).
- Localhost (`127.0.0.1`) — legal Python socket test target.
