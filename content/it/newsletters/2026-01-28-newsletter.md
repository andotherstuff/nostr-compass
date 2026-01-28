---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

Bentornati a Nostr Compass, la vostra guida settimanale a Nostr.

**Questa settimana:** Ridestr porta il ridesharing decentralizzato su Nostr con pagamenti [Cashu](/it/topics/cashu/) e condivisione crittografata della posizione. Pomade introduce il recupero basato su email per i firmatari multisig. Damus implementa [negentropy](/it/topics/negentropy/) per una sincronizzazione affidabile dei DM. L'app desktop di Amethyst aggiunge ricerca, segnalibri e zap. Amber v4.1.1 mostra i punteggi di fiducia dei relay. Marmot unisce MIP-03 e costruisce un'app di chat di riferimento in TypeScript. diVine aggiunge l'autenticazione QR [NIP-46](/it/topics/nip-46/) e il supporto alle menzioni. Nuove proposte NIP affrontano la gestione delle community, la sincronizzazione basata su sequenze e l'archiviazione crittografata dei file. Diamo anche uno sguardo a cinque anni di gennaio di Nostr, tracciando l'evoluzione del protocollo da una manciata di primi utilizzatori nel 2021, attraverso l'esplosivo lancio di Damus sull'App Store nel 2023, fino all'ecosistema client in maturazione del 2025.

## Notizie

### Ridestr Porta il Ridesharing Decentralizzato su Nostr

