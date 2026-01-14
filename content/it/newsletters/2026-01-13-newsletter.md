---
title: 'Nostr Compass #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** Bitchat viene sottoposto a un audit di sicurezza professionale da Cure53, la stessa azienda che ha verificato Signal e [NIP-44](/it/topics/nip-44/), con oltre 17 PR già integrate per correggere vulnerabilità critiche. [NIP-71](/it/topics/nip-71/) è stato approvato, portando nel protocollo gli event video indirizzabili. Una NIP sulla crittografia post-quantistica apre la discussione sulla protezione futura di Nostr contro gli attacchi quantistici. Amethyst v1.05.0 introduce le liste di segnalibri, le note vocali e una versione desktop preliminare, mentre Nostur v1.25.3 migliora i DM [NIP-17](/it/topics/nip-17/) con reazioni e risposte. Per quanto riguarda le librerie, rust-nostr estende il supporto [NIP-62](/it/topics/nip-62/) ai backend SQLite e LMDB, e NDK corregge un bug nel tracciamento delle subscription.

## Notizie

### Bitchat Completa l'Audit di Sicurezza Cure53

Bitchat, il messenger crittografato per iOS che combina Nostr con Cashu, è stato sottoposto a un audit di sicurezza professionale da Cure53, una delle aziende di sicurezza più rispettate del settore. Cure53 ha precedentemente verificato Signal, Mullvad VPN e soprattutto la specifica di crittografia [NIP-44](/it/topics/nip-44/) che è alla base della messaggistica privata moderna su Nostr.

L'audit ha rilevato oltre 12 problemi di sicurezza (BCH-01-002 fino a BCH-01-013). Il team di Bitchat ha risposto con oltre 17 pull request. Le correzioni principali includono:

