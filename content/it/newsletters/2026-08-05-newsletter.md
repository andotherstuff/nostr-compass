---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
translationOf: /en/newsletters/2026-08-05-newsletter.md
translationDate: 2026-08-06
draft: false
type: newsletters
description: "Sandstr offre tour con dati finti dei client Nostr, nostr-mill aggiunge il consenso alla firma per evento, e nostrord espande i gruppi ospitati su relay. Gli approfondimenti coprono la ricerca assistita dai relay e i highlight portatili."
---

Bentornati su [Nostr Compass](https://github.com/andotherstuff/nostr-compass), la vostra guida settimanale a Nostr.

**Questa settimana:** [Sandstr](https://sandstr.app/) permette ai nuovi arrivati di esplorare client Nostr simulati senza creare chiavi né installare un'app. [nostr-mill](https://github.com/0ceanSlim/nostr-mill) aggiunge il consenso del firmatario per evento e il recupero delle chiavi tra client, mentre [nostrord](https://github.com/nostrord/nostrord) espande i gruppi ospitati su relay, i firmatari, la moderazione, i caricamenti e i highlight. Il lavoro sul protocollo copre i formati di eventi Nostr, le connessioni ai wallet, la scoperta dei relay, i napplets, Marmot e Concord; gli approfondimenti spiegano la ricerca assistita dai relay e i highlight portatili.

## Storie principali

### nostr-mill 1.6.0 porta il consenso alla firma e il recupero dell'account nel browser

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) è un selettore di account e firmatario integrabile nel browser. Ora chiede il consenso per kind di evento e mostra contenuto e tag decodificati prima della firma, con concessioni a tempo limitato e un gestore dei permessi. La release corregge anche un bug della prima sessione che permetteva alle categorie configurate per chiedere ogni volta di firmare senza chiedere. Il suo onboarding opzionale con Google può importare un `nsec` esistente, memorizza la chiave cifrata nella cartella dei dati dell'app Drive dell'utente, supporta più identità e può esportare un `ncryptsec` in formato [NIP-49](/it/topics/nip-49/) (formato di chiave privata cifrata).

Il [backup sperimentale su relay](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) deriva una frase di recupero robusta con scrypt e HKDF, avvolge la chiave come `ncryptsec`, verifica gli eventi recuperati e richiede un quorum di relay prima del recupero. Il login [NIP-55](/it/topics/nip-55/) (intent del firmatario Android) ora usa il percorso di ritorno tramite appunti di Amber, e le connessioni [NIP-46](/it/topics/nip-46/) (firma remota mediata da relay) sono silenziose per impostazione predefinita. Controlli di branding e schermate dei permessi responsive completano la release senza modificare le integrazioni esistenti, a meno che un operatore non lo scelga.

### nostrord 2.5.0 dà ai gruppi su relay identità stabili e specifiche del relay

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) è un client multipiattaforma per comunità ospitate su relay. Ora deriva un'identità [NIP-29](/it/topics/nip-29/) (gruppi gestiti da relay) sia dall'ID del gruppo sia dal relay ospitante, delimita allo stesso modo appartenenza e badge di amministratore, accetta deep link `naddr` di gruppo e sincronizza i thread dei gruppi privati tra dispositivi.

La [release](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) aggiunge anche una casella di moderazione con [NIP-56](/it/topics/nip-56/) (eventi di segnalazione), login con Amber tramite NIP-55, backoff per il rate-limit del traffico del firmatario NIP-46, rendering di [NIP-84](/it/topics/nip-84/) (highlight portatili) con nuovi tentativi per i riferimenti non risolti, e caricamenti multimediali tramite Blossom o [NIP-96](/it/topics/nip-96/) (archiviazione file HTTP). Il login con Google ora esegue il backup della chiave prima della creazione dell'account e conferma le disconnessioni. Le risposte nei thread ottengono contenuti più ricchi e la cancellazione da parte degli amministratori, mentre le correzioni al portachiavi desktop e alla tastiera mobile mantengono utilizzabili quelle funzionalità di protocollo.

