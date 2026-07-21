---
title: "Concord Protocol"
date: 2026-07-15
draft: false
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
categories:
  - Protocol
  - Messaging
---

Concord is een open, MIT-gelicentieerd protocol voor end-to-end versleutelde gemeenschappen en kanalen op Nostr, gedefinieerd door de [CORD-01 tot en met CORD-07-specificaties](https://github.com/concord-protocol/concord). [Vector](https://github.com/VectorPrivacy/Vector) nam het vanaf v0.4.0 over als standaardtransport voor zijn Groepschat-functie en noemde het in de eigen release notes "ons eigen berichtenprotocol", maar de specificatie zelf wordt los van Vector gepubliceerd en heeft al onafhankelijke implementaties.

## Hoe het werkt

Concord splitst wat een Discord-achtige gemeenschapsserver normaal doet op in stukken die niemand hoeven te vertrouwen: relay's bewaren alleen versleutelde blobs geadresseerd aan roterende labels, het bezit van de sleutel van een ruimte maakt iemand lid, en het gezag over rollen, kicks en bans is een ondertekende ledenlijst geworteld in de identiteit van de eigenaar die elke client lokaal verifieert in plaats van erop te vertrouwen dat een server het handhaaft. Elk blijvend event rijdt op dezelfde envelop van drie lagen: een kind 1059 wrap ondertekend met de eigen afgeleide streamsleutel van het vlak, met daarin een seal ondertekend met de echte sleutel van de auteur, met daarin een niet-ondertekende rumor die het functionele event draagt. Een chatbericht-rumor is een gewoon kind 9-event:

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

Controle-, chat- en gastenboekverkeer krijgen elk hun eigen [NIP-59](/nl/topics/nip-59/) gift-wrapped vlak, zodat een relay die alle drie bewaart zonder de ruimtesleutel nog steeds een controlebericht niet kan onderscheiden van een chatbericht of een gastenboekvermelding. De specificatie is verdeeld over zeven CORD-documenten: privéstreams (01), gemeenschappen en lidmaatschap (02), kanalen (03), rollen (04), uitnodigingen (05), herkeying en heroprichting om verwijderde leden af te snijden (06), en audio/video via een blinde tokenmakelaar (07). Lidmaatschap zelf heeft geen lijst aan de serverkant: wie het vlak kan ontsleutelen is lid, en iemand echt verwijderen betekent de gemeenschap doorrollen naar een nieuw sleutel-epoch en die alleen aan de overgeblevenen geven, in plaats van een rij uit een tabel te schrappen.

## Hoe het verschilt van Marmot

Concord en [Marmot](/nl/topics/marmot/) lossen versleutelde groepsberichten op Nostr op met verschillende cryptografie voor verschillende groepsvormen, en de vergelijking van het Concord-project zelf is expliciet over die scheiding: Marmot legt [MLS](/nl/topics/mls/) boven op Nostr voor forward secrecy en post-compromise security, met sleutelpakketten per apparaat en geordende commits die de hele groep in de pas vooruit brengen. Dat levert sterke garanties op, tegen een prijs die meeschaalt met wijzigingen in het lidmaatschap, en past goed bij kleine groepen met hoge inzet waar toetreden en vertrekken zeldzaam zijn. Concord geeft in plaats daarvan elk lid dezelfde ruimtesleutel en herkeyt bij verwijdering de hele ruimte in plaats van per commit te ratelen, waarmee het een deel van de cryptografische garanties van MLS inruilt voor een model dat goedkoop blijft naarmate een gemeenschap groeit naar honderden of duizenden losse leden met veel verloop, de vorm die Discord-achtige gemeenschappen in de praktijk aannemen.

## Waarom Vector overstapte

Vectors eigen [v0.4.0 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) beschrijven Concord alleen als "ons eigen berichtenprotocol" voor Groepschats, zonder de redenering direct te noemen. De aansluiting op Concords eigen gepubliceerde motivatie is hoe dan ook duidelijk: Groepschats in een client als Vector zijn precies het grote, open geval met vaak veranderend lidmaatschap waar Marmots MLS-staat per apparaat het duurdere pad wordt, en Concords asynchrone ontwerp dat op elk moment kan worden dichtgevouwen is juist voor dat geval gebouwd. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) zette Marmot opzij voor Groepschats ten gunste van Concord, en bestaande Marmot-groepsgeschiedenis ging bij de overstap niet mee. [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) leverde vier dagen later "Concord v2" met privacy- en stabiliteitsverbeteringen. In dezelfde week [voegde Amethyst zijn eigen clean-room, wire-compatibele Concord-implementatie samen](https://github.com/vitorpamplona/amethyst/pull/3566), en Soapbox' Discord-achtige client [Armada](https://gitlab.com/soapbox-pub/armada) bouwt zijn Communities-functie al op dezelfde specificatie als referentie-implementatie. Drie onafhankelijke clients die binnen enkele dagen op één open specificatie samenkomen is een snelle route naar echte interoperabiliteit tussen clients, de moeite waard om te volgen tegenover hoeveel van de overige Nostr-groepschatclients juist bij Marmot blijven.

## Implementaties

- [Vector](https://github.com/VectorPrivacy/Vector) - privacy-eerst Nostr-messenger met één binary; eerste client die Concord leverde, in v0.4.0
- [Armada](https://gitlab.com/soapbox-pub/armada) (Soapbox) - Discord-achtige gemeenschapsclient; referentie-implementatie, backend in de aparte `armada-relay`-repo
- [Amethyst](https://github.com/vitorpamplona/amethyst) - functierijke Nostr-client voor Android en meerdere platforms; clean-room herimplementatie die wire-compatibel is met Armada ([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**Primaire bronnen:**
- [Concord-protocolspecificaties (CORD-01 tot CORD-07)](https://github.com/concord-protocol/concord)
- [Vector v0.4.0 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Vector v0.4.1 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**Genoemd in:**
- [Newsletter #31: Vector v0.4.0 verplaatst Groepschats van Marmot naar Concord, en Amethyst levert dagen later zijn eigen Concord-client](/nl/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Amethyst levert een clean-room Concord-implementatie voor end-to-end versleutelde gemeenschappen](/nl/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**Zie ook:**
- [Marmot Protocol](/nl/topics/marmot/)
- [MLS (Message Layer Security)](/nl/topics/mls/)
- [NIP-46: Nostr Connect](/nl/topics/nip-46/)
