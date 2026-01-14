---
title: "NIP-65: Relay-Listen-Metadaten"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 definiert kind 10002 Events, die bekannt geben, welche Relays ein Benutzer zum Lesen und Schreiben bevorzugt. Diese Metadaten helfen anderen Benutzern und Clients, deine Inhalte im verteilten Relay-Netzwerk zu finden, und ermöglichen das „Outbox-Modell", das die Last verteilt und die Zensurresistenz verbessert.

## Struktur

Eine Relay-Liste ist ein ersetzbares Event (kind 10002), das `r`-Tags für jedes Relay enthält, das der Benutzer bewerben möchte. Das Event ersetzt jede vorherige Relay-Liste desselben pubkeys.

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

Jeder `r`-Tag enthält eine Relay-WebSocket-URL und einen optionalen Marker, der angibt, wie der Benutzer mit diesem Relay interagiert. Der `read`-Marker bedeutet, dass der Benutzer Events von diesem Relay konsumiert, also sollten andere dort veröffentlichen, um den Benutzer zu erreichen. Der `write`-Marker bedeutet, dass der Benutzer auf diesem Relay veröffentlicht, also sollten andere dort abonnieren, um die Inhalte des Benutzers zu sehen. Das Weglassen des Markers zeigt sowohl Lesen als auch Schreiben an.

Das `content`-Feld ist bei Relay-Listen-Events leer.

## Das Outbox-Modell

NIP-65 ermöglicht ein dezentralisiertes Inhaltsverteilungsmuster namens „Outbox-Modell". Anstatt dass jeder auf denselben zentralen Relays veröffentlicht und liest, veröffentlichen Benutzer auf ihren eigenen bevorzugten Relays, und Clients entdecken dynamisch, wo sie die Inhalte jedes Benutzers finden.

Wenn Alice Bobs Beiträge finden möchte, ruft ihr Client zuerst Bobs kind 10002 Event von einem beliebigen Relay ab, das es hat. Sie extrahiert dann die Relays, die Bob für `write` markiert hat, da dort er veröffentlicht. Ihr Client abonniert diese Relays für Bobs Events. Wenn Alice Bob eine Direktnachricht senden möchte, sucht ihr Client stattdessen nach seinen `read`-Relays und veröffentlicht die Nachricht dort.

Clients, die dem Outbox-Modell folgen, halten Verbindungen zu Relays aufrecht, die in den NIP-65-Events ihrer gefolgten Benutzer aufgelistet sind. Wenn sie neue Konten entdecken, verbinden sie sich dynamisch mit neuen Relays. Relays, die in den Listen mehrerer gefolgter Benutzer erscheinen, werden priorisiert, da die Verbindung zu ihnen mehr vom sozialen Graphen des Benutzers bedient.

Diese Architektur verbessert die Zensurresistenz, da kein einzelnes Relay die Inhalte aller speichern oder bereitstellen muss. Wenn ein Relay offline geht oder einen Benutzer blockiert, bleiben seine Inhalte auf seinen anderen gelisteten Relays verfügbar.

## Beziehung zu Relay-Hints

NIP-65 ergänzt die Relay-Hints, die in anderen NIPs zu finden sind. Wenn du jemanden mit `["p", "pubkey", "wss://hint.relay"]` taggst, teilt der Hint Clients mit, wo sie nach dieser spezifischen Referenz suchen sollen. NIP-65 liefert die autoritative, vom Benutzer kontrollierte Liste der bevorzugten Relays, während Hints Abkürzungen bieten, die in einzelne Events eingebettet sind, um die Entdeckung zu beschleunigen.

## Best Practices

Halte deine Relay-Liste aktuell, da veraltete Einträge, die auf nicht mehr existierende Relays zeigen, dich schwerer auffindbar machen. Füge mindestens zwei oder drei Relays zur Redundanz hinzu, damit wenn ein Relay offline geht, deine Inhalte über die anderen zugänglich bleiben.

Vermeide es, zu viele Relays aufzulisten. Wenn du zehn oder fünfzehn Relays auflistest, muss sich jeder Client, der deine Inhalte abrufen möchte, mit allen verbinden, was deren Erfahrung verlangsamt und die Netzwerklast erhöht. Eine fokussierte Liste von drei bis fünf gut gewählten Relays dient dir besser als eine umfassende Liste, die jeden belastet, der dir folgt.

Mische allgemeine Relays mit spezialisierten Relays, die du verwendest. Zum Beispiel könntest du ein beliebtes allgemeines Relay wie `wss://relay.damus.io`, ein Relay mit Fokus auf deine geografische Region und ein Relay für eine bestimmte Community, an der du teilnimmst, auflisten.

---

**Primärquellen:**
- [NIP-65 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Erwähnt in:**
- [Newsletter #5: NIP-Vertiefung](/de/newsletters/2026-01-13-newsletter/#nip-65-relay-listen-metadaten)

**Siehe auch:**
- [NIP-11: Relay-Informationen](/de/topics/nip-11/)
