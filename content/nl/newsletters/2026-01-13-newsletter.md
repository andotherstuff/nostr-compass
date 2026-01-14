---
title: 'Nostr Compass #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** Bitchat ondergaat een professionele beveiligingsaudit door Cure53, hetzelfde bedrijf dat Signal en [NIP-44](/nl/topics/nip-44/) heeft geauditeerd, met inmiddels 17+ PR's gemerged die kritieke bevindingen oplossen. [NIP-71](/nl/topics/nip-71/) is gemerged en brengt adresseerbare video events naar het protocol. Een post-quantum cryptografie NIP opent discussie over het toekomstbestendig maken van Nostr tegen quantum-aanvallen. Amethyst v1.05.0 bevat bladwijzerlijsten, spraaknotities en een vroege desktoprelease, terwijl Nostur v1.25.3 [NIP-17](/nl/topics/nip-17/) DM's verbetert met reacties en antwoorden. In bibliotheeknieuws breidt rust-nostr [NIP-62](/nl/topics/nip-62/) ondersteuning uit naar SQLite en LMDB backends, en lost NDK een bug in subscription tracking op.

## Nieuws

### Bitchat Voltooit Cure53 Beveiligingsaudit

Bitchat, de iOS versleutelde messenger die Nostr combineert met Cashu, heeft een professionele beveiligingsaudit ondergaan door Cure53, een van de meest gerespecteerde beveiligingsbedrijven in de industrie. Cure53 heeft eerder Signal, Mullvad VPN, en met name de [NIP-44](/nl/topics/nip-44/) encryptiespecificatie geauditeerd die de basis vormt voor moderne Nostr privéberichten.

De audit vond 12+ beveiligingsproblemen (BCH-01-002 tot en met BCH-01-013). Het Bitchat-team reageerde met 17+ pull requests. Belangrijke fixes zijn:

