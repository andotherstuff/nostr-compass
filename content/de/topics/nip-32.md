---
title: "NIP-32: Labeling"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 definiert einen Standard für das Anhängen von Labels an Nostr-Events, Benutzer und andere Entitäten. Labels bieten strukturierte Metadaten, die Clients für Kategorisierung, Inhaltswarnungen, Reputationssysteme und Moderation verwenden können.

## Funktionsweise

Labels verwenden kind 1985 Events mit einem `L`-Tag, das den Label-Namespace definiert, und `l`-Tags, die spezifische Labels innerhalb dieses Namespace anwenden. Die gelabelte Entität wird durch Standard-Tags wie `e` (Events), `p` (pubkeys) oder `r` (Relay-URLs) referenziert.

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Enthält explizite Bilder"
}
```

Das Namespace-System verhindert Label-Kollisionen. Ein „spam"-Label im „ugc-moderation"-Namespace hat andere Semantik als „spam" im „relay-report"-Namespace. Dies ermöglicht das Koexistieren mehrerer Label-Systeme ohne Interferenz.

## Anwendungsfälle

Inhaltsmoderierungssysteme verwenden Labels, um Spam, illegale Inhalte oder Richtlinienverstöße zu markieren. Reputationssysteme fügen Vertrauenswerte oder Verifizierungsstatus an pubkeys an. Medienplattformen wenden Inhaltswarnungen an (NSFW, Gewalt, Spoiler). Relay-Betreiber verwenden Labels für Einsprüche und Streitbeilegung.

Der Trusted Relay Assertions-Vorschlag verwendet NIP-32-Labels für Relay-Einsprüche. Wenn Betreiber Vertrauenswerte anfechten, veröffentlichen sie kind 1985 Events mit `L` = `relay-appeal` und Label-Typen wie „spam", „censorship" oder „score".

Client-Implementierungen variieren darin, wie sie Labels konsumieren. Einige Clients behandeln Labels von gefolgten Benutzern als Empfehlungen, während andere spezialisierte Labeling-Dienste abfragen. Das dezentralisierte Design lässt Benutzer wählen, welchen Labelern sie vertrauen.

---

**Primärquellen:**
- [NIP-32 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/32.md) - Labeling-Standard

**Erwähnt in:**
- [Newsletter #6: NIP-Updates](/de/newsletters/2026-01-21-newsletter/#nip-updates)

**Siehe auch:**
- [Trusted Relay Assertions](/de/topics/trusted-relay-assertions/)
- [NIP-51: Listen](/de/topics/nip-51/)
