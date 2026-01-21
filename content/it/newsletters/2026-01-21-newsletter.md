---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** Bitchat sostituisce C Tor con l'implementazione Rust Arti per una maggiore affidabilità e prestazioni. nostrdb-rs ottiene query fold streaming che abilitano operazioni di database a zero allocazioni. Listr riceve un importante refactoring con la migrazione a NDK 3 beta e manutenzione assistita da AI dopo un anno di inattività. Zeus spedisce 17 PR unite focalizzate su correzioni [NIP-47](/it/topics/nip-47/) (Nostr Wallet Connect per il controllo remoto di Lightning) e miglioramenti Cashu, mentre Primal Android aggiunge flussi di backup del wallet e supporto [NIP-92](/it/topics/nip-92/) (dimensioni dei media per rapporti di aspetto corretti). Una nuova bozza di NIP propone [Trusted Relay Assertions](/it/topics/trusted-relay-assertions/) per la valutazione standardizzata della fiducia nei relay.

## Notizie

### Bitchat Migra ad Arti Rust per il Supporto Tor

Bitchat è migrato da C Tor ad [Arti](https://gitlab.torproject.org/tpo/core/arti), l'implementazione Rust del protocollo Tor. [PR #958](https://github.com/permissionlesstech/bitchat/pull/958) rimuove la dipendenza da C Tor e integra Arti, portando garanzie di sicurezza della memoria e maggiore affidabilità. Il cambiamento elimina i tentativi di riattivazione dormiente che causavano riavvii del servizio in primo piano, un problema di lunga data con l'implementazione C.

**Cosa significa per gli utenti:** Messaggistica crittografata più stabile con meno disconnessioni, specialmente su dispositivi mobili. L'implementazione Rust riduce i rischi di crash e il consumo della batteria dai tentativi di riconnessione costanti.

Arti è una riscrittura completa di Tor in Rust, sviluppata dal Tor Project per fornire maggiore sicurezza attraverso la sicurezza della memoria e un'integrazione più facile nelle applicazioni. Per Bitchat, le proprietà di sicurezza della memoria riducono la superficie di attacco durante la gestione di messaggi crittografati e connessioni relay. La migrazione segue il recente [audit di sicurezza Cure53](/it/newsletters/2026-01-13-newsletter/#bitchat-completes-cure53-security-audit) del team (trattato nella Newsletter #5), continuando i loro miglioramenti di sicurezza.

Il PR introduce anche una copertura di test completa per ChatViewModel e BLEService, rimuove codice morto e stabilizza la suite di test. I miglioramenti di affidabilità della mesh Bluetooth Low Energy accompagnano le modifiche Tor, affrontando i fallimenti di trasferimenti grandi. Insieme, questi cambiamenti migliorano la resilienza di Bitchat per scenari di rete mesh offline dove Tor fornisce connettività internet insieme alla comunicazione BLE locale.


### Listr Rivitalizzato con Manutenzione Potenziata dall'AI

JeffG ha annunciato un importante refactoring di [Listr](https://github.com/erskingardner/listr), l'applicazione di gestione liste Nostr disponibile su [listr.lol](https://listr.lol), dopo che il progetto era rimasto inattivo per oltre un anno. Usando l'assistenza dell'AI, ha completato un aggiornamento completo includendo la migrazione a [NDK](https://github.com/nostr-dev-kit/ndk) 3 beta, aggiornamenti alle ultime versioni di Svelte e Vite, e tutte le dipendenze portate alla versione corrente. Il refactoring aggiunge supporto di prima classe per i pacchetti di following, implementa la paginazione per liste che superano i 50 elementi e corregge numerosi bug che si erano accumulati durante il periodo di inattività.

**Cosa significa per gli utenti:** Listr è tornato online con prestazioni migliorate e nuove funzionalità per gestire liste di following, collezioni di contenuti e curatela di argomenti. La correzione della paginazione rende effettivamente utilizzabili le liste grandi.

JeffG ha notato che senza l'assistenza dell'AI, questo lavoro di manutenzione probabilmente non sarebbe mai avvenuto, impedendo che il progetto venisse abbandonato. Listr abilita la curatela dei contenuti su Nostr, permettendo agli utenti di creare, gestire e condividere liste di profili, argomenti e risorse. L'aggiornamento mantiene l'applicazione compatibile con gli standard Nostr correnti e le aspettative dei client man mano che la gestione delle liste diventa più centrale per la scoperta dei contenuti sul protocollo.


## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Unite:**

- **[NIP-29](/it/topics/nip-29/)** (Gruppi basati su relay) - Chiarimento Chiave Relay ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - unito) chiarisce che la chiave relay è l'URL del relay stesso, non una pubkey. La specifica ora afferma esplicitamente "La chiave relay è l'URL WebSocket del relay (es. wss://groups.example.com)" per evitare confusione. Questo influisce su come i client identificano quale relay ospita un determinato gruppo, garantendo che i gruppi siano correttamente attribuiti ai loro relay ospitanti.

**PR Aperte e Discussioni:**

- **Trusted Relay Assertions** - Una bozza di NIP propone di standardizzare il punteggio di fiducia nei relay attraverso eventi kind 30385 contenenti punteggi di fiducia (0-100) calcolati da metriche [NIP-66](/it/topics/nip-66/) (scoperta e monitoraggio relay), reputazione dell'operatore e segnalazioni degli utenti. La specifica divide la fiducia in componenti di affidabilità (uptime, latenza), qualità (TLS, documentazione, verifica operatore) e accessibilità (giurisdizione, barriere, rischio sorveglianza). La verifica dell'operatore include firme crittografiche tramite [NIP-11](/it/topics/nip-11/) (documenti informativi relay), record TXT DNS e file .well-known. Gli utenti dichiarano i fornitori di asserzioni fidati tramite eventi kind 10385, permettendo ai client di interrogare più fornitori per prospettive diverse. La proposta complementa la scoperta [NIP-66](/it/topics/nip-66/) con la valutazione, aiutando [NIP-46](/it/topics/nip-46/) (firma remota/Nostr Connect) a valutare l'affidabilità dei relay negli URI di connessione.

- **Crittografia Post-Quantistica** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) (aperta) continua ad evolversi da quando la [Newsletter #5](/it/newsletters/2026-01-13-newsletter/#nip-updates) ha introdotto la proposta per algoritmi resistenti ai computer quantistici. La discussione di questa settimana si è concentrata sui dettagli di implementazione per la crypto-agility: come i client gestiscono le firme doppie durante la migrazione, la compatibilità retroattiva per i client più vecchi e le implicazioni prestazionali delle firme quantistiche resistenti più grandi. I contributori hanno dibattuto se imporre solo ML-DSA-44 o supportare più algoritmi (ML-DSA-44, Falcon-512, Dilithium) per flessibilità. Il consenso propende verso un approccio graduale: firme quantistiche opzionali inizialmente, diventando obbligatorie solo dopo un ampio supporto dei client e l'emergere di una reale minaccia quantistica.


## Approfondimento NIP: NIP-11 e NIP-66

Questa settimana esaminiamo due NIP che lavorano insieme per abilitare la scoperta e valutazione dei relay: NIP-11 definisce come i relay si descrivono, e NIP-66 standardizza come misuriamo il comportamento dei relay. Insieme formano la base per i sistemi di valutazione della fiducia nei relay.

### [NIP-11](/it/topics/nip-11/): Documento Informativo Relay

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md) definisce un documento JSON che i relay servono via HTTP per descrivere le loro capacità, politiche e informazioni sull'operatore. Quando un client si connette a `wss://relay.example.com`, può recuperare `https://relay.example.com` (sostituendo `wss://` con `https://`) per ottenere il documento informativo del relay.

Il documento usa la negoziazione standard del contenuto HTTP con l'header `Accept: application/nostr+json`. Questo permette ai relay di servire il loro sito web normale ai browser mentre forniscono metadati leggibili dalle macchine ai client Nostr. La risposta include il nome del software relay e la versione, informazioni di contatto dell'operatore (pubkey, email, contatto alternativo), NIP supportati e parametri operativi come requisiti di pagamento o restrizioni di contenuto.

Importante notare che i documenti NIP-11 di base sono JSON non firmati serviti via HTTPS, affidandosi esclusivamente ai certificati TLS per l'autenticità. Questo significa che chiunque controlli il server web del relay può modificare il documento, rendendo non verificabili le affermazioni dell'operatore. La proposta Trusted Relay Assertions affronta questa lacuna introducendo attestazioni firmate attraverso il campo `self` pubkey di un relay, abilitando la prova crittografica dell'identità dell'operatore in modo simile a come i relay usano eventi firmati per i meccanismi di autenticazione.

```json
{
  "name": "relay.example.com",
  "description": "Un relay pubblico per uso generale",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
```

L'oggetto `limitation` indica ai client quali vincoli applica il relay. `max_message_length` limita la dimensione del frame WebSocket, `max_subscriptions` limita le sottoscrizioni REQ concorrenti per connessione, `max_filters` limita i filtri per REQ, e `max_limit` vincola quanti eventi può richiedere un singolo filtro. Questi parametri aiutano i client ad adattare il loro comportamento alle capacità del relay, evitando disconnessioni dal superamento dei limiti.

Le informazioni di pagamento appaiono in `fees` e `payments_url`. I relay possono addebitare per l'ammissione (accesso una tantum), l'abbonamento (accesso ricorrente) o la pubblicazione (tariffe per evento). Il `payments_url` punta ai dettagli sui metodi di pagamento, tipicamente fatture Lightning o mint ecash. I relay a pagamento usano questi campi per comunicare i prezzi prima che i client tentino l'autenticazione.

L'array `supported_nips` permette ai client di scoprire le capacità del relay. Se un relay elenca [NIP-50](/it/topics/nip-50/), i client sanno di poter inviare query di ricerca full-text. Se appare [NIP-42](/it/topics/nip-42/), i client dovrebbero aspettarsi challenge di autenticazione. Questa pubblicità dichiarativa delle capacità abilita il miglioramento progressivo: i client possono usare funzionalità avanzate dove disponibili mentre degradano elegantemente su relay con supporto limitato.

Le informazioni sull'operatore costruiscono responsabilità. Il campo `pubkey` identifica l'operatore del relay su Nostr, abilitando la comunicazione diretta tramite DM [NIP-17](/it/topics/nip-17/) o menzioni pubbliche. L'`contact` email fornisce un fallback fuori protocollo. Insieme, questi campi aiutano gli utenti a raggiungere gli operatori per segnalazioni di abuso, richieste di accesso o problemi tecnici.

I documenti [NIP-11](/it/topics/nip-11/) sono auto-riportati: i relay descrivono cosa affermano di supportare, non necessariamente cosa fanno effettivamente. Qui è dove NIP-66 diventa importante.

### [NIP-66](/it/topics/nip-66/): Scoperta Relay e Monitoraggio Liveness

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) standardizza la pubblicazione di dati di monitoraggio relay su Nostr. I servizi di monitoraggio testano continuamente i relay per disponibilità, latenza, conformità al protocollo e NIP supportati. Pubblicano i risultati come eventi kind 30166, fornendo lo stato relay in tempo reale indipendente dall'auto-segnalazione del relay.

