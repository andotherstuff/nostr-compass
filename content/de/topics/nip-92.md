---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - Medien
  - Protokoll
---

NIP-92 ermöglicht es Benutzern, Mediendateien an Nostr-Events anzuhängen, indem URLs zusammen mit Inline-Metadaten-Tags eingefügt werden, die diese Ressourcen beschreiben.

## Funktionsweise

1. Der Benutzer platziert Medien-URLs direkt im Event-Inhalt (z.B. in einer kind 1 Textnachricht)
2. Ein entsprechender `imeta` (Inline-Metadaten) Tag liefert Details zu jeder URL
3. Clients können imeta-URLs durch reichhaltige Vorschauen basierend auf den Metadaten ersetzen
4. Metadaten werden typischerweise automatisch generiert, wenn Dateien während der Erstellung hochgeladen werden

## Der imeta Tag

Jeder `imeta` Tag muss eine `url` und mindestens ein weiteres Feld haben. Unterstützte Felder umfassen:

- `url` - Die Medien-URL (erforderlich)
- `m` - MIME-Typ der Datei
- `dim` - Bildabmessungen (Breite x Höhe)
- `blurhash` - Blurhash für Vorschaugenerierung
- `alt` - Alternativtext für Barrierefreiheit
- `x` - SHA-256-Hash (aus NIP-94)
- `fallback` - Alternative URLs bei Ausfall der primären

## Beispiel

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Primärquellen:**
- [NIP-92 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/92.md)

**Erwähnt in:**
- [Newsletter #3: Dezember-Rückblick](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-94: Datei-Metadaten](/de/topics/nip-94/)
