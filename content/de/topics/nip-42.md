---
title: "NIP-42: Authentifizierung von Clients bei Relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 definiert, wie sich Clients bei Relays authentifizieren. Relays können eine Authentifizierung verlangen, um Zugriffskontrolle bereitzustellen, Missbrauch zu verhindern oder bezahlte Relay-Dienste zu implementieren.

## Wie es funktioniert

Der Authentifizierungsablauf beginnt, wenn ein Relay eine `AUTH`-Nachricht an den Client sendet. Diese Nachricht enthält einen Challenge-String, den der Client signieren muss. Der Client erstellt ein kind 22242 Authentifizierungs-Event, das die Challenge enthält, und signiert es mit seinem privaten Schlüssel. Das Relay verifiziert Signatur und Challenge und gewährt dann Zugriff.

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

Die Challenge verhindert Replay-Angriffe. Die Relay-URL in den Tags stellt sicher, dass dasselbe signierte Event nicht bei verschiedenen Relays wiederverwendet werden kann.

## Protokollhinweise

Authentifizierung ist an die Verbindung gebunden. Eine Challenge bleibt für die Dauer der Verbindung gültig oder bis das Relay eine neue sendet. Das signierte Event ist ephemer und darf nicht wie ein normales Event verbreitet werden.

Die Spezifikation definiert außerdem maschinenlesbare Fehler-Präfixe. `auth-required:` bedeutet, dass der Client noch nicht authentifiziert ist. `restricted:` bedeutet, dass er zwar authentifiziert ist, der pubkey für die angeforderte Aktion aber trotzdem keine Berechtigung hat.

## Anwendungsfälle

Bezahlte Relays verwenden NIP-42, um Abonnenten vor der Gewährung des Zugriffs zu verifizieren. Private Relays beschränken Lese- oder Schreibzugriffe auf genehmigte pubkeys. Authentifizierung verbessert auch Rate Limiting, weil Relays Verhalten pro authentifiziertem Schlüssel statt pro IP-Adresse verfolgen können.

Kombiniert mit [NIP-11](/de/topics/nip-11/)-Metadaten können Clients erkennen, ob ein Relay NIP-42 unterstützt, bevor sie geschützte Anfragen versuchen. In der Praxis ist die Unterstützung noch uneinheitlich, deshalb brauchen Clients einen Fallback-Pfad, wenn ein Relay NIP-42 ankündigt, geschützte Events aber falsch behandelt.

---

**Primärquellen:**
- [NIP-42 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**Erwähnt in:**
- [Newsletter #6: Relay Information Documents](/en/newsletters/2026-01-21-newsletter/#relay-information-documents-get-formalized)
- [Newsletter #9: Marmot Relay Status Testing](/en/newsletters/2026-02-11-newsletter/#nip-70-relay-support-critical-for-encrypted-messaging-security)
- [Newsletter #10: Nostr MCP Server](/en/newsletters/2026-02-18-newsletter/#nostr-mcp-server)

**Siehe auch:**
- [NIP-11: Relay-Informationsdokument](/de/topics/nip-11/)
- [NIP-50: Suchfähigkeit](/de/topics/nip-50/)