I monitor controllano la disponibilità del relay connettendosi e inviando sottoscrizioni di test. Le misurazioni di latenza tracciano il tempo di connessione, il tempo di risposta alle sottoscrizioni e il ritardo di propagazione degli eventi. I test di conformità al protocollo verificano che il comportamento del relay corrisponda alle specifiche, individuando bug di implementazione o deviazioni intenzionali. La verifica del supporto NIP va oltre le affermazioni [NIP-11](/it/topics/nip-11/) testando effettivamente se le funzionalità pubblicizzate funzionano correttamente.

```json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\"last_check\": 1736784000, \"checks\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
```

Il tag `d` contiene l'URL del relay, rendendo questo un evento sostituibile parametrizzato. Ogni monitor pubblica un evento per relay, aggiornato al cambiare delle misurazioni. Più monitor possono tracciare lo stesso relay, fornendo ridondanza e validazione incrociata. I client interrogano più pubkey di monitor per ottenere prospettive diverse sulla salute del relay.

I tag round-trip time (rtt) misurano la latenza per diverse operazioni. `rtt open` traccia l'instaurazione della connessione WebSocket, `rtt read` misura il tempo di risposta alle sottoscrizioni, e `rtt write` testa la velocità di pubblicazione degli eventi. Tutti i valori sono in millisecondi. I client usano queste metriche per preferire relay a bassa latenza per operazioni sensibili al tempo o deprioritizzare relay lenti.

