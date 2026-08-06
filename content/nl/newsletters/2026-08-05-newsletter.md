---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
translationOf: /en/newsletters/2026-08-05-newsletter.md
translationDate: 2026-08-06
draft: false
type: newsletters
description: "Sandstr biedt rondleidingen met mockdata door Nostr-clients, nostr-mill voegt ondertekeningstoestemming per event toe, en nostrord breidt relay-gehoste groepen uit. De deep dives behandelen relay-ondersteund zoeken en draagbare highlights."
---

Welkom terug bij [Nostr Compass](https://github.com/andotherstuff/nostr-compass), je wekelijkse gids voor Nostr.

**Deze week:** [Sandstr](https://sandstr.app/) laat nieuwkomers gesimuleerde Nostr-clients verkennen zonder sleutels aan te maken of een app te installeren. [nostr-mill](https://github.com/0ceanSlim/nostr-mill) voegt ondertekeningstoestemming per event en sleutelherstel tussen clients toe, terwijl [nostrord](https://github.com/nostrord/nostrord) relay-gehoste groepen, signers, moderatie, uploads en highlights uitbreidt. Protocolwerk beslaat Nostr-eventformaten, wallet-verbindingen, relay-discovery, napplets, Marmot en Concord; de deep dives leggen relay-ondersteund zoeken en draagbare highlights uit.

## Topverhalen

### nostr-mill 1.6.0 brengt ondertekeningstoestemming en accountherstel naar de browser

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) is een inbeddbare browser-accountkiezer en -signer. Hij vraagt nu om toestemming per event-kind en toont gedecodeerde inhoud en tags vóór het ondertekenen, met tijdsbeperkte verleningen en een permissiebeheerder. De release herstelt ook een bug in de eerste sessie waardoor categorieën die zo geconfigureerd waren dat ze elke keer moesten vragen zonder te vragen konden ondertekenen. De optionele Google-onboarding kan een bestaande `nsec` importeren, slaat de sleutel versleuteld op in de Drive-app-gegevensmap van de gebruiker, ondersteunt meerdere identiteiten en kan een `ncryptsec` exporteren in het [NIP-49](/nl/topics/nip-49/)-formaat (versleuteld privésleutelformaat).

De [experimentele relay-backup](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) leidt een sterke herstelzin af met scrypt en HKDF, verpakt de sleutel als `ncryptsec`, verifieert opgehaalde events en vereist een relay-quorum vóór herstel. [NIP-55](/nl/topics/nip-55/)-login (Android-signer-intents) gebruikt nu Ambers klembord-retourpad, en [NIP-46](/nl/topics/nip-46/)-verbindingen (relay-bemiddeld remote signing) zijn standaard stil. Branding-controls en responsieve permissieschermen maken de release compleet zonder bestaande integraties te wijzigen, tenzij een operator daarvoor kiest.

### nostrord 2.5.0 geeft relay-groepen stabiele, relay-specifieke identiteiten

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) is een cross-platform client voor relay-gehoste gemeenschappen. Hij leidt nu een [NIP-29](/nl/topics/nip-29/)-identiteit (relay-beheerde groepen) af uit zowel groeps-ID als host-relay, begrenst lidmaatschap en beheerdersbadges op dezelfde manier, accepteert groeps-`naddr`-deeplinks en synchroniseert privégroepsthreads tussen apparaten.

De [release](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) voegt ook een [NIP-56](/nl/topics/nip-56/)-moderatie-inbox (rapport-events) toe, Amber-login via NIP-55, rate-limit-backoff voor NIP-46-signerverkeer, [NIP-84](/nl/topics/nip-84/)-rendering (draagbare highlights) met nieuwe pogingen voor onopgeloste verwijzingen, en media-uploads via Blossom of [NIP-96](/nl/topics/nip-96/) (HTTP-bestandsopslag). Google-login maakt nu een back-up van de sleutel vóór het aanmaken van het account en bevestigt verbroken verbindingen. Thread-antwoorden krijgen rijkere inhoud en beheerdersverwijdering, terwijl fixes voor de desktop-sleutelhanger en het mobiele toetsenbord die protocolfuncties bruikbaar houden.

