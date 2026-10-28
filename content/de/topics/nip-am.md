---
title: 'Buzz-Entwurf NIP-AM: Metriken für Agenten-Turns'
date: 2026-10-28
translationOf: /en/topics/nip-am.md
translationDate: 2026-10-28
draft: false
---

**Status:** Dies ist ein Entwurfsvorschlag speziell für das Buzz-Projekt. NIP-AM ist kein akzeptierter offizieller NIP. Die Bezeichnung stammt aus der Dokumentation des Buzz-Projekts, und das offizielle NIPs-Repository hat sie weder vergeben noch genehmigt.

## Zweck

NIP-AM erfasst die Nutzung für jeden abgeschlossenen Turn eines KI-Agenten. Der Agent veröffentlicht pro Turn ein `kind:44200`-Event, das nach Buzz-Konvention als reguläres Event behandelt wird, an das nur angehängt wird (append-only). Der Inhalt ist mit NIP-44 vom Agenten an den Eigentümer verschlüsselt. Er enthält Angaben zur Token-Nutzung zusammen mit Korrelations-IDs, und etwaige Kostenwerte sind Schätzungen. Er enthält kein Gesprächsprotokoll.

## Grenzen

Öffentliche Tags identifizieren den Eigentümer und den Agenten, und Relays können weiterhin sehen, wann Events veröffentlicht werden. Das Format verbirgt also nicht, dass Aktivität stattgefunden hat. Ein fehlender Nutzungswert bedeutet „unbekannt“ und darf niemals als null gezählt werden.

## Vorschlag für delegierte Leser

Ein offener Dokumentations-Pull-Request, #8582, schlägt eine vom Eigentümer signierte Berechtigung nach dem Prinzip der minimalen Rechte vor. Danach würde der Agent für jeden aktiven Leser eine separate verschlüsselte Kopie veröffentlichen, die jeweils an die exakte Event-ID der Berechtigung gebunden ist. Der Pull Request ändert keine Autorisierung zur Laufzeit. Die vorgeschlagene kind für die Berechtigung, `30180`, und die Obergrenze für Leser sind noch offene Fragen, und auch die Richtlinie für den Widerruf ist ungeklärt. Ein Widerruf könnte die Relay-Historie und künftige Lesezugriffe einschränken. Er kann keine Kopien löschen, die ein Leser bereits erhalten hat.

## Primärquellen

- [Buzz-Entwurf NIP-AM: Metriken für Agenten-Turns (fixierte Revision)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Buzz-Pull-Request #8582: delegierte Leser von Metriken (offener Entwurf)](https://github.com/block/buzz/pull/8582)

## Siehe auch

- [NIP-44](/de/topics/nip-44/)

**Erwähnt in:**

- [Newsletter #46: Entwurfstext für NIP-AM zu delegierten Lesern von Metriken](/de/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [Newsletter #46: Buzz](/de/newsletters/2026-10-28-newsletter/#buzz)
