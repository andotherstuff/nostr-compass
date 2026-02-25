---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 definieert Event Deletion, een mechanisme waarmee gebruikers kunnen verzoeken dat relays hun eerder gepubliceerde events verwijderen.

## Hoe Het Werkt

Gebruikers publiceren kind 5-events die `e`-tags bevatten met verwijzingen naar de event-ID's die ze willen laten verwijderen. Relays die NIP-09 ondersteunen moeten stoppen met het serveren van de gerefereerde events en mogen ze verwijderen uit hun opslag.

Verwijdering is een verzoek, geen garantie. Relays kunnen verwijderingsverzoeken negeren, en events kunnen al zijn verspreid naar relays die verwijdering niet ondersteunen. Gebruikers moeten niet op NIP-09 vertrouwen voor het verwijderen van privacygevoelige inhoud.

## Kernfuncties

- Kind 5 verwijderingsverzoek-events
- Refereer verwijderde events op ID via e-tags
- Optioneel redenveld voor verwijderingscontext
- Relaynaleving is vrijwillig

---

**Primaire bronnen:**
- [NIP-09 Specificatie](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Vermeld in:**
- [Newsletter #11: NIP-60 Deep Dive](/nl/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)

**Zie ook:**
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
