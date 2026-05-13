---
title: 'Nostr Compass #21'
date: 2026-05-06
publishDate: 2026-05-06
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-06-newsletter.md
translationDate: 2026-05-13
---

Welkom terug bij Nostr Compass, uw wekelijkse gids voor Nostr.

**Deze week:** Marmot Protocol levert MDK 0.8.0 met de eerste MIP-05 notificatieprimitieven, adresseerbare NIP-51 sleutelpakketten en een aangescherpte beveiligingsreview. LaWallet NWC levert v0.10.0 als de grootste release sinds de OpenSats-financiering, met een volledig beheerdersdashboard, gebruikersportemonnee, activiteitenlog van begin tot eind en het nieuwe LightningAddress 1→N en NWCConnection-schema. Amethyst voert een Nests-stabilisatiesprint uit met eliminatie van audiogaten tijdens JWT-vernieuwing, levenscyclusbewuste sleuteldata-abonnementen, relay keep-alive herverbinding en een geanimeerde indicator voor de sprekende deelnemer. ngit levert v2.4.2 en v2.4.3 met fixes voor GRASP-serverdetectie bij PR-indieningen en filtering van multi-remote statusgebeurtenissen. GRAIN levert v0.5.4 met productieharding en een stille fix voor gegevensverlies. Mostro Core levert v0.10.1 met PGP-ondertekende release-artefacten. Clave lanceert v0.2.0 met multi-accountondersteuning op iOS.

## Hoofdverhalen

### MDK 0.8.0 voegt MIP-05 notificatieprimitieven en adresseerbare sleutelpakketten toe

MDK, de Rust-kernbibliotheek voor het Marmot-protocol, leverde v0.8.0 op 4 mei. Deze release bevat de eerste MIP-05 notificatiebouwstenen, verplaatst MIP-00 sleutelpakketten naar adresseerbare gebeurtenissen zodat het sleutelpakket van een gebruiker ter plekke kan worden vervangen, verbetert de compatibiliteit van groepen met gemengde versies, breidt UniFFI-dekking voor mobiele bindingen uit en scherpt validatiepaden aan rondom beheerdersacties, commits, opslag, versleutelingsgrenzen en replay-afhandeling. MIP-05-primitieven bevatten bladindexhelpers toegevoegd in PR #235, die downstream clients voldoende informatie geven om per-ontvanger pushnotificaties te bezorgen zonder de groepsstructuur te onthullen. PR #273 herstelt de publicatie van mdk-core op crates.io, en PR #269 onthult de test_util-module achter een test-utils Cargo-functie zodat externe clienttestsuites het testharnas van Marmot kunnen delen.

### LaWallet NWC v0.10.0 levert het volledige monorepo en gebruikersportemonnee

LaWallet NWC, de NIP-47 Nostr Wallet Connect-implementatie van het LaWallet-team, leverde v0.10.0 op 30 april. Dit is de grootste release sinds het project OpenSats-financiering ontving. Het levert het volledige monorepo, het complete beheerdersdashboard, een gebruikersportemonnee, een activiteitenlog van begin tot eind, dynamische branding en het nieuwe LightningAddress 1→N en NWCConnection-schema. De gebruikersgerichte portemonnee in PR #191 omvat onboarding, startpagina, verzenden/ontvangen, scannen, valuta's, een activiteitenfeed en een offline cache.

### Amethyst stabiliseert Nests met keep-alive, JWT-veerkracht en levenscyclusabonnementen

Amethyst, de veelzijdige Android-client, zette het NIP-53 Nests audiokamerwerk voort met een stabilisatiesprint gericht op faalwijzen die gesprekken in productie verbraken. De audiogat-fix in PR #2733 overlapt nieuwe referentieverkrijging met de actieve stream tijdens JWT-vernieuwing. Een nieuw keep-alive-mechanisme in PR #2730 verbindt verbroken relays opnieuw zonder handmatige gebruikersactie, en PR #2728 vervangt het verouderde KeyDataSourceSubscription door LifecycleAwareKeyDataSourceSubscription. PR #2724 voegt een geanimeerde buitenringindicator toe die de sprekende deelnemer benadrukt in sessies met meerdere sprekers.

