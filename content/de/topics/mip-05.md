---
title: "MIP-05: Datenschutzfreundliche Push-Benachrichtigungen"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 definiert ein Push-Benachrichtigungsprotokoll für Marmot-Clients, das versucht, die Privatsphäre in einem Umfeld zu wahren, in dem gewöhnliche mobile Push-Systeme meist Device Tokens und Kontobeziehungen offenlegen.

## Wie es funktioniert

- Device Tokens werden mit ECDH+HKDF und ChaCha20-Poly1305 verschlüsselt
- Ephemere Schlüssel verhindern Korrelationen zwischen Benachrichtigungen
- Ein Drei-Event-Gossip-Protokoll (Kinds 447-449) synchronisiert verschlüsselte Tokens zwischen Gruppenmitgliedern
- Decoy Tokens über NIP-59 gift wrapping verschleiern Gruppengrößen

## Privatsphärenmodell

- Push-Benachrichtigungsserver können Nutzer nicht identifizieren
- Die Gruppenmitgliedschaft wird durch Benachrichtigungsmuster nicht offengelegt
- Device Tokens lassen sich nicht über mehrere Nachrichten hinweg korrelieren

Die konkrete Verbesserung ist, dass der Push-Anbieter undurchsichtige Zustell-Tokens sieht, keine direkte Zuordnung von Gruppenmitglied zu Gerät. Das macht Benachrichtigungen nicht in einem absoluten Sinn anonym, aber es reduziert, wie viel die Push-Schicht standardmäßig erfährt.

## Event Kinds

- **Kind 447**: Veröffentlichung eines verschlüsselten Device Tokens
- **Kind 448**: Anfrage zur Token-Synchronisierung
- **Kind 449**: Antwort zur Token-Synchronisierung

## Abwägungen

MIP-05 erhöht die Privatsphäre, indem es zusätzliche Koordination verlangt. Clients müssen den Zustand verschlüsselter Tokens zwischen Gruppenmitgliedern synchronisieren, und Decoy Tokens erhöhen die Nachrichtenlast absichtlich.

Das bedeutet, Implementierer müssen Zustellzuverlässigkeit gegen Metadatenschutz abwägen. Das Protokoll ist gerade deshalb nützlich, weil es Push als Privatsphärenproblem behandelt und nicht nur als Transportbequemlichkeit.

---

**Primärquellen:**
- [MIP-05 Specification](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1 release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Erwähnt in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [Marmot Protocol](/de/topics/marmot/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
