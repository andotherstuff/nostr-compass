---
title: "NIP-F4: Podcast"
date: 2026-06-03
draft: false
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4 definisce come i client Nostr fanno riferimento, presentano e interagiscono socialmente con gli episodi dei podcast. Fatto il merge il 2026-05-28 dopo due anni e tre mesi in stato di draft, la specifica usa eventi di kind 54 per gli episodi ed è progettata attorno all'esistente stack RSS di podcasting come livello complementare.

## Come funziona

Un evento episodio podcast di kind 54 trasporta un tag `title`, un tag `image` opzionale, un tag `description`, uno o più tag `imeta` per il file audio (URL, mime type, hash, durata, bitrate, codice lingua, URL di fallback, flag del servizio NIP-96), tag topic `t` e un tag `alt` NIP-31 per la visualizzazione di fallback.

La scelta di design portante è il tag `i`, che trasporta il GUID RSS dell'episodio usando il formato `podcast:item:guid:<guid>`. Questo consente:

- A un client Nostr di visualizzare un evento di kind 54 e collegarlo allo stesso episodio in qualsiasi app di podcast compatibile con RSS
- A un client Nostr compatibile con RSS di presentare gli episodi di un podcast esistente come eventi di kind 54 senza costringere il podcaster a migrare l'hosting
- Il threading dei commenti cross-protocol tramite i tag Podcasting 2.0 `<podcast:socialInteract>` e `<podcast:chat>`

## Coesistenza con RSS

Il dibattito durato due anni sul thread della PR (con il co-autore di Podcasting 2.0 Dave Jones, Alex Gleason, fiatjaf, Mike Terenzio, Pablo F7z e Jeff Gardner) si è concluso con la coesistenza. Nostr fornisce il livello sociale e di scoperta mentre RSS mantiene la fonte di verità per il file audio e i metadati del feed. Nostr non duplica il livello di distribuzione RSS.

Questo contrasta con i precedenti tentativi di sostituire RSS (JSONFeed, RSS 3.0, API proprietarie per podcast). Il namespace Podcasting 2.0 supporta già `<podcast:socialInteract>` che fa riferimento a eventi Nostr tramite note ID, quindi un feed RSS può dichiarare il proprio thread di discussione Nostr accompagnatore senza richiedere che Nostr rispecchi il feed stesso.

## Esempio di evento

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

## Implementazioni

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Schermata podcast dedicata con lista degli episodi e player inline (prima implementazione in un client di rilievo, maggio 2026)
- [Wavlake](https://wavlake.com) - Piattaforma di musica e podcasting Nostr-native più estesa, prevista in allineamento con kind 54 per i contenuti podcast
- [Fountain](https://fountain.fm) - App podcast Bitcoin, prevista come bridge tra RSS e NIP-F4

## Questioni aperte

La specifica fatta il merge lascia diverse questioni di design su cui le implementazioni dovranno convergere:

- I pubkey per creatore sono raccomandati ma non richiesti, quindi piattaforme come Wavlake che pubblicano molti creatori sotto un unico pubkey rimangono valide
- I commenti e le discussioni per episodio usano il threading generico NIP-22 e note di kind 1 in timeline invece di un kind dedicato ai commenti degli episodi
- I metadati per podcast (host, network, lingua, licenza) risiedono sia nei metadati di kind 0 del pubblicatore sia in un record separato di kind 54 a livello di podcast

---

**Fonti primarie:**
- [Specifica NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - Proposta originale, fatto il merge il 2026-05-28 dopo due anni di discussione
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - Prima implementazione in un client di rilievo

**Menzionato in:**
- [Newsletter #25: NIP Updates and Deep Dive](/it/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/it/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Vedi anche:**
- [NIP-22 (Comments)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Alt tags)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (File Metadata)](/it/topics/nip-94/)
- [NIP-96 (HTTP File Storage)](/it/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
