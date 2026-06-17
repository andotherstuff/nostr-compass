---
title: "NIP-101e: Fitness Workouts"
date: 2026-06-17
draft: false
categories:
  - Fitness
  - Discovery
---

NIP-101e defines a workout-event format so fitness tracking applications can publish, share, and discover training sessions on Nostr. The spec uses kind 1301 events that carry session metrics (distance, duration, elevation, heart rate, calories, cycling cadence, source app) in structured tags so a client can render the workout as a structured card with metrics displayed in their proper units.

## How it works

A NIP-101e workout is a kind 1301 event with structured tags for every metric the source application captured. Common tags include:

- `type` for the workout discipline (run, bike, swim, lift, etc.)
- `distance` with value and unit
- `duration` in seconds
- `elevation_gain` with value and unit
- `start` and `end` timestamps
- `heart_rate` (average and maximum)
- `calories` for energy expenditure
- `source` naming the publishing application
- `t` topic tags for hashtag discovery

The `content` field carries an optional user-authored note (the equivalent of the caption a user would attach to a Strava upload). Clients that recognize kind 1301 render the structured metrics as a workout card; clients that do not fall back to showing the `content` field as a regular note.

## Discovery and feed semantics

NIP-101e events are normal feed events, so a workout posted by a user shows up in their followers' timelines like any other post. Clients with dedicated workout views can subscribe to kind 1301 with author or hashtag filters to build training-log surfaces, leaderboards, or community challenge feeds. The author pubkey is the canonical identity for the workout, so a third-party application reading another user's workouts inherits the same trust assumptions as any other Nostr feed.

## Implementations

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) ships kind 1301 workout rendering with a hero metric, a stats grid, cycling-specific speed display, and source badges ([PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184), refactored in [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226))

---

**Primary sources:**
- [NIP-101e Specification](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - Add NIP-101e fitness workout support (Kind 1301)
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - Redesign workout display with hero metric and stats grid

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
