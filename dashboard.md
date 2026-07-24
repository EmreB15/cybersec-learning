# Cybersecurity Training Dashboard
*Last updated: 2026-07-24 — Session 21. **Bandit gym: bandit0 → 6 cleared** (debt #1 paid). `loginwatch` still 6/15 — Increment 6 (⭐ dual-role IPs) next.*

---

## Pickup Here

**RESUME AT — loginwatch Increment 6: "Dual-role IP detection (Failed ∩ Accepted)"** — the ⭐ standout defender feature (unchanged; Bandit was the low-energy diversion this session).
- Build a function that finds IPs appearing in **both** the Failed set and the Accepted set (failed-then-succeeded = credential-compromise signal).
- New concept = **set operations / cross-referencing**.
- Expected single result on `data/auth-sample.log`: **198.51.100.22** (6 Failed + 1 Accepted). Your Increment 4 counter is already sitting on this evidence.

**Done this session (21):** Bandit gym — cleared **bandit0 → 6** self-directed (target was 0→4, +2 over). **Debt #1 (Bandit, deferred 3×) paid.** Taught `file` / `file -i` (MIME) / `strings` / `xxd` for human-readable-vs-binary classification, `file * | grep text` to bulk-classify a whole directory, the `./` dash-prefix gotcha, and "most tools take a *list* of filenames."

**OPSEC win:** refused to read the level-password file into tutor context unprompted — right reflex. Tutor elevated the real threat model (the **public repo**, not context) and gitignored `overthewire/` — it was untracked and one `git add -A` from a public password leak.

**Cold-redo agreed:** wipe `overthewire/notes.txt` and redo bandit0→6 **cold after 2–4 weeks** — a genuine retention check against the forget-across-time problem.

**Watch:** the `with` context-manager idiom still wasn't re-tested (no new file-open) — confirm it fires unprompted next file-open, or it becomes a logged WP.

**⭐ Head-of-Year Review (Fable):** fortnightly trajectory review runs **first** at bootstrap when due. **First one is due 2026-08-06.**

---

## Open Debts (clear before opening new platforms)

1. ~~**Bandit — not started.**~~ ✅ **PAID 2026-07-24** — bandit0→6 cleared, first Bandit session. Follow-up is the cold-redo retest (wipe + redo after 2–4 weeks), not a debt.
2. **Ship `sectools` public.** Spellcheck SPEC.md + OPSEC scrub, confirm GitHub repo creation, push. A real spec + tests already beat most junior CVs. **← the one remaining debt.**

---

## Head-of-Year Review — Fable (fortnightly)

Program-level trajectory oversight, distinct from the teacher's per-session work. **Teacher = the in-session tutor; head of year = Fable, stepping back across weeks.**

- **Conducted by:** a **Fable agent** (mandatory). **Cadence:** every 14 days.
- **When due, it speaks FIRST** at bootstrap — before greeting or planning (user instruction 2026-07-23).
- **Shape:** what got done · on-track read · drift · refine-or-stay · 1–3 focus priorities for the next fortnight.
- **Next due:** **2026-08-06.** State in `progress.json.head_of_year_review`; protocol in CLAUDE.md 2026-07-23 amendment + bootstrap step 10.

---

## Active Project — `loginwatch` (sectools blue-team toolkit)

**The baseline.** First portfolio project *and* the reference template for how every future project is built, tested, and showcased. A CLI auth-log brute-force detector: aggregate failed logins by source IP, flag brute-force sources over a threshold, and surface **dual-role IPs** (Failed *and* Accepted = credential-compromise — the "thinks like a defender" feature).

- **Interface:** CLI only. Visual layer = a well-formed report (arrives ~Increment 7). **Status: 6/15 increments, detection spine complete.**
- **Repo:** clean public repo at `/home/emrebektas/sectools` (local, 3 commits; **GitHub not yet created — confirm before public**).

**Increment plan** (✅ = done):

| # | Increment | New concept | |
|---|-----------|-------------|---|
| 0 | Spec + dir skeleton | what a spec is / project structure | ✅ |
| 1 | `parse_line` → dict/None | dict + None sentinel | ✅ |
| 2 | `parse_file` → records | composing a helper across lines | ✅ |
| 3 | Split into `parser.py`, import | **modules & import** (first multi-file) ⚠️wall | ✅ |
| 4 | `count_failed_by_ip` | dict accumulation (bridge from `sort\|uniq -c`) | ✅ |
| 5 | `flag_suspicious(threshold)` | sorting dict items by value | ✅ |
| 6 | Dual-role IP detection | set operations / cross-referencing ⭐ | 🔜 next |
| 7 | `report.py` text table | f-string alignment | ⬜ |
| 8 | `--format csv` | the `csv` module | ⬜ |
| 9 | `cli.py` argparse | **argparse** ⚠️wall | ⬜ |
| 10 | Nonzero exit on findings | `sys.exit()` / exit codes | ⬜ |
| 11 | `run-daily.sh` | Bash vars + `$?` + `if` (+ **awk** revisit) ⚠️wall | ⬜ |
| 12 | `install.sh` | Bash functions + heredoc + `set -euo pipefail` | ⬜ |
| 13 | pytest + fixtures | automated testing (= verify-don't-proxy in code) | ⬜ |
| 14 | `pyproject.toml` + entry point | packaging ⚠️wall (MVP fallback: `python -m`) | ⬜ |
| 15 | README + MANUAL | technical documentation | ⬜ |

---

## Direction — spine + tastings (session 20 coaching)

**One spine deep, cheap tastings of the rest.** Blue-team is rung one (nearest employable + shared fundamentals + loginwatch is blue); deliberate cheap tastings of **red / devsecops / AI-security** so exploration is designed in, not foreclosed. North star unchanged: **blue → red → cloud → AI** (AI security = highest-differentiation destination).

**Priority stack (user's framing):** degree *(theory evidence)* → **practical cyber *(the lever)*** → theory cyber *(absorbed)* → maths *(multiplier — feeds trading/AI/crypto; active lever while trading is blocked)* → trading *(roadblock, reloading via maths)*.

**Practice ladder:** pay Bandit debt → picoGym/CyLab (General Skills + Forensics) → blue platform (**TryHackMe SOC**, already owned + **CyberDefenders** for publishable DFIR write-ups) → HTB retired-easy (later, Bash L3-ish) → CryptoHack (enjoyment/maths lane, no public write-ups) / PortSwigger (later, red).

**CTF operating rules:** no AI before the flag, full AI after · ~30–45 min struggle floor + stuck-report · describe challenges in your own words · **cold-redo retest 2–4 weeks after a clean solve** · write-ups = failure trail + a defender's note.

*Two visual artifacts (strategy board, roadmap) were produced this session, then de-prioritized in favour of the recurring Fable review — not maintained resources.*

⚠️ **Verify (Fable-sourced, unconfirmed vs Jan-2026 cutoff):** picoCTF → "CyLab Security Academy" rename (~May 2026); TryHackMe cert name (SAL1?).

---

## Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| Python | **L2 (in progress)** | loginwatch 6/15 | 4 (L1) | L1 complete; **L2 underway via loginwatch.** Primary focus. |
| Bash | **L2 (pending)** | — | 4 (L1) | L1 complete; L2 arrives at loginwatch Increments 11–12 (Bash scripts) + awk revisit. |
| Concepts | **ARCHIVED** | ████ 3/3 | 3 | Archived 2026-07-16 — retained for history, reinstatable. |
| Scenarios | — | Locked | 0 | Unlocks when Python L2 + Bash L2 both complete. |

---

## Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: right tool, but parameter values / format constraints can slip unprompted. **Positive signal 2026-07-23:** `>=` boundary held unprompted at loginwatch Inc 5 — the exact gap this retest targets. | 2 | 0 | **2026-07-31** |

**Carried-forward discipline (no standalone retest):** *verify-don't-proxy* — watched inside Python/Bash code review. Fired unprompted twice this session (Failed-only filter in Inc 4; boundary in Inc 5).

---

## Paused Weak Points (Concepts archived)

| ID | Track | Issue | Stage at pause | Note |
|----|-------|-------|----------------|------|
| WP003 | concepts | Phishing analysis: declares "no indicator" without the verification step. | 2 | Paused 2026-07-16. Reinstates if Concepts returns. |
| WP005 | concepts | Vuln triage skips the version-check step before deciding response. | 1 | Paused 2026-07-16. Reinstates if Concepts returns. |

---

## Mastered Weak Points

| ID | Track | Mastered Date | Closed Via |
|----|-------|---------------|------------|
| WP002 | bash | 2026-05-21 | Remediation challenge ("Don't Trust the Pipeline") — both fingerprints closed |
| WP004 | python | 2026-05-24 | Second clean retest — lazy-iteration discipline fired unprompted |

---

## Linux Gym — OverTheWire Bandit (wargame diversions)

Self-directed **Linux CLI fluency** practice in parallel with the project. Free, legal, no VM. **The tutor proactively pushes you to it.**

- **Status:** **started 2026-07-24 — cleared bandit0 → 6** (session 21, first Bandit session). Banked: `file`/`file -i`/`strings`/`xxd`, human-readable classification, glob-over-many-files, the `./` dash-prefix trick.
- **Cold-redo retest:** wipe `overthewire/notes.txt`, redo bandit0→6 cold **after 2–4 weeks** — retention check against the forget-across-time problem.
- **How:** log stumpers in [external/bandit-notes.md](external/bandit-notes.md) (no passwords). Continue: https://overthewire.org/wargames/bandit/

---

## Program Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| **2026-07-23** | **(A) Fortnightly Head-of-Year Review (Fable) that speaks first when due. (B) "One spine deep, cheap tastings" lane model + blue rung on the CTF ladder.** | Teacher is too close to judge the multi-week arc — a head-of-year role (Fable) tracks trajectory, serving the forget-across-time problem at program level. User pushed back on over-steering to blue → depth-first on blue + deliberate tastings of red/devsecops/AI. Practical cyber = #1 leverage; maths = cross-cutting multiplier. |
| **2026-07-16** | Archive the Concepts track; focus on Python + Bash + Linux terminal. | Concepts absorbed via the OU R60 degree. Coding + Bash is the hard, scarce skill; user needs to code nearly every day. |

---

## Watch-Areas & Spaced-Repetition Flags

- **awk action-block syntax** — still not durable. Folds into loginwatch Increment 11 (run-daily.sh CSV post-processing).
- **`with` context-manager idiom** — slipped once at Inc 2; not re-tested Inc 3–5. Confirm unprompted next file-open or log a WP.

---

## Checkpoints

- [x] Diagnostic complete *(2026-04-27)*
- [x] First L1-grade challenge completed cleanly *(2026-05-08)*
- [x] Bash L1 complete *(2026-05-10)* · Python L1 complete *(2026-05-11)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] Portfolio has 10+ archived write-ups *(2026-05-18 — 11 total)*
- [x] First L2 challenge started *(2026-07-18 — loginwatch, Python L2)*
- [x] **First multi-file Python program** *(2026-07-23 — loginwatch Increment 3)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Side Tasks Still Open

- **Ship `sectools` public** — spellcheck SPEC.md + OPSEC pass + create GitHub repo *(debt #2)*.
- **Bandit** — start it, next short session *(debt #1)*.
- **Vulnerable target VM install (Metasploitable2/DVWA)** — not needed until the end of the project arc.
- Redirection `<` operator: user reports never trained; introduce when a Bash task calls for it.
- `bash-L0-trail-in-the-logs` write-up: decide whether to add a WP002-falsification correction note. *(Carried since session 6.)*

---

## Up Next

**Next session:** Increment 6 — dual-role IP detection (⭐ set operations). Short/low-energy again? **Continue Bandit** (bandit6 onward) or ship `sectools` public.
**Python (L2):** continues through loginwatch.
**Bash (L2):** scripting basics arrive at Increments 11–12; awk revisit baked in.
**Scenarios:** locked until Python L2 + Bash L2 both complete.

---

## Cross-Track Connections

**8 logged.** Latest (2026-07-23): *Python dict accumulation ≡ Bash `sort | uniq -c`* — the WP002 frequency-count, re-expressed in Python at loginwatch Increment 4.

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Total challenges completed: **11** · attempted-unfinished: 2
- `loginwatch` increments: **6 / 15**
- Bandit levels cleared: **6** (bandit0→6)
- Total sessions: **21** · Total hours: **~18.5**
- Weak points mastered: **2** (WP002, WP004)
- Active tracks: **Python, Bash** *(Concepts archived 2026-07-16)*

---

## Lab Status

- Host attacker box — native Pop!_OS laptop.
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed** (not needed until end of project arc).
- `sectools` (`/home/emrebektas/sectools`) — loginwatch build, 6/15 increments, 3 commits, GitHub repo not yet created.
- Localhost (`127.0.0.1`) — legal Python socket test target.
