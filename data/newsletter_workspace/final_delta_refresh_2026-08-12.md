# Compass final delta refresh — 2026-08-12

Target: `content/en/newsletters/2026-08-12-newsletter.md`
Draft PR: [#133](https://github.com/andotherstuff/nostr-compass/pull/133)

## Clock and prerequisites

- Live UTC gate verified at `2026-08-12T15:20:06Z`, inside the required Wednesday 14:30–15:59 window.
- Broad pass began at `2026-08-12T15:20:44Z`.
- Mandatory final cutoff pass began at `2026-08-12T15:32:48Z` and finished at `2026-08-12T15:44:14Z`.
- `prepublish_refresh_2026-08-12.md` ended in an evidence-bearing `GATE: PASS` before this task edited the draft.
- PR #133 was a draft, single-commit PR at the start of the pass.

## Broad pass

`scripts/fetch_all.sh --since-days 8 --newsletter-date 2026-08-12` completed nine applicable source families and skipped only month-end history because August 12 is not the month's final weekly issue. It refreshed tracked GitHub projects, Nostr/NIP discussions, Nostr Recap, Shakespeare apps, NIP-34 repositories, Zapstore releases, untracked-app discovery, OpenSats/Sovereign Engineering heartbeats, and all seven specification families. All produced artifacts were reported as zero hours old and no fetch family failed.

The only repository delta relative to the 13:20 prepublish snapshot was specification activity: NIPs PR #2435 opened at `2026-08-12T15:26:34Z`, and the already-merged NWC PR #2 received metadata activity without a new merge or content change. No other broad-pass source artifact changed.

## Mandatory post-15:30 cutoff

The one-day cutoff reran tracked repositories, Nostr/NIP discussions, Nostr Recap, Shakespeare apps, NIP-34 discovery, untracked-app discovery, OpenSats/Sovereign Engineering heartbeats, and all seven spec families. The Zapstore relay's full app-metadata pagination did not finish within the publication window, so it was stopped after ten minutes; the successful 15:20 broad Zapstore pass was retained and had produced no delta from the prepublish snapshot. Month-end history remained inapplicable.

Cutoff counts included 4 app-discovery candidates, 297 in-window `nostr-fund` events across 31 repositories, 483 `general-fund` events across 49 repositories, zero SEC-tagged events, one active NIP PR, zero BUD/NAP/MIP/Gamma/Concord changes, and one NWC metadata update. No additional publishable item appeared after PR #2435.

## Triage and integration

### Included

- [NIPs PR #2435](https://github.com/nostr-protocol/nips/pull/2435): verified through the GitHub PR API and exact `34.md` patch. The open proposal adds an optional `b` tag to NIP-34 pull-request events so a PR can target a non-default branch. Its body links implementations in ngit and GitWorkshop. The item was added to the English draft, synchronized protocol section, NIP-34 topic page, claims review, and spec snapshot.

### Excluded

- NWC PR #2: metadata-only update at `2026-08-12T14:36:41Z`; it merged August 2 and was already covered in Newsletter #34, so there is no new material status change.
- All other cutoff candidates: no new source delta relative to the successful prepublish/broad snapshots, or no publication-standard Nostr-facing change.

## Verification

- Claims: PR #2435 title, open status, timestamp, one-line NIP patch, and implementation links verified from GitHub primary data.
- Continuity: `PASS: repeated topics use new sources or state a material status change` against the complete English archive.
- Prose/style: `PASS: no banned Compass filler phrases`; the complete issue retained canonical structure and explicit proposal status.
- Links/sourcing: `PASS: every prose paragraph links to a repository or primary source`; 73/73 unique external destinations returned HTTP 2xx/3xx, with zero duplicate destinations.
- Events/topics: `PASS: every JSON event example has valid structure and no placeholder data`; 8 topic pages have Primary sources blocks and 8 rendered backlinks.
- Identity database: 318 entries and 166 unique valid pubkeys; zero errors (two documented legacy-evidence warnings).
- Build: `bun run build` passed for all ten locales; Pagefind indexed 2,204 pages.
- Integrity: `git diff --check` passed and the assembled Markdown is synchronized with section artifacts.

## Publication boundary

The newsletter remains `draft: true`. This task did not merge PR #133, deploy, sign, broadcast, translate, prepare the podcast, or send duplicate outreach.

GATE: PASS (broad pass started 2026-08-12T15:20:44Z; mandatory cutoff started 15:32:48Z; all source families accounted for; NIPs PR #2435 integrated from primary evidence; 73/73 links live; five review gates and production build passed; publication boundary preserved)
