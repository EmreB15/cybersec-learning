# Phishing Anatomy

**Track:** Concepts | **Level:** L1 | **Date Completed:** 2026-05-10 | **Hints Used:** 1 tutor explanation (lens 6) | **Time Spent:** ~50m

## What This Was

First Concepts L1 challenge. Direct response to **WA002** (diagnostic phishing analysis was partial — surfaced obvious red flags but missed link inspection, account specifics, and footer analysis).

A 6-lens systematic framework was introduced (Sender / Subject / Body / Call to Action / Links / Footer), then applied to a fresh phishing email — a fake DocuSign signature request. The framework was designed to upgrade phishing analysis from instinct ("this feels off") to method (run every lens, every time, including ones that look empty — because absence of an indicator in a lens is itself information).

The email had spoofed sender domain (`docusign-secure.net` vs real `docusign.com`), urgency framing, generic greeting, disarming "safely ignore" line, mismatched link (displayed "Review Document" with actual URL `docusign-verification.tk/auth?...`), and a deliberately absent footer.

## What I Built

I analysed an email against 6 lenses. I was checking the email to see if it was a phishing attempt. I had to go through in detail each lens and figure out every detail as to why this might be a phishing attempt. I did not make the lenses but I used them as a guide.

## Key Concepts Used

- **6-lens phishing analysis framework**: Sender / Subject / Body / Call to Action / Links / Footer.
- **Lookalike domain spoofing**: attacker registers a domain that visually resembles the target (`docusign-secure.net` vs `docusign.com`) — the most common phishing technique.
- **Display text vs href mismatch**: the link a user _sees_ and the URL a click _resolves to_ can differ. Hover/inspect always.
- **TLD reputation**: country-code TLDs (`.tk` Tokelau, `.uk` UK, etc.) and generic TLDs (`.com`, `.net`) carry different baseline trust. A US SaaS company should not be operating from a Pacific micro-state TLD.
- **Workflow blending as a social-engineering play**: the most dangerous phishes mimic _routine business emails_ (DocuSign requests, Microsoft 365 alerts, payroll notifications) rather than relying on urgency alone — they don't trigger the "this feels weird" instinct.
- **Absence as an indicator**: missing personalisation, missing footer, missing specifics — empty fields are signals, not free passes.

**Sources cited (Concept-Track integrity rule):**

- NIST SP 800-177 Rev. 1, _Trustworthy Email_ (sender authentication infrastructure: SPF/DKIM/DMARC).
- CISA, _Recognize and Report Phishing_ guidance (user-facing indicator framework).

## What I Got Wrong First

I failed the domain false flag check. I also failed to realise that the provided link was not with the same domain. I guess same root cause is that I was unaware of the domain name of DocuSign. I also got the .tk wrong, I thought it was something to do with tokens but it was a country code I think. I missed an entire lens for the footer as I was confused.

## Weak Points Flagged

- **WP003 (new — promoted from WA002).** Phishing analysis: declares "no indicator" on a lens without doing or naming the verification step that lens requires. Not a knowledge gap (can't be expected to know every company's domain) — a method gap. The skill: when a lens needs information you don't have, the lens output is _"I'd verify X"_ not _"no indicator."_ Stage 0, retest 2026-05-14.
- **WP002 cross-reference.** The lens-5 first-pass behaviour (skip the URL inspection, jump straight to "what the link does") is the same shape as the bash WP002 frequency-pipeline failure — _infer the answer without doing the named verification step_. Not double-logged, but watching whether this is one underlying habit across tracks.

## What I Would Do Differently

Next time I will check the domain name before beginning and then use that as my reference. I will always check the footer of the email for any discrepancies. I will inspect the provided link in detail to make sure I understand what it is and where it might send me.

## Final Output

lens 1 - sender - the email was sent from 'docusign-secure.net' but DocuSign's domain is DocuSign.com so this is not a match. Also the 'secure' gives a false sense of security. Why would a document signature come from the 'DocuSign Security' this is strange, it would surely come from a different department.
lens 2 - Subject - 'expiring' this makes the reader feel urgency as something is expiring. The Ref in brackets makes it feel formal alongside the square brackets. feels automated due to the ref number.
lens 3 - body - they do not cite anything about the receiver. It feels very generic and is easily sent to many users. 'hello' also doesn't feel corporate. Something that doesn't make sense is that the document is awaiting a signature but it writes 'if you did not request this document' which makes it feel strange. It sort of tries to throw the user off by offering a sense of security. The thank you also feels off, if someone is asking you to sign something why are you being thanked?
lens 4 -call to action-in the subject there is a 'signature needed'. In the body there is an 'urgent' and 'expire within 24 hours' setting a time constraint to make the user feel stressed and left with no choice.
lens 5 - links - this link will take you to a sign in for the 'docusign', but this will be a fake sign in box and once you enter your details you will be hit with a wrong password to make you re-enter and then the hacker will more than likely have something that is or very very close to your details. It is definitely not a link to a document. The domain name again doesn't match, so this is a big no. the .tk points to something to do with tokens? the auth has something to do with authentication so it will likely try to make you authenticate something illegitimate.
lens 6 - does not exist, no copyright sign, no legitimate signs. No unsubscribe button. No footer is a big sign of a phishing attempt.

A target would click here because they would feel a sense of security plus a sense of urgency, it was sent to their work email so they might feel like it is real.
