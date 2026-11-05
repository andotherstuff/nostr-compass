---
title: "NIP-31: Omgaan met onbekende event-kinds"
date: 2026-11-04
draft: false
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
categories:
  - NIPs
  - Protocol
---

> **Statuswaarschuwing:** De huidige [NIP-31-specificatie](https://github.com/nostr-protocol/nips/blob/master/31.md) markeert zichzelf als `unrecommended` omdat ze "onnodig opgeblazen" is, en de statusregel luidt draft, unrecommended en optional. Relays bevatten al events die deze conventie gebruiken, dus deze pagina legt uit hoe clients ze lezen. NIP-31 wordt hier niet aanbevolen voor nieuwe protocollen.

NIP-31 definieert een `alt`-tag op het hoogste niveau. De tag bevat een korte samenvatting in platte tekst voor aangepaste event-kinds die niet bedoeld zijn om als gewone tekstnotities gelezen te worden.

## Hoe het werkt {#how-it-works}

De auteur van een event met een aangepaste kind voegt een `alt`-tag toe met een label dat een mens kan lezen. Clients die rond kind 1 zijn gebouwd, hoeven zich niet te abonneren op elke kind die ze niet herkennen. Hun gebruikers kunnen zo'n event toch tegenkomen wanneer een notitie ernaar verwijst, en het label geeft dan enige context, ook al implementeert de client die kind niet.

Tagfragment, geen volledig event:

```
["alt", "<short plaintext summary>"]
```

Een leesbaar label dekt alleen de weergave. Het kan geen stem uitbrengen, geen walletverzoek afhandelen en geen andere native actie van de kind uitvoeren. Voor rijkere interactie verwijst de specificatie naar [NIP-89: Aanbevolen applicatiehandlers](/nl/topics/nip-89/).

## Implementaties {#implementations}

In de [kaart voor onbekende events van noStrudel op commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx) wordt de eerste `alt`-tag getrimd en wordt die het hoofdlabel, met een optionele regel `Using <client>`. Een ontbrekende of lege waarde levert `Unknown event (kind ...)` op, en maximaal drie regels content verschijnen afzonderlijk. Hetzelfde component zet de `client`-tag om via NIP-89-handlertemplates. Het toont een Open-knop wanneer er een deelbaar adres bestaat en `Open in <client>` wanneer een geldige handlerlink wordt gevonden. De uitleg en het doorsturen naar de app zijn aparte bedieningselementen.

[UnknownEventDigest.kt van Amethyst op commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) geeft de voorkeur aan content die het als lopende tekst classificeert en valt terug op `alt`. De parser trimt waarden en neemt de eerste niet-lege `alt`. Daardoor kan een event waarvan de eerste `alt` leeg is hier een ander label krijgen dan in noStrudel. Beide beschrijvingen weerspiegelen de broncode op die commits. Geen van beide bevestigt hoe een uitgebrachte versie zich gedraagt.

## Beperkingen {#limits}

- `alt` is een tag, dus de event-ID en de handtekening die in [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) zijn gedefinieerd, dekken hem. Een geldige handtekening toont aan dat de auteur het label heeft gepubliceerd. Ze toont niet aan dat het label klopt, dus een samenvatting kan misleiden.
- Tags zijn openbaar. Een `alt` op een event met versleutelde content legt de samenvatting bloot en kan onthullen wat de content verbergt.
- Beide bovenstaande eigenschappen komen voort uit de event-envelop van NIP-01. De tekst van NIP-31 zelf noemt ze niet als vereisten.
- Een `alt`-tag op het hoogste niveau is iets anders dan het `alt`-veld voor afbeeldingsbeschrijvingen binnen `imeta`, en renderers parsen ze afzonderlijk.

---

**Primaire bronnen:**
- [NIP-31-specificatie](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [noStrudel embedded-unknown.tsx op commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [Amethyst UnknownEventDigest.kt op commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**Vermeld in:**
- [Nieuwsbrief #47: NIP-verdieping](/nl/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**Zie ook:**
- [NIP-89: Aanbevolen applicatiehandlers](/nl/topics/nip-89/)
- [NIP-73: Externe content-ID's](/nl/topics/nip-73/)
- [NIP-01: Beschrijving van de basisprotocolflow](/nl/topics/nip-01/)
