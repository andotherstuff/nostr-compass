---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Bentornati su Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [Amethyst](https://github.com/vitorpamplona/amethyst) integra desktop Tor, una implementazione C di secp256k1, chiamate WebRTC per [NIP-AC](/it/topics/nip-ac/), conformità RFC 9420 MLS per [Marmot](/it/topics/marmot/) e supporto multi-wallet [NIP-47](/it/topics/nip-47/). [nstrfy](https://github.com/vcavallo/nstrfy-android) lancia notifiche push native su Nostr per Android con eventi kind `7741`. [HAMSTR](https://github.com/LibertyFarmer/hamstr) aggiunge Reticulum e porta eventi Nostr su mesh LoRa senza Internet. [Bloom](https://github.com/nostrnative/bloom) pubblica una prima release come server [Blossom](/it/topics/blossom/) e relay self-hosted in un'app desktop. [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) debutta come directory e player di radio Internet basata su Nostr. [Botburrow](https://github.com/marmot-protocol/botburrow) avvia lo sviluppo come piattaforma bot self-hosted per chat di gruppo cifrate con Marmot. [Snort](https://github.com/v0l/snort) pubblica quattro release con audit di sicurezza e un grande lavoro sulle performance, mentre [Primal Android](https://github.com/PrimalHQ/primal-android-app) ridisegna feed e app bars.

## Top Stories

### Amethyst merges desktop Tor, C secp256k1, WebRTC calls, and multi-wallet NWC

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android mantenuto da vitorpamplona, ha unito 29 PR in una sola settimana tra crittografia, networking, calling e infrastruttura wallet.

[PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381) aggiunge il supporto a Tor su desktop incorporando un daemon kmp-tor con design fail-closed. Se Tor è attivo, tutte le connessioni ai relay passano dal processo Tor integrato e l'app rifiuta di connettersi se Tor non parte. Il routing orientato alla privacy raggiunge cosi la parità tra build Android e desktop, supportato da oltre 130 unit test.

[PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374) aggiunge una implementazione personalizzata in C di secp256k1 con binding JNI per la verifica delle firme. Il risultato è un'accelerazione di circa 2-3x nella verifica delle firme Schnorr rispetto al precedente percorso puro Kotlin. Le PR collegate [#2188](https://github.com/vitorpamplona/amethyst/pull/2188), [#2195](https://github.com/vitorpamplona/amethyst/pull/2195) e [#2204](https://github.com/vitorpamplona/amethyst/pull/2204) introducono fused multiply-reduce, una struct Fe4 dedicata e intrinsics specifiche per piattaforma per migliorare ulteriormente le prestazioni su Android.

[PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202) aggiorna l'implementazione MLS in puro Kotlin per allinearla a RFC 9420, aggiungendo reuse guard, additional authenticated data, correzioni nella gestione dei commit e thread safety per l'integrazione con [Marmot](/it/topics/marmot/). La serie WebRTC da [PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203) a [PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211) introduce un sistema completo di chiamate vocali e video per [NIP-AC](/it/topics/nip-ac/), con ICE restart, cambio camera a runtime, monitoraggio della rete, riconnessione automatica e fix per le restrizioni Android 14+ sui servizi in foreground.

[PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988) aggiunge il supporto multi-wallet [NIP-47](/it/topics/nip-47/). Gli utenti possono collegare più wallet NWC allo stesso account, vedere schede saldo separate, scegliere un wallet predefinito e migrare dal vecchio modello a wallet singolo. [PR #2189](https://github.com/vitorpamplona/amethyst/pull/2189) aggiunge anche la conversione GIF-to-MP4 con uno slider di qualità.

### nstrfy launches Nostr-native push notifications for Android

[nstrfy](https://github.com/vcavallo/nstrfy-android) è stato lanciato il 13 aprile con tre release da [v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0) a [v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0). L'app è un fork di ntfy-android dove il trasporto HTTP è stato sostituito da Nostr. Invece di interrogare un server per ricevere notifiche push, nstrfy si sottoscrive a eventi kind `7741` su relay configurabili e li mostra come notifiche Android native.

Il modello di notifica supporta sia payload in chiaro sia payload cifrati con [NIP-44](/it/topics/nip-44/). Quando la cifratura è attiva, nstrfy usa [Amber](https://github.com/greenart7c3/Amber) per firmare via [NIP-55](/it/topics/nip-55/) o tramite un nsec locale. Le subscription per topic permettono allowlist per mittente con whitelist npub, l'app importa le liste relay dal profilo utente con [NIP-65](/it/topics/nip-65/) e rispetta la scadenza degli eventi di [NIP-40](/it/topics/nip-40/). La ricerca utenti usa NIP-50 e dati [Web of Trust](/it/topics/web-of-trust/) da brainstorm.world.

Il progetto companion [nstrfy.sh](https://github.com/vcavallo/nstrfy.sh) fornisce sia una CLI bash sia un client web ospitato su [nstrfy.sh](https://nstrfy.sh), con supporto al signer [NIP-07](/it/topics/nip-07/). L'app nativa è disponibile su [Zapstore](https://zapstore.dev/apps/io.nstrfy.android).

### HAMSTR adds Reticulum for Nostr over LoRa mesh

[HAMSTR](https://github.com/LibertyFarmer/hamstr), il progetto che invia eventi Nostr e Lightning zaps via radio amatoriale, ha unito [PR #10](https://github.com/LibertyFarmer/hamstr/pull/10) il 12 aprile aggiungendo [Reticulum](https://reticulum.network/) come backend di trasporto mesh. Reticulum è un protocollo mesh crittografico che funziona su LoRa, HF, VHF/UHF, link seriali e TCP/IP. Con questa aggiunta, HAMSTR può inoltrare eventi Nostr su una mesh di dispositivi RNode senza alcuna infrastruttura Internet.

I trasporti AX.25 Packet Radio e VARA HF restano disponibili, cosi gli operatori possono scegliere il collegamento radio più adatto. L'architettura zero-knowledge del server significa che il relay non vede le chiavi private, e la conformità zap di [NIP-57](/it/topics/nip-57/) fa si che i Lightning zap offline appaiano correttamente in client come Amethyst e Primal. Una guida di setup per Reticulum è inclusa in [RETICULUM.MD](https://github.com/LibertyFarmer/hamstr/blob/master/RETICULUM.MD). Nella stessa settimana, [PR #11](https://github.com/LibertyFarmer/hamstr/pull/11) ha migrato il frontend a Svelte 5 e TailwindCSS v4.

## Shipping This Week

### Bloom v0.1.0 ships self-hosted Blossom server and relay

[Bloom](https://github.com/nostrnative/bloom) ha pubblicato la sua prima release, [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0), il 9 aprile. Costruita con Tauri v2 e React 19, Bloom unisce in una sola applicazione desktop un server media completo [Blossom](/it/topics/blossom/) e un relay Nostr. Gli utenti ottengono storage file sovrano con content addressing SHA-256, supporto ai metadati file di [NIP-94](/it/topics/nip-94/) e risoluzione dello schema URI `blossom://` senza dover gestire da soli l'infrastruttura server.

### WaveFunc v0.1.0 and v0.1.1 launch Nostr internet radio

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) ha pubblicato [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0) e [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) il 13 aprile, debuttando come directory e player di internet radio basato su Nostr. Event kind personalizzati definiscono il modello dati: kind `31237` per le stazioni radio, kind `30078` per i preferiti, kind `1311` per la live chat e kind `1111` per i commenti alle stazioni. Il backend relay basato su Khatru usa SQLite e ricerca full-text Bluge con supporto a [NIP-50](/it/topics/nip-50/).

WaveFunc include un wallet Cashu [NIP-60](/it/topics/nip-60/) e supporto nutzap, con migrazione da NDK ad applesauce-core. [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) aggiunge caroselli per genere, un popover per donazioni Lightning, gestione delle stazioni per utenti autenticati e listing Zapstore. La build desktop Tauri v2 guadagna system tray, media key, autostart e deep linking.

### Snort ships v0.5.0 through v0.5.3 with security hardening and performance overhaul

[Snort](https://github.com/v0l/snort), il client web React per Nostr, ha pubblicato tre release da [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0) a [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3). La v0.5.0 è la più grande e consegna un audit di sicurezza completo con verifica reale delle firme Schnorr, protezione rafforzata di [NIP-46](/it/topics/nip-46/) contro messaggi relay falsificati, PIN encryption migliorata e rimozione della fiducia verso delegation NIP-26 non verificata. Sul fronte performance arrivano verifica WASM batch delle firme, route lazy-loaded, un loader profili riscritto e ottimizzazioni del worker relay.

La release aggiunge anche la visualizzazione delle invoice kind `7000` per DVM [NIP-90](/it/topics/nip-90/). [PR #620](https://github.com/v0l/snort/pull/620) rifà il sistema di messaggistica per ridurre la complessità del calcolo della chat list e persistere i gift wrap nel worker relay.

### Primal Android ships 3.0.21 and redesigns feed layout

[Primal Android](https://github.com/PrimalHQ/primal-android-app) ha pubblicato [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21) con fix per poll zap votes, condivisione multi-account del wallet e auto-reconnect per signer remoto e servizio wallet. Sette PR successive ridisegnano il layout principale: [PR #1008](https://github.com/PrimalHQ/primal-android-app/pull/1008) unifica la schermata principale, [PR #1010](https://github.com/PrimalHQ/primal-android-app/pull/1010) implementa nuove feed card, [PR #1009](https://github.com/PrimalHQ/primal-android-app/pull/1009) aggiunge supporto video nelle card media e [PR #1013](https://github.com/PrimalHQ/primal-android-app/pull/1013) ridisegna le app bar.

### Nostria v3.1.19 through v3.1.21 add local AI image generation

[Nostria](https://github.com/nostria-app/nostria) ha pubblicato tre release da [v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19) a [v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21) con oltre 80 commit. L'aggiunta principale è la generazione locale di immagini con Janus Pro e accelerazione WebGPU, cosi gli utenti possono creare immagini sul dispositivo senza API esterne. Le release aggiungono anche generazione cloud, chat multimodale, supporto ONNX runtime, libreria di prompt e gestione della cache.

### TubeStr v1.0.3 ships feed and studio updates

[TubeStr](https://github.com/Tubestr/tubestr-v2), app privata per la condivisione di video familiari costruita su Nostr, ha pubblicato [v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3) il 13 aprile. La release aggiunge miglioramenti a feed e studio. [PR #3](https://github.com/Tubestr/tubestr-v2/pull/3) rinnova l'onboarding e [PR #2](https://github.com/Tubestr/tubestr-v2/pull/2) corregge un errore nell'export video. L'app usa NDK e MDK per la condivisione cifrata dei media tra familiari, con integrazione [Blossom](/it/topics/blossom/) pianificata per lo storage.

## In Development

### Botburrow begins development as Marmot bot platform

[Botburrow](https://github.com/marmot-protocol/botburrow) è un nuovo progetto del team Marmot, iniziato il 3 aprile. È una piattaforma self-hosted di gestione bot dove ogni bot ha una propria identità Nostr, entra in chat di gruppo cifrate [Marmot](/it/topics/marmot/) tramite messaggi Welcome e invia e riceve messaggi end-to-end encrypted. La dashboard, costruita con Rails 8.1, comunica con un singolo daemon whitenoise-rs (`wnd`) attraverso un socket Unix.

Botburrow espone un livello consistente di scripting e operations: comandi, trigger e azioni pianificate eseguono codice Ruby personalizzato, gli script possono ispezionare profili, membership di gruppo e inviti pendenti tramite `wnd`, la dashboard include una vista live chat e ogni bot ha un proprio storage file per configurazioni, cache e output generato. Un'[immagine Docker](https://github.com/marmot-protocol/botburrow/commit/2ed012078eaab3c5b92dff16b87865c2e353bd80) con build multi-arch punta a self-hosting zero-config su Umbrel e Start9.

### Nostr Archives adds trending feeds relay and entity resolution

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api), la piattaforma di archiviazione e analytics per Nostr su [nostrarchives.com](https://nostrarchives.com), ha continuato a svilupparsi sia lato [API](https://github.com/barrydeen/nostrarchives-api) sia lato [frontend](https://github.com/barrydeen/nostrarchives-frontend). [PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118) aggiunge il filtro per intervallo temporale alla classifica client e [PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117) aggiunge contatori di engagement agli eventi di risposta. Sul frontend, [PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85) risolve entità Nostr direttamente dall'URL e [PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86) aggiunge una pagina di documentazione API.

La piattaforma gestisce quattro servizi relay: un relay di ricerca NIP-50, un relay per trending feeds, un scheduler relay per eventi futuri e un relay indicizzatore per kind 0, 3 e 10002.

### Damus fixes favorites timeline

[Damus](https://github.com/damus-io/damus), il client iOS, ha unito [PR #3708](https://github.com/damus-io/damus/pull/3708) riscrivendo `subscribe_to_favorites()` con filtraggio in-place, ricostruzione della deduplicazione e persistenza della selezione tab.

### Nostur adds private zaps and custom emoji viewing

[Nostur](https://github.com/nostur-com/nostur-ios-public), il client iOS, ha pubblicato 10 commit questa settimana aggiungendo supporto ai private zaps, visualizzazione di custom emoji, un fix per il rendering di `.webp` animati e il rilevamento del formato audio dei messaggi vocali.

### Amber ships v6.0.1 through v6.0.3 with WebDAV backup and relay reconnection fixes

[Amber](https://github.com/greenart7c3/Amber), l'app signer Android [NIP-55](/it/topics/nip-55/), ha pubblicato tre release questa settimana. [v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1) aggiunge backup WebDAV e condivisione su Google Drive, implementa exponential backoff per la riconnessione ai relay, aggiorna Quartz alla 1.08.0 e corregge la validazione eventi. [v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2) aggiunge un indice account per chi usa seed words e corregge la riconnessione quando il relay è offline all'avvio. [v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3) aggiunge un ulteriore fix per request ID vuoti nella ricezione di intent.

### Plektos v0.6.0 redesigns with Ditto themes

[Plektos](https://github.com/derekross/plektos), la piattaforma decentralizzata per meetup ed eventi costruita su [NIP-52](/it/topics/nip-52/), ha pubblicato [v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77) e [v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879). L'aggiornamento aggiunge temi di comunità in stile Ditto con upload di sfondi personalizzati, configurazione della forma avatar e un generale restyling dell'interfaccia.

### Shadow adds Nostr OS API and Cashu wallet app

[Shadow](https://github.com/justinmoon/shadow), la piattaforma runtime di app di Justin Moon, ha pubblicato oltre 30 commit in due giorni. [Commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df) aggiunge un'app wallet Cashu dentro il runtime, [commit 865c415](https://github.com/justinmoon/shadow/commit/865c415) aggiunge una demo podcast player e il runtime espone `Shadow.os.nostr` e `Shadow.os.audio` come API di sistema di primo livello.

### Lief fixes Amber login and adds Zapstore

[Lief](https://gitlab.com/chad.curtis/lief), app Nostr per comporre e inviare lettere long-form ad altri utenti Nostr, ha pubblicato la build `v2026.04.12`. L'aggiornamento corregge un problema di login con [Amber](https://github.com/greenart7c3/Amber) su Android, semplifica il flusso di nudge al signer, aggiorna nostrify e aggiunge l'integrazione Zapstore.

### Espy overhauls color picker and fixes Amber login

[Espy](https://gitlab.com/chad.curtis/espy), app social Nostr dove gli utenti condividono "momenti colore", ha pubblicato la build `v2026.04.12`. L'update rifà il color picker con un arco di saturazione curvo, corregge bug di flicker nell'anello della tonalità, aggiunge personaggi Easter egg e riduce gli asset PNG di 703KB. Corregge anche il login con Amber e aggiorna nostrify.

### Jumble adds per-feed kind filters and articles tab

[Jumble](https://github.com/CodyTseng/jumble) ha pubblicato 13 commit questa settimana aggiungendo filtri per kind per singolo feed, una tab Articles, sincronizzazione dello stato di lettura delle notifiche con opzione privacy-preserving, una modalità per nascondere gli avatar e un fix a una race condition nel cambio account.

### Primal Web ships 8 version bumps

[Primal Web](https://github.com/PrimalHQ/primal-web-app) ha pubblicato le versioni 3.0.93 fino alla 3.0.101 in una settimana con 21 commit. Il lavoro si concentra su miglioramenti alla live stream chat, fix ai boundary delle mention, paginazione dei bookmark, prevenzione dei like duplicati e correzioni al relay proxy.

## Protocol and Spec Work

### NIP Updates

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-34](/it/topics/nip-34/) (Git Stuff): Add `nostr://` clone URLs** ([PR #2312](https://github.com/nostr-protocol/nips/pull/2312)): [NIP-34](/it/topics/nip-34/) definisce come ospitare repository git su Nostr usando annunci di repository kind `30617` che elencano branch, tag, relay e pubkey dei maintainer. Questa PR aggiunge un formato `nostr://` per il clone che funziona con helper `git-remote-nostr`, cosi `git clone nostr://npub1.../relay.ngit.dev/ngit` può risolvere npub o un indirizzo NIP-05, scoprire i relay del repository e recuperare i dati del repo. Sono definiti tre pattern URL, e la PR stringe anche il formato del tag `d` per garantire URI validi.

**Open PRs and Discussions:**

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): propone un evento replaceable kind `10164` che permette ai creatori di dichiarare gateway di pagamento, modelli di prezzo e regole di subscription per contenuti a pagamento.
- **NIP-XX: Relay Self-Declaration Manifest and Retention Horizon** ([PR #2314](https://github.com/nostr-protocol/nips/pull/2314)): propone un evento replaceable kind `10100` per dichiarazioni gossipabili dei relay e un nuovo messaggio relay-to-client `HORIZON` che indica il timestamp più antico conservato.
- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): propone il kind `20411` per condividere dati di geolocalizzazione cifrati con destinatari specifici tramite [NIP-44](/it/topics/nip-44/), con supporto `ttl` per la retention.
- **[NIP-5C](/it/topics/nip-5c/) (Scrolls): WASM programs update** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): continua lo sviluppo della specifica per la pubblicazione ed esecuzione di programmi WASM su Nostr, estendendo [NIP-5A](/it/topics/nip-5a/) da siti statici a programmi interattivi.
- **[NIP-44](/it/topics/nip-44/) large payload support** ([PR #1907](https://github.com/nostr-protocol/nips/pull/1907)): propone di estendere la cifratura versionata NIP-44 oltre l'attuale limite di 65.535 byte, utile soprattutto per le risposte [NIP-46](/it/topics/nip-46/) che contengono grandi contact list kind `3`.
- **[NIP-C7](/it/topics/nip-c7/): Restrict kind 9 to chat views** ([PR #2310](https://github.com/nostr-protocol/nips/pull/2310)): richiede che i client che renderizzano una "chat view" recuperino solo eventi kind `9`, evitando la perdita di contesto quando altri tipi di contenuto finiscono nella timeline di chat.

## NIP Deep Dive: NIP-29 (Relay-based Groups)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md) definisce un modello di messaggistica di gruppo in cui è il relay a gestire membership e moderazione. I gruppi vivono su un relay specifico, identificati da una stringa casuale, e il relay applica le regole su chi può scrivere nel gruppo. È un'architettura diversa da [Marmot](/it/topics/marmot/) o dalle chat di gruppo [NIP-17](/it/topics/nip-17/): qui il relay è l'autorità e può leggere i messaggi.

Un gruppo è identificato dal formato `<host>'<group-id>`, per esempio `groups.nostr.com'abcdef`. Tutti gli eventi inviati al gruppo portano un tag `h` con l'ID del gruppo:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744675200,
  "kind": 9,
  "tags": [
    ["h", "abcdef"],
    ["previous", "a1b2c3d4", "e5f67890", "12345678"]
  ],
  "content": "Has anyone tested the new relay config?",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

Il tag `previous` funge da meccanismo di rilevamento delle manomissioni. I client includono i primi 8 caratteri hex di eventi recenti visti sullo stesso relay, e i relay rifiutano riferimenti a eventi che non possiedono. La membership è gestita da kind di moderazione nell'intervallo `9000-9020`. Un utente entra pubblicando un kind `9021` e può includere un tag `code` collegato a codici invito creati dagli admin:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "f1a2b3c4d5e6f7890123456789abcdef0123456789abcdef1234567890abcdef",
  "created_at": 1744675200,
  "kind": 9021,
  "tags": [
    ["h", "abcdef"],
    ["code", "invite-xyz-123"]
  ],
  "content": "I'd like to join the dev discussion group.",
  "sig": "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff"
}
```

Gli admin possono aggiungere utenti con ruoli, rimuoverli, modificare i metadati del gruppo e cancellare eventi. Le configurazioni vengono pubblicate come eventi addressable kind `39000` fino a `39003`. I gruppi possono essere pubblici, chiusi o aperti, e la specifica accetta molti tipi di evento nel contesto del gruppo, inclusi articoli [NIP-23](/it/topics/nip-23/) e live stream [NIP-53](/it/topics/nip-53/). Client come Flotilla e Coracle supportano già questo modello, mentre [Nostrord](https://github.com/Nostrord/nostrord) è in sviluppo. Il compromesso rispetto a [Marmot](/it/topics/marmot/) è esplicito: niente end-to-end encryption, ma molta più semplicità operativa per comunità pubbliche e spazi di discussione aperti.

## NIP Deep Dive: NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md) definisce un protocollo per computazione on-demand su Nostr. Un cliente pubblica una richiesta di lavoro, i service provider competono per eseguirla e i risultati vengono consegnati come eventi Nostr. Il protocollo riserva i kind `5000-5999` alle richieste, `6000-6999` ai risultati e `7000` al feedback di stato.

Una richiesta può usare input di tipo `url`, `event`, `job` o `text`, specificare un `bid` massimo in millisats, aggiungere parametri con tag `param` e dichiarare il formato di output con `output`:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744675200,
  "kind": 5001,
  "tags": [
    ["i", "https://example.com/article.txt", "url"],
    ["output", "text/plain"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol"],
    ["bid", "5000"],
    ["param", "lang", "en"],
    ["param", "max_tokens", "280"]
  ],
  "content": "",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Il provider pubblica poi un risultato kind `6001` che rimanda alla richiesta originale e può includere una invoice Lightning nel tag `amount`. Gli eventi kind `7000` permettono aggiornamenti come `payment-required`, `processing`, `error` e `success`, dando visibilità sullo stato dei job lunghi. Il chaining dei job consente pipeline composte, per esempio trascrizione, riassunto e traduzione in sequenza.

Per la privacy, input e parametri possono essere cifrati con [NIP-04](/it/topics/nip-04/) verso il provider selezionato. Tipi di job specifici vengono definiti in un repository separato, con richieste per generazione testo, riassunto, speech-to-text, immagini e raccomandazione contenuti. Client come [Snort](https://github.com/v0l/snort) mostrano già invoice `payment-required`, mentre noStrudel e DVMDash aiutano rispettivamente nella scoperta e nell'osservazione dei DVM.

---

Questo è tutto per questa settimana. Se state costruendo qualcosa o avete notizie da condividere, scriveteci su Nostr o passate da [nostrcompass.org](https://nostrcompass.org).
