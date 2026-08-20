---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "Post-quantum-identiteitstools, sterkere versleutelde berichten en ondertekening, draagbare community-instellingen en protocolwerk over NIPs en Concord."
---

Welkom terug bij [Nostr Compass](https://nostrcompass.org), je wekelijkse gids voor Nostr.

**Deze week:** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) voegt post-quantum-sleutels en optioneel beschermde berichten toe naast bestaande Nostr-identiteiten. [Divine](https://github.com/divinevideo/divine-mobile) verscherpt accountisolatie, validatie van privéberichten en publicatiebevestiging; [MDK](https://github.com/marmot-protocol/mdk) versterkt convergentie en herstel van versleutelde groepen; en [Amber](https://github.com/greenart7c3/Amber) maakt gegroepeerde ondertekeningsbeslissingen expliciet. Releases verbeteren walletverbindingen, versleutelde chat, sociale ontdekking, apparaatsynchronisatie en remote signing, terwijl protocolwerk identiteit en versleutelde communities behandelt. De deep dives leggen geauthenticeerde verwijderingsverzoeken en gedecentraliseerde meldingen uit.

## Topverhalen

### nostr-wot-extension 0.4.0 voegt post-quantum-sleutels toe naast een Nostr-identiteit

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) is een browserextensie voor het beheren van Nostr-identiteiten en ondertekenen. Accounts die uit een 24-woords seed zijn aangemaakt, kunnen nu ML-KEM-1024-versleutelings- en ML-DSA-87-ondertekeningssleutels afleiden naast hun bestaande Nostr-sleutel. Een flow met één klik publiceert een kind `10203`-attestatie die de Nostr-public key bindt aan beide post-quantum-public keys en een ML-DSA-bezitsbewijs bevat. Accounts geïmporteerd uit een 12-woords mnemonic, een kale `nsec`, een remote signer of een alleen-lezen sleutel kunnen de afleidingsflow niet gebruiken, en de extensie legt die beperking uit in de accountweergave.

De release voegt ook optionele post-quantum directe berichten toe. Het combineert het ML-KEM-gedeelde geheim met de bestaande [NIP-44 encrypted-message conversation key](https://github.com/nostr-protocol/nips/blob/master/44.md) via HKDF en behoudt de normale NIP-59 metadata-hiding gift-wrap-lagen voor relaylevering. Versleuteling valt nooit stil terug nadat een ontvanger zich heeft aangemeld, terwijl ontsleuteling automatisch het passende pad kiest. Dit beschermt het nieuwe berichtenpad tegen later herstel van een huidige Nostr-private key, maar vervangt geen secp256k1-eventsignaturen; de release laat die grotere migratie expliciet over aan toekomstige coördinatie met relays en clients.

### Divine Mobile 1.0.19 verscherpt accounts, privéberichten en publiceren

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) is een mobiele kortvideo-client die video's publiceert en ophaalt via Nostr. De accountwisselaar bouwt elke ingelogde identiteit nu rond een accountgebonden container, en een publicatiefix voorkomt dat een video onder het verkeerde account wordt verstuurd. Relaypublicatiepaden wachten nu op een `OK`-antwoord met expliciete successemantiek, terwijl een relay-`CLOSED`-frame zijn eigen lopende query kan beëindigen in plaats van het verzoek te laten hangen.

[Privéberichtenafhandeling](https://github.com/divinevideo/divine-mobile/pull/6368) wijst niet-geauthenticeerde rumor-velden en ongetekende seals af, herstelt vier gevallen van ontbrekende berichten en stuurt groepsgesprekken van volledig gevolgde deelnemers naar de inbox. De release behoudt ook de tags op adresseerbare video-events wanneer lijsten worden bijgewerkt en verwerkt waargenomen verwijderingsverzoeken zodat verwijderde video's uit de lokale staat verdwijnen. Die wijzigingen volgen op het per-relay query-timeoutwerk van vorige week, maar verschuiven de focus van ophaalisolatie naar identiteitsgrenzen, berichtvalidatie en publicatiebevestiging.

### MDK 0.9.11 verhardt Marmot-groepsconvergentie en -herstel

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) is een Rust-ontwikkelkit voor Marmot, een versleuteld groepsberichtenprotocol over Nostr. De release bouwt een groter convergentie- en herstelsysteem rond de groepsstate machine: verouderde convergentiepasses heropenen op de huidige groepstip, inkomende capability-projecties worden atomisch gecommit, uitgestelde berichten krijgen begrensde levensduur over herstarts heen, en commit-adressed checkpoints helpen de eigen commit-forks van een identiteit te herstellen. Niet-stabiele sends kunnen in de wachtrij worden gezet en hersteld, terwijl een epoch-stall-pad escaleert naar backfill en verzonden berichten convergentiewerk overleven.

