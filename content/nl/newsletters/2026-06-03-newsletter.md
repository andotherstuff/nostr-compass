---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-01
---

Amber 6.2.0 levert NIP-44 v3 versleuteling vooruitlopend op de spec. Mostro legt de basis voor Cashu-afgewikkelde escrow over acht PRs, waarbij de bestaande Cashu Development Kit wordt gewrapt als een tweede afwikkelingsbackend naast Lightning. NIP-F4 podcasts wordt gemerged na 27 maanden debat. fiatjaf opent een controversieel NIP-17 key-ontkoppeling voorstel dat het bunker-versus-Marmot architecturale argument heropent. Amethyst levert NIP-32 hashtag-labeling, een dedicated podcastscherm en onchain zaps over 52 onuitgebrachte PRs.

## Belangrijkste verhalen

### Amber 6.2.0: NIP-44 v3 versleuteling geleverd

[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0), uitgebracht op 1 juni, voegt [NIP-44 v3 versleutelingsondersteuning](https://github.com/greenart7c3/Amber/pull/448) toe met een dedicated goedkeuringsscherm, intent preview, bunker preview, historieregistratie en auto-reject voor ongeldige verzoeken. De release registreert ook [NIP-44 v3 ContentProvider authorities](https://github.com/greenart7c3/Amber/commit/8b93340) zodat andere Android-apps v3-versleuteling kunnen aanvragen naast het bestaande v2-pad. NIP-44 zelf is de versioned versleutelde payload-spec gebruikt door [NIP-17](/nl/topics/nip-17/) private DMs, NIP-46 bunker-verkeer en andere Nostr-primitieven; v3 in Amber is een opt-in naast v2, gesignaleerd door een aparte signer-methode zodat receiver-side clients het algoritme expliciet kunnen negotiëren. De bijbehorende NIPs PR moet nog landen, dus Amber rolt v3 uit vooruitlopend op de protocolconsensus, met het wire format en ContentProvider-authority geregistreerd voor downstream client-integratie.

NIP-46 sessies accepteren nu automatisch ping-verzoeken bij connect, waardoor de prompt bij de eerste round trip na pairing wordt verwijderd. De `sign_message` signer-methode werd volledig verwijderd nadat deze werd gedeprecieerd en ongebruikt was.

Omdat Amber de dominante Android-signer is, moet elke downstream client die v3 wil richten op Amber's wire format totdat de NIPs PR landt. Dat geeft Amber impliciete zeggenschap over de uiteindelijke v3-spec totdat het protocol inhaalt. De ruil is reëel: v3 in productie laat Amber implementatiefeedback verzamelen voor de uiteindelijke NIP, ten koste van een tijdelijk single-implementation referentiepunt dat andere clients nu moeten matchen.

### Mostro: Cashu escrow-integratie via CDK

grunch landde deze week acht PRs door MostroP2P heen die Cashu's bestaande P2PK multisig-primitieven (NUT-10 en NUT-11) integreren als een tweede afwikkelingsbackend naast Lightning op de Nostr-gecoördineerde P2P Bitcoin-uitwisseling. De cryptografische primitieven zijn van Cashu; het werk is integratie-scaffolding en een nieuwe escrow-backend trait. [Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0), uitgebracht op 30 mei, voegt de [protocoltypes voor 2-of-3 multisig escrow](https://github.com/MostroP2P/mostro-core/pull/150) toe, per-proof P_M signatures en staat escrow events toe via responsvalidatie. De architectuur is gedocumenteerd in [PR #756](https://github.com/MostroP2P/mostro/pull/756) en gebruikt per-order trade keys verduidelijkt in [PR #757](https://github.com/MostroP2P/mostro/pull/757).

De implementatie werd uitgerold over zes follow-up PRs binnen één dag. [F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758) voegde de config, escrow-modus en conditional boot toe. Het volgende deel, [F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760), definieerde een `EscrowBackend` trait met een Lightning-implementatie en een Cashu-stub, waardoor Mostro afwikkelingsbackends kan wisselen zonder de order state machine te veranderen. [F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759) wrapte [CDK](https://github.com/cashubtc/cdk) (de Cashu Development Kit) voor mint- en wallet-operaties. Databasewerk in [F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761) voegde compare-and-swap escrow locks en active-locked queries toe. [F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762) bouwde een containerized mint in een dedicated CI-job voor end-to-end escrow-testen. De Mostro-flow gebruikt al NIP-59 gift-wrapped DMs voor ordercoördinatie via de relay, dus Cashu escrow past in als een tweede afwikkelingsoptie naast Lightning zonder het wire-protocol aan te raken.

## Releases

### ngit v2.5.0: GRASP fallback en lazy git-fetches

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0) verandert het standaardgedrag van `git push pr/<branch>` en `ngit send` om een PR-kind te produceren voor nieuwe voorstellen wanneer de repository ten minste één GRASP-server geregistreerd heeft. Voorheen werd dit alleen getriggerd voor oversized commits van meer dan 60 KB of commits die submodules bevatten. Wanneer een PR niet naar de GRASP-servers van de repository kan worden gepusht, valt ngit nu terug op GRASP-06 routing via de gedeclareerde servers. De `ngit send --git-server` flag of `git push -o git-server=<url>` laat contributors expliciet een aangepaste git-URL of GRASP-server richten.

`ngit init` republish behoudt nu onbekende tags van bestaande announcements, zodat tags toegevoegd door een toekomstige ngit-versie of derde-partij tool republish overleven. Een gele waarschuwing lijst de meegedragen tags en `--clean` verwijdert ze op verzoek. `ngit pr apply`, `ngit pr checkout` en `ngit pr list` raadplegen git-servers lazy en delen een enkele fetch-helper, zodat checkout niet langer onvoorwaardelijk fetch wanneer de commit al lokaal is. `ngit pr checkout` probeert ook door submitter aangeleverde clone-URLs uit het PR-event als fallback wanneer de gedeclareerde git-servers van de repo de PR-tip niet dragen, wat overeenkomt met het bestaande gedrag in `ngit pr apply`. ngit is de referentie [NIP-34](/nl/topics/nip-34/) implementatie voor git-collaboratie via Nostr, en v2.5.0 maakt GRASP het first-class pad voor nieuwe contributors.

### Jumble v26.5.7: EXIF-strippen en gevalideerde zap counts

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7) voegt twee wijzigingen toe die gebruikersprivacy en data-integriteit direct beïnvloeden. EXIF-locatie en camera-identifiers worden nu gestript uit image uploads voordat ze de client verlaten, waarmee een langstaand metadata-leak oppervlak wordt gesloten dat elk vanuit Jumble geplaatst beeld raakte. Zap counts worden nu alleen berekend uit cryptografisch gevalideerde receipts, waarmee opgeblazen counts van misvormde zap events worden verholpen die aanvallers hadden laten overdrijven op zap-totalen op notes. De release voegt ook zender-identiteitsverificatie toe voor [NIP-17](/nl/topics/nip-17/) DMs, waarmee een spoofing-oppervlak wordt gesloten waar een zender zijn `pubkey` in de seal kon vervalsen.

