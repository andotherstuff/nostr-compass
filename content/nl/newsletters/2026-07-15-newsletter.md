---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
draft: false
type: newsletters
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
description: "Vector v0.4.0 zet Marmot opzij voor groepschats ten gunste van het open Concord-protocol en levert dagen later Concord v2, Amethyst voegt zijn eigen clean-room Concord-implementatie samen, Sonar splitst zich af van Bitchat met een cross-platform alpha en een stickerpakket-specificatie, Divine Mobile 1.0.16 levert versleuteling in rust en ProofMode-herkomst, Bitchat 1.7.0 voegt live push-to-talk-spraak toe, en MDK v0.9.4 begrenst het inloggen met een externe ondertekenaar."
---

Welkom terug bij Nostr Compass, uw wekelijkse gids voor Nostr.

**Deze week:** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) zet [Marmot](/nl/topics/marmot/) opzij als standaardtransport voor Groepschats ten gunste van [Concord](/nl/topics/concord-protocol/), een open, MIT-gelicentieerd gemeenschapsprotocol dat ook door Armada van Soapbox wordt gebruikt, en levert vier dagen later Concord v2 met een slash-commandokiezer voor bots, een zelfvernietigingstimer en NIP-58-badges. [Amethyst voegt zijn eigen clean-room, wire-compatibele Concord-implementatie samen](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) in dezelfde week. [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) splitst zich af van Bitchat met een cross-platform alpha en is de geciteerde specificatiebron voor het stickerpakket-kindsvoorstel van deze week. [Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) levert een diepere video-editor, versleuteling in rust en ProofMode-herkomst die het downloaden van clips met watermerk overleeft. [Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) voegt live push-to-talk-spraak toe voor DMs en ondertekende push-to-talk op het publieke mesh. [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) begrenst het inloggen met een externe ondertekenaar en voegt persistentie van concepten toe, waarmee het zijn hardeningsronde voortzet in dezelfde week dat Vector afstand neemt van de specificatie voor groepschat.

Getagde releases brengen [n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) met ondersteuning voor NSEC Bunker, [cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) met NIP-47 wallet-serviceondersteuning in cdk, cdk-nwc en cdk-ffi, [Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) met verbeteringen aan Nostr Connect en ncryptsec1-import, [Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) dat op macOS landt met gepland verzenden, [Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) met een DM-hoofdschakelaar, [Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) dat sleutelback-ups verstevigt naar het NIP-49-formaat, [Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) met FROST-onboarding bij eerste gebruik, [Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) met een Cashu-wallet en relay-gebaseerde pushmeldingen, [Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) met tabletmodus en foto's in groepschats, en [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) met hulpverzoeken voor git, diff en het lezen van bestanden.

