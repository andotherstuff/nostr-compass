---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) porta la messaggistica in tempo reale e il supporto al signer Amber con oltre 160 miglioramenti uniti. [diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) corregge problemi di riproduzione video e aggiunge eventi di visualizzazione Kind 22236 per l'analisi dei creator. [Pika](https://github.com/sledtools/pika), [Ridestr](https://github.com/variablefate/ridestr) e [Unfiltered](https://github.com/dmcarrington/unfiltered) pubblicano aggiornamenti. [FIPS](https://github.com/jmcorgan/fips) distribuisce un'implementazione Rust funzionante di reti mesh native su Nostr. Notecrumbs riceve correzioni di stabilità per le anteprime link di damus.io. [ContextVM](https://contextvm.org) collega Nostr con il Model Context Protocol. I nuovi progetti includono [Burrow](https://github.com/CentauriAgent/burrow) per la messaggistica cifrata con MLS tra agenti AI e umani, e [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) per la gestione di vault e identità basata su browser. Gli approfondimenti coprono la firma Android NIP-55 e la sincronizzazione del wallet Cashu NIP-60.

## Notizie

### Miglioramenti di Stabilità di Notecrumbs

[Notecrumbs](https://github.com/damus-io/notecrumbs), il server API e web che alimenta le anteprime link di damus.io, ha ricevuto una serie di correzioni che risolvono problemi di affidabilità.

Una [correzione della concorrenza](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49) ha sostituito il meccanismo di deduplicazione in-flight con watch channel. Due chiamanti che richiedevano la stessa nota potevano diventare entrambi fetcher, causando un deadlock quando uno completava prima che l'altro si iscrivesse alla notifica. I watch channel con operazioni atomiche garantiscono che un solo fetcher sia attivo mentre gli altri attendono il risultato.

Il [rate limiting](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17) implementa una difesa a due livelli contro il bombardamento dei relay. Quando gli utenti accedono ripetutamente alla stessa nota, il sistema ora fa debounce delle richieste ai relay con una finestra di raffreddamento di 5 minuti. Questa protezione si estende a tutti i tipi [NIP-19](/it/topics/nip-19/) e ai feed dei profili, prevenendo spam proporzionale ai relay durante il traffico intenso.

I [miglioramenti delle prestazioni](https://github.com/damus-io/notecrumbs/commit/38670b3972b6) hanno spostato i fetch secondari dei dati a task tokio in background. Le pagine ora si renderizzano istantaneamente con dati in cache invece di bloccarsi su timeout sequenziali dei relay che potevano aggiungere fino a 7,5 secondi. Un aggiornamento a nostrdb 0.10.0 ha accompagnato queste correzioni.

### ContextVM: MCP su Nostr

[ContextVM](https://contextvm.org) è una suite di strumenti che collega Nostr e il [Model Context Protocol](https://modelcontextprotocol.io/) (MCP). I commit recenti hanno introdotto la nuova specifica [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/) che abilita i pagamenti, con miglioramenti all'[SDK](https://github.com/ContextVM/sdk) distribuiti nel corso di febbraio.

L'SDK fornisce transport TypeScript client e server per MCP su Nostr. Gli sviluppatori possono esporre server MCP attraverso la rete Nostr e i client possono connettersi ad essi. I relay agiscono come un bus messaggi cieco, instradando semplicemente eventi cifrati in modo opaco. I client senza supporto nativo a Nostr si connettono attraverso un livello proxy. La libreria gestisce la gestione dei relay e la firma crittografica per l'autenticazione degli event. Funziona sia in ambienti Node.js che browser.

[CVMI](https://github.com/ContextVM/cvmi) fornisce una CLI per la scoperta di server e l'invocazione di metodi. [Relatr](https://github.com/ContextVM/relatr) calcola punteggi di fiducia personalizzati dalla distanza nel grafo sociale combinata con la validazione del profilo.

ContextVM si posiziona come livello ponte: i server MCP esistenti acquisiscono interoperabilità con Nostr mantenendo i loro transport convenzionali.

### White Noise Documenta la Ricerca Utenti Decentralizzata

Un [post sul blog di jgmontoya](https://blog.jgmontoya.com/2026/02/22/user-search.html) spiega come [White Noise](https://github.com/marmot-protocol/whitenoise) gestisce la ricerca utenti attraverso la rete relay decentralizzata.

La distribuzione dei profili crea la sfida: a differenza dei messenger centralizzati con database unificati, i profili Nostr si disperdono su decine di relay senza indice centrale. White Noise risolve questo problema attraverso un'architettura produttore-consumatore che gira in parallelo.

Un processo produttore espande continuamente il grafo sociale verso l'esterno a partire dai seguiti dell'utente, recuperando liste di follow a distanze crescenti e accodando le pubkey scoperte per la risoluzione dei profili. Il consumatore risolve le corrispondenze attraverso cinque livelli di costo crescente: tabella utenti locale (più veloce), profili in cache dalle ricerche precedenti, relay connessi, liste relay utente per [NIP-65](/it/topics/nip-65/) e query dirette ai relay dichiarati dall'utente (più lento).

Le ricerche a freddo richiedono circa 3 secondi mentre le ricerche a caldo dalla cache scendono a circa 10 millisecondi. Per i nuovi utenti senza grafi sociali consolidati, il sistema inietta nodi bootstrap ben connessi per garantire la funzionalità di ricerca. L'appartenenza ai gruppi fornisce un segnale sociale implicito accanto ai seguiti espliciti.

La strumentazione si è rivelata fondamentale per l'ottimizzazione, nota l'autore. Senza metriche, i miglioramenti erano solo intuizioni.

### FIPS: Rete Mesh Nativa su Nostr

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System) è un'implementazione Rust funzionante di una rete mesh auto-organizzante che usa le keypair Nostr (secp256k1) come identità dei nodi. La [documentazione di design](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md) accompagna il codice funzionale.

Il protocollo affronta l'indipendenza infrastrutturale: i nodi si scoprono automaticamente senza server centrali o autorità di certificazione. Un spanning tree fornisce routing basato su coordinate mentre i bloom filter propagano informazioni di raggiungibilità, permettendo ai nodi di prendere decisioni di inoltro con sola conoscenza locale. L'agnosticismo dal trasporto significa che lo stesso protocollo funziona su UDP, Ethernet, Bluetooth, radio LoRa o qualsiasi mezzo capace di datagrammi.

Due livelli di cifratura proteggono il traffico. La cifratura a livello link (pattern Noise IK) protegge la comunicazione hop-by-hop tra vicini con autenticazione reciproca e forward secrecy. La cifratura a livello sessione (pattern Noise XK) fornisce protezione end-to-end contro i router intermedi, dove solo la destinazione può decifrare il payload. Questo rispecchia come TLS protegge il traffico HTTP anche quando attraversa reti non fidate.

L'architettura usa uno spanning tree a "greedy embedding" per il routing. Ogni nodo riceve coordinate basate sulla sua posizione relativa alla radice dell'albero e al genitore. I pacchetti vengono instradati greedy verso coordinate più vicine alla destinazione, con bloom filter che pubblicizzano gli endpoint raggiungibili. Quando il routing greedy fallisce (minimi locali), i nodi possono ricorrere ai percorsi basati sull'albero.

L'implementazione Rust include già il trasporto UDP con scoperta tramite bloom filter. I lavori futuri mirano all'integrazione relay Nostr per il bootstrapping dei peer.

## Rilasci

Questa settimana ha portato rilasci nell'infrastruttura relay e nelle applicazioni client, con nuovi progetti che entrano nello spazio.

### HAVEN v1.2.0

[HAVEN](https://github.com/bitvora/haven), il relay personale all-in-one che raggruppa quattro funzioni relay con un server media [Blossom](/it/topics/blossom/), ha distribuito la [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0). Questo rilascio va oltre la fase RC [coperta la settimana scorsa](/it/newsletters/2026-02-18-newsletter/#haven-v120-rc3).

Il supporto multi-npub permette a una singola istanza HAVEN di servire diverse identità Nostr tramite whitelisting, con nuove funzionalità di blacklisting per il controllo degli accessi. Un sistema di backup riscritto usa il formato JSONL portabile, con un comando `haven restore` per importare note da file JSONL. L'integrazione con lo storage cloud aggiunge i flag `--to-cloud` e `--from-cloud` per la gestione dei backup remoti.

I miglioramenti al [Web of Trust](/it/topics/web-of-trust/) includono livelli di profondità configurabili per i calcoli di fiducia e intervalli di aggiornamento automatico di 24 ore con ottimizzazione lockless che riduce l'overhead di memoria. La configurazione dello user-agent per le richieste ai relay e le impostazioni di timeout Blastr configurabili completano il rilascio, insieme all'esportazione dati in JSONL compresso.

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise), l'app di messaggistica cifrata basata su [MLS](/it/topics/mls/) che implementa il protocollo [Marmot](/it/topics/marmot/), ha distribuito la [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) con oltre 160 miglioramenti uniti.

Questo rilascio porta la messaggistica in tempo reale attraverso connessioni in streaming invece del polling, così i messaggi arrivano istantaneamente. Il supporto Amber ([NIP-55](/it/topics/nip-55/)) significa che le chiavi private non devono mai toccare l'app. La condivisione delle immagini ora funziona con tracciamento del progresso di upload e placeholder blurhash durante il caricamento. La visualizzazione a schermo intero supporta il pinch-to-zoom.

La messaggistica di gruppo ha ricevuto miglioramenti di affidabilità con le liste chat che mostrano i nomi dei mittenti e la cifratura [MLS](/it/topics/mls/) che garantisce la forward secrecy. La ricerca utenti si espande verso l'esterno dai seguiti fino a quattro gradi di separazione con risultati che arrivano in streaming man mano che vengono trovati.

Un breaking change azzera tutti i dati locali all'aggiornamento a causa di modifiche al protocollo Marmot e al passaggio allo storage locale cifrato. Gli utenti dovrebbero fare il backup delle chiavi nsec prima di aggiornare.

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile), il client video a ciclo breve costruito sugli archivi restaurati di Vine, ha distribuito la [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) con ampie correzioni alla riproduzione video e un nuovo sistema di analisi decentralizzato.

I problemi di riproduzione video hanno dominato le correzioni: pausa fantasma, audio doppio tra video, flash nero tra miniature e primi frame, e crash del player smaltito sono tutti risolti. Un player video in pool gestisce ora il feed Home per una riproduzione coerente.

Gli event di visualizzazione effimeri Kind 22236 abilitano l'analisi dei creator e le raccomandazioni. Il sistema traccia le fonti di traffico (home, varianti di scoperta, profilo, condivisione, ricerca) e i conteggi dei loop filtrando le auto-visualizzazioni. Le perdite di percorso file locale nei tag imeta degli event Nostr sono corrette con URL Blossom canonici costruiti lato client secondo la specifica BUD-01.

I miglioramenti al signer remoto [NIP-46](/it/topics/nip-46/) includono connessioni relay parallelizzate e supporto all'URL di callback. Android riconnette le connessioni WebSocket alla ripresa dell'app dopo l'approvazione del signer.

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle), il client Nostr web focalizzato sulla gestione dei relay e la moderazione [Web of Trust](/it/topics/web-of-trust/), ha distribuito la [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30) con supporto alle miniature video, migliorando la navigazione dei media nei feed.

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public), il client Nostr per iOS, ha distribuito la [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0) con una nuova sezione feed Live Streams e una schermata Impostazioni riprogettata. I GIF possono ora essere ospitati su server media Blossom, riducendo la dipendenza da servizi centralizzati. L'integrazione Klipy GIFs fornisce un backup quando Tenor non è disponibile. Le intestazioni per anno nelle conversazioni DM e la visualizzazione del conteggio menzioni completano le modifiche lato utente.

Gli strumenti per sviluppatori e le app CLI hanno ricevuto aggiornamenti anche questa settimana.

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak), il coltellino svizzero a riga di comando di fiatjaf per Nostr, ha distribuito la [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5) con un nuovo sottocomando `nak profile` per recuperare e visualizzare profili utente. Il comando `git clone` ora supporta i nomi [NIP-05](/it/topics/nip-05/) negli URI `nostr://`, abilitando il cloning di repository tramite identificatori leggibili.

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika), il messenger cifrato con [MLS](/it/topics/mls/) per iOS, Android e desktop costruito sul protocollo [Marmot](/it/topics/marmot/), ha distribuito la [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3). I commit recenti aggiungono il caricamento di file e il supporto al drag-and-drop media nell'app desktop, insieme a correzioni per il deployment su Cloudflare Workers.

