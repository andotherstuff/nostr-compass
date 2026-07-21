---
title: "Nostr Compass #32"
date: 2026-07-22
translationOf: /en/newsletters/2026-07-22-newsletter.md
translationDate: 2026-07-22
draft: false
type: newsletters
description: "IndieSats laat zijn uitgeversrol vallen en herlanceert als open Nostr-muziekinfrastructuur, Nostrord v2.3.0 levert de clientkant van een week met vijf NIP-29-spec-PRs, Zapstore 1.1.0 maakt de apparaatsleutel verplaatsbaar en brengt automatische achtergrondupdates, favoriete volgsets worden samengevoegd en meteen hernummerd, en het Iris-ecosysteem levert een pubsub-bibliotheek, een browser-FIPS-runtime en nostr-social-graph 2.0."
---

Welkom terug bij Nostr Compass, uw wekelijkse gids voor Nostr.

**Deze week:** [IndieSats](#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure) zet sleutelbeheer, zijn whitelist en zijn verplichte inkomstenaandeel opzij, en herlanceert als een open relay, speler en ontdekkingslaag waar artiesten onder hun eigen sleutels publiceren. [Nostrord v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) levert groepsmoderatie, mute-lijsten en onion-relays in dezelfde week waarin [vijf NIP-29-spec-PRs worden samengevoegd](#protocol-work-and-nip-updates). [Zapstore 1.1.0](#zapstore-110-makes-the-device-key-portable-and-adds-background-auto-updates) introduceert een verplaatsbare versleutelde apparaatsleutel met Amber-back-up en opt-in automatische achtergrondupdates. Het [lijst-kind voor favoriete volgsets](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house) wordt samengevoegd en opent binnen enkele dagen een hernummerings-PR. En het [Iris-ecosysteem](#the-iris-ecosystem-ships-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week) levert nostr-pubsub, de fips-ts-browserruntime en nostr-social-graph 2.0.0 in één enkele week.

Getagde releases brengen [Amber v6.3.0](#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support) met gegroepeerde goedkeuringen voor bunker-ondertekening, [Wisp v1.2.0](#wisp-v120-adds-a-multi-account-switcher-and-collapsible-reply-threads) met een multi-accountwisselaar, [Sonar v0.1-alpha.11](#sonar-v01-alpha11-continues-the-alpha-line) dat de alpha-lijn voortzet, en nieuw project [ClipRelay v0.1.2](#cliprelay-v012-new-project-syncs-clipboards-across-devices-over-nostr-relays) dat klemborden synchroniseert via Nostr-relays.

Aan de niet-uitgebrachte kant voegt [nostream](#nostream-merges-seven-prs-without-cutting-a-release) de toegangscontrolestack samen die de Deep Dive van deze week behandelt, en voltooit [Amethyst](#amethyst-lands-v1130-pre-release-qa-on-napplet-isolation-and-concord-authority) de pre-release-QA van v1.13.0 over 81 samengevoegde PRs.

De NIPs-repository voegt deze week vijf PRs samen, waaronder het [NIP-29-cluster](#protocol-work-and-nip-updates) en de [favoriete volgsets van kind:10011](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house), en opent debatten over [NIP-47-vereenvoudiging](#protocol-work-and-nip-updates) en [vertrouwde relay-asserties](#protocol-work-and-nip-updates). De Deep Dive behandelt [NIP-42 en NIP-43, het relay-toegangscontrolepaar](#nip-deep-dive-nip-42-and-nip-43).

---

## Hoofdverhalen

### IndieSats laat zijn uitgeversrol vallen en herlanceert als open Nostr-muziekinfrastructuur

[IndieSats](https://zapstore.dev) is een op Nostr gebaseerd muziekplatform dat tot deze week als uitgever optrad: het beheerde sleutels voor artiesten, voerde een whitelist en nam een verplichte 2%-aandeel van de inkomsten. In een [omslagaankondiging gepubliceerd op 20 juli](https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u) heeft het project al die drie rollen tegelijk afgestoten. Het herlanceerde platform bestaat in plaats daarvan uit drie stukken open infrastructuur: een open relay, een speler en een ontdekkingslaag, waarbij artiesten muziek publiceren onder hun eigen Nostr-profielen in plaats van een door het platform beheerde identiteit. Inkomstenverdelingen worden opt-in, niet langer verplicht, en het platform honoreert nu [NIP-09](/nl/topics/nip-09/) kind:5-verwijderingsverzoeken zodat artiesten hun werk kunnen verwijderen. Voor een ruimte die het meestal heeft over protocollen die platforms vervangen, is dit een levend voorbeeld van een platform dat zichzelf vrijwillig in protocolstukken demonteert.

### Nostrord v2.3.0 levert groepsmoderatie, mute-lijsten en onion-relays

[Nostrord](https://github.com/nostrord/nostrord), de groepschatclient voor Android, iOS, web en desktop, heeft [v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) uitgebracht met aangesloten groepsmoderatieacties op alle interfaces ([PR #192](https://github.com/nostrord/nostrord/pull/192)), groepsuitnodigingen met toestemmingsvoorwaarde en cross-relay-detectie ([PR #195](https://github.com/nostrord/nostrord/pull/195)), cross-platform [NIP-51](/nl/topics/nip-51/) mute-lijsten ([PR #188](https://github.com/nostrord/nostrord/pull/188)), en ondersteuning voor Tor .onion-relays. De release landt in dezelfde week waarin de onderliggende [NIP-29](/nl/topics/nip-29/)-specificatie vijf PRs samenvoegde over subgroepen, het vastzetten van berichten, banners en uitnodigingscodes (details in de [protocolsectie](#protocol-work-and-nip-updates) van deze week), dus groepschat op Nostr heeft nu zowel een diepere specificatie als een client die het merendeel ervan uitoefent, wat de feedbacklus verkort voor iedereen die verder bouwt op relay-groepen.

### Zapstore 1.1.0 maakt de apparaatsleutel verplaatsbaar en voegt automatische achtergrondupdates toe

[Zapstore](https://github.com/zapstore/zapstore) is een Nostr-native appstore waar releases worden ondertekend door ontwikkelaarssleutels en geen centrale operator ervoor instaat. [Versie 1.1.0](https://github.com/zapstore/zapstore/releases/tag/1.1.0), de eerste release die hier sinds begin maart wordt behandeld, dicht de twee grootste gaten met conventionele appstores. De eerste is updates: opt-in automatische achtergrondupdates downloaden nu via wifi en installeren stilletjes of gefaseerd, zodat apps actueel blijven zonder handmatige toeren door de store. De tweede is identiteitscontinuïteit: de apparaatsleutel wordt verplaatsbaar, versleuteld en te back-uppen via [Amber](https://github.com/greenart7c3/Amber) over [NIP-55](/nl/topics/nip-55/), de Android-ondertekenaarsinterface, zodat een gebruiker die van telefoon wisselt niet opnieuw begint als een onbekend apparaat. De release verplaatst ook de appcatalogus naar relays als door het apparaat ondertekende kind:10067-events, voegt [NIP-56](/nl/topics/nip-56/) geverifieerde meldingen toe vanuit het overloopmenu zodat gebruikers problematische apps kunnen markeren op een manier die andere clients kunnen consumeren, en verifieert het C1-bewijs dat aan een release is gehecht voordat een installatie doorgaat, waarmee de band wordt aangehaald tussen wat een ontwikkelaar heeft ondertekend en wat een apparaat draait.

### Het lijst-kind voor favoriete volgsets wordt samengevoegd en verhuist meteen

Een verhaal over specificatiecoördinatie speelde zich af binnen één enkele week. [PR #2413](https://github.com/nostr-protocol/nips/pull/2413) werd op 15 juli samengevoegd en standaardiseerde een vervangbaar lijst-kind voor favoriete volgsets onder [NIP-51](/nl/topics/nip-51/) (lijsten): een toegewijd kind waar clients de samengestelde sets van gevolgde accounts van een gebruiker kunnen publiceren in plaats van generieke lijst-kinds te overbelasten. Binnen enkele dagen bleek dat het toegewezen kind:10011 al elders in gebruik was, dus een vervolg-[PR #2417](https://github.com/nostr-protocol/nips/pull/2417) is nu open om de lijst te hernummeren naar kind:10021. Er is nog niets uitgebracht tegen het samengevoegde kind, wat dit het goedkope moment maakt om te hernummeren; zodra clients kind:10011-events gaan publiceren, wordt de botsing duur om te ontwarren. Ontwikkelaars die lijstconsumerende functies bouwen zouden de hernummerings-PR moeten volgen, niet de samengevoegde tekst, totdat deze is opgelost.

### Het Iris-ecosysteem levert een pubsub-bibliotheek, een browser-FIPS-runtime en een social-graph 2.0 in één week

Drie releases uit de Iris-baan landden tegelijk, en ze grijpen in elkaar. [nostr-pubsub](https://github.com/mmalmi/nostr-pubsub) is een transportneutrale publish/subscribe-bibliotheek voor Nostr-events; zijn [eerste gevolgde releases, v0.1.3 tot en met v0.5.2](https://github.com/mmalmi/nostr-pubsub/releases), leveren een browser-relaydrager gebouwd op de SimplePool van nostr-tools, eventverificatie aan de transportgrens zodat ongeldige handtekeningen nooit abonnees bereiken, en begrensde historische queries. [fips-ts](https://github.com/mmalmi/fips-ts) brengt [FIPS](/nl/topics/fips/), het Noise-over-secp256k1-peertransport dat eerder als Rust-stack beschikbaar was, naar de browser als een TypeScript-runtime: releases [0.0.24 tot en met 0.0.30](https://github.com/mmalmi/fips-ts/releases) voegden een WebRTC-datachanneldrager toe, op Nostr gebaseerde signalering voor peerdetectie, een cache van recente peers en een IndexedDB-adapter voor browseropslag, en de runtime is wire-compatibel met de referentie-implementatie in Rust. Het derde stuk, [nostr-social-graph v2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0), is een major-versie van de social-graph-bibliotheek: ondertekende rosteroperaties voor Nostr-identiteitsgrafen, apparaatgoedkeuringsstromen opgestart vanuit een canonieke URI met drie velden, en FIPS-transportidentiteitsfacetten met gedeelde Rust- en TypeScript-testvectoren. Het verbindende kader is de [Iris Stack](https://stack.iris.to/), het integratielab van het project dat deze bibliotheken samenbindt met Blossom, Hashtree en versleutelde berichtgeving. Alles bij elkaar kan een webapp nu peers ontdekken via Nostr, een versleuteld FIPS-kanaal naar hen openen en een ondertekende sociale graaf bijhouden, allemaal in TypeScript.

---

## Getagde releases

### Amber v6.3.0 groepeert goedkeuringen voor bunker-ondertekening en voegt Expert List-ondersteuning toe

[Amber](https://github.com/greenart7c3/Amber) is een Android [NIP-46](/nl/topics/nip-46/) remote signer. [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) voegt gegroepeerde goedkeuring van meerdere verzoeken toe voor bunker-ondertekening, zodat een reeks hangende handtekeningverzoeken samen kan worden beoordeeld en goedgekeurd in plaats van één prompt tegelijk. De release voegt ook ondersteuning toe voor Expert List (kind 12022)- en Expert Pack (kind 32022)-events, een privacymodus die gevoelige inhoud op het scherm verbergt, en een wijziging om eerst de [NIP-65](/nl/topics/nip-65/)-relaylijst van een account op te halen vóór de profielmetadata, zodat ondertekenstromen beginnen vanuit de werkelijke relayset van de gebruiker. Dit volgt op de v6.2.x-lijn die in de uitgave van 2026-07-08 werd behandeld.

### Vervolg op Nostrord v2.2.0

Met [v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) aan kop van de nieuwssectie van deze week noteert de getagde-releaseplek alleen wat het hoofdverhaal niet behandelt: v2.3.0 volgt op de DM-bediening van v2.2.0 die in #31 werd behandeld, en is daarmee de tweede opeenvolgende wekelijkse release van de client.

### Wisp v1.2.0 voegt een multi-accountwisselaar en inklapbare antwoordthreads toe

[Wisp](https://github.com/barrydeen/wisp) is een privacygerichte Nostr-client met ingebouwde walletondersteuning. [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) voegt een multi-accountwisselaar toe om tussen profielen te schakelen zonder opnieuw in te loggen, inklapbare antwoordthreads voor lange gesprekken, het strippen van trackingparameters uit notitielinks voordat ze openen, en een overzicht van de transactiegeschiedenis van de wallet. De release volgt op de Wisp-update die in de uitgave van 2026-07-08 werd behandeld.

### ClipRelay v0.1.2 (nieuw project) synchroniseert klemborden tussen apparaten via Nostr-relays

[ClipRelay](https://github.com/tajava2006/cliprelay) is een nieuw gelanceerde cross-platform app (Android, macOS, Windows, Linux) die je klembord synchroniseert tussen je eigen apparaten: kopiëren op de ene machine, plakken op een andere. Al het verkeer loopt via Nostr-relays als [NIP-44](/nl/topics/nip-44/) versleutelde events geadresseerd aan jezelf, dus er is geen server om te draaien en geen account om aan te maken; de privésleutel blijft buiten de app. [v0.1.2](https://github.com/tajava2006/cliprelay/releases) repareert een subtiele syncfout waarbij een machine die uit de slaapstand ontwaakte bleef publiceren maar stilletjes stopte met ontvangen, en haalt de relay-statusindicatoren aan die eerder dode abonnementen als gezond rapporteerden. Dit is ClipRelays eerste verschijning in de nieuwsbrief.

### Sonar v0.1-alpha.11 zet de alpha-lijn voort

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar), het hoofdverhaal van vorige week, heeft [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) getagd met werk aan de Rust-meshlinkengine, BLE- en meshfixes, en relaydiagnostiek; een incrementeel vervolg op de alpha-lijn die in #31 werd behandeld.

### De kleinere lanceringen van de week

Drie kleinere releases verdienen elk één regel: [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release), de Nostr-belapp, migreerde zijn pushmeldingen naar UnifiedPush, waardoor gesprekssignalering buiten Googles push-infrastructuur blijft; [nostr-vpn v4.1.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.1), een mesh-VPN die Nostr voor signalering gebruikt, leverde een update op Zapstore; en twee nieuwe apps debuteerden daar ook: StableKraft, een Nostr-plus-Lightning muziek- en podcastaggregator, en Hakari, een versleutelde Nostr-back-up voor een gewichtslogger.

### Amethyst voltooit pre-release-QA van v1.13.0 over napplet-isolatie en Concord-autoriteit

[Amethyst](https://github.com/vitorpamplona/amethyst) voegde deze week 81 PRs samen voorafgaand aan de v1.13.0-release. [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) is een pre-release-QA-ronde die napplet-accountisolatie, fixes voor Concord-autoriteit en ongeveer 30 andere fixes dekt, met verdere v1.13.0-voorbereidings-PRs die landden tot 21 juli. Dit zet de dekking uit #31 van Amethysts clean-room Concord-clientimplementatie voort, waarbij het autoriteits- en isolatiegedrag van dat werk wordt aangehaald voordat het getagd wordt uitgebracht.

---

## Niet-uitgebrachte wijzigingen

### nostream voegt zeven PRs samen zonder een release te taggen

[nostream](https://github.com/Cameri/nostream), de TypeScript-relayimplementatie, voegde deze week zeven PRs samen zonder een release te taggen. Het koppeltje aan kop is [PR #702](https://github.com/Cameri/nostream/pull/702) en [PR #676](https://github.com/Cameri/nostream/pull/676), die samen relayoperators een werkende toegangscontrolestack met authenticatie plus lidmaatschap geven; de NIP Deep Dive van deze week loopt precies die handshake door.

### FIPS v0.4.1 haalt het transport aan waarop het Iris-ecosysteem bouwt

[jmcorgan/fips](https://github.com/jmcorgan/fips) leverde [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1), een onderhoudsrelease die de antipoison-status begrenst, convergentie- en MTU-afhandeling repareert en CPU-gebruik verlaagt. Op zichzelf is dit loodgieterswerk, maar deze week is het bindweefsel: de browser-TypeScript-runtime [fips-ts](https://github.com/mmalmi/fips-ts) uit het Iris-ecosysteemcluster in de nieuwssectie van dit nummer is wire-compatibel met dit Rust-transport, dus fixes hier planten zich direct voort naar waarmee de browserruntime interopereert.

---

## Protocolwerk en NIP-updates

Recente wijzigingen in de [NIPs-repository](https://github.com/nostr-protocol/nips):

**Samengevoegd:**

- **[NIP-29](/nl/topics/nip-29/) (Relay-based Groups): Subgroepen** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319), samengevoegd op 2026-07-16): NIP-29 definieert op relays gehoste groepen waar lidmaatschap, rollen en chatgeschiedenis op één enkel relay leven als adresseerbare events uit de `kind:39000`-serie, met moderatieacties gedragen door admin-events uit de `kind:9000`-serie. Deze PR laat een groep zichzelf als subgroep declareren door een `parent`-tag aan zijn metadata toe te voegen, verwijzend naar de `d`-identifier van een andere groep op hetzelfde relay. Subgroepen zijn in elk ander opzicht gewone groepen: lidmaatschap cascadeert niet (lid worden van een ouder verleent geen lidmaatschap van een kind), adminrollen erven niet over (de `kind:39001`-adminlijst van elke subgroep is gezaghebbend voor zijn eigen bereik), en elke subgroep houdt zijn eigen onafhankelijke `kind:9000`/`kind:9001`-ledenevents bij. Relays die de hiërarchie ondersteunen adverteren dit in hun NIP-11-relayinformatiedocument onder een `nip29`-object met `"subgroups": true`, zodat clients de mogelijkheid kunnen ontdekken voordat ze geneste gemeenschappen proberen aan te maken.

- **[NIP-29](/nl/topics/nip-29/): Berichten vastzetten** ([PR #2379](https://github.com/nostr-protocol/nips/pull/2379), samengevoegd op 2026-07-15; [PR #2416](https://github.com/nostr-protocol/nips/pull/2416), samengevoegd op 2026-07-17): Groepsadmins kunnen nu berichten vastzetten binnen een relay-gebaseerde groep. Het mechanisme voegt een nieuw moderatie-event toe, `kind:9010` `update-pin-list`, dat de volledige geordende pinlijst draagt als `e`-tags die verwijzen naar reguliere event-ids, en een nieuw optioneel groepsniveau-event, `kind:39005` *group pinned events*, dat het relay regenereert om de meest recente geaccepteerde pinlijst te spiegelen. Omdat elke `kind:9010` de hele lijst vervangt in plaats van afzonderlijke items om te schakelen, worden vastzetten, losmaken, herordenen en leegmaken van pins allemaal uitgedrukt door één nieuwe lijst in te dienen. De vervolg-PR #2416 breidt het formaat uit zodat ook `a`-tags in de pinlijst worden geaccepteerd, waardoor admins adresseerbare events (longform-artikelen, wikipagina's en andere geparameteriseerde vervangbare inhoud) naast gewone chatberichten kunnen vastzetten. Relays mogen het aantal pins begrenzen, en de samengevoegde spectekst beveelt aan pins weer te geven in de volgorde waarin de tags verschijnen.

- **[NIP-29](/nl/topics/nip-29/): Bannertag en uitnodigingscode-achtervoegsel** ([PR #2383](https://github.com/nostr-protocol/nips/pull/2383), samengevoegd op 2026-07-16; [PR #2380](https://github.com/nostr-protocol/nips/pull/2380), samengevoegd op 2026-07-16): Twee toevoegingen voor weergave en onboarding aan groepsmetadata. PR #2383 voegt een optionele `banner`-tag toe aan het `kind:39000`-groepsmetadata-event, naast de bestaande velden `name`, `picture` en `about`, zodat clients een kopafbeelding voor een groepspagina kunnen renderen. PR #2380 definieert een uitnodigingscode-achtervoegsel voor groepsdeellinks: een uitnodigingscode kan worden toegevoegd aan de `naddr`-identifier van de groep als `naddr1...?invite=<code>`. Omdat de bech32-tekenset geen `?` bevat, blijft het deel vóór het achtervoegsel op zichzelf een geldige naddr, zodat clients die de extensie niet begrijpen de groep alsnog kunnen oplossen. Clients die hem wel begrijpen vullen de `code`-tag vooraf in op het `kind:9021`-deelnameverzoek, dat samengaat met het bestaande `kind:9009` `create-invite`-moderatie-event om toelating tot gesloten groepen te vereenvoudigen.

- **[NIP-51](/nl/topics/nip-51/) (Lijsten): Favoriete volgsets, kind:10011** ([PR #2413](https://github.com/nostr-protocol/nips/pull/2413), samengevoegd op 2026-07-15): NIP-51 definieert de standaardlijst-kinds, verdeeld tussen vervangbare lijsten uit de `kind:10000`-serie (één per gebruiker) en adresseerbare sets uit de `kind:30000`-serie (veel per gebruiker, gerefereerd via de `d`-tag). Deze PR voegt `kind:10011` toe, *favorite follow sets*, een standaard vervangbare lijst waarvan de `a`-tags naar `kind:30000`-volgsets verwijzen. Als spiegel van `kind:10012` (relay feeds), dat `a`-tags bevat die naar `kind:30002`-relaysets verwijzen, stelt het nieuwe kind een gebruiker in staat benoemde volgsets te bookmarken, zoals samengestelde lijsten van pubkey-verzamelingen gepubliceerd door zichzelf of anderen, en clients deze te laten aanbieden voor volgen met één tik of het wisselen van feed. Merk op dat dit kindnummer al betwist wordt: zie de open hernummerings-PR hieronder.

- **[NIP-46](/nl/topics/nip-46/) (Nostr Connect): Richtlijn voor stille time-out** ([PR #2375](https://github.com/nostr-protocol/nips/pull/2375), samengevoegd op 2026-07-15): NIP-46 is het remote-signingprotocol waarbij een client versleutelde JSON-RPC-achtige verzoeken naar een signer (bunker) via relays stuurt en op een versleuteld antwoord wacht. De samengevoegde wijziging is één zin draadgedrag: verzoeken met onbekende of niet-ondersteunde methoden MOETEN worden beantwoord met een fout. Voorheen kon een signer die een methode ontving die hij niet implementeerde nooit antwoorden, waardoor de client hing totdat zijn eigen time-out afging zonder manier om "niet-ondersteunde methode" te onderscheiden van "signer offline". Het verplichte foutantwoord stelt clients in staat snel te falen en een betekenisvol bericht aan de gebruiker te tonen in plaats van eindeloos te blijven draaien.

**Open PRs en discussies:**

- **Hernummering van kind:10011 naar kind:10021** ([PR #2417](https://github.com/nostr-protocol/nips/pull/2417)): Verplaatst de zojuist samengevoegde favoriete-volgsetslijst van `kind:10011` naar `kind:10021`, omdat `10011` al elders in gebruik is. De hernummerings-PR was binnen enkele dagen na de oorspronkelijke samenvoeging open, dus clients die favoriete volgsets implementeren zouden deze PR moeten volgen en op het definitieve nummer moeten mikken, niet op `10011`.

- **[NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect): Kernvereenvoudiging** ([PR #2419](https://github.com/nostr-protocol/nips/pull/2419)): Stelt voor NIP-47, het wallet-connectprotocol dat apps Lightning-betalingen laat aanvragen bij een remote wallet via Nostr, te verkleinen tot een compactere kernspecificatie. Optionele en meer gespecialiseerde functionaliteit zou uit `47.md` verhuizen naar een toegewijde extensierepository, [nostr-wallet-connect/nwc](https://github.com/nostr-wallet-connect/nwc), waar extensiespecificaties onafhankelijk van de kern kunnen evolueren. Het gestelde doel is de kern klein, stabiel en eenvoudig te implementeren te houden, in lijn met de richting die in eerdere NWC-calls is afgesproken om een minimale wallet-connectlaag te scheiden van rijkere optionele gedragingen. Gezien hoe breed NIP-47 is uitgerold over wallets en apps, zou iedereen die NWC spreekt de herstructureringsdiscussie moeten volgen.

- **Trusted Relay Assertions (concept, geen nummer toegewezen)** ([PR #2418](https://github.com/nostr-protocol/nips/pull/2418)): Stelt een standaard voor voor het publiceren van vertrouwensevaluaties over Nostr-relays, gepositioneerd als de "wat wij concluderen"-laag naast [NIP-11](/nl/topics/nip-11/) (wat een relay over zichzelf beweert) en [NIP-66](/nl/topics/nip-66/) (wat monitors hebben gemeten). Assertieproviders zouden vertrouwensscores berekenen uit waargenomen metrieken, operatorreputatie en gebruikersmeldingen; clients zouden deze asserties raadplegen bij het kiezen met welke relays ze verbinden. Het concept introduceert `kind:30385` (adresseerbare Trusted Relay Assertion, met tags voor score, betrouwbaarheid, kwaliteit, toegankelijkheid, operator, beleid en jurisdictie), `kind:10385` (vervangbare Trusted Provider List, de door de gebruiker gekozen assertieproviders), en hergebruikt [NIP-32](/nl/topics/nip-32/)-labels voor relay- en operatormeldingen. Er is nog geen NIP-nummer toegewezen; dit is een vroeg stadium-concept.

- **AND-operator voor filters ("NIP-91", voorgesteld, nummer nog niet in de repository)** ([PR #2252](https://github.com/nostr-protocol/nips/pull/2252)): Onder NIP-01 zijn tagfilters alleen OR: een filter `"#t": ["meme", "cat"]` matcht events met een van beide tags. Dit voorstel voegt een `&`-modifier toe voor indexeerbare tags, zodat `"&t": ["meme", "cat"]` alleen events teruggeeft die beide tags dragen, waardoor relays de intersectie server-side kunnen doen in plaats van dat clients te veel ophalen en lokaal filteren. De regels specificeren dat AND voorrang heeft op OR, dat tagwaarden die in AND worden gebruikt door ondersteunende relays in OR moeten worden genegeerd, en dat clients OOK de standaard `#` OR-tags MOETEN opnemen voor compatibiliteit met relays die de extensie niet ondersteunen (die relays geven het bredere OR-resultaat terug, dat de client lokaal intersecteert). De PR is een heropend vervolg op een eerder voorstel en noemt relayimplementaties waaronder een nostr-rs-relay-dockerimage, netstr en een Snort-workerrelay. Het NIP-91-nummer verschijnt alleen in de PR-branch; het staat nog niet in de NIP-index van de README van de repository, dus behandel het nummer als voorlopig.

- **Nostr web applets ("NIP-5D", voorgesteld, nummer nog niet in de repository)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Definieert een `postMessage`-protocol voor gesandboxte webapplicaties ("napplets") die in iframes of webviews draaien om te communiceren met een host-applicatie ("shell"). De specificatie is bewust een dunne kern: ze specificeert de berichtenvelop, sandboxregels (napplet-iframes MOETEN `sandbox="allow-scripts"` gebruiken zonder `allow-same-origin`, en shells MOGEN NIET `window.nostr` NIP-07 binnen de iframe blootstellen), afzenderidentificatie via de onvervalsbare `MessageEvent.source`-windowreferentie, niet `event.origin`, en op manifest gebaseerde capaciteitsonderhandeling. De feitelijke protocolberichten voor ondertekening, relaytoegang, opslag en inter-nappletcommunicatie worden gedelegeerd aan NAP (Nostr Applet Protocol)-extensiespecificaties, elk eigenaar van een capaciteitsdomein, waarbij ondertekening en versleuteling altijd door de shell worden bemiddeld zodat sleutels nooit de sandbox binnenkomen. Het voorstel is afhankelijk van de NIP-5A-nappletmanifestspecificatie en is deze week actueel: Amethysts pre-release-werk voor v1.13.0 omvat napplet-accountisolatie, waardoor client-side napplet-hosting een actief implementatiegebied is. Net als bij "NIP-91" hierboven is het 5D-nummer voorlopig.

---

## NIP Deep Dive: NIP-42 en NIP-43

Een relay draaien die niet voor iedereen open is betekende vroeger alles zelf uitvinden. Een betaalde of alleen-op-uitnodiging relayoperator moest out-of-band een whitelist bijhouden, meestal een tekstbestand met pubkeys verzameld via DMs, zonder een standaardmanier om een verbonden client te vertellen "bewijs wie je bent" en zonder een standaardmanier voor een gebruiker om toelating te vragen of te weten of hij lid was. Elk relay dat begrensde lees- of schrijfrechten wilde bouwde zijn eigen privémechanisme, en clients konden met geen ervan inter-opereren. [NIP-42](/nl/topics/nip-42/) standaardiseert de identiteitsbewijshelft van dat probleem, en [NIP-43](/nl/topics/nip-43/) standaardiseert de lidmaatschapshelft. Deze week heeft nostream, de TypeScript-relay, het paar van begin tot eind samengevoegd: [PR #702](https://github.com/Cameri/nostream/pull/702) begrenst het lezen van versleutelde kinds tot geauthenticeerde ontvangers, en [PR #676](https://github.com/Cameri/nostream/pull/676) voegt strategieën toe voor deelname- en vertrekverzoek-events, beide samengevoegd op 20 juli.

### NIP-42: Authenticatie van clients bij relays

[NIP-42](/nl/topics/nip-42/) beantwoordt één vraag: wie zit er op deze verbinding? Een relay dat lees- of schrijfrechten wil begrenzen stuurt een `AUTH`-bericht met een challenge-string, bij het verbinden of op verzoek wanneer een aanvraag authenticatie vereist. De client antwoordt met zijn eigen `AUTH`-bericht met een ondertekend efemeer event, kind 22242, en het relay antwoordt met een `OK`-bericht precies alsof het auth-event een gewone schrijfbewerking was. De geauthenticeerde sessie geldt vervolgens voor de duur van de verbinding, en een client kan meerdere pubkeys op één verbinding authenticeren met een reeks `AUTH`-berichten, die het relay elk als geauthenticeerd behandelt.

Het ondertekende auth-event ziet er zo uit:

```json
{
  "id": "4ef6f2c0b1a84c9a3d0f9c58e2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0",
  "pubkey": "c308e1f882c1f1dff2a43d4294239ddeec04e575f2d1aad1fa21ea7684e61fb5",
  "created_at": 1753195800,
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com/"],
    ["challenge", "challengestringhere"]
  ],
  "content": "",
  "sig": "8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1"
}
```

De `pubkey` is de identiteit die wordt bewezen, aangezien het relay de `sig` over het event-`id` ertegen verifieert. De `kind` 22242 zit in het efemere bereik: het event is een credential op verbindingsniveau, en relays mogen het nooit opslaan of naar andere clients uitzenden. De `relay`-tag bindt de handtekening aan één relay-URL zodat een onderschept auth-event niet tegen een ander relay kan worden afgespeeld, en de `challenge`-tag bindt hem aan de specifieke challenge-string die het relay op deze verbinding heeft uitgegeven, waardoor het afspelen van een onderschepte auth op een latere verbinding wordt geblokkeerd. De `created_at` moet dicht bij de huidige tijd liggen, binnen een venster van ongeveer tien minuten, zodat een verouderd auth-event vanzelf verloopt. Het `content`-veld is leeg; er wordt niets gepubliceerd.

De specificatie definieert ook twee machineleesbare voorvoegsels die begrenzing zichtbaar maken voor clients. Een relay dat een abonnement weigert omdat de client zich nog niet heeft geauthenticeerd antwoordt met een `CLOSED`-bericht dat begint met `auth-required:`, en een geweigerde schrijfbewerking krijgt een `OK` met hetzelfde voorvoegsel. Een client die wel is geauthenticeerd maar nog steeds geen toestemming heeft voor de actie krijgt in plaats daarvan `restricted:`. Het is dat onderscheid waarop [nostreams PR #702](https://github.com/Cameri/nostream/pull/702) bouwt: leesbewerkingen van versleutelde kinds kunnen nu worden gesloten met `auth-required:` totdat de aanvragende pubkey bewijst dat hij de ontvanger is.

### NIP-43: Relay-toegangsmetadata en -verzoeken

[NIP-43](/nl/topics/nip-43/) beantwoordt de vervolgvraag: nu het relay weet wie je bent, wat mag je doen? Waar NIP-42 een handshake op een live verbinding is, is NIP-43 een set gepubliceerde events die de lidmaatschapsstatus beschrijven en gebruikers laten vragen die te wijzigen. Aan de relaykant toont een kind 13534-event, ondertekend door de pubkey in het `self`-veld van het [NIP-11](/nl/topics/nip-11/)-document van het relay, één `member`-tag per pubkey, met optionele rolargumenten die verwijzen naar roldefinities gepubliceerd als kind 33534. Kind 8000 kondigt een toegevoegd lid aan en kind 8001 kondigt een verwijdering aan, beide ondertekend door dezelfde relaysleutel met een `p`-tag voor het betrokken lid. Aan de gebruikerskant is kind 28934 een deelnameverzoek dat een uitnodigingscode draagt in een `claim`-tag, is kind 28935 een efemeer uitnodigingscode-event dat het relay ter plaatse genereert wanneer een gebruiker een claim aanvraagt, en is kind 28936 een vertrekverzoek.

Een deelnameverzoek ziet er zo uit:

```json
{
  "id": "9f0e1d2c3b4a59687a6b5c4d3e2f1098a7b6c5d4e3f2019a8b7c6d5e4f3021a9b8",
  "pubkey": "ee1d336e13779e4d4c527b988429d96de16088f958cbf6c074676ac9cfd9c958",
  "created_at": 1753195900,
  "kind": 28934,
  "tags": [
    ["-"],
    ["claim", "invite-code-from-operator"]
  ],
  "content": "",
  "sig": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
}
```

De `pubkey` is de gebruiker die om toelating vraagt, en kind 28934 markeert het event als deelnameverzoek. De `-`-tag is de [NIP-70](/nl/topics/nip-70/)-markering voor beschermde events, die relays vertelt dit event van niemand anders dan de auteur te accepteren. De `claim`-tag draagt de uitnodigingscode die de gebruiker out-of-band heeft verkregen, en `created_at` moet nu zijn, plus of min een paar minuten, zodat een oud verzoek niet kan worden afgespeeld. Het relay beantwoordt de claim met een `OK`-bericht, waarbij het het NIP-42-`restricted:`-voorvoegsel hergebruikt voor mislukkingen zoals een verlopen of ongeldige code, en zou vervolgens zijn kind 13534-lijst moeten bijwerken en kan een kind 8000-lid-toevoegingsevent publiceren. Lidmaatschap wordt bewust niet uit één enkel event afgeleid: de specificatie zegt dat de door het relay ondertekende lijst niet als exhaustief of gezaghebbend moet worden beschouwd, en een client die bepaalt of iemand momenteel lid is zou zowel het kind 13534 van het relay als de eigen events van het lid moeten raadplegen. Clients mogen deelname-, uitnodigings- of vertrekverzoeken alleen sturen naar relays die deze NIP adverteren in de `supported_nips`-sectie van hun NIP-11-document, en [nostreams PR #676](https://github.com/Cameri/nostream/pull/676) is de relay-side-machinerie die die verzoek-kinds omzet in daadwerkelijke lidmaatschapswijzigingen.

### Geschiedenis

NIP-42 is met afstand de oudste van de twee. Hij kwam op 2 januari 2023 de NIPs-repository binnen, in [commit c80be21c](https://github.com/nostr-protocol/nips/commit/c80be21c), waar fiatjaf een eerdere relay-auth-NIP opgesteld door semisol drastisch vereenvoudigde, waarbij een complexer challenge-schema werd teruggebracht tot het enkele ondertekende efemere event dat de specificatie vandaag nog gebruikt. NIP-43 arriveerde veel later, op 30 oktober 2025, toen hodlbods [PR #1079](https://github.com/nostr-protocol/nips/pull/1079) werd samengevoegd, met relay-toegangsmetadata en -verzoeken die direct voortbouwen op het `restricted:`-voorvoegsel van NIP-42. De kloof van tweeënhalf jaar weerspiegelt hoe lang het ecosysteem betaalde en privé-relays draaide op ad-hoc-whitelists voordat de lidmaatschapslaag een standaard kreeg.

### Implementaties

Aan de relaykant levert [nostream](https://github.com/Cameri/nostream) na de samenvoegingen van deze week nu beide helften. [strfry](https://github.com/hoytech/strfry) implementeert NIP-42, waarbij kind 22242-auth-events in zijn ingester worden gevalideerd en challenges vanuit de configuratie worden uitgegeven. [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) handelt de AUTH-handshake af in zijn verbindingslaag met tests die de challenge en het tijdstempelvenster dekken. [khatru](https://github.com/fiatjaf/khatru), het Go-relayframework, houdt de geauthenticeerde pubkey per verbinding bij zodat policies lees- en schrijfbewerkingen erop kunnen begrenzen. Aan de clientkant ondertekent [Amethyst](https://github.com/vitorpamplona/amethyst) kind 22242-antwoorden op relay-challenges, inclusief per-stream-auth voor zijn versleutelde Concord-gemeenschappen. De twee NIPs splitsen toegangscontrole langs een schone lijn: NIP-42 is identiteitsbewijs, begrensd tot één verbinding, één challenge en een paar minuten geldigheid, en zegt niets over beleid. NIP-43 is beleid, uitgedrukt als gewone relay-events: wie lid is, wie is toegevoegd of verwijderd, en hoe een gebruiker die overgangen aanvraagt. Het gat dat implementeerders in gedachten moeten houden is dat nog niets fijnmazigere permissies standaardiseert dan de optionele rolmetadata van NIP-43, dus elk relay dat meer doet dan een binaire lid/niet-lid-splitsing ontwerpt die laag zelf.

---

Dat was het voor deze week. Bouwt u iets of heeft u nieuws te delen? Neem contact op via een NIP-17-DM of vind ons op Nostr.
