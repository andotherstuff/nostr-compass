---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** Bitchat vervangt C Tor door de Rust Arti-implementatie voor betere betrouwbaarheid en prestaties. nostrdb-rs krijgt streaming fold queries die zero-allocation databasebewerkingen mogelijk maken. Listr ondergaat een grote refactoring met NDK 3 beta migratie en AI-ondersteund onderhoud na een jaar stilstand. Zeus verzond 17 samengevoegde PRs gericht op [NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect voor afstandsbediening van Lightning) fixes en Cashu-verbeteringen, terwijl Primal Android wallet backup flows en [NIP-92](/nl/topics/nip-92/) (mediadimensies voor correcte beeldverhoudingen) ondersteuning toevoegt. Een nieuw concept NIP stelt [Trusted Relay Assertions](/nl/topics/trusted-relay-assertions/) voor voor gestandaardiseerde relay trust scoring.

## Nieuws

### Bitchat gaat over naar Rust Arti voor Tor-ondersteuning

Bitchat is gemigreerd van C Tor naar [Arti](https://gitlab.torproject.org/tpo/core/arti), de Rust-implementatie van het Tor protocol. [PR #958](https://github.com/permissionlesstech/bitchat/pull/958) verwijdert de C Tor-afhankelijkheid en integreert Arti, wat geheugenveiliigheidsgaranties en verbeterde betrouwbaarheid biedt. De wijziging elimineert dormante wake-pogingen die serviceherstart op de voorgrond veroorzaakten, een langlopend probleem met de C-implementatie.

**Wat dit voor gebruikers betekent:** Stabieler versleuteld berichten met minder verbreken, vooral op mobiele apparaten. De Rust-implementatie vermindert crashrisico's en batterijdrain door constante heraansluitingspogingen.

Arti is een volledig herschrijven van Tor in Rust, ontwikkeld door het Tor Project om betere beveiliging door geheugenveiliigheid en gemakkelijkere integratie in applicaties te bieden. Voor Bitchat verminderen de geheugenveiliigheidseigenschappen de aanvalsoppervlakte bij het verwerken van versleutelde berichten en relay-verbindingen. De migratie volgt de recente [Cure53 security audit](/nl/newsletters/2026-01-13-newsletter/#bitchat-completes-cure53-security-audit) van het team (behandeld in Newsletter #5), waarmee hun beveiligingsverbeteringen worden voortgezet.

De PR introduceert ook uitgebreide testdekking voor ChatViewModel en BLEService, verwijdert dode code en stabiliseert de testsuite. Bluetooth Low Energy mesh betrouwbaarheidsverbeteringen gaan gepaard met de Tor-wijzigingen, waardoor grote overdrachtfouten worden aangepakt. Samen verbeteren deze wijzigingen Bitchat's veerkracht voor offline mesh-netwerk-scenario's waarin Tor internetconnectiviteit naast lokale BLE-communicatie biedt.


### Listr herleefd met AI-ondersteund onderhoud

JeffG kondigde een grote refactoring van [Listr](https://github.com/erskingardner/listr), de Nostr lijstbeheertoepassing beschikbaar op [listr.lol](https://listr.lol), aan na een jaar stilstand van het project. Met AI-ondersteuning voltooide hij een uitgebreide upgrade inclusief migratie naar [NDK](https://github.com/nostr-dev-kit/ndk) 3 beta, updates naar de nieuwste versies van Svelte en Vite, en alle afhankelijkheden up-to-date gebracht. De refactoring voegt eersteklas ondersteuning voor follow packs toe, implementeert paginering voor lijsten met meer dan 50 items, en verhelpt talrijke bugs die zich hadden opgehoopt tijdens de stilstandsperiode.

**Wat dit voor gebruikers betekent:** Listr is terug online met verbeterde prestaties en nieuwe functies voor het beheren van volglijsten, inhoudsollecties en onderwerpscuratie. De paginafiksering maakt grote lijsten eigenlijk bruikbaar.

JeffG merkte op dat zonder AI-ondersteuning dit onderhoudswerk waarschijnlijk nooit zou zijn gebeurd, waardoor het project was verlaten. Listr maakt inhoudscuratie op Nostr mogelijk, waardoor gebruikers lijsten van profielen, onderwerpen en bronnen kunnen maken, beheren en delen. De upgrade houdt de applicatie compatibel met huidige Nostr-standaarden en client-verwachtingen als lijstbeheer centraler wordt voor content discovery op het protocol.


## NIP Updates

Recente wijzigingen in de [NIPs repository](https://github.com/nostr-protocol/nips):

**Samengevoegd:**

- **[NIP-29](/nl/topics/nip-29/)** (Relay-based groups) - Relay Key Clarification ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - samengevoegd) verduidelijkt dat de relay-sleutel de relay URL zelf is, niet een pubkey. De spec stelt nu expliciet: "De relay-sleutel is de relay's WebSocket URL (bijv. wss://groups.example.com)" om verwarring te voorkomen. Dit beïnvloedt hoe clients bepalen welke relay een bepaalde groep host, zodat groepen correct worden toegeschreven aan hun hosting-relays.

**Open PRs en Discussies:**

- **Trusted Relay Assertions** - Een concept NIP stelt het standaardiseren van relay trust scoring voor via kind 30385 events met trust scores (0-100) berekend uit [NIP-66](/nl/topics/nip-66/) (relay discovery en monitoring) metriek, operator reputatie en gebruiksrapportages. De specificatie verdeelt trust in betrouwbaarheid (uptime, latentie), kwaliteit (TLS, documentatie, operator verificatie) en toegankelijkheid (jurisdictie, barrières, surveillancerisico) componenten. Operator verificatie omvat cryptografische handtekeningen via [NIP-11](/nl/topics/nip-11/) (relay informatiedocumenten), DNS TXT records en .well-known bestanden. Gebruikers declareren vertrouwde assertion providers via kind 10385 events, waardoor clients meerdere providers kunnen raadplegen voor diverse perspectieven. Het voorstel complementeert [NIP-66](/nl/topics/nip-66/) discovery met evaluatie, waardoor [NIP-46](/nl/topics/nip-46/) (afstandsbediening/Nostr Connect) relay betrouwbaarheid in verbindings-URI's kan beoordelen.

- **Post-Quantum Cryptography** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) (open) evolueert voort sinds [Newsletter #5](/nl/newsletters/2026-01-13-newsletter/#nip-updates) het voorstel voor quantum-resistente algoritmen introduceerde. De discussie deze week concentreerde zich op implementatiedetails voor crypto-agility: hoe clients dual signatures afhandelen tijdens migratie, achterwaartse compatibiliteit voor oudere clients en prestatieimplicaties van grotere quantum-resistente handtekeningen. Bijdragers debatteerden of men ML-DSA-44 alleen zou mandateren of meerdere algoritmen (ML-DSA-44, Falcon-512, Dilithium) zou ondersteunen voor flexibiliteit. De consensus neigt naar een gefaseerde benadering: optionele quantum signatures aanvankelijk, alleen verplicht nadat brede client-ondersteuning en echte quantum-dreiging ontstaan.


## NIP Deep Dive: NIP-11 en NIP-66

Deze week onderzoeken we twee NIPs die samenwerken om relay discovery en evaluatie mogelijk te maken: NIP-11 bepaalt hoe relays zichzelf beschrijven, en NIP-66 standardiseert hoe we relay-gedrag meten. Samen vormen ze de basis voor relay trust evaluatiesystemen.

### [NIP-11](/nl/topics/nip-11/): Relay Informatiedocument

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md) bepaalt een JSON-document dat relays via HTTP serveren om hun mogelijkheden, beleid en operatorinformatie te beschrijven. Wanneer een client verbinding maakt met `wss://relay.example.com`, kan het `https://relay.example.com` opvragen (vervangend `wss://` door `https://`) om het informatiedocument van de relay op te halen.

Het document gebruikt standaard HTTP content negotiation met de `Accept: application/nostr+json` header. Dit stelt relays in staat om hun normale website aan browsers te serveren terwijl machine-readable metadata aan Nostr clients wordt geboden. Het antwoord omvat relay software naam en versie, operator contactinformatie (pubkey, e-mail, alternatief contact), ondersteunde NIPs en operationele parameters zoals betalingsvereisten of inhoudsbeperkingen.

Belangrijk is dat basisniveau NIP-11-documenten ongesigneerde JSON zijn die via HTTPS worden geserveerd, vertrouwend op TLS-certificaten voor authenticiteit. Dit betekent dat iedereen die de web-server van de relay controleert het document kan wijzigen, waardoor operator claims niet verifieerbaar zijn. Het Trusted Relay Assertions voorstel verhelpt deze hiaat door ondertekende verklaringen via een relay's `self` pubkey veld in te voeren, waardoor cryptografisch bewijs van operator-identiteit mogelijk wordt, vergelijkbaar met hoe relays ondertekende events voor verificatiemechanismen gebruiken.

```json
{
  "name": "relay.example.com",
  "description": "A general-purpose public relay",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
```

Het `limitation` object vertelt clients welke beperkingen de relay handhaaft. `max_message_length` beperkt de WebSocket framegrootte, `max_subscriptions` limiteert gelijktijdige REQ subscripties per verbinding, `max_filters` beperkt filters per REQ, en `max_limit` beperkt hoeveel events een enkele filter kan aanvragen. Deze parameters helpen clients hun gedrag aan relay mogelijkheden aan te passen, waardoor disconnects door limiet overschrijding worden voorkomen.

Betalingsinformatie verschijnt in `fees` en `payments_url`. Relays kunnen in rekening brengen voor toelating (eenmalige toegang), abonnement (terugkerende toegang) of publicatie (per-event fees). De `payments_url` verwijst naar details over betalingsmethoden, meestal Lightning invoices of ecash mints. Betaalde relays gebruiken deze velden om prijzen in te stellen voordat clients proberen zich te authenticeren.

De `supported_nips` array stelt clients in staat relay mogelijkheden te ontdekken. Als een relay [NIP-50](/nl/topics/nip-50/) vermeldt, weten clients dat ze volledige tekstzoekopdrachten kunnen versturen. Als [NIP-42](/nl/topics/nip-42/) verschijnt, moeten clients authenticatieuitdagingen verwachten. Deze declaratieve mogelijkheidsbewaarlegging maakt progressieve verbetering mogelijk: clients kunnen geavanceerde functies waar beschikbaar gebruiken terwijl netjes afglijdend op relays met beperkte ondersteuning.

Operatorinformatie bouwt verantwoording op. Het `pubkey` veld identificeert de relay operator op Nostr, waardoor directe communicatie via [NIP-17](/nl/topics/nip-17/) DMs of publieke vermelding mogelijk wordt. De `contact` e-mail biedt een fallback buiten protocol. Samen helpen deze velden gebruikers operatoren te bereiken voor misbruikrapporten, toegangsaanvragen of technische problemen.

[NIP-11](/nl/topics/nip-11/) documenten zijn zelf-gerapporteerd: relays beschrijven wat ze beweren te ondersteunen, niet noodzakelijk wat ze daadwerkelijk doen. Dit is waar NIP-66 belangrijk wordt.

### [NIP-66](/nl/topics/nip-66/): Relay Discovery en Liveness Monitoring

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) standardiseert het publiceren van relay monitoring data naar Nostr. Monitor services testen relays continu op beschikbaarheid, latentie, protocol compliance en ondersteunde NIPs. Ze publiceren resultaten als kind 30166 events, waarmee real-time relay status onafhankelijk van relay zelf-rapportage wordt geboden.

Monitors controleren relay beschikbaarheid door verbinding te maken en test subscripties te versturen. Latentie metingen volgen connection time, subscription response time en event propagation delay. Protocol compliance testing verifieert dat relay gedrag specificaties aansluit, implementatiebugs of opzettelijke afwijkingen vangend. NIP ondersteuningsverificatie gaat verder dan [NIP-11](/nl/topics/nip-11/) claims door daadwerkelijk te testen of geadverteerde functies correct werken.

```json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\"last_check\": 1736784000, \"checks\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
```

De `d` tag bevat de relay URL, waardoor dit een geparameteriseerde replaceable event is. Elke monitor publiceert één event per relay, bijgewerkt als metingen veranderen. Meerdere monitors kunnen dezelfde relay volgen, waardoor redundantie en cross-validatie worden geboden. Clients bevragen meerdere monitor pubkeys om diverse perspectieven op relay gezondheid te krijgen.

Round-trip time (rtt) tags meten latentie voor verschillende bewerkingen. `rtt open` volgt WebSocket connection establishment, `rtt read` meet subscription response time en `rtt write` test event publicatie snelheid. Alle waarden zijn in milliseconden. Clients gebruiken deze metriek om lage-latentie relays voor tijd-gevoelige bewerkingen te kiezen of trage relays te deprioritiseren.

De `nips` tag somt daadwerkelijk geverifieerde NIP ondersteuning op, niet slechts geclaimde ondersteuning. Monitors testen elke NIP door de functionaliteit uit te oefenen. Als een relay [NIP-50](/nl/topics/nip-50/) zoeken in zijn [NIP-11](/nl/topics/nip-11/) document claimt maar zoekquery's mislukken, zullen monitors NIP-50 uit de geverifieerde lijst weglaten. Dit geeft waarheid over relay mogelijkheden.

Geografische informatie helpt clients nabijgelegen relays te selecteren voor betere latentie en censuurbestendigheid. De `geo` tag bevat landcode, landnaam en regio. De `network` tag onderscheidt clearnet relays van Tor hidden services of I2P endpoints. Samen stellen deze tags geografische diversiteit in: clients kunnen verbinding maken met relays in meerdere jurisdicties om regionale censuur te weerstaan.

Monitor data drijft relay selectors in clients, explorer websites en het Trusted Relay Assertions voorstel. Door zelf-gerapporteerde [NIP-11](/nl/topics/nip-11/) documenten met gemeten [NIP-66](/nl/topics/nip-66/) data en berekende trust assertions te combineren, beweegt het ecosysteem naar geïnformeerde relay selectie in plaats van vertrouwen op hardcoded defaults of mondelinge aanbevelingen.

## Releases

### 0xchat v1.5.3 - Enhanced Messaging Features

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release) brengt significante verbeteringen aan de Telegram-stijl Nostr messaging client. De release behandelt [NIP-55](/nl/topics/nip-55/) (Android signer applicatie) compliance problemen die correct event ondertekening door externe signers zoals Amber verhinderden. Volledige compliance betekent dat 0xchat nu ondertekeningsbewerkingen correct delegeert, waardoor veiligheid wordt verbeterd door private sleutels geïsoleerd te houden.

