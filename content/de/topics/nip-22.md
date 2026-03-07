---
title: "NIP-22: Kommentare"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-22 definiert einen Standard für Kommentare zu beliebigen addressable Nostr-Inhalten. Damit lassen sich Thread-Diskussionen zu Artikeln, Videos, Kalender-Events und anderen addressable Events führen.

## Wie es funktioniert

Kommentare verwenden Kind-1111-Events mit plaintext `content`. Tags für den Root-Kontext sind großgeschrieben, Tags für die direkte Parent-Antwort kleingeschrieben:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Great article!"
}
```

## Tag-Struktur

- **`A` / `E` / `I`** - Root-Kontext der Diskussion: addressable Event, Event-ID oder externer Identifikator
- **`K`** - Kind oder Root-Kontext-Typ dieses Root-Objekts
- **`P`** - Autor des Root-Events, sofern es einen gibt
- **`a` / `e` / `i`** - Direktes Parent-Objekt, auf das geantwortet wird
- **`k`** - Kind oder Kontext-Typ des Parent-Objekts
- **`p`** - Autor des Parent-Objekts

Bei Top-Level-Kommentaren zeigen Root und Parent meist auf dasselbe Ziel. Bei Antworten auf Kommentare bleibt der Root fest, während die kleingeschriebenen Parent-Tags auf den konkreten Kommentar verschoben werden, auf den geantwortet wird.

## Interop-Hinweise

NIP-22-Kommentare sind kein generischer Ersatz für Kind-1-Antworten. Die Spezifikation sagt ausdrücklich, dass Kommentare nicht für Antworten auf Kind-1-Notizen verwendet werden dürfen. Für Note-to-Note-Threads sollten Clients weiter [NIP-10](/de/topics/nip-10/) verwenden.

Ein weiterer nützlicher Unterschied ist der Kontext. NIP-22 kann Diskussionen mit `I`- und `i`-Tags an Ressourcen außerhalb von Notes anheften, darunter URLs und andere externe Identifikatoren aus [NIP-73](/de/topics/nip-73/). Das gibt Clients einen Standardweg, Kommentar-Threads an Webseiten, Podcasts oder andere Objekte außerhalb von Nostr zu hängen.

## Anwendungsfälle

- Artikeldiskussionen
- Videokommentare
- [NIP-52](/de/topics/nip-52/) Kalender-Event-Diskussionen
- Diskussionsseiten für Wiki-Seiten
- Kommentare zu externen Ressourcen, die über `I`-Tags identifiziert werden

---

**Primärquellen:**
- [NIP-22 Specification](https://github.com/nostr-protocol/nips/blob/master/22.md)

**Erwähnt in:**
- [Newsletter #7: Notedeck](/en/newsletters/2026-01-28-newsletter/#notedeck)
- [Newsletter #10: AI Agent NIPs Arrive](/en/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [Newsletter #12: diVine](/en/newsletters/2026-03-04-newsletter/#divine)

**Siehe auch:**
- [NIP-10: Reply Threads](/de/topics/nip-10/)
- [NIP-52: Calendar Events](/de/topics/nip-52/)
- [NIP-73: External Content IDs](/de/topics/nip-73/)
