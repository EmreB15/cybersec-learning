# Cybersecurity Training Dashboard
*Last updated: 2026-10-19 — Session 32. **Bandit 13→16, increment 5a green at 49 — and he finished the session by specifying how briefs should be sized.***

---

## Pickup Here

> ### ⭐ NOTHING WAS COMMITTED. Commit first, then increment 5b — one line.
> `/home/emrebektas/sectools` holds uncommitted changes to `derive.py`, [PASSCHECK-SPEC.md](../sectools/PASSCHECK-SPEC.md) and `tests/test_derive.py`, plus an untracked `tests/test_screen.py`. **49 green** in `test_derive.py`; 8 frozen and red in `test_screen.py` awaiting `screen.py`.

**Increment 5a is closed.** The red finding was fixed — **tutor-applied, at his explicit request**, so it isn't credited to him. His 47 were his: the tree walk, both stage comparisons, `sorted()` in both places, `parts + ["year"]` over `.append`. The fix deleted 8 lines and added none, and the tutor's *first* recommendation for it was wrong and would have broken two frozen tests.

**→ 5b: `screen.py`**, importing nothing from `derive`. `screen(password, candidates) -> tuple[str, str] | None`. Exact match, no normalising. **It should come out one line** — he's been told that if it's longer, 5a built the wrong structure. 8 frozen tests exist. Pass condition: `pytest` → **57 passed**.

> **5b is also a probe.** The conditional expression `A if cond else B` was tutor-applied, not written by him. If 5b needs it and he reaches for it unaided, it landed. **Don't prompt him toward it.**

**→ Increment 6, already split** — see the correction below.

| | What he builds | Runnable? |
|---|---|---|
| **6a** | argparse skeleton — repeatable `--word` / `--year`, prints what it parsed | yes |
| **6b** | wire in `build_candidate_map` + `screen` on `--password`, print REJECTED / ACCEPTED | yes |
| **6c** | the explanation line — *"rejected: derived from 'liverpool' by case+leet+year"* | the finished tool |

---

> ### 📌 TWO METHOD CHANGES — BOTH RAISED BY HIM, BOTH NOW STANDING
>
> **1. Grow the shape one level at a time** *(his, 2026-10-19)*
>
> > *"Honestly a better approach here would have been starting off with just case then adding the leet and then the year. So i would understand it better."*
>
> He's right. Split his way, **each sub-step adds exactly one loop and one comparison** — and at two levels deep it's nearly impossible to miss that the source word lives in the enclosing loop and can't be recovered from a finished candidate. The insight would have arrived free, at a depth where it's obvious, then scaled twice. Instead the whole four-level shape arrived at once and the insight had nowhere to come from.
>
> **The programme already had this pattern and the tutor broke it.** Increments 1, 2 and 4 were one generator at a time, each green before the next. It was abandoned exactly where the difficulty stopped being *a new function* and became *a new shape*. It's also better on the metric that counts: more typing, three green lights, three commits.
>
> **2. Draw the shape of the data at brief time** *(his, 2026-10-18)*
>
> > *"your explaination for tier 2 is useless because im struggling to see the bigger picture"*
>
> Tier 2 named a technique to someone who couldn't see the data's shape. What moved him in one step was Tier 3 **drawing the derivation as a tree**. Prose describing a tree is not a tree. This is **"show the path"** applied to data flow rather than file layout.
>
> **Neither becomes an eighth teaching rule.** Both are the existing one-new-concept rule being broken. The head of year's standing call stands: test compliance, don't legislate.

**Repeat verbatim:** offer two or three builds and let him pick · lock the spec section and frozen tests in the repo **before** he starts, pass condition as a number · verify tutor-written tests against a reference implementation that **imports his functions**, so expected values are computed, not guessed · pytest is the green light, not the tutor · one commit per increment.

**New:** ⏱ **warn him at the halfway mark of any timed chunk.** The Bandit chunk ran 50 minutes against a 25-minute budget with no check-in, and that is what cost increment 5b.

