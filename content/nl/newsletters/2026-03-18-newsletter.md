---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [Amethyst](https://github.com/vitorpamplona/amethyst) landt volledige [NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect) methodeondersteuning, [Alby Hub](https://github.com/getAlby/hub) voegt meervoudige relay-ondersteuning toe in [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6), [Amber](https://github.com/greenart7c3/Amber) levert [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3) met ingebouwde Tor en fijnere signerrechten, en [Zeus](https://github.com/ZeusLN/zeus) verwijdert een riskant NWC keysend-pad in [PR #3835](https://github.com/ZeusLN/zeus/pull/3835). [Notedeck](https://github.com/damus-io/notedeck) levert een ondertekende updater in [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) die releases ontdekt via [NIP-94](/nl/topics/nip-94/) (File Metadata) events, terwijl [Damus](https://github.com/damus-io/damus) verouderde [NIP-65](/nl/topics/nip-65/) (Relay List Metadata) status repareert, [Nostrability Outbox](https://github.com/nostrability/outbox) zijn benchmarkresultaten herziet met gecorrigeerde data, en [Primal iOS](https://github.com/PrimalHQ/primal-ios-app) directe relay-abonnementen voor DM's test. [Primal Android](https://github.com/PrimalHQ/primal-android-app) levert [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7), [Route96](https://github.com/v0l/route96) levert [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0), [OpenChat](https://github.com/DavidGershony/openChat) blijft Marmot-interoperabiliteit aanscherpen in [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11), [Pika](https://github.com/sledtools/pika) consolideert zijn runtime in [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1), en [Nostria](https://github.com/nostria-app/nostria) voegt [NIP-85](/nl/topics/nip-85/) (Trusted Assertions) Web of Trust-filtering toe. Het NIPs-repository merget [NIP-54](/nl/topics/nip-54/) (Wiki) Djot-opmaak en een 5000-karakter invoerlimiet voor [NIP-19](/nl/topics/nip-19/) (Bech32-Encoded Entities), terwijl open voorstellen een `.nostrkey` bestandsformaat voor [NIP-49](/nl/topics/nip-49/) (Private Key Encryption), lidmaatschapsstatusconsistentie voor [NIP-43](/nl/topics/nip-43/) (Relay Access Metadata and Requests), verwijderingsrichtlijnen voor [NIP-17](/nl/topics/nip-17/) (Private Direct Messages), en een share-intent URI voor [NIP-222](/nl/topics/nip-222/) omvatten.

## Nieuws

### Wallet Connect-ondersteuning wordt breder, en walletclients verscherpen foutpaden

[Amethyst](https://github.com/vitorpamplona/amethyst), de Android-client onderhouden door vitorpamplona, mergede [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828), dat zijn [NIP-47](/nl/topics/nip-47/) implementatie dicht bij volledige protocoldekking brengt. De patch voegt `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`, hold invoice-methoden, keysend-ondersteuning met TLV-records, capability discovery via kind `13194` en notificatie-events op kind `23197` met [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads) toe. Dat geeft de client een veel breder NWC-oppervlak zonder te leunen op app-specifieke extensies.

De omringende walletstack bewoog in dezelfde richting. [Alby Hub](https://github.com/getAlby/hub), de self-custodial Lightning-node en walletservice achter veel NWC-deployments, leverde [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) met meervoudige relay-ondersteuning en eenvoudigere verbindings- en swapflows. [Zeus](https://github.com/ZeusLN/zeus), de mobiele Lightning-wallet, mergede [PR #3835](https://github.com/ZeusLN/zeus/pull/3835) dat NWC keysend-ondersteuning verwijdert nadat een stil fund-drain-pad in die flow was geïdentificeerd, terwijl ook pending-event en Cashu-activiteitsafhandeling werd gerepareerd. Walletconnectiviteit op Nostr wordt breder, en implementeerders verwijderen flows die moeilijk te beveiligen zijn.

### Notedeck verplaatst release-ontdekking naar Nostr

[Aansluitend op de Notedeck-berichtgeving van vorige week](/en/newsletters/2026-03-11-newsletter/), leverde [Notedeck](https://github.com/damus-io/notedeck), de native desktopclient van het Damus-team, [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) na het mergen van [PR #1326](https://github.com/damus-io/notedeck/pull/1326). De nieuwe updater abonneert op ondertekende kind `1063` release-events, matcht het lokale platform, downloadt het gerefereerde binaire bestand en verifieert de SHA256-hash voor installatie. Releasemetadata hoeft niet langer van de GitHub API of een projectwebsite te komen. Een vertrouwde release-pubkey en een relayverbinding zijn voldoende.

Dezelfde patch voegt een `notedeck-release` CLI toe die die events publiceert vanuit GitHub release-artefacten, wat betekent dat de release-pipeline nu zowel een Nostr-native publicatiepad als een Nostr-native ontdekkingspad heeft. Het brengt het Damus en Notedeck updater-model ook veel dichter bij Zapstore's relay-gepubliceerde ondertekende releaseflow: Zapstore's `zsp`-tooling verwerkt software-assets al als kind `1063` of `3063` events, dus dit pad is niet gekoppeld aan één client of één publisher. De rest van de release candidate is praktisch desktopwerk: followkolommen, profiel "View As User," [NIP-59](/nl/topics/nip-59/) (Gift Wrap) ondersteuning, realtime notestatistieken en [NIP-11](/nl/topics/nip-11/) (Relay Information Document) limietafhandeling, maar de updater is het deel dat waarschijnlijk deze ene releasecyclus zal overleven.

### Relaystatus beweegt dichter naar runtimegedrag

[Damus](https://github.com/damus-io/damus) mergede [PR #3665](https://github.com/damus-io/damus/pull/3665), dat een verouderd opgeslagen relaylijst-event-ID vervangt door een directe databasequery voor het nieuwste kind `10002` event. Wanneer de oude waarde verouderd raakte, konden relay-toevoeg- en verwijderoperaties terugvallen op bootstrap of een jaar oude lijsten, waardoor sommige relaywijzigingen leken te slagen terwijl de actieve status ongewijzigd bleef. [PR #3690](https://github.com/damus-io/damus/pull/3690) repareert een tweede foutpad door verouderde `lock.mdb`-status te verwijderen tijdens LMDB-compactie zodat de app niet crasht met `SIGBUS` bij de volgende start.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) opende [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194), dat direct abonneert op de [NIP-04](/nl/topics/nip-04/) (Encrypted Direct Messages) schrijfrelays van een chatpartner terwijl een gesprek open is, met de cacheserver als terugval. [Nostur](https://github.com/nostur-com/nostur-ios-public) opende [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53), dat gerandomiseerde relayscoring, [NIP-66](/nl/topics/nip-66/) liveness-filtering van nostr.watch en Thompson-sampling combineert om relayselectie te veranderen van een vaste heuristiek naar een geleerd beleid. Clients hebben relaykeuxe lang behandeld als configuratiedata. Meer apps behandelen het nu als live status die meet- en reparatielogica nodig heeft.

## Releases

### Primal Android 3.0.7

[Primal Android](https://github.com/PrimalHQ/primal-android-app), de Android-client van Primal, leverde [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7) met een nieuwe poll- en walletcyclus. [PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945) voegt zap-gebaseerd pollstemmen toe, [PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948) pagineert stemladingen zodat grotere polls bruikbaar blijven, en [PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965) haalt zapreceipts op voor alle transacties. Dezelfde release tagt ook ondersteunde events met [NIP-89](/nl/topics/nip-89/) (Recommended Application Handlers) clientmetadata in [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968), wat downstream clients helpt eventoorsprong schoner toe te schrijven.

### Amber v4.1.3

[Aansluitend op de Amber-berichtgeving van vorige week](/en/newsletters/2026-03-11-newsletter/), leverde [Amber](https://github.com/greenart7c3/Amber), de Android signer-app voor [NIP-55](/nl/topics/nip-55/) flows, [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3). De release bouwt voort op zijn recente [NIP-42](/nl/topics/nip-42/) relay-auth-werk met meer operationele verharding: [PR #327](https://github.com/greenart7c3/Amber/pull/327) voegt ingebouwde Tor toe naast Orbot-ondersteuning, [PR #324](https://github.com/greenart7c3/Amber/pull/324) vervangt grove NIP-gebaseerde versleutelingsrechten door inhoudtype-specifieke regels, en [PR #336](https://github.com/greenart7c3/Amber/pull/336) verwijdert netwerkrechten uit de offline-variant terwijl [PR #335](https://github.com/greenart7c3/Amber/pull/335) CI-controles toevoegt om dat zo te houden. [PR #322](https://github.com/greenart7c3/Amber/pull/322) verplaatst ook PIN-opslag naar versleutelde DataStore.

Deze release verscherpt de signergrens zelf. Dat is nuttig voor elke Android-flow die echte sleutels of relay-auth-beslissingen aan Amber overdraagt, omdat het moeilijke deel niet alleen is wat de signer kan doen. Het is ook hoe smal het kan worden afgebakend.

### Route96 v0.6.0

[Aansluitend op de Route96-berichtgeving van vorige week](/en/newsletters/2026-03-11-newsletter/), bracht [Route96](https://github.com/v0l/route96), de mediaserver die Blossom en [NIP-96](/nl/topics/nip-96/) (HTTP File Storage) ondersteunt, [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0) uit. De release verplaatst configuratie en whitelist-status naar de database met hot reload en voegt retentiebeleid toe voor koude of verouderende bestanden. Het voegt ook een rijker `GET /user/files` eindpunt plus bestandsstattracking voor downloads en egress toe, wat operators meer zichtbaarheid geeft in hoe hun opslagserver wordt gebruikt.

### OpenChat v0.1.0-alpha.11

[Aansluitend op de OpenChat-berichtgeving van vorige week](/en/newsletters/2026-03-11-newsletter/), leverde [OpenChat](https://github.com/DavidGershony/openChat), de Avalonia-gebaseerde chatclient gebouwd op de Marmot-stack, [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11) na een week snel protocolwerk. [Commit c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c) wrapt Welcome events in [NIP-59](/nl/topics/nip-59/) gift wrap en verwijdert oude MIP-00 tag-normalisatieshims, [commit 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1) voltooit de MIP-02 compliance-audit, en [commit 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f) doet hetzelfde voor MIP-03 groepsberichtversleuteling. [Commit 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547) consolideert ook NIP-44-afhandeling op de gedeelde marmot-cs-implementatie, wat het risico op client-side cryptodrift vermindert.

### nak v0.19.0 en v0.19.1

[nak](https://github.com/fiatjaf/nak), fiatjaf's commandoregel Nostr-toolkit, leverde [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0) en [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1). De 0.19-serie voegt een groepsforum-UI toe in [commit 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47), schakelt groepsmetadata-bewerkingen over naar een volledige vervangingsflow in [commit da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3), en vervangt de oudere `no-text`-afhandeling door `supported_kinds` in [commit bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf). Voor groepsimplementeerders houdt dat de CLI in lijn met de richting waarin groepsspecificaties en clients zich bewegen.

## Projectupdates

### Amethyst

[Aansluitend op de Amethyst-berichtgeving van vorige week](/en/newsletters/2026-03-11-newsletter/), bleef [Amethyst](https://github.com/vitorpamplona/amethyst), de Android-client met een van de breedste protocoloppervlakken in Nostr, bouwen op zijn wallet- en relaywerk na de NIP-47 patch. [PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853) voegt [NIP-45](/nl/topics/nip-45/) (Event Counting) COUNT-queries toe over relaybeherschermen, zodat gebruikers kunnen zien hoeveel events elke relay daadwerkelijk bevat voor homefeed, notificaties, DM's en indexdata. [PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849) voegt versleutelde bestandsuploads toe voor [NIP-17](/nl/topics/nip-17/) (Private Direct Messages) chats, met een retry-pad voor onversleutelde uploads wanneer een opslaghost de versleutelde versie weigert.

[PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791) brengt ook volledige [NIP-46](/nl/topics/nip-46/) (Nostr Connect) desktop bunker-login met een heartbeat-indicator, wat belangrijk is omdat remote signing-fouten vaak als willekeurige UI-storingen aanvoelen vanuit het perspectief van de gebruiker. De client toont of de signer actief is en hoe recent deze heeft geantwoord, terwijl het ook duidelijk maakt wanneer de huidige sessie een bunker gebruikt.

### Nostria

[Nostria](https://github.com/nostria-app/nostria), de multiplatformclient gebouwd rond een local-first-stack, mergede [PR #561](https://github.com/nostria-app/nostria/pull/561) dat Web of Trust-filtering toevoegt voor feeds en threadreacties. De functie gebruikt de bestaande trust-servicerangdata en stelt deze beschikbaar als zowel een feedfilter als een reactiefilter, waarbij auteurs wiens rang de drempel niet haalt worden verborgen terwijl de threadstructuur behouden blijft wanneer vertrouwde afstammelingen aanwezig zijn. Dat geeft gebruikers een middenlaag tussen "toon iedereen" en hardgecodeerde lijst-gebaseerde curatie.

Dezelfde week bracht ook [PR #563](https://github.com/nostria-app/nostria/pull/563), dat inhoudsfiltering en repost-ondersteuning toevoegt aan de overzichtspagina. Buiten de bijgehouden PR-lijst heeft Nostria ook meer van zijn power-usersurface ingevuld. Het ondersteunt nu de nieuwste Brainstorm Web of Trust-service met in-app aanmelding, samen met geld verzenden en ontvangen in DM's via NWC en BOLT-11 facturen. Het voegt ook Nostr-native GIF-afhandeling toe via de emoji NIP en een sterker RSS-importpad voor muzikanten dat bestaande Lightning-splits kan oppikken uit podcastfeeds. Nostria behandelt ranking, media, betalingen en publicatie als één verbonden appsurface.

### Nostur

[Nostur](https://github.com/nostur-com/nostur-ios-public), de iOS-client onderhouden door nostur-com, opende [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53) om outbox-routing te veranderen van een vast plan naar een gescoord beleid. De patch voegt gerandomiseerde relayscoring toe, [NIP-66](/nl/topics/nip-66/) relay liveness-filtering met een gecachte nostr.watch-feed, en Thompson-sampling zodat relay succes- en faaldata toekomstige selecties beïnvloedt. Het ontwerp behoudt een veiligheidsventiel wanneer te veel relays uitgefilterd zouden worden en bewaart `.onion`-relays. Dit is een van de duidelijkste huidige voorbeelden van een client die relayselectie behandelt als een adaptief systeem.

### Nostrability Outbox

[Aansluitend op het eerdere Outbox-benchmarkrapport](/nl/newsletters/2026-03-04-newsletter/), besteedde [Nostrability Outbox](https://github.com/nostrability/outbox), het benchmark- en analyseproject gericht op [NIP-65](/nl/topics/nip-65/) en [NIP-66](/nl/topics/nip-66/) clientrouting, de week aan het aanscherpen van zijn eigen claims. [PR #35](https://github.com/nostrability/outbox/pull/35) vervangt opgeblazen Thompson-samplingresultaten door een volledige herbenchmark over 1.511 runs en beveelt de `CG3`-variant aan voor NDK-stijl routing. [PR #43](https://github.com/nostrability/outbox/pull/43) voegt verval en use-case vergelijkingen toe, repareert een `0 follows` cache-poisoning bug, en herhaalt vervolgens de Telluride-dataset na het vastzetten van cache-TTL's.

Dat is geen productwerk in de gebruikelijke zin, maar het is belangrijk voor clientauteurs omdat de cijfers van het project nu scherper en minder vleiend zijn op de plekken waar ze eerder te veel hadden geclaimd. Het gecorrigeerde resultaat is nog steeds nuttig. Gerandomiseerde selectie blijft puur deterministische routing verslaan in de gevallen waar Outbox om geeft, Thompson-stijl leren kan de dekking aanzienlijk verbeteren wanneer clients nuttige relaygeschiedenis bewaren, en [NIP-66](/nl/topics/nip-66/) liveness-filtering vermindert verspilde tijd aan dode relays. Het werk vertaalt zich ook in concrete implementatievoorstellen, waaronder [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387), [Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53), [Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833), [rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282), [welshman #53](https://github.com/coracle-social/welshman/pull/53), en [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) plus [applesauce #55](https://github.com/hzrd149/applesauce/pull/55).

### White Noise backend

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), de Rust-backend gebruikt door White Noise en andere Marmot-tooling, mergede twee grensverhardingspatches rondom Blossom-mediaafhandeling. [PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637) dwingt HTTPS af op Blossom-URL's en voegt een uploadtimeout toe, terwijl [PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642) blobdownloads beperkt tot `100 MiB` om te voorkomen dat oversized mediapulls een denial-of-servicepad worden. Voor privéberichtensoftware zijn media-URL's een van de scherpste interfaces tussen versleutelde applicatielogica en onvertrouwde netwerkinfrastructuur. Deze week heeft het team die rand verscherpt.

### rust-nostr

[rust-nostr](https://github.com/rust-nostr/nostr), de Rust-protocolbibliotheek, mergede [PR #1280](https://github.com/rust-nostr/nostr/pull/1280) dat gemaksconstructors toevoegt voor `LocalRelayBuilderNip42`. De nieuwe lees- en schrijfhelpers geven embedded relay- en testopstellingen een duidelijkere manier om [NIP-42](/nl/topics/nip-42/) auth-beleid in code om te zetten. Dit is een kleine bibliotheekpatch, maar het is belangrijk voor teams die lokale of app-gebundelde relays bouwen die auth nodig hebben zonder elke keer boilerplate te herhalen.

### Pika

[Aansluitend op eerdere Pika-berichtgeving](/nl/newsletters/2026-03-04-newsletter/), leverde [Pika](https://github.com/sledtools/pika), de Marmot-gebaseerde berichtenapp, [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) en [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1) met een releasecyclus gericht op runtime-convergentie. [PR #542](https://github.com/sledtools/pika/pull/542) introduceert een gedeelde Marmot-runtimefaçade voor de CLI en sidecar, waarbij de apphost naar hetzelfde oppervlak verhuist. [PR #556](https://github.com/sledtools/pika/pull/556) verscherpt OpenClaw agent-levenscyclus en provisioningstatus, terwijl [PR #600](https://github.com/sledtools/pika/pull/600) herstel-van-back-up toevoegt en striktere herstelveiligheid voor beheerde omgevingen.

Het directe gebruikersgerichte oppervlak is hier kleiner dan in het vorige Pika-artikel, maar de architecturale verandering is betekenisvol. Het samenvoegen van groeps-, media-, bel- en sessielogica achter één gedeelde runtime vermindert de kans dat de app en daemon uit elkaar drijven naarmate de Marmot-stack groeit.

## NIP-Updates

Recente wijzigingen in het [NIPs-repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-54](/nl/topics/nip-54/) (Wiki): Overstap van Asciidoc naar Djot** ([PR #2242](https://github.com/nostr-protocol/nips/pull/2242)): Wiki-inhoud op kind `30818` gebruikt nu Djot als het canonieke opmaakformaat. De gemerge tekst voegt expliciet wikilinkgedrag toe, merge-request voorbeelden voor kind `818`, redirectvoorbeelden voor kind `30819` en niet-Latijnse normalisatievoorbeelden voor `d` tags. Dat geeft implementeerders een schoner parsedoel dan Asciidoc en verwijdert nog een specpad dat afhankelijk was van een Ruby-gecentreerde toolchain.

- **[NIP-19](/nl/topics/nip-19/) (Bech32-Encoded Entities): Invoerlimiet toevoegen** ([PR #2264](https://github.com/nostr-protocol/nips/pull/2264)): De specificatie beveelt nu aan om Bech32-gecodeerde entitystrings te beperken tot 5000 karakters. Dit is een kleine wijziging met echte parserwaarde, omdat NIP-19 strings nu verschijnen in QR-flows, deep links, deelschermen en door gebruikers geplakte invoer over veel clients.

**Open PR's en Discussies:**

- **Nostr Key File voor [NIP-49](/nl/topics/nip-49/) (Private Key Encryption)** ([PR #2269](https://github.com/nostr-protocol/nips/pull/2269)): Stelt een `.nostrkey` bestandsformaat voor voor wachtwoordversleutelde sleutelexport en -import. Indien gemerged zou het clients een normaler bestandsgebaseerd back-uppad geven dan het kopiëren van rauwe `ncryptsec`-strings.

- **Lidmaatschapsstatusconsistentie voor [NIP-43](/nl/topics/nip-43/) (Relay Access Metadata and Requests)** ([PR #2267](https://github.com/nostr-protocol/nips/pull/2267)): Voegt een sectie toe die verduidelijkt dat relays één autoritatieve lidmaatschapsstatus per pubkey moeten bijhouden. Dat zou groepsclientlogica rond lidmaatschapswijzigingen en afgespeelde geschiedenis vereenvoudigen.

- **Verwijderingsrichtlijnen voor [NIP-17](/nl/topics/nip-17/) (Private Direct Messages)** ([PR #2260](https://github.com/nostr-protocol/nips/pull/2260)): Stelt een concreet pad voor om privéberichten te bewerken en te verwijderen via gift-wrapped verwijderevents. Het werk is nog open, maar clientauteurs hebben hier een antwoord nodig als NIP-17 oudere DM-flows volledig gaat vervangen.

- **Share-intent URI voor [NIP-222](/nl/topics/nip-222/)** ([PR #2266](https://github.com/nostr-protocol/nips/pull/2266)): Het concept zou standaardiseren hoe mobiele en desktop-apps gedeelde inhoud in een Nostr-client overdragen. Dat is een van de ruwste interop-randen in huidige app-naar-app flows.

## NIP Deep Dive: NIP-94 (File Metadata)

[NIP-94](/nl/topics/nip-94/) definieert kind `1063` als een eerste-klas metadata-event voor een bestand. De [specificatie](https://github.com/nostr-protocol/nips/blob/master/94.md) geeft het event zijn eigen leesbare `content` plus machineleesbare tags voor download-URL, MIME-type, hashes, dimensies, previews, terugvallinks en opslagservicehints. Dit is belangrijk omdat het bestand doorzoekbaar wordt op relays als een eigen object. Een client hoeft geen metadata uit omringende inhoud te schrapen om te begrijpen wat het bestand is.

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

De tags doen meer werk dan het op het eerste gezicht lijkt. `x` identificeert het geserveerde bestand, terwijl `ox` het oorspronkelijke bestand identificeert voor eventuele server-side transformatie. De previewtags laten clients doorbladerbare bestandsindexen bouwen zonder het volledige asset te downloaden, en `summary` kan er een kort excerpt naast dragen. `fallback` geeft een tweede bron wanneer de hoofd-URL faalt, en `service` hint naar het opslagprotocol achter het bestand, zoals [NIP-96](/nl/topics/nip-96/) of een andere host. NIP-94 zit daarom onder sociale berichten en boven ruwe opslag. Het beschrijft het bestand, niet het gesprek rond het bestand.

Daarom is de Notedeck-updater van deze week interessant. [PR #1326](https://github.com/damus-io/notedeck/pull/1326) gebruikt ondertekende kind `1063` events voor software-releaseontdekking en verifieert vervolgens het gedownloade binaire bestand tegen de gepubliceerde SHA256. Dezelfde eventvorm kan een software-artefact of een media-upload beschrijven. NIP-94 is oud genoeg om stabiel te zijn, maar het heeft nog ruimte om te groeien omdat meer projecten metadata-events behandelen als transport voor machines, niet alleen als decoratie voor mensen.

## NIP Deep Dive: NIP-54 (Wiki)

[NIP-54](/nl/topics/nip-54/) definieert kind `30818` als een wiki-artikel-event. De [specificatie](https://github.com/nostr-protocol/nips/blob/master/54.md) behandelt de `d` tag als het genormaliseerde artikelonderwerp en laat veel auteurs items publiceren voor hetzelfde onderwerp. De artikeltekst staat in `content`, terwijl tags genormaliseerde identiteit, weergavetitel, samenvattingen en referenties naar eerdere versies afhandelen. Dat betekent dat NIP-54 niet alleen een inhoudformaat is. Het is ook een ophaal- en rangschikkingsprobleem, omdat elke client nog steeds moet beslissen welke artikelversie getoond wordt.

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

De merge deze week verandert de canonieke opmaak van Asciidoc naar Djot in [PR #2242](https://github.com/nostr-protocol/nips/pull/2242). Dat is belangrijk voor implementeerders omdat Djot een strakkere zelfstandige specificatie en een eenvoudiger parserverhaal over talen heen heeft. De gemerge tekst verduidelijkt ook hoe referentiestijl-wikilinks resolven, hoe merge-verzoeken kind `818` gebruiken, hoe redirects kind `30819` gebruiken, en hoe `d` tag-normalisatie zich moet gedragen voor niet-Latijnse schriften. Dat zijn de delen die twee onafhankelijke clients het eens laten worden over naar welk artikel een link verwijst.

NIP-54 zit ook op een ongebruikelijke plek in het protocol. Een wikiclient heeft contentrendering nodig, maar ook rangschikkingsbeleid. Reacties, relaylijsten, contactlijsten en expliciete eerbiedigingssignalen voeden allemaal in welk artikel wint voor een bepaald onderwerp. De Djot-overstap lost dat rangschikkingsprobleem niet op, maar verwijdert wel een van de parser-ambiguïteiten die eronder lagen. Daarom is de merge nu belangrijk: de verandering gaat minder over mooiere proseformattering en meer over het eenvoudiger maken van consistente multi-client wikifunctionaliteit.

Iets aan het bouwen, of wil je dat we het behandelen? Neem contact op via [NIP-17](/nl/topics/nip-17/) DM op Nostr op `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`.
