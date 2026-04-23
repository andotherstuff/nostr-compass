---
title: "NIP-42: Authentication of clients to relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 definiert, wie sich Clients bei Relays authentifizieren. Relays können Authentifizierung verlangen, um Zugriffskontrolle bereitzustellen, Missbrauch zu verhindern oder bezahlte Relay-Dienste zu implementieren.

## Funktionsweise

Der Authentifizierungsablauf beginnt, wenn ein Relay eine `AUTH`-Nachricht an den Client sendet. Diese Nachricht enthält einen Challenge-String, den der Client signieren muss. Der Client erstellt ein kind-22242-Authentifizierungs-Event, das die Challenge enthält, und signiert es mit seinem private key. Das Relay verifiziert Signatur und Challenge und gewährt danach Zugriff.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

Die Challenge verhindert Replay-Angriffe. Die Relay-URL in den Tags verhindert, dass dasselbe signierte Event über verschiedene Relays hinweg wiederverwendet wird.

## Protokollhinweise

Authentifizierung ist verbindungsgebunden. Eine Challenge bleibt für die Dauer der Verbindung gültig oder bis das Relay eine neue sendet. Das signierte Event ist ephemeral und darf nicht wie ein normales Event verbreitet werden.

Die Spezifikation definiert außerdem maschinenlesbare Fehlerpräfixe. `auth-required:` bedeutet, dass der Client noch nicht authentifiziert ist. `restricted:` bedeutet, dass er zwar authentifiziert ist, dieser pubkey aber trotzdem keine Berechtigung für die angeforderte Aktion hat.

## Anwendungsfälle

Bezahlte Relays nutzen NIP-42, um Abonnenten zu verifizieren, bevor sie Zugriff gewähren. Private Relays nutzen es, um Lese- oder Schreibzugriffe auf genehmigte pubkeys zu beschränken. Es verbessert auch Rate Limiting, weil Relays Verhalten pro authentifiziertem Schlüssel statt pro IP-Adresse verfolgen können.

In Kombination mit Metadaten aus [NIP-11](/de/topics/nip-11/) können Clients erkennen, ob ein Relay NIP-42 unterstützt, bevor sie geschützte Queries versuchen. In der Praxis ist die Unterstützung aber weiter uneinheitlich, daher brauchen Clients einen Fallback-Pfad, wenn ein Relay NIP-42 ankündigt, geschützte Events jedoch falsch behandelt.

---

**Primärquellen:**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**Erwähnt in:**
- [Newsletter #6: Relay Information Documents](/de/newsletters/2026-01-21-newsletter/)
- [Newsletter #9: Marmot Relay Status Testing](/de/newsletters/2026-02-11-newsletter/)
- [Newsletter #10: Nostr MCP Server](/de/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Relay AUTH Starts Reaching Real Apps](/en/newsletters/2026-03-11-newsletter/)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
- [NIP-50: Search Capability](/de/topics/nip-50/)
