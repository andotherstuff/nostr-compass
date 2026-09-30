# TopicAudit — Compass #42

Draft: `content/en/newsletters/2026-09-30-newsletter.md`
Draft SHA-256: `08440bb4505bc8a32ac3b907f1a6cf2b4917ab82873ddc3998ba39c47e28e705`
Rendered page: `public/en/newsletters/2026-09-30-newsletter/index.html`, rebuilt 2026-09-29 15:29 UTC.
Reviewer: Codex subagent, 2026-09-29. This is a same-family editorial audit, not an independent-model review.

The draft contains 31 distinct `NIP-*` labels. Every label has a sourced topic page, a topic link in the issue, and a #42 Mentioned in backlink. The numbered historical pages NIP-26 and NIP-28 identify their current unrecommended status. The `NIP-AR`, `NIP-DB`, `NIP-FE`, and `NIP-FI` pages distinguish project or open proposal terminology from accepted NIPs. The NIP-FE page also identifies the unrelated, still-open private-feeds proposal using the same provisional label.

`python3 scripts/check_topic_backlinks.py content/en/newsletters/2026-09-30-newsletter.md --rendered-html public/en/newsletters/2026-09-30-newsletter/index.html` returned `PASS: 35 topic pages have Primary sources blocks and 36 rendered newsletter backlinks` on this exact draft and rendered page. A separate check found 36 explicit `/en/topics/` or `/en/newsletters/` links in the draft, all with existing Markdown targets; every #42 fragment used by the draft exists in the rendered HTML. The topic pages' #42 fragments also pass the rendered checker. The four protocol headings use plain text so their fragment IDs remain stable while their body paragraphs link the topic pages.

GATE: PASS