De update integreert zowel FileDropServer als BlossomServer als standaard media-opslag opties, waardoor gebruikers redundantie voor bestandsuploads krijgen. [Blossom](https://github.com/hzrd149/blossom) biedt content-addressed opslag waar bestanden worden verwezen door hun SHA-256 hashes, waardoor integriteit wordt gegarandeerd en deduplicatie over het netwerk mogelijk wordt. Automatisch concept opslaan voor Moments voorkomt gegevensverlies bij het opstellen van long-form inhoud, wat gebruikersbezwaren over verloren posts bij app switches of connectiviteitsonderbrekingen adresseert.

Cashu wallet integratie krijgt poets met automatisch proof filtering dat uitgegeven tokens uit de wallet view verwijdert. Dit lost de verwarrende UX op waar gebruikers ongeldige bewijzen naast geldige ecash zagen, waardoor balansberekeningen onbetrouwbaar werden. Het filteren gebeurt client-side, waardoor privacy wordt behouden terwijl de betalingservaring voor peer-to-peer transacties in chats wordt verbeterd.

### Amber v4.1.0 Pre-releases - UI Overhaul

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1) tot [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3) introduceren een herontworpen interface voor de populaire Android event signer. Het login scherm toont nu duidelijk welke applicatie handtekeningspermissies aanvraagt, wat gebruikerverwarring over autorisatieflows adresseert. Het nieuwe events scherm biedt gedetailleerde inspectie van welke data applicaties willen ondertekenen, waardoor gebruikers geïnformeerde veiligheidsbeslissingen voordat operaties worden goedgekeurd kunnen nemen.

