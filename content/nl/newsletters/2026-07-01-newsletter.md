---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-07-01
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [FIPS v0.4.0](#fips-v040-levert-nym-mixnet-transport-mdns-ontdekking-en-een-vernieuwde-dataplane) levert Nym-mixnettransport, optionele mDNS-ontdekking op het LAN, ononderbroken rekeying bij pakketverlies en een vernieuwde dataplane, wire-compatible met v0.3.0. [Whitenoise Linux](#whitenoise-linux-verschijnt-als-desktopclient-voor-marmot) verschijnt als desktopclient voor Marmot in Rust en Slint, met een protocolvoorstel om berichteffecten naar een afzonderlijk kind-9-event te verplaatsen. [CustID v0.1.10-beta](#custid-verschijnt-als-mobiele-identiteitskluis-met-nip-46-en-nfc-challenge-flow) verschijnt als hardwarematig beveiligde mobiele identiteitskluis die als NIP-46-remote signer werkt en fysieke toegangsuitdagingen via NFC beantwoordt. [myco](#myco-verschijnt-met-peer-to-peer-deling-van-nsites-over-het-fips-mesh) brengt peer-to-peer-deling van nsites over het FIPS-mesh, met een nieuw BLE L2CAP-transport in v0.1.0. [Nostr Codex Phone](#nostr-codex-phone-verschijnt-als-mobiel-bedieningspaneel-voor-een-lokale-codex-worker-over-nostr) verschijnt als Android-bedieningspaneel voor een lokale Codex-codeerassistent via versleutelde Nostr-DM's. [De nog niet uitgebrachte versie van Amethyst](#amethyst-bouwt-een-nip-89-bewuste-ui-een-git-repositories-feed-en-een-discover-sectie-voor-napplets) voegt parsing van NIP-89-apphandlers, een Git Repositories-feed voor NIP-34 en een Discover-sectie voor nSites en napplets toe. [Notedeck](#notedeck-implementeert-nip-37-relays-voor-privesynchronisatie-nip-52-agendas-en-nip-22-commentaren) implementeert NIP-37, NIP-52 en NIP-22 in één week. [Applesauce](#applesauce-levert-nbunksec-nip-46-sessies-en-een-cashu-v4-walletupgrade) brengt twaalf subpackagereleases uit met nbunksec-helpers voor NIP-46 en een walletupgrade naar Cashu-ts v4. [Meiso v1.4.0](#meiso-v140-levert-collaborative-lists-met-een-gedeelde-sleutel-die-mls-voor-taakdeling-vervangen) levert Collaborative Lists met een gedeelde sleutel op adresseerbaar kind 35000. De NIPs-repository voegde vijf PR's samen, waaronder een Relay Roles-event, het schrappen van de limiet van 65.535 bytes in NIP-44, NIP-34-forksemantiek, NIP-46-clientmetadata en een NIP-86-`signevent`-methode. De deep dives behandelen [NIP-86 (Relay Management API)](#nip-deep-dive-nip-86-relay-management-api) en [NIP-89 (Recommended Application Handlers)](#nip-deep-dive-nip-89-recommended-application-handlers).

---

## Topverhalen

### FIPS v0.4.0 levert Nym-mixnettransport, mDNS-ontdekking en een vernieuwde dataplane

[FIPS](https://github.com/jmcorgan/fips) is een privaat, zelforganiserend peer-to-peer-meshnetwerk voor Nostr waarin nodes elkaar ontdekken en verkeer routeren zonder centrale infrastructuur. [FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) levert Nym-mixnettransport, optionele mDNS-ontdekking op het LAN, een vernieuwde dataplane, ononderbroken rekeying bij pakketverlies, een herschreven `fipstop`-TUI op een render-snapshot-harnas, een observability-plane buiten het hot path en nieuwe packagingtargets voor OpenWrt-apk en Nix flakes. Alles blijft wire-compatible met v0.3.0, zodat gemengde meshes tijdens een rolling upgrade samenwerken. Twee nieuwe transporten voor peerontdekking vormen de kern van de release. Een nieuw [uitgaand Nym-mixnettransport](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) routeert FIPS-verkeer via een `nym-socks5-client`-SOCKS5-proxy en mengt het in het cover-traffic-netwerk van [Nym](https://nymtech.net/), zodat waarnemers op linkniveau niet kunnen correleren welke meshpeers met elkaar praten. De map `examples/sidecar-nostr-mixnet-relay/` demonstreert een Nostr-relay die via een FIPS-link end-to-end over het mixnet bereikbaar is. Met optionele mDNS-/DNS-SD-ontdekking vinden nodes op dezelfde lokale link elkaar zonder adresconfiguratie of STUN; ze adverteren en accepteren peers via een standaard-servicerecord wanneer `node.discovery.lan.enabled: true` staat.

De dataplane is herwerkt voor meer throughput per node. Encryptie en decryptie per peer draaien nu in eigen workertaken buiten de receive-loop, zodat één drukke peer de cryptografie van de hele node niet meer serialiseert. Het Linux-sendpad gebruikt waar mogelijk generic segmentation offload en een verbonden UDP-socket, het receive-hotpath vermijdt bufferkopieën die voorheen per pakket werden gemaakt en macOS krijgt `recvmsg_x` voor batched receive als tegenhanger van Linux' `recvmmsg`-batching uit v0.3.0. Het volledige `show_*`-leesoppervlak voor `fipsctl` en `fipstop` wordt nu bediend vanuit een snapshot per tick, dat de control-accept-taak in een lock-free `ArcSwap` publiceert. Daardoor worden operatorqueries snel beantwoord, ook wanneer de receive-loop van een node druk is. Een nieuwe `show_metrics`-query met alleen tellers (beschikbaar als `fipsctl stats metrics`) maakt Prometheus-scraping mogelijk zonder kosten in het hot path.

Rekeying van FMP- en FSP-sessies verloopt nu in beide richtingen zonder onderbreking bij pakketverlies en herordening: inkomende frames worden tegen de wachtende sessie geauthenticeerd voordat de K-bit-cutover die sessie promoveert (zodat een oud of gespooft frame rekeying niet kan ontsporen), retransmissie van rekey-bericht 1 is begrensd, de link-dead-heartbeat houdt rekening met rekeying en races bij gelijktijdige initiatie op high-latency-links worden met symmetrische jitter gedesynchroniseerd. De `fipstop`-TUI is herbouwd op een render-snapshot-harnas dat voor elke view het exacte tekstraster en de stijl per cel controleert tegen vooraf gemaakte control-socket-output. Er komen ook nieuwe packagingtargets: een OpenWrt-`.apk` voor OpenWrt 25+ (gebouwd zonder SDK, met hergebruik van de bestaande `.ipk`-crosscompile en de payload van het geïnstalleerde bestandssysteem) en een `flake.nix` in de projectroot die alle vier binaries (`fips`, `fipsctl`, `fips-gateway`, `fipstop`) vanuit de bron bouwt op Nix/NixOS met de vastgezette toolchain.

### Whitenoise Linux verschijnt als desktopclient voor Marmot

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git) is een desktopclient voor [Marmot](/nl/topics/marmot/): MLS-groepsberichten via Nostr-relays, verpakt als één Rust-binary met een Slint-UI die elk geheim in één met een wachtwoord versleutelde kluis bewaart.

De belangrijkste discussie van deze week stelt voor om Whitenoise-berichteffecten te vervoeren als een afzonderlijk kind-9-event dat naar het bovenliggende bericht verwijst. Het huidige wire-formaat plakt een marker zoals `dmfx:sparkle` achter aan de berichttekst, waardoor renderers die de conventie niet kennen vervuilde tekst tonen. Effecten in een eigen event houden de berichttekst schoon en leggen een ontwerpvraag bloot waarmee de bredere Marmot-stack te maken krijgt: inline-conventies in de body of sidecar-events voor optionele rijke functies.

### CustID verschijnt als mobiele identiteitskluis met NIP-46 en NFC-challenge-flow

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c) is de eerste publieke bèta van CustID, een mobiele identiteitskluis op Nostr en het SISTR-protocol. CustID bewaart meerdere Nostr-identiteiten in hardwarematig beveiligde opslag, werkt voor andere clients als [NIP-46](/nl/topics/nip-46/)-remote signer en beantwoordt fysieke en online toegangsuitdagingen via NFC en QR-codes.

