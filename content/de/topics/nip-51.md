---
title: "NIP-51: Listen"
date: 2025-12-17
translationOf: /en/topics/nip-51.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 definiert Listen-Events zum Organisieren von Benutzern, Events, Relays, Hashtags und anderen Referenzen. Es ist das wichtigste Protokoll fur Lesezeichen, Stummschaltlisten, Follow-Sets, Relay-Sets und mehrere andere vom Nutzer kuratierte Sammlungen.

## Standardlisten und Sets

- **Standardlisten** verwenden ersetzbare Event-Kinds wie Kind `10000` fur Stummschaltlisten, Kind `10003` fur Lesezeichen und Kind `10007` fur Search Relays.
- **Sets** verwenden adressierbare Kinds mit `d`-Tags, etwa Kind `30000` fur Follow-Sets, Kind `30003` fur Bookmark-Sets und Kind `30030` fur Emoji-Sets.

Diese Unterscheidung ist fur das Verhalten von Clients wichtig. Standardlisten implizieren eine kanonische Liste pro Nutzer und Kind. Sets implizieren viele benannte Sammlungen, deshalb mussen Clients das `d`-Tag jeder Liste erhalten.

## Struktur

Listen verwenden Tags, um Inhalte zu referenzieren:

- `p`-Tags fur Pubkeys
- `e`-Tags fur Events
- `a`-Tags fur adressierbare Events
- `t`-Tags fur Hashtags
- `word`-Tags fur stummgeschaltete Worter
- `relay`-Tags fur Relay-URLs in relay-orientierten List-Kinds

Einige List-Kinds erlauben engere Tag-Formen als andere. Relay-orientierte Listen verwenden zum Beispiel `relay`-Tags, wahrend Lesezeichen auf Notizen oder adressierbare Events zeigen sollen. Clients, die jede NIP-51-Liste als beliebige Sammlung freier Tags behandeln, verlieren Interoperabilitat.

## Offentlich vs. privat

Listen konnen offentliche Tags und private Eintrage enthalten. Private Eintrage werden als JSON-Array serialisiert, das die Struktur von `tags` spiegelt, verschlusselt und im Event-`content` gespeichert. Die aktuelle Spezifikation verwendet fur dieses Self-Encryption-Modell NIP-44, NIP-04 bleibt nur als Legacy-Kompatibilitat.

Diese Trennung erlaubt es Nutzern, eine sichtbare Listenhulle zu veroffentlichen und einzelne Eintrage trotzdem zu verbergen. Eine Lesezeichenliste kann offentlich sein, wahrend private Notizen oder private Lesezeichen im verschlusselten Inhalt bleiben.

## Nutzliche Kinds

- **Kind 10000**: Stummschaltliste fur Pubkeys, Threads, Hashtags und stummgeschaltete Worter
- **Kind 10003**: Lesezeichen fur Notizen und adressierbare Inhalte
- **Kind 10007**: Bevorzugte Search Relays
- **Kind 30002**: Relay-Sets fur benannte Relay-Gruppen
- **Kind 30006**: Picture Curation Sets
- **Kind 39089**: Starter Packs fur teilbare Follow-Bundles

Jungere Anderungen an der Spezifikation haben Hashtags aus generischen Lesezeichen entfernt und in Interest Sets verschoben. AuBerdem wurde Kind `30006` fur Picture Curation hinzugefugt. Beides verringert Mehrdeutigkeit bei der Interpretation von Listeninhalten durch Clients.

---

**Primarquellen:**
- [NIP-51 Specification](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Erwahnt in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-13-newsletter/#nip-deep-dive-nip-51-and-nip-65)
- [Newsletter #8: njump Adds NIP-51 Support](/en/newsletters/2026-02-04-newsletter/#njump)

**Siehe auch:**
- [NIP-02: Follow List](/de/topics/nip-02/)
