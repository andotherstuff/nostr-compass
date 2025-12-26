---
title: "BUD-10: Blossom URI Schema"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 definieert een aangepast URI-schema voor Blossom dat alle informatie embed die nodig is om een bestand van elke beschikbare server op te halen.

## URI Formaat

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

Componenten:
- **sha256**: Bestandshash (vereist)
- **ext**: Bestandsextensie
- **size**: Bestandsgrootte in bytes
- **server**: Een of meer server-hints
- **pubkey**: Auteur-pubkeys voor BUD-03 serverontdekking

## Voordelen

- Veerkrachtiger dan statische HTTP-URL's
- Automatische fallback over meerdere servers
- Auteur-gebaseerde ontdekking via pubkey-hints
- Zelfverifiërend (hash garandeert integriteit)

---

**Primaire bronnen:**
- [BUD-10 PR](https://github.com/hzrd149/blossom/pull/84)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)

**Zie ook:**
- [Blossom Protocol](/nl/topics/blossom/)
- [BUD-03: Gebruiker Serverlijst](/nl/topics/bud-03/)
