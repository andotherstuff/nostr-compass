---
title: "NIP-27 (Textnotiz-Referenzen)"
date: 2026-02-04
description: "NIP-27 definiert, wie Profile, Notizen und andere Entitäten innerhalb von Notizinhalten mit dem nostr: URI-Schema referenziert werden."
---

NIP-27 spezifiziert, wie Referenzen auf Nostr-Entitäten in den Inhalt von Textnotizen eingebettet werden. Referenzen verwenden das `nostr:` URI-Schema, gefolgt von einem bech32-kodierten Identifikator (npub, note, nevent, nprofile, naddr).

## Funktionsweise

Beim Verfassen einer Notiz, die einen anderen Benutzer erwähnt oder auf ein anderes Event verweist, wird die Referenz direkt in den Inhalt eingebettet:

```
Schau dir diesen Beitrag von nostr:npub1... über nostr:note1... an
```

Clients parsen diese Referenzen und rendern sie entsprechend, typischerweise als klickbare Links oder Inline-Profilkarten. Die referenzierten Entitäten werden auch zu den Tags des Events für Indizierung und Benachrichtigungszwecke hinzugefügt.

Der NIP behandelt auch das Parsing von Hashtags. Mit `#` versehene Tags werden extrahiert und zu den `t`-Tags des Events für Suchbarkeit hinzugefügt.

## Referenztypen

- `nostr:npub1...` - Referenz auf ein Benutzerprofil
- `nostr:note1...` - Referenz auf ein bestimmtes Notiz-Event
- `nostr:nevent1...` - Referenz auf ein Event mit Relay-Hinweisen
- `nostr:nprofile1...` - Referenz auf ein Profil mit Relay-Hinweisen
- `nostr:naddr1...` - Referenz auf ein adressierbares Event

## Implementierungen

Alle großen Nostr-Clients implementieren NIP-27:
- Text-Parser extrahieren Referenzen während der Komposition
- Renderer stellen Referenzen als interaktive Elemente dar
- Benachrichtigungssysteme verwenden die zugehörigen Tags

## Primäre Quellen

- [NIP-27 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 Kodierte Entitäten)](/de/topics/nip-19/) - Definiert die in Referenzen verwendeten Kodierungsformate

## Erwähnt in

- [Newsletter #8 (2026-02-04)](/de/newsletters/2026-02-04-newsletter/) - nostr-tools-Fix für Hashtag-Parsing nach Zeilenumbrüchen
