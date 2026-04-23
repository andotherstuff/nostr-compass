---
title: "Marmot Protocol"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot is een protocol voor end-to-end versleutelde groepsberichten op Nostr. Het combineert Nostr's identiteit en relaynetwerk met MLS voor groepssleutelbeheer, forward secrecy en post-compromise security.

## Hoe Het Werkt

Marmot gebruikt Nostr voor identiteit, relaytransport en eventdistributie, en legt daar MLS bovenop voor wijzigingen in groepslidmaatschap en berichtversleuteling. In tegenstelling tot [NIP-17](/nl/topics/nip-17/), dat zich richt op één-op-één berichten, is Marmot gebouwd voor groepen waarin leden in de loop van de tijd toetreden, vertrekken of sleutels roteren.

## Waarom Het Belangrijk Is

MLS geeft Marmot eigenschappen die Nostr's schema's voor directe berichten op zichzelf niet bieden: evolutie van de groepsstatus, semantiek voor het verwijderen van leden en herstel na compromittering via latere sleutelupdates.

Die taakverdeling is het nuttige inzicht. Nostr lost identiteit en transport op in een open netwerk. MLS lost geauthenticeerde groepssleutelafspraak op. Marmot is de lijmlaag tussen die twee.

## Implementatiestatus

Het protocol blijft experimenteel, maar het heeft nu meerdere implementaties en actief gebruik in applicaties. [MDK](https://github.com/marmot-protocol/mdk) is de belangrijkste Rust-referentiestack, [marmot-ts](https://github.com/marmot-protocol/marmot-ts) brengt het model naar TypeScript, en applicaties zoals [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika en Vector gebruiken Marmot-compatibele componenten.

Recent werk heeft zich gericht op hardening en interop. Auditgedreven fixes landden begin 2026, en MIP-03 introduceerde deterministische commit resolution zodat clients kunnen convergeren wanneer gelijktijdige wijzigingen in de groepsstatus via relays met elkaar concurreren.

In april 2026 bracht Amethyst zijn ingebedde MDK in lijn met de MIP-01- en MIP-05-wire formats: [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) voegde VarInt-encoding van TLS-achtige length prefixes en round-trip-validatie tegen MDK-testvectors toe, [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) voegde MIP-00 KeyPackage Relay List-ondersteuning toe, en [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) sloot resterende admin-gate- en media-handling-gaten die door cross-client tests tegen White Noise waren gevonden. [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) corrigeerde MLS commit framing zodat encrypted welcome bytes overeenkomen met de output van mdk-core, en [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) repareerde een outer-layer decryption bug die state divergence tussen co-admins veroorzaakte. De vervolg-PR [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) voegt uitgebreide MLS commit cryptography-validatie toe, en [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) levert `amy`, een CLI-interface voor Marmot- en MLS-groepsoperaties vanuit de implementatie van Amethyst.

MDK merge'de [PR #261](https://github.com/marmot-protocol/mdk/pull/261) om `RequiredCapabilities` van een groep als de LCD van invitee capabilities te berekenen, waarmee mixed-version invites tussen Amethyst en White Noise worden vrijgemaakt, [PR #262](https://github.com/marmot-protocol/mdk/pull/262) om key packages van invitees te parsen voordat de signer van de maker wordt opgeslagen, [PR #264](https://github.com/marmot-protocol/mdk/pull/264) om het SelfUpdate-wire format tussen implementaties te laten convergeren, en [PR #265](https://github.com/marmot-protocol/mdk/pull/265) om een `group_required_proposals` accessor bloot te stellen.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) zit midden in een meerfasige refactor van globale singletons naar `AccountSession`-views per account: [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) zette de `AccountSession`- en `AccountManager`-scaffolding op, en vervolgfases migreerden relay handles, drafts en settings, message ops, group read en write, membership, push notifications, key-package reads, group creation en, vanaf [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), session-scoped event dispatch. [marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) migreert de TypeScript-client naar addressable kind `30443` key packages.

---

**Primaire bronnen:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - MIP-01/MIP-05 wire format alignment
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - Amy CLI

**Vermeld in:**
- [Newsletter #1: News](/nl/newsletters/2025-12-17-newsletter/)
- [Newsletter #1: Releases](/nl/newsletters/2025-12-17-newsletter/)
- [Newsletter #4](/nl/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/nl/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/nl/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Amethyst MIP compliance](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: MDK interop work](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: whitenoise-rs session refactor](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [MLS (Message Layer Security)](/nl/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/nl/topics/mip-05/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