Pika usa un core Rust che possiede tutta la logica di business mentre iOS (SwiftUI) e Android (Kotlin) agiscono come livelli UI snelli che renderizzano snapshot dello stato. MDK (Marmot Development Kit) fornisce l'implementazione MLS. Il progetto indica lo stato alpha e sconsiglia l'uso per carichi di lavoro sensibili.

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr), la piattaforma di ridesharing decentralizzata con pagamenti Cashu, ha distribuito la [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6). Questo rilascio corregge problemi di accessibilità TalkBack e risolve bug in cui i driver scomparivano dalla lista nelle vicinanze quando si cambiava metodo di pagamento, o in cui il conteggio dei driver selezionati non si aggiornava quando i driver andavano offline.

La funzione "Send to All" è ora "Broadcast RoadFlare" con correzioni per i silenziosi fallimenti su installazioni fresche dei driver. Ridestr implementa l'escrow HTLC per pagamenti trustless delle corse e la sincronizzazione wallet [NIP-60](/it/topics/nip-60/) tra dispositivi.

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered), l'app di condivisione foto simile a Instagram per Android, ha distribuito la [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6) con ricerca utenti migliorata e riconnessione automatica ai relay ogni 60 secondi.

Costruita con Kotlin e Jetpack Compose, Unfiltered usa le binding rust-nostr e server compatibili con Blossom per l'hosting delle immagini. L'integrazione Amber ([NIP-55](/it/topics/nip-55/)) gestisce la gestione sicura delle chiavi. L'app mostra i post degli account seguiti in ordine cronologico senza algoritmi o pubblicità.