### Primal Android 3.5.25 aggiorna la firma remota e il filtraggio della lista dei seguiti

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) è un client mobile Nostr con feed, ricerca e firma remota. Aggiorna il suo firmatario remoto al comportamento attuale del protocollo, aggiunge una lista di silenziati dei seguiti, apre la ricerca da Esplora, ripara automaticamente le connessioni ai relay bloccate, espone i timeout delle richieste nell'interfaccia, rifiuta le voci non valide della lista dei seguiti e aggiorna gli URL dei relay di riserva. Il prefetching dei feed, il minor uso di memoria e un limite di cache di 100 MB riducono il costo di mantenere aggiornati quei feed. Le note con una sola immagine ora usano tutta la larghezza del contenuto, e i controlli del profilo e il precaricamento dei media ricevono correzioni minori di interazione e ordinamento.

### Nostur 1.30.2 espande le risposte private e i media nei messaggi diretti

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) è un client Nostr per piattaforme Apple. Espone sempre l'azione di risposta privata, aggiunge cache di media per conversazione con limiti e controlli di cancellazione, migliora il completamento automatico di nomi e tag nei post e nelle chat, mostra i messaggi referenziati nella chat dal vivo e include il titolo della stanza nelle notifiche di chat. Le correzioni alla paginazione del feed e alle risposte annidate affrontano regressioni nel recupero e nel rendering delle conversazioni.

### Chama 5.7.0 aggiunge i registri degli arbitri e il recupero degli scambi dalla cache

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) coordina scambi tra pari e arbitrato tramite catene di eventi Nostr firmati. Mostra l'importo bloccato di un arbitro, l'anzianità della sua cauzione e il suo outpoint di finanziamento; registra quando un sostituto ha rimpiazzato un arbitro assente; e definisce le attestazioni di colpa dormienti di kind `38136` che richiedono le firme di entrambi i principali. Una riparazione esplicita riprova le cronologie incomplete dei relay contro la cache durevole del dispositivo e ripubblica gli eventi recuperati, mentre le pubblicazioni fallite vengono accodate per la connessione successiva. La release impedisce inoltre pagamenti duplicati tra dispositivi del premio dell'arbitro trattando l'evento di kind `38113` dell'autore come la registrazione del pagamento.

### Auditable Voting 0.1.165 ripristina la consegna delle schede delegate

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) conduce votazioni verificabili separando le credenziali dell'elettore dal contenuto della scheda. Ripristina l'emissione delegata di schede cieche tramite consegna autenticata delle deleghe e recupero dei DM di controllo, mantiene i messaggi diretti delle credenziali cieche sui relay privati configurati e aggiorna il proxy di audit alla versione 0.1.52.

### Sandstr permette ai nuovi arrivati di provare i client Nostr con dati finti

