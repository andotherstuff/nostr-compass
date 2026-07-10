---
title: 'Nostr Compass #23'
date: 2026-05-21
publishDate: 2026-05-21
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-21-newsletter.md
translationDate: 2026-07-01
---

Primal 3.5 levert een herbouwde Android-shell, Amethyst voegt onchain Bitcoin zaps toe, White Noise krijgt markdown-rendering en deep links, Keycast passeert een security audit, en AgentNoise laat je lokale AI-coding agents besturen via Marmot-versleutelde chat. Hostr lanceert een P2P huuraccommodatieplatform op Nostr met vier concept-NIPs die listings, reserveringen en EVM-gebaseerde escrow behandelen. Angor migreert versleutelde berichten van NIP-04 naar NIP-44, Dart NDK voegt NIP-77 en een web signer toe, Alby js-sdk v8 levert native NWC multi-relay reconnect, en KeyChat verhelpt een forward secrecy-gat in Signal one-time prekey deletion. Aan de protocolzijde bereikt Mostro's anti-abuse bond fase 2, levert Wisp private replies en gift-wrapped reactions, en raakt een Namecoin NIP-05 implementatiegolf een half dozijn clients in één week.

## Belangrijkste verhalen

### Primal 3.5 voor Android

Primal, de social client ondersteund door zijn eigen caching relay-infrastructuur, bracht deze week [3.5.9](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.9) uit met een herbouwde applicatie-shell. Het redesign vervangt de vorige navigatiestructuur door een bijgewerkte lay-out en een nieuw Explore-scherm, waardoor het belangrijkste discovery-oppervlak zijn eigen dedicated home krijgt. De release voegt audio-afspelen toe voor link-previews, zodat audiobestanden ingebed in notes inline afspelen zonder de feed te verlaten. NIP-05 verificatie-badges tonen nu inline op profielen, waardoor identiteitsbevestiging in één oogopslag zichtbaar wordt. Notificatiefiltering kreeg een herziening, waarmee gebruikers kunnen beperken welke event-typen hun notificatielijst bereiken. De editor kreeg betere event-link handling en de onderliggende databaselaag ontving stabiliteitsfixes.

### White Noise: markdown, deep links en audio-metadata

