# Cybersecurity Training Dashboard
*Last updated: 2026-07-30 — Session 24. **Bandit 6→11** (five levels, one past target) **+ `loginwatch` 9/15 → 10/15** (Increment 9, `argparse` — the ⚠wall cleared). `loginwatch` is now a **real CLI tool**. Increment 10 (exit codes) next.*

---

## Pickup Here

**RESUME AT — loginwatch Increment 10: "Nonzero exit on findings"** (`sys.exit` / exit codes).
- **Unusually good groundwork:** he *met* exit code **2** this session from the receiving end — argparse rejecting `--format xml`, `--threshold abc`, and a missing path. He also chose `choices=` over his own `else` **because** argparse errors go to **stderr with a nonzero exit** while his `else` printed to **stdout with exit 0**. He already has the model; Increment 10 is him *emitting* a code instead of receiving one.
- **The hook:** a detector that always exits `0` can't be branched on by `run-daily.sh` at Increment 11 (`if ./loginwatch.py …; then`). That's what `$?` is for.
- **Design question to put to him:** is *"brute-force sources found"* an **error**, or a normal successful run that happened to find something? Show `grep`'s precedent — `0` = match, `1` = no match, `2` = error.
- Files in `/home/emrebektas/sectools`: `loginwatch.py` (three `add_argument` calls + `args` wiring), `parser.py`, `report.py`. **Inc 9 uncommitted at write time.**

**Done this session (24):** the pairing he asked for by name — *"overthewire work into sectools work."* ~2h10.

**Bandit 6 → 11 (~70 min, solo, zero hints).** Two acquisitions he named himself:
- **`2>/dev/null`** — not a command but the realisation that a program has **two output streams that route independently**, and that a destination can be **nowhere**. He'd had `2>` and `2>&1` since Evidence Trail in May; the missing piece was `/dev/null` as a target.
- **`base64 -d` carried over from picoCTF** — he recognised the *shape* (alphanumeric text with `=` padding = encoding, not encryption), not the level. Unprompted transfer.
- Tutor posed the danger (empty output conflates *"found nothing"* with *"was blocked from looking"*); **he reached the collision himself**, then it was sharpened into false-negatives + the nastier case: `2>/dev/null` silences **your own typos**, so a broken command looks like a clean negative.

**Increment 9 — `argparse`, the ⚠wall — cleared without reaching a formal hint tier.** Every question he asked was a **syntax/API gap, never a reasoning gap**: does `add_argument` return the value (declare vs collect) · how does argparse tell positional from optional (the **dashes**; there is no `positional=True`) · does `required` mean "use the default" (`required` and `default` are opposite corners) · do I assign `parse_args()` (validation is the side effect, the return value is the payload).
- **Design calls, all his:** `path` positional — correct, and it matches his own `SPEC.md` line 13; `--threshold` / `--format` optional with defaults so the bare invocation still works; **`choices=` adopted over the `else`, justified by *channel*.**
- **One crash mid-build:** `required=True` on a positional → `TypeError`. Taught as a concept (positionals are required *by definition*; argparse refuses the contradiction rather than ignoring it), not patched as a one-word fix.
- **Verified by tutor:** behaviour preserved · `--format csv` · `--threshold 7` cuts to one row · `--help` generated with `{csv,table}` self-documenting · `--format xml` → exit 2 with **nothing** on stdout under `2>/dev/null` · `--threshold abc` rejected **before the log is opened**.
- **⚠ Accepted risk:** the `else` was removed as unreachable. A future `choices` entry added without a matching branch reintroduces silent-nothing. Named, accepted, his call.

**His headline, unprompted:** writing his first `--help` page retroactively made *every other tool's* `--help` legible — *"it makes soo much more sense now wow."* The consumer→author crossing, which is exactly what the pairing was built to produce. **His idea, not the tutor's.**