### ngit v2.4.2 en v2.4.3 fixen GRASP-serverdetectie en multi-remote statusgebeurtenissen

ngit, het commandoregelgereedschap en git-plugin voor NIP-34-samenwerking, leverde v2.4.2 op 28 april en v2.4.3 op 1 mei. v2.4.2 repareert een URL-normalisatiemismatch waarbij repo_grasps genormaliseerde hostnamen bevatte maar de vergelijking plaatsvond met volledige kloon-URL's. v2.4.3 repareert een statusgebeurtenisambiguïteit die optrad wanneer een repository meerdere nostr://-remotes heeft met dezelfde identifier.

### GRAIN v0.5.4 brengt productieharding en een stille fix voor gegevensverlies

GRAIN, de op Go gebaseerde Nostr-relay en clientbibliotheek, leverde v0.5.4 op 30 april. De release bundelt zes geaccumuleerde fixes sinds v0.5.3, waaronder een stil gegevensverliesbug in de Docker-snelstart die eerder gebeurtenissen verwierp wanneer de container herstartte, en een opslaglaag-correctheidbug in adresseerbare gebeurtenislezingen.

### Mostro Core v0.10.1 voegt PGP-ondertekende release-artefacten toe

Mostro Core, de Rust-bibliotheek die peer-to-peer-functionaliteit levert voor de Mostro-daemon, leverde v0.10.1 op 28 april. De nieuwe release voegt PGP-ondertekende release-artefacten en een release-verificatiestroom toe zodat downstream-packagers de artefactherkomst kunnen bevestigen.

## Releases

### Clave v0.2.0 lanceert multi-account op iOS met NIP-46 (Nostr Connect) ondertekening

Clave, de iOS NIP-46 remote signing-app, leverde v0.2.0 op 5 mei. De grootste update introduceert multi-accountondersteuning: Clave kan nu tot vier accounts op één apparaat bewaren, met een éénklik-wisselaar en per-accountisolatie. PR #23 voegt de iOS-loodgieterij toe voor multi-account, en PR #22 voegt een signer_pubkey-veld toe aan de APNs-lading zodat het apparaat weet bij welk account een remote ondertekeningsverzoek hoort.

### Wisp levert v1.0.3 → v1.0.5 stabiliteitswerk

Wisp, de Android-client, leverde v1.0.3, v1.0.4 en v1.0.5 op 4 mei met stabiliteitswerk. PR #506 voegt Thumbhash toe voor wazige afbeeldingsvoorbeelden terwijl volledige media laadt, en PR #514 vermindert haperingen bij het wisselen van onderste tabbladen.

### Amber 6.1.0-pre1 levert layout- en stabiliteitsfixes

Amber, de Android-ondertekeningsapp voor NIP-55 en NIP-46, leverde v6.1.0-pre1 met een layoutpass op de nieuwe app-verbindingsstroom en diverse crashfixes. PR #416 repareert ActivityStatsBar-layout en tekstoverloopproblemen.

### Routstr Core v0.4.3 verbetert betaling, terugbetaling en gebruiksrapportage

Routstr Core leverde v0.4.3 als pre-release op 1 mei met verbeteringen in betaling- en terugbetalingsafhandeling, kostentracking en gebruiksrapportage.

### Nostria v3.1.37 t/m v3.1.41 voegen webbladwijzers en een automatisch thema toe

Nostria, de multi-platform Nostr-client, leverde v3.1.37 t/m v3.1.41 met NIP-B0 webbladwijzerondersteuning, een automatisch thema dat apparaatinstellingen volgt en in-app PDF-weergave.

### NoorNote v0.8.9 repareert leeg scherm bij eerste start op desktop

NoorNote leverde v0.8.9 op 28 april en repareert een leegscherm-bug bij de eerste start van de desktopapp.

### Kubo v0.3.4 t/m v0.4.1 lanceren een kindveilig Nostr-videoplatform met ouderlijk toezicht en Web of Trust-feedcuratie

