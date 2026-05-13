---
title: 'Nostr Compass #21'
date: 2026-05-06
publishDate: 2026-05-06
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-06-newsletter.md
translationDate: 2026-05-13
description: 'Marmot Protocol pubblica MDK 0.8.0 con le primitive di notifica MIP-05 e i pacchetti di chiavi indirizzabili; LaWallet NWC pubblica v0.10.0 con il monorepo completo, dashboard admin, portafoglio utente finale e un nuovo schema LightningAddress verso NWCConnection; Amethyst Nests si stabilizza con la riconnessione dei relay, le sottoscrizioni lifecycle-aware, la continuità audio durante il refresh JWT e indicatori di parlante visibili; ngit pubblica v2.4.2 e v2.4.3 correggendo il rilevamento del server GRASP e il filtraggio degli eventi di stato multi-remote; GRAIN v0.5.4 aggiunge hardening per la produzione; Mostro Core v0.10.1 aggiunge artefatti di release firmati con PGP; Clave v0.2.0 introduce il supporto multi-account su iOS; nostream aggiunge il supporto al relay del Marmot Protocol e le reazioni NIP-25; Sprout pubblica Desktop v0.0.4 e v0.0.5 con l\'autenticazione agente NIP-OA e un sidecar di pairing effimero; Angor 0.2.21 pubblica flussi applicativi compatti; Routstrd integra Hermes per i client daemon; micro-vpn-ansible entra nel set di repository NIP-34 tracciati; le discussioni NIP portano alla luce una bozza di mercato dell\'hashrate senza broker, una proposta di Curated Feeds, un NIP per i colori del profilo e una traccia di identità ancorata a Namecoin. Due approfondimenti NIP coprono NIP-34 (git stuff) e NIP-53 (Live Activities).'
---

Bentornati a Nostr Compass, la vostra guida settimanale all'ecosistema Nostr.

**Questa settimana:** Marmot Protocol pubblica MDK 0.8.0 con le prime primitive di notifica MIP-05, pacchetti di chiavi NIP-51 indirizzabili e una revisione della sicurezza rafforzata. LaWallet NWC pubblica v0.10.0, la versione più importante dalla copertura di OpenSats, con una dashboard admin completa, portafoglio utente, registro delle attività end-to-end e un nuovo schema LightningAddress 1→N e NWCConnection. Amethyst porta uno sprint di stabilizzazione di Nests con l'eliminazione dei gap audio durante il refresh JWT, sottoscrizioni di dati chiave lifecycle-aware, riconnessione keep-alive dei relay e un indicatore animato del parlante attivo. ngit pubblica v2.4.2 e v2.4.3 correggendo il rilevamento del server GRASP per le submission di PR e il filtraggio degli eventi di stato multi-remote. GRAIN pubblica v0.5.4 con hardening per la produzione e una correzione silenziosa di perdita di dati nel Docker quick-start. Mostro Core pubblica v0.10.1 con artefatti di release firmati con PGP. Clave lancia v0.2.0 con supporto multi-account su iOS.

## Storie principali

### MDK 0.8.0 aggiunge le primitive di notifica MIP-05 e i pacchetti di chiavi indirizzabili

MDK, la libreria Rust centrale per il protocollo Marmot, ha pubblicato v0.8.0 il 4 maggio. Questa versione introduce i primi blocchi costruttivi di notifica MIP-05, sposta i pacchetti di chiavi MIP-00 verso eventi indirizzabili così da poter sostituire il pacchetto chiavi di un utente in-place, migliora la compatibilità dei gruppi a versione mista, espande la copertura UniFFI per i binding mobile e rafforza i percorsi di validazione attorno alle azioni admin, commit, storage, limiti di cifratura e gestione dei replay. Le primitive MIP-05 includono helper di indice foglia aggiunti in PR #235, che forniscono ai client downstream informazioni sufficienti per consegnare notifiche push per destinatario senza rivelare la struttura del gruppo. PR #273 ripristina la pubblicazione di mdk-core su crates.io, e PR #269 espone il modulo test_util dietro una feature Cargo test-utils così che le suite di test client esterne possano condividere il test harness di Marmot.

### LaWallet NWC v0.10.0 pubblica il monorepo completo e il portafoglio utente finale

