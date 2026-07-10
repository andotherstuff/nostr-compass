---
title: 'Nostr Compass #23'
date: 2026-05-21
publishDate: 2026-05-21
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-21-newsletter.md
translationDate: 2026-07-01
---

Primal 3.5 rilascia una shell Android ricostruita, Amethyst aggiunge gli zap Bitcoin onchain, White Noise guadagna il rendering markdown e i deep link, Keycast supera un audit di sicurezza e AgentNoise permette di controllare agenti di coding AI locali su chat cifrate Marmot. Hostr lancia una piattaforma di locazione P2P su Nostr con quattro bozze di NIP che coprono annunci, prenotazioni ed escrow basato su EVM. Angor migra la messaggistica cifrata da NIP-04 a NIP-44, Dart NDK aggiunge NIP-77 e un web signer, Alby js-sdk v8 rilascia la riconnessione multi-relay nativa NWC, e KeyChat corregge un gap di forward secrecy nell'eliminazione delle one-time prekey di Signal. Sul lato protocollo, il bond anti-abuso di Mostro raggiunge la Fase 2, Wisp rilascia risposte private e reazioni gift-wrapped, e un'ondata di implementazione NIP-05 su Namecoin tocca una mezza dozzina di client in una sola settimana.

## Storie principali

### Primal 3.5 per Android

Primal, il client sociale sostenuto dalla propria infrastruttura di relay di caching, ha rilasciato [3.5.9](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.9) questa settimana con una shell applicativa ricostruita. Il redesign sostituisce la struttura di navigazione precedente con un layout aggiornato e una nuova schermata Explore, dando alla superficie principale di scoperta la propria home dedicata. La release aggiunge la riproduzione audio per le anteprime dei link, così i file audio incorporati nelle note vengono riprodotti inline senza lasciare il feed. I badge di verifica NIP-05 sono ora mostrati inline sui profili, portando in vista la conferma di identità a colpo d'occhio. Il filtraggio delle notifiche ha ricevuto una revisione, consentendo agli utenti di restringere quali tipi di evento raggiungono la loro lista di notifiche. L'editor ha guadagnato una migliore gestione degli event-link, e il layer di database sottostante ha ricevuto correzioni di stabilità.

### White Noise: markdown, deep link e metadati audio

White Noise, l'app di messaggistica di gruppo cifrata con Marmot costruita su Nostr e MLS ([RFC 9420](https://www.rfc-editor.org/rfc/rfc9420)), ha avuto una delle sue settimane più intense fino a oggi attraverso i repository frontend e backend.

