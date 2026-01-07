---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Welkom terug bij Nostr Compass, je wekelijkse gids voor het Nostr protocol-ecosysteem.

**Deze week:** Primal Android levert [NIP-46](/nl/topics/nip-46/) remote signing en [NIP-55](/nl/topics/nip-55/) lokale signer-ondersteuning, waardoor het een volwaardige signing-hub wordt voor andere Android-apps. Het [Marmot Protocol](/nl/topics/marmot/)-team heeft bevindingen uit een beveiligingsaudit aangepakt met 18 samengevoegde PR's die [MLS](/nl/topics/mls/)-gebaseerde versleutelde berichten versterken. Citrine bereikt v1.0 en Applesauce levert v5.0 voor zijn hele bibliotheeksuite. TENEX bouwt AI-agentsupervisie op Nostr, en Jumble voegt slimme relay-pooling toe. Een NIP-55 specificatiefix verduidelijkt `nip44_encrypt` retourvelden, en een [NIP-50](/nl/topics/nip-50/) PR stelt query-expressie-uitbreidingen voor geavanceerd zoeken voor. In onze deep dive leggen we [NIP-04](/nl/topics/nip-04/) en [NIP-44](/nl/topics/nip-44/) uit: waarom de verouderde versleuteling beveiligingsfouten heeft en hoe de moderne vervanger deze oplost.

## Nieuws

