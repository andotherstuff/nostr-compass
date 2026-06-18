---
title: "NIP-82: Software Applications"
date: 2026-06-17
draft: false
categories:
  - Discovery
  - Apps
---

NIP-82 defines a software-application event so Nostr clients can render applications (Android APKs, iOS apps, web apps, desktop binaries) as first-class objects in feeds and discovery surfaces. The spec replaces the older approach of describing apps through generic kind 1 notes or [NIP-89](/en/topics/nip-89/) handler recommendations with a dedicated, structured event that carries application metadata, screenshots, repository links, and author identity.

## How it works

A NIP-82 software application is a single replaceable event addressed by author pubkey and `d` tag. The event carries:

- `name`, `description`, `icon`, `image` tags for display
- `repository` and `web` tags for source and homepage URLs
- `platforms` tag enumerating supported targets (android, ios, web, linux, macos, windows)
- `download` tags for each platform-specific binary or web URL
- `screenshots` tags carrying image URLs for the application screenshots
- `t` topic tags for categorization
- `version` tag for the current published version

A client browsing a NIP-82 feed can show the application card, link to the canonical repository, and surface screenshots without falling back to scraping a Nostr long-form post or a third-party app store. The author pubkey is the source of truth for the application, so a client can verify the publisher matches the expected developer identity before promoting a download link.

## Feed semantics

NIP-82 events are addressable, so each application has one canonical replaceable event per author. A developer publishing a new version replaces the previous event in place, and subscribers see the update without managing event history. Clients that want a change log can subscribe to the addressable event and render version bumps as activity on the application surface.

The spec composes with [NIP-89](/en/topics/nip-89/) (Application Handlers): a NIP-82 event describes the application as an artifact, while a NIP-89 event describes that the application can handle specific event kinds. Clients can use one without the other, but the pair gives a discovery surface (NIP-82) and a delegation surface (NIP-89) that work together.

## Implementations

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) ships a dedicated NIP-82 software-applications feed with a detail screen, author info, and screenshots ([PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036), [PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078), [PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200))

---

**Primary sources:**
- [NIP-82 Specification](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - Add NIP-82 Software Applications support with dedicated feed
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - Add dedicated NIP-82 software app detail screen
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - Improve NIP-82 software app UI with author info and screenshots

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**See also:**
- [NIP-89: Application Handlers](/en/topics/nip-89/)
