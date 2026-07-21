---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
draft: false
type: newsletters
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
description: "Vector v0.4.0 ritira Marmot per le chat di gruppo a favore del protocollo aperto Concord e rilascia Concord v2 pochi giorni dopo, Amethyst integra la propria implementazione pulita di Concord, Sonar si separa da Bitchat con un'alpha multipiattaforma e una specifica per pacchetti di sticker, Divine Mobile 1.0.16 introduce la cifratura a riposo e la provenienza ProofMode, Bitchat 1.7.0 aggiunge la voce push-to-talk dal vivo, e MDK v0.9.4 limita il login con firmatario esterno."
---

Bentornati su Nostr Compass, la vostra guida settimanale su Nostr.

**Questa settimana:** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) ritira [Marmot](/it/topics/marmot/) come trasporto predefinito per le Chat di Gruppo a favore di [Concord](/it/topics/concord-protocol/), un protocollo di comunità aperto con licenza MIT usato anche da Armada di Soapbox, e rilascia Concord v2 quattro giorni dopo con un selettore di comandi con barra per i bot, un timer di autodistruzione e badge NIP-58. [Amethyst integra la propria implementazione pulita e compatibile a livello di protocollo di Concord](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities), la stessa settimana. [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) si separa da Bitchat con un'alpha multipiattaforma ed è la fonte di specifica citata per la proposta di kind per pacchetti di sticker di questa settimana. [Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) introduce un editor video più completo, la cifratura a riposo e la provenienza ProofMode che sopravvive al download di clip con filigrana. [Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) aggiunge la voce push-to-talk dal vivo per i DM e il push-to-talk firmato sulla mesh pubblica. [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) limita il login con firmatario esterno e aggiunge la persistenza delle bozze, proseguendo il suo lavoro di irrobustimento la stessa settimana in cui Vector si allontana dalla specifica per la chat di gruppo.

I rilasci taggati portano [n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) con il supporto per NSEC Bunker, [cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) con il supporto per il servizio di wallet NIP-47 su cdk, cdk-nwc e cdk-ffi, [Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) con miglioramenti a Nostr Connect e l'importazione ncryptsec1, [Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) che arriva su macOS con l'invio programmato, [Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) con un interruttore generale per i DM, [Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) che irrobustisce i backup delle chiavi al formato NIP-49, [Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) con l'onboarding FROST al primo avvio, [Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) con un wallet Cashu e notifiche push basate su relay, [Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) con la modalità tablet e le foto nelle chat di gruppo, e [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) con richieste ausiliarie per git, diff e lettura di file.