[Opslag- en hostintegraties](https://github.com/marmot-protocol/mdk/pull/1201) krijgen een parallelle verhardingsronde. MDK verwijdert veilig geprunede SQLite-projecties, wist geïmporteerde private keys, NIP-49 encrypted-key export-intermediairs en OpenMLS-serialisatiebuffers, en redacteert groepsafbeeldingssleutels uit debug-output. Accountimport kan hervat worden na onderbreking, iOS- en Android-paden voor privéopslag zijn gerepareerd, en hosts kunnen opslag expliciet sluiten vóór suspensie. Nieuwe lichtgewicht roster- en lokale-lidmaatschapsprojecties verminderen wat applicaties moeten lezen, terwijl de Hermes-connector meerdere door agents gegenereerde afbeeldingen als één Marmot-album kan afleveren.

### Nostria 4.1.67 breidt versleutelde-communitybeheer uit

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) is een web- en desktop-social client voor Nostr. De release bouwt voort op de experimentele NIP-29 relay-beheerde groepen en Concord-versleutelde communities uit 4.1.53, met community-ontbinding, icoon- en bannerbeheer, versleutelde fotouploads met gecomprimeerde previews, een volledige reactiepicker en een dual-pane-layout die een community openhoudt terwijl de gebruiker notities of artikelen leest. De release voegt ook threaded messaging en een gecombineerde hub voor publieke, groeps- en privéchats toe.

### Amber 6.4.0 maakt elke gegroepeerde ondertekeningsbeslissing expliciet

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) is een Android-signer die Nostr-private keys scheidt van de applicaties die handtekeningen aanvragen. Het herontworpen multi-requestscherm biedt Approve- en Deny-controls voor elk verzoek en elke groep, ter vervanging van de vorige selectie-en-bevestigingsflow. Afgewezen verzoeken via Amber's relay-bemiddelde bunkerinterface ontvangen nu correcte foutresponses, zodat de aanvragende client afwijzing kan onderscheiden van een vastgelopen signer.

