---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptografie
  - Protocol
  - Berichtenverkeer
  - Privacy
---

Message Layer Security (MLS) is een IETF-protocol voor end-to-end versleutelde groepsberichten. Het biedt forward secrecy en post-compromise security voor groepen waarvan het lidmaatschap in de loop van de tijd kan veranderen.

## Hoe het werkt

MLS gebruikt een boomgebaseerde sleutelovereenkomststructuur met de naam TreeKEM:

1. **Key Packages**: Elke deelnemer publiceert een key package met zijn identiteit en encryptiesleutels
2. **Group State**: Een ratchet tree houdt de cryptografische toestand van de groep bij
3. **Commits**: Leden werken de tree bij wanneer iemand toetreedt, vertrekt of sleutels roteert
4. **Message Encryption**: Inhoud wordt versleuteld met sleutels die zijn afgeleid van het gedeelde groepsgeheim

## Waarom het belangrijk is

MLS lost een probleem op dat pairwise encryptie niet goed oplost: groepslidmaatschap en encryptiestatus coherent houden terwijl leden asynchroon toetreden, vertrekken of sleutels roteren.

De tree-structuur is het praktische inzicht. Updates vereisen niet dat elke deelnemer opnieuw pairwise onderhandelt met alle anderen, waardoor het protocol veel beter schaalt dan ad-hoc groepssleutelschema's.

## Standaardisatie

- **RFC 9420** (juli 2023): Core MLS-protocolspecificatie
- **RFC 9750** (april 2025): MLS-architectuur voor systeemintegratie

## Adoptie in Nostr

Verschillende Nostr-applicaties gebruiken MLS voor beveiligde groepsberichten:

- **KeyChat**: MLS-gebaseerde versleutelde berichtenapp voor mobiel en desktop
- **White Noise**: Privéberichten met MLS en Marmot protocol-integratie
- **Marmot Protocol**: Nostr-extensie die MLS-gebaseerde groepsencryptie biedt

MLS biedt sterkere groepsbeveiligingsgaranties dan alleen [NIP-04](/nl/topics/nip-04/) of [NIP-44](/nl/topics/nip-44/), vooral wanneer het lidmaatschap vaak verandert.

## Afwegingen

MLS is geen volledig berichtenproduct. Applicaties hebben nog steeds identity, transport, spam resistance, opslag en conflict handling rond het protocol nodig.

Daarom voegen Nostr-projecten zoals Marmot extra regels toe boven op MLS. De cryptografie is gestandaardiseerd, maar het omliggende applicatieprotocol blijft belangrijk voor interoperabiliteit.

---

**Primaire bronnen:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Vermeld in:**
- [Nieuwsbrief #3: Releases](/en/newsletters/2025-12-31-newsletter/#releases)
- [Nieuwsbrief #10](/en/newsletters/2026-02-18-newsletter/)
- [Nieuwsbrief #12](/en/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [Marmot Protocol](/nl/topics/marmot/)
- [MIP-05: Privacybeschermende pushmeldingen](/nl/topics/mip-05/)
- [NIP-17: Privé direct messages](/nl/topics/nip-17/)
- [NIP-44: Versleutelde payloads](/nl/topics/nip-44/)
