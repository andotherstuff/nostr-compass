---
title: "NIP-29: Relay-based Groups"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-04-22
draft: false
categories:
  - Sociaal
  - Groepen
---

NIP-29 definieert relay-gebaseerde groepen, waarbij een relay groepslidmaatschap, permissies en zichtbaarheid van berichten beheert.

## Hoe Het Werkt

Groepen worden geïdentificeerd door een relay-host plus een group id, en de relay is de autoriteit voor lidmaatschap en moderatie. Door gebruikers gemaakte events die naar een groep worden gestuurd, dragen een `h` tag met de group id. Door de relay gegenereerde metadata gebruikt addressable events die zijn ondertekend met de eigen sleutel van de relay.

Het belangrijkste metadata-event is kind 39000, terwijl kinds 39001 tot en met 39003 admins, leden en ondersteunde rollen beschrijven. Moderatieacties verlopen via events in de 9000-reeks zoals `put-user`, `remove-user`, `edit-metadata` en `create-invite`.

## Toegangsmodel

- **private**: Alleen leden kunnen groepsberichten lezen
- **closed**: Join-verzoeken worden genegeerd, tenzij de relay invite-code-afhandeling gebruikt
- **hidden**: De relay verbergt groepsmetadata voor niet-leden, waardoor de groep onvindbaar wordt
- **restricted**: Alleen leden kunnen berichten naar de groep schrijven

Deze tags staan los van elkaar. Een groep kan voor iedereen leesbaar zijn maar alleen voor leden beschrijfbaar, of volledig verborgen zijn voor niet-leden. Dat onderscheid is belangrijk, omdat clients "private" niet als algemene afkorting voor alle toegangsregels moeten behandelen.

## Trust Model

NIP-29 is geen trustless groepsprotocol. De relay die de groep host beslist welke moderatie-events geldig zijn, welke rollen bestaan, of ledenlijsten zichtbaar zijn en of oude of uit hun context gehaalde berichten worden geaccepteerd. Een client kan handtekeningen en tijdlijnverwijzingen verifiëren, maar blijft voor de werkelijke staat van de groep afhankelijk van relaybeleid.

Dat maakt migratie en forks mogelijk, maar niet automatisch. Dezelfde group id kan op verschillende relays bestaan met verschillende geschiedenissen of regels, dus de relay-URL maakt in de praktijk deel uit van de identiteit van de groep.

## Useful Implementation Notes

## Recent Spec Work

- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) en de [Flotilla 1.7.3/1.7.4 release notes](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) van hodlbod stellen kind-9-wrapping van niet-chat-contenttypes voor, zodat roomcontext behouden blijft wanneer die objecten in een groep worden verstuurd.
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) breidt de spec uit met een subgrouphiërarchie zodat een enkele groep meerdere parallelle kanalen kan hosten zonder onafhankelijke groepen op dezelfde relay te hoeven maken.
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) definieert expliciete permissies op het kind `39003` role-event, zodat elke rol een benoemde set van toegestane operaties wordt.

## Implementaties

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) is de primaire NIP-29-client van hodlbod; [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) en [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) brachten kind-9-wrapping, polls, [NIP-46](/nl/topics/nip-46/) login via het Aegis URL scheme, native share support voor space invites, room mentions, image paste vanaf het mobiele clipboard, drafts en video in gesprekken.
- [Wisp](https://github.com/barrydeen/wisp) voegde NIP-29 group configuration voor flags, invites, roles en AUTH-prompts toe in [PR #471](https://github.com/barrydeen/wisp/pull/471) en verstevigde de AUTH-sequencing vóór group `9021`, `9007` en `9009` events in [PR #478](https://github.com/barrydeen/wisp/pull/478).

- Clients moeten de relay-URL behandelen als de host-sleutel van de groep. Een verduidelijking uit januari 2026 maakte dit expliciet in de specificatie en nam onduidelijkheid weg over het gebruik van een pubkey
- De groepsstatus wordt gereconstrueerd uit de moderatiegeschiedenis, terwijl relay-events in de 39000-reeks informatieve momentopnames van die status zijn
- Tijdlijnverwijzingen naar `previous` zijn bedoeld om rebroadcasting buiten context over relay-forks heen te voorkomen, niet alleen om UI-threading te verbeteren

---

**Primaire bronnen:**
- [NIP-29-specificatie](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Verduidelijkte `private`, `closed` en `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Verduidelijkte relay-URL als relay-sleutel
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Voegde `unallowpubkey` en `unbanpubkey` toe
- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) - Kind-9 wrapping for non-chat content
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) - Subgroups spec
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) - Explicit role permissions on kind 39003
- [Flotilla 1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)
- [Wisp PR #471](https://github.com/barrydeen/wisp/pull/471) - NIP-29 group configuration

**Vermeld in:**
- [Newsletter #2: NIP Updates](/nl/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #6: NIP Updates](/nl/newsletters/2026-01-21-newsletter/)
- [Newsletter #11: NIP Updates](/nl/newsletters/2026-02-25-newsletter/)
- [Newsletter #12: NIP Updates](/nl/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Flotilla 1.7.3/1.7.4](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Wisp NIP-29 config](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Updates (subgroups, role permissions)](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
