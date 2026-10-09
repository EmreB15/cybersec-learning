# OverTheWire Bandit — notes log

Self-directed Linux CLI gym. Play at https://overthewire.org/wargames/bandit/

**How to use this file:** whenever a level stumps you, jot a line here — date, the level, and what tripped you up (a command you didn't know, a concept that didn't click). Don't paste passwords. At session start the tutor reads this and pulls recurring gaps into a teaching touch or a challenge.

Format: `YYYY/MM/DD  banditN→N+1 — what stumped me / what I learned`

Rule: struggle first, read the level's hint page, try commands. Only look at a walkthrough as a last resort — copying the answer teaches nothing.

---

<!-- entries below -->

when you run a command if you get a lot of output and the majority is errors or permission denied. use 2>/dev/null to throw the errors into a black hole and get the answer from the minority of the output.

xargs is used before a command but it is used after a pipe. If you want a command to read the path names but not the literal path names. So read the strings as a file target (the input) of the command being piped into.

---

2026/10/09  bandit11→12 — **ROT13 with `tr`.** *(logged by the tutor at Emre's request)*

Picked `tr` himself after reading the man pages of six candidate commands — the selection was the hard part and it was solo.

**The misconception that cost the time: `tr` has no concept of "13".** It does not take a shift amount. It takes **two character sets and maps them positionally** — 1st char of SET1 → 1st char of SET2, 2nd → 2nd, and so on. So you express a rotation by writing out both alphabets and letting the position do the work.
- A wrap-around is **two touching ranges in one set**: `n-z` immediately followed by `a-m`. `n-m` is not a range — ranges run forward, low to high.
- **Uppercase is separate.** `a-z` and `A-Z` are different characters to `tr`, so both halves go in both sets — and **in the same order on each side**, or letters silently map to the wrong case with no error at all.
- `-d` is delete mode and takes only **one** set — hence `tr: extra operand`. Substitution takes no flag at all.
- Don't wrap sets in `[ ]`: `tr` doesn't want them, and bash expands `[a-z]` as a filename glob before `tr` ever sees it.

**Generalises to any ROT-N, not just 13.** Positional substitution + two touching ranges.

**Side lesson, self-corrected: `>` vs `|`.** `cat data.txt > tr -d 13` tried to create a *file literally called `tr`* (`>` expects a filename; home is read-only on Bandit → `Permission denied`). `|` sends output to a **command**. File versus process — spotted and fixed unaided.

---

2026/10/09  bandit12→13 — **the `file`-driven decompression loop. The hardest level so far, and the one that built the reflex.** *(logged by the tutor at Emre's request)*

**Step 1, and the real blocker: it's a HEXDUMP, not a compressed file.** `file data.txt` said **`ASCII text`** — and `bzip2`/`gzip` both refused it for exactly that reason. A hexdump is a *human-readable rendering* of bytes, not the bytes: `1f8b` on screen is **four ASCII characters** on disk, where the real file holds **two** bytes, `0x1f` and `0x8b`. You're holding a photograph of a file.
- **`hexdump` and `hd` only travel one way** (bytes → text). **`xxd -r` reverses it** — and `xxd`'s output format is exactly what the dump looked like. `xxd -r data.txt > data.bin`.

**Step 2 onward — the loop, ~9 layers deep:** `file <thing>` → read the format it names → run that tool → `file` the result → repeat. gzip → bzip2 → gzip → tar → … until a text file with the password falls out.

**MAGIC NUMBERS — the payoff, and it was visible in the raw dump the whole time.** The dump opened with `1f 8b 08`: **`1f 8b` is gzip's signature**, present at the start of every gzip file. Further in sat `BZh91AY&SY`, **bzip2's signature**. **This is literally how `file` works** — it reads the leading bytes and looks them up in a table of known signatures. The table was on screen in raw form.

**TWO TOOL MECHANICS THAT COST ATTEMPTS:**
- **`gzip` decides by FILENAME EXTENSION, not content** → `unknown suffix -- ignored` until the file was renamed to end `.gz` (`.gzip` was not accepted either). **This is why the level tells you to use `mv` — the rename is load-bearing, not housekeeping.**
- **`tar` ignores the extension entirely but requires `-f <file>`** to name the archive; without it tar reads stdin, i.e. the terminal → `Refusing to read archive contents from terminal`. `tar -xf <file>`.
- **So: `file` tells you the *real* format from the bytes; the extension only tells `gzip` whether it's willing to try. Two different things, and only one of them is honest.**

**Defender's note:** extension-based trust is a live attack surface — `invoice.pdf.exe`, or a web upload filter that accepts `.jpg` and never reads the bytes. **Content inspection (magic numbers) is the control; extensions are attacker-supplied input.** Same instinct as the `split` fragments in Piece by Piece the same session: identify the artefact from what it *is*, not from what it's labelled.

**Cold-redo (~2026-11-06):** given a hexdump, is `xxd -r` the first move, and is `file` run between **every** decompression step rather than guessing the next tool?
