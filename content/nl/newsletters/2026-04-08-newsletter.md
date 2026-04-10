---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [Amethyst](https://github.com/vitorpamplona/amethyst) brengt [v1.08.0](#amethyst-brengt-arti-tor-en-merget-pure-kotlin-mls-en-marmot) uit met Arti Tor-integratie en een herontworpen Shorts-UI, terwijl pure Kotlin-implementaties van [MLS](/nl/topics/mls/) en [Marmot](/nl/topics/marmot/) in de [Quartz](/nl/topics/quartz/)-bibliotheek worden gemerged. [Nostur](https://github.com/nostur-com/nostur-ios-public) brengt [v1.27.0](#nostur-v1270-voegt-video-opname-en-prive-antwoorden-toe) uit met video-opname, geanimeerde GIF-profielen en private replies. [Shosho](https://github.com/r0d8lsh0p/shosho-releases) lanceert [v0.15.0](#shosho-v0150-lanceert-shows-en-verticale-video-carousel) met Shows (aangepaste live-streaminfo gekoppeld aan OBS) en een verticale videocarrousel in TikTok-stijl. [Nymchat](https://github.com/Spl0itable/NYM) [draait Marmot terug en brengt verbeterde NIP-17-groepschats uit](#nymchat-draait-marmot-terug-en-brengt-verbeterde-nip-17-groepschats-uit) met roterende ephemeral keys. [Nostr VPN](https://github.com/mmalmi/nostr-vpn) brengt [ondersteuning voor exit nodes en Umbrel-packaging](#nostr-vpn-brengt-ondersteuning-voor-exit-nodes-en-umbrel-packaging-uit) uit in zes releases. [Amber](https://github.com/greenart7c3/Amber) springt naar [v6.0.0-pre1](#amber-v600-pre1-voegt-nip-46-signing-keys-per-verbinding-toe) met [NIP-46](/nl/topics/nip-46/) signing keys per verbinding en in-app updates via Zapstore. [Notedeck](https://github.com/damus-io/notedeck) bereikt [v0.10.0-beta](#notedeck-v0100-beta-brengt-zapstore-self-update-uit) met APK self-update via Zapstore, en [NIP-58](/nl/topics/nip-58/) (Badges) krijgt een [kind-migratie](#nip-updates). Twee NIP-deep-dives behandelen [NIP-17](/nl/topics/nip-17/) (Private Direct Messages) en [NIP-46](/nl/topics/nip-46/) (Nostr Remote Signing).

## Nieuws

### Amethyst brengt Arti Tor en merget pure Kotlin MLS en Marmot

[Amethyst](https://github.com/vitorpamplona/amethyst), de Android-client onderhouden door vitorpamplona, bracht vier releases uit van [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3) tot en met [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0) en merge'de een grote reeks nog niet uitgebrachte wijzigingen in de [Quartz](/nl/topics/quartz/)-bibliotheek (de gedeelde Kotlin Multiplatform Nostr-module). De hoofdrelease is v1.08.0 "Arti Tor", die de Tor-connectiviteit van de app migreert van de op C gebaseerde Tor-bibliotheek naar [Arti](https://gitlab.torproject.org/tpo/core/arti), de Rust-implementatie van het Tor Project. Die migratie pakt willekeurige crashes aan die optraden onder de eerdere C Tor-bindings. Arti is de langetermijnvervanger van het Tor Project voor de C-codebase, vanaf nul geschreven in Rust voor memory safety en async I/O.

De v1.07.3-release herontwierp de Shorts-UI en verving het gepagineerde ontwerp door rand-tot-rand-feeds voor afbeeldingen, shorts en lange video's. Diezelfde release migreerde badges naar kind `10008` en bookmarks naar kind `10003`, in lijn met de [NIP-58](/nl/topics/nip-58/) kind-migratie die [deze week werd gemerged](#nip-updates). v1.07.4 repareerde een probleem met de secret-afhandeling van Nostr Wallet Connect, en v1.07.5 repareerde een crash bij image-upload.

Op main, maar nog niet in een getagde release, schreef het team een volledige Kotlin-implementatie van zowel [MLS](/nl/topics/mls/) als het [Marmot](/nl/topics/marmot/)-protocol, waardoor native C/Rust-library bindings niet langer nodig zijn. [PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147) voegt de kernlaag voor Marmot MLS-groepsberichten toe, [PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149) voegt de groepschat-UI toe, [PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146) voegt inkomende en uitgaande berichtprocessors met een subscription manager toe, [PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141) voegt persistente MLS-groepsstatus en KeyPackage-rotatiebeheer toe, [PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150) voegt een volledige MLS-testsuite met verbeterde GroupInfo-signing toe, en [PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158) voegt tracking van de publicatiestatus van KeyPackages toe. [PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166) voegt een pure Kotlin secp256k1-implementatie toe voor Nostr-cryptografische operaties, als vervanging van de native C-library dependency. In combinatie met de Kotlin MLS-implementatie kan [Quartz](/nl/topics/quartz/) Nostr-signing en Marmot-groepsberichten draaien zonder native bindings, wat de deur opent naar Kotlin Multiplatform-targets waaronder iOS.

Het team bouwt ook ondersteuning voor [NIP-AC](/en/topics/nip-ac/) (P2P Voice and Video Calls): [PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143) voegt een volledige testsuite toe voor de NIP-AC call state machine, en [PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164) voorkomt dat verouderde call offers opnieuw worden getriggerd nadat de app opnieuw is gestart.

### Nostur v1.27.0 voegt video-opname en private replies toe

[Nostur](https://github.com/nostur-com/nostur-ios-public), de iOS Nostr-client, bracht [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0) uit op 2 april. De release voegt video-opname in de app toe met trim-before-upload, zodat gebruikers korte clips kunnen opnemen, op lengte kunnen knippen en publiceren zonder de client te verlaten. Ondersteuning voor geanimeerde GIF's strekt zich nu uit tot profiel- en bannerfoto's, en er is ook geanimeerde WebP-rendering toegevoegd. Een nieuwe Shortcuts-integratie laat gebruikers Nostr-posts versturen vanuit Apple Shortcuts-automatiseringen. De release voegt ook private replies toe en repareert DM-compatibiliteitsproblemen die de berichtbezorging tussen Nostur en andere clients beïnvloedden.

### Shosho v0.15.0 lanceert Shows en verticale video-carousel

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), de Nostr-livestreamingapp, bracht [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0) en [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1) uit op 7 april. De hoofdfunctie is Shows: streamers kunnen aangepaste show-informatie instellen voordat ze live gaan en hun show koppelen aan OBS of een andere externe encoder. Daarmee wordt de metadata van "wat stream ik" losgekoppeld van het daadwerkelijk live gaan, zodat streamers titels, beschrijvingen en producten kunnen voorbereiden voordat de uitzending begint. Diezelfde release voegt een verticale videocarrousel in TikTok-stijl toe om door lives, clips en replays te swipen in een fullscreen-feed, plus Quick Add om videoclips te publiceren en producten direct vanaf een profielpagina toe te voegen. v0.15.1 repareert een bug waarbij het toetsenbord het chatinvoerveld van de livestream verborg.

## Releases

### Notedeck v0.10.0-beta brengt Zapstore self-update uit

[Notedeck](https://github.com/damus-io/notedeck), de desktop- en mobiele client van het Damus-team, bracht [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1) en [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2) uit als test-prereleases voor APK self-update. [PR #1417](https://github.com/damus-io/notedeck/pull/1417) voegt APK self-update toe via de Nostr/Zapstore-updater op Android, voortbouwend op het [Nostr-native update-discoverywerk uit Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr). De updateflow ontdekt nieuwe releases via Nostr-events die naar relays zijn gepubliceerd, downloadt vervolgens de APK van waar de ontwikkelaar die host (GitHub releases, Blossom CDN of andere bronnen), verifieert de SHA-256-hash tegen het ondertekende Nostr-event en installeert die daarna. [PR #1438](https://github.com/damus-io/notedeck/pull/1438) repareert een bug op het welkomstscherm waarbij Login- en CreateAccount-knoppen direct terug navigeerden, en [PR #1424](https://github.com/damus-io/notedeck/pull/1424) repareert tekstoverflow in de Agentium AI-sessieweergave.

### Amber v6.0.0-pre1 voegt NIP-46 signing keys per verbinding toe

[Amber](https://github.com/greenart7c3/Amber), de [NIP-55](/nl/topics/nip-55/) (Android Signer Application) signer-app, bracht [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1) uit op 4 april. De belangrijkste wijziging is signing keys per verbinding voor het [NIP-46](/nl/topics/nip-46/) (Nostr Remote Signing) bunker-protocol. In plaats van één keypair te gebruiken voor alle bunker-verbindingen genereert Amber nu een aparte sleutel voor elke verbonden client. Als één clientverbinding gecompromitteerd raakt, kan de aanvaller zich niet voordoen als de signer tegenover andere clients.

[PR #377](https://github.com/greenart7c3/Amber/pull/377) voegt in-app controle op updates en installatie via Zapstore toe, waarmee Amber zich naast [Notedeck](#notedeck-v0100-beta-brengt-zapstore-self-update-uit) schaart in Nostr-native appdistributie. [PR #375](https://github.com/greenart7c3/Amber/pull/375) handelt AndroidKeyStore-fouten netjes af door gebruikers een waarschuwing te tonen in plaats van te crashen, en [PR #371](https://github.com/greenart7c3/Amber/pull/371) voegt database-opruiming toe met groottelimieten en truncatie van content om onbegrensde opslaggroei te voorkomen. De pre-release bevat ook de [NIP-42](/nl/topics/nip-42/) relay-auth-whitelist en login via mnemonic recovery phrase uit de [v5.0.x-cyclus die vorige week werd behandeld](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504).

### Nostria brengt native mobiele app uit

[Nostria](https://github.com/nostria-app/nostria), de cross-platform Nostr-client onderhouden door SondreB, bracht een native mobiele app voor Android uit met acht releases van [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11) tot en met [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18). De belangrijkste nieuwe mogelijkheid is native ondersteuning voor local signers zoals [Amber](https://github.com/greenart7c3/Amber) en Aegis. [Desktop-installers](https://www.nostria.app/download) voor Linux, macOS en Windows zijn ook beschikbaar. [PR #610](https://github.com/nostria-app/nostria/pull/610) verlaagt de geheugendruk van de feed met adaptieve runtime-limieten en opschoning van preview-URL's. v3.1.14 repareert de integratie met Brainstorm, een [Web of Trust](/nl/topics/web-of-trust/)-provider. v3.1.15 richt zich op muziekverbeteringen. De nieuwe Android-app is beschikbaar op [Zapstore](https://zapstore.dev/apps/app.nostria).

### diVine 1.0.8 brengt hervatbare uploads en DM's uit

[diVine](https://github.com/divinevideo/divine-mobile), de short-form videocliënt, bracht [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8) uit met 87 gemergede PR's. Hervatbare uploads laten makers onderbroken uploads chunk voor chunk voortzetten in plaats van opnieuw vanaf nul te beginnen op een instabiele verbinding. De release voegt instellingen voor videokwaliteit en bitrate toe, double-tap om te liken en verbeteringen aan DM's. [PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722) voegt een macOS-camera-plugin toe voor desktop-video-opname, en [PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820) migreert het notificatiesysteem naar een BLoC-architectuur met enrichment en grouping. Het team verving ook AI-generated stickers en category art door OpenMoji SVG's ([PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844), [PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)).

### Manent v1.3.0 voegt vervaging van gevoelige notities en NIP-42-auth toe

[Manent](https://github.com/dtonon/manent), de private app voor versleutelde notities en bestandsopslag, bracht [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0) uit op 2 april. Gebruikers kunnen notities nu als gevoelig markeren om ze in de lijstweergave te vervagen, zodat private content verborgen blijft tijdens vluchtig scrollen. De release voegt ook ondersteuning voor [NIP-42](/nl/topics/nip-42/) (Authentication of Clients to Relays) toe, waardoor Manent zich kan authenticeren bij relays die dat vereisen voordat ze events accepteren. Manent slaat alle data versleuteld op Nostr-relays op met het keypair van de gebruiker, dus NIP-42-ondersteuning vergroot het aantal relays dat het voor opslag kan gebruiken.

### Wisp v0.17.0 tot en met v0.17.3 voegen livestream-zaps en walletbackup toe

[Wisp](https://github.com/barrydeen/wisp), de Android Nostr-client, bracht zes releases uit van [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta) tot en met [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta) met 44 gemergede PR's. De v0.17.0-release voegt veiligheidsmeldingen voor walletbackups en zap-UX-verbeteringen toe. [v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta) voegt zichtbaarheid van livestreamchat over platforms heen en functionaliteit voor livestream-zaps toe. [PR #423](https://github.com/barrydeen/wisp/pull/423) voegt automatisch zoeken naar profielen, een zap-success-animatie en verbeteringen aan de gebruikersstatus toe. [PR #426](https://github.com/barrydeen/wisp/pull/426) repareert een out-of-memory-crash in `computeId` voor events met grote taglijsten. De v0.16.x-releases voegden emoji-shortcode-autocomplete, verbeteringen aan de groepschat-UI en filtering van geblokkeerde gebruikers toe over alle notificatiepaden heen.

### Mostro brengt deep links, Nostr-wisselkoersen en een fix voor dubbele betalingen uit

[Mostro](https://github.com/MostroP2P/mostro), de peer-to-peer Bitcoin-beurs gebouwd op Nostr, zag deze week updates in zowel zijn serverdaemon als mobiele client. Aan serverzijde voorkomt [PR #692](https://github.com/MostroP2P/mostro/pull/692) dat verouderde orderwrites dubbele betalingen veroorzaken, een bug die ertoe kon leiden dat een verkoper twee keer voor dezelfde trade werd betaald. [PR #693](https://github.com/MostroP2P/mostro/pull/693) gebruikt gerichte updates voor dev_fee-writes in plaats van volledige order-overschrijvingen.

[Mostro Mobile](https://github.com/MostroP2P/mobile), de Flutter-client, bracht [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3) uit op 3 april. De release handelt deep links van verschillende Mostro-instanties af, zodat gebruikers op links kunnen tikken die naar de juiste exchange-server routeren. [PR #498](https://github.com/MostroP2P/mobile/pull/498) detecteert admin- en dispute-DM's in de achtergrondnotificatiepipeline, en de app haalt wisselkoersen nu op via Nostr met een HTTP/cache-fallback. [PR #560](https://github.com/MostroP2P/mobile/pull/560) repareert een relay-connection blocking bug waardoor de app onder bepaalde netwerkcondities relays niet kon bereiken.

### Unfiltered v1.0.12 voegt hashtags en comments toe

[Unfiltered](https://github.com/dmcarrington/unfiltered), een Nostr-client gericht op beeldrijke content, bracht [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12) uit. [PR #69](https://github.com/dmcarrington/unfiltered/pull/69) voegt hashtag-ondersteuning toe en [PR #72](https://github.com/dmcarrington/unfiltered/pull/72) voegt de mogelijkheid toe om comments op posts te schrijven en te tonen. [PR #71](https://github.com/dmcarrington/unfiltered/pull/71) repareert navigatieproblemen bij posts met meerdere afbeeldingen.

### Primal Android brengt walletdeling voor meerdere accounts en auto-reconnect voor remote signer uit

[Primal](https://github.com/PrimalHQ/primal-android-app), de Android Nostr-client, bracht op 7 april een release uit. De update voegt walletdeling voor meerdere accounts toe en een overflow-menu met walletverwijdering in Dev Tools. De remote signer reconnect nu automatisch bij verbroken verbindingen, en de walletservice kreeg zijn eigen auto-reconnectlogica. Fixes zorgen ervoor dat poll-zap-stemmen niet langer als Top Zaps verschijnen, lege pollopties geen crash meer veroorzaken, walletsaldo wordt verborgen wanneer er geen wallet bestaat, en WalletException-typen naar foutcodes in NWC-antwoorden worden gemapt.

### Titan v0.1.0 lanceert native nsite://-browser met Bitcoin-naamsregistratie

[Titan](https://github.com/btcjt/titan), een native desktopbrowser voor het Nostr-web, bracht [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0) uit op 7 april. Titan resolveert `nsite://`-URL's door mensleesbare namen op te zoeken die op Bitcoin zijn geregistreerd, Nostr-relays te bevragen voor de contentevents van de site en pagina's te renderen die van [Blossom](/nl/topics/blossom/)-servers zijn opgehaald. Het resultaat is een webbrowse-ervaring zonder DNS, zonder TLS-certificaten en zonder hostingproviders. Namen worden geregistreerd via een [webinterface](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register) die gekoppeld is aan Bitcoin-transacties. De eerste release wordt geleverd als een macOS `.dmg` (ARM, met Rosetta 2-ondersteuning voor Intel) en bevat ondersteuning voor een Nix-ontwikkelomgeving.

### Bikel v1.5.0 brengt een native foreground service uit voor de-Googled telefoons

[Bikel](https://github.com/Mnpezz/bikel), een gedecentraliseerde fietstracker die ritten omzet in publieke infrastructuurdata via Nostr, bracht [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0) uit op 4 april. De release migreert van de van GMS afhankelijke Expo TaskManager naar een aangepaste native foreground service, wat betrouwbare achtergrondtracking van ritten garandeert op LineageOS, GrapheneOS en andere de-Googled Android-varianten. De Bikel Bot kreeg een dual-pocket-architectuur met autonome eCash-collectie via Cashu nutzaps. v1.4.3 en v1.4.2 repareren sync van achtergrondtracking voor niet-standaard Android-omgevingen, en de app voegt OSM bike rack map point toggles toe.

### Sprout voegt NIP-01, NIP-23 en NIP-33-ondersteuning toe

[Sprout](https://github.com/block/sprout), een communicatieplatform van Block met een ingebouwde Nostr-relay, bracht [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7) uit op 6 april. Deze week voegde het team ondersteuning toe voor [NIP-23](/en/topics/nip-23/) (Long-form Content) kind `30023`-artikelen, [NIP-33](/en/topics/nip-33/) parameterized replaceable events met vervanging op basis van `d`-tags, en [NIP-01](/nl/topics/nip-01/)/[NIP-02](/en/topics/nip-02/) kind `1` text notes en kind `3` follow lists. De release voegt ook een adaptief IDE-themasysteem met 54 thema's toe, UX-polish voor workflow- en agent-run history, en een opgeschoonde ledenzijbalk.

### mesh-llm v0.56.0 brengt distributed config protocol uit

[mesh-llm](https://github.com/michaelneale/mesh-llm), een gedistribueerd LLM-inferentiesysteem dat Nostr-keypairs gebruikt voor node-identiteit, bracht [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0) uit op 7 april. De release voegt een distributed config protocol toe met ownership-semantiek, asymmetrische KV-cache-kwantisatie (Q8_0-sleutels met Q4-waarden) voor lager geheugengebruik, OS keychain-opslag voor identity keystores, vloeiende chatstreaming met message queuing, en fixes voor fullscreen-layout en KV-cache-splitting met flash attention.

### Nostr VPN brengt ondersteuning voor exit nodes en Umbrel-packaging uit

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), een peer-to-peer VPN die Nostr-relays gebruikt voor signalering en WireGuard voor versleutelde tunnels, bracht deze week zes releases uit van [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0) tot en met [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6). De v0.3.x-cyclus voegt ondersteuning voor exit nodes op Windows en macOS toe, waardoor peers internetverkeer via andere nodes in het netwerk kunnen routeren. Invite- en alias-propagatie synchroniseren nu over Nostr, zodat gebruikers netwerktoegang kunnen delen zonder coördinatie buiten het protocol om. De releases voegen Umbrel-packaging voor self-hosted deployment toe, NAT punch-through met onthouden publieke endpoints, automatische opschoning van verouderde exit nodes en een gepubliceerde protocolspecificatie. Het project stabiliseerde ook de route-afhandeling op macOS met zelfherstellende default routes en underlay-reparatie, en voegde een Android-build via Tauri toe. Builds zijn beschikbaar voor macOS (Apple Silicon en Intel), Linux (AppImage en .deb), Windows en Android.

### Nymchat draait Marmot terug en brengt verbeterde NIP-17-groepschats uit

[Nymchat](https://github.com/Spl0itable/NYM), de MLS-capabele chatclient, bracht 14 releases uit van [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261) tot en met [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274). De belangrijkste wijziging is een protocoldraai: [v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261) voegde Marmot MLS-groepschats toe, maar [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268) keerde terug naar [NIP-17](/nl/topics/nip-17/) omdat de ondersteuning van Marmot voor meerdere apparaten nog niet af is, wat problemen veroorzaakte met de synchronisatie van groepschatstatus tussen apparaten. v3.58.271 introduceert verbeterde NIP-17-groepschats met roterende ephemeral keys voor alle berichten, ontworpen om timing- en correlatieaanvallen te voorkomen. De week bracht ook een friendsysteem met fijnmazige controle over instellingen ([v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)), synchronisatie van MLS-groepschatberichten in versleutelde appinstellingen en meerdere fixes voor relayconnectiviteit.

### nak v0.19.5 voegt Blossom multi-server en outbox-publicatie toe

[nak](https://github.com/fiatjaf/nak), fiatjaf's command-line Nostr-toolkit, bracht [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5) uit. Het `blossom`-commando accepteert nu meerdere `--server`-flags om in één keer naar verschillende [Blossom](/nl/topics/blossom/)-servers te uploaden. Een nieuw `key`-commando breidt partiële sleutels uit door links nullen toe te voegen. Het `event`-commando krijgt een `--outbox`-flag om events via het outbox-model te publiceren, en `fetch` stopt nu met een foutcode wanneer geen event wordt teruggegeven.

## In ontwikkeling

### White Noise voegt thumbhash-previews en push registration bridge toe

[White Noise](https://github.com/marmot-protocol/whitenoise), de private messenger gebouwd op het [Marmot](/nl/topics/marmot/)-protocol, merge'de vijf PR's. [PR #549](https://github.com/marmot-protocol/whitenoise/pull/549) vervangt blurhash-image previews door thumbhash, een nieuwer algoritme dat scherpere placeholderafbeeldingen produceert met een kleinere payload (doorgaans minder dan 30 bytes tegenover blurhash met ongeveer 50-100 bytes), terwijl de aspectverhouding en kleurverdeling van de oorspronkelijke afbeelding behouden blijven. Blurhash blijft als fallback bestaan voor oudere content. [PR #548](https://github.com/marmot-protocol/whitenoise/pull/548) werkt whitenoise-rs bij en voegt de [MIP-05](/nl/topics/mip-05/) push registration bridge toe, waarmee het [werk aan de pushnotificatiespecificatie van vorige week](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications) met de client wordt verbonden. [PR #493](https://github.com/marmot-protocol/whitenoise/pull/493) voegt cursor-based pagination toe voor chatberichten, als vervanging van de eerdere laadstrategie door een scrollgestuurde aanpak.

### Route96 voegt dynamische labelconfiguratie en zero-egress-opruiming toe

[Route96](https://github.com/v0l/route96), de [Blossom](/nl/topics/blossom/)-mediaserver van v0l, merge'de drie PR's. [PR #80](https://github.com/v0l/route96/pull/80) voegt dynamische configuratie van labelmodellen via de admin-API toe, waardoor operators contentclassificatiemodellen kunnen wisselen zonder de server opnieuw te starten. [PR #82](https://github.com/v0l/route96/pull/82) voegt labelconfiguratievelden toe aan de admin-UI. [PR #79](https://github.com/v0l/route96/pull/79) voegt een zero-egress-opruimbeleid toe dat bestanden die nooit zijn gedownload automatisch verwijdert, zodat opslagkosten voor operators laag blijven.

### Snort brengt beveiligingsverharding en DVM-betaalfacturen uit

[Snort](https://github.com/v0l/snort), de webclient, bracht deze week twee releases uit samen met een uitgebreide beveiligingsaudit. Fixes omvatten Schnorr-signatuurverificatie, bescherming tegen relay message forgery in [NIP-46](/nl/topics/nip-46/) (waardoor aanvallers geen signing requests kunnen injecteren via gecompromitteerde relays), verbeteringen aan PIN-versleuteling en verwijdering van vertrouwen op NIP-26-delegatie. Prestatieverbeteringen komen van gebatchte Schnorr-verificatie in WASM, lazy-loaded routes, vooraf gecompileerde vertalingen en het weghalen van dubbele verificatie per event. [PR #618](https://github.com/v0l/snort/pull/618) voegt weergave van payment-required invoices toe voor [NIP-90](/en/topics/nip-90/) (Data Vending Machine) kind `7000`, zodat Snort de Lightning-factuur direct in de feed rendert wanneer een DVM met een betaalverzoek reageert.

### Damus verbetert LMDB-compaction

[Damus](https://github.com/damus-io/damus), de iOS-client, merge'de [PR #3719](https://github.com/damus-io/damus/pull/3719), die automatische LMDB-compaction volgens een schema toevoegt en voorkomt dat de lokale database na verloop van tijd onbegrensd groeit. [PR #3663](https://github.com/damus-io/damus/pull/3663) verbetert de BlurOverlayView zodat die beschermend oogt in plaats van kapot.

### Captain's Log voegt tag-indexering en note-sync toe

[Captain's Log](https://github.com/nodetec/captains-log) (Comet), de Nostr-native long-form schrijftool van Nodetec, merge'de deze week vier PR's. [PR #156](https://github.com/nodetec/captains-log/pull/156) voegt tag-indexering en sync-ondersteuning over notes heen toe, [PR #157](https://github.com/nodetec/captains-log/pull/157) refactort note-sync en tag-afhandeling, en [PR #159](https://github.com/nodetec/captains-log/pull/159) repareert sync van verwijderde notes zodat gewiste notes op alle apparaten verwijderd blijven.

### Relatr v0.2.x herontwerpt plug-insysteem met Nostr-native validator-marktplaats

[Relatr](https://github.com/ContextVM/relatr), een [Web of Trust](/nl/topics/web-of-trust/)-scoringengine die vertrouwensranglijsten berekent op basis van sociale-graafafstand en configureerbare validators, bracht de v0.2.x-familie uit met een complete herziening van het plug-insysteem. Validators worden nu geschreven in Elo, een draagbare functionele expressietaal die is geforkt om host-georkestreerde capabilities in meerdere stappen te ondersteunen (Nostr-queries, social graph-lookups, NIP-05-resolutie). Plug-ins worden gepubliceerd als kind `765` Nostr-events, waardoor distributie native wordt aan het relaynetwerk. Een nieuwe [plugin marketplace](https://relatr.net) laat operators validators ontdekken, installeren en wegen vanuit de browser, met een CLI (`relo`) voor lokaal authoren en publiceren. De architectuur is gesandboxed: plug-ins kunnen alleen capabilities aanroepen die de host expliciet beschikbaar stelt, zodat een kwaadaardige validator niet buiten zijn gedefinieerde scope kan ontsnappen. Relatr-instanties kunnen nu vanaf de website worden beheerd, met volledige zichtbaarheid in welke plug-ins het scoringsalgoritme vormen en welke individuele gewichten ze hebben.

### Shopstr verbetert mobiele navigatie en toegangscontrole

[Shopstr](https://github.com/shopstr-eng/shopstr), de Nostr-native marktplaats voor kopen en verkopen met Bitcoin, pushte deze week 158 commits over de hoofdapp en het begeleidende [Milk Market](https://github.com/shopstr-eng/milk-market)-project. Fixes omvatten verbeteringen aan de mobiele communitylayout, gedrag waarbij menu's bij navigatie sluiten en het automatisch sluiten van dropdowns. Beschermde routes zijn niet langer via een directe URL bereikbaar zonder in te loggen, en de slug-matchinglogica behandelt meerdere exacte matches nu correct.

### Pollerama voegt notificaties, filmzoekfunctie en rating-UI toe

[Pollerama](https://github.com/formstr-hq/nostr-polls), een polling-, survey- en social rating-app gebouwd op Nostr, voegde thread-notificaties, een filmzoekfunctie en een herziening van de rating-UI toe. De release repareert ook problemen met het laden van de feed en verhoogt dependency-versies.

### Purser bouwt Nostr-native betaaldemon met Marmot-versleuteling

[Purser](https://github.com/EthnTuttle/purser), een Nostr-native betaaldemon ontworpen als vervanger voor Zaprite, merge'de deze week negen PR's die de kernarchitectuur uitbouwen. Het project gebruikt [Marmot](/nl/topics/marmot/) MLS via MDK voor versleutelde merchant-customer messaging, met Strike en Square als payment providers. Deze week landden config- en catalog-loading, validatie van berichtschema's, de MDK-communicatielaag, implementaties voor Strike en Square, een polling-engine, anti-spam-rate limiting, persistentie van pending payments en de orderverwerkingspipeline. Alle 99 tests oefenen nu echte mdk-core MLS-operaties uit nadat het team mock MLS verwijderde ten gunste van echte versleuteling in local mode.

### Vector refactort DM-bijlagen en voegt profielbewerking toe

[Vector](https://github.com/VectorPrivacy/Vector), de privacygerichte Nostr-messenger gebouwd met Tauri, merge'de [PR #55](https://github.com/VectorPrivacy/Vector/pull/55), die de frontend refactort. Het decrypten en opslaan van DM-bijlagen is verplaatst naar de vector-core-library, en de app ondersteunt nu profielbewerking. De upload-cancel-flag is correct doorverbonden via TauriSendCallback, en ongebruikte callbacks voor attachment previews zijn opgeschoond.

## Protocol- en specificatiewerk

### NIP-Updates

Recente wijzigingen in het [NIPs-repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-58](/nl/topics/nip-58/) (Badges): Profile Badges verhuizen naar kind 10008, Badge Sets naar kind 30008** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Migreert Profile Badges van kind `30008` naar kind `10008` (een replaceable event, één per pubkey) en introduceert kind `30008` voor Badge Sets. Eerder gebruikten Profile Badges hetzelfde kind (`30008`) als badge-definities, waardoor ze parameterized replaceable events waren met een `d`-tag als sleutel. Het nieuwe kind `10008` is een eenvoudig replaceable event: één per pubkey, zonder `d`-tag. Clients vragen nu per gebruiker één enkel replaceable event op in plaats van parameterized replaceable events te scannen. Amethyst v1.07.3 wordt al met deze migratie geleverd.

- **[NIP-34](/nl/topics/nip-34/) (Git Stuff): Add git-related follow lists** ([PR #2130](https://github.com/nostr-protocol/nips/pull/2130)): Voegt conventies voor follow lists toe voor NIP-34 repository- en issue-tracking. Gebruikers publiceren kind `30000` follow sets met `d`-tags zoals `git-repos` of `git-issues` die `a`-tagverwijzingen bevatten naar repositories (kind `30617`) die zij willen volgen. Clients kunnen zich op deze follow sets abonneren om repository-activiteit in de feed van een gebruiker te tonen, vergelijkbaar met hoe kind `3` contactlijsten werken voor pubkeys.

**Open PR's en discussies:**

- **NIP-AC: P2P Voice and Video Calls over WebRTC** ([PR #2301](https://github.com/nostr-protocol/nips/pull/2301)): Breidt de oorspronkelijke NIP-100 (geïmplementeerd door 0xChat) uit met drie wijzigingen: migratie naar [NIP-44](/nl/topics/nip-44/)-versleuteling verpakt in [NIP-59](/nl/topics/nip-59/) gift wraps om metadata-lekken te elimineren, een gespecificeerde WebRTC-workflow voor de setup van voice- en videocalls (offer, answer, ICE candidates), en een mesh-model voor groepscalls waarin elke peer een directe WebRTC-verbinding opzet met elke andere peer. De specificatie is niet backwards-compatible met NIP-100. Amethyst bouwt er al tegenaan, met een testsuite voor de call state machine ([PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)) en afhandeling van verouderde call offers ([PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)) die deze week landden.

- **[NIP-340](/en/topics/nip-340/) (FROST Quorum)** ([PR #2299](https://github.com/nostr-protocol/nips/pull/2299)): Stelt conventies voor voor threshold-signing op Nostr met [FROST](/nl/topics/frost/) (Flexible Round-Optimized Schnorr Threshold). FROST laat een groep signers gezamenlijk een Nostr-identiteit beheren waarbij elke t-of-n-combinatie events kan signeren zonder de volledige private key te reconstrueren. Het NIP definieert hoe signing-rondes worden gecoördineerd, key shares worden verdeeld en threshold-signed events worden gepubliceerd, voortbouwend op het Igloo-signerwerk uit het [FROSTR-project](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11).

- **[NIP-5D](/en/topics/nip-5d/) (Nostr Web Applets)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Definieert een `postMessage`-protocol voor gesandboxte webapplicaties ("napplets") die in iframes draaien om te communiceren met een hostapplicatie ("shell"). De shell voorziet de napplet via een gestructureerde message-API van Nostr-signing, relaytoegang en gebruikerscontext, terwijl de iframe-sandbox directe sleuteltoegang verhindert. Dit breidt het model voor hosting van statische websites uit [NIP-5A](/en/topics/nip-5a/) uit richting interactieve applicaties die Nostr-events kunnen lezen en schrijven. Het NIP is actief in ontwikkeling met een werkende runtime-implementatie.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls)** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Is hernoemd vanuit het eerdere voorstel NIP-A5. Het definieert conventies voor het publiceren en ontdekken van WebAssembly-programma's op Nostr. WASM-binaries worden als Nostr-events opgeslagen, en clients kunnen ze downloaden en uitvoeren in een gesandboxte runtime. Een [demo-app](https://nprogram.netlify.app/) laat scrolls in de browser draaien, met voorbeeldprogramma's die als Nostr-events zijn gepubliceerd en door elke client kunnen worden opgehaald en uitgevoerd.

- **[NIP-85](/nl/topics/nip-85/) (Trusted Assertions): Clarifications** ([PR #2304](https://github.com/nostr-protocol/nips/pull/2304)): Verscherpt de specificatietaal rond meerdere sleutels en relays per serviceprovider en verduidelijkt hoe clients assertions van providers moeten afhandelen die over meerdere pubkeys of relay-endpoints opereren.

- **[NIP-24](/nl/topics/nip-24/) (Extra Metadata Fields): published_at voor replaceable events** ([PR #2300](https://github.com/nostr-protocol/nips/pull/2300)): Generaliseert de `published_at`-tag uit [NIP-23](/en/topics/nip-23/) (Long-form Content) naar alle replaceable en addressable events. De tag is uitsluitend bedoeld voor weergave: als `published_at` gelijk is aan `created_at`, tonen clients het event als "gemaakt" op dat moment; als ze verschillen (omdat het event is bijgewerkt), kunnen clients in plaats daarvan "bijgewerkt" tonen. Dit laat kind `0`-profielen "joined at"-data tonen en laat andere replaceable events hun oorspronkelijke publicatietijdstip behouden over updates heen. Een aanvullend voorstel voor [NIP-51](/nl/topics/nip-51/) ([PR #2302](https://github.com/nostr-protocol/nips/pull/2302)) voegt dezelfde tag toe aan list-events.

- **[NIP-59](/nl/topics/nip-59/) (Gift Wrap): Ephemeral gift wrap kind** ([PR #2245](https://github.com/nostr-protocol/nips/pull/2245)): Voegt kind `21059` toe als ephemeral tegenhanger van de bestaande kind `1059` gift wrap. Ephemeral events (kinds `20000`-`29999`) volgen de semantiek van [NIP-01](/nl/topics/nip-01/): relays hoeven ze niet op te slaan en mogen ze na bezorging weggooien. Daarmee kunnen applicaties gift-wrapped berichten versturen die van relays verdwijnen zodra ze zijn afgeleverd, wat de opslagbehoefte voor berichtenverkeer met hoog volume vermindert terwijl hetzelfde drielagige versleutelingsmodel als gewone [NIP-17](/nl/topics/nip-17/) DM's behouden blijft.

### OpenSats kondigt zestiende golf Nostr-subsidies aan

[OpenSats](https://opensats.org) kondigde op 8 april zijn [zestiende golf Nostr-subsidies](https://opensats.org/blog/sixteenth-wave-of-nostr-grants) aan, met financiering voor vier eerste subsidies en één verlenging. [Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp) ontvangt financiering voor bijdrager Robert Nagy om een zelfstandige desktopapp te bouwen bovenop de [Quartz](/nl/topics/quartz/) en Commons-modules, waarmee de feature-set van de Android-client naar muisgestuurde interfaces met persistente relayverbindingen wordt gebracht. [Nostr Mail](https://github.com/nogringo/nostr-mail) ontvangt financiering om een volledig e-mailsysteem op Nostr te bouwen met kind `1301`-events verpakt in [NIP-59](/nl/topics/nip-59/) gift wraps, met een Flutter-client en SMTP-bridgeservers voor compatibiliteit met Gmail en Outlook. [Nostrord](https://github.com/Nostrord/nostrord) ontvangt financiering voor een Kotlin Multiplatform [NIP-29](/en/topics/nip-29/) relay-based groepsclient met Discord-achtige groepsberichten, moderatie en threads. [Nurunuru](https://github.com/tami1A84/null--nostr) ontvangt financiering om een native iOS-versie te bouwen van de op Japan gerichte Nostr-client gemodelleerd naar de vertrouwde interface van LINE, met op passkeys gebaseerde biometrische login voor onboarding. HAMSTR kreeg een verlenging van zijn subsidie (voor het eerst gefinancierd in de [elfde golf](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)).

## NIP Deep Dive: NIP-17 (Private Direct Messages)

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) definieert de huidige standaard voor private direct messages op Nostr. Het vervangt het oudere schema van [NIP-04](/nl/topics/nip-04/) (Encrypted Direct Messages), dat metadata lekte (afzender, ontvanger en tijdstempels waren allemaal zichtbaar op relays) en een zwakkere versleutelingsconstructie gebruikte. NIP-17 combineert [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads) voor versleuteling met [NIP-59](/nl/topics/nip-59/) (Gift Wrap) voor bescherming van metadata, en creëert zo een systeem met drie lagen waarin relays niet kunnen zien wie met wie praat.

Het protocol gebruikt drie event kinds die in elkaar zijn genest. De binnenste laag is het daadwerkelijke bericht, een ongetekend kind `14`-event:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

Het kind `14`-event is bewust ongetekend (lege `sig`). De specificatie beschrijft dit als het bieden van ontkenbaarheid, maar in de praktijk is die bescherming beperkt. De kind `13` seal die het rumor-bericht inpakt, is ondertekend met de echte sleutel van de afzender. Een ontvanger kan die ondertekende seal aan een derde partij tonen en daarmee bewijzen dat de afzender met hen heeft gecommuniceerd, zelfs zonder de inhoud van het bericht prijs te geven. Met zero-knowledge proofs kan een ontvanger zelfs de exacte inhoud van het bericht bewijzen zonder zijn eigen private key prijs te geven. Het ongetekende rumor is als een ongetekende brief in een ondertekende envelop: de handtekening op de envelop koppelt de afzender aan de inhoud. Echte ontkenbaarheid zou symmetrische authenticatie vereisen (zoals de HMACs van Signal), wat onverenigbaar is met het gedecentraliseerde relaymodel van Nostr waarin berichten zelfauthenticerend moeten zijn. De echte sterke punten van NIP-17 zijn metadata-privacy en geheimhouding van content, niet ontkenbaarheid.

Dit ongetekende bericht wordt vervolgens verpakt in een kind `13` seal, die door de werkelijke afzender wordt ondertekend en met [NIP-44](/nl/topics/nip-44/) voor de ontvanger wordt versleuteld:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

De seal heeft geen tags, dus zelfs na decryptie zou die de ontvanger niet onthullen. De seal is ondertekend met de echte sleutel van de afzender, waardoor de ontvanger het bericht kan authenticeren door te controleren dat de `pubkey` van de seal overeenkomt met de `pubkey` van het binnenste kind `14`.

De seal wordt daarna verpakt in een kind `1059` gift wrap, ondertekend met een willekeurige wegwerpsleutel en geadresseerd aan de ontvanger:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

De `pubkey` van de gift wrap is een willekeurige sleutel die alleen voor dit bericht wordt gegenereerd, en de `created_at` wordt tot twee dagen in het verleden gerandomiseerd. Dit is de buitenste laag die relays daadwerkelijk zien: een bericht van een onbekende pubkey aan de ontvanger, met een tijdstempel die niet weerspiegelt wanneer het bericht echt is verzonden. De gerandomiseerde tijdstempel beschermt tegen analyse achteraf van opgeslagen events, maar een aanvaller die actief met relays is verbonden kan nog steeds zien wanneer de gift wrap voor het eerst verscheen, waardoor deze verdediging beperkt blijft tot passieve waarnemers die relaydata later opvragen. Omdat de pubkey willekeurig is en de tijdstempel nep, kunnen relays de echte afzender niet bepalen. Om het bericht te lezen decrypt de ontvanger de gift wrap met zijn eigen sleutel en de willekeurige pubkey, vindt daarbinnen de seal, decrypt vervolgens de seal met zijn eigen sleutel en de pubkey van de afzender uit de seal, en vindt daarbinnen het kind `14`-bericht.

NIP-17 biedt geen forward secrecy. Alle berichten worden versleuteld met het statische Nostr-keypair (via de sleutelafleiding van NIP-44 uit de sleutels van afzender en ontvanger). Als een private key gecompromitteerd raakt, kan elk vroeger en toekomstig bericht dat naar die sleutel is versleuteld worden gedecrypt. Dat is een bewuste afruil: omdat versleuteling alleen van de nsec afhangt, kan een gebruiker die zijn nsec back-upt de volledige berichtgeschiedenis herstellen van elke relay die de gift wraps nog bewaart. Protocollen zoals MLS (gebruikt door [Marmot](/nl/topics/marmot/)) bieden forward secrecy via roterend sleutelmateriaal, maar ten koste van statussynchronisatie en met als gevolg dat historische berichten na sleutelrotatie niet meer kunnen worden hersteld.

NIP-17 definieert ook kind `15` voor versleutelde bestandsberichten, met `file-type`-, `encryption-algorithm`-, `decryption-key`- en `decryption-nonce`-tags zodat de ontvanger een bijgevoegd bestand kan decrypten dat met AES-GCM is versleuteld voordat het naar een Blossom-server werd geüpload. Kind `10050` wordt gebruikt om de voorkeurslijst van DM-relays van een gebruiker te publiceren, zodat afzenders weten waar zij gift wraps moeten afleveren. De set van `pubkey` + `p`-tags in een bericht definieert een chatroom; een deelnemer toevoegen of verwijderen maakt een nieuwe room met een schone geschiedenis.

Implementaties dekken de meeste grote clients. [nospeak](https://github.com/psic4t/nospeak) gebruikt NIP-17 voor alle één-op-één-berichten. [Flotilla](https://gitea.coracle.social/coracle/flotilla) gebruikt NIP-17 voor zijn proof-of-work-DM's. [Amethyst](https://github.com/vitorpamplona/amethyst), [Primal](https://github.com/PrimalHQ/primal-android-app), [Nostur](https://github.com/nostur-com/nostur-ios-public), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel) en [Coracle](https://github.com/coracle-social/coracle) implementeren allemaal NIP-17 als hun primaire DM-protocol. De specificatie ondersteunt ook verdwijnende berichten door een `expiration`-tag in de gift wrap te zetten.

## NIP Deep Dive: NIP-46 (Nostr Remote Signing)

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) definieert een protocol om de private key van de gebruiker te scheiden van de clientapplicatie. In plaats van een nsec in een webapp te plakken draait de gebruiker een remote signer (ook wel een "bunker" genoemd) die de private key vasthoudt en op signing requests via Nostr-relays reageert. De client ziet de private key nooit. Dat verkleint het aanvalsoppervlak: een gecompromitteerde client kan signatures aanvragen, maar kan de sleutel zelf niet extraheren.

Het protocol gebruikt kind `24133` voor zowel verzoeken als antwoorden, versleuteld met [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads). Een client genereert voor de sessie een wegwerp-`client-keypair` en communiceert met de remote signer via met NIP-44 versleutelde berichten die met elkaars pubkeys zijn getagd. Hieronder staat een signing request van een client aan een remote signer:

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

De versleutelde `content` bevat een JSON-RPC-achtige structuur:

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

De remote signer decrypt het verzoek, presenteert het aan de gebruiker ter goedkeuring (of keurt het automatisch goed op basis van geconfigureerde permissies), ondertekent het event met de private key van de gebruiker en retourneert het ondertekende event in een antwoord:

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Verbindingen kunnen vanaf beide kanten worden gestart. Een remote signer levert een `bunker://`-URL met zijn pubkey en relayinformatie. Een client levert een `nostrconnect://`-URL met zijn client pubkey, relays en een secret voor verificatie van de verbinding. De `secret`-parameter voorkomt connection spoofing: alleen de partij die de URL out-of-band heeft ontvangen kan de handshake voltooien.

Acht methoden zijn gedefinieerd: `connect` voor het opzetten van de sessie, `sign_event` voor het signeren van events, `get_public_key` om de pubkey van de gebruiker op te vragen, `ping` voor keepalive, `nip04_encrypt`/`nip04_decrypt` voor legacy-versleuteling, `nip44_encrypt`/`nip44_decrypt` voor huidige versleuteling, en `switch_relays` voor relaybeheer. Relaymigratie wordt afgehandeld door de remote signer, die de verbinding in de loop van de tijd naar nieuwe relays kan verplaatsen zonder de sessie te breken.

Clients vragen tijdens het verbinden specifieke capabilities aan via een permissiesysteem. Een permissiestring als `nip44_encrypt,sign_event:1,sign_event:14` vraagt toegang tot NIP-44-versleuteling en signingtoegang voor alleen kind `1`- en kind `14`-events. De remote signer kan deze permissies accepteren, weigeren of aanpassen. Dat betekent dat een webclient voor het lezen en posten van notes misschien alleen permissie `sign_event:1` krijgt, terwijl een DM-client ook `sign_event:14` en `nip44_encrypt` kan krijgen.

[Amber](https://github.com/greenart7c3/Amber) implementeert NIP-46 op Android, en de [v6.0.0-pre1](#amber-v600-pre1-voegt-nip-46-signing-keys-per-verbinding-toe) van deze week voegt signing keys per verbinding toe voor isolatie tussen clients. [nsec.app](https://github.com/nicktee/nsecapp) (voorheen Nostr Connect) levert een webgebaseerde bunker. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) bevat `BunkerSigner` voor JavaScript-clients, en [de PR #530 van vorige week](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing) voegde `skipSwitchRelays` toe voor handmatig relaybeheer. Het protocol ondersteunt ook auth challenges: wanneer een remote signer extra authenticatie nodig heeft (wachtwoord, biometrie of hardwaretoken), reageert die met een `auth_url` die de client in een browser opent zodat de gebruiker die kan voltooien.

---

Dat is het voor deze week. Bouw je iets of heb je nieuws om te delen? Stuur ons een DM op Nostr of vind ons op [nostrcompass.org](https://nostrcompass.org).
