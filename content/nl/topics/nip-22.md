---
title: "NIP-22: Comments"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22 definieert een standaard voor het reageren op elke adresseerbare Nostr-content, waardoor threaded discussies mogelijk zijn op artikelen, video's, kalenderevents en andere adresseerbare events.

## Hoe Het Werkt

Reacties gebruiken kind 1111 events met tags die verwijzen naar de content waarop wordt gereageerd:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "Geweldig artikel!"
}
```

## Tag-Structuur

- **`A` tag**: Verwijst naar het adresseerbare event waarop wordt gereageerd (kind:pubkey:d-tag formaat)
- **`E` tag**: Verwijst naar de root event ID voor threading
- **`K` tag**: Geeft de kind van het root event aan
- **`e` tag**: Verwijst naar bovenliggende reactie voor geneste antwoorden

## Verschil met Kind 1

Hoewel kind 1 notities kunnen antwoorden op andere notities, zijn NIP-22 reacties specifiek ontworpen voor:

- Adresseerbare content (artikelen, video's, kalenderevents)
- Het behouden van duidelijke ouder-kind relaties
- Het mogelijk maken van moderatie en threading op langvormige content

## Toepassingen

- Artikeldiscussies
- Videoreacties
- [NIP-52](/nl/topics/nip-52/) kalenderevent-discussies
- Wiki-pagina overlegpagina's
- Elk adresseerbaar event-type

## Gerelateerd

- [NIP-01](/nl/topics/nip-01/) - Basisprotocol (kind 1 notities)
- [NIP-52](/nl/topics/nip-52/) - Kalenderevents
