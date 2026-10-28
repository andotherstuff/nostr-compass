---
title: "NIP-06: Sleutelafleiding uit een mnemonic"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06 beschrijft hoe je een Nostr-sleutelpaar afleidt uit een mnemonic seed phrase. De [huidige officiële NIP-06-tekst](https://github.com/nostr-protocol/nips/blob/master/06.md) is gemarkeerd als draft en optioneel, en bevat deze waarschuwing:

> __Waarschuwing__ `unrecommended`: geef de voorkeur aan één enkele nsec

Deze pagina behandelt NIP-06 omwille van historische compatibiliteit. Het gebruik van seed-afleiding wordt hier niet aanbevolen.

## Hoe het werkt

Volgens de [huidige specificatie](https://github.com/nostr-protocol/nips/blob/master/06.md) wordt BIP39 gebruikt om de mnemonic-woorden te genereren en daaruit een binaire seed af te leiden. Vervolgens leidt BIP32 sleutels af langs het pad `m/44'/1237'/<account>'/0/0`, waarbij 1237 de Nostr-vermelding in SLIP44 is. Een eenvoudige client kan account 0 gebruiken. Wie de accountwaarde verhoogt, krijgt andere sleutels uit dezelfde seed. Twee implementaties reproduceren alleen dezelfde identiteit als ze het eens zijn over de afleidingsstappen en voor het resultaat de juiste coderingen gebruiken.

## Testvectoren

Een [commit van 12 oktober 2023](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b) voegde twee testvectoren toe: de ene opgebouwd uit een mnemonic van 12 woorden, de andere uit een mnemonic van 24 woorden. Elke vector vermeldt de verwachte private key en public key in hex, samen met de bijbehorende nsec- en npub-coderingen. Ontwikkelaars kunnen de vectoren gebruiken om implementaties onderling te controleren. Over het beheer van sleutels zeggen de vectoren niets; ze certificeren geen beveiliging en garanderen geen universele interoperabiliteit.

## Zie ook

- [NIP-01](/nl/topics/nip-01/)

**Primaire bronnen:**

- [NIP-06 (huidig)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [Commit die NIP-06-testvectoren toevoegt (12 oktober 2023)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**Genoemd in:**

- [Nieuwsbrief #46](/nl/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
