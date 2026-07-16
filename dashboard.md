# Cybersecurity Training Dashboard
*Last updated: 2026-07-16 — Session 17. **PROGRAM PIVOT: Concepts track archived** to focus on hands-on coding + Bash + Linux terminal.*

---

## Pickup Here

**PROGRAM CHANGE (2026-07-16) — Concepts track ARCHIVED.**
- **Why (user's call):** *"concepts will eventually be learnt"* (the OU R60 degree covers theory); the hard, scarce skill is **coding and Bash**, and *"I need to be coding nearly every day if I want to get good at it."* From here, practical effort goes into **doing** — coding tasks, Bash tasks, terminal work.
- Concepts is **archived, not deleted** — record retained, reinstatable if you change your mind.
- **Scenario missions now unlock on Python L2 + Bash L2 only** (Concepts L2 requirement dropped).
- **WP003 + WP005 (both Concepts) are paused** — not failed, not mastered. The discipline they track (verify-don't-proxy) is the same family as WP002 and now gets watched inside Python/Bash code review.
- Security reasoning isn't dropped — it moves into the **CONTEXT** section of every coding/Bash challenge.

**NEXT ACTION — agree the plan for coding + Bash:**
1. **Cadence** — user wants near-daily coding. Decide session shape (short daily reps vs. longer blocks) and how L2 challenges get sized to fit.
2. **First L2 challenge** — two live candidates:
   - **Python L2** — port scanner (localhost-only until a vulnerable VM lands; builds on the First Knock TCP-probe primitive) / subdomain enumerator / log anomaly detector / hash identifier.
   - **Bash L2** — scripting basics (variables, loops, conditionals, exit codes). **Bake in the awk action-block syntax revisit** — untouched 6+ sessions, still not durable.
3. **WP001 retest still live** (cross-track instruction-precision, stage 2 → mastered if pass, overdue from 2026-05-29) — knock it out via a Bash/Python multi-sub-task brief, before or alongside first L2 content.

**Re-warm note:** 53-day gap since last working session (2026-05-24). First session back is re-warm, not a sprint.

**Lab gating:** Vulnerable target VM (Metasploitable2/DVWA) **still not installed.** Blocks broadest L2/L3 paths in Python and Bash. Localhost (`127.0.0.1`) remains the only legal scanning surface until then.

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
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. Clean when the brief enumerates deliverables explicitly; slips when implicit. | 2 | 0 | **Overdue (was 2026-05-29)** — run via Bash/Python multi-sub-task brief |

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
- [ ] **First L2 challenge started (Python or Bash)** ← next milestone
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

**Next session:** agree coding/Bash cadence + first L2 challenge; run the live WP001 retest via a Bash/Python multi-sub-task brief.
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
- Total sessions: **17**
- Total hours: **~15.5**
- Weak points mastered: **2** (WP002, WP004)
- Active tracks: **Python, Bash** *(Concepts archived 2026-07-16)*

---

## Lab Status

- Ubuntu VM running (host attacker box) — now native Pop!_OS laptop post-migration.
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**.
- `labs/bash-L1/triage/` — reusable.
- Localhost (`127.0.0.1`) as a fully-legal Python socket test target.
- `python/L1/` — six scripts (foundation for L2 tool-building).
