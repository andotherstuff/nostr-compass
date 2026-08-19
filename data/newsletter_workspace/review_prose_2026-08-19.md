# Review: ProseReview — Newsletter #36 (2026-08-19)

## Mechanical checkers

```
python3 scripts/check_newsletter_style.py content/en/newsletters/2026-08-19-newsletter.md
  PASS: no banned Compass filler phrases
python3 scripts/check_newsletter_paragraph_links.py content/en/newsletters/2026-08-19-newsletter.md
  PASS: every prose paragraph links to a repository or primary source
python3 scripts/check_month_end_history.py content/en/newsletters/2026-08-19-newsletter.md
  PASS: month-end history title, yearly depth, sourcing, and progressive narrative are valid
```

The month-end checker passes in its deep-dive mode: 2026-08-19 plus seven days stays inside
August, so a history section is correctly absent.

## Anti-slop scan

```
bun ~/.claude/skills/_BLOGGING/Tools/AntiPatternScanner.ts content/en/newsletters/2026-08-19-newsletter.md
  PASS  score 100/100  qualitative 50/50
  slop-density 0.00/100  negations 0 (threshold 1.5)
  Zero violations.
```

The first scan of this draft returned 98/100 with two low findings, both three-item lists in
the opening digest. The Citrine clause was rewritten to two items and the Vector clause to a
single object, after which the scan returned zero violations. Recorded because a passing score
that was never re-earned after an edit is not evidence.

## Manual prose pass

- Em dashes: 0 occurrences.
- Banned intensifiers (`actually`, `basically`, `clearly`, `definitely`, `essentially`,
  `eventually`, `fundamentally`, `literally`, `obviously`, `quite`, `really`, `simply`,
  `truly`, `very`, `virtually`): 0 occurrences.
- Banned buzzwords (`exciting`, `dive into`, `robust`, `leverage`, `cutting-edge`,
  `ecosystem`): 0 occurrences.
- Banned comparison structures: three `rather than` constructions and one `not X but Y`
  construction were present in the first draft and were rewritten into positive statements.
  Current count: 0.
- Banned meta-frames (`worth noting`, `worth flagging`, `one to watch`, `the key takeaway`):
  one `worth reading as a signal` was present in the nostrord paragraph and was replaced with a
  direct claim about where the specification's working definition lives. Current count: 0.
- Rhetorical questions: 0.
- Workflow, tracker, fetch-queue, discovery, or scope-cut commentary in reader-facing prose: 0.
  The Glow section states its Lightning work carries no Nostr surface, which is an editorial
  statement about the project, not about Compass's pipeline.

## Structure

Canonical order verified: Top Stories, Tagged Releases, Newly Discovered, In Development,
Protocol and Spec Work, NIP Deep Dive. No "Closing notes" or "Closing thoughts" section. Six
H2 sections and 29 H3 subsections across 6,382 words.

GATE: PASS (style checker, paragraph-link checker, and month-end checker all PASS; anti-slop scanner 100/100 with zero violations, re-run after the fixes it prompted; 0 em dashes, 0 banned intensifiers, 0 banned comparison structures, 0 meta-frames)