Due nuovi progetti di messaggistica e firma sono stati lanciati questa settimana.

### Burrow: Messaggistica MLS per Agenti AI

[Burrow](https://github.com/CentauriAgent/burrow) è un messenger che implementa il protocollo [Marmot](/it/topics/marmot/) per la comunicazione cifrata con MLS senza numeri di telefono o server centralizzati. Sia gli utenti umani che gli agenti AI possono partecipare.

Un daemon CLI in Rust puro con modalità di output JSONL gestisce l'integrazione con i sistemi automatizzati. Un'app Flutter cross-platform copre Android, iOS, Linux, macOS e Windows. Gli allegati media vengono cifrati insieme ai messaggi, e WebRTC gestisce le chiamate audio e video con server TURN configurabili.

Burrow stratifica la cifratura MLS sull'infrastruttura Nostr. L'identità usa le keypair Nostr (secp256k1) mentre i KeyPackage MLS vengono pubblicati come event di kind 443. I messaggi vengono cifrati con [NIP-44](/it/topics/nip-44/) come event di kind 445, e gli inviti di benvenuto usano il gift-wrapping [NIP-59](/it/topics/nip-59/).

L'integrazione con [OpenClaw](https://openclaw.ai) abilita la partecipazione degli agenti AI con accesso completo agli strumenti. Le liste di controllo degli accessi con log di audit gestiscono i permessi di contatto e gruppo. Questa combinazione posiziona Burrow per scenari di messaggistica agente-agente e agente-umano che richiedono cifratura di livello Signal su infrastruttura decentralizzata.

### Estensione Nostria Signer

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) è un'estensione browser basata su Chromium che fornisce gestione di vault e identità per gli utenti Nostr.

