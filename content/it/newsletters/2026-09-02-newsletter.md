---
title: "Nostr Compass #38"
date: 2026-09-02
publishDate: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
description: "Voca 1.0 porta la lettura verificata di Nostr in un’app text-to-speech offline, nostream amplia l’instradamento dei job e l’autenticazione lato relay, Napstr pubblica cataloghi audio basati su Tor, MDK 0.9.17 riduce il costo della manutenzione dei gruppi, i NIP principali integrano un suggerimento di paginazione e tag per gli highlight insieme ai totali delle transazioni NWC, e l’approfondimento NIP spiega repost e reazioni."
---
Bentornati su [Nostr Compass](https://nostrcompass.org), la vostra guida settimanale a Nostr.

**Questa settimana:** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 porta note Nostr verificate e subscription long-form in un lettore Android offline che legge gli articoli ad alta voce, [nostream](https://github.com/cameri/nostream) amplia l'instradamento dei job lato relay e il funzionamento autenticato, [NDK for Dart](https://github.com/relaystr/ndk) corregge negentropy e la durata delle richieste multi-relay, [Divine Mobile](https://github.com/divinevideo/divine-mobile) rende deterministiche l'eliminazione e la firma dei messaggi incapsulati, [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) protegge per impostazione predefinita le inbox dei gift wrap, [Amethyst](https://github.com/vitorpamplona/amethyst) distribuisce highlight portabili e [Mostro](https://github.com/MostroP2P/mostro) verifica gli ordini firmati prima del proprio filtro antispam. [Napstr](https://github.com/lnbits/napstr) pubblica cataloghi audio e heartbeat dei seeder su Nostr, trasferendo i file tramite Tor. Le release riguardano [MDK](https://github.com/marmot-protocol/mdk) e [pakstr](https://git.nostrdev.com/stuff/pakstr); il lavoro sul protocollo integra un suggerimento di paginazione [NIP-67](/it/topics/nip-67/) e uno schema di tag per gli highlight [NIP-84](/it/topics/nip-84/) nel [repository dei NIP](https://github.com/nostr-protocol/nips), mentre [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) aggiunge i totali delle transazioni; e l'approfondimento NIP segue repost e reazioni nelle loro forme di event e nelle implementazioni attuali.
## Storie principali

### Voca 1.0 legge ad alta voce note e subscription Nostr verificate su Android

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) è un lettore Android offline che legge articoli, PDF, file Markdown e note Nostr con la voce text-to-speech del telefono, mentre la frase pronunciata resta evidenziata sulla pagina. La sua [release 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en), [pubblicata il 2026-08-27](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) con la propria [chiave di progetto](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu), rende Nostr una fonte di prima classe: incollando l'indirizzo di una nota, l'identificatore di un event, un npub, un profilo o un normale link web contenente un'entità Nostr, l'app decodifica il riferimento, recupera l'event firmato dai relay e legge il testo dell'autore invece della pagina web costruita attorno ad esso.

Due comportamenti verificati definiscono l'integrazione Nostr, entrambi descritti nell'[annuncio firmato di Voca 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en). Primo, ogni event recuperato viene controllato rispetto al suo id ricalcolato e alla firma Schnorr BIP-340 prima di essere persistito, usando i relay di bootstrap, la lista relay [NIP-65](/it/topics/nip-65/) dell'autore (un event kind `10002` firmato e sostituibile in cui un autore elenca i relay da cui legge e su cui scrive) e i suggerimenti contenuti nel riferimento stesso, così un relay può rifiutarsi di rispondere ma non può attribuire parole all'autore. Secondo, aggiungere l'npub di un autore inserisce i suoi articoli long-form [NIP-23](/it/topics/nip-23/) (post indirizzabili kind `30023` con titoli, riassunti e immagini) in un'unica inbox sul dispositivo accanto ai feed RSS e Atom. L'aggiornamento 1.1.0, [annunciato il 2026-08-28](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca) e pubblicato su [Zapstore](https://zapstore.dev) il 2026-08-29, sincronizza lo scorrimento a livello di frase, rende più fluidi i documenti lunghi e ripristina il widget della schermata iniziale dopo scorrimento manuale, ridimensionamento, riavvii del processo e aggiornamenti.


### nostream amplia l’instradamento DVM lato relay e il funzionamento autenticato

Dopo il [lavoro del 19 agosto sull'acquisizione dei job](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes), [nostream](https://github.com/cameri/nostream), un'implementazione relay in TypeScript, [memorizza e serve event di gestori di applicazioni NIP-89](https://github.com/cameri/nostream/pull/737). [NIP-89](/it/topics/nip-89/) (scoperta dei gestori di applicazioni) usa raccomandazioni kind `31989` e informazioni sui gestori kind `31990`, entrambe già nell'intervallo sostituibile parametrizzato, così un client può interrogare quei kind e ricevere una sostituzione quando collide un tag `d`. Il relay non pubblica informazioni sui gestori per i propri worker.

I job [NIP-90](/it/topics/nip-90/) (data vending machine) in attesa ora [raggiungono un processo worker e tornano come event di risultato](https://github.com/cameri/nostream/pull/734). In caso di successo il relay firma un risultato kind 6000-6999 con la propria chiave. Un timeout o un arresto anomalo del worker contrassegna il job come fallito invece di lasciarlo inviato.

Le sessioni autenticate e le chiamate HTTP amministrative si trovano su confini differenti. [NIP-42](/it/topics/nip-42/) (autenticazione dei client ai relay) [tiene traccia della pubkey autenticata per ogni socket](https://github.com/cameri/nostream/pull/716), può richiedere AUTH prima che i client pubblichino event e pubblicizza tale requisito nel documento [NIP-11](/it/topics/nip-11/) (informazioni sul relay), con entrambi i controlli disattivati per impostazione predefinita. Separatamente, [le route API amministrative possono accettare autorizzazione HTTP firmata NIP-98](https://github.com/cameri/nostream/pull/730). [NIP-98](/it/topics/nip-98/) (autenticazione HTTP con event firmati) resta disattivato finché un operatore non lo abilita e indica le pubkey consentite.

### NDK for Dart corregge negentropy, la durata delle richieste multi-relay e la verifica delle firme

Un'esecuzione [NIP-77](/it/topics/nip-77/) (riconciliazione di insiemi con negentropy) in [NDK](https://github.com/relaystr/ndk), un kit di sviluppo Dart per Nostr, restituiva insiemi have e need errati senza segnalare errori, perché il codec non parlava il protocollo [negentropy](/it/topics/negentropy/) v1. La [correzione della codifica v1](https://github.com/relaystr/ndk/pull/722) ora restituisce gli id posseduti dal relay e quelli di cui ha ancora bisogno.

Filtri identici inviati a relay diversi [venivano accorpati in un'unica richiesta](https://github.com/relaystr/ndk/pull/705). Le richieste con lo stesso filtro ora restano distinte quando puntano a relay diversi o hanno durate differenti, così una query breve non può mescolare nel risultato event di un altro relay né lasciare bloccata una subscription attiva.

Lo stesso kit [verifica una firma una sola volta e conserva il risultato](https://github.com/relaystr/ndk/pull/726). Una consegna duplicata successiva non richiede più un altro controllo né sovrascrive l’event verificato memorizzato.

### Divine Mobile rende deterministiche l’eliminazione e la firma dei messaggi diretti incapsulati

Gli event kind `5` incapsulati [NIP-09](/it/topics/nip-09/) (richiesta di eliminazione di event) che prendevano di mira un messaggio non venivano mai applicati in [Divine Mobile](https://github.com/divinevideo/divine-mobile), un client mobile per video brevi che pubblica tramite Nostr. Il client [ora risolve ogni eliminazione rispetto al messaggio indicato](https://github.com/divinevideo/divine-mobile/pull/8174), invece di trattare come già elaborato tutto ciò che non è una reazione. Una seconda [richiesta di eliminazione per tutti mentre la prima era ancora in corso](https://github.com/divinevideo/divine-mobile/pull/8164) prima scompariva senza errori e senza alcun kind `5` in rete; ora ogni eliminazione concorrente viene pubblicata.

Dopo la release 1.0.22 già trattata, inviare due volte nello stesso secondo lo stesso testo 1:1 [NIP-17](/it/topics/nip-17/) (DM privati in gift wrap) [generava un solo rumor id](https://github.com/divinevideo/divine-mobile/pull/8163), quindi il secondo invio scompariva; ora ogni invio porta un token all'interno del rumor [NIP-59](/it/topics/nip-59/) (gift wrap), così gli id differiscono.

Un chiamante che aveva già firmato un event kind `4` o kind `5` [manteneva quella firma](https://github.com/divinevideo/divine-mobile/pull/8173), invece di ricevere in seguito un tag client che modificava l’id e induceva i relay a rifiutare l’event come non valido.

### Conduit Relay irrobustisce la propria inbox protetta NIP-42

I gift wrap kind `1059` vengono memorizzati per un solo destinatario. [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), un relay Go che conserva tali wrap in un'inbox protetta per destinatario, [usa per impostazione predefinita la modalità enforce](https://github.com/Conduit-BTC/conduit-relay/pull/8): una query kind `1059` deve presentare autenticazione [NIP-42](/it/topics/nip-42/) come quel destinatario, altrimenti il relay respinge la richiesta. Filtri con kind misti, wildcard, conteggi e [negentropy](/it/topics/negentropy/) su tali wrap sono `restricted`, così un'altra AUTH non può trasformarli in un dump dell'inbox altrui.

Lo stesso [merge dell'inbox protetta](https://github.com/Conduit-BTC/conduit-relay/pull/8) richiede un event id canonico sull'event AUTH trasmesso e accetta un event NIP-42 altrimenti valido indipendentemente dal fatto che `content` sia vuoto. Challenge-only offre ancora AUTH senza bloccare la lettura; disabled consente l'accesso libero. L'impostazione predefinita della libreria è enforce.

### Amethyst distribuisce highlight NIP-84 e corregge due percorsi di errore rivolti ai relay

Dopo il [lavoro della scorsa settimana sull'autorizzazione Blossom](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads), [Amethyst](https://github.com/vitorpamplona/amethyst), un client Nostr per Android, distribuisce [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) con [NIP-84](/it/topics/nip-84/) (highlight portabili). Un passaggio selezionato diventa un event kind `9802` dal compositore, da un feed di highlight o tramite condivisione nell'app.

La release aggiunge controlli di eliminazione e archiviazione dei canali [NIP-29](/it/topics/nip-29/) ([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)) e misura il comportamento dei relay tramite il traffico già generato dal client, quindi estende tali sonde [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) con controlli di streaming, lettura, scrittura e URL ([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). Amethyst elimina inoltre una vulnerabilità di collisione hash in SharedKeyCache e confronta i codici di autenticazione dei messaggi in tempo costante ([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), corregge una race che poteva perdere la consegna AUTH in fase di connessione ([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), suddivide il locking dello stato delle subscription per terminare un convoglio ANR ([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)) e confronta tutti i filtri della subscription invece del solo primo ([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)).

[La newsletter #36 aveva già trattato queste modifiche ad autenticazione relay, backup e chat pubbliche](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow); ora v1.14.0 le ha distribuite insieme. I soft ban di Concord colmano lacune di autorità rilevate da un audit ([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). L'autenticazione relay dispone di un flusso di autorizzazioni riprogettato ([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), attende la risoluzione della challenge invece di andare in timeout ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), fa sì che i nuovi account si autentichino per impostazione predefinita ([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), rispetta tale preferenza sui relay esterni all'insieme normale dell'account ([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)) e conserva le autorizzazioni di sessione tra le riconnessioni ([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). Un flusso guidato per il primo avvio e le Impostazioni rende individuabili i backup delle chiavi ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)), il backfill delle proof Cashu e la paginazione della cronologia impediscono che i saldi wallet vengano troncati ([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)) e ora le chat pubbliche possono essere silenziate ([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)).

Dopo quel tag, le [liste fidate](https://github.com/vitorpamplona/amethyst/pull/3983) nei kind da `30392` a `30395` sono indicizzate da [NIP-50](/it/topics/nip-50/) (ricerca full-text) solo per titolo, così una lista nominata nella prosa può essere trovata senza indicizzare gli id esadecimali dei membri. I rifiuti del wallet arrivati tramite [NIP-47](/it/topics/nip-47/) (Nostr Wallet Connect) [ora mostrano l'errore invece di sembrare un tocco senza effetto](https://github.com/vitorpamplona/amethyst/pull/3987), inclusi `QUOTA_EXCEEDED` e `RESTRICTED`, oltre a un timeout quando il wallet non risponde mai.

### Mostro convalida gli ordini firmati prima del lavoro costoso e conserva gli event di audit degli ordini

Dopo le [fondamenta dell'escrow Cashu di v0.18.1](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon), [Mostro](https://github.com/MostroP2P/mostro), un daemon di scambio peer-to-peer che coordina ordini su Nostr, ha creato il tag [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5), che usa per impostazione predefinita [NIP-44](/it/topics/nip-44/) (cifratura del payload) per il trasporto e mantiene il gift wrap come opt-in esplicito.

La release ancora i timeout dello stato di attesa all'ora di presa registrata, così il bond del maker non viene penalizzato secondo l'orologio sbagliato ([PR #879](https://github.com/MostroP2P/mostro/pull/879)), invia al massimo una volta il pagamento all'acquirente per ogni ordine regolato ([PR #881](https://github.com/MostroP2P/mostro/pull/881)) e sposta tali pagamenti attraverso attese `send_payment` limitate e non bloccanti ([PR #883](https://github.com/MostroP2P/mostro/pull/883)). Un tentativo di pagare il vincitore della penalità per timeout ([PR #875](https://github.com/MostroP2P/mostro/pull/875)) è stato annullato prima della distribuzione dello stesso tag ([PR #885](https://github.com/MostroP2P/mostro/pull/885)). Mostro smette inoltre di ripubblicare ogni ora e all'avvio un order book in attesa invariato ([PR #888](https://github.com/MostroP2P/mostro/pull/888)), e i suoi event di disputa kind `38386` ora portano un tag `created_at` per l'ordinamento downstream ([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

Dopo quel tag, [un controllo della firma ora viene eseguito prima del filtro antispam](https://github.com/MostroP2P/mostro/pull/892). Un event id non incorpora `sig`, quindi una copia del kind `14` di una vittima con firma non valida poteva occupare lo slot di replay e scartare silenziosamente il messaggio valido; il daemon verifica prima e scarta un wrap non valido invece di avvertire e proseguire.

Gli event di audit delle commissioni kind `8383` portavano un timestamp di scadenza [NIP-40](/it/topics/nip-40/) di 15 giorni. Ora [mantengono una scadenza di un anno](https://github.com/MostroP2P/mostro/pull/924), coerente con il loro ruolo di registro pubblico dei pagamenti. Su un nodo con Cashu abilitato, prendere un ordine [chiede al venditore tramite Nostr di bloccare un escrow 2-su-3](https://github.com/MostroP2P/mostro/pull/830), pubblica l'event dell'ordine in attesa e salta la creazione di una hold invoice Lightning. Questo completa il percorso della richiesta; da solo non risolve ogni caso di escrow o abuso del mercato.

### Napstr pubblica cataloghi audio su Nostr e trasferisce file tramite Tor

[Napstr](https://github.com/lnbits/napstr) è un client desktop per la condivisione audio che pubblica cataloghi ricercabili e seeder attivi su Nostr, quindi trasferisce i file tramite un processo Tor integrato senza fallback sull'IP diretto. [La versione 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) mantiene pubblici profili e metadati del catalogo, e tiene richieste, credenziali di trasferimento, contenuti dei file e indirizzi IP dei peer fuori dai relay.

La scoperta usa due kind di event indirizzabili nel [repository Napstr](https://github.com/lnbits/napstr). Le voci di catalogo kind `30421` identificano un file tramite digest SHA-256, basename pubblico, dimensione e formato audio, e un autore ritira un file sostituendo quella coordinata con un marcatore di eliminazione. Gli heartbeat di disponibilità kind `30422` scadono dopo dieci minuti ed elencano gli id dei file che l'autore è pronto a distribuire, così una riga di catalogo è attiva solo finché un heartbeat non scaduto contiene ancora quel digest.

La conversazione pubblica usa [NIP-C7](/it/topics/nip-c7/) (messaggi chat kind 9) invece di un gruppo posseduto da un relay. Il [repository Napstr](https://github.com/lnbits/napstr) definisce una stanza pubblica condivisa e una discussione per traccia associata al digest del file. Quei messaggi sono firmati e pubblici. Non contengono indirizzi onion, credenziali di trasferimento o byte dei file.

Un download inizia come negoziazione [NIP-17](/it/topics/nip-17/) (DM privati in gift wrap). Il [repository Napstr](https://github.com/lnbits/napstr) incapsula una richiesta, un'offerta o un rifiuto in un rumor kind `14`, così i relay non vedono l'hostname onion v3 temporaneo né la capability monouso restituita da un'offerta accettata. Tor integrato trasferisce quindi i byte attraverso quell'onion, verifica l'intero digest SHA-256 e convalida nuovamente l'audio prima che il file diventi riproducibile.

Il [confronto tra v0.1.7 e v0.2.0](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) aggiunge raccolte di audiolibri e Napstrfy, un companion Android opzionale. I manifest kind `30423` elencano capitoli ordinati che restano normali file di catalogo, così un client che ignora la raccolta può comunque recuperare ogni capitolo. Napstr crea a tale scopo una cartella locale Audiobooks non distruttiva. Napstrfy si abbina a un desktop in esecuzione con un QR code monouso, quindi cerca e richiede download tramite i servizi Nostr e Tor già presenti sul desktop senza ricevere la chiave segreta del desktop.

Lo stesso [confronto](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) applica un timeout a un handshake del companion che non si completa. Un seeder copia e calcola l'hash del file condiviso prima di servire i byte, scrive i dati in arrivo in un file temporaneo privato, limita le destinazioni degli audiolibri a un vero figlio della cartella Napstr e interrompe il trasferimento se la destinazione cambia durante l'operazione.

## Release

### MDK v0.9.17: KeyPackage più recenti, attività dei membri e invii durevoli

[La newsletter #37 ha trattato MDK 0.9.14 e 0.9.15](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles), incluso il passaggio nel [repository MDK](https://github.com/marmot-protocol/mdk) dalla selezione della KeyPackage più vecchia alla più recente e valida del profilo corrente, i gate di recupero dai gap di epoch, la pulizia degli account e la separazione tra relay di scoperta e operativi. Tali correzioni restano la base delle due release successive, così un package obsoleto non blocca più un membro che ne ha già pubblicato uno utilizzabile.

[Gli event di membership e amministrazione ora fanno avanzare la lista chat](https://github.com/marmot-protocol/mdk/pull/1551) come un nuovo messaggio: testo di anteprima, ordinamento, conteggi dei non letti e marcatori di lettura si aggiornano quando le persone entrano, escono o cambiano ruolo, e l'attore di sistema locale non viene trattato come profilo Nostr. Riconnessioni e riavvii [riutilizzano un'unica identità di invio per un testo outbound durevole ritentato](https://github.com/marmot-protocol/mdk/pull/1516), così lo stesso messaggio di gruppo non viene pubblicato due volte.

Le due release successive si concentrano sul costo di mantenimento dei gruppi numerosi. [La versione 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [misura la divergenza di epoch rispetto all'epoch corrente invece che a un massimo storico](https://github.com/marmot-protocol/mdk/pull/1559), mantiene recuperabili gli event inbound rifiutati ([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), limita il rollback del replay allo stato canonico del gruppo ([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)) e introduce [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545), un'ABI C generata tramite macro sopra i binding UniFFI che consente agli host di incorporare direttamente il motore. [La versione 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) combina poi le scansioni di ammissione dei pass in [un solo attraversamento dei membri invece di uno per membro](https://github.com/marmot-protocol/mdk/pull/1617), [verifica se lo stato di un gruppo è contestato senza inizializzare l'intero grafo storico](https://github.com/marmot-protocol/mdk/pull/1620), [riduce il costo di polling inattivo della scansione deferred-peel](https://github.com/marmot-protocol/mdk/pull/1621) e [applica la lettura in batch dei componenti ai tre siti di proiezione mancati dal primo passaggio](https://github.com/marmot-protocol/mdk/pull/1622). Gli artefatti corrispondenti [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) e [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) sono costruiti dallo stesso commit, così chi li incorpora riceve insieme i percorsi di manutenzione più economici.


### pakstr v0.16.0: identificatori kind-32267 durante la pubblicazione

Dopo la [pipeline di pubblicazione Zapstore dalla 0.13.0 alla 0.15.0 della scorsa settimana](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit), [pakstr](https://git.nostrdev.com/stuff/pakstr), una CLI che impacchetta un'app web in un APK Android firmato e la pubblica con una chiave Nostr, [registra gli ID degli event applicazione kind `32267`](https://git.nostrdev.com/stuff/pakstr/pulls/67) che cerca, pubblica o sostituisce. [La versione 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) stampa sia l'ID precedente sia quello nuovo quando metadati obsoleti dell'inserzione provocano una nuova pubblicazione, così un publisher può confermare quale event dell'inserzione sia attivo sul relay.

Lo stesso [log degli identificatori](https://git.nostrdev.com/stuff/pakstr/pulls/67) registra l'ID trovato durante la ricerca prima di qualsiasi sostituzione, poi l'ID dell'event pubblicato, così un riuso senza modifiche appare come ID ripetuto. Questa è la modifica inclusa nel tag [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0); i comportamenti Content-Digest, pubblicazione prima dell'upload e convalida del publisher erano già stati distribuiti nei tag precedenti.

## Modifiche non ancora rilasciate

### Zap Cooking limita i relay del bunker e firma gli endpoint a pagamento

Ricaricare una sessione bunker su [Zap Cooking](https://github.com/zapcooking/frontend), un sito di ricette basato su event long-form Nostr, prima pubblicava la conversazione cifrata [NIP-46](/it/topics/nip-46/) (firma remota tramite relay) su ogni relay già usato dalla pagina. [Limitare il traffico del signer ai relay propri del bunker](https://github.com/zapcooking/frontend/pull/633) ora applica tale restrizione al ripristino della sessione e all'abbinamento nostrconnect, il flusso di connessione avviato dal signer, in linea con il percorso di login tramite URL bunker. Si rifiuta di installare un insieme di relay vuoto da un record memorizzato non valido, così i relay che ospitano solo ricette non apprendono più che la stessa pubkey mantiene una sessione bunker attiva.

L'[autenticazione HTTP firmata](https://github.com/zapcooking/frontend/pull/630) ora protegge la chat a pagamento dell'assistente di cucina, l'introduzione al ricettario e gli aggiornamenti delle ricette con accesso limitato tramite [NIP-98](/it/topics/nip-98/) (autenticazione HTTP con un event Nostr firmato). Il server legge una sola volta il corpo della richiesta, verifica la firma rispetto a quel payload esatto e ricava l'identità dall'event di autenticazione verificato invece che da una chiave pubblica fornita nel corpo. L'anteprima della chat continua a funzionare senza header, mentre una firma presente ma non valida viene respinta e l'introduzione al ricettario richiede sempre una firma. Anche l'aggiornamento di una ricetta con accesso limitato ora richiede che la chiave verificata corrisponda all'autore memorizzato; a chiunque altro viene detto che la ricetta non esiste, così l'endpoint non conferma quali record a pagamento esistano.

### nostrord corregge i DM incapsulati e i link agli event condivisi

Dopo la [v2.9.0 della scorsa settimana](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media), [nostrord](https://github.com/nostrord/nostrord), un client multipiattaforma per community ospitate su relay, ha integrato correzioni alla consegna affinché un [NIP-17](/it/topics/nip-17/) (DM privato in gift wrap) inviato da un dispositivo raggiunga lo stesso account altrove. [Pubblicare indipendentemente la copia del mittente](https://github.com/nostrord/nostrord/pull/295) impedisce che la prima accettazione del wrap del destinatario da parte di un relay faccia perdere la copia recuperata dagli altri dispositivi. La stessa modifica reinvia un wrap dopo il completamento di [NIP-42](/it/topics/nip-42/) (autenticazione dei client ai relay) e contrassegna l'invio come riuscito alla prima accettazione di un relay, così un host guasto non può bloccare gli altri. [Il nuovo tentativo dei gift wrap parcheggiati](https://github.com/nostrord/nostrord/pull/297) che non hanno superato la decifrazione [NIP-59](/it/topics/nip-59/) (gift wrap) avviene ora tramite timer, così un bunker che resta connesso non lascia più quei messaggi mi... [troncato]

Una risposta [NIP-C7](/it/topics/nip-c7/) (messaggi chat kind `9`) ripete il proprio genitore come puntatore [NIP-19](/it/topics/nip-19/) (entità codificate bech32) `nevent` iniziale accanto al tag `q`. [Eliminare quel puntatore iniziale al genitore](https://github.com/nostrord/nostrord/pull/292) quando apre il corpo e indica il genitore della risposta permette alla riga di essere visualizzata come un'unica citazione di risposta, mentre un puntatore nel mezzo del corpo o che costituisce l'intero corpo continua a essere visualizzato come scheda di citazione. [I link agli event citati ora codificano `nevent`](https://github.com/nostrord/nostrord/pull/293) con autore, kind e relay da cui è stata letta la citazione, così un event [NIP-29](/it/topics/nip-29/) (gruppi gestiti da relay) condiviso in un DM può essere recuperato da un altro client invece di usare un identificatore di nota privo di suggerimenti per la ricerca.

## Aggiornamenti ai NIP e lavoro sulle specifiche del protocollo

### Possibilità di implementazione di Nostr

Questa settimana sono stati integrati due aggiornamenti delle specifiche nel [repository principale dei NIP](https://github.com/nostr-protocol/nips).

[NIP-67](/it/topics/nip-67/) definisce i suggerimenti che un relay può aggiungere a un messaggio `EOSE` (fine degli event memorizzati), così un client sa se continuare la paginazione. Il [suggerimento `"auth"` integrato](https://github.com/nostr-protocol/nips/pull/2371) aggiunge un terzo valore accanto a `finish` e `more`: ora un relay può segnalare che altri event memorizzati potrebbero diventare visibili se l'utente si autentica e deve inviare la challenge `AUTH` [NIP-42](/it/topics/nip-42/) (autenticazione relay) prima dell'`EOSE` che porta il suggerimento. La [corrispondente aggiunta a NIP-42](https://github.com/nostr-protocol/nips/pull/2371) definisce lo stesso flusso dal lato client, così un client che riceve un `EOSE` con `auth` possiede già la challenge a cui deve rispondere.

[NIP-84](/it/topics/nip-84/) (highlight portabili, gli event kind `9802` per cui Amethyst ha distribuito il supporto sopra) [ha integrato un aggiornamento dello schema dei tag](https://github.com/nostr-protocol/nips/pull/2454): ora gli highlight possono contrassegnare la fonte con tag `i` strutturati secondo [NIP-73](/it/topics/nip-73/) (identificatori di contenuto esterno), oltre ai tag `a`/`e` per gli event Nostr e ai tag `r` per tutto il resto, e per gli highlight di citazioni il rendering come quote repost è passato da MUST a SHOULD.

### Nostr Wallet Connect

Una risposta `list_transactions` può indicare quante transazioni corrispondono alla richiesta, non quante righe ha restituito la pagina corrente. Il [`total_count` opzionale integrato](https://github.com/nostr-wallet-connect/nwc/pull/4) in NWC-05 (l'estensione per la cronologia del wallet) nel [repository delle estensioni NWC](https://github.com/nostr-wallet-connect/nwc) aggiunge tale campo alla risposta usata con [NIP-47](/it/topics/nip-47/) (controllo remoto cifrato del wallet tramite Nostr).

Il [commit che aggiunge `total_count`](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) lo documenta come intero opzionale: il numero totale di transazioni che corrispondono ai filtri della richiesta.

Il [commit che esclude la paginazione dal conteggio](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) afferma che questo totale esclude la paginazione, quindi conta tutte le transazioni corrispondenti in ogni pagina.

## Approfondimento NIP: Repost e reazioni

Un contatto può riproporre una nota esistente ai propri follower e può aggiungere un like, dislike o emoji compatto senza scrivere una risposta. [NIP-18](/it/topics/nip-18/) (repost) pubblica tale ridistribuzione come event firmato autonomo. [NIP-25](/it/topics/nip-25/) (reazioni) pubblica la risposta compatta come event firmato separato. Entrambi restano file `draft` `optional` nella [specifica canonica dei repost](https://github.com/nostr-protocol/nips/blob/master/18.md) e nella [specifica canonica delle reazioni](https://github.com/nostr-protocol/nips/blob/master/25.md): sono presenti nel repository dei NIP e implementati dai client, ma ancora etichettati come non definitivi.

### Repost (NIP-18)

I follower ricevono un puntatore firmato a una nota di testo kind 1 già pubblicata da qualcuno quando un client scrive un event kind 6. [La specifica dei repost](https://github.com/nostr-protocol/nips/blob/master/18.md) imposta `kind` a 6, inserisce in `content` il JSON serializzato di quella nota (`content` vuoto è consentito ma sconsigliato), richiede un tag `e` il cui valore sia l'`id` della nota e la cui terza voce sia l'URL di un relay da cui recuperarla, e afferma che l'event SHOULD includere anche un tag `p` con la `pubkey` dell'autore originale. Il repost di un event [NIP-70](/it/topics/nip-70/) (event protetti) SHOULD mantenere `content` vuoto, affinché il payload protetto non venga copiato nel nuovo event.

Una citazione è un riferimento all'interno di un altro event, non un wrapper kind 6. Quando un client menziona un [NIP-21](/it/topics/nip-21/) (`nostr:` URI) `nevent`, `note` o `naddr`, deve convertire tale menzione in un tag `q` nella forma `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`. I [tag dei quote repost](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) tengono tali citazioni fuori dai thread di risposta e permettono ai client di recuperare e contare le citazioni di un post.

Kind 6 è riservato alle note kind 1. Un repost generico kind 16 può incapsulare qualsiasi kind di event diverso da kind 1. SHOULD includere un tag `k` il cui valore sia il kind serializzato dell'event interno. Quando tale event interno è sostituibile, il repost generico SHOULD aggiungere un tag `a` con la coordinata `kind:pubkey:d-tag`; se quel tag `a` è assente, il repost prende di mira una versione specifica e `content` deve contenere l'intera stringa JSON di quella versione. Le [regole dei repost generici](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) impediscono che event long-form, indirizzabili e altri event diversi dalle note vengano pubblicati come se fossero kind 1.

Il seguente event kind 6 è un repost reale recuperato da `wss://relay.damus.io` al momento dell’assemblaggio ([apri l’event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)):

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

Il suo `kind` è 6, il tag `e` punta alla nota ripubblicata, il tag `p` identifica l'autore di quella nota e `content` contiene l'event kind 1 originale come JSON serializzato. Questo event recuperato da un relay omette il suggerimento del relay che la [specifica NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md) contrassegna come obbligatorio, illustrando perché lettori e client debbano convalidare event reali e tollerare produttori che omettono campi.

### Reazioni (NIP-25)

Un post può raccogliere like, dislike ed emoji firmati senza che tali segni entrino nel thread di risposta. [La specifica delle reazioni](https://github.com/nostr-protocol/nips/blob/master/25.md) definisce quel segno come un event kind 7 il cui `content` MUST contenere il valore della reazione. `+` o una stringa vuota MUST essere interpretati come like o upvote. `-` MUST essere interpretato come dislike o downvote. Un'emoji o uno shortcode [NIP-30](/it/topics/nip-30/) (emoji personalizzata) SHOULD NOT essere interpretato come like o dislike, e un client MAY mostrare tale emoji sul post.

L'obiettivo si trova nei tag, non viene dedotto da `content`. MUST esserci un tag `e` impostato sull'`id` dell'event obiettivo, e tale tag SHOULD includere un suggerimento relay; tag `e` aggiuntivi sono sconsigliati e, se presenti, l'`id` obiettivo deve essere l'ultimo. SHOULD esserci un tag `p` per l'autore dell'obiettivo, per ultimo se compaiono più tag `p`. Un obiettivo indirizzabile SHOULD ricevere anche un tag `a` con coordinate `kind:pubkey:d-tag`. I tag `e` e `a` SHOULD includere suggerimenti relay e pubkey, i tag `p` SHOULD includere suggerimenti relay e un tag `k` MAY contenere il kind serializzato dell'event oggetto della reazione. [Tali regole sui tag](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) consentono a un client di recuperare l'obiettivo e avvisarne l'autore dal solo event di reazione.

Un client MAY inserire un singolo `:shortcode:` in `content` e un tag `emoji` che associa tale shortcode a un URL immagine, seguendo le [regole delle reazioni con emoji personalizzate](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction). Se l'obiettivo non è un event Nostr nativo, la reazione MUST essere kind 17 e MUST includere i tag `k` e `i` [NIP-73](/it/topics/nip-73/) (ID di contenuto esterno), come nelle [regole delle reazioni a contenuto esterno](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions). Kind 17 è una reazione a un sito web, episodio di podcast o altro oggetto esterno. Non è una reazione event-a-event kind 7 e non è un repost.

Il seguente event kind 7 è una reazione reale recuperata da `wss://relay.damus.io` al momento dell’assemblaggio ([apri l’event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)):

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

Il suo `content` è `+`, il like convenzionale di [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). Il tag `e` indica l'event oggetto della reazione; il tag `a` aggiunge la sua coordinata indirizzabile; il tag `p` ne identifica l'autore; e il tag `k` opzionale registra il kind dell'obiettivo come stringa.

### Implementazioni attuali nei client

[Amethyst](https://github.com/vitorpamplona/amethyst), un client Nostr per Android, definisce il [tipo di event repost](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) e il [tipo di event reazione](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) nel proprio livello di protocollo attuale.

[Snort](https://github.com/v0l/snort), un client Nostr web, implementa [helper NIP-18 che includono la gestione dei tag dei link di citazione](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) e [crea tag di reazione agli event NIP-25](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

[Ditto](https://github.com/soapbox-pub/ditto), un server Mastodon e relay Nostr combinato, [pubblica repost generici kind 16 con un tag `k` e una coordinata `a` sugli obiettivi indirizzabili](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) e [applica la semantica delle reazioni kind 7 trattando l'ultimo tag `e` come event obiettivo](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### Come funzionano insieme

Un event kind 6 o kind 16 ridistribuisce un event esistente nei feed dei follower di chi effettua il repost, incorporando il JSON dell'event oppure puntando a una coordinata sostituibile. Un tag `q` contrassegna una citazione all'interno di un altro event, così la ricostruzione del thread può contare i riferimenti senza trattare l'event che cita come una risposta, distinzione illustrata nella [sezione sui quote repost](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). Un event kind 7 lascia al suo posto l'event originale e vi associa soltanto il valore della reazione e i tag obiettivo, secondo il contratto della [specifica delle reazioni](https://github.com/nostr-protocol/nips/blob/master/25.md). I client che recuperano una pubkey vedono quindi i repost di quella pubkey come nuovi event kind 6 o 16 e le opinioni di quella pubkey come event kind 7 sui post altrui.

---

Inviate un DM NIP-17 per condividere un progetto o una notizia attraverso il [progetto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
