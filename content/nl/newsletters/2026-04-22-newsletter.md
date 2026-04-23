---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [Amethyst](https://github.com/vitorpamplona/amethyst) levert een grote update rond [Marmot](/nl/topics/marmot/), communities en MoQ-audiorooms. [TollGate](https://github.com/OpenTollGate/tollgate) stabiliseert pay-per-use internettoegang over Nostr en Cashu in v0.1.0, en [nostream](https://github.com/Cameri/nostream) sluit een week relaywerk af rond [NIP-45](/nl/topics/nip-45/), [NIP-62](/nl/topics/nip-62/), compressie, query hardening en volledige [NIP-11](/nl/topics/nip-11/) parity. Forgesworn publiceert een volledige signing-, identity- en paid-API-stack voor Nostr. ShockWallet blijft Nostr-native Lightning-walletflows doorontwikkelen. De Formstr-suite (Pollerama, Forms, Calendar) merge't 26 PR's rond security hardening en RRULE support. StableKraft, Keep, topaz, WoT Relay, Flotilla en NipLock ronden de shipping-lijst af. De deep dives behandelen [NIP-72](/nl/topics/nip-72/) moderated communities en [NIP-57](/nl/topics/nip-57/) zaps.

## Top Stories

### Amethyst ships Marmot MIP compliance, NIP-72 communities, zap goals, and MoQ audio rooms

[Amethyst](https://github.com/vitorpamplona/amethyst) merge'de deze week 57 PR's. De hoofdthema's zijn encrypted-group compliance voor [Marmot](/nl/topics/marmot/), first-class moderated communities, zap goals op live streams en een nieuwe audiorooms-stack gebouwd op Media over QUIC.

Aan de Marmot-kant brengt [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) de embedded [MDK](https://github.com/marmot-protocol/mdk)-implementatie in lijn met MIP-01 en MIP-05, inclusief VarInt-encoding van TLS-achtige length prefixes en round-trip-validatie tegen MDK-testvectors. [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) voegt MIP-00 KeyPackage Relay List support toe, [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) sluit admin- en mediagaten uit cross-client tests met White Noise, en [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) plus [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) repareren MLS commit framing en outer-layer decryptie. De vervolg-PR's [PR #2477](https://github.com/vitorpamplona/amethyst/pull/2477) en [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) dichten de resterende commit- en message-encryptiongaten en voegen een volledige cryptografische validator toe. [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) levert daarnaast `amy`, een CLI voor Marmot- en MLS-groepsoperaties.

[PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) voegt first-class [NIP-72](/nl/topics/nip-72/) community creation en management toe, inclusief kind `34550` community definitions, moderator- en relay hints, posting via `a`-tags en approvalbeheer via kind `4549`. [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) voegt [NIP-75](/nl/topics/nip-75/) zap goals toe aan het [NIP-53](/nl/topics/nip-53/) Live Activities-scherm, met progress bars, one-tap zaps en een top-zappers leaderboard op basis van kind `9735` receipts. [PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494) brengt ten slotte een Media over QUIC-client en audio-rooms support, terwijl [PR #2487](https://github.com/vitorpamplona/amethyst/pull/2487) het Public Chats-scherm toevoegt.

### TollGate v0.1.0 stabilizes pay-per-use internet over Nostr and Cashu

[TollGate](https://github.com/OpenTollGate/tollgate) bracht op 21 april [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) uit, de eerste getagde snapshot van zijn specification set voor pay-per-use network access. Het protocol laat een apparaat dat connectiviteit kan afschermen, zoals een WiFi-router of Bluetooth-tether, prijzen adverteren, [Cashu](/nl/topics/cashu/) ecash accepteren en sessies beheren via prepaid lokale tokens in plaats van accounts of abonnementen.

De release fixeert drie architectuurlagen. [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) definieert Advertisement-, Session- en Notice-events. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) legt Cashu-betalingen daarbovenop, zodat klanten tokens van elke geadverteerde mint kunnen inwisselen. [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) tot en met HTTP-03 definiëren een plain-HTTP-oppervlak voor beperktere apparaten, [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) beschrijft het Nostr-relaytransport en [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) de captive-portal routinglaag.

Het betaalmiddel is een bearer token, zodat een klant met een lokale Cashu-wallet de eerste minuut connectiviteit kan kopen zonder voorafgaande internettoegang. TollGates kunnen ook uplink van elkaar kopen, wat het bereik voorbij één operator duwt. De nieuwe [TollGate topic page](/nl/topics/tollgate/) behandelt de volledige laagstapel.

### nostream merges 53 PRs for NIP-45, NIP-62, compression, and query hardening

[nostream](https://github.com/Cameri/nostream) merge'de 53 PR's in één week rond nieuwe NIP-support, queryperformance, security hardening en operationele polish. [PR #522](https://github.com/Cameri/nostream/pull/522) voegt [NIP-45](/nl/topics/nip-45/) `COUNT`-support toe, [PR #544](https://github.com/Cameri/nostream/pull/544) adverteert [NIP-62](/nl/topics/nip-62/) right-to-vanish, [PR #548](https://github.com/Cameri/nostream/pull/548) laat uppercase tag filters toe en [PR #514](https://github.com/Cameri/nostream/pull/514) voegt gzip- en xz-compressie toe aan import en export van events.

Aan de correctheids- en securitykant brengt [PR #534](https://github.com/Cameri/nostream/pull/534) een benchmarkharnas en SQL-optimalisatie, [PR #524](https://github.com/Cameri/nostream/pull/524) vervangt prefix matching voor whitelist/blacklist pubkeys door exact-match checks, [PR #553](https://github.com/Cameri/nostream/pull/553) maakt `upsertMany` deterministisch bij gelijke `created_at`-waarden en [PR #493](https://github.com/Cameri/nostream/pull/493) beperkt vertrouwen in `X-Forwarded-For` tot geconfigureerde trusted proxies. [PR #557](https://github.com/Cameri/nostream/pull/557) brengt de relay bovendien naar volledige [NIP-11](/nl/topics/nip-11/) parity.

## Shipping This Week

### Primal Android ships Explore tab, NIP-05 verification, and audio player

[Primal Android](https://github.com/PrimalHQ/primal-android-app) bouwde door op de feed-redesign van vorige week met 11 nieuwe PR's. [PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021) introduceert een Explore-tab rond populaire gebruikers, follow packs en curated feeds, [PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015) voegt een feed editor toe, [PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994) levert NIP-05-verificatie-UI en [PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997) een inline audiospeler. [PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018) voegt [NIP-46](/nl/topics/nip-46/) nostr-connect-pairing toe vanuit de wallet-QR-scanner.

### strfry adds Prometheus write-path metrics and fixes NIP-42 AUTH envelope

[strfry](https://github.com/hoytech/strfry) bracht operatorgerichte verbeteringen uit. [PR #194](https://github.com/hoytech/strfry/pull/194) voegt Prometheus write-path metrics toe, [PR #197](https://github.com/hoytech/strfry/pull/197) logt bytes up/down en compressieratio's per verbinding, en [PR #192](https://github.com/hoytech/strfry/pull/192) maakt de filter-taglimiet runtime-configureerbaar. [PR #201](https://github.com/hoytech/strfry/pull/201) wijzigt [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH-fouten van `NOTICE` naar de `OK` envelope die de NIP voorschrijft.

### Shopstr hardens storefront security across 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr) merge'de 13 PR's die grotendeels door security fixes worden gedomineerd. [PR #434](https://github.com/shopstr-eng/shopstr/pull/434) sluit stored JavaScript in storefrontlinks, [PR #417](https://github.com/shopstr-eng/shopstr/pull/417) blokkeert reflected XSS in storefront policy-rendering, [PR #418](https://github.com/shopstr-eng/shopstr/pull/418) sluit een ongeauthenticeerde cached-event deletion API en [PR #433](https://github.com/shopstr-eng/shopstr/pull/433) maakt cached-message reads auth-verplicht. Andere fixes behandelen SSRF, veilige replay van failed-relay publish queues, wallet-event fetches en discount-hervalidatie.

### Nostria v3.1.26 through v3.1.28 add background music playback on Android

[Nostria](https://github.com/nostria-app/nostria) bracht zes releases uit van [v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22) tot [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28). De hoofdfunctie in [v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26) is achtergrondmuziekweergave op Android, inclusief mediabediening in de notificatiebalk en op het lockscreen. De vervolgreleases harden dat nieuwe media-service-oppervlak.

### Wisp v0.18.0-beta adds Normie Mode, For You feed, and NIP-29 group config

[Wisp](https://github.com/barrydeen/wisp) bracht [v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta) uit op 16 april. [PR #462](https://github.com/barrydeen/wisp/pull/462) voegt een Normie Mode met fiatbedragen toe, [PR #464](https://github.com/barrydeen/wisp/pull/464) vernieuwt onboarding en [PR #469](https://github.com/barrydeen/wisp/pull/469) bouwt een For You-feed. Aan protocolzijde voegt [PR #471](https://github.com/barrydeen/wisp/pull/471) [NIP-29](/nl/topics/nip-29/) group configuration toe en [PR #478](https://github.com/barrydeen/wisp/pull/478) repareert AUTH-volgorde voor groepsacties.

### NoorNote v0.8.4 adds Scheduled Posts and live stream zapping

[NoorNote](https://github.com/77elements/noornote) bracht [v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) en [v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5) uit. v0.8.4 voegt Scheduled Posts toe via een NoorNote-relay die een volledig ondertekend event op het ingestelde moment publiceert, zodat private keys het apparaat niet verlaten. Diezelfde release voegt one-tap zapping toe vanaf live-stream cards via [NIP-53](/nl/topics/nip-53/). v0.8.5 repareert een timeline deduplication bug.

### topaz v0.0.2 ships a Nostr relay for Android

[topaz](https://github.com/fiatjaf/topaz), een nieuwe Nostr-relay van fiatjaf die op Android-telefoons draait, publiceerde [v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2) op 2026-04-17. De scope is nog smal maar bruikbaar: een werkende relay in een installeerbaar Android-pakket.

### StableKraft v1.0.0 ships the first stable music-and-podcast PWA release

[StableKraft](https://github.com/ChadFarrow/stablekraft-app) is een Next.js PWA voor het ontdekken en streamen van muziek uit podcastfeeds, met Nostr voor auth en social features en Lightning voor V4V-betalingen. Het project bereikte [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0) op 2026-04-18. In dezelfde week verkleinde het team de nightly reparse-window en verstevigde feed-ingestie met OPML-cache en illegal-XML stripping.

### NipLock ships a NIP-17-based password manager

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) is een password manager die credentials op meerdere apparaten opslaat en synchroniseert via [NIP-17](/nl/topics/nip-17/) gift-wrapped direct messages. Elke password entry is een NIP-17 DM van de sleutel van de gebruiker naar zichzelf, zodat dezelfde events repliceren naar elk apparaat dat met dezelfde sleutel authenticeert. Signing werkt met een ruwe `nsec`, browserextensies zoals [nos2x](https://github.com/fiatjaf/nos2x) of [Amber](https://github.com/greenart7c3/Amber) via [NIP-46](/nl/topics/nip-46/).

### flotilla-budabit polishes its NIP-34 repo surface

De Budabit-fork van [Flotilla](https://gitea.coracle.social/coracle/flotilla), [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit), bracht een cluster fixes uit voor zijn NIP-34 git-over-Nostr-workflow. De week herstelt repo-discussiebediening, houdt sticky tabs zichtbaar, laadt repo-announcements van opgeslagen GRASP-relays en synchroniseert maintainer-applied patch status.

### rx-nostr 3.7.2 through 3.7.4 add default verifier and optional constructor args

[rx-nostr](https://github.com/penpenpng/rx-nostr) bracht [3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2), [3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3) en [3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4) uit. [PR #192](https://github.com/penpenpng/rx-nostr/pull/192) voegt een default Schnorr verifier toe, een bijpassende `crypto@3.1.6` corrigeert een `@noble/curves`-bug en [PR #195](https://github.com/penpenpng/rx-nostr/pull/195) maakt de argumenten van `createRxNostr()` optioneel.

### Keep Android v1.0.0 ships with reproducible builds and zero trackers

[Keep](https://github.com/privkeyio/keep-android) bracht [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0) uit op 21 april. [PR #241](https://github.com/privkeyio/keep-android/pull/241) voegt een reproduceerbaar buildrecept toe, [PR #248](https://github.com/privkeyio/keep-android/pull/248) vervangt Google ML Kit door ZXing om Google Play Services te verwijderen en [PR #252](https://github.com/privkeyio/keep-android/pull/252) publiceert een Exodus Privacy-scan met nul trackers op de releasebuild.

### Flotilla 1.7.3 and 1.7.4 add kind-9 wrapping for richer NIP-29 rooms

[Flotilla](https://gitea.coracle.social/coracle/flotilla), de [NIP-29](/nl/topics/nip-29/) groups-client van hodlbod, bracht [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) en [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) uit. De belangrijkste protocolwijziging is kind-9-wrapping van niet-chat-contenttypes, waardoor polls, kalenderitems en andere objecten hun roomcontext behouden wanneer ze in een groep worden geplaatst. Dezelfde releaselijn voegt polls, Aegis URL scheme support voor [NIP-46](/nl/topics/nip-46/) login, native share support, room mentions, drafts, video in calls en feed-paginationverbeteringen toe.

### WoT Relay v0.2.1 migrates eventstore to LMDB

[WoT Relay](https://github.com/bitvora/wot-relay) bracht [v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1) uit op 2026-04-22. [PR #97](https://github.com/bitvora/wot-relay/pull/97) migreert de eventstore naar LMDB en stemt de bootstrap-fetches opnieuw af zodat de relay zijn initiële trust graph kan opbouwen zonder upstream read budgets uit te putten. [PR #99](https://github.com/bitvora/wot-relay/pull/99) werkt `golang.org/x/crypto` bij en [PR #100](https://github.com/bitvora/wot-relay/pull/100) actualiseert de geadverteerde [NIP-11](/nl/topics/nip-11/) software-URL en versie.

### Formstr suite: Pollerama security pass, Forms i18n, Calendar RRULE support

De Formstr-suite merge'de 26 PR's over Pollerama, Formstr Forms en Nostr Calendar, met een duidelijke securityfocus in de polling-app en featurewerk in de rest. [Pollerama](https://pollerama.fun) hardent key handling met logout-expiry voor cached DMs, secure browser storage voor lokale sleutels en defensieve `JSON.parse` rond kind `0`-profielen. [Formstr](https://formstr.app) voegt audio- en video-URL support, i18n en een Google Forms-importer toe, plus een fix die gevoelige key-logs uit de browserconsole verwijdert.

[Nostr Calendar by Formstr](https://calendar.formstr.app) bracht [v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0) en [v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0) op dezelfde dag uit, met als hoofdfunctie een echte recurrence-rule-laag. [PR #107](https://github.com/formstr-hq/nostr-calendar/pull/107) voegt multiple en custom RRULE support toe, [PR #101](https://github.com/formstr-hq/nostr-calendar/pull/101) interpreteert floating RRULE-datums als UTC en andere PR's voegen gedeelde events, list-level notification preferences en een vernieuwde loginflow toe. Alle drie de projecten bouwen voort op [NIP-52](/nl/topics/nip-52/).

### Also shipped: notedeck, nostr.blue, cliprelay, Captain's Log

Een handvol clients bracht iteratieve releases uit zonder grote headline-functies. [notedeck](https://github.com/damus-io/notedeck) publiceerde [v0.10.0-beta.4](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.4) met fixes voor kolomrendering en relaypools. [nostr.blue v0.8.6](https://github.com/patrickulrich/nostr.blue/releases/tag/v0.8.6) trok Dioxus 0.7.5 binnen en maakte de Android-build weer mogelijk. [cliprelay](https://github.com/tajava2006/cliprelay) bracht desktop- en Android-updates uit voor clipboard-sync via Nostr, en [Captain's Log](https://github.com/nodetec/comet) publiceerde alpha-builds met liveness detection voor sync-relays.

## In Development

### whitenoise-rs refactors to session-scoped account views

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), de Rust-daemon onder de [Marmot](/nl/topics/marmot/)-client, merge'de 15 PR's die een meerfasige refactor van globale singletons naar `AccountSession`-views per account voortzetten. [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) zette de `AccountSession`- en `AccountManager`-scaffolding neer, waarna vervolgfases relay handles, drafts en settings, message ops, group read/write, membership, push notifications, key-package reads, group creation en uiteindelijk event dispatch naar session-owned oppervlakken migreerden.

### White Noise app adds block/unblock UI, leave-group, and offline notices

[White Noise](https://github.com/marmot-protocol/whitenoise) voegde de ontbrekende group-lifecycle controls toe. [PR #578](https://github.com/marmot-protocol/whitenoise/pull/578) levert block/unblock UI, [PR #571](https://github.com/marmot-protocol/whitenoise/pull/571) en [PR #572](https://github.com/marmot-protocol/whitenoise/pull/572) koppelen Rust-side `clear_chat`, `delete_chat` en `leave_and_delete_group` aan de app, en [PR #569](https://github.com/marmot-protocol/whitenoise/pull/569) plus [PR #576](https://github.com/marmot-protocol/whitenoise/pull/576) tonen offline notices wanneer de daemon zijn relays niet kan bereiken. [PR #585](https://github.com/marmot-protocol/whitenoise/pull/585) vernauwt "delete all key packages" naar legacy key packages.

### MDK adds mixed-version invite support and SelfUpdate convergence

[MDK](https://github.com/marmot-protocol/mdk) merge'de zeven PR's rond compatibiliteit en robustness. [PR #261](https://github.com/marmot-protocol/mdk/pull/261) berekent `RequiredCapabilities` als de LCD van invitee capabilities, waardoor mixed-version invites tussen Amethyst en White Noise werken. [PR #264](https://github.com/marmot-protocol/mdk/pull/264) brengt SelfUpdate wire formats tussen implementaties samen, terwijl andere PR's malformed invitees opvangen, admin depletion-validatie repareren en state in het in-memory opslagbackend beschermen.

### nostter adds NIP-44 encryption across people lists, bookmarks, and mutes

[nostter](https://github.com/SnowCait/nostter) merge'de tien PR's. [PR #2088](https://github.com/SnowCait/nostter/pull/2088), [PR #2089](https://github.com/SnowCait/nostter/pull/2089) en [PR #2090](https://github.com/SnowCait/nostter/pull/2090) migreren mute lists, bookmarks en people lists naar [NIP-44](/nl/topics/nip-44/) encryption, terwijl [PR #2087](https://github.com/SnowCait/nostter/pull/2087) een legacy mute-migratiepad verwijdert.

### zap.cooking ships Nourish scoring and a reusable comment thread

[zap.cooking](https://github.com/zapcooking/frontend) merge'de 20 PR's. De hoofdfunctie is een nieuwe Nourish recipe-scoring module, terwijl een vierfasige refactor de commentsmodule uitwerkt tot een herbruikbare `CommentThread`. Andere polish omvat recipe scaling, een uniforme media-uploadknop en een profile Replies-tab.

### ridestr extracts shared rider coordinator

[ridestr](https://github.com/variablefate/ridestr) merge'de tien PR's die Compose-schermen opsplitsen in scherpere componenten en rider- en driverprotocol­logica in een gedeelde `:common` coordinator-module onderbrengen. [PR #60](https://github.com/variablefate/ridestr/pull/60) voegt daarnaast een kind `3189` driver-ping receiver toe.

### Blossom drafts a BUD-01 Sunset header for blob expiration

[Blossom](https://github.com/hzrd149/blossom) opende [PR #99](https://github.com/hzrd149/blossom/pull/99) om een `Sunset`-header aan BUD-01 toe te voegen. Daarmee kan een server een toekomstige timestamp adverteren waarop een blob niet langer zal worden geserveerd, zodat clients kunnen plannen rond beperkte retention zonder eerst een 404 te moeten treffen.

## New Projects

### Forgesworn publishes a 29-repo cryptographic toolkit for Nostr

[Forgesworn](https://github.com/forgesworn) publiceerde in vijf dagen 29 open-source repositories rond signing, identity, attestations, web-of-trust en paid-API discovery op Nostr. De signing-stack rust op [nsec-tree](https://github.com/forgesworn/nsec-tree), een deterministic sub-identity derivation scheme, en op [Heartwood](https://github.com/forgesworn/heartwood), een NIP-46 remote signer die op een Raspberry Pi draait met Tor standaard aan. [Sapwood](https://github.com/forgesworn/sapwood), [heartwood-esp32](https://github.com/forgesworn/heartwood-esp32) en [nsec-tree-cli](https://github.com/forgesworn/nsec-tree-cli) vullen die signinglaag aan.

Aan identity- en trustzijde bracht [Signet](https://github.com/forgesworn/signet) [v1.6.0](https://github.com/forgesworn/signet/releases/tag/v1.6.0) uit als decentralized identity verification protocol, [nostr-attestations](https://github.com/forgesworn/nostr-attestations) definieert een kind `31000` credential-event en [nostr-veil](https://github.com/forgesworn/nostr-veil) bouwt een privacy-preserving web of trust met LSAG ring signatures. Aan monetisatiezijde levert [toll-booth](https://github.com/forgesworn/toll-booth) L402-middleware voor meerdere runtimes, [toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm) exposeert gated APIs als [NIP-90](/nl/topics/nip-90/) DVM en andere repos publiceren 402-service discovery op Nostr.

### ShockWallet ships Nostr-native Lightning wallet sync and multi-node connections

[ShockWallet](https://github.com/shocknet/wallet2) is een Lightning-wallet die Nostr als transport gebruikt voor verbinding met self-custodial Lightning-nodes. De app pairt via een `nprofile` met een of meer [Lightning.Pub](https://github.com/shocknet/Lightning.Pub)-nodes en signet betalingsautorisaties end-to-end tussen wallet en node. [PR #608](https://github.com/shocknet/wallet2/pull/608) leverde op 2026-04-18 een channels-dashboardpass, naast een admin-invite-link QR-flow en een readability-fix voor het metricsdashboard.

ShockWallet gebruikt [NIP-78](/nl/topics/nip-01/) application-specific data events voor multi-device wallet state sync, zodat dezelfde walletweergave tussen browser en telefoon consistent blijft zonder centrale syncserver. Dat plaatst het één laag onder [NIP-47](/nl/topics/nip-47/), dat een interface is voor apps om een bestaande wallet te vragen te betalen.

### Nostrability issues migrate to git over Nostr after GitHub censorship

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues), de interoperability tracker van elsat voor Nostr-clients en relays, migreert zijn issueworkflow naar git over Nostr nadat de GitHub-organisatie zonder antwoord van GitHub-support werd verwijderd. De tracker leeft nu op GitWorkshop/ngit zodat interop-issues op Nostr-native infrastructuur kunnen blijven bestaan.

### nowhere encodes full websites into URL fragments and routes orders through Nostr

[nowhere](https://github.com/5t34k/nowhere) is een nieuw AGPL-3.0-project van 5t34k dat complete websites serialiseert in het URL-fragment na `#`, comprimeert met dictionary substitution en raw DEFLATE en dan base64url-encodeert. Omdat browsers fragments niet naar servers sturen, ziet de host die de pagina levert de inhoud nooit. Voor dynamische sitetypen zoals stores, forums en petitions loopt live communicatie via Nostr relays met ephemeral keys en [NIP-44](/nl/topics/nip-44/) encryption.

### Small new surfaces: relayk.it and Brainstorm Search

Twee kleinere projecten verdienen nog een korte vermelding. [relayk.it](https://relayk.it), gebouwd door sam van het Soapbox-team, is een relay-discoveryclient gebouwd met Shakespeare die volledig in de browser draait. [Brainstorm Search](https://brainstorm.world) levert een single-page Nostr search UI gericht op content over het netwerk.

## Protocol and Spec Work

### NIP Updates

Recente voorstellen en discussies in de [NIPs-repository](https://github.com/nostr-protocol/nips):

**Open PRs and Discussions:**

- **[NIP-67](/nl/topics/nip-67/): EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): voegt een optioneel derde element toe aan `EOSE` zodat een relay kan signaleren of alle opgeslagen matches voor een filter zijn afgeleverd.
- **NIP-5D: Nostr Applets** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): stelt een nieuwe kind voor voor interactieve applets op Nostr, tussen [NIP-5A](/nl/topics/nip-5a/) en [NIP-5C](/nl/topics/nip-5c/) in.
- **NIP-29: Subgroups spec** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319)): breidt [NIP-29](/nl/topics/nip-29/) uit met een subgrouphiërarchie zodat één groep meerdere parallelle kanalen kan hosten.
- **NIP-29: Explicit role permissions on kind 39003** ([PR #2316](https://github.com/nostr-protocol/nips/pull/2316)): geeft clients expliciete permissieschema's voor rollen in relay-based groups.
- **NIP-11: access_control field for gated-relay discovery** ([PR #2318](https://github.com/nostr-protocol/nips/pull/2318)): voegt een adviserend `access_control`-object toe aan [NIP-11](/nl/topics/nip-11/).
- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): werkt verder aan kind `10164` voor payment gateway descriptors en per-tier subscription rules.
- **NIP-XX: Agent Reputation Attestations (Kind 30085)** ([PR #2320](https://github.com/nostr-protocol/nips/pull/2320)): stelt signed attestations voor over autonome agents en services op Nostr, relevant voor [NIP-90](/nl/topics/nip-90/) markten.
- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): bouwt verder op per-recipient [NIP-44](/nl/topics/nip-44/) encryptie voor gevoelige locatiegegevens.
- **marmot-ts 0.5.0 release PR** ([PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)): bundelt de eerste geplande breaking changes in de TypeScript Marmot-client, waaronder support voor zowel legacy kind `443` als nieuw kind `30443` voor KeyPackages.

## NIP Deep Dive: NIP-72 (Moderated Communities)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) definieert een model voor topic-based communities op Nostr waarin moderatoren een read view cureren over verder onbegrensde writes. Anders dan bij [NIP-29](/nl/topics/nip-29/) groups, waar de relay lidmaatschap en moderatie afdwingt, leeft een NIP-72-community in gewone Nostr-events en kan elke relay die de relevante kinds draagt die community serveren.

Een community wordt gedefinieerd door een kind `34550` addressable event van de maker. De `d`-tag bevat de slug, tags zoals `name`, `description`, `image` en `rules` dragen metadata, en `p`-tags met de marker `moderator` benoemen welke pubkeys approvals kunnen geven. Gebruikers dienen vervolgens gewone events in met een `a`-tag die verwijst naar de communitycoördinaat `34550:<creator_pubkey>:<slug>`. Moderatoren publiceren afzonderlijke kind `4549` approval-events die de submission via `e`, `p` en `a` refereren en een stringified kopie in `content` kunnen insluiten.

Dat model maakt moderatie transparant, forkable en herroepbaar op de readlaag. Dezelfde post kan door meerdere communities worden goedgekeurd, en approvals van een moderator tellen niet meer mee als die moderator later uit de actuele community definition verdwijnt. De tradeoff is dat submissions direct openbaar zijn en alleen op clientniveau worden verborgen als ze niet zijn goedgekeurd. Voor publieke topic communities werkt dat goed; voor omgevingen waar spam niet eens op de wire mag verschijnen blijft [NIP-29](/nl/topics/nip-29/) geschikter.

## NIP Deep Dive: NIP-57 (Zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md) definieert zaps: Lightning-betalingen gekoppeld aan Nostr-identiteiten en -events, plus een verifieerbaar payment receipt dat terug naar relays wordt gepubliceerd. De flow omvat drie systemen tegelijk: LNURL, Lightning en Nostr. De client van de afzender ontdekt het LNURL-endpoint van de ontvanger via profielmetadata of een `zap`-tag, tekent vervolgens een kind `9734` zap request en stuurt dat naar de LNURL-callback van de ontvanger. Na betaling publiceert de walletserver van de ontvanger een kind `9735` receipt naar de gevraagde relays.

Een geldig zap request bevat minimaal een `p`-tag met de pubkey van de ontvanger, een optionele `e`- of `a`-tag met het doel, een `amount`-tag in millisats en een `relays`-tag. Het zap receipt bevat daarna de stringified request in `description`, de betaalde invoice in `bolt11` en een `preimage` als betalingsbewijs. Een client die zaps correct wil tonen moet verifiëren dat de receipt-signatuur overeenkomt met de `nostrPubkey` uit de LNURL-respons, dat het invoicebedrag overeenkomt met de request, dat de description hash commit op het request en dat de `preimage` overeenkomt met de `payment_hash`.

Private zaps kunnen de `content` encrypten, en anonieme zaps gebruiken zelfs een nieuw ephemeral keypair voor het request zelf. [NIP-57](/nl/topics/nip-57/) vormt ook de basis van [NIP-75](/nl/topics/nip-75/): zap goals tellen gevalideerde `bolt11`-bedragen uit gematchte kind `9735` receipts op. Daarnaast laat een appendix zap splits toe, zodat een enkele betaling atomair over meerdere pubkeys kan worden verdeeld.

---

Dat is het voor deze week. Als je iets bouwt of nieuws te delen hebt, stuur ons een DM op Nostr of vind ons op [nostrcompass.org](https://nostrcompass.org).