[Sandstr](https://sandstr.app/) offre simulazioni interattive nel browser dei client Nostr così che un nuovo arrivato possa confrontare le loro interfacce prima di installarne uno o creare una coppia di chiavi. Il suo lancio del 3 agosto include riproduzioni verificate sul riferimento di Damus, Amethyst, Primal, Snort, YakiHonne, Coracle e Wisp, oltre ad anteprime iniziali chiaramente etichettate di Gossip, Keychat e Olas. Tutto funziona localmente su dati finti, quindi le simulazioni non generano chiavi né si connettono ai relay. Ogni simulazione rimanda al sito web e al repository del codice del client reale, rendendo Sandstr uno strumento di onboarding e confronto delle interfacce piuttosto che un altro client Nostr. Mostra come si presentano feed, profili, thread, messaggi diretti, ricerca, zap e controlli dei relay senza chiedere a un utente alle prime armi di prendere in anticipo una decisione di identità o sicurezza.


### mineracks signer abbina un'estensione del browser a un bunker desktop

[mineracks signer](https://github.com/mineracks/mineracks-signer) offre due superfici di firma dallo stesso progetto. La sua estensione del browser implementa [NIP-07](/it/topics/nip-07/) così che le applicazioni web possano richiedere firme senza ricevere la chiave privata, mentre l'applicazione desktop espone un firmatario remoto [NIP-46](/it/topics/nip-46/) per i client che comunicano tramite relay.

La [release desktop 0.1.0](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0) del progetto memorizza il materiale delle chiavi con la codifica a chiave cifrata di NIP-49 e mantiene la chiave decifrata all'interno del processo Rust anziché passarla all'interfaccia. Ogni richiesta mostra l'applicazione chiamante e l'azione richiesta, mentre l'approvazione automatica per applicazione è opzionale e revocabile. La prima build desktop supporta Apple Silicon ma non i Mac Intel.

## Release

### Jumble 26.8.1 aggiunge controlli di proof-of-work e anteprime dei commenti

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) è un client Nostr web e desktop. Ricorda la difficoltà del proof-of-work per la pubblicazione, mostra badge di lavoro verificato, mostra in anteprima i commenti collegati sopra il contenuto esterno, salva le immagini dal visualizzatore a schermo intero ed espande le biografie lunghe del profilo su richiesta. Le notifiche delle reazioni ora scartano i kind di evento non supportati, gli avvisi di disconnessione dai relay sono meno invadenti, i relay predefiniti sono stati aggiornati ed è stato corretto un conflitto di riproduzione automatica dei media.

### nostr-calendar 2.1.0 ripristina il binding del firmatario per i moduli privati

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) pubblica calendari, eventi e risposte ai moduli come dati Nostr. Lega gli invii dei moduli privati al firmatario attivo, salva gli eventi duplicati intenzionali sui relay, corregge il recupero dai relay, analizza le date del calendario nell'ora locale e aggiunge notifiche dell'app oltre a un client iOS. La correzione del firmatario impedisce a un'identità obsoleta di produrre una risposta cifrata inutilizzabile.

### Manent 2.0.0 aggiunge tag e ricerca per le note salvate

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) è un archivio personale per note Nostr firmate. Aggiunge tag locali e ricerca, permettendo al lettore di organizzare e recuperare gli eventi salvati senza modificarne il contenuto firmato.

### nosvelte 0.6.1 chiude le sottoscrizioni vuote dopo l'EOSE

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) fornisce componenti e hook reattivi di Svelte per i dati dei relay. Le ricerche vuote ora si concludono all'End of Stored Events, la cancellazione chiude il `REQ` sottostante, i nuovi tentativi cancellano gli errori obsoleti e gli hook di lista restituiscono il loro valore vuoto documentato. Riconosce inoltre gli eventi indirizzabili indipendentemente da dove appaia il loro tag `d`, sostituisce metadati e articoli superati, deduplica le reazioni per ID evento e conserva ogni evento del primo batch di un relay.

## Modifiche non rilasciate

### NMP lega l'ammissione al relay alle dichiarazioni e amplia le query di gruppo

