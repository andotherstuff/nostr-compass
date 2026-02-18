---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** Prende forma un livello di cache locale per Blossom, con progetti indipendenti che convergono sull'accesso offline ai media per Android. Alby lancia un [sandbox per sviluppatori NWC](https://sandbox.albylabs.com) per costruire e testare integrazioni Nostr Wallet Connect senza rischiare fondi reali. Nello stesso arco di giorni arrivano due proposte concorrenti per la comunicazione di agenti AI su Nostr, firmate da autori diversi. fiatjaf elimina i campi inutilizzati da [NIP-11](https://github.com/nostr-protocol/nips/pull/1946), rimuovendo policy di riservatezza, retention, codici paese e tag sulle preferenze comunitarie che gli operatori relay non avevano mai adottato. [NIP-85](https://github.com/nostr-protocol/nips/pull/2223) viene unito con linee guida sulla scoperta dei provider di servizi per le Trusted Assertions. Un nuovo tag `D` in [NIP-52](https://github.com/nostr-protocol/nips/pull/1752) abilita l'indicizzazione temporale a granularità giornaliera per gli eventi calendario. Tra i nuovi progetti: [Mapnolia](https://github.com/zeSchlausKwab/mapnolia) per la distribuzione decentralizzata di tile cartografiche, [Pika](https://github.com/sledtools/pika) per la messaggistica cifrata con MLS, [Keep](https://github.com/privkeyio/keep-android) per la firma a soglia FROST su Android, [Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) per lo storage content-addressed con integrazione Nostr, e [Prism](https://github.com/hardran3/Prism) per condividere contenuti su Nostr da qualsiasi app Android. [Primal Android](https://github.com/PrimalHQ/primal-android-app) unisce 11 PR NWC aggiungendo supporto doppio wallet e gestione automatica del ciclo di vita del servizio. [Mostro Mobile](https://github.com/MostroP2P/mobile) rilascia un [wallet Lightning integrato](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) tramite integrazione NWC. [Notedeck](https://github.com/damus-io/notedeck) si prepara al rilascio sull'App Store Android, mentre HAVEN raggiunge la [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3) con supporto multi-npub e backup cloud. Gli approfondimenti di questa settimana coprono il sistema Trusted Assertions di NIP-85 per delegare i calcoli del Web of Trust ai provider di servizi, e il protocollo Calendar Events di NIP-52 a seguito dell'aggiornamento per l'indicizzazione a granularità giornaliera.

## Notizie

### Emerge un Livello di Cache Locale per Blossom

Diversi progetti indipendenti stanno convergendo sullo stesso problema: l'accesso offline ai media [Blossom](/it/topics/blossom/) su dispositivi mobili.

[Morganite](https://github.com/greenart7c3/Morganite), una nuova app Android di greenart7c3 (lo sviluppatore dietro [Amber](https://github.com/greenart7c3/amber) e [Citrine](https://github.com/greenart7c3/Citrine)), implementa il caching lato client per i media Blossom. Gli utenti possono accedere a immagini e file precedentemente visualizzati senza connessione di rete.

[Aerith](https://github.com/hardran3/Aerith) ha rilasciato la [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) con etichettatura delle immagini, operazioni bulk di mirror/tag/eliminazione, filtraggio per etichetta e tipo di file, più il supporto iniziale alla cache locale Blossom. Aerith è un'interfaccia di gestione per utenti che archiviano media su più server Blossom e necessitano di organizzare e replicare i propri blob.

Una nuova [guida all'implementazione della cache locale](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md) nella specifica Blossom documenta lo storage blob lato client, mentre [Prism](https://github.com/hardran3/Prism) (dello stesso sviluppatore di Aerith) aggiunge l'integrazione Blossom upload al proprio flusso share-to-Nostr su Android. Quattro progetti indipendenti hanno convergito sullo stesso problema questa settimana: un'app di caching dedicata, un gestore media, una specifica di riferimento e uno strumento di condivisione con integrazione Blossom, tutti con storage locale persistente oltre il semplice upload-e-recupero.

### Sandbox NWC per Sviluppatori di Alby

[Alby](https://sandbox.albylabs.com) ha lanciato un ambiente sandbox per gli sviluppatori che lavorano con [Nostr Wallet Connect (NIP-47)](/it/topics/nip-47/). Il sandbox offre un servizio NWC wallet ospitato dove gli sviluppatori possono creare connessioni di test e inviare pagamenti simulati senza collegare un vero wallet Lightning, osservando in tempo reale il ciclo completo richiesta/risposta degli eventi NWC. Gli sviluppatori generano una stringa di connessione `nostr+walletconnect://` dal sandbox e la passano al proprio client. Il sandbox mostra poi il kind 23194 (richiesta) e il kind 23195 (risposta) risultanti mentre scorrono tra client e wallet service.

Questo abbassa la barriera per le nuove integrazioni NWC. In precedenza, i test richiedevano un wallet Lightning personale o un servizio NWC self-hosted. Il sandbox astrae questa complessità, dando agli sviluppatori un ciclo di feedback immediato per implementare i metodi `pay_invoice`, `get_balance`, `make_invoice`, `lookup_invoice` e `list_transactions` su un endpoint NWC attivo.

### Arrivano le Proposte di NIP per Agenti AI

Proposte per la comunicazione di agenti AI su Nostr sono apparse a distanza di giorni l'una dall'altra, affrontando il problema da angolazioni diverse.

[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226) di joelklabo definisce un protocollo completo per l'interazione con agenti AI: kind di eventi per prompt, risposte, delta di streaming, aggiornamenti di stato, telemetria degli strumenti, errori, cancellazioni e scoperta delle capacità. Un evento di scoperta `ai.info` (kind 31340, sostituibile) permette agli agenti di annunciare i modelli supportati, gli strumenti con i relativi schemi, il supporto allo streaming e i limiti di frequenza. La proposta di joelklabo include la correlazione delle esecuzioni tramite prompt ID, la gestione delle sessioni, la riconciliazione dello stream con ordinamento sequenziale e indicazioni [NIP-59](/it/topics/nip-59/) per la privacy dei metadata.

[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220) di pablof7z adotta un approccio diverso, definendo kind per l'istanziazione degli agenti: definizioni e lezioni. Si tratta dei tipi di eventi che pablof7z usa in [TENEX](https://github.com/tenex-chat/tenex), il sistema di apprendimento autonomo costruito su Nostr. Una proposta complementare, [NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221), sempre di pablof7z, definisce eventi per annunciare server [Model Context Protocol](https://modelcontextprotocol.io/) e skill su Nostr. I commenti [NIP-22](/it/topics/nip-22/) sono supportati, così la community può discutere e valutare i server MCP direttamente su Nostr.

NIP-XX copre la comunicazione completa degli agenti, mentre NIP-AE e NIP-AD si occupano di identità e scoperta degli strumenti. Queste proposte potrebbero convergere in uno standard unificato o coesistere come livelli complementari.

## Rilasci

### HAVEN v1.2.0-rc3

[HAVEN](https://github.com/bitvora/haven), il relay personale all-in-one che raggruppa quattro funzioni relay con un server media [Blossom](/it/topics/blossom/), ha raggiunto la [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3). Questa release candidate aggiunge il supporto per più npub, permettendo a una singola istanza HAVEN di servire diverse identità Nostr. Le RC precedenti avevano aggiunto i flag `--from-cloud` e `--to-cloud` per il backup cloud (RC2) e corretto un bug di doppio conteggio nel Web of Trust (RC1).

### Mostro Mobile v1.2.0: Wallet Lightning Integrato

[Mostro Mobile](https://github.com/MostroP2P/mobile), il client mobile per l'exchange Bitcoin P2P [Mostro](https://github.com/MostroP2P/mostro) ([v1.1.0 coperto la settimana scorsa](/it/newsletters/2026-02-11-newsletter/#mostro-rilascia-la-prima-beta-pubblica)), ha rilasciato la [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) con un wallet Lightning integrato attraverso la completa integrazione [NWC (NIP-47)](/it/topics/nip-47/). Acquirenti e venditori non devono più cambiare app per gestire le fatture. L'app rileva le hold invoice per i venditori e le paga automaticamente tramite il wallet collegato, mentre gli acquirenti ricevono la generazione automatica delle fatture. Il rilascio fa seguito alla [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1) pubblicata all'inizio della settimana, che aggiungeva il supporto multi-nodo Mostro con un registro curato di istanze fidate, il recupero dei metadata kind 0 per la visualizzazione dei nodi, la gestione di nodi personalizzati tramite pubkey e il fallback automatico quando un nodo selezionato va offline.

Sul lato server, [Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2) è arrivato con correzioni per i pagamenti doppi delle dev fee, il rate limiting sull'endpoint RPC di validazione password e la corretta pulizia delle dispute alla cancellazione cooperativa.

Un nuovo progetto companion, [mostro-skill](https://github.com/MostroP2P/mostro-skill), consente agli agenti di fare trading su Mostro tramite Nostr.

### Aerith v0.2

[Aerith](https://github.com/hardran3/Aerith), il gestore di immagini [Blossom](/it/topics/blossom/), ha rilasciato la [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) con etichette per l'organizzazione dei media, operazioni bulk di mirror/tag/eliminazione tra server, filtraggio per etichetta e tipo di file, più il supporto iniziale alla cache locale. Vedi la [sezione Notizie](#emerge-un-livello-di-cache-locale-per-blossom) per il contesto sul trend più ampio della cache locale.

### Mapnolia: Tile Cartografiche Decentralizzate su Nostr

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia) è un nuovo server di dati geospaziali che suddivide gli archivi di tile cartografiche [PMTiles](https://github.com/protomaps/PMTiles) in regioni geografiche e le annuncia su Nostr per la scoperta decentralizzata. Pubblica eventi parametrizzati sostituibili kind 34444 sui relay Nostr contenenti un indice completo dei chunk di tile con metadati dei layer, regioni geohash, riferimenti ai file e dettagli del server [Blossom](/it/topics/blossom/).

I client scoprono e recuperano i dati cartografici attraverso la rete Nostr invece dei server di tile centralizzati, con eventi di annuncio che portano metadati sufficienti a richiedere solo le regioni geografiche necessarie dai server Blossom elencati. Mapnolia è il primo progetto a portare la distribuzione di dati geospaziali su Nostr, aprendo possibilità per applicazioni cartografiche con supporto offline.

### Pika: Messaggistica Cifrata con Marmot

[Pika](https://github.com/sledtools/pika) è una nuova app di messaggistica end-to-end cifrata per iOS e Android che usa il protocollo [Marmot](/it/topics/marmot/), che stratifica il [Messaging Layer Security (MLS)](/it/topics/mls/) sui relay Nostr. L'architettura separa le responsabilità in un core Rust (`pika_core`) che gestisce lo stato MLS e la cifratura/decifratura dei messaggi sui relay Nostr, con shell UI native snelle in SwiftUI (iOS) e Kotlin (Android). Lo stato scorre unidirezionalmente: la UI invia azioni all'attore Rust, che modifica lo stato e restituisce snapshot con numeri di revisione alla UI tramite binding UniFFI e JNI.

Pika si unisce a un campo in crescita di messenger MLS-on-Nostr insieme a [White Noise](https://github.com/marmot-protocol/whitenoise), [Vector](https://github.com/VectorPrivacy) e [0xchat](https://0xchat.com). Tutti usano i relay Nostr come livello di trasporto per il ciphertext cifrato MLS, rendendo gli operatori relay incapaci di leggere il contenuto dei messaggi. Pika usa il Marmot Development Kit (MDK) per la propria implementazione MLS e nostr-sdk per la connettività relay.

### Keep: Firma a Soglia [FROST](/it/topics/frost/) per Android

[Keep](https://github.com/privkeyio/keep-android) è una nuova applicazione Android per la firma a soglia [FROST](/it/topics/frost/) dove nessun singolo dispositivo detiene la chiave privata completa. Implementa [NIP-55](/it/topics/nip-55/) (Android Signer) e [NIP-46](/it/topics/nip-46/) (firma remota), così i client Nostr compatibili possono richiedere firme mantenendo il materiale crittografico distribuito tra dispositivi. Le configurazioni predefinite sono 2-di-3 e 3-di-5, ma è supportata qualsiasi soglia t-di-n.

La cerimonia di generazione distribuita delle chiavi (DKG) di Keep avviene sui relay Nostr usando kind di eventi personalizzati: kind 21101 per gli annunci di gruppo, kind 21102 per i polinomi di commitment del round 1 (trasmessi pubblicamente) e kind 21103 per le share segrete del round 2 (cifrate [NIP-44](/it/topics/nip-44/) punto-a-punto tra i partecipanti). Lo scalare della chiave privata di gruppo non viene mai calcolato né assemblato durante il DKG. Ogni dispositivo detiene solo la propria share di valutazione polinomiale, e qualsiasi t share può produrre una firma Schnorr valida attraverso un protocollo commit-then-sign a due round. La firma da 64 byte risultante è indistinguibile da una firma Schnorr a singolo firmatario. Internamente, Keep usa il crate `frost-secp256k1-tr` della Zcash Foundation con il Taproot tweaking, così la chiave pubblica di gruppo funziona direttamente come un npub Nostr.

Keep si unisce alla famiglia di progetti [Frostr](https://frostr.org) insieme a [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), [Igloo for Android](https://github.com/FROSTR-ORG/igloo-android), [Frost2x](https://github.com/FROSTR-ORG/frost2x) e [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios), ampliando le opzioni per la gestione a soglia delle chiavi su Nostr.

### Prism: Condividi Qualsiasi Cosa su Nostr da Android

[Prism](https://github.com/hardran3/Prism) è una nuova app Android (Kotlin/Jetpack Compose, API 26+) che si registra come target di condivisione di sistema, permettendo agli utenti di pubblicare testo, URL, immagini e video su Nostr da qualsiasi app del proprio telefono. Gli URL condivisi passano attraverso uno stripping dei parametri di tracciamento prima di essere composti in note. Prism recupera i metadata OpenGraph per generare anteprime link ricche e rende i riferimenti Nostr nativi (`note1`, `nevent1`) inline.

Il motore di pianificazione usa un approccio ibrido `AlarmManager`/`WorkManager` per aggirare le ottimizzazioni della batteria Android: AlarmManager gestisce la temporizzazione precisa dei wake-up mentre i task WorkManager urgenti garantiscono la consegna, con retry a backoff esponenziale per gli scenari offline. I caricamenti media avvengono su server [Blossom](/it/topics/blossom/) configurabili con generazione di thumbnail per immagini e frame video. Tutta la firma degli eventi è delegata a signer esterni [NIP-55](/it/topics/nip-55/) come [Amber](https://github.com/greenart7c3/amber), con supporto multi-account per passare tra identità. Prism supporta anche i post [NIP-84 (Highlights)](/it/topics/nip-84/). Dello stesso sviluppatore di [Aerith](#aerith-v02).

### Hashtree: Storage Content-Addressed con Integrazione Nostr

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) è un sistema di storage blob content-addressed basato su filesystem che pubblica radici Merkle su Nostr per creare indirizzi npub/percorso mutabili. Il sistema usa uno "storage stupido" che funziona con qualsiasi key-value store, suddividendo il contenuto in blocchi da 2MB ottimizzati per i caricamenti [Blossom](/it/topics/blossom/). A differenza di BitTorrent, non è necessaria alcuna computazione attiva delle prove Merkle: basta archiviare e recuperare i blob per hash.

L'integrazione Nostr abilita URL git remoti come `htree://npub.../repo-name` per il cloning di repository, con comandi come `htree publish mydata <hash>` per pubblicare hash di contenuto agli indirizzi `npub.../mydata`. Il CLI completo supporta sia la modalità di storage cifrata (predefinita) che quella pubblica, il pinning dei contenuti, il push ai server Blossom e la gestione delle identità Nostr. Ogni elemento archiviato è o raw bytes o un nodo dell'albero, fornendo una base per la distribuzione decentralizzata di contenuti attraverso la rete relay di Nostr.

### Espy: Cattura Palette Colori su Shakespeare

[Espy](https://espy.you), costruito sulla piattaforma [Shakespeare](https://soapbox.pub/tools/shakespeare/), permette agli utenti di catturare palette colori da foto e condividerle come eventi Nostr. Shakespeare è un costruttore di app assistito da AI che autentica gli utenti tramite estensioni browser NIP-07 e fornisce connettività relay Nostr integrata, così gli sviluppatori pubblicano app senza implementare la propria gestione delle chiavi o il proprio pool relay. Espy estrae i colori dominanti dall'input della fotocamera in schede palette condivisibili e scopribili tramite i feed Nostr standard.

### Flotilla 1.6.4

[Flotilla](https://gitea.coracle.social/coracle/flotilla), il client Nostr in stile Discord di hodlbod che organizza i relay come gruppi, ha rilasciato la [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4). La famiglia di progetti Coracle è migrata da GitHub a un'istanza [Gitea](https://gitea.coracle.social/coracle) self-hosted. Questo rilascio aggiunge notifiche push tramite NIP-9a e un flusso per la ricezione wallet, oltre a inserzioni classificate e supporto agli URL degli spazi. I miglioramenti all'interfaccia includono modal e gestione delle notifiche riorganizzati. Il muting delle stanze e gli inset safe area su mobile completano le modifiche, insieme a correzioni per i caricamenti immagini su Safari e i dettagli degli eventi calendario.

### Shosho v0.12.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), l'app mobile di live-streaming con integrazione Nostr, ha rilasciato la [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0). Questo rilascio aggiunge Clip video con risposte in-player e integrazione emoji personalizzate. La protezione dei thread blocca lo spam da menzione indiretta, e una nuova funzione di condivisione QR permette agli utenti di scambiare profili offline. Una nuova modalità di riproduzione orizzontale offre agli stream un'esperienza di visione in stile Twitch, e la schermata di esplorazione ora mostra i clip dei creator insieme agli stream in diretta.

### Granary v10.0

[Granary](https://github.com/snarfed/granary), una libreria di traduzione per il web sociale che converte dati tra Nostr, Bluesky, ActivityPub e altre piattaforme in un formato comune, ha rilasciato la [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0) con modifiche incompatibili. Il rilascio passa gli ID ActivityStreams 1 predefiniti di Nostr da bech32 a hex e aggiunge un supporto Nostr esteso tra cui il parsing delle menzioni [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) e i tag degli articoli. Una nuova opzione di output multiplo tra i converter permette agli sviluppatori di tradurre tra protocolli in batch.

### Nostr MCP Server v3.0.0

[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server), un server [Model Context Protocol](https://modelcontextprotocol.io/) che consente agli agenti AI di interagire con la rete Nostr, ha rilasciato la [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0). Questo rilascio principale aggiunge azioni sociali (follow, reazioni, repost, risposte) e gestione delle liste relay con supporto [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) più autenticazione opzionale [NIP-42](/it/topics/nip-42/). Sono nuovi anche i messaggi diretti tramite [NIP-17](/it/topics/nip-17/) e [NIP-44](/it/topics/nip-44/). Il rilascio si affianca alle [proposte di NIP per agenti AI](#arrivano-le-proposte-di-nip-per-agenti-ai) di questa settimana come strumenti pratici per gli agenti che operano su Nostr.

### Aegis v0.3.8

[Aegis](https://github.com/ZharlieW/Aegis), il signer Nostr cross-platform, ha rilasciato la [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8) con supporto UI multilingua e un gestore di aggiornamenti incrementale per il proprio browser di app Nostr integrato. Il nuovo meccanismo di aggiornamento calcola il diff in modo incrementale rispetto allo stato locale, mantenendo aggiornata la directory in-app delle web app Nostr con un consumo di banda ridotto. Il rilascio introduce anche un caching del materiale crittografico da 5 minuti per ridurre i round-trip al database quando si firmano più eventi in successione.

### SNSTR v0.3.1

[SNSTR](https://github.com/AustinKelsay/snstr) (Secure Nostr Software Toolkit for Renegades), una libreria TypeScript per il protocollo Nostr, ha rilasciato la [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1). Il rilascio aggiunge guardie di verifica dei pacchetti che assicurano che tutti i punti di ingresso siano inclusi nei tarball npm, con verifica CI su Node e Bun. La [v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0) è uscita nella stessa settimana.

### Citrine v2.0.0-pre1

[Citrine](https://github.com/greenart7c3/Citrine), il relay Nostr per Android di greenart7c3, ha rilasciato la [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1) con miglioramenti delle prestazioni tramite indici del database ottimizzati e una migliore gestione delle coroutine Kotlin. Il rilascio migliora anche il supporto per l'hosting di web app, con ogni app ora in esecuzione sulla propria porta.

## Aggiornamenti dei Progetti

### Primal Android: Espansione dell'Infrastruttura NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) ha unito 11 PR legate a NWC questa settimana, continuando il lavoro avviato [due settimane fa](/it/newsletters/2026-02-04-newsletter/#primal-android-rilascia-crittografia-nwc). Questa tornata aggiunge il supporto NWC per doppio wallet, avvio/arresto automatico del servizio legato alle notifiche del backend, routing delle connessioni per tipo di wallet e corretta pulizia dei dati all'eliminazione del wallet. Il servizio NWC ora gestisce il proprio ciclo di vita in base allo stato della connessione wallet, riducendo l'intervento manuale dell'utente.

### Notedeck: Preparazione all'App Store Android

[Notedeck](https://github.com/damus-io/notedeck), il client Nostr multi-piattaforma del team [Damus](https://github.com/damus-io/damus), ha unito la [preparazione al rilascio sull'App Store Android](https://github.com/damus-io/notedeck/pull/1287) questa settimana. La PR aggiunge un piano di conformità UGC (User Generated Content) richiesto da Google Play, inclusa una schermata di accettazione dei Termini di Servizio, il blocco degli utenti tramite menu contestuali e impostazioni, la funzionalità [NIP-56 (Segnalazione)](/it/topics/nip-56/) che pubblica eventi di segnalazione sui relay, e una sezione di impostazioni per Contenuto e Sicurezza. È stata aggiunta l'infrastruttura di build per generare APK firmati e AAB (Android App Bundle) tramite nuovi target Makefile. Un documento EULA stabilisce un requisito di età di 17 anni e disclaimer specifici per Nostr riguardo ai contenuti decentralizzati. Le funzionalità di conformità stesse arriveranno in PR successive; questo merge pone le basi documentali e di firma.

Sul fronte Damus iOS, è stata corretta una [regressione del caricamento infinito](https://github.com/damus-io/damus/pull/3593) in cui lo spinner persisteva indefinitamente dopo che il contenuto era stato caricato.

### Nostria: Relay di Scoperta e Correzioni DM

[Nostria](https://github.com/nostria-app/nostria), il client Nostr cross-platform focalizzato sulla scala globale, ha unito 9 PR questa settimana. La più importante aggiunge l'[auto-inizializzazione dei Discovery Relay](https://github.com/nostria-app/nostria/pull/460) per la ricerca dei profili, garantendo ai nuovi utenti una connettività relay funzionante senza configurazione manuale. Altre correzioni riguardano [l'avvolgimento del testo nelle textarea DM](https://github.com/nostria-app/nostria/pull/466), [il riempimento del viewport per i video a schermo intero](https://github.com/nostria-app/nostria/pull/479), [l'estrazione dei metadata degli articoli nelle anteprime repost](https://github.com/nostria-app/nostria/pull/481) e [la risoluzione degli URI nostr: nelle notifiche](https://github.com/nostria-app/nostria/pull/458).

### Camelus: Migrazione a Riverpod v3

[Camelus](https://github.com/camelus-hq/camelus), il client Nostr basato su Flutter, ha unito 5 PR questa settimana incentrate su una [migrazione all'API Riverpod v3](https://github.com/camelus-hq/camelus/pull/158) e un [refactoring del feed generico](https://github.com/camelus-hq/camelus/pull/159). Una [cache delle note incorporate](https://github.com/camelus-hq/camelus/pull/161) evita fetch ridondanti ai relay per le note citate.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti:**

- **[NIP-85: Scoperta dei Provider di Servizi](https://github.com/nostr-protocol/nips/pull/2223)**: vitorpamplona ha aggiunto indicazioni sulla scoperta da parte dei client dei provider di servizi [NIP-85 Trusted Assertions](/it/topics/trusted-relay-assertions/), inclusi gli hint relay e le chiavi di servizio specifiche per algoritmo. Vedi l'[approfondimento](#nip-deep-dive-nip-85-trusted-assertions) per la copertura completa.

- **[NIP-11: Pulizia delle Informazioni Relay](https://github.com/nostr-protocol/nips/pull/1946)**: fiatjaf ha rimosso `privacy_policy`, l'array `retention`, `relay_countries` e il blocco delle preferenze comunitarie da [NIP-11](/it/topics/nip-11/). Gli operatori relay raramente popolavano questi campi e i client non vi agivano sopra.

- **[NIP-52: Tag di Timestamp a Granularità Giornaliera](https://github.com/nostr-protocol/nips/pull/1752)**: staab ha aggiunto un tag `D` obbligatorio a [NIP-52](/it/topics/nip-52/) per gli eventi calendario basati sul tempo (kind 31923) che rappresenta il timestamp Unix a granularità giornaliera, calcolato come `floor(unix_seconds / 86400)`. Più tag `D` coprono eventi multi-giorno, abilitando un efficiente indicizzazione temporale senza dover analizzare i timestamp completi.

- **[NIP-47: Semplificazione](https://github.com/nostr-protocol/nips/pull/2210)**: La PR di semplificazione [discussa nel numero #9](/it/newsletters/2026-02-11-newsletter/) è stata unita questa settimana, rimuovendo `multi_pay_invoice` e `multi_pay_keysend` da [NIP-47 (Nostr Wallet Connect)](/it/topics/nip-47/). Vedi il [numero #8](/it/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect) per l'approfondimento completo sul protocollo NWC.

**PR Aperte e Discussioni:**

- **[NIP-74: Podcast](https://github.com/nostr-protocol/nips/pull/2211)**: Coperto nel [numero #8](/it/newsletters/2026-02-04-newsletter/), questa proposta di specifica per i podcast ha visto un acceso dibattito questa settimana. staab ha notato che esistono già almeno tre standard podcast concorrenti in circolazione, e derekross ha indicato un'implementazione esistente risalente a sei mesi fa con app e podcast attivi. Il percorso da seguire richiede una convergenza tra le implementazioni prima che possa essere assegnato un numero NIP.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)**: joelklabo propone un protocollo completo di comunicazione per agenti AI con kind di eventi per prompt, risposte, streaming, telemetria degli strumenti, errori e scoperta delle capacità. Vedi la [sezione Notizie](#arrivano-le-proposte-di-nip-per-agenti-ai) per la copertura di tutte le proposte AI di questa settimana.

- **[NIP-PNS: Private Note Storage](https://github.com/nostr-protocol/nips/pull/1893)**: il sistema di note private di jb55 definisce eventi kind 1080 per archiviare note personali cifrate sui relay senza rivelare chi le ha scritte. Lo schema deriva una coppia di chiavi pseudonima deterministica dalla nsec dell'utente tramite HKDF: `pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`, quindi genera una coppia di chiavi secp256k1 da quella chiave derivata. Una seconda derivazione produce una chiave di cifratura simmetrica: `pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`. Le note interne sono cifrate con [NIP-44](/it/topics/nip-44/) v2 usando questa chiave e pubblicate sotto la pubkey pseudonima, così i relay vedono eventi kind 1080 da un'identità non collegata alla chiave principale dell'utente. A differenza dei gift wrap [NIP-59](/it/topics/nip-59/), PNS non è soggetto a spam (la chiave pseudonima è deterministica, non casuale) e non porta metadata pubblici (non servono tag `p` poiché non c'è destinatario). Questa settimana, jb55 ha pubblicato le conclusioni tratte dall'implementazione di PNS nel backend Rust di Notedeck (modulo `enostr::pns`). Ha identificato che la chiamata `hkdf_extract` della spec è ambigua perché HKDF secondo RFC 5869 ha due fasi (Extract ed Expand) che producono output diversi, e la maggior parte delle librerie si aspetta entrambe. Ha chiarito che `pns_nip44_key` aggira il normale accordo di chiavi ECDH di NIP-44 e viene usata direttamente come conversation key, un dettaglio che gli implementatori devono conoscere poiché la maggior parte delle librerie NIP-44 usa ECDH di default. Ha anche segnalato una variabile non definita nell'implementazione di riferimento TypeScript. La PR, originariamente dell'aprile 2025, è ora in fase di implementazione attiva.

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)**: pablof7z definisce quattro kind di eventi per l'identità degli agenti su Nostr, tratti dal suo lavoro su [TENEX](https://github.com/tenex-chat/tenex). Il template base è kind 4199 (Agent Definition), che contiene titolo, descrizione del ruolo, istruzioni di sistema, dichiarazioni di strumenti e versione. I modificatori comportamentali risiedono nel kind 4201 (Agent Nudge), che usa i tag `only-tool`, `allow-tool` e `deny-tool` per il controllo delle capacità in runtime. Gli agenti pubblicano ciò che apprendono come eventi kind 4129 (Agent Lesson), categorizzati e collegati alla definizione genitore tramite tag `e`, perfezionabili attraverso thread di commenti [NIP-22](/it/topics/nip-22/). La verifica della proprietà usa kind 14199, un evento sostituibile in cui gli operatori umani elencano le proprie pubkey agente, stabilendo una catena bidirezionale quando abbinato al tag `p` del profilo kind 0 dell'agente.

- **[NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221)**: pablof7z definisce eventi per annunciare server [Model Context Protocol](https://modelcontextprotocol.io/) e skill individuali su Nostr. Gli annunci di server MCP portano l'URL endpoint del server e la versione di protocollo supportata insieme a un elenco di strumenti disponibili con i relativi schemi di input. I commenti [NIP-22](/it/topics/nip-22/) sono supportati sugli annunci di server, così la community può discutere e valutare i server MCP direttamente su Nostr.

- **[NIP-73: OSM Tag Kind](https://github.com/nostr-protocol/nips/pull/2224)**: DestBro propone di aggiungere gli identificatori OpenStreetMap a [NIP-73 (External Content IDs)](/it/topics/nip-73/), che standardizza come gli eventi Nostr referenziano contenuti esterni come libri (ISBN), film (ISAN), feed podcast (GUID), geohash e URL tramite tag `i` e `k`. Il kind OSM proposto permetterebbe agli eventi di referenziare elementi cartografici specifici (edifici, strade, parchi) tramite il loro ID nodo o way OpenStreetMap, collegando i contenuti Nostr al database geografico aperto.

- **[NIP-XX: Responsive Image Variants](https://github.com/nostr-protocol/nips/pull/2219)**: woikos propone di estendere gli eventi di metadata file [NIP-94](/it/topics/nip-94/) con tag per varianti di immagini responsive a risoluzioni diverse. I client potrebbero selezionare la variante appropriata in base alle dimensioni del display e alle condizioni di rete, riducendo il consumo di banda per gli utenti mobile che visualizzano immagini ad alta risoluzione ospitate su server [Blossom](/it/topics/blossom/).

## NIP Deep Dive: NIP-85 (Trusted Assertions)

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) definisce un sistema per delegare calcoli costosi a provider di servizi fidati che pubblicano i risultati firmati come eventi Nostr. I punteggi Web of Trust e le metriche di engagement richiedono la scansione di molti relay e l'elaborazione di grandi volumi di eventi, un lavoro impraticabile su dispositivi mobili. Il [merge](https://github.com/nostr-protocol/nips/pull/2223) di questa settimana ha aggiunto indicazioni sul processo di scoperta da parte dei client di questi provider.

**Delega:**

Calcolare il punteggio Web of Trust di un utente richiede la scansione dei grafi di follow per diversi livelli su molti relay, e il calcolo accurato dei conteggi follower comporta la deduplicazione sull'intera rete relay. I dispositivi mobili e i client browser non possono eseguire queste operazioni, eppure i risultati sono essenziali per il filtraggio dello spam e il ranking dei contenuti. NIP-85 colma questo divario permettendo agli utenti di designare provider fidati per eseguire i calcoli e pubblicare i risultati come eventi Nostr standard.

**Design del Protocollo:**

NIP-85 usa quattro kind di eventi per le asserzioni su diversi tipi di soggetti. Le asserzioni sugli utenti (kind 30382) portano il conteggio follower, i conteggi post/risposte/reazioni, gli importi zap, il rank normalizzato (0-100), i topic comuni e le ore attive:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Le asserzioni sugli eventi (kind 30383) valutano le singole note con il conteggio commenti, citazioni, repost, reazioni e dati zap:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Per gli eventi indirizzabili (articoli long-form, pagine wiki), kind 30384 applica le stesse metriche di engagement su tutte le versioni collettivamente. Kind 30385 valuta gli identificatori esterni (libri, film, siti web, luoghi, hashtag) referenziati tramite [NIP-73 (External Content IDs)](/it/topics/nip-73/), che standardizza come gli eventi Nostr referenziano contenuti esterni tramite tag `i` e `k`:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Ogni asserzione è un evento indirizzabile sostituibile dove il tag `d` contiene il soggetto: una pubkey, un ID evento, un indirizzo evento o un identificatore NIP-73. I provider di servizi firmano questi eventi con le proprie chiavi, e i client li valutano in base alle relazioni di fiducia.

**Scoperta dei Provider:**

Gli utenti dichiarano quali provider di asserzioni si fidano pubblicando eventi kind 10040. Ogni voce specifica il tipo di asserzione con la pubkey del provider e l'hint relay, più varianti di algoritmo opzionali:

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

Gli utenti possono cifrare l'elenco dei tag nel `.content` usando [NIP-44](/it/topics/nip-44/) per mantenere private le proprie preferenze di provider. I client costruiscono un elenco di provider controllando quali provider si fidano i propri account seguiti, creando un livello di reputazione decentralizzato per i provider di asserzioni stessi.

**Modello di Sicurezza:**

I provider devono usare chiavi di servizio diverse per algoritmi distinti, e una chiave unica per utente quando gli algoritmi sono personalizzati, impedendo la correlazione incrociata delle query tra utenti. Ogni chiave di servizio ottiene un evento di metadata kind 0 che descrive il comportamento dell'algoritmo, dando agli utenti trasparenza su ciò in cui ripongono la propria fiducia. Gli eventi di asserzione dovrebbero essere aggiornati solo quando i dati sottostanti cambiano effettivamente, prevenendo traffico relay non necessario e permettendo ai client di memorizzare nella cache i risultati con fiducia.

**Adozione Attuale:**

NIP-85 formalizza un pattern già emerso informalmente. Il server cache di Primal calcola le metriche di engagement e i punteggi Web of Trust. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal), coperto nel [numero #9](/it/newsletters/2026-02-11-newsletter/#antiprimal-gateway-conforme-per-il-cache-di-primal), collega questi calcoli ai client Nostr standard usando i kind di eventi NIP-85. [Nostr.band](https://nostr.band) gestisce il relay `wss://nip85.nostr.band` referenziato negli esempi della spec stessa, servendo eventi di asserzione per i dati del proprio indice di ricerca. Sul lato client, [Amethyst](https://github.com/vitorpamplona/amethyst) (scritto da vitorpamplona, anche autore di questo NIP) ha un supporto sperimentale alle Trusted Assertions nella propria libreria `quartz`, che analizza gli eventi di asserzione e le dichiarazioni dei provider di servizi. [Vertex](https://vertexlab.io) calcola metriche Web of Trust simili ma ha [scelto un approccio diverso](https://vertexlab.io/blog/dvms_vs_nip_85/), usando una API diretta invece degli eventi NIP-85, citando il problema della scoperta e l'overhead computazionale delle architetture basate su asserzioni. Con NIP-85, qualsiasi client può consumare asserzioni da qualsiasi provider attraverso un formato di evento standard, e i provider competono sull'accuratezza mentre gli utenti scelgono di chi fidarsi.

## NIP Deep Dive: NIP-52 (Calendar Events)

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md) definisce gli eventi calendario su Nostr, dando ai client un modo standard per rappresentare e scoprire occorrenze in momenti specifici o tra momenti. Il [merge del tag D](https://github.com/nostr-protocol/nips/pull/1752) di questa settimana ha aggiunto l'indicizzazione a granularità giornaliera, completando un elemento mancante nell'infrastruttura di query della spec.

**Due Tipi di Evento:**

NIP-52 separa gli eventi calendario in due kind in base alla precisione temporale. Gli eventi basati sulla data (kind 31922) rappresentano occorrenze che durano un'intera giornata come festività o festival multi-giorno. Usano stringhe di data ISO 8601 nei tag `start` e `end` opzionale, senza considerazioni sul fuso orario:

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

Gli eventi basati sul tempo (kind 31923) rappresentano momenti specifici con timestamp Unix nei tag `start` e `end` opzionale, più identificatori di fuso orario IANA (`start_tzid`, `end_tzid`) per la visualizzazione. Entrambi i kind sono eventi parametrizzati sostituibili, così gli organizzatori aggiornano i dettagli pubblicando un nuovo evento con lo stesso tag `d`.

**Calendari e RSVP:**

Gli eventi kind 31924 definiscono i calendari come collezioni, referenziando gli eventi tramite tag `a` che puntano agli eventi kind 31922 o 31923 tramite le loro coordinate di indirizzo:

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

Gli utenti possono mantenere più calendari (personale, lavoro, comunitario) e i client possono iscriversi ai calendari di pubkey specifiche. Gli eventi calendario possono includere un tag `a` che referenzia un calendario per richiedere l'inclusione, abilitando la gestione collaborativa dei calendari dove più utenti contribuiscono eventi a calendari che non possiedono.

Gli RSVP usano kind 31925, dove gli utenti pubblicano il proprio stato di partecipazione insieme a un indicatore opzionale libero/occupato:

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

I valori `status` validi sono "accepted", "declined", "tentative", e il tag opzionale `fb` marca l'utente come libero o occupato per quel periodo. Gli eventi RSVP referenziano il tag `a` dell'evento calendario e portano il tag `p` dell'organizzatore, così il client dell'organizzatore può aggregare le risposte dai relay.

**L'Aggiunta del Tag D:**

Prima del merge di questa settimana, i client che interrogavano gli eventi in un intervallo di date dovevano recuperare tutti gli eventi da una pubkey o un calendario e filtrare lato client. Il nuovo tag `D` obbligatorio sugli eventi basati sul tempo (kind 31923) contiene un timestamp Unix a granularità giornaliera calcolato come `floor(unix_seconds / 86400)`. Gli eventi multi-giorno portano più tag `D`, uno per giorno. I relay possono ora indicizzare gli eventi per giorno e rispondere a query filtrate in modo efficiente, trasformando quello che era un problema di filtraggio lato client in una ricerca nell'indice lato relay.

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

Il valore `D` `20139` equivale a `floor(1740067200 / 86400)`, collocando questo evento il 20 febbraio 2025. I client che interrogano "tutti gli eventi di questa settimana" inviano un filtro con il corrispondente intervallo `D`, e i relay restituiscono solo gli eventi corrispondenti.

**Scelte di Design:**

NIP-52 omette intenzionalmente gli eventi ricorrenti. La spec esclude completamente le regole di ricorrenza (RRULE da iCalendar), delegando quella complessità ai client. Un organizzatore pubblica eventi individuali per ogni occorrenza, mantenendo semplice il modello dati lato relay. I tag partecipante portano ruoli opzionali ("host", "speaker", "attendee"), e i tag di localizzazione possono includere tag geohash `g` per query spaziali insieme agli indirizzi leggibili.

**Implementazioni:**

[Flockstr](https://github.com/zmeyer44/flockstr) è il principale client calendario costruito su NIP-52. [Coracle](https://gitea.coracle.social/coracle/coracle) visualizza gli eventi calendario nel proprio feed sociale. L'aggiunta del tag `D` di questa settimana abilita l'indicizzazione temporale lato relay che entrambi i client possono usare per ridurre la banda quando si interrogano eventi in un intervallo di date specifico.

---

È tutto per questa settimana. Stai costruendo qualcosa o hai notizie da condividere? Vuoi che copriamo il tuo progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattaci via DM [NIP-17](/it/topics/nip-17/)</a> o trovaci su Nostr.
