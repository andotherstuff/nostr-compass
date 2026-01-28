---
title: "NIP-22: Kommentare"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22 definiert einen Standard für das Kommentieren beliebiger adressierbarer Nostr-Inhalte und ermöglicht Thread-Diskussionen zu Artikeln, Videos, Kalenderereignissen und anderen adressierbaren Events.

## Funktionsweise

Kommentare verwenden kind 1111 Events mit Tags, die auf den kommentierten Inhalt verweisen:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "Toller Artikel!"
}
```

## Tag-Struktur

- **`A`-Tag**: Verweist auf das adressierbare Event, das kommentiert wird (kind:pubkey:d-tag Format)
- **`E`-Tag**: Verweist auf die Root-Event-ID für Threading
- **`K`-Tag**: Gibt die Art des Root-Events an
- **`e`-Tag**: Verweist auf Elternkommentar für verschachtelte Antworten

## Unterschied zu Kind 1

Während kind 1 Notizen auf andere Notizen antworten können, sind NIP-22-Kommentare speziell konzipiert für:

- Adressierbare Inhalte (Artikel, Videos, Kalenderereignisse)
- Aufrechterhaltung klarer Eltern-Kind-Beziehungen
- Ermöglichung von Moderation und Threading bei Langform-Inhalten

## Anwendungsfälle

- Artikeldiskussionen
- Videokommentare
- [NIP-52](/de/topics/nip-52/) Kalenderereignis-Diskussionen
- Wiki-Seiten-Diskussionsseiten
- Jeder adressierbare Event-Typ

## Verwandt

- [NIP-01](/de/topics/nip-01/) - Grundprotokoll (kind 1 Notizen)
- [NIP-52](/de/topics/nip-52/) - Kalenderereignisse
