---
title: "Blossom-Protokoll"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

Blossom ist ein Medien-Hosting-Protokoll für Nostr, das Blobs auf gewöhnlichen HTTP-Servern speichert und sie anhand ihres SHA-256-Hashes statt durch serverseitig vergebene IDs adressiert.

## Wie es funktioniert

Blossom-Server bieten eine kleine HTTP-Schnittstelle für den Abruf, das Hochladen und die Verwaltung von Blobs. Der kanonische Bezeichner ist der Datei-Hash, sodass derselbe Blob auf jedem konformen Server dieselbe Adresse behält.

- `GET /<sha256>` ruft einen Blob per Hash ab
- `PUT /upload` lädt einen Blob hoch
- kind `24242` Nostr-Events autorisieren Uploads und Verwaltungsaktionen
- kind `10063`-Events, definiert in [BUD-03](/de/topics/bud-03/), ermöglichen es Nutzern, ihre bevorzugten Server zu veröffentlichen

Da der Hash der Bezeichner ist, können Clients die Integrität nach dem Download lokal prüfen und einen anderen Server versuchen, ohne die zugrunde liegende Referenz zu ändern.

## Warum es wichtig ist

Blossom trennt Blob-Speicherung von sozialen Events. Eine Notiz oder ein Profil kann auf Medien verweisen, ohne diese Medien an das URL-Schema eines einzigen Hosts zu binden.

Das verändert auch die Fehlerbehandlung. Wenn ein Server ausfällt, können Clients denselben Hash von einem Spiegel, einem Cache oder einem Server abrufen, der über die [BUD-03](/de/topics/bud-03/)-Liste des Autors gefunden wurde. Das ist eine praktische Verbesserung gegenüber Mediensystemen, bei denen die URL des ursprünglichen Hosts der einzige Locator ist.

## Interop-Hinweise

Blossom ist modular aufgebaut. Das grundlegende Abruf- und Upload-Verhalten ist in BUD-01 und BUD-02 definiert, während Spiegelung, Medienoptimierung, Autorisierung und URI-Freigabe in separate BUDs aufgeteilt sind.

Diese Aufteilung ermöglicht es Clients, das Minimum für grundlegende Interoperabilität zu implementieren und dann optionale Teile wie [BUD-10](/de/topics/bud-10/) URI-Hinweise oder lokales Caching hinzuzufügen, wenn die Unterstützung reift.

---

**Primärquellen:**
- [Blossom Repository](https://github.com/hzrd149/blossom)
- [BUD-01: Server-Anforderungen und Blob-Abruf](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02: Blob-Upload und -Verwaltung](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [Leitfaden für lokalen Blossom-Cache](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**Erwähnt in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Notable Code Changes](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)
- [Newsletter #10: Blossom local cache layer emerges](/en/newsletters/2026-02-18-newsletter/#blossom-local-cache-layer-emerges)

**Siehe auch:**
- [BUD-03: User Server List](/de/topics/bud-03/)
- [BUD-10: Blossom URI Scheme](/de/topics/bud-10/)