**Not to be volunteered as "Python work":** the `loginwatch` write-up (debt #2 — a separate errand) · `loginwatch` Increments 11/12 when he wants **Bash** · packaging or docs for either project.

---

## Session 32 (2026-10-18) — Bandit 13→16, then `passcheck` increment 5a

**108 minutes, measured** — 22:29 to 00:17. A stated 90 plus a 20-minute extension he asked for at 23:56, three minutes from lock, when he was stuck and wanted to finish. Second consecutive measured session.

| Chunk | Budget | Actual | Outcome |
|---|---|---|---|
| Bandit 13→16 | 25 min | **50 min** | 3 levels, commands looked up |
| `passcheck` 5a | 60 min | ~35 min | **47 passed**, 1 red outstanding |
| Increment 5b | — | — | **cut for time** |

### Bandit 13→16 — fast, and honestly graded

Three levels in ~50 minutes. **He disclosed unprompted** that he used AI chatbots for the commands and then self-served the flags with `--help`.

The `--help` half is the part that transfers and was named as such. But on *these* levels the command **is** the answer — `ssh -i`, then talking to a port, then talking to a port wrapped in TLS, with no parsing or decoding underneath — so "which tool do I need" was an **answer-lookup**, not the permitted tool-lookup. Passwords banked; recall unproven.

**→ Cold redo queued 2026-11-01, graded on tool recall alone,** not flag capture: does a plain TCP client arrive unaided, and when the level says the port speaks SSL is a TLS client reached for *deliberately* rather than retrying the plain one? Full entry in [external/bandit-notes.md](external/bandit-notes.md).

### A real design finding came out of the tutor's prep

Provenance built by iterating generator **sets** is non-deterministic *across processes*. A candidate reachable by two routes — `"4"` from `"a"` via leet and from `"A"` via case+leet — takes whichever route is visited last, and string hashing is randomised per process. **Measured across 15 `PYTHONHASHSEED` values: 2 of 6 candidates flipped.** Wrapping the two inner set iterations in `sorted()` removed it on all 15.

That became a frozen spec requirement with the reason recorded: **a security tool that gives two different explanations for the same password on two runs is defective, not quirky.**

### Increment 5a — the ladder, and why it was climbed

Tiers **1, 2, 3 and 4** in ~35 minutes. His first architecture built one set per rule-combination and classified candidates by membership over the finished `build_candidate_set` output. Real thinking — it even resolved the double-route ambiguity deterministically through `elif` order, with no `sorted()` needed — but **structurally unable to report the source word**, because by the time it iterated the finished set the origin had been discarded. pytest said it in one line: `assert ('4','leet') == ('a','leet')`, index 0.

He diagnosed the rewrite himself — *"i have the feeling i need to rewrite all the code"* — and was told plainly he was right, and that the scope was **one function body**, ~20 lines deleted and ~15 written, not the project.

**⭐ Solo wins worth naming.**
1. Once he had the shape, he wrote the tree walk **correctly on the first attempt**: source word carried from the root, each stage compared to its **immediate parent** rather than the root, `sorted()` in both places.
2. `parts + ["year"]` rather than `.append` — the list-aliasing trap, dodged deliberately after one warning. Appending would have left `"year"` stuck in `parts` for every later candidate and the bug would have looked random.
3. He diagnosed his own architecture as unfixable **before** being told.
4. He flagged his finished solution as *"kind of silly"* **before review** — correct, and a first.

**Concepts that stuck:** a dict is built by assignment, and re-assigning a key **overwrites** with no error · `sorted()` on a set gives an ordered **list**, and that is what makes dict-write order reproducible · set iteration order is not in Python's contract and string hashing is randomised **per process** · `.get()` returns `None` where `[]` raises `KeyError` · `"+".join([])` is `""`, not nothing · provenance has to be recorded **while you still hold the root**.

---

## Active Build — `passcheck`

| # | Increment | Status |
|---|-----------|--------|
| 1 | `case_variants` + `year_variants` | ✅ 2026-10-17 · `68d6d17` |
| 2 | `leet_variants` — substitution combinatorics | ✅ 2026-10-17 · `f66c73e` |
| 3 | `joins` — concatenate pairs of facts | ⬜ deferred past 4 |
| 4 | `build_candidate_set` — compose the generators | ✅ 2026-10-17 · `ffa1709` |
| **5a** | **`build_candidate_map` — set + provenance** | ✅ **49 green 2026-10-19 · UNCOMMITTED** |
| **5b** | **`screen(password, candidates)` — the verdict** | ⬜ **next — one line** |
| 6 | argparse CLI | ⬜ **then this** |
| 7 | Scoring and the report | ⬜ direction only |

**Frozen corpora must include adversarial inputs.** The original twelve had no mixed-case input word, and that single gap let a candidate-inventing bug pass the entire suite. Two cases and a superset guard were added as a dated amendment.

**Design principles, both settled by argument rather than decree:** for a screener, **over-generation is the safe direction of error** (his, 2026-10-17) · **a reproducible explanation is part of correctness**, hence `sorted()` (tutor, 2026-10-18, measured).

**Why provenance exists at all:** "rejected" with no reason reads as an arbitrary rule and gets worked around — the user tries `L1v3rp00l1999` and gets in. ⚠️ **Verify** [NIST SP 800-63B §5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html).

---

## Previous Project — `loginwatch` (12/15 + 11a)

**Python work is complete.** Increments 11 and 12 are Bash, 14 is packaging, 15 is docs. **Do not offer any of it as "Python work."** Increment 11 (`run-daily.sh`) is still the **Bash L2 gate on Scenario missions**. 23 tests green, mypy strict clean, exit-code contract honest.

---

## Track Progress

| Track | Level | Status |
|-------|-------|--------|
| Python | **L2 (in progress)** | L1 complete 2026-05-11. Last active **2026-10-18**. |
| Bash | **L2 (pending)** | L1 complete. Track challenges last active 2026-05-10 — **flagged, 161 days**; Linux fluency carried by Bandit + CTF. L2 arrives at `loginwatch` Increment 11. |
| Concepts | **ARCHIVED** | 3/3 done, archived 2026-07-16, reinstatable. |
| Scenarios | Locked | Unlocks on Python L2 + Bash L2. **Increment 11 is the gate.** |

---

## Active Weak Points

**None logged.** WP001 retired; WP002 & WP004 mastered; WP003 & WP005 paused with the Concepts track.

**Watched quietly inside review — read the output you were given (WP002 family).** Surfaced twice this session and resolved both times off a single Tier 1 pointing at the diff rather than the fix: `('4','leet')` vs `('a','leet')` named the source-word bug, and `'' != 'exact'` named all six remaining failures at once. He is now reliably *given* the diff rather than the answer, and reliably reads it.

**Still tracked in the CTF lane: identify before you act.** Untouched.

---

## Linux Gym — OverTheWire Bandit

- **Status: bandit16** (port scan 31000–32000, not started). Last touched **2026-10-18**. Diversion satisfied — next trigger ~2026-10-25.
- **Cold redos outstanding:** bandit13→16 **~2026-11-01, graded on tool recall alone** (new) · bandit12 ~2026-11-06 · bandit0→6 cold, **overdue since ~2026-08-07**.
- Notes: [external/bandit-notes.md](external/bandit-notes.md). Scratch lives in `overthewire/` — **gitignored, correctly.**

---

## picoCTF / CyLab — CTF Practice

- **Flags captured: 17.** Untouched this session.
- **Requeued:** 09-30 batch **~2026-10-21** · Piece by Piece **~2026-10-23** (graded on `file`-first alone) · 10-03 batch ~2026-10-24 · Printer Shares ~2026-11-05 · Sudo Make Me a Sandwich needs one clean self-powered retest · **Endianness** he self-flagged.
- **Log:** [external/cylab-notes.md](external/cylab-notes.md) · **Rules:** tool-lookups fine, **answer-lookups not** — and this session showed the line is thinner than it looks.

---

## Open Debts

1. ~~**Ship `sectools` public**~~ — **CLOSED 2026-10-17 as a decision.** Private repo instead; public work must meet his own bar: *done properly, documented properly, no heavy AI reliance.*
2. **`loginwatch` write-up** — none since July. The exit-code contract, the 23-test suite and the false-all-clear bug with measured before/after numbers is still the strongest portfolio material to date. Raise as a separate errand, never as the session.
3. **Push `sectools` to a private GitHub repo** — 21 commits exist only on this laptop, and **session 32 added none**. OPSEC scrub + spellcheck first. ~10 minutes.
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
- [x] Second portfolio tool started — `passcheck`, his own idea, chosen from three *(2026-10-17)*
- [x] First combinatorial Python — `itertools.product` *(2026-10-17)*
- [x] **First dict-building code — provenance carried through a three-deep walk** *(2026-10-18)*
- [x] **First time he pre-empted a red finding on his own code** *(2026-10-18)*
- [x] **First time he rejected a hint tier as the wrong rung — and was right** *(2026-10-18)*
- [x] **First time he specified the method himself — increment sizing, and it was adopted** *(2026-10-19)*
- [ ] Lab environment fully set up — vulnerable target VM installed
- [ ] `sectools` backed up to a private GitHub repo
- [ ] Scenarios unlocked — Python L2 + Bash L2 both complete
- [ ] All active tracks reach Level 3

---

## Portfolio Stats

- Write-ups generated / archived: **11 / 11**
- Track challenges completed: **11** · attempted-unfinished: 2
- **CTF flags captured: 17** · cold redos run: 2 (1 partial, 1 fail) · **queued: 4**
- `loginwatch`: **12 / 15 + 11a**, Python complete · **23 tests**
- **`passcheck`: increments 1, 2, 4, 5a · 49 green of 57 frozen · 5 functions, all his**
- `sectools` repo: **21 commits** — unchanged, **session 32 committed nothing**, still no remote
- **Bandit levels cleared: 16**
- Total sessions: **32** · Total hours: **~33.1** *(31.3 + 1.8 measured)*
- Weak points mastered: **2** · retired: 1
- **Cross-track connections: 20**
- Active tracks: **Python, Bash**

---

## Weekly Rhythm

**Weekly summary:** ~4.8h over 2 sessions in the 7 days to 10-18 — still under the 5–10h band, but two sessions on consecutive days is the best back-to-back frequency since July.

**Durations are measurable again** — two consecutive measured sessions. Standing head-of-year instruction: don't ask mid-session, take the git record as the metric. **Session 32 breaks that metric**, because nothing was committed.

**🎓 Head-of-year priorities to 2026-10-31** *(review #2, AMBER)*:
1. **Two project sessions he closes because he's done, not fed up.** ✅ one (s31) · **s32 is a half** — he chose to extend and finished what he started, but it ended on an uncommitted red finding.
2. **Decide `sectools`-public in one sentence.** ✅ answered 2026-10-17.
3. **Retention lane on schedule, outside project time.** ✅ **delivered 2026-10-18** — Bandit 13→16, with an honest cold redo queued off the back of it.

---

## Lab Status

- Host attacker box — native Pop!_OS laptop. `pytest 9.1.1`, `mypy` in `sectools/.venv`.
- ⚠️ `pip3` reports a **pre-existing** apt conflict (`pipx 1.0.0` wants `argcomplete>=1.9.4`, Ubuntu shipped `1.8.1`). **Do not** `pip3 install --upgrade argcomplete` over the apt-owned package.
- Vulnerable target VM (Metasploitable2 / DVWA) — **not installed**.
- `sectools` (`/home/emrebektas/sectools`) — `loginwatch` + `passcheck`, **72 tests between them (23 + 49)**, **dirty tree**, no GitHub remote.
- `ctf-work/` — CTF solution scratch, **gitignored**. `overthewire/` — Bandit scratch with live level passwords, **gitignored**.
- Localhost (`127.0.0.1`) — legal Python socket test target.
