# Three Loose Bricks

**Track:** Concepts | **Level:** L1 | **Date Completed:** 2026-05-18 | **Hints Used:** 0 (Tier 0 — solo on first submission and on revision) | **Time Spent:** ~30m

## What This Was

Third and final Concepts L1 challenge. Designed to close Concepts L1 with a reasoning pattern that did not overlap the prior two (phishing analysis in #1, OSINT/threat-intel triage in #2). The pattern selected: **attack-surface analysis** — given a small organisation's network description, rank the three biggest weaknesses with reasoning, naming the CIA property most threatened and the justification for the ranking.

Scenario: ACME Marketing, a 12-person agency, single office, one flat /24 network. Five items described in the brief:

1. Reception desktop — shared local user `Reception` / `Reception2023`, always logged in
2. File server (Windows Server 2016) — SMB share writable by everyone in Domain Users; holds NDAs and campaign decks
3. Wi-Fi — single SSID, WPA2-PSK shared with staff and guests, passphrase printed on a card
4. CCTV recorder — web UI on flat network, default `admin/admin`
5. Bookkeeper laptop — pushes QuickBooks backups over plain FTP to LAN NAS; goes home each night

Brief explicitly invited `verify: X` for unknown items rather than substituting confidence (same WP003 family discipline applied to the user's own knowledge state). Three source citations provided (NIST SP 800-12 Rev 1 §2.1 for CIA; NIST SP 800-41 Rev 1 for segmentation; CIS Controls v8 Control 4 for default-credentials / asset hygiene).

## What I Built

I analysed ACME's network and after finding some vulnerabilities I ranked the top 3 based around the CIA triad. I analysed each vulnerability and decided how bad it could be for the business. I tried to think like the attacker and what they would want to do and where they would want to get.

## Key Concepts Used

- **CIA triad applied to ranking, not classification.** The skill at L1 is not "what is integrity" — it's picking which property is _most_ threatened by a given weakness when multiple are at risk simultaneously. CIA primary is a judgement call you justify, not a label you assign.
- **Attack-surface triage by effort-to-impact ratio.** The right top-3 picks aren't the assets that matter most (file server with NDAs) — they're the weaknesses where attacker effort is lowest relative to what they gain. Default credentials on a flat-network IoT device beat over-broad share permissions on the file server, because the default-creds attacker doesn't need to be inside first; the file-server attacker does.
- **The IoT / default-credential blind spot.** Real breaches start at the unloved, lower-priority-looking device with shipped defaults that nobody changed (CCTV recorder, network printer, BMS controller). Triaging only the obviously-important assets and skipping the small ones is the most common attack-surface miss at junior level. _Item 4 of the brief stated `admin/admin` verbatim; the miss was triage, not knowledge._
- **Pivot-and-foothold thinking.** Attack-surface analysis is not "rank weaknesses in isolation" — it is "rank by what an attacker actually gains, including reach to other hosts." Reasoning about a CCTV recorder as _a sensor that gathers human-intelligence (screens, faces, swipe cards) and a Linux box that can host attacker tooling_ is the same pattern as the Reception → file server chain in the original submission. The pattern is recognising attack chains, not isolated weaknesses.
- **Network segmentation as the meta-multiplier.** A flat /24 with no VLAN separation is what turns each individual weakness into a chained one — guest on Wi-Fi can hit the CCTV; CCTV pivot can hit the file server. The segmentation principle (NIST SP 800-41 Rev 1) is the underlying concept that makes the _combination_ of weaknesses dangerous rather than the individual ones.
- **Default credentials as a distinct failure class.** "Easy to guess" suggests an attacker is guessing; "default" means the manufacturer documented the credentials and the operator never changed them — no guess needed. CIS Controls v8 Control 4 (Secure Configuration of Enterprise Assets and Software) names this as a top-tier hygiene control specifically because the failure mode is _trivial_ to exploit and _trivial_ to fix.
- **Brief-precision applies to the tutor as much as the user.** The original review marked the file server CIA primary as Confidentiality (because in real Windows/SMB, "Modify" includes Read by default). The brief only stated "writable by everyone in Domain Users." The user reasoned correctly from the stated brief and pushed back. The point was withdrawn. Captured as tutor process note 15 — if an evaluation depends on a property X, X must be stated in the brief, not inferred from domain knowledge the user doesn't yet have.

**Sources cited (Concept-Track integrity rule):**

- CIA triad — NIST SP 800-12 Rev 1, §2.1 — https://csrc.nist.gov/pubs/sp/800/12/r1/final
- Network segmentation — NIST SP 800-41 Rev 1 — https://csrc.nist.gov/pubs/sp/800/41/r1/final
- Default credentials / asset configuration hygiene — CIS Controls v8, Control 4 — https://www.cisecurity.org/controls/v8
- Windows Server 2016 lifecycle (⚠️ Verify reference) — https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2016

## What I Got Wrong First

At first I decided that the receptionist desktop was the second biggest problem because it would be possible for any of the staff to log on and carry out attacks, but the bigger problem is the CCTV recorder being on the flat network using default credentials. What I didn't realise is that CCTV recorders have Linux on their system which attackers can use to host tools and attack the network, but they can also use the physical aspect to look for easy-to-manipulate staff or security leaks that can be exploited.

## Weak Points Flagged

**None logged.** The CCTV miss on the first pass was a single instance — flagged in review with a teaching moment, not promoted to a weak point. Revision integrated the feedback (CCTV slotted in at #2, Reception swapped out) and added a physical-surveillance angle the tutor had not named. The verify-or-skip trap built into the brief did not fire cleanly because the items requiring verification (cleartext FTP, Windows Server 2016 patch state) did not make the user's top 3 — discipline was not tested in this challenge.

**Tutor process note 15 captured** (separate from any user weak point): _brief precision applies to the tutor as much as the user — if an evaluation depends on a property X, X must be stated in the brief, not inferred from domain knowledge the user doesn't yet have._ Sibling to process note 10 (count concrete deliverables explicitly) and process note 13 (verify-or-skip trap design for retests).

## What I Would Do Differently

I would think about IoT devices as being very important and being a common way for threat-actors to gain access. I need to think about the credentials — are they default, or are they easy to guess? I also need to think about devices being on the flat network: if the network is not segmented, it would be very easy for attackers to get in and attack.

## Final Solution

1. The most dangerous vulnerability here is the Wi-fi being used by ACME Marketing, staff and guests sharing the same network and guests knowing the password is a real security threat. Confidentiality is at risk here because if a guest gets on to the network they can easily listen to network transmissions and even carry out MITM attacks. The reason why I think this is the most dangerous is because the WPA-PSK passphrase is almost like the key to a house, once they are on the network they can figure out its design and they can know who and what to target, the fact that it is printed on a card makes this the biggest vulnerability.

2. The CCTV recorder is the second biggest vulnerability here, it sits on the flat network with very easy credentials to guess. These cameras probably have some form of Linux on them so that can host attacking tools which can then be used silently on the network and nobody would figure it out until it's too late. In the CIA triad this is a real risk of confidentiality as CCTV cameras can spy on people in person and also since it's on the same network it can spy on network transmissions. The hacker would be able to see the computer logically and physically and map out the employees and could then use social engineering tools to find more discrete ways of entering.

3. The file server is the third biggest vulnerability here, everyone can write to it making it a key source of concern, why should every staff member have access to important documents? Integrity is at risk here because if multiple people are writing at once there might not be a truth, also if anyone can edit it this leaves the company at real risk since it's on the domain users group and everyone can get access to the network. It is in my top 3 because of how important the files are, since these are considered secret documents the fact that everyone can write to it is very concerning.
