---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - Cryptografie
  - Protocol
  - Berichtenverkeer
  - Privacy
---

Message Layer Security (MLS) is een IETF-gestandaardiseerd protocol voor end-to-end versleutelde groepsberichten. Het biedt efficiënte sleuteluitwisseling met forward secrecy en post-compromise beveiliging voor groepen van twee tot duizenden deelnemers.

## Hoe het werkt

MLS gebruikt een boomgebaseerde sleutelovereenkomststructuur genaamd TreeKEM:

1. **Sleutelpakketten**: Elke deelnemer publiceert een sleutelpakket met zijn identiteit en encryptiesleutels
2. **Groepsstatus**: Een ratchet-boom onderhoudt de cryptografische status van de groep
3. **Commits**: Leden werken de boom bij bij toetreden, verlaten of roteren van sleutels
4. **Berichtversleuteling**: Inhoud wordt versleuteld met sleutels afgeleid van het gedeelde groepsgeheim

## Belangrijke beveiligingseigenschappen

- **Forward secrecy**: Eerdere berichten blijven veilig, zelfs als huidige sleutels worden gecompromitteerd
- **Post-compromise beveiliging**: Toekomstige berichten worden weer veilig na sleutelrotatie
- **Lidmaatschapsauthenticatie**: Alle groepsleden worden cryptografisch geverifieerd
- **Asynchrone werking**: Leden kunnen toetreden/verlaten zonder dat alle deelnemers online zijn
- **Schaalbaarheid**: Efficiënt voor groepen tot 50.000 deelnemers

## Standaardisatie

- **RFC 9420** (juli 2023): Core MLS-protocolspecificatie
- **RFC 9750** (april 2025): MLS-architectuur voor systeemintegratie

## Adoptie in Nostr

Verschillende Nostr-applicaties gebruiken MLS voor beveiligde groepsberichten:

- **KeyChat**: MLS-gebaseerde versleutelde berichtenapp voor mobiel en desktop
- **White Noise**: Privéberichten met MLS en Marmot-protocolintegratie
- **Marmot Protocol**: Nostr-extensie die MLS-gebaseerde groepsversleuteling biedt

MLS biedt sterkere beveiligingsgaranties dan NIP-04 of NIP-44 alleen, met name voor groepschats waar leden dynamisch toetreden en verlaten.

## Industrieadoptie

Buiten Nostr wordt MLS geadopteerd door:
- Google Messages (RCS met MLS via GSMA Universal Profile 3.0)
- Apple Messages (RCS-ondersteuning aangekondigd voor MLS)
- Cisco WebEx, Wickr, Matrix

---

**Primaire bronnen:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Vermeld in:**
- [Newsletter #3: Releases](/nl/newsletters/2025-12-31-newsletter/#releases)

**Zie ook:**
- [Marmot Protocol](/nl/topics/marmot/)
- [MIP-05: Privacybeschermende Pushmeldingen](/nl/topics/mip-05/)
- [NIP-17: Privé Directe Berichten](/nl/topics/nip-17/)
- [NIP-44: Versleutelde Payloads](/nl/topics/nip-44/)
