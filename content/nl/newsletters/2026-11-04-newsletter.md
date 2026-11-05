---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

Deze week bracht [Amethyst](/nl/newsletters/2026-11-04-newsletter/#amethyst) inline napplets uit met fixes uit een [beveiligingsreview van embeds](https://github.com/vitorpamplona/amethyst/pull/4710), koppelde [Napplets](/nl/newsletters/2026-11-04-newsletter/#napplets---web-packages) de applet-identiteit aan poorten per document en maakten de nightlies van [Marmots mdk](/nl/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk) groepsberichten strikter. Daarnaast veranderden relays, wallets, signeerbibliotheken en nieuwe apps, veelal in samengevoegde broncode die nog niet is uitgebracht.

## Hoofdverhalen {#top-stories}

### Amethyst {#amethyst}

Amethyst, de Android-client, bracht [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0) uit, die napplets inline in notes draait op Android 11+ en op desktop. Fixes uit een [beveiligingsreview van embeds](https://github.com/vitorpamplona/amethyst/pull/4710) dichten een pad waarlangs elke napplet met relaytoegang ontsleutelde DM's kon lezen. Ontsleuteling vereist nu een aparte toestemming van de gebruiker en `nostr.signEvent` vereist toestemming van de signer, terwijl de Chromium-renderer op desktop nog steeds niet gesandboxed is. Een [wijziging in de versleuteling per bijlagebestand](https://github.com/vitorpamplona/amethyst/pull/4701) geeft elke bijlage van een [NIP-17](/nl/topics/nip-17/) privé direct bericht een nieuwe AES-GCM-sleutel en nonce, terwijl batches met meerdere bestanden beide hergebruikten. De upstream risicobeschrijving is gebaseerd op codeanalyse zonder gereproduceerde exploit, en al verzonden bestanden worden niet hersteld.

### Marmot Protocol (mdk) {#marmot-protocol-mdk}

mdk, Marmots op MLS gebaseerde kit voor versleutelde berichten op Nostr, publiceerde nightly-prereleases die alleen bedoeld zijn om te testen, zonder stabiele release in die lijn. In de nightly van 2 november [wachten nieuwe verzendingen achter oudere berichten in de wachtrij](https://github.com/marmot-protocol/mdk/pull/2849) binnen een groep, zodat versleutelingsgeneraties op volgorde blijven voor leden die de geschiedenis inhalen, al biedt dit geen garantie tegen verloren berichten. Een samengevoegde, standaard uitgeschakelde [reparatie voor verloren Welcomes](https://github.com/marmot-protocol/mdk/pull/2936) volgt de [Marmot-heartbeatregel](https://github.com/marmot-protocol/marmot/pull/497) en verstuurt de exact bewaarde Welcome opnieuw zodra de heartbeat van het doel activiteit toont van minstens tien minuten na de laatste publicatie van de carrier. De heartbeatfrequentie of klokachterstand kan de reparatie een uur of langer vertragen, en voor voltooiing geldt geen bovengrens. [Commando's voor het koppelen van apparaten](https://github.com/marmot-protocol/mdk/pull/2922) blijven achter de standaard uitgeschakelde feature dev-device-groups en staan uit in productie.

### Napplets - Webpakketten {#napplets---web-packages}

Napplets, de webpakketten voor gesandboxte Nostr-applets, bracht [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0), [nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0) en [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0) uit, die [de applet-identiteit binden aan een MessagePort per document](https://github.com/napplet/web/pull/302). De geverifieerde (dTag, artifactHash)-identiteit is gekoppeld aan de poort die in de hello vanuit het aangemaakte iframe wordt meegegeven, en al het NAP-verkeer loopt via die poort. Een document dat via navigatie is geladen, krijgt geen toestemmingen. Shells die nog Window-messaging gebruiken, moeten upgraden, omdat er geen compatibiliteitspad is. Latere broncode [vergrendelt het previewframe op het geverifieerde document](https://github.com/napplet/web/pull/305) met frame-src 'none'.

## Getagde releases {#tagged-releases}

### Marble {#marble}

Marble, een bètaclient gebouwd op Cosign threshold signing, kan relays als feeds lezen in [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23). Een relay die via zijn adres wordt geopend, toont eerst zijn eigen beschrijving en daarna zijn posts, nieuwste eerst. Favoriete relays worden bewaard in een kind 10012-lijst en relaygroepen in kind 30002-sets, dezelfde lijsten die Jumble gebruikt. De release vernieuwt ook de reacties, met een lade met recente reacties en de eigen custom emoji van de gebruiker.

### Sidecar {#sidecar}

Sidecar, een browserextensie voor het publiceren van notes en webhighlights, kan zijn walletback-up van relays verwijderen in [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6). Na een bevestiging vervangt het de versleutelde kopie door een lege en vraagt het relays om die te vergeten, terwijl de gekoppelde wallet behouden blijft. Er is geen garantie dat relays de back-up wissen. Sinds [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5) verwijdert Sidecar EXIF-, XMP- en IPTC-metadata uit JPEG's vóór het uploaden, en de [wijziging in de uploadvoorbereiding](https://github.com/dmnyc/sidecar/pull/572) blokkeert elke JPEG die niet kan worden opgeschoond.

### Haps {#haps}

Haps publiceert en installeert native pakketten onder Nostr-sleutels. [Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25) levert bundels voor macOS, Linux en Windows met htree-helpers die met checksums zijn vastgepind en een SHA256SUMS-bestand dat alle archieven dekt. De broncode voor 0.1.24 [schrijft geversioneerde Hashtree-referenties](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8) volgens de concept-specificatie van Hashtree. Haps 0.1.23 en eerder kunnen de nieuwe catalogi niet lezen zonder een legacy-overgangscatalogus of een bijgewerkte installer of Cargo-build.

### Cosign {#cosign}

Cosign, de threshold-signingbibliotheek achter de Marble-bèta, levert een gedeeltelijke fix voor joins in [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9): een join via een gescande uitnodiger vereist nu de bijdrage van die uitnodiger en stukken van minstens twee verschillende afzenders. Joins van telefoon naar telefoon blijven ongebonden, dus een aanvaller met twee sleutels volstaat nog steeds, en lege ontsleutelingsdelen slaan nog steeds de bewijsverificatie over. In [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8) kan een server die de ledenlijst schrijft nog steeds share points met bekende geheimen kiezen. Telefoons krijgen fixes alleen via een Marble-release.

### nostream {#nostream}

nostream, een TypeScript-relay met PostgreSQL als backend, voegt [uitgaande peersynchronisatie](https://github.com/cameri/nostream/pull/1043) toe in [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0). De worker leest per peer de scopes uit de [NIP-11](/nl/topics/nip-11/)-relayinformatie, authenticeert met [NIP-42](/nl/topics/nip-42/)-clientauthenticatie en stemt af via [NIP-77](/nl/topics/nip-77/)-negentropysynchronisatie, waarbij opgehaalde events worden gecontroleerd op ID, handtekening en scope. [Peerspecifieke limieten](https://github.com/cameri/nostream/pull/1034) gelden pas nadat een geconfigureerde peer AUTH heeft voltooid. Een bronrelease bewijst niet dat een relay deze heeft uitgerold.

### diVine {#divine}

diVine, een client voor korte loopende video's, publiceerde [stabiele Android 1.0.27](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27) met interactieve publieke videostickers; beschikbaarheid voor iOS en macOS is onbevestigd. Een samengevoegde [requery onder het venster](https://github.com/divinevideo/divine-mobile/pull/10711) draait pas nadat het eerste herstel van de geschiedenis is voltooid en leest gift wraps, [NIP-04](/nl/topics/nip-04/) verouderde versleutelde DM's en verwijderingen in pagina's van 100 berichten per relay. Deze doorloopt elke relay afzonderlijk, terwijl de bestaande history drain één cursor deelt en de oudere geschiedenis van een begrensde relay kan overslaan. De dekking is begrensd en herstelt niet de volledige geschiedenis.

### Whistle {#whistle}

Whistle, een mobiele app voor het delen van locaties in groepen en chatten, bracht [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1) uit, de eerste publieke release op Marmot-protocol v2. Bestaande groepen kunnen niet worden overgezet, dus groepen moeten opnieuw worden aangemaakt en elk lid moet updaten, terwijl npub-identiteiten behouden blijven. Scan-to-join vervangt uitnodigingscodes en -links. Een bekend probleem is dat chatberichten die offline zijn verstuurd mogelijk laat of helemaal niet aankomen, wat de release toeschrijft aan MarmotKit; het delen van locaties wordt niet beïnvloed.

## In ontwikkeling {#in-development}

### Quartz {#quartz}

Quartz, een Kotlin Multiplatform-bibliotheek voor Nostr, leverde in release 2.14.0 [het hervatten van live abonnementen na een herverbinding](https://github.com/vitorpamplona/quartz/pull/82). Elke relay hervat vanaf de nieuwste afgeleverde created_at, begrensd door de klok van het apparaat, en gift-wrap-filters reiken twee extra dagen terug om backdating op te vangen. Events met een oudere tijdstempel die een relay tijdens een storing heeft opgeslagen, kunnen nog steeds gemist worden. De samengevoegde maar nog niet uitgebrachte [count-aware negentropy-vensters](https://github.com/vitorpamplona/quartz/pull/85) vergelijken een optioneel [NIP-45](/nl/topics/nip-45/)-eventaantal met het lokale aantal en behandelen aantallen van relays als onbetrouwbaar.

### Buzz {#buzz}

Buzz voegde een wijziging samen die [verwijderingen van kind 5 en 9005 in één transactie vastlegt samen met de soft delete van het doel](https://github.com/block/buzz/pull/8944), zodat een fout niet langer kan leiden tot een geaccepteerde verwijdering terwijl het doel actief blijft. Historische half weggeschreven rijen (torn rows) worden niet hersteld. Het mobiele profiel van [NIP-RS](/nl/topics/nip-rs/), een Buzz-concept voor leesstatus over apparaten heen, is samengevoegd en [synchroniseert leesgrenzen tussen apparaten](https://github.com/block/buzz/pull/8998). Op oudere relays zonder read_state_snapshot werkt lokaal lezen nog steeds, maar stopt de synchronisatie tussen apparaten zonder terugvaloptie.

### Alby Hub {#alby-hub}

Alby Hub, een self-custodial Lightning-node die [NIP-47](/nl/topics/nip-47/) Nostr Wallet Connect-apps bedient, voegde een [fix voor databasemigratie](https://github.com/getAlby/hub/pull/2657) samen die de ID-teller van elke tabel behoudt tijdens db_migrate of een Postgres-migratie. Daarvoor kon een nieuwe app de ID van een verwijderde app hergebruiken en diens transacties en geïsoleerde saldo erven. Er is geen getagde release of uitrol gevonden die de fix bevat. Een aparte [wijziging in notificaties](https://github.com/getAlby/hub/pull/2677) isoleert fouten per app, al worden mislukte notificaties nog steeds zonder nieuwe poging verworpen.

### swift-nostr-client {#swift-nostr-client}

swift-nostr-client, een Swift 6-bibliotheek voor Nostr, voegde een brekende wijziging samen waardoor [RemoteSigner de connect-handshake uitvoert vóór het eerste commando](https://github.com/yysskk/swift-nostr/pull/287). De nieuwe instelling connectsAutomatically staat standaard op true, en bij een mislukte handshake wordt het commando niet verzonden. Omdat geheimen voor [NIP-46](/nl/topics/nip-46/) remote signing maar één keer bruikbaar zijn, moeten apps die een bunker-sessie hervatten met een opgeslagen sleutelpaar van de client deze instelling op false zetten, anders presenteert het eerste commando het al verbruikte geheim. Er is nog geen release getagd.

## Nieuwe projecten {#new-projects}

### Trikey {#trikey}

Trikey, een pre-alpha, niet-geaudite wallet waarvan de telefoonapp en de guardian communiceren via versleutelde berichten over Nostr-relays, pakt in [release 0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf) het bevriezen van de app bij het openen aan. Beide kanten houden nu een overzicht bij dat een herstart overleeft van al gelezen wrap-ID's en slaan die over vóór enige handtekeningcontrole of ontsleuteling. Verloopaanwijzingen op verzoeken en meldingen garanderen niet dat relays iets verwijderen, en de prestatiemetingen van de uitgever zijn op een laptop gedaan.

### Pacto {#pacto}

Pacto, een desktopapp voor het organiseren van gemeenschappen die legacy Marmot-groepen naast NIP-17-DM's draait, bracht de ongesigneerde [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5) uit, waarmee verzonden berichten tot één minuut na verzending bewerkt kunnen worden. De [fixes voor DM-aflevering](https://github.com/covenant-gov/pacto-app/pull/425) laten verzendingen direct mislukken als de pool geen vertrouwde relay bevat en sturen typindicatoren via vertrouwde relays. Open, niet samengevoegde pull requests zouden [squad-events](https://github.com/covenant-gov/pacto-app/pull/488) en [versleutelde squad-documenten](https://github.com/covenant-gov/pacto-app/pull/490) toevoegen.

### Mialuna {#mialuna}

Mialuna, een op media gerichte Flutter-client voor Nostr, publiceerde een [releaseaankondiging voor versie 0.19.0](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez) die verwijderverzoeken toevoegt voor de eigen stories van de gebruiker zodra die verlopen. De [changelog-commit](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886) vermeldt verwijderverzoeken aan relays en verwijdering van Blossom-media. Bij accounts met een lokale sleutel gebeurt dit automatisch, terwijl accounts met Amber of een bunker wachten tot de gebruiker Delete now kiest. De APK en het gedrag ervan op apparaten zijn niet onafhankelijk gecontroleerd. Verwijderverzoeken kunnen niet garanderen dat relays of servers de gegevens wissen.

### whereAreYou {#whereareyou}

whereAreYou, een Android-app die locaties deelt binnen kringen waar je via een QR-code of uitnodigingslink lid van wordt, versleutelt coördinaten met AES-256-GCM en verstuurt ze via publieke relays. Een [commit voor ondertekening door leden](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e) voorkomt dat houders van de kringsleutel berichten plaatsen als een ander lid, en elk apparaat moet updaten. Bij de [Base45-identiteitsback-up](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc) waarschuwt de auteur dat iedereen die de QR-code fotografeert de achtcijferige code offline zou kunnen raden, volgens zijn schatting binnen enkele tientallen minuten GPU-tijd; er is geen benchmark gepubliceerd. De bron bevat geen aanbeveling op het gebied van beveiliging.

## Protocol- en specificatiewerk {#protocol-and-spec-work}

### Buzz definieert door de eigenaar geautoriseerde credential-routes voor agents {#buzz-defines-owner-authorized-agent-credential-routes}

Buzz voegde een [NIP-FA](/nl/topics/nip-fa/)-[concept voor door de eigenaar geautoriseerde agent-credentials](https://github.com/block/buzz/pull/9015) samen, dat routes voor toekenning, assertie en intrekking definieert voor agents die via [NIP-OA](/nl/topics/nip-oa/)-eigenaarsattestatie zijn geautoriseerd. Een toekenning komt voort uit een RFC 8693-tokenuitwisseling die de sessie van de eigenaar koppelt aan een [NIP-98](/nl/topics/nip-98/) HTTP-authenticatiebewijs van de agent, en intrekking verbreekt de verbinding met de agent en voorkomt dat diens sleutel zich opnieuw inschrijft. NIP-FA is een Buzz-specificatie die alleen in de broncode is samengevoegd, zonder claim van activering in productie of interoperabiliteit.

### Post-kwantumhandtekeningen voor events krijgen exacte validatieregels {#post-quantum-event-signatures-gain-exact-validation-rules}

Het al lang lopende, openstaande voorstel voor post-kwantumhandtekeningen kreeg [exacte ML-DSA-44-validatieregels voor Nostr-events](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6). Sleutels en handtekeningen hebben vaste lengtes, verifiers controleren de handtekening over de 32 ruwe digest-bytes van het event-ID met een lege context, en er is geen terugvalalgoritme toegestaan. De voorgestelde identiteit heeft geen [NIP-19](/nl/topics/nip-19/) bech32-codering, en nieuwe handtekeningen maken [NIP-44](/nl/topics/nip-44/)-versleutelde payloads of [NIP-59](/nl/topics/nip-59/)-gift wraps niet post-kwantumveilig.

### Een voorgestelde ondertekende voorwaarde voorkomt verloren vervangingen van events {#a-proposed-signed-precondition-prevents-lost-event-replacements}

Een openstaande pull request van Buzz [stelt een projectlokale ondertekende NIP-CS-voorwaarde voor](https://github.com/block/buzz/pull/8835) voor vervangbare en adresseerbare events. Dit is geen officiële NIP. De ondertekende tag noemt het huidige head-ID of `none`, en de relay controleert die atomair onder een vergrendeling op de coördinaat. Een verouderde schrijfactie wordt geweigerd met een false OK of HTTP 409, en er wordt niets opgeslagen. Schrijfacties zonder tag werken zoals voorheen, en de tag biedt geen compare-and-swap-garantie over meerdere relays heen.

## NIP Deep Dive: NIP-31 en NIP-73 {#nip-deep-dive-nip-31-and-nip-73}

Clients komen vaak inhoud tegen die ze niet van zichzelf begrijpen. [NIP-31: Dealing with Unknown Event Kinds](/nl/topics/nip-31/) geeft een onbekend event-kind een leesbaar label, en [NIP-73: External Content IDs](/nl/topics/nip-73/) benoemt onderwerpen buiten Nostr, zoals boeken of webpagina's. De twee conventies zijn onafhankelijke, al bestaande specificaties ([NIP-31-tekst](https://github.com/nostr-protocol/nips/blob/master/31.md), [NIP-73-tekst](https://github.com/nostr-protocol/nips/blob/master/73.md)).

### NIP-31 is gemarkeerd als unrecommended {#nip-31-is-marked-unrecommended}

De huidige [NIP-31-tekst](https://github.com/nostr-protocol/nips/blob/master/31.md) opent met een waarschuwing die de NIP als `unrecommended` markeert omdat die "unnecessarily bloated" zou zijn, en de statusregel vermeldt draft, unrecommended en optional. Events die de conventie gebruiken staan al op relays, dus de werking hieronder beschrijft hoe clients ze lezen, zonder aanbeveling voor nieuwe protocollen.

### Wat een alt-tag bevat {#what-an-alt-tag-carries}

Volgens de [spec](https://github.com/nostr-protocol/nips/blob/master/31.md) voegt een auteur van een eigen kind dat niet als tekst bedoeld is een `alt`-tag toe met een korte samenvatting in platte tekst. Van clients die op kind 1 gericht zijn wordt niet verwacht dat ze andere kinds opvragen, maar gebruikers kunnen zulke events nog steeds vanuit notes aanhalen, waar een samenvatting context biedt. Een label kan geen stem uitbrengen en niet op een walletverzoek reageren. Voor rijkere interactie verwijst de spec naar [NIP-89: Recommended Application Handlers](/nl/topics/nip-89/).

Omdat `alt` een tag is, valt die onder de event-ID en handtekening uit [NIP-01](/nl/topics/nip-01/): [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md). Een geldige handtekening authenticeert een samenvatting die de auteur zelf bepaalt: ze laat zien dat de auteur het label heeft gepubliceerd, niet dat het klopt, dus misleidende samenvattingen zijn mogelijk. Tags zijn openbaar, dus een `alt` op een event met versleutelde inhoud legt de samenvatting bloot en kan onthullen wat de inhoud verbergt. Deze eigenschappen komen voort uit de envelop van [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), buiten de normatieve tekst van NIP-31. Een `alt`-tag op het hoogste niveau staat bovendien los van het `alt`-veld voor afbeeldingsbeschrijvingen binnen `imeta`, en renderers parsen ze afzonderlijk.

### Hoe twee clients alt lezen {#how-two-clients-read-alt}

In de [kaart voor onbekende events van noStrudel op commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx) wordt de eerste `alt`-tag getrimd en wordt die het hoofdlabel, met een optionele regel `Using <client>`. Een ontbrekende of lege waarde levert `Unknown event (kind ...)` op, en daarnaast verschijnen onafhankelijk maximaal drie regels inhoud. Dezelfde component zet de `client`-tag om via NIP-89-handlersjablonen en toont Open wanneer er een deelbaar adres bestaat en `Open in <client>` wanneer een geldige handlerlink wordt gevonden. Uitleg en het doorsturen naar een app zijn afzonderlijke bedieningselementen.

[UnknownEventDigest.kt van Amethyst op commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) geeft de voorkeur aan inhoud die het als proza classificeert en valt terug op `alt`. De parser trimt waarden en neemt de eerste niet-lege `alt`, dus een event waarvan de eerste `alt` leeg is, kan hier een ander label krijgen dan in noStrudel. Beide beschrijvingen geven de broncode op die commits weer, geen bevestigd releasegedrag.

### Voorbeeld: een poll met een alt-label {#example-a-poll-with-an-alt-label}

De poll van kind 1068 hieronder is opgehaald van wss://relay.damus.io, en de ID en BIP340-handtekening kloppen volgens de regels van [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Een generieke renderer kan de tweetalige `alt`-tekst tonen, terwijl een client die polls ondersteunt de tags `option` en `polltype` leest.

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### NIP-73: onderwerpen en families {#nip-73-subjects-and-families}

De [NIP-73-specificatie](https://github.com/nostr-protocol/nips/blob/master/73.md) (draft, optional, zonder unrecommended-markering) plaatst een extern onderwerp in een `i`-tag en de familie van de identifier in een `k`-tag, zodat clients één exact onderwerp of een hele familie kunnen opvragen. Een boek gebruikt `["i", "isbn:9780765382030"]` met `["k", "isbn"]`, en een webpagina gebruikt haar URL met `k` ingesteld op `web`. NIP-73 definieert geen event-kind; andere events dragen de tags.

### Normalisatie en URL-hints {#normalization-and-url-hints}

Matching hangt af van identieke strings, dus de [spec](https://github.com/nostr-protocol/nips/blob/master/73.md) legt per familie een vorm vast: URL's genormaliseerd zonder fragment, ISBN's zonder koppeltekens, geohashes in kleine letters, ISO 3166-codes in hoofdletters. Een optioneel derde array-element bevat een URL-hint voor clients zonder eigen interpretatie van de identifier. De auteur kiest die hint, en die maakt geen deel uit van de identiteit. De hint bewijst ook geen eigendom en wijst geen canonieke site aan.

### Wat een gedeelde identifier niet bewijst {#what-a-shared-identifier-does-not-prove}

Volgens [NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md) brengen gelijke identifiers gesprekken samen en stellen ze verder niets vast. Een ondertekende reactie identificeert wie de reactie schreef, maar authenticeert het boek, de site of de podcastuitgever niet en laat niet zien wie die beheert. Aliassen, editiespecifieke ISBN's en URL's die verschillend normaliseren kunnen één onderwerp over meerdere threads verdelen. Context doet ertoe: [NIP-22](/nl/topics/nip-22/): [Comment](https://github.com/nostr-protocol/nips/blob/master/22.md) gebruikt hoofdletters `I`/`K` voor de root-scope en kleine letters `i`/`k` voor de parent, en [NIP-39: External Identities in Profiles](/nl/topics/nip-39/) gebruikt `i` voor profielidentiteiten, dus niet elke `i`-tag is een NIP-73-onderwerp.

### NIP-73 in parser- en renderercode {#nip-73-in-parser-and-renderer-code}

[nip73.rs van rust-nostr op commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) parseert bekende prefixen naar een getypeerde `ExternalContentId` en zet een optionele hint om in een getypeerde URL, waarbij het derde tag-element alleen wordt uitgegeven als er een hint is. De tests behouden ISBN's met koppeltekens: de parser verwijdert de prefix en slaat de rest op zonder de normalisatie uit de spec toe te passen, dus getypeerd parsen garandeert geen canonieke strings. Chain-ID's worden gescheiden van de familie, zodat `ethereum:100:tx:<hash>` op `ethereum:tx` wordt gemapt. Die revisie heeft geen landvariant `iso3166`.

[DisplayExternalId.kt van Amethyst op commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) stuurt geohash- en hashtag-identifiers naar eigen weergaven. URL-identifiers krijgen ook een eigen weergave, terwijl andere ondersteunde typen naar een generieke scope-chip gaan. Een URL opent de eigen threadroute van de app voor die pagina. Met previews uitgeschakeld toont de normale weergave een gewone linkchip en wordt geen preview opgevraagd. Met previews ingeschakeld kan het ophalen van een ontbrekende preview contact maken met de doelsite. Door previews uit te zetten wordt dat verzoek bij normale weergave vermeden. Geen van beide bestanden stelt releasegedrag vast.

### Voorbeeld: een reactie op een webpagina {#example-a-comment-on-a-webpage}

Deze reactie van kind 1111, opgehaald van wss://nos.lol, plaatst dezelfde openbare Reddit-thread-URL in zowel het `I`/`K`-paar als het `i`/`k`-paar, met `web` als familie volgens [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) en NIP-73. De ID en handtekening zijn geldig, wat aangeeft wie de reactie schreef en niets zegt over de gelinkte pagina.

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