White Noise, de Marmot-versleutelde groepsberichten-app gebouwd op Nostr en MLS ([RFC 9420](https://www.rfc-editor.org/rfc/rfc9420)), had een van zijn drukste weken tot nu toe over de frontend- en backend-repositories.

Aan de frontend voegt [PR #665](https://github.com/marmot-protocol/whitenoise/pull/665) volledige markdown-rendering voor chatberichten toe, zodat bold, italic, codeblokken en links nu native renderen in de berichtweergave. [PR #675](https://github.com/marmot-protocol/whitenoise/pull/675) activeert de leave-group flow die eerder was geblokkeerd voor niet-laatste admins, en [PR #661](https://github.com/marmot-protocol/whitenoise/pull/661) voegt native deep link-ondersteuning toe voor `whitenoise://` en `whitenoise-staging://` URIs voor gebruikers, chats en instellingen, zonder dat er HTTP redirect-infrastructuur nodig is.

Aan de backend in whitenoise-rs zorgt [PR #835](https://github.com/marmot-protocol/whitenoise-rs/pull/835) ervoor dat key package rotation goed werkt door de `d_tag` slot te hergebruiken voor kind:30443 publicaties, waardoor NIP-33 replaceable event-semantiek wordt ingeschakeld zodat opeenvolgende key package rotaties het vorige event op relays vervangen en alleen het huidige key package behouden. [PR #833](https://github.com/marmot-protocol/whitenoise-rs/pull/833) breidt `FileMetadata` uit met optionele `duration_ms` en `waveform` velden voor audiobijlagen, gecoördineerd met MDK's [PR #300](https://github.com/marmot-protocol/mdk/pull/300) die dezelfde velden toevoegt aan MIP-04 media-tags. Een nieuwe `whitenoise-markdown` crate ([PR #836](https://github.com/marmot-protocol/whitenoise-rs/pull/836)) vervangt de vorige nostr-sdk token parser door een dedicated markdown rendering library.

De Marmot protocolspecificatie zelf ontving een security fix in [PR #68](https://github.com/marmot-protocol/marmot/pull/68), die een security-probleem sluit door HKDF-SHA256 expliciet te specificeren voor image key derivations in MIP-01, waardoor ambiguïteit die tot implementatiedivergentie kon leiden wordt verwijderd. In MDK saneert [PR #307](https://github.com/marmot-protocol/mdk/pull/307) welcome failure reasons en beperkt de opgeslagen lengte, waarmee een aparte security-bevinding wordt gesloten.

### Amethyst v1.10.0: Onchain Bitcoin Zaps

Amethyst leverde deze week vier releases, met [v1.10.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.10.0) als het hoofdverhaal. De release voegt ondersteuning toe voor NIP-BC onchain Bitcoin zaps, waardoor gebruikers zaps kunnen verzenden, ontvangen en weergeven die direct onchain worden afgewikkeld via Bitcoin-transacties. Eerdere releases in de reeks verhielpen Blossom blob-detectie om niet-conforme bestandsnamen te weigeren ([v1.09.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.09.2)), patchten ProGuard-regels voor desktopbuilds, en mergeden pull request [#2977](https://github.com/vitorpamplona/amethyst/pull/2977) om onchain Bitcoin zappers te tonen als een dedicated ₿ rij in de uitgebreide reactions-galerij. Een in-progress on-chain transactiegeschiedenisscherm met paginering landde in [PR #2974](https://github.com/vitorpamplona/amethyst/pull/2974).

### AgentNoise: controleer coding agents via White Noise

[AgentNoise](https://github.com/nvk/agentnoise) door nvk is een Rust-native desktop-helper die je een telefoon met White Noise laat gebruiken als besturingsoppervlak voor lokale Codex- en Claude coding agent-sessies. De tool luistert naar een of meer White Noise chats, authenticeert afzenders via een first-pairing PIN-flow en start lokale coding agents via de geconfigureerde launcher. Het verzenden van `/claude <prompt>` vanaf je telefoon opent een nieuwe White Noise-werksessie genoemd naar de machine hostname en een korte prompt-samenvatting, en streamt vervolgens voortgangsupdates en eindresultaat terug naar die chat. Het is bewust Rust-first en houdt Node buiten het vertrouwde brugpad. Het project bereikte deze week [v0.1.24](https://github.com/nvk/agentnoise/releases/tag/v0.1.24), met kortere telefoon-leesbare antwoorden, jobreferenties op korte unieke prefix en een opt-in lokale sessie-watcher. AgentNoise stuurt de `wn` en `wnd` CLIs van `marmot-protocol/whitenoise-rs` aan als subprocessen, zodat het zijn Nostr-transport deelt met de White Noise-client zelf.

### Keycast security audit voltooid

[Keycast](https://github.com/marmot-protocol/keycast), de team-georiënteerde NIP-46 remote signing-server die Nostr private keys versleuteld at-rest opslaat in SQLite, voltooide in mei 2026 een security audit. De hardening-pass behandelde auth-, permission-, data-integriteit- en dependency-issues, en de resultaten zijn gedocumenteerd in [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md). Wijzigingen zijn onder meer: NIP-98 HTTP auth vereist nu precies één `u` tag en één `method` tag, wijst verouderde timestamps af en valideert `payload` hashes; de `ALLOWED_PUBKEYS` allowlist wordt exact geparsed en server-side afgedwongen; lege policies gaan nu standaard uit van deny voor sign/encrypt/decrypt verzoeken; foreign-key enforcement is ingeschakeld op SQLite-connecties; en geneste app-routes zoals `/teams/:id` worden server-side beschermd. Een SQL-migratie normaliseert oude allowed-kinds permission JSON bij opstart. Het project is nog in een vroeg stadium en de audit vermeldt overgebleven items voordat het kan worden vertrouwd met echte team-keys.

### Scramble: Marmot-client voor desktop en Android

[Scramble](https://github.com/DavidGershony/Scramble) (voorheen OpenChat) is een .NET/Avalonia desktop- en Android-client voor het [Marmot Protocol](/nl/topics/marmot/), die MIPs 00-04 implementeert: KeyPackage publishing (kind:30443), groepsmetadata met de NostrGroupData MLS-extensie, NIP-59 gift-wrapped welcome events (kind:444), ChaCha20-Poly1305 versleutelde berichten (kind:445) en Blossom versleutelde mediabijlagen. Het is volledig interop met White Noise en elke andere Marmot-compatibele client.

Het project leverde deze week 13 releases, met multi-device-ondersteuning als hoofdfunctie. Elk apparaat genereert een uniek KeyPackage-slot (een `d`-tag op kind:30443). Bij opstart haalt Scramble de eigen KeyPackages van de gebruiker op van relays, detecteert peer-device slot-IDs en voegt ze automatisch toe aan bestaande MLS-groepen met behulp van de staged commit-flow. Auto-add is beperkt tot groepen waar de huidige gebruiker admin is; niet-admin-groepen worden overgeslagen met begeleiding om de groepsadmin te vragen. Een forward-secrecy disclosure banner informeert nieuw-gekoppelde apparaten dat oude berichten niet beschikbaar zijn. Een slot-ID reconciliation pass (`TryReconcileSlotId`) verwerkt apparaten die vanaf pre-multi-device versies zijn gemigreerd door relay KeyPackage bytes te matchen tegen lokaal keymateriaal om de juiste `d`-tag over te nemen. External signer reconnect voor Amber- en NIP-46-gebruikers werd ook verholpen: de `IsConnected` guard die `ExternalSignerService`'s ingebouwde auto-reconnect blokkeerde werd verwijderd op alle negen call sites in `NostrService`.

### Hostr: P2P huuraccommodatie op Nostr

[Hostr](https://hostr.network) ([source](https://github.com/sudonym-btc/hostr)) is een peer-to-peer huuraccommodatieplatform volledig gebouwd op Nostr. Het bestrijkt de volledige Airbnb-achtige flow (zoeken en aanbieden van eigendommen, onderhandelen van reserveringen en afhandelen van betalingen) met behulp van vier concept-NIPs die het project parallel met de applicatie ontwikkelt.

De accommodation NIP breidt [NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md) classified listings (kind:30402 actief, kind:30403 concept) uit met accommodatie-specifieke tags voor type (`room`, `house`, `apartment`, `villa`, `hotel`, `hostel`, `resort`), check-in/check-out tijden, minimumverblijf en H3 geospatial cel-indexen voor locatie-gebaseerd zoeken op configureerbare precisie. De reservation NIP definieert een volledig onderhandelings- en levenscyclusprotocol: kind:32122 replaceable reservation events dragen een `d` trade ID, een listing anchor `a` tag en deelnemer `p` tags met rollen (`buyer`, `seller`, `escrow`); kind:1327 structured message rumors leveren private negotiate-stage tegenaanbiedingen via NIP-59 gift wraps zodat de onderhandeling buiten publieke relays blijft; kind:1326 append-only transition events creëren een openbaar audit trail zodra een reservering wordt vastgelegd. Koperprivacy wordt behouden via per-trade tijdelijke Nostr-sleutels gebonden aan de werkelijke identiteit van de koper via versleutelde `participant_proof` tags. De escrow NIP definieert kind:30303 escrow service advertisements en kind:17388 user trust declarations; de referentie-implementatie gebruikt EVM smart contracts op Rootstock, waarbij `contractBytecodeHash` clients in staat stelt te verifiëren dat het gedeployde contract overeenkomt met een bekende gecontroleerde implementatie. De marketplace listing NIP definieert generieke tags gedeeld over alle NIP-99 marktplaatsprofielen, waaronder `instantBook`, `negotiable`, `quantity`, `securityDeposit`, `cancellationPolicy` en `maxDisputePeriod`. Deze week bereidde het project zijn app store-indiening voor en mergde MCP client identity-ondersteuning voor agent-gerichte automatisering.

Twee nieuwe entries verschenen deze week op het Shakespeare MiniApps-platform: [InkPress](https://inkpress.shakespeare.wtf), een AI-magazine generator die gestructureerde tijdschriftachtige inhoud publiceert als Nostr events, en [PressStr](https://pressstr.shakespeare.wtf), een schrijf- en publicatieplatform voor de Soapbox-stack.

## Uitgebracht deze week

### ngit v2.4.4

**ngit** bracht [v2.4.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.4) uit met de toevoeging van `ngit sync --trust-server` (`-t`) voor gevallen waarin een git-server fast-forward voor loopt op Nostr-status. Wanneer deze situatie wordt gedetecteerd, rapporteert sync de betrokken refs en vereist de flag om een bijgewerkt state event te ondertekenen en publiceren; een `nostr.trust-server-domains` git config-instelling biedt een puntkomma-gescheiden allowlist voor servers die automatisch moeten worden vertrouwd zonder de flag.

### Amber v6.1.0-pre3 voegt PSBT signing toe

**Amber** bracht [v6.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre3) uit met verbeterde lay-out voor nieuwe appverbindingen, crashfixes en een select/deselect all optie op het permissions-scherm. [PR #438](https://github.com/greenart7c3/Amber/pull/438) voegt PSBT signing-ondersteuning toe via zowel de Intent-gebaseerde als de NIP-46 relay-gebaseerde paden, waardoor Amber Partially Signed Bitcoin Transactions kan ondertekenen zonder de nsec bloot te stellen aan de aanvragende app.

### Wisp v1.1.0 levert private replies en laat Amber-ondersteuning vallen

**Wisp** bracht [v1.1.0](https://github.com/barrydeen/wisp/releases/tag/v1.1.0) uit met private replies via NIP-17 gift wrap ([PR #540](https://github.com/barrydeen/wisp/pull/540)), gift-wrapped reactions en DIP-03 zaps op private replies ([PR #543](https://github.com/barrydeen/wisp/pull/543)), auto-translate voor notes ([PR #523](https://github.com/barrydeen/wisp/pull/523)) en een register-style fiat input op de zap-dialoog. [PR #541](https://github.com/barrydeen/wisp/pull/541) migreert private zaps van een eigen DM-relay plaintext-schema naar DIP-03 met correcte DM-relay routing. Dezelfde release-cyclus verwijderde NIP-55 remote signer-ondersteuning ([PR #531](https://github.com/barrydeen/wisp/pull/531)), waardoor Amber en andere externe signer-integraties werden gedropt, en verwijderde de bundled local relay ([PR #533](https://github.com/barrydeen/wisp/pull/533)). Wisp is een Nostr social client voor Android.

### Calendar by Formstr v1.5.4 verhelpt gift wrap voor nieuwe deelnemers

**Calendar by Formstr** bracht [v1.5.4](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.4) uit (de laatste in een v1.5.2 → v1.5.4 reeks). [PR #160](https://github.com/formstr-hq/nostr-calendar/pull/160) verhelpt een bug waarbij het bewerken van een private calendar event met nieuwe deelnemers het bijgewerkte event met de nieuwe pubkeys in `p` tags publiceerde maar nooit gift wrap uitnodigingen creëerde of leverde aan die deelnemers, wat de invite-flow voor last-minute toevoegingen brak. [PR #156](https://github.com/formstr-hq/nostr-calendar/pull/156) voegt error handling toe rond private event decryption zodat clients niet langer een fout gooien op niet-ontsleutelbare events, en [PR #138](https://github.com/formstr-hq/nostr-calendar/pull/138) corrigeert terugkerende event-tijden die over tijdzones dreven.

### Applesauce v6.1.0 voegt NIP-34 git casts en NIP-51 lookup relays toe

**Applesauce** bracht [v6.1.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.1.0) uit over zijn pakketten met significante NIP-34 (git-over-Nostr) ondersteuning: applesauce-common voegt nieuwe `GitRepository`, `GitGraspList` en `FavoriteGitRepos` casts toe plus bijbehorende factories, en exposeert `User.favoriteGitRepos$`, `User.gitAuthors$` en `User.graspServers$` reactieve properties zodat applicaties de gevolgde git-repos, repo-maintainers en geconfigureerde GRASP-servers van een gebruiker direct kunnen weergeven vanuit hetzelfde User-object. Dezelfde release voegt ondersteuning toe voor NIP-51 kind 10086 lookup relay-lijsten, een recente toevoeging aan de relay-list familie die wordt gebruikt om te ontdekken waar specifieke data te vinden is. applesauce-core krijgt `replaceableAddress` op `EventCast` voor NIP-01 replaceable address lookup, plus `pointer`, `kind` en een `getReplaceableAddressForEvent` helper, en voegt een `timeline$()` methode toe op de base `User` cast. [PR #73](https://github.com/hzrd149/applesauce/pull/73) verhelpt pool manual methods die stilletjes offline relays lieten wegvallen.

### Sprout v0.0.16 levert Sprig binary en huddle protocol v2

**Sprout** door Block, een self-hosted Nostr-relay-gebaseerde team-workspace waar mensen en AI-agents dezelfde ruimtes en event log delen, bracht [v0.0.16](https://github.com/block/sprout/releases/tag/v0.0.16) van de desktop-app uit naast rolling builds van de nieuwe Sprig all-in-one binary ([PR #605](https://github.com/block/sprout/pull/605)), die de ACP-harness, agent en developer MCP bundelt in één busybox-stijl binary voor eenvoudige deployment. De `--no-memory` flag toegevoegd in [PR #611](https://github.com/block/sprout/pull/611) laat operators NIP-AE core memory injection voor de ACP-harness uitschakelen. Aan de realtime kant breidt [PR #609](https://github.com/block/sprout/pull/609) het huddle voice-protocol uit naar een v2 frame header met ondersteuning voor tot 10 gelijktijdige peers.

### Nostrord v1.0.3 voegt OS-keychain en multi-account toe

**Nostrord** bracht [v1.0.3](https://github.com/nostrord/nostrord/releases/tag/v1.0.3) uit met lokale key-opslag gehard met OS-keychain en passphrase-fallback, multi-account-ondersteuning en een aantikbare bunker QR-code die op Android de signer-app opent.

### Angor migreert naar NIP-44 en levert security hardening

**Angor**, de Bitcoin crowdfunding-app gebouwd op Nostr en Taproot, bracht deze week drie unstable releases uit ([v0.2.24](https://github.com/block-core/angor/releases/tag/v0.2.24), [v0.2.25](https://github.com/block-core/angor/releases/tag/v0.2.25) en [v0.2.26](https://github.com/block-core/angor/releases/tag/v0.2.26)) met een set aan security hardening en Nostr-integratieveranderingen. [PR #860](https://github.com/block-core/angor/pull/860) migreert Nostr versleutelde berichten van NIP-04 naar NIP-44, waarbij het gedeprecieerde XOR-gebaseerde schema wordt vervangen door ChaCha20-Poly1305-versleuteling. [PR #861](https://github.com/block-core/angor/pull/861) staat Blossom media-uploads toe zonder een geselecteerde wallet door een kortstondige Nostr auth-sleutel te gebruiken, waardoor uploads worden gedeblokkeerd voor gebruikers die nog geen wallet hebben verbonden. De security-reeks behandelde meerdere gehardde categorieën: [PR #854](https://github.com/block-core/angor/pull/854) voegt type safety toe voor AngorKey en mnemonic memory protection, [PR #856](https://github.com/block-core/angor/pull/856) dwingt protocol-niveau validatie af voor timelocks, fee rates, dust thresholds en penalty rules, en [PR #851](https://github.com/block-core/angor/pull/851) past niet-brekende hardening toe over acht medium- en low-severity categorieën. [PR #859](https://github.com/block-core/angor/pull/859) verhelpt GrapheneOS-compatibiliteit door AOT-compilatie in te schakelen en runtime code generation te verwijderen, en [PR #855](https://github.com/block-core/angor/pull/855) voorkomt walletverlies bij Android swipe-kill door de walletstatus te persisteren voordat het OS het proces beëindigt.

### Alby js-sdk v8.0 levert NWC multi-relay reconnect

**Alby js-sdk** bracht de v8.0-lijn uit ([v8.0.1](https://github.com/getAlby/js-sdk/releases/tag/v8.0.1) tot en met [v8.0.3](https://github.com/getAlby/js-sdk/releases/tag/v8.0.3)) met NWC multi-relay subscription-ondersteuning. [PR #516](https://github.com/getAlby/js-sdk/pull/516) update de nostr-tools dependency en schakelt native auto-reconnect over meerdere relays in, waarbij de vorige polling-benadering wordt vervangen door relay-native reconnection-logica. [PR #542](https://github.com/getAlby/js-sdk/pull/542) vervangt alle `console.debug` calls door een injecteerbare logger-interface zodat applicatie-ontwikkelaars SDK-diagnostiek door hun eigen logging-infrastructuur kunnen routeren. De release laat de WebSocket-polyfill vallen en vereist Node.js 22 of hoger voor server-side consumers. v8.0.2 voegde een fix toe voor een utils crypto import bug die bepaalde bundlers brak.

### KeyChat v1.41.1 verhelpt forward secrecy

**KeyChat**, een berichten-app die het Signal-protocol combineert met Nostr relay-transport, bracht [v1.41.1+6513](https://github.com/keychat-io/keychat-app/releases/tag/v1.41.1+6513) uit. De belangrijkste fix dwingt forward secrecy af door Signal one-time prekeys onmiddellijk na een succesvolle decryptie te verwijderen, waardoor een gat wordt gesloten waarin een behouden prekey gebruikt kon worden om eerdere berichten te ontsleutelen als het apparaat later werd gecompromitteerd. De release voegt ook URL-preview toe voor berichten die uit één link bestaan, centraliseert media auto-download onder een nieuwe `FileDownloadManager` met een 20 MB automatische drempel en refactort NIP-11 relay info-fetching om een force-refresh bij cold start uit te voeren zodat betaalde relay fee-configuraties altijd correct worden geladen.

## In ontwikkeling

**Citrine** mergde [PR #151](https://github.com/greenart7c3/Citrine/pull/151) waarmee NIP-70 enforcement wordt geïmplementeerd: de Android-relay blokkeert nu reposts die beschermde event-inhoud embedden, zoals de spec vereist. [PR #149](https://github.com/greenart7c3/Citrine/pull/149) voegt weergave- en kopieeracties toe voor meerdere connectieadressen, localhost, lokaal Wi-Fi en Tor, vanuit het relay-instellingenscherm. [PR #141](https://github.com/greenart7c3/Citrine/pull/141) voegt NIP-42 AUTH challenge handling toe via externe signer-integratie met Amber.

**Mostro** bereikte fase 2 van zijn anti-abuse bond-uitrol. [PR #737](https://github.com/MostroP2P/mostro/pull/737) landt solver-gestuurde dispute slash-logica: admin-handlers consumeren nu de `BondResolution` payload van mostro-core, waardoor een admin de bond van beide partijen kan slashen bij het oplossen van een dispuut. Fase 1.5, gemerged in [PR #736](https://github.com/MostroP2P/mostro/pull/736), introduceerde een dedicated `PayBondInvoice` actie en `WaitingTakerBond` status, waarbij de anti-abuse bond-betaling van de taker wordt gescheiden van de trade-uitbetaling van de koper. De mobiele client voegde de volledige Phase 1.5 UX toe in [PR #592](https://github.com/MostroP2P/mobile/pull/592). Mostro is een peer-to-peer Bitcoin-uitwisselingsprotocol gebouwd op Nostr.

**Damus** mergde [PR #3773](https://github.com/damus-io/damus/pull/3773) waarmee de relay signal-indicator wordt hersteld, en [PR #3775](https://github.com/damus-io/damus/pull/3775) verhelpt relays die weigerden opnieuw te verbinden na een initiële verbindingsfout.

**rust-nostr** mergde [PR #1358](https://github.com/rust-nostr/nostr/pull/1358) waarmee event finalization-traits en NIP-specifieke event builders worden toegevoegd, waardoor het gemakkelijker wordt om correct-getypte events voor specifieke protocolfuncties te construeren. [PR #1363](https://github.com/rust-nostr/nostr/pull/1363) backport een fix die ervoor zorgt dat de NIP-46 signer zich abonneert op notificaties voordat het connect-antwoord wordt verzonden, waardoor een race condition wordt gesloten waarin client-berichten die onmiddellijk na connect binnenkomen konden worden gemist.

**dart-nostr** mergde [PR #44](https://github.com/ethicnology/dart-nostr/pull/44) met de toevoeging van een Namecoin `.bit` relay resolver en TLSA pin records, waardoor Flutter-applicaties `wss://example.bit/` relay-URLs kunnen oplossen via Namecoin DNS naar hun daadwerkelijke WebSocket-adressen.

**Dart NDK** (de Dart/Flutter Nostr development kit, nu op `relaystr/ndk`) mergde [PR #464](https://github.com/relaystr/ndk/pull/464) waarmee NIP-77, het offline event signing-protocol, wordt geïmplementeerd. Aan de signer-kant voegen [PR #602](https://github.com/relaystr/ndk/pull/602) en [PR #601](https://github.com/relaystr/ndk/pull/601) een web-specifieke event signer en een `PlatformEventVerifier` abstractie toe, waardoor Flutter web-apps de platform-signer kunnen gebruiken zonder een apart codepad; [PR #604](https://github.com/relaystr/ndk/pull/604) introduceert een event signer factory voor runtime signer-selectie. [PR #608](https://github.com/relaystr/ndk/pull/608) voegt `getDmRelays()` toe om de NIP-17 DM relay-lijst van een gebruiker op te halen (kind:10050), en [PR #600](https://github.com/relaystr/ndk/pull/600) verhelpt NIP-46 signed field preservation zodat remote signers geen velden verliezen bij round-trip.

**Pages by Form\*** ([repo](https://github.com/formstr-hq/nostr-docs)), Formstr's Nostr-native collaboratieve document-app gehost op [pages.formstr.app](https://pages.formstr.app), mergde deze week vier PRs die de flows voor versleutelde bijlagen en documentbeheer aanscherpen. [PR #37](https://github.com/formstr-hq/nostr-docs/pull/37) verhelpt ontbrekende afbeeldingen in DOCX, HTML en PDF exports door versleutelde bijlagen inline te plaatsen: het haalt `<encrypted-file>` blobs op van Blossom-servers, ontsleutelt ze met AES-GCM 256-bit met de opgeslagen sleutel en nonce, valideert het image MIME-type en converteert ze naar base64 data-URLs zodat exports afbeeldingen behouden die alleen in versleutelde vorm op Blossom bestaan. [PR #39](https://github.com/formstr-hq/nostr-docs/pull/39) voegt een lokaal document-zoekmechanisme toe, [PR #38](https://github.com/formstr-hq/nostr-docs/pull/38) ruimt de rename-flow op en [PR #40](https://github.com/formstr-hq/nostr-docs/pull/40) verhelpt shared backup handling.

**Zap Cooking** mergde [PR #396](https://github.com/zapcooking/frontend/pull/396), de eerste fase van een feed-herziening die feed-rendering primitieven legt zonder al enige door de gebruiker zichtbare wijziging. De PR introduceert een NIP-92 `imeta` tag parser die de `url`, `m` (MIME), `dim` (afmetingen), `blurhash`, `alt`, `x` (file hash) en `fallback` slots leest, plus een handmatig geporteerde canonieke blurhash decoder (~200 LOC) die PNG data-URLs produceert via canvas met een SSR-veilige null-fallback. Wanneer `imeta` tags ontbreken, valt de parser terug op het extraheren van ruwe afbeeldings- en video-URLs uit de event-inhoud met dezelfde heuristieken die de huidige feed al gebruikt.

**Nurunuru** (ぬるぬる, `tami1A84/null--nostr`), een Nostr-client met native Android-, iOS- en Web-varianten die een Rust FFI engine delen, mergde zijn v1.5.0 Native → Web sync in [PR #176](https://github.com/tami1A84/null--nostr/pull/176). De sync brengt verschillende feature-toevoegingen naar de Web-build die al op Android v1.4.9 en iOS 1.0.4 werden geleverd: de [NotificationModal](https://github.com/tami1A84/null--nostr/pull/176) toont nu birthday notifications, mutual-follow zap-detectie en custom-emoji reactie-notificaties; de reactie-picker laat de Unicode default-reactions quick-row vallen en centreert de UX op custom emoji; de recommendation engine in `lib/recommendation.js` filtert gebruikers zonder iconen of display names uit en prioriteert Following entries met Recommended die op de achtergrond laden. Voice input is de ene feature die de andere kant op gaat: de Web-build gebruikt al ElevenLabs Scribe streaming, en v1.5.0 sync partieel de Native-kant naar de OS-standaard `SpeechRecognizer` (Android) en `SFSpeechRecognizer` + `AVAudioEngine` (iOS) terwijl de volledige Native Scribe-integratie is uitgesteld tot v1.6.

## Protocol- en spec-werk

**PR [#2251](https://github.com/nostr-protocol/nips/pull/2251)** scherpt de NIP-70 protected events spec aan: er staat nu expliciet dat reposts die de volledige inhoud van een beschermd event embedden door relays moeten worden afgewezen. NIP-70 definieert de `-` tag die aangeeft dat een note-auteur niet toestaat dat zijn note wordt hergepubliceerd. De originele spec dekte relay filtering-gedrag, maar liet het repost-geval onduidelijk. Deze PR sluit dat gat. Citrine's [PR #151](https://github.com/greenart7c3/Citrine/pull/151) implementeert de enforcement aan de relay-kant in dezelfde week.

**PR [#1653](https://github.com/nostr-protocol/nips/pull/1653)** stelt een Drafts NIP voor voor het opslaan en synchroniseren van private draft events. Het voorstel gebruikt replaceable events met een `draft` status en NIP-44 versleuteling naar de eigen key van de auteur, waardoor clients works in progress naar relays kunnen opslaan zonder dat die events voor iemand anders zichtbaar zijn. Het draft event draagt de volledige beoogde-publicatie event als versleutelde inhoud, inclusief zijn uiteindelijke kind en tags.

**Snapshots ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279))** is een open voorstel om een immutable snapshot-event te definiëren voor het bewaren van één exacte versie van een replaceable Nostr-event. Het snapshot-event draagt de volledige inhoud van het replaceable event op een bepaald tijdstip, met een `a` tag die het terugkoppelt naar het adres van het replaceable event zodat alle historische versies samen opvraagbaar zijn. Dit maakt het mogelijk voor waarnemers om historische status te inspecteren, zelfs nadat relays oude versies niet meer bewaren.

**Namecoin NIP-05 golf:** Deze week was er een gecoördineerde push om `.bit` NIP-05 resolutie toe te voegen aan Nostr-clients. De NIP-discussiefeed legde open-source PRs vast tegen Aegis ([#14](https://github.com/ZharlieW/Aegis/pull/14), die sign-time verificatie bij de signer toevoegt), nostter ([#2128](https://github.com/SnowCait/nostter/pull/2128)) en dart-nostr ([#44](https://github.com/ethicnology/dart-nostr/pull/44)), naast een upstream NIP draft ([PR #2349](https://github.com/nostr-protocol/nips/pull/2349)). De Aegis PR is opmerkelijk omdat het verificatie aan de producentenkant plaatst: de signer controleert de Namecoin-chain voordat een kind:0 event dat een `.bit` identiteit claimt wordt ondertekend en waarschuwt de gebruiker bij een mismatch, waarbij het probleem wordt opgevangen voordat het event een relay bereikt.

## NIP Deep Dive: NIP-07 (window.nostr voor webbrowsers)

[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) definieert de `window.nostr` interface die browserextensies aan webapplicaties blootstellen. Het is de meest wijdverbreid gedeployde signer-interface op het web, geïmplementeerd door extensies waaronder Alby, nos2x, Flamingo en horse.

De interface heeft twee vereiste methoden en verschillende optionele. `window.nostr.getPublicKey()` retourneert de public key van de gebruiker als hex string zonder ooit de private key bloot te stellen aan de aanroepende pagina. `window.nostr.signEvent(event)` neemt een gedeeltelijk event met `created_at`, `kind`, `tags` en `content`, en retourneert het volledig ondertekende event met `id`, `pubkey` en `sig` toegevoegd. Het belangrijkste punt is dat de private key nooit de geïsoleerde context van de extensie verlaat; de webapplicatie dient een niet-ondertekend event in en ontvangt een ondertekende terug.

De optionele methoden dekken versleuteling: `window.nostr.nip04.encrypt` en `window.nostr.nip04.decrypt` voor het oudere NIP-04-schema (nu gedeprecieerd) en `window.nostr.nip44.encrypt` en `window.nostr.nip44.decrypt` voor het huidige NIP-44-schema. Extensies die NIP-44 ondersteunen kunnen daarom zowel direct message-versleuteling als elke andere applicatie die pubkey-gekoppelde versleuteling nodig heeft afhandelen zonder dat de aanroepende pagina de nsec ziet.

De spec bevat ook een aanbeveling aan extensie-auteurs: laad scripts met `"run_at": "document_end"` in het extensiemanifest zodat `window.nostr` synchroon beschikbaar is wanneer de pagina wordt geladen, waarmee race conditions worden vermeden waarbij een client `window.nostr` controleert voordat de extensie het heeft geïnjecteerd.

Een belangrijk voorbeeld van NIP-07 in actie is het Keycast-project dat hierboven werd behandeld. De Keycast web-frontend gebruikt NIP-07 om NIP-98 HTTP auth events te ondertekenen: de SvelteKit-app hanteert nooit de nsec van de gebruiker direct. Het roept `window.nostr.signEvent` aan om de auth-header te produceren en verzendt die header vervolgens naar de Keycast API. Deze architectuur betekent dat het key-materiaal in de browserextensie blijft gedurende de gehele team key management flow.

```json
{
  "id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 1,
  "tags": [],
  "content": "Hello from a NIP-07 signed event",
  "sig": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2cdd"
}
```

## NIP Deep Dive: NIP-39 (externe identiteiten in profielen)

[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) definieert hoe een Nostr-gebruiker controle over externe platform-identiteiten kan verklaren in zijn profiel. Elke verklaring gebruikt een `i` tag binnen een kind:10011 event, waarbij eigendom van een specifieke account op een ander platform wordt geclaimd samen met een bewijs dat onafhankelijk kan worden geverifieerd.

Elke tag volgt het formaat `["i", "platform:identity", "proof"]`, waarbij `platform:identity` de platformnaam en gebruikersnaam combineert met een dubbele punt als scheidingsteken (`github:semisol`, `twitter:semisol_public`). `proof` verwijst naar een verifieerbaar artefact op het platform zelf.

Voor GitHub is het bewijs een Gist ID. De gebruiker maakt een publieke Gist aan vanaf zijn GitHub-account met de tekst `Verifying that I control the following Nostr public key: npub1...`. Een client die de claim verifieert haalt `https://gist.github.com/<identity>/<proof>` op en controleert dat de Gist is geschreven door de geclaimde GitHub-gebruikersnaam en de verwachte pubkey bevat. Voor Twitter is het bewijs een tweet ID, voor Mastodon een post ID en voor Telegram een berichtreferentie in een publieke groep.

De identity provider-naam mag alleen `a-z`, `0-9` en de tekens `._-/` bevatten, en mag geen `:` bevatten. Identiteitsnamen moeten worden genormaliseerd naar kleine letters, waarbij de primaire alias wordt gebruikt wanneer er meerdere bestaan.

De Namecoin `.bit` NIP-05 discussie die deze week plaatsvindt laat de rol van NIP-39 in de bredere identiteitsstack zien: het biedt een gestandaardiseerde, relay-agnostische manier om een Nostr-sleutel te kruisverwijzen met een gevestigde identiteit elders, zonder dat er een centrale verificatie-autoriteit nodig is. Een client kan het bewijs onafhankelijk verifiëren door een publiek artefact op het genoemde platform op te halen, en het bewijs is gebonden aan de specifieke Nostr-pubkey in de Gist- of tweet-tekst, niet aan een generieke platform-credential.

```json
{
  "id": "b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 10011,
  "tags": [
    ["i", "github:semisol", "9721ce4ee4fceb91c9711ca2a6c9a5ab"],
    ["i", "twitter:semisol_public", "1619358434134196225"],
    ["i", "mastodon:bitcoinhackers.org/@semisol", "109775066355589974"]
  ],
  "content": "",
  "sig": "1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3eff"
}
```

---

Dat was het voor deze week. Als je iets aan het bouwen bent of nieuws hebt om te delen, DM ons op Nostr of vind ons op [nostrcompass.org](https://nostrcompass.org).
