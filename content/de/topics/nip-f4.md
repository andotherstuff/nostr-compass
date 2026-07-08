---
title: "NIP-F4: Podcasts"
date: 2026-06-03
draft: false
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4 definiert, wie Nostr-Clients Podcast-Episoden referenzieren, präsentieren und sozial mit ihnen interagieren. Nach zwei Jahren und drei Monaten im Entwurfsstadium am 2026-05-28 gemergt, verwendet die Spezifikation kind 54-events für Episoden und ist um den bestehenden RSS-Podcasting-Stack als ergänzende Schicht herum konzipiert.

## Wie es funktioniert

Ein kind 54-Podcast-Episoden-event trägt einen `title`-tag, einen optionalen `image`-tag, einen `description`-tag, einen oder mehrere `imeta`-tags für die Audiodatei (URL, MIME-Typ, Hash, Dauer, Bitrate, Sprachcode, Fallback-URLs, NIP-96-Dienst-Flag), `t`-Themen-tags und einen NIP-31-`alt`-tag für die Fallback-Anzeige.

Die tragende Designentscheidung ist der `i`-tag, der die RSS-GUID der Episode im Format `podcast:item:guid:<guid>` trägt. Dies ermöglicht:

- Einem Nostr-Client, ein kind 54-event anzuzeigen und es mit derselben Episode in jeder RSS-fähigen Podcast-App zu verknüpfen
- Einem RSS-fähigen Nostr-Client, Episoden eines bestehenden Podcasts als kind 54-events zu präsentieren, ohne den Podcaster zum Wechsel des Hostings zu zwingen
- Protokollübergreifende Kommentar-Threading über die Podcasting 2.0-tags `<podcast:socialInteract>` und `<podcast:chat>`

## Koexistenz mit RSS

Die zweijährige Debatte im PR-Thread (mit Podcasting 2.0-Co-Autor Dave Jones, Alex Gleason, fiatjaf, Mike Terenzio, Pablo F7z und Jeff Gardner) einigte sich auf Koexistenz. Nostr liefert die soziale und Discovery-Schicht, während RSS die Wahrheitsquelle für die Audiodatei und die Feed-Metadaten behält. Nostr dupliziert die RSS-Verteilungsschicht nicht.

Dies steht im Gegensatz zu früheren Versuchen, RSS zu ersetzen (JSONFeed, RSS 3.0, proprietäre Podcast-APIs). Der Podcasting 2.0-Namespace unterstützt bereits `<podcast:socialInteract>`, das Nostr-events per Notiz-ID referenziert, sodass ein RSS-Feed seinen begleitenden Nostr-Diskussionsthread deklarieren kann, ohne dass Nostr den Feed selbst spiegeln muss.

## Beispiel-Event

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

## Implementierungen

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Dedizierter Podcast-Bildschirm mit Episodenliste und Inline-Player (erste größere Client-Implementierung, Mai 2026)
- [Wavlake](https://wavlake.com) - Größte Nostr-native Musik- und Podcasting-Plattform, voraussichtliche Ausrichtung auf kind 54 für Podcast-Inhalte
- [Fountain](https://fountain.fm) - Bitcoin-Podcast-App, voraussichtliche Brücke zwischen RSS und NIP-F4

## Offene Fragen

Die gemergte Spezifikation lässt mehrere Designfragen offen, auf die sich Implementierungen einigen müssen:

- pubkeys pro Ersteller werden empfohlen, aber nicht vorgeschrieben, sodass Plattformen wie Wavlake, die viele Ersteller unter einem pubkey veröffentlichen, gültig bleiben
- Kommentare und Diskussionen pro Episode verwenden generisches NIP-22-Threading und kind 1-Timeline-Notizen anstelle eines dedizierten Episoden-Kommentar-kinds
- Metadaten pro Podcast (Host, Netzwerk, Sprache, Lizenz) liegen entweder in den kind 0-Metadaten des Herausgebers oder in einem separaten kind 54-Podcast-Level-Datensatz

---

**Primärquellen:**
- [NIP-F4-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - Ursprünglicher Vorschlag, gemergt am 2026-05-28 nach zweijähriger Diskussion
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Erste größere Client-Implementierung

**Erwähnt in:**
- [Newsletter #25: NIP-Aktualisierungen und Deep Dive](/de/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Newsletter #27: Amethyst v1.12.0 liefert Cashu-Wallets, nutzaps, einen CLINK-Treiber und Tor-Selbstheilung](/de/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Siehe auch:**
- [NIP-22 (Comments)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Alt tags)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (File Metadata)](/de/topics/nip-94/)
- [NIP-96 (HTTP File Storage)](/de/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
