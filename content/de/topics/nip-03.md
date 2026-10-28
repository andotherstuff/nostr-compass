---
title: "NIP-03: OpenTimestamps-Attestierungen für Events"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03 beschreibt, wie man einen [OpenTimestamps](https://opentimestamps.org/)-Nachweis für ein Nostr-Event veröffentlicht. Der Nachweis belegt, dass das Event spätestens zum Zeitpunkt eines bestimmten Bitcoin-Blocks existierte.

**Warnung:** Die aktuelle Spezifikation ist mit `draft`, `optional` und `unrecommended` gekennzeichnet. Laut ihrem Kopfbereich ist sie für einen bestimmten Angriff anfällig und muss aktualisiert werden. Der Text beschreibt den Angriff nicht. Betrachten Sie das Format als historische Referenz und übernehmen Sie es nicht für neue Arbeiten, bis die Spezifikation überarbeitet ist.

## Funktionsweise

Ein Nachweis wird als separates Event der kind 1040 veröffentlicht. Sein Tag `e` nennt die ID des Ziel-Events samt einer Relay-URL, und sein Tag `k` hält die kind des Ziel-Events fest. Der OpenTimestamps-Nachweis muss die ID des Ziel-Events selbst als Digest belegen. Die ID wird nicht erneut gehasht.

Das Feld `content` enthält die vollständige Datei `.ots`, base64-kodiert, mit mindestens einer Bitcoin-Attestierung. Die Spezifikation empfiehlt genau eine Attestierung und keine ausstehenden Attestierungen, da diese Bytes hinzufügen, ohne bei der Verifikation zu helfen.

Ein Verifizierer ruft das Event der kind 1040 ab, dekodiert dessen Inhalt und prüft den Nachweis gegen Bitcoin. Ein gültiger Nachweis zeigt, dass die Event-ID bis zum attestierten Block festgeschrieben wurde. Damit wird ein spätestmöglicher Erstellungszeitpunkt für das Event festgelegt, der nicht vom eigenen `created_at`-Wert des Autors abhängt. Der Nachweis zeigt nicht, dass der Inhalt des Events wahr ist.

## Geschichte

Ein [Commit vom 11. Oktober 2023](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e) änderte, wo Nachweise abgelegt werden. Davor war ein Nachweis ein `ots`-Feld, das an das Event selbst angehängt war. Seitdem ist jeder Nachweis ein separates Event der kind 1040, das auf sein Ziel verweist.

## Primärquellen

- [Aktuelle NIP-03-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [Commit vom 11. Oktober 2023, der Nachweise in Events der kind 1040 verlagert](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## Erwähnt in Newslettern

- [Newsletter #46 (2026-10-28): Oktober 2023, Events tragen Belege und Arbeitsaufträge](/de/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## Siehe auch

- [NIP-01: Grundlegendes Protokoll](/de/topics/nip-01/)
