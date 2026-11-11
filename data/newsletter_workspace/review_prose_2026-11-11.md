# ProseReview: Newsletter #48 (2026-11-11)

Reviewer: Reviewer 3 (ProseReview)
Draft: content/en/newsletters/2026-11-11-newsletter.md (read in full, 307 lines)

## Script results

- `python3 scripts/check_newsletter_style.py <draft>`: PASS (no banned filler, opaque anchors, or grouped spec changes).
- `python3 scripts/check_newsletter_paragraph_links.py <draft>`: PASS.
- configured AntiPatternScanner tool: NOT RUN, file does not exist on this host.
- `shaka scan` / ProseReview skill: not available (not installed in this environment). Substituted by anti-slop below plus manual read.
- `anti-slop --json <draft>`: pass=true, score 97, 2759 words. Low-severity only: negation audit 37 in 2759 words = 1.34/100 (under 1.5, contextual review), Title Case heading at L89 and L143 (canonical headings, ignore), rule-of-three at L137.
- grep GHSA-/CVE-: 0 matches. No em dashes or banned meta-frames found in manual read.

## Word counts (prose only, excl. frontmatter, fences, link destinations)

Total about 2,681 (inside 2,000-3,000 target). Sections: Top Stories 154, Tagged Releases 1031, In Development 108, New Projects 109, Protocol and Spec Work 610, Deep Dive 611.
Entries over 90 words: Top story 154 (two paragraphs, acceptable but trim), Route96 108, Vector 97, NIP-D9 95, MDK 91, Keep Android 92. Routine entries at or under 90: rest. Structure OK: one entry per project, one H3 per PR, no closing section.

## Explainer inventory (first substantive mention)

Missing or weak context:
- NIP-88: first appears L9 and L23 (kind 1018 responses) with no description. Hard fail under first-mention rule.
- Marmot at L9 (intro) has no description; first description is L15 "encrypted groups" and full one at L117.
- Concord: first appears L71 (Vector, "Concord v1 communities") before its only description at L109.
- Not described at first mention: Frostsnap (L15), White Noise (L17), marmot-ts (L17), Shroud (L17), kiss-bdk (L17), Vertex (L35), Armada (L113), Amethyst/noStrudel/Coracle/welshman (L151, L299-301), KeyPackages (L17, defined only at L67), bunker (L59), "Commit" (L117), "device group" (L117-133, never explained).
- NIPs with descriptions: 01, 09, 13 (via proof of work), 40, 46, 47, 55, 57, 62, 65, 69, 77, 96, D9 OK. NIP-13 L151 acceptable.
- NIP topic-link targets: all slugs match (my awk check was a field-index artifact; visually verified).

## Fix list