### Primal Android 3.5.25 werkt remote signing en volglijst-filtering bij

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) is een mobiele Nostr-client met feeds, zoeken en remote signing. Hij werkt zijn remote signer bij voor het huidige protocolgedrag, voegt een demp-lijst voor gevolgden toe, opent zoeken vanuit Verkennen, herstelt vastgelopen relay-verbindingen automatisch, legt request-time-outs bloot in de interface, weigert ongeldige volglijst-items en ververst fallback-relay-URL's. Feed-prefetching, lager geheugengebruik en een cacheplafond van 100 MB verlagen de kosten van het actueel houden van die feeds. Notities met één afbeelding gebruiken nu de volledige inhoudsbreedte, en profielcontrols en media-preloading krijgen kleinere interactie- en ordeningsfixes.

### Nostur 1.30.2 breidt privé-antwoorden en media in directe berichten uit

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) is een Nostr-client voor Apple-platforms. Hij toont nu altijd de actie voor privé-antwoorden, voegt DM-mediacaches per gesprek toe met limieten en wis-controls, verbetert naam- en tag-aanvulling in berichten en chats, toont gerefereerde berichten in livechat en neemt de kamertitel op in chatmeldingen. Fixes voor feed-paginering en geneste antwoorden pakken regressies in ophalen en gespreksweergave aan.

### Chama 5.7.0 voegt arbiterregisters en herstel van gecachte trades toe

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) coördineert peer-trades en arbitrage via ondertekende Nostr-eventketens. Hij toont het geblokkeerde bedrag van een arbiter, de looptijd van diens borg en de financierings-outpoint; registreert wanneer een vervanger een afwezige arbiter verving; en definieert slapende fout-attestaties van kind `38136` die de handtekeningen van beide principals vereisen. Een expliciete reparatie probeert onvolledige relay-historieën opnieuw tegen de duurzame apparaatcache en publiceert herstelde events opnieuw, terwijl mislukte publicaties in de wachtrij gaan voor de volgende verbinding. De release voorkomt ook dubbele arbiter-premiebetalingen tussen apparaten door het kind `38113`-event van de auteur als het betalingsbewijs te behandelen.

### Auditable Voting 0.1.165 herstelt levering van gedelegeerde stembiljetten

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) voert verifieerbare stemmingen uit terwijl kiezerscredentials gescheiden blijven van de inhoud van het stembiljet. Hij herstelt gedelegeerde uitgifte van blinde stembiljetten via geauthenticeerde delegatielevering en backfill van controle-DM's, houdt directe berichten met blinde credentials op de geconfigureerde privé-relays en werkt de auditproxy bij naar 0.1.52.

### Sandstr laat nieuwkomers Nostr-clients uitproberen met mockdata

