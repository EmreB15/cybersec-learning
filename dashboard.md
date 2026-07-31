# Cybersecurity Training Dashboard
*Last updated: 2026-07-31 — Session 25. **The dual-role feature finally ships** — computed since Increment 6, discarded every run, now in both output formats. Good code, bad teaching: read the post-mortem below before planning the next session.*

---

## Pickup Here

**RESUME AT — loginwatch Increment 10: "Nonzero exit on findings"** (`sys.exit` / exit codes). Unchanged from last session and still the right next step.
- **Groundwork:** he met exit code **2** from the receiving end at Inc 9, and chose `choices=` over his own `else` **because** argparse errors land on **stderr with a nonzero exit**. Increment 10 is him *emitting* a code instead of receiving one.
- **Design question:** is *"brute-force sources found"* an **error**, or a normal successful run that happened to find something? `grep`'s precedent — `0` = match, `1` = no match, `2` = error.
- **Live material:** the tool currently exits **1 on a bad path** (uncaught `FileNotFoundError`), which *collides* with grep's `1` = no-match convention.

> ### ⚠ Two standing rules, both earned this session
>
> **1. Show the path.** Every brief states the **full structural map up front** — which files change, which signatures change, what data moves between them, what decisions he'll face. Withhold the *how*, never the *what-changes*. Dripping structure out one question at a time is what wrecked this session.
>
> **2. Failure first.** *"Prioritise me seeing the failure and then either teaching me the fix or me finding the fix naturally."* Don't warn about defects whose consequence doesn't exist yet. Plant them; let them detonate.

