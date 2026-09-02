# Owner refresh notes — 2026-09-02

## Voca 1.0

The current draft contains no Voca coverage. Voca recorded its public 1.0.0
publication on 2026-08-27, after the initial draft's 2026-08-26 fetch cutoff.

- NIP-34 repository: `nostr://npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/relay.ngit.dev/voca`
- Exact local publication-record commit: `a44ae376b72ae4791500ea8ef0e5d3f3ab0a5b49`
- Release baseline commit: `c1f7e38a65cc6f1b3e0eabf240a35242a0d75cd7`

The Wednesday refresh must verify the public release against primary Nostr,
repository, and package evidence and integrate Voca into Newsletter #38. The
owner explicitly confirmed on 2026-09-02 that Voca has Nostr integration: it
fetches from Nostr relays, validates event signatures, reads events, and can
subscribe to an npub so its long-form articles are added to the queue. Verify
the exact implementation and event-kind details from primary source before
wording the claim, but inclusion itself is required rather than optional.
Mirror the final copy into the owning section artifact and rerun the full review
and build gates.

The owner also requires the finalized English Markdown file to be delivered in
the originating Marmot group before publication. Publication must remain held
until that exact file has passed Marmot delivery preflight and its attachment
has durable timeline readback.

## MDK v0.9.17 final-delta inclusion

The owner explicitly requested that MDK be updated to its latest release. MDK
v0.9.17 was published at 2026-09-02T15:21:14Z, after the scheduled final-delta
fetch began:

- MDK release: https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17
- Exact source commit: `2bbcca3ebe4a971152412c16c3049cc7bd08d278`
- Marmot C v0.9.17: https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17
- WN Agent v0.9.17: https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17

Update the existing MDK release entry from v0.9.15 to v0.9.17 and cover the
material 0.9.16–0.9.17 delta using the release notes and linked primary PRs.
The v0.9.17 MDK notes identify PRs #1617, #1620, #1621, and #1622 for lower-cost
pass-admission scans, contested-ness probing without full-graph seeding,
deferred-peel idle polling, and batched component reads at the remaining
projection sites. Synchronize the assembled newsletter and tagged-releases
section, then rerun exact-final review, link, and build gates.