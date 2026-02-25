---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) brengt realtime berichten en Amber-signer-ondersteuning met meer dan 160 samengevoegde verbeteringen. [diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) lost problemen met videoweergave op en voegt Kind 22236 view-events toe voor makeranalyses. [Pika](https://github.com/sledtools/pika), [Ridestr](https://github.com/variablefate/ridestr) en [Unfiltered](https://github.com/dmcarrington/unfiltered) brengen updates uit. [FIPS](https://github.com/jmcorgan/fips) levert een werkende Rust-implementatie van Nostr-native mesh-netwerken. Notecrumbs krijgt stabiliteitsverbeteringen voor linkvoorbeelden van damus.io. [ContextVM](https://contextvm.org) verbindt Nostr met het Model Context Protocol. Nieuwe projecten zijn onder meer [Burrow](https://github.com/CentauriAgent/burrow) voor MLS-versleuteld berichtenverkeer tussen AI-agenten en mensen, en [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) voor browsergebaseerd kluis- en identiteitsbeheer. De deep dives behandelen NIP-55 Android-ondertekening en NIP-60 Cashu-walletsynchronisatie.

## Nieuws

### Stabiliteitsverbeteringen voor Notecrumbs

[Notecrumbs](https://github.com/damus-io/notecrumbs), de Nostr-API en webserver die linkvoorbeelden van damus.io aandrijft, ontving een reeks fixes voor betrouwbaarheidsproblemen.

De [concurrency-fix](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49) verving het inflight-deduplicatiemechanisme door watch channels. Twee aanroepers die dezelfde note opvroegen konden allebei fetcher worden, wat leidde tot een deadlock wanneer een van hen voltooide voordat de ander zich abonneerde op de notificatie. Watch channels met atomaire operaties zorgen ervoor dat slechts een fetcher draait terwijl anderen op het resultaat wachten.

[Rate limiting](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17) implementeert een tweelaagse verdediging tegen relay-hamering. Wanneer gebruikers herhaaldelijk dezelfde note benaderen, past het systeem nu debounce toe op relay-verzoeken met een cooldown-venster van 5 minuten. Deze bescherming strekt zich uit tot alle [NIP-19](/nl/topics/nip-19/)-typen en profielfeeds, en voorkomt proportionele spam naar relays tijdens druk verkeer.

[Prestatieverbeteringen](https://github.com/damus-io/notecrumbs/commit/38670b3972b6) verplaatsten secundaire data-opvragingen naar tokio-achtergrondtaken. Pagina's renderen nu direct met gecachte data in plaats van te blokkeren op sequentiele relay-timeouts die konden oplopen tot 7,5 seconden. Daarnaast is nostrdb geupgraded naar versie 0.10.0.

### ContextVM: MCP over Nostr

[ContextVM](https://contextvm.org) is een toolkit die Nostr en het [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) met elkaar verbindt. Recente commits introduceerden de nieuwe [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/)-specificatie voor betalingen, en hebben de [SDK](https://github.com/ContextVM/sdk) gedurende februari verbeterd.

De SDK biedt TypeScript client- en servertransports voor MCP over Nostr. Ontwikkelaars kunnen MCP-servers beschikbaar maken via het Nostr-netwerk en clients kunnen er verbinding mee maken. Relays fungeren als een blinde berichtenbus die versleutelde events blindelings routeert. Clients zonder native Nostr-ondersteuning verbinden via een proxylaag. De bibliotheek verzorgt relaybeheer en cryptografische ondertekening voor eventauthenticatie. Het werkt in zowel Node.js- als browseromgevingen.

[CVMI](https://github.com/ContextVM/cvmi) biedt een CLI voor serverontdekking en methodeaanroep. [Relatr](https://github.com/ContextVM/relatr) berekent gepersonaliseerde vertrouwensscores op basis van afstand in de sociale graaf gecombineerd met profielvalidatie.

ContextVM positioneert zichzelf als een bruglaag: bestaande MCP-servers krijgen Nostr-interoperabiliteit terwijl ze hun conventionele transports behouden.

### White Noise Documenteert Gedecentraliseerd Gebruikers Zoeken

In een [blogpost](https://blog.jgmontoya.com/2026/02/22/user-search.html) beschrijft jgmontoya hoe [White Noise](https://github.com/marmot-protocol/whitenoise) gebruikerszoekfunctionaliteit afhandelt over het gedecentraliseerde relay-netwerk.

Profieldistributie creeert de uitdaging: anders dan gecentraliseerde messengers met uniforme databases, zijn Nostr-profielen verspreid over tientallen relays zonder centraal register. White Noise lost dit op via een producer-consumer-architectuur die parallel draait.

Het producerproces breidt de sociale graaf continu uit vanuit de follows van de gebruiker, haalt followlijsten op bij toenemende afstanden en plaatst ontdekte pubkeys in een wachtrij voor profielresolutie. De consumer matcht via vijf steeds duurdere niveaus: lokale gebruikerstabel (snelst), gecachte profielen van eerdere zoekopdrachten, verbonden relays, gebruikersrelaylijsten per [NIP-65](/nl/topics/nip-65/), en directe queries naar door gebruikers gedeclareerde relays (traagst).

Koude zoekopdrachten duren ongeveer 3 seconden terwijl warme zoekopdrachten uit de cache terugvallen naar circa 10 milliseconden. Voor nieuwe gebruikers zonder gevestigde sociale graaf injecteert het systeem goed verbonden bootstrap-nodes om zoekfunctionaliteit te garanderen. Groepslidmaatschap biedt een impliciet sociaal signaal naast expliciete follows.

Instrumentatie bleek cruciaal voor optimalisatie, merkt de auteur op. Zonder meetgegevens waren verbeteringen giswerk.

### FIPS: Nostr-Native Mesh-Netwerken

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System) is een werkende Rust-implementatie van een zelforganiserend mesh-netwerk dat Nostr-sleutelparen (secp256k1) gebruikt als nodeidentiteiten. De [ontwerpdocumentatie](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md) vergezelt de functionele code.

Het protocol richt zich op infrastructuuronafhankelijkheid: nodes ontdekken elkaar automatisch zonder centrale servers of certificaatautoriteiten. Via een spanning tree verloopt op coordinaten gebaseerde routing terwijl bloomfilters bereikbaarheidsinformatie verspreiden, waardoor nodes met alleen lokale kennis forwardingbeslissingen kunnen nemen. Transportagnosticisme betekent dat hetzelfde protocol werkt over UDP, Ethernet, Bluetooth, LoRa-radio of elk ander medium dat datagrammen ondersteunt.

Twee encryptielagen beschermen het verkeer. Link-layer-encryptie (Noise IK-patroon) beveiligt hop-by-hop-communicatie tussen buren met wederzijdse authenticatie en forward secrecy. Session-layer-encryptie (Noise XK-patroon) biedt end-to-end-bescherming tegen tussenliggende routers, waarbij alleen de bestemming de payload kan ontsleutelen. Dit weerspiegelt hoe TLS HTTP-verkeer beschermt, zelfs bij het doorkruisen van onvertrouwde netwerken.

De architectuur gebruikt een "greedy embedding" spanning tree voor routing. Elke node krijgt coordinaten op basis van zijn positie ten opzichte van de boomwortel en ouder. Pakketten routeren greedy richting coordinaten dichter bij de bestemming, terwijl bloomfilters bereikbare eindpunten adverteren. Wanneer greedy routing faalt (lokale minima), kunnen nodes terugvallen op boomgebaseerde paden.

De Rust-implementatie bevat al UDP-transport met bloomfilterontdekking. Toekomstig werk richt zich op Nostr-relayintegratie voor peer-bootstrapping.

## Releases

Deze week bracht releases in relay-infrastructuur en clientapplicaties, met ook nieuwe projecten die de ruimte betreden.

### HAVEN v1.2.0

[HAVEN](https://github.com/bitvora/haven), de alles-in-een persoonlijke relay die vier relayfuncties bundelt met een [Blossom](/nl/topics/blossom/)-mediaserver, bracht [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0) uit. Deze release gaat verder dan de RC-fase [die vorige week werd behandeld](/nl/newsletters/2026-02-18-newsletter/#haven-v120-rc3).

Multi-npub-ondersteuning laat een enkele HAVEN-instantie meerdere Nostr-identiteiten bedienen via whitelisting, met nieuwe blacklistingfunctionaliteit voor toegangscontrole. Het herschreven back-upsysteem gebruikt draagbaar JSONL-formaat, met een `haven restore`-commando voor het importeren van notes uit JSONL-bestanden. Cloudopslagintegratie voegt `--to-cloud`- en `--from-cloud`-vlaggen toe voor extern back-upbeheer.

[Web of Trust](/nl/topics/web-of-trust/)-verbeteringen omvatten configureerbare diepteniveaus voor vertrouwensberekeningen en automatische 24-uurs verversingsintervallen met lockless optimalisatie die geheugenoverhead vermindert. User-agent-configuratie voor relayverzoeken en configureerbare Blastr-timeoutinstellingen completeren de release, samen met data-export naar gecomprimeerd JSONL.

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise), de op [MLS](/nl/topics/mls/) gebaseerde versleutelde berichtenapp die het [Marmot](/nl/topics/marmot/)-protocol implementeert, bracht [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) uit met meer dan 160 samengevoegde verbeteringen.

Deze release brengt realtime berichten via streamingverbindingen in plaats van polling, zodat berichten direct aankomen. Amber-ondersteuning ([NIP-55](/nl/topics/nip-55/)) betekent dat prive-sleutels de app nooit hoeven te raken. Het delen van afbeeldingen werkt nu met uploadvoortgangsregistratie en blurhash-plaatshouders tijdens het laden. Volledig-schermweergave ondersteunt pinch-to-zoom.

Groepsberichten kregen betrouwbaarheidsverbeteringen met chatlijsten die afzendernamen tonen en [MLS](/nl/topics/mls/)-versleuteling die forward secrecy garandeert. Gebruikerszoeken breidt zich uit vanuit follows tot vier graden van scheiding, met resultaten die binnenstromen zodra ze worden gevonden.

Let op: een brekende wijziging reset alle lokale data bij het upgraden vanwege Marmot-protocolwijzigingen en de overstap naar versleutelde lokale opslag. Gebruikers moeten nsec-sleutels back-uppen voordat ze upgraden.

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile), de short-form looping videoclient gebouwd op herstelde Vine-archieven, bracht [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) uit met uitgebreide videoweergave-fixes en een nieuw gedecentraliseerd analysesysteem.

Videoweergaveproblemen domineerden de fixes: fantoomonderbreking, dubbele audio tussen video's, zwarte flits tussen thumbnails en eerste frames, en crashes bij afgedankte spelers zijn allemaal opgelost. De Home-feed draait nu op een gepoold videospeler voor consistente weergave.

Kind 22236 efemere view-events maken makeranalyses en aanbevelingen mogelijk. Het systeem volgt verkeersbronnen (home, ontdekkingsvarianten, profiel, delen, zoeken) en lustellingen terwijl zelfweergaven worden uitgefilterd. Lekken van lokale bestandspaden in Nostr-event imeta-tags zijn verholpen met canonieke Blossom-URL's die client-side worden opgebouwd conform de BUD-01-specificatie.

[NIP-46](/nl/topics/nip-46/) remote signer-verbeteringen omvatten geparallelliseerde relayverbindingen en callback-URL-ondersteuning. Android herstelt WebSocket-verbindingen bij het hervatten van de app na goedkeuring door de signer.

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle), de webgebaseerde Nostr-client gericht op relaybeheer en [Web of Trust](/nl/topics/web-of-trust/)-moderatie, bracht [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30) uit met ondersteuning voor videothumbnails, wat mediabrowsing in feeds verbetert.

Nostur bracht ook deze week een update uit voor iOS.

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public), de iOS Nostr-client, bracht [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0) uit met een nieuwe Live Streams-feedsectie en een herontworpen Instellingen-scherm. GIF's kunnen nu worden gehost op Blossom-mediaservers, waardoor de afhankelijkheid van gecentraliseerde diensten afneemt. Klipy GIF-integratie biedt een terugvalmogelijkheid wanneer Tenor onbeschikbaar is. Jaarkopteksten in DM-gesprekken en weergave van het aantal vermeldingen completeren de gebruikersgerichte wijzigingen.

Ontwikkeltools en CLI-apps kregen deze week ook updates.

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak), fiatjaf's Zwitsers zakmes voor Nostr op de commandoregel, bracht [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5) uit met een nieuw `nak profile`-subcommando voor het ophalen en weergeven van gebruikersprofielen. Het `git clone`-commando ondersteunt nu [NIP-05](/nl/topics/nip-05/)-namen in `nostr://`-URI's, waardoor repositories kunnen worden gekloond op basis van voor mensen leesbare identifiers.

Pika verbeterde zijn cross-platform messenger.

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika), de [MLS](/nl/topics/mls/)-versleutelde messenger voor iOS, Android en desktop gebouwd op het [Marmot](/nl/topics/marmot/)-protocol, bracht [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3) uit. Recente commits voegen bestandsupload en drag-and-drop media-ondersteuning toe aan de desktop-app, naast Cloudflare Workers-deploymentfixes.

