---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "Strumenti di identità post-quantum, messaggistica cifrata e firma più robuste, impostazioni comunitarie portabili e lavoro sul protocollo su NIP e Concord."
---

Bentornati su [Nostr Compass](https://nostrcompass.org), la vostra guida settimanale a Nostr.

**Questa settimana:** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) aggiunge chiavi post-quantum e messaggi protetti opt-in accanto alle identità Nostr esistenti. [Divine](https://github.com/divinevideo/divine-mobile) rafforza l'isolamento degli account, la validazione dei messaggi privati e la conferma di pubblicazione; [MDK](https://github.com/marmot-protocol/mdk) rafforza convergenza e recupero dei gruppi cifrati; e [Amber](https://github.com/greenart7c3/Amber) rende esplicite le decisioni di firma raggruppate. Le release migliorano connessioni ai wallet, chat cifrata, scoperta sociale, sincronizzazione tra dispositivi e firma remota, mentre il lavoro sul protocollo copre identità e comunità cifrate. Gli approfondimenti spiegano richieste di cancellazione autenticate e segnalazioni decentralizzate.

## Storie principali

### nostr-wot-extension 0.4.0 aggiunge chiavi post-quantum accanto a un'identità Nostr

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) è un'estensione del browser per gestire identità Nostr e firmare. Gli account creati da un seed a 24 parole possono ora derivare chiavi di crittografia ML-KEM-1024 e di firma ML-DSA-87 accanto alla chiave Nostr esistente. Un flusso con un clic pubblica un'attestazione di kind `10203` che lega la chiave pubblica Nostr a entrambe le chiavi pubbliche post-quantum e include una proof of possession ML-DSA. Gli account importati da un mnemonic a 12 parole, un `nsec` nudo, un firmatario remoto o una chiave read-only non possono usare il flusso di derivazione, e l'estensione spiega tale limitazione nella vista dell'account.

La release aggiunge anche messaggi diretti post-quantum opt-in. Combina il shared secret ML-KEM con la [chiave di conversazione del messaggio cifrato NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) esistente tramite HKDF, poi mantiene i normali strati gift-wrap NIP-59 per nascondere i metadati nella consegna via relay. La crittografia non ricade mai silenziosamente dopo che un destinatario ha optato, mentre la decrittazione seleziona automaticamente il percorso appropriato. Questo protegge il nuovo percorso dei messaggi contro un successivo recupero di una chiave privata Nostr odierna, ma non sostituisce le firme degli eventi secp256k1; la release lascia esplicitamente quella migrazione più ampia a un futuro coordinamento con relay e client.

### Divine Mobile 1.0.19 rafforza account, messaggi privati e pubblicazione

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) è un client mobile di video brevi che pubblica e recupera video tramite Nostr. Il selettore di account ora costruisce ogni identità connessa attorno a un container scoped per account, e una correzione alla pubblicazione impedisce che un video venga inviato sotto l'account sbagliato. I percorsi di pubblicazione sui relay attendono ora una risposta `OK` con semantica di successo esplicita, mentre un frame relay `CLOSED` può terminare la propria query in sospeso invece di lasciare la richiesta appesa.

La [gestione dei messaggi privati](https://github.com/divinevideo/divine-mobile/pull/6368) rifiuta campi rumor non autenticati e seal non firmati, ripristina quattro casi di messaggi mancanti e instrada le conversazioni di gruppo da partecipanti completamente seguiti nella inbox. La release preserva anche i tag sugli eventi video indirizzabili quando le liste vengono aggiornate e consuma le richieste di cancellazione osservate così che i video rimossi scompaiano dallo stato locale. Queste modifiche seguono il lavoro sui timeout per query per relay trattato la scorsa settimana, ma spostano il focus dall'isolamento del recupero ai confini dell'identità, alla validazione dei messaggi e alla conferma di pubblicazione.

### MDK 0.9.11 rafforza convergenza e recupero dei gruppi Marmot

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) è un kit di sviluppo Rust per Marmot, un protocollo di messaggistica di gruppo cifrata trasportato su Nostr. La release costruisce un sistema più ampio di convergenza e recupero attorno alla macchina a stati del gruppo: i passaggi di convergenza obsoleti si riaprono alla punta corrente del gruppo, le proiezioni delle capability in ingresso vengono committate atomicamente, i messaggi differiti ricevono durate di vita limitate tra i riavvii, e i checkpoint indirizzati per commit aiutano a recuperare i fork di commit propri di un'identità. Gli invii non stabili possono essere accodati e recuperati, mentre un percorso di stallo dell'epoca scala verso backfill e i messaggi inviati sopravvivono al lavoro di convergenza.

