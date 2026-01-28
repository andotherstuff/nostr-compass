---
title: "NIP-42: Authentifizierung von Clients bei Relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 definiert, wie sich Clients bei Relays authentifizieren. Relays können eine Authentifizierung verlangen, um Zugriffskontrolle bereitzustellen, Missbrauch zu verhindern oder bezahlte Relay-Dienste zu implementieren.

## Funktionsweise

Der Authentifizierungsablauf beginnt, wenn ein Relay eine AUTH-Nachricht an den Client sendet. Diese Nachricht enthält einen Challenge-String, den der Client signieren muss. Der Client erstellt ein kind 22242 Authentifizierungs-Event, das die Challenge enthält, und signiert es mit seinem privaten Schlüssel. Das Relay verifiziert die Signatur und Challenge und gewährt dann Zugriff.

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

Die Challenge verhindert Replay-Angriffe: Clients müssen frische Challenges für jeden Authentifizierungsversuch signieren. Die Relay-URL in den Tags stellt sicher, dass Authentifizierungs-Tokens nicht über verschiedene Relays hinweg wiederverwendet werden können.

## Anwendungsfälle

Bezahlte Relays verwenden NIP-42, um Abonnenten vor der Gewährung des Zugriffs zu verifizieren. Nach der Authentifizierung können Relays den Zahlungsstatus oder das Ablaufdatum des Abonnements überprüfen. Private Relays beschränken den Zugriff auf genehmigte pubkeys und schaffen geschlossene Communities oder persönliche Relay-Infrastruktur.

Rate-Limiting wird mit Authentifizierung effektiver. Relays können Anfrageraten pro authentifiziertem pubkey anstatt pro IP-Adresse verfolgen, was Missbrauch verhindert und gleichzeitig legitime Benutzer hinter gemeinsamen IPs unterstützt. Spam-Prävention verbessert sich, wenn Relays für das Veröffentlichen von Events eine Authentifizierung verlangen.

Einige Relays verwenden NIP-42 für Analysen und verfolgen, welche Benutzer auf welche Inhalte zugreifen, ohne zentralisierte Konten zu erfordern. Kombiniert mit [NIP-11](/de/topics/nip-11/)-Metadaten entdecken Clients, ob Relays eine Authentifizierung erfordern, bevor sie Verbindungen versuchen.

---

**Primärquellen:**
- [NIP-42 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentifizierung von Clients bei Relays

**Siehe auch:**
- [NIP-11: Relay-Informationsdokument](/de/topics/nip-11/)
- [NIP-50: Suchfähigkeit](/de/topics/nip-50/)
