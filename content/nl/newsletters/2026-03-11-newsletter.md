---
title: 'Nostr Kompas #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Welkom terug bij Nostr Kompas, je wekelijkse gids voor Nostr.

**Deze week:** [Shopstr](https://github.com/shopstr-eng/shopstr) en [Milk Market](https://github.com/shopstr-eng/milk-market) voegen MCP-oppervlakken toe voor agentgestuurde handel, terwijl [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) en [strfry](https://github.com/hoytech/strfry) relay-auth en protected-event-support voor [NIP-42](/nl/topics/nip-42/) (Authenticatie van clients bij relays) toevoegen in app-, signer- en relaysoftware. [Route96](https://github.com/v0l/route96) brengt twee releases uit rond AI-labeling, moderatiequeues, perceptuele hashing en machineleesbare serverdocumentatie. [Samizdat](https://github.com/satsdisco/samizdat), al live op het web, bracht zijn eerste Android-alpha uit en voegde later signer-support voor [NIP-55](/nl/topics/nip-55/) (Android Signer Application) toe. [Formstr](https://github.com/formstr-hq/nostr-forms) voegt signup toe via [NIP-49](/nl/topics/nip-49/) (Private Key Encryption), [Amethyst](https://github.com/vitorpamplona/amethyst) brengt Namecoin-gebaseerde [NIP-05](/nl/topics/nip-05/) (Domain Verification) resolutie uit, [Mostro](https://github.com/MostroP2P/mostro) brengt [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4) uit, en de NIPs-repository merged [NIP-91](/nl/topics/nip-91/) (AND Operator for Filters) en defensieve richtlijnen voor [NIP-66](/nl/topics/nip-66/) (Relay Discovery and Liveness Monitoring).

## Nieuws

### Shopstr en Milk Market openen MCP-oppervlakken voor handel

[Shopstr](https://github.com/shopstr-eng/shopstr), de peer-to-peer marktplaats met Lightning- en Cashu-betalingen, mergeerde [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), waarmee een MCP-server met API-key-authenticatie voor agent accountbeheer werd toegevoegd. De wijziging voegt `.well-known/agent.json` toe voor agent discovery, MCP-endpoints voor onboarding en status, routes voor ordercreatie en betaalverificatie, en aparte purchase- en read-tools plus een instellingenpagina voor API-sleutels. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) breidt dit uit met verkopersacties voor berichten, adressen, orderupdates en productspecificaties. Een securityfix in [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) vervangt single-iteration SHA-256 hashing van API-sleutels door salted PBKDF2 met 100.000 iteraties.

Agents kunnen [NIP-99](/nl/topics/nip-99/) (Classified Listings)-vermeldingen lezen en het checkoutproces doorlopen via de bestaande betaalstromen van [NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect) en [NIP-60](/nl/topics/nip-60/) (Cashu Wallet), zonder pagina's te scrapen of clientgedrag te reverse-engineeren.

[Milk Market](https://github.com/shopstr-eng/milk-market), een voedselmarktplaats op Nostr via [milk.market](https://milk.market), kreeg dezelfde MCP- en API-key-basis in [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) voegt abonnementsorders toe, wijzigingen aan verzendadressen na aankoop en afhandeling van multi-merchant- en multi-currency-checkout voor Stripe en andere fiat-betaalpaden. Een vervolgwijziging in [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) repareert een bug bij database-initialisatie tijdens opstarten, waarbij de tabel voor mislukte relay-publicaties op verse installaties niet werd aangemaakt en daardoor 500-fouten op de eerste load ontstonden. De agentgerichte interface werkt zowel met Bitcoin-native checkout op Shopstr als met gemengde fiat- en Bitcoin-checkout op Milk Market.

### NIP-42 relay-auth bij bunker, signer en relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), een [NIP-46](/nl/topics/nip-46/) (Nostr Connect)-bunker die OAuth-providers koppelt aan Nostr-signing, voegde login via [NIP-07](/nl/topics/nip-07/) (Browser Extension Signer), automatische selectie van een enkele identiteit en opruiming van verwijderde identiteiten toe ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Wanneer er maar een identiteit bestaat, kiest de bunker die nu automatisch in plaats van de gebruiker eerst te laten kiezen. Het verwijderen van een identiteit verwijdert ook achterblijvende assignments en connections. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) voegt een configuratiepad `ALWAYS_ALLOWED_KINDS` toe voor toegewezen gebruikers, met kind `30078` app-specific data als standaard, zodat gedelegeerde identiteiten zonder goedkeuring per event naar app-specifieke opslag kunnen schrijven.

[Amber](https://github.com/greenart7c3/Amber), de belangrijkste [NIP-55](/nl/topics/nip-55/) signer voor Android, bracht [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) uit na vier prereleases in de loop van de week. [PR #317](https://github.com/greenart7c3/Amber/pull/317) voegt relay-authenticatie volgens [NIP-42](/nl/topics/nip-42/) toe voor verzoeken van kind `22242`. De implementatie voegt een nieuwe databasekolom toe voor relay-specifieke permissies met een unieke index op `(pkKey, type, kind, relay)`. Gebruikers krijgen een apart auth-scherm waar ze per relay of voor alle relays via wildcard `*` toestemming kunnen geven of weigeren, en die keuze kunnen bewaren. Wildcard-permissies verwijderen alle relay-specifieke entries voor dat kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) bouwt daarop voort door schermen voor multi-event-verzoeken te refactoren, zodat details inline in composable kaarten worden getoond in plaats van op een apart scherm. De release werkt ook standaard profiellists bij, voegt bottom-sheet-weergave voor verzoeken toe en repareert een crash op MediaTek-apparaten door StrongBox keystore uit te schakelen.

Aan relay-zijde implementeert [strfry PR #156](https://github.com/hoytech/strfry/pull/156) NIP-42-auth voor [NIP-70](/nl/topics/nip-70/) (Protected Events), en [PR #176](https://github.com/hoytech/strfry/pull/176) weigert reposts die protected events insluiten.

### Notedeck voegt NIP-11 relay-limieten en Agentium-features toe

[Notedeck](https://github.com/damus-io/notedeck), de native desktopclient van het Damus-team, mergeerde deze week 14 PR's. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) voegt relay-limietophaling toe uit [NIP-11](/nl/topics/nip-11/) (Relay Information Document), zodat alle outbox-relays nu `max_message_length` en `max_subscriptions` uit het relay-infodocument respecteren. De implementatie bevat verwerking via achtergrondjobs, exponential backoff met jitter voor verbindingsherstel en aangepaste HTTP Accept-headers. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) repareert een bug waarbij DM's soms niet laadden na het wisselen van account, en [PR #1333](https://github.com/damus-io/notedeck/pull/1333) voegt een backoff-mechanisme toe aan multicast-communicatie met relays om broadcastspam bij fouten te voorkomen.

Het Agentium-subsysteem, de ingebouwde coding-agent-UI van Notedeck die intern "Dave" heet, kreeg ondersteuning voor het plakken van clipboard-afbeeldingen, benoemde run-configuraties die via kind `31991` events tussen apparaten synchroniseren ([NIP-33](/nl/topics/nip-33/) Parameterized Replaceable Events), een git-worktree-creator en een model picker voor het kiezen van backends per sessie ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integreert `egui_kittest` voor headless UI-tests, en [PR #1339](https://github.com/damus-io/notedeck/pull/1339) voegt een dashboardkaart toe die nieuwe creaties van contactlijsten per client volgt. Een openstaande [PR #1314](https://github.com/damus-io/notedeck/pull/1314) porteert Amethysts Namecoin-gebaseerde NIP-05-resolutie naar Notedeck met ElectrumX-lookups, SOCKS5-Tor-routing en integratie in de zoekbalk.

### diVine brengt v1.0.6 uit met E2E-testinfrastructuur en NIP-49-import {#divine-v106-met-e2e-testinfrastructuur-en-nip-49-import}

[diVine](https://github.com/divinevideo/divine-mobile), de short-form looping-videoclient die Vine-archieven terugbrengt op [divine.video](https://divine.video), bracht [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) uit met 127 gemergede PR's. De release voegt accountimport via [NIP-49](/nl/topics/nip-49/), externe [NIP-05](/nl/topics/nip-05/)-ondersteuning, multi-accountbeheer en macOS- plus experimentele Linux-builds toe, samen met een opnieuw ontworpen bibliotheek voor drafts en clips die op lokale opslag steunt.

Aan de engineeringkant voegt [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) een volledige E2E-integratietestinfrastructuur toe met Patrol voor native UI-automatisering tegen een Docker-backendstack met relay, API, Blossom, Postgres, Redis en ClickHouse. Vijf tests van auth-trajecten dekken registratie, verificatie, wachtwoordreset, sessieverval en token refresh. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) schakelt videoladen om van HLS-first naar direct MP4 met automatische HLS-fallback, waardoor laadtijden van 30-60 seconden naar vrijwel direct dalen. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) cached de API-respons van de homefeed in SharedPreferences voor een directe weergave na een cold start. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) dwingt labels voor `ai-generated` content af als verborgen in feeds, en [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) voegt een veiligheidsinstelling toe om alleen door diVine gehoste video's te tonen. De migratie van Hive naar Drift voor de profielcache loopt verder via [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) en [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), waarmee ongeveer 1.074 regels Hive-code worden vervangen door Drift DAO's.

### Vector v0.3.2 brengt NIP-77-negentropy-sync en MLS-verbeteringen

[Vector](https://github.com/VectorPrivacy/Vector), een privacygerichte desktopmessenger die MLS-groepsversleuteling gebruikt met [NIP-17](/nl/topics/nip-17/) (Private Direct Messages) en [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads), bracht [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2) uit. De belangrijkste wijziging is NIP-77-negentropy voor MLS-groepssynchronisatie ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), waarmee gemiste berichten via parallel boot veel sneller worden ingehaald. De release voegt ook een opnieuw gebouwde audio-engine met volledige Linux-ondersteuning toe, image spoilers met vervaagde previews, klikbare hyperlinks met rich link previews, `@mention`-pings met `@everyone` voor groepsadmins, emoji-shortcode-autocomplete, group muting, tik-om-te-reageren op bestaande reacties en annuleerbare bestandsuploads. Vector filtert expliciet groepschat-events van NIP-17 uit ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)) en gebruikt MLS exclusief voor groepsversleuteling.

## Releases

### Route96 v0.5.0 en v0.5.1

[Route96](https://github.com/v0l/route96), een mediaserver met ondersteuning voor Blossom en [NIP-96](/nl/topics/nip-96/) (HTTP File Storage), bracht [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) en [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1) uit. v0.5.0 voegt geautomatiseerde AI-labeling toe, retroactieve backfill voor ongelabelde uploads, moderatiequeues voor gemarkeerde bestanden, privacy-afwijzing op basis van EXIF en verwerking van verboden hashes.

v0.5.1 voegt perceptuele image hashes, locality-sensitive hashing voor vergelijkbare afbeeldingen, batch-admin-endpoints en een gepubliceerde [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) toe die het Blossom- en NIP-96-API-oppervlak van de server beschrijft voor agent tooling. [PR #58](https://github.com/v0l/route96/pull/58) verplaatst achtergrondworkers naar volledig asynchrone Tokio-taken, en [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) voegt backoff toe om hot loops te vermijden.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), een reader en uitgever voor long-form content op [samizdat.press](https://samizdat.press), bracht zijn eerste Android-build uit in [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). De app opent met een gecureerde Press-pagina van lange Nostr-artikelen en biedt navigatie onderin tussen Press, Feed, Saved en Write. De Android-build voegt native key storage toe via Android Keystore-versleuteling met biometrische ontgrendeling, ondersteunt `nostr:`-URI's en `samizdat.press`-deeplinks, en ondersteunt signer-handoff via de Android-appkiezer zoals Amber en Primal, in plaats van directe sleutelimport te vereisen. Pull-to-refresh, safe-area-afhandeling op verschillende schermformaten en integratie van native share, clipboard, haptics en splash screen zitten nu in de Android-shell in plaats van de webwrapper.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) voegt intent-gebaseerde [NIP-55](/nl/topics/nip-55/)-signing toe voor Amber- en Primal-flows, en [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) vervangt een JavaScript-bridge-workaround door een native Capacitor-plugin met `startActivityForResult`. De app vereist Android 7.0+ (API 24), wordt in deze alpha als debug-APK geleverd en mist nog pushnotificaties. Publiceren hangt momenteel af van een signer-app, terwijl inloggen met `nsec` lokaal lezen en accounttoegang afdekt.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), een gedecentraliseerde kalenderapp met private eventdeling via [NIP-59](/nl/topics/nip-59/) (Gift Wrap) op [calendar.formstr.app](https://calendar.formstr.app), bracht [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) uit samen met [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). De release breidt de afhandeling van terugkerende events voor [NIP-52](/nl/topics/nip-52/) (Calendar Events) uit, boven op de basis met enkelvoudige events uit v0.1.0. De onderliggende wijzigingen raken ook lokale eventopslag, signer-afhandeling en Android-notificatieplumbing. Dit is de tweede actieve applicatie van de Formstr-organisatie sinds de repositorymigratie van vorige maand.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), de peer-to-peer Bitcoin-exchange gebouwd op Nostr, bracht [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4) uit. De fixes voor herstel van disputessessies ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) en automatisch sluiten ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) die [vorige week](/nl/newsletters/2026-03-04-newsletter/) aan bod kwamen, zitten in deze release. Nieuw in deze versie: [PR #625](https://github.com/MostroP2P/mostro/pull/625) voegt een `days`-veld toe aan rating-events van kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) voegt een verloopdatum toe aan diezelfde rating-events, en [PR #614](https://github.com/MostroP2P/mostro/pull/614) laat order-events verlopen op basis van geconfigureerde instellingen in plaats van een hardcoded venster van 24 uur. [PR #622](https://github.com/MostroP2P/mostro/pull/622) voegt een idempotency-check toe om dubbele betalingen van ontwikkelingsfees te voorkomen.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), de Flutter-client voor de Mostro P2P-exchange, bracht [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) uit met 11 nieuwe features en 11 bugfixes. De release voegt rendering van versleutelde multimedia in dispute chat toe ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), sluit de dispute-UI automatisch wanneer orders een eindstatus bereiken ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), voegt QR-scanning toe voor import van NWC-wallets ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), plus Franse vertalingen en FCM-pushnotificaties. [PR #496](https://github.com/MostroP2P/mobile/pull/496) repareert een paddingbug in Schnorr-handtekeningen door de dependency `bip340` vast te pinnen op v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), de Telegram-achtige berichtenclient met Cashu-support, bracht [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) uit met focus op Linux-desktopfixes: AppImage-dockicons, emoji-rendering, vastlopende contextmenu's en reply/copy-hangs in de UI. De release repareert ook problemen met image uploads en npub.cash-integratie. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) verwijdert onnodige UI-rebuilds door een polling-timer van 3 seconden te schrappen die niets deed behalve glassmorphic hertekeningen forceren, en maakt login-initialisatie weer niet-blokkerend door het laden van de eventcache parallel te laten lopen met relay-, contact- en channel-opstart.

### Keep v0.6.0 {#keep-v060}

[Keep](https://github.com/privkeyio/keep-android), een FROST-threshold-signer voor Android met support voor [NIP-55](/nl/topics/nip-55/) en [NIP-46](/nl/topics/nip-46/), bracht [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) en [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1) uit. v0.6.0 voegt coördinatie en beheer-UI voor wallet descriptors toe, een backup/restore-flow met biometrische authenticatie ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), `nsec`-herstel uit threshold shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), cross-platform geanimeerde QR-frames via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)) en een audit trail voor signing met ketenverificatie ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). v0.6.1 wijzigt de licentie van AGPL-3.0 naar MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), de statische gateway voor het bekijken van Nostr-content via [njump.me](https://njump.me), bracht [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) uit met een brekende wijziging in parsing van `note1`-codes en een update van de onderliggende nostr-bibliotheek.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), een gedecentraliseerde app voor meldingen over wegincidenten via Nostr, bracht zijn eerste demo-release [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1) uit. De app toont wegincidenten op een kaart met vector tiles van openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), een e-bill-applicatie met een Nostr-transportlaag en relay via [bit.cr](https://www.bit.cr/), bracht [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3) uit. [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) voegt `payment_actions`- en `bill_state`-velden toe aan de API voor betaal- en acceptatiestatus, en [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) repareert de afhandeling van signing-adressen voor anonieme signers.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), een chatapplicatie gebouwd op de .NET MLS- en C#-bibliotheken van het Marmot-protocol, bracht [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3) uit. De release voegt externe signer-support toe voor Amber- en [NIP-46](/nl/topics/nip-46/)-flows ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), verplaatst MLS-state-persistentie naar de MLS-service om dataverlies in crashvensters te voorkomen ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), en publiceert Windows-, Linux- en Android-builds via een nieuwe CI-pijplijn.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), een Kotlin Multiplatform trading copilot voor Nostr, bracht [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0) uit. De release verpakt gedeelde KMP-modules voor domeinlogica, chart rendering, Nostr-authenticatie en publicatie, Blossom [NIP-96](/nl/topics/nip-96/) upload-support en ONNX-gebaseerde AI-inference-hooks voor Desktop- en Android-shells. De gepubliceerde architectuur bevat ook een FastAPI AI-service voor analyse van chart screenshots, pijplijnen voor modeltraining en een risk engine die gestructureerde trade plans met sizing en waarschuwingen oplevert. Inloggen ondersteunt zowel ruwe `nsec`-sleutels als externe signers, en de outputflow eindigt in Nostr-eventpublicatie in plaats van alleen lokale analyse.

## Projectupdates

### Formstr {#formstr}

[Formstr](https://github.com/formstr-hq/nostr-forms), het Google Forms-alternatief op Nostr, mergeerde [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), waarmee een signupflow werd toegevoegd die versleutelde private keys volgens [NIP-49](/nl/topics/nip-49/) gebruikt. Voor deze wijziging hadden gebruikers een [NIP-07](/nl/topics/nip-07/) browserextensie of een rechtstreeks geplakte `nsec` nodig om Formstr te gebruiken. De nieuwe flow genereert client-side een sleutelpaar, versleutelt de private key met een door de gebruiker gekozen wachtwoord via NIP-49's scrypt + XChaCha20-Poly1305-schema, en slaat vervolgens de resulterende `ncryptsec`-string op. Gebruikers kunnen later weer inloggen met hun wachtwoord zonder een signer-extensie te hoeven installeren. Key management blijft gedurende het hele proces client-side.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), de feature-rijke Android-client, mergeerde vier PR's die het Namecoin-gebaseerde werk voor [NIP-05](/nl/topics/nip-05/) uitbrachten dat [vorige week](/nl/newsletters/2026-03-04-newsletter/) nog open stond. [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) voegt censuurbestendige NIP-05-verificatie via ElectrumX toe voor `.bit`, `d/` en `id/` identifiers. Wanneer Amethyst een van deze suffixen in een NIP-05-veld detecteert, vraagt de client de transactiegeschiedenis van de naam op bij een ElectrumX-NMC-server, parseert daarna het `NAME_UPDATE`-script uit de laatste output om de Nostr-pubkey te extraheren, en weigert namen die ouder zijn dan 36.000 blokken, het verloopvenster van Namecoin. ElectrumX-verbindingen lopen via SOCKS5 wanneer Tor is ingeschakeld, met dynamische serverkeuze tussen clearnet- en `.onion`-endpoints. Een LRU-cache met een TTL van een uur voorkomt herhaalde blockchainqueries.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) repareert race conditions en resolver correctness in die flow. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) laat nieuwe gebruikers tijdens signup een followlijst importeren uit gewone NIP-05-identifiers of Namecoin-gebaseerde varianten. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) voegt instellingen toe voor aangepaste ElectrumX-servers, zodat gebruikers zelf kunnen kiezen welke server hun lookups afhandelt.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), een bibliotheek met helpermethoden voor het opslaan van Nostr-events in IndexedDB, mergeerde [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) met support voor AND-tagfilters uit [NIP-91](/nl/topics/nip-91/). De wijziging voegt intersection-semantiek toe aan client-side filtermatching, zodat IndexedDB-query's alle vermelde tagwaarden kunnen vereisen in plaats van eender welke. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) werkt de bibliotheek bij naar de nieuwste NIP-DB-interface, en een vervolgwijziging in [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) repareert een deadlock bij subscriben en verwijdert nostr-tools als productiedependency.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), een archive-first Nostr-indexer met ClickHouse-analytics, mergeerde [PR #8](https://github.com/andotherstuff/pensieve/pull/8) die cache-TTL's per entry afdwingt en misses per sleutel samenvoegt om CPU-pieken in de API te verlagen. De duurste time-series-endpoints, zoals engagement stats, activity per uur en activity per kind, gebruiken nu server-side TTL's van 10 minuten in plaats van gesynchroniseerde recompute-stormen uit te lokken.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), het gedecentraliseerde protocol en de serverstack voor mediahosting, mergeerde twee updates rond autorisatie voor BUD-11. [PR #91](https://github.com/hzrd149/blossom/pull/91) verplaatst optionele autorisatie naar een eigen BUD en verduidelijkt de rol van de tags `x` en `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) ruimt endpoint-specifiek auth-gedrag op en formaliseert de `X-SHA-256`-header voor verificatie van uploads. Samen brengen deze twee PR's de auth-logica onder in BUD-11 en halen ze ambiguiteit weg rond request hashing voor upload-, delete- en mediabeheerflows.

## NIP Updates

Recente wijzigingen in de [NIPs-repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-91](/nl/topics/nip-91/) (AND Operator for Filters)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): Voegt intersection-semantiek toe voor tagfilters, zodat relays queries kunnen beantwoorden die alle opgegeven tagwaarden vereisen in plaats van er slechts een. Dit vermindert client-side nafiltering en bandbreedteverbruik bij tagzware queries.

- **[NIP-66](/nl/topics/nip-66/) (Relay Discovery and Liveness Monitoring): Defensieve maatregelen** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): Na het [outbox-benchmarkwerk van vorige week](/nl/newsletters/2026-03-04-newsletter/), voegt de specificatie nu waarschuwingen toe voor unhappy paths in relay-monitoringdata. Clients mogen kind `30166` monitoring-events niet vereisen om te functioneren. Een monitor kan fout, verouderd of kwaadaardig zijn. Van clients wordt verwacht dat ze bronnen kruisen en niet grote delen van de relaygraaf van een gebruiker afsluiten op basis van een enkele feed.

- **[NIP-39](/nl/topics/nip-39/) (External Identities in Profiles): opschoning van kind 10011-register** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): Voegt de verwijzing naar kind `10011` direct aan de specificatie toe, in lijn met de implementatie van Amethyst die [vorige week](/nl/newsletters/2026-03-04-newsletter/) is besproken.

**Open PR's en discussies:**

- **[NIP-70](/nl/topics/nip-70/) (Protected Events): reposts weigeren die protected events insluiten** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): Als een relay NIP-70 afdwingt op het oorspronkelijke event maar reposts met dezelfde content accepteert, heeft de tag `-` in de praktijk geen effect. Deze PR voegt daarom de regel toe dat relays ook reposts van kind 6 en kind 16 van protected events moeten weigeren. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) implementeert dit al.

- **[NIP-71](/nl/topics/nip-71/) (Video Events): meerdere audiotracks** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): Voegt `imeta`-tags voor audio toe voor alternatieve tracks, taalvarianten en audio-only streams. Een client kan dan hetzelfde videobestand behouden terwijl de audiotaal wisselt, of audio als aparte track serveren voor podcastachtige content.

- **[NIP-11](/nl/topics/nip-11/) (Relay Information Document) en relay-attributen voor [NIP-66](/nl/topics/nip-66/)** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Voegt een gestructureerd veld `attributes` toe aan relay-infodocumenten, zodat clients en discovery-tools machineleesbare metadata krijgen naast de huidige vrije beschrijving.

## NIP Deep Dive: NIP-49 (Private Key Encryption)

[NIP-49](/nl/topics/nip-49/) definieert hoe een client een private key met een wachtwoord versleutelt en het resultaat codeert als een bech32-string `ncryptsec`. [Formstr](#formstr) gebruikt NIP-49 in zijn nieuwe signupflow.

Het formaat is niet gekoppeld aan een eigen event kind. Een client begint met de ruwe 32-byte secp256k1 private key, leidt met scrypt een symmetrische sleutel af uit het wachtwoord, versleutelt de key met XChaCha20-Poly1305 en verpakt het resultaat daarna in een bech32-string `ncryptsec`. Een flag van een byte legt vast of van de key bekend is dat die voor encryptie ooit onveilig is behandeld.

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

Het JSON-event hierboven is een voorbeeld op applicatieniveau, geen vereiste van NIP-49. De NIP standaardiseert het formaat van de versleutelde key. Een client kan de `ncryptsec` lokaal opslaan, synchroniseren via app-specifieke opslag of exporteren als backupstring. Wachtwoorden worden eerst genormaliseerd naar Unicode NFKC, zodat hetzelfde wachtwoord op verschillende clients en platforms consequent kan ontsleutelen.

De key-security-flag van een byte heeft drie gedefinieerde waarden: `0x00` betekent dat de geschiedenis van de key onbekend is, `0x01` betekent dat de key aantoonbaar onveilig is behandeld, bijvoorbeeld als plaintext geplakt in een webformulier voordat die werd versleuteld, en `0x02` betekent dat de key in een veilige context is gegenereerd en versleuteld en nooit is blootgesteld. Clients kunnen dit gebruiken om waarschuwingen te tonen wanneer een key met een bekende onveilige geschiedenis wordt geimporteerd.

NIP-49 beschermt keys beter dan een gewone export als `nsec`, maar de versleuteling is niet sterker dan het wachtwoord en de gekozen scrypt-cost. Hogere `LOG_N`-waarden maken offline guessing moeilijker maar vertragen ook legitieme decrypties. De specificatie waarschuwt tegen het publiceren van versleutelde keys naar publieke relays, omdat aanvallers baat hebben bij het verzamelen van ciphertext voor offline cracking. Ter vergelijking: remote signing via [NIP-46](/nl/topics/nip-46/) voorkomt blootstelling van keys helemaal, en Android-signing via [NIP-55](/nl/topics/nip-55/) houdt keys binnen een aparte signer-app. NIP-49 vult een andere rol: een draagbare versleutelde backup voor gebruikers die hun eigen sleutels beheren.

Implementaties zijn onder meer [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) voor signup, [Amber](https://github.com/greenart7c3/Amber) voor backup en restore van `ncryptsec`, [diVine v1.0.6](#divine-v106-met-e2e-testinfrastructuur-en-nip-49-import) voor accountimport, [Keep v0.6.0](#keep-v060) voor export van FROST-shares, en key-managementtools zoals [nsec.app](https://nsec.app) en [Alby](https://github.com/getAlby/hub).

## NIP Deep Dive: NIP-70 (Protected Events)

[NIP-70](/nl/topics/nip-70/) definieert protected events. Wanneer een event de tag `["-"]` draagt, moet een relay het weigeren tenzij die relay [NIP-42](/nl/topics/nip-42/)-authenticatie vereist en de geauthenticeerde pubkey overeenkomt met de auteur van het event.

De NIP-42-authflow werkt als volgt: de relay stuurt een `AUTH`-challenge met een willekeurige string, en de client antwoordt met een ondertekend event van kind `22242` waarvan de tags de relay-URL en de challenge bevatten. De relay controleert de handtekening en kijkt of de pubkey in het auth-event overeenkomt met de pubkey in het protected event dat wordt gepubliceerd. Als de pubkeys niet overeenkomen, weigert de relay het event met het message-prefix `restricted`.

De eventinhoud kan nog steeds openbaar zijn. De tag `-` bepaalt alleen wie het event mag publiceren naar een relay die de tag respecteert. Dit dekt semigesloten feeds van [NIP-29](/nl/topics/nip-29/) (Simple Groups), relayruimtes alleen voor leden en andere situaties waarin de auteur verspreiding via de relaygraaf wil beperken. NIP-70 is een conventie met een enkele tag, geen nieuw event kind, dus elk bestaand event kind kan de tag `-` dragen.

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

Zelfs als een relay publicatie door derden van het oorspronkelijke event blokkeert, kan iemand de inhoud nog opnieuw publiceren in een repost. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) pakt dat aan door te eisen dat relays ook reposts van protected events van kind 6 en kind 16 weigeren. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) voegt NIP-42-auth voor protected events toe, en [strfry PR #176](https://github.com/hoytech/strfry/pull/176) blokkeert reposts die protected content insluiten.

NIP-70 stuurt relaygedrag aan. Een ontvanger kan de inhoud nog steeds elders kopieren, en de specificatie zegt dat ook expliciet. De tag `-` geeft relays een machineleesbaar signaal om herpublicatie te weigeren. Ter vergelijking: [NIP-62](/nl/topics/nip-62/) (Request to Vanish) vraagt relays data achteraf te verwijderen, terwijl NIP-70 ongeautoriseerde publicatie al bij ingest voorkomt. De twee vullen elkaar aan: een auteur kan events als protected markeren om verspreiding te beperken en later verwijdering vragen als die de content ook van relays wil laten verdwijnen die ze toch hebben geaccepteerd.

---

Dat is het voor deze week. Bouw je iets of heb je nieuws om te delen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via [NIP-17](/nl/topics/nip-17/) DM</a> of vind ons op Nostr.
