---
title: Kind Register
url: /nl/kind-registry/
translationOf: /en/kind-registry.md
translationDate: 2025-12-26
---

Event kinds zijn gehele getallen die Nostr-events categoriseren. Dit register bevat alle gestandaardiseerde kinds met hun beschrijvingen en definierende NIPs.

**Kind-bereiken** (uit [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)):
- **0-999**: Reguliere events (alle versies worden bewaard)
- **1000-9999**: Reguliere events (vervolg)
- **10000-19999**: Vervangbare events (alleen de laatste per pubkey wordt bewaard)
- **20000-29999**: Efemere events (niet opgeslagen, alleen doorgestuurd)
- **30000-39999**: Adresseerbare events (laatste per pubkey + kind + d-tag)

## Kern Events (0-99)

| Kind | Beschrijving | NIP |
|------|-------------|-----|
| 0 | Gebruikersmetadata | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 1 | Korte Tekstnotitie | [10](https://github.com/nostr-protocol/nips/blob/master/10.md) |
| 2 | Relay Aanbevelen (verouderd) | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 3 | Volgt | [02](https://github.com/nostr-protocol/nips/blob/master/02.md) |
| 4 | Versleutelde Directe Berichten | [04](https://github.com/nostr-protocol/nips/blob/master/04.md) |
| 5 | Event Verwijderingsverzoek | [09](https://github.com/nostr-protocol/nips/blob/master/09.md) |
| 6 | Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 7 | Reactie | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 8 | Badge Toekenning | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 9 | Chatbericht | [C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) |
| 10 | Groepschat Discussie Antwoord (verouderd) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 11 | Discussie | [7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) |
| 12 | Groep Discussie Antwoord (verouderd) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 13 | Seal | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 14 | Direct Bericht | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 15 | Bestandsbericht | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 16 | Generieke Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 17 | Reactie op een website | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 20 | Afbeelding | [68](https://github.com/nostr-protocol/nips/blob/master/68.md) |
| 21 | Video Event | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 22 | Korte Portretvideo | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 40 | Kanaal Aanmaken | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 41 | Kanaal Metadata | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 42 | Kanaalbericht | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 43 | Kanaal Bericht Verbergen | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 44 | Kanaal Gebruiker Dempen | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 62 | Verzoek tot Verdwijnen | [62](https://github.com/nostr-protocol/nips/blob/master/62.md) |
| 64 | Schaken (PGN) | [64](https://github.com/nostr-protocol/nips/blob/master/64.md) |

## MLS Encryptie (443-445)

| Kind | Beschrijving | NIP |
|------|-------------|-----|
| 443 | KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 444 | Welkomstbericht | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 445 | Groep Event | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |

## Reguliere Events (1000-9999)

| Kind | Beschrijving | NIP |
|------|-------------|-----|
| 1018 | Poll Antwoord | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1021 | Bod | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1022 | Bodbevestiging | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1040 | OpenTimestamps | [03](https://github.com/nostr-protocol/nips/blob/master/03.md) |
| 1059 | Gift Wrap | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 1063 | Bestandsmetadata | [94](https://github.com/nostr-protocol/nips/blob/master/94.md) |
| 1068 | Poll | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1111 | Commentaar | [22](https://github.com/nostr-protocol/nips/blob/master/22.md) |
| 1222 | Spraakbericht | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1244 | Spraakbericht Commentaar | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1311 | Live Chat Bericht | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 1337 | Code Snippet | [C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) |
| 1617 | Patches | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1618 | Pull Requests | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1619 | Pull Request Updates | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1621 | Issues | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1984 | Rapportage | [56](https://github.com/nostr-protocol/nips/blob/master/56.md) |
| 1985 | Label | [32](https://github.com/nostr-protocol/nips/blob/master/32.md) |
| 2003 | Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 2004 | Torrent Commentaar | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 4550 | Community Post Goedkeuring | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 5000-5999 | Taakverzoek | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 6000-6999 | Taakresultaat | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7000 | Taakfeedback | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7374 | Gereserveerde Cashu Wallet Tokens | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7375 | Cashu Wallet Tokens | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7376 | Cashu Wallet Geschiedenis | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 8000 | Gebruiker Toevoegen | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 8001 | Gebruiker Verwijderen | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 9000-9030 | Groep Controle Events | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 9041 | Zap Doel | [75](https://github.com/nostr-protocol/nips/blob/master/75.md) |
| 9321 | Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 9734 | Zap Verzoek | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9735 | Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9802 | Highlights | [84](https://github.com/nostr-protocol/nips/blob/master/84.md) |

## Vervangbare Events (10000-19999)

| Kind | Beschrijving | NIP |
|------|-------------|-----|
| 10000 | Demplijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10001 | Vastpinlijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10002 | Relay Lijst Metadata | [65](https://github.com/nostr-protocol/nips/blob/master/65.md) |
| 10003 | Bladwijzerlijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10004 | Communitylijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10005 | Openbare chatslijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10006 | Geblokkeerde relayslijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10007 | Zoekrelayslijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10009 | Gebruikersgroepen | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10012 | Favoriete relayslijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10013 | Prive event relaylijst | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 10015 | Interesselijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10019 | Nutzap Mint Aanbeveling | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 10020 | Media volgt | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10030 | Gebruikers emojilijst | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10050 | Relaylijst voor DM's ontvangen | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 10051 | KeyPackage Relayslijst | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 10063 | Gebruikers serverlijst | Blossom |
| 10166 | Relay Monitor Aankondiging | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 10312 | Ruimte Aanwezigheid | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 13194 | Wallet Info | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 13534 | Lidmaatschapslijsten | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 17375 | Cashu Wallet Event | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |

## Authenticatie en Wallet (22000-27999)

| Kind | Beschrijving | NIP |
|------|-------------|-----|
| 22242 | Client Authenticatie | [42](https://github.com/nostr-protocol/nips/blob/master/42.md) |
| 23194 | Wallet Verzoek | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 23195 | Wallet Antwoord | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 24133 | Nostr Connect | [46](https://github.com/nostr-protocol/nips/blob/master/46.md) |
| 24242 | Blobs opgeslagen op mediaservers | Blossom |
| 27235 | HTTP Auth | [98](https://github.com/nostr-protocol/nips/blob/master/98.md) |

## Toegangscontrole (28000-29999)

| Kind | Beschrijving | NIP |
|------|-------------|-----|
| 28934 | Lidmaatschapsverzoek | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28935 | Uitnodigingsverzoek | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28936 | Vertrekverzoek | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |

## Adresseerbare Events (30000-39999)

| Kind | Beschrijving | NIP |
|------|-------------|-----|
| 30000 | Volgsets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30002 | Relaysets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30003 | Bladwijzersets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30004 | Curatiesets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30005 | Videosets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30007 | Kind dempsets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30008 | Profiel Badges | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30009 | Badge Definitie | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30015 | Interessesets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30017 | Kraam aanmaken of bijwerken | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30018 | Product aanmaken of bijwerken | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30019 | Marktplaats UI/UX | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30020 | Product verkocht als veiling | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30023 | Lange-vorm Content | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30024 | Concept Lange-vorm Content | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30030 | Emojisets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30063 | Release artifact sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30078 | Applicatiespecifieke Data | [78](https://github.com/nostr-protocol/nips/blob/master/78.md) |
| 30166 | Relay Ontdekking | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 30267 | App curatiesets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30311 | Live Event | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30312 | Interactieve Ruimte | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30313 | Conferentie Event | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30315 | Gebruikersstatussen | [38](https://github.com/nostr-protocol/nips/blob/master/38.md) |
| 30402 | Geclassificeerde Advertentie | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30403 | Concept Geclassificeerde Advertentie | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30617 | Repository aankondigingen | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30618 | Repository status aankondigingen | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30818 | Wiki artikel | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 30819 | Doorverwijzingen | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 31234 | Concept Event | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 31922 | Datumgebaseerd Agenda Event | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31923 | Tijdgebaseerd Agenda Event | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31924 | Agenda | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31925 | Agenda Event RSVP | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31989 | Handler aanbeveling | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 31990 | Handler informatie | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 34550 | Community Definitie | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 38172 | Cashu Mint Aankondiging | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38173 | Fedimint Aankondiging | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38383 | Peer-to-peer Order events | [69](https://github.com/nostr-protocol/nips/blob/master/69.md) |
| 39000-39009 | Groep metadata events | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 39089 | Starterpakketten | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39092 | Media starterpakketten | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39701 | Web bladwijzers | [B0](https://github.com/nostr-protocol/nips/blob/master/B0.md) |

*Laatst bijgewerkt: december 2025*

Zie de [NIPs repository](https://github.com/nostr-protocol/nips) voor de gezaghebbende bron.
