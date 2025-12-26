---
title: "BUD-03: Gebruiker Serverlijst"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 definieert hoe gebruikers hun voorkeurs-Blossom-servers publiceren, waardoor clients kunnen ontdekken waar ze mediabestanden van een gebruiker kunnen uploaden en ophalen.

## Hoe Het Werkt

Gebruikers publiceren een kind 10063 event dat hun Blossom-servers opsomt. Clients kunnen dan:
- Media uploaden naar de voorkeursservers van de gebruiker
- Ontdekken waar de blobs van een gebruiker te vinden zijn wanneer hun pubkey wordt gegeven

Dit maakt auteur-gebaseerde ontdekking mogelijk als alternatief voor het direct embedden van server-URL's in content.

---

**Primaire bronnen:**
- [BUD-03 Specificatie](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**Zie ook:**
- [Blossom Protocol](/nl/topics/blossom/)
- [NIP-51: Lijsten](/nl/topics/nip-51/)
