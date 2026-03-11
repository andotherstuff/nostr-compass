---
title: "NIP-29: Relay-gebaseerde groepen"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-03-11
draft: false
categories:
  - Social
  - Groups
---

NIP-29 definieert relay-gebaseerde groepen, waarbij een relay groepslidmaatschap, permissies en zichtbaarheid van berichten beheert.

## Hoe het werkt

Groepen worden geïdentificeerd door een relay-host plus een group id, en de relay is de autoriteit voor lidmaatschap en moderatie. Door gebruikers gemaakte events die naar een groep worden gestuurd, dragen een `h` tag met de group id. Door de relay gegenereerde metadata gebruikt addressable events die zijn ondertekend met de eigen sleutel van de relay.

Het belangrijkste metadata-event is kind 39000, terwijl kinds 39001 tot en met 39003 admins, leden en ondersteunde rollen beschrijven. Moderatieacties verlopen via events in de 9000-reeks zoals `put-user`, `remove-user`, `edit-metadata` en `create-invite`.

## Toegangsmodel

- **private**: Alleen leden kunnen groepsberichten lezen
- **closed**: Join-verzoeken worden genegeerd, tenzij de relay invite-code-afhandeling gebruikt
- **hidden**: De relay verbergt groepsmetadata voor niet-leden, waardoor de groep onvindbaar wordt
- **restricted**: Alleen leden kunnen berichten naar de groep schrijven

Deze tags staan los van elkaar. Een groep kan voor iedereen leesbaar zijn maar alleen voor leden beschrijfbaar, of volledig verborgen zijn voor niet-leden. Dat onderscheid is belangrijk, omdat clients "private" niet als algemene afkorting voor alle toegangsregels moeten behandelen.

## Vertrouwensmodel

NIP-29 is geen trustless groepsprotocol. De relay die de groep host beslist welke moderatie-events geldig zijn, welke rollen bestaan, of ledenlijsten zichtbaar zijn en of oude of uit hun context gehaalde berichten worden geaccepteerd. Een client kan handtekeningen en tijdlijnverwijzingen verifiëren, maar blijft voor de werkelijke staat van de groep afhankelijk van relaybeleid.

Dat maakt migratie en forks mogelijk, maar niet automatisch. Dezelfde group id kan op verschillende relays bestaan met verschillende geschiedenissen of regels, dus de relay-URL maakt in de praktijk deel uit van de identiteit van de groep.

## Nuttige implementatienotities

- Clients moeten de relay-URL behandelen als de host-sleutel van de groep. Een verduidelijking uit januari 2026 maakte dit expliciet in de specificatie en nam onduidelijkheid weg over het gebruik van een pubkey
- De groepsstatus wordt gereconstrueerd uit de moderatiegeschiedenis, terwijl relay-events in de 39000-reeks informatieve momentopnames van die status zijn
- Tijdlijnverwijzingen naar `previous` zijn bedoeld om rebroadcasting buiten context over relay-forks heen te voorkomen, niet alleen om UI-threading te verbeteren

---

**Primaire bronnen:**
- [NIP-29-specificatie](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Verduidelijkte `private`, `closed` en `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Verduidelijkte relay-URL als relay-sleutel
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Voegde `unallowpubkey` en `unbanpubkey` toe

**Vermeld in:**
- [Nieuwsbrief #2: NIP Updates](/nl/newsletters/2025-12-24-newsletter/#nip-updates)
- [Nieuwsbrief #3: Decemberoverzicht](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #6: NIP Updates](/nl/newsletters/2026-01-21-newsletter/#nip-updates)
- [Nieuwsbrief #11: NIP Updates](/nl/newsletters/2026-02-25-newsletter/#nip-updates)
- [Nieuwsbrief #12: NIP Updates](/nl/newsletters/2026-03-04-newsletter/#nip-updates)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
