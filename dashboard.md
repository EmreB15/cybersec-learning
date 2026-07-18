# Cybersecurity Training Dashboard
*Last updated: 2026-07-18 — Session 19. **`loginwatch` build underway** — Increments 0–2 done, 3 next.*

---

## Pickup Here

**RESUME AT — Increment 3: "Split parser into `parser.py`, import it"** — the **first ⚠️ wall** (modules & import; first multi-file program).
- Move `parse_line` + `parse_file` out of `loginwatch.py` into a new `parser.py`; import them back into `loginwatch.py`.
- Introduce `if __name__ == "__main__":` so the temp test prints don't fire on import.
- New concept = **modules & import**. Deferred here on purpose — you'd already done two increments; a wall deserves a fresh head.

**Done this session (19):** Increment 1 `parse_line` (dict/`None` sentinel) and Increment 2 `parse_file` (list of 19 records, count reconciled). Both committed. Two bugs on Inc 1 (an always-True `if`, and dict shape — the shape one was **my** ambiguous brief, owned) and one on Inc 2 (`with` vs manual open) — all closed on revision, zero hints.

**Watch:** the `with` context-manager idiom slipped once (Inc 2) — confirm it fires unprompted the next file-open, or it becomes a logged WP.

**Two open TODOs before `sectools` goes public:**
1. **Spellcheck `SPEC.md`** (several typos, left as-is for your voice).
2. `sectools` GitHub repo **not created yet** — confirm before making public.

**Bandit:** still not started — wargame diversion now **deferred two sessions**. Push it next short/low-energy session.

**Lab gating:** Vulnerable target VM (Metasploitable2/DVWA) **still not installed** — not needed until the end of the project arc. Everything in `loginwatch` runs on synthetic logs + localhost. No blocker.

---

## Active Project — `loginwatch` (sectools blue-team toolkit)

**The baseline.** First portfolio project *and* the reference template for how every future project is approached, built, tested, and showcased. A CLI auth-log brute-force detector: aggregate failed logins by source IP, flag brute-force sources over a threshold, and surface **dual-role IPs** (Failed *and* Accepted = credential-compromise signal — the standout "thinks like a defender" feature, straight off the WP002 remediation).

- **Interface:** **CLI only, no GUI.** Visual layer for a security tool is a well-formed report (HTML/Markdown, arrives at stage 3). A GUI reads as a student project.
- **Repo:** separate clean public repo at `/home/emrebektas/sectools` (local repo initialized; **GitHub not yet created — confirm before making public**). Kept apart from this journal so hiring managers never see hint logs.
- **Lifecycle deliverables:** spec · modular package (parser/analyze/report/cli) · pytest w/ adversarial fixtures · README + MANUAL · `install.sh` · `run-daily.sh` (cron) · `pyproject.toml` + entry point · optional CI badge.
- **Pedagogy:** user writes every line (tutor hints only); one new concept per increment; **test fixtures = the verify-don't-proxy habit trained in code**; awk revisit folded into Increment 11.

**Increment plan** (each is one short session; ✅ = done):

| # | Increment | New concept | |
|---|-----------|-------------|---|
| 0 | Spec + dir skeleton | what a spec is / project structure — *was the WP001 retest* | ✅ |
| 1 | `parse_line` → dict/None | function returning a dict + None sentinel | ✅ |
| 2 | `parse_file` → records | composing a helper across lines | ✅ |
| 3 | Split into `parser.py`, import | **modules & import** (first multi-file) ⚠️wall | 🔜 next |
| 4 | `count_failed_by_ip` | dict accumulation (bridge from `sort\|uniq -c`) | ⬜ |
| 5 | `flag_suspicious(threshold)` | sorting dict items by value | ⬜ |
| 6 | Dual-role IP detection | set operations / cross-referencing ⭐ | ⬜ |
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

## North Star (direction, not blueprint)

**blue-team → red-team → cloud security → AI security.** Cloud + AI security are the ~12–18 month destination ("where I want and need to be"); AI security is the highest-differentiation target and the user has an edge (builds with AI daily). **The through-line:** the transferable asset is the tool-building discipline, not the domain — each phase re-points the same muscle at a harder domain. Phases 2–4 are **deliberately not architected yet** (design depends on skills acquired en route; AI security moves too fast to plan a year out). Focus is **only** `loginwatch` for now.

---

## Linux Gym — OverTheWire Bandit (wargame diversions)

Self-directed **Linux CLI fluency** practice running in parallel with the project. Free, legal (OverTheWire issues the credentials), no VM. **The tutor proactively pushes you to it** — *"go do some wargames"* — it's not just an offer.

- **When it fires:** ≥7 days since your last Bandit touch · a short/low-energy session · or a Linux-CLI gap that surfaced in project work. **Floor: ~1 in 5 sessions is Linux-CLI**, so Python project work never starves your terminal skills.
- **How:** log anything that stumps you in [external/bandit-notes.md](external/bandit-notes.md) (no passwords); the tutor pulls recurring gaps into teaching.
- **Status:** not started — mechanic live as of 2026-07-16. Start page: https://overthewire.org/wargames/bandit/

---

## Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| Python | **L1 OK → L2** | ████ 4/4 | 4 | **L1 COMPLETE** — L2 open. WP004 mastered. **Primary focus.** |
| Bash | **L1 OK → L2** | ████ 4/3 | 4 | **L1 COMPLETE** — L2 open. WP002 mastered. **Primary focus.** |
| Concepts | **ARCHIVED** | ████ 3/3 | 3 | **Archived 2026-07-16** — L1 was complete; retained for history, reinstatable |
| Scenarios | — | Locked | 0 | Unlocks when **Python L2 + Bash L2** both complete |

---

## Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. Enumeration of sections now holds first-pass; remaining gap is **parameter values + format constraints** slipping unprompted (SPEC.md: `>5` vs `≥`, missing `##` headings). | 2 | 0 | **2026-07-31** (held stage 2 via SPEC.md retest 2026-07-17) |

**Carried-forward discipline (no longer a standalone retest):** *verify-don't-proxy* — verify what you claim instead of substituting confidence for a check. Was tracked by WP002 (bash, mastered), WP003 + WP005 (concepts, now paused). **Watch for it inside Python/Bash code review.**

---

## Paused Weak Points (Concepts track archived)

| ID | Track | Issue | Stage at pause | Note |
|----|-------|-------|----------------|------|
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without the verification step. Two clean retests (HMRC, GitHub). | 2 | Paused 2026-07-16. Reinstates if Concepts returns. |
| WP005 | concepts | Vuln triage skips the version-check step before deciding response. One clean retest (NVD-for-version-check named unprompted). | 1 | Paused 2026-07-16. Reinstates if Concepts returns. |

---

## Mastered Weak Points

| ID | Track | Mastered Date | Closed Via |
|----|-------|---------------|------------|
| WP002 | bash | 2026-05-21 | Remediation challenge ("Don't Trust the Pipeline") — both fingerprints closed |
| WP004 | python | 2026-05-24 | Second clean retest — lazy-iteration discipline fired unprompted on a fresh question shape |

---

## Program Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| **2026-07-16** | **Archive the Concepts track; focus on Python + Bash + Linux terminal.** | Concepts absorbed over time via the OU R60 degree. Coding + Bash is the hard, scarce skill; user needs to code nearly every day to get good. Hands-on doing takes priority over standalone concept exercises. Concepts retained for possible reinstatement; scenario unlock relaxed to Python L2 + Bash L2; WP003/WP005 paused; security reasoning folded into challenge CONTEXT. |

---

## Watch-Areas & Spaced-Repetition Flags

- **awk action-block syntax** — third+ exposure still not durable. **Untouched 6+ sessions.** Pair with Bash L2 entry (scripting basics). *(High priority now that Bash is a primary focus.)*
- *(WA003 — concepts incident-response interpretation — dormant with the Concepts track archived.)*

---

## Checkpoints

- [x] Diagnostic complete — starting levels confirmed *(2026-04-27)*
- [x] First challenge completed on any track *(2026-04-28 — Bash L0 First Footprints)*
- [x] First L1-grade challenge completed cleanly *(2026-05-08 — Bash L1 Find Tour)*
- [x] First track reaches Level 1 complete — Bash L1 *(2026-05-10)*
- [x] Second track reaches Level 1 complete — Python L1 *(2026-05-11)*
- [x] First weak point mastered — WP002 *(2026-05-21)*
- [x] Second weak point mastered — WP004 *(2026-05-24)*
- [x] Portfolio has 10+ archived write-ups *(2026-05-18 — 11 total)*
- [x] **First L2 challenge started (Python or Bash)** *(2026-07-18 — loginwatch Increments 1–2, Python L2)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Side Tasks Still Open

- **Vulnerable target VM install (Metasploitable2/DVWA)** — highest-leverage lab unblock for L2/L3 network work.
- **awk action-block syntax** durable-revisit — folds into Bash L2 scripting basics.
- Redirection `<` operator: user reports never trained; introduce as new content when relevant to a Bash task.
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried since session 6.)*
- External courses budget decision — user has TryHackMe subscription unused. *(Now aligns well with the coding-focus pivot — OverTheWire Bandit for Bash, PortSwigger for Python L2 web work.)*

---

## Up Next

**Next session:** Increment 3 — split into `parser.py` + `import` (first ⚠️ wall). Short/low-energy session? Push a Bandit re-warm instead — still not started.
**Python (L2):** port scanner / subdomain enumerator / log anomaly detector / hash identifier.
**Bash (L2):** scripting basics — variables, loops, conditionals, exit codes; awk-syntax revisit baked in.
**Scenarios:** locked until Python L2 + Bash L2 both complete.

---

## Cross-Track Connections

**7 logged.** *(Python ↔ Bash tooling equivalences — the through-line for the coding-focus pivot.)*

---

## Portfolio Stats

- Write-ups generated: **11**
- Write-ups archived: **11**
- Total challenges completed: **11**
- Total challenges attempted-unfinished: 2
- Total sessions: **19**
- Total hours: **~17.5**
- Weak points mastered: **2** (WP002, WP004)
- Active tracks: **Python, Bash** *(Concepts archived 2026-07-16)*

---

## Lab Status

- Ubuntu VM running (host attacker box) — now native Pop!_OS laptop post-migration.
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**.
- `labs/bash-L1/triage/` — reusable.
- Localhost (`127.0.0.1`) as a fully-legal Python socket test target.
- `python/L1/` — six scripts (foundation for L2 tool-building).
