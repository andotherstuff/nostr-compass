# Email digest trial

The owner approved a four-issue trial on 2026-10-06, beginning with Compass
#43 (2026-10-07) and continuing through #46 (2026-10-28). The email becomes an
800–1,200-word digest linking to the complete edition and its deep dive. A
quiet week may be shorter; 1,200 words is the email maximum. This range is a
trial hypothesis, not a claim about an optimal reading length.

## Full edition and podcast source

`content/en/newsletters/<date>-newsletter.md` remains the complete canonical
edition. Its date, issue number, section order, primary evidence, qualifying
coverage, deep dive or month-end history, participant identities and section
anchors retain their existing rules. Concise entries and one substantive news
entry per project apply to the full edition as well as the email.

The website, RSS, translations, Nostr article and announcement, podcast prep,
Logbook section mapping, and review/podcast participant extraction continue to
consume the full edition. Podcast prep covers every full-edition topic in its
actual order. It must never read the email digest as its newsletter source.
Publication proof, dependent-card promotion, Logbook access checks, invitation
timing and recipient exclusions retain their existing gates. The digest is
not a new publication signal, episode, source collector or invitation campaign.
The current podcast release deadline remains the first verified newsletter
publication + seven days (604800 seconds, same UTC time).

Keep the digest outside `content/`, in
`data/newsletter_workspace/email_digest_<date>.md`. It must not use the canonical
`<date>-newsletter.md` filename or be passed to `scripts/publish.ts` or the Nostr
publication payload parser. No canonical headings or anchors are renamed to
accommodate the email.

## Editorial shape

Write the digest after the full edition has cleared source and selection gates
and has been assembled. Use the reviewed full edition as the evidence source:

- Open with the week's most consequential changes, without a second copy of
  the same project later in the email.
- Give selected project updates one or two concrete sentences: what changed,
  why a reader would care, and a meaningful remaining limit where evidenced.
  Combine release and development progress under one project entry.
- Provide brief navigation to other broad coverage in the full edition.
  Email omissions do not remove qualifying items from the canonical edition.
- Tease the deep dive or history with the question it answers and a link to
  its full section; preserve technical depth, signed examples and references
  in the full edition and topic pages.
- Close with a clearly labeled link to the complete issue. Prefer descriptive
  section links over a long list of project names, vague teasers or changelogs.

Use prose, short headings and inline Markdown links. Avoid images, raw HTML,
inline code, code fences, reference links and nested link syntax in this digest draft.
These constraints make the preparation helper's URL and word checks explicit.
Write web URLs as `[descriptive label](URL)` with no optional link title;
bare web URLs, indented code and malformed links fail preparation.
Percent-encode literal parentheses in URL targets. Preparation receipts contain
local paths and stay in the workspace; keep them out of public commits.

## Preparation and review

Digest frontmatter binds the exact source bytes, including frontmatter:

```yaml
---
type: email-digest
issue: 43
edition: 2026-10-07
newsletter_sha256: <SHA-256 of the complete canonical Markdown file>
---
```

After the normal production build, prepare the email against that same build's
rendered full edition. For example, from the owning edition worktree:

```bash
python3 scripts/prepare_email_digest.py \
  --newsletter content/en/newsletters/2026-10-07-newsletter.md \
  --digest data/newsletter_workspace/email_digest_2026-10-07.md \
  --rendered-html public/en/newsletters/2026-10-07-newsletter/index.html \
  --output data/newsletter_workspace/email_ready_2026-10-07.md \
  --receipt data/newsletter_workspace/email_digest_receipt_2026-10-07.json
```

The helper checks issue/date/source binding, converts internal URLs to absolute
URLs, verifies full-edition fragments against actual rendered IDs, requires a
link to this issue and enforces the email word maximum. It does not summarize,
verify claims, certify a fresh build, sign, send, create publication proof or
replace the canonical file. Its receipt records exact input/output hashes,
`editorial_review_required: true` and `sent: false`.

Stage 7 reviews both surfaces. ClaimCheck checks every digest assertion against
the full edition and its primary evidence; ProseReview checks concise selection,
duplicate coverage, explanatory wording and runs `shaka scan` on the digest;
LinkChecker verifies its links, including actual rendered anchors. TopicAudit
and ContinuityValueCheck retain their complete-edition checks. Record both file
hashes, the preparation receipt and executed review evidence in the consolidated
review log. Neither a preparation receipt nor a word-count PASS is editorial
approval. Full-edition structure/selection checkers still receive the full
edition, never the shortened digest.

Any full-source edit invalidates the digest binding, even a frontmatter edit.
After refresh, feedback, mention injection or the final `draft: false` change,
reconcile the digest, rebuild, regenerate its receipt and rerun affected reviews
before email handoff. Do not merely replace the hash to silence a stale check.

## Distribution and trial evaluation

PublishingAgent hands off the reviewed prepared digest to the existing email
channel. Verify its bytes against the receipt and current canonical source at
handoff. Preview the actual email, including subject, preheader and links, in
the configured sender. The repository's legacy automatic Buttondown workflow
is disabled; the publication CLI records a manual sent/skipped disposition.
Verify the configured service's delivery mode before the first trial send so
external RSS automation cannot send the full edition instead of the reviewed
digest. Do not silently fall back to sending the full edition
during the trial. A failed digest review remains pending; any decision to skip
email follows the existing explicit sent/skipped disposition, with its reason.
The publisher's existing Buttondown journal confirmation still requires an
actual external send ID or an explicit skip reason. A local digest receipt is
neither. This change grants no new sending or tracking authority.

After four issues, compare reader feedback, useful link clicks and retention
using data already legitimately available. Do not use open rate alone as proof
of reading; privacy mail fetching can distort it. Record which topics readers
follow into full coverage. No new tracking, surveys, reminders, extra mail
streams or automatic extension of the trial are implied. Reassess the format
with the owner after #46.
