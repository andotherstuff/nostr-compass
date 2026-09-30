# ContinuityValueCheck — Compass #42

Draft: `content/en/newsletters/2026-09-30-newsletter.md`
Draft SHA-256: `08440bb4505bc8a32ac3b907f1a6cf2b4917ab82873ddc3998ba39c47e28e705`
Preceding published issue: `content/en/newsletters/2026-09-23-newsletter.md` (#41).
Reviewer: Codex subagent, 2026-09-29. This is a same-family editorial audit, not an independent-model review.

Both `python3 scripts/check_newsletter_continuity.py <draft> <#41>` and the broader `--history-dir content/en/newsletters` returned `PASS: repeated topics use new sources or state a material status change` on this exact SHA.

Manual comparison found distinct primary sources and material changes for repeated projects: MDK 0.11.0 recovery and delivery queue versus 0.10.4 durable sending; nostream 3.1.0 rate-based admission versus NIP-66 monitor publication; Amethyst's new group-interoperability merges versus its prior release and Quartz merges; Divine's encrypted video DM versus relay reconnect; Buzz's channel artifacts and ingress identity versus relay moderation; Conduit's checkout acknowledgement and signer sessions versus image upload; Mostro's library and daemon transport changes versus the earlier CLI migration and order timestamp; nostter's pin and replaceable-event work versus session-bound signing; Pensieve's isolated negentropy runtime versus durable receipts; ContextVM's inbound deduplication versus publish wait and stream fixes; Cordn's multi-device coordinator hints versus web-client offline queue; Wisp's comment-reply kind fix versus 1.2.4 thread reads; and Zap Cooking's account-history recovery versus image descriptions and search safety. Repeated release sections for Scramble, Amber, Ditto, and Armada also cite new tags or events with distinct behavior. The NIP-86 invite-code merge is separate from #41's relay-management clear/list methods.

The prior draft's statement that Compass covered the NIP-86 invitation proposal “last week” was corrected. The final draft accurately identifies the [July 8 issue](/en/newsletters/2026-07-08-newsletter/) as the earlier coverage and states the proposal's subsequent merge.

GATE: PASS
