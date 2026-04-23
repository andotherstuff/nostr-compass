---
title: 'Nostr Compass #3'
date: 2025-12-31
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale all'ecosistema del protocollo Nostr.

**Questa settimana:** mentre il 2025 si chiude, ripercorriamo cinque anni di traguardi di dicembre nell'evoluzione di Nostr. Dal primo rilascio client di fiatjaf nel dicembre 2020, passando per la decisiva donazione di 14 BTC di Jack Dorsey nel dicembre 2022, fino alla proliferazione dei signer [NIP-55](/it/topics/nip-55/) di questo mese e all'accelerazione di 162x della cache di NDK, dicembre ha segnato con costanza momenti di svolta per il protocollo. Questo numero speciale segue la storia tecnica attraverso ogni dicembre, documentando la crescita del protocollo da due relay sperimentali a oltre 2.500 nodi in 50 paesi. In più: il modulo desktop di Amethyst prende forma tramite Quartz, Notedeck guadagna la messaggistica, Citrine ospita web app, e [NIP-54](/it/topics/nip-54/) corregge l'internazionalizzazione per gli script non latini.

## Retrospettiva di Dicembre: Cinque Dicembre di Nostr

Quest'anno Nostr compie cinque anni. fiatjaf ha avviato il protocollo il 7 novembre 2020, e ogni dicembre da allora ha segnato una fase distinta della sua evoluzione: da proof of concept a movimento globale fino a ecosistema di produzione. Questa è una retrospettiva tecnica da dicembre 2020 a dicembre 2025, gli anni formativi che hanno stabilito le fondamenta di Nostr e ne hanno catalizzato il momento di svolta.

### Dicembre 2020: Genesi

