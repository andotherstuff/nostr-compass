---
title: "NIP-78: App-specifieke gegevens"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78 definieert een standaard evenementkind voor applicaties om willekeurige gegevens namens een gebruiker op te slaan via Nostr-events, waarmee apparaatoverschrijdende statussynchronisatie mogelijk wordt zonder centrale server.

## Hoe het werkt

Het centrale evenementkind is 30078, een geparametriseerd vervangbaar event. De `d`-tag is een applicatiegedefinieerde identificatiestring die de opslagslot beperkt tot een specifieke applicatie en doel.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

Een applicatie publiceert een 30078-event met een unieke `d`-tag (bijvoorbeeld `tamagostrich-pet-state` of `amethyst-settings`) en de JSON of tekstinhoud die moet worden opgeslagen. Omdat 30078 vervangbaar is en afgebakend door de `d`-tag, betekent het bijwerken van opgeslagen toestand het publiceren van een nieuw event met dezelfde `d`-tag; de relay bewaart alleen de meest recente versie.

## Synchronisatie tussen apparaten

Elke client die de publieke sleutel van een gebruiker en de `d`-tag van de applicatie kent, kan de huidige toestand ophalen uit de relay-set van de gebruiker en deze op elk apparaat reconstrueren. De gebruiker is eigenaar van de gegevens omdat ze leven in events ondertekend door hun sleutelpaar, opgeslagen op relays uit hun [NIP-65](/nl/topics/nip-65/)-relaylijst.

## Privé- vs. openbare gegevens

Voor privé-applicatiegegevens kan het inhoudsveld worden versleuteld met [NIP-44](/nl/topics/nip-44/) vóór publicatie, zodat de relay alleen versleutelde tekst opslaat die alleen de sleutelhouder kan ontsleutelen. Openbare applicatiegegevens kunnen onversleuteld worden opgeslagen zodat andere clients ze kunnen lezen en weergeven.

## Inhoudsformaat

NIP-78 laat het inhoudsformaat bewust open; applicaties kiezen hun eigen schema. De gangbare conventie is om `d`-tags te prefixeren met de applicatienaam om botsingen te voorkomen tussen apps die dezelfde relay gebruiken.

## Implementaties

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — huisdierstatussynchronisatie tussen apparaten via `tamagostrich-pet-state` kind:30078-events
- [Wisp](https://github.com/barrydeen/wisp-android) — kind:30078-portemonnee-back-up en apparaatoverschrijdende beveiligingsinstellingensynchronisatie; outbox-abonnementen samengevoegd in één REQ met NIP-78-auteursfilter
- [NosPress](https://github.com/nostrapps/nospress) — CMS-orchestratiestatus opgeslagen in NIP-78-events
- Verschillende Nostr-client-instellingssynchronisatie-implementaties (Amethyst, anderen)

---

**Primaire bronnen:**
- [NIP-78-specificatie](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — productie-implementatie

**Vermeld in:**
- [Newsletter #22: NIP-78 Deep Dive](/nl/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [Newsletter #22: Tamagostrich](/nl/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**Zie ook:**
- [NIP-51: Lijsten](/nl/topics/nip-51/)
- [NIP-44: Versiebeheerde versleuteling](/nl/topics/nip-44/)
- [NIP-65: Relaylijstmetadata](/nl/topics/nip-65/)
