---
title: "Marmot-Protokoll"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot ist ein Protokoll für Ende-zu-Ende-verschlüsselte Gruppennachrichten, das auf Nostr aufbaut und den Message Layer Security (MLS)-Standard für Forward Secrecy und Post-Compromise-Sicherheit verwendet.

## Funktionsweise

Marmot erweitert Nostr um MLS-basierte Verschlüsselung für Gruppenchats. Im Gegensatz zu NIP-17-DMs, die Eins-zu-Eins sind, bewältigt Marmot sichere Gruppenkommunikation, bei der Mitglieder beitreten und austreten können, während die Verschlüsselungsgarantien erhalten bleiben.

## Hauptfunktionen

- Forward Secrecy und Post-Compromise-Sicherheit über MLS
- Gruppenschlüssel-Management für dynamische Mitgliedschaft
- Datenschutzfreundliche Push-Benachrichtigungen über MIP-05

---

**Primärquellen:**
- [Marmot-Protokoll Repository](https://github.com/marmot-protocol/marmot)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Veröffentlichungen](/de/newsletters/2025-12-17-newsletter/#releases)

**Siehe auch:**
- [MIP-05: Datenschutzfreundliche Push-Benachrichtigungen](/de/topics/mip-05/)
- [NIP-17: Private Direktnachrichten](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