[Sandstr](https://sandstr.app/) biedt interactieve browsersimulaties van Nostr-clients zodat een nieuwkomer hun interfaces kan vergelijken voordat hij er een installeert of een sleutelpaar aanmaakt. De lancering van 3 augustus omvat referentie-geverifieerde reproducties van Damus, Amethyst, Primal, Snort, YakiHonne, Coracle en Wisp, plus duidelijk gelabelde vroege previews van Gossip, Keychat en Olas. Alles draait lokaal tegen mockdata, dus de simulaties genereren geen sleutels en maken geen verbinding met relays. Elke simulatie linkt door naar de website en de bronrepository van de echte client, waardoor Sandstr een onboarding- en interface-vergelijkingstool is in plaats van nog een Nostr-client. Het laat zien hoe feeds, profielen, threads, directe berichten, zoeken, zaps en relay-controls aanvoelen zonder een eerste keer gebruiker vooraf een identiteits- of beveiligingsbeslissing te vragen.


### mineracks signer combineert een browserextensie met een desktop-bunker

[mineracks signer](https://github.com/mineracks/mineracks-signer) biedt twee ondertekeningsoppervlakken vanuit hetzelfde project. Zijn browserextensie implementeert [NIP-07](/nl/topics/nip-07/) zodat webapplicaties handtekeningen kunnen aanvragen zonder de privésleutel te ontvangen, terwijl de desktopapplicatie een [NIP-46](/nl/topics/nip-46/)-remote-signer beschikbaar stelt voor clients die via relays communiceren.

De [desktop-0.1.0-release](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0) van het project slaat sleutelmateriaal op met de NIP-49-versleutelde-sleutelcodering en houdt de ontsleutelde sleutel binnen het Rust-proces in plaats van hem aan de interface door te geven. Elk verzoek toont de aanroepende applicatie en de gevraagde actie, terwijl automatische goedkeuring per applicatie optioneel en herroepbaar is. De eerste desktopbuild ondersteunt Apple Silicon maar geen Intel-Macs.

## Releases

### Jumble 26.8.1 voegt proof-of-work-controls en commentaarpreviews toe

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) is een web- en desktop-Nostr-client. Hij onthoudt de proof-of-work-moeilijkheid voor publicatie, toont badges voor geverifieerd werk, toont previews van gelinkte commentaren boven externe inhoud, slaat afbeeldingen op vanuit de volledig-schermviewer en klapt lange profielbio's op verzoek uit. Reactiemeldingen verwerpen nu niet-ondersteunde event-kinds, meldingen over verbroken relay-verbindingen zijn minder luidruchtig, standaardrelays zijn ververst en een conflict met automatisch afspelen van media is verholpen.

### nostr-calendar 2.1.0 herstelt signer-binding voor privéformulieren

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) publiceert agenda's, events en formulierantwoorden als Nostr-data. Hij bindt inzendingen van privéformulieren aan de actieve signer, slaat opzettelijke dubbele events op relays op, herstelt het ophalen van relays, parseert agendadatums in lokale tijd en voegt app-meldingen plus een iOS-client toe. De signer-correctie voorkomt dat een verouderde identiteit een onbruikbaar versleuteld antwoord produceert.

### Manent 2.0.0 voegt tagging en zoeken toe voor opgeslagen notities

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) is een persoonlijk archief voor ondertekende Nostr-notities. Hij voegt lokale tags en zoeken toe, zodat een lezer opgeslagen events kan organiseren en terugvinden zonder hun ondertekende inhoud te wijzigen.

### nosvelte 0.6.1 sluit lege abonnementen na EOSE

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) biedt reactieve Svelte-componenten en -hooks voor relay-data. Lege zoekopdrachten komen nu tot rust bij End of Stored Events, annuleren sluit de onderliggende `REQ`, nieuwe pogingen wissen verouderde fouten en lijst-hooks geven hun gedocumenteerde lege waarde terug. Hij herkent ook adresseerbare events ongeacht waar hun `d`-tag staat, vervangt achterhaalde metadata en artikelen, dedupliceert reacties op event-ID en behoudt elk event uit de eerste batch van een relay.

## Onuitgebrachte wijzigingen

### NMP bindt relay-toelating aan declaraties en verbreedt groepsqueries

