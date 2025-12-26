---
title: 'Nostr Kompas #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
---

Welkom bij Nostr Kompas, een wekelijkse nieuwsbrief gewijd aan het Nostr-protocol ecosysteem. Onze missie is om ontwikkelaars, relay-operators en bouwers op de hoogte te houden van belangrijke ontwikkelingen in het netwerk. We documenteren protocol-evolutie met technische nauwkeurigheid, neutraliteit en diepgang, en behandelen alles van NIP-voorstellen tot client-releases tot implementatie best practices.

Nostr Kompas is geïnspireerd door [Bitcoin Optech](https://bitcoinops.org/), wiens jarenlange toegewijde werk aan het bevorderen van Bitcoin technische kennis de standaard heeft gezet voor protocol-gerichte nieuwsbrieven. We zijn dankbaar voor hun voorbeeld en hopen dezelfde nauwkeurigheid naar het Nostr-ecosysteem te brengen.

Deze inaugurele editie introduceert ons wekelijkse format. Elke woensdag brengen we je NIP-updates, release notes, ontwikkelingshoogtepunten en technische begeleiding. Of je nu een client bouwt, een relay beheert of bijdraagt aan het protocol, Nostr Kompas wil je betrouwbare bron zijn voor wat er gebeurt in het ecosysteem.

## Wat is Nostr?

*Aangezien dit onze eerste editie is, beginnen we met een introductie over hoe Nostr werkt. Vaste lezers kunnen [vooruit springen](#news).*

Nostr (Notes and Other Stuff Transmitted by Relays) is een gedecentraliseerd protocol voor sociale netwerken en berichtenverkeer. In tegenstelling tot traditionele platforms heeft Nostr geen centrale server, geen bedrijf dat het controleert en geen enkel punt van falen. Gebruikers bezitten hun identiteit via cryptografische sleutelparen, en content stroomt via onafhankelijke relay-servers die iedereen kan draaien.

**Hoe het werkt:** Gebruikers genereren een sleutelpaar (een privésleutel genaamd nsec en publieke sleutel genaamd npub). De privésleutel ondertekent berichten die "events" worden genoemd, en de publieke sleutel dient als je identiteit. Events worden naar relays gestuurd, die ze opslaan en doorsturen naar andere gebruikers. Omdat je je sleutels beheert, kun je wisselen tussen clients of relays zonder je identiteit of volgers te verliezen.

**Waarom het belangrijk is:** Nostr biedt censuurbestendigheid door relay-diversiteit (als één relay je bant, kunnen anderen nog steeds je content serveren), portabiliteit (je identiteit werkt in elke Nostr-app) en interoperabiliteit (alle Nostr-clients spreken hetzelfde protocol). Er is geen algoritme dat bepaalt wat je ziet, geen advertenties en geen dataverzameling.

**Het ecosysteem vandaag:** Nostr ondersteunt microblogging (zoals Twitter/X), long-form content (zoals Medium), directe berichten, marktplaatsen, livestreaming en meer. Clients omvatten Damus (iOS), Amethyst (Android), Primal, Coracle en tientallen anderen. Lightning Network-integratie maakt directe betalingen mogelijk via "zaps." Het protocol blijft evolueren via NIPs (Nostr Implementation Possibilities), community-gedreven specificaties die functionaliteit uitbreiden.

## Nieuws {#news}

**NIP-BE Samengevoegd: Bluetooth Low Energy Ondersteuning** - Een belangrijke nieuwe mogelijkheid [is aan het protocol toegevoegd](https://github.com/nostr-protocol/nips/pull/1979). [NIP-BE](/nl/topics/nip-be/) specificeert hoe Nostr-applicaties kunnen communiceren en synchroniseren via Bluetooth Low Energy. Dit maakt offline-capabele apps mogelijk die data kunnen synchroniseren tussen apparaten in de buurt zonder internetverbinding. De specificatie past WebSocket relay-patronen aan voor de beperkingen van BLE, met behulp van DEFLATE-compressie en gesegmenteerde berichten om de kleine MTU-groottes van BLE (20-256 bytes) te hanteren. Apparaten onderhandelen rollen op basis van UUID-vergelijking, waarbij de hogere UUID de GATT-server wordt.

**MIP-05: Privacy-behoudende Push Notificaties** - Het [Marmot Protocol](/nl/topics/marmot/) publiceerde [MIP-05](/nl/topics/mip-05/) ([specificatie](https://github.com/marmot-protocol/mips/blob/main/mip-05.md)), een specificatie voor push notificaties die privacy behouden. Traditionele push-systemen vereisen dat servers apparaat-tokens en gebruikersidentiteiten kennen; MIP-05 lost dit op door apparaat-tokens te versleutelen met ECDH+HKDF en ChaCha20-Poly1305, met behulp van tijdelijke sleutels om correlatie te voorkomen. Een drie-event gossip-protocol (kinds 447-449) synchroniseert versleutelde tokens over groepsleden, en notificaties gebruiken [NIP-59](/nl/topics/nip-59/) gift wrapping met decoy-tokens om groepsgroottes te verbergen. Dit stelt WhiteNoise en andere Marmot-clients in staat om tijdige notificaties te leveren zonder de privacy van gebruikers te compromitteren.

**Blossom BUD-10: Nieuw URI-schema** - Het [Blossom](/nl/topics/blossom/) mediaprotocol krijgt een aangepast URI-schema via [BUD-10](/nl/topics/bud-10/) ([specificatie](https://github.com/hzrd149/blossom/blob/master/buds/10.md)). Het nieuwe `blossom:<sha256>.ext` formaat bevat bestandshash, extensie, grootte, meerdere serverhints en auteur-pubkeys voor [BUD-03](/nl/topics/bud-03/) serverontdekking. Dit maakt blob-links veerkrachtiger dan statische HTTP-URL's door automatische fallback over servers mogelijk te maken.

**Shopstr Marktplaats Updates** - De Nostr-native marktplaats [implementeerde Nostr Wallet Connect](https://github.com/shopstr-eng/shopstr/pull/202) ([NIP-47](/nl/topics/nip-47/)) voor betalingen, [voegde vermelding-verloopdatum toe](https://github.com/shopstr-eng/shopstr/pull/203) met behulp van [NIP-40](/nl/topics/nip-40/), en introduceerde [kortingscodes](https://github.com/shopstr-eng/shopstr/pull/210) voor verkopers.

## NIP Updates {#nip-updates}

Recente wijzigingen in de [NIPs repository](https://github.com/nostr-protocol/nips):

**Nieuwe NIPs:**
- **[NIP-BE](/nl/topics/nip-be/)** - Bluetooth Low Energy messaging en apparaatsynchronisatie ([#1979](https://github.com/nostr-protocol/nips/pull/1979))
- **[NIP-63](/nl/topics/nip-63/)** - Paywall/Premium Content standaard voor het afhandelen van afgesloten content binnen het protocol ([#2156](https://github.com/nostr-protocol/nips/pull/2156))

**Significante Wijzigingen:**
- **[NIP-24](/nl/topics/nip-24/)** - Optionele `languages` array toegevoegd aan Kind 0 gebruikersmetadata, waarmee gebruikers meerdere voorkeurstalen kunnen specificeren met IETF BCP 47 tags voor verbeterde contentontdekking en relay-matching ([#2159](https://github.com/nostr-protocol/nips/pull/2159))
- **[NIP-69](/nl/topics/nip-69/)** - Ondersteuning voor orderverloopdatum toegevoegd voor P2P-handel met `expires_at` en `expiration` tags ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **[NIP-59](/nl/topics/nip-59/)** - Gift wrap events kunnen nu worden verwijderd via NIP-09/NIP-62 verzoeken ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **[NIP-51](/nl/topics/nip-51/)** - Hashtag en URL tags verwijderd uit generieke bladwijzers; hashtags gebruiken nu kind 30015 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **[NIP-18](/nl/topics/nip-18/)** - Verbeterde generieke reposts voor vervangbare events met `a` tag ondersteuning ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **[NIP-17](/nl/topics/nip-17/)** - Verfijnde bewoording en kind 7 reactie-ondersteuning toegevoegd aan DMs ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **[NIP-11](/nl/topics/nip-11/)** - `self` veld toegevoegd voor relay publieke sleutel identificatie ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## NIP Diepgaand: NIP-01 en NIP-19 {#nip-deep-dive-nip-01-and-nip-19}

Voor deze inaugurele editie behandelen we twee fundamentele NIPs die elke Nostr-ontwikkelaar moet begrijpen. Zie onze onderwerpspagina's voor [NIP-01](/nl/topics/nip-01/) en [NIP-19](/nl/topics/nip-19/).

### NIP-01: Basisprotocol

[NIP-01](/nl/topics/nip-01/) definieert het kernprotocol. Alles in Nostr bouwt voort op deze specificatie.

**Events** zijn het enige objecttype. Elk event bevat:
- `id`: SHA256-hash van het geserialiseerde event (de unieke identifier van het event)
- `pubkey`: De publieke sleutel van de maker (32-byte hex, secp256k1)
- `created_at`: Unix-tijdstempel
- `kind`: Integer die het eventtype categoriseert
- `tags`: Array van arrays voor metadata
- `content`: De payload (interpretatie hangt af van kind)
- `sig`: Schnorr-handtekening die bewijst dat de pubkey dit event heeft gemaakt

**Kinds** bepalen hoe relays events opslaan:
- Reguliere events (1, 2, 4-44, 1000-9999): Normaal opgeslagen, alle versies behouden
- Vervangbare events (0, 3, 10000-19999): Alleen de laatste per pubkey wordt behouden
- Vluchtige events (20000-29999): Niet opgeslagen, alleen doorgestuurd naar abonnees
- Adresseerbare events (30000-39999): Laatste per pubkey + kind + `d` tag combinatie

Kind 0 is gebruikersmetadata (profiel), kind 1 is een tekstnota (de basis post), kind 3 is de volglijst.

**Kind 1: Tekstnota's** vormen het hart van sociaal Nostr. Een kind 1 event is een korte post, vergelijkbaar met een tweet. Het `content` veld bevat de berichttekst (platte tekst, hoewel clients vaak markdown renderen). Tags maken reacties, vermeldingen en referenties mogelijk:

```json
{
  "id": "<32-byte-hex>",
  "pubkey": "<32-byte-hex>",
  "created_at": 1734480000,
  "kind": 1,
  "content": "Hallo Nostr! Bekijk het werk van @jb55 aan Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ],
  "sig": "<64-byte-hex>"
}
```

De `e` tag met "reply" markering geeft aan dat dit een reactie is (zie [NIP-10](/nl/topics/nip-10/) voor threading-conventies). De `p` tag vermeldt een gebruiker, waardoor clients hen kunnen notificeren en hun naam kunnen renderen in plaats van de ruwe pubkey. Clients halen het kind 0 event van de vermelde gebruiker op om hun weergavenaam en foto te krijgen.

Om een tijdlijn te bouwen, abonneert een client zich op kind 1 events van gevolgde pubkeys: `["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`. De relay retourneert overeenkomende nota's en de client rendert ze chronologisch.

**Adresseerbare events** (30000-39999) werken zoals vervangbare events maar gebruiken een `d` tag als extra identifier. De relay behoudt alleen de laatste versie van elke pubkey + kind + d-tag combinatie. Dit maakt bewerkbare artikelen, productvermeldingen of elk geval mogelijk waar je meerdere vervangbare items per gebruiker nodig hebt.

**Tags** zijn arrays waarbij het eerste element de tagnaam is. Standaard enkelletter-tags (`e`, `p`, `a`, `d`, `t`) worden geïndexeerd door relays voor efficiënt opvragen. Bijvoorbeeld, `["e", "<event-id>"]` verwijst naar een ander event, `["p", "<pubkey>"]` verwijst naar een gebruiker.

**Client-Relay Communicatie** gebruikt WebSocket-verbindingen met JSON-arrays als berichten. Het eerste element identificeert het berichttype.

Van client naar relay:
- `["EVENT", <event>]` - Publiceer een event naar de relay
- `["REQ", <sub-id>, <filter>, ...]` - Abonneer op events die overeenkomen met de filter(s)
- `["CLOSE", <sub-id>]` - Beëindig een abonnement

Van relay naar client:
- `["EVENT", <sub-id>, <event>]` - Levert een event dat overeenkomt met je abonnement
- `["EOSE", <sub-id>]` - "Einde van opgeslagen events" - de relay heeft alle historische overeenkomsten verzonden en zal nu alleen nieuwe events sturen wanneer ze binnenkomen
- `["OK", <event-id>, <true|false>, <message>]` - Bevestigt of een event is geaccepteerd of afgewezen (en waarom)
- `["NOTICE", <message>]` - Leesbaar bericht van de relay

De abonnementsstroom: client stuurt `REQ` met een abonnement-ID en filter, relay antwoordt met overeenkomende `EVENT`-berichten, stuurt vervolgens `EOSE` om aan te geven dat het de geschiedenis heeft ingehaald. Na `EOSE` zijn eventuele nieuwe `EVENT`-berichten realtime. Client stuurt `CLOSE` wanneer klaar.

**Filters** specificeren welke events opgehaald moeten worden. Een filterobject kan bevatten: `ids` (event-ID's), `authors` (pubkeys), `kinds` (eventtypes), `#e`/`#p`/`#t` (tagwaarden), `since`/`until` (tijdstempels), en `limit` (max resultaten). Alle voorwaarden binnen één filter gebruiken AND-logica. Je kunt meerdere filters opnemen in een `REQ`, en ze combineren met OR-logica - handig voor het ophalen van verschillende eventtypes in één abonnement.

### NIP-19: Bech32-gecodeerde Identifiers

[NIP-19](/nl/topics/nip-19/) definieert de mensvriendelijke formaten die je overal in Nostr ziet: npub, nsec, note en meer. Deze worden niet in het protocol zelf gebruikt (dat gebruikt hex), maar ze zijn essentieel voor delen en weergave.

**Waarom bech32?** Ruwe hex-sleutels zijn foutgevoelig om te kopiëren en visueel moeilijk te onderscheiden. Bech32-codering voegt een leesbaar voorvoegsel en checksum toe. Je kunt onmiddellijk een `npub` (publieke sleutel) onderscheiden van een `nsec` (privésleutel) of `note` (event-ID).

**Basisformaten** coderen ruwe 32-byte waarden:
- `npub` - Publieke sleutel (je identiteit, veilig om te delen)
- `nsec` - Privésleutel (houd geheim, gebruikt voor ondertekenen)
- `note` - Event-ID (verwijst naar een specifiek event)

Voorbeeld: De hex-pubkey `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d` wordt `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

**Deelbare identifiers** bevatten metadata met TLV (Type-Length-Value) codering:
- `nprofile` - Profiel met relay-hints (helpt clients de gebruiker te vinden)
- `nevent` - Event met relay-hints, auteur-pubkey en kind
- `naddr` - Adresseerbare event-referentie (pubkey + kind + d-tag + relays)

Deze lossen een belangrijk probleem op: als iemand een note-ID deelt, hoe weet je welke relay het heeft? Een `nevent` bundelt de event-ID met voorgestelde relays, waardoor delen betrouwbaarder wordt.

**Belangrijk:** Gebruik nooit bech32-formaten in het protocol zelf. Events, relay-berichten en NIP-05 antwoorden moeten hex gebruiken. Bech32 is puur voor menselijke interfaces: weergave, kopiëren/plakken, QR-codes en URL's.

## Releases {#releases}

**Amber v4.0.4** - De Android signer-app repareert een NullPointerException, verbetert prestaties op het activiteitenscherm en voegt vertalingen toe voor sommige event-kinds. De eerdere v4.0.3 release voegde een vernieuwde encryptie/decryptie-UI toe, account export/import, per-account relay-afhandeling, bunker ping-ondersteuning en crashrapportage. [Release](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - Bugfix-release voor de webclient. Opgeloste problemen met topic-feeds, afbeeldingsafhandeling wanneer imgproxy is uitgeschakeld, en linkificatie van niet-link highlight-bronnen. [Release](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - De Discord-achtige communities-client repareert modal-scrolling en stijlproblemen. Eerdere releases in deze cyclus voegden optionele badges en geluiden toe voor notificaties, verbeterde linkrendering, QR-code scanning voor uitnodigingslinks en gestroomlijnde wallet-setup. [Release](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - De commandoregel Nostr-tool voegde een nieuw `nip`-commando toe voor snelle NIP-referentie-opzoekingen, plus fixes voor git repository-afhandeling en stdin event-verwerking. [Release](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - Grote release voor de MLS-gebaseerde versleutelde berichten-app met het toevoegen van afbeeldingen delen via Blossom, achtergrondsynchronisatie, push-notificaties, 8-talige lokalisatie en groepslidmaatschapsbeheer. [Release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - Feature-release met introductie van volglijsten/pakketten, nieuwe tijdlijnfilters, afbeeldingsgalerij en H.265 videocompressie (50% kleinere bestanden). Voltooide Kotlin Multiplatform-migratie. [Release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - P2P-handelsbot update met NIP-69 orderverloopdatum-ondersteuning en verbeterde handelsgeschiedenis-antwoorden. [Release](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

**Nosflare v8.9.26** - Serverless Nostr-relay gebouwd op Cloudflare-infrastructuur. Deze release levert een kritieke hotfix die een bug aanpakt die websocket-fouten kon veroorzaken, wat zorgt voor stabielere verbindingen voor gebruikers en applicaties die afhankelijk zijn van de relay. [Release](https://github.com/Spl0itable/nosflare/releases/tag/v8.9.26)

**Noscall v0.4.1** - Nostr-gebaseerde beveiligde audio- en video-bel-app. Deze release verbetert de pop-up UI op de Me-pagina en repareert verschillende bekende problemen, resulterend in betere stabiliteit en belbetrouwbaarheid. [Release](https://github.com/sanah9/noscall/releases/tag/v0.4.1-release)

**Gitplaza v0.25.0** - Desktop Nostr-client gericht op Git-gerelateerde activiteit. Deze release introduceert een geavanceerd kind-filter voor de inbox-feed, omvat reguliere zaps in filters en vereenvoudigt tab-tekstopmaak. Prestatieverbeteringen optimaliseren comment-tree laden, verminderen onnodige database-queries en gebruiken gecachte comment-branches voor snellere weergave. [Release](https://codeberg.org/dluvian/gitplaza/releases/tag/v0.25.0)

## Noemenswaardige code- en documentatiewijzigingen {#notable-code-and-documentation-changes}

### Damus (iOS) {#damus}

Stabiliteitsfocus met crash- en UI-fixes: [cursor-sprong fix](https://github.com/damus-io/damus/pull/3377) voor de compose-weergave, [NostrDB interface herontwerp](https://github.com/damus-io/damus/pull/3366) met Swift's `~Copyable` types voor transactieveiligheid, [thread UI-stabiliteit](https://github.com/damus-io/damus/pull/3341) die action bar herinstantiatie repareert, [mute-lijst bevriezing](https://github.com/damus-io/damus/pull/3346) van AttributeGraph-cycli, en [profiel-crash](https://github.com/damus-io/damus/pull/3334) van cross-thread transactie-opruiming. Ook [AGENTS.md](https://github.com/damus-io/damus/pull/3293) richtlijnen toegevoegd voor AI-codeeragenten.

### Notedeck (Desktop/Mobiel) {#notedeck}

[Beveiligde sleutelopslag](https://github.com/damus-io/notedeck/pull/1191) verplaatst nsec naar OS beveiligde opslag met automatische migratie. [Toekomstige nota-filtering](https://github.com/damus-io/notedeck/pull/1201) verbergt events met datum 24+ uur vooruit (anti-spam). [nevent kopiëren](https://github.com/damus-io/notedeck/pull/1183) bevat nu relay-hints. Ook: [profiel-kolom snelle toevoeging](https://github.com/damus-io/notedeck/pull/1212), [toetsenbordnavigatie](https://github.com/damus-io/notedeck/pull/1208), [media-laadoptimalisatie](https://github.com/damus-io/notedeck/pull/1210).

### Amethyst (Android) {#amethyst}

[[NIP-46](/nl/topics/nip-46/) remote signing](https://github.com/vitorpamplona/amethyst/pull/1555) ondersteuning voor Nostr Connect. [Bladwijzerorganisatie](https://github.com/vitorpamplona/amethyst/pull/1586) met publiek/privé lijstbeheer. [strfry-compatibiliteit](https://github.com/vitorpamplona/amethyst/pull/1596) fix voor relay-info parsing edge cases.

### Primal (Android) {#primal}

[Nostr Connect deep links](https://github.com/PrimalHQ/primal-android-app/pull/788) voor `nostrconnect://` URL's. [Remote login](https://github.com/PrimalHQ/primal-android-app/pull/787) via QR-scan voor bunker-verbindingen. [Verbindings-race condition fix](https://github.com/PrimalHQ/primal-android-app/pull/783).

### White Noise (Versleutelde Berichten) {#white-noise}

[App-dataretentie fix](https://github.com/marmot-protocol/whitenoise/pull/890) schakelt Android auto-backup uit voor privacy. [Chat-scrollgedrag](https://github.com/marmot-protocol/whitenoise/pull/861) behoudt positie bij het lezen van geschiedenis.

### Zeus (Lightning Wallet) {#zeus}

[[NIP-47](/nl/topics/nip-47/) parallelle betalingen](https://github.com/ZeusLN/zeus/pull/3407) voor verbeterde batch-zap doorvoer.

## Best Practices voor Ontwikkelaars

**Valideer Auth Events Defensief** - go-nostr repareerde een [panic in NIP-42 validatie](https://github.com/nbd-wtf/go-nostr/pull/182) wanneer de relay-tag ontbrak. Controleer altijd op vereiste tags voordat je ze opent, zelfs in auth-flows waar je welgevormde events verwacht.

**Rate Limit op Basis van Authenticatiestatus** - khatru voegde [NIP-42 gebaseerde rate limiting](https://github.com/fiatjaf/khatru/pull/57) toe, waardoor relays verschillende limieten kunnen toepassen voor geauthenticeerde versus anonieme verbindingen. Overweeg gelaagde limieten op basis van auth-status in plaats van algemene restricties.

**Gebruik Cursor-paginering voor Lijsten** - Blossom [verving datum-gebaseerde paginering](https://github.com/hzrd149/blossom/pull/65) met cursor-gebaseerde paginering op het `/list` endpoint. Datum-gebaseerde paginering faalt wanneer items tijdstempels delen; cursors bieden betrouwbare iteratie.

**Schema-validatie voor Eventtypes** - Het [nostrability/schemata](https://github.com/nostrability/schemata) project biedt JSON-schema's voor het valideren van NIP-conforme events. Overweeg schema-validatie te integreren tijdens ontwikkeling om misvormde events te detecteren voordat ze relays bereiken.

---

Dat is het voor deze week. Bouw je iets? Heb je nieuws te delen? Wil je dat we jouw project behandelen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via NIP-17 DM</a> of vind ons op Nostr.
