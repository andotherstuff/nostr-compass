---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "Amethyst su desktop, correzioni di sicurezza per Amber, allegati privati, installazioni software autenticate, avvisi sui contenuti e stato."
translationOf: /en/newsletters/2026-10-14-newsletter.md
translationDate: 2026-10-15
---

**[Amethyst](#amethyst)** porta la propria interfaccia Android su desktop e aggiunge il supporto nativo a Wayland. **[Amber](#amber)** corregge la revoca dei permessi, la cancellazione dei segreti copiati e una modifica alle impostazioni che poteva causare la perdita delle chiavi. **[Keep](#keep-android)** rende più rigorosi i permessi di firma automatica, mentre **[MDK](#mdk)** introduce allegati privati in streaming e il recupero dei messaggi a partire dai più vecchi. **[Zap Cooking](#zap-cooking)** integra protezioni per le modifiche all’elenco dei profili seguiti e l’iscrizione autenticata. Seguono i [dettagli delle versioni](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0), insieme alle modifiche al protocollo e ai meccanismi dello stato pubblico.

## Notizie principali

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) porta su desktop l’interfaccia condivisa del client social Android, con feed personalizzati, pannelli per finestre ampie, blocchi facoltativi, contenuti multimediali crittografati e [caricamenti su Blossom](/it/topics/blossom/). I punteggi dei fornitori di [NIP-85, attestazioni fidate](/it/topics/nip-85/), vengono indicizzati localmente per richieste, notifiche e badge, con fornitori e soglie scelti dall’utente.

La [versione v1.19.0 di oggi](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) aggiunge il supporto nativo a Wayland e la compressione video su desktop tramite FFmpeg e ffprobe installati separatamente. Le correzioni all’archiviazione delle chiavi risolvono le richieste ripetute del portachiavi e i malfunzionamenti del keyring su Linux. Viene aggiunta la visualizzazione delle raccolte di calendari e delle risposte RSVP, mentre l’interfaccia di accesso Android introduce la [firma remota NIP-46](/it/topics/nip-46/). L’apertura parallela delle buste crittografate precede l’indicizzazione seriale, mentre vengono corrette la riconnessione ai relay e la gestione degli elenchi di relay degli autori dei feed. Il [client relay rispetta l’attesa imposta dai limiti di frequenza](https://github.com/vitorpamplona/amethyst/pull/4422) prima di riprendere le sottoscrizioni o le pubblicazioni.

La [modifica ai relay dei fornitori di fiducia](https://github.com/vitorpamplona/amethyst/pull/4437) tratta i relay dei fornitori presenti nell’elenco kind 10040 dell’utente come relay propri e fidati. Queste connessioni utilizzano per impostazione predefinita un percorso diretto; per usare Tor occorre abilitare l’impostazione relativa ai relay fidati. L’[autenticazione ai relay NIP-42](/it/topics/nip-42/) del client principale può rivelare la chiave pubblica dell’utente a questi relay.

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) corregge tre vulnerabilità di sicurezza nel firmatario Nostr per Android. I [permessi revocati](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw) non sopravvivono più a una condizione di concorrenza nella cache, e i rifiuti espliciti prevalgono sullo stato di piena fiducia. Per i [segreti copiati](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p) viene programmata dal sistema la cancellazione dagli appunti dopo 60 secondi, anche se il processo viene terminato; i contenuti restano leggibili durante tale intervallo e anche il testo copiato successivamente potrebbe essere cancellato. La modifica dell’impostazione [«richiedi dispositivo sbloccato»](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5) conserva la vecchia chiave di protezione fino al completamento della migrazione dei segreti, mentre le chiavi perse in precedenza restano perse. La versione corregge le approvazioni nostrconnect con più richieste e invia le risposte sui relay specificati nell’URI. Gli utenti della versione 6.6.8 e precedenti dovrebbero aggiornare.

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0), un [firmatario a soglia FROST](/it/topics/frost/), aggiunge la generazione distribuita delle chiavi sui dispositivi e il recupero autenticato delle operazioni interrotte sulle quote. Gestisce inoltre i dispositivi privi del supporto a StrongBox. Con la firma a soglia, i dispositivi partecipanti detengono quote del segreto di firma e cooperano per produrre una firma; le fasi di configurazione e recupero determinano quali dispositivi possono partecipare.

