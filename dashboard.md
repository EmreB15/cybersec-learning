# Cybersecurity Training Dashboard
*Last updated: 2026-07-29 — Session 23. **`loginwatch` 8/15 → 9/15** (Increment 8, `--format csv`). **WP001 retired at the user's instruction — the active weak-point board is now empty.** Increment 9 (`argparse`) next.*

---

## Pickup Here

**RESUME AT — loginwatch Increment 9: "`cli.py` with `argparse`"** — flagged ⚠**wall**.
- **Groundwork already laid:** `__main__` holds an `output_format` variable driving an `if/elif/else` dispatcher. `argparse`'s job is to supply that value from a real `--format` flag instead of a hardcoded literal.
- The **log path** (`data/auth-sample.log`) and the **threshold** (`5`) are also hardcoded — the other two obvious flags.
- **Keep the `else` branch.** It's what stops an unrecognised `--format` from silently printing nothing.
- Files in `/home/emrebektas/sectools`: `loginwatch.py`, `parser.py`, `report.py` (`create_report` table + `create_csv_report`).

**Done this session (23):** Increment 8 in the planned hour. Bandit briefed but not started.
- **`create_csv_report`** via `csv.writer(sys.stdout)`. First submission clean on all six specified constraints — including writing the header `source_ip,failed_count` correctly while `create_report`'s `'SOURCE IP'`/`'FAILED'` sat three lines above it.
- **Design reasoning arrived before the code:** asked whether `csv` needed a file, then justified stdout himself with Bash `>` and `|` — Bash shaping a Python API decision, the harder direction of transfer.
- **🟡 fixed — silent empty output.** The dispatcher had no `else`, so an unrecognised format printed *nothing* and exited successfully. For a detection tool that reads as *"scanned the log, found no brute-force sources."* A misconfiguration rendering as a clean bill of health. Also took the `"string"` → `"table"` rename unprompted (survives into the `--format` flag).
- **CRLF taught from zero.** `csv.writer` defaults to the `excel` dialect — `\r\n` on *every* platform, per RFC 4180. Invisible on screen, visible as `^M$` under `cat -A`. Fixed with `lineterminator="\n"`, verified. Framed as a **decision**: spreadsheet consumer → CRLF; Unix pipe → LF. *The consumer decides, not the OS you're sitting at.*

**Tutor defects owned (user-flagged, both conceded):** (1) the CRLF quirk was withheld as *"a defect you cannot see"* — gotcha framing applied to pure lookup knowledge. Withholding is fair only for reasoning available from what's on screen. (2) The control-comparison method was explained *before* teaching what `^M` is, leaving nothing to conclude. Verdict was blunt — *"all your explainations here have been poor"* — and the re-taught versions landed. **Explanation quality is the thing to watch next session.**

**⭐ Head-of-Year Review (Fable):** due **2026-08-06** — speaks **first** at bootstrap.

---

## Program Change — Weak-Point Tracking Retired

**2026-07-29, at the user's instruction.** WP001 moved to `retired_points` — stage 2, 0 failures, **neither mastered nor failed**.

> *"it is a weak point that will not just dissapear. ignore it and move on."*

The per-task ceremony had grown larger than the code review it was attached to. What changes: **no retests, no per-submission verdicts, no "this is the fingerprint" commentary.** If imprecision actually breaks code it gets flagged as a normal 🔴/🟡/🟢 issue on its own merits. The review protocol keeps its does-it-work / strong / weak / security-implication spine and drops the weak-point section. **This extends to any future weak point: log it, watch quietly, don't narrate it.**

*For the record, the last observation before retirement: all six specified parameter values and format constraints held unprompted on first submission — the exact facet the 2026-07-17 retest had named as the remaining gap.*

---

## Open Debts

1. **Ship `sectools` public.** Spellcheck SPEC.md + OPSEC scrub, create the GitHub repo, push. A real spec + tests already beat most junior CVs. **← the one remaining debt.**

---

## Active Project — `loginwatch` (sectools blue-team toolkit)

**The baseline.** First portfolio project *and* the reference template for how every future project is built, tested, and showcased. A CLI auth-log brute-force detector: aggregate failed logins by source IP, flag brute-force sources over a threshold, and surface **dual-role IPs** (Failed *and* Accepted = credential-compromise — the "thinks like a defender" feature).

- **Interface:** CLI only. **Status: 9/15 increments — detection spine complete, both output formats complete.**
- **Repo:** `/home/emrebektas/sectools` — 4 commits through `8be978d`, **Inc 8 uncommitted**. **GitHub not yet created.**

