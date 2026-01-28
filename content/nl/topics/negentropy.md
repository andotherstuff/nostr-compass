---
title: "Negentropy: Set Reconciliation Protocol"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy is een set reconciliation protocol dat efficiënte synchronisatie mogelijk maakt tussen Nostr-clients en relays door ontbrekende events te identificeren zonder de volledige dataset over te dragen.

## Hoe Het Werkt

In plaats van alle events op te vragen die aan een filter voldoen, stelt negentropy clients in staat om hun lokale event-set te vergelijken met die van een relay en alleen de verschillen te identificeren. Dit wordt bereikt via een multi-round protocol:

1. **Fingerprinting**: Client en relay berekenen elk een fingerprint van hun event-sets
2. **Vergelijking**: Fingerprints worden uitgewisseld en vergeleken
3. **Reconciliatie**: Alleen ontbrekende event ID's worden geïdentificeerd en overgedragen

## Waarom Het Belangrijk Is

Traditionele Nostr-sync gebruikt tijdstempelgebaseerde `since`-filters, die events kunnen missen door:
- Klokdrift tussen client en relay
- Meerdere events met identieke tijdstempels
- Events die buiten volgorde aankomen

Negentropy lost deze problemen op door daadwerkelijke event-sets te vergelijken in plaats van te vertrouwen op tijdstempels.

## Toepassingen

- **DM-Herstel**: Clients kunnen ontbrekende directe berichten detecteren en ophalen, zelfs met oude tijdstempels
- **Feed Sync**: Zorgt voor complete tijdlijnsynchronisatie over relays
- **Offline Sync**: Haalt efficiënt achterstand in na periodes van disconnectie

## Implementatie

Negentropy vereist relay-ondersteuning. Clients implementeren het typisch als een fallback-herstelmechanisme in plaats van standaard REQ-abonnementen te vervangen, en degraderen elegant wanneer relays het protocol niet ondersteunen.

## Gerelateerd

- [NIP-01](/nl/topics/nip-01/) - Basisprotocol