**Explanation quality** (last session's flagged concern) **held.** All support was lookup/API knowledge delivered plainly and up front; only the `2>/dev/null` danger was posed as a question — because that one *was* derivable from what he had on screen. **Keep that split.**

**⭐ Head-of-Year Review (Fable):** due **2026-08-06** — speaks **first** at bootstrap. Next session or the one after.

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

- **Interface:** CLI only. **Status: 10/15 increments — detection spine complete, both output formats complete, real CLI complete.**
- **Repo:** `/home/emrebektas/sectools` — 5 commits through `1def5b4`, **Inc 9 uncommitted**. **GitHub not yet created.**

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
| 9 | `argparse` CLI | **argparse** ⚠wall · positional vs optional · boundary validation | ✅ |
| 10 | Nonzero exit on findings | `sys.exit()` / exit codes | 🔜 next |
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
| Python | **L2 (in progress)** | loginwatch 10/15 | 4 (L1) | L1 complete; **L2 underway via loginwatch.** Primary focus. `argparse` + piping-ready output = **L2's "tool building" criteria substantially met.** |
| Bash | **L2 (pending)** | — | 4 (L1) | L1 complete. Last *formal* touch 2026-05-10, but **Bandit is carrying real Linux load** (11 levels; stream routing landed today). L2 proper arrives at Increments 11–12. |
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

- **Status: bandit11.** bandit0→6 cleared 2026-07-24; **bandit6→11 cleared 2026-07-30 — five levels, one past the briefed 6→10 target, solo, zero hints.** Sitting at bandit11 (ROT13), not started.
- **Banked:** `file`/`file -i`/`strings`/`xxd`, human-readable classification, glob-over-many-files, the `./` dash-prefix trick, **multi-predicate `find`**, **`2>/dev/null`**, **`base64 -d`**, **`xargs`**.
- **Paid off:** *(s23)* `cat -A`/`xxd` turned on his own Python output to expose a CRLF bug. *(s24)* **stream routing became a design principle** — `2>/dev/null` from the user's side, then `choices=` on stderr from the author's side, in the same session.
- **Cold-redo retest:** wipe notes, redo bandit0→6 cold **after 2–4 weeks** (i.e. from ~2026-08-07).
- **✅ Notes log is no longer empty.** He wrote the first entries in [external/bandit-notes.md](external/bandit-notes.md) himself at the wrap — unprompted, without being re-asked. **`2>/dev/null`** and **`xargs`** *(the latter never came up in conversation — it surfaced only in the file)*. The cold-redo retest now has something to check against. No passwords. https://overthewire.org/wargames/bandit/
- **OPSEC verified 2026-07-30:** `overthewire/notes.txt` holds level passwords, is covered by [.gitignore:11](.gitignore#L11), and `git log` confirms it has **never** been committed. Clean. *(Note: `external/bandit-notes.md` IS public — lessons only, no credentials.)*

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
- **`choices` / dispatcher drift** — the permitted-values list and the `if/elif` that acts on them are two places holding one fact. A structural fix (one source of truth) was named and **deliberately deferred** as a second concept. Revisit if a third format appears.
- **Dead computation** — `find_accepted_and_failed` runs every invocation and its result is discarded; **dual-role IPs are the spec's headline feature and never reach the report.** Pre-existing, not from Inc 9. Needs a home before the README is written.
- **`import parser`** — shadows a stdlib module name that was *removed* in Python 3.10, so it works here. On an older interpreter it would silently import the wrong thing. Rename before publishing.

---

## Checkpoints

- [x] Diagnostic complete *(2026-04-27)*
- [x] First L1-grade challenge completed cleanly *(2026-05-08)*
- [x] Bash L1 complete *(2026-05-10)* · Python L1 complete *(2026-05-11)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] Portfolio has 10+ archived write-ups *(2026-05-18 — 11 total)*
- [x] First L2 challenge started *(2026-07-18)* · **First multi-file Python program** *(2026-07-23)*
- [x] **First machine-readable tool output** *(2026-07-29 — `loginwatch` speaks CSV)*
- [x] **First real CLI — a tool someone else could run without editing the source** *(2026-07-30)*
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

**Next session:** **Increment 10 — nonzero exit on findings** (`sys.exit`; he's already met exit 2 from the receiving end). Optional 10-min warm-up: **Part B of Inc 9** — extract the interface into `cli.py`, leaving `loginwatch.py` as pure detection logic. Short/low-energy instead? **Bandit 11+** (ROT13 next) or ship `sectools` public.
**Python (L2):** continues through loginwatch. Tool-building criteria substantially met.
**Bash (L2):** scripting basics arrive at Increments 11–12; awk revisit baked in.
**Scenarios:** locked until Python L2 + Bash L2 both complete.

---

## Cross-Track Connections

**13 logged.** Two added 2026-07-30 — both from the deliberate Bandit→sectools pairing:
- ***the CLI contract, from both sides in one session*** — 70 minutes obeying other people's contracts (`ssh -p 2220`, `find / -user X -size 33c`, `base64 -d`), then writing his own. He reasoned out positional-vs-optional **before** knowing the syntax. Result: *"it makes soo much more sense now."*
- ***stderr, from redirecting it to emitting on it*** — `2>/dev/null` in Bandit, then `choices=` chosen over his own `else` **because** argparse errors land on stderr with exit 2 rather than stdout with exit 0. Bash stream discipline driving a Python API decision.

*Previously (2026-07-29): stdout as the composability seam · byte-level inspection.*

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Total challenges completed: **11** · attempted-unfinished: 2
- `loginwatch` increments: **10 / 15**
- Bandit levels cleared: **11** (bandit0→11)
- Total sessions: **24** · Total hours: **~22.5**
- Weak points mastered: **2** (WP002, WP004) · retired: 1 (WP001)
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**~6 hours over 4 sessions** in the 7 days to 2026-07-30 — **inside the 5–10h band.** Four sessions in eight days is the near-daily rhythm he said he wanted.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop.
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed** (not needed until end of project arc).
- `sectools` (`/home/emrebektas/sectools`) — loginwatch build, 9/15 increments, 4 commits (Inc 8 uncommitted), GitHub repo not yet created.
- Localhost (`127.0.0.1`) — legal Python socket test target.
