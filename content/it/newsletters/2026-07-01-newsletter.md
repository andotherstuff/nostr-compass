---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-07-01
draft: false
type: newsletters
---

Bentornati su Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [FIPS v0.4.0](#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul) introduce un trasporto sulla mixnet Nym, la scoperta mDNS facoltativa sulla LAN, il rekey senza interruzioni in caso di perdita di pacchetti e una revisione del data plane, mantenendo la compatibilità wire con v0.3.0. [Whitenoise Linux](#whitenoise-linux-surfaces-as-a-desktop-marmot-client) emerge come client Marmot desktop in Rust e Slint, con una proposta di protocollo per spostare gli effetti dei messaggi in un evento kind 9 dedicato. [CustID v0.1.10-beta](#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow) debutta come cassaforte mobile per identità protetta dall'hardware, che opera da signer remoto NIP-46 e risponde tramite NFC alle richieste di accesso fisico. [myco](#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh) inaugura la condivisione peer-to-peer di nsite sulla mesh FIPS con un nuovo trasporto BLE L2CAP nella v0.1.0. [Nostr Codex Phone](#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr) debutta come superficie di controllo Android per un assistente di programmazione Codex locale, raggiunto tramite DM Nostr cifrati. [Il ramo non ancora rilasciato di Amethyst](#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section) aggiunge il parsing degli application handler NIP-89, un feed Git Repositories per NIP-34 e una sezione Discover per nSite e napplet. [Notedeck](#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments) implementa NIP-37, NIP-52 e NIP-22 in una sola settimana. [Applesauce](#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut) pubblica 12 release coordinate dei suoi sottopacchetti, con helper nbunksec per NIP-46 e un aggiornamento del wallet a Cashu-ts v4. [Meiso v1.4.0](#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing) introduce Shared-Key Collaborative Lists su eventi indirizzabili kind 35000. Il repository NIPs ha integrato cinque PR, fra cui un evento Relay Roles, la rimozione del limite di 65.535 byte di NIP-44, la semantica dei fork di NIP-34, i metadati client di NIP-46 e un metodo `signevent` per NIP-86. Gli approfondimenti riguardano [NIP-86 (API di gestione dei relay)](#nip-deep-dive-nip-86-relay-management-api) e [NIP-89 (application handler consigliati)](#nip-deep-dive-nip-89-recommended-application-handlers).

---

## Storie principali

### FIPS v0.4.0 introduce il trasporto sulla mixnet Nym, la scoperta mDNS e una revisione del data plane

[FIPS](https://github.com/jmcorgan/fips) è una rete mesh peer-to-peer privata e auto-organizzata per Nostr, nella quale i nodi si scoprono e instradano il traffico senza infrastruttura centrale. [FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) porta un trasporto sulla mixnet Nym, la scoperta mDNS facoltativa sulla LAN, una revisione del data plane, il rekey senza interruzioni in caso di perdita di pacchetti, una TUI `fipstop` riscritta su un harness di snapshot del rendering, un piano di osservabilità fuori dall'hot path e nuovi target di packaging apk per OpenWrt e flake per Nix. Tutto resta compatibile a livello wire con v0.3.0, così le mesh miste continuano a interoperare durante un aggiornamento progressivo. Due nuovi trasporti per la scoperta dei peer sono al centro della release. Un nuovo [trasporto in uscita sulla mixnet Nym](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) instrada il traffico FIPS attraverso un proxy SOCKS5 `nym-socks5-client`, mescolandolo nella rete di cover traffic di [Nym](https://nymtech.net/) affinché gli osservatori a livello di collegamento non possano correlare quali peer della mesh stiano comunicando; un esempio `examples/sidecar-nostr-mixnet-relay` mostra come esporre un relay Nostr locale attraverso quel percorso. Sulla LAN, la nuova scoperta mDNS è esplicitamente facoltativa e pubblicizza solo un identificatore di nodo e una porta, senza chiavi o metadati dell'utente.

Il data plane è stato rielaborato per aumentare il throughput di un singolo nodo. La cifratura e la decifratura per peer ora vengono eseguite da task worker dedicati fuori dal ciclo di ricezione, così un peer molto attivo non può serializzare la crittografia dell'intero nodo. Il percorso di invio Linux usa generic segmentation offload e, dove disponibile, un socket UDP connesso; l'hot path di ricezione evita le copie dei buffer effettuate in precedenza per ogni pacchetto, mentre macOS riceve una modalità di ricezione in batch `recvmsg_x` analoga al batching Linux `recvmmsg` introdotto nella v0.3.0. L'intera superficie di lettura `show_*` per `fipsctl` e `fipstop` ora viene servita da uno snapshot per tick, pubblicato in un `ArcSwap` lock-free dal task che accetta le connessioni di controllo, così le richieste degli operatori ricevono risposta rapidamente anche quando il ciclo di ricezione del nodo è occupato. Una nuova query `show_metrics` di soli contatori, esposta come `fipsctl stats metrics`, consente lo scraping Prometheus senza costi sull'hot path.

Il rekey delle sessioni FMP e FSP ora avviene senza interruzioni in presenza di perdita e riordinamento dei pacchetti in entrambe le direzioni: i frame in ingresso vengono autenticati rispetto alla sessione in attesa prima che il passaggio con K-bit la promuova, così un frame obsoleto o contraffatto non può mandare fuori strada il rekey; la ritrasmissione del messaggio 1 del rekey è limitata, l'heartbeat che rileva un collegamento interrotto tiene conto del rekey e le corse dovute all'avvio simultaneo su collegamenti ad alta latenza vengono desincronizzate con jitter simmetrico. La TUI `fipstop` è stata ricostruita su un harness di snapshot del rendering che verifica l'esatta griglia di testo e lo stile di ogni cella per ciascuna vista, usando output predefiniti del socket di controllo. Arrivano anche nuovi target di packaging: un `.apk` per OpenWrt 25+ costruito senza SDK, riutilizzando la cross-compilazione `.ipk` esistente e il payload del filesystem installato, e un `flake.nix` nella radice del progetto che compila dal sorgente tutti e quattro i binari (`fips`, `fipsctl`, `fips-gateway`, `fipstop`) su Nix/NixOS con la toolchain fissata.

### Whitenoise Linux emerge come client Marmot desktop

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git) è un client [Marmot](/it/topics/marmot/) desktop: messaggistica di gruppo MLS su relay Nostr, distribuita come singolo binario Rust con un'interfaccia Slint che conserva ogni segreto in una cassaforte cifrata con password.

Il filone più rilevante di questa settimana propone di trasportare gli effetti dei messaggi Whitenoise come eventi kind 9 dedicati che fanno riferimento al messaggio padre. L'attuale formato wire aggiunge alla fine del corpo un marcatore come `dmfx:sparkle`, sporcando il testo per qualsiasi renderer che non conosca questa convenzione. Spostare gli effetti in eventi propri mantiene pulito il testo dei messaggi e apre una questione progettuale che l'intero stack Marmot dovrà affrontare: convenzioni inline nel corpo oppure eventi sidecar per le funzionalità avanzate facoltative.

### CustID debutta come cassaforte mobile per identità con NIP-46 e richieste via NFC

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c) è la prima beta pubblica di CustID, una cassaforte mobile per identità costruita su Nostr e sul protocollo SISTR. CustID memorizza più identità Nostr in un archivio sicuro protetto dall'hardware, opera come signer remoto [NIP-46](/it/topics/nip-46/) per altri client e risponde a richieste di accesso fisiche e online tramite NFC e codici QR.

