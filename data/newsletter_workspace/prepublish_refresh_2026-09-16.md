# Compass pre-publication refresh — 2026-09-16

## Run and exact source pass

- Worktree: `/opt/data/compass-worktrees/2026-09-16`
- Edition: Nostr Compass #40
- Refresh began before the publication boundary and completed as delayed recovery at 2026-09-16T19:02:06Z.
- Exact frozen source window: `2026-09-08T00:00:00Z..2026-09-16T16:00:00Z`.
- Final immutable pass: `refresh-t_a4ffab29-final5-20260916T1600Z`.
- Manifest: `data/source_runs/source_run_2026-09-16_refresh-t_a4ffab29-final5-20260916T1600Z.json`; schema 2, `finalized: true`, all ten expected families observed.

| Family | Status | Exact-pass evidence |
|---|---|---|
| Projects | complete | 37,595 exact collector records; `collector_refresh-t_a4ffab29-final5-20260916T1600Z_projects.json` |
| NIP discussions | complete | 14 records, all explicitly skipped; `..._nip-discussions.json` |
| Nostr Recap | complete | 19 retained records; `..._nostr-recap.json` |
| Shakespeare apps | empty verified | complete exhausted query; `..._shakespeare-apps.json` |
| NIP-34 | complete | 167 records, all explicitly dispositioned; `..._nip34.json` |
| Zapstore | complete | 1,180 records, 1,006 developer-signed relevant records retained by collector gates; `..._zapstore.json` |
| App discovery | complete | 2,069 source records; 34 final candidates after signature, tracking, and persistent-baseline gates; `..._app-discovery.json` |
| Heartbeats | complete | 23,657 source records, 5,736 retained by collector gates; `..._heartbeats.json` |
| Monthly history | not applicable | September 16 is not the final weekly issue of the month; `..._monthly-history.json` |
| Specifications | complete | 2,096 source records, 26 retained by collector gates; `..._specs.json` |

`python3 scripts/build_coverage_history.py` passed with 393 projects across 40 newsletters. `bash scripts/detect_non_github_sources.sh` passed and recorded 32 tracked non-GitHub repositories, 19 relevant non-GitHub Zapstore releases, and 114 NIP-34 repositories without GitHub mirrors.

## Final candidate disposition

- Myco v0.7.0 was published at 2026-09-16T16:54:43Z, read back from the live GitHub API, and included as a Top Story. The copy covers sandboxed NIP-5D napplets and their permission model, encrypted offline file transfer, multi-path FIPS failover, compatibility limits, and the LMDB migration.
- Linky v26.9.17 was published at 2026-09-16T16:31:11Z, read back from the live GitHub API, and included under Tagged Releases. The copy covers the recovery-seed disclosure fix, payment-file URL hardening, and disabled Android backups.
- NIP #2468, NIP #2469, and Marmot #423 were integrated as distinct descriptive H3 sections. NIP-A3, NIP-CD, NIP-90, Marmot #422, and NWC #3/#5 were retained with exact merged/open status.
- Nostr Spring Boot Starter 0.6.0 was explicitly skipped after live release-note readback: the release establishes framework and `nostr-proto` dependency upgrades, not a distinct new Nostr-facing capability.
- The release-digest gate covered 44/44 projects with zero untriaged high-signal or unflagged projects. `selection_review_2026-09-16.md` records all 71 editorial candidate dispositions with no fixed item cap.
- PR #173 had no issue comments, inline comments, or reviews at the final authenticated scan. No unverified feedback or owner hold remained.

## Final exact-draft gates

Final newsletter SHA-256: `080a48f9b9a0e8ef7b1982dc5b55e86c64eba65caea66c35433a1e6bdce346c7`.

- Style and protocol-heading gate: PASS.
- Complete-history continuity: PASS.
- Paragraph primary-source links: PASS.
- Event examples, NIP-01 identifiers, and BIP-340 signatures: PASS.
- External HTTP audit: PASS, 53/53 unique links.
- Production Hugo/Pagefind build: PASS.
- Rendered topic audit: PASS, 8/8 topic pages and 8/8 backlinks.
- Python suite: PASS, 166 tests.
- Bun suite: PASS, 132 tests.
- `git diff --check`: PASS.

The assembled newsletter and section artifacts were synchronized after the final edit. The frontmatter is `draft: false` under the owner's explicit immediate-publication instruction. PR #173 remained open, draft, mergeable, and one commit at the last pre-push authenticated readback; the publication workflow must pin the amended one-commit head and successful exact-head CI before merging.

GATE: PASS (all ten maintained source families accounted for by one finalized immutable pass; Myco and Linky late releases integrated from live primary readback; all five review roles, 53 links, production build, topic backlinks, 166 Python tests, 132 Bun tests, and exact-draft checks passed)
