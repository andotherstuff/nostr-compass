# Review Log — 2026-07-22 (Newsletter #32)

Draft: content/en/newsletters/2026-07-22-newsletter.md (draft: true)
Swarm run: 2026-07-21 15:00–15:30 UTC. Round 1 → fixes applied → verified.

## Round 1 results

| Reviewer | Report | Round 1 verdict | Evidence |
|----------|--------|-----------------|----------|
| LinkChecker | review_links_2026-07-22.md | FAIL → fixed | 46/47 external links curl 200 OK (njump.me 403 is anti-scrape; content verified alive via Firecrawl); 12/12 internal topic links verified. 2 bare PR mentions + 1 unlinked version flagged. |
| ClaimCheck | review_claims_2026-07-22.md | FAIL → fixed | 40+ claims VERIFIED via gh/curl/nak (PR states, release tags, IndieSats kind-1 note content, NIP kind numbers vs spec text, zapstore data). 1 MISMATCH: Amethyst PRs #3653/#3654 mischaracterized as QA hardening (actually feature PRs). |
| ProseReview | review_prose_2026-07-22.md | FAIL → fixed | grep-verified scans: 0 em dashes, 0 curly quotes; 5 "rather than", 2 "worth X-ing", 1 "matters" amplifier, 1 "streamline", 5 hedging/intensifier hits, 8 "ecosystem" (branding exemption noted for "Iris ecosystem"). |
| TopicAudit | review_topics_2026-07-22.md | PASS | 12/12 topic pages verified (all exist, all have Primary sources); 0 missing-page errors; 12 Mentioned-in updates queued for assembler; no new topic page warranted this week. |

## Fixes applied (Orchestrator, 2026-07-21 ~15:25 UTC)

Links:
1. L153: linked bare "nostream's PR #702" → https://github.com/Cameri/nostream/pull/702
2. L176: linked bare "nostream's PR #676" → https://github.com/Cameri/nostream/pull/676
3. Amethyst v1.13.0 body mention: resolved together with the claims fix below (reviewer-approved rephrase option; tag does not exist yet so no tag link possible).

Claims:
4. Amethyst item: dropped the mischaracterized PR #3653/#3654 references; now reads "with further v1.13.0 prep PRs landing through 07-21".

Prose (11 edits):
5. "actually remove" → "remove"; "not just a statement of intent" → "with working client code behind it"; "an ecosystem that usually talks" → "a space that usually talks"
6. Sonar: dropped trailing "rather than a new headline"
7. FIPS: "it matters this week as connective tissue" → "this week it is connective tissue"
8. Trusted Relay Assertions: "rather than hardcoding operator lists" → ", replacing hardcoded operator lists"
9. NIP-47 open item: "is a discussion worth watching" → "deserves attention"
10. NIP-29 pinning: "rather than toggling single entries" → "instead of toggling single entries"
11. NIP-29 banner: "streamline admission" → "simplify admission"
12. NIP-46: "could simply never respond" → "could never respond"
13. kind:10021: "just-merged" → "newly merged"; "rather than shipping against 10011" → ", not 10011"
14. NIP-47 bullet: "worth following for any wallet" → "any wallet or app that speaks NWC should track"
15. NIP-5D: "rather than event.origin" → ", not event.origin"
16. Deep dive: "just shipped" → "shipped this week"
17. "from the same ecosystem" → "from the same project family" (nostr-social-graph item)

Remaining "ecosystem" uses (6) are all "Iris ecosystem" as the project-cluster branding the Iris Stack site itself uses; retained per ProseReview's documented branding-exemption note.

## Post-fix verification (Orchestrator-run, not narrated)

- `grep -c "rather than"` → 0
- `grep "streamline|simply |actually |worth watching|worth following|just-merged|just shipped|it matters"` → 0 hits
- `grep -c "—"` → 0
- `hugo --buildFuture` → exit 0, 283+ pages, no errors (run 2026-07-21 15:27 UTC)

## Round 2 verdict

All four reviewers' fix-lists exhausted; no reviewer reported a second-round issue class. Prose re-scan by Orchestrator confirms zero remaining banned-pattern hits outside the documented branding exemption.

GATE: PASS (post-fix grep scans: 0 banned-structure hits; hugo --buildFuture exit 0)
