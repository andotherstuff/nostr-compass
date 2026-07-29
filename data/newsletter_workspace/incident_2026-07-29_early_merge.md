# Publication incident — 2026-07-29

## Summary

A migration recovery Kanban card created with `--initial-status blocked` was automatically promoted and claimed because no typed block event existed yet. The worker changed Newsletter #33 to `draft: false`, committed `ee274c5b08407207fd4b0d9148d1a28255a0bedc`, and merged [PR #117](https://github.com/andotherstuff/nostr-compass/pull/117) at **2026-07-29T12:45:34Z**, before the intended 16:00 UTC publication window.

## Containment

- The worker process was terminated.
- The Compass pipeline parent remains blocked; translation and podcast children remain `todo`.
- GitHub Pages deployment for main SHA `4fd0ebedc662760c3d3d128f0315810b54d4dc6a` succeeded.
- No `publish/out/33/event.json`, `announcement.json`, `receipts.json`, signed workspace artifacts, or publish log existed at containment time.
- Direct queries to `wss://nos.lol`, `wss://relay.primal.net`, and `wss://purplepag.es` recovered no canonical kind 30023 event for Newsletter #33.
- Therefore no Nostr publication was verified and no translation/podcast work was released.

## Recovery gate

1. The 14:00 UTC `compass-wednesday-refresh` job must rerun every source family and write `prepublish_refresh_2026-07-29.md` with evidence-bearing `GATE: PASS` or `GATE: FAIL`.
2. It may create a publication-day update PR if material late changes exist, but must not merge, sign, or broadcast.
3. The 16:00 UTC `compass-wednesday-publish` job owns final publication. It may use the already-deployed base issue or first merge a PASSed update PR.
4. The Kanban parent completes only after production verification and independent relay recovery of both kind 30023 and kind 1 events.

GATE: CONTAINED — waiting for 14:00 refresh and 16:00 publication.