Kubo, een kindveilig videoplatform op Nostr, leverde v0.3.4 t/m v0.4.1 op 4 en 5 mei. Elk kind krijgt een apart Nostr-sleutelpaar en een videogericht feed waarbij ouders tijdslimieten (15 tot 180 minuten per dag), toegestane tijdvensters en zichtbaarheid van plaatsingsacties beheren.

## Niet-uitgebrachte wijzigingen

### Sprout levert Desktop v0.0.4 en v0.0.5 naast NIP-OA agentauthenticatie en de pair-relay sidecar

Sprout, Block's Nostr-client met ingebouwde relay, leverde Desktop v0.0.4 op 5 mei en v0.0.5 op 6 mei. PR #471 koppelt NIP-OA agentauthenticatie aan de NIP-43 lidmaatschapsstroom van de relay zodat een autonome agent kan bewijzen dat een specifieke menselijke publieke sleutel zijn acties heeft geautoriseerd. Een nieuwe tijdelijke sidecar-relay voor NIP-AB apparaatkoppeling arriveeert in PR #467 als sprout-pair-relay.

### nostream voegt Marmot-relayondersteuning en NIP-25-reacties toe

nostream, de Node.js relay-implementatie, fuseerde Marmot Protocol-relayondersteuning voor MIPs 00 t/m 03 in PR #602, NIP-25-reactieondersteuning in PR #589 en geohash-prefixmatching voor #g-filters in PR #586.

### strfry voegt per-verbinding observeerbaarheid toe en verlaagt nofiles-plafond

strfry, de C++ Nostr-relay, fuseerde 14 PR's gericht op observeerbaarheid. PR #218 voegt per-verbinding observeerbaarheid van uitstaande uitgaande berichten en een configureerbaar tegendrukplafond toe. PR #224 verwijdert std::function heap-allocaties uit de per-gebeurtenismonitor-fanout.

### Damus vervangt Tenor-GIF's door een Purple-proxy en levert compressie-UX

Damus fuseerde PR #3737 dat de Tenor GIF-integratie vervangt door een Damus Purple-proxy.

### Primal Android polijst Verkennen, meldingen en de NIP-05 geverifieerde badge

Primal Android fuseerde PR #1043 dat een knipperende NIP-05 geverifieerde badge repareert voor gebruikers met _@domein-identifiers.

### Alby Hub voegt NWC-betalingen toe vanuit appverbindingen

Alby Hub fuseerde PR #2267 waarmee betalingen vanuit appverbindingen mogelijk worden.

### routstrd-auth: een gedocker­iseerde Routstrd voor teams met NIP-98-auth en npub RBAC

routstrd-auth, aangemaakt op 27 april, is een gedockeriseerde variant van Routstrd voor multi-gebruiker teamimplementaties met op npub gebaseerde rolgebaseerde toegangscontrole en NIP-98 HTTP-authenticatie.

### Routstrd integreert Hermes voor daemonclients en externe modus

Routstrd fuseerde PR #22 die integratie met Hermes Agent toevoegt zodat het configuratiebestand van de agent gevuld wordt met modelleveranciers en API-sleutels die Routstrd via Nostr ontdekt.

### whitenoise-rs levert per-account database-isolatie en voorstelupgrades

whitenoise-rs fuseerde PR #796 dat berichtprojectietabellen naar per-account databases verplaatst, en PR #791 voegt voorstelupgrades toe zodat groepen functionaliteit kunnen uitbreiden met nieuwe voorsteltypes.

### Angor 0.2.21 levert compacte appstromen naast sleutelleverancier- en netwerkswitchharding

Angor leverde 0.2.21 op 6 mei met verbeteringen in mobiel ontwerpprestaties, compacte appstromen en een veilige sleutelleverancier.

## Nieuw gevolgd en ontdekt

### BitMacro Signer: een zelf te hosten NIP-46 bunker met client-side sleutelversleuteling

BitMacro Signer is een zelf te hosten Nostr-ondertekeningsgereedschap met het NIP-46 bunkermodel. Sleutels worden aan de clientzijde versleuteld vóór opslag zodat de server nooit platte tekst bezit.

