---
title: "NIP-32: Labeling"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 definiert einen Standard für das Anhängen von Labels an Nostr-Events, Benutzer und andere Entitäten. Labels liefern strukturierte Metadaten, die Clients für Kategorisierung, Inhaltswarnungen, Reputationssysteme und Moderation verwenden können.

## Wie es funktioniert

Labels verwenden kind 1985 Events mit einem `L`-Tag, das den Label-Namespace definiert, und `l`-Tags, die konkrete Labels innerhalb dieses Namespace anwenden. Die gelabelte Entität wird durch Standard-Tags wie `e` für Events, `p` für pubkeys oder `r` für Relay-URLs referenziert.

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

Das Namespace-System verhindert Label-Kollisionen. Ein `spam`-Label im Namespace `ugc-moderation` hat eine andere Semantik als `spam` im Namespace `relay-report`. Dadurch können mehrere Label-Systeme nebeneinander existieren, ohne sich gegenseitig zu stören.

## Warum es wichtig ist

Die entscheidende Designwahl ist, dass Labels Behauptungen sind und keine im Protokoll eingebauten Fakten. Ein kind 1985 Event sagt nur, dass ein bestimmter Akteur etwas in einem bestimmten Namespace gelabelt hat. Clients brauchen weiterhin eine Vertrauensrichtlinie, um zu entscheiden, wessen Labels sie anzeigen, verbergen oder ignorieren.

Dadurch ist NIP-32 weit über Moderation hinaus nützlich. Dieselbe Struktur kann Inhaltswarnungen, Verifizierungsmarker, Klassifikationssysteme oder Relay-Reputationsdaten transportieren, ohne alle Clients auf ein gemeinsames globales Vokabular festzulegen.

## Anwendungsfälle

Inhaltsmoderierungssysteme verwenden Labels, um Spam, illegale Inhalte oder Richtlinienverstöße zu markieren. Reputationssysteme fügen Vertrauenswerte oder Verifizierungsstatus an pubkeys an. Medienplattformen wenden Inhaltswarnungen wie NSFW, Gewalt oder Spoiler an. Relay-Betreiber verwenden Labels für Einsprüche und Streitbeilegung.

Der Vorschlag Trusted Relay Assertions verwendet NIP-32-Labels für Relay-Einsprüche. Wenn Betreiber Vertrauenswerte anfechten, veröffentlichen sie kind 1985 Events mit `L = relay-appeal` und Labels wie `spam`, `censorship` oder `score`.

## Interop-Hinweise

Clients unterscheiden sich darin, wie sie Labels auswerten. Einige behandeln Labels von gefolgten Nutzern als Empfehlung, während andere spezialisierte Labeling-Dienste abfragen. Das dezentrale Design lässt Nutzer selbst entscheiden, welchen Labelern sie vertrauen, aber ein Label ohne sichtbaren Vertrauenskontext kann leicht irreführend sein.

---

**Primärquellen:**
- [NIP-32 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/32.md) - Labeling-Standard

**Erwähnt in:**
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)

**Siehe auch:**
- [Trusted Relay Assertions](/de/topics/trusted-relay-assertions/)
- [NIP-51: Listen](/de/topics/nip-51/)