Vault multipli contenenti account multipli permettono agli utenti di organizzare le identità per contesti diversi. L'internazionalizzazione include il supporto alle lingue RTL. Costruita con Angular e TypeScript (79,2% del codebase), funziona sia come estensione browser che come Progressive Web App.

Nostria Signer implementa [NIP-07](/it/topics/nip-07/) per la firma tramite estensione browser, permettendo ai client Nostr web di richiedere firme degli event senza accedere direttamente alle chiavi private. La migrazione automatica del wallet gestisce gli aggiornamenti distribuiti attraverso il Chrome Web Store. Gli utenti possono anche fare il sideload dalla cartella `dist/extension`.

Gli sviluppatori sottolineano lo stato sperimentale: gli utenti devono gestire le proprie frasi di recupero segrete poiché gli sviluppatori non possono ripristinare l'accesso alle chiavi perse.

## Aggiornamenti dei Progetti

### Formstr Migra alla Nuova Organizzazione

[Formstr](https://github.com/formstr-hq/nostr-forms), l'alternativa a Google Forms su Nostr, ha migrato il suo repository da `abh3po/nostr-forms` all'organizzazione `formstr-hq`. Questo beneficiario di una grant OpenSats continua lo sviluppo nella nuova posizione.

### PR Aperte di Rilievo

Lavori in corso nei progetti Nostr:

- **Damus Outbox Model** ([PR #3602](https://github.com/damus-io/damus/pull/3602)): Piano di implementazione per il modello relay gossip/outbox su iOS. Questo cambiamento architetturale migliora la consegna dei messaggi pubblicando ai relay dove i destinatari leggono effettivamente.

- **Notedeck Cross-Platform Notifications** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296)): Sistema di notifiche nativo per il client desktop Damus che copre Android FCM, macOS e Linux.

- **NDK Cashu v3 Upgrade** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)): Aggiorna l'integrazione wallet del Nostr Development Kit a cashu-ts v3.

