---
title: "NIP-01: Basic Protocol"
date: 2025-12-17
translationOf: /en/topics/nip-01.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
---

NIP-01 definieert het basismodel voor events en het relayprotocol waarop de rest van Nostr voortbouwt. Als een client, relay of library Nostr spreekt, begint het hier.

## Hoe Het Werkt

Events zijn het enige objecttype in Nostr. Profielen, notities, reacties, relaylijsten en veel applicatiespecifieke payloads gebruiken allemaal dezelfde envelope met zeven velden:

- **id**: SHA256-hash van het geserialiseerde event (unieke identifier)
- **pubkey**: De publieke sleutel van de maker (32-byte hex, secp256k1)
- **created_at**: Unix-tijdstempel
- **kind**: Integer die het eventtype categoriseert
- **tags**: Array van arrays voor metadata
- **content**: De payload (de interpretatie hangt af van kind)
- **sig**: Schnorr-handtekening die authenticiteit bewijst

De event-`id` is de SHA256-hash van de geserialiseerde eventdata, geen willekeurige identifier. Dat is in de praktijk belangrijk: als je een veld wijzigt, inclusief de volgorde van tags of een tijdstempel, krijg je een ander event en is een nieuwe handtekening nodig.

## Kinds

Kinds bepalen hoe relays events opslaan en afhandelen:

- **Reguliere events** (1, 2, 4-44, 1000-9999): Normaal opgeslagen, alle versies blijven bewaard
- **Vervangbare events** (0, 3, 10000-19999): Alleen de laatste per pubkey blijft bewaard
- **Efemere events** (20000-29999): Niet opgeslagen, alleen doorgestuurd naar abonnees
- **Adresseerbare events** (30000-39999): Laatste per combinatie van pubkey + kind + `d`-tag

Belangrijke kernkinds zijn 0 (gebruikersmetadata), 1 (tekstnotitie) en 3 (volglijst).

## Client-relay-communicatie

Clients communiceren met relays via WebSocket-verbindingen met JSON-arrays:

**Client naar relay:**
- `["EVENT", <event>]` - Publiceer een event
- `["REQ", <sub-id>, <filter>, ...]` - Abonneer je op events
- `["CLOSE", <sub-id>]` - Beëindig een abonnement

**Relay naar client:**
- `["EVENT", <sub-id>, <event>]` - Lever een overeenkomend event af
- `["EOSE", <sub-id>]` - Einde van opgeslagen events, daarna volgt live streaming
- `["OK", <event-id>, <true|false>, <message>]` - Acceptatie- of afwijzingsbevestiging
- `["NOTICE", <message>]` - Menselijk leesbaar bericht

In de praktijk veranderen de meeste hogere NIPs de transportlaag niet. Ze definiëren nieuwe event kinds, tags of interpretatieregels, terwijl ze nog steeds dezelfde `EVENT`-, `REQ`- en `CLOSE`-berichten uit NIP-01 gebruiken.

## Filters

Filters geven aan welke events opgehaald moeten worden, met velden zoals `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`, `since`, `until` en `limit`. Voorwaarden binnen een filter gebruiken AND-logica. Meerdere filters binnen een `REQ` gebruiken OR-logica.

## Interop-opmerkingen

Twee details veroorzaken veel implementatiebugs. Ten eerste moeten clients relayresponses behandelen als uiteindelijk consistent, niet als globaal geordend, omdat verschillende relays verschillende subsets van de geschiedenis kunnen teruggeven. Ten tweede betekenen vervangbare en adresseerbare events dat "latest" deel is van het protocolmodel, dus clients hebben deterministische regels nodig om het nieuwste geldige event te kiezen wanneer meerdere relays het oneens zijn.

---

**Primaire bronnen:**
- [NIP-01-specificatie](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Vermeld in:**
- [Newsletter #1: NIP Deep Dive](/nl/newsletters/2025-12-17-newsletter/)
- [Newsletter #19: NIP-67 EOSE completeness hint proposal](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-19: Bech32-gecodeerde entiteiten](/nl/topics/nip-19/)
- [Kind-register](/en/kind-registry/)