La [versione 1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1) impedisce alla firma automatica di scavalcare i rifiuti memorizzati, i permessi impostati su Chiedi, le approvazioni scadute o gli errori di lettura dei permessi. La scadenza rimuove l’approvazione in background, mantenendo però i dinieghi. La [migrazione delle regole per singola app](https://github.com/privkeyio/keep-android/pull/532) sposta i permessi nell’archivio gestito dal nucleo dell’applicazione, conservando le decisioni più restrittive.

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) [autentica il bridge del wallet nativo](https://github.com/jesuspirate/chama/pull/29) utilizzato dalla sua applicazione di scambio mediata da Nostr, disabilita in produzione il reindirizzamento del bridge basato su URL e convalida gli importi dei pagamenti. Rifiuta inoltre di cancellare un wallet il cui contenuto non può essere letto.

La [versione 6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22) rafforza la resistenza al replay degli event provenienti da soggetti esterni, verifica le relazioni di successione, rifiuta gli insiemi vuoti di arbitri e ricava le tempistiche di rimborso dall’orario LOCK firmato. Le modifiche al consenso si applicano agli event CREATE firmati a partire dal 1º novembre 2026; le protezioni del client si applicano immediatamente. Le note di rilascio mantengono le riserve sulle federazioni selezionate negli annunci e sui pagamenti di importi minimi. Le successive [modifiche al firmatario e al recupero](https://github.com/jesuspirate/chama/releases/tag/v6.4.23) aggiungono lettori per seed protetti e blocchi tardivi recuperabili, mentre la [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24) migliora gli elenchi di scambi di grandi dimensioni.

### Zap Cooking

Il client di ricette e social [Zap Cooking integra protezioni per le modifiche all’elenco dei profili seguiti](https://github.com/zapcooking/frontend/pull/795) contro letture incomplete, obsolete o con riduzioni inattese. Le azioni per seguire i profili condividono un unico percorso di aggiornamento protetto che conserva i tag e i contenuti esistenti. L’identità del firmatario viene verificata prima della pubblicazione. La sua [correzione dell’autorizzazione all’iscrizione](https://github.com/zapcooking/frontend/pull/802) utilizza la chiave pubblica che firma la richiesta autenticata. È stata [rimossa una route che esponeva un segreto amministrativo](https://github.com/zapcooking/frontend/pull/801); in fase di distribuzione è comunque necessaria la rotazione del segreto, che la sola integrazione di una modifica non può attestare. Le successive [correzioni a thread e segnalibri](https://github.com/zapcooking/frontend/pull/833) preservano la vera radice delle risposte e recuperano le scritture dei segnalibri non riuscite. I [campi dei tag delle ricette](https://github.com/zapcooking/frontend/pull/836) non inviano più le battute ai servizi di ricerca dei profili o NIP-50 e non provocano più l’uscita dall’editor con modifiche non salvate.

## Versioni con tag

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0), l’ambiente di esecuzione per i [gruppi crittografati Marmot](/it/topics/marmot/), aggiunge allegati privati in streaming e riprendibili, con indicazione dell’avanzamento e possibilità di annullamento. Invia inoltre [segnalazioni NIP-56](/it/topics/nip-56/) private all’operatore dell’istanza tramite [gift wrap NIP-59](/it/topics/nip-59/), omettendo gli identificatori di messaggi, gruppi e relay. Il recupero elabora lotti di un massimo di 256 event a partire dai più vecchi e conserva i rifiuti CLOSED dei relay. L’instradamento SOCKS5 copre relay, contenuti multimediali e servizi di individuazione senza ripiego su una connessione diretta.

La [guida al rilascio](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md) richiede che binding, header e artefatti nativi vengano aggiornati insieme. Gli schemi del database avanzano da 101 a 107 senza possibilità di tornare a una versione precedente. L’archiviazione dei segreti dell’host richiede una migrazione. MarmotKit e gli artefatti C sono stabili; WN Agent resta una versione preliminare e i crate del workspace non sono pubblicati su crates.io. La cronologia che arriva con un ritardo superiore a cinque [epoche MLS](/it/topics/mls/) può ancora risultare impossibile da decrittografare senza un avviso di cronologia incompleta, e i client agent autenticati mantengono l’accesso all’intera API.

La versione inoltre [ritenta i salvataggi di profilo, elenco dei profili seguiti ed elenco dei relay rimasti in sospeso dopo la prima conferma](https://github.com/marmot-protocol/mdk/pull/2228); questi tentativi in background non sopravvivono al riavvio. La [ricerca degli inviti verifica l’eliminazione e la scadenza dei KeyPackage sui relay di individuazione](https://github.com/marmot-protocol/mdk/pull/2211), le cui risposte non possono dimostrare che il destinatario detenga ancora il materiale privato del proprio KeyPackage. I [destinatari delle reazioni alle attività](https://github.com/marmot-protocol/mdk/pull/2187) vengono ora ricavati in modo coerente dagli attori autenticati e dai singoli commit di gruppo; la cronologia precedente priva di attore resta incompleta.

Modifiche successive al ramo master [chiudono le sottoscrizioni ai relay rimaste aperte e suddividono in pagine i replay di attivazione limitati a 500 event](https://github.com/marmot-protocol/mdk/pull/2274). Il [recupero dei divari tra epoche](https://github.com/marmot-protocol/mdk/pull/2298) recupera i 256 event più recenti di un relay per il quale il confronto è fallito, senza certificare la completezza della cronologia. [I commit di autoaggiornamento ritentano l’invio a ogni relay del gruppo non raggiunto](https://github.com/marmot-protocol/mdk/pull/2275). Nuovi controlli di avviso riguardano le [epoche notoriamente obsolete](https://github.com/marmot-protocol/mdk/pull/2273) e i [commit ancora da inviare ai relay](https://github.com/marmot-protocol/mdk/pull/2288); gli utenti possono accettare il rischio, quindi questi controlli non garantiscono che un gruppo non possa biforcarsi.

I [download di allegati bloccati per mancanza di spazio](https://github.com/marmot-protocol/mdk/pull/2249) conservano i progressi per poter riprendere quando lo spazio libero è insufficiente. I download espliciti di grandi dimensioni scrivono direttamente su file, con un’area temporanea e checkpoint che richiedono uno spazio libero pari a circa cinque o sei volte la dimensione del contenuto. Le [anteprime verificate degli event pubblici](https://github.com/marmot-protocol/mdk/pull/2304) acquisiscono una cache cifrata per account di dimensioni limitate, mentre i [risultati KeyPackage contenenti solo elementi obsoleti](https://github.com/marmot-protocol/mdk/pull/2305) diventano distinguibili dalle ricerche incomplete sui relay. Si tratta di modifiche successive al codice sorgente che richiedono un’adozione corrispondente da parte dell’applicazione ospitante; le anteprime basate sull’ID dell’event ottenute da recuperi completati non ricontrollano eventuali eliminazioni successive.

I bridge degli agenti inoltre [limitano l’output del backend](https://github.com/marmot-protocol/mdk/pull/2103) per impedire che risposte troppo grandi esauriscano la memoria e [accettano l’effettiva risposta di eliminazione del connettore](https://github.com/marmot-protocol/mdk/pull/2301). Il testo già consegnato rimane consegnato quando un limite di output interrompe un turno.

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0) aggiunge collegamenti USB tra telefoni o computer desktop fips e adotta [l’attuale formato di manifest proposto da NIP-5D](https://github.com/Origami74/myco/pull/135), con hash firmati degli artefatti e delle icone. I telefoni meno recenti possono ancora essere abbinati, ma devono essere aggiornati per aprire queste napplet. Le sue [modifiche alle politiche di download](https://github.com/Origami74/myco/pull/133) distinguono tra destinazioni HTTP su Internet, sulla mesh e configurate dall’utente. I suggerimenti forniti dall’autore e i reindirizzamenti non possono sondare le reti locali con la politica Internet, mentre le destinazioni configurate dall’utente restano prive di restrizioni. Il client software inoltre [individua i blob sui server Blossom BUD-03 dell’autore](https://github.com/Origami74/myco/pull/134). Questo migliora l’individuazione degli artefatti, ma espone il traffico di installazione a tali server. Queste modifiche HTTP non introducono protezioni equivalenti per le connessioni WebSocket. I [controlli di disponibilità sulla mesh nelle vicinanze](https://github.com/Origami74/myco/pull/132) interrogano i peer per verificare la presenza di blob senza scaricarli né contattare server Blossom pubblici. Queste richieste HEAD limitate richiedono l’autorizzazione per la mesh; il numero di detentori non dimostra che l’intero artefatto sia ancora disponibile.

La versione inoltre [interroga in parallelo i server DNS a monte, usando la prima risposta](https://github.com/Origami74/myco/pull/137), per evitare che i timeout dell’operatore in roaming blocchino la ricerca di relay e artefatti. Le pubblicazioni outbox sono indirizzate a ogni relay di scrittura elencato, con consegna alle destinazioni più lente in background. La mesh su Internet rimane disattivata per impostazione predefinita e le immagini web non vengono conservate tra un riavvio e l’altro.

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13) aggiunge elenchi di relay di lettura e scrittura e instradamento outbox al suo client fotografico per Android. Le sue [note di rilascio](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2) descrivono i ruoli dei relay, e gli account senza un elenco iniziano con tre relay pubblici predefiniti. La funzione Nearby usa geohash a bassa precisione e celle adiacenti; l’aggiunta della posizione a un post richiede un consenso esplicito ed è disattivata per impostazione predefinita. Questi tag rivelano comunque pubblicamente un’area. Il risultato di pubblicazione esaminato indica l’accodamento a un socket, mentre l’accettazione da parte del relay resta non confermata.

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0) consente agli utenti di ricevere mance in Monero tramite un servizio di monitoraggio personale, mentre [0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0) nasconde per impostazione predefinita gli importi delle mance e i nomi dei mittenti nelle notifiche delle nuove configurazioni. Per impostazione predefinita le immagini si caricano solo al tocco, e i conteggi facoltativi di Primal e i tag del client sono disattivati. Un servizio di monitoraggio ospitato viene comunque a conoscenza di ogni pagamento in entrata al portafoglio registrato tramite la sua chiave di visualizzazione privata. Le ricevute pubbliche conservano il destinatario, l’ora e il post di riferimento anche quando gli importi sono nascosti.

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2) combina liste della spesa condivise e cifrate con identità Nostr basate su passkey e chat Marmot per ciascuna lista. È possibile unirsi a una lista incollando una chiave al portatore, che concede l’accesso in lettura e modifica. L’accesso tramite passkey dipende dal supporto del browser e del fornitore per l’estensione a funzione pseudocasuale di WebAuthn; i tag dei membri restano visibili ai relay. La [versione 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3) conserva le liste alla riapertura memorizzando localmente nella cache i contenuti decifrati, risolvendo i casi in cui sopravviveva solo la chiave finché un relay non consegnava nuovamente la lista.

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0) legge gli event di kind 1315/1316 di un altro client Roadstr rispettandone i periodi di validità e le regole di conferma previsti. Un codec compatto conserva segnalazioni firmate ricostruibili per un bridge sperimentale tra radio MeshCore e relay. La pubblicazione compatibile e la trasmissione radio sono disattivate per impostazione predefinita, con richiesta di consenso prima della condivisione. Le segnalazioni radio espongono posizione, ora e chiave pubblica di firma a chiunque si trovi nel raggio di copertura. I test hanno usato radio simulate; l’hardware reale, Android BLE e la pubblicazione su relay pubblici restano non verificati.

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3) migliora i commenti agli articoli e la gestione dei post citati nel suo client Android. I commenti agli articoli usano kind 1111 con l’articolo come radice e il commento come elemento padre, mentre le normali risposte alle note restano di kind 1. L’individuazione delle citazioni accetta sia i tag q sia le precedenti menzioni `e` contenenti link; le citazioni appena pubblicate aggiungono tag q. Una pubblicazione fallita annulla le reazioni applicate in modo ottimistico.

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28) descrive la [lettura di indici di pubblicazione annidati](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0) di kind-30040 contenenti sia capitoli sia indici figli nell’ordine stabilito dall’editore. Le copie offline conservano tale gerarchia e i segnalibri associati a ciascuna occorrenza. L’aggiornamento recupera le revisioni correnti tramite le coordinate, ma mantiene il download precedente quando i risultati sono incompleti, meno recenti o non riusciti. La ritrasmissione conserva i discendenti originali firmati. L’espansione limitata e i rami parziali leggibili impediscono che una struttura incompleta venga presentata come un libro completo.

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0) sostituisce Global con Discover nei suoi feed di contenuti. Discover attinge alle persone seguite dagli account che l’utente segue e ordina i post in base alle connessioni condivise, escludendo l’utente stesso e gli account già seguiti. Gli utenti non autenticati e gli account che non seguono nessuno vedono invece una rete iniziale selezionata. Questo circoscrive la scoperta predefinita a un vicinato sociale; la resistenza allo spam e l’affidabilità di tali account restano questioni distinte.

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x) mantiene le identità dei profili selezionati associate alle menzioni durante il salvataggio delle bozze e la pubblicazione. L’editor blocca l’account, il testo, le menzioni e gli allegati durante la firma e l’invio, trattenendo le condivisioni in arrivo fino al termine dell’operazione. I nuovi tentativi conservano l’event firmato originale, inclusi i post meno recenti ancora in sospeso. Digitare un nome dopo @ non è sufficiente: gli utenti devono selezionare un profilo, e le identità già perse nelle vecchie bozze devono essere selezionate di nuovo.

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0) collega le comunità ai loro incontri. L’approvazione per un incontro collegato può anche concedere l’iscrizione alla comunità senza una seconda approvazione; il modulo di adesione lo dichiara e consente ai richiedenti di rinunciarvi. Chi partecipa già riceve un invito accettabile con un solo tocco. Gli incontri mantengono i propri partecipanti, abbinamenti e chat, mentre la comunità elenca i propri incontri. Le note di rilascio descrivono il supporto per coordinatori diversi per incontri e comunità, senza attestare verifiche indipendenti di interoperabilità o crittografia.

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1) corregge l’elaborazione dei pagamenti tramite [Nostr Wallet Connect](/it/topics/nip-47/) su Android, che poteva interrompersi mentre il wallet era in background e accumulare operazioni fino a causare un errore di mancata risposta dell’applicazione. La versione nativa incorpora cinque mesi di precedenti modifiche distribuite via OTA. La [versione 0.4.5 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1) corregge il trasferimento NFC da Android a iOS; i futuri aggiornamenti via OTA richiedono questa versione. Si tratta di correzioni dichiarate nelle note di rilascio; l’elaborazione in background resta soggetta alle restrizioni del telefono sul ciclo di vita delle applicazioni.

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0) consente agli utenti di pubblicare ricette dal suo editor di articoli, aprire raccolte di ricette condivise e sfogliare le ricette degli autori seguiti. Le schede dei siti web e le griglie dei profili descritte la scorsa settimana sono ora incluse nella versione, insieme alla gestione dei limiti di frequenza dei relay e ai collegamenti diretti `nostr:` su Android. I collegamenti ai siti web restano distinti dalla verifica dei loro contenuti; l’accesso tramite gateway espone a quel gateway la richiesta generata dal clic.

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2) rende disponibile su Android la propria piattaforma di sviluppo collaborativo Git basata su Nostr, usando Amber tramite la [firma remota NIP-46](/it/topics/nip-46/). L’APK apre l’applicazione ospitata già esistente `gittr.space`, quindi gli utenti continuano a dipendere dal codice per il browser che essa distribuisce e dalla sua disponibilità. La firma tramite estensione del browser non è disponibile all’interno di questo contenitore; l’hosting autonomo rimane una distribuzione Git separata.