[Ridestr](https://github.com/variablefate/ridestr) sta sviluppando un'applicazione di ridesharing peer-to-peer costruita interamente su Nostr, che consente transazioni dirette tra autisti e passeggeri con pagamenti in Bitcoin e [Cashu](/it/topics/cashu/). Il protocollo utilizza tipi di evento personalizzati (30173, 3173-3175, 30180/30181) per coordinare le corse mantenendo la privacy attraverso la divulgazione progressiva della posizione e la crittografia [NIP-44](/it/topics/nip-44/).

Il sistema funziona attraverso un flusso attentamente coreografato: gli autisti trasmettono la disponibilità usando posizioni codificate in geohash (precisione ~5km) tramite eventi kind 30173, i passeggeri richiedono corse con stime delle tariffe attraverso kind 3173, e i pagamenti sono protetti usando token escrow HTLC prima dell'inizio della corsa. La privacy della posizione è preservata attraverso la divulgazione progressiva, dove i dettagli del ritiro vengono rivelati solo quando gli autisti arrivano e le destinazioni sono condivise dopo la verifica del PIN. Tutta la comunicazione tra le parti utilizza la crittografia [NIP-44](/it/topics/nip-44/) per la privacy.

Ridestr implementa la sicurezza dei pagamenti attraverso escrow HTLC con firme P2PK. Quando un passeggero accetta l'offerta di un autista, blocca i token [Cashu](/it/topics/cashu/) con un hash di pagamento che solo l'autista può reclamare dopo il completamento della corsa. Il protocollo attualmente opera con un'architettura single-mint, richiedendo che passeggeri e autisti utilizzino lo stesso mint [Cashu](/it/topics/cashu/). L'implementazione Android basata su Kotlin gestisce la verifica delle prove e il recupero delle prove obsolete attraverso i controlli di stato NUT-07.

Ridestr affronta sfide che la maggior parte delle applicazioni Nostr evita: coordinamento della posizione in tempo reale, escrow dei pagamenti con risoluzione delle dispute e sistemi di reputazione per interazioni nel mondo fisico. Il progetto è in beta e dimostra che il modello di eventi di Nostr può supportare marketplace di servizi peer-to-peer, non solo la condivisione di contenuti.

### Pomade Lancia il Sistema di Recupero Alpha per Firmatari Multisig

[Pomade](https://github.com/coracle-social/pomade), sviluppato da hodlbod, si basa sull'ecosistema [FROSTR](https://github.com/FROSTR-ORG) esistente per fornire un servizio di firma a soglia focalizzato sul recupero. Utilizzando le firme [FROST](/it/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) tramite la libreria @frostr/bifrost, Pomade aggiunge flussi di recupero basati su email sopra la crittografia a soglia. Il sistema frammenta la chiave segreta di un utente usando Shamir Secret Sharing, distribuendo le quote tra più firmatari indipendenti con una soglia configurabile (2-di-3, 3-di-5, ecc.).

Il protocollo opera interamente su Nostr usando un singolo tipo di evento (28350) con payload crittografati [NIP-44](/it/topics/nip-44/). Durante la firma, il client richiede firme parziali da almeno `threshold` firmatari, poi le aggrega in una firma Schnorr valida. Per la crittografia, i firmatari collaborano per derivare segreti condivisi via ECDH senza che nessuna singola parte apprenda la chiave completa.

Il recupero funziona attraverso due metodi di autenticazione: basato su password (usando argon2id con la pubkey del firmatario come salt) o OTP via email. Per prevenire attacchi MITM durante il recupero OTP, ogni firmatario genera il proprio codice di verifica con un prefisso fornito dal client, richiedendo agli utenti di autenticarsi indipendentemente con ogni firmatario. Il protocollo richiede proof-of-work sugli eventi di registrazione (20+ bit secondo [NIP-13](/it/topics/nip-13/)) per prevenire lo spam.

Il modello di fiducia è esplicito: se `threshold` firmatari colludono, possono rubare la chiave. I provider email sono completamente fidati poiché possono intercettare gli OTP. Gli utenti non possono recuperare indipendentemente la loro chiave segreta completa; farlo richiede la cooperazione di `threshold` firmatari. Il protocollo è progettato per l'onboarding di nuovi utenti non familiari con la gestione delle chiavi, con la raccomandazione esplicita che gli utenti migrino all'auto-custodia una volta a loro agio. Pomade avverte di potenziali "perdite di chiavi, furti, denial of service o fughe di metadati" dato il suo stato alpha non auditato.

## Rilasci

### Damus Implementa Negentropy per la Sincronizzazione Affidabile dei DM

[Damus v1.13](https://github.com/damus-io/damus/releases/tag/v1.13-6) implementa l'implementazione negentropy [che abbiamo presentato come PR aperta la settimana scorsa](/it/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs). [PR #3536](https://github.com/damus-io/damus/pull/3536) aggiunge il supporto base [negentropy](/it/topics/negentropy/) al livello di rete, abilitando la riconciliazione degli insiemi con i relay che supportano il protocollo. Una [PR #3547](https://github.com/damus-io/damus/pull/3547) complementare aggiunge la sincronizzazione DM pull-to-refresh che usa negentropy per recuperare i messaggi mancanti quando le sottoscrizioni REQ standard falliscono.

L'implementazione segue un approccio conservativo: il caricamento normale dei DM continua invariato, con [negentropy](/it/topics/negentropy/) disponibile come meccanismo di recupero quando gli utenti aggiornano manualmente. I test automatizzati dimostrano la correzione generando un DM con un timestamp vecchio che le query standard mancherebbero, poi usando la sincronizzazione [negentropy](/it/topics/negentropy/) per recuperarlo con successo. Mentre il supporto [negentropy](/it/topics/negentropy/) richiede relay compatibili, l'implementazione gestisce elegantemente ambienti con relay misti usando il protocollo dove disponibile.

### Amber v4.1.1 - Punteggi di Fiducia dei Relay

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1) implementa la visualizzazione dei punteggi di fiducia dei relay ([PR #289](https://github.com/greenart7c3/Amber/pull/289)), implementando i concetti di valutazione dei relay discussi nella [copertura dei Trusted Relay Assertions della settimana scorsa](/it/newsletters/2026-01-21-newsletter/#nip-updates). I punteggi di fiducia ora appaiono nella pagina Relays e per le richieste di connessione NostrConnect, aiutando gli utenti a valutare l'affidabilità dei relay prima di autorizzare le connessioni. Il rilascio include anche una UI ridisegnata per login/eventi/permessi e supporto per il metodo `switch_relays`. I miglioramenti delle prestazioni memorizzano in cache le operazioni del keystore, affrontando le segnalazioni di tempi di caricamento di oltre 20 secondi su dispositivi più vecchi.

### nak v0.18.2 - Integrazione MCP

Il [nak](https://github.com/fiatjaf/nak) di fiatjaf (Nostr Army Knife) [v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2) aggiunge il supporto [Model Context Protocol](https://nostrify.dev/mcp) tramite `nak mcp`, permettendo agli agenti AI di cercare persone su Nostr, pubblicare note, menzionare utenti e leggere contenuti usando il modello outbox. Il rilascio introduce anche un [installer con una sola riga](https://github.com/fiatjaf/nak/blob/master/install.sh) (`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`) che scarica binari precompilati, eliminando il requisito della toolchain Go per gli utenti finali. La modalità Bunker ora supporta Unix socket e `switch_relays`.

### Zeus v0.12.2 Beta - Fix NWC

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases) implementa multiple correzioni NWC che affrontano i problemi coperti nella [copertura di Zeus della settimana scorsa](/it/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect).

## Aggiornamenti dei Progetti

### Amethyst Desktop - Fase 2A Rilasciata

[Amethyst](https://github.com/vitorpamplona/amethyst) ha rilasciato [la Fase 2A della sua app desktop](https://github.com/vitorpamplona/amethyst/pull/1676), aggiungendo Ricerca, Segnalibri, Zap, viste Thread e contenuti long-form (Letture) all'esperienza desktop. Una [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683) complementare aggiunge feedback trasparente sulla trasmissione degli eventi così gli utenti ora vedono lo stato in tempo reale per-relay mentre i loro eventi si propagano attraverso la rete, rendendo più facile diagnosticare problemi di connettività.

### Progressi di Notedeck: App Calendario e Rifinitura UX

L'app desktop [Notedeck](https://github.com/damus-io/notedeck) del team Damus ha unito il comportamento di auto-nascondimento della toolbar ([PR #1268](https://github.com/damus-io/notedeck/pull/1268)) che risponde alla velocità di scorrimento per più spazio sullo schermo nelle viste mobile. Una [bozza PR #1271](https://github.com/damus-io/notedeck/pull/1271) aggiunge un'app Calendario [NIP-52](/it/topics/nip-52/) completa con viste mese/settimana/giorno/agenda, supporto RSVP e commenti [NIP-22](/it/topics/nip-22/) sugli eventi del calendario, attualmente con feature-flag per i test.

### Jumble Aggiunge Modalità Community

[Jumble](https://github.com/CodyTseng/jumble), il client web focalizzato sui relay, ha aggiunto [modalità community](https://github.com/CodyTseng/jumble/pull/738) e supporto per [preset di set di relay tramite variabili d'ambiente](https://github.com/CodyTseng/jumble/pull/736), rendendo più facile distribuire istanze tematiche come [nostr.moe](https://nostr.moe/).

### Dashboard Ordini di Shopstr

[Shopstr](https://github.com/shopstr-eng/shopstr) ha sostituito la sua gestione ordini basata su chat con una [Dashboard Ordini](https://github.com/shopstr-eng/shopstr/pull/219) dedicata. La nuova interfaccia fornisce una vista centralizzata per i merchant per tracciare lo stato degli ordini, segnare i messaggi come letti e gestire l'evasione senza scorrere le conversazioni chat. L'aggiornamento depreca il caching IndexedDB in favore delle API server-side per lo stato degli ordini e rivede come i DM degli ordini vengono taggati per un miglior filtraggio.

### Formstr Aggiunge Domande a Griglia

[Formstr](https://github.com/abh3po/nostr-forms), l'app form nativa Nostr, ha aggiunto [domande a griglia](https://github.com/abh3po/nostr-forms/pull/419) e [riscritto il suo SDK](https://github.com/abh3po/nostr-forms/pull/410) con supporto per embed. Una [correzione per firmatari non-[NIP-07](/it/topics/nip-07/)](https://github.com/abh3po/nostr-forms/pull/418) ha risolto problemi per utenti con bunker o firmatari locali che tentavano di inviare form con la loro identità.

### nostr-tools Aggiorna le Dipendenze Crittografiche

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), la libreria JavaScript core, [ha aggiornato a @noble/curves v2.0.1](https://github.com/nbd-wtf/nostr-tools/pull/520), affrontando modifiche API breaking attraverso 27 file e adottando le ultime librerie noble auditate. fiatjaf ha anche aggiunto il supporto `switch_relays` a [NIP-46](/it/topics/nip-46/), permettendo ai client bunker di cambiare dinamicamente le connessioni ai relay.

### Zeus Lavora sulle Recensioni Mint NIP-87

[Zeus](https://github.com/ZeusLN/zeus) ha una [PR aperta per le recensioni mint [NIP-87](/it/topics/nip-87/)](https://github.com/ZeusLN/zeus/pull/3576), permettendo agli utenti di scoprire e recensire i mint [Cashu](/it/topics/cashu/) filtrati dai seguiti Nostr. Le recensioni includono valutazioni a stelle e possono essere inviate anonimamente o con l'nsec dell'utente.

### Camelus Implementa Supporto DM Completo

[Camelus](https://github.com/camelus-hq/camelus), un client Android basato su Flutter costruito con Dart NDK per prestazioni mobile efficienti in termini di batteria, ha aggiunto messaggistica diretta completa con oltre 20 commit questa settimana. L'aggiornamento include categorie chat, date dei messaggi, UI di invio ottimistica, funzionalità nota-a-se-stessi e gestione corretta dei relay DM.

### Aggiornamenti del Protocollo Marmot

La risoluzione deterministica dei commit MIP-03 [che abbiamo coperto come PR aperta la settimana scorsa](/it/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library) è stata ora unita. [MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152) assicura che tutte le chat di gruppo basate su [MLS](/it/topics/mls/) convergano sullo stesso stato quando più commit validi arrivano per la stessa epoca.

Una [PR spec #28](https://github.com/marmot-protocol/marmot/pull/28) complementare aggiunge requisiti del ciclo di vita init_key che affrontano lacune dagli audit di implementazione: il materiale della chiave privata dai messaggi Welcome deve essere cancellato in modo sicuro dopo l'elaborazione (zeroizzazione, pulizia dello storage), e i nuovi membri devono eseguire auto-aggiornamenti entro 24 ore per la forward secrecy.

L'SDK TypeScript ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) sta costruendo un'applicazione di chat di riferimento. [PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37) aggiunge creazione/lista gruppi, gestione key package con flussi di pubblicazione/trasmissione/cancellazione e inviti tramite codice QR. Una [PR aperta #38](https://github.com/marmot-protocol/marmot-ts/pull/38) di hzrd149 implementa la persistenza della cronologia messaggi con paginazione. Su whitenoise-rs, 8 PR sono state unite a master questa settimana, in particolare Add event id to user reaction che abilita l'eliminazione delle reazioni esponendo gli ID degli eventi di reazione, e fix(message_aggregator/emoji_utils): improve is_valid_emoji to capture more valid emoji che amplia la validazione emoji per supportare blocchi Unicode estesi, indicatori regionali e sequenze di tasti. Altri aggiornamenti includono la memorizzazione delle preferenze linguistiche per la localizzazione lato client e la rimozione dei soprannomi predefiniti per dare ai client il pieno controllo sui metadati di registrazione.

### diVine Aggiunge Funzionalità di Integrazione Nostr

[diVine](https://github.com/divinevideo/divine-mobile), l'app video short-form, continua la rapida integrazione Nostr.

I merge recenti includono l'autenticazione tramite codice QR [NIP-46](/it/topics/nip-46/) ([PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)) e la messaggistica diretta crittografata [NIP-17](/it/topics/nip-17/) ([PR #834](https://github.com/divinevideo/divine-mobile/pull/834)). L'attività di questa settimana si è concentrata sul [supporto menzioni](https://github.com/divinevideo/divine-mobile/pull/1098) che converte URI `nostr:` e @menzioni in link profilo cliccabili, [fallback avatar Classic Viners](https://github.com/divinevideo/divine-mobile/pull/1097) usando profili Nostr, e strumenti di editing video inclusi [disegno](https://github.com/divinevideo/divine-mobile/pull/1056), [filtri](https://github.com/divinevideo/divine-mobile/pull/1053) e [sticker](https://github.com/divinevideo/divine-mobile/pull/1050).

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**PR Aperte e Discussioni:**

- **[Trusted Relay Assertions](https://github.com/nostr-protocol/nips/pull/1534)** - La proposta bozza per standardizzare i punteggi di fiducia dei relay [che abbiamo coperto la settimana scorsa](/it/newsletters/2026-01-21-newsletter/#nip-updates) continua la discussione. Il dibattito centrale si concentra sul fatto che i punteggi di fiducia debbano essere "globali" (calcolati una volta per tutti gli utenti) o "personalizzati" (relativi al grafo sociale di ogni osservatore). Algoritmi in stile PageRank come [Trust Rank di nostr.band](https://trust.nostr.band/) e [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) resistono agli attacchi sybil dividendo qualsiasi rank passato attraverso account falsi per la dimensione della bot farm. I critici sostengono che i punteggi veramente personalizzati sono più accurati ma richiedono calcoli costosi per-utente. La discussione esplora anche se usare DVM per il punteggio on-demand rispetto a eventi attestazione kind 30382 pre-calcolati che i client possono memorizzare in cache.

- **Communikeys** - Una [proposta completa](https://nostrhub.io) per la gestione delle community che usa npub esistenti come identificatori di community invece di approcci basati su relay. Qualsiasi npub può diventare una community pubblicando un evento kind 10222; le pubblicazioni mirano alle community tramite eventi kind 30222. Il controllo degli accessi usa badge [NIP-58](/it/topics/nip-58/), abilitando la gestione delegata dell'appartenenza con cold storage per le chiavi della community.

- **[NIP-CF: Changes Feed](https://njump.me/nevent1qqsyxrrdu09yktr7x5cqqrcj9v2hrqqqefem6f3stkrzwf8anr236sgcpzfmhxue69uhkummnw3ezu7nzvshxwec4wa0qn)** - Una bozza che propone la sincronizzazione degli eventi basata su sequenze come alternativa ai filtri `since` basati su timestamp. Il problema: la sincronizzazione Nostr standard usando timestamp `since` può perdere eventi quando più eventi condividono lo stesso timestamp con precisione al secondo, gli orologi del client e del relay divergono, o il checkpointing è impreciso. NIP-CF risolve questo facendo assegnare ai relay numeri di sequenza monotonicamente crescenti agli eventi memorizzati, fornendo un ordinamento totale rigoroso. I client richiedono modifiche da un numero di sequenza specifico e ricevono eventi in ordine garantito, con checkpointing preciso che non perde mai eventi. La proposta supporta anche la modalità live/continua dove le sottoscrizioni rimangono aperte dopo la sincronizzazione iniziale per aggiornamenti in tempo reale.

- **[NIP-XX: Encrypted File Sync](https://njump.me/nevent1qqsr98tvcy7c4y5w03rd6cdujq9dpdt75uzv4kmkgpdlq7ggdmzptrqcpzfmhxue69uhkummnw3ezu7nzvshxwec4wa0qn)** - Un protocollo che definisce i kind 30800 (file crittografati), 30801 (indici vault) e 30802 (documenti condivisi) per sincronizzare contenuti crittografati tra dispositivi usando i relay Nostr. Il protocollo abilita app di note-taking local-first per fornire sincronizzazione crittografata end-to-end senza server centralizzati. Contenuti dei file, percorsi, nomi e struttura delle cartelle sono tutti crittografati usando l'auto-crittografia [NIP-44](/it/topics/nip-44/), così i relay memorizzano blob che non possono leggere. Gli allegati binari come le immagini usano server [Blossom](/it/topics/blossom/) con crittografia lato client. Il kind 30802 abilita la condivisione di documenti tra utenti crittografando verso la chiave pubblica del destinatario.

## Cinque Anni di Gennaio di Nostr

[La newsletter del mese scorso](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers) ha tracciato le pietre miliari di dicembre di Nostr dal primo rilascio client di fiatjaf attraverso la donazione catalizzatrice di Jack Dorsey. Questa retrospettiva traccia cosa è successo ogni gennaio dal 2021 al 2025, concentrandosi sugli sviluppi tecnici verificati.

### Gennaio 2021: Sviluppo Iniziale

Il terzo mese di Nostr vide lo sviluppo continuato di Branle, il client Vue.js di fiatjaf lanciato a dicembre 2020. Un piccolo gruppo di primi utilizzatori, probabilmente meno di 15 persone, si coordinava attraverso il gruppo Telegram [@nostr_protocol](https://t.me/nostr_protocol) (creato il 16 novembre 2020), testando il protocollo su uno o due relay sperimentali. Il client da riga di comando noscl forniva interazione basata su terminale.

Le fondamenta tecniche erano già bloccate: utenti identificati da chiavi pubbliche secp256k1, post firmati crittograficamente con firme Schnorr, e relay che servono come storage stupido che non comunicano tra loro. Questa era crittografia deliberatamente nativa di Bitcoin, una scelta di design che avrebbe plasmato i pattern di adozione anni dopo.

### Gennaio 2022: Scoperta degli Sviluppatori

Gennaio 2022 si aprì con Nostr ancora in fermento dalla sua [prima apparizione su Hacker News](https://news.ycombinator.com/item?id=29749061) (31 dicembre 2021), che generò 110 punti e 138 commenti. Al momento di quel post, solo circa sette relay alimentavano l'intera rete, con i commentatori che notavano "lo spam non è ancora un problema perché nostr è super nuovo e nessuno lo usa ancora". Robert C. Martin ("Uncle Bob") aveva appoggiato Nostr come potenzialmente "la soluzione definitiva per la comunicazione sociale". La discussione continuò a gennaio, con sviluppatori che dibattevano architettura relay versus vero P2P, resistenza alla censura versus moderazione, e se la semplicità potesse scalare.

Il post HN scatenò un'ondata di nuove implementazioni. Uncle Bob stesso iniziò [more-speech](https://github.com/unclebob/more-speech), un client desktop Clojure, il 18 gennaio. La libreria [go-nostr](https://github.com/nbd-wtf/go-nostr) di fiatjaf (creata gennaio 2021) e il client da riga di comando [noscl](https://github.com/fiatjaf/noscl) fornivano strumenti Go, mentre [nostr-tools](https://github.com/nbd-wtf/nostr-tools) offriva supporto JavaScript. Entro dicembre 2022, circa 800 profili avevano bio. Branle rimase il client web principale, ricevendo aggiornamenti inclusi import della chiave privata e supporto multi-relay. Le sfide tecniche erano evidenti: le chiavi esadecimali da 64 caratteri si rivelarono non intuitive, i ritardi dei messaggi frustravano gli utenti, e la community si chiedeva se l'architettura potesse gestire traffico a scala Twitter.

### Gennaio 2023: La Svolta

Gennaio 2023 trasformò Nostr da esperimento a movimento. Damus, il client iOS di William Casarin (jb55), lottava con il processo di approvazione dell'App Store di Apple. Rifiutato il 1° gennaio, rifiutato di nuovo il 26 gennaio, fu finalmente [approvato il 31 gennaio](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store). Quell'approvazione scatenò una cascata: Damus raggiunse immediatamente la posizione #10 in U.S. Social Networking. Jack Dorsey [lo definì](https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store) "una pietra miliare per i protocolli aperti".

Otto giorni prima, il 23 gennaio, [Edward Snowden annunciò](https://x.com/Snowden/status/1617623779626352640) la sua presenza su Nostr: "Una delle cose cool di Nostr... oltre alla resistenza alla censura, è che non sei limitato a 280 caratteri". Il suo endorsement da parte di un whistleblower della NSA aveva peso nei circoli attenti alla privacy, e gli utenti iniziarono immediatamente a inviargli zap in sats via Lightning.

I client web corsero per gestire l'afflusso. [Snort](https://github.com/v0l/snort), creato da kieran a dicembre 2022, emerse come un client React ricco di funzionalità; il 13 gennaio, Snort integrò la registrazione NIP-05 tramite l'API Nostr Plebs, permettendo ai nuovi utenti di reclamare identità leggibili durante l'onboarding. [Iris](https://iris.to), sviluppato a tempo pieno da Martti Malmi (un early contributor di Bitcoin che ricevette la seconda transazione Bitcoin mai fatta da Satoshi), offriva interfacce sia web che mobile con identità NIP-05 gratuite su iris.to. [Astral](https://github.com/monlovesmango/astral), costruito da monlovesmango con Quasar (Vue.js) come fork di Branle, si concentrava sulla gestione dei relay con la sua funzionalità di raggruppamento relay che permetteva agli utenti di organizzare i relay in set per la pubblicazione e il filtraggio. Le beta TestFlight per i client iOS si riempivano in poche ore, e Amethyst dominava su Android.

L'infrastruttura faticava a tenere il passo. Tutti i relay erano gestiti da appassionati che pagavano di tasca propria. I relay a pagamento che usavano micropagamenti Lightning creavano un filtraggio naturale dello spam ma introducevano frizione nell'accesso. [Damus fu rimosso dall'App Store della Cina](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) solo due giorni dopo l'approvazione, riferibilmente su richiesta del principale organo di vigilanza internet della Cina.

### Gennaio 2024: Consolidamento del Protocollo

Gennaio 2024 si concentrò sulla standardizzazione del protocollo e sulla costruzione della community. [Nostr PHX](https://www.nostrphx.com/events) iniziò l'anno con un meetup il 5 gennaio a Phoenix, riunendo cypherpunk locali. Questo fu il primo di molti eventi della community quell'anno inclusi BTC Prague (giugno), Nostriga a Riga (agosto) e Nostrasia.

Lo sviluppo del protocollo più significativo fu [NIP-59 (Gift Wrap)](https://github.com/nostr-protocol/nips/pull/716) unito il 29 gennaio, fornendo protezione dei metadati per le comunicazioni crittografate. Gift Wrap si basa sullo [standard di crittografia NIP-44](https://github.com/paulmillr/nip44) (che era stato [auditato da Cure53](https://cure53.de/audit-report_nip44-implementations.pdf) a dicembre 2023) per nascondere l'identità del mittente dai relay. Il protocollo avvolge i messaggi crittografati all'interno di un evento esterno firmato da una keypair casuale, usa-e-getta. I relay vedono solo la pubkey usa-e-getta, mentre la vera identità del mittente è sepolta nel payload crittografato che solo il destinatario può decifrare. Questo impedisce agli operatori dei relay e agli osservatori della rete di sapere chi sta messaggiando chi. I timestamp possono anche essere randomizzati per sconfiggere l'analisi temporale.

L'ecosistema si espanse oltre i social media. [Plebeian Market](https://plebeian.market) diventò completamente Nostr-native con conformità [NIP-15](/it/topics/nip-15/), abilitando carrelli cross-stall e un browser di stall per scoprire i merchant. [Shopstr](https://github.com/shopstr-eng/shopstr) emerse come un marketplace permissionless che facilitava il commercio Bitcoin. [Zap.stream](https://zap.stream/), costruito da kieran, portò lo streaming live su Nostr con pagamenti Lightning a 21 sats/minuto. Gli strumenti per sviluppatori maturarono con [NDK](https://github.com/nostr-dev-kit/ndk) che forniva astrazioni TypeScript e [rust-nostr](https://github.com/rust-nostr/nostr) che offriva binding Rust. [Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/) fu rilasciato con import contatti Nostr e LND persistente, gettando le basi per l'integrazione Nostr Wallet Connect nei rilasci successivi.

Eppure la sostenibilità dell'infrastruttura [rimaneva una sfida](https://arxiv.org/abs/2402.05709). La ricerca accademica di questo periodo trovò che il 95% dei relay faticava a coprire i costi operativi, con il 20% che sperimentava significativi tempi di inattività. La tariffa di ammissione per i relay a pagamento era in media meno di 1.000 sats (~$0.45), insufficiente a sostenere le operazioni.

*Una nota sulle truffe: Il "Nostr Assets Protocol" e il token "$NOSTR" associato che furono lanciati in questo periodo [furono pubblicamente denunciati da fiatjaf](https://www.aicoin.com/en/article/377704) come "100% fraudolenti" e "una truffa di affinità" senza alcuna connessione con il vero protocollo Nostr.*

### Gennaio 2025: Maturazione dei Client

Gennaio 2025 vide lo sviluppo continuato dei client attraverso l'ecosistema. [Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/) fu rilasciato il 13 gennaio con sincronizzazione cross-device per gli stati di lettura, supporto login multi-sig [FROST](/it/topics/frost/) e prestazioni ottimizzate del database locale. Amethyst continuò la sua transizione al modello outbox, compilando automaticamente set di relay basati sulle liste di follow piuttosto che richiedere configurazione manuale.

I principali client iniziarono ad allontanarsi da [NIP-04](/it/topics/nip-04/) per i messaggi diretti, migrando verso [NIP-17](/it/topics/nip-17/) e il proposto [NIP-104](/it/topics/nip-104/) per crittografia migliorata e protezione dei metadati. Il modello Gossip (comunicazione outbox/inbox) guadagnò adozione mentre l'ecosistema convergeva verso pattern di utilizzo dei relay più efficienti. Gli osservatori del settore prevedevano che questo sarebbe stato l'anno in cui Nostr transita da protocollo di nicchia a riconoscimento mainstream, con una potenziale migrazione di piattaforma ad alto profilo che potrebbe raddoppiare l'attività giornaliera.

### Gennaio 2026: Sicurezza e Infrastruttura di Firma

Gennaio 2026 portò significativi avanzamenti nella sicurezza e nell'infrastruttura di firma. [Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) fu rilasciato con firma remota [NIP-46](/it/topics/nip-46/) e supporto per firmatario locale [NIP-55](/it/topics/nip-55/), unendosi ad Amber e Aegis come hub di firma completo per altre app Android. [Bitchat completò un audit di sicurezza Cure53](https://github.com/permissionlesstech/bitchat/pulls), la stessa azienda che auditò Signal e NIP-44, con oltre 17 PR che correggevano problemi critici inclusa la cancellazione dei segreti DH e problemi di thread safety. Sia Bitchat che Damus migrarono da C Tor a Rust Arti per maggiore affidabilità e sicurezza della memoria.

Il lavoro sul protocollo continuò con [NIP-71](https://github.com/nostr-protocol/nips/pull/1669) (eventi video addressable) unito e una NIP sulla crittografia post-quantistica che aprì la discussione sul future-proofing di Nostr contro attacchi quantistici. La bozza Trusted Relay Assertions propose la standardizzazione del punteggio di fiducia dei relay attraverso attestazioni firmate. Il [Protocollo Marmot](https://github.com/marmot-protocol/mdk) rafforzò la sua messaggistica crittografata basata su [MLS](/it/topics/mls/) con 18 PR unite che affrontavano le scoperte dell'audit.

Le applicazioni nel mondo reale si espansero con [Ridestr](https://github.com/variablefate/ridestr) che sviluppa ridesharing decentralizzato usando escrow [Cashu](/it/topics/cashu/) e crittografia [NIP-44](/it/topics/nip-44/), e [Pomade](https://github.com/coracle-social/pomade) che aggiunge flussi di recupero basati su email alla firma a soglia [FROST](/it/topics/frost/). Damus rilasciò [negentropy](/it/topics/negentropy/) per la sincronizzazione affidabile dei DM, mentre l'app desktop di Amethyst raggiunse la Fase 2A con ricerca, segnalibri e zap.

### Guardando Avanti

Sei anni di gennaio rivelano l'evoluzione di Nostr dallo sviluppo iniziale (2021) alla scoperta pubblica (2022) alla crescita esplosiva (2023) al consolidamento del protocollo (2024) alla maturazione dei client (2025) all'infrastruttura di sicurezza (2026). Il pattern è familiare a chiunque abbia osservato la crescita dei protocolli aperti: anni di costruzione silenziosa, un'esplosione improvvisa quando le condizioni si allineano, poi il lavoro più lungo di rendere tutto affidabile. Quello che è iniziato con sette relay e un thread su Hacker News è ora infrastruttura auditata con applicazioni reali. La domanda per il 2027: quando qualcuno chiamerà una corsa, invierà un messaggio crittografato o recupererà una chiave persa usando Nostr, sapranno anche che lo stanno usando?

---

È tutto per questa settimana. Stai costruendo qualcosa? Hai notizie da condividere? Vuoi che copriamo il tuo progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattaci via DM NIP-17</a> o trovaci su Nostr.
