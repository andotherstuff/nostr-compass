---
title: "NIP-34: Git Collaboration"
date: 2026-02-04
description: "NIP-34 enables decentralized git repository hosting and collaboration through Nostr events: repos, patches, pull requests, issues, and status."
draft: false
categories:
  - NIP
  - Development
---

NIP-34 defines event kinds for hosting git repositories, patches, pull requests, issues, and merge status on Nostr relays. It enables fully decentralized code collaboration without dependence on centralized hosting platforms like GitHub or GitLab, while still allowing the underlying repository to be served from any git server. The result is a Nostr-distributed coordination layer that sits on top of the existing git protocol, so projects keep their git-native tooling but stop depending on one forge's database, API, or moderation policy.

## How It Works

A repository is announced as a kind `30617` addressable event. The `d` tag is a kebab-case identifier (typically the project name), and the event includes human-readable `name` and `description` tags, one or more `clone` URLs, optional `web` URLs for browsing, a `relays` tag listing the relays the maintainer monitors for patches and issues, and a `maintainers` tag with additional pubkeys allowed to manage the project. The `r` tag annotated with the `euc` ("earliest unique commit") marker carries the commit ID of the first commit unique to this repository, which lets clients group mirrors and forks of the same project across different hosts. Optional hashtags via `t` and a `personal-fork` `t` tag let an author publish a fork without claiming maintainer status.

The canonical ngit repository announcement looks like this:

```json
{
  "id": "08bb929a05fd9bbb5e1b227a3850269f2f9615e9e830bd34e664b72df14dead6",
  "pubkey": "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd",
  "created_at": 1758124128,
  "kind": 30617,
  "tags": [
    ["d", "ngit"],
    ["r", "26689f97810fc656c7134c76e2a37d33b2e40ce7", "euc"],
    ["name", "ngit"],
    ["description", "cli and git plugin for code collaboration over nostr"],
    ["clone", "https://codeberg.org/DanConwayDev/ngit-cli.git", "https://relay.ngit.dev/npub15qydau2hjma6ngxkl2cyar74wzyjshvl65za5k5rl69264ar2exs5cyejr/ngit.git"],
    ["web", "https://gitworkshop.dev/danconwaydev.com/ngit"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol", "wss://relay.nostr.band"],
    ["maintainers", "a008def15796fba9a0d6fab04e8fd57089285d9fd505da5a83fe8aad57a3564d", "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd"],
    ["alt", "git repository: ngit"]
  ],
  "content": "",
  "sig": "ad571d2ec44fcdb5d684281deb8aea3862b6660d73e66f1c921f381f2fec6869f4b9444414b4ffdafccd414f3489502af193401b35edcebd8f50dcebbbc0b37a"
}
```

Patches use kind `1617` and carry the output of `git format-patch` in the `content` field. Each patch references the target repository through an `a` tag of the form `30617:<maintainer-pubkey>:<d-tag>`. Patch series use a `t` tag of `root` for the cover letter and chain follow-ups with [NIP-10](/en/topics/nip-10/) `e` reply tags. For maintainers who want stable commit IDs after applying a patch, the patch can include `commit`, `parent-commit`, `committer`, and `commit-pgp-sig` tags so the resulting commit hash matches the proposer's machine. The 60 KB rule of thumb is the dividing line: anything below that limit ships as a patch event, while larger changesets go out as pull requests with a separate branch tip.