Il primo mese completo di esistenza di Nostr ha visto fiatjaf pubblicare [Branle](https://github.com/fiatjaf/branle), il primo client del protocollo, costruito con Quasar (Vue.js) e absurd-sql per lo storage locale. fiatjaf aveva già definito l'architettura di base: utenti identificati da chiavi pubbliche secp256k1, tutti i post firmati crittograficamente, relay che fungono da storage stupido senza comunicare tra loro. Uno o due relay sperimentali servivano un piccolo gruppo di primi adottanti che si coordinavano nel gruppo Telegram [@nostr_protocol](https://t.me/nostr_protocol), lanciato il 16 novembre. La [documentazione originale](https://fiatjaf.com/nostr.html) descriveva "il più semplice protocollo aperto capace di creare un social network globale resistente alla censura", una premessa che avrebbe richiesto altri due anni per dimostrarsi.

### Dicembre 2021: Sviluppo Iniziale

Il 31 dicembre 2021, Nostr è arrivato sulla [front page di Hacker News](https://news.ycombinator.com/item?id=29749061) con 110 punti e 138 commenti, grazie a una submission di Cameri. Questo ha segnato la prima esposizione significativa del protocollo alla più ampia comunità di sviluppatori. La rete funzionava su circa sette relay con meno di 1.000 utenti. Branle ha ricevuto aggiornamenti inclusa l'importazione di chiavi private il 31 dicembre e il supporto multi-relay. Un client da riga di comando, noscl, forniva interazione da terminale. Le specifiche del protocollo esistevano nella documentazione di fiatjaf, anche se il repository formale dei [NIPs](https://github.com/nostr-protocol/nips) non sarebbe stato creato fino a maggio 2022. Il protocollo era, come lo descriveva fiatjaf, "un work in progress".

### Dicembre 2022: Il Punto di Svolta

Dicembre 2022 ha trasformato Nostr da esperimento di nicchia a movimento mainstream. Il catalizzatore è arrivato il 15 dicembre, quando Jack Dorsey ha donato [14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding) (~$245.000-$250.000) a fiatjaf dopo aver scoperto il protocollo e aver dichiarato che era "al 100 percento ciò che volevamo da Bluesky, ma non era sviluppato da un'azienda". Il 16 dicembre fiatjaf ha annunciato la divisione dei fondi con William Casarin (jb55), sviluppatore di Damus, e Dorsey ha verificato il suo account Nostr (npub: `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`). Il finanziamento ha legittimato il progetto dall'oggi al domani.

Nella stessa settimana, il caos di Twitter ha accelerato l'adozione. Il 14-15 dicembre sono arrivate le sospensioni di giornalisti di primo piano del New York Times, CNN e Washington Post. Il 18 dicembre Twitter ha [annunciato il divieto](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) per gli account che promuovevano Nostr, Mastodon e altre piattaforme. La policy è stata revocata il giorno successivo dopo il contraccolpo pubblico. L'esodo ha spinto gli utenti a esplorare alternative.

Lo sviluppo del protocollo ha subito un'impennata. Il 16 dicembre è stato unito [NIP-19](/it/topics/nip-19/) ([#57](https://github.com/nostr-protocol/nips/pull/57)), introducendo identificatori codificati in bech32 (npub, nsec, note, nprofile, nevent) che rendevano le chiavi leggibili dagli umani e distinguibili. Il repository NIPs ha registrato oltre 36 commit quel mese, inclusi aggiornamenti a NIP-40 e NIP-07. I client si sono moltiplicati: Damus ha riempito la beta TestFlight in poche ore, Astral ha forkato Branle per la creazione dei profili, Snort è stato lanciato come client web "veloce e resistente alla censura", e Vitor Pamplona ha iniziato lo sviluppo di Amethyst. Alby v1.22.1 "Kemble's Cascade of Stars" è uscita il 22 dicembre con supporto NIP-19. Al 7 dicembre, Nostr aveva circa 800 utenti con profili; quando Damus è arrivato sull'App Store il 31 gennaio 2023, i cancelli si sono spalancati, spingendo la crescita oltre 315.000 utenti entro giugno 2023.

### Dicembre 2023: Maturazione dell'Ecosistema

Dicembre 2023 ha segnato un punto di inflessione critico per la sicurezza del protocollo Nostr. Il 20 dicembre, [NIP-44 revisione 3 è stato unito](https://github.com/nostr-protocol/nips/pull/746) dopo un audit di sicurezza indipendente di Cure53 (NOS-01) che ha identificato 10 problemi nelle implementazioni TypeScript, Go e Rust, inclusi timing attack e problemi di forward secrecy. La specifica aggiornata ha sostituito la cifratura difettosa di [NIP-04](/it/topics/nip-04/) con ChaCha20 e HMAC-SHA256, stabilendo la base crittografica che oggi sostiene i DM privati di [NIP-17](/it/topics/nip-17/) e il gift wrapping di [NIP-59](/it/topics/nip-59/). Nella stessa settimana, [OpenSats ha annunciato la quarta ondata di grant](https://opensats.org/blog/nostr-grants-december-2023) il 21 dicembre, finanziando sette progetti tra cui Lume, noStrudel, ZapThreads e un audit indipendente di NIP-44. Questo seguiva la [prima ondata di luglio 2023](https://opensats.org/blog/nostr-grants-july-2023), che aveva finanziato Damus, Coracle, Iris e altri, portando l'allocazione totale del Nostr Fund a circa 3,4 milioni di dollari distribuiti su 39 grant.

Il mese ha anche messo in luce tensioni di sostenibilità nell'ecosistema. Il 28 dicembre, William Casarin (jb55) [ha scritto su Stacker News](https://stacker.news/items/368863) che il 2024 sarebbe stato "probabilmente l'ultimo anno di Damus", citando il fatto che "i client nostr non fanno soldi" dopo che le restrizioni di Apple sugli zaps in-app avevano limitato pesantemente il potenziale di ricavo. Il team Damus aveva già rifiutato finanziamenti VC. Nel frattempo, [Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1) è uscita il 26 dicembre, estendendo [NIP-47](/it/topics/nip-47/) con i metodi `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` e `get_info`, gettando le basi per le integrazioni wallet che sarebbero poi diventate standard nei client.

### Dicembre 2024: Avanzamento del Protocollo

Dicembre 2024 si è aperto con il [lancio alpha di Notedeck](https://damus.io/notedeck/) il 30 novembre, il client desktop Rust-based del team Damus con interfaccia multi-colonna e supporto per più account. Costruito per Linux, macOS e Windows, con Android pianificato per il 2025, Notedeck è stato inizialmente distribuito agli abbonati Damus Purple e ha rappresentato un'espansione strategica oltre iOS. Due settimane dopo, [OpenSats ha annunciato la nona ondata di grant](https://opensats.org/blog/9th-wave-of-nostr-grants) il 16 dicembre, finanziando AlgoRelay, il primo relay algoritmico per feed personalizzati, Pokey, app Android con Bluetooth mesh per internet limitato, Nostr Safebox ([NIP-60](/it/topics/nip-60/) con storage di token [Cashu](/it/topics/cashu/)) e LumiLumi, client web leggero e accessibile, spingendo l'allocazione totale del Nostr Fund a circa 9 milioni di dollari, un aumento del 67% su base annua.

Il mese ha visto una significativa maturazione dei client in tutto l'ecosistema. [Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0) è arrivato il 23 dicembre con supporto File Metadata ([NIP-92](/it/topics/nip-92/)/[NIP-94](/it/topics/nip-94/)), integrazione Blossom e ricerca relay di [NIP-50](/it/topics/nip-50/). [Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0) è uscita il 12 dicembre con onboarding rielaborato e integrazione nostr-editor. Lo sviluppo del protocollo è rimasto attivo con 30 pull request inviate tra il 9 e il 22 dicembre, di cui 10 unite, inclusi riscritture di [NIP-46](/it/topics/nip-46/) per usare solo la cifratura NIP-44 e il lavoro continuo su [NIP-104](/it/topics/nip-104/) per la cifratura double ratchet a livello Signal. Le statistiche di rete hanno mostrato oltre 224.000 trusted pubkey event giornalieri, una crescita di 4x anno su anno nei nuovi profili con contact list e un aumento del 50% negli event di scrittura pubblica.

### Dicembre 2025: Espansione dell'Ecosistema

Dicembre 2025 ha portato la prosecuzione della maturazione del protocollo e dell'espansione dell'ecosistema. Il 21 dicembre, [OpenSats ha annunciato la quattordicesima ondata di grant Nostr](https://opensats.org/blog/fourteenth-wave-of-nostr-grants), finanziando tre progetti: YakiHonne, un client multi-piattaforma con creator portal per contenuti long-form e integrazione pagamenti [Cashu](/it/topics/cashu/)/Nutzaps, Quartz, la libreria Kotlin Multiplatform di Vitor Pamplona che alimenta Amethyst e permetterà una versione iOS, e Nostr Feedz, l'integrazione bidirezionale RSS-to-Nostr di PlebOne. I rinnovi dei grant sono andati a Dart NDK e al nostr-relay di Mattn.

L'evoluzione del protocollo è continuata con [NIP-BE](/it/topics/nip-be/) (messaggistica Bluetooth Low Energy, [#1979](https://github.com/nostr-protocol/nips/pull/1979)) unito a novembre, permettendo la sincronizzazione offline tra dispositivi. [NIP-A4](/it/topics/nip-a4/) (Public Messages, kind 24, [#1988](https://github.com/nostr-protocol/nips/pull/1988)) è arrivato più tardi nel mese, definendo messaggi per la schermata notifiche che usano tag `q` per evitare complicazioni di threading. [NIP-29](/it/topics/nip-29/) ha ricevuto un importante chiarimento ([#2106](https://github.com/nostr-protocol/nips/pull/2106)), introducendo il tag `hidden` per gruppi veramente privati e non individuabili. Anche la specifica di [NIP-55](/it/topics/nip-55/) ha visto affinamenti ([#2166](https://github.com/nostr-protocol/nips/pull/2166)), affrontando un errore di implementazione comune in cui gli sviluppatori chiamavano `get_public_key` da processi in background.

Sul lato client, [Primal Android è diventato un signer NIP-55 completo](/en/newsletters/2025-12-24-newsletter/#news) attraverso otto PR unite che implementano `LocalSignerContentProvider`, unendosi ad Amber e Aegis come opzioni di firma Android. La [libreria NDK ha raggiunto query cache 162x più veloci](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes), passando da ~3.690ms a ~22ms, eliminando scritture duplicate e lookup non necessari nella cache LRU ([PR #371](https://github.com/nostr-dev-kit/ndk/pull/371), [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)). Shopstr ha introdotto [Zapsnags](/en/newsletters/2025-12-24-newsletter/#news) per flash sale via zaps. White Noise ha distribuito [MIP-05](/it/topics/mip-05/) per notifiche push che preservano la privacy. Per una copertura completa, consultate [Newsletter #1](/en/newsletters/2025-12-17-newsletter/) e [Newsletter #2](/en/newsletters/2025-12-24-newsletter/).

---

Cinque anni fa, fiatjaf pubblicò Branle per una manciata di utenti distribuiti su due relay sperimentali. Oggi il protocollo supporta oltre 140 client, più di 2.500 relay in 50 paesi e una crescente web of trust che collega centinaia di migliaia di coppie di chiavi. Il modello di dicembre fatto di grandi rilasci è continuato anche questo mese, con messaggistica Bluetooth, proliferazione di signer Android e grant infrastrutturali che segnalano investimenti continui negli strumenti cross-platform.

## Notizie

**Amethyst Desktop prende forma** - Il grant Quartz della quattordicesima ondata di OpenSats sta già producendo risultati. [PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625) crea un modulo `:desktopApp` completo per Amethyst usando Compose Multiplatform, con schermate di login e global feed già funzionanti su Desktop JVM. L'architettura converte il modulo `:commons` in Kotlin Multiplatform con una struttura pulita dei source set (`commonMain`, `jvmAndroid`, `androidMain`, `jvmMain`), permettendo componenti UI condivisi tra Android e desktop e lasciando le decisioni specifiche della piattaforma a ciascun target. Questo getta le basi per la futura versione iOS tramite lo stesso approccio Kotlin Multiplatform.

**Risposte vocali in Amethyst** - Un regalo di Natale da davotoula: [PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622) aggiunge schermate dedicate alle risposte vocali con visualizzazione della waveform, supporto alla ri-registrazione, selezione del media server e indicatori di avanzamento upload. Gli utenti possono ora rispondere con audio sia ai messaggi vocali root sia alle risposte vocali.

**Notedeck aggiunge la messaggistica** - Notedeck, il client desktop di Damus, ha guadagnato una funzione messaggi in [PR #1223](https://github.com/damus-io/notedeck/pull/1223), espandendosi oltre la navigazione della timeline verso la comunicazione diretta.

**Citrine ospita web app** - Citrine ora può [ospitare applicazioni web](https://github.com/greenart7c3/Citrine/pull/81), trasformando il telefono in un server web Nostr local-first. Una seconda [PR #85](https://github.com/greenart7c3/Citrine/pull/85) aggiunge la riconnessione automatica e il broadcasting degli event quando la connettività di rete ritorna, con copertura di test completa su diversi livelli API Android.

**Registro Nostrability per developer toolkit** - Il tracker [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264) mantiene un registro curato di SDK, librerie e strumenti per sviluppatori in diversi linguaggi, tra cui TypeScript, Rust, Python, Go, Dart e Swift. Se siete nuovi allo sviluppo su Nostr, questo è un buon punto di partenza per trovare il toolkit adatto al vostro stack.

## Aggiornamenti NIP

Cambiamenti recenti nel [repository NIPs](https://github.com/nostr-protocol/nips):

- **[NIP-54](/it/topics/nip-54/)** - Correzione critica di internazionalizzazione per la normalizzazione dei d-tag wiki ([#2177](https://github.com/nostr-protocol/nips/pull/2177)). Le regole precedenti convertivano tutti i caratteri non ASCII in `-`, rompendo il supporto a giapponese, cinese, arabo, cirillico e altri script. La specifica aggiornata preserva le lettere UTF-8, applica il lowercase solo ai caratteri che hanno varianti maiuscole/minuscole e include esempi completi: `"ウィキペディア"` resta `"ウィキペディア"`, `"Москва"` diventa `"москва"`, e script misti come `"日本語 Article"` si normalizzano in `"日本語-article"`.

## Rilasci

**Zapstore 1.0-rc1** - Il permissionless app store basato su Nostr distribuisce il [primo release candidate](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1) della sua nuova architettura, con un completo refresh della UI, package manager riscritto con migliore gestione degli errori, App Stacks per la scoperta curata, schermate profilo riprogettate, controllo degli aggiornamenti in background e infinite scrolling nelle liste delle release.

**KeyChat v1.38.1** - L'app di messaggistica cifrata basata su MLS [aggiunge il supporto a UnifiedPush](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489) per le notifiche push su Android e Linux, oltre all'autenticazione biometrica per le operazioni che incidono sulla privacy. Disponibile per Android, Windows, macOS e Linux.

**Alby Go v2.0.0** - Il companion mobile wallet Lightning [distribuisce un redesign visivo](https://github.com/getAlby/go/releases/tag/v2.0.0) con nuovo logo, palette colori aggiornata, rubrica riprogettata e tastiera migliorata per l'inserimento degli importi. BTC Map è ora accessibile dalla schermata principale e le descrizioni delle transazioni compaiono nelle notifiche.

**nak v0.17.4** - Lo strumento Nostr da riga di comando di fiatjaf è stato [rilasciato](https://github.com/fiatjaf/nak/releases/tag/v0.17.4), dopo la correzione della settimana scorsa in v0.17.3 alla restrizione Linux di LMDB.

## Cambiamenti notevoli nel codice e nella documentazione

*Pull request aperte e lavori nelle prime fasi che vale la pena osservare.*

### Damus (iOS)

[Relay hint NIP-19](https://github.com/damus-io/damus/pull/3477) implementa il consumo dei relay hint nel recupero degli event. Quando gli utenti aprono link nevent, nprofile o naddr, Damus ora estrae i relay hint dai dati bech32 TLV e si connette a relay effimeri per recuperare contenuti che non si trovano nel relay pool dell'utente. L'implementazione include cleanup ref-counted per prevenire race condition durante lookup concorrenti. [Image URL detection](https://github.com/damus-io/damus/pull/3474) converte automaticamente gli URL immagine incollati in anteprime thumbnail nel composer, con un badge di posizione nel carosello per immagini multiple. [npub paste conversion](https://github.com/damus-io/damus/pull/3473) trasforma stringhe npub/nprofile incollate in link mention con risoluzione asincrona del profilo.

### Amethyst (Android)

[Payment targets](https://github.com/vitorpamplona/amethyst/pull/1627) aggiunge un'interfaccia event per gli zap split [NIP-57](/it/topics/nip-57/), permettendo ai post di specificare più destinatari che condividono gli zaps in arrivo, utile per collaborazioni, revenue sharing o mance sia ai creatori di contenuti sia agli strumenti che usano. [Quartz feature parity documentation](https://github.com/vitorpamplona/amethyst/pull/1624) aggiunge una tabella dettagliata che traccia quali funzionalità sono implementate tra target Android, Desktop JVM e iOS, evidenziando che a iOS mancano la crittografia core (`Secp256k1Instance`), la serializzazione JSON e le strutture dati.

### Notedeck (Desktop)

[Timeline filter rebuild](https://github.com/damus-io/notedeck/pull/1226) corregge un bug per cui gli account non più seguiti continuavano a comparire nei feed. I filtri della timeline venivano costruiti una sola volta a partire dalla contact list e non venivano mai aggiornati; la correzione aggiunge il tracciamento di `contact_list_timestamp` e un metodo `invalidate()` per innescare la ricostruzione quando cambia lo stato dei follow.

### Citrine (Relay Android)

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86) espone il database event del relay locale alle altre app Android tramite `ContentResolver`. A differenza dell'interfaccia WebSocket, che richiede alle app di mantenere una connessione persistente e parlare il protocollo relay Nostr, ContentProvider offre accesso diretto sincrono al database tramite il meccanismo IPC nativo di Android. Le app esterne possono interrogare gli event per ID, pubkey, kind o intervallo di date, inserire nuovi event con validazione e cancellarli senza dover gestire connessioni socket.

### rust-nostr (Libreria)

[Supporto NIP-40 a livello relay](https://github.com/rust-nostr/nostr/pull/1183) aggiunge la gestione della scadenza al livello del relay builder. Gli event scaduti vengono ora rifiutati prima dello storage e filtrati prima dell'invio ai client, eliminando la necessità che ogni implementazione del database gestisca i controlli di scadenza in modo indipendente.

### nak (CLI)

[Blossom mirror](https://github.com/fiatjaf/nak/pull/91) implementa la funzionalità di mirroring blob per lo strumento da riga di comando.

### Mostro (Trading P2P)

[Dev fee audit events](https://github.com/MostroP2P/mostro/pull/559) aggiunge audit trail trasparenti per i pagamenti del fondo sviluppo tramite event Nostr di kind 8383. L'implementazione pubblica event di audit non bloccanti dopo i pagamenti fee riusciti, includendo dettagli dell'ordine e hash dei pagamenti ed escludendo le pubkey di buyer e seller per motivi di privacy.

### MDK (Marmot Development Kit)

Sono arrivate tre correzioni da security audit: [Author verification](https://github.com/marmot-protocol/mdk/pull/40) impone che le rumor pubkey corrispondano alle credenziali MLS del mittente, impedendo attacchi di impersonation. [KeyPackage identity binding](https://github.com/marmot-protocol/mdk/pull/41) verifica che l'identità della credential corrisponda ai signer degli event. [Admin update validation](https://github.com/marmot-protocol/mdk/pull/42) impedisce set admin vuoti e assegnazioni admin a non membri.

### Shopstr (Marketplace)

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217) implementa un sistema di pagamento trust-minimized per beni fisici. L'architettura usa `makeHoldInvoice` di Alby per bloccare i fondi del buyer nel suo wallet, con settlement attivato solo dopo la verifica dell'inventario da parte del merchant. Il protocollo di handshake scorre attraverso DM cifrati di [NIP-17](/it/topics/nip-17/): il buyer invia la richiesta ordine, il merchant risponde con la HODL invoice, il buyer paga con fondi bloccati, il merchant conferma stock e spedizione, poi il settlement rilascia i fondi. Il supporto cart multi-merchant divide i pagamenti tra i vendor.

### Jumble (Client Web)

[Per-relay discovery mode](https://github.com/CodyTseng/jumble/pull/713) aggiunge un toggle per nascondere i post degli utenti seguiti su relay specifici, permettendo feed di scoperta basati sulla lingua, per esempio nostr.band/lang/*. La funzionalità filtra i post in cui la pubkey dell'autore compare nella follow list dell'utente, persistendo lo stato del toggle per URL relay in localStorage.

### White Noise (Messaggistica Cifrata)

[Media upload retry](https://github.com/marmot-protocol/whitenoise/pull/937) aggiunge opzioni di retry per gli upload falliti. [Profile edit warnings](https://github.com/marmot-protocol/whitenoise/pull/927) avvisano gli utenti sulle modifiche al profilo. Sul backend, [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422) corregge una race condition nella creazione di AccountGroup.

### npub.cash (Servizio Lightning Address)

[v3 rewrite](https://github.com/cashubtc/npubcash-server/pull/40) migra il monorepo e il server a Bun, aggiunge il supporto SQLite, rimuove la compatibilità v1, implementa LUD-21 e aggiunge aggiornamenti realtime per le mint quote.

### nostr-java (Libreria)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1) distribuisce refactor della gestione WebSocket e una migliore robustezza dei test attraverso [due PR](https://github.com/tcheeric/nostr-java/pull/499).

### Repository NIPs

[Migrazione Djot di NIP-54](https://github.com/nostr-protocol/nips/pull/2180) propone una modifica separata alla specifica wiki: passare il formato dei contenuti da Asciidoc a Djot, un linguaggio di markup leggero con sintassi più pulita. La PR introduce link in stile reference per i wikilink, rendendo i riferimenti incrociati tra articoli wiki più leggibili nel sorgente. [NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179) introduce la governance threshold multi-signature per i gruppi Nostr usando FROST. Un Quorum è un nsec condiviso tra i membri attraverso uno schema T-of-N in cui i membri possono rappresentare sé stessi o delegare a un consiglio di rappresentanti. Quando il consiglio cambia, il vecchio nsec diventa obsoleto e uno nuovo viene distribuito; l'atto finale di ogni consiglio è firmare l'event di transizione della governance. La specifica definisce membership pubblica o privata, elezioni e poll, eventuali "leggi" in linguaggio naturale e, soprattutto, ontologie di quorum in cui i quorum possono essere membri di altri quorum, permettendo strutture gerarchiche come località che aderiscono a organismi regionali. I casi d'uso vanno dallo sviluppo di codice sorgente ai consigli di amministrazione, dalle HOA alle comunità moderate.

---

Per questa settimana e per quest'anno è tutto. State costruendo qualcosa? Avete novità da condividere? Volete che parliamo del vostro progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattateci via DM NIP-17</a> o cercateci su Nostr.
