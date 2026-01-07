---
title: "NIP-89: Aanbevolen Applicatie Handlers"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 definieert hoe applicaties hun mogelijkheden kunnen aankondigen en hoe gebruikers apps kunnen aanbevelen die specifieke event kinds afhandelen.

## Event Kinds

- **kind 31990** - Application handler (gepubliceerd door app-ontwikkelaars)
- **kind 31989** - App-aanbeveling (gepubliceerd door gebruikers)

## Hoe Het Werkt

1. **Applicaties** publiceren handler-events die beschrijven welke event kinds ze ondersteunen en hoe content te openen
2. **Gebruikers** bevelen apps aan die ze gebruiken voor specifieke event kinds
3. **Clients** zoeken naar aanbevelingen om "openen in..." functionaliteit te bieden voor onbekende event types

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

De `k` tags specificeren ondersteunde event kinds. URL-templates gebruiken `<bech32>` als placeholder voor NIP-19 gecodeerde entiteiten.

## Gebruikersaanbeveling

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

De `d` tag is de event kind die wordt aanbevolen. Meerdere `a` tags kunnen verschillende apps aanbevelen voor verschillende platformen.

## Toepassingen

- Ontdekken van apps die longform artikelen kunnen weergeven (kind 30023)
- Vinden van clients die specifieke event types ondersteunen
- Cross-client "openen in..." functionaliteit
- Detecteren van client-mogelijkheden voor versleutelingsondersteuning

---

**Primaire bronnen:**
- [NIP-89 Specificatie](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Genoemd in:**
- [Nieuwsbrief #4: NIP Deep Dive](/nl/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)

**Zie ook:**
- [NIP-19: Bech32-Gecodeerde Entiteiten](/nl/topics/nip-19/)
