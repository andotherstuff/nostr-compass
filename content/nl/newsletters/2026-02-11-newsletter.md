---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** Mostro brengt zijn eerste publieke beta uit na drie jaar ontwikkeling en brengt P2P Bitcoin-handel naar mobiel via Nostr. OpenSats kent zijn zestiende golf Bitcoin-subsidies toe, waarbij Minibits Wallet verlenging ontvangt voor zijn Nostr-geintegreerde Cashu-wallet. **Zapstore bereikt stabiele 1.0-release**, de mijlpaal voor de gedecentraliseerde Android-appwinkel. Coracle 0.6.29 voegt topics en commentaar op highlights toe. Igloo Desktop v1.0.3 levert ingrijpende beveiligingsverharding voor Frostr threshold signing. Amber v4.1.2-pre1 migreert naar Flow-architectuur. Angor bereikt v0.2.5 met vernieuwde funding-UI en NIP-96 image server-configuratie. NostrPress lanceert als tool die Nostr-profielen omzet naar statische blogs. Antiprimal levert standaardconforme gateway die Primal's proprietary cache server koppelt aan standaard Nostr NIPs. Primal Android merget 18 PR's die de NWC-infrastructuur uitbreiden met dubbele wallet-ondersteuning, auditlogging en de `lookup_invoice`-methode. diVine levert API-first videofeeds. De Marmot TypeScript SDK splitst zijn referentie chatapp af naar aparte repo en begint de migratie naar ts-mls v2. De NIPs-repository merget HyperLogLog approximate counting voor NIP-45 en extraheert identity tags uit kind 0. Vitorpamplona opent meerdere voorstellen die kind 0 metadata-events systematisch afslanken. Nieuwe protocolvoorstellen omvatten Nostr Relay Connect voor NAT-traversal en Nostr Web Tokens voor ondertekende webclaims. De deep dives behandelen NIP-45's nieuwe HyperLogLog approximate counting voor cross-relay eventmetrics en NIP-96's HTTP-bestandsopslagprotocol, nu afgeraden ten gunste van Blossom, terwijl projecten de overgang tussen de twee mediastandaarden doorlopen.

## Nieuws

### Mostro Brengt Eerste Publieke Beta Uit

