---
title: 'Nostr Kompas #2'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
---

Welkom terug bij Nostr Kompas, je wekelijkse gids voor het Nostr-protocol ecosysteem.

**Deze week:** Drie [NIP-55](/nl/topics/nip-55/) signer-implementaties krijgen updates: Amber voegt prestatiecaching toe, Aegis krijgt `nostrsigner:` URI-ondersteuning, en Primal Android voegt zich bij hen als volledige lokale signer. Shopstr introduceert "Zapsnags" voor flash-verkopen via zaps. Mostro voegt een ontwikkelingsfonds toe. Vier NIP-updates landen, waaronder Public Messages (kind 24) en verbeteringen in groepsprivacy. NDK cache-queries worden 162x sneller, Applesauce voegt reacties en NIP-60 wallet-ondersteuning toe, en Tenex introduceert RAL-architectuur voor AI-agent delegatie. In onze deep dive leggen we [NIP-02](/nl/topics/nip-02/) (volglijsten) en [NIP-10](/nl/topics/nip-10/) (reply threading) uit, fundamentele specificaties voor het bouwen van sociale tijdlijnen en gesprekken.

## Nieuws {#news}

**Primal Android Wordt een NIP-55 Signer** - Voortbouwend op de [Nostr Connect ondersteuning](/nl/newsletters/2025-12-17-newsletter/#primal-android) van vorige week, heeft Primal volledige lokale ondertekeningscapaciteiten geïmplementeerd via acht samengevoegde pull requests. De implementatie omvat een complete `LocalSignerContentProvider` die ondertekeningsbewerkingen blootstelt aan andere Android-apps via Android's content provider interface, volgens de [NIP-55](/nl/topics/nip-55/) specificatie. De architectuur scheidt verantwoordelijkheden netjes: `SignerActivity` handelt gebruikersgerichte goedkeuringsflows af, `LocalSignerService` beheert achtergrondbewerkingen, en een nieuw permissiesysteem laat gebruikers bepalen welke apps handtekeningen kunnen aanvragen. Dit maakt Primal een levensvatbaar alternatief voor Amber voor Android-gebruikers die hun sleutels in één app willen houden terwijl ze anderen gebruiken voor verschillende Nostr-ervaringen.

**Shopstr Zapsnags: Flash-verkopen via Lightning** - De Nostr-native marktplaats introduceerde ["Zapsnags"](https://github.com/shopstr-eng/shopstr/pull/211), een flash-verkoop functie waarmee kopers items direct vanuit hun sociale feed kunnen kopen met een enkele zap. De implementatie filtert kind 1 nota's getagd met `#shopstr-zapsnag` en rendert ze als productkaarten met een "Zap om te Kopen" knop in plaats van de standaard winkelwagen-flow. Wanneer een koper zapt, genereert het systeem een betalingsverzoek met behulp van [NIP-57](/nl/topics/nip-57/), pollt voor de kind 9735 zap-ontvangst om betaling te bevestigen, en versleutelt vervolgens verzendinformatie met [NIP-17](/nl/topics/nip-17/) gift wrapping voordat het privé naar de verkoper wordt gestuurd. De functie slaat kopergegevens lokaal op voor herhaalaankopen en bevat een handelarendashboard voor het maken van flash-verkoopvermeldingen. Het is een slimme combinatie van sociale, betalings- en privacy-primitieven die laat zien hoe Nostr's componeerbare ontwerp nieuwe handelspatronen mogelijk maakt.

**Mostro Introduceert Ontwikkelingsfonds** - De [NIP-69](/nl/topics/nip-69/) P2P Bitcoin-handelsbot [implementeerde configureerbare ontwikkelingskosten](https://github.com/MostroP2P/mostro/pull/555) om duurzaam onderhoud te ondersteunen. Operators kunnen `dev_fee_percentage` instellen tussen 10-100% van de Mostro-handelskosten (standaard 30%), die automatisch worden doorgestuurd naar een ontwikkelingsfonds bij elke succesvolle transactie. De implementatie voegt drie databasekolommen toe (`dev_fee`, `dev_fee_paid`, `dev_fee_payment_hash`) om bijdragen bij te houden en valideert het percentage bij daemon-opstart. Technische documentatie in [`docs/DEV_FEE.md`](https://github.com/MostroP2P/mostro/blob/main/docs/DEV_FEE.md) legt het systeem uit. Dit opt-in model laat operators lopende ontwikkeling ondersteunen met behoud van volledige transparantie over kostenallocatie.

## NIP Updates {#nip-updates}

Recente wijzigingen in de [NIPs repository](https://github.com/nostr-protocol/nips):

**Nieuwe NIPs:**
- **[NIP-A4](/nl/topics/nip-a4/) (Public Messages, kind 24)** - Een nieuwe kind voor notificatiescherm-berichten ontworpen voor brede client-ondersteuning ([#1988](https://github.com/nostr-protocol/nips/pull/1988)). In tegenstelling tot threaded gesprekken hebben deze berichten geen concept van chatgeschiedenis of berichtketens. Ze gebruiken `q` tags (citaten) in plaats van `e` tags om threading-complicaties te vermijden, waardoor ze ideaal zijn voor eenvoudige openbare notificaties die in de notificatiefeed van een ontvanger verschijnen zonder gespreksstatus te creëren.

**Significante Wijzigingen:**
- **[NIP-29](/nl/topics/nip-29/)** - Grote verduidelijking van groepssemantiek ([#2106](https://github.com/nostr-protocol/nips/pull/2106)). De `closed` tag betekent nu "kan niet schrijven" (alleen-lezen voor niet-leden), losgekoppeld van join-mechanica. Een nieuwe `hidden` tag voorkomt dat relays metadata of ledenevents serveren aan niet-leden, waardoor echt privégroepen mogelijk zijn die niet ontdekt kunnen worden zonder out-of-band uitnodiging. De `private` tag controleert berichtzichtbaarheid terwijl publieke metadata nog steeds mogelijk is voor ontdekking.
- **[NIP-51](/nl/topics/nip-51/)** - Kind 30006 toegevoegd voor gecureerde fotosets ([#2170](https://github.com/nostr-protocol/nips/pull/2170)), volgens het patroon van 30004 (artikelen) en 30005 (video's). Al geïmplementeerd in Nostria.
- **[NIP-55](/nl/topics/nip-55/)** - Verduidelijkte verbindingsinitiatie voor Android signers ([#2166](https://github.com/nostr-protocol/nips/pull/2166)). Ontwikkelaars die multi-gebruiker sessies implementeerden misbruikten `get_public_key` door het aan te roepen vanuit achtergrondprocessen. De bijgewerkte specificatie raadt aan om het slechts eenmaal aan te roepen tijdens initiële verbindingsopstelling, waarmee een veelvoorkomende implementatiefout wordt voorkomen.

## NIP Diepgaand: NIP-02 en NIP-10 {#nip-deep-dive-nip-02-and-nip-10}

Deze week behandelen we twee NIPs die essentieel zijn voor sociale functionaliteit: hoe clients weten wie je volgt en hoe gesprekken worden gethreadd.

### [NIP-02](/nl/topics/nip-02/): Volglijst

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md) definieert kind 3 events, die je volglijst opslaan. Dit eenvoudige mechanisme voedt de sociale graaf die tijdlijnen mogelijk maakt.

**Structuur:** Een kind 3 event bevat `p` tags die gevolgde pubkeys opsommen:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Elke `p` tag heeft vier posities: de tagnaam, de gevolgde pubkey (hex), een optionele relay URL-hint, en een optionele "petname" (een lokale bijnaam). De relay-hint vertelt andere clients waar ze de events van die gebruiker kunnen vinden. De petname laat je gedenkwaardige namen toewijzen aan contacten zonder te vertrouwen op hun zelf-gedeclareerde weergavenamen.

**Vervangbaar gedrag:** Kind 3 valt in het vervangbare bereik (0, 3, 10000-19999), dus relays houden alleen de laatste versie per pubkey bij. Wanneer je iemand nieuws volgt, publiceert je client een volledig nieuw kind 3 dat al je volgers bevat plus de nieuwe. Dit betekent dat volglijsten elke keer compleet moeten zijn; je kunt geen incrementele updates publiceren.

**Tijdlijnen bouwen:** Om een home-feed te construeren, haalt de client het kind 3 van de gebruiker op, extraheert alle `p` tag pubkeys, en abonneert zich dan op kind 1 events van die auteurs:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

De relay retourneert overeenkomende nota's en de client rendert ze. De relay-hints in kind 3 helpen clients te weten welke relays te bevragen voor elke gevolgde gebruiker.

**Petnames en identiteit:** Het petname-veld maakt een gedecentraliseerd naamgevingsschema mogelijk. In plaats van te vertrouwen op welke naam een gebruiker ook claimt in hun profiel, kun je je eigen label toewijzen. Een client zou kunnen weergeven "alice (Mijn Zus)" waar "alice" komt van haar kind 0 profiel en "Mijn Zus" is je petname. Dit biedt context die globale gebruikersnamen niet kunnen bieden.

**Praktische overwegingen:** Omdat kind 3 events vervangbaar zijn en compleet moeten zijn, moeten clients onbekende tags behouden bij het updaten. Als een andere client tags heeft toegevoegd die jouw client niet begrijpt, zou blind overschrijven die data verliezen. Voeg nieuwe volgers toe in plaats van helemaal opnieuw te bouwen.

### [NIP-10](/nl/topics/nip-10/): Tekstnota Threading

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) specificeert hoe kind 1 nota's naar elkaar verwijzen om reply-threads te vormen. Dit begrijpen is essentieel voor het bouwen van gespreksweergaven.

**Het probleem:** Wanneer iemand reageert op een nota, moeten clients weten: Waarop is dit een reactie? Wat is de root van het gesprek? Wie moet genotificeerd worden? NIP-10 beantwoordt deze vragen via `e` tags (event-referenties) en `p` tags (pubkey-vermeldingen).

**Gemarkeerde tags (voorkeur):** Moderne clients gebruiken expliciete markers in `e` tags:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Goed punt! Ik ben het ermee eens.",
  "sig": "b7d3f..."
}
```

De `root` marker wijst naar de originele nota die de thread startte. De `reply` marker wijst naar de specifieke nota die wordt beantwoord. Als je direct reageert op de root, gebruik alleen `root` (geen `reply` tag nodig). Het onderscheid is belangrijk voor rendering: de `reply` bepaalt inspringing in een threadweergave, terwijl `root` alle replies groepeert.

**Threading-regels:**
- Directe reply naar root: Eén `e` tag met `root` marker
- Reply op een reply: Twee `e` tags, één `root` en één `reply`
- De `root` blijft constant door de thread; `reply` verandert op basis van waarop je reageert

**Pubkey tags voor notificaties:** Neem `p` tags op voor iedereen die genotificeerd moet worden. Minimaal, tag de auteur van de nota waarop je reageert. Conventie is om ook alle `p` tags van het parent-event op te nemen (zodat iedereen in het gesprek op de hoogte blijft), plus alle gebruikers die je @vermeldt in je content.

**Relay-hints:** De derde positie in `e` en `p` tags kan een relay URL bevatten waar dat event of de content van die gebruiker gevonden kan worden. Dit helpt clients de gerefereerde content op te halen zelfs als ze niet verbonden zijn met de originele relay.

**Verouderde positionele tags:** Vroege Nostr-implementaties leidden betekenis af uit tagpositie in plaats van markers: eerste `e` tag was root, laatste was reply, middelste waren vermeldingen. Deze aanpak is verouderd omdat het ambiguïteit creëert. Als je `e` tags ziet zonder markers, zijn ze waarschijnlijk van oudere clients. Moderne implementaties moeten altijd expliciete markers gebruiken.

**Threadweergaven bouwen:** Om een thread weer te geven, haal het root-event op, vraag dan alle events op met een `e` tag die naar die root verwijst:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Sorteer resultaten op `created_at` en gebruik `reply` markers om de boomstructuur te bouwen. Events waarvan de `reply` naar de root wijst zijn top-level replies; events waarvan de `reply` naar een andere reply wijst zijn geneste antwoorden.

## Releases {#releases}

**Zeus v0.12.0** - Voortbouwend op de [NWC parallelle betalingen ondersteuning](/nl/newsletters/2025-12-17-newsletter/#zeus) van vorige week, levert de [grote release](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0) van de Lightning wallet een complete [NIP-47](/nl/topics/nip-47/) Nostr Wallet Connect service met aangepaste relay-ondersteuning en budgettracking. Een [budget-herlaad fix](https://github.com/ZeusLN/zeus/pull/3455) zorgt ervoor dat verbindingen huidige limieten gebruiken. [Lightning adres kopiëren](https://github.com/ZeusLN/zeus/pull/3460) bevat niet langer het `lightning:` prefix, wat plakproblemen in Nostr-profielvelden repareert.

**Amber v4.0.6** - De Android [NIP-55](/nl/topics/nip-55/) signer [voegt prestatiecaching toe](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6) aan ondertekeningsbewerkingen en verbetert foutafhandeling bij het decrypten van misvormde content. Verbindingsbetrouwbaarheid verbeterd met retry-logica voor relay connect events, en verschillende crashfixes pakken edge cases aan rond ongeldige `nostrconnect://` URI's en permissiescherm-interacties.

**nak v0.17.3** - De nieuwste release van de commandoregel Nostr-tool [beperkt LMDB builds tot Linux](https://github.com/fiatjaf/nak/releases/tag/v0.17.3), wat cross-platform compilatieproblemen repareert.

**Aegis v0.3.4** - De cross-platform Nostr signer [voegt ondersteuning toe](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4) voor het `nostrsigner:` URI-schema gedefinieerd in [NIP-55](/nl/topics/nip-55/), overeenkomend met Amber's verbindingsflow. Lokale relay-data kan nu worden geïmporteerd en geëxporteerd voor backup, en de release bevat bugfixes voor relay socket-fouten en UI-verbeteringen aan de lokale relay-interface.

## Noemenswaardige code- en documentatiewijzigingen {#notable-code-and-documentation-changes}

*Dit zijn open pull requests en werk in vroeg stadium, perfect om feedback te krijgen voordat ze worden samengevoegd. Als iets je aandacht trekt, overweeg om te reviewen of te reageren!*

### Damus (iOS) {#damus}

[Mute-lijst persistentie](https://github.com/damus-io/damus/pull/3469) repareert een probleem waarbij mute-lijsten werden gewist bij koude start. De fix voegt guards toe om onbedoelde overschrijvingen tijdens app-initialisatie te voorkomen. [Profiel stream timing](https://github.com/damus-io/damus/pull/3457) elimineert een vertraging van ~1 seconde voordat gecachte profielen verschenen. Voorheen wachtten weergaven op abonnementstaken om te herstarten; nu levert `streamProfile()` onmiddellijk gecachte data van NostrDB, waardoor het venster verdwijnt waarin afgekorte pubkeys en placeholder-afbeeldingen werden getoond.

### White Noise (Versleutelde Berichten) {#white-noise}

[Real-time berichtenstreaming](https://github.com/marmot-protocol/whitenoise/pull/919) vervangt het vorige polling-mechanisme met een stream-gebaseerde architectuur. De nieuwe `ChatStreamNotifier` consumeert de berichtenstream van de Rust SDK direct, handhaaft chronologische volgorde en handelt incrementele updates efficiënt af. Testen toonden significante verbetering in responsiviteit. Een [chat-lijst API](https://github.com/marmot-protocol/whitenoise/pull/921) voegt `get_chat_list` toe voor het ophalen van gesprekssamenvattingen, en een [stabiele sorteer-fix](https://github.com/marmot-protocol/whitenoise/pull/905) voorkomt berichtherschikkingslussen door `createdAt` met bericht-ID als tiebreaker te gebruiken.

### NDK (Bibliotheek) {#ndk}

Twee pull requests leverden dramatische cache-prestatieverbeteringen. [PR #371](https://github.com/nostr-dev-kit/ndk/pull/371) repareerde een bug waarbij events gelezen uit SQLite-cache onmiddellijk terug werden geschreven, wat 100% duplicate writes veroorzaakte bij app-boot. De fix voegt een `fromCache` guard toe en implementeert O(1) duplicaatcontrole via een in-memory Set. Voor kleine resultaatsets (<100 events) vervangt directe JSON-overdracht binaire encoding-overhead. [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372) verwijderde onnodige `seenEvent` calls voor gecachte events. De LRU cache lookup kostte 0.24-0.64ms per event; voor 5.700 gecachte events voegde dit ~1.4 seconden overhead toe. Resultaat: cache-queries daalden van ~3.690ms naar ~22ms (162x sneller).

### rust-nostr (Bibliotheek) {#rust-nostr}

[Multi-filter REQ ondersteuning](https://github.com/rust-nostr/nostr/pull/1176) werd hersteld na verwijdering in een eerdere refactor. De SDK accepteert weer `Vec<Filter>` voor abonnementsverzoeken, wat efficiënte queries mogelijk maakt die meerdere filtervoorwaarden combineren met OR-logica. [Relay-herkomst](https://github.com/rust-nostr/nostr/pull/1156) werd toegevoegd aan `stream_events*` methodes, zodat elk gestreamd event nu de `RelayUrl` bevat waar het vandaan kwam en een `Result` die succes of falen aangeeft, nuttig voor het volgen van relay-betrouwbaarheid en debugging van verbindingsproblemen. Een [beveiligingsfix](https://github.com/rust-nostr/nostr/pull/1179) verwijderde de `url-fork` dependency na RUSTSEC-2024-0421, wat een bekende kwetsbaarheid elimineert.

### Applesauce (Bibliotheek) {#applesauce}

De TypeScript-bibliotheek die [noStrudel](https://github.com/hzrd149/nostrudel) aandrijft zag significante ontwikkeling deze week. Nieuwe modellen omvatten een [reactiesysteem](https://github.com/hzrd149/applesauce) en gebruikersgroepen casting. Wallet-functionaliteit breidde uit met NIP-60 ondersteuning, een verzend-tab en verbeterde token-recovery tools. Een nieuwe `user.directMessageRelays$` property onthult DM relay-configuratie. Alle acties werden gerefactored om async interfaces te gebruiken (async generators verwijderd), en bugfixes pakten versleutelde content-herstel en tijd-gebaseerde event-filter edge cases aan.

### Tenex (AI Agents) {#tenex}

Het [multi-agent coördinatiesysteem](https://github.com/tenex-chat/tenex) gebouwd op Nostr introduceerde RAL (Request-Action-Lifecycle) architectuur in [vijf samengevoegde PRs](https://github.com/pablof7z/tenex/pull/38). RAL stelt agents in staat om te pauzeren bij het delegeren van taken en te hervatten wanneer resultaten binnenkomen, met gespreks-gebaseerde state-persistentie. Delegatie-tools (`delegate`, `ask`, `delegate_followup`, `delegate_external`) publiceren nu Nostr events en retourneren stop-signalen in plaats van te blokkeren. De refactor omvat AI SDK v6 migratie, VCR-testinfrastructuur voor deterministische LLM-interactie recording, en multimodale afbeeldingsondersteuning.

---

Dat is het voor deze week. Bouw je iets? Heb je nieuws te delen? Wil je dat we jouw project behandelen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via NIP-17 DM</a> of vind ons op Nostr.
