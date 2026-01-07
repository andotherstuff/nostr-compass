---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Bentornati su Nostr Compass, la vostra guida settimanale all'ecosistema del protocollo Nostr.

**Questa settimana:** Primal Android implementa la firma remota [NIP-46](/it/topics/nip-46/) e il supporto per signer locali [NIP-55](/it/topics/nip-55/), trasformandosi in un hub di firma completo per altre app Android. Il team del [Marmot Protocol](/it/topics/marmot/) ha affrontato le problematiche emerse da un audit di sicurezza con 18 PR integrate che rafforzano la messaggistica crittografata basata su [MLS](/it/topics/mls/). Citrine raggiunge la v1.0 e Applesauce rilascia la v5.0 per l'intera suite di librerie. TENEX sviluppa la supervisione di agenti AI su Nostr, e Jumble aggiunge il pooling intelligente dei relay. Una correzione alla specifica NIP-55 chiarisce i campi di ritorno di `nip44_encrypt`, e una PR per [NIP-50](/it/topics/nip-50/) propone estensioni per espressioni di query per ricerche avanzate. Nel nostro approfondimento, spieghiamo [NIP-04](/it/topics/nip-04/) e [NIP-44](/it/topics/nip-44/): perché la crittografia legacy presenta falle di sicurezza e come la sostituzione moderna le risolve.

## Notizie