Pull requests use kind `1618` and carry markdown text in the content body. A PR points to a branch tip with a `c` tag (current commit ID), a `clone` tag listing where the commit can be fetched, an optional `branch-name` suggestion, and an optional `merge-base` tag for the most recent common ancestor with the target branch. Before signing the PR event, clients SHOULD push the branch tip to `refs/nostr/<event-id>` on every clone URL the user can write to, including any GRASP server identified by the `clone`/`relays` tag pattern. If the user lacks write access to the listed clone URLs, the client MAY publish a `personal-fork` repository announcement that lists alternative GRASP servers (such as those in the user's GRASP list) and pushes there instead. Updates to the branch tip are published as kind `1619` PR Update events that reference the original PR through capital-letter `E` and `P` tags, matching [NIP-22](/en/topics/nip-22/) reply conventions.

Issues use kind `1621` with markdown content and an optional `subject` tag for display. Replies to any NIP-34 thread (issues, patches, and pull requests alike) follow standard [NIP-22](/en/topics/nip-22/) comment threading. Status events let the issue/patch author or a maintainer move a thread between Open (`1630`), Applied/Merged or Resolved (`1631`), Closed (`1632`), and Draft (`1633`). The most recent valid status event by `created_at` wins. When a `1631` is published, the maintainer can include `merge-commit` with the resulting commit ID and `applied-as-commits` listing every commit that landed in the target branch, plus `q` tags for each accepted patch revision. That payload gives clients enough information to display merge state without an external API call: the patch is checked off, the merge commit is linkable, and downstream tooling can verify the commits in any clone of the repository.

A separate kind `30618` Repository State announcement is an optional canonical pointer to current branch and tag heads. Each `refs/heads/<branch>` or `refs/tags/<tag>` tag carries the corresponding commit ID, and a `HEAD` tag indicates the default branch. The state event is what lets a NIP-34 web client render an accurate "default branch" view without polling every clone URL.

## Discovery and the `nostr://` Clone URL

NIP-34 also defines a `nostr://` URL scheme that works with `git clone` when a `git-remote-nostr` helper is installed. Three forms are supported: `nostr://<naddr>` for a direct addressable event reference, `nostr://<npub|nip05>/<identifier>` for a human-readable repository reference, and `nostr://<npub|nip05>/<relay-hint>/<identifier>` when the client needs a relay hint to locate the repository announcement. Both the relay hint and identifier are percent-encoded per RFC 3986 §2.1. The format was merged in [PR #2312](https://github.com/nostr-protocol/nips/pull/2312) and is implemented by `git-remote-nostr`, [Shakespeare](https://shakespeare.diy), [GitWorkshop](https://gitworkshop.dev), and NostrHub.io. The wider effect is that you can paste a `nostr://` URL into any NIP-34-aware tool and resolve a repository without first knowing which relay or which forge holds the canonical copy.

A separate kind `10317` "User GRASP list" lets users advertise the GRASP servers they prefer for NIP-34 work, similar in shape to a [NIP-65](/en/topics/nip-65/) relay list or a [NIP-B7](https://github.com/hzrd149/blossom) Blossom server list. The event has zero or more `g` tags with GRASP service WebSocket URLs in preference order. Clients use this list as fallback hosting when a PR author lacks write access to the original clone URLs, so the PR's branch tip can still be pushed somewhere both parties can fetch.

NIP-34 follow lists, merged in [PR #2130](https://github.com/nostr-protocol/nips/pull/2130), reuse [NIP-51](/en/topics/nip-51/) follow sets (kind `30000`) with `d` tag values like `git-repos` or `git-issues`. Each follow set lists `a` tag references to the repositories or issue trackers a user wants in their feed, so a NIP-34 client can render a "watching" view that mirrors the contact-list mechanics of kind `3` follow lists for users.

## Event Kinds

- **30617** - Repository announcement (addressable)
- **30618** - Repository state (current branch and tag heads)
- **1617** - Patch
- **1618** - Pull request
- **1619** - Pull request update
- **1621** - Issue
- **1630** - Status: Open
- **1631** - Status: Applied / Merged / Resolved
- **1632** - Status: Closed
- **1633** - Status: Draft
- **10317** - User GRASP list (preferred GRASP servers)

## Discovery Independent of Hosting

NIP-34 splits discovery from transport. The repository data can still live on ordinary git servers, while Nostr events provide a relay-distributed layer for discovery, discussion, patch exchange, and status tracking. A project keeps using git-native tooling and stays portable across forges. The `r euc` tag is the structural piece that makes cross-mirror identification work: clients identify the same project on different hosts even when names diverge, which is something GitHub itself does not do. Combined with the `nostr://` URL scheme, the user GRASP list, and PR fallback to a personal-fork announcement, NIP-34 produces a forge layer where any participant can host, fork, or contribute without first asking permission from a central platform.

## Implementations

- [ngit](https://codeberg.org/DanConwayDev/ngit-cli) is DanConwayDev's command-line tool and `git` plugin for publishing repository announcements, patches, and PRs as Nostr events. It ships the `git-remote-nostr` helper that resolves `nostr://` URLs and implements the GRASP-server detection logic for PR submissions. Newsletter [#20](/en/newsletters/2026-04-29-newsletter/#ngit-v242-fixes-grasp-server-detection-for-pr-submissions) covered v2.4.2, which fixed GRASP server detection for PR submissions and improved clone behavior when an open PR's git data is unavailable on the listed servers.
- [GitWorkshop](https://gitworkshop.dev) is DanConwayDev's web client for browsing NIP-34 repositories, reviewing PRs, managing issues, and tracking maintainer status updates. Newsletter [#20](/en/newsletters/2026-04-29-newsletter/#gitworkshop-ships-in-browser-pr-merge-repository-following-and-a-bandwidth-efficient-git-explorer) covered the v2 release, which added in-browser PR merge for repositories using GRASP relays, repository following built on reactions and kind `10617` pinned-repository sets, a bandwidth-efficient git explorer that uses the underlying GRASP git protocol, and improved cross-relay discovery powered by [NIP-50](/en/topics/nip-50/) search and an `ngit-indexer` relay implementation.
- [ngit-indexer](https://gitworkshop.dev/ngit-indexer/ngit-indexer) is DanConwayDev's relay implementation that discovers and syncs repository announcements across the Nostr network. It is what makes cross-relay search practical: a single client query against an `ngit-indexer` instance returns repositories that were originally announced on many different relays, without the client having to fan out queries.
- [Pika](https://github.com/sledtools/pika) is a Marmot-based encrypted messenger that also ships a self-hosted NIP-34 forge with pre-merge CI. The forge runs lane-based CI per code path (Rust, TypeScript, Apple builds run independently), reports structured CI metadata as Nostr events with live status badges, isolates managed CI agents in Incus OpenClaw containers, and exposes a `ph forge` CLI for command-line interaction. Newsletter [#15](/en/newsletters/2026-03-25-newsletter/#pika-builds-a-nip-34-forge-ci-pipeline) covered this as one of the first working CI/CD systems built on top of NIP-34.
- [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit) is the Budabit community's fork of Flotilla that polishes the NIP-34 repo surface for community contributors. The fork stays close to upstream Flotilla and prioritizes the repo view, with recent fixes covering discussion controls, sticky repo tabs on detail pages, GRASP-relay-aware repo announcements, and maintainer-applied patch status sync. Covered in newsletter [#19](/en/newsletters/2026-04-22-newsletter/#flotilla-budabit-polishes-its-nip-34-repo-surface).
- [Gittr](https://gittr.space) is a web-based decentralized git platform that combines NIP-34 with zaps, bounties, SSH key authentication, and code review. The companion [gittr-helper-tools](https://github.com/arbadacarbaYK/gittr-helper-tools) repository publishes production code snippets covering file fetching, URL normalization, GRASP detection, [NIP-46](/en/topics/nip-46/) signer integration, and [NIP-C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) code snippets, which makes Gittr useful as a reference for building new NIP-34 clients.
- [gitstr](https://github.com/fiatjaf/gitstr) is fiatjaf's CLI for sending and receiving git patches over Nostr using NIP-34. It predates ngit and overlaps with it but stays minimal: a small Go binary that emits and consumes patch events without taking on the full forge surface that ngit and GitWorkshop cover.
- [nostr-git](https://github.com/chebizarro/nostr-git) is chebizarro's component and utility library for integrating git and Nostr, with [nostr-git-ui](https://relay.ngit.dev/npub1hw6amg8p24ne08c9gdq8hhpqx0t0pwanpae9z25crn7m9uy7yarse465gr/nostr-git-ui.git) shipping Svelte UI components for the same package. Together they give downstream projects a typed, reusable surface for repository announcements, patches, issues, and status events without rewriting the event handling each time.
- [GitCitadel](https://gitworkshop.dev/r/naddr1qq9rzd35vsckxv3kx5cnydpsve3rgvphxgmnwvphxccnsxe5xy6nzxesxccrjxqkqz9rhwden5te0wfjkccte9ehx7um5wghxyctwvshszxnhwden5te0dehhxarj9emkjmn99uqzpa5sthgerredupzj42jtnwgg3nyac6lagssx8zy4wugxjs8ajf7p) is the team behind GitWorkshop and the broader ngit toolchain. Their kind `30617` repository serves as an abstract collection point for project-wide documentation, design discussions, and cross-repo metadata that does not belong to any single tool.
- [Notedeck](https://github.com/damus-io/notedeck) is the Damus team's cross-platform desktop client. The team published [PR #1279](https://github.com/damus-io/notedeck/pull/1279) as a draft NIP-34 viewer (now closed) and [PR #1289](https://github.com/damus-io/notedeck/pull/1289) is the open implementation plan for a full Git App. Adoption inside Notedeck would put NIP-34 browsing into a Damus-affiliated desktop client and on top of the `nostrdb` storage layer that Damus and Notedeck share.
- **schemata** is the Nostrability project's collection of JSON schemas for validating NIP-compliant events, published as a NIP-34 repository under d-tag `schemata` by the Nostrability maintainer pubkey. The repo currently sees regular issue traffic on `relay.ngit.dev`, and the team uses NIP-34 as the working surface for protocol-conformance discussions. Companion language packages (schemata-rs, schemata-swift, schemata-go) ship the schemas as platform-native libraries for downstream client integration.
- [Shakespeare](https://shakespeare.diy) is the editor and one-click app builder that adopted the `nostr://` clone URL scheme early. It is the canonical example of a tool that imports a NIP-34 repository directly via the URL scheme without requiring a separate "Nostr import" step.

## Relays

`wss://relay.ngit.dev` is the primary relay for NIP-34 traffic and the default relay used by ngit, GitWorkshop, and most NIP-34 clients. Several GRASP servers also host repositories and serve as the `clone` URL target for `nostr://` references. The user GRASP list (kind `10317`) lets users declare which servers they trust, both as a discovery aid and as the fallback target when a PR author needs to push a branch they cannot push to the original clone URL. Long-term, the GRASP server tier is what makes NIP-34 forking permissionless: anyone can host a fork, the fork is announced as a Nostr event, and the PR mechanics still work even if the base repository's maintainer never set up an account on the same server.

---

**Primary sources:**

- [NIP-34 Specification](https://github.com/nostr-protocol/nips/blob/master/34.md)
- [PR #997 (original NIP-34 merge, March 2024)](https://github.com/nostr-protocol/nips/pull/997) - over 130 comments and 44 days of discussion
- [PR #2130 (git-related follow lists)](https://github.com/nostr-protocol/nips/pull/2130) - kind `30000` follow sets with `git-repos` and `git-issues` `d` tags
- [PR #2312 (`nostr://` clone URL scheme)](https://github.com/nostr-protocol/nips/pull/2312) - three URL forms, RFC 3986 percent-encoding, `d` tag tightening

**Mentioned in:**

- [Newsletter #8 (2026-02-04): Notedeck adds NIP-34 viewer](/en/newsletters/2026-02-04-newsletter/#notedeck)
- [Newsletter #9 (2026-02-11): Notedeck Ships Dashboard and Agentium](/en/newsletters/2026-02-11-newsletter/#notedeck-ships-dashboard-and-agentium)
- [Newsletter #15 (2026-03-25): Pika builds a NIP-34 forge CI pipeline](/en/newsletters/2026-03-25-newsletter/#pika-builds-a-nip-34-forge-ci-pipeline)
- [Newsletter #15 (2026-03-25): March 2024: Protocol Maturation (NIP-34 merge history)](/en/newsletters/2026-03-25-newsletter/#march-2024-protocol-maturation)
- [Newsletter #17 (2026-04-08): NIP Updates (git-related follow lists)](/en/newsletters/2026-04-08-newsletter/#nip-updates)
- [Newsletter #18 (2026-04-15): NIP Updates (`nostr://` clone URLs)](/en/newsletters/2026-04-15-newsletter/#nip-updates)
- [Newsletter #19 (2026-04-22): flotilla-budabit polishes its NIP-34 repo surface](/en/newsletters/2026-04-22-newsletter/#flotilla-budabit-polishes-its-nip-34-repo-surface)
- [Newsletter #20 (2026-04-29): GitWorkshop ships in-browser PR merge](/en/newsletters/2026-04-29-newsletter/#gitworkshop-ships-in-browser-pr-merge-repository-following-and-a-bandwidth-efficient-git-explorer)
- [Newsletter #20 (2026-04-29): ngit v2.4.2 fixes GRASP server detection](/en/newsletters/2026-04-29-newsletter/#ngit-v242-fixes-grasp-server-detection-for-pr-submissions)
- [Newsletter #20 (2026-04-29): Six Nostr Aprils (April 2024 git-over-Nostr milestones)](/en/newsletters/2026-04-29-newsletter/#april-2024-private-messaging-git-over-nostr-and-maintainer-support)
- [Newsletter #20 (2026-04-29): April 2026: NIP-34 hardening, badges, and adoption-focused grants](/en/newsletters/2026-04-29-newsletter/#april-2026-nip-34-hardening-badges-and-adoption-focused-grants)
- [Newsletter #31 (2026-07-15): GitWorkshop v3.0.3 fixes newly announced refs in the repo explorer](/en/newsletters/2026-07-15-newsletter/#gitworkshop-v303-fixes-newly-announced-refs-in-the-repo-explorer)
- [Newsletter #32 (2026-07-22): Armada and nak add NIP-34 workspace and CLI support](/en/newsletters/2026-07-22-newsletter/#armada-v0370-opens-buzz-workspaces-from-a-second-client)

**See also:**

- [NIP-10: Text Notes and Threads](/en/topics/nip-10/)
- [NIP-19: bech32-encoded entities](/en/topics/nip-19/)
- [NIP-22: Comments](/en/topics/nip-22/)
- [NIP-50: Search Capability](/en/topics/nip-50/)
- [NIP-51: Lists](/en/topics/nip-51/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
