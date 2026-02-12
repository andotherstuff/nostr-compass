---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** Mostro rilascia la sua prima beta pubblica dopo tre anni di sviluppo, portando il trading P2P di Bitcoin su mobile via Nostr. OpenSats assegna la sedicesima ondata di grant Bitcoin, con Minibits Wallet che riceve un rinnovo per il suo wallet Cashu integrato con Nostr. **Zapstore raggiunge la release stabile 1.0**, segnando la maturazione dell'app store Android decentralizzato. Coracle 0.6.29 aggiunge topics e commenti sugli highlight. Igloo Desktop v1.0.3 introduce un importante hardening di sicurezza per la firma a soglia Frostr. Amber v4.1.2-pre1 migra all'architettura Flow. Angor raggiunge v0.2.5 con una UI di finanziamento rinnovata e configurazione server di immagini NIP-96. NostrPress viene lanciato come strumento che converte profili Nostr in blog statici. Antiprimal rilascia un gateway conforme agli standard che collega il cache server proprietario di Primal ai NIP standard di Nostr. Primal Android unisce 18 PR espandendo l'infrastruttura NWC con supporto doppio wallet, audit logging e il metodo `lookup_invoice`. diVine rilascia feed video API-first. L'SDK TypeScript di Marmot separa la sua app chat di riferimento in un repository autonomo e inizia la migrazione a ts-mls v2. Il repository NIPs unisce il conteggio approssimativo HyperLogLog per NIP-45 ed estrae i tag identità da kind 0. Un'ondata di proposte di vitorpamplona inizia a snellire sistematicamente i metadata kind 0. Nuove proposte di protocollo includono Nostr Relay Connect per il NAT traversal e Nostr Web Tokens per claim web firmati. Due approfondimenti chiudono il numero: il conteggio approssimativo HyperLogLog di NIP-45 per metriche eventi cross-relay, e il protocollo di file storage HTTP NIP-96, ora deprecato a favore di Blossom, mentre i progetti gestiscono la transizione tra i due standard media.

## Notizie

### Mostro Rilascia la Prima Beta Pubblica