- **Zeus Cashu Offline** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742)): Invio e ricezione ecash offline per il wallet Lightning Zeus.

- **Shopstr Encrypted Digital Delivery** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231)): Aggiunge la consegna cifrata per i beni digitali con supporto al peso dinamico per gli articoli fisici.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti questa settimana:**

- **[NIP-85 Scoperta dei Provider di Servizi](https://github.com/nostr-protocol/nips/pull/2223)**: La specifica [NIP-85](/it/topics/nip-85/) include ora indicazioni su come i client scoprono i provider di trusted assertion. Quando un client necessita di punteggi [Web of Trust](/it/topics/web-of-trust/) o altre metriche calcolate, può interrogare i relay per gli annunci kind 30085 da provider che l'utente già segue o di cui si fida.

- **[NIP-29 Rimuove i Gruppi Non Gestiti](https://github.com/nostr-protocol/nips/pull/2229)**: La specifica dei gruppi chat [NIP-29](/it/topics/nip-29/) ha eliminato il supporto per i gruppi non gestiti (dove qualsiasi membro poteva aggiungere altri). Tutti i gruppi NIP-29 richiedono ora la gestione lato relay con ruoli admin espliciti, semplificando le implementazioni e riducendo i vettori di spam.

- **[NIP-11 Rimuove i Campi Deprecati](https://github.com/nostr-protocol/nips/pull/2231)**: I documenti di informazione relay [NIP-11](/it/topics/nip-11/) non includono più i campi deprecati `software` e `version`. Le implementazioni dovrebbero rimuoverli dalle proprie risposte.

- **[NIP-39 Sposta i Tag di Identità](https://github.com/nostr-protocol/nips/pull/2227)**: Le rivendicazioni di identità esterna (tag `i` di [NIP-39](/it/topics/nip-39/) per GitHub, Twitter, ecc.) si sono spostate dai profili kind 0 a event kind 30382 dedicati. Questo separa la verifica dell'identità dai metadata del profilo.

**Avanzamento dei NIP per Agenti AI:**

Quattro NIP focalizzati sull'AI continuano lo sviluppo attivo. Da [quando li abbiamo coperti la settimana scorsa](/it/newsletters/2026-02-18-newsletter/#arrivano-le-proposte-di-nip-per-agenti-ai):

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)** (aggiornato il 19 feb): Definisce l'identità degli agenti con kind 4199 per le definizioni degli agenti e kind 4201 per i prompt ("nudge"). Gli agenti possono referenziare i metadata dei file [NIP-94](/it/topics/nip-94/) per descrizioni estese.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)** (aggiornato il 18 feb): Standardizza la messaggistica conversazionale con sette kind di event effimeri (25800-25806) per stato, delta di streaming, prompt, risposte, chiamate agli strumenti, errori e cancellazione. Gli event kind 31340 "AI Info" permettono agli agenti di pubblicizzare modelli e capacità supportate.

- **[NIP-AC: DVM Agent Coordination](https://github.com/nostr-protocol/nips/pull/2228)** (aperto il 18 feb): Estende [NIP-90](/it/topics/nip-90/) per i flussi di lavoro autonomi degli agenti. Aggiunge heartbeat per la scoperta degli agenti, recensioni dei job per il tracciamento della qualità, escrow dei dati per l'impegno sui risultati, catene di flusso di lavoro per pipeline multi-step e bidding in sciame per la selezione competitiva dei provider. Un'implementazione di riferimento gira su 2020117.xyz.

- **[NIP-AD: MCP Server Announcements](https://github.com/nostr-protocol/nips/pull/2221)** (aperto il 12 feb): Standardizza l'annuncio dei server e delle skill del Model Context Protocol su Nostr. Già in uso sulla piattaforma TENEX.

**Altre PR Aperte:**

- **[NIP-144: Service Authorization Protocol](https://github.com/nostr-protocol/nips/pull/2232)**: Definisce come i client dimostrano identità e permessi ai provider di servizi su Nostr.

- **[NIP-DC: Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**: alexgleason propone di integrare Webxdc (applicazioni web decentralizzate) con gli event Nostr.

## NIP Deep Dive: NIP-55 (Applicazione Signer Android)

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md) definisce come i client Nostr Android richiedono operazioni crittografiche da applicazioni signer dedicate. Con [White Noise v0.3.0](#white-noise-v030) e [Unfiltered v1.0.6](#unfiltered-v106) che aggiungono entrambi il supporto ad Amber questa settimana, il protocollo di firma Android merita un esame.

**Canali di Comunicazione:**

NIP-55 abilita la firma inter-app attraverso due meccanismi. Gli Intent forniscono l'approvazione manuale dell'utente con feedback visivo per operazioni una tantum. I Content Resolver abilitano la firma automatizzata quando gli utenti concedono permessi persistenti, permettendo alle app di firmare in background senza prompt ripetuti.

La comunicazione usa lo schema URI personalizzato `nostrsigner:`. Un client avvia il contatto con:

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**Operazioni Supportate:**

La specifica definisce sette metodi crittografici: firma degli event (`sign_event`), recupero della chiave pubblica (`get_public_key`), cifratura/decifratura [NIP-04](/it/topics/nip-04/), cifratura/decifratura [NIP-44](/it/topics/nip-44/) e decifratura degli event zap (`decrypt_zap_event`).

**Modello di Permessi:**

I client chiamano `get_public_key` una volta per stabilire una relazione di fiducia, ricevendo il nome del pacchetto del signer e la pubkey dell'utente. La specifica impone che i client salvino questi valori e non chiamino mai più `get_public_key`, prevenendo attacchi di fingerprinting.

Per le richieste di firma, gli utenti possono approvare una volta o concedere "ricorda la mia scelta" per le operazioni in background. Se gli utenti rifiutano ripetutamente le operazioni, il signer restituisce uno stato "rejected", prevenendo prompt ripetuti.

**Implementazioni:**

[Amber](https://github.com/greenart7c3/amber) è il signer NIP-55 principale per Android. I client che supportano NIP-55 includono [Amethyst](https://github.com/vitorpamplona/amethyst), [White Noise](#white-noise-v030), [Unfiltered](#unfiltered-v106) e altri. Le applicazioni web non possono ricevere direttamente le risposte del signer e devono usare URL di callback o operazioni con gli appunti.

**Relazione con gli Altri NIP di Firma:**

NIP-55 completa [NIP-07](/it/topics/nip-07/) (estensioni browser) e [NIP-46](/it/topics/nip-46/) (firma remota sui relay). Dove NIP-07 gestisce i browser desktop e NIP-46 gestisce la firma cross-device, NIP-55 fornisce integrazione nativa Android con latenza minima.

## NIP Deep Dive: NIP-60 (Wallet Cashu)

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) definisce come i wallet ecash [Cashu](/it/topics/cashu/) memorizzano lo stato sui relay Nostr, abilitando la sincronizzazione del wallet tra applicazioni. Con [Ridestr v0.2.6](#ridestr-v026) che usa NIP-60 per la sincronizzazione del wallet tra dispositivi, il protocollo merita un esame.

**Tipi di Event:**

NIP-60 usa quattro tipi di event. Il kind 17375 sostituibile memorizza la configurazione del wallet inclusi gli URL dei mint e una chiave privata dedicata per ricevere pagamenti ecash P2PK. Gli event token (kind 7375) contengono prove crittografiche non spese, mentre la cronologia delle spese (kind 7376) registra le transazioni per la trasparenza dell'utente. Un kind 7374 opzionale traccia le quote di pagamento del mint.

**Architettura del Wallet:**

Lo stato del wallet risiede sui relay, rendendolo accessibile tra le applicazioni. L'event wallet di un utente contiene riferimenti cifrati ai mint Cashu e una chiave privata specifica per il wallet separata dall'identità Nostr dell'utente. Questa separazione è importante: la chiave wallet gestisce le operazioni ecash mentre la chiave Nostr gestisce le funzioni sociali.

```json
{
  "kind": 17375,
  "content": "<nip44-encrypted-wallet-config>",
  "tags": [["d", "cashu-wallet"]]
}
```

**Gestione delle Prove:**

Le prove Cashu sono strumenti al portatore. Una volta spesa, una prova diventa non valida. NIP-60 gestisce questo attraverso un meccanismo di rollover: durante la spesa, i client creano un nuovo event token con le prove non spese rimanenti ed eliminano l'originale tramite [NIP-09](/it/topics/nip-09/). Gli ID dei token distrutti vanno in un campo `del` per il tracciamento dello stato.

I client dovrebbero periodicamente validare le prove contro i mint per rilevare credenziali precedentemente spese. Sono consentiti event token multipli per mint, e gli event della cronologia delle spese aiutano gli utenti a tracciare le transazioni anche se sono facoltativi.

**Modello di Sicurezza:**

Tutti i dati sensibili usano la cifratura [NIP-44](/it/topics/nip-44/). La chiave privata del wallet non appare mai in chiaro. Poiché i relay memorizzano blob cifrati senza comprenderne il contenuto, lo stato del wallet rimane privato anche su relay non fidati.

**Implementazioni:**

I wallet che supportano NIP-60 includono [Nutsack](https://github.com/gandlafbtc/nutsack) e [eNuts](https://github.com/cashubtc/eNuts). Client come [Ridestr](#ridestr-v026) usano NIP-60 per la sincronizzazione cross-device, permettendo agli utenti di ricaricare dal desktop e spendere dal mobile senza trasferimenti manuali.

---

È tutto per questa settimana. Stai costruendo qualcosa o hai notizie da condividere? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattaci via DM [NIP-17](/it/topics/nip-17/)</a> o trovaci su Nostr.