Il tag `nips` elenca il supporto NIP effettivamente verificato, non solo il supporto dichiarato. I monitor testano ogni NIP esercitando la sua funzionalità. Se un relay rivendica la ricerca [NIP-50](/it/topics/nip-50/) nel suo documento [NIP-11](/it/topics/nip-11/) ma le query di ricerca falliscono, i monitor ometteranno NIP-50 dalla lista verificata. Questo fornisce la verità di base sulle capacità del relay.

Le informazioni geografiche aiutano i client a selezionare relay vicini per una migliore latenza e resistenza alla censura. Il tag `geo` contiene il codice paese, il nome paese e la regione. Il tag `network` distingue i relay clearnet dai servizi nascosti Tor o endpoint I2P. Insieme, questi tag abilitano la diversità geografica: i client possono connettersi a relay in più giurisdizioni per resistere alla censura regionale.

I dati dei monitor alimentano i selettori di relay nei client, i siti web esploratori e la proposta Trusted Relay Assertions. Combinando documenti auto-riportati [NIP-11](/it/topics/nip-11/) con dati misurati [NIP-66](/it/topics/nip-66/) e asserzioni di fiducia calcolate, l'ecosistema si muove verso la selezione informata dei relay piuttosto che fare affidamento su default codificati o raccomandazioni di passa-parola.