### Dart NDK

[Dart NDK 0.11.0 development zero](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0) introduce in una versione preliminare il [gestore del consenso all’autenticazione](https://github.com/relaystr/ndk/pull/862) del toolkit per Dart e Flutter e il cambio dei relay del firmatario NIP-46. Queste modifiche erano state descritte la scorsa settimana come lavoro già integrato e ora sono state rilasciate. Il firmatario può seguire un elenco sostitutivo di relay, che le applicazioni devono salvare in modo persistente. [Development one](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1) aggiunge il supporto per gli identificatori NIP contenenti lettere nelle informazioni dei relay. Entrambe le versioni introducono modifiche incompatibili con le integrazioni esistenti.

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0) offre alle app Android native [quattro opzioni di approvazione](https://github.com/forgesworn/cambium/pull/32): una sola volta, un’ora, un giorno o a tempo indeterminato. Le autorizzazioni sono circoscritte per operazione e kind dell’event. Cambium inoltra le richieste a un firmatario hardware Heartwood tramite firma remota; resta Heartwood a decidere quali richieste firmare. Le approvazioni per i siti web rimangono valide per una sola operazione. I firmatari associati ottengono controlli per i test e la riconnessione, aggiornamenti dei relay di trasporto supportati e diagnostica con dati sensibili oscurati. I batch [NIP-55, firma su Android](/it/topics/nip-55/), preservano l’ordine delle richieste e i singoli rifiuti, con un consenso esplicito valido una sola volta per gli intent riutilizzati ambigui.

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1) corregge l’[autenticazione dei relay NIP-42](/it/topics/nip-42/) nella propria libreria client Go per le applicazioni che servono più utenti. Ogni `UserContext` dispone di connessioni autenticate private, preferenze dei relay e meccanismi per mantenere aperte le connessioni; il pool condiviso non esegue mai l’autenticazione. La libreria convalida gli ID e le firme in ingresso, verifica la corrispondenza con le sottoscrizioni e serializza correttamente i filtri per tag e tempo. I chiamanti autenticati devono migrare a `UserContext`. L’archiviazione e la distribuzione dei dati da parte dei relay restano invariate e l’autenticazione richiede ancora una challenge all’apertura della connessione.

### Nmail

[Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0), un client di posta crittografata, colloca i mittenti sconosciuti in Richieste e quelli bloccati in Spam. L’accettazione e il blocco si sincronizzano tra i dispositivi. I mittenti già presenti nella posta in arrivo devono essere accettati, con l’opzione Accetta tutti disponibile; Spam non genera avvisi e le richieste in attesa evitano avvisi ripetuti per lo stesso mittente. Le risposte usano l’identità destinataria. La gestione dei relay privati, i controlli sul blocco del dispositivo prima di copiare i codici di sincronizzazione, i temi condivisi, una conservazione più completa dei dati dei contatti e un programma di installazione per Windows accompagnano le correzioni al ripristino della casella di posta dopo una reimpostazione o un accesso.

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0) introduce commenti crittografati e indicatori di elementi non letti nel proprio gestore di attività sincronizzato tramite Nostr. I commenti usano event indirizzabili di kind 35002 con [crittografia NIP-44](/it/topics/nip-44/), mantenendo l’associazione con l’attività all’interno del testo cifrato. La versione [corregge gli invii offline](https://github.com/higedamc/meiso/pull/212), il recupero degli aggiornamenti alla riconnessione, l’avvio con i relay salvati e la propagazione degli elenchi vuoti. Impedisce inoltre che una sincronizzazione parziale elimini le attività. Le funzioni per gli elementi non letti e il recupero degli aggiornamenti non aggiungono un servizio di notifiche quando l’applicazione è chiusa.

### Haps

[Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13), un programma sperimentale per l’installazione di software, richiede per impostazione predefinita una verifica della versione esatta da parte della [rete di fiducia](/it/topics/web-of-trust/) dell’utente. Le verifiche possono confrontare il codice sorgente fissato a una revisione specifica e gli artefatti ricompilati, e rimanere private oppure essere pubblicate. La [versione 0.1.14](https://github.com/mmalmi/haps/releases/tag/v0.1.14) chiede agli utenti di confermare l’autore della pubblicazione quando installano usando il solo nome; le procedure automatizzate devono specificarne uno. Le verifiche forniscono elementi di riscontro, mentre i programmi nativi e le ricette di compilazione continuano a essere eseguiti senza una sandbox. Il requisito della verifica può essere aggirato per una singola operazione; restano i controlli su firma, integrità e conferma dell’autore della pubblicazione.

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0) aggiunge la [scoperta e la riproduzione di dirette streaming](https://github.com/dmnyc/sidecar/pull/479) al proprio client social sotto forma di estensione del browser, con chat firmata, reazioni e zap. I segnalibri delle dirette salvati supportano il backup e il ripristino crittografati dell’account, e le impostazioni private per silenziare le notifiche consentono agli utenti di controllare gli avvisi. La ricerca acquisisce comandi per seguire e silenziare; a questi si affiancano modifiche al blocco automatico e all’aggiornamento della cronologia del wallet.

### Ants

L’interfaccia di ricerca [Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0) [instrada le ricerche strutturate](https://github.com/dergigi/ants/pull/316) verso i relay di scrittura dichiarati dagli autori e i relay di lettura degli utenti menzionati tramite gli [elenchi di relay NIP-65](/it/topics/nip-65/), senza richiedere l’accesso. La fase di individuazione limita il numero di identità e relay consultati e si interrompe in caso di annullamento o timeout. In assenza di elenchi viene mantenuto l’instradamento di ripiego. Le query testuali continuano a usare [relay di ricerca NIP-50](/it/topics/nip-50/) verificati.

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0), uno strumento per pubblicare ed eseguire napplet per le [applicazioni NIP-5D](/it/topics/nip-5d/) proposte, aggiunge scorciatoie da tastiera e proposte senza fork tramite GRASP, un servizio di hosting Git, con controlli sulla revisione esatta nei nuovi tentativi. La sua [versione v0.26.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0) distribuisce le versioni firmate ai relay outbox verificati dopo la pubblicazione primaria; l’eliminazione tiene traccia delle destinazioni tentate, ma non può ritirare copie sconosciute. La [versione 0.26.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1) porta a 100 MiB i limiti per lettura, esecuzione e revisione, mantenendo un limite di 25 MiB per le nuove compilazioni e la pubblicazione. I successivi [metadati di presentazione diretti](https://github.com/zeSchlausKwab/napplet-soy/pull/14) collocano copertine e clip degli autori direttamente sui manifest firmati, eliminando l’event complementare. I vecchi job congelati restano supportati; questa estensione Soy con versione richiede lettori compatibili e non fa parte della specifica NIP-5D fissata a una revisione specifica.

### nostream

Il server relay [nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0) aggiunge sonde di [monitoraggio dei relay NIP-66](/it/topics/nip-66/) per i tempi di andata e ritorno delle letture e scritture WebSocket, il rilevamento dell’autenticazione opzionale e l’individuazione delle destinazioni di mirroring. Segnala quando il comportamento osservato non corrisponde alle [informazioni del relay NIP-11](/it/topics/nip-11/). Le risposte OK soggette a limitazione della frequenza possono includere un quinto elemento opzionale contenente un tempo di attesa in millisecondi. La [versione 3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0) aggiunge alle [risposte CLOSED](https://github.com/cameri/nostream/pull/821) un quarto elemento, un tempo di attesa in millisecondi, quando i limiti sui messaggi per IP rifiutano `REQ` o `COUNT`. Include il [nucleo di riconciliazione negentropy per PostgreSQL](https://github.com/cameri/nostream/pull/809) e un inventario ordinato degli event; i messaggi del protocollo di comunicazione dei relay e l’annuncio delle funzionalità previsti da [NIP-77](/it/topics/nip-77/) restano interventi separati.

### Bark

[Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15) introduce comandi da tastiera per le approvazioni della firma remota, una verifica esplicita di event e identità e [uno, cinque o dieci minuti per decidere](https://github.com/forgesworn/bark/pull/52). I controlli in background rifiutano le decisioni scadute e le richieste in coda; se l’invio della decisione fallisce, il popup rimane aperto per consentire un nuovo tentativo. La [versione 1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17) rende disponibile la [firma nel browser NIP-07](/it/topics/nip-07/) al completamento dell’handshake con il firmatario, mentre la diagnostica opzionale prosegue. Ripristina i bridge nelle schede già aperte dopo gli aggiornamenti.

### Mostro

[Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3) risponde alle richieste autenticate tramite identità relative alla reputazione dell’utente stesso, anche in assenza di un ordine aperto. La piattaforma di scambio peer-to-peer invia le risposte privatamente alla chiave di negoziazione richiedente, e un [comando CLI integrato](https://github.com/MostroP2P/mostro-cli/pull/203) rende disponibile questa interrogazione. L’importazione della reputazione rimane un’anteprima nella quale le importazioni non sono implementate; gli operatori dovrebbero lasciarla disabilitata. Un [intervento integrato successivamente](https://github.com/MostroP2P/mostro/pull/1057) pubblica il margine del guardiano dell’escrow Lightning e rifiuta le configurazioni non sicure; il minimo di 18 blocchi presuppone l’impostazione predefinita di LND per la scadenza degli hold.

### Elisym

[Il componente commerce 0.11.0 di Elisym](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0) supporta commissioni detratte dai ricavi del commerciante, con un tag firmato del profilo del negozio che dichiara il supporto ai pagamenti ripartiti e il rifiuto dei negozi incompatibili quando si applica una commissione. Un [intervento amministrativo integrato](https://github.com/elisymlabs/elisym/pull/170) legge ordini e inserzioni dai relay Nostr. Richiede la chiave segreta del negozio, rendendo necessaria la fiducia nel codice fornito al browser e nelle estensioni; l’interfaccia amministrativa locale rimane disponibile. La distribuzione in hosting e l’attivazione delle commissioni su mainnet restano non verificate. [Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0) aggiorna il proprio registro contabile senza supportare il ritorno a una versione precedente.

### Routstrd

[Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16) impedisce che una ricarica tramite [Nostr Wallet Connect](/it/topics/nip-47/) scaduta per timeout produca immediatamente un’altra fattura pagabile. [Controlla l’operazione di mint esistente](https://github.com/Routstr/routstrd/pull/144) finché il pagamento non riesce o fallisce; se lo stato non è disponibile, la ricarica rimane sospesa. Il gateway di inferenza abilita i fornitori in base all’etichetta di revisione Nostr, mentre le etichette sperimentali richiedono un’adesione esplicita. La [versione 0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17) include l’SDK di supporto. La protezione contro le operazioni non ancora regolate rimane in memoria, quindi il riavvio del daemon la fa perdere.

### Buzz

[Buzz desktop 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28) consente al personale autenticato di [consultare e moderare tutte le comunità](https://github.com/block/buzz/pull/8027) su un relay senza cambiare connessione. Le azioni amministrative mantengono la comunità esaminata, il relay e il firmatario; se l’autenticazione è disabilitata, la console rimane disponibile per la lettura. Separatamente, un [intervento sul relay integrato](https://github.com/block/buzz/pull/8197) nasconde, sia nelle query sia nell’invio in tempo reale, gli event di eliminazione correttamente contrassegnati con tag relativi a record privati degli autori. Questa correzione lato server richiede la distribuzione e non copre le copie già divulgate né i record storici di eliminazione privi di tag.

### Earthly

[Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21) consente agli utenti di [incorporare nei siti web dataset cartografici pubblici di Nostr](https://github.com/zeSchlausKwab/earthly/pull/35), con un’anteprima e controlli per l’aspetto e la posizione iniziale della camera. L’integrazione Maps MCP crea e pubblica mappe dalla chat, quindi genera link di condivisione o incorporamenti. L’integrazione rimane un progetto pilota personale con plugin connesso. Gli incorporamenti supportano dataset inline fino a 300 elementi geografici e 48 KiB; sono esclusi i dataset privati, non pubblicati e basati su blob.

### Milk Market

[La versione mobile v0.3.0 di Milk Market](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0) introduce nell’app per i venditori editor completi per la progettazione delle vetrine, con le stesse sezioni e gli stessi campi dell’editor web. Il design della pagina di ciascun prodotto può sostituire le scelte relative al tema e alle sezioni, inclusi i metadati e le immagini per i social. La versione aggiunge controlli per mantenere allineate le configurazioni mobile e web. La [versione 0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1) corregge il contrasto nella scheda di anteprima mobile; i download per Android sono allegati alle release, mentre la versione iOS è disponibile su TestFlight.

### Zeus

[Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3) include la [correzione delle commissioni di instradamento LDK](https://github.com/ZeusLN/zeus/pull/4353) trattata la settimana scorsa, ora rilasciata. Il suo servizio Nostr Wallet Connect basato su LDK può includere le commissioni di instradamento riportate nelle risposte e nei registri di spesa. I controlli del budget continuano a coprire l’importo della fattura prima del regolamento, con le commissioni arrotondate addebitate in seguito e un limite separato di 1.000 satoshi per le commissioni di instradamento. La versione aggiorna anche LND incorporato e include correzioni di sicurezza per rust-lightning; la convalida dal vivo con dispositivi NWC rimane non verificata. La successiva [rimozione di Zaplocker, già integrata](https://github.com/ZeusLN/zeus/pull/4933), ritira il relativo flusso di attestazione e riscatto Nostr. L’aggiornamento mentre i pagamenti sono ancora trattenuti da quel server elimina la possibilità di riscatto; i mittenti devono attendere la scadenza della hold-invoice e il rimborso. Questo ritiro non fa parte di v13.2.3; la sua introduzione dipende dalla disattivazione del server e dall’avviso agli utenti esistenti.

## In sviluppo

### nosvelte

[La correzione del verificatore di event di nosvelte](https://github.com/akiomik/nosvelte/pull/162) confronta l’ID fornito per un event con l’hash canonico dei suoi campi prima di verificare la firma. In precedenza, il verificatore predefinito della libreria Svelte accettava campi correttamente firmati che riportavano un ID sostituito, consentendo al contenuto di assumere l’identità di un altro event e di interferire con la gestione delle sostituzioni. La modifica integrata si applica ai percorsi di richiesta e invio della versione uno che utilizzano il verificatore predefinito; non certifica l’esportazione legacy né i verificatori personalizzati rispetto al [formato degli event di NIP-01](/it/topics/nip-01/). Una successiva [correzione dei filtri di richiesta](https://github.com/akiomik/nosvelte/pull/171) controlla e copia i campi degli event del relay prima di verificarne la corrispondenza. I dati malformati non possono più terminare la sottoscrizione del provider predefinito né causare lo scarto del suo event valido successivo. I client del motore forniti dal chiamante possono mantenere il precedente comportamento di corrispondenza della dipendenza.

### nostter

nostter [limita gli indizi sui relay forniti dall’esterno](https://github.com/SnowCait/nostter/pull/2684) agli URL WebSocket sicuri, rifiutando i nomi host locali e gli indirizzi IP non globali. I relay locali selezionati dall’account e gli URL dei firmatari remoti mantengono i percorsi esistenti; il DNS rebinding rimane escluso dal controllo. Il client web inoltre [legge i payload sperimentali separati degli avvisi sui contenuti](https://github.com/SnowCait/nostter/pull/2680) solo dopo che il lettore preme Mostra, controllando l’ID dell’event referenziato, la corrispondenza dell’autore e un tag `k` corrispondente al kind dell’event originale. Reazioni e risposte sono indirizzate all’event originale. Queste modifiche integrate lasciano invariato il formato di pubblicazione attuale basato su [NIP-36](/it/topics/nip-36/).

### Coracle

[L’editor di liste di Coracle](https://github.com/coracle-social/coracle/pull/679) ripristina la modifica e l’eliminazione attendendo la decodifica asincrona prima di visualizzare il modulo. In precedenza, la modifica perdeva i campi della lista e né il salvataggio né l’eliminazione pubblicavano un event.

### Routstr Core

[Il codice sorgente dell’attuale versione 0.5.0 di Routstr Core](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0) [smette di registrare nei log le chiavi private Nostr generate automaticamente](https://github.com/Routstr/routstr-core/pull/812) e [conserva l’identità pubblica del primo avvio](https://github.com/Routstr/routstr-core/pull/818). [Gli annunci dei provider](https://github.com/Routstr/routstr-core/pull/823) escludono localhost e gli indirizzi HTTP letterali privati o link-local; i nomi host non vengono risolti per questo controllo. Il tag attuale include interventi integrati dopo la data di pubblicazione registrata del 7 ottobre, quindi i binari e le distribuzioni precedenti restano non verificati. I log esposti in precedenza richiedono comunque una revisione da parte degli operatori.

### Alby Hub

[La modifica di Alby Hub all’autorizzazione delle fatture](https://github.com/getAlby/hub/pull/2629) limita il regolamento e l’annullamento alle fatture create dall’app richiedente. Il wallet autogestito espone le connessioni delle app tramite [NIP-47, Nostr Wallet Connect](/it/topics/nip-47/); la possibilità di una connessione di gestire le proprie fatture non deve conferire autorità sulle fatture di un’altra app. Una [correzione separata per la privacy delle connessioni isolate](https://github.com/getAlby/hub/pull/2621) rimuove l’indirizzo Lightning del wallet principale dai percorsi di esito positivo nel browser per le connessioni isolate.

### nak

[Il comando relay integrato in nak](https://github.com/fiatjaf/nak/pull/222) verifica i tempi di connessione, lettura e scrittura e le informazioni del relay, quindi stampa event di individuazione di kind 30166 non firmati. Passando questi risultati tramite pipe a `nak event` si ottengono firma e pubblicazione, rendendo possibile il [monitoraggio programmato dei relay secondo NIP-66](/it/topics/nip-66/) con lo stesso strumento da terminale. Le risposte di autenticazione o restrizione osservate prevalgono sulle informazioni dichiarate dal relay. I test di scrittura usano un event effimero firmato con una chiave usa e getta; gli annunci dei monitor di kind 10166 restano un’operazione separata.

### Kehto

[La verifica dei manifest di Kehto](https://github.com/kehto/web/pull/277) controlla i manifest firmati attuali a singolo artefatto e i byte degli artefatti prima dell’esecuzione, mantenendo separata l’analisi del formato precedente. La shell napplet inoltre [verifica i gestori consigliati](https://github.com/kehto/web/pull/294), chiede agli utenti come gestire i conflitti con le scelte salvate e consuma un URL di invocazione accettato per impedire consegne ripetute. La verifica dei manifest controlla l’identità del pubblicatore e i byte degli artefatti; non stabilisce che il codice dell’applicazione sia sicuro. [Le istantanee del gamepad](https://github.com/kehto/web/pull/297) ora seguono il focus e la visibilità. I frame Paja/playground bloccano l’accesso nativo diretto a gamepad, HID e USB prima dell’esecuzione del codice dell’applicazione, lasciando all’host l’accesso mediato. Chi li utilizza necessita dei corrispondenti pacchetti host; la disponibilità operativa della shell è una capacità separata. Una successiva [modifica all’ammissione in Paja](https://github.com/kehto/web/pull/305) avvisa della presenza di domini obbligatori sperimentali non disponibili, ma consente il caricamento; tali domini continuano a non esporre API né concessioni di accesso.

### napplet SDK

[L’SDK napplet implementa l’invocazione basata su URI e la consegna con conservazione](https://github.com/napplet/web/pull/228). [I metadati di pubblicazione vengono conservati nell’HTML autonomo](https://github.com/napplet/web/pull/226), e [i riferimenti facoltativi alle applicazioni](https://github.com/napplet/web/pull/239) collegano i manifest a schede firmate e schermate senza modificare gli hash degli artefatti. Il formato dei riferimenti alle applicazioni resta una proposta. I test della shell di riferimento lasciano agli host l’individuazione, l’installazione e la verifica delle firme in produzione.

### rust-nostr

La libreria Rust per Nostr [rust-nostr conserva l’avanzamento parziale dei download insieme agli errori terminali dei relay](https://github.com/nostrdevkit/nostr/pull/1483). Il relay che ha riportato l’errore rimane nell’insieme di quelli non riusciti, così chi effettua la chiamata può usare gli event già ricevuti senza perdere la prova che la sincronizzazione si è interrotta prima del termine.

### Pensieve

[La correzione di sicurezza della riconciliazione di Pensieve](https://github.com/andotherstuff/pensieve/pull/92) fa seguito al [lavoro sull’esclusione degli event mancanti](https://github.com/andotherstuff/pensieve/pull/90). Gli strumenti per relay e archiviazione richiedono nuovamente gli esatti ID mancanti prima di classificare gli errori, impedendo che le porzioni finali troncate delle query diventino false esclusioni. Il conteggio delle pause è separato per ciascuna attività, e gli event già archiviati vengono gestiti separatamente. Un’attività completata può conservare registrazioni esplicite degli event mancanti; il solo completamento non dimostra che l’archivio sia completo.

[La riconciliazione continua di Premium Primal](https://github.com/andotherstuff/pensieve/pull/84) è stata abilitata il 12 ottobre. Il [registro di distribuzione](https://github.com/andotherstuff/pensieve/pull/93) dell’operatore riporta che entrambi i binari corretti sono stati distribuiti e che la sospensione basata sugli errori è stata abilitata il 13 ottobre. Il successivo [riporto delle esclusioni](https://github.com/andotherstuff/pensieve/pull/95) riutilizza soltanto le esclusioni originali comprovate per lo stesso relay e una finestra temporale sovrapposta, escludendo riporti concatenati e ID mescolati di recente; la sua [distribuzione è stata registrata quello stesso pomeriggio](https://github.com/andotherstuff/pensieve/pull/97). La [correzione dei controlli preliminari dell’archivio e degli stalli della cache](https://github.com/andotherstuff/pensieve/pull/98) è stata [distribuita il 14 ottobre](https://github.com/andotherstuff/pensieve/pull/99). Una successiva [correzione della priorità dei riporti](https://github.com/andotherstuff/pensieve/pull/103) risulta integrata, ma non ancora distribuita nella relativa registrazione alla fonte.

### njump

Il visualizzatore web per Nostr [njump ripristina le impostazioni predefinite dei relay incorporate](https://github.com/fiatjaf/njump/pull/173) quando non viene fornito un file di configurazione alternativo. Inoltre [isola i renderer Markdown concorrenti](https://github.com/fiatjaf/njump/pull/171) e [le intestazioni di risposta durante i timeout](https://github.com/fiatjaf/njump/pull/169), correggendo condizioni di competizione che potevano causare l’arresto anomalo del processo durante il rendering di event di formato lungo citati o la gestione di richieste concorrenti. Si tratta di modifiche al server già integrate; la distribuzione in produzione resta non verificata.

### Nostr Components

[La correzione di Nostr Components alla firma degli zap](https://github.com/saiy2k/nostr-components/pull/187) interrompe il flusso di pagamento quando il firmatario selezionato rifiuta. I widget social incorporabili non sostituiscono più il firmatario con un’identità anonima casuale dopo il rifiuto. La loro [aggregazione delle ricevute](https://github.com/saiy2k/nostr-components/pull/197) convalida le [ricevute zap NIP-57](/it/topics/nip-57/) prima di deduplicare le copie provenienti dai relay, le fatture e gli ID delle richieste.

### rx-nostr

Le [modifiche alla verifica nella versione quattro di rx-nostr](https://github.com/penpenpng/rx-nostr/pull/207), la libreria client reattiva, controllano in modo coerente la struttura canonica degli event, gli ID e le firme in JavaScript e WebAssembly. Un elenco vuoto di condizioni della richiesta non trova alcuna corrispondenza e termina; l’invio con il meccanismo precedente segnala un errore quando non ha destinazioni. Gli osservatori della pubblicazione non possono modificarne l’esito, e i discendenti delle richieste dismessi non possono riavviarsi. I [segmenti di query finiti](https://github.com/penpenpng/rx-nostr/pull/213) consentono alle query a ritroso di concludersi dopo che tutti i segmenti forniti sono terminati. Queste modifiche sono incluse nella [4.0.0 beta 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2), una versione preliminare con modifiche alle API che interrompono la compatibilità.

### eHagaki

Il client social [eHagaki aggiunge la consegna outbox in più fasi](https://github.com/Lokuyow/ehagaki/pull/268), fissando i relay di destinazione dell’autore prima della firma. Il suo flusso per i post sensibili invia a ciascun relay il payload prima della struttura che vi fa riferimento, usando la conferma di ricezione di quel relay; se riesce solo l’invio del payload, l’editor viene mantenuto. Una [scansione completa della cronologia dei post](https://github.com/Lokuyow/ehagaki/pull/312) salva progressivamente i risultati verificati. Gli intervalli ambigui restano non confermati anche quando la scansione viene mostrata come completata, con un controllo informativo esplicativo. Il [supporto per il relay locale Citrine](https://github.com/Lokuyow/ehagaki/pull/315) conserva gli intervalli di consultazione verificati e archivia gli esatti event firmati dopo la pubblicazione esterna riuscita. Le conferme locali non trasformano un invio esterno non riuscito in un successo, e questa funzionalità non aggiunge una coda di pubblicazione offline. La [gestione dei contenuti multimediali caricati](https://github.com/Lokuyow/ehagaki/pull/321) elenca ed elimina immagini e video caricati sui server NIP-96 e Blossom supportati. Una [successiva migrazione del database](https://github.com/Lokuyow/ehagaki/pull/325) reimposta i dati di visualizzazione memorizzati nella cache e la cronologia dei post, conservando le bozze e le richieste di eliminazione. Impedisce inoltre che risultati di sincronizzazione precedenti ancora in coda ripopolino la cronologia dopo una cancellazione.

### Formstr

[La correzione del risultato di invio di Formstr](https://github.com/formstr-hq/nostr-forms/pull/508) rifiuta una risposta a un modulo quando nessun relay la accetta. L'applicazione Nostr per i moduli mostra gli esiti dei relay e offre la possibilità di riprovare, conservando le risposte compilate. I webhook e le pagine di conferma attendono l'accettazione, e lo stesso controllo viene applicato all'SDK. Una conferma da parte di un relay resta distinta dalla garanzia di conservazione a lungo termine, ma un fallimento totale della pubblicazione non produce più un messaggio di successo.

### Auditable Voting

[Auditable Voting aggiunge il raggruppamento facoltativo delle schede tramite un worker privato](https://github.com/tidley/auditable-voting/pull/35). Le definizioni firmate dall'organizzatore selezionano l'identità del worker, i relay per i DM e una soglia o una scadenza per il rilascio. Gli elettori inviano [schede con confezionamento gift-wrap NIP-17](/it/topics/nip-17/) e autenticano le ricevute rispetto a quel worker; le deleghe devono autorizzare sia l'accodamento sia il rilascio. Le schede rilasciate usano l'identità del worker. Il worker può leggere le schede inviate, e i lotti rilasciati alla scadenza possono essere piccoli. Se non viene individuato alcun percorso privato valido, il client esaminato ripiega sull'invio pubblico. Si tratta di lavoro di sviluppo già integrato.

### MintRadar

[MintRadar aggiunge avvisi facoltativi con confezionamento gift-wrap](https://github.com/hroomnik007/MintRadar/pull/122) per problemi di mint o melt, software obsoleto e perdita del supporto per queste operazioni. La sua directory di mint Cashu [collega i controlli della lista di monitoraggio](https://github.com/hroomnik007/MintRadar/pull/123) a queste impostazioni di notifica e le conferma dopo la risposta del server. Le prenotazioni atomiche impediscono che verifiche sovrapposte inviino lo stesso avviso, e una pubblicazione sui relay non riuscita libera la prenotazione per un nuovo tentativo. I [messaggi privati NIP-17](/it/topics/nip-17/) proteggono il contenuto delle notifiche; l'accettazione da parte dei relay non conferma la lettura da parte del destinatario.

### Nostr Docs

[La migrazione di Nostr Docs al relay locale](https://github.com/formstr-hq/nostr-docs/pull/65) instrada le letture e le scritture dell'editor Markdown collaborativo attraverso un Web Worker con una cache di event in IndexedDB e una coda in uscita per i nuovi tentativi. I titoli e i tag dei documenti vengono conservati dopo i ricaricamenti, e le modifiche successive ai metadati ricevono timestamp crescenti, così che due modifiche nello stesso secondo rimangano distinte. L'archiviazione esistente delle chiavi di cifratura rimane intatta. Il meccanismo di ripiego sul pool di rete non offre la persistenza della coda in uscita del worker, e l'accettazione di una pubblicazione in coda non dimostra l'accettazione da parte dei relay.

### Pakstr

[Il firmatario locale nativo di Pakstr](https://git.nostrdev.com/stuff/pakstr/pulls/105) consente al contenitore della sua applicazione Android di creare un account Nostr sul dispositivo. La chiave rimane nel livello nativo, cifrata con una chiave di wrapping protetta da Android Keystore. I risultati della firma vengono verificati prima di essere restituiti all'applicazione web. Il contenitore supporta la [firma nel browser NIP-07](/it/topics/nip-07/) e le richieste cifrate. La selezione del firmatario si apre solo quando necessario e coordina le richieste concorrenti.

### Nostr WoT SDK

La libreria web-of-trust [Nostr WoT SDK estende il consenso all'autenticazione](https://github.com/nostr-wot/nostr-wot-sdk/pull/15) ai richiedenti nativi e remoti tipizzati. I rifiuti memorizzati vengono controllati prima di mostrare le richieste di consenso, e il consenso riutilizzabile è vincolato al trasporto e alla destinazione del richiedente. Le richieste web rimangono monouso per impostazione predefinita. I suoi [caricamenti Blossom gestiti](https://github.com/nostr-wot/nostr-wot-sdk/pull/13) convalidano byte immutabili, supportano l'annullamento e si interrompono quando cambia la sessione attiva, con autenticazione vincolata al server e restrizioni sui reindirizzamenti.

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49) fornisce programmi di installazione per desktop. Separatamente, il lavoro lato server già integrato [aggiunge la pubblicazione programmata persistente](https://github.com/flox1an/nostube/pull/126). Gli event vengono firmati prima dell'orario previsto, memorizzati in SQLite e pubblicati da un worker che recupera le pubblicazioni arretrate dopo un periodo di inattività. Il suo [flusso di modifica ed eliminazione](https://github.com/flox1an/nostube/pull/124) tiene traccia dei marcatori di eliminazione, della consegna ai mirror e della pulizia dei file di proprietà. La [configurazione al primo avvio](https://github.com/flox1an/nostube/pull/134) distingue il firmatario nel browser dell'utente da una chiave di canale gestita dal server. I blob storici privi di proprietario restano esclusi dalla pulizia automatica.

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24) aggiunge la collaborazione privata sulle clip con attribuzione dei crediti e verifiche della provenienza firmata di acquisizioni o modifiche. I sottotitoli tradotti selezionati dallo spettatore ripiegano sugli originali mentre la traduzione è in attesa o non verificata. Queste verifiche della provenienza non garantiscono che una registrazione non sia stata modificata.

Le [modifiche all'instradamento](https://github.com/divinevideo/divine-mobile/pull/9884) del client per video brevi consultano i relay della posta in arrivo dei destinatari per i messaggi di chat testuali e video e mantengono gli esiti di consegna incerti. La [gestione delle copie del mittente](https://github.com/divinevideo/divine-mobile/pull/10006) consente ai messaggi di gruppo inviati dagli utenti di apparire sugli altri loro dispositivi; per le copie precedentemente scartate è necessario reimportare l'account. Gli [invii parziali ai gruppi annullati](https://github.com/divinevideo/divine-mobile/pull/10031) conservano le registrazioni «Non inviato a tutti»; l'annullamento è definitivo e per queste registrazioni non è possibile riprovare. La creazione di gruppi e il riconoscimento di nuove stanze avviate da altri partecipanti restano [subordinati a un flag disattivato per impostazione predefinita](https://github.com/divinevideo/divine-mobile/pull/10020).

Le successive modifiche al ramo principale [mantengono fuori dalla cache temporanea le copie interrotte del ripristino del database](https://github.com/divinevideo/divine-mobile/pull/10118) e [conservano i post programmati, le segnalazioni in coda, le modifiche al profilo e le registrazioni delle chat rimosse durante la ricostruzione](https://github.com/divinevideo/divine-mobile/pull/10115). Le [scadenze di invio includono la riconnessione ai relay](https://github.com/divinevideo/divine-mobile/pull/10127), riducendo da 160 a 137 secondi la soglia per ritentare gli invii abbandonati. Le [ricerche della posta in arrivo tramite l'indicizzatore usano un pool separato con capacità limitata](https://github.com/divinevideo/divine-mobile/pull/10116) per evitare di restare in attesa dietro alle letture del feed, e i [controlli per seguire gli utenti conservano l'azione scelta](https://github.com/divinevideo/divine-mobile/pull/10147) se l'elenco dei contatti cambia prima della conferma. Queste integrazioni successive lasciano meno tempo per la conferma dei relay durante le riconnessioni lente; le riparazioni del database non possono ripristinare dati persi in precedenza. Le successive [copie facoltative delle registrazioni](https://github.com/divinevideo/divine-mobile/pull/10110) consentono al backup nella galleria di Android e iOS di conservare le clip appena registrate. Le copie prive di provenienza firmata sono accompagnate da un avviso e non possono essere reimportate; questa funzione è disattivata per impostazione predefinita e richiede spazio di archiviazione aggiuntivo.

### Conduit

Le applicazioni commerciali di [Conduit ottengono una casella di posta in arrivo condivisa e persistente](https://github.com/Conduit-BTC/conduit-mono/pull/616), mantenendo la consegna e il recupero dei messaggi cifrati tra Market e Merchant. L'accettazione da parte dei relay del destinatario rimane valida anche se fallisce la copia per il mittente, e il recupero riutilizza gli stessi byte per evitare un secondo invio semanticamente equivalente. I [wallet condivisi basati sul firmatario](https://github.com/Conduit-BTC/conduit-mono/pull/635) collegano entrambe le applicazioni. Questo percorso di recupero affida al firmatario il testo in chiaro usato per il recupero; la sola integrazione nel codice sorgente non dimostra né una distribuzione operativa né test di accettazione con fondi. Le [autorizzazioni indipendenti per i relay](https://github.com/Conduit-BTC/conduit-mono/pull/645) vengono conservate quando più percorsi dell'account condividono un URL. Disabilitare un percorso non elimina più un'altra autorizzazione firmata per l'elenco dei relay o la posta in arrivo, e le letture incomplete o che richiedono autenticazione mantengono un esito di indisponibilità. Il [router dei pagamenti integrato](https://github.com/Conduit-BTC/conduit-mono/pull/613) suddivide un unico pagamento di finanziamento approvato dall'acquirente in pagamenti Lightning al commerciante e al fornitore, seguiti dalla commissione di Conduit, con riconciliazione rispetto all'intento esatto e recupero cifrato attraverso la casella Nostr condivisa. L'esecuzione in produzione e in staging rimane disabilitata; il completamento da parte del fornitore non dimostra né la riscossione da parte del destinatario né la chiusura definitiva del pagamento.

### Bitcredit

[La cifratura dei dati persistenti di Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041) protegge le chiavi di identità, azienda e cambiale della sua applicazione per cambiali elettroniche, inclusa la coda di reinvio Nostr, usando la frase mnemonica dell'identità personale. L'inizializzazione richiede una frase mnemonica corrispondente. La [gestione delle istanze](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043) consente alle istanze testnet e mainnet di mantenere attive in modo indipendente le proprie sottoscrizioni Nostr in background su un unico dispositivo.

## Nuovi progetti

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0) introduce un gestore di password i cui archivi cifrati si sincronizzano tramite Nostr. Supporta firmatari esterni e conserva versioni concorrenti degli elementi, con importazione ed esportazione in formato JSON di Bitwarden. Le modifiche vengono salvate localmente prima di attendere l'accettazione da parte dei relay. La versione è accompagnata da download per Android, desktop e CLI. Il progetto si definisce giovane e consiglia un gestore collaudato per le password critiche; la specifica del protocollo associata alla versione è ancora vuota. La sua [archiviazione web](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md) conserva la chiave di cifratura insieme ai dati protetti.

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md) aggiunge un'implementazione in Common Lisp delle chat di gruppo MLS su Nostr. Il codice del 9 ottobre aggiunge la convergenza dei commit concorrenti e allegati Blossom cifrati, con test di interoperabilità con il client a riga di comando wn di MDK dichiarati dall'autore. L'implementazione non è stata sottoposta ad audit e le chiavi degli account e i registri dei messaggi non sono cifrati a riposo. Le finestre temporizzate di convergenza, il replay oltre l'orizzonte di rollback e lo scioglimento dei gruppi restano da implementare; il sistema di test esaminato usa relay locali usa e getta.

### nalgorithm Android

[La versione Android di nalgorithm](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0) crea un feed Nostr ordinato in base alle preferenze e un riepilogo audio in background riproducibile offline. Gli utenti scelgono tra inferenza ospitata, con prezzi in Lightning, e inferenza con chiave propria richiesta dal telefono; si tratta di due percorsi distinti. L'accesso supporta Amber tramite firma remota. Le versioni successive [correggono l'ordinamento con chiave propria e l'individuazione dell'elenco dei profili seguiti](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1), poi [conservano i «mi piace» provenienti dai relay funzionanti quando un altro relay non risponde](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2) e migliorano il recupero del riepilogo. [La versione 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3) riordina la configurazione del modello e segnala i dati mancanti per il test di connessione.

## Lavori sul protocollo e sulle specifiche

### Endpoint autenticati per napplet

Nelle specifiche NAP per le applicazioni napplet, gli [identificatori degli endpoint NAP-INC](https://github.com/napplet/naps/pull/104), integrati il 9 ottobre, sostituiscono i semplici nomi dei gestori con identificatori autenticati. Nomi uguali provenienti da editori diversi non identificano più lo stesso peer. Il runtime continua a mediare la comunicazione e i manifest radice o snapshot non richiedono una coordinata `d` con un nome.

### Raccomandazioni di gestori nei link di invocazione

[La raccomandazione nei link di invocazione](https://github.com/napplet/naps/pull/99), anch'essa integrata il 9 ottobre, consente una raccomandazione facoltativa di un gestore tramite `#naddr`. Una shell può offrire individuazione e installazione, ricorrendo alla risoluzione ordinaria come alternativa. Le preferenze salvate e le regole della shell hanno la precedenza. Un gestore raccomandato fornisce quindi un suggerimento per l'individuazione, senza sostituire la scelta esistente dell'utente né trasferire al mittente del link l'autorità di installazione.

### Accettazione della consegna ed elaborazione dell'applicazione

[Le modifiche alla pubblicizzazione degli intenti e alla consegna](https://github.com/napplet/naps/pull/91) ricavano ruoli e intenti dallo stesso manifest verificato, usando identificatori sicuri per gli editori. L'accettazione della consegna non dipende più dal fatto che l'applicazione di origine rimanga attiva. Una risposta `ok: true` accetta la responsabilità della consegna; non significa che l'elaborazione dell'applicazione di destinazione sia terminata. Con questa modifica integrata alla specifica, il comportamento dei tentativi successivi e dei riavvii resta disciplinato dalle regole del runtime.

### Catene di azioni di Cyberspace

[Le regole riviste per le catene di Cyberspace](https://github.com/arkin0x/cyberspace/pull/48) fanno sì che una biforcazione invalidi una catena di azioni firmata a partire dal suo punto di spawn e richiedono ai client di confermare la testa corrente prima di firmare un'altra azione. Il mondo basato su Nostr aggiunge [140 catene sintetiche firmate](https://github.com/arkin0x/cyberspace/pull/49) con verdetti normativi per le implementazioni. Le [regole di attribuzione delle copie](https://github.com/arkin0x/cyberspace/pull/47) usano riferimenti `q` all'oggetto originale e ne avvisano l'autore per i remix pubblici; le copie sigillate omettono tale notifica. Si tratta di specifiche di progetto integrate, mentre la copertura dei verificatori in uso non è stata verificata.

### Conferme di persistenza dei relay

[La proposta aperta sulla persistenza](https://github.com/nostr-protocol/nips/pull/2496) introduce conferme di avvenuta persistenza, query PROOF e attestazioni facoltative firmate dei relay di kind 1797. Una firma rende attribuibile a un relay una dichiarazione di archiviazione; non dimostra che la conservazione continui nel tempo. Le query rivelano inoltre quali event interessano al client.

### Messaggi fissati condivisi per i gruppi Marmot

[La proposta aperta di Marmot per fissare messaggi](https://github.com/marmot-protocol/marmot/pull/434) definisce uno stato condiviso autenticato per un massimo di 64 riferimenti a messaggi, con permessi per membri e amministratori. Le modifiche effettive richiedono un MLS Commit e una transizione di epoca, e ogni foglia membro risultante deve supportare la funzionalità. Fissare messaggi non ne copia il corpo né ne prolunga la conservazione, quindi i riferimenti a messaggi non disponibili restano irrisolti. I dati di test forniti presuppongono uno stato autenticato; non dimostrano l'elaborazione crittografica né la convergenza tra client.

## Approfondimento sui NIP: NIP-36 e NIP-38

### Avvisi sui contenuti prima della visualizzazione

[NIP-36, contenuti sensibili](/it/topics/nip-36/), consente agli autori di aggiungere un tag `content-warning` a un event, includendo facoltativamente una motivazione. Un client può nascondere il contenuto finché il lettore non sceglie di mostrarlo. La [specifica](https://github.com/nostr-protocol/nips/blob/master/36.md) lascia ai client la scelta dell'interfaccia e consente tag supplementari di etichettatura. L'aggiunta di un avviso non cambia chi può leggere l'event. In un post pubblico, i relay e gli altri client continuano a riceverne il contenuto.

[Il parser dei tag di avviso di Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) riconosce il tag e considera non specificata una motivazione assente o vuota. [L'editor di composizione di Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte) scrive la motivazione nel tag; la sua [vista dei contenuti](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) rispetta l'impostazione del lettore sui contenuti sensibili e offre un'azione per mostrarli. [La vista delle note di noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) applica la propria preferenza sugli avvisi e lo stato di espansione prima di mostrare l'interfaccia di avviso.

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md) non cifra gli event né impone di nasconderli. L'assenza di un avviso non dice nulla sul contenuto; sono i client a decidere come gli avvisi influiscono sulle anteprime e sui controlli per mostrare il contenuto.

### Stato del profilo e scadenza

[NIP-38, stati degli utenti](/it/topics/nip-38/), usa event indirizzabili di kind 30315. L'autore, il kind e il tag `d` identificano una coordinata di stato; `general` e `music` hanno significati definiti. Un event più recente sostituisce lo stato precedente a quella coordinata, mentre un valore `d` diverso rimane separato. Un contenuto vuoto cancella uno stato. La [specifica](https://github.com/nostr-protocol/nips/blob/master/38.md) consente anche riferimenti a URL, profili, event e indirizzi.

Questo event [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) firmato mostra uno stato generale scaduto. L'ortografia originale dell'autore è conservata.

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[Il modello degli stati di Damus](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift) gestisce stati generali e musicali con scadenza. [Il servizio degli stati di Nostria](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts) ignora i valori vuoti o scaduti e pubblica stati musicali usando la durata del brano; le sue normali sottoscrizioni richiedono soltanto i tipi generale e musicale. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt) conserva l’identificatore `d` quando cancella uno stato. I tipi personalizzati richiedono quindi un accordo che vada oltre la struttura condivisa del formato di trasmissione.

Gli stati sono dichiarazioni pubbliche degli autori. Non dimostrano la presenza online né che qualcuno abbia ascoltato un brano. Pubblicare informazioni sulla musica o sulla disponibilità può rivelare abitudini, e la scadenza facoltativa limita la visualizzazione di informazioni non più attuali senza garantirne l’eliminazione. [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) rimane una specifica facoltativa in fase di bozza, così come NIP-36. I client possono implementare l’una o l’altra indipendentemente, e le loro impostazioni di visualizzazione determinano ciò che vedono i lettori.
