# 🛡️ Cybersecurity Training Dashboard
*Last updated: 2026-05-08 — after Session 5 (Bash retests + Find Tour pass; trust-break arc closed; WP002 description corrected mid-session)*

---

## 🎯 Pickup Here

**Next session: redirection-focused Bash L1 challenge to close the level.**

> 📌 **Bash L1 is at 3/3 challenges, but NOT yet complete.** The level criterion requires redirection (`>`, `>>`, `2>`, `2>&1`) to be covered, and Find Tour was deliberately scoped find-only. One more challenge needed: redirection-only, single-concept, scoped tight per the one-concept-per-challenge rule.

> ⚠️ **Retests prioritised over new content. Both run before the redirection challenge if session date is on/after the retest date:**
> - **WP002 retest — due 2026-05-12** *(failures = 1, stage 0; third failure triggers a remediation challenge)*
> - **WP001 retest — due 2026-05-15** *(stage 1, 0 failures)*

> ⏰ **Stale-track watch:** Python and Concepts last touched 2026-04-27 → will trip the 14-day neglect flag on 2026-05-11 if untouched.

> 🔧 **Tutor process from Sessions 4 + 5 — confirmed in effect:**
> 1. **One new concept per challenge** at level boundaries.
> 2. **Verify before claiming** — every expected count gets the command run first.
> 3. **Precise meta-comms** — no scope-ambiguous words without spelling out concretely.
> 4. **Brief explicitness** *(new 2026-05-08)* — concrete inputs (patterns, literals, values) go in task descriptions, not buried as examples in Constraints.

**Side tasks still open (portfolio polish):**
- Archive `bash-L0-first-footprints` write-up — still has `<target>` placeholder.
- Decide whether `bash-L0-trail-in-the-logs` write-up needs a correction note — its "Key Concepts" and "Security Implication" sections still propagate the WP002 *"`sort -r` misranks ≥10"* claim that was empirically falsified 2026-05-08.

---

## 📊 Track Progress

| Track | Level | Progress | Challenges Done | Status |
|-------|-------|----------|-----------------|--------|
| 🐍 Python | L1 | ░░░░ 0/4 | 0 | 🟢 Ready to start (untouched 11 days) |
| 🖥️ Bash | L1 | ███ 3/3 | 3 | 🟡 Challenges met; **redirection still required** to close level |
| 🔐 Concepts | L1 | ░░░ 0/3 | 0 | 🟢 Ready to start (untouched 11 days) |
| 🎭 Scenarios | — | Locked | 0 | 🔒 |

**Bash L1 completion criterion:** *3 challenges done + redirection covered.* Challenges-done bar met; redirection bar not. **One more challenge needed**, redirection-focused.

---

## 📝 Session 5 Summary (2026-05-08)

- ✅ **WP001 retest passed.** `head -5`, `tail -3`, `grep -c 'sudo'` — three precise sub-tasks, three correct outputs, no chaining. Used `grep -c` rather than piping to `wc -l` (single-tool idiomatic). Stage 0 → 1, next retest **2026-05-15**.
- ❌ **WP002 retest failed.** Pipeline produced the correct top IP (`203.0.113.45` with 11 hits) but missed two explicit brief criteria: (1) no `Failed`-only filter — `awk '{print $13}'` ran on Accepted lines too where `$13` is the source port not the IP, polluting the count list with three rogue port-number rows; (2) no intermediate-stage inspection performed before stating the answer. Discipline practiced post-hoc after tutor pushed. Failures → 1, next retest **2026-05-12**.
- 🔁 **WP002 description corrected mid-session.** Verified empirically that the original *"`sort -r` misranks counts ≥10 lexicographically"* claim is wrong on raw `uniq -c` output — column padding makes lex order match numeric order. Tested on both the original Trail in the Logs `auth.log` and a fresh retest dataset with counts spanning 3–11. Description and evidence rewritten to reflect what's actually demonstrated.
- ✅ **Bash L1 Find Tour passed.** All 4 tasks correct against pre-verified outputs. `-mtime -14` sign syntax right first try, both globs (`"*.sh"`, `".*"`) properly quoted, `-type f` scaffold carried consistently. Task 2 surfaced both deliberately-seeded IOCs (`tmp/suspicious_payload.sh`, `tmp/.hidden_dropper`).
- 🆕 **New durable feedback memory:** brief-explicitness — concrete inputs go in the task description, not buried as examples inside Constraints.
- 🛡️ **Tutor process held throughout:** verify-before-claiming caught the WP002 over-claim mid-session and led to a clean retraction; precise-meta-comms held; one-concept-per-challenge held (find-only, redirection deferred).

**Trust-break arc from 2026-04-29: closed.** First clean L1 challenge, with verified counts on every assertion.

---

## ⚠️ Active Weak Points

| ID | Track | Issue | Stage | Failures | Retest Due |
|----|-------|-------|-------|----------|------------|
| WP001 | cross-track | Instruction-precision: identifies right tool but misses sub-tasks or substitutes parameters | **1** *(↑ from 0)* | 0 | **2026-05-15** |
| WP002 | bash | Frequency-count pipelines: skips count-column sorting, trusts pipeline output without inspecting intermediate stages | 0 | **1** *(↑ from 0)* | **2026-05-12** |

