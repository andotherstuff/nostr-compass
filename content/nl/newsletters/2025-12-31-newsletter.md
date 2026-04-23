---
title: 'Nostr Kompas #3'
date: 2025-12-31
publishDate: 2025-12-31
draft: false
type: newsletters
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2026-04-23
---

Welkom terug bij Nostr Kompas, je wekelijkse gids voor het Nostr-protocol ecosysteem.

**Deze week:** Terwijl 2025 eindigt, kijken we terug op vijf jaar decembermilepalen in Nostr's evolutie. Van fiatjaf's eerste clientrelease in december 2020, via Jack Dorsey's pivotale donatie van 14 BTC in december 2022, tot deze maand's verspreiding van NIP-55-signers en NDK's 162x cacheversnelling, heeft december consistente keerpunten voor het protocol gemarkeerd. Dit speciale nummer volgt de technische geschiedenis door elke december, documenterend de groei van het protocol van twee experimentele relays naar 2.500+ nodes over 50 landen. Plus: het desktopmodule van Amethyst krijgt vorm via Quartz, Notedeck voegt berichten toe, Citrine host webapps, en NIP-54 lost internationalisatie voor niet-Latijnse scripts op.

## December Recap: Vijf jaar Nostr-decembers

Nostr wordt dit jaar vijf jaar oud. fiatjaf initieerde het protocol op 7 november 2020, en elke december sinds dien heeft een distinct fase in zijn evolutie gemarkeerd: van proof-of-concept naar mondiale beweging naar production-ecosysteem. Dit is een technische terugblik van december 2020 tot en met december 2025, de vormende jaren die Nostr's grondslag hebben gevestigd en zijn doorbraakmoment hebben gekatalyseerd.

### December 2020: Genesis

De eerste volledige maand van Nostr's bestaan zag fiatjaf [Branle](https://github.com/fiatjaf/branle) vrijgeven, de eerste client van het protocol, gebouwd met Quasar (Vue.js) en absurd-sql voor lokale opslag. fiatjaf had al de kernarchitectuur vastgesteld: gebruikers geïdentificeerd door secp256k1 publieke sleutels, alle berichten cryptografisch ondertekend, relays als domme opslag die niet met elkaar communiceren. Een of twee experimentele relays dienden een handvol early adopters die coördineerden in de Telegram-groep [@nostr_protocol](https://t.me/nostr_protocol), die op 16 november was gestart. De [originele documentatie](https://fiatjaf.com/nostr.html) beschreef "het eenvoudigste open protocol dat in staat is om een censuurbestendige wereldwijd sociaal netwerk te creëren," een premise die twee jaar later zou worden bewezen.

### December 2021: Vroege ontwikkeling

