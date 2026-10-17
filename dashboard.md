# Cybersecurity Training Dashboard
*Last updated: 2026-10-17 — Session 31. **A new tool, three increments, and the first project session in four that he closed on a win instead of walking away from it.***

---

## Pickup Here

> ### ⭐ CONTINUE `passcheck` — it is a live build with building work left.
> No backfilling with upkeep. The repo is clean, 21 commits, **35 tests green**, and [PASSCHECK-SPEC.md](../sectools/PASSCHECK-SPEC.md) holds the increment map.

**Where it stands:** `derive.py` is **38 lines, four pure functions, all his** — `case_variants`, `year_variants`, `leet_variants`, `build_candidate_set`. Increments 1, 2 and 4 are done; 3 was deliberately deferred past 4.

**Next build — Increment 5: `screen(password, candidates)`** returning a verdict *plus which fact and which rule chain matched*, then **Increment 6 (argparse CLI)**. That pair turns `passcheck` from a module he imports into a tool he can run on a real password. Increment 6 reuses argparse he already did in `loginwatch`, so **5 is where the thinking is**. Increment 3 (`joins`) is the alternative if he wants something purely mechanical — same concept as increment 2, no new machinery, pure typing volume.

> ### 📌 THE ONE CORRECTION FROM TONIGHT — and it is a REPEAT, not a new rule
> **Incidental machinery must be handed to him, not discovered.** Before writing any brief, list the operations the objective actually requires and check each one has already been given to him. If not, it goes in the brief. Tonight's only escalation traces entirely to this. **Per the head of year's explicit call, no eighth teaching rule was written.**
>
> Also: when describing an accumulator, say **one set, one loop, and what happens per item.** The Tier 3 wording for stage C ("starts as a copy of stage B, then loop over stage B") was muddled and he was right to call it.

**Repeat verbatim next session — this is what worked:** offer two or three builds and let him pick · lock the frozen corpus and spec section in the repo **before** he starts, with the pass condition stated as a number · tell him **pytest is the green light, not the tutor** · one commit per increment.

