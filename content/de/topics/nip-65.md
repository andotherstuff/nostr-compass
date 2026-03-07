---
title: "NIP-65: Relay-Listen-Metadaten"
date: 2026-01-13
translationOf: /en/topics/nip-65.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 definiert kind 10002 Events, die bekanntgeben, welche Relays ein Nutzer zum Lesen und Schreiben bevorzugt. Diese Metadaten helfen anderen Nutzern und Clients, deine Inhalte im verteilten Relay-Netzwerk zu finden, und ermöglichen das "Outbox Model", das Last verteilt und die Zensurresistenz verbessert.

## Struktur

Eine Relay-Liste ist ein ersetzbares Event (kind 10002), das für jedes Relay, das der Nutzer veröffentlichen möchte, ein `r`-Tag enthält. Das Event ersetzt jede frühere Relay-Liste desselben Pubkeys.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

Jedes `r`-Tag enthält eine Relay-WebSocket-URL und optional einen Marker, der angibt, wie der Nutzer mit diesem Relay interagiert. Der Marker `read` bedeutet, dass der Nutzer von diesem Relay Events liest, also sollten andere dort veröffentlichen, um ihn zu erreichen. Der Marker `write` bedeutet, dass der Nutzer auf diesem Relay veröffentlicht, also sollten andere dort abonnieren, um seine Inhalte zu sehen. Wird der Marker weggelassen, bedeutet das sowohl read als auch write.

Das `content`-Feld ist bei Relay-Listen-Events leer.

## Das Outbox Model

NIP-65 ermöglicht ein dezentrales Muster zur Inhaltsverteilung, das "Outbox Model". Statt dass alle auf denselben zentralen Relays veröffentlichen und lesen, veröffentlichen Nutzer auf ihren eigenen bevorzugten Relays und Clients entdecken dynamisch, wo die Inhalte jedes Nutzers zu finden sind.

Wenn Alice Bobs Beiträge finden will, holt ihr Client zuerst Bobs kind-10002-Event von einem Relay, das es hat. Dann extrahiert sie die Relays, die Bob für `write` markiert hat, weil er dort veröffentlicht. Ihr Client abonniert diese Relays für Bobs Events. Wenn Alice Bob eine Direktnachricht senden will, sucht ihr Client stattdessen nach seinen `read`-Relays und veröffentlicht die Nachricht dort.

Clients, die dem Outbox Model folgen, halten Verbindungen zu den Relays aufrecht, die in den NIP-65-Events der gefolgten Nutzer stehen. Entdecken sie neue Accounts, verbinden sie sich dynamisch mit neuen Relays. Relays, die in den Listen mehrerer gefolgter Nutzer auftauchen, werden priorisiert, weil eine Verbindung zu ihnen mehr vom sozialen Graphen des Nutzers abdeckt.

Diese Architektur verbessert die Zensurresistenz, weil kein einzelnes Relay alle Inhalte speichern oder ausliefern muss. Wenn ein Relay offline geht oder einen Nutzer blockiert, bleiben seine Inhalte über andere eingetragene Relays verfügbar.

## Warum das wichtig ist

NIP-65 macht die Relay-Auswahl aus einer hartcodierten Client-Voreinstellung zu vom Nutzer veröffentlichten Routing-Metadaten. So können Clients sich an die tatsächlichen Lese- und Schreibgewohnheiten eines Accounts anpassen, statt anzunehmen, dass alle denselben Relay-Satz verwenden.

Es verlagert aber auch Komplexität auf Clients. Um das Outbox Model gut zu nutzen, braucht ein Client Relay-Caching, Retry-Logik und Fallback-Verhalten für fehlende oder veraltete Relay-Listen. Die Spezifikation verbessert Auffindbarkeit, ersetzt aber keine guten Heuristiken für Relay-Auswahl.

## Beziehung zu Relay-Hints

NIP-65 ergänzt die Relay-Hints aus anderen NIPs. Wenn du jemanden mit `[["p", "pubkey", "wss://hint.relay"]]` taggst, sagt der Hint Clients, wo sie für genau diese Referenz suchen sollen. NIP-65 liefert die autoritative, vom Nutzer kontrollierte Liste bevorzugter Relays, während Hints Abkürzungen in einzelnen Events für schnellere Auffindung bieten.

Für private Nachrichten reicht NIP-65 nicht allein aus. Öffentliches Content-Routing nutzt kind 10002, aber moderne private Messaging-Stacks verlassen sich oft auf eigene Inbox-Metadaten wie Relay-Listen aus [NIP-17](/de/topics/nip-17/), damit Nutzer DM-Routing von ihren Relays für öffentliche Posts trennen können.

## Best Practices

Halte deine Relay-Liste aktuell, denn veraltete Einträge auf nicht mehr funktionierende Relays machen dich schwerer auffindbar. Füge mindestens zwei oder drei Relays für Redundanz hinzu, damit deine Inhalte erreichbar bleiben, wenn eines offline geht.

Liste nicht zu viele Relays auf. Wenn du zehn oder fünfzehn Relays einträgst, muss sich jeder Client, der deine Inhalte abrufen will, mit allen verbinden. Das verlangsamt die Nutzung und erhöht die Last im Netzwerk. Eine fokussierte Liste von drei bis fünf gut gewählten Relays ist hilfreicher als eine vollständige Liste, die alle belastet, die dir folgen.

Mische allgemeine Relays mit spezialisierten Relays, die du nutzt. Du könntest etwa ein verbreitetes allgemeines Relay wie `wss://relay.damus.io`, ein Relay mit regionalem Fokus und ein Relay für eine bestimmte Community eintragen, an der du teilnimmst.

---

**Primärquellen:**
- [NIP-65 Specification](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Erwähnt in:**
- [Newsletter #5: NIP Deep Dive](/de/newsletters/2026-01-13-newsletter/#nip-65-relay-list-metadata)
- [Newsletter #10: Outbox Model Benchmarks](/de/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [NIP-11: Relay Information](/de/topics/nip-11/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
