---
title: "NIP-09: Verzoek tot verwijderen van event"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 definieert een manier waarop auteurs kunnen verzoeken om events te verwijderen die zij eerder hebben gepubliceerd. Het is een relay-side deletionsignaal, geen netwerkbrede wisfunctie.

## Hoe Het Werkt

Gebruikers publiceren kind 5-events met verwijzingen naar events die ze willen laten verwijderen. Relays die NIP-09 ondersteunen moeten overeenkomende events van dezelfde auteur niet langer serveren en mogen ze uit de opslag verwijderen.

Verwijdering is een verzoek, geen garantie. Relays kunnen verwijderingsverzoeken negeren, en events kunnen al zijn verspreid naar relays die verwijdering niet ondersteunen. Gebruikers moeten niet op NIP-09 vertrouwen voor het verwijderen van privacygevoelige inhoud.

## Waarom Het Belangrijk Is

NIP-09 geeft clients en relays een gemeenschappelijke manier om uit te drukken: "dit event zou niet langer zichtbaar moeten zijn". Dat is nuttig voor per ongeluk gepubliceerde berichten, rollover van walletstatus en moderatieworkflows. Maar de auteur kan alleen verzoeken om verwijdering van eigen events. Het is geen algemeen takedownmechanisme voor content van derden.

## Afwegingen

Het zwakke punt is verspreiding. Zodra een event is gespiegeld over meerdere relays, wordt verwijdering best-effort. Sommige relays verwijderen het, sommige markeren het als tombstone en sommige blijven het onbeperkt serveren. Clients die verwijdering als definitief presenteren, overschatten wat het protocol garandeert.

Een ander praktisch probleem zijn verwijzingen. Gebruikers en apps kunnen het verwijderde event nog steeds lokaal bewaren, of het elders citeren, zelfs nadat een conforme relay het niet langer serveert.

---

**Primaire bronnen:**
- [NIP-09 Specification](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Vermeld in:**
- [Newsletter #11: NIP-60 Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