**Primal Android Wordt een Volwaardige Signing Hub** - [Versie 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) voegt zowel [NIP-46](/nl/topics/nip-46/) remote signing als [NIP-55](/nl/topics/nip-55/) lokale signing toe, waardoor Primal een complete signer wordt voor andere Nostr-apps. Remote signing via NIP-46 stelt gebruikers in staat om verbinding te maken met bunker-diensten via Nostr-relays, waarbij sleutels volledig van hun apparaat worden gehouden. Lokale signing via NIP-55 stelt Primal beschikbaar als een Android content provider, zodat apps zoals Amethyst of Citrine handtekeningen kunnen aanvragen zonder ooit de privésleutel aan te raken. [Meerdere vervolgPR's](https://github.com/PrimalHQ/primal-android-app/pull/839) losten compatibiliteitsproblemen op met de NIP-55-specificatie's hex pubkey-vereiste, en verbeterden het parsen van misvormde `nostrconnect://` URI's. De release bevat ook media pre-caching voor soepeler scrollen, verbeterde thread-laadtijden en avatar pre-caching.

**Marmot Protocol Versterkt Beveiliging Na Audit** - De [Marmot Development Kit](https://github.com/marmot-protocol/mdk) (mdk), die [NIP-104](/nl/topics/nip-104/) MLS-gebaseerde end-to-end versleutelde berichten implementeert, ontving deze week uitgebreide beveiligingsfixes. Achttien samengevoegde pull requests pakten auditbevindingen aan, waaronder: [hashverificatie voor versleutelde groepsafbeeldingen](https://github.com/marmot-protocol/mdk/pull/97) om blob-vervangingsaanvallen op opslagniveau te voorkomen, [paginering voor wachtende welcomes](https://github.com/marmot-protocol/mdk/pull/110) om geheugenuitputting te voorkomen, [MLS Group ID-lekkage in foutmeldingen](https://github.com/marmot-protocol/mdk/pull/112), en [base64-coderingshandhaving](https://github.com/marmot-protocol/mdk/pull/98) voor key packages. De [Marmot-specificatie zelf werd bijgewerkt](https://github.com/marmot-protocol/marmot/pull/20) met MIP-04 v2 versiebeheer en beveiligingsverbeteringen. Actieve PR's blijven nonce-hergebruik, secret zeroization en cache pollution vectors aanpakken.

**Nostrability Volgt Relay Hint Ondersteuning** - Een nieuwe [relay hints compatibiliteitstracker](https://github.com/nostrability/nostrability/issues/270) documenteert hoe clients relay hints construeren en consumeren in het ecosysteem. De tracker onthult dat hoewel de meeste clients nu hints construeren volgens [NIP-10](/nl/topics/nip-10/) en [NIP-19](/nl/topics/nip-19/), het consumeren sterk varieert: sommige clients nemen hints op in uitgaande events maar gebruiken inkomende hints niet voor het ophalen. Zes clients verdienden de "Volledig" tier-status voor complete implementatie. De tracker is nuttig voor ontwikkelaars die interoperabiliteit controleren en voor gebruikers die zich afvragen waarom sommige clients content vinden die anderen niet kunnen vinden.

**Nostria 2.0 Levert Cross-Platform Feature Overhaul** - De [Nostria](https://nostria.app) client [bracht versie 2.0 uit](https://njump.me/nevent1qqs9z4l8z82zphszjlmrjkr8whpvupnlaxc7xk5gfg9syzj0thygtzgpz4mhxue69uhhyetvv9ujuerpd46hxtnfduhszxthwden5te0wfjkccte9enrw73wd9hsz9nhwden5te0wfjkccte9ec8y6tdv9kzumn9wsq3gamnwvaz7tmjv4kxz7fwv3sk6atn9e5k7qgkwaehxw309aex2mrp0yhxgctdw4eju6t09uq32amnwvaz7tmwdaejumr0dshsz9mhwden5te0wfjkccte9ec82c30989ksmfnv9kzumn9wshsqgzxsnsv7pfqqd7rw4fvr0jnkpqmwzfqq3znlc4pqunagxrkl84u66y7fq9) op 30 december met significante toevoegingen op iOS (TestFlight), Android (Play Store), Web en Windows. De release voegt native muziekondersteuning toe met afspeellijst-creatie, track-uploads, zap-gebaseerde artiestenbetalingen en een WinAmp-stijl speler met werkende equalizer. Live streaming krijgt Game API-integratie die rijke metadata toont tijdens gameplay-streams. Een nieuwe Samenvatting-functie genereert uur-, dag- of weekoverzichten als gecomprimeerde tijdlijnweergaven. De Ontdek-sectie biedt samengestelde lijsten voor het vinden van content en profielen. Mediapublicatie wordt vereenvoudigd met automatische korte-vorm berichtgeneratie voor cross-client vindbaarheid. Remote signer-verbindingen werken nu via QR-code scannen zonder handmatige configuratie. Profielontdekking pakt een veelvoorkomend Nostr-probleem aan: wanneer gebruikers tussen relays verhuizen zonder hun metadata mee te nemen, lokaliseert Nostria hun profiel en herpubliceert het naar hun huidige relays. Premium-abonnees krijgen YouTube-kanaalintegratie, privé Memo's, analytics-dashboards en automatische volglijst-backups met samenvoeg-/herstel-opties.

## NIP Updates

Recente wijzigingen aan de [NIPs repository](https://github.com/nostr-protocol/nips):

**Samengevoegd:**
- **[NIP-55](/nl/topics/nip-55/)** - Het retourveld voor de `nip44_encrypt` methode is gecorrigeerd ([#2184](https://github.com/nostr-protocol/nips/pull/2184)). Android signers moeten nu de versleutelde payload retourneren in het `signature` veld (overeenkomend met `nip44_decrypt`) in plaats van een apart veld. Dit brengt de spec in lijn met bestaande implementaties in Amber en Primal.

**Open PR's:**
- **[NIP-50](/nl/topics/nip-50/)** - Query Expression Extensions ([#2182](https://github.com/nostr-protocol/nips/pull/2182)) stelt voor om NIP-50 zoeken uit te breiden met gestructureerde query-expressies. De PR voegt operatoren toe zoals `kind:1`, `author:npub1...`, en booleaanse combinaties (`AND`, `OR`, `NOT`), waardoor preciezere zoekopdrachten mogelijk worden naast eenvoudige tekstmatching. Dit zou clients in staat stellen geavanceerde zoekinterfaces te bouwen met behoud van achterwaartse compatibiliteit met basis zoekstrings.

## NIP Deep Dive: NIP-04 en NIP-44

Deze week behandelen we Nostr's versleutelingsstandaarden: de verouderde NIP-04 die je nog steeds zult tegenkomen, en zijn moderne vervanger NIP-44 die kritieke beveiligingsfouten oplost.

### [NIP-04](/nl/topics/nip-04/): Versleutelde Directe Berichten (Verouderd)

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md) was Nostr's eerste poging tot versleutelde berichten, gebruikmakend van kind 4 events. Hoewel eenvoudig te implementeren, heeft het bekende beveiligingszwakheden en is het afgeschreven ten gunste van NIP-44.

**Hoe het werkt:** NIP-04 gebruikt ECDH (Elliptic Curve Diffie-Hellman) om een gedeeld geheim af te leiden tussen verzender en ontvanger, en versleutelt vervolgens met AES-256-CBC.

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

De versleutelingsstroom:
1. Bereken gedeeld punt: `shared = ECDH(sender_privkey, recipient_pubkey)`
2. Leid sleutel af: `key = SHA256(shared_x_coordinate)`
3. Genereer willekeurige 16-byte IV
4. Versleutel: `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. Formatteer content: `base64(ciphertext)?iv=base64(iv)`

**Beveiligingsproblemen:**

- **Geen authenticatie:** AES-CBC biedt vertrouwelijkheid maar geen integriteit. Een aanvaller die een relay controleert zou ciphertext-bits kunnen wijzigen, wat voorspelbare wijzigingen in plaintext veroorzaakt (bit-flipping aanvallen).
- **IV in het zicht:** De initialisatievector wordt naast ciphertext verzonden, en CBC-modus met voorspelbare IV's maakt chosen-plaintext aanvallen mogelijk.
- **Geen padding-validatie:** Implementaties variëren in hoe ze PKCS#7 padding afhandelen, wat mogelijk padding oracle-aanvallen mogelijk maakt.
- **Metadata-blootstelling:** De verzender-pubkey, ontvanger-pubkey en timestamp zijn allemaal zichtbaar voor relays.
- **Sleutelhergebruik:** Hetzelfde gedeelde geheim wordt voor altijd gebruikt voor alle berichten tussen twee partijen.

**Waarom het nog bestaat:** Veel oudere clients en relays ondersteunen alleen NIP-04. Je zult het tegenkomen bij interactie met legacy-systemen. Signers zoals Amber en apps zoals Primal implementeren nog steeds `nip04_encrypt`/`nip04_decrypt` voor achterwaartse compatibiliteit.

### [NIP-44](/nl/topics/nip-44/): Versiebeheerde Versleuteling

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) is de moderne versleutelingsstandaard, ontworpen om de bekende fouten van NIP-04 op te lossen. Een Cure53-beveiligingsaudit van NIP-44-implementaties identificeerde 10 problemen (waaronder timing-aanvallen en forward secrecy-zorgen) die werden aangepakt voordat de spec werd gefinaliseerd. Het gebruikt ChaCha20-Poly1305 met correcte sleutelafleiding en geauthenticeerde versleuteling.

**Belangrijkste verbeteringen ten opzichte van NIP-04:**

| Aspect           | NIP-04                     | NIP-44                  |
|:-----------------|:---------------------------|:------------------------|
| Cipher           | AES-256-CBC                | XChaCha20-Poly1305      |
| Authenticatie    | Geen                       | Poly1305 MAC            |
| Sleutelafleiding | SHA256(shared_x)           | HKDF met salt           |
| Nonce            | 16-byte IV, hergebruikt patroon | 24-byte willekeurige nonce |
| Padding          | PKCS#7 (lekt lengte)       | Opgevuld tot macht van 2 |
| Versiebeheer     | Geen                       | Versie-byte prefix      |

**Versleutelingsstroom:**

1. **Conversation key:** Leid een stabiele sleutel af voor elk verzender-ontvanger paar:
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **Message keys:** Voor elk bericht, genereer een willekeurige 32-byte nonce en leid versleuteling/authenticatie-sleutels af:
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **Pad plaintext:** Vul aan tot de volgende macht van 2 (minimum 32 bytes) om berichtlengte te verbergen:
   ```
   padded = [length_u16_be] + [plaintext] + [zeros to next power of 2]
   ```

4. **Versleutel en authenticeer:**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **Formatteer payload:**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**Versie-byte:** De eerste byte (`0x02`) geeft de versleutelingsversie aan. Dit maakt toekomstige upgrades mogelijk zonder bestaande berichten te breken. Versie `0x01` was een eerdere draft die nooit breed werd uitgerold.

**Ontsleuteling:**

1. Decodeer base64, controleer of versie-byte `0x02` is
2. Extraheer nonce (bytes 1-32), ciphertext en MAC (laatste 32 bytes)
3. Leid conversation key af met de privésleutel van de ontvanger en de publieke sleutel van de verzender
4. Leid message keys af van conversation key en nonce
5. Verifieer MAC voordat je ontsleutelt (weiger als ongeldig)
6. Ontsleutel ciphertext, extraheer lengteprefix, retourneer onopgevulde plaintext

**Beveiligingseigenschappen:**

- **Geauthenticeerde versleuteling:** Poly1305 MAC zorgt ervoor dat elke manipulatie wordt gedetecteerd voordat er wordt ontsleuteld
- **Forward secrecy (gedeeltelijk):** Elk bericht gebruikt een unieke nonce, dus het compromitteren van één bericht onthult anderen niet. Het compromitteren van een privésleutel onthult echter nog steeds alle vorige berichten (geen ratcheting).
- **Lengte verbergen:** Power-of-2 padding verbergt exacte berichtlengte
- **Timing-aanval weerstand:** Constant-time vergelijking voor MAC-verificatie

**Gebruik in de praktijk:** NIP-44 is de versleutelingslaag voor:
- [NIP-17](/nl/topics/nip-17/) privé directe berichten (binnen gift wrap)
- [NIP-46](/nl/topics/nip-46/) remote signer-communicatie
- [NIP-59](/nl/topics/nip-59/) seal-versleuteling
- [Marmot Protocol](/nl/topics/nip-104/) groepsberichten, waarbij NIP-44 MLS-versleutelde content wrapt met een sleutel afgeleid van het MLS exporter secret
- Elke applicatie die veilige punt-naar-punt versleuteling nodig heeft

**Migratieadvies:** Nieuwe applicaties zouden exclusief NIP-44 moeten gebruiken. Voor achterwaartse compatibiliteit, controleer of de client van een contact NIP-44 ondersteunt (via [NIP-89](/nl/topics/nip-89/) app-metadata of relay-ondersteuning) voordat je terugvalt op NIP-04. Bij het ontvangen van berichten, probeer eerst NIP-44 ontsleuteling, val dan terug naar NIP-04 voor legacy-content.

## Releases

**Primal Android v2.6.18** - [Volledige release](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) voegt [NIP-46](/nl/topics/nip-46/) remote signing en [NIP-55](/nl/topics/nip-55/) lokale signing toe, waardoor Primal een signing-hub wordt voor andere Android-apps. Prestatieverbeteringen omvatten media pre-caching, avatar pre-caching en snellere thread-laadtijden. Bugfixes pakken zelf-vermeldingen in bio's, mediagalerij-crashes en stream-titel fallbacks aan. Op iOS gebruikt Primal achtergrond-audioafspeling om de app actief te houden voor het ontvangen van NIP-46 signing-verzoeken; gebruikers kunnen het geluid wijzigen of volledig dempen in instellingen.

**Mostro v0.15.6** - De nieuwste release van de [NIP-69](/nl/topics/nip-69/) P2P Bitcoin-handelsbot [](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6) voltooit de implementatie van het ontwikkelingsfonds met Phase 4 audit-events. Dev-feebetalingen worden nu gevolgd via kind 38383 Nostr-events die na elke succesvolle betaling worden gepubliceerd, wat verificatie en analytics door derden mogelijk maakt. Bedragberekeningen werden gecorrigeerd voor koper-/verkoperberichten, en premium-logica werd afgestemd op de lnp2pbot-referentie-implementatie.

**Aegis v0.3.5** - De cross-platform signer [voegt donkere modus toe](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5), verbeterde app-icoon weergave en schonere UI-layouts. Bugfixes pakken iOS iCloud Private Relay-conflicten en event-parsingproblemen aan. De release verbetert ook hoe event JSON wordt doorgegeven aan de Rust signing-functie.

**Citrine v1.0.0** - De Android relay-app [bereikt 1.0](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0). Citrine laat je een persoonlijke Nostr-relay direct op je Android-apparaat draaien, nuttig voor lokale caching, backup of als NIP-55 companion. Deze release voegt een crash report handler toe, verbetert database query-efficiëntie en werkt vertalingen bij via Crowdin.

**Applesauce v5.0.0** - hzrd149's TypeScript-bibliotheeksuite [levert een major versie](https://github.com/hzrd149/applesauce/releases) met breaking changes gericht op correctheid en eenvoud. Het core-pakket [verifieert nu event-handtekeningen standaard](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0) en hernoemt coördinaat-methodes naar duidelijkere "address" terminologie (`parseCoordinate` → `parseReplaceableAddress`). Het relay-pakket [verlaagt standaard retries van 10 naar 3](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0) en negeert standaard onbereikbare relays, plus voegt `createUnifiedEventLoader` toe voor eenvoudiger event-ophalen. Het wallet-pakket krijgt [NIP-87](/nl/topics/nip-87/) [Cashu mint discovery](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0). Directe `nostr-tools` dependencies werden verwijderd uit pakketten, wat bundlegrootte en versieconflicten vermindert.

## Noemenswaardige code- en documentatiewijzigingen

*Dit zijn open pull requests en werk in een vroeg stadium, perfect voor het krijgen van feedback voordat ze worden samengevoegd. Als iets je aandacht trekt, overweeg dan te reviewen of commentaar te geven!*

### Damus (iOS)

Een reeks PR's verbetert de longform artikel-ervaring. [Reading UX-verbeteringen](https://github.com/damus-io/damus/pull/3496) voegen een voortgangsbalk toe, geschatte leestijd, sepia-modus, aanpasbare regelhoogte en focusmodus die navigatie verbergt tijdens scrollen. [Afbeeldingsfixes](https://github.com/damus-io/damus/pull/3489) zorgen ervoor dat afbeeldingen in markdown-content worden weergegeven met correcte aspectratio's door standalone afbeeldingen voor te verwerken als blokniveau-elementen. [Longform preview cards](https://github.com/damus-io/damus/pull/3497) vervangen inline `@naddr1...` tekst door rijke preview-kaarten die artikeltitel en metadata tonen. Een nieuwe [relay integration test suite](https://github.com/damus-io/damus/pull/3508) voegt 137 netwerkgerelateerde tests toe inclusief [NIP-01](/nl/topics/nip-01/) protocolverificatie en gedrag onder verslechterde netwerkomstandigheden (3G-simulatie).

### Bitchat (Versleutelde Berichten)

Beveiligingsversterking in de iOS Nostr+Cashu messenger. [Noise protocol DH secret clearing](https://github.com/permissionlesstech/bitchat/pull/928) repareert zes locaties waar gedeelde geheimen niet werden gewist na Diffie-Hellman sleutelovereenkomst, wat forward secrecy-garanties herstelt. [Thread safety voor read receipt queues](https://github.com/permissionlesstech/bitchat/pull/929) voegt barrier-synchronisatie toe om race conditions in NostrTransport te voorkomen. [Message deduplicator-optimalisatie](https://github.com/permissionlesstech/bitchat/pull/920) verbetert prestaties bij hoge berichtvolumes, en [hex string parsing hardening](https://github.com/permissionlesstech/bitchat/pull/919) voorkomt crashes van misvormde input.

### Frostr (Threshold Signing)

Het [FROST](/nl/topics/frost/)-gebaseerde threshold signing protocol [voegde QR-code weergave toe](https://github.com/FROSTR-ORG/igloo-desktop/pull/62) voor groeps-credentials en share-credentials tijdens onboarding en in de signer-interface. Dit maakt eenvoudigere setup mogelijk bij het distribueren van sleutel-shares over meerdere apparaten, waarbij gebruikers credentials kunnen scannen in plaats van lange strings handmatig te kopiëren.

### Marmot mdk (Bibliotheek)

Naast de hierboven genoemde beveiligingsfixes, pakken actieve PR's resterende auditbevindingen aan: [Secret<T> type voor zeroization](https://github.com/marmot-protocol/mdk/pull/109) introduceert een wrapper-type dat automatisch gevoelige data wist bij drop, [messages query paginering](https://github.com/marmot-protocol/mdk/pull/111) voorkomt geheugenuitputting bij het laden van chatgeschiedenis, en [versleutelde opslag](https://github.com/marmot-protocol/mdk/pull/102) voegt at-rest versleuteling toe voor de SQLite-database die groepsstaat en berichten opslaat.

### Amethyst (Android)

Een drukke week van stabiliteitsfixes in de Android-client. [Coulante JSON-parsing](https://github.com/vitorpamplona/amethyst/commit/2c42796) voorkomt crashes van misvormde events door Kotlin Serialization coulanter te maken. Event-validatie [controleert nu kind-veldgrootte](https://github.com/vitorpamplona/amethyst/commit/40f9622) voordat verwerking plaatsvindt om exceptions van te grote waarden te vermijden. De trust score UI kreeg een kleiner icoon om visuele interferentie te verminderen, en [verbeterde foutlogging](https://github.com/vitorpamplona/amethyst/commit/69c53ac) helpt bij het diagnosticeren van relay-verbindingsproblemen. Vertaalupdates arriveerden via Crowdin, en meerdere SonarQube-waarschuwingen werden aangepakt.

### TENEX (AI Agents)

Het Nostr-native AI agent-framework zag 81 commits deze week die autonome mogelijkheden uitbouwen. Nieuw [agent supervision systeem](https://github.com/tenex-chat/tenex/pull/48) implementeert gedragsheuristieken om agent-acties te monitoren en in te grijpen wanneer nodig. [Delegatie-transparantie](https://github.com/tenex-chat/tenex/commit/b244c10) voegt gebruikersinterventie-logging toe aan delegatie-transcripten, zodat gebruikers kunnen auditen wat agents namens hen deden. De [LLM provider registry](https://github.com/tenex-chat/tenex/pull/47) werd gemodulariseerd voor eenvoudigere integratie van verschillende AI-backends. Cross-project conversatie-ondersteuning laat agents context behouden over meerdere Nostr-gebaseerde projecten.

### Jumble (Web Client)

De relay-gerichte webclient voegde meerdere gebruikerservaringverbeteringen toe. [Smart relay pool](https://github.com/CodyTseng/jumble/commit/695f2fe) beheert intelligent verbindingen op basis van gebruikspatronen. [Live feed toggle](https://github.com/CodyTseng/jumble/commit/917fcd9) laat gebruikers schakelen tussen real-time streaming en handmatige verversing. [Auto-show new notes](https://github.com/CodyTseng/jumble/commit/d1b3a8c) aan de bovenkant toont verse content zonder pagina-herlading te vereisen. [Persistent cache](https://github.com/CodyTseng/jumble/commit/fd9f41c) voor volg-feed en notificaties verbetert laadtijden bij terugkerende bezoeken. Gebruikers kunnen nu [standaard relays wijzigen](https://github.com/CodyTseng/jumble/commit/53a67d8) via instellingen.

---

Dat was het voor deze week. Bouw je iets? Heb je nieuws te delen? Wil je dat we je project behandelen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Neem contact op via NIP-17 DM</a> of vind ons op Nostr.
