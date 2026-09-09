# Assembly Report: 2026-09-09

Stage 6 condensation and its Sol correction loop updated `content/en/newsletters/2026-09-09-newsletter.md`, the final selection evidence, synchronized section artifacts, and affected topic backlinks. This remains within `EDITORIAL_MUTATION_BOUNDARY: owner-feedback-condensation-prose` and `IMPLEMENTATION_OWNER_KEY: compass-edition:2026-09-09:owner-feedback-condensation-prose`; publisher and review-authority code were not changed.

## Condensation boundary

- Top Stories: 7 retained — ngit / GitWorkshop, nsite-clay, Wingman App, Shosho / Livelier, Communitator, cal.emre.xyz, and Plektos.
- Tagged Releases: 9 retained — Vector, Primal Android, GRAIN, LibreNostr, SkateSpots, Whistle, TWENTY ONE Companion, ZapStore, and Amber. Vector and Primal Android were moved from the former Top Stories block into Tagged Releases; Mafrend was removed after exact tag comparison showed no in-window code change.
- In Development: 4 retained — Zap Cooking, Conduit, Amethyst/Grimoire/Pollerama as one ecosystem item, and Ditto. NosCall was removed after the final prose review found too little reader consequence for a standalone item.
- Protocol and Spec Work: 3 retained — NIP-01 `limit: 0`, NIP-78 authenticated app data, and the open NIP-AC signaling proposal.
- NIP Deep Dive: NIP-21 URI dispatch, NIP-19 semantics, NIP-27 rendering and optional tags, trust/failure behavior, three client examples, and the verified seven-field event were retained.
- Removed from the assembled draft: all items listed under “Removed from the current draft” in `selection_review_2026-09-09.md`; no projects were added.

## Evidence

- Frontmatter preserves `draft: true`, `date: 2026-09-09`, `publishDate: 2026-09-09`, and `type: newsletters`.
- The condensed draft contains 3,278 words and 31,258 bytes by `wc`; section counts are Top Stories 744, Tagged Releases 865, In Development 326, Protocol and Spec Work 200, and NIP Deep Dive 982 words.
- Sol's factual-control pass removed Mafrend, recast Livelier around Shosho's substantive release, corrected nsite-clay and Wingman source targeting, narrowed SkateSpots and Ditto claims to their evidence, linked the exact deep-dive event, reconciled topic backlinks, and removed topic pages created solely for discarded proposals.
- The exact condensed Markdown SHA-256 is `b3d4be55ec64028c71891f417fca36169e8f52cff8eb6075a53f34efb0e9b359`.
- The standard welcome line and NIP-17 DM footer remain present.
- The deep dive retains the full real seven-field NIP-01 event (`id`, `pubkey`, `created_at`, `kind`, `tags`, `content`, `sig`) exactly as supplied in the approved draft.
- The retained source corrections keep Shosho on its canonical GitHub release URL, SkateSpots on its live Zapstore page plus locally verified signed event evidence, and the deep-dive event on its exact resolving identifier; no nonexistent SkateSpots GitHub repository link is present.
- The exact draft passes Shaka at 100/100 with zero violations, plus the style, paragraph-source, full-history continuity, and structured-event checks.
- `python3 scripts/sync_newsletter_sections.py content/en/newsletters/2026-09-09-newsletter.md` synchronized `lead-stories.md`, `tagged-releases.md`, `unreleased-changes.md`, `protocol-work.md`, `nip-updates.md`, and `nip-deep-dive.md`. Existing writer provenance wrappers were preserved and all synchronized section gates were reset to `GATE: PENDING REVIEW`.

Stage 7 independent review, publication, outreach, PR update, and handoff remain outside this bounded wording pass.

GATE: PASS (owner-feedback condensation and Sol factual control complete; style, paragraph-source, continuity, event-structure, section-sync, YAML, topic-backlink, production Hugo/Pagefind, and diff checks pass; fresh exact-revision Stage 7 review required)
