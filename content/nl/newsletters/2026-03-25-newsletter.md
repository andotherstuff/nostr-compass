---
title: 'Nostr Compass #15'
date: 2026-03-25
translationOf: /en/newsletters/2026-03-25-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [Primal Android](https://github.com/PrimalHQ/primal-android-app) bouwt verder op zijn 3.0-walletrelease met [Follow Packs, zap-verrijking en `primalconnect://` deep links](#primal-voegt-follow-packs-zap-verrijking-en-deep-links-toe). [BigBrotr](https://github.com/BigBrotr/bigbrotr) publiceert een [analyse van gelekte nsec-sleutels](#bigbrotr-brengt-blootgestelde-prive-sleutels-over-het-relay-netwerk-in-kaart) op basis van 41 miljoen events over 1.085 relays, terwijl [npub.world](https://npub.world) in dezelfde week waarschuwingsbanners op profielen toevoegt. Martti Malmi lanceert [nostr-vpn](#nostr-vpn-lanceert-als-een-tailscale-alternatief), een Tailscale-alternatief dat signaleert over Nostr-relays en WireGuard-tunnels opzet, en in zeven dagen 11 releases uitbrengt. Het [Vector](https://github.com/VectorPrivacy/Vector)-team [maakt P2P DOOM open source](#open-source-doom-draait-peer-to-peer-over-nostr) op Nostr, [FIPS](https://github.com/jmcorgan/fips) brengt [v0.2.0](#fips-v020-levert-tor-transport-reproduceerbare-builds-en-sidecar-voorbeelden) uit, en [Nostrability Schemata](https://github.com/nostrability/schemata) breidt in één week uit naar [zes talen](#nostrability-schemata-wordt-meertalig).

## Nieuws

### Primal voegt Follow Packs, zap-verrijking en deep links toe

[Aansluitend op de berichtgeving over 3.0.7 van vorige week](/nl/newsletters/2026-03-18-newsletter/), besteedde [Primal Android](https://github.com/PrimalHQ/primal-android-app) deze week aan werk na de release rond onboarding, composer-UX en walletcontext. De herontworpen onboarding voegt Follow Packs toe ([PR #949](https://github.com/PrimalHQ/primal-android-app/pull/949)), een native GIF-knop verschijnt in de note-composer, een zap-verrijkingsservice ([PR #979](https://github.com/PrimalHQ/primal-android-app/pull/979)) annoteert wallettransacties met zapcontext, en een `primalconnect://` deep-linkingprotocol ([PR #969](https://github.com/PrimalHQ/primal-android-app/pull/969)) maakt navigatie tussen apps mogelijk.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) levert hetzelfde werk parallel via TestFlight, met de walletwissel ([PR #191](https://github.com/PrimalHQ/primal-ios-app/pull/191)), pollimplementatie en onboarding-refactor in hetzelfde tijdsvenster.

### BigBrotr brengt blootgestelde privé-sleutels over het relay-netwerk in kaart

[BigBrotr](https://github.com/BigBrotr/bigbrotr), het Nostr relay-analyseplatform, publiceerde een [gedetailleerde analyse van blootgestelde privésleutels](https://bigbrotr.com/blog/exposed-nsec-analysis/) op het relay-netwerk. De studie scande 41 miljoen events van 1.085 relays, zocht naar geldige nsec-strings in eventcontent, en vond 16.599 geldige privésleutels. Dat getal ziet er alarmerend uit tot je een bot met de naam "Mr.nsec" eruit filtert, die verantwoordelijk blijkt voor 92% van de matches. Na het verwijderen van botverkeer bleven slechts 38 echte accounts met samen meer dan 21.000 volgers over, en geen daarvan leek te weten dat de sleutel publiek was.

Het team bouwde een nsec-lekchecker als [NIP-90](/nl/topics/nip-90/) (Data Vending Machine)-dienst, zodat gebruikers kunnen controleren of hun privésleutel ergens in de gescande dataset voorkomt zonder die sleutel aan de checker prijs te geven. [npub.world](https://npub.world) integreerde de lekdata in dezelfde week en toont waarschuwingen op profielpagina's waar blootgestelde sleutels zijn aangetroffen. De combinatie geeft het netwerk zowel een programmeerbare interface voor DVM's en agents als een leesbare waarschuwing voor gewone gebruikers. De onderliggende dataset voedt ook [BigBrotr v6.4.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.4.0), dat replaceable en addressable event-materialized views toevoegt en een fix voor synchronizer idle timeout bevat.

### Nostr VPN lanceert als een Tailscale-alternatief

Martti Malmi (mmalmi), maker van Iris, bouwde en bracht [nostr-vpn](https://github.com/mmalmi/nostr-vpn) uit, een peer-to-peer VPN die Nostr-relays gebruikt voor signalering en WireGuard (via boringtun) voor versleutelde tunnels. De motivatie was direct: "Got annoyed by Tailscale requiring 3rd party accounts, so created Nostr VPN." De tool maakt mesh-netwerken tussen apparaten met Nostr-sleutelparen als identiteit, zonder centrale coördinatieserver.

Het project bracht in zeven dagen 11 releases uit, van [v0.2.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.2) tot [v0.2.13](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.13). Die sprint voegde Windows-ondersteuning, LAN-pairing voor lokale netwerkontdekking en een Android-sidecar voor mobiele apparaten toe. De architectuur is eenvoudig: twee apparaten wisselen verbindingsmetadata uit over Nostr-relays en zetten daarna een directe WireGuard-tunnel op. Nostr verzorgt discovery en NAT-traversal-signalen. WireGuard verwerkt het daadwerkelijke verkeer. De identiteit is een Nostr-sleutelpaar.

Malmi bleef in dezelfde week ook [nostr-double-ratchet](https://github.com/mmalmi/nostr-double-ratchet) doorontwikkelen, een Signal-achtige beveiligde berichtenbibliotheek, met zes releases van [v0.0.86](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.86) tot [v0.0.93](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.93).

### Open-source DOOM draait peer-to-peer over Nostr

Het [Vector](https://github.com/VectorPrivacy/Vector)-team maakte een peer-to-peer multiplayer-implementatie van DOOM open source die Nostr gebruikt voor peer discovery, [Marmot](/nl/topics/marmot/) voor end-to-end versleuteling en [Iroh](https://github.com/n0-computer/iroh), de QUIC-netwerkbibliotheek van n0, voor gossip-transport. Het spel wordt geleverd als een WebXDC-bestand van 4,2 MB dat in chatberichten kan worden verzonden, zonder servers om een match te hosten of te coördineren.

De technische aanpak vervangt de oorspronkelijke lockstep-netcode uit 1993 door een realtime hybride synchronisatiemodel. Spelers ontdekken elkaar via Nostr relay-queries, onderhandelen sessies via Marmot-versleutelde kanalen en schakelen daarna over naar Iroh's QUIC-gossiplaag voor laaglatency spelverkeer. De stack gebruikt Nostr voor discovery, Marmot voor versleuteling en Iroh voor transport.

Vector leverde deze week ook extra beveiligingsverharding. De release voegt een geheugen-verhard sleutelkluisje toe met anti-debug-bescherming en zeroize voor gevoelig sleutelmateriaal, gebruikersblokkering met volledige DM- en groepsberichtfiltering, en realtime kanaalfixes voor WebXDC Mini Apps.

### FIPS v0.2.0 levert Tor-transport, reproduceerbare builds en sidecar-voorbeelden

[FIPS](https://github.com/jmcorgan/fips), het Free Internetworking Peering System en een Nostr-aangrenzend mesh-netwerkproject, bracht [v0.2.0](https://github.com/jmcorgan/fips/releases/tag/v0.2.0-rel) uit. De release voegt Tor-transport toe voor geanonimiseerde mesh-links, reproduceerbare builds, een sidecar-voorbeeld dat via een Nostr-relay verbindt, en publicatie van releases op Nostr in de OpenWrt-packageworkflow. De release repareert ook jitterpieken na rekeying veroorzaakt door drain-window-frames. Het wire-format veranderde sinds v0.1.0, waardoor bestaande v0.1.0-nodes niet met v0.2.0 kunnen samenwerken zonder upgrade.

### Nostrability Schemata wordt meertalig

Het [Nostrability Schemata](https://github.com/nostrability/schemata)-project, dat JSON Schema-definities onderhoudt voor het valideren van Nostr event kinds, breidde in één week uit van alleen JavaScript naar zes talen. Nieuwe pakketten verschenen voor Rust, Go, Dart, Swift en Python, elk met zowel een datapakket als een validator. [v0.2.6](https://github.com/nostrability/schemata/releases/tag/v0.2.6) voegde ook 17 nieuwe event-kind-schema's toe.

De [Nostrability interop tracker](https://nostrability.github.io/nostrability/) kreeg tegelijk een grote update. Een nieuwe What's New-tab publiceert updates via zowel een Atom-feed als een Nostr-event, app-categoriefiltering laat bezoekers inzoomen op specifieke clienttypes, en de tracker detecteert programmeertalen nu automatisch uit GitHub-repositorymetadata. Nostrability heeft nu ook een eigen npub, waardoor het project zelf via het protocol dat het documenteert vindbaar wordt. Voor bibliotheekauteurs die over talen heen werken, betekenen de meertalige schema-pakketten dat dezelfde event-kind-definities beschikbaar zijn als native imports in plaats van dat elk project een eigen schemacopie moet onderhouden.

## Releases

### Amethyst v1.06.0 en v1.06.1

[Amethyst](https://github.com/vitorpamplona/amethyst), de Android-client onderhouden door vitorpamplona, bracht [v1.06.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.0) en [v1.06.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.1) uit op 23 maart. De hoofdfunctie is poll-ondersteuning die [NIP-85](/nl/topics/nip-85/) (Trusted Assertions)-data gebruikt voor gewogen stemmen, met herontworpen poll- en zap-pollkaarten. Die nieuwe rendering geeft zowel gewone polls als zap-gewogen polls een schonere visuele lay-out. v1.06.1 volgt met crashfixes voor concurrent modification die stabiliteitsregressies in het poll-renderpad aanpakken.

### Amber v5.0.0 en v5.0.1

[Amber](https://github.com/greenart7c3/Amber), de [NIP-55](/nl/topics/nip-55/) (Android Signer Application) signer-app, promoveerde recent 4.1.x pre-releasewerk naar stable met [v5.0.0](https://github.com/greenart7c3/Amber/releases/tag/v5.0.0) op 18 maart. Die stable release bevat de [NIP-42](/nl/topics/nip-42/) relay-auth, ingebouwde Tor, content-type-specifieke rechten en versleutelde PIN-opslag die vorige week aan bod kwamen. [v5.0.1](https://github.com/greenart7c3/Amber/releases/tag/v5.0.1) verwijdert vervolgens internetrechten uit de offline-buildvariant, zodat die build op Android-permissieniveau geen netwerkverzoeken meer kan doen.

### Mostro v0.17.0 en Mostro Mobile v1.2.2

[Mostro](https://github.com/MostroP2P/mostro), de peer-to-peer Bitcoin-beurs gebouwd op Nostr, bracht [v0.17.0](https://github.com/MostroP2P/mostro/releases/tag/v0.17.0) uit op 18 maart. De serverrelease zet het geschillen- en waarderingswerk uit de v0.16.x-cyclus voort en voegt completere reputatiedata voor kopers en verkopers toe als Nostr-events. [Mostro Mobile](https://github.com/MostroP2P/mobile), de Flutter-client, volgde op 23 maart met [v1.2.2](https://github.com/MostroP2P/mobile/releases/tag/v1.2.2), zodat de mobiele interface synchroon blijft met de nieuwste protocolwijzigingen.

### Shosho v0.14.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), de Nostr-livestreamingapp, bracht [v0.14.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.14.0) uit op 19 maart met de lancering van Shosho Shop. De release voegt een Shop-tab op profielen toe, Shop in Browse, en een In-Live Shop-knop op lives en clips. De release notes zeggen dat bestaande "Nostr products" automatisch verschijnen en dat kopers doorklikken naar de Plebeian Market-pagina van de verkoper. De release notes noemen het listing-kind niet, waardoor nog niet bevestigd kan worden of Shosho Shop dezelfde [NIP-99](/nl/topics/nip-99/) advertenties leest die [Shopstr](https://github.com/shopstr-eng/shopstr) expliciet in zijn README ondersteunt.

### Applesauce v5.2.0

[Applesauce](https://github.com/hzrd149/applesauce), hzrd149's verzameling helperpakketten voor het bouwen van Nostr-applicaties, bracht [v5.2.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core@5.2.0) uit op 22 maart. De release bestrijkt zes pakketten. Het SQLite-pakket repareert een UNIQUE-constraintbotsing op eventtags die dubbele inserts veroorzaakte. Het signers-pakket voegt `AndroidNativeSigner` toe, dat de native Android signer-interface van [NIP-55](/nl/topics/nip-55/) wrapt zodat apps gebaseerd op web views hardware-backed signing kunnen gebruiken zonder aangepaste bridgecode. Het relay-pakket voegt een `challenge`-veld toe aan relay- en poolstatusobjecten om [NIP-42](/nl/topics/nip-42/) auth-status bij te houden, zodat apps kunnen detecteren wanneer een relay authenticatie vraagt en programmatisch kunnen reageren. Het core-pakket krijgt `isEventPointerSame` en `isAddressPointerSame` om eventverwijzingen te dedupliceren, en het common-pakket voegt `user.blossomServers$` toe voor het resolven van de Blossom-mediaservers van een gebruiker. Applesauce voedt noStrudel, Satellite en verschillende andere webclients, dus deze fixes verspreiden zich door de webclientlaag.

### Wisp brengt 16 releases uit in één week

[Wisp](https://github.com/barrydeen/wisp), de Android Nostr-client, bracht deze week 16 releases uit, van [v0.9.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.9.3-beta) tot [v0.13.1-beta](https://github.com/barrydeen/wisp/releases/tag/v0.13.1-beta). De functietoevoegingen omvatten ondersteuning voor meerdere accounts, een zen-notificatiemodus voor minder onderbrekingen, concepten en geplande posts, veiligheidsfilters voor content en een nieuw vlamicoon.

### Manent v1.2.0

[Manent](https://github.com/dtonon/manent), de privé-app voor versleutelde notities en bestandsopslag, bracht [v1.2.0](https://github.com/dtonon/manent/releases/tag/v1.2.0) uit op 20 maart. De release voegt cameracaptatie direct vanuit de app toe, afbeeldingresizing voor upload om opslagkosten te verlagen, en pinch-to-zoom voor het bekijken van opgeslagen afbeeldingen. Manent slaat notities en bestanden versleuteld op op Nostr-relays met het sleutelpaar van de gebruiker, waardoor de telefoon- of desktopapp een thin client wordt die zijn volledige status uit relaydata kan reconstrueren.

### diVine 1.0.7

[diVine](https://github.com/divinevideo/divine-mobile), de short-form videocliënt, bracht [1.0.7](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.7) uit op 21 maart met een video-playback-watchdog die vastgelopen video's automatisch hervat. Na de E2E-testinfrastructuur en direct MP4-laden in [v1.0.6](/en/newsletters/2026-03-11-newsletter/#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import) richt deze release zich op het resterende playback-foutpad: video's die halverwege stoppen zonder een fout te geven.

### Alby Extension v3.14.2

[Alby Extension](https://github.com/getAlby/lightning-browser-extension), de [NIP-07](/nl/topics/nip-07/) (Browser Extension Signer) browserextensie, bracht [v3.14.2](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.2) uit op 18 maart met QR-codeweergave voor Lightning-adressen en ondersteuning voor Schnorr-signing. Die toevoeging brengt de browserextensie in lijn met het secp256k1-handtekeningschema dat Nostr native gebruikt.

### NoorNote v0.6.5 tot v0.6.11

[NoorNote](https://github.com/77elements/noornote), de notitieapp, bracht zeven releases uit van [v0.6.5](https://github.com/77elements/noornote/releases/tag/v0.6.5) tot [v0.6.11](https://github.com/77elements/noornote/releases/tag/v0.6.11). De hoofdfunctie is Follow Packs: gecureerde bundels accounts die gebruikers in bulk kunnen bekijken en volgen, vergelijkbaar met Twitter Lists maar gericht op onboarding. Gebruikers kunnen Follow Packs maken, bewerken en delen met aangepaste titels, beschrijvingen en omslagafbeeldingen. De serie upgrade ook de onderliggende Nostr-bibliotheek van NDK v2 naar v3, wat betere relayverbindingsafhandeling en abonnementsbeheer brengt. Picture notes en een herontworpen relay-verbindingservaring ronden deze run af.

### nak v0.19.1 en v0.19.2

[nak](https://github.com/fiatjaf/nak), fiatjaf's command-line Nostr-toolkit voor interactie met relays, het coderen en decoderen van [NIP-19](/nl/topics/nip-19/) (Bech32-Encoded Entities)-identifiers, het signeren van events en het opvragen van relaydata, bracht [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1) en [v0.19.2](https://github.com/fiatjaf/nak/releases/tag/v0.19.2) uit op 17 en 20 maart. De twee point releases volgen op de groepsforum-UI-toevoeging in [v0.19.0](/nl/newsletters/2026-03-18-newsletter/) van vorige week.

### Calendar by Form* v0.2.1

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), de gedecentraliseerde kalenderapp gebouwd op [NIP-52](/nl/topics/nip-52/) (Calendar Events), bracht [v0.2.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.1) uit op 20 maart. De release repareert een probleem met notificatiesjablonen dat herinneringen voor events beïnvloedde. Calendar slaat events op als Nostr kind 31922 (datumgebaseerd) en kind 31923 (tijdgebaseerd), zodat elke Nostr-client kalenderdata kan renderen als die ervoor kiest deze kinds te ondersteunen. De app is gebouwd door het Formstr-team, dat ook Formstr (gedecentraliseerde formulieren) en Pollerama (polls) onderhoudt.

### NYM v3.50 tot v3.53

[NYM](https://github.com/Spl0itable/NYM), de lichtgewicht efemere chatclient gekoppeld aan Bitchat, bracht 28 releases uit van v3.50 tot v3.53. De opvallendste functie is Nymbot, een ingebouwde chatbot die reageert op `@nymbot`-vermeldingen in kanalen en relaystatus- en beheerfuncties levert. Een "hardcore mode" genereert voor elk verzonden bericht een nieuw sleutelpaar, waardoor gespreksthreads op identiteitsniveau niet aan elkaar te koppelen zijn. De afruil is duidelijk: je verliest persistente identiteit maar wint anonimiteit per bericht. Ook de relay-proxylaag kreeg werk, met geshardde relay-proxyworkers voor betere connectiviteit, geohash-kanaalondersteuning en tolerantie voor clock skew bij nodes met onnauwkeurige systeemklokken.

## Projectupdates

### Ditto voegt Bluesky-bridge en Wikipedia-integratie toe

[Ditto](https://github.com/soapbox-pub/ditto), de aanpasbare Nostr social client van het Soapbox-team, noteerde deze week meer dan 300 commits over drie verschillende featuretrajecten. Het eerste is een Bluesky-bridge (19 commits) die Bluesky-posts inline rendert als volledige feedachtige threads, zijbalknavigatie toevoegt naar een Bluesky-discoverypagina gebaseerd op de officiële Discover-feed (whats-hot), en actieknoppen koppelt voor commentaar, delen, reageren en links kopiëren. Wanneer een gebruiker vanuit Ditto reageert op een Bluesky-post, toont de compose-modal een disclaimer die de cross-protocol aard van de interactie benoemt. [NIP-73](/nl/topics/nip-73/) (External Content IDs) kind 17-reacties voeden dit model: een Nostr-gebruiker reageert op een Bluesky-post en de reactie wordt opgeslagen als een standaard Nostr-event dat naar de externe contentidentifier verwijst. Hetzelfde patroon kan reacties koppelen aan elke externe contentsoort, van Bluesky-posts tot YouTube-video's en webpagina's.

Het tweede traject is Wikipedia-integratie (9 commits). Ditto rendert nu rijke Wikipedia-artikelinhoud op detailpagina's in plaats van generieke linkpreviews, voegt zoek-autocomplete toe met artikelminiaturen, en biedt een `/wikipedia`-pagina die featured content van de Wikipedia API ophaalt. Wikipedia- en Archive.org-resultaten verschijnen ook in de algemene zoek-autocomplete. Het derde traject is iOS-platformondersteuning via Capacitor, met een remote buildscript en platformconfiguratie naast een UI-herziening (55 commits) die backdrop-blur headers vervangt door een nieuw arc-gebaseerd navigatieontwerp op elke pagina van de app. Die 314 commits verplaatsen Ditto van een Nostr-only client naar een multi-protocol aggregator die Bluesky en Wikipedia behandelt als eersteklas contentbronnen naast de Nostr-feed.

### Pika bouwt een NIP-34 forge-CI-pipeline

[Pika](https://github.com/sledtools/pika), de Marmot-gebaseerde versleutelde berichtenapp, mergede deze week 33 PR's rond een self-hosted [NIP-34](/nl/topics/nip-34/) forge met pre-merge CI. Die forge is een git-hostinglaag die patches ontvangt als NIP-34-events, CI-checks draait voor merge, en gestructureerde status terugrapporteert via Nostr-events. [PR #701](https://github.com/sledtools/pika/pull/701) voegt lane-gebaseerde pre-merge en nightly CI toe, waarbij elk codepad (Rust, TypeScript, Apple-builds) in een eigen lane draait met onafhankelijke pass/fail-status. [PR #715](https://github.com/sledtools/pika/pull/715) verplaatst beheerde CI-agents naar Incus OpenClaw-containers voor isolatie, en [PR #733](https://github.com/sledtools/pika/pull/733) voegt een `ph forge` CLI toe om vanaf de command line met de gehoste forge te werken. Ondersteunende PR's regelen repository-schrijfrechten voor merges ([PR #736](https://github.com/sledtools/pika/pull/736)), gestructureerde CI-metadata met live statusbadges ([PR #722](https://github.com/sledtools/pika/pull/722)), Apple nightly build-splits ([PR #738](https://github.com/sledtools/pika/pull/738)) en fixes voor forge-auth en branch lookup ([PR #734](https://github.com/sledtools/pika/pull/734)). Dit is een van de eerste werkende CI/CD-systemen gebouwd bovenop NIP-34 git-events, en brengt Nostr-gebaseerde broncodehosting voorbij eenvoudige patchuitwisseling richting de merge-en-testworkflow die ontwikkelaars van GitHub of GitLab verwachten.

### Nostria voegt communities, code snippets en voice-eventafhandeling toe

[Nostria](https://github.com/nostria-app/nostria), de cross-platform Nostr-client onderhouden door sondreb, breidde deze week het appoppervlak verder uit voorbij de Web of Trust-filtering uit #14. De belangrijkste toevoeging is een volledige [NIP-72](/nl/topics/nip-72/) (Moderated Communities)-implementatie met community-creatie, moderator- en relayconfiguratie, het volgen van postgoedkeuringen met image previews en een aparte communitypagina met Posts- en Moderators-tabs.

In dezelfde periode voegde het project ook rendering en bewerking van code snippets toe met een editor met syntax highlighting, ondersteuning voor voice-event-replies voor audiogesprekken, chat-relayinstellingen voor directe berichten, kanaaldeling via de Web Share API, een toolbar-dockingsysteem voor de mediaspeler, in-app signup voor de nieuwste Brainstorm Web of Trust-service, geld verzenden en ontvangen in DM's via NWC en BOLT-11 facturen, Nostr-native GIF-afhandeling en een sterker RSS-importpad voor muzikanten dat bestaande Lightning-splits uit podcastfeeds kan overnemen.

### nostr-vpn snelle iteratie

Naast de [eerste lancering](#nostr-vpn-lanceert-als-een-tailscale-alternatief) laat de [nostr-vpn](https://github.com/mmalmi/nostr-vpn)-commitlog zien welke concrete problemen tijdens echte deployment opdoken. [v0.2.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.3) tot en met [v0.2.5](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.5) voegden het eerste installerscript en een cross-platform CLI toe. [v0.2.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.6) en [v0.2.7](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.7) brachten Windows-ondersteuning, waarvoor UAC-padquoting voor configuratieschrijfsels en daemon-owned config-updates nodig waren. [v0.2.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.8) tot en met [v0.2.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.10) repareerden Windows GUI-serviceacties, CLI-subprocessafhandeling en machine-scoped serviceconfiguratie. [v0.2.12](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.12) verving LAN-discovery door timed LAN pairing, een gebruikersgestuurde flow waarbij twee apparaten op hetzelfde lokale netwerk kunnen pairen zonder relay-signalen. Het patroon is schoolboekachtige field testing in een vroege fase: elke release pakt een specifiek deploymentprobleem aan, de gebruikersbasis is klein genoeg voor dagelijkse iteratie, en de ontwikkelaar gebruikt het gereedschap zelf tussen releases door.

### Comet geautomatiseerde builds

[Comet](https://github.com/nodetec/comet) (voorheen Captain's Log), de Nostr-native long-form schrijftool van Nodetec, produceerde deze week meer dan 40 geautomatiseerde alpha-builds. Comet is een desktopapp voor het schrijven en publiceren van NIP-23 (Long-form Content)-artikelen, met lokale conceptopslag, markdownbewerking en one-click publicatie naar de relayset van de gebruiker. De geautomatiseerde buildpipeline maakt voor elke commit op de main-branch een tagged release aan, wat het ruwe aantal releases een misleidende maat voor feature-snelheid maakt. Wat die 40 builds wel laten zien, is dat de app dagelijks actief wordt ontwikkeld, en dat elke commit binnen minuten wordt getest, verpakt en beschikbaar gemaakt voor download.

## NIP-Updates

Recente wijzigingen in het [NIPs-repository](https://github.com/nostr-protocol/nips) tijdens het venster van 17-24 maart:

Er werden tussen 18 en 24 maart geen NIP-merges gedaan.

**Open PR's en discussies bijgewerkt in dit venster:**

- **NIP-AA: Autonomous Agents on Nostr** ([PR #2259](https://github.com/nostr-protocol/nips/pull/2259)): Stelt conventies voor autonome agents voor die op het Nostr-netwerk opereren. De PR definieert hoe agents zichzelf identificeren, diensten ontdekken en met andere agents en mensen coördineren via Nostr-events.

- **[NIP-50](/nl/topics/nip-50/) (Search): Sort extensions** ([PR #2283](https://github.com/nostr-protocol/nips/pull/2283)): Voegt sorteerparameters toe aan NIP-50-zoekqueries, waaronder top, hot, zaps en new. Dat zou clients in staat stellen gerangschikte resultaten op te vragen bij relays die full-text search ondersteunen in plaats van client-side te sorteren.

- **NIP-A5: WASM Programs** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Stelt een conventie voor voor het publiceren en ontdekken van WebAssembly-programma's op Nostr. WASM-binaries zouden als Nostr-events kunnen worden verspreid, met relays als discoverylaag voor draagbare uitvoerbare code.

- **NIP-CF: Combine Forces interoperable napps** ([PR #2277](https://github.com/nostr-protocol/nips/pull/2277)): Definieert een conventie voor interoperabele Nostr-applicaties ("napps") die functionaliteit over verschillende clients en diensten heen kunnen samenstellen.

- **Snapshots NIP** ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279)): Stelt een mechanisme voor voor relay-state snapshots, bedoeld voor relaysynchronisatie en back-up.

- **Checkpoints NIP** ([PR #2278](https://github.com/nostr-protocol/nips/pull/2278)): Stelt checkpoint-events voor om bekende goede relaystatus te markeren, als aanvulling op het snapshots-voorstel.

- **[NIP-58](/nl/topics/nip-58/) (Badges): Badge Sets refactor** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Herstructureert hoe badgeverzamelingen worden georganiseerd en gerefereerd.

- **[NIP-11](/nl/topics/nip-11/) (Relay Information Document): Extensions** ([PR #2280](https://github.com/nostr-protocol/nips/pull/2280)): Voegt extra velden toe aan het relay-informatiedocument voor rijkere machineleesbare relaymetadata.

## Vijf Jaar Nostr-Maart

[De nieuwsbrief van vorige maand](/nl/newsletters/2026-03-04-newsletter/#five-years-of-nostr-februaries) beschreef hoe Nostr's februaris zich ontwikkelden van de NIP-01 (Basic Protocol Flow)-herschrijving via de Damus App Store-golf naar mesh-netwerken en agentvoorstellen. Dit retrospectief volgt wat er elke maart gebeurde van 2021 tot en met 2026.

### Maart 2021: Twee commits

Vier maanden na het ontstaan produceerde Nostr's maart precies twee commits in het protocolrepository, beide op 4 maart. fiatjaf [voegde links naar nostwitter-instances toe](https://github.com/nostr-protocol/nostr/commit/dcd8cc3), zodat vroege bezoekers werkende deployments konden vinden, en [voegde kind toe aan de basisfilterdefinitie](https://github.com/nostr-protocol/nostr/commit/54dfb46). Die tweede commit is onthullend: in maart 2021 kon je Nostr-events nog niet op kind filteren. Het protocol was zó primitief. Twee of drie relays bedienden het netwerk. De Telegram-groep was het enige coördinatiekanaal. Het NIPs-repository bestond nog niet; protocolvoorstellen leefden als bestanden in het hoofd-repository van nostr. fiatjaf was die maand de enige committer. De volledige output van maart 2021 van wat vijf jaar later een protocol zou zijn dat VPN's, multiplayergames en mesh-netwerken ondersteunt, past in één enkele git diff.

### Maart 2022: Bouwen vóór Damus

Het hoofdrepository van het protocol ontving in maart 2022 nul commits. Ontwikkeling was volledig verschoven naar toolrepositories. [Branle](https://github.com/fiatjaf/branle), fiatjaf's Vue.js-webclient en destijds de primaire Nostr-interface, kreeg 5 commits, waaronder Docker-deploymentondersteuning en [NIP-05](/nl/topics/nip-05/) (DNS-Based Verification)-displaynamefixes die het `_@`-prefix verwijderden uit verificatiebadges. Robert C. Martins [more-speech](https://github.com/unclebob/more-speech), de Clojure-desktopclient, noteerde 13 of meer commits die threading, toetsenbordnavigatie en een editvenster toevoegden. De beroemdste softwareauteur die die maand actief op Nostr bouwde was geen crypto-ontwikkelaar, maar de persoon wiens "Clean Code" miljoenen exemplaren verkocht, die een Nostr-client in Clojure schreef, een taalkeuze die veel zegt over de vroege gemeenschap: dit waren eigenzinnige programmeurs die voor zichzelf bouwden.

Het relay-netwerk was gegroeid tot ongeveer 15 relays met een actieve gebruikersbasis in de honderden. Damus bestond nog niet en zou pas in april 2022 worden gemaakt. Nostream was er ook nog niet. Het werk van die maand was infrastructuur: bestaande tools betrouwbaarder maken voor de kleine gemeenschap die ze al dagelijks gebruikte.

### Maart 2023: Infrastructuur na de explosie

Een maand na de Damus App Store-golf en de sprong voorbij 300.000 publieke sleutels draaide maart 2023 om het absorberen van die groei. Het [NIPs-repository](https://github.com/nostr-protocol/nips) mergede 28 pull requests, het op één na hoogste maandtotaal in de protocolgeschiedenis. [NIP-51](/nl/topics/nip-51/) (Lists) werd gemerged en gaf clients gestructureerde volg-, mute- en bookmarkcollecties. [NIP-39](/nl/topics/nip-39/) (External Identities in Profiles) landde, NIP-78 (Application-Specific Data) leverde een algemeen opslagkind voor apps die privéstatus nodig hadden, en een herschrijving van [NIP-57](/nl/topics/nip-57/) (Lightning Zaps) ([PR #392](https://github.com/nostr-protocol/nips/pull/392)) consolideerde de zapflow en verduidelijkte de terminologie. De meest besproken PR van de maand was een alternatief voorstel voor mention-afhandeling ([PR #381](https://github.com/nostr-protocol/nips/pull/381)) met meer dan 50 opmerkingen.

Het meest consequentiale nieuwe project was [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit), de TypeScript-bibliotheek voor relayverbindingen, event-signing, caching en subscription management. pablof7z deed de [eerste commit](https://github.com/nostr-dev-kit/ndk/commit/09e5e03) op 16 maart 2023, herschreef het 11 dagen later volledig op 27 maart ("basically another initial commit"), en had tegen 31 maart LNURL- en zap-ondersteuning werkend. NDK ging van niets naar zap-capable in 15 dagen. Vijf dagen na het ontstaan van NDK, op 21 maart, maakte het Alby-team [NWC](https://github.com/getAlby/nostr-wallet-connect) (Nostr Wallet Connect), de referentie-implementatie van [NIP-47](/nl/topics/nip-47/) die Lightning-wallets aan Nostr-applicaties koppelde. De twee projecten die de volgende drie jaar webgebaseerde Nostr-ontwikkeling zouden dragen, werden geboren in hetzelfde venster van 30 dagen. OpenSats had zijn Nostr-fonds toen nog niet gelanceerd; de eerste golf kwam pas in [juli 2023](https://opensats.org/blog/nostr-grants-july-2023), vier maanden na de creatie van NDK.

Andere opvallende creaties die maand waren NostrGit, NostrChat, een nostr-signing-deviceproject van LNbits en nostrmo. [Gossip](https://github.com/mikedilger/gossip), de Rust-desktopclient gericht op intelligente relayselectie, bracht drie releases uit. Het protocol stond in build-modus, en de tools die in maart 2023 zijn gemaakt, zijn drie jaar later nog steeds in gebruik.

### Maart 2024: Protocolvolwassenheid

Maart 2024 draaide om het verharden van het protocol voor langdurig gebruik. Het NIPs-repository mergede 12 pull requests. De belangrijkste was [NIP-34](/nl/topics/nip-34/) (Git Stuff), [PR #997](https://github.com/nostr-protocol/nips/pull/997), die op 5 maart werd gemerged na meer dan 130 opmerkingen en 44 dagen review. De discussiethread is een tijdcapsule van een gemeenschap die debatteert over hoe een gedecentraliseerde GitHub eruit zou moeten zien. jb55 trok parallellen met `git send-email`, Giszmo stelde voor om root commit hashes te gebruiken voor cross-fork discovery ("something GitHub doesn't do and we could"), mikedilger stelde [NIP-98](/nl/topics/nip-98/) (HTTP Auth) event-ondertekende authenticatie voor in plaats van SSH-sleutels, en fiatjaf wees de noodzaak van versiebeheeralgemeenheid botweg af: "not for each version control system, just for git. No one uses the others." Binnen enkele uren na het openen van de PR had fiatjaf nak, go-nostr en gitstr al omgeschakeld om patches over Nostr te accepteren. DanConwayDev, wiens ngit al een OpenSats-subsidie had, behoorde tot de actiefste bijdragers aan de discussie. Een botveld voor profielmetadata werd ook gemerged, waardoor clients machineleesbaar onderscheid kunnen maken tussen geautomatiseerde accounts en mensen.

[Amethyst](https://github.com/vitorpamplona/amethyst) bracht v0.85.0 uit met git-eventondersteuning, wiki-artikelen, rendering van medische data en contentbewerking in één release. [Mostro](https://github.com/MostroP2P/mostro) bereikte v0.10.0. [Nosflare](https://github.com/Spl0itable/nosflare), een serverless Nostr-relay op Cloudflare Workers, bewees dat relaylogica aan de edge kan draaien. OpenSats gaf een [Long-Term Support grant aan Bruno Garcia](https://opensats.org/blog/bruno-garcia-receives-lts-grant) voor duurzame bijdragen aan de Amethyst-client.

### Maart 2025: Uitbreiding van infrastructuur

Maart 2025 produceerde 10 gemergede NIPs. De koploper was [NIP-66](/nl/topics/nip-66/) (Relay Discovery and Liveness Monitoring), [PR #230](https://github.com/nostr-protocol/nips/pull/230), die op 3 maart werd gemerged na een traject van 25 maanden. dskvr stelde relaymonitoring voor het eerst voor in februari 2023 voor, kreeg te horen dat het client-side kon, legde uit waarom tegelijk verbinden met duizenden relays onpraktisch was voor individuele clients, ging door zeven volledige drafts, bouwde monitoringnodes in acht geografische regio's (Northeast US, Brazilië, US-West, US-East, Australië, India, Korea, Zuid-Afrika), en wachtte tot de relaytooling was bijgehaald. Tegen de tijd van de merge bestonden al implementaties in nostr.watch, relaypag.es, monitorlizard, Snort, noStrudel en Jumble. De NIP-66-data zou later de Nostrability outbox-benchmarks voeden [behandeld in Newsletter #12](/nl/newsletters/2026-03-04-newsletter/#outbox-model-under-the-microscope). NIP-C0 (Code Snippets) werd ook gemerged ([PR #1852](https://github.com/nostr-protocol/nips/pull/1852), 63 opmerkingen), en voegde kind 1337-events toe voor het delen van broncode.

De eerste MCP-servers voor Nostr verschenen deze maand. [nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server) verscheen op 23 maart en [nwc-mcp-server](https://github.com/getAlby/nwc-mcp-server) op 14 maart, slechts vier maanden nadat Anthropic in november 2024 het Model Context Protocol aankondigde. Deze vroege bridges gingen vooraf aan de volledige [ContextVM](/nl/topics/contextvm/) SDK en het agent-commercewerk dat eind 2025 en begin 2026 volgde.

[Gossip](https://github.com/mikedilger/gossip) bracht v0.14.0 uit. [Coracle](https://github.com/coracle-social/coracle), hodlbod's webclient met relay-aware feedbeheer, bracht drie releases uit. OpenSats kondigde zijn [tiende golf Nostr-subsidies](https://opensats.org/blog/10th-wave-of-nostr-grants) aan en zette daarmee de financieringspijplijn voort die sinds medio 2023 liep.

### Maart 2026: Convergentie

*Activiteit in maart 2026 is ontleend aan Nostr Compass-edities [#12](/nl/newsletters/2026-03-04-newsletter/) tot [#15](#) (deze editie).*

Maart 2026 is de maand waarin verschillende draden samenkomen in werkende systemen. De [Marmot Development Kit](/nl/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release) bracht zijn eerste publieke release uit met versleutelde media, meertalige bindings en een ChaCha20-Poly1305-migratie die gecoördineerde updates vroeg over spec, Rust en TypeScript heen. [Shopstr en Milk Market](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces) voegden MCP-commerceoppervlakken toe voor agent-gedreven aankopen. [NIP-42](/nl/topics/nip-42/) relay-auth landde gelijktijdig in [Amber](/en/newsletters/2026-03-11-newsletter/#nip-42-relay-auth-across-bunker-signer-and-relay), strfry en OAuth Bunker, waarmee de lus tussen signer-, relay- en bunkersoftware werd gesloten. [Notedeck](/nl/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr) bracht Nostr-native software-updates uit met [NIP-94](/nl/topics/nip-94/) (File Metadata) release-events.

Deze week scande [BigBrotr](#bigbrotr-brengt-blootgestelde-prive-sleutels-over-het-relay-netwerk-in-kaart) het volledige relay-netwerk op gelekte privésleutels en publiceerde zowel de analyse als een DVM-checker. [Nostr VPN](#nostr-vpn-lanceert-als-een-tailscale-alternatief) bewees dat het sleutelmodel van Nostr bruikbaar is voor netwerkinfrastructuur, niet alleen voor social media. [DOOM](#open-source-doom-draait-peer-to-peer-over-nostr) liet zien dat Nostr-discovery, Marmot-versleuteling en QUIC-transport samen een realtime multiplayergame kunnen dragen. [Amber](#amber-v500-en-v501) sprong naar v5.0.0. [Wisp](#wisp-brengt-16-releases-uit-in-een-week) leverde 16 releases in zeven dagen. Meer dan 25 getagde releases kwamen in één week van grote projecten.

In de eerste 24 dagen van de maand werden zeven NIPs gemerged. Het protocol kreeg [NIP-54](/nl/topics/nip-54/) (Wiki) Djot-opmaak, [NIP-19](/nl/topics/nip-19/) (Bech32-Encoded Entities) invoerlimieten, [NIP-91](/nl/topics/nip-91/) (AND Operator for Filters) boolean querylogica en [NIP-85](/nl/topics/nip-85/) (Trusted Assertions) Web of Trust-asserties. Open voorstellen liepen uiteen van autonome agents (NIP-AA) via WASM-programma's (NIP-A5) tot sorteervarianten voor zoeken in [NIP-50](/nl/topics/nip-50/).

### Vooruitblik

Vijf maartmaanden van Nostr tekenen een duidelijke boog. In 2021 deed één persoon twee commits aan een protocol dat events nog niet op kind kon filteren. In 2023 werden NDK en NWC met vijf dagen ertussen geboren om de explosie na Damus op te vangen. In 2024 debatteerde een PR-thread met 141 opmerkingen over hoe git-samenwerking op een sociaal protocol moest werken. In 2025 werd een relaymonitoringspecificatie die zeven keer over 25 maanden was herschreven eindelijk gemerged. In 2026 raakte iemand geïrriteerd door het feit dat Tailscale een account vereist en bouwde een VPN met Nostr-sleutelparen, terwijl iemand anders multiplayer DOOM uitbracht dat peers ontdekt via Nostr-relays en gameplay versleutelt via Marmot. BigBrotr's scan van 41 miljoen events over 1.085 relays geeft een concreet gevoel voor hoe ver het netwerk is gegroeid. Het protocoloppervlak van maart 2026 zou onherkenbaar zijn geweest voor maart 2021, maar het onderliggende model, events ondertekend met secp256k1-sleutels en verspreid via relays, is niet veranderd.

---

Dat is het voor deze week. Bouw je iets of heb je nieuws om te delen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via [NIP-17](/nl/topics/nip-17/) (Private Direct Messages) DM</a> of vind ons op Nostr.
