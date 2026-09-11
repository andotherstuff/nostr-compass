---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "Nostr Compass #39 volgt ondertekende git-workflows, publiceren vanuit de browser, zelfgehoste livestreams, toestemming voor communityrelays, privé-events, gerichte releases en het linkcontract van NIP-21/NIP-27."
---

Welkom terug bij [Nostr Compass](https://nostrcompass.org), je wekelijkse gids voor Nostr.

**Deze week:** [ngit en GitWorkshop](https://ngit.dev/v3) brengen ondertekende git-workflows naar Nostr en [Blossom](/nl/topics/blossom/), [nsite-clay](https://github.com/jooray/nsite-clay) maakt publiceren vanuit de browser herstelbaar en [Wingman App](https://github.com/OtherStuffAI/wm-app) brengt browsen, lokaal ondertekenen, authenticatie en bestanden samen. [Shosho en Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) verbinden zelfgehoste streams met Nostr, [Communitator](https://github.com/dyne/communitator) maakt relay-sjablonen vóór ondertekening inspecteerbaar, [cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) publiceert tijdvakken voor afspraken en [Plektos](https://github.com/derekross/plektos/pull/16) versleutelt privé-events. Releases met tags voegen herstel- en privacywerk toe in [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4), [Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), [LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) en [SkateSpots](https://zapstore.dev/apps/org.skatespots.app). Het ontwikkelwerk omvat weergave volgens [NIP-27](/nl/topics/nip-27/), ondertekende relayvoorkeuren in [Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397), betalingsdoelen volgens [NIP-A3](/nl/topics/nip-a3/) en Blossom-mirrors. Samengevoegde wijzigingen in de [NIPs-repository](https://github.com/nostr-protocol/nips) verduidelijken uitsluitend live gebruikte abonnementen en geauthenticeerde applicatiegegevens. In onze diepgaande bespreking leggen we uit hoe links volgens [NIP-21](/nl/topics/nip-21/) en verwijzingen volgens NIP-27 Nostr-profielen en -events tussen applicaties overbrengen.

## Belangrijkste verhalen

### Ondertekende git-workflows brengen CI, privérepository's en releases naar Nostr

De [lancering van v3 op 8 september](https://ngit.dev/v3) brengt ngit, GitWorkshop, ngit-grasp en ngit-ci samen in één ondertekende workflow. [ngit](https://ngit.dev/ngit.git) verwerkt branches, patches en pull requests als events volgens [NIP-34](/nl/topics/nip-34/), terwijl [GitWorkshop](https://ngit.dev/gitworkshop.git) de beoordelingsinterface biedt. De lancering voegt ngit-ci 0.1 toe, een zelfgehoste dienst voor continue integratie waarvan de instructies en resultaten als ondertekende Nostr-events worden uitgewisseld. Daardoor kunnen controles naast de codebeoordeling worden uitgevoerd op hardware die door beheerders wordt gecontroleerd.

Dezelfde release biedt [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) privérepository's via de GRASP-08-extensie voor privérepository's en maakt de bevoegdheid van beheerders expliciet. Ondertekende releasegegevens kunnen verwijzen naar bestanden in [Blossom](/nl/topics/blossom/), zodat zowel de releasemetadata als de inhoudsgeadresseerde bestanden buiten een gehoste forge blijven. De [nieuwe documentatiesite](https://ngit.dev/v3) brengt de onderdelen voor de client, privérepository's, CI en het web samen.

### nsite-clay maakt publiceren vanuit de browser herstelbaar

Een [oplossing van 31 augustus voor signer-prompts](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), [herstel van publicaties](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0) en [bewerkingsfuncties van 2 september](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) maken van [nsite-clay](https://github.com/jooray/nsite-clay) een browsertool voor het publiceren van een site met één pagina. Een gebruiker bewerkt het document object model direct, serialiseert het resultaat, uploadt het als een inhoudsgeadresseerde [Blossom](/nl/topics/blossom/)-blob en publiceert het [NIP-5A](/nl/topics/nip-5a/)-manifest van de site opnieuw. Er is geen lokale build of server nodig.

De [browserpublisher](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) maakt herstel na een mislukte publicatie nu mogelijk en vermindert het aantal herhaalde signer-prompts, terwijl de [bewerkingsgids](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) de cyclus documenteert. Het resultaat blijft een reguliere NIP-5A-site voor bestaande gateways.

### Wingman App brengt browsen, ondertekenen en bestanden samen

Het werk in september voegt [bestandskiezers](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), [profielpublicatie](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), [veilig herstel van signer en sessie](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6) en [geteste mobiele builds](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac) toe aan [Wingman App](https://github.com/OtherStuffAI/wm-app). De Flutter-shell injecteert een [NIP-07](/nl/topics/nip-07/)-provider in pagina's die binnen de app worden geopend, terwijl Flight Deck en de door Tower ondersteunde Drive naast de browser een werkoppervlak en bestandswerkruimte bieden.

Wingman ondertekent geauthenticeerde HTTP-verzoeken met [NIP-98](/nl/topics/nip-98/). De [implementatie van verzoeken](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) stelt het event samen dat een server controleert voordat die antwoordt. Zo krijgt één geïnstalleerde identiteit een consistent goedkeuringsproces voor relayacties, het ondertekenen vanuit webapps en bestanden.

### Shosho brengt zelfgehoste streams van Livelier

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) verscheen op 1 september met ondersteuning voor [Livelier](https://github.com/r0d8lsh0p/livelier), waarvan de [update van de bronvermelding van 31 augustus](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc) de bridge en de Owncast-bron vermeldt in gekoppelde profielen. Livelier volgt de openbare directory van Owncast, controleert of een videostream live is en publiceert vervolgens een adresseerbaar `kind:30311`-[NIP-53](/nl/topics/nip-53/)-event. Ontdekking verloopt via Nostr, terwijl de video op de server van de streamer blijft.

Chat gaat via de bridge als `kind:1311`-events. Het [bridgeontwerp](https://github.com/r0d8lsh0p/livelier) opent alleen een verbinding aan de bronzijde zolang een Nostr-lezer geabonneerd is, labelt afgeleide identiteiten en stuurt tijdelijke chatberichten naar een relay die ze na drie uur verwijdert. De relay voor ontdekking accepteert schrijfacties voor live-events uitsluitend van de bridgesleutel. De chatrelay gebruikt [NIP-42-authenticatie](/nl/topics/nip-42/) en [NIP-70-vlaggen voor beschermde events](/nl/topics/nip-70/).

### Communitator maakt relaytemplates vóór ondertekening inspecteerbaar

De [reeks lanceringen van 31 augustus](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c) voorziet [Communitator](https://github.com/dyne/communitator) van canonieke templates voor relaylijsten van kind `10002`, Blossom-servers van kind `10063` en inboxen voor privéberichten van kind `10050`. Voordat een ondertekenaar verbinding maakt, toont de applicatie genormaliseerde eindpunten, lees- en schrijfrechten, event kinds, vaste publicatierelays en bestemmingen.

De [begrensde procedure voor ondertekening en publicatie](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501) scheidt het verbinden van het toepassen. Elk event wordt afzonderlijk ondertekend, één uitvoering gebruikt maximaal vier WebSocket-verbindingen en een bestemming telt pas mee na een positieve [NIP-01](/nl/topics/nip-01/) `OK`. De resultaten maken onderscheid tussen volledige, gedeeltelijke, mislukte en geannuleerde bezorging. Gedeelde templates blijven niet-vertrouwde aanbevelingen. Het [toestemmingsscherm](https://github.com/dyne/communitator#security-and-consent) legt uit in hoeverre relays en netwerkactiviteit waarneembaar zijn.

### cal.emre.xyz publiceert beschikbaarheid voor afspraken via NIP-52

De openbare repository werd geopend met een [eerste commit op 2 september](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743), gevolgd door een ondertekende [aankondiging van de handler op 3 september](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) voor [cal.emre.xyz](https://cal.emre.xyz). Een organisator publiceert beschikbaarheid als een `kind:31923`-[NIP-52](/nl/topics/nip-52/)-event. Een gast publiceert een `kind:31925`-RSVP.

De toepassing leest events van de organisator en geaccepteerde bezette RSVP's uit relays, sluit overlappende tijdsperioden uit en behoudt Nostr-events als het planningsregister zonder ze naar een afzonderlijke database te kopiëren. Organisatoren kunnen ondertekenen met [NIP-07](/nl/topics/nip-07/), [NIP-46](/nl/topics/nip-46/) of een lokale sleutel. Gasten kunnen een afzonderlijke sleutel genereren. De [repository](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) stelt ook de resulterende `naddr` en agendalinks beschikbaar, waarbij e-mail standaard is uitgeschakeld.

### Plektos maakt van privé-events één versleuteld kanaal

De [implementatie van privé-events van 2 september](https://github.com/derekross/plektos/pull/12) maakt van elke bijeenkomst in [Plektos](https://github.com/derekross/plektos) een privékanaal binnen een versleutelde [Concord](/nl/topics/concord-protocol/)-community. De gastenlijst, het RSVP-overzicht, het inschrijfbord, de thread, bijdragen, omslagafbeeldingen, bewerkingen en verwijderingen worden samen versleuteld. Een uitnodiging bevat alleen de sleutel van dat event en er wordt geen agenda-event in platte tekst gepubliceerd.

De [levenscycluscontrole van 6 september](https://github.com/derekross/plektos/pull/14) verankert de id van de eventdefinitie voor directe opzoeking wanneer er meer dan 500 wraps bestaan, met behoud van een gepagineerde terugvaloptie. Uitnodigingsbundels verlopen 30 dagen nadat een event eindigt en kunnen worden uitgeschakeld, maar iemand die al een kanaalsleutel heeft verkregen, kan die behouden. Een afzonderlijke [reparatie voor parserbeveiliging](https://github.com/derekross/plektos/pull/16) zorgt ervoor dat onjuist gevormde type-length-value (TLV)-[NIP-19](/nl/topics/nip-19/)-identifiers mislukken in plaats van de parser vast te laten lopen.

## Getagde releases

### Vector 0.4.4 maakt herstel van versleutelde communities veiliger

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) verscheen op 31 augustus met oplossingen voor communityherstel, sleutelrotatie, moderatie en de routering van antwoorden. Bij heroprichting wordt een aangevallen community afgesloten voor het uitnodigingspad dat door aanvallers werd gebruikt. Vervangend lidmaatschap heeft voorrang op verouderde lokale status en één onbereikbaar lid bevriest niet langer het ledenoverzicht. Lege rotaties worden geweigerd, promoties behouden online leden en bewerkingen worden niet uitgevoerd wanneer vereiste leden niet bereikbaar zijn.

De [release](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) bewaart ook verwijderingen en verbanningen door moderators, versleutelt het gastenboek opnieuw na een wachtwoordwijziging, koppelt antwoorden op meldingen na een herstart aan de bijbehorende conversatie en gebruikt uitsluitend geverifieerde multiplayerpaden. Dit zijn herstelmaatregelen, geen intrekking van reeds verkregen sleutels.

### Primal Android 3.5.27 controleert de identiteit van ondertekenaar en wallet

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) verscheen op 3 september nadat [de identiteitscontrole van de ondertekenaar](https://github.com/PrimalHQ/primal-android-app/pull/1108) en [authenticatie van walletverzoeken](https://github.com/PrimalHQ/primal-android-app/pull/1105) op 31 augustus waren samengevoegd. Lokale ondertekening weigert een verzoek waarvan de identiteit niet overeenkomt met het beheerde account, en inkomende [NIP-47](/nl/topics/nip-47/)-verzoeken worden vóór verwerking geauthenticeerd. De routering van zappeilingen stuurt stemmen ook naar de auteur van de peiling wanneer de peiling in een antwoord voorkomt.

### GRAIN 0.8.0-rc2 sluit een pad af waarbij gebeurtenissen wel werden bevestigd maar niet opgeslagen

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) verscheen op 7 september nadat een opslagfout ervoor had gezorgd dat `OK` kon worden gegeven voordat de asynchrone LMDB-databaseschrijver merkte dat de opslagcapaciteit vol was. De relay waarschuwt nu bij 80 en 95 procent, weigert bij 97 procent nieuwe gebeurtenissen maar laat ruimte over voor verwijdering, en meldt fouten van de schrijver die na acceptatie optreden. Het retentieproces werkt van oud naar nieuw, het afsluitproces verwerkt laat binnenkomende berichten en ongeldige filters leiden er niet langer toe dat geldige filters uit dezelfde groep worden genegeerd.

De [release](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) bevestigt ook monitoraankondigingen van kind `10166` en relayrapporten van kind `30166`, verwijdert verouderde rapporten, behoudt geconfigureerde relays als terugvaloptie en vermeldt actuele limieten en authenticatie in [NIP-11](/nl/topics/nip-11/) in plaats van statische nullen.

### LibreNostr 0.5.0–0.5.2 laat Tor-routering veilig stoppen bij fouten

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) verscheen op 7 september met een Orbot-modus die relays, zaps, uploads, media, afspelen en voorbeelden via één SOCKS-poort routeert, plus een oplossing voor een crash van het zapvenster. Als Orbot of de proxy niet beschikbaar is, worden verbindingen gestopt in plaats van ongemerkt over te schakelen op een directe route. [Versie 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) voorkomt dat trage [NIP-50](/nl/topics/nip-50/)-zoekopdrachten lokale resultaten vertragen; [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) vervangt de recursieve threadindeling en herstelt de volgorde van threads.

Het [veilig stoppende gedrag bij fouten](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) geldt voor elk netwerkoppervlak dat in de release wordt genoemd. Een herstart is vereist omdat deze clients lang actief blijven. De patchreleases behouden die keuze en beperken tegelijkertijd niet-gerelateerde problemen met zoeken, stackdiepte en indeling.

### SkateSpots voegt een relaypad op het apparaat toe

De ondertekende [Zapstore-release van 8 september](https://zapstore.dev/apps/org.skatespots.app) voegt een optionele Citrine-relay toe aan SkateSpots. Spots, crews, berichten en kaartgegevens kunnen lokaal worden geladen, berichten worden offline in een wachtrij geplaatst en de telefoon bewaart een lokale kopie. Bestaande inhoud in de stash en berichten blijft end-to-end versleuteld. Betalingscontroles vereisen factuurbedragen en door de provider uitgegeven zap-ontvangstbewijzen voordat toegang wordt verleend of bijdragen worden meegeteld.

De [lokale relay](https://zapstore.dev/apps/org.skatespots.app) is een optie voor opslag en continuïteit, geen vervanging voor elke externe relay. Hiermee kan een skater tijdens een periode zonder verbinding blijven werken en de ondertekende activiteit later synchroniseren. Tegelijkertijd voorkomen de betalingswijzigingen dat een zelf opgesteld ontvangstbewijs als bewijs van betaling kan dienen.

### Whistle 1.8.15 herstelt het lifecycle-herstel van versleutelde groepen

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) verscheen op 3 september nadat een Android-lifecycle-oplossing had voorkomen dat statusobjecten op routeniveau relay-abonnementen en locatie-updates voor de hele applicatie beëindigden. De release notes beschrijven ook een vernieuwde verbindingsstatus na vergrendeling of sluimerstand en, in het waargenomen geval, het herstel van een achterstand van 501 gebeurtenissen.

De [bug](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) koppelde het eigenaarschap van een langlevende service aan een kortlevend scherm. Door de aan de activity gebonden instantie actief te houden en de socket te controleren vóór een eenmalige leesactie, is de kans kleiner dat normale Android-navigatie en opschorting op de achtergrond eruitzien als een lege groep.

### TWENTY ONE Companion 1.12.0 scheidt versleutelde DM's van oudere chat

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) verscheen op 5 september met in gift wraps verpakte DM's volgens [NIP-17](/nl/topics/nip-17/). De versleutelde inbox staat los van de oudere space-chat, die afzonderlijk blijft omdat die berichten nooit zijn versleuteld en niet kunnen worden gemigreerd. PDF's en video's worden ondersteund voor zover het relaybeleid dit toestaat, en persoonlijke verbergingen worden gesynchroniseerd zonder moderatorblokkades te worden.

De [zichtbare scheiding](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) maakt deel uit van het beveiligingsmodel. De oude geschiedenis een beveiligde inbox noemen zou de herkomst ervan verkeerd voorstellen, terwijl een geruisloze migratie zou suggereren dat er versleuteling bestond toen de berichten werden geschreven.

### ZapStore 1.1.2 valideert event-id's en certificaatrotatie

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) verscheen op 4 september met validatie van event-id's volgens NIP-01: de client berekent de id van een inkomende gebeurtenis opnieuw en weigert de gebeurtenis bij een afwijking voordat deze wordt gebruikt. De release identificeert ook pakketten die buiten ZapStore zijn geïnstalleerd. Op de server zorgt [behoud van certificaathashes](https://github.com/zapstore/relay/pull/8) ervoor dat herhaalde `apk_certificate_hash`-tags behouden blijven, zodat bij rotatie van Android-ondertekeningssleutels een goedgekeurde afstammingslijn in stand kan blijven.

De [controle van de event-id](https://github.com/zapstore/zapstore/releases/tag/1.1.2) voorkomt dat een relay of cache tags of inhoud wijzigt en daarbij de oude id behoudt. De indicator voor de installatiebron biedt afzonderlijke informatie over de herkomst wanneer een Android-pakket met dezelfde applicatie-id via een ander kanaal afkomstig is.

### Amber 6.6.1 houdt antwoorden van de ondertekenaar herleidbaar

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) verscheen op 4 september nadat de verwerking van toestemmingen was aangepast om een ontbrekende optionele `kind` te accepteren, en afgewezen ondertekeningsverzoeken hun oorspronkelijke verzoek-id begonnen terug te sturen. Aanroepende applicaties kunnen een afwijzing zo koppelen aan de ingediende bewerking. De release werkt ook de standaardinstellingen voor externe ondertekenaars bij en voegt een indexer-relay toe.

Samen behouden deze [oplossingen](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) de herleidbaarheid in beide richtingen: een toestemmingsrecord blijft bruikbaar wanneer een optioneel veld ontbreekt, en een weigering blijft gekoppeld aan het verzoek dat deze veroorzaakte. De wijzigingen aan de standaardrelays beïnvloeden de vindbaarheid, maar vervangen de lokale autorisatiebeslissing van de ondertekenaar niet.

## In ontwikkeling

### Zap Cooking geeft NIP-27-verwijzingen met relayhints weer

[De merge van 4 september](https://github.com/zapcooking/frontend/pull/665) zorgt ervoor dat [Zap Cooking](https://github.com/zapcooking/frontend) verwijzingen naar `nostr:npub` en `nostr:nprofile` weergeeft in artikelen, recepten, editorvoorbeelden en afdrukweergaven. Ongeldige identifiers blijven als tekst staan, het opzoeken is niet-blokkerend en de editor toont een voorbeeld van de Markdown die zal worden ondertekend. Wanneer relayinformatie beschikbaar is, wordt een losse `npub` omgezet in een `nprofile` met outbox-relays en een overeenkomende `p`-tag.

In dezelfde week werden [auteursgebonden uitlezingen van kind `30023`](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7) hersteld, [geverifieerde NIP-50-zoekrelays](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea) toegevoegd met deduplicatie en controles op verouderde zoekopdrachten, en [NIP-47-walletaanroepen](https://github.com/zapcooking/frontend/pull/705) gerepareerd nadat wijzigingen in afhankelijkheden saldi en geschiedenis onbruikbaar hadden gemaakt.

### Conduit brengt ondertekende relay- en Blossom-voorkeuren met elkaar in overeenstemming

[Conduit](https://github.com/Conduit-BTC/conduit-mono) heeft op 2 september [bewerking van Blossom-voorkeuren](https://github.com/Conduit-BTC/conduit-mono/pull/374) en op 7 september [afstemming van ondertekende voorkeuren](https://github.com/Conduit-BTC/conduit-mono/pull/397) gemerged. Market en Merchant behouden de recentste geldige relaylijst van kind `10002` en inboxverklaring van kind `10050`, bewaren een bruikbare ondertekende lijst wanneer een nieuwere event ongeldig is, maken onderscheid tussen een expliciet lege lijst en een niet-beschikbare opzoekactie, en vervangen mislukte opgegeven relays niet door standaardwaarden uit de code.

Met [de editor voor kind `10063`](https://github.com/Conduit-BTC/conduit-mono/pull/374) kan een gebruiker een geordende lijst met HTTPS-mediaservers laden, herschikken, controleren, extern ondertekenen, publiceren en opnieuw uitlezen, zonder contact met die servers op te nemen of een niet-opgegeven standaardserver toe te voegen.

### NIP-A3-betaaldoelen bereiken drie clients

Van 1 tot en met 3 september implementeerden [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) en [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) NIP-A3-betaaldoelen van kind `10133`. Amethyst biedt alleen na expliciete toestemming een overdracht aan wanneer er een compatibel doel bestaat en maakt daar geen zap van; Grimoire gebruikt een vast register voordat wallet-URI's worden opgebouwd; Pollerama valideert Monero-adressen en haalt de relaylijst van de auteur op voordat doelen worden opgevraagd. Elke client heeft nog steeds een toegestane betaalmethode, een relayroute en een correcte weergave nodig.

### Ditto breidt Blossom-fallback en live-embeds uit

[Ditto](https://github.com/soapbox-pub/ditto) heeft op 6 september [brede Blossom-fallback en mirroring](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07) gemerged. Avatars, badges, banners, communityafbeeldingen, aangepaste emoji en applicatiepictogrammen proberen nu opgegeven servers met dezelfde blobhash; mirroruploads gebruiken een standaard BUD-11-autorisatietoken. Een [wijziging van 4 september](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa) voegde compacte livestream-embeds van `kind:30311` toe.

## Werk aan protocol en specificaties

### Mogelijkheden voor Nostr-implementaties

[NIP-01](/nl/topics/nip-01/) verduidelijkt nu [het filter `limit: 0`](https://github.com/nostr-protocol/nips/pull/2460), dat op 4 september werd gemerged. Een relay MOET geen opgeslagen events retourneren, MOET `EOSE` verzenden wanneer de initiële query's zijn voltooid en MOET het abonnement actief houden voor nieuwe overeenkomende events. Clients kunnen met één filterveld een uitsluitend live werkend abonnement openen en tegelijk de lokale geschiedenis behouden. De verduidelijking beschrijft compatibel gedrag van verschillende relayimplementaties en openbare relays.

Aan [NIP-78](/nl/topics/nip-78/) werd een [vereiste voor geauthenticeerde appgegevens](https://github.com/nostr-protocol/nips/pull/2458) toegevoegd, die op 3 september werd gemerged. Relays ZOUDEN [NIP-42](/nl/topics/nip-42/)-authenticatie moeten vereisen voor kinds `78` en `30078` en ZOUDEN deze alleen aan de geauthenticeerde auteur van de event moeten aanbieden. Dat is een aanbeveling, geen garantie van vertrouwelijkheid: clients kunnen willekeurige relays niet als privéopslag behandelen. De merge raadt ook af om aangepaste kinds voor appgegevens te gebruiken als algemene openbare uitwisselingsmethode.

[NIP-AC](/nl/topics/nip-ac/) werd op 4 september geopend als een expliciet open [voorstel voor WebRTC-signalering](https://github.com/nostr-protocol/nips/pull/2461). Het gebruikt voorlopige efemere kinds voor ping, verbindingsverzoeken, offers, answers en ICE candidates, geadresseerd met `p` en gegroepeerd via een sessiegebonden `e`-tag; kind `30600` ondersteunt ontdekking. Relays ZOUDEN die signaleringsevents moeten uitzenden en MOGEN ze NIET opslaan terwijl peers rechtstreeks verbinding maken. De nummers blijven voorlopig, clients ZOUDEN [NIP-65-relaylijsten](/nl/topics/nip-65/) moeten gebruiken en applicaties die vertrouwelijkheid nodig hebben ZOUDEN de inhoud van offers, answers en candidates met [NIP-44](/nl/topics/nip-44/) moeten versleutelen.

## Uitgelichte NIP: URI-links en verwijzingen in eventtekst

Een Nostr-identifier heeft een overdraagbare betekenis nodig voordat een andere applicatie deze kan openen. [NIP-21](/nl/topics/nip-21/) plaatst een [NIP-19](/nl/topics/nip-19/)-identifier achter het URI-schema `nostr:`, waardoor browsers, besturingssystemen en applicaties één vorm krijgen die kan worden doorgestuurd. [NIP-27](/nl/topics/nip-27/) definieert wat diezelfde URI betekent binnen leesbare event-`content`. NIP-21 overschrijdt de grens van een applicatie; NIP-27 behoudt een profiel- of eventverwijzing in ondertekende tekst. Geen van beide creëert een event kind of wijzigt relayberichten; de [twee specificaties](https://github.com/nostr-protocol/nips/tree/master) definiëren uitsluitend het gedrag voor links en weergave.

### URI-dispatch en NIP-19-semantiek

[De grammatica van NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) bestaat uit `nostr:`, gevolgd door één NIP-19 bech32-entiteit. `nsec` is uitgesloten omdat het een privésleutel codeert. Er is geen autoriteits-, pad- of querycomponent, dus een conforme link is `nostr:npub1...`, niet `nostr://npub1...`. Een platform of client kan zich als handler registreren. De specificatie kiest niet welke geïnstalleerde applicatie wordt gebruikt en definieert geen webalternatief.

Het voorvoegsel vertelt een client wat die moet decoderen. `npub` bevat een publieke sleutel en `note` een event-id. `nprofile` voegt optionele relayhints toe aan een profiel, `nevent` voegt relays, auteur en kind toe aan een event-id, en `naddr` bevat de auteur, kind en `d`-identifier van een adresseerbaar event, met optionele relays. Deze vormen gebruiken [NIP-19-velden van het type type-length-value](https://github.com/nostr-protocol/nips/blob/master/19.md). Hints verfijnen het zoeken, maar bewijzen niet dat een relay het event bezit of dat de auteur er controle over heeft. Voor elk opgehaald event moeten nog steeds de id opnieuw worden berekend en de handtekening worden gecontroleerd.

De profielvorm in de [NIP-21-specificatie](https://github.com/nostr-protocol/nips/blob/master/21.md) is:

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) definieert ook HTML-bruggen: een pagina die een Nostr-event aanbiedt, kan de bijbehorende `naddr` in `<link rel="alternate">` plaatsen, en een profiel kan een `nprofile` in `<link rel="me">` of `<link rel="author">` plaatsen.

### NIP-27-weergave en optionele tags

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) is van toepassing op leesbare eventinhoud, zoals notities van kind `1` en artikelen van kind `30023`. Een editor kan `@name` weergeven, maar publiceert `nostr:nprofile1...` in de ondertekende tekenreeks. Een reader scant de URI, decodeert de NIP-19-entiteit, haalt het doel op en kan een naam, kaart, voorbeeldweergave of lokale link tonen. Als het decoderen mislukt, blijft de URI gewone tekst. De onbewerkte inhoud mag niet worden herschreven: een wijziging verandert de NIP-01-serialisatie, id en handtekening.

Inhoudsverwijzingen en tags hebben verwante maar verschillende functies. [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) beschrijft optionele `p`- en `e`-tags en de `q`-tag uit [NIP-18](/nl/topics/nip-18/). Een client kan een verwijzing tonen zonder een notificatie of threadrelatie te creëren. Voor het vindbaar maken van citaten moeten zowel de URI als een `q`-tag worden opgenomen. [De implementatie van Zap Cooking van 4 september](https://github.com/zapcooking/frontend/pull/665) volgt die scheiding door de URI te behouden en tegelijk relayhints en een overeenkomende `p`-tag toe te voegen. Het toevoegen van `p` of `q` maakt de URI niet privé, en NIP-27 kent geen modus voor verborgen vermeldingen.

Het volgende [event van kind `1`](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a) is teruggevonden via `wss://nos.lol` en vóór opname geverifieerd als concreet NIP-27-referentievoorbeeld. De `content` bevat een `naddr` voor een versie-onafhankelijk adresseerbaar event. Decodering levert kind `30402`, auteur `91036d...310a`, de `d`-identifier van het werkboek en een hint voor `wss://nos.lol/` op. De tags `q`, `p`, `t`, `zap` en `client` zijn keuzes van de applicatie, geen vereisten van NIP-27.

```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### Vertrouwen, foutgedrag en clientimplementaties

Een veilige reader vindt een volledig `nostr:`-token, valideert bech32, decodeert NIP-19, weigert `nsec`, negeert onbekende TLV-typen en laat misvormde of te lange tekst ongemoeid. `npub` en `nprofile` leiden tot profielquery's; `note` en `nevent` identificeren onveranderlijke events; `naddr` selecteert het nieuwste geldige adresseerbare event voor het betreffende kind, de auteur en de `d`-tag. Relayhints beperken het zoekgebied, maar vormen geen uitbreiding van vertrouwen. Volgens de [eventregels van NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) verifieert de client de id van een opgehaald `nevent` en controleert deze de handtekening van elke `naddr`-kandidaat voordat de vervangingsregels voor adresseerbare events worden toegepast.

Inlinevoorvertoningen zijn een keuze van de client en brengen kosten voor privacy en resources met zich mee. Het ophalen van elke verwijzing onthult de interesses van de lezer en kan een stortvloed aan zoekopdrachten veroorzaken. Clients kunnen daarom een cache gebruiken, het ophalen uitstellen totdat een verwijzing zichtbaar is, het aantal gelijktijdige aanvragen beperken en een klik vereisen voor onbekende media. Volgens [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) moet een voorvertoning duidelijk gescheiden blijven van de ondertekende tekst van de huidige auteur. Een mislukking moet zichtbaar zijn als onopgeloste tekst of als een niet-beschikbare kaart en mag niet stilzwijgend als geverifieerde inhoud worden behandeld.

Vertrouwen verschilt ook per identificatortype. Een `nevent` verwijst naar onveranderlijke bytes, waardoor een client een opgehaald event kan weigeren als de geserialiseerde id afwijkt van de gevraagde id. Een `naddr` verwijst naar een vervangbare coördinaat, waardoor een client elke kandidaat moet verifiëren en de regels voor adresseerbare events moet toepassen voordat wordt bepaald welke versie wordt weergegeven. Een relayhint is in beide gevallen nuttig voor de eerste query, maar vormt geen goedkeuring van de relay of van de teruggegeven inhoud. [De TLV-definitie van NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md) levert de gegevens die nodig zijn om deze controles expliciet uit te voeren.

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) definieert een overdraagbare link die van buiten Nostr kan worden geopend, terwijl NIP-27 dezelfde link duurzaam maakt binnen ondertekende tekst. Een client die alleen NIP-21 implementeert, kan een geplakte URI openen, maar geen ingesloten verwijzingen weergeven. Volledige ondersteuning voor NIP-27 voegt scannen, veilig decoderen, ophaalbeleid, lokale weergave en een expliciete keuze voor notificatie- en citaattags toe. De gedeelde URI houdt deze lagen interoperabel zonder clients te dwingen ze op dezelfde manier te presenteren.[Damus](https://github.com/damus-io/damus) modelleert inlineverwijzingen als getypeerde vermeldingen. De [vermeldingscode](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift) wijst `npub` en `nprofile` toe aan profielverwijzingen, `note` en `nevent` aan eventverwijzingen en `naddr` aan adresverwijzingen; [NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift) leidt ze naar de juiste bestemming. [Primal Android](https://github.com/PrimalHQ/primal-android-app) [parseert de scheme- en geplakte vormen](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt), valideert bech32 en extraheert relayhints, en [zet verwijzingen vervolgens om in modellen voor note-inhoud](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt). [Zap Cooking](https://github.com/zapcooking/frontend/pull/665) geeft dezelfde verwijzingen weer in artikelen, recepten, editorvoorvertoningen en afdrukweergaven.

---

Stuur een NIP-17-DM om een project of nieuwsitem te delen via het [Nostr Compass-project](https://github.com/andotherstuff/nostr-compass).