## Rilasci

### 0xchat v1.5.3 - Funzionalità di Messaggistica Migliorate

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release) porta miglioramenti significativi al client di messaggistica Nostr stile Telegram. Il rilascio affronta problemi di conformità [NIP-55](/it/topics/nip-55/) (applicazione signer Android) che impedivano la corretta firma degli eventi attraverso signer esterni come Amber. La piena conformità significa che 0xchat ora delega correttamente le operazioni di firma, migliorando la sicurezza mantenendo le chiavi private isolate.

L'aggiornamento integra sia FileDropServer che BlossomServer come opzioni di archiviazione media predefinite, offrendo agli utenti ridondanza per i caricamenti di file. [Blossom](https://github.com/hzrd149/blossom) fornisce archiviazione indirizzata ai contenuti dove i file sono referenziati dai loro hash SHA-256, garantendo integrità e abilitando la deduplicazione sulla rete. Il salvataggio automatico delle bozze per Moments previene la perdita di dati quando si compone contenuto long-form, affrontando le lamentele degli utenti sui post persi durante i cambi di app o le interruzioni di connettività.

L'integrazione del wallet Cashu riceve una lucidatura con il filtraggio automatico delle prove che rimuove i token spesi dalla vista del wallet. Questo risolve la UX confusa dove gli utenti vedevano prove invalide insieme a ecash valido, rendendo inaffidabili i calcoli del saldo. Il filtraggio avviene lato client, mantenendo la privacy mentre migliora l'esperienza di pagamento per le transazioni peer-to-peer nelle chat.

### Amber v4.1.0 Pre-releases - Revisione UI

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1) fino a [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3) introducono un'interfaccia ridisegnata per il popolare signer di eventi Android. La schermata di login ora visualizza chiaramente quale applicazione sta richiedendo permessi di firma, affrontando la confusione degli utenti sui flussi di autorizzazione. La nuova schermata eventi fornisce un'ispezione dettagliata di quali dati le applicazioni vogliono firmare, permettendo agli utenti di prendere decisioni di sicurezza informate prima di approvare le operazioni.

La gestione dei permessi riceve attenzione significativa con un'interfaccia rinnovata che mostra esattamente quali capacità è stata concessa a ogni applicazione connessa. Gli utenti possono revocare permessi specifici senza disconnettersi completamente, abilitando il controllo a grana fine sulla delegazione della firma. I contatori relay rifattorizzati usando la libreria quartz aggiornata forniscono statistiche in tempo reale sul throughput degli eventi e le prestazioni dei relay. Le connessioni bunker [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) (Nostr Connect) ora mostrano messaggi di errore dettagliati quando le connessioni falliscono, sostituendo gli errori di timeout criptici con diagnostiche azionabili.

## Modifiche notevoli a codice e documentazione

*Queste sono pull request unite e sviluppi in fase iniziale che vale la pena tracciare. Alcuni sono funzionalità sperimentali che potrebbero evolversi prima del rilascio.*

