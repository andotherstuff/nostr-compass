---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "Amethyst voor desktop, beveiligingsoplossingen in Amber, privébijlagen, geauthenticeerde software-installaties, en inhoudswaarschuwingen en status."
translationOf: /en/newsletters/2026-10-14-newsletter.md
translationDate: 2026-10-15
---

**[Amethyst](#amethyst)** brengt zijn Android-interface naar de desktop en voegt native Wayland-ondersteuning toe. **[Amber](#amber)** verhelpt problemen met het intrekken van machtigingen, het wissen van gekopieerde geheimen en een instellingswijziging waardoor sleutels verloren konden gaan. **[Keep](#keep-android)** scherpt de machtigingen voor automatisch ondertekenen aan, terwijl **[MDK](#mdk)** streaming van privébijlagen en het bijwerken van berichten met de oudste eerst introduceert. **[Zap Cooking](#zap-cooking)** integreert beveiligingen voor wijzigingen aan volglijsten en geauthenticeerd lidmaatschap. [Releasedetails](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) volgen hieronder, naast protocolwijzigingen en mechanismen voor openbare status.

## Hoofdnieuws

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) brengt de gedeelde interface van de sociale Android-client naar de desktop, met aangepaste feeds, kolomindelingen voor brede vensters, optionele vergrendelingen, versleutelde media en [Blossom-uploads](/nl/topics/blossom/). Scores van aanbieders uit [NIP-85, vertrouwde verklaringen](/nl/topics/nip-85/), worden lokaal geïndexeerd voor verzoeken, meldingen en badges, met door de gebruiker gekozen aanbieders en drempelwaarden.

De [v1.19.0-release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) van vandaag voegt native Wayland-ondersteuning en videocompressie op de desktop toe, met behulp van afzonderlijk geïnstalleerde FFmpeg en ffprobe. Oplossingen voor sleutelopslag verhelpen herhaalde sleutelhangerprompts en problemen met de Linux-sleutelbos. Agendaverzamelingen en RSVP's worden nu weergegeven, en de Android-inloginterface voegt [ondertekening op afstand via NIP-46](/nl/topics/nip-46/) toe. Versleutelde enveloppen worden parallel geopend voordat ze serieel worden geïndexeerd, terwijl het opnieuw verbinden met relays en de verwerking van relaylijsten van feedauteurs zijn gecorrigeerd. De [relayclient respecteert wachttijden bij snelheidslimieten](https://github.com/vitorpamplona/amethyst/pull/4422) voordat abonnementen of publicaties worden hervat.

De [wijziging voor relays van vertrouwensaanbieders](https://github.com/vitorpamplona/amethyst/pull/4437) behandelt relays van aanbieders uit de kind 10040-lijst van de gebruiker als eigen, vertrouwde relays. Die verbindingen gebruiken standaard een rechtstreekse route; voor Tor moet de instelling voor vertrouwde relays worden ingeschakeld. De [NIP-42-relayauthenticatie](/nl/topics/nip-42/) van de hoofdclient kan de publieke sleutel van de gebruiker aan deze relays bekendmaken.

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) verhelpt drie beveiligingsproblemen in de Nostr-ondertekenaar voor Android. [Ingetrokken machtigingen](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw) blijven niet langer bestaan door een raceconditie in de cache, en expliciete weigeringen krijgen voorrang op de status volledig vertrouwd. Voor [gekopieerde geheimen](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p) plant het systeem in dat het klembord na 60 seconden wordt gewist, ook als het proces wordt beëindigd; de inhoud blijft gedurende die periode leesbaar, en ook later gekopieerde tekst kan worden gewist. Bij het wijzigen van [‘ontgrendeld apparaat vereisen’](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5) blijft de oude omhullende sleutel behouden totdat de migratie van geheimen is voltooid, terwijl eerder verloren sleutels verloren blijven. De release herstelt goedkeuringen voor meerdere nostrconnect-verzoeken en antwoorden via de in de URI opgegeven relays. Gebruikers van 6.6.8 en ouder moeten bijwerken.

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0), een [FROST-drempelondertekenaar](/nl/topics/frost/), voegt gedistribueerde sleutelgeneratie op het apparaat en geauthenticeerd herstel van onderbroken bewerkingen met sleutelaandelen toe. Ook apparaten zonder StrongBox-ondersteuning worden ondersteund. Bij drempelondertekening bezitten deelnemende apparaten elk een aandeel van het ondertekeningsgeheim en werken ze samen om een handtekening te produceren; de instellings- en herstelstappen bepalen welke apparaten kunnen deelnemen.