[Storage e integrazioni host](https://github.com/marmot-protocol/mdk/pull/1201) ricevono un passaggio parallelo di hardening. MDK elimina in modo sicuro le proiezioni SQLite potate, azzera le chiavi private importate, gli intermedi di export delle chiavi cifrate NIP-49 e i buffer di serializzazione OpenMLS, e redige le chiavi delle immagini di gruppo dall'output di debug. L'import dell'account può riprendere dopo un'interruzione, i percorsi di storage privato iOS e Android sono riparati, e gli host possono chiudere esplicitamente lo storage prima della sospensione. Nuove proiezioni leggere del roster e dell'appartenenza locale riducono ciò che le applicazioni devono leggere, mentre il connettore Hermes può consegnare diverse immagini generate da agent come un unico album Marmot.

### Nostria 4.1.67 espande l'amministrazione delle comunità cifrate

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) è un client social web e desktop per Nostr. Si basa sui gruppi sperimentali [NIP-29](/it/topics/nip-29/) (gruppi gestiti da relay) e sulle comunità cifrate Concord introdotti in 4.1.53, aggiungendo scioglimento della comunità, amministrazione di icona e banner, caricamenti di foto cifrati con anteprime compresse, un selettore completo di reazioni e un layout a doppio pannello che mantiene aperta una comunità mentre l'utente legge note o articoli. La release aggiunge anche messaggistica in thread e un hub combinato per chat pubbliche, di gruppo e private.

### Amber 6.4.0 rende esplicita ogni decisione di firma raggruppata

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) è un firmatario Android che mantiene le chiavi private Nostr separate dalle applicazioni che richiedono firme. La sua schermata multi-richiesta ridisegnata fornisce controlli Approva e Nega per ogni richiesta e ogni gruppo, sostituendo il precedente flusso di selezione e conferma. Le richieste negate inviate tramite l'interfaccia bunker mediata da relay di Amber ricevono ora risposte di errore corrette, così il client richiedente può distinguere un rifiuto da un firmatario bloccato.

