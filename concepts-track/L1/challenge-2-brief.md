# First Light Triage

**Track:** Concepts — L1 (#2)
**Time estimate:** 25–30 minutes (≈5 min read, ≈15 min reason, ≈10 min review)
**Format:** scenario-based reasoning (Concepts L1 standard — no multiple choice)

---

## Context

You are the morning shift on a small SOC. The overnight on-call left a triage ticket with three loose pieces of evidence and no narrative — they were called away mid-write-up. Your job: triage. For each piece of evidence, decide which OSINT / threat-intel source you would query first, what specific question you are putting to it, and what answer would change your next action.

This is what threat-intel sources are *for* — turning loose, unannotated indicators into decisions. Your TryHackMe pass-through showed you what each source is (shodan, censys, virustotal, exploit database — flagged 2026-05-11 as "not too sure why they are important"). This challenge tests whether you can reach for the right one under realistic ambiguity.

## Objective

Produce a short triage report covering all three pieces of evidence. For each piece, three lines:

1. **Source:** which OSINT/threat-intel tool you would query first. Name a close alternative if relevant.
2. **Question:** the specific thing you are asking that tool. Not "look it up" — the actual investigative question.
3. **Decision:** what result (positive OR negative) would change your next action, and to what.

## The evidence

**Evidence A.** An external IP, `198.51.100.47`, was seen making 14 connection attempts to your customer-facing web app's login endpoint over a 90-second window last night. The IP is not on any internal allow-list and you do not recognise it.

**Evidence B.** A file hash, `SHA256: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`, extracted from an email attachment that your mail filter quarantined automatically. The filter flagged it as "suspicious — unknown" rather than as a known-bad match.

**Evidence C.** The overnight ticket includes the line "possibly relevant: CVE-2024-XXXXX" (placeholder — treat as a real CVE ID) next to the name of the framework your web app is built on. The on-call did not say whether your deployed version is affected.

## Constraints

- **No web lookups during the challenge.** Reason from what you remember after your THM exposure. This tests transfer, not browsing.
- **Plain English, not bullet-spam.** Short paragraph or 3–4 lines per evidence piece covering source / question / decision.
- **If you don't know, say so.** "I don't know which tool fits this and would look it up" is a valid answer. Substituting confidence for ignorance is the WP003 family fingerprint, and verify-don't-proxy (WP002 family) applies here too — if the answer requires verification you can't do from your seat, name the verification step.
- **One tool can be re-used across multiple evidence pieces** if your reasoning genuinely says so. Don't artificially spread one-tool-per-piece.

## Hints available

6 tiers, standard escalation. Ask for a nudge if stuck.

## Expected output

A triage report — 3 evidence pieces × (source / question / decision). Length ~150–250 words total. I will mark up correct / missing / wrong, explicitly state where I am uncertain (Concept Track integrity rule), and flag any weak point that surfaces.

---

## Sources I will evaluate against

So you can verify my evaluation:

- **Shodan basics:** https://help.shodan.io/the-basics/what-is-shodan
- **Censys overview:** https://about.censys.io/
- **VirusTotal — how it works:** https://docs.virustotal.com/docs/how-it-works
- **Exploit Database — about:** https://www.exploit-db.com/about-exploit-db
- **NIST SP 800-61r2 (Incident Handling Guide) §3.2.3** — Information Sources during incident analysis. Supports the broader "use OSINT during triage" framing.

If any of my marks-up don't match what these sources say, push back.
