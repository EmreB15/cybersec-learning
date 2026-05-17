# First Light Triage

**Track:** Concepts | **Level:** L1 | **Date Completed:** 2026-05-18 | **Hints Used:** 0 in-challenge (pre-challenge tutored intro on the 4 OSINT sources after the original "no web lookups" constraint proved unworkable) | **Time Spent:** ~30m

## What This Was

Second Concepts L1 challenge. Designed to close the THM unresolved entry from 2026-05-11 ("learnt what shodan and censys is but not used them, not too sure why they are important. Found out about virustotal... Also learned about exploit database"). Tested whether the user could **match an evidence type to the right OSINT / threat-intel source** under a small triage scenario.

The brief presented three loose pieces of evidence left by an overnight SOC analyst: (A) an external IP making repeated connection attempts to a login endpoint, (B) a file hash from a quarantined email attachment flagged "suspicious — unknown," (C) a CVE ID mentioned alongside the name of the web app's framework, with no indication of whether the deployed version was affected. For each, the user had to name a tool, the investigative question, and what answer would change the next action.

The session opened with a design correction: the original "no web lookups" constraint assumed the user's THM exposure had filled the prerequisite. The user opened by stating they didn't remember what each source did — that honesty caught a tutor design defect (challenge built on assumed retention that hadn't happened). The session pivoted to **teach first, then apply** — a ~5 minute tutored intro on the four sources (Shodan, Censys, VirusTotal, Exploit-DB) with citation links, followed by the 3-evidence triage with the intro available as reference.

Evidence A and B passed first attempt. Evidence C surfaced a verify-before-act gap (logged as WP005) and required one revision.

## What I Built

What I built here was the initial use of threat-intel sources to identify threats and decide whether they are of concern or not and if so to what degree. We built a 3 question system to quickly check through each piece of evidence.

## Key Concepts Used

- **The four OSINT / threat-intel sources, by question they answer:**
  - **Shodan** — what services / banners are exposed on a public IP. Pivoted by IP, port, service, geography, organisation.
  - **Censys** — close alternative to Shodan; stronger on certificate transparency (pivot off cert fingerprints, subjects, issuers).
  - **VirusTotal** — multi-engine reputation lookup for files / hashes / URLs / IPs / domains, plus passive context (related samples, network behaviour, community comments).
  - **Exploit Database** — archive of public PoC exploits indexed by CVE; tells you whether weaponised public code exists for a given vulnerability.
- **NVD / MITRE CVE database** as sister tool — tells you _what a CVE describes_ (affected version range, CVSS, attack vector). Different question from "is there working code for it." For vulnerability triage you typically hit NVD first (am I vulnerable?), then exploit-db (how urgent?).
- **Verify-before-act in vulnerability triage.** When a CVE is mentioned alongside a framework name with no indication of affected version, the first step is _check whether your deployed version is in the affected range_, not _act on the assumption you're affected_. Same fingerprint as the verification-step skip already flagged in WP002 (bash) and WP003 (phishing) — now logged in a third domain as WP005.
- **Shodan returns data, not verdicts.** Shodan tells you which services are running and what banners they return. Whether that's "malicious" is your interpretation. Different banner profiles (commodity scanner, residential ISP, reputable cloud range, no services exposed) shift the response.
- **VirusTotal upload disclosure.** File hash _lookups_ are private and safe. File _uploads_ become visible to other VirusTotal subscribers; in a targeted-attack context this can leak the fact you were targeted, or expose sensitive content embedded in the sample. Uploading an unknown sample is an operational decision, not a default action.
- **Vulnerability response ladder.** Once you've confirmed vulnerable: (1) patch to fixed version, (2) apply vendor mitigation (config change / feature disable from the vendor's advisory), (3) compensating control (defensive layer _you_ add — WAF rule, network segmentation, disable affected endpoint), (4) emergency shutdown — last resort. Jumping to (4) without trying (1)–(3) causes unnecessary downtime.

**Sources cited (Concept-Track integrity rule):**

- Shodan basics — https://help.shodan.io/the-basics/what-is-shodan
- Censys overview — https://about.censys.io/
- VirusTotal — https://docs.virustotal.com/docs/how-it-works
- Exploit Database — https://www.exploit-db.com/about-exploit-db
- NVD (National Vulnerability Database) — https://nvd.nist.gov/
- NIST SP 800-61r2, _Computer Security Incident Handling Guide_, §3.2.3 (Information Sources) and §3.3 (Containment, Eradication, Recovery).

## What I Got Wrong First

For Evidence C I got the intel source wrong, and I also didn't discuss whether the framework version that the app is using is actually at risk or is it not.

## Weak Points Flagged

- **WP005 (new).** Vulnerability triage skips the version-check step before deciding response. Pattern: framework name appears alongside CVE ID → assumes affected → jumps to action, without naming the NVD / vendor-advisory lookup that establishes whether the deployed version is actually in the affected range. Same family as **WP002** (bash frequency-count — skip the verification step) and **WP003** (phishing — substitute confidence for ignorance). Stage 0, failures 0, retest **2026-05-22**.
- **Cross-track pattern note (carried forward).** WP002 (bash), WP003 (concepts/phishing), WP005 (concepts/vuln-triage) are now three concrete instances of the same underlying habit — _skip the named verification step_ — in three different domains. The underlying habit is the load-bearing weakness, not the domain surface.
- **Honesty discipline (positive signal — not a weak point, worth recording).** Three separate moments in the session, the user named a knowledge gap directly instead of substituting confidence: (i) at session start, "I don't remember at all what each threat-intel source does" (which caught a tutor design defect); (ii) during the answer ("just to be clear... I don't understand what vendor mitigation and compensate control are, I only included them since you mentioned them"); (iii) in the framing around revision-C, asking what the unfamiliar terms meant rather than guessing. This is exactly the discipline WP003 was logged to address, now applied unprompted to the user's own knowledge state.

## What I Would Do Differently

Next time make sure to answer the question properly and make sure that the intel-source is the correct one.

## Final Output

**Evidence A.**
I would use Shodan here to query the IP address, if Shodan can not find it I would look at Censys as an alternative. We would search the IP address but what we are looking for is a device or a service with that public IP, we want to see what is exposed. If on search we found the IP running something malicious through the banner we would then look to block this IP and investigate to find the level of seriousness here if data has been stolen or if this was the beginning of a breach.

**Evidence B.**
VirusTotal should be used here to investigate the hash. The investigative question here is to see if any antivirus has come across this before and if VirusTotal has it, since this was flagged as unknown we initially want to see if it's found anywhere else before determining if it is dangerous or not. If it has been seen before we check in what context and if any antivirus says it's harmful, if so to not download the file. If not seen before to potentially spend some time investigating it in a safe environment and then looking to add it VirusTotal.

**Evidence C (initial submission).**
I would use exploit-db in this instance since we can index by CVE ID. We are investigating if the framework has weaponised code on it that could be harmful to our app and to our devices. If we find that the framework has weaponised public code we should look to halt any app, remove the framework or move to a different version of the framework without the threat.

**Evidence C (revised after review).**
I would use exploit-db in this instance since we can index by CVE ID. We are investigating if the framework version we are using has weaponised code on it that could be harmful to our app and to our devices, the lookup will tell us the framework version and we can find out if we are actually vulnerable. If we are vulnerable we should patch to a safe version, apply vendor mitigation, compensate control and if none of those are possible to emergency shutdown.
