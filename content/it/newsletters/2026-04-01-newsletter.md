---
title: 'Nostr Compass #16'
date: 2026-04-01
translationOf: /en/newsletters/2026-04-01-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [Amethyst](https://github.com/vitorpamplona/amethyst) distribuisce la [v1.07.0](#amethyst-distribuisce-note-fissate-gestione-relay-e-request-to-vanish) con note fissate, gestione relay tramite [NIP-86](/it/topics/nip-86/), e supporto [NIP-62](/it/topics/nip-62/) Request to Vanish. [NIP-5A](#nip-5a-viene-unito-portando-i-siti-web-statici-su-nostr) (Siti Web Statici) viene unito nel repository NIPs, definendo come ospitare siti web sotto keypair Nostr usando lo storage [Blossom](/it/topics/blossom/). [Flotilla](https://gitea.coracle.social/coracle/flotilla) distribuisce la [v1.7.0](#flotilla-v170-aggiunge-stanze-vocali-e-login-email) con stanze vocali, login email/password e DM con proof-of-work. [White Noise](https://github.com/marmot-protocol/whitenoise) corregge il relay churn nella [v2026.3.23](#white-noise-corregge-il-relay-churn-e-amplia-i-controlli-client), [nospeak](https://github.com/psic4t/nospeak) lancia la sua [1.0.0](#nospeak-si-lancia-come-messenger-privato-10) come messenger cifrato senza registrazione. [Nymchat](https://github.com/Spl0itable/NYM) [adotta Marmot](#nymchat-distribuisce-chat-di-gruppo-basate-su-marmot) per chat di gruppo cifrate MLS con fallback NIP-17. [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) raggiunge la [v1.0.0](#calendar-by-form-v100) con liste calendario private e import ICS, [Amber](https://github.com/greenart7c3/Amber) aggiunge [recovery mnemonico e whitelisting relay auth NIP-42](#amber-v502-fino-a-v504), e la [spec Marmot](#marmot-sposta-i-keypackage-su-event-indirizzabili-e-stringe-le-push-notification) sposta i KeyPackage su event indirizzabili mentre stringe il formato delle push notification MIP-05.

## Notizie

### Amethyst distribuisce note fissate, gestione relay e Request to Vanish

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android mantenuto da vitorpamplona, ha distribuito sei rilasci in tre giorni, dalla [v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) alla [v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5). Il set di funzionalità principale copre sei superfici di protocollo: note fissate, una schermata feed dedicata ai sondaggi, supporto [NIP-62](/it/topics/nip-62/) (Request to Vanish) per richiedere la cancellazione completa degli event dai relay, [NIP-86](/it/topics/nip-86/) (Relay Management API) dall'interno del client, valutazioni [NIP-66](/it/topics/nip-66/) (Relay Discovery and Liveness Monitoring) nella schermata informazioni relay, e visualizzazione delle informazioni membri [NIP-43](/it/topics/nip-43/) (Relay Access Metadata and Requests).

[NIP-86](/it/topics/nip-86/) definisce un'interfaccia JSON-RPC per gli operatori relay, permettendo ai client di inviare comandi amministrativi come ban di pubkey, allow di pubkey e lista utenti bannati tramite un'API standardizzata. Amethyst ora espone tutto questo direttamente nella sua UI di gestione relay, così gli utenti che eseguono i propri relay possono amministrarli dallo stesso client che usano per pubblicare. La [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) sostituisce il vecchio dialog di input hex per le pubkey da bannare o consentire con un dialog di ricerca utenti interattivo.

La v1.07.2 ha aggiunto upload dalla tastiera GIF e ha corretto una regressione nella firma in cui le risposte di rifiuto di Amber venivano interpretate male perché le versioni più vecchie di Amber restituivano una stringa vuota per il campo `rejected` ([PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)). La v1.07.5 corregge un crash nel caricamento delle immagini. I rilasci [v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2) e [v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3) all'inizio della settimana hanno aggiunto un selettore del tipo di sondaggio per scelte singole o multiple, drag-to-seek sulle barre di avanzamento video e miglioramenti alla pubblicazione anonima.

### NIP-5A viene unito, portando i siti web statici su Nostr

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) (Siti Web Statici) è stato unito tramite [PR #1538](https://github.com/nostr-protocol/nips/pull/1538), definendo come ospitare siti web statici sotto keypair Nostr. La specifica usa due kind di event: kind `15128` per un sito root, uno per pubkey, e kind `35128` per siti con nome identificati da un tag `d`. Ogni manifesto mappa i percorsi URL agli hash SHA256, con tag `server` opzionali che puntano agli host di storage [Blossom](/it/topics/blossom/) dove vivono i file effettivi.

Il modello di hosting funziona così: l'autore di un sito costruisce un sito statico, carica i file su uno o più server Blossom, poi pubblica un event manifesto firmato che mappa i percorsi agli hash del contenuto. Un server host riceve richieste web, risolve la pubkey dell'autore dal sottodominio, recupera il manifesto dalla relay list [NIP-65](/it/topics/nip-65/) dell'autore, e serve i file scaricando i blob corrispondenti da Blossom. Il sito rimane sotto il controllo dell'autore perché solo quella chiave può firmare un manifesto aggiornato. Il server host è sostituibile perché qualsiasi server che comprende NIP-5A può servire lo stesso sito dallo stesso manifesto.

La specifica si basa su infrastrutture già esistenti. [nsite](https://github.com/lez/nsite), l'implementazione host di riferimento NIP-5A costruita da lez, e [nsite-manager](https://github.com/hzrd149/nsite-manager), la UI di gestione di hzrd149, erano già in esecuzione prima del merge del NIP. Il merge rende ufficiali i kind di event e le regole di risoluzione URL, dando alle seconde e terze implementazioni un obiettivo stabile.

### White Noise corregge il relay churn e amplia i controlli client

[White Noise](https://github.com/marmot-protocol/whitenoise), il messenger privato costruito sul protocollo [Marmot](/it/topics/marmot/), ha distribuito la [v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23) il 25 marzo. Il lavoro principale riguarda la stabilità dei relay. Il login non aspetta più che ogni pubblicazione della relay-list termini prima di proseguire, perché la pubblicazione delle relay-list ora usa logica di quorum e ritenta il resto in background. Fetch e publish one-off usano sessioni relay effimere e delimitate invece di restare nel pool long-lived, le sessioni ripristinate recuperano il loro percorso di refresh di gruppo dopo l'avvio, e l'app ora espone diagnostica relay e ispezione dello stato relay tramite [PR #495](https://github.com/marmot-protocol/whitenoise/pull/495) e [PR #502](https://github.com/marmot-protocol/whitenoise/pull/502).

Lo stesso rilascio cambia anche il comportamento delle conversazioni. La [PR #468](https://github.com/marmot-protocol/whitenoise/pull/468) aggiunge threading delle risposte NIP-C7 con tag `q` e riferimenti `nostr:nevent`, la [PR #471](https://github.com/marmot-protocol/whitenoise/pull/471) e la [PR #512](https://github.com/marmot-protocol/whitenoise/pull/512) mantengono i messaggi cancellati visibili come placeholder cancellati invece di rimuoverli silenziosamente, la [PR #478](https://github.com/marmot-protocol/whitenoise/pull/478) aggiunge un flusso di bug report in-app usando report anonimi [NIP-44](/it/topics/nip-44/) (Encrypted Payloads), e la [PR #486](https://github.com/marmot-protocol/whitenoise/pull/486) aggiunge una chat di supporto direttamente nel client. Nella stessa finestra sono arrivati anche controlli sui messaggi rivolti all'utente: la [PR #532](https://github.com/marmot-protocol/whitenoise/pull/532) archivia le chat, la [PR #541](https://github.com/marmot-protocol/whitenoise/pull/541) aggiunge mute e unmute con durate configurabili, e la [PR #535](https://github.com/marmot-protocol/whitenoise/pull/535) aggiunge impostazioni delle notifiche. La [PR #539](https://github.com/marmot-protocol/whitenoise/pull/539) prepara il lavoro di registrazione push, collegando la registrazione APNs su iOS e il rilevamento Play Services su Android in modo che la registrazione possa essere costruita sopra questo. Sul lato backend, il [MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit) ha aggiunto primitive push notification MIP-05 e un notification request builder ([PR #235](https://github.com/marmot-protocol/mdk/pull/235), [PR #238](https://github.com/marmot-protocol/mdk/pull/238)), mentre [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) ha aggiunto la persistenza della registrazione push notification ([PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)), correzioni alla cancellazione dei task in background ([PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)), e recovery dei key package all'avvio ([PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693)).

### Nostr VPN raggiunge la v0.3.0 con roster sync e invite v2

[Come da copertura del lancio della settimana scorsa](/it/newsletters/2026-03-25-newsletter/#nostr-vpn-si-lancia-come-alternativa-a-tailscale), [nostr-vpn](https://github.com/mmalmi/nostr-vpn), la VPN peer-to-peer che usa relay Nostr per la segnalazione e WireGuard per tunnel cifrati, ha continuato il suo ritmo di rilascio rapido, distribuendo versioni fino alla [v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3). Il salto di versione porta due cambi incompatibili: il formato invite passa alla v2 (la 0.3.0 può ancora importare invite v1, ma le build più vecchie non possono importare invite v2), e il roster sync firmato dall'admin è stato aggiunto al protocollo di segnalazione. I peer con versioni miste possono ancora connettersi a livello mesh, ma i peer più vecchi non partecipano alla sincronizzazione del roster.

L'aggiunta del roster sync avvia il passaggio verso una rete gestita. Un nodo admin può ora inviare cambiamenti di appartenenza a tutti i peer, così aggiungere o rimuovere un dispositivo dalla mesh non richiede che ogni peer aggiorni manualmente la propria configurazione. I rilasci v0.2.x nella stessa settimana hanno affrontato problemi specifici di deployment: dalla [v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22) alla [v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28) hanno corretto la gestione del servizio Windows, aggiunto script di build Android, e perfezionato il flusso di pairing LAN.

### nospeak si lancia come messenger privato 1.0

[nospeak](https://github.com/psic4t/nospeak), un messenger privato costruito su Nostr, ha distribuito il rilascio [1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0) il 27 marzo. Il progetto include conversazioni uno-a-uno e di gruppo, gestione contatti, e un'architettura self-hostable. Le chat uno-a-uno usano [NIP-17](/it/topics/nip-17/) (Private Direct Messages), che combina [NIP-59](/it/topics/nip-59/) (Gift Wrap) con [NIP-44](/it/topics/nip-44/) (Encrypted Payloads) per nascondere il mittente ai relay. Per i media, i file sono cifrati lato client con AES-256-GCM prima dell'upload sui server Blossom. Il rilascio viene distribuito anche come immagine container per il self-hosting.

### Flotilla v1.7.0 aggiunge stanze vocali e login email

[Flotilla](https://gitea.coracle.social/coracle/flotilla), il client in stile Discord di hodlbod basato su [NIP-29](/it/topics/nip-29/) (Relay-based Groups) e sul modello “relay come gruppi”, ha distribuito la [v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0) e la [v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1) il 30 e 31 marzo. La funzionalità principale sono le stanze vocali, contribuite da mplorentz. Gli utenti possono ora unirsi a chiamate vocali all'interno dei canali di gruppo, con un dialog di ingresso ([PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109)) che permette di selezionare il dispositivo di input audio e scegliere se entrare nella chiamata vocale o solo visualizzare la chat testuale. Il dialog risolve un problema UX della precedente iterazione: entrare in una stanza con voce attiva accendeva prima il microfono anche quando l'utente voleva solo leggere i messaggi o controllare le impostazioni della stanza.

Lo stesso rilascio aggiunge il login email e password come alternativa all'autenticazione basata su chiave Nostr, proof-of-work sui DM, editing dei DM, onboarding e impostazioni relay ridisegnati, rilevamento del supporto Blossom tramite `supported_nips`, badge notifiche migliorati, fallback push notification su Android, e correzioni agli upload file su Android. La v1.7.1 segue con una correzione per il fallback di registrazione pomade quando si usa un signer offline.

Hodlbod sta anche costruendo [Caravel](https://gitea.coracle.social/coracle/caravel), un hosting manager e dashboard per relay zooid, che ha registrato 40 commit questa settimana nella fase iniziale di sviluppo.

### Nymchat distribuisce chat di gruppo basate su Marmot

[Nymchat](https://github.com/Spl0itable/NYM) (noto anche come NYM, Nostr Ynstant Messenger), il client di chat effimero collegato a Bitchat, ha annunciato che tutte le nuove chat di gruppo ora usano il protocollo [Marmot](/it/topics/marmot/) per messaggistica cifrata MLS. L'integrazione usa kind `443`, `444`, e `445` per key package, welcome message e group message rispettivamente, fornendo forward secrecy, post-compromise security e zero metadata leakage. Se un destinatario non può usare MLS, Nymchat ricade sul suo precedente percorso di chat di gruppo [NIP-17](/it/topics/nip-17/) (Private Direct Messages), che è comunque cifrato end-to-end ma privo delle proprietà a ratchet-tree di MLS.

Le serie v3.55 e v3.56 di questa settimana si sono concentrate sui casi limite delle chat di gruppo: caricamento su nuovi dispositivi, comportamento di uscita, instradamento delle notifiche, e conteggi dei badge non letti. Lo stesso ciclo ha anche corretto una vulnerabilità XSS dovuta a HTML non escapato e ha aggiunto il blocco di parole chiave e frasi esteso ai nickname utente. Questo rende Nymchat un altro client Marmot che si unisce a [White Noise](#white-noise-corregge-il-relay-churn-e-amplia-i-controlli-client) e [OpenChat](#openchat-v024-fino-a-v030), ampliando l'insieme di app che possono scambiare messaggi di gruppo cifrati MLS sullo stesso protocollo.

## Rilasci

### Calendar by Form* v1.0.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), l'app calendario decentralizzata costruita su [NIP-52](/it/topics/nip-52/) (Calendar Events), ha raggiunto la [v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0) il 29 marzo. Il rilascio aggiunge liste calendario private usando event Nostr cifrati (kind `32123`) con auto-cifratura [NIP-44](/it/topics/nip-44/) (Encrypted Payloads), così gli utenti possono organizzare gli eventi in collezioni private senza esporre il raggruppamento ai relay. Lo stesso rilascio aggiunge la gestione degli intent ICS per importare dati calendario da altre applicazioni e richieste di invito per condividere eventi tra utenti.

### Amber v5.0.2 fino a v5.0.4

[Amber](https://github.com/greenart7c3/Amber), l'app signer [NIP-55](/it/topics/nip-55/) (Android Signer Application), ha distribuito tre point release: [v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2), [v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3), e [v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4). L'aggiunta più visibile è il login tramite frase mnemonica di recovery ([PR #358](https://github.com/greenart7c3/Amber/pull/358)), che permette agli utenti di ripristinare il proprio signer da una seed phrase BIP39 invece di richiedere la stringa nsec o ncryptsec grezza. La [PR #357](https://github.com/greenart7c3/Amber/pull/357) aggiunge una whitelist relay auth [NIP-42](/it/topics/nip-42/), così gli utenti possono limitare quali relay sono autorizzati a richiedere l'autenticazione client. La [PR #353](https://github.com/greenart7c3/Amber/pull/353) aggiunge la selezione dell’ambito di cifratura per i permessi di decrypt, permettendo agli utenti di concedere accesso di decrypt solo NIP-04 o solo NIP-44 invece di un permesso generale. La v5.0.4 corregge un bug in cui il rifiuto non rispettava i permessi scoped di encrypt e decrypt e migliora le prestazioni quando arrivano più richieste bunker.

### Aegis v0.4.0

[Aegis](https://github.com/ZharlieW/Aegis), il signer cross-platform, ha distribuito la [v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0) il 26 marzo. Il rilascio aggiunge le modalità di autorizzazione Full e Selective nelle Impostazioni e corregge diversi problemi di scansione QR. I commit successivi [d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b), [3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7), [3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f), e [e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e) continuano lo stesso lavoro con controlli batch select, statistiche riutilizzabili sulle selezioni batch, API set-all-groups selection, e statistiche di utilizzo per permesso nella pagina dei permessi dell'app.

### Schemata v0.2.7 fino a v0.3.0

[Schemata](https://github.com/nostrability/schemata), le definizioni JSON Schema per la validazione dei kind di event Nostr, ha distribuito quattro rilasci dalla [v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7) alla [v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0) con 21 PR unite. Il rilascio v0.3.0 porta correzioni di coerenza dei pattern per URL relay, ID hex, tipi MIME, e stringhe BOLT-11 ([PR #126](https://github.com/nostrability/schemata/pull/126)), centralizzazione dei pattern URL relay ([PR #117](https://github.com/nostrability/schemata/pull/117)), schemi del tipo base bech32 [NIP-19](/it/topics/nip-19/) ([PR #118](https://github.com/nostrability/schemata/pull/118)), e validazione per gli event spell kind 777 ([PR #125](https://github.com/nostrability/schemata/pull/125)). La pipeline di rilascio ora pubblica una nota kind `1` su Nostr per ogni rilascio ([PR #120](https://github.com/nostrability/schemata/pull/120)), così il progetto si annuncia attraverso il protocollo che valida. Schemata ora supporta una dozzina di linguaggi oltre al pacchetto canonico JS/TS: Rust, Go, Python, Kotlin, Java, Swift, Dart, PHP, C#/.NET, C++, Ruby, e C.

Accanto a Schemata, il team ha pubblicato [schemata-codegen](https://github.com/nostrability/schemata-codegen), un generatore di codice sperimentale che affronta lo stesso problema di validazione con un approccio diverso. Dove i pacchetti validator di Schemata richiedono una dipendenza runtime da JSON Schema, schemata-codegen converte gli schemi direttamente in costrutti tipizzati nativi del linguaggio (tuple tipizzate per tag, interfacce kind, e validator runtime), rimuovendo la necessità di una libreria validator a runtime. Il documento [codegen-vs-validators comparison](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md) spiega quando ciascun approccio è adatto.

### BigBrotr v6.5.0 fino a v6.5.4

[BigBrotr](https://github.com/BigBrotr/bigbrotr), la piattaforma di analisi relay, ha distribuito cinque rilasci dalla [v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0) alla [v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4). La v6.5.0 centralizza la validazione degli URL relay con una factory function `parse_relay_url()` e aggiunge controlli sulla lunghezza URL e sanitizzazione dei path. Anche l'infrastruttura di monitoraggio ha ricevuto correzioni: gli event di annuncio ora includono tag di geolocalizzazione geohash (seguendo [NIP-52](/it/topics/nip-52/)), ed è stata aggiunta protezione timeout ai test di metadati Geo/Net [NIP-66](/it/topics/nip-66/) che non avevano scadenza e potevano bloccarsi indefinitamente. La [PR #410](https://github.com/BigBrotr/bigbrotr/pull/410) aggiorna PostgreSQL dalla 16 alla 18, portando il sottosistema async I/O e un throughput WAL migliorato alla pipeline di analisi relay.

### Il relay Vertex Lab aggiunge la ricerca profili NIP-50

[Vertex Lab](https://vertexlab.io), il team dietro [npub.world](https://github.com/vertex-lab/npub.world) e il motore Web of Trust [Vertex](https://vertexlab.io/docs), ha annunciato che `wss://relay.vertexlab.io` ora supporta [NIP-50](/it/topics/nip-50/) (Search) per le query sui profili. NIP-50 estende il filtro standard `REQ` di Nostr con un campo `search`, permettendo ai client di inviare query full-text ai relay che supportano l'indicizzazione. Aggiungere la ricerca profili a un relay che serve già dati Web of Trust significa che i client connessi a `relay.vertexlab.io` possono scoprire utenti per nome o descrizione senza un servizio di ricerca separato.

### Hashtree v0.2.17 e v0.2.18 distribuiscono mesh WebRTC e Iris Desktop

[Hashtree](https://github.com/mmalmi/hashtree), il sistema di storage blob content-addressed di mmalmi che pubblica radici Merkle su Nostr, ha distribuito la [v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17) e la [v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18) il 31 marzo. I due rilasci chiudono uno sprint di 30 commit che aggiunge tre capacità distinte. Primo, il crate `hashtree-webrtc` (rinominato `hashtree-network` nella v0.2.18) aggiunge distribuzione blob peer-to-peer basata su WebRTC con segnalazione mesh unificata attraverso la CLI Rust, l'harness di simulazione, e il client TypeScript. Secondo, la pipeline di rilascio ora costruisce artefatti Windows (zip CLI e installer Iris), portando copertura cross-platform su macOS, Linux e Windows. Terzo, entrambi i rilasci includono Iris Desktop 0.1.0, il client social Nostr di mmalmi, come asset AppImage, .deb e installer Windows accanto alla CLI hashtree. [Hashtree è stato trattato per la prima volta nella Newsletter #10](/it/newsletters/2026-02-18-newsletter/) quando è stato lanciato come store compatibile [Blossom](/it/topics/blossom/) basato su filesystem. Il livello WebRTC è il primo passo verso una distribuzione dei contenuti peer-to-peer senza dipendere da server Blossom centralizzati.

### Nostr Mail Client v0.7.0 fino a v0.7.2

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client), il client in stile email Flutter costruito su identità Nostr, ha distribuito la [v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0), la [v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1), e la [v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2) in tre giorni. Il lavoro di prodotto più visibile si è concentrato su onboarding ([PR #9](https://github.com/nogringo/nostr-mail-client/pull/9)) e modifica profilo ([PR #10](https://github.com/nogringo/nostr-mail-client/pull/10)), elementi di base per qualsiasi client che cerca di presentare Nostr come una casella di posta. Le point release successive hanno impacchettato quel lavoro in nuove build Android e Linux.

### Wisp v0.14.0 fino a v0.16.1

[Wisp](https://github.com/barrydeen/wisp), il client Nostr Android, ha distribuito altri 13 rilasci dalla [v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta) alla [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta). Il lavoro di questa settimana include correzioni al JSON rumor NIP-17 ([PR #385](https://github.com/barrydeen/wisp/pull/385)), badge repost sulle gallery card ([PR #383](https://github.com/barrydeen/wisp/pull/383)), dettagli delle reazioni espandibili ([PR #382](https://github.com/barrydeen/wisp/pull/382)), set emoji persistenti ([PR #381](https://github.com/barrydeen/wisp/pull/381)), e controlli di autoplay video ([PR #380](https://github.com/barrydeen/wisp/pull/380)). L'ultima [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta) corregge anche shortcode emoji personalizzate con trattini e tag emoji mancanti.

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app) ha distribuito la [3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17) il 24 marzo. La [PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000) mappa i tipi WalletException in codici errore nelle risposte NWC, dando ai client [NIP-47](/it/topics/nip-47/) informazioni di errore strutturate invece di errori generici. La [PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995) corregge i voti zap dei sondaggi che apparivano come Top Zaps, e la [PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998) nasconde il saldo wallet e i pulsanti di azione quando non è configurato alcun wallet.

### OpenChat v0.2.4 fino a v0.3.0

[OpenChat](https://github.com/DavidGershony/openChat), il client chat basato su Avalonia costruito sullo stack [Marmot](/it/topics/marmot/), ha distribuito sei rilasci dalla [v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4) alla [v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0) in quattro giorni. Il log dei commit racconta la storia di un client che colma il divario tra “Marmot funziona” e “qualcuno può davvero usarlo ogni giorno”. È arrivata l'autenticazione relay [NIP-42](/it/topics/nip-42/), seguita da una UI relay picker con filtraggio degli event duplicati. I messaggi vocali hanno ottenuto pausa, ripresa, seek e visualizzazione del tempo. Il percorso signer è stato rafforzato: le connessioni Amber sono state corrette con un formato URI [NIP-46](/it/topics/nip-46/) aggiornato, il WebSocket si riconnette automaticamente prima di inviare le richieste, e le richieste Amber duplicate ora vengono intercettate controllando le risposte riprodotte. Sul lato storage, Linux e macOS hanno ottenuto secure storage AES-256-GCM con chiavi salvate su file, e il recupero dei metadata utente ora usa la discovery relay [NIP-65](/it/topics/nip-65/) e mette in cache i risultati in un database locale.

### Igloo Signer 1.1

[Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype), il signer threshold [FROST](/it/topics/frost/) per iOS del progetto FROSTR, ha distribuito la [v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1) il 28 marzo. Le firme FROST (Flexible Round-Optimized Schnorr Threshold) permettono a un gruppo di signer di controllare collettivamente un keypair Nostr, dove qualsiasi insieme t-of-n di partecipanti può firmare un event senza che nessuna singola parte possieda la chiave privata completa. Igloo è una delle prime implementazioni mobili di questo approccio per Nostr.

### nak v0.19.3 e v0.19.4

[nak](https://github.com/fiatjaf/nak), il toolkit Nostr a riga di comando di fiatjaf, ha distribuito la [v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3) e la [v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4) il 26 e 30 marzo. Entrambi i rilasci correggono condizioni di panic: la [PR #118](https://github.com/fiatjaf/nak/pull/118) sostituisce `strings.Split` con `strings.Cut` per prevenire un potenziale accesso out-of-bounds, e la [PR #119](https://github.com/fiatjaf/nak/pull/119) previene la stessa classe di panic nel parsing dei flag curl.

### Flora v0.3.0

[Flora](https://github.com/shawnyeager/flora-extension), un'estensione Chrome per screen recording e condivisione decentralizzati su Nostr, ha distribuito la [v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0). Il rilascio aggiunge condivisione video privata cifrata con modalità pubblica, non in elenco e privata. Le registrazioni private sono cifrate con AES-256-GCM e consegnate ai destinatari tramite [NIP-17](/it/topics/nip-17/) (Private Direct Messages), così la registrazione non tocca mai un server in chiaro.

### YakiHonne Mobile 2.0.3

[YakiHonne](https://github.com/YakiHonne/mobile-app), il client mobile Nostr, ha distribuito la [2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3) con recensioni relay e join request, risposte nidificate ampliate, traduzione automatica delle note, e supporto multi-relay NWC.

## Aggiornamenti Progetti

### Zap Cooking aggiunge zap poll e verifica dei pagamenti Branta

[Zap Cooking](https://github.com/zapcooking/frontend), la piattaforma di ricette e contenuti, ha unito 11 PR questa settimana focalizzate su contenuti interattivi e flussi di pagamento. La [PR #277](https://github.com/zapcooking/frontend/pull/277) aggiunge gli zap poll (kind 6969), in cui gli utenti votano inviando sats e possono vedere le liste dei votanti con foto profilo. La [PR #274](https://github.com/zapcooking/frontend/pull/274) ridisegna la UX dei sondaggi in modo che l'interfaccia di voto si integri più naturalmente nel feed.

La [PR #276](https://github.com/zapcooking/frontend/pull/276) aggiunge scansione QR tramite fotocamera al flusso Send Payment e integra [Branta](https://branta.pro/), un servizio di verifica che controlla se una destinazione di pagamento è legittima prima dell'invio. Branta verifica le destinazioni di pagamento contro phishing, address swap e intercettazioni man-in-the-middle prima dell'invio. Nell'implementazione di Zap Cooking, un nome piattaforma e logo verificati da Branta appaiono direttamente nel flusso di pagamento, e i QR code abilitati a Branta possono trasportare parametri `branta_id` e `branta_secret` così il wallet può verificare la destinazione direttamente dal codice scansionato.

### diVine prepara le basi per una ricerca unificata e rafforza la consegna video

[diVine](https://github.com/divinevideo/divine-mobile), il client di video brevi, ha passato la settimana a stringere ricerca, navigazione del feed, recovery della riproduzione, e comportamento di upload. La [PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540) getta le basi per una schermata di ricerca unificata, con sezioni raggruppate per Video, Persone, e Tag. La [PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623) rafforza la paginazione su feed profilo, inbox, notifiche, liste discover, classic vines, ricerca, e feed a griglia componibili spostandoli su un controller di paginazione condiviso.

Anche la consegna video ha ricevuto diverse correzioni concrete. La [PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643) ritenta in ordine le sorgenti derivate ospitate da Divine e ricade sul blob grezzo prima di mostrare un errore di riproduzione, così fallimenti transitori su una sorgente non uccidono subito la riproduzione. La [PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634) mantiene gli upload resumable sul percorso gestito da Divine quando il capability probing fallisce temporaneamente, riducendo gli upload rotti causati da brevi guasti di rete. La [PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637) cambia anche il filtro dei contenuti sensibili in modo che i video siano bloccati rigidamente solo per etichette di avviso reali, non semplicemente per content warning impostati dal creatore.

### Shopstr aggiunge storefront personalizzati e Milk Market continua a distribuire lavoro di marketplace

[Shopstr](https://github.com/shopstr-eng/shopstr), il marketplace basato su Nostr, ha unito la [PR #245](https://github.com/shopstr-eng/shopstr/pull/245) aggiungendo storefront personalizzati. Questo dà ai venditori una superficie home più distintiva invece di costringere ogni annuncio nella stessa presentazione generica.

[Milk Market](https://github.com/shopstr-eng/milk-market), un marketplace dedicato al latte, ha continuato con ottimizzazioni degli storefront ([PR #18](https://github.com/shopstr-eng/milk-market/pull/18)), account recovery ([PR #17](https://github.com/shopstr-eng/milk-market/pull/17)), beef splits ([PR #15](https://github.com/shopstr-eng/milk-market/pull/15)), e correzioni ai tipi degli strumenti MCP ([PR #16](https://github.com/shopstr-eng/milk-market/pull/16)).

### Notedeck aggiunge effetti sonori e estende il suo percorso updater verso Android

[Notedeck](https://github.com/damus-io/notedeck), il client desktop del team Damus, ha unito la [PR #1412](https://github.com/damus-io/notedeck/pull/1412) aggiungendo un sottosistema di effetti sonori con suoni di interazione UI usando rodio, e la [PR #1399](https://github.com/damus-io/notedeck/pull/1399) con aggiornamenti Agentium inclusi un flag CLI per il titolo e cartelle di sessione comprimibili. Una [PR #1417](https://github.com/damus-io/notedeck/pull/1417) aperta propone l'auto-aggiornamento APK via Nostr/Zapstore su Android, costruendo sul [lavoro updater nativo Nostr di Notedeck dalla Newsletter #14](/it/newsletters/2026-03-18-newsletter/#notedeck-sposta-la-scoperta-dei-rilasci-su-nostr).

### Nostria aggiunge relay hint per i repost e allineamento NIP-98

[Nostria](https://github.com/nostria-app/nostria) ha unito la [PR #583](https://github.com/nostria-app/nostria/pull/583) aggiungendo relay hint [NIP-18](/it/topics/nip-18/) (Reposts) ai tag `e` dei repost per gli event kind 6 e kind 16, la [PR #582](https://github.com/nostria-app/nostria/pull/582) allineando l'HTTP auth Brainstorm (kind 27235) ai tag richiesti da [NIP-98](/it/topics/nip-98/) (HTTP Auth), e la [PR #576](https://github.com/nostria-app/nostria/pull/576) aggiungendo test di validazione degli schemi Schemata. Il cambiamento NIP-98 significa che Nostria può autenticarsi verso servizi esterni usando lo stesso formato HTTP auth che usano gli altri client.

### Nostr-Doc aggiunge packaging desktop e lavoro offline-first

[Nostr-Doc](https://github.com/formstr-hq/nostr-docs), l'editor collaborativo di Form*, ha avuto una settimana intensa di packaging e lavoro sull'editor. Il [commit fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4) aggiunge un'app desktop, il [commit 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927) avvia il lavoro sull'app nativa, e il [commit 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869) spinge l'app verso un comportamento offline-first. Sul lato editor, il [commit 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786) aggiunge salvataggio Ctrl+S, avvisi di salvataggio, correzioni alle anteprime link, e rendering corretto del barrato.

### rust-nostr ottimizza il parsing NIP-21 e aggiunge supporto NIP-62 lato relay

[rust-nostr](https://github.com/rust-nostr/nostr) ha unito otto PR. La più notevole è la [PR #1308](https://github.com/rust-nostr/nostr/pull/1308), che ottimizza il parsing degli URI [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) in `PublicKey::parse` allineandolo alle prestazioni standard del parsing bech32. In precedenza, gli URI NIP-21 richiedevano circa il doppio del tempo per essere analizzati rispetto alle chiavi bech32 grezze. Il progetto ha anche quattro PR aperte che aggiungono supporto specifico relay a [NIP-62](/it/topics/nip-62/) (Request to Vanish) nei backend memory, LMDB, SQLite, e database test ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)).

### nostr-tools aggiunge controllo relay bunker e corregge il parsing multi-relay NIP-47

[nostr-tools](https://github.com/nbd-wtf/nostr-tools) ha unito la [PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530) aggiungendo `skipSwitchRelays` ai BunkerSignerParams per la gestione manuale dei relay, e la [PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529) correggendo il parsing delle stringhe di connessione [NIP-47](/it/topics/nip-47/) (Nostr Wallet Connect) per supportare più relay come consente la specifica.

### Nostrability integra i dati di audit Sherlock e pubblica una panoramica di Schemata

[Nostrability](https://github.com/nostrability/nostrability), l'interoperability tracker per i client Nostr, ha unito 14 PR. La [PR #306](https://github.com/nostrability/nostrability/pull/306) integra le statistiche delle scansioni Sherlock nella dashboard. Sherlock è lo strumento di audit automatizzato di Nostrability che si connette ai client Nostr, cattura gli event che pubblicano, e valida ogni event rispetto alle definizioni JSON Schema di Schemata per rilevare violazioni della specifica. La dashboard ora mostra i tassi di fallimento degli schemi per client ([PR #315](https://github.com/nostrability/nostrability/pull/315)) così gli sviluppatori possono vedere quali kind di event il proprio client sbaglia. La [PR #323](https://github.com/nostrability/nostrability/pull/323) rivede il workflow di pubblicazione Nostr in modo che gli annunci di rilascio girino come job separato che non può essere cancellato da step CI precedenti.

elsat ha anche pubblicato [Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww) il 30 marzo, descrivendo come schemata, schemata-codegen e Sherlock si incastrano e dando i numeri attuali di copertura: 179 schemi di kind event su 65 NIP, 154 schemi di tag, 13 messaggi di protocollo, e 310 event di esempio.

### Nalgorithm aggiunge generazione digest e caching locale del punteggio

[Nalgorithm](https://github.com/jooray/nalgorithm), un nuovo progetto feed Nostr ordinato per rilevanza, ha avviato lo sviluppo pubblico questa settimana. Il [commit cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43) imposta l'app web iniziale che recupera i post dai follow e li valuta rispetto a un prompt di preferenze definito dall'utente. Il [commit 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86) aggiunge uno strumento CLI digest che trasforma i post più rilevanti in un riepilogo parlato, mentre il [commit 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153) aggiunge caching del punteggio basato su file e evoluzione incrementale del prompt appreso a partire dai like recenti. Il [commit c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03) smette anche di mettere in cache i fallback score da batch falliti, così un fallimento transitorio del punteggio non appiattisce permanentemente il ranking di un post.

### TENEX aggiunge vector store RAG e startup MCP mirato

[TENEX](https://github.com/tenex-chat/tenex), il framework agenti nativo Nostr che collega agenti AI ai canali Nostr via Telegram, ha unito sette PR questa settimana. La [PR #101](https://github.com/tenex-chat/tenex/pull/101) aggiunge un'astrazione vector store pluggable con backend SQLite-vec, LanceDB, e Qdrant, dando agli agenti retrieval-augmented generation senza vincolarsi a un singolo database vettoriale. La [PR #102](https://github.com/tenex-chat/tenex/pull/102) rende lo startup MCP mirato: vengono avviati solo i server MCP i cui strumenti un agente usa davvero, invece di lanciare tutti i server subito alla prima esecuzione. La [PR #100](https://github.com/tenex-chat/tenex/pull/100) aggiunge uno strumento `send_message` così gli agenti con binding ai canali Telegram possono inviare messaggi proattivamente invece di limitarsi a rispondere a quelli in arrivo. La [PR #106](https://github.com/tenex-chat/tenex/pull/106) evita uno spawn di sottoprocesso che attivava una pre-allocazione da 9GB di memoria Bun/JSC leggendo `.git/HEAD` direttamente invece di eseguire `git branch`.

### Dart NDK sposta il signer Amber e aggiunge Alby Go 1-click

[Dart NDK](https://github.com/relaystr/ndk), il Flutter Nostr development kit, ha distribuito 11 PR unite. La [PR #525](https://github.com/relaystr/ndk/pull/525) sposta il supporto al signer Amber nel pacchetto ndk_flutter, e la [PR #552](https://github.com/relaystr/ndk/pull/552) aggiunge la connessione wallet one-click Alby Go all'app di esempio. La [PR #502](https://github.com/relaystr/ndk/pull/502) aggiunge uno script install.sh per la CLI, e la [PR #523](https://github.com/relaystr/ndk/pull/523) rimuove la dipendenza dal verifier Rust a favore della gestione nativa degli asset.

## Lavoro su Protocollo e Specifica

### Marmot sposta i KeyPackage su event indirizzabili e stringe le push notification

La [specifica Marmot](https://github.com/marmot-protocol/marmot) ha unito quattro PR che cambiano il modo in cui il protocollo gestisce il materiale chiave e l'appartenenza ai gruppi. La [PR #54](https://github.com/marmot-protocol/marmot/pull/54) migra gli event KeyPackage dal normale `kind:443` al `kind:30443` indirizzabile con tag `d`, eliminando la necessità di cancellazione event [NIP-09](/it/topics/nip-09/) durante la rotazione delle chiavi. Gli event indirizzabili si sovrascrivono sul posto, rendendo la rotazione auto-contenuta. La [PR #57](https://github.com/marmot-protocol/marmot/pull/57) permette agli utenti non admin di fare commit di proposte SelfRemove (uscita volontaria dal gruppo), e la [PR #62](https://github.com/marmot-protocol/marmot/pull/62) richiede agli admin di rinunciare allo status di admin prima di usare SelfRemove, impedendo a un admin di sparire mantenendo ancora privilegi elevati.

La [PR #61](https://github.com/marmot-protocol/marmot/pull/61) stringe il formato delle push notification [MIP-05](/it/topics/mip-05/), rendendo espliciti la codifica base64 single-blob, il versioning, il formato wire del token, e l'uso delle chiavi x-only. L'effetto è una singola rappresentazione wire definita per token blob e chiavi x-only attraverso la specifica, le librerie client, e i backend delle app. L'implementazione di questi cambi di specifica è arrivata nello stack White Noise questa settimana ed è coperta nella [sezione White Noise v2026.3.23 sopra](#white-noise-corregge-il-relay-churn-e-amplia-i-controlli-client).

### Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti:**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md): Siti Web Statici** ([PR #1538](https://github.com/nostr-protocol/nips/pull/1538)): Definisce gli event manifesto kind `15128` (sito root) e kind `35128` (sito con nome) per ospitare siti statici sotto keypair Nostr usando lo storage Blossom. Vedi il [deep dive sotto](#nip-deep-dive-nip-5a-siti-web-statici).

- **[NIP-30](/it/topics/nip-30/) (Custom Emoji): Permettere i trattini negli shortcode** ([PR #2297](https://github.com/nostr-protocol/nips/pull/2297)): Aggiorna la descrizione degli shortcode per includere i trattini. Gli shortcode con trattini sono stati usati nella pratica fin dall'introduzione del NIP, quindi la specifica ora documenta l'uso corrente.

**PR Aperte e Discussioni:**

- **NIP-C1: Agent TUI Messages** ([PR #2295](https://github.com/nostr-protocol/nips/pull/2295)): Propone un formato di messaggio strutturato per gli agenti che inviano elementi UI interattivi tramite DM cifrati, inclusi payload tipizzati `text`, `buttons`, `card`, e `table`. La bozza mantiene tutto dentro il contenuto JSON degli existing DM [NIP-17](/it/topics/nip-17/) e [NIP-04](/it/topics/nip-04/). Non definisce un nuovo kind di event e usa un semplice formato stringa callback per le risposte ai pulsanti.

- **NIP-95: Hybrid Peer-to-Peer Relay Protocol** ([PR #2293](https://github.com/nostr-protocol/nips/pull/2293)): Propone un modello relay ibrido in cui i relay restano autorevoli ma possono anche coordinare la distribuzione peer-to-peer degli event recenti via WebRTC. La bozza introduce messaggi relay come `PEER_REGISTER`, `PEER_REQUEST`, e `PEER_OFFER`, con client stabili che agiscono da Super Peer e il relay che funge da seed node e fallback.

- **NIP-B9: Zap Poll Events** ([PR #2284](https://github.com/nostr-protocol/nips/pull/2284)): Riapre la vecchia idea NIP-69 degli zap-poll ora che [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) (Polls) copre i sondaggi gratuiti. La bozza usa definizioni di sondaggi kind `6969` e zaps kind `9734` come voti, rendendolo un sistema di polling a pagamento con resistenza economica ai Sybil. Completa i sondaggi gratuiti one-key-one-vote.

- **NIP-AD: Super Zap** ([PR #2289](https://github.com/nostr-protocol/nips/pull/2289)): Propone una convenzione in cui gli zap inviati alla pubkey di un relay o a quella di un client vengono mostrati come note promozionali specializzate, trasformando di fatto le zap receipt in una superficie pubblicitaria. Gli operatori relay e i client pubblicherebbero profili con `lud16`, recupererebbero quelle receipt, estrarrebbero il contenuto incorporato dalle descrizioni zap, e potrebbero opzionalmente impostare soglie minime in sats per sopprimere lo spam.

- **NIP-XX: Agent Reputation Attestations** ([PR #2285](https://github.com/nostr-protocol/nips/pull/2285)): Propone kind `30085` come event sostituibile parametrizzato per attestazioni strutturate di reputazione sugli agenti Nostr. La bozza evita un singolo punteggio globale rendendo la reputazione dipendente dall'osservatore, aggiunge decadimento temporale così le attestazioni vecchie perdono peso, supporta rating negativi con requisiti di evidenza, e abbozza sia punteggio ponderato semplice sia punteggio di diversità del grafo per migliore resistenza Sybil.

- **NIP-XX: Paid API Service Announcements** ([PR #2291](https://github.com/nostr-protocol/nips/pull/2291)): Propone event indirizzabili kind `31402` per pubblicizzare API HTTP a pagamento, con Nostr che gestisce discovery e pagamento tramite HTTP 402. La bozza è tags-first così i relay possono filtrare su metodi di pagamento, prezzi e capacità senza fare parsing di contenuto JSON, e permette schemi opzionali di richiesta e risposta così client o agenti possono auto-generare le chiamate.

- **NIP-XX: Key Derivation from LNURL-auth via SplitSig** ([PR #2294](https://github.com/nostr-protocol/nips/pull/2294)): Propone di derivare un keypair Nostr da una firma ECDSA LNURL-auth combinata con un nonce casuale lato client. La formula di derivazione è `nsec = SHA256(ecdsa_signature || nonce)`. Il server vede la firma ECDSA (intrinseca all'handshake LNURL-auth) ma non vede mai il nonce, e il browser genera il nonce ma non controlla la firma. Nessun pezzo da solo può derivare l'nsec. L'obiettivo è che lo stesso wallet Lightning produca la stessa chiave Nostr su dispositivi diversi, con il wallet come àncora di recovery e nessun server in grado di ricostruire la chiave privata.

- **[NIP-55](/it/topics/nip-55/): Documentare il campo rejected** ([PR #2290](https://github.com/nostr-protocol/nips/pull/2290)): Documenta il campo `rejected` per le risposte dei signer intent-based, formalizzando il comportamento che la [correzione di Amethyst v1.07.x](#amethyst-distribuisce-note-fissate-gestione-relay-e-request-to-vanish) ha dovuto aggirare.

## NIP Deep Dive: NIP-5A (Siti Web Statici)

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) definisce come ospitare siti web statici sotto keypair Nostr, usando due kind di event e l'infrastruttura blob esistente per trasformare event firmati in pagine web servite. La [specifica](https://github.com/nostr-protocol/nips/blob/master/5A.md) è stata unita il 25 marzo tramite [PR #1538](https://github.com/nostr-protocol/nips/pull/1538).

Il modello usa kind `15128` per un sito root, uno per pubkey, e kind `35128` per siti con nome identificati da un tag `d`. Ogni manifesto mappa percorsi URL assoluti agli hash SHA256. Ecco un manifesto di sito root:

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

Il flusso di serving funziona in tre passaggi. Un server host riceve una richiesta HTTP, estrae la pubkey dell'autore dal sottodominio (un npub per i siti root o una pubkey codificata base36 per i siti con nome), recupera la relay list dell'autore tramite [NIP-65](/it/topics/nip-65/), e interroga il manifesto del sito. Una volta trovato il manifesto, il server risolve il path richiesto in un hash di contenuto, scarica il blob corrispondente dal server o dai server Blossom elencati nei tag `server`, e lo restituisce.

Il formato del sottodominio DNS è strettamente specificato. I siti root usano l'npub standard come sottodominio. I siti con nome usano una codifica base36 di 50 caratteri della pubkey grezza seguita dal valore del tag `d`, tutto in una singola etichetta DNS. Poiché le etichette DNS sono limitate a 63 caratteri e la codifica base36 ne occupa sempre 50, il tag `d` è limitato a 13 caratteri. La specifica richiede anche che i tag `d` corrispondano a `^[a-z0-9-]{1,13}$` e non terminino con un trattino, evitando ambiguità nella risoluzione DNS.

L'uso di hash del contenuto significa che lo stesso sito può essere servito da server host diversi, e l'integrità dei file è verificabile senza fidarsi del server. Un server host non ha bisogno di memorizzare alcun file localmente. Li recupera on demand da Blossom usando gli hash nel manifesto. Questo significa che l'autore controlla ciò che viene servito, il server Blossom memorizza i file grezzi, e il server host si limita a collegare i due. Ciascuno di questi tre componenti può essere sostituito indipendentemente.

Le implementazioni esistenti includono [nsite](https://github.com/lez/nsite), il server host che risolve i manifesti e serve i file, e [nsite-manager](https://github.com/hzrd149/nsite-manager), una UI per costruire e pubblicare i manifesti. La specifica ha aggiunto anche un tag `source` per collegare il repository del codice sorgente del sito, e l'aggiornamento del README unito separatamente nella [PR #2286](https://github.com/nostr-protocol/nips/pull/2286) ha registrato sia il kind `15128` sia il `35128` nell'indice dei kind NIP.

## NIP Deep Dive: NIP-62 (Request to Vanish)

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md) definisce kind `62` come una richiesta ai relay di cancellare tutti gli event della pubkey richiedente. La [specifica](https://github.com/nostr-protocol/nips/blob/master/62.md) ha una motivazione legale: nelle giurisdizioni con leggi sul diritto all'oblio, avere una richiesta di cancellazione standardizzata e firmata dà agli operatori relay un segnale chiaro su cui agire.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

La specifica separa le richieste vanish mirate da quelle globali. Una richiesta mirata include tag `relay` specifici che identificano i relay che devono agire. Una richiesta globale usa la stringa letterale `ALL_RELAYS` come valore del tag relay, chiedendo a ogni relay che vede l'event di cancellare tutti gli event di quella pubkey. I relay che rispettano la richiesta devono anche assicurarsi che gli event cancellati non possano essere ripubblicati di nuovo nel relay, rendendo la cancellazione persistente.

NIP-62 va oltre [NIP-09](/it/topics/nip-09/) (Event Deletion) sia per ambito che per intento. NIP-09 permette di cancellare singoli event, e i relay MAY rispettarlo. NIP-62 chiede la cancellazione di tutto, e la specifica dice che i relay MUST rispettare la richiesta se il loro URL è taggato. Chiede anche ai relay di cancellare gli event [NIP-59](/it/topics/nip-59/) (Gift Wrap) che contengono un p-tag verso la pubkey richiedente, il che significa che i DM in arrivo vengono ripuliti insieme agli event dell'utente. Pubblicare una cancellazione NIP-09 contro una richiesta vanish NIP-62 non ha effetto: una volta che fai vanish, non puoi annullare il vanish cancellando la richiesta di vanish.

Questa settimana, [Amethyst v1.07.0](#amethyst-distribuisce-note-fissate-gestione-relay-e-request-to-vanish) ha distribuito il supporto client-side a NIP-62, permettendo agli utenti di avviare richieste vanish dall'app. Sul lato relay, [rust-nostr](https://github.com/rust-nostr/nostr) ha quattro PR aperte che aggiungono il supporto NIP-62 nei backend memory, LMDB, SQLite, e database test ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)). Questo mette il lavoro di supporto lato client e lato relay nella stessa settimana.

Il design del protocollo introduce una tensione pratica. La proposta di valore di Nostr include la resistenza alla censura, cioè i relay non dovrebbero essere in grado di impedire la pubblicazione. NIP-62 introduce un caso in cui un relay MUST impedire la ripubblicazione da una specifica pubkey. Le due proprietà convivono perché la richiesta è auto-diretta: chiedi la cancellazione dei tuoi event, non di quelli di qualcun altro. La proprietà di resistenza alla censura rimane intatta per tutti tranne che per la persona che ha scelto esplicitamente di uscirne.

---

Questo è tutto per questa settimana. Stai costruendo qualcosa o hai notizie da condividere? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattaci tramite DM [NIP-17](/it/topics/nip-17/) (Private Direct Messages)</a> o trovaci su Nostr.