**Noise Protocol DH Secret Clearing** - [PR #928](https://github.com/permissionlesstech/bitchat/pull/928) lost zes locaties op waar Diffie-Hellman gedeelde geheimen niet werden gewist na key agreement, waardoor forward secrecy garanties worden hersteld. Wanneer geheimen langer dan nodig in het geheugen blijven, kan een memory dump of cold boot aanval eerdere communicatie compromitteren.

**Handtekeningverificatie** - Meerdere PR's versterken cryptografische verificatiepaden, zodat authenticiteitscontroles van berichten niet kunnen worden omzeild door misvormde invoer.

**Thread Safety** - [PR #929](https://github.com/permissionlesstech/bitchat/pull/929) voegt barrieresynchronisatie toe aan leesbevestigingswachtrijen in NostrTransport, waardoor race conditions worden voorkomen die datacorruptie of crashes kunnen veroorzaken bij hoge berichtvolumes.

**Memory Safety** - [PR #920](https://github.com/permissionlesstech/bitchat/pull/920) optimaliseert de berichtdeduplicator voor betere prestaties bij hoge berichtdoorvoer terwijl geheugenuitputting wordt vermeden.

**Invoervalidatie** - [PR #919](https://github.com/permissionlesstech/bitchat/pull/919) versterkt hex-stringparsing om crashes door misvormde invoer te voorkomen, een veelvoorkomende aanvalsvector voor denial-of-service.

Bitchat verwerkt Cashu ecash, waardoor professionele beveiligingsbeoordeling essentieel is. De audit volgt op de [Marmot](/nl/topics/marmot/) Protocol-audit van vorig jaar en de NIP-44-audit die de encryptielaag verifieerde.

## NIP Updates

Recente wijzigingen aan de [NIPs repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-71](/nl/topics/nip-71/)** - Adresseerbare Video Events ([#1669](https://github.com/nostr-protocol/nips/pull/1669)) introduceert kinds 34235 (horizontale video) en 34236 (verticale video) als adresseerbare events. Een vereiste `d` tag biedt unieke identificatoren, zodat videometadata kan worden bijgewerkt zonder het hele event opnieuw te publiceren. Een optionele `origin` tag houdt importbronnen bij. Al geïmplementeerd in Amethyst en nostrvine.

**Open PR's:**

- **Post-Quantum Cryptografie** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) stelt voor om kwantumbestendige cryptografische algoritmen aan Nostr toe te voegen. De specificatie introduceert ML-DSA-44 en Falcon-512 voor digitale handtekeningen, gericht op "super-high value events" zoals applicaties en autoriteiten in plaats van individuele gebruikers. Hoewel de symmetrische encryptie van [NIP-44](/nl/topics/nip-44/) (ChaCha20) kwantumbestendig is, gebruikt de key exchange secp256k1 ECDH wat kwetsbaar is voor Shor's algoritme. Het voorstel bevat ML-KEM voor key agreement om deze kloof te dichten. Dit is een vroeg voorstel dat discussie opent over crypto-agiliteit voor de langetermijnbeveiliging van Nostr.
- **BOLT12 voor NIP-47** - Na 137 reacties en uitgebreide discussie besloot de gemeenschap dat BOLT12 offers hun eigen specificatie verdienen in plaats van [NIP-47](/nl/topics/nip-47/) uit te breiden. BOLT12 offers bieden aanzienlijke upgrades ten opzichte van BOLT11 invoices, waaronder herbruikbaarheid, betere privacy door blinded paths, en optionele betalersinformatie. De nieuwe NIP zal methodes definiëren zoals `make_offer`, `pay_offer`, en `list_offers` voor Nostr Wallet Connect implementaties.
- **Audio Track NIP** - [PR #1043](https://github.com/nostr-protocol/nips/pull/1043) stelt kinds 32100 voor muzieknummers en 32101 voor podcast-afleveringen voor, waardoor audiocontent dezelfde eersteklas behandeling krijgt die NIP-71 biedt voor video. Momenteel gebruiken audioplatformen zoals Wavlake, Zapstr en Stemstr elk eigen event-formaten, wat het ecosysteem fragmenteert. Een gemeenschappelijke standaard zou interoperabiliteit mogelijk maken zodat gebruikers audio kunnen ontdekken en afspelen vanuit elke compatibele client.
- **NIP-A3 Universele Betalingsdoelen** - [PR #2119](https://github.com/nostr-protocol/nips/pull/2119) stelt kind 10133 events voor die RFC-8905 `payto:`-URI's gebruiken om betalingsopties beschikbaar te stellen over meerdere netwerken. In plaats van aparte event kinds te maken voor Bitcoin, Lightning, Cashu, of traditionele betalingssystemen, laat deze abstractie clients gestandaardiseerde tags parsen en native betalingshandlers aanroepen. De aanpak is toekomstbestendig omdat nieuwe betaalmethoden alleen een `payto:`-URI-schema nodig hebben.

## NIP Diepgaand: NIP-51 en NIP-65

Deze week behandelen we twee NIP's die gebruikersvoorkeuren opslaan: NIP-51 voor het organiseren van content, en NIP-65 voor het organiseren van relay-verbindingen. Beide gebruiken vervangbare events, wat betekent dat elke nieuwe publicatie de vorige versie overschrijft.

### [NIP-51](/nl/topics/nip-51/): Lijsten

[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) definieert meerdere lijsttypen voor het organiseren van verwijzingen naar events, gebruikers, hashtags en andere content. Amethyst v1.05.0 voegt bladwijzerondersteuning toe, waardoor dit een goed moment is om te begrijpen hoe lijsten werken.

De spec definieert verschillende list kinds, elk met een ander doel. Kind 10000 is je dempenlijst voor het verbergen van gebruikers, threads of woorden. Kind 10001 pint events om uit te lichten op je profiel. Kind 30003 slaat bladwijzers op, wat Amethyst nu ondersteunt. Andere kinds behandelen follow sets (30000), gecureerde artikelcollecties (30004), hashtag-interesses (30015), en aangepaste emoji sets (30030).

Lijsten verwijzen naar content via tags. Een bladwijzerlijst gebruikt `e` tags voor specifieke events en `a` tags voor adresseerbare content zoals artikelen:

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

De `d` tag biedt een unieke identificator, zodat je meerdere bladwijzersets kunt onderhouden zoals "saved-articles", "read-later" of "favorites" onder dezelfde kind.

Lijsten ondersteunen zowel openbare als privé-items. Openbare items verschijnen in de tags-array, zichtbaar voor iedereen die het event ophaalt. Privé-items gaan in het `content`-veld, versleuteld met [NIP-44](/nl/topics/nip-44/) naar jezelf. Deze dubbele structuur laat je openbare bladwijzers bijhouden terwijl je privénotities toevoegt, of een dempenlijst onderhouden zonder te onthullen wie je hebt gedempt. Om naar jezelf te versleutelen, gebruik NIP-44 met je eigen pubkey als ontvanger.

De 10000-serie kinds zijn vervangbaar, wat betekent dat relays slechts een event per pubkey bewaren. De 30000-serie zijn geparametriseerd vervangbaar, waardoor een event per pubkey en `d`-tagcombinatie mogelijk is. In beide gevallen betekent het bijwerken van een lijst het publiceren van een complete vervanging; je kunt geen incrementele wijzigingen sturen. Clients moeten onbekende tags behouden bij het wijzigen van lijsten om te voorkomen dat data wordt overschreven die door andere applicaties is toegevoegd.

### [NIP-65](/nl/topics/nip-65/): Relay Lijst Metadata

[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) definieert kind 10002 events die adverteren welke relays een gebruiker prefereert voor lezen en schrijven. Dit helpt andere gebruikers en clients je content te vinden.

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

Elke `r` tag bevat een relay URL en een optionele marker. Een `write` marker wijst je outbox aan: relays waar je je content publiceert. Een `read` marker wijst je inbox aan: relays waar je controleert op vermeldingen, antwoorden en tags. Het weglaten van de marker betekent beide.

Wanneer Alice Bob's berichten wil vinden, haalt haar client Bob's kind 10002 op, extraheert zijn write relays (zijn outbox), en abonneert zich daar. Wanneer Alice op Bob reageert, publiceert haar client naar zijn read relays (zijn inbox) zodat hij de vermelding ziet. Deze relay-bewuste routering is het "outbox model," en het verdeelt gebruikers over veel relays in plaats van iedereen te concentreren op een paar centrale servers.

NIP-65 handelt routering van openbare content af, maar privéberichten gebruiken een aparte lijst. [NIP-17](/nl/topics/nip-17/) definieert kind 10050 voor DM inbox relays, met `relay` tags in plaats van `r` tags. Bij het versturen van een privébericht aan iemand, zoeken clients naar het kind 10050 event van de ontvanger en publiceren het versleutelde gift-wrapped bericht daar. Deze scheiding houdt DM-routering gescheiden van openbare content routering, en laat gebruikers verschillende relays specificeren voor privé versus openbare communicatie.

Het outbox-model verbetert censuurbestendigheid omdat geen enkele relay ieders content hoeft op te slaan of te serveren. Clients onderhouden verbindingen met relays die vermeld staan in de NIP-65-events van hun gevolgde gebruikers, en verbinden dynamisch met nieuwe relays naarmate ze nieuwe accounts ontdekken. NIP-65 complementeert de relay-hints in andere NIP's. Wanneer je iemand tagt met `["p", "pubkey", "wss://hint.relay"]`, vertelt de hint clients waar ze moeten zoeken naar die specifieke verwijzing. NIP-65 biedt de gezaghebbende, door de gebruiker beheerde lijst, terwijl hints snelkoppelingen bieden ingebed in individuele events.

Voor de beste resultaten, houd je relaylijst actueel aangezien verouderde vermeldingen je moeilijker vindbaar maken. De specificatie raadt twee tot vier relays per categorie aan. Te veel relays vermelden belast elke client die je content wil ophalen, vertraagt hun ervaring en verhoogt netwerkbelasting. Clients cachen NIP-65-events en vernieuwen ze periodiek om actueel te blijven wanneer gebruikers hun voorkeuren bijwerken.

## Releases

**Amethyst v1.05.0** - De populaire Android-client [brengt een grote update uit](https://github.com/vitorpamplona/amethyst/releases) met verschillende hoofdfuncties. [NIP-51](/nl/topics/nip-51/) kind 30003 bladwijzerlijsten laten gebruikers berichten opslaan voor latere referentie, synchroon over compatibele clients. Spraaknotities werken nu in DM's en reguliere berichten met golfvormvisualisatie, mediaserverselectie en uploadvoortgangsindicatoren. [Web of Trust](/nl/topics/web-of-trust/)-scores zijn nu zichtbaar in de interface, waardoor gebruikers kunnen begrijpen hoe het algoritme accounts evalueert ten opzichte van hun sociale grafiek. De [Quartz](/nl/topics/quartz/)-databasemigratie verbetert queryprestaties als onderdeel van het OpenSats-gefinancierde Kotlin Multiplatform-werk. Een vroege desktoprelease brengt Amethyst naar Windows, macOS en Linux via Compose Multiplatform, met dezelfde codebase als de Android-app. Nieuwe gebruikers-onboardingflows versoepelen de ervaring voor eerste Nostr-gebruikers.

**Nostur v1.25.3** - De iOS- en macOS-client [focust op privéberichten](https://github.com/nostur-com/nostur-ios-public/releases) met [NIP-17](/nl/topics/nip-17/)-verbeteringen. DM-gesprekken ondersteunen nu reacties en antwoorden, waardoor de interactiviteit van openbare berichten in versleutelde berichten komt. De gespreksweergave is herwerkt met betere threading zodat uitwisselingen van meerdere berichten makkelijker te volgen zijn, en tijdstempels tonen "tijd geleden" in de DM-lijst voor snel scannen. Desktopgebruikers krijgen multi-kolomlayouts voor het bekijken van meerdere feeds of gesprekken naast elkaar. [NIP-46](/nl/topics/nip-46/) remote signer-ondersteuning stelt gebruikers in staat hun private keys in speciale signer-apps te houden zoals Amber of nsec.app. Aanvullende fixes herstellen DM-functionaliteit op iOS 15 en iOS 16, lossen notificatievertragingen op, en voegen de mogelijkheid toe om te configureren welke relays gepubliceerde DM's ontvangen.

## Opmerkelijke code- en documentatiewijzigingen

*Dit zijn open pull requests en werk in een vroeg stadium, perfect om feedback te krijgen voordat ze worden gemerged. Als iets je aandacht trekt, overweeg dan te reviewen of commentaar te geven!*

### Citrine (Android Relay)

[PR #89](https://github.com/greenart7c3/Citrine/pull/89) lost een SQL-injectiekwetsbaarheid op in de persoonlijke Android-relayapp. Het probleem stond toe dat misvormde eventdata willekeurige databasequeries kon uitvoeren, een ernstige fout voor elke app die onbetrouwbare invoer opslaat en verwerkt. De fix sanitiseert alle databaseoperaties correct met geparametriseerde queries. Er is nog geen release getagd, dus gebruikers moeten wachten op de volgende versie of bouwen vanaf broncode. [PR #90](https://github.com/greenart7c3/Citrine/pull/90) optimaliseert ContentProvider-queryprestaties met filtering en paginering op databaseniveau, wat latentie vermindert wanneer externe apps zoals Amethyst toegang krijgen tot Citrine's eventdatabase via Android's inter-process communicatielaag.

### rust-nostr (Library)

[NIP-62](/nl/topics/nip-62/) (Vanish Requests)-ondersteuning breidt uit over rust-nostr's database-backends. [PR #1180](https://github.com/rust-nostr/nostr/pull/1180), twee weken geleden gemerged, voegde NIP-62-ondersteuning toe aan SQLite, en handelt `ALL_RELAYS` vanish requests af aangezien de databaselaag geen specifieke relay-URL's kent. [PR #1210](https://github.com/rust-nostr/nostr/pull/1210) breidt dit uit naar de LMDB-backend, wat ervoor zorgt dat vanish requests naar schijf worden opgeslagen en relay-herstarts overleven. Een IndexedDB-implementatie voor browseromgevingen is ook in ontwikkeling. Samen geven deze wijzigingen ontwikkelaars consistente NIP-62-ondersteuning over SQLite, LMDB, en binnenkort browseropslag.

### NDK (Nostr Development Kit)

[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) lost een bug op in het seenEvents-trackingsysteem. Het probleem zorgde ervoor dat bepaalde subscriptionpatronen events incorrect als al gezien markeerden, wat leidde tot gemiste content wanneer gebruikers nieuwe subscriptions openden of opnieuw verbonden met relays. De fix zorgt ervoor dat events nauwkeurig worden gevolgd over subscription-lifecycles, wat bijzonder belangrijk is voor applicaties die dynamisch subscriben en unsubscriben op basis van gebruikersnavigatie. NDK is opgehoogd naar beta.70 met deze fix inbegrepen.

### Damus (iOS)

[PR #3515](https://github.com/damus-io/damus/pull/3515) lost een opstartcrash op die iOS 17-gebruikers treft. Het probleem kwam voort uit een rekenkundige overflow in `NdbUseLock`, een fallbackklasse die wordt gebruikt omdat Swift Mutexes niet beschikbaar zijn op iOS 17. De fix vervangt de vorige synchronisatieaanpak met `NSLock`, die wel beschikbaar is op iOS 17 en de resterende race conditions correct afhandelt. iOS 18+-gebruikers waren niet getroffen omdat zij toegang hebben tot de native Swift Mutex-implementatie.

Afzonderlijk landde een batch longform-artikelverbeteringen via [PR #3509](https://github.com/damus-io/damus/pull/3509). Leesvoortgangsbalken volgen je positie door artikelen, geschatte leestijden verschijnen op previews, en sepiamodus met instelbare regelhoogte-instellingen bieden comfortabeler lezen. Focusmodus verbergt automatisch de navigatiechrome bij naar beneden scrollen en herstelt het bij tikken, wat visuele rommel vermindert voor afleidingsvrij lezen. Verschillende fixes pakken beeldweergave in markdowncontent aan en zorgen ervoor dat artikelen bovenaan openen in plaats van halverwege.

### Zap.stream (Live Streaming)

YouTube- en Kick-chatintegratie verbindt berichten van externe streamingplatformen met Nostr. Streamers die naar YouTube, Kick en Zap.stream multicasten kunnen nu alle chatberichten in een uniforme weergave zien, met berichten van elk platform naast native Nostr-reacties. Dit verwijdert een groot wrijvingspunt voor creators die Nostr willen gebruiken voor streaming maar hun publiek op gevestigde platformen niet kunnen verlaten. De integratie toont van welk platform elk bericht afkomstig is en handelt de authenticatiestroom af voor het verbinden van externe accounts.

### Chachi (NIP-29 Groups)

De [NIP-29](/nl/topics/nip-29/) groepschatclient heeft deze week zes gemergede PR's verscheept. Een beveiligingsupdate adresseert [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89), een XSS-kwetsbaarheid in react-router die open redirect-aanvallen mogelijk kon maken; de fix updatet naar react-router-dom 6.30.0. [PR #92](https://github.com/purrgrammer/chachi/pull/92) voegt gepagineerd berichten laden toe voor groepschats, zodat lange gesprekken incrementeel laden in plaats van allemaal tegelijk. [PR #91](https://github.com/purrgrammer/chachi/pull/91) lost verschillende NIP-29-bugs op waaronder een race condition die lege groepsnamen veroorzaakte bij initieel laden en undefined deelnemerslijsten die ledenweergaven lieten crashen. Vertalingsdekking beslaat nu alle 31 ondersteunde talen met elk 1060 keys.

### 0xchat (Messaging)

De Telegram-stijl messagingclient verbeterde [NIP-55](/nl/topics/nip-55/)-compliance door signer package names correct op te slaan bij gebruik van externe signing-apps, wat problemen oploste waarbij de app vergat welke signer te gebruiken na herstarts. NIP-17-antwoordafhandeling bevat nu correct de `e`-tag voor threading, wat ervoor zorgt dat antwoorden in de juiste gesprekscontext verschijnen over clients heen. Prestatieoptimalisaties pakken scroll-lag aan in berichtlijsten, een veelvoorkomend pijnpunt bij het laden van lange chatgeschiedenissen. Concept-auto-save voorkomt berichtverlies als je wegnavigeert tijdens het opstellen, en bestandsopslagopties bevatten nu standaard FileDropServer- en BlossomServer-endpoints.

### Primal (iOS)

[NIP-46](/nl/topics/nip-46/) remote signer-ondersteuning landt op iOS via [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184), wat de cross-platform uitrol voltooit die enkele weken geleden begon met Android. Gebruikers kunnen nu hun private keys bewaren in speciale bunkerservices zoals nsec.app of zelf-gehoste nsecBunker-instances, verbindend over Nostr-relays om events te ondertekenen zonder keys bloot te stellen aan de client-app. Deze scheiding verbetert de beveiligingspositie voor gebruikers die Primal's functies willen gebruiken terwijl ze strengere key management-praktijken handhaven. De implementatie bevat QR-codescannen voor bunkerverbindings-URI's en handelt de NIP-46 request/response-flow af over versleutelde relayberichten.

---

Dat was het voor deze week. Bouw je iets? Heb je nieuws te delen? Wil je dat we je project behandelen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via NIP-17 DM</a> of vind ons op Nostr.