[Versie 1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1) voorkomt dat automatisch ondertekenen onthouden weigeringen, machtigingen met de instelling Vragen, verlopen goedkeuringen of mislukte leespogingen van machtigingen negeert. Bij het verlopen wordt goedkeuring op de achtergrond verwijderd, terwijl weigeringen behouden blijven. De [migratie van beleid per app](https://github.com/privkeyio/keep-android/pull/532) verplaatst machtigingen naar de door de kern beheerde opslag, met behoud van strengere beslissingen.

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) [authenticeert de native walletbridge](https://github.com/jesuspirate/chama/pull/29) die door zijn via Nostr bemiddelde handelsapplicatie wordt gebruikt, schakelt URL-gebaseerde omleiding van de bridge in productie uit en valideert uitbetalingsbedragen. Ook weigert de applicatie een wallet te wissen waarvan de inhoud niet kan worden gelezen.

[Versie 6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22) beveiligt het opnieuw afspelen tegen events van buitenstaanders, controleert opvolgingsrelaties, weigert lege verzamelingen arbiters en leidt het tijdstip voor terugbetaling af van de ondertekende LOCK-tijd. De consensuswijzigingen zijn van toepassing op CREATE-events die vanaf 1 november 2026 worden ondertekend; de clientbeveiligingen gelden onmiddellijk. De releaseopmerkingen behouden de kanttekeningen over federaties die via de handelsadvertentie worden geselecteerd en stofuitbetalingen. Latere [wijzigingen aan ondertekening en herstel](https://github.com/jesuspirate/chama/releases/tag/v6.4.23) voegen lezers voor beschermde seeds en herstelbare late vergrendelingen toe, terwijl [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24) grote handelslijsten verbetert.

### Zap Cooking

De recepten- en sociale client [Zap Cooking integreert beveiligingen voor wijzigingen aan volglijsten](https://github.com/zapcooking/frontend/pull/795) tegen onvolledige, verouderde of onverwacht krimpende leesresultaten. Volgacties gebruiken één beveiligd updatepad dat bestaande tags en inhoud behoudt. De identiteit van de ondertekenaar wordt vóór publicatie gecontroleerd. De [oplossing voor lidmaatschapsautorisatie](https://github.com/zapcooking/frontend/pull/802) gebruikt de publieke sleutel waarmee het geauthenticeerde verzoek is ondertekend. Een [route die een beheerdersgeheim blootlegde, is verwijderd](https://github.com/zapcooking/frontend/pull/801); bij de uitrol moet het geheim nog steeds worden vervangen, iets wat een geïntegreerde wijziging op zichzelf niet kan garanderen. Latere [reparaties aan discussiedraden en bladwijzers](https://github.com/zapcooking/frontend/pull/833) behouden het werkelijke hoofdelement van de antwoordketen en herstellen mislukte schrijfacties voor bladwijzers. [Velden voor recept-tags](https://github.com/zapcooking/frontend/pull/836) sturen geen toetsaanslagen meer naar profielzoekdiensten of NIP-50-zoekdiensten en verlaten de editor niet meer met niet-opgeslagen wijzigingen.

## Releases met een tag

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0), de runtime voor [versleutelde Marmot-groepen](/nl/topics/marmot/), voegt streaming en hervatbare privébijlagen toe, met voortgangsweergave en annulering. Ook stuurt deze privé [NIP-56-meldingen](/nl/topics/nip-56/) naar de beheerder van de installatie via [NIP-59-geschenkverpakkingen](/nl/topics/nip-59/), zonder identificatoren van berichten, groepen en relays. Het inhalen verwerkt batches van maximaal 256 events met de oudste eerst en behoudt CLOSED-weigeringen van relays. SOCKS5-routering omvat relays, media en ontdekkingsdiensten, zonder rechtstreekse terugvaloptie.

De [releasehandleiding](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md) vereist dat bindings, headers en native artefacten samen worden bijgewerkt. Databaseschema's gaan van 101 naar 107 zonder mogelijkheid om terug te keren naar een oudere versie. De opslag van geheimen op de host moet worden gemigreerd. MarmotKit en C-artefacten zijn stabiel; WN Agent blijft een prerelease en workspace-crates zijn niet gepubliceerd op crates.io. Geschiedenis die meer dan vijf [MLS-epochs](/nl/topics/mls/) te laat aankomt, kan nog steeds niet te ontsleutelen zijn zonder melding van onvolledige geschiedenis, en geauthenticeerde agentclients behouden toegang tot de volledige API.

De release [probeert ook het opslaan van profielen, volglijsten en relaylijsten opnieuw wanneer dit na de eerste bevestiging nog in behandeling is](https://github.com/marmot-protocol/mdk/pull/2228); deze nieuwe pogingen op de achtergrond blijven na een herstart niet behouden. [Bij het opzoeken van uitnodigingen worden verwijdering en vervaldatum van KeyPackages gecontroleerd op ontdekkingsrelays](https://github.com/marmot-protocol/mdk/pull/2211), waarvan de antwoorden niet kunnen bewijzen dat de ontvanger nog over het private KeyPackage-materiaal beschikt. [Doelen van activiteitsreacties](https://github.com/marmot-protocol/mdk/pull/2187) worden nu consistent afgeleid van geauthenticeerde actoren en afzonderlijke groepscommits; oudere geschiedenis zonder actor blijft onvolledig.

Latere wijzigingen op master [sluiten achtergebleven relay-abonnementen en halen activatieherhalingen op in pagina’s van maximaal 500 events](https://github.com/marmot-protocol/mdk/pull/2274). [Herstel van hiaten tussen epochs](https://github.com/marmot-protocol/mdk/pull/2298) haalt de nieuwste 256 events op van een relay waarvoor de vergelijking is mislukt, zonder een volledige geschiedenis te garanderen. [Commits voor zelfupdates proberen elke overgeslagen groepsrelay opnieuw](https://github.com/marmot-protocol/mdk/pull/2275). Nieuwe waarschuwingscontroles omvatten [bekende verouderde epochs](https://github.com/marmot-protocol/mdk/pull/2273) en [commits die nog naar relays moeten worden verstuurd](https://github.com/marmot-protocol/mdk/pull/2288); gebruikers kunnen het risico accepteren, dus deze controles garanderen niet dat een groep niet kan splitsen.

[Bijlagedownloads die door opslaggebrek zijn geblokkeerd](https://github.com/marmot-protocol/mdk/pull/2249) behouden hun hervatbare voortgang wanneer er onvoldoende vrije ruimte is. Grote expliciete downloads schrijven rechtstreeks naar een bestand, waarbij tijdelijke opslag en controlepunten ongeveer vijf tot zes keer de omvang van de inhoud aan vrije ruimte vereisen. [Voorvertoningen van geverifieerde openbare events](https://github.com/marmot-protocol/mdk/pull/2304) krijgen een versleutelde accountcache met een beperkte omvang, terwijl [KeyPackage-resultaten die uitsluitend verouderde items bevatten](https://github.com/marmot-protocol/mdk/pull/2305) te onderscheiden worden van onvolledige zoekopdrachten bij relays. Dit zijn latere broncodewijzigingen die overeenkomstige aanpassingen in de host vereisen; voorvertoningen op basis van event-ID’s uit voltooide ophaalacties controleren niet opnieuw op latere verwijderingen.

De agentbruggen [begrenzen ook de backenduitvoer](https://github.com/marmot-protocol/mdk/pull/2103) om te voorkomen dat te grote antwoorden het geheugen uitputten, en [accepteren het daadwerkelijke verwijderingsantwoord van de connector](https://github.com/marmot-protocol/mdk/pull/2301). Reeds afgeleverde tekst blijft afgeleverd wanneer een uitvoerlimiet een beurt beëindigt.

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0) voegt USB-verbindingen tussen telefoons of fips-desktops toe en neemt [het huidige voorgestelde NIP-5D-manifestformaat](https://github.com/Origami74/myco/pull/135) over, met ondertekende hashes van artefacten en pictogrammen. Oudere telefoons kunnen nog steeds worden gekoppeld, maar moeten worden bijgewerkt om deze napplets te openen. De [wijzigingen in het downloadbeleid](https://github.com/Origami74/myco/pull/133) maken onderscheid tussen internetbestemmingen, meshbestemmingen en door de gebruiker geconfigureerde HTTP-bestemmingen. Door de auteur aangeleverde hints en omleidingen kunnen onder het internetbeleid geen lokale netwerken aftasten, terwijl door de gebruiker geconfigureerde bestemmingen onbeperkt blijven. De softwareclient [ontdekt ook blobs op de BUD-03 Blossom-servers van de auteur](https://github.com/Origami74/myco/pull/134). Dat verbetert het vinden van artefacten, maar maakt installatieverkeer zichtbaar voor die servers. Deze HTTP-wijzigingen bieden geen gelijkwaardige bescherming voor WebSocket-verbindingen. [Controles op beschikbaarheid in het nabijgelegen meshnetwerk](https://github.com/Origami74/myco/pull/132) vragen peers naar blobs zonder deze te downloaden of contact op te nemen met openbare Blossom-servers. Deze begrensde HEAD-verzoeken vereisen toestemming voor meshgebruik; het aantal houders bewijst niet dat het volledige artefact beschikbaar blijft.

De release [bevraagt ook upstream-DNS-servers gelijktijdig en gebruikt het snelste antwoord](https://github.com/Origami74/myco/pull/137), om te voorkomen dat time-outs bij roamingproviders het opzoeken van relays en artefacten blokkeren. Outbox-publicaties richten zich op elke vermelde schrijfrelay, waarbij aflevering aan tragere bestemmingen op de achtergrond plaatsvindt. Internetmesh blijft standaard uitgeschakeld en afbeeldingen van het web worden niet bewaard na een herstart.

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13) voegt lees- en schrijfrelaylijsten en outbox-routering toe aan zijn Android-fotoclient. De [releaseopmerkingen](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2) beschrijven de rollen van relays, en accounts zonder lijst beginnen met drie openbare standaardrelays. Nearby gebruikt grove geohashes en aangrenzende cellen; het toevoegen van een locatie aan een bericht is opt-in en staat standaard uit. Die tags maken nog steeds een gebied openbaar zichtbaar. Het onderzochte publicatieresultaat betekent dat het bericht in de wachtrij voor een socket staat, terwijl acceptatie door de relay nog niet is bevestigd.

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0) laat gebruikers Monero-fooien ontvangen via een persoonlijke watcher, terwijl [0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0) bij nieuwe configuraties de fooibedragen en de namen van afzenders in meldingen standaard verbergt. Afbeeldingen worden standaard pas geladen nadat erop is getikt, en optionele Primal-aantallen en client-tags zijn uitgeschakeld. Een gehoste watcher krijgt via de private view key nog steeds inzicht in elke inkomende betaling aan de geregistreerde wallet. Openbare ontvangstbewijzen behouden de ontvanger, het tijdstip en het bericht waarnaar wordt verwezen, ook wanneer bedragen verborgen zijn.

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2) combineert gedeelde versleutelde boodschappenlijsten met op passkeys gebaseerde Nostr-identiteiten en Marmot-chat per lijst. Deelnemen aan lijsten kan door een toondersleutel te plakken, die lees- en bewerkingsrechten geeft. Inloggen met een passkey is afhankelijk van ondersteuning door browser en provider voor de pseudo-random-function-extensie van WebAuthn; tags van leden blijven zichtbaar voor relays. [Versie 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3) bewaart lijsten bij het opnieuw openen door ontsleutelde inhoud lokaal te cachen, en verhelpt zo gevallen waarin alleen de sleutel behouden bleef totdat een relay de lijst opnieuw afleverde.

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0) leest de kinds 1315/1316 van een andere Roadstr-client met de bijbehorende beoogde geldigheidsduur en bevestigingsregels. Een compacte codec bewaart reconstrueerbare ondertekende meldingen voor een experimentele MeshCore-radio- en relaybrug. Compatibel publiceren en radioverzending staan standaard uit, en delen vereist voorafgaande toestemming. Radiomeldingen maken de positie, het tijdstip en de openbare ondertekeningssleutel zichtbaar voor iedereen binnen bereik. Tests gebruikten gesimuleerde radio’s; echte hardware, Android BLE en publicatie naar openbare relays zijn nog niet geverifieerd.

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3) verbetert reacties op artikelen en de verwerking van geciteerde berichten in zijn Android-client. Reacties op artikelen gebruiken kind 1111 met het artikel als root en de reactie als parent, terwijl gewone antwoorden op notities kind 1 blijven. Het vinden van citaten accepteert zowel q-tags als oudere e-vermeldingen met links; nieuw gepubliceerde citaten voegen q-tags toe. Bij een mislukte publicatie worden optimistisch getoonde reacties teruggedraaid.

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28) beschrijft [het lezen van geneste](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0) publicatie-indexen van kind 30040 die zowel hoofdstukken als onderliggende indexen bevatten in de volgorde van de uitgever. Offlinekopieën behouden die hiërarchie en bladwijzers die aan elk afzonderlijk voorkomen zijn gekoppeld. Vernieuwen haalt de huidige revisies op aan de hand van coördinaten, maar behoudt de vorige download wanneer resultaten onvolledig of ouder zijn, of wanneer het ophalen mislukt. Opnieuw uitzenden behoudt de oorspronkelijke ondertekende onderliggende elementen. Begrensde uitbreiding en leesbare gedeeltelijke takken voorkomen dat een onvolledige structuur als een compleet boek wordt gepresenteerd.

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0) vervangt Global door Discover in zijn contentfeeds. Discover put uit mensen die worden gevolgd door de accounts die de gebruiker volgt, en rangschikt berichten op basis van gedeelde connecties, met uitsluiting van de gebruiker zelf en reeds gevolgde accounts. Uitgelogde gebruikers en accounts die niemand volgen, zien in plaats daarvan een geselecteerd startnetwerk. Dit beperkt het bereik van standaardontdekking tot een sociale omgeving; spambestendigheid en de betrouwbaarheid van die accounts blijven afzonderlijke kwesties.

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x) houdt geselecteerde profielidentiteiten gekoppeld aan vermeldingen bij het opslaan van concepten en het publiceren. De berichteditor zet het account, de tekst, de vermeldingen en de bijlagen vast tijdens het ondertekenen en verzenden, en bewaart binnenkomende gedeelde inhoud totdat die bewerking is voltooid. Nieuwe pogingen behouden het oorspronkelijke ondertekende event, ook bij oudere berichten die nog op verzending wachten. Een naam typen na @ is niet voldoende: gebruikers moeten een profiel selecteren, en identiteiten die al uit oude concepten verloren zijn gegaan, moeten opnieuw worden geselecteerd.

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0) koppelt communities aan hun bijeenkomsten. Goedkeuring voor een gekoppeld event kan ook het lidmaatschap van de community verlenen zonder een tweede goedkeuring; het aanmeldformulier vermeldt dit en laat aanvragers hiervan afzien. Bestaande deelnemers ontvangen een uitnodiging die ze met één tik kunnen accepteren. Events behouden hun eigen deelnemers, matching en chat, terwijl de community haar events vermeldt. De releaseopmerkingen beschrijven ondersteuning voor verschillende coördinatoren voor events en communities, zonder dat daarmee onafhankelijke tests van interoperabiliteit of versleuteling zijn aangetoond.

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1) verhelpt problemen met de verwerking van [Nostr Wallet Connect](/nl/topics/nip-47/)-betalingen op Android, die kon stoppen wanneer de wallet op de achtergrond draaide en door ophoping kon leiden tot een fout waarbij de applicatie niet meer reageerde. De native release bundelt vijf maanden aan eerdere over-the-airwijzigingen. [Versie 0.4.5 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1) verhelpt NFC-overdracht van Android naar iOS; toekomstige over-the-airupdates vereisen deze versie. Deze oplossingen worden in de release gemeld; verwerking op de achtergrond blijft afhankelijk van de levenscyclusbeperkingen van de telefoon.

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0) laat gebruikers recepten publiceren vanuit de artikeleditor, gedeelde receptenpakketten openen en recepten van gevolgde auteurs bekijken. De websitekaarten en profielrasters die vorige week aan bod kwamen, zijn nu opgenomen in de release, naast de afhandeling van snelheidslimieten van relay en directe `nostr:`-links op Android. Websitelinks staan los van het verifiëren van de inhoud van een site; bij toegang via een gateway wordt een door aanklikken verstuurd verzoek zichtbaar voor die gateway.

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2) verpakt zijn op Nostr gebaseerde Git-ontwikkelplatform voor Android en gebruikt daarbij Amber via [ondertekening op afstand met NIP-46](/nl/topics/nip-46/). De APK opent de bestaande gehoste applicatie `gittr.space`, waardoor gebruikers afhankelijk blijven van de browsercode die deze aanbiedt en van de beschikbaarheid ervan. Ondertekening via browserextensies is binnen deze wrapper niet beschikbaar; zelf hosten blijft een afzonderlijke Git-implementatie.

