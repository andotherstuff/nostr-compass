---
title: "NIP-F4: Podcasts"
date: 2026-06-03
draft: false
categories:
  - NIPs
  - Protocol
  - Media
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
---

NIP-F4 definieert hoe Nostr-clients podcastafleveringen kunnen refereren, weergeven en er sociaal mee kunnen interacteren. Samengevoegd op 2026-05-28 na twee jaar en drie maanden in draft, gebruikt de specificatie kind 54-events voor afleveringen en is deze ontworpen rond de bestaande RSS-podcaststack als aanvullende laag.

## Hoe het werkt

Een kind 54 podcast-aflevering-event bevat een `title`-tag, een optionele `image`-tag, een `description`-tag, één of meer `imeta`-tags voor het audiobestand (URL, mime-type, hash, duur, bitrate, taalcode, fallback-URL's, NIP-96 service-vlag), `t`-onderwerptags en een NIP-31 `alt`-tag voor fallback-weergave.

De dragende ontwerpkeuze is de `i`-tag, die de RSS-GUID van de aflevering meedraagt in het formaat `podcast:item:guid:<guid>`. Dit maakt het volgende mogelijk:

- Een Nostr-client kan een kind 54-event weergeven en het terugkoppelen aan dezelfde aflevering in elke RSS-bewuste podcast-app
- Een RSS-bewuste Nostr-client kan de afleveringen van een bestaande podcast presenteren als kind 54-events zonder dat de podcaster gedwongen wordt om de hosting te migreren
- Cross-protocol comment-threading via de Podcasting 2.0-tags `<podcast:socialInteract>` en `<podcast:chat>`

## Coëxistentie met RSS

Het twee jaar durende debat in de PR-thread (met Podcasting 2.0-medeauteur Dave Jones, Alex Gleason, fiatjaf, Mike Terenzio, Pablo F7z en Jeff Gardner) landde op coëxistentie. Nostr biedt de sociale en discovery-laag, terwijl RSS de bron van waarheid behoudt voor het audiobestand en de feed-metadata. Nostr dupliceert de RSS-distributielaag niet.

Dit contrasteert met eerdere pogingen om RSS te vervangen (JSONFeed, RSS 3.0, propriëtaire podcast-API's). De Podcasting 2.0-namespace ondersteunt al `<podcast:socialInteract>` dat verwijst naar Nostr-events op basis van note-ID, dus een RSS-feed kan de bijbehorende Nostr-discussiethread aangeven zonder dat Nostr de feed zelf hoeft te spiegelen.

## Voorbeeldevent

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["imeta", "url https://podcast.example.com/audio/ep42.mp3", "m audio/mpeg", "x b2e0a7a82ac9f3f3a71f1d9a78c381d5be9d1cf19dce258765c17c8a76287c93", "duration 4523", "bitrate 192000", "l en ISO-639-1"],
    ["i", "podcast:item:guid:9b2a4c7d-1e3f-4a5b-8c9d-0e1f2a3b4c5d"],
    ["t", "podcasting"],
    ["alt", "Podcast episode: Why RSS Won (43 min)"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

## Implementaties

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Speciaal podcastscherm met afleveringenlijst en inline speler (eerste grote client-implementatie, mei 2026)
- [Wavlake](https://wavlake.com) - Grootste Nostr-native muziek- en podcastplatform, verwacht wordt dat het aansluit op kind 54 voor podcastinhoud
- [Fountain](https://fountain.fm) - Bitcoin-podcast-app, verwacht wordt dat het een brug slaat tussen RSS en NIP-F4

## Openstaande vragen

De samengevoegde specificatie laat verschillende ontwerpvragen open zodat implementaties er naartoe kunnen convergeren:

- Pubkeys per creator worden aanbevolen maar niet vereist, zodat platforms zoals Wavlake die veel creators onder één pubkey publiceren geldig blijven
- Comments en discussies per aflevering gebruiken NIP-22 generieke threading en kind 1-timeline-notes in plaats van een speciaal aflevering-comment-kind
- Metadata per podcast (host, netwerk, taal, licentie) leeft ofwel in de kind 0-metadata van de uitgever ofwel in een apart kind 54 podcast-niveau-record

---

**Primaire bronnen:**
- [NIP-F4 Specificatie](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - Oorspronkelijk voorstel, samengevoegd 2026-05-28 na een discussie van twee jaar
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Eerste grote client-implementatie

**Genoemd in:**
- [Newsletter #25: NIP Updates and Deep Dive](/nl/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/nl/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Zie ook:**
- [NIP-22 (Comments)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Alt tags)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (File Metadata)](/nl/topics/nip-94/)
- [NIP-96 (HTTP File Storage)](/nl/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