Il [codice sorgente taggato di Amber](https://github.com/greenart7c3/Amber/tree/v6.4.0) aggiunge anche etichette localizzate e leggibili per altri 113 kind di evento in ogni locale distribuito. Le aggiunte includono eventi di gruppo Concord, segnalibri di repository Git [NIP-51](/it/topics/nip-51/) (liste e insiemi curati) ed eventi di presenza in stanza [NIP-53](/it/topics/nip-53/) (attività live), dando agli utenti più contesto su dati non familiari prima di approvare una firma. Una guardia concurrent-map corregge anche un crash di sottoscrizione ai relay che poteva produrre un `NegativeArraySizeException`.

### Safebox Acorn separa un componente di recupero portatile dall'app web

[Safebox Acorn](https://github.com/trbouma/safebox-acorn) è un componente Python autonomo e un'interfaccia a riga di comando per proteggere chiavi, fondi e record controllati dall'utente tramite stato supportato da Nostr. L'estrazione di Acorn dalla più ampia applicazione web Safebox consente a un altro progetto Python di installare il runtime e usare i suoi helper per chiavi, profili Nostr, relay, record, Cashu, Lightning e crittografia senza adottare l'interfaccia web. Le attuali primitive di protezione dei record possono generare una nuova chiave a 256 bit, derivarne una da entropia fornita separatamente e codificare la chiave esatta come frase di recupero di 24 parole con checksum.

La [guida al recupero e alla continuità](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) del progetto presenta Acorn come componente di protocollo sostituibile all'interno di una Safebox domestica o comunitaria. Il design mantiene lo stato cifrato disponibile tramite un relay locale e repliche indipendenti, così il recupero non dipende da un singolo dispositivo, applicazione, relay, mint o fornitore di servizi. La documentazione chiarisce con attenzione il limite attuale: la cifratura dei record protetti è ancora in fase di progettazione, quindi le applicazioni non dovrebbero far dipendere i record dalla nuova chiave di protezione finché quel profilo non sarà implementato e sottoposto a revisione.


## Rilasci taggati

### Mostro Core 0.14.2 cambia l'envelope della chat cifrata

[Mostro Core](https://github.com/MostroP2P/mostro-core) è la libreria Rust di tipi condivisi e funzioni peer-to-peer usata dal daemon di scambio Mostro e dai suoi client. La [versione 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) sostituisce i messaggi di chat gift-wrap con envelope di kind 14 che usano chiavi separate di crittografia della conversazione e di firma derivate dal shared secret dei peer. Il nuovo reader valida autore, firma, destinatario, timestamp e dimensione del contenuto, mentre gli helper gift-wrap legacy restano disponibili così i client possono leggere entrambi i formati durante la migrazione.

### Mostro 0.18.1 avvia un percorso escrow Cashu e rafforza il daemon

[Mostro](https://github.com/MostroP2P/mostro) è un daemon di scambio Lightning peer-to-peer che coordina gli ordini tramite Nostr. La [versione 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1) getta le basi per un backend escrow Cashu, inclusi configurazione, helper del database, integrazione con mint, wiring all'avvio e la prima azione di lock. Può anche usare prezzi annunciati da un nodo fidato su Nostr e pubblica requisiti di proof-of-work per il primo contatto nel suo evento info sostituibile. La release aggiorna la dipendenza Nostr per una correzione denial-of-service NIP-44, rimuove le chiavi private dai log di restore-session, rifiuta messaggi di cooperative-cancel non autorizzati, rafforza i fetch LNURL contro server-side request forgery e hang, valida le invoice di payout e ripristina le sottoscrizioni alle hold invoice dopo un riavvio.

### LaWallet NWC 2.3.0 aggiunge notifiche Nostr e ricevute zap

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) è una piattaforma Lightning Address open-source che collega i wallet tramite [Nostr Wallet Connect](/it/topics/nip-47/) (NIP-47). La [versione 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) permette a ogni wallet di inviare notifiche di ricezione e inoltro come eventi Nostr configurabili, inclusi un tag destinatario `p`, relay selezionati, contenuto templato e crittografia opzionale [NIP-44](/it/topics/nip-44/) (crittografia versionata); i tentativi riusano lo stesso ID evento firmato. Accetta anche zap request e pubblica ricevute firmate [NIP-57](/it/topics/nip-57/) (zap) di kind 9735 dopo il regolamento, mentre una nuova vista delle capability dell'indirizzo mostra se l'indirizzo risolto supporta NIP-05, NIP-57 e i protocolli Lightning Address correlati.

### nostr-double-ratchet TypeScript 0.0.166 lega inviti pubblici alle chiavi di sessione

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) fornisce primitive TypeScript e Rust per messaggistica diretta e di gruppo cifrata end-to-end su relay Nostr. [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) richiede che una risposta a un invito dimostri la proprietà della sua chiave di sessione, impedendo a un invito pubblico riutilizzabile di legare un'identità Nostr alla sessione di un'altra parte. La release rifiuta anche campi rumor malformati e rafforza la validazione del payload; le sessioni esistenti continuano a funzionare, ma un invitante aggiornato rifiuta risposte senza prova da invitati più vecchi.

### cln-nip47 0.2.0 espande e isola le richieste NWC

[cln-nip47](https://github.com/daywalker90/cln-nip47) è un plugin Core Lightning che espone un nodo ai wallet tramite [Nostr Wallet Connect](/it/topics/nip-47/) (NIP-47). La [versione 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) aggiunge metodi NWC per creare, annullare e regolare hold invoice più una notifica `hold_invoice_accepted`, e pubblica l'insieme di metodi che il nodo connesso supporta effettivamente. Le risposte transaction-list si fermano ora a 500 voci e circa 128 kB, gli eventi di richiesta vengono deduplicati per ID evento, e la notifica fallita di un client non impedisce più la consegna agli altri client. La release rimuove anche i due metodi multi-payment che non fanno più parte della specifica NWC.

### ClipRelay 0.1.3 ripristina connessioni a relay e firmatario dopo periodi di inattività

[ClipRelay](https://github.com/tajava2006/cliprelay) sincronizza gli appunti di un utente tra dispositivi tramite relay Nostr, cifrando il contenuto verso la stessa identità con [NIP-44](/it/topics/nip-44/) (crittografia versionata). Le release [desktop](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) e [Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3 corrispondenti aggiungono una casella di testo per inviare testo digitato direttamente agli appunti di un altro dispositivo. Testano anche la liveness con round trip reali sui relay dopo periodi di inattività, escalando da risottoscrizione a sostituzione del socket e a un pool di connessioni ricostruito, mentre le chiamate al firmatario [NIP-46](/it/topics/nip-46/) (firma remota mediata da relay) bloccate ora scadono e si ricostruiscono automaticamente.

### NoorNote 1.3.2 sposta la scoperta degli articoli nel grafo sociale

[NoorNote](https://github.com/77elements/noornote) è un client Nostr per post social, messaggi cifrati, articoli in formato lungo e altri kind di evento su web, desktop e Android. La [versione 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) sostituisce il feed globale piatto degli articoli con una scoperta tratta da contatti di primo, secondo e terzo grado, offrendo ai lettori una timeline di articoli radicata nel grafo dei follow. Collassa anche raffiche di messaggi diretti riprodotti da mittenti sconosciuti in un'unica notifica continua invece di produrre una pila di toast man mano che arriva la cronologia dei relay.


### Bray 2.4.0 aggiunge un dialetto compatto di firma remota

[Bray](https://github.com/forgesworn/bray) è un server MCP Nostr che offre ad agenti software e persone strumenti per accesso ai relay, identità, pubblicazione e firma remota. La [versione 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) accetta una richiesta di firma il cui evento è un oggetto oltre alla forma stringificata usata da [NIP-46](/it/topics/nip-46/) (firma remota mediata da relay), e aggiunge `sign_event_compact`, che restituisce solo ID evento, firma, chiave pubblica e timestamp. Quel formato più piccolo di richiesta e risposta riduce l'uso di memoria per firmatari hardware vincolati, mentre il flusso standard `sign_event` resta invariato e entrambi i dialetti producono una firma sull'ID dell'evento ricevuto.


## Appena scoperti

### Pact porta legami tra agenti con consenso reciproco su Nostr

[Pact](https://github.com/bobodread876/pact), scoperto questa settimana, è uno strato relazionale in fase iniziale per agenti software costruito su MATE.md e su una bozza di trasporto NIP-BD. I suoi legami firmati con consenso reciproco sono detenuti dalle chiavi degli agenti stessi e possono essere pubblicati su Nostr, mentre i legami privati usano il gift wrapping [NIP-59](/it/topics/nip-59/) (metadati nascosti). Il monorepo include un server MCP, SDK TypeScript, client da riga di comando, daemon self-hostable e interfaccia web. La sua attività più recente nel repository precede la finestra settimanale di questo numero, quindi questa è una nota di scoperta e non l'affermazione di una nuova release.


## Modifiche non rilasciate

### nostrord mantiene sincronizzato il muting di gruppo tra dispositivi

[nostrord](https://github.com/nostrord/nostrord) è un client multipiattaforma per comunità gestite da relay. La [PR #250](https://github.com/nostrord/nostrord/pull/250) memorizza le scelte di mute per gruppo di ogni account in un evento [NIP-78](/it/topics/nip-78/) (dati specifici dell'applicazione) di kind `30078` auto-cifrato, così un'impostazione fatta su un dispositivo può seguire l'utente su un altro senza rivelare la lista dei gruppi al relay. Il record sostituibile usa l'ordinamento per evento più recente, ascolta le modifiche in tempo reale e ripristina l'interfaccia quando la firma o la pubblicazione falliscono invece di lasciare lo stato locale fuori sync. I gruppi mutati smettono anche di contribuire ai totali non letti visibili mantenendo la posizione non letta per la visita successiva.

### Amethyst completa il ciclo di vita degli inviti Concord

[Amethyst](https://github.com/vitorpamplona/amethyst) è un client Nostr Android il cui supporto alle comunità cifrate implementa il protocollo Concord. La [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) permette ai link di invito di sopravvivere a un refounding della comunità riemettendo i bundle alle stesse coordinate indirizzabili, mentre un controllo di ban impedisce a un membro rimosso di usare quel percorso di recupero. Implementa anche la lista inviti cifrata CORD-05 sia sull'app sia sul client da riga di comando `amy`, aggiunge tombstone di revoca per link, e richiede conferma del relay prima di eliminare l'unica chiave di firma memorizzata che può ritirare un link. Lo stesso lavoro dà a `amy` i percorsi di consegna della control key, refounding, rekeying e recupero dei membri stranded necessari per seguire le epoche comunitarie successive.

### Buzz porta l'aspetto di ogni comunità tra desktop e mobile

[Buzz](https://github.com/block/buzz) è uno workspace comunitario basato su Nostr con client desktop e mobile. Le PR desktop [PR #3653](https://github.com/block/buzz/pull/3653) e mobile [PR #3767](https://github.com/block/buzz/pull/3767) unite memorizzano tema, accento e scelta della modalità di sistema di ogni comunità come record NIP-78 cifrato sul relay di quella comunità. Entrambi i client condividono lo stesso payload versionato e mantengono cache locali scoped per identità, così cambiare comunità o account non può applicare l'aspetto sbagliato mentre il relay non è disponibile. Ordinamento di sostituzione, scritture protette e risottoscrizione dopo una connessione chiusa permettono ai due client di riconvergere dopo la riconnessione.

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) è seguito prima del cutoff del numero con un passaggio di performance e affidabilità. Rimuove regressioni introdotte dopo 0.5.9, accelera il caricamento dei canali, limita la retention iniziale della timeline, coalescesce la persistenza dello stato di lettura, preserva timeline di canale fresche e impedisce al worker di ingest dei relay di crashare sulle reazioni agli eventi di progetto. Aggiunge anche l'invio di un messaggio di thread a un canale e restringe la ricerca desktop allo scope previsto.


## Aggiornamenti NIP e lavoro di specifica del protocollo

### NIP

La [PR NIPs #2435](https://github.com/nostr-protocol/nips/pull/2435) è un emendamento aperto a NIP-34, che standardizza la collaborazione su repository git tramite eventi Nostr. Aggiunge un tag `b` opzionale a un evento pull-request così l'autore può nominare un branch di destinazione diverso dal default del repository. La proposta corrisponde al supporto già implementato in ngit e GitWorkshop, ma non è entrata nella specifica.

La [PR NIPs #2434](https://github.com/nostr-protocol/nips/pull/2434) è una proposta aperta per chiavi di identità post-quantum. Deriva chiavi post-quantum di crittografia e firma accanto alla chiave secp256k1 esistente da un seed di derivazione chiavi NIP-06, poi lega le chiavi pubbliche all'identità Nostr con un'attestazione di kind `10203`. La bozza limita la sua pretesa alla protezione della riservatezza dei messaggi precedenti se secp256k1 venisse compromesso in seguito; non sostituisce le firme degli eventi odierne.

La [PR NIPs #2431](https://github.com/nostr-protocol/nips/pull/2431) è un emendamento aperto a NIP-07 per firmatari browser. Un client potrebbe allegare la chiave pubblica che si aspetta alle richieste di firma o crittografia, richiedendo al firmatario di usare quell'account o rifiutare la chiamata. Ciò impedirebbe a una pagina di continuare silenziosamente sotto un'identità diversa dopo che l'utente cambia account nel firmatario.

La [PR NIPs #1813](https://github.com/nostr-protocol/nips/pull/1813) resta una proposta open double-ratchet dopo lavoro sostanziale nella finestra. Specifica conversazioni cifrate forward-secret le cui chiavi avanzano con i messaggi, con un'implementazione già disponibile nella libreria nostr-double-ratchet e in Iris. Resta una bozza, non un NIP unito.

La [PR NIPs #2433](https://github.com/nostr-protocol/nips/pull/2433) si è aperta e chiusa senza merge nella finestra. Proponeva di chiarire gli errori relay NIP-42 così `auth-required` significherebbe che un'altra autenticazione potrebbe cambiare il risultato, mentre `restricted` significherebbe che non potrebbe. La distinzione riguardava connessioni autenticate per una chiave ma ancora prive di autorizzazione per un'altra; lo stato chiuso significa che la formulazione non è entrata nella specifica.

La [PR NIPs #2378](https://github.com/nostr-protocol/nips/pull/2378), trattata in precedenza mentre era ancora proposta, si è ora chiusa senza merge. I suoi eventi proposti di agent passport, discovery, task, marketplace, invoice e connection restano quindi fuori dall'insieme dei NIP.

Il [commit NIPs 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) ha unito una correzione solo documentale a NIP-29. Aggiunge un tag `previous` all'esempio di metadati del gruppo, mostrando come un evento di sostituzione possa identificare l'evento che sostituisce. Questo chiarisce un esempio e non introduce una nuova funzionalità di protocollo.

### Concord e CORD

La [PR CORD #18](https://github.com/concord-protocol/concord/pull/18) frammenterebbe le Community List cifrate su eventi di kind `33302`, rimuoverebbe il limite di 50 appartenenze e poterebbe le voci ritirate per restare entro i limiti dei relay. Altre due proposte aperte aggiungono [locator di menzione privati](https://github.com/concord-protocol/concord/pull/16) e un [segnale di pausa](https://github.com/concord-protocol/concord/pull/17) che sospende la chat senza scartare i messaggi.

La [PR CORD-02 #15](https://github.com/concord-protocol/concord/pull/15) si è unita il 6 agosto e restringe le scritture al piano di controllo di una comunità. Proprietari e staff detengono un nuovo secret di firma `control_root`, mentre tutti i membri conservano la chiave pubblica derivata e la read key necessarie per verificare e decifrare lo stato di moderazione. La write key è una barriera anti-spam, non un sostituto delle firme interne dell'attore e dei controlli del roster che stabiliscono l'autorità.

La [PR CORD #12](https://github.com/concord-protocol/concord/pull/12), trattata in precedenza come bozza aperta, si è ora chiusa senza merge. La sua porzione di piano di controllo è stata superata dall'emendamento CORD-02 più ristretto unito sopra, mentre canali restricted-write e gli altri materiali di bozza non sono entrati nella specifica.

## Approfondimento NIP

### Richieste di cancellazione degli eventi (NIP-09)

[NIP-09](/it/topics/nip-09/) (richieste di cancellazione eventi), definito dalla [specifica principale](https://github.com/nostr-protocol/nips/blob/master/09.md), offre a un autore di evento un modo firmato di chiedere a relay e client di smettere di servire uno o più eventi di quell'autore. Non cancella ogni copia. Trasporta l'intenzione dell'autore attraverso la stessa rete di relay che ha distribuito l'evento originale.

La richiesta è un evento firmato ordinario di kind `5`. I suoi tag contengono uno o più riferimenti `e` a ID evento specifici o riferimenti `a` a coordinate di eventi indirizzabili, e le [regole dei tag NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) dicono che dovrebbe includere un tag `k` per ogni kind di evento referenziato. Il `content` opzionale può spiegare il motivo. Per un riferimento `a`, un relay dovrebbe rimuovere ogni versione a quella coordinata il cui timestamp non è successivo al `created_at` della richiesta, impedendo a una vecchia richiesta di cancellazione di sopprimere una sostituzione successiva.

[L'autore è il confine di sicurezza](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior). Un relay dovrebbe smettere di pubblicare un evento referenziato solo quando la sua `pubkey` corrisponde alla `pubkey` della richiesta di cancellazione, e un client deve eseguire quel controllo prima di nascondere un evento. Un relay potrebbe non possedere l'evento referenziato e quindi non essere in grado di validare la relazione quando accetta la richiesta, così i client non possono trattare l'accettazione del relay come prova che la cancellazione fosse autorizzata. La specifica chiede anche ai relay di conservare la richiesta di kind `5` perché un altro client potrebbe già detenere l'evento originale e incontrare la richiesta in seguito.

Ecco un [evento firmato di kind `5`](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943):

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

La cancellazione resta una politica cooperativa, non la revoca di un oggetto firmato. Un relay, una cache, uno screenshot o un client offline possono preservare i byte originali, e cancellare la richiesta di kind `5` stessa non la annulla. I client possono nascondere l'obiettivo, contrassegnarlo come disconosciuto o mostrare il motivo della richiesta, ma dovrebbero dire agli utenti che una cancellazione universale non può essere garantita. Questo differisce da [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), dove un tag `expiration` chiede ai relay di smettere di memorizzare un evento dopo un tempo scelto al momento della pubblicazione. NIP-09 gestisce una decisione successiva dell'autore e può puntare a eventi già distribuiti.

Le implementazioni attuali applicano quella politica a livelli diversi. La [PR Divine #6623](https://github.com/divinevideo/divine-mobile/pull/6623) rimuove i video cancellati dall'event store del client, la [PR strfry #251](https://github.com/hoytech/strfry/pull/251) estende le richieste di cancellazione valide ai destinatari gift-wrap, e [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) dichiara supporto NIP-09 nel suo client. Il [client di gruppo di nostrord](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) offre un altro percorso di implementazione attuale.

### Segnalazioni (NIP-56)

[NIP-56](/it/topics/nip-56/) (eventi di segnalazione), definito dalla [specifica principale](https://github.com/nostr-protocol/nips/blob/master/56.md), standardizza una segnalazione firmata su un account, un evento o un blob referenziato. Separa il segnale di segnalazione dalla decisione di moderazione, permettendo a ogni client o relay di scegliere quali reporter fidare e quale risposta si adatti alla propria politica.

Una segnalazione usa kind `1984` e deve identificare l'account segnalato in un tag `p`. Segnalare una nota richiede anche un tag `e` per l'ID evento. Il terzo valore del tag porta una delle categorie specificate: `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation` o `other`. Una segnalazione su un blob può usare il suo hash in un tag `x`, un tag `e` per l'evento che ha referenziato il blob, e un tag `server` opzionale per una posizione. I tag opzionali `L` e `l` da [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) possono aggiungere un'etichetta con namespace quando l'elenco fisso di categorie non è abbastanza preciso.

[L'evento prova solo che una chiave ha fatto un'accusa](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting). Il contenuto segnalato non diventa falso, illegale o rimovibile solo perché esiste un kind `1984` valido, e un relay aperto non può contare in sicurezza segnalazioni anonime come voti. La specifica sconsiglia la moderazione automatica del relay perché le segnalazioni sono facili da manipolare, permettendo però agli amministratori di relay di agire su segnalazioni da moderatori che già fidano. Un client può invece pesare le segnalazioni attraverso il grafo sociale dell'utente, per esempio sfocando contenuti dopo che diversi contatti fidati segnalano lo stesso account.

Ecco un [evento firmato di kind `1984`](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2):

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 e NIP-09 risolvono problemi diversi](https://github.com/nostr-protocol/nips/tree/master). Una segnalazione di kind `1984` può prendere di mira l'account o l'evento di qualcun altro, ma non conferisce alcuna autorità di cancellazione. Una richiesta di kind `5` esprime l'intenzione dell'autore originale ed è valida solo contro gli eventi di quell'autore. Nessuna garantisce la rimozione: NIP-56 delega deliberatamente l'azione alla politica di moderazione locale, mentre NIP-09 dipende da relay e client che onorano una richiesta autenticata.

Le implementazioni espongono quelle scelte in prodotti diversi. La [PR Divine #6591](https://github.com/divinevideo/divine-mobile/pull/6591) corregge la consegna delle segnalazioni in un client di video brevi, la [PR Conduit #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) legge le segnalazioni come contesto limitato per i partecipanti al marketplace, e il [modulo NIP-56 di nostrord](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) pubblica e processa eventi di segnalazione. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) elenca anche il supporto NIP-56 attuale.


---

Invia un DM NIP-17 per condividere un progetto o una notizia tramite il [progetto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
