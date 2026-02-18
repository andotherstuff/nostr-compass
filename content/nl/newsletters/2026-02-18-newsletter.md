---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** Een Blossom lokale cachelaag neemt vorm aan nu onafhankelijke projecten convergeren op offline mediajuurdgang voor Android. Alby lanceert een [NWC-ontwikkelaarssandbox](https://sandbox.albylabs.com) voor het bouwen en testen van Nostr Wallet Connect-integraties zonder echt geld te riskeren. Concurrerende voorstellen voor AI-agentcommunicatie op Nostr arriveren in dezelfde week van twee auteurs. fiatjaf verwijdert ongebruikte velden uit [NIP-11](https://github.com/nostr-protocol/nips/pull/1946) en schrapt retentiebeleid, landcodes, privacybeleid en communityvoorkeurstags die relay-operators nooit hebben overgenomen. [NIP-85](https://github.com/nostr-protocol/nips/pull/2223) merget richtlijnen voor vindbaarheid van serviceproviders voor Trusted Assertions. Een nieuwe `D`-tag in [NIP-52](https://github.com/nostr-protocol/nips/pull/1752) maakt daggranulaire tijdstempelindexering van agendagebeurtenissen mogelijk. Nieuwe projecten zijn onder meer [Mapnolia](https://github.com/zeSchlausKwab/mapnolia) voor gedecentraliseerde kaarttegelverspreiding, [Pika](https://github.com/sledtools/pika) voor MLS-versleuteld berichtenverkeer, [Keep](https://github.com/privkeyio/keep-android) voor FROST-drempelondertekening op Android, [Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) voor inhoudsgeadresseerde opslag met Nostr-integratie, en [Prism](https://github.com/hardran3/Prism) voor het delen van inhoud naar Nostr vanuit elke Android-app. [Primal Android](https://github.com/PrimalHQ/primal-android-app) merget 11 NWC-PR's die dubbele wallet-ondersteuning en automatische servicelifecycle toevoegen. [Mostro Mobile](https://github.com/MostroP2P/mobile) levert een [ingebouwde Lightning-wallet](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) via NWC-integratie. [Notedeck](https://github.com/damus-io/notedeck) bereidt zich voor op Android App Store-release terwijl HAVEN [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3) bereikt met ondersteuning voor meerdere npubs en cloudback-up. De deep dives van deze week behandelen het Trusted Assertions-systeem van NIP-85 voor het delegeren van Web of Trust-berekeningen aan serviceproviders, en het Calendar Events-protocol van NIP-52 na de update voor daggranulaire indexering.

## Nieuws

### Blossom Lokale Cachelaag Ontstaat

Meerdere onafhankelijke projecten convergeren op hetzelfde probleem: offline toegang tot [Blossom](/nl/topics/blossom/) media op mobiele apparaten.

[Morganite](https://github.com/greenart7c3/Morganite), een nieuwe Android-app van greenart7c3 (de ontwikkelaar achter [Amber](https://github.com/greenart7c3/amber) en [Citrine](https://github.com/greenart7c3/Citrine)), implementeert client-side caching voor Blossom-media. Gebruikers hebben toegang tot eerder bekeken afbeeldingen en bestanden zonder netwerkverbinding.

[Aerith](https://github.com/hardran3/Aerith) bracht [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) uit met beeldlabeling, bulk mirror/tag/verwijder-bewerkingen, filteren op label en bestandstype, plus initiële lokale Blossom-cacheondersteuning. Aerith is een beheerinterface voor gebruikers die media op meerdere Blossom-servers opslaan en hun blobs willen organiseren en spiegelen.

Een nieuwe [implementatiehandleiding voor lokale cache](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md) in de Blossom-specificatie documenteert client-side blobopslag, terwijl [Prism](https://github.com/hardran3/Prism) (van dezelfde ontwikkelaar als Aerith) Blossom-uploadintegratie toevoegt aan zijn Android deel-naar-Nostr-flow. Vier onafhankelijke projecten convergeerden deze week op hetzelfde probleem: een toegewijde caching-app, een mediabeheerder, een referentiespecificatie en een deeltool met Blossom-integratie, alle vier met persistente lokale opslag die verder gaat dan eenvoudig uploaden en ophalen.

### Alby NWC-Ontwikkelaarssandbox

[Alby](https://sandbox.albylabs.com) lanceerde een sandboxomgeving voor ontwikkelaars die bouwen met [Nostr Wallet Connect (NIP-47)](/nl/topics/nip-47/). De sandbox biedt een gehoste NWC-walletservice waarmee ontwikkelaars testverbindingen kunnen aanmaken en gesimuleerde betalingen kunnen versturen zonder verbinding te maken met een echte Lightning-wallet, terwijl ze de volledige verzoek/antwoord-cyclus van NWC-events in realtijd kunnen observeren. Ontwikkelaars genereren een `nostr+walletconnect://`-verbindingsstring vanuit de sandbox en geven die door aan hun client. De sandbox toont vervolgens de resulterende kind 23194-verzoek- en kind 23195-antwoordevents terwijl die tussen client en walletservice vloeien.

Dit verlaagt de drempel voor nieuwe NWC-integraties. Eerder vereiste testen een persoonlijke Lightning-wallet of een zelf gehoste NWC-service. De sandbox abstraheert dat weg en geeft ontwikkelaars een directe feedbacklus voor het implementeren van de methoden `pay_invoice`, `get_balance`, `make_invoice`, `lookup_invoice` en `list_transactions` tegen een live NWC-eindpunt.

### AI-Agent NIPs Arriveren

Voorstellen voor AI-agentcommunicatie op Nostr verschenen binnen dagen van elkaar, elk met een andere aanpak.

[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226) van joelklabo definieert een volledig protocol voor AI-agentinteractie: event kinds voor prompts, antwoorden, streaming delta's, statusupdates, tooltelemetrie, fouten, annuleringen en capability-discovery. Een `ai.info`-discoveryevent (kind 31340, vervangbaar) laat agents hun ondersteunde modellen, tools met schema's, streamingondersteuning en tarieflimieten aankondigen. Het voorstel van joelklabo omvat run-correlatie via prompt-ID, sessiebeheer, stream-reconciliatie met volgordebepaling, en [NIP-59](/nl/topics/nip-59/)-richtlijnen voor metadataprivacy.

[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220) van pablof7z neemt een andere aanpak en definieert kinds voor agentinstantiëring: definities en lessen. Dit zijn de event-typen die pablof7z gebruikt in [TENEX](https://github.com/tenex-chat/tenex), het autonome leersysteem gebouwd op Nostr. Een begeleidend voorstel, [NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221), eveneens van pablof7z, definieert events voor het aankondigen van [Model Context Protocol](https://modelcontextprotocol.io/)-servers en vaardigheden op Nostr. [NIP-22](/nl/topics/nip-22/)-commentaar wordt ondersteund, zodat de community MCP-servers direct op Nostr kan bespreken en beoordelen.

NIP-XX bestrijkt volledige agentcommunicatie terwijl NIP-AE en NIP-AD identiteit en tool-discovery adresseren. Deze voorstellen kunnen convergeren tot een uniforme standaard of naast elkaar bestaan als complementaire lagen.

## Releases

### HAVEN v1.2.0-rc3

[HAVEN](https://github.com/bitvora/haven), de alles-in-één persoonlijke relay die vier relayfuncties bundelt met een [Blossom](/nl/topics/blossom/)-mediaserver, bereikte [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3). Deze release candidate voegt ondersteuning toe voor meerdere npubs, waardoor één HAVEN-instantie meerdere Nostr-identiteiten kan bedienen. Eerdere RC's voegden `--from-cloud`- en `--to-cloud`-vlaggen toe voor cloudback-up (RC2) en losten een bug voor dubbel tellen in Web of Trust op (RC1).

### Mostro Mobile v1.2.0: Ingebouwde Lightning-Wallet

[Mostro Mobile](https://github.com/MostroP2P/mobile), de mobiele client voor de [Mostro](https://github.com/MostroP2P/mostro) P2P Bitcoin-exchange ([v1.1.0 behandeld vorige week](/nl/newsletters/2026-02-11-newsletter/#mostro-brengt-eerste-publieke-beta-uit)), bracht [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) uit met een ingebouwde Lightning-wallet via volledige [NWC (NIP-47)](/nl/topics/nip-47/)-integratie. Kopers en verkopers hoeven niet meer van app te wisselen om facturen af te handelen. De app detecteert hold invoices voor verkopers en betaalt die automatisch via de verbonden wallet, terwijl kopers automatische factuurgeneratie krijgen. De release volgt op [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1) van eerder in de week, dat ondersteuning voor meerdere Mostro-nodes toevoegde met een samengesteld register van vertrouwde instanties, kind 0 metadataophaling voor knooppuntweergave, aangepast knooppuntbeheer via pubkey en automatische terugval als een geselecteerde node offline gaat.

Aan de serverkant landde [Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2) met fixes voor dubbele dev fee-betalingen, snelheidsbegrenzing op het RPC-eindpunt voor wachtwoordvalidatie, en correcte geschillenopruiming bij coöperatieve annulering.

Een nieuw begeleidend project, [mostro-skill](https://github.com/MostroP2P/mostro-skill), stelt agents in staat te handelen op Mostro via Nostr.

### Aerith v0.2

[Aerith](https://github.com/hardran3/Aerith), de [Blossom](/nl/topics/blossom/)-afbeeldingsbeheerder, bracht [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) uit met beeldlabels voor het organiseren van media, bulk mirror/tag/verwijder-bewerkingen over servers, filteren op label en bestandstype, plus initiële lokale cacheondersteuning. Zie de [Nieuwssectie](#blossom-lokale-cachelaag-ontstaat) voor context over de bredere lokale cachetrend.

### Mapnolia: Gedecentraliseerde Kaarttegels via Nostr

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia) is een nieuwe georuimtelijke dataserver die [PMTiles](https://github.com/protomaps/PMTiles)-kaartarchieven opdeelt in geografische regio's en die aankondigt via Nostr voor gedecentraliseerde ontdekking. Het publiceert kind 34444-geparametriseerde vervangbare events naar Nostr-relays met een volledige index van kaarttegelstukken met laagmetadata, geohashregio's, bestandsreferenties en [Blossom](/nl/topics/blossom/)-serverdetails.

Clients ontdekken en halen kaartdata op via het Nostr-netwerk in plaats van gecentraliseerde tegelservers, waarbij aankondigingsevents genoeg metadata bevatten om alleen de benodigde geografische regio's op te vragen bij vermelde Blossom-servers. Mapnolia is het eerste project dat georuimtelijke datadistributie naar Nostr brengt, en opent mogelijkheden voor offlinecapabele kaarttoepassingen.

### Pika: Marmot-Gebaseerd Versleuteld Berichtenverkeer

[Pika](https://github.com/sledtools/pika) is een nieuwe end-to-end versleutelde berichtenapp voor iOS en Android die het [Marmot](/nl/topics/marmot/)-protocol gebruikt, dat [Messaging Layer Security (MLS)](/nl/topics/mls/) over Nostr-relays legt. De architectuur scheidt verantwoordelijkheden in een Rust-kern (`pika_core`) die MLS-statusbeheer en berichtversleuteling/-ontsleuteling over Nostr-relays afhandelt, met dunne native UI-shells in SwiftUI (iOS) en Kotlin (Android). Status stroomt eenzijdig: de UI verzendt acties naar de Rust-actor, die status muteert en momentopnames met revisienummers teruggeeft aan de UI via UniFFI en JNI-bindingen.

Pika voegt zich bij een groeiend veld van MLS-op-Nostr-berichtenapps naast [White Noise](https://github.com/marmot-protocol/whitenoise), [Vector](https://github.com/VectorPrivacy) en [0xchat](https://0xchat.com). Alle gebruiken Nostr-relays als transportlaag voor MLS-versleutelde cijfertekst, waardoor relay-operators de berichtinhoud niet kunnen lezen. Pika gebruikt de Marmot Development Kit (MDK) voor zijn MLS-implementatie en nostr-sdk voor relayconnectiviteit.

### Keep: [FROST](/nl/topics/frost/)-Drempelondertekening voor Android

[Keep](https://github.com/privkeyio/keep-android) is een nieuwe Android-applicatie voor [FROST](/nl/topics/frost/)-drempelondertekening waarbij geen enkel apparaat de volledige privésleutel bezit. Het implementeert [NIP-55](/nl/topics/nip-55/) (Android Signer) en [NIP-46](/nl/topics/nip-46/) (remote signing), zodat compatibele Nostr-clients handtekeningen kunnen aanvragen terwijl sleutelmateriaal verdeeld blijft over apparaten. De standaardconfiguraties zijn 2-van-3 en 3-van-5, hoewel elke t-van-n-drempel wordt ondersteund.

Keep's gedistribueerde sleutelgeneratie (DKG)-ceremonie verloopt over Nostr-relays met aangepaste event kinds: kind 21101 voor groepsaankondigingen, kind 21102 voor ronde 1-commitmentpolynomen (openbaar uitgezonden) en kind 21103 voor ronde 2-geheime aandelen ([NIP-44](/nl/topics/nip-44/) versleuteld punt-tot-punt tussen deelnemers). De groepsprivésleutelscalairewaarde wordt tijdens DKG nergens berekend of samengesteld. Elk apparaat bezit alleen zijn polynoomsafhandelingsaandeel, en elk willekeurig t aandelen kunnen een geldige Schnorr-handtekening produceren via een tweerondig commit-dan-onderteken-protocol. De resulterende 64-byte handtekening is niet te onderscheiden van een Schnorr-handtekening van één ondertekenaar. Achter de schermen gebruikt Keep de `frost-secp256k1-tr`-crate van de Zcash Foundation met Taproot-aanpassing, zodat de groepspublieke sleutel direct als Nostr npub werkt.

Keep voegt zich bij de [Frostr](https://frostr.org)-familie van projecten naast [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), [Igloo for Android](https://github.com/FROSTR-ORG/igloo-android), [Frost2x](https://github.com/FROSTR-ORG/frost2x) en [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios), wat de opties voor drempelsleutelbeheer op Nostr uitbreidt.

### Prism: Deel Alles naar Nostr vanuit Android

[Prism](https://github.com/hardran3/Prism) is een nieuwe Android-app (Kotlin/Jetpack Compose, API 26+) die zich registreert als systeemdoelwit voor delen, waarmee gebruikers tekst, URL's, afbeeldingen en video naar Nostr kunnen publiceren vanuit elke app op hun telefoon. Gedeelde URL's passeren een stripper voor trackingparameters voordat ze worden samengesteld tot notities. Prism haalt OpenGraph-metadata op om rijke linkvoorbeelden te genereren en rendert native Nostr-referenties (`note1`, `nevent1`) inline.

De planningsengine gebruikt een hybride `AlarmManager`/`WorkManager`-aanpak om Android-batterijoptimalisaties te omzeilen: AlarmManager verzorgt nauwkeurige wektijden terwijl versnelde WorkManager-taken aflevering garanderen, met exponentiële backoff-herpoging voor offlinescenario's. Media-uploads verlopen via configureerbare [Blossom](/nl/topics/blossom/)-servers met miniatuurweergavegeneratie voor afbeeldingen en videoframes. Alle event-ondertekening wordt gedelegeerd aan [NIP-55](/nl/topics/nip-55/) externe ondertekenaars zoals [Amber](https://github.com/greenart7c3/amber), met ondersteuning voor meerdere accounts voor het wisselen tussen identiteiten. Prism ondersteunt ook [NIP-84 (Highlights)](/nl/topics/nip-84/)-posts. Van dezelfde ontwikkelaar als [Aerith](#aerith-v02).

### Hashtree: Inhoudsgeadresseerde Opslag met Nostr-Integratie

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) is een bestandssysteemgebaseerd inhoudsgeadresseerd blobopslagsysteem dat Merkle-wortels op Nostr publiceert om muteerbare npub/pad-adressen te maken. Het systeem gebruikt "domme opslag" die werkt met elke sleutel-waarde-opslag en deelt inhoud op in 2MB-blokken geoptimaliseerd voor [Blossom](/nl/topics/blossom/)-uploads. Anders dan BitTorrent is geen actieve Merkle-bewijsberekening nodig; sla blobs gewoon op en haal ze op via hash.

De Nostr-integratie maakt git remote URL's mogelijk zoals `htree://npub.../repo-name` voor het klonen van repositories, met commando's als `htree publish mydata <hash>` om inhouds-hashes te publiceren naar `npub.../mydata`-adressen. De uitgebreide CLI ondersteunt zowel versleutelde (standaard) als openbare opslagmodi, vastpinnen van inhoud, pushen naar Blossom-servers en het beheren van Nostr-identiteiten. Elk opgeslagen item is ofwel ruwe bytes of een boomknooppunt, wat een basis biedt voor gedecentraliseerde inhoudsdistributie via het relaynetwerk van Nostr.

### Espy: Kleurpalet vastleggen op Shakespeare

[Espy](https://espy.you), gebouwd op het [Shakespeare](https://soapbox.pub/tools/shakespeare/)-platform, laat gebruikers kleurpaletten vastleggen uit foto's en ze delen als Nostr-events. Shakespeare is een AI-aangedreven app-bouwer die gebruikers authenticeert via NIP-07-browserextensies en ingebouwde Nostr-relayconnectiviteit biedt, zodat ontwikkelaars apps kunnen uitbrengen zonder eigen sleutelbeheer of relaypool te implementeren. Espy extraheert dominante kleuren uit camera-input naar deelbare paletkaarten die vindbaar zijn via standaard Nostr-feeds.

### Flotilla 1.6.4

[Flotilla](https://gitea.coracle.social/coracle/flotilla), hodlbod's Discord-achtige Nostr-client die relays als groepen organiseert, bracht [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4) uit. De Coracle-familie van projecten is gemigreerd van GitHub naar een zelf gehoste [Gitea-instantie](https://gitea.coracle.social/coracle). Deze release voegt pushmeldingen via NIP-9a toe en een wallet-ontvangstflow, plus geclassificeerde vermeldingen en URL-ondersteuning voor ruimtes. Interfaceverbeteringen omvatten opgeschoonde modals en meldingafhandeling. Ruimte dempen en veilige gebiedsinsets op mobiel ronden de wijzigingen af, naast fixes voor Safari-afbeeldinguploads en agendagebeurtenisdetails.

### Shosho v0.12.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), de mobiele livestreamingapp met Nostr-integratie, bracht [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0) uit. Deze release voegt video-clips toe met in-speler-antwoorden en aangepaste emoji-integratie. Threadbeveiliging blokkeert indirecte vermeldingsspam, en een nieuw QR-deelfunctie laat gebruikers profielen offline uitwisselen. Een nieuwe horizontale afspeelmodus geeft streams een Twitch-achtige kijkervaring, en het bladerscherm toont nu maker-clips naast livestreams.

### Granary v10.0

[Granary](https://github.com/snarfed/granary), een sociale web-vertaalbibliotheek die data converteert tussen Nostr, Bluesky, ActivityPub en andere platformen naar een gemeenschappelijk formaat, bracht [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0) uit met ingrijpende wijzigingen. De release schakelt de standaard ActivityStreams 1-ID's van Nostr van bech32 naar hex en voegt uitgebreide Nostr-ondersteuning toe, inclusief [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)-vermeldingsparsering en artikeltags. Een nieuwe optie voor meerdere outputs bij converters stelt ontwikkelaars in staat batch-vertalingen tussen protocollen uit te voeren.

### Nostr MCP Server v3.0.0

[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server), een [Model Context Protocol](https://modelcontextprotocol.io/)-server die AI-agents in staat stelt te communiceren met het Nostr-netwerk, bracht [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0) uit. Deze hoofdrelease voegt sociale acties toe (volgen, reacties, reposts, antwoorden) en relaybeheer van lijsten met [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)-ondersteuning plus optionele [NIP-42](/nl/topics/nip-42/)-authenticatie. Directe berichten via [NIP-17](/nl/topics/nip-17/) en [NIP-44](/nl/topics/nip-44/) zijn ook nieuw. De release is een praktisch hulpmiddel voor agents die op Nostr opereren, passend bij de [AI-agent NIP-voorstellen](#ai-agent-nips-arriveren) van deze week.

### Aegis v0.3.8

[Aegis](https://github.com/ZharlieW/Aegis), de platformonafhankelijke Nostr-ondertekenaar, bracht [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8) uit met meertalige UI-ondersteuning en een incrementele updatebeheerder voor zijn ingebouwde Nostr-appbrowser. Het nieuwe updatemechanisme maakt incrementele diff's tegen de lokale status, waardoor de in-app-directory van Nostr-webapps actueel blijft met minder bandbreedtegebruik. De release introduceert ook 5-minuten sleutelmateriaalcaching om databaserondreizen te verminderen bij het ondertekenen van meerdere events achtereen.

### SNSTR v0.3.1

[SNSTR](https://github.com/AustinKelsay/snstr) (Secure Nostr Software Toolkit for Renegades), een TypeScript-bibliotheek voor het Nostr-protocol, bracht [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1) uit. De release voegt pakketverificatiecontroles toe die ervoor zorgen dat alle ingangspunten zijn opgenomen in npm-tarballpakketten, met CI-handhaving op Node en Bun. [v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0) verscheen in dezelfde week.

### Citrine v2.0.0-pre1

[Citrine](https://github.com/greenart7c3/Citrine), de Android Nostr-relay van greenart7c3, bracht [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1) uit met prestatieverbeteringen door geoptimaliseerde database-indexen en beter Kotlin-coroutinebeheer. De release verbetert ook de ondersteuning voor het hosten van webapps, waarbij elke app nu op zijn eigen poort draait.

## Projectupdates

### Primal Android: NWC-Infrastructuuruitbreiding

[Primal Android](https://github.com/PrimalHQ/primal-android-app) mergede deze week 11 NWC-gerelateerde PR's, als vervolg op de uitbouw die [twee weken geleden begon](/nl/newsletters/2026-02-04-newsletter/#primal-android-ships-nwc-encryption). Deze batch voegt dubbele wallet-NWC-ondersteuning toe, automatisch starten/stoppen van service gekoppeld aan backendmeldingen, verbindingsrouting per wallettype en correcte gegevensopruiming bij verwijdering van wallet. De NWC-service beheert nu zijn eigen levenscyclus op basis van de walletverbindingsstatus, waardoor handmatige gebruikersingreep wordt verminderd.

### Notedeck: Voorbereiding voor Android App Store

[Notedeck](https://github.com/damus-io/notedeck), de platformonafhankelijke Nostr-client van het [Damus](https://github.com/damus-io/damus)-team, mergede deze week [voorbereiding voor Android App Store-release](https://github.com/damus-io/notedeck/pull/1287). De PR voegt een UGC-nalevingsplan (User Generated Content) toe dat Google Play vereist, inclusief een scherm voor het accepteren van servicevoorwaarden, gebruikersblokkeringen via contextmenu's en instellingen, [NIP-56 (Reporting)](/nl/topics/nip-56/)-functionaliteit die rapportevents publiceert naar relays, en een sectie Inhoud & Veiligheid in de instellingen. Bouwinfrastructuur is toegevoegd voor het genereren van ondertekende release-APK's en AAB's (Android App Bundles) via nieuwe Makefile-doelen. Een EULA-document stelt een leeftijdseis van 17+ en Nostr-specifieke disclaimers over gedecentraliseerde inhoud vast. De nalevingsfuncties zelf worden uitgebracht in vervolgde PR's; deze merge legt de documentatie- en ondertekeningsgrondslag.

Aan de Damus iOS-kant landde een fix voor een [oneindige laadspinner-regressie](https://github.com/damus-io/damus/pull/3593) waarbij de spinner oneindig bleef draaien nadat inhoud was geladen.

### Nostria: Discovery-Relays en DM-Fixes

[Nostria](https://github.com/nostria-app/nostria), de platformonafhankelijke Nostr-client gericht op mondiale schaal, mergede deze week 9 PR's. De meest opvallende voegt [automatische initialisatie van Discovery-Relays](https://github.com/nostria-app/nostria/pull/460) toe voor profielopzoekingen, wat nieuwe gebruikers werkende relayconnectiviteit geeft zonder handmatige configuratie. Andere fixes pakken [DM-tekstgebied-omloop](https://github.com/nostria-app/nostria/pull/466), [volledigschermvideo-viewportopvulling](https://github.com/nostria-app/nostria/pull/479), [artikelmetadata-extractie in repost-voorbeelden](https://github.com/nostria-app/nostria/pull/481) en [nostr: URI-omzetting in meldingen](https://github.com/nostria-app/nostria/pull/458) aan.

### Camelus: Riverpod v3-Migratie

[Camelus](https://github.com/camelus-hq/camelus), de Flutter-gebaseerde Nostr-client, mergede 5 PR's gericht op een [Riverpod v3 API-migratie](https://github.com/camelus-hq/camelus/pull/158) en [generieke feed-refactoring](https://github.com/camelus-hq/camelus/pull/159). Een [ingesloten notitiecache](https://github.com/camelus-hq/camelus/pull/161) vermijdt overbodige relay-ophaalacties voor geciteerde notities.

## NIP-Updates

Recente wijzigingen aan de [NIPs-repository](https://github.com/nostr-protocol/nips):

**Samengevoegd:**

- **[NIP-85: Service Provider Discoverability](https://github.com/nostr-protocol/nips/pull/2223)**: vitorpamplona voegde richtlijnen toe voor clientontdekking van [NIP-85 Trusted Assertions](/nl/topics/trusted-relay-assertions/)-serviceproviders, inclusief relay-hints en algoritme-specifieke servicesleutels. Zie de [deep dive hieronder](#nip-deep-dive-nip-85-trusted-assertions) voor volledige behandeling.

- **[NIP-11: Relay-informatieOpruiming](https://github.com/nostr-protocol/nips/pull/1946)**: fiatjaf verwijderde `privacy_policy`, de `retention`-array, `relay_countries` en het communityvoorkeurenblok uit [NIP-11](/nl/topics/nip-11/). Relay-operators vulden deze velden zelden in en clients handelden er niet naar.

- **[NIP-52: Daggranulaire Tijdstempeltag](https://github.com/nostr-protocol/nips/pull/1752)**: staab voegde een verplichte `D`-tag toe aan [NIP-52](/nl/topics/nip-52/) tijdgebaseerde agendagebeurtenissen (kind 31923) die het daggranulaire Unix-tijdstempel bevat, berekend als `floor(unix_seconds / 86400)`. Meerdere `D`-tags dekken meerdaagse evenementen, waardoor efficiënte temporele indexering mogelijk wordt zonder volledige tijdstempels te hoeven parseren.

- **[NIP-47: Vereenvoudiging](https://github.com/nostr-protocol/nips/pull/2210)**: De vereenvoudigings-PR [besproken in Nieuwsbrief #9](/nl/newsletters/2026-02-11-newsletter/) mergede deze week en verwijderde `multi_pay_invoice` en `multi_pay_keysend` uit [NIP-47 (Nostr Wallet Connect)](/nl/topics/nip-47/). Zie [Nieuwsbrief #8](/nl/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect) voor de volledige NWC-protocol deep dive.

**Open PR's en Discussies:**

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)**: Behandeld in [Nieuwsbrief #8](/nl/newsletters/2026-02-04-newsletter/), zag dit podcastspecificatievoorstel deze week verhitte discussie. staab merkte op dat er al minstens drie concurrerende podcaststandaarden in het wild bestaan, en derekross wees op een bestaande zes maanden oude implementatie met actieve apps en podcasts. De weg vooruit vereist convergentie tussen implementaties voordat een NIP-nummer kan worden toegewezen.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)**: joelklabo stelt een volledig AI-agentcommunicatieprotocol voor met event kinds voor prompts, antwoorden, streaming, tooltelemetrie, fouten en capability-discovery. Zie de [Nieuwssectie](#ai-agent-nips-arriveren) voor de behandeling van alle AI-voorstellen van deze week.

- **[NIP-PNS: Private Note Storage](https://github.com/nostr-protocol/nips/pull/1893)**: Het privénotitiesysteem van jb55 definieert kind 1080-events voor het opslaan van versleutelde persoonlijke notities op relays zonder te onthullen wie ze schreef. Het schema leidt een deterministisch pseudoniem sleutelpaar af van de nsec van de gebruiker via HKDF: `pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`, en genereert vervolgens een secp256k1-sleutelpaar van die afgeleide sleutel. Een tweede afleiding produceert een symmetrische versleutelingssleutel: `pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`. Binnenste notities worden versleuteld met [NIP-44](/nl/topics/nip-44/) v2 met deze sleutel en gepubliceerd onder de pseudonieme pubkey, zodat relays kind 1080-events zien van een identiteit die niet gekoppeld is aan de hoofdsleutel van de gebruiker. Anders dan [NIP-59](/nl/topics/nip-59/) gift wraps is PNS niet te spammen (de pseudonieme sleutel is deterministisch, niet willekeurig) en draagt geen publieke metadata (geen `p`-tags nodig omdat er geen ontvanger is). Deze week plaatste jb55 bevindingen van de implementatie van PNS in de Rust-backend van Notedeck (`enostr::pns`-module). Hij stelde vast dat de `hkdf_extract`-aanroep in de specificatie dubbelzinnig is omdat RFC 5869 HKDF twee fasen heeft (Extract en Expand) die verschillende uitvoer produceren, en de meeste bibliotheken beide verwachten. Hij verduidelijkte dat `pns_nip44_key` de normale ECDH-sleutelovereenstemming van NIP-44 omzeilt en direct als gesprekssleutel wordt gebruikt - een detail dat implementators moeten weten omdat de meeste NIP-44-bibliotheken standaard ECDH gebruiken. Hij markeerde ook een ongedefinieerde variabele in de TypeScript-referentie-implementatie. De PR, oorspronkelijk uit april 2025, wordt nu actief geïmplementeerd.

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)**: pablof7z definieert vier event kinds voor agentidentiteit op Nostr, ontleend aan zijn werk aan [TENEX](https://github.com/tenex-chat/tenex). De basissjabloon is kind 4199 (Agent Definition), met titel, rolomschrijving, systeeminstructies, tooltoewijzingen en versie. Gedragsmodificatoren leven in kind 4201 (Agent Nudge), dat `only-tool`-, `allow-tool`- en `deny-tool`-tags gebruikt voor runtimecapabiliteitsbeheer. Agents publiceren wat ze leren als kind 4129 (Agent Lesson)-events, gecategoriseerd en gekoppeld aan de bovenliggende definitie via `e`-tags, verfijnbaar via [NIP-22](/nl/topics/nip-22/)-commentaarreeksen. Eigendomsverificatie gebruikt kind 14199, een vervangbaar event waarbij menselijke operators hun agent-pubkeys vermelden, waarmee een bidirectionele keten ontstaat die overeenkomt met de `p`-tag in het kind 0-profiel van de agent.

- **[NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221)**: pablof7z definieert events voor het aankondigen van [Model Context Protocol](https://modelcontextprotocol.io/)-servers en individuele vaardigheden op Nostr. MCP-serveraankondigingen bevatten het eindpunt-URL van de server en de ondersteunde protocolversie naast een lijst van beschikbare tools met hun invoerschema's. [NIP-22](/nl/topics/nip-22/)-commentaar wordt ondersteund bij serveraankondigingen, zodat de community MCP-servers direct op Nostr kan bespreken en beoordelen.

- **[NIP-73: OSM-tagkind](https://github.com/nostr-protocol/nips/pull/2224)**: DestBro stelt voor OpenStreetMap-identificatoren toe te voegen aan [NIP-73 (External Content IDs)](/nl/topics/nip-73/), dat standaardiseert hoe Nostr-events externe inhoud refereren zoals boeken (ISBN), films (ISAN), podcastfeeds (GUID), geohashes en URL's via `i`- en `k`-tags. De voorgestelde OSM-kind zou events in staat stellen specifieke kaartfuncties (gebouwen, wegen, parken) te refereren via hun OpenStreetMap-node- of weg-ID, waardoor Nostr-inhoud wordt gekoppeld aan de open geografische database.

- **[NIP-XX: Responsieve Afbeeldingsvarianten](https://github.com/nostr-protocol/nips/pull/2219)**: woikos stelt voor [NIP-94](/nl/topics/nip-94/)-bestandsmetadataevents uit te breiden met tags voor responsieve afbeeldingsvarianten op verschillende resoluties. Clients kunnen de juiste variant selecteren op basis van weergavegrootte en netwerkomstandigheden, waardoor de bandbreedte wordt beperkt voor mobiele gebruikers die hoge-resolutieafbeeldingen bekijken die worden gehost op [Blossom](/nl/topics/blossom/)-servers.

## NIP Deep Dive: NIP-85 (Trusted Assertions)

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) definieert een systeem voor het delegeren van dure berekeningen aan vertrouwde serviceproviders die ondertekende resultaten publiceren als Nostr-events. Web of Trust-scores en betrokkenheidsmetrics vereisen het crawlen van veel relays en het verwerken van grote eventvolumes - werk dat onpraktisch is op mobiele apparaten. De [merge](https://github.com/nostr-protocol/nips/pull/2223) van deze week voegde richtlijnen toe over het clientontdekkingsproces voor deze providers.

**Delegering:**

Het berekenen van de Web of Trust-score van een gebruiker vereist het crawlen van volggrafen meerdere stappen diep over vele relays, en het berekenen van nauwkeurige volgersaantallen betekent dedupliceren over het gehele relaynetwerk. Mobiele apparaten en browsercliënts kunnen deze bewerkingen niet uitvoeren, terwijl de resultaten essentieel zijn voor spamfiltering en rangschikking van inhoud. NIP-85 overbrugt dit gat door gebruikers in staat te stellen vertrouwde providers aan te wijzen om de berekeningen uit te voeren en resultaten te publiceren als standaard Nostr-events.

**Protocolontwerp:**

NIP-85 gebruikt vier event kinds voor beweringen over verschillende onderwerptypen. Gebruikersbeweringen (kind 30382) bevatten volgersaantal, post-/antwoord-/reactietellingen, zap-bedragen, genormaliseerde rang (0-100), gemeenschappelijke onderwerpen en actieve uren:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Eventbeweringen (kind 30383) beoordelen individuele notities met commentaartelling, citatelling, reposts, reacties en zap-gegevens:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Voor adresseerbare events (lange-vorm artikelen, wikipagina's) past kind 30384 dezelfde betrokkenheidsmetrics toe op alle versies gezamenlijk. Kind 30385 beoordeelt externe identificatoren (boeken, films, websites, locaties, hashtags) waarnaar wordt verwezen via [NIP-73 (External Content IDs)](/nl/topics/nip-73/), dat standaardiseert hoe Nostr-events externe inhoud refereren via `i`- en `k`-tags:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Elke bewering is een vervangbaar adresseerbaar event waarbij de `d`-tag het onderwerp bevat: een pubkey, event-ID, eventadres of NIP-73-identificator. Serviceproviders ondertekenen deze events met hun eigen sleutels, en clients beoordelen ze op basis van vertrouwensrelaties.

**Providerontdekking:**

Gebruikers verklaren welke assertieproviders ze vertrouwen door kind 10040-events te publiceren. Elk item specificeert het assertietype met de provider-pubkey en relay-hint, plus optionele algoritme-varianten:

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

Gebruikers kunnen de taglijst in `.content` versleutelen met [NIP-44](/nl/topics/nip-44/) om hun providervoorkeuren privé te houden. Clients bouwen een providerlijst op door te controleren welke providers hun gevolgde accounts vertrouwen, waardoor een gedecentraliseerde reputatielaag ontstaat voor de assertieproviders zelf.

**Beveiligingsmodel:**

Providers moeten verschillende servicesleutels gebruiken voor afzonderlijke algoritmen, en een unieke sleutel per gebruiker wanneer algoritmen gepersonaliseerd zijn, om kruiscorrelatie van zoekopdrachten over gebruikers te voorkomen. Elke servicesleutel krijgt een kind 0-metadataevent dat het gedrag van het algoritme beschrijft, waardoor gebruikers transparantie krijgen over wat ze vertrouwen. Assertie-events mogen alleen worden bijgewerkt wanneer de onderliggende gegevens daadwerkelijk veranderen, om onnodige relayverkeer te voorkomen en clients de mogelijkheid te geven resultaten met vertrouwen te cachen.

**Huidige adoptie:**

NIP-85 formaliseert een patroon dat al informeel is ontstaan. De cacheserver van Primal berekent betrokkenheidsmetrics en Web of Trust-scores. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal), behandeld in [Nieuwsbrief #9](/nl/newsletters/2026-02-11-newsletter/#antiprimal-standaardconforme-gateway-naar-primals-cache), koppelt deze berekeningen aan standaard Nostr-clients via NIP-85 event kinds. [Nostr.band](https://nostr.band) beheert de `wss://nip85.nostr.band`-relay waarnaar de eigen voorbeelden van de specificatie verwijzen en serveert assertie-events voor zijn zoekindexdata. Aan de clientkant heeft [Amethyst](https://github.com/vitorpamplona/amethyst) (geschreven door vitorpamplona, die ook deze NIP schreef) experimentele Trusted Assertions-ondersteuning in zijn `quartz`-bibliotheek, waarbij assertie-events en serviceproviderverklaringen worden geparseerd. [Vertex](https://vertexlab.io) berekent vergelijkbare Web of Trust-metrics maar [koos een andere aanpak](https://vertexlab.io/blog/dvms_vs_nip_85/), met een directe API in plaats van NIP-85-events, met als reden het ontdekkingsprobleem en de rekenoverhead van assertiegerichte architecturen. Met NIP-85 kan elke client asserties van elke provider consumeren via een standaard eventformaat, en concurreren providers op nauwkeurigheid terwijl gebruikers kiezen wie ze vertrouwen.

## NIP Deep Dive: NIP-52 (Agendagebeurtenissen)

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md) definieert agendagebeurtenissen op Nostr en biedt clients een standaardmanier om occurrences op specifieke momenten of tussen momenten te vertegenwoordigen en te ontdekken. De [D-tag merge](https://github.com/nostr-protocol/nips/pull/1752) van deze week voegde daggranulaire indexering toe, waardoor een ontbrekend onderdeel in de queryinfrastructuur van de specificatie werd voltooid.

**Twee Eventtypen:**

NIP-52 scheidt agendagebeurtenissen in twee kinds op basis van temporele precisie. Datumgebaseerde events (kind 31922) vertegenwoordigen aaneengesloten occurrences zoals feestdagen of meerdaagse festivals. Ze gebruiken ISO 8601-datumstrings in hun `start`- en optionele `end`-tags, zonder tijdzoneconsideratie:

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

Tijdgebaseerde events (kind 31923) vertegenwoordigen specifieke momenten met Unix-tijdstempels in hun `start`- en optionele `end`-tags, plus IANA-tijdzoneidentificatoren (`start_tzid`, `end_tzid`) voor weergave. Beide kinds zijn geparametriseerde vervangbare events, zodat organisatoren details kunnen bijwerken door een nieuw event te publiceren met dezelfde `d`-tag.

**Kalenders en RSVP's:**

Kind 31924-events definiëren kalenders als verzamelingen en refereren events via `a`-tags die verwijzen naar kind 31922- of 31923-events via hun adrescoördinaten:

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

Gebruikers kunnen meerdere kalenders bijhouden (persoonlijk, werk, community) en clients kunnen zich abonneren op kalenders van specifieke pubkeys. Agendagebeurtenissen kunnen een `a`-tag bevatten die verwijst naar een kalender om opname te verzoeken, wat collaboratief kalenderbeheer mogelijk maakt waarbij meerdere gebruikers bijdragen aan kalenders die ze niet bezitten.

RSVP's gebruiken kind 31925, waarbij gebruikers hun aanwezigheidsstatus publiceren samen met een optionele vrij/bezet-indicator:

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

Geldige `status`-waarden zijn "accepted", "declined", "tentative", en de optionele `fb`-tag markeert de gebruiker als vrij of bezet voor die periode. RSVP-events refereren de `a`-tag van de agendagebeurtenis en bevatten de `p`-tag van de organisator, zodat de client van de organisator reacties over relays kan samenvoegen.

**De D-tagtoevoeging:**

Vóór de merge van deze week moesten clients die zochten naar events in een datumbereik alle events van een pubkey of kalender ophalen en aan de clientkant filteren. De nieuwe verplichte `D`-tag op tijdgebaseerde events (kind 31923) bevat een daggranulaire Unix-tijdstempel berekend als `floor(unix_seconds / 86400)`. Meerdaagse events bevatten meerdere `D`-tags, één per dag. Relays kunnen events nu indexeren per dag en efficiënt reageren op gefilterde zoekopdrachten, waardoor wat eerder een clientfilterprobleem was nu een relay-indexzoekopdracht wordt.

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

De `D`-waarde `20139` is gelijk aan `floor(1740067200 / 86400)`, waarmee dit event op 20 februari 2025 wordt geplaatst. Clients die zoeken naar "alle events deze week" sturen een filter met het bijbehorende `D`-bereik, en relays retourneren alleen overeenkomende events.

**Ontwerpkeuzes:**

NIP-52 laat terugkerende events bewust weg. De specificatie laat herhalingsregels (RRULE uit iCalendar) volledig buiten beschouwing en delegeert die complexiteit aan clients. Een organisator publiceert individuele events voor elke herhaling, waardoor het datmodel aan de relaykant eenvoudig blijft. Deelnemertags bevatten optionele rollen ("host", "speaker", "attendee"), en locatietags kunnen geohash-`g`-tags bevatten voor ruimtelijke zoekopdrachten naast voor mensen leesbare adressen.

**Implementaties:**

[Flockstr](https://github.com/zmeyer44/flockstr) is de primaire agendaclient gebouwd op NIP-52. [Coracle](https://gitea.coracle.social/coracle/coracle) toont agendagebeurtenissen in zijn sociale feed. De D-tagtoevoeging van deze week maakt relay-side temporele indexering mogelijk die beide clients kunnen gebruiken om bandbreedte te beperken bij het opvragen van events in een specifiek datumbereik.

---

Dat was het voor deze week. Iets aan het bouwen of nieuws te delen? Wil je dat we je project behandelen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via [NIP-17](/nl/topics/nip-17/) DM</a> of vind ons op Nostr.
