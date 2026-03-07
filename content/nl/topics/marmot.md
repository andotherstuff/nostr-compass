---
title: "Marmot Protocol"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Privacy
  - Berichten
---

Marmot is een protocol voor end-to-end versleutelde groepsberichten op Nostr. Het combineert Nostr's identiteit en relaynetwerk met MLS voor groepssleutelbeheer, forward secrecy en post-compromise security.

## Hoe Het Werkt

Marmot gebruikt Nostr voor identiteit, relaytransport en eventdistributie, en legt daar MLS bovenop voor wijzigingen in groepslidmaatschap en berichtversleuteling. In tegenstelling tot [NIP-17](/nl/topics/nip-17/), dat zich richt op één-op-één berichten, is Marmot gebouwd voor groepen waarin leden in de loop van de tijd toetreden, vertrekken of sleutels roteren.

## Waarom Het Belangrijk Is

MLS geeft Marmot eigenschappen die Nostr's schema's voor directe berichten op zichzelf niet bieden: evolutie van de groepsstatus, semantiek voor het verwijderen van leden en herstel na compromittering via latere sleutelupdates.

Die taakverdeling is het nuttige inzicht. Nostr lost identiteit en transport op in een open netwerk. MLS lost geauthenticeerde groepssleutelafspraak op. Marmot is de lijmlaag tussen die twee.

## Implementatiestatus

Het protocol blijft experimenteel, maar heeft nu meerdere implementaties en actief gebruik in applicaties. MDK is de belangrijkste Rust-referentiestack, `marmot-ts` brengt het model naar TypeScript, en applicaties zoals White Noise, Pika en Vector gebruiken Marmot-compatibele componenten.

Recent werk heeft zich gericht op hardening en interop. Auditgedreven fixes landden begin 2026, en MIP-03 introduceerde deterministische commit resolution zodat clients kunnen convergeren wanneer gelijktijdige wijzigingen in de groepsstatus via relays met elkaar concurreren.

---

**Primaire bronnen:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [NIP-104: MLS-based Encrypted Group Chats](/nl/topics/nip-104/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/en/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Nieuwsbrief #4](/en/newsletters/2026-01-07-newsletter/)
- [Nieuwsbrief #7](/en/newsletters/2026-01-28-newsletter/)
- [Nieuwsbrief #12](/en/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [MLS (Message Layer Security)](/nl/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/nl/topics/mip-05/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
