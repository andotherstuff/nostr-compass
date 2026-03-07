---
title: "NIP-87: Ecash Mint Vindbaarheid"
date: 2026-01-07
translationDate: 2026-03-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 definieert hoe ecash mints (Cashu en Fedimint) zichzelf kunnen aankondigen op Nostr, en hoe gebruikers mints aan anderen kunnen aanbevelen.

## Event Kinds

- **kind 38172** - Cashu mint-aankondiging (gepubliceerd door mint-operators)
- **kind 38173** - Fedimint-aankondiging (gepubliceerd door mint-operators)
- **kind 38000** - Mint-aanbeveling (gepubliceerd door gebruikers)

## Hoe Het Werkt

1. **Mint-operators** publiceren de URL van hun mint, ondersteunde functies en het netwerk (mainnet/testnet)
2. **Gebruikers** die een mint vertrouwen publiceren aanbevelingen met optionele reviews
3. **Andere gebruikers** zoeken aanbevelingen op van mensen die ze volgen om vertrouwde mints te ontdekken

## Cashu Mint-aankondiging

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

De `nuts` tag geeft ondersteunde NUTs weer (Notation, Usage, and Terminology specs voor Cashu).

De `d` tag hoort de Cashu-pubkey van de mint te zijn. Die geeft clients een stabiele identifier voor discovery, ook als de mint later metadata wijzigt of de aankondiging opnieuw publiceert.

## Gebruikersaanbevelingen

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

Gebruikers kunnen reviews opnemen in het `content` veld en verwijzen naar specifieke mint-aankondigingsevents.

Aanbevelingsevents zijn parameterized replaceable events. Dat is nuttig omdat een gebruiker een aanbeveling kan herzien, de reviewtekst kan bijwerken of kan stoppen met het aanbevelen van een mint zonder meerdere verouderde aanbevelingsevents achter te laten.

## Vertrouwensmodel

NIP-87 vertelt clients niet welke mint veilig is. Het geeft hen een manier om door operators gepubliceerde metadata te combineren met sociale aanbevelingen van accounts die de gebruiker al vertrouwt.

Dat onderscheid is belangrijk omdat directe queries naar mint-aankondigingsevents veel ruis of kwaadwillende resultaten kunnen opleveren. De spec waarschuwt clients expliciet om spampreventiemaatregelen of relays van hoge kwaliteit te gebruiken wanneer ze sociale aanbevelingen omzeilen en aankondigingen direct opvragen.

## Interop-opmerkingen

Cashu en Fedimint gebruiken verschillende announcement kinds omdat ze verschillende verbindingsgegevens tonen. Cashu-aankondigingen publiceren mint-URLs en ondersteunde NUTs, terwijl Fedimint-aankondigingen invite codes en ondersteunde federation modules publiceren. Een wallet die beide ondersteunt moet beide formats kunnen parsen.

---

**Primaire bronnen:**
- [NIP-87 Specificatie](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Genoemd in:**
- [Nieuwsbrief #4: Releases](/en/newsletters/2026-01-07-newsletter/#releases)
- [Nieuwsbrief #7: Zeus](/en/newsletters/2026-01-28-newsletter/)

**Zie ook:**
- [Cashu](/nl/topics/cashu/)
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
