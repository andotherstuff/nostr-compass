---
title: "NIP-34: Git Collaboration"
date: 2026-02-04
description: "NIP-34 enables decentralized git repository hosting and collaboration through Nostr events."
draft: false
categories:
  - NIP
  - Development
---

NIP-34 defines event kinds for hosting git repositories, patches, and issues on Nostr relays. This enables fully decentralized code collaboration without dependence on centralized hosting platforms like GitHub or GitLab.

## How It Works

Repositories are represented as addressable events (kind 30617) containing metadata like name, description, and clone URLs. The repository owner publishes this event to establish the project on Nostr.

Patches (kind 1617) contain `git format-patch` content that can be applied to a repository. Contributors submit patches as events referencing the target repository. This mirrors the email-based patch workflow used by projects like the Linux kernel.

Issues (kind 1621) function like traditional issue trackers. Pull requests use kinds 1618 and 1619, and status updates use 1630 through 1633. Replies to issues, patches, and pull requests use [NIP-22](/en/topics/nip-22/) comments.

## Event Kinds

- **30617** - Repository announcement (addressable)
- **30618** - Repository state announcement for branches and tags
- **1617** - Patch submission
- **1618** - Pull request
- **1619** - Pull request update
- **1621** - Issue
- **1630-1633** - Open, merged/resolved, closed, and draft status events

## Why It Matters

NIP-34 splits discovery from transport. The actual repository can still live on ordinary Git servers, but Nostr events provide a relay-distributed layer for discovery, discussion, patch exchange, and status tracking. That means a project can keep using git-native tooling without depending on one forge's database or API.

The `r` tag with the earliest unique commit is one of the most important details. It gives clients a way to group mirrors and forks that represent the same underlying repository lineage, which is hard to infer from names alone.

## Implementation Status

- **ngit** - Command-line tool for publishing repos and patches to Nostr
- **gitworkshop.dev** - Web interface for browsing Nostr-hosted repositories
- **Notedeck** - Desktop client with [draft support for NIP-34 viewing](https://github.com/damus-io/notedeck/pull/1279)

---

**Primary sources:**

- [NIP-34 Specification](https://github.com/nostr-protocol/nips/blob/master/34.md)

**Mentioned in:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Notedeck adding NIP-34 viewer
- [Newsletter #9: Notedeck](/en/newsletters/2026-02-11-newsletter/#notedeck)

**See also:**
- [NIP-22: Comments](/en/topics/nip-22/)
