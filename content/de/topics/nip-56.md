---
title: "NIP-56: Meldungen"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 definiert Meldungs-Events vom Kind `1984`. Sie erlauben Nutzern und Apps, Moderationssignale uber Accounts, Notizen und Blobs zu veroffentlichen, ohne eine einzige gemeinsame Moderationsinstanz zu brauchen.

## Wie es funktioniert

Eine Meldung muss ein `p`-Tag fur den gemeldeten Pubkey enthalten. Wenn sich die Meldung auf ein bestimmtes Event bezieht, muss sie auBerdem ein `e`-Tag fur dieses Event enthalten. Der Meldungstyp steht als dritter Wert im jeweiligen `p`-, `e`- oder `x`-Tag.

## Meldekategorien

- **nudity**: Inhalte fur Erwachsene
- **malware**: Viren, Trojaner, Ransomware und ahnliche Payloads
- **profanity**: beleidigende Sprache und Hassrede
- **illegal**: Inhalte, die moglicherweise gegen Gesetze verstoBen
- **spam**: unerwunschte wiederholte Nachrichten
- **impersonation**: betrugerische Identitatsbehauptungen
- **other**: Verstosse, die nicht in die Kategorien oben passen

Blob-Meldungen verwenden `x`-Tags mit dem Hash des Blobs und konnen ein `server`-Tag mit dem Hosting-Endpunkt enthalten. Damit ist NIP-56 nicht nur fur die Moderation von Notizen und Profilen nutzbar, sondern auch fur Medien.

## Sicherheits- und Vertrauensmodell

Meldungen sind Signale, keine Urteile. Clients konnen sie anhand sozialen Vertrauens, von Moderationslisten oder expliziten Moderatorrollen gewichten. Relays konnen sie ebenfalls lesen, aber die Spezifikation warnt vor vollautomatischer Moderation, weil sich Meldungen leicht manipulieren lassen.

Zusatzliche Klassifikation kann uber NIP-32-`l`- und `L`-Tags hinzugefugt werden. Das ist nutzlich, wenn ein Client ein feineres Moderationsvokabular als die sieben Basistypen braucht.

---

**Primarquellen:**
- [NIP-56 Specification](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Erwahnt in:**
- [Newsletter #10: Project Updates](/en/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**Siehe auch:**
- [NIP-22: Comment](/de/topics/nip-22/)
