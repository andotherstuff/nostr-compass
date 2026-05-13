---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-13-newsletter.md
translationDate: 2026-05-13
---

Welkom terug bij Nostr Compass, uw wekelijkse gids voor de ontwikkeling van het Nostr-protocol.

**Deze week:** Nostr VPN brengt acht releases uit in zeven dagen, van een opnieuw ontworpen apparaatkoppelingsflow tot een FIPS AEAD-wissel die de TCP-doorvoer ruwweg verdubbelt. Marmot Protocol (de basis voor White Noise) brengt een frontend-release uit die de gebruikersblokkering voltooit en 31 samengevoegde PR's over MDK en de backend. Grain brengt v0.6.0 uit met vier nieuwe NIP-implementaties in één mijlpaal. Citrine brengt v3.0.0-pre1 uit met ingebouwde Tor en relay-aggregatie. Amber brengt v6.1.0-pre2 uit met verbeteringen in de verbindingsflow en ondertekening. Alby Hub brengt v1.22.2 uit met een AI en Agents-pagina en Core Lightning-integratie. Mostro brengt gelijktijdige taker bonds en mostro-core v0.11.0 uit. Jumble brengt vijf releases uit met recente zoekgeschiedenis en fixes voor het bewaren van accountgegevens. Nostrord brengt drie releases uit met groepsdeelvensters en Arch Linux-pakketten. Flotilla brengt 1.8.0 uit met videogesprekken, e-mailweergave en kamerverwijzingen. Calendar by Formstr brengt v1.5.1 uit met afspraakplanning en Android-kalendersynchronisatie. Tamagostrich lanceert een gedecentraliseerde NIP-78 Tamagotchi met sats-beloningen.

## Hoofdverhalen

### Nostr VPN brengt acht releases uit die culmineren in v4.0.10

Nostr VPN, het op Rust gebaseerde gedecentraliseerde mesh-VPN dat Nostr gebruikt voor peer-discovery, bracht acht releases uit van v4.0.1 tot v4.0.10 voor macOS, Linux, Windows en Android. De belangrijkste wijziging in v4.0.8: de AEAD werd gewisseld van de RustCrypto chacha20poly1305 soft backend naar BoringSSL's ChaCha20-Poly1305 in ring 0.17, dat gebruik maakt van handmatig afgestemde NEON op aarch64 en AVX2/AVX-512 op x86_64. Docker-benchmarks op identieke hardware toonden een directe TCP-doorvoer van 2-knooppunten die sprong van 437 naar 1097 Mbps. v4.0.9 voegde sendmmsg(2)-batching toe op het UDP-verzendpad, waardoor de TCP-enkelvoudige stroom steeg van 1066 naar 1548 Mbps (1,45×). v4.0.10 bracht een volledige UX-revisie voor apparaatkoppeling.

### Marmot / White Noise brengt frontend-release uit die gebruikersblokkering voltooit en 31 samengevoegde PR's over MDK en backend

White Noise bracht v2026.5.7+24 uit op 7 mei, waarmee de blokkeerfeatureset wordt voltooid. Een geblokkeerde gebruiker is nu verborgen in uitnodigingen, chatvoorbeelden, berichttijdlijnen, zoekresultaten en meldingen, en hun berichten tellen niet meer mee voor ongelezen badges. MDK landde PR #258 met het extensie v3-draadformaat en het disappearing_message_secs-schema, waarmee de basis wordt gelegd voor verdwijnende berichten.

### Grain v0.6.0 voegt NIP-40, NIP-50, NIP-70 en NIP-45 toe

Grain bracht v0.6.0 uit op 6 mei met vier nieuwe NIP-implementaties. NIP-40 event-vervaldatum laat uitgevers een vervaltijdstempel instellen zodat de relay events verwijdert nadat ze vervallen. NIP-50 volledige tekstzoekopdracht laat clients zoekfilters uitsturen in REQ-berichten. NIP-70 beschermde events voorkomt dat relays events opnieuw delen zonder expliciete toestemming van de auteur. NIP-45 telquery's laten clients een relay vragen om een telling van overeenkomende events te retourneren.

## Deze week verschenen

### Citrine v3.0.0-pre1 brengt ingebouwde Tor en relay-aggregatie

Citrine bracht v3.0.0-pre1 uit met ingebouwde Tor-ondersteuning voor privacybesparende relay-toegang en relay-aggregatie, waarbij Citrine events kan ophalen uit meerdere upstream-relays en ze kan bedienen aan lokale clients. PR #139 voegt NIP-77 (Negentropy Reconciliation)-ondersteuning toe voor efficiënte set-reconciliatie-gebaseerde eventsynchronisatie.

### Amber v6.1.0-pre2 verbetert de nieuwe app-verbindingsflow

Amber bracht v6.1.0-pre2 uit. De belangrijkste fixes: het ondertekeningsvenster sluit nu correct na het accepteren van een bunker-verzoek, misvormde bunker-verzoeken tonen een scherm voor ongeldig verzoek, en snelheidsbegrenzing wordt toegevoegd voor op intent gebaseerde ondertekeningsverzoeken.

