# Cybersecurity Training Dashboard
*Last updated: 2026-05-24 — after Session 16 (triple-retest session: WP004 mastered, WP005 stage 0→1, WP003 stage 1→2; two weak points mastered overall in the programme)*

---

## Pickup Here

**SESSION 17 PRIORITY 1 — WP001 retest due 2026-05-29 (stage 2 → mastered if pass).**
- Cross-track instruction-precision retest.
- The multi-sub-task brief shape that worked for 2026-05-15 is the recommended pattern again.
- WP001 is the **last active weak point gating clean entry to L2 content with all WPs at stage 2+.** If it clears, only WP005 (stage 1, next 2026-05-31) and WP003 (stage 2, next 2026-06-07) remain active — both spaced out, neither blocking L2 entry.

**PRIORITY 2 — L2 ENTRY UNLOCKED on all three core tracks.** User declined L2 entry session 16 in favour of clean three-retest wrap; entry now fully available next session. Three candidate first L2 challenges:
- **Concepts L2 #1** — vulnerability classes / methodologies / defence frameworks. Pivot/L2-shape reasoning has shown reliably at L1 across **four** consecutive Concepts events (FLT, TLB original, TLB revision, WP005 retest). Entry pace probably does NOT need scaffolding.
- **Bash L2 #1** — scripting basics (variables, loops, conditionals, exit codes) with awk-syntax revisit baked in. **awk action-block syntax untouched 6 sessions running** (carried since session 10).
- **Python L2 #1** — port scanner (localhost-only until vulnerable VM lands); builds on First Knock primitive.

**PRIORITY 3 — Concepts L2 directed challenge banked.** Origin: session 16 WP005 retest. User named the load-bearing mental model unprompted: *"i always think the quicker we take the server down the less chance of being attacked"* — the intuition driving shutdown-primary disposition on proportional response laddering. Design shape: scenario with explicit cost asymmetry (active customer session draining mid-checkout, hot-failover available, plausible WAF rule) so the "take it down" reflex feels wrong from the inside, not from a tutor saying so. Pair with NIST SP 800-40r4 §3 ladder as the L2-grade content.

**PRIORITY 4 — Concepts L2 also has the syslog / log-file structural conventions gap.** Origin: WP004 retest 2026-05-24, user-named gap *"if you didnt tell me that these log files are already chronological i would have struggled."* Append-order = time order, line format components, severity facility codes. Natural fit alongside any L2 log-handling task.

**Lab gating:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed.** Blocks broadest L2/L3 paths in Python and Bash. Localhost (`127.0.0.1`) remains the only legal scanning surface until then.

---

## Session 16 Summary (2026-05-24 — ~2h, no formal time cap)

### Three retests, three passes, zero hint tiers

| Retest | Track | Outcome | Stage shift | Next due |
|---|---|---|---|---|
| **WP004** | python | **PASSED → MASTERED** | 1 → mastered | — |
| **WP005** | concepts | PASSED | 0 → 1 | 2026-05-31 |
| **WP003** | concepts | PASSED | 1 → 2 | 2026-06-07 |

**Active weak point count: 4 → 2** (WP001 + WP005; WP003 at stage 2 still listed but one retest from mastered).

### What landed

**WP004 — file iteration habit fired unprompted, on a fresh question shape.** [First and Last Failed](python/L1/retest_wp004_r2.py): print earliest and latest Failed-login timestamp from a 30-line synthetic auth log. User wrote `for line in f:` directly — no `f.readlines()` reach. Direct contrast to the original 2026-05-10 first version that defaulted to `for line in f.readlines():`. Different question shape from the 2026-05-15 retest (first/last timestamp vs distinct-count); same discipline fired. Lazy-iteration lesson landed as **habit, not recall.** Raw-string path notation `r'labs\...'` carried unprompted from the 2026-05-15 backslash-escape gotcha — specific lesson, specifically retained.

🟡 **Moderate teaching observation** (NOT a WP004 gate per process note 17): accumulator pattern grows with input size. User used `for line in f:` for the read but appended every Failed line into a list, then only ever read `[0]` and `[-1]`. Two scalars would carry the same info in constant memory. Lesson landed on the read step, not on the accumulator. Banked for future watching; not promoted to WP.

**WP005 — NVD-for-version-check named unprompted on fresh CVE scenario.** [Edge Proxy CVE Triage](concepts-track/L1/): fictional `CVE-2026-1847` nginx request-smuggling scenario, deployed version unspecified, colleague asks *"should I take the proxy offline?"*. User's reasoning explicitly named NVD for the version-check step *before* any response action: *"We should then check the NIST NVD to see if our version of nginx is vulnerable, this is key..."*. Direct contrast to:
- 2026-05-18 first pass — jumped from CVE-name-alongside-framework to *"halt any app, remove the framework"* with no version-check named.
- 2026-05-18 revision — verification concept landed but tool was `exploit-db` instead of NVD.