Pika gebruikt een Rust-core die alle bedrijfslogica bezit, terwijl iOS (SwiftUI) en Android (Kotlin) als dunne UI-lagen fungeren die state-snapshots renderen. MDK (Marmot Development Kit) biedt de MLS-implementatie. Het project vermeldt alfastatus en waarschuwt tegen gebruik voor gevoelige werklasten.

Het gedecentraliseerde ritdeelplatform Ridestr kreeg ook een update.

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr), het gedecentraliseerde ritdeelplatform met Cashu-betalingen, bracht [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6) uit. Deze release lost TalkBack-toegankelijkheidsproblemen op en verhelpt bugs waarbij chauffeurs verdwenen van de lijst met nabije chauffeurs bij het wisselen van betaalmethoden of waarbij geselecteerde chauffeurstellingen niet werden bijgewerkt wanneer chauffeurs offline gingen.

De "Send to All"-functie is nu "Broadcast RoadFlare" met fixes voor stille fouten bij nieuwe chauffeurinstallaties. Ridestr implementeert HTLC-escrow voor vertrouwensloze ritbetalingen en [NIP-60](/nl/topics/nip-60/)-walletsynchronisatie tussen apparaten.

Unfiltered breidde zijn fotodeel-app voor Android uit.

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered), de Instagram-achtige fotodeel-app voor Android, bracht [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6) uit met verbeterde gebruikerszoekfunctie en automatische relay-herverbinding elke 60 seconden.

