---
title: "NIP-77: Negentropy-reconciliatie"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77 definieert hoe Nostr-relays en clients het [Negentropy](/nl/topics/negentropy/)-setreconciliatieprotocol gebruiken om eventsets efficiënt te synchroniseren, waarbij wordt vastgesteld welke events aan elke kant ontbreken zonder de volledige dataset opnieuw te verzenden.

## Hoe het werkt

Negentropy-reconciliatie verloopt via een WebSocket-verbinding met een speciaal berichttype. De client en relay wisselen compacte bereikvingerafdrukken uit over hun gesorteerde eventsets, waarbij ze alleen de bereiken die verschillen verder inperken. Zodra de verschillen zijn geïdentificeerd, worden alleen de ontbrekende event-ID's (en vervolgens de ontbrekende events zelf) overgedragen.

NIP-77 standaardiseert het berichtopmaak zodat elke client en relay die de specificatie implementeert een efficiënte synchronisatiesessie kan onderhandelen. Het protocol gebruikt de berichttypen `NEG-OPEN`, `NEG-MSG` en `NEG-CLOSE` via de bestaande Nostr WebSocket-verbinding.

## Waarom het belangrijk is

Traditionele Nostr-synchronisatie gebruikt op tijdstempel gebaseerde `since`-filters, die events kunnen missen vanwege klokafwijking, events met identieke tijdstempels of events die buiten volgorde aankomen. Negentropy vergelijkt werkelijke eventsets in plaats van op tijdstempels te vertrouwen, wat een aantoonbaar volledige synchronisatie oplevert in aanzienlijk minder round trips dan eenvoudig polling.

Dit is met name nuttig voor:
- Mobiele clients die na offline gaan bijwerken
- Relay-naar-relay-replicatie
- Lokale relay-synchronisatie (zoals in Citrines relay-aggregator)

## Implementaties

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) voegde NIP-77-ondersteuning toe voor efficiënte set-reconciliatiesynchronisatie in het Android-relay-knooppunt
- [strfry](https://github.com/hoytech/strfry) — relay-zijdige Negentropy-ondersteuning
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — client-zijdige Negentropy-implementatie

---

**Primaire bronnen:**
- [NIP-77-specificatie](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Negentropy-protocol](https://github.com/hoytech/negentropy)

**Vermeld in:**
- [Newsletter #22: Citrine v3.0.0-pre1](/nl/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**Zie ook:**
- [Negentropy](/nl/topics/negentropy/)
