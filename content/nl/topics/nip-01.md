---
title: "NIP-01: Basisprotocol"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01 definieert het fundamentele protocol voor Nostr, en stelt de datastructuren en communicatiepatronen vast waarop alle andere NIPs voortbouwen.

## Events

Events zijn het enige objecttype in Nostr. Elk stukje data, van een profielupdate tot een tekstpost tot een reactie, wordt gerepresenteerd als een event met deze structuur:

- **id**: SHA256-hash van het geserialiseerde event (unieke identifier)
- **pubkey**: De publieke sleutel van de maker (32-byte hex, secp256k1)
- **created_at**: Unix-tijdstempel
- **kind**: Integer die het eventtype categoriseert
- **tags**: Array van arrays voor metadata
- **content**: De payload (interpretatie hangt af van kind)
- **sig**: Schnorr-handtekening die authenticiteit bewijst

## Kinds

Kinds bepalen hoe relays events opslaan en afhandelen:

- **Reguliere events** (1, 2, 4-44, 1000-9999): Normaal opgeslagen, alle versies behouden
- **Vervangbare events** (0, 3, 10000-19999): Alleen de laatste per pubkey wordt behouden
- **Vluchtige events** (20000-29999): Niet opgeslagen, alleen doorgestuurd naar abonnees
- **Adresseerbare events** (30000-39999): Laatste per pubkey + kind + `d` tag combinatie

Kernkinds omvatten: 0 (gebruikersmetadata), 1 (tekstnota), 3 (volglijst).

## Client-Relay Communicatie

Clients communiceren met relays via WebSocket-verbindingen met JSON-arrays:

**Client naar relay:**
- `["EVENT", <event>]` - Publiceer een event
- `["REQ", <sub-id>, <filter>, ...]` - Abonneer op events
- `["CLOSE", <sub-id>]` - Beëindig een abonnement

**Relay naar client:**
- `["EVENT", <sub-id>, <event>]` - Lever overeenkomend event
- `["EOSE", <sub-id>]` - Einde van opgeslagen events (nu live streaming)
- `["OK", <event-id>, <true|false>, <message>]` - Accepteer/weiger bevestiging
- `["NOTICE", <message>]` - Leesbaar bericht

## Filters

Filters specificeren welke events opgehaald moeten worden, met velden inclusief: `ids`, `authors`, `kinds`, `#e`/`#p`/`#t` (tagwaarden), `since`/`until`, en `limit`. Voorwaarden binnen een filter gebruiken AND-logica; meerdere filters in een `REQ` combineren met OR-logica.

---

**Primaire bronnen:**
- [NIP-01 Specificatie](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Diepgaand](/nl/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**Zie ook:**
- [NIP-19: Bech32-gecodeerde Entiteiten](/nl/topics/nip-19/)
- [Kind Register](/nl/kind-registry/)
