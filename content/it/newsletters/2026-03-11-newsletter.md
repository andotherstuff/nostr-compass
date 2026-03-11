---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [Shopstr](https://github.com/shopstr-eng/shopstr) e [Milk Market](https://github.com/shopstr-eng/milk-market) aggiungono superfici MCP per il commerce guidato da agenti, mentre [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) e [strfry](https://github.com/hoytech/strfry) aggiungono supporto relay-auth e protected-event per [NIP-42](/it/topics/nip-42/) (Autenticazione dei client ai relay) tra software applicativo, signer e relay. [Route96](https://github.com/v0l/route96) rilascia due versioni attorno a labeling AI, code di moderazione, perceptual hashing e documentazione server machine-readable. [Samizdat](https://github.com/satsdisco/samizdat), già live sul web, ha pubblicato la sua prima alpha Android e in seguito ha aggiunto il supporto signer di [NIP-55](/it/topics/nip-55/) (Applicazione signer Android). [Formstr](https://github.com/formstr-hq/nostr-forms) aggiunge il signup tramite [NIP-49](/it/topics/nip-49/) (Cifratura della chiave privata), [Amethyst](https://github.com/vitorpamplona/amethyst) distribuisce il lavoro di risoluzione [NIP-05](/it/topics/nip-05/) (Verifica del dominio) basato su Namecoin, [Mostro](https://github.com/MostroP2P/mostro) distribuisce [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), e il repository NIPs unisce [NIP-91](/it/topics/nip-91/) (Operatore AND per i filtri) e linee guida difensive per [NIP-66](/it/topics/nip-66/) (Scoperta dei relay e monitoraggio della liveness).

## Notizie

### Shopstr e Milk Market aprono superfici commerce MCP

[Shopstr](https://github.com/shopstr-eng/shopstr), il marketplace peer-to-peer con pagamenti Lightning e Cashu, ha unito [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), aggiungendo un server MCP con autenticazione tramite API key per la gestione degli account da parte degli agenti. La modifica aggiunge `.well-known/agent.json` per la scoperta degli agenti, endpoint MCP di onboarding e stato, route per creazione ordini e verifica dei pagamenti, tool dedicati per acquisto e lettura, e una schermata impostazioni per le API key. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) estende il tutto con azioni lato venditore per messaggi, indirizzi, aggiornamenti degli ordini e selezione delle specifiche di prodotto. Una correzione di sicurezza in [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) sostituisce l'hashing SHA-256 delle API key a singola iterazione con PBKDF2 con salt a 100.000 iterazioni.

Gli agenti possono leggere gli annunci [NIP-99](/it/topics/nip-99/) (Annunci classificati) e passare al checkout usando i flussi di pagamento esistenti di [NIP-47](/it/topics/nip-47/) (Nostr Wallet Connect) e [NIP-60](/it/topics/nip-60/) (Wallet Cashu), senza fare scraping delle pagine o reverse engineering del comportamento del client.

[Milk Market](https://github.com/shopstr-eng/milk-market), marketplace alimentare su Nostr disponibile su [milk.market](https://milk.market), ha introdotto la stessa base MCP e API key con [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) aggiunge ordini in abbonamento, modifica dell'indirizzo di spedizione dopo l'acquisto, e gestione del checkout multi-merchant e multi-valuta per Stripe e altri percorsi di pagamento fiat. Una successiva [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) corregge un bug di inizializzazione del database all'avvio, in cui la tabella delle pubblicazioni relay fallite non veniva creata sulle installazioni fresche, causando errori 500 al primo caricamento. L'interfaccia rivolta agli agenti funziona con checkout nativo Bitcoin su Shopstr oppure con checkout misto fiat e Bitcoin su Milk Market.

### NIP-42 relay auth tra bunker, signer e relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), un bunker [NIP-46](/it/topics/nip-46/) (Nostr Connect) che collega provider OAuth alla firma Nostr, ha aggiunto login [NIP-07](/it/topics/nip-07/) (Signer estensione browser), selezione automatica della singola identità e pulizia delle identità eliminate ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Quando esiste una sola identità, il bunker ora la seleziona automaticamente invece di chiedere conferma. Eliminare un'identità rimuove anche assegnazioni e connessioni pendenti. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) aggiunge un percorso di configurazione `ALWAYS_ALLOWED_KINDS` per gli utenti assegnati, con valore predefinito kind `30078` per dati specifici dell'app, così le identità delegate possono scrivere nello storage dell'app senza approvazione per evento.

[Amber](https://github.com/greenart7c3/Amber), il signer [NIP-55](/it/topics/nip-55/) principale per Android, ha distribuito [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) con quattro pre-release nel corso della settimana. [PR #317](https://github.com/greenart7c3/Amber/pull/317) aggiunge la gestione dell'autenticazione relay [NIP-42](/it/topics/nip-42/) per richieste kind `22242`. L'implementazione aggiunge una nuova colonna al database che traccia i permessi specifici per relay con un indice univoco su `(pkKey, type, kind, relay)`. Gli utenti vedono una schermata auth dedicata da cui possono consentire o negare per relay oppure su tutti i relay con uno scope wildcard `*`, e rendere persistente la scelta. I permessi wildcard cancellano tutte le voci specifiche per relay per quel kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) prosegue rifattorizzando le schermate delle richieste multi-evento per mostrare i dettagli inline usando card composable invece di navigare verso una schermata separata. Il rilascio aggiorna inoltre i relay di profilo predefiniti, aggiunge la visualizzazione delle richieste in bottom sheet e corregge un crash sui dispositivi MediaTek disabilitando il keystore StrongBox.

Sul lato relay, [strfry PR #156](https://github.com/hoytech/strfry/pull/156) implementa la gestione auth NIP-42 per [NIP-70](/it/topics/nip-70/) (Eventi protetti), e [PR #176](https://github.com/hoytech/strfry/pull/176) rifiuta i repost che incorporano eventi protetti.

<a id="notedeck-aggiunge-limiti-relay-nip-11-e-funzionalita-agentium"></a>
### Notedeck aggiunge limiti relay NIP-11 e funzionalità Agentium

[Notedeck](https://github.com/damus-io/notedeck), il client desktop nativo del team Damus, ha unito 14 PR questa settimana. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) aggiunge il fetch dei limiti relay di [NIP-11](/it/topics/nip-11/) (Documento informativo del relay), così tutti i relay outbox rispettano ora `max_message_length` e `max_subscriptions` dal documento informativo del relay. L'implementazione include elaborazione di job in background, exponential backoff con jitter per i retry di connessione, e header HTTP Accept personalizzati. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) corregge un bug per cui i DM a volte non si caricavano dopo il cambio account, e [PR #1333](https://github.com/damus-io/notedeck/pull/1333) aggiunge un meccanismo di backoff alla comunicazione relay multicast per prevenire spam di broadcast sugli errori.

Il sottosistema Agentium (la UI di coding agent integrata in Notedeck, internamente chiamata "Dave") ha ricevuto incolla immagini dagli appunti, configurazioni di esecuzione nominate che si sincronizzano tra dispositivi tramite eventi kind `31991` ([NIP-33](/it/topics/nip-33/) (Eventi sostituibili parametrizzati)), un creatore di git worktree e un selettore di modelli per scegliere i backend per sessione ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integra `egui_kittest` per test UI headless, e [PR #1339](https://github.com/damus-io/notedeck/pull/1339) aggiunge una card dashboard che traccia le nuove creazioni di contact list per client. Una [PR #1314](https://github.com/damus-io/notedeck/pull/1314) ancora aperta porta in Notedeck la risoluzione NIP-05 di Amethyst basata su Namecoin con lookup ElectrumX, instradamento Tor SOCKS5 e integrazione nella barra di ricerca.

### diVine distribuisce v1.0.6 con infrastruttura di test E2E e import NIP-49

[diVine](https://github.com/divinevideo/divine-mobile), il client video short-form in loop che ripristina gli archivi Vine su [divine.video](https://divine.video), ha distribuito [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) con 127 PR unite. Il rilascio aggiunge import account [NIP-49](/it/topics/nip-49/), supporto esterno [NIP-05](/it/topics/nip-05/), gestione multi-account, build macOS e Linux sperimentali, e una libreria bozze e clip ridisegnata basata su storage locale.

Sul lato ingegneristico, [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) aggiunge un'infrastruttura completa di test di integrazione E2E usando Patrol per l'automazione UI nativa contro uno stack backend Docker (relay, API, Blossom, Postgres, Redis, ClickHouse). Cinque test del percorso auth coprono registrazione, verifica, reset password, scadenza sessione e refresh del token. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) cambia il caricamento video da HLS-first a MP4 diretto con fallback automatico a HLS, riducendo i tempi di caricamento da 30-60 secondi a quasi istantanei. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) mette in cache la risposta API del feed home in SharedPreferences per una visualizzazione istantanea al cold start. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) applica le etichette `ai-generated` come nascoste nei feed, e [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) aggiunge un'impostazione di sicurezza per mostrare solo video ospitati da diVine. La migrazione della cache profili da Hive a Drift continua in [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) e [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), sostituendo circa 1.074 linee di codice Hive con DAO Drift.

### Vector v0.3.2 distribuisce sincronizzazione negentropy NIP-77 e miglioramenti MLS

[Vector](https://github.com/VectorPrivacy/Vector), messenger desktop orientato alla privacy che usa cifratura di gruppo MLS con [NIP-17](/it/topics/nip-17/) (Messaggi diretti privati) e [NIP-44](/it/topics/nip-44/) (Payload cifrati), ha distribuito [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). La modifica principale è la negentropy NIP-77 per la sincronizzazione dei gruppi MLS ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), che recupera i messaggi persi molto più velocemente usando parallel boot. Il rilascio aggiunge anche un motore audio ricostruito con pieno supporto Linux, spoiler per immagini con anteprime sfocate, hyperlink cliccabili con rich link preview, ping `@mention` con `@everyone` per gli admin di gruppo, autocomplete degli shortcode emoji, silenziamento dei gruppi, tap-to-react sulle reazioni esistenti e upload di file annullabili. Vector filtra esplicitamente gli eventi di chat di gruppo NIP-17 ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), usando MLS esclusivamente per la cifratura di gruppo.

## Rilasci

### Route96 v0.5.0 e v0.5.1

[Route96](https://github.com/v0l/route96), un media server che supporta Blossom e [NIP-96](/it/topics/nip-96/) (Storage file HTTP), ha distribuito [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) e [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). La v0.5.0 aggiunge labeling AI automatizzato, backfill retroattivo per upload senza etichetta, code di moderazione per file segnalati, rifiuto della privacy basato su EXIF e gestione degli hash bannati.

La v0.5.1 aggiunge hash percettivi delle immagini, locality-sensitive hashing per il lookup di immagini simili, endpoint admin batch, e un [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) pubblicato che descrive la superficie API del server per Blossom e NIP-96 per tool agentici. [PR #58](https://github.com/v0l/route96/pull/58) sposta i worker in background su task Tokio completamente async, e [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) aggiunge backoff per evitare hot loop.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), lettore e publisher long-form disponibile su [samizdat.press](https://samizdat.press), ha distribuito la sua prima build Android in [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). L'app si apre su una pagina Press curata di articoli long-form Nostr con navigazione a tab inferiori tra viste Press, Feed, Saved e Write. La build Android aggiunge storage nativo delle chiavi tramite cifratura Android Keystore con sblocco biometrico, gestisce URI `nostr:` e deep link `samizdat.press`, e supporta il passaggio al signer tramite Android app chooser (Amber, Primal, ecc.) invece di richiedere l'import diretto della chiave. Pull-to-refresh, gestione delle safe area su schermi di varie dimensioni, e integrazioni native per condivisione, appunti, haptic e splash screen fanno ora parte della shell Android invece del wrapper web.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) aggiunge la firma intent-based [NIP-55](/it/topics/nip-55/) per i flussi Amber e Primal, e [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) sostituisce un workaround basato su bridge JavaScript con un plugin Capacitor nativo che usa `startActivityForResult`. L'app richiede Android 7.0+ (API 24), viene distribuita come APK debug in questa alpha e ancora non ha notifiche push. La pubblicazione dipende al momento da un'app signer, mentre il login `nsec` copre la lettura locale e l'accesso all'account.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), applicazione calendario decentralizzata con condivisione di eventi privati [NIP-59](/it/topics/nip-59/) (Gift Wrap) disponibile su [calendar.formstr.app](https://calendar.formstr.app), ha distribuito [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) con [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). Il rilascio estende la gestione degli eventi ricorrenti per [NIP-52](/it/topics/nip-52/) (Eventi calendario), andando oltre la base a evento singolo della v0.1.0. Le modifiche sottostanti toccano anche storage locale degli eventi, gestione del signer e plumbing delle notifiche Android. Questa è la seconda applicazione attiva dell'organizzazione Formstr dopo la migrazione del repository del mese scorso.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), lo scambio Bitcoin peer-to-peer costruito su Nostr, ha distribuito [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). Sono incluse le correzioni di restore della sessione dispute ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) e di auto-close ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) [trattate la settimana scorsa](/it/newsletters/2026-03-04-newsletter/). Novità di questo rilascio: [PR #625](https://github.com/MostroP2P/mostro/pull/625) aggiunge un campo `days` agli eventi di rating utente di kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) aggiunge una scadenza a quegli eventi di rating, e [PR #614](https://github.com/MostroP2P/mostro/pull/614) fa passare gli eventi ordine a impostazioni di scadenza configurate invece di una finestra hardcoded di 24 ore. [PR #622](https://github.com/MostroP2P/mostro/pull/622) aggiunge un controllo di idempotenza per prevenire pagamenti duplicati delle development fee.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), client Flutter per lo scambio P2P Mostro, ha distribuito [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) con 11 nuove funzionalità e 11 bug fix. Il rilascio aggiunge rendering multimediale cifrato nella chat dispute ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), chiusura automatica della UI dispute quando gli ordini raggiungono uno stato terminale ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), scansione QR per l'import wallet NWC ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), traduzioni francesi e gestione delle notifiche push FCM. [PR #496](https://github.com/MostroP2P/mobile/pull/496) corregge un bug di padding delle firme Schnorr bloccando la dipendenza bip340 alla v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), il client di messaggistica in stile Telegram con supporto Cashu, ha distribuito [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) focalizzata sulle correzioni Linux desktop: icone dock AppImage, rendering delle emoji, freeze dei menu contestuali e blocchi della UI reply/copy. Il rilascio corregge anche problemi di upload immagini e integrazione npub.cash. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) elimina rebuild UI non necessari rimuovendo un timer di polling a 3 secondi che forzava repaint glassmorphic senza fare nulla, e sblocca l'inizializzazione del login eseguendo il caricamento della cache eventi in parallelo invece di bloccare l'avvio di relay, contatti e canali.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), signer FROST threshold per Android con supporto [NIP-55](/it/topics/nip-55/) e [NIP-46](/it/topics/nip-46/), ha distribuito [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) e [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). La v0.6.0 aggiunge coordinamento dei wallet descriptor e UI di gestione, un flusso di backup/ripristino con autenticazione biometrica ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), recupero `nsec` da share threshold ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), generazione cross-platform di frame QR animati via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)), e una traccia di audit della firma con verifica della catena ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). La v0.6.1 cambia la licenza da AGPL-3.0 a MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), il gateway statico per visualizzare contenuti Nostr su [njump.me](https://njump.me), ha distribuito [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) con una modifica incompatibile nel parsing dei codici `note1` e un aggiornamento della libreria nostr sottostante.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), applicazione decentralizzata di segnalazione eventi stradali che usa Nostr, ha distribuito la sua prima demo release [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). L'app mostra gli eventi stradali su una mappa usando vector tile da openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), applicazione di e-bill con un livello di trasporto Nostr e relay dedicato su [bit.cr](https://www.bit.cr/), ha distribuito [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) aggiunge campi `payment_actions` e `bill_state` all'API per stato di pagamento e accettazione, e [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) corregge la gestione dell'indirizzo di firma per signer anonimi.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), applicazione chat costruita sulle librerie .NET MLS e C# del protocollo Marmot, ha distribuito [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). Il rilascio aggiunge supporto per signer esterni per Amber e flussi [NIP-46](/it/topics/nip-46/) ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), sposta la persistenza dello stato MLS nel servizio MLS per eliminare la perdita di dati nella finestra di crash ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), e pubblica build Windows, Linux e Android tramite una nuova pipeline CI.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), trading copilot Kotlin Multiplatform per Nostr, ha distribuito [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). Il rilascio impacchetta moduli KMP condivisi per logica di dominio, rendering dei grafici, autenticazione e pubblicazione Nostr, supporto all'upload Blossom [NIP-96](/it/topics/nip-96/) e hook di inferenza AI basati su ONNX tra shell Desktop e Android. L'architettura pubblicata include anche un servizio AI FastAPI per l'analisi degli screenshot dei grafici, pipeline di training dei modelli e un risk engine che produce trade plan strutturati con sizing e warning. Il login supporta sia chiavi `nsec` grezze sia signer esterni, e il flusso di output termina con la pubblicazione di eventi Nostr invece che con analisi solo locali.

## Aggiornamenti dei progetti

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), l'alternativa a Google Forms su Nostr, ha unito [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), aggiungendo un flusso di signup che usa chiavi private cifrate [NIP-49](/it/topics/nip-49/) (Cifratura della chiave privata). Prima di questo cambiamento, gli utenti avevano bisogno di un'estensione browser [NIP-07](/it/topics/nip-07/) oppure di incollare un `nsec` grezzo per usare Formstr. Il nuovo flusso genera una coppia di chiavi lato client, cifra la chiave privata con una password scelta dall'utente tramite lo schema scrypt + XChaCha20-Poly1305 di NIP-49, e memorizza la stringa `ncryptsec` risultante. Gli utenti possono quindi effettuare di nuovo il login con la loro password senza installare un'estensione signer. La gestione delle chiavi resta interamente lato client.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android ricco di funzionalità, ha unito quattro PR che distribuiscono il lavoro di risoluzione [NIP-05](/it/topics/nip-05/) basato su Namecoin che era [aperto la settimana scorsa](/it/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) aggiunge verifica NIP-05 resistente alla censura via ElectrumX per identificatori `.bit`, `d/` e `id/`. Quando Amethyst rileva uno di questi suffissi in un campo NIP-05, interroga un server ElectrumX-NMC per la cronologia delle transazioni del nome, analizza lo script `NAME_UPDATE` dall'output più recente per estrarre la pubkey Nostr, e rifiuta i nomi più vecchi di 36.000 blocchi (la finestra di scadenza di Namecoin). Le connessioni ElectrumX passano tramite SOCKS5 quando Tor è abilitato, con selezione dinamica del server tra endpoint clearnet e `.onion`. Una cache LRU con TTL di un'ora previene query ripetute alla blockchain.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) corregge race condition e correttezza del resolver in quel flusso. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) permette ai nuovi utenti di importare una follow list durante il signup da identificatori NIP-05 ordinari o basati su Namecoin. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) aggiunge impostazioni personalizzate del server ElectrumX così gli utenti possono scegliere quale server gestisce i lookup.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), libreria che fornisce metodi helper per memorizzare eventi Nostr in IndexedDB, ha unito [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) aggiungendo supporto ai filtri tag AND di [NIP-91](/it/topics/nip-91/). La modifica aggiunge la semantica di intersezione al matching dei filtri lato client, così le query IndexedDB possono richiedere tutti i valori di tag elencati invece di uno qualsiasi. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) aggiorna la libreria all'ultima interfaccia NIP-DB, e un successivo [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) corregge un deadlock nelle subscribe e rimuove nostr-tools come dipendenza di produzione.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), indexer Nostr archive-first con analytics ClickHouse, ha unito [PR #8](https://github.com/andotherstuff/pensieve/pull/8) che aggiunge enforcement della cache TTL per entry e coalescenza dei miss per chiave per ridurre i picchi di CPU dell'API. Gli endpoint time-series con costo più alto (statistiche di engagement, attività oraria, attività per kind) usano ora TTL server-side di 10 minuti invece di innescare tempeste di ricalcolo sincronizzate.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), protocollo e server stack decentralizzato per media hosting, ha unito due aggiornamenti di autorizzazione BUD-11. [PR #91](https://github.com/hzrd149/blossom/pull/91) sposta l'autorizzazione opzionale nel suo stesso BUD e chiarisce il ruolo dei tag `x` e `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) pulisce il comportamento auth specifico per endpoint e formalizza l'header `X-SHA-256` per la verifica degli upload. Le due PR consolidano la logica auth in BUD-11 e rimuovono ambiguità attorno all'hashing delle richieste per flussi di upload, delete e gestione dei media.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti:**

- **[NIP-91](/it/topics/nip-91/) (Operatore AND per i filtri)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): Aggiunge la semantica di intersezione per i filtri tag, permettendo ai relay di rispondere a query che richiedono tutti i valori di tag elencati invece di uno qualsiasi. Riduce il post-filtering lato client e la larghezza di banda nelle query ricche di tag.

- **[NIP-66](/it/topics/nip-66/) (Scoperta dei relay e monitoraggio della liveness): misure difensive** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): In seguito al [lavoro sui benchmark outbox trattato la settimana scorsa](/it/newsletters/2026-03-04-newsletter/), la spec aggiunge ora avvertimenti sui percorsi negativi per i dati di monitoraggio dei relay. I client non devono richiedere eventi di monitoraggio kind `30166` per poter funzionare. Un monitor può essere sbagliato, obsoleto o malevolo. I client devono incrociare le fonti ed evitare di tagliare fuori ampie parti del grafo relay di un utente basandosi su un singolo feed.