| # | Increment | New concept | |
|---|-----------|-------------|---|
| 0 | Spec + dir skeleton | what a spec is / project structure | ✅ |
| 1 | `parse_line` → dict/None | dict + None sentinel | ✅ |
| 2 | `parse_file` → records | composing a helper across lines | ✅ |
| 3 | Split into `parser.py`, import | **modules & import** ⚠wall | ✅ |
| 4 | `count_failed_by_ip` | dict accumulation (bridge from `sort\|uniq -c`) | ✅ |
| 5 | `flag_suspicious(threshold)` | sorting dict items by value | ✅ |
| 6 | Dual-role IP detection | set operations / cross-referencing ⭐ | ✅ |
| 7 | `report.py` text table | f-string alignment | ✅ |
| 8 | `--format csv` | **the `csv` module** + file-like objects + dialect defaults | ✅ |
| 9 | `cli.py` argparse | **argparse** ⚠wall | 🔜 next |
| 10 | Nonzero exit on findings | `sys.exit()` / exit codes | ⬜ |
| 11 | `run-daily.sh` | Bash vars + `$?` + `if` (+ **awk** revisit) ⚠wall | ⬜ |
| 12 | `install.sh` | Bash functions + heredoc + `set -euo pipefail` | ⬜ |
| 13 | pytest + fixtures | automated testing | ⬜ |
| 14 | `pyproject.toml` + entry point | packaging ⚠wall (MVP fallback: `python -m`) | ⬜ |
| 15 | README + MANUAL | technical documentation | ⬜ |

---

## Direction — spine + tastings

**One spine deep, cheap tastings of the rest.** Blue-team is rung one (nearest employable + shared fundamentals + loginwatch is blue); deliberate cheap tastings of **red / devsecops / AI-security** so exploration is designed in, not foreclosed. North star: **blue → red → cloud → AI**.

