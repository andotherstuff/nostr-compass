---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
translationOf: /en/topics/nip-59.md
translationDate: 2026-03-11
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 definieert gift wrap, een manier om een event in te kapselen zodat relays en buitenstaanders uit het outer event dat zij ontvangen niet de echte afzender kunnen afleiden.

## Structuur

Een gift-wrapped event heeft drie lagen:

1. **Rumor** - Het doel-event zonder handtekening.
2. **Seal** (kind `13`) - De rumor, versleuteld voor de ontvanger en ondertekend door de echte afzender.
3. **Gift Wrap** (kind `1059`) - De seal, opnieuw versleuteld en ondertekend met een willekeurige eenmalige sleutel.

De seal moet lege tags hebben. De outer gift wrap draagt meestal de `p`-tag van de ontvanger zodat relays het kunnen routeren.

## Wat Het Verbergt

Gift wrap verbergt de afzender voor relays en netwerkwaarnemers omdat het outer event is ondertekend met een wegwerpsleutel. De ontvanger kan de inner seal echter nog steeds ontsleutelen en zien welke langetermijnsleutel die heeft ondertekend. De privacywinst zit dus in bescherming van metadata op de transportlaag, niet in anonimiteit tegenover de ontvanger.

De specificatie raadt ook aan om wrapper-timestamps te randomiseren en, waar mogelijk, relays te gebruiken die authenticatie vereisen en wrapped events alleen aan de bedoelde ontvanger serveren. Zonder dat relaygedrag kan metadata van ontvangers nog steeds uitlekken.

## Operationele Notities

Gift wrap is op zichzelf geen messaging protocol. Andere protocollen, zoals private messaging systems, gebruiken het als bouwsteen.

Relays kunnen ervoor kiezen wrapped events niet lang op te slaan omdat ze publiek weinig nut hebben. De specificatie staat ook proof-of-work toe op de outer wrapper wanneer implementaties extra spamweerstand willen.

## Gebruiksscenario's

- Private direct messages (NIP-17)
- Friends-only notes (NIP-FR proposal)
- Push notification payloads (NIP-9a proposal)
- Elk scenario dat afzenderprivacy tegenover het netwerk vereist

---

**Primaire bronnen:**
- [NIP-59 Specificatie](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Vermeld in:**
- [Nieuwsbrief #8: NIP Deep Dive](/nl/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)
- [Nieuwsbrief #3: December Recap](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #15: Open PRs](/nl/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Zie ook:**
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