LaWallet NWC, l'implementazione NIP-47 Nostr Wallet Connect del team LaWallet, ha pubblicato v0.10.0 il 30 aprile. È la versione più importante da quando il progetto ha ricevuto il finanziamento OpenSats. Include il monorepo completo, la dashboard admin completa, un portafoglio utente finale, un registro attività end-to-end, branding dinamico e il nuovo schema LightningAddress 1→N e NWCConnection. Il portafoglio per gli utenti finali, pubblicato in PR #191, copre l'onboarding, la home, invio/ricezione, scansione, valute, un feed attività e una cache offline.

### Amethyst stabilizza Nests con keep-alive, resilienza JWT e sottoscrizioni lifecycle

Amethyst, il client Android ricco di funzionalità, ha continuato il lavoro sulle stanze audio NIP-53 Nests con uno sprint di stabilizzazione incentrato sui modi di guasto che interrompevano le chiamate in produzione. La correzione del gap audio in PR #2733 sovrappone la nuova acquisizione delle credenziali con il flusso attivo durante il refresh JWT. Un nuovo meccanismo keep-alive in PR #2730 riconnette i relay disconnessi senza richiedere un'azione manuale dell'utente, e PR #2728 sostituisce la vecchia KeyDataSourceSubscription con LifecycleAwareKeyDataSourceSubscription. PR #2724 aggiunge un indicatore ad anello esterno animato che evidenzia il parlante attivo nelle sessioni multi-parlante.

### ngit v2.4.2 e v2.4.3 correggono il rilevamento del server GRASP e gli eventi di stato multi-remote

ngit, lo strumento da riga di comando e plugin git per la collaborazione NIP-34, ha pubblicato v2.4.2 il 28 aprile e v2.4.3 il 1° maggio. v2.4.2 corregge una mancata corrispondenza di normalizzazione URL in cui i repo_grasps contenevano hostname normalizzati ma il confronto veniva effettuato rispetto agli URL di clone completi. v2.4.3 corregge un'ambiguità negli eventi di stato che emergeva quando un repository ha più remote nostr:// che condividono lo stesso identificatore.

### GRAIN v0.5.4 aggiunge hardening per la produzione e corregge una perdita di dati silenziosa

GRAIN, il relay Nostr e la libreria client basati su Go, ha pubblicato v0.5.4 il 30 aprile. La versione raccoglie sei correzioni accumulate dalla v0.5.3, incluso un bug di perdita di dati silenziosa nel Docker quick-start che in precedenza eliminava eventi al riavvio del container, e un bug di correttezza nel livello di storage nelle letture di eventi indirizzabili.

### Mostro Core v0.10.1 aggiunge artefatti di release firmati con PGP

Mostro Core, la libreria Rust che fornisce funzionalità peer-to-peer per il daemon Mostro, ha pubblicato v0.10.1 il 28 aprile. La nuova versione aggiunge artefatti di release firmati con PGP e un flusso di verifica della release così che i packager downstream possano confermare la provenienza degli artefatti.

## Release con tag

### Clave v0.2.0 lancia il multi-account su iOS con firma NIP-46 (Nostr Connect)

Clave, l'app iOS per la firma remota NIP-46, ha pubblicato v0.2.0 il 5 maggio. Il principale aggiornamento introduce il supporto multi-account: Clave può ora gestire fino a quattro account su un unico dispositivo, con un selettore one-tap e isolamento per account. PR #23 aggiunge il codice iOS per il multi-account, e PR #22 aggiunge un campo signer_pubkey al payload APNs così che il dispositivo sappia a quale account appartiene una richiesta di firma remota.

### Wisp pubblica v1.0.3 → v1.0.5 con lavori di stabilità

Wisp, il client Android, ha pubblicato v1.0.3, v1.0.4 e v1.0.5 il 4 maggio con lavori di stabilità. PR #506 aggiunge Thumbhash per le anteprime sfocate delle immagini mentre i media completi si caricano, e PR #514 riduce lo scatto nel cambio delle schede inferiori.

### Amber 6.1.0-pre1 pubblica correzioni di layout e stabilità

Amber, l'app di firma Android per NIP-55 e NIP-46, ha pubblicato v6.1.0-pre1 con una revisione del layout nel flusso di connessione delle nuove app e diverse correzioni di crash. PR #416 corregge il layout di ActivityStatsBar e i problemi di overflow del testo.

### Routstr Core v0.4.3 migliora pagamento, rimborso e reportistica sull'utilizzo

