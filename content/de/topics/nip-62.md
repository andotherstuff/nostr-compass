---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
translationOf: /en/topics/nip-62.md
translationDate: 2026-03-11
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 definiert Vanish Requests, einen Mechanismus, mit dem Nutzer Relays auffordern können, ihre Inhalte zu löschen. Relays müssen diese Requests nicht befolgen, aber die Unterstützung von NIP-62 gibt Nutzern mehr Kontrolle über ihre veröffentlichten Daten und schafft einen standardisierten Weg, Löschabsicht im ganzen Netzwerk zu signalisieren.

## Funktionsweise

Ein Vanish Request ist ein kind 62 Event, das vom Nutzer signiert wird, der seine Inhalte entfernen möchte. Der Request kann bestimmte Events ansprechen, indem deren IDs in `e`-Tags angegeben werden, oder die Löschung aller Inhalte dieses Pubkeys anfordern, indem die `e`-Tags ganz weggelassen werden.

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

Das `content`-Feld kann optional einen menschenlesbaren Grund für die Löschanfrage enthalten. Relay-Hints in den `e`-Tags zeigen Relays, wo die ursprünglichen Events veröffentlicht wurden, auch wenn Relays den Request unabhängig davon befolgen können, ob sie die genannten Events besitzen.

## Relay-Verhalten

Relays, die NIP-62 unterstützen, sollten die angegebenen Events aus ihrem Speicher entfernen und sie nicht mehr an Abonnenten ausliefern. Der Vanish Request selbst kann als Nachweis erhalten bleiben, dass eine Löschung angefordert wurde. Das hilft zu verhindern, dass gelöschte Events später wieder von anderen Relays importiert werden.

Wenn ein Vanish Request alle `e`-Tags weglässt, interpretieren Relays das als Bitte, alle Events dieses Pubkeys zu entfernen. Das ist ein stärkerer Eingriff, und Relays können unterschiedlich damit umgehen, zum Beispiel indem sie den Pubkey als "vanished" markieren und künftig keine Events dieses Schlüssels mehr akzeptieren oder ausliefern.

Relays müssen NIP-62 nicht unterstützen. Das Nostr-Netzwerk ist dezentral, und jeder Relay-Betreiber entscheidet über seine eigene Datenaufbewahrung. Nutzer sollten nicht annehmen, dass ihre Inhalte überall gelöscht werden, nur weil sie einen Vanish Request veröffentlicht haben.

## Warum das wichtig ist

NIP-62 gibt Clients und Relay-Betreibern ein gemeinsames Löschsignal, das über ad-hoc-Moderations-APIs oder relay-spezifische Dashboards hinausgeht. Ein Nutzer kann einen einzigen signierten Request veröffentlichen und jedes Relay entscheidet selbst, wie es ihn verarbeitet.

Die praktische Grenze ist der Geltungsbereich. Ein Vanish Request wirkt nur auf Relays, die ihn sehen, unterstützen und befolgen wollen. Er nimmt keine Screenshots, lokalen Datenbanken, Drittanbieter-Archive oder erneut veröffentlichten Kopien außerhalb der Kontrolle des Relays zurück.

## Datenschutzaspekte

Vanish Requests sind ein Best-Effort-Mechanismus zur Löschung, keine Garantie für Privatsphäre. Selbst nach der Veröffentlichung eines Vanish Requests können Kopien des Inhalts anderswo im Netzwerk existieren, etwa auf Relays ohne NIP-62-Unterstützung, in lokalen Caches auf Client-Geräten, in Drittanbieter-Archiven oder Suchmaschinen sowie in Backups.

Auch der Request selbst ist ein signiertes Nostr-Event und damit Teil des öffentlichen Verlaufs. Jeder, der den Vanish Request sieht, weiß also, dass du etwas gelöscht hast, auch wenn er nicht sehen kann, was genau gelöscht wurde.

Für Inhalte, die privat bleiben müssen, ist verschlüsselte Kommunikation wie [NIP-17](/de/topics/nip-17/) die bessere Wahl, statt sich auf spätere Löschung zu verlassen.

## Interop-Hinweise

NIP-62 ergänzt [NIP-09](/de/topics/nip-09/). NIP-09 ist das allgemeine Event für Löschanfragen in Nostr, während NIP-62 Relays ein stärkeres, auf Verschwinden ausgerichtetes Signal gibt, das bestimmte Events oder den gesamten Inhaltsbestand eines Pubkeys abdecken kann. Implementierungen können beides unterstützen, und die Datenbank-Backends von rust-nostr bieten inzwischen Konfiguration für diese Durchsetzungsgrenze.

---

**Primärquellen:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Erwähnt in:**
- [Newsletter #5: Notable Code Changes](/de/newsletters/2026-01-13-newsletter/#rust-nostr-library)
- [Newsletter #10: rust-nostr](/de/newsletters/2026-03-04-newsletter/#rust-nostr-nip-62-request-to-vanish)

**Siehe auch:**
- [NIP-09: Event Deletion Request](/de/topics/nip-09/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
