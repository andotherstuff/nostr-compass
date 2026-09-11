---
title: "NIP-A3: Betalingsdoelen"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3 definieert een overdraagbare manier waarop een Nostr-account betalingsadressen voor meerdere netwerken en diensten kan publiceren. Een vervangbare kind `10133`-event bevat een of meer `payto`-tags.

## Hoe het werkt

Elke tag heeft de vorm `["payto", "<type>", "<address>"]`. Het type wordt in kleine letters geschreven, zoals `bitcoin`, `lightning` of `monero`. Clients kunnen bekende indelingen valideren en een eigen betalings-URI weergeven wanneer die bestaat. Voor onbekende typen wordt teruggevallen op het `payto:`-URI-schema uit RFC 8905.

De event vermeldt bestemmingen, niet een voltooide betaling of een Nostr-zap. Clients bepalen nog steeds welke betalingstypen ze ondersteunen, hoe ze een adres valideren en hoe duidelijk ze de bestemming tonen voordat ze die aan een wallet doorgeven.

## Implementaties

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041) biedt een optionele overdracht naar een betaalapp wanneer het een compatibel doel herkent.
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) koppelt toegestane doeltypen aan betalings-URI's.
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) valideert Monero-doelen en bevraagt de relays van de auteur.

---

**Primaire bronnen:**
- [NIP-A3-specificatie](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905: het payto-URI-schema](https://www.rfc-editor.org/rfc/rfc8905.html)

**Vermeld in:**
- [Nieuwsbrief #39: NIP-A3-betalingsdoelen bereiken drie clients](/nl/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**Zie ook:**
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