**Priority stack (user's framing):** degree *(theory evidence)* → **practical cyber *(the lever)*** → theory cyber *(absorbed)* → maths *(multiplier)* → trading *(roadblock, reloading via maths)*.

**Practice ladder:** ~~Bandit debt~~ ✅ → picoGym/CyLab (General Skills + Forensics) → blue platform (**TryHackMe SOC** + **CyberDefenders** for publishable DFIR write-ups) → HTB retired-easy (later) → CryptoHack (maths lane) / PortSwigger (later, red).

**CTF operating rules:** no AI before the flag, full AI after · ~30–45 min struggle floor + stuck-report · describe challenges in your own words · **cold-redo retest 2–4 weeks after a clean solve** · write-ups = failure trail + a defender's note.

⚠️ **Verify (unconfirmed vs cutoff):** picoCTF → "CyLab Security Academy" rename (~May 2026); TryHackMe cert name (SAL1?).

---

## Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| Python | **L2 (in progress)** | loginwatch 9/15 | 4 (L1) | L1 complete; **L2 underway via loginwatch.** Primary focus. |
| Bash | **L2 (pending)** | — | 4 (L1) | L1 complete. **Longest-neglected track — last formal touch 2026-05-10.** L2 arrives at Increments 11–12; Bandit/CTF carrying Linux load meanwhile. |
| Concepts | **ARCHIVED** | ████ 3/3 | 3 | Archived 2026-07-16 — retained for history, reinstatable. |
| Scenarios | — | Locked | 0 | Unlocks when Python L2 + Bash L2 both complete. |

---

## Active Weak Points

**None.** WP001 retired 2026-07-29 (see *Program Change* above); WP002 and WP004 mastered; WP003 and WP005 paused with the Concepts track.

| ID | Track | Issue | Final state | Disposition |
|----|-------|-------|-------------|-------------|
| WP001 | cross-track | Instruction-precision: right tool, parameter values / format constraints could slip. | Stage 2, 0 failures | **Retired 2026-07-29** — user instruction. Not mastered, not failed. |
| WP002 | bash | Frequency-count pipelines / trusting output without inspecting intermediates. | — | **Mastered 2026-05-21** via remediation challenge. |
| WP004 | python | Eager full-file load (`readlines`) instead of lazy iteration. | — | **Mastered 2026-05-24.** |
| WP003 | concepts | Declares "no indicator" without the verification step. | Stage 2 | Paused 2026-07-16. Reinstates if Concepts returns. |
| WP005 | concepts | Skips the version-check step before deciding response. | Stage 1 | Paused 2026-07-16. Reinstates if Concepts returns. |

**Carried-forward discipline (watched quietly inside code review, never narrated):** *verify-don't-proxy*.

---

## Linux Gym — OverTheWire Bandit

Self-directed **Linux CLI fluency** practice in parallel with the project. Free, legal, no VM.

- **Status:** bandit0 → 6 cleared (2026-07-24). Session 23 target **bandit6 → 10** was briefed but not started (user had to leave) — re-offer it. Banked so far: `file`/`file -i`/`strings`/`xxd`, human-readable classification, glob-over-many-files, the `./` dash-prefix trick.
- **Paid off this session:** `cat -A` and `xxd` turned on his *own Python output* to expose a CRLF bug — first time the Bandit toolkit was used as a debugging instrument rather than a puzzle-solver.
- **Cold-redo retest:** wipe notes, redo bandit0→6 cold **after 2–4 weeks**.
- **How:** log stumpers in [external/bandit-notes.md](external/bandit-notes.md) — *still empty; nothing logged from the bandit0→6 run.* No passwords. https://overthewire.org/wargames/bandit/

---

## Program Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| **2026-07-29** | **Retire WP001 and the per-task weak-point ceremony.** | The tracking had outgrown the code review it was attached to and read as repetitive nagging about a trait already known. Code correctness is the deliverable; precision issues get flagged as ordinary code issues when they actually break something. |
| **2026-07-29** | **Withholding is only fair for reasoning available on screen.** | Framing a library default (`csv.writer`'s CRLF) as a defect to be discovered is a gotcha, not teaching. Domain knowledge gets taught; reasoning gets prompted. |
| **2026-07-23** | Fortnightly Head-of-Year Review (Fable) that speaks first when due; "one spine deep, cheap tastings" lane model. | The teacher is too close to judge the multi-week arc. Practical cyber = #1 leverage; maths = cross-cutting multiplier. |
| **2026-07-16** | Archive the Concepts track; focus on Python + Bash + Linux terminal. | Concepts absorbed via the OU R60 degree. Coding + Bash is the hard, scarce skill. |

---

## Watch-Areas (teaching touches to re-offer — not graded)

- **`with` context-manager idiom** — slipped once at Inc 2, still not re-tested; `report.py` deliberately opens no file. Confirm at the next real file-open.
- **awk action-block syntax** — not yet durable. Folds into Increment 11.
- **Byte-level output verification** (`cat -A` / `xxd` on anything another program will read) — taught fresh at Inc 8. Natural next occasion is Increment 11's CSV post-processing.
- **CSV / formula injection** — `csv` escapes delimiters and quotes; it does *nothing* about a field starting `=`, `+`, `-`, `@` executing in a spreadsheet. Becomes live the moment a username or raw log message reaches a column. ⚠️ Verify at `owasp.org/www-community/attacks/CSV_Injection`.

---

## Checkpoints

- [x] Diagnostic complete *(2026-04-27)*
- [x] First L1-grade challenge completed cleanly *(2026-05-08)*
- [x] Bash L1 complete *(2026-05-10)* · Python L1 complete *(2026-05-11)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] Portfolio has 10+ archived write-ups *(2026-05-18 — 11 total)*
- [x] First L2 challenge started *(2026-07-18)* · **First multi-file Python program** *(2026-07-23)*
- [x] **First machine-readable tool output** *(2026-07-29 — `loginwatch` speaks CSV)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Side Tasks Still Open

- **Ship `sectools` public** — spellcheck SPEC.md + OPSEC pass + create GitHub repo *(the remaining debt)*.
- **Vulnerable target VM install (Metasploitable2/DVWA)** — not needed until the end of the project arc.
- Redirection `<` operator: never trained; introduce when a Bash task calls for it.
- `bash-L0-trail-in-the-logs` write-up: decide whether to add a WP002-falsification correction note. *(Carried since session 6.)*

---

## Up Next

**Next session:** **Increment 9 — `cli.py` with `argparse`** (⚠wall; the dispatcher is already shaped for it). Short/low-energy instead? Continue **Bandit** or ship `sectools` public.
**Python (L2):** continues through loginwatch.
**Bash (L2):** scripting basics arrive at Increments 11–12; awk revisit baked in.
**Scenarios:** locked until Python L2 + Bash L2 both complete.

---

## Cross-Track Connections

**11 logged.** Two added 2026-07-29:
- ***stdout as the composability seam*** — Bash `>` and `|` supplied the justification for a Python API decision (print, not return). Transfer in the harder direction: Bash shaping Python design, not Python reimplementing a Bash command.
- ***byte-level inspection*** — Bandit's `cat -A`/`xxd` pointed at his own Python program's output to expose `csv.writer`'s `\r\n` default.

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Total challenges completed: **11** · attempted-unfinished: 2
- `loginwatch` increments: **9 / 15**
- Bandit levels cleared: **6** (bandit0→6, session-23 target 6→10)
- Total sessions: **23** · Total hours: **~20.5**
- Weak points mastered: **2** (WP002, WP004) · retired: 1 (WP001)
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**~4 hours over 3 sessions** in the 7 days to 2026-07-29 — just under the 5–10h band, not drifting. Adding today: ~5h over 4 sessions.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop.
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed** (not needed until end of project arc).
- `sectools` (`/home/emrebektas/sectools`) — loginwatch build, 9/15 increments, 4 commits (Inc 8 uncommitted), GitHub repo not yet created.
- Localhost (`127.0.0.1`) — legal Python socket test target.
