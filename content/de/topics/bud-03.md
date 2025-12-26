---
title: "BUD-03: Benutzer-Serverliste"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 definiert, wie Benutzer ihre bevorzugten Blossom-Server veröffentlichen, wodurch Clients erkennen können, wo sie Mediendateien eines Benutzers hochladen und abrufen können.

## Funktionsweise

Benutzer veröffentlichen ein Kind-10063-Event, das ihre Blossom-Server auflistet. Clients können dann:
- Medien auf die bevorzugten Server des Benutzers hochladen
- Herausfinden, wo die Blobs eines Benutzers zu finden sind, wenn dessen Pubkey angegeben wird

Dies ermöglicht autorenbasierte Erkennung als Alternative zum direkten Einbetten von Server-URLs in Inhalte.

---

**Primärquellen:**
- [BUD-03 Spezifikation](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**Siehe auch:**
- [Blossom-Protokoll](/de/topics/blossom/)
- [NIP-51: Listen](/de/topics/nip-51/)
