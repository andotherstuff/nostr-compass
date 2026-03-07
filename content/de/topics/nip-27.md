---
title: "NIP-27 (Textnotiz-Referenzen)"
date: 2026-02-04
description: "NIP-27 definiert, wie Profile, Notizen und andere Entitäten innerhalb von Notizinhalten mit dem nostr: URI-Schema referenziert werden."
translationDate: 2026-03-07
---

NIP-27 legt fest, wie Referenzen auf Nostr-Entitäten in den Inhalt von Text Notes eingebettet werden. Referenzen verwenden das `nostr:`-URI-Schema, gefolgt von einem bech32-kodierten Identifikator, `npub`, `note`, `nevent`, `nprofile` oder `naddr`.

## Wie es funktioniert

Wenn du eine Note schreibst, die einen anderen Nutzer erwähnt oder auf ein anderes Event verweist, wird die Referenz direkt in den Inhalt eingebettet:

```
Check out this post by nostr:npub1... about nostr:note1...
```

Clients parsen diese Referenzen und rendern sie passend, meist als anklickbare Links oder Inline-Profilkarten. Die referenzierten Entitäten können zusätzlich in Event-Tags gespiegelt werden, damit Indexierung oder Benachrichtigungen funktionieren, aber die Spezifikation macht das optional.

Der NIP deckt auch das Parsen von Hashtags ab. Mit `#` markierte Tags werden extrahiert und den `t`-Tags des Events hinzugefügt, damit sie auffindbar sind.

## Referenztypen

- `nostr:npub1...` - Referenz auf ein User-Profil
- `nostr:note1...` - Referenz auf ein bestimmtes Note-Event
- `nostr:nevent1...` - Referenz auf ein Event mit Relay-Hints
- `nostr:nprofile1...` - Referenz auf ein Profil mit Relay-Hints
- `nostr:naddr1...` - Referenz auf ein addressable Event

## Warum es wichtig ist

NIP-27 trennt das, was Menschen lesen, von dem, was Clients speichern. Ein Nutzer kann in einem komfortablen Composer `@name` tippen, während das veröffentlichte Event im `content` trotzdem eine stabile Referenz wie `nostr:nprofile...` enthält. Dadurch bleibt die Referenz zwischen Clients portabel, ohne von der Mention-Syntax einer einzelnen App abzuhängen.

Ein weiterer praktischer Vorteil ist Resilienz. Ein rohes `nostr:nevent...` oder `nostr:naddr...`, das in Text eingebettet ist, trägt noch genug Informationen, damit ein anderer Client das Ziel rekonstruieren kann, selbst wenn er das ursprüngliche lokale Rendering nie gesehen hat.

## Interop-Hinweise

- Verwende im Inhalt selbst das Format aus [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md): `nostr:<bech32-id>`
- Füge `p`- oder `q`-Tags nur hinzu, wenn dein Client Mention-Benachrichtigungen oder stärkeres Event-Indexing will
- Gehe nicht davon aus, dass jede Inline-Referenz automatisch eine Reply-Beziehung werden sollte. Die Spezifikation überlässt diese Entscheidung dem Client

---

**Primärquellen:**

- [NIP-27 Specification](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 Encoded Entities)](/de/topics/nip-19/) - Defines the encoding formats used in references

**Erwähnt in:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - nostr-tools fix for hashtag parsing after newlines

**Siehe auch:**
- [NIP-18: Reposts](/de/topics/nip-18/)
- [NIP-19: Bech32-Encoded Entities](/de/topics/nip-19/)
