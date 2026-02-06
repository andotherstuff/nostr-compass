---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** rust-nostr levert een grote API-herontwerp met 21 PR's die de architectuur van de SDK herzien. Nostria 3.0 lanceert met dual pane navigatie, lijstbeheer en een complete UI-herziening. Vector voegt SIMD-versnelling toe met 65x-184x snelheidswinst en levert [Marmot](/nl/topics/marmot/)-protocolondersteuning voor versleutelde groepsberichten. Frostr brengt threshold signing naar iOS via TestFlight. Damus implementeert [NIP-19 (Bech32 Gecodeerde Entiteiten)](/nl/topics/nip-19/) relay hints voor cross-relay content discovery. Primal Android voegt NWC-encryptie en wallet-transactie-exports toe. nostr-tools en NDK ontvangen betrouwbaarheidsverbeteringen. NIP-82 (Software Applications) breidt uit naar 98% van apparaatplatforms. De NIPs-repository merget hold invoice-ondersteuning voor [NIP-47 (Nostr Wallet Connect)](/nl/topics/nip-47/). Nieuwe protocolvoorstellen omvatten NIP-74 voor podcasting, NIP-DB voor browser event databases, en een TRUSTed Filters-suite voor gedecentraliseerde contentcuratie. Nieuwe projecten zijn Instagram to Nostr v2 voor contentmigratie, Pod21 die een gedecentraliseerde 3D-printmarktplaats lanceert, Clawstr die AI agent-beheerde communities introduceert, en Shosho en NosCall die livestreaming en videobellen uitbreiden.

## Nieuws

### rust-nostr Levert Grote API-Herontwerp

