# Cybersecurity Training Dashboard
*Last updated: 2026-05-16 — after Session 11 (short focused session: WP003 retest passed clean, stage 0 → 1)*

---

## Pickup Here

**Next session: no overdue retests. WP002 (2026-05-19) is closest — HIGHEST STAKES.** Failures = 2; one more failure triggers a remediation challenge. Design as a fresh bash frequency-count with the **retest-wp002-r3** dataset (generate before session). The verify-don't-proxy discipline must fire **unprompted** on first submission.

Until 2026-05-19 the session can be flexible — new content, awk-syntax revisit, or side-task closure.

> **Retest queue (priority order — nothing overdue):**
> 1. **WP002 — due 2026-05-19** *(bash frequency-count discipline; failures = 2, stage 0; **next failure = remediation challenge** — highest-stakes retest)*
> 2. **WP004 — due 2026-05-22** *(python file iteration; stage 1; one more clean retest = mastered)*
> 3. **WP003 — due 2026-05-23** *(concepts phishing analysis; stage 1; one more clean retest = stage 2)*
> 4. **WP001 — due 2026-05-29** *(cross-track instruction precision; stage 2; one more clean retest = mastered)*

> **New content options:**
> - **Bash L2 #1** — scripting basics (variables, loops, conditionals, exit codes). Lab depends on choice: file organiser / log monitor reuse existing labs; ping sweep needs Metasploitable target.
> - **Python L2 #1** — tool-building (subprocess, argparse, pipe-friendly output). Port scanner scales First Knock primitive across a range with concurrency; subdomain enumerator, log anomaly detector, hash identifier are alternatives.
> - **Concepts L1 #2** — NOW UNLOCKED (WP003 cleared). Candidate placement for the THM unresolved entry (shodan / censys / virustotal / exploit database — flagged 2026/05/11 "not too sure why they are important").

> **Spaced-repetition flag (carried forward):**
> - **awk action-block syntax** — third L0/L1 exposure on session 10 still needed full T1→T2→T3 escalation; user reports "awk just doesn't sit in my mind". Treat as syntax-recall gap (like redirection operators), not conceptual. Untouched session 11 — schedule a short revisit alongside next bash work.

> **Tutor process — confirmed in effect:**
> 1. One new concept per challenge at level boundaries.
> 2. Verify before claiming — every expected count gets the command run first.
> 3. Precise meta-comms — no scope-ambiguous words without spelling out concretely.
> 4. Brief explicitness — concrete inputs go in task descriptions, not buried as examples in Constraints.
> 5. When introducing analysis frameworks, explicitly state *"if you don't know X, the lens output is verify X, not no indicator"*.
> 6. When using real-world brand impersonations as phishing props, preface with *"X is a real company that does Y."* (skipped for HMRC on session 11 — UK user, real UK tax authority, not unfamiliar).
> 7. When a single command takes multiple inputs, never describe them as *"X AND Y"* in caps — operator-clash with shell `&&`. Use *"two paths together"* or list with commas.
> 8. Never give a working answer and ask the user to "pick" from inside it. Either give the answer cleanly OR show a placeholder for them to fill — not both.
> 9. When a Tier 1 reframe gets shortcut (user takes the easier step and stops), do NOT escalate tiers during the challenge. Flag in review and let revision force the abstraction.
> 10. Brief-precision miss recurs when concrete deliverables are implicit. When designing briefs, count concrete deliverables explicitly. **VALIDATED 2026-05-15.**
> 11. Sustained Tier 1 (multiple reframes, same mode, no escalation) carries an entire challenge when the gap is conceptual rather than syntactic.
> 12. Before any network-touching challenge, deliver the ethics framing (UK CMA 1990 §1; target must be own machine / own VM / written-authorisation lab). Restate in shorter form at start of each subsequent network challenge.
> 13. **Phishing-analysis retests test verification habit specifically when the email contains at least one lens-indicator the analyst cannot resolve from email content alone.** Without that, you're only testing recall of indicator types, not the corrective method. **VALIDATED 2026-05-16** — HMRC retest worked because lens 1 (real domain unknown to user without lookup) and lens 5 (link rendered as anchor text only) were both verify-or-skip traps.

