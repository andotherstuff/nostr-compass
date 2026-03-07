---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2026-03-07
draft: false
categories:
  - Kryptografie
  - Protokoll
  - Messaging
  - Datenschutz
---

Message Layer Security (MLS) ist ein IETF-Protokoll für Ende-zu-Ende-verschlüsselte Gruppennachrichten. Es bietet Forward Secrecy und Post-Compromise Security für Gruppen, deren Mitgliedschaft sich im Lauf der Zeit ändern kann.

## Wie es funktioniert

MLS verwendet eine baumbasierte Schlüsselvereinbarungsstruktur namens TreeKEM:

1. **Key Packages**: Jeder Teilnehmer veröffentlicht ein Key Package mit seiner Identität und seinen Verschlüsselungsschlüsseln
2. **Group State**: Ein Ratchet Tree verwaltet den kryptografischen Zustand der Gruppe
3. **Commits**: Mitglieder aktualisieren den Baum beim Beitritt, Austritt oder bei Schlüsselrotationen
4. **Message Encryption**: Inhalte werden mit Schlüsseln verschlüsselt, die aus dem gemeinsamen Gruppengeheimnis abgeleitet sind

## Warum es wichtig ist

MLS löst ein Problem, das paarweise Verschlüsselung nicht gut löst: Gruppenmitgliedschaft und Verschlüsselungszustand konsistent zu halten, wenn Mitglieder asynchron beitreten, ausscheiden oder Schlüssel rotieren.

Seine Baumstruktur ist der praktische Kernpunkt. Updates erfordern nicht, dass jeder Teilnehmer paarweise mit allen anderen neu verhandelt, deshalb skaliert das Protokoll viel besser als ad hoc entworfene Gruppenschlusselschemata.

## Standardisierung

- **RFC 9420** (Juli 2023): Kernspezifikation des MLS-Protokolls
- **RFC 9750** (April 2025): MLS-Architektur für die Systemintegration

## Einsatz in Nostr

Mehrere Nostr-Anwendungen verwenden MLS für sichere Gruppennachrichten:

- **KeyChat**: MLS-basierte verschlüsselte Messaging-App für Mobilgeräte und Desktop
- **White Noise**: Private Nachrichten mit MLS und Marmot-Protocol-Integration
- **Marmot Protocol**: Nostr-Erweiterung mit MLS-basierter Gruppenverschlusselung

MLS bietet stärkere Sicherheitsgarantien für Gruppen als [NIP-04](/de/topics/nip-04/) oder [NIP-44](/de/topics/nip-44/) allein, besonders wenn sich die Mitgliedschaft häufig ändert.

## Abwägungen

MLS ist kein vollständiges Messaging-Produkt. Anwendungen brauchen zusätzlich Identität, Transport, Spam-Abwehr, Speicherung und Konfliktbehandlung rund um das Protokoll.

Deshalb legen Nostr-Projekte wie Marmot weitere Regeln auf MLS. Die Kryptografie ist standardisiert, aber das umgebende Anwendungsprotokoll bleibt für Interoperabilität wichtig.

---

**Primärquellen:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Erwähnt in:**
- [Newsletter #3: Releases](/en/newsletters/2025-12-31-newsletter/#releases)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [Marmot Protocol](/de/topics/marmot/)
- [MIP-05: Datenschutzfreundliche Push-Benachrichtigungen](/de/topics/mip-05/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
