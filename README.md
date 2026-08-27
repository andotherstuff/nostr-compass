# Nostr Compass

Technical resource for the Nostr protocol. A weekly newsletter covering NIP
proposals, client updates, relay developments, and notable code changes; a
weekly podcast with the developers whose work each issue covers; and a topic
index documenting protocol concepts with links to primary sources.

Published at [nostrcompass.org](https://nostrcompass.org) in ten languages, and
to Nostr as a NIP-23 long-form article. All materials MIT licensed.

## Repository layout

```
content/<lang>/       Hugo content. en is authoritative; the other nine are translations.
  newsletters/        One file per issue, YYYY-MM-DD-newsletter.md
  topics/             Topic and NIP reference pages
data/
  projects.yml        Tracked projects: repo, website, category, npub
  npubs.yml           Verified Nostr identities and their roles
  nip34_tracked.yml   NIP-34 repositories whose subject matter is Nostr
  newsletter_workspace/  Per-issue editorial record (triage, reviews, publication logs)
  <fetcher>/          Fetcher output, regenerated weekly and gitignored
publish/              Publication pipeline (Bun/TypeScript). Signs and broadcasts to Nostr.
scripts/              Discovery fetchers, editorial gates, translation, build
skills/_COMPASS/      Agent definitions for the weekly editorial workflow
tests/                Python tests for scripts/
layouts/ assets/ i18n/ static/   Hugo theme
```

`CLAUDE.md` holds the editorial rules every issue must satisfy. `AGENTS.md`
describes the weekly workflow stages. `STRATEGY.md` covers direction and
audience.

## Development

```bash
bun install
bun run build            # full build including Pagefind search index, output in public/
hugo server              # live reload at localhost:1313, no search index
docker-compose up        # same, containerised
```

`bun run build` reserves two CPU cores for headroom. Override with
`BUILD_HEADROOM_CORES=<n>`, or cap directly with `BUILD_MAX_CORES=<n>`.

## Tests

```bash
python3 -m unittest discover -s tests    # scripts/
bun test                                 # publish/ and scripts/*.test.ts
```

## Weekly workflow

**Discover.** `scripts/fetch_all.sh` runs every fetcher: tracked-repository
releases and merged PRs, NIP discussions, NIP-34 repositories, Zapstore
listings, NIP-89 application handlers, and a GitHub sweep for projects Compass
does not track yet. It finishes by writing
`data/newsletter_workspace/release_digest_<date>.md`, which names every release
in the window so a release cannot exist in the data and in no editorial
artifact.

Cross-run discovery baselines live under `$COMPASS_STATE_DIR` (default
`/opt/data/compass-state`), deliberately outside the repository. Each issue is
drafted in its own worktree, and a baseline stored inside a fresh worktree
starts empty, which makes every project look new and suppresses real signal.
Run `scripts/migrate_discovery_state.py` after adding a worktree or moving that
state.

**Triage and select.** Every release in the digest needs a written-up-or-skipped
decision recorded in `data/newsletter_workspace/`. A project may be omitted only
when the previous issue already covered it *and* it shipped nothing substantive;
the digest computes that as `suppression_allowed`. This gate blocks:

```bash
python3 scripts/check_triage_coverage.py \
  --digest data/project_updates/release_digest_<date>.json \
  --triage data/newsletter_workspace/triage_<date>.md
```

**Write and check.** Draft into `content/en/newsletters/<date>-newsletter.md`.
The blocking gates:

```bash
python3 scripts/check_newsletter_style.py <file>            # filler, opaque advisory anchors
python3 scripts/check_newsletter_continuity.py <file>       # back-references resolve
python3 scripts/check_newsletter_paragraph_links.py <file>  # every claim is sourced
python3 scripts/check_newsletter_event_examples.py <file>   # example events are valid
python3 scripts/check_topic_backlinks.py                    # topic pages link the issue
python3 scripts/check_month_end_history.py <file>           # month-end retrospective rules
bun run check:npubs                                         # identities and roles
```

**Publish.** One command runs parse, sign, announce-sign, broadcast, merge, and
log:

```bash
bun publish/publish.ts <issue> --stage all --really-broadcast --really-merge
```

Broadcast and merge belong together: broadcasting alone leaves the issue live on
Nostr and absent from the website. The `log` stage derives
`data/newsletter_workspace/publish_log_<date>.md` from the run's own receipts,
the matched Pages deploy, and a fresh relay readback, then opens a PR for it.
See `publish/README.md` for stages and configuration, and `publish/BUNKER.md`
for the NIP-46 remote-signing session.

Signing keys are never in this repository. The pipeline holds a NIP-46 session
against an external signer; the bunker URI and client key live in
`~/.config/compass-publish/`.

**Translate.** After publication, into all nine other languages:

```bash
bash scripts/translate.sh next                 # oldest published issue still untranslated
bash scripts/translate.sh commit <lang> <date> # checkpoint one language
bash scripts/translate.sh ship <date>          # push, open PR, merge on green
```

Cross-newsletter back-references inside a translation keep their `/en/` path,
because their anchors are English heading slugs.

## Contributing

See the [contributing guidelines](CONTRIBUTING.md). Newsletter PRs are kept to
exactly one commit; update one by squashing and force-pushing with
`--force-with-lease`.

If you build on Nostr and would like to contribute or appear on the podcast,
reach out via NIP-17 DM to
`npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`.

## Deployment

GitHub Actions builds and deploys to GitHub Pages on every push. Custom domain
`nostrcompass.org`; DNS A records point at the GitHub Pages addresses
(185.199.108-111.153). Repository settings: Pages source "GitHub Actions", and
`github-pages` environment deployment branches set to "All branches".

## License

MIT.
