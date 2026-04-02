---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** [Amethyst](https://github.com/vitorpamplona/amethyst) implementa il supporto completo ai metodi [NIP-47](/it/topics/nip-47/) (Nostr Wallet Connect), [Alby Hub](https://github.com/getAlby/hub) aggiunge il supporto multi-relay nella [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6), [Amber](https://github.com/greenart7c3/Amber) distribuisce la [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3) con Tor integrato e permessi signer più granulari, e [Zeus](https://github.com/ZeusLN/zeus) rimuove un percorso keysend NWC rischioso nella [PR #3835](https://github.com/ZeusLN/zeus/pull/3835). [Notedeck](https://github.com/damus-io/notedeck) distribuisce un updater firmato nella [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) che scopre i rilasci attraverso event [NIP-94](/it/topics/nip-94/) (File Metadata), mentre [Damus](https://github.com/damus-io/damus) corregge lo stato [NIP-65](/it/topics/nip-65/) (Relay List Metadata) obsoleto, [Nostrability Outbox](https://github.com/nostrability/outbox) rivede i suoi risultati di benchmark con dati corretti, e [Primal iOS](https://github.com/PrimalHQ/primal-ios-app) testa sottoscrizioni relay dirette per i DM. [Primal Android](https://github.com/PrimalHQ/primal-android-app) distribuisce la [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7), [Route96](https://github.com/v0l/route96) distribuisce la [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0), [OpenChat](https://github.com/DavidGershony/openChat) continua a perfezionare l'interoperabilità Marmot nella [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11), [Pika](https://github.com/sledtools/pika) consolida il suo runtime nella [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1), e [Nostria](https://github.com/nostria-app/nostria) aggiunge il filtraggio Web of Trust tramite [NIP-85](/it/topics/nip-85/) (Trusted Assertions). Il repository NIPs unisce il markup Djot per [NIP-54](/it/topics/nip-54/) (Wiki) e un limite di input di 5000 caratteri per [NIP-19](/it/topics/nip-19/) (Bech32-Encoded Entities), mentre nuove proposte aprono discussioni su file `.nostrkey` per [NIP-49](/it/topics/nip-49/) (Private Key Encryption), consistenza dello stato di appartenenza per [NIP-43](/it/topics/nip-43/) (Relay Access Metadata and Requests), guida alla cancellazione per [NIP-17](/it/topics/nip-17/) (Private Direct Messages) e un URI share-intent per [NIP-222](/it/topics/nip-222/).

## Notizie

### Il supporto Wallet Connect si amplia, e i client wallet stringono i percorsi di errore

[Amethyst](https://github.com/vitorpamplona/amethyst), il client Android mantenuto da vitorpamplona, ha unito la [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828), che porta la sua implementazione [NIP-47](/it/topics/nip-47/) vicino alla copertura completa del protocollo. La patch aggiunge `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`, metodi per hold invoice, supporto keysend con record TLV, discovery delle capacità tramite kind `13194`, e event di notifica su kind `23197` con [NIP-44](/it/topics/nip-44/) (Encrypted Payloads). Questo dà al client una superficie NWC molto più ampia senza dipendere da estensioni specifiche dell'app.

Lo stack wallet circostante si è mosso nella stessa direzione. [Alby Hub](https://github.com/getAlby/hub), il nodo Lightning auto-custodiale e servizio wallet dietro molti deployment NWC, ha distribuito la [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) con supporto multi-relay e flussi di connessione e swap più semplici. [Zeus](https://github.com/ZeusLN/zeus), il wallet Lightning mobile, ha unito la [PR #3835](https://github.com/ZeusLN/zeus/pull/3835) rimuovendo il supporto keysend NWC dopo aver identificato un percorso silenzioso di drenaggio fondi in quel flusso, correggendo anche la gestione degli event in sospeso e l'attività Cashu. La connettività wallet su Nostr si sta ampliando, e gli implementatori stanno rimuovendo i flussi difficili da rendere sicuri.

### Notedeck sposta la scoperta dei rilasci su Nostr

[Come da copertura di Notedeck della settimana scorsa](/en/newsletters/2026-03-11-newsletter/), [Notedeck](https://github.com/damus-io/notedeck), il client desktop nativo del team Damus, ha distribuito la [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) dopo aver unito la [PR #1326](https://github.com/damus-io/notedeck/pull/1326). Il nuovo updater si sottoscrive a event di rilascio firmati di kind `1063`, abbina la piattaforma locale, scarica il binario referenziato e verifica il suo hash SHA256 prima dell'installazione. I metadati di rilascio non devono più provenire dall'API GitHub o dal sito web di un progetto. Una pubkey di rilascio fidata e una connessione relay sono sufficienti.

La stessa patch aggiunge una CLI `notedeck-release` che pubblica quegli event dagli artefatti di rilascio GitHub, il che significa che la pipeline di rilascio ora ha un percorso di pubblicazione nativo Nostr oltre a un percorso di scoperta nativo Nostr. Avvicina anche il modello di updater Damus e Notedeck al flusso di rilascio firmato pubblicato via relay di Zapstore: lo strumento `zsp` di Zapstore gestisce già gli asset software come event kind `1063` o `3063`, quindi questo percorso non è vincolato a un singolo client o un singolo publisher. Il resto della release candidate è lavoro desktop pratico: colonne di follow, profilo "View As User", supporto [NIP-59](/it/topics/nip-59/) (Gift Wrap), statistiche note in tempo reale e gestione delle limitazioni [NIP-11](/it/topics/nip-11/) (Relay Information Document), ma l'updater è la parte che probabilmente sopravviverà a questo singolo ciclo di rilascio.

### Lo stato dei relay si avvicina al comportamento runtime

[Damus](https://github.com/damus-io/damus) ha unito la [PR #3665](https://github.com/damus-io/damus/pull/3665), sostituendo un ID event di relay-list obsoleto memorizzato con una query diretta al database per l'event kind `10002` più recente. Quando il vecchio valore diventava obsoleto, le operazioni di aggiunta e rimozione relay potevano ricadere su bootstrap o liste vecchie di un anno, facendo apparire alcune modifiche ai relay come riuscite mentre lasciavano lo stato attivo invariato. La [PR #3690](https://github.com/damus-io/damus/pull/3690) corregge un secondo percorso di errore eliminando lo stato `lock.mdb` obsoleto durante la compattazione LMDB in modo che l'app non vada in crash con `SIGBUS` al prossimo avvio.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) ha aperto la [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194), che si sottoscrive direttamente ai relay di scrittura [NIP-04](/it/topics/nip-04/) (Encrypted Direct Messages) di un partner di chat mentre una conversazione è aperta, mantenendo il cache server come fallback. [Nostur](https://github.com/nostur-com/nostur-ios-public) ha aperto la [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53), che combina scoring randomizzato dei relay, filtraggio di liveness [NIP-66](/it/topics/nip-66/) da nostr.watch e Thompson sampling per trasformare la selezione dei relay da un'euristica fissa in una policy appresa. I client hanno a lungo trattato la scelta dei relay come dati di configurazione. Sempre più app ora la trattano come stato live che necessita di logica di misurazione e riparazione.

## Rilasci

### Primal Android 3.0.7

[Primal Android](https://github.com/PrimalHQ/primal-android-app), il client Android di Primal, ha distribuito la [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7) con un nuovo ciclo di sondaggi e wallet. La [PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945) aggiunge il voto nei sondaggi basato su zap, la [PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948) pagina il caricamento dei voti in modo che i sondaggi più grandi restino utilizzabili, e la [PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965) recupera le ricevute zap per tutte le transazioni. Lo stesso rilascio tagga anche gli event supportati con metadati client [NIP-89](/it/topics/nip-89/) (Recommended Application Handlers) nella [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968), che aiuta i client downstream ad attribuire le origini degli event in modo più pulito.

### Amber v4.1.3

[Come da copertura di Amber della settimana scorsa](/en/newsletters/2026-03-11-newsletter/), [Amber](https://github.com/greenart7c3/Amber), l'app signer Android per i flussi [NIP-55](/it/topics/nip-55/) (Android Signer Application), ha distribuito la [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3). Il rilascio si basa sul suo recente lavoro relay-auth [NIP-42](/it/topics/nip-42/) con più hardening operativo: la [PR #327](https://github.com/greenart7c3/Amber/pull/327) aggiunge Tor integrato insieme al supporto Orbot, la [PR #324](https://github.com/greenart7c3/Amber/pull/324) sostituisce i permessi di cifratura grossolani basati sui NIP con regole specifiche per tipo di contenuto, e la [PR #336](https://github.com/greenart7c3/Amber/pull/336) rimuove i permessi di rete dal flavor offline mentre la [PR #335](https://github.com/greenart7c3/Amber/pull/335) aggiunge controlli CI per mantenerli così. La [PR #322](https://github.com/greenart7c3/Amber/pull/322) sposta anche lo storage del PIN nel DataStore cifrato.

Questo rilascio stringe il confine del signer stesso. Questo è utile per qualsiasi flusso Android che affida chiavi reali o decisioni di relay-auth ad Amber, perché la parte difficile non è solo cosa il signer può fare. È anche quanto strettamente può essere limitato nel suo ambito.

### Route96 v0.6.0

[Come da copertura di Route96 della settimana scorsa](/en/newsletters/2026-03-11-newsletter/), [Route96](https://github.com/v0l/route96), il media server che supporta Blossom e [NIP-96](/it/topics/nip-96/) (HTTP File Storage), ha rilasciato la [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0). Il rilascio sposta la configurazione e lo stato della whitelist nel database con hot reload e aggiunge policy di conservazione per file freddi o invecchiati. Aggiunge anche un endpoint `GET /user/files` più ricco e il tracciamento delle statistiche dei file per download e egress, che dà agli operatori maggiore visibilità su come il loro storage server viene utilizzato.

### OpenChat v0.1.0-alpha.11

[Come da copertura di OpenChat della settimana scorsa](/en/newsletters/2026-03-11-newsletter/), [OpenChat](https://github.com/DavidGershony/openChat), il client chat basato su Avalonia costruito sullo stack Marmot, ha distribuito la [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11) dopo una settimana di lavoro rapido sul protocollo. Il [commit c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c) avvolge gli event Welcome in gift wrap [NIP-59](/it/topics/nip-59/) e rimuove i vecchi shim di normalizzazione tag MIP-00, il [commit 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1) completa l'audit di conformità MIP-02, e il [commit 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f) fa lo stesso per la cifratura dei messaggi di gruppo MIP-03. Il [commit 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547) consolida anche la gestione NIP-44 sull'implementazione marmot-cs condivisa, riducendo il rischio di deriva crittografica lato client.

### nak v0.19.0 e v0.19.1

[nak](https://github.com/fiatjaf/nak), il toolkit Nostr a riga di comando di fiatjaf, ha distribuito la [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0) e la [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1). La serie 0.19 aggiunge una UI group-forum nel [commit 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47), passa le modifiche dei metadati di gruppo a un flusso di sostituzione completa nel [commit da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3), e sostituisce la vecchia gestione `no-text` con `supported_kinds` nel [commit bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf). Per gli implementatori di gruppi, questo mantiene la CLI allineata con la direzione in cui si stanno muovendo le specifiche e i client dei gruppi.

## Aggiornamenti Progetti

### Amethyst

[Come da copertura di Amethyst della settimana scorsa](/en/newsletters/2026-03-11-newsletter/), [Amethyst](https://github.com/vitorpamplona/amethyst), il client Android con una delle superfici protocollari più ampie in Nostr, ha continuato a costruire sul suo lavoro wallet e relay dopo la patch NIP-47. La [PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853) aggiunge query COUNT [NIP-45](/it/topics/nip-45/) (Event Counting) nelle schermate di gestione relay, così gli utenti possono vedere quanti event ogni relay detiene effettivamente per home feed, notifiche, DM e dati indice. La [PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849) aggiunge caricamenti di file cifrati per le chat [NIP-17](/it/topics/nip-17/) (Private Direct Messages), con un percorso di retry per caricamenti non cifrati quando un host di storage rifiuta la versione cifrata.

La [PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791) porta anche il login bunker desktop completo [NIP-46](/it/topics/nip-46/) (Nostr Connect) con un indicatore heartbeat, che è importante perché i fallimenti di firma remota spesso appaiono come rotture casuali della UI dal lato dell'utente. Il client mostra se il signer è attivo e quanto recentemente ha risposto, rendendo anche ovvio quando la sessione corrente usa un bunker.

### Nostria

[Nostria](https://github.com/nostria-app/nostria), il client multi-piattaforma costruito attorno a uno stack local-first, ha unito la [PR #561](https://github.com/nostria-app/nostria/pull/561) aggiungendo il filtraggio Web of Trust per feed e risposte nei thread. La funzionalità usa i dati di ranking del trust-service esistente e li espone sia come filtro feed che come filtro risposte, nascondendo gli autori il cui rank non supera la soglia preservando la struttura del thread quando sono presenti discendenti fidati. Questo dà agli utenti un livello intermedio tra "mostra tutti" e la curazione basata su liste hardcoded.

La stessa settimana ha portato anche la [PR #563](https://github.com/nostria-app/nostria/pull/563), che aggiunge filtraggio dei contenuti e supporto repost alla pagina sommario. Fuori dalla lista PR tracciata, Nostria ha anche completato più della sua superficie per utenti avanzati. Ora supporta l'ultimo servizio Web of Trust di Brainstorm con registrazione in-app, insieme a flussi di invio e ricezione denaro nei DM usando NWC e fatture BOLT-11. Aggiunge anche la gestione GIF nativa Nostr tramite l'emoji NIP e un percorso di importazione RSS più robusto per i musicisti che può raccogliere gli split Lightning esistenti dai feed podcast. Nostria tratta ranking, media, pagamenti e pubblicazione come un'unica superficie app connessa.

### Nostur

[Nostur](https://github.com/nostur-com/nostur-ios-public), il client iOS mantenuto da nostur-com, ha aperto la [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53) per trasformare il routing outbox da un piano fisso in una policy con punteggio. La patch aggiunge scoring randomizzato dei relay, filtraggio di liveness [NIP-66](/it/topics/nip-66/) con un feed nostr.watch in cache, e Thompson sampling in modo che i dati di successo e fallimento dei relay cambino le selezioni future. Il design mantiene una valvola di sicurezza quando troppi relay verrebbero filtrati e preserva i relay `.onion`. Questo è uno degli esempi più chiari attualmente di un client che tratta la selezione dei relay come un sistema adattivo.

### Nostrability Outbox

[Come dal precedente report sui benchmark Outbox](/it/newsletters/2026-03-04-newsletter/#il-modello-outbox-sotto-la-lente), [Nostrability Outbox](https://github.com/nostrability/outbox), il progetto di benchmark e analisi focalizzato sul routing client [NIP-65](/it/topics/nip-65/) e [NIP-66](/it/topics/nip-66/), ha dedicato la settimana a stringere le proprie affermazioni. La [PR #35](https://github.com/nostrability/outbox/pull/35) sostituisce i risultati Thompson-sampling gonfiati con un re-benchmark completo su 1.511 esecuzioni e raccomanda la variante `CG3` per il routing in stile NDK. La [PR #43](https://github.com/nostrability/outbox/pull/43) aggiunge decadimento e confronti per caso d'uso, corregge un bug di cache-poisoning `0 follows`, poi riesegue il dataset Telluride dopo aver fissato i TTL della cache.

Questo non è lavoro di prodotto nel senso usuale, ma è importante per gli autori di client perché i numeri del progetto sono ora più precisi e meno lusinghieri nei punti in cui avevano precedentemente sovrastimato. Il risultato corretto è comunque utile. La selezione randomizzata continua a battere il routing puramente deterministico nei casi di cui Outbox si occupa, l'apprendimento in stile Thompson può migliorare materialmente la copertura quando i client persistono la cronologia utile dei relay, e il filtraggio di liveness [NIP-66](/it/topics/nip-66/) riduce il tempo sprecato su relay inattivi. Il lavoro si sta anche trasformando in proposte di implementazione concrete, incluse [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387), [Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53), [Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833), [rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282), [welshman #53](https://github.com/coracle-social/welshman/pull/53), e [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) più [applesauce #55](https://github.com/hzrd149/applesauce/pull/55).

### Backend White Noise

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), il backend Rust usato da White Noise e altri strumenti Marmot, ha unito due patch di hardening al confine della gestione media Blossom. La [PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637) impone HTTPS sugli URL Blossom e aggiunge un timeout di upload, mentre la [PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642) limita i download blob a `100 MiB` per impedire che pull di media sovradimensionati si trasformino in un percorso denial-of-service. Per il software di messaggistica privata, gli URL dei media sono una delle interfacce più critiche tra la logica applicativa cifrata e l'infrastruttura di rete non fidata. Questa settimana il team ha stretto quel confine.

### rust-nostr

[rust-nostr](https://github.com/rust-nostr/nostr), la libreria Rust per il protocollo, ha unito la [PR #1280](https://github.com/rust-nostr/nostr/pull/1280) aggiungendo costruttori di convenienza per `LocalRelayBuilderNip42`. I nuovi helper di lettura e scrittura danno ai setup di relay embedded e test un modo più chiaro per trasformare la policy auth [NIP-42](/it/topics/nip-42/) in codice. Questa è una piccola patch alla libreria, ma è importante per i team che costruiscono relay locali o integrati nelle app che necessitano di auth attivata senza ripetere boilerplate ogni volta.

### Pika

[Come dalla copertura precedente di Pika](/it/newsletters/2026-03-04-newsletter/), [Pika](https://github.com/sledtools/pika), l'app di messaggistica basata su Marmot, ha distribuito [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) e [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1) con un ciclo di rilascio focalizzato sulla convergenza del runtime. La [PR #542](https://github.com/sledtools/pika/pull/542) introduce una facade runtime Marmot condivisa per CLI e sidecar, con l'host dell'app che si sposta sulla stessa superficie. La [PR #556](https://github.com/sledtools/pika/pull/556) stringe il ciclo di vita degli agenti OpenClaw e lo stato di provisioning, mentre la [PR #600](https://github.com/sledtools/pika/pull/600) aggiunge il ripristino da backup e una sicurezza di recovery più rigorosa per gli ambienti gestiti.

La superficie utente diretta qui è più piccola rispetto all'ultimo writeup su Pika, ma il cambiamento architetturale è significativo. Riunire logica di gruppo, media, chiamate e sessioni dietro un unico runtime condiviso riduce la possibilità che app e daemon divergano man mano che lo stack Marmot cresce.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Uniti:**

- **[NIP-54](/it/topics/nip-54/) (Wiki): Passaggio da Asciidoc a Djot** ([PR #2242](https://github.com/nostr-protocol/nips/pull/2242)): I contenuti wiki su kind `30818` ora usano Djot come formato di markup canonico. Il testo unito aggiunge il comportamento esplicito dei wikilink, esempi di merge-request per kind `818`, esempi di redirect per kind `30819`, e esempi di normalizzazione per script non latini nei tag `d`. Questo dà agli implementatori un target di parsing più pulito rispetto ad Asciidoc e rimuove un altro percorso di specifica che dipendeva da un toolchain centrato su Ruby.

- **[NIP-19](/it/topics/nip-19/) (Bech32-Encoded Entities): Aggiunta limite di input** ([PR #2264](https://github.com/nostr-protocol/nips/pull/2264)): La specifica ora raccomanda di limitare le stringhe di entità codificate Bech32 a 5000 caratteri. Questa è una piccola modifica con valore reale per i parser, perché le stringhe NIP-19 ora appaiono nei flussi QR, deep link, fogli di condivisione e input incollato dagli utenti in molti client.

**PR Aperte e Discussioni:**

- **File Nostr Key per [NIP-49](/it/topics/nip-49/) (Private Key Encryption)** ([PR #2269](https://github.com/nostr-protocol/nips/pull/2269)): Propone un formato di file `.nostrkey` per l'esportazione e importazione di chiavi cifrate con password. Se unito, darebbe ai client un percorso di backup basato su file più normale rispetto alla copia di stringhe `ncryptsec` grezze.

- **Consistenza dello stato di appartenenza per [NIP-43](/it/topics/nip-43/) (Relay Access Metadata and Requests)** ([PR #2267](https://github.com/nostr-protocol/nips/pull/2267)): Aggiunge una sezione che chiarisce che i relay dovrebbero mantenere un unico stato di appartenenza autoritativo per pubkey. Questo semplificherebbe la logica dei client di gruppo attorno ai cambiamenti di appartenenza e alla cronologia riprodotta.

- **Guida alla cancellazione per [NIP-17](/it/topics/nip-17/) (Private Direct Messages)** ([PR #2260](https://github.com/nostr-protocol/nips/pull/2260)): Propone un percorso concreto per la modifica e cancellazione dei messaggi privati attraverso event di cancellazione avvolti in gift wrap. Il lavoro è ancora aperto, ma gli autori di client necessitano di una risposta qui se NIP-17 deve sostituire completamente i vecchi flussi DM.

- **URI Share-intent per [NIP-222](/it/topics/nip-222/)** ([PR #2266](https://github.com/nostr-protocol/nips/pull/2266)): La bozza standardizzerebbe come le app mobile e desktop passano contenuti condivisi in un client Nostr. Questo è uno dei confini di interoperabilità più ruvidi nei flussi app-to-app attuali.

## NIP Deep Dive: NIP-94 (File Metadata)

[NIP-94](/it/topics/nip-94/) definisce kind `1063` come un event di metadati di prima classe per un file. La [specifica](https://github.com/nostr-protocol/nips/blob/master/94.md) dà all'event il suo `content` leggibile più tag leggibili dalle macchine per URL di download, tipo MIME, hash, dimensioni, anteprime, fallback e hint sul servizio di storage. Questo è importante perché il file diventa interrogabile sui relay come oggetto a sé stante. Un client non deve estrarre i metadati dal contenuto circostante per capire cos'è il file.

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

I tag fanno più lavoro di quanto appaia a prima vista. `x` identifica il file servito, mentre `ox` identifica il file originale prima di qualsiasi trasformazione lato server. I tag di anteprima permettono ai client di costruire indici di file navigabili senza scaricare l'intero asset, e `summary` può portare un breve estratto accanto ad essi. `fallback` fornisce una seconda sorgente quando l'URL principale fallisce, e `service` indica il protocollo di storage dietro il file, come [NIP-96](/it/topics/nip-96/) o un altro host. NIP-94 si colloca quindi sotto il posting sociale e sopra lo storage grezzo. Descrive il file, non la conversazione attorno al file.

Ecco perché l'updater di Notedeck di questa settimana è interessante. La [PR #1326](https://github.com/damus-io/notedeck/pull/1326) usa event firmati di kind `1063` per la scoperta dei rilasci software, poi verifica il binario scaricato rispetto allo SHA256 pubblicato. La stessa forma di event può descrivere un artefatto software o un upload media. NIP-94 è abbastanza vecchio da essere stabile, ma ha ancora spazio per crescere perché sempre più progetti trattano gli event di metadati come un trasporto per le macchine, non solo come decorazione per le persone.

## NIP Deep Dive: NIP-54 (Wiki)

[NIP-54](/it/topics/nip-54/) definisce kind `30818` come un event articolo wiki. La [specifica](https://github.com/nostr-protocol/nips/blob/master/54.md) tratta il tag `d` come l'argomento normalizzato dell'articolo e permette a molti autori di pubblicare voci per lo stesso soggetto. Il corpo dell'articolo vive in `content`, mentre i tag gestiscono identità normalizzata, titolo di visualizzazione, sommari e riferimenti a versioni precedenti. Questo significa che NIP-54 non è solo un formato di contenuto. È anche un problema di recupero e ranking, perché ogni client deve ancora decidere quale versione dell'articolo mostrare.

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

Il merge di questa settimana cambia il markup canonico da Asciidoc a Djot nella [PR #2242](https://github.com/nostr-protocol/nips/pull/2242). Questo è importante per gli implementatori perché Djot ha una specifica standalone più stretta e una storia di parser più semplice attraverso i linguaggi. Il testo unito chiarisce anche come i wikilink in stile reference si risolvono, come le merge request usano kind `818`, come i redirect usano kind `30819`, e come la normalizzazione del tag `d` dovrebbe comportarsi per gli script non latini. Queste sono le parti che fanno sì che due client indipendenti concordino su quale articolo un link punta.

NIP-54 occupa anche un posto insolito nel protocollo. Un client wiki necessita di rendering del contenuto, ma necessita anche di una policy di ranking. Reazioni, liste relay, liste contatti e segnali di deferenza espliciti alimentano tutti quale articolo vince per un dato argomento. Il passaggio a Djot non risolve quel problema di ranking, ma rimuove una delle ambiguità del parser che stava sotto di esso. Ecco perché il merge è importante ora: la modifica riguarda meno la formattazione della prosa più bella e più il rendere il comportamento wiki multi-client più facile da implementare in modo consistente.

Stai costruendo qualcosa, o vuoi che lo copriamo? Contattaci tramite DM [NIP-17](/it/topics/nip-17/) su Nostr a `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`.
