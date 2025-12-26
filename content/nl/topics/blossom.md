---
title: "Blossom Protocol"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom is een media-hosting protocol voor Nostr dat gedecentraliseerde bestandsopslag biedt met content-addresseerbare URL's.

## Hoe Het Werkt

Bestanden worden opgeslagen op Blossom-servers en geadresseerd via hun SHA256-hash. Dit betekent:
- Hetzelfde bestand heeft altijd dezelfde URL over alle servers
- Bestanden kunnen worden opgehaald van elke server die ze heeft
- Clients kunnen bestandsintegriteit verifiëren door de hash te controleren

## Kenmerken

- Content-addresseerbare opslag
- Redundantie over meerdere servers
- Auteurontdekking via BUD-03
- Aangepast URI-schema via BUD-10
- Cursor-gebaseerde paginering op `/list` endpoint

---

**Primaire bronnen:**
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #2: Noemenswaardige Codewijzigingen](/nl/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**Zie ook:**
- [BUD-03: Gebruiker Serverlijst](/nl/topics/bud-03/)
- [BUD-10: Blossom URI Schema](/nl/topics/bud-10/)
