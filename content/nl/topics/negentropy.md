---
title: "Negentropy: protocol voor set-reconciliatie"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy is een protocol voor set-reconciliatie waarmee je kunt vaststellen welke events de ene kant heeft en de andere mist, zonder de volledige dataset opnieuw te verzenden.

## Hoe het werkt

In plaats van elk event op te vragen dat aan een filter voldoet, vergelijkt negentropy twee gesorteerde sets en zoomt het alleen in op de bereiken die verschillen. Het protocol wisselt compacte samenvattingen van bereiken uit en valt alleen waar nodig terug op expliciete lijsten met ID's.

1. **Ordening**: Beide kanten sorteren records op timestamp, daarna op ID
2. **Vergelijking van bereiken**: Ze wisselen fingerprints uit voor bereiken van records
3. **Verfijning**: Bereiken met verschillen worden opgesplitst totdat de werkelijk ontbrekende ID's duidelijk zijn

## Waarom het belangrijk is

Traditionele Nostr-sync gebruikt op timestamp gebaseerde `since`-filters, die events kunnen missen door:
- Klokdrift tussen client en relay
- Meerdere events met identieke timestamps
- Events die buiten volgorde aankomen

Negentropy lost deze problemen op door feitelijke event-sets te vergelijken in plaats van op timestamps te vertrouwen.

## Praktisch gebruik

- **DM-herstel**: Clients kunnen ontbrekende directe berichten detecteren en ophalen, zelfs met oude timestamps
- **Feed-sync**: Zorgt voor volledige tijdlijnsynchronisatie tussen relays
- **Offline sync**: Werkt de achterstand efficiënt bij na periodes zonder verbinding

Het relevante implementatiedetail is dat veel clients normale subscriptions niet vervangen door negentropy. Ze gebruiken het als herstelpad. Damus hield bijvoorbeeld de gewone DM-laadstroom aan en voegde negentropy toe bij handmatige refresh om berichten terug te halen die de normale stroom zou missen.

## Afwegingen

Negentropy vereist ondersteuning aan beide kanten en voegt protocolcomplexiteit toe bovenop standaard `REQ`-gebruik. Het is het nuttigst wanneer correctheid zwaarder weegt dan minimale implementatie-inspanning.

In gemengde omgevingen hebben clients nog steeds nette fallback-logica nodig, omdat niet elke relay het protocol ondersteunt.

---

**Primaire bronnen:**
- [Negentropy Protocol Repository](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**Vermeld in:**
- [Nieuwsbrief #6: Damus levert negentropy voor betrouwbare DM-sync](/en/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [Nieuwsbrief #12](/en/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [NIP-01: Basic Protocol Flow](/nl/topics/nip-01/)