**Not to be volunteered as "Python work":** the `loginwatch` write-up (debt #2 — raise as a separate errand) · `loginwatch` Increments 11/12 when he wants **Bash** · packaging or docs for either project.

---

## Session 31 (2026-10-17) — `passcheck` increments 1, 2 and 4

**Two hours, stated and measured** — 22:00 to 00:00, the first measured duration in six sessions. Three increments, three commits, no demoralised ending.

He picked the build from three offered: `passcheck` (his own idea), `peel` (a layered-encoding decoder from his own picoCTF charset cheat sheet), `netcalc` (a subnet calculator from bitwise arithmetic).

**What `passcheck` is.** It inverts `cupp`. `cupp` takes a person's details and generates a wordlist to attack them with; `passcheck` takes the same details and **rejects** any candidate password that falls inside that set. ⚠️ **Verify** [NIST SP 800-63B §5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html) — screening candidates against "context-specific words... and derivatives thereof" is the actual requirement. *Derivatives* is the whole job: no complexity rule catches `R3x1998!`.

| Inc | What | Time | Hints | Commit |
|-----|------|------|-------|--------|
| 1 | `case_variants` + `year_variants` | 28 min | **none** | `68d6d17` |
| 2 | `leet_variants` via `itertools.product` | 47 min | Tier 1 | `f66c73e` |
| 3 | `joins` | — | *deferred past 4* | — |
| **4** | **`build_candidate_set` — compose all three** | 25 min | Tiers 2,3,4 | `ffa1709` |

**Measured payoff.** `build_candidate_set(["liverpool"], ["1998","2020"])` → **240 candidates**, and `L1v3rp00l1998` is one of them. Thirteen characters, mixed case, digits, passes every complexity rule in common use — caught by code he wrote in one evening. Adding `"emre"` takes it to 290.

**⭐ Solo wins worth naming.**
1. He carried **one-guard/one-return** from last session's refactor onto a brand-new file, unprompted.
2. He hit his own obstacle in `year_variants` — index arithmetic wouldn't pick the short form out of a 2-character year — and solved it with **negative slicing**, which is both the intent-stating form *and* the one that cannot raise `IndexError`.
3. He gave non-substitutable characters a **one-option list** instead of branching around them. That's why two frozen tests pass with **no code written for them** and the function contains no special case at all.
4. He applied **all three** outstanding 🟢 review notes unprompted — including going back into increment 1's code that increment 2 never touched, and rewriting his accumulate loop as a set comprehension.
5. He reached the **staged (non-nested)** decomposition of increment 4 himself. It's equivalent to the spec's nested wording, and he was told so before he wasted time doubting it.

**He won a spec argument.** His `year_variants` applied the short form unconditionally where the spec said 4-character years only. The frozen corpus couldn't detect it — the set swallows the duplicate — and **over-generating is the safe direction of error for a screener**: too large a derivation set costs one extra password attempt, too small lets a guessable password through. **The spec was amended to his implementation**, with his reasoning recorded in it. Since the tutor had said "pytest is your green light, not me", it was flagged as a *weak test* (tutor-written) rather than a weak implementation.

**Concepts that stuck:** sets dedupe, have no order, and `{}` is a dict · set equality is **membership, not order** — pytest's `Extra items in the right set` is a membership statement · `itertools.product` takes one iterable **per position**, and `*` unpacks a list of choice-lists into those positions · a uniform one-option list removes the need for a special case · `join` takes any iterable of strings, tuples included · `.add()` takes **one item**, `.update()`/`.union()`/`|` take an **iterable** · and the security principle above.

---

## The one method failure — which he diagnosed himself

> *"the part that confused me the most was the lack of teaching. You needed to teach me the update function or the union function. the code itself now i see it is easy i had it i was on the right track. i would have struggled with the final set but the others i essentialy had it."*

**He's right.** The increment 1 brief taught `set()`, `.add()` and `a | b` — and never the merge form. Increment 4's *central operation* was merging a set into an accumulator, so he built one out of `.add()` and a generator expression and put two generator **objects** into his set. **All three hint tiers tonight trace to that single gap.** His third signal — *"you havent explained the final step? we have a copy set and the additional set? i feel like this final function was a step up and im not getting it at all"* — was also correct.

**Seventh consecutive session of correct pushback on method.** Logged against the **existing** one-new-concept / pre-built-machinery rule. No new rule written, by design.

---

## 🎓 Head-of-Year Review #2 (2026-10-17, Fable) — **AMBER**

Ran first, before the greeting, three days late. Full text in `progress.json.head_of_year_review.log`.

**Its own three priorities, graded by itself:** re-warm by cold redo — **done**, honestly · make something public — **half** (Increment 10 landed and much more, but the repo still didn't exist after 3.5 months) · teacher accountability — **FAILED**.

**Amber again, and it named the repetition as the finding:** best attendance and the most code the programme has produced, and the colour didn't move, because nothing is public and project sessions kept ending badly.

**It confirmed one half of the dashboard's claim and rejected the other.** Method is the main risk to him **staying** — but *"retention is still the risk to you improving, and the cold redos show it live. Two risks. Don't let the teacher's self-criticism bury the one the programme exists for."*

**Its sharpest observation:** seven standing teaching rules across four project sessions, each written after a failure, none preventing the next. *"The rulebook is complete. Another rule is not the fix."* **Call: REFINE, then hold still** — test compliance, don't legislate. Followed tonight.

**Priorities for the fortnight to 2026-10-31:**
1. **Two project sessions he closes because he's done, not fed up.** ✅ **one delivered tonight**, one to go.
2. **Decide `sectools`-public in one sentence.** ✅ **answered** — see below.
3. **Retention lane on schedule, outside project time.** ⬜ deferred one session at his request.

---

## His portfolio decision (2026-10-17) — a debt becomes a decision

> *"i want it on github but the repo should be private, sectools is good for beginner, the stuff i display on my github i need to make sure its done properly, documented properly and without heavy AI reliance."*

**Open debt #1 is closed as a decision, not as outstanding work.** It is not avoidance — he's distinguishing a learning repo from a portfolio piece, which is the correct distinction, and it **raises the bar** on what this programme should be building toward.

**His recorded standard for anything public:** done properly, documented properly, **no heavy AI reliance** — i.e. something he can defend as substantially his own. That now governs what gets proposed as portfolio work.

Replacement task, lower stakes: a **private** repo + push, so 21 commits exist off-machine. OPSEC scrub and `SPEC.md` spellcheck still apply first.

---

## Active Build — `passcheck` (3 increments)

| # | Increment | Status |
|---|-----------|--------|
| 1 | `case_variants` + `year_variants` | ✅ 2026-10-17 |
| 2 | `leet_variants` — substitution combinatorics | ✅ 2026-10-17 |
| 3 | `joins` — concatenate pairs of facts | ⬜ deferred past 4 |
| **4** | **`build_candidate_set` — compose the generators** | ✅ **2026-10-17** |
| **5** | **`screen(password, candidates)` + which rule matched** | ⬜ **next — recommended** |
| 6 | argparse CLI | ⬜ |
| 7 | Scoring and the report | ⬜ direction only |

**Design principle, settled by his argument:** for a screener, **over-generation is the safe direction of error.**

---

## Previous Project — `loginwatch` (12/15 + 11a)

**Python work is complete.** Increments 11 and 12 are Bash, 14 is packaging, 15 is docs. **Do not offer any of it as "Python work."** Increment 11 (`run-daily.sh`) is still the **Bash L2 gate on Scenario missions**. 23 tests green, mypy strict clean, exit-code contract honest. Five minor flagged code items outstanding, none blocking.

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete 2026-05-11. Last active **2026-10-17**. *(progress.json said L1 until tonight — drift corrected.)* |
| Bash | **L2 (pending)** | L1 complete. Track challenges last active 2026-05-10; Linux work carried by Bandit + CTF to 2026-10-09. L2 arrives at `loginwatch` Increment 11. |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks on Python L2 + Bash L2. **Increment 11 is the gate.** |

---

## Active Weak Points

**None.** WP001 retired; WP002 & WP004 mastered; WP003 & WP005 paused with the Concepts track. Nothing logged this session.

**Watched quietly inside review — read the output you were given (WP002 family).** It surfaced once tonight and resolved immediately: he asked whether he needed to *sort* when pytest had said `Extra items in the right set: 'R3X'` — a membership statement, not an ordering one. Fixed off a single Tier 1. He had also printed the generator objects himself, which is what made the diagnosis quick.

**Still tracked in the CTF lane: identify before you act.** Untouched this session.

---

## picoCTF / CyLab — CTF Practice

- **Flags captured: 17.** Untouched this session.
- **Requeued:** 09-30 batch **~2026-10-21** · Piece by Piece **~2026-10-23** (graded on `file`-first alone) · 10-03 batch ~2026-10-24 · Printer Shares ~2026-11-05 · bandit12 ~2026-11-06 · Sudo Make Me a Sandwich needs one clean self-powered retest · **Endianness** he self-flagged.
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) · **Rules:** tool-lookups fine, **answer-lookups not**.

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit13** (`sshkey.private`, not started). Last touched **2026-10-09** — 8 days.
- **Diversion trigger passed 2026-10-16.** Deferred **one** session tonight because he asked for Python; **it re-triggers next session.**
- **Cold-redo outstanding:** bandit0→6 cold (overdue since ~2026-08-07).
- Notes: [external/bandit-notes.md](external/bandit-notes.md).

---

## Open Debts

1. ~~**Ship `sectools` public**~~ — **CLOSED 2026-10-17 as a decision.** Private repo instead; public work must meet his own bar.
2. **`loginwatch` write-up** — none since July. The exit-code contract, the 23-test suite and the false-all-clear bug with measured before/after numbers is still the strongest portfolio material to date. Raise as a separate errand, never as the session.
3. **Push `sectools` to a private GitHub repo** — 21 commits exist only on this laptop. OPSEC scrub + spellcheck first. ~10 minutes.
4. Vulnerable target VM (Metasploitable2/DVWA) — not needed until the end of the project arc.

---

## Checkpoints

- [x] Diagnostic *(2026-04-27)* · Bash L1 *(2026-05-10)* · Python L1 *(2026-05-11)* · Concepts L1 *(2026-05-18)*
- [x] First weak point mastered — WP002 *(2026-05-21)* · Second — WP004 *(2026-05-24)*
- [x] 10+ archived write-ups *(2026-05-18)* · First L2 challenge *(2026-07-18)* · First multi-file Python program *(2026-07-23)*
- [x] First machine-readable tool output *(2026-07-29)* · First real CLI *(2026-07-30)*
- [x] First Head-of-Year review *(2026-09-30)*
- [x] First automated test suite *(2026-10-07)* · First real bug found by his own tests *(2026-10-07)*
- [x] First cold redos executed and graded honestly *(2026-10-09)*
- [x] First custom exception type · First refactor under a green suite *(2026-10-11)*
- [x] First locked, in-repo acceptance criterion written before work started *(2026-10-11)*
- [x] **Second portfolio tool started — `passcheck`, his own idea, chosen from three** *(2026-10-17)*
- [x] **First combinatorial Python — `itertools.product` and a choice-list per position** *(2026-10-17)*
- [x] **First project session in four to end on a win — and first measured duration in six** *(2026-10-17)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] `sectools` backed up to a private GitHub repo
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11** · attempted-unfinished: 2
- **CTF flags captured: 17** · cold redos run: 2 (1 partial, 1 fail)
- `loginwatch`: **12 / 15 + 11a**, Python complete · **23 tests**
- **`passcheck`: increments 1, 2, 4 · 35 tests · 38 lines of his Python**
- `sectools` repo: **21 commits**, clean, **no remote yet**
- **Bandit levels cleared: 13**
- Total sessions: **31** · Total hours: **~31.3** *(26.3 → 31.3: session 30's 3h had never been added; session 31 is measured)*
- Weak points mastered: **2** · retired: 1
- **Cross-track connections: 20** — newest: picoCTF *Password Profiler* handed him `cupp` and **provided** the checker; `passcheck` is him writing that checker.
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**Weekly summary:** ~3h over 1 session in the 7 days to 10-17, under the 5–10h band — but five touches in the eighteen days before it. Frequency is holding; volume dipped over the last week.

**Durations are measurable again.** Session 31 was stated, locked and measured. The head of year's standing instruction: don't ask him mid-session — take the git record (commits and line counts per session) as the metric.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop. `pytest 9.1.1`, `mypy` in `sectools/.venv`.
- ⚠️ `pip3` reports a **pre-existing** apt conflict (`pipx 1.0.0` wants `argcomplete>=1.9.4`, Ubuntu shipped `1.8.1`). **Do not** `pip3 install --upgrade argcomplete` over the apt-owned package.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed**.
- `sectools` (`/home/emrebektas/sectools`) — `loginwatch` + `passcheck`, **58 tests between them**, clean tree, **no GitHub remote yet**.
- `ctf-work/` — CTF solution scratch, **gitignored**.
- Localhost (`127.0.0.1`) — legal Python socket test target.