NIP-34 repository-ontdekking leverde deze week 26 nieuwe repository-aankondigingen op, waarvan vier opvallen:

### gnostr: een git-implementatie gebouwd direct op Nostr

gnostr is een git-implementatie gebouwd direct op Nostr, met eigen werktreeopdrachten als een from-scratch Nostr-native versiebeheerclient.

### nostr-archive: een inhoudsgeadresseerde archiefspecificatie op Nostr en Blossom

nostr-archive is een conceptspecificatie en referentie-implementatie voor inhoudsgeadresseerde archieven op Nostr en Blossom.

### flower-cache: een lokale Blossom-cacheserver

flower-cache is een lokale Blossom-cacheserver, nuttig voor clients die een warme lokale spiegel willen van de blobset van een externe Blossom-server.

### micro-vpn-ansible: Ansible-playbooks voor VPN-implementatie via NIP-34

micro-vpn-ansible is een kleine verzameling Ansible-playbooks voor het implementeren van een micro-VPN, gehost als een NIP-34 repository.

## Protocolwerk

### NIP-updates

- Een makelaarsloze hashratemarkt via Nostr (conceptvoorstel): Anoniem concept-NIP dat stelt dat huidige hashratemarktspelers bewaarnemende makelaars zijn die gebruikers KYC-screenen. Stelt een P2P-hashratemarkt op Nostr-gebeurtenissen voor.
- Curated Feeds: een eenvoudiger alternatief voor DVM-feeds (conceptvoorstel): Betoogt dat NIP-90 DVM's te zwaar zijn voor eenvoudige feedcuratie; stelt in plaats daarvan dunne adresseerbare gebeurtenissen met geordende lijsten van gebeurtenis-ID's voor.
- Profile Colors: deterministische visuele identiteit (conceptvoorstel): Nieuw NIP-concept voor het afleiden van deterministische leesbare kleuren van een Nostr-publieke sleutel voor consistente visuele identiteit over clients heen.
- Namecoin-Track NIPs: identiteit, relays, TLS en reputatie verankeren (conceptcluster): Een cluster van concept-NIP's dat Nostr-stackonderdelen naar Namecoin-verankerde records verplaatst.

## NIP-diepteduik: NIP-34 (git stuff)

NIP-34 definieert gebeurtenissoorten voor het hosten van git-repositories, patches, pull requests, issues en samenvoegstatus op Nostr-relays. Een repository wordt aangekondigd als een adresseerbare gebeurtenis van soort 30617. Patches gebruiken soort 1617 met git format-patch-uitvoer. Pull requests gebruiken soort 1618. Issues gebruiken soort 1621 met markdown-inhoud. Statusgebeurtenissen verplaatsen een thread tussen Open (1630), Applied/Merged of Resolved (1631), Closed (1632) en Draft (1633). Het NIP-34-verhaal deze week is hetzelfde als de GitWorkshop v2-lancering van vorige week: de PR-samenvoegknop in de browser werkt omdat GRASP-servers, ngit en het nostr://-kloon-URL-schema samen de lus sluiten op een volledig gedecentraliseerde forge.

## NIP-diepteduik: NIP-53 (Live Activities)

NIP-53 definieert het standaard gebeurtenisoppervlak voor live-activiteiten op Nostr: livestreams, persistente vergaderruimten, geplande conferentie-evenementen, aanwezigheid van luisteraars en live chat. Een livestream wordt aangekondigd als een adresseerbare gebeurtenis van soort 30311. NIP-53 scheidt de persistente ruimte van de geplande gebeurtenis die daarbinnen plaatsvindt: een soort 30312 Meeting Space definieert een ruimte, en een soort 30313 Conference Event vertegenwoordigt een geplande of lopende vergadering in die ruimte. Het Nostr live-activiteitsoppervlak is opzettelijk smal: NIP-53 kondigt de activiteit aan, terwijl andere NIP's aangrenzende zaken afhandelen zoals zaps (NIP-57), zapdoelen (NIP-75) en video-opnames (NIP-71).

---

Dat is het voor deze week. Als u iets bouwt of nieuws wilt delen, stuur ons een DM op Nostr of bezoek nostrcompass.org.
