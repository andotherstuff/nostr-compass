---
title: 'Nostr Compass #15'
date: 2026-03-25
translationOf: /en/newsletters/2026-03-25-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [Primal Android](https://github.com/PrimalHQ/primal-android-app) fa seguito al suo rilascio wallet 3.0 con [Follow Pack, arricchimento zap e deep link `primalconnect://`](#primal-aggiunge-follow-pack-arricchimento-zap-e-deep-link). [BigBrotr](https://github.com/BigBrotr/bigbrotr) pubblica un'[analisi delle nsec esposte](#bigbrotr-mappa-le-chiavi-private-esposte-nella-rete-relay) scansionando 41 milioni di event su 1.085 relay, trovando 16.599 chiavi private valide, mentre [npub.world](https://npub.world) integra gli avvisi di esposizione nelle pagine profilo la stessa settimana. Martti Malmi lancia [nostr-vpn](#nostr-vpn-si-lancia-come-alternativa-a-tailscale), un'alternativa a Tailscale che segnala tramite relay Nostr e crea tunnel WireGuard, distribuendo 11 rilasci in sette giorni. Il team [Vector](https://github.com/VectorPrivacy/Vector) [rilascia in open-source DOOM P2P](#doom-open-source-gira-peer-to-peer-su-nostr) su Nostr, [FIPS](https://github.com/jmcorgan/fips) distribuisce la [v0.2.0](#fips-v020-distribuisce-trasporto-tor-build-riproducibili-e-esempi-sidecar), e [Nostrability Schemata](https://github.com/nostrability/schemata) si espande a [sei linguaggi](#nostrability-schemata-diventa-multilingue) in una settimana.

## Notizie

### Primal aggiunge Follow Pack, arricchimento zap e deep link

[Come da copertura della 3.0.7 della settimana scorsa](/it/newsletters/2026-03-18-newsletter/), [Primal Android](https://github.com/PrimalHQ/primal-android-app) ha dedicato questa settimana al lavoro post-rilascio su onboarding, UX del composer e contesto wallet. L'onboarding ridisegnato introduce i Follow Pack ([PR #949](https://github.com/PrimalHQ/primal-android-app/pull/949)), un pulsante GIF nativo si unisce al composer delle note, un servizio di arricchimento zap ([PR #979](https://github.com/PrimalHQ/primal-android-app/pull/979)) annota le transazioni wallet con il contesto zap, e un protocollo di deep-linking `primalconnect://` ([PR #969](https://github.com/PrimalHQ/primal-android-app/pull/969)) abilita la navigazione cross-app.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) sta distribuendo lo stesso lavoro tramite TestFlight in parallelo, con lo switch wallet ([PR #191](https://github.com/PrimalHQ/primal-ios-app/pull/191)), l'implementazione dei sondaggi e il refactoring dell'onboarding che arrivano nella stessa finestra.

### BigBrotr mappa le chiavi private esposte nella rete relay

[BigBrotr](https://github.com/BigBrotr/bigbrotr), la piattaforma di analisi relay Nostr, ha pubblicato un'[analisi dettagliata delle chiavi private esposte](https://bigbrotr.com/blog/exposed-nsec-analysis/) nella rete relay. Lo studio ha scansionato 41 milioni di event da 1.085 relay, cercando stringhe nsec valide incorporate nel contenuto degli event, e ha trovato 16.599 chiavi private valide. Quel numero sembra allarmante finché non si filtra un bot chiamato "Mr.nsec" che rappresenta il 92% delle corrispondenze. Dopo aver rimosso il traffico bot, solo 38 account reali con più di 21.000 follower combinati avevano chiavi esposte, e nessuno mostrava segni di consapevolezza che le proprie chiavi fossero pubbliche.

Il team ha costruito un nsec-leak-checker come servizio [NIP-90](/it/topics/nip-90/) (Data Vending Machine), permettendo agli utenti di verificare se la loro chiave privata appare ovunque nel dataset scansionato senza rivelare la chiave al verificatore. [npub.world](https://npub.world) ha integrato i dati di esposizione la stessa settimana, mostrando banner di avviso sulle pagine profilo dove sono state rilevate chiavi esposte. La combinazione dà alla rete sia un'interfaccia programmatica per DVM e agenti sia un avviso leggibile per gli utenti comuni. Il dataset sottostante alimenta anche [BigBrotr v6.4.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.4.0), che aggiunge viste materializzate per event sostituibili e indirizzabili e una correzione del timeout di inattività del sincronizzatore.

### Nostr VPN si lancia come alternativa a Tailscale

Martti Malmi (mmalmi), creatore di Iris, ha costruito e distribuito [nostr-vpn](https://github.com/mmalmi/nostr-vpn), una VPN peer-to-peer che usa relay Nostr per la segnalazione e WireGuard (tramite boringtun) per tunnel cifrati. La motivazione era diretta: "Mi sono irritato che Tailscale richieda account di terze parti, quindi ho creato Nostr VPN." Lo strumento crea reti mesh tra dispositivi usando keypair Nostr come identità, senza server di coordinamento centrale.

Il progetto ha distribuito 11 rilasci in sette giorni, dalla [v0.2.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.2) alla [v0.2.13](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.13). Quello sprint ha aggiunto il supporto Windows, il pairing LAN per la scoperta nella rete locale, e un sidecar Android per dispositivi mobili. L'architettura è semplice: due dispositivi si scambiano metadati di connessione tramite relay Nostr, poi stabiliscono un tunnel WireGuard diretto. Nostr gestisce la scoperta e la segnalazione per l'attraversamento NAT. WireGuard gestisce il traffico effettivo. L'identità è un keypair Nostr.

Malmi ha anche continuato a sviluppare [nostr-double-ratchet](https://github.com/mmalmi/nostr-double-ratchet), una libreria per canali di messaggistica sicura in stile Signal, distribuendo sei rilasci dalla [v0.0.86](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.86) alla [v0.0.93](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.93) durante la stessa settimana.

### DOOM open-source gira peer-to-peer su Nostr

Il team [Vector](https://github.com/VectorPrivacy/Vector) ha rilasciato in open-source un'implementazione multiplayer peer-to-peer di DOOM che usa Nostr per la scoperta dei peer, [Marmot](/it/topics/marmot/) per la cifratura end-to-end, e [Iroh](https://github.com/n0-computer/iroh), la libreria di networking QUIC di n0, per il trasporto gossip. Il gioco viene distribuito come file WebXDC da 4,2 MB che può essere inviato all'interno di messaggi chat, senza richiedere server per ospitare o coordinare una partita.

L'approccio tecnico sostituisce il netcode lockstep originale del 1993 con un modello di sincronizzazione ibrido in tempo reale. I giocatori si scoprono a vicenda tramite query ai relay Nostr, negoziano le sessioni attraverso canali cifrati con Marmot, poi passano al livello gossip QUIC di Iroh per il traffico di gioco a bassa latenza. Lo stack usa Nostr per la scoperta, Marmot per la cifratura, e Iroh per il trasporto.

Vector ha anche distribuito hardening di sicurezza questa settimana. Il rilascio aggiunge un vault di chiavi con protezione della memoria con protezioni anti-debug e zeroize per il materiale chiave sensibile, blocco utenti con filtraggio completo di DM e messaggi di gruppo, e correzioni del canale realtime WebXDC per le Mini App.

### FIPS v0.2.0 distribuisce trasporto Tor, build riproducibili e esempi sidecar

[FIPS](https://github.com/jmcorgan/fips), il Free Internetworking Peering System e progetto di networking mesh adiacente a Nostr, ha distribuito la [v0.2.0](https://github.com/jmcorgan/fips/releases/tag/v0.2.0-rel). Il rilascio aggiunge supporto al trasporto Tor per link mesh anonimizzati, build riproducibili, un esempio sidecar che si connette attraverso un relay Nostr, e pubblicazione dei rilasci su Nostr nel workflow del pacchetto OpenWrt. Il rilascio corregge anche i picchi di jitter post-rekey causati da frame della finestra di drain. Il formato wire è cambiato dalla v0.1.0, quindi i nodi v0.1.0 esistenti non possono interoperare con la v0.2.0 senza aggiornamento.

### Nostrability Schemata diventa multilingue

Il progetto [Nostrability Schemata](https://github.com/nostrability/schemata), che mantiene definizioni JSON Schema per la validazione dei kind di event Nostr, si è espanso dal solo JavaScript a sei linguaggi in una settimana. Nuovi pacchetti sono stati distribuiti per Rust, Go, Dart, Swift e Python, ognuno fornendo sia un pacchetto dati che un validatore. La [v0.2.6](https://github.com/nostrability/schemata/releases/tag/v0.2.6) ha anche aggiunto 17 nuovi schemi di kind event.

Il [tracker di interoperabilità Nostrability](https://nostrability.github.io/nostrability/) ha ricevuto una revisione parallela. Una nuova scheda What's New pubblica aggiornamenti sia tramite un feed Atom che un event Nostr, il filtraggio per categoria app permette ai visitatori di esplorare tipi specifici di client, e il tracker ora rileva automaticamente i linguaggi di programmazione dai metadati dei repository GitHub. Nostrability ha anche il suo npub ora, rendendo il progetto stesso scopribile attraverso il protocollo che documenta. Per gli autori di librerie che lavorano su più linguaggi, i pacchetti schema multi-linguaggio significano che le stesse definizioni di kind event sono disponibili come import nativi invece di richiedere ad ogni progetto di mantenere la propria copia dello schema.

## Rilasci

### Amethyst v1.06.0 e v1.06.1

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android mantenuto da vitorpamplona, ha distribuito la [v1.06.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.0) e la [v1.06.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.1) il 23 marzo. La funzionalità principale è il supporto ai sondaggi usando dati [NIP-85](/it/topics/nip-85/) (Trusted Assertions) per il voto ponderato, con card ridisegnate per sondaggi e sondaggi zap. Il nuovo rendering dà sia ai sondaggi standard che ai sondaggi con peso zap un layout visivo più pulito. La v1.06.1 segue con correzioni di crash per modifiche concorrenti che risolvono regressioni di stabilità introdotte nel percorso di rendering dei sondaggi.

### Amber v5.0.0 e v5.0.1

[Amber](https://github.com/greenart7c3/Amber), l'app signer [NIP-55](/it/topics/nip-55/) (Android Signer Application), ha promosso il suo recente lavoro pre-release 4.1.x in stabile con la [v5.0.0](https://github.com/greenart7c3/Amber/releases/tag/v5.0.0) il 18 marzo. Quel rilascio stabile porta le modifiche di relay-auth [NIP-42](/it/topics/nip-42/), Tor integrato, permessi specifici per tipo di contenuto e storage PIN cifrato coperte la settimana scorsa. La [v5.0.1](https://github.com/greenart7c3/Amber/releases/tag/v5.0.1) rimuove poi il permesso internet dal build flavor offline, in modo che quel build non possa più effettuare richieste di rete a livello di permessi Android.

### Mostro v0.17.0 e Mostro Mobile v1.2.2

[Mostro](https://github.com/MostroP2P/mostro), lo scambio Bitcoin peer-to-peer costruito su Nostr, ha distribuito la [v0.17.0](https://github.com/MostroP2P/mostro/releases/tag/v0.17.0) il 18 marzo. Il rilascio server continua il lavoro sulle dispute e le valutazioni dal ciclo v0.16.x, aggiungendo dati di reputazione commerciale più completi per acquirenti e venditori come event Nostr. [Mostro Mobile](https://github.com/MostroP2P/mobile), il client Flutter, ha seguito con la [v1.2.2](https://github.com/MostroP2P/mobile/releases/tag/v1.2.2) il 23 marzo, mantenendo l'interfaccia mobile sincronizzata con le ultime modifiche al protocollo.

### Shosho v0.14.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), l'app di live streaming Nostr, ha distribuito la [v0.14.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.14.0) il 19 marzo con il lancio di Shosho Shop. Il rilascio aggiunge una scheda Shop sui profili, Shop in Esplora, e un pulsante In-Live Shop su live e clip. Le note di rilascio dicono che i "prodotti Nostr" esistenti appaiono automaticamente e gli acquirenti cliccano per accedere alla pagina Plebeian Market del venditore per l'acquisto. Le note di rilascio di Shosho non identificano il kind di event degli annunci, quindi non è ancora possibile confermare se Shosho Shop legge gli stessi annunci classificati [NIP-99](/it/topics/nip-99/) che [Shopstr](https://github.com/shopstr-eng/shopstr) supporta esplicitamente nel suo README.

### Applesauce v5.2.0

[Applesauce](https://github.com/hzrd149/applesauce), la collezione di pacchetti helper di hzrd149 per costruire applicazioni Nostr, ha distribuito la [v5.2.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core@5.2.0) il 22 marzo. Il rilascio copre sei pacchetti. Il pacchetto SQLite corregge una collisione di vincolo UNIQUE sui tag degli event che causava inserimenti duplicati. Il pacchetto signers aggiunge `AndroidNativeSigner`, che avvolge l'interfaccia signer nativa Android [NIP-55](/it/topics/nip-55/) in modo che le app basate su web-view possano usare la firma hardware-backed senza codice bridge personalizzato. Il pacchetto relay aggiunge un campo `challenge` agli oggetti di stato relay e pool, tracciando lo stato auth [NIP-42](/it/topics/nip-42/) in modo che le app possano rilevare quando un relay sta richiedendo l'autenticazione e rispondere programmaticamente. Il pacchetto core acquisisce i metodi `isEventPointerSame` e `isAddressPointerSame` per la deduplicazione dei riferimenti event, e il pacchetto common aggiunge `user.blossomServers$` per risolvere i server media Blossom di un utente. Applesauce alimenta noStrudel, Satellite e diversi altri client web, quindi queste correzioni si propagano attraverso il livello client web.

### Wisp distribuisce 16 rilasci in una settimana

[Wisp](https://github.com/barrydeen/wisp), il client Nostr Android, ha distribuito 16 rilasci dalla [v0.9.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.9.3-beta) alla [v0.13.1-beta](https://github.com/barrydeen/wisp/releases/tag/v0.13.1-beta) questa settimana. Le aggiunte di funzionalità includono supporto multi-account, una modalità notifiche zen per interruzioni ridotte, bozze e post programmati, filtri di sicurezza dei contenuti e una nuova icona fiamma.

### Manent v1.2.0

[Manent](https://github.com/dtonon/manent), l'app di note private cifrate e storage file, ha distribuito la [v1.2.0](https://github.com/dtonon/manent/releases/tag/v1.2.0) il 20 marzo. Il rilascio aggiunge la cattura dalla fotocamera direttamente dall'app, il ridimensionamento delle immagini prima dell'upload per ridurre i costi di storage, e pinch-to-zoom per esaminare le immagini archiviate. Manent archivia note e file cifrati sui relay Nostr usando il keypair dell'utente, rendendo il telefono o l'app desktop un thin client che può ricostruire il suo stato completo dai dati dei relay.

### diVine 1.0.7

[diVine](https://github.com/divinevideo/divine-mobile), il client di video brevi, ha distribuito la [1.0.7](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.7) il 21 marzo con un watchdog per la riproduzione video che riprende automaticamente i video bloccati. Dopo l'infrastruttura di test E2E e il caricamento diretto MP4 nella [v1.0.6](/en/newsletters/2026-03-11-newsletter/#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import), questo rilascio mira al percorso di errore di riproduzione rimanente: video che si fermano a metà stream senza generare un errore.

### Alby Extension v3.14.2

[Alby Extension](https://github.com/getAlby/lightning-browser-extension), l'estensione browser [NIP-07](/it/topics/nip-07/) (Browser Extension Signer), ha distribuito la [v3.14.2](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.2) il 18 marzo con la visualizzazione QR code dell'indirizzo Lightning e supporto alla firma Schnorr. L'aggiunta di Schnorr allinea l'estensione browser con lo schema di firma secp256k1 che Nostr usa nativamente.

### NoorNote da v0.6.5 a v0.6.11

[NoorNote](https://github.com/77elements/noornote), l'app per prendere appunti, ha distribuito sette rilasci dalla [v0.6.5](https://github.com/77elements/noornote/releases/tag/v0.6.5) alla [v0.6.11](https://github.com/77elements/noornote/releases/tag/v0.6.11). L'aggiunta principale sono i Follow Pack: bundle curati di account che gli utenti possono esplorare e sottoscrivere in blocco, simili alle Liste Twitter ma pensati per l'onboarding. Gli utenti possono creare, modificare e condividere Follow Pack con titoli, descrizioni e immagini di copertina personalizzati. La serie aggiorna anche la libreria Nostr sottostante da NDK v2 a v3, che porta una gestione migliorata delle connessioni relay e delle sottoscrizioni. Le note con immagini e un'esperienza di connessione relay ridisegnata completano il ciclo.

### nak v0.19.1 e v0.19.2

[nak](https://github.com/fiatjaf/nak), il toolkit Nostr a riga di comando di fiatjaf per interagire con i relay, codificare e decodificare identificatori [NIP-19](/it/topics/nip-19/) (Bech32-Encoded Entities), firmare event e interrogare dati dei relay, ha distribuito la [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1) e la [v0.19.2](https://github.com/fiatjaf/nak/releases/tag/v0.19.2) il 17 e 20 marzo. Le due point release seguono l'aggiunta della UI group-forum [v0.19.0](/it/newsletters/2026-03-18-newsletter/) dalla settimana scorsa.

### Calendar by Form* v0.2.1

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), l'app calendario decentralizzata costruita su [NIP-52](/it/topics/nip-52/) (Calendar Events), ha distribuito la [v0.2.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.1) il 20 marzo. Il rilascio corregge un problema nel template delle notifiche che influiva sui promemoria degli eventi. Calendar archivia gli event come kind 31922 (basati su data) e kind 31923 (basati su orario) di Nostr, permettendo a qualsiasi client Nostr di renderizzare i dati calendario se sceglie di supportare quei kind. L'app è costruita dal team Formstr, che mantiene anche Formstr (moduli decentralizzati) e Pollerama (sondaggi).

### NYM da v3.50 a v3.53

[NYM](https://github.com/Spl0itable/NYM), il client di chat effimero leggero collegato a Bitchat, ha distribuito 28 rilasci dalla v3.50 alla v3.53 (le versioni patch incrementano rapidamente). La funzionalità più notevole è Nymbot, un chat bot integrato che risponde alle menzioni `@nymbot` nei canali e fornisce funzioni di stato e gestione dei relay. Una "hardcore mode" genera un keypair fresco per ogni messaggio inviato, rendendo i thread di conversazione non collegabili a livello di identità. Il compromesso è chiaro: si perde l'identità persistente ma si guadagna l'anonimato per messaggio. Il livello proxy relay ha anche ricevuto lavoro, con worker proxy relay sharded per migliore connettività, supporto canali geohash, e tolleranza al clock skew per nodi con orologi di sistema imprecisi.

## Aggiornamenti Progetti

### Ditto aggiunge bridge Bluesky e integrazione Wikipedia

[Ditto](https://github.com/soapbox-pub/ditto), il client social Nostr personalizzabile del team Soapbox, ha registrato oltre 300 commit questa settimana su tre percorsi di funzionalità distinti. Il primo è un bridge Bluesky (19 commit) che renderizza i post Bluesky inline come thread completi in stile feed, aggiunge navigazione sidebar a una pagina di scoperta Bluesky alimentata dal feed ufficiale Discover (whats-hot), e collega pulsanti di azione per commentare, condividere, reagire e copiare link. Quando un utente risponde a un post Bluesky dall'interno di Ditto, la modale di composizione mostra un avviso che nota la natura cross-protocollo dell'interazione. Le reazioni kind 17 [NIP-73](/it/topics/nip-73/) (External Content IDs) alimentano il modello cross-protocollo: un utente Nostr reagisce a un post Bluesky, e la reazione viene archiviata come un event Nostr standard che referenzia l'identificatore di contenuto esterno. Questo è lo stesso pattern NIP-73 che potrebbe collegare reazioni a qualsiasi contenuto esterno, dai post Bluesky ai video YouTube alle pagine web.

Il secondo percorso è un'integrazione Wikipedia (9 commit). Ditto ora renderizza contenuti ricchi di articoli Wikipedia sulle pagine di dettaglio invece di anteprime link generiche, aggiunge autocompletamento nella ricerca con miniature degli articoli, e fornisce una pagina `/wikipedia` che attinge contenuti in evidenza dall'API Wikipedia. I risultati di Wikipedia e Archive.org appaiono anche nel dropdown di autocompletamento della ricerca generale. Il terzo percorso è il supporto piattaforma iOS tramite Capacitor, con script di build remoto e configurazione piattaforma che arrivano insieme a una revisione della UI (55 commit) che sostituisce gli header con backdrop-blur con un nuovo design di navigazione basato su arco su ogni pagina dell'app. I 314 commit muovono Ditto da un client solo-Nostr verso un aggregatore multi-protocollo che tratta Bluesky e Wikipedia come sorgenti di contenuto di prima classe accanto al feed Nostr.

### Pika costruisce una pipeline CI forge NIP-34

[Pika](https://github.com/sledtools/pika), l'app di messaggistica cifrata basata su Marmot, ha unito 33 PR questa settimana focalizzate su un forge [NIP-34](/it/topics/nip-34/) self-hosted con CI pre-merge. Il forge è un livello di hosting git che riceve patch come event NIP-34, esegue controlli CI prima del merge, e riporta lo stato strutturato tramite event Nostr. La [PR #701](https://github.com/sledtools/pika/pull/701) aggiunge CI pre-merge e nightly basata su lane, dove ogni percorso di codice (Rust, TypeScript, build Apple) gira nella propria lane con stato pass/fail indipendente. La [PR #715](https://github.com/sledtools/pika/pull/715) riduce gli agenti CI gestiti a container Incus OpenClaw per l'isolamento, e la [PR #733](https://github.com/sledtools/pika/pull/733) aggiunge una CLI `ph forge` per interagire con il forge ospitato dalla riga di comando. PR di supporto gestiscono i permessi di scrittura al repo per i merge ([PR #736](https://github.com/sledtools/pika/pull/736)), metadati CI strutturati con badge di stato live ([PR #722](https://github.com/sledtools/pika/pull/722)), split delle build Apple nightly ([PR #738](https://github.com/sledtools/pika/pull/738)), e correzioni di auth e ricerca branch del forge ([PR #734](https://github.com/sledtools/pika/pull/734)). Questo è uno dei primi sistemi CI/CD funzionanti costruiti sopra gli event git NIP-34, spostando l'hosting del codice sorgente basato su Nostr oltre lo scambio base di patch verso il workflow di merge-and-test che gli sviluppatori si aspettano da GitHub o GitLab.

### Nostria aggiunge comunità, snippet di codice e gestione event vocali

[Nostria](https://github.com/nostria-app/nostria), il client Nostr cross-platform mantenuto da sondreb, ha dedicato questa settimana a estendere la superficie app oltre il filtraggio Web of Trust coperto nel #14. L'aggiunta principale è un'implementazione completa di [NIP-72](/it/topics/nip-72/) (Moderated Communities) con creazione comunità, configurazione moderatori e relay, tracciamento approvazione post con anteprime immagini, e una pagina comunità dedicata con tab Post e Moderatori.

Lo stesso arco di lavoro aggiunge anche rendering e editing di snippet di codice con un editor con evidenziazione della sintassi, supporto risposte a event vocali per conversazioni audio, impostazioni relay chat per messaggi diretti, condivisione canali tramite la Web Share API, un sistema di docking toolbar per il media player, registrazione in-app per l'ultimo servizio Web of Trust di Brainstorm, flussi di invio e ricezione denaro nei DM usando NWC e fatture BOLT-11, gestione GIF nativa Nostr, e un percorso di importazione RSS più robusto per i musicisti che può raccogliere gli split Lightning esistenti dai feed podcast.

### Iterazione rapida nostr-vpn

Oltre al [lancio iniziale](#nostr-vpn-si-lancia-come-alternativa-a-tailscale), il log dei commit di [nostr-vpn](https://github.com/mmalmi/nostr-vpn) rivela i problemi specifici incontrati durante il deployment reale. La [v0.2.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.3) fino alla [v0.2.5](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.5) hanno aggiunto lo script di installazione iniziale e la CLI cross-platform. La [v0.2.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.6) e la [v0.2.7](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.7) hanno portato il supporto Windows, che ha richiesto il quoting del percorso UAC per le scritture di configurazione e aggiornamenti di configurazione di proprietà del daemon. La [v0.2.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.8) fino alla [v0.2.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.10) hanno corretto le azioni del servizio GUI Windows, la gestione dei sottoprocessi CLI e la configurazione del servizio machine-scoped. La [v0.2.12](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.12) ha sostituito la scoperta LAN con il pairing LAN a tempo, un flusso avviato dall'utente dove due dispositivi sulla stessa rete locale si accoppiano senza segnalazione relay. Il pattern è da manuale di testing sul campo in fase iniziale: ogni rilascio mira a uno specifico fallimento di deployment, la base utenti è abbastanza piccola per iterare quotidianamente, e lo sviluppatore usa lo strumento personalmente tra i rilasci.

### Build automatizzate Comet

[Comet](https://github.com/nodetec/comet) (precedentemente Captain's Log), lo strumento di scrittura long-form nativo Nostr di Nodetec, ha prodotto oltre 40 build alpha automatizzate questa settimana. Comet è un'app desktop per scrivere e pubblicare articoli NIP-23 (Long-form Content), con storage locale delle bozze, editing markdown e pubblicazione one-click sul set di relay dell'utente. La pipeline di build automatizzata genera un rilascio taggato per ogni commit sul branch main, il che rende il conteggio grezzo dei rilasci fuorviante come misura della velocità delle funzionalità. Ciò che le 40 build mostrano è che l'app è in sviluppo attivo quotidiano, con ogni commit testato, pacchettizzato e reso disponibile per il download in pochi minuti.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips) nella finestra 17-24 marzo:

Nessun merge NIP è arrivato tra il 18 e il 24 marzo.

**PR Aperte e Discussioni aggiornate nella finestra:**

- **NIP-AA: Agenti Autonomi su Nostr** ([PR #2259](https://github.com/nostr-protocol/nips/pull/2259)): Propone convenzioni per agenti autonomi che operano sulla rete Nostr. La PR definisce come gli agenti si identificano, scoprono servizi e si coordinano con altri agenti e umani attraverso event Nostr.

- **[NIP-50](/it/topics/nip-50/) (Search): Estensioni di ordinamento** ([PR #2283](https://github.com/nostr-protocol/nips/pull/2283)): Aggiunge parametri di ordinamento alle query di ricerca NIP-50, inclusi top, hot, zaps e new. Questo permetterebbe ai client di richiedere risultati classificati dai relay che supportano la ricerca full-text invece di ordinare lato client.

- **NIP-A5: Programmi WASM** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Propone una convenzione per pubblicare e scoprire programmi WebAssembly su Nostr. I binari WASM potrebbero essere distribuiti come event Nostr, con i relay che servono come livello di scoperta per codice eseguibile portabile.

- **NIP-CF: Combine Forces napps interoperabili** ([PR #2277](https://github.com/nostr-protocol/nips/pull/2277)): Definisce una convenzione per applicazioni Nostr interoperabili ("napps") che possono comporre funzionalità tra diversi client e servizi.

- **NIP Snapshots** ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279)): Propone un meccanismo per snapshot dello stato dei relay, per la sincronizzazione e il backup dei relay.

- **NIP Checkpoints** ([PR #2278](https://github.com/nostr-protocol/nips/pull/2278)): Propone event checkpoint per segnare lo stato valido noto dei relay, complementando la proposta snapshots.

- **[NIP-58](/it/topics/nip-58/) (Badges): Refactoring Badge Sets** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Ristruttura come le collezioni di badge sono organizzate e referenziate.

- **[NIP-11](/it/topics/nip-11/) (Relay Information Document): Estensioni** ([PR #2280](https://github.com/nostr-protocol/nips/pull/2280)): Aggiunge campi aggiuntivi al documento informativo del relay per metadati relay leggibili dalle macchine più ricchi.

## Cinque Anni di Marzo di Nostr

[La newsletter del mese scorso](/it/newsletters/2026-03-04-newsletter/#cinque-anni-di-febbraio-di-nostr) ha coperto come i febbrai di Nostr sono progrediti dalla riscrittura di NIP-01 (Basic Protocol Flow) attraverso l'ondata Damus sull'App Store fino alle reti mesh e le proposte per agenti. Questa retrospettiva traccia cosa è successo ogni marzo dal 2021 al 2026.

### Marzo 2021: Due Commit

Quattro mesi dopo la sua nascita, il marzo di Nostr ha prodotto esattamente due commit al repository del protocollo, entrambi il 4 marzo. fiatjaf [ha aggiunto link alle istanze nostwitter](https://github.com/nostr-protocol/nostr/commit/dcd8cc3), indirizzando i primi visitatori a deployment funzionanti, e [ha aggiunto kind alla definizione base dei filtri](https://github.com/nostr-protocol/nostr/commit/54dfb46). Quel secondo commit è rivelatore: nel marzo 2021, non si potevano ancora filtrare gli event Nostr per kind. Il protocollo era così primitivo. Due o tre relay servivano la rete. Il gruppo Telegram era l'unico canale di coordinamento. Il repository NIPs non esisteva ancora; le proposte di protocollo vivevano come file nel repo principale nostr. fiatjaf era l'unico committer quel mese. L'intero output del marzo 2021 di quello che sarebbe diventato un protocollo che supporta VPN, giochi multiplayer e networking mesh cinque anni dopo entra in una singola diff git.

### Marzo 2022: Costruzione Pre-Damus

Il repository principale del protocollo ha ricevuto zero commit nel marzo 2022. Lo sviluppo si era spostato interamente nei repository degli strumenti. [Branle](https://github.com/fiatjaf/branle), il client web Vue.js di fiatjaf e all'epoca l'interfaccia Nostr principale, ha ricevuto 5 commit incluso il supporto al deployment Docker e correzioni alla visualizzazione del nome di verifica [NIP-05](/it/topics/nip-05/) (DNS-Based Verification) che rimuovevano il prefisso `_@` dai badge di verifica. [more-speech](https://github.com/unclebob/more-speech) di Robert C. Martin, il client desktop Clojure, ha registrato 13 o più commit aggiungendo threading, navigazione da tastiera e una finestra di editing. L'autore di software più famoso che costruiva attivamente su Nostr quel mese non era uno sviluppatore crypto ma la persona il cui "Clean Code" ha venduto milioni di copie, che scriveva un client Nostr in Clojure, una scelta di linguaggio che dice tutto sulla comunità iniziale: erano programmatori con opinioni forti che costruivano per sé stessi.

La rete relay si era espansa a circa 15 relay con una base utenti attiva nell'ordine delle centinaia. Damus non esisteva ancora e non sarebbe stato creato fino ad aprile 2022. Nemmeno Nostream era apparso. Il lavoro del mese era infrastruttura: rendere gli strumenti esistenti più affidabili per la piccola comunità che li usava già quotidianamente.

### Marzo 2023: Infrastruttura Post-Esplosione

Un mese dopo l'ondata Damus sull'App Store e il superamento delle 300.000 chiavi pubbliche, il marzo 2023 riguardava l'assorbimento della crescita. Il [repository NIPs](https://github.com/nostr-protocol/nips) ha unito 28 pull request, il secondo conteggio mensile più alto nella storia del protocollo. [NIP-51](/it/topics/nip-51/) (Lists) è stato unito, dando ai client collezioni strutturate di follow, mute e segnalibri. [NIP-39](/it/topics/nip-39/) (External Identities in Profiles) è arrivato, NIP-78 (Application-Specific Data) ha fornito un kind di storage generale per le app che necessitavano di stato privato, e una riscrittura di [NIP-57](/it/topics/nip-57/) (Lightning Zaps) ([PR #392](https://github.com/nostr-protocol/nips/pull/392)) ha consolidato il flusso zap e chiarito la terminologia. La PR più discussa del mese era una proposta alternativa di gestione delle menzioni ([PR #381](https://github.com/nostr-protocol/nips/pull/381)) con oltre 50 commenti.

Il nuovo progetto più importante è stato [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit), la libreria TypeScript per connessioni relay, firma event, caching e gestione sottoscrizioni. pablof7z ha fatto il [commit iniziale](https://github.com/nostr-dev-kit/ndk/commit/09e5e03) il 16 marzo 2023, poi l'ha riscritto da zero 11 giorni dopo il 27 marzo ("praticamente un altro commit iniziale"), e aveva il supporto LNURL e zap funzionante entro il 31 marzo. NDK è passato dal nulla alla capacità zap in 15 giorni. Cinque giorni dopo la creazione di NDK, il 21 marzo, il team Alby ha creato [NWC](https://github.com/getAlby/nostr-wallet-connect) (Nostr Wallet Connect), l'implementazione di riferimento di [NIP-47](/it/topics/nip-47/) che connetteva i wallet Lightning alle applicazioni Nostr. I due progetti che avrebbero sostenuto i successivi tre anni di sviluppo Nostr basato sul web sono nati nella stessa finestra di 30 giorni. OpenSats non aveva ancora lanciato il suo fondo Nostr; la prima ondata non sarebbe arrivata fino a [luglio 2023](https://opensats.org/blog/nostr-grants-july-2023), quattro mesi dopo la creazione di NDK.

Altre creazioni notevoli di quel mese includevano NostrGit, NostrChat, un progetto nostr-signing-device di LNbits, e nostrmo. [Gossip](https://github.com/mikedilger/gossip), il client desktop Rust focalizzato sulla selezione intelligente dei relay, ha distribuito tre rilasci. Il protocollo era in modalità costruzione, e gli strumenti creati nel marzo 2023 sono ancora in uso tre anni dopo.

### Marzo 2024: Maturazione del Protocollo

Il marzo 2024 riguardava l'hardening del protocollo per l'uso a lungo termine. Il repository NIPs ha unito 12 pull request. La più significativa è stata [NIP-34](/it/topics/nip-34/) (Git Stuff), [PR #997](https://github.com/nostr-protocol/nips/pull/997), che è stata unita il 5 marzo dopo oltre 130 commenti e 44 giorni di revisione. Il thread di discussione è una capsula del tempo della comunità che dibatteva come costruire un GitHub decentralizzato. jb55 ha tracciato paralleli con `git send-email`, Giszmo ha proposto di usare gli hash dei root commit per la scoperta cross-fork ("qualcosa che GitHub non fa e che noi potremmo"), mikedilger ha suggerito l'autenticazione con event firmati [NIP-98](/it/topics/nip-98/) (HTTP Auth) invece delle chiavi SSH, e fiatjaf ha liquidato bruscamente la necessità di generalità nel controllo versione: "non per ogni sistema di controllo versione, solo per git. Nessuno usa gli altri." Entro poche ore dall'apertura della PR, fiatjaf aveva già convertito nak, go-nostr e gitstr per accettare patch su Nostr. DanConwayDev, il cui ngit era già un grantee OpenSats, era tra i contributori più attivi alla discussione. È stato unito anche un campo bot per i metadati dei profili, dando ai client un modo leggibile dalle macchine per distinguere gli account automatizzati da quelli umani.

[Amethyst](https://github.com/vitorpamplona/amethyst) ha distribuito la v0.85.0 con supporto event git, articoli wiki, rendering di dati medici e editing di contenuti in un singolo rilascio. [Mostro](https://github.com/MostroP2P/mostro) ha raggiunto la v0.10.0. [Nosflare](https://github.com/Spl0itable/nosflare), un relay Nostr serverless in esecuzione su Cloudflare Workers, ha dimostrato che la logica relay poteva girare all'edge. OpenSats ha emesso una [grant di Supporto a Lungo Termine a Bruno Garcia](https://opensats.org/blog/bruno-garcia-receives-lts-grant) per contributi sostenuti al client Amethyst.

### Marzo 2025: Espansione dell'Infrastruttura

Il marzo 2025 ha prodotto 10 NIP uniti. Il titolo principale è stato [NIP-66](/it/topics/nip-66/) (Relay Discovery and Liveness Monitoring), [PR #230](https://github.com/nostr-protocol/nips/pull/230), che è stata unita il 3 marzo dopo un percorso di 25 mesi. dskvr ha proposto per la prima volta il monitoraggio dei relay nel febbraio 2023, gli è stato detto che poteva essere fatto lato client, ha spiegato perché connettersi a migliaia di relay contemporaneamente era impraticabile per i singoli client, ha attraversato sette bozze complete, ha costruito nodi di monitoraggio in otto regioni geografiche (Northeast US, Brasile, US-West, US-East, Australia, India, Corea, Sud Africa), e ha atteso che il tooling relay si mettesse al passo. Quando è stata unita, le implementazioni esistevano già in nostr.watch, relaypag.es, monitorlizard, Snort, noStrudel e Jumble. I dati NIP-66 avrebbero poi alimentato i benchmark outbox di Nostrability [coperti nella Newsletter #12](/it/newsletters/2026-03-04-newsletter/#il-modello-outbox-sotto-la-lente). È stato unito anche NIP-C0 (Code Snippets) ([PR #1852](https://github.com/nostr-protocol/nips/pull/1852), 63 commenti), aggiungendo event kind 1337 per la condivisione di codice sorgente.

I primi server MCP per Nostr sono apparsi questo mese. [nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server) è apparso il 23 marzo e [nwc-mcp-server](https://github.com/getAlby/nwc-mcp-server) il 14 marzo, solo quattro mesi dopo che Anthropic ha annunciato il Model Context Protocol nel novembre 2024. Questi primi bridge hanno preceduto l'SDK completo di [ContextVM](/it/topics/contextvm/) e il lavoro di commercio agenti che è seguito alla fine del 2025 e inizio 2026.

[Gossip](https://github.com/mikedilger/gossip) ha distribuito la v0.14.0. [Coracle](https://github.com/coracle-social/coracle), il client web di hodlbod con gestione feed consapevole dei relay, ha distribuito tre rilasci. OpenSats ha annunciato la sua [decima ondata di grant Nostr](https://opensats.org/blog/10th-wave-of-nostr-grants), continuando la pipeline di finanziamento attiva dalla metà del 2023.

### Marzo 2026: Convergenza

*L'attività di marzo 2026 è tratta dai numeri di Nostr Compass [#12](/it/newsletters/2026-03-04-newsletter/) fino al [#15](#) (questo numero).*

Il marzo 2026 è il mese in cui thread disparati sono convergiti in sistemi funzionanti. Il [Marmot Development Kit](/it/newsletters/2026-03-04-newsletter/#marmot-development-kit-distribuisce-il-primo-rilascio-pubblico) ha distribuito il suo primo rilascio pubblico con media cifrati, binding multi-linguaggio, e una migrazione ChaCha20-Poly1305 che ha richiesto aggiornamenti coordinati tra specifica, Rust e TypeScript. [Shopstr e Milk Market](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces) hanno aggiunto superfici di commercio MCP per acquisti guidati da agenti. [NIP-42](/it/topics/nip-42/) relay auth è arrivato simultaneamente in [Amber](/en/newsletters/2026-03-11-newsletter/#nip-42-relay-auth-across-bunker-signer-and-relay), strfry e OAuth Bunker, chiudendo il cerchio tra software signer, relay e bunker. [Notedeck](/it/newsletters/2026-03-18-newsletter/#notedeck-sposta-la-scoperta-dei-rilasci-su-nostr) ha distribuito aggiornamenti software nativi Nostr usando event di rilascio [NIP-94](/it/topics/nip-94/) (File Metadata).

Questa settimana, [BigBrotr](#bigbrotr-mappa-le-chiavi-private-esposte-nella-rete-relay) ha scansionato l'intera rete relay alla ricerca di chiavi private trapelate e ha pubblicato sia l'analisi che un checker DVM. [Nostr VPN](#nostr-vpn-si-lancia-come-alternativa-a-tailscale) ha dimostrato che il modello di chiavi di Nostr funziona per l'infrastruttura di rete, non solo per i social media. [DOOM](#doom-open-source-gira-peer-to-peer-su-nostr) ha dimostrato che scoperta Nostr, cifratura Marmot e trasporto QUIC possono far girare un gioco multiplayer in tempo reale. [Amber](#amber-v500-e-v501) è passato alla v5.0.0. [Wisp](#wisp-distribuisce-16-rilasci-in-una-settimana) ha distribuito 16 rilasci in sette giorni. Venticinque o più rilasci taggati sono arrivati da progetti importanti in una singola settimana.

Sette NIP sono stati uniti nei primi 24 giorni del mese. Il protocollo ha aggiunto il markup Djot [NIP-54](/it/topics/nip-54/) (Wiki), i limiti di input [NIP-19](/it/topics/nip-19/) (Bech32-Encoded Entities), la logica di query booleana [NIP-91](/it/topics/nip-91/) (AND Operator for Filters), e le asserzioni Web of Trust [NIP-85](/it/topics/nip-85/) (Trusted Assertions). Le proposte aperte spaziavano dagli agenti autonomi (NIP-AA) ai programmi WASM (NIP-A5) alle estensioni di ordinamento per la ricerca [NIP-50](/it/topics/nip-50/).

### Guardando Avanti

Cinque marzi di Nostr tracciano un arco chiaro. Nel 2021, una persona ha fatto due commit a un protocollo che non poteva ancora filtrare event per kind. Entro il 2023, NDK e NWC sono nati a cinque giorni di distanza per assorbire l'esplosione post-Damus. Entro il 2024, un thread di PR da 141 commenti dibatteva come la collaborazione git dovrebbe funzionare su un protocollo sociale. Entro il 2025, una specifica di monitoraggio relay che era stata pazientemente riscritta sette volte in 25 mesi è stata finalmente unita. Nel 2026, qualcuno si è irritato per il fatto che Tailscale richiede un account e ha costruito una VPN usando keypair Nostr, mentre qualcun altro ha distribuito DOOM multiplayer che scopre i peer tramite relay Nostr e cifra il gameplay tramite Marmot. La scansione di BigBrotr di 41 milioni di event su 1.085 relay dà una misura concreta di quanto la rete sia cresciuta. La superficie del protocollo nel marzo 2026 sarebbe stata irriconoscibile per il marzo 2021, ma il modello sottostante, event firmati da chiavi secp256k1 e distribuiti attraverso relay, non è cambiato.

---

Questo è tutto per questa settimana. Stai costruendo qualcosa o hai notizie da condividere? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattaci tramite DM [NIP-17](/it/topics/nip-17/) (Private Direct Messages)</a> o trovaci su Nostr.
