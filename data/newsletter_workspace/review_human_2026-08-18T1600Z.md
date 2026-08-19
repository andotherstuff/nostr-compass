# Human feedback — Newsletter #36, 2026-08-18T16:00Z

## Feedback

The owner reported that Nail, a Nostr mail project from the Formstr team, was absent from the
draft, and directed that the discovery pipeline be fixed and the project added:
`https://github.com/formstr-hq/nail`.

This arrived while #36 was still unpublished, so it takes the `/newsletter-fix` path into the
**current** issue rather than the link queue, per the mid-week intake rule.

## Root cause of the miss

`formstr-hq/nail` was invisible to every discovery stream at once:

| Stream | Query | Why it missed |
|---|---|---|
| `github_topic_active` | `topic:nostr pushed:>=2026-08-10` | the repository carries no topics |
| `github_text_new` | `nostr in:name,description created:>=2026-08-10` | created 2026-02-25, outside the creation window |
| explicit-signal gate | `has_explicit_nostr_application_signal` | "Nostr Email Bridge" contains no word in `APPLICATION_SIGNALS` |
| tracked-repository fetch | `data/projects.yml` | Compass tracks repositories; the Formstr owner had five tracked repos and Nail was not one of them |
| NIP-89 / Zapstore | kind 31990 / 32267 | Nail publishes neither a handler descriptor nor a Zapstore listing |

The structural defect is that tracking is per repository, so an actively shipping project from an
already-tracked team has no path into discovery. Fixed in PR
[#136](https://github.com/andotherstuff/nostr-compass/pull/136), which adds an owner sweep over
every distinct GitHub owner in `projects.yml`, an activity-gated text query, and the missing
application nouns, with a regression test named for this repository. Verified live: the sweep
returns Nail and three other untracked Formstr siblings while correctly excluding the three
already-tracked ones.

The Hermes-side procedure was updated in the same pass. `skills/personal/compass-newsletter/SKILL.md`
gains editorial-contract rule 13, requiring Intake to read `github_owner_sibling` rows and route
them to Triage the same week, plus a verification-checklist line.

## Intake and triage of the item itself

- Canonical repository `formstr-hq/nail`, MIT, TypeScript, created 2026-02-25, from the Formstr
  team that also ships `nostr-forms`, `nostr-calendar`, `nostr-polls`, and `nostr-docs`.
- Deployment at `https://mailstr.app` returns HTTP 200 and serves the bridge's own `_smtp` NIP-05
  record resolving to `23024bfdb793b6f3b42658bb98e876a75855c7462d69f3f158a50a2599573c76`.
- Nostr surface verified from source rather than from the README: `client/src/lib/nostr/constants.ts`
  defines kind `1301` mail rumors, kind `1059` gift wraps, kind `10050` DM relay lists, kind `10002`
  relay lists, kind `1985` labels under a `mail` namespace, kind `30078` settings, and a 60,000-byte
  Blossom threshold set against the NIP-44 plaintext cap. `client/src/lib/mail/receive.ts` implements
  the four-state sender-provenance model, and `client/src/lib/api/nip98.ts` authenticates bridge calls.
- In-window activity: [PR #7](https://github.com/formstr-hq/nail/pull/7) "Changes before launch"
  merged 2026-08-18T15:15:20Z across 22 files, and PR #6 on 2026-08-15. GREEN.
- Placement: `messaging_clients` in `data/projects.yml`, matching the category table for encrypted
  chat clients. Section: **Newly Discovered**, as a first-mention project launch.

## Changes applied to the issue

1. `data/projects.yml`: Nail added under `messaging_clients`.
2. `data/npubs.yml`: `Nail` bound to the verified Formstr project key, which the Formstr suite
   already resolves to. No new key was guessed.
3. `content/en/newsletters/2026-08-19-newsletter.md`: new `### Nail brings email onto Nostr as
   gift-wrapped events` subsection leading **Newly Discovered**, one clause added to the opening
   digest, and the frontmatter description updated.
4. `data/newsletter_workspace/sections/*.md` re-synchronized from the assembled draft.
5. Topic backlinks extended to 27 pages, adding NIP-65 and NIP-78 for this issue.

## Gates re-run after the edit

- style PASS, paragraph-links PASS, event-examples PASS, continuity PASS, month-end PASS
- anti-slop scanner PASS, 100/100, zero violations
- production build exit 0; topic-backlink checker PASS at 27/27
- external links: 165 distinct, 165 HTTP 200, including all nine newly added URLs
- `bun run check:npubs`: 325 entries, 0 errors
- `bun scripts/publish.ts --no-inject`: 18 projects resolved, 0 missing, 2 researched-unresolved

GATE: PASS (feedback item verified from primary sources, added to the current issue, root cause fixed in PR #136 with a regression test, and every gate re-run after the edit)
