---
title: "NIP-34 (Git Collaboration)"
date: 2026-02-04
description: "NIP-34 enables decentralized git repository hosting and collaboration through Nostr events."
---

NIP-34 defines event kinds for hosting git repositories, patches, and issues on Nostr relays. This enables fully decentralized code collaboration without dependence on centralized hosting platforms like GitHub or GitLab.

## How It Works

Repositories are represented as addressable events (kind 30617) containing metadata like name, description, and clone URLs. The repository owner publishes this event to establish the project on Nostr.

Patches (kind 1617) contain git patch content that can be applied to a repository. Contributors submit patches as events referencing the target repository. This mirrors the email-based patch workflow used by projects like the Linux kernel.

Issues (kind 1621) function like traditional issue trackers. They reference a repository and contain a title and description. Comments on issues and patches use standard reply events.

## Event Kinds

- **30617** - Repository announcement (addressable)
- **1617** - Patch submission
- **1621** - Issue
- **1622** - Issue status (open/closed)

## Implementations

- **ngit** - Command-line tool for publishing repos and patches to Nostr
- **gitworkshop.dev** - Web interface for browsing Nostr-hosted repositories
- **Notedeck** - Desktop client with [draft support for NIP-34 viewing](https://github.com/damus-io/notedeck/pull/1279)

## Primary Sources

- [NIP-34 Specification](https://github.com/nostr-protocol/nips/blob/master/34.md)

## Mentioned In

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Notedeck adding NIP-34 viewer
