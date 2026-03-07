---
title: "NIP-30: Custom Emoji"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-30 definiert, wie Clients benutzerdefinierte Emoji in Nostr-Events anzeigen. Custom Emoji werden im Event-Inhalt über Shortcodes (`:shortcode:`) referenziert und durch `emoji`-Tags aufgelöst, die jeden Shortcode einer Bild-URL zuordnen.

## Wie es funktioniert

Ein Event mit Custom Emoji enthält `emoji`-Tags zusammen mit den Shortcode-Referenzen im Inhalt:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

Clients ersetzen `:gleam:` und `:nostrich:` im gerenderten Inhalt durch Inline-Bilder von den angegebenen URLs. Shortcodes müssen alphanumerisch sein, wobei Unterstriche als Trennzeichen erlaubt sind, und die Bild-URLs sollten auf kleine, quadratische Bilder verweisen, die sich für die Inline-Anzeige eignen.

## Emoji-Sets

Custom Emoji können in benannten Sets organisiert werden, die als kind 30030 parameterized replaceable events veröffentlicht werden. Jedes Set gruppiert verwandte Emoji unter einem `d`-Tag-Bezeichner:

```json
{
  "kind": 30030,
  "tags": [
    ["d", "nostr-animals"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"],
    ["emoji", "nostrcat", "https://example.com/nostrcat.png"]
  ]
}
```

Ein Update im März 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) fügte optionale Emoji-Set-Adressreferenzen in Emoji-Tags hinzu, sodass Clients das zugehörige Set zum Durchsuchen oder Speichern öffnen können, wenn ein Nutzer auf ein Emoji klickt.

## Interop-Hinweise

Custom Emoji sind eine Darstellungsfunktion, keine Transportgarantie. Wenn ein Client NIP-30 nicht versteht oder die Bild-URL nicht laden kann, sollte er trotzdem den rohen `:shortcode:`-Text anzeigen. Genau deshalb sind lesbare Shortcodes wichtig.

Das Tag ist lokal für das jeweilige Event, solange es nicht auf ein Set verweist. Wenn `:fire:` in zwei verschiedenen Events vorkommt, bedeutet das nicht automatisch dieselbe globale Bedeutung, es sei denn, beide verweisen auf dasselbe Bild oder dasselbe Set. Clients sollten die Emoji-Definition zuerst aus dem aktuellen Event auflösen.

## Reaktionen

NIP-30 Custom Emoji funktionieren auch in kind-7-Reaktions-Events. Eine Reaktion mit `content`, das auf einen Shortcode gesetzt ist, und einem passenden `emoji`-Tag wird als Custom-Emoji-Reaktion auf dem referenzierten Event gerendert:

```json
{
  "kind": 7,
  "content": ":fire:",
  "tags": [
    ["emoji", "fire", "https://example.com/fire.gif"],
    ["e", "<event-id>"]
  ]
}
```

---

**Primärquellen:**
- [NIP-30 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Emoji-Set-Adresse in Tags

**Erwähnt in:**
- [Newsletter #12: NoorNote v0.5.x](/en/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)
