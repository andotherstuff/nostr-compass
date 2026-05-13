---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-13-newsletter.md
translationDate: 2026-05-13
description: 'Nostr VPN pubblica otto versioni in una settimana culminando con v4.0.10, passando da un flusso di pairing dei dispositivi ridisegnato a uno swap AEAD BoringSSL che raddoppia il throughput TCP fino al batching sendmmsg e una completa revisione della UX di pairing; Marmot Protocol (White Noise) pubblica una versione frontend che completa la funzionalità di blocco degli utenti e 31 PR unite su MDK e backend; Grain v0.6.0 aggiunge NIP-40, NIP-50, NIP-70 e NIP-45 in un unico traguardo; Citrine v3.0.0-pre1 integra Tor nativo e aggregazione relay; Amber v6.1.0-pre2 migliora il flusso di connessione delle nuove app; Alby Hub v1.22.2 aggiunge una pagina AI e Agenti e il supporto Core Lightning; Mostro pubblica i bond del taker concorrenti e v0.11.0 di mostro-core; Jumble pubblica cinque versioni da v26.5.2 a v26.5.6 con raggruppamento notifiche, ricerca recente e persistenza dei dati account; Nostrord pubblica v1.0.0 fino a v1.0.2 con modal di condivisione gruppo e pacchetti Arch Linux; Flotilla 1.8.0 aggiunge videochiamate, rendering email e menzioni di stanza; Calendar by Formstr v1.5.1 pubblica la pianificazione degli appuntamenti e la sincronizzazione del calendario Android; Tamagostrich lancia un Tamagotchi NIP-78 decentralizzato con ricompense in sats via NIP-47; le discussioni NIP portano alla luce Prenotazioni, Servizi di escrow, Annunci di alloggio, Zap on-chain e regole di comunità verificabili. Due approfondimenti NIP coprono NIP-78 (dati specifici dell\'app) e NIP-98 (HTTP Auth).'
---

Bentornati a Nostr Compass, la vostra guida settimanale allo sviluppo del protocollo Nostr.

**Questa settimana:** Nostr VPN pubblica otto versioni in sette giorni, da un flusso di pairing dei dispositivi ridisegnato a uno swap AEAD FIPS che circa raddoppia il throughput TCP. Marmot Protocol (la base di White Noise) pubblica una versione frontend che completa la funzionalità di blocco degli utenti e 31 PR unite su MDK e backend. Grain pubblica v0.6.0 con quattro nuove implementazioni NIP in un unico traguardo. Citrine pubblica v3.0.0-pre1 con Tor integrato e aggregazione relay. Amber pubblica v6.1.0-pre2 con miglioramenti al flusso di connessione e alla firma. Alby Hub pubblica v1.22.2 con una pagina AI e Agenti e l'integrazione Core Lightning. Mostro pubblica i bond del taker concorrenti e mostro-core v0.11.0. Jumble pubblica cinque versioni con la cronologia delle ricerche recenti e correzioni alla persistenza dei dati account. Nostrord pubblica tre versioni con modal di condivisione gruppo e pacchetti Arch Linux. Flotilla pubblica 1.8.0 con videochiamate, rendering email e menzioni di stanza. Calendar by Formstr pubblica v1.5.1 con la pianificazione degli appuntamenti e la sincronizzazione del calendario Android. Tamagostrich lancia un Tamagotchi NIP-78 decentralizzato con ricompense in sats.

## Storie principali

### Nostr VPN pubblica otto versioni culminando con v4.0.10

Nostr VPN, la VPN mesh decentralizzata basata su Rust che utilizza Nostr per la scoperta dei peer, ha pubblicato otto versioni da v4.0.1 a v4.0.10 su macOS, Linux, Windows e Android. La modifica principale di v4.0.8: l'AEAD è stato sostituito dal backend software RustCrypto chacha20poly1305 con ChaCha20-Poly1305 di BoringSSL in ring 0.17, che utilizza NEON ottimizzato a mano su aarch64 e AVX2/AVX-512 su x86_64. I benchmark Docker su hardware identico hanno mostrato il throughput TCP diretto a 2 nodi passare da 437 a 1097 Mbps. v4.0.9 ha aggiunto il batching sendmmsg(2) sul percorso di invio UDP, portando il TCP single-stream da 1066 a 1548 Mbps (1,45×). v4.0.10 ha pubblicato una completa revisione della UX di pairing dei dispositivi.