- **[NIP-39](/it/topics/nip-39/) (Identità esterne nei profili): pulizia del registro kind 10011** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): Aggiunge il riferimento al kind `10011` direttamente nella spec, allineandosi con l'implementazione di Amethyst [trattata la settimana scorsa](/it/newsletters/2026-03-04-newsletter/).

**PR aperte e discussioni:**

- **[NIP-70](/it/topics/nip-70/) (Eventi protetti): rifiutare i repost che incorporano eventi protetti** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): Se un relay applica NIP-70 all'evento originale ma accetta repost che trasportano lo stesso contenuto, il tag `-` non ha alcun effetto pratico. Questa PR aggiunge la regola secondo cui i relay devono rifiutare anche i repost kind 6 e kind 16 di eventi protetti. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) lo implementa già.

- **[NIP-71](/it/topics/nip-71/) (Eventi video): tracce audio multiple** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): Aggiunge tag audio `imeta` per tracce alternative, varianti linguistiche e stream solo audio. Un client potrebbe mantenere stabile un file video cambiando lingua audio, oppure servire l'audio come traccia separata per contenuti in stile podcast.

- **[NIP-11](/it/topics/nip-11/) (Documento informativo del relay) e attributi relay [NIP-66](/it/topics/nip-66/)** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Aggiunge un campo strutturato `attributes` ai documenti informativi dei relay, offrendo a client e tool di discovery metadata machine-readable oltre all'attuale descrizione testuale libera.