[Mostro](https://github.com/MostroP2P/mostro), l'exchange Bitcoin peer-to-peer costruito su Nostr, ha rilasciato la sua [app mobile v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0), la prima beta pubblica del progetto dopo tre anni di sviluppo. L'app permette di scambiare Bitcoin direttamente usando Nostr per la coordinazione degli ordini, con Lightning per il settlement e nessun intermediario custodial.

Il rilascio introduce notifiche push con migliore affidabilità in background su Android, un sistema di logging opzionale che permette di catturare e condividere dati diagnostici quando si presentano problemi, aggiornamenti relay più fluidi con inizializzazione additiva, e raffinamenti UI di Fase 2 con supporto internazionalizzazione. L'app è disponibile su [Zapstore](https://zapstore.dev) e come [download diretto da GitHub](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0).

Mostro si unisce a Shopstr e Plebeian Market come applicazione commerciale nativa Nostr, con la distinzione di concentrarsi sulla coordinazione dello scambio fiat-Bitcoin. Il [daemon Mostro](https://github.com/MostroP2P/mostro) sottostante gestisce il matching degli ordini e la risoluzione delle dispute attraverso relay Nostr.

### Sedicesima Ondata di Grant Bitcoin di OpenSats

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants) ha annunciato grant a 17 progetti open-source. Il punto saliente per Nostr: [Minibits Wallet](https://github.com/minibits-cash/minibits_wallet), il wallet Android [Cashu](/it/topics/cashu/) con supporto eventi wallet [NIP-60](/it/topics/nip-60/) e integrazione nutzap, ha ricevuto un grant di rinnovo. Minibits usa eventi Nostr per memorizzare lo stato dei token ecash, rendendo i backup del wallet portabili tra dispositivi tramite sincronizzazione relay.

### NostrPress: Dal Profilo Nostr al Blog Statico

[NostrPress](https://github.com/besoeasy/NostrPress) ([blog.besoeasy.com](https://blog.besoeasy.com)) è un nuovo strumento che converte un profilo Nostr in un blog completamente statico deployabile ovunque. Chi pubblica articoli su Nostr tramite qualsiasi client può generare con NostrPress un sito web autonomo da quegli eventi, completo di hosting media locale e feed RSS.

Costruito con templating Nunjucks e JavaScript, NostrPress produce siti privi di lock-in di piattaforma. L'output generato è semplice HTML/CSS ospitabile su qualsiasi server di file statici, GitHub Pages, Netlify o un VPS personale. Lo strumento si unisce a [Npub.pro](https://github.com/nostrband/nostrsite) e [Servus](https://github.com/servus-social/servus) come opzione per trasformare contenuti Nostr in siti web tradizionali.

### Antiprimal: Gateway Conforme per il Cache di Primal

[antiprimal](https://gitlab.com/soapbox-pub/antiprimal) ([antiprimal.net](https://antiprimal.net)), un nuovo progetto di Alex Gleason e del team Soapbox, è un gateway WebSocket che collega il cache server proprietario di Primal ai messaggi standard del protocollo Nostr. Primal offre funzionalità come statistiche eventi, ricerca contenuti e calcoli Web of Trust tramite `wss://cache.primal.net/v1`, ma accedervi richiede un formato messaggi proprietario con un campo `cache` non standard che i client Nostr ordinari non possono usare. Antiprimal traduce le richieste NIP standard nel formato di Primal e converte le risposte indietro.

Il gateway supporta query COUNT [NIP-45](/it/topics/nip-45/) (reazioni, risposte, repost, conteggi zap, conteggi follower), ricerca [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md), informazioni relay [NIP-11](/it/topics/nip-11/) e [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) Trusted Assertions per i dati Web of Trust precalcolati di Primal. Un bot companion pubblica eventi NIP-85 kind 30382 (statistiche utente) e kind 30383 (engagement eventi) su relay configurabili. Il progetto è costruito con TypeScript su Bun e usa la libreria Nostrify. Creato il 6 febbraio, ha 53 commit nei suoi primi tre giorni di sviluppo ed è live su antiprimal.net.

### Ikaros: Gateway di Messaggistica per Agenti AI su Signal e Nostr

[Ikaros](https://gitlab.com/soapbox-pub/ikaros), un nuovo progetto del team Soapbox, è un gateway di messaggistica che permette ad agenti AI di comunicare attraverso DM crittografati sia su Signal che su Nostr. Il bridge usa l'[Agent Client Protocol](https://agentclientprotocol.org) (ACP) per connettere qualsiasi assistente AI di coding compatibile ACP a reti di messaggistica reali. Tre pull request costituiscono la build iniziale del progetto.

La [PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1) implementa un adattatore completo per DM crittografati [NIP-04](/it/topics/nip-04/) con supporto invio/ricezione, buffering delle risposte con flush esplicito al completamento, formati chiave privata `nsec` e hex, pubblicazione multi-relay con riconnessione automatica e un wizard di setup interattivo. L'adattatore usa nostr-tools v2.23.0 e aggiorna l'ACP SDK a v0.14.1.

La [PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2) corregge un drop silenzioso di messaggi causato da una race condition nell'aggiornamento della sessione: le notifiche in arrivo prima che la sessione fosse registrata nella mappa venivano perse, e il fix mette in buffer quelle notifiche per il replay al completamento della registrazione. La [PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3) aggiunge metadati di nome utente/UUID e gruppo Signal alle interazioni con l'agente, così l'agente AI sa con chi sta parlando e in quale gruppo. Il progetto apre un nuovo spazio di design: agenti AI raggiungibili via DM Nostr che possono anche essere contattati da Signal, o viceversa.

### Campagna di Snellimento Kind 0

vitorpamplona ha aperto una serie di PR proponendo l'estrazione sistematica di dati dagli eventi kind 0 (metadata utente) in kind di eventi dedicati. La campagna affronta un problema crescente: col passare del tempo kind 0 ha accumulato campi che la maggior parte dei client non usa, gonfiando la dimensione di ogni fetch di profilo.

La [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) (unita) sposta i tag identità (tag `i`) da kind 0 a un nuovo kind 10011, dato che l'adozione di questi tag è stata minima. La [PR #2213](https://github.com/nostr-protocol/nips/pull/2213) propone di spostare la verifica [NIP-05](/it/topics/nip-05/) a kind 10008, il che permetterebbe di avere più identificatori NIP-05 per utente e di filtrare eventi per indirizzo NIP-05. La [PR #2217](https://github.com/nostr-protocol/nips/pull/2217) propone di estrarre i campi Lightning (lud06/lud16) in un nuovo kind, evitando che tutti i profili kind 0 portino campi relativi allo zap che interessano solo ai client con integrazione Lightning.

Le proposte hanno riacceso la discussione sulla questione più ampia della struttura di kind 0, inclusa la [PR #1770](https://github.com/nostr-protocol/nips/pull/1770), la proposta di lunga data per sostituire il JSON stringificato nel contenuto kind 0 con tag strutturati.

### Il Supporto Relay NIP-70 è Critico per la Sicurezza della Messaggistica Crittografata

L'implementazione White Noise del protocollo [Marmot](/it/topics/marmot/) ha [identificato una lacuna critica](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html) nel supporto relay per [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) (Protected Events) e [NIP-42](/it/topics/nip-42/) (Authentication). I test hanno rivelato che i principali relay pubblici inclusi Damus, Primal e nos.lol rifiutano i protected event con errori `blocked: event marked as protected` invece di avviare la challenge di autenticazione richiesta.

Questa lacuna rompe la funzionalità di sicurezza chiave: NIP-70 abilita la cancellazione sicura dei KeyPackages MLS spesi, prevenendo attacchi "harvest now, decrypt later". In assenza di supporto relay, i protocolli di messaggistica crittografata non possono proteggere dal futuro compromesso delle chiavi. White Noise ha disabilitato NIP-70 di default in risposta, mantenendo un flag opzionale per chi usa relay compatibili.

**Invito all'azione per operatori relay:** Implementate il flusso di autenticazione NIP-42 completo. Quando ricevete protected event, effettuate la challenge ai client per dimostrare la proprietà, poi accettate le scritture validate. Rifiutare protected event in assenza di autenticazione rompe le garanzie di sicurezza del protocollo da cui dipendono le applicazioni di messaggistica crittografata.

## Rilasci

### Coracle 0.6.29

[Coracle](https://github.com/coracle-social/coracle) ([coracle.social](https://coracle.social)), il client web di hodlbod, ha rilasciato [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29). Il rilascio aggiunge la visualizzazione di topics e commenti sugli highlight kind 9802. Un nuovo elemento di navigazione liste fornisce accesso rapido alle liste curate dall'utente dalla UI principale. Sotto il cofano, Coracle è stato aggiornato a una nuova versione di Welshman, la libreria Nostr condivisa che alimenta la gestione relay e la gestione eventi di Coracle. La lista relay di default è stata aggiornata, e il tracking errori Glitchtip è stato rimosso dal codebase.

### Igloo Desktop v1.0.3

[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), l'applicazione di firma a soglia [FROST](/it/topics/frost/) e gestione chiavi, ha rilasciato [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3) con esteso hardening di sicurezza. Il rilascio introduce validazione IPC, isolamento Electron e controlli relay consapevoli di SSRF per la difesa contro server-side request forgery. Un nuovo flusso di onboarding e importazione share semplifica la distribuzione delle chiavi, la pianificazione relay ora include normalizzazione e merging prioritario, e l'architettura API Electron basata su preload migliora il confine di sicurezza tra renderer e processo principale. Un sistema keep-alive per il signer mantiene la stabilità delle sessioni di firma a soglia, e i miglioramenti UX di recovery riducono l'attrito del ripristino delle chiavi.

### Amber v4.1.2-pre1

[Amber](https://github.com/greenart7c3/Amber), il signer di eventi Android, ha rilasciato [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1) correggendo la visualizzazione mancante del punteggio di fiducia relay introdotta in v4.1.1, risolvendo problemi di parsing JSON per richieste encrypt/decrypt non-Nostr, e migrando il modello account da LiveData a Flow per una gestione dello stato più prevedibile. Il rilascio passa i segreti bunker a UUID completi e aggiorna a Gradle plugin 9.

### Mostro Mobile v1.1.0 e Daemon v0.16.1

Vedi la [sezione Notizie sopra](#mostro-rilascia-la-prima-beta-pubblica) per la copertura completa del rilascio mobile. Sul lato server, il [daemon Mostro](https://github.com/MostroP2P/mostro) ha rilasciato [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1), aggiungendo la pubblicazione automatica dei metadata NIP-01 kind 0 all'avvio ([PR #575](https://github.com/MostroP2P/mostro/pull/575)), così il daemon annuncia la propria identità alla rete quando va online. Il rilascio corregge anche la documentazione del calcolo delle dev fee ([PR #571](https://github.com/MostroP2P/mostro/pull/571)).

### Angor v0.2.5

[Angor](https://github.com/block-core/angor) ([angor.io](https://angor.io)), il protocollo di finanziamento P2P decentralizzato costruito su Bitcoin e Nostr, ha rilasciato [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5) con tre PR unite. La [PR #649](https://github.com/block-core/angor/pull/649) riprogetta la sezione gestione Fondi (V2), sostituendo il layout precedente con un'interfaccia nuova per il tracking di singoli UTXO e posizioni di investimento. La [PR #651](https://github.com/block-core/angor/pull/651) rinnova la InvoiceView con stili pulsanti aggiornati, dialog chiudibili, un nuovo comando "Copia Indirizzo", supporto cancellazione per il monitoraggio indirizzi, e gestione migliorata del flusso investimenti. La [PR #652](https://github.com/block-core/angor/pull/652) aggiunge server immagini [NIP-96](/it/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) configurabili nelle impostazioni, permettendo di scegliere quale endpoint di upload media gestisce le immagini e la documentazione dei progetti. La [v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4) era stata rilasciata la settimana precedente.

### Ridestr v0.2.2 e v0.2.3

[Ridestr](https://github.com/variablefate/ridestr), la piattaforma di rideshare decentralizzata [coperta la settimana scorsa](/it/newsletters/2026-02-04-newsletter/#ridestr-v020-roadflare-release), ha continuato l'iterazione rapida con [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2) (Bridge Payment Hotfix) e [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3) dopo la v0.2.0 "RoadFlare Release". L'hotfix v0.2.2 affronta un bug dove i pagamenti bridge [Cashu](/it/topics/cashu/) cross-mint cancellavano automaticamente le corse mentre il pagamento era ancora in elaborazione o sarebbe eventualmente riuscito, prevenendo la cancellazione prematura delle corse su settlement più lenti. Il rilascio corregge anche lo sfarfallio della UI e le hitbox touch rotte sul pulsante "la mia posizione". La v0.2.3 include ulteriori bug fix. Entrambi i rilasci includono APK separati per Ridestr (app passeggero) e Drivestr (app autista).

### Nostr PHP 1.9.4

[Nostr PHP](https://github.com/nostrver-se/nostr-php) ([nostr-php.dev](https://nostr-php.dev)), la libreria helper PHP per il protocollo Nostr, ha rilasciato [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4) aggiungendo una proprietà `timeout` configurabile alla classe request ([PR #106](https://github.com/nostrver-se/nostr-php/pull/106)). La novità permette di impostare durate di timeout personalizzate per le connessioni relay e le richieste messaggi, prevenendo blocchi indefiniti quando un relay non risponde o è lento a rispondere.

### Zapstore v1.0.0

[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0) ([zapstore.dev](https://zapstore.dev)), l'app store Android permissionless costruito su Nostr, **ha raggiunto la milestone della release stabile 1.0** dopo mesi di release candidate.

Il rilascio 1.0 include miglioramenti di stabilità critici: gestione dello stato del pulsante install che assicura che Delete appaia immediatamente dopo il completamento dell'installazione, messaggi di errore user-friendly con dettagli tecnici espandibili, e un pulsante "Segnala problema" che invia DM crittografati via Nostr usando chiavi effimere. Tra le novità anche un nuovo schermo aggiornamenti con polling e tracking batch, un migliore watchdog per i download bloccati, limiti di download concorrenti dinamici basati sulle prestazioni del dispositivo, sincronizzazione più frequente dei pacchetti installati e logica di confronto versioni migliorata. Il team ha corretto un problema critico con flutter_secure_storage e migliorato la gestione dei casi limite del package manager.

La milestone rappresenta la maturazione della prima piattaforma dedicata di distribuzione app di Nostr, permettendo agli sviluppatori di pubblicare applicazioni Android direttamente verso i propri utenti, aggirando il gatekeeping degli app store centralizzati.

### ZSP v0.3.1

[ZSP](https://github.com/zapstore/zsp), lo strumento CLI Go del team [Zapstore](https://github.com/zapstore/zapstore) che sostituisce il tooling di pubblicazione precedente di Zapstore per la firma e l'upload di app Android su relay Nostr, ha rilasciato [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1). ZSP gestisce l'acquisizione APK da GitHub, GitLab, Codeberg, F-Droid o file locali, poi analizza i metadata, firma eventi Nostr (tramite chiave privata, bunker [NIP-46](/it/topics/nip-46/) o estensione browser [NIP-07](/it/topics/nip-07/)), e carica i manufatti su server [Blossom](/it/topics/blossom/). Tra le novità: modalità offline completa per il linking del keystore anche in assenza di rete, header `Content-Digest` sugli upload Blossom per la conformità al protocollo, rilevamento corretto degli APK arm64-v8a dai repository F-Droid, fix dei parametri query trailing di GitLab e supporto completo file `.env` per la configurazione.

### Damus iOS 1.17

[Damus](https://github.com/damus-io/damus), il client Nostr per iOS, è passato alla versione 1.17 ([PR #3606](https://github.com/damus-io/damus/pull/3606)). Il rilascio corregge un problema RelayPool dove le connessioni si chiudevano dopo il rilascio del lease effimero ([PR #3605](https://github.com/damus-io/damus/pull/3605)), che poteva causare il drop inatteso delle sottoscrizioni. Risolve anche un bug dove la timeline dei preferiti non mostrava eventi nel passaggio tra tab ([PR #3603](https://github.com/damus-io/damus/pull/3603)).

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak), il Nostr army knife CLI, ha rilasciato [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) con tre fix di stabilità: prevenzione di un panic quando i tag AUTH challenge sono nil o troppo corti, controllo degli errori del dateparser prima di usare il valore analizzato, e gestione degli URL mint Cashu che mancano del separatore `://`.

### Mi: Relay Locale Basato su Browser

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git) ([mi.shakespeare.wtf](https://mi.shakespeare.wtf)), la nuova MiniApp [Shakespeare](https://shakespeare.wtf), è un relay locale basato su browser che archivia in IndexedDB gli eventi Nostr dell'utente. Mi recupera profili (kind 0), liste contatti (kind 3), liste relay (kind 10002) e eventi wallet dai relay connessi e li memorizza localmente, dando accesso offline ai propri dati. Costruito con React e nostr-tools 2.15.0.

### Agora v1.0.2

[Agora](https://gitlab.com/soapbox-pub/agora) ([agora.spot](https://agora.spot)), piattaforma decentralizzata di attivismo e raccolta fondi del team Soapbox, ha rilasciato [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2) con un APK Android disponibile per installazione diretta. Si tratta della prima menzione di Agora su Compass; la piattaforma è stata lanciata il 17 gennaio con la dichiarazione di missione: "Unisciti al movimento globale per la libertà. Invia supporto agli attivisti sul campo a livello internazionale e partecipa alle azioni locali."

La piattaforma si centra su una mappa mondiale dove chi la usa naviga per paese, crea "azioni" geolocalizzate (proteste, campagne, organizzazione comunitaria) e le discute tramite commenti threaded. Tutti i contenuti si propagano tramite relay Nostr, quindi nessun server centrale può essere messo offline per silenziare la coordinazione. Agora supporta più lingue con parità di traduzione imposta da CI, integra server media [Blossom](/it/topics/blossom/) per gli upload, e include ricerca, navigazione hashtag con toggle globale/regionale, profili utente e sistemi di reazione. Il rilascio v1.0.2 è la build Android corrente, disponibile come download APK diretto.

### xonos v0.1.6

[xonos](https://codeberg.org/xonos/xonos), il client Nostr 3D sperimentale costruito con il motore di gioco Bevy, ha rilasciato [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6). xonos renderizza eventi Nostr in un ambiente spaziale 3D con capacità text-to-speech, esplorando come i dati del protocollo sociale potrebbero funzionare al di fuori delle interfacce 2D convenzionali.

## Aggiornamenti dei Progetti

### Primal Android Espande l'Infrastruttura NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) ha unito 18 PR in settimana, continuando il lavoro NWC [iniziato la settimana scorsa](/it/newsletters/2026-02-04-newsletter/#primal-android-rilascia-crittografia-nwc). La [PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883) aggiunge supporto per connessioni NWC attraverso entrambi i wallet (Spark ed esterno), e la [PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879) implementa il metodo NWC `lookup_invoice` per controllare lo stato dei pagamenti.

La [PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880) aggiunge audit logging request-response NWC per il debugging delle interazioni wallet. La [PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877) introduce il supporto multi-account a `PrimalNwcService`, permettendo a chi ha più profili di mantenere connessioni wallet separate. La [PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882) implementa la pulizia periodica dei budget hold scaduti, prevenendo che prenotazioni di pagamento stale blocchino le operazioni wallet.

Il lavoro UI include ridisegno della schermata upgrade wallet ([PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)), FAQ sull'upgrade wallet ([PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)), impostazione indirizzo Lightning durante l'onboarding ([PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)) e un fix per le transazioni zap che apparivano come pagamenti regolari per i tipi non-Lightning ([PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)).

### diVine Rilascia Feed Video API-First

[diVine](https://github.com/divinevideo/divine-mobile), il client video short-form, ha unito 19 PR in settimana, spostandosi verso l'architettura API-first. La [PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468) introduce feed video API-first, e la [PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466) aggiunge endpoint API trending, recent e home. La [PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433) indicizza controller video specifici per un rendering efficiente dei feed.

La gestione profili è migliorata con la [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440) che implementa un pattern cache-plus-fresh per la visualizzazione di altri profili, riducendo i tempi di caricamento garantendo al contempo la freschezza dei dati. Il team ha anche rilasciato fix per le notifiche ([PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)), refactoring del flusso commenti ([PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)) e tab swiping sulla schermata Notifiche ([PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388)).

### White Noise: Unificazione Keyring e Ricerca Utenti

Il backend [White Noise](https://github.com/marmot-protocol/whitenoise-rs) per il protocollo [Marmot](/it/topics/marmot/) ha unito 4 PR in settimana. Due PR hanno migliorato la gestione del keyring: la [PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468) rende l'identificatore del servizio keyring configurabile tramite `WhitenoiseConfig`, e la [PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475) unifica l'implementazione su un singolo crate `keyring-core` con store nativi per piattaforma, sostituendo codice frammentato specifico per piattaforma. Separatamente, la [PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470) aggiunge funzionalità di ricerca utenti.

### Marmot TS Estrae l'App Chat di Riferimento

L'SDK TypeScript di [Marmot](/it/topics/marmot/) ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) ha unito la [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40), rimuovendo l'applicazione chat di riferimento integrata e separandola in un repository autonomo: [marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat). Il nuovo repo, creato il 6 febbraio, è un'implementazione di riferimento dell'SDK TypeScript Marmot con la propria pipeline CI, vista chat a tab e sistema di build indipendente. La separazione permette all'SDK di concentrarsi sulle funzioni di libreria mentre l'app chat itera sulla UX in modo indipendente.

Una PR aperta ([#41](https://github.com/marmot-protocol/marmot-ts/pull/41)) migra marmot-ts a ts-mls v2.0.0, portando un'API ridisegnata con oggetti contesto unificati, nuove utility di gestione messaggi (creazione eventi, lettura, deserializzazione), helper per i metadata dei key package, e supporto eventi di cancellazione.

### Aggiornamenti Alby Hub

[Alby Hub](https://github.com/getAlby/hub) ha unito 5 PR in settimana. La [PR #2049](https://github.com/getAlby/hub/pull/2049) aggiunge un Alby CLI all'interfaccia dell'app store. La [PR #2033](https://github.com/getAlby/hub/pull/2033) corregge la gestione di dati zap invalidi nella lista transazioni, e la [PR #2046](https://github.com/getAlby/hub/pull/2046) rimuove il metodo `ListTransactions` non utilizzato dall'interfaccia LNClient.

### Notedeck Rilascia Dashboard e Agentium

[Notedeck](https://github.com/damus-io/notedeck), il client Nostr cross-platform di Damus, ha unito 6 PR in settimana. La [PR #1247](https://github.com/damus-io/notedeck/pull/1247) aggiunge un'app dashboard iniziale. La [PR #1293](https://github.com/damus-io/notedeck/pull/1293) introduce Agentium, un ambiente di sviluppo multi-agente che trasforma l'assistente AI Dave in un sistema con due modalità AI e gestione agenti basata su scene. La [PR #1276](https://github.com/damus-io/notedeck/pull/1276) aggiunge un compositore messaggi multilinea con keybinding stile Signal, e la [PR #1278](https://github.com/damus-io/notedeck/pull/1278) fornisce miglioramenti delle prestazioni media. PR aperte degne di nota includono [infrastruttura outbox](https://github.com/damus-io/notedeck/pull/1288) e [pianificazione Git App](https://github.com/damus-io/notedeck/pull/1289) [NIP-34](/it/topics/nip-34/).

### Agora Rilascia un Importante Rinnovo della UI

[Agora](https://gitlab.com/soapbox-pub/agora) ha unito 7 PR in settimana insieme al rilascio v1.0.2. La [PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106) è la più grande, chiudendo 11 task UI attraverso impostazioni, modifica profilo, interazioni mappa, risultati ricerca, filtraggio commenti e gestione server Blossom. Il merge ha disabilitato i pulsanti reazione per chi non è autenticato (che prima riceveva errori silenziosi cercando di reagire ai post sulla mappa), corretto il panning della mappa sulla linea di cambio data, e aggiunto testo corrispondente in grassetto nei risultati di ricerca.

La [PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108) aggiunge conteggi commenti sotto i post del feed e nelle pagine thread. La [PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107) aggiunge retry automatico sui fallimenti di caricamento eventi con un pulsante di reload esplicito quando i tentativi si esauriscono. La [PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104) cambia la navigazione hashtag per default allo scope globale, dato che il default precedente limitato per paese spesso restituiva zero risultati.

La [PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109) aggiunge un passaggio CI che verifica la parità di traduzione tra tutte le lingue, facendo fallire la build se a qualche chiave manca un valore. La [PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110) taglia le note lunghe nei feed per preservare il ritmo di scroll, e la [PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111) corregge un problema di zoom iOS mobile quando si commentano azioni causato da font di dimensioni ridotte.

### Clawstr Rilascia CLI e Pulsanti Zap Lightning

[Clawstr](https://gitlab.com/soapbox-pub/clawstr), la piattaforma ispirata a Reddit dove agenti AI creano e gestiscono community su Nostr, ha unito 3 PR in settimana. La [PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11) sostituisce tutti i comandi manuali nak nelle definizioni skill dell'agente AI con il nuovo pacchetto `@clawstr/cli` (`npx -y @clawstr/cli@latest`), rimuovendo la costruzione manuale di eventi JSON a favore di comandi CLI e aggiungendo operazioni wallet (init, balance, zap, npc) e ricerca full-text [NIP-50](/it/topics/nip-50/).

La [PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13) aggiunge la pagina di documentazione "For Humans" e un componente `ProfileZapDialog`. Il pulsante zap appare sulle pagine profilo quando l'utente ha un indirizzo Lightning configurato e funziona anche non autenticati, usando LNURL-pay direttamente con importi sats preimpostati e visualizzazione codice QR. La [PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12) documenta il comando `wallet sync`, spiegando come i pagamenti verso indirizzi Lightning vengono trattenuti da NPC fino a che i rispettivi agenti sincronizzano esplicitamente i wallet.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti:**

- **[NIP-45: Risposta Relay HyperLogLog](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45 (Event Counting)](/it/topics/nip-45/) ora supporta il conteggio approssimativo HyperLogLog (HLL). I relay possono restituire valori registro HLL da 256 byte insieme alle risposte COUNT. I client uniscono questi registri da più relay per calcolare la cardinalità approssimativa evitando di scaricare set completi di eventi. Il caso d'uso principale: conteggi follower e reazioni indipendenti da un singolo relay come fonte autoritativa. Anche solo due eventi reazione consumano più banda del payload HLL da 256 byte. I client possono applicare le correzioni HyperLogLog++ per migliorare l'accuratezza su cardinalità ridotte.

- **[NIP-39: Tag Identità Spostati da Kind 0](https://github.com/nostr-protocol/nips/pull/2216)** - I tag di claim identità [NIP-39](/it/topics/nip-39/) (tag `i`) sono stati estratti dagli eventi metadata kind 0 a un nuovo kind dedicato 10011. La motivazione: quasi nessun client supporta questi tag, quindi aggiungono dimensione a ogni fetch kind 0 senza valore reale. Si tratta della prima di un ciclo di PR di estrazione kind 0 di vitorpamplona (vedi [sezione Notizie](#campagna-di-snellimento-kind-0)).

**PR Aperte e Discussioni:**

- **[NIP-XX: Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos propone un protocollo per accedere ai relay Nostr attraverso tunneling crittografato tramite un relay rendezvous pubblico. Il meccanismo abilita l'accesso a relay dietro NAT o firewall, inclusi relay personali in esecuzione su home server o dispositivi mobili. Il tunneling usa eventi kind 24891/24892 con crittografia [NIP-44](/it/topics/nip-44/) attraverso un relay rendezvous che non può decrittare il traffico. Applicazione pratica: qualsiasi client Nostr può esporre lo storage locale (IndexedDB, SQLite) come endpoint relay per la sincronizzazione cross-device. La semantica standard NIP-01 (REQ, EVENT, CLOSE, COUNT) passa attraverso il tunnel in modo trasparente. Implementazioni di riferimento esistono in Go (ORLY Relay) e TypeScript (Smesh).

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc propone Nostr Web Tokens, un formato evento Nostr per trasmettere claim firmati tra parti web, ispirato ai JSON Web Tokens (JWT). NWT può rappresentare sia [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (HTTP Auth) che [eventi di autorizzazione Blossom](/it/topics/blossom/), dando ai client flessibilità su come e quanto a lungo i token rimangono validi. Sono disponibili la libreria Go di riferimento, la [spiegazione video](https://github.com/pippellia-btc/nostr-web-tokens) e il [confronto dettagliato](https://github.com/pippellia-btc/nostr-web-tokens?tab=readme-ov-file#comparisons) con NIP-98 e Blossom Auth.

- **[Semplificazione NIP-47](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz propone di rimuovere i metodi `multi_` da [NIP-47 (Nostr Wallet Connect)](/it/topics/nip-47/), complessi da implementare e privi di adozione. La PR riduce anche la duplicazione nella gestione crittografia e retrocompatibilità, ripulendo la spec dopo [l'aggiunta hold invoice della settimana scorsa](/it/newsletters/2026-02-04-newsletter/#aggiornamenti-nip).

- **[NIP-05: Spostamento in un Kind Evento Proprio](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona propone di spostare la verifica NIP-05 da kind 0 a un nuovo kind 10008, abilitando più identificatori NIP-05 per utente e il filtraggio per indirizzo NIP-05. Parte della campagna di snellimento kind 0.

- **[NIP-57: Indirizzi Lightning da Kind 0](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona propone di estrarre lud06/lud16 (indirizzi Lightning) da kind 0 a un kind evento dedicato per [NIP-57](/it/topics/nip-57/), continuando lo sforzo di snellimento kind 0.

- **[Iperpersonalizzazione Profilo](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf propone capacità estese di personalizzazione profilo oltre a quanto kind 0 supporta attualmente.

## NIP Deep Dive: NIP-45 (Event Counting) e HyperLogLog

[NIP-45](/it/topics/nip-45/) ([spec](https://github.com/nostr-protocol/nips/blob/master/45.md)) definisce come i client possono chiedere ai relay di contare eventi corrispondenti a un filtro evitando di trasferire gli eventi stessi. Il merge del [supporto HyperLogLog](https://github.com/nostr-protocol/nips/pull/1561) aggiunge una struttura dati probabilistica che risolve un problema fondamentale: come contare cose attraverso più relay indipendenti.

**Il Problema:**

Contare eventi su un singolo relay è semplice: invia una richiesta COUNT, ottieni un numero indietro. Contare attraverso la rete è più difficile. Se il relay A riporta 50 reazioni e il relay B ne riporta 40, il totale non è 90 perché molti eventi esistono su entrambi i relay. Non è possibile calcolare il conteggio reale in assenza del download completo per deduplicare.

**HyperLogLog:**

HyperLogLog (HLL) è un algoritmo probabilistico che stima il numero di elementi distinti in un insieme usando un quantitativo fisso di memoria. L'implementazione NIP-45 usa 256 registri di un byte ciascuno, consumando esattamente 256 byte indipendentemente dal numero di eventi contati. L'algoritmo funziona esaminando la rappresentazione binaria di ciascun ID evento e tracciando la posizione degli zeri iniziali. ID evento che iniziano con molti zeri sono statisticamente rari, e la loro occorrenza indica un insieme grande.

**Come Funziona in NIP-45:**

Un relay che risponde a una richiesta COUNT può includere un campo `hll` contenente valori registro codificati in base64:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

Il client raccoglie i valori HLL da più relay e li unisce prendendo il valore massimo a ciascuna posizione registro. L'HLL unito rappresenta l'unione di tutti gli insiemi di eventi attraverso i relay, gestendo automaticamente la deduplicazione. La stima finale di cardinalità viene calcolata dai registri uniti.

**Accuratezza:**

Con 256 registri, l'errore standard è di circa il 5,2%. Per un conteggio reale di 1.000, la stima cadrà tipicamente tra 948 e 1.052. Per conteggi più grandi, l'errore relativo rimane costante: un conteggio reale di 100.000 verrà stimato in circa 94.800-105.200. Le correzioni HyperLogLog++ migliorano l'accuratezza per cardinalità ridotte (sotto ~200), dove l'algoritmo base tende a sovrastimare.

**Perché è Importante:**

Le metriche social (conteggi follower, conteggi reazioni, conteggi repost) sono tra le funzionalità core dei client social media. In assenza di HLL, i client devono interrogare un singolo relay "fidato" (centralizzando il conteggio) o scaricare tutti gli eventi da tutti i relay (sprecando banda). HLL permette ai client di ottenere un buon conteggio approssimativo da più relay con un overhead totale di 256 byte per relay, indipendentemente dal conteggio effettivo. Anche solo due eventi reazione consumano più banda di un payload HLL completo.

La spec fissa il numero di registri a 256 per l'interoperabilità. Tutti i relay producono valori HLL che i client possono unire, indipendentemente da quale implementazione relay usano. I client possono implementare il supporto HLL una volta e beneficiare di ogni relay che lo supporta.

**Stato Attuale:**

La PR è stata aperta da fiatjaf ed era in discussione da diversi mesi prima del merge avvenuto in settimana. Le implementazioni relay dovranno aggiungere il calcolo HLL ai loro handler COUNT. Le implementazioni client dovranno aggiungere il merging HLL alla propria logica di aggregazione conteggi.

## NIP Deep Dive: NIP-96 (HTTP File Storage) e la Transizione a Blossom

[NIP-96](/it/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) definiva come i client Nostr caricavano, scaricavano e gestivano file su server media HTTP. Ora contrassegnato come "non raccomandato" a favore di [Blossom](/it/topics/blossom/) (hosting media basato su BUD), NIP-96 resta rilevante in settimana perché Angor v0.2.5 [ha aggiunto la configurazione server NIP-96](#angor-v025) e ZSP v0.3.1 [carica su server Blossom](#zsp-v031), illustrando la transizione di protocollo in corso.

**Come Funziona NIP-96:**

Un client scopre le capacità di un file server recuperando `/.well-known/nostr/nip96.json`, che restituisce l'URL API, i tipi di contenuto supportati, i limiti di dimensione e le trasformazioni media disponibili:

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

Per caricare, il client invia un POST `multipart/form-data` all'URL API con un header di autorizzazione [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (un evento Nostr firmato che prova l'identità di chi carica). Il server restituisce una struttura metadata file [NIP-94](/it/topics/nip-94/) contenente l'URL del file, i hash SHA-256 originali e trasformati, il tipo MIME e le dimensioni:

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

I download usano richieste GET a `<api_url>/<sha256-hash>`, con parametri query opzionali per trasformazioni server-side come il ridimensionamento immagini (`?w=320`). La cancellazione usa DELETE con auth NIP-98, e solo chi ha caricato il file originale può cancellare i propri file. Un endpoint di elenco file restituisce risultati paginati dei caricamenti di un utente.

Chi pubblica eventi kind 10096 dichiara i propri server di upload preferiti, permettendo ai client di selezionare automaticamente il server giusto in assenza di configurazione manuale.

**Perché È Stato Deprecato:**

NIP-96 legava gli URL dei file a server specifici. Se `files.example.com` andava giù, ogni nota Nostr che referenziava quegli URL perdeva i suoi media. Il server era l'indirizzo, e l'indirizzo era fragile.

[Blossom](/it/topics/blossom/) (Blobs Stored Simply on Mediaservers) inverte il modello rendendo l'hash SHA-256 del contenuto del file l'identificatore canonico. Un URL Blossom ha la forma `https://blossom.example/<sha256>.png`, ma qualsiasi server Blossom che ospita lo stesso file lo serve allo stesso percorso hash. Se un server scompare, i client interrogano un altro server per lo stesso hash. L'indirizzamento basato sul contenuto rende i dati portabili tra server di default.

Blossom semplifica anche l'API. NIP-96 usava upload multipart form con risposte JSON, policy di trasformazione e un endpoint di discovery. Blossom usa semplice PUT per gli upload, GET per i download, ed eventi Nostr firmati (non header HTTP) per l'autorizzazione. La specifica Blossom è divisa in documenti modulari: BUD-01 copre il protocollo server, l'autorizzazione e il recupero, BUD-02 copre l'upload blob, BUD-03 copre i server utente, e BUD-04 copre il mirroring tra server.

La deprecazione è avvenuta a settembre 2025 tramite [PR #2047](https://github.com/nostr-protocol/nips/pull/2047), che ha contrassegnato NIP-96 come "non raccomandato" nell'indice NIPs.

**La Transizione in Pratica:**

Server come nostr.build e void.cat supportavano NIP-96 e hanno aggiunto o migrato a endpoint Blossom. I client sono a vari stadi: il rilascio v0.2.5 di Angor in settimana ha aggiunto la configurazione server NIP-96 per le immagini dei progetti, mentre il rilascio v0.3.1 di ZSP carica artefatti esclusivamente su server Blossom con header `Content-Digest` per la conformità al protocollo. Amethyst e Primal supportano gli upload Blossom. La coesistenza probabilmente continuerà fino a quando le rimanenti implementazioni NIP-96 completeranno la propria migrazione.

**Cosa Viene Preservato:**

I preference event kind 10096 rimangono utili per la selezione server Blossom. I metadata file NIP-94 (eventi kind 1063) descrivono ancora le proprietà dei file indipendentemente da quale protocollo di upload li ha creati. L'hashing SHA-256 che NIP-96 usava per gli URL di download è diventato la base dell'indirizzamento basato sul contenuto di Blossom. Il design di NIP-96 ha informato ciò che Blossom ha semplificato: la lezione è stata che l'hosting media su rete decentralizzata richiede storage indirizzato per contenuto per corrispondere alla resistenza alla censura del livello relay.

---

È tutto per questa settimana. Stai costruendo qualcosa? Hai notizie da condividere? Vuoi che copriamo il tuo progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattaci via DM NIP-17</a> o trovaci su Nostr.
