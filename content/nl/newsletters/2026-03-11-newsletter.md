---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [Shopstr](https://github.com/shopstr-eng/shopstr) en [Milk Market](https://github.com/shopstr-eng/milk-market) voegen MCP-oppervlakken toe voor agentgedreven commerce, terwijl [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) en [strfry](https://github.com/hoytech/strfry) relay-auth en ondersteuning voor beschermde events toevoegen via [NIP-42](/nl/topics/nip-42/) (Authenticatie van clients bij relays) in app-, signer- en relay-software. [Route96](https://github.com/v0l/route96) brengt twee releases uit rond AI-labeling, moderatiequeues, perceptual hashing en machineleesbare serverdocumentatie. [Samizdat](https://github.com/satsdisco/samizdat), al live op het web, bracht zijn eerste Android alpha uit en voegde later signer-ondersteuning toe via [NIP-55](/nl/topics/nip-55/) (Android Signer-applicatie). [Formstr](https://github.com/formstr-hq/nostr-forms) voegt signup via [NIP-49](/nl/topics/nip-49/) (Encryptie van private keys) toe, [Amethyst](https://github.com/vitorpamplona/amethyst) brengt Namecoin-gebaseerd werk voor [NIP-05](/nl/topics/nip-05/) (Domeinverificatie) uit, [Mostro](https://github.com/MostroP2P/mostro) brengt [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4) uit, en het NIPs-repository merge't [NIP-91](/nl/topics/nip-91/) (AND-operator voor filters) plus defensieve richtlijnen voor [NIP-66](/nl/topics/nip-66/) (Relay-ontdekking en liveness-monitoring).

## Nieuws

<a id="shopstr-and-milk-market-open-mcp-commerce-surfaces"></a>
### Shopstr en Milk Market openen MCP-commerce-oppervlakken

[Shopstr](https://github.com/shopstr-eng/shopstr), de peer-to-peer-marketplace met Lightning- en Cashu-betalingen, merge'de [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), waarmee een MCP-server met API-key-authenticatie voor agent-accountbeheer werd toegevoegd. De wijziging voegt `.well-known/agent.json` toe voor agent-discovery, MCP-onboarding- en status-endpoints, routes voor ordercreatie en betalingsverificatie, speciale purchase- en read-tools en een instellingenpagina voor API-keys. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) breidt dit uit met verkopersacties voor berichten, adressen, orderupdates en product-spec-selectie. Een security-fix in [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) vervangt single-iteration SHA-256-hashing van API-keys door salted PBKDF2 met 100.000 iteraties.

Agents kunnen [NIP-99](/nl/topics/nip-99/) (Rubrieksadvertenties)-listings lezen en door de checkout bewegen via de bestaande betaalflows van [NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect) en [NIP-60](/nl/topics/nip-60/) (Cashu Wallet), zonder pagina's te scrapen of clientgedrag te reverse-engineeren.

[Milk Market](https://github.com/shopstr-eng/milk-market), een voedselmarketplace op Nostr via [milk.market](https://milk.market), landde dezelfde MCP- en API-key-basis in [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) voegt abonnementsorders, wijzigingen van verzendadres na aankoop en checkout-afhandeling voor meerdere merchants en meerdere valuta toe voor Stripe en andere fiat-betaalpaden. Een vervolgstap in [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) repareert een bug in de database-initialisatie bij het opstarten waarbij de tabel voor mislukte relay-publicaties op verse installaties niet werd aangemaakt, wat bij de eerste load voor 500-fouten zorgde. De agentgerichte interface werkt met Bitcoin-native checkout op Shopstr of met gemengde fiat- en Bitcoin-checkout op Milk Market.

<a id="nip-42-relay-auth-across-bunker-signer-and-relay"></a>
### NIP-42 relay-auth bij bunker, signer en relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), een [NIP-46](/nl/topics/nip-46/) (Nostr Connect)-bunker die OAuth-providers aan Nostr-signing koppelt, voegde login via [NIP-07](/nl/topics/nip-07/) (Browser Extension Signer), automatische selectie van een enkele identiteit en opschoning voor verwijderde identiteiten toe ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Wanneer er maar een identiteit bestaat, selecteert de bunker die nu automatisch in plaats van een prompt te tonen. Het verwijderen van een identiteit verwijdert nu ook de achtergebleven assignments en verbindingen. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) voegt een configuratiepad `ALWAYS_ALLOWED_KINDS` toe voor toegewezen gebruikers, standaard kind `30078` app-specifieke data, zodat gedelegeerde identiteiten zonder goedkeuring per event naar app-specifieke opslag kunnen schrijven.

[Amber](https://github.com/greenart7c3/Amber), de belangrijkste [NIP-55](/nl/topics/nip-55/) signer voor Android, bracht [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) uit met vier pre-releases in de loop van de week. [PR #317](https://github.com/greenart7c3/Amber/pull/317) voegt relay-auth-afhandeling van [NIP-42](/nl/topics/nip-42/) toe voor verzoeken van kind `22242`. De implementatie voegt een nieuwe databasekolom toe voor relay-specifieke permissies met een unieke index op `(pkKey, type, kind, relay)`. Gebruikers zien een apart auth-scherm waarop ze per relay of voor alle relays tegelijk permissie kunnen geven of weigeren met wildcard-scope `*`, en die keuze kunnen opslaan. Wildcard-permissies verwijderen alle relay-specifieke entries voor een kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) volgt dit op met een refactor van multi-event request-schermen, zodat details inline worden getoond via composable cards in plaats van navigatie naar een apart scherm. De release werkt ook de standaard profielrelays bij, voegt bottom-sheet-weergave van requests toe en repareert een crash op MediaTek-apparaten door StrongBox-keystore uit te schakelen.

Aan de relay-kant implementeert [strfry PR #156](https://github.com/hoytech/strfry/pull/156) NIP-42-auth-afhandeling voor [NIP-70](/nl/topics/nip-70/) (Beschermde events), en [PR #176](https://github.com/hoytech/strfry/pull/176) weigert reposts die beschermde events insluiten.

<a id="notedeck-adds-nip-11-relay-limits-and-agentium-features"></a>
### Notedeck voegt NIP-11 relay-limieten en Agentium-functies toe

[Notedeck](https://github.com/damus-io/notedeck), de native desktopclient van het Damus-team, merge'de deze week 14 PR's. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) voegt het ophalen van relay-limieten uit [NIP-11](/nl/topics/nip-11/) (Relay-informatiedocument) toe, zodat alle outbox-relays nu `max_message_length` en `max_subscriptions` uit het relay-informatiedocument respecteren. De implementatie bevat background-jobverwerking, exponential backoff met jitter voor connection retries en aangepaste HTTP Accept-headers. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) repareert een bug waarbij DM's soms niet wilden laden na accountwisseling, en [PR #1333](https://github.com/damus-io/notedeck/pull/1333) voegt een backoff-mechanisme toe aan multicast-relaycommunicatie om broadcast-spam bij fouten te voorkomen.

Het Agentium-subsysteem (Notedecks ingebouwde coding-agent-UI, intern "Dave" genoemd) kreeg clipboard image paste, benoemde runconfiguraties die tussen apparaten synchroniseren via kind `31991`-events ([NIP-33](/nl/topics/nip-33/) (Geparametriseerde vervangbare events)), een git-worktree-maker en een model picker om backends per sessie te kiezen ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integreert `egui_kittest` voor headless UI-testing, en [PR #1339](https://github.com/damus-io/notedeck/pull/1339) voegt een dashboardkaart toe die nieuwe contactlijstcreaties per client bijhoudt. Een open [PR #1314](https://github.com/damus-io/notedeck/pull/1314) port de Namecoin-NIP-05-resolutie van Amethyst naar Notedeck met ElectrumX-lookups, SOCKS5 Tor-routing en zoekbalkintegratie.

<a id="divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import"></a>
### diVine brengt v1.0.6 uit met E2E-testinfrastructuur en NIP-49-import

[diVine](https://github.com/divinevideo/divine-mobile), de short-form looping-videoclient die Vine-archieven herstelt via [divine.video](https://divine.video), bracht [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) uit met 127 gemerge'de PR's. De release voegt accountimport via [NIP-49](/nl/topics/nip-49/) toe, externe ondersteuning voor [NIP-05](/nl/topics/nip-05/), multi-account-afhandeling, macOS- en experimentele Linux-builds, en een herontworpen bibliotheek voor drafts en clips op basis van lokale opslag.

Aan de engineeringkant voegt [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) een volledige E2E-integratietestinfrastructuur toe met Patrol voor native UI-automatisering tegen een Docker-backendstack (relay, API, Blossom, Postgres, Redis, ClickHouse). Vijf auth-journey-tests dekken registratie, verificatie, wachtwoordreset, sessieverval en tokenrefresh. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) schakelt videoladen om van HLS-first naar directe MP4 met automatische HLS-fallback, waardoor laadtijden dalen van 30-60 seconden naar vrijwel direct. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) cached de API-response van de home feed in SharedPreferences voor directe weergave bij cold start. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) dwingt labels voor `ai-generated` content af als verborgen in feeds, en [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) voegt een veiligheidsinstelling toe om alleen door diVine gehoste video's te tonen. De migratie van Hive naar Drift voor de profielcache gaat verder via [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) en [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), waarbij ongeveer 1.074 regels Hive-code worden vervangen door Drift-DAO's.

<a id="vector-v032-ships-nip-77-negentropy-sync-and-mls-improvements"></a>
### Vector v0.3.2 brengt NIP-77 negentropy-sync en MLS-verbeteringen

[Vector](https://github.com/VectorPrivacy/Vector), een privacygerichte desktopmessenger die MLS-groepsencryptie gebruikt met [NIP-17](/nl/topics/nip-17/) (Privé Directe Berichten) en encryptie uit [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads), bracht [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2) uit. De hoofdfunctie is NIP-77 negentropy voor MLS-groepssync ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), die gemiste berichten veel sneller inhaalt met parallel boot. De release voegt ook een opnieuw opgebouwde audio-engine met volledige Linux-ondersteuning toe, image spoilers met vervaagde previews, klikbare hyperlinks met rich link previews, `@mention`-pings met `@everyone` voor groepsadmins, emoji-shortcode-autocomplete, dempen van groepen, tap-to-react op bestaande reacties en annuleerbare bestandsuploads. Vector filtert expliciet groepschatevents van NIP-17 eruit ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), en gebruikt MLS exclusief voor groepsencryptie.

## Releases

<a id="route96-v050-and-v051"></a>
### Route96 v0.5.0 en v0.5.1

[Route96](https://github.com/v0l/route96), een mediaserver die Blossom en [NIP-96](/nl/topics/nip-96/) (HTTP File Storage) ondersteunt, bracht [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) en [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1) uit. v0.5.0 voegt geautomatiseerde AI-labeling toe, retroactieve backfill voor niet-gelabelde uploads, moderatiequeues voor gemarkeerde bestanden, op EXIF gebaseerde privacyweigering en afhandeling van gebande hashes.

v0.5.1 voegt perceptual image hashes toe, locality-sensitive hashing voor het opzoeken van vergelijkbare afbeeldingen, batch-admin-endpoints en een gepubliceerde [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) die het Blossom- en NIP-96-API-oppervlak van de server beschrijft voor agent-tooling. [PR #58](https://github.com/v0l/route96/pull/58) verplaatst background workers naar volledig asynchrone Tokio-taken, en [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) voegt backoff toe om hot loops te vermijden.

<a id="samizdat-v100-alpha"></a>
### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), een long-form-reader en publisher beschikbaar via [samizdat.press](https://samizdat.press), bracht zijn eerste Android-build uit in [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). De app opent op een gecureerde Press-pagina met lange Nostr-artikelen en bottom-tab-navigatie tussen Press-, Feed-, Saved- en Write-weergaven. De Android-build voegt native key-opslag toe via versleuteling met Android Keystore en biometrische ontgrendeling, verwerkt `nostr:`-URI's en deep links van `samizdat.press`, en ondersteunt signer-handoff via de Android app chooser (Amber, Primal enzovoort) in plaats van directe key-import. Pull-to-refresh, safe-area-afhandeling op verschillende schermgroottes en native integraties voor delen, klembord, haptics en splash screen maken nu deel uit van de Android-shell in plaats van van de webwrapper.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) voegt intent-gebaseerde [NIP-55](/nl/topics/nip-55/)-signing toe voor Amber- en Primal-flows, en [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) vervangt een JavaScript-bridge-workaround door een native Capacitor-plugin met `startActivityForResult`. De app vereist Android 7.0+ (API 24), wordt in deze alpha als debug-APK uitgebracht en mist nog steeds pushnotificaties. Publiceren hangt momenteel af van een signer-app, terwijl login met `nsec` lokaal lezen en accounttoegang dekt.

<a id="calendar-by-form-v020"></a>
### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), een gedecentraliseerde kalenderapp met private eventdeling via [NIP-59](/nl/topics/nip-59/) (Gift Wrap) beschikbaar op [calendar.formstr.app](https://calendar.formstr.app), bracht [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) uit met [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). De release breidt de afhandeling van terugkerende events voor [NIP-52](/nl/topics/nip-52/) (Calendar Events) uit en gaat daarmee verder dan de single-event-basis van v0.1.0. De onderliggende wijzigingen raken ook lokale eventopslag, signer-afhandeling en Android-notificatieplumbing. Dit is de tweede actieve applicatie van de Formstr-organisatie na de repositoriemigratie van vorige maand.

<a id="mostro-v0164"></a>
### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), de peer-to-peer-Bitcoinbeurs gebouwd op Nostr, bracht [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4) uit. De fixes voor herstel van disputesessies ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) en automatisch sluiten ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) die [vorige week werden behandeld](/nl/newsletters/2026-03-04-newsletter/) zitten hierin. Nieuw in deze release: [PR #625](https://github.com/MostroP2P/mostro/pull/625) voegt een veld `days` toe aan user-rating-events van kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) voegt expiratie toe aan die rating-events, en [PR #614](https://github.com/MostroP2P/mostro/pull/614) laat order-events verlopen volgens geconfigureerde instellingen in plaats van een hardcoded venster van 24 uur. [PR #622](https://github.com/MostroP2P/mostro/pull/622) voegt een idempotency-check toe om dubbele betalingen van development fees te voorkomen.

<a id="mostro-mobile-v121"></a>
### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), de Flutter-client voor de Mostro P2P-beurs, bracht [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) uit met 11 nieuwe functies en 11 bugfixes. De release voegt rendering van versleutelde multimedia toe in dispute-chat ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), automatisch sluiten van de dispute-UI wanneer orders een terminale status bereiken ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), QR-scannen voor NWC-walletimport ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), Franse vertalingen en FCM-pushnotificatieafhandeling. [PR #496](https://github.com/MostroP2P/mobile/pull/496) repareert een Schnorr-signature-paddingbug door de afhankelijkheid bip340 vast te pinnen op v0.2.0.

<a id="0xchat-v154"></a>
### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), de Telegram-achtige messagingclient met Cashu-ondersteuning, bracht [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) uit met focus op fixes voor Linux-desktop: AppImage-dockicons, emoji-rendering, freezes in contextmenu's en vastlopers in reply/copy-UI. De release repareert ook problemen met image-upload en npub.cash-integratie. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) elimineert onnodige UI-rebuilds door een pollingtimer van 3 seconden te verwijderen die niets deed behalve glassmorphic repaints forceren, en deblokkeert login-initialisatie door het laden van de eventcache gelijktijdig uit te voeren in plaats van relay-, contact- en channel-opstart te blokkeren.

<a id="keep-v060"></a>
### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), een FROST-threshold-signer voor Android met ondersteuning voor [NIP-55](/nl/topics/nip-55/) en [NIP-46](/nl/topics/nip-46/), bracht [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) en [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1) uit. v0.6.0 voegt coördinatie van wallet descriptors en beheer-UI toe, een back-up- en herstel-flow met biometrische authenticatie ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), `nsec`-herstel vanuit threshold shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), cross-platform generatie van geanimeerde QR-frames via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)) en een signing-audit trail met chain verification ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). v0.6.1 verandert de licentie van AGPL-3.0 naar MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

<a id="njump-v030"></a>
### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), de statische gateway om Nostr-content te bekijken via [njump.me](https://njump.me), bracht [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) uit met een brekende wijziging in de parsing van `note1`-codes en een update van de onderliggende nostr-bibliotheek.

<a id="roadstr-v011"></a>
### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), een gedecentraliseerde app voor meldingen van verkeersevenementen die Nostr gebruikt, bracht zijn eerste demo-release [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1) uit. De app toont weggebeurtenissen op een kaart met vector tiles van openfreemap.org.

<a id="bitcredit-v053"></a>
### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), een e-bill-applicatie met een Nostr-transportlaag en een eigen relay op [bit.cr](https://www.bit.cr/), bracht [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3) uit. [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) voegt velden `payment_actions` en `bill_state` toe aan de API voor betaal- en acceptatiestatus, en [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) repareert de afhandeling van signing-adressen voor anonieme signers.

<a id="openchat-v010-alpha3"></a>
### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), een chatapplicatie gebouwd op de .NET MLS- en C#-bibliotheken van het Marmot-protocol, bracht [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3) uit. De release voegt ondersteuning voor externe signers toe voor Amber- en [NIP-46](/nl/topics/nip-46/)-flows ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), verplaatst MLS-statuspersistentie naar de MLS-service om dataverlies in crashvensters te elimineren ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), en publiceert Windows-, Linux- en Android-builds via een nieuwe CI-pipeline.

<a id="opensignal-v100"></a>
### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), een Kotlin Multiplatform-trading-copilot voor Nostr, bracht [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0) uit. De release verpakt gedeelde KMP-modules voor domeinlogica, chart-rendering, Nostr-authenticatie en publicatie, Blossom-[NIP-96](/nl/topics/nip-96/)-uploadondersteuning en ONNX-gebaseerde AI-inference-hooks over Desktop- en Android-shells. De gepubliceerde architectuur bevat ook een FastAPI-AI-service voor analyse van chart-screenshots, modeltrainingspipelines en een risk engine die gestructureerde trade plans met sizing en waarschuwingen produceert. Login ondersteunt zowel ruwe `nsec`-keys als externe signers, en de outputflow eindigt in publicatie van Nostr-events in plaats van in lokale-only analyse.

## Projectupdates

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), het Google Forms-alternatief op Nostr, merge'de [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), die een signup-flow toevoegt met versleutelde private keys via [NIP-49](/nl/topics/nip-49/) (Encryptie van private keys). Voor deze wijziging hadden gebruikers ofwel een [NIP-07](/nl/topics/nip-07/) browserextensie nodig of een ruwe `nsec`-paste om Formstr te gebruiken. De nieuwe flow genereert client-side een key pair, versleutelt de private key met een door de gebruiker gekozen wachtwoord via het scrypt + XChaCha20-Poly1305-schema van NIP-49, en slaat de resulterende `ncryptsec`-string op. Gebruikers kunnen daarna opnieuw inloggen met hun wachtwoord zonder een signer-extensie te installeren. Key management blijft de hele tijd client-side.

<a id="amethyst"></a>
### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), de functierijke Android-client, merge'de vier PR's die het op Namecoin gebaseerde resolutiewerk voor [NIP-05](/nl/topics/nip-05/) opleveren dat [vorige week nog open stond](/nl/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) voegt censuurbestendige NIP-05-verificatie toe via ElectrumX voor `.bit`-, `d/`- en `id/`-identifiers. Wanneer Amethyst een van deze suffixen detecteert in een NIP-05-veld, vraagt het een ElectrumX-NMC-server om de transacties van de naamgeschiedenis, parse't het `NAME_UPDATE`-script uit de nieuwste output om de Nostr-pubkey te extraheren, en weigert het namen ouder dan 36.000 blokken, het vervalvenster van Namecoin. ElectrumX-verbindingen lopen via SOCKS5 wanneer Tor is ingeschakeld, met dynamische serverselectie tussen clearnet- en `.onion`-endpoints. Een LRU-cache met een TTL van een uur voorkomt herhaalde blockchainqueries.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) repareert racecondities en de correctheid van de resolver in die flow. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) laat nieuwe gebruikers tijdens signup een follow-lijst importeren uit gewone NIP-05-identifiers of Namecoin-ondersteunde identifiers. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) voegt aangepaste instellingen voor ElectrumX-servers toe, zodat gebruikers kunnen kiezen welke server hun lookups afhandelt.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), een bibliotheek met helpermethoden om Nostr-events in IndexedDB op te slaan, merge'de [PR #6](https://github.com/hzrd149/nostr-idb/pull/6), die ondersteuning toevoegt voor AND-tagfilters uit [NIP-91](/nl/topics/nip-91/). De wijziging voegt intersection-semantiek toe aan client-side filter matching, zodat IndexedDB-queries alle opgegeven tagwaarden kunnen vereisen in plaats van willekeurig een ervan. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) werkt de bibliotheek bij naar de nieuwste interface van NIP-DB, en een vervolgende [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) repareert een subscribe-deadlock en verwijdert nostr-tools als production dependency.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), een archive-first Nostr-indexer met ClickHouse-analytics, merge'de [PR #8](https://github.com/andotherstuff/pensieve/pull/8), die handhaving van per-entry cache-TTL en per-key miss-coalescing toevoegt om CPU-spikes in de API te verminderen. De duurste time-series-endpoints, engagement stats, hourly activity en per-kind activity, gebruiken nu server-side TTL's van 10 minuten in plaats van gesynchroniseerde recompute-stormen te triggeren.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), het gedecentraliseerde media-hostingprotocol en de serverstack, merge'de twee BUD-11-updates voor autorisatie. [PR #91](https://github.com/hzrd149/blossom/pull/91) verplaatst optionele autorisatie naar een eigen BUD en verduidelijkt de rol van de tags `x` en `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) ruimt endpoint-specifiek auth-gedrag op en formaliseert de header `X-SHA-256` voor uploadverificatie. Samen consolideren de twee PR's auth-logica in BUD-11 en verwijderen ze onduidelijkheden rond request hashing voor upload-, delete- en media-management-flows.

<a id="nip-updates"></a>
## NIP-updates

Recente wijzigingen in het [NIPs-repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-91](/nl/topics/nip-91/) (AND-operator voor filters)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): voegt intersection-semantiek toe voor tagfilters, zodat relays queries kunnen beantwoorden die alle opgegeven tagwaarden vereisen in plaats van een enkele ervan. Dat vermindert client-side post-filtering en bandbreedte bij tag-zware queries.

- **[NIP-66](/nl/topics/nip-66/) (Relay-ontdekking en liveness-monitoring): Defensive Measures** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): na het [outbox-benchmarkwerk van vorige week](/nl/newsletters/2026-03-04-newsletter/), voegt de specificatie nu waarschuwingen toe voor unhappy paths in relay-monitoringdata. Clients mogen monitoring-events van kind `30166` niet vereisen om te functioneren. Een monitor kan het mis hebben, verouderd zijn of kwaadaardig handelen. Van clients wordt verwacht dat ze bronnen kruiselings controleren en niet grote delen van iemands relaygrafiek afsnijden op basis van een enkele feed.

- **[NIP-39](/nl/topics/nip-39/) (Externe identiteiten in profielen): opschoning van het kind-10011-register** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): voegt de verwijzing naar kind `10011` direct toe aan de specificatie, in lijn met de implementatie van Amethyst die [vorige week werd behandeld](/nl/newsletters/2026-03-04-newsletter/).

**Open PR's en discussies:**

- **[NIP-70](/nl/topics/nip-70/) (Beschermde events): reposts weigeren die beschermde events insluiten** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): als een relay NIP-70 afdwingt op het oorspronkelijke event maar reposts met dezelfde inhoud accepteert, heeft de `-` tag in de praktijk geen effect. Deze PR voegt de regel toe dat relays ook reposts van kind 6 en kind 16 van beschermde events moeten weigeren. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) implementeert dit al.

- **[NIP-71](/nl/topics/nip-71/) (Video-events): meerdere audiotracks** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): voegt `imeta`-audiotags toe voor alternatieve tracks, taalvarianten en audio-only streams. Een client zou een stabiel videobestand kunnen behouden terwijl tussen audiotalen wordt gewisseld, of audio als apart spoor kunnen aanbieden voor podcastachtig materiaal.

- **[NIP-11](/nl/topics/nip-11/) (Relay-informatiedocument) en [NIP-66](/nl/topics/nip-66/) relay-attributen** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): voegt een gestructureerd veld `attributes` toe aan relay-informatiedocumenten, waardoor clients en discovery-tools machineleesbare metadata krijgen naast de huidige vrije-tekstbeschrijving.