**Cancellazione dei Secret DH del Noise Protocol** - [PR #928](https://github.com/permissionlesstech/bitchat/pull/928) corregge sei punti in cui i secret condivisi Diffie-Hellman non venivano azzerati dopo lo scambio delle chiavi, ripristinando le garanzie di forward secrecy. Quando i secret persistono in memoria più a lungo del necessario, un dump della memoria o un attacco cold boot potrebbero compromettere le comunicazioni passate.

**Verifica delle Firme** - Diverse PR rafforzano i percorsi di verifica crittografica, assicurando che i controlli di autenticità dei messaggi non possano essere aggirati tramite input malformati.

**Thread Safety** - [PR #929](https://github.com/permissionlesstech/bitchat/pull/929) aggiunge la sincronizzazione con barriere alle code delle ricevute di lettura in NostrTransport, prevenendo race condition che potrebbero causare corruzione dei dati o crash con alti volumi di messaggi.

**Sicurezza della Memoria** - [PR #920](https://github.com/permissionlesstech/bitchat/pull/920) ottimizza il deduplicatore di messaggi per migliori prestazioni con alto throughput di messaggi, evitando l'esaurimento della memoria.

**Validazione degli Input** - [PR #919](https://github.com/permissionlesstech/bitchat/pull/919) rafforza il parsing delle stringhe esadecimali per prevenire crash da input malformati, un vettore di attacco comune per denial-of-service.

Bitchat gestisce ecash Cashu, rendendo essenziale una revisione di sicurezza professionale. L'audit segue quello del [Marmot](/it/topics/marmot/) Protocol dello scorso anno e l'audit NIP-44 che ha verificato il layer di crittografia.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Approvate:**

- **[NIP-71](/it/topics/nip-71/)** - Event Video Indirizzabili ([#1669](https://github.com/nostr-protocol/nips/pull/1669)) introduce i kind 34235 (video orizzontale) e 34236 (video verticale) come event indirizzabili. Un tag `d` obbligatorio fornisce identificatori univoci, così i metadati video possono essere aggiornati senza ripubblicare l'intero event. Un tag `origin` opzionale traccia le fonti di importazione. Già implementato in Amethyst e nostrvine.

**PR Aperte:**

- **Crittografia Post-Quantistica** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) propone l'aggiunta di algoritmi crittografici resistenti ai computer quantistici in Nostr. La specifica introduce ML-DSA-44 e Falcon-512 per le firme digitali, mirando a "event di altissimo valore" come applicazioni e autorità piuttosto che singoli utenti. Mentre la crittografia simmetrica di [NIP-44](/it/topics/nip-44/) (ChaCha20) è resistente ai quantum, il suo scambio di chiavi usa secp256k1 ECDH che è vulnerabile all'algoritmo di Shor. La proposta include ML-KEM per lo scambio di chiavi per colmare questa lacuna. Si tratta di una proposta in fase iniziale che apre la discussione sulla cripto-agilità per la sicurezza a lungo termine di Nostr.
- **BOLT12 per NIP-47** - Dopo 137 commenti e un'ampia discussione, la comunità ha deciso che le offer BOLT12 meritano una specifica propria piuttosto che estendere [NIP-47](/it/topics/nip-47/). Le offer BOLT12 offrono miglioramenti significativi rispetto alle invoice BOLT11, inclusa la riusabilità, migliore privacy attraverso i blinded path e informazioni opzionali sul pagatore. La nuova NIP definirà metodi come `make_offer`, `pay_offer` e `list_offers` per le implementazioni Nostr Wallet Connect.
- **NIP per Tracce Audio** - [PR #1043](https://github.com/nostr-protocol/nips/pull/1043) propone i kind 32100 per tracce musicali e 32101 per episodi podcast, dando ai contenuti audio lo stesso trattamento di prima classe che NIP-71 fornisce per i video. Attualmente, le piattaforme audio come Wavlake, Zapstr e Stemstr usano ciascuna formati di event proprietari, frammentando l'ecosistema. Uno standard comune permetterebbe l'interoperabilità così gli utenti potrebbero scoprire e riprodurre audio da qualsiasi client compatibile.
- **NIP-A3 Target di Pagamento Universali** - [PR #2119](https://github.com/nostr-protocol/nips/pull/2119) propone event di kind 10133 che usano URI `payto:` RFC-8905 per esporre opzioni di pagamento su reti multiple. Invece di creare kind di event separati per Bitcoin, Lightning, Cashu o sistemi di pagamento tradizionali, questa astrazione permette ai client di interpretare tag standardizzati e invocare handler di pagamento nativi. L'approccio è a prova di futuro poiché i nuovi metodi di pagamento necessitano solo di uno schema URI `payto:`.

## Approfondimento NIP: NIP-51 e NIP-65

Questa settimana trattiamo due NIP che memorizzano le preferenze utente: NIP-51 per organizzare i contenuti e NIP-65 per organizzare le connessioni ai relay. Entrambe usano event sostituibili, il che significa che ogni nuova pubblicazione sovrascrive la versione precedente.

### [NIP-51](/it/topics/nip-51/): Liste

[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) definisce diversi tipi di liste per organizzare riferimenti a event, utenti, hashtag e altri contenuti. Amethyst v1.05.0 aggiunge il supporto ai segnalibri, rendendo questo un buon momento per capire come funzionano le liste.

La specifica definisce diversi kind di liste, ciascuno con uno scopo diverso. Il kind 10000 è la vostra lista di silenziamento per nascondere utenti, thread o parole. Il kind 10001 fissa event da mettere in evidenza sul vostro profilo. Il kind 30003 memorizza i segnalibri, che è ciò che Amethyst ora supporta. Altri kind gestiscono set di following (30000), collezioni di articoli curate (30004), interessi per hashtag (30015) e set di emoji personalizzate (30030).

Le liste referenziano contenuti attraverso tag. Una lista di segnalibri usa tag `e` per event specifici e tag `a` per contenuti indirizzabili come articoli:

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

Il tag `d` fornisce un identificatore univoco, così potete mantenere più set di segnalibri come "saved-articles", "read-later" o "favorites" sotto lo stesso kind.

Le liste supportano sia elementi pubblici che privati. Gli elementi pubblici appaiono nell'array dei tag, visibili a chiunque recuperi l'event. Gli elementi privati vanno nel campo `content`, crittografati usando [NIP-44](/it/topics/nip-44/) verso voi stessi. Questa doppia struttura vi permette di mantenere segnalibri pubblici aggiungendo note private, o mantenere una lista di silenziamento senza rivelare chi avete silenziato. Per crittografare verso voi stessi, usate NIP-44 con la vostra pubkey come destinatario.

I kind della serie 10000 sono sostituibili, il che significa che i relay mantengono un solo event per pubkey. La serie 30000 è sostituibile parametrizzata, permettendo un event per combinazione di pubkey e tag `d`. In entrambi i casi, aggiornare una lista significa pubblicare una sostituzione completa; non potete inviare modifiche incrementali. I client dovrebbero preservare i tag sconosciuti quando modificano le liste per evitare di sovrascrivere dati aggiunti da altre applicazioni.

### [NIP-65](/it/topics/nip-65/): Metadati Lista Relay

[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) definisce event di kind 10002 che pubblicizzano quali relay un utente preferisce per leggere e scrivere. Questo aiuta altri utenti e client a trovare i vostri contenuti.

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

Ogni tag `r` contiene un URL del relay e un marcatore opzionale. Un marcatore `write` designa la vostra outbox: relay dove pubblicate i vostri contenuti. Un marcatore `read` designa la vostra inbox: relay dove controllate menzioni, risposte e tag. Omettere il marcatore indica entrambi.

Quando Alice vuole trovare i post di Bob, il suo client recupera il kind 10002 di Bob, estrae i suoi relay write (la sua outbox) e si iscrive lì. Quando Alice risponde a Bob, il suo client pubblica sui suoi relay read (la sua inbox) così lui vedrà la menzione. Questo routing consapevole dei relay è il "modello outbox", e distribuisce gli utenti su molti relay invece di concentrare tutti su pochi server centrali.

NIP-65 gestisce il routing dei contenuti pubblici, ma i messaggi privati usano una lista separata. [NIP-17](/it/topics/nip-17/) definisce il kind 10050 per i relay inbox dei DM, usando tag `relay` invece di tag `r`. Quando inviate a qualcuno un messaggio privato, i client cercano l'event kind 10050 del destinatario e pubblicano lì il messaggio crittografato gift-wrapped. Questa separazione mantiene il routing dei DM distinto dal routing dei contenuti pubblici, e permette agli utenti di specificare relay diversi per comunicazioni private rispetto a quelle pubbliche.

Il modello outbox migliora la resistenza alla censura poiché nessun singolo relay deve memorizzare o servire i contenuti di tutti. I client mantengono connessioni ai relay elencati negli event NIP-65 degli utenti seguiti, collegandosi dinamicamente a nuovi relay mentre scoprono nuovi account. NIP-65 complementa gli hint dei relay trovati in altre NIP. Quando taggate qualcuno con `["p", "pubkey", "wss://hint.relay"]`, l'hint dice ai client dove cercare quel riferimento specifico. NIP-65 fornisce la lista autorevole controllata dall'utente, mentre gli hint offrono scorciatoie incorporate nei singoli event.

Per migliori risultati, mantenete aggiornata la vostra lista di relay poiché voci obsolete vi rendono più difficili da trovare. La specifica raccomanda da due a quattro relay per categoria. Elencare troppi relay grava su ogni client che vuole recuperare i vostri contenuti, rallentando la loro esperienza e aumentando il carico di rete. I client memorizzano in cache gli event NIP-65 e li aggiornano periodicamente per rimanere al passo con le preferenze aggiornate degli utenti.

## Release

**Amethyst v1.05.0** - Il popolare client Android [rilascia un aggiornamento importante](https://github.com/vitorpamplona/amethyst/releases) con diverse funzionalità di rilievo. Le liste di segnalibri [NIP-51](/it/topics/nip-51/) kind 30003 permettono agli utenti di salvare post per riferimento futuro, sincronizzandosi tra client compatibili. Le note vocali ora funzionano nei DM e nei post regolari con visualizzazione della forma d'onda, selezione del media server e indicatori di progresso del caricamento. I punteggi [Web of Trust](/it/topics/web-of-trust/) sono ora visibili nell'interfaccia, aiutando gli utenti a capire come l'algoritmo valuta gli account relativamente al loro grafo sociale. La migrazione del database [Quartz](/it/topics/quartz/) migliora le prestazioni delle query come parte del lavoro Kotlin Multiplatform finanziato da OpenSats. Una release desktop preliminare porta Amethyst su Windows, macOS e Linux tramite Compose Multiplatform, condividendo lo stesso codebase dell'app Android. Nuovi flussi di onboarding per gli utenti facilitano l'esperienza per chi usa Nostr per la prima volta.

**Nostur v1.25.3** - Il client iOS e macOS [si concentra sulla messaggistica privata](https://github.com/nostur-com/nostur-ios-public/releases) con miglioramenti a [NIP-17](/it/topics/nip-17/). Le conversazioni DM ora supportano reazioni e risposte, portando l'interattività dei post pubblici nei messaggi crittografati. La vista delle conversazioni è stata rielaborata con un migliore threading così gli scambi multi-messaggio sono più facili da seguire, e i timestamp mostrano "tempo fa" nella lista DM per una scansione rapida. Gli utenti desktop ottengono layout multi-colonna per visualizzare feed o conversazioni multiple affiancate. Il supporto al remote signer [NIP-46](/it/topics/nip-46/) permette agli utenti di mantenere le loro chiavi private in app di firma dedicate come Amber o nsec.app. Correzioni aggiuntive ripristinano la funzionalità DM su iOS 15 e iOS 16, risolvono ritardi nelle notifiche e aggiungono la possibilità di configurare quali relay ricevono i DM pubblicati.

## Modifiche notevoli a codice e documentazione

*Queste sono pull request aperte e lavori in fase iniziale, perfetti per ricevere feedback prima del merge. Se qualcosa vi interessa, considerate di fare review o commentare!*

### Citrine (Relay Android)

[PR #89](https://github.com/greenart7c3/Citrine/pull/89) corregge una vulnerabilità SQL injection nell'app relay personale Android. Il problema permetteva a dati di event malformati di eseguire query arbitrarie sul database, un difetto grave per qualsiasi app che memorizza ed elabora input non fidati. La correzione sanifica correttamente tutte le operazioni sul database usando query parametrizzate. Non è ancora stata taggata una release, quindi gli utenti dovranno aspettare la prossima versione o compilare dal sorgente. [PR #90](https://github.com/greenart7c3/Citrine/pull/90) ottimizza le prestazioni delle query ContentProvider con filtraggio e paginazione a livello di database, riducendo la latenza quando app esterne come Amethyst accedono al database di event di Citrine attraverso il layer di comunicazione inter-processo di Android.

### rust-nostr (Libreria)

Il supporto a [NIP-62](/it/topics/nip-62/) (Richieste di Scomparsa) si sta espandendo attraverso i backend di database di rust-nostr. [PR #1180](https://github.com/rust-nostr/nostr/pull/1180), integrata due settimane fa, ha aggiunto il supporto NIP-62 a SQLite, gestendo le richieste di scomparsa `ALL_RELAYS` poiché il layer del database non conosce URL specifici dei relay. [PR #1210](https://github.com/rust-nostr/nostr/pull/1210) estende questo al backend LMDB, assicurando che le richieste di scomparsa siano persistite su disco e sopravvivano ai riavvii del relay. Un'implementazione IndexedDB per ambienti browser è anche in corso. Insieme, queste modifiche danno agli sviluppatori un supporto NIP-62 coerente attraverso SQLite, LMDB e presto lo storage del browser.

### NDK (Nostr Development Kit)

[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) corregge un bug nel sistema di tracciamento seenEvents. Il problema causava che certi pattern di subscription marcassero erroneamente gli event come già visti, portando a contenuti mancati quando gli utenti aprivano nuove subscription o si riconnettevano ai relay. La correzione assicura che gli event siano tracciati accuratamente attraverso i cicli di vita delle subscription, il che è particolarmente importante per applicazioni che si iscrivono e cancellano dinamicamente in base alla navigazione dell'utente. NDK è passato alla beta.70 con questa correzione inclusa.

### Damus (iOS)

[PR #3515](https://github.com/damus-io/damus/pull/3515) corregge un crash all'avvio che colpiva gli utenti iOS 17. Il problema derivava da un overflow aritmetico in `NdbUseLock`, una classe di fallback usata perché i Mutex di Swift non sono disponibili su iOS 17. La correzione sostituisce l'approccio di sincronizzazione precedente con `NSLock`, che è disponibile su iOS 17 e gestisce correttamente le race condition rimanenti. Gli utenti iOS 18+ non erano colpiti poiché hanno accesso all'implementazione nativa del Mutex Swift.

Separatamente, un gruppo di miglioramenti per gli articoli longform è arrivato tramite [PR #3509](https://github.com/damus-io/damus/pull/3509). Le barre di progresso della lettura tracciano la vostra posizione attraverso gli articoli, i tempi di lettura stimati appaiono nelle anteprime, e la modalità seppia con impostazioni di altezza riga regolabili forniscono una lettura più confortevole. La modalità focus nasconde automaticamente la chrome di navigazione durante lo scorrimento verso il basso e la ripristina al tocco, riducendo il disordine visivo per una lettura senza distrazioni. Diverse correzioni affrontano la visualizzazione delle immagini nei contenuti markdown e assicurano che gli articoli si aprano dall'inizio piuttosto che a metà.

### Zap.stream (Live Streaming)

L'integrazione della chat di YouTube e Kick collega i messaggi dalle piattaforme di streaming esterne a Nostr. Gli streamer che trasmettono in multicast su YouTube, Kick e Zap.stream possono ora vedere tutti i messaggi della chat in una vista unificata, con i messaggi da ogni piattaforma che appaiono accanto ai commenti nativi Nostr. Questo rimuove un importante punto di attrito per i creator che vogliono usare Nostr per lo streaming ma non possono abbandonare il pubblico sulle piattaforme consolidate. L'integrazione mostra da quale piattaforma ha origine ogni messaggio e gestisce il flusso di autenticazione per connettere account esterni.

### Chachi (Gruppi NIP-29)

Il client di chat di gruppo [NIP-29](/it/topics/nip-29/) ha integrato sei PR questa settimana. Un aggiornamento di sicurezza affronta [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89), una vulnerabilità XSS in react-router che potrebbe abilitare attacchi di open redirect; la correzione aggiorna a react-router-dom 6.30.0. [PR #92](https://github.com/purrgrammer/chachi/pull/92) aggiunge il caricamento paginato dei messaggi per le chat di gruppo, così le conversazioni lunghe si caricano incrementalmente piuttosto che tutte insieme. [PR #91](https://github.com/purrgrammer/chachi/pull/91) corregge diversi bug NIP-29 inclusa una race condition che causava nomi di gruppo vuoti al caricamento iniziale e liste di partecipanti non definite che facevano crashare le viste dei membri. La copertura delle traduzioni ora copre tutte le 31 lingue supportate con 1060 chiavi ciascuna.

### 0xchat (Messaggistica)

Il client di messaggistica stile Telegram ha migliorato la conformità a [NIP-55](/it/topics/nip-55/) salvando correttamente i nomi dei pacchetti dei signer quando si usano app di firma esterne, correggendo problemi in cui l'app perdeva traccia di quale signer usare dopo i riavvii. La gestione delle risposte NIP-17 ora include correttamente il tag `e` per il threading, assicurando che le risposte appaiano nel contesto di conversazione corretto attraverso i client. Le ottimizzazioni delle prestazioni affrontano il lag di scorrimento nelle liste di messaggi, un punto dolente comune quando si caricano cronologie di chat lunghe. Il salvataggio automatico delle bozze previene la perdita di messaggi se navigate via durante la composizione, e le opzioni di archiviazione file ora includono endpoint predefiniti FileDropServer e BlossomServer.

### Primal (iOS)

Il supporto al remote signer [NIP-46](/it/topics/nip-46/) arriva su iOS tramite [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184), completando il rollout cross-platform iniziato con Android diverse settimane fa. Gli utenti possono ora mantenere le loro chiavi private in servizi bunker dedicati come nsec.app o istanze nsecBunker self-hosted, connettendosi attraverso relay Nostr per firmare event senza esporre le chiavi all'app client. Questa separazione migliora la postura di sicurezza per gli utenti che vogliono usare le funzionalità di Primal mantenendo pratiche di gestione delle chiavi più rigorose. L'implementazione include la scansione di codici QR per gli URI di connessione al bunker e gestisce il flusso richiesta/risposta NIP-46 attraverso messaggi relay crittografati.

---

Questo è tutto per questa settimana. State costruendo qualcosa? Avete notizie da condividere? Volete che copriamo il vostro progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattateci tramite DM NIP-17</a> o trovateci su Nostr.