Aan de niet-uitgebrachte kant laat [Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) accounts contacten een bijnaam geven met versleutelde NIP-85-kaarten verspreid over 54 samengevoegde PRs, levert [Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) fase 3 van My Kitchen en repareert een quorumfout in de NDK-pool, streamt [Kehto](#kehto-streams-outbox-reads-before-relay-discovery) outbox-leesbewerkingen voordat relaydetectie klaar is, voegen [Wired en TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) NIP-57 inkomstendeling voor makers toe, herbouwt [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) zijn bestellingeninbox voor verkopers rond efemeer afrekenen als gast, verstevigt [Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) de provisioning van kanaalmakers over 240 samengevoegde PRs, en adopteert [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) een NIP-49-ondertekenaar met meerdere accounts en QR-koppeling. Deze week nieuw gevolgd: [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr), [Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles), en de Discovery-keuze [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer), een sleutelloze NIP-55-ondertekenaar die doorschakelt naar een Heartwood-hardwaremetgezel.

De NIPs-repository voegt de afgelopen week niets samen en opent zes voorstellen: [kind:10011 favoriete volgsets](#open-kind10011-favorite-follow-sets), een [privé versleutelde schijf die NIP-4E uitbreidt](#open-private-encrypted-drive-extends-nip-4e), [NIP-DA privé gegevensdeling met permissies](#open-nip-da-permissioned-private-data-sharing), [stickerpakket-kinds 10031 en 30031](#open-sticker-pack-kinds-10031-and-30031), [NIP-29 berichten vastzetten](#open-nip-29-message-pinning-with-kind9010-and-kind39005), en een [herstructurering van NIP-66 relaydetectie](#open-nip-66-relay-discovery-restructure). De Deep Dive behandelt [NIP-99 en de Gamma Markets-handelsuitbreiding](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension).

---

## Hoofdverhalen

### Vector v0.4.0 verplaatst Groepschats van Marmot naar Concord, en Amethyst levert dagen later zijn eigen Concord-client

[Vector](https://github.com/VectorPrivacy/Vector) is een Nostr-messenger gebouwd rond een privacy-eerst client met één binary voor DMs en groepschats. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) herschrijft de berichtenengine van de app tot een gedeelde `vector-core`-bibliotheek en zet in dezelfde release [Marmot](/nl/topics/marmot/) (MLS-over-Nostr) opzij als standaardtransport voor Groepschats ten gunste van [Concord](/nl/topics/concord-protocol/), een end-to-end versleuteld gemeenschapsprotocol; bestaande Marmot-groepsgeschiedenis gaat niet mee, en de release notes zeggen gebruikers hun Marmot-groepsgegevens te back-uppen voor het upgraden. Vectors eigen release notes beschrijven Concord als "ons eigen berichtenprotocol", maar de onderliggende [CORD-01 tot en met CORD-07-specificaties](https://github.com/concord-protocol/concord) worden apart gepubliceerd, zijn MIT-gelicentieerd en al buiten Vector geïmplementeerd: Soapbox' Discord-achtige client [Armada](https://gitlab.com/soapbox-pub/armada) bouwt zijn Communities-functie op dezelfde Concord-specificatie, en één dag later [voegde Amethyst zijn eigen clean-room, wire-compatibele Concord-implementatie samen](https://github.com/vitorpamplona/amethyst/pull/3566), hieronder volledig behandeld. Dezelfde Vector-release voegt optionele Tor-routering voor al het verkeer toe, [NIP-46](/nl/topics/nip-46/) inloggen met een externe ondertekenaar via QR of geplakte bunker-URI, meerdere accounts met een schakelaar in de app, en aangepaste emojipakketten die tussen clients worden gedeeld. Het verwijderen van een bericht haalt het bij beide kanten weg in DMs en groepschats, en Vector houdt bewust de efemere ondertekeningssleutel in plaats van de standaard [NIP-17](/nl/topics/nip-17/)-verwijderstroom te volgen, een door privacy ingegeven afwijking die het project expliciet benoemt in de release notes. Vier dagen later levert [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) **Concord v2**, beschreven als een release met grote privacy- en stabiliteitsverbeteringen voor Communities terwijl bestaande blijven werken, samen met een Discord-achtige slash-commandokiezer voor bots met getypeerde parameters, een zelfvernietigingstimer per chat, en een NIP-58-badgesysteem voor bugjagers. De stap weg van Marmot voor groepschat komt in dezelfde week waarin [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) hieronder blijft investeren in de specificatie.

### Amethyst levert een clean-room Concord-implementatie voor end-to-end versleutelde gemeenschappen

[Amethyst](https://github.com/vitorpamplona/amethyst) is een functierijke Nostr-client voor Android en meerdere platforms. [PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) voegt een volledige implementatie van [Concord](/nl/topics/concord-protocol/) (CORD-01 tot en met CORD-07) toe die serverloze, end-to-end versleutelde gemeenschappen dekt: gift-wrapped controle-, chat- en gastenboekvlakken over gewone relay's, handhaving van rollen en bans geworteld bij de eigenaar die elke client lokaal verifieert in plaats van een server te vertrouwen, en herkeying om verwijderde leden af te snijden. Protocol- en cryptocode zit in `quartz/`, state- en viewmodels in `commons/`, en schermen en navigatie in `amethyst/` voor Android, met dunne CLI-werkwoorden onder `cli/`; er is nog geen desktop-UI, omdat de gedeelde logica in `quartz`/`commons` zit zodat Desktop die later kan overnemen. De implementatie is clean-room: gebouwd vanuit de publieke CORD-specificaties en waargenomen wire-constanten, onder Amethysts eigen MIT-licentie, los van Armada's AGPL-3.0-codebase. Armada's eigen testvectorwaarden zijn overgezet naar de unittests van Quartz om te bevestigen dat de twee clients daadwerkelijk op de wire interopereren, waarmee Concord binnen enkele dagen drie onafhankelijke implementaties heeft: Vector die als eerste leverde, Armada als referentieclient van Soapbox, en nu Amethysts bouw vanaf de specificatie.

### Sonar splitst zich af van Bitchat met een cross-platform alpha en een stickerpakket-specificatie

[Sonar](https://sonarprivacy.xyz/) is een messenger en wallet met Bluetooth-mesh plus Nostr, gegroeid uit Bitchat, met Marmot-groeps-DMs die interopereren met White Noise. De code staat op [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar). [v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) voegt begrensde transcript-vensters in Signal-stijl toe zodat openen en scrollen local-first blijven presteren, synchroniseert de staat van detectie in de buurt tussen peers, en repareert Blossom-media-uploads die faalden op content-type- en HTTP-statusafhandeling; de voorafgaande [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) liet live Marmot-events leeglopen voor sneller vernieuwen van de chat en dichtte gaten in functiepariteit tussen Android en iOS bij gesprekken, berichten, wallet en push. Sonar is ook de geciteerde specificatiebron voor [PR #2410](#open-sticker-pack-kinds-10031-and-30031), die stickerpakket-eventkinds registreert onder de eigen "Sonar Stickers"-specificatie van het project, wat deze lancering een directe link geeft naar het protocolwerk van deze week.

### Divine Mobile 1.0.16 levert een diepere video-editor, versleuteling in rust en ProofMode-herkomst

[Divine](https://github.com/divinevideo/divine-mobile) is een client voor korte video's gebouwd op Nostr met feedcuratie via Web-of-Trust. [v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16), de eerste getagde release sinds #30, voegt clipovergangen, achterwaarts afspelen, een voice-overrecorder en beatmarkeringen op de tijdlijn toe aan de video-editor, samen met een feedafstemming waarmee een gebruiker kan swipen om aanbevelingen direct bij te stellen in plaats van ze over te laten aan ondoorzichtige engagementsignalen. De release zet ook versleuteling in rust aan voor lokale gegevens, voegt uploads op de achtergrond toe die overleven wanneer de app wordt onderbroken, en draagt [ProofMode](/nl/topics/proofmode/)-herkomstgegevens mee wanneer een clip met watermerk wordt gedownload zodat de verklaring van menselijke makelij niet onderweg verdwijnt. Divine levert ook nieuwe bescherming voor accounts van onder de 16 en breidt de lokalisatie uit naar 17 talen en 284 vertaalde teksten.

### Bitchat v1.7.0 voegt live push-to-talk-spraak toe voor DMs en het publieke mesh

[Bitchat](https://github.com/permissionlesstech/bitchat) is een chat-app met Bluetooth-mesh en een opt-in gateway naar Nostr-relay's. [v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0), uitgebracht op de avond dat #30 verscheen, voegt live push-to-talk-spraak toe in [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) die audio streamt zolang de zender de knop ingedrukt houdt en terugvalt op een spraakbericht als de stream wegvalt, plus ondertekende push-to-talk op het publieke mesh in [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406) zodat live spraakflarden op het gedeelde meshkanaal authenticatie van de zender meedragen. De release herstelt ook peer-ID-rotatie door de link opnieuw te binden bij een geverifieerde her-aankondiging, waarbij dezelfde peer onder zijn nieuwe ID wordt herkend ([PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)), en directe berichten naar een momenteel onbereikbare peer komen nu in de wachtrij met store-and-forward-bezorging in plaats van meteen te falen ([PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)). Dit sluit direct aan op de behandeling in #30 van het [NIP-13](/nl/topics/nip-13/) proof-of-work- en mesh-naar-Nostr-gatewaywerk in v1.6.0.

### MDK v0.9.4 begrenst het inloggen met een externe ondertekenaar en voegt persistentie van concepten toe

[MDK](https://github.com/marmot-protocol/mdk) is de referentie-SDK voor het [Marmot](/nl/topics/marmot/)-protocol, de MLS-over-Nostr berichtenlaag waarvan #30 behandelde dat de specificatie als geadopteerd werd gemarkeerd. [v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) begrenst de adviserende directorystappen die een client doorloopt bij het inloggen met een externe ondertekenaar in [PR #793](https://github.com/marmot-protocol/mdk/pull/793), wat een onbegrensde herhaallus voorkomt wanneer een externe ondertekenaar traag is of niet reageert. Dezelfde release voegt persistentie van conceptberichten en bindingen tussen profiel en website toe in [PR #812](https://github.com/marmot-protocol/mdk/pull/812), waarmee de stapsgewijze hardeningsronde doorloopt die MDK sinds v0.9.0 uitvoert.

---

## Getagde releases

### n_cord v1.1 voegt ondersteuning voor NSEC Bunker toe

[n_cord](https://github.com/0n4t3/n_cord) is een chatclient op Nostr geïnspireerd door Discord en IRC. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) voegt [NIP-46](/nl/topics/nip-46/) NSEC Bunker-ondersteuning toe naast een bugfix in de afhandeling van antwoorden.

### cdk v0.17.3 voegt NIP-47 wallet-serviceondersteuning toe in cdk, cdk-nwc en cdk-ffi

[cdk](https://github.com/cashubtc/cdk) is een Cashu-ontwikkelkit; deze release is in de meeste opzichten alleen Bitcoin/Lightning, maar [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) voegt [NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect) serviceondersteuning toe met een aparte NWC-servicecrate, wallet-integratie, FFI-bindings voor `cdk-ffi`, en end-to-end testdekking, waarmee Cashu-wallets gebouwd op cdk een standaard Nostr Wallet Connect-oppervlak krijgen.

### Coop Mobile v0.2.4 verbetert Nostr Connect en voegt ncryptsec1-import toe

[Coop Mobile](https://git.reya.su/reya/coop-mobile) is een [NIP-17](/nl/topics/nip-17/)-client voor privéberichten op mobiele platforms. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) verbetert de [NIP-46](/nl/topics/nip-46/) Nostr Connect-stroom, repareert een laadindicator die bij sommige verbindingen permanent bleef hangen, en voegt importondersteuning toe voor het [NIP-49](/nl/topics/nip-49/) `ncryptsec1` versleutelde sleutelformaat, samen met een herontworpen scherm voor identiteitsimport.

### Nmail v0.14.0 landt op macOS met gepland verzenden en pushmeldingen

[Nmail](https://github.com/nogringo/nostr-mail-client) is een mailclient gebouwd op Nostr; [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) brengt de app naar macOS, voegt gepland verzenden toe met een aparte Gepland-mailbox voor berichten in de wachtrij, en voegt pushmeldingen toe. De release schakelt het oplossen van Nostr-identifiers in het adresboek ook over naar NDK's [NIP-05](/nl/topics/nip-05/)-resolver in plaats van een eigen implementatie.

### Nostrord v2.2.0 voegt een DM-hoofdschakelaar en rijkere directe berichten toe

[Nostrord](https://github.com/nostrord/nostrord) is een [NIP-29](/nl/topics/nip-29/) relay-gebaseerde groepschatclient voor Android, iOS, web en desktop. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) voegt een hoofdschakelaar toe om alle functies voor directe berichten in één keer uit te schakelen ([PR #175](https://github.com/nostrord/nostrord/pull/175)) en levert "rijkere directe berichten" ([PR #186](https://github.com/nostrord/nostrord/pull/186)), voortbouwend op de behandeling in #30 van de release die de relaypool samenvoegde en zombie-WebSockets detecteerde.

### Nostr WoT 0.3.86 verstevigt sleutelback-ups en ondertekeningsprompts

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) is een browserextensie die een Nostr-identiteit koppelt aan een Lightning-wallet. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) verplaatst versleutelde sleutelback-ups naar het standaard [NIP-49](/nl/topics/nip-49/)-formaat, laat ondertekeningsprompts het volledige event en alle tags tonen in plaats van een samenvatting, verifieert relaygegevens tegen hun handtekening, en stopt met het blootgeven van de actieve identiteit bij het wisselen van account. De extensie laat ook de ongebruikte `scripting`-browserpermissie vallen.

### Keep Android v1.1.8 voegt FROST-onboarding bij eerste gebruik toe

[Keep](https://github.com/privkeyio/keep-android) is een Android-ondertekenaar gebouwd op FROST-sleuteldelen met drempelwaarde. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) voegt een stroom bij eerste gebruik toe die FROST-sleuteldelen uitlegt en een nieuwe gebruiker een ondertekeningsbeleid van Handmatig, Basis of Automatisch laat kiezen voordat het eerste ondertekeningsverzoek binnenkomt, de eerste onboarding aan de Android-kant voor het drempelondertekeningsmodel van de onderliggende keep-mobile-crate.

### Noscall v0.6.0 voegt een Cashu-wallet en relay-gebaseerde pushmeldingen toe

[Noscall](https://github.com/sanah9/noscall) is een app voor veilige audio- en videogesprekken gebouwd op Nostr. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) voegt een Cashu-wallet per account toe met saldi over meerdere mints, verzenden en ontvangen van ecash, en Lightning betalen en ontvangen met persistentie van quotes. De release migreert Android-pushmeldingen ook weg van Firebase Cloud Messaging naar een bezorgpad via Nostr-relay's met UnifiedPush, en verbetert de betrouwbaarheid van iOS VoIP en APNs-push tijdens herhaalde inlogpogingen.

### Kubo levert tabletmodus en foto's in groepschats

[Kubo](https://github.com/JeroenOnNostr/kubo) is een kindveilig Nostr-videoplatform met feedcuratie via Web-of-Trust. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) voegt een optionele rasterindeling voor tablets toe aan de kinderfeed en ondersteuning voor het bijvoegen van foto's bij groepschatberichten, plus fixes voor de aanmeldknop die op Android achter het schermtoetsenbord verdween.

### Nostr Codex Phone v0.2.9 voegt hulpverzoeken voor git/diff/bestand lezen toe

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) is een mobiel bedieningsoppervlak voor een lokale coding-assistent-worker die communiceert over versleutelde Nostr-DMs. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) voegt mobiele OpenCode-toolacties toe waaronder hulpverzoeken voor git, diff, bestand lezen, status en geschiedenis, verbeteringen aan het vastzetten en doorzoeken van sessies, en een besturing om taken te stoppen, naast een versleutelde [Blossom](/nl/topics/blossom/)-uploadwrapper die in de voorafgaande v0.2.8 werd geleverd.

### GitWorkshop v3.0.3 repareert nieuw aangekondigde refs in de repo-verkenner, en levert zijn eerste Android-build

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) is een git-over-Nostr web-UI voor het bekijken en beoordelen van NIP-34-repository's. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) repareert de weergaven voor branches, tags, commits en codeverkenning die een ref niet konden oplossen die een repo aankondigt nadat de verkenner die al had geladen, samen met opruiming van CI-workflowtiming, direct bevestigd tegen de tag- en commitgeschiedenis. In dezelfde week publiceerde GitWorkshop zijn eerste native Android-build op [Zapstore](https://zapstore.dev), beginnend bij v3.0.0 en binnen uren op v3.0.3; de web-UI blijft de primaire interface, en het Android-pakket brengt hetzelfde bladeren door NIP-34-repository's voor het eerst naar een telefoon.

### Bitcoin-Safe bereikt Flathub, wat de Nostr Sync & Chat-plugin voor het voetlicht brengt

[Bitcoin-Safe](https://bitcoin-safe.org) is een Bitcoin-wallet in eigen beheer gebouwd rond werkstromen met hardware-ondertekenaars. Het project [bracht deze week een Flathub-pakket uit](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe), zijn eerste vermelding in een gangbare Linux-appstore. De Flathub-release zet Bitcoin-Safe's Sync & Chat-plugin voor een breder publiek: de plugin gebruikt [NIP-17](/nl/topics/nip-17/) directe berichten, via de eigen [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat)-bibliotheek van het project, om wallet-labels tussen de apparaten van een gebruiker te synchroniseren en om PSBTs te versturen en te ontvangen voor multisig-medeondertekening op afstand tussen vertrouwde deelnemers. De Nostr-laag zelf verscheen eerder, in [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0) (2026-06-29), die het ondertekenen van transacties herontwierp rond een verbindingstype "Share via Chat & Sync" naast QR, USB en Bluetooth. Het nieuws van deze week is dat de Flathub-verpakking die bestaande functie voor het eerst voor een gangbaar Linux-publiek brengt.

---

## Niet-uitgebrachte wijzigingen

### Amethyst laat accounts contacten een bijnaam geven met versleutelde NIP-85-kaarten

Naast de [Concord-implementatie](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) die hierboven is behandeld, voegde Amethyst de afgelopen week 54 andere PRs samen. De belangrijkste daarvan is [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548), die een account elke andere gebruiker een bijnaam laat geven door een eigen kind 30382 [NIP-85](/nl/topics/nip-85/)-contactkaart over hen te publiceren. De bijnaam, een privénotitie, en eventuele aangepaste [NIP-30](/nl/topics/nip-30/) emoji-shortcode-toewijzingen leven binnen de met [NIP-44](/nl/topics/nip-44/) versleutelde inhoud van de kaart, zodat alleen het ondertekenende account ze kan lezen, en kaarten synchroniseren via de uitgebreide outbox-relayset van het account bij het inloggen en daarna stapsgewijs. Feeds, chats en vermeldingen tonen de bijnaam in plaats van de publieke weergavenaam, met een aantikbare bijnaamkaart op de profielpagina boven de echte naam van de gebruiker.

### Zap Cooking levert fase 3 van My Kitchen en repareert een quorumfout in de NDK-pool

[Zap Cooking](https://github.com/zapcooking/frontend) is een app voor het delen van recepten en een kookgemeenschap gebouwd op Nostr. Het voegde 43 PRs samen die de maaltijdplanningsfunctie "My Kitchen" voortzetten, met in deze fase het genereren van boodschappenlijstjes, een receptkiezer en een weekraster voor de planner. Dezelfde reeks wijzigingen repareert een quorumgereedheidsfout in de verbindingspool van [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit) waardoor relayleesbewerkingen konden blijven wachten voorbij het punt waarop een quorum van relay's al had geantwoord.

### Kehto streamt outbox-leesbewerkingen voor relaydetectie

[Kehto](https://github.com/kehto/web) is een vroege webruntime voor [NIP-5D](/nl/topics/nip-5d/) Nostr-applets, oftewel "napplets". Het voegde 26 PRs samen. [PR #193](https://github.com/kehto/web/pull/193) repareert outbox-leesbewerkingen die eerder wachtten tot het laden van de [NIP-65](/nl/topics/nip-65/)-relaylijst klaar was voordat er überhaupt een relay werd geopend, zodat het laden van een relaylijst dat nooit afrondde zowel de bezorging van events als querytimeouts kon blokkeren; de fix opent gevalideerde relayhints direct en streamt resultaten naarmate schrijfrelay's worden ontdekt. Een tweede wijziging ([PR #196](https://github.com/kehto/web/pull/196)) brengt de identiteitsauditpagina van het project in lijn met NAP-SHELL, het levenscycluscontract van het Napplet-platform, onderdeel van hetzelfde protocolafstemmingswerk dat elders in de `napplet/web`-release van deze week zichtbaar is.

### Wired en TAO voegen NIP-57 inkomstendeling voor makers toe

[Wired](https://github.com/smolgrrr/Wired) en [TAO](https://github.com/smolgrrr/TAO) zijn tweelingclients voor sociale media met de nadruk op vrije meningsuiting, gebouwd op Nostr en met dezelfde PR-lijst; beide voegden [PR #121](https://github.com/smolgrrr/Wired/pull/121) samen, die [NIP-57](/nl/topics/nip-57/) inkomstendeling voor makers implementeert zodat zaps naar een bericht automatisch kunnen worden verdeeld onder bijdragers buiten de oorspronkelijke plaatser. Dit sluit aan op de behandeling in #30 van het duo dat zijn proof-of-work-signaal naar 21 bits bracht als niet-uitgebracht werk.

### Conduit Mono herbouwt de bestellingeninbox voor verkopers rond efemeer afrekenen als gast

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) is een marktplaatsprotocol dat grenst aan [NIP-99](/nl/topics/nip-99/)-advertenties. [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) voegt afrekenen als gast toe met een door de browser gegenereerde efemere sleutel: de gast stuurt een versleutelde bestelling en een betalingsrapport naar de verkoper met die eenmalige sleutel, en de verkoper neemt buiten het kanaal om contact op per telefoon of e-mail, zodat de koper nooit een blijvende inbox-identiteit nodig heeft. [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) herbouwt de bestellingeninbox voor verkopers rond één gedeeld bestelstatusmodel, scheidt de rollen van koper en verkoper, en vereist een trackingcode en vervoerder voordat een fysieke of gemengde bestelling naar verzonden kan gaan. De afrekenstroom van het project bouwt op [NIP-17](/nl/topics/nip-17/) privéberichten, [NIP-44](/nl/topics/nip-44/)-versleuteling en [NIP-59](/nl/topics/nip-59/) gift wrap. De [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) van deze week behandelt de [Gamma Markets](/nl/topics/gamma-markets/)-conventies waar ditzelfde bestelstatusprobleem naartoe werkt.

### Buzz verstevigt de provisioning van kanaalmakers rond kind 39002

[Buzz](https://github.com/block/buzz) is een communicatieplatform als zwermgeest dat AI-agents en mensen over Nostr verbindt. Het voegde de afgelopen week 240 PRs samen, waarmee het zijn hardeningsboog in de relaylaag voortzet vanaf de behandeling in #30 van kind 44200 agent-beurtmetrieken. De fix van deze week ([PR #1830](https://github.com/block/buzz/pull/1830)) behandelt de maker van een kanaal als lid voordat de kind 39002 kanaalprovisioningslogica draait, wat een race sluit waarbij het eigen kanaal van de maker hem tijdens de opzet kon weigeren.

### Nostr Docs adopteert een NIP-49-ondertekenaar met meerdere accounts en QR-koppeling

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) is een Nostr-native applicatie voor samenwerken aan documenten. Het voegde 5 PRs samen, waarvan de opvallende ([PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)) het `@formstr/signer`-pakket adopteert voor volledige [NIP-49](/nl/topics/nip-49/)-authenticatie met wisselen tussen meerdere accounts en QR-koppeling, ter vervanging van een eerder eigen ondertekeningspad.

### Ook geleverd

Kleinere fixes voor ondertekenaar-interoperabiliteit en betrouwbaarheid landden de afgelopen week bij verscheidene gevolgde projecten zonder genoeg nieuw oppervlak voor een eigen alinea: [ngit-cli](https://github.com/DanConwayDev/ngit-cli), een commandoregelclient voor een op Nostr gebaseerd alternatief voor GitHub, levert [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3) waarmee `ngit init` bruikbare instelaanwijzingen geeft in plaats van herhaaldelijk om een nsec te vragen; [Manent](https://github.com/dtonon/manent), een privé-app voor versleutelde notities en bestanden gebouwd op Nostr, levert [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1) die het inloggen met een Android-ondertekenaar repareert wanneer Amber een hex-pubkey teruggeeft en het scrollen bij bunker-login verbetert; [NoorNote](https://github.com/77elements/noornote), een slanke Nostr-client zonder Google-diensten, levert [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8) die gemiste meldingen van Nostrord-groepen repareert en een schakelaar voor waarschuwingen bij eigen berichten toevoegt; [Bray](https://github.com/forgesworn/bray), een vertrouwensbewuste Nostr-MCP-server voor AI-agents en mensen, levert [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0) die metadata met de clientnaam meestuurt bij [NIP-46](/nl/topics/nip-46/) bunker-connect; [Lumilumi](https://github.com/TsukemonoGit/lumilumi), een Nostr-webclient, cachet [NIP-65](/nl/topics/nip-65/)-relaylijsten in lokale opslag als offline terugval; [Earthly](https://github.com/moogmodular/earthly), een op Nostr gebaseerde app voor lokale stad en gemeenschap, voegt [NIP-50](/nl/topics/nip-50/) geozoeken toe; en [lnbits](https://github.com/lnbits/lnbits), een gratis en opensource systeem voor Lightning-wallets en -accounts, levert [PR #3925](https://github.com/lnbits/lnbits/pull/3925) waarmee `send_nostr_dm` niet-blokkerend publiceert binnen een verder op Lightning gerichte release.

---

## Nieuw gevolgd en ontdekt

### OpenDiscord v1.0.1 lanceert als een Discord-achtige client op Nostr

[OpenDiscord](https://github.com/sofia-gros/open-discord) is een Discord-achtige client met servers en kanalen gebouwd op Nostr met rolgebaseerde permissies en WebRTC/SFU-spraaklobby's. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) is de eerste getagde installerrelease van het project.

### Auditable Voting v0.1.140 stemt de rollen van organisator, kiezer en auditproxy op elkaar af

[Auditable Voting](https://github.com/tidley/auditable-voting) is een stemschil op Nostr die volledig in de client draait. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) stemt de rollen van organisator, kiezer en auditproxy af op het exacte, door de organisator ondertekende publieke event met de vragenlijstdefinitie, wat een gat dicht waarbij een auditproxy kon handelen op verouderde gegenereerde accounts of op staat die van een andere worker of organisator was blijven staan.

### Cambium v0.3.2 koppelt met Heartwood als een sleutelloze NIP-55-ondertekenaar

[Cambium](https://github.com/forgesworn/cambium) is de Discovery-keuze van dit nummer: een Android [NIP-55](/nl/topics/nip-55/)-ondertekenaar die zelf geen privésleutelmateriaal bewaart en elk ondertekeningsverzoek over [NIP-46](/nl/topics/nip-46/) doorstuurt naar een bijbehorende Heartwood-hardware-ondertekenaar. Het project deelt de GitHub-organisatie `forgesworn` met het gevolgde project Bray, en Heartwood zelf kwam in #30 aan bod met de relay-naar-serieel ondertekeningsbrug waarmee de Android-kant van Cambium nu praat. [v0.3.2](https://github.com/forgesworn/cambium) polijst het goedkeuringsvenster zodat het live waarschuwt wanneer de gekozen identiteit afwijkt van de bestaande binding van de app, en verplaatst het schrijven van het activiteitenlogboek naar één niet-blokkerende wachtrij.

### Ook gelanceerd deze week: echoes, Dispatch en Linky

Drie andere lanceringen verdienen deze week een vermelding. [echoes](https://github.com/Lwb89dev/echoes) is een offline-first, end-to-end versleutelde notitie-app die privé synchroniseert over Nostr. [Dispatch](https://github.com/freecritter/dispatch) is een local-first reisplanner waarbij elke opslag met [NIP-44](/nl/topics/nip-44/) is versleuteld en over Nostr wordt geback-upt onder een aparte, niet-koppelbare sleutel, en de release [v0.3.0](https://github.com/freecritter/dispatch) voegt Amber [NIP-55](/nl/topics/nip-55/)-login toe zodat de app de privésleutel van de gebruiker nooit direct aanraakt. [Linky](https://github.com/hynek-jina/linky) combineert Nostr-contacten en -DMs met Lightning- en Cashu-betalingen in één progressieve webapp.

---

## Protocolwerk en NIP-updates

Er zijn de afgelopen week geen PRs samengevoegd in de [NIPs-repository](https://github.com/nostr-protocol/nips). Zes voorstellen zijn geopend.

### Open: kind:10011 favoriete volgsets

[PR #2413](https://github.com/nostr-protocol/nips/pull/2413), van fiatjaf, voegt kind:10011 favoriete volgsets toe. Het spiegelt het bestaande patroon waarbij kind:10012 (favoriete relaysets) `a`-tags bevat die naar kind:30002-relaysets wijzen, en breidt hetzelfde favorietenmechanisme uit naar kind:30000-volgsets zodat een client een samengestelde volglijst kan bewaren zonder zijn eigen contactenlijst te vervangen.

### Open: privé versleutelde schijf breidt NIP-4E uit

[PR #2412](https://github.com/nostr-protocol/nips/pull/2412), van het Form*-team, stelt een generiek Metadata-event voor, kind 34578, onderscheiden door een `d`-identifiertag en een `t`-subtypetag, samen met een privé versleuteld bestandssysteem daarbovenop dat al is geïmplementeerd in Form*'s eigen, nog experimentele Form* Drive-client. Een bestandsrecord is een Metadata-event met `t=files`: bestandsblobs staan op [Blossom](/nl/topics/blossom/)-servers terwijl alleen een versleutelde index op relay's staat, en elk bestandsdeel krijgt zijn eigen efemere sleutelpaar met [NIP-44](/nl/topics/nip-44/) v2 HKDF-afgeleide versleuteling. Een bijbehorend Decoupled Encryption Key-event bevat één symmetrische sleutel voor de hele schijf waartegen de metadata van elk bestand ontsleutelt, en het bouwt expliciet voort op [NIP-4E](/nl/topics/nip-4e/), fiatjafs nog openstaande concept voor opslagabstractie ([PR #1647](https://github.com/nostr-protocol/nips/pull/1647), open sinds december 2024).

Die ene schijfbrede sleutel betekent dat een gelekte sleutel de metadata van elk bestand op de schijf blootlegt, niet alleen van één bestand, aangezien de efemere sleutelparen per bestand alleen de versleutelingssleutel van het deel variëren en niet de ontsleutelingssleutel van de metadata; er bestaat nog geen pad voor rotatie of intrekking behalve een nieuw Metadata-event publiceren met de waarschuwing dat oudere events verloren kunnen gaan. Een tweede, smaller voorstel reikt vanuit een andere hoek naar hetzelfde onderliggende NIP-4E-idee: [PR #2361](https://github.com/nostr-protocol/nips/pull/2361), van fiatjaf, ontkoppelt identiteits- en versleutelingssleutels specifiek binnen [NIP-17](/nl/topics/nip-17/)-berichten, open sinds 1 juni. Beide PRs zijn niet samengevoegd, waardoor dit een actieve, betwiste hoek van de ontwerpruimte blijft. Form* zegt dat de Drive-client experimenteel is en dat er binnenkort een update komt.

### Open: NIP-DA privé gegevensdeling met permissies

[PR #2411](https://github.com/nostr-protocol/nips/pull/2411), van JAFairweather, is een nieuw NIP-DA-concept voor privé gegevensdeling met permissies via afgebakende gegevenstoekenningen. Elke gebruiker houdt per scope één versleuteld, gezaghebbend record op relay's, en toegang wordt verleend door de symmetrische sleutel van die scope privé te bezorgen in een [NIP-59](/nl/topics/nip-59/) gift wrap, zodat relay's alleen cijfertekst opslaan en nooit te weten komen wie wie toegang gaf; een intrekking is enkel een sleutelrotatie, zonder de kopie van elke consument te hoeven herschrijven. De auteur positioneert het als onderscheiden van [NIP-17](/nl/topics/nip-17/)-DMs (die een momentopname van gegevens kunnen dragen maar geen live updates of intrekking) en van NIP-51 privélijsten (die geen sleutelmateriaal dragen), en noemt twee onafhankelijke implementaties, een JavaScript-referentiebibliotheek en een Go-CLI op go-nostr, kruislings getest tegen relay.damus.io, nos.lol en relay.primal.net.

### Open: stickerpakket-kinds 10031 en 30031

[PR #2410](https://github.com/nostr-protocol/nips/pull/2410), van vincenzopalazzo, registreert kind 30031 (adresseerbare stickerpakketten) en kind 10031 (de stickerpakketlijst van een gebruiker) in de Event Kinds-tabel, gespecificeerd door het "Sonar Stickers"-formaat dat [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) deze week levert. De kinds zitten bewust één plek boven de [NIP-30](/nl/topics/nip-30/) aangepaste-emojikinds 30030 en 10030 zodat een client een stickerpakket niet kan verwarren met een emojiset; de afbeeldingsbytes van stickers staan op HTTPS [Blossom](/nl/topics/blossom/)-compatibele servers, en verwijzingen naar verzonden stickers dragen een hash in platte tekst zodat een bewerkt adresseerbaar pakket het uiterlijk van al in oude berichten verzonden stickers niet stilzwijgend kan veranderen. Een bijbehorende PR registreert dezelfde kinds in het aparte `registry-of-kinds`-project.

### Open: NIP-29 berichten vastzetten met kind:9010 en kind:39005

[PR #2379](https://github.com/nostr-protocol/nips/pull/2379), van Anderson-Juhasc, voegt het vastzetten van berichten toe aan [NIP-29](/nl/topics/nip-29/) relay-gebaseerde groepen: kind:9010 `update-pin-list` is een moderatie-event dat de volledige lijst met vastgezette events als `e`-tags in weergavevolgorde draagt, zodat één event de vastgezette set kan vastzetten, losmaken, herordenen of leegmaken, en kind:39005 is een door de relay gegenereerde spiegel die de laatst geaccepteerde lijst blootgeeft. Het ontwerp vervangt een eerdere aanpak met toevoeg/verwijder-paren uit [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) na feedback uit review, en kiest de kindnummers 9010/39005 omdat 9009 en 39003 inmiddels zijn opgeëist door `create-invite` en grouprollen. Anderson-Juhasc onderhoudt ook [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages), waarvan [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) in dezelfde week verschijnt.

### Open: herstructurering van NIP-66 relaydetectie

[PR #2241](https://github.com/nostr-protocol/nips/pull/2241), van VincenzoImp, is een aanzienlijke herstructurering van [NIP-66](/nl/topics/nip-66/) relaydetectie. Het vervangt het losse proza "Other tags include" door een gestructureerde sectie Indexed Tags, voegt een `W`-tag toe die het `attributes`-veld van NIP-11 spiegelt voor het filteren bij relaydetectie, voegt een `l`-labeltag toe met gestandaardiseerde naamruimten (`ISO-639-1`, `ISO-3166-1`, `IANA-asn`, `IANA-tz`, `nip66.label.city`), en ordent RTT-, SSL/TLS-, netwerk-, geografische, DNS- en HTTP-tags in eigen secties naast een nieuwe Check Types-tabel. Het repareert ook kapotte voorbeeldevents met verkeerde veldnamen, een ontbrekende `kind` en ongeldige checktypenamen, en sluit [issue #2171](https://github.com/nostr-protocol/nips/issues/2171) af. Alle wijzigingen blijven achterwaarts compatibel omdat elke toegevoegde tag optioneel is.

---

## NIP Deep Dive: NIP-99 en de Gamma Markets-handelsuitbreiding

[NIP-15](/nl/topics/nip-15/), de oorspronkelijke Nostr Marketplace-specificatie, is inmiddels verouderd: het modelleerde een verkoperskraam (kind 30017) met producten (kind 30018) daaronder, en de clients die er ooit op draaiden, Shopstr daaronder, zijn sindsdien overgestapt op [NIP-99](/nl/topics/nip-99/)-advertenties als de actieve specificatie. NIP-99 zelf is één adresseerbaar event, kind 30402 voor een actieve advertentie of kind 30403 voor een concept, zonder eerst een kraam aan te maken. Het laat alles voorbij de advertentie ongedefinieerd: verzendkosten, bestelstatus, bonnen, recensies, en een manier om meerdere advertenties onder één winkel te groeperen, precies de delen van NIP-15 die nooit zijn meegegaan. [Gamma Markets](/nl/topics/gamma-markets/) vult dat gat, en is de moderne handelslaag die vandaag de moeite van het begrijpen waard is.

### Het gat dat NIP-99 openlaat

Het `content`-veld van een NIP-99-advertentie draagt een Markdown-beschrijving, `price` en `location` staan direct op het event, en `t`-tags maken het doorzoekbaar als gewone hashtag-inhoud. Omdat het adresseerbaar is op de tuple van pubkey, kind en `d`-tag, bewerkt een verkoper een advertentie ter plekke door een nieuwe versie met dezelfde `d`-tag te publiceren:

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

Dat is de hele specificatie: een ondertekende, bijwerkbare advertentie. Elke client die NIP-99 voor echte e-commerce implementeerde, verder dan een eenmalige advertentie, eindigde met het uitvinden van eigen privéconventies voor verzending, bestelberichten en recensies. Twee NIP-99-clients konden elk een advertentie correct weergeven en toch geen gedeelde manier hebben om samen een afrekening te voltooien.

### Gamma Markets: standaardiseren wat NIP-99 wegliet

Gamma Markets is de naam die een werkgroep van Nostr-marktplaatsontwikkelaars, de teams achter Shopstr, Cypher, Plebeian Market en Conduit Market, gaf aan een gedeelde set e-commerceconventies bovenop het bestaande kind 30402-event van NIP-99. De specificatie is vanuit het canonieke NIP-99-document gelinkt via [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) en wordt onderhouden in een eigen repository, [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec).

Gamma Markets voegt twee zelfstandige kinds toe die naast advertenties staan. Kind 30405 groepeert meerdere advertenties in een productcollectie en verwijst naar elk ervan met een expliciete `a`-tag:

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Kind 30406 definieert een verzendoptie met prijzen per land en optionele kostenregels op basis van gewicht of afstand:

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

Het aanmaken van bestellingen, betalingsverzoeken, status- en verzendupdates, en betalingsbonnen reizen allemaal als gewone [NIP-17](/nl/topics/nip-17/) gift-wrapped privéberichten, verdeeld over drie kinds naar rol en niet door het transport opnieuw in te pakken: kind 14 draagt vrije communicatie tussen koper en verkoper, kind 16 draagt elke overgang van bestelstatus (een `type`-tag van 1 tot en met 4 markeert het aanmaken van een bestelling, een betalingsverzoek, een statusupdate of een verzendupdate), en kind 17 draagt de betalingsbon van de koper. Een bericht voor het aanmaken van een bestelling ziet er zo uit voor het gift-wrappen:

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Een afgeronde aankoop beoordelen is een aparte adresseerbare kind, 31555, die terugwijst naar de advertentie die het recenseert:

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

Bestelberichten op NIP-17 laten meeliften betekent dat een Gamma Markets-afrekening hetzelfde transport voor privéberichten gebruikt dat clients al voor DMs leveren, in plaats van een eigen kind voor bestelberichten.

De centrale ontwerpkeuze van de specificatie is dat niets doorsijpelt. Een advertentie die bij een collectie hoort, verwijst er expliciet naar met een `a`-tag in plaats van automatisch de verzendopties of beschrijving van de collectie te erven, en een verzendoptie die een advertentie gebruikt, wordt op dezelfde expliciete manier aangehaald. Dat is een bewuste omkering van het kraammodel van NIP-15, waar een product stilzwijgend erfde welke valuta en verzendtabel de bovenliggende kraam definieerde. De afweging is meer expliciete tagging op elke advertentie, in ruil voor een advertentie waarvan de volledige configuratie altijd uit het event zelf leesbaar is, zonder eerst een bovenliggend object op te lossen.

### Waar dit in de praktijk opduikt

Het werk van [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) van deze week zit in hetzelfde bestelberichtenterrein dat Gamma Markets standaardiseert: het afrekenen als gast met efemere sleutel uit [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) en de herbouw van de bestellingeninbox voor verkopers uit [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) lossen allebei het bestelstatusprobleem tussen koper en verkoper op dat de kind 14-, 16- en 17-berichten van Gamma Markets formaliseren; Conduit Mono draait zijn eigen bestelstatusmodel naast die kinds, zonder ze direct over te nemen. Shopstr, een van de vier projecten die de specificatie schreven, hield de afgelopen week ook zijn eigen handelsleidingwerk in beweging: [PR #568](https://github.com/shopstr-eng/shopstr/pull/568) trekt gedupliceerde NIP-17 gift-wrap-logica uit naar een gedeelde module, en [PR #567](https://github.com/shopstr-eng/shopstr/pull/567) brengt zijn [NIP-98](/nl/topics/nip-98/) HTTP-authenticatieparser op volledige testdekking, onderhoud aan precies de berichten- en authenticatielagen waarvan een Gamma Markets-bestelstroom afhangt om koper en verkoper veilig te bereiken.

NIP-15 verloor de winkelrol door een kraam en een product te standaardiseren en vervolgens betalingen, verzending, recensies en bestelstatus als een probleem voor de applicatie te laten. Gamma Markets vult het meeste van dat ontbrekende oppervlak zonder de vorm van de enkele advertentie van NIP-99 aan te raken, en bouwt voort op Nostrs bestaande DM-stack, NIP-17, in plaats van een nieuwe berichtenlaag uit te vinden.

---

Dat was het voor deze week. Bouwt u iets of heeft u nieuws te delen? Neem contact op via een NIP-17-DM of vind ons op Nostr.