Sul frontend, [PR #665](https://github.com/marmot-protocol/whitenoise/pull/665) aggiunge il rendering markdown completo per i messaggi in chat, così grassetto, corsivo, blocchi di codice e link ora sono resi nativamente nella vista dei messaggi. [PR #675](https://github.com/marmot-protocol/whitenoise/pull/675) abilita il flusso di uscita dal gruppo che era precedentemente bloccato per gli admin non ultimi, e [PR #661](https://github.com/marmot-protocol/whitenoise/pull/661) aggiunge il supporto nativo ai deep link per gli URI `whitenoise://` e `whitenoise-staging://` che coprono utenti, chat e impostazioni, senza richiedere alcuna infrastruttura di redirect HTTP.

Sul backend in whitenoise-rs, [PR #835](https://github.com/marmot-protocol/whitenoise-rs/pull/835) fa funzionare correttamente la rotazione dei key package riutilizzando lo slot `d_tag` per le pubblicazioni di kind:30443, abilitando la semantica di eventi replaceable NIP-33 così che le successive rotazioni di key package sostituiscano l'evento precedente sui relay, mantenendo solo il key package corrente. [PR #833](https://github.com/marmot-protocol/whitenoise-rs/pull/833) estende `FileMetadata` con campi opzionali `duration_ms` e `waveform` per gli allegati audio, coordinato con la [PR #300](https://github.com/marmot-protocol/mdk/pull/300) di MDK che aggiunge gli stessi campi ai tag media MIP-04. Un nuovo crate `whitenoise-markdown` ([PR #836](https://github.com/marmot-protocol/whitenoise-rs/pull/836)) sostituisce il precedente parser di token nostr-sdk con una libreria dedicata al rendering markdown.

La spec del protocollo Marmot stessa ha ricevuto una correzione di sicurezza in [PR #68](https://github.com/marmot-protocol/marmot/pull/68), che chiude un problema di sicurezza specificando esplicitamente HKDF-SHA256 per le derivazioni di chiave immagine in MIP-01, rimuovendo un'ambiguità che poteva portare a divergenze implementative. In MDK, [PR #307](https://github.com/marmot-protocol/mdk/pull/307) sanifica le ragioni di fallimento dei welcome e limita la lunghezza memorizzata, chiudendo una separata segnalazione di sicurezza.

### Amethyst v1.10.0: Zap Bitcoin Onchain

Amethyst ha rilasciato quattro release questa settimana, con [v1.10.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.10.0) come principale. La release aggiunge il supporto agli zap Bitcoin onchain NIP-BC, consentendo agli utenti di inviare, ricevere e visualizzare zap regolati direttamente onchain tramite transazioni Bitcoin. Le release precedenti nella serie hanno corretto la rilevazione di blob Blossom per rifiutare filename non conformi ([v1.09.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.09.2)), patchato le regole ProGuard per le build desktop e mergiato la pull request [#2977](https://github.com/vitorpamplona/amethyst/pull/2977) per mostrare gli zapper Bitcoin onchain come una riga ₿ dedicata nella galleria delle reazioni espansa. Una schermata in-progress di cronologia transazioni onchain con paginazione è arrivata in [PR #2974](https://github.com/vitorpamplona/amethyst/pull/2974).

### AgentNoise: controllare agenti di coding su White Noise

[AgentNoise](https://github.com/nvk/agentnoise) di nvk è un helper desktop Rust-nativo che consente di usare un telefono che esegue White Noise come superficie di controllo per sessioni di agenti di coding Codex e Claude locali. Lo strumento ascolta una o più chat White Noise, autentica i mittenti tramite un flusso PIN di first-pairing e lancia gli agenti di coding locali tramite il launcher configurato. Inviare `/claude <prompt>` dal telefono apre una nuova sessione di lavoro White Noise chiamata come l'hostname della macchina e un breve riepilogo del prompt, poi trasmette gli aggiornamenti di progresso e l'output finale a quella chat. È intenzionalmente Rust-first e tiene Node fuori dal percorso trusted del bridge. Il progetto ha raggiunto [v0.1.24](https://github.com/nvk/agentnoise/releases/tag/v0.1.24) questa settimana, aggiungendo risposte più brevi leggibili dal telefono, riferimenti a job per prefisso breve univoco e un watcher opzionale di sessione locale. AgentNoise pilota le CLI `wn` e `wnd` di `marmot-protocol/whitenoise-rs` come sottoprocessi, quindi condivide il proprio trasporto Nostr con il client White Noise stesso.

### Audit di sicurezza di Keycast completato

[Keycast](https://github.com/marmot-protocol/keycast), il server di remote signing NIP-46 orientato ai team che memorizza chiavi private Nostr cifrate a riposo in SQLite, ha completato un audit di sicurezza nel maggio 2026. Il passaggio di hardening ha affrontato problemi di autenticazione, permessi, integrità dei dati e dipendenze, e i risultati sono documentati in [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md). Le modifiche includono: l'auth HTTP NIP-98 richiede ora esattamente un tag `u` e un tag `method`, rifiuta timestamp obsoleti e valida gli hash `payload`; l'allowlist `ALLOWED_PUBKEYS` è parsata esattamente e forzata lato server; le policy vuote ora rifiutano di default le richieste sign/encrypt/decrypt; il rispetto delle foreign key è abilitato sulle connessioni SQLite; e le route app nidificate come `/teams/:id` sono protette lato server. Una migrazione SQL normalizza il JSON dei vecchi permessi di kind consentiti all'avvio. Il progetto è ancora in fase iniziale e l'audit segnala elementi residui prima di affidargli chiavi di team reali.

### Scramble: client Marmot per desktop e Android

[Scramble](https://github.com/DavidGershony/Scramble) (precedentemente OpenChat) è un client desktop e Android in .NET/Avalonia per il [Marmot Protocol](/it/topics/marmot/), che implementa i MIP 00-04: pubblicazione di KeyPackage (kind:30443), metadati di gruppo con l'estensione MLS NostrGroupData, eventi welcome gift-wrapped NIP-59 (kind:444), messaggi cifrati ChaCha20-Poly1305 (kind:445) e allegati media cifrati Blossom. È pienamente interoperabile con White Noise e con qualsiasi altro client compatibile con Marmot.

Il progetto ha rilasciato 13 release questa settimana, con il supporto multi-dispositivo come funzionalità principale. Ogni dispositivo genera uno slot KeyPackage univoco (un tag `d` su kind:30443). All'avvio, Scramble recupera i KeyPackage propri dell'utente dai relay, rileva gli ID slot dei dispositivi peer e li aggiunge automaticamente ai gruppi MLS esistenti usando il flusso di staged commit. L'auto-aggiunta è ristretta ai gruppi in cui l'utente corrente è admin; i gruppi non-admin vengono saltati con l'indicazione di chiedere all'admin del gruppo. Un banner informativo di forward-secrecy avvisa i dispositivi appena collegati che i vecchi messaggi non sono disponibili. Un passaggio di riconciliazione degli ID slot (`TryReconcileSlotId`) gestisce i dispositivi migrati da versioni pre-multi-dispositivo confrontando i byte di KeyPackage del relay con il materiale di chiave locale per adottare il tag `d` corretto. È stata anche corretta la riconnessione al signer esterno per utenti Amber e NIP-46: la guardia `IsConnected` che bloccava l'auto-riconnessione interna di `ExternalSignerService` è stata rimossa in tutti e nove i call site in `NostrService`.

### Hostr: locazione P2P su Nostr

[Hostr](https://hostr.network) ([sorgente](https://github.com/sudonym-btc/hostr)) è una piattaforma di locazione peer-to-peer costruita interamente su Nostr. Copre l'intero flusso stile Airbnb (ricerca e pubblicazione di proprietà, negoziazione di prenotazioni e regolamento dei pagamenti) usando quattro bozze di NIP che il progetto sta sviluppando in parallelo con l'applicazione.

Il NIP di accommodation estende gli annunci classificati [NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md) (kind:30402 attivo, kind:30403 draft) con tag specifici per l'ospitalità per il tipo (`room`, `house`, `apartment`, `villa`, `hotel`, `hostel`, `resort`), orari di check-in/check-out, permanenza minima e indici di celle geospaziali H3 per la ricerca basata su posizione con precisione configurabile. Il NIP di prenotazione definisce un protocollo completo di negoziazione e ciclo di vita: gli eventi di prenotazione replaceable di kind:32122 portano un trade ID `d`, un tag `a` di ancoraggio all'annuncio e tag `p` dei partecipanti con ruoli (`buyer`, `seller`, `escrow`); i rumor di messaggio strutturato di kind:1327 consegnano controproposte private in fase di negoziazione tramite gift wrap NIP-59 così la negoziazione resta fuori dai relay pubblici; gli eventi di transizione append-only di kind:1326 creano un audit trail pubblico una volta che una prenotazione viene confermata. La privacy del compratore è preservata tramite chiavi Nostr temporanee per-trade legate all'identità reale del compratore tramite tag `participant_proof` cifrati. Il NIP di escrow definisce annunci di servizio escrow di kind:30303 e dichiarazioni di fiducia utente di kind:17388; l'implementazione di riferimento usa smart contract EVM su Rootstock, con `contractBytecodeHash` che permette ai client di verificare che il contratto deployato corrisponda a un'implementazione nota e auditata. Il NIP di marketplace listing definisce tag generici condivisi da tutti i profili marketplace NIP-99, inclusi `instantBook`, `negotiable`, `quantity`, `securityDeposit`, `cancellationPolicy` e `maxDisputePeriod`. Questa settimana il progetto ha preparato la sua submission all'app store e mergiato il supporto all'identità del client MCP per l'automazione rivolta agli agenti.

Due nuove voci sono apparse sulla piattaforma Shakespeare MiniApps questa settimana: [InkPress](https://inkpress.shakespeare.wtf), un generatore di riviste AI che pubblica contenuto strutturato in stile rivista come eventi Nostr, e [PressStr](https://pressstr.shakespeare.wtf), una piattaforma di scrittura e pubblicazione per lo stack Soapbox.

## Rilasciato questa settimana

### ngit v2.4.4

**ngit** ha rilasciato [v2.4.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.4), aggiungendo `ngit sync --trust-server` (`-t`) per i casi in cui un server git è fast-forward avanti rispetto allo stato Nostr. Quando questa situazione viene rilevata, sync segnala i ref interessati e richiede il flag per firmare e pubblicare un evento di stato aggiornato; un setting git config `nostr.trust-server-domains` fornisce una allowlist separata da punti e virgola per i server che dovrebbero essere considerati affidabili automaticamente senza il flag.

### Amber v6.1.0-pre3 aggiunge la firma PSBT

**Amber** ha rilasciato [v6.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre3) con un layout migliorato per le nuove connessioni di app, correzioni di crash e un'opzione seleziona/deseleziona tutto nella schermata dei permessi. [PR #438](https://github.com/greenart7c3/Amber/pull/438) aggiunge il supporto alla firma PSBT sia tramite il percorso Intent-based sia tramite quello NIP-46 basato su relay, permettendo ad Amber di firmare Partially Signed Bitcoin Transactions senza esporre l'nsec all'app richiedente.

### Wisp v1.1.0 rilascia risposte private e abbandona il supporto ad Amber

**Wisp** ha rilasciato [v1.1.0](https://github.com/barrydeen/wisp/releases/tag/v1.1.0) con risposte private tramite gift wrap NIP-17 ([PR #540](https://github.com/barrydeen/wisp/pull/540)), reazioni gift-wrapped e zap DIP-03 sulle risposte private ([PR #543](https://github.com/barrydeen/wisp/pull/543)), auto-traduzione per le note ([PR #523](https://github.com/barrydeen/wisp/pull/523)) e un input fiat stile register sul dialog dello zap. [PR #541](https://github.com/barrydeen/wisp/pull/541) migra gli zap privati da uno schema plaintext DM-relay fatto in casa a DIP-03 con un corretto routing DM-relay. Lo stesso ciclo di release ha rimosso il supporto al remote signer NIP-55 ([PR #531](https://github.com/barrydeen/wisp/pull/531)), abbandonando Amber e altre integrazioni con signer esterni, e ha rimosso il relay locale in bundle ([PR #533](https://github.com/barrydeen/wisp/pull/533)). Wisp è un client sociale Nostr per Android.

### Calendar by Formstr v1.5.4 corregge il gift wrap per i nuovi partecipanti

**Calendar by Formstr** ha rilasciato [v1.5.4](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.4) (l'ultima in una sequenza v1.5.2 → v1.5.4). [PR #160](https://github.com/formstr-hq/nostr-calendar/pull/160) corregge un bug in cui l'editing di un evento di calendario privato con nuovi partecipanti pubblicava l'evento aggiornato con le nuove pubkey nei tag `p` ma non creava né consegnava mai inviti gift wrap a quei partecipanti, rompendo il flusso di invito per aggiunte dell'ultimo minuto. [PR #156](https://github.com/formstr-hq/nostr-calendar/pull/156) aggiunge gestione degli errori attorno alla decifratura degli eventi privati così i client non lanciano più eccezioni su eventi non decifrabili, e [PR #138](https://github.com/formstr-hq/nostr-calendar/pull/138) corregge orari di eventi ricorrenti che stavano andando alla deriva fra fusi orari.

### Applesauce v6.1.0 aggiunge git cast NIP-34 e lookup relay NIP-51

**Applesauce** ha rilasciato [v6.1.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.1.0) attraverso i suoi pacchetti con un significativo supporto NIP-34 (git-over-Nostr): applesauce-common aggiunge nuovi cast `GitRepository`, `GitGraspList` e `FavoriteGitRepos` più factory corrispondenti, ed espone le proprietà reattive `User.favoriteGitRepos$`, `User.gitAuthors$` e `User.graspServers$` così le applicazioni possono elencare i repo git seguiti da un utente, i manutentori dei repo e i server GRASP configurati direttamente dallo stesso oggetto User. La stessa release aggiunge il supporto alle liste di lookup relay NIP-51 di kind 10086, un'aggiunta recente alla famiglia di relay list usata per scoprire dove trovare dati specifici. applesauce-core guadagna `replaceableAddress` su `EventCast` per il lookup di indirizzi replaceable NIP-01, più `pointer`, `kind` e un helper `getReplaceableAddressForEvent`, e aggiunge un metodo `timeline$()` sul cast `User` base. [PR #73](https://github.com/hzrd149/applesauce/pull/73) corregge i metodi manuali del pool che scartavano silenziosamente i relay offline.

### Sprout v0.0.16 rilascia il binario Sprig e il protocollo huddle v2

**Sprout** di Block, un workspace di team basato su relay Nostr self-hosted dove esseri umani e agenti AI condividono le stesse stanze e event log, ha rilasciato [v0.0.16](https://github.com/block/sprout/releases/tag/v0.0.16) dell'app desktop insieme a build rolling del nuovo binario all-in-one Sprig ([PR #605](https://github.com/block/sprout/pull/605)), che raggruppa l'harness ACP, l'agente e l'MCP per sviluppatori in un unico binario stile busybox per un deployment facile. Il flag `--no-memory` aggiunto in [PR #611](https://github.com/block/sprout/pull/611) consente agli operatori di disabilitare l'injection della core memory NIP-AE per l'harness ACP. Sul lato realtime, [PR #609](https://github.com/block/sprout/pull/609) estende il protocollo voice huddle a un header di frame v2 che supporta fino a 10 peer simultanei.

### Nostrord v1.0.3 aggiunge keychain OS e multi-account

**Nostrord** ha rilasciato [v1.0.3](https://github.com/nostrord/nostrord/releases/tag/v1.0.3) con lo storage locale delle chiavi rafforzato usando keychain OS e fallback a passphrase, supporto multi-account e un QR code bunker tappable che apre l'app signer su Android.

### Angor migra a NIP-44 e rilascia hardening di sicurezza

**Angor**, l'app di crowdfunding Bitcoin costruita su Nostr e Taproot, ha rilasciato tre release unstable questa settimana ([v0.2.24](https://github.com/block-core/angor/releases/tag/v0.2.24), [v0.2.25](https://github.com/block-core/angor/releases/tag/v0.2.25) e [v0.2.26](https://github.com/block-core/angor/releases/tag/v0.2.26)) con una serie di modifiche di hardening di sicurezza e integrazione Nostr. [PR #860](https://github.com/block-core/angor/pull/860) migra la messaggistica cifrata Nostr da NIP-04 a NIP-44, sostituendo lo schema deprecato basato su XOR con la cifratura ChaCha20-Poly1305. [PR #861](https://github.com/block-core/angor/pull/861) consente upload media Blossom senza un wallet selezionato usando una chiave di auth Nostr effimera, sbloccando gli upload per gli utenti che non hanno ancora connesso un wallet. La serie di sicurezza ha affrontato diverse categorie hardened: [PR #854](https://github.com/block-core/angor/pull/854) aggiunge type safety per AngorKey e protezione della memoria della mnemonic, [PR #856](https://github.com/block-core/angor/pull/856) impone validazione a livello di protocollo per timelock, fee rate, soglie di dust e regole di penalty, e [PR #851](https://github.com/block-core/angor/pull/851) applica hardening non-breaking attraverso otto categorie di gravità media e bassa. [PR #859](https://github.com/block-core/angor/pull/859) corregge la compatibilità con GrapheneOS abilitando la compilazione AOT e rimuovendo la generazione di codice a runtime, e [PR #855](https://github.com/block-core/angor/pull/855) previene la perdita del wallet allo swipe-kill Android persistendo lo stato del wallet prima che l'OS termini il processo.

### Alby js-sdk v8.0 rilascia la riconnessione multi-relay NWC

**Alby js-sdk** ha rilasciato la linea v8.0 (da [v8.0.1](https://github.com/getAlby/js-sdk/releases/tag/v8.0.1) a [v8.0.3](https://github.com/getAlby/js-sdk/releases/tag/v8.0.3)) con il supporto alle sottoscrizioni multi-relay NWC. [PR #516](https://github.com/getAlby/js-sdk/pull/516) aggiorna la dipendenza nostr-tools e abilita l'auto-riconnessione nativa attraverso più relay, sostituendo il precedente approccio a polling con una logica di riconnessione nativa del relay. [PR #542](https://github.com/getAlby/js-sdk/pull/542) sostituisce tutte le chiamate `console.debug` con un'interfaccia logger iniettabile così gli sviluppatori di applicazioni possono instradare la diagnostica dell'SDK attraverso la propria infrastruttura di logging. La release abbandona il polyfill WebSocket, richiedendo Node.js 22 o superiore per i consumer lato server. v8.0.2 ha aggiunto una correzione per un bug di import crypto utils che rompeva certi bundler.

### KeyChat v1.41.1 corregge la forward secrecy

**KeyChat**, un'app di messaggistica che combina il protocollo Signal con il trasporto tramite relay Nostr, ha rilasciato [v1.41.1+6513](https://github.com/keychat-io/keychat-app/releases/tag/v1.41.1+6513). La correzione principale impone la forward secrecy eliminando le one-time prekey di Signal immediatamente dopo una decifratura riuscita, chiudendo un gap dove una prekey trattenuta poteva essere usata per decifrare messaggi passati se il dispositivo fosse stato successivamente compromesso. La release aggiunge anche l'anteprima URL per i messaggi consistenti in un singolo link, centralizza l'auto-download dei media sotto un nuovo `FileDownloadManager` con una soglia automatica di 20 MB, e rifattora il fetch delle informazioni di relay NIP-11 per forzare il refresh al cold start così le configurazioni di fee dei relay a pagamento vengono sempre caricate correttamente.

## In sviluppo

**Citrine** ha mergiato [PR #151](https://github.com/greenart7c3/Citrine/pull/151) implementando l'enforcement di NIP-70: il relay Android ora blocca i repost che incorporano contenuto di eventi protetti, come richiede la spec. [PR #149](https://github.com/greenart7c3/Citrine/pull/149) aggiunge azioni di visualizzazione e copia per più indirizzi di connessione, localhost, Wi-Fi locale e Tor, dalla schermata delle impostazioni del relay. [PR #141](https://github.com/greenart7c3/Citrine/pull/141) aggiunge la gestione delle challenge AUTH NIP-42 tramite integrazione con signer esterno tramite Amber.

**Mostro** ha raggiunto la Fase 2 del suo rollout di bond anti-abuso. [PR #737](https://github.com/MostroP2P/mostro/pull/737) porta la logica di slash di dispute diretta dal solver: gli handler admin ora consumano il payload `BondResolution` da mostro-core, consentendo a un admin di slashare il bond di una delle parti quando risolve una disputa. La Fase 1.5, mergiata in [PR #736](https://github.com/MostroP2P/mostro/pull/736), ha introdotto un'azione dedicata `PayBondInvoice` e uno status `WaitingTakerBond`, separando il pagamento del bond anti-abuso del taker dal payout di trade del compratore. Il client mobile ha aggiunto la UX completa di Fase 1.5 in [PR #592](https://github.com/MostroP2P/mobile/pull/592). Mostro è un protocollo di exchange Bitcoin peer-to-peer costruito su Nostr.

**Damus** ha mergiato [PR #3773](https://github.com/damus-io/damus/pull/3773) ripristinando l'indicatore di segnale del relay, e [PR #3775](https://github.com/damus-io/damus/pull/3775) corregge relay che rifiutavano di riconnettersi dopo un fallimento iniziale di connessione.

**rust-nostr** ha mergiato [PR #1358](https://github.com/rust-nostr/nostr/pull/1358) aggiungendo trait di finalizzazione degli eventi e builder di eventi specifici per NIP, rendendo più facile costruire eventi correttamente tipizzati per funzioni di protocollo specifiche. [PR #1363](https://github.com/rust-nostr/nostr/pull/1363) porta indietro una correzione che assicura che il signer NIP-46 si sottoscriva alle notifiche prima di inviare la risposta di connect, chiudendo una race condition in cui i messaggi del client che arrivavano immediatamente dopo il connect potevano essere persi.

**dart-nostr** ha mergiato [PR #44](https://github.com/ethicnology/dart-nostr/pull/44) aggiungendo un resolver di relay Namecoin `.bit` e record di pin TLSA, permettendo alle applicazioni Flutter di risolvere URL di relay `wss://example.bit/` tramite DNS Namecoin ai loro effettivi indirizzi WebSocket.

**Dart NDK** (il Nostr development kit Dart/Flutter, ora in `relaystr/ndk`) ha mergiato [PR #464](https://github.com/relaystr/ndk/pull/464) implementando NIP-77, il protocollo di firma eventi offline. Sul lato signer, [PR #602](https://github.com/relaystr/ndk/pull/602) e [PR #601](https://github.com/relaystr/ndk/pull/601) aggiungono un event signer specifico per web e un'astrazione `PlatformEventVerifier`, consentendo alle app Flutter web di usare il signer di piattaforma senza un percorso di codice separato; [PR #604](https://github.com/relaystr/ndk/pull/604) introduce una factory di event signer per la selezione a runtime del signer. [PR #608](https://github.com/relaystr/ndk/pull/608) aggiunge `getDmRelays()` per recuperare la lista di relay DM NIP-17 di un utente (kind:10050), e [PR #600](https://github.com/relaystr/ndk/pull/600) corregge la preservazione dei campi firmati NIP-46 così i remote signer non perdono campi al round-trip.

**Pages by Form\*** ([repo](https://github.com/formstr-hq/nostr-docs)), l'app di documenti collaborativi Nostr-native di Formstr ospitata a [pages.formstr.app](https://pages.formstr.app), ha mergiato quattro PR questa settimana stringendo i flussi di attachment cifrato e gestione documenti. [PR #37](https://github.com/formstr-hq/nostr-docs/pull/37) corregge immagini mancanti negli export DOCX, HTML e PDF inserendo inline gli allegati cifrati: recupera i blob `<encrypted-file>` dai server Blossom, li decifra con AES-GCM 256-bit usando la chiave e il nonce memorizzati, valida il MIME type dell'immagine e li converte in URL dati base64 così gli export preservano immagini che esistono solo su Blossom in forma cifrata. [PR #39](https://github.com/formstr-hq/nostr-docs/pull/39) aggiunge un meccanismo di ricerca documenti locali, [PR #38](https://github.com/formstr-hq/nostr-docs/pull/38) sistema il flusso di rinomina, e [PR #40](https://github.com/formstr-hq/nostr-docs/pull/40) corregge la gestione dei backup condivisi.

**Zap Cooking** ha mergiato [PR #396](https://github.com/zapcooking/frontend/pull/396), la prima fase di una revisione del feed che pone le primitive di rendering del feed senza alcun cambiamento ancora visibile all'utente. La PR introduce un parser di tag `imeta` NIP-92 che legge gli slot `url`, `m` (MIME), `dim` (dimensioni), `blurhash`, `alt`, `x` (hash file) e `fallback`, più un decoder canonico blurhash portato a mano (~200 LOC) che produce data URL PNG tramite canvas con un fallback null SSR-safe. Quando i tag `imeta` sono assenti, il parser ricade sull'estrazione di URL grezzi di immagine e video dal contenuto dell'evento usando le stesse euristiche che il feed corrente già usa.

**Nurunuru** (ぬるぬる, `tami1A84/null--nostr`), un client Nostr con varianti Android, iOS e Web native che condividono un engine FFI Rust, ha mergiato la sua sync Native → Web v1.5.0 in [PR #176](https://github.com/tami1A84/null--nostr/pull/176). La sync porta diverse aggiunte di funzionalità alla build Web che erano già state rilasciate su Android v1.4.9 e iOS 1.0.4: la [NotificationModal](https://github.com/tami1A84/null--nostr/pull/176) ora mostra notifiche di compleanno, rilevazione di zap mutual-follow e notifiche di reazione con emoji custom; il selettore di reazioni abbandona la quick-row di reazioni Unicode di default e centra la UX sulle emoji custom; l'engine di raccomandazione in `lib/recommendation.js` filtra utenti senza icone o display name e dà priorità alle voci Following con Recommended che carica in background. L'input vocale è l'unica funzionalità che va nella direzione opposta: la build Web usa già lo streaming ElevenLabs Scribe, e v1.5.0 sincronizza parzialmente il lato Native con `SpeechRecognizer` standard OS (Android) e `SFSpeechRecognizer` + `AVAudioEngine` (iOS) mentre l'integrazione Scribe Native completa è rimandata a v1.6.

## Lavoro di protocollo e spec

**PR [#2251](https://github.com/nostr-protocol/nips/pull/2251)** stringe la spec degli eventi protetti NIP-70: ora dichiara esplicitamente che i repost che incorporano il contenuto completo di un evento protetto devono essere rifiutati dai relay. NIP-70 definisce il tag `-` che segnala che un autore di nota non acconsente a che la sua nota venga ripubblicata. La spec originale copriva il comportamento di filtraggio del relay, ma lasciava ambiguo il caso di repost. Questa PR chiude quel gap. La [PR #151](https://github.com/greenart7c3/Citrine/pull/151) di Citrine implementa l'enforcement sul lato relay in questa stessa settimana.

**PR [#1653](https://github.com/nostr-protocol/nips/pull/1653)** propone un NIP Drafts per salvare e sincronizzare eventi di bozza privati. La proposta usa eventi replaceable con status `draft` e cifratura NIP-44 verso la chiave dell'autore stesso, consentendo ai client di salvare lavori in corso sui relay senza che quegli eventi siano visibili a chiunque altro. L'evento draft porta l'evento completo di pubblicazione intesa come contenuto cifrato, incluso il suo eventuale kind e tag.

**Snapshots ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279))** è una proposta aperta di definire un evento snapshot immutabile per preservare una versione esatta di un evento Nostr replaceable. L'evento snapshot porta il contenuto completo dell'evento replaceable in un dato momento nel tempo, con un tag `a` che lo collega all'indirizzo dell'evento replaceable così tutte le versioni storiche sono interrogabili insieme. Questo rende possibile agli osservatori ispezionare lo stato storico anche dopo che i relay smettono di conservare le vecchie versioni.

**Ondata Namecoin NIP-05:** Questa settimana ha visto una spinta coordinata per aggiungere la risoluzione NIP-05 `.bit` ai client Nostr. Il feed di discussione NIP ha catturato PR open-source contro Aegis ([#14](https://github.com/ZharlieW/Aegis/pull/14), che aggiunge la verifica al momento della firma nel signer), nostter ([#2128](https://github.com/SnowCait/nostter/pull/2128)) e dart-nostr ([#44](https://github.com/ethicnology/dart-nostr/pull/44)), insieme a una bozza NIP upstream ([PR #2349](https://github.com/nostr-protocol/nips/pull/2349)). La PR di Aegis è notevole per aver posto la verifica sul lato produttore: il signer controlla la chain Namecoin prima di firmare qualsiasi evento di kind:0 che rivendica un'identità `.bit` e avvisa l'utente in caso di mismatch, catturando il problema prima che l'evento raggiunga qualsiasi relay.

## NIP Deep Dive: NIP-07 (window.nostr per i browser Web)

[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) definisce l'interfaccia `window.nostr` che le estensioni browser espongono alle applicazioni web. È l'interfaccia di signer più ampiamente deployata sul web, implementata da estensioni tra cui Alby, nos2x, Flamingo e horse.

L'interfaccia ha due metodi obbligatori e diversi opzionali. `window.nostr.getPublicKey()` restituisce la chiave pubblica dell'utente come stringa hex senza mai esporre la chiave privata alla pagina chiamante. `window.nostr.signEvent(event)` prende un evento parziale con `created_at`, `kind`, `tags` e `content`, e restituisce l'evento firmato completo con `id`, `pubkey` e `sig` aggiunti. Il punto chiave è che la chiave privata non lascia mai il contesto isolato dell'estensione; l'applicazione web sottomette un evento non firmato e riceve indietro uno firmato.

I metodi opzionali coprono la cifratura: `window.nostr.nip04.encrypt` e `window.nostr.nip04.decrypt` per il vecchio schema NIP-04 (ora deprecato), e `window.nostr.nip44.encrypt` e `window.nostr.nip44.decrypt` per lo schema NIP-44 corrente. Le estensioni che supportano NIP-44 possono quindi gestire sia la cifratura dei messaggi diretti sia qualsiasi altra applicazione che necessita di cifratura keyed su pubkey senza che la pagina chiamante veda l'nsec.

La spec include anche una raccomandazione agli autori di estensioni: caricare gli script con `"run_at": "document_end"` nel manifest dell'estensione così `window.nostr` è disponibile in modo sincrono quando la pagina si carica, evitando race condition in cui un client controlla `window.nostr` prima che l'estensione l'abbia iniettato.

Un esempio chiave di NIP-07 in azione è il progetto Keycast trattato sopra. Il frontend web di Keycast usa NIP-07 per firmare eventi di auth HTTP NIP-98: l'app SvelteKit non gestisce mai direttamente l'nsec dell'utente. Chiama `window.nostr.signEvent` per produrre l'header di auth, poi invia quell'header all'API Keycast. Questa architettura significa che il materiale della chiave resta nell'estensione browser lungo tutto il flusso di gestione delle chiavi di team.

```json
{
  "id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 1,
  "tags": [],
  "content": "Hello from a NIP-07 signed event",
  "sig": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2cdd"
}
```

## NIP Deep Dive: NIP-39 (identità esterne nei profili)

[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) definisce come un utente Nostr può dichiarare il controllo su identità esterne di piattaforma nel proprio profilo. Ciascuna dichiarazione usa un tag `i` dentro un evento di kind:10011, asserendo la proprietà di uno specifico account su un'altra piattaforma insieme a una prova che può essere verificata indipendentemente.

Ogni tag segue il formato `["i", "platform:identity", "proof"]`, dove `platform:identity` combina il nome della piattaforma e lo username con un separatore due punti (`github:semisol`, `twitter:semisol_public`). `proof` punta a un artefatto verificabile sulla piattaforma stessa.

Per GitHub, la prova è un ID di Gist. L'utente crea una Gist pubblica dal proprio account GitHub contenente il testo `Verifying that I control the following Nostr public key: npub1...`. Un client che verifica il claim recupera `https://gist.github.com/<identity>/<proof>` e controlla che la Gist sia stata scritta dallo username GitHub reclamato e contenga la pubkey attesa. Per Twitter la prova è un ID di tweet, per Mastodon un ID di post, e per Telegram un riferimento a messaggio in un gruppo pubblico.

Il nome del provider di identità deve contenere solo `a-z`, `0-9` e i caratteri `._-/`, e non deve contenere `:`. I nomi di identità dovrebbero essere normalizzati in minuscolo, con l'alias principale usato quando ne esistono multipli.

La discussione NIP-05 `.bit` Namecoin che avviene questa settimana mostra il ruolo di NIP-39 nello stack di identità più ampio: fornisce un modo standardizzato e agnostico ai relay di cross-referenziare una chiave Nostr con un'identità stabilita altrove, senza richiedere alcuna autorità di verifica centrale. Un client può verificare indipendentemente la prova recuperando un artefatto pubblico sulla piattaforma nominata, e la prova è legata alla specifica pubkey Nostr nel testo della Gist o del tweet, non a una credenziale di piattaforma generica.

```json
{
  "id": "b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 10011,
  "tags": [
    ["i", "github:semisol", "9721ce4ee4fceb91c9711ca2a6c9a5ab"],
    ["i", "twitter:semisol_public", "1619358434134196225"],
    ["i", "mastodon:bitcoinhackers.org/@semisol", "109775066355589974"]
  ],
  "content": "",
  "sig": "1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3eff"
}
```

---

È tutto per questa settimana. Se stai costruendo qualcosa o hai notizie da condividere, mandaci un DM su Nostr o trovaci su [nostrcompass.org](https://nostrcompass.org).