### nostr-calendar v1.6.0: RSVP en dubbele deelnemer-verwerking

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0) brengt Formstr's RSVP-flow ([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) en voorkomt dubbele deelnemers in event uitnodigingen ([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)). De `waitForAll` optie in de publish-functie defaults nu naar false zodat de UI niet blokkeert op langzame relays ([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)). [PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157) leverde Formstr's twee NIP-voorstel drafts voor appointment scheduling en reserveringen.

### Sprout 0.3.6: Sprout × mesh-llm en channel-secties

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6) is het hoofdverhaal van een zes-release reeks van v0.3.1 tot en met v0.3.6 deze week. In-process Sprout × mesh-llm integratie landt in [PR #798](https://github.com/block/sprout/pull/798), waardoor Sprout mesh-llm nodes kan serveren en consumeren via relay-admissie. Door de gebruiker gedefinieerde channel-secties synchroniseren over apparaten via Nostr in [PR #792](https://github.com/block/sprout/pull/792), en channel-secties komen naar mobile met relay sync in [PR #800](https://github.com/block/sprout/pull/800). Thread-bewuste notificaties met mutable follow- en mute-controle komen in [PR #761](https://github.com/block/sprout/pull/761).

Willekeurige file-type bijlagen met download cards kwamen in [PR #810](https://github.com/block/sprout/pull/810), waarmee Sprout wordt uitgebreid voorbij alleen-image bijlagen. Mobile kreeg een Pulse social feed-tab ([PR #772](https://github.com/block/sprout/pull/772)) en Pulse-polish over feed, compose en filter-oppervlakken ([PR #796](https://github.com/block/sprout/pull/796)).

### NostrBotKit v0.5.0: Marmot groepschat in een Rust bot-framework

[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md), uitgebracht op 24 mei op Codeberg, voegt [Marmot](/nl/topics/marmot/) (MLS-over-Nostr, [NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) ondersteuning toe aan het self-hosted Rust bot-framework. Wanneer `marmot: true` is ingesteld, publiceert de bot zijn MLS key packages (kind 443, 30443, 10051), accepteert groepsuitnodigingen automatisch en luistert naar berichten in gejoinede groepen. Twee nieuwe commandotypes, `dm_marmot` en `dm_marmot_npub`, laten bots berichten sturen naar benoemde Marmot-groepen of 1:1 Marmot-chats via cron jobs of webhooks. Om feedback-loops met andere bots te voorkomen, reageren NostrBotKit-bots alleen op berichten die expliciet aan hen zijn geadresseerd via `/command` of `@botname/command`. Versleutelde bijlagen met MIP-04 worden automatisch ontsleuteld en opnieuw geüpload via Blossom of NIP-96, en de MLS state-database wordt versleuteld met een sleutel afgeleid van de private key van de bot. NostrBotKit is het eerste Rust-framework dat NIP-104 bot-ondersteuning levert, waardoor Marmot-versleutelde bot-deployment beschikbaar komt voor een ander operator-profiel dan het bestaande TypeScript-pad.

### noscrypt v0.1.14: ondertekende cryptography library release

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14) is een security release van de C cryptography library gebruikt door verschillende Nostr clients voor secp256k1, NIP-04 en NIP-44 primitieven. De release wordt geleverd met [PGP-signed downloads](https://www.vaughnnugent.com/resources/software/modules/noscrypt) verifieerbaar tegen de public key van de maintainer. Downstream clients die noscrypt bundelen moeten de handtekening valideren voordat ze integreren.

### Chama v1.3.0: nieuwe Nostr-native P2P escrow met Fedimint

[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0), uitgebracht op 1 juni, is het hoofdverhaal van een vier-release reeks voor een nieuwe Nostr-native P2P escrow-client die Fedimint ecash en 2-of-3 Shamir secret sharing gebruikt voor afwikkeling. Het project draait op [getchama.app](https://getchama.app) en werkt zonder server. v1.3.0 introduceert "heal that sticks" (succesvolle re-broadcast en trade healing die sessieherstarts overleeft) en pay-rail matching, waarbij US-georiënteerde Chamas eerst US-betalingsrails tonen. Multi-unit storefront-basiswerk landde in [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11) (multi-unit schema) en [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12) (storefront stock accountant + native Fedimint bridge recovery hardening). Chama voegt zich bij Mostro en Shopstr in de Nostr-marktplaats categorie, onderscheiden door zijn serverloze architectuur en Fedimint-gebaseerde escrow-afwikkeling.

## Onuitgebrachte wijzigingen

### Amethyst: NIP-32 hashtag-labeling, podcastscherm, muziektracks

Amethyst mergde deze week 52 PRs en 411 commits zonder een release tag te knippen. De grootste functionele toevoeging is [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111), waarmee [NIP-32](/nl/topics/nip-32/) hashtag-labeling en een label-gebaseerde hashtag feed worden geïmplementeerd met kind 1985 events met `L` namespace en `l` label tags. Dit vervangt het brosse text-match `#tag` mechanisme door een labeler-gebaseerd discovery-model waarbij gebruikers specifieke labeler npubs kunnen volgen zoals ze contentmakers volgen. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) voegt een dedicated podcastscherm toe met episode-lijst en inline player, dat landt binnen dagen na de [NIP-F4](/nl/topics/nip-f4/) podcast-spec merge. [PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071) voegt een Software Apps feed toe met follow-list filtering, en [PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067) voegt music tracks en playlist-ondersteuning toe via [NIP-51](/nl/topics/nip-51/) sets.

Ephemeral signers voor anonieme post uploads landen in [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123), waardoor gebruikers anoniem kunnen posten zonder hun identity key bloot te stellen aan upload-services. Een Tor self-heal watchdog met integratietests tegen Arti v2.3.0 komt in [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053), wat Amethyst's Tor-routing versterkt tijdens transiënte netwerkuitval. Onchain zaps en een NIP-05 filter voor terugkerende gebruikers van Gemini landen in [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052), waarmee het zap-oppervlak wordt verbreed voorbij Lightning naar onchain Bitcoin-betalingen.

### Shopstr: OpenGraph preview URL-validatie

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504) valideert OpenGraph preview URLs voordat ze worden gerenderd in marktplaats-listings, waarmee een potentieel XSS-oppervlak wordt gesloten waar kwaadaardige verkopers scripted content konden embedden via vervaardigde OG-metadata. Door Shopstr gehoste shops tonen OG previews voor externe links, en ongevalideerde URLs laten een aanvaller willekeurige content injecteren in de shop-UI.

## NIP-updates en protocol-spec werk

### NIP-F4 (Podcasts) gemerged na twee jaar

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093) werd gemerged op 28 mei, twee jaar en drie maanden nadat fiatjaf de oorspronkelijke draft opende. NIP-F4 definieert podcast-afleveringen als kind 54 events met `imeta` tags voor audio-bestandsmetadata (URL, mime type, taal ISO code, fallback URLs, NIP-96 service flag, bitrate, duur), een `title` tag, optionele `image` en `description` tags, en `t` tags voor onderwerplabels. De spec houdt bewust RSS als de bron van waarheid: afleveringen kunnen een `i` tag dragen die verwijst naar de RSS podcast GUID, waardoor Nostr-clients kunnen linken naar bestaande podcastfeeds zonder audio-hosting te dupliceren. Het lange debat in de PR-thread (met podcast-namespace co-auteur Dave Jones, Alex Gleason en Mike Terenzio) kwam uit op een coëxistentiemodel waarbij Nostr de sociale laag biedt bovenop RSS terwijl RSS de distributielaag behoudt. Amethyst's [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) podcastscherm landt binnen dagen na de spec-merge, en Jumble's GIF picker-werk bevat ook vroege podcast-attachment scaffolding.

### NIP-17 key ontkoppeling (PR #2361)

fiatjaf opende [PR #2361](https://github.com/nostr-protocol/nips/pull/2361) op 1 juni, met het voorstel dat NIP-17 de identity key scheidt van de encryption key. Ontvangers adverteren hun encryption key in een nieuw kind 10044 event, en verzenders gebruiken die geadverteerde key (indien aanwezig) voor de gift-wrap inner seal, waarbij ze alleen terugvallen op de identity key van de ontvanger wanneer de advertentie afwezig is. De PR voegt ook een `n` tag toe aan de seal die de encryption pubkey van de zender draagt, zodat ontvangers de juiste conversation key kunnen afleiden zonder trial-decryption tegen elke retired key. De genoemde motivatie is bunker UX: onder het huidige ontwerp moet een bunker-gebruiker elke ontvangen DM door de signer round-trippen om te ontsleutelen, aangezien de encryption key de signer-gehouden identity key is. Ontkoppeling laat de client de encryption key lokaal houden terwijl de identity key in de bunker blijft voor signatures.

Het voorstel trok de meest controversiële review van de week. Cody Tseng (Jumble) steunt het als het gemakkelijkste pad naar cross-client DM interop. Vitor Pamplona (Amethyst) maakt bezwaar op twee gronden: het voegt een nieuw langlevend decryptie-geheim toe buiten de bunker, en clients die het niet leveren zullen stilletjes falen om berichten te ontsleutelen van clients die dat wel doen, zonder degradatiepad omdat de breuk op de seal-laag zit. Pamplona betoogt dat het probleem al correct is opgelost door [Marmot](/nl/topics/marmot/)'s key packages en epoch-rotatie, en dat het retrofitten van key-scheiding in de basis-NIP-17 spec het soort interop-falen creëert waar Marmot twee jaar over deed om er omheen te engineeren. fiatjaf's tegenwerping heeft drie delen: ontkoppeling is optioneel per ontvanger, de n-tag fix pakt de trial-decryption zorg aan, en het alternatief is de bunker-UX gebroken houden terwijl Telegram de messaging use case opeet. De thread blijft open zonder merge-beslissing en is de meest bekeken NIP-discussie van het kwartaal.

### NIP-Silent Payments payment flow (PR #2362)

[silentius-satoshi opende PR #2362](https://github.com/nostr-protocol/nips/pull/2362) op 1 juni als een companion aan de bredere [Nostr Silent Payments NIP draft (PR #2355)](https://github.com/nostr-protocol/nips/pull/2355). De payment-flow NIP definieert kind 8352 voor silent payment receipt notifications (geleverd via [NIP-59](/nl/topics/nip-59/) gift wrap zodat de receipt link niet publiekelijk waarneembaar is) en kind 10353 voor een versleutelde UTXO-cache die synchroniseert over apparaten voor dezelfde Silent Payments wallet. Het paar samen laat een betaler een betaling signaleren aan een Silent Payments adres met Nostr-native primitieven zonder de on-chain link bloot te leggen op de open relaylaag.

### NIP-PIP Perfect IP Packets (PR #2364)

[RandyMcMillan opende PR #2364](https://github.com/nostr-protocol/nips/pull/2364) op 1 juni als draft. Het introduceert een packet-tree transport met drie nieuwe addressable kinds: 39078 draagt het manifest, 39079 draagt individuele slices en 39080 draagt repair requests. De spec definieert een wire format waarbij grote bestanden worden opgesplitst in addressable slices, waarbij manifests de slice-tree beschrijven en repair requests ontvangers laten vragen om ontbrekende slices. Early-draft status is van toepassing en het voorstel heeft nog geen maintainer-review aangetrokken.

### NIP-29 audio/video live spaces (PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238) werd gemerged op 28 mei, waarbij [NIP-29](/nl/topics/nip-29/) relay-gebaseerde groepen worden uitgebreid met audio- en video-live-space ondersteuning. Groepen kunnen nu verwijzen naar een actieve live-space sessie, waardoor [NIP-53](/nl/topics/nip-53/)-stijl live activity events kunnen ankeren in een NIP-29 groepscontext.

### NIP-71 video multiple audio tracks (PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255) werd gemerged op 28 mei, met de toevoeging van audio-track `imeta` tags aan NIP-71 video events. Het nieuwe formaat draagt URL, hash, mime type, taal-tag (met ISO-639-1 plus original-version flag), fallback URLs, NIP-96 service signal, bitrate en duur. Dit maakt audio-only streaming (video podcasts), resolutie-switching met stabiele audio, meerdere taaltracks en verminderde opslag mogelijk wanneer servers geen audio direct in videobestanden inbedden. Clients moeten controleren op audio-track beschikbaarheid voordat single-track gedrag wordt aangenomen.

### NIP-59 ephemeral gift wrap (PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) werd gemerged op 28 mei, waarbij kind 21059 wordt toegevoegd als ephemeral tegenhanger van de bestaande kind 1059 gift wrap. De semantiek komt overeen met de standaard NIP-59 wrap maar volgt ephemeral event-regels per NIP-01 (relays laten ze vallen na broadcast en persisteren ze niet). Dit laat apps persistentie kiezen op basis van vereisten: typing-indicators en presence-pings profiteren van ephemeral, terwijl DM-geschiedenis persistentie nodig heeft.

### NIP-78 application-specific kind (PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292) werd gemerged op 28 mei, waarbij NIP-78 application-specific data wordt herclassificeerd als een normale addressable kind, waarbij het vorige aparte bereik wordt gedropt. Dit vereenvoudigt replaceability-semantiek en stemt NIP-78 af op het addressable event-model dat door andere application-state NIPs wordt gebruikt.

### NIP-85 verduidelijkingen (PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304) werd gemerged op 28 mei met kleine verbeteringen aan de taal rond meerdere keys en relays per service provider in [NIP-85](/nl/topics/nip-85/) Trusted Assertions, waarmee het operator-key-rotation pad voor relay assertion services wordt verduidelijkt.

### NIP-01 relay connection management one-liner (PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307) werd gemerged op 28 mei, met de toevoeging van één zin aan NIP-01 over hoe clients relay-connectielevens moeten verwerken. De fix pakt een langlopend gat aan waar clients van mening verschilden over of ze WebSocket-verbindingen open zouden houden na fetching, wat leidde tot silent message loss op relays die idle-verbindingen laten vallen.

### NIP-C7 kind 9 chat constraint (PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310) werd gemerged op 28 mei, waarbij NIP-C7 chat-weergaven worden beperkt tot alleen kind 9 berichten. Dit scheidt ephemeral chat van kind 1 timeline-posts in clients die NIP-C7-stijl chatoppervlakken implementeren.

### NIP-55 vereenvoudiging (PR #2363)

[PR #2363](https://github.com/nostr-protocol/nips/pull/2363) door greenart7c3, geopend op 1 juni, vereenvoudigt de Android signer applicatie-spec. Vitor Pamplona tekende af als "Looks good" en fiatjaf vroeg of het klaar was om te mergen. De wijziging maakt de weg vrij voor de NIP-44 v3 ContentProvider-authority registratie die Amber deze week leverde.

### NIP-44 v3 (Amber-implementatie vooruitlopend op spec)

Amber leverde NIP-44 v3 in v6.2.0 met acht commits die de versleuteling-upgrade en ContentProvider-authority registratie implementeren, maar de NIPs-repo spec PR moet nog landen. NIP-44 zelf definieert een versioned versleuteld payload-formaat gebruikt binnen ondertekende events; de bestaande v2 (in productie sinds 2024) gebruikt secp256k1 ECDH, HKDF, padding, ChaCha20, HMAC-SHA256 en base64. Het v3 wire format voegt een nieuwe versie-byte (0x03) toe voor de nonce, waardoor receiver clients het algoritme expliciet kunnen negotiëren. Amber's implementatie omvat auto-reject voor ongeldige v3-verzoeken, een dedicated goedkeuringsscherm onderscheiden van v2-goedkeuringen, en per-direction plaintext logging voor de historie. Totdat de NIPs PR merged, staat v3 als een Amber-specifieke uitbreiding. Behandel het als een toekomstgericht signaal, niet als een stabiele protocol-brede signalering.

## NIP deep dive: NIP-32 (Labeling)

[NIP-32](/nl/topics/nip-32/) definieert een gestructureerde manier voor elke Nostr-actor om events, pubkeys, relays, URLs of onderwerpen te labelen met addressable kind 1985 events met een namespaced label-vocabulaire. De spec introduceert twee nieuwe tags: `L` duidt een label-namespace aan en `l` duidt een label binnen die namespace aan. Label-target tags (`e`, `p`, `a`, `r` of `t`) specificeren wat wordt gelabeld. De namespace-vereiste voorkomt dat meerdere labelsystemen botsen: een `spam` label in `nip28.moderation` draagt andere semantiek dan een `spam` label in `relay-report`.

De ontwerpkeuze die NIP-32 nuttig maakt buiten moderatie is dat labels beweringen zijn, geen protocol-niveau waarheid. Een kind 1985 event zegt alleen dat een bepaalde pubkey een bepaald doel labelde in een bepaalde namespace. Het vertrouwensmodel wordt gedelegeerd aan de client: elke client kiest welke labelers te honoreren, welke namespaces te lezen en welke UI-affordance aan elk label te geven. Hetzelfde primitief draagt content warnings, licentietoewijzing, ISO-639-1 taal-tags op kind 1 notes, ISO-3166-2 geografische tags, contentclassificatie, gedistribueerde moderatie-suggesties en reputatiescores.

Amethyst's [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111) deze week is de grootste deployment tot nu toe. Het voegt hashtag labeling toe via NIP-32 en een label-gebaseerde hashtag feed, waardoor gebruikers kunnen browsen op labels toegewezen door vertrouwde labelers. Het eerdere `#tag` text-match mechanisme dat oorspronkelijk hashtag discovery op Nostr aandreef blijft als fallback voor niet-gelabelde notes. Het hashtag-as-label model betekent dat dezelfde note kan worden ontdekt onder meerdere labels toegewezen door verschillende labelers, en gebruikers kunnen specifieke labelers muten of boosten zonder de onderliggende notes te beïnvloeden.

Zelflabeling wordt ook ondersteund. Een auteur kan `L` en `l` tags direct aan zijn eigen kind 1 notes hangen om taal, locatie en onderwerp te verklaren. Een note getagd `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]` identificeert zichzelf als Engels en kan door taal-bewuste clients worden gefilterd zonder derde-partij labeling-infrastructuur.

Voorbeeld van een NIP-32 label event dat een kind 1 note als Engels tagt en een moderation-tag toewijst:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

De Amethyst-uitrol gecombineerd met het recente Trusted Relay Assertions-werk suggereert dat NIP-32 het standaardsubstraat wordt voor elk "gebruiker-gedreven bewering over een doelwit" patroon op Nostr. De volgende test is of labelers zelf vertrouwenshiërarchieën ontwikkelen: of gebruikers specifieke labeler npubs zullen volgen zoals ze contentmakers volgen.

## NIP deep dive: NIP-F4 (Podcasts)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md) werd deze week gemerged, twee jaar en drie maanden nadat fiatjaf de oorspronkelijke draft opende (PR #1093). Het F-prefix is gewoon hex-nummering: NIP-F0 tot en met NIP-FF gebruiken dezelfde 1-byte hex space als NIP-0A tot en met NIP-0D, waarbij het bovenste hex-bereik dient als overflow nu het 01-99 decimale bereik zich vult. NIP-F4 definieert hoe podcasts afleveringen en metadata publiceren als Nostr-events terwijl RSS wordt gehouden als een complementaire laag voor het audio-bestand zelf.

De centrale architecturale keuze is dat elke podcast zijn eigen Nostr keypair is. De spec opent direct hiermee: "each podcast is its own Nostr keypair". Dit laat podcasts hun podcasting-aanwezigheid combineren met een normale kind 0 / kind 1 microblogging-aanwezigheid, en laat een podcast eigendom veranderen in de tijd via key handover of MuSig2-stijl gedeelde signing. Vier event-kinds dragen de publicatielaag:

- **`kind:10154`**: replaceable podcast metadata. Draagt `title`, `image`, `description`, optionele `website` tags en optionele `p` tags die auteurs markeren met een `role` van `host`, `cohost` of `editor`.
- **`kind:10164`**: auteur counter-claim. Het voorbeeld in de spec gebruikt kind `10064` (een typo open voor correctie), maar de kop en omringende tekst identificeren het als `kind:10164`. Gebruikers noemen de podcast-pubkeys die ze schrijven, zodat clients de `p` tags in `kind:10154` kunnen verifiëren tegen een equivalente claim van de veronderstelde auteur. Zonder dit zou een podcast valselijk iedereen als host kunnen taggen.
- **`kind:54`**: episode-events geschreven door de podcast-pubkey direct. Tags omvatten `title`, optioneel `image`, `description` en één of meer `audio` tags. Elke `audio` tag is `["audio", "<audio-url>", "<optional_media_type>"]`. De spec merkt op "other important fields to be specified here later after further discovery", en de gemergde vorm is bewust minimaal.
- **`kind:10054`**: een [NIP-51](/nl/topics/nip-51/)-stijl favoriete-podcasts lijst, waardoor gebruikers kunnen markeren welke podcasts ze volgen.

Het thread-debat rond de merge betrof Podcasting 2.0 co-auteur [Dave Jones](https://github.com/daveajones), [Alex Gleason](https://github.com/alexgleason), [Mike Terenzio](https://github.com/mterenzio), [Pablo F7z](https://github.com/pablof7z) en [staab](https://github.com/staab). Jones argumenteerde sterk tegen elke poging om RSS te vervangen: "It's been tried many times and always fails", verwijzend naar JSONfeed, XMPP, AMP, Twitter's API en Spotify's mislukte migratie. Terenzio herformuleerde het voorstel als een sociale laag bovenop RSS, waarbij RSS zelf als de distributielaag wordt gehouden. fiatjaf stemde ermee in een stapje terug te doen en het voorstel te laten rijpen: "I agree with everything you said but I still think we can pull it off, let's stop here for a while". Twee jaar later landt de gemergde spec dichter bij coëxistentie dan vervanging.

Drie ontwerpvragen blijven expliciet in de gemergde spec:

- De `kind:10164` typo (voorbeeld toont `10064`) moet worden verzoend voordat clients veilig kunnen interopereren.
- Episode-niveau discovery zonder RSS GUID-linking wordt open gelaten. De gemergde spec heeft geen `i` tag, geen `podcast:item:guid` formaat en geen RSS-bridging mechanisme. Clients die een bestaande RSS-catalogus in kind 54 events willen overbruggen moeten de bridge-conventie zelf definiëren.
- De "other important fields" stub op de `kind:54` definitie laat bitrate, duur, taal, transcript pointers, chapters en per-segment metadata als open territorium voor follow-up voorstellen.

Amethyst's [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) brengt een dedicated podcastscherm met episode-lijst en inline player binnen dagen na de merge, de eerste grote client-implementatie. Jumble leverde vroege podcast-attachment scaffolding naast zijn GIF-picker. Wavlake blijft het grootste Nostr-native podcastplatform en zal moeten beslissen of het zijn bestaande kind 31337 music track events afstemt op NIP-F4's kind 54 episode-model.

Voorbeeld van een NIP-F4 kind 54 episode-event, overeenkomstig de minimale tag-set van de gemergde spec:

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093 was 27 maanden open, ruim boven de mediane open-duur voor gemergde NIPs PRs. De volgende test voor NIP-F4 is of de kind 10164 typo wordt verzoend, of episode-discovery en RSS-bridge conventies opkomen vanuit de implementers, en of de grote podcasthosts publiceren onder per-podcast keypairs zoals de spec aanbeveelt.