[Mostro](https://github.com/MostroP2P/mostro), de peer-to-peer Bitcoin-exchange op Nostr, bracht zijn [mobiele app v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0) uit, de eerste publieke beta na drie jaar ontwikkeling. De app maakt directe Bitcoin-handel mogelijk met Nostr voor ordercoordinatie en Lightning voor afwikkeling, zonder custodial tussenpersoon.

Push-notificaties met verbeterde achtergrondbetrouwbaarheid op Android vormen de kern van de release, samen met optioneel loggen waarmee diagnostische gegevens kunnen worden vastgelegd en gedeeld bij problemen, soepelere relay-updates door additieve initialisatie, en Fase 2 UI-verfijningen met internationaliseringsondersteuning. Beschikbaar op [Zapstore](https://zapstore.dev) en als directe [GitHub-download](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0).

Mostro voegt zich bij Shopstr en Plebeian Market in de categorie Nostr-native commerce-applicaties, met als onderscheid dat fiat-naar-Bitcoin exchangecoordinatie centraal staat. De onderliggende [Mostro daemon](https://github.com/MostroP2P/mostro) handelt ordermatching en geschillenbeslechting af over Nostr relays.

### OpenSats Zestiende Golf Bitcoin-Subsidies

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants) kondigde subsidies aan voor 17 open-sourceprojecten. De Nostr-relevante toekenning: [Minibits Wallet](https://github.com/minibits-cash/minibits_wallet), de Android [Cashu](/nl/topics/cashu/)-wallet met [NIP-60](/nl/topics/nip-60/) wallet event-ondersteuning en nutzap-integratie, ontving verlengingssubsidie. Minibits gebruikt Nostr events om ecash-tokenstatus op te slaan, waardoor wallet-backups draagbaar worden tussen apparaten door relay sync.

### NostrPress: Nostr-Profiel naar Statische Blog

[NostrPress](https://github.com/besoeasy/NostrPress) ([blog.besoeasy.com](https://blog.besoeasy.com)) zet Nostr-profielen om naar volledig statische blogs, deploybaar waar dan ook. Artikelen worden op Nostr gepubliceerd met willekeurige clients, waarna NostrPress uit die events vanzelf websites genereert, compleet met lokale media-hosting en RSS-feeds.

Gebouwd met Nunjucks-templating en JavaScript produceert NostrPress sites zonder platformvergrendeling. De gegenereerde output is puur HTML/CSS, geschikt voor elke statische bestandsserver, GitHub Pages, Netlify of persoonlijke VPS. De tool voegt zich bij [Npub.pro](https://github.com/nostrband/nostrsite) en [Servus](https://github.com/servus-social/servus) voor wie Nostr-content wil omzetten naar traditionele websites.

### Antiprimal: Standaardconforme Gateway naar Primal's Cache

[antiprimal](https://gitlab.com/soapbox-pub/antiprimal) ([antiprimal.net](https://antiprimal.net)), van Alex Gleason en het Soapbox-team, is de WebSocket-gateway die Primal's proprietary cache server koppelt aan standaard Nostr-protocolberichten. Primal biedt functies als eventstatistieken en content-zoeken, plus Web of Trust-berekeningen over `wss://cache.primal.net/v1`, maar toegang vereist proprietary berichtformaat met niet-standaard `cache`-veld dat gewone Nostr-clients niet kunnen gebruiken. Antiprimal vertaalt standaard NIP-verzoeken naar Primal's formaat en converteert de antwoorden terug.

Ondersteund worden [NIP-45](/nl/topics/nip-45/) COUNT-queries (reacties, antwoorden, reposts, zap-tellingen, volger-tellingen), [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) zoeken, [NIP-11](/nl/topics/nip-11/) relay-informatie en [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) Trusted Assertions voor Primal's voorberekende Web of Trust-gegevens. Via begeleidende bot publiceert het project NIP-85 kind 30382 (gebruikersstatistieken) en kind 30383 (event engagement) events naar configureerbare relays. Gebouwd op TypeScript/Bun met de Nostrify-library telt de codebase 53 commits in zijn eerste drie dagen na oprichting op 6 februari en is live op antiprimal.net.

### Ikaros: AI Agent Messaging Gateway voor Signal en Nostr

[Ikaros](https://gitlab.com/soapbox-pub/ikaros), eveneens van het Soapbox-team, is de messaging-gateway die AI-agents in staat stelt te communiceren over zowel Signal als Nostr versleutelde DM's. De bridge gebruikt het [Agent Client Protocol](https://agentclientprotocol.org) (ACP) om willekeurige ACP-compatibele AI-codeassistenten te verbinden met echte berichtennetwerken. Drie pull requests vormen de initiële bouw.

De eerste, [PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1), implementeert volledige [NIP-04](/nl/topics/nip-04/) versleutelde DM-adapter met verzend/ontvangstondersteuning, responsbuffering met expliciete flush bij voltooiing, `nsec`- en hex-privesleutelformaten, multi-relay publishing met automatische herverbinding en interactieve setup-wizard. De adapter gebruikt nostr-tools v2.23.0 en updatet de ACP SDK naar v0.14.1.

Stil berichtverlies door sessie-update race condition is opgelost in [PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2): inkomende notificaties die arriveerden voordat registratie in de map was voltooid gingen stilletjes verloren, en de fix buffert die notificaties voor replay zodra registratie afrondt. Signal-gebruikers- en groepsnaam/UUID-metadata voor agent-interacties zijn toegevoegd in [PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3), zodat de AI-agent weet met wie die praat en in welke groep. Hiermee opent Ikaros nieuwe ontwerpruimte: AI-agents bereikbaar over Nostr DM's die ook vanuit Signal benaderd kunnen worden, of andersom.

### Kind 0 Afslankingscampagne

vitorpamplona opende meerdere PR's met als voorstel de systematische extractie van gegevens uit kind 0 (gebruikersmetadata) events naar toegewijde event kinds. De campagne pakt groeiend probleem aan: kind 0 events hebben in de loop der tijd velden verzameld die de meeste clients niet gebruiken, waardoor elke profielfetch groter wordt dan nodig.

Gemerged is [PR #2216](https://github.com/nostr-protocol/nips/pull/2216), dat identity tags (`i` tags) verplaatst van kind 0 naar nieuwe kind 10011 omdat adoptie van die tags minimaal is gebleven. Verplaatsing van [NIP-05](/nl/topics/nip-05/)-verificatie naar kind 10008 wordt voorgesteld in [PR #2213](https://github.com/nostr-protocol/nips/pull/2213), waardoor meerdere NIP-05-identifiers per gebruiker mogelijk worden en events gefilterd kunnen worden op NIP-05-adres. Extractie van Lightning-adressen (lud06/lud16) naar nieuwe kind wordt voorgesteld in [PR #2217](https://github.com/nostr-protocol/nips/pull/2217), zodat niet elk kind 0-event zap-gerelateerde velden meedraagt die alleen relevant zijn voor clients met Lightning-integratie.

De voorstellen hebben de bredere discussie over de structuur van kind 0 nieuw leven ingeblazen, waaronder [PR #1770](https://github.com/nostr-protocol/nips/pull/1770), het langlopende voorstel om geserializeerde JSON in kind 0 content te vervangen door gestructureerde tags.

### NIP-70 Relay-Ondersteuning Kritiek voor Beveiliging Versleutelde Berichten

White Noise, de [Marmot](/nl/topics/marmot/)-implementatie, heeft [kritiek hiaat geidentificeerd](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html) in relay-ondersteuning voor [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) (Protected Events) en [NIP-42](/nl/topics/nip-42/) (Authentication). Uit tests bleek dat grote publieke relays waaronder Damus, Primal en nos.lol beschermde events ronduit afwijzen met `blocked: event marked as protected`-fouten, in plaats van de vereiste authenticatie-uitdaging te initiëren.

Daarmee breekt er beveiligingsfunctionaliteit: NIP-70 maakt veilige verwijdering van gebruikte MLS KeyPackages mogelijk en voorkomt "harvest now, decrypt later"-aanvallen. Protocollen voor versleutelde berichten kunnen hun gebruikers niet beschermen tegen toekomstig sleutelcompromis zolang relay-ondersteuning ontbreekt. White Noise heeft NIP-70 standaard uitgeschakeld als reactie, met optionele vlag voor wie wel ondersteunende relays heeft.

**Oproep aan relay-operators:** Implementeer de volledige NIP-42 authenticatieflow. Daag bij binnenkomst van beschermde events de client uit om eigenaarschap te bewijzen en accepteer vervolgens gevalideerde schrijfacties. Afwijzen van beschermde events zonder authenticatie breekt protocolbeveiligingsgaranties waarop versleutelde berichtenapplicaties vertrouwen.

## Releases

### Coracle 0.6.29

[Coracle](https://github.com/coracle-social/coracle) ([coracle.social](https://coracle.social)), hodlbod's webclient, bracht [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29) uit. De release voegt weergave van topics en commentaar op kind 9802 highlights toe. Lijstnavigatie geeft nu snelle toegang tot zelfsamengestelde lijsten vanuit de hoofd-UI. Onder de motorkap is Coracle geupgraded naar nieuwe versie van Welshman, de gedeelde Nostr-library die relaybeheer en eventafhandeling aandrijft. De standaard relay-lijst is vernieuwd en Glitchtip-foutregistratie is verwijderd uit de codebase.

### Igloo Desktop v1.0.3

[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), de [FROST](/nl/topics/frost/)-gebaseerde threshold signer en sleutelbeheer-applicatie, bracht [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3) uit met uitgebreide beveiligingsverharding. IPC-validatie en Electron-isolatie bieden bescherming naast SSRF-bewuste relaychecks als verdediging tegen server-side request forgery. Vernieuwde onboarding- en share-importflows vereenvoudigen sleuteldistributie, relayplanning bevat nu normalisatie en prioriteitssamenvoeging, en preload-gebaseerde Electron API-architectuur verbetert de beveiligingsgrens tussen renderer en hoofdproces. Signer keep-alive handhaaft de stabiliteit van threshold signing-sessies, terwijl UX-verbeteringen de frictie van sleutelrestauratie verminderen.

### Amber v4.1.2-pre1

[Amber](https://github.com/greenart7c3/Amber), de Android event signer, bracht [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1) uit met fix voor de ontbrekende relay-vertrouwensscoreweergave uit v4.1.1 en oplossingen voor JSON-parsingproblemen bij niet-Nostr encrypt/decrypt-verzoeken. Het accountmodel migreert van LiveData naar Flow voor voorspelbaarder statusbeheer. Bunker secrets schakelen over naar volledige UUID's en de release upgradet naar Gradle plugin 9.

### Mostro Mobile v1.1.0 en Daemon v0.16.1

Zie de [Nieuwssectie hierboven](#mostro-brengt-eerste-publieke-beta-uit) voor volledige coverage van de mobiele release. Aan de serverkant bracht de [Mostro daemon](https://github.com/MostroP2P/mostro) [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1) uit, met automatisch publiceren van NIP-01 kind 0 metadata bij opstart ([PR #575](https://github.com/MostroP2P/mostro/pull/575)), zodat de daemon nu zijn identiteit aankondigt aan het netwerk bij online komen. Documentatiefixes voor dev fee-berekening zijn ook meegenomen ([PR #571](https://github.com/MostroP2P/mostro/pull/571)).

### Angor v0.2.5

[Angor](https://github.com/block-core/angor) ([angor.io](https://angor.io)), gedecentraliseerd P2P-fundingprotocol op Bitcoin en Nostr, bracht [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5) uit met drie gemergde PR's. De Funds-beheersectie (V2) is herontworpen in [PR #649](https://github.com/block-core/angor/pull/649), met nieuwe interface voor individuele UTXO's en investeringsposities. InvoiceView-herziening in [PR #651](https://github.com/block-core/angor/pull/651) brengt bijgewerkte knopstijlen en sluitbare dialogen, plus nieuw "Copy Address"-commando met annuleringsondersteuning voor adresmonitoring en verbeterde investeringsflowafhandeling. Configureerbare [NIP-96](/nl/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) image servers in instellingen komen in [PR #652](https://github.com/block-core/angor/pull/652), zodat per project gekozen kan worden welk media-upload-endpoint afbeeldingen en documentatie afhandelt. [v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4) werd de week ervoor uitgebracht.

### Ridestr v0.2.2 en v0.2.3

[Ridestr](https://github.com/variablefate/ridestr), het gedecentraliseerde rideshare-platform [vorige week behandeld](/nl/newsletters/2026-02-04-newsletter/#ridestr-v020-roadflare-release), ging door met snelle iteratie in [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2) (Bridge Payment Hotfix) en [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3) na de v0.2.0 "RoadFlare Release." De v0.2.2-hotfix lost bug op waarbij cross-mint [Cashu](/nl/topics/cashu/) bridge-betalingen ritten automatisch annuleerden terwijl de betaling nog werd verwerkt of uiteindelijk zou slagen, en voorkomt zo premature ritannulering bij tragere afwikkelingen. UI-flikkering en kapotte touch-hitboxes op de "mijn locatie"-knop zijn ook opgelost. v0.2.3 bevat extra bugfixes. Beide releases bevatten aparte APK's voor Ridestr (passagiersapp) en Drivestr (chauffeursapp).

### Nostr PHP 1.9.4

[Nostr PHP](https://github.com/nostrver-se/nostr-php) ([nostr-php.dev](https://nostr-php.dev)), de PHP-helperbibliotheek voor Nostr, bracht [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4) uit met configureerbare `timeout`-eigenschap voor de request class ([PR #106](https://github.com/nostrver-se/nostr-php/pull/106)). Ontwikkelaars kunnen nu aangepaste timeoutduren instellen voor relay-verbindingen en berichtverzoeken, waardoor oneindig wachten wordt voorkomen bij niet-reagerende of trage relays.

### Zapstore v1.0.0

[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0) ([zapstore.dev](https://zapstore.dev)), de permissieloze Android-appwinkel op Nostr, **bereikte zijn stabiele 1.0-releasemijlpaal** na maanden van release candidates.

De 1.0-release bevat verbeteringen voor stabiliteit: installeerknopstatusafhandeling die ervoor zorgt dat de verwijderknop direct verschijnt na voltooiing en gebruiksvriendelijke foutmeldingen met uitklapbare technische details. De "Issue melden"-knop verstuurt versleutelde DM's over Nostr met ephemeral keys. Verder: nieuw updatescherm met polling en batchtracking, betere download-watchdog voor vastgelopen transfers, dynamische limieten voor gelijktijdige downloads op basis van apparaatprestaties, frequentere synchronisatie van geinstalleerde packages en verbeterde versievergelijkingslogica. Het team loste kritiek flutter_secure_storage-probleem op en verbeterde de afhandeling van edge cases in de package manager.

De mijlpaal vertegenwoordigt de volwassenwording van Nostr's eerste toegewijde appdistributieplatform, waarmee ontwikkelaars Android-applicaties direct aan gebruikers kunnen publiceren zonder gecentraliseerde appwinkel-gatekeeping.

### ZSP v0.3.1

[ZSP](https://github.com/zapstore/zsp), de Go CLI-tool van het [Zapstore](https://github.com/zapstore/zapstore)-team die eerdere publishing-tooling vervangt voor ondertekenen en uploaden van Android-apps naar Nostr relays, bracht [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1) uit. ZSP handelt APK-acquisitie af van GitHub, GitLab, Codeberg, F-Droid of lokale bestanden, parseert vervolgens metadata, ondertekent Nostr events (met privesleutel, [NIP-46](/nl/topics/nip-46/) bunker of [NIP-07](/nl/topics/nip-07/) browserextensie) en uploadt artefacten naar [Blossom](/nl/topics/blossom/)-servers. Volledige offline modus voor keystore-koppeling zonder netwerkverbinding is nieuw, naast `Content-Digest`-headers op Blossom-uploads voor protocolconformiteit, gefixte arm64-v8a APK-detectie van F-Droid-repositories, GitLab trailing query parameter-fixes en `.env`-bestandsondersteuning voor configuratie.

### Damus iOS 1.17

[Damus](https://github.com/damus-io/damus), de iOS Nostr-client, ging naar versie 1.17 ([PR #3606](https://github.com/damus-io/damus/pull/3606)). De release lost RelayPool-probleem op waarbij verbindingen sloten na ephemeral lease release ([PR #3605](https://github.com/damus-io/damus/pull/3605)), wat ertoe kon leiden dat abonnementen onverwacht wegvielen. Daarnaast is bug opgelost waarbij de favorietentijdlijn geen events toonde bij tabwisseling ([PR #3603](https://github.com/damus-io/damus/pull/3603)).

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak), de Nostr army knife CLI, bracht [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) uit met drie stabiliteitsfixes: voorkomen van panic bij nil of te korte AUTH challenge tags en controleren van dateparser-fouten voordat de geparseerde waarde wordt gebruikt. Cashu mint-URL's zonder `://`-separator worden nu ook correct afgehandeld.

### Mi: Browsergebaseerde Lokale Relay

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git) ([mi.shakespeare.wtf](https://mi.shakespeare.wtf)), nieuwe [Shakespeare](https://shakespeare.wtf) MiniApp, is browsergebaseerde lokale relay die Nostr events archiveert in IndexedDB. Mi haalt profielen (kind 0), contactlijsten (kind 3), relay-lijsten (kind 10002) en wallet events op van verbonden relays en slaat ze lokaal op, waardoor offline toegang tot eigen gegevens ontstaat. Gebouwd met React en nostr-tools 2.15.0.

### Agora v1.0.2

[Agora](https://gitlab.com/soapbox-pub/agora) ([agora.spot](https://agora.spot)), gedecentraliseerd activisme- en fondsenwervingsplatform van Soapbox, bracht [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2) uit met Android APK beschikbaar voor directe installatie. Compass vermeldt Agora hier voor het eerst; de lancering was op 17 januari met de missieverklaring: "Sluit je aan bij de wereldwijde beweging voor vrijheid. Stuur steun naar activisten in het veld internationaal en neem deel aan lokale acties."

Centraal staat wereldkaart waar gebruikers per land browsen, locatiegetagde "acties" aanmaken (protesten, campagnes, fondsenwerving, community-organisatie) en die bespreken in threaded comments. Alle content verspreidt zich over Nostr relays, zodat geen centrale server offline kan worden gehaald om coordinatie te onderdrukken. Agora ondersteunt meerdere talen met CI-afgedwongen vertalingspariteit, integreert [Blossom](/nl/topics/blossom/) mediaservers voor uploads en bevat zoeken, hashtagbrowsing met globale/regionale schakelaar, profielen en reactiesystemen. De v1.0.2-release is de huidige Android-build, beschikbaar als directe APK-download.

### xonos v0.1.6

[xonos](https://codeberg.org/xonos/xonos), de experimentele 3D Nostr-client gebouwd met de Bevy game engine, bracht [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6) uit. xonos rendert Nostr events in 3D ruimtelijke omgeving met text-to-speech-mogelijkheden, en verkent hoe sociale protocolgegevens zouden kunnen werken buiten conventionele 2D-interfaces.

## Projectupdates

### Primal Android Breidt NWC-Infrastructuur Uit

[Primal Android](https://github.com/PrimalHQ/primal-android-app) mergede 18 PR's, als vervolg op de NWC-uitbouw die [vorige week begon](/nl/newsletters/2026-02-04-newsletter/#primal-android-ships-nwc-encryption). Ondersteuning voor NWC-verbindingen over beide wallets (Spark en extern) komt in [PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883), en de `lookup_invoice` NWC-methode voor betalingsstatuscontrole in [PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879).

NWC request-response auditlogging voor wallet-debugging is toegevoegd in [PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880). Multi-accountondersteuning voor `PrimalNwcService` in [PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877) stelt mensen met meerdere profielen in staat aparte wallet-verbindingen te behouden. Periodieke opruiming van verlopen budgetreserveringen in [PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882) voorkomt dat verouderde betalingsreserveringen wallet-operaties blokkeren.

UI-werk omvat herontwerp van wallet-upgradescherm ([PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)), wallet-upgrade FAQ ([PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)), Lightning-adresinstelling tijdens onboarding ([PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)), en fix voor zap-transacties die verschenen als reguliere betalingen voor niet-Lightning types ([PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)).

### diVine Levert API-First Videofeeds

[diVine](https://github.com/divinevideo/divine-mobile), de korte-video-client, mergede 19 PR's met verschuiving richting API-first architectuur. API-first videofeeds komen in [PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468), met trending en recente API-endpoints plus home-feed in [PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466). Specifieke videocontrollers worden geindexeerd in [PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433) voor efficiente feedrendering.

Profielafhandeling verbeterde met cache-plus-fresh patroon in [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440), wat laadtijden verkort en tegelijk gegevensversheid waarborgt bij andermans profielen. Het team leverde ook notificatiefixes ([PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)) en refactoring van de commentaarflow ([PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)). Tabswiping op het notificatiescherm komt in [PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388).

### White Noise: Keyring-Unificatie en Zoekfunctie

De [White Noise](https://github.com/marmot-protocol/whitenoise-rs) backend voor het [Marmot](/nl/topics/marmot/)-protocol mergede 4 PR's. Twee daarvan verbeterden keyring-afhandeling: [PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468) maakt de keyring-service identifier configureerbaar via `WhitenoiseConfig`, en [PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475) unificeert de implementatie op enkele `keyring-core` crate met platformnative stores, ter vervanging van gefragmenteerde platformspecifieke code. Los daarvan voegt [PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470) zoekfunctionaliteit toe.

### Marmot TS Splitst Referentie Chatapp Af

De [Marmot](/nl/topics/marmot/) TypeScript SDK ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) mergede [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40), die de ingebouwde referentie chatapplicatie verwijdert en afsplitst naar eigen repo: [marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat). Aangemaakt op 6 februari is de nieuwe repo referentie-implementatie met eigen CI-pipeline, tabbedchatweergave en onafhankelijk buildsysteem. Door de scheiding kan de SDK zich richten op library-taken terwijl de chatapp onafhankelijk aan UX itereert.

Open PR [#41](https://github.com/marmot-protocol/marmot-ts/pull/41) migreert marmot-ts naar ts-mls v2.0.0, met herontworpen API met uniforme contextobjecten, nieuwe hulpprogramma's voor berichtafhandeling (event creation, reading, deserialization), key package metadata-helpers en ondersteuning voor verwijderingsevents.

### Alby Hub Updates

[Alby Hub](https://github.com/getAlby/hub) mergede 5 PR's. De Alby CLI is toegevoegd aan de app store-interface in [PR #2049](https://github.com/getAlby/hub/pull/2049). Afhandeling van ongeldige zap-gegevens in de transactielijst is opgelost in [PR #2033](https://github.com/getAlby/hub/pull/2033), en de ongebruikte `ListTransactions`-methode is verwijderd uit de LNClient-interface in [PR #2046](https://github.com/getAlby/hub/pull/2046).

### Notedeck Levert Dashboard en Agentium

[Notedeck](https://github.com/damus-io/notedeck), de cross-platform Nostr-client van Damus, mergede 6 PR's. Initieel dashboard-app komt in [PR #1247](https://github.com/damus-io/notedeck/pull/1247). Agentium, multi-agent ontwikkelomgeving die de Dave AI-assistent transformeert tot systeem met duale AI-modi en scenegebaseerd agentbeheer, is geintroduceerd in [PR #1293](https://github.com/damus-io/notedeck/pull/1293). Meerregelige berichtensamensteller met Signal-achtige toetsenbindingen volgt in [PR #1276](https://github.com/damus-io/notedeck/pull/1276), en mediaprestatieverbetering in [PR #1278](https://github.com/damus-io/notedeck/pull/1278). Openstaande PR's van belang zijn onder andere [outbox-infrastructuur](https://github.com/damus-io/notedeck/pull/1288) en [NIP-34](/nl/topics/nip-34/) [Git App-planning](https://github.com/damus-io/notedeck/pull/1289).

### Agora Levert Grote UI-Herziening

[Agora](https://gitlab.com/soapbox-pub/agora) mergede 7 PR's naast de v1.0.2-release. Grootste is [PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106), dat 11 UI-taken afsluit over instellingen, profielbewerking, kaartinteracties, zoekresultaten, commentaarfiltering en Blossom-serverbeheer. De merge schakelde reactieknoppen uit voor niet-geauthenticeerde bezoekers (die eerder stille fouten kregen bij pogingen tot reageren op posts op de kaart), loste date-line kaartpanning op en voegde vetgedrukte overeenkomende tekst toe in zoekresultaten.

Commentaartellingen verschijnen nu onder feedposts en op threadpagina's dankzij [PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108). Automatische herpoging bij mislukte eventbelading met expliciete herlaadknop bij uitgeputte pogingen komt in [PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107). Hashtagbrowsing is gewijzigd naar standaard globaal bereik in [PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104), aangezien de vorige landgerichte standaard vaak nul resultaten opleverde.

Vertalingspariteitcontrole over alle talen is als CI-stap toegevoegd in [PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109), waarbij de build faalt bij ontbrekende waarden. Lange notities in feeds worden afgeknipt in [PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110) om scrollritme te behouden, en iOS mobiel zoomprobleem bij reageren op acties is opgelost in [PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111), veroorzaakt door kleine lettergroottes.

### Clawstr Levert CLI en Lightning Zap-Knoppen

[Clawstr](https://gitlab.com/soapbox-pub/clawstr), het Reddit-geinspireerde platform waar AI-agents communities aanmaken en beheren op Nostr, mergede 3 PR's. Handmatige nak-commando's in AI-agent skill-definities zijn vervangen door nieuw `@clawstr/cli`-pakket (`npx -y @clawstr/cli@latest`) in [PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11), met eliminatie van handmatige JSON-eventconstructie ten gunste van CLI-commando's plus wallet-operaties (init, balance, zap, npc) en [NIP-50](/nl/topics/nip-50/) full-text zoeken.

"For Humans"-documentatiepagina en `ProfileZapDialog`-component komen in [PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13). De zap-knop verschijnt op profielpagina's voor wie Lightning-adres heeft geconfigureerd en werkt zonder inloggen, met directe LNURL-pay met vooraf ingestelde sats-bedragen en QR-codeweergave. In [PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12) is het `wallet sync`-commando gedocumenteerd, met uitleg hoe betalingen aan Lightning-adressen worden vastgehouden door NPC totdat agents expliciet hun wallets synchroniseren.

## NIP-Updates

Recente wijzigingen aan de [NIPs-repository](https://github.com/nostr-protocol/nips):

**Samengevoegd:**

- **[NIP-45: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45 (Event Counting)](/nl/topics/nip-45/) ondersteunt nu HyperLogLog (HLL) approximate counting. Relays kunnen 256-byte HLL-registerwaarden retourneren naast COUNT-responses. Door registers van meerdere relays te mergen berekenen clients bij benadering de cardinaliteit, zonder volledige eventsets te downloaden. Primair gebruik is het berekenen van volger- en reactietellingen zonder afhankelijkheid van enkele relay als gezaghebbende bron. Zelfs twee reactie-events verbruiken meer bandbreedte dan de 256-byte HLL-payload. HyperLogLog++-correcties zijn beschikbaar voor verbeterde nauwkeurigheid bij kleine cardinaliteiten.

- **[NIP-39: Identity Tags Verplaatst uit Kind 0](https://github.com/nostr-protocol/nips/pull/2216)** - [NIP-39](/nl/topics/nip-39/) identity claim tags (`i` tags) zijn geextraheerd uit kind 0 metadata-events naar toegewijde kind 10011. Bijna geen clients ondersteunen die tags, waardoor ze omvang toevoegen aan elke kind 0-fetch zonder waarde te bieden. De eerste in reeks kind 0-extractie-PR's van vitorpamplona (zie [Nieuwssectie](#kind-0-afslankingscampagne)).

**Open PR's en Discussies:**

- **[NIP-XX: Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos stelt protocol voor om Nostr relays te benaderen door versleutelde tunneling over publieke rendezvous relay. Toegang tot relays achter NAT of firewalls wordt mogelijk, inclusief persoonlijke relays op thuisservers of mobiele apparaten. De tunneling gebruikt kind 24891/24892 events met [NIP-44](/nl/topics/nip-44/)-encryptie over rendezvous relay die het verkeer niet kan ontcijferen. Praktische toepassing: elke Nostr-client kan lokale opslag (IndexedDB, SQLite) blootstellen als relay-endpoint voor cross-device sync. Standaard NIP-01 semantiek (REQ, EVENT, CLOSE, COUNT) gaat transparant door de tunnel. Referentie-implementaties bestaan in Go (ORLY Relay) en TypeScript (Smesh).

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc stelt Nostr Web Tokens voor, Nostr event-formaat voor overdracht van ondertekende claims tussen webpartijen, geinspireerd door JSON Web Tokens (JWTs). NWT kan zowel [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (HTTP Auth) als [Blossom autorisatie-events](/nl/topics/blossom/) vertegenwoordigen, wat flexibiliteit geeft in hoe en hoe lang tokens geldig blijven. Referentie Go-library is beschikbaar. [Video-uitleg](https://github.com/pippellia-btc/nostr-web-tokens) en [gedetailleerde vergelijking](https://github.com/pippellia-btc/nostr-web-tokens?tab=readme-ov-file#comparisons) met NIP-98 en Blossom Auth zijn gelinkt in de PR.

- **[NIP-47 Vereenvoudiging](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz stelt voor om de `multi_`-methoden te verwijderen uit [NIP-47 (Nostr Wallet Connect)](/nl/topics/nip-47/), die complex waren om te implementeren en geen adoptie kregen. De PR vermindert ook duplicatie in encryptie en backward compatibility-afhandeling, en schoont de spec op na [de hold invoice-toevoeging van vorige week](/nl/newsletters/2026-02-04-newsletter/#nip-updates).

- **[NIP-05: Verplaatsen naar Eigen Event Kind](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona stelt voor om NIP-05-verificatie van kind 0 te verplaatsen naar nieuwe kind 10008, waardoor meerdere NIP-05-identifiers per gebruiker mogelijk worden en filtering op NIP-05-adres. Onderdeel van de kind 0-afslankingscampagne.

- **[NIP-57: Lightning-Adressen uit Kind 0](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona stelt voor lud06/lud16 (Lightning-adressen) te extraheren uit kind 0 naar toegewijd event kind volgens [NIP-57](/nl/topics/nip-57/), als vervolg op de kind 0-afslanking.

- **[Profiel Hypercustomization](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf stelt uitgebreide profielaanpassingsmogelijkheden voor die verder gaan dan wat kind 0 momenteel ondersteunt.

## NIP Deep Dive: NIP-45 (Event Counting) en HyperLogLog

[NIP-45](/nl/topics/nip-45/) ([spec](https://github.com/nostr-protocol/nips/blob/master/45.md)) definieert hoe clients relays kunnen vragen events te tellen die overeenkomen met filter, zonder de events zelf over te dragen. De merge van [HyperLogLog-ondersteuning](https://github.com/nostr-protocol/nips/pull/1561) voegt probabilistische datastructuur toe die fundamenteel probleem oplost: tellen over meerdere onafhankelijke relays.

**Het Probleem:**

Events tellen op enkele relay is eenvoudig: stuur COUNT-verzoek, krijg getal terug. Over het netwerk tellen is moeilijker. Meldt relay A 50 reacties en relay B 40, dan is de som niet 90 omdat veel events op beide relays bestaan. Werkelijk aantal is onberekenbaar zonder downloaden en dedupliceren van de volledige eventsets.

**HyperLogLog:**

HyperLogLog (HLL) is probabilistisch algoritme dat unieke elementen in verzameling schat met vaste hoeveelheid geheugen. De NIP-45-implementatie gebruikt 256 registers van elk byte, wat precies 256 bytes verbruikt ongeacht hoeveel events worden geteld. De werking berust op onderzoek van de binaire representatie van elke event ID, waarbij de positie van de leidende nullen wordt bijgehouden. Events waarvan de ID's beginnen met veel nullen zijn statistisch zeldzaam, dus hun voorkomen duidt op grote verzameling.

**Werking in NIP-45:**

Relays die reageren op COUNT-verzoek kunnen `hll`-veld bevatten met base64-gecodeerde registerwaarden:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

De client verzamelt HLL-waarden van meerdere relays en merget die door de maximumwaarde op elke registerpositie te nemen. Gemergede HLL vertegenwoordigt de unie van eventsets over relays, met automatische deduplicatie. De uiteindelijke cardinaliteitsschatting wordt berekend uit de gemergede registers.

**Nauwkeurigheid:**

Met 256 registers is de standaardfout ongeveer 5,2%. Voor werkelijk aantal van 1.000 valt de schatting typisch tussen 948 en 1.052. Bij grotere aantallen blijft de relatieve fout constant: werkelijk aantal van 100.000 schat op ruwweg 94.800-105.200. HyperLogLog++-correcties verbeteren de nauwkeurigheid voor kleine cardinaliteiten (onder ~200), waar het basisalgoritme de neiging heeft om te overschatten.

**Waarom Dit Ertoe Doet:**

Sociale metrics (volger-tellingen, reactietellingen) zijn kernfunctie van sociale media-apps. Zonder HLL moeten ze ofwel enkele "vertrouwde" relay bevragen (wat het tellen centraliseert) of events van iedere relay downloaden (wat bandbreedte verspilt). HLL levert goede benaderende telling van meerdere relays met totale overhead van 256 bytes per relay, ongeacht het werkelijke aantal. Zelfs twee reactie-events verbruiken meer bandbreedte dan volledige HLL-payload.

De spec fixeert het aantal registers op 256 voor interoperabiliteit. Iedere relay produceert HLL-waarden die clients kunnen mergen, ongeacht welke relay-implementatie ze draaien. Die standaardisatie betekent dat eenmalige HLL-implementatie volstaat om te profiteren van elke relay die het ondersteunt.

**Huidige Status:**

Geopend door fiatjaf en maanden in discussie, is de PR nu gemerged. Relay-implementaties zullen HLL-berekening moeten toevoegen aan hun COUNT-handlers. Client-implementaties moeten HLL-merging inbouwen in hun count-aggregatielogica.

## NIP Deep Dive: NIP-96 (HTTP-Bestandsopslag) en de Transitie naar Blossom

[NIP-96](/nl/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) definieerde hoe Nostr-clients bestanden uploaden, downloaden en beheren op HTTP-mediaservers. Nu gemarkeerd als "afgeraden" ten gunste van [Blossom](/nl/topics/blossom/) (BUD-gebaseerde media-hosting), blijft NIP-96 relevant omdat Angor v0.2.5 [NIP-96 serverconfiguratie toevoegde](#angor-v025) en ZSP v0.3.1 [uploadt naar Blossom-servers](#zsp-v031), wat protocoltransitie in uitvoering illustreert.

**Werking van NIP-96:**

Via `/.well-known/nostr/nip96.json` ontdekt de client de mogelijkheden van bestandsserver, met API-URL, ondersteunde contenttypes, groottelimieten en beschikbare mediatransformaties:

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

Voor uploads stuurt de client `multipart/form-data` POST naar de API-URL met [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) autorisatieheader (ondertekend Nostr event dat de identiteit van de uploader bewijst). De server retourneert [NIP-94](/nl/topics/nip-94/) bestandsmetadatastructuur met bestands-URL, originele en getransformeerde SHA-256-hashes, MIME-type, afmetingen en meer:

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

Downloads gebruiken GET-verzoeken naar `<api_url>/<sha256-hash>`, met optionele queryparameters voor serverside transformaties zoals beeldverkleining (`?w=320`). Verwijdering gebruikt DELETE met NIP-98 auth, en alleen de oorspronkelijke uploader kan zijn bestanden verwijderen. Bestandslijstendpoint retourneert gepagineerde resultaten van uploads per gebruiker.

Met kind 10096 events geven gebruikers hun voorkeur-uploadservers aan, zodat clients automatisch de juiste server selecteren zonder handmatige configuratie.

**Reden voor Afkeuring:**

NIP-96 koppelde bestands-URL's aan specifieke servers. Viel `files.example.com` uit, dan verloor elke Nostr-notitie die verwees naar die URL's zijn media. De server was het adres, en dat adres was fragiel.

[Blossom](/nl/topics/blossom/) (Blobs Stored Simply on Mediaservers) keert dat om door de SHA-256-hash van de bestandsinhoud tot canonieke identifier te maken. Blossom-URL's hebben de vorm `https://blossom.example/<sha256>.png`, maar elke Blossom-server die hetzelfde bestand host serveert het op hetzelfde hashpad. Verdwijnt de ene server, dan bevragen clients gewoon andere server voor dezelfde hash. Content addressing maakt gegevens standaard draagbaar over servers.

Blossom vereenvoudigt ook de API. NIP-96 gebruikte multipart form-uploads met JSON-responses en transformatiebeleid, plus discovery-endpoint. Blossom gebruikt plain PUT voor uploads en GET voor downloads, met ondertekende Nostr events (geen HTTP-headers) voor autorisatie. De Blossom-specificatie is opgesplitst in modulaire documenten: BUD-01 behandelt serverprotocol, autorisatie en ophalen, BUD-02 behandelt blob-upload, BUD-03 behandelt servers en BUD-04 behandelt mirroring tussen servers.

De afkeuring vond plaats in september 2025 met [PR #2047](https://github.com/nostr-protocol/nips/pull/2047), die NIP-96 markeerde als "afgeraden" in de NIPs-index.

**Transitie in de Praktijk:**

Servers als nostr.build en void.cat ondersteunden NIP-96 en hebben Blossom-endpoints toegevoegd of zijn ernaar gemigreerd. Angor's v0.2.5-release voegde NIP-96-serverconfiguratie toe voor projectafbeeldingen, terwijl ZSP's v0.3.1-release artefacten exclusief naar Blossom-servers uploadt met `Content-Digest`-headers voor protocolconformiteit. Amethyst en Primal ondersteunen Blossom-uploads. De co-existentie zal waarschijnlijk voortduren totdat de overgebleven NIP-96-implementaties hun migratie voltooien.

**Wat Behouden Blijft:**

Kind 10096 servervoorkeur-events blijven nuttig voor Blossom-serverselectie. NIP-94 bestandsmetadata (kind 1063 events) beschrijft bestandseigenschappen ongeacht welk uploadprotocol ze heeft aangemaakt. De SHA-256-hashing die NIP-96 gebruikte voor download-URL's werd de basis van Blossom's content addressing. NIP-96's ontwerp informeerde wat Blossom vereenvoudigde: de les was dat mediahosting op gedecentraliseerd netwerk content-addressed opslag vereist om te passen bij de censuurbestendigheid van de relay-laag.

---

Dat was het voor deze week. Iets aan het bouwen of nieuws te delen, <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">neem contact op via NIP-17 DM</a> of vind ons op Nostr.