La beta è completa nelle funzionalità del signer NIP-46 e del flusso challenge-response NFC; i flussi di accesso basati su zero-knowledge proof restano un traguardo futuro. Questa release elimina inoltre il livello keep-alive [NIP-65](/it/topics/nip-65/) in background dell'app, che apriva un WebSocket per profilo per ciascun relay di lettura e acquisiva kind poi scartati immediatamente dal client. Ora restano attivi in background soltanto i socket NIP-46 che trasportano le notifiche delle richieste di firma: è la correzione che rende praticabile l'uso di CustID come bunker per altri client su un telefono.

### myco inaugura la condivisione peer-to-peer di nsite sulla mesh FIPS

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0) è comparso questa settimana, il 27 giugno, e ha raggiunto v0.1.0 il 1° luglio. myco è un'app Android in Rust che installa applicazioni provenienti dalle persone vicine: condivisione peer-to-peer di [nsite](/it/topics/nip-5a/) su una mesh FIPS, attraverso qualsiasi trasporto supportato dalla mesh (UDP, TCP, Tor, Bluetooth), funzionante interamente offline. Il progetto abbina direttamente FIPS come substrato di trasporto al formato di eventi per siti web statici di NIP-5A come payload, consentendo a un'app distribuita come nsite di spostarsi fra peer della mesh senza dipendere da relay o HTTP.

La v0.1.0 aggiunge un percorso radio Bluetooth L2CAP, così due telefoni con FIPS installato possono collegarsi in peer tramite BLE senza alcuna rete, oltre a uno speedtest per peer e alla condivisione attivata via NFC dal bottom sheet Circle dell'app. myco è pubblicato anche su Zapstore per l'installazione diretta.

### Nostr Codex Phone debutta come superficie di controllo mobile per un worker Codex locale tramite Nostr

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone) debutta questa settimana come client Android che controlla un worker locale dell'assistente di programmazione Codex tramite messaggi diretti Nostr cifrati. L'app supporta più sessioni di repository, trascrizione vocale, sessioni worker instradate, upload di media su Blossom e risposte vocali facoltative, così uno sviluppatore che esegue un worker Codex a casa può inviare richieste dal telefono ovunque questo abbia accesso ai relay.

Il progetto è un diretto parente di [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr), presentato nel numero 28. Entrambi portano su un trasporto Nostr i flussi di programmazione agentica con DM cifrati ed entrambi usano Nostr come livello di associazione e messaggistica che permette a un telefono di raggiungere un worker domestico senza aprire varchi nella rete. L'uso di Nostr come control plane per agenti locali sta diventando uno schema consolidato.

### Coop Mobile pubblica le sue prime build con versione

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1) e [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2) sono uscite questa settimana come prime build con versione di Coop Mobile, un client Android per messaggi diretti cifrati [NIP-17](/it/topics/nip-17/). Le due release migliorano la sicurezza contro i crash durante il parsing dei messaggi e la gestione dei QR e cancellano tutti i dati memorizzati al logout.

### Amethyst sviluppa un'interfaccia consapevole di NIP-89, un feed Git Repositories e una sezione Discover per napplet