<a id="nip-deep-dive-nip-49-private-key-encryption"></a>
## NIP-verdieping: NIP-49 (Encryptie van private keys)

[NIP-49](/nl/topics/nip-49/) definieert hoe een client een private key met een wachtwoord versleutelt en het resultaat codeert als een bech32-`ncryptsec`-string. [Formstr](#formstr) gebruikt NIP-49 in zijn nieuwe signup-flow.

Het formaat is niet gekoppeld aan een apart event kind. Een client begint met de ruwe secp256k1 private key van 32 bytes, leidt met scrypt een symmetrische sleutel af uit het wachtwoord van de gebruiker, versleutelt de key met XChaCha20-Poly1305 en verpakt het resultaat dan in een bech32-`ncryptsec`-string. Een flag van een byte legt vast of bekend is dat de key ooit onveilig is behandeld voordat de encryptie plaatsvond.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Het JSON-event hierboven is een voorbeeld op applicatieniveau, geen vereiste van NIP-49. De NIP standaardiseert het formaat van de versleutelde key. Een client kan de `ncryptsec` lokaal opslaan, via app-specifieke opslag synchroniseren of als back-upstring exporteren. Wachtwoorden worden naar Unicode NFKC genormaliseerd voordat keys worden afgeleid, zodat hetzelfde wachtwoord op clients en platforms consistent kan ontsleutelen.

De byte voor key-security kent drie gedefinieerde waarden: `0x00` betekent dat de afhandelingsgeschiedenis van de key onbekend is, `0x01` betekent dat bekend is dat de key onveilig is behandeld, bijvoorbeeld als plaintext geplakt in een webformulier voor de encryptie, en `0x02` betekent dat de key in een veilige context is gegenereerd en versleuteld en nooit is blootgesteld. Clients kunnen dit gebruiken om waarschuwingen te tonen wanneer keys met een bekende onveilige geschiedenis worden geimporteerd.

NIP-49 beschermt keys beter dan een plain `nsec`-export, maar de encryptie is slechts zo sterk als het wachtwoord en de geconfigureerde scrypt-cost. Hogere `LOG_N`-waarden maken offline gokken moeilijker, maar vertragen ook legitieme decrypt-operaties. De specificatie waarschuwt tegen het publiceren van versleutelde keys op publieke relays, omdat aanvallers profiteren van het verzamelen van ciphertext voor offline cracking. Ter vergelijking: remote signing via [NIP-46](/nl/topics/nip-46/) voorkomt dat keys uberhaupt worden blootgesteld, en Android-signing via [NIP-55](/nl/topics/nip-55/) houdt keys binnen een aparte signer-app. NIP-49 vult een andere rol: draagbare versleutelde back-up voor gebruikers die hun eigen keys beheren.

Implementaties omvatten [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) voor signup, [Amber](https://github.com/greenart7c3/Amber) voor ncryptsec-back-up en herstel, [diVine v1.0.6](#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import) voor accountimport, [Keep v0.6.0](#keep-v060) voor FROST-share-export en key-management-tools als [nsec.app](https://nsec.app) en [Alby](https://github.com/getAlby/hub).

<a id="nip-deep-dive-nip-70-protected-events"></a>
## NIP-verdieping: NIP-70 (Beschermde events)

[NIP-70](/nl/topics/nip-70/) definieert beschermde events. Wanneer een event de tag `[["-"]]` draagt, moet een relay het weigeren tenzij de relay authenticatie via [NIP-42](/nl/topics/nip-42/) vereist en de geauthenticeerde pubkey overeenkomt met de auteur van het event.

De NIP-42-auth-flow werkt als volgt: de relay stuurt een `AUTH`-challenge met een willekeurige string, en de client reageert met een ondertekend event van kind `22242` waarvan de tags de relay-URL en de challenge bevatten. De relay verifieert de handtekening en controleert dat de pubkey in het auth-event overeenkomt met de pubkey in het protected event dat wordt gepubliceerd. Als de pubkeys niet overeenkomen, weigert de relay het event met een berichtprefix `restricted`.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

De inhoud van het event kan nog steeds publiek zijn. De tag `-` bepaalt alleen wie het event naar een relay mag publiceren die de tag respecteert. Dit dekt semi-gesloten feeds van [NIP-29](/nl/topics/nip-29/) (Relay-gebaseerde groepen), relayruimtes alleen voor leden en andere contexten waarin de auteur herdistributie via de relaygrafiek wil beperken. NIP-70 is een conventie van een enkele tag, geen nieuw event kind, dus elk bestaand event kind kan de `-` tag dragen.

Zelfs als een relay publicatie door derden van het oorspronkelijke event blokkeert, kan iemand de inhoud nog steeds in een repost herpubliceren. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) pakt dit aan door te eisen dat relays ook reposts van kind 6 en kind 16 van beschermde events weigeren. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) voegt NIP-42-auth-afhandeling toe voor beschermde events, en [strfry PR #176](https://github.com/hoytech/strfry/pull/176) blokkeert reposts die beschermde inhoud insluiten.

NIP-70 stuurt relaygedrag aan. Een ontvanger kan de inhoud nog steeds elders kopieren, en de specificatie zegt dat ook expliciet. De tag `-` geeft relays een machineleesbaar signaal om republicatie te weigeren. Ter vergelijking: [NIP-62](/nl/topics/nip-62/) (Vanish Requests) vraagt relays om data achteraf te verwijderen, terwijl NIP-70 ongeautoriseerde publicatie voorkomt op het moment van ingest. De twee vullen elkaar aan: een auteur kan events als protected markeren om verspreiding te beperken, en later verwijdering vragen als de inhoud ook van relays moet verdwijnen die het event wel accepteerden.

---

Dat is het voor deze week. Ben je iets aan het bouwen of heb je nieuws om te delen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via [NIP-17](/nl/topics/nip-17/) DM</a> of vind ons op Nostr.
