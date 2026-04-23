---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [Shopstr](https://github.com/shopstr-eng/shopstr) e [Milk Market](https://github.com/shopstr-eng/milk-market) aggiungono superfici MCP per il commercio guidato da agenti, mentre [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) e [strfry](https://github.com/hoytech/strfry) aggiungono relay-auth e supporto agli event protetti di [NIP-42](/it/topics/nip-42/) in software per app, signer e relay. [Route96](https://github.com/v0l/route96) distribuisce due release incentrate su etichettatura AI, code di moderazione, perceptual hashing e documentazione server machine-readable. [Samizdat](https://github.com/satsdisco/samizdat), già live sul web, ha rilasciato la sua prima alpha Android e in seguito ha aggiunto il supporto signer di [NIP-55](/it/topics/nip-55/). [Formstr](https://github.com/formstr-hq/nostr-forms) aggiunge la registrazione tramite [NIP-49](/it/topics/nip-49/), [Amethyst](https://github.com/vitorpamplona/amethyst) distribuisce il lavoro di risoluzione [NIP-05](/it/topics/nip-05/) basato su Namecoin, [Mostro](https://github.com/MostroP2P/mostro) rilascia la [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), e il repository NIPs unisce [NIP-91](/it/topics/nip-91/) e le linee guida difensive per [NIP-66](/it/topics/nip-66/).

## Notizie

### Shopstr e Milk Market aprono superfici MCP per il commercio

[Shopstr](https://github.com/shopstr-eng/shopstr), il marketplace peer-to-peer con pagamenti Lightning e Cashu, ha unito [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), aggiungendo un server MCP con autenticazione API key per la gestione degli account degli agenti. La modifica aggiunge `.well-known/agent.json` per la discovery degli agenti, endpoint MCP per onboarding e stato, route per la creazione degli ordini e la verifica dei pagamenti, strumenti dedicati per acquisto e lettura, e una schermata impostazioni per le API key. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) estende il tutto con azioni lato venditore per messaggi, indirizzi, aggiornamenti degli ordini e selezione delle specifiche di prodotto. Una correzione di sicurezza in [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) sostituisce l'hashing delle API key con SHA-256 a singola iterazione con PBKDF2 salato a 100.000 iterazioni.

Gli agenti possono leggere gli annunci di [NIP-99](/it/topics/nip-99/) e procedere al checkout usando i flussi di pagamento esistenti di [NIP-47](/it/topics/nip-47/) e [NIP-60](/it/topics/nip-60/) senza dover fare scraping delle pagine o reverse-engineering del comportamento del client.

[Milk Market](https://github.com/shopstr-eng/milk-market), marketplace alimentare su Nostr attivo su [milk.market](https://milk.market), ha introdotto la stessa base MCP e API key nel [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) aggiunge ordini in abbonamento, modifica dell'indirizzo di spedizione dopo l'acquisto, e gestione del checkout multi-merchant e multi-valuta per Stripe e altri percorsi di pagamento fiat. Una successiva [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) corregge un bug di inizializzazione del database all'avvio in cui la tabella delle pubblicazioni relay fallite non veniva creata nelle installazioni nuove, causando errori 500 al primo caricamento. L'interfaccia rivolta agli agenti funziona con checkout Bitcoin-native su Shopstr o con checkout misto fiat e Bitcoin su Milk Market.

### NIP-42 relay auth tra bunker, signer e relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), un bunker [NIP-46](/it/topics/nip-46/) che collega provider OAuth alla firma Nostr, ha aggiunto il login [NIP-07](/it/topics/nip-07/), la selezione automatica della singola identità e la pulizia delle identità eliminate ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Quando esiste una sola identità, il bunker ora la seleziona automaticamente invece di chiedere all'utente. L'eliminazione di un'identità rimuove anche assegnazioni e connessioni rimaste orfane. Il [commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) aggiunge un percorso di configurazione `ALWAYS_ALLOWED_KINDS` per gli utenti assegnati, con kind `30078` come valore predefinito per i dati specifici dell'app, così le identità delegate possono scrivere nello storage dell'app senza approvazione per ogni event.

[Amber](https://github.com/greenart7c3/Amber), il signer [NIP-55](/it/topics/nip-55/) principale su Android, ha distribuito la [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) insieme a quattro pre-release nel corso della settimana. [PR #317](https://github.com/greenart7c3/Amber/pull/317) aggiunge la gestione dell'autenticazione relay [NIP-42](/it/topics/nip-42/) per richieste di kind `22242`. L'implementazione aggiunge una nuova colonna nel database che traccia i permessi specifici per relay con un indice univoco su `(pkKey, type, kind, relay)`. Gli utenti vedono una schermata auth dedicata dove possono concedere o negare il permesso per relay singolo o per tutti i relay con wildcard `*`, e salvare quella scelta. I permessi wildcard cancellano tutte le voci specifiche per relay di quel kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) segue con un refactor delle schermate per richieste multi-event, che ora mostrano i dettagli inline tramite composable card invece di navigare verso una schermata separata. La release aggiorna anche i relay profilo predefiniti, aggiunge la visualizzazione delle richieste in bottom sheet e corregge un crash sui dispositivi MediaTek disabilitando il keystore StrongBox.

Sul lato relay, [strfry PR #156](https://github.com/hoytech/strfry/pull/156) implementa la gestione auth NIP-42 per gli event protetti di [NIP-70](/it/topics/nip-70/), e [PR #176](https://github.com/hoytech/strfry/pull/176) rifiuta i repost che incorporano event protetti.

### Notedeck aggiunge i limiti relay di NIP-11 e funzionalità Agentium

[Notedeck](https://github.com/damus-io/notedeck), il client desktop nativo del team Damus, ha unito 14 PR questa settimana. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) aggiunge il recupero dei limiti relay di [NIP-11](/it/topics/nip-11/), così tutti i relay outbox ora rispettano `max_message_length` e `max_subscriptions` dal relay information document. L'implementazione include elaborazione in background, exponential backoff con jitter per i retry di connessione e header HTTP Accept personalizzati. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) corregge un bug per cui i DM talvolta non si caricavano dopo il cambio account, e [PR #1333](https://github.com/damus-io/notedeck/pull/1333) aggiunge un meccanismo di backoff alla comunicazione relay multicast per evitare broadcast spam in caso di errore.

Il sottosistema Agentium, l'interfaccia integrata per agenti di coding di Notedeck chiamata internamente "Dave", ha ricevuto il supporto all'incolla di immagini dalla clipboard, configurazioni di esecuzione nominate che si sincronizzano tra dispositivi tramite event kind `31991` di [NIP-33](/it/topics/nip-33/), un creatore di git worktree e un model picker per selezionare backend diversi per sessione ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integra `egui_kittest` per test UI headless, e [PR #1339](https://github.com/damus-io/notedeck/pull/1339) aggiunge una dashboard card che traccia la creazione di nuove contact list da parte dei client. Una [PR #1314](https://github.com/damus-io/notedeck/pull/1314) ancora aperta porta in Notedeck la risoluzione NIP-05 basata su Namecoin di Amethyst con lookup ElectrumX, routing SOCKS5 via Tor e integrazione nella barra di ricerca.

### diVine distribuisce la v1.0.6 con infrastruttura di test E2E e import NIP-49

[diVine](https://github.com/divinevideo/divine-mobile), il client video short-form in loop che ripristina gli archivi Vine su [divine.video](https://divine.video), ha distribuito la [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) con 127 PR unite. La release aggiunge l'import account [NIP-49](/it/topics/nip-49/), supporto [NIP-05](/it/topics/nip-05/) esterno, gestione multi-account, build macOS e Linux sperimentale, e una libreria ridisegnata per draft e clip basata su storage locale.

Sul lato engineering, [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) aggiunge un'infrastruttura completa di test di integrazione E2E usando Patrol per l'automazione UI nativa contro uno stack backend Docker composto da relay, API, Blossom, Postgres, Redis e ClickHouse. Cinque test del percorso auth coprono registrazione, verifica, reset password, scadenza sessione e refresh del token. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) cambia il caricamento video da HLS-first a MP4 diretto con fallback automatico a HLS, riducendo i tempi di caricamento da 30-60 secondi a quasi istantanei. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) mette in cache la risposta API del feed home in SharedPreferences per la visualizzazione immediata a cold start. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) impone che le etichette di contenuto `ai-generated` siano nascoste nei feed, e [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) aggiunge un'impostazione di sicurezza per mostrare solo video ospitati da diVine. La migrazione della cache profili da Hive a Drift prosegue nelle [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) e [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), sostituendo circa 1.074 linee di codice Hive con DAO Drift.

### Vector v0.3.2 distribuisce la sincronizzazione negentropy di NIP-77 e miglioramenti MLS

[Vector](https://github.com/VectorPrivacy/Vector), messenger desktop orientato alla privacy che usa la cifratura di gruppo MLS con [NIP-17](/it/topics/nip-17/) e [NIP-44](/it/topics/nip-44/), ha distribuito la [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). La novità principale è la negentropy NIP-77 per la sincronizzazione dei gruppi MLS ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), che recupera i messaggi persi molto più rapidamente tramite parallel boot. La release aggiunge anche un motore audio ricostruito con pieno supporto Linux, spoiler immagine con anteprime sfocate, hyperlink cliccabili con anteprime ricche, ping `@mention` con `@everyone` per gli admin dei gruppi, autocomplete per shortcode emoji, silenziamento dei gruppi, tap-to-react sulle reazioni esistenti e upload file annullabili. Vector filtra esplicitamente gli event di chat di gruppo NIP-17 ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), usando MLS in modo esclusivo per la cifratura di gruppo.

## Rilasci

### Route96 v0.5.0 e v0.5.1

[Route96](https://github.com/v0l/route96), media server che supporta Blossom e [NIP-96](/it/topics/nip-96/), ha distribuito [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) e [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). La v0.5.0 aggiunge etichettatura AI automatizzata, backfill retroattivo per upload non etichettati, code di moderazione per file segnalati, rifiuto basato su EXIF per la privacy e gestione degli hash vietati.

La v0.5.1 aggiunge hash percettivi per immagini, locality-sensitive hashing per la ricerca di immagini simili, endpoint admin batch e un [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) pubblicato che descrive la superficie API Blossom e NIP-96 del server per gli strumenti agentici. [PR #58](https://github.com/v0l/route96/pull/58) sposta i background worker su task Tokio completamente asincroni, e il [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) aggiunge il backoff per evitare hot loop.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), lettore e publisher long-form disponibile su [samizdat.press](https://samizdat.press), ha distribuito la sua prima build Android nella [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). L'app si apre con una pagina Press curata di articoli long-form Nostr e navigazione bottom tab tra le viste Press, Feed, Saved e Write. La build Android aggiunge storage nativo delle chiavi tramite cifratura Android Keystore con sblocco biometrico, gestisce URI `nostr:` e deep link `samizdat.press`, e supporta il passaggio della firma tramite chooser delle app Android, Amber, Primal e altre, invece di richiedere l'import diretto delle chiavi. Pull-to-refresh, gestione delle safe area su schermi di dimensioni diverse, e integrazioni native per condivisione, clipboard, feedback aptico e splash screen fanno ora parte della shell Android invece del wrapper web.

Il [commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) aggiunge la firma intent-based [NIP-55](/it/topics/nip-55/) per i flussi Amber e Primal, e il [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) sostituisce un workaround JavaScript bridge con un plugin Capacitor nativo che usa `startActivityForResult`. L'app richiede Android 7.0+ (API 24), viene distribuita come APK debug in questa alpha e ancora non include notifiche push. La pubblicazione dipende al momento da un'app signer, mentre il login con `nsec` copre la lettura locale e l'accesso all'account.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), calendario decentralizzato con condivisione di eventi privati tramite [NIP-59](/it/topics/nip-59/), disponibile su [calendar.formstr.app](https://calendar.formstr.app), ha distribuito la [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) con [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). La release estende la gestione degli eventi ricorrenti di [NIP-52](/it/topics/nip-52/), andando oltre la base a evento singolo della v0.1.0. Le modifiche sottostanti toccano anche storage locale degli eventi, gestione del signer e plumbing delle notifiche Android. Questa è la seconda applicazione attiva dell'organizzazione Formstr dopo la migrazione del repository dello scorso mese.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), exchange Bitcoin peer-to-peer costruito su Nostr, ha rilasciato la [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). Le correzioni per il ripristino delle sessioni di disputa ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) e la chiusura automatica ([PR #606](https://github.com/MostroP2P/mostro/pull/606)), [coperte la settimana scorsa](/en/newsletters/2026-03-04-newsletter/), sono incluse. Nuove in questa release: [PR #625](https://github.com/MostroP2P/mostro/pull/625) aggiunge un campo `days` agli event di rating utente di kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) aggiunge la scadenza a quegli event di rating, e [PR #614](https://github.com/MostroP2P/mostro/pull/614) sposta gli event ordine verso le impostazioni di scadenza configurate invece di una finestra hardcoded di 24 ore. [PR #622](https://github.com/MostroP2P/mostro/pull/622) aggiunge un controllo di idempotenza per evitare pagamenti duplicati delle dev fee.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), client Flutter per l'exchange P2P Mostro, ha distribuito la [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) con 11 nuove funzionalità e 11 bug fix. La release aggiunge il rendering di contenuti multimediali cifrati nella chat di disputa ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), la chiusura automatica della UI delle dispute quando gli ordini raggiungono uno stato terminale ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), la scansione QR per importare wallet NWC ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), traduzioni francesi e gestione delle notifiche push FCM. [PR #496](https://github.com/MostroP2P/mobile/pull/496) corregge un bug di padding delle firme Schnorr bloccando la dipendenza bip340 alla v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), client di messaggistica in stile Telegram con supporto Cashu, ha distribuito la [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) focalizzata sulle correzioni per Linux desktop: icone AppImage nel dock, rendering delle emoji, freeze nei menu contestuali e blocchi della UI per reply/copy. La release corregge anche i problemi di upload delle immagini e l'integrazione npub.cash. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) elimina rebuild UI non necessari rimuovendo un timer di polling da 3 secondi che forzava repaint glassmorphic senza fare nulla, e sblocca l'inizializzazione del login eseguendo il caricamento della cache event in parallelo invece di bloccare l'avvio di relay, contatti e canali.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), signer threshold FROST per Android con supporto [NIP-55](/it/topics/nip-55/) e [NIP-46](/it/topics/nip-46/), ha distribuito [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) e [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). La v0.6.0 aggiunge coordinamento dei wallet descriptor e relativa UI di gestione, un flusso backup/restore con autenticazione biometrica ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), recupero `nsec` da threshold share ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), generazione cross-platform di frame QR animati tramite Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)) e un audit trail della firma con verifica della chain ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). La v0.6.1 cambia la licenza da AGPL-3.0 a MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), gateway statico per visualizzare contenuti Nostr su [njump.me](https://njump.me), ha distribuito la [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) con una modifica incompatibile nel parsing dei codici `note1` e un aggiornamento della libreria nostr sottostante.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), applicazione decentralizzata per segnalare eventi stradali usando Nostr, ha distribuito la sua prima demo [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). L'app mostra gli eventi stradali su una mappa usando vector tile da openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), applicazione di e-bill con transport layer Nostr e relay dedicato su [bit.cr](https://www.bit.cr/), ha distribuito la [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) aggiunge i campi `payment_actions` e `bill_state` all'API per stato dei pagamenti e dell'accettazione, e [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) corregge la gestione dell'indirizzo di firma per signer anonimi.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), applicazione chat costruita sulle librerie .NET MLS e C# del protocollo Marmot, ha distribuito la [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). La release aggiunge supporto a signer esterni per Amber e flussi [NIP-46](/it/topics/nip-46/) ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), sposta la persistenza dello stato MLS dentro il servizio MLS per eliminare la perdita di dati nella finestra di crash ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), e pubblica build Windows, Linux e Android attraverso una nuova pipeline CI.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), trading copilot Kotlin Multiplatform per Nostr, ha distribuito la [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). La release include moduli KMP condivisi per logica di dominio, rendering dei grafici, autenticazione e pubblicazione Nostr, supporto upload Blossom [NIP-96](/it/topics/nip-96/) e hook di inferenza AI basati su ONNX su shell Desktop e Android. L'architettura pubblicata include anche un servizio AI FastAPI per l'analisi di screenshot dei grafici, pipeline di training dei modelli e un motore di rischio che produce piani di trading strutturati con sizing e warning. Il login supporta chiavi `nsec` grezze oppure signer esterni, e il flusso di output termina con la pubblicazione di event Nostr invece che con un'analisi solo locale.

## Aggiornamenti Progetto

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), l'alternativa a Google Forms su Nostr, ha unito [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), aggiungendo un flusso di registrazione che usa chiavi private cifrate [NIP-49](/it/topics/nip-49/). Prima di questa modifica, gli utenti avevano bisogno di un'estensione browser [NIP-07](/it/topics/nip-07/) oppure di incollare una `nsec` grezza per usare Formstr. Il nuovo flusso genera una coppia di chiavi lato client, cifra la chiave privata con una password scelta dall'utente tramite lo schema scrypt + XChaCha20-Poly1305 di NIP-49, e memorizza la stringa `ncryptsec` risultante. Gli utenti possono quindi accedere di nuovo con la propria password senza installare un'estensione signer. La gestione delle chiavi resta interamente lato client.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android ricco di funzionalità, ha unito quattro PR che distribuiscono il lavoro di risoluzione [NIP-05](/it/topics/nip-05/) supportato da Namecoin che era [aperto la settimana scorsa](/en/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) aggiunge una verifica NIP-05 resistente alla censura via ElectrumX per identificatori `.bit`, `d/` e `id/`. Quando Amethyst rileva uno di questi suffissi in un campo NIP-05, interroga un server ElectrumX-NMC per la cronologia delle transazioni del nome, analizza lo script `NAME_UPDATE` dall'ultimo output per estrarre la pubkey Nostr e rifiuta i nomi più vecchi di 36.000 blocchi, la finestra di scadenza di Namecoin. Le connessioni ElectrumX passano attraverso SOCKS5 quando Tor è attivo, con selezione dinamica del server tra endpoint clearnet e `.onion`. Una cache LRU con TTL di un'ora evita interrogazioni ripetute della blockchain.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) corregge race condition e accuratezza del resolver in quel flusso. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) permette ai nuovi utenti di importare una follow list durante la registrazione sia da normali identificatori NIP-05 sia da quelli supportati da Namecoin. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) aggiunge impostazioni personalizzate per il server ElectrumX così gli utenti possono scegliere quale server gestirà i loro lookup.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), libreria che fornisce metodi helper per memorizzare event Nostr in IndexedDB, ha unito [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) aggiungendo il supporto ai filtri tag AND di [NIP-91](/it/topics/nip-91/). La modifica aggiunge semantica di intersezione al matching lato client dei filtri, così le query IndexedDB possono richiedere tutti i valori tag elencati invece di uno qualsiasi. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) aggiorna la libreria all'ultima interfaccia NIP-DB, e un successivo [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) corregge un deadlock di subscribe e rimuove nostr-tools come dipendenza di produzione.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), indicizzatore Nostr archive-first con analytics ClickHouse, ha unito [PR #8](https://github.com/andotherstuff/pensieve/pull/8) aggiungendo enforcement del TTL della cache per entry e coalescing dei miss per chiave, così da ridurre i picchi di CPU API. Gli endpoint time-series più costosi, statistiche di engagement, attività oraria e attività per kind, usano ora TTL server-side di 10 minuti invece di innescare tempeste di ricalcolo sincronizzate.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), protocollo e stack server per l'hosting media decentralizzato, ha unito due aggiornamenti di autorizzazione BUD-11. [PR #91](https://github.com/hzrd149/blossom/pull/91) sposta l'autorizzazione opzionale in un BUD dedicato e chiarisce il ruolo dei tag `x` e `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) ripulisce il comportamento auth specifico per endpoint e formalizza l'header `X-SHA-256` per la verifica degli upload. Le due PR consolidano la logica auth in BUD-11 e rimuovono ambiguità sull'hashing delle richieste nei flussi di upload, delete e media management.

## Aggiornamenti NIP

Cambiamenti recenti nel [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti:**

- **[NIP-91](/it/topics/nip-91/) (AND Operator for Filters)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): aggiunge semantica di intersezione per i filtri tag, permettendo ai relay di rispondere a query che richiedono tutti i valori tag elencati invece di uno qualsiasi. Riduce il post-filtering lato client e la larghezza di banda nelle query ricche di tag.

- **[NIP-66](/it/topics/nip-66/) (Relay Discovery and Liveness Monitoring): misure difensive** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): dopo il [lavoro di benchmark outbox coperto la settimana scorsa](/en/newsletters/2026-03-04-newsletter/), la specifica aggiunge ora avvertimenti sui percorsi sfavorevoli dei dati di monitoraggio relay. I client non devono richiedere event di monitoraggio kind `30166` per funzionare. Un monitor può essere errato, obsoleto o malevolo. Ci si aspetta che i client incrocino le fonti ed evitino di tagliare ampie parti del grafo relay di un utente basandosi su un singolo feed.

- **[NIP-39](/it/topics/nip-39/) (External Identities in Profiles): pulizia del registry kind 10011** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): aggiunge il riferimento al kind `10011` direttamente nella specifica, allineandosi con l'implementazione di Amethyst [coperta la settimana scorsa](/en/newsletters/2026-03-04-newsletter/).

**PR aperte e discussioni:**

- **[NIP-70](/it/topics/nip-70/) (Protected Events): rifiutare i repost che incorporano event protetti** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): se un relay applica NIP-70 all'event originale ma accetta repost che trasportano lo stesso contenuto, il tag `-` non ha effetto pratico. Questa PR aggiunge la regola per cui i relay devono rifiutare anche i repost di kind 6 e kind 16 degli event protetti. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) lo implementa già.