Il ramo principale di [Amethyst](https://github.com/vitorpamplona/amethyst) ha sviluppato diverse nuove superfici questa settimana. Un [feed Git Repositories](https://github.com/vitorpamplona/amethyst/pull/3406) trasforma i repository [NIP-34](/it/topics/nip-34/) in una categoria consultabile della timeline Android, filtrabile per community e autore, abbinata a un [browser git smart-HTTP](https://github.com/vitorpamplona/amethyst/pull/3415) che legge contenuti e commit dei repository senza uscire dall'app. L'host per napplet ha ricevuto una [sezione Discover](https://github.com/vitorpamplona/amethyst/pull/3409) che elenca web app curate insieme agli nSite e ai napplet seguiti, ricavati dagli eventi handler [NIP-89](/it/topics/nip-89/) e dagli eventi site [NIP-5A](/it/topics/nip-5a/). La visualizzazione delle note ora [rivela quale app Nostr ha creato un evento](https://github.com/vitorpamplona/amethyst/pull/3422) tramite i tag NIP-89. Sul fronte della sincronizzazione arriva il [supporto alla negentropy NIP-77](https://github.com/vitorpamplona/amethyst/pull/3434), con riconciliazione in streaming e finestre `created_at` automatiche per aggirare i limiti ai risultati imposti dai relay, riducendo la banda necessaria a mantenere sincronizzati con un relay grandi insiemi locali di eventi.

### Buzz v0.3.38 irrobustisce la superficie di attacco dei relay e aggiunge la selezione dei modelli indipendente dal provider

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38) irrobustisce la [superficie di attacco dei relay](https://github.com/block/buzz/pull/1369) esposta da Buzz quando pubblica persona, team, agenti gestiti e attestazioni dei proprietari NIP-OA come eventi Nostr firmati. Un relay Buzz è un registro pubblico delle identità Nostr del team e del loro stato; questa release rafforza la validazione degli input e la protezione dai replay sui kind di evento ben noti definiti da Buzz. La release generalizza inoltre la selezione dei modelli, così un team Buzz può scegliere qualsiasi provider per cui Buzz disponga di adapter, incluso un nuovo backend Databricks AI Gateway v2.

### Notedeck implementa relay di sincronizzazione privata NIP-37, calendario NIP-52 e commenti NIP-22

[Notedeck](https://github.com/damus-io/notedeck), il client desktop nativo in Rust del team Damus, ha implementato tre protocolli in una sola settimana. I relay di sincronizzazione privata ora vengono memorizzati come lista kind `10013` [NIP-37](/it/topics/nip-37/), separando l'insieme di relay per contenuti privati dell'utente dall'outbox pubblica NIP-65. Il pannello calendario `horizon` legge eventi [NIP-52](/it/topics/nip-52/) da nostrdb e ha ricevuto una nuova disposizione a tre riquadri. Il pannello `headway` ha aggiunto un modello di eventi commento [NIP-22](/it/topics/nip-22/) su kind `1111`, il kind definito da NIP-22 per la superficie unificata dei commenti che sostituisce il concatenamento delle risposte NIP-10.



### Applesauce introduce sessioni NIP-46 nbunksec e aggiorna il wallet a Cashu v4

[Applesauce](https://github.com/hzrd149/applesauce), il toolkit modulare Nostr per signer, relay, wallet e contenuti, ha pubblicato una serie coordinata di [release 6.2.x](https://github.com/hzrd149/applesauce/releases) nei suoi sottopacchetti. Il pacchetto signers ha ricevuto helper per importare ed esportare `nbunksec`, trattando una sessione bunker [NIP-46](/it/topics/nip-46/) come un artefatto portabile che può spostarsi fra client. Il pacchetto wallet ha aggiornato i binding [Cashu](/it/topics/nip-60/) a `@cashu/cashu-ts` v4, dove gli importi delle proof diventano value object `Amount` e cambia l'API di decodifica dei token.

---

## Release con tag

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0) introduce la successiva iterazione del protocollo per la rete [Mostro](/it/topics/nip-69/) di scambio P2P di valuta fiat. La release segue [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2) ed esce insieme a [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0), che adotta il nuovo core. Questa settimana sono state integrate tre PR nel repository core; lo stack circostante, mostro daemon e Mostro mobile, si allinea alla v0.14.0 del crate di tipi condivisi.

### ngit v2.6.1

[ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli), la CLI canonica per git su Nostr nei repository [NIP-34](/it/topics/nip-34/), implementa la [semantica dei fork GRASP-06 di NIP-34](https://github.com/nostr-protocol/nips/pull/2395) integrata questa settimana, che sostituisce il tag `personal-fork` con un tag `u` negli eventi repo-state.

### mesh-llm v0.72.0 e v0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm), il componente di inferenza dello stack ContextVM che esegue LLM open source dietro una superficie JSON-RPC indirizzabile via Nostr, ha pubblicato [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0) e [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1), con una correzione per un crash del batching su singoli prompt di grandi dimensioni e una migrazione del bridge MCP che abbandona helper deprecati.

### Meiso v1.4.0 introduce Shared-Key Collaborative Lists che sostituiscono MLS per la condivisione dei task

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0) introduce un modello Shared-Key Collaborative Lists che sostituisce la precedente condivisione dei task basata su MLS con un design più semplice di eventi indirizzabili. Ogni lista condivisa genera una chiave Nostr dedicata distribuita ai membri; i task sono eventi indirizzabili kind `35000`, identificati da `d=task-id`, con contenuto auto-cifrato tramite [NIP-44](/it/topics/nip-44/), mentre i relay applicano Last-Write-Wins per ciascun task. Il design rinuncia alla forward secrecy e alla sicurezza post-compromissione di MLS in cambio di un'implementazione più semplice nei client e della risoluzione dei conflitti a livello di relay.

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn) introduce un filone "more-private-coordinator" che rimuove le pubkey effimere dei mittenti dalla pubblicazione dei messaggi di gruppo e irrobustisce il flusso delle richieste di ingresso contro nuove richieste obsolete. Cordn è lo stack di messaggistica basato su MLS presentato nel [lancio del CVM ad hoc di Cordn nel numero 28](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator); questa release è il corrispondente aggiornamento lato coordinatore.

---

## Modifiche non ancora rilasciate

### diVine integra 108 PR di rifiniture successive al lancio

[diVine](https://github.com/divinevideo/divine-mobile), il client per brevi video in loop che riporta in vita Vine, attraversa un'intensa fase di rifinitura successiva al lancio. Il lavoro visibile su Nostr questa settimana consiste in un passaggio di stabilizzazione del flusso di connessione [NIP-46](/it/topics/nip-46/), che migra gli errori `nostrconnect://` verso codici di motivo strutturati.

### Zap Cooking prosegue la correzione NIP-46 trasversale ai progetti e la revisione del compositore

[Zap Cooking](https://github.com/zapcooking/frontend) è un client Nostr per condividere ricette, pubblicate come eventi Nostr long-form. Il lavoro di questa settimana prosegue la correzione [NIP-46](/it/topics/nip-46/) trasversale ai progetti e la revisione del compositore descritte fra le modifiche non ancora rilasciate nel [numero 28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes).

### Conduit irrobustisce il flusso degli annunci e la correttezza del marketplace

[Conduit](https://github.com/Conduit-BTC/conduit-mono) è un monorepo di marketplace su Nostr composto da tre app: mercato per acquirenti, portale per commercianti e generatore di negozi. Il lavoro di questa settimana prosegue la spinta sulla correttezza del marketplace descritta nella [copertura del lancio nel numero 28](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default), sulla scia dell'ondata commerciale [NIP-99](/it/topics/nip-99/) che ha costituito la storia di protocollo dello scorso numero.

### Pollerama dalla v1.12 alla v1.13.1 aggiunge la scelta del client tag, schede del profilo e limiti ai thread

[Pollerama](https://github.com/formstr-hq/nostr-polls), un client Nostr Android incentrato su sondaggi e note con un forte livello di scoperta basato sul web of trust, ha pubblicato questa settimana su Zapstore v1.12.0, v1.13.0 e v1.13.1. Ora gli utenti possono scegliere quale client tag allegare alle note e ai sondaggi che creano, selezionandolo da un elenco predefinito o inserendone uno proprio. Le catene di commenti e risposte molto annidate si interrompono ora dopo pochi livelli e rimandano al thread completo nella pagina della nota. Le pagine dei profili si aprono per impostazione predefinita su Notes, suddivise nelle schede Posts e Conversations. È stato corretto un bug di persistenza dei follow, per cui gli account appena seguiti scomparivano al riavvio dell'app, e i pulsanti di follow ora mostrano l'avanzamento.

### getwired.app e get-tao.app correggono il flusso di invio confess di NIP-13

[getwired.app](https://github.com/smolgrrr/Wired) e [get-tao.app](https://github.com/smolgrrr/TAO), che condividono un flusso di pubblicazione anonima che aggiunge proof-of-work NIP-13 al momento dell'invio per limitare lo spam, hanno corretto il [flusso di invio confess](https://github.com/smolgrrr/Wired/pull/57) affinché l'esperienza utente durante il mining PoW sia coerente.

### nostui aggiunge una scheda della timeline delle menzioni

[nostui](https://github.com/akiomik/nostui), un client Nostr da terminale in Rust, ha aggiunto una [scheda della timeline delle menzioni](https://github.com/akiomik/nostui/pull/463) che presenta in una vista TUI dedicata gli eventi kind 1 che taggano la pubkey attiva.

### Heartwood introduce URI bunker NIP-46 per identità e un bridge di firma in modalità HSM

[Heartwood](https://github.com/forgesworn/heartwood) è un signer [NIP-46](/it/topics/nip-46/) nel quale la chiave di firma non raggiunge mai il client: quest'ultimo comunica tramite NIP-46 con un piccolo relay, che a sua volta usa un protocollo di frame seriali per parlare con un dispositivo hardware collegato ed eseguire la firma. Questa settimana il progetto ha integrato un [bridge di firma da relay a seriale](https://github.com/forgesworn/heartwood/pull/11) e [connessioni bunker per identità](https://github.com/forgesworn/heartwood/pull/16), così un singolo dispositivo hardware che custodisce più identità espone un URI bunker distinto per ciascuna.

### Refactoring dell'autenticazione e dei signer di Nostter

Questa settimana [Nostter](https://github.com/SnowCait/nostter) ha rielaborato il proprio [livello di autenticazione e signer](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth), spostando lo stato di login su un unico signal ed estraendo il dispatch del signer in moduli di strategia. La direzione è un'astrazione pulita del signer, nella quale estensione web NIP-07, bunker remoto NIP-46 e nsec grezzo condividono un solo percorso di codice.

### Dart NDK estrae il signer NIP-07 e randomizza i timestamp NIP-59

[Dart NDK](https://github.com/relaystr/dart_ndk) ha spostato il signer [NIP-07](/it/topics/nip-07/) fuori dal pacchetto core e dentro `ndk_flutter`, dove risiede la WebView Flutter, e ha [randomizzato i timestamp dei gift wrap NIP-59](https://github.com/relaystr/dart_ndk/pull/667) per rafforzare la protezione contro la correlazione temporale dei messaggi cifrati.

### Milk Market aggiunge pagine vetrina NIP-23 e pagamenti tramite Square

[Milk Market](https://github.com/shopstr-eng/milk-market), la vetrina marketplace del team Shopstr, ha dotato ogni negozio di una pagina blog basata sugli eventi long-form [NIP-23](/it/topics/nip-23/) del venditore, con sezioni modificabili e una route diretta per le impostazioni del blog. Nella stessa settimana ha aggiunto [Square](https://github.com/shopstr-eng/milk-market/pull/30) come processore di pagamenti alternativo per i venditori e l'acquisto automatico delle etichette di spedizione per gli ordini pagati.

### Calendar by Formstr pubblica un'app iOS

Questa settimana [Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) ha integrato la [PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159), portando su iOS il client calendario [NIP-52](/it/topics/nip-52/). La [PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197) corregge il parsing delle date del calendario nell'ora locale e la [PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201) aggiunge un flusso E2E Playwright attivato da un'etichetta `run-tests`.

### cagliostr applica NIP-22, NIP-09 per coordinate e proof-of-work NIP-13

[cagliostr](https://github.com/mattn/cagliostr), un'implementazione di relay in Go, ha rafforzato questa settimana tre percorsi di applicazione delle regole: [proof-of-work NIP-13 configurabile](https://github.com/mattn/cagliostr/pull/7) sugli eventi in ingresso, [eliminazione NIP-09 per coordinate indirizzabili](https://github.com/mattn/cagliostr/pull/8), così gli eventi sostituibili possono essere eliminati tramite il loro tag `a`, cosa impossibile con la sola eliminazione per id evento, e [limiti temporali NIP-22 configurabili](https://github.com/mattn/cagliostr/pull/9), che rifiutano eventi datati troppo nel passato o nel futuro.

---

## Nuovi progetti monitorati e scoperti

La [suite per il benessere Vanderwarker](https://git.vanderwarker.family/wellbeing) pubblica telemetria del mondo fisico come eventi Nostr tramite una chiave di firma condivisa del publisher. Comprende cinque app collegate: [Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android) è un contapassi che registra dati di fitness su Nostr come `kind:30078`; [Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android) pubblica ogni giorno il numero di sblocchi del telefono; [Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android) pubblica la riproduzione multimediale corrente come User Status; [Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android) pubblica ogni 15 minuti livello, tensione e temperatura della batteria; [Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android) pubblica il consumo giornaliero di dati. Tutte e cinque sono apparse su Zapstore fra il 24 e il 30 giugno.

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9) è un'app Android serverless per la condivisione cifrata della posizione in tempo reale, realizzata in Rust e Slint e pubblicata il 29 giugno. È un progetto collegato a [Haven](https://github.com/mehmetefeumit/Haven-App), il sistema di condivisione della posizione basato su [Marmot](/it/topics/marmot/) descritto nel [numero 28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot), ma usa un'architettura di trasporto diversa: gli aggiornamenti della posizione viaggiano in DM Nostr cifrati, mentre Haven usa messaggi di gruppo Marmot.

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell) è uno scaffold iniziale di shell applicativa per costruire app Nostr. Questa settimana il progetto ha pubblicato la sua prima documentazione rivolta agli utenti.

[NIPs by Pollerama](https://nips.pollerama.fun), repository [abh3po/better-nips](https://github.com/abh3po/better-nips) creato il 2026-06-29, è un nuovo client per i NIP `kind:30817` scritti dalla community di [NostrHub](https://nostrhub.io), proposto come superficie alternativa a nostrhub.io con ponderazione basata sulla fiducia. Ogni NIP `kind:30817` ha un proprio URL condivisibile (`#/nip/<naddr>`), con rendering Markdown completo e i kind di evento che definisce. Il client offre tre feed, Following, Web of Trust (follow dei follow) e Global, ciascuno ordinabile per approvazioni ponderate in base alla fiducia o per data. Le approvazioni vengono pubblicate come label [NIP-32](/it/topics/nip-32/) su kind `1985`, con i tag `["L","nostrhub"]` e `["l","approve","nostrhub"]`, oltre a un tag `a` che punta all'indirizzo del NIP obiettivo e a un tag `client` che dichiara `better-nips`. È esattamente la forma di evento firmata dallo stesso NostrHub, così le approvazioni sono compatibili fra i due client. L'approvazione di un follow diretto pesa nella classifica più di quella proveniente da un follow di secondo grado.

Lo stack di firma è [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer), con una finestra di login completa che comprende signer [NIP-07](/it/topics/nip-07/), bunker e nostrconnect [NIP-46](/it/topics/nip-46/), ncryptsec [NIP-49](/it/topics/nip-49/) e signer Android [NIP-55](/it/topics/nip-55/); le sessioni si ricollegano silenziosamente al ricaricamento. Il livello di rete passa attraverso [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay), un Web Worker che suddivide l'outbox [NIP-65](/it/topics/nip-65/) dell'utente fra i relay, impedendo che un grande insieme web of trust venga inoltrato in massa a un singolo relay. La posizione progettuale è che i NIP della community, ospitati da NostrHub, in `better-nips` o da altri client futuri, siano tutti uguali a livello di protocollo; la classifica deriva dal grafo sociale, non dalla selezione dei moderatori, collegandosi direttamente al flusso di labeling NIP-32 esaminato nell'approfondimento del [numero 25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling).

Questa settimana sono comparsi due nuovi cluster di repository [NIP-34](/it/topics/nip-34/). [Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git) è un client Nostr incentrato sui video, mentre un [cluster nostrapps.com](wss://gitnostr.com) pubblica tre progetti collegati: [verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git), una VM per napp desktop; [hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git), un client personalizzabile per community; e [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git), una specifica e runtime per microapp HTML. Il cluster si colloca in parallelo al lavoro sui [napplet](/it/topics/nip-5d/) trattato nella storia principale dello scorso numero.

---

## Lavoro sul protocollo e aggiornamenti dei NIP

### Integrata: NIP-44 elimina il limite di payload di 65.535 byte

La [PR #1907](https://github.com/nostr-protocol/nips/pull/1907) è stata integrata il 28 giugno dopo essere rimasta aperta dal 2024-09. La modifica rimuove il limite massimo di 65.535 byte per il payload in chiaro di un envelope di cifratura versionata [NIP-44](/it/topics/nip-44/), portandolo a un massimo di 4 GiB (`uint32_max`). NIP-44 codifica la lunghezza del payload come `uint16` nel formato wire, requisito imposto rigidamente dalla specifica originale per l'interoperabilità; la modifica integrata adotta un campo di lunghezza maggiore indicato nel byte di versione, così le implementazioni v2 restano compatibili a livello wire e quelle v3+ trasportano la lunghezza estesa. I client che usano NIP-44 per messaggi diretti [NIP-17](/it/topics/nip-17/), gift wrap [NIP-59](/it/topics/nip-59/), payload dei signer remoti [NIP-46](/it/topics/nip-46/) o qualsiasi altro messaggio Nostr cifrato con NIP-44 possono ora scambiare singoli eventi più grandi di 64 KiB senza suddividerli a livello applicativo.

### Integrate: NIP-86 riceve un metodo signevent e un evento Relay Roles

La [PR #2389](https://github.com/nostr-protocol/nips/pull/2389) aggiunge un metodo `signevent` all'API JSON-RPC di gestione dei relay [NIP-86](/it/topics/nip-86/), permettendo a un amministratore di chiedere al relay di firmare un evento con la pubkey del relay stesso. La [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) associata definisce un evento Relay Roles: un evento sostituibile pubblicato dal relay per dichiarare i propri amministratori e moderatori. Insieme consentono ai client NIP-86 di ricavare l'elenco degli amministratori di un relay e verificare che una richiesta autenticata provenga da un amministratore corrente, senza fiducia fuori banda. Entrambe le modifiche sono approfondite più avanti.

### Integrata: NIP-34 sostituisce personal-fork con `u` per GRASP-06

La [PR #2395](https://github.com/nostr-protocol/nips/pull/2395), integrata il 24 giugno, sostituisce il tag `personal-fork` di [NIP-34](/it/topics/nip-34/) negli eventi repo-state (`kind:30618`) con un tag `u`, per "upstream", allineando il formato wire alla semantica dei fork GRASP-06 implementata dalla suite GitWorkshop. La modifica chiude la [PR #2384](https://github.com/nostr-protocol/nips/pull/2384), `NIP-34: remove maintainers to solve expiry issues`, che proponeva una diversa correzione alla semantica dei fork. La direzione integrata è quella implementata da ngit v2.6.x, quindi specifica e CLI di riferimento sono ora allineate. I repository esistenti che usano `personal-fork` continuano a interoperare; i nuovi repository e la linea ngit v2.6 pubblicano il tag `u`.

### Integrati: metadati client NIP-46, ora upstream dopo l'implementazione in Amber

La [PR #2381](https://github.com/nostr-protocol/nips/pull/2381), integrata il 23 giugno, aggiunge metadati client facoltativi alla richiesta `connect` di [NIP-46](/it/topics/nip-46/), consentendo a un client di pubblicare nome, URL dell'icona e URL della homepage durante la connessione al signer. [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) ha introdotto l'estensione dei metadati la scorsa settimana, come descritto nel [numero 28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata); questa settimana il NIP upstream raggiunge l'implementazione già distribuita.

### Aperte: chiavi wrapper NIP-17 deterministiche basate su epoche

La [PR #2397](https://github.com/nostr-protocol/nips/pull/2397) e la [PR #2396](https://github.com/nostr-protocol/nips/pull/2396) riguardano due proposte convergenti per le chiavi di wrapping NIP-17. La PR #2397 propone che la chiave di firma effimera usata per creare un gift wrap [NIP-59](/it/topics/nip-59/) sia derivata in modo deterministico da un seed per conversazione, legato a un'epoca temporale approssimativa, così un destinatario che conosce la chiave della conversazione può prevedere a quali pubkey sottoscriversi. La specifica attuale richiede una nuova chiave casuale per ogni wrap, rendendo impossibile tale previsione. La PR #2396 è la modifica complementare: i wrap di una determinata conversazione dovrebbero essere firmati direttamente con la chiave della conversazione, così la pubkey del wrap funge anche da identificatore della conversazione. Insieme definiscono un percorso verso conversazioni NIP-17 filtrabili senza perdita di metadati. Entrambe sono aperte e in discussione.

### Aperta: NIP-59 dovrebbe far rifiutare ai relay gli eventi seal kind 13

La [PR #2399](https://github.com/nostr-protocol/nips/pull/2399) propone che i relay rifiutino gli eventi kind 13, il seal interno di un gift wrap [NIP-59](/it/topics/nip-59/), quando compaiono al livello superiore di una richiesta di pubblicazione, perché un evento seal ha senso soltanto dentro un wrap e un seal esposto rivela la pubkey del destinatario. La [issue #2398](https://github.com/nostr-protocol/nips/issues/2398) associata va oltre e sostiene che il seal dovrebbe essere ridefinito come kind effimero, poiché i kind effimeri NIP-01 non vengono memorizzati dai relay; ciò irrobustirebbe la regola a livello di protocollo ed eliminerebbe la dipendenza dalle policy dei singoli relay.

### Aperta: stati dei gruppi NIP-29

La [PR #2372](https://github.com/nostr-protocol/nips/pull/2372) aggiunge una semantica esplicita degli stati dei gruppi a [NIP-29](/it/topics/nip-29/), dedicato ai gruppi basati su relay, definendo cosa significhi che un gruppo sia aperto, chiuso, pubblico, privato o archiviato e come le transizioni di stato interagiscano con gli eventi dei membri. La proposta porta nella specifica del relay una semantica finora specifica dei singoli client.

### Aperta: supporto facoltativo per più maintainer in NIP-34

La [PR #2324](https://github.com/nostr-protocol/nips/pull/2324) è la proposta complementare alla [PR #2395](https://github.com/nostr-protocol/nips/pull/2395) integrata, relativa alla semantica dei fork GRASP-06 trattata sopra. La PR #2324 aggiunge il supporto facoltativo per più maintainer agli eventi di annuncio dei repository [NIP-34](/it/topics/nip-34/) (`kind:30617`), permettendo a un repository di dichiarare più di una pubkey di maintainer canonico tramite tag `maintainer` ripetuti. Patch e issue firmate da qualsiasi maintainer dichiarato vengono quindi considerate ufficiali dai client, colmando la lacuna storica per cui i repository NIP-34 con più maintainer devono convogliare tutto attraverso una pubkey oppure ricorrere al coordinamento fuori protocollo.

### Aperta: operatore AND di NIP-91 per i filtri, la proposta non è integrata

La [PR #2252](https://github.com/nostr-protocol/nips/pull/2252) propone un operatore AND per i [filtri](/it/topics/nip-01/) Nostr, riaprendo un progetto discusso per la prima volta nella precedente [PR #1365](https://github.com/nostr-protocol/nips/pull/1365), poi chiusa. Esistono già implementazioni in [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay), applesauce, [Amethyst](https://github.com/vitorpamplona/amethyst) e worker-relay, ma la PR della specifica resta aperta.

### Chiuse: quattro NIP commerciali di pats2sats

Questa settimana sono state chiuse quattro proposte per il commercio su Nostr: Escrow ([#2334](https://github.com/nostr-protocol/nips/pull/2334)), Reservations ([#2335](https://github.com/nostr-protocol/nips/pull/2335)), una Marketplace Listing Extension [NIP-99](/it/topics/nip-99/) ([#2346](https://github.com/nostr-protocol/nips/pull/2346)) e un Accommodation Listing Profile ([#2333](https://github.com/nostr-protocol/nips/pull/2333)). La stessa superficie commerciale viene ora consolidata nella [Gamma Market Spec](https://github.com/GammaMarkets/market-spec), un repository di estensioni di proprietà del progetto costruito sugli annunci marketplace NIP-99, con semantica per ordini, checkout, escrow e controversie. Compass ora monitora questo repository insieme a Marmot e Blossom come repository di specifiche di protocollo esterno allo stesso repository NIPs; le PR aperte questa settimana comprendono chiarimenti sull'attribuzione del client ([#11](https://github.com/GammaMarkets/market-spec/pull/11)), un tag supersedes per le modifiche all'identità dei prodotti ([#8](https://github.com/GammaMarkets/market-spec/pull/8)) e la semantica delle recensioni dei commercianti ([#7](https://github.com/GammaMarkets/market-spec/pull/7)).

### Aperte: collegamento delle identità Bitcoin

Questa settimana sono state aperte due proposte per collegare identità Bitcoin a identità Nostr: un [indirizzo Bitcoin Silent Payment NIP-352](https://github.com/nostr-protocol/nips/pull/2392) e una [proof di collegamento dell'identità Bitcoin-OTC](https://github.com/nostr-protocol/nips/pull/2401).

---

## Approfondimento NIP: NIP-86 (API di gestione dei relay)

[NIP-86](/it/topics/nip-86/) definisce un'interfaccia JSON-RPC per la gestione dei relay, consentendo ai client autorizzati di inviare comandi amministrativi ai relay tramite un'API standardizzata. Un unico client può gestire qualsiasi relay compatibile con NIP-86 senza strumenti specifici per ciascuno. Due modifiche alla specifica integrate questa settimana, [PR #2389](https://github.com/nostr-protocol/nips/pull/2389) e [PR #2390](https://github.com/nostr-protocol/nips/pull/2390), chiudono il circuito fra eventi firmati dai relay e amministratori dichiarati dai relay.

### Il trasporto

Una richiesta di gestione NIP-86 è un HTTP POST allo stesso URI dal quale il relay serve le connessioni WebSocket, con `Content-Type: application/nostr+json+rpc`. Il corpo della richiesta è un documento JSON della forma:

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

L'autenticazione usa un evento firmato di autenticazione HTTP [NIP-98](/it/topics/nip-98/) nell'header `Authorization`. Prima di eseguire il metodo, il relay verifica che la pubkey firmataria sia nel proprio elenco di amministratori. La risposta del relay è un documento JSON della forma:

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### I metodi esistenti prima di questa settimana

L'insieme di metodi preesistente comprende ban delle pubkey (`banpubkey`, `allowpubkey`, `listbannedpubkeys`), ban degli eventi (`banevent`, `allowevent`, `listbannedevents`), metadati del relay (`changerelayname`, `changerelaydescription`, `changerelayicon`), gestione dell'elenco dei kind consentiti (`allowkind`, `disallowkind`, `listallowedkinds`) e un metodo `stats` che restituisce statistiche del relay. La forma è volutamente simile a quella di un servizio JSON-RPC standard, così un client può costruirvi sopra binding tipizzati.

### Cosa è cambiato questa settimana

La [PR #2389](https://github.com/nostr-protocol/nips/pull/2389) aggiunge alla specifica un metodo `signevent`. Il metodo riceve come argomento un template di evento parziale, con kind, tag e content, e chiede al relay di firmare e restituire un evento completo usando la pubkey del relay nel campo `pubkey`. È il prerequisito affinché un relay possa pubblicare eventi di protocollo su se stesso: annunci di pubkey bloccate, metadati del relay e il nuovo evento Relay Roles descritto sotto richiedono tutti che il relay firmi con la chiave controllata dall'operatore, ma la maggior parte degli operatori non vuole custodire una chiave privata nel proprio client amministrativo.

La [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) definisce un evento Relay Roles: un kind di evento sostituibile parametrizzato che un relay pubblica, firmato con la propria pubkey tramite `signevent`, per dichiarare le pubkey dei suoi amministratori e moderatori con una semantica esplicita dei ruoli. Un client consapevole di NIP-86 può recuperare l'evento Relay Roles da qualsiasi relay monitorato, costruire l'elenco degli amministratori dai tag dell'evento e verificare che una richiesta NIP-86 autenticata provenga da un amministratore corrente, senza fiducia fuori banda né configurazione specifica per relay. Le due PR chiudono insieme il circuito: `signevent` è il meccanismo, Relay Roles è il primo kind di evento costruito su di esso.

### Esempio di richiesta NIP-86

Una richiesta NIP-86 `banpubkey` completa ha questa forma:

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

con un header `Authorization` che trasporta un evento firmato NIP-98:

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

La pubkey firmataria deve comparire nell'insieme degli amministratori del relay, ora dichiarato nell'evento relay-roles; il tag `u` deve corrispondere all'URL HTTPS del relay; il tag `payload` deve corrispondere allo SHA-256 del corpo JSON della richiesta. Il relay restituisce:

```json
{
  "result": true,
  "error": null
}
```

### Implementazioni

- [Amethyst](https://github.com/vitorpamplona/amethyst) offre su Android un'interfaccia di gestione dei relay NIP-86 dalla v1.07.0 in poi.
- Fra i relay di riferimento che implementano la specifica vi sono [strfry](https://github.com/hoytech/strfry), [khatru](https://github.com/fiatjaf/khatru) e diverse implementazioni minori collegate dalla sezione `Implementation Status` della specifica.

I client consapevoli di NIP-86 inizieranno a trattare l'evento relay-roles come fonte canonica dell'elenco degli amministratori di un relay, quando gli implementatori adotteranno le modifiche `signevent` e Relay Roles.

---

## Approfondimento NIP: NIP-89 (application handler consigliati)

[NIP-89](/it/topics/nip-89/) definisce due kind di eventi sostituibili parametrizzati, `kind:31990`, l'application handler pubblicato dallo sviluppatore di un'app, e `kind:31989`, la raccomandazione pubblicata dall'utente per un'app che utilizza. Insieme permettono ai client di scoprire applicazioni capaci di gestire un kind di evento sconosciuto senza coordinamento fuori banda: un lettore long-form che incontra un evento `kind:30030` non gestito nativamente può interrogare il grafo NIP-89 alla ricerca di handler e offrire all'utente un flusso `Open in...` verso un'app pubblicata che sappia gestirlo. NIP-89 è l'infrastruttura originaria per lo stesso problema di instradamento fra app che il lavoro su napplet e napps presente in questo numero sta ora estendendo ad applet componibili native di Nostr.

### L'evento application handler (`kind:31990`)

Lo sviluppatore di un'app pubblica uno o più eventi handler che descrivono quali kind di evento sono supportati dall'app e come aprire un'entità Nostr al suo interno:

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

Il tag `d` identifica l'handler, così può essere sostituito; ogni tag `k` dichiara un kind di evento gestito dall'app e ogni tag di piattaforma (`web`, `ios`, `android`, ...) fornisce un template URL con `<bech32>` come segnaposto per un'entità codificata secondo [NIP-19](/it/topics/nip-19/), che il client chiamante sostituisce al momento dell'apertura. Un singolo evento handler può pubblicizzare più kind supportati se condividono lo stesso schema di instradamento, mantenendo compatta la scoperta delle app ed evitando un evento handler per ogni kind.

### L'evento di raccomandazione dell'utente (`kind:31989`)

Un utente pubblica una raccomandazione che dichiara quali app usa per un determinato kind di evento:

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

Il tag `d` contiene il kind di evento raccomandato. Ogni tag `a` è un puntatore di indirizzo NIP-01 a un evento handler `kind:31990`, con il relay suggerito e la piattaforma a cui si applica la raccomandazione. La stessa raccomandazione può elencare più app per piattaforme differenti.

### Il client tag e il compromesso sulla privacy

NIP-89 definisce inoltre un tag `client` facoltativo che qualsiasi app di pubblicazione può allegare agli eventi di cui è autrice:

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

Ciò consente a qualsiasi client che mostra l'evento di presentare l'app da cui proviene, recuperare metadati più ricchi dell'handler e rispettare i suggerimenti di rendering dichiarati dall'handler. La specifica segnala esplicitamente anche il costo per la privacy: un client che emette un tag `client` su ogni evento pubblica l'identità del software dell'utente, rivelando nel tempo schemi di utilizzo. La specifica raccomanda ai client di offrire agli utenti la possibilità di disattivarlo.

La [PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422) di Amethyst analizza e mostra i tag NIP-89 `t`, `i`, `a` e `client` nella visualizzazione degli eventi, indicando direttamente nella timeline quale app ha creato una nota.

### Come funziona in pratica il flusso di scoperta

Un client che riceve un kind di evento sconosciuto segue questi passaggi. (1) Interroga il grafo dei follow dell'utente alla ricerca di eventi `kind:31989` con un tag `d` corrispondente al kind dell'evento. (2) Risolve ogni tag `a` raccomandato nel relativo evento handler `kind:31990`. (3) Sceglie l'handler il cui template URL `web`, `ios` o `android` corrisponde alla piattaforma corrente. (4) Sostituisce nel template URL la codifica `bech32` dell'entità. (5) Offre all'utente l'URL risultante come opzione `Open in...`. Il flusso è filtrato socialmente: un client che interroghi eventi handler arbitrari da relay non fidati potrebbe reindirizzare gli utenti verso app malevole, quindi partire dalle persone seguite dall'utente è un'impostazione predefinita più sicura che considerare ugualmente affidabile ogni handler pubblicato.

### NIP-89 e il livello napplet

La sezione Discover di Amethyst, il runtime host per napplet e la visualizzazione dei tag `client` costruiscono insieme una superficie completa di consumo NIP-89 su Android. La specifica napplet, introdotta nello scorso numero, estende ciò a cui possono puntare gli eventi handler NIP-89: applet in sandbox che vengono eseguite in un runtime componibile nativo di Nostr, sopra Nostr e Blossom. NIP-89 è il grafo di scoperta e instradamento; il runtime napplet è uno dei target di esecuzione a cui può puntare.

---

*Per segnalazioni, correzioni e progetti che ci sono sfuggiti, aprite una issue su [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass) oppure contattateci tramite DM NIP-17 all'indirizzo npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923.*
