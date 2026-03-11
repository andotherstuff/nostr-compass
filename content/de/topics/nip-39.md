---
title: "NIP-39: Externe Identitäten in Profilen"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 definiert, wie Nutzer externe Identitätsansprüche mit `i`-Tags an ihre Nostr-Profile anhängen. Diese Tags verknüpfen einen Nostr-pubkey mit Accounts auf externen Plattformen wie GitHub, Twitter, Mastodon oder Telegram.

## Wie es funktioniert

Nutzer veröffentlichen Identitätsansprüche in kind-10011-Events als `i`-Tags. Jedes Tag enthält einen Wert `platform:identity` plus einen Proof-Pointer, mit dem ein Client den Anspruch verifizieren kann:

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Clients rekonstruieren die Proof-URL aus Plattform und Proof-Wert und prüfen dann, ob der externe Post das `npub` des Nutzers enthält. Dadurch bleibt der Anspruch über Clients hinweg portabel, ohne einen zentralen Verifizierer zu benötigen.

## Proof-Modell

Der wichtige Punkt ist, dass NIP-39 gleichzeitig die Kontrolle über zwei Identitäten beweist: den Nostr-Schlüssel und den externen Account. Wenn eine Seite dieses Belegs wegfällt, wird die Verifizierung schwächer. Ein gelöschter gist oder Tweet macht das historische Event nicht ungültig, entfernt aber den Live-Proof, auf den die meisten Clients angewiesen sind.

Ein weiterer nützlicher Implementierungspunkt ist die Fetch-Strategie. Da Ansprüche nun außerhalb von kind 0 leben, können Clients entscheiden, ob sie diese nur in Profildetailansichten, nur für gefolgte Nutzer oder gar nicht anfordern. Das vermeidet zusätzliche Last auf dem ohnehin stark genutzten kind-0-Pfad.

## Implementierungen

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - Veröffentlicht externe Identitäten als dedizierte kind-10011-Events
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Ergänzt eine explizite kind-10011-Registry-Referenz zum NIP-Set

## Aktueller Status

Nach der aktuellen Spezifikation liegen Identitätsansprüche in dedizierten kind-10011-Events statt in kind-0-Metadaten. Diese Trennung entstand aus dem breiteren Versuch, Abrufe von kind-0-Profilen schlanker zu machen.

---

**Primärquellen:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Verschob Identitätsansprüche aus kind 0
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Ergänzte explizite kind-10011-Referenz

**Erwähnt in:**
- [Newsletter #9: NIP Updates](/de/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/de/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)
- [Newsletter #13: NIP Updates](/de/newsletters/2026-03-11-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-05: DNS-Based Verification](/de/topics/nip-05/)
