---
title: "NIP-39: Externe Identitäten in Profilen"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 definiert, wie Nutzer externe Identitätsansprüche mit `i`-Tags an ihre Nostr-Profile anhängen. Diese Tags verknüpfen einen Nostr-pubkey mit Accounts auf externen Plattformen wie GitHub, Twitter, Mastodon oder Telegram.

## Wie es funktioniert

Nutzer veröffentlichen Identitätsansprüche in kind 10011 Events als `i`-Tags. Jedes Tag enthält einen Wert im Format `platform:identity` plus einen Proof-Pointer, mit dem ein Client den Anspruch verifizieren kann:

```json
{
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

Clients rekonstruieren die Proof-URL aus Plattform und Proof-Wert und prüfen dann, ob der externe Post das `npub` des Nutzers enthält. Dadurch bleibt der Anspruch client-übertragbar, ohne einen zentralen Verifizierer zu brauchen.

## Proof-Modell

Der wichtige Punkt ist, dass NIP-39 gleichzeitig die Kontrolle über zwei Identitäten belegt: den Nostr-Key und den externen Account. Wenn eine Seite dieses Belegs wegfällt, wird die Verifizierung schwächer. Ein gelöschter gist oder Tweet macht das historische Event nicht ungültig, entfernt aber den Live-Proof, auf den die meisten Clients angewiesen sind.

Ein weiterer wichtiger Implementierungspunkt ist die Fetch-Strategie. Da diese Ansprüche jetzt außerhalb von kind 0 leben, können Clients selbst entscheiden, ob sie sie nur in der Profildetailansicht, nur für gefolgte Nutzer oder gar nicht anfordern. Das vermeidet zusätzliches Gewicht auf dem ohnehin stark genutzten kind-0-Pfad.

## Aktueller Status

Nach der aktuellen Spezifikation liegen Identitätsansprüche in dedizierten kind 10011 Events statt in kind-0-Metadaten. Diese Trennung entstand aus dem breiteren Versuch, kind-0-Profilabrufe schlanker zu machen.

---

**Primärquellen:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Identitätsansprüche aus kind 0 verschoben

**Erwähnt in:**
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/en/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)

**Siehe auch:**
- [NIP-05: DNS-basierte Verifizierung](/de/topics/nip-05/)
