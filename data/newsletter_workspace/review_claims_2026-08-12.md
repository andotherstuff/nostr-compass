# Claim review — Newsletter #35

Validated: 2026-08-12 UTC
Target: `content/en/newsletters/2026-08-12-newsletter.md`

Primary release notes and full in-window source records were rechecked for all selected project items. GitHub PR state was read back for every protocol item. The final correction removed NAP proposals whose branches had no in-window commits, NWC PR #2 because its August 2 merge was already covered in Newsletter #34, and repeated Concord PRs #13/#14. NIPs #2378 and Concord #12 remain only because each changed from open to closed-unmerged during this issue window, and the prose states that transition explicitly.

The Wednesday refresh compared the complete release notes and tag diffs for Nostria 4.1.67, Mostro 0.18.1, Buzz Desktop 0.5.10, and BitBlik 0.10.0. Nostria, Mostro, and Buzz introduced substantive Nostr-facing changes and were incorporated. BitBlik was skipped because its release concentrated on fiat payment rails, translations, NFC wallet import, and payout-state UI rather than a material Nostr protocol or client change. Mostro's retained checklist covers its Cashu escrow foundation, Nostr price provider, first-contact proof-of-work advertisement, NIP-44 dependency fix, key-log redaction, cooperative-cancel sender validation, LNURL hardening, payout validation, and hold-invoice restart recovery.

Every retained item has a distinct user-, relay-, signer-, messaging-, or protocol-facing change supported by its linked primary source. The required SKIP list accounts for vague releases, maintenance-only work, scope failures, discovery candidates without ownership/current-release proof, and recent duplicates.

The final-delta pass verified NIPs PR #2435 from its GitHub metadata and one-line `34.md` patch. The open proposal adds an optional pull-request `b` tag for a non-default target branch and cites matching ngit and GitWorkshop commits; the newsletter states both its proposed status and existing implementation evidence without presenting it as merged.

GATE: PASS (all selected project items, three late release updates, and all retained protocol claims reconciled against primary artifacts on 2026-08-12; no unsupported status claim remains)
