---
title: "NIP-CD: Slash-Befehle"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD definiert Slash-Befehle. Ein Dienst veröffentlicht einen Befehl, und jeder kann ihn als Klartext im Inhalt eines beliebigen Nostr-Events aufrufen. NIP-CD ist eine optionale Entwurfsspezifikation. Sie wurde am 21. Oktober 2026 nach einem früheren Vorschlag unter dem Titel Commands gemergt und in Slash Commands umbenannt, als am 27. Oktober 2026 optionale Listen installierter Befehle gemergt wurden.

## Funktionsweise

Ein Event der kind 31992 definiert einen Befehl. Pflicht-Tags geben das Auslösewort ohne Schrägstrich, einen Titel und eine Beschreibung der Verwendung an. Geordnete `arg`-Tags deklarieren Positionsargumente mit Typen wie pubkey, event, relay, number, enum oder text. `s`-Tags beschränken nach kind, relay, Autor oder tag, welche Events den Befehl auslösen. Diese Geltungsbereiche funktionieren wie ein Filter: Werte desselben Typs sind Alternativen, und jeder vorhandene Typ muss übereinstimmen.

Ein Aufruf ist Text, der bei Index 0 des Inhalts eines Events beginnt, etwa `/ban` gefolgt von Argumenten, und er trägt keine Tags. Durch Hinzufügen eines Qualifizierers der Form `@nostr:npub1...` wird ein einzelner Executor angesprochen. Ohne Qualifizierer kann jeder Befehl reagieren, dessen Auslöser passt und dessen Geltungsbereich das Event einschließt, sodass eine Nachricht mehrere Dienste auslösen kann.

Die Unterstützung durch Clients ist optional. Clients können Autovervollständigung, Auswahlhilfen für Argumente und gerenderte Chips anbieten. Sie dürfen das Senden eines Aufrufs nicht von ihrer eigenen Unterstützung abhängig machen, und sie müssen Text, der sich nicht parsen lässt, als gewöhnlichen Inhalt senden.

Bei relaybasierten Gruppen gehen Definitionen und Aufrufe an das Gruppen-Relay. Bei der Verwendung als Broadcast gehen Definitionen an die Outboxes der Executoren und Aufrufe an deren Inboxes.

## Listen installierter Befehle

Ein Nutzer kann eine optionale Liste der kind 10992 nach NIP-51 pflegen, die `a`-Tags enthält, welche über den pubkey des Executors und den `d`-Wert auf Befehlsdefinitionen der kind 31992 verweisen, optional mit einem Relay-Hinweis. Clients sollten die Liste für Autovervollständigung und gerenderte Chips verwenden. Die Liste hält die Anzeige- und Auffindungspräferenz eines Nutzers fest. Sie autorisiert keinen Executor, und Aufrufe als Klartext funktionieren auch ohne sie. Dieser Teil der Spezifikation wurde am 27. Oktober 2026 über PR #2525 gemergt. Der Merge zeigt nicht, welche Clients die Liste implementiert haben.

## Primärquellen

- [NIP-CD-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [Merge von NIP-CD am 21. Oktober 2026](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [PR #2525 für Listen installierter Befehle, gemergt am 27. Oktober 2026](https://github.com/nostr-protocol/nips/pull/2525)
- [Commit aus PR #2525 vom 26. Oktober 2026, vor dem Merge auf dessen Branch erstellt](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [Merge der Listen installierter Befehle in NIP-CD am 27. Oktober 2026](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## Erwähnt in
- [Newsletter #46: NIP-CD definiert Befehle, die als Klartext aufgerufen werden](/de/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) Newsletter

- [Newsletter #46: NIP-CD ergänzt optionale Listen installierter Befehle](/de/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) Newsletter

- [Newsletter #46 (2026-10-28): Oktober 2026, gemeinsame Bedeutungen von Abfragen und durch Text ausgelöste Dienste](/de/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## Siehe auch

- [NIP-01: Grundlegendes Protokoll](/de/topics/nip-01/)
