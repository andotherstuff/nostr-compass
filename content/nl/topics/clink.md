---
title: "CLINK: Common Lightning Interface for Nostr Keys"
date: 2026-06-17
draft: false
categories:
  - Payments
  - Lightning
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
---

CLINK (Common Lightning Interface for Nostr Keys) is een voorgesteld formaat voor betalingsverzoeken waarmee een verzender elke Nostr-gebaseerde identiteit kan betalen via één enkele noffer-interface. Een CLINK noffer codeert de Nostr-publieke sleutel van de ontvanger plus voldoende routeringsmetadata zodat de wallet van de verzender een Lightning-betaling, een on-chain betaling of een toekomstige afwikkelingsprimitief kan opbouwen die naar de ontvanger leidt. De ontvanger publiceert één noffer per identiteit, en verzenders betalen deze zonder te weten of de ontvangende wallet afwikkelt via Lightning, on-chain of een ander kanaal.

## Hoe het werkt

Een CLINK noffer is een gestructureerd betalingsverzoek dat de wallet van de verzender decodeert tot een concrete betalingsinstructie. De noffer bevat:

- De Nostr-publieke sleutel van de ontvanger als canonieke identiteitswortel
- Eén of meer betalingseindpunten (Lightning node-URI, hint voor on-chain adresafleiding, toekomstige kanalen)
- Optionele metadata voor de betaling (memo, bedrag, vervaldatum)
- Een handtekening van de ontvanger die de noffer bindt aan diens Nostr-identiteit

Een verzendende wallet die CLINK ondersteunt, leest de noffer, kiest het kanaal dat hij kan bedienen (een Lightning-only wallet betaalt het Lightning-eindpunt, een multi-rail wallet kiest het goedkoopste pad), en verstuurt de betaling. De wallet van de ontvanger bevestigt ontvangst door het bijbehorende voltooiingsevent te publiceren of op te halen, waarbij de Nostr-publieke sleutel fungeert als duurzame identiteit over alle kanalen heen.

## Waarom een Nostr-gebaseerde interface

LNURL en BOLT-12 bestaan al als formaten voor Lightning-betalingsverzoeken, en Bitcoin heeft een bekend adresformaat voor on-chain afwikkeling. CLINK vervangt geen van beide. Het voegt een laag toe die is verankerd in Nostr-sleutels, zodat een verzender een ontvanger kan aanspreken via diens Nostr-identiteit en de wallet kan bepalen welk onderliggend kanaal wordt gebruikt. Een gebruiker die van Lightning-provider wisselt, een nieuwe mint opent of zijn on-chain wallet migreert, publiceert zijn noffer opnieuw met dezelfde Nostr-sleutel, en verzenders hoeven hun adresboeken niet bij te werken.

Voor Zeus Pay (dat voor elk account een CLINK noffer genereert) betekent dit dat een verzender elke Zeus-gebruiker kan betalen op basis van de Nostr-sleutel alleen. Voor Amethyst's on-chain zap-driver bevestigt de CLINK-verificatiestatemachine dat de ondertekende noffer on-chain overeenkomt met de Nostr pubkey die in het zap-verzoek wordt geclaimd, waarmee een vervalsingsroute tegen niet-ondertekende on-chain zaps wordt gesloten.

## Implementaties

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) levert ondersteuning voor CLINK noffer-betalingen, waarbij Zeus Pay voor elk account een CLINK noffer genereert zodat een verzender elke Zeus-gebruiker kan betalen op basis van de Nostr-sleutel alleen
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) levert een CLINK-driver voor verificatie van on-chain zaps met een verificatiestatemachine en een herverificatie-driver ([PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182))

---

**Primaire bronnen:**
- [Zeus v13.1.0-rc1 release notes](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - CLINK noffer-oplevering
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - Verificatiestatemachine en herverificatie-driver voor NIP-BC on-chain zaps
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - Implementatie van CLINK (Common Lightning Interface for Nostr Keys)
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - Ondersteuning van kotlinx-serialization voor CLINK-protocol DTO's

**Genoemd in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/nl/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27: Zeus v13.1.0-rc1 ships CLINK noffers and queue-less NWC](/nl/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**Zie ook:**
- [NIP-57: Zaps](/nl/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
