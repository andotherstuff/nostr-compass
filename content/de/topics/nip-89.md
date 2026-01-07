---
title: "NIP-89: Empfohlene Anwendungs-Handler"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 definiert, wie Anwendungen ihre Fähigkeiten ankündigen können und wie Nutzer Apps empfehlen können, die bestimmte Event-Kinds verarbeiten.

## Event Kinds

- **kind 31990** - Anwendungs-Handler (veröffentlicht von App-Entwicklern)
- **kind 31989** - App-Empfehlung (veröffentlicht von Nutzern)

## Wie es funktioniert

1. **Anwendungen** veröffentlichen Handler-Events, die beschreiben, welche Event-Kinds sie unterstützen und wie Inhalte geöffnet werden
2. **Nutzer** empfehlen Apps, die sie für bestimmte Event-Kinds nutzen
3. **Clients** fragen Empfehlungen ab, um "Öffnen mit..."-Funktionalität für unbekannte Event-Typen anzubieten

## Anwendungs-Handler

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

Die `k`-Tags spezifizieren unterstützte Event-Kinds. URL-Vorlagen verwenden `<bech32>` als Platzhalter für NIP-19-kodierte Entitäten.

## Nutzer-Empfehlung

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

Der `d`-Tag ist der Event-Kind, der empfohlen wird. Mehrere `a`-Tags können verschiedene Apps für verschiedene Plattformen empfehlen.

## Anwendungsfälle

- Apps entdecken, die Langform-Artikel (kind 30023) anzeigen können
- Clients finden, die bestimmte Event-Typen unterstützen
- Cross-Client "Öffnen mit..."-Funktionalität
- Client-Fähigkeiten für Verschlüsselungsunterstützung erkennen

---

**Primäre Quellen:**
- [NIP-89 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Erwähnt in:**
- [Newsletter #4: NIP Deep Dive](/de/newsletters/2026-01-07-newsletter/#nip-44-versionierte-verschluesselung)

**Siehe auch:**
- [NIP-19: Bech32-kodierte Entitäten](/de/topics/nip-19/)