### Zeus (Wallet Lightning con Nostr Wallet Connect)

Zeus ha unito 17 pull request questa settimana, rafforzando la sua posizione come implementazione [NIP-47](/it/topics/nip-47/) Nostr Wallet Connect leader. Le correzioni più significative affrontano problemi di consistenza dei dati e conformità al protocollo che stavano causando problemi di interoperabilità con i client Nostr.

**Correzione Cronologia Transazioni** - [PR #3542](https://github.com/ZeusLN/zeus/pull/3542) risolve un bug critico dove le liste transazioni NWC visualizzavano voci errate o duplicate. Il problema si verificava quando Zeus metteva in cache i dati delle transazioni senza gestire correttamente gli aggiornamenti degli eventi, causando agli utenti di vedere transazioni fantasma o pagamenti mancanti. La correzione implementa la deduplicazione corretta degli eventi e l'invalidazione della cache, garantendo che la cronologia delle transazioni rifletta accuratamente lo stato del nodo Lightning.

**Conformità al Protocollo** - [PR #3548](https://github.com/ZeusLN/zeus/pull/3548) affronta risposte `getInfo` incomplete che rompevano la compatibilità con i client che si aspettano la piena conformità NIP-47. Alcuni client Nostr crashavano quando ricevevano risposte parziali mancanti di campi come `block_height` o `network`. Il PR garantisce che tutti i campi richiesti ritornino con default sensati anche quando l'implementazione Lightning sottostante non li fornisce, migliorando la compatibilità di Zeus nell'ecosistema.

**Resilienza della Connessione** - [PR #3543](https://github.com/ZeusLN/zeus/pull/3543) implementa notifiche di timeout per connessioni Nostr bloccate. Precedentemente, gli utenti aspettavano indefinitamente quando le connessioni relay cadevano silenziosamente. Ora Zeus visualizza messaggi di timeout chiari dopo 30 secondi di inattività, permettendo agli utenti di riprovare o cambiare relay. [PR #3541](https://github.com/ZeusLN/zeus/pull/3541) aggiunge validazione backend per prevenire l'attivazione NWC su implementazioni Lightning incompatibili, individuando errori di configurazione prima che causino crash runtime.

**Race Condition Cashu** - [PR #3531](https://github.com/ZeusLN/zeus/pull/3531) corregge un bug di concorrenza nella gestione dei token Cashu dove operazioni di mint simultanee potevano corrompere il database dei token. La race condition si verificava quando più thread aggiornava i conteggi dei token senza un locking appropriato, risultando occasionalmente in saldi errati. La correzione aggiunge protezione mutex attorno alle sezioni critiche, garantendo aggiornamenti atomici allo stato dei token.

### Primal Android (Client)

Primal Android ha spedito 12 PR unite con miglioramenti significativi alla sicurezza del wallet e alla gestione dei media. L'implementazione del backup del wallet affronta una delle funzionalità più richieste, mentre il supporto NIP-92 migliora l'esperienza visiva nell'applicazione.

**Sistema di Backup Wallet** - Una serie di quattro PR ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848)) implementa una funzionalità completa di backup della seed phrase. Gli utenti possono ora esportare il loro mnemonico di 12 parole attraverso un flusso sicuro che previene screenshot, visualizza lo stato del backup nel dashboard del wallet e guida gli utenti esistenti attraverso la migrazione. L'implementazione segue gli standard BIP-39 e include validazione per prevenire che gli utenti perdano fondi a causa della registrazione errata della frase.

**Dimensioni Media (NIP-92)** - [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) implementa il supporto [NIP-92](/it/topics/nip-92/) per i corretti rapporti di aspetto di immagini e video. Senza metadati delle dimensioni, i client devono scaricare le immagini per determinare la loro dimensione, causando salti di layout mentre il contenuto si carica. NIP-92 aggiunge tag `dim` (come `["dim", "1920x1080"]`) agli eventi di metadati dei file, permettendo a Primal di riservare lo spazio corretto prima di scaricare i media. Questo elimina i reflow fastidiosi nelle gallerie di immagini e migliora le prestazioni percepite.

**Affidabilità Signer Remoto** - [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841) corregge problemi di connessione [NIP-46](/it/topics/nip-46/) dove i prefissi `wss://` mancanti causavano fallimenti silenziosi. Il PR valida gli URI relay durante la configurazione della connessione bunker, aggiungendo automaticamente il prefisso di protocollo quando gli utenti incollano domini nudi. [PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843) affronta un bug di threading dove condizioni di rete scarse causavano la pubblicazione delle risposte come note radice, rompendo il flusso della conversazione. La correzione garantisce che gli ID degli eventi genitore persistano attraverso le interruzioni di rete.

### Marmot Protocol: White Noise (Libreria Chat di Gruppo Crittografata)

White Noise, la libreria Rust che alimenta le chat di gruppo crittografate del [Protocollo Marmot](/it/topics/marmot/), ha unito sei PR migliorando l'esperienza utente e la sicurezza. I cambiamenti portano Marmot più vicino alla parità di funzionalità con le applicazioni di messaggistica mainstream mantenendo la sua architettura privacy-first.

**Ricevute di Lettura** - [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) e [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436) implementano il tracciamento della lettura dei messaggi per le conversazioni di gruppo. Il sistema memorizza le posizioni di lettura per utente per gruppo all'interno di un singolo dispositivo, abilitando i badge del conteggio non letti. L'implementazione usa timestamp monotonici per tracciare l'ultima posizione di messaggio letto per ogni conversazione. Questa funzionalità fondamentale abilita indicatori UI che mostrano i conteggi di messaggi non letti per conversazione.

**Fissaggio Conversazioni** - [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442) aggiunge il fissaggio persistente delle conversazioni attraverso un campo `pin_order` nella tabella di giunzione `accounts_groups` che collega gli account ai gruppi. Le conversazioni fissate mantengono la loro posizione in cima alle liste di chat indipendentemente dall'attività dei messaggi, rispettando le aspettative degli utenti da Signal e WhatsApp. L'implementazione usa l'ordinamento intero per permettere pin illimitati con ordinamento deterministico.

**Risoluzione Commit Deterministica (MIP-03)** - [PR #152](https://github.com/marmot-protocol/mdk/pull/152) (aperta) implementa il Marmot Improvement Proposal 03, risolvendo il problema critico delle race condition dei commit nelle chat di gruppo distribuite. Quando più membri inviano cambiamenti di stato del gruppo (aggiungere/rimuovere membri, cambiare permessi) simultaneamente, i client potrebbero divergere sull'ordinamento dei commit, frammentando il gruppo in stati incompatibili. MIP-03 introduce snapshot di epoca e una selezione deterministica del vincitore: vince il commit con il timestamp `created_at` più precoce, con l'ID evento lessicografico come tiebreaker. Questo permette a tutti i client di convergere sullo stesso stato attraverso rollback e replay, mantenendo la coerenza del gruppo anche durante le partizioni di rete.

**Hardening di Sicurezza** - [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443) previene la copia non necessaria di segreti crittografici usando riferimenti in `resolve_group_image_path`. Questo riduce la finestra per attacchi alla memoria dove i segreti potrebbero essere recuperati da allocazioni heap liberate. [PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438) abilita la crittografia del database SQLCipher attraverso parametri keyring, proteggendo la cronologia dei messaggi a riposo. L'integrazione keyring permette l'archiviazione sicura delle chiavi nei keychain della piattaforma piuttosto che nei file di configurazione.

### nostrdb-rs (Libreria Database) - PR Aperta

**Implementazione Query Streaming** - [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58) (aperta) propone query fold streaming per abilitare operazioni di database a zero allocazioni. L'implementazione aggiunge metodi `fold`, `try_fold`, `count`, `any`, `all`, e `find_map` che processerebbero i risultati del database uno alla volta senza materializzare interi set di risultati in vettori. Questo approccio ridurrebbe il consumo di memoria e abiliterebbe la terminazione anticipata per pattern di query comuni.

L'implementazione tecnica espone callback di risultati query a basso livello (`ndb_query_visit`) come visitor Rust stateful che mappano varianti `ControlFlow` ad azioni visitor C. Una volta unite, il codice applicativo si leggerà come logica iteratore mentre gira vicino al layer database. Ad esempio, contare note corrispondenti farebbe streaming attraverso i risultati piuttosto che raccoglierli, e `find_map` ritornerebbe il primo risultato utile senza processare le righe rimanenti.

nostrdb alimenta Damus e Notedeck, rispettivamente client iOS/macOS e desktop. Le query streaming abiliterebbero pattern efficienti come paginazione, filtraggio condizionale e controlli di esistenza. Il PR cambia 3 file con +756 aggiunte e -32 eliminazioni, un refactoring sostanziale del layer query. Gli utenti delle applicazioni basate su nostrdb-rs vedrebbero un uso ridotto della memoria quando navigano timeline grandi o cercano attraverso database eventi estesi.

### nak (Strumento CLI)

nak, lo strumento Nostr da linea di comando di fiatjaf, ha unito sei PR focalizzati sui miglioramenti del sistema di build e nuove funzionalità. [PR #91](https://github.com/fiatjaf/nak/pull/91) implementa una funzionalità mirror Blossom, permettendo a nak di servire come mirror per server media Blossom. [Blossom](/it/topics/blossom/) è un protocollo di archiviazione media indirizzato ai contenuti che lavora insieme agli eventi Nostr.

I PR rimanenti affrontano la compatibilità del sistema di build attraverso le piattaforme Windows, macOS e Linux, abilitando il supporto filesystem FUSE per montare gli eventi Nostr come directory locali.

### Damus (Client iOS) - PR Aperte

Damus ha 11 PR aperte che esplorano miglioramenti architetturali significativi. Sebbene questi non siano stati ancora uniti, segnalano direzioni importanti per lo sviluppo del client Nostr iOS, particolarmente attorno alla privacy, l'efficienza di sincronizzazione e l'ottimizzazione dei dati mobili.

**Integrazione Tor** - [PR #3535](https://github.com/damus-io/damus/pull/3535) incorpora il client Arti Tor direttamente in Damus, abilitando connessioni relay anonime senza dipendenze esterne. A differenza degli approcci Orbot o Tor Browser, incorporare Arti fornisce un'integrazione senza soluzione di continuità con il sandboxing iOS e i limiti di esecuzione in background. L'implementazione Rust porta la sicurezza della memoria all'anonimizzazione di rete, riducendo la superficie di attacco rispetto a C Tor. Gli utenti potrebbero attivare la modalità Tor per relay o globalmente, con il client che gestisce la gestione dei circuiti in modo trasparente.

**Protocollo di Sincronizzazione Negentropy** - [PR #3536](https://github.com/damus-io/damus/pull/3536) implementa Negentropy, un protocollo di riconciliazione di set che migliora radicalmente l'efficienza di sincronizzazione. Invece di scaricare tutti gli eventi dall'ultima connessione, Negentropy scambia fingerprint compatti (alberi Merkle) per identificare esattamente quali eventi differiscono tra client e relay. Per gli utenti che seguono centinaia di pubkey, questo riduce la banda di sincronizzazione da megabyte a kilobyte. L'implementazione si integra con RelayPool e SubscriptionManager, abilitando la sincronizzazione efficiente automatica attraverso tutti i relay connessi.

**Modalità Dati Bassi** - [PR #3549](https://github.com/damus-io/damus/pull/3549) aggiunge funzionalità di conservazione dei dati cellulari rispondendo al feedback degli utenti sul consumo di banda. La modalità disabilita il caricamento automatico delle immagini, il prefetching dei video e riduce i limiti di sottoscrizione. Gli utenti su connessioni a consumo possono navigare contenuti testuali senza paura di superare i limiti dati. L'implementazione rispetta le impostazioni della modalità dati bassi di iOS e fornisce controlli granulari per diversi tipi di media.

**Ottimizzazioni Database** - [PR #3548](https://github.com/damus-io/damus/pull/3548) rilavora l'archiviazione snapshot nostrdb per query più veloci e uso ridotto del disco. L'ottimizzazione cambia come gli snapshot del database persistono su disco, migliorando sia le prestazioni di lettura che l'amplificazione di scrittura. Questo affronta le lamentele sul consumo della batteria da parte degli utenti con database eventi grandi.

---

È tutto per questa settimana. State costruendo qualcosa? Avete notizie da condividere? Volete che copriamo il vostro progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattateci via DM NIP-17</a> o trovateci su Nostr.