Today: NVD named correctly, before any response action, on a fresh scenario with no telegraph. Two-step verification gate sequenced correctly (MITRE CVE registry → NVD). Branching reasoning structure (*"if safe... if not safe... if attacked..."*). Three of four brief-cited sources used precisely.

🟡 **Moderate teaching observation** (in WP005's evidence scope but NOT a gate per process note 17): response-laddering disposition is **shutdown-primary**. Rungs 1-3 of the NIST SP 800-40r4 §3 ladder (patch in place → vendor mitigation → compensating control → take offline) not named; decision goes straight from *"we're vulnerable"* to *"take it offline."* Banked for Concepts L2 directed challenge.

**WP003 — verification habit unprompted across six lenses, GitHub security alert.** [github-secure.org sender, [Action Required] subject tag, 48-hour deadline, anchor-text-only link, no footer]. All six lenses substantive, **no "no indicator" defaults.** WP003 corrective behaviour fired on:
- **Lens 1** (sender) — verification implicit; user compared `github-secure.org` against known `github.com`, named the mismatch. Verify step internalised at this point — not written as *"verify: X"* because X was already known.
- **Lens 5** (links) — explicit verification named (*"hover over it and check the domain name, if it is not GitHub.com it can not be trusted"*).
- **Lens 6** (footer absence) — applied unprompted, **third consecutive instance.** Durable carry confirmed from the original 2026-05-10 tutor-walked explanation.

Plus disarming-pattern recognition in lens 3 (*"the attempt was blocked"* identified as false reassurance before the 48-hour threat) — reading the email's emotional arc, not just surface content.

### Honesty discipline — two instances same session

1. **WP004 — syslog-chronological gap named unprompted after the challenge:** *"if you didnt tell me that these log files are already chronological i would have struggled, that was the gap in my knowledge."* Underlying gap (syslog / log-file structural conventions) flagged for future L2 design.
2. **WP005 — underlying mental model named unprompted:** *"i always think the quicker we take the server down the less chance of being attacked."* User proactively requested a directed Concepts L2 challenge to dislodge it. Banked.

Pattern note: when the user names the **intuition** behind a finding (not just the finding), the dislodge-vector becomes a specific cost-asymmetry scenario, not abstract instruction.

### Pushback as positive signal — fifth consecutive session

Session 16 didn't have a direct tutor-evaluation pushback, but user pushback on session 15's framing about response laddering (wanting it as its own Concepts task) is the same discipline applied constructively. Generalising outward, holding.

### Hint tier log
**Zero across all three retests.** Two syntax-recall questions during WP004 (list slicing, `.join`) — concept clarifications, not tier escalations. Scope-clarification questions at challenge starts (month/date handling on WP004, source-use vs lookup on WP005) — verify-before-coding reflex, correct.

---

## Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| Python | **L1 OK** | ████ 4/4 | 4 | **COMPLETE** — ready for L2; **WP004 MASTERED 2026-05-24** |
| Bash | **L1 OK** | ████ 4/3 | 4 | **COMPLETE** — ready for L2; WP002 mastered 2026-05-21 |
| Concepts | **L1 OK** | ████ 3/3 | 3 | **COMPLETE** — ready for L2; WP003 stage 2 / WP005 stage 1 |
| Scenarios | — | Locked | 0 | Unlocks when all 3 core tracks reach L2 |

---

## Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. 2026-05-15 retest clean (stage 1→2). | 2 | 0 | **2026-05-29** |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing the verification step. **Two consecutive retests passed unprompted (HMRC 2026-05-16; GitHub 2026-05-24).** One more clean retest → mastered. | 2 | 0 | **2026-06-07** |
| WP005 | concepts | Vulnerability triage skips version-check step before deciding response. 2026-05-24 first retest: NVD-for-version-check named unprompted; response-laddering observation banked for Concepts L2 directed challenge. | 1 | 0 | **2026-05-31** |

**Retest history (most recent):**
- **WP004 (2026-05-24):** ✅ **PASSED — MASTERED.** Stage 1 → mastered. Second clean retest, different question shape; lazy-iteration discipline fired unprompted with no telegraph.
- **WP005 (2026-05-24):** ✅ **PASSED.** Stage 0 → 1. NVD-for-version-check named unprompted on fresh CVE-2026-1847 scenario. Shutdown-primary response laddering surfaced as teaching observation (banked, not WP-promoting).
- **WP003 (2026-05-24):** ✅ **PASSED.** Stage 1 → 2. GitHub security alert; six lenses substantive; verification habit fired on lenses 1/5/6 unprompted; lens 6 absence-as-indicator third consecutive instance.
- **WP002 (2026-05-21):** ✅ Passed remediation → MASTERED.

---

## Mastered Weak Points

| ID | Track | Mastered Date | Closed Via |
|----|-------|---------------|------------|
| WP002 | bash | 2026-05-21 | Remediation challenge ("Don't Trust the Pipeline") — both fingerprints closed (original 2026-04-28 no-count-sort + generalised 2026-05-10 trust-output-without-verification) |
| WP004 | python | **2026-05-24** | **Second clean retest** — Anki schedule, stage 1 → mastered; lazy-iteration discipline fired unprompted on a different question shape than the 2026-05-15 retest |

---

## Watch-Areas

| ID | Track | Issue | First Observed | Promotion Trigger |
|----|-------|-------|----------------|-------------------|
| WA003 | concepts | Incident-response interpretation on **credential-compromise patterns**: (1) hypothetical-framing of known events, (2) slow brute-force cadence read as innocuous, (3) action-ladder with IP-block as primary on confirmed credential success, (4) priority inversion (loud-failed > quiet-succeeded). | 2026-05-21 (WP002 remediation) | One more occurrence on a Concepts L2-shape **credential-compromise** IR scenario = WP |

**WA003 status note (added 2026-05-24):** the WP005 retest scenario was vuln-triage (no credential-compromise dynamics), so none of the four WA003 sub-shapes had surface to fire on. Promotion trigger did not fire. Status unchanged. The shutdown-primary disposition surfaced on WP005's response laddering is *related* (action-ladder ordering family) but distinct from WA003's credential-compromise-IP-block-primary shape, and is logged as a WP005 teaching observation rather than a WA003 instance.

**Spaced-repetition flag (informal, not a WP):**
- **awk action-block syntax** — needs revisit; third exposure still not durable. **Untouched six sessions running.** Pairs naturally with Bash L2 entry (scripting basics).

---

## Retests Scheduled

| Date | ID | Type | Track | Stage | Failures |
|------|------|------|-------|-------|----------|
| **2026-05-29** | WP001 | Retest *(stage 2 → mastered if pass)* | cross-track | 2 | 0 |
| **2026-05-31** | WP005 | Retest *(stage 1 → 2 if pass)* | concepts | 1 | 0 |
| **2026-06-07** | WP003 | Retest *(stage 2 → mastered if pass)* | concepts | 2 | 0 |

---

## Tutor Process Notes — in effect

1. One new concept per challenge at level boundaries.
2. Verify before claiming — every expected count gets the command run first.
3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
4. Brief explicitness — concrete inputs go in task descriptions, not buried in Constraints.
5. When introducing analysis frameworks, state explicitly *"if you don't know X, the lens output is verify X, not no indicator"*.
6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."*
7. When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`.
8. Never give a working answer and ask the user to "pick" from inside it.
9. When a Tier 1 reframe gets shortcut, do NOT escalate tiers during the challenge. Flag in review and let revision force the abstraction.
10. Brief-precision miss recurs when concrete deliverables are implicit. Count concrete deliverables explicitly. **VALIDATED 2026-05-15.**
11. Sustained Tier 1 (multiple reframes, same mode, no escalation) carries an entire challenge when the gap is conceptual rather than syntactic.
12. Before any network-touching challenge, deliver the ethics framing (UK CMA 1990 §1).
13. **Phishing-analysis retests test verification habit specifically when the email contains at least one lens-indicator the analyst cannot resolve from email content alone.** **VALIDATED 2026-05-16. GENERALISED 2026-05-18. VALIDATED AGAIN 2026-05-24** (GitHub security alert: sender domain + link-href + footer-conventions all required external knowledge to resolve).
14. *(Forming.)* When external-learning entries are noted but flagged "not sure why this matters", schedule a teach-first slot before any application slot. Origin: session 12 design-defect.
15. **Brief precision applies to the tutor as much as the user.** Every grading criterion must trace back to a property explicitly stated in the brief. **Origin 2026-05-18.**
16. **When retesting a cross-track-generalised weak point in a DIFFERENT brief format than prior retests, the new format must be telegraphed in the brief.** Otherwise the unprompted-discipline bar is unfair. **Origin 2026-05-19.** **APPLIED 2026-05-24** on WP004 retest (format-shift from single-integer to two-line formatted output telegraphed explicitly in the brief per this note).
17. **Evaluation scope must equal brief scope. If teaching territory surfaces outside the stated bar, demote it from "weakness" to "teaching observation" or schedule it for a more appropriate challenge.** **Origin 2026-05-21. APPLIED 2026-05-24** twice — WP004 accumulator finding kept as teaching not gate (file-iteration habit fired clean, that's the WP's strict scope); WP005 response-laddering finding kept as teaching not gate (NVD-version-check fired clean, that's the WP's top-line identity). Saved as durable feedback memory `feedback_evaluation_scope`.

---

## Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [x] **First L1-grade challenge completed cleanly** *(2026-05-08 — Bash L1 Find Tour)*
- [x] **All three core tracks active at L1** *(2026-05-10)*
- [x] **First track reaches Level 1 complete — Bash L1** *(2026-05-10)*
- [x] **Second track reaches Level 1 complete — Python L1** *(2026-05-11)*
- [x] **🏆 ALL TRACKS REACH LEVEL 1 COMPLETE** *(2026-05-18)*
- [x] **First weak point mastered — WP002** *(2026-05-21)*
- [x] **Second weak point mastered — WP004** *(2026-05-24)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [x] **Portfolio has 10+ archived write-ups** *(2026-05-18 — 11 total)*

---

## Side Tasks Still Open

- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried since session 6.)*
- External courses budget decision — user has TryHackMe subscription unused.
- Redirection `<` operator: user reports never trained; introduce as new content OR amend the session-10 recall check to drop Q4.
- Vulnerable target VM install (Metasploitable2/DVWA) — highest-leverage lab unblock.
- **NEW:** Syslog / log-file structural conventions teaching — origin WP004 retest 2026-05-24 user-named gap; pairs with any L2 log-handling task.
- **NEW:** Concepts L2 directed challenge on response laddering with explicit cost asymmetry — origin WP005 retest 2026-05-24 user-named mental model.

---

## Up Next

**Next session (Session 17):** WP001 retest 2026-05-29 (last active WP retest before everything is mastered or stage-2-or-higher). L2 entry available on all three tracks immediately after.
**Concepts (L2):** Available; entry pace probably does not need scaffolding.
**Bash (L2):** Available — scripting basics. awk-syntax revisit pairs naturally.
**Python (L2):** Available — port scanner / subdomain enumerator / log anomaly detector / hash identifier.
**Scenarios:** Locked until all three tracks at L2.

---

## Cross-Track Connections

**7 logged.** *(Unchanged — Session 16 was all retest work; no new tooling-equivalence link surfaced.)*

---

## Weekly Summary

**2026-05-18 → 2026-05-24 (closed):** 5 sessions (12, 13, 14, 15, 16), ~280 minutes (~**4h 40m**) — lower bound of the 5-10h/week target, but session 16 ran longest at ~2h and was unusually retest-heavy. Three sessions in the past three days (14, 15, 16) — solid recovery cadence after the earlier-week lighter pace.
**Next formal weekly summary regenerates 2026-05-31.**

---

## Lab Status

- Ubuntu VM running (host attacker box).
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**.
- `labs/bash-L1/triage/` — reusable.
- `labs/bash-L1/retest-wp002/` — retired (r1, 2026-05-08).
- `labs/bash-L1/retest-wp002-r2/` — retired (r2, 2026-05-15).
- `labs/bash-L1/retest-wp002-r3/` — retired (r3, 2026-05-19).
- `labs/bash-L1/wp002-remediation/` — used 2026-05-21 (remediation pass). **Retain** as reference for any future cross-track-generalised remediation design.
- `labs/python-L1/wp004-retest-r2/` — used 2026-05-24 (WP004 mastered). 30-line synthetic SSH auth log; First Failed `May 24 03:15:22`, Last Failed `May 24 22:20:18`.
- `python/L1/` — six scripts.
- `concepts-track/L1/` — `challenge-2-brief.md` (First Light Triage brief).
- Localhost (`127.0.0.1`) as a fully-legal Python socket test target.

---

## Portfolio Stats

- Write-ups generated: **11** *(unchanged — Session 16 was retest work; no new challenge writeups)*
- Write-ups archived: **11**
- Total challenges completed: **11**
- Total challenges attempted-unfinished: 2
- Total sessions: **16** *(↑ from 15)*
- Total hours: **~15.5** *(↑ from 13.5 — Session 16 ran ~2h)*
- **Weak points mastered: 2** *(↑ from 1 — WP004 closed 2026-05-24)*
