---
title: "NIP-89: Aanbevolen applicatiehandlers"
date: 2026-01-07
translationDate: 2026-03-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 definieert hoe applicaties hun mogelijkheden kunnen aankondigen en hoe gebruikers apps kunnen aanbevelen die specifieke event kinds afhandelen.

## Event Kinds

- **kind 31990** - Application handler (gepubliceerd door app-ontwikkelaars)
- **kind 31989** - App recommendation (gepubliceerd door gebruikers)

## Hoe het werkt

1. **Applicaties** publiceren handler-events die beschrijven welke event kinds ze ondersteunen en hoe content moet worden geopend
2. **Gebruikers** bevelen apps aan die ze gebruiken voor specifieke event kinds
3. **Clients** vragen recommendations op om "open in..." functionaliteit te bieden voor onbekende event types

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

De `k` tags specificeren ondersteunde event kinds. URL-templates gebruiken `<bech32>` als placeholder voor volgens NIP-19 gecodeerde entiteiten.

Hetzelfde handler-event kan meerdere ondersteunde kinds adverteren als ze hetzelfde routeringspatroon delen. Dat houdt app discovery compact en voorkomt dat er voor elk kind een apart handler-event moet worden gepubliceerd wanneer de bestemmingslogica identiek is.

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

De `d` tag is het event kind dat wordt aanbevolen. Meerdere `a` tags kunnen verschillende apps aanbevelen voor verschillende platforms.

## Client Tag

NIP-89 definieert ook een optionele `client` tag die publishing apps aan gewone events kunnen toevoegen. Die legt de clientnaam vast plus een verwijzing naar het handler-event, zodat andere clients kunnen tonen waar een note vandaan kwam of rijkere applicatiemetadata kunnen opzoeken.

Dit heeft privacygevolgen. De spec zegt expliciet dat clients gebruikers moeten laten afmelden, omdat het publiceren van software-identiteit op elk event gebruikspatronen kan onthullen die mensen misschien niet willen blootgeven.

## Use Cases

- Apps ontdekken die longform-artikelen kunnen weergeven (kind 30023)
- Clients vinden die specifieke event types ondersteunen
- Cross-client "open in..." functionaliteit
- Client-capabilities voor encryptieondersteuning detecteren

## Vertrouwens- en veiligheidsnotities

NIP-89 verbetert interoperabiliteit, maar het creëert ook een redirect-oppervlak. Als een client willekeurige handler announcements van niet-vertrouwde relays opvraagt, kan die gebruikers naar kwaadaardige of misleidende applicaties sturen.

Daarom begint de recommendation-flow bij mensen die je volgt. Sociaal gefilterde recommendations zijn niet perfect, maar ze zijn veiliger dan elke gepubliceerde handler als even betrouwbaar behandelen.

---

**Primaire bronnen:**
- [NIP-89-specificatie](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Genoemd in:**
- [Nieuwsbrief #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Nieuwsbrief #12: Damus](/en/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**Zie ook:**
- [NIP-19: Bech32-gecodeerde entiteiten](/nl/topics/nip-19/)
