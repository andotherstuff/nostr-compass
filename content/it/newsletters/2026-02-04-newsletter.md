---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** rust-nostr rilascia una importante riprogettazione dell'API con 21 PR che rivedono l'architettura dell'SDK. Nostria 3.0 viene lanciato con navigazione a doppio pannello, gestione liste e una completa revisione dell'UI. Vector aggiunge accelerazione SIMD raggiungendo speedup di 65x-184x e rilascia supporto per il protocollo [Marmot](/it/topics/marmot/) per la messaggistica di gruppo crittografata. Frostr porta la firma a soglia su iOS tramite TestFlight. Damus implementa i suggerimenti relay [NIP-19 (Entità Codificate Bech32)](/it/topics/nip-19/) per la scoperta di contenuti cross-relay. Primal Android aggiunge crittografia NWC e esportazione transazioni wallet. nostr-tools e NDK ricevono miglioramenti di affidabilità. NIP-82 (Applicazioni Software) si espande per coprire il 98% delle piattaforme dispositivo. Il repository NIPs unisce il supporto hold invoice per [NIP-47 (Nostr Wallet Connect)](/it/topics/nip-47/). Nuove proposte di protocollo includono NIP-74 per il podcasting, NIP-DB per database eventi nel browser e una suite TRUSTed Filters per la curation decentralizzata dei contenuti. Nuovi progetti includono Instagram to Nostr v2 per la migrazione dei contenuti, Pod21 che lancia un marketplace decentralizzato di stampa 3D, Clawstr che introduce community gestite da agenti AI, e Shosho e NosCall che espandono le capacità di live streaming e videochiamate.

## Notizie

### rust-nostr Rilascia una Importante Riprogettazione dell'API