De bèta is volledig voor de NIP-46-signer en de NFC-challenge-response-flow; toegangsflows met zero-knowledge proofs blijven een toekomstige mijlpaal. Deze release verwijdert ook de [NIP-65](/nl/topics/nip-65/)-keep-alive-laag op de achtergrond. Die opende per profiel en per leesrelay een WebSocket en nam kinds in die de client meteen weggooide. Alleen de NIP-46-sockets met meldingen van ondertekeningsverzoeken blijven nu op de achtergrond actief. Daardoor is CustID op een telefoon bruikbaar als bunker voor andere clients.

### myco verschijnt met peer-to-peer-deling van nsites over het FIPS-mesh

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0) opende deze week op 27 juni en bereikte v0.1.0 op 1 juli. myco is een Android-app in Rust die apps installeert van mensen in je omgeving: peer-to-peer-deling van [nsites](/nl/topics/nip-5a/) over een FIPS-mesh, via elk transport dat het mesh kan dragen (UDP, TCP, Tor, Bluetooth) en volledig offline. Het ontwerp koppelt FIPS als transportlaag rechtstreeks aan het eventformaat voor statische websites van NIP-5A als payload. Daardoor kan een als nsite gedistribueerde app tussen meshpeers bewegen zonder afhankelijk te zijn van relays of HTTP.

v0.1.0 voegt een L2CAP-radiopad via Bluetooth toe, zodat twee telefoons met FIPS via BLE kunnen peeren zonder netwerk. Ook komen er een speedtest per peer en door NFC geactiveerd delen vanuit de Circle-bottom-sheet van de app. myco staat eveneens op Zapstore voor rechtstreekse installatie.

### Nostr Codex Phone verschijnt als mobiel bedieningspaneel voor een lokale Codex-worker over Nostr

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone) verschijnt deze week als Android-client die een lokale Codex-worker voor codeerassistentie bestuurt via versleutelde directe berichten over Nostr. De app ondersteunt meerdere repositorysessies, spraaktranscriptie, gerouteerde workersessies, Blossom-mediauploads en optionele gesproken antwoorden. Zo kan een ontwikkelaar met een Codex-worker thuis vanaf een telefoon opdrachten versturen zodra die telefoon toegang tot een relay heeft.

Het project is een directe tegenhanger van [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr), dat in #28 verscheen. Beide plaatsen agentic-coding-workflows op Nostr-transport met versleutelde DM's en gebruiken Nostr als koppelings- en berichtenlaag waarmee een telefoon een worker thuis bereikt zonder gaten in het netwerk te openen. Nostr als control-plane voor lokale agents wordt een herkenbaar patroon.

### Coop Mobile publiceert zijn eerste versiegenummerde builds

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1) en [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2) verschenen deze week als de eerste versiegenummerde builds van Coop Mobile, een Android-client voor versleutelde directe berichten via [NIP-17](/nl/topics/nip-17/). De twee releases verbeteren de crashbestendigheid bij het parsen van berichten en verwerken van QR-codes en wissen bij uitloggen alle opgeslagen gegevens.

### Amethyst bouwt een NIP-89-bewuste UI, een Git Repositories-feed en een Discover-sectie voor napplets

