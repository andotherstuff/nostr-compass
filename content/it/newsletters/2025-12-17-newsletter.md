---
title: 'Nostr Compass #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
---

Benvenuti a Nostr Compass, una newsletter settimanale dedicata all'ecosistema del protocollo Nostr. La nostra missione e' mantenere sviluppatori, operatori di relay e costruttori informati sugli sviluppi importanti in tutta la rete. Documentiamo l'evoluzione del protocollo con precisione tecnica, neutralita' e profondita', coprendo tutto dalle proposte NIP ai rilasci dei client fino alle migliori pratiche di implementazione.

Nostr Compass e' ispirato da [Bitcoin Optech](https://bitcoinops.org/), il cui lavoro dedicato nel corso degli anni per far progredire la conoscenza tecnica di Bitcoin ha stabilito lo standard per le newsletter focalizzate sul protocollo. Siamo grati per il loro esempio e speriamo di portare lo stesso rigore all'ecosistema Nostr.

Questo numero inaugurale stabilisce il nostro formato settimanale. Ogni mercoledi' vi porteremo aggiornamenti NIP, note di rilascio, punti salienti dello sviluppo e guide tecniche. Che stiate costruendo un client, gestendo un relay o contribuendo al protocollo, Nostr Compass mira ad essere la vostra fonte affidabile per cio' che sta accadendo nell'ecosistema.

## Cos'e' Nostr?

