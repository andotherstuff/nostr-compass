# Nostr Compass Strategy

Guide for contributors on populating and maintaining the Nostr Compass archive.

## Mission

Keep developers, relay operators, and builders informed about important Nostr ecosystem developments. Document protocol evolution with technical accuracy, neutrality, and academic rigor.

## Newsletter

**Schedule**: Weekly, Wednesdays at 16:00 UTC. Sequential numbering (#1, #2, #3...).

**Policy**: Publish on schedule even without full review. Corrections noted in subsequent editions. Consistency over perfection.

**Length**: As long as needed, as short as possible. No fluff.

### Sections

1. **News & Updates** - Notable events and announcements.

2. **NIP Updates** - New proposals, status changes (draft → proposed → final), significant revisions, rejected NIPs with explanation of what failed and why.

3. **Releases** - Clients, relay software, libraries, signing tools, other tooling. Web clients ship frequent small updates; cover notable changes without formal releases. Release candidates and merged-but-unreleased PRs included when early feedback is valuable.

4. **Developer Best Practices** - Security and implementation guidance: key handling, NIP-07 integration, relay privacy, event validation, spam prevention. Mix of recurring tips and one-time explainers.

5. **NIP Deep Dive** - 1-2 NIPs explained per issue. Covers: problem solved, how it works, client/relay support, links to spec and implementations. No code examples unless essential.

6. **This Month in Nostr History** (monthly) - Events from this month in previous years. Key moments: early experiments (2020), NIP-01 and first relays (2021), Damus launch and Jack's first note (2022), zaps and client explosion (2023), protocol debates, milestones. Sources: Wayback Machine, old GitHub issues, Twitter/X archives, fiatjaf's blog, repo archaeology.

7. **Other** (as needed) - Relay economics, spam prevention approaches, notable discussions.

### Style

Technical, neutral, academic. Handle controversies with good faith and charitable interpretation. Present multiple perspectives without taking sides. Link to topic pages for concepts, directly to source for PRs/releases. Include diagrams when helpful; avoid screenshots.

### What's Notable?

Cover changes that affect users, interoperability, or protocol direction. Skip minor refactors, dependency bumps, and typo fixes. When uncertain, include it briefly rather than omit entirely.

### Newsletter #1

Special edition: introduction to Nostr for newcomers plus establishing the weekly format. Launch publicly from issue #1.

## Topics Index

High-level documentation of Nostr concepts. One topic can cover multiple NIPs or kinds.

**Each topic includes**: explanation, relevant NIPs, implementations, newsletter coverage (compass_mentions), see-also links.

**Categories**: Clients, Content Types, Cryptography, Data Storage, Developer Tools, Identity, Key Management, Messaging, Moderation, NIPs, Privacy, Protocol, Relay Software, Security, Social Features.

**Naming**: Introduce formally ("NIP-57: Lightning Zaps"), then use common names ("Zaps").

**Historical backfill**: Populate topics with 2021-2024 content. No fake-dated newsletters. "This Month in History" section provides dated references; topic pages link to primary sources.

## Kind Registry

Separate page: kind number, description, relevant NIP(s), topic page links.

## NIP Reference

Separate reference page listing all NIPs (distinct from newsletter NIP Deep Dives which explain NIPs in depth). Each entry: NIP number/title, status (draft/proposed/final/rejected), one-line description, spec link, topic page links.

## Compatibility Matrix

Shows which clients support which NIPs to encourage interoperability.

**Structure**: Rows = clients (grouped by category, not platform). Columns = NIPs.

**Data**: Self-reported by developers, reviewed before merge, quarterly freshness check.

## Project Tracking

**Inclusion**: FOSS, identifiable maintainer, active contributions.

**Entry format**: Name, category, description, maintainer(s), repo link, npub, website.

**Categories & Initial List**:

| Category | Projects |
|----------|----------|
| Social Clients | Damus, Primal, Amethyst, Coracle, Snort, Nostrudel, Iris |
| Long-form / Blogging | Habla, Yakihonne |
| Messaging | 0xchat, White Noise |
| Media / Streaming | Zap.stream, Wavlake |
| Marketplaces | Shopstr, Plebeian Market, Mostro |
| Developer Tools | ngit, Gitworkshop, Zapstore |
| Signing / Key Management | Amber, Alby, Nowser, Aegis |
| Relay Implementations | strfry, nostr-rs-relay, nostream |
| Libraries / SDKs | nostr-tools, rust-nostr, nostr-sdk, Applesauce |
| Other | DVMs / AI agents |

*List requires research and expansion.*

## Podcast

Weekly, published Fridays (after newsletter gives readers time to read first).

**Distribution**: Fountain, direct link on Nostr, possibly YouTube.

**Format**: Newsletter recap → guest contributors present topics with deeper insight → Q&A → hosts cover remaining topics.

Regular hosts for continuity; guests rotate based on content.

## Contributors

**Coordination**: Signal group for contributors.

**Roles**: Technical writers, researchers (track repos/releases), translators (Spanish, Japanese, German, Portuguese), podcast hosts, reviewers (optional but encouraged).

Reading PR descriptions is sufficient; deep code review optional. Explore translation automation with human review.

**Recruitment**: Nostr outreach, manual outreach to known contributors.

**Incentives**: Grant funding.

**Review process**: PRs to nostr-compass repo. Maintainers have merge rights.

## Research Checklist

Weekly tracking:

**NIPs**
- [ ] New proposals
- [ ] Status changes
- [ ] Revisions and discussions

**Clients**
- [ ] Damus
- [ ] Primal
- [ ] Amethyst
- [ ] Coracle
- [ ] Snort
- [ ] Nostrudel
- [ ] Iris
- [ ] Habla
- [ ] Yakihonne
- [ ] 0xchat
- [ ] White Noise
- [ ] Zap.stream
- [ ] Wavlake

**Relay Software**
- [ ] strfry
- [ ] nostr-rs-relay
- [ ] nostream

**Libraries / SDKs**
- [ ] nostr-tools
- [ ] rust-nostr
- [ ] nostr-sdk
- [ ] Applesauce

**Signing / Key Management**
- [ ] Amber
- [ ] Alby
- [ ] Nowser
- [ ] Aegis

**Developer Tools**
- [ ] Zapstore
- [ ] ngit
- [ ] Gitworkshop

**Marketplaces**
- [ ] Shopstr
- [ ] Plebeian Market
- [ ] Mostro

**Other**
- [ ] Notable discussions
- [ ] Developer announcements
- [ ] Security disclosures

## Style Guide

**Tone**: Technical, precise, neutral, accessible to newcomers, no hype, charitable interpretation.

**Format**: Markdown, headers for sections, bullet points, bold sparingly, liberal linking.

**Attribution**: Credit sources, link originals, name maintainers.

**Corrections**: Note in subsequent newsletter, update topic pages directly, be transparent.

## Languages

English primary. Translations based on contributor availability: Spanish, Japanese, German, Portuguese.

## Success Metrics

- Developers cite Nostr Compass when explaining protocol decisions
- NIP authors reference our coverage in PR descriptions and discussions
- New developers understand Nostr evolution from archive
- Coverage seen as fair by all sides of debates

## Open Questions

- Compatibility matrix columns: NIPs vs features vs kinds
- Priority order for historical topic backfill
- Translation automation opportunities

## Getting Started

1. Review this document
2. Check research checklist
3. Draft content following style guide
4. Submit PR
5. Iterate on feedback

Contact: info@nostrcompass.org
