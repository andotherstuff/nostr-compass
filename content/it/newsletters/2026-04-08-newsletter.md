---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [Amethyst](https://github.com/vitorpamplona/amethyst) distribuisce la [v1.08.0](#amethyst-distribuisce-arti-tor-e-integra-mls-e-marmot-in-puro-kotlin) con integrazione Arti Tor e una UI Shorts ridisegnata, mentre integra implementazioni in puro Kotlin di [MLS](/it/topics/mls/) e [Marmot](/it/topics/marmot/) nella sua libreria [Quartz](/it/topics/quartz/). [Nostur](https://github.com/nostur-com/nostur-ios-public) distribuisce la [v1.27.0](#nostur-v1270-aggiunge-registrazione-video-e-risposte-private) con registrazione video, profili GIF animati e risposte private. [Shosho](https://github.com/r0d8lsh0p/shosho-releases) lancia la [v0.15.0](#shosho-v0150-lancia-shows-e-un-carousel-video-verticale) con Shows (informazioni personalizzate sul live stream collegate a OBS) e un carousel video verticale in stile TikTok. [Nymchat](https://github.com/Spl0itable/NYM) [torna da Marmot e distribuisce chat di gruppo NIP-17 potenziate](#nymchat-abbandona-marmot-e-distribuisce-chat-di-gruppo-nip-17-potenziate) con chiavi ephemeral a rotazione. [Nostr VPN](https://github.com/mmalmi/nostr-vpn) distribuisce [supporto exit node e packaging Umbrel](#nostr-vpn-distribuisce-supporto-exit-node-e-packaging-umbrel) attraverso sei rilasci. [Amber](https://github.com/greenart7c3/Amber) sale alla [v6.0.0-pre1](#amber-v600-pre1-aggiunge-chiavi-di-firma-nip-46-per-connessione) con chiavi di firma [NIP-46](/it/topics/nip-46/) per connessione e aggiornamenti in-app via Zapstore. [Notedeck](https://github.com/damus-io/notedeck) raggiunge la [v0.10.0-beta](#notedeck-v0100-beta-distribuisce-lauto-aggiornamento-via-zapstore) con auto-aggiornamento APK via Zapstore, e [NIP-58](/it/topics/nip-58/) (Badges) riceve una [migrazione di kind](#aggiornamenti-nip). Due approfondimenti NIP coprono [NIP-17](/it/topics/nip-17/) (Private Direct Messages) e [NIP-46](/it/topics/nip-46/) (Nostr Remote Signing).

## Notizie Principali

### Amethyst distribuisce Arti Tor e integra MLS e Marmot in puro Kotlin

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android mantenuto da vitorpamplona, ha distribuito quattro rilasci dalla [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3) alla [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0) e ha integrato un ampio blocco di lavoro non ancora rilasciato nella sua libreria [Quartz](/it/topics/quartz/) (il modulo Nostr condiviso Kotlin Multiplatform). Il rilascio di punta è la v1.08.0 "Arti Tor", che sposta la connettività Tor dell'app dalla libreria Tor basata su C a [Arti](https://gitlab.torproject.org/tpo/core/arti), l'implementazione Rust del Tor Project. La migrazione affronta i crash casuali che si verificavano con i precedenti binding C di Tor. Arti è il sostituto a lungo termine del Tor Project per la codebase C, riscritto da zero in Rust per memory safety e async I/O.

Il rilascio v1.07.3 ha ridisegnato la UI Shorts, sostituendo il design paginato con feed edge-to-edge per immagini, short e video lunghi. Lo stesso rilascio ha migrato i badge al kind `10008` e i bookmark al kind `10003`, allineandosi alla migrazione di kind [NIP-58](/it/topics/nip-58/) [unita questa settimana](#aggiornamenti-nip). La v1.07.4 ha corretto un problema nella gestione dei secret di Nostr Wallet Connect, e la v1.07.5 ha corretto un crash durante l'upload di immagini.

Sul branch main, ma non ancora in un rilascio taggato, il team ha scritto un'implementazione completa in Kotlin sia di [MLS](/it/topics/mls/) sia del protocollo [Marmot](/it/topics/marmot/), eliminando la necessità di binding a librerie native C/Rust. La [PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147) aggiunge il layer centrale di messaggistica di gruppo Marmot MLS, la [PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149) aggiunge la UI della chat di gruppo, la [PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146) aggiunge i processor dei messaggi in ingresso e in uscita con un subscription manager, la [PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141) aggiunge la persistenza dello stato dei gruppi MLS e la gestione della rotazione dei KeyPackage, la [PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150) aggiunge una suite di test MLS completa con una firma di GroupInfo migliorata, e la [PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158) aggiunge il tracciamento dello stato di pubblicazione dei KeyPackage. La [PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166) aggiunge un'implementazione secp256k1 in puro Kotlin per le operazioni crittografiche Nostr, sostituendo la dipendenza dalla libreria C nativa. Combinata con l'implementazione Kotlin di MLS, [Quartz](/it/topics/quartz/) può eseguire firma Nostr e messaggistica di gruppo Marmot senza alcun binding nativo, aprendo la strada ai target Kotlin Multiplatform inclusi quelli iOS.

Il team sta anche costruendo il supporto a [NIP-AC](/en/topics/nip-ac/) (P2P Voice and Video Calls): la [PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143) aggiunge una suite di test completa per la call state machine di NIP-AC, e la [PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164) impedisce che offerte di chiamata stale vengano riattivate dopo il riavvio dell'app.

### Nostur v1.27.0 aggiunge registrazione video e risposte private

[Nostur](https://github.com/nostur-com/nostur-ios-public), il client Nostr per iOS, ha distribuito la [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0) il 2 aprile. Il rilascio aggiunge la registrazione video in-app con trim prima dell'upload, così gli utenti possono registrare clip brevi, tagliarle alla lunghezza desiderata e pubblicarle senza uscire dal client. Il supporto alle GIF animate si estende alle foto profilo e banner, con l'aggiunta anche del rendering WebP animato. Una nuova integrazione con Shortcuts permette agli utenti di inviare post Nostr dalle automazioni Apple Shortcuts. Il rilascio aggiunge anche le risposte private e corregge problemi di compatibilità DM che influivano sulla consegna dei messaggi tra Nostur e altri client.

### Shosho v0.15.0 lancia Shows e un carousel video verticale

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), l'app di live streaming Nostr, ha distribuito la [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0) e la [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1) il 7 aprile. La funzione principale è Shows: gli streamer possono preparare informazioni personalizzate sul proprio show prima di andare live e collegare lo show a OBS o a qualsiasi encoder esterno. Questo separa i metadati del "cosa sto trasmettendo" dall'atto di andare in diretta, così gli streamer possono preparare titoli, descrizioni e prodotti prima di iniziare la trasmissione. Lo stesso rilascio aggiunge un carousel video verticale in stile TikTok per scorrere live, clip e replay in un feed a schermo intero, e Quick Add per pubblicare clip video e aggiungere prodotti direttamente dalla pagina profilo. La v0.15.1 corregge un bug per cui la tastiera nascondeva il campo di input della chat del live stream.

## Rilasci di Questa Settimana

### Notedeck v0.10.0-beta distribuisce l'auto-aggiornamento via Zapstore

[Notedeck](https://github.com/damus-io/notedeck), il client desktop e mobile del team Damus, ha distribuito [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1) e [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2) come prerelease di test per l'auto-aggiornamento APK. La [PR #1417](https://github.com/damus-io/notedeck/pull/1417) aggiunge l'auto-aggiornamento APK via updater Nostr/Zapstore su Android, costruendo sul [lavoro di discovery degli aggiornamenti nativo Nostr dalla Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr). Il flusso di aggiornamento scopre i nuovi rilasci tramite event Nostr pubblicati sui relay, poi scarica l'APK da dove lo sviluppatore lo ospita (GitHub releases, Blossom CDN o altre sorgenti), verifica l'hash SHA-256 rispetto all'event Nostr firmato e lo installa. La [PR #1438](https://github.com/damus-io/notedeck/pull/1438) corregge un bug della welcome screen in cui i pulsanti Login e CreateAccount tornavano subito indietro, e la [PR #1424](https://github.com/damus-io/notedeck/pull/1424) corregge l'overflow del testo nella vista sessione di Agentium AI.

### Amber v6.0.0-pre1 aggiunge chiavi di firma NIP-46 per connessione

[Amber](https://github.com/greenart7c3/Amber), l'app signer [NIP-55](/it/topics/nip-55/) (Android Signer Application), ha distribuito la [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1) il 4 aprile. Il cambiamento più importante è l'introduzione di chiavi di firma per connessione per il protocollo bunker [NIP-46](/it/topics/nip-46/) (Nostr Remote Signing). Invece di usare una singola keypair per tutte le connessioni bunker, Amber ora genera una chiave distinta per ogni client connesso. Se una connessione client viene compromessa, l'attaccante non può impersonare il signer verso gli altri client.

La [PR #377](https://github.com/greenart7c3/Amber/pull/377) aggiunge il controllo e l'installazione degli aggiornamenti in-app via Zapstore, unendosi a [Notedeck](#notedeck-v0100-beta-distribuisce-lauto-aggiornamento-via-zapstore) nell'adozione della distribuzione app nativa Nostr. La [PR #375](https://github.com/greenart7c3/Amber/pull/375) gestisce con grazia i fallimenti di AndroidKeyStore mostrando un avviso agli utenti invece di far crashare l'app, e la [PR #371](https://github.com/greenart7c3/Amber/pull/371) aggiunge cleanup del database con limiti di dimensione e troncamento dei contenuti per prevenire una crescita di storage senza limiti. La prerelease include anche la whitelist relay auth [NIP-42](/it/topics/nip-42/) e il login tramite frase mnemonica di recovery dal [ciclo v5.0.x trattato la settimana scorsa](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504).

### Nostria distribuisce un'app mobile nativa

[Nostria](https://github.com/nostria-app/nostria), il client Nostr cross-platform mantenuto da SondreB, ha rilasciato un'app mobile nativa per Android con otto rilasci dalla [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11) alla [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18). La capacità nuova più importante è il supporto nativo ai signer locali come [Amber](https://github.com/greenart7c3/Amber) e Aegis. Sono disponibili anche gli [installer desktop](https://www.nostria.app/download) per Linux, macOS e Windows. La [PR #610](https://github.com/nostria-app/nostria/pull/610) riduce la pressione sulla memoria del feed con limiti runtime adattivi e cleanup delle preview URL. La v3.1.14 corregge l'integrazione con Brainstorm, un provider [Web of Trust](/it/topics/web-of-trust/). La v3.1.15 si concentra sui miglioramenti musicali. La nuova app Android è disponibile su [Zapstore](https://zapstore.dev/apps/app.nostria).

### diVine 1.0.8 distribuisce upload resumable e DM

[diVine](https://github.com/divinevideo/divine-mobile), il client per video brevi, ha distribuito la [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8) con 87 PR unite. Gli upload resumable permettono ai creator di riprendere upload interrotti chunk per chunk invece di ricominciare da zero su una connessione instabile. Il rilascio aggiunge impostazioni di qualità video e bitrate, doppio tap per mettere like e miglioramenti ai DM. La [PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722) aggiunge un plugin fotocamera macOS per la cattura video desktop, e la [PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820) migra il sistema di notifiche a un'architettura BLoC con enrichment e grouping. Il team ha anche sostituito sticker e artwork di categoria generati da AI con SVG OpenMoji ([PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844), [PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)).

### Manent v1.3.0 aggiunge blur per note sensibili e auth NIP-42

[Manent](https://github.com/dtonon/manent), l'app per note private cifrate e storage file, ha distribuito la [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0) il 2 aprile. Gli utenti possono ora segnare le note come sensibili per sfocarle nella list view, mantenendo nascosto il contenuto privato durante lo scorrimento casuale. Il rilascio aggiunge anche il supporto [NIP-42](/it/topics/nip-42/) (Authentication of Clients to Relays), permettendo a Manent di autenticarsi verso relay che lo richiedono prima di accettare event. Manent archivia tutti i dati cifrati sui relay Nostr usando la keypair dell'utente, quindi il supporto NIP-42 amplia l'insieme di relay che può usare per lo storage.

### Wisp da v0.17.0 a v0.17.3 aggiunge zap ai live stream e backup wallet

[Wisp](https://github.com/barrydeen/wisp), il client Nostr Android, ha distribuito sei rilasci dalla [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta) alla [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta) con 44 PR unite. La v0.17.0 aggiunge prompt di sicurezza per il backup del wallet e miglioramenti alla UX degli zap. La [v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta) aggiunge la visibilità della chat del live stream tra piattaforme e la funzionalità zap per i live stream. La [PR #423](https://github.com/barrydeen/wisp/pull/423) aggiunge la ricerca automatica dei profili, un'animazione di successo per gli zap e miglioramenti allo stato utente. La [PR #426](https://github.com/barrydeen/wisp/pull/426) corregge un crash out-of-memory in `computeId` per event con grandi liste di tag. I rilasci v0.16.x avevano aggiunto autocompletamento degli shortcode emoji, miglioramenti alla UI della chat di gruppo e filtraggio degli utenti bloccati in tutti i percorsi delle notifiche.

### Mostro distribuisce deep link, tassi di cambio da Nostr e una correzione ai pagamenti duplicati

[Mostro](https://github.com/MostroP2P/mostro), l'exchange Bitcoin peer-to-peer costruito su Nostr, ha registrato aggiornamenti questa settimana sia nel daemon server sia nel client mobile. Sul lato server, la [PR #692](https://github.com/MostroP2P/mostro/pull/692) impedisce che scritture stale degli ordini causino pagamenti duplicati, un bug che poteva portare a pagare due volte un venditore per lo stesso trade. La [PR #693](https://github.com/MostroP2P/mostro/pull/693) usa aggiornamenti mirati per le scritture di dev_fee invece di riscrivere l'intero ordine.

[Mostro Mobile](https://github.com/MostroP2P/mobile), il client Flutter, ha distribuito la [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3) il 3 aprile. Il rilascio gestisce deep link provenienti da diverse istanze Mostro, così gli utenti possono toccare link che instradano verso il server exchange corretto. La [PR #498](https://github.com/MostroP2P/mobile/pull/498) rileva DM di admin e dispute nella pipeline di notifiche in background, e l'app ora recupera i tassi di cambio da Nostr con fallback HTTP/cache. La [PR #560](https://github.com/MostroP2P/mobile/pull/560) corregge un bug bloccante nella connessione ai relay che impediva all'app di raggiungerli in certe condizioni di rete.

### Unfiltered v1.0.12 aggiunge hashtag e commenti

[Unfiltered](https://github.com/dmcarrington/unfiltered), un client Nostr focalizzato su contenuti image-forward, ha distribuito la [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12). La [PR #69](https://github.com/dmcarrington/unfiltered/pull/69) aggiunge il supporto agli hashtag e la [PR #72](https://github.com/dmcarrington/unfiltered/pull/72) aggiunge la possibilità di scrivere e visualizzare commenti sui post. La [PR #71](https://github.com/dmcarrington/unfiltered/pull/71) corregge problemi di navigazione con più immagini per post.

### Primal Android distribuisce condivisione wallet multi-account e auto-reconnect del remote signer

[Primal](https://github.com/PrimalHQ/primal-android-app), il client Nostr Android, ha distribuito un rilascio il 7 aprile. L'aggiornamento aggiunge la condivisione wallet multi-account e un menu overflow con cancellazione del wallet nei Dev Tools. Il remote signer ora si riconnette automaticamente quando la connessione cade, e il servizio wallet ha ottenuto una propria logica di auto-reconnect. Le correzioni includono i voti zap dei sondaggi che non appaiono più come Top Zaps, la prevenzione del crash con opzioni di sondaggio vuote, l'occultamento del saldo wallet quando non esiste alcun wallet, e il mapping dei tipi WalletException in codici errore nelle risposte NWC.

### Titan v0.1.0 lancia un browser nativo nsite:// con registrazione dei nomi su Bitcoin

[Titan](https://github.com/btcjt/titan), un browser desktop nativo per il web di Nostr, ha distribuito la [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0) il 7 aprile. Titan risolve gli URL `nsite://` cercando nomi leggibili registrati su Bitcoin, interrogando i relay Nostr per gli event di contenuto del sito e renderizzando pagine recuperate da server [Blossom](/it/topics/blossom/). Il risultato è un'esperienza di navigazione web senza DNS, senza certificati TLS e senza hosting provider. I nomi vengono registrati tramite una [web interface](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register) legata a transazioni Bitcoin. Il rilascio iniziale è distribuito come `.dmg` per macOS (ARM, con supporto Rosetta 2 per Intel) e include il supporto all'ambiente di sviluppo Nix.

### Bikel v1.5.0 distribuisce un native foreground service per telefoni de-Googled

[Bikel](https://github.com/Mnpezz/bikel), un tracker ciclistico decentralizzato che trasforma le corse in dati di infrastruttura pubblica usando Nostr, ha distribuito la [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0) il 4 aprile. Il rilascio migra da Expo TaskManager dipendente da GMS a un foreground service nativo personalizzato, garantendo un tracking affidabile in background su LineageOS, GrapheneOS e altre varianti Android de-Googled. Il Bikel Bot ha ottenuto un'architettura dual-pocket con raccolta eCash autonoma via Cashu nutzaps. La v1.4.3 e la v1.4.2 correggono la sincronizzazione del tracking in background per ambienti Android non standard, e l'app aggiunge toggle per i punti mappa dei portabici OSM.

### Sprout aggiunge supporto a NIP-01, NIP-23 e NIP-33

[Sprout](https://github.com/block/sprout), una piattaforma di comunicazione di Block con relay Nostr integrato, ha distribuito la [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7) il 6 aprile. Questa settimana il team ha aggiunto supporto agli articoli kind `30023` di [NIP-23](/en/topics/nip-23/) (Long-form Content), agli event replaceable parametrizzati di [NIP-33](/en/topics/nip-33/) con sostituzione indicizzata dal tag `d`, e alle text note kind `1` e follow list kind `3` di [NIP-01](/it/topics/nip-01/)/[NIP-02](/en/topics/nip-02/). Il rilascio aggiunge anche un sistema di temi IDE adattivi con 54 temi, rifiniture UX per workflow e cronologia delle esecuzioni degli agenti, e cleanup della sidebar membri.

### mesh-llm v0.56.0 distribuisce un protocollo di configurazione distribuito

[mesh-llm](https://github.com/michaelneale/mesh-llm), un sistema distribuito di inferenza LLM che usa keypair Nostr per l'identità dei nodi, ha distribuito la [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0) il 7 aprile. Il rilascio aggiunge un protocollo di configurazione distribuito con semantiche di ownership, quantizzazione asimmetrica della cache KV (chiavi Q8_0 con valori Q4) per ridurre l'uso di memoria, storage nel keychain del sistema operativo per i keystore di identità, streaming chat fluido con coda dei messaggi, e correzioni al layout fullscreen e alla suddivisione della cache KV con flash attention.

### Nostr VPN distribuisce supporto exit node e packaging Umbrel

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), una VPN peer-to-peer che usa relay Nostr per la segnalazione e WireGuard per i tunnel cifrati, ha distribuito sei rilasci dalla [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0) alla [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6) questa settimana. Il ciclo v0.3.x aggiunge il supporto agli exit node su Windows e macOS, permettendo ai peer di instradare il traffico Internet attraverso altri nodi della rete. La propagazione di invite e alias ora si sincronizza via Nostr, così gli utenti possono condividere l'accesso alla rete senza coordinamento out-of-band. I rilasci aggiungono packaging Umbrel per deployment self-hosted, NAT punch-through usando endpoint pubblici ricordati, cleanup automatico degli exit node stale e una specifica di protocollo pubblicata. Il progetto ha anche stabilizzato la gestione delle route su macOS con default route auto-riparanti e underlay repair, e ha aggiunto un build Android via Tauri. Sono disponibili build per macOS (Apple Silicon e Intel), Linux (AppImage e .deb), Windows e Android.

### Nymchat abbandona Marmot e distribuisce chat di gruppo NIP-17 potenziate

[Nymchat](https://github.com/Spl0itable/NYM), il client chat capace di MLS, ha distribuito 14 rilasci dalla [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261) alla [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274). Il cambiamento più significativo è una svolta di protocollo: la [v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261) aveva aggiunto chat di gruppo Marmot MLS, ma la [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268) è tornata a [NIP-17](/it/topics/nip-17/) perché il supporto multi-device di Marmot non è ancora completo, e questo causava problemi nella sincronizzazione dello stato delle chat di gruppo tra dispositivi. La v3.58.271 introduce chat di gruppo NIP-17 potenziate con chiavi ephemeral a rotazione per tutti i messaggi, progettate per prevenire timing attack e correlation attack. La settimana ha portato anche un sistema amici con controllo granulare delle impostazioni ([v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)), sincronizzazione dei messaggi delle chat di gruppo MLS nelle impostazioni cifrate dell'app, e diverse correzioni alla connettività relay.

### nak v0.19.5 aggiunge Blossom multi-server e pubblicazione outbox

[nak](https://github.com/fiatjaf/nak), il toolkit Nostr a riga di comando di fiatjaf, ha distribuito la [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5). Il comando `blossom` ora accetta più flag `--server` per caricare su diversi server [Blossom](/it/topics/blossom/) in una sola chiamata. Un nuovo comando `key` espande chiavi parziali aggiungendo zeri a sinistra. Il comando `event` guadagna un flag `--outbox` per pubblicare event attraverso il modello outbox, e `fetch` ora termina con un codice errore quando non viene restituito alcun event.

## In Sviluppo

### White Noise aggiunge anteprime thumbhash e il bridge per la registrazione push

[White Noise](https://github.com/marmot-protocol/whitenoise), il messenger privato costruito sul protocollo [Marmot](/it/topics/marmot/), ha unito cinque PR. La [PR #549](https://github.com/marmot-protocol/whitenoise/pull/549) sostituisce le anteprime immagine blurhash con thumbhash, un algoritmo più recente che produce immagini placeholder più nitide con una dimensione payload minore (tipicamente sotto i 30 byte contro i ~50-100 byte di blurhash) preservando il rapporto d'aspetto e la distribuzione dei colori dell'immagine originale. Blurhash viene mantenuto come fallback per i contenuti più vecchi. La [PR #548](https://github.com/marmot-protocol/whitenoise/pull/548) aggiorna whitenoise-rs e aggiunge il bridge di registrazione push [MIP-05](/it/topics/mip-05/), collegando al client il [lavoro sulla specifica delle push notification della settimana scorsa](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications). La [PR #493](https://github.com/marmot-protocol/whitenoise/pull/493) aggiunge la paginazione basata su cursore per i messaggi chat, sostituendo la strategia di caricamento precedente con un approccio guidato dallo scroll.

### Route96 aggiunge configurazione dinamica delle label e cleanup zero-egress

[Route96](https://github.com/v0l/route96), il media server [Blossom](/it/topics/blossom/) di v0l, ha unito tre PR. La [PR #80](https://github.com/v0l/route96/pull/80) aggiunge la configurazione dinamica del modello di label tramite admin API, permettendo agli operatori di sostituire i modelli di classificazione dei contenuti senza riavviare il server. La [PR #82](https://github.com/v0l/route96/pull/82) aggiunge i campi di configurazione delle label alla admin UI. La [PR #79](https://github.com/v0l/route96/pull/79) aggiunge una policy di cleanup dei file zero-egress che rimuove automaticamente i file mai scaricati, mantenendo bassi i costi di storage per gli operatori.

### Snort distribuisce hardening di sicurezza e invoice di pagamento DVM

[Snort](https://github.com/v0l/snort), il client web, ha distribuito due rilasci questa settimana insieme a un audit di sicurezza completo. Le correzioni includono verifica delle firme Schnorr, protezione [NIP-46](/it/topics/nip-46/) contro la falsificazione dei messaggi relay (impedendo ad attaccanti di iniettare richieste di firma attraverso relay compromessi), miglioramenti alla cifratura del PIN e rimozione della fiducia nella delega NIP-26. I miglioramenti prestazionali arrivano dalla verifica Schnorr batch in WASM, route lazy-loaded, traduzioni precompilate ed eliminazione della doppia verifica per event. La [PR #618](https://github.com/v0l/snort/pull/618) aggiunge la visualizzazione dell'invoice kind `7000` con pagamento richiesto di [NIP-90](/en/topics/nip-90/) (Data Vending Machine), così quando un DVM risponde con un requisito di pagamento, Snort renderizza direttamente la Lightning invoice nel feed.

### Damus migliora la compattazione LMDB

[Damus](https://github.com/damus-io/damus), il client iOS, ha unito la [PR #3719](https://github.com/damus-io/damus/pull/3719) che aggiunge la compattazione automatica di LMDB su base pianificata, impedendo al database locale di crescere senza limiti nel tempo. La [PR #3663](https://github.com/damus-io/damus/pull/3663) migliora la BlurOverlayView in modo che sembri protettiva invece che rotta.

### Captain's Log aggiunge indicizzazione dei tag e sync delle note

[Captain's Log](https://github.com/nodetec/captains-log) (Comet), lo strumento di scrittura long-form nativo Nostr di Nodetec, ha unito quattro PR questa settimana. La [PR #156](https://github.com/nodetec/captains-log/pull/156) aggiunge indicizzazione dei tag e supporto alla sincronizzazione tra note, la [PR #157](https://github.com/nodetec/captains-log/pull/157) rifattorizza il sync delle note e la gestione dei tag, e la [PR #159](https://github.com/nodetec/captains-log/pull/159) corregge la sincronizzazione delle note cestinate in modo che gli elementi eliminati restino eliminati su tutti i dispositivi.

### Relatr v0.2.x ridisegna il sistema plugin con un marketplace di validator nativo Nostr

[Relatr](https://github.com/ContextVM/relatr), un motore [Web of Trust](/it/topics/web-of-trust/) che calcola ranking di fiducia dalla distanza nel grafo sociale e da validator configurabili, ha distribuito la famiglia v0.2.x con un redesign completo del sistema plugin. I validator sono ora scritti in Elo, un linguaggio di espressioni funzionali portabile forkato per supportare capacità orchestrate dall'host in più passi (query Nostr, lookup del grafo sociale, risoluzione NIP-05). I plugin vengono pubblicati come event Nostr kind `765`, rendendo la distribuzione nativa alla rete relay. Un nuovo [plugin marketplace](https://relatr.net) permette agli operatori di scoprire, installare e pesare i validator dal browser, con una CLI (`relo`) per authoring e pubblicazione locale. L'architettura è sandboxed: i plugin possono invocare solo le capacità che l'host fornisce esplicitamente, quindi un validator malevolo non può uscire dal proprio scope definito. Le istanze Relatr ora possono essere gestite dal sito web, con visibilità completa su quali plugin compongono l'algoritmo di scoring e sui pesi individuali di ciascuno.

### Shopstr migliora navigazione mobile e controllo accessi

[Shopstr](https://github.com/shopstr-eng/shopstr), il marketplace nativo Nostr per comprare e vendere con Bitcoin, ha spinto 158 commit questa settimana nella sua app principale e nel progetto companion [Milk Market](https://github.com/shopstr-eng/milk-market). Le correzioni includono miglioramenti al layout mobile delle community, comportamento di chiusura del menu durante la navigazione e auto-chiusura dei dropdown. Le route protette non possono più essere raggiunte via URL diretto senza login, e la logica di matching degli slug ora gestisce correttamente più corrispondenze esatte.

### Pollerama aggiunge notifiche, ricerca film e nuova rating UI

[Pollerama](https://github.com/formstr-hq/nostr-polls), un'app di polling, survey e rating sociale costruita su Nostr, ha aggiunto notifiche dei thread, una funzione di ricerca film e un overhaul della rating UI. Il rilascio corregge anche problemi di caricamento del feed e aggiorna le versioni delle dipendenze.

### Purser costruisce un payment daemon nativo Nostr con cifratura Marmot

[Purser](https://github.com/EthnTuttle/purser), un payment daemon nativo Nostr progettato come sostituto di Zaprite, ha unito nove PR questa settimana che costruiscono la sua architettura centrale. Il progetto usa MLS di [Marmot](/it/topics/marmot/) tramite MDK per la messaggistica cifrata merchant-customer, con Strike e Square come payment provider. Questa settimana sono arrivati caricamento di configurazione e catalogo, validazione dello schema dei messaggi, il layer di comunicazione MDK, le implementazioni dei provider Strike e Square, un motore di polling, anti-spam rate limiting, persistenza dei pagamenti pending e la pipeline di elaborazione degli ordini. Tutti i 99 test ora esercitano operazioni MLS reali di mdk-core dopo che il team ha rimosso il mock MLS in favore della cifratura reale in modalità locale.

### Vector rifattorizza gli allegati DM e aggiunge la modifica del profilo

[Vector](https://github.com/VectorPrivacy/Vector), il messenger Nostr focalizzato sulla privacy costruito con Tauri, ha unito la [PR #55](https://github.com/VectorPrivacy/Vector/pull/55) che rifattorizza il frontend. La decrittazione e il salvataggio degli allegati DM sono stati spostati nella libreria vector-core, e l'app ora supporta la modifica del profilo. Il flag di cancellazione dell'upload è collegato correttamente attraverso TauriSendCallback, e i callback inutilizzati per l'anteprima degli allegati sono stati ripuliti.

## Lavoro su Protocollo e Specifiche

### Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti:**

- **[NIP-58](/it/topics/nip-58/) (Badges): i Profile Badges passano al kind 10008, i Badge Sets al kind 30008** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Migra i Profile Badges dal kind `30008` al kind `10008` (un event replaceable, uno per pubkey) e introduce il kind `30008` per i Badge Sets. In precedenza i Profile Badges usavano lo stesso kind (`30008`) delle definizioni dei badge, rendendoli event replaceable parametrizzati indicizzati da un tag `d`. Il nuovo kind `10008` è un semplice event replaceable: uno per pubkey, nessun tag `d` necessario. I client interrogano un singolo event replaceable per utente invece di scandire event replaceable parametrizzati. Amethyst v1.07.3 distribuisce già questa migrazione.

- **[NIP-34](/it/topics/nip-34/) (Git Stuff): aggiungere follow list relative a git** ([PR #2130](https://github.com/nostr-protocol/nips/pull/2130)): Aggiunge convenzioni di follow list per il tracciamento di repository e issue NIP-34. Gli utenti pubblicano follow set kind `30000` con tag `d` come `git-repos` o `git-issues` contenenti riferimenti tag `a` ai repository (kind `30617`) che vogliono seguire. I client possono sottoscrivere questi follow set per mostrare l'attività dei repository nel feed di un utente, in modo simile a come le contact list kind `3` funzionano per le pubkey.

**PR aperte e discussioni:**

- **NIP-AC: P2P Voice and Video Calls over WebRTC** ([PR #2301](https://github.com/nostr-protocol/nips/pull/2301)): Estende il NIP-100 originale (implementato da 0xChat) con tre cambiamenti: migrazione alla cifratura [NIP-44](/it/topics/nip-44/) avvolta in gift wrap [NIP-59](/it/topics/nip-59/) per eliminare i metadata leak, un workflow WebRTC specificato per setup di chiamate vocali e video (offer, answer, ICE candidates), e un modello di mesh group call in cui ogni peer stabilisce una connessione WebRTC diretta con tutti gli altri peer. La specifica non è backwards-compatible con NIP-100. Amethyst ci sta già lavorando, con una suite di test per la call state machine ([PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)) e la gestione delle call offer stale ([PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)) arrivate questa settimana.

- **[NIP-340](/en/topics/nip-340/) (FROST Quorum)** ([PR #2299](https://github.com/nostr-protocol/nips/pull/2299)): Propone convenzioni per la threshold signing [FROST](/it/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) su Nostr. FROST permette a un gruppo di signer di controllare collettivamente un'identità Nostr dove qualsiasi insieme t-of-n di membri può firmare event senza ricostruire la chiave privata completa. Il NIP definisce come coordinare i round di firma, distribuire key share e pubblicare event firmati in threshold, costruendo sul lavoro del signer Igloo dal [progetto FROSTR](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11).

- **[NIP-5D](/en/topics/nip-5d/) (Nostr Web Applets)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Definisce un protocollo `postMessage` per applicazioni web sandboxed ("napplets") eseguite in iframe che comunicano con un'applicazione host ("shell"). La shell fornisce alla napplet firma Nostr, accesso relay e contesto utente tramite una structured message API, mentre la sandbox iframe impedisce l'accesso diretto alle chiavi. Questo estende il modello di hosting di siti web statici di [NIP-5A](/en/topics/nip-5a/) verso applicazioni interattive in grado di leggere e scrivere event Nostr. Il NIP è in sviluppo attivo con un'implementazione runtime funzionante.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls)** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Rinominato dalla precedente proposta NIP-A5. Definisce convenzioni per pubblicare e scoprire programmi WebAssembly su Nostr. I binari WASM vengono archiviati come event Nostr, e i client possono scaricarli ed eseguirli in un runtime sandboxed. Una [demo app](https://nprogram.netlify.app/) mostra scrolls in esecuzione nel browser, con programmi di esempio pubblicati come event Nostr che qualsiasi client può recuperare ed eseguire.

- **[NIP-85](/it/topics/nip-85/) (Trusted Assertions): chiarimenti** ([PR #2304](https://github.com/nostr-protocol/nips/pull/2304)): Stringe il linguaggio della specifica intorno a chiavi multiple e relay multipli per provider di servizi, chiarendo come i client dovrebbero gestire assertion provenienti da provider che operano attraverso più pubkey o endpoint relay.

- **[NIP-24](/it/topics/nip-24/) (Extra Metadata Fields): `published_at` per event replaceable** ([PR #2300](https://github.com/nostr-protocol/nips/pull/2300)): Generalizza il tag `published_at` da [NIP-23](/en/topics/nip-23/) (Long-form Content) a tutti gli event replaceable e addressable. Il tag è solo display-only: se `published_at` è uguale a `created_at`, i client mostrano l'event come "created" in quel momento; se differiscono (perché l'event è stato aggiornato), i client possono mostrare "updated" invece. Questo permette ai profili kind `0` di mostrare date "joined at" e agli altri event replaceable di preservare il timestamp di pubblicazione originale attraverso gli aggiornamenti. Una proposta complementare [NIP-51](/it/topics/nip-51/) ([PR #2302](https://github.com/nostr-protocol/nips/pull/2302)) aggiunge lo stesso tag agli event di lista.

- **[NIP-59](/it/topics/nip-59/) (Gift Wrap): kind di gift wrap ephemeral** ([PR #2245](https://github.com/nostr-protocol/nips/pull/2245)): Aggiunge il kind `21059` come controparte ephemeral del gift wrap esistente kind `1059`. Gli event ephemeral (kind `20000`-`29999`) seguono la semantica di [NIP-01](/it/topics/nip-01/): i relay non sono tenuti a memorizzarli e possono scartarli dopo la consegna. Questo permette alle applicazioni di inviare messaggi gift-wrapped che scompaiono dai relay dopo la consegna, riducendo i requisiti di storage per la messaggistica ad alto volume mantenendo lo stesso modello di cifratura a tre layer dei normali DM [NIP-17](/it/topics/nip-17/).

### OpenSats annuncia la sedicesima ondata di grant Nostr

[OpenSats](https://opensats.org) ha annunciato la sua [sedicesima ondata di grant Nostr](https://opensats.org/blog/sixteenth-wave-of-nostr-grants) l'8 aprile, finanziando quattro grant alla prima assegnazione e un rinnovo. [Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp) riceve fondi per permettere al contributor Robert Nagy di costruire un'app desktop standalone sopra i moduli [Quartz](/it/topics/quartz/) e Commons, portando il set di funzionalità del client Android a interfacce guidate dal mouse con connessioni relay persistenti. [Nostr Mail](https://github.com/nogringo/nostr-mail) riceve fondi per costruire un sistema email completo su Nostr usando event kind `1301` avvolti in gift wrap [NIP-59](/it/topics/nip-59/), con un client Flutter e server bridge SMTP per compatibilità con Gmail/Outlook. [Nostrord](https://github.com/Nostrord/nostrord) riceve fondi per un client di gruppo Kotlin Multiplatform basato su relay [NIP-29](/en/topics/nip-29/) con messaggistica di gruppo, moderazione e thread in stile Discord. [Nurunuru](https://github.com/tami1A84/null--nostr) riceve fondi per costruire una versione iOS nativa del client Nostr orientato al pubblico giapponese modellata sull'interfaccia familiare di LINE, con login biometrico basato su passkey per l'onboarding. HAMSTR ha ricevuto un rinnovo del grant (finanziato la prima volta nell'[undicesima ondata](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)).

## NIP Deep Dive: NIP-17 (Private Direct Messages)

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) definisce lo standard attuale per i messaggi diretti privati su Nostr. Sostituisce il vecchio schema [NIP-04](/it/topics/nip-04/) (Encrypted Direct Messages), che perdeva metadati (mittente, destinatario e timestamp erano tutti visibili sui relay) e usava una costruzione crittografica più debole. NIP-17 combina [NIP-44](/it/topics/nip-44/) (Encrypted Payloads) per la cifratura con [NIP-59](/it/topics/nip-59/) (Gift Wrap) per la protezione dei metadati, creando un sistema a tre layer in cui i relay non possono vedere chi sta parlando con chi.

Il protocollo usa tre event kind annidati l'uno dentro l'altro. Il layer più interno è il messaggio vero e proprio, un event kind `14` non firmato:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

L'event kind `14` è deliberatamente non firmato (`sig` vuoto). La specifica descrive questo aspetto come una forma di deniability, ma nella pratica la protezione è limitata. Il seal kind `13` che avvolge il rumor è firmato con la chiave reale del mittente. Un destinatario può mostrare il seal firmato a una terza parte, provando che il mittente ha comunicato con lui, anche senza rivelare il contenuto del messaggio. Con prove a conoscenza zero, un destinatario può persino dimostrare il contenuto esatto del messaggio senza rivelare la propria chiave privata. Il rumor non firmato è come una lettera non firmata in una busta firmata: la firma sulla busta collega il mittente al contenuto. La vera deniability richiederebbe autenticazione simmetrica (come gli HMAC di Signal), incompatibile con il modello relay decentralizzato di Nostr dove i messaggi devono essere self-authenticating. I veri punti di forza di NIP-17 sono la privacy dei metadati e la segretezza del contenuto, non la deniability.

Questo messaggio non firmato viene avvolto in un seal kind `13`, firmato dal mittente effettivo e cifrato con [NIP-44](/it/topics/nip-44/) per il destinatario:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

Il seal non ha tag, quindi anche se venisse decrittato non rivelerebbe il destinatario. Il seal è firmato con la chiave reale del mittente, il che permette al destinatario di autenticare il messaggio controllando che il `pubkey` del seal corrisponda al `pubkey` del kind `14` interno.

Il seal viene poi avvolto in un gift wrap kind `1059`, firmato con una chiave casuale usa-e-getta e indirizzato al destinatario:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

Il `pubkey` del gift wrap è una chiave casuale generata solo per questo messaggio, e il `created_at` è randomizzato fino a due giorni nel passato. Questo è il layer più esterno che i relay vedono davvero: un messaggio da una pubkey sconosciuta indirizzato al destinatario, con un timestamp che non riflette quando il messaggio è stato effettivamente inviato. Il timestamp randomizzato protegge dall'analisi retrospettiva degli event archiviati, ma un avversario collegato attivamente ai relay può comunque osservare quando il gift wrap è apparso per la prima volta, quindi questa difesa è limitata agli osservatori passivi che interrogano i dati del relay in seguito. Poiché la pubkey è casuale e il timestamp è fittizio, i relay non possono determinare il mittente reale. Per leggere il messaggio, il destinatario decripta il gift wrap usando la propria chiave e la pubkey casuale, trova il seal all'interno, decripta il seal usando la propria chiave e la pubkey del mittente ricavata dal seal, e trova all'interno il messaggio kind `14`.

NIP-17 non fornisce forward secrecy. Tutti i messaggi sono cifrati usando la keypair Nostr statica (tramite la derivazione delle chiavi di NIP-44 dalle chiavi del mittente e del destinatario). Se una chiave privata viene compromessa, ogni messaggio passato e futuro cifrato verso quella chiave può essere decrittato. È un tradeoff deliberato: poiché la cifratura dipende solo dall'nsec, un utente che fa il backup del proprio nsec può recuperare l'intera cronologia dei messaggi da qualsiasi relay che conservi ancora i gift wrap. Protocolli come MLS (usato da [Marmot](/it/topics/marmot/)) forniscono forward secrecy attraverso la rotazione del materiale di chiave, ma al costo di richiedere sincronizzazione dello stato e rendere impossibile il recupero storico dei messaggi dopo la rotazione delle chiavi.

NIP-17 definisce anche il kind `15` per i messaggi file cifrati, che aggiunge i tag `file-type`, `encryption-algorithm`, `decryption-key` e `decryption-nonce` così il destinatario può decrittare un file allegato cifrato con AES-GCM prima dell'upload a un server Blossom. Il kind `10050` viene usato per pubblicare la relay list DM preferita dell'utente, così i mittenti sanno dove consegnare i gift wrap. L'insieme di tag `pubkey` + `p` in un messaggio definisce una chat room; aggiungere o rimuovere un partecipante crea una nuova stanza con cronologia pulita.

Le implementazioni coprono la maggior parte dei client principali. [nospeak](https://github.com/psic4t/nospeak) usa NIP-17 per tutta la messaggistica uno-a-uno. [Flotilla](https://gitea.coracle.social/coracle/flotilla) usa NIP-17 per i suoi DM con proof-of-work. [Amethyst](https://github.com/vitorpamplona/amethyst), [Primal](https://github.com/PrimalHQ/primal-android-app), [Nostur](https://github.com/nostur-com/nostur-ios-public), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel) e [Coracle](https://github.com/coracle-social/coracle) implementano tutti NIP-17 come protocollo DM principale. La specifica supporta anche i messaggi a scomparsa impostando un tag `expiration` nel gift wrap.

## NIP Deep Dive: NIP-46 (Nostr Remote Signing)

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) definisce un protocollo per separare la chiave privata dell'utente dall'applicazione client. Invece di incollare un nsec in una web app, l'utente esegue un remote signer (chiamato anche "bunker") che custodisce la chiave privata e risponde alle richieste di firma via relay Nostr. Il client non vede mai la chiave privata. Questo riduce la superficie d'attacco: un client compromesso può richiedere firme ma non può estrarre la chiave stessa.

Il protocollo usa il kind `24133` sia per le richieste sia per le risposte, cifrate con [NIP-44](/it/topics/nip-44/) (Encrypted Payloads). Un client genera una `client-keypair` usa-e-getta per la sessione e comunica con il remote signer attraverso messaggi cifrati NIP-44 taggati con le reciproche pubkey. Ecco una richiesta di firma da un client a un remote signer:

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

Il `content` cifrato contiene una struttura in stile JSON-RPC:

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

Il remote signer decripta la richiesta, la presenta all'utente per l'approvazione (o la approva automaticamente in base ai permessi configurati), firma l'event con la chiave privata dell'utente e restituisce l'event firmato in una risposta:

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Le connessioni possono essere avviate da entrambi i lati. Un remote signer fornisce un URL `bunker://` contenente la sua pubkey e le informazioni relay. Un client fornisce un URL `nostrconnect://` con la propria pubkey client, i relay e un secret per la verifica della connessione. Il parametro `secret` previene il connection spoofing: solo la parte che ha ricevuto l'URL fuori banda può completare l'handshake.

Sono definiti otto metodi: `connect` per stabilire la sessione, `sign_event` per firmare event, `get_public_key` per ottenere la pubkey dell'utente, `ping` per keepalive, `nip04_encrypt`/`nip04_decrypt` per la cifratura legacy, `nip44_encrypt`/`nip44_decrypt` per la cifratura corrente, e `switch_relays` per la gestione dei relay. La migrazione relay è gestita dal remote signer, che può spostare nel tempo la connessione verso nuovi relay senza rompere la sessione.

I client richiedono capacità specifiche al momento della connessione attraverso un sistema di permessi. Una stringa di permessi come `nip44_encrypt,sign_event:1,sign_event:14` richiede accesso alla cifratura NIP-44 e accesso alla firma per i soli event kind `1` e kind `14`. Il remote signer può accettare, rifiutare o modificare questi permessi. Questo significa che un client web per leggere e pubblicare note potrebbe ricevere solo il permesso `sign_event:1`, mentre un client DM potrebbe ricevere anche i permessi `sign_event:14` e `nip44_encrypt`.

[Amber](https://github.com/greenart7c3/Amber) implementa NIP-46 su Android, e la sua [v6.0.0-pre1](#amber-v600-pre1-aggiunge-chiavi-di-firma-nip-46-per-connessione) di questa settimana aggiunge chiavi di firma per connessione per isolare i client tra loro. [nsec.app](https://github.com/nicktee/nsecapp) (precedentemente Nostr Connect) fornisce un bunker web-based. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) include `BunkerSigner` per i client JavaScript, e [la PR #530 della settimana scorsa](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing) ha aggiunto `skipSwitchRelays` per la gestione manuale dei relay. Il protocollo supporta anche auth challenge: quando un remote signer richiede autenticazione aggiuntiva (password, biometria o token hardware), risponde con un `auth_url` che il client apre in un browser perché l'utente completi il flusso.

---

Questo è tutto per questa settimana. Stai costruendo qualcosa o hai notizie da condividere? Scrivici in DM su Nostr o vieni a trovarci su [nostrcompass.org](https://nostrcompass.org).
