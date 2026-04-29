---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Bentornati su Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [Amethyst](https://github.com/vitorpamplona/amethyst) chiude un grande ciclo di lavoro su [Marmot](/it/topics/marmot/), communities [NIP-72](/it/topics/nip-72/), zap goals [NIP-75](/it/topics/nip-75/) e audio rooms basate su Media over QUIC. [TollGate](https://github.com/OpenTollGate/tollgate) stabilizza l'accesso Internet pay-per-use su Nostr e Cashu con [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0). [nostream](https://github.com/Cameri/nostream) completa una settimana di lavoro relay attorno a [NIP-45](/it/topics/nip-45/), [NIP-62](/it/topics/nip-62/), compressione, hardening delle query e piena parità con [NIP-11](/it/topics/nip-11/). [Forgesworn](https://github.com/forgesworn) pubblica un intero stack per firma, identità e API a pagamento su Nostr. [ShockWallet](https://github.com/shocknet/wallet2) continua a spingere flussi Lightning nativi su Nostr. Il gruppo Formstr porta avanti 26 PR tra hardening di sicurezza e supporto RRULE. [StableKraft](https://github.com/ChadFarrow/stablekraft-app), [Keep](https://github.com/privkeyio/keep-android), [topaz](https://github.com/fiatjaf/topaz), [WoT Relay](https://github.com/bitvora/wot-relay), [Flotilla](https://gitea.coracle.social/coracle/flotilla) e [NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) completano la lista delle release. Gli approfondimenti di questa settimana coprono [NIP-72](/it/topics/nip-72/) e [NIP-57](/it/topics/nip-57/).

## Top Stories

### Amethyst ships Marmot MIP compliance, NIP-72 communities, zap goals, and MoQ audio rooms

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android mantenuto da vitorpamplona, ha unito 57 PR questa settimana. I temi principali sono la conformità ai MIP di [Marmot](/it/topics/marmot/), il supporto di prima classe alle moderated communities, gli zap goals sui live stream e un nuovo stack per audio rooms costruito su Media over QUIC.

Sul fronte Marmot, [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) allinea l'implementazione embedded di [MDK](https://github.com/marmot-protocol/mdk) ai formati wire MIP-01 e MIP-05, aggiungendo codifica VarInt e validazione round-trip contro i test vector di MDK. [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) aggiunge il supporto MIP-00 KeyPackage Relay List, [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) chiude i gap residui emersi dai test cross-client con [White Noise](https://github.com/marmot-protocol/whitenoise), e [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466), [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471), [PR #2477](https://github.com/vitorpamplona/amethyst/pull/2477) e [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) sistemano framing MLS, bug di decrittazione e validazione completa della crittografia dei commit.

Accanto al lavoro di protocollo, [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) pubblica `amy`, uno strumento command-line per operazioni di gruppo Marmot e MLS guidato dall'implementazione di Amethyst. Gli integratori ottengono così un modo scriptabile per creare gruppi, generare KeyPackages, simulare welcome e validare commit contro un signer reale di Amethyst.

[PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) aggiunge la creazione e la gestione complete delle community [NIP-72](/it/topics/nip-72/). Gli utenti possono pubblicare il kind `34550`, aggiungere moderator e relay hint, inviare post con un tag `a` che punta alla community e gestire l'approvazione dei contributi tramite eventi kind `4549`. [PR #2458](https://github.com/vitorpamplona/amethyst/pull/2458) e [PR #2473](https://github.com/vitorpamplona/amethyst/pull/2473) aggiungono supporto agli emoji set e una UI completa per la gestione degli emoji pack [NIP-30](/it/topics/nip-30/).

[PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) collega gli zap goals [NIP-75](/it/topics/nip-75/) alla schermata Live Activities [NIP-53](/it/topics/nip-53/). Ogni stream mostra un header con goal di raccolta, barra di avanzamento, pulsante zap e classifica dei top zapper calcolata dalle ricevute kind `9735`. [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) aggiunge una schermata dedicata Live Streams, [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) introduce helper per proof-of-agreement ed event builder, e [PR #2461](https://github.com/vitorpamplona/amethyst/pull/2461) migliora la riproduzione HLS.

La nuova superficie più ambiziosa è l'audio real-time. [PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494) aggiunge un client Media over QUIC e il supporto alle audio rooms. Insieme alla nuova schermata Public Chats di [PR #2487](https://github.com/vitorpamplona/amethyst/pull/2487), Amethyst arriva a una superficie end-to-end per stanze audio pubbliche accanto alla propria messaggistica cifrata Marmot.

### TollGate v0.1.0 stabilizes pay-per-use internet over Nostr and Cashu

[TollGate](https://github.com/OpenTollGate/tollgate) ha taggato [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) il 21 aprile, il primo snapshot stabile del suo insieme di specifiche per l'accesso alla rete pay-per-use. Il protocollo permette a un dispositivo che può controllare la connettività, come un router WiFi o uno switch Ethernet, di pubblicizzare i prezzi, accettare token ecash [Cashu](/it/topics/cashu/) e gestire sessioni tramite token locali prepagati invece di account o subscription. Un cliente con pochi sats in un wallet Cashu locale può acquistare il prossimo minuto o megabyte di connettività da qualunque TollGate compatibile.

La release fissa tre livelli dell'architettura. Il livello protocollo, definito in [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md), specifica tre forme di evento base: Advertisement, Session e Notice. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) aggiunge i pagamenti Cashu, permettendo al cliente di riscattare token da qualunque mint pubblicizzata dal gate. Sopra c'è il livello interfaccia: [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) fino a HTTP-03 definiscono una superficie HTTP semplice per dispositivi con sistemi operativi restrittivi, mentre [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) definisce il trasporto tramite relay Nostr. Infine, [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) copre il livello medium descrivendo il routing captive-portal per i clienti paganti.

Il nuovo [topic su TollGate](/it/topics/tollgate/) copre l'intero stack.

### nostream merges 53 PRs for NIP-45, NIP-62, compression, and query hardening

[nostream](https://github.com/Cameri/nostream), implementazione relay TypeScript di Cameri, ha unito 53 PR in una settimana tra nuovo supporto NIP, performance delle query, hardening di sicurezza e miglioramenti operativi.

Sul lato funzionale, [PR #522](https://github.com/Cameri/nostream/pull/522) aggiunge il supporto `COUNT` di [NIP-45](/it/topics/nip-45/), [PR #544](https://github.com/Cameri/nostream/pull/544) aggiunge [NIP-62](/it/topics/nip-62/) alla lista delle funzionalità pubblicizzate, [PR #548](https://github.com/Cameri/nostream/pull/548) estende lo schema dei filtri ai tag maiuscoli e [PR #514](https://github.com/Cameri/nostream/pull/514) aggiunge compressione gzip e xz per import ed export di eventi.

Prestazioni e correttezza arrivano con [PR #534](https://github.com/Cameri/nostream/pull/534), che introduce un harness di benchmark e una passata di ottimizzazione sulla traduzione dei filtri in SQL. [PR #524](https://github.com/Cameri/nostream/pull/524) corregge un bug nel matching pubkey delle whitelist e blacklist, [PR #553](https://github.com/Cameri/nostream/pull/553) aggiunge un tie-breaker deterministico a `upsertMany`, [PR #493](https://github.com/Cameri/nostream/pull/493) limita la fiducia in `X-Forwarded-For` ai proxy configurati e [PR #557](https://github.com/Cameri/nostream/pull/557) porta il relay alla piena parità con [NIP-11](/it/topics/nip-11/).

## Shipping This Week

### Primal Android ships Explore tab, NIP-05 verification, and audio player

[Primal Android](https://github.com/PrimalHQ/primal-android-app) ha unito 11 PR sopra il redesign del feed della settimana scorsa. [PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021) introduce una nuova tab Explore costruita su utenti popolari, follow packs e curated feeds, [PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015) aggiunge un editor dei feed che si prepopola dalla DSL Advanced Search di Primal, [PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994) porta la UI di verifica [NIP-05](/it/topics/nip-05/) e [PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997) integra un audio player inline nei feed. [PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018) aggiunge anche il pairing nostr-connect [NIP-46](/it/topics/nip-46/) dal wallet QR scanner.

### strfry adds Prometheus write-path metrics and fixes NIP-42 AUTH envelope

[strfry](https://github.com/hoytech/strfry) ha pubblicato un gruppo di miglioramenti orientati agli operatori. [PR #194](https://github.com/hoytech/strfry/pull/194) aggiunge un exporter Prometheus dedicato per le metriche del write path, [PR #197](https://github.com/hoytech/strfry/pull/197) registra byte e compressione per connessione e [PR #192](https://github.com/hoytech/strfry/pull/192) rende configurabile a runtime il limite dei tag nei filtri. Sul piano della correttezza del protocollo, [PR #201](https://github.com/hoytech/strfry/pull/201) cambia le risposte di fallimento AUTH [NIP-42](/it/topics/nip-42/) da `NOTICE` all'envelope `OK` previsto dalla specifica.

### Shopstr hardens storefront security across 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr), client marketplace su Nostr, ha unito 13 PR dominate da fix di sicurezza. [PR #434](https://github.com/shopstr-eng/shopstr/pull/434) chiude un hole di stored JavaScript nei link delle storefront, [PR #417](https://github.com/shopstr-eng/shopstr/pull/417) fa escaping dell'HTML delle policy per bloccare XSS riflesso, [PR #418](https://github.com/shopstr-eng/shopstr/pull/418) chiude un'API di cancellazione eventi cached non autenticata e [PR #433](https://github.com/shopstr-eng/shopstr/pull/433), [PR #419](https://github.com/shopstr-eng/shopstr/pull/419), [PR #435](https://github.com/shopstr-eng/shopstr/pull/435) e [PR #414](https://github.com/shopstr-eng/shopstr/pull/414) rafforzano letture, mutazioni ed endpoint sensibili.

### Nostria v3.1.26 through v3.1.28 add background music playback on Android

[Nostria](https://github.com/nostria-app/nostria) ha pubblicato sei release da [v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22) a [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28). La novità principale di [v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26) è la riproduzione musicale in background su Android, con controlli media nella notification bar e nella lock screen. Le release successive rafforzano questo nuovo media-service surface.

### Wisp v0.18.0-beta adds Normie Mode, For You feed, and NIP-29 group config

[Wisp](https://github.com/barrydeen/wisp), client Android in Kotlin e Jetpack Compose di barrydeen, ha pubblicato [v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta) il 16 aprile. [PR #462](https://github.com/barrydeen/wisp/pull/462) aggiunge una Normie Mode con importi fiat-denominati, [PR #464](https://github.com/barrydeen/wisp/pull/464) rinnova l'onboarding e [PR #469](https://github.com/barrydeen/wisp/pull/469) introduce un feed For You. Sul lato protocollo, [PR #471](https://github.com/barrydeen/wisp/pull/471) aggiunge la configurazione dei gruppi [NIP-29](/it/topics/nip-29/) e [PR #478](https://github.com/barrydeen/wisp/pull/478) corregge il flusso AUTH [NIP-42](/it/topics/nip-42/) prima degli eventi amministrativi di gruppo. [PR #481](https://github.com/barrydeen/wisp/pull/481) inoltra anche le note agli inbox relay [NIP-65](/it/topics/nip-65/) delle pubkey menzionate.

### NoorNote v0.8.4 adds Scheduled Posts and live stream zapping

[NoorNote](https://github.com/77elements/noornote) ha pubblicato [v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) e [v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5). La novità principale della v0.8.4 è Scheduled Posts: l'app consegna un evento già firmato a un relay gestito da NoorNote che lo pubblica al momento pianificato, cosi le chiavi private non lasciano mai il dispositivo. La stessa release aggiunge zapping con un tocco dalle card dei live stream, dove i sats compaiono nell'overlay chat via [NIP-53](/it/topics/nip-53/). La v0.8.5 corregge un bug di deduplicazione della timeline.

### topaz v0.0.2 ships a Nostr relay for Android

[topaz](https://github.com/fiatjaf/topaz), nuovo relay Nostr che gira su telefoni Android creato da fiatjaf, ha pubblicato [v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2) il 17 aprile. Il progetto è Kotlin-first e punta a trasformare il telefono in un relay personale sempre disponibile. Per ora l'obiettivo è stretto: un relay funzionante in un pacchetto Android installabile.

### StableKraft v1.0.0 ships the first stable music-and-podcast PWA release

[StableKraft](https://github.com/ChadFarrow/stablekraft-app) è una PWA Next.js per scoprire, organizzare e ascoltare musica prelevata dai feed podcast, con Nostr per auth e funzioni social e Lightning per i pagamenti V4V. Ha raggiunto [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0) il 18 aprile. Nella stessa settimana il progetto ha stretto l'ingestion dei feed con una cache OPML di 15 minuti e la rimozione di XML illegale, e ha ridotto la finestra di reparse notturna da 720 ore a 24 ore per permettere ai feed aggiunti di recente di autoripararsi più in fretta.

### NipLock ships a NIP-17-based password manager

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) è un password manager che memorizza e sincronizza credenziali tra dispositivi usando messaggi diretti gift-wrapped [NIP-17](/it/topics/nip-17/). Ogni voce password è un DM NIP-17 dall'utente verso se stesso, cosi gli stessi eventi si replicano su qualunque dispositivo si autentichi con la stessa chiave. La firma funziona con `nsec` raw, estensioni browser come [nos2x](https://github.com/fiatjaf/nos2x) o [Amber](https://github.com/greenart7c3/Amber) via [NIP-46](/it/topics/nip-46/).

### flotilla-budabit polishes its NIP-34 repo surface

Il fork della comunità Budabit di [Flotilla](https://gitea.coracle.social/coracle/flotilla), [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit), ha pubblicato un gruppo di fix per il proprio workflow git-over-nostr NIP-34. Gli aggiornamenti ripristinano i controlli per la discussione dei repository, mantengono visibili le sticky repo tabs sulle pagine dettaglio, caricano gli annunci repo dai relay GRASP salvati e tengono sincronizzato lo stato delle patch applicate dai maintainer.

### rx-nostr 3.7.2 through 3.7.4 add default verifier and optional constructor args

[rx-nostr](https://github.com/penpenpng/rx-nostr), libreria Nostr basata su RxJS, ha pubblicato [3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2), [3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3) e [3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4). [PR #192](https://github.com/penpenpng/rx-nostr/pull/192) aggiunge un verificatore Schnorr predefinito e [PR #195](https://github.com/penpenpng/rx-nostr/pull/195) rende opzionali gli argomenti di `createRxNostr()` per integrazioni rapide a configurazione zero.

### Keep Android v1.0.0 ships with reproducible builds and zero trackers

[Keep](https://github.com/privkeyio/keep-android), gestore di password e segreti nativo Nostr, ha pubblicato [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0) il 21 aprile dopo una serie di PR di hardening. [PR #241](https://github.com/privkeyio/keep-android/pull/241) aggiunge una recipe per build riproducibili, [PR #248](https://github.com/privkeyio/keep-android/pull/248) sostituisce Google ML Kit con ZXing per rimuovere la dipendenza da Google Play Services, [PR #252](https://github.com/privkeyio/keep-android/pull/252) pubblica una scansione Exodus Privacy che mostra zero tracker e [PR #256](https://github.com/privkeyio/keep-android/pull/256) aggiunge un file `zapstore.yaml` per la distribuzione tramite [zapstore](https://zapstore.dev).

### Flotilla 1.7.3 and 1.7.4 add kind-9 wrapping for richer NIP-29 rooms

[Flotilla](https://gitea.coracle.social/coracle/flotilla), client per gruppi [NIP-29](/it/topics/nip-29/) di hodlbod, ha pubblicato [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) e [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4). Il cambiamento di protocollo principale è il wrapping dei tipi di contenuto non-chat dentro eventi kind `9`, annunciato nel [release note di hodlbod](nostr:nevent1qvzqqqqqqypzp978pfzrv6n9xhq5tvenl9e74pklmskh4xw6vxxyp3j8qkke3cezqyvhwumn8ghj76rzwghxxmmjv93kcefwwdhkx6tpdshszrnhwden5te0dehhxtnvdakz7qgawaehxw309a5x7ervvfhkgtnrdaexzcmvv5h8xmmrd9skctcqyrrclae7mhmm5dnumwfzhg3fxu74a4hh24jd8pvn8v0hye9w3g6tuljtr85) e collegato a [PR #2310](https://github.com/nostr-protocol/nips/pull/2310). Questo permette di preservare il contesto della stanza quando eventi come poll o calendario vengono inviati nel gruppo.

### WoT Relay v0.2.1 migrates eventstore to LMDB

[WoT Relay](https://github.com/bitvora/wot-relay), relay filtrato tramite web of trust di bitvora, ha pubblicato [v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1) il 22 aprile. [PR #97](https://github.com/bitvora/wot-relay/pull/97) migra l'eventstore a [LMDB](http://www.lmdb.tech/), [PR #99](https://github.com/bitvora/wot-relay/pull/99) aggiorna `golang.org/x/crypto` e [PR #100](https://github.com/bitvora/wot-relay/pull/100) aggiorna URL software e stringa versione in [NIP-11](/it/topics/nip-11/).

### Formstr suite: Pollerama security pass, Forms i18n, Calendar RRULE support

La suite Formstr ha unito 26 PR tra Pollerama, Formstr Forms e Nostr Calendar, con un tema chiaro di sicurezza sul lato poll e avanzamento funzionale sul resto.

[Pollerama](https://pollerama.fun), l'app [nostr-polls](https://github.com/formstr-hq/nostr-polls), rafforza la gestione delle chiavi. [PR #182](https://github.com/formstr-hq/nostr-polls/pull/182) scade i DM in cache al logout, [PR #175](https://github.com/formstr-hq/nostr-polls/pull/175) sposta la chiave locale in uno storage browser più sicuro e [PR #171](https://github.com/formstr-hq/nostr-polls/pull/171) protegge `JSON.parse` del contenuto profilo kind `0` in tutti i percorsi di login. [PR #186](https://github.com/formstr-hq/nostr-polls/pull/186) aggiunge deep linking HTTPS e [PR #169](https://github.com/formstr-hq/nostr-polls/pull/169) rende cliccabili i nomi degli autori nei risultati.

[Formstr](https://formstr.app), suite [nostr-forms](https://github.com/formstr-hq/nostr-forms), amplia la superficie di input e onboarding. [PR #475](https://github.com/formstr-hq/nostr-forms/pull/475) aggiunge supporto a URL audio e video, [PR #439](https://github.com/formstr-hq/nostr-forms/pull/439) introduce i18n, [PR #466](https://github.com/formstr-hq/nostr-forms/pull/466) aggiunge un importatore da Google Forms e [PR #463](https://github.com/formstr-hq/nostr-forms/pull/463) rimuove log sensibili dal browser console.

[Nostr Calendar by Formstr](https://calendar.formstr.app) ha pubblicato [v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0) e [v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0). [PR #107](https://github.com/formstr-hq/nostr-calendar/pull/107) aggiunge supporto multiplo e personalizzato a RRULE, [PR #101](https://github.com/formstr-hq/nostr-calendar/pull/101) interpreta come UTC le floating RRULE date secondo RFC 5545, [PR #97](https://github.com/formstr-hq/nostr-calendar/pull/97) permette di aggiungere eventi condivisi al proprio calendario, [PR #86](https://github.com/formstr-hq/nostr-calendar/pull/86) introduce preferenze di notifica per lista e [PR #112](https://github.com/formstr-hq/nostr-calendar/pull/112) rinnova login e loading path. Tutti e tre i progetti si basano sugli eventi calendario [NIP-52](/it/topics/nip-52/).

### Also shipped: notedeck, nostr.blue, cliprelay, Captain's Log

Alcuni client hanno pubblicato release iterative senza una singola headline dominante. [notedeck](https://github.com/damus-io/notedeck) ha pubblicato [v0.10.0-beta.4](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.4) con fix su rendering a colonne e relay pool. [nostr.blue v0.8.6](https://github.com/patrickulrich/nostr.blue/releases/tag/v0.8.6) aggiorna Dioxus e sblocca la build Android. [cliprelay](https://github.com/tajava2006/cliprelay) ha pubblicato [Desktop v0.0.3](https://github.com/tajava2006/cliprelay/releases/tag/desktop%2Fv0.0.3) e [Android v0.0.4](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.0.4), stringendo il loop di sync. [Captain's Log](https://github.com/nodetec/comet) ha pubblicato tre build alpha che aggiungono il rilevamento della liveness dei sync relay.

## In Development

### whitenoise-rs refactors to session-scoped account views

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), il daemon Rust sotto il client [Marmot](/it/topics/marmot/), ha unito 15 PR per una refactor multi-fase che sposta la logica da singleton globali a viste per-account `AccountSession`. L'obiettivo è scomporre un monolite condiviso in superfici più piccole, più facili da comprendere, testare ed evolvere senza effetti collaterali tra account diversi.

La base arriva con [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) e [PR #753](https://github.com/marmot-protocol/whitenoise-rs/pull/753), seguite dallo spostamento di draft, settings, operazioni messaggi, lettura e scrittura di gruppo, membership, notifiche push, letture dei key package e creazione dei gruppi nelle PR successive. [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770) chiude il giro reindirizzando il dispatch degli eventi sulla sessione, cosi ogni account consuma il proprio traffico relay senza contesa.

### White Noise app adds block/unblock UI, leave-group, and offline notices

[White Noise](https://github.com/marmot-protocol/whitenoise), client [Marmot](/it/topics/marmot/), aggiunge i controlli mancanti sul ciclo di vita dei gruppi. [PR #578](https://github.com/marmot-protocol/whitenoise/pull/578) pubblica la UI per block e unblock sopra l'hook introdotto in [PR #573](https://github.com/marmot-protocol/whitenoise/pull/573), [PR #571](https://github.com/marmot-protocol/whitenoise/pull/571) e [PR #572](https://github.com/marmot-protocol/whitenoise/pull/572) collegano `clear_chat`, `delete_chat` e `leave_and_delete_group` dal lato Rust all'app, e [PR #569](https://github.com/marmot-protocol/whitenoise/pull/569) insieme a [PR #576](https://github.com/marmot-protocol/whitenoise/pull/576) aggiungono avvisi offline nelle schermate chat e impostazioni. [PR #585](https://github.com/marmot-protocol/whitenoise/pull/585) restringe inoltre la cancellazione da "all key packages" a "legacy key packages".

### MDK adds mixed-version invite support and SelfUpdate convergence

[MDK](https://github.com/marmot-protocol/mdk), il [Marmot](/it/topics/marmot/) Development Kit, ha unito sette PR. La linea comune è la compatibilità tra versioni vicine, mantenendo i client in grado di invitarsi a vicenda, ruotare il proprio stato e recuperare da input malformati.

[PR #261](https://github.com/marmot-protocol/mdk/pull/261) calcola le `RequiredCapabilities` di un gruppo come LCD delle capability degli invitati e sblocca inviti tra [Amethyst](https://github.com/vitorpamplona/amethyst) e [White Noise](https://github.com/marmot-protocol/whitenoise). [PR #264](https://github.com/marmot-protocol/mdk/pull/264) converge il formato wire di SelfUpdate tra implementazioni, [PR #262](https://github.com/marmot-protocol/mdk/pull/262) valida i key package degli invitati prima di persistere il signer del creatore, [PR #256](https://github.com/marmot-protocol/mdk/pull/256) corregge la validazione della depletion admin lato ricevente, [PR #259](https://github.com/marmot-protocol/mdk/pull/259) protegge lo stato in-memory critico e [PR #265](https://github.com/marmot-protocol/mdk/pull/265) espone un accessor `group_required_proposals`.

### nostter adds NIP-44 encryption across people lists, bookmarks, and mutes

[nostter](https://github.com/SnowCait/nostter) ha unito 10 PR. [PR #2088](https://github.com/SnowCait/nostter/pull/2088) aggiunge cifratura [NIP-44](/it/topics/nip-44/) alle mute list, [PR #2089](https://github.com/SnowCait/nostter/pull/2089) la aggiunge ai bookmark e [PR #2090](https://github.com/SnowCait/nostter/pull/2090) alle people list, migrando dove possibile da [NIP-04](/it/topics/nip-04/). [PR #2087](https://github.com/SnowCait/nostter/pull/2087) rimuove anche un vecchio percorso di migrazione per le mute kind 30000.

### zap.cooking ships Nourish scoring and a reusable comment thread

[zap.cooking](https://github.com/zapcooking/frontend), client Nostr per ricette, ha unito 20 PR. La novità principale è un modulo Nourish per il punteggio nutrizionale delle ricette nelle [PR #317](https://github.com/zapcooking/frontend/pull/317) e [PR #319](https://github.com/zapcooking/frontend/pull/319). Accanto a questo, una refactor in quattro fasi da [PR #299](https://github.com/zapcooking/frontend/pull/299) a [PR #302](https://github.com/zapcooking/frontend/pull/302) estrae il modulo Comments in un `CommentThread` riutilizzabile.

### ridestr extracts shared rider coordinator

[ridestr](https://github.com/variablefate/ridestr), app di ride-sharing decentralizzata, ha unito 10 PR che rifattorizzano le schermate Compose in componenti più focalizzati ed estraggono la logica di protocollo per rider e driver in un modulo coordinatore condiviso `:common`. [PR #60](https://github.com/variablefate/ridestr/pull/60) aggiunge anche un ricevitore kind `3189` lato Roadflare.

### Blossom drafts a BUD-01 Sunset header for blob expiration

[Blossom](https://github.com/hzrd149/blossom), protocollo di hzrd149 per la memorizzazione di blob su server HTTP indicizzati da hash SHA-256, ha aperto [PR #99](https://github.com/hzrd149/blossom/pull/99) per aggiungere un header `Sunset` a BUD-01. Il server potrebbe usarlo per pubblicizzare un timestamp futuro dopo il quale un blob non sarà più servito, permettendo ai client di pianificare in anticipo invece di scoprire la scadenza solo con un 404.

## New Projects

### Forgesworn publishes a 29-repo cryptographic toolkit for Nostr

[Forgesworn](https://github.com/forgesworn) ha pubblicato 29 repository open source in cinque giorni, coprendo firma, identità, attestazioni, web of trust e discovery di API a pagamento su Nostr.

Lo stack di firma ruota attorno a [nsec-tree](https://github.com/forgesworn/nsec-tree), schema deterministico di derivazione di sotto-identità che trasforma un master secret in identità Nostr illimitate e non collegabili, e a [Heartwood](https://github.com/forgesworn/heartwood), signer remoto NIP-46 che gira su Raspberry Pi con Tor attivo per default. [Sapwood](https://github.com/forgesworn/sapwood) aggiunge una UI di gestione web, [heartwood-esp32](https://github.com/forgesworn/heartwood-esp32) porta lo stesso approccio su una board Heltec WiFi LoRa 32 e [nsec-tree-cli](https://github.com/forgesworn/nsec-tree-cli) espone i flussi di derivazione, prova e recupero Shamir.

Sul lato identità e fiducia, [Signet](https://github.com/forgesworn/signet) arriva a [v1.6.0](https://github.com/forgesworn/signet/releases/tag/v1.6.0) come protocollo di verifica dell'identità decentralizzata per Nostr, [nostr-attestations](https://github.com/forgesworn/nostr-attestations) definisce un singolo evento kind `31000` per credential, endorsement, provenance e trust, e [nostr-veil](https://github.com/forgesworn/nostr-veil) costruisce sopra un web of trust privacy-preserving con firme di anello LSAG su secp256k1.

Sul lato monetizzazione, [toll-booth](https://github.com/forgesworn/toll-booth) è un middleware L402 per Express, Hono, Deno, Bun e Cloudflare Workers che trasforma una API in un toll booth Lightning in una riga. [toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm) espone la API protetta come DVM [NIP-90](/it/topics/nip-90/), [toll-booth-announce](https://github.com/forgesworn/toll-booth-announce) la collega a [402-announce](https://github.com/forgesworn/402-announce), che pubblica eventi parameterized replaceable kind `31402` per la discovery di servizi HTTP 402 su Nostr, e [402-indexer](https://github.com/forgesworn/402-indexer) indicizza questi annunci. L'organizzazione pubblica anche una [collezione di 29 draft NIP](https://github.com/forgesworn/nip-drafts).

### ShockWallet ships Nostr-native Lightning wallet sync and multi-node connections

[ShockWallet](https://github.com/shocknet/wallet2) è un wallet Lightning che usa Nostr come trasporto per connettersi a nodi Lightning self-custodial. L'app si accoppia a uno o più nodi [Lightning.Pub](https://github.com/shocknet/Lightning.Pub) tramite un `nprofile`, poi firma le autorizzazioni di pagamento end-to-end tra wallet e nodo. Il team ha pubblicato [PR #608](https://github.com/shocknet/wallet2/pull/608) il 18 aprile con un pass UI sulla dashboard dei canali, accanto a un flusso QR con admin-invite-link per nuovi utenti PUB ([PR #606](https://github.com/shocknet/wallet2/pull/606)) e un fix di leggibilità della dashboard metriche ([PR #607](https://github.com/shocknet/wallet2/pull/607)).

ShockWallet usa gli eventi dati specifici per applicazione di [NIP-78](/it/topics/nip-01/) per la sincronizzazione multi-device dello stato del wallet, cosi la vista del wallet resta coerente tra browser desktop e telefono senza server centralizzato. Questo lo colloca un livello sotto [NIP-47](/it/topics/nip-47/): NIP-47 è l'interfaccia che un'app usa per chiedere a un wallet esistente di pagare, mentre ShockWallet usa Nostr come trasporto dell'account e della sessione del wallet verso il nodo Lightning sottostante.

### Nostrability issues migrate to git over Nostr after GitHub censorship

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues), il tracker di interoperabilità di elsat per client e relay Nostr, sta spostando il proprio workflow issue su git over Nostr dopo la rimozione dell'organizzazione Nostrability da GitHub. Il tracker migrato ora vive su GitWorkshop/ngit, dove i problemi esistenti sono già stati trasferiti e i futuri report di interoperabilità possono restare dentro un'infrastruttura nativa Nostr.

### nowhere encodes full websites into URL fragments and routes orders through Nostr

[nowhere](https://github.com/5t34k) è un nuovo progetto AGPL-3.0 di 5t34k che serializza un intero sito nel frammento URL dopo `#`, lo comprime con sostituzione di dizionario e raw DEFLATE e lo codifica in base64url. Poiché HTTP vieta al browser di inviare i frammenti al server, l'host che consegna la pagina non vede mai il contenuto e il sito stesso non viene memorizzato su un server. Il progetto include otto tipi di sito, cinque completamente statici e tre che usano relay Nostr per ordini, post e firme con chiavi effimere e cifratura [NIP-44](/it/topics/nip-44/).

### Small new surfaces: relayk.it and Brainstorm Search

Due progetti piccoli meritano una menzione rapida. [relayk.it](https://relayk.it), costruito da sam del team Soapbox, è un client per la discovery di relay costruito con Shakespeare che gira interamente nel browser. [Brainstorm Search](https://brainstorm.world) arriva come interfaccia di ricerca Nostr single-page focalizzata sull'emersione di contenuti attraverso la rete.

## Protocol and Spec Work

### NIP Updates

Proposte e discussioni recenti nel [repository NIPs](https://github.com/nostr-protocol/nips):

**Open PRs and Discussions:**

- **[NIP-67](/it/topics/nip-67/): EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): propone un terzo elemento facoltativo nel messaggio `EOSE` di [NIP-01](/it/topics/nip-01/) per indicare se il relay ha davvero consegnato tutti gli eventi memorizzati che corrispondono al filtro.
- **NIP-5D: Nostr Applets** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): propone un nuovo kind per distribuire applet interattive su Nostr, tra [NIP-5A](/it/topics/nip-5a/) per siti statici e [NIP-5C](/it/topics/nip-5c/) per scroll WASM.
- **NIP-29: Subgroups spec** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319)): estende [NIP-29](/it/topics/nip-29/) con una gerarchia di sottogruppi, cosi un singolo gruppo può ospitare più canali paralleli senza creare gruppi indipendenti.
- **NIP-29: Explicit role permissions on kind 39003** ([PR #2316](https://github.com/nostr-protocol/nips/pull/2316)): definisce uno schema esplicito dei permessi nei ruoli kind `39003`, rendendo leggibili a client e utenti i poteri effettivi di un ruolo come moderator.
- **NIP-11: access_control field for gated-relay discovery** ([PR #2318](https://github.com/nostr-protocol/nips/pull/2318)): aggiunge un oggetto `access_control` facoltativo a [NIP-11](/it/topics/nip-11/) per descrivere il modello di accesso del relay.
- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): continua a iterare sulla forma dell'evento kind `10164` e sul layout dei campi per regole di subscription per livello.
- **NIP-XX: Agent Reputation Attestations (Kind 30085)** ([PR #2320](https://github.com/nostr-protocol/nips/pull/2320)): propone un evento addressable kind `30085` per attestazioni firmate su agenti e servizi autonomi in Nostr, con punteggi, evidenze e supporto ai mercati [NIP-90](/it/topics/nip-90/).
- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): prosegue il lavoro sul kind `20411`, sulla forma di cifratura [NIP-44](/it/topics/nip-44/) per destinatario e sulla semantica del tag `ttl`.
- **marmot-ts 0.5.0 release PR** ([PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)): la PR di release per `@internet-privacy/marmot-ts@0.5.0` include i primi breaking changes pianificati nel client TypeScript Marmot.

## NIP Deep Dive: NIP-72 (Moderated Communities)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) definisce un modello di community tematiche su Nostr in cui i moderator curano una vista di lettura sopra scritture altrimenti non ristrette. Diversamente dai gruppi basati su relay di [NIP-29](/it/topics/nip-29/), una community NIP-72 vive in eventi Nostr ordinari e qualunque relay che porti i kind rilevanti può servirla. Chiunque può pubblicare in una community, ma solo i post approvati da un moderator riconosciuto compaiono nel feed della community.

Una community è definita da un evento addressable kind `34550` pubblicato dal suo creatore. Il tag `d` è lo slug stabile della community, i tag `name`, `description`, `image` e `rules` portano i metadati di presentazione, e una serie di tag `p` marcati `moderator` elenca le pubkey i cui approval contano. Tag `relay` facoltativi con marker `author`, `requests` o `approvals` suggeriscono dove pubblicare e recuperare ciascun tipo di evento:

```json
{
  "id": "f1e2d3c4b5a69788f1e2d3c4b5a69788f1e2d3c4b5a69788f1e2d3c4b5a69788",
  "pubkey": "c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2",
  "created_at": 1745280000,
  "kind": 34550,
  "tags": [
    ["d", "bitcoin-devs"],
    ["name", "Bitcoin Devs"],
    ["description", "A moderated community for Bitcoin protocol discussion."],
    ["image", "https://example.com/bitcoin-devs.png"],
    ["rules", "Stay on topic. Cite code or specs when possible."],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876", "", "moderator"],
    ["p", "a1b2c3d4e5f6a7b8c9d0a1b2c3d4e5f6a7b8c9d0a1b2c3d4e5f6a7b8c9d0a1b2", "", "moderator"],
    ["relay", "wss://relay.example.com", "author"],
    ["relay", "wss://relay.moderator.com", "approvals"]
  ],
  "content": "",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Un utente invia un post pubblicando un normale evento Nostr e aggiungendo un tag `a` con coordinata `34550:<creator_pubkey>:<slug>`. L'approvazione è un evento separato kind `4549` pubblicato da un moderator. Questo evento riferisce il post tramite tag `e`, il submitter tramite tag `p` e la community tramite tag `a`, e inserisce nel `content` una copia stringified dell'evento inviato. Questo mantiene renderizzabile il post approvato anche se l'autore originale elimina in seguito l'evento sorgente.

```json
{
  "id": "a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1745283600,
  "kind": 4549,
  "tags": [
    ["a", "34550:c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2:bitcoin-devs"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["p", "e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5"],
    ["k", "1"]
  ],
  "content": "{\"id\":\"b3c4d5e6...\",\"pubkey\":\"e4f5a6b7...\",\"kind\":1,\"content\":\"Question about sighash flags\",\"tags\":[[\"a\",\"34550:c3d2e1f0...:bitcoin-devs\"]],\"created_at\":1745283500,\"sig\":\"...\"}",
  "sig": "bbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aa"
}
```

Il modello di approvazione ha tre proprietà utili. La moderazione è trasparente, perché ogni approval è un evento Nostr firmato che chiunque può recuperare e verificare. Non è esclusiva, perché lo stesso post può essere approvato da community diverse. Ed è reversibile al livello di lettura, perché se una community rimuove un moderator dal suo evento kind `34550`, le approvazioni precedenti di quel moderator smettono di contare per i client che rispettano la lista corrente dei moderator.

Il lato lettura è il punto in cui i client divergono. Molti client community-aware renderizzano il feed filtrando gli eventi kind `4549` taggati con la coordinata della community, deduplicando per ID dell'evento sottostante e poi renderizzando il post embedded. Alcuni recuperano anche direttamente i submission event e usano gli approval solo come whitelist. Client come [noStrudel](https://github.com/hzrd149/nostrudel) e, da questa settimana, [Amethyst](https://github.com/vitorpamplona/amethyst) via [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468), espongono anche la coda dei post pendenti ai moderator. Rispetto a [NIP-29](/it/topics/nip-29/), il compromesso è chiaro: NIP-72 è più portabile e forkabile, mentre NIP-29 è più adatto quando spam e post non approvati devono restare del tutto fuori dal wire.

## NIP Deep Dive: NIP-57 (Zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md) definisce gli zaps, un modo per collegare pagamenti Lightning a identità ed eventi Nostr e pubblicare una ricevuta verificabile del pagamento sui relay. Uno zap prova che un determinato mittente ha pagato un determinato importo a un destinatario specifico per un target specifico, e la prova è leggibile da qualunque client Nostr senza doversi fidare della parola del mittente. La specifica attraversa LNURL, Lightning e Nostr e fissa come devono cooperare.

Il flusso coinvolge quattro attori. Il client del mittente scopre l'endpoint LNURL del destinatario dai metadati profilo kind `0` (`lud06` o `lud16`) o da un tag `zap` sull'evento da zappare. Quel client firma poi un evento zap request kind `9734` che descrive il pagamento desiderato e lo invia al callback LNURL del destinatario, non ai relay. Dall'altra parte, il server LNURL del destinatario valida la richiesta, restituisce una invoice Lightning il cui description hash si impegna alla richiesta stringified e, una volta pagata la invoice, pubblica una ricevuta kind `9735` sull'insieme di relay richiesto dal mittente.

Una zap request kind `9734` contiene un tag `p` con la pubkey del destinatario, opzionalmente un tag `e` o `a` che identifica il contenuto da finanziare, un tag `amount` in millisats, un tag `relays` che elenca dove pubblicare la ricevuta e un tag `k` che registra il kind del target:

```json
{
  "id": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "pubkey": "a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876",
  "created_at": 1745280000,
  "kind": 9734,
  "tags": [
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["amount", "21000"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol", "wss://relay.nostr.band"],
    ["k", "1"]
  ],
  "content": "great post",
  "sig": "ccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbcc"
}
```

La ricevuta zap kind `9735` viene pubblicata dal wallet server del destinatario dopo la conferma del pagamento. Non è firmata dal mittente ma dal wallet server usando la `nostrPubkey` pubblicizzata nella risposta LNURL. Una ricevuta valida porta la richiesta zap stringified nel tag `description`, la invoice pagata nel tag `bolt11` e un tag `preimage` che prova il settlement:

```json
{
  "id": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "pubkey": "e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0",
  "created_at": 1745280060,
  "kind": 9735,
  "tags": [
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["P", "a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["bolt11", "lnbc210n1pj...bolt11invoicestring"],
    ["description", "{\"id\":\"c1d2e3f4...\",\"pubkey\":\"a5b4c3d2...\",\"kind\":9734,\"content\":\"great post\",\"tags\":[...]}"],
    ["preimage", "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"]
  ],
  "content": "",
  "sig": "ddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccdd"
}
```

La regola di validazione è il cuore delle garanzie di NIP-57. Un client che mostra una ricevuta kind `9735` come zap dovrebbe verificare quattro cose: che la firma della ricevuta corrisponda alla `nostrPubkey` annunciata nella risposta LNURL, che l'importo della invoice `bolt11` corrisponda al tag `amount` nella richiesta embedded, che il description hash della invoice si impegni alla richiesta zap stringified e che il `preimage` faccia hash al `payment_hash` della invoice. Una ricevuta che fallisce uno di questi controlli è solo una dichiarazione di pagamento, non una prova.

I private zaps aggiungono riservatezza. Il mittente può cifrare il `content` della richiesta per il destinatario e includere un tag `anon`, cosi la rete relay vede il target del pagamento ma non legge la nota allegata. Alcuni client fanno un passo in più e generano una coppia di chiavi effimera per la richiesta stessa, cosi la ricevuta continua a provare che il pagamento è avvenuto ma il destinatario non può ricollegare lo zap alla pubkey di lunga durata del mittente.

NIP-57 sostiene anche il sistema di zap goals di [NIP-75](/it/topics/nip-75/). Un goal è un evento kind `9041` che dichiara un target e un insieme di relay sui quali contano le ricevute. Qualunque ricevuta zap collegata all'ID dell'evento del goal contribuisce al suo avanzamento. Client come [Amethyst](https://github.com/vitorpamplona/amethyst) sommano gli importi validati dei `bolt11` per mostrare il progresso e una classifica dei top zapper nella schermata [NIP-53](/it/topics/nip-53/) Live Activities.

Le zap split sono definite in un'appendice del NIP. Un destinatario può pubblicare un profilo kind `0` con più tag `zap`, ciascuno con un peso, cosi un singolo zap viene diviso tra più pubkey secondo i pesi pubblicati. Client come [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus) e [noStrudel](https://github.com/hzrd149/nostrudel) implementano già il pagamento split end-to-end.

---

Questo è tutto per questa settimana. Se state costruendo qualcosa o avete notizie da condividere, scriveteci su Nostr o passate da [nostrcompass.org](https://nostrcompass.org).