### Alby Hub v1.22.2 voegt AI en Agents-pagina en Core Lightning-ondersteuning toe

Alby Hub bracht v1.22.2 uit. De nieuwe AI en Agents-pagina stelt de Lightning- en NWC-mogelijkheden van Alby Hub beschikbaar aan AI-agents en MCP-compatibele tools. Core Lightning (CLN) is nu een ondersteunde backend naast LND en LDK.

### Mostro brengt gelijktijdige taker bonds en mostro-core v0.11.0 uit

Mostro voegde 11 PR's samen voor de taker bond-feature. PR #733 implementeert gelijktijdige taker bonds waarbij meerdere takers tegelijkertijd bond-facturen kunnen indienen en de eerste die vergrendelt wint. mostro-core bracht v0.11.0 uit met PR #144 die Action::PayBondInvoice en Status::WaitingTakerBond toevoegt. mostro-cli bracht v0.15.0 uit.

### Jumble brengt vijf releases uit met recente zoekfunctie en accountpersistentie

Jumble bracht v26.5.2 tot en met v26.5.6 uit. v26.5.5 voegt recente zoekgeschiedenis toe. Een kritieke persistentiebug is opgelost in v26.5.6: accounts en gecachte gegevens overleven nu een volledig opnieuw starten van de app.

### Nostrord brengt groepsdeelvensters, media-upload en Arch Linux-pakketten uit

Nostrord bracht v1.0.0, v1.0.1 en v1.0.2 uit. v1.0.1 brengt Arch Linux-pakketten via AUR als nostrord-bin met PGP-ondertekende artefacten, een knop om naar het laatste bericht te springen, en afbeeldingen/media plakken in chat. v1.0.2 voegt groepsdeling toe via PR #49 met een deelvenster dat zowel een nostr:naddr URI als een nostrord.com/open/-link genereert.

### FIPS v0.3.0 brengt platformoverschrijdend bereik, Nostr peer-discovery en een gateway voor ongewijzigde LAN's

FIPS bracht v0.3.0 uit, een belangrijke mijlpaal die uitbreidt van alleen Linux naar Linux, macOS, Windows en OpenWrt. Knooppunten publiceren nu ondertekende overlay-advertenties als kind:37195 geparametriseerde vervangbare events op publieke Nostr-relays. Dezelfde ring 0.17 ChaCha20-Poly1305-wissel die de Nostr VPN-doorvoersprong aandreef, landt ook in FIPS v0.3.0.

### Camelus v1.10.1 brengt desktopbuilds uit

Camelus bracht v1.10.1 uit met Windows- en Linux-desktopbuilds, waarmee de distributie wordt uitgebreid van alleen mobiel.

### Flotilla 1.8.0 brengt videogesprekken, e-mailweergave en kamerverwijzingen uit

Flotilla bracht 1.8.0 uit. Spraakkamers ondersteunen nu video: deelnemers kunnen camera's aanzetten of hun scherm delen tijdens een gesprek. E-mailweergave arriveert via een update van de welshman-bibliotheek. Kamerverwijzingen laten gebruikers andere kamers en relays verwijzen met klikbare inline-links.

### Calendar by Formstr brengt v1.5.1 uit met afspraakplanning en Android-kalendersynchronisatie

Calendar by Formstr bracht v1.5.0 uit op 10 mei en v1.5.1 op 11 mei. Afspraakplanning laat gebruikers boekbare tijdslots aanmaken. Alleen-lezen Android-kalenderintegratie synchroniseert Nostr-events naar de apparaatkalender.

## In ontwikkeling

### Amethyst voegt geplande berichten, NIP-9A community-regels en een lokale desktayrelay toe

Amethyst voegde 78 PR's samen deze week. Geplande berichten landen in PR #2765. Een desktopbuild krijgt een ingebedde lokale relay met SQLite-eventpersistentie in PR #2841. Drie PR's implementeren NIP-9A community-regels: PR #2798 valideert berichten tegen community-regels voor verzending, PR #2799 voegt een gestructureerde NIP-9A regeleditor toe, en PR #2800 voegt een opt-in NIP-9A-feedfilter toe.

### Shopstr voegt MCP-auditlogboekregistratie en sessiebeveiliging toe

Shopstr voegde vijf PR's samen. Auditlogboekregistratie voor de MCP-toollaag landt in PR #456. Sessiebeveiliging wordt aangescherpt in PR #477 met sessieverankering aan de oorspronkelijke API-sleutel en TTL-verwijdering.

### Dart NDK voegt webondersteuning en seal-handtekeningverificatie toe

Dart NDK voegde zes PR's samen. Webondersteuning arriveert in SembastCacheManager via PR #571. Seal-handtekeningverificatie landt in PR #595 voor de NIP-59 Gift Wrap-flow.