[Amber's getagde bron](https://github.com/greenart7c3/Amber/tree/v6.4.0) voegt ook gelokaliseerde, menselijk leesbare labels toe voor 113 extra event kinds in elke uitgeleverde locale. De toevoegingen omvatten Concord-groepsevents, NIP-51 Git-repositorybookmarks en NIP-53 room-presence-events, waardoor gebruikers meer context krijgen over onbekende data voordat ze een handtekening goedkeuren. Een concurrent-map-guard lost ook een relay-subscriptiecrash op die een `NegativeArraySizeException` kon opleveren.

### Safebox Acorn scheidt een draagbare herstelcomponent af van de webapp

[Safebox Acorn](https://github.com/trbouma/safebox-acorn) is een standalone Python-component en command-line interface voor het beveiligen van door de gebruiker beheerde sleutels, fondsen en records met Nostr-ondersteunde staat. Acorn uit de bredere Safebox-webapplicatie halen laat een ander Python-project de runtime installeren en de sleutel-, Nostr-profiel-, relay-, record-, Cashu-, Lightning- en cryptografische helpers gebruiken zonder de webinterface mee te nemen. De huidige recordbeschermingsprimitieven kunnen een nieuwe 256-bit sleutel genereren, er één afleiden uit apart aangeleverde entropie, en de exacte sleutel coderen als een gecontroleerde 24-woords herstelzin.

De [recovery and continuity guide](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) van het project positioneert Acorn als het vervangbare protocolcomponent binnen een huishouden- of community-Safebox. Het ontwerp houdt versleutelde staat beschikbaar via een lokale relay en onafhankelijke replica's, zodat herstel niet afhangt van één apparaat, applicatie, relay, mint of dienstverlener. De documentatie is voorzichtig over de huidige grens: versleuteling van beschermde records is nog in ontwerp, dus applicaties mogen records niet afhankelijk maken van de nieuwe recordbeschermingssleutel totdat dat profiel is geïmplementeerd en beoordeeld.


## Getagde releases

### Mostro Core 0.14.2 wijzigt de versleutelde chat-envelope

[Mostro Core](https://github.com/MostroP2P/mostro-core) is de Rust-bibliotheek met gedeelde types en peer-to-peer-functies voor de Mostro-exchange-daemon en zijn clients. [Versie 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) vervangt gift-wrapped chatberichten door kind 14-envelopes die aparte conversation-encryption- en signing keys afleiden uit het gedeelde geheim van de peers. De nieuwe reader valideert auteur, handtekening, ontvanger, timestamp en contentgrootte, terwijl legacy gift-wrap-helpers beschikbaar blijven zodat clients beide formaten kunnen lezen tijdens migratie.

### Mostro 0.18.1 start een Cashu-escrowpad en verhardt de daemon

[Mostro](https://github.com/MostroP2P/mostro) is een peer-to-peer Lightning-exchange-daemon die orders coördineert via Nostr. [Versie 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1) legt de basis voor een Cashu-escrow-backend, inclusief configuratie, databasehelpers, mint-integratie, startup-verdraad en de eerste lock-actie. Het kan ook prijzen gebruiken die een vertrouwde node via Nostr aankondigt, en adverteert proof-of-work-vereisten voor eerste contact in zijn replaceable info-event. De release werkt de Nostr-afhankelijkheid bij voor een NIP-44 denial-of-service-fix, verwijdert private keys uit restore-sessionlogs, wijst niet-geautoriseerde cooperative-cancel-berichten af, verhardt LNURL-fetches tegen server-side request forgery en hangs, valideert payout-invoices en herstelt hold-invoice-subscripties na een herstart.

### LaWallet NWC 2.3.0 voegt Nostr-meldingen en zap-receipts toe

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) is een open-source Lightning Address-platform dat wallets verbindt via [Nostr Wallet Connect](/nl/topics/nip-47/). [Versie 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) laat elke wallet ontvangen en doorgestuurde meldingen sturen als configureerbare Nostr-events, inclusief een ontvanger-`p`-tag, geselecteerde relays, gesjabloonde content en optionele [NIP-44](/nl/topics/nip-44/)-versleuteling; retries hergebruiken dezelfde getekende event-ID. Het accepteert ook zap-verzoeken en publiceert getekende [NIP-57](/nl/topics/nip-57/) kind 9735-receipts na settlement, terwijl een nieuwe address-capability-weergave laat zien of het opgeloste adres NIP-05, NIP-57 en gerelateerde Lightning Address-protocollen ondersteunt.

### nostr-double-ratchet TypeScript 0.0.166 bindt publieke invites aan session keys

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) levert TypeScript- en Rust-primitieven voor end-to-end versleutelde directe en groepsberichten over Nostr-relays. [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) vereist dat een invite-response het bezit van zijn session key bewijst, zodat een herbruikbare publieke invite geen Nostr-identiteit kan binden aan de session van een andere partij. De release wijst ook malformed rumor-velden af en verscherpt payloadvalidatie; bestaande sessions blijven werken, maar een bijgewerkte inviter wijst proofless responses van oudere invitees af.

### cln-nip47 0.2.0 breidt NWC-verzoeken uit en isoleert ze

[cln-nip47](https://github.com/daywalker90/cln-nip47) is een Core Lightning-plugin die een node blootstelt aan wallets via [Nostr Wallet Connect](/nl/topics/nip-47/). [Versie 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) voegt NWC-methodes toe om hold invoices aan te maken, te annuleren en te settlen plus een `hold_invoice_accepted`-notificatie, en adverteert de methodeset die de verbonden node daadwerkelijk ondersteunt. Transaction-list-responses stoppen nu bij 500 entries en ongeveer 128 kB, request-events worden gededupliceerd op event-ID, en de mislukte notificatie van één client blokkeert levering aan andere clients niet meer. De release verwijdert ook de twee multi-payment-methodes die niet langer deel uitmaken van de NWC-specificatie.

### ClipRelay 0.1.3 herstelt relay- en signer-verbindingen na idle-periodes

[ClipRelay](https://github.com/tajava2006/cliprelay) synchroniseert het klembord van een gebruiker tussen apparaten via Nostr-relays en versleutelt de content voor dezelfde identiteit met [NIP-44](/nl/topics/nip-44/). De bijpassende [desktop-](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) en [Android-](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3)releases 0.1.3 voegen een tekstvak toe om getypte tekst rechtstreeks naar het klembord van een ander apparaat te sturen. Ze testen ook liveness met echte relay-roundtrips na idle-periodes, escalerend van resubscriptie naar socket-vervanging en een herbouwde connection pool, terwijl vastgelopen [NIP-46](/nl/topics/nip-46/)-signer-aanroepen nu time-outen en automatisch herbouwen.

### NoorNote 1.3.2 verplaatst artikelontdekking naar de social graph

[NoorNote](https://github.com/77elements/noornote) is een Nostr-client voor social posts, versleutelde berichten, long-form-artikelen en andere event types op web, desktop en Android. [Versie 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) vervangt de platte globale artikelfeed door ontdekking uit eerste-, tweede- en derdegraadscontacten, waardoor lezers een aan de follow graph gewortelde artikeltimeline krijgen. Het vouwt ook bursts van gereplayde directe berichten van onbekende afzenders samen tot één rollende notificatie in plaats van een stapel toasts terwijl relayhistorie binnenkomt.

### Bray 2.4.0 voegt een compact remote-signing-dialect toe

[Bray](https://github.com/forgesworn/bray) is een Nostr MCP-server die software-agents en mensen tools geeft voor relaytoegang, identiteit, publiceren en remote signing. [Versie 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) accepteert een signing request waarvan het event een object is naast de stringified vorm die [NIP-46](/nl/topics/nip-46/) gebruikt, en voegt `sign_event_compact` toe, dat alleen event-ID, handtekening, public key en timestamp teruggeeft. Dat kleinere request- en responseformaat vermindert geheugengebruik voor constrained hardware signers, terwijl de standaard `sign_event`-flow ongewijzigd blijft en beide dialecten een handtekening over de ID van het ontvangen event produceren.


## Nieuw ontdekt

### Pact brengt wederzijds toegestemde agent bonds naar Nostr

[Pact](https://github.com/bobodread876/pact), deze week nieuw ontdekt, is een vroeg stadium relationshiplaag voor software-agents gebouwd op MATE.md en een draft NIP-BD-transport. Zijn getekende, wederzijds toegestemde bonds worden vastgehouden door de eigen sleutels van de agents en kunnen via Nostr worden gepubliceerd, terwijl private bonds [NIP-59](/nl/topics/nip-59/) gift wrapping gebruiken. De monorepo omvat een MCP-server, TypeScript SDK, command-line client, zelf te hosten daemon en webinterface. De laatste repositoryactiviteit valt vóór het wekelijkse venster van deze editie, dus dit is een ontdekkingsnotitie en geen claim op een nieuwe release.


## In ontwikkeling

### nostrord houdt groepsdempen gesynchroniseerd tussen apparaten

[nostrord](https://github.com/nostrord/nostrord) is een cross-platform client voor relay-beheerde communities. [PR #250](https://github.com/nostrord/nostrord/pull/250) slaat de per-groep dempkeuzes van elk account op in een zelfversleuteld [NIP-78](/nl/topics/nip-78/) (application-specific data) kind `30078`-event, zodat een instelling op één apparaat de gebruiker naar een ander kan volgen zonder de groepslijst aan de relay prijs te geven. Het replaceable record gebruikt newest-event ordering, luistert naar live wijzigingen en rolt de interface terug wanneer ondertekenen of publiceren mislukt in plaats van lokale staat desynchroon te laten. Gedempte groepen dragen niet meer bij aan zichtbare ongelezen totalen maar behouden hun ongelezen positie voor het volgende bezoek.

### Amethyst voltooit Concords invite lifecycle

[Amethyst](https://github.com/vitorpamplona/amethyst) is een Android Nostr-client waarvan de versleutelde-community-ondersteuning het Concord-protocol implementeert. [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) laat invitelinks een community-refounding overleven door hun bundles opnieuw uit te geven op dezelfde adresseerbare coördinaten, terwijl een ban-check voorkomt dat een verwijderd lid dat herstelpad gebruikt. Het implementeert ook de versleutelde CORD-05-invitelijst in zowel de app als de `amy` command-line client, voegt per-link revocation tombstones toe en vereist relaybevestiging vóór het verwijderen van de enige opgeslagen signing key die een link kan pensioneren. Hetzelfde werk geeft `amy` de control-key delivery-, refounding-, rekeying- en stranded-member recovery-paden die nodig zijn om latere community-epochs te volgen.

### Buzz draagt het uiterlijk van elke community mee over desktop en mobiel

[Buzz](https://github.com/block/buzz) is een Nostr-gebaseerde community-workspace met desktop- en mobiele clients. Gemergde desktop-[PR #3653](https://github.com/block/buzz/pull/3653) en mobiele [PR #3767](https://github.com/block/buzz/pull/3767) slaan het theme, accent en system-mode-keuze van elke community op als versleuteld NIP-78-record op de relay van die community. Beide clients delen dezelfde versioned payload en houden identiteitsscoped lokale caches bij, zodat wisselen van community of account het verkeerde uiterlijk niet kan toepassen terwijl de relay niet beschikbaar is. Replacement ordering, guarded writes en resubscriptie na een gesloten verbinding laten beide clients opnieuw convergeren na reconnect.

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) volgde vóór de issue-cutoff met een performance- en betrouwbaarheidsronde. Het verwijdert regressies na 0.5.9, versnelt het laden van kanalen, begrenst initiële timeline-retentie, coalesceert read-state persistence, behoudt verse kanaaltimelines en voorkomt dat de relay ingest worker crasht op reacties op projectevents. Het voegt ook het sturen van een threadbericht naar een kanaal toe en beperkt desktopzoeken tot de bedoelde scope.


## Protocol- en specificatiewerk

### NIPs

[NIPs PR #2435](https://github.com/nostr-protocol/nips/pull/2435) is een open amendement op NIP-34, dat git-repositorysamenwerking via Nostr-events standaardiseert. Het voegt een optionele `b`-tag toe aan een pull-request-event zodat de auteur een target branch anders dan de default van de repository kan noemen. Het voorstel komt overeen met ondersteuning die al is geïmplementeerd in ngit en GitWorkshop, maar is nog niet in de specificatie opgenomen.

[NIPs PR #2434](https://github.com/nostr-protocol/nips/pull/2434) is een open voorstel voor post-quantum-identiteitssleutels. Het leidt post-quantum-versleutelings- en signing keys af naast de bestaande secp256k1-sleutel uit een NIP-06 mnemonic key-derivation seed en bindt de public keys aan de Nostr-identiteit met een kind `10203`-attestatie. Het draft beperkt zijn claim tot het beschermen van de vertrouwelijkheid van eerdere berichten als secp256k1 later wordt gebroken; het vervangt de huidige eventsignaturen niet.

[NIPs PR #2431](https://github.com/nostr-protocol/nips/pull/2431) is een open NIP-07-amendement voor browser signers. Een client zou de public key die hij verwacht kunnen meegeven bij signing- of encryption requests, waardoor de signer dat account moet gebruiken of de call moet afwijzen. Dat zou voorkomen dat een pagina stil doorgaat onder een andere identiteit nadat de gebruiker van account wisselt in de signer.

[NIPs PR #1813](https://github.com/nostr-protocol/nips/pull/1813) blijft een open double-ratchet-voorstel na substantieel werk in het venster. Het specificeert forward-secret versleutelde gesprekken waarvan de sleutels met berichten doorgaan, met een implementatie die al beschikbaar is in de nostr-double-ratchet-bibliotheek en Iris. Het is nog steeds een draft, geen gemergde NIP.

[NIPs PR #2433](https://github.com/nostr-protocol/nips/pull/2433) opende en sloot zonder merge in het venster. Het stelde voor NIP-42 relay errors te verduidelijken zodat `auth-required` zou betekenen dat verdere authenticatie het resultaat kan wijzigen, terwijl `restricted` zou betekenen dat dit niet kan. Het onderscheid richtte zich op verbindingen geauthenticeerd voor één sleutel maar nog zonder autorisatie voor een andere; de closed status betekent dat de formulering niet in de specificatie is opgenomen.

[NIPs PR #2378](https://github.com/nostr-protocol/nips/pull/2378), eerder behandeld terwijl het nog voorgesteld was, is nu gesloten zonder merge. De voorgestelde agent passports, discovery-, task-, marketplace-, invoice- en connection-events blijven daarmee buiten de NIP-set.

[NIPs commit 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) merge een uitsluitend documentaire correctie op NIP-29. Het voegt een `previous`-tag toe aan het groepsmetadatavoorbeeld, waarmee wordt getoond hoe een replacement event het event kan identificeren dat het vervangt. Dit verduidelijkt een voorbeeld en introduceert geen nieuw protocolfeature.

### Concord en CORDs

[CORD PR #18](https://github.com/concord-protocol/concord/pull/18) zou versleutelde Community Lists sharden over kind `33302`-events, de limiet van 50 lidmaatschappen verwijderen en gepensioneerde entries prunen om binnen relaylimieten te blijven. Twee andere open voorstellen voegen [private mention locators](https://github.com/concord-protocol/concord/pull/16) en een [pause signal](https://github.com/concord-protocol/concord/pull/17) toe dat chat pauzeert zonder berichten weg te gooien.

[CORD-02 PR #15](https://github.com/concord-protocol/concord/pull/15) merge op 6 augustus en beperkt writes tot het control plane van een community. Owners en staff houden een nieuw `control_root` signing secret, terwijl alle leden de afgeleide public key en read key behouden die nodig zijn om moderatiestaat te verifiëren en te ontsleutelen. De write key is een spambarrière, geen vervanging voor de inner actor signatures en roster checks die autoriteit vestigen.

[CORD PR #12](https://github.com/concord-protocol/concord/pull/12), eerder behandeld als open draft, is nu gesloten zonder merge. Het control-plane-gedeelte werd vervangen door het smallere gemergde CORD-02-amendement hierboven, terwijl restricted-write channels en het overige draftmateriaal niet in de specificatie zijn opgenomen.

## NIP Deep Dive

### Event Deletion Requests (NIP-09)

[NIP-09](/nl/topics/nip-09/), gedefinieerd door de [primaire specificatie](https://github.com/nostr-protocol/nips/blob/master/09.md), geeft een eventauteur een getekende manier om relays en clients te vragen één of meer events van die auteur niet meer te serveren. Het wist niet elke kopie. Het draagt de intentie van de auteur door hetzelfde relaynetwerk dat het oorspronkelijke event verspreidde.

Het verzoek is een gewoon getekend kind `5`-event. De tags bevatten één of meer `e`-referenties naar specifieke event-ID's of `a`-referenties naar adresseerbare-eventcoördinaten, en de [NIP-09 tag rules](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) zeggen dat het een `k`-tag moet bevatten voor elk gerefereerd event kind. De optionele `content` kan de reden uitleggen. Voor een `a`-referentie moet een relay elke versie op die coördinaat verwijderen waarvan de timestamp niet later is dan de `created_at` van het verzoek, wat voorkomt dat een oud verwijderingsverzoek een latere replacement onderdrukt.

[Auteurschap is de beveiligingsgrens](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior). Een relay moet een gerefereerd event stoppen met publiceren alleen wanneer zijn `pubkey` overeenkomt met de `pubkey` van het verwijderingsverzoek, en een client moet die check uitvoeren vóór het verbergen van een event. Een relay bezit het gerefereerde event mogelijk niet en kan daardoor de relatie niet valideren bij acceptatie van het verzoek, dus clients kunnen relayacceptatie niet behandelen als bewijs dat de verwijdering geautoriseerd was. De specificatie vraagt relays ook het kind `5`-verzoek te bewaren omdat een andere client het oorspronkelijke event al kan hebben en het verzoek later tegenkomt.

Hier is een [getekend kind `5`-event](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943):

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

Verwijdering blijft een coöperatief beleid, geen intrekking van een getekend object. Een relay, cache, screenshot of offline client kan de oorspronkelijke bytes bewaren, en het verwijderen van het kind `5`-verzoek zelf maakt het niet ongedaan. Clients kunnen het doel verbergen, als disowned markeren of de reden van het verzoek tonen, maar moeten gebruikers vertellen dat universele verwijdering niet gegarandeerd kan worden. Dit verschilt van [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), waar een `expiration`-tag relays vraagt een event niet meer op te slaan na een tijd die bij publicatie is gekozen. NIP-09 behandelt een latere auteursbeslissing en kan naar al verspreide events wijzen.

Huidige implementaties passen dat beleid op verschillende lagen toe. [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623) verwijdert verwijderde video's uit de event store van de client, [strfry PR #251](https://github.com/hoytech/strfry/pull/251) breidt geldige verwijderingsverzoeken uit naar gift-wrap-ontvangers, en [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) declareert NIP-09-ondersteuning in zijn client. [nostrord's group client](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) levert nog een huidig implementatiepad.

### Reporting (NIP-56)

[NIP-56](/nl/topics/nip-56/), gedefinieerd door de [primaire specificatie](https://github.com/nostr-protocol/nips/blob/master/56.md), standaardiseert een getekende melding over een account, event of gerefereerde blob. Het scheidt het meldingssignaal van de moderatiebeslissing, zodat elke client of relay kan kiezen welke reporters hij vertrouwt en welke respons bij zijn beleid past.

Een melding gebruikt kind `1984` en moet het gemelde account identificeren in een `p`-tag. Het melden van een note vereist ook een `e`-tag voor de event-ID. De derde waarde van de tag draagt één van de gespecificeerde categorieën: `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation` of `other`. Een melding over een blob kan zijn hash gebruiken in een `x`-tag, een `e`-tag voor het event dat naar de blob verwees, en optioneel een `server`-tag voor een locatie. Optionele `L`- en `l`-tags uit [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) kunnen een namespaced label toevoegen wanneer de vaste categorielijst niet precies genoeg is.

[Het event bewijst alleen dat één sleutel een beschuldiging heeft gedaan](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting). De gemelde content wordt niet onwaar, illegaal of verwijderbaar alleen omdat een geldig kind `1984` bestaat, en een open relay kan anonieme meldingen niet veilig als stemmen tellen. De specificatie adviseert tegen automatische relaymoderatie omdat meldingen gemakkelijk te manipuleren zijn, maar staat relaybeheerders toe te handelen op meldingen van moderators die ze al vertrouwen. Een client kan meldingen in plaats daarvan wegen via de social graph van een gebruiker, bijvoorbeeld door content te vervagen nadat meerdere vertrouwde contacten hetzelfde account hebben gemarkeerd.

Hier is een [getekend kind `1984`-event](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2):

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 en NIP-09 lossen verschillende problemen op](https://github.com/nostr-protocol/nips/tree/master). Een kind `1984`-melding kan het account of event van iemand anders targeten, maar verleent geen verwijderingsautoriteit. Een kind `5`-verzoek drukt de intentie van de oorspronkelijke auteur uit en is alleen geldig tegen de eigen events van die auteur. Geen van beide garandeert verwijdering: NIP-56 delegeert actie bewust aan lokaal moderatiebeleid, terwijl NIP-09 afhangt van relays en clients die een geauthenticeerd verzoek honoreren.

Implementaties leggen die keuzes bloot in verschillende producten. [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) corrigeert meldingslevering in een kortvideo-client, [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) leest meldingen als begrensde context voor marketplace-deelnemers, en [nostrord's NIP-56 module](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) publiceert en verwerkt meldingsevents. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) vermeldt ook huidige NIP-56-ondersteuning.


---

Stuur een NIP-17 DM om een project of nieuwsitem te delen via het [Nostr Compass-project](https://github.com/andotherstuff/nostr-compass).
