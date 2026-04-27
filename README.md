# Cybersecurity Learning Portfolio

Hands-on practical work alongside my OU BSc Cyber Security degree (R60).

This repo contains the practical track — Python tooling, Bash scripting, security concept reasoning, and scenario missions — that complements the theory side of the degree. Sessions are structured by a Claude Code-based tutor (see [CLAUDE.md](CLAUDE.md)) with deliberate spaced retests and weak-point tracking.

## What's here

- **`python-track/`** — Python challenges, security-oriented from L1 onward
- **`bash-track/`** — Bash scripting from terminal survival to security automation
- **`concepts-track/`** — Written reasoning exercises on attack and defence
- **`scenarios/`** — Multi-track scenario missions (unlocked once all tracks reach L2)
- **`writeups/`** — One write-up per completed challenge, with reflections

## Status

See **[dashboard.md](dashboard.md)** for live progress: current levels, active weak points, scheduled retests, and what's next.

## Why this exists

The OU degree handles theory and assessment. This is where the practical work lives — built up over months and years, deliberately documented, every challenge owned and explained.

The system is designed around one specific learning challenge I have: I learn things but don't repeat them enough, so I forget. The tutor enforces structured retests on a real spaced-repetition schedule.

## Stack

WSL2 + Ubuntu 24.04, Python 3, Bash, git, gh. Lab work uses VirtualBox + Metasploitable2 / DVWA (set up when first network-touching challenge is reached). Pre-commit hook with [gitleaks](https://github.com/gitleaks/gitleaks) blocks accidental secret commits.

---

*All practical work is conducted on systems I own or have explicit written permission to test, in compliance with the UK Computer Misuse Act 1990.*