## Nieuwe projecten

### Tamagostrich lanceert een gedecentraliseerde NIP-78 Tamagotchi met sats-beloningen

Tamagostrich is een browsergebaseerd virtueel huisdierengame gelanceerd op IDENTITY Hackathon 2026, waarbij een babystruisvogel, Nori, evolueert via uw Nostr sociale activiteit. De toestand van het huisdier leeft in een NIP-78 kind:30078-event voor synchronisatie tussen apparaten. Mijlpaalbeloningen worden uitbetaald in sats via NIP-47: 50 sats op level 5, 210 sats op level 10, en 420 sats op het maximale level 21, verzonden naar het lud16-adres van de gebruiker.

## Protocol- en specificatiewerk

Vijf nieuwe voorstellen werden deze week ingediend:

PR #2331 stelt NIP-9A voor: Verifieerbare Community-regels, met introductie van kind:34551 voor machineleesbare cryptografisch ondertekende community-regeldocumenten.

PR #2335 stelt Reservation Events voor Nostr Marketplaces voor, waarbij kind:32122 (geparametriseerde vervangbare reserveringsevents), kind:1326 (alleen-toevoegen overgangsauditrecords) en kind:32124 (post-handelsevaluaties) worden gedefinieerd. Onderhandeling is privé via NIP-59 gift-wrapped berichten.

PR #2334 stelt Escrow Services voor Nostr Marketplaces voor met kind:30303 zodat escrow-operators hun EVM-contractadres en tariefschema kunnen verklaren.

PR #2333 stelt Accommodation Listing Profiles voor NIP-99 Marketplace Listings voor, waarmee NIP-99 wordt uitgebreid met H3 geospatiale index g-tags voor kortetermijnverhuurlijsten.

PR #2332 stelt NIP-BC voor: Onchain Zaps (kind 8333), waarbij de directe identiteit tussen Nostr-sleutels en Bitcoin Taproot-adressen wordt benut. Het kind-nummer weerspiegelt NIP-57: 9735 is de Lightning P2P-poort; 8333 is de P2P-poort van Bitcoin mainnet.

## NIP-diepteduik: NIP-78 (App-specifieke gegevens)

NIP-78 definieert een standaardmanier voor applicaties om willekeurige privé- of openbare gegevens namens een gebruiker op te slaan met behulp van Nostr-events. Het kerntype is 30078, een geparametriseerd vervangbaar event waarbij de d-tag een door de applicatie gedefinieerde identificatiereeks is. Een applicatie geeft zijn opslagslot een unieke d-tag en publiceert een 30078-event met de JSON- of tekstinhoud die het moet bewaren. De primaire motivatie is apparaatoverschrijdende synchronisatie zonder een gecentraliseerde server. Voor privé-applicatiegegevens kunnen NIP-78-events het inhoudsfeld versleutelen met NIP-44 voor publicatie. Huidige gebruikers zijn onder meer Tamagostrich (synchronisatie van huisdiertoestand), Wisp (portefeuilleback-up en beveiligingsinstellingen), NosPress (CMS-orchestratiestatus) en verschillende Nostr-clientinstellingen voor synchronisatie-implementaties.

---

Primaire bronnen:
- NIP-78-specificatie: https://github.com/nostr-protocol/nips/blob/master/78.md
- Tamagostrich: https://github.com/Negr087/tamagostrich

Zie ook: NIP-51 Lijsten, NIP-65 Relay-lijstmetadata

## NIP-diepteduik: NIP-98 (HTTP Auth)

NIP-98 definieert een HTTP-authenticatieschema waarmee Nostr-sleutelparen verzoeken aan HTTP-servers autoriseren, waardoor gebruikersnamen, wachtwoorden of OAuth-tokens overbodig worden. Een client construeert een kortlevend Nostr-event van kind 27235, ondertekent het met zijn privésleutel, codeert de JSON in base64 en verzendt het in een Authorization: Nostr <base64> HTTP-header. Het kind 27235-event bevat de HTTP-methode in een method-tag, de volledige verzoek-URL in een u-tag, en een created_at-tijdstempel. De server valideert de handtekening, controleert of methode en URL overeenkomen, en verifieert of het tijdstempel recent is om hergebruiksaanvallen te voorkomen. NIP-98 wordt gebruikt in Blossom (BUD-01) voor blob-uploadauthenticatie, Routstr voor API-toegangscontrole per verzoek, Sprout voor git-transportauthenticatie en Alby Hub voor admin-API-authenticatie.

---

Primaire bronnen:
- NIP-98-specificatie: https://github.com/nostr-protocol/nips/blob/master/98.md
- BUD-01: https://github.com/hzrd149/blossom/blob/master/buds/01.md

Zie ook: NIP-96 HTTP-bestandsopslagintegratie

---

Dat is het voor deze week. Als u iets bouwt of nieuws te delen heeft, stuur ons een DM op Nostr of vind ons op nostrcompass.org.
