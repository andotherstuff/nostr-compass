---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "Nostr Compass #39 segue i flussi di lavoro git firmati, la pubblicazione dal browser, gli streaming in diretta self-hosted, il consenso sui relay delle comunità, gli eventi privati, le release mirate e il contratto dei link NIP-21/NIP-27."
---

Bentornati su [Nostr Compass](https://nostrcompass.org), la vostra guida settimanale a Nostr.

**Questa settimana:** [ngit e GitWorkshop](https://ngit.dev/v3) portano i flussi di lavoro git firmati su Nostr e [Blossom](/it/topics/blossom/), [nsite-clay](https://github.com/jooray/nsite-clay) rende recuperabile la pubblicazione dal browser e [Wingman App](https://github.com/OtherStuffAI/wm-app) riunisce navigazione, firma locale, autenticazione e file. [Shosho e Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) collegano gli streaming self-hosted a Nostr, [Communitator](https://github.com/dyne/communitator) rende ispezionabili i modelli dei relay prima della firma, [cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) pubblica le fasce orarie per gli appuntamenti e [Plektos](https://github.com/derekross/plektos/pull/16) cifra gli eventi privati. Le release con tag aggiungono interventi per il recupero e la privacy in [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4), [Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), [LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) e [SkateSpots](https://zapstore.dev/apps/org.skatespots.app). Il lavoro di sviluppo comprende il rendering di [NIP-27](/it/topics/nip-27/), le preferenze dei relay firmate in [Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397), le destinazioni di pagamento [NIP-A3](/it/topics/nip-a3/) e i mirror Blossom. Le modifiche integrate nel [repository delle NIP](https://github.com/nostr-protocol/nips) chiariscono le sottoscrizioni riservate alle dirette e i dati applicativi autenticati. Il nostro approfondimento spiega come i link [NIP-21](/it/topics/nip-21/) e i riferimenti NIP-27 trasportano profili ed eventi Nostr tra le applicazioni.

## Notizie principali

### I flussi di lavoro git firmati portano CI, repository privati e release su Nostr

Il [lancio della v3 dell'8 settembre](https://ngit.dev/v3) riunisce ngit, GitWorkshop, ngit-grasp e ngit-ci in un unico flusso di lavoro firmato. [ngit](https://ngit.dev/ngit.git) trasporta branch, patch e richieste di pull come eventi [NIP-34](/it/topics/nip-34/), mentre [GitWorkshop](https://ngit.dev/gitworkshop.git) fornisce l'interfaccia per la revisione. Il lancio aggiunge ngit-ci 0.1, un servizio self-hosted di integrazione continua le cui istruzioni e i cui risultati viaggiano come eventi Nostr firmati, consentendo l'esecuzione dei controlli su hardware gestito dai manutentori insieme alla revisione del codice.

La stessa release dota [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) di repository privati tramite l'estensione GRASP-08 per i repository privati e rende esplicita l'autorità dei manutentori. I registri firmati delle release possono puntare agli asset in [Blossom](/it/topics/blossom/), mantenendo sia i metadati delle release sia i file indirizzati per contenuto al di fuori di una forge ospitata. Il [nuovo sito della documentazione](https://ngit.dev/v3) riunisce i componenti relativi al client, ai repository privati, alla CI e al web.

### nsite-clay rende recuperabile la pubblicazione dal browser

Una [correzione del 31 agosto per le richieste del firmatario](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), il [recupero della pubblicazione](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0) e i [controlli di modifica del 2 settembre](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) rendono [nsite-clay](https://github.com/jooray/nsite-clay) uno strumento di pubblicazione dal browser per un sito a pagina singola. L'utente modifica direttamente il modello a oggetti del documento, serializza il risultato, lo carica come blob [Blossom](/it/topics/blossom/) indirizzato per contenuto e ripubblica il manifest [NIP-5A](/it/topics/nip-5a/) del sito. Non sono necessari una build locale né un server.

Lo [strumento di pubblicazione dal browser](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) consente ora di recuperare una pubblicazione non riuscita e riduce le richieste ripetute del firmatario, mentre la [guida alla modifica](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) documenta il ciclo operativo. Il risultato rimane un normale sito NIP-5A per i gateway esistenti.

### Wingman App riunisce navigazione, firma e file

Il lavoro di settembre aggiunge a [Wingman App](https://github.com/OtherStuffAI/wm-app) [selettori di file](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), la [pubblicazione del profilo](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), il [ripristino sicuro del firmatario e della sessione](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6) e [build mobili testate](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac). La sua shell Flutter inserisce un provider [NIP-07](/it/topics/nip-07/) nelle pagine aperte all'interno dell'app, mentre Flight Deck e Drive, supportato da Tower, offrono un'area di lavoro e uno spazio per i file accanto al browser.

Wingman firma le richieste HTTP autenticate usando [NIP-98](/it/topics/nip-98/). L'[implementazione delle richieste](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) costruisce l'evento che un server verifica prima di rispondere, offrendo a un'unica identità installata un percorso di approvazione coerente per le azioni sui relay, la firma nelle applicazioni web e i file.

### Shosho integra gli stream self-hosted di Livelier

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) è stato pubblicato il 1° settembre con il supporto a [Livelier](https://github.com/r0d8lsh0p/livelier), il cui [aggiornamento delle attribuzioni del 31 agosto](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc) identifica il bridge e la sorgente Owncast nei profili collegati tramite bridge. Livelier monitora la directory pubblica di Owncast, verifica se uno stream video è in diretta e pubblica quindi un evento indirizzabile `kind:30311` [NIP-53](/it/topics/nip-53/). La scoperta avviene tramite Nostr, mentre il video rimane sul server di chi trasmette.

La chat attraversa il bridge sotto forma di eventi `kind:1311`. La [struttura del bridge](https://github.com/r0d8lsh0p/livelier) apre una connessione sul lato della sorgente solo mentre un lettore Nostr è iscritto, contrassegna le identità derivate e invia la chat transitoria a un relay che la elimina dopo tre ore. Il relay di scoperta accetta la scrittura di eventi live soltanto dalla chiave del bridge; il relay della chat utilizza l'[autenticazione NIP-42](/it/topics/nip-42/) e i [contrassegni per eventi protetti NIP-70](/it/topics/nip-70/).

### Communitator rende ispezionabili i modelli dei relay prima della firma

La [serie di aggiornamenti di lancio del 31 agosto](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c) fornisce a [Communitator](https://github.com/dyne/communitator) modelli canonici per gli elenchi di relay kind `10002`, i server Blossom kind `10063` e le caselle di posta dei messaggi privati kind `10050`. Prima che un firmatario si connetta, l'applicazione mostra endpoint normalizzati, autorizzazioni di lettura e scrittura, event kind, relay di pubblicazione fissi e destinazioni.

Il [flusso limitato di firma e pubblicazione](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501) separa la connessione dall'applicazione. Ogni evento viene firmato separatamente, una singola esecuzione utilizza al massimo quattro connessioni WebSocket e una destinazione viene conteggiata solo dopo un `OK` positivo secondo [NIP-01](/it/topics/nip-01/). I risultati distinguono tra consegna completa, parziale, non riuscita e annullata. I modelli condivisi rimangono raccomandazioni non attendibili; l'[interfaccia per il consenso](https://github.com/dyne/communitator#security-and-consent) illustra l'osservabilità dei relay e della rete.

### cal.emre.xyz pubblica la disponibilità per gli appuntamenti tramite NIP-52

Il repository pubblico è stato aperto con un [commit iniziale del 2 settembre](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743), seguito il 3 settembre da un [annuncio firmato dell'handler](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) per [cal.emre.xyz](https://cal.emre.xyz). Un host pubblica la propria disponibilità come evento `kind:31923` [NIP-52](/it/topics/nip-52/); un ospite pubblica una conferma RSVP `kind:31925`.

Il servizio legge dai relay gli eventi dell'host e le conferme RSVP accettate che indicano periodi occupati, esclude gli intervalli temporali sovrapposti e mantiene gli eventi Nostr come registro della pianificazione senza copiarli in un database separato. Gli host possono firmare con [NIP-07](/it/topics/nip-07/), [NIP-46](/it/topics/nip-46/) o una chiave locale; gli ospiti possono generare una chiave separata. Il suo [repository](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) rende inoltre disponibili il relativo `naddr` e i link al calendario, con l'email disabilitata per impostazione predefinita.

### Plektos riunisce gli eventi privati in un unico canale cifrato

L'[implementazione degli eventi privati del 2 settembre](https://github.com/derekross/plektos/pull/12) trasforma ogni incontro di [Plektos](https://github.com/derekross/plektos) in un canale privato all'interno di una comunità cifrata [Concord](/it/topics/concord-protocol/). L'elenco degli invitati, l'elenco delle conferme RSVP, la bacheca delle iscrizioni, la discussione, i contributi, le immagini di copertina, le modifiche e le eliminazioni vengono cifrati insieme; un invito contiene soltanto la chiave di quell'evento e non viene pubblicato alcun evento di calendario in chiaro.

L'[audit del ciclo di vita del 6 settembre](https://github.com/derekross/plektos/pull/14) usa come riferimento l'id della definizione dell'evento per consentire una ricerca diretta quando esistono più di 500 wrap, mantenendo al contempo un sistema di ripiego paginato. I pacchetti di invito scadono 30 giorni dopo la conclusione di un evento e possono essere disabilitati, ma chi ha già ottenuto la chiave di un canale può conservarla. Una [correzione separata per la sicurezza del parser](https://github.com/derekross/plektos/pull/16) fa sì che gli identificatori type-length-value (TLV) [NIP-19](/it/topics/nip-19/) malformati restituiscano un errore anziché bloccare il parser.

## Release con tag

### Vector 0.4.4 rende più sicuro il recupero delle comunità cifrate

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) è stato pubblicato il 31 agosto con correzioni per il recupero delle comunità, la rotazione delle chiavi, la moderazione e l'instradamento delle risposte. La rifondazione impedisce a una comunità attaccata di utilizzare il percorso di invito sfruttato dagli aggressori; la nuova appartenenza sostituisce lo stato locale obsoleto; inoltre, un singolo membro non raggiungibile non blocca più l'elenco dei membri. Le rotazioni vuote vengono rifiutate, le promozioni mantengono i membri online e le operazioni non vengono eseguite quando i membri necessari non sono raggiungibili.

La [release](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) rende inoltre persistenti le eliminazioni e i ban applicati dai moderatori, cifra nuovamente il registro degli ospiti dopo una modifica della password, ricollega le risposte alle notifiche alla rispettiva conversazione dopo un riavvio e utilizza esclusivamente percorsi multiplayer verificati. Si tratta di controlli per il recupero, non della revoca di chiavi già ottenute.

### Primal Android 3.5.27 verifica l'identità del firmatario e del wallet

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) è stato pubblicato il 3 settembre, dopo l'integrazione, il 31 agosto, della [verifica dell'identità del firmatario](https://github.com/PrimalHQ/primal-android-app/pull/1108) e dell'[autenticazione delle richieste del wallet](https://github.com/PrimalHQ/primal-android-app/pull/1105). La firma locale rifiuta una richiesta la cui identità non corrisponde all'account in uso, mentre le richieste [NIP-47](/it/topics/nip-47/) in arrivo vengono autenticate prima dell'elaborazione. L'instradamento degli zap-poll invia inoltre i voti all'autore del sondaggio quando quest'ultimo compare in una risposta.

### GRAIN 0.8.0-rc2 chiude un percorso con conferma ma senza archiviazione

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) è stato pubblicato il 7 settembre dopo che un errore di archiviazione aveva consentito l'invio di `OK` prima che il writer asincrono del database LMDB rilevasse l'esaurimento dello spazio disponibile. Ora il relay avvisa all'80 e al 95 percento, rifiuta nuovi eventi al 97 percento lasciando spazio per le eliminazioni e segnala gli errori del writer successivi all'accettazione. La procedura di conservazione parte dagli elementi più vecchi, la fase di arresto gestisce i messaggi tardivi e i filtri non validi non causano più l'eliminazione di quelli validi associati.

La [release](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) verifica inoltre gli annunci di monitoraggio di kind `10166` e i rapporti sui relay di kind `30166`, elimina i rapporti obsoleti, mantiene i relay configurati come opzione di riserva e riporta limiti e autenticazione effettivi in [NIP-11](/it/topics/nip-11/) anziché valori zero statici.

### LibreNostr 0.5.0–0.5.2 interrompe le connessioni se l'instradamento Tor non è disponibile

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) è stato pubblicato il 7 settembre con una modalità Orbot che instrada relay, zap, caricamenti, contenuti multimediali, riproduzione e anteprime attraverso un'unica porta SOCKS, oltre a una correzione per un arresto anomalo della schermata degli zap. Se Orbot o il proxy non sono disponibili, le connessioni vengono interrotte anziché passare inavvertitamente a un percorso diretto. La [versione 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) impedisce che le ricerche [NIP-50](/it/topics/nip-50/) lente ritardino i risultati locali; la [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) sostituisce il layout ricorsivo dei thread e ne corregge l'ordinamento.

Il [comportamento con interruzione in caso di errore](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) si applica a ogni interfaccia di rete elencata nella release ed è necessario un riavvio perché questi client rimangono attivi a lungo. Le release correttive mantengono questa scelta, limitando al contempo errori non correlati relativi alla ricerca, alla profondità dello stack e al layout.

### SkateSpots aggiunge un percorso verso un relay sul dispositivo

La [release firmata dell'8 settembre su Zapstore](https://zapstore.dev/apps/org.skatespots.app) aggiunge a SkateSpots un relay Citrine opzionale. Spot, crew, messaggi e dati delle mappe possono essere caricati localmente; i post vengono messi in coda offline e il telefono ne conserva una copia locale. I contenuti esistenti delle raccolte e dei messaggi rimangono crittografati end-to-end. Le verifiche dei pagamenti richiedono gli importi delle fatture e le ricevute degli zap emesse dal provider prima di concedere l'accesso o conteggiare i contributi.

Il [relay locale](https://zapstore.dev/apps/org.skatespots.app) è un'opzione per l'archiviazione e la continuità, non un sostituto di ogni relay remoto. Consente a uno skater di continuare a operare durante un periodo senza connessione e di sincronizzare in seguito l'attività firmata, mentre le modifiche ai pagamenti impediscono che una ricevuta creata dallo stesso utente diventi una prova dell'avvenuto pagamento.

### Whistle 1.8.15 corregge il ripristino del ciclo di vita dei gruppi crittografati

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) è stato pubblicato il 3 settembre dopo che una correzione del ciclo di vita su Android ha impedito ai gestori dello stato a livello di route di terminare le sottoscrizioni ai relay e gli aggiornamenti della posizione validi per l'intera applicazione. Le note di rilascio descrivono inoltre l'aggiornamento dello stato della connessione dopo il blocco o la modalità doze e, nel caso osservato, il recupero di un arretrato di 501 eventi.

Il [bug](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) legava la gestione di un servizio di lunga durata a una schermata di breve durata. Mantenere attiva l'istanza associata all'activity e controllare il socket prima di una lettura singola riduce la probabilità che la normale navigazione su Android e la sospensione in background facciano apparire vuoto un gruppo.

### TWENTY ONE Companion 1.12.0 separa i DM crittografati dalla chat precedente

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) è stato pubblicato il 5 settembre con DM crittografati in modalità gift-wrap secondo [NIP-17](/it/topics/nip-17/). La casella dei messaggi crittografati è separata dalla precedente chat dello spazio, che resta distinta perché quei messaggi non sono mai stati crittografati e non possono essere migrati. PDF e video sono supportati nel rispetto delle politiche dei relay e i contenuti nascosti a livello personale vengono sincronizzati senza diventare esclusioni imposte dai moderatori.

La [separazione visibile](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) fa parte del modello di sicurezza. Definire la cronologia precedente una casella dei messaggi sicura ne rappresenterebbe in modo errato la provenienza, mentre migrarla silenziosamente farebbe supporre l'esistenza di una crittografia che non era presente quando è stata scritta.

### ZapStore 1.1.2 convalida gli id degli eventi e la rotazione dei certificati

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) è stato pubblicato il 4 settembre con la convalida degli id degli eventi secondo NIP-01: il client ricalcola l'id di un evento in entrata e rifiuta eventuali discrepanze prima di utilizzarlo. La release identifica inoltre i pacchetti installati al di fuori di ZapStore. Sul server, la [conservazione degli hash dei certificati](https://github.com/zapstore/relay/pull/8) mantiene i tag `apk_certificate_hash` ripetuti, così la rotazione delle chiavi di firma Android può preservare una catena approvata.

La [verifica dell'id dell'evento](https://github.com/zapstore/zapstore/releases/tag/1.1.2) impedisce a un relay o a una cache di modificare tag o contenuto mantenendo il vecchio id. L'indicatore della fonte di installazione fornisce informazioni distinte sulla provenienza quando un pacchetto Android con lo stesso id applicazione proviene da un altro canale.

### Amber 6.6.1 mantiene attribuibili le risposte del firmatario

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) è stato pubblicato il 4 settembre dopo che l'analisi dei permessi è stata corretta per tollerare l'assenza del campo opzionale `kind` e le richieste di firma rifiutate hanno iniziato a restituire l'id della richiesta originale. Le applicazioni chiamanti possono associare un rifiuto all'operazione inviata. La release aggiorna inoltre le impostazioni predefinite del firmatario remoto e aggiunge un relay di indicizzazione.

Nel loro insieme, queste [correzioni](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) preservano l'attribuzione in entrambe le direzioni: un record di autorizzazione rimane utilizzabile quando manca un campo opzionale e un rifiuto resta associato alla richiesta che lo ha provocato. Le modifiche ai relay predefiniti influiscono sulla scoperta, ma non sostituiscono la decisione di autorizzazione locale del firmatario.

## In fase di sviluppo

### Zap Cooking visualizza i riferimenti NIP-27 con indicazioni sui relay

[Il merge del 4 settembre](https://github.com/zapcooking/frontend/pull/665) consente a [Zap Cooking](https://github.com/zapcooking/frontend) di visualizzare i riferimenti `nostr:npub` e `nostr:nprofile` in articoli, ricette, anteprime dell'editor e viste di stampa. Gli identificatori non validi restano testo, la risoluzione non è bloccante e l'editor mostra l'anteprima del Markdown che verrà firmato. Quando sono disponibili informazioni sui relay, un semplice `npub` diventa un `nprofile` con relay outbox e un tag `p` corrispondente.

Nella stessa settimana sono state corrette le [letture del kind `30023` limitate all'autore](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7), sono stati aggiunti [relay di ricerca NIP-50 verificati](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea), con deduplicazione e protezioni contro le query obsolete, e sono state riparate le [chiamate ai wallet NIP-47](https://github.com/zapcooking/frontend/pull/705), dopo che modifiche alle dipendenze avevano compromesso saldi e cronologia.

### Conduit riconcilia le preferenze firmate per relay e Blossom

[Conduit](https://github.com/Conduit-BTC/conduit-mono) ha integrato la [modifica delle preferenze Blossom](https://github.com/Conduit-BTC/conduit-mono/pull/374) il 2 settembre e la [riconciliazione delle preferenze firmate](https://github.com/Conduit-BTC/conduit-mono/pull/397) il 7 settembre. Market e Merchant conservano l'elenco di relay kind `10002` valido più recente e la dichiarazione inbox kind `10050`, mantengono un elenco firmato utilizzabile quando un evento più recente è malformato, distinguono un elenco esplicitamente vuoto da una ricerca non disponibile e non sostituiscono i relay dichiarati che non funzionano con i valori predefiniti del codice.

[L'editor del kind `10063`](https://github.com/Conduit-BTC/conduit-mono/pull/374) consente a un utente di caricare, riordinare, esaminare, firmare esternamente, pubblicare e rileggere un elenco ordinato di server multimediali HTTPS senza contattare tali server né inserire un valore predefinito non dichiarato.

### I destinatari di pagamento NIP-A3 arrivano in tre client

Dal 1° al 3 settembre, [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) e [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) hanno implementato i destinatari di pagamento NIP-A3 kind `10133`. Amethyst offre un passaggio facoltativo solo quando esiste un destinatario compatibile e non lo trasforma in uno zap; Grimoire usa un registro fisso prima di creare gli URI del wallet; Pollerama convalida gli indirizzi Monero e recupera l'elenco di relay dell'autore prima di interrogare i destinatari. Ogni client necessita comunque di un metodo di pagamento consentito, di un percorso tramite relay e di una visualizzazione accurata.

### Ditto amplia il fallback Blossom e gli incorporamenti live

[Ditto](https://github.com/soapbox-pub/ditto) ha integrato un [fallback Blossom esteso e il mirroring](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07) il 6 settembre. Avatar, badge, banner, immagini delle comunità, emoji personalizzate e icone delle applicazioni ora vengono cercati sui server dichiarati usando lo stesso hash del blob; i caricamenti per il mirroring usano un token di autorizzazione BUD-11 standard. Una [modifica del 4 settembre](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa) ha aggiunto incorporamenti compatti per le dirette `kind:30311`.

## Lavori sul protocollo e sulle specifiche

### Possibilità di implementazione Nostr

[NIP-01](/it/topics/nip-01/) ora chiarisce [il filtro `limit: 0`](https://github.com/nostr-protocol/nips/pull/2460), integrato il 4 settembre. Un relay DEVE restituire zero eventi archiviati, DEVE inviare `EOSE` al completamento delle query iniziali e DEVE mantenere attiva la sottoscrizione per i nuovi eventi corrispondenti. I client possono aprire una sottoscrizione riservata ai nuovi eventi con un solo campo di filtro, mantenendo al contempo la cronologia locale. Il chiarimento documenta un comportamento compatibile tra diverse implementazioni di relay e relay pubblici.

[NIP-78](/it/topics/nip-78/) ha ricevuto un [requisito di autenticazione per i dati delle applicazioni](https://github.com/nostr-protocol/nips/pull/2458), integrato il 3 settembre. I relay DOVREBBERO richiedere l'autenticazione [NIP-42](/it/topics/nip-42/) per i kind `78` e `30078` e DOVREBBERO fornirli soltanto all'autore autenticato dell'evento. Si tratta di un DOVREBBERO, non di una garanzia di riservatezza: i client non possono considerare relay arbitrari come archivi privati. Il merge sconsiglia inoltre l'uso di kind personalizzati per i dati delle applicazioni come formato generico di scambio pubblico.

[NIP-AC](/it/topics/nip-ac/) è stata aperta il 4 settembre come [proposta di segnalazione WebRTC](https://github.com/nostr-protocol/nips/pull/2461) esplicitamente aperta. Usa kind effimeri provvisori per ping, richieste di connessione, offerte, risposte e candidati ICE, indirizzati tramite `p` e raggruppati mediante un tag di sessione `e`; il kind `30600` supporta il rilevamento. I relay DOVREBBERO trasmettere e NON DEVONO archiviare tali eventi di segnalazione mentre i peer si connettono direttamente. I numeri restano provvisori, i client DOVREBBERO usare gli [elenchi di relay NIP-65](/it/topics/nip-65/) e le applicazioni che richiedono riservatezza DOVREBBERO cifrare il contenuto di offerte, risposte e candidati con [NIP-44](/it/topics/nip-44/).

## Approfondimento NIP: link URI e riferimenti nel testo degli eventi

Un identificatore Nostr necessita di un significato trasportabile prima che un'altra applicazione possa aprirlo. [NIP-21](/it/topics/nip-21/) inserisce un identificatore [NIP-19](/it/topics/nip-19/) dopo lo schema URI `nostr:`, fornendo a browser, sistemi operativi e applicazioni un unico formato instradabile. [NIP-27](/it/topics/nip-27/) definisce il significato dello stesso URI all'interno del `content` leggibile di un evento. NIP-21 attraversa il confine di un'applicazione; NIP-27 mantiene un riferimento a un profilo o a un evento all'interno di un testo firmato. Nessuna delle due crea un event kind né modifica i messaggi dei relay; le [due specifiche](https://github.com/nostr-protocol/nips/tree/master) definiscono soltanto il comportamento relativo ai collegamenti e alla visualizzazione.

### Instradamento degli URI e semantica di NIP-19

[La grammatica di NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) è composta da `nostr:` seguito da una singola entità bech32 NIP-19. `nsec` è escluso perché codifica una chiave privata. Non sono presenti componenti di autorità, percorso o query, quindi un link conforme è `nostr:npub1...`, non `nostr://npub1...`. Una piattaforma o un client può registrarsi come gestore; la specifica non sceglie l'applicazione installata né definisce un'alternativa web.

Il prefisso indica al client cosa decodificare. `npub` contiene una chiave pubblica e `note` un id evento. `nprofile` aggiunge suggerimenti facoltativi sui relay a un profilo; `nevent` aggiunge relay, autore e kind a un id evento; `naddr` contiene invece l'autore, il kind e l'identificatore `d` di un evento indirizzabile, con relay facoltativi. Questi formati utilizzano i [campi tipo-lunghezza-valore di NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md). I suggerimenti restringono la ricerca, ma non dimostrano né che il relay disponga dell'evento né il controllo da parte dell'autore. Per ogni evento recuperato è comunque necessario ricalcolare l'id e verificare la firma.

Il formato per i profili nella [specifica NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) è:

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) definisce anche bridge HTML: una pagina che presenta un evento Nostr può inserire il relativo `naddr` in `<link rel="alternate">`, mentre un profilo può inserire un `nprofile` in `<link rel="me">` o `<link rel="author">`.

### Rendering di NIP-27 e tag facoltativi

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) si applica a contenuti leggibili degli eventi, come le note di kind `1` e gli articoli di kind `30023`. Un editor può mostrare `@name`, ma pubblica `nostr:nprofile1...` nella stringa firmata. Un lettore analizza l'URI, decodifica la relativa entità NIP-19, recupera la destinazione e può visualizzare un nome, una scheda, un'anteprima o un link locale. Se la decodifica non riesce, l'URI rimane testo normale. Il contenuto grezzo non deve essere riscritto: modificarlo cambia la serializzazione NIP-01, l'id e la firma.

I riferimenti nei contenuti e i tag svolgono funzioni correlate ma distinte. [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) descrive i tag facoltativi `p` ed `e` e il tag `q` di [NIP-18](/it/topics/nip-18/). Un client può mostrare un riferimento senza creare una notifica o una relazione nel thread; per consentire di individuare una citazione, è opportuno inserire sia l'URI sia un tag `q`. [L'implementazione di Zap Cooking del 4 settembre](https://github.com/zapcooking/frontend/pull/665) segue questa distinzione, mantenendo l'URI e aggiungendo al contempo suggerimenti sui relay e un tag `p` corrispondente. L'aggiunta di `p` o `q` non rende privato l'URI e NIP-27 non prevede una modalità per le menzioni nascoste.

Il seguente [evento di kind `1`](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a) è stato recuperato da `wss://nos.lol` e verificato prima di essere incluso come riferimento concreto a NIP-27. Il suo `content` contiene un `naddr` per un evento indirizzabile indipendente dalla versione. La decodifica restituisce il kind `30402`, l'autore `91036d...310a`, l'identificatore `d` del quaderno di lavoro e un suggerimento `wss://nos.lol/`. I tag `q`, `p`, `t`, `zap` e `client` sono scelte dell'applicazione, non requisiti di NIP-27.```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### Fiducia, comportamento in caso di errore e implementazioni dei client

Un lettore sicuro individua un token `nostr:` completo, convalida bech32, decodifica NIP-19, rifiuta `nsec`, ignora i tipi TLV sconosciuti e lascia invariato il testo malformato o di dimensioni eccessive. `npub` e `nprofile` portano a query sui profili; `note` e `nevent` identificano eventi immutabili; `naddr` seleziona l'evento indirizzabile valido più recente per il relativo kind, autore e tag `d`. I suggerimenti sui relay riducono l'ambito della ricerca, ma non estendono la fiducia. In base alle [regole sugli eventi di NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), il client verifica l'id di un `nevent` recuperato e controlla la firma di ogni candidato `naddr` prima di applicare le regole di sostituzione degli eventi indirizzabili.

Le anteprime in linea sono una scelta del client che comporta costi in termini di privacy e risorse. Recuperare ogni riferimento rivela gli interessi del lettore e può generare una raffica di richieste, quindi i client possono usare una cache, rinviare il recupero finché il riferimento non diventa visibile, limitare le richieste simultanee e richiedere un clic per i contenuti multimediali non riconosciuti. In base a [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md), un'anteprima deve rimanere distinta dal testo firmato dell'autore corrente. Un errore deve essere visibile sotto forma di testo non risolto o di scheda non disponibile, senza essere trattato silenziosamente come contenuto verificato.

Anche la fiducia varia in base al tipo di identificatore. Un `nevent` identifica byte immutabili, quindi un client può rifiutare un evento recuperato il cui id serializzato differisce da quello richiesto. Un `naddr` identifica una coordinata sostituibile, quindi un client deve verificare ogni candidato e applicare le regole per gli eventi indirizzabili prima di decidere quale versione mostrare. In entrambi i casi, un suggerimento sul relay è utile per la prima query, ma non costituisce un'approvazione del relay o del contenuto restituito. La [definizione TLV di NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md) fornisce i dati necessari per rendere espliciti questi controlli.

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) definisce un link portabile che può essere aperto dall'esterno di Nostr, mentre NIP-27 rende lo stesso link persistente all'interno del testo firmato. Un client che implementa soltanto NIP-21 può aprire un URI incollato, ma non visualizzare i riferimenti incorporati. Il supporto completo per NIP-27 aggiunge la scansione, la decodifica sicura, i criteri di recupero, la visualizzazione locale e una scelta esplicita relativa ai tag di notifica e citazione. L'URI condiviso mantiene interoperabili questi livelli senza obbligare i client a presentarli nello stesso modo.[Damus](https://github.com/damus-io/damus) rappresenta i riferimenti in linea come menzioni tipizzate. Il suo [codice per le menzioni](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift) associa `npub` e `nprofile` ai riferimenti ai profili, `note` e `nevent` ai riferimenti agli eventi e `naddr` ai riferimenti agli indirizzi; [NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift) li indirizza alla destinazione appropriata. [Primal Android](https://github.com/PrimalHQ/primal-android-app) [analizza lo schema e i formati incollati](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt), convalida bech32 ed estrae i suggerimenti sui relay, quindi [associa i riferimenti ai modelli del contenuto delle note](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt). [Zap Cooking](https://github.com/zapcooking/frontend/pull/665) visualizza gli stessi riferimenti negli articoli, nelle ricette, nelle anteprime dell'editor e nelle viste di stampa.

---

Invia un DM NIP-17 per condividere un progetto o una notizia tramite il [progetto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
