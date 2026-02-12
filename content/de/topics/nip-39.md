---
title: "NIP-39: Externe Identitäten in Profilen"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 definiert, wie Benutzer externe Identitätsansprüche mit `i`-Tags an ihre Nostr-Profile anhängen. Diese Tags verknüpfen einen Nostr-pubkey mit Konten auf externen Plattformen wie GitHub, Twitter oder DNS-Domains.

## Funktionsweise

Benutzer veröffentlichen Identitätsansprüche als `i`-Tags. Jeder Tag enthält eine Plattformkennung und eine Beweis-URL, unter der das externe Konto zurück auf den Nostr-pubkey verweist, was eine bidirektionale Verifizierung herstellt:

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

Clients verifizieren Ansprüche, indem sie die Beweis-URL abrufen und prüfen, ob sie den Nostr-pubkey des Benutzers enthält. Das erzeugt ein Netz von Identitätsverknüpfungen ohne zentralisierte Verifizierungsdienste.

## Aktuelle Änderungen

Seit Februar 2026 hat [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) Identitäts-Tags aus kind 0 (Benutzer-Metadaten) Events in ein dediziertes kind 10011 extrahiert. Der Umzug war Teil von vitorpamplonas Kind-0-Schlankheitskampagne, motiviert durch geringe Adoption: fast keine Clients implementierten die `i`-Tag-Verifizierung, trotzdem trug jeder kind 0 Abruf den Overhead mit. Das neue kind 10011 ermöglicht es interessierten Clients, Identitätsansprüche separat abzurufen.

---

**Primärquellen:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**Erwähnt in:**
- [Newsletter #9: NIP-Updates](/de/newsletters/2026-02-11-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-05: DNS-basierte Verifizierung](/de/topics/nip-05/)