[NMP](https://github.com/pablof7z/nmp) è un toolkit TypeScript per costruire applicazioni Nostr e interfacce di gruppi supportati da relay. La [PR #1254](https://github.com/pablof7z/nmp/pull/1254) fa sì che l'ammissione al relay segua il proprietario della dichiarazione che la autorizza, mantenendo la decisione sui permessi legata allo stato Nostr firmato. La [PR #1255](https://github.com/pablof7z/nmp/pull/1255) generalizza le query dei gruppi gestiti da relay di [NIP-29](/it/topics/nip-29/) invece di assumere un'unica forma di ricerca ristretta. Entrambe le modifiche sono state unite ma non sono ancora apparse in una release taggata.

### Mosaico deriva l'identità del gruppo gestito dai record del relay

[Mosaico](https://github.com/pablof7z/mosaico) è un client Nostr per esplorare e amministrare comunità gestite da relay. La [PR #758](https://github.com/pablof7z/mosaico/pull/758) deriva l'identità di un gruppo gestito dal relay che ospita i suoi record autorevoli. La [PR #757](https://github.com/pablof7z/mosaico/pull/757) osserva il record pubblicato del gruppo nel risolvere lo stato di amministrazione. Questo mantiene distinti due gruppi con nomi simili su relay diversi e offre ai client una fonte supportata dal relay per i loro metadati di gestione.

### Divine isola i relay lenti durante le query multi-relay

[Divine](https://github.com/divinevideo/divine-mobile) è un client mobile di video brevi che pubblica e recupera video tramite Nostr. La [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) dà a ogni query di relay il proprio timeout invece di lasciare che una connessione bloccata consumi il budget di tempo di un'intera richiesta. I risultati dei relay che rispondono possono quindi arrivare mentre l'endpoint lento viene abbandonato indipendentemente. La modifica migliora il recupero senza trattare un relay come autorevole per il risultato combinato.

### rust-nostr rafforza crittografia, hash e riconciliazione

[rust-nostr](https://github.com/rust-nostr/nostr) è una libreria e un toolkit Rust per client, relay e implementazioni del protocollo Nostr. La [PR #1421](https://github.com/rust-nostr/nostr/pull/1421) riduce le allocazioni nel suo percorso di crittografia versionata [NIP-44](/it/topics/nip-44/), mentre la [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) introduce hash tipizzati che rendono più difficile mescolare accidentalmente valori di digest incompatibili. Il [commit 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) impedisce a un messaggio malformato di riconciliazione degli insiemi Negentropy di [NIP-77](/it/topics/nip-77/) di disconnettere il relay locale. Il lavoro unito rafforza sia la gestione dei payload cifrati sia il comportamento di fallimento della riconciliazione prima della prossima release.

### Zeus serializza i pagamenti NWC prima di addebitare i budget di spesa

[Zeus](https://github.com/ZeusLN/zeus) è un wallet mobile Bitcoin e Lightning che può esporre operazioni del wallet tramite Nostr Wallet Connect. La [PR #4305](https://github.com/ZeusLN/zeus/pull/4305) conta i pagamenti in sospeso contro un budget [NIP-47](/it/topics/nip-47/) Nostr Wallet Connect invece di attendere il regolamento. La [PR #4303](https://github.com/ZeusLN/zeus/pull/4303) serializza la gestione dei pagamenti così che le richieste concorrenti non possano correre attraverso lo stesso limite di autorizzazione. La coppia unita chiude una lacuna nell'applicazione dei budget sulla superficie di controllo Nostr del wallet.

### Nostr Components condivide un unico tentativo di connessione al relay

[Nostr Components](https://github.com/saiy2k/nostr-components) è una libreria riutilizzabile di componenti web per aggiungere dati e interazioni Nostr alle applicazioni. La [PR #105](https://github.com/saiy2k/nostr-components/pull/105) permette ai componenti montati contemporaneamente di condividere un tentativo di connessione al relay in corso. Ogni consumatore riceve comunque la connessione risultante, ma i montaggi concorrenti non aprono più socket duplicati mentre il primo handshake è in attesa. La modifica riduce il carico evitabile sui relay nelle applicazioni assemblate da diversi componenti indipendenti.

## Aggiornamenti NIP e lavoro di specifica del protocollo

### Formati di eventi Nostr e scoperta

La [PR NIP #2430](https://github.com/nostr-protocol/nips/pull/2430) propone pacchetti di adesivi come definizioni indirizzabili di kind `30031` e i pacchetti installati da un utente come kind sostituibile `10031`. Ogni tag di adesivo porta uno shortcode, un hash SHA-256 e un tipo MIME; l'immagine resta su un server [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md) (archiviazione blob Blossom). La bozza aperta standardizza così identità e installazione dei pacchetti senza collocare i byte dell'immagine negli eventi.

La [PR NIP #2429](https://github.com/nostr-protocol/nips/pull/2429) propone documenti Gopher indirizzabili di kind `31436`. Ogni evento contiene un nodo di testo o menu UTF-8, e i nodi firmati sotto una stessa pubkey formano un gopherhole che qualsiasi bridge RFC 1436 supportato da relay può servire. La proposta aperta usa il normale storage degli eventi indirizzabili invece di legare la pubblicazione a un unico hostname Gopher.

La [PR NIP #2428](https://github.com/nostr-protocol/nips/pull/2428) propone gruppi privati con biglietti per epoca. Un gruppo ruota le credenziali di appartenenza tra epoche, e i client presentano il biglietto dell'epoca corrente per partecipare. La bozza punta alla chat privata senza chiedere a un relay di trattare un bearer token permanente come appartenenza a vita.

La [PR NIP #2425](https://github.com/nostr-protocol/nips/pull/2425), trattata come proposta la scorsa settimana, ha ora unito un chiarimento sugli URI in [NIP-B0](/it/topics/nip-b0/) (segnalibri web indirizzabili). Distingue i prefissi HTTPS omessi dagli schemi URI espliciti quando un segnalibro memorizza la sua destinazione nel tag `d`, impedendo ai client di ricostruire una destinazione ambigua.

### Pagamenti e connessioni ai wallet

La [PR NIP #2419](https://github.com/nostr-protocol/nips/pull/2419), trattata come proposta nel numero del 22 luglio, ha ora unito un nucleo [NIP-47](/it/topics/nip-47/) (Nostr Wallet Connect) ridotto. Gli URI di connessione, il trasporto cifrato su relay, la scoperta delle capacità, la negoziazione della crittografia e i metodi comuni restano nel NIP; notifiche, fatture in sospeso, keysend, cronologia delle transazioni, metadati e accoppiamento tramite deep link passano a un repository di estensioni dedicato. Le connessioni esistenti restano compatibili mentre i wallet possono implementare i contratti opzionali in modo indipendente.

La [PR NWC #2](https://github.com/nostr-wallet-connect/nwc/pull/2), trattata come proposta la scorsa settimana, ha ora unito i metodi di pagamento BIP-321 in quel repository di estensioni. BIP-321 fornisce un URI di pagamento Bitcoin comune che può portare diversi rail, così che i chiamanti NWC possano richiedere o inviare un pagamento senza aggiungere un nuovo RPC centrale per ogni tipo di istruzione sottostante.

### Capacità dell'host dei napplets

La [PR NAP #95](https://github.com/napplet/naps/pull/95) propone la scoperta del catalogo per applicazioni in sandbox distribuite via Nostr. Un napplet chiede al suo host quali applicazioni e capacità sono disponibili, e l'host restituisce metadati filtrati per policy invece di esporre tutto il suo ambiente locale. Il contratto supporta le decisioni di lancio senza concedere autorità di esecuzione durante la scoperta.

La [PR NAP #33](https://github.com/napplet/naps/pull/33) propone caricamenti di file e blob mediati dalla shell. Un napplet fornisce byte e intenzione; l'host seleziona un rail NIP-96 o Blossom, firma l'autorizzazione, riporta i progressi e restituisce URL, hash, dati MIME e tag [NIP-94](/it/topics/nip-94/) (metadati di file) pronti da allegare. Credenziali di storage e autorità HTTP non entrano mai nel napplet.

### Gruppi cifrati Marmot

La [PR Marmot #410](https://github.com/marmot-protocol/marmot/pull/410) ha unito regole di convergenza e di input differito. I client distinguono un oggetto a cui manca una dipendenza dall'epoca corrente da un input obsoleto o non valido, lo mantengono idoneo per un nuovo recupero dopo un rifiuto di risorse e riprovano quando un altro commit cambia il contesto di decrittazione. Un commitment di stato con separazione di dominio offre ai test di conformità un oracolo di convergenza condiviso senza aggiungere un campo wire di produzione.

### Piani comunitari di Concord

La [PR Concord #14](https://github.com/concord-protocol/concord/pull/14) ha unito i messaggi a scomparsa di CORD-08. Un valore di metadati della comunità fissa la durata; i rumors di chat e gli involucri cifrati portano un tag [NIP-40](/it/topics/nip-40/) (scadenza degli eventi), mentre gli eventi di cancellazione e l'avviso del timer di kind `1740` ne sono esenti. Il timer firmato viaggia con lo stato della comunità, anche se la cancellazione da parte del relay resta una richiesta di conservazione e non una garanzia crittografica di eliminazione.

La [PR Concord #13](https://github.com/concord-protocol/concord/pull/13) ha unito in CORD-04 il pinning resistente alle rotazioni. Ogni canale ha una lista di pin a sostituzione completa sul piano di controllo; le voci portano il sigillo firmato originale più le chiavi di espansione NIP-44 per messaggio, permettendo a un nuovo membro di verificare autore e testo in chiaro senza ricevere una vecchia chiave d'epoca. Le liste private possono restare sigillate a un'epoca del canale, dei limiti vincolano la dimensione della lista, e le cancellazioni dell'autore rimuovono i pin senza biforcare la catena del piano di controllo.

## Approfondimento NIP

### Capacità di ricerca (NIP-50)

[NIP-50](/it/topics/nip-50/), definito nella [specifica principale](https://github.com/nostr-protocol/nips/blob/master/50.md), aggiunge un filtro di ricerca opzionale per i relay. I filtri Nostr ordinari funzionano quando un client conosce già un autore, un kind di evento, un identificatore o un tag; NIP-50 affronta la scoperta quando l'input è una query umana come `best nostr apps`.

Il [formato wire di NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field) aggiunge una stringa `search` a un filtro normale all'interno di un messaggio `REQ`. Una richiesta può combinare quel campo con `kinds`, `authors`, `ids`, filtri di tag e `limit`, e un REQ può portare diversi filtri indipendenti. Un relay che lo supporta dovrebbe cercare principalmente nel `content` dell'evento, può usare altri campi quando il kind di evento lo rende utile e dovrebbe ordinare secondo il proprio punteggio di rilevanza prima di applicare il `limit`. Quest'ordine differisce dal consueto flusso di eventi dal più recente al più vecchio.

La stringa di query può includere le [estensioni `key:value`](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions) della specifica. Essa nomina `include:spam`, `domain:`, `language:`, `sentiment:` e `nsfw:`; un relay dovrebbe ignorare le estensioni che non implementa. I client scoprono il supporto dichiarato tramite il campo `supported_nips` di [NIP-11](/it/topics/nip-11/) del relay, ma possono comunque inviare il filtro altrove se sono pronti a scartare risposte non pertinenti.

La [specifica NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) deliberatamente non standardizza tokenizzazione, stemming, ranking, rilevamento della lingua, analisi del sentiment o classificazione dello spam. Due relay conformi possono restituire eventi e ordinamenti diversi per la stessa query. Questo rende il relay un fornitore di indici e ranking, non una fonte di verità. La specifica raccomanda di interrogare diversi relay che la supportano, di verificare se gli eventi restituiti soddisfano il caso d'uso del client e di abbandonare i relay i cui risultati hanno scarsa precisione.

Questo differisce dal [filtraggio esatto di NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Un filtro `authors` o `#t` ha una semantica di corrispondenza deterministica che un client può verificare direttamente, mentre una corrispondenza di ricerca può dipendere da un indice e da un punteggio opaco. NIP-50 mantiene l'involucro firmato dell'evento e il trasporto via relay di NIP-01, ma accetta variazione nel recall e nell'ordinamento per rendere possibile il recupero aperto.

L'evento qui sotto è un risultato di ricerca illustrativo che usa i [sette campi dell'evento di NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). I valori esadecimali ripetuti sono segnaposto e non una firma valida.

```json
{
  "id": "2943d6b43bcbf0ee4a8b4cac912111be0309607b8bb435ae40529989bea7f6c5",
  "pubkey": "3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d",
  "created_at": 1785771175,
  "kind": 1,
  "tags": [],
  "content": "I've been working on a customizable client (mostly relay feeds, but a ton of other things and subtle details too). It's called Hallway for reasons I don't remember and it's a fork of Fevela which is a fork of Jumble, but very rewritten for speed and simplicity...",
  "sig": "5b058b89dab9bd09d81bdc10eff95536125b87fbcbbc97f08d835c1272b2a3190cc3d340e42f54acb0d7e0e4b00355ab91292d0305c84a2d73b538319c0da12c"
}
```

I client attuali usano lo stesso filtro in diverse superfici di scoperta. [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) invia ricerche NIP-50 a relay di ricerca dedicati, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) cerca eventi tramite il suo pool di relay, e [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) coordina ricerche supportate da relay per la lettura di formato lungo. Il loro diverso trattamento dei risultati riflette la libertà che NIP-50 lascia a relay e client.

### Highlight (NIP-84)

[NIP-84](/it/topics/nip-84/), definito dalla sua [specifica principale](https://github.com/nostr-protocol/nips/blob/master/84.md), assegna il kind `9802` a un highlight. Trasforma un passaggio selezionato, o un riferimento a un media non testuale, in un evento firmato che può muoversi tra client di lettura, sociali e di annotazione.

Il [`content` dell'evento](https://github.com/nostr-protocol/nips/blob/master/84.md#format) contiene il testo selezionato e può essere vuoto quando la fonte è audio, video o un altro medium non testuale. Un highlight punta a una fonte Nostr con un tag `a` per un evento indirizzabile o un tag `e` per un evento ordinario; un tag `r` identifica un URL web. I client che producono URL dovrebbero rimuovere i parametri di tracciamento e altri parametri di query non utili prima della pubblicazione, così che varianti cosmetiche dell'URL non frammentino i riferimenti alla stessa fonte.

I [tag `p`](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution) opzionali attribuiscono la fonte a una o più pubkey Nostr. Il loro quarto valore può identificare un ruolo come `author` o `editor`, e un tag `context` può conservare il testo circostante quando la selezione da sola risulterebbe poco chiara. Un highlight con citazione aggiunge un tag `comment` invece di pubblicare una seconda nota di kind `1`: il tag `r` della fonte riceve il marcatore `source`, mentre le pubkey o gli URL menzionati nel commento portano `mention`, permettendo ai renderer di distinguere l'attribuzione dalla risposta dell'utente.

La [definizione del kind `9802`](https://github.com/nostr-protocol/nips/blob/master/84.md) rende un highlight un evento regolare anziché sostituibile. Ripetere o correggere una selezione crea un altro evento firmato, e rimuoverne uno si affida al normale flusso di richiesta di cancellazione e alla politica di conservazione del relay. La specifica non definisce offset di byte, selettori o uno snapshot canonico del documento, quindi un client potrebbe non riuscire a rintracciare un passaggio dopo che la sua fonte web è cambiata. Gli highlight pubblici rivelano inoltre interessi di lettura; l'annotazione privata richiede un design separato di crittografia e condivisione.

NIP-84 differisce da un [evento di formato lungo NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md), che pubblica un intero articolo come kind `30023`; un highlight cita o punta a materiale che può restare altrove. Differisce anche da un [insieme di segnalibri NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md), che memorizza una collezione sostituibile di riferimenti. NIP-84 rende ogni selezione indipendentemente firmata, attribuibile, scopribile e discutibile.

Questo highlight illustrativo contiene i [sette campi dell'evento di NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Il suo identificatore e la sua firma sono segnaposto.

```json
{
  "id": "0d57c07cfdfe8ec00711e2af88a666b61fc35c167b90b02dfb5db7ffba7b794a",
  "pubkey": "07367baec8e73c076b14e47fba3b0d5c014d559d7986a7172a79a8a64419d7c2",
  "created_at": 1785797755,
  "kind": 9802,
  "tags": [
    ["context", "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will be able to derive your nsec, read all your encrypted data and sign events as you."],
    ["alt", "This is a highlight created in https://primal.net iOS application"],
    ["a", "30023:1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139:nostr-quantum-preparation"],
    ["p", "1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139", "", "mention"]
  ],
  "content": "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will b",
  "sig": "219f3c1e572d1a087d667dc0d3a5443c77c0db3a5d42ce4e630604901ac63d2c879a86269d81e220bb77fd48b1579adafc333075e53c6eb0a108791fdd4a1622"
}
```

Il formato attraversa già i confini tra client. [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) ha aggiunto il rendering di NIP-84 questa settimana, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) renderizza gli eventi di highlight nel suo client di formato lungo, e [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) li pubblica dal contenuto selezionato. Queste implementazioni coprono lettura, creazione e rendering sociale senza richiedere che un unico servizio possieda l'annotazione.

---

Invia un DM NIP-17 per condividere un progetto o una notizia tramite il [progetto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