### Marmot / White Noise pubblica una versione frontend che completa il blocco degli utenti e 31 PR unite su MDK e backend

White Noise ha pubblicato v2026.5.7+24 il 7 maggio completando il set di funzionalità di blocco. Un utente bloccato è ora nascosto dagli inviti, dalle anteprime delle chat, dalle timeline dei messaggi, dai risultati di ricerca e dalle notifiche, e i suoi messaggi non contano più nei badge dei messaggi non letti. MDK ha integrato PR #258 con il formato wire dell'estensione v3 e lo schema disappearing_message_secs, gettando le basi per i messaggi a scomparsa.

### Grain v0.6.0 aggiunge NIP-40, NIP-50, NIP-70 e NIP-45

Grain ha pubblicato v0.6.0 il 6 maggio con quattro nuove implementazioni NIP. La scadenza degli eventi NIP-40 consente ai publisher di impostare un timestamp di scadenza affinché il relay elimini gli eventi dopo la loro scadenza. La ricerca full-text NIP-50 consente ai client di emettere filtri di ricerca nei messaggi REQ. Gli eventi protetti NIP-70 impediscono ai relay di ricondividere eventi senza l'esplicita autorizzazione dell'autore. Le query di conteggio NIP-45 consentono ai client di chiedere a un relay di restituire un conteggio degli eventi corrispondenti.

## Pubblicazioni della settimana

### Citrine v3.0.0-pre1 integra Tor nativo e aggregazione relay

Citrine ha pubblicato v3.0.0-pre1 con supporto Tor integrato per un accesso ai relay che preserva la privacy e l'aggregazione relay, dove Citrine può estrarre eventi da più relay upstream e servirli ai client locali. PR #139 aggiunge il supporto NIP-77 (Negentropy Reconciliation) per la sincronizzazione efficiente degli eventi basata sulla riconciliazione degli insiemi.

### Amber v6.1.0-pre2 migliora il flusso di connessione delle nuove app

Amber ha pubblicato v6.1.0-pre2. Le correzioni principali: il dialogo del firmatario ora si chiude correttamente dopo aver accettato una richiesta bunker, le richieste bunker malformate mostrano una schermata di richiesta non valida, e viene aggiunta la limitazione della velocità per le richieste di firma basate su intent.

### Alby Hub v1.22.2 aggiunge la pagina AI e Agenti e il supporto Core Lightning

Alby Hub ha pubblicato v1.22.2. La nuova pagina AI e Agenti espone le capacità Lightning e NWC di Alby Hub agli agenti AI e agli strumenti compatibili MCP. Core Lightning (CLN) è ora un backend supportato insieme a LND e LDK.

### Mostro pubblica i bond del taker concorrenti e mostro-core v0.11.0

Mostro ha integrato 11 PR che avanzano la funzionalità di bond del taker. PR #733 implementa i bond del taker concorrenti dove più taker possono inviare fatture di bond contemporaneamente e il primo a bloccare vince. mostro-core ha pubblicato v0.11.0 con PR #144 che aggiunge Action::PayBondInvoice e Status::WaitingTakerBond. mostro-cli ha pubblicato v0.15.0.

### Jumble pubblica cinque versioni con ricerca recente e persistenza degli account

Jumble ha pubblicato v26.5.2 fino a v26.5.6. v26.5.5 aggiunge la cronologia delle ricerche recenti. Un bug critico di persistenza è corretto in v26.5.6: gli account e i dati memorizzati nella cache sopravvivono ora a un riavvio completo dell'app.

### Nostrord pubblica modal di condivisione gruppo, caricamento media e pacchetti Arch Linux