## Approfondimento NIP: NIP-49 (Cifratura della chiave privata)

[NIP-49](/it/topics/nip-49/) definisce come un client cifra una chiave privata con una password e codifica il risultato come stringa bech32 `ncryptsec`. [Formstr](#formstr) usa NIP-49 nel suo nuovo flusso di signup.

Il formato non è legato a un kind di evento dedicato. Un client parte dalla chiave privata secp256k1 grezza di 32 byte, deriva una chiave simmetrica dalla password dell'utente con scrypt, cifra la chiave usando XChaCha20-Poly1305, poi incapsula il risultato in una stringa bech32 `ncryptsec`. Un flag di un byte registra se la chiave sia mai stata nota come gestita in modo insicuro prima della cifratura.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

L'evento JSON sopra è un esempio a livello applicativo, non un requisito di NIP-49. Il NIP standardizza il formato della chiave cifrata. Un client può memorizzare `ncryptsec` localmente, sincronizzarlo tramite storage specifico dell'app, oppure esportarlo come stringa di backup. Le password sono normalizzate in Unicode NFKC prima della derivazione della chiave, così la stessa password viene decifrata in modo coerente tra client e piattaforme.

Il flag di sicurezza della chiave a un byte ha tre valori definiti: `0x00` significa che la storia di gestione della chiave è sconosciuta, `0x01` significa che la chiave è nota per essere stata gestita in modo insicuro (per esempio incollata in chiaro in un form web prima della cifratura), e `0x02` significa che la chiave è stata generata e cifrata in un contesto sicuro e non e mai stata esposta. I client possono usare questo dato per mostrare warning quando importano chiavi con una storia nota come insicura.

NIP-49 protegge le chiavi meglio dell'export `nsec` in chiaro, ma la cifratura e forte solo quanto la password e il costo scrypt configurato. Valori `LOG_N` più alti rendono più difficile il guessing offline ma rallentano le operazioni legittime di decifratura. La spec mette in guardia dal pubblicare chiavi cifrate su relay pubblici, perché gli attaccanti traggono beneficio dal raccogliere ciphertext per cracking offline. Per confronto, la firma remota [NIP-46](/it/topics/nip-46/) evita di esporre del tutto le chiavi, e la firma Android [NIP-55](/it/topics/nip-55/) mantiene le chiavi dentro un'app signer dedicata. NIP-49 copre uno slot diverso: backup cifrato portabile per utenti che gestiscono da soli le proprie chiavi.

Le implementazioni includono [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) per il signup, [Amber](https://github.com/greenart7c3/Amber) per backup e restore ncryptsec, [diVine v1.0.6](#divine-distribuisce-v106-con-infrastruttura-di-test-e2e-e-import-nip-49) per l'import account, [Keep v0.6.0](#keep-v060) per l'export delle share FROST, e tool di gestione chiavi come [nsec.app](https://nsec.app) e [Alby](https://github.com/getAlby/hub).

## Approfondimento NIP: NIP-70 (Eventi protetti)

[NIP-70](/it/topics/nip-70/) definisce gli eventi protetti. Quando un evento porta il tag `["-"]`, un relay deve rifiutarlo a meno che il relay non richieda l'autenticazione [NIP-42](/it/topics/nip-42/) e la pubkey autenticata non corrisponda all'autore dell'evento.

Il flusso auth NIP-42 funziona così: il relay invia una challenge `AUTH` contenente una stringa casuale, e il client risponde con un evento firmato di kind `22242` i cui tag includono l'URL del relay e la challenge. Il relay verifica la firma e controlla che la pubkey nell'evento auth corrisponda alla pubkey nell'evento protetto in pubblicazione. Se le pubkey non corrispondono, il relay rifiuta l'evento con un prefisso di messaggio `restricted`.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

Anche se un relay blocca la pubblicazione dell'evento originale da parte di terzi, qualcuno può ripubblicarne il contenuto dentro un repost. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) affronta questo punto richiedendo ai relay di rifiutare anche i repost kind 6 e kind 16 di eventi protetti. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) aggiunge la gestione auth NIP-42 per gli eventi protetti, e [strfry PR #176](https://github.com/hoytech/strfry/pull/176) blocca i repost che incorporano contenuto protetto.

NIP-70 controlla il comportamento dei relay. Un destinatario può comunque copiare il contenuto altrove, e la spec lo dice esplicitamente. Il tag `-` offre ai relay un segnale machine-readable per rifiutare la ripubblicazione. Per confronto, [NIP-62](/it/topics/nip-62/) (Richieste di scomparsa) chiede ai relay di cancellare i dati a posteriori, mentre NIP-70 previene la pubblicazione non autorizzata in fase di ingestione. I due sono complementari: un autore può contrassegnare gli eventi come protetti per limitarne la diffusione, e poi richiederne la cancellazione se vuole che il contenuto venga rimosso dai relay che lo hanno accettato.

---

Questo è tutto per questa settimana. State costruendo qualcosa o avete notizie da condividere? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Scriveteci via DM [NIP-17](/it/topics/nip-17/)</a> oppure trovateci su Nostr.