Gebouwd met Kotlin en Jetpack Compose, gebruikt Unfiltered rust-nostr-bindings en Blossom-compatibele servers voor afbeeldingshosting. Amber-integratie ([NIP-55](/nl/topics/nip-55/)) verzorgt veilig sleutelbeheer. De app toont berichten van gevolgde accounts in chronologische volgorde zonder algoritmen of advertenties.

Deze week werden ook twee nieuwe berichten- en ondertekeningsprojecten gelanceerd.

### Burrow: MLS-Berichtenverkeer voor AI-Agenten

[Burrow](https://github.com/CentauriAgent/burrow) is een messenger die het [Marmot](/nl/topics/marmot/)-protocol implementeert voor MLS-versleutelde communicatie zonder telefoonnummers of gecentraliseerde servers. Zowel menselijke gebruikers als AI-agenten kunnen deelnemen.

De pure Rust CLI-daemon met JSONL-uitvoermodus verzorgt integratie met geautomatiseerde systemen. Via een Flutter cross-platform app worden Android, iOS, Linux, macOS en Windows ondersteund. Mediabijlagen worden versleuteld samen met berichten, en WebRTC verzorgt audio- en videogesprekken met configureerbare TURN-servers.

Burrow legt MLS-versleuteling over Nostr-infrastructuur. Identiteit gebruikt Nostr-sleutelparen (secp256k1) terwijl MLS-KeyPackages worden gepubliceerd als kind 443-events. Berichten worden versleuteld met [NIP-44](/nl/topics/nip-44/) als kind 445-events, en welkomstuitnodigingen gebruiken [NIP-59](/nl/topics/nip-59/) gift-wrapping.

[OpenClaw](https://openclaw.ai)-integratie maakt AI-agentdeelname mogelijk met volledige toegang tot tools. Toegangscontrolelijsten met auditlogging beheren contact- en groepsmachtigingen. Deze combinatie positioneert Burrow voor agent-naar-agent en agent-naar-mens berichtenscenario's die Signal-niveau versleuteling op gedecentraliseerde infrastructuur vereisen.

Nostria Signer bracht identiteitsbeheer naar de browser.

### Nostria Signer-Extensie

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) is een op Chromium gebaseerde browserextensie die kluis- en identiteitsbeheer biedt voor Nostr-gebruikers.

Meerdere kluizen met meerdere accounts laten gebruikers identiteiten organiseren voor verschillende contexten. Internationalisatie omvat ondersteuning voor RTL-talen. Gebouwd met Angular en TypeScript (79,2% van de codebase), werkt het als zowel browserextensie als Progressive Web App.

Nostria Signer implementeert [NIP-07](/nl/topics/nip-07/) voor ondertekening via browserextensies, waardoor webgebaseerde Nostr-clients eventhandtekeningen kunnen aanvragen zonder direct toegang te krijgen tot prive-sleutels. Automatische walletmigratie verzorgt updates die via de Chrome Web Store worden verspreid. Gebruikers kunnen ook sideloaden vanuit de `dist/extension`-map.

Ontwikkelaars benadrukken de experimentele status: gebruikers moeten hun eigen geheime herstelzinnen beheren aangezien de ontwikkelaars geen toegang tot verloren sleutels kunnen herstellen.

## Projectupdates

### Formstr Migreert naar Nieuwe Organisatie

[Formstr](https://github.com/formstr-hq/nostr-forms), het Google Forms-alternatief op Nostr, migreerde zijn repository van `abh3po/nostr-forms` naar de `formstr-hq`-organisatie. Deze OpenSats-subsidie-ontvanger zet de ontwikkeling voort op de nieuwe locatie.

### Opvallende Open PR's

Lopend werk in Nostr-projecten:

- **Damus Outbox Model** ([PR #3602](https://github.com/damus-io/damus/pull/3602)): Implementatieplan voor het gossip/outbox relay-model op iOS. Deze architecturale wijziging verbetert berichtaflevering door te publiceren naar de relays waar ontvangers daadwerkelijk lezen.

- **Notedeck Cross-Platform Notificaties** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296)): Native notificatiesysteem voor de Damus-desktopclient voor Android FCM, macOS en Linux.

- **NDK Cashu v3 Upgrade** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)): Upgradet de walletintegratie van de Nostr Development Kit naar cashu-ts v3.