LINE 9: "[Nostur] added polls, which this issue's NIP-88 deep dive explains" — NIP-88 undescribed at first mention; Marmot undescribed — "Nostur added polls under NIP-88 (Nostr polls), which this issue's deep dive explains" and "[Marmot](...) encrypted-group messaging".
LINE 23: "Votes are NIP-88 kind 1018 responses" — if L9 is fixed this is fine; otherwise add "(polls)".
LINE 15: "Frostsnap hardware signers co-sign payments to silent-payment addresses" — jargon, Frostsnap undefined — "Frostsnap hardware wallets jointly sign Bitcoin payments to silent-payment (reusable private) addresses".
LINE 17: "Most pin marmot-ts 0.9.0 ... White Noise rejects mdk squared's KeyPackages" — three undefined names, "pin" is jargon — "Most depend on marmot-ts 0.9.0, the TypeScript Marmot library. ... White Noise, the Marmot messenger, rejects mdk squared's KeyPackages (the keys a device publishes so others can add it)." Then trim L67 duplicate gloss.
LINE 17: "a Shroud chat pull request (still open) and a kiss-bdk multi-signer silent payment" — Shroud undescribed, awkward list — "an open Shroud chat pull request and kiss-bdk, a multi-signer silent-payment wallet".
LINE 17: "The Awesome Marmot catalog added them on 6 November." — catalog/tracker commentary, not what changed for readers — cut the sentence or link the catalog once as a pointer ("listed in the Awesome Marmot catalog").
LINE 27: "see a Tor exit node, not your IP address, onion relays can join your relay list" — comma splice, three clauses fused — "relays, images, uploads and the tip watcher see a Tor exit node instead of your IP address. Onion relays can join your relay list, and web links offer Tor Browser or copying."
LINE 31: "closes the last item of its security audit" — vague; "Until then the funder can take the sats back" — ambiguous "until" — "closes the final open item from its security audit" and "Until the counterparty accepts, the funder can reclaim the sats."
LINE 35: "in place of a raw proof" — unclear — "in place of the raw ownership proof".
LINE 35: "When the Vertex service will not answer" — Vertex undefined — "When Vertex, a Web of Trust scoring service, will not answer a personal trust check".
LINE 47: sentence starting "The app now decodes ..." is one 60-word sentence — split after "signed zap request" and start a new sentence for the https callback fix.
LINE 55: "relay auth requests are now decided per relay" — jargon — "relay authentication (NIP-42) requests"; add what is decided ("approve or deny").
LINE 59: "NIP-46 bunker list of 100 apps" — bunker undefined — "its NIP-46 (remote signing) bunker, which lists up to 100 connected apps". Entry is 92 words; cut the DNS clause if needed.
LINE 67: entry 91 words, dense — drop "using up to 20 KeyPackages ... last 30 days" detail or the downgrade sentence tail.
LINE 71: "Upgrading deletes unmigrated Concord v1 communities and their history." — Concord undefined here — "Upgrading deletes unmigrated communities built on Concord (encrypted Nostr communities) v1, with their history." Also "inbox relays" and "emoji packs set in other apps" need plain wording. Entry 97 words, trim.
LINE 77: "nosniff and a sandboxed content policy" — jargon; entry 108 words — "served with browser content-sniffing disabled and a sandboxing Content-Security-Policy"; compress the five bullets-in-prose to the three most material fixes.
LINE 83: "records it from source inspection only" — catalog workflow commentary — "The Awesome Marmot catalog lists it, but the code is unreleased and unaudited, so keep real funds out of it."
LINE 87: "The Awesome Marmot catalog lists it from source inspection, with no runtime test of the call path." — same issue — "Calls are untested outside the author's own builds" only if sourced, else cut.
LINE 93: "Its meaning depends on the message prefix" — "Its" ambiguous — "The parameter's meaning depends on the message prefix".
LINE 109: "revised Roles model with an @everyone role and rank ordering ... raid lockdown" — jargon list; "covered in the October 21 issue ... while still open" is tracker-style back-reference — "adds Discord-style roles with an @everyone default and rank order, categories, per-channel permissions, private channels, peer-to-peer voice and moderation tools (timeouts, raid lockdown)". Drop the issue-history clause or shorten to "(Newsletter #45)".
LINE 113: "open the owner's genesis community metadata under the delivered keys" — opaque — "decrypt the community's founding metadata with the keys it received, and confirm it came from the owner, before saving the join". "Armada" undefined — "Armada, another Concord client".
LINE 115-117: "moved devices keep trusting the old group until the first Commit" — "device group", "moved device", "Commit" never explained; the H3 says nothing a reader can parse — add one sentence defining a device group (a user's linked devices share one MLS group) and a Commit (MLS message that changes group membership/keys); rewrite H3 "Marmot: a moved device keeps its old group until its first Commit".
LINE 117: "In the first, a moved device ..." — refers to sibling H3s, breaks one-PR-per-H3 independence — reword "Marmot merged five experimental device-group changes in five days. PR 498 makes a moved device keep trusting ..." or move the count to the intro.
LINE 119-133: four 14-32 word entries without the problem solved or why it matters — add one clause each (e.g. L121 "so a lost or compromised device can be replaced without losing message history"; L125 "so stale devices stop receiving group keys").
LINE 137: "an answer, and a receipt confirming the agent runtime accepted it" — flagged rule-of-three by scanner (low) — "a request with up to four options, plus an answer and a receipt confirming ...". Also "one-shot agent decisions" unexplained — add "(a human or agent picks one option)".
LINE 141: "It has no maintainer approval." — ambiguous — "No NIP maintainer has approved it."
LINE 145: opening paragraph states mechanics and history but not the problem solved, and the whole deep dive has no design-tradeoff or adjacent-spec comparison section (NIP-69 aside at L297 is not a comparison; NIP-57 zap polls would fit) — add one opening sentence on the problem (public, countable polls on any relay) and a short "Tradeoffs" H3 (no vote privacy, relay-dependent tallies, spec silence on ties; kind 6969 zap polls vs NIP-88).
LINE 149: "polltype picks singlechoice (the default) ..." fine; "Each option tag pairs a short alphanumeric ID" fine.
LINE 151: "The poll below was posted from Amethyst" — Amethyst undefined — "Amethyst, an Android Nostr client".
LINE 297: sentence beginning "Polls get proof of work only when..." packs two unrelated facts (NIP-13 mining, kind 6969) in 55 words — split; move the kind 6969 aside to the new comparison section.
LINE 299: "It departs from the spec on single choice: the applesauce helper it relies on discards any response naming more than one valid option; it does not count the first." — "it" ambiguous, three clauses — "noStrudel departs from the spec on single choice. Its applesauce helper discards any response naming more than one valid option, where the spec counts the first."
LINE 301: "welshman's Poll reader" — welshman undefined — "welshman, Coracle's Nostr toolkit".
LINE 307: closing pointer is acceptable (one sentence).

## Residual notes (no change required)

- No hyperbole, banned meta-frames, closing section, or GHSA/CVE anchors.
- Negation density 1.34/100 under threshold; L31 "no longer hands" and L113 "was not a live vulnerability" are factual.
- Deep-dive example events: id/sig verification is Reviewer scope elsewhere; I only confirmed the 1794808500 endsAt = 2026-11-16 05:55 UTC and the 156-second vote gap, and 21 leading zero bits in the poll id.

## Verdict

Hard-fail items under the Reviewer 3 rubric: missing first-mention context for NIP-88 (L9) and Concord (L71), plus several undefined project/jargon terms in Marmot and spec entries, catalog workflow commentary (L17, L83, L87), and a deep dive lacking the required problem and tradeoff/comparison content.

GATE: FAIL

## Re-review addendum (draft SHA-256 `5a4a669a42e74783ca91b87c839a0fc47297230a3ebb68bfe4831bb0831ad42d`)

The re-review found every substantive finding resolved: first-mention context for NIP-88, Marmot, Concord, marmot-ts, White Noise, KeyPackage and kiss-bdk; split NoorNote, Monostr, Chama, Zapstore and zap-poll sentences; catalog commentary removed; Amber, Keep Android and MDK trimmed; the deep dive now opens with the problem and has a tradeoffs section. Residuals were then fixed: Shroud is described as a silent-payment wallet, the catalog sentence now states the caveat directly, and low-value clauses (Monostr links, Manent packaging, Streets history, nostr-social-graph bandwidth figure) were cut to bring the issue to 2,927 words by the anti-slop count. The Concord #25 back-reference keeps the "covered in the October 21 issue" phrasing because the continuity gate requires that form. Deterministic style, paragraph-link and continuity checks pass; anti-slop scores 95 with no critical, high or medium findings.

GATE: PASS
