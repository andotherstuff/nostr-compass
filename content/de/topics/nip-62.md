---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 definiert Vanish Requests, einen Mechanismus, mit dem Benutzer Relays auffordern können, ihre Inhalte zu löschen. Obwohl Relays nicht verpflichtet sind, diese Anfragen zu erfüllen, gibt die Unterstützung von NIP-62 den Benutzern mehr Kontrolle über ihre veröffentlichten Daten und bietet einen standardisierten Weg, die Löschabsicht im gesamten Netzwerk zu signalisieren.

## Funktionsweise

Ein Vanish Request ist ein kind 62 Event, das vom Benutzer signiert wird, der seine Inhalte entfernen möchte. Die Anfrage kann spezifische Events anvisieren, indem deren IDs in `e`-Tags aufgenommen werden, oder sie kann die Löschung aller Inhalte dieses pubkeys anfordern, indem die `e`-Tags weggelassen werden.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

Das `content`-Feld enthält optional einen für Menschen lesbaren Grund für die Löschanfrage. Relay-Hints in den `e`-Tags teilen Relays mit, wo die ursprünglichen Events veröffentlicht wurden, obwohl Relays Anfragen erfüllen können, unabhängig davon, ob sie die angegebenen Events haben.

## Relay-Verhalten

Relays, die NIP-62 unterstützen, sollten die angegebenen Events aus ihrem Speicher löschen und sie nicht mehr an Abonnenten ausliefern. Der Vanish Request selbst kann als Aufzeichnung aufbewahrt werden, dass eine Löschung angefordert wurde, was hilft zu verhindern, dass gelöschte Events von anderen Relays wieder importiert werden.

Wenn ein Vanish Request alle `e`-Tags weglässt, interpretieren Relays dies als Anfrage, alle Events dieses pubkeys zu entfernen. Dies ist eine drastischere Aktion, und Relays können damit unterschiedlich umgehen, zum Beispiel indem sie den pubkey als „verschwunden" markieren und sich weigern, seine Events künftig zu akzeptieren oder auszuliefern.

Relays sind nicht verpflichtet, NIP-62 zu unterstützen. Das Nostr-Netzwerk ist dezentralisiert, und jeder Relay-Betreiber entscheidet über seine eigenen Datenaufbewahrungsrichtlinien. Benutzer sollten nicht davon ausgehen, dass ihre Inhalte überall gelöscht werden, nur weil sie einen Vanish Request veröffentlicht haben.

## Datenschutzüberlegungen

Vanish Requests sind ein Best-Effort-Löschmechanismus, keine Garantie für Privatsphäre. Selbst nach der Veröffentlichung eines Vanish Requests können Kopien der Inhalte anderswo im Netzwerk existieren, einschließlich auf anderen Relays, die NIP-62 nicht unterstützen, in lokalen Caches auf Client-Geräten, in Drittanbieter-Archiven oder Suchmaschinen und in Backups.

Die Anfrage selbst ist auch ein signiertes Nostr-Event, was bedeutet, dass sie Teil deiner öffentlichen Aufzeichnung wird. Jeder, der den Vanish Request sieht, weiß, dass du etwas gelöscht hast, auch wenn er nicht sehen kann, was gelöscht wurde.

Für Inhalte, die privat bleiben müssen, erwäge die Verwendung von verschlüsselten Nachrichten wie [NIP-17](/de/topics/nip-17/), anstatt dich auf nachträgliche Löschung zu verlassen.

---

**Primärquellen:**
- [NIP-62 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Erwähnt in:**
- [Newsletter #5: Bemerkenswerte Code-Änderungen](/de/newsletters/2026-01-13-newsletter/#rust-nostr-library)
