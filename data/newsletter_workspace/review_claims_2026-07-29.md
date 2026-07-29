# Newsletter #33 claims review

Generated: 2026-07-29T14:35:31Z
Target: `content/en/newsletters/2026-07-29-newsletter.md`

## Live verification

- Extracted 34 distinct `NIP-XX` citations and verified every corresponding file through `gh api repos/nostr-protocol/nips/contents/<NN>.md`: 34/34 present.
- Extracted 52 distinct GitHub PR URLs and queried every pull-request API endpoint: 52/52 present, comprising 43 merged and 9 open PRs, with 0 closed-unmerged PRs.
- Rechecked Amethyst release tags `1.13.0` and `1.13.1`. The broad app, browser, Git, payment, and identity feature set is now attributed to 1.13.0; only the July 29 follow-up changes are attributed to 1.13.1.
- Rechecked Bray `2.3.0` and merged PRs #75, #76, and #77 against the live release and PR APIs.
- Rechecked Buzz Desktop `0.5.0` and merged PRs #3141, #2871, #2862, and #2607 against the live release and PR APIs.
- Rechecked Kairos `0.1.1` against the developer-signed Zapstore event; the text now uses the release's exact local-instruction terminology.

## Attribution and scope

The late Bray and Buzz stories fall inside the issue window, directly affect Nostr signing, relay authentication/search, Blossom testing, and identity behavior, and cite primary sources. Bitcoin-only and host-only material remains excluded.

GATE: PASS (34/34 NIP files and 52/52 PR API records verified; release attribution audit complete at 2026-07-29T14:35Z)