**🌱 Planted lesson for Increment 11 — do not pre-empt.** The two loops over `failed_and_accepted` ([report.py:16](../sectools/report.py#L16) and `:25`) iterate a **set**, so output order flips between runs — verified, 4 of 10 runs printed the reverse order on identical input. He was told; he pushed back that the consequence doesn't exist until `run-daily.sh` diffs yesterday against today, and that teaching it now is an abstraction with no felt need. **He's right and the deferral was accepted.** At Increment 11: let him build the diff, let it fire a **false positive on unchanged data**, *then* let him find the cause.

---

**Done this session (25):** ~1h20 of a booked 2h, ended early by agreement.

**The spec's headline feature reached the output.** `find_accepted_and_failed` had run on every invocation since Increment 6 with its return value dropped on the floor — dual-role IPs, the "thinks like a defender" feature named in `SPEC.md` line 16, never printed. Now `create_report` takes the dual-role set and prints a `DUAL-ROLE IP` section; `create_csv_report` takes the set *and* the failed-counts dict and emits a `finding_type` discriminator column. Fixture extended with an `Accepted` line for `192.0.2.55`, so a dual-role IP now exists **below** the threshold — the feature demonstrably catches what the count check cannot see.

**He won the design argument on a better rationale than the tutor's.** Offered Option A (`finding_type` column, rows are findings) vs Option B (`dual_role` boolean, rows are IPs). The tutor's case for A was schema stability. **His** case was **detector yield** — a type column lets you count how many findings each detector produced, which is what tells you whether a rule earns its place:

```
$ ... --format csv | tail -n +2 | cut -d, -f1 | sort | uniq -c
      2 brute_force
      2 dual_role
```

That's detection engineering, and it's the better reason. *(One sharpening given: overlap ≠ redundancy — `198.51.100.22` fires both detectors, but `192.0.2.55` fires only one, so neither is redundant. Redundancy is subset, not intersection.)*

**Second strong call:** he passed the **failed-counts dict** into `create_csv_report` rather than changing `find_accepted_and_failed` to return `(ip, count)` pairs. The shorter route would have coupled a detector to a reporting need. He kept the seam he drew at Increment 3 — and didn't pass `failed_ips` to `create_report`, which has no use for it.

### 🔴 Teaching post-mortem — four tutor-side defects

He arrived enjoying the work and planning picoCTF after. He left saying the session had turned something motivating into *"stressful"*, and came close to walking out of it. Root cause and contributors:

1. **Scope dripped instead of mapped** *(root cause)* — table target given, then `create_report` needed a new parameter, then the CSV needed counts nobody was passing, then the seam decision was forced mid-build. All structural, all belonged in the brief.
2. **Two consecutive malformed briefs** — the first mixed tutor commentary into a block presented as literal program output; the rewrite contained a visible self-correction mid-block.
3. **Handed back a problem the tutor had agreed to own** — he asked, correctly, why *he* was editing sample data. Tutor agreed, then reported an edit collision back to him instead of finishing the job.
4. **Flagged a defect without pointing at it** — "sort them" with no line reference; he reasonably read it as sorting the input log.

**Second session running where his pushback on *method* was right on the merits** (cf. 2026-07-29 gotcha-framing and the WP001 retirement). His read on how he learns is reliable and should be treated as data, not mood.

**Not done:** Increment 10 (exit codes) — the planned Part B.

**⭐ Head-of-Year Review (Fable):** due **2026-08-06** — speaks **first** at bootstrap. Next session or the one after. It should read the post-mortem above.

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

- **Interface:** CLI only. **Status: 10/15 increments — detection spine complete, both output formats complete, real CLI complete, and as of 2026-07-31 the dual-role feature actually reaches the output.**
- **Repo:** `/home/emrebektas/sectools` — 6 commits through `e25dd91`. **2026-07-31 dual-role work uncommitted at write time.** **GitHub not yet created.**

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
| — | *Debt clear: dual-role IPs into both formats* | *`finding_type` discriminator column · schema contracts* | ✅ |
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
| Python | **L2 (in progress)** | loginwatch 10/15 | 4 (L1) | L1 complete; **L2 underway via loginwatch.** Primary focus. `argparse` + piping-ready output = **L2's "tool building" criteria substantially met.** Multi-file data flow and output-schema design added 2026-07-31. |
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
| **2026-07-31** | **Failure first — don't pre-empt defects whose consequence doesn't exist yet.** | *"Prioritise me seeing the failure and then either teaching me the fix or me finding the fix naturally."* A fix with no observable consequence is an abstraction with no felt need; after the failure fires, it's a lesson that sticks. |
| **2026-07-31** | **Show the path — briefs state the full structural map up front.** | Withholding *structure* isn't tiered hinting, it's an unclear spec. Withhold the *how*; never the *what-changes*. |
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
- ~~**Dead computation** — `find_accepted_and_failed`'s result discarded.~~ **Closed 2026-07-31** — dual-role IPs now print in both formats.
- **Output-schema versioning** — the CSV contract changed on 2026-07-31: a row used to mean *"this IP exceeded the threshold"*; now `192.0.2.55` appears with 3 failures under a threshold of 5. `finding_type` keeps a filtering consumer correct, but any consumer assuming *row ⇒ brute force* is now reading a false statement. Becomes live the moment anything downstream parses this. Taught once, not retested.
- **Invariant at a distance** — `failed_count[record]` is a bare dict lookup whose safety lives in a *different file*: `find_accepted_and_failed` returns an intersection with the failed set, so the key always exists. Correct today; would `KeyError` here with a traceback pointing at the wrong place if that ever became a union.
- **Loop-variable rebinding** — `create_csv_report` uses `record` for three different shapes in seven lines. Raised 🟢, not fixed, his call.
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

**Next session:** **Increment 10 — nonzero exit on findings** (`sys.exit`). **Brief it with a full structural map up front** — files, signatures, data flow, decisions — per the standing rule above. Short/low-energy instead? **Bandit 11+** (ROT13 next) or ship `sectools` public.
**Python (L2):** continues through loginwatch. Tool-building criteria substantially met.
**Bash (L2):** scripting basics arrive at Increments 11–12; awk revisit baked in.
**Scenarios:** locked until Python L2 + Bash L2 both complete.

---

## Cross-Track Connections

**14 logged.** One added 2026-07-31 — ***schema design driven by a shell one-liner***: he picked the `finding_type`-column CSV shape over a boolean-column shape **because** `cut -d, -f1 | sort | uniq -c` can then count findings per detector. The `sort | uniq -c` pipeline from Bash L0/L1 came back as the *reason* for a Python output-schema decision — Bash consumption shaping Python authorship, same direction as the stderr link below.

Two added 2026-07-30 — both from the deliberate Bandit→sectools pairing:
- ***the CLI contract, from both sides in one session*** — 70 minutes obeying other people's contracts (`ssh -p 2220`, `find / -user X -size 33c`, `base64 -d`), then writing his own. He reasoned out positional-vs-optional **before** knowing the syntax. Result: *"it makes soo much more sense now."*
- ***stderr, from redirecting it to emitting on it*** — `2>/dev/null` in Bandit, then `choices=` chosen over his own `else` **because** argparse errors land on stderr with exit 2 rather than stdout with exit 0. Bash stream discipline driving a Python API decision.

*Previously (2026-07-29): stdout as the composability seam · byte-level inspection.*

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Total challenges completed: **11** · attempted-unfinished: 2
- `loginwatch` increments: **10 / 15** (+ dual-role debt cleared)
- Bandit levels cleared: **11** (bandit0→11)
- Total sessions: **25** · Total hours: **~23.8**
- Weak points mastered: **2** (WP002, WP004) · retired: 1 (WP001)
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**~7.3 hours over 5 sessions** in the 7 days to 2026-07-31 — **inside the 5–10h band.** Five sessions in nine days is the near-daily rhythm he said he wanted.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop.
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed** (not needed until end of project arc).
- `sectools` (`/home/emrebektas/sectools`) — loginwatch build, 10/15 increments, 6 commits through `e25dd91` (2026-07-31 dual-role work uncommitted), GitHub repo not yet created.
- Localhost (`127.0.0.1`) — legal Python socket test target.
