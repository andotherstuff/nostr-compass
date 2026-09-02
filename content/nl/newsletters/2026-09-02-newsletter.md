---
title: "Nostr Compass #38"
date: 2026-09-02
publishDate: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
description: "Voca 1.0 brengt geverifieerd lezen via Nostr naar een offline tekst-naar-spraakapp, nostream breidt jobroutering en authenticatie aan de relaykant uit, Napstr publiceert audiocatalogi via Tor, MDK 0.9.17 verlaagt de kosten van groepsonderhoud, de kern-NIPs voegen een pagineringstip en highlight-tags samen naast NWC-transactietotalen, en de NIP Deep Dive legt reposts en reacties uit."
---

Welkom terug bij [Nostr Compass](https://nostrcompass.org), jullie wekelijkse gids voor Nostr.

**Deze week:** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 brengt geverifieerde Nostr-notes en longform-subscriptions naar een offline Android-reader die artikelen voorleest, [nostream](https://github.com/cameri/nostream) breidt jobroutering en geauthenticeerde werking aan de relaykant uit, [NDK for Dart](https://github.com/relaystr/ndk) repareert negentropy en de levensduur van requests over meerdere relays, [Divine Mobile](https://github.com/divinevideo/divine-mobile) maakt het verwijderen en ondertekenen van verpakte berichten deterministisch, [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) beschermt gift-wrap-inboxen standaard, [Amethyst](https://github.com/vitorpamplona/amethyst) levert portabele highlights, en [Mostro](https://github.com/MostroP2P/mostro) verifieert ondertekende orders vóór zijn spamfilter. [Napstr](https://github.com/lnbits/napstr) publiceert audiocatalogi en seeder-heartbeats over Nostr terwijl bestanden via Tor worden overgedragen. Releases omvatten [MDK](https://github.com/marmot-protocol/mdk) en [pakstr](https://git.nostrdev.com/stuff/pakstr); protocolwerk voegt een pagineringstip van [NIP-67](/nl/topics/nip-67/) en een tag-schema voor highlights van [NIP-84](/nl/topics/nip-84/) samen in de [NIPs-repository](https://github.com/nostr-protocol/nips), terwijl [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) transactietotalen toevoegt; en de NIP Deep Dive volgt reposts en reacties door hun eventvormen en huidige implementaties.

## Topverhalen

### Voca 1.0 leest geverifieerde Nostr-notes en subscriptions voor op Android

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) is een offline Android-reader die artikelen, PDF's, Markdown-bestanden en Nostr-notes voorleest met de eigen tekst-naar-spraakstem van de telefoon, terwijl de uitgesproken zin op de pagina verlicht blijft. De [1.0-release](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en), [op 2026-08-27 gepubliceerd](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) onder een eigen [projectsleutel](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu), maakt Nostr tot een volwaardige bron: plak een note-adres, een event-id, een npub, een profiel of een gewone weblink met daarin een Nostr-entiteit, en de app decodeert de verwijzing, haalt het ondertekende event bij relays op en leest de tekst van de auteur in plaats van de webpagina die eromheen is gebouwd.

Twee geverifieerde gedragingen definiëren de Nostr-integratie, beide beschreven in [Voca's ondertekende aankondiging van 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en). Ten eerste wordt elk opgehaald event vóór opslag gecontroleerd aan de hand van zijn opnieuw berekende id en zijn BIP-340 Schnorr-signature, met behulp van de bootstrap-relays, de [NIP-65](/nl/topics/nip-65/)-relaylijst van de auteur (een ondertekend, vervangbaar kind `10002`-event waarin een auteur de relays opsomt waar die leest en schrijft) en hints in de verwijzing zelf. Een relay kan dus weigeren te antwoorden, maar kan een auteur geen woorden in de mond leggen. Ten tweede plaatst het toevoegen van de npub van een auteur diens longform-artikelen van [NIP-23](/nl/topics/nip-23/) (adresseerbare kind `30023`-berichten met titels, samenvattingen en afbeeldingen) in één inbox op het apparaat naast RSS- en Atom-feeds. De 1.1.0-update, [aangekondigd op 2026-08-28](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca) en op 2026-08-29 gepubliceerd in [Zapstore](https://zapstore.dev), stemt scrollen per zin af op de timing, maakt lange documenten vloeiender en herstelt de widget op het startscherm na handmatig scrollen, formaatwijzigingen, herstarts van het proces en upgrades.


### nostream breidt DVM-routering en geauthenticeerde werking aan de relaykant uit

Na [het werk aan job-inname van 19 augustus](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes) [slaat nostream](https://github.com/cameri/nostream), een TypeScript-relayimplementatie, [NIP-89-events voor application handlers op en serveert die](https://github.com/cameri/nostream/pull/737). [NIP-89](/nl/topics/nip-89/) (ontdekking van application handlers) gebruikt kind `31989`-aanbevelingen en kind `31990`-informatie over handlers, die beide al binnen het bereik van geparametriseerd vervangbare events vallen. Een client kan die kinds dus opvragen en een vervanging ontvangen wanneer een `d`-tag botst. De relay publiceert geen handlerinformatie voor zijn eigen workers.

Openstaande jobs van [NIP-90](/nl/topics/nip-90/) (data vending machine) [bereiken nu een workerproces en keren terug als resultaat-events](https://github.com/cameri/nostream/pull/734). Bij succes ondertekent de relay een kind 6000-6999-resultaat met zijn eigen sleutel. Een timeout of crash van de worker markeert de job als mislukt in plaats van hem ingediend te laten staan.

Geauthenticeerde sessies en HTTP-aanroepen voor beheer vallen onder verschillende grenzen. [NIP-42](/nl/topics/nip-42/) (clientauthenticatie bij relays) [houdt de geauthenticeerde pubkey per socket bij](https://github.com/cameri/nostream/pull/716), kan AUTH vereisen voordat clients events publiceren en vermeldt die vereiste in het [NIP-11](/nl/topics/nip-11/)-document (relayinformatie), waarbij beide instellingen standaard uitstaan. Afzonderlijk daarvan [kunnen routes van de admin-API ondertekende HTTP-autorisatie van NIP-98 accepteren](https://github.com/cameri/nostream/pull/730). [NIP-98](/nl/topics/nip-98/) (HTTP-authenticatie met ondertekende events) blijft uit totdat een operator dit inschakelt en de toegestane pubkeys opgeeft.

### NDK for Dart repareert negentropy, levensduur van requests over meerdere relays en signatureverificatie

Een uitvoering van [NIP-77](/nl/topics/nip-77/) (negentropy-setafstemming) in [NDK](https://github.com/relaystr/ndk), een Dart-developmentkit voor Nostr, gaf zonder foutmelding de verkeerde have- en need-sets terug, omdat de codec versie 1 van het [negentropy](/nl/topics/negentropy/)-protocol niet sprak. De [reparatie van de v1-encoding](https://github.com/relaystr/ndk/pull/722) geeft nu de ids terug die de relay bezit en de ids die hij nog nodig heeft.

Identieke filters die naar verschillende relays werden gestuurd [vielen samen tot één request](https://github.com/relaystr/ndk/pull/705). Requests met hetzelfde filter blijven nu gescheiden wanneer ze op verschillende relays zijn gericht of een andere levensduur hebben, zodat een korte query geen events van een andere relay in het resultaat kan mengen en een actieve subscription niet kan laten vastlopen.

Dezelfde kit [verifieert een signature één keer en bewaart dat resultaat](https://github.com/relaystr/ndk/pull/726). Een latere dubbele bezorging kost niet opnieuw een controle en overschrijft het opgeslagen geverifieerde event niet meer.

### Divine Mobile maakt verwijderen en ondertekenen van verpakte direct messages deterministisch

Verpakte kind `5`-events van [NIP-09](/nl/topics/nip-09/) (verzoek om een event te verwijderen) die op een bericht waren gericht, werden in [Divine Mobile](https://github.com/divinevideo/divine-mobile), een mobiele client voor korte video's die via Nostr publiceert, nooit toegepast. De client [toetst nu elke verwijdering aan het genoemde bericht](https://github.com/divinevideo/divine-mobile/pull/8174), in plaats van alles wat geen reactie is als al verwerkt te behandelen. Een tweede [verzoek om voor iedereen te verwijderen terwijl het eerste nog liep](https://github.com/divinevideo/divine-mobile/pull/8164) verdween vroeger zonder foutmelding en zonder kind `5` op de wire; gelijktijdige verwijderingen worden nu elk gepubliceerd.

Na de eerder behandelde 1.0.22-release leverde het tweemaal binnen één seconde verzenden van dezelfde 1:1-tekst via [NIP-17](/nl/topics/nip-17/) (gift-wrapped privé-DM's) [één rumor-id op](https://github.com/divinevideo/divine-mobile/pull/8163), waardoor de tweede verzending verdween. Elke verzending draagt nu een token in de [NIP-59](/nl/topics/nip-59/)-rumor (gift wrap), zodat de ids verschillen.

Een aanroeper die een kind `4`- of kind `5`-event al had ondertekend, [behield die signature](https://github.com/divinevideo/divine-mobile/pull/8173), in plaats van dat achteraf een client-tag werd toegevoegd die de id veranderde en relays het event als ongeldig liet weigeren.

### Conduit Relay verstevigt zijn door NIP-42 beschermde inbox

Kind `1059` gift wraps worden voor één ontvanger opgeslagen. [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), een Go-relay die zulke wraps in een door de ontvanger beschermde inbox bewaart, [gebruikt standaard enforce-modus](https://github.com/Conduit-BTC/conduit-relay/pull/8): een query naar kind `1059` moet [NIP-42](/nl/topics/nip-42/)-authenticatie als die ontvanger tonen, anders weigert de relay het request. Filters met gemengde kinds, wildcards, tellingen en [negentropy](/nl/topics/negentropy/) over die wraps zijn `restricted`, zodat een andere AUTH ze niet kan veranderen in een dump van andermans inbox.

Dezelfde [merge voor de beschermde inbox](https://github.com/Conduit-BTC/conduit-relay/pull/8) vereist een canonieke event-id in het verzonden AUTH-event en accepteert een verder geldig NIP-42-event ongeacht of `content` leeg is. Challenge-only biedt nog steeds AUTH aan zonder de leesopdracht te blokkeren; disabled laat alles vrij toe. De standaardinstelling van de library is enforce.

### Amethyst levert NIP-84-highlights en repareert twee foutpaden richting relays

Na het [werk van vorige week aan Blossom-autorisatie](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads) levert [Amethyst](https://github.com/vitorpamplona/amethyst), een Android-Nostr-client, [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) met [NIP-84](/nl/topics/nip-84/) (portabele highlights). Een geselecteerde passage wordt een kind `9802`-event vanuit de composer, een feed met highlights of een deelactie naar de app.

De release voegt verwijderings- en archiveringsbediening voor kanalen van [NIP-29](/nl/topics/nip-29/) toe ([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)) en meet relaygedrag via het verkeer dat de client al maakt. Vervolgens worden die probes van [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) uitgebreid met controles voor streaming, lezen, schrijven en URL's ([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). Amethyst verwijdert ook een hash-collision-kwetsbaarheid in SharedKeyCache en vergelijkt message-authentication codes in constante tijd ([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), repareert een race waardoor de bezorging van AUTH tijdens het verbinden verloren kon gaan ([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), verdeelt de vergrendeling van subscription-state om een ANR-konvooi te beëindigen ([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)) en vergelijkt elk subscription-filter in plaats van alleen het eerste ([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)).

[Newsletter #36 behandelde deze wijzigingen aan relayauthenticatie, back-ups en publieke chats al](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow); v1.14.0 heeft ze nu samen uitgebracht. Zachte bans in Concord dichten door een audit gevonden gaten in de autoriteit ([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). Relayauthenticatie heeft een opnieuw ontworpen toestemmingsflow ([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), wacht op de afhandeling van challenges in plaats van een timeout ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), laat nieuwe accounts standaard authenticeren ([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), respecteert die voorkeur op relays buiten de normale set van het account ([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)) en behoudt sessietoestemmingen na opnieuw verbinden ([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). Een begeleide eerste start en flow in Settings maken sleutelback-ups vindbaar ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)), het aanvullen van Cashu-proofs en pagineren door de geschiedenis voorkomen dat walletsaldos worden afgekapt ([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)), en publieke chats kunnen nu worden gedempt ([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)).

Na die tag worden [vertrouwde lijsten](https://github.com/vitorpamplona/amethyst/pull/3983) in kinds `30392` tot en met `30395` volgens [NIP-50](/nl/topics/nip-50/) (zoeken in volledige tekst) alleen op titel geïndexeerd, zodat een lijst die in proza wordt genoemd vindbaar is zonder hex-ids van leden te indexeren. Weigeringen van wallets die via [NIP-47](/nl/topics/nip-47/) (Nostr Wallet Connect) binnenkwamen, [tonen nu hun foutmelding in plaats van eruit te zien als een tik die niets deed](https://github.com/vitorpamplona/amethyst/pull/3987), waaronder `QUOTA_EXCEEDED` en `RESTRICTED`, plus een timeout wanneer de wallet nooit antwoordt.

### Mostro valideert ondertekende orders vóór kostbaar werk en bewaart audit-events van orders

Na [de basis voor Cashu-escrow in v0.18.1](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon) heeft [Mostro](https://github.com/MostroP2P/mostro), een peer-to-peer-exchangedaemon die orders over Nostr coördineert, [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5) getagd. Die versie gebruikt standaard [NIP-44](/nl/topics/nip-44/) (payloadversleuteling) als transport en houdt gift wrap als expliciete opt-in.

De release verankert timeouts in de wachtstatus aan de geregistreerde take-tijd, zodat een maker-bond niet volgens de verkeerde klok wordt geslashed ([PR #879](https://github.com/MostroP2P/mostro/pull/879)), verstuurt elke uitbetaling aan de koper van een afgeronde order hoogstens eenmaal ([PR #881](https://github.com/MostroP2P/mostro/pull/881)) en laat die uitbetalingen verlopen via begrensde, niet-blokkerende `send_payment`-wachttijden ([PR #883](https://github.com/MostroP2P/mostro/pull/883)). Een poging om de winnaar van een timeout-slash te betalen ([PR #875](https://github.com/MostroP2P/mostro/pull/875)) werd teruggedraaid voordat dezelfde tag uitkwam ([PR #885](https://github.com/MostroP2P/mostro/pull/885)). Mostro stopt ook met het elk uur en bij het opstarten opnieuw publiceren van een ongewijzigd orderboek met openstaande orders ([PR #888](https://github.com/MostroP2P/mostro/pull/888)), en zijn kind `38386`-events voor geschillen dragen nu een `created_at`-tag voor downstream-sortering ([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

Na die tag [wordt nu vóór het spamfilter een signaturecontrole uitgevoerd](https://github.com/MostroP2P/mostro/pull/892). Een event-id legt `sig` niet vast, zodat een kopie van de kind `14` van een slachtoffer met een kapotte signature de replay-positie kon bezetten en het geldige bericht geruisloos kon laten vallen. De daemon verifieert nu eerst en laat een ongeldige wrap vallen in plaats van te waarschuwen en door te gaan.

Fee-audit-events van kind `8383` droegen een [NIP-40](/nl/topics/nip-40/)-vervaltijd van 15 dagen. Ze [behouden nu een vervaltijd van één jaar](https://github.com/MostroP2P/mostro/pull/924), passend bij hun rol als publiek betalingsbewijs. Op een node waarop Cashu is ingeschakeld, [vraagt het aannemen van een order de verkoper via Nostr een 2-of-3-escrow te vergrendelen](https://github.com/MostroP2P/mostro/pull/830), publiceert het het wachtende order-event en slaat het de aanmaak van een Lightning hold invoice over. Daarmee is het requestpad voltooid; dat sluit op zichzelf niet elke escrow- of misbruikzaak op de marktplaats af.

### Napstr publiceert audiocatalogi op Nostr en draagt bestanden over via Tor

[Napstr](https://github.com/lnbits/napstr) is een desktopclient voor het delen van audio die doorzoekbare catalogi en actieve seeders op Nostr publiceert en de bestanden vervolgens overdraagt via een meegeleverd Tor-proces zonder fallback naar een direct IP-adres. [Versie 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) houdt profielen en catalogusmetadata publiek, en houdt requests, overdrachtsgegevens, bestandsinhoud en IP-adressen van peers buiten de relays.

Ontdekking gebruikt twee adresseerbare eventkinds uit de [Napstr-repository](https://github.com/lnbits/napstr). Kind `30421`-catalogusitems benoemen een bestand aan de hand van de SHA-256-digest, publieke basisnaam, grootte en audio-indeling. Een auteur trekt een bestand in door die coördinaat te vervangen door een verwijderd-markering. Kind `30422`-heartbeats voor beschikbaarheid verlopen na tien minuten en vermelden de bestands-ids die de auteur wil seeden. Een catalogusregel is dus alleen actief zolang een niet-verlopen heartbeat die digest nog bevat.

Publieke gesprekken gebruiken [NIP-C7](/nl/topics/nip-c7/) (kind 9-chatberichten) in plaats van een groep die eigendom is van een relay. De [Napstr-repository](https://github.com/lnbits/napstr) definieert een gedeelde publieke ruimte plus een gesprek per track dat aan de bestandsdigest is gekoppeld. Die berichten zijn ondertekend en publiek. Ze bevatten geen onion-adressen, overdrachtsgegevens of bestandsbytes.

Een download begint als onderhandeling via [NIP-17](/nl/topics/nip-17/) (gift-wrapped privé-DM's). De [Napstr-repository](https://github.com/lnbits/napstr) verpakt een request, aanbod of weigering in een kind `14`-rumor, zodat relays de tijdelijke v3-onion-hostnaam of de eenmalige capability die een geaccepteerd aanbod teruggeeft niet zien. De meegeleverde Tor verplaatst de bytes vervolgens via die onion, verifieert de volledige SHA-256-digest en valideert de audio opnieuw voordat het bestand afspeelbaar wordt.

De [vergelijking van v0.1.7 met v0.2.0](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) voegt audioboekcollecties en Napstrfy toe, een optionele Android-companion. Kind `30423`-manifests vermelden geordende hoofdstukken die gewone catalogusbestanden blijven, zodat een client die de collectie negeert elk hoofdstuk nog steeds kan ophalen. Napstr maakt daarvoor een niet-destructieve lokale map Audiobooks. Napstrfy koppelt via een eenmalige QR-code met een actieve desktop en zoekt en vraagt downloads vervolgens aan via de bestaande Nostr- en Tor-services van die desktop, zonder de geheime sleutel van de desktop te ontvangen.

Dezelfde [vergelijking](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) laat een companion-handshake die niet wordt voltooid verlopen. Een seeder kopieert en hasht het gedeelde bestand voordat bytes worden geserveerd, schrijft binnenkomende gegevens naar een privé-tijdelijk bestand, beperkt bestemmingen van audioboeken tot een werkelijk onderliggend pad in de Napstr-map en breekt af als die bestemming tijdens de overdracht verandert.

## Releases

### MDK v0.9.17: nieuwste KeyPackages, lidmaatschapsactiviteit en duurzame verzendingen

[Newsletter #37 behandelde MDK 0.9.14 en 0.9.15](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles), waaronder de wijziging in de [MDK-repository](https://github.com/marmot-protocol/mdk) van selectie van het oudste KeyPackage naar het nieuwste geldige pakket voor het huidige profiel, de herstelgates voor epoch-gaps, het opschonen van accounts en de scheiding tussen discovery- en operationele relays. Die reparaties blijven de basis voor de twee daaropvolgende releases, zodat een verouderd pakket niet langer een lid blokkeert dat al een bruikbaar pakket heeft gepubliceerd.

[Events voor lidmaatschap en beheer schuiven de chatlijst nu op](https://github.com/marmot-protocol/mdk/pull/1551), net zoals een nieuw bericht: previewtekst, volgorde, aantallen ongelezen berichten en leesmarkeringen worden bijgewerkt wanneer mensen toetreden, vertrekken of van rol veranderen, en de lokale systeemactor wordt niet als Nostr-profiel behandeld. Nieuwe verbindingen en herstarts [hergebruiken één verzendidentiteit voor duurzame uitgaande tekst die opnieuw wordt geprobeerd](https://github.com/marmot-protocol/mdk/pull/1516), zodat hetzelfde groepsbericht niet tweemaal wordt gepubliceerd.

De twee releases sindsdien richten zich op de kosten om grote groepen gezond te houden. [Versie 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [meet epoch-afwijking vanaf de huidige epoch in plaats van een hoogwatermerk](https://github.com/marmot-protocol/mdk/pull/1559), houdt geweigerde inkomende events opvraagbaar ([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), beperkt rollback van replay tot canonieke groepstoestand ([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)) en introduceert [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545), een met macro's gegenereerde C ABI bovenop de UniFFI-bindings waarmee hosts de engine rechtstreeks kunnen inbedden. [Versie 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) vouwt pass-admission-scans vervolgens samen tot [één ronde langs de leden in plaats van één ronde per lid](https://github.com/marmot-protocol/mdk/pull/1617), [controleert of een groepstoestand wordt betwist zonder de volledige geschiedenisgraaf op te bouwen](https://github.com/marmot-protocol/mdk/pull/1620), [verlaagt de kosten van idle-polling voor de deferred-peel-sweep](https://github.com/marmot-protocol/mdk/pull/1621) en [past de gebatchte component-read toe op de drie projectieplekken die de eerste ronde miste](https://github.com/marmot-protocol/mdk/pull/1622). De bijbehorende artefacten [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) en [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) zijn uit dezelfde commit gebouwd, zodat ontwikkelaars die de engine inbedden de goedkopere onderhoudspaden samen krijgen.


### pakstr v0.16.0: kind-32267-identificatoren bij publicatie

Na [de Zapstore-publicatiepipeline van vorige week, van 0.13.0 tot en met 0.15.0](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit) [logt pakstr](https://git.nostrdev.com/stuff/pakstr), een CLI die een webapp verpakt in een ondertekende Android-APK en die met een Nostr-sleutel publiceert, [de ids van kind `32267`-applicatie-events](https://git.nostrdev.com/stuff/pakstr/pulls/67) die het opzoekt, publiceert of vervangt. [Versie 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) drukt zowel de vorige als de nieuwe id af wanneer verouderde listingmetadata een herpublicatie veroorzaakt, zodat een uitgever kan bevestigen welk listing-event op de relay actief is.

Dezelfde [identifier-log](https://git.nostrdev.com/stuff/pakstr/pulls/67) registreert vóór elke vervanging de id die tijdens het opzoeken is gevonden en daarna de id van het event dat is aangekomen, zodat een no-op-hergebruik als herhaalde id verschijnt. Dat is de getagde wijziging in [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0); het gedrag rond Content-Digest, publiceren vóór uploaden en validatie van de uitgever was al in eerdere tags uitgebracht.

## Niet-uitgebrachte wijzigingen

### Zap Cooking beperkt bunker-relays en ondertekent betaalde endpoints

Bij het opnieuw laden van een bunkersessie in [Zap Cooking](https://github.com/zapcooking/frontend), een receptensite die is gebouwd op longform-events van Nostr, werd het versleutelde [NIP-46](/nl/topics/nip-46/)-gesprek (remote signing over relays) vroeger gepubliceerd naar elke relay die de pagina al gebruikte. [Signer-verkeer beperken tot de eigen relays van de bunker](https://github.com/zapcooking/frontend/pull/633) past die beperking nu toe bij sessieherstel en bij nostrconnect-koppeling, de door de signer gestarte verbindingsflow, net als bij inloggen via een bunker-URL. Een lege relayset uit een misvormd opgeslagen record wordt niet geïnstalleerd, zodat relays die alleen recepten hosten niet langer vernemen dat dezelfde pubkey een actieve bunkersessie onderhoudt.

[Ondertekende HTTP-authenticatie](https://github.com/zapcooking/frontend/pull/630) bewaakt nu de betaalde chat met kookassistent, de inleiding van het kookboek en updates van afgeschermde recepten via [NIP-98](/nl/topics/nip-98/) (HTTP-authenticatie met een ondertekend Nostr-event). De server leest de requestbody eenmaal, verifieert de signature tegen precies die payload en ontleent de identiteit aan het geverifieerde auth-event in plaats van aan een publieke sleutel in de body. De preview van de chat werkt nog steeds zonder header, terwijl een aanwezige maar ongeldige signature wordt geweigerd en de inleiding van het kookboek altijd een signature vereist. Het bijwerken van een afgeschermd recept vereist nu ook dat de geverifieerde sleutel overeenkomt met de opgeslagen auteur. Ieder ander krijgt te horen dat het recept niet bestaat, zodat het endpoint niet bevestigt welke betaalde records bestaan.

### nostrord repareert verpakte DM's en gedeelde eventlinks

Na [v2.9.0 van vorige week](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media) heeft [nostrord](https://github.com/nostrord/nostrord), een crossplatformclient voor door relays gehoste communities, bezorgingsreparaties samengevoegd zodat een [NIP-17](/nl/topics/nip-17/)-bericht (gift-wrapped privé-DM) dat vanaf één apparaat wordt verzonden hetzelfde account elders bereikt. [De eigen kopie van de afzender onafhankelijk publiceren](https://github.com/nostrord/nostrord/pull/295) voorkomt dat de eerste acceptatie van de wrap voor de ontvanger door een relay de kopie laat vallen die andere apparaten ophalen. Dezelfde wijziging verzendt een wrap opnieuw nadat [NIP-42](/nl/topics/nip-42/) (clientauthenticatie bij relays) is voltooid, en markeert de verzending als geslaagd bij de eerste acceptatie door een relay, zodat één falende host de rest niet kan ophouden. [Geparkeerde gift wraps opnieuw proberen](https://github.com/nostrord/nostrord/pull/297) nadat ontsleuteling volgens [NIP-59](/nl/topics/nip-59/) (gift wrap) is mislukt, gebeurt nu op een timer, zodat een bunker die verbonden blijft die berichten niet langer mi... [afgekapt]

Een antwoord volgens [NIP-C7](/nl/topics/nip-c7/) (kind `9`-chatberichten) herhaalt zijn parent als vooraanstaande [NIP-19](/nl/topics/nip-19/)-pointer (bech32-gecodeerde entiteiten) van het type `nevent` naast de `q`-tag. [Die vooraanstaande pointer naar de parent weglaten](https://github.com/nostrord/nostrord/pull/292) wanneer de body wordt geopend en de parent van het antwoord wordt benoemd, laat de regel als één geciteerd antwoord renderen, terwijl een pointer midden in de body of een pointer die de hele body vormt nog steeds als quote-card wordt weergegeven. [Links naar geciteerde events coderen nu `nevent`](https://github.com/nostrord/nostrord/pull/293) met de auteur, kind en de relay waarvan het citaat is gelezen, zodat een event van [NIP-29](/nl/topics/nip-29/) (door relays beheerde groepen) dat in een DM wordt gedeeld door een andere client kan worden opgehaald, in plaats van een kale note-id zonder hints voor het opzoeken.

## NIP-updates en werk aan protocolspecificaties

### Mogelijkheden voor Nostr-implementaties

Deze week zijn twee specificatiewijzigingen samengevoegd in de kern-[NIPs-repository](https://github.com/nostr-protocol/nips).

[NIP-67](/nl/topics/nip-67/) definieert hints die een relay aan een `EOSE`-bericht (einde van opgeslagen events) kan toevoegen, zodat een client weet of die moet blijven pagineren. De [samengevoegde hint `"auth"`](https://github.com/nostr-protocol/nips/pull/2371) voegt naast `finish` en `more` een derde waarde toe: een relay kan nu aangeven dat aanvullende opgeslagen events zichtbaar kunnen worden wanneer de gebruiker zich authenticeert, en moet de `AUTH`-challenge van [NIP-42](/nl/topics/nip-42/) (relayauthenticatie) verzenden vóór de `EOSE` die de hint bevat. De [bijbehorende toevoeging aan NIP-42](https://github.com/nostr-protocol/nips/pull/2371) definieert dezelfde flow vanaf de clientkant, zodat een client die een `EOSE` met `auth` ontvangt de benodigde challenge al bezit om te antwoorden.

[NIP-84](/nl/topics/nip-84/) (portabele highlights, de kind `9802`-events waarvoor Amethyst hierboven ondersteuning uitbracht) [voegde een bijgewerkt tag-schema samen](https://github.com/nostr-protocol/nips/pull/2454): highlights mogen hun bron nu taggen met gestructureerde `i`-tags volgens [NIP-73](/nl/topics/nip-73/) (identificatoren voor externe content), naast `a`/`e`-tags voor Nostr-events en `r`-tags voor al het overige. Bij het renderen als quote-repost zijn geciteerde highlights bovendien van MUST naar SHOULD gegaan.

### Nostr Wallet Connect

Een `list_transactions`-response kan melden hoeveel transacties overeenkomen met het request, niet hoeveel rijen de huidige pagina teruggaf. De [samengevoegde optionele `total_count`](https://github.com/nostr-wallet-connect/nwc/pull/4) in NWC-05 (de extensie voor walletgeschiedenis) in de [NWC-extensierepository](https://github.com/nostr-wallet-connect/nwc) voegt dat veld toe aan de response die wordt gebruikt met [NIP-47](/nl/topics/nip-47/) (versleutelde remote walletbesturing over Nostr).

De [commit die `total_count` toevoegt](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) documenteert het als een optioneel geheel getal: het totale aantal transacties dat overeenkomt met de requestfilters.

De [commit die paginering van de telling uitsluit](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) stelt dat dit totaal paginering uitsluit en dus alle overeenkomende transacties over alle pagina's telt.

## NIP Deep Dive: Reposts en reacties

Een contact kan een bestaande note opnieuw onder de aandacht van zijn volgers brengen en kan een compacte like, dislike of emoji toevoegen zonder een antwoord te schrijven. [NIP-18](/nl/topics/nip-18/) (reposts) publiceert die herverdeling als een eigen ondertekend event. [NIP-25](/nl/topics/nip-25/) (reacties) publiceert de compacte respons als afzonderlijk ondertekend event. Beide blijven `draft` `optional`-bestanden in de [canonieke specificatie voor reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) en de [canonieke specificatie voor reacties](https://github.com/nostr-protocol/nips/blob/master/25.md): ze staan in de NIPs-repository en worden door clients geïmplementeerd, maar zijn nog steeds als niet-definitief gelabeld.

### Reposts (NIP-18)

Volgers ontvangen een ondertekende pointer naar een kind 1-tekstnote die iemand al heeft gepubliceerd wanneer een client een kind 6-event schrijft. [De specificatie voor reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) stelt `kind` in op 6, plaatst de als string weergegeven JSON van die note in `content` (lege `content` is toegestaan en wordt niet aanbevolen), vereist een `e`-tag waarvan de waarde de `id` van de note is en waarvan het derde item een relay-URL is waar de note kan worden opgehaald, en zegt dat het event ook een `p`-tag met de `pubkey` van de oorspronkelijke auteur SHOULD bevatten. Een repost van een event volgens [NIP-70](/nl/topics/nip-70/) (beschermde events) SHOULD `content` leeg houden, zodat de beschermde payload niet naar het nieuwe event wordt gekopieerd.

Een citaat is een verwijzing in een ander event, geen kind 6-wrapper. Wanneer een client een `nevent`, `note` of `naddr` van [NIP-21](/nl/topics/nip-21/) (`nostr:`-URI) vermeldt, moet die client de vermelding omzetten in een `q`-tag met de vorm `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`. [Tags voor quote-reposts](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) houden die verwijzingen buiten antwoordthreads en laten clients de citaten van een bericht ophalen en tellen.

Kind 6 is gereserveerd voor kind 1-notes. Een algemene repost van kind 16 kan elk eventkind behalve kind 1 verpakken. Die SHOULD een `k`-tag bevatten waarvan de waarde de als string weergegeven kind van het binnenste event is. Wanneer dat binnenste event vervangbaar is, SHOULD de algemene repost een `a`-tag toevoegen met de coördinaat `kind:pubkey:d-tag`. Als die `a`-tag ontbreekt, richt de repost zich op één specifieke versie en moet `content` de volledige JSON-string van die versie bevatten. [De regels voor algemene reposts](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) voorkomen dat longform-, adresseerbare en andere events die geen note zijn worden gepubliceerd alsof ze kind 1 waren.

Het volgende kind 6-event is een live repost die tijdens het samenstellen is opgehaald van `wss://relay.damus.io` ([open het event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)):

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

De `kind` is 6, de `e`-tag wijst naar de gereposte note, de `p`-tag identificeert de auteur van die note en `content` bevat het oorspronkelijke kind 1-event als JSON-string. Dit bij een relay opgehaalde event laat de relayhint weg die de [NIP-18-specificatie](https://github.com/nostr-protocol/nips/blob/master/18.md) als vereist markeert. Dat illustreert waarom readers en clients echte events moeten valideren en rekening moeten houden met producenten die velden weglaten.

### Reacties (NIP-25)

Een bericht kan ondertekende likes, dislikes en emoji verzamelen zonder dat die markeringen in de antwoordthread terechtkomen. [De specificatie voor reacties](https://github.com/nostr-protocol/nips/blob/master/25.md) definieert zo'n markering als een kind 7-event waarvan `content` de reactiewaarde MUST bevatten. `+` of een lege string MUST als like of upvote worden gelezen. `-` MUST als dislike of downvote worden gelezen. Een emoji of shortcode voor aangepaste emoji volgens [NIP-30](/nl/topics/nip-30/) SHOULD NOT als like of dislike worden gelezen, en een client MAY die emoji op het bericht tonen.

Het doel staat in de tags en wordt niet uit `content` afgeleid. Er MUST een `e`-tag zijn die op de `id` van het doel-event is ingesteld, en die tag SHOULD een relayhint bevatten. Extra `e`-tags worden niet aanbevolen; als ze voorkomen, moet de doel-`id` als laatste staan. Er SHOULD een `p`-tag voor de doelauteur zijn, als laatste wanneer meerdere `p`-tags voorkomen. Een adresseerbaar doel SHOULD ook een `a`-tag met `kind:pubkey:d-tag`-coördinaten krijgen. De `e`- en `a`-tags SHOULD relay- en pubkey-hints bevatten, de `p`-tags SHOULD relayhints bevatten, en een `k`-tag MAY de als string weergegeven kind van het event waarop is gereageerd dragen. [Die tagregels](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) laten een client het doel ophalen en de auteur ervan op basis van alleen het reactie-event op de hoogte stellen.

Een client MAY één `:shortcode:` in `content` plaatsen en één `emoji`-tag die die shortcode aan een afbeeldings-URL koppelt, volgens de [reactieregels voor aangepaste emoji](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction). Als het doel geen native Nostr-event is, MUST de reactie kind 17 zijn en MUST die volgens [NIP-73](/nl/topics/nip-73/) (ids van externe content) `k`- en `i`-tags bevatten, zoals in de [reactieregels voor externe content](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions). Kind 17 is een reactie op een website, podcastaflevering of ander extern object. Het is geen kind 7-reactie van event op event en geen repost.

Het volgende kind 7-event is een live reactie die tijdens het samenstellen is opgehaald van `wss://relay.damus.io` ([open het event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)):

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

De `content` is `+`, de conventionele like van [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). De `e`-tag noemt het event waarop is gereageerd; de `a`-tag voegt de adresseerbare coördinaat ervan toe; de `p`-tag identificeert de auteur; en de optionele `k`-tag legt de kind van het doel als string vast.

### Huidige clientimplementaties

[Amethyst](https://github.com/vitorpamplona/amethyst), een Android-Nostr-client, definieert het [eventtype voor reposts](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) en het [eventtype voor reacties](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) in zijn huidige protocollaag.

[Snort](https://github.com/v0l/snort), een Nostr-webclient, implementeert [helpers voor NIP-18 die afhandeling van tags voor quote-links omvatten](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) en [maakt tags voor NIP-25-eventreacties](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

[Ditto](https://github.com/soapbox-pub/ditto), een gecombineerde Mastodon-server en Nostr-relay, [publiceert algemene kind 16-reposts met een `k`-tag en een `a`-coördinaat op adresseerbare doelen](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) en [past de semantiek van kind 7-reacties toe door de laatste `e`-tag als doel-event te behandelen](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### Hoe ze samenwerken

Een kind 6- of kind 16-event herverdeelt een bestaand event naar de feeds van de volgers van de reposter, door de JSON van dat event in te bedden of naar een vervangbare coördinaat te wijzen. Een `q`-tag markeert een citaat binnen een ander event, zodat de reconstructie van threads verwijzingen kan tellen zonder het citerende event als antwoord te behandelen. Dat is de scheiding uit het [gedeelte over quote-reposts](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). Een kind 7-event laat het oorspronkelijke event op zijn plaats en voegt alleen de reactiewaarde plus doeltags toe, volgens het contract in de [specificatie voor reacties](https://github.com/nostr-protocol/nips/blob/master/25.md). Clients die één pubkey ophalen, zien de reposts van die pubkey daarom als nieuwe kind 6- of 16-events en de meningen van die pubkey als kind 7-events op berichten van anderen.

---

Stuur een NIP-17-DM om een project of nieuwsbericht te delen via het [Nostr Compass-project](https://github.com/andotherstuff/nostr-compass).
