---
title: "NIP-89: Empfohlene Application Handlers"
date: 2026-01-07
translationOf: /en/topics/nip-89.md
translationDate: 2026-03-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 definiert, wie Anwendungen ihre Fähigkeiten ankündigen können und wie Nutzer Apps empfehlen, die bestimmte Event-Kinds verarbeiten.

## Event-Kinds

- **kind 31990** - Application Handler, veröffentlicht von App-Entwicklern
- **kind 31989** - App-Empfehlung, veröffentlicht von Nutzern

## Funktionsweise

1. **Anwendungen** veröffentlichen Handler-Events, die beschreiben, welche Event-Kinds sie unterstützen und wie Inhalte geöffnet werden
2. **Nutzer** empfehlen Apps, die sie für bestimmte Event-Kinds verwenden
3. **Clients** fragen Empfehlungen ab, um für unbekannte Event-Typen eine Funktion "open in..." anzubieten

## Application Handler

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

Die `k`-Tags geben an, welche Event-Kinds unterstützt werden. URL-Templates verwenden `<bech32>` als Platzhalter für nach NIP-19 kodierte Entitäten.

Dasselbe Handler-Event kann mehrere unterstützte Kinds bewerben, wenn sie dasselbe Routing-Muster teilen. Das hält App-Discovery kompakt und vermeidet ein eigenes Handler-Event pro Kind, wenn die Ziel-Logik identisch ist.

## Empfehlung durch Nutzer

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

Das `d`-Tag ist der empfohlene Event-Kind. Mehrere `a`-Tags können unterschiedliche Apps für verschiedene Plattformen empfehlen.

## Client-Tag

NIP-89 definiert außerdem ein optionales `client`-Tag, das veröffentlichende Apps an gewöhnliche Events anhängen können. Es hält den Client-Namen plus einen Verweis auf das Handler-Event fest, sodass andere Clients sehen können, woher eine Note stammt, oder reichere Anwendungs-Metadaten abrufen können.

Das hat Datenschutzfolgen. Die Spezifikation sagt ausdrücklich, dass Clients Nutzern ein Opt-out geben sollten, weil die Software-Identität an jedem Event Nutzungsgewohnheiten offenlegen kann, die jemand vielleicht nicht preisgeben will.

## Anwendungsfälle

- Apps entdecken, die Longform-Artikel vom kind 30023 darstellen können
- Clients finden, die bestimmte Event-Typen unterstützen
- Client-übergreifende Funktionen vom Typ "open in..."
- Fähigkeiten eines Clients bei der Verschlüsselung erkennen

## Hinweise zu Vertrauen und Sicherheit

NIP-89 verbessert Interoperabilität, schafft aber auch eine Umleitungsfläche. Wenn ein Client beliebige Handler-Ankündigungen von nicht vertrauenswürdigen Relays abfragt, kann er Nutzer zu bösartigen oder irreführenden Anwendungen schicken.

Deshalb beginnt der Empfehlungsfluss mit Menschen, denen du folgst. Sozial gefilterte Empfehlungen sind nicht perfekt, aber sicherer, als jeden veröffentlichten Handler als gleich vertrauenswürdig zu behandeln.

---

**Primärquellen:**
- [NIP-89 Specification](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Erwähnt in:**
- [Newsletter #4: NIP Deep Dive](/de/newsletters/2026-01-07-newsletter/#nip-44-versionierte-verschluesselung)
- [Newsletter #12: Damus](/de/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**Siehe auch:**
- [NIP-19: Bech32-Encoded Entities](/de/topics/nip-19/)
