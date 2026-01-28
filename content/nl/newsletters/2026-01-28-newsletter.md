---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor Nostr.

**Deze week:** Ridestr brengt gedecentraliseerd ridesharing naar Nostr met [Cashu](/nl/topics/cashu/)-betalingen en versleutelde locatiedeling. Pomade introduceert e-mailgebaseerd herstel voor multisig-ondertekenaars. Damus levert [negentropy](/nl/topics/negentropy/) voor betrouwbare DM-synchronisatie. De desktopapp van Amethyst krijgt zoeken, bladwijzers en zaps. Amber v4.1.1 toont relay-vertrouwensscores. Marmot merget MIP-03 en bouwt een TypeScript-referentie chatapp. diVine voegt [NIP-46](/nl/topics/nip-46/) QR-authenticatie en mentions-ondersteuning toe. Nieuwe NIP-voorstellen behandelen communitybeheer, sequentiegebaseerde synchronisatie en versleutelde bestandsopslag. We kijken ook terug op vijf jaar Nostr-januaries, en volgen de evolutie van het protocol van een handvol early adopters in 2021 via de explosieve App Store-lancering van Damus in 2023 naar het volwassen wordende client-ecosysteem van 2025.

## Nieuws

### Ridestr Brengt Gedecentraliseerd Ridesharing naar Nostr

