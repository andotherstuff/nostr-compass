---
title: "NIP-B0: Web-Lesezeichen"
date: 2026-05-28
draft: false
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
categories:
  - Protocol
  - Social
---

NIP-B0 definiert ein parametrisiertes ersetzbares event (kind 39701), das Web-Lesezeichen als erstklassige Nostr-events veröffentlicht. Der Vorschlag lässt Nutzer kuratierte Lesezeichensammlungen aufbauen, die entdeckt, gezapt und über Clients hinweg neu veröffentlicht werden können, ohne auf einen zentralen Lesezeichendienst angewiesen zu sein.

## Wie es funktioniert

Ein Lesezeichen ist ein kind 39701-event, dessen `d`-tag die kanonische URL der markierten Seite ist. Ersetzbare Semantik lässt den Autor sein eigenes Lesezeichen für diese URL aktualisieren (neu taggen, den Titel aktualisieren, als veraltet markieren), ohne doppelte events zu erzeugen. Das content-Feld trägt die Notiz des Autors zum Lesezeichen; tags tragen Titel, Beschreibung, Bild und `t`-Themen-tags zur Entdeckung.

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

Der `d`-tag identifiziert das Lesezeichen eindeutig pro Autor, sodass zwei Nutzer dieselbe URL mit ihren eigenen Anmerkungen und tag-Sets mit einem Lesezeichen versehen können.

## Entdeckung und Kuration

Da jedes Lesezeichen ein erstklassiges event ist, kann jeder Nostr-Client einen Feed von Lesezeichen darstellen, indem er kind 39701-events abonniert, gefiltert nach tags oder Autoren. Kurator-gesteuerte Workflows werden natürlich: Ein Kurator veröffentlicht eine Liste von Lesezeichen, Leser folgen dem pubkey des Kurators, und die Lesezeichen fließen durch jedes relay, das sie trägt. Es gibt kein zentrales Verzeichnis.

## Implementierungen

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) - Referenz-Web-Client mit einer Drei-Box-Architektur (Kurator, Indexer, Betrachter) und einem Stufensystem, das durch direkte NIP-57-zaps an den Kurator finanziert wird. Implementiert NIP-B0 neben NIP-07, NIP-46, NIP-57, NIP-44, NIP-98, NIP-65 und Blossom BUD-01/BUD-04 zur Dateispeicherung.

## Vertrauens- und Sicherheitshinweise

- Lesezeichen sind standardmäßig öffentlich; private Leselisten sollten nicht auf diese Weise veröffentlicht werden
- Die erneute Veröffentlichung ist darauf angewiesen, dass relays die events weiterhin tragen; ephemere relays werden Lesezeichen verwerfen
- Der `published_at`-tag wird vom Herausgeber behauptet, ist aber nicht verifizierbar

---

**Primärquellen:**
- [NIP-B0-Spezifikationsvorschlag](https://github.com/nostr-protocol/nips/pull/2089) - Verfolgt das vorgeschlagene kind 39701-Web-Lesezeichen-event
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) - Referenzimplementierung mit Kurator-Stufensystem

**Erwähnt in:**
- [Newsletter #24: deepmarks NIP-B0-Lesezeichen mit kurator-monetarisierter Veröffentlichung](/de/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Newsletter #27: Ebenfalls veröffentlicht](/de/newsletters/2026-06-17-newsletter/#also-shipped)

**Siehe auch:**
- [NIP-57: Lightning Zaps](/de/topics/nip-57/)
- [NIP-65: Relay-Listen-Metadaten](/de/topics/nip-65/)
