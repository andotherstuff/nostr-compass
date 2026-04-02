---
title: 'Nostr Compass #16'
date: 2026-04-01
translationOf: /en/newsletters/2026-04-01-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** [Amethyst](https://github.com/vitorpamplona/amethyst) brengt [v1.07.0](#amethyst-brengt-vastgepinde-notes-relaybeheer-en-request-to-vanish) uit met vastgepinde notes, relaybeheer via [NIP-86](/nl/topics/nip-86/) en ondersteuning voor [NIP-62](/nl/topics/nip-62/) Request to Vanish. [NIP-5A](#nip-5a-wordt-gemerged-en-brengt-statische-websites-naar-nostr) (Static Websites) wordt gemerged in het NIPs-repository en definieert hoe websites onder Nostr-sleutelparen kunnen worden gehost met [Blossom](/nl/topics/blossom/)-opslag. [Flotilla](https://gitea.coracle.social/coracle/flotilla) brengt [v1.7.0](#flotilla-v170-voegt-voice-rooms-en-e-mail-login-toe) uit met voice rooms, e-mail/wachtwoordlogin en proof-of-work DM's. [White Noise](https://github.com/marmot-protocol/whitenoise) repareert relay churn in [v2026.3.23](#white-noise-repareert-relay-churn-en-breidt-clientbesturing-uit), [nospeak](https://github.com/psic4t/nospeak) lanceert [1.0.0](#nospeak-lanceert-als-een-10-prive-messenger) als messenger zonder signup. [Nymchat](https://github.com/Spl0itable/NYM) [adopteert Marmot](#nymchat-brengt-marmot-aangedreven-groepschats) voor MLS-versleutelde groepschats met NIP-17-terugval. [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) bereikt [v1.0.0](#calendar-by-form-v100) met private kalenderlijsten en ICS-import, [Amber](https://github.com/greenart7c3/Amber) voegt [mnemonic-herstel en NIP-42 relay-auth-whitelisting](#amber-v502-tot-en-met-v504) toe, en de [Marmot-specificatie](#marmot-verplaatst-keypackages-naar-addressable-events-en-verscherpt-pushnotificaties) verplaatst KeyPackages naar addressable events terwijl MIP-05 pushnotificatieformattering wordt aangescherpt.

## Nieuws

### Amethyst brengt vastgepinde notes, relaybeheer en Request to Vanish

[Amethyst](https://github.com/vitorpamplona/amethyst), de Android-client onderhouden door vitorpamplona, bracht in drie dagen zes releases uit, van [v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) tot [v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5). De kernset functies bestrijkt zes protocoloppervlakken: vastgepinde notes, een speciaal poll-feedscherm, ondersteuning voor [NIP-62](/nl/topics/nip-62/) (Request to Vanish) om volledige eventverwijdering van relays te vragen, [NIP-86](/nl/topics/nip-86/) (Relay Management API) vanuit de client, [NIP-66](/nl/topics/nip-66/) (Relay Discovery and Liveness Monitoring)-beoordelingen in het relay-infoscherm en weergave van ledeninformatie uit [NIP-43](/nl/topics/nip-43/) (Relay Access Metadata and Requests).

[NIP-86](/nl/topics/nip-86/) definieert een JSON-RPC-interface voor relayoperators, waarmee clients administratieve commando's zoals het bannen of toestaan van pubkeys en het opvragen van gebande gebruikers via een gestandaardiseerde API kunnen sturen. Amethyst stelt dit nu direct bloot in zijn relaybeheer-UI, zodat gebruikers die hun eigen relays draaien ze kunnen beheren vanuit dezelfde client die ze gebruiken om te posten. [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) vervangt de oude hex-invoerdialoog voor ban- en allow-pubkeys door een interactieve gebruikerszoekdialoog.

v1.07.2 voegde GIF-keyboarduploads toe en repareerde een signingregressie waarbij afwijzingsantwoorden van Amber verkeerd werden gelezen omdat oudere Amber-versies een lege string teruggaven voor het `rejected`-veld ([PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)). v1.07.5 repareert een crash tijdens image-upload. De [v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2)- en [v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3)-releases eerder in de week voegden een polltype-selector toe voor single- versus multiple-choice polls, drag-to-seek op videovoortgangsbalken en verbeteringen voor anoniem posten.

### NIP-5A wordt gemerged en brengt statische websites naar Nostr

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) (Static Websites) werd gemerged via [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) en definieert hoe statische websites onder Nostr-sleutelparen kunnen worden gehost. De specificatie gebruikt twee event kinds: kind `15128` voor een rootsite, één per pubkey, en kind `35128` voor benoemde sites die met een `d` tag worden geïdentificeerd. Elk manifest koppelt URL-paden aan SHA256-hashes, met optionele `server` tags die verwijzen naar [Blossom](/nl/topics/blossom/)-opslaghosts waar de werkelijke bestanden staan.

Het hostingmodel werkt zo: een site-auteur bouwt een statische site, uploadt de bestanden naar een of meer Blossom-servers en publiceert daarna een ondertekend manifestevent dat paden aan inhoudshashes koppelt. Een hostserver ontvangt webverzoeken, resolveert de pubkey van de auteur uit het subdomein, haalt het manifest op uit de [NIP-65](/nl/topics/nip-65/)-relaylijst van de auteur en serveert bestanden door de overeenkomende blobs van Blossom te downloaden. De site blijft onder controle van de auteur omdat alleen die sleutel een bijgewerkt manifest kan signeren. De hostserver is vervangbaar omdat elke server die NIP-5A begrijpt dezelfde site uit hetzelfde manifest kan serveren.

De specificatie bouwt voort op infrastructuur die al bestond. [nsite](https://github.com/lez/nsite), de referentie-hostimplementatie van NIP-5A gebouwd door lez, en [nsite-manager](https://github.com/hzrd149/nsite-manager), hzrd149's beheer-UI, draaiden al voordat het NIP werd gemerged. De merge maakt de event kinds en URL-resolutieregels officieel, waardoor tweede en derde implementaties nu een stabiel doel hebben.

### White Noise repareert relay churn en breidt clientbesturing uit

[White Noise](https://github.com/marmot-protocol/whitenoise), de private messenger gebouwd op het [Marmot](/nl/topics/marmot/)-protocol, bracht [v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23) uit op 25 maart. De kern van de release is relaystabiliteit. Login wacht niet langer op publicatie naar elke relay uit de relaylijst voordat het verdergaat, omdat relaylijstpublicatie nu quorumlogica gebruikt en de rest op de achtergrond herprobeert. Eenmalige fetches en publicaties gebruiken scoped efemere relaysessies in plaats van in de langlevende pool te blijven hangen, herstelde sessies vinden na opstarten hun groepsrefreshpad terug, en de app toont nu relaydiagnostiek en inspectie van relaystatus via [PR #495](https://github.com/marmot-protocol/whitenoise/pull/495) en [PR #502](https://github.com/marmot-protocol/whitenoise/pull/502).

Dezelfde release verandert ook hoe gesprekken zich gedragen. [PR #468](https://github.com/marmot-protocol/whitenoise/pull/468) voegt NIP-C7 reply-threading toe met `q` tags en `nostr:nevent`-verwijzingen, [PR #471](https://github.com/marmot-protocol/whitenoise/pull/471) en [PR #512](https://github.com/marmot-protocol/whitenoise/pull/512) houden verwijderde berichten zichtbaar als verwijderde placeholders in plaats van ze stil te verwijderen, [PR #478](https://github.com/marmot-protocol/whitenoise/pull/478) voegt een in-app bugreportflow toe met anonieme rapporten via [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads), en [PR #486](https://github.com/marmot-protocol/whitenoise/pull/486) voegt supportchat direct in de client toe. Ook gebruikersgerichte berichtbesturing verscheen in dezelfde periode: [PR #532](https://github.com/marmot-protocol/whitenoise/pull/532) archiveert chats, [PR #541](https://github.com/marmot-protocol/whitenoise/pull/541) voegt mute en unmute toe met configureerbare duur, en [PR #535](https://github.com/marmot-protocol/whitenoise/pull/535) voegt notificatie-instellingen toe. [PR #539](https://github.com/marmot-protocol/whitenoise/pull/539) is voorbereidend werk voor push-registratie met APNs-registratie op iOS en Play Services-detectie op Android. Aan de backendzijde voegde de [MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit) MIP-05 pushnotificatieprimitieven en een notification request builder toe ([PR #235](https://github.com/marmot-protocol/mdk/pull/235), [PR #238](https://github.com/marmot-protocol/mdk/pull/238)), terwijl [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) persistentie voor pushregistratie ([PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)), fixes voor annulering van background tasks ([PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)) en herstel van key packages bij startup ([PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693)) toevoegde.

### Nostr VPN bereikt v0.3.0 met roster sync en invite v2

[Aansluitend op de lanceringsberichtgeving van vorige week](/nl/newsletters/2026-03-25-newsletter/#nostr-vpn-lanceert-als-een-tailscale-alternatief), zette [nostr-vpn](https://github.com/mmalmi/nostr-vpn), de peer-to-peer VPN die Nostr-relays gebruikt voor signalering en WireGuard voor versleutelde tunnels, zijn snelle releasetempo voort en bracht versies uit tot en met [v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3). De versionsprong brengt twee brekende wijzigingen: het invite-formaat gaat naar v2 (0.3.0 kan nog steeds v1-invites importeren, maar oudere builds kunnen geen v2-invites importeren), en admin-ondertekende roster sync werd aan het signaleringsprotocol toegevoegd. Peers met verschillende versies kunnen op mesh-niveau nog verbinden, maar oudere peers nemen niet deel aan rostersynchronisatie.

Die roster sync markeert het begin van een beheerd netwerk. Een admin-node kan nu lidmaatschapswijzigingen naar alle peers pushen, zodat het toevoegen of verwijderen van een apparaat uit de mesh niet vereist dat elke peer handmatig de configuratie aanpast. De v0.2.x-releases in dezelfde week pakten specifieke deploymentproblemen aan: [v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22) tot en met [v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28) repareerden Windows-servicemanagement, voegden Android-buildscripts toe en verfijnden de LAN-pairingflow.

### nospeak lanceert als een 1.0 private messenger

[nospeak](https://github.com/psic4t/nospeak), een private messenger gebouwd op Nostr, bracht zijn [1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0)-release uit op 27 maart. Het project bevat één-op-één- en groepsgesprekken, contactbeheer en een self-hostable architectuur. Eén-op-één-chats gebruiken [NIP-17](/nl/topics/nip-17/) (Private Direct Messages), dat [NIP-59](/nl/topics/nip-59/) (Gift Wrap) combineert met [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads) om de afzender voor relays te verbergen. Voor media worden bestanden client-side versleuteld met AES-256-GCM voordat ze naar Blossom-servers worden geüpload. De release wordt ook als container image geleverd voor self-hosting.

### Flotilla v1.7.0 voegt voice rooms en e-mail-login toe

[Flotilla](https://gitea.coracle.social/coracle/flotilla), hodlbod's Discord-achtige [NIP-29](/nl/topics/nip-29/) (Relay-based Groups)-client gebouwd rond het model "relays as groups", bracht [v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0) en [v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1) uit op 30 en 31 maart. De opvallendste functie is voice rooms, bijgedragen door mplorentz. Gebruikers kunnen nu deelnemen aan voice calls binnen groepskanalen, met een join-dialoog ([PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109)) waarin ze een audio-inputdevice kunnen kiezen en kunnen beslissen of ze echt aan de voice call meedoen of alleen de tekstchat willen bekijken. Die dialoog lost een UX-probleem uit de vorige iteratie op: het betreden van een room met voice activeerde eerder direct de microfoon, ook wanneer de gebruiker alleen berichten wilde lezen of kamerinstellingen wilde bekijken.

Dezelfde release voegt e-mail/wachtwoordlogin toe als alternatief voor Nostr key-gebaseerde auth, proof-of-work op DM's, DM-bewerking, herontworpen relay-onboarding en instellingen, detectie van Blossom-ondersteuning via `supported_nips`, verbeterde notificatiebadges, Android push notification fallback en fixes voor bestandsuploads op Android. v1.7.1 volgt met een fix voor pomade registration fallback bij gebruik van een offline signer.

Hodlbod bouwt ook [Caravel](https://gitea.coracle.social/coracle/caravel), een hostingmanager en dashboard voor zooid-relays, dat deze week 40 commits noteerde in de eerste ontwikkelfase.

### Nymchat brengt Marmot-aangedreven groepschats

[Nymchat](https://github.com/Spl0itable/NYM) (ook bekend als NYM, Nostr Ynstant Messenger), de efemere chatclient gekoppeld aan Bitchat, kondigde aan dat alle nieuwe groepschats nu het [Marmot](/nl/topics/marmot/)-protocol gebruiken voor MLS-versleutelde berichten. De integratie gebruikt kinds `443`, `444` en `445` voor respectievelijk key packages, welcome messages en groepsberichten, en levert forward secrecy, post-compromise security en nul metadata-lekkage. Als een ontvanger MLS niet kan gebruiken, valt Nymchat terug op zijn eerdere [NIP-17](/nl/topics/nip-17/) (Private Direct Messages)-pad voor groepschats, dat nog steeds end-to-end versleuteld is maar niet de ratchet-tree-eigenschappen van MLS heeft.

De v3.55- en v3.56-serie richtten zich deze week op randgevallen voor groepschats: laden op nieuwe apparaten, leave-gedrag, notificatierouting en unread badge counts. In dezelfde cyclus werd ook een XSS-kwetsbaarheid uit ongeëscapete HTML gepatcht en werd blokkering van trefwoorden en zinnen uitgebreid naar gebruikersbijnamen. Daarmee wordt Nymchat nog een Marmot-client naast [White Noise](#white-noise-repareert-relay-churn-en-breidt-clientbesturing-uit) en [OpenChat](#openchat-v024-tot-en-met-v030), en wordt de set apps groter die MLS-versleutelde groepsberichten via hetzelfde protocol kunnen uitwisselen.

## Releases

### Calendar by Form* v1.0.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), de gedecentraliseerde kalenderapp gebouwd op [NIP-52](/nl/topics/nip-52/) (Calendar Events), bereikte [v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0) op 29 maart. De release voegt private kalenderlijsten toe met versleutelde Nostr-events (kind `32123`) en [NIP-44](/nl/topics/nip-44/) (Encrypted Payloads) self-encryption, zodat gebruikers events in privécollecties kunnen groeperen zonder die structuur aan relays bloot te stellen. Dezelfde release voegt ook ICS-intentafhandeling toe voor het importeren van kalenderdata uit andere applicaties en invitation requests voor het delen van events tussen gebruikers.

### Amber v5.0.2 tot en met v5.0.4

[Amber](https://github.com/greenart7c3/Amber), de [NIP-55](/nl/topics/nip-55/) (Android Signer Application) signer-app, bracht drie point releases uit: [v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2), [v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3) en [v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4). De meest zichtbare toevoeging is login via mnemonic recovery phrase ([PR #358](https://github.com/greenart7c3/Amber/pull/358)), waarmee gebruikers hun signer kunnen herstellen vanuit een BIP39-seed phrase in plaats van de ruwe nsec- of ncryptsec-string nodig te hebben. [PR #357](https://github.com/greenart7c3/Amber/pull/357) voegt een [NIP-42](/nl/topics/nip-42/) relay-auth-whitelist toe, zodat gebruikers kunnen beperken welke relays clientauthenticatie mogen opvragen. [PR #353](https://github.com/greenart7c3/Amber/pull/353) voegt selectie van encryptie-scope toe voor decrypt-rechten, waardoor gebruikers alleen NIP-04- of alleen NIP-44-decrypttoegang kunnen geven in plaats van een algemene permissie. v5.0.4 repareert een bug waarbij rejection scoped encrypt- en decryptrechten niet respecteerde en verbetert de prestaties bij ontvangst van meerdere bunker requests.

### Aegis v0.4.0

[Aegis](https://github.com/ZharlieW/Aegis), de cross-platform signer, bracht [v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0) uit op 26 maart. De release voegt Full- en Selective-authorizationmodi toe in Instellingen en repareert meerdere QR-scanproblemen. Opvolgende commits [d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b), [3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7), [3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f) en [e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e) zetten datzelfde werk voort met batchselectiebediening, herbruikbare batchselectiestatistieken, set-all-groups selectie-API's en gebruiksstatistieken per permissie op de app permissions-pagina.

### Schemata v0.2.7 tot en met v0.3.0

[Schemata](https://github.com/nostrability/schemata), de JSON Schema-definities voor het valideren van Nostr event kinds, bracht vier releases uit van [v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7) tot [v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0) met 21 gemergede PR's. De v0.3.0-release brengt fixes voor patroonconsistentie over relay-URL's, hex-ID's, MIME-types en BOLT-11-strings heen ([PR #126](https://github.com/nostrability/schemata/pull/126)), gecentraliseerde relay-URL-patronen ([PR #117](https://github.com/nostrability/schemata/pull/117)), [NIP-19](/nl/topics/nip-19/) bech32-basistype-schema's ([PR #118](https://github.com/nostrability/schemata/pull/118)) en validatie voor kind 777 spell-events ([PR #125](https://github.com/nostrability/schemata/pull/125)). De releasepipeline publiceert nu bij elke release een kind `1` note op Nostr ([PR #120](https://github.com/nostrability/schemata/pull/120)), zodat het project zichzelf aankondigt via het protocol dat het valideert. Schemata ondersteunt nu naast het canonieke JS/TS-pakket ook Rust, Go, Python, Kotlin, Java, Swift, Dart, PHP, C#/.NET, C++, Ruby en C.

Naast Schemata publiceerde het team ook [schemata-codegen](https://github.com/nostrability/schemata-codegen), een experimentele codegenerator die een andere benadering kiest voor hetzelfde validatieprobleem. Waar de validatorpakketten van Schemata een JSON Schema-runtimeafhankelijkheid vereisen, vertaalt schemata-codegen schema's direct naar getypte native-language constructies (getypte tag-tuples, kind-interfaces en runtime validators), waardoor een validatorbibliotheek tijdens runtime niet nodig is. De [vergelijking codegen-vs-validators](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md) documenteert wanneer welke aanpak het beste past.

### BigBrotr v6.5.0 tot en met v6.5.4

[BigBrotr](https://github.com/BigBrotr/bigbrotr), het relay-analyseplatform, bracht vijf releases uit van [v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0) tot [v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4). v6.5.0 centraliseert relay-URL-validatie met een `parse_relay_url()` factory function en voegt controle op URL-lengte en pad-sanitization toe. Ook de monitoringinfrastructuur kreeg fixes: announcement-events bevatten nu geohash-locatietags (volgens [NIP-52](/nl/topics/nip-52/)), en timeoutbescherming werd toegevoegd aan de Geo/Net [NIP-66](/nl/topics/nip-66/)-metadatatests die eerder geen deadline hadden en onbeperkt konden blijven hangen. [PR #410](https://github.com/BigBrotr/bigbrotr/pull/410) upgrade PostgreSQL van 16 naar 18, wat het async I/O-subsysteem en betere WAL-throughput naar de relay-analysepipeline brengt.

### Vertex Lab-relay voegt NIP-50-profielsearch toe

[Vertex Lab](https://vertexlab.io), het team achter [npub.world](https://github.com/vertex-lab/npub.world) en de [Vertex](https://vertexlab.io/docs) Web of Trust-engine, kondigde aan dat `wss://relay.vertexlab.io` nu [NIP-50](/nl/topics/nip-50/) (Search) ondersteunt voor profielqueries. NIP-50 breidt de standaard Nostr `REQ`-filter uit met een `search`-veld, zodat clients full-text zoekqueries naar relays kunnen sturen die indexering ondersteunen. Profielsearch toevoegen aan een relay die al Web of Trust-data levert, betekent dat clients verbonden met `relay.vertexlab.io` gebruikers op naam of beschrijving kunnen ontdekken zonder aparte zoekdienst.

### Hashtree v0.2.17 en v0.2.18 leveren WebRTC-mesh en Iris Desktop

[Hashtree](https://github.com/mmalmi/hashtree), mmalmi's content-addressed blobopslagsysteem dat Merkle roots op Nostr publiceert, bracht [v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17) en [v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18) uit op 31 maart. Die twee releases sluiten een sprint van 30 commits af die drie aparte capaciteiten toevoegt. Ten eerste voegt de `hashtree-webrtc` crate (hernoemd naar `hashtree-network` in v0.2.18) WebRTC-gebaseerde peer-to-peer distributie van blobs toe met uniforme mesh-signalering over de Rust CLI, de simulation harness en de TypeScript-client. Ten tweede bouwt de releasepipeline nu Windows-artefacten (CLI zip en Iris installer), waardoor er dekking is voor macOS, Linux en Windows. Ten derde bundelen beide releases Iris Desktop 0.1.0, mmalmi's Nostr social client, als AppImage-, .deb- en Windows-installer-assets naast de hashtree CLI. [Hashtree werd voor het eerst behandeld in Newsletter #10](/nl/newsletters/2026-02-18-newsletter/) toen het lanceerde als een op filesystems gebaseerde [Blossom](/nl/topics/blossom/)-compatibele store. De WebRTC-laag is de eerste stap richting peer-to-peer distributie van content zonder afhankelijkheid van gecentraliseerde Blossom-servers.

### Nostr Mail Client v0.7.0 tot en met v0.7.2

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client), de Flutter mailachtige client gebouwd op Nostr-identiteiten, bracht [v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0), [v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1) en [v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2) uit in drie dagen. Het zichtbare productwerk draaide om onboarding ([PR #9](https://github.com/nogringo/nostr-mail-client/pull/9)) en profielbewerking ([PR #10](https://github.com/nogringo/nostr-mail-client/pull/10)), twee basisstukken voor elke client die Nostr als mailbox wil presenteren. De latere point releases verpaktten dat werk in nieuwe Android- en Linux-builds.

### Wisp v0.14.0 tot en met v0.16.1

[Wisp](https://github.com/barrydeen/wisp), de Android Nostr-client, bracht nog 13 releases uit van [v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta) tot [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta). Het werk deze week omvat fixes voor NIP-17 rumor JSON ([PR #385](https://github.com/barrydeen/wisp/pull/385)), repostbadges op gallery cards ([PR #383](https://github.com/barrydeen/wisp/pull/383)), uitklapbare reactiedetails ([PR #382](https://github.com/barrydeen/wisp/pull/382)), persistente emoji-sets ([PR #381](https://github.com/barrydeen/wisp/pull/381)) en videobediening voor autoplay ([PR #380](https://github.com/barrydeen/wisp/pull/380)). De nieuwste [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta) repareert ook custom emoji-shortcodes met koppeltekens en ontbrekende emoji-tags.

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app) bracht [3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17) uit op 24 maart. [PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000) mapt WalletException-types naar foutcodes in NWC-antwoorden, zodat [NIP-47](/nl/topics/nip-47/) clients gestructureerde foutinformatie krijgen in plaats van generieke fouten. [PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995) repareert poll-zap-stemmen die als Top Zaps verschenen, en [PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998) verbergt walletsaldo en actieknoppen wanneer geen wallet is geconfigureerd.

### OpenChat v0.2.4 tot en met v0.3.0

[OpenChat](https://github.com/DavidGershony/openChat), de Avalonia-gebaseerde chatclient gebouwd op de [Marmot](/nl/topics/marmot/)-stack, bracht in vier dagen zes releases uit van [v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4) tot [v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0). De commitlog vertelt het verhaal van een client die de kloof dicht tussen "Marmot works" en "someone can actually use this daily." [NIP-42](/nl/topics/nip-42/) relay-authenticatie landde, gevolgd door een relay picker-UI met duplicate event filtering. Voice messages kregen pause, resume, seek en tijdsweergave. Het signerpad werd verhard: Amber-verbindingen werden gerepareerd met een bijgewerkt [NIP-46](/nl/topics/nip-46/) URI-formaat, de WebSocket reconnect automatisch vóór het versturen van requests, en dubbele Amber-requests worden nu onderschept door te controleren op replayed responses. Aan de opslagkant kregen Linux en macOS AES-256-GCM secure storage met file-backed keys, en user metadata-fetching gebruikt nu [NIP-65](/nl/topics/nip-65/) relay discovery en cachet resultaten in een lokale database.

### Igloo Signer 1.1

[Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype), de iOS [FROST](/nl/topics/frost/) threshold signer uit het FROSTR-project, bracht [v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1) uit op 28 maart. FROST (Flexible Round-Optimized Schnorr Threshold)-handtekeningen laten een groep signers gezamenlijk een Nostr-sleutelpaar beheren, waarbij elke t-of-n combinatie een event kan signeren zonder dat één partij de volledige privésleutel bezit. Igloo is een van de eerste mobiele implementaties van deze aanpak voor Nostr.

### nak v0.19.3 en v0.19.4

[nak](https://github.com/fiatjaf/nak), fiatjaf's command-line Nostr-toolkit, bracht [v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3) en [v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4) uit op 26 en 30 maart. Beide releases repareren panic-condities: [PR #118](https://github.com/fiatjaf/nak/pull/118) vervangt `strings.Split` door `strings.Cut` om een potentiële out-of-bounds access te voorkomen, en [PR #119](https://github.com/fiatjaf/nak/pull/119) voorkomt dezelfde klasse panic in curl-flag parsing.

### Flora v0.3.0

[Flora](https://github.com/shawnyeager/flora-extension), een Chrome-extensie voor gedecentraliseerde schermopname en -deling op Nostr, bracht [v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0) uit. De release voegt private encrypted video sharing toe met public, unlisted en private modi. Private opnames worden versleuteld met AES-256-GCM en aan ontvangers geleverd via [NIP-17](/nl/topics/nip-17/) (Private Direct Messages), zodat de opname nooit in platte tekst een server raakt.

### YakiHonne Mobile 2.0.3

[YakiHonne](https://github.com/YakiHonne/mobile-app), de mobiele Nostr-client, bracht [2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3) uit met relayreviews en join requests, uitgebreidere nested replies, automatische vertaling van notes en NWC multi-relay-ondersteuning.

## Projectupdates

### Zap Cooking voegt zap-polls en Branta-betalingsverificatie toe

[Zap Cooking](https://github.com/zapcooking/frontend), het recepten- en contentplatform, mergede deze week 11 PR's gericht op interactieve content en betalingsflows. [PR #277](https://github.com/zapcooking/frontend/pull/277) voegt zap-polls toe (kind 6969), waarbij gebruikers stemmen door sats te sturen en stemmerslijsten met profielfoto's kunnen bekijken. [PR #274](https://github.com/zapcooking/frontend/pull/274) herontwerpt de poll-UX zodat de steminterface natuurlijker in de feed past.

[PR #276](https://github.com/zapcooking/frontend/pull/276) voegt camera-gebaseerd QR-scannen toe aan de Send Payment-flow en integreert [Branta](https://branta.pro/), een verificatiedienst die controleert of een betalingsbestemming legitiem is vóór verzending. Branta controleert bestemmingen op phishing, address swaps en man-in-the-middle onderschepping. In de implementatie van Zap Cooking verschijnen een door Branta geverifieerde platformnaam en logo direct in de betaalflow, en Branta-enabled QR-codes kunnen `branta_id`- en `branta_secret`-parameters dragen zodat de wallet de bestemming direct uit de gescande code kan verifiëren.

### diVine legt de basis voor unified search en verhardt videolevering

[diVine](https://github.com/divinevideo/divine-mobile), de short-form videocliënt, besteedde de week aan het aanscherpen van search, feednavigatie, playback recovery en uploadgedrag. [PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540) legt de basis voor een unified search-scherm met gegroepeerde secties voor Videos, People en Tags. [PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623) verhardt pagination over profielfeeds, inbox, notificaties, discover lists, classic vines, search en de composable grid feeds door ze op een gedeelde pagination controller te zetten.

Ook videolevering kreeg meerdere concrete fixes. [PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643) probeert Divine-gehoste afgeleide bronnen opnieuw in volgorde en valt terug op de ruwe blob voordat een playbackfout wordt getoond, zodat tijdelijke storingen op één bron de playback niet meteen stoppen. [PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634) houdt resumable uploads op het Divine-owned pad wanneer capability probing tijdelijk faalt, wat gebroken uploads door korte netwerkstoringen vermindert. [PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637) verandert ook de sensitive-content-gate zodat video's alleen hard worden geblokkeerd voor echte waarschuwingslabels, niet enkel voor door makers aangeleverde content warning labels.

### Shopstr voegt custom storefronts toe en Milk Market blijft marktplaatswerk leveren

[Shopstr](https://github.com/shopstr-eng/shopstr), de Nostr-gebaseerde marktplaats, mergede [PR #245](https://github.com/shopstr-eng/shopstr/pull/245) dat custom storefronts toevoegt. Daardoor krijgen verkopers een onderscheidender thuisoppervlak in plaats van dat elke listing in dezelfde generieke presentatie wordt gedwongen.

[Milk Market](https://github.com/shopstr-eng/milk-market), een gespecialiseerde marktplaats voor melk, ging verder met storefront-optimalisaties ([PR #18](https://github.com/shopstr-eng/milk-market/pull/18)), account recovery ([PR #17](https://github.com/shopstr-eng/milk-market/pull/17)), beef splits ([PR #15](https://github.com/shopstr-eng/milk-market/pull/15)) en typefixes voor MCP-tools ([PR #16](https://github.com/shopstr-eng/milk-market/pull/16)).

### Notedeck voegt geluidseffecten toe en trekt zijn updaterpad door naar Android

[Notedeck](https://github.com/damus-io/notedeck), de desktopclient van het Damus-team, mergede [PR #1412](https://github.com/damus-io/notedeck/pull/1412) dat een sound effects-subsysteem toevoegt met UI-interactiegeluiden via rodio, en [PR #1399](https://github.com/damus-io/notedeck/pull/1399) met Agentium-updates waaronder een CLI-titelvlag en inklapbare sessiemappen. Een open [PR #1417](https://github.com/damus-io/notedeck/pull/1417) stelt APK self-update via Nostr/Zapstore op Android voor, voortbouwend op [het Nostr-native updaterwerk van Notedeck uit Newsletter #14](/nl/newsletters/2026-03-18-newsletter/#notedeck-verplaatst-release-ontdekking-naar-nostr).

### Nostria voegt repost-relayhints en NIP-98-alignering toe

[Nostria](https://github.com/nostria-app/nostria) mergede [PR #583](https://github.com/nostria-app/nostria/pull/583) dat [NIP-18](/nl/topics/nip-18/) (Reposts)-relayhints toevoegt aan repost-`e` tags voor kind 6- en kind 16-events, [PR #582](https://github.com/nostria-app/nostria/pull/582) dat Brainstorm HTTP auth (kind 27235) in lijn brengt met verplichte tags van [NIP-98](/nl/topics/nip-98/) (HTTP Auth), en [PR #576](https://github.com/nostria-app/nostria/pull/576) dat Schemata-schema-validatietests toevoegt. Die NIP-98-wijziging betekent dat Nostria zich bij externe diensten kan authenticeren met hetzelfde HTTP-auth-formaat dat andere clients gebruiken.

### Nostr-Doc voegt desktop packaging en offline-first werk toe

[Nostr-Doc](https://github.com/formstr-hq/nostr-docs), de collaboratieve editor van Form*, had een drukke week met packaging- en editorwerk. [commit fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4) voegt een desktopapp toe, [commit 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927) start native appwerk, en [commit 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869) duwt de app richting offline-first gedrag. Aan de editorzijde voegt [commit 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786) Ctrl+S opslaan toe, waarschuwingen bij opslaan, fixes voor link previews en gecorrigeerde weergave van strikethrough.

### rust-nostr optimaliseert NIP-21-parsing en voegt relay-side NIP-62-ondersteuning toe

[rust-nostr](https://github.com/rust-nostr/nostr) mergede acht PR's. De opvallendste is [PR #1308](https://github.com/rust-nostr/nostr/pull/1308), die [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) URI-parsing in `PublicKey::parse` optimaliseert door deze op één lijn te brengen met standaard bech32-parsingprestaties. Eerder duurde het parsen van NIP-21 URI's grofweg twee keer zo lang als ruwe bech32-sleutels. Het project heeft daarnaast vier open PR's die relay-specifieke [NIP-62](/nl/topics/nip-62/) (Request to Vanish)-ondersteuning toevoegen over de memory-, LMDB-, SQLite- en database test-backends heen ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)).

### nostr-tools voegt bunker-relaycontrole toe en repareert NIP-47 multi-relay parsing

[nostr-tools](https://github.com/nbd-wtf/nostr-tools) mergede [PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530) dat `skipSwitchRelays` toevoegt aan BunkerSignerParams voor handmatig relaybeheer, en [PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529) dat [NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect)-parsing van connection strings repareert zodat meerdere relays worden ondersteund zoals de specificatie toelaat.

### Nostrability integreert Sherlock-auditdata en publiceert Schemata-overzicht

[Nostrability](https://github.com/nostrability/nostrability), de interoperabiliteitstracker voor Nostr-clients, mergede 14 PR's. [PR #306](https://github.com/nostrability/nostrability/pull/306) integreert Sherlock-scanstatistieken in het dashboard. Sherlock is Nostrability's geautomatiseerde audittool die verbinding maakt met Nostr-clients, de events vastlegt die zij publiceren en elk event valideert tegen de Schemata JSON Schema-definities om specificatieovertredingen te detecteren. Het dashboard toont nu schema-fail rates per client ([PR #315](https://github.com/nostrability/nostrability/pull/315)), zodat ontwikkelaars kunnen zien welke event kinds hun client verkeerd krijgt. [PR #323](https://github.com/nostrability/nostrability/pull/323) herziet de Nostr-publicatieworkflow zodat release-aankondigingen als aparte job draaien die niet geannuleerd kan worden door eerdere CI-stappen.

elsat publiceerde op 30 maart ook [Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww), waarin wordt beschreven hoe schemata, schemata-codegen en Sherlock in elkaar passen, samen met de actuele dekking: 179 event-kind-schema's over 65 NIPs, 154 tag-schema's, 13 protocolberichten en 310 voorbeeld-events.

### Nalgorithm voegt digestgeneratie en lokale scorecaching toe

[Nalgorithm](https://github.com/jooray/nalgorithm), een nieuw project voor relevantie-gerangschikte Nostr-feeds, begon deze week met publieke ontwikkeling. [commit cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43) legt de eerste webapp vast die posts van follows ophaalt en ze scoort tegen een door de gebruiker gedefinieerde voorkeursprompt. [commit 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86) voegt een CLI-digesttool toe die topgerangschikte posts omzet in een gesproken samenvatting, terwijl [commit 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153) file-based scorecaching en incrementele evolutie van learned prompts vanuit recente likes toevoegt. [commit c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03) stopt ook met het cachen van fallback-scores uit mislukte batches, zodat een tijdelijke scoringsfout de ranking van een post niet permanent afvlakt.

### TENEX voegt RAG vector store en gerichte MCP-startup toe

[TENEX](https://github.com/tenex-chat/tenex), het Nostr-native agentframework dat AI-agents via Telegram aan Nostr-kanalen koppelt, mergede deze week zeven PR's. [PR #101](https://github.com/tenex-chat/tenex/pull/101) voegt een plugbare vector store-abstractie toe met SQLite-vec-, LanceDB- en Qdrant-backends, waardoor agents retrieval-augmented generation krijgen zonder vast te zitten aan één vector database. [PR #102](https://github.com/tenex-chat/tenex/pull/102) maakt MCP-startup gericht: alleen MCP-servers waarvan de tools daadwerkelijk gebruikt worden, worden gestart in plaats van alles gretig op te starten bij eerste uitvoering. [PR #100](https://github.com/tenex-chat/tenex/pull/100) voegt een `send_message` tool toe zodat agents met Telegram-kanaalbindingen proactief berichten kunnen versturen in plaats van alleen te reageren op inkomende berichten. [PR #106](https://github.com/tenex-chat/tenex/pull/106) vermijdt een subprocess-spawn die een Bun/JSC-geheugenvoorallocatie van 9 GB triggerde door `.git/HEAD` direct te lezen in plaats van `git branch` uit te voeren.

### Dart NDK verplaatst Amber-signer en voegt Alby Go 1-click toe

[Dart NDK](https://github.com/relaystr/ndk), de Flutter Nostr development kit, noteerde 11 gemergede PR's. [PR #525](https://github.com/relaystr/ndk/pull/525) verplaatst Amber-signerondersteuning naar het ndk_flutter-pakket, en [PR #552](https://github.com/relaystr/ndk/pull/552) voegt Alby Go one-click wallet connection toe aan de sample-app. [PR #502](https://github.com/relaystr/ndk/pull/502) voegt een install.sh-script toe voor de CLI, en [PR #523](https://github.com/relaystr/ndk/pull/523) verwijdert de Rust verifier-afhankelijkheid ten gunste van native asset-afhandeling.

## Protocol- en specificatiewerk

### Marmot verplaatst KeyPackages naar addressable events en verscherpt pushnotificaties

De [Marmot-specificatie](https://github.com/marmot-protocol/marmot) mergede vier PR's die veranderen hoe het protocol sleutelmateriaal en groepslidmaatschap afhandelt. [PR #54](https://github.com/marmot-protocol/marmot/pull/54) migreert KeyPackage-events van regulier `kind:443` naar addressable `kind:30443` met een `d` tag, waardoor [NIP-09](/nl/topics/nip-09/) eventverwijdering tijdens sleutelrotatie niet meer nodig is. Addressable events overschrijven op hun plaats, wat rotatie self-contained maakt. [PR #57](https://github.com/marmot-protocol/marmot/pull/57) laat niet-admingebruikers SelfRemove-proposals committen (vrijwillig vertrek uit een groep), en [PR #62](https://github.com/marmot-protocol/marmot/pull/62) vereist dat admins eerst hun adminstatus opgeven voordat ze SelfRemove gebruiken, zodat een admin niet kan verdwijnen terwijl die nog elevated privileges heeft.

[PR #61](https://github.com/marmot-protocol/marmot/pull/61) verscherpt het [MIP-05](/nl/topics/mip-05/)-pushnotificatieformaat en maakt single-blob base64-encoding, versioning, token wire format en x-only key-gebruik expliciet. Het effect is één gedefinieerde wirerepresentatie voor token blobs en x-only keys over specificatie, client libraries en app-backends heen. Implementatie van deze specwijzigingen landde deze week in de White Noise-stack en wordt hierboven behandeld in de [White Noise v2026.3.23-sectie](#white-noise-repareert-relay-churn-en-breidt-clientbesturing-uit).

### NIP-Updates

Recente wijzigingen in het [NIPs-repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md): Static Websites** ([PR #1538](https://github.com/nostr-protocol/nips/pull/1538)): Definieert kind `15128` (rootsite) en kind `35128` (benoemde site) manifestevents voor het hosten van statische websites onder Nostr-sleutelparen met Blossom-opslag. Zie de [deep dive hieronder](#nip-deep-dive-nip-5a-static-websites).

- **[NIP-30](/nl/topics/nip-30/) (Custom Emoji): Allow hyphens in shortcodes** ([PR #2297](https://github.com/nostr-protocol/nips/pull/2297)): Werkt de beschrijving van shortcodes bij om ook koppeltekens toe te staan. Shortcodes met koppeltekens worden in de praktijk al gebruikt sinds de introductie van het NIP, dus de specificatie documenteert nu bestaand gebruik.

**Open PR's en discussies:**

- **NIP-C1: Agent TUI Messages** ([PR #2295](https://github.com/nostr-protocol/nips/pull/2295)): Stelt een gestructureerd berichtformaat voor waarmee agents interactieve UI-elementen via versleutelde DM's kunnen sturen, inclusief getypte `text`, `buttons`, `card` en `table` payloads. Het concept houdt alles binnen bestaande [NIP-17](/nl/topics/nip-17/) en [NIP-04](/nl/topics/nip-04/) direct-message-content als JSON. Het definieert geen nieuw event kind en gebruikt een eenvoudig callback-stringformaat voor knopreacties.

- **NIP-95: Hybrid Peer-to-Peer Relay Protocol** ([PR #2293](https://github.com/nostr-protocol/nips/pull/2293)): Stelt een hybride relaymodel voor waarin relays autoritatief blijven maar ook peer-to-peer distributie van recente events via WebRTC kunnen coördineren. Het concept introduceert relay-berichten zoals `PEER_REGISTER`, `PEER_REQUEST` en `PEER_OFFER`, met stabiele clients als Super Peers en de relay als seed node en fallback.

- **NIP-B9: Zap Poll Events** ([PR #2284](https://github.com/nostr-protocol/nips/pull/2284)): Opent het oude NIP-69 zap-pollidee opnieuw nu [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) (Polls) gratis polls afdekt. Het concept gebruikt kind `6969` polldefinities en kind `9734` zaps als stemmen, waardoor een betaald pollsysteem ontstaat met economische Sybil-resistentie als aanvulling op gratis one-key-one-vote polls.

- **NIP-AD: Super Zap** ([PR #2289](https://github.com/nostr-protocol/nips/pull/2289)): Stelt een conventie voor waarbij zaps verzonden naar de pubkey van een relay of client worden weergegeven als gespecialiseerde promotionele notes, en zo van zap receipts een advertentieoppervlak maken. Relayoperators en clients zouden profielen met `lud16` publiceren, die receipts ophalen, de ingebedde content uit zap descriptions extraheren, en optioneel minimum-satsdrempels instellen om spam te onderdrukken.

- **NIP-XX: Agent Reputation Attestations** ([PR #2285](https://github.com/nostr-protocol/nips/pull/2285)): Stelt kind `30085` voor als parameterized replaceable event voor gestructureerde reputatie-attestaties over Nostr-agents. Het concept vermijdt één globale score door reputatie waarnemer-afhankelijk te maken, voegt tijdsverval toe zodat oude attestaties vervagen, ondersteunt negatieve ratings met bewijsvereisten, en schetst zowel eenvoudige gewogen scoring als graph-diversity scoring voor betere Sybil-resistentie.

- **NIP-XX: Paid API Service Announcements** ([PR #2291](https://github.com/nostr-protocol/nips/pull/2291)): Stelt kind `31402` addressable events voor om betaalde HTTP API's te adverteren, met Nostr voor discovery en HTTP 402 voor betaling. Het concept is tags-first zodat relays kunnen filteren op betaalmethoden, prijzen en capabilities zonder JSON-content te parsen, en laat optionele request- en response-schema's toe zodat clients of agents automatisch calls kunnen genereren.

- **NIP-XX: Key Derivation from LNURL-auth via SplitSig** ([PR #2294](https://github.com/nostr-protocol/nips/pull/2294)): Stelt voor een Nostr-sleutelpaar af te leiden uit een LNURL-auth ECDSA-handtekening gecombineerd met een client-side random nonce. De formule is `nsec = SHA256(ecdsa_signature || nonce)`. De server ziet de ECDSA-handtekening, inherent aan de LNURL-auth-handshake, maar ziet de nonce nooit; de browser genereert de nonce, maar beheert de handtekening niet. Geen van beide delen kan alleen de nsec afleiden. Het beoogde resultaat is dat dezelfde Lightning-wallet op meerdere apparaten dezelfde Nostr-sleutel produceert, met de wallet als recovery anchor en zonder dat een server de privésleutel kan reconstrueren.

- **[NIP-55](/nl/topics/nip-55/): Document rejected field** ([PR #2290](https://github.com/nostr-protocol/nips/pull/2290)): Documenteert het `rejected`-veld voor intent-based signer-antwoorden en formaliseert daarmee het gedrag waar [de v1.07.x-fix van Amethyst](#amethyst-brengt-vastgepinde-notes-relaybeheer-en-request-to-vanish) omheen moest werken.

## NIP Deep Dive: NIP-5A (Static Websites)

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) definieert hoe statische websites onder Nostr-sleutelparen kunnen worden gehost, met twee event kinds en bestaande blobopslaginfrastructuur om ondertekende events om te zetten in geserveerde webpagina's. De [specificatie](https://github.com/nostr-protocol/nips/blob/master/5A.md) werd op 25 maart gemerged via [PR #1538](https://github.com/nostr-protocol/nips/pull/1538).

Het model gebruikt kind `15128` voor een rootsite, één per pubkey, en kind `35128` voor benoemde sites die met een `d` tag worden geïdentificeerd. Elk manifest koppelt absolute URL-paden aan SHA256-hashes. Hieronder staat een rootsite-manifest:

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

De serveerflow werkt in drie stappen. Een hostserver ontvangt een HTTP-verzoek, haalt de pubkey van de auteur uit het subdomein (voor rootsites een npub, voor benoemde sites een base36-gecodeerde pubkey), haalt de relaylijst van de auteur op via [NIP-65](/nl/topics/nip-65/) en queryt het sitemanifest. Zodra het manifest is gevonden, resolveert de server het opgevraagde pad naar een inhoudshash, downloadt de overeenkomende blob van de Blossom-server of servers in de `server` tags, en retourneert het bestand.

Het DNS-subdomeinformaat is strikt gespecificeerd. Rootsites gebruiken de standaard npub als subdomein. Benoemde sites gebruiken een 50-karakterige base36-codering van de ruwe pubkey gevolgd door de `d` tagwaarde, allemaal in één DNS-label. Omdat DNS-labels beperkt zijn tot 63 karakters en de base36-codering altijd 50 gebruikt, is de `d` tag beperkt tot 13 karakters. De specificatie vereist ook dat `d` tags overeenkomen met `^[a-z0-9-]{1,13}$` en niet eindigen op een koppelteken, om ambiguïteit bij DNS-resolutie te voorkomen.

Door inhoudshashes te gebruiken kan dezelfde site door verschillende hostservers worden geserveerd en is bestandsintegriteit controleerbaar zonder de server te vertrouwen. Een hostserver hoeft zelf geen bestanden op te slaan. Hij haalt ze op aanvraag uit Blossom op basis van de hashes in het manifest. Dat betekent dat de auteur bepaalt wat wordt geserveerd, de Blossom-server de ruwe bestanden bewaart en de hostserver die twee verbindt. Elk van die drie componenten kan onafhankelijk worden vervangen.

Bestaande implementaties zijn onder meer [nsite](https://github.com/lez/nsite), de hostserver die manifesten resolveert en bestanden serveert, en [nsite-manager](https://github.com/hzrd149/nsite-manager), een UI voor het bouwen en publiceren van manifesten. De specificatie voegde ook een `source` tag toe om te linken naar de broncoderepository van de site, en een afzonderlijke README-update in [PR #2286](https://github.com/nostr-protocol/nips/pull/2286) registreerde zowel kind `15128` als `35128` in de NIP kind-index.

## NIP Deep Dive: NIP-62 (Request to Vanish)

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md) definieert kind `62` als een verzoek aan relays om alle events van de aanvragende pubkey te verwijderen. De [specificatie](https://github.com/nostr-protocol/nips/blob/master/62.md) is juridisch gemotiveerd: in rechtsgebieden met right-to-be-forgotten-wetten geeft een gestandaardiseerd, ondertekend verwijderverzoek relayoperators een duidelijk signaal om te handelen.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

De specificatie maakt onderscheid tussen gerichte en globale vanish-verzoeken. Een gericht verzoek bevat specifieke `relay` tags die aangeven welke relays moeten handelen. Een globaal verzoek gebruikt de letterlijke string `ALL_RELAYS` als relay-tagwaarde en vraagt elke relay die het event ziet om alle events van die pubkey te verwijderen. Relays die voldoen, moeten er ook voor zorgen dat verwijderde events niet opnieuw in de relay kunnen worden uitgebroadcast, zodat de verwijdering sticky wordt.

NIP-62 gaat in zowel reikwijdte als intentie verder dan [NIP-09](/nl/topics/nip-09/) (Event Deletion). NIP-09 laat je individuele events verwijderen, en relays MOGEN daaraan voldoen. NIP-62 vraagt om verwijdering van alles, en de specificatie zegt dat relays MOETEN voldoen als hun URL is getagd. Ook vraagt het relays om [NIP-59](/nl/topics/nip-59/) (Gift Wrap)-events te verwijderen die de aanvragende pubkey p-taggen, waardoor ook inkomende DM's samen met de events van de gebruiker worden opgeruimd. Een NIP-09-deletion publiceren tegen een NIP-62 vanish-verzoek heeft geen effect: zodra je vanished bent, kun je dat niet ongedaan maken door het vanish-verzoek te verwijderen.

Deze week bracht [Amethyst v1.07.0](#amethyst-brengt-vastgepinde-notes-relaybeheer-en-request-to-vanish) client-side NIP-62-ondersteuning uit, zodat gebruikers vanish-verzoeken vanuit de app kunnen starten. Aan relayzijde heeft [rust-nostr](https://github.com/rust-nostr/nostr) vier open PR's die NIP-62-ondersteuning toevoegen over de memory-, LMDB-, SQLite- en database test-backends heen ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)). Daarmee vallen client- en relayondersteuning in dezelfde week samen.

Het protocolontwerp introduceert een praktische spanning. De waardepropositie van Nostr omvat censuurbestendigheid, wat betekent dat relays publicatie niet zouden moeten kunnen verhinderen. NIP-62 introduceert een geval waarin een relay WEL herpublicatie van een specifieke pubkey moet verhinderen. Die twee eigenschappen kunnen naast elkaar bestaan omdat het verzoek zelfgericht is: je vraagt om verwijdering van je eigen events, niet die van iemand anders. De censuurbestendige eigenschap blijft voor iedereen intact behalve voor de persoon die er expliciet voor kiest zich terug te trekken.

---

Dat is het voor deze week. Bouw je iets of heb je nieuws om te delen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via [NIP-17](/nl/topics/nip-17/) (Private Direct Messages) DM</a> of vind ons op Nostr.
