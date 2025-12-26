---
title: "MIP-05: Datenschutzfreundliche Push-Benachrichtigungen"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 definiert ein Protokoll für Push-Benachrichtigungen, die die Privatsphäre der Benutzer wahren und das Problem lösen, dass traditionelle Push-Systeme erfordern, dass Server Geräte-Tokens und Benutzeridentitäten kennen.

## Funktionsweise

- Geräte-Tokens werden mit ECDH+HKDF und ChaCha20-Poly1305 verschlüsselt
- Ephemere Schlüssel verhindern die Korrelation zwischen Benachrichtigungen
- Ein Drei-Event-Gossip-Protokoll (Kinds 447-449) synchronisiert verschlüsselte Tokens zwischen Gruppenmitgliedern
- Decoy-Tokens über NIP-59 Gift Wrapping verbergen Gruppengrößen

## Privatsphäre-Garantien

- Push-Benachrichtigungs-Server können Benutzer nicht identifizieren
- Gruppenmitgliedschaft wird nicht durch Benachrichtigungsmuster offengelegt
- Geräte-Tokens können nicht über Nachrichten hinweg korreliert werden

## Event-Kinds

- **Kind 447**: Verschlüsselter Geräte-Token-Veröffentlichung
- **Kind 448**: Token-Synchronisationsanfrage
- **Kind 449**: Token-Synchronisationsantwort

---

**Primärquellen:**
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)

**Siehe auch:**
- [Marmot-Protokoll](/de/topics/marmot/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
