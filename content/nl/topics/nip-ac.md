---
title: "NIP-AC: P2P Voice and Video Calls"
date: 2026-04-08
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Messaging
---

NIP-AC stelt een protocol voor peer-to-peer spraak- en videogesprekken over Nostr voor. De specificatie gebruikt Nostr-events voor call signaling (offers, answers, ICE candidates) en WebRTC voor het daadwerkelijke mediatransport, zodat de gespreksopzet gedecentraliseerd blijft terwijl standaard browser-API's voor audio en video worden gebruikt.

## Hoe Het Werkt

Een beller publiceert een call offer-event met een WebRTC Session Description Protocol (SDP) offer, getagd met de pubkey van de ontvanger. De ontvanger antwoordt met een SDP answer-event. Beide partijen wisselen ICE candidate-events uit om het netwerkpad te onderhandelen. Zodra de WebRTC-verbinding is opgezet, stroomt de media direct tussen peers zonder relay-betrokkenheid.

De signaling-events zijn encrypted, zodat relays niet kunnen zien wie wie belt. De call state machine verwerkt offer-, answer-, reject-, busy- en hangup-overgangen.

## Implementaties

- [Amethyst](https://github.com/vitorpamplona/amethyst) bouwt NIP-AC-ondersteuning met een testsuite voor de call state machine en afhandeling van verouderde call offers.

---

**Primaire bronnen:**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - P2P Voice and Video Calls over WebRTC

**Vermeld in:**
- [Nostr Compass #17 (2026-04-08)](/nl/newsletters/2026-04-08-newsletter/)

**Zie ook:**
- [NIP-44 (Encrypted Payloads)](/nl/topics/nip-44/)
