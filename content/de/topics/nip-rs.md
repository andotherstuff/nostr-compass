---
title: 'Buzz-Entwurf NIP-RS: Geräteübergreifende Synchronisierung des Lesestatus'
date: 2026-10-28
translationOf: /en/topics/nip-rs.md
translationDate: 2026-10-28
draft: false
---

**Status:** Dies ist ein Entwurfsvorschlag speziell für das Buzz-Projekt. NIP-RS ist kein akzeptierter offizieller NIP. Die Bezeichnung stammt aus der Dokumentation des Buzz-Projekts, und das offizielle NIPs-Repository hat sie weder vergeben noch genehmigt.

## Zweck

NIP-RS ermöglicht es den Geräten eines einzelnen Nutzers, untereinander abzugleichen, bis wohin dieser Nutzer gelesen hat. Jede Installation veröffentlicht ein adressierbares `kind:30078`-Event. Sein `d`-Tag besteht aus `read-state:`, gefolgt von einer zufälligen Slot-ID, und sein Inhalt ist mit NIP-44 an den eigenen Schlüssel des Nutzers verschlüsselt. Der Klartext ordnet Kontext-IDs Zeitstempel-Grenzen (Frontiers) zu, die jeweils bedeuten, dass alles zu oder vor diesem Zeitpunkt gelesen wurde. Der Entwurf veröffentlicht keine Lesebestätigungen und gibt nicht preis, was andere Personen gelesen haben.

## Grenzen

Frontiers sind Best-Effort-Hinweise auf jüngste Aktivität. Sie bilden keine vollständige Historie gelesener Nachrichten. Manuelle Überschreibungen als ungelesen, einschließlich Tombstone-Untergrenzen, folgen einem separaten dauerhaften Vertrag. Das Laden des vollständigen Überschreibungszustands hängt vom Sortier- und Kapazitätsverhalten der Relays ab, das ein Client nicht vollständig überprüfen kann, sodass ein beliebiges Relay möglicherweise keinen vollständigen Ungelesen-Zustand zurückgibt. Kontext-IDs haben meist nur innerhalb einer Client-Familie eine Bedeutung.

Ein offener Pull Request, #8639, schlägt vor, Buzz-Clients auf eine NIP-11-Fähigkeit `buzz_v1` umzustellen, die auf einer privaten, authentifizierten HTTP-API basiert und standardmäßig deaktiviert ist. Relays ohne diese Fähigkeit würden NIP-RS beibehalten.

## Primärquellen

- [Buzz-Entwurf NIP-RS: Geräteübergreifende Synchronisierung des Lesestatus (fixierte Revision)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Buzz-Pull-Request #8639: Lesestatus über eine Relay-Fähigkeit (offen)](https://github.com/block/buzz/pull/8639)

## Siehe auch

- [NIP-44](/de/topics/nip-44/)
- [NIP-78](/de/topics/nip-78/)

**Erwähnt in:**

- [Newsletter #46: Buzz](/de/newsletters/2026-10-28-newsletter/#buzz)