Op 31 december 2021 haalde Nostr de [Hacker News voorpagina](https://news.ycombinator.com/item?id=29749061) met 110 punten en 138 opmerkingen, ingediend door Cameri. Dit markeerde de eerste significante blootstelling van het protocol aan de bredere developer-community. Het netwerk liep op ongeveer zeven relays met minder dan 1.000 gebruikers. Branle ontving updates inclusief private key import (31 december) en multi-relay ondersteuning. Een command-line client, noscl, voorzag terminal-gebaseerde interactie. De protocol-specificaties bestonden in fiatjaf's documentatie, hoewel de formele [NIPs-repository](https://github.com/nostr-protocol/nips) niet tot mei 2022 zou worden aangemaakt. Het protocol was, zoals fiatjaf het beschreef, "work in progress".

### December 2022: Het omslagpunt

December 2022 veranderde Nostr van een niche experiment in een mainstream beweging. De katalysator kwam op 15 december, toen Jack Dorsey [14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding) (~$245.000-$250.000) aan fiatjaf doneerde nadat hij het protocol ontdekte en het "100 procent wat we van Bluesky wilden, maar het was niet van een bedrijf ontwikkeld" noemde. Op 16 december kondigde fiatjaf aan dat hij middelen zou verdelen met Damus-ontwikkelaar William Casarin (jb55), en Dorsey verificeerde zijn Nostr-account (npub: `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`). De financiering legitimeerde het project in één nacht.

Dezelfde week versnelde Twitter's chaos de adoptie. 14-15 december zagen schorsingen van prominente journalisten van de New York Times, CNN en Washington Post. Op 18 december [kondigde Twitter verboden aan](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) op accounts die Nostr, Mastodon en andere platforms bevorderden. Het beleid werd de volgende dag na tegenkanting omgekeerd. De exodus dreef gebruikers om alternatieven te verkennen.

Protocol-ontwikkeling nam toe. Op 16 december werd [NIP-19](/nl/topics/nip-19/) gemerged ([#57](https://github.com/nostr-protocol/nips/pull/57)), introductie van bech32-gecodeerde identificatoren (npub, nsec, note, nprofile, nevent) die sleutels mensleesbaar en onderscheidbaar maakten. De NIPs-repository registreerde 36+ commits die maand, inclusief NIP-40 en NIP-07 updates. Clients vermenigvuldigden zich: Damus vulde zijn TestFlight-bèta binnen uren, Astral forkte Branle voor profielbepaling, Snort lanceerde als een "snelle, censuurbestendige" webclient, en Vitor Pamplona begon Amethyst-ontwikkeling. Alby v1.22.1 "Kemble's Cascade of Stars" werd op 22 december verscheept met NIP-19 ondersteuning. Op 7 december had Nostr ongeveer 800 gebruikers met profielen; toen Damus op 31 januari 2023 de App Store raakte, gingen de sluizen open, groei naar 315.000+ gebruikers tegen juni 2023.

### December 2023: Ecosysteem volwassenheid

December 2023 markeerde een kritisch keerpunt voor Nostr-protocolbeveiliging. Op 20 december werd [NIP-44 revisie 3 gemerged](https://github.com/nostr-protocol/nips/pull/746) na een onafhankelijke Cure53-beveiligingsaudit (NOS-01) die 10 problemen in TypeScript-, Go- en Rust-implementaties identificeerde, inclusief timing-aanvallen en forward-secrecy-zorgen. De bijgewerkte spec verving de gebrekkige [NIP-04](/nl/topics/nip-04/) versleuteling met ChaCha20 en HMAC-SHA256, waarbij de cryptografische basis werd vastgesteld die nu [NIP-17](/nl/topics/nip-17/) private DMs en [NIP-59](/nl/topics/nip-59/) gift wrapping ondersteunt. Dezelfde week kondigde [OpenSats hun vierde golfbeurzen aan](https://opensats.org/blog/nostr-grants-december-2023) op 21 december, financiering van zeven projecten inclusief Lume, noStrudel, ZapThreads en een onafhankelijke NIP-44-audit. Dit volgde de [eerste golf in juli 2023](https://opensats.org/blog/nostr-grants-july-2023) die Damus, Coracle, Iris en anderen had gefinancierd, waarbij de totale Nostr Fund-toewijzing ongeveer $3,4 miljoen over 39 beurzen bedroeg.

De maand stelde ook duurzaamheidsspanningen in het ecosysteem bloot. Op 28 december [postte William Casarin (jb55) op Stacker News](https://stacker.news/items/368863) dat 2024 "waarschijnlijk het laatste jaar van Damus" zou zijn, stellende dat "nostr-clients geen geld verdienen" na Apple's restricties op in-app zaps die de opbrengstmogelijkheden ernstig beperkte. Het Damus-team had eerder VC-financiering afgewezen. Ondertussen werd [Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1) op 26 december uitgegeven, uitbreiding van [NIP-47](/nl/topics/nip-47/) met `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` en `get_info`-methoden, leggende grondwerk voor de portefeuilleintegraties die standaard zouden worden over clients.

### December 2024: Protocol-vooruitgang

December 2024 opende met de [Notedeck Alpha-lancering](https://damus.io/notedeck/) op 30 november, de Rust-gebaseerde desktopclien van het Damus-team met een multi-kolom interface met meervoudig accountondersteuning. Gebouwd voor Linux, macOS en Windows (Android gepland voor 2025), Notedeck werd aanvankelijk naar Damus Purple-abonnees verstuurd en vertegenwoordigde een strategische expansie voorbij iOS. Twee weken later kondigde [OpenSats hun negende golfbeurzen aan](https://opensats.org/blog/9th-wave-of-nostr-grants) op 16 december, financiering van AlgoRelay (de eerste algoritmische relay voor gepersonaliseerde feeds), Pokey (Android-app met Bluetooth-mesh voor beperkt internet), Nostr Safebox ([NIP-60](/nl/topics/nip-60/) [Cashu](/nl/topics/cashu/) token-opslag) en LumiLumi (lichtgewicht toegankelijke webclient), toewijzing van totale Nostr Fund naar ongeveer $9 miljoen, een stijging van 67% jaar-op-jaar.

De maand zag significante client-volwassenheid over het ecosysteem. [Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0) landde op 23 december met Bestandsmetadata ([NIP-92](/nl/topics/nip-92/)/[NIP-94](/nl/topics/nip-94/)) ondersteuning, Blossom-integratie en [NIP-50](/nl/topics/nip-50/) relayzoeken. [Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0) werd op 12 december verscheept met herziene onboarding en nostr-editor integratie. Protocol-ontwikkeling bleef actief met 30 pull requests ingediend tussen 9-22 december (10 gemerged), inclusief [NIP-46](/nl/topics/nip-46/) herschrijvingen om alleen NIP-44 versleuteling te gebruiken en voortgezet werk aan [NIP-104](/nl/topics/nip-104/) voor Signal-niveau double ratchet-versleuteling. Netwerkstatistieken toonden 224.000+ dagelijkse vertrouwde pubkey-events, 4x jaar-op-jaar groei in nieuwe profielen met contactlijsten en 50% toename in openbare schrijfevents.

### December 2025: Ecosysteem-expansie

December 2025 bracht voortgezette protocol-volwassenheid en ecosysteem-expansie. Op 21 december kondigde [OpenSats hun veertiende golfbeurzen aan](https://opensats.org/blog/fourteenth-wave-of-nostr-grants), financiering van drie projecten: YakiHonne (een multi-platformclient met creatorsportal voor inhoud met lange vorm en [Cashu](/nl/topics/cashu/)/Nutzaps betalingsintegratie), Quartz (Vitor Pamplona's Kotlin Multiplatform-bibliotheek die Amethyst aandrijft en een iOS-versie zal mogelijk maken) en Nostr Feedz (bidirectionele RSS-naar-Nostr integratie door PlebOne). Grant-verlengingen gingen naar Dart NDK en Mattn's nostr-relay.

Protocol-evolutie ging door met [NIP-BE](/nl/topics/nip-be/) (Bluetooth Low Energy messaging, [#1979](https://github.com/nostr-protocol/nips/pull/1979)) gemerged in november, het mogelijk maken van offlinevice synchronisatie. [NIP-A4](/nl/topics/nip-a4/) (Openbare berichten, kind 24, [#1988](https://github.com/nostr-protocol/nips/pull/1988)) landde later in de maand, definiërend notificatieschermbericht die `q` tags gebruiken om threadingproblemen te vermijden. [NIP-29](/nl/topics/nip-29/) ontving grote verduidelijking ([#2106](https://github.com/nostr-protocol/nips/pull/2106)), introductie van de `hidden` tag voor echt private, ondetecteerbare groepen. De [NIP-55](/nl/topics/nip-55/) spec ontving ook verfijning ([#2166](https://github.com/nostr-protocol/nips/pull/2166)), het aanpakken van een veelgebruikt implementatiefout waar ontwikkelaars `get_public_key` vanuit achtergrondprocessen belden.

Aan de client-zijde werd [Primal Android een volledige NIP-55-signer](/nl/newsletters/2025-12-24-newsletter/#nieuws) via acht samengevoegde PRs die `LocalSignerContentProvider` implementeerden, sluitend aan bij Amber en Aegis als Android signing opties. De [NDK-bibliotheek bereikte 162x snellere cachequery's](/nl/newsletters/2025-12-24-newsletter/#opmerkelijk-code-en-documentatiewijzigingen) (van ~3.690ms naar ~22ms) door het elimineren van dubbele schrijfbewerkingen en onnodig LRU-cachequery's ([PR #371](https://github.com/nostr-dev-kit/ndk/pull/371), [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)). Shopstr introduceerde [Zapsnags](/nl/newsletters/2025-12-24-newsletter/#nieuws) voor flitsverkoop via zaps. White Noise verzond [MIP-05](/nl/topics/mip-05/) privacybehoudende pushnotificaties. Zie [Nieuwsbrief #1](/nl/newsletters/2025-12-17-newsletter/) en [Nieuwsbrief #2](/nl/newsletters/2025-12-24-newsletter/) voor volledige dekking.

---

Vijf jaar geleden gaf fiatjaf Branle vrij aan een handvol gebruikers over twee experimentele relays. Vandaag ondersteunt het protocol 140+ clients, 2.500+ relays over 50 landen, en een groeiend web van vertrouwen dat honderdduizenden sleutelparen verbindt. Het decemberpatroon van grote releases zette zich deze maand voort met Bluetooth-berichten, Android-signer verspreiding en infrastructuurbeurzen die aanhoudende investeringen in cross-platformtooling signaleerden.

## Nieuws

**Amethyst Desktop neemt vorm aan** - De Quartz-beurs van OpenSats' veertiende golf produceert al resultaten. [PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625) creëert een volledige `:desktopApp` module voor Amethyst met Compose Multiplatform, met login- en globale feedschermen functioneel op Desktop JVM. De architectuur converteert de `:commons` module naar Kotlin Multiplatform met een schone bron set-structuur (`commonMain`, `jvmAndroid`, `androidMain`, `jvmMain`), het mogelijk maken van gedeelde UI-componenten tussen Android en desktop terwijl platform-specifieke beslissingen aan elk doel worden overgelaten. Dit legt de grondslag voor de uiteindelijke iOS-versie via dezelfde Kotlin Multiplatform-aanpak.

**Amethyst Voice Replies** - Een Kerstgeschenk van davotoula: [PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622) voegt toegewijde voice reply-schermen toe met golfvormvisualisatie, hernamedondersteuning, media server-selectie en uploadvoortgangsindicatoren. Gebruikers kunnen nu antwoorden op zowel root voice-berichten als voice-antwoorden met audio.

**Notedeck voegt berichten toe** - Notedeck, de Damus-desktopclien, kreeg een berichtenfunctie in [PR #1223](https://github.com/damus-io/notedeck/pull/1223), expansie voorbij timelines naar directe communicatie.

**Citrine Host Webapps** - Citrine kan nu [webapplicaties hosten](https://github.com/greenart7c3/Citrine/pull/81), je telefoon omzetten in een lokale Nostr-webserver. Een aparte [PR #85](https://github.com/greenart7c3/Citrine/pull/85) voegt automatische herverbinding en event-uitzending toe wanneer netwerkconnectiviteit terugkeert, met uitgebreide testdekking over Android API-niveaus.

**Nostrability Developer Toolkit Registry** - De [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264) tracker onderhoudt een gecureerde registerboek van SDK's, bibliotheken en developer-tools over talen (TypeScript, Rust, Python, Go, Dart, Swift en meer). Als je nieuw bent in Nostr-ontwikkeling, is dit een nuttig startpunt voor het vinden van de juiste toolkit voor je stack.

## NIP Updates

Recente wijzigingen in de [NIPs-repository](https://github.com/nostr-protocol/nips):

- **[NIP-54](/nl/topics/nip-54/)** - Kritieke internationalisatieoplossing voor wiki d-tag normalisatie ([#2177](https://github.com/nostr-protocol/nips/pull/2177)). Vorige regels converteerden alle niet-ASCII-tekens naar `-`, verbroken ondersteuning voor Japans, Chinees, Arabisch, Cyrillisch en andere scripts. De bijgewerkte spec behoudt UTF-8-letters, past alleen kleine letters toe op tekens met variantengevallen, en bevat uitgebreide voorbeelden: `"ウィキペディア"` blijft `"ウィキペディア"`, `"Москва"` wordt `"москва"`, en gemengde scripts zoals `"日本語 Article"` normaliseren naar `"日本語-article"`.

## Releases

**Zapstore 1.0-rc1** - De Nostr-gebaseerde toepassing zonder toestemming verzendt de [eerste release candidate](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1) van zijn nieuwe architectuur, met een volledige UI-vernieuwing, herschreven packagemanager met verbeterde foutafhandeling, App Stacks voor gecureerde ontdekkingen, herdoordachte profielschermen, achtergrondupdate controle en oneindige scrollen in release lists.

**KeyChat v1.38.1** - De MLS-gebaseerde versleutelde berichtenapp [voegt UnifiedPush-ondersteuning toe](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489) voor Android en Linux pushnotificaties, plus biometrische authenticatie voor privacyoperaties. Beschikbaar voor Android, Windows, macOS en Linux.

**Alby Go v2.0.0** - De mobiele Lightning-portefeuille metgezel [verzendt een visuele herontwerp](https://github.com/getAlby/go/releases/tag/v2.0.0) met nieuw logo, bijgewerkt kleurenpalet, herontworpen adresboek en verbeterd bedragsinvoerkeyboard. BTC Map is nu toegankelijk van het thuisscherm, en transactiebeschrijvingen verschijnen in notificaties.

**nak v0.17.4** - fiatjaf's command-line Nostr-tool [vrijgegeven](https://github.com/fiatjaf/nak/releases/tag/v0.17.4), volgend op v0.17.3's LMDB Linux-restrictie reparatie van vorige week.

## Opmerkelijk code en documentatiewijzigingen

*Open pull requests en vroeg-stadium werk de moeite waard om te volgen.*

### Damus (iOS)

[NIP-19 relay hints](https://github.com/damus-io/damus/pull/3477) implementeert relay hint consumptie voor event-ophaling. Wanneer gebruikers nevent, nprofile of naddr links openen, haalt Damus nu relayhinten uit de bech32 TLV-gegevens en verbindt zich met kortstondig relays om inhoud op te halen die niet in de relay pool van de gebruiker staat. De implementatie omvat ref-geteld opruiming om race conditions tijdens gelijktijdige lookups te voorkomen. [URL-detectie van afbeelding](https://github.com/damus-io/damus/pull/3474) converteert automatisch geplakte afbeeldings-URL's in preview-miniatuurafbeeldingen in de composer, met een carrouselpositie badge voor meerdere afbeeldingen. [npub plakken conversie](https://github.com/damus-io/damus/pull/3473) transformeert geplakte npub/nprofile-strings in vermeldingskoppelingen met asynchrone profielresolutie.

### Amethyst (Android)

[Betalingsdoelen](https://github.com/vitorpamplona/amethyst/pull/1627) voegt een event-interface toe voor NIP-57 zap splits, waardoor berichten meerdere ontvangers kunnen specificeren die binnenkomende zaps delen (nuttig voor samenwerkingen, inkomstendelende of tipping zowel contentmakers als de tools die zij gebruiken). [Quartz-functie pariteit documentatie](https://github.com/vitorpamplona/amethyst/pull/1624) voegt een gedetailleerde tabel toe die volgt welke functies over Android, Desktop JVM en iOS-doelen zijn geïmplementeerd, stellende dat iOS kernelcryptografie (`Secp256k1Instance`), JSON-serialisatie en gegevensstructuren mist.

### Notedeck (Desktop)

[Timeline filter wederopbouw](https://github.com/damus-io/notedeck/pull/1226) repareert een fout waarbij onvolgde accounts keer op keer in feeds verschenen. Timeline-filters werden eenmaal uit de contactlijst gebouwd en nooit bijgewerkt; de oplossing voegt `contact_list_timestamp` tracking en een `invalidate()` methode toe om herbouwen te triggeren wanneer vervolgstatus verandert.

### Citrine (Android Relay)

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86) stelt de lokale relay's event-database bloot aan andere Android-apps via `ContentResolver`. In plaats van de WebSocket-interface (die vereist dat apps een aanhoudende verbinding onderhouden en het Nostr relay-protocol spreken), biedt ContentProvider directe synchrone database-toegang via Android's eigen IPC-mechanisme. Externe apps kunnen query-events op ID, pubkey, kind of datumbereik, insert nieuwe events met validatie en delete events zonder socket-verbindingen te beheren.

### rust-nostr (Bibliotheek)

[NIP-40 relay-niveau ondersteuning](https://github.com/rust-nostr/nostr/pull/1183) voegt verval-afhandeling toe op het relay builder-niveau. Verlopen events worden nu geweigerd vóór opslag en gefilterd voordat ze naar clients worden verstuurd, waardoor elke database-implementatie onafhankelijk vervalbevoegingen hoeft af te handelen.

### nak (CLI)

[Blossom mirror](https://github.com/fiatjaf/nak/pull/91) implementeert blob mirroring functionaliteit voor het command-line-tool.

### Mostro (P2P Trading)

[Dev fee audit events](https://github.com/MostroP2P/mostro/pull/559) voegt transparante audit trails toe voor ontwikkelingsfonds betalingen via kind 8383 Nostr-events. De implementatie publiceert niet-blokkerend audit events na succesvolle fee-betalingen, met orderdetails en betalingshashes terwijl koper/verkoper pubkeys voor privacy worden uitgesloten.

### MDK (Marmot Development Kit)

Drie security audit reparaties landden: [Author verificatie](https://github.com/marmot-protocol/mdk/pull/40) handhaaft dat roddel pubkeys MLS zender gegevens afstemmen, het voorkomen van imitatie-aanvallen. [KeyPackage identiteitsBinding](https://github.com/marmot-protocol/mdk/pull/41) verifieert dat referentie-identiteit event ondertekenaar afstemt. [Admin update validatie](https://github.com/marmot-protocol/mdk/pull/42) voorkomt lege admin sets en niet-lid admin toewijzingen.

### Shopstr (Marketplace)

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217) implementeert een vertrouwensminimale betalingssysteem voor fysieke goederen. De architectuur gebruikt Alby's `makeHoldInvoice` om koper middelen in hun eigen portefeuille vast te leggen, met settling getriggerd alleen na inventarisverificatie door handelspartij. Het handshake-protocol stroomt door [NIP-17](/nl/topics/nip-17/) versleuterde DMs: koper verzendt orderverzoek, handelspartij reageert met HODL factuur, koper betaalt (middelen vergrendeld), handelspartij bevestigt voorraad en verzending, dan setting geeft middelen vrij. Multi-handelspartij cart ondersteuning splitsbare betalingen over leveranciers.

### Jumble (Web Client)

[Per-relay discovery mode](https://github.com/CodyTseng/jumble/pull/713) voegt een toggle toe om berichten van vervolgde gebruikers op specifieke relays te verbergen, discovery feeds op basis van taal mogelijk makende (bijvoorbeeld nostr.band/lang/*). De functie filtert berichten uit waarbij de auteur pubkey in de volglijst van de gebruiker verschijnt, permanente toggle status per relay URL in localStorage.

### White Noise (Versleutelde Messaging)

[Media upload retry](https://github.com/marmot-protocol/whitenoise/pull/937) voegt herhalingopties toe voor mislukte uploads. [Profile edit warnings](https://github.com/marmot-protocol/whitenoise/pull/927) waarschuwen gebruikers over profielwijzigingen. Op de achterkant repareerde [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422) een race condition in AccountGroup creatie.

### npub.cash (Lightning Address Service)

[v3 herschrijving](https://github.com/cashubtc/npubcash-server/pull/40) migreert naar Bun voor de monorepo en server, voegt SQLite ondersteuning toe, laat v1-compatibiliteit vallen, implementeert LUD-21 en voegt real-time munt quote updates toe.

### nostr-java (Bibliotheek)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1) verzendt WebSocket-afhandelingsherschrijvingen en verbeterde test-robuustheid over [twee PRs](https://github.com/tcheeric/nostr-java/pull/499).

### NIPs Repository

[NIP-54 Djot migratie](https://github.com/nostr-protocol/nips/pull/2180) stelt een aparte wijziging voor aan de wiki spec: het format van Asciidoc naar Djot omzetten, een lichtgewicht opmaaktaal met schonere syntaxis. De PR introduceert verwijzingsstijlkoppelingen voor wikilinks, het maken van cross-verwijzingen tussen wiki artikelen leesbaarder in bronvorm. [NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179) introduceert drempelmulti-handtekeningbestuur voor Nostr-groepen met behulp van FROST (Flexible Round-Optimized Schnorr Threshold signatures). Een Quorum is een nsec gedeeld onder leden via een T-van-N-schema waarbij leden zichzelf kunnen vertegenwoordigen of naar een raad van gevolmachtigden kunnen delegeren. Wanneer de raad verandert, wordt de oude nsec verouderd en een nieuwe wordt verdeeld—de afsluitende daad van elke raad ondertekent de bestuuring transitie event. De spec definieert lidmaatschap (openbaar of privé), verkiezingen en peilingen (populaire stemmen, stemmen van geen vertrouwen), optioneel natuurlijke taal "wetten," en crucaal, quorum ontologieën waarbij quorum leden van andere quorum kunnen zijn, het mogelijk maken van hiërarchische structuren zoals lokaliteiten die zich voegen bij regionale lichamen. Gebruikssituaties beslaan broncode ontwikkeling, bedrijfsbesturen, HOA's en gemodereerde gemeenschappen.

---

Dat is het voor deze week en dit jaar. Bouwt u iets? Hebt u nieuws om te delen? Wilt u dat we uw project dekken? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Bereik ons via NIP-17 DM</a> of zoek ons op Nostr.
