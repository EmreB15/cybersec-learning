# OverTheWire Bandit — notes log

Self-directed Linux CLI gym. Play at https://overthewire.org/wargames/bandit/

**How to use this file:** whenever a level stumps you, jot a line here — date, the level, and what tripped you up (a command you didn't know, a concept that didn't click). Don't paste passwords. At session start the tutor reads this and pulls recurring gaps into a teaching touch or a challenge.

Format: `YYYY/MM/DD  banditN→N+1 — what stumped me / what I learned`

Rule: struggle first, read the level's hint page, try commands. Only look at a walkthrough as a last resort — copying the answer teaches nothing.

---

<!-- entries below -->

when you run a command if you get a lot of output and the majority is errors or permission denied. use 2>/dev/null to throw the errors into a black hole and get the answer from the minority of the output.

xargs is used before a command but it is used after a pipe. If you want a command to read the path names but not the literal path names. So read the strings as a file target (the input) of the command being piped into.
