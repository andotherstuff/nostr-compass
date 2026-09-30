# Link review — 2026-09-30

Draft checked: `content/en/newsletters/2026-09-30-newsletter.md` at SHA-256 `08440bb4505bc8a32ac3b907f1a6cf2b4917ab82873ddc3998ba39c47e28e705`. The hash was identical before and after the final HTTP pass.

## External URLs

The draft has 191 external URL occurrences and 166 unique destinations, unchanged in count after the heading edit. A fresh HTTP HEAD check of all 166 URLs at six concurrent requests returned HTTP 200 for each, with no host or semantic path mismatch. Every source external URL also appears as an `href` in the rendered Hugo newsletter. No GitHub API endpoint was called.

I separately opened [NIPs PR #2488](https://github.com/nostr-protocol/nips/pull/2488) and the [immutable NIP-86 specification permalink](https://github.com/nostr-protocol/nips/blob/5b9920982ae1f4061328c1b09a90360da28d13c8/86.md) with GET during this review. Both returned HTTP 200 at unchanged URLs with page titles identifying the expected PR and `86.md` at the stated commit.

## Internal URLs and rendered page

The draft has 44 `/en/topics/` or `/en/newsletters/` link occurrences and 36 unique routes. The generated newsletter HTML is newer than the source Markdown. Every one of the 36 source routes appears in its rendered `href` set, and every corresponding generated destination page exists, including `/en/topics/fips/`. The newsletter fragment `/en/newsletters/2026-09-23-newsletter/#nip-86-adds-clear-and-list-methods-for-relay-management` exists as an `id` in the rendered previous issue. All 58 rendered H3 headings have nonempty IDs after the heading cleanup.

## Failures and uncertainty

- Definite 404s or missing rendered destinations: none.
- Redirect mismatches or missing rendered anchors: none.
- Rate limits, access denials, timeouts, or transient server errors: none.

HTTP success checks reachability; it does not independently validate destination claims. The generated site check verifies local output, not the status of a public deployment.

GATE: PASS