*Poiche' questo e' il nostro primo numero, iniziamo con una introduzione su come funziona Nostr. I lettori abituali possono [passare avanti](#notizie--aggiornamenti).*

Nostr (Notes and Other Stuff Transmitted by Relays) e' un protocollo decentralizzato per social networking e messaggistica. A differenza delle piattaforme tradizionali, Nostr non ha server centrale, nessuna azienda che lo controlla e nessun singolo punto di fallimento. Gli utenti possiedono la propria identita' attraverso coppie di chiavi crittografiche, e il contenuto fluisce attraverso server relay indipendenti che chiunque puo' gestire.

**Come funziona:** Gli utenti generano una coppia di chiavi (una chiave privata chiamata nsec e una chiave pubblica chiamata npub). La chiave privata firma i messaggi chiamati "eventi", e la chiave pubblica serve come vostra identita'. Gli eventi vengono inviati ai relay, che li memorizzano e li inoltrano ad altri utenti. Poiche' voi controllate le vostre chiavi, potete passare da un client all'altro o da un relay all'altro senza perdere la vostra identita' o i vostri follower.

**Perche' e' importante:** Nostr fornisce resistenza alla censura attraverso la diversita' dei relay (se un relay vi blocca, altri possono comunque servire il vostro contenuto), portabilita' (la vostra identita' funziona su qualsiasi app Nostr) e interoperabilita' (tutti i client Nostr parlano lo stesso protocollo). Non c'e' nessun algoritmo che decide cosa vedete, niente pubblicita' e nessuna raccolta di dati.

**L'ecosistema oggi:** Nostr supporta microblogging (come Twitter/X), contenuti di lunga forma (come Medium), messaggi diretti, marketplace, livestreaming e altro. I client includono Damus (iOS), Amethyst (Android), Primal, Coracle e dozzine di altri. L'integrazione con Lightning Network consente pagamenti istantanei attraverso gli "zap". Il protocollo continua ad evolversi attraverso i NIP (Nostr Implementation Possibilities), specifiche guidate dalla comunita' che estendono le funzionalita'.

## Notizie {#news}

**NIP-BE Unito: Supporto Bluetooth Low Energy** - Una nuova significativa capacita' [e' arrivata nel protocollo](https://github.com/nostr-protocol/nips/pull/1979). [NIP-BE](/it/topics/nip-be/) specifica come le applicazioni Nostr possono comunicare e sincronizzarsi tramite Bluetooth Low Energy. Questo consente alle app di funzionare offline e sincronizzare dati tra dispositivi vicini senza connettivita' internet. La specifica adatta i pattern dei relay WebSocket ai vincoli del BLE, usando compressione DEFLATE e messaggistica a blocchi per gestire le piccole dimensioni MTU del BLE (20-256 byte). I dispositivi negoziano i ruoli in base al confronto UUID, con l'UUID piu' alto che diventa il server GATT.

**MIP-05: Notifiche Push che Preservano la Privacy** - Il [Protocollo Marmot](/it/topics/marmot/) ha pubblicato [MIP-05](/it/topics/mip-05/) ([specifica](https://github.com/marmot-protocol/mips/blob/main/mip-05.md)), una specifica per notifiche push che mantengono la privacy. I sistemi push tradizionali richiedono che i server conoscano i token dei dispositivi e le identita' degli utenti; MIP-05 risolve questo problema crittografando i token dei dispositivi con ECDH+HKDF e ChaCha20-Poly1305, usando chiavi effimere per prevenire la correlazione. Un protocollo gossip a tre eventi (kind 447-449) sincronizza i token crittografati tra i membri del gruppo, e le notifiche usano il [NIP-59](/it/topics/nip-59/) gift wrapping con token esca per nascondere le dimensioni dei gruppi. Questo consente a WhiteNoise e altri client Marmot di consegnare notifiche tempestive senza compromettere la privacy degli utenti.

**Blossom BUD-10: Nuovo Schema URI** - Il protocollo media [Blossom](/it/topics/blossom/) sta ottenendo uno schema URI personalizzato tramite [BUD-10](/it/topics/bud-10/) ([specifica](https://github.com/hzrd149/blossom/blob/master/buds/10.md)). Il nuovo formato `blossom:<sha256>.ext` incorpora hash del file, estensione, dimensione, suggerimenti per piu' server e pubkey degli autori per la scoperta server [BUD-03](/it/topics/bud-03/). Questo rende i link blob piu' resilienti degli URL HTTP statici abilitando il fallback automatico tra server.

**Aggiornamenti Marketplace Shopstr** - Il marketplace nativo Nostr ha [implementato Nostr Wallet Connect](https://github.com/shopstr-eng/shopstr/pull/202) ([NIP-47](/it/topics/nip-47/)) per i pagamenti, [aggiunto la scadenza delle inserzioni](https://github.com/shopstr-eng/shopstr/pull/203) usando [NIP-40](/it/topics/nip-40/), e introdotto [codici sconto](https://github.com/shopstr-eng/shopstr/pull/210) per i venditori.

## Aggiornamenti NIP {#nip-updates}

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Nuovi NIP:**
- **[NIP-BE](/it/topics/nip-be/)** - Messaggistica Bluetooth Low Energy e sincronizzazione dispositivi ([#1979](https://github.com/nostr-protocol/nips/pull/1979))
- **[NIP-63](/it/topics/nip-63/)** - Standard Paywall/Contenuto Premium per gestire contenuti protetti all'interno del protocollo ([#2156](https://github.com/nostr-protocol/nips/pull/2156))

**Modifiche Significative:**
- **[NIP-24](/it/topics/nip-24/)** - Aggiunto array opzionale `languages` ai metadati utente Kind 0, permettendo agli utenti di specificare piu' lingue preferite usando tag IETF BCP 47 per migliorare la scoperta dei contenuti e il matching dei relay ([#2159](https://github.com/nostr-protocol/nips/pull/2159))
- **[NIP-69](/it/topics/nip-69/)** - Aggiunto supporto scadenza ordini per trading P2P con tag `expires_at` e `expiration` ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **[NIP-59](/it/topics/nip-59/)** - Gli eventi gift wrap possono ora essere eliminati tramite richieste NIP-09/NIP-62 ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **[NIP-51](/it/topics/nip-51/)** - Rimossi tag hashtag e URL dai segnalibri generici; gli hashtag ora usano kind 30015 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **[NIP-18](/it/topics/nip-18/)** - Migliorati i repost generici per eventi sostituibili con supporto tag `a` ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **[NIP-17](/it/topics/nip-17/)** - Formulazione raffinata e aggiunto supporto reazioni kind 7 ai DM ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **[NIP-11](/it/topics/nip-11/)** - Aggiunto campo `self` per l'identificazione della chiave pubblica del relay ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## Approfondimento NIP: NIP-01 e NIP-19 {#nip-deep-dive-nip-01-and-nip-19}

Per questo numero inaugurale, copriamo due NIP fondamentali che ogni sviluppatore Nostr dovrebbe comprendere. Consultate le nostre pagine tematiche per [NIP-01](/it/topics/nip-01/) e [NIP-19](/it/topics/nip-19/).

### NIP-01: Protocollo Base

[NIP-01](/it/topics/nip-01/) definisce il protocollo core. Tutto in Nostr si basa su questa specifica.

**Eventi** sono l'unico tipo di oggetto. Ogni evento contiene:
- `id`: Hash SHA256 dell'evento serializzato (l'identificatore unico dell'evento)
- `pubkey`: La chiave pubblica del creatore (32 byte esadecimali, secp256k1)
- `created_at`: Timestamp Unix
- `kind`: Intero che categorizza il tipo di evento
- `tags`: Array di array per i metadati
- `content`: Il payload (l'interpretazione dipende dal kind)
- `sig`: Firma Schnorr che prova che la pubkey ha creato questo evento

**Kind** determinano come i relay memorizzano gli eventi:
- Eventi regolari (1, 2, 4-44, 1000-9999): Memorizzati normalmente, tutte le versioni mantenute
- Eventi sostituibili (0, 3, 10000-19999): Solo l'ultimo per pubkey viene mantenuto
- Eventi effimeri (20000-29999): Non memorizzati, solo inoltrati ai sottoscrittori
- Eventi indirizzabili (30000-39999): Ultimo per combinazione pubkey + kind + tag `d`

Kind 0 sono i metadati utente (profilo), kind 1 e' una nota di testo (il post base), kind 3 e' la lista dei seguiti.

**Kind 1: Note di Testo** sono il cuore del Nostr sociale. Un evento kind 1 e' un post breve, simile a un tweet. Il campo `content` contiene il testo del messaggio (testo semplice, anche se i client spesso renderizzano markdown). I tag abilitano risposte, menzioni e riferimenti:

```json
{
  "id": "<32-byte-hex>",
  "pubkey": "<32-byte-hex>",
  "created_at": 1734480000,
  "kind": 1,
  "content": "Ciao Nostr! Date un'occhiata al lavoro di @jb55 su Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ],
  "sig": "<64-byte-hex>"
}
```

Il tag `e` con marcatore "reply" indica che questa e' una risposta (vedi [NIP-10](/it/topics/nip-10/) per le convenzioni di threading). Il tag `p` menziona un utente, permettendo ai client di notificarlo e renderizzare il suo nome invece della pubkey grezza. I client recuperano l'evento kind 0 dell'utente menzionato per ottenere il suo nome visualizzato e l'immagine.

Per costruire una timeline, un client si iscrive agli eventi kind 1 dalle pubkey seguite: `["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`. Il relay restituisce le note corrispondenti, e il client le renderizza cronologicamente.

**Eventi indirizzabili** (30000-39999) funzionano come eventi sostituibili ma usano un tag `d` come identificatore aggiuntivo. Il relay mantiene solo l'ultima versione di ogni combinazione pubkey + kind + tag-d. Questo abilita articoli modificabili, elenchi di prodotti o qualsiasi caso in cui servono piu' elementi sostituibili per utente.

**Tag** sono array dove il primo elemento e' il nome del tag. I tag standard a singola lettera (`e`, `p`, `a`, `d`, `t`) sono indicizzati dai relay per query efficienti. Per esempio, `["e", "<event-id>"]` referenzia un altro evento, `["p", "<pubkey>"]` referenzia un utente.

**Comunicazione Client-Relay** usa connessioni WebSocket con array JSON come messaggi. Il primo elemento identifica il tipo di messaggio.

Da client a relay:
- `["EVENT", <event>]` - Pubblica un evento sul relay
- `["REQ", <sub-id>, <filter>, ...]` - Sottoscrivi agli eventi che corrispondono ai filtri
- `["CLOSE", <sub-id>]` - Termina una sottoscrizione

Da relay a client:
- `["EVENT", <sub-id>, <event>]` - Consegna un evento che corrisponde alla tua sottoscrizione
- `["EOSE", <sub-id>]` - "Fine degli eventi memorizzati" - il relay ha inviato tutte le corrispondenze storiche e ora inviera' solo nuovi eventi quando arrivano
- `["OK", <event-id>, <true|false>, <message>]` - Conferma se un evento e' stato accettato o rifiutato (e perche')
- `["NOTICE", <message>]` - Messaggio leggibile dal relay

Il flusso di sottoscrizione: il client invia `REQ` con un ID sottoscrizione e filtro, il relay risponde con messaggi `EVENT` corrispondenti, poi invia `EOSE` per segnalare che ha completato lo storico. Dopo `EOSE`, qualsiasi nuovo messaggio `EVENT` e' in tempo reale. Il client invia `CLOSE` quando ha finito.

**Filtri** specificano quali eventi recuperare. Un oggetto filtro puo' includere: `ids` (ID eventi), `authors` (pubkey), `kinds` (tipi di evento), `#e`/`#p`/`#t` (valori tag), `since`/`until` (timestamp), e `limit` (max risultati). Tutte le condizioni in un filtro usano logica AND. Potete includere piu' filtri in una `REQ`, e si combinano con logica OR - utile per recuperare diversi tipi di evento in una sottoscrizione.

### NIP-19: Identificatori Codificati Bech32

[NIP-19](/it/topics/nip-19/) definisce i formati user-friendly che vedete ovunque in Nostr: npub, nsec, note e altro. Questi non sono usati nel protocollo stesso (che usa esadecimale), ma sono essenziali per la condivisione e la visualizzazione.

**Perche' bech32?** Le chiavi esadecimali grezze sono soggette a errori nella copia e difficili da distinguere visivamente. La codifica bech32 aggiunge un prefisso leggibile e un checksum. Potete immediatamente distinguere un `npub` (chiave pubblica) da un `nsec` (chiave privata) o `note` (ID evento).

**Formati base** codificano valori grezzi a 32 byte:
- `npub` - Chiave pubblica (la vostra identita', sicura da condividere)
- `nsec` - Chiave privata (mantenere segreta, usata per firmare)
- `note` - ID evento (referenzia un evento specifico)

Esempio: La pubkey esadecimale `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d` diventa `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

**Identificatori condivisibili** includono metadati usando codifica TLV (Type-Length-Value):
- `nprofile` - Profilo con suggerimenti relay (aiuta i client a trovare l'utente)
- `nevent` - Evento con suggerimenti relay, pubkey autore e kind
- `naddr` - Riferimento evento indirizzabile (pubkey + kind + tag-d + relay)

Questi risolvono un problema chiave: se qualcuno condivide un ID nota, come fate a sapere quale relay ce l'ha? Un `nevent` raggruppa l'ID evento con relay suggeriti, rendendo la condivisione piu' affidabile.

**Importante:** Non usate mai formati bech32 nel protocollo stesso. Eventi, messaggi relay e risposte NIP-05 devono usare esadecimale. Bech32 e' puramente per interfacce umane: visualizzazione, copia/incolla, codici QR e URL.

## Rilasci {#releases}

**Amber v4.0.4** - L'app signer Android corregge una NullPointerException, migliora le prestazioni nella schermata attivita' e aggiunge traduzioni per alcuni tipi di evento. La precedente release v4.0.3 ha aggiunto UI rinnovata per cifratura/decifratura, esportazione/importazione account, gestione relay per account, supporto ping bunker e segnalazione crash. [Release](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - Release di correzione bug per il web client. Corretti feed topic, gestione immagini quando imgproxy e' disabilitato e linkificazione di sorgenti highlight non-link. [Release](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - Il client per comunita' stile Discord corregge problemi di scorrimento modal e stili. Release precedenti in questo ciclo hanno aggiunto badge e suoni opzionali per le notifiche, migliorato il rendering dei link, scansione codice QR per link di invito e configurazione wallet semplificata. [Release](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - Lo strumento Nostr a riga di comando ha aggiunto un nuovo comando `nip` per consultazione rapida dei NIP, piu' correzioni per gestione repository git e processamento eventi stdin. [Release](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - Release importante per l'app di messaggistica crittografata basata su MLS aggiungendo condivisione immagini tramite Blossom, sincronizzazione in background, notifiche push, localizzazione in 8 lingue e gestione membri gruppo. [Release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - Release con nuove funzionalita' che introduce liste/pacchetti di follow, nuovi filtri timeline, galleria immagini e compressione video H.265 (file piu' piccoli del 50%). Completata migrazione Kotlin Multiplatform. [Release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - Aggiornamento bot trading P2P con supporto scadenza ordini NIP-69 e risposte migliorate per la cronologia scambi. [Release](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

**Nosflare v8.9.26** - Relay Nostr serverless costruito su infrastruttura Cloudflare. Questa release fornisce un hotfix critico che risolve un bug che poteva causare fallimenti websocket, garantendo connessioni piu' stabili per utenti e applicazioni che dipendono dal relay. [Release](https://github.com/Spl0itable/nosflare/releases/tag/v8.9.26)

**Noscall v0.4.1** - App per chiamate audio e video sicure basata su Nostr. Questa release migliora l'interfaccia pop-up nella pagina Me e corregge diversi problemi noti, risultando in maggiore stabilita' e affidabilita' delle chiamate. [Release](https://github.com/sanah9/noscall/releases/tag/v0.4.1-release)

**Gitplaza v0.25.0** - Client Nostr desktop focalizzato su attivita' relative a Git. Questa release introduce un filtro kind avanzato per il feed inbox, include zap regolari nei filtri e semplifica la formattazione del testo delle schede. Miglioramenti delle prestazioni ottimizzano il caricamento dell'albero commenti, riducono query database non necessarie e usano branch di commenti in cache per visualizzazione piu' veloce. [Release](https://codeberg.org/dluvian/gitplaza/releases/tag/v0.25.0)

## Modifiche notevoli a codice e documentazione {#notable-code-and-documentation-changes}

### Damus (iOS) {#damus-ios}

Focus sulla stabilita' con correzioni crash e UI: [correzione salto cursore](https://github.com/damus-io/damus/pull/3377) per la vista di composizione, [redesign interfaccia NostrDB](https://github.com/damus-io/damus/pull/3366) usando tipi Swift `~Copyable` per sicurezza delle transazioni, [stabilita' UI thread](https://github.com/damus-io/damus/pull/3341) correggendo reinstanziazione della barra azioni, [freeze lista mute](https://github.com/damus-io/damus/pull/3346) da cicli AttributeGraph, e [crash profilo](https://github.com/damus-io/damus/pull/3334) da pulizia transazioni cross-thread. Aggiunto anche [AGENTS.md](https://github.com/damus-io/damus/pull/3293) linee guida per agenti di coding AI.

### Notedeck (Desktop/Mobile) {#notedeck}

[Archiviazione chiavi sicura](https://github.com/damus-io/notedeck/pull/1191) sposta nsec nel secure store del SO con migrazione automatica. [Filtraggio note future](https://github.com/damus-io/notedeck/pull/1201) nasconde eventi datati 24+ ore in avanti (anti-spam). [Copia nevent](https://github.com/damus-io/notedeck/pull/1183) ora include suggerimenti relay. Inoltre: [aggiunta rapida colonna profilo](https://github.com/damus-io/notedeck/pull/1212), [navigazione tastiera](https://github.com/damus-io/notedeck/pull/1208), [ottimizzazione caricamento media](https://github.com/damus-io/notedeck/pull/1210).

### Amethyst (Android) {#amethyst-android}

Supporto [firma remota [NIP-46](/it/topics/nip-46/)](https://github.com/vitorpamplona/amethyst/pull/1555) per Nostr Connect. [Organizzazione segnalibri](https://github.com/vitorpamplona/amethyst/pull/1586) con gestione liste pubbliche/private. [Correzione compatibilita' strfry](https://github.com/vitorpamplona/amethyst/pull/1596) per casi limite parsing info relay.

### Primal (Android) {#primal-android}

[Deep link Nostr Connect](https://github.com/PrimalHQ/primal-android-app/pull/788) per URL `nostrconnect://`. [Login remoto](https://github.com/PrimalHQ/primal-android-app/pull/787) tramite scansione QR per connessioni bunker. [Correzione race condition connessione](https://github.com/PrimalHQ/primal-android-app/pull/783).

### White Noise (Messaggistica Crittografata) {#white-noise}

[Correzione ritenzione dati app](https://github.com/marmot-protocol/whitenoise/pull/890) disabilita auto-backup Android per privacy. [Comportamento scroll chat](https://github.com/marmot-protocol/whitenoise/pull/861) preserva posizione durante lettura cronologia.

### Zeus (Wallet Lightning) {#zeus}

[Pagamenti paralleli [NIP-47](/it/topics/nip-47/)](https://github.com/ZeusLN/zeus/pull/3407) per miglior throughput zap in batch.

## Best Practice per Sviluppatori

**Validare Eventi Auth in Modo Difensivo** - go-nostr ha corretto un [panic nella validazione NIP-42](https://github.com/nbd-wtf/go-nostr/pull/182) quando il tag relay mancava. Controllate sempre i tag richiesti prima di accedervi, anche nei flussi auth dove vi aspettate eventi ben formati.

**Rate Limit per Stato Autenticazione** - khatru ha aggiunto [rate limiting basato su NIP-42](https://github.com/fiatjaf/khatru/pull/57), permettendo ai relay di applicare limiti diversi per connessioni autenticate vs anonime. Considerate limiti a livelli basati sullo stato auth invece di restrizioni generiche.

**Usare Paginazione a Cursore per Liste** - Blossom ha [sostituito la paginazione basata su data](https://github.com/hzrd149/blossom/pull/65) con paginazione a cursore sull'endpoint `/list`. La paginazione basata su data fallisce quando elementi condividono timestamp; i cursori forniscono iterazione affidabile.

**Validazione Schema per Tipi di Evento** - Il progetto [nostrability/schemata](https://github.com/nostrability/schemata) fornisce schemi JSON per validare eventi conformi ai NIP. Considerate di integrare la validazione schema in sviluppo per catturare eventi malformati prima che raggiungano i relay.

---

Questo e' tutto per questa settimana. State costruendo qualcosa? Avete notizie da condividere? Volete che copriamo il vostro progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattateci via DM NIP-17</a> o trovateci su Nostr.