**Primal Android diventa un Hub di Firma Completo** - La [Versione 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) aggiunge sia la firma remota [NIP-46](/it/topics/nip-46/) che la firma locale [NIP-55](/it/topics/nip-55/), trasformando Primal in un signer completo per altre app Nostr. La firma remota tramite NIP-46 permette agli utenti di connettersi a servizi bunker attraverso i relay Nostr, mantenendo le chiavi completamente fuori dal dispositivo. La firma locale tramite NIP-55 espone Primal come content provider Android, così app come Amethyst o Citrine possono richiedere firme senza mai toccare la chiave privata. [Diverse PR successive](https://github.com/PrimalHQ/primal-android-app/pull/839) hanno risolto problemi di compatibilità con il requisito della specifica NIP-55 per pubkey esadecimali, e migliorato il parsing di URI `nostrconnect://` malformati. Il rilascio include anche pre-caching dei media per uno scorrimento più fluido, tempi di caricamento dei thread migliorati e pre-caching degli avatar.

**Marmot Protocol rafforza la sicurezza dopo l'Audit** - Il [Marmot Development Kit](https://github.com/marmot-protocol/mdk) (mdk), che implementa la messaggistica end-to-end crittografata basata su [NIP-104](/it/topics/nip-104/) MLS, ha ricevuto ampie correzioni di sicurezza questa settimana. Diciotto pull request integrate hanno affrontato le problematiche dell'audit tra cui: [verifica hash per immagini di gruppo crittografate](https://github.com/marmot-protocol/mdk/pull/97) per prevenire attacchi di sostituzione blob a livello storage, [paginazione per welcome pendenti](https://github.com/marmot-protocol/mdk/pull/110) per prevenire esaurimento della memoria, [perdita di MLS Group ID nei messaggi di errore](https://github.com/marmot-protocol/mdk/pull/112), e [applicazione della codifica base64](https://github.com/marmot-protocol/mdk/pull/98) per i key package. La [specifica Marmot stessa è stata aggiornata](https://github.com/marmot-protocol/marmot/pull/20) con MIP-04 v2 versioning e miglioramenti di sicurezza. PR attive continuano ad affrontare riuso di nonce, azzeramento dei segreti e vettori di inquinamento della cache.

**Nostrability traccia il supporto Relay Hint** - Un nuovo [tracker di compatibilità relay hints](https://github.com/nostrability/nostrability/issues/270) documenta come i client costruiscono e consumano relay hint nell'ecosistema. Il tracker rivela che mentre la maggior parte dei client ora costruisce hint secondo [NIP-10](/it/topics/nip-10/) e [NIP-19](/it/topics/nip-19/), il consumo varia ampiamente: alcuni client includono hint negli eventi in uscita ma non usano gli hint in entrata per il recupero. Sei client hanno ottenuto lo status "Full" per implementazione completa. Il tracker è utile per sviluppatori che verificano l'interoperabilità e per utenti che si chiedono perché alcuni client trovano contenuti che altri non riescono a trovare.

**Nostria 2.0 rilascia revisione completa delle funzionalità Cross-Platform** - Il client [Nostria](https://nostria.app) [ha rilasciato la versione 2.0](https://njump.me/nevent1qqs9z4l8z82zphszjlmrjkr8whpvupnlaxc7xk5gfg9syzj0thygtzgpz4mhxue69uhhyetvv9ujuerpd46hxtnfduhszxthwden5te0wfjkccte9enrw73wd9hsz9nhwden5te0wfjkccte9ec8y6tdv9kzumn9wsq3gamnwvaz7tmjv4kxz7fwv3sk6atn9e5k7qgkwaehxw309aex2mrp0yhxgctdw4eju6t09uq32amnwvaz7tmwdaejumr0dshsz9mhwden5te0wfjkccte9ec82c30989ksmfnv9kzumn9wshsqgzxsnsv7pfqqd7rw4fvr0jnkpqmwzfqq3znlc4pqunagxrkl84u66y7fq9) il 30 dicembre con aggiunte significative su iOS (TestFlight), Android (Play Store), Web e Windows. Il rilascio aggiunge supporto nativo per la musica con creazione di playlist, caricamento di tracce, pagamenti agli artisti basati su zap, e un player in stile WinAmp con equalizzatore funzionante. Lo streaming live ottiene l'integrazione Game API che mostra metadati ricchi durante gli streaming di gameplay. Una nuova funzione Summary genera digest di attività orari, giornalieri o settimanali come viste timeline compresse. La sezione Discover offre liste curate per trovare contenuti e profili. La pubblicazione di media è semplificata con generazione automatica di post short-form per la scoperta cross-client. Le connessioni ai signer remoti ora funzionano tramite scansione di codici QR senza configurazione manuale. La scoperta dei profili affronta un problema comune di Nostr: quando gli utenti si spostano tra relay senza portare i propri metadati, Nostria localizza il loro profilo e lo ripubblica sui relay correnti. Gli abbonati Premium ottengono integrazione con canali YouTube, Memo privati, dashboard analitiche e backup automatici delle liste di following con opzioni di merge/restore.

## Aggiornamenti NIP

Modifiche recenti al [repository NIPs](https://github.com/nostr-protocol/nips):

**Integrate:**
- **[NIP-55](/it/topics/nip-55/)** - Corretto il campo di ritorno per il metodo `nip44_encrypt` ([#2184](https://github.com/nostr-protocol/nips/pull/2184)). I signer Android devono ora restituire il payload crittografato nel campo `signature` (come `nip44_decrypt`) invece che in un campo separato. Questo allinea la specifica con le implementazioni esistenti in Amber e Primal.

**PR Aperte:**
- **[NIP-50](/it/topics/nip-50/)** - Estensioni Espressioni di Query ([#2182](https://github.com/nostr-protocol/nips/pull/2182)) propone di estendere la ricerca NIP-50 con espressioni di query strutturate. La PR aggiunge operatori come `kind:1`, `author:npub1...`, e combinazioni booleane (`AND`, `OR`, `NOT`), abilitando query di ricerca più precise oltre il semplice matching testuale. Questo permetterebbe ai client di costruire interfacce di ricerca avanzate mantenendo la retrocompatibilità con stringhe di ricerca base.

## Approfondimento NIP: NIP-04 e NIP-44

Questa settimana copriamo gli standard di crittografia Nostr: il legacy NIP-04 che incontrerete ancora, e la sua sostituzione moderna NIP-44 che corregge falle di sicurezza critiche.

### [NIP-04](/it/topics/nip-04/): Messaggi Diretti Crittografati (Legacy)

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md) è stato il primo tentativo di Nostr per la messaggistica crittografata, usando eventi di kind 4. Sebbene semplice da implementare, ha debolezze di sicurezza note ed è deprecato in favore di NIP-44.

**Come funziona:** NIP-04 usa ECDH (Elliptic Curve Diffie-Hellman) per derivare un segreto condiviso tra mittente e destinatario, poi crittografa con AES-256-CBC.

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

Il flusso di crittografia:
1. Calcola il punto condiviso: `shared = ECDH(sender_privkey, recipient_pubkey)`
2. Deriva la chiave: `key = SHA256(shared_x_coordinate)`
3. Genera IV casuale di 16 byte
4. Crittografa: `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. Formatta il contenuto: `base64(ciphertext)?iv=base64(iv)`

**Problemi di sicurezza:**

- **Nessuna autenticazione:** AES-CBC fornisce confidenzialità ma non integrità. Un attaccante che controlla un relay potrebbe modificare bit del ciphertext, causando modifiche prevedibili al plaintext (attacchi bit-flipping).
- **IV in chiaro:** Il vettore di inizializzazione è trasmesso insieme al ciphertext, e la modalità CBC con IV prevedibili abilita attacchi chosen-plaintext.
- **Nessuna validazione del padding:** Le implementazioni variano nel modo in cui gestiscono il padding PKCS#7, potenzialmente abilitando attacchi padding oracle.
- **Esposizione dei metadati:** La pubkey del mittente, la pubkey del destinatario e il timestamp sono tutti visibili ai relay.
- **Riuso della chiave:** Lo stesso segreto condiviso è usato per tutti i messaggi tra due parti, per sempre.

**Perché esiste ancora:** Molti client e relay più vecchi supportano solo NIP-04. Lo incontrerete quando interagite con sistemi legacy. Signer come Amber e app come Primal implementano ancora `nip04_encrypt`/`nip04_decrypt` per retrocompatibilità.

### [NIP-44](/it/topics/nip-44/): Crittografia Versionata

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) è lo standard di crittografia moderno, progettato per correggere le falle note di NIP-04. Un audit di sicurezza Cure53 delle implementazioni NIP-44 ha identificato 10 problemi (inclusi attacchi temporali e preoccupazioni sulla forward secrecy) che sono stati affrontati prima della finalizzazione della specifica. Usa ChaCha20-Poly1305 con derivazione di chiave appropriata e crittografia autenticata.

**Miglioramenti chiave rispetto a NIP-04:**

| Aspetto          | NIP-04                     | NIP-44                  |
|:-----------------|:---------------------------|:------------------------|
| Cifrario         | AES-256-CBC                | XChaCha20-Poly1305      |
| Autenticazione   | Nessuna                    | Poly1305 MAC            |
| Derivazione chiave | SHA256(shared_x)         | HKDF con salt           |
| Nonce            | IV 16 byte, pattern riusato | Nonce casuale 24 byte  |
| Padding          | PKCS#7 (rivela lunghezza)  | Arrotondato a potenza di 2 |
| Versionamento    | Nessuno                    | Prefisso byte versione  |

**Flusso di crittografia:**

1. **Chiave di conversazione:** Deriva una chiave stabile per ogni coppia mittente-destinatario:
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **Chiavi del messaggio:** Per ogni messaggio, genera un nonce casuale di 32 byte e deriva chiavi di crittografia/autenticazione:
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **Padding del plaintext:** Arrotonda alla prossima potenza di 2 (minimo 32 byte) per nascondere la lunghezza del messaggio:
   ```
   padded = [length_u16_be] + [plaintext] + [zeri fino alla prossima potenza di 2]
   ```

4. **Crittografa e autentica:**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **Formatta il payload:**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**Byte di versione:** Il primo byte (`0x02`) indica la versione di crittografia. Questo permette upgrade futuri senza compromettere i messaggi esistenti. La versione `0x01` era una bozza precedente mai ampiamente distribuita.

**Decrittografia:**

1. Decodifica base64, verifica che il byte di versione sia `0x02`
2. Estrai nonce (byte 1-32), ciphertext e MAC (ultimi 32 byte)
3. Deriva la chiave di conversazione usando la chiave privata del destinatario e la chiave pubblica del mittente
4. Deriva le chiavi del messaggio dalla chiave di conversazione e dal nonce
5. Verifica il MAC prima di decrittografare (rifiuta se non valido)
6. Decrittografa il ciphertext, estrai il prefisso di lunghezza, restituisci il plaintext senza padding

**Proprietà di sicurezza:**

- **Crittografia autenticata:** Il MAC Poly1305 assicura che qualsiasi manomissione sia rilevata prima della decrittografia
- **Forward secrecy (parziale):** Ogni messaggio usa un nonce unico, quindi compromettere un messaggio non rivela gli altri. Tuttavia, compromettere una chiave privata rivela comunque tutti i messaggi passati (nessun ratcheting).
- **Occultamento della lunghezza:** Il padding a potenza di 2 oscura la lunghezza esatta del messaggio
- **Resistenza agli attacchi temporali:** Confronto a tempo costante per la verifica del MAC

**Uso pratico:** NIP-44 è il livello di crittografia per:
- [NIP-17](/it/topics/nip-17/) messaggi diretti privati (dentro gift wrap)
- [NIP-46](/it/topics/nip-46/) comunicazione con signer remoti
- [NIP-59](/it/topics/nip-59/) crittografia seal
- [Marmot Protocol](/it/topics/nip-104/) messaggi di gruppo, dove NIP-44 avvolge contenuto crittografato MLS usando una chiave derivata dal segreto esportatore MLS
- Qualsiasi applicazione che necessita crittografia sicura punto-a-punto

**Guida alla migrazione:** Le nuove applicazioni dovrebbero usare esclusivamente NIP-44. Per retrocompatibilità, verificate se il client del contatto supporta NIP-44 (tramite metadati app [NIP-89](/it/topics/nip-89/) o supporto relay) prima di ricadere su NIP-04. Quando ricevete messaggi, tentate prima la decrittografia NIP-44, poi ricadete su NIP-04 per contenuti legacy.

## Rilasci

**Primal Android v2.6.18** - Il [rilascio completo](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) aggiunge firma remota [NIP-46](/it/topics/nip-46/) e firma locale [NIP-55](/it/topics/nip-55/), trasformando Primal in un hub di firma per altre app Android. I miglioramenti delle prestazioni includono pre-caching dei media, pre-caching degli avatar e caricamento più veloce dei thread. Le correzioni di bug affrontano auto-menzioni nelle bio, crash nella galleria media e fallback dei titoli degli stream. Su iOS, Primal usa la riproduzione audio in background per mantenere l'app attiva per ricevere richieste di firma NIP-46; gli utenti possono cambiare il suono o silenziarlo completamente nelle impostazioni.

**Mostro v0.15.6** - L'[ultimo rilascio](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6) del bot di trading P2P Bitcoin [NIP-69](/it/topics/nip-69/) completa l'implementazione del fondo di sviluppo con gli eventi di audit della Fase 4. I pagamenti delle commissioni dev sono ora tracciati tramite eventi Nostr kind 38383 pubblicati dopo ogni pagamento riuscito, abilitando verifica e analytics di terze parti. I calcoli degli importi sono stati corretti per i messaggi acquirente/venditore, e la logica del premium è stata allineata con l'implementazione di riferimento lnp2pbot.

**Aegis v0.3.5** - Il signer cross-platform [aggiunge la modalità scura](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5), visualizzazione migliorata delle icone app e layout UI più puliti. Le correzioni di bug affrontano conflitti iOS iCloud Private Relay e problemi di parsing degli eventi. Il rilascio migliora anche come il JSON degli eventi viene passato alla funzione di firma Rust.

**Citrine v1.0.0** - L'app relay Android [raggiunge la 1.0](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0). Citrine permette di eseguire un relay Nostr personale direttamente sul dispositivo Android, utile per caching locale, backup o come companion NIP-55. Questo rilascio aggiunge un gestore di crash report, migliora l'efficienza delle query database e aggiorna le traduzioni tramite Crowdin.

**Applesauce v5.0.0** - La suite di librerie TypeScript di hzrd149 [rilascia una major version](https://github.com/hzrd149/applesauce/releases) con breaking changes focalizzati su correttezza e semplicità. Il pacchetto core ora [verifica le firme degli eventi per default](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0) e rinomina i metodi coordinate per usare terminologia "address" più chiara (`parseCoordinate` -> `parseReplaceableAddress`). Il pacchetto relay [abbassa i retry di default da 10 a 3](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0) e ignora i relay irraggiungibili per default, più aggiunge `createUnifiedEventLoader` per un recupero eventi più semplice. Il pacchetto wallet ottiene la [scoperta mint Cashu](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0) [NIP-87](/it/topics/nip-87/). Le dipendenze dirette da `nostr-tools` sono state rimosse dai pacchetti, riducendo dimensione del bundle e conflitti di versione.

## Modifiche notevoli a codice e documentazione

*Queste sono pull request aperte e lavori in fase iniziale, perfetti per ricevere feedback prima del merge. Se qualcosa vi interessa, considerate di revisionare o commentare!*

### Damus (iOS)

Una serie di PR migliorano l'esperienza degli articoli longform. [Miglioramenti UX di lettura](https://github.com/damus-io/damus/pull/3496) aggiungono una barra di progresso, tempo di lettura stimato, modalità seppia, altezza delle righe regolabile e modalità focus che nasconde la navigazione durante lo scorrimento. [Correzioni immagini](https://github.com/damus-io/damus/pull/3489) assicurano che le immagini nel contenuto markdown vengano visualizzate con proporzioni corrette preprocessando le immagini standalone come elementi block-level. [Card anteprima longform](https://github.com/damus-io/damus/pull/3497) sostituiscono il testo inline `@naddr1...` con card di anteprima ricche che mostrano titolo dell'articolo e metadati. Una nuova [suite di test di integrazione relay](https://github.com/damus-io/damus/pull/3508) aggiunge 137 test relativi alla rete inclusa verifica protocollo [NIP-01](/it/topics/nip-01/) e comportamento in condizioni di rete degradate (simulazione 3G).

### Bitchat (Messaggistica Crittografata)

Rafforzamento della sicurezza nel messenger iOS Nostr+Cashu. [Pulizia segreti DH protocollo Noise](https://github.com/permissionlesstech/bitchat/pull/928) corregge sei posizioni dove i segreti condivisi non venivano azzerati dopo l'accordo chiavi Diffie-Hellman, ripristinando le garanzie di forward secrecy. [Thread safety per code read receipt](https://github.com/permissionlesstech/bitchat/pull/929) aggiunge sincronizzazione barrier per prevenire race condition in NostrTransport. [Ottimizzazione deduplicatore messaggi](https://github.com/permissionlesstech/bitchat/pull/920) migliora le prestazioni con alti volumi di messaggi, e [rafforzamento parsing stringhe hex](https://github.com/permissionlesstech/bitchat/pull/919) previene crash da input malformato.

### Frostr (Firma a Soglia)

Il protocollo di firma a soglia basato su [FROST](/it/topics/frost/) [ha aggiunto visualizzazione codici QR](https://github.com/FROSTR-ORG/igloo-desktop/pull/62) per credenziali di gruppo e credenziali di share durante l'onboarding e nell'interfaccia signer. Questo abilita una configurazione più semplice quando si distribuiscono key share su dispositivi multipli, permettendo agli utenti di scansionare credenziali invece di copiare manualmente stringhe lunghe.

### Marmot mdk (Libreria)

Oltre alle correzioni di sicurezza menzionate sopra, PR attive affrontano i rimanenti risultati dell'audit: [Tipo Secret<T> per azzeramento](https://github.com/marmot-protocol/mdk/pull/109) introduce un tipo wrapper che azzera automaticamente i dati sensibili alla distruzione, [paginazione query messaggi](https://github.com/marmot-protocol/mdk/pull/111) previene esaurimento memoria durante il caricamento della cronologia chat, e [storage crittografato](https://github.com/marmot-protocol/mdk/pull/102) aggiunge crittografia a riposo per il database SQLite che memorizza stato di gruppo e messaggi.

### Amethyst (Android)

Una settimana intensa di correzioni di stabilità nel client Android. [Parsing JSON tollerante](https://github.com/vitorpamplona/amethyst/commit/2c42796) previene crash da eventi malformati rendendo Kotlin Serialization più permissiva. La validazione eventi ora [controlla la dimensione del campo kind](https://github.com/vitorpamplona/amethyst/commit/40f9622) prima dell'elaborazione per evitare eccezioni da valori sovradimensionati. La UI del trust score ha ottenuto un'icona più piccola per ridurre l'interferenza visiva, e [logging errori migliorato](https://github.com/vitorpamplona/amethyst/commit/69c53ac) aiuta a diagnosticare problemi di connessione ai relay. Aggiornamenti delle traduzioni sono arrivati tramite Crowdin, e diversi warning SonarQube sono stati affrontati.

### TENEX (Agenti AI)

Il framework di agenti AI nativo Nostr ha visto 81 commit questa settimana per costruire capacità autonome. Il nuovo [sistema di supervisione agenti](https://github.com/tenex-chat/tenex/pull/48) implementa euristiche comportamentali per monitorare le azioni degli agenti e intervenire quando necessario. [Trasparenza della delega](https://github.com/tenex-chat/tenex/commit/b244c10) aggiunge logging degli interventi utente alle trascrizioni di delega, così gli utenti possono verificare cosa hanno fatto gli agenti per loro conto. Il [registro provider LLM](https://github.com/tenex-chat/tenex/pull/47) è stato modularizzato per una più facile integrazione di diversi backend AI. Il supporto conversazioni cross-project permette agli agenti di mantenere il contesto attraverso multipli progetti basati su Nostr.

### Jumble (Client Web)

Il client web focalizzato sui relay ha aggiunto diversi miglioramenti all'esperienza utente. [Pool relay intelligente](https://github.com/CodyTseng/jumble/commit/695f2fe) gestisce intelligentemente le connessioni basandosi sui pattern di utilizzo. [Toggle feed live](https://github.com/CodyTseng/jumble/commit/917fcd9) permette agli utenti di passare tra streaming in tempo reale e refresh manuale. [Auto-mostra nuove note](https://github.com/CodyTseng/jumble/commit/d1b3a8c) in cima fa emergere contenuto fresco senza richiedere ricaricamento della pagina. [Cache persistente](https://github.com/CodyTseng/jumble/commit/fd9f41c) per feed following e notifiche migliora i tempi di caricamento alle visite successive. Gli utenti possono ora [cambiare i relay di default](https://github.com/CodyTseng/jumble/commit/53a67d8) attraverso le impostazioni.

---

Questo è tutto per questa settimana. State costruendo qualcosa? Avete notizie da condividere? Volete che copriamo il vostro progetto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contattateci via NIP-17 DM</a> o trovateci su Nostr.
