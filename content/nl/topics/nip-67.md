---
title: "NIP-67: EOSE Completeness Hint"
date: 2026-04-22
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67 is een open voorstel dat het bestaande `EOSE`-bericht uit [NIP-01](/nl/topics/nip-01/) uitbreidt met een optioneel derde element dat aangeeft of de relay elk opgeslagen event heeft afgeleverd dat bij het filter past. Het is bedoeld om de onbetrouwbare heuristiek te vervangen die clients vandaag gebruiken om te bepalen of een subscription volledig is uitgeput of door een relay-side cap is afgebroken.

## Het Probleem

`EOSE` markeert de grens tussen opgeslagen en realtime events, maar bevat geen informatie over volledigheid. In de praktijk hanteren relays een cap per subscription, vaak tussen 300 en 1000 events, onafhankelijk van de `limit` van de client. Een client die de laatste 500 notities opvraagt bij een relay met een cap van 300 krijgt 300 events en een `EOSE`, zonder te kunnen onderscheiden tussen "dit is alles" en "we zijn halverwege gestopt". De huidige workaround is het aantal events te vergelijken met de `limit` van de client en defensief te pagineren, wat zowel events mist wanneer de cap lager is dan de gevraagde limiet als een extra round trip verspilt wanneer de cap een veelvoud is van het werkelijke aantal matches.

Ties op de grens maken dit erger. Pagineren met `until = oldest_created_at` riskeert ofwel gemiste events ofwel dubbele fetches van events die dezelfde oudste timestamp in de batch delen, afhankelijk van hoe de relay timestamps vergelijkt.

## De Wijziging

NIP-67 voegt een optioneel derde element toe aan `EOSE`:

```
["EOSE", "<subscription_id>", "finish"]   // alle overeenkomende opgeslagen events afgeleverd
["EOSE", "<subscription_id>"]             // geen claim over volledigheid (legacy)
```

Alleen het positieve signaal is gespecificeerd. Een relay die NIP-67-ondersteuning adverteert maar de hint weglaat, zegt daarmee dat er meer is. Een relay die geen ondersteuning adverteert, valt terug op de bestaande heuristiek, dus de wijziging is backward compatible met elke huidige client en relay.

Clients die weten dat hun relay NIP-67 ondersteunt, kunnen stoppen met pagineren zodra ze `"finish"` zien, de verplichte extra round trip vermijden wanneer de cap exact overeenkomt met het resultaat en nauwkeurige volledigheid aan de gebruiker tonen.

## Status

Het voorstel staat [open als PR #2317](https://github.com/nostr-protocol/nips/pull/2317) tegen de NIPs-repository.

---

**Primaire bronnen:**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Vermeld in:**
- [Newsletter #19: NIP Updates](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-01: Basic protocol flow](/nl/topics/nip-01/)
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