**Side tasks still open:**
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note for the WP002 falsification. *(Carried forward from session 6.)*
- External courses budget decision — user has TryHackMe subscription unused.
- THM unresolved entry: shodan / censys / virustotal / exploit database — strong candidate for Concepts L1 #2 placement now that WP003 has cleared.
- Redirection `<` operator: user reports never trained; introduce as new content in a future bash session, OR amend the session-10 recall check to drop Q4.

**Lab status flag:** Vulnerable target VM (Metasploitable2/DVWA) **STILL not installed** — highest-leverage side task to unblock the broadest L2/L3 paths.

---

## Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| Python | **L1 OK** | ████ 4/4 | 4 | **COMPLETE** — ready for L2; WP004 retest passed 2026-05-15, stage 1 |
| Bash | **L1 OK** | ████ 4/3 | 4 | **COMPLETE** — ready for L2 |
| Concepts | L1 | █░░ 1/3 | 1 | Active — WP003 cleared 2026-05-16, **L1 #2 now unlocked** |
| Scenarios | — | Locked | 0 | Unlocks when all 3 core tracks reach L2 |

---

## Session 11 Summary (2026-05-16 — 30-min planned, ~20-min actual, under-ran cleanly)

### Retest run

**WP003 ✅ PASSED — Phishing Analysis (HMRC tax-refund impersonation, fresh email, no scaffold).**

Verification habit fired **unprompted** on both trap lenses:
- **Lens 1 (sender):** User named real HMRC domain (`hmrc.gov.uk` / `gov.uk`), compared against `refunds@hmrc-services.org.uk`, called the mismatch. Exact WP003 corrected behaviour on a NEW email with no redo pressure.
- **Lens 5 (links):** Chained verification step ("hover the link, check the domain ends in `.gov.uk`") with payload hypothesis ("sign-in page that steals bank details"). Analyst-grade reasoning, not just "link suspicious".
- **Lens 6 (sign-off / footer):** Absence-as-indicator applied unprompted ("no footer, no copyright, no contact details; you can expect an email from an organisation to have some sort of sophisticated footer"). Durable carry from the 2026-05-10 tutor-walked explanation.