Routstr Core ha pubblicato v0.4.3 come pre-release il 1° maggio con miglioramenti alla gestione dei pagamenti e dei rimborsi, al tracciamento dei costi e alla reportistica sull'utilizzo.

### Nostria v3.1.37 fino a v3.1.41 aggiungono i segnalibri Web e un tema Auto

Nostria, il client Nostr multi-piattaforma, ha pubblicato v3.1.37 fino a v3.1.41 aggiungendo il supporto ai segnalibri Web NIP-B0, un tema Auto che segue le impostazioni del dispositivo e la visualizzazione PDF integrata nell'app.

### NoorNote v0.8.9 corregge la schermata vuota al primo avvio sul desktop

NoorNote ha pubblicato v0.8.9 il 28 aprile correggendo un bug di schermata vuota al primo avvio dell'app desktop.

### Kubo v0.3.4 fino a v0.4.1 pubblicano una piattaforma video Nostr a misura di bambino con controlli parentali e curation del feed tramite Web of Trust

Kubo, una piattaforma video a misura di bambino su Nostr, ha pubblicato v0.3.4 fino a v0.4.1 il 4 e 5 maggio. Ogni bambino riceve una coppia di chiavi Nostr separata e un feed incentrato sui video dove i genitori controllano i limiti di tempo (da 15 a 180 minuti al giorno), le finestre temporali consentite e la visibilità delle azioni sui post.

## Modifiche non rilasciate

### Sprout pubblica Desktop v0.0.4 e v0.0.5 con autenticazione agente NIP-OA e il sidecar pair-relay

Sprout, il client Nostr di Block con relay integrato, ha pubblicato Desktop v0.0.4 il 5 maggio e v0.0.5 il 6 maggio. PR #471 integra l'autenticazione agente NIP-OA nel flusso di membership NIP-43 del relay così che un agente autonomo possa dimostrare che una specifica chiave pubblica umana ha autorizzato le sue azioni. Un nuovo relay sidecar effimero per il pairing di dispositivi NIP-AB arriva in PR #467 come sprout-pair-relay.

### nostream aggiunge il supporto relay Marmot e le reazioni NIP-25

nostream, l'implementazione relay Node.js, ha integrato il supporto relay Marmot Protocol che copre i MIP da 00 a 03 in PR #602, il supporto alle reazioni NIP-25 in PR #589 e la corrispondenza del prefisso geohash per i filtri #g in PR #586.

### strfry aggiunge l'osservabilità per connessione e riduce il tetto nofiles

strfry, il relay Nostr in C++, ha integrato 14 PR che puntano all'osservabilità. PR #218 aggiunge l'osservabilità degli outbound in attesa per connessione e un cap di back-pressure configurabile. PR #224 rimuove le allocazioni heap di std::function dal fanout del monitor per evento.

### Damus sostituisce i GIF Tenor con un proxy Purple e pubblica la UX di compattazione

Damus ha integrato PR #3737 sostituendo l'integrazione GIF Tenor con un proxy Damus Purple.

### Primal Android migliora Explore, gli avvisi e il badge di verifica NIP-05

Primal Android ha integrato PR #1043 correggendo un badge di verifica NIP-05 lampeggiante per gli utenti con identificatori _@domain.

### Alby Hub aggiunge i pagamenti NWC dalle connessioni delle app

Alby Hub ha integrato PR #2267 che consente i pagamenti dalle connessioni delle app.

### routstrd-auth: un Routstrd Docker per team con autenticazione NIP-98 e RBAC npub

routstrd-auth, creato il 27 aprile, è una variante Docker di Routstrd per i deployment in team multi-utente con controllo degli accessi basato sui ruoli npub e autenticazione HTTP NIP-98.

### Routstrd integra Hermes per i client daemon e la modalità remota

Routstrd ha integrato PR #22 aggiungendo l'integrazione con Hermes Agent così che il file di configurazione dell'agente venga popolato con i provider di modelli e le chiavi API che Routstrd scopre tramite Nostr.

### whitenoise-rs pubblica l'isolamento del database per account e gli aggiornamenti delle proposte

whitenoise-rs ha integrato PR #796 spostando le tabelle di proiezione dei messaggi in database per account, e PR #791 aggiunge gli aggiornamenti delle proposte così che i gruppi possano estendere le funzionalità con nuovi tipi di proposta.

### Angor 0.2.21 pubblica flussi applicativi compatti con hardening del provider di chiavi e del cambio rete