De main-branch van [Amethyst](https://github.com/vitorpamplona/amethyst) bouwde deze week meerdere nieuwe oppervlakken uit. Een [Git Repositories-feed](https://github.com/vitorpamplona/amethyst/pull/3406) verandert [NIP-34](/nl/topics/nip-34/)-repo's in een doorbladerbare Android-tijdlijn, filterbaar op community en auteur, naast een [smart-HTTP-gitbrowser](https://github.com/vitorpamplona/amethyst/pull/3415) die repository-inhoud en commits leest zonder de app te verlaten. De napplet-host kreeg een [Discover-sectie](https://github.com/vitorpamplona/amethyst/pull/3409) met gecureerde webapps, gevolgde nSites en napplets, afkomstig uit [NIP-89](/nl/topics/nip-89/)-handlerevents en [NIP-5A](/nl/topics/nip-5a/)-site-events. De weergave van notes [toont nu welke Nostr-app een event schreef](https://github.com/vitorpamplona/amethyst/pull/3422) via NIP-89-tags. Voor synchronisatie komt [NIP-77-negentropy-ondersteuning](https://github.com/vitorpamplona/amethyst/pull/3434) met streaming reconciliation en automatische `created_at`-vensters om resultaatlimieten van relays te omzeilen. Dat vermindert de bandbreedte die nodig is om grote lokale eventsets met een relay te synchroniseren.

### Buzz v0.3.38 verhardt het relay-aanvalsoppervlak en voegt provideronafhankelijke modelkeuze toe

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38) verhardt het [relay-aanvalsoppervlak](https://github.com/block/buzz/pull/1369) dat Buzz blootstelt wanneer het persona's, teams, beheerde agents en NIP-OA-owner attestations als ondertekende Nostr-events publiceert. Een Buzz-relay is een openbaar register van de Nostr-identiteiten en toestand van een team; deze release scherpt de invoervalidatie en replaybescherming aan voor de bekende eventkinds die Buzz definieert. De release veralgemeniseert ook de modelkeuze, zodat een Buzz-team elke provider kan gebruiken waarvoor Buzz een adapter heeft, waaronder een nieuwe Databricks AI Gateway v2-backend.

### Notedeck implementeert NIP-37-relays voor privésynchronisatie, NIP-52-agenda's en NIP-22-commentaren

[Notedeck](https://github.com/damus-io/notedeck), de native Rust-desktopclient van het Damus-team, implementeerde in één week drie protocollen. Relays voor privésynchronisatie worden nu opgeslagen als een kind `10013`-[NIP-37](/nl/topics/nip-37/)-lijst, los van de publieke NIP-65-outbox van de gebruiker. Het agendapaneel `horizon` leest [NIP-52](/nl/topics/nip-52/)-events uit nostrdb en kreeg een herontwerp met drie panelen. Het paneel `headway` voegde een [NIP-22](/nl/topics/nip-22/)-model voor commentaarevents toe op kind `1111`, het kind dat NIP-22 definieert voor het uniforme commentaaroppervlak dat reply-threading uit NIP-10 vervangt.



### Applesauce levert nbunksec-NIP-46-sessies en een Cashu v4-walletupgrade

[Applesauce](https://github.com/hzrd149/applesauce), de modulaire Nostr-toolkit voor signers, relays, wallets en content, bracht een gecoördineerde [6.2.x-release](https://github.com/hzrd149/applesauce/releases) uit voor zijn subpackages. Het signerpackage kreeg helpers voor het importeren en exporteren van `nbunksec`, waarmee een [NIP-46](/nl/topics/nip-46/)-bunkersessie een verplaatsbaar artefact wordt dat tussen clients kan worden overgezet. Het walletpackage vernieuwde zijn [Cashu](/nl/topics/nip-60/)-bindings naar `@cashu/cashu-ts` v4, waarin proofbedragen `Amount`-value objects worden en de API voor tokendecodering verandert.

---

## Releases met tags

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0) levert de volgende protocoliteratie voor het [Mostro](/nl/topics/nip-69/)-netwerk voor peer-to-peerhandel in fiatgeld. De release volgt op [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2) en verschijnt naast [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0), dat de nieuwe core overneemt. Deze week werden drie PR's in de core-repository samengevoegd; de omliggende stack (mostro daemon en Mostro mobile) volgt v0.14.0 van de gedeelde types-crate.

### ngit v2.6.1

[ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli), de canonieke git-over-Nostr-CLI voor [NIP-34](/nl/topics/nip-34/)-repositories, implementeert de deze week samengevoegde [NIP-34 GRASP-06-forksemantiek](https://github.com/nostr-protocol/nips/pull/2395), die de `personal-fork`-tag op repo-state-events vervangt door een `u`-tag.

### mesh-llm v0.72.0 en v0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm), het inference-onderdeel van de ContextVM-stack dat opensource-LLM's achter een via Nostr adresseerbaar JSON-RPC-oppervlak draait, bracht [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0) en [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1) uit met een oplossing voor een batchingcrash bij grote afzonderlijke prompts en een migratie van de MCP-bridge weg van verouderde helpers.

### Meiso v1.4.0 levert Collaborative Lists met een gedeelde sleutel die MLS voor taakdeling vervangen

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0) introduceert een model van Collaborative Lists met een gedeelde sleutel, dat de eerdere taakdeling op basis van MLS vervangt door een eenvoudiger ontwerp met adresseerbare events. Elke gedeelde lijst maakt een eigen Nostr-sleutel die onder leden wordt verspreid. Taken zijn adresseerbare events op kind `35000`, geïdentificeerd met `d=task-id`, met via [NIP-44](/nl/topics/nip-44/) zelfversleutelde content. Relays dwingen Last-Write-Wins per taak af. Het ontwerp levert de forward secrecy en post-compromise security van MLS in voor een eenvoudiger clientimplementatie en conflictoplossing op relayniveau.

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn) levert een "more-private-coordinator"-traject dat tijdelijke pubkeys van afzenders uit het publiceren van groepsberichten verwijdert en de flow voor joinverzoeken verhardt tegen verouderde herhaalde verzoeken. Cordn is de op MLS gebaseerde berichtenstack uit [de lancering van Cordn Ad-hoc CVM in #28](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator); deze release is de bijbehorende update aan de coördinatorzijde.

---

## Nog niet uitgebrachte wijzigingen

### diVine verwerkt 108 samengevoegde PR's met verbeteringen na de lancering

[diVine](https://github.com/divinevideo/divine-mobile), de client voor korte loopingvideo's die Vine terugbrengt, zit in een intensieve verbeteringsronde na de lancering. Het voor Nostr zichtbare werk van deze week is een stabiliteitspass voor de [NIP-46](/nl/topics/nip-46/)-connectflow die fouten van `nostrconnect://` omzet in gestructureerde redencodes.

### Zap Cooking zet de projectoverschrijdende NIP-46-fix en herbouw van de composer voort

[Zap Cooking](https://github.com/zapcooking/frontend) is een Nostr-client voor het delen van recepten, waarbij recepten als longform-events op Nostr worden gepubliceerd. Het werk van deze week zet de projectoverschrijdende [NIP-46](/nl/topics/nip-46/)-fix en herbouw van de composer voort die in [#28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes) als nog niet uitgebracht zijn beschreven.

### Conduit verhardt de flow voor listings en de correctheid van de marktplaats

[Conduit](https://github.com/Conduit-BTC/conduit-mono) is een marktplaats-monorepo op Nostr met drie apps: de kopersmarkt, het handelaarsportaal en de winkelbouwer. Het werk van deze week zet de verbeteringen aan de correctheid van de marktplaats voort die in [de lanceringsdekking van #28](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default) aan bod kwamen, voortbouwend op de [NIP-99](/nl/topics/nip-99/)-handelsgolf die vorig nummer het protocolverhaal vormde.

### Pollerama v1.12 tot en met v1.13.1 voegen keuze van clienttag, profieltabbladen en threadlimieten toe

[Pollerama](https://github.com/formstr-hq/nostr-polls), een Android-Nostr-client voor polls en notes met een sterke web-of-trust-ontdekkingslaag, bracht deze week v1.12.0, v1.13.0 en v1.13.1 uit op Zapstore. Gebruikers kunnen nu kiezen welke clienttag aan hun notes en polls wordt toegevoegd, uit een vooraf ingestelde lijst of met een eigen invoer. Diep geneste commentaar- en antwoordketens stoppen nu na enkele niveaus en linken naar de volledige thread op de notepagina. Profielpagina's openen standaard op Notes, onderverdeeld in een tabblad Posts en een tabblad Conversations. Een persistentiefout waarbij nieuw gevolgde accounts na een herstart verdwenen is opgelost en volgknoppen tonen nu voortgang.

### getwired.app en get-tao.app repareren de NIP-13-flow voor confess-inzendingen

[getwired.app](https://github.com/smolgrrr/Wired) en [get-tao.app](https://github.com/smolgrrr/TAO) delen een flow voor anoniem publiceren die bij het inzenden NIP-13-proof-of-work toevoegt om spam te onderdrukken. Ze repareerden de [flow voor confess-inzendingen](https://github.com/smolgrrr/Wired/pull/57), zodat de UX tijdens PoW-mining samenhangend is.

### nostui voegt een tijdlijntabblad voor vermeldingen toe

[nostui](https://github.com/akiomik/nostui), een terminalclient voor Nostr in Rust, voegde een [tijdlijntabblad voor vermeldingen](https://github.com/akiomik/nostui/pull/463) toe dat kind-1-events die de actieve pubkey taggen in een afzonderlijke TUI-view toont.

### Heartwood krijgt NIP-46-bunker-URI's per identiteit en een ondertekeningsbridge in HSM-modus

[Heartwood](https://github.com/forgesworn/heartwood) is een [NIP-46](/nl/topics/nip-46/)-signer waarbij de ondertekeningssleutel nooit bij de client terechtkomt: de client spreekt NIP-46 met een kleine relay en de relay spreekt een serieel frameprotocol met een aangesloten hardwareapparaat dat de handtekening uitvoert. Deze week kreeg het project een [ondertekeningsbridge van relay naar seriële verbinding](https://github.com/forgesworn/heartwood/pull/11) en [bunkerverbindingen per identiteit](https://github.com/forgesworn/heartwood/pull/16), zodat één hardwareapparaat met meerdere identiteiten voor elke identiteit een afzonderlijke bunker-URI aanbiedt.

### Nostter vernieuwt authenticatie en signers

[Nostter](https://github.com/SnowCait/nostter) vernieuwde deze week zijn [authenticatie- en signerlaag](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth): de loginstatus verhuisde naar één signal en signer-dispatch werd opgesplitst in strategiemodules. Het doel is een heldere signerabstractie waarin de NIP-07-webextensie, NIP-46-remote bunker en raw nsec hetzelfde codepad delen.

### Dart NDK splitst de NIP-07-signer af en randomiseert NIP-59-tijdstempels

[Dart NDK](https://github.com/relaystr/dart_ndk) verplaatste zijn [NIP-07](/nl/topics/nip-07/)-signer uit het corepackage naar `ndk_flutter` (waar de Flutter WebView zich bevindt) en [randomiseerde de NIP-59-tijdstempels van gift wraps](https://github.com/relaystr/dart_ndk/pull/667) om correlatie van versleutelde berichten op basis van timing te bemoeilijken.

### Milk Market voegt NIP-23-winkelpagina's en betalingsverwerking via Square toe

[Milk Market](https://github.com/shopstr-eng/milk-market), de marktplaatswinkel van het Shopstr-team, gaf elke winkel een blogpagina op basis van de [NIP-23](/nl/topics/nip-23/)-longform-events van de verkoper, met bewerkbare secties en een rechtstreekse route naar de bloginstellingen. In dezelfde week kwamen [Square](https://github.com/shopstr-eng/milk-market/pull/30) als alternatieve betalingsverwerker voor verkopers en automatische aankoop van verzendlabels voor betaalde bestellingen erbij.

### Calendar by Formstr brengt een iOS-app uit

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) voegde deze week [PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159) samen en bracht daarmee de [NIP-52](/nl/topics/nip-52/)-agendaclient naar iOS. [PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197) repareert het parsen van kalenderdatums in lokale tijd en [PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201) voegt een Playwright-E2E-workflow toe die door een `run-tests`-label wordt geactiveerd.

### cagliostr handhaaft NIP-22, NIP-09 per coördinaat en NIP-13-proof-of-work

[cagliostr](https://github.com/mattn/cagliostr), een relayimplementatie in Go, scherpte deze week drie handhavingspaden aan: [configureerbare NIP-13-proof-of-work](https://github.com/mattn/cagliostr/pull/7) voor inkomende events, [NIP-09-verwijdering per adresseerbare coördinaat](https://github.com/mattn/cagliostr/pull/8), zodat vervangbare events via hun `a`-tag kunnen worden verwijderd (wat verwijdering per event-id niet kan bereiken), en [configureerbare NIP-22-limieten voor tijdstempels](https://github.com/mattn/cagliostr/pull/9) die events met een tijdstempel te ver in het verleden of de toekomst weigeren.

---

## Nieuw gevolgd en ontdekt

De [wellbeing-suite van Vanderwarker](https://git.vanderwarker.family/wellbeing) publiceert telemetrie uit de fysieke wereld als Nostr-events onder één gedeelde ondertekeningssleutel van de publisher. De suite bestaat uit vijf zusterapps: [Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android) is een stappenteller die fitnessgegevens als `kind:30078` aan Nostr verankert; [Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android) publiceert dagelijks hoe vaak een telefoon is ontgrendeld; [Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android) publiceert de huidige mediaweergave als User Status; [Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android) publiceert elke vijftien minuten batterijniveau, spanning en temperatuur; en [Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android) publiceert dagelijks het dataverbruik. Alle vijf verschenen tussen 24 en 30 juni op Zapstore.

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9) is een versleutelde, serverloze Android-app voor live locatiedeling, gebouwd in Rust en Slint en uitgebracht op 29 juni. Het is een tegenhanger van [Haven](https://github.com/mehmetefeumit/Haven-App), de op [Marmot](/nl/topics/marmot/) gebaseerde app voor locatiedeling uit [#28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot), maar met een andere transportarchitectuur: versleutelde Nostr-DM's vervoeren de locatie-updates, terwijl Haven Marmot-groepsberichten gebruikt.

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell) is een applicatieshell in een vroeg stadium voor het bouwen van Nostr-apps. Het project publiceerde deze week zijn eerste gebruikersdocumentatie.

[NIPs by Pollerama](https://nips.pollerama.fun) (repository [abh3po/better-nips](https://github.com/abh3po/better-nips), aangemaakt op 2026-06-29) is een nieuwe client voor de door de community geschreven `kind:30817`-NIPs van [NostrHub](https://nostrhub.io), bedoeld als op vertrouwen gewogen alternatief voor nostrhub.io. Elke `kind:30817`-NIP heeft een eigen deelbare URL (`#/nip/<naddr>`) met volledige Markdown-weergave en de eventkinds die de NIP definieert. De client biedt drie feeds: Following, Web of Trust (gevolgden van gevolgden) en Global. Elke feed kan worden gesorteerd op op vertrouwen gewogen goedkeuringen of op nieuwste. Goedkeuringen worden gepubliceerd als [NIP-32](/nl/topics/nip-32/)-labels op kind `1985`, met tags `["L","nostrhub"]` en `["l","approve","nostrhub"]`, plus een `a`-tag die naar het doeladres van de NIP wijst en een `client`-tag die `better-nips` vermeldt. Dat is exact de eventvorm die NostrHub zelf ondertekent, zodat goedkeuringen tussen beide clients compatibel zijn. Een goedkeuring van een direct gevolgd account weegt in de rangschikking zwaarder dan een goedkeuring van een tweede graad.

De signerstack is [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer), met een volledige loginmodal voor [NIP-07](/nl/topics/nip-07/), [NIP-46](/nl/topics/nip-46/)-bunker en nostrconnect, [NIP-49](/nl/topics/nip-49/)-ncryptsec en [NIP-55](/nl/topics/nip-55/)-Android-signer. Sessies worden bij herladen stil opnieuw gekoppeld. De netwerklaag draait via [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay), een Web Worker die de [NIP-65](/nl/topics/nip-65/)-outbox van de gebruiker over relays verdeelt, zodat een grote web-of-trust-set niet naar één relay uitwaaiert. Het ontwerp stelt dat community-NIPs, ongeacht of ze bij NostrHub, in `better-nips` of bij toekomstige clients staan, op protocolniveau gelijk zijn; de rangschikking komt uit de sociale grafiek, niet uit moderatie. Dat sluit rechtstreeks aan op de NIP-32-labelingflow uit de deep dive in [#25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling).

Deze week verschenen twee nieuwe clusters van [NIP-34](/nl/topics/nip-34/)-repo's. [Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git) is een videogerichte Nostr-client. Een [nostrapps.com-cluster](wss://gitnostr.com) publiceert drie zusterprojecten: [verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git) (een napp-VM voor desktop), [hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git) (een aanpasbare communityclient) en [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git) (een specificatie en runtime voor HTML-microapps). Het cluster loopt parallel aan het [napplet](/nl/topics/nip-5d/)-werk uit het topverhaal van het vorige nummer.

---

## Protocolwerk en NIP-updates

### Samengevoegd: NIP-44 schrapt de payloadlimiet van 65.535 bytes

[PR #1907](https://github.com/nostr-protocol/nips/pull/1907) werd op 28 juni samengevoegd nadat hij sinds 2024-09 openstond. De wijziging schrapt de bovengrens van 65.535 bytes voor de plaintext-payload van een [NIP-44](/nl/topics/nip-44/)-envelope met versiegebonden versleuteling en verhoogt die naar 4 GiB (`uint32_max`). NIP-44 codeert de payloadlengte als een `uint16` in het wire-formaat, wat de oorspronkelijke specificatie strikt vereiste voor interoperabiliteit. De samengevoegde wijziging gebruikt een langer lengteveld dat in de versiebyte wordt gemarkeerd, zodat v2-implementaties wire-compatible blijven en v3+-implementaties de langere lengte dragen. Clients die NIP-44 gebruiken voor directe berichten via [NIP-17](/nl/topics/nip-17/), gift wraps via [NIP-59](/nl/topics/nip-59/), payloads voor remote signers via [NIP-46](/nl/topics/nip-46/) of andere via NIP-44 versleutelde Nostr-berichten, kunnen nu afzonderlijke events groter dan 64 KiB uitwisselen zonder ze op applicatieniveau te splitsen.

### Samengevoegd: NIP-86 krijgt een `signevent`-methode en een Relay Roles-event

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) voegt een `signevent`-methode toe aan de JSON-RPC-API voor relaybeheer van [NIP-86](/nl/topics/nip-86/), waarmee een beheerder de relay kan vragen een event met de eigen pubkey van de relay te ondertekenen. De bijbehorende [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) definieert een Relay Roles-event: een vervangbaar event dat een relay publiceert om zijn beheerders en moderators bekend te maken. Samen laten ze NIP-86-clients de beheerderslijst van een relay inspecteren en zonder out-of-band-vertrouwen controleren of een geauthenticeerd verzoek van een huidige beheerder kwam. Hieronder volgt een deep dive over beide wijzigingen.

### Samengevoegd: NIP-34 vervangt `personal-fork` door `u` voor GRASP-06

[PR #2395](https://github.com/nostr-protocol/nips/pull/2395) werd op 24 juni samengevoegd en vervangt de `personal-fork`-tag van [NIP-34](/nl/topics/nip-34/) op repo-state-events (`kind:30618`) door een `u`-tag (voor "upstream"). Daarmee sluit het wire-formaat aan op de GRASP-06-forksemantiek die de GitWorkshop-suite implementeert. De wijziging sluit [PR #2384](https://github.com/nostr-protocol/nips/pull/2384) (`NIP-34: remove maintainers to solve expiry issues`), die een andere oplossing voor forksemantiek voorstelde. ngit v2.6.x implementeert de samengevoegde richting, zodat de samengevoegde specificatie en de referentie-CLI nu overeenkomen. Bestaande repo's met `personal-fork` blijven interoperabel; nieuwe repo's en ngit v2.6 publiceren de `u`-tag.

### Samengevoegd: NIP-46-clientmetadata, nu upstream nadat Amber die al leverde

[PR #2381](https://github.com/nostr-protocol/nips/pull/2381) werd op 23 juni samengevoegd en voegt optionele clientmetadata toe aan het `connect`-verzoek van [NIP-46](/nl/topics/nip-46/). Een client kan bij het verbinden met de signer zijn naam, een icoon-URL en een homepage-URL publiceren. [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) leverde de metadata-uitbreiding vorige week al (behandeld in [#28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata)); deze week haalt de upstream-NIP de bestaande implementatie in.

### Open: deterministische NIP-17-wrappersleutels per epoch

[PR #2397](https://github.com/nostr-protocol/nips/pull/2397) en [PR #2396](https://github.com/nostr-protocol/nips/pull/2396) behandelen twee naar elkaar toegroeiende voorstellen voor NIP-17-wrapsleutels. PR #2397 stelt voor om de tijdelijke ondertekeningssleutel voor een [NIP-59](/nl/topics/nip-59/)-gift wrap deterministisch af te leiden uit een seed per gesprek die aan een grove tijdsepoch is gekoppeld. Een ontvanger die de gesprekssleutel kent, kan dan voorspellen op welke pubkeys die zich moet abonneren. De huidige specificatie vereist voor elke wrap een nieuwe willekeurige sleutel, waardoor die voorspelling onmogelijk is. PR #2396 is de bijbehorende wijziging: wraps voor een bepaald gesprek zouden rechtstreeks met de gesprekssleutel moeten worden ondertekend, zodat de pubkey van de wrap ook als gespreksidentifier dient. Samen vormen ze een route naar filterbare NIP-17-gesprekken zonder metadatalekken. Beide voorstellen staan open en worden besproken.

### Open: NIP-59 moet kind-13-seal-events bij de relay weigeren

[PR #2399](https://github.com/nostr-protocol/nips/pull/2399) stelt voor dat relays kind-13-events, de binnenste seal van een [NIP-59](/nl/topics/nip-59/)-gift wrap, weigeren wanneer ze op het hoogste niveau van een publicatieverzoek verschijnen. Een seal-event is alleen zinvol binnen een wrap en een gelekte seal onthult de pubkey van de ontvanger. Het bijbehorende [issue #2398](https://github.com/nostr-protocol/nips/issues/2398) gaat verder en stelt dat de seal opnieuw moet worden gedefinieerd als tijdelijk kind (tijdelijke kinds van NIP-01 worden niet door relays opgeslagen). Dat zou de regel op protocolniveau afdwingen en de afhankelijkheid van beleid per relay wegnemen.

### Open: groepstoestanden in NIP-29

[PR #2372](https://github.com/nostr-protocol/nips/pull/2372) voegt expliciete semantiek voor groepstoestanden toe aan [NIP-29](/nl/topics/nip-29/) (relay-gebaseerde groepen). Het voorstel definieert wanneer een groep open, gesloten, openbaar, privé of gearchiveerd is en hoe toestandsveranderingen met lidgebeurtenissen omgaan. Daarmee verhuist semantiek die tot nu toe clientspecifiek was naar de relayspecificatie.

### Open: optionele ondersteuning voor meerdere maintainers in NIP-34

[PR #2324](https://github.com/nostr-protocol/nips/pull/2324) hoort bij de samengevoegde [PR #2395](https://github.com/nostr-protocol/nips/pull/2395) over de hierboven behandelde GRASP-06-forksemantiek. PR #2324 voegt optionele ondersteuning voor meerdere maintainers toe aan repository-announcement-events van [NIP-34](/nl/topics/nip-34/) (`kind:30617`). Een repository kan zo via herhaalde `maintainer`-tags meer dan één canonieke maintainer-pubkey opgeven. Clients vertrouwen patches en issues die door een van de opgegeven maintainers zijn ondertekend dan als officieel. Dat vult het lang bestaande hiaat waarbij NIP-34-repo's met co-maintainers alles via één pubkey moeten leiden of terugvallen op coördinatie buiten het protocol.

### Open: AND-operator voor filters in NIP-91; het voorstel is niet samengevoegd

[PR #2252](https://github.com/nostr-protocol/nips/pull/2252) is het voorstel voor een AND-operator voor Nostr-[filters](/nl/topics/nip-01/) en heropent een ontwerp dat eerder in de gesloten [PR #1365](https://github.com/nostr-protocol/nips/pull/1365) is besproken. Er bestaan al implementaties in [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay), applesauce, [Amethyst](https://github.com/vitorpamplona/amethyst) en worker-relay, maar de PR voor de specificatie staat nog open.

### Gesloten: vier handels-NIPs van pats2sats

Vier voorstellen voor handel op Nostr zijn deze week gesloten: Escrow ([#2334](https://github.com/nostr-protocol/nips/pull/2334)), Reservations ([#2335](https://github.com/nostr-protocol/nips/pull/2335)), een Marketplace Listing Extension voor [NIP-99](/nl/topics/nip-99/) ([#2346](https://github.com/nostr-protocol/nips/pull/2346)) en een Accommodation Listing Profile ([#2333](https://github.com/nostr-protocol/nips/pull/2333)). Hetzelfde handelsoppervlak wordt nu geconsolideerd in de [Gamma Market Spec](https://github.com/GammaMarkets/market-spec), een uitbreidingsrepository van het project zelf die boven op NIP-99-marktplaatsvermeldingen orders, checkout, escrow en geschilsemantiek samenstelt. Compass volgt deze repository nu naast Marmot en Blossom als protocolspecificatierepository buiten de NIPs-repository. Open PR's daar omvatten deze week verduidelijking van client attribution ([#11](https://github.com/GammaMarkets/market-spec/pull/11)), een `supersedes`-tag voor wijzigingen aan productidentiteit ([#8](https://github.com/GammaMarkets/market-spec/pull/8)) en semantiek voor beoordelingen van handelaars ([#7](https://github.com/GammaMarkets/market-spec/pull/7)).

### Open: koppeling van Bitcoin-identiteiten

Deze week zijn twee voorstellen geopend om Bitcoin-identiteiten aan Nostr-identiteiten te koppelen: een [NIP-352 Bitcoin Silent Payment Address](https://github.com/nostr-protocol/nips/pull/2392) en een [Bitcoin-OTC Identity Linkage Proof](https://github.com/nostr-protocol/nips/pull/2401).

---

## NIP Deep Dive: NIP-86 (Relay Management API)

[NIP-86](/nl/topics/nip-86/) definieert een JSON-RPC-interface voor relaybeheer, waarmee geautoriseerde clients via een gestandaardiseerde API administratieve opdrachten naar relays sturen. Eén client kan elke NIP-86-compatibele relay beheren zonder gereedschap per relay. Twee deze week samengevoegde specificatiewijzigingen ([PR #2389](https://github.com/nostr-protocol/nips/pull/2389) en [PR #2390](https://github.com/nostr-protocol/nips/pull/2390)) sluiten de kring tussen door relays ondertekende events en door relays bekendgemaakte beheerders.

### Het transport

Een NIP-86-beheerverzoek is een HTTP-POST naar dezelfde URI waarop de relay WebSocket-verbindingen aanbiedt, met `Content-Type: application/nostr+json+rpc`. De body van het verzoek is een JSON-document in deze vorm:

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

Authenticatie gebruikt een via HTTP-auth ondertekend event van [NIP-98](/nl/topics/nip-98/) in de `Authorization`-header. De relay controleert of de ondertekenende pubkey op zijn beheerderslijst staat voordat de methode wordt uitgevoerd. Het antwoord van de relay is een JSON-document in deze vorm:

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### De methoden die vóór deze week bestonden

De bestaande methodeset dekt bans van pubkeys (`banpubkey`, `allowpubkey`, `listbannedpubkeys`), bans van events (`banevent`, `allowevent`, `listbannedevents`), relaymetadata (`changerelayname`, `changerelaydescription`, `changerelayicon`), beheer van de lijst met toegestane kinds (`allowkind`, `disallowkind`, `listallowedkinds`) en een methode `stats` die relaystatistieken teruggeeft. De vorm ligt bewust dicht bij een standaard-JSON-RPC-service, zodat een client er typed bindings bovenop kan leggen.

### Wat deze week veranderde

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) voegt een `signevent`-methode aan de specificatie toe. De methode neemt een gedeeltelijke eventtemplate (kind, tags, content) als argument en vraagt de relay een volledig event te ondertekenen en terug te geven, met de eigen pubkey van de relay in het veld `pubkey`. Dit is de voorwaarde waaronder een relay events op protocolniveau over zichzelf kan publiceren: aankondigingen van geblokkeerde pubkeys, relaymetadata en het nieuwe Relay Roles-event hieronder moeten allemaal door de relay met de sleutel van de operator worden ondertekend. De meeste relayoperators willen echter geen privésleutel in hun administratieve client bewaren.

[PR #2390](https://github.com/nostr-protocol/nips/pull/2390) definieert een Relay Roles-event: een geparametriseerd vervangbaar eventkind dat een relay publiceert, met de eigen pubkey ondertekend via `signevent`, om de pubkeys van zijn beheerders en moderators met expliciete rolsemantiek bekend te maken. Een NIP-86-bewuste client kan het Relay Roles-event van elke gevolgde relay ophalen, de beheerderslijst uit de eventtags opbouwen en zonder out-of-band-vertrouwen of configuratie per relay controleren of een geauthenticeerd NIP-86-verzoek van een huidige beheerder kwam. De twee PR's sluiten samen de kring: `signevent` is het mechanisme en Relay Roles is het eerste eventkind dat erop voortbouwt.

### Voorbeeld van een NIP-86-verzoek

Een volledig NIP-86-`banpubkey`-verzoek ziet er zo uit:

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

met een `Authorization`-header die een door NIP-98 ondertekend event bevat:

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

De ondertekenende pubkey moet in de beheerdersset van de relay staan, die nu in het Relay Roles-event wordt bekendgemaakt; de `u`-tag moet met de HTTPS-URL van de relay overeenkomen; de `payload`-tag moet overeenkomen met de SHA-256 van de JSON-body van het verzoek. De relay antwoordt:

```json
{
  "result": true,
  "error": null
}
```

### Implementaties

- [Amethyst](https://github.com/vitorpamplona/amethyst) levert op Android een UI voor NIP-86-relaybeheer (v1.07.0+).
- Referentierelays die de specificatie implementeren zijn onder meer [strfry](https://github.com/hoytech/strfry), [khatru](https://github.com/fiatjaf/khatru) en enkele kleinere implementaties waarnaar de specificatie in `Implementation Status` verwijst.

NIP-86-bewuste clients zullen het Relay Roles-event als canonieke bron voor de beheerderslijst van een relay gaan behandelen zodra implementeerders de wijzigingen aan `signevent` en Relay Roles overnemen.

---

## NIP Deep Dive: NIP-89 (Recommended Application Handlers)

[NIP-89](/nl/topics/nip-89/) definieert twee geparametriseerde vervangbare eventkinds: `kind:31990` (de applicatiehandler die een appontwikkelaar publiceert) en `kind:31989` (de aanbeveling die een gebruiker publiceert voor een gebruikte app). Samen laten ze clients zonder out-of-band-coördinatie applicaties ontdekken die een onbekend eventkind verwerken. Een longform-lezer die een `kind:30030`-event tegenkomt dat hij niet native ondersteunt, kan de NIP-89-grafiek naar handlers doorzoeken en de gebruiker een `Open in...`-flow naar een gepubliceerde app aanbieden. NIP-89 is de oorspronkelijke infrastructuur voor hetzelfde routeringsprobleem tussen apps dat het napplet-/napps-werk in dit nummer nu uitbreidt naar samenstelbare, Nostr-native applets.

### Het applicatiehandlerevent (`kind:31990`)

Een appontwikkelaar publiceert een of meer handlerevents die beschrijven welke eventkinds de app ondersteunt en hoe een Nostr-entiteit in de app wordt geopend:

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

De `d`-tag identificeert de handler, zodat die kan worden vervangen. Elke `k`-tag vermeldt een eventkind dat de app verwerkt en elke platformtag (`web`, `ios`, `android`, ...) geeft een URL-template waarin `<bech32>` de placeholder is voor een via [NIP-19](/nl/topics/nip-19/) gecodeerde entiteit die de aanroepende client bij het openen invult. Eén handlerevent kan meerdere ondersteunde kinds adverteren als ze hetzelfde routeringspatroon delen. Dat houdt appontdekking compact en voorkomt één handlerevent per kind.

### Het aanbevelingsevent van de gebruiker (`kind:31989`)

Een gebruiker publiceert een aanbeveling die vermeldt welke apps die voor een bepaald eventkind gebruikt:

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

De `d`-tag bevat het aanbevolen eventkind. Elke `a`-tag is een NIP-01-adresverwijzing naar een `kind:31990`-handlerevent, met de voorgestelde relay en het platform waarop de aanbeveling van toepassing is. Dezelfde aanbeveling kan meerdere apps voor verschillende platforms vermelden.

### De clienttag en de privacyafweging

NIP-89 definieert ook een optionele `client`-tag die elke publicerende app aan zelf geschreven events kan toevoegen:

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

Hierdoor kan elke client die het event toont ook de app van herkomst tonen, rijkere handlermetadata opzoeken en door de handler opgegeven renderhints respecteren. De specificatie benoemt ook expliciet de privacykosten: een client die op elk event een `client`-tag plaatst, publiceert welke software de gebruiker inzet en onthult daarmee na verloop van tijd gebruikspatronen. De specificatie adviseert clients gebruikers een opt-out te geven.

[PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422) van Amethyst parset en toont de NIP-89-tags `t`, `i`, `a` en `client` bij de eventweergave, zodat direct in de tijdlijn zichtbaar wordt welke app een note schreef.

### Hoe de ontdekkingsflow in de praktijk verloopt

Een client die een onbekend eventkind ontvangt, doorloopt de volgende stappen. (1) Doorzoek de volgrafiek van de gebruiker naar `kind:31989`-events met een `d`-tag die met het eventkind overeenkomt. (2) Los elke aanbevolen `a`-tag op naar het bijbehorende `kind:31990`-handlerevent. (3) Kies de handler waarvan de URL-template voor `web`, `ios` of `android` bij het huidige platform past. (4) Vul de `bech32`-codering van de entiteit in de URL-template in. (5) Bied de resulterende URL aan als keuze voor `Open in...`. De flow wordt sociaal gefilterd: een client die willekeurige handlerevents van onvertrouwde relays opvraagt, kan gebruikers naar schadelijke apps doorsturen. Beginnen bij mensen die de gebruiker volgt, is daarom veiliger dan elke gepubliceerde handler even betrouwbaar te behandelen.

### NIP-89 en de nappletlaag

De Discover-sectie, napplet-host-runtime en weergave van `client`-tags in Amethyst vormen samen een volledig NIP-89-consumentenoppervlak op Android. De nappletspecificatie uit het vorige nummer breidt uit waarnaar die NIP-89-handlerevents kunnen verwijzen: sandboxed applets die een samenstelbare, Nostr-native runtime op Nostr en Blossom draaien. NIP-89 is de grafiek voor ontdekking en routering; de napplet-runtime is een uitvoeringsdoel waarnaar die grafiek kan wijzen.

---

*Feedback, correcties en projecten die we hebben gemist: open een issue op [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass) of bereik ons via een NIP-17-DM op npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923.*