Nostrord ha pubblicato v1.0.0, v1.0.1 e v1.0.2. v1.0.1 pubblica pacchetti Arch Linux tramite AUR come nostrord-bin con artefatti firmati con PGP, un pulsante per saltare all'ultimo messaggio e l'incolla di immagini/media nella chat. v1.0.2 aggiunge la condivisione del gruppo tramite PR #49 con un modal di condivisione che genera sia un URI nostr:naddr che un link nostrord.com/open/.

### FIPS v0.3.0 pubblica portata multipiattaforma, scoperta peer Nostr e un gateway per LAN non modificate

FIPS ha pubblicato v0.3.0, un traguardo importante che si espande da Linux-only a Linux, macOS, Windows e OpenWrt. I nodi ora pubblicano annunci overlay firmati come eventi parametrizzati sostituibili kind:37195 sui relay Nostr pubblici. Lo stesso swap ChaCha20-Poly1305 di ring 0.17 che ha alimentato il salto di throughput di Nostr VPN è presente anche in FIPS v0.3.0.

### Camelus v1.10.1 pubblica versioni desktop

Camelus ha pubblicato v1.10.1 con versioni desktop per Windows e Linux, espandendo la distribuzione oltre il solo mobile.

### Flotilla 1.8.0 pubblica videochiamate, rendering email e menzioni di stanza

Flotilla ha pubblicato 1.8.0. Le stanze vocali ora supportano il video: i partecipanti possono attivare le telecamere o condividere il proprio schermo durante una chiamata. Il rendering email arriva tramite un aggiornamento alla libreria welshman. Le menzioni di stanza consentono agli utenti di fare riferimento ad altre stanze e relay con link inline cliccabili.

### Calendar by Formstr pubblica v1.5.1 con pianificazione degli appuntamenti e sincronizzazione del calendario Android

Calendar by Formstr ha pubblicato v1.5.0 il 10 maggio e v1.5.1 l'11 maggio. La pianificazione degli appuntamenti consente agli utenti di creare slot temporali prenotabili. L'integrazione del calendario Android in sola lettura sincronizza gli eventi Nostr con il calendario del dispositivo.

## In sviluppo

### Amethyst aggiunge post programmati, regole di comunità NIP-9A e un relay locale desktop

Amethyst ha integrato 78 PR questa settimana. I post programmati arrivano in PR #2765. Una versione desktop acquisisce un relay locale integrato con persistenza degli eventi SQLite in PR #2841. Tre PR implementano le regole di comunità NIP-9A: PR #2798 valida i post rispetto alle regole di comunità prima dell'invio, PR #2799 aggiunge un editor di regole NIP-9A strutturato, e PR #2800 aggiunge un filtro di feed NIP-9A opzionale.

### Shopstr aggiunge la registrazione degli audit MCP e la sicurezza delle sessioni

Shopstr ha integrato cinque PR. La registrazione degli audit per il livello di strumenti MCP arriva in PR #456. La sicurezza delle sessioni si rafforza in PR #477 con il pinning delle sessioni alla chiave API di origine e l'espulsione TTL.

### Dart NDK aggiunge il supporto web e la verifica delle firme dei sigilli

Dart NDK ha integrato sei PR. Il supporto web arriva in SembastCacheManager tramite PR #571. La verifica delle firme dei sigilli arriva in PR #595 per il flusso NIP-59 Gift Wrap.

## Nuovi progetti

### Tamagostrich lancia un Tamagotchi NIP-78 decentralizzato con ricompense in sats

Tamagostrich è un gioco di animale virtuale nel browser lanciato all'IDENTITY Hackathon 2026 dove un piccolo struzzo, Nori, si evolve attraverso la tua attività sociale Nostr. Lo stato dell'animale è memorizzato in un evento NIP-78 kind:30078 per la sincronizzazione multi-dispositivo. Le ricompense ai traguardi vengono pagate in sats tramite NIP-47: 50 sats al livello 5, 210 sats al livello 10 e 420 sats al livello massimo 21, inviati all'indirizzo lud16 dell'utente.

## Lavori su protocollo e specifiche

