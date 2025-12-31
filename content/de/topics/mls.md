---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - Kryptografie
  - Protokoll
  - Messaging
  - Datenschutz
---

Message Layer Security (MLS) ist ein IETF-standardisiertes Protokoll für Ende-zu-Ende-verschlüsselte Gruppennachrichten. Es bietet effizienten Schlüsselaustausch mit Forward Secrecy und Post-Compromise-Sicherheit für Gruppen von zwei bis zu Tausenden von Teilnehmern.

## Funktionsweise

MLS verwendet eine baumbasierte Schlüsselvereinbarungsstruktur namens TreeKEM:

1. **Schlüsselpakete**: Jeder Teilnehmer veröffentlicht ein Schlüsselpaket mit seiner Identität und Verschlüsselungsschlüsseln
2. **Gruppenzustand**: Ein Ratchet-Baum pflegt den kryptografischen Zustand der Gruppe
3. **Commits**: Mitglieder aktualisieren den Baum beim Beitreten, Verlassen oder Rotieren von Schlüsseln
4. **Nachrichtenverschlüsselung**: Inhalte werden mit Schlüsseln verschlüsselt, die vom gemeinsamen Gruppengeheimnis abgeleitet sind

## Wichtige Sicherheitseigenschaften

- **Forward Secrecy**: Vergangene Nachrichten bleiben sicher, auch wenn aktuelle Schlüssel kompromittiert werden
- **Post-Compromise-Sicherheit**: Zukünftige Nachrichten werden nach Schlüsselrotation wieder sicher
- **Mitgliederauthentifizierung**: Alle Gruppenmitglieder sind kryptografisch verifiziert
- **Asynchroner Betrieb**: Mitglieder können beitreten/verlassen, ohne dass alle Teilnehmer online sind
- **Skalierbarkeit**: Effizient für Gruppen bis zu 50.000 Teilnehmern

## Standardisierung

- **RFC 9420** (Juli 2023): Kernspezifikation des MLS-Protokolls
- **RFC 9750** (April 2025): MLS-Architektur für Systemintegration

## Adoption in Nostr

Mehrere Nostr-Anwendungen verwenden MLS für sichere Gruppennachrichten:

- **KeyChat**: MLS-basierte verschlüsselte Messaging-App für Mobilgeräte und Desktop
- **White Noise**: Private Nachrichten mit MLS und Marmot-Protokoll-Integration
- **Marmot Protocol**: Nostr-Erweiterung mit MLS-basierter Gruppenverschlüsselung

MLS bietet stärkere Sicherheitsgarantien als NIP-04 oder NIP-44 allein, besonders für Gruppenchats, bei denen Mitglieder dynamisch beitreten und verlassen.

## Branchenadoption

Über Nostr hinaus wird MLS adoptiert von:
- Google Messages (RCS mit MLS über GSMA Universal Profile 3.0)
- Apple Messages (RCS-Unterstützung für MLS angekündigt)
- Cisco WebEx, Wickr, Matrix

---

**Primärquellen:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Erwähnt in:**
- [Newsletter #3: Veröffentlichungen](/de/newsletters/2025-12-31-newsletter/#releases)

**Siehe auch:**
- [Marmot Protocol](/de/topics/marmot/)
- [MIP-05: Datenschutzfreundliche Push-Benachrichtigungen](/de/topics/mip-05/)
- [NIP-17: Private Direktnachrichten](/de/topics/nip-17/)
- [NIP-44: Verschlüsselte Nutzdaten](/de/topics/nip-44/)
