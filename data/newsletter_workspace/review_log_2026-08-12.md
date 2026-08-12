# Newsletter #35 consolidated review

Validated: 2026-08-12 UTC (Wednesday pre-publication refresh)
Target: `content/en/newsletters/2026-08-12-newsletter.md`

## Final review outcome

The Wednesday refresh preserved the earlier continuity corrections and added three fully verified release updates: Nostria 4.1.67, Mostro 0.18.1, and Buzz Desktop 0.5.10. The final-delta pass added NIPs PR #2435 after verifying its one-line NIP-34 patch and implementation links. All other late candidates were explicitly skipped where the Nostr relevance, ownership, continuity, or complete delta did not meet the publication standard.

## Evidence-bearing gates

1. **Claims and project selection: PASS.** Every retained item has a primary source, an in-window material change, a Nostr-facing consequence, and a continuity rationale. The late-release checklist is recorded in `review_claims_2026-08-12.md`, and all final-two-day candidates have an include/skip disposition in `prepublish_refresh_2026-08-12.md`.
2. **Continuity: PASS.** The complete-archive checker reports that repeated topics use a new source or an explicit material status change.
3. **Links and sourcing: PASS.** All 73 distinct external destinations returned HTTP 2xx/3xx. Exact-destination duplicate count is zero. Every prose paragraph has a repository or primary-source link.
4. **Prose and structure: PASS.** The complete refreshed draft was read front to back and passes the style scanner after the last edit.
5. **Topics and event examples: PASS.** Both real relay-recovered event examples pass structural validation. Eight topic pages have primary-source blocks and eight rendered backlinks.
6. **Build and integrity: PASS.** `bun run build` completed for all ten locales and Pagefind indexed 2,204 pages. `git diff --check` reports no whitespace errors.

Individual evidence: `review_claims_2026-08-12.md`, `review_links_2026-08-12.md`, `review_prose_2026-08-12.md`, `review_topics_2026-08-12.md`, and `review_continuity_2026-08-12.md`.

The newsletter remains `draft: true`. No merge, deployment, signing, broadcast, translation, or podcast action has occurred.

Stage 8 opened draft PR #133. The verified outreach campaign delivered review invitations to all 14 eligible unique recipients: 13 in the main receipt and Safebox Acorn in a successful targeted retry. Two identities were excluded by the repository's explicit `no_dm` list. No eligible recipient remains unresolved.

The final-delta pass reran continuity, style, paragraph-source, event-example, production-build, rendered-topic-backlink, whitespace, duplicate-destination, and live-link gates against the final assembled file. All 73 unique external destinations returned HTTP 2xx/3xx, and synchronized section artifacts match the assembled Markdown.

GATE: PASS (final delta passed at 2026-08-12T15:45Z: broad and post-15:30 cutoff passes accounted for every source family, NIPs PR #2435 integrated, 73/73 links live, five review gates and production build passed)