- **Zeus Cashu Offline** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742)): Offline ecash verzenden en ontvangen voor de Zeus Lightning-wallet.

- **Shopstr Versleutelde Digitale Levering** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231)): Voegt versleutelde levering voor digitale goederen toe met dynamische gewichtsondersteuning voor fysieke artikelen.

## NIP-Updates

Recente wijzigingen in het [NIPs-repository](https://github.com/nostr-protocol/nips):

**Deze week gemerged:**

- **[NIP-85 Vindbaarheid van Serviceproviders](https://github.com/nostr-protocol/nips/pull/2223)**: De [NIP-85](/nl/topics/nip-85/)-specificatie bevat nu richtlijnen over hoe clients trusted assertion-providers ontdekken. Wanneer een client [Web of Trust](/nl/topics/web-of-trust/)-scores of andere berekende metrics nodig heeft, kan het relays bevragen op kind 30085-aankondigingen van providers die de gebruiker al volgt of vertrouwt.

- **[NIP-29 Verwijdert Onbeheerde Groepen](https://github.com/nostr-protocol/nips/pull/2229)**: De [NIP-29](/nl/topics/nip-29/)-groepschatspecificatie schrapte ondersteuning voor onbeheerde groepen (waar elk lid anderen kon toevoegen). Alle NIP-29-groepen vereisen nu relay-side beheer met expliciete adminrollen, wat implementaties vereenvoudigt en spamvectoren vermindert.

- **[NIP-11 Verwijdert Verouderde Velden](https://github.com/nostr-protocol/nips/pull/2231)**: [NIP-11](/nl/topics/nip-11/) relay-informatiedocumenten bevatten niet langer de verouderde velden `software` en `version`. Implementaties moeten deze verwijderen uit hun responses.

- **[NIP-39 Verplaatst Identiteitstags](https://github.com/nostr-protocol/nips/pull/2227)**: Externe identiteitsclaims ([NIP-39](/nl/topics/nip-39/) `i`-tags voor GitHub, Twitter, etc.) zijn verplaatst van kind 0-profielen naar speciale kind 30382-events. Dit scheidt identiteitsverificatie van profielmetadata.

**Voortgang AI-Agent NIPs:**

Vier op AI gerichte NIPs blijven actief in ontwikkeling. Sinds [de behandeling vorige week](/nl/newsletters/2026-02-18-newsletter/#ai-agent-nips-arriveren):

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)** (bijgewerkt 19 feb): Definieert agentidentiteit met kind 4199 voor agentdefinities en kind 4201 voor prompting ("nudges"). Agenten kunnen [NIP-94](/nl/topics/nip-94/)-bestandsmetadata refereren voor uitgebreide beschrijvingen.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)** (bijgewerkt 18 feb): Standaardiseert conversatieberichten met zeven efemere event-kinds (25800-25806) voor status, streaming deltas, prompts, responses, tool calls, fouten en annulering. Kind 31340 "AI Info"-events laten agenten ondersteunde modellen en mogelijkheden adverteren.

- **[NIP-AC: DVM Agent Coordination](https://github.com/nostr-protocol/nips/pull/2228)** (geopend 18 feb): Breidt [NIP-90](/nl/topics/nip-90/) uit voor autonome agentworkflows. Voegt heartbeats toe voor agentontdekking, jobbeoordeling voor kwaliteitsmonitoring, data-escrow voor resultaatcommitment, workflowketens voor meerstaps-pipelines, en swarmbiedingen voor competitieve providerselectie. Op 2020117.xyz draait een referentie-implementatie.

- **[NIP-AD: MCP Server Announcements](https://github.com/nostr-protocol/nips/pull/2221)** (geopend 12 feb): Standaardiseert de aankondiging van Model Context Protocol-servers en vaardigheden op Nostr. Al in gebruik op het TENEX-platform.

**Overige Open PR's:**

- **[NIP-144: Service Authorization Protocol](https://github.com/nostr-protocol/nips/pull/2232)**: Definieert hoe clients identiteit en machtigingen bewijzen aan serviceproviders op Nostr.

- **[NIP-DC: Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**: alexgleason stelt voor om Webxdc (gedecentraliseerde webapplicaties) te integreren met Nostr-events.

## NIP Deep Dive: NIP-55 (Android Signer Applicatie)

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md) definieert hoe Android Nostr-clients cryptografische operaties aanvragen bij speciale signer-applicaties. Met [White Noise v0.3.0](#white-noise-v030) en [Unfiltered v1.0.6](#unfiltered-v106) die deze week beide Amber-ondersteuning toevoegen, verdient het Android-ondertekeningsprotocol aandacht.

**Communicatiekanalen:**

NIP-55 maakt inter-app-ondertekening mogelijk via twee mechanismen. Intents bieden handmatige gebruikersgoedkeuring met visuele feedback voor eenmalige operaties. Content Resolvers maken geautomatiseerde ondertekening mogelijk wanneer gebruikers permanente machtigingen verlenen, waardoor apps op de achtergrond kunnen ondertekenen zonder herhaalde prompts.

Communicatie gebruikt het aangepaste `nostrsigner:`-URI-schema. Een client initieert contact met:

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**Ondersteunde Operaties:**

De specificatie definieert zeven cryptografische methoden: eventondertekening (`sign_event`), ophalen van publieke sleutel (`get_public_key`), [NIP-04](/nl/topics/nip-04/)-versleuteling/ontsleuteling, [NIP-44](/nl/topics/nip-44/)-versleuteling/ontsleuteling, en zap-eventontsleuteling (`decrypt_zap_event`).

**Machtigingsmodel:**

Clients roepen `get_public_key` eenmalig aan om een vertrouwensrelatie op te bouwen, waarbij ze de pakketnaam van de signer en de pubkey van de gebruiker ontvangen. De specificatie schrijft voor dat clients deze waarden opslaan en nooit opnieuw `get_public_key` aanroepen, om fingerprinting-aanvallen te voorkomen.

Voor ondertekeningsverzoeken kunnen gebruikers eenmalig goedkeuren of "onthoud mijn keuze" verlenen voor achtergrondoperaties. Als gebruikers operaties consistent weigeren, retourneert de signer een "afgewezen"-status om herhaalde prompts te voorkomen.

**Implementaties:**

[Amber](https://github.com/greenart7c3/amber) is de primaire NIP-55-signer voor Android. Clients die NIP-55 ondersteunen zijn onder meer [Amethyst](https://github.com/vitorpamplona/amethyst), [White Noise](#white-noise-v030), [Unfiltered](#unfiltered-v106), en andere. Webapplicaties kunnen niet direct signer-responses ontvangen en moeten callback-URL's of klembordoperaties gebruiken.

**Relatie met Andere Ondertekenings-NIPs:**

NIP-55 is een aanvulling op [NIP-07](/nl/topics/nip-07/) (browserextensies) en [NIP-46](/nl/topics/nip-46/) (remote ondertekening via relays). Waar NIP-07 desktopbrowsers afhandelt en NIP-46 cross-device-ondertekening verzorgt, biedt NIP-55 native Android-integratie met minimale latentie.

## NIP Deep Dive: NIP-60 (Cashu Wallet)

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) definieert hoe [Cashu](/nl/topics/cashu/) ecash-wallets hun status opslaan op Nostr-relays, waardoor cross-applicatie walletsynchronisatie mogelijk wordt. Met [Ridestr v0.2.6](#ridestr-v026) die NIP-60 gebruikt voor walletsynchronisatie tussen apparaten, verdient het protocol aandacht.

**Event Kinds:**

NIP-60 gebruikt vier eventtypen. Het vervangbare kind 17375 slaat walletconfiguratie op inclusief mint-URL's en een speciale prive-sleutel voor het ontvangen van P2PK ecash-betalingen. Token-events (kind 7375) bevatten onbestede cryptografische bewijzen, terwijl bestedingsgeschiedenis (kind 7376) transacties registreert voor gebruikerstransparantie. Een optioneel kind 7374 volgt mint-betalingsoffertes.

**Walletarchitectuur:**

Walletstatus leeft op relays, waardoor het toegankelijk is over applicaties heen. Het wallet-event van een gebruiker bevat versleutelde verwijzingen naar Cashu-mints en een walletspecifieke prive-sleutel gescheiden van de Nostr-identiteit van de gebruiker. Deze scheiding is van belang: de walletsleutel verzorgt ecash-operaties terwijl de Nostr-sleutel sociale functies afhandelt.

```json
{
  "kind": 17375,
  "content": "<nip44-encrypted-wallet-config>",
  "tags": [["d", "cashu-wallet"]]
}
```

**Bewijsbeheer:**

Cashu-bewijzen zijn toonderinstrumenten. Zodra besteed, wordt een bewijs ongeldig. NIP-60 beheert dit via een rollover-mechanisme: bij het besteden maken clients een nieuw token-event met resterende onbestede bewijzen en verwijderen het origineel via [NIP-09](/nl/topics/nip-09/). Vernietigde token-ID's gaan in een `del`-veld voor statusregistratie.

Clients moeten periodiek bewijzen valideren tegen mints om eerder bestede credentials te detecteren. Meerdere token-events per mint zijn toegestaan, en bestedingsgeschiedenisevents helpen gebruikers transacties te volgen, al zijn ze optioneel.

**Beveiligingsmodel:**

Alle gevoelige data gebruikt [NIP-44](/nl/topics/nip-44/)-versleuteling. De prive-sleutel van de wallet verschijnt nooit in leesbare tekst. Aangezien relays versleutelde blobs opslaan zonder de inhoud te begrijpen, blijft de walletstatus privaat, zelfs op onvertrouwde relays.

**Implementaties:**

Wallets die NIP-60 ondersteunen zijn onder meer [Nutsack](https://github.com/gandlafbtc/nutsack) en [eNuts](https://github.com/cashubtc/eNuts). Clients zoals [Ridestr](#ridestr-v026) gebruiken NIP-60 voor synchronisatie tussen apparaten, waardoor gebruikers op desktop kunnen opwaarderen en vanaf mobiel kunnen besteden zonder handmatige overdrachten.

---

Dat was het voor deze week. Bouw je iets of heb je nieuws te delen, neem dan contact op via <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/nl/topics/nip-17/) DM</a> of vind ons op Nostr.
