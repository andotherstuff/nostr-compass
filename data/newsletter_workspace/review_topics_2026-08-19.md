# Review: TopicAudit — Newsletter #36 (2026-08-19)

## Production build

```
npm run build
  Hugo build + Pagefind index, exit 0
  public/en/newsletters/2026-08-19-newsletter/index.html written (71,081 bytes)
hugo --buildFuture --buildDrafts
  exit 0
```

The draft carries `draft: true` and a future `publishDate`, and still renders under the
production build script, so the checker below runs against the same minified HTML production
would serve.

## Backlink checker

```
python3 scripts/check_topic_backlinks.py \
  content/en/newsletters/2026-08-19-newsletter.md \
  --rendered-html public/en/newsletters/2026-08-19-newsletter/index.html
  PASS: 27 topic pages have Primary sources blocks and 27 rendered newsletter backlinks
```

## Topic pages touched

Twenty-seven topic pages are referenced: `blossom` plus NIP-05, 07, 10, 13, 17, 22, 27, 29, 42,
43, 44, 45, 46, 47, 51, 55, 58, 59, 5A, 65, 66, 70, 73, 78, 86, and 98. NIP-65 and NIP-78 joined
the set with the Nail section on 2026-08-18 and were backlinked and rebuilt in the same pass. Every one already existed with a
Primary sources block, so no new topic page was required this issue. Each received one
`Mentioned in` entry pointing at the section of #36 where the topic first appears, and every
fragment was validated against the ids present in the rendered production HTML rather than
assumed from the Markdown heading.

The first pass inserted those entries without a blank line before the following `**See also:**`
block on 24 of the 25 pages, which would have folded two definition lists together in the
rendered output. That was corrected and the site was rebuilt before this gate was recorded.

## Link-target correctness

Every `[NIP-XX](/en/topics/nip-yy/)` pair was audited for a matching identifier:

```
27 topic links checked, 0 mismatches
```

The two deep-dive subjects, NIP-58 and NIP-22, both link to their own pages, and the adjacent
specifications each dive compares against (NIP-51 for badges, NIP-10 for comments) link to
their own pages as well.

GATE: PASS (production build exit 0; backlink checker PASS with 27/27 topic pages carrying Primary sources and a validated #36 fragment; 0 NIP-to-topic-page mismatches; 0 new topic pages required)