[NMP](https://github.com/pablof7z/nmp) is een TypeScript-toolkit voor het bouwen van Nostr-applicaties en relay-gesteunde groepsinterfaces. [PR #1254](https://github.com/pablof7z/nmp/pull/1254) laat relay-toelating de eigenaar volgen van de declaratie die hem autoriseert, waardoor de permissiebeslissing aan ondertekende Nostr-staat gehecht blijft. [PR #1255](https://github.com/pablof7z/nmp/pull/1255) generaliseert [NIP-29](/nl/topics/nip-29/)-queries voor relay-beheerde groepen in plaats van één smalle opzoekvorm aan te nemen. Beide wijzigingen zijn gemerged maar nog niet verschenen in een getagde release.

### Mosaico leidt de identiteit van beheerde groepen af uit relay-records

[Mosaico](https://github.com/pablof7z/mosaico) is een Nostr-client voor het bekijken en beheren van relay-beheerde gemeenschappen. [PR #758](https://github.com/pablof7z/mosaico/pull/758) leidt de identiteit van een beheerde groep af van de relay die diens gezaghebbende records host. [PR #757](https://github.com/pablof7z/mosaico/pull/757) observeert het gepubliceerde record van de groep bij het vaststellen van de beheerstaat. Zo blijven twee gelijknamige groepen op verschillende relays onderscheiden en krijgen clients een relay-gesteunde bron voor hun beheermetadata.

### Divine isoleert trage relays tijdens multi-relay-queries

[Divine](https://github.com/divinevideo/divine-mobile) is een mobiele korte-video-client die video's publiceert en ophaalt via Nostr. [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) geeft elke relay-query zijn eigen time-out in plaats van één vastgelopen verbinding het tijdsbudget van een hele request te laten opgebruiken. Resultaten van responsieve relays kunnen zo aankomen terwijl het trage eindpunt onafhankelijk wordt opgegeven. De wijziging verbetert het ophalen zonder één relay als gezaghebbend voor het gecombineerde resultaat te behandelen.

### rust-nostr verhardt versleuteling, hashes en reconciliatie

[rust-nostr](https://github.com/rust-nostr/nostr) is een Rust-bibliotheek en -toolkit voor Nostr-clients, -relays en protocolimplementaties. [PR #1421](https://github.com/rust-nostr/nostr/pull/1421) vermindert allocatie in het [NIP-44](/nl/topics/nip-44/)-versiegebonden versleutelingspad, terwijl [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) getypeerde hashes introduceert die het per ongeluk mengen van incompatibele digestwaarden moeilijker maken. [Commit 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) voorkomt dat een misvormd [NIP-77](/nl/topics/nip-77/)-Negentropy-set-reconciliatiebericht de lokale relay verbreekt. Het gemergde werk verscherpt zowel de afhandeling van versleutelde payloads als het faalgedrag van reconciliatie vóór de volgende release.

### Zeus serialiseert NWC-betalingen voordat bestedingsbudgetten worden belast

[Zeus](https://github.com/ZeusLN/zeus) is een mobiele Bitcoin- en Lightning-wallet die wallet-operaties via Nostr Wallet Connect kan beschikbaar stellen. [PR #4305](https://github.com/ZeusLN/zeus/pull/4305) telt hangende betalingen mee voor een [NIP-47](/nl/topics/nip-47/)-budget (Nostr Wallet Connect) in plaats van op afwikkeling te wachten. [PR #4303](https://github.com/ZeusLN/zeus/pull/4303) serialiseert de betalingsafhandeling zodat gelijktijdige verzoeken niet door dezelfde autorisatielimiet kunnen racen. Het gemergde paar dicht een hiaat in budgethandhaving op het Nostr-controleoppervlak van de wallet.

### Nostr Components deelt één relay-verbindingspoging

[Nostr Components](https://github.com/saiy2k/nostr-components) is een herbruikbare web-componentenbibliotheek om Nostr-data en -interacties aan applicaties toe te voegen. [PR #105](https://github.com/saiy2k/nostr-components/pull/105) laat tegelijk gemounte componenten een lopende relay-verbindingspoging delen. Elke afnemer ontvangt nog steeds de resulterende verbinding, maar gelijktijdige mounts openen geen dubbele sockets meer terwijl de eerste handshake nog loopt. De wijziging vermindert vermijdbare relay-belasting in applicaties die uit meerdere onafhankelijke componenten zijn samengesteld.

## NIP-updates en protocolspecificatiewerk

### Nostr-eventformaten en discovery

[NIP-PR #2430](https://github.com/nostr-protocol/nips/pull/2430) stelt stickerpacks voor als adresseerbare kind `30031`-definities en de geïnstalleerde packs van een gebruiker als vervangbaar kind `10031`. Elke stickertag draagt een shortcode, een SHA-256-hash en een MIME-type; de afbeelding blijft op een [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md)-server (Blossom-blobopslag). Het open ontwerp standaardiseert zo pack-identiteit en -installatie zonder afbeeldingsbytes in events te plaatsen.

[NIP-PR #2429](https://github.com/nostr-protocol/nips/pull/2429) stelt adresseerbare Gopher-documenten van kind `31436` voor. Elk event bevat één UTF-8-tekst- of menuknoop, en ondertekende knopen onder één pubkey vormen een gopherhole die elke relay-gesteunde RFC 1436-brug kan bedienen. Het open voorstel gebruikt gewone adresseerbare-eventopslag in plaats van de publicatie aan één Gopher-hostnaam te binden.

[NIP-PR #2428](https://github.com/nostr-protocol/nips/pull/2428) stelt privégroepen met epoche-tickets voor. Een groep roteert lidmaatschapscredentials tussen epoches, en clients tonen het ticket van de huidige epoche om deel te nemen. Het ontwerp richt zich op privéchat zonder een relay te vragen een permanent bearer-token als levenslang lidmaatschap te behandelen.

[NIP-PR #2425](https://github.com/nostr-protocol/nips/pull/2425), vorige week behandeld als voorstel, heeft nu een URI-verheldering in [NIP-B0](/nl/topics/nip-b0/) (adresseerbare webbladwijzers) gemerged. Hij onderscheidt weggelaten HTTPS-prefixen van expliciete URI-schema's wanneer een bladwijzer zijn doel in de `d`-tag opslaat, waardoor clients geen ambigue bestemming kunnen reconstrueren.

### Betalingen en wallet-verbindingen

[NIP-PR #2419](https://github.com/nostr-protocol/nips/pull/2419), behandeld als voorstel in de uitgave van 22 juli, heeft nu een kleinere [NIP-47](/nl/topics/nip-47/)-kern (Nostr Wallet Connect) gemerged. Verbindings-URI's, versleuteld relay-transport, capability-discovery, versleutelingsonderhandeling en gangbare methoden blijven in de NIP; meldingen, hold-invoices, keysend, transactiehistorie, metadata en deep-link-pairing verhuizen naar een eigen extensierepository. Bestaande verbindingen blijven compatibel terwijl wallets de optionele contracten onafhankelijk kunnen implementeren.

[NWC-PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2), vorige week behandeld als voorstel, heeft nu BIP-321-betaalmethoden in die extensierepository gemerged. BIP-321 biedt een gemeenschappelijke Bitcoin-betaal-URI die verschillende rails kan dragen, zodat NWC-aanroepers een betaling kunnen aanvragen of versturen zonder voor elk onderliggend instructietype een nieuwe kern-RPC toe te voegen.

### Napplet-hostmogelijkheden

[NAP-PR #95](https://github.com/napplet/naps/pull/95) stelt catalogus-discovery voor Nostr-gedistribueerde sandbox-applicaties voor. Een napplet vraagt zijn host welke applicaties en mogelijkheden beschikbaar zijn, en de host geeft policy-gefilterde metadata terug in plaats van zijn volledige lokale omgeving bloot te leggen. Het contract ondersteunt lanceerbeslissingen zonder uitvoeringsbevoegdheid te verlenen tijdens discovery.

[NAP-PR #33](https://github.com/napplet/naps/pull/33) stelt shell-bemiddelde bestands- en blob-uploads voor. Een napplet levert bytes en intentie; de host kiest een NIP-96- of Blossom-rail, ondertekent de autorisatie, rapporteert voortgang en geeft URL's, hashes, MIME-data en kant-en-klare [NIP-94](/nl/topics/nip-94/)-tags (bestandsmetadata) terug. Opslagcredentials en HTTP-autoriteit komen nooit in het napplet terecht.

### Marmot-versleutelde groepen

[Marmot-PR #410](https://github.com/marmot-protocol/marmot/pull/410) heeft convergentie- en uitgestelde-inputregels gemerged. Clients onderscheiden een object dat een actuele epoche-afhankelijkheid mist van verouderde of ongeldige input, houden het in aanmerking voor herophaling na een resourceweigering en proberen opnieuw wanneer een andere commit de ontsleutelingscontext wijzigt. Een domein-gescheiden staatscommitment geeft conformiteitstests een gedeeld convergentie-orakel zonder een productie-wireveld toe te voegen.

### Concord-communityvlakken

[Concord-PR #14](https://github.com/concord-protocol/concord/pull/14) heeft CORD-08-verdwijnende berichten gemerged. Eén community-metadatawaarde bepaalt de levensduur; chat-geruchten en versleutelde omhulsels dragen een [NIP-40](/nl/topics/nip-40/)-tag (event-verval), terwijl verwijderingsevents en de kind `1740`-timer-melding zijn vrijgesteld. De ondertekende timer reist mee met de community-staat, hoewel relay-verwijdering een retentieverzoek blijft in plaats van een cryptografische wissingsgarantie.

[Concord-PR #13](https://github.com/concord-protocol/concord/pull/13) heeft rotatiebestendig pinnen in CORD-04 gemerged. Elk kanaal heeft één volledig vervangende pinlijst op het controlevelak; items dragen het originele ondertekende zegel plus NIP-44-expansiesleutels per bericht, zodat een nieuw lid auteur en platte tekst kan verifiëren zonder een oude epoche-sleutel te ontvangen. Privélijsten kunnen verzegeld blijven aan een kanaalepoche, limieten begrenzen de lijstgrootte, en verwijderingen door de auteur halen pins weg zonder de controlevelak-keten te forken.

## NIP Deep Dive

### Zoekcapaciteit (NIP-50)

[NIP-50](/nl/topics/nip-50/), gedefinieerd in de [primaire specificatie](https://github.com/nostr-protocol/nips/blob/master/50.md), voegt een optioneel zoekfilter voor relays toe. Gewone Nostr-filters werken wanneer een client al een auteur, event-kind, identificatie of tag kent; NIP-50 adresseert discovery wanneer de invoer een menselijke query is zoals `best nostr apps`.

Het [NIP-50-wireformaat](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field) voegt een `search`-string toe aan een normaal filter binnen een `REQ`-bericht. Een request kan dat veld combineren met `kinds`, `authors`, `ids`, tagfilters en `limit`, en één REQ kan meerdere onafhankelijke filters dragen. Een ondersteunende relay zou primair tegen de `content` van het event moeten matchen, mag andere velden gebruiken wanneer het event-kind dat nuttig maakt, en zou moeten sorteren op zijn eigen relevantiescore voordat de `limit` wordt toegepast. Die volgorde verschilt van de gebruikelijke nieuwste-eerst-eventstroom.

De querystring kan de [`key:value`-extensies](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions) van de specificatie bevatten. Hij noemt `include:spam`, `domain:`, `language:`, `sentiment:` en `nsfw:`; een relay zou extensies die hij niet implementeert moeten negeren. Clients ontdekken verklaarde ondersteuning via het `supported_nips`-veld van [NIP-11](/nl/topics/nip-11/) van de relay, maar mogen het filter nog steeds elders heen sturen als ze bereid zijn niet-gerelateerde antwoorden te verwerpen.

De [NIP-50-specificatie](https://github.com/nostr-protocol/nips/blob/master/50.md) standaardiseert bewust geen tokenisatie, stemming, ranking, taaldetectie, sentimentanalyse of spamclassificatie. Twee conforme relays kunnen verschillende events en verschillende volgordes teruggeven voor dezelfde query. Dat maakt de relay een index- en rankingprovider, geen bron van waarheid. De specificatie raadt aan meerdere ondersteunende relays te bevragen, te controleren of teruggegeven events voldoen aan de use case van de client, en relays te laten vallen waarvan de resultaten een slechte precisie hebben.

Dit verschilt van exact [NIP-01-filteren](https://github.com/nostr-protocol/nips/blob/master/01.md). Een `authors`- of `#t`-filter heeft deterministische match-semantiek die een client direct kan verifiëren, terwijl een zoekmatch kan afhangen van een index en een opake score. NIP-50 behoudt de ondertekende event-envelop en het relay-transport van NIP-01, maar accepteert variatie in recall en volgorde om openvormig ophalen mogelijk te maken.

Het onderstaande event is een illustratief zoekresultaat met de [zeven NIP-01-eventvelden](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). De herhaalde hexadecimale waarden zijn placeholders en geen geldige handtekening.

```json
{
  "id": "0000000000000000000000000000000000000000000000000000000000000000",
  "pubkey": "1111111111111111111111111111111111111111111111111111111111111111",
  "created_at": 1785888000,
  "kind": 1,
  "tags": [["t", "nostr"]],
  "content": "A comparison of Nostr search relays and their indexes.",
  "sig": "22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
}
```

Huidige clients gebruiken hetzelfde filter in verschillende discovery-oppervlakken. [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) stuurt NIP-50-zoekopdrachten naar toegewijde zoekrelays, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) zoekt events via zijn relay-pool, en [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) coördineert relay-gesteunde zoekopdrachten voor longform-lezen. Hun verschillende resultaatbehandeling weerspiegelt de speelruimte die NIP-50 aan relays en clients laat.

### Highlights (NIP-84)

[NIP-84](/nl/topics/nip-84/), gedefinieerd door zijn [primaire specificatie](https://github.com/nostr-protocol/nips/blob/master/84.md), kent kind `9802` toe aan een highlight. Hij verandert een geselecteerde passage, of een verwijzing naar niet-tekstuele media, in een ondertekend event dat kan bewegen tussen lees-, sociale- en annotatie-clients.

De [`content` van het event](https://github.com/nostr-protocol/nips/blob/master/84.md#format) bevat de geselecteerde tekst en kan leeg zijn wanneer de bron audio, video of een ander niet-tekstueel medium is. Een highlight wijst naar een Nostr-bron met een `a`-tag voor een adresseerbaar event of een `e`-tag voor een gewoon event; een `r`-tag identificeert een web-URL. URL-producerende clients zouden tracking- en andere niet-nuttige queryparameters vóór publicatie moeten verwijderen, zodat cosmetische URL-varianten verwijzingen naar dezelfde bron niet fragmenteren.

Optionele [`p`-tags](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution) schrijven de bron toe aan een of meer Nostr-pubkeys. Hun vierde waarde kan een rol identificeren zoals `author` of `editor`, en een `context`-tag kan omringende tekst bewaren wanneer de selectie alleen onduidelijk zou zijn. Een quote-highlight voegt in plaats daarvan een `comment`-tag toe in plaats van een tweede kind `1`-notitie te publiceren: de `r`-tag van de bron krijgt de markering `source`, terwijl pubkeys of URL's die in het commentaar worden genoemd `mention` dragen, zodat renderers attributie kunnen onderscheiden van de reactie van de gebruiker.

De [kind `9802`-definitie](https://github.com/nostr-protocol/nips/blob/master/84.md) maakt een highlight een regulier event in plaats van een vervangbaar event. Een selectie herhalen of corrigeren creëert een nieuw ondertekend event, en het verwijderen ervan vertrouwt op de normale verwijderverzoek-flow en het retentiebeleid van de relay. De specificatie definieert geen byte-offsets, selectors of een canonieke document-snapshot, dus een client kan mogelijk een passage niet terugvinden nadat zijn webbron is gewijzigd. Publieke highlights onthullen ook leesinteresses; privé-annotatie vereist een apart versleutelings- en deelontwerp.

NIP-84 verschilt van een [NIP-23-longform-event](https://github.com/nostr-protocol/nips/blob/master/23.md), dat een heel artikel publiceert als kind `30023`; een highlight citeert of wijst in materiaal dat elders kan blijven. Hij verschilt ook van een [NIP-51-bladwijzersets](https://github.com/nostr-protocol/nips/blob/master/51.md), die een vervangbare verzameling verwijzingen opslaat. NIP-84 maakt elke selectie onafhankelijk ondertekend, toeschrijfbaar, vindbaar en bespreekbaar.

Deze illustratieve highlight bevat de [zeven NIP-01-eventvelden](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Zijn identificatie en handtekening zijn placeholders.

```json
{
  "id": "3333333333333333333333333333333333333333333333333333333333333333",
  "pubkey": "4444444444444444444444444444444444444444444444444444444444444444",
  "created_at": 1785888000,
  "kind": 9802,
  "tags": [
    ["a", "30023:6666666666666666666666666666666666666666666666666666666666666666:relay-search", "wss://relay.example"],
    ["p", "6666666666666666666666666666666666666666666666666666666666666666", "wss://relay.example", "author"],
    ["context", "Search relays are indexes whose ranking policies can differ."]
  ],
  "content": "ranking policies can differ",
  "sig": "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"
}
```

Het formaat overschrijdt al clientgrenzen. [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) heeft deze week NIP-84-rendering toegevoegd, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) rendert highlight-events in zijn longform-client, en [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) publiceert ze vanuit geselecteerde inhoud. Die implementaties dekken lezen, creëren en sociale rendering zonder dat één dienst de annotatie hoeft te bezitten.

---

Stuur een NIP-17-DM om een project of nieuwsitem te delen via het [Nostr Compass-project](https://github.com/andotherstuff/nostr-compass).