Two minor misses logged, not promoted:
- 🟢 Lens 3 missed the "Dear Taxpayer" generic greeting (HMRC has the user's name from PAYE — generic greeting on personalised-claim email is a classic tell).
- 🟢 Lens 4 substituted pressure analysis for analysis of the ask itself. The ask is "confirm your details" — vague (what details?) and contradicts how real HMRC refunds work (direct to bank, no portal confirmation).

Both interpretable as scope ambiguity on lens prompts; not a WP001 substitution miss. **Zero hint tiers used.** **Stage 0 → 1.** Next retest 2026-05-23.

### Key process observation

- **Phishing-retest design principle validated.** The retest worked because the email contained at least one lens-indicator the analyst cannot resolve from email content alone (lens 1 needs brand-domain knowledge; lens 5 needs URL inspection). That's what tests the verification habit specifically. Without such a trap, a phishing retest only tests recall of indicator types, not the corrective method. Promoted to tutor process note 13.

### No new content

User offered three options at the 20-min mark (wrap / awk syntax revisit / lens discussion); chose clean wrap on the passed retest. Valid call given the short session length and the strong-pass result.

---

## Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters. 2026-05-15 retest clean pass on explicitly-enumerated brief; same session showed two soft misses on briefs with implicit enumeration. | 2 | 0 | **2026-05-29** |
| WP002 | bash | Frequency-count pipelines / verify-don't-proxy generalisation: trust visible output without inspecting adjacent evidence. 2026-05-15 retest FAILED — same fingerprint as 2026-05-08 (correct top answer surfaces, verification not run unprompted). | 0 | **2** | **2026-05-19** ⚠️ |
| WP003 | concepts | Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step. **2026-05-16 retest PASSED** — verification habit fired unprompted on both trap lenses (sender domain comparison + link hover/inspect with payload hypothesis). Stage 0 → 1. | 1 | 0 | **2026-05-23** |
| WP004 | python | File iteration defaults to `f.readlines()` instead of `for line in f:`. 2026-05-15 retest PASSED — lazy iteration unprompted on first submission. | 1 | 0 | **2026-05-22** |

**Cross-track pattern note:** WP002 (skip-the-inspection-step) and the cross-language data points (use-a-cheap-proxy-instead-of-the-real-test; generalise-from-one-observation; skip-the-named-verification-step) are the same underlying habit. WP003's 2026-05-16 pass is a positive data point on the same family — verification habit fired unprompted on a new instance, in a different track. Remediation challenge remains one WP002 failure away.

**Retest history (most recent):**
- **WP003 (2026-05-16):** ✅ PASSED. Fresh HMRC phishing email, verification habit unprompted on lenses 1 and 5. Stage 0 → 1.
- **WP001 (2026-05-15):** ✅ PASSED. Multi-sub-task brief, 4/4 sub-tasks first pass, no nudges. Stage 1 → 2.
- **WP002 (2026-05-15):** ❌ FAILED. Same fingerprint as 2026-05-08 (correct answer, no verification). Failures 1 → 2.
- **WP004 (2026-05-15):** ✅ PASSED. Lazy iteration unprompted. Stage 0 → 1.

---

## Watch-Areas

**Spaced-repetition flag (informal, not a WP):**
- **awk action-block syntax** — needs revisit; third exposure still not durable. Untouched session 11.

---

## Retests + Recall Checks Scheduled

| Date | ID | Type | Track | Stage | Failures |
|------|------|------|-------|-------|----------|
| **2026-05-19** | WP002 | Retest | bash | 0 | 2 *(next failure → remediation challenge)* |
| **2026-05-22** | WP004 | Retest | python | 1 | 0 |
| **2026-05-23** | WP003 | Retest | concepts | 1 | 0 |
| **2026-05-29** | WP001 | Retest | cross-track | 2 → mastered if pass | 0 |

---

## Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [x] **First L1-grade challenge completed cleanly** *(2026-05-08 — Bash L1 Find Tour)*
- [x] **All three core tracks active at L1** *(2026-05-10)*
- [x] **First track reaches Level 1 complete — Bash L1** *(2026-05-10)*
- [x] **Second track reaches Level 1 complete — Python L1** *(2026-05-11; WP004 retest passed 2026-05-15 confirms)*
- [ ] All tracks reach Level 1 complete *(Concepts 1/3 remaining — L1 #2 now unlocked after WP003 pass)*
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups *(currently 9 — 1 to go)*

---

## Up Next

**Concepts (L1):** L1 #2 now unlocked. Candidate placement for the THM unresolved entry (shodan / censys / virustotal / exploit database).
**Bash (L2):** Available — scripting basics. Awk-syntax revisit fits here too.
**Python (L2):** Available — port scanner / subdomain enumerator / log anomaly detector / hash identifier.
**Scenarios:** Locked.

---

## Cross-Track Connections

**7 logged.** *(Unchanged — no new content session.)*

---

## Weekly Summary

**2026-05-08 → 2026-05-15 (last regen):** 4 sessions, ~370 minutes total (~**6h 10m**). Within 5–10h target. Both Bash L1 and Python L1 closed in this period. Trajectory healthy. **Next formal weekly summary regenerates 2026-05-22.**

---

## Lab Status

- Ubuntu VM running (host attacker box).
- Vulnerable target VM (Metasploitable2 / DVWA) — **still not installed**. Highest-leverage side task.
- `labs/bash-L1/triage/` — reusable.
- `labs/bash-L1/retest-wp002/` — retired (used 2026-05-08; r2 set replaces for future retests).
- `labs/bash-L1/retest-wp002-r2/` — built 2026-05-15. 30 lines, 28 Failed + 2 Accepted, top IP 45.142.122.81 (12). Filter trap on 185.220.101.50 (in BOTH columns). 5 distinct invalid usernames. **For 2026-05-19 WP002 retest: generate retest-wp002-r3 if pattern-matching is a concern, otherwise reuse r2.**
- `python/L1/` — contains five scripts: `log_filter.py`, `ip_extractor.py`, `password_audit.py`, `port_check.py`, `retest_wp004.py`.
- Localhost (`127.0.0.1`) as a fully-legal Python socket test target — pattern established session 9.

---

## Portfolio Stats

- Write-ups generated: **9** *(unchanged — retests don't generate write-ups)*
- Write-ups archived: **9** *(unchanged)*
- Total challenges completed: **9** *(unchanged)*
- Total challenges attempted-unfinished: 2 *(unchanged)*
- Total sessions: **11** *(↑ from 10)*
- Total hours: **~10.9** *(↑ from 10.6)*