**WP001 retest history:**
- 2026-05-08 — passed cleanly. Brief Precision: 3 sub-tasks, all parameters exactly as briefed, single-tool answers.

**WP002 retest history:**
- 2026-05-08 — failed. Frequency Recall: correct answer surfaced but missed `Failed`-only filter and intermediate inspection (both explicit brief criteria). Discipline only emerged after tutor pushed for the inspection step.

> ℹ️ **WP002 description updated 2026-05-08.** Earlier evidence of *"`sort -r` would misrank counts ≥10 by lexicographic comparison"* was verified empirically and **falsified** — `uniq -c` column padding preserves numeric order under lex sort on the raw pipeline. The trap only fires if leading whitespace is stripped (e.g., post-`awk` processing). The round-1 bug from Trail in the Logs (no count-column sort at all) remains real and earned. The round-2 *"`sort -r` is iffy"* concern was correct as a discipline reflection but not as a functional misranking on this data shape.

---

## 👀 Watch-Areas

| ID | Track | Observation | Source |
|----|-------|-------------|--------|
| WA002 | Concepts | Phishing indicator list partial (misses link inspection, missing specifics, vague sign-off) | Diagnostic task 5 |

*WA001 promoted to WP001 on 2026-04-28.*

---

## 📅 Retests Scheduled

| Date | Weak Point | Track | Stage | Failures |
|------|-----------|-------|-------|----------|
| **2026-05-12** | WP002 (frequency-count pipelines) | bash | 0 | 1 *(third failure → remediation challenge)* |
| **2026-05-15** | WP001 (instruction-precision) | cross-track | 1 → 2 if pass | 0 |

---

## 🏁 Checkpoints

- [x] **Diagnostic complete — starting levels confirmed** *(2026-04-27)*
- [x] **First challenge completed on any track** *(2026-04-28 — Bash L0 First Footprints)*
- [x] **Lab environment partially set up — Ubuntu VM running** *(2026-04-28)*
- [x] **First L1-grade challenge completed cleanly** *(2026-05-08 — Bash L1 Find Tour; trust-break arc closed)*
- [ ] All tracks reach Level 1 complete
- [ ] Lab environment fully set up — vulnerable target VM (Metasploitable2/DVWA) installed
- [ ] Scenarios unlocked — all tracks at Level 2
- [ ] First scenario completed
- [ ] All tracks reach Level 3
- [ ] First employer-grade scenario completed
- [ ] Portfolio has 10+ archived write-ups

---

## 🗺️ Up Next

**Bash:** Final L1 challenge — redirection-focused, single-concept (`>`, `>>`, `2>`, `2>&1`). Scoped tight. Closes Bash L1.
**Concepts (L1):** First challenge — full phishing analysis with a systematic indicator framework, direct response to WA002. **Untouched 11 days** — flag at 14.
**Python (L1):** First challenge — log file reader or password strength evaluator. **Untouched 11 days** — flag at 14.
**Scenarios:** 🔒 Locked until all tracks reach L2.

---

## 🔗 Cross-Track Connections

**3 logged.** *(No new ones added in session 5 — find didn't trigger a natural cross-link this session; the redirection challenge will likely surface 1–2.)*

- *2026-04-28* — **Bash ↔ Python**: reading first/last N lines. Bash: `head -n N` / `tail -n N`. Python: `open() + readlines()[:N]` or `[-N:]`. Bash version is a pipe-ready one-shot; Python version composes inside larger scripts.
- *2026-04-28* — **Bash ↔ Python**: frequency analysis. Bash: `... | sort | uniq -c | sort -nr | head -n N`. Python: `collections.Counter(iterable).most_common(N)`. **Same gotcha in both**: default sort/min/max on numeric strings is lexicographic — `sorted(['10','9'])` returns `['10','9']` in Python too. Convert to int first.
- *2026-04-28* — **Bash ↔ Python**: positional field extraction is fragile. `awk '{print $11}'` and `line.split()[10]` both break the moment log format shifts a column. Real-world fix in either language is regex extraction (`grep -oE` / `re.search`) targeting the value's *shape*, not its *position*.

---

## 📈 Weekly Summary

**2026-05-02 → 2026-05-08:** 1 session, ~70 minutes total. **Below the 5h target** — but the gap was the user-stated post-session-4 break. Trust restored; tempo can rebuild from here.

---

## 🧪 Lab Status

- ✅ Ubuntu VM running (host attacker box).
- ❌ Vulnerable target VM (Metasploitable2 / DVWA) — not yet installed. **Required before any scanning / network challenge.**
- ✅ `labs/bash-L1/triage/` verified clean *(8 files, mtimes intact)*. Reusable for redirection challenge.
- ✅ `labs/bash-L1/retest-wp002/auth-snippet.log` built and verified *(2026-05-08)*. Reusable for next WP002 retest.

---

## 📁 Portfolio Stats

- Write-ups generated: **3** *(↑ from 2)*
- Write-ups archived (with reflections filled): **2** *(↑ from 1; 1 still awaiting user fill — bash-L0-first-footprints)*
- Total challenges completed: **3** *(↑ from 2)*
- Total challenges attempted-unfinished: 2 *(both session 4, both tutor-side abandons)*
- Total sessions: **5** *(↑ from 4)*
- Total hours: **~3.9** *(↑ from 2.8)*