### Dart NDK

[Dart NDK 0.11.0 development zero](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0) brengt de [handler voor authenticatietoestemming](https://github.com/relaystr/ndk/pull/862) van de Dart- en Flutter-toolkit en het wisselen van relay voor de NIP-46-ondertekenaar naar een prerelease. Deze wijzigingen kwamen vorige week aan bod als samengevoegd werk en zijn nu uitgebracht. De ondertekenaar kan een vervangende relay-lijst volgen, die applicaties blijvend moeten opslaan. [Development one](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1) voegt ondersteuning toe voor NIP-identificatoren met letters in relay-informatie. Beide releases bevatten integratiewijzigingen die de bestaande compatibiliteit doorbreken.

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0) biedt native Android-apps [vier goedkeuringsopties](https://github.com/forgesworn/cambium/pull/32): eenmalig, één uur, één dag of voor onbepaalde tijd. Toestemmingen zijn afgebakend per bewerking en event-kind. Cambium stuurt verzoeken via ondertekening op afstand door naar een Heartwood-hardwareondertekenaar; Heartwood bepaalt nog steeds welke verzoeken het ondertekent. Goedkeuringen voor websites blijven eenmalig. Gekoppelde ondertekenaars krijgen bedieningselementen voor testen en opnieuw verbinden, ondersteuning voor updates van transport-relay en diagnostiek waarin gevoelige gegevens zijn weggelaten. Batches voor [NIP-55, ondertekening op Android](/nl/topics/nip-55/), behouden de volgorde van verzoeken en afzonderlijke afwijzingen, met zichtbare eenmalige toestemming voor ambigue hergebruikte intents.

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1) herstelt de [NIP-42-authenticatie bij relay](/nl/topics/nip-42/) in zijn Go-clientbibliotheek voor applicaties die meerdere gebruikers bedienen. Elke `UserContext` heeft eigen afgeschermde geauthenticeerde verbindingen, relay-voorkeuren en verbindingen die worden opengehouden; de gedeelde pool authenticeert nooit. De bibliotheek valideert inkomende ID's en handtekeningen, controleert of gegevens overeenkomen met abonnementen en serialiseert tag- en tijdfilters correct. Geauthenticeerde aanroepers moeten migreren naar `UserContext`. Opslag en uitlevering door relay blijven ongewijzigd, en authenticatie vereist nog steeds een challenge wanneer de verbinding wordt geopend.

### Nmail

[Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0), een versleutelde mailclient, plaatst onbekende afzenders in Verzoeken en geblokkeerde afzenders in Spam. Acceptaties en blokkeringen worden tussen apparaten gesynchroniseerd. Bestaande afzenders in het postvak IN moeten worden geaccepteerd, met de optie Alles accepteren; Spam blijft stil en wachtende verzoeken voorkomen herhaalde meldingen over afzenders. Antwoorden gebruiken de ontvangende identiteit. Beheer van privé-relay, controles van de apparaatvergrendeling vóór het kopiëren van synchronisatiecodes, gedeelde thema's, uitgebreider behoud van contactgegevens en een Windows-installatieprogramma gaan samen met oplossingen voor het herstellen van de mailbox na een reset of aanmelding.

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0) voegt versleutelde reacties en indicatoren voor ongelezen berichten toe aan zijn via Nostr gesynchroniseerde taakbeheerder. Reacties gebruiken adresseerbare events van kind 35002 met [NIP-44-versleuteling](/nl/topics/nip-44/), waarbij hun koppeling aan de taak binnen de versleutelde tekst blijft. De release [verhelpt problemen met offline verzenden](https://github.com/higedamc/meiso/pull/212), het inhalen van gemiste gegevens na opnieuw verbinden, opstarten met opgeslagen relay en de verspreiding van lege lijsten. Ook voorkomt de release dat gedeeltelijke synchronisatie taken verwijdert. De functies voor ongelezen berichten en het inhalen van gemiste gegevens voegen geen meldingsdienst toe voor een afgesloten applicatie.

### Haps

[Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13), een experimenteel software-installatieprogramma, vereist standaard een audit van de exacte release vanuit het [vertrouwensweb](/nl/topics/web-of-trust/) van de gebruiker. Audits kunnen vastgezette broncode en opnieuw gebouwde artefacten vergelijken en kunnen privé blijven of worden gepubliceerd. [Versie 0.1.14](https://github.com/mmalmi/haps/releases/tag/v0.1.14) vraagt gebruikers de uitgever te bevestigen wanneer ze uitsluitend op naam installeren; automatisering moet een uitgever opgeven. Audits leveren bewijs, terwijl native programma's en bouwrecepten nog steeds zonder sandbox worden uitgevoerd. De auditvereiste kan voor één bewerking worden omzeild; controles van handtekeningen, integriteit en uitgeversbevestiging blijven van kracht.

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0) voegt [het ontdekken en afspelen van livestreams](https://github.com/dmnyc/sidecar/pull/479) toe aan zijn sociale client in de vorm van een browserextensie, met ondertekende chat, reacties en zaps. Opgeslagen streambladwijzers ondersteunen versleutelde accountback-ups en herstel, en privé-instellingen voor het dempen van meldingen laten gebruikers waarschuwingen beheren. De zoekfunctie krijgt opties voor volgen en dempen; daarnaast zijn er wijzigingen in automatische vergrendeling en het vernieuwen van de walletgeschiedenis.

### Ants

De zoekinterface [Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0) [stuurt gestructureerde zoekopdrachten](https://github.com/dergigi/ants/pull/316) zonder aanmelding naar de door auteurs bekendgemaakte schrijf-relay en de lees-relay van genoemde gebruikers via [NIP-65-relay-lijsten](/nl/topics/nip-65/). Het ontdekken beperkt het aantal geraadpleegde identiteiten en relay en stopt bij annulering of een time-out. Bij ontbrekende lijsten blijft terugvalroutering behouden. Tekstzoekopdrachten gebruiken nog steeds geverifieerde [NIP-50-zoek-relay](/nl/topics/nip-50/).

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0), een publicatie- en afspeelprogramma voor napplets voor voorgestelde [NIP-5D-applicaties](/nl/topics/nip-5d/), voegt toetscombinaties en voorstellen zonder fork toe via GRASP, een Git-hostingdienst, met controles van de exacte revisie bij nieuwe pogingen. De [v0.26.0-release](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0) verspreidt ondertekende releases na de primaire publicatie naar geverifieerde outbox-relay; verwijdering houdt bij naar welke bestemmingen verzending is geprobeerd, maar kan onbekende kopieën niet terughalen. [Versie 0.26.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1) verhoogt de limieten voor lezen, afspelen en beoordelen naar 100 MiB, met behoud van een limiet van 25 MiB voor nieuwe builds en publicatie. Latere [directe presentatiemetadata](https://github.com/zeSchlausKwab/napplet-soy/pull/14) plaatsen omslagafbeeldingen en clips van auteurs rechtstreeks op ondertekende manifesten, waardoor het bijbehorende event vervalt. Vastgezette oudere taken blijven ondersteund; deze geversioneerde Soy-uitbreiding vereist compatibele lezers en maakt geen deel uit van de vastgezette NIP-5D-specificatie.

### nostream

De relayserver [nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0) voegt probes voor [NIP-66-relaymonitoring](/nl/topics/nip-66/) toe voor de heen-en-terugtijden van WebSocket-lees- en schrijfbewerkingen, detectie van optionele authenticatie en het ontdekken van mirrors. De server waarschuwt wanneer waargenomen gedrag afwijkt van de [NIP-11-relayinformatie](/nl/topics/nip-11/). OK-antwoorden bij snelheidsbeperking kunnen een optioneel vijfde element bevatten met een wachttijd in milliseconden. [Versie 3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0) voegt een vierde element met een wachttijd in milliseconden toe aan [CLOSED-antwoorden](https://github.com/cameri/nostream/pull/821) wanneer berichtlimieten per IP-adres `REQ` of `COUNT` afwijzen. De versie bevat de [PostgreSQL-kern voor negentropy-reconciliatie](https://github.com/cameri/nostream/pull/809) en een geordende eventinventaris; relayberichten op protocolniveau en het bekendmaken van mogelijkheden volgens [NIP-77](/nl/topics/nip-77/) blijven afzonderlijk werk.

### Bark

[Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15) geeft goedkeuringen voor ondertekening op afstand toetsenbordbediening, expliciete beoordeling van event en identiteit, en [één, vijf of tien minuten om te beslissen](https://github.com/forgesworn/bark/pull/52). Handhaving op de achtergrond wijst verlopen beslissingen en verzoeken in de wachtrij af; als het afleveren van een beslissing mislukt, blijft de pop-up open om het opnieuw te proberen. [Versie 1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17) maakt [NIP-07-browserondertekening](/nl/topics/nip-07/) beschikbaar zodra de handshake met de ondertekenaar is voltooid, terwijl optionele diagnostiek doorgaat. Na updates herstelt de versie bridges op bestaande tabbladen.

### Mostro

[Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3) beantwoordt verzoeken die op identiteit zijn geauthenticeerd om de eigen reputatie van de gebruiker op te vragen, ook zonder openstaande order. De peer-to-peerbeurs stuurt antwoorden privé naar de handelssleutel die het verzoek heeft ingediend, en een [samengevoegd CLI-commando](https://github.com/MostroP2P/mostro-cli/pull/203) maakt die opvraging toegankelijk. Reputatie-import blijft een preview waarvan de importfunctionaliteit niet is geïmplementeerd; beheerders moeten deze uitgeschakeld laten. [Later samengevoegd werk](https://github.com/MostroP2P/mostro/pull/1057) publiceert de veiligheidsmarge van de Lightning-escrowbewaker en wijst onveilige configuraties af; het minimum van 18 blokken gaat uit van LND's standaardinstelling voor het verlopen van hold-invoices.

### Elisym

[Elisym's commerce 0.11.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0) ondersteunt kosten die op de omzet van de handelaar worden ingehouden, met een ondertekende tag in het winkelprofiel die ondersteuning voor gesplitste betalingen aangeeft en weigering van incompatibele winkels wanneer kosten van toepassing zijn. [Samengevoegd werk aan het beheer](https://github.com/elisymlabs/elisym/pull/170) leest orders en aanbiedingen van Nostr-relays. Het vraagt om de geheime sleutel van de winkel, waardoor vertrouwen in de aangeboden browsercode en extensies vereist is; het lokale beheer blijft beschikbaar. Gehoste uitrol en activering van kosten op mainnet blijven ongeverifieerd. [Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0) werkt zijn grootboek bij zonder ondersteuning voor downgraden.

### Routstrd

[Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16) voorkomt dat een [Nostr Wallet Connect](/nl/topics/nip-47/)-aanvulling na een time-out onmiddellijk een nieuwe betaalbare factuur oplevert. Het [controleert de bestaande mintbewerking](https://github.com/Routstr/routstrd/pull/144) totdat de betaling slaagt of mislukt; bij een niet-beschikbare status blijft de aanvulling gepauzeerd. De inferentiegateway schakelt aanbieders in op basis van een Nostr-beoordelingslabel, waarbij experimentele labels expliciete aanmelding vereisen. [Versie 0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17) bevat de ondersteunende SDK. De beveiliging tegen onafgewikkelde bewerkingen blijft in het geheugen, dus bij het herstarten van de daemon gaat die bescherming verloren.

### Buzz

[Buzz desktop 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28) laat geauthenticeerde medewerkers [elke community op een relay bekijken en modereren](https://github.com/block/buzz/pull/8027) zonder van verbinding te wisselen. Beheeracties behouden de beoordeelde community, relay en ondertekenaar; bij uitgeschakelde authenticatie blijft de console beschikbaar om te lezen. Afzonderlijk [samengevoegd werk aan de relay](https://github.com/block/buzz/pull/8197) verbergt correct getagde verwijderingsevents voor privéauteursrecords bij zowel opvragingen als livelevering. Die serverreparatie vereist uitrol en laat eerder openbaar gemaakte kopieën en historische ongetagde verwijderingsrecords buiten de oplossing.

### Earthly

[Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21) laat gebruikers [openbare Nostr-kaartdatasets insluiten op websites](https://github.com/zeSchlausKwab/earthly/pull/35), met een voorbeeldweergave en instellingen voor het uiterlijk en de initiële camerapositie. De Maps MCP-integratie maakt en publiceert kaarten vanuit een chat en genereert vervolgens deellinks of insluitingen. De integratie blijft een persoonlijke pilot met een gekoppelde plug-in. Insluitingen ondersteunen inline datasets met maximaal 300 objecten en 48 KiB; privé-, ongepubliceerde en op blobs gebaseerde datasets zijn uitgesloten.

### Milk Market

[Milk Market's mobile v0.3.0](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0) brengt volledige ontwerpeditors voor webwinkels naar de verkopersapp, met dezelfde secties en velden als de webeditor. Het paginaontwerp per product kan thema- en sectiekeuzes overschrijven, inclusief metadata en afbeeldingen voor sociale media. De release voegt controles toe om mobiele en webconfiguraties op elkaar afgestemd te houden. [Versie 0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1) corrigeert het contrast in de mobiele voorbeeldkaart; Android-downloads zijn bij de releases gevoegd en iOS is beschikbaar via TestFlight.

### Zeus

[Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3) bevat de [reparatie voor LDK-routeringskosten](https://github.com/ZeusLN/zeus/pull/4353) die vorige week werd besproken en nu is uitgebracht. De op LDK gebaseerde Nostr Wallet Connect-dienst kan gerapporteerde routeringskosten opnemen in antwoorden en uitgavenregistraties. Budgetcontroles hebben nog steeds betrekking op het factuurbedrag vóór afwikkeling, waarbij afgeronde kosten achteraf worden afgeschreven en een afzonderlijk maximum van 1.000 satoshi voor routeringskosten geldt. De release werkt ook de ingebouwde LND bij en bevat beveiligingsoplossingen voor rust-lightning; livevalidatie met NWC-apparaten blijft ongeverifieerd. De later [samengevoegde verwijdering van Zaplocker](https://github.com/ZeusLN/zeus/pull/4933) beëindigt de Nostr-attestatie- en inwisselprocedure ervan. Upgraden terwijl betalingen nog door die server worden vastgehouden, verwijdert de mogelijkheid tot inwisselen; afzenders moeten wachten tot de hold-invoice verloopt en terugbetaling plaatsvindt. Die uitfasering valt buiten v13.2.3; uitrol is afhankelijk van het uitschakelen van de server en het waarschuwen van bestaande gebruikers.

## In ontwikkeling

### nosvelte

[De reparatie van nosvelte's eventverificatie](https://github.com/akiomik/nosvelte/pull/162) controleert de aangeleverde ID van een event aan de hand van de canonieke hash van de velden voordat de handtekening wordt geverifieerd. De standaardverificator van de Svelte-bibliotheek accepteerde voorheen correct ondertekende velden met een vervangen ID, waardoor inhoud de identiteit van een ander event kon innemen en de afhandeling van vervangingen kon verstoren. De samengevoegde wijziging is van toepassing op verzoek- en verzendpaden van versie één die de standaardverificator gebruiken; ze bevestigt niet de correctheid van de verouderde export of aangepaste verificatoren volgens [het eventformaat van NIP-01](/nl/topics/nip-01/). Een latere [reparatie van verzoekfilters](https://github.com/akiomik/nosvelte/pull/171) controleert en kopieert eventvelden van relays voordat deze worden vergeleken. Ongeldige gegevens kunnen niet langer het abonnement van de standaardprovider beëindigen of het volgende geldige event ervan doen vervallen. Door de aanroeper aangeleverde engineclients kunnen het eerdere vergelijkingsgedrag van afhankelijkheden behouden.

### nostter

nostter [beperkt extern aangeleverde relayhints](https://github.com/SnowCait/nostter/pull/2684) tot beveiligde WebSocket-URL's en wijst lokale hostnamen en niet-globale IP-adressen af. Lokaal door het account geselecteerde relays en URL's van externe ondertekenaars behouden hun bestaande paden; DNS-rebinding valt buiten de controle. De webclient [leest ook experimentele afzonderlijke payloads voor inhoudswaarschuwingen](https://github.com/SnowCait/nostter/pull/2680), maar pas nadat de lezer op Tonen drukt, waarbij de ID van het event waarnaar wordt verwezen, de overeenkomende auteur en een `k` tag die overeenkomt met de kind van het oorspronkelijke event worden gecontroleerd. Reacties en antwoorden zijn gericht op het oorspronkelijke event. Deze samengevoegde wijzigingen laten het huidige publicatieformaat volgens [NIP-36](/nl/topics/nip-36/) ongewijzigd.

### Coracle

[Coracle's lijsteditor](https://github.com/coracle-social/coracle/pull/679) herstelt bewerken en verwijderen door op asynchrone decodering te wachten voordat het formulier wordt weergegeven. Voorheen gingen bij het bewerken de velden van de lijst verloren en publiceerde noch opslaan noch verwijderen een event.

### Routstr Core

[De broncode van Routstr Core’s huidige versie 0.5.0](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0) [logt automatisch gegenereerde Nostr-privésleutels niet meer](https://github.com/Routstr/routstr-core/pull/812) en [behoudt de publieke identiteit van de eerste opstart](https://github.com/Routstr/routstr-core/pull/818). [Provideraankondigingen](https://github.com/Routstr/routstr-core/pull/823) sluiten localhost en letterlijke private of link-local HTTP-adressen uit; hostnamen worden voor deze controle niet naar IP-adressen vertaald. De huidige tag bevat werk dat is samengevoegd na de vastgelegde publicatiedatum van 7 oktober, dus historische binaries en implementaties zijn nog niet geverifieerd. Eerder blootgestelde logs moeten nog steeds door de beheerder worden gecontroleerd.

### Alby Hub

[De wijziging in factuurautorisatie van Alby Hub](https://github.com/getAlby/hub/pull/2629) beperkt afwikkeling en annulering tot facturen die door de aanvragende app zijn aangemaakt. De zelfgehoste wallet biedt appverbindingen aan via [NIP-47, Nostr Wallet Connect](/nl/topics/nip-47/); de mogelijkheid van een verbinding om haar eigen facturen te beheren mag geen bevoegdheid geven over de facturen van een andere app. Een afzonderlijke [privacyreparatie voor geïsoleerde verbindingen](https://github.com/getAlby/hub/pull/2621) verwijdert het Lightning-adres van de hoofdwallet uit de succesroutes in de browser voor geïsoleerde verbindingen.

### nak

[Het samengevoegde relay-commando van nak](https://github.com/fiatjaf/nak/pull/222) meet verbindings-, lees- en schrijftijden en vraagt relay-informatie op, waarna het ongetekende discovery-events van kind 30166 afdrukt. Door die resultaten via een pipe naar `nak event` te sturen, worden ondertekening en publicatie verzorgd, waardoor geplande [NIP-66-relaymonitoring](/nl/topics/nip-66/) mogelijk wordt met hetzelfde terminalhulpmiddel. Waargenomen antwoorden over authenticatie of beperkingen hebben voorrang op de door de relay gepubliceerde informatie. Schrijfproeven gebruiken een tijdelijk event dat met een wegwerpsleutel is ondertekend; monitoraankondigingen van kind 10166 blijven een afzonderlijke handeling.

### Kehto

[De manifestverificatie van Kehto](https://github.com/kehto/web/pull/277) controleert vóór uitvoering de huidige ondertekende manifesten voor één artefact en de bytes van dat artefact, waarbij de verwerking van oudere formaten gescheiden blijft. De napplet-shell [verifieert ook aanbevolen handlers](https://github.com/kehto/web/pull/294), vraagt gebruikers naar conflicten met opgeslagen keuzes en verbruikt een geaccepteerde aanroep-URL om herhaalde aflevering te voorkomen. Manifestverificatie controleert de identiteit van de uitgever en de bytes van het artefact; ze stelt niet vast dat de applicatiecode veilig is. [Gamepadmomentopnamen](https://github.com/kehto/web/pull/297) volgen nu de focus en zichtbaarheid. Paja/playground-frames blokkeren directe native toegang tot gamepad, HID en USB voordat applicatiecode wordt uitgevoerd, zodat bemiddelde toegang aan de host wordt overgelaten. Gebruikers van deze functionaliteit hebben de bijbehorende hostpakketten nodig; gereedheid van de shell is een afzonderlijke capaciteit. Een latere [wijziging in de toelating door Paja](https://github.com/kehto/web/pull/305) waarschuwt voor niet-beschikbare experimentele vereiste domeinen, maar staat laden toe; die domeinen bieden nog steeds geen API’s of toegekende rechten.

### napplet SDK

[De napplet SDK implementeert URI-gebaseerde aanroepen en bewaarde aflevering](https://github.com/napplet/web/pull/228). [Publicatiemetadata blijft behouden in zelfstandige HTML](https://github.com/napplet/web/pull/226), en [optionele applicatieverwijzingen](https://github.com/napplet/web/pull/239) verbinden manifesten met ondertekende vermeldingen en schermafbeeldingen zonder artefacthashes te wijzigen. Het formaat voor applicatieverwijzingen blijft een voorstel. Tests van de referentieshell laten ontdekking, installatie en handtekeningverificatie in productie aan hosts over.

### rust-nostr

De Rust Nostr-bibliotheek [rust-nostr behoudt gedeeltelijke downloadvoortgang naast definitieve relay-fouten](https://github.com/nostrdevkit/nostr/pull/1483). De mislukte relay blijft in de verzameling mislukte relays staan, zodat aanroepende code reeds ontvangen events kan gebruiken zonder het bewijs te verliezen dat de synchronisatie voortijdig is gestopt.

### Pensieve

[De veiligheidsreparatie voor reconciliatie van Pensieve](https://github.com/andotherstuff/pensieve/pull/92) volgt op het [werk aan uitsluiting van ontbrekende events](https://github.com/andotherstuff/pensieve/pull/90). De relay- en archiveringshulpmiddelen vragen de exacte ontbrekende ID’s opnieuw op voordat ze fouten classificeren, zodat afgekapte uiteinden van queryresultaten niet tot onterechte uitsluitingen leiden. Pauzes worden per taak bijgehouden en reeds gearchiveerde events worden afzonderlijk afgehandeld. Een voltooide taak kan expliciete registraties van ontbrekende events behouden; voltooiing alleen bewijst niet dat een archief volledig is.

[Doorlopende Premium Primal-reconciliatie](https://github.com/andotherstuff/pensieve/pull/84) werd op 12 oktober ingeschakeld. Het [implementatieverslag](https://github.com/andotherstuff/pensieve/pull/93) van de beheerder meldt dat beide gerepareerde binaries op 13 oktober in gebruik zijn genomen en dat pauzeren op basis van fouten toen is ingeschakeld. Het latere [overnemen van uitsluitingen](https://github.com/andotherstuff/pensieve/pull/95) hergebruikt alleen oorspronkelijke, bewezen uitsluitingen voor dezelfde relay en een overlappend tijdvenster, met uitsluiting van ketens van overgenomen uitsluitingen en nieuw bijgemengde ID’s; de [ingebruikname werd die middag vastgelegd](https://github.com/andotherstuff/pensieve/pull/97). De [voorafgaande archiefcontrole en reparatie van vastlopende caches](https://github.com/andotherstuff/pensieve/pull/98) werd [op 14 oktober in gebruik genomen](https://github.com/andotherstuff/pensieve/pull/99). Een latere [reparatie van de prioriteit bij het overnemen](https://github.com/andotherstuff/pensieve/pull/103) is samengevoegd, maar volgens de bijbehorende bronregistratie nog niet in gebruik genomen.

### njump

De Nostr-webviewer [njump herstelt de ingebouwde relay-standaardinstellingen](https://github.com/fiatjaf/njump/pull/173) wanneer er geen bestand met vervangende instellingen wordt aangeleverd. Ook [isoleert hij gelijktijdige Markdown-renderers](https://github.com/fiatjaf/njump/pull/171) en [antwoordheaders tijdens time-outs](https://github.com/fiatjaf/njump/pull/169), waarmee racecondities worden verholpen die het proces konden laten crashen tijdens het weergeven van geciteerde lange events of het afhandelen van gelijktijdige verzoeken. Dit zijn samengevoegde serverwijzigingen; ingebruikname in de liveomgeving is nog niet geverifieerd.

### Nostr Components

[De reparatie van zap-ondertekening in Nostr Components](https://github.com/saiy2k/nostr-components/pull/187) stopt het betalingsproces wanneer de geselecteerde ondertekenaar weigert. De in te sluiten sociale widgets gebruiken na een weigering niet langer een willekeurige anonieme identiteit als vervanging. Hun [aggregatie van ontvangstbewijzen](https://github.com/saiy2k/nostr-components/pull/197) valideert [NIP-57-zap-ontvangstbewijzen](/nl/topics/nip-57/) voordat duplicaten van relay-kopieën, facturen en verzoek-ID’s worden verwijderd.

### rx-nostr

De [verificatiewijzigingen in versie vier van de reactieve clientbibliotheek rx-nostr](https://github.com/penpenpng/rx-nostr/pull/207) controleren de canonieke event-structuur, ID’s en handtekeningen op consistente wijze in JavaScript en WebAssembly. Een lege lijst met verzoekvoorwaarden komt met niets overeen en wordt voltooid; verzending via de oude methode meldt een fout wanneer er geen bestemming is. Publicatie-observers kunnen de afwikkeling niet wijzigen, en afgeleide verzoeken die zijn opgeruimd kunnen niet opnieuw starten. [Eindige querysegmenten](https://github.com/penpenpng/rx-nostr/pull/213) maken het mogelijk achterwaartse query’s te voltooien nadat alle aangeleverde segmenten zijn afgerond. Deze wijzigingen zijn opgenomen in [4.0.0 beta 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2), een prerelease met niet-achterwaarts compatibele API-wijzigingen.

### eHagaki

De sociale client [eHagaki voegt gefaseerde outbox-aflevering toe](https://github.com/Lokuyow/ehagaki/pull/268), waarbij de relay-doelen van de auteur vóór ondertekening worden vastgezet. Het proces voor gevoelige berichten stuurt elke relay de payload vóór de structuur die ernaar verwijst, op basis van de eigen ontvangstbevestiging van die relay; wanneer alleen de payload succesvol is afgeleverd, blijft het berichtopstelvenster behouden. Een [volledige scan van de berichtgeschiedenis](https://github.com/Lokuyow/ehagaki/pull/312) slaat geverifieerde resultaten stapsgewijs op. Onduidelijke bereiken blijven onbevestigd, zelfs wanneer de scan als voltooid wordt weergegeven, met een informatieknop die dit uitlegt. [Ondersteuning voor de lokale relay Citrine](https://github.com/Lokuyow/ehagaki/pull/315) behoudt geverifieerde weergavebereiken en archiveert exacte ondertekende events na succesvolle externe publicatie. Lokale ontvangstbevestigingen maken een mislukte externe verzending niet succesvol, en dit voegt geen wachtrij voor offline publiceren toe. [Beheer van geüploade media](https://github.com/Lokuyow/ehagaki/pull/321) toont en verwijdert geüploade afbeeldingen en video’s op ondersteunde NIP-96- en Blossom-servers. Een [latere databasemigratie](https://github.com/Lokuyow/ehagaki/pull/325) wist de gecachte weergave- en berichtgeschiedenis, maar behoudt concepten en verwijderingsverzoeken. Ze voorkomt ook dat oudere synchronisatieresultaten in de wachtrij de geschiedenis na het wissen opnieuw vullen.

### Formstr

[De oplossing van Formstr voor indieningsresultaten](https://github.com/formstr-hq/nostr-forms/pull/508) wijst een formulierantwoord af wanneer geen enkele relay het accepteert. De Nostr-formulierenapplicatie toont de resultaten per relay en biedt de mogelijkheid om het opnieuw te proberen met behoud van de ingevulde antwoorden. Webhooks en bevestigingspagina's wachten op acceptatie, en de SDK krijgt dezelfde controle. Een bevestiging van een relay is nog steeds iets anders dan gegarandeerde langdurige opslag, maar een volledig mislukte publicatie levert niet langer een succesmelding op.

### Auditable Voting

[Auditable Voting voegt optionele bundeling van stembiljetten via een private worker toe](https://github.com/tidley/auditable-voting/pull/35). Door de organisator ondertekende definities selecteren een worker-identiteit, DM-relays en een vrijgavedrempel of deadline. Kiezers versturen [gift-wrapped stembiljetten volgens NIP-17](/nl/topics/nip-17/) en authenticeren ontvangstbewijzen aan de hand van die worker; delegaties moeten zowel het in de wachtrij plaatsen als de vrijgave autoriseren. Vrijgegeven stembiljetten gebruiken de identiteit van de worker. De worker kan inzendingen lezen, en bundels die op een deadline worden vrijgegeven, kunnen klein zijn. Als er geen geldige private route kan worden bepaald, valt de onderzochte client terug op openbare indiening. Dit is ontwikkelwerk dat in de codebasis is opgenomen.

### MintRadar

[MintRadar voegt optionele gift-wrapped waarschuwingen toe](https://github.com/hroomnik007/MintRadar/pull/122) voor mint- of melt-problemen, verouderde software en weggevallen ondersteuning voor die bewerkingen. De Cashu-mintcatalogus [koppelt de bediening van de volglijst](https://github.com/hroomnik007/MintRadar/pull/123) aan die meldingsinstellingen en bevestigt ze nadat de server heeft gereageerd. Atomaire claims voorkomen dat overlappende controles dezelfde waarschuwing versturen, en bij een mislukte publicatie naar een relay wordt de claim vrijgegeven voor een nieuwe poging. [Privéberichten volgens NIP-17](/nl/topics/nip-17/) beschermen de inhoud van de meldingen; acceptatie door een relay bevestigt niet dat de ontvanger ze heeft gelezen.

### Nostr Docs

[De migratie van Nostr Docs naar een lokale relay](https://github.com/formstr-hq/nostr-docs/pull/65) leidt lees- en schrijfbewerkingen van de gezamenlijke Markdown-editor via een Web Worker met een IndexedDB-eventcache en een uitgaande wachtrij voor herhaalpogingen. Documenttitels en tags blijven behouden na het herladen, en opeenvolgende metadatabewerkingen krijgen oplopende tijdstempels, zodat twee bewerkingen binnen één seconde van elkaar te onderscheiden blijven. De bestaande opslag van versleutelingssleutels blijft intact. De terugvaloptie via de netwerkpool mist de duurzame opslag van de uitgaande wachtrij van de worker, en acceptatie van een publicatie in de wachtrij betekent niet dat een relay deze heeft geaccepteerd.

### Pakstr

[De native lokale signer van Pakstr](https://git.nostrdev.com/stuff/pakstr/pulls/105) laat de Android-applicatieshell op het apparaat een Nostr-account aanmaken. De sleutel blijft in de native laag, versleuteld met een wrapping key die door Android Keystore wordt beschermd. Ondertekeningsresultaten worden geverifieerd voordat ze aan de webapplicatie worden teruggegeven. De shell ondersteunt [browserondertekening volgens NIP-07](/nl/topics/nip-07/) en versleutelde verzoeken. De selectie van een signer wordt pas geopend wanneer dat nodig is en coördineert gelijktijdige verzoeken.

### Nostr WoT SDK

De web-of-trust-bibliotheek [Nostr WoT SDK breidt toestemming voor authenticatie uit](https://github.com/nostr-wot/nostr-wot-sdk/pull/15) naar getypeerde native en externe aanvragers. Opgeslagen weigeringen worden gecontroleerd voordat toestemmingsvragen verschijnen, en herbruikbare toestemming is gebonden aan het aanvragende transport en de bestemming. Webverzoeken blijven standaard eenmalig. De [beheerde Blossom-uploads](https://github.com/nostr-wot/nostr-wot-sdk/pull/13) valideren onveranderlijke bytes, ondersteunen annulering en stoppen wanneer de actieve sessie verandert, met servergebonden authenticatie en beperkingen voor doorverwijzingen.

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49) biedt desktopinstallatieprogramma's. Los daarvan [voegt in de codebasis opgenomen serverwerk duurzame geplande publicatie toe](https://github.com/flox1an/nostube/pull/126). Events worden vóór hun geplande tijdstip ondertekend, in SQLite opgeslagen en gepubliceerd door een worker die achterstanden na uitval inhaalt. De [bewerkings- en verwijderingsprocedure](https://github.com/flox1an/nostube/pull/124) houdt tombstones, levering aan mirrors en het opruimen van eigen bestanden bij. [De eerste configuratie](https://github.com/flox1an/nostube/pull/134) maakt onderscheid tussen de browsersigner van een gebruiker en een door de server beheerde kanaalsleutel. Historische blobs zonder eigenaar blijven buiten de automatische opruiming.

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24) voegt besloten samenwerking aan clips toe, met naamsvermelding en controles op ondertekende herkomstgegevens van opnamen of bewerkingen. Door kijkers geselecteerde vertaalde ondertitels vallen terug op de originelen zolang de vertaling nog niet klaar of niet geverifieerd is. Deze herkomstcontroles garanderen niet dat een opname onbewerkt is.

De [routeringswijzigingen](https://github.com/divinevideo/divine-mobile/pull/9884) van de client voor korte video's raadplegen de inbox-relays van ontvangers voor tekst- en videochatberichten en behouden onzekere afleverresultaten. [De verwerking van afzenderkopieën](https://github.com/divinevideo/divine-mobile/pull/10006) zorgt ervoor dat eigen groepsberichten van gebruikers op hun andere apparaten verschijnen; voor eerder weggegooide kopieën moet het account opnieuw worden geïmporteerd. [Geannuleerde gedeeltelijke groepsverzendingen](https://github.com/divinevideo/divine-mobile/pull/10031) behouden vermeldingen met ‘Niet naar iedereen verzonden’; annulering is definitief en deze vermeldingen kunnen niet opnieuw worden verzonden. Het aanmaken van groepen en het herkennen van nieuwe, door gesprekspartners gestarte gespreksruimten blijven [achter een standaard uitgeschakelde vlag](https://github.com/divinevideo/divine-mobile/pull/10020).

Latere wijzigingen in de main-branch [houden kopieën van onderbroken databaseherstel buiten de tijdelijke cache](https://github.com/divinevideo/divine-mobile/pull/10118) en [behouden geplande berichten, meldingen in de wachtrij, profielbewerkingen en registraties van verwijderde chats tijdens het opnieuw opbouwen](https://github.com/divinevideo/divine-mobile/pull/10115). [Verzenddeadlines omvatten het opnieuw verbinden met relays](https://github.com/divinevideo/divine-mobile/pull/10127), waardoor de drempel voor het opnieuw proberen van een afgebroken verzending van 160 naar 137 seconden daalt. [Inbox-opzoekingen via de indexer gebruiken een aparte begrensde pool](https://github.com/divinevideo/divine-mobile/pull/10116) om te voorkomen dat ze achter feedleesbewerkingen moeten wachten, en [volgknoppen behouden de gekozen actie](https://github.com/divinevideo/divine-mobile/pull/10147) als de contactenlijst vóór de bevestiging verandert. Deze latere samenvoegingen laten minder tijd over voor een bevestiging van de relay wanneer het opnieuw verbinden traag verloopt; databasereparaties kunnen eerder verloren gegevens niet herstellen. Latere [optionele opnamekopieën](https://github.com/divinevideo/divine-mobile/pull/10110) maken het mogelijk om nieuw opgenomen clips te bewaren via galerijback-ups op Android en iOS. Kopieën zonder ondertekende herkomstgegevens krijgen een waarschuwing en kunnen niet opnieuw worden geïmporteerd; dit staat standaard uit en vereist extra opslagruimte.

### Conduit

De handelsapplicaties in [Conduit krijgen een gedeelde duurzame inbox](https://github.com/Conduit-BTC/conduit-mono/pull/616), met behoud van versleutelde berichtaflevering en herstel tussen Market en Merchant. Acceptatie door de relay van de ontvanger blijft behouden als de zelfkopie van de afzender mislukt, waarbij herstel dezelfde bytes hergebruikt om een tweede semantische verzending te vermijden. [Gedeelde wallets op basis van signers](https://github.com/Conduit-BTC/conduit-mono/pull/635) verbinden beide applicaties. Dat herstelpad vertrouwt de signer de onversleutelde herstelgegevens toe; integratie in de broncode op zichzelf bewijst noch een live-implementatie, noch acceptatietests met daadwerkelijk geld. [Onafhankelijke relaymachtigingen](https://github.com/Conduit-BTC/conduit-mono/pull/645) blijven behouden wanneer meerdere accountroutes een URL delen. Het uitschakelen van één route wist niet langer een andere ondertekende relaylijst of inboxmachtiging, en leesbewerkingen die authenticatie vereisen of onvolledig zijn, behouden de uitkomst ‘niet beschikbaar’. De [in de codebasis opgenomen betalingsrouter](https://github.com/Conduit-BTC/conduit-mono/pull/613) splitst één door de koper goedgekeurde financieringsbetaling in Lightning-uitbetalingen aan de handelaar en de leverancier, gevolgd door de Conduit-vergoeding, met afstemming op de exacte betaalintentie en versleuteld herstel via de gedeelde Nostr-inbox. Uitvoering in productie en staging blijft uitgeschakeld; voltooiing door de dienstverlener bewijst niet dat de ontvanger het bedrag heeft opgeëist of dat de betaling definitief is afgesloten.

### Bitcredit

[De versleuteling van persistent opgeslagen gegevens van Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041) beschermt de identiteits-, bedrijfs- en wisselsleutels van de applicatie voor elektronische wissels, inclusief de Nostr-wachtrij voor opnieuw verzenden, met behulp van de mnemonische herstelzin van de persoonlijke identiteit. Initialisatie vereist een bijpassende mnemonische herstelzin. [Instantiebeheer](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043) laat testnet- en mainnet-instanties hun Nostr-abonnementen op de achtergrond onafhankelijk van elkaar op één apparaat actief houden.

## Nieuwe projecten

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0) brengt een wachtwoordmanager uit waarvan de versleutelde kluizen via Nostr synchroniseren. Hij ondersteunt externe ondertekenaars en bewaart gelijktijdige versies van items, met import en export in Bitwarden JSON-formaat. Wijzigingen worden lokaal opgeslagen voordat op acceptatie door een relay wordt gewacht. Bij de release zijn downloads voor Android, desktop en CLI beschikbaar. Het project noemt zichzelf pril en raadt voor kritieke wachtwoorden een beproefde manager aan; de protocolspecificatie bij deze versie is nog leeg. De [webopslag](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md) bewaart de versleutelingssleutel naast de beschermde gegevens.

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md) voegt een Common Lisp-implementatie van MLS-groepschat via Nostr toe. Code van 9 oktober voegt convergentie bij concurrerende commits en versleutelde Blossom-bijlagen toe, met door de auteur gerapporteerde interoperabiliteitstests met de wn-opdrachtregelclient van MDK. De implementatie is niet geaudit en accountsleutels en berichtlogboeken worden niet versleuteld opgeslagen. Tijdgebonden convergentievensters, replay voorbij de terugrolhorizon en het ontbinden van groepen zijn nog niet geïmplementeerd; de onderzochte testopstelling gebruikt tijdelijke lokale relays.

### nalgorithm Android

[De Android-release van nalgorithm](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0) stelt een op voorkeuren gerangschikte Nostr-feed samen en maakt op de achtergrond een audiosamenvatting die offline kan worden afgespeeld. Gebruikers kiezen tussen gehoste inferentie met tarieven in Lightning en inferentie met een eigen sleutel die vanaf de telefoon wordt aangevraagd; dit zijn afzonderlijke routes. Aanmelden ondersteunt Amber via ondertekening op afstand. Vervolgreleases [herstellen de rangschikking met een eigen sleutel en het vinden van volglijsten](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1), en [behouden vervolgens likes van werkende relays wanneer een andere relay uitvalt](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2) en verbeteren het herstel van samenvattingen. [Versie 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3) wijzigt de volgorde van de modelconfiguratie en meldt ontbrekende invoer voor verbindingstests.

## Werk aan protocollen en specificaties

### Geauthenticeerde napplet-eindpunten

In de NAP-specificaties voor napplet-applicaties vervangen [NAP-INC-eindpuntidentificatoren](https://github.com/napplet/naps/pull/104), op 9 oktober samengevoegd, kale handlernamen door geauthenticeerde identificatoren. Gelijke namen van verschillende uitgevers identificeren niet langer dezelfde peer. De runtime blijft de communicatie bemiddelen en root- of snapshotmanifesten hebben geen benoemde `d`-coördinaat nodig.

### Handleraanbevelingen in aanroeplinks

[De aanbeveling in aanroeplinks](https://github.com/napplet/naps/pull/99), eveneens op 9 oktober samengevoegd, maakt een optionele `#naddr`-handleraanbeveling mogelijk. Een shell kan zoek- en installatiemogelijkheden bieden, met de gewone resolutie als terugvaloptie. Opgeslagen voorkeuren en het shellbeleid hebben voorrang. Een aanbevolen handler biedt dus een aanwijzing voor het vinden van een handler, zonder de bestaande keuze van de gebruiker te vervangen of de bevoegdheid om te installeren aan de afzender van de link over te dragen.

### Acceptatie van bezorging en applicatiewerk

[De wijzigingen in intentieadvertenties en bezorging](https://github.com/napplet/naps/pull/91) leiden rollen en intenties af uit hetzelfde geverifieerde manifest, met identificatoren die veilig zijn voor uitgevers. Acceptatie van de bezorging hangt er niet langer van af of de bronapplicatie actief blijft. Een antwoord met `ok: true` aanvaardt de verantwoordelijkheid voor de bezorging; het betekent niet dat het applicatiewerk aan de bestemmingskant is voltooid. Het gedrag bij nieuwe pogingen en herstarts blijft onder deze samengevoegde specificatiewijziging onderdeel van het runtimebeleid.

### Actieketens in Cyberspace

[De herziene ketenregels van Cyberspace](https://github.com/arkin0x/cyberspace/pull/48) laten een fork een ondertekende actieketen vanaf het ontstaan ervan ongeldig maken en vereisen dat clients de actuele ketenkop bevestigen voordat ze een volgende actie ondertekenen. De op Nostr gebaseerde wereld voegt [140 ondertekende synthetische ketens](https://github.com/arkin0x/cyberspace/pull/49) toe met normatieve oordelen voor implementaties. [Regels voor bronvermelding bij kopieën](https://github.com/arkin0x/cyberspace/pull/47) gebruiken `q`-verwijzingen naar het oorspronkelijke object en stellen de auteur daarvan op de hoogte bij openbare remixen; verzegelde kopieën laten die melding achterwege. Dit zijn samengevoegde projectspecificaties; in hoeverre uitgerolde verifiers ze afdekken, is niet geverifieerd.

### Bevestigingen van persistente opslag door relays

[Het openstaande voorstel voor persistente opslag](https://github.com/nostr-protocol/nips/pull/2496) introduceert bevestigingen van persistente opslag, PROOF-query's en optionele ondertekende relay-attestaties van kind 1797. Een handtekening maakt een opslagclaim toerekenbaar aan een relay; zij bewijst niet dat de gegevens bewaard blijven. Query's onthullen ook in welke events de client geïnteresseerd is.

### Gedeelde vastgezette berichten voor Marmot-groepen

[Het openstaande voorstel van Marmot voor vastgezette berichten](https://github.com/marmot-protocol/marmot/pull/434) definieert een geauthenticeerde gedeelde toestand voor maximaal 64 berichtverwijzingen, met rechten voor leden en beheerders. Daadwerkelijke wijzigingen vereisen een MLS Commit en een epoch-overgang, en elk resulterend ledenblad moet de functie ondersteunen. Vastgezette verwijzingen kopiëren geen berichtinhoud en verlengen de bewaartermijn niet, dus niet-beschikbare doelen blijven onopgelost. De meegeleverde testgegevens gaan uit van een geauthenticeerde toestand; ze tonen geen cryptografische verwerking of convergentie tussen clients aan.

## NIP nader bekeken: NIP-36 en NIP-38

### Inhoudswaarschuwingen vóór weergave

[NIP-36, gevoelige inhoud](/nl/topics/nip-36/), laat auteurs een `content-warning`-tag aan een event toevoegen, eventueel met een reden. Een client kan de inhoud verbergen totdat de lezer ervoor kiest die te tonen. De [specificatie](https://github.com/nostr-protocol/nips/blob/master/36.md) laat de interface aan clients over en staat aanvullende label-tags toe. Een waarschuwing toevoegen verandert niet wie het event kan lezen. Bij een openbaar bericht ontvangen relays en andere clients de inhoud nog steeds.

[De parser voor waarschuwingstags van Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) herkent de tag en behandelt een ontbrekende of lege reden als niet opgegeven. [De berichteditor van Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte) schrijft de reden in de tag; de [inhoudsweergave](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) respecteert de instelling van de lezer voor gevoelige inhoud en biedt een actie om de inhoud te tonen. [De berichtweergave van noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) past de eigen waarschuwingsvoorkeur en uitgevouwen toestand toe voordat de waarschuwingsinterface wordt getoond.

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md) versleutelt events niet en verplicht niet tot verbergen. Het ontbreken van een waarschuwing zegt niets over de inhoud; clients bepalen hoe waarschuwingen voorvertoningen en bedieningselementen voor het tonen van inhoud beïnvloeden.

### Profielstatus en vervaltijd

[NIP-38, gebruikersstatussen](/nl/topics/nip-38/), gebruikt adresseerbare events van kind 30315. De auteur, kind en de `d`-tag identificeren een statuscoördinaat; `general` en `music` hebben een vastgelegde betekenis. Een nieuwer event vervangt de vorige status op die coördinaat, terwijl een andere `d`-waarde afzonderlijk blijft. Lege inhoud wist een status. De [specificatie](https://github.com/nostr-protocol/nips/blob/master/38.md) staat ook verwijzingen naar URL's, profielen, events en adressen toe.

Dit ondertekende [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md)-event toont een verlopen algemene status. De oorspronkelijke spelling van de auteur is behouden.

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[Het statusmodel van Damus](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift) verwerkt algemene en muziekstatussen met een vervaltijd. [De statusservice van Nostria](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts) negeert lege of verlopen waarden en publiceert muziekstatussen op basis van de duur van het nummer; de gebruikelijke abonnementen vragen alleen algemene en muziektypen op. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt) behoudt de identificatie `d` bij het wissen van een status. Aangepaste typen vereisen daarom afspraken die verder gaan dan de gedeelde structuur voor gegevensoverdracht.

Statussen zijn openbare verklaringen van de auteur. Ze bewijzen niet dat iemand online is of naar een nummer heeft geluisterd. Het publiceren van muziek of beschikbaarheid kan gewoonten onthullen, en een optionele vervaltijd beperkt de weergave van verouderde informatie zonder verwijdering te garanderen. [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) blijft een optionele conceptspecificatie, net als NIP-36. Clients kunnen beide onafhankelijk van elkaar implementeren, waarbij hun weergave-instellingen bepalen wat lezers zien.
