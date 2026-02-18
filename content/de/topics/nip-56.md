---
title: "NIP-56: Meldungen"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 definiert einen Meldemechanismus über kind-1984-Events und ermöglicht Nutzern und Anwendungen, anstößige Inhalte im Nostr-Netzwerk zu kennzeichnen.

## Funktionsweise

Ein Nutzer veröffentlicht ein kind-1984-Event mit einem `p`-Tag, das den gemeldeten pubkey referenziert. Beim Melden einer spezifischen Notiz referenziert ein `e`-Tag die Notiz-ID. Beide Tags akzeptieren einen dritten Parameter, der die Verstoßkategorie angibt.

## Meldekategorien

- **nudity**: Erwachseneninhalte
- **malware**: Viren, Trojaner, Ransomware
- **profanity**: Anstößige Sprache und Hassrede
- **illegal**: Möglicherweise rechtswidrige Inhalte
- **spam**: Unerwünschte Wiederholungsnachrichten
- **impersonation**: Betrügerische Identitätsansprüche
- **other**: Verstöße, die in keine der obigen Kategorien passen

## Verhalten von Clients und Relays

Clients können Meldungen von gefolgten Nutzern für Moderationsentscheidungen verwenden, etwa zum Unschärfen von Inhalten, wenn mehrere vertrauenswürdige Kontakte sie kennzeichnen. Relays sollten automatische Moderation über Meldungen aufgrund von Manipulationsrisiken vermeiden; Meldungen vertrauenswürdiger Moderatoren können stattdessen manuelle Durchsetzung informieren. Zusätzliche Klassifikation wird durch NIP-32 `l`- und `L`-Tags unterstützt.

---

**Primärquellen:**
- [NIP-56-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Erwähnt in:**
- [Newsletter #10: Projekt-Updates](/de/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-vorbereitung)

**Siehe auch:**
- [NIP-22: Kommentar](/de/topics/nip-22/)
