---
title: 'Nostr Compass #2'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale all'ecosistema del protocollo Nostr.

**Questa settimana:** Tre implementazioni signer [NIP-55](/it/topics/nip-55/) ricevono aggiornamenti: Amber aggiunge caching delle prestazioni, Aegis ottiene supporto URI `nostrsigner:`, e Primal Android si unisce a loro come signer locale completo. Shopstr introduce "Zapsnags" per vendite flash tramite zap. Mostro aggiunge un fondo di sviluppo. Quattro aggiornamenti NIP arrivano inclusi Messaggi Pubblici (kind 24) e miglioramenti alla privacy dei gruppi. Le query cache NDK accelerano di 162x, Applesauce aggiunge reazioni e supporto wallet NIP-60, e Tenex introduce l'architettura RAL per la delega di agenti AI. Nel nostro approfondimento, spieghiamo [NIP-02](/it/topics/nip-02/) (liste follow) e [NIP-10](/it/topics/nip-10/) (threading delle risposte), specifiche fondamentali per costruire timeline sociali e conversazioni.

## Notizie {#news}

**Primal Android Diventa un Signer NIP-55** - Costruendo sul [supporto Nostr Connect della settimana scorsa](/it/newsletters/2025-12-17-newsletter/#primal-android), Primal ha implementato capacita' complete di firma locale attraverso otto pull request unite. L'implementazione include un `LocalSignerContentProvider` completo che espone le operazioni di firma ad altre app Android tramite l'interfaccia content provider di Android, seguendo la specifica [NIP-55](/it/topics/nip-55/). L'architettura separa chiaramente le responsabilita': `SignerActivity` gestisce i flussi di approvazione rivolti all'utente, `LocalSignerService` gestisce le operazioni in background, e un nuovo sistema di permessi consente agli utenti di controllare quali app possono richiedere firme. Questo rende Primal un'alternativa valida ad Amber per gli utenti Android che vogliono mantenere le proprie chiavi in un'app mentre ne usano altre per diverse esperienze Nostr.

**Shopstr Zapsnags: Vendite Flash via Lightning** - Il marketplace nativo Nostr ha introdotto ["Zapsnags"](https://github.com/shopstr-eng/shopstr/pull/211), una funzionalita' di vendita flash che consente agli acquirenti di acquistare articoli direttamente dal loro feed sociale con un singolo zap. L'implementazione filtra le note kind 1 taggate con `#shopstr-zapsnag` e le renderizza come schede prodotto con un pulsante "Zap to Buy" invece del flusso carrello standard. Quando un acquirente fa uno zap, il sistema genera una richiesta di pagamento usando [NIP-57](/it/topics/nip-57/), controlla la ricevuta zap kind 9735 per confermare il pagamento, poi cripta le informazioni di spedizione usando il gift wrapping [NIP-17](/it/topics/nip-17/) prima di inviarle privatamente al venditore. La funzionalita' memorizza i dettagli dell'acquirente localmente per acquisti ripetuti e include una dashboard per commercianti per creare inserzioni di vendita flash. E' una combinazione intelligente di primitive sociali, di pagamento e di privacy che dimostra come il design componibile di Nostr abiliti nuovi pattern di commercio.

**Mostro Introduce Fondo di Sviluppo** - Il bot di trading Bitcoin P2P [NIP-69](/it/topics/nip-69/) ha [implementato commissioni di sviluppo configurabili](https://github.com/MostroP2P/mostro/pull/555) per supportare la manutenzione sostenibile. Gli operatori possono impostare `dev_fee_percentage` tra 10-100% della commissione di trading Mostro (default 30%), che viene automaticamente instradata a un fondo di sviluppo ad ogni scambio riuscito. L'implementazione aggiunge tre colonne database (`dev_fee`, `dev_fee_paid`, `dev_fee_payment_hash`) per tracciare i contributi e valida la percentuale all'avvio del daemon. La documentazione tecnica in [`docs/DEV_FEE.md`](https://github.com/MostroP2P/mostro/blob/main/docs/DEV_FEE.md) spiega il sistema. Questo modello opt-in consente agli operatori di supportare lo sviluppo continuo mantenendo piena trasparenza sull'allocazione delle commissioni.

## Aggiornamenti NIP {#nip-updates}

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Nuovi NIP:**
- **[NIP-A4](/it/topics/nip-a4/) (Messaggi Pubblici, kind 24)** - Un nuovo kind per messaggi dello schermo notifiche progettato per ampio supporto client ([#1988](https://github.com/nostr-protocol/nips/pull/1988)). A differenza delle conversazioni threaded, questi messaggi non hanno concetto di cronologia chat o catene di messaggi. Usano tag `q` (citazioni) invece di tag `e` per evitare complicazioni di threading, rendendoli ideali per semplici notifiche pubbliche che appaiono nel feed notifiche di un destinatario senza creare stato di conversazione.

**Modifiche Significative:**
- **[NIP-29](/it/topics/nip-29/)** - Importante chiarimento della semantica dei gruppi ([#2106](https://github.com/nostr-protocol/nips/pull/2106)). Il tag `closed` ora significa "impossibile scrivere" (sola lettura per non-membri), disaccoppiato dalla meccanica di adesione. Un nuovo tag `hidden` impedisce ai relay di servire eventi di metadati o membri ai non-membri, abilitando gruppi veramente privati che sono impossibili da scoprire senza invito out-of-band. Il tag `private` controlla la visibilita' dei messaggi permettendo comunque metadati pubblici per la scoperta.
- **[NIP-51](/it/topics/nip-51/)** - Aggiunto kind 30006 per set di immagini curate ([#2170](https://github.com/nostr-protocol/nips/pull/2170)), seguendo il pattern di 30004 (articoli) e 30005 (video). Gia' implementato in Nostria.
- **[NIP-55](/it/topics/nip-55/)** - Chiarito l'avvio della connessione per signer Android ([#2166](https://github.com/nostr-protocol/nips/pull/2166)). Gli sviluppatori che implementavano sessioni multi-utente usavano erroneamente `get_public_key` chiamandolo da processi in background. La specifica aggiornata raccomanda di chiamarlo solo una volta durante la connessione iniziale, prevenendo un comune errore di implementazione.

## Approfondimento NIP: NIP-02 e NIP-10 {#nip-deep-dive-nip-02-and-nip-10}

Questa settimana copriamo due NIP essenziali per la funzionalita' sociale: come i client sanno chi seguite e come le conversazioni sono threaded.

### [NIP-02](/it/topics/nip-02/): Lista Follow

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md) definisce gli eventi kind 3, che memorizzano la vostra lista follow. Questo semplice meccanismo alimenta il grafo sociale che rende possibili le timeline.

**Struttura:** Un evento kind 3 contiene tag `p` che elencano le pubkey seguite:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Ogni tag `p` ha quattro posizioni: il nome del tag, la pubkey seguita (esadecimale), un suggerimento URL relay opzionale, e un "petname" opzionale (un soprannome locale). Il suggerimento relay dice ad altri client dove trovare gli eventi di quell'utente. Il petname vi consente di assegnare nomi memorabili ai contatti senza affidarvi ai nomi visualizzati auto-dichiarati.

**Comportamento sostituibile:** Kind 3 rientra nell'intervallo sostituibile (0, 3, 10000-19999), quindi i relay mantengono solo l'ultima versione per pubkey. Quando seguite qualcuno di nuovo, il vostro client pubblica un nuovo kind 3 completo contenente tutti i vostri follow piu' quello nuovo. Questo significa che le liste follow devono essere complete ogni volta; non potete pubblicare aggiornamenti incrementali.

**Costruire timeline:** Per costruire un feed home, i client recuperano il kind 3 dell'utente, estraggono tutte le pubkey dai tag `p`, poi si iscrivono agli eventi kind 1 da quegli autori:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

Il relay restituisce le note corrispondenti, e il client le renderizza. I suggerimenti relay nel kind 3 aiutano i client a sapere quali relay interrogare per ogni utente seguito.

**Petname e identita':** Il campo petname abilita uno schema di naming decentralizzato. Invece di fidarvi di qualsiasi nome un utente dichiara nel suo profilo, potete assegnare la vostra etichetta. Un client potrebbe visualizzare "alice (Mia Sorella)" dove "alice" viene dal suo profilo kind 0 e "Mia Sorella" e' il vostro petname. Questo fornisce contesto che i nomi utente globali non possono.

**Considerazioni pratiche:** Poiche' gli eventi kind 3 sono sostituibili e devono essere completi, i client dovrebbero preservare tag sconosciuti durante l'aggiornamento. Se un altro client ha aggiunto tag che il vostro client non capisce, sovrascrivere alla cieca perderebbe quei dati. Aggiungete nuovi follow invece di ricostruire da zero.

### [NIP-10](/it/topics/nip-10/): Threading Note di Testo

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) specifica come le note kind 1 si referenziano a vicenda per formare thread di risposte. Capire questo e' essenziale per costruire viste di conversazione.

**Il problema:** Quando qualcuno risponde a una nota, i client devono sapere: A cosa e' una risposta? Qual e' la radice della conversazione? Chi dovrebbe essere notificato? NIP-10 risponde a queste domande attraverso tag `e` (riferimenti eventi) e tag `p` (menzioni pubkey).

**Tag marcati (preferiti):** I client moderni usano marcatori espliciti nei tag `e`:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Ottimo punto! Sono d'accordo.",
  "sig": "b7d3f..."
}
```

Il marcatore `root` punta alla nota originale che ha iniziato il thread. Il marcatore `reply` punta alla nota specifica a cui si sta rispondendo. Se rispondete direttamente alla root, usate solo `root` (nessun tag `reply` necessario). La distinzione conta per il rendering: il `reply` determina l'indentazione in una vista thread, mentre `root` raggruppa tutte le risposte insieme.

**Regole di threading:**
- Risposta diretta alla root: Un tag `e` con marcatore `root`
- Risposta a una risposta: Due tag `e`, uno `root` e uno `reply`
- Il `root` rimane costante in tutto il thread; `reply` cambia in base a cosa state rispondendo

**Tag pubkey per notifiche:** Includete tag `p` per tutti quelli che dovrebbero essere notificati. Come minimo, taggate l'autore della nota a cui state rispondendo. La convenzione e' anche includere tutti i tag `p` dall'evento parent (cosi' tutti nella conversazione rimangono nel loop), piu' qualsiasi utente che @menzionate nel vostro contenuto.

**Suggerimenti relay:** La terza posizione nei tag `e` e `p` puo' contenere un URL relay dove quell'evento o contenuto utente potrebbe essere trovato. Questo aiuta i client a recuperare il contenuto referenziato anche se non sono connessi al relay originale.

**Tag posizionali deprecati:** Le prime implementazioni Nostr inferivano il significato dalla posizione del tag invece che dai marcatori: il primo tag `e` era root, l'ultimo era reply, quelli in mezzo erano menzioni. Questo approccio e' deprecato perche' crea ambiguita'. Se vedete tag `e` senza marcatori, sono probabilmente da client piu' vecchi. Le implementazioni moderne dovrebbero sempre usare marcatori espliciti.

**Costruire viste thread:** Per visualizzare un thread, recuperate l'evento root, poi interrogate tutti gli eventi con un tag `e` che referenzia quella root:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Ordinate i risultati per `created_at` e usate i marcatori `reply` per costruire la struttura ad albero. Gli eventi il cui `reply` punta alla root sono risposte di primo livello; gli eventi il cui `reply` punta a un'altra risposta sono risposte annidate.

## Rilasci {#releases}

**Zeus v0.12.0** - Costruendo sul [supporto pagamenti paralleli NWC della settimana scorsa](/it/newsletters/2025-12-17-newsletter/#zeus), la [release principale](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0) del wallet Lightning rilascia un servizio completo Nostr Wallet Connect [NIP-47](/it/topics/nip-47/) con supporto relay personalizzato e tracciamento budget. Una [correzione ricarica budget](https://github.com/ZeusLN/zeus/pull/3455) assicura che le connessioni usino i limiti correnti. [Copia indirizzo Lightning](https://github.com/ZeusLN/zeus/pull/3460) non include piu' il prefisso `lightning:`, correggendo problemi di incolla nei campi profilo Nostr.

**Amber v4.0.6** - Il signer Android [NIP-55](/it/topics/nip-55/) [aggiunge caching delle prestazioni](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6) alle operazioni di firma e migliora la gestione errori durante la decifratura di contenuti malformati. L'affidabilita' della connessione e' migliorata con logica di retry per eventi di connessione relay, e diverse correzioni crash affrontano casi limite intorno a URI `nostrconnect://` invalidi e interazioni con schermate di permesso.

**nak v0.17.3** - L'[ultima release](https://github.com/fiatjaf/nak/releases/tag/v0.17.3) dello strumento Nostr a riga di comando restringe le build LMDB a Linux, correggendo problemi di compilazione cross-platform.

**Aegis v0.3.4** - Il signer Nostr cross-platform [aggiunge supporto](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4) per lo schema URI `nostrsigner:` definito in [NIP-55](/it/topics/nip-55/), abbinandosi al flusso di connessione di Amber. I dati relay locali possono ora essere importati ed esportati per backup, e la release include correzioni bug per errori socket relay e miglioramenti UI all'interfaccia relay locale.

## Modifiche notevoli a codice e documentazione {#notable-code-and-documentation-changes}

*Queste sono pull request aperte e lavori in fase iniziale, perfetti per ricevere feedback prima del merge. Se qualcosa cattura la vostra attenzione, considerate di revisionare o commentare!*

### Damus (iOS) {#damus-ios}

[Persistenza lista mute](https://github.com/damus-io/damus/pull/3469) corregge un problema dove le liste mute venivano cancellate all'avvio a freddo. La correzione aggiunge guard per prevenire sovrascritture accidentali durante l'inizializzazione dell'app. [Timing stream profilo](https://github.com/damus-io/damus/pull/3457) elimina un ritardo di ~1 secondo prima che i profili in cache apparissero. Precedentemente, le viste attendevano che i task di sottoscrizione ripartissero; ora `streamProfile()` produce immediatamente dati in cache da NostrDB, rimuovendo la finestra dove pubkey abbreviate e immagini placeholder venivano mostrate.

### White Noise (Messaggistica Crittografata) {#white-noise}

[Streaming messaggi in tempo reale](https://github.com/marmot-protocol/whitenoise/pull/919) sostituisce il precedente meccanismo di polling con un'architettura basata su stream. Il nuovo `ChatStreamNotifier` consuma direttamente lo stream di messaggi dell'SDK Rust, mantenendo l'ordine cronologico e gestendo efficientemente gli aggiornamenti incrementali. I test hanno mostrato miglioramenti significativi nella reattivita'. Una [API lista chat](https://github.com/marmot-protocol/whitenoise/pull/921) aggiunge `get_chat_list` per recuperare sommari delle conversazioni, e una [correzione ordinamento stabile](https://github.com/marmot-protocol/whitenoise/pull/905) previene loop di riordinamento messaggi usando `createdAt` con ID messaggio come spareggio.

### NDK (Libreria) {#ndk}

Due pull request hanno fornito miglioramenti drammatici delle prestazioni della cache. [PR #371](https://github.com/nostr-dev-kit/ndk/pull/371) ha corretto un bug dove gli eventi letti dalla cache SQLite venivano immediatamente riscritti, causando 100% di scritture duplicate all'avvio dell'app. La correzione aggiunge un guard `fromCache` e implementa controllo duplicati O(1) tramite un Set in memoria. Per set di risultati piccoli (<100 eventi), il trasferimento JSON diretto sostituisce l'overhead della codifica binaria. [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372) ha rimosso chiamate `seenEvent` non necessarie per eventi in cache. Il lookup cache LRU costava 0.24-0.64ms per evento; per 5,700 eventi in cache, questo aggiungeva ~1.4 secondi di overhead. Risultato: le query cache sono scese da ~3,690ms a ~22ms (162x piu' veloci).

### rust-nostr (Libreria) {#rust-nostr}

[Supporto REQ multi-filtro](https://github.com/rust-nostr/nostr/pull/1176) e' stato ripristinato dopo essere stato rimosso in un refactor precedente. L'SDK accetta di nuovo `Vec<Filter>` per richieste di sottoscrizione, abilitando query efficienti che combinano piu' condizioni filtro con logica OR. [Provenienza relay](https://github.com/rust-nostr/nostr/pull/1156) e' stata aggiunta ai metodi `stream_events*`, cosi' ogni evento in streaming ora include il `RelayUrl` da cui proviene e un `Result` che indica successo o fallimento, utile per tracciare l'affidabilita' dei relay e debug di problemi di connessione. Una [correzione sicurezza](https://github.com/rust-nostr/nostr/pull/1179) ha rimosso la dipendenza `url-fork` seguendo RUSTSEC-2024-0421, eliminando una vulnerabilita' nota.

### Applesauce (Libreria) {#applesauce}

La libreria TypeScript che alimenta [noStrudel](https://github.com/hzrd149/nostrudel) ha visto sviluppi significativi questa settimana. Nuovi modelli includono un [sistema di reazioni](https://github.com/hzrd149/applesauce) e casting gruppi utente. La funzionalita' wallet si e' espansa con supporto NIP-60, scheda invio e strumenti di recupero token migliorati. Una nuova proprieta' `user.directMessageRelays$` espone la configurazione relay per DM. Tutte le azioni sono state refactoratе per usare interfacce async (rimuovendo generatori async), e correzioni bug hanno affrontato il ripristino contenuto crittografato e casi limite filtri eventi basati sul tempo.

### Tenex (Agenti AI) {#tenex}

Il [sistema di coordinamento multi-agente](https://github.com/tenex-chat/tenex) costruito su Nostr ha introdotto l'architettura RAL (Request-Action-Lifecycle) in [cinque PR unite](https://github.com/pablof7z/tenex/pull/38). RAL consente agli agenti di mettersi in pausa quando delegano task e riprendere quando arrivano i risultati, con persistenza dello stato a scope conversazione. Gli strumenti di delega (`delegate`, `ask`, `delegate_followup`, `delegate_external`) ora pubblicano eventi Nostr e restituiscono segnali di stop invece di bloccarsi. Il refactor include migrazione AI SDK v6, infrastruttura testing VCR per registrazione deterministica interazioni LLM, e supporto immagini multimodali.

---

Questo e' tutto per questa settimana. State costruendo qualcosa? Avete notizie da condividere? Volete che copriamo il vostro progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattateci via DM NIP-17</a> o trovateci su Nostr.

