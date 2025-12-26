---
title: "Blossom-Protokoll"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom ist ein Medien-Hosting-Protokoll für Nostr, das dezentralen Dateispeicher mit inhaltsadressierbaren URLs bereitstellt.

## Funktionsweise

Dateien werden auf Blossom-Servern gespeichert und über ihren SHA256-Hash adressiert. Das bedeutet:
- Dieselbe Datei hat immer dieselbe URL auf allen Servern
- Dateien können von jedem Server abgerufen werden, der sie hat
- Clients können die Dateiintegrität durch Überprüfen des Hashes verifizieren

## Funktionen

- Inhaltsadressierbare Speicherung
- Redundanz über mehrere Server
- Autorenerkennung über BUD-03
- Benutzerdefiniertes URI-Schema über BUD-10
- Cursor-basierte Paginierung auf dem `/list`-Endpunkt

---

**Primärquellen:**
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Bemerkenswerte Code-Änderungen](/de/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**Siehe auch:**
- [BUD-03: Benutzer-Serverliste](/de/topics/bud-03/)
- [BUD-10: Blossom-URI-Schema](/de/topics/bud-10/)
