---
title: "NIP-51: Listen"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 definiert verschiedene Listentypen zum Organisieren von Verweisen auf Events, Benutzer und Inhalte in Nostr.

## Listen-Kinds

- **Kind 10000**: Stummschaltliste (Benutzer, Threads oder Wörter zum Ausblenden)
- **Kind 10001**: Pin-Liste (Events, die im Profil hervorgehoben werden)
- **Kind 30000**: Follow-Sets (kategorisierte Folgelisten)
- **Kind 30003**: Lesezeichen-Sets
- **Kind 30004**: Kuratierungs-Sets (Artikel)
- **Kind 30005**: Video-Sets
- **Kind 30006**: Bilder-Sets
- **Kind 30015**: Interessen-Sets (Hashtags)
- **Kind 30030**: Emoji-Sets

## Struktur

Listen verwenden Tags zum Verweisen auf Inhalte:
- `p`-Tags für Pubkeys
- `e`-Tags für Events
- `a`-Tags für adressierbare Events
- `t`-Tags für Hashtags
- `word`-Tags für stummgeschaltete Wörter

## Öffentlich vs. Privat

Listen können öffentliche Tags (für jeden sichtbar) und verschlüsselten Inhalt (privat) haben. Private Elemente werden mit NIP-44 verschlüsselt und im `content`-Feld des Events gespeichert. Die Verschlüsselung verwendet die eigenen Schlüssel des Autors (Verschlüsselung an sich selbst).

Dies ermöglicht Funktionen wie öffentliche Lesezeichen mit privaten Notizen oder eine Stummschaltliste, bei der stummgeschaltete Elemente vor anderen verborgen sind.

## Aktuelle Änderungen

- Hashtag- und URL-Tags aus allgemeinen Lesezeichen entfernt; Hashtags verwenden jetzt Kind 30015
- Kind 30006 für kuratierte Bilder-Sets hinzugefügt

---

**Primärquellen:**
- [NIP-51 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Erwähnt in:**
- [Newsletter #1: NIP-Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: NIP-Updates](/de/newsletters/2025-12-24-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-02: Folgeliste](/de/topics/nip-02/)
