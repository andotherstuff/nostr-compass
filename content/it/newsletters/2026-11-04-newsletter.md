---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

Questa settimana [Amethyst](/it/newsletters/2026-11-04-newsletter/#amethyst) ha rilasciato i napplet inline con le correzioni emerse da una [revisione di sicurezza degli embed](https://github.com/vitorpamplona/amethyst/pull/4710). [Napplets](/it/newsletters/2026-11-04-newsletter/#napplets---web-packages) ha legato l'identità degli applet a porte assegnate a ogni singolo documento, mentre le nightly di [mdk di Marmot](/it/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk) hanno reso più rigorosa la messaggistica di gruppo. Altrove sono cambiati relay, wallet, librerie di firma e nuove app, in gran parte in codice sorgente già integrato ma non ancora rilasciato.

## Notizie principali {#top-stories}

### Amethyst {#amethyst}

Amethyst, il client Android, ha rilasciato la [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0), che esegue i napplet inline nelle note su Android 11+ e su desktop. Le correzioni derivanti da una [revisione di sicurezza degli embed](https://github.com/vitorpamplona/amethyst/pull/4710) chiudono una via attraverso cui qualsiasi napplet con accesso ai relay poteva leggere i DM decifrati. Ora la decifratura richiede un'autorizzazione separata da parte dell'utente e `nostr.signEvent` richiede il permesso del signer, mentre il renderer Chromium su desktop resta privo di sandbox. Una [modifica alla cifratura degli allegati per singolo file](https://github.com/vitorpamplona/amethyst/pull/4701) assegna a ogni allegato dei messaggi diretti privati [NIP-17](/it/topics/nip-17/) una chiave e un nonce AES-GCM nuovi, mentre in precedenza i batch con più file riutilizzavano entrambi. La descrizione del rischio fornita dall'upstream deriva da un'analisi del codice, senza un exploit riprodotto, e i file già inviati non vengono corretti.

### Marmot Protocol (mdk) {#marmot-protocol-mdk}

mdk, il kit di Marmot per la messaggistica cifrata su Nostr basato su MLS, ha pubblicato prerelease nightly destinate solo ai test, senza alcuna release stabile in quella linea. Nella nightly del 2 novembre, all'interno di un gruppo [i nuovi invii attendono che quelli più vecchi in coda siano partiti](https://github.com/marmot-protocol/mdk/pull/2849). In questo modo le generazioni di cifratura restano in ordine per i membri che stanno recuperando la cronologia, anche se ciò non mette al riparo dalla perdita di messaggi. Una [riparazione dei Welcome persi](https://github.com/marmot-protocol/mdk/pull/2936), già integrata e disattivata per impostazione predefinita, segue la [regola dell'heartbeat di Marmot](https://github.com/marmot-protocol/marmot/pull/497). Reinvia esattamente il Welcome conservato non appena l'heartbeat del destinatario mostra attività ad almeno dieci minuti dall'ultima pubblicazione del carrier. La cadenza dell'heartbeat o lo sfasamento dell'orologio possono ritardare la riparazione di un'ora o più, e il completamento non ha un limite massimo. I [comandi per il collegamento dei dispositivi](https://github.com/marmot-protocol/mdk/pull/2922) restano dietro la feature dev-device-groups, disattivata per impostazione predefinita, e sono disattivati in produzione.

### Napplets - Pacchetti web {#napplets---web-packages}

Napplets, i pacchetti web per applet Nostr in sandbox, ha rilasciato [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0), [nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0) e [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0), che [vincolano l'identità dell'applet a una MessagePort specifica per ogni documento](https://github.com/napplet/web/pull/302). L'identità verificata (dTag, artifactHash) è legata alla porta passata nel messaggio hello dall'iframe creato, e tutto il traffico NAP passa per quella porta. Un documento caricato tramite navigazione non riceve alcuna autorizzazione. Le shell che usano ancora la messaggistica Window devono aggiornarsi, perché non esiste un percorso di compatibilità. Codice sorgente successivo [blocca il frame di anteprima sul relativo documento verificato](https://github.com/napplet/web/pull/305) con frame-src 'none'.

## Release con tag {#tagged-releases}

### Marble {#marble}

Marble, un client in beta basato sulla firma a soglia di Cosign, con la [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23) può leggere i relay come feed. Un relay aperto tramite il suo indirizzo mostra prima la propria descrizione e poi i suoi post, dal più recente. I relay preferiti sono conservati in una lista kind 10012 e i gruppi di relay in set kind 30002, le stesse liste usate da Jumble. La release rinnova anche le reazioni, con un pannello delle reazioni recenti e le emoji personalizzate dell'utente.

### Sidecar {#sidecar}

Sidecar, un'estensione per browser con cui pubblicare note ed evidenziazioni dal web, con la [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6) può eliminare dai relay il backup del proprio wallet. Dopo una conferma, sostituisce la copia cifrata con una vuota e chiede ai relay di dimenticarla, lasciando al suo posto il wallet collegato. Non è garantito che i relay cancellino il backup. Dalla [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5), Sidecar rimuove i metadati EXIF, XMP e IPTC dai JPEG prima del caricamento, e la sua [modifica alla preparazione dei caricamenti](https://github.com/dmnyc/sidecar/pull/572) blocca qualsiasi JPEG che non sia possibile ripulire.

### Haps {#haps}

Haps pubblica e installa pacchetti nativi associati a chiavi Nostr. [Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25) distribuisce bundle per macOS, Linux e Windows con helper htree vincolati tramite checksum e un file SHA256SUMS che copre tutti gli archivi. Il codice sorgente della 0.1.24 [scrive riferimenti Hashtree con versione](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8) secondo la bozza della specifica Hashtree. Haps 0.1.23 e le versioni precedenti non sono in grado di leggere i nuovi cataloghi senza un catalogo di transizione legacy oppure un installer o una build Cargo aggiornati.

### Cosign {#cosign}

Cosign, la libreria di firma a soglia alla base della beta di Marble, introduce nella [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9) una correzione parziale per l'ingresso nel gruppo. Un ingresso tramite un invitante scansionato ora richiede il contributo di quell'invitante e frammenti provenienti da almeno due mittenti distinti. Gli ingressi da telefono a telefono restano non vincolati, quindi a un attaccante bastano ancora due chiavi, e le parti di decifratura vuote continuano a saltare la verifica della prova. Nella [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8), un server che scrive l'elenco dei membri può ancora scegliere punti di share con segreti noti. I telefoni ricevono le correzioni solo tramite una release di Marble.

### nostream {#nostream}

nostream, un relay in TypeScript basato su PostgreSQL, aggiunge nella [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0) la [sincronizzazione in uscita verso i peer](https://github.com/cameri/nostream/pull/1043). Il worker legge gli ambiti presenti nelle informazioni del relay [NIP-11](/it/topics/nip-11/) di ciascun peer, si autentica con l'autenticazione client [NIP-42](/it/topics/nip-42/) e riconcilia tramite la sincronizzazione negentropy [NIP-77](/it/topics/nip-77/), verificando ID, firma e ambito degli eventi recuperati. I [limiti specifici per peer](https://github.com/cameri/nostream/pull/1034) si applicano solo dopo che un peer configurato ha completato l'AUTH. Una release del codice sorgente non dimostra che un qualsiasi relay l'abbia messa in produzione.

### diVine {#divine}

diVine, un client per brevi video in loop, ha pubblicato la [versione stabile 1.0.27 per Android](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27) con sticker video pubblici interattivi; la disponibilità su iOS e macOS non è confermata. Una [nuova interrogazione al di sotto della finestra](https://github.com/divinevideo/divine-mobile/pull/10711), già integrata, viene eseguita solo una volta terminato il ripristino iniziale della cronologia. Legge i gift wrap, i DM cifrati deprecati [NIP-04](/it/topics/nip-04/) e le cancellazioni in pagine da 100 messaggi per relay. Scorre ogni relay in modo indipendente, mentre l'attuale recupero della cronologia usa un unico cursore condiviso e può saltare la cronologia più vecchia di un relay soggetto a un limite. La copertura è limitata e non recupera la cronologia completa.

### Whistle {#whistle}

Whistle, un'app mobile per la chat e la condivisione della posizione in gruppo, ha rilasciato la [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1), la sua prima release pubblica sul protocollo Marmot v2. I gruppi esistenti non possono essere trasferiti, quindi vanno ricreati e ogni membro deve aggiornare l'app; le identità npub vengono invece mantenute. L'ingresso tramite scansione sostituisce i codici e i link di invito. Tra i problemi noti, i messaggi di chat inviati offline possono arrivare in ritardo o non arrivare affatto, cosa che la release attribuisce a MarmotKit; la condivisione della posizione non è interessata.

## In sviluppo {#in-development}

### Quartz {#quartz}

Quartz, una libreria Nostr per Kotlin Multiplatform, ha introdotto nella release 2.14.0 la [ripresa delle sottoscrizioni live dopo la riconnessione](https://github.com/vitorpamplona/quartz/pull/82). Ogni relay riprende dal created_at più recente già consegnato, limitato all'orologio del dispositivo, e i filtri per i gift wrap risalgono di due giorni in più per coprire le retrodatazioni. Gli eventi con timestamp più vecchi che un relay ha memorizzato durante un'interruzione possono comunque andare persi. Le [finestre negentropy basate sul conteggio](https://github.com/vitorpamplona/quartz/pull/85), già unite ma non ancora rilasciate, confrontano un conteggio opzionale di eventi [NIP-45](/it/topics/nip-45/) con il conteggio locale e considerano non attendibili i conteggi forniti dai relay.

### Buzz {#buzz}

Buzz ha unito una modifica che [esegue il commit delle cancellazioni di kind 5 e 9005 nella stessa transazione della soft delete del target](https://github.com/block/buzz/pull/8944), così un errore non può più accettare una cancellazione lasciando attivo il target. Le righe rimaste incoerenti in passato non vengono riparate. Il profilo mobile di [NIP-RS](/it/topics/nip-rs/), una bozza di Buzz per lo stato di lettura tra dispositivi, è stato unito e [sincronizza le frontiere di lettura tra dispositivi](https://github.com/block/buzz/pull/8998). Sui relay più vecchi privi di read_state_snapshot, le letture locali continuano a funzionare, mentre la sincronizzazione tra dispositivi si interrompe senza alcun fallback.

### Alby Hub {#alby-hub}

Alby Hub, un nodo Lightning in autocustodia che serve le app Nostr Wallet Connect [NIP-47](/it/topics/nip-47/), ha unito una [correzione della migrazione del database](https://github.com/getAlby/hub/pull/2657) che preserva il contatore degli ID di ogni tabella durante db_migrate o una migrazione Postgres. In precedenza, una nuova app poteva riutilizzare l'ID di un'app eliminata ed ereditarne le transazioni e il saldo isolato. Non è stata individuata alcuna release taggata o distribuzione che contenga la correzione. Una [modifica separata alle notifiche](https://github.com/getAlby/hub/pull/2677) isola i fallimenti delle singole app, anche se le notifiche non riuscite vengono ancora scartate senza nuovi tentativi.

### swift-nostr-client {#swift-nostr-client}

swift-nostr-client, una libreria Nostr per Swift 6, ha unito una modifica incompatibile che fa sì che [RemoteSigner esegua l'handshake di connessione prima del primo comando](https://github.com/yysskk/swift-nostr/pull/287). La nuova impostazione connectsAutomatically vale true per impostazione predefinita, e se l'handshake fallisce il comando non viene inviato. Poiché i segreti di firma remota [NIP-46](/it/topics/nip-46/) sono monouso, le app che riprendono una sessione bunker con una coppia di chiavi client salvata devono impostarla su false, altrimenti il primo comando presenta il segreto già usato. Non è stata ancora taggata alcuna release.

## Nuovi progetti {#new-projects}

### Trikey {#trikey}

Trikey, un wallet pre-alpha e non sottoposto ad audit, la cui app per telefono e il guardian comunicano tramite messaggi cifrati attraverso relay Nostr, risolve nella [release 0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf) il blocco dell'app all'apertura. Entrambe le parti ora mantengono un registro, persistente tra i riavvii, degli ID dei wrap già letti e li saltano prima di qualsiasi verifica della firma o decifratura. Le indicazioni di scadenza su richieste e avvisi non garantiscono la cancellazione da parte dei relay, e le misurazioni delle prestazioni fornite da chi ha pubblicato la release sono state effettuate su un laptop.

### Pacto {#pacto}

Pacto, un'app desktop per l'organizzazione di comunità che usa i gruppi Marmot legacy insieme ai DM NIP-17, ha rilasciato la versione non firmata [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5), che consente di modificare i messaggi inviati entro un minuto. Le sue [correzioni alla consegna dei DM](https://github.com/covenant-gov/pacto-app/pull/425) fanno fallire immediatamente gli invii quando il pool non contiene alcun relay attendibile e instradano gli indicatori di digitazione attraverso relay attendibili. Alcune pull request aperte e non ancora unite aggiungerebbero [eventi per le squad](https://github.com/covenant-gov/pacto-app/pull/488) e [documenti cifrati per le squad](https://github.com/covenant-gov/pacto-app/pull/490).

### Mialuna {#mialuna}

Mialuna, un client Nostr in Flutter orientato ai contenuti multimediali, ha pubblicato un [annuncio di rilascio della versione 0.19.0](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez) che aggiunge richieste di cancellazione per le storie dell'utente alla loro scadenza. Il [commit del changelog](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886) registra le richieste di cancellazione ai relay e la cancellazione dei media su Blossom: gli account con chiave locale le eseguono automaticamente, mentre gli account Amber o bunker attendono che l'utente scelga Delete now. L'APK e il suo comportamento sul dispositivo non sono stati verificati in modo indipendente. Le richieste di cancellazione non possono garantire che relay o server cancellino effettivamente i dati.

### whereAreYou {#whereareyou}

whereAreYou, un'app Android che condivide la posizione all'interno di cerchie a cui si accede tramite codice QR o link di invito, cifra le coordinate con AES-256-GCM e le invia attraverso relay pubblici. Un [commit sulla firma dei membri](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e) impedisce a chi possiede la chiave della cerchia di pubblicare spacciandosi per un altro membro, e ogni dispositivo deve essere aggiornato. Per il [backup dell'identità in Base45](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc), l'autore avverte che chiunque fotografi il codice QR potrebbe indovinarne offline il codice a otto cifre, secondo la sua stima nel giro di decine di minuti di tempo GPU; non è stato pubblicato alcun benchmark. La fonte non offre alcuna attestazione di sicurezza.

## Lavori su protocollo e specifiche {#protocol-and-spec-work}

### Buzz definisce le route per le credenziali degli agenti autorizzati dal proprietario {#buzz-defines-owner-authorized-agent-credential-routes}

Buzz ha unito [NIP-FA](/it/topics/nip-fa/), una [bozza per le credenziali degli agenti autorizzati dal proprietario](https://github.com/block/buzz/pull/9015), che definisce le route di concessione, asserzione e revoca per gli agenti autorizzati tramite l'attestazione del proprietario [NIP-OA](/it/topics/nip-oa/). Una concessione deriva da uno scambio di token RFC 8693 che associa la sessione del proprietario a una prova di autenticazione HTTP [NIP-98](/it/topics/nip-98/) dell'agente, e la revoca disconnette l'agente e impedisce alla sua chiave di registrarsi nuovamente. NIP-FA è una specifica di Buzz unita solo nel codice sorgente, senza alcuna affermazione di attivazione in produzione o di interoperabilità.

### Le firme post-quantistiche degli eventi ottengono regole di validazione precise {#post-quantum-event-signatures-gain-exact-validation-rules}

La proposta di firme post-quantistiche, aperta da tempo, ha ottenuto [regole di validazione ML-DSA-44 precise per gli eventi Nostr](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6). Chiavi e firme hanno lunghezze fisse, i verificatori controllano la firma sui 32 byte grezzi del digest dell'ID evento con un contesto vuoto, e non è ammesso alcun algoritmo di fallback. L'identità proposta non ha una codifica bech32 [NIP-19](/it/topics/nip-19/), e le nuove firme non rendono resistenti agli attacchi quantistici né i payload cifrati [NIP-44](/it/topics/nip-44/) né i gift wrap [NIP-59](/it/topics/nip-59/).

### Una proposta di precondizione firmata previene la perdita di sostituzioni di eventi {#a-proposed-signed-precondition-prevents-lost-event-replacements}

Una pull request aperta su Buzz [propone una precondizione firmata NIP-CS locale al progetto](https://github.com/block/buzz/pull/8835) per gli eventi sostituibili e indirizzabili; non si tratta di una NIP ufficiale. Il tag firmato indica l'ID della head corrente oppure `none`, e il relay lo verifica in modo atomico sotto un lock sulla coordinata, rifiutando una scrittura obsoleta con un OK false o un HTTP 409 senza memorizzare nulla. Le scritture senza tag funzionano come prima, e il tag non offre alcuna garanzia di compare-and-swap tra relay diversi.

## Approfondimento NIP: NIP-31 e NIP-73 {#nip-deep-dive-nip-31-and-nip-73}

I client incontrano spesso contenuti che non comprendono in modo nativo. [NIP-31: Dealing with Unknown Event Kinds](/it/topics/nip-31/) assegna un'etichetta leggibile a un kind di evento sconosciuto, mentre [NIP-73: External Content IDs](/it/topics/nip-73/) dà un nome a soggetti esterni a Nostr, come libri o pagine web. Le due convenzioni sono specifiche già esistenti e indipendenti l'una dall'altra ([testo di NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md), [testo di NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)).

### NIP-31 è contrassegnato come non raccomandato {#nip-31-is-marked-unrecommended}

L'attuale [testo di NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md) si apre con un avviso che lo contrassegna come `unrecommended` perché "inutilmente appesantito", e la sua riga di stato indica draft, unrecommended e optional. Sui relay esistono già eventi che usano questa convenzione, quindi i meccanismi descritti di seguito spiegano come i client li leggono, senza alcuna raccomandazione per nuovi protocolli.

### Cosa trasporta un tag alt {#what-an-alt-tag-carries}

Secondo la [specifica](https://github.com/nostr-protocol/nips/blob/master/31.md), l'autore di un kind personalizzato non destinato a essere letto come testo aggiunge un tag `alt` con un breve riassunto in testo semplice. Non ci si aspetta che i client incentrati sul kind 1 richiedano altri kind, ma gli utenti possono comunque citare tali eventi nelle note, dove un riassunto fornisce contesto. Un'etichetta non può esprimere un voto né dare seguito a una richiesta rivolta a un wallet. Per un'interazione più ricca la specifica rimanda a [NIP-89: Recommended Application Handlers](/it/topics/nip-89/).

Poiché `alt` è un tag, l'ID dell'evento e la firma definiti in [NIP-01](/it/topics/nip-01/): [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md) lo coprono. Una firma valida autentica un riassunto controllato dall'autore: dimostra che l'autore ha pubblicato l'etichetta, non che l'etichetta sia accurata, quindi sono possibili riassunti fuorvianti. I tag sono pubblici, perciò un `alt` su un evento con contenuto cifrato ne espone il riassunto e può rivelare ciò che il contenuto nasconde. Queste proprietà derivano dall'involucro di [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), non dal testo normativo di NIP-31. Un tag `alt` di primo livello è inoltre distinto dal campo `alt` di descrizione delle immagini all'interno di `imeta`, e i renderer li analizzano separatamente.

### Come due client leggono alt {#how-two-clients-read-alt}

Nella [scheda per eventi sconosciuti di noStrudel al commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), il primo tag `alt` viene ripulito dagli spazi iniziali e finali e diventa l'etichetta principale, con una riga facoltativa `Using <client>`. Un valore mancante o vuoto produce `Unknown event (kind ...)`, e fino a tre righe di contenuto vengono mostrate in modo indipendente. Lo stesso componente risolve il tag `client` tramite i template degli handler NIP-89, mostrando Open quando esiste un indirizzo condivisibile e `Open in <client>` quando si risolve un link valido a un handler. La spiegazione e l'apertura nell'app sono controlli separati.

Il file [UnknownEventDigest.kt di Amethyst al commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) privilegia il contenuto che classifica come prosa e in mancanza ripiega su `alt`. Il suo parser ripulisce i valori e prende il primo `alt` non vuoto, quindi un evento il cui primo `alt` è vuoto può ricevere qui un'etichetta diversa rispetto a noStrudel. Entrambe le descrizioni riflettono il codice sorgente a quei commit, non un comportamento confermato nelle release.

### Esempio: un sondaggio con un'etichetta alt {#example-a-poll-with-an-alt-label}

Il sondaggio di kind 1068 riportato qui sotto è stato recuperato da wss://relay.damus.io, e il suo ID e la sua firma BIP340 risultano validi secondo le regole di [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Un renderer generico può mostrare il testo bilingue di `alt`, mentre un client che supporta i sondaggi legge i tag `option` e `polltype`.

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### Soggetti e famiglie in NIP-73 {#nip-73-subjects-and-families}

La [specifica NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md) (draft, optional, senza il contrassegno unrecommended) inserisce un soggetto esterno in un tag `i` e la sua famiglia di identificatori in un tag `k`, così i client possono interrogare un singolo soggetto esatto oppure un'intera famiglia. Un libro usa `["i", "isbn:9780765382030"]` con `["k", "isbn"]`, mentre una pagina web usa il proprio URL con `k` impostato su `web`. NIP-73 non definisce alcun kind di evento; sono altri eventi a trasportare i tag.

### Normalizzazione e suggerimenti URL {#normalization-and-url-hints}

La corrispondenza dipende da stringhe identiche, quindi la [specifica](https://github.com/nostr-protocol/nips/blob/master/73.md) fissa una forma per ciascuna famiglia: URL normalizzati senza frammento, ISBN senza trattini, geohash in minuscolo, codici ISO 3166 in maiuscolo. Un terzo elemento facoltativo dell'array contiene un suggerimento URL per i client che non hanno una propria interpretazione dell'identificatore. È l'autore a scegliere quel suggerimento, che non fa parte dell'identità. Inoltre non dimostra alcuna titolarità e non indica alcun sito canonico.

### Cosa non dimostra un identificatore condiviso {#what-a-shared-identifier-does-not-prove}

Secondo [NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md), identificatori uguali uniscono le conversazioni e non stabiliscono nient'altro. Un commento firmato identifica chi lo ha scritto, ma non autentica il libro, il sito o l'editore del podcast né mostra chi li controlla. Alias, ISBN specifici di un'edizione e URL che si normalizzano in modo diverso possono dividere un unico soggetto in più thread. Il contesto conta: [NIP-22](/it/topics/nip-22/): [Comment](https://github.com/nostr-protocol/nips/blob/master/22.md) usa `I`/`K` maiuscoli per l'ambito radice e `i`/`k` minuscoli per il genitore, mentre [NIP-39: External Identities in Profiles](/it/topics/nip-39/) usa `i` per le identità del profilo, quindi non tutti i tag `i` sono soggetti NIP-73.

### NIP-73 nel codice di parser e renderer {#nip-73-in-parser-and-renderer-code}

Il file [nip73.rs di rust-nostr al commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) analizza i prefissi noti trasformandoli in un `ExternalContentId` tipizzato e converte un eventuale suggerimento in un URL tipizzato, emettendo il terzo elemento del tag solo quando il suggerimento esiste. I suoi test mantengono gli ISBN con trattini: il parser rimuove il prefisso e memorizza il resto senza applicare la normalizzazione prevista dalla specifica, quindi il parsing tipizzato non garantisce stringhe canoniche. Separa inoltre gli ID di chain dalla famiglia, mappando `ethereum:100:tx:<hash>` su `ethereum:tx`. Quella revisione non ha una variante per i paesi `iso3166`.

Il file [DisplayExternalId.kt di Amethyst al commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) indirizza gli identificatori geohash e hashtag verso visualizzazioni dedicate. Anche gli identificatori URL hanno una visualizzazione dedicata, mentre gli altri tipi supportati finiscono in un chip di ambito generico. Un URL apre la route di thread propria dell'app per quella pagina. Con le anteprime disattivate, il rendering normale mostra un semplice chip con il link e non richiede alcuna anteprima. Con le anteprime attivate, il recupero di un'anteprima mancante può contattare il sito di destinazione. Disattivare le anteprime evita quella richiesta nel rendering normale. Nessuno dei due file stabilisce il comportamento nelle release.

### Esempio: un commento su una pagina web {#example-a-comment-on-a-webpage}

Questo commento di kind 1111, recuperato da wss://nos.lol, inserisce lo stesso URL pubblico di un thread Reddit sia nella coppia `I`/`K` sia nella coppia `i`/`k`, con `web` come famiglia secondo [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) e NIP-73. Il suo ID e la sua firma risultano validi: questo identifica chi ha scritto il commento e non dice nulla sulla pagina collegata.

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