Permissie beheer ontvangt aanzienlijke aandacht met een vernieuwd interface dat exact toont welke mogelijkheden elke verbonden applicatie is verleend. Gebruikers kunnen specifieke permissies intrekken zonder volledig te verbreken, wat fijnkorrelig controle over ondertekeningsdelegatie inschakelt. De gerefactoriseerde relay tellers met de bijgewerkte quartz library bieden real-time statistieken over event throughput en relay performance. [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) (Nostr Connect) bunker verbindingen oppervlak nu gedetailleerde foutberichten wanneer verbindingen mislukken, vervangend cryptische timeout fouten met handelbare diagnostiek.

## Opmerkelijk code en documentatiewijzigingen

*Dit zijn samengevoegde pull requests en early-stage ontwikkelingen die de moeite waard zijn om te volgen. Sommige zijn experimentele functies die voor release kunnen evolueren.*

### Zeus (Lightning Wallet met Nostr Wallet Connect)

Zeus voegde deze week 17 pull requests samen, versterking van zijn positie als toonaangevende [NIP-47](/nl/topics/nip-47/) Nostr Wallet Connect implementatie. De belangrijkste fixes behandelen data consistency en protocol compliance problemen die interoperabiliteitsproblemen met Nostr clients veroorzaakten.

**Transaction History Fix** - [PR #3542](https://github.com/ZeusLN/zeus/pull/3542) verhelpt een kritieke bug waar NWC transactie lijsten incorrecte of dubbele invoeren toonden. Het probleem ontstond wanneer Zeus transactiegegevens cachede zonder event updates correct af te handelen, waardoor gebruikers fantoomtransacties of ontbrekende betalingen zagen. De fix implementeert correct event deduplicatie en cache invalidatie, waardoor transactiegeschiedenis nauwkeurig de Lightning node status weerspiegelt.

**Protocol Compliance** - [PR #3548](https://github.com/ZeusLN/zeus/pull/3548) adresseert onvolledige `getInfo` reacties die compatibiliteit met clients verwachting volledige NIP-47 compliance verbraken. Sommige Nostr clients crashten wanneer ontvangende partiële reacties velden misten zoals `block_height` of `network`. De PR zorgt ervoor dat alle vereiste velden met zinvolle defaults terugkeren zelfs wanneer de onderliggende Lightning implementatie ze niet biedt, waardoor Zeus's compatibiliteit over het ecosysteem wordt verbeterd.

**Connection Resilience** - [PR #3543](https://github.com/ZeusLN/zeus/pull/3543) implementeert timeout notificaties voor stalemate Nostr verbindingen. Eerder wachtten gebruikers onbepaald wanneer relay verbindingen stierf. Nu toont Zeus duidelijke timeout berichten na 30 seconden inactiviteit, waardoor gebruikers kunnen herproberen of relays kunnen wisselen. [PR #3541](https://github.com/ZeusLN/zeus/pull/3541) voegt backend validatie toe om NWC activatie op incompatibele Lightning implementaties te voorkomen, configuratiefouten vangend voordat ze runtime crashes veroorzaken.

**Cashu Race Condition** - [PR #3531](https://github.com/ZeusLN/zeus/pull/3531) verhelpt een concurrency bug in Cashu token beheer waar gelijktijdige mint operaties de token database konden corrupteren. De race condition ontstond wanneer meerdere threads token counts bijwerkten zonder correct locking, occasioneel resulterende in incorrecte balansen. De fix voegt mutex bescherming rond kritieke secties toe, waarmee atomaire updates naar token state worden gegarandeerd.

### Primal Android (Client)

Primal Android verzond 12 samengevoegde PRs met significante verbeteringen aan wallet veiligheid en mediaafhandeling. De wallet backup implementatie adresseert één van de meest aangevraagde functies, terwijl NIP-92 ondersteuning de visuele ervaring over de applicatie verbetert.

**Wallet Backup System** - Een vier-PR serie ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848)) implementeert uitgebreide seed phrase backup functionaliteit. Gebruikers kunnen nu hun 12-woord mnemonic via een veilige flow exporteren die screenshots voorkomt, backup status in het wallet dashboard toont, en bestaande gebruikers door migratie begeleidt. De implementatie volgt BIP-39 standaarden en omvat validatie om gebruikers van fondsen verlies door incorrect phrase opname te voorkomen.

**Media Dimensions (NIP-92)** - [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) implementeert [NIP-92](/nl/topics/nip-92/) ondersteuning voor correcte afbeelding en video beeldverhoudingen. Zonder dimensie metadata moeten clients afbeeldingen downloaden om hun grootte te bepalen, waardoor layout jumps ontstaan als inhoud laadt. NIP-92 voegt `dim` tags toe (zoals `["dim", "1920x1080"]`) naar bestandsmetadata events, waardoor Primal correcte ruimte kan reserveren voordat media wordt gedownload. Dit elimineert jarring reflows in afbeeldinggalerijen en verbetert waargenomen prestaties.

**Remote Signer Reliability** - [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841) verhelpt [NIP-46](/nl/topics/nip-46/) verbindingsproblemen waar ontbrekende `wss://` voorvoegsels stille fouten veroorzaakten. De PR valideert relay URIs tijdens bunker verbinding setup, automatisch het protocol voorvoegsel toevoegend wanneer gebruikers bare domeinen plakken. [PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843) adresseert een threading bug waar slechte netwerkcondities replies als root notes veroorzaakten, conversatie flow brekend. De fix zorgt ervoor dat parent event IDs door netwerkonderbrekingen heen persistent blijven.

### Marmot Protocol: White Noise (Encrypted Group Chat Library)

White Noise, de Rust library die [Marmot](/nl/topics/marmot/) Protocol's versleutelde groepsgesprekken aandrijft, voegde zes PRs samen die gebruikerservaring en veiligheid verbeteren. De wijzigingen brengen Marmot dichter naar feature pariteit met mainstream messaging applicaties terwijl de privacy-first architectuur behouden blíjft.

**Read Receipts** - [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) en [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436) implementeren message read tracking voor groepsgesprekken. Het systeem slaat read posities per gebruiker per groep binnen een enkel device op, waardoor unread count badges worden ingeschakeld. De implementatie gebruikt monotone timestamps om de laatste gelezen berichtpositie voor elk gesprek bij te volgen. Deze basisfeature maakt UI indicatoren die unread berichtaantallen per gesprek tonen mogelijk.

**Conversation Pinning** - [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442) voegt persistent conversation pinning toe via een `pin_order` veld in de `accounts_groups` junction table die accounts met groepen verbindt. Vastgezette gesprekken behouden hun positie bovenaan chatlijsten ongeacht berichtactiviteit, wat gebruikersverwachtingen uit Signal en WhatsApp aansluit. De implementatie gebruikt integer ordering om onbeperkte pins met deterministische sortering toe te staan.

**Deterministic Commit Resolution (MIP-03)** - [PR #152](https://github.com/marmot-protocol/mdk/pull/152) (open) implementeert Marmot Improvement Proposal 03, het kritieke probleem van commit race conditions in gedistribueerde groepsgesprekken oplossend. Wanneer meerdere leden groeps-state wijzigingen (leden toevoegen/verwijderen, permissies wijzigen) gelijktijdig indienen, konden clients op commit volgorde divergeren, de groep in incompatibele states fragmentering. MIP-03 introduceert epoch snapshots en deterministische winnerselectie: de commit met de vroegste `created_at` timestamp wint, met lexicografische event ID als tiebreaker. Dit stelt alle clients in staat op dezelfde state te convergen door rollback en replay, groep coherentie zelfs tijdens netwerkpartities behoudend.

**Security Hardening** - [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443) voorkomt onnodige copying van cryptografische secrets door verwijzingen in `resolve_group_image_path` te gebruiken. Dit beperkt het raam voor geheugen-aanvallen waarbij secrets van bevrijde heap allocaties kunnen worden hersteld. [PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438) maakt SQLCipher database versleuteling via keyring parameters mogelijk, berichtgeschiedenis in rust beschermend. De keyring integratie maakt veilige sleutelopslag in platform keychains in plaats van configuratiebestanden mogelijk.

### nostrdb-rs (Database Library) - Open PR

**Streaming Queries Implementation** - [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58) (open) stelt streaming fold queries voor om zero-allocation databasebewerkingen mogelijk te maken. De implementatie voegt `fold`, `try_fold`, `count`, `any`, `all` en `find_map` methoden toe die database resultaten één tegelijk zouden verwerken zonder gehele result sets in vectors te materializeren. Deze benadering zou geheugenverbruik verminderen en vroege beëindiging voor veelvoorkomende query patterns inschakelen.

De technische implementatie stelt low-level query result callbacks (`ndb_query_visit`) bloot als stateful Rust visitors die `ControlFlow` varianten naar C visitor acties kaarten. Eenmaal samengevoegd zal toepassingscode lezen als iterator logica terwijl dicht bij de databaselaag wordt uitgevoerd. Bijvoorbeeld, het tellen van overeenkomende notes zou resultaten streamen in plaats van ze te verzamelen, en `find_map` zou het eerste nuttige resultaat terugkeren zonder resterende rijen te verwerken.

nostrdb drijft Damus en Notedeck aan, beide iOS/macOS en desktop clients respectievelijk. De streaming queries zouden efficiënte patronen zoals paginering, voorwaardelijk filteren en bestaan checks mogelijk maken. De PR wijzigt 3 bestanden met +756 toevoegingen en -32 deletions, een aanzienlijke refactoring van de query laag. Gebruikers van nostrdb-rs-gebaseerde applicaties zouden verminderd geheugengebruik zien bij het bladeren van grote timelines of zoeken door uitgebreide event databases.

### nak (CLI Tool)

nak, fiatjaf's command-line Nostr tool, voegde zes PRs samen gericht op build system verbeteringen en nieuwe functionaliteit. [PR #91](https://github.com/fiatjaf/nak/pull/91) implementeert een Blossom mirror feature, waardoor nak als mirror voor Blossom media servers kan dienen. [Blossom](/nl/topics/blossom/) is een content-addressed media storage protocol die naast Nostr events werkt.

De resterende PRs behandelen build system compatibiliteit over Windows, macOS en Linux platforms, FUSE filesystem ondersteuning voor het mounten van Nostr events als lokale directories inschakeled.

### Damus (iOS Client) - Open PRs

Damus heeft 11 open PRs die significante architecturale verbeteringen verkennen. Terwijl deze nog niet zijn samengevoegd, signaleren zij belangrijke richtingen voor iOS Nostr client ontwikkeling, bijzonder rond privacy, synchronisatie efficiëntie en mobiele data optimalisatie.

**Tor Integration** - [PR #3535](https://github.com/damus-io/damus/pull/3535) bedraait de Arti Tor client rechtstreeks in Damus, anonieme relay verbindingen zonder externe afhankelijkheden mogelijk makend. Anders dan Orbot of Tor Browser benaderingen, bedraait Arti naadloze integratie met iOS sandboxing en background executie limieten. De Rust implementatie brengt geheugenveiliigheid naar netwerkveranonimisering, aanvalsoppervlakte reducerend vergeleken met C Tor. Gebruikers konden Tor mode per-relay of globaal inschakelen, met de client circuit beheer transparant handafnd.

**Negentropy Sync Protocol** - [PR #3536](https://github.com/damus-io/damus/pull/3536) implementeert Negentropy, een set reconciliation protocol die synchronisatie efficiëntie radicaal verbetert. In plaats van alle events sinds laatste verbinding te downloaden, wisselt Negentropy compacte fingerprints (Merkle trees) uit om exact welke events tussen client en relay verschillen te identificeren. Voor gebruikers die honderden pubkeys volgen, beperkt dit sync bandbreedte van megabytes tot kilobytes. De implementatie integreert met RelayPool en SubscriptionManager, efficïente sync over alle verbonden relays automatisch inschakeld.

**Low Data Mode** - [PR #3549](https://github.com/damus-io/damus/pull/3549) voegt mobiel data besparingsfuncties toe die antwoorden op gebruikersfeedback over bandbreedte verbruik. De mode schakelt automatisch afbeeldingladen uit, video prefetching en beperkt subscription limieten. Gebruikers op gemeten verbindingen kunnen tekstinhoud bladeren zonder angst voor gegevenslimieten te overschrijden. De implementatie respecteert iOS low data mode instellingen en biedt granulaire controles voor verschillende media types.

**Database Optimizations** - [PR #3548](https://github.com/damus-io/damus/pull/3548) herziet nostrdb snapshot opslag voor snellere queries en verminderd diskgebruik. De optimalisatie wijzigt hoe database snapshots naar schijf persistent, waardoor zowel read performance als write amplification worden verbeterd. Dit adresseert batterij drain klachten van gebruikers met grote event databases.

---

Dat is het voor deze week. Bouw je iets? Nieuws om te delen? Wil je dat we je project behandelen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Bereik ons via NIP-17 DM</a> of vind ons op Nostr.