Angor ha pubblicato 0.2.21 il 6 maggio con miglioramenti alle performance del design mobile, flussi applicativi compatti e un provider di chiavi sicuro.

## Nuovi tracciati e scoperti

### BitMacro Signer: un bunker NIP-46 auto-ospitato con cifratura delle chiavi lato client

BitMacro Signer è uno strumento di firma Nostr auto-ospitato che utilizza il modello bunker NIP-46. Le chiavi vengono cifrate lato client prima della memorizzazione così che il server non detenga mai testo in chiaro.

La scoperta di repository NIP-34 ha portato alla luce 26 nuovi annunci di repository questa settimana, di cui quattro si distinguono:

### gnostr: un'implementazione git costruita direttamente su Nostr

gnostr è un'implementazione git costruita direttamente su Nostr, che fornisce i propri comandi di albero di lavoro come client di controllo versione nativo Nostr sviluppato da zero.

### nostr-archive: una specifica di archivio content-addressed su Nostr e Blossom

nostr-archive è una specifica bozza e un'implementazione di riferimento per archivi content-addressed su Nostr e Blossom.

### flower-cache: un server di cache Blossom locale

flower-cache è un server di cache Blossom locale, utile per i client che desiderano un mirror locale attivo del set di blob di un server Blossom remoto.

### micro-vpn-ansible: playbook Ansible per il deployment VPN tramite NIP-34

micro-vpn-ansible è una piccola raccolta di playbook Ansible per il deployment di una micro VPN, ospitata come repository NIP-34.

## Lavori sul protocollo

### Aggiornamenti NIP

- Un mercato dell'hashrate senza broker su Nostr (proposta bozza): Una bozza di NIP anonima che sostiene che gli attuali attori del mercato dell'hashrate sono broker custodiali che richiedono il KYC agli utenti. Propone un mercato P2P dell'hashrate sugli eventi Nostr.
- Curated Feeds: un'alternativa più semplice ai feed DVM (proposta bozza): Sostiene che i DVM NIP-90 sono troppo pesanti per la curation semplice dei feed; propone eventi indirizzabili snelli con liste ordinate di ID evento.
- Profile Colors: identità visiva deterministica (proposta bozza): Nuova bozza di NIP per derivare colori leggibili deterministici da una chiave pubblica Nostr per un'identità visiva coerente tra i client.
- NIPs della traccia Namecoin: ancoraggio di identità, relay, TLS e reputazione (cluster di bozze): Un cluster di bozze di NIP che spostano i componenti dello stack Nostr in record ancorati a Namecoin.

## Approfondimento NIP: NIP-34 (git stuff)

NIP-34 definisce i tipi di evento per ospitare repository git, patch, pull request, issue e stati di merge sui relay Nostr. Un repository è annunciato come evento indirizzabile di kind 30617. Le patch usano il kind 1617 che porta l'output di git format-patch. Le pull request usano il kind 1618. Le issue usano il kind 1621 con contenuto markdown. Gli eventi di stato fanno passare un thread tra Aperto (1630), Applicato/Unito o Risolto (1631), Chiuso (1632) e Bozza (1633). La notizia NIP-34 di questa settimana è la stessa del lancio di GitWorkshop v2 della settimana scorsa: il pulsante di merge della PR nel browser funziona perché i server GRASP, ngit e lo schema URL di clone nostr:// insieme chiudono il cerchio su una forge completamente decentralizzata.

## Approfondimento NIP: NIP-53 (Live Activities)

NIP-53 definisce la superficie di eventi standard per le attività live su Nostr: stream live, spazi di meeting persistenti, eventi di conferenza programmati, presenza degli ascoltatori e chat live. Uno stream live è annunciato come evento indirizzabile di kind 30311. NIP-53 separa la stanza persistente dall'evento programmato che vi si tiene: un kind 30312 Meeting Space definisce una stanza, e un kind 30313 Conference Event rappresenta un meeting programmato o in corso in quella stanza. La superficie delle attività live di Nostr è intenzionalmente snella: NIP-53 annuncia l'attività, mentre altri NIP gestiscono le preoccupazioni adiacenti come i zap (NIP-57), gli obiettivi di zap (NIP-75) e le registrazioni video (NIP-71).

---

È tutto per questa settimana. Se state costruendo qualcosa o avete notizie da condividere, inviateci un DM su Nostr o trovateci su nostrcompass.org.