- **[NIP-71](/it/topics/nip-71/) (Video Events): tracce audio multiple** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): aggiunge tag audio `imeta` per tracce alternative, varianti linguistiche e stream solo audio. Un client potrebbe mantenere stabile il file video cambiando lingua audio, oppure servire l'audio come traccia separata per contenuti tipo podcast.

- **[NIP-11](/it/topics/nip-11/) (Relay Information Document) e attributi relay di [NIP-66](/it/topics/nip-66/)** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): aggiunge un campo `attributes` strutturato ai relay information document, fornendo a client e strumenti di discovery metadati machine-readable oltre l'attuale descrizione a testo libero.

## NIP Deep Dive: NIP-49 (Cifratura della chiave privata)

[NIP-49](/it/topics/nip-49/) definisce come un client cifra una chiave privata con una password e codifica il risultato come stringa bech32 `ncryptsec`. [Formstr](#formstr) usa NIP-49 nel suo nuovo flusso di registrazione.

Il formato non è legato a un kind di event dedicato. Un client parte dalla chiave privata secp256k1 grezza a 32 byte, deriva una chiave simmetrica dalla password dell'utente con scrypt, cifra la chiave usando XChaCha20-Poly1305, poi incapsula il risultato in una stringa bech32 `ncryptsec`. Un flag di un byte registra se la chiave è mai stata gestita in modo insicuro prima della cifratura.

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

L'event JSON sopra è un esempio a livello applicativo, non un requisito NIP-49. Il NIP standardizza il formato della chiave cifrata. Un client può memorizzare `ncryptsec` localmente, sincronizzarlo tramite storage specifico dell'app o esportarlo come stringa di backup. Le password sono normalizzate in Unicode NFKC prima della derivazione della chiave, così la stessa password può decifrare in modo coerente tra client e piattaforme.

Il flag di sicurezza della chiave a un byte ha tre valori definiti: `0x00` significa che la cronologia di gestione della chiave è sconosciuta, `0x01` significa che la chiave è nota per essere stata gestita in modo insicuro, per esempio incollata in chiaro in un form web prima della cifratura, e `0x02` significa che la chiave è stata generata e cifrata in un contesto sicuro e non è mai stata esposta. I client possono usare questa informazione per mostrare avvisi quando importano chiavi con una storia nota di gestione insicura.

NIP-49 protegge le chiavi meglio dell'esportazione semplice `nsec`, ma la cifratura è forte solo quanto la password e il costo scrypt configurato. Valori `LOG_N` più alti rendono l'attacco offline più difficile ma rallentano anche la decifratura legittima. La specifica sconsiglia di pubblicare chiavi cifrate su relay pubblici, perché gli attaccanti traggono vantaggio dal raccogliere ciphertext da sottoporre a cracking offline. Per confronto, la firma remota di [NIP-46](/it/topics/nip-46/) evita di esporre del tutto le chiavi, e la firma Android di [NIP-55](/it/topics/nip-55/) le mantiene all'interno di un'app signer dedicata. NIP-49 occupa uno spazio diverso: backup cifrato portabile per utenti che gestiscono le proprie chiavi.

Le implementazioni includono [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) per la registrazione, [Amber](https://github.com/greenart7c3/Amber) per backup e restore ncryptsec, [diVine v1.0.6](#divine-distribuisce-la-v106-con-infrastruttura-di-test-e2e-e-import-nip-49) per l'import account, [Keep v0.6.0](#keep-v060) per l'esportazione di share FROST, e strumenti di gestione delle chiavi come [nsec.app](https://nsec.app) e [Alby](https://github.com/getAlby/hub).

## NIP Deep Dive: NIP-70 (Event protetti)

[NIP-70](/it/topics/nip-70/) definisce gli event protetti. Quando un event porta il tag `["-"]`, un relay deve rifiutarlo a meno che il relay richieda l'autenticazione [NIP-42](/it/topics/nip-42/) e la pubkey autenticata corrisponda all'autore dell'event.

Il flusso auth di NIP-42 funziona così: il relay invia una challenge `AUTH` contenente una stringa casuale, e il client risponde con un event signed di kind `22242` i cui tag includono l'URL del relay e la challenge. Il relay verifica la firma e controlla che la pubkey nell'event auth coincida con la pubkey dell'event protetto in pubblicazione. Se le pubkey non coincidono, il relay rifiuta l'event con il prefisso di messaggio `restricted`.

Il contenuto dell'event può comunque essere pubblico. Il tag `-` controlla solo chi può pubblicare l'event su un relay che onora il tag. Questo copre feed semi-chiusi di [NIP-29](/it/topics/nip-29/), spazi relay riservati ai membri e altri contesti in cui l'autore vuole limitare la ridistribuzione attraverso il grafo relay. NIP-70 è una convenzione a tag singolo, non un nuovo kind di event, quindi qualunque kind esistente può portare il tag `-`.

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

Anche se un relay blocca la pubblicazione di terzi dell'event originale, qualcuno può ripubblicarne il contenuto dentro un repost. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) affronta il problema richiedendo ai relay di rifiutare anche i repost di kind 6 e kind 16 degli event protetti. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) aggiunge la gestione auth NIP-42 per gli event protetti, e [strfry PR #176](https://github.com/hoytech/strfry/pull/176) blocca i repost che incorporano contenuto protetto.

NIP-70 controlla il comportamento del relay. Un destinatario può comunque copiare altrove il contenuto, e la specifica lo dice esplicitamente. Il tag `-` fornisce ai relay un segnale machine-readable per rifiutare la ripubblicazione. Per confronto, [NIP-62](/it/topics/nip-62/) chiede ai relay di cancellare i dati dopo il fatto, mentre NIP-70 impedisce la pubblicazione non autorizzata al momento dell'ingest. I due approcci sono complementari: un autore può contrassegnare gli event come protetti per limitarne la diffusione, e in seguito chiedere la cancellazione se desidera che il contenuto venga rimosso dai relay che lo avevano accettato.

---

Per questa settimana è tutto. State costruendo qualcosa o avete novità da condividere? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattateci via DM [NIP-17](/it/topics/nip-17/)</a> o cercateci su Nostr.