[Ridestr](https://github.com/variablefate/ridestr) ontwikkelt een peer-to-peer rideshare-applicatie die volledig op Nostr is gebouwd, en directe chauffeur-passagier transacties mogelijk maakt met Bitcoin en [Cashu](/nl/topics/cashu/)-betalingen. Het protocol gebruikt aangepaste event kinds (30173, 3173-3175, 30180/30181) om ritten te coördineren terwijl privacy behouden blijft door progressieve locatieonthulling en [NIP-44](/nl/topics/nip-44/)-encryptie.

Het systeem werkt via een zorgvuldig gechoreografeerde flow: chauffeurs zenden beschikbaarheid uit met geohash-gecodeerde locaties (~5km precisie) via kind 30173 events, passagiers vragen ritten aan met tariefschattingen via kind 3173, en betalingen worden beveiligd met HTLC escrow tokens voordat de rit begint. Locatieprivacy wordt bewaard door progressieve onthulling, waarbij ophaaldetails alleen worden onthuld wanneer chauffeurs arriveren en bestemmingen worden gedeeld na PIN-verificatie. Alle communicatie tussen partijen gebruikt [NIP-44](/nl/topics/nip-44/)-encryptie voor privacy.

Ridestr implementeert betalingsbeveiliging via HTLC escrow met P2PK-handtekeningen. Wanneer een passagier het aanbod van een chauffeur accepteert, vergrendelen ze [Cashu](/nl/topics/cashu/)-tokens met een betaalhash die alleen de chauffeur kan claimen na voltooiing van de rit. Het protocol werkt momenteel met single-mint architectuur, wat vereist dat passagiers en chauffeurs dezelfde [Cashu](/nl/topics/cashu/) mint gebruiken. De op Kotlin gebaseerde Android-implementatie van het project handelt proof-verificatie af en herstel van verouderde proofs via NUT-07 state checks.

Ridestr pakt uitdagingen aan die de meeste Nostr-applicaties vermijden: realtime locatiecoördinatie, betalingsescrow met geschillenbeslechting en reputatiesystemen voor interacties in de fysieke wereld. Het project is in beta en demonstreert dat Nostr's event-model peer-to-peer servicemarktplaatsen kan ondersteunen, niet alleen het delen van content.

### Pomade Lanceert Alpha-Herstelsysteem voor Multisig-Ondertekenaars

[Pomade](https://github.com/coracle-social/pomade), ontwikkeld door hodlbod, bouwt voort op het bestaande [FROSTR](https://github.com/FROSTR-ORG)-ecosysteem om een op herstel gerichte threshold signing service te bieden. Met [FROST](/nl/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) handtekeningen via de @frostr/bifrost library, voegt Pomade e-mailgebaseerde herstelflows toe bovenop de threshold-cryptografie. Het systeem verdeelt de geheime sleutel van een gebruiker via Shamir Secret Sharing, en distribueert shares over meerdere onafhankelijke ondertekenaars met een configureerbare drempel (2-van-3, 3-van-5, etc.).

Het protocol werkt volledig over Nostr met een enkel event kind (28350) met [NIP-44](/nl/topics/nip-44/) versleutelde payloads. Bij het ondertekenen vraagt de client partiële handtekeningen op van minimaal `threshold` ondertekenaars, waarna deze worden samengevoegd tot een geldige Schnorr-handtekening. Voor encryptie werken ondertekenaars samen om gedeelde geheimen af te leiden via ECDH zonder dat een enkele partij de volledige sleutel kent.

Herstel werkt via twee authenticatiemethoden: wachtwoordgebaseerd (met argon2id met de pubkey van de ondertekenaar als salt) of e-mail OTP. Om MITM-aanvallen tijdens OTP-herstel te voorkomen, genereert elke ondertekenaar zijn eigen verificatiecode met een door de client verstrekte prefix, wat gebruikers verplicht om onafhankelijk te authenticeren bij elke ondertekenaar. Het protocol vereist proof-of-work op registratie-events (20+ bits per [NIP-13](/nl/topics/nip-13/)) om spam te voorkomen.

Het vertrouwensmodel is expliciet: als `threshold` ondertekenaars samenspannen, kunnen ze de sleutel stelen. E-mailproviders worden volledig vertrouwd aangezien zij OTP's kunnen onderscheppen. Gebruikers kunnen hun volledige geheime sleutel niet onafhankelijk herstellen; dit vereist medewerking van `threshold` ondertekenaars. Het protocol is ontworpen voor het onboarden van nieuwe gebruikers die niet vertrouwd zijn met sleutelbeheer, met de expliciete aanbeveling dat gebruikers migreren naar self-custody zodra ze comfortabel zijn. Pomade waarschuwt voor mogelijke "sleutelverlies, diefstal, denial of service, of metadata-lekkage" gezien de ongeauditte alpha-status.

## Releases

### Damus Levert Negentropy voor Betrouwbare DM-Synchronisatie

[Damus v1.13](https://github.com/damus-io/damus/releases/tag/v1.13-6) levert de negentropy-implementatie die [we vorige week als open PR previewed hebben](/nl/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs). [PR #3536](https://github.com/damus-io/damus/pull/3536) voegt basis [negentropy](/nl/topics/negentropy/)-ondersteuning toe aan de netwerklaag, wat set reconciliation mogelijk maakt met relays die het protocol ondersteunen. Een begeleidende [PR #3547](https://github.com/damus-io/damus/pull/3547) voegt pull-to-refresh DM-synchronisatie toe die negentropy gebruikt om ontbrekende berichten te herstellen wanneer standaard REQ-abonnementen falen.

De implementatie volgt een conservatieve aanpak: normale DM-loading gaat ongewijzigd door, met [negentropy](/nl/topics/negentropy/) beschikbaar als herstelmechanisme wanneer gebruikers handmatig verversen. Geautomatiseerde tests demonstreren de fix door een DM te genereren met een oude timestamp die standaard queries zouden missen, en vervolgens negentropy sync te gebruiken om deze succesvol op te halen. Hoewel [negentropy](/nl/topics/negentropy/)-ondersteuning compatibele relays vereist, gaat de implementatie elegant om met gemengde relay-omgevingen door het protocol te gebruiken waar beschikbaar.

### Amber v4.1.1 - Relay-Vertrouwensscores

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1) levert weergave van relay-vertrouwensscores ([PR #289](https://github.com/greenart7c3/Amber/pull/289)), en implementeert de relay-evaluatieconcepten die we bespraken in [de Trusted Relay Assertions NIP-coverage van vorige week](/nl/newsletters/2026-01-21-newsletter/#nip-updates). Vertrouwensscores verschijnen nu op de Relays-pagina en voor NostrConnect-verbindingsverzoeken, wat gebruikers helpt relay-betrouwbaarheid te beoordelen voordat ze verbindingen autoriseren. De release bevat ook een herontworpen login/events/permissions UI en ondersteuning voor de `switch_relays`-methode. Prestatieverbeteringen cachen keystore-operaties, wat rapporten van 20+ seconden laadtijden op oudere apparaten aanpakt.

### nak v0.18.2 - MCP-Integratie

fiatjaf's [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) [v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2) voegt [Model Context Protocol](https://nostrify.dev/mcp)-ondersteuning toe via `nak mcp`, wat AI-agents in staat stelt om mensen op Nostr te zoeken, notities te publiceren, gebruikers te vermelden en content te lezen met het outbox-model. De release introduceert ook een [one-line installer](https://github.com/fiatjaf/nak/blob/master/install.sh) (`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`) die voorgebouwde binaries downloadt, wat de Go-toolchain-vereiste elimineert voor eindgebruikers. Bunker-modus ondersteunt nu Unix sockets en `switch_relays`.

### Zeus v0.12.2 Beta - NWC-Fixes

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases) levert meerdere NWC-fixes die problemen aanpakken die we behandelden in [de Zeus-coverage van vorige week](/nl/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect).

## Projectupdates

### Amethyst Desktop - Fase 2A Geleverd

[Amethyst](https://github.com/vitorpamplona/amethyst) heeft [Fase 2A van zijn desktopapp](https://github.com/vitorpamplona/amethyst/pull/1676) uitgerold, met Zoeken, Bladwijzers, Zaps, Thread-weergaven en langvormige content (Reads) voor de desktopervaring. Een begeleidende [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683) voegt transparante feedback voor event-broadcasting toe, zodat gebruikers nu realtime per-relay status zien terwijl hun events zich over het netwerk verspreiden, wat het gemakkelijker maakt om connectiviteitsproblemen te diagnosticeren.

### Notedeck Voortgang: Kalender-App en UX-Polish

De Damus-team's [Notedeck](https://github.com/damus-io/notedeck) desktopclient heeft auto-hide toolbar-gedrag gemerged ([PR #1268](https://github.com/damus-io/notedeck/pull/1268)) dat reageert op scrollsnelheid voor meer schermruimte op mobiele weergaven. Een [draft PR #1271](https://github.com/damus-io/notedeck/pull/1271) voegt een volledige [NIP-52](/nl/topics/nip-52/) Kalender-app toe met maand/week/dag/agenda-weergaven, RSVP-ondersteuning en [NIP-22](/nl/topics/nip-22/)-reacties op kalenderevents, momenteel feature-flagged voor testen.

### Jumble Voegt Community-Modus Toe

[Jumble](https://github.com/CodyTseng/jumble), de relay-gerichte webclient, heeft [community-modus](https://github.com/CodyTseng/jumble/pull/738) toegevoegd en ondersteuning voor [relay set presets via omgevingsvariabelen](https://github.com/CodyTseng/jumble/pull/736), wat het gemakkelijker maakt om thema-instanties te deployen zoals [nostr.moe](https://nostr.moe/).

### Shopstr Orders-Dashboard

[Shopstr](https://github.com/shopstr-eng/shopstr) heeft zijn chatgebaseerd orderbeheer vervangen door een dedicated [Orders Dashboard](https://github.com/shopstr-eng/shopstr/pull/219). De nieuwe interface biedt een gecentraliseerd overzicht voor handelaren om orderstatus te volgen, berichten als gelezen te markeren en fulfillment te beheren zonder door chatthreads te scrollen. De update depreceert IndexedDB-caching ten gunste van server-side orderstatus-API's en herziet hoe order-DM's worden getagd voor betere filtering.

### Formstr Voegt Rastervragen Toe

[Formstr](https://github.com/abh3po/nostr-forms), de Nostr-native formulieren-app, heeft [rastervragen](https://github.com/abh3po/nostr-forms/pull/419) toegevoegd en [zijn SDK herschreven](https://github.com/abh3po/nostr-forms/pull/410) met embed-ondersteuning. Een [fix voor niet-[NIP-07](/nl/topics/nip-07/)-ondertekenaars](https://github.com/abh3po/nostr-forms/pull/418) loste problemen op voor gebruikers met bunker of lokale ondertekenaars die formulieren probeerden in te dienen met hun identiteit.

### nostr-tools Upgradet Crypto-Dependencies

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), de kern JavaScript-library, [heeft geupgrade naar @noble/curves v2.0.1](https://github.com/nbd-wtf/nostr-tools/pull/520), wat breaking API-wijzigingen over 27 bestanden aanpakt en de nieuwste geauditte noble libraries adopteert. fiatjaf voegde ook `switch_relays`-ondersteuning toe aan [NIP-46](/nl/topics/nip-46/), wat bunker-clients in staat stelt om dynamisch relay-verbindingen te wijzigen.

### Zeus Werkt aan NIP-87 Mint Reviews

[Zeus](https://github.com/ZeusLN/zeus) heeft een [open PR voor [NIP-87](/nl/topics/nip-87/) mint reviews](https://github.com/ZeusLN/zeus/pull/3576), waarmee gebruikers [Cashu](/nl/topics/cashu/) mints kunnen ontdekken en reviewen, gefilterd op Nostr-follows. Reviews bevatten sterbeoordelingen en kunnen anoniem of met de nsec van een gebruiker worden ingediend.

### Camelus Levert Volledige DM-Ondersteuning

[Camelus](https://github.com/camelus-hq/camelus), een Flutter-gebaseerde Android-client gebouwd met Dart NDK voor batterij-efficiente mobiele prestaties, heeft uitgebreide direct messaging toegevoegd met 20+ commits deze week. De update bevat chatcategorieën, berichtdatums, optimistische verzend-UI, note-to-self-functionaliteit en correcte DM-relay-handling.

### Marmot Protocol Updates

De MIP-03 deterministische commit-resolutie die [we vorige week als open PR behandelden](/nl/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library) is nu gemerged. [MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152) zorgt ervoor dat alle [MLS](/nl/topics/mls/)-gebaseerde groepschats convergeren naar dezelfde staat wanneer meerdere geldige commits aankomen voor hetzelfde epoch.

Een begeleidende [spec PR #28](https://github.com/marmot-protocol/marmot/pull/28) voegt init_key-levenscyclusvereisten toe die hiaten aanpakken van implementatie-audits: privésleutelmateriaal van Welcome-berichten moet veilig worden verwijderd na verwerking (zeroization, storage cleanup), en nieuwe leden moeten self-updates uitvoeren binnen 24 uur voor forward secrecy.

De TypeScript SDK ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) bouwt een referentie chatapplicatie. [PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37) voegt groepscreatie/listing toe, key package management met publish/broadcast/delete flows, en QR-code uitnodigingen. Een [open PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) door hzrd149 implementeert berichtgeschiedenispersistentie met paginering. Op whitenoise-rs zijn deze week 8 PR's naar master gemerged, met name Add event id to user reaction die het verwijderen van reacties mogelijk maakt door reactie-event-ID's bloot te stellen, en fix(message_aggregator/emoji_utils): improve is_valid_emoji to capture more valid emoji die emoji-validatie uitbreidt om uitgebreide Unicode-blokken, regionale indicatoren en keycap-sequenties te ondersteunen. Andere updates omvatten opslag van taalvoorkeuren voor client-side lokalisatie en verwijdering van standaard bijnamen om clients volledige controle over aanmeldingsmetadata te geven.

### diVine Voegt Nostr-Integratiefuncties Toe

[diVine](https://github.com/divinevideo/divine-mobile), de korte-video-app, continueert snelle Nostr-integratie.

Recente merges omvatten [NIP-46](/nl/topics/nip-46/) QR-code authenticatie ([PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)) en [NIP-17](/nl/topics/nip-17/) versleutelde directe berichten ([PR #834](https://github.com/divinevideo/divine-mobile/pull/834)). De activiteit van deze week richtte zich op [mentions-ondersteuning](https://github.com/divinevideo/divine-mobile/pull/1098) die `nostr:` URI's en @mentions converteert naar klikbare profiellinks, [Classic Viners avatar-fallbacks](https://github.com/divinevideo/divine-mobile/pull/1097) met Nostr-profielen, en videobewerkingstools inclusief [tekenen](https://github.com/divinevideo/divine-mobile/pull/1056), [filters](https://github.com/divinevideo/divine-mobile/pull/1053) en [stickers](https://github.com/divinevideo/divine-mobile/pull/1050).

## NIP-Updates

Recente wijzigingen aan de [NIPs repository](https://github.com/nostr-protocol/nips):

**Open PR's en Discussies:**

- **[Trusted Relay Assertions](https://github.com/nostr-protocol/nips/pull/1534)** - Het conceptvoorstel voor het standaardiseren van relay-vertrouwensscoring dat [we vorige week behandelden](/nl/newsletters/2026-01-21-newsletter/#nip-updates) wordt nog steeds bediscussieerd. Het kerngedebat draait om of vertrouwensscores "globaal" (eenmaal berekend voor alle gebruikers) of "gepersonaliseerd" (relatief aan de sociale grafiek van elke waarnemer) moeten zijn. PageRank-achtige algoritmen zoals [nostr.band's Trust Rank](https://trust.nostr.band/) en [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) weerstaan sybil-aanvallen door elke rang die door nepaccounts wordt doorgegeven te delen door de grootte van de botfarm. Critici stellen dat echt gepersonaliseerde scores nauwkeuriger zijn maar dure per-gebruiker berekening vereisen. De discussie verkent ook of DVM's gebruikt moeten worden voor on-demand scoring versus voorberekende kind 30382 attestatie-events die clients kunnen cachen.

- **Communikeys** - Een [uitgebreid voorstel](https://nostrhub.io) voor communitybeheer dat bestaande npubs gebruikt als community-identifiers in plaats van relay-gebaseerde benaderingen. Elke npub kan een community worden door een kind 10222 event te publiceren; publicaties richten zich op communities via kind 30222 events. Toegangscontrole gebruikt [NIP-58](/nl/topics/nip-58/) badges, wat gedelegeerd lidmaatschapsbeheer mogelijk maakt met cold storage voor communitysleutels.

- **[NIP-CF: Changes Feed](https://njump.me/nevent1qqsyxrrdu09yktr7x5cqqrcj9v2hrqqqefem6f3stkrzwf8anr236sgcpzfmhxue69uhkummnw3ezu7nzvshxwec4wa0qn)** - Een concept dat sequentiegebaseerde eventsynchronisatie voorstelt als alternatief voor tijdstempelgebaseerde `since`-filters. Het probleem: standaard Nostr-sync met `since`-tijdstempels kan events missen wanneer meerdere events dezelfde seconde-precisie tijdstempel delen, client- en relayklokken uit elkaar drijven, of checkpointing onnauwkeurig is. NIP-CF lost dit op door relays monotoon oplopende volgnummers te laten toewijzen aan opgeslagen events, wat strikte totale ordening biedt. Clients vragen wijzigingen op sinds een specifiek volgnummer en ontvangen events in gegarandeerde volgorde, met precieze checkpointing die nooit events mist. Het voorstel ondersteunt ook live/continue modus waarbij abonnementen open blijven na initiële sync voor realtime updates.

- **[NIP-XX: Encrypted File Sync](https://njump.me/nevent1qqsr98tvcy7c4y5w03rd6cdujq9dpdt75uzv4kmkgpdlq7ggdmzptrqcpzfmhxue69uhkummnw3ezu7nzvshxwec4wa0qn)** - Een protocol dat kinds 30800 (versleutelde bestanden), 30801 (vault-indexen) en 30802 (gedeelde documenten) definieert voor het synchroniseren van versleutelde content over apparaten via Nostr relays. Het protocol maakt het mogelijk dat local-first notitie-apps end-to-end versleutelde sync bieden zonder gecentraliseerde servers. Bestandsinhoud, paden, namen en mapstructuur zijn allemaal versleuteld met [NIP-44](/nl/topics/nip-44/) zelfencryptie, zodat relays blobs opslaan die ze niet kunnen lezen. Binaire bijlagen zoals afbeeldingen gebruiken [Blossom](/nl/topics/blossom/)-servers met client-side encryptie. Kind 30802 maakt het delen van documenten tussen gebruikers mogelijk door te versleutelen naar de publieke sleutel van de ontvanger.

## Vijf Jaar Nostr-Januaries

[De nieuwsbrief van vorige maand](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers) traceerde Nostr's december-mijlpalen van fiatjaf's eerste clientrelease tot Jack Dorsey's katalyserende donatie. Deze terugblik brengt in kaart wat er elke januari gebeurde van 2021 tot en met 2025, met focus op geverifieerde technische ontwikkelingen.

### Januari 2021: Vroege Ontwikkeling

Nostr's derde maand zag voortgezette ontwikkeling aan Branle, fiatjaf's Vue.js client die in december 2020 was gelanceerd. Een kleine groep early adopters, waarschijnlijk minder dan 15 mensen, coördineerde via de Telegram-groep [@nostr_protocol](https://t.me/nostr_protocol) (aangemaakt op 16 november 2020), en testte het protocol op een of twee experimentele relays. De command-line client noscl bood terminalgebaseerde interactie.

De technische basis was al vastgelegd: gebruikers geïdentificeerd door secp256k1 publieke sleutels, posts cryptografisch ondertekend met Schnorr-handtekeningen, en relays die fungeren als domme opslag die niet met elkaar communiceren. Dit was bewust Bitcoin-native cryptografie, een ontwerpkeuze die adoptiepatronen jaren later zou vormgeven.

### Januari 2022: Ontwikkelaarsontdekking

Januari 2022 opende met Nostr nog steeds gonzend van zijn [eerste Hacker News-verschijning](https://news.ycombinator.com/item?id=29749061) (31 december 2021), die 110 punten en 138 reacties genereerde. Op het moment van die post draaiden slechts ongeveer zeven relays het hele netwerk, waarbij commentatoren opmerkten dat "spam nog geen probleem is omdat nostr super nieuw is en niemand het nog gebruikt." Robert C. Martin ("Uncle Bob") had Nostr onderschreven als mogelijk "de eindoplossing voor sociale communicatie." De discussie ging door tot in januari, met ontwikkelaars die debatteerden over relay-architectuur versus echte P2P, censuurbestendigheid versus moderatie, en of eenvoud kon schalen.

De HN-post veroorzaakte een golf van nieuwe implementaties. Uncle Bob zelf startte [more-speech](https://github.com/unclebob/more-speech), een Clojure desktopclient, op 18 januari. fiatjaf's [go-nostr](https://github.com/nbd-wtf/go-nostr) library (aangemaakt januari 2021) en [noscl](https://github.com/fiatjaf/noscl) command-line client boden Go-tooling, terwijl [nostr-tools](https://github.com/nbd-wtf/nostr-tools) JavaScript-ondersteuning bood. Tegen december 2022 hadden ongeveer 800 profielen bio's. Branle bleef de primaire webclient en ontving updates waaronder private key import en multi-relay ondersteuning. Technische uitdagingen waren evident: 64-karakter hex sleutels bleken onintuïtief, berichtvertragingen frustreerden gebruikers, en de community vroeg zich af of de architectuur Twitter-schaal verkeer aankon.

### Januari 2023: De Doorbraak

Januari 2023 transformeerde Nostr van experiment naar beweging. Damus, de iOS-client van William Casarin (jb55), vocht met Apple's App Store-goedkeuringsproces. Afgewezen op 1 januari, opnieuw afgewezen op 26 januari, werd het uiteindelijk [goedgekeurd op 31 januari](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store). Die goedkeuring ontketende een cascade: Damus bereikte onmiddellijk #10 in U.S. Social Networking. Jack Dorsey [noemde het](https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store) "een mijlpaal voor open protocollen."

Acht dagen eerder, op 23 januari, [kondigde Edward Snowden](https://x.com/Snowden/status/1617623779626352640) zijn aanwezigheid op Nostr aan: "Een van de coole dingen aan Nostr... naast censuurbestendigheid, is dat je niet beperkt bent tot 280 tekens." Zijn steunbetuiging als NSA-klokkenluider had gewicht in privacybewuste kringen, en gebruikers begonnen hem onmiddellijk sats te zappen via Lightning.

Webclients raceten om de instroom te onboarden. [Snort](https://github.com/v0l/snort), gecreëerd door kieran in december 2022, verscheen als een feature-rijke React-client; op 13 januari integreerde Snort NIP-05-registratie via de Nostr Plebs API, waarmee nieuwe gebruikers leesbare identiteiten konden claimen tijdens onboarding. [Iris](https://iris.to), fulltime ontwikkeld door Martti Malmi (een vroege Bitcoin-bijdrager die de tweede Bitcoin-transactie ooit ontving van Satoshi), bood zowel web- als mobiele interfaces met gratis NIP-05 identiteiten op iris.to. [Astral](https://github.com/monlovesmango/astral), gebouwd door monlovesmango met Quasar (Vue.js) als Branle-fork, richtte zich op relaybeheer met zijn relay-groeperingsfunctie waarmee gebruikers relays konden organiseren in sets voor posten en filteren. TestFlight beta's voor iOS-clients vulden zich binnen uren, en Amethyst domineerde Android.

Infrastructuur worstelde om bij te blijven. Alle relays werden beheerd door enthousiastelingen die uit eigen zak betaalden. Betaalde relays met Lightning-microbetalingen creëerden natuurlijke spamfiltering maar introduceerden toegangsfrictie. [Damus werd uit China's App Store verwijderd](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) slechts twee dagen na goedkeuring, naar verluidt op verzoek van China's hoogste internetwaakhond.

### Januari 2024: Protocolversterking

Januari 2024 richtte zich op protocolstandaardisatie en communitybuilding. [Nostr PHX](https://www.nostrphx.com/events) trapte het jaar af met een meetup op 5 januari in Phoenix, die lokale cypherpunks samenbracht. Dit was de eerste van vele community-events dat jaar, waaronder BTC Prague (juni), Nostriga in Riga (augustus) en Nostrasia.

De belangrijkste protocolontwikkeling was [NIP-59 (Gift Wrap)](https://github.com/nostr-protocol/nips/pull/716) die werd gemerged op 29 januari, wat metadatabescherming bood voor versleutelde communicatie. Gift Wrap bouwt voort op [NIP-44's encryptiestandaard](https://github.com/paulmillr/nip44) (die was [geaudit door Cure53](https://cure53.de/audit-report_nip44-implementations.pdf) in december 2023) om afzenderidentiteit te verbergen voor relays. Het protocol verpakt versleutelde berichten in een buitenste event ondertekend door een willekeurig, eenmalig sleutelpaar. Relays zien alleen de wegwerp-pubkey, terwijl de echte identiteit van de afzender begraven ligt in de versleutelde payload die alleen de ontvanger kan ontcijferen. Dit voorkomt dat relay-operators en netwerkwaarnemers leren wie met wie berichten uitwisselt. Tijdstempels kunnen ook worden gerandomiseerd om timinganalyse te verslaan.

Het ecosysteem breidde uit voorbij sociale media. [Plebeian Market](https://plebeian.market) werd volledig Nostr-native met [NIP-15](/nl/topics/nip-15/)-compliance, wat cross-stall winkelwagens en een stallenbrowser mogelijk maakte voor het ontdekken van handelaren. [Shopstr](https://github.com/shopstr-eng/shopstr) verscheen als een toestemmingsloze marktplaats die Bitcoin-handel faciliteerde. [Zap.stream](https://zap.stream/), gebouwd door kieran, bracht livestreaming naar Nostr met Lightning-betalingen tegen 21 sats/minuut. Ontwikkelaarstools werden volwassener met [NDK](https://github.com/nostr-dev-kit/ndk) die TypeScript-abstracties bood en [rust-nostr](https://github.com/rust-nostr/nostr) die Rust-bindings bood. [Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/) leverde Nostr-contactimport en persistente LND, wat de basis legde voor Nostr Wallet Connect-integratie in latere releases.

Toch [bleef infrastructuurduurzaamheid uitdagend](https://arxiv.org/abs/2402.05709). Academisch onderzoek uit deze periode vond dat 95% van de relays moeite had om operationele kosten te dekken, met 20% die significante downtime ervoer. De toegangsprijs voor betaalde relays bedroeg gemiddeld minder dan 1.000 sats (~$0,45), onvoldoende om operaties te ondersteunen.

*Een opmerking over scams: Het "Nostr Assets Protocol" en bijbehorende "$NOSTR" token dat rond deze tijd lanceerde [werd publiekelijk veroordeeld door fiatjaf](https://www.aicoin.com/en/article/377704) als "100% frauduleus" en "een affiniteitszwendel" zonder connectie met het daadwerkelijke Nostr-protocol.*

### Januari 2025: Clientmaturatie

Januari 2025 zag voortgezette clientontwikkeling over het ecosysteem. [Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/) leverde op 13 januari met cross-device sync voor leesstatussen, [FROST](/nl/topics/frost/) multi-sig login-ondersteuning, en geoptimaliseerde lokale databaseprestaties. Amethyst zette zijn transitie naar het outbox-model voort, automatisch relay-sets compileren gebaseerd op volglijsten in plaats van handmatige configuratie te vereisen.

Grote clients begonnen weg te bewegen van [NIP-04](/nl/topics/nip-04/) voor directe berichten, migrerend naar [NIP-17](/nl/topics/nip-17/) en het voorgestelde [NIP-104](/nl/topics/nip-104/) voor verbeterde encryptie en metadatabescherming. Het Gossip-model (outbox/inbox-communicatie) won adoptie terwijl het ecosysteem convergeerde naar efficiëntere relay-gebruikspatronen. Industriewaarnemers voorspelden dat dit het jaar zou zijn dat Nostr zou overgaan van nicheprotocol naar mainstream erkenning, met een mogelijke high-profile platformmigratie die dagelijkse activiteit zou kunnen verdubbelen.

### Januari 2026: Beveiliging en Ondertekeningsinfrastructuur

Januari 2026 bracht significante vooruitgang in beveiliging en ondertekeningsinfrastructuur. [Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) leverde [NIP-46](/nl/topics/nip-46/) remote signing en [NIP-55](/nl/topics/nip-55/) lokale ondertekenaarondersteuning, en voegde zich bij Amber en Aegis als volledige signing hub voor andere Android-apps. [Bitchat voltooide een Cure53-beveiligingsaudit](https://github.com/permissionlesstech/bitchat/pulls), hetzelfde bedrijf dat Signal en NIP-44 auditeerde, met 17+ PR's die kritieke bevindingen fixten waaronder DH secret clearing en thread-veiligheidsproblemen. Zowel Bitchat als Damus migreerden van C Tor naar Rust Arti voor verbeterde betrouwbaarheid en geheugenveiligheid.

Protocolwerk ging door met [NIP-71](https://github.com/nostr-protocol/nips/pull/1669) (adresseerbare video-events) die mergede en een post-quantum cryptografie NIP die discussie opende over het toekomstbestendig maken van Nostr tegen kwantumaanvallen. Het Trusted Relay Assertions-concept stelde voor om relay-vertrouwensscoring te standaardiseren via ondertekende attestaties. Het [Marmot Protocol](https://github.com/marmot-protocol/mdk) verhardde zijn [MLS](/nl/topics/mls/)-gebaseerde versleutelde berichten met 18 gemerged PR's die auditbevindingen aanpakten.

Real-world applicaties breidden uit met [Ridestr](https://github.com/variablefate/ridestr) die gedecentraliseerd ridesharing ontwikkelde met [Cashu](/nl/topics/cashu/) escrow en [NIP-44](/nl/topics/nip-44/)-encryptie, en [Pomade](https://github.com/coracle-social/pomade) die e-mailgebaseerde herstelflows toevoegde aan [FROST](/nl/topics/frost/) threshold signing. Damus leverde [negentropy](/nl/topics/negentropy/) voor betrouwbare DM-synchronisatie, terwijl Amethyst's desktopapp Fase 2A bereikte met zoeken, bladwijzers en zaps.

### Vooruitkijken

Zes jaar van Januaries onthullen Nostr's evolutie van vroege ontwikkeling (2021) naar publieke ontdekking (2022) naar explosieve groei (2023) naar protocolversterking (2024) naar clientmaturatie (2025) naar beveiligingsinfrastructuur (2026). Het patroon is bekend voor iedereen die open protocollen heeft zien groeien: jaren van stil bouwen, een plotselinge explosie wanneer de omstandigheden samenkomen, dan het langere werk om alles betrouwbaar te maken. Wat begon met zeven relays en een Hacker News-thread is nu geauditte infrastructuur met echte applicaties. De vraag voor 2027: wanneer iemand een rit aanvraagt, een versleuteld bericht verstuurt, of een verloren sleutel herstelt met Nostr, zullen ze dan zelfs weten dat ze het gebruiken?

---

Dat was het voor deze week. Iets aan het bouwen? Nieuws te delen? Wil je dat we je project behandelen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via NIP-17 DM</a> of vind ons op Nostr.