Sul fronte non rilasciato, [Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) consente agli account di assegnare soprannomi ai contatti con schede NIP-85 cifrate attraverso 54 PR integrate, [Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) rilascia la Fase 3 di My Kitchen e corregge un bug di quorum del pool NDK, [Kehto](#kehto-streams-outbox-reads-before-relay-discovery) trasmette le letture di outbox prima che finisca la scoperta dei relay, [Wired e TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) aggiungono la condivisione dei ricavi per i creatori con NIP-57, [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) ricostruisce la casella degli ordini del commerciante attorno al checkout come ospite effimero, [Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) irrobustisce il provisioning del creatore di canale attraverso 240 PR integrate, e [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) adotta un firmatario NIP-49 con account multipli e accoppiamento QR. Tracciati per la prima volta questa settimana: [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr), [Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles), e la scelta Discovery [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer), un firmatario NIP-55 senza chiavi che fa da proxy verso un dispositivo hardware Heartwood.

Il repository dei NIP non integra nulla nell'ultima settimana e apre sei proposte: [kind:10011 set di follow preferiti](#open-kind10011-favorite-follow-sets), un'[unità cifrata privata che estende NIP-4E](#open-private-encrypted-drive-extends-nip-4e), [NIP-DA condivisione privata di dati con permessi](#open-nip-da-permissioned-private-data-sharing), [kind per pacchetti di sticker 10031 e 30031](#open-sticker-pack-kinds-10031-and-30031), [fissaggio dei messaggi NIP-29](#open-nip-29-message-pinning-with-kind9010-and-kind39005), e una [ristrutturazione della scoperta di relay NIP-66](#open-nip-66-relay-discovery-restructure). Il Deep Dive copre [NIP-99 e l'estensione di commercio Gamma Markets](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension).

---

## Storie principali

### Vector v0.4.0 sposta le Chat di Gruppo da Marmot a Concord, e Amethyst rilascia il proprio client Concord pochi giorni dopo

[Vector](https://github.com/VectorPrivacy/Vector) è un messenger Nostr costruito attorno a un client a binario singolo, orientato alla privacy, per DM e chat di gruppo. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) riscrive il motore di messaggistica dell'app in una libreria condivisa `vector-core` e, nello stesso rilascio, ritira [Marmot](/it/topics/marmot/) (MLS-su-Nostr) come trasporto predefinito per le Chat di Gruppo a favore di [Concord](/it/topics/concord-protocol/), un protocollo di comunità cifrato end-to-end; la cronologia esistente dei gruppi Marmot non viene trasferita, e le note di rilascio indicano agli utenti di fare il backup di qualsiasi dato dei gruppi Marmot prima di aggiornare. Le note di rilascio di Vector descrivono Concord come "il nostro protocollo di messaggistica personalizzato", ma le [specifiche da CORD-01 a CORD-07](https://github.com/concord-protocol/concord) sottostanti sono pubblicate separatamente, con licenza MIT, e già implementate al di fuori di Vector: il client in stile Discord di Soapbox, [Armada](https://gitlab.com/soapbox-pub/armada), costruisce la sua funzionalità Communities sulla stessa specifica Concord, e un giorno dopo [Amethyst ha integrato la propria implementazione pulita e compatibile a livello di protocollo di Concord](https://github.com/vitorpamplona/amethyst/pull/3566), trattata in dettaglio più sotto. Lo stesso rilascio di Vector aggiunge il routing Tor opzionale per tutto il traffico, il login con firmatario remoto [NIP-46](/it/topics/nip-46/) tramite QR o URI bunker incollata, account multipli con un commutatore interno all'app, e pacchetti di emoji personalizzati condivisi tra i client. L'eliminazione di un messaggio lo rimuove per entrambe le parti nei DM e nelle chat di gruppo, e Vector mantiene deliberatamente la chiave di firma effimera invece di seguire il flusso di eliminazione standard [NIP-17](/it/topics/nip-17/), una deviazione motivata dalla privacy che il progetto segnala esplicitamente nelle note di rilascio. Quattro giorni dopo, [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) rilascia **Concord v2**, descritto come portatore di importanti miglioramenti di privacy e stabilità alle Communities mantenendo funzionanti quelle esistenti, insieme a un selettore di comandi con barra in stile Discord per i bot con parametri tipizzati, un timer di autodistruzione per chat, e un sistema di badge NIP-58 per i cacciatori di bug. L'allontanamento da Marmot per la chat di gruppo arriva la stessa settimana in cui [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) più sotto continua a investire nella specifica.

### Amethyst rilascia un'implementazione pulita di Concord per comunità cifrate end-to-end

[Amethyst](https://github.com/vitorpamplona/amethyst) è un client Nostr ricco di funzionalità per Android e multipiattaforma. [PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) aggiunge un'implementazione completa di [Concord](/it/topics/concord-protocol/) (da CORD-01 a CORD-07) che copre comunità serverless e cifrate end-to-end: piani di controllo, chat e guestbook avvolti con gift-wrap su relay ordinari, applicazione di ruoli e ban radicata nel proprietario che ogni client verifica localmente invece di fidarsi di un server, e re-keying per tagliare fuori i membri rimossi. Il codice di protocollo e crittografia risiede in `quartz/`, i modelli di stato e vista in `commons/`, e le schermate e la navigazione in `amethyst/` per Android, con verbi CLI leggeri sotto `cli/`; non c'è ancora un'interfaccia desktop, poiché la logica condivisa risiede in `quartz`/`commons` perché Desktop la adotti in seguito. L'implementazione è pulita: costruita dalle specifiche CORD pubbliche e dalle costanti di protocollo osservate, sotto la licenza MIT di Amethyst, distinta dal codice AGPL-3.0 di Armada. I valori dei vettori di test di Armada sono stati portati nei test unitari di Quartz per confermare che i due client interoperano realmente a livello di protocollo, dando a Concord tre implementazioni indipendenti nel giro di pochi giorni: Vector che rilascia per primo, Armada come client di riferimento di Soapbox, e ora la build da specifica di Amethyst.

### Sonar si separa da Bitchat con un'alpha multipiattaforma e una specifica per pacchetti di sticker

[Sonar](https://sonarprivacy.xyz/) è un messenger e wallet con mesh Bluetooth più Nostr nato da Bitchat, con DM di gruppo Marmot interoperabili con White Noise. Il codice risiede in [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar). [v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) aggiunge una finestratura limitata delle trascrizioni in stile Signal affinché le prestazioni di apertura e scorrimento restino local-first, sincronizza lo stato di scoperta dei peer vicini, e corregge i caricamenti di media Blossom che fallivano nella gestione del content-type e dello stato HTTP; la precedente [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) drenava gli eventi Marmot dal vivo per un aggiornamento più rapido della chat e chiudeva le lacune di parità di funzionalità tra Android e iOS su chiamate, messaggistica, wallet e push. Sonar è anche la fonte di specifica citata per [PR #2410](#open-sticker-pack-kinds-10031-and-30031), che registra i kind di evento per pacchetti di sticker sotto la specifica "Sonar Stickers" del progetto, dando a questo lancio un collegamento diretto al lavoro di protocollo di questa settimana.

### Divine Mobile 1.0.16 introduce un editor video più completo, la cifratura a riposo e la provenienza ProofMode

[Divine](https://github.com/divinevideo/divine-mobile) è un client di video brevi costruito su Nostr con curazione del feed tramite Web-of-Trust. [v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16), il primo rilascio taggato dal #30, aggiunge transizioni tra clip, riproduzione inversa, un registratore di voice-over e marcatori di ritmo sulla timeline all'editor video, insieme a un controllo di regolazione del feed che consente all'utente di scorrere per aggiustare le raccomandazioni direttamente invece di lasciarle a segnali di interazione opachi. Il rilascio attiva anche la cifratura a riposo per i dati locali, aggiunge caricamenti in background che sopravvivono alla sospensione dell'app, e trasporta i dati di provenienza [ProofMode](/it/topics/proofmode/) quando si scarica una clip con filigrana affinché l'attestazione di creazione umana non venga rimossa durante il transito. Divine include anche nuove protezioni per gli account di minori di 16 anni ed estende la localizzazione a 17 lingue e 284 stringhe tradotte.

### Bitchat v1.7.0 aggiunge la voce push-to-talk dal vivo per i DM e la mesh pubblica

[Bitchat](https://github.com/permissionlesstech/bitchat) è un'app di chat con mesh Bluetooth con un gateway opzionale verso i relay Nostr. [v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0), rilasciata la sera in cui è stato pubblicato il #30, aggiunge la voce push-to-talk dal vivo in [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) che trasmette l'audio mentre il mittente tiene premuto il pulsante e ripiega su una nota vocale se il flusso si interrompe, più il push-to-talk firmato sulla mesh pubblica in [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406) affinché le raffiche di voce dal vivo sul canale mesh condiviso portino l'autenticazione del mittente. Il rilascio ripara anche la rotazione del peer-ID riagganciando il collegamento su un ri-annuncio verificato, riconoscendo lo stesso peer sotto il suo nuovo ID ([PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)), e i messaggi diretti a un peer attualmente irraggiungibile ora vengono messi in coda con consegna store-and-forward invece di fallire subito ([PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)). Questo prosegue direttamente dalla copertura del #30 sul lavoro di proof-of-work [NIP-13](/it/topics/nip-13/) e sul gateway mesh-verso-Nostr della v1.6.0.

### MDK v0.9.4 limita il login con firmatario esterno e aggiunge la persistenza delle bozze

[MDK](https://github.com/marmot-protocol/mdk) è l'SDK di riferimento per il protocollo [Marmot](/it/topics/marmot/), il livello di messaggistica MLS-su-Nostr che il #30 ha trattato segnalandone l'adozione della specifica. [v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) limita i passaggi di directory consultiva che un client percorre durante il login con firmatario esterno in [PR #793](https://github.com/marmot-protocol/mdk/pull/793), prevenendo un ciclo di tentativi illimitato quando un firmatario remoto è lento o non risponde. Lo stesso rilascio aggiunge la persistenza delle bozze di messaggio e i collegamenti profilo-sito web in [PR #812](https://github.com/marmot-protocol/mdk/pull/812), proseguendo il lavoro di irrobustimento incrementale che MDK porta avanti da quando ha rilasciato la v0.9.0.

---

## Rilasci taggati

### n_cord v1.1 aggiunge il supporto per NSEC Bunker

[n_cord](https://github.com/0n4t3/n_cord) è un client di chat basato su Nostr ispirato a Discord e IRC. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) aggiunge il supporto per NSEC Bunker [NIP-46](/it/topics/nip-46/) insieme a una correzione di un bug nella gestione delle risposte.

### cdk v0.17.3 aggiunge il supporto per il servizio di wallet NIP-47 su cdk, cdk-nwc e cdk-ffi

[cdk](https://github.com/cashubtc/cdk) è un development kit per Cashu; questo rilascio è per la maggior parte solo Bitcoin/Lightning, ma [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) aggiunge il supporto per il servizio [NIP-47](/it/topics/nip-47/) (Nostr Wallet Connect) con un crate di servizio NWC dedicato, l'integrazione con il wallet, i binding FFI per `cdk-ffi`, e una copertura di test end-to-end, dando ai wallet Cashu costruiti su cdk una superficie Nostr Wallet Connect standard.

### Coop Mobile v0.2.4 migliora Nostr Connect e aggiunge l'importazione ncryptsec1

[Coop Mobile](https://git.reya.su/reya/coop-mobile) è un client di messaggistica privata [NIP-17](/it/topics/nip-17/) per piattaforme mobili. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) migliora il suo flusso [NIP-46](/it/topics/nip-46/) Nostr Connect, corregge un indicatore di caricamento che rimaneva bloccato in modo permanente su alcune connessioni, e aggiunge il supporto all'importazione del formato di chiave cifrata [NIP-49](/it/topics/nip-49/) `ncryptsec1` insieme a una schermata di importazione dell'identità ridisegnata.

### Nmail v0.14.0 arriva su macOS con invio programmato e notifiche push

[Nmail](https://github.com/nogringo/nostr-mail-client) è un client di posta costruito su Nostr; [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) porta l'app su macOS, aggiunge l'invio programmato con una casella Programmati dedicata per i messaggi in coda, e aggiunge le notifiche push. Il rilascio passa anche la risoluzione degli identificatori Nostr della rubrica al resolver [NIP-05](/it/topics/nip-05/) di NDK al posto di un'implementazione su misura.

### Nostrord v2.2.0 aggiunge un interruttore generale per i DM e messaggi diretti più ricchi

[Nostrord](https://github.com/nostrord/nostrord) è un client di chat di gruppo basato su relay [NIP-29](/it/topics/nip-29/) per Android, iOS, web e desktop. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) aggiunge un interruttore generale per disabilitare tutte le funzionalità di messaggistica diretta in una volta ([PR #175](https://github.com/nostrord/nostrord/pull/175)) e rilascia "messaggi diretti più ricchi" ([PR #186](https://github.com/nostrord/nostrord/pull/186)), proseguendo dalla copertura del #30 sul rilascio che consolidava il pool di relay e rilevava i WebSocket zombie.

### Nostr WoT 0.3.86 irrobustisce i backup delle chiavi e le richieste di firma

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) è un'estensione per browser che abbina un'identità Nostr a un wallet Lightning. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) sposta i backup delle chiavi cifrate al formato standard [NIP-49](/it/topics/nip-49/), fa sì che le richieste di firma mostrino l'evento completo e tutti i tag invece di un riepilogo, verifica i dati del relay rispetto alla loro firma, e smette di esporre l'identità attiva al cambio di account. L'estensione elimina anche il permesso `scripting` del browser inutilizzato.

### Keep Android v1.1.8 aggiunge l'onboarding FROST al primo avvio

[Keep](https://github.com/privkeyio/keep-android) è un firmatario Android costruito su frammenti di chiave a soglia FROST. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) aggiunge un flusso al primo avvio che spiega i frammenti di chiave FROST e consente a un nuovo utente di scegliere una politica di firma tra Manuale, Base o Automatica prima che arrivi la prima richiesta di firma, il primo onboarding lato Android per il modello di firma a soglia del crate keep-mobile sottostante.

### Noscall v0.6.0 aggiunge un wallet Cashu e notifiche push basate su relay

[Noscall](https://github.com/sanah9/noscall) è un'app per chiamate audio e video sicure costruita su Nostr. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) aggiunge un wallet Cashu con ambito account con saldi multi-mint, invio e ricezione di ecash, e pagamento e ricezione Lightning con persistenza delle quote. Il rilascio migra anche le notifiche push di Android da Firebase Cloud Messaging a un percorso di consegna basato su relay Nostr tramite UnifiedPush, e migliora l'affidabilità del VoIP di iOS e del push APNs durante i nuovi tentativi di login.

### Kubo rilascia la modalità tablet e le foto nelle chat di gruppo

[Kubo](https://github.com/JeroenOnNostr/kubo) è una piattaforma video Nostr sicura per bambini con curazione del feed tramite Web-of-Trust. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) aggiunge un layout a griglia per tablet opzionale per il feed dei bambini e il supporto all'allegato di foto ai messaggi delle chat di gruppo, oltre a correzioni per il pulsante di registrazione che si nascondeva dietro la tastiera a schermo su Android.

### Nostr Codex Phone v0.2.9 aggiunge richieste ausiliarie per git/diff/lettura di file

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) è una superficie di controllo mobile per un worker locale di assistenza alla programmazione che comunica tramite DM Nostr cifrati. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) aggiunge azioni di strumenti OpenCode mobili, incluse richieste ausiliarie per git, diff, lettura di file, stato e cronologia, miglioramenti al fissaggio e alla ricerca delle sessioni, e un controllo di arresto delle attività, insieme a un wrapper di caricamento cifrato su [Blossom](/it/topics/blossom/) che è stato rilasciato nella precedente v0.2.8.

### GitWorkshop v3.0.3 corregge i ref appena annunciati nell'esploratore di repository, e rilascia la sua prima build Android

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) è un'interfaccia web git-su-Nostr per esplorare e revisionare repository NIP-34. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) corregge le viste di rami, tag, commit ed esplorazione del codice che non riuscivano a risolvere un ref annunciato da un repository dopo che l'esploratore lo aveva già caricato, insieme alla pulizia dei tempi del flusso CI, confermato direttamente rispetto al tag e alla cronologia dei commit. La stessa settimana, GitWorkshop ha pubblicato la sua prima build Android nativa su [Zapstore](https://zapstore.dev), partendo dalla v3.0.0 e raggiungendo la v3.0.3 nel giro di ore; l'interfaccia web rimane l'interfaccia principale, e il pacchetto Android porta per la prima volta su un telefono la stessa esplorazione di repository NIP-34.

### Bitcoin-Safe arriva su Flathub, mettendo in luce il suo plugin Nostr Sync & Chat

[Bitcoin-Safe](https://bitcoin-safe.org) è un wallet Bitcoin ad autocustodia costruito attorno ai flussi di lavoro con firmatari hardware. Il progetto ha [pubblicato un pacchetto su Flathub](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe) questa settimana, il suo primo inserimento in uno store di applicazioni Linux mainstream. Il rilascio su Flathub mette il plugin Sync & Chat di Bitcoin-Safe davanti a un pubblico più ampio: il plugin usa i messaggi diretti [NIP-17](/it/topics/nip-17/), tramite la libreria [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) del progetto, per sincronizzare le etichette del wallet tra i dispositivi di un utente e per inviare e ricevere PSBT per la co-firma multisig remota tra partecipanti fidati. Il livello Nostr stesso è stato rilasciato prima, nella [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0) (2026-06-29), che ha ridisegnato la firma delle transazioni attorno a un tipo di connessione "Share via Chat & Sync" insieme a QR, USB e Bluetooth. La notizia di questa settimana è il pacchetto Flathub che mette quella funzionalità esistente davanti a un pubblico Linux mainstream per la prima volta.

---

## Modifiche non rilasciate

### Amethyst consente agli account di assegnare soprannomi ai contatti con schede NIP-85 cifrate

Oltre all'[implementazione di Concord](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) trattata sopra, Amethyst ha integrato altre 54 PR nell'ultima settimana. La principale tra queste è [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548), che consente a un account di assegnare un soprannome a qualsiasi altro utente pubblicando la propria scheda di contatto kind 30382 [NIP-85](/it/topics/nip-85/) su di lui. Il soprannome, una nota privata, e qualsiasi mappatura personalizzata di codici brevi di emoji [NIP-30](/it/topics/nip-30/) risiedono all'interno del contenuto cifrato con [NIP-44](/it/topics/nip-44/) della scheda, così che solo l'account firmatario possa leggerli, e le schede si sincronizzano attraverso il set esteso di relay outbox dell'account al login e in modo incrementale in seguito. Feed, chat e menzioni rendono il soprannome al posto del nome visualizzato pubblico, con una scheda del soprannome toccabile nella pagina del profilo sopra il vero nome dell'utente.

### Zap Cooking rilascia la Fase 3 di My Kitchen e corregge un bug di quorum del pool NDK

[Zap Cooking](https://github.com/zapcooking/frontend) è un'app di condivisione di ricette e comunità culinaria costruita su Nostr. Ha integrato 43 PR proseguendo la sua funzionalità di pianificazione dei pasti "My Kitchen", introducendo in questa fase la generazione di liste della spesa, un selettore di ricette e una griglia settimanale del pianificatore. Lo stesso insieme di modifiche corregge un bug di prontezza del quorum del pool di connessioni di [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit) che poteva lasciare le letture dei relay in attesa oltre il punto in cui un quorum di relay aveva già risposto.

### Kehto trasmette le letture di outbox prima della scoperta dei relay

[Kehto](https://github.com/kehto/web) è un runtime web iniziale per applet Nostr [NIP-5D](/it/topics/nip-5d/), o "napplet". Ha integrato 26 PR. [PR #193](https://github.com/kehto/web/pull/193) corregge le letture di outbox che in precedenza attendevano il completamento del caricamento della lista di relay [NIP-65](/it/topics/nip-65/) prima di aprire qualsiasi relay, così che un caricamento della lista di relay che non si risolveva mai poteva bloccare sia la consegna degli eventi sia i timeout delle query; la correzione apre immediatamente gli hint di relay validati e trasmette i risultati man mano che vengono scoperti i relay di scrittura. Una seconda modifica ([PR #196](https://github.com/kehto/web/pull/196)) allinea la pagina di audit dell'identità del progetto con NAP-SHELL, il contratto di ciclo di vita della piattaforma Napplet, parte dello stesso lavoro di allineamento del protocollo visibile altrove nel rilascio `napplet/web` di questa settimana.

### Wired e TAO aggiungono la condivisione dei ricavi per i creatori con NIP-57

[Wired](https://github.com/smolgrrr/Wired) e [TAO](https://github.com/smolgrrr/TAO) sono client social gemelli orientati alla libertà di parola costruiti su Nostr, che condividono la stessa lista di PR; entrambi hanno integrato [PR #121](https://github.com/smolgrrr/Wired/pull/121), che implementa la condivisione dei ricavi per i creatori [NIP-57](/it/topics/nip-57/) affinché gli zap inviati a un post possano dividersi automaticamente tra collaboratori oltre all'autore originale. Questo prosegue la copertura del #30 sulla coppia che alzava il proprio segnale di proof-of-work a 21 bit come lavoro non rilasciato.

### Conduit Mono ricostruisce la casella degli ordini del commerciante attorno al checkout come ospite effimero

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) è un protocollo di marketplace adiacente agli annunci classificati [NIP-99](/it/topics/nip-99/). [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) aggiunge il checkout come ospite usando una chiave effimera generata dal browser: l'ospite invia un ordine cifrato e un rapporto di pagamento al commerciante usando quella chiave monouso, e il commerciante dà seguito fuori banda per telefono o email, così che l'acquirente non abbia mai bisogno di un'identità di casella durevole. [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) ricostruisce la casella degli ordini del commerciante attorno a un unico modello di stato dell'ordine condiviso, separando i ruoli di acquirente e commerciante e richiedendo un codice di tracciamento e un corriere prima che un ordine fisico o misto possa passare a spedito. Il flusso di checkout del progetto si basa sui messaggi privati [NIP-17](/it/topics/nip-17/), sulla cifratura [NIP-44](/it/topics/nip-44/) e sul gift wrap [NIP-59](/it/topics/nip-59/). Il [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) di questa settimana copre le convenzioni di [Gamma Markets](/it/topics/gamma-markets/) verso cui questo stesso problema di stato dell'ordine si dirige.

### Buzz irrobustisce il provisioning del creatore di canale attorno al kind 39002

[Buzz](https://github.com/block/buzz) è una piattaforma di comunicazione a mente collettiva che collega agenti IA e umani su Nostr. Ha integrato 240 PR nell'ultima settimana, proseguendo il suo arco di irrobustimento del livello di relay dalla copertura del #30 sulle metriche di turno degli agenti kind 44200. La correzione di questa settimana ([PR #1830](https://github.com/block/buzz/pull/1830)) tratta il creatore di un canale come membro prima che venga eseguita la logica di provisioning del canale kind 39002, chiudendo una race condition in cui il canale del creatore stesso poteva rifiutarlo durante la configurazione.

### Nostr Docs adotta un firmatario NIP-49 con account multipli e accoppiamento QR

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) è un'applicazione di documenti collaborativi nativa di Nostr. Ha integrato 5 PR, quella notevole ([PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)) adottando il pacchetto `@formstr/signer` per l'autenticazione completa [NIP-49](/it/topics/nip-49/) con cambio tra account multipli e accoppiamento QR, sostituendo un percorso di firma su misura precedente.

### Anche rilasciato

Correzioni minori di interoperabilità dei firmatari e di affidabilità sono arrivate in diversi progetti tracciati nell'ultima settimana senza superficie nuova sufficiente per un proprio paragrafo: [ngit-cli](https://github.com/DanConwayDev/ngit-cli), un client da riga di comando per un'alternativa a GitHub basata su Nostr, rilascia [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3) facendo sì che `ngit init` dia indicazioni di configurazione concrete invece di richiedere ripetutamente un nsec; [Manent](https://github.com/dtonon/manent), un'app privata di note e file cifrati costruita su Nostr, rilascia [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1) correggendo il login con firmatario Android che si rompeva quando Amber restituisce un pubkey esadecimale e migliorando lo scorrimento del login bunker; [NoorNote](https://github.com/77elements/noornote), un client Nostr snello e privo di servizi Google, rilascia [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8) correggendo le notifiche mancate dei gruppi Nostrord e aggiungendo un interruttore di avviso per i propri post; [Bray](https://github.com/forgesworn/bray), un server MCP Nostr consapevole della fiducia per agenti IA e umani, rilascia [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0) inviando i metadati del nome del client alla connessione bunker [NIP-46](/it/topics/nip-46/); [Lumilumi](https://github.com/TsukemonoGit/lumilumi), un client web Nostr, memorizza le liste di relay [NIP-65](/it/topics/nip-65/) nello storage locale come fallback offline; [Earthly](https://github.com/moogmodular/earthly), un'app di città e comunità locale basata su Nostr, aggiunge la ricerca geografica [NIP-50](/it/topics/nip-50/); e [lnbits](https://github.com/lnbits/lnbits), un sistema di wallet e account Lightning gratuito e open-source, rilascia [PR #3925](https://github.com/lnbits/lnbits/pull/3925) rendendo `send_nostr_dm` non bloccante all'interno di un rilascio per il resto focalizzato su Lightning.

---

## Appena tracciati e scoperti

### OpenDiscord v1.0.1 debutta come client in stile Discord su Nostr

[OpenDiscord](https://github.com/sofia-gros/open-discord) è un client con server e canali in stile Discord costruito su Nostr con permessi basati sui ruoli e lobby vocali WebRTC/SFU. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) è il primo rilascio con installer taggato del progetto.

### Auditable Voting v0.1.140 allinea i ruoli di organizzatore, votante e proxy di audit

[Auditable Voting](https://github.com/tidley/auditable-voting) è uno shell di voto solo client su Nostr. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) allinea i ruoli di organizzatore, votante e proxy di audit con l'esatto evento di definizione del questionario pubblico firmato dall'organizzatore, chiudendo una lacuna in cui un proxy di audit poteva agire su account generati obsoleti o su uno stato persistito da un worker o organizzatore diverso.

### Cambium v0.3.2 si abbina a Heartwood come firmatario NIP-55 senza chiavi

[Cambium](https://github.com/forgesworn/cambium) è la scelta Discovery di questo numero: un firmatario Android [NIP-55](/it/topics/nip-55/) che non conserva alcun materiale di chiave privata proprio, facendo da proxy per ogni richiesta di firma tramite [NIP-46](/it/topics/nip-46/) verso un firmatario hardware Heartwood compagno. Il progetto condivide l'organizzazione GitHub `forgesworn` con il progetto tracciato Bray, e Heartwood stesso è stato trattato nel #30 quando ha rilasciato il ponte di firma relay-verso-seriale con cui ora dialoga il lato Android di Cambium. [v0.3.2](https://github.com/forgesworn/cambium) rifinisce il foglio di approvazione per avvisare dal vivo quando l'identità selezionata differisce dal collegamento esistente dell'app e sposta le scritture del registro di attività in un'unica coda non bloccante.

### Anche in lancio questa settimana: echoes, Dispatch e Linky

Tre altri lanci meritano una menzione questa settimana. [echoes](https://github.com/Lwb89dev/echoes) è un'app di note offline-first e cifrata end-to-end che si sincronizza privatamente su Nostr. [Dispatch](https://github.com/freecritter/dispatch) è un organizzatore di viaggi local-first in cui ogni salvataggio è cifrato con [NIP-44](/it/topics/nip-44/) e sottoposto a backup su Nostr con una chiave dedicata e non collegabile, e il suo rilascio [v0.3.0](https://github.com/freecritter/dispatch) aggiunge il login Amber [NIP-55](/it/topics/nip-55/) affinché l'app non tocchi mai direttamente la chiave privata dell'utente. [Linky](https://github.com/hynek-jina/linky) combina contatti e DM Nostr con pagamenti Lightning e Cashu in un'unica progressive web app.

---

## Lavoro di protocollo e aggiornamenti dei NIP

Nessuna PR integrata nel [repository dei NIP](https://github.com/nostr-protocol/nips) nell'ultima settimana. Sono state aperte sei proposte.

### Aperta: kind:10011 set di follow preferiti

[PR #2413](https://github.com/nostr-protocol/nips/pull/2413), di fiatjaf, aggiunge i set di follow preferiti kind:10011. Rispecchia il modello esistente in cui kind:10012 (set di relay preferiti) contiene tag `a` che puntano a set di relay kind:30002, estendendo lo stesso meccanismo di preferenza ai set di follow kind:30000 affinché un client possa segnare una lista di follow curata senza sostituire la propria lista di contatti.

### Aperta: unità cifrata privata che estende NIP-4E

[PR #2412](https://github.com/nostr-protocol/nips/pull/2412), del team Form*, propone un evento Metadata generico, kind 34578, distinto da un tag identificatore `d` e da un tag di sottotipo `t`, insieme a un file system cifrato privato costruito su di esso che è già implementato nel client Form* Drive del progetto, ancora sperimentale. Un record di file è un evento Metadata con `t=files`: i blob dei file risiedono su server [Blossom](/it/topics/blossom/) mentre solo un indice cifrato risiede sui relay, e ogni chunk di file ottiene la propria coppia di chiavi effimera con cifratura [NIP-44](/it/topics/nip-44/) v2 derivata tramite HKDF. Un evento compagno di Chiave di Cifratura Disaccoppiata contiene un'unica chiave simmetrica valida per l'intera unità contro cui i metadati di ogni file vengono decifrati, e si basa esplicitamente su [NIP-4E](/it/topics/nip-4e/), la bozza di astrazione dello storage ancora aperta di fiatjaf ([PR #1647](https://github.com/nostr-protocol/nips/pull/1647), aperta da dicembre 2024).

Quell'unica chiave valida per l'intera unità significa che una chiave trapelata espone i metadati di ogni file dell'unità, non solo di uno, poiché le coppie di chiavi effimere per file variano solo la chiave di cifratura del chunk, non la chiave di decifratura dei metadati; non esiste ancora alcun percorso di rotazione o revoca oltre alla pubblicazione di un nuovo evento Metadata che avverte che gli eventi più vecchi potrebbero andare persi. Una seconda proposta, più ristretta, raggiunge la stessa idea sottostante di NIP-4E da un'angolazione diversa: [PR #2361](https://github.com/nostr-protocol/nips/pull/2361), di fiatjaf, disaccoppia le chiavi di identità e cifratura all'interno della messaggistica [NIP-17](/it/topics/nip-17/) nello specifico, aperta dal 1° giugno. Entrambe le PR non sono integrate, lasciando questo un angolo attivo e conteso dello spazio di progettazione. Form* dice che il client Drive è sperimentale con un aggiornamento in arrivo a breve.

### Aperta: NIP-DA condivisione privata di dati con permessi

[PR #2411](https://github.com/nostr-protocol/nips/pull/2411), di JAFairweather, è una nuova bozza NIP-DA per la condivisione privata di dati con permessi attraverso concessioni di dati con ambito. Ogni utente mantiene un record cifrato e autoritativo per ambito sui relay, e l'accesso viene concesso consegnando privatamente la chiave simmetrica di quell'ambito dentro un gift wrap [NIP-59](/it/topics/nip-59/), così che i relay memorizzino solo testo cifrato e non sappiano mai chi ha concesso l'accesso a chi; una revoca è semplicemente una rotazione di chiave, senza bisogno di riscrivere la copia di ogni consumatore. L'autore la posiziona come distinta dai DM [NIP-17](/it/topics/nip-17/) (che possono portare uno snapshot di dati ma non aggiornamenti dal vivo né revoca) e dalle liste private NIP-51 (che non portano materiale di chiave), e cita due implementazioni indipendenti, una libreria di riferimento in JavaScript e una CLI in Go su go-nostr, testate in modo incrociato contro relay.damus.io, nos.lol e relay.primal.net.

### Aperta: kind per pacchetti di sticker 10031 e 30031

[PR #2410](https://github.com/nostr-protocol/nips/pull/2410), di vincenzopalazzo, registra il kind 30031 (pacchetti di sticker indirizzabili) e il kind 10031 (la lista di pacchetti di sticker di un utente) nella tabella Event Kinds, specificati dal formato "Sonar Stickers" che [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) rilascia questa settimana. I kind si collocano deliberatamente uno slot sopra i kind di emoji personalizzati [NIP-30](/it/topics/nip-30/) 30030 e 10030 affinché un client non possa scambiare un pacchetto di sticker per un set di emoji; i byte dell'immagine degli sticker risiedono su server HTTPS compatibili con [Blossom](/it/topics/blossom/), e i riferimenti agli sticker inviati portano un hash in testo semplice affinché un pacchetto indirizzabile modificato non possa cambiare silenziosamente l'aspetto degli sticker già inviati in vecchi messaggi. Una PR compagna registra gli stessi kind nel progetto separato `registry-of-kinds`.

### Aperta: fissaggio dei messaggi NIP-29 con kind:9010 e kind:39005

[PR #2379](https://github.com/nostr-protocol/nips/pull/2379), di Anderson-Juhasc, aggiunge il fissaggio dei messaggi ai gruppi basati su relay [NIP-29](/it/topics/nip-29/): kind:9010 `update-pin-list` è un evento di moderazione che porta la lista completa degli eventi fissati come tag `e` in ordine di visualizzazione, così che un singolo evento possa fissare, rimuovere dal fissaggio, riordinare o azzerare il set fissato, e kind:39005 è uno specchio generato dal relay che espone l'ultima lista accettata. Il design sostituisce un precedente approccio a coppie aggiungi/rimuovi di [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) dopo il feedback della revisione, e sceglie i numeri di kind 9010/39005 perché 9009 e 39003 sono nel frattempo stati rivendicati da `create-invite` e dai ruoli di gruppo. Anderson-Juhasc mantiene anche [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages), la cui [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) viene rilasciata questa stessa settimana.

### Aperta: ristrutturazione della scoperta di relay NIP-66

[PR #2241](https://github.com/nostr-protocol/nips/pull/2241), di VincenzoImp, è una ristrutturazione sostanziale della scoperta di relay [NIP-66](/it/topics/nip-66/). Sostituisce la prosa vaga di "Altri tag includono" con una sezione strutturata di Tag Indicizzati, aggiunge un tag `W` che rispecchia il campo `attributes` di NIP-11 per il filtraggio della scoperta di relay, aggiunge un tag di etichetta `l` che usa spazi dei nomi standardizzati (`ISO-639-1`, `ISO-3166-1`, `IANA-asn`, `IANA-tz`, `nip66.label.city`), e organizza i tag di RTT, SSL/TLS, rete, geografici, DNS e HTTP in sezioni dedicate insieme a una nuova tabella di Tipi di Verifica. Corregge anche eventi di esempio rotti che avevano nomi di campo errati, un `kind` mancante e nomi di tipo di verifica non validi, e chiude la [issue #2171](https://github.com/nostr-protocol/nips/issues/2171). Tutte le modifiche restano retrocompatibili poiché ogni tag aggiunto è opzionale.

---

## NIP Deep Dive: NIP-99 e l'estensione di commercio Gamma Markets

[NIP-15](/it/topics/nip-15/), la specifica originale del Marketplace Nostr, è ormai legacy: modellava un banco del commerciante (kind 30017) con i prodotti (kind 30018) archiviati sotto di esso, e i client che un tempo ci giravano sopra, Shopstr tra questi, sono da allora passati agli annunci classificati [NIP-99](/it/topics/nip-99/) come specifica attiva. NIP-99 in sé è un singolo evento indirizzabile, kind 30402 per un annuncio attivo o kind 30403 per una bozza, senza alcun banco da creare prima. Lascia indefinito tutto ciò che va oltre l'annuncio: costo di spedizione, stato dell'ordine, ricevute, recensioni, e un modo per raggruppare più annunci sotto un'unica vetrina, esattamente le parti di NIP-15 che non sono mai state trasferite. [Gamma Markets](/it/topics/gamma-markets/) colma quella lacuna, ed è il livello di commercio moderno che vale la pena capire oggi.

### La lacuna che NIP-99 lascia aperta

Il campo `content` di un annuncio NIP-99 porta una descrizione in Markdown, `price` e `location` risiedono direttamente sull'evento, e i tag `t` lo rendono ricercabile come contenuto hashtag ordinario. Poiché è indirizzabile sulla tupla pubkey, kind e tag `d`, un venditore modifica un annuncio sul posto pubblicando una nuova versione con lo stesso tag `d`:

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

Questa è l'intera specifica: un annuncio classificato firmato e aggiornabile. Ogni client che implementa NIP-99 per un e-commerce reale, oltre a un classificato occasionale, ha finito per inventare le proprie convenzioni private per spedizione, messaggi d'ordine e recensioni. Due client NIP-99 potevano ciascuno rendere correttamente un annuncio e comunque non avere alcun modo condiviso di completare un checkout tra loro.

### Gamma Markets: standardizzare ciò che NIP-99 ha lasciato fuori

Gamma Markets è il nome che un gruppo di lavoro di sviluppatori di marketplace Nostr, i team dietro Shopstr, Cypher, Plebeian Market e Conduit Market, ha dato a un insieme condiviso di convenzioni di e-commerce costruite sopra l'evento kind 30402 esistente di NIP-99. La specifica è collegata dal documento canonico di NIP-99 tramite [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) e mantenuta nel proprio repository, [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec).

Gamma Markets aggiunge due kind autonomi adiacenti agli annunci. Il kind 30405 raggruppa più annunci in una collezione di prodotti, referenziando ciascuno con un tag `a` esplicito:

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Il kind 30406 definisce un'opzione di spedizione con prezzi per paese e regole di costo opzionali basate su peso o distanza:

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

La creazione degli ordini, le richieste di pagamento, gli aggiornamenti di stato e spedizione, e le ricevute di pagamento viaggiano tutti come normali messaggi privati avvolti con gift-wrap [NIP-17](/it/topics/nip-17/), suddivisi in tre kind per ruolo, non ri-avvolgendo il trasporto: il kind 14 porta la comunicazione libera tra acquirente e commerciante, il kind 16 porta ogni transizione di stato dell'ordine (un tag `type` da 1 a 4 segna creazione dell'ordine, richiesta di pagamento, aggiornamento di stato o aggiornamento di spedizione), e il kind 17 porta la ricevuta di pagamento dell'acquirente. Un messaggio di creazione dell'ordine appare così prima del gift-wrapping:

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Valutare un acquisto completato è un kind indirizzabile separato, 31555, che punta all'annuncio che recensisce:

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

Far viaggiare i messaggi d'ordine su NIP-17 significa che un checkout di Gamma Markets usa lo stesso trasporto di messaggi privati che i client già rilasciano per i DM, invece di un kind di messaggio d'ordine su misura.

La scelta di progettazione centrale della specifica è che nulla si eredita a cascata. Un annuncio che appartiene a una collezione la referenzia esplicitamente con un tag `a` invece di ereditare automaticamente le opzioni di spedizione o la descrizione della collezione, e un'opzione di spedizione che un annuncio usa viene referenziata nello stesso modo esplicito. Questa è un'inversione deliberata del modello a banco di NIP-15, dove un prodotto ereditava silenziosamente qualunque valuta e tabella di spedizione definisse il suo banco genitore. Il compromesso è un tagging più esplicito su ogni annuncio, in cambio del fatto che la configurazione completa di un annuncio sia sempre leggibile dall'evento stesso, senza alcun oggetto genitore da risolvere prima.

### Dove questo si manifesta nella pratica

Il lavoro di [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) di questa settimana si colloca nello stesso territorio di messaggi d'ordine che Gamma Markets standardizza: il checkout come ospite con chiave effimera di [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) e la ricostruzione della casella degli ordini del commerciante di [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) risolvono entrambi il problema di stato dell'ordine acquirente/commerciante che i messaggi kind 14, 16 e 17 di Gamma Markets formalizzano; Conduit Mono esegue il proprio modello di stato dell'ordine accanto a quei kind, senza adottarli direttamente. Shopstr, uno dei quattro progetti che hanno scritto la specifica, ha tenuto in movimento anche il proprio impianto di commercio nell'ultima settimana: [PR #568](https://github.com/shopstr-eng/shopstr/pull/568) estrae la logica di gift-wrap NIP-17 duplicata in un modulo condiviso, e [PR #567](https://github.com/shopstr-eng/shopstr/pull/567) porta il suo parser di autenticazione HTTP [NIP-98](/it/topics/nip-98/) a una copertura di test completa, manutenzione esattamente sui livelli di messaggistica e autenticazione da cui un flusso d'ordine di Gamma Markets dipende per raggiungere acquirente e commerciante in sicurezza.

NIP-15 ha perso il ruolo di vetrina standardizzando un banco e un prodotto, e poi lasciando pagamenti, spedizione, recensioni e stato dell'ordine come problema dell'applicazione. Gamma Markets colma la maggior parte di quella superficie mancante senza toccare la forma a singolo annuncio di NIP-99, costruendo sullo stack di DM esistente di Nostr, NIP-17, invece di inventare un nuovo livello di messaggistica.

---

Questo è tutto per questa settimana. Stai costruendo qualcosa o hai notizie da condividere? Scrivici via DM NIP-17 o trovaci su Nostr.
