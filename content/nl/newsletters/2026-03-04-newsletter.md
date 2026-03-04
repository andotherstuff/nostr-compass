---
title: 'Nostr Compass #12'
date: 2026-03-04
translationOf: /en/newsletters/2026-03-04-newsletter.md
translationDate: 2026-03-04
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** De [Marmot Development Kit](https://github.com/marmot-protocol/mdk) brengt zijn [eerste publieke release](#marmot-development-kit-brengt-eerste-publieke-release) uit met versleutelde media en meertalige bindings. [Nostrability](https://github.com/nostrability/outbox) publiceert [outbox-modelbenchmarks](#outbox-model-onder-de-loep) over 14 relay-selectie-algoritmen. [Wisp](https://github.com/barrydeen/wisp) gaat van [eerste alpha naar beta](#wisp-van-alpha-naar-beta) in acht dagen met Tor en [NIP-55](/nl/topics/nip-55/) (Android Signer Application) ondertekening. [NIP-91](#nip-updates) (AND-filters) wordt gemerged. [Vector v0.3.1](#vector-v031) levert negentropy-synchronisatie met 15x prestatieverbetering. Deze editie bevat ook het retrospectief Vijf Jaar Nostr-Februaries, dat het protocol volgt van een specificatieherschrijving met drie relays via de Damus App Store-explosie tot mesh-netwerken en AI-agentvoorstellen.

## Nieuws

### Outbox-Model Onder de Loep

[Nostrability](https://github.com/nostrability/outbox) publiceerde een reeks outbox-modelbenchmarks die testen hoe goed verschillende relay-selectie-algoritmen events ophalen uit het gedecentraliseerde relay-netwerk. Het project mergede 16 PR's en 76 commits in tien dagen, wat mogelijk de meest grondige empirische analyse van [NIP-65](/nl/topics/nip-65/) (Relay List Metadata) implementatiestrategieën tot nu toe oplevert.

De benchmarks testen 14 relay-selectie-algoritmen tegen real-world followlijsten over 15 clients en bibliotheken in vijf talen. Een basisaanpak van alleen populaire relays bevragen haalt ongeveer 26% van de events op. Greedy set-cover met Thompson Sampling bereikt 80-90% recall. Het toevoegen van een latentiebewuste variant met hyperbolische verdiscontering en EWMA relay-latentieregistratie verhoogde de volledigheid van 62-80% naar 72-96% bij het 2-secondenpunt over zes testprofielen.

[NIP-66](/nl/topics/nip-66/) (Relay Monitoring) dead-relayfiltering bleek consequent. Het voorfilteren van relaykandidaten tegen [nostr.watch](https://nostr.watch) liveness-data verwijderde 40-64% van de dode relays en verdubbelde het slagingspercentage van relays van 30% naar 75-85%. Feedlaadtijden daalden met 39% (van 40 seconden naar 24 seconden over 10 profielen). Een EOSE-racesimulatie toonde aan dat wachten op EOSE plus een graceperiode van 200ms de volledigheid verbeterde ten opzichte van stoppen bij de eerste relay die klaar is.

Voor clients die hun relay-routing niet volledig kunnen herschrijven, voegt een "hybride outbox-verrijking" per-auteur outbox-queries toe bovenop bestaande hardcoded app-relays. Deze hybride aanpak behaalde 80% eenjaars-eventrecall versus de 26% baseline, wat een migratiepad biedt voor clients met legacy relay-architecturen.

### ContextVM Opent MCP NIP en Brengt Efemere Gift Wraps Uit

[ContextVM](https://contextvm.org), het protocol dat Nostr verbindt met het [Model Context Protocol](https://modelcontextprotocol.io/), opende deze week twee voorstellen in het [NIPs-repository](https://github.com/nostr-protocol/nips). [PR #2246](https://github.com/nostr-protocol/nips/pull/2246) formaliseert CVM als een conventie voor het transporteren van MCP JSON-RPC-berichten over Nostr met behulp van efemere kind 25910 events. [PR #2245](https://github.com/nostr-protocol/nips/pull/2245) breidt [NIP-59](/nl/topics/nip-59/) (Gift Wrap) uit met een efemere kind (21059) die [NIP-01](/nl/topics/nip-01/) (Basic Protocol Flow) efemere semantiek volgt, zodat relays gewrapte berichten na aflevering kunnen verwijderen.

De efemere gift wrap-conventie werd uitgebracht als [CEP-19](https://docs.contextvm.org/spec/ceps/cep-19/) in de ContextVM SDK v0.6.x releasefamilie. De [SDK-implementatie](https://github.com/ContextVM/sdk) voegt een `GiftWrapMode` enum toe met drie instellingen: OPTIONAL (accepteer beide kinds en detecteer automatisch peer-capability), EPHEMERAL (alleen kind 21059) en PERSISTENT (alleen kind 1059). Voor AI-toolaanroepen voorkomt de efemere modus het opslaan van tussenliggend verzoek-responsverkeer op relays, waardoor zowel opslagkosten als privacyblootstelling afnemen.

Nieuwe publieke MCP-servers verschenen op het netwerk van onafhankelijke operators, waaronder een Wolfram Alpha queryserver. Het ContextVM-team publiceerde CEP-15 (gemeenschappelijk toolsschema) en CEP-17 (publicatie van serverrelaylijsten) naast de v0.6.x releasecyclus.

### Marmot Development Kit Brengt Eerste Publieke Release

[MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit), de Rust-bibliotheek die [Marmot](/nl/topics/mls/)-versleuteld berichtenverkeer aandrijft voor [Pika](https://github.com/sledtools/pika) en [White Noise](https://github.com/marmot-protocol/whitenoise), bracht [v0.6.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.6.0) uit als eerste publieke release. Meer dan 200 PR's werden gemerged in deze versie, met zes nieuwe bijdragers.

De release omvat versleutelde mediaondersteuning (MIP-04) met HKDF seed-derivatie (MIP-01 v2), deterministische commit-raceresolutie (MIP-03), versleutelde lokale opslag, adminautorisatievalidatie voor Marmot-commits en -proposals, en GREASE-ondersteuning voor protocoluitbreidbaarheid. Bindings worden geleverd voor Kotlin, Python, Ruby en Windows naast Android cross-compilatie. De bibliotheek upgradet naar OpenMLS 0.8.0 met beveiligingsadviesfixes en een `Secret<T>`-type dat gevoelige waarden in het geheugen nulstelt.

Een begeleidende protocolwijziging ([MIP-03](https://github.com/marmot-protocol/marmot/pull/48)) verving [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads) versleuteling door ChaCha20-Poly1305 voor kind 445-berichten. NIP-44 vereiste UTF-8 stringinvoer volgens de specificatie, waardoor het onmogelijk was om ruwe Marmot-berichtbytes door standaard TypeScript Nostr-bibliotheken te sturen. De vervanging leidt sleutels direct af van het Marmot-exportergeheim. Deze brekende wijziging vereiste gecoördineerde updates over de [kernspecificatie](https://github.com/marmot-protocol/marmot/pull/48), [MDK](https://github.com/marmot-protocol/mdk/pull/208) en [TypeScript SDK](https://github.com/marmot-protocol/marmot-ts/pull/54).

[marmot-ts](https://github.com/marmot-protocol/marmot-ts), de TypeScript-implementatie onderhouden door hzrd149, mergede vier PR's met brekende API-wijzigingen. Een [omnibusupdate](https://github.com/marmot-protocol/marmot-ts/pull/52) voegde een key package manager toe voor de create/publish/rotate-levenscyclus, een `sendChatMessage`-gemaksmethode, uitnodigingsvoorbeeld zonder deelname (`readInviteGroupInfo`), zelfupdate voor forward-secrecyrotaties en gestructureerde debuglogging. Groepsontsleutelings-API's werden hernoemd van `readGroupMessage` naar `decryptGroupMessage` met rijkere resultaatvarianten (processed/skipped/rejected/unreadable). gzuuus droeg bij aan voorbeeldopschoning met NIP-65 relay-ondersteuning en last-resort key package-afhandeling per MIP-00.

De [White Noise CLI](https://github.com/marmot-protocol/whitenoise-rs) (`wn`), de Rust-backend die zowel de mobiele app als de nieuwe TUI aandrijft, mergede 16 PR's in tien dagen. Signer-levenscyclusafhandeling kreeg annuleringsveiligheid door een RAII scope guard ([PR #538](https://github.com/marmot-protocol/whitenoise-rs/pull/538)), waarmee een klasse bugs werd opgelost waarbij afgebroken operaties signerstatus konden lekken. Login blokkeert nu wanneer vereiste relaylijsten (kind 10002/10050/10051) ontbreken ([PR #515](https://github.com/marmot-protocol/whitenoise-rs/pull/515)), en giftwrap-abonnementen vallen terug op [NIP-65](/nl/topics/nip-65/) relays wanneer inboxlijsten afwezig zijn ([PR #518](https://github.com/marmot-protocol/whitenoise-rs/pull/518)). Een debugmodus ([PR #528](https://github.com/marmot-protocol/whitenoise-rs/pull/528)) geeft databasequeries en MLS ratchet-tree-inspectie weer als JSON-uitvoer. Andere fixes betroffen abonnementsherstel na herregistratie van de signer, catch-uptiming van welkomstberichten, relayfiltervalidatie en limieten voor de zoekradius van gebruikers.

Marmot kende deze week een significante uitbreiding buiten de kern-Ruststack. [White Noise TUI](https://github.com/marmot-protocol/wn-tui), een terminalinterface voor de White Noise-berichtenstack, werd gelanceerd op 3 maart. Het wrapt de `wn` CLI als een subproces en rendert de JSON-uitvoer via een Elm-geïnspireerde unidirectionele architectuur, met multi-conversatienavigatie met ongelezen-indicatoren, groepscreatie en ledenzoek, realtime berichtstreaming en emojireacties vanuit de terminal.

[DavidGershony](https://github.com/DavidGershony) publiceerde een complete C# Marmot-stack die de gelaagde architectuur van de Rust-toolchain spiegelt. [dotnet-mls](https://github.com/DavidGershony/dotnet-mls) implementeert MLS RFC 9420 cryptografische primitieven in C#. [marmot-cs](https://github.com/DavidGershony/marmot-cs) bouwt hierop voort met Nostr relay-transport, als C#-equivalent van MDK. [OpenChat](https://github.com/DavidGershony/openChat), een cross-platform desktopapp gebouwd met .NET 9 en Avalonia UI, combineert beide tot een werkende chatclient met NIP-44 DM's, Marmot-groepsversleuteling, [NIP-46](/nl/topics/nip-46/) (Nostr Connect) remote ondertekening en multi-relaystatusindicatoren.

[MDK PWA Reference](https://github.com/zerosats/mdk-pwa-reference) biedt een Progressive Web App-sjabloon voor het bouwen van Marmot-versleutelde applicaties, met experimentele ondersteuning voor AI-agentdeelname in groepschats en Bitcoin-betalingen via Arkade wallet-infrastructuur.

### Wisp Van Alpha Naar Beta

[Wisp](https://github.com/barrydeen/wisp) is een nieuwe Android Nostr-client die ging van [eerste alpha](https://github.com/barrydeen/wisp/releases/tag/v0.1.0-alpha) op 24 februari naar [v0.3.4-beta](https://github.com/barrydeen/wisp/releases/tag/v0.3.4-beta) op 3 maart, met 19 releases, 115 gemerge PR's en 276 commits in acht dagen.

Het featuretraject bestrijkt terrein waar de meeste clients maanden over doen. v0.1.0 verscheen met outbox/inbox relay-modelondersteuning en onboardingflows. Tegen v0.1.3 had de client [NIP-55](/nl/topics/nip-55/) intent-gebaseerde ondertekening voor Amber, een ingebouwde Tor SOCKS5-proxy voor `.onion` relay-connectiviteit en [NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect). v0.2.0 promoveerde naar beta met mutelistfiltering en aangepaste emoji-ondersteuning, terwijl v0.2.4 content warning-overlays toevoegde. De v0.3.x-serie introduceerde [NIP-13](/nl/topics/nip-13/) proof-of-work voor notes, achtergrond-PoW-mining met persistente instellingen, `.onion` relay-opslag en mute-threadnotificaties.

On-device vertaling via Google ML Kit draait lokaal zonder netwerktoegang na de initiële modeldownload. Een interactieve sociale-graafvisualisatie gebruikt een velocity Verlet-fysicasimulatie op ongeveer 30fps met pinch-to-zoom-navigatie en profielinspectie.

## Releases

### Vector v0.3.1

[Vector](https://github.com/VectorPrivacy/Vector), de Marmot-versleutelde berichtenapp, bracht [v0.3.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.1) uit met verbeteringen in groepsbeheer en prestaties. Multi-admingroepen, bulkuitnodigingen, uitnodiging-per-npub en groepsavatars breiden de samenwerkingsfuncties uit. Android-achtergrondnotificaties ondersteunen nu inline Reply- en Mark Read-acties.

Op [Negentropy](/nl/topics/negentropy/) gebaseerde deterministische synchronisatie haalt de volledige gespreksgeschiedenis op, inclusief berichten die tijdens offlineperiodes zijn gemist. Voice-to-text is herbouwd met GPU-versnelling op Android. Bestandsbijlageafhandeling is herzien met downloadvoortgang, herhaalpogingen, directory zip-and-send en live voortgangsindicatoren. De prestaties verbeterden meer dan 15x over opstarttijd, beeldverwerking, audioweergave en algemene UI-responsiviteit. De installatiegrootte van de app daalde met meer dan een derde, en de frontend werd ruwweg gehalveerd. 32-bit ARM Android-ondersteuning werd toegevoegd.

### Alby Hub v1.21.5

[Alby Hub](https://github.com/getAlby/hub), de self-custodial Lightning-node met Nostr Wallet Connect ([NIP-47](/nl/topics/nip-47/)) ondersteuning, bracht [v1.21.5](https://github.com/getAlby/hub/releases/tag/v1.21.5) uit. Een tweede relay werd toegevoegd aan de standaard NWC-configuratie, wat de betrouwbaarheid tijdens relay-herstarts verbetert. Een fix voor ongeldige zapdata in de transactielijst lost een weergaveprobleem op met misvormde [NIP-57](/nl/topics/nip-57/) (Lightning Zaps) events. Nieuwe app store-vermeldingen omvatten Alby CLI en LNVPS.

### nospeak v0.12.x

[nospeak](https://github.com/psic4t/nospeak), de tekstgebaseerde Nostr-berichtenclient, bracht drie releases uit in deze periode. [v0.12.0](https://github.com/psic4t/nospeak/releases/tag/v0.12.0) voegde een PIN app-vergrendeling toe met 4-cijferig toetsenbord en meer dan 15 nieuwe taalvertalingen waaronder Bengaals, Thais, Vietnamees, Hindi, Arabisch, Hebreeuws, Urdu, Turks, Japans, Chinees, Koreaans, Nederlands, Pools, Russisch en Perzisch met RTL-ondersteuning. [v0.12.1](https://github.com/psic4t/nospeak/releases/tag/v0.12.1) introduceerde een Cypher-thema met pure zwarte achtergronden en cyaan-accenten, plus Android-videopostergeneration. [v0.12.2](https://github.com/psic4t/nospeak/releases/tag/v0.12.2) voegde chatexport en View Profile toe in contactmenu's.

### Citrine v2.0.0-pre2

[Citrine](https://github.com/greenart7c3/Citrine), de Android persoonlijke relay van greenart7c3, bracht [v2.0.0-pre2](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre2) uit met relay-prestatieverbeteringen door nieuwe database-indexen en geherstructureerde Kotlin-coroutines. Elke gehoste webapp start nu op een eigen poort. Full-text search en een herontworpen events-scherm met eventuitklapping completeren de wijzigingen.

### NoorNote v0.5.x

[NoorNote](https://github.com/77elements/noornote), een Nostr-gebaseerde notitieapplicatie, bracht 8 releases uit van [v0.5.0](https://github.com/77elements/noornote/releases/tag/v0.5.0) tot [v0.5.7](https://github.com/77elements/noornote/releases/tag/v0.5.7). De v0.5.0-lancering op Android voegde [NIP-55](/nl/topics/nip-55/) Amber signer-ondersteuning en [NIP-71](/nl/topics/nip-71/) (Video Events) notepublicatie toe. Een herontworpen welkomstpagina in v0.5.1 bevatte publieke tijdlijnvoorbeelden en verkleinde de APK tot 15 MB. De Relay Browser in v0.5.2 laat gebruikers publieke relay-tijdlijnen bladeren via deelbare URL's, naast mediadownload en [NIP-30](/nl/topics/nip-30/) aangepaste emojireacties. Opvolgende releases tot v0.5.7 losten synchronisatie-racecondities op in het collaboratieve "tribes"-notitiedeelsysteem.

### NosCall v0.5.1

[NosCall](https://github.com/sanah9/noscall), de Nostr spraak- en videobel-app, bracht [v0.5.1](https://github.com/sanah9/noscall/releases/tag/v0.5.1-release) uit met spraakberichtondersteuning, een geoptimaliseerde desktopervaring met groepstoegang, contactfavorieten op desktop, contactnotities en filtering, data-export en opschoningsmogelijkheden, en ondersteuning voor systeemlettergrootte-toegankelijkheid.

### Shosho v0.13.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), de Nostr livestreaming-app, bracht [v0.13.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.13.0) uit met MP4 replay-downloads vanuit streamkaartmenu's en [NIP-05](/nl/topics/nip-05/) (DNS-Based Verification) voor profielen. De RTMP-publisher migreerde naar Expo Modules API. Streamingprestaties op verbindingen met lagere bandbreedte verbeterden, en crashes op oudere apparaten en iOS-streaming naar [Zap.Stream](https://zap.stream) zijn opgelost.

### nostr-java v2.0.0

[nostr-java](https://github.com/tcheeric/nostr-java) bracht [v2.0.0](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.0) uit met configureerbare WebSocket-buffergroottes, waardoor applicaties grotere Nostr-events kunnen verwerken zonder afkapping. De major version bump weerspiegelt brekende wijzigingen in de verbindings-API.

### Prism 1.1.0

[Prism](https://github.com/hardran3/Prism) bracht [1.1.0](https://github.com/hardran3/Prism/releases/tag/1.1.0) uit met ondersteuning voor long-form content (kind 30023 artikelen) en een Markdown-editor voor het direct schrijven in de app, gevolgd door een [1.1.1](https://github.com/hardran3/Prism/releases/tag/1.1.1) bugfix-release.

### Angor v0.2.6

[Angor](https://github.com/block-core/angor), het Bitcoin-crowdfundingplatform, bracht [v0.2.6](https://github.com/block-core/angor/releases/tag/v0.2.6) uit met Boltz-integratie en een 1-klik investeerflow. Zowel invest als fund projecttypes werken end-to-end op testnet. Het team merkt op dat de UI ongeveer 70% compleet is.

## NIP-Updates

Recente wijzigingen in het [NIPs-repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-91: AND Operator voor Filters](https://github.com/nostr-protocol/nips/pull/1365)**: Voegt AND-filtersemantiek toe voor tag-arrays in relay-abonnementen. Momenteel matcht het opgeven van meerdere waarden in een tagfilter (bijv. meerdere `p`-tags) events die een ervan bevatten. NIP-91 laat clients vereisen dat events alle opgegeven tagwaarden tegelijkertijd matchen, waardoor bandbreedte wordt verminderd en snellere indexoperaties mogelijk worden. Meerdere relay-implementaties bestaan al, waaronder nostr-rs-relay, satellite-node, worker-relay en applesauce. Voorheen genummerd als NIP-119.

- **[NIP-30: Emoji-Setadres in Tags](https://github.com/nostr-protocol/nips/pull/2247)**: Aangepaste emoji-tags in [NIP-30](/nl/topics/nip-30/) kunnen nu een optioneel emoji-setadres bevatten. Het klikken op een emoji in een client kan de set openen waartoe deze behoort om als bladwijzer op te slaan of te bladeren. Afkomstig van de [Chachi](https://github.com/purrgrammer/chachi)-client.

- **[NIP-29: Toevoeging van unallowpubkey en unbanpubkey](https://github.com/nostr-protocol/nips/pull/2111)**: Twee nieuwe admincommando's voor [NIP-29](/nl/topics/nip-29/) groepschat. `unallowpubkey` verwijdert een pubkey van de toegestane lijst zonder deze te bannen. `unbanpubkey` heft een ban op zonder de pubkey opnieuw als lid toe te voegen. Voorheen was de enige manier om iemand van de toegestane lijst te verwijderen ook een ban, en het opheffen van een ban vereiste het opnieuw toevoegen van de gebruiker als lid.

**Open PR's en Discussies:**

- **[NIP-A7: Spells](https://github.com/nostr-protocol/nips/pull/2244)** (geopend 27 feb): Voorgesteld door purrgrammer, spells zijn draagbare opgeslagen Nostr-queries gepubliceerd als kind 777-events. Een spell codeert een REQ- of COUNT-filter in gestructureerde tags (`k` voor kinds, `authors` voor pubkeys, `tag` voor willekeurige tagfilters) met runtimevariabelen: `$me` wordt omgezet naar de pubkey van de ingelogde gebruiker, `$contacts` breidt uit naar de kind 3 followlijst van de gebruiker. Relatieve tijdstempels (`7d`, `2w`, `1mo`) laten spells rollende tijdvensters definiëren zonder hardcoded datums. Al geïmplementeerd in [nak](https://github.com/fiatjaf/nak) en [Grimoire](https://github.com/purrgrammer/grimoire), stellen spells gebruikers in staat om gecureerde feeds te creëren, delen en abonneren die meereizen over clients.

- **[NIP-59: Efemere Gift Wrap (kind 21059)](https://github.com/nostr-protocol/nips/pull/2245)** (geopend 27 feb): Voegt een efemere variant toe van [NIP-59](/nl/topics/nip-59/) gift wraps. Kind 21059 volgt NIP-01 efemere semantiek, zodat relays events na aflevering verwijderen. Voorgesteld door ContextVM voor MCP-transport waar berichtpersistentie niet nodig is.

- **[ContextVM: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)** (geopend 27 feb): Specificeert hoe Model Context Protocol-berichten over Nostr worden getransporteerd met behulp van efemere kind 25910 events met `p`- en `e`-tags voor adressering en correlatie. Bewust minimaal, de protocoldetails worden doorverwezen naar de [ContextVM-spec](https://docs.contextvm.org).

- **[NIP-29: Audio/Video Live Spaces](https://github.com/nostr-protocol/nips/pull/2238)** (geopend 25 feb, draft): Een draft van fiatjaf dat [NIP-29](/nl/topics/nip-29/) groepen uitbreidt met live audio en video. Het voorstel voegt optionele `livekit`- en `no-text`-tags toe aan groepsmetadata-events. Wanneer een gebruiker wil deelnemen aan een spraakruimte, vraagt de client een JWT aan bij de relay op `/.well-known/nip29/livekit/{groupId}`. De relay controleert groepslidmaatschap en geeft een token uit met de hex pubkey van de gebruiker als `sub`-claim, die wordt doorgegeven aan [LiveKit](https://livekit.io/) voor mediatransport. Spraakruimtetoegang erft het bestaande machtigingsmodel van de groep, zodat relay-side lidmaatschapsregels bepalen wie kan spreken. Wordt getest in Pyramid en Chachi.

- **[Collaboratief Eventeigenaarschap](https://github.com/nostr-protocol/nips/pull/2235)** (geopend 24 feb): pablof7z stelt een pointer event (kind 39382) voor dat een collaboratieve ruimte declareert door co-eigenaar pubkeys in `p`-tags en een doeleventkind in een `k`-tag te vermelden. Elke vermelde eigenaar kan events van dat kind met dezelfde `d`-tag publiceren, en clients bepalen de huidige status door alle eigenaren te bevragen en het meest recente event te nemen. Co-auteurschapattributie wordt alleen weergegeven wanneer een verifieerbare `a`-tag terugverwijst naar de pointer en de auteur in de `p`-tags voorkomt, wat gespoofte claims voorkomt. Dit maakt gedeelde wikipagina's en co-auteur-bronnen mogelijk zonder controle aan een enkel sleutelpaar toe te wijzen.

- **[NIP-09: Cascadeverwijdering van Reposts](https://github.com/nostr-protocol/nips/pull/2234)** (geopend 24 feb): Wanneer een oorspronkelijke auteur een note verwijdert, moeten relays ook eventuele kind 6 of kind 16 reposts die ernaar verwijzen verwijderen. Gemotiveerd door privacyzorgen: reposts kunnen per ongeluk gelekte informatie bewaren nadat de auteur de bron heeft verwijderd. De wijziging is alleen relay-side en vereist geen clientaanpassingen.

- **[NIP-07: peekPublicKey](https://github.com/nostr-protocol/nips/pull/2233)** (geopend 23 feb): Voegt een `peekPublicKey()`-methode toe aan [NIP-07](/nl/topics/nip-07/) browserextensies. Anders dan `getPublicKey()` retourneert deze de huidige pubkey zonder om gebruikersbevestiging te vragen, waardoor stille auto-login mogelijk wordt wanneer de gebruiker auto-login heeft ingeschakeld.

- **[NIP-BB: Book](https://github.com/nostr-protocol/nips/pull/2248)** (geopend 28 feb, draft): Definieert vier adresseerbare event kinds (30300-30303) voor gestructureerde boekpublicatie op Nostr. Een Cover-event bevat rootmetadata inclusief titel, omslagafbeelding, licentie via [NIP-32](/nl/topics/nip-32/) (Labeling) labels en taalcode. Een Index-event koppelt elk hoofdstuk aan zijn positie met base62 fractionele indexering, waardoor auteurs nieuwe hoofdstukken tussen bestaande kunnen invoegen zonder hernummering. Chapter-events fungeren als structurele headers met optionele afbeeldingen, terwijl Episode-events de daadwerkelijke tekst bevatten, begrensd op 30.000 tekens, met gepositioneerde afbeeldingstags. Recensies gebruiken Zaps op Cover-events met de Zapbeschrijving als recensietekst.

- **[NIP-54: Overstap van Asciidoc naar Djot](https://github.com/nostr-protocol/nips/pull/2242)** (geopend 26 feb): Na de [d-tag internationalisatiefix](/nl/newsletters/2025-12-31-newsletter/) in december, stelt deze PR voor om het [NIP-54](/nl/topics/nip-54/) wiki Asciidoc-opmaakformaat te vervangen door [Djot](https://djot.net/), met toevoeging van een motivatiesectie en wikilink-voorbeelden voor niet-Latijnse schriften.

- **[NIP-66: Defensieve Maatregelen](https://github.com/nostr-protocol/nips/pull/2240)** (geopend 26 feb): Gebaseerd op lessen uit de [nostrability/outbox](#outbox-model-onder-de-loep)-benchmarks, voegt expliciete aanwijzingen toe voor [NIP-66](/nl/topics/nip-66/) randgevallen. Een begeleidende [PR #2241](https://github.com/nostr-protocol/nips/pull/2241) definieert outputtags voor SSL, geolocatie, netwerk en connectiviteitscontroles.

- **NIP-C1: Cryptografische Identiteitsbewijzen** (wiki-vermelding, kind 30817): Stelt kind 30509-events voor die APK-ondertekeningscertificaten cryptografisch koppelen aan Nostr-profielen. Het bewijs werkt door een canoniek bericht met de Nostr pubkey te ondertekenen met de privésleutel van het certificaat (met ondersteuning voor ECDSA, RSA PKCS1v15, Ed25519 en andere standaardalgoritmen), en vervolgens de handtekening te publiceren in een kind 30509-event dat is ondertekend met de Nostr-sleutel. Verifieerders kunnen bevestigen dat de persoon die het Android-ondertekeningscertificaat van een app beheert ook de Nostr pubkey beheert die beweert deze te publiceren. Bewijzen verlopen standaard na een jaar en kunnen expliciet worden ingetrokken. Geïmplementeerd in de [Zapstore](https://github.com/zapstore/zapstore)-toolchain.

- **NIP-31402: SARA Revenue Share Offering Registry** (wiki-vermelding, kind 30817): Definieert kind 31402 adresseerbare events voor het publiceren van Simple Autonomous Revenue Agreement (SARA)-aanbiedingen op Nostr-relays. Uitgevers adverteren Lightning-afgehandelde revenue share-voorwaarden inclusief poolaandeelpercentage, uitbetalingstrigger, drempelwaarde in sats, looptijd en gelaagde prijsstelling. Agents en mensen kunnen aanbiedingen over relays ontdekken en autonoom abonneren zonder centraal platform. Het kind-nummer spiegelt kind 30402 (L402 Service Registry, gepubliceerd door dezelfde auteur als begeleidende wiki-vermelding) omdat SARA het retourtraject van de L402-betalingsrelatie vertegenwoordigt.

## Open PR's en Projectupdates

### Damus: [NIP-89](/nl/topics/nip-89/) (Recommended Application Handlers)

[PR #3337](https://github.com/damus-io/damus/pull/3337) implementeert NIP-89 clienttag-ondersteuning voor [Damus](https://github.com/damus-io/damus). De app zendt nu een clienttag uit op alle publicatiepaden (hoofdapp, share-extensie, highlighter, drafts) en toont "via ClientName" naast tijdstempels wanneer andere apps hun tags bevatten. Een Privacy-toggle in Weergave-instellingen laat gebruikers tagemissie uitschakelen. [PR #3652](https://github.com/damus-io/damus/pull/3652) voegt een Opslag-sectie toe in Instellingen met een interactief cirkeldiagram dat NostrDB- en Kingfisher-cache schijfgebruik uitsplitst met exportondersteuning.

Open: [PR #3657](https://github.com/damus-io/damus/pull/3657) voegt [NIP-65](/nl/topics/nip-65/) relay-terugval toe voor geciteerde notes. Wanneer een inline `nevent` een auteur-pubkey bevat maar geen relayhints en de note ontbreekt in de pool van de gebruiker, haalt Damus de kind 10002 relaylijst van de auteur op en probeert opnieuw vanaf hun schrijfrelays.

### Amethyst: [NIP-39](/nl/topics/nip-39/) (External Identities), NIP-C0, [NIP-66](/nl/topics/nip-66/)

[Amethyst](https://github.com/vitorpamplona/amethyst) mergede een golf van NIP-implementaties over 28 PR's. Externe identiteitsclaims publiceren nu als speciale kind 10011-events onder [NIP-39](/nl/topics/nip-39/) ([PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747)), waardoor sociale identiteit wordt gescheiden van kind 0-metadata met achterwaarts-compatibele terugval. Code snippet-ondersteuning via NIP-C0 ([PR #1744](https://github.com/vitorpamplona/amethyst/pull/1744)) voegt kind 1337-events toe met accessors voor taal, extensie, runtime, licentie en afhankelijkheden. De [NIP-66](/nl/topics/nip-66/) relay-monitoringimplementatie ([PR #1742](https://github.com/vitorpamplona/amethyst/pull/1742)) bestrijkt beide event kinds met volledige tagparsing voor RTT-metrics, netwerktype, ondersteunde NIPs en geohash.

Versleutelde DM's arriveerden op Amethyst Desktop ([PR #1710](https://github.com/vitorpamplona/amethyst/pull/1710)) met een gesplitst-paneelchatlayout die zowel [NIP-04](/nl/topics/nip-04/) (Encrypted Direct Messages) als [NIP-17](/nl/topics/nip-17/) (Private Direct Messages) ondersteunt. Een nieuw relayfeeds-scherm ([PR #1733](https://github.com/vitorpamplona/amethyst/pull/1733)) laat gebruikers berichten van een specifieke relay bladeren met follow/unfollow-functionaliteit. Open: censuurbestendige NIP-05-verificatie ([PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)) voegt een parallel verificatiepad toe voor `.bit`-identifiers die oplost tegen de Namecoin-blockchain in plaats van HTTP DNS. Wanneer Amethyst een `.bit`-achtervoegsel detecteert in een NIP-05-veld, bevraagt het een ElectrumX-NMC server voor de naamtransactiegeschiedenis, parst het `NAME_UPDATE`-script van de laatste uitvoer om de Nostr pubkey te extraheren, en weigert namen ouder dan 36.000 blokken (Namecoins vervalvenster). ElectrumX-verbindingen routeren via SOCKS5 wanneer Tor is ingeschakeld, met dynamische serverselectie tussen clearnet en `.onion`-eindpunten. Een LRU-cache met een TTL van een uur voorkomt herhaalde blockchainqueries.

### Notedeck: Outbox-Architectuur

[PR #1303](https://github.com/damus-io/notedeck/pull/1303) migreert [Notedeck](https://github.com/damus-io/notedeck) van ad-hoc relay-poolbeheer naar een gecentraliseerd outbox-model met accountgerichte abonnementen. De Messages-module publiceert nu een standaard DM-relaylijst als er geen bestaat en routeert DM's naar ontvangers' voorkeursrelays per kind 10050.

### Pika: Per-Groepprofielen en Tutorial-Feed

[Pika](https://github.com/sledtools/pika), de Marmot-versleutelde berichtenapp beschikbaar op iOS en Android met een desktopbuild, kreeg per-groepprofielen ([PR #368](https://github.com/sledtools/pika/pull/368)). Gebruikers kunnen nu een apart weergavenaam en -foto instellen voor elke groepschat, samen met een aangepaste bio. Deze profielen worden gepubliceerd als versleutelde kind 0-events binnen de Marmot-groep, onzichtbaar voor iedereen daarbuiten, met een terugval naar het globale Nostr-profiel van de gebruiker wanneer er geen groepsspecifiek profiel is ingesteld. Wanneer nieuwe leden toetreden, herzendt de admin alle opgeslagen groepsprofielen en elk lid herpubliceert zijn eigen profiel bij commit. Profielfoto's worden Marmot-media-versleuteld voor Blossom-upload. De PR bevat 16 nieuwe unittests en stelt de functie beschikbaar via zowel een CLI-commando (`update-group-profile`) als de UI.

Een nieuwe `pika-news` webapp ([PR #401](https://github.com/sledtools/pika/pull/401)) monitort Pika's eigen GitHub PR's en genereert automatisch stapsgewijze tutorial-doorlopen van PR-diffs, gepubliceerd als server-gerenderde pagina's met [NIP-07](/nl/topics/nip-07/)-authenticatie. Gebruikers kunnen specifieke tutorials in realtime bespreken via Nostr-geauthenticeerde chat.

### diVine: Insluitbare Widgets en Videoreacties

[diVine](https://github.com/divinevideo/divine-mobile), het Nostr-native videodelingsplatform, mergede 132 PR's in tien dagen. Insluitbare iframe-widgets ([PR #1843](https://github.com/divinevideo/divine-mobile/pull/1843)) bieden een op zichzelf staande `/embed?npub=...`-pagina die het profiel en de laatste video's van een gebruiker rendert. Videoreactiefunctionaliteit ([PR #1915](https://github.com/divinevideo/divine-mobile/pull/1915)), afgeschermd achter een feature flag, gebruikt Kind 1111-opmerkingen ([NIP-22](/nl/topics/nip-22/)) met [NIP-92](/nl/topics/nip-92/) (Media Attachments) imeta-metadata. Bluesky-geïnspireerde drieweg-inhoudsfilters ([PR #1797](https://github.com/divinevideo/divine-mobile/pull/1797)) bieden Show/Warn/Hide-besturingselementen over 17 [NIP-32](/nl/topics/nip-32/) content warning-categorieën.

### strfry: REQ-Filtervalidatie

[PR #163](https://github.com/hoytech/strfry/pull/163) voegt configureerbare REQ-filtervalidatie toe aan [strfry](https://github.com/hoytech/strfry), de C++ Nostr-relay. Operators kunnen maximale filters per REQ instellen, vereiste auteur- of tagaanwezigheid, toegestane kind-whitelists en per-filterkindlimieten. De functie richt zich op NWC relay-deployments die strikte filterhandhaving nodig hebben. Open: [PR #173](https://github.com/hoytech/strfry/pull/173) voegt optionele zstd-compressie toe voor eventpayloads bij ingest.

### rust-nostr: [NIP-62](/nl/topics/nip-62/) Request to Vanish

[rust-nostr](https://github.com/rust-nostr/nostr), de Rust Nostr-protocolbibliotheek, voegde [NIP-62](/nl/topics/nip-62/) (Request to Vanish) ondersteuning toe voor alle drie database-backends: [LMDB](https://github.com/rust-nostr/nostr/pull/1268), [SQLite](https://github.com/rust-nostr/nostr/pull/1270) en [in-memory](https://github.com/rust-nostr/nostr/pull/1272). De LMDB-implementatie bevat configureerbare opties om [NIP-09](/nl/topics/nip-09/) en NIP-62-handhaving per deployment in of uit te schakelen.

### NDK: Collaboratieve Events en NIP-46 Timeout

[NDK](https://github.com/nostr-dev-kit/ndk), de Nostr Development Kit voor JavaScript/TypeScript, mergede [PR #380](https://github.com/nostr-dev-kit/ndk/pull/380) die `NDKCollaborativeEvent` introduceert voor multi-auteur collaboratieve documenten met behulp van een adresseerbaar pointer event (kind 39382) dat geautoriseerde auteurs definieert. Een configureerbare timeout voor `NDKNip46Signer` ([PR #381](https://github.com/nostr-dev-kit/ndk/pull/381)) voorkomt dat [NIP-46](/nl/topics/nip-46/) remote ondertekeningsoperaties oneindig blijven hangen wanneer een bunker niet reageert.

### TENEX: Agentcategorisatie en Pubkey-Gating

[TENEX](https://github.com/tenex-chat/tenex), het Nostr-native AI-agentorchestratie-platform, mergede twee beveiligingsgerelateerde PR's. TIP-01 rolgebaseerde agentcategorisatie ([PR #91](https://github.com/tenex-chat/tenex/pull/91)) koppelt agentcategorieën (principal, orchestrator, worker, advisor, auditor) aan geautomatiseerde toolbeperkingen via een denied-tools map. Front-door pubkey-gating ([PR #87](https://github.com/tenex-chat/tenex/pull/87)) zorgt ervoor dat alleen events van gewhiteliste of backend-ondertekende pubkeys worden doorgestuurd naast bekende agents; onbekende pubkeys worden stilzwijgend gedropt met OpenTelemetry-spans voor audit.

### Zap Cooking: Lidmaatschapsdashboard

[Zap Cooking](https://github.com/zapcooking/frontend), het Nostr-gebaseerde receptendelingsplatform, mergede 25 PR's en 85 commits in tien dagen. Een lidmaatschapsdashboard ([PR #228](https://github.com/zapcooking/frontend/pull/228)) toont abonnementsstatus met vervaldatums en beheer-/upgrademogelijkheden, herschakelt feature gates voor Sous Chef- en Zappy-niveaus met zowel client-side als server-side controles, en standaardiseert niveaunaamgeving over 26 bestanden. Tweefasige groepsberichtlading ([PR #227](https://github.com/zapcooking/frontend/pull/227)) biedt een snelle 3-daagse initiële ophaling voor directe weergave gevolgd door een achtergrond-40-dagenterughaling.

Wallet mnemonic-opslag verhuisde van pubkey-afgeleide versleuteling naar [NIP-44](/nl/topics/nip-44/) encrypt-to-self ([PR #224](https://github.com/zapcooking/frontend/pull/224)), waarmee een kwetsbaarheid werd opgelost waarbij het oude schema zijn sleutel afleidde van `SHA-256(pubkey)`, wat effectief onversleuteld is aangezien pubkeys publiek zijn. Bestaande wallets worden stilzwijgend gemigreerd bij eerste gebruik. [NIP-29](/nl/topics/nip-29/) groepschat kreeg ongelezen-indicatoren met rode stip-badges en invite-only-toegang met kind 9009-uitnodigingscodes ([PR #213](https://github.com/zapcooking/frontend/pull/213)). Linkvoorbeelden en Nostr-eventembeds worden nu weergegeven in DM's en groepsberichten ([PR #218](https://github.com/zapcooking/frontend/pull/218)). Een Nostr-backupsectie in Instellingen ([PR #210](https://github.com/zapcooking/frontend/pull/210)) slaat follows en mutelistop via [NIP-78](/nl/topics/nip-78/) (Application-specific Data) versleutelde opslag met roterende 3-slotsversionering. Opstartprestaties verbeterden door uitgestelde notificatieservices, lazy DOM-rendering via IntersectionObserver (waardoor DOM-nodes daalden van ~15.000 naar ~3.000 bij een feed van 200 events), en verlengde outbox-cache-TTL's ([PR #208](https://github.com/zapcooking/frontend/pull/208)). Een aanpasbare printreceptmodal ([PR #205](https://github.com/zapcooking/frontend/pull/205)) laat gebruikers kiezen welke secties worden opgenomen met een livevoorbeeld. [Branta SDK](https://github.com/BrantaOps/branta-core) integratie ([PR #222](https://github.com/zapcooking/frontend/pull/222)) voegt verificatiebeveiligingen toe voor POST- en GET-verzoeken.

### Keep: Rust-Gedreven Statusmigratie

[Keep](https://github.com/privkeyio/keep-android), de Nostr-gebaseerde privésleutelbeheerder voor Android, mergede [PR #178](https://github.com/privkeyio/keep-android/pull/178), die vier Kotlin-configuratiestores verwijderde ten gunste van Rust-gedreven gedeelde status vanuit de keep-mobile-laag. Een 10-seconden polling-loop werd vervangen door push-gebaseerde `KeepStateCallback` vanuit Rust. [PR #179](https://github.com/privkeyio/keep-android/pull/179) voegt versleutelde back-up en herstel toe met wachtwoordzinbescherming.

### Mostro Mobile: Versleuteling van Geschillenchat

[Mostro Mobile](https://github.com/MostroP2P/mobile), de mobiele client voor het Mostro P2P Bitcoin-handelsplatform, bracht een tweefasige migratie uit van geschillenchatversleuteling. De eerste stap ([PR #495](https://github.com/MostroP2P/mobile/pull/495)) schakelt over van mostro-specifieke wrapping naar gedeelde sleutelversleuteling afgeleid van de pubkey van de admin. Hierop voortbouwend unificeert [PR #501](https://github.com/MostroP2P/mobile/pull/501) het berichtenmodel met `NostrEvent` en slaat gift wrap-events versleuteld op schijf op, consistent met het peer-to-peer chatpatroon. Een BIP-340 handtekeningfix ([PR #496](https://github.com/MostroP2P/mobile/pull/496)) overschrijft de bip340-afhankelijkheid naar 0.2.0, waarmee een `bigToBytes()`-paddingbug wordt opgelost die 1-2% van de Schnorr-handtekeningen ongeldig maakte en 100% falen veroorzaakte voor sleutels waarvan de publieke sleutel begint met `0x00`. Order Details toont nu leesbare statuslabels in plaats van ruwe protocolwaarden, gelokaliseerd in het Engels, Spaans, Italiaans en Frans ([PR #502](https://github.com/MostroP2P/mobile/pull/502)). HalCash werd toegevoegd en SEPA verwijderd als betaalmethode ([PR #493](https://github.com/MostroP2P/mobile/pull/493)), aangezien SEPA-overboekingen langer dan 24 uur kunnen duren (SEPA Instant blijft beschikbaar).

Aan de serverzijde repareerde [Mostro](https://github.com/MostroP2P/mostro) het herstel van geschillensessies om het initiator-veld op te nemen ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) en sluit nu automatisch actieve geschillen wanneer een verkoper fondsen vrijgeeft, waarbij een afgehandeld Nostr-event wordt gepubliceerd zodat admincients de resolutie zien ([PR #606](https://github.com/MostroP2P/mostro/pull/606)).

## Vijf Jaar Nostr-Februaries

[De nieuwsbrief van vorige maand](/nl/newsletters/2026-01-28-newsletter/#five-years-of-nostr-januaries) volgde Nostr's januarimijlpalen van vroege ontwikkeling via de Damus-doorbraak tot beveiligingsinfrastructuur in 2026. Dit retrospectief behandelt wat er elke februari gebeurde van 2021 tot 2026.

### Februari 2021: De Herschrijving

Drie maanden na het ontstaan produceerde Nostr's februari de meest consequentiële vroege wijziging van het protocol. Op 14-15 februari [herschreef fiatjaf NIP-01](https://github.com/nostr-protocol/nostr/commit/33a1a70), waarbij het oorspronkelijke berichtenformaat werd vervangen door het EVENT/REQ/CLOSE-model dat het protocol nog steeds gebruikt. Voor deze herschrijving communiceerden clients en relays via een eenvoudigere structuur. Het scheiden van eventpublicatie (EVENT) van abonnementsbeheer (REQ/CLOSE) maakte relay-side filtering mogelijk die essentieel zou blijken voor schaalbaarheid.

[NIP-04](/nl/topics/nip-04/) arriveerde dezelfde maand, met toevoeging van versleutelde directe berichten met gedeelde geheimen afgeleid van Diffie-Hellman-sleuteluitwisseling over secp256k1. De versleuteling was basaal (AES-256-CBC) en zou later worden vervangen door [NIP-44](/nl/topics/nip-44/)'s gecontroleerde cryptografie, maar het gaf de handvol vroege gebruikers hun eerste privé communicatiekanaal op het protocol.

Tooling breidde uit met [noscl](https://github.com/fiatjaf/noscl), een Go commandoregelclient voor terminalgebaseerde relay-interactie, en futurepaul startte [nostr-rs](https://github.com/futurepaul/nostr-rs), een vroege Rust-implementatie. Het gehele netwerk draaide op twee of drie relays, gecoördineerd via een [Telegram-groep](https://t.me/nostr_protocol), met ruwweg zeven actieve bijdragers.

### Februari 2022: Opbouwend Momentum

De [Hacker News-post](https://news.ycombinator.com/item?id=29749061) van 31 december 2021 bleef ontwikkelaars aantrekken tot in februari. Het [nostr-protocol/nostr](https://github.com/nostr-protocol/nostr)-repository (het formele [NIPs-repository](https://github.com/nostr-protocol/nips) zou pas in mei 2022 bestaan) ontving zes pull requests in februari, waaronder NIP-13 (Proof of Work) van vinliao, NIP-14 (Reputation) van fiatjaf, NIP-15 (Resource Relations) van Cameri en [NIP-17](https://github.com/nostr-protocol/nostr/pull/75) (Git Updates Over Nostr) van melvincarvalho. Het NIP-nummer werd later opnieuw toegewezen aan Private Direct Messages; git-samenwerking op Nostr ging apart door als wat [gitworkshop.dev](https://gitworkshop.dev) werd.

Greg Heartsfield's [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) was het werkpaard van de maand met 34 commits en drie releases. Versie 0.5.0 op 12 februari voegde [NIP-05](/nl/topics/nip-05/) geverifieerde gebruikerspublicatielimieten toe. Versies 0.5.1 en 0.5.2 volgden in de twee weken daarna, en de relay verwerkte het leeuwendeel van het netwerkverkeer in zijn eentje.

Robert C. Martin (Uncle Bob) bouwde [more-speech](https://github.com/unclebob/more-speech), een Clojure-desktopclient, met 69 commits tussen 18 januari en eind februari. Zijn betrokkenheid trok aandacht uit de bredere software-engineeringgemeenschap. fiatjaf's [nos2x](https://github.com/fiatjaf/nos2x) browserextensie leverde [NIP-04](/nl/topics/nip-04/) ontsleutelingsondersteuning en relayvoorkeurbeleid in februari, als implementatie van de `window.nostr`-interface ([NIP-07](/nl/topics/nip-07/)) die webclients nog steeds gebruiken voor sleuteldelegatie.

[Branle](https://github.com/fiatjaf/branle), nog steeds de primaire webclient, kreeg `web+nostr`-protocolhandlerregistratie op 13 februari, een vroege poging tot deep linking tussen Nostr-applicaties. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) verscherpte NIP-05-validatie. [go-nostr](https://github.com/nbd-wtf/go-nostr) voegde NIP-04 versleutelde DM-ondersteuning en NIP-12 (Generic Tag Queries) parsing toe over 11 commits. Het netwerk draaide op ruwweg 7-15 relays met een actieve gebruikersbasis van waarschijnlijk enkele honderden. Damus en Nostream bestonden nog niet en zouden pas verschijnen in april 2022.

### Februari 2023: Internationale Aandacht

Februari 2023 bracht Nostr zijn grootste golf van publieke aandacht. [Damus](https://github.com/damus-io/damus), de iOS-client van William Casarin, was [goedgekeurd in Apple's App Store op 31 januari](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store) na herhaalde afwijzingen. Op 1 februari bereikte het de top 10 in U.S. Social Networking. Twee dagen later, op 2 februari, [haalde Apple Damus uit China's App Store](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) naar verluidt op verzoek van de Cyberspace Administration of China.

Grote media waaronder TechCrunch en CoinDesk berichtten over de verwijdering, waardoor de bekendheid van zowel de app als het protocol werd vergroot. Unieke publieke sleutels met metadata op nostr.directory kruisten 300.000 op 3 februari. Alle relays werden beheerd door enthousiastelingen die uit eigen zak betaalden, en de infrastructuur worstelde om de belasting aan te kunnen. Ongeveer 289 relays werden bijgehouden begin februari, een aantal dat bleef stijgen.

Het [NIPs-repository](https://github.com/nostr-protocol/nips) registreerde 29 gemerge pull requests die maand, het hoogste aantal in een enkele maand in de protocolgeschiedenis tot dat moment. [NIP-57](https://github.com/nostr-protocol/nips/pull/224) (Lightning Zaps) en [NIP-23](https://github.com/nostr-protocol/nips/pull/220) (Long-form Content) werden beide gemerged op 13 februari, waardoor Bitcoin-microbetalingen werden toegevoegd en Nostr in een dag verder werd uitgebreid dan korte berichten. [NIP-65](/nl/topics/nip-65/) (Relay List Metadata) was een week eerder gemerged op 7 februari, wat het outbox-model mogelijk maakte dat volgde. [NIP-46](/nl/topics/nip-46/) (Nostr Connect) en [NIP-58](/nl/topics/nip-58/) (Badges) landden ook voor het einde van de maand.

De Human Rights Foundation [kende $50.000 toe aan William Casarin voor Nostr- en Damus-ontwikkeling](https://hrf.org/devfund2023q1) op 21 februari, een van de eerste institutionele subsidies voor een Nostr-project. OpenSats had zijn Nostr-fonds nog niet gelanceerd (dat zou komen in [juli 2023](https://opensats.org/blog/nostr-grants-july-2023)).

### Februari 2024: Protocolduurzaamheid

Februari 2024 verschoof de focus van groei naar protocolduurzaamheid. [NIP-17](/nl/topics/nip-17/) (Private Direct Messages), open sinds de vorige juli, werkte aan een vervanging voor de verouderende [NIP-04](/nl/topics/nip-04/) versleuteling met [NIP-44](/nl/topics/nip-44/)'s gecontroleerde cryptografie en [NIP-59](/nl/topics/nip-59/) gift wrapping. NIP-04 lekte metadata naar relayoperators, die afzender-ontvangerparen konden zien. NIP-17 verbergt de identiteit van de afzender achter wegwerpsleutelparen en werd die lente gemerged na een laatste beoordelingsronde in maart.

[NIP-29](/nl/topics/nip-29/) (Simple Groups) [werd gemerged op 28 februari](https://github.com/nostr-protocol/nips/pull/566) na maanden van discussie, waarmee werd gedefinieerd hoe relays gemodereerde groepschats kunnen hosten met adminrollen en toegangscontrole. [NIP-92](/nl/topics/nip-92/) (imeta-tags) werd gemerged op 1 februari, als standaardisering van hoe clients afbeeldingsdimensies en blurhash-voorbeelden koppelen aan media-events.

Op 16 februari voegde het NIPs-repository [BREAKING.md](https://github.com/nostr-protocol/nips/commit/62c48eff) toe, een bestand dat achterwaarts-incompatibele wijzigingen aan de protocolspecificatie bijhoudt. De creatie ervan erkende dat Nostr een volwassenheidsniveau had bereikt waarop brekende wijzigingen formele documentatie nodig hadden.

Tweeëntwintig pull requests werden die maand gemerged. [npub.cash](https://github.com/cashubtc/npubcash-server) lanceerde als een Lightning-adresservice waarmee elke npub betalingen kan ontvangen zonder een server te draaien. Een [academisch paper](https://arxiv.org/abs/2402.05709) gepubliceerd op 8 februari constateerde dat 95% van de gratis relays operationele kosten niet kon dekken door donaties, waarbij 35% van de betaalde relays toegangsgelden onder 1.000 sats (destijds ruwweg $0,45) in rekening bracht.

### Februari 2025: Infrastructuurgroei

Februari 2025 produceerde 28 gemerge pull requests voor het NIPs-repository. Een [Right to Vanish](/nl/topics/nip-62/) NIP werd gemerged op 19 februari, waarmee werd gedefinieerd hoe gebruikers verwijdering van hun data van relays kunnen aanvragen als reactie op regelgevingsvragen rond datadraagbaarheid en gebruikerscontrole.

[NIP-60](/nl/topics/nip-60/) (Cashu Wallet) en NIP-61 (Nutzaps) ontvingen vereenvoudigingsupdates, die het ecash-tokenopslagformaat stroomlijnden. Een q-tag (quote tag) uitrol ging verder over meerdere NIPs, waardoor werd gestandaardiseerd hoe events andere events refereren voor citeren en threading.

Clientreleases markeerden gestage vooruitgang. [Notedeck](https://github.com/damus-io/notedeck) v0.3.0 alpha verscheen op de laatste dag van januari, met adoptie die doorging in februari. Primal v2.1 volgde op 7 februari, en [GRAIN](https://github.com/0ceanSlim/grain) v0.3.0, een Go relay-implementatie, werd uitgebracht op 21 februari.

NOSTRLDN v5 bracht de Londense Nostr-gemeenschap samen voor zijn vijfde meetup. Een DVMCP-brug verbond Nostr's Data Vending Machines ([NIP-90](/nl/topics/nip-90/)) met het Model Context Protocol, als voorafschaduwing van het AI-agentintegratiewerk dat de volgende maand arriveerde.

### Februari 2026: Voorbij Social Media

*De activiteit van februari 2026 is ontleend aan Nostr Compass-edities [#8](/nl/newsletters/2026-02-04-newsletter/) tot [#11](/nl/newsletters/2026-02-25-newsletter/).*

Februari 2026 produceerde het breedste scala aan applicatielaag-ontwikkeling in enige Nostr-maand. [Mostro](https://github.com/MostroP2P/mostro) bracht zijn [eerste publieke beta](/nl/newsletters/2026-02-11-newsletter/#mostro-ships-first-public-beta) uit voor gedecentraliseerde peer-to-peer Bitcoin-handel, en [Zapstore](https://github.com/zapstore/zapstore) bereikte [1.0 stable](/nl/newsletters/2026-02-11-newsletter/#zapstore-v100) na maanden in release-candidate-testing. [White Noise v0.3.0](/nl/newsletters/2026-02-25-newsletter/#white-noise-v030) leverde realtime [Marmot](/nl/topics/mls/)-versleuteld berichtenverkeer met Amber-signerondersteuning en meer dan 160 samengevoegde verbeteringen.

Concurrerende AI-agentvoorstellen van pablof7z (NIP-AE voor agentworkflows, NIP-AD voor MCP-serveraankondigingen) en joelklabo (AI Agent Messages) arriveerden naast een [DVM Agent Coordination-voorstel](/nl/newsletters/2026-02-25-newsletter/#nip-updates) dat [NIP-90](/nl/topics/nip-90/) uitbreidt. [ContextVM](/nl/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr) bracht SDK-verbeteringen uit die het Model Context Protocol verbinden met Nostr-transport. [Burrow](/nl/newsletters/2026-02-25-newsletter/#burrow-mls-messaging-for-ai-agents) voegde [Marmot](/nl/topics/mls/)-versleuteld berichtenverkeer toe voor zowel AI-agenten als mensen, waardoor Nostr's identiteits- en relay-infrastructuur werd uitgebreid naar machine-naar-machine communicatie.

[FIPS](/nl/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking) leverde een werkende Rust-implementatie van Nostr-native mesh-netwerken, met secp256k1-sleutelparen als nodeidentiteiten met transportagnostische routing over UDP, Ethernet, Bluetooth of LoRa-radio. Het ontwerp toonde aan dat Nostr's sleutelmodel verder reikt dan social media tot fysieke netwerkinfrastructuur.

[OpenSats kondigde zijn vijftiende golf van Nostr-subsidies aan](https://opensats.org/blog/fifteenth-wave-of-nostr-grants), met financiering voor projecten waaronder ContextVM en Nostube. Protocolwijzigingen omvatten [NIP-47](/nl/topics/nip-47/) hold invoice-ondersteuning voor Nostr Wallet Connect en [NIP-45](/nl/topics/nip-45/) (Counting Results) HyperLogLog voor relay-side countschatting. [NIP-85](/nl/topics/nip-85/) (Trusted Assertions) vindbaarheid van serviceproviders voor [Web of Trust](/nl/topics/web-of-trust/)-scoring werd ook gemerged. [rust-nostr](https://github.com/rust-nostr/nostr) begon een volledige API-herontwerp terwijl Nostria 3.0 en [Frostr](https://github.com/FROSTR-ORG) (iOS TestFlight) beide verschenen. [Blossom](/nl/topics/blossom/)'s lokale cachelaag adresseerde mediabeschikbaarheid over relays.

### Vooruitkijkend

Vijf februaries van protocolgeschiedenis tonen een consistente progressie van fundamenteel werk naar applicatielaagdiversificatie, met de gebruikersinstroming van 2023 als het keerpunt. In 2021 werkten zeven bijdragers op drie relays. Tegen 2026 ondersteunde hetzelfde protocol mesh-netwerken en autonome agentvoorstellen op productie-infrastructuur.

---

Dat was het voor deze week. Bouw je iets of heb je nieuws te delen, neem dan contact op via <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/nl/topics/nip-17/) DM</a> of vind ons op Nostr.