Cinque nuove proposte sono state aperte questa settimana:

PR #2331 propone NIP-9A: Regole di Comunità Verificabili, introducendo kind:34551 per documenti di regole di comunità leggibili da macchina e firmati crittograficamente.

PR #2335 propone gli Eventi di Prenotazione per i Marketplace Nostr, definendo kind:32122 (eventi di prenotazione parametrizzati sostituibili), kind:1326 (record di audit delle transizioni solo in aggiunta) e kind:32124 (recensioni post-transazione). La negoziazione è privata tramite messaggi gift-wrapped NIP-59.

PR #2334 propone i Servizi di Escrow per i Marketplace Nostr usando kind:30303 affinché gli operatori di escrow dichiarino il loro indirizzo di contratto EVM e il listino tariffe.

PR #2333 propone i Profili di Annuncio di Alloggio per gli Annunci del Marketplace NIP-99, estendendo NIP-99 con tag g di indice geospaziale H3 per gli annunci di affitto a breve termine.

PR #2332 propone NIP-BC: Zap On-chain (kind 8333), sfruttando l'identità diretta tra le chiavi Nostr e gli indirizzi Bitcoin Taproot. Il numero di kind rispecchia NIP-57: 9735 è la porta P2P di Lightning; 8333 è la porta P2P della mainnet Bitcoin.

## Approfondimento NIP: NIP-78 (dati specifici dell'app)

NIP-78 definisce un metodo standard con cui le applicazioni memorizzano dati arbitrari privati o pubblici per conto di un utente tramite eventi Nostr. Il tipo di evento centrale è 30078, un evento parametrizzato sostituibile in cui il tag d è una stringa identificatore definita dall'applicazione. Un'applicazione assegna al proprio slot di storage un tag d univoco e pubblica un evento 30078 con qualsiasi contenuto JSON o testo che deve persistere. La motivazione principale è la sincronizzazione multi-dispositivo senza un server centralizzato. Per i dati privati dell'applicazione, gli eventi NIP-78 possono cifrare il campo content usando NIP-44 prima della pubblicazione. Gli utenti attuali includono Tamagostrich (sincronizzazione dello stato dell'animale), Wisp (backup del portafoglio e impostazioni di sicurezza), NosPress (stato di orchestrazione CMS) e diverse implementazioni di sincronizzazione delle impostazioni dei client Nostr.

---

Fonti primarie:
- Specifica NIP-78: https://github.com/nostr-protocol/nips/blob/master/78.md
- Tamagostrich: https://github.com/Negr087/tamagostrich

Vedi anche: Liste NIP-51, Metadati elenco relay NIP-65

## Approfondimento NIP: NIP-98 (HTTP Auth)

NIP-98 definisce uno schema di autenticazione HTTP che consente alle coppie di chiavi Nostr di autorizzare richieste a server HTTP, eliminando nomi utente, password o token OAuth. Un client costruisce un evento Nostr di breve durata di kind 27235, lo firma con la propria chiave privata, codifica il JSON in base64 e lo invia in un header HTTP Authorization: Nostr <base64>. L'evento kind 27235 include il metodo HTTP in un tag method, l'URL completo della richiesta in un tag u e un timestamp created_at. Il server valida la firma, verifica che metodo e URL corrispondano e controlla che il timestamp sia recente per prevenire gli attacchi di replay. NIP-98 è usato in Blossom (BUD-01) per l'autenticazione dell'upload dei blob, Routstr per il controllo degli accessi API per richiesta, Sprout per l'autenticazione del trasporto git e Alby Hub per l'autenticazione dell'API admin.

---

Fonti primarie:
- Specifica NIP-98: https://github.com/nostr-protocol/nips/blob/master/98.md
- BUD-01: https://github.com/hzrd149/blossom/blob/master/buds/01.md

Vedi anche: Integrazione archiviazione file HTTP NIP-96

---

È tutto per questa settimana. Se state costruendo qualcosa o avete notizie da condividere, inviateci un DM su Nostr o trovateci su nostrcompass.org.