De [rust-nostr](https://github.com/rust-nostr/nostr) SDK onderging deze week een significante architectuurherziening met 21 gemerged PR's die breaking changes introduceren door de hele library. Het herontwerp raakt kern-API's waar de meeste Rust-ontwikkelaars op vertrouwen.

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245) herontwerpt notificatie-API's, terwijl [PR #1244](https://github.com/rust-nostr/nostr/pull/1244) `RelayNotification::Shutdown` vervangt door `RelayStatus::Shutdown` voor schonere state handling. De signer-API's sluiten nu aan bij andere SDK-patronen via [PR #1243](https://github.com/rust-nostr/nostr/pull/1243). Client- en Relay-methodes kregen opschoning in [PR #1242](https://github.com/rust-nostr/nostr/pull/1242), en client options gebruiken nu een builder pattern ([PR #1241](https://github.com/rust-nostr/nostr/pull/1241)).

Bericht-verzend-API's werden herontworpen in [PR #1240](https://github.com/rust-nostr/nostr/pull/1240), REQ-uitschrijving in [PR #1239](https://github.com/rust-nostr/nostr/pull/1239), en relay-verwijdering in [PR #1229](https://github.com/rust-nostr/nostr/pull/1229). Een [open PR #1246](https://github.com/rust-nostr/nostr/pull/1246) voegt ondersteuning toe voor blocking API's om het herontwerp af te ronden.

De wijzigingen brengen consistentie naar de SDK maar vereisen migratie-inspanning van bestaande projecten. Ontwikkelaars die bouwen op rust-nostr moeten de changelog zorgvuldig doornemen voor upgraden.

### Instagram to Nostr v2 Maakt Contentmigratie Mogelijk

Een nieuwe tool stelt creators in staat om hun bestaande content te migreren van gecentraliseerde platforms naar Nostr. [Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2) ondersteunt importeren van Instagram, TikTok, Twitter en Substack zonder toegang tot de private keys van de gebruiker te vereisen.

De tool adresseert een veelvoorkomende onboardingbarrière: gebruikers die aarzelen om opnieuw te beginnen op een nieuw platform kunnen nu hun contentgeschiedenis behouden. Het ondersteunt ook het schenken van Nostr-accounts aan nieuwe gebruikers of het voorstellen van content aan bestaande accounts, wat het bruikbaar maakt om anderen te helpen overstappen naar het protocol.

### Pod21: Gedecentraliseerd 3D-Printnetwerk

[Pod21](https://github.com/gobrrrme/Pod21) ([pod21.com](https://pod21.com)) verbindt 3D-printeroperators met kopers via Nostr voor marktplaatscoördinatie. Het platform bevat een [NIP-17 (Privéberichten)](/nl/topics/nip-17/)-compatibele DM-bot die marktplaatsinteracties afhandelt, waardoor kopers prints kunnen aanvragen en onderhandelen met makers via versleutelde directe berichten.

Makers vermelden hun printcapaciteit en mogelijkheden; kopers bladeren door listings en initiëren orders via de bot. De architectuur volgt een vergelijkbaar patroon als andere Nostr-commerceapplicaties: relay-gebaseerde ontdekking, versleutelde berichten voor ordercoördinatie en Lightning voor afwikkeling. Pod21 voegt zich bij Ridestr en Shopstr als Nostr-applicaties die real-world transacties coördineren via het protocol.

### Clawstr: AI Agent Sociaal Netwerk

[Clawstr](https://github.com/clawstr/clawstr) lanceert als een Reddit-geïnspireerd platform waar AI-agents communities creëren en beheren op Nostr. Het platform stelt autonome agents in staat om thematische communities op te zetten, content te cureren en met gebruikers te interacteren. Communities functioneren als subreddits maar met AI-moderators en -curators die discussies begeleiden. De architectuur gebruikt Nostr's open protocol voor agent-to-agent en agent-to-human interacties, wat een nieuw model vestigt voor communityvorming op gedecentraliseerde sociale media.

## Releases

### Ridestr v0.2.0: RoadFlare Release

[Ridestr](https://github.com/variablefate/ridestr) leverde [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0), genaamd de "RoadFlare Release," met persoonlijke rideshare-netwerken. De feature laat passagiers favoriete chauffeurs toevoegen aan een vertrouwd netwerk. Chauffeurs keuren volgers goed en delen versleutelde locaties, waardoor passagiers kunnen zien wanneer vertrouwde chauffeurs online en in de buurt zijn. Ritaanvragen gaan direct naar bekende chauffeurs.

Betalingsbetrouwbaarheid verbeterde met automatisch escrow-herstel, betere wallet-sync tussen apparaten en snellere betalingsverwerking via progressive polling. [PR #37](https://github.com/variablefate/ridestr/pull/37) voegt de Fase 5-6 infrastructuur toe die deze features ondersteunt. [v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1) volgde met hotfixes voor betalingsdialoog-bugs en de "Toevoegen aan Favorieten"-flow na de rit.

### Nostria 3.0

[Nostria](https://github.com/nostria-app/nostria), sondreb's cross-platform client gebouwd voor wereldwijde schaal, leverde versie 3.0 met een complete UI-herziening, nieuw logo en honderden fixes. De release vertegenwoordigt een intensieve zes-weken ontwikkelcyclus.

Dual pane navigatie is de grootste UX-wijziging, waardoor desktopgebruikers minder hoeven te wisselen tussen lijsten, details en threads. Een nieuwe Home-sectie biedt een overzicht van alle beschikbare features, en alle schermen delen een uniforme toolbar, layout en functionaliteit.

Lijstbeheer is de meest significante feature-update, geïntegreerd door de hele applicatie. Gebruikers kunnen profiellijsten beheren en content filteren in elke feature: Streams, Music of Feeds. Last van spam in threads? Filter op favorieten om alleen hun replies te zien. Quick Zaps voegt one-tap zapping toe met configureerbare waarden. Copy/Screenshot genereert clipboard-screenshots voor het delen van events overal. Muted Words filtert nu op profielvelden (name, display_name, NIP-05), waardoor gebruikers alle gebridgede profielen kunnen blokkeren met een enkel geblokkeerd woord. Settings werd doorzoekbaar voor snellere configuratiewijzigingen.

De release voegt BOLT11 en BOLT12 betalingsverzoek-rendering toe, tekstgrootte- en lettertypeselectie, en "Note-to-Self"-berichten in de Messages-sectie met rendering van gerefereerde content zoals artikelen en events. De nieuwe Share-dialoog maakt snel delen mogelijk via e-mail, websites of directe berichten naar meerdere ontvangers. Extra features zijn aangepaste emoji-sets, Interests (hashtag-lijsten als dynamische feeds), Bookmarks, Public Relay Feeds en volledige menu-aanpassing inclusief welke optie het Nostria-icoon opent.

Beschikbaar op Android, iOS, Windows en web op [nostria.app](https://www.nostria.app/).

### Applesauce v5.1.0

hzrd149's [Applesauce](https://github.com/hzrd149/applesauce) library-suite releasede v5.1.0 over alle packages. [applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0) voegt ondersteuning toe voor `switch_relays` en `ping` methodes op Nostr Connect remote signers, bruikbaar voor het programmatisch beheren van signer-verbindingen. [applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0) introduceert `loadAsyncMap` voor parallel async laden. [applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0) voegt padding-argumenten toe aan `useAction().run()`. [applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0) updatet event-to-store mapping om strings direct te verwerken zonder `onlyEvents` te vereisen.

### nak v0.18.3

fiatjaf's [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) bereikte [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) met stabiliteitsfixes van mattn. De release voorkomt panics wanneer mint-URL's de `://` separator missen, valideert dateparser-fouten voor het gebruiken van datumwaarden, en handelt edge cases af in AUTH challenge tag parsing. Deze defensieve fixes maken de CLI robuuster bij het verwerken van malformed inputs.

### Aegis v0.3.7

[Aegis](https://github.com/ZharlieW/Aegis), de cross-platform desktop signer, leverde [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7) met Nostr App Browser-ondersteuning met [NIP-07 (Browser Extension Interface)](/nl/topics/nip-07/) signing. De release registreert [NIP-04 (Versleutelde Directe Berichten)](/nl/topics/nip-04/) en [NIP-44 (Versioned Encryption)](/nl/topics/nip-44/) encryptie-events, waardoor gebruikers kunnen tracken welke applicaties encryptie-operaties aanvragen. Het browser-segment filtert nu op platform om alleen web-apps te tonen.

### Bitchat v1.5.1 (iOS)

[Bitchat](https://github.com/permissionlesstech/bitchat), de offline-capable messaging app die Nostr en Bluetooth mesh gebruikt, releasede [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1) met iOS-beveiligingsverharding. [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) valideert Nostr event-handtekeningen voor verwerking, verwerpt ongeldige giftwraps en embedded packets, capt oversized payloads en blokkeert gespoofde BLE announce sender ID's. [PR #998](https://github.com/permissionlesstech/bitchat/pull/998) fixt iOS BLE mesh-authenticatie door sender ID's te binden aan connection UUID's, wat identiteitsspoofing in het mesh-netwerk voorkomt. [PR #972](https://github.com/permissionlesstech/bitchat/pull/972) voegt notificatie rate limiting toe om peer discovery floods te voorkomen wanneer meerdere mesh-apparaten in de buurt zijn.

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app) releasede [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495) met [NIP-47](/nl/topics/nip-47/) Nostr Wallet Connect-ondersteuning via [PR #148](https://github.com/keychat-io/keychat-app/pull/148). Gebruikers kunnen nu externe Lightning-wallets verbinden voor betalingen binnen de messaging-app. De release voegt ook macOS desktop-notificaties toe.

### Nostrmo v3.5.0

[Nostrmo](https://github.com/haorendashu/nostrmo), de cross-platform Flutter-client, leverde [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0) met een herziening van het feedsysteem. De update vervangt vaste feeds door aanpasbare alternatieven: General Feed, Mentioned Feed en Relay Feed, elk configureerbaar via nieuwe bewerkingspagina's. De release implementeert outbox-modelondersteuning voor betere event-routing en breidt lokale relay-functionaliteit uit met configureerbare groottelimieten en abonnementsondersteuning.

### Shosho v0.11.1

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), de livestreaming-app voor Nostr, releasede [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1) met opname- en VOD-mogelijkheden. De update voegt room presence-indicatoren toe die tonen wie streams bekijkt, threaded chat-conversaties voor betere discussie-organisatie, en Nostr Connect-ondersteuning op iOS via [NIP-46](/nl/topics/nip-46/). Streamers kunnen nu hun uitzendingen opslaan voor later bekijken terwijl ze realtime chatinteracties met hun publiek behouden.

### NosCall v0.5.0

[NosCall](https://github.com/sanah9/noscall), de audio- en videobel-app voor Nostr, leverde [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release) met contactgroepen voor het organiseren van gesprekken per categorie, relaybeheer voor verbindingsoptimalisatie en configureerbare ICE-serverinstellingen voor verbeterde NAT-traversal. De release voegt ook dark mode-ondersteuning toe. NosCall gebruikt Nostr voor call signaling en coördinatie, wat peer-to-peer gesprekken mogelijk maakt zonder gecentraliseerde servers.

### diVine 1.0.4

[diVine](https://github.com/divinevideo/divine-mobile), rabble's korte-video-client met looping, releasede [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4) als Android pre-release alpha voorafgaand aan de Zapstore-indiening. De release richt zich op het testen van Nostr-sleutelbeheer, inclusief nsec-import, [NIP-46 (Nostr Connect)](/nl/topics/nip-46/) remote signing met nsecBunker en Amber, en nostrconnect:// URL-handling. Het team vraagt feedback over relay-compatibiliteit en video-interoperabiliteit met andere clients. [PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265) fixt iOS-bestandspadafhandeling die videoclips onbruikbaar maakte na app-updates door relatieve paden op te slaan in plaats van absolute containerpaden. [PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251) fixt navigatieproblemen bij het bekijken van profielen vanuit reacties.

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus) leverde [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2) als stabiele release, die de [NWC-fixes behandeld in vorige edities](/nl/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---nwc-fixes) consolideert.

### Frostr Igloo iOS TestFlight

[Frostr](https://github.com/FROSTR-ORG) ([frostr.org](https://frostr.org/)) lanceerde [Igloo voor iOS](https://github.com/FROSTR-ORG/igloo-ios) op [TestFlight](https://testflight.apple.com/join/72hjQe3J), wat threshold signing uitbreidt naar Apple-apparaten. Frostr gebruikt FROST (Flexible Round-Optimized Schnorr Threshold) handtekeningen om nsec-sleutels op te splitsen in shares verdeeld over apparaten, wat k-of-n signing met fouttolerantie mogelijk maakt. Gebruikers die in "demo mode" meedoen nemen deel aan een live 2-of-2 threshold signature experiment, wat de realtime coördinatiemogelijkheden van het protocol demonstreert. De iOS-release voegt zich bij [Igloo voor Android](https://github.com/FROSTR-ORG/igloo-android) (v0.1.2), die in december werd geleverd met [NIP-55 (Android Signer)](/nl/topics/nip-55/)-ondersteuning voor cross-app signing requests. Beide mobiele clients complementeren [Igloo desktop](https://github.com/FROSTR-ORG/igloo-desktop) en de [Frost2x](https://github.com/FROSTR-ORG/frost2x) browser-extensie.

## Projectupdates

### Damus Implementeert NIP-19 Relay Hints

[Damus](https://github.com/damus-io/damus) mergede [PR #3477](https://github.com/damus-io/damus/pull/3477), die [NIP-19](/nl/topics/nip-19/) relay hint-consumptie implementeert voor event-fetching. De feature maakt het bekijken van notities mogelijk op relays die niet in de geconfigureerde pool van de gebruiker zitten door hints te extraheren uit [NIP-10 (Reply Threads)](/nl/topics/nip-10/), [NIP-18 (Reposts)](/nl/topics/nip-18/) en NIP-19-referenties. De implementatie gebruikt efemere relay-verbindingen met reference-counted cleanup, waarmee permanente relay pool-uitbreiding wordt vermeden.

Aanvullende fixes omvatten Lightning invoice-parsing ([PR #3566](https://github.com/damus-io/damus/pull/3566)), wallet view-laden ([PR #3554](https://github.com/damus-io/damus/pull/3554)), relay list-timing ([PR #3553](https://github.com/damus-io/damus/pull/3553)), en profiel-preloading om visueel "poppen" te verminderen ([PR #3550](https://github.com/damus-io/damus/pull/3550)). Een [draft PR #3590](https://github.com/damus-io/damus/pull/3590) toont [NIP-17](/nl/topics/nip-17/) privé-DM-ondersteuning in ontwikkeling.

### Primal Android Levert NWC-Encryptie

[Primal Android](https://github.com/PrimalHQ/primal-android-app) had een zeer actieve week met 18 gemerged PR's gericht op wallet-infrastructuur. De app integreert nu met Spark, Lightspark's self-custodial Lightning-protocol. [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) voegt NWC-encryptie-ondersteuning toe, terwijl [PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872) NWC info-events verstuurt wanneer verbindingen tot stand komen.

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870) maakt CSV-export voor wallet-transacties mogelijk, bruikbaar voor boekhoud- en belastingdoeleinden. [PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716) voegt een lokale accountwisselaar toe in de Note Editor. Meerdere wallet-herstelfixes ([PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876), [PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875), [PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)) adresseren edge cases voor gebruikers met niet-Spark wallet-configuraties.

### Marmot TypeScript SDK Voegt Berichtgeschiedenis Toe

De TypeScript-implementatie van het [Marmot](https://github.com/marmot-protocol/marmot)-protocol zet ontwikkeling voort. [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) door hzrd149 implementeert berichtgeschiedenis-persistentie met paginering voor de referentie chatapplicatie, terwijl [PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39) de library-ergonomie verbetert.

Aan de Rust-kant implementeert [PR #161](https://github.com/marmot-protocol/mdk/pull/161) herhalbare state-handling om berichtcontext te behouden bij falen, en [PR #164](https://github.com/marmot-protocol/mdk/pull/164) schakelt over naar std::sync::Mutex om tokio-panics met SQLite te vermijden. De whitenoise-rs backend voegt [Amber-integratie](https://github.com/marmot-protocol/whitenoise-rs/pull/418) toe ([PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)), [upgradet naar MDK en nostr-sdk 0.44](https://github.com/marmot-protocol/whitenoise-rs/pull/467) ([PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)), en introduceert realtime notification streaming via [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460) met NewMessage en GroupInvite event types.

### HAVEN Voegt Periodieke WoT-Refresh Toe

[HAVEN](https://github.com/bitvora/haven), de persoonlijke relay, mergede [PR #108](https://github.com/bitvora/haven/pull/108) met periodieke [Web of Trust](/nl/topics/web-of-trust/)-refresh. De feature zorgt ervoor dat vertrouwensscores actueel blijven naarmate de sociale grafieken van gebruikers evolueren, wat de nauwkeurigheid van spamfiltering verbetert.

### nostr-tools

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), de kern JavaScript-library, ontving meerdere verbeteringen deze week. Commits omvatten een [fix voor hashtag-parsing na newlines](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5) in [NIP-27 (Tekstnotitiereferenties)](/nl/topics/nip-27/) mentions, [automatische pruning van kapotte relay-objecten met idle tracking](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2) voor verbindingsopruiming, [verwijdering van message queue](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638) voor single-threaded prestatieoptimalisatie, en [source file exports](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139) voor betere TypeScript-imports.

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk) leverde [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0) met een [fix voor reconnection na device sleep/wake-cycli en stale connection handling](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3), wat betrouwbaarheidsproblemen voor mobiele applicaties aanpakt.

### Notedeck

[Notedeck](https://github.com/damus-io/notedeck), de desktopclient van het Damus-team, heeft een [open PR #1279](https://github.com/damus-io/notedeck/pull/1279) die een [NIP-34 (Git-samenwerking)](/nl/topics/nip-34/) viewer toevoegt. Dit zou het browsen van git-repositories, patches en issues gepubliceerd op Nostr relays direct binnen de client mogelijk maken, wat Notedeck een potentiële front-end maakt voor ngit-gebaseerde workflows.

### njump

[njump](https://github.com/fiatjaf/njump), de Nostr web-gateway, voegde ondersteuning toe voor twee [NIP-51 (Lists)](/nl/topics/nip-51/) event types via [PR #152](https://github.com/fiatjaf/njump/pull/152). De gateway rendert nu kind:30000 Follow Sets, die gecategoriseerde groeperingen van gebruikers zijn die clients in verschillende contexten kunnen weergeven, en kind:39089 Starter Packs, die gecureerde profielcollecties zijn ontworpen voor delen en groepsvolgen. Deze toevoegingen laten njump community-gecureerde lijsten weergeven wanneer gebruikers nevent-links delen.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), de Android-client, fixte een bug die het delen van video's vanuit de speler-weergave verhinderde ([PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)). De "Video delen"-optie verscheen niet omdat de content-parameter niet werd doorgegeven aan de controleknoppencomponent. Gebruikers kunnen nu Nostr-videocontent delen naar andere apps direct vanuit de speler. [PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693) fixt Jackson JSON-deserialisatiecrashes die optraden bij het parsen van bepaalde malformed events.

### Jumble

[Jumble](https://github.com/CodyTseng/jumble), de webclient gericht op relay feed-browsen, voegde audiobestand-uploads via clipboard toe in [PR #743](https://github.com/CodyTseng/jumble/pull/743). Gebruikers kunnen nu audiobestanden direct in de post-editor plakken, die ze uploadt naar geconfigureerde media-servers en de URL inbedt in de notitie. De feature weerspiegelt bestaande image paste-functionaliteit.

### Flotilla

[Flotilla](https://github.com/coracle-social/flotilla), hodlbod's [NIP-29 (Relay-Based Groups)](/nl/topics/nip-29/) communities-client, leverde notificaties via [PR #270](https://github.com/coracle-social/flotilla/pull/270). De update refactort het alertsysteem van anchor-based polling naar lokale pull-notificaties voor web en push-notificaties voor mobiel. De architectuur implementeert de voorgestelde NIP-9a standaard (zie [PR #2194](https://github.com/nostr-protocol/nips/pull/2194) hieronder), waarbij gebruikers webhook-callbacks registreren bij relays en versleutelde event-payloads ontvangen wanneer filters matchen.

### Formstr

[Formstr](https://github.com/abh3po/nostr-forms), de Nostr-native formulieren-applicatie, voegde formulier-import en versleutelde formulier-ondersteuning toe in [PR #422](https://github.com/abh3po/nostr-forms/pull/422). Gebruikers kunnen nu bestaande formulieren importeren via een antwoordlink of andere Formstr-instanties. De encryptiefunctie stelt formuliercreators in staat om antwoorden te beperken zodat alleen aangewezen ontvangers inzendingen kunnen lezen, bruikbaar voor enquêtes die gevoelige informatie verzamelen.

### Pollerama

[Pollerama](https://github.com/abh3po/nostr-polls) ([pollerama.fun](https://pollerama.fun)), gebouwd op [nostr-tools](https://github.com/nbd-wtf/nostr-tools), voegde [NIP-17](/nl/topics/nip-17/) DM-delen voor polls toe via [PR #141](https://github.com/abh3po/nostr-polls/pull/141) en [PR #142](https://github.com/abh3po/nostr-polls/pull/142). Gebruikers kunnen nu polls direct naar contacten delen via versleutelde directe berichten.

### Nostrability Schemata

[Nostrability schemata](https://github.com/nostrability/schemata), de JSON-verificatieschema-collectie voor Nostr events, voegde [NIP-59 (Gift Wrap)](/nl/topics/nip-59/)-dekking toe via [PR #59](https://github.com/nostrability/schemata/pull/59). De update bevat schema's voor kind 13 (seal) en kind 1059 (gift wrap) events, als aanvulling op bestaande [NIP-17](/nl/topics/nip-17/) schema-dekking.

### Vector

[Vector](https://github.com/VectorPrivacy/Vector), de privacy-gerichte desktop messenger die [NIP-17](/nl/topics/nip-17/), [NIP-44](/nl/topics/nip-44/) en [NIP-59](/nl/topics/nip-59/) gebruikt voor zero-metadata encryptie, mergede [PR #39](https://github.com/VectorPrivacy/Vector/pull/39) met SIMD-versnelde prestatieoptimalisaties. Hex-encoding draait 65x sneller, image preview-generatie tot 38x sneller, en bericht-lookups 184x sneller via binary search-indexering. De PR voegt ARM64 NEON intrinsics toe voor Apple Silicon en x86_64 AVX2/SSE2 met runtime-detectie voor Windows en Linux. Geheugengebruik daalde met berichtstructs gereduceerd van 472 naar 128 bytes en npub-opslag 99,6% verminderd door interning.

Vector v0.3.0 (december 2025) integreerde [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk) voor MLS protocol-gebaseerde groepsberichten, wat end-to-end versleutelde groepen met forward secrecy naar de client bracht. MIP-04 file sharing handelt nu imeta-attachments af voor MLS-groepen, ontworpen voor interoperabiliteit met [White Noise](/nl/newsletters/2026-01-28-newsletter/#marmot-protocol-updates). De release introduceerde ook een Mini Apps-platform met WebXDC-gebaseerde P2P multiplayer games, een gedecentraliseerde app store genaamd The Nexus, PIVX wallet-integratie voor in-app betalingen, berichtbewerking met volledige geschiedenistracking, en 4x geheugenverlaging tijdens image-uploads.

## NIP-Updates

Recente wijzigingen aan de [NIPs-repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-47: Hold Invoice-ondersteuning](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/nl/topics/nip-47/) ondersteunt nu hold invoices, wat geavanceerde betalingsworkflows mogelijk maakt waarbij ontvangers betalingen expliciet moeten settlen of annuleren. De PR voegt drie nieuwe RPC-methodes toe: `make_hold_invoice` creëert een hold invoice met een vooraf gegenereerde preimage en payment hash, `settle_hold_invoice` claimt betaling door de originele preimage te verstrekken, en `cancel_hold_invoice` verwerpt betaling met zijn payment hash. Een nieuwe `hold_invoice_accepted` notificatie vuurt wanneer een betaler betaling vergrendelt. Dit maakt use cases mogelijk zoals pay-to-unlock content, marketplace escrow-systemen en payment gating. Implementaties zijn al onderweg in [Alby Hub](https://github.com/getAlby/hub/pull/1298), [Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382) en [dart NDK](https://github.com/relaystr/ndk/pull/147).

- **[NIP-05: Lowercase-vereiste](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (Domeinverificatie)](/nl/topics/nip-05/) vereist nu expliciet lowercase voor zowel hex publieke sleutels als lokale namen in het `nostr.json` bestand. Dit was impliciet in de spec maar niet vermeld, wat interoperabiliteitsproblemen veroorzaakte wanneer sommige implementaties mixed case gebruikten terwijl andere normaliseerden naar lowercase. Clients die NIP-05 identifiers valideren moeten nu alle `nostr.json` responses verwerpen die uppercase karakters bevatten in keys of namen.

- **[NIP-73: Landcodes](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (Geotags)](/nl/topics/nip-73/) ondersteunt nu ISO 3166 landcodes als alternatief voor geohashes. Events kunnen `["g", "US", "countryCode"]` tags bevatten om locatie op landniveau aan te geven zonder precieze coördinaten te vereisen. Dit maakt contentfiltering en -ontdekking op landbasis mogelijk voor applicaties waar exacte locatie onnodig of ongewenst is. De PR voegde ook een ontbrekend geohash-voorbeeld toe aan de spec-documentatie.

**Open PR's en Discussies:**

- **[NIP-82: Software Applications](https://github.com/nostr-protocol/nips/pull/1336)** - franzap kondigde een grote update aan voor deze conceptspecificatie, die definieert hoe softwareapplicaties worden gedistribueerd via Nostr met kind 30063 release events. De update dekt nu ongeveer 98% van apparaatplatforms wereldwijd, inclusief macOS, Linux, Windows, FreeBSD, WASM-omgevingen, VS Code-extensies, Chrome-extensies en Web Bundles/PWA's. Het team richt zich vervolgens op Android-, PWA- en iOS-ondersteuning, en nodigt ontwikkelaars uit om te convergeren op deze gedeelde standaard. Zapstore plant om in de komende weken te migreren naar het nieuwe formaat.

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)** - Definieert adresseerbare events voor podcastshows (kind 30074) en afleveringen (kind 30075). Shows bevatten metadata zoals titel, beschrijving, categorieën en coverafbeeldingen. Afleveringen verwijzen naar hun bovenliggende show en bevatten enclosure-URL's, duur en chapter markers. De spec integreert met Podcasting 2.0 metadata-standaarden en bevat value tags voor V4V (value-for-value) monetisatie via Lightning. Platforms zoals [transmit.fm](https://transmit.fm), een Nostr-native podcast publishing platform, kunnen direct naar relays publiceren met dit formaat, wat podcasters in staat stelt content te distribueren zonder tussenpersonen.

- **[NIP-FR: Friends-Only Notes](https://github.com/nostr-protocol/nips/pull/2207)** - Stelt een mechanisme voor om notities te publiceren die alleen zichtbaar zijn voor een door de gebruiker gedefinieerde vriendenlijst met behulp van een gedeelde symmetrische sleutel genaamd een ViewKey. De auteur versleutelt notities (kind 2044) met de ViewKey via NIP-44. De ViewKey zelf wordt eenmalig aan elke vriend gedistribueerd via [NIP-59 (Gift Wrap)](/nl/topics/nip-59/). Vrienden die de ViewKey bezitten kunnen de notities ontsleutelen en lezen; alle anderen zien alleen cijfertekst. Wanneer de auteur een vriend verwijdert, wordt de ViewKey geroteerd: een nieuwe sleutel wordt gegenereerd en herverdeeld naar alle resterende vrienden via gift wrap, waardoor de verwijderde vriend geen toegang meer heeft tot toekomstige berichten. Deze aanpak scheidt contentversleuteling (symmetrisch, efficiënt) van sleuteldistributie (asymmetrisch, per vriend), waardoor het protocol lichtgewicht blijft terwijl het een veelgevraagde privacy-feature mogelijk maakt.

- **[NIP-DB: Browser Nostr Event Database Interface](https://nostrhub.io/e/1a451c1581888215ae5c311d36c8a7c7d9e5e81f1f4010de4afaf7fcbd553e90)** ([spec](https://github.com/hzrd149/nostr-bucket/blob/master/nip.md)) - Stelt een standaard `window.nostrdb` interface voor voor browser-extensies die lokale Nostr event-opslag bieden. De API bevat methodes voor het toevoegen van events, opvragen op ID of filter, tellen van matches, en abonneren op updates. Webapplicaties kunnen deze interface gebruiken om te lezen van lokaal gecachte events zonder relay-verzoeken te doen, wat bandbreedte en latentie vermindert. hzrd149's [nostr-bucket](https://github.com/hzrd149/nostr-bucket) browser-extensie biedt een referentie-implementatie, die de interface injecteert in alle browsertabs. Een begeleidende [polyfill library](https://github.com/hzrd149/window.nostrdb.js) implementeert dezelfde API met IndexedDB voor omgevingen zonder de extensie.

- **[TRUSTed Filters](https://nostrhub.io/e/237667820943d1c8bbe7ab7732623ae51b337f177776ece439d4a8be84708eb7)** - Een suite van vijf gerelateerde voorstellen voor gedecentraliseerde contentcuratie, voortbouwend op vitorpamplona's samengevoegde [Trusted Assertions PR #1534](https://github.com/nostr-protocol/nips/pull/1534). De kernspecificatie introduceert kind 17570 events voor het declareren van Trust Provider Preferences, waardoor gebruikers kunnen specificeren welke diensten ze vertrouwen voor event-filtering en -ranking. Trust providers publiceren assertions (kind 37571), statistieken (kind 37572) en rankings (kind 37573) waarop clients kunnen abonneren. Het systeem gebruikt een plugin-architectuur met W/w tags om filtertypes en transformaties te specificeren. Dit maakt rekenintensieve operaties zoals spamdetectie, reputatiescoring en contentranking mogelijk op dedicated infrastructuur terwijl gebruikers controle behouden over welke providers ze vertrouwen. De suite bevat aparte specs voor filterpresets, gebruikersrankings, trusted events en plugin-definities.

- **[NIP-9a: Push Notifications](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod stelt een standaard voor voor relay-gebaseerde push-notificaties met kind 30390 registratie-events. Gebruikers creëren een registratie met filters voor events die ze willen ontvangen en een webhook callback-URL. De registratie is versleuteld naar de pubkey van de relay (van zijn NIP-11 `self` veld). Wanneer matchende events plaatsvinden, POST relays naar de callback met de event ID (plaintext voor deduplicatie) en het event zelf (NIP-44 versleuteld naar de gebruiker). Deze architectuur laat relays notificaties pushen terwijl event-content wordt beschermd tegen intermediaire push-servers. Flotilla's [PR #270](https://github.com/coracle-social/flotilla/pull/270) implementeert deze standaard.

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - Stelt een gedecentraliseerd contractwerk-protocol voor met escrow via kind 33400 events. Het systeem definieert drie rollen: arbiters kondigen beschikbaarheid en voorwaarden aan, patrons creëren gefinancierde taken met Bitcoin in escrow, en free agents voltooien werk om betaling te claimen. Arbiters lossen geschillen op indien nodig. Het protocol maakt trustless freelancewerkcoördinatie mogelijk waarbij fondsen vergrendeld blijven tot deliverables worden geaccepteerd of arbitrage afloopt.

## NIP Deep Dive: NIP-47 (Nostr Wallet Connect)

[NIP-47](/nl/topics/nip-47/) definieert Nostr Wallet Connect (NWC), een protocol voor remote Lightning wallet-besturing via Nostr als communicatielaag. Met de hold invoice-ondersteuning van deze week dekt NWC nu het volledige scala aan Lightning-operaties.

Het protocol werkt via een simpele uitwisseling. Een wallet-applicatie publiceert een "wallet info" event (kind 13194) die zijn mogelijkheden beschrijft. Client-applicaties sturen versleutelde verzoeken (kind 23194) die de wallet vragen om operaties uit te voeren zoals invoices betalen, invoices aanmaken of saldo's controleren. De wallet antwoordt met versleutelde resultaten (kind 23195).

NWC gebruikt [NIP-44](/nl/topics/nip-44/)-encryptie tussen de client en wallet, met een dedicated keypair voor wallet-operaties, gescheiden van de hoofdidentiteit van de gebruiker. Deze scheiding betekent dat het compromitteren van een NWC-verbinding de Nostr-identiteit van de gebruiker niet blootstelt.

**Ondersteunde Methodes:**

De spec definieert methodes voor kern Lightning-operaties: `pay_invoice` verstuurt betalingen, `make_invoice` genereert invoices voor ontvangen, `lookup_invoice` controleert betalingsstatus, `get_balance` retourneert het wallet-saldo, en `list_transactions` biedt betalingsgeschiedenis. De recent gemergede `pay_keysend` maakt betalingen zonder invoices mogelijk, en `hold_invoice` ondersteunt voorwaardelijke betalingen.

**Voorbeeld Events:**

De wallet-service publiceert een info event (kind 13194) die zijn mogelijkheden adverteert:

```json
{
  "kind": 13194,
  "pubkey": "<wallet service pubkey>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

Een client stuurt een versleuteld verzoek (kind 23194) om een invoice te betalen:

```json
{
  "kind": 23194,
  "pubkey": "<client ephemeral pubkey from connection URI secret>",
  "content": "<NIP-44 encrypted: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<wallet service pubkey>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<client ephemeral key signature>"
}
```

De wallet-service antwoordt (kind 23195) met het betalingsresultaat:

```json
{
  "kind": 23195,
  "pubkey": "<wallet service pubkey>",
  "content": "<NIP-44 encrypted: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<client ephemeral pubkey>"],
    ["e", "<request event id>"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

De `e` tag in het antwoord refereert naar het originele verzoek, waardoor clients antwoorden kunnen matchen met hun verzoeken.

**Hold Invoices:**

De [PR #1913](https://github.com/nostr-protocol/nips/pull/1913) van deze week voegde hold invoice-ondersteuning toe, wat escrow-achtige betalingen mogelijk maakt. In tegenstelling tot standaard invoices waarbij de ontvanger direct betaling claimt door de preimage vrij te geven, laten hold invoices de ontvanger deze beslissing uitstellen. Wanneer een betaler naar een hold invoice verstuurt, worden fondsen vergrendeld langs de betalingsroute. De ontvanger kiest vervolgens om te settlen (preimage vrijgeven en fondsen claimen) of annuleren (betaling afwijzen, fondsen teruggeven aan betaler). Als geen van beide acties plaatsvindt, time-out de betaling en worden fondsen automatisch teruggegeven. De PR voegt drie NWC-methodes toe: `make_hold_invoice`, `settle_hold_invoice` en `cancel_hold_invoice`, plus een `hold_invoice_accepted` notificatie. Dit mechanisme ondersteunt applicaties zoals Ridestr's rideshare escrow en marketplace geschillenbeslechting.

**Huidige Implementaties:**

Grote wallets ondersteunen NWC: Zeus, Alby en Primal (sinds de [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) van deze week) implementeren allemaal wallet-side ondersteuning. Aan de clientkant kunnen Damus, Amethyst en de meeste grote Nostr-clients verbinden met NWC-wallets voor zappen en betalingen.

Het protocol maakt een scheiding van verantwoordelijkheden mogelijk: gebruikers kunnen hun wallet op een apparaat draaien terwijl ze vanaf een ander met Nostr interacteren, met Nostr relays als communicatiekanaal. Deze architectuur betekent dat mobiele clients geen fondsen direct hoeven vast te houden, wat de beveiliging verbetert door wallet-infrastructuur gescheiden te houden van sociale clients.

**Beveiligingsoverwegingen:**

NWC-verbindingen moeten als gevoelig worden behandeld. Hoewel de encryptie berichtinhoud beschermt, moeten de wallet pubkey en connection secret worden bewaakt. Applicaties moeten gebruikers toestaan verbindingen in te trekken en bestedingslimieten in te stellen. Het protocol ondersteunt capability restrictions, zodat wallets kunnen beperken welke operaties een bepaalde verbinding kan uitvoeren.

## NIP Deep Dive: NIP-59 (Gift Wrap)

[NIP-59](/nl/topics/nip-59/) definieert een protocol voor het inkapselen van elk Nostr event in meerdere lagen encryptie, wat de identiteit van de afzender verbergt voor relays en waarnemers. De voorstellen van deze week voor friends-only notes (NIP-FR) en push notifications (NIP-9a) vertrouwen beide op gift wrapping, wat het een fundamentele privacy-primitief maakt die het begrijpen waard is.

**De Drie Lagen:**

Gift wrapping gebruikt drie geneste structuren:

1. **Rumor** (unsigned event): De originele content als Nostr event zonder handtekening. De rumor kan niet direct naar relays worden gestuurd omdat relays unsigned events verwerpen.

2. **Seal** (kind 13): De rumor wordt versleuteld met [NIP-44](/nl/topics/nip-44/) en geplaatst in een kind 13 event. De seal IS getekend door de echte sleutel van de auteur. Dit is het cryptografische bewijs van auteurschap.

3. **Gift Wrap** (kind 1059): De seal wordt versleuteld en geplaatst in een kind 1059 event getekend door een willekeurig, eenmalig keypair. De gift wrap bevat een `p` tag voor routering naar de ontvanger.

**Een Veelvoorkomend Misverstand: Deniability**

De spec vermeldt dat unsigned rumors "deniability" bieden, maar dit is misleidend. De seal-laag IS getekend door de echte auteur. Wanneer de ontvanger de gift wrap ontsleutelt en vervolgens de seal, hebben ze cryptografisch bewijs van wie het bericht stuurde. De ontvanger zou zelfs een zero-knowledge proof kunnen construeren die de identiteit van de afzender onthult zonder hun eigen privésleutel bloot te stellen.

Wat gift wrap daadwerkelijk biedt is **afzenderprivacy voor waarnemers**: relays en derden kunnen niet bepalen wie het bericht stuurde omdat ze alleen de gift wrap zien getekend door een willekeurige sleutel. Maar de ontvanger weet het altijd, en kan het bewijzen.

**Voorbeeld Events:**

Hier is de complete drielaagse structuur uit de spec (versturen van "Ga je vanavond naar het feest?"):

De rumor (unsigned, kan niet naar relays worden gepubliceerd):
```json
{
  "created_at": 1691518405,
  "content": "Are you going to the party tonight?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

De seal (kind 13, getekend door echte auteur, bevat versleutelde rumor):
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

De gift wrap (kind 1059, getekend door willekeurige efemere sleutel, bevat versleutelde seal):
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

Let op: de `pubkey` van de seal is de echte auteur (`611df01...`), terwijl de `pubkey` van de gift wrap een willekeurige eenmalige sleutel is (`18b1a75...`). Relays zien alleen de gift wrap, dus kunnen het bericht niet toeschrijven aan de echte auteur.

**Wat Elke Laag Beschermt:**

De rumor is unsigned en kan niet direct naar relays worden gepubliceerd. De seal is getekend door de echte auteur en bewijst auteurschap aan de ontvanger. De gift wrap is getekend door een willekeurige eenmalige sleutel, wat de echte auteur verbergt voor relays en waarnemers. Alleen de ontvanger kan door beide lagen heen ontsleutelen om de originele content te bereiken en de handtekening van de auteur op de seal te verifieren.

**Huidige Toepassingen:**

[NIP-17 (Privéberichten)](/nl/topics/nip-17/) gebruikt gift wrap voor versleutelde DM's, ter vervanging van het oudere NIP-04-schema. Het voorgestelde NIP-FR (alleen-voor-vrienden notities) gebruikt gift wrapping om ViewKeys aan vrienden te distribueren, die vervolgens notities ontsleutelen die met die sleutels zijn versleuteld. NIP-9a (push notifications) versleutelt notificatie-payloads volgens gift wrap-principes.

**Metadatabescherming:**

Timestamps moeten worden gerandomiseerd om timinganalyse te dwarsbomen. Relays moeten AUTH vereisen voor het serveren van kind 1059 events en ze alleen serveren aan de gemarkeerde ontvanger. Bij verzenden naar meerdere ontvangers, creëer aparte gift wraps voor elk.

---

Dat was het voor deze week. Iets aan het bouwen? Nieuws te delen? Wil je dat we je project behandelen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via NIP-17 DM</a> of vind ons op Nostr.