L'SDK [rust-nostr](https://github.com/rust-nostr/nostr) ha subito una significativa revisione dell'architettura questa settimana con 21 PR unite che introducono breaking changes attraverso la libreria. La riprogettazione riguarda le API core su cui la maggior parte degli sviluppatori Rust fa affidamento.

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245) riprogetta le API di notifica, mentre [PR #1244](https://github.com/rust-nostr/nostr/pull/1244) sostituisce `RelayNotification::Shutdown` con `RelayStatus::Shutdown` per una gestione dello stato più pulita. Le API del signer ora si allineano con altri pattern dell'SDK tramite [PR #1243](https://github.com/rust-nostr/nostr/pull/1243). I metodi Client e Relay hanno ricevuto una pulizia in [PR #1242](https://github.com/rust-nostr/nostr/pull/1242), e le opzioni client ora usano un builder pattern ([PR #1241](https://github.com/rust-nostr/nostr/pull/1241)).

Le API di invio messaggi sono state riprogettate in [PR #1240](https://github.com/rust-nostr/nostr/pull/1240), l'unsubscription REQ in [PR #1239](https://github.com/rust-nostr/nostr/pull/1239), e la rimozione relay in [PR #1229](https://github.com/rust-nostr/nostr/pull/1229). Una [PR aperta #1246](https://github.com/rust-nostr/nostr/pull/1246) aggiunge supporto per le API bloccanti per completare la riprogettazione.

Le modifiche portano consistenza all'SDK ma richiederanno sforzo di migrazione dai progetti esistenti. Gli sviluppatori che costruiscono su rust-nostr dovrebbero rivedere attentamente il changelog prima di aggiornare.

### Instagram to Nostr v2 Abilita la Migrazione dei Contenuti

Un nuovo strumento permette ai creatori di migrare i loro contenuti esistenti dalle piattaforme centralizzate a Nostr. [Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2) supporta l'importazione da Instagram, TikTok, Twitter e Substack senza richiedere accesso alle chiavi private dell'utente.

Lo strumento affronta una barriera comune all'onboarding: gli utenti esitanti a ricominciare da zero su una nuova piattaforma possono ora preservare la loro cronologia di contenuti. Supporta anche il regalare account Nostr a nuovi utenti o proporre contenuti ad account esistenti, rendendolo utile per aiutare altri nella transizione al protocollo.

### Pod21: Rete di Stampa 3D Decentralizzata

[Pod21](https://pod21.com) connette operatori di stampanti 3D con acquirenti usando Nostr per la coordinazione del marketplace. La piattaforma include un bot DM compatibile [NIP-17 (Messaggi Diretti Privati)](/it/topics/nip-17/) che gestisce le interazioni del marketplace, permettendo agli acquirenti di richiedere stampe e negoziare con i maker attraverso messaggi diretti crittografati.

I maker elencano la loro capacità e competenze di stampa; gli acquirenti sfogliano le inserzioni e avviano ordini tramite il bot. L'architettura segue un pattern simile ad altre applicazioni commerciali Nostr: scoperta basata su relay, messaggistica crittografata per la coordinazione degli ordini, e Lightning per il settlement. Pod21 si unisce a Ridestr e Shopstr come applicazioni Nostr che coordinano transazioni nel mondo reale attraverso il protocollo.

### Clawstr: Social Network con Agenti AI

[Clawstr](https://github.com/clawstr/clawstr) si lancia come piattaforma ispirata a Reddit dove agenti AI creano e gestiscono community su Nostr. La piattaforma permette ad agenti autonomi di stabilire community tematiche, curare contenuti e interagire con gli utenti. Le community funzionano come subreddit ma con moderatori e curatori AI che guidano le discussioni. L'architettura usa il protocollo aperto di Nostr per interazioni agente-agente e agente-umano, stabilendo un nuovo modello per la formazione di community sui social media decentralizzati.

## Rilasci

### Ridestr v0.2.0: RoadFlare Release

[Ridestr](https://github.com/variablefate/ridestr) ha rilasciato [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0), denominato "RoadFlare Release", introducendo reti personali di rideshare. La funzionalità permette ai passeggeri di aggiungere autisti preferiti a una rete fidata. Gli autisti approvano i follower e condividono posizioni crittografate, permettendo ai passeggeri di vedere quando autisti fidati sono online e nelle vicinanze. Le richieste di corsa vanno direttamente agli autisti conosciuti.

L'affidabilità dei pagamenti è migliorata con recupero automatico dell'escrow, migliore sincronizzazione wallet tra dispositivi e elaborazione pagamenti più veloce tramite polling progressivo. [PR #37](https://github.com/variablefate/ridestr/pull/37) aggiunge l'infrastruttura Fase 5-6 che supporta queste funzionalità. [v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1) ha seguito con hotfix per bug della dialog di pagamento e il flusso "Aggiungi ai Preferiti" post-corsa.

### Nostria 3.0

[Nostria](https://github.com/nostria-app/nostria), il client cross-platform di sondreb costruito per scala globale, ha rilasciato la versione 3.0 con una completa revisione dell'UI, nuovo logo e centinaia di fix. Il rilascio rappresenta un intensivo ciclo di sviluppo di sei settimane.

La navigazione a doppio pannello è il cambiamento UX più grande, permettendo agli utenti desktop di ridurre il cambio di contesto quando si spostano tra liste, dettagli e thread. Una nuova sezione Home fornisce una panoramica di tutte le funzionalità disponibili, e tutti gli schermi condividono toolbar, layout e funzionalità unificati.

La gestione delle liste è l'aggiornamento funzionale più significativo, integrato in tutta l'applicazione. Gli utenti possono gestire liste di profili e filtrare contenuti in qualsiasi funzionalità: Stream, Musica o Feed. Stanchi dello spam nei thread? Filtra per preferiti per vedere solo le loro risposte. Quick Zaps aggiunge zapping con un tap con valori configurabili. Copia/Screenshot genera screenshot per la clipboard per condividere eventi ovunque. Parole Silenziate ora filtra sui campi del profilo (name, display_name, NIP-05), permettendo agli utenti di bloccare tutti i profili bridged con una singola parola bannata. Le Impostazioni sono diventate ricercabili per modifiche di configurazione più veloci.

Il rilascio aggiunge rendering delle richieste di pagamento BOLT11 e BOLT12, selezione dimensione testo e font, e messaggistica "Nota-a-Te-Stesso" nella sezione Messaggi con rendering di contenuti referenziati come articoli ed eventi. La nuova dialog Condividi permette condivisione rapida via email, siti web o messaggi diretti a più destinatari. Funzionalità aggiuntive includono set di emoji personalizzati, Interessi (liste hashtag come feed dinamici), Segnalibri, Feed Relay Pubblici e personalizzazione completa del menu inclusa quale opzione apre l'icona Nostria.

Disponibile su Android, iOS, Windows e web su [nostria.app](https://www.nostria.app/).

### Applesauce v5.1.0

La suite di librerie [Applesauce](https://github.com/hzrd149/applesauce) di hzrd149 ha rilasciato v5.1.0 su tutti i pacchetti. [applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0) aggiunge supporto per i metodi `switch_relays` e `ping` sui signer remoti Nostr Connect, utili per gestire le connessioni signer programmaticamente. [applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0) introduce `loadAsyncMap` per caricamento asincrono parallelo. [applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0) aggiunge argomenti padding a `useAction().run()`. [applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0) aggiorna il mapping event-to-store per gestire stringhe direttamente senza richiedere `onlyEvents`.

### nak v0.18.3

Il [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) di fiatjaf ha raggiunto [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) con fix di stabilità da mattn. Il rilascio previene panic quando gli URL mint mancano del separatore `://`, valida gli errori del dateparser prima di usare i valori data e gestisce casi limite nel parsing dei tag AUTH challenge. Questi fix difensivi rendono la CLI più resiliente quando elabora input malformati.

### Aegis v0.3.7

[Aegis](https://github.com/ZharlieW/Aegis), il signer desktop cross-platform, ha rilasciato [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7) aggiungendo supporto Nostr App Browser con firma [NIP-07 (Interfaccia Estensione Browser)](/it/topics/nip-07/). Il rilascio registra eventi di crittografia [NIP-04 (Messaggi Diretti Crittografati)](/it/topics/nip-04/) e [NIP-44 (Crittografia Versionata)](/it/topics/nip-44/), permettendo agli utenti di tracciare quali applicazioni richiedono operazioni di crittografia. Il segmento browser ora filtra per piattaforma per mostrare solo app web.

### Bitchat v1.5.1 (iOS)

[Bitchat](https://github.com/permissionlesstech/bitchat), l'app di messaggistica offline-capable che usa Nostr e mesh Bluetooth, ha rilasciato [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1) con hardening di sicurezza iOS. [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) valida le firme degli eventi Nostr prima dell'elaborazione, rifiuta giftwrap e pacchetti embedded invalidi, limita i payload sovradimensionati e blocca gli ID mittente BLE announce spoofati. [PR #998](https://github.com/permissionlesstech/bitchat/pull/998) corregge l'autenticazione mesh BLE iOS legando gli ID mittente agli UUID di connessione, prevenendo lo spoofing di identità nella rete mesh. [PR #972](https://github.com/permissionlesstech/bitchat/pull/972) aggiunge rate limiting delle notifiche per prevenire flood di peer discovery quando più dispositivi mesh sono nelle vicinanze.

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app) ha rilasciato [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495) aggiungendo supporto [NIP-47](/it/topics/nip-47/) Nostr Wallet Connect tramite [PR #148](https://github.com/keychat-io/keychat-app/pull/148). Gli utenti possono ora connettere wallet Lightning esterni per i pagamenti all'interno dell'app di messaggistica. Il rilascio aggiunge anche notifiche desktop macOS.

### Nostrmo v3.5.0

[Nostrmo](https://github.com/haorendashu/nostrmo), il client Flutter cross-platform, ha rilasciato [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0) rivedendo il suo sistema di feed. L'aggiornamento sostituisce i feed fissi con alternative personalizzabili: Feed Generale, Feed Menzioni e Feed Relay, ciascuno configurabile attraverso nuove pagine di modifica. Il rilascio implementa supporto per il modello outbox per un migliore routing degli eventi ed espande la funzionalità relay locale con limiti di dimensione configurabili e supporto sottoscrizioni.

### Shosho v0.11.1

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), l'app di live streaming per Nostr, ha rilasciato [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1) con capacità di registrazione e VOD. L'aggiornamento aggiunge indicatori di presenza nella stanza che mostrano chi sta guardando gli stream, conversazioni chat threaded per una migliore organizzazione delle discussioni e supporto Nostr Connect su iOS tramite [NIP-46](/it/topics/nip-46/). Gli streamer possono ora salvare le loro trasmissioni per la visione successiva mantenendo interazioni chat in tempo reale con il loro pubblico.

### NosCall v0.5.0

[NosCall](https://github.com/sanah9/noscall), l'app per chiamate audio e video per Nostr, ha rilasciato [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release) con gruppi di contatti per organizzare le chiamate per categoria, gestione relay per l'ottimizzazione delle connessioni e impostazioni server ICE configurabili per una migliore traversal NAT. Il rilascio aggiunge anche supporto per la modalità scura. NosCall usa Nostr per il signaling e la coordinazione delle chiamate, abilitando chiamate peer-to-peer senza server centralizzati.

### diVine 1.0.4

[diVine](https://github.com/divinevideo/divine-mobile), il client video short-form looping di rabble, ha rilasciato [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4) come pre-release alpha Android prima della sua sottomissione a Zapstore. Il rilascio si concentra sul test della gestione delle chiavi Nostr, incluso import nsec, firma remota [NIP-46 (Nostr Connect)](/it/topics/nip-46/) con nsecBunker e Amber, e gestione URL nostrconnect://. Il team sta sollecitando feedback sulla compatibilità relay e l'interoperabilità video con altri client. [PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265) corregge la gestione dei percorsi file iOS che causava l'inutilizzabilità dei clip video dopo gli aggiornamenti dell'app memorizzando percorsi relativi invece di percorsi container assoluti. [PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251) corregge problemi di navigazione quando si visualizzano profili dai commenti.

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus) ha rilasciato [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2) come rilascio stabile, consolidando i [fix NWC coperti nelle edizioni precedenti](/it/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---fix-nwc).

### Frostr Igloo iOS TestFlight

[Frostr](https://frostr.org/) ha lanciato [Igloo per iOS](https://github.com/FROSTR-ORG/igloo-ios-prototype) su [TestFlight](https://testflight.apple.com/join/72hjQe3J), espandendo la firma a soglia ai dispositivi Apple. Frostr usa firme FROST (Flexible Round-Optimized Schnorr Threshold) per dividere le chiavi nsec in quote distribuite tra dispositivi, abilitando firma k-di-n con tolleranza ai guasti. Gli utenti che si uniscono in "demo mode" partecipano a un esperimento live di firma a soglia 2-di-2, dimostrando le capacità di coordinazione in tempo reale del protocollo. Il rilascio iOS si unisce a [Igloo per Android](https://github.com/FROSTR-ORG/igloo-android) (v0.1.2), rilasciato a dicembre con supporto [NIP-55 (Android Signer)](/it/topics/nip-55/) per richieste di firma cross-app. Entrambi i client mobile complementano [Igloo desktop](https://github.com/FROSTR-ORG/igloo-desktop) e l'estensione browser [Frost2x](https://github.com/FROSTR-ORG/frost2x).

## Aggiornamenti dei Progetti

### Damus Implementa Suggerimenti Relay NIP-19

[Damus](https://github.com/damus-io/damus) ha unito [PR #3477](https://github.com/damus-io/damus/pull/3477), implementando il consumo di suggerimenti relay [NIP-19](/it/topics/nip-19/) per il recupero degli eventi. La funzionalità permette di visualizzare note su relay non nel pool configurato dell'utente estraendo suggerimenti da riferimenti [NIP-10 (Thread di Risposta)](/it/topics/nip-10/), [NIP-18 (Repost)](/it/topics/nip-18/) e NIP-19. L'implementazione usa connessioni relay effimere con cleanup reference-counted, evitando l'espansione permanente del pool di relay.

Fix aggiuntivi includono parsing di Lightning invoice ([PR #3566](https://github.com/damus-io/damus/pull/3566)), caricamento vista wallet ([PR #3554](https://github.com/damus-io/damus/pull/3554)), timing lista relay ([PR #3553](https://github.com/damus-io/damus/pull/3553)) e precaricamento profili per ridurre il "popping" visivo ([PR #3550](https://github.com/damus-io/damus/pull/3550)). Una [bozza PR #3590](https://github.com/damus-io/damus/pull/3590) mostra il supporto DM privati [NIP-17](/it/topics/nip-17/) in corso.

### Primal Android Rilascia Crittografia NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) ha avuto una settimana molto attiva con 18 PR unite focalizzate sull'infrastruttura wallet. L'app ora si integra con Spark, il protocollo Lightning self-custodial di Lightspark. [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) aggiunge supporto crittografia NWC, mentre [PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872) invia eventi info NWC quando le connessioni si stabiliscono.

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870) abilita l'export CSV per le transazioni wallet, utile per contabilità e fini fiscali. [PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716) aggiunge uno switcher account locale nell'Editor Note. Molteplici fix di ripristino wallet ([PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876), [PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875), [PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)) affrontano casi limite per utenti con configurazioni wallet non-Spark.

### Marmot TypeScript SDK Aggiunge Cronologia Messaggi

L'implementazione TypeScript del protocollo [Marmot](https://github.com/marmot-protocol/marmot) continua lo sviluppo. [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) di hzrd149 implementa la persistenza della cronologia messaggi con paginazione per l'applicazione chat di riferimento, mentre [PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39) migliora l'ergonomia della libreria.

Sul lato Rust, [PR #161](https://github.com/marmot-protocol/mdk/pull/161) implementa gestione dello stato riprovabile per preservare il contesto dei messaggi in caso di fallimento, e [PR #164](https://github.com/marmot-protocol/mdk/pull/164) passa a std::sync::Mutex per evitare panic tokio con SQLite. Il backend whitenoise-rs aggiunge [integrazione Amber](https://github.com/marmot-protocol/whitenoise-rs/pull/418) ([PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)), [upgrade a MDK e nostr-sdk 0.44](https://github.com/marmot-protocol/whitenoise-rs/pull/467) ([PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)), e introduce streaming notifiche in tempo reale tramite [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460) con tipi evento NewMessage e GroupInvite.

### HAVEN Aggiunge Refresh Periodico WoT

[HAVEN](https://github.com/bitvora/haven), il relay personale, ha unito [PR #108](https://github.com/bitvora/haven/pull/108) aggiungendo refresh periodico [Web of Trust](/it/topics/web-of-trust/). La funzionalità assicura che i punteggi di fiducia rimangano aggiornati mentre i grafi sociali degli utenti evolvono, migliorando l'accuratezza del filtraggio spam nel tempo.

### nostr-tools

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), la libreria JavaScript core, ha ricevuto molteplici miglioramenti questa settimana. I commit includono un [fix per il parsing degli hashtag dopo le newline](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5) nelle menzioni [NIP-27 (Riferimenti nelle Note di Testo)](/it/topics/nip-27/), [pruning automatico di oggetti relay rotti con tracking idle](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2) per cleanup delle connessioni, [rimozione della coda messaggi](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638) per ottimizzazione delle prestazioni single-threaded, e [export dei file sorgente](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139) per migliori import TypeScript.

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk) ha rilasciato [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0) con un [fix per la riconnessione dopo cicli sleep/wake del dispositivo e gestione connessioni stale](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3), affrontando problemi di affidabilità per le applicazioni mobile.

### Notedeck

[Notedeck](https://github.com/damus-io/notedeck), il client desktop del team Damus, ha una [PR aperta #1279](https://github.com/damus-io/notedeck/pull/1279) che aggiunge un visualizzatore [NIP-34 (Collaborazione Git)](/it/topics/nip-34/). Questo permetterebbe di sfogliare repository git, patch e issue pubblicati sui relay Nostr direttamente nel client, rendendo Notedeck un potenziale front-end per workflow basati su ngit.

### njump

[njump](https://github.com/fiatjaf/njump), il gateway web Nostr, ha aggiunto supporto per due tipi di evento [NIP-51 (Liste)](/it/topics/nip-51/) tramite [PR #152](https://github.com/fiatjaf/njump/pull/152). Il gateway ora renderizza Follow Sets kind:30000, che sono raggruppamenti categorizzati di utenti che i client possono visualizzare in contesti diversi, e Starter Packs kind:39089, che sono collezioni di profili curate progettate per la condivisione e il following di gruppo. Queste aggiunte permettono a njump di visualizzare liste curate dalla community quando gli utenti condividono link nevent.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android, ha corretto un bug che impediva la condivisione video dalla vista player ([PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)). L'opzione "Condividi video" non appariva perché il parametro content non veniva passato al componente pulsanti di controllo. Gli utenti possono ora condividere contenuti video Nostr ad altre app direttamente dal player. [PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693) corregge crash di deserializzazione Jackson JSON che si verificavano durante il parsing di certi eventi malformati.

### Jumble

[Jumble](https://github.com/CodyTseng/jumble), il client web focalizzato sul browsing dei feed relay, ha aggiunto upload di file audio tramite clipboard in [PR #743](https://github.com/CodyTseng/jumble/pull/743). Gli utenti possono ora incollare file audio direttamente nell'editor post, che li carica sui media server configurati e incorpora l'URL nella nota. La funzionalità rispecchia la funzionalità esistente di incolla immagini.

### Flotilla

[Flotilla](https://github.com/coracle-social/flotilla), il client community [NIP-29 (Gruppi Basati su Relay)](/it/topics/nip-29/) di hodlbod, ha rilasciato notifiche tramite [PR #270](https://github.com/coracle-social/flotilla/pull/270). L'aggiornamento rifà il sistema di alert da polling basato su anchor a notifiche pull locali per web e notifiche push per mobile. L'architettura implementa lo standard proposto NIP-9a (vedi [PR #2194](https://github.com/nostr-protocol/nips/pull/2194) sotto), dove gli utenti registrano callback webhook con i relay e ricevono payload evento crittografati quando i filtri corrispondono.

### Formstr

[Formstr](https://github.com/abh3po/nostr-forms), l'applicazione form nativa Nostr, ha aggiunto import form e supporto form crittografati in [PR #422](https://github.com/abh3po/nostr-forms/pull/422). Gli utenti possono ora importare form esistenti da JSON o altre istanze Formstr. La funzionalità di crittografia permette ai creatori di form di restringere le risposte in modo che solo i destinatari designati possano leggere le sottomissioni, utile per sondaggi che raccolgono informazioni sensibili.

### Pollerama

[Pollerama](https://pollerama.fun), costruito sulla libreria [nostr-polls](https://github.com/abh3po/nostr-polls), ha aggiunto condivisione DM [NIP-17](/it/topics/nip-17/) per i sondaggi tramite [PR #141](https://github.com/abh3po/nostr-polls/pull/141) e [PR #142](https://github.com/abh3po/nostr-polls/pull/142). Gli utenti possono ora condividere sondaggi direttamente ai contatti attraverso messaggi diretti crittografati.

### Nostrability Schemata

[Nostrability schemata](https://github.com/nostrability/schemata), la collezione di schema di verifica JSON per eventi Nostr, ha aggiunto copertura [NIP-59 (Gift Wrap)](/it/topics/nip-59/) tramite [PR #59](https://github.com/nostrability/schemata/pull/59). L'aggiornamento include schema per eventi kind 13 (seal) e kind 1059 (gift wrap), complementando la copertura schema [NIP-17](/it/topics/nip-17/) esistente.

### Vector

[Vector](https://github.com/VectorPrivacy/Vector), il messenger desktop privacy-focused che usa [NIP-17](/it/topics/nip-17/), [NIP-44](/it/topics/nip-44/) e [NIP-59](/it/topics/nip-59/) per crittografia zero-metadata, ha unito [PR #39](https://github.com/VectorPrivacy/Vector/pull/39) introducendo ottimizzazioni di prestazioni accelerate SIMD. La codifica hex gira 65x più veloce, la generazione preview immagini fino a 38x più veloce, e le ricerche messaggi 184x più veloci tramite indicizzazione binary search. La PR aggiunge intrinsics ARM64 NEON per Apple Silicon e x86_64 AVX2/SSE2 con rilevamento runtime per Windows e Linux. L'uso di memoria è calato con struct messaggi ridotte da 472 a 128 byte e storage npub tagliato del 99.6% attraverso interning.

Vector v0.3.0 (Dicembre 2025) ha integrato [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk) per messaggistica di gruppo basata su protocollo MLS, portando gruppi crittografati end-to-end con forward secrecy al client. La condivisione file MIP-04 ora gestisce attachment imeta per gruppi MLS, progettata per interoperabilità con [White Noise](/it/newsletters/2026-01-28-newsletter/#marmot-typescript-sdk-aggiunge-cronologia-messaggi). Il rilascio ha anche introdotto una piattaforma Mini Apps con giochi multiplayer P2P basati su WebXDC, un app store decentralizzato chiamato The Nexus, integrazione wallet PIVX per pagamenti in-app, editing messaggi con tracking completo della cronologia e riduzione memoria 4x durante gli upload di immagini.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti:**

- **[NIP-47: Supporto Hold Invoice](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/it/topics/nip-47/) ora supporta hold invoice, abilitando workflow di pagamento avanzati dove i riceventi devono esplicitamente settlare o cancellare i pagamenti. La PR aggiunge tre nuovi metodi RPC: `make_hold_invoice` crea un hold invoice usando preimage e payment hash pre-generati, `settle_hold_invoice` reclama il pagamento fornendo la preimage originale, e `cancel_hold_invoice` rifiuta il pagamento usando il suo payment hash. Una nuova notifica `hold_invoice_accepted` scatta quando un pagante blocca il pagamento. Questo abilita casi d'uso come pay-to-unlock content, sistemi escrow marketplace e payment gating. Le implementazioni sono già in corso in [Alby Hub](https://github.com/getAlby/hub/pull/1298), [Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382) e [dart NDK](https://github.com/relaystr/ndk/pull/147).

- **[NIP-05: Requisito Minuscole](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (Verifica del Dominio)](/it/topics/nip-05/) ora richiede esplicitamente minuscole sia per le chiavi pubbliche esadecimali che per i nomi locali nel file `nostr.json`. Questo era implicito nella spec ma non dichiarato, causando problemi di interoperabilità quando alcune implementazioni usavano case misto mentre altre normalizzavano a minuscole. I client che validano identificatori NIP-05 dovrebbero ora rifiutare qualsiasi risposta `nostr.json` contenente caratteri maiuscoli in chiavi o nomi.

- **[NIP-73: Codici Paese](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (Geotag)](/it/topics/nip-73/) ora supporta codici paese ISO 3166 come alternativa ai geohash. Gli eventi possono includere tag `["g", "US", "countryCode"]` per indicare posizione a livello paese senza richiedere coordinate precise. Questo abilita filtraggio e scoperta contenuti basati sul paese per applicazioni dove la posizione esatta è non necessaria o indesiderata. La PR ha anche aggiunto un esempio geohash mancante alla documentazione spec.

**PR Aperte e Discussioni:**

- **[NIP-82: Applicazioni Software](https://github.com/nostr-protocol/nips/pull/1336)** - franzap ha annunciato un importante aggiornamento a questa specifica bozza, che definisce come le applicazioni software vengono distribuite via Nostr usando eventi release kind 30063. L'aggiornamento ora copre approssimativamente il 98% delle piattaforme dispositivo globalmente, incluso macOS, Linux, Windows, FreeBSD, ambienti WASM, estensioni VS Code, estensioni Chrome e Web Bundles/PWA. Il team si sta concentrando poi su Android, PWA e supporto iOS, invitando gli sviluppatori a convergere su questo standard condiviso. Zapstore pianifica di migrare al nuovo formato nelle prossime settimane.

- **[NIP-74: Podcast](https://github.com/nostr-protocol/nips/pull/2211)** - Definisce eventi addressable per show podcast (kind 30074) ed episodi (kind 30075). Gli show includono metadati come titolo, descrizione, categorie e immagini copertina. Gli episodi referenziano il loro show genitore e includono URL enclosure, durate e marcatori capitoli. La spec si integra con gli standard metadati Podcasting 2.0 e include tag value per monetizzazione V4V (value-for-value) via Lightning. Piattaforme come [transmit.fm](https://transmit.fm), una piattaforma di pubblicazione podcast nativa Nostr, possono pubblicare direttamente sui relay usando questo formato, permettendo ai podcaster di distribuire contenuti senza intermediari.

- **[NIP-FR: Note Solo-Amici](https://github.com/nostr-protocol/nips/pull/2207)** - Propone un meccanismo per pubblicare note visibili solo ai follow reciproci. L'implementazione usa [NIP-59 (Gift Wrap)](/it/topics/nip-59/) per crittografare i contenuti: l'autore crea una nota regolare, poi gift-wrappa copie a ogni follow reciproco. La copia di ogni destinatario è crittografata alla loro pubkey usando NIP-44 e inviata via meccanismo gift wrap. I destinatari possono verificare che la nota provenga da qualcuno che seguono, mentre i non-reciproci non possono accedere al contenuto. Questo approccio riusa l'infrastruttura crittografica esistente abilitando una funzionalità privacy frequentemente richiesta.

- **[NIP-DB: Interfaccia Database Eventi Nostr nel Browser](https://github.com/hzrd149/nostr-bucket)** - Propone un'interfaccia standard `window.nostrdb` per estensioni browser che forniscono storage eventi Nostr locale. L'API include metodi per aggiungere eventi, query per ID o filtro, conteggio match e sottoscrizione agli aggiornamenti. Le applicazioni web possono usare questa interfaccia per leggere da eventi cached localmente senza fare richieste relay, riducendo banda e latenza. L'estensione browser [nostr-bucket](https://github.com/hzrd149/nostr-bucket) di hzrd149 fornisce un'implementazione di riferimento, iniettando l'interfaccia in tutti i tab del browser. Una [libreria polyfill](https://github.com/hzrd149/window.nostrdb.js) complementare implementa la stessa API usando IndexedDB per ambienti senza l'estensione.

- **[TRUSTed Filters](https://github.com/nostr-protocol/nips/pull/1534)** - Una suite di cinque proposte correlate per la curation decentralizzata dei contenuti, costruendo sulla [PR #1534 Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534) di vitorpamplona. La specifica core introduce eventi kind 17570 per dichiarare Trust Provider Preferences, permettendo agli utenti di specificare quali servizi fidano per filtraggio e ranking degli eventi. I trust provider pubblicano assertions (kind 37571), statistiche (kind 37572) e rankings (kind 37573) a cui i client possono sottoscriversi. Il sistema usa un'architettura plugin con tag W/w per specificare tipi di filtro e trasformazioni. Questo permette a operazioni computazionalmente costose come spam detection, reputation scoring e content ranking di girare su infrastruttura dedicata mentre gli utenti mantengono controllo su quali provider fidano. La suite include spec separate per filter presets, user rankings, trusted events e definizioni plugin.

- **[NIP-9a: Notifiche Push](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod propone uno standard per notifiche push basate su relay usando eventi registrazione kind 30390. Gli utenti creano una registrazione contenente filtri per eventi che vogliono ricevere e un URL callback webhook. La registrazione è crittografata alla pubkey del relay (dal suo campo `self` NIP-11). Quando si verificano eventi corrispondenti, i relay POSTano al callback con l'ID evento (plaintext per deduplicazione) e l'evento stesso (crittografato NIP-44 all'utente). Questa architettura permette ai relay di pushare notifiche proteggendo il contenuto degli eventi dai server push intermediari. La [PR #270](https://github.com/coracle-social/flotilla/pull/270) di Flotilla implementa questo standard.

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - Propone un protocollo decentralizzato per lavoro a contratto con escrow usando eventi kind 33400. Il sistema definisce tre ruoli: gli arbiter annunciano disponibilità e termini, i patron creano task finanziati con Bitcoin in escrow, e i free agent completano lavoro per reclamare il pagamento. Gli arbiter risolvono le dispute quando necessario. Il protocollo abilita coordinazione di lavoro freelance trustless dove i fondi sono bloccati fino a che i deliverable sono accettati o l'arbitrato conclude.

## NIP Deep Dive: NIP-47 (Nostr Wallet Connect)

[NIP-47](/it/topics/nip-47/) definisce Nostr Wallet Connect (NWC), un protocollo per il controllo remoto di wallet Lightning usando Nostr come layer di comunicazione. Con l'aggiunta del supporto hold invoice di questa settimana, NWC ora copre l'intera gamma di operazioni Lightning.

Il protocollo funziona attraverso uno scambio semplice. Un'applicazione wallet pubblica un evento "wallet info" (kind 13194) che descrive le sue capacità. Le applicazioni client inviano richieste crittografate (kind 23194) chiedendo al wallet di eseguire operazioni come pagare invoice, creare invoice o controllare saldi. Il wallet risponde con risultati crittografati (kind 23195).

NWC usa crittografia [NIP-44](/it/topics/nip-44/) tra client e wallet, con una keypair dedicata per le operazioni wallet, mantenendola separata dall'identità principale dell'utente. Questa separazione significa che compromettere una connessione NWC non espone l'identità Nostr dell'utente.

**Metodi Supportati:**

La spec definisce metodi per operazioni Lightning core: `pay_invoice` invia pagamenti, `make_invoice` genera invoice per ricevere, `lookup_invoice` controlla lo stato del pagamento, `get_balance` restituisce il saldo wallet, e `list_transactions` fornisce la cronologia pagamenti. I nuovi `pay_keysend` appena uniti abilitano pagamenti senza invoice, e `hold_invoice` supporta pagamenti condizionali.

**Eventi di Esempio:**

Il servizio wallet pubblica un evento info (kind 13194) pubblicizzando le sue capacità:

```json
{
  "kind": 13194,
  "pubkey": "<pubkey servizio wallet>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<timestamp unix>",
  "id": "<hash evento>",
  "sig": "<firma servizio wallet>"
}
```

Un client invia una richiesta crittografata (kind 23194) per pagare un invoice:

```json
{
  "kind": 23194,
  "pubkey": "<pubkey effimera client dall'URI connection secret>",
  "content": "<NIP-44 crittografato: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<pubkey servizio wallet>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<timestamp unix>",
  "id": "<hash evento>",
  "sig": "<firma chiave effimera client>"
}
```

Il servizio wallet risponde (kind 23195) con il risultato del pagamento:

```json
{
  "kind": 23195,
  "pubkey": "<pubkey servizio wallet>",
  "content": "<NIP-44 crittografato: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<pubkey effimera client>"],
    ["e", "<id evento richiesta>"]
  ],
  "created_at": "<timestamp unix>",
  "id": "<hash evento>",
  "sig": "<firma servizio wallet>"
}
```

Il tag `e` nella risposta referenzia la richiesta originale, permettendo ai client di abbinare le risposte alle loro richieste.

**Hold Invoice:**

La [PR #1913](https://github.com/nostr-protocol/nips/pull/1913) di questa settimana ha aggiunto supporto hold invoice, abilitando pagamenti stile escrow. A differenza degli invoice standard dove il ricevente reclama immediatamente il pagamento rilasciando la preimage, gli hold invoice permettono al ricevente di differire questa decisione. Quando un pagante invia a un hold invoice, i fondi si bloccano lungo il percorso di pagamento. Il ricevente poi sceglie se settlare (rilasciare la preimage e reclamare i fondi) o cancellare (rifiutare il pagamento, restituendo i fondi al pagante). Se nessuna azione avviene, il pagamento va in timeout e i fondi ritornano automaticamente. La PR aggiunge tre metodi NWC: `make_hold_invoice`, `settle_hold_invoice` e `cancel_hold_invoice`, più una notifica `hold_invoice_accepted`. Questo meccanismo alimenta applicazioni come l'escrow rideshare di Ridestr e la risoluzione dispute marketplace.

**Implementazioni Attuali:**

I wallet principali supportano NWC: Zeus, Alby e Primal (dalla [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) di questa settimana) tutti implementano supporto lato wallet. Sul lato client, Damus, Amethyst e la maggior parte dei client Nostr principali possono connettersi a wallet NWC per zapping e pagamenti.

Il protocollo abilita una separazione delle responsabilità: gli utenti possono far girare il loro wallet su un dispositivo mentre interagiscono con Nostr da un altro, con i relay Nostr che servono come canale di comunicazione. Questa architettura significa che i client mobile non devono detenere fondi direttamente, migliorando la sicurezza mantenendo l'infrastruttura wallet separata dai client social.

**Considerazioni sulla Sicurezza:**

Le connessioni NWC dovrebbero essere trattate come sensibili. Mentre la crittografia protegge il contenuto dei messaggi, la pubkey wallet e il connection secret devono essere custoditi. Le applicazioni dovrebbero permettere agli utenti di revocare connessioni e impostare limiti di spesa. Il protocollo supporta restrizioni di capacità, così i wallet possono limitare quali operazioni una particolare connessione può eseguire.

## NIP Deep Dive: NIP-59 (Gift Wrap)

[NIP-59](/it/topics/nip-59/) definisce un protocollo per incapsulare qualsiasi evento Nostr in più livelli di crittografia, nascondendo l'identità del mittente dai relay e dagli osservatori. Le proposte di questa settimana per note solo-amici (NIP-FR) e notifiche push (NIP-9a) entrambe si basano sul gift wrapping, rendendolo una primitiva privacy fondamentale da comprendere.

**I Tre Livelli:**

Il gift wrapping usa tre strutture annidate:

1. **Rumor** (evento non firmato): Il contenuto originale come evento Nostr senza firma. Il rumor non può essere inviato direttamente ai relay perché i relay rifiutano eventi non firmati.

2. **Seal** (kind 13): Il rumor è crittografato usando [NIP-44](/it/topics/nip-44/) e posto in un evento kind 13. Il seal E' firmato dalla chiave reale dell'autore. Questa è la prova crittografica di paternità.

3. **Gift Wrap** (kind 1059): Il seal è crittografato e posto in un evento kind 1059 firmato da una keypair casuale, usa-e-getta. Il gift wrap include un tag `p` per il routing al destinatario.

**Un Malinteso Comune: La Negabilità**

La spec menziona che i rumor non firmati forniscono "negabilità", ma questo è fuorviante. Il livello seal E' firmato dal vero autore. Quando il destinatario decritta il gift wrap e poi il seal, ha prova crittografica di chi ha inviato il messaggio. Il destinatario potrebbe persino costruire una prova zero-knowledge rivelando l'identità del mittente senza esporre la propria chiave privata.

Quello che il gift wrap in realtà fornisce è **privacy del mittente dagli osservatori**: i relay e le terze parti non possono determinare chi ha inviato il messaggio perché vedono solo il gift wrap firmato da una chiave casuale. Ma il destinatario sa sempre, e può provarlo.

**Eventi di Esempio:**

Ecco la struttura completa a tre livelli dalla spec (invio "Vai alla festa stasera?"):

Il rumor (non firmato, non può essere pubblicato sui relay):
```json
{
  "created_at": 1691518405,
  "content": "Are you going to the party tonight?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

Il seal (kind 13, firmato dal vero autore, contiene rumor crittografato):
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

Il gift wrap (kind 1059, firmato da chiave effimera casuale, contiene seal crittografato):
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

Nota: la `pubkey` del seal è il vero autore (`611df01...`), mentre la `pubkey` del gift wrap è una chiave casuale usa-e-getta (`18b1a75...`). I relay vedono solo il gift wrap, quindi non possono attribuire il messaggio al vero autore.

**Cosa Protegge Ogni Livello:**

Il rumor non è firmato e non può essere pubblicato direttamente sui relay. Il seal è firmato dal vero autore e prova la paternità al destinatario. Il gift wrap è firmato da una chiave casuale usa-e-getta, nascondendo il vero autore dai relay e dagli osservatori. Solo il destinatario può decrittare attraverso entrambi i livelli per raggiungere il contenuto originale e verificare la firma dell'autore sul seal.

**Applicazioni Attuali:**

[NIP-17 (Messaggi Diretti Privati)](/it/topics/nip-17/) usa gift wrap per DM crittografati, sostituendo il vecchio schema NIP-04. Il proposto NIP-FR (note solo-amici) gift-wrappa note a ogni follow reciproco. NIP-9a (notifiche push) critta i payload di notifica usando principi gift wrap.

**Protezione dei Metadati:**

I timestamp dovrebbero essere randomizzati per contrastare l'analisi temporale. I relay dovrebbero richiedere AUTH prima di servire eventi kind 1059 e servirli solo al destinatario marcato. Quando si invia a più destinatari, creare gift wrap separati per ciascuno.

---

È tutto per questa settimana. Stai costruendo qualcosa? Hai notizie da condividere? Vuoi che copriamo il tuo progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattaci via DM NIP-17</a> o trovaci su Nostr.
