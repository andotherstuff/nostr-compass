---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [Amethyst](https://github.com/vitorpamplona/amethyst) merge't desktop Tor, een custom C secp256k1-pad, [NIP-AC](/nl/topics/nip-ac/) calls, RFC 9420 MLS-compliance voor [Marmot](/nl/topics/marmot/) en multi-wallet [NIP-47](/nl/topics/nip-47/). [nstrfy](https://github.com/vcavallo/nstrfy-android) lanceert Nostr-native push notifications voor Android. [HAMSTR](https://github.com/LibertyFarmer/hamstr) voegt Reticulum toe voor Nostr over LoRa mesh. [Bloom](https://github.com/nostrnative/bloom) brengt een self-hosted [Blossom](/nl/topics/blossom/)-server en relay uit als desktopapp. [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) debuteert als internetradiodirectory op Nostr. [Botburrow](https://github.com/marmot-protocol/botburrow) start als self-hosted botplatform voor [Marmot](/nl/topics/marmot/)-groepschats. [Snort](https://github.com/v0l/snort) levert een security pass en grote performance-overhaul. [Primal Android](https://github.com/PrimalHQ/primal-android-app) herontwerpt de feed-layout.

## Top Stories

### Amethyst merges desktop Tor, C secp256k1, WebRTC calls, and multi-wallet NWC

[Amethyst](https://github.com/vitorpamplona/amethyst), de Android-client van vitorpamplona, merge'de deze week 29 PR's rond cryptografie, networking, calling en walletinfrastructuur.

[PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381) voegt desktop Tor-ondersteuning toe via een ingebedde kmp-tor-daemon met een fail-closed-ontwerp. Als Tor is ingeschakeld, lopen alle relayverbindingen door het embedded Tor-proces en weigert de app verbinding te maken als Tor niet start. Daarmee komt privacy-routing op gelijk niveau tussen Android en desktop, ondersteund door meer dan 130 unittests voor de Tor-integratie.

[PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374) voegt een custom C secp256k1-implementatie met JNI-bindings voor signature verification toe. De implementatie gebruikt GLV decomposition, wNAF point encoding en hardware-accelerated SHA-256 op zowel x86_64 als ARM64, wat een 2-3x versnelling oplevert voor Schnorr-signatuurverificatie ten opzichte van het eerdere pure Kotlin-pad. Aanvullende PR's ([PR #2188](https://github.com/vitorpamplona/amethyst/pull/2188), [PR #2195](https://github.com/vitorpamplona/amethyst/pull/2195), [PR #2204](https://github.com/vitorpamplona/amethyst/pull/2204)) voegen fused multiply-reduce-bewerkingen, een Fe4-struct en platform-specifieke intrinsics toe.

[PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202) werkt de pure Kotlin MLS-implementatie bij naar RFC 9420-compliance voor [Marmot](/nl/topics/marmot/), met reuse guard checks, additional authenticated data in ciphertext-bewerkingen, ciphertext-sample-derivatie, commit-fixes en thread safety. Een reeks WebRTC-PR's van [PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203) tot [PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211) bouwt daarnaast een volledig voice- en videocallsysteem voor [NIP-AC](/nl/topics/nip-ac/), inclusief ICE restart, runtime camera switching, network monitoring, automatische reconnect en Android 14+-foreground-service-fixes. [PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988) rondt de week af met multi-wallet [NIP-47](/nl/topics/nip-47/) support.

### nstrfy launches Nostr-native push notifications for Android

[nstrfy](https://github.com/vcavallo/nstrfy-android) lanceerde op 13 april met drie releases van [v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0) tot [v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0). De app is een fork van ntfy-android waarin het HTTP-transport is vervangen door Nostr. In plaats van een server te pollen voor push notifications subscribe't nstrfy op kind `7741`-events op configureerbare relays en toont die als native Android-notificaties.

Het notificatiemodel ondersteunt zowel plaintext als [NIP-44](/nl/topics/nip-44/) encrypted payloads. Wanneer encryptie actief is gebruikt nstrfy [Amber](https://github.com/greenart7c3/Amber) voor signing via [NIP-55](/nl/topics/nip-55/) of een lokale nsec. Topic-based subscriptions laten per topic npub-allowlists toe, relaylijsten worden uit het profiel van de gebruiker geïmporteerd via [NIP-65](/nl/topics/nip-65/), en de app respecteert [NIP-40](/nl/topics/nip-40/) event expiration. De volledige ntfy-notificatiewoordenschat blijft beschikbaar, inclusief tap-to-open URLs, prioriteitsniveaus, custom icons en action buttons.

Het companion-project [nstrfy.sh](https://github.com/vcavallo/nstrfy.sh) levert zowel een bash CLI als een hosted webclient op [nstrfy.sh](https://nstrfy.sh) voor versturen en luisteren vanuit de browser, met NIP-07 signer support. De native app staat op [Zapstore](https://zapstore.dev/apps/io.nstrfy.android).

### HAMSTR adds Reticulum for Nostr over LoRa mesh

[HAMSTR](https://github.com/LibertyFarmer/hamstr), het project dat Nostr-events en Lightning zaps over ham radio verstuurt, merge'de [PR #10](https://github.com/LibertyFarmer/hamstr/pull/10) op 12 april en voegde [Reticulum](https://reticulum.network/) mesh networking toe als transport-backend. Reticulum is een cryptografisch mesh-protocol dat kan draaien over LoRa, HF, VHF/UHF-radio, seriële links en TCP/IP. Daarmee kan HAMSTR Nostr-events over een mesh van RNode-hardware doorgeven zonder internetinfrastructuur.

De bestaande AX.25 Packet Radio- en VARA HF-transports blijven beschikbaar, zodat operators de radioverbinding kunnen kiezen die past bij hun setup. De zero-knowledge serverarchitectuur van HAMSTR betekent dat de relay geen private keys ziet, en de [NIP-57](/nl/topics/nip-57/) zap-compliance zorgt ervoor dat offline Lightning zaps correct verschijnen in clients zoals Amethyst en Primal. Een setupgids voor het Reticulum-transport staat in [RETICULUM.MD](https://github.com/LibertyFarmer/hamstr/blob/master/RETICULUM.MD). In dezelfde week migreerde [PR #11](https://github.com/LibertyFarmer/hamstr/pull/11) de frontend naar Svelte 5 en TailwindCSS v4.

## Shipping This Week

### Bloom v0.1.0 ships self-hosted Blossom server and relay

[Bloom](https://github.com/nostrnative/bloom) bracht zijn eerste release uit, [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0), op 9 april. Gebouwd met Tauri v2 en React 19 bundelt Bloom een volledige [Blossom](/nl/topics/blossom/)-media server en een Nostr relay in een enkele desktopapp voor macOS, Windows en Linux. Gebruikers krijgen sovereign file storage met SHA-256 content addressing, [NIP-94](/nl/topics/nip-94/) file metadata support en `blossom://`-resolutie zonder zelf serverinfrastructuur te hoeven beheren.

### WaveFunc v0.1.0 and v0.1.1 launch Nostr internet radio

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) bracht [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0) en [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) uit op 13 april en lanceerde als Nostr-gebaseerde internetradiodirectory en speler. De app gebruikt custom event kinds voor stations, favorieten, live chat en comments, terwijl een Khatru-relaybackend SQLite-opslag en Bluge full-text search met [NIP-50](/nl/topics/nip-50/) verzorgt.

WaveFunc levert daarnaast een [NIP-60](/nl/topics/nip-60/) Cashu-wallet en nutzap-support, plus in v0.1.1 genrecarrousels, een Lightning-donatiepopover, station management voor geauthenticeerde gebruikers en Zapstore-listing. De Tauri v2-desktopbuild kreeg system tray integration, media key support, autostart en deep linking.

### Snort ships v0.5.0 through v0.5.3 with security hardening and performance overhaul

[Snort](https://github.com/v0l/snort) bracht drie releases uit van [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0) tot [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3). v0.5.0 levert de grootste wijziging: een security audit, echte Schnorr-signatuurverificatie, hardening van [NIP-46](/nl/topics/nip-46/) tegen forged relay messages, verbeterde PIN-encryptie en het verwijderen van vertrouwen op onbevestigde NIP-26-delegation. Aan de prestatiekant zijn er batched WASM-verificatie, lazy-loaded routes, een herschreven priority profile loader en worker-relay-optimalisaties.

[PR #620](https://github.com/v0l/snort/pull/620) werkte het berichten­systeem opnieuw uit voor performance, met gift wraps die in de worker relay worden opgeslagen en een efficiëntere Map-gebaseerde chatlijst. De release voegt ook kind `7000` payment-required invoice-weergave toe voor [NIP-90](/nl/topics/nip-90/) DVM's.

### Primal Android ships 3.0.21 and redesigns feed layout

[Primal Android](https://github.com/PrimalHQ/primal-android-app) bracht [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21) uit met fixes voor poll zap votes, walletdeling tussen meerdere accounts en auto-reconnect voor remote signer en walletservice. Daarbovenop merge'de het team zeven PR's die de hoofdfeed opnieuw vormgeven, met grotere avatars, contentindentatie, video in mediacards, een compact quick-replyveld en opnieuw ontworpen app bars.

### Nostria v3.1.19 through v3.1.21 add local AI image generation

[Nostria](https://github.com/nostria-app/nostria) bracht drie releases uit van [v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19) tot [v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21) met meer dan 80 commits. De hoofdfunctie is lokale image generation met Janus Pro en WebGPU-acceleratie, zodat gebruikers afbeeldingen on-device kunnen genereren zonder externe API. De releases voegen ook cloud image generation, multimodal chat, ONNX runtime support, een AI prompt library en cachebeheer toe.

### TubeStr v1.0.3 ships feed and studio updates

[TubeStr](https://github.com/Tubestr/tubestr-v2), een privé video-app voor families gebouwd op Nostr, bracht [v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3) uit op 13 april. De release voegt feed- en studioverbeteringen toe, met [PR #3](https://github.com/Tubestr/tubestr-v2/pull/3) voor vernieuwde onboarding en [PR #2](https://github.com/Tubestr/tubestr-v2/pull/2) voor een fix van een video-exportfout. De app gebruikt NDK en MDK voor encrypted mediadeling tussen familieleden.

## In Development

### Botburrow begins development as Marmot bot platform

[Botburrow](https://github.com/marmot-protocol/botburrow) is een nieuw project van het Marmot-team, gestart op 3 april. Het is een self-hosted botmanagementplatform waarin elke bot een eigen Nostr-identity krijgt, lid wordt van [Marmot](/nl/topics/marmot/) MLS-encrypted groepschats via Welcome messages en end-to-end encrypted berichten kan verzenden en ontvangen. Het dashboard is gebouwd met Rails 8.1 en praat met een enkele `wnd`-daemon via een Unix socket.

Botburrow exposeert ook een substantiële scripting- en operationslaag, met commands, triggers en scheduled actions in custom Ruby-code, live chatweergaven voor echte groepen en opslag per bot voor configuratie en gegenereerde output. Een [Docker image](https://github.com/marmot-protocol/botburrow/commit/2ed012078eaab3c5b92dff16b87865c2e353bd80) richt zich op zero-config self-hosting op Umbrel en Start9.

### Nostr Archives adds trending feeds relay and entity resolution

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api) werkte verder aan zowel de Rust-API als de Next.js-frontend. [PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118) voegt time-range filtering toe aan de client leaderboard en [PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117) engagement counters aan reply-events. Aan frontendzijde resolven [PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85) en [PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86) Nostr-entiteiten direct uit URL-paden en voegen een API-documentatiepagina toe.

### Damus fixes favorites timeline

[Damus](https://github.com/damus-io/damus) merge'de [PR #3708](https://github.com/damus-io/damus/pull/3708), die `subscribe_to_favorites()` herschrijft met filtering in place, heropbouw van deduplicatie en persistente tabselectie.

### Nostur adds private zaps and custom emoji viewing

[Nostur](https://github.com/nostur-com/nostur-ios-public) pushte deze week tien commits met private zap support, custom emoji viewing, een fix voor geanimeerde `.webp`-weergave en detectie van audioformaten voor voice messages.

### Amber ships v6.0.1 through v6.0.3 with WebDAV backup and relay reconnection fixes

[Amber](https://github.com/greenart7c3/Amber), de Android [NIP-55](/nl/topics/nip-55/) signer-app, bracht drie releases uit. [v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1) voegt WebDAV- en Google Drive-backups toe, exponential backoff voor relay reconnects en Quartz 1.08.0. [v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2) voegt een accountindexoptie toe bij seed words en repareert reconnect wanneer een relay offline is bij startup. [v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3) repareert lege request IDs bij intents.

### Plektos v0.6.0 redesigns with Ditto themes

[Plektos](https://github.com/derekross/plektos), het meetup- en eventsplatform gebouwd op [NIP-52](/nl/topics/nip-52/), bracht [v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77) en [v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879) uit. De update voegt Ditto-achtige communitythemes, custom background images, avatarvormconfiguratie en een UI-overhaul toe. [PR #6](https://github.com/derekross/plektos/pull/6) behandelt daarnaast een brede code review.

### Shadow adds Nostr OS API and Cashu wallet app

[Shadow](https://github.com/justinmoon/shadow), het app-runtimeplatform van Justin Moon, pushte meer dan 30 commits in twee dagen. [Commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df) voegt een Cashu-walletapp toe binnen de Shadow-runtime, en [commit 865c415](https://github.com/justinmoon/shadow/commit/865c415) een podcastspelerdemo. De runtime exposeert `Shadow.os.nostr` en `Shadow.os.audio` als first-class OS API's.

### Lief fixes Amber login and adds Zapstore

[Lief](https://gitlab.com/chad.curtis/lief), een Nostr-app voor lange brieven aan andere Nostr-gebruikers, bracht build `v2026.04.12` uit op 12 april. De update repareert een Amber-loginprobleem op Android, vereenvoudigt de signer nudge-flow, werkt nostrify bij en voegt Zapstore-integratie toe.

### Espy overhauls color picker and fixes Amber login

[Espy](https://gitlab.com/chad.curtis/espy) bracht build `v2026.04.12` uit met een vernieuwde color picker, fixes voor hue ring flicker, Easter egg-personages en een compressiewinst van 703KB in PNG-assets. De release repareert ook dezelfde Amber-loginissues en voegt Zapstore-integratie toe.

### Jumble adds per-feed kind filters and articles tab

[Jumble](https://github.com/CodyTseng/jumble) pushte 13 commits die per-feed kind filtering, een Articles-tab, sync van notification read status, een avatar hide mode en een fix voor account switching toevoegen.

### Primal Web ships 8 version bumps

[Primal Web](https://github.com/PrimalHQ/primal-web-app) bracht versies 3.0.93 tot en met 3.0.101 uit in één week met 21 commits. Het werk richtte zich op live-streamchatverbeteringen, mention boundary-fixes, bookmark pagination, duplicate like prevention en relay proxy-fixes.

## Protocol and Spec Work

### NIP Updates

Recente wijzigingen in de [NIPs-repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-34](/nl/topics/nip-34/) (Git Stuff): Add `nostr://` clone URLs** ([PR #2312](https://github.com/nostr-protocol/nips/pull/2312)): deze PR voegt een `nostr://` clone URL-formaat toe voor git-over-Nostr repositories. Er worden drie URL-vormen gedefinieerd, met percent-encoding voor relay hints en identifiers, en de vorm is al geïmplementeerd door Shakespeare, ngit en tools zoals GitWorkshop.dev en NostrHub.io.

**Open PRs and Discussions:**

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): stelt een nieuw kind `10164` replaceable event voor waarmee makers payment gateways, prijsmodellen en subscription rules voor betaalde content kunnen publiceren.
- **NIP-XX: Relay Self-Declaration Manifest and Retention Horizon** ([PR #2314](https://github.com/nostr-protocol/nips/pull/2314)): stelt kind `10100` voor als gossipable relay-manifest en `HORIZON` als nieuw relay-to-client message om retention-vensters expliciet te maken.
- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): stelt kind `20411` voor voor encrypted geolocation met per-recipient [NIP-44](/nl/topics/nip-44/) payloads en een `ttl`-tag.
- **[NIP-5C](/nl/topics/nip-5c/) (Scrolls): WASM programs update** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): verfijnt het publiceren en uitvoeren van sandboxed WASM-programma's op Nostr en bouwt voort op [NIP-5A](/nl/topics/nip-5a/).
- **[NIP-44](/nl/topics/nip-44/) large payload support** ([PR #1907](https://github.com/nostr-protocol/nips/pull/1907)): stelt een backwards-compatible uitbreiding voor voor payloads groter dan 65.535 bytes, relevant voor onder meer grote [NIP-46](/nl/topics/nip-46/) contactlijsten.
- **[NIP-C7](/nl/topics/nip-c7/): Restrict kind 9 to chat views** ([PR #2310](https://github.com/nostr-protocol/nips/pull/2310)): verduidelijkt dat kind `9`-chatberichten alleen in chatgerichte weergaven horen te verschijnen, niet in algemene sociale feeds.

## NIP Deep Dive: NIP-29 (Relay-based Groups)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md) definieert een model voor groepsberichten waarin de relay zelf groepslidmaatschap en moderatie beheert. Groepen leven op een specifieke relay, worden geïdentificeerd door een string-ID en vertrouwen op de relay voor write-permissions en policy enforcement. Dat is een ander model dan [Marmot](/nl/topics/marmot/) of [NIP-17](/nl/topics/nip-17/): in NIP-29 is de relay de autoriteit en kan de relay-operator de berichten lezen.

Een groep wordt geïdentificeerd door het formaat `<host>'<group-id>`, bijvoorbeeld `groups.nostr.com'abcdef`. Gebruikersevents die naar een groep worden gestuurd dragen een `h`-tag met de group ID, en de `previous`-tag dient als tamper-detection door recente eventfragmenten in de laatste vijftig berichten te refereren. Relays kunnen events met ongeldige `previous`-verwijzingen weigeren, zodat out-of-context rebroadcasting op geforkte kopieën detecteerbaar wordt.

Lidmaatschap en moderatie worden beheerd via 9000-range events zoals join requests, removals, metadata-edits en rolbeheer. De relay publiceert snapshots van de groepsconfiguratie via addressable events zoals kind `39000` voor metadata en kind `39003` voor rollen en capabilities. Omdat de spec elk event kind binnen een groep accepteert kunnen niet alleen chatberichten maar ook [NIP-23](/nl/topics/nip-23/) artikelen, [NIP-52](/nl/topics/nip-52/) events en [NIP-53](/nl/topics/nip-53/) live-activiteiten in dezelfde groepsnamespace bestaan.

[Flotilla](https://gitea.coracle.social/coracle/flotilla) is vandaag de meest actieve NIP-29-client, en [Coracle](https://github.com/coracle-social/coracle) ondersteunt het model ook. De tradeoff tegenover encrypted alternatieven blijft duidelijk: NIP-29 biedt eenvoud en publieke communities, maar geen end-to-end encryptie of forward secrecy.

## NIP Deep Dive: NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md) definieert een protocol voor on-demand computation over Nostr. Een klant publiceert een job request, providers concurreren om die uit te voeren en resultaten worden teruggeleverd als Nostr-events. De spec reserveert kinds `5000-5999` voor requests, `6000-6999` voor resultaten en kind `7000` voor feedbackstatussen.

Requests gebruiken `i`-tags voor input, `output` voor het gewenste formaat, `bid` voor het maximale bedrag en `param` voor jobspecifieke instellingen. Resultaten verwijzen naar de oorspronkelijke aanvraag, bevatten de pubkey van de klant en kunnen optioneel een Lightning invoice dragen. Feedback-events zoals `payment-required`, `processing`, `error` en `success` geven de klant realtime zicht op langer lopende jobs.

Het model ondersteunt job chaining via inputtype `job`, zodat output van de ene provider input kan worden voor een volgende stap, bijvoorbeeld transcriptie, samenvatting en vertaling. Voor privacy kunnen klanten input en parameters encrypted in `content` plaatsen met [NIP-04](/nl/topics/nip-04/), al vereist dat gerichte requests naar een specifieke provider. DVM-discovery zelf ligt buiten de request/response-lus en leunt op [NIP-89](/nl/topics/nip-89/).

---

Dat is het voor deze week. Bouw je iets of heb je nieuws om te delen? Stuur ons een DM op Nostr of vind ons op [nostrcompass.org](https://nostrcompass.org).
