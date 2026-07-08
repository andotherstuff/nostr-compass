---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-01
---

Amber 6.2.0 rilascia la cifratura NIP-44 v3 prima della spec. Mostro porta le fondamenta per l'escrow regolato con Cashu attraverso otto PR, avvolgendo l'esistente Cashu Development Kit come secondo backend di regolamento accanto a Lightning. NIP-F4 podcast è mergiato dopo 27 mesi di dibattito. fiatjaf apre una proposta contestata di disaccoppiamento delle chiavi NIP-17 che riapre la discussione architetturale bunker-contro-Marmot. Amethyst porta l'etichettatura di hashtag NIP-32, una schermata podcast dedicata e gli zap onchain attraverso 52 PR non rilasciate.

## Storie principali

### Amber 6.2.0: cifratura NIP-44 v3 rilasciata

[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0), rilasciato il 1° giugno, aggiunge il [supporto alla cifratura NIP-44 v3](https://github.com/greenart7c3/Amber/pull/448) con una schermata di approvazione dedicata, anteprima dell'intent, anteprima bunker, logging della cronologia e auto-reject per richieste non valide. La release registra anche le [autorità ContentProvider NIP-44 v3](https://github.com/greenart7c3/Amber/commit/8b93340) così altre app Android possono richiedere la cifratura v3 insieme al percorso v2 esistente. NIP-44 stesso è la spec versionata di payload cifrato usata dai DM privati [NIP-17](/it/topics/nip-17/), dal traffico bunker NIP-46 e da altre primitive Nostr; v3 in Amber è opt-in accanto a v2, segnalato da un metodo signer separato così i client lato ricevente possono negoziare l'algoritmo esplicitamente. La corrispondente PR nel repo NIPs deve ancora arrivare, quindi Amber sta rilasciando v3 prima del consensus di protocollo, con il wire format e l'autorità ContentProvider registrati per l'integrazione dei client a valle.

Le sessioni NIP-46 ora auto-accettano le richieste di ping alla connessione, rimuovendo il prompt sul primo round trip dopo il pairing. Il metodo signer `sign_message` è stato rimosso completamente dopo essere stato deprecato e non utilizzato.

Poiché Amber è il signer Android dominante, ogni client a valle che vuole v3 deve puntare al wire format di Amber finché la PR NIPs non arriva. Ciò dà ad Amber implicitamente voce in capitolo sulla spec finale v3 finché il protocollo non recupera. Il trade è reale: v3 in produzione lascia che Amber raccolga feedback implementativi per l'eventuale NIP, al costo di un punto di riferimento a singola implementazione temporaneo che gli altri client ora devono eguagliare.

### Mostro: integrazione dell'escrow Cashu tramite CDK

grunch ha portato otto PR attraverso MostroP2P questa settimana integrando le primitive multisig P2PK esistenti di Cashu (NUT-10 e NUT-11) come secondo backend di regolamento accanto a Lightning sull'exchange Bitcoin P2P coordinato via Nostr. Le primitive crittografiche sono di Cashu; il lavoro è impalcatura di integrazione e un nuovo trait di backend escrow. [Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0), rilasciato il 30 maggio, aggiunge i [tipi di protocollo per l'escrow multisig 2-di-3](https://github.com/MostroP2P/mostro-core/pull/150), firme P_M per-proof e consente eventi escrow attraverso la validazione della risposta. L'architettura è documentata in [PR #756](https://github.com/MostroP2P/mostro/pull/756) e usa chiavi di trade per-order chiarite in [PR #757](https://github.com/MostroP2P/mostro/pull/757).

L'implementazione è stata dispiegata attraverso sei PR di follow-up in un solo giorno. [F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758) ha aggiunto la configurazione, la modalità escrow e il boot condizionale. La fetta successiva, [F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760), ha definito un trait `EscrowBackend` con un'implementazione Lightning e uno stub Cashu, consentendo a Mostro di cambiare backend di regolamento senza cambiare la macchina a stati degli ordini. [F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759) ha wrappato [CDK](https://github.com/cashubtc/cdk) (il Cashu Development Kit) per operazioni di mint e wallet. Il lavoro sul database in [F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761) ha aggiunto lock escrow compare-and-swap e query active-locked. [F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762) ha costruito una mint containerizzata in un job CI dedicato per il test end-to-end dell'escrow. Il flusso Mostro usa già DM gift-wrapped NIP-59 per la coordinazione degli ordini sul relay, così l'escrow Cashu si inserisce come una seconda opzione di regolamento accanto a Lightning senza toccare il wire protocol.

## Rilasci

### ngit v2.5.0: fallback GRASP e fetch git pigri

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0) cambia il comportamento di default di `git push pr/<branch>` e `ngit send` per produrre un PR kind per nuove proposte quando il repository ha almeno un server GRASP registrato. In precedenza questo si attivava solo per commit sovradimensionati oltre i 60 KB o commit contenenti submoduli. Quando un PR non può essere pushato ai server GRASP del repository, ngit ora ricade su routing GRASP-06 attraverso i server dichiarati. Il flag `ngit send --git-server` o `git push -o git-server=<url>` consente ai contributor di puntare esplicitamente a un URL git custom o server GRASP.

I republish di `ngit init` ora preservano i tag sconosciuti dagli annunci esistenti, così i tag aggiunti da una futura versione di ngit o da uno strumento di terze parti sopravvivono al republish. Un warning giallo elenca i tag riportati, e `--clean` li rimuove su richiesta. `ngit pr apply`, `ngit pr checkout` e `ngit pr list` consultano i server git pigramente e condividono un singolo helper di fetch, così il checkout non fa più fetch incondizionato quando il commit è già locale. `ngit pr checkout` prova anche URL di clone forniti dal submitter dall'evento PR come fallback quando i server git dichiarati del repo non portano la punta del PR, corrispondendo al comportamento esistente in `ngit pr apply`. ngit è l'implementazione di riferimento [NIP-34](/it/topics/nip-34/) per la collaborazione git su Nostr, e v2.5.0 rende GRASP il percorso di prima classe per i nuovi contributor.

### Jumble v26.5.7: rimozione EXIF e conteggi zap validati

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7) aggiunge due modifiche che influenzano direttamente la privacy dell'utente e l'integrità dei dati. Gli identificatori di posizione EXIF e della camera sono ora rimossi dagli upload di immagini prima che lascino il client, chiudendo una superficie di lunga data di leak di metadati che ha colpito ogni immagine postata da Jumble. I conteggi degli zap sono ora calcolati solo da ricevute validate crittograficamente, correggendo conteggi gonfiati da eventi zap malformati che avevano lasciato agli attaccanti la possibilità di esagerare i totali degli zap sulle note. La release aggiunge anche la verifica dell'identità del mittente per i DM [NIP-17](/it/topics/nip-17/), chiudendo una superficie di spoofing in cui un mittente poteva falsificare il proprio `pubkey` nel seal.

### nostr-calendar v1.6.0: RSVP e gestione dei partecipanti duplicati

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0) porta il flusso RSVP di Formstr ([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) e impedisce partecipanti duplicati negli inviti a eventi ([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)). L'opzione `waitForAll` nella funzione di publish ora ha come default false così la UI non si blocca su relay lenti ([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)). [PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157) ha rilasciato le due bozze di proposta NIP di Formstr per la programmazione di appuntamenti e prenotazioni.

### Sprout 0.3.6: Sprout × mesh-llm e sezioni di canale

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6) è la principale di una serie di sei release da v0.3.1 a v0.3.6 questa settimana. L'integrazione in-process Sprout × mesh-llm arriva in [PR #798](https://github.com/block/sprout/pull/798), consentendo a Sprout di servire e consumare nodi mesh-llm tramite ammissione dal relay. Le sezioni di canale definite dall'utente si sincronizzano fra dispositivi via Nostr in [PR #792](https://github.com/block/sprout/pull/792), e le sezioni di canale arrivano su mobile con sync via relay in [PR #800](https://github.com/block/sprout/pull/800). Le notifiche thread-aware con controlli di follow e mute mutabili arrivano in [PR #761](https://github.com/block/sprout/pull/761).

Gli allegati file di tipo arbitrario con card di download sono arrivati in [PR #810](https://github.com/block/sprout/pull/810), espandendo Sprout oltre gli allegati solo immagine. Mobile ha guadagnato una tab feed sociale Pulse ([PR #772](https://github.com/block/sprout/pull/772)) e rifiniture Pulse fra feed, compose e superfici di filtro ([PR #796](https://github.com/block/sprout/pull/796)).

### NostrBotKit v0.5.0: chat di gruppo Marmot in un framework di bot Rust

[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md), rilasciato il 24 maggio su Codeberg, aggiunge il supporto [Marmot](/it/topics/marmot/) (MLS-over-Nostr, [NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) al framework di bot Rust self-hosted. Quando `marmot: true` è impostato, il bot pubblica i suoi key package MLS (kind 443, 30443, 10051), accetta inviti di gruppo automaticamente e ascolta i messaggi nei gruppi a cui è unito. Due nuovi tipi di comando, `dm_marmot` e `dm_marmot_npub`, consentono ai bot di inviare messaggi in gruppi Marmot con nome o chat Marmot 1:1 tramite cron job o webhook. Per prevenire loop di feedback con altri bot, i bot NostrBotKit rispondono solo a messaggi esplicitamente indirizzati a loro tramite `/command` o `@botname/command`. Gli allegati cifrati che usano MIP-04 sono decifrati automaticamente e ri-caricati via Blossom o NIP-96, e il database di stato MLS è cifrato con una chiave derivata dalla chiave privata del bot. NostrBotKit è il primo framework Rust a rilasciare il supporto ai bot NIP-104, aprendo il deployment di bot cifrati Marmot a un profilo operatore diverso dal percorso TypeScript esistente.

### noscrypt v0.1.14: rilascio firmato della libreria di crittografia

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14) è una release di sicurezza della libreria di crittografia C usata da diversi client Nostr per le primitive secp256k1, NIP-04 e NIP-44. La release è distribuita con [download PGP-firmati](https://www.vaughnnugent.com/resources/software/modules/noscrypt) verificabili contro la chiave pubblica del manutentore. I client a valle che integrano noscrypt dovrebbero validare la firma prima di integrarla.

### Chama v1.3.0: nuovo escrow P2P Nostr-native con Fedimint

[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0), rilasciato il 1° giugno, è la principale di una serie di quattro release per un nuovo client di escrow P2P Nostr-native che usa ecash Fedimint e secret sharing Shamir 2-di-3 per il regolamento. Il progetto è rilasciato a [getchama.app](https://getchama.app) e gira senza server. v1.3.0 introduce "heal that sticks" (re-broadcast riuscito e healing del trade che sopravvive ai riavvii di sessione) e pay-rail matching, dove le Chama US-leaning mostrano prima le rail di pagamento US. Le fondamenta per storefront multi-unità sono arrivate attraverso [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11) (schema multi-unità) e [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12) (accountant per lo stock dello storefront + hardening del recovery del bridge Fedimint nativo). Chama si unisce a Mostro e Shopstr nella categoria marketplace Nostr, distinta per la sua architettura serverless e il regolamento escrow basato su Fedimint.

## Modifiche non rilasciate

### Amethyst: etichettatura hashtag NIP-32, schermata podcast, tracce musicali

Amethyst ha mergiato 52 PR e 411 commit questa settimana senza tagliare una release tag. La più grande aggiunta funzionale è [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111), che implementa l'etichettatura hashtag [NIP-32](/it/topics/nip-32/) e un feed hashtag basato su etichette usando eventi di kind 1985 con namespace `L` e tag di etichetta `l`. Questo sostituisce il fragile meccanismo di corrispondenza testuale `#tag` con un modello di scoperta basato su labeler dove gli utenti possono seguire specifici npub labeler nel modo in cui seguono i creator di contenuto. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) aggiunge una schermata podcast dedicata con lista degli episodi e player inline, arrivando entro pochi giorni dal merge della spec podcast [NIP-F4](/it/topics/nip-f4/). [PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071) aggiunge un feed Software Apps con filtraggio per follow list, e [PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067) aggiunge il supporto a tracce musicali e playlist tramite set [NIP-51](/it/topics/nip-51/).

I signer effimeri per upload di post anonimi arrivano in [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123), consentendo agli utenti di postare anonimamente senza esporre la propria chiave di identità ai servizi di upload. Un watchdog di auto-healing Tor con test di integrazione contro Arti v2.3.0 arriva in [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053), rafforzando il routing Tor di Amethyst durante outage di rete transitori. Gli zap onchain e un filtro NIP-05 per utenti che ritornano da Gemini arrivano in [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052), ampliando la superficie di zap oltre Lightning ai pagamenti Bitcoin onchain.

### Shopstr: validazione degli URL di anteprima OpenGraph

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504) valida gli URL di anteprima OpenGraph prima di renderizzarli negli annunci del marketplace, chiudendo una potenziale superficie XSS in cui venditori malevoli potevano incorporare contenuto scriptato tramite metadati OG appositamente costruiti. Gli shop ospitati su Shopstr mostrano anteprime OG per link esterni, e URL non validati permettevano a un attaccante di iniettare contenuto arbitrario nella UI dello shop.

## Aggiornamenti NIP e lavoro di spec di protocollo

### NIP-F4 (Podcast) mergiato dopo due anni

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093) è stato mergiato il 28 maggio, due anni e tre mesi dopo che fiatjaf ha aperto la bozza originale. NIP-F4 definisce gli episodi di podcast come eventi di kind 54 con tag `imeta` per i metadati del file audio (URL, mime type, codice lingua ISO, URL di fallback, flag di servizio NIP-96, bitrate, durata), un tag `title`, tag opzionali `image` e `description` e tag `t` per etichette di topic. La spec mantiene deliberatamente RSS come fonte di verità: gli episodi possono portare un tag `i` che fa riferimento al GUID del podcast RSS, consentendo ai client Nostr di collegarsi ai feed di podcast esistenti senza duplicare l'hosting audio. Il lungo dibattito nel thread della PR (con Dave Jones co-autore del podcast-namespace, Alex Gleason e Mike Terenzio) si è concluso su un modello di coesistenza in cui Nostr fornisce il layer sociale sopra RSS mentre RSS mantiene il layer di distribuzione. La [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) schermata podcast di Amethyst arriva entro pochi giorni dal merge della spec, e il lavoro sul picker GIF di Jumble include anche fondamenta iniziali per l'allegato podcast.

### Disaccoppiamento delle chiavi NIP-17 (PR #2361)

fiatjaf ha aperto [PR #2361](https://github.com/nostr-protocol/nips/pull/2361) il 1° giugno, proponendo che NIP-17 separi la chiave di identità dalla chiave di cifratura. I destinatari pubblicizzano la loro chiave di cifratura in un nuovo evento di kind 10044, e i mittenti usano quella chiave pubblicizzata (quando presente) per il seal interno del gift-wrap, ricadendo sulla chiave di identità del destinatario solo quando la pubblicità è assente. La PR aggiunge anche un tag `n` al seal che porta la pubkey di cifratura del mittente, così i destinatari possono derivare la conversation key corretta senza decifratura per tentativi contro ogni chiave ritirata. La motivazione dichiarata è la UX bunker: sotto il design attuale, un utente bunker deve fare round-trip di ogni DM ricevuto attraverso il signer per decifrare, poiché la chiave di cifratura è la chiave di identità detenuta dal signer. Il disaccoppiamento lascia che il client detenga la chiave di cifratura localmente mantenendo la chiave di identità nel bunker per le firme.

La proposta ha attirato la review più contestata della settimana. Cody Tseng (Jumble) la sostiene come il percorso più facile per l'interop DM cross-client. Vitor Pamplona (Amethyst) obietta su due basi: aggiunge un nuovo secret di decifratura a lungo termine fuori dal bunker, e i client che non lo rilasciano falliranno silenziosamente a decifrare i messaggi dai client che lo fanno, senza percorso di degradazione perché la rottura è al layer del seal. Pamplona argomenta che il problema è già risolto correttamente dai key package e dalla rotazione di epoch di [Marmot](/it/topics/marmot/), e che retrofittare la separazione delle chiavi nella spec base NIP-17 crea il tipo di fallimento di interop che Marmot ha impiegato due anni a progettare per aggirare. La controrisposta di fiatjaf ha tre parti: il disaccoppiamento è opzionale per destinatario, il fix dell'n-tag affronta la preoccupazione della decifratura per tentativi, e l'alternativa è mantenere rotta la UX bunker mentre Telegram divora il caso d'uso della messaggistica. Il thread resta aperto senza una decisione di merge ed è la discussione NIP più osservata del trimestre.

### NIP-Silent Payments flusso di pagamento (PR #2362)

[silentius-satoshi ha aperto la PR #2362](https://github.com/nostr-protocol/nips/pull/2362) il 1° giugno come compagno della più ampia [bozza NIP Nostr Silent Payments (PR #2355)](https://github.com/nostr-protocol/nips/pull/2355). Il NIP del flusso di pagamento definisce il kind 8352 per le notifiche di ricevuta di silent payment (consegnate tramite gift wrap [NIP-59](/it/topics/nip-59/) così il link di ricevuta non è pubblicamente osservabile) e il kind 10353 per una cache UTXO cifrata che si sincronizza fra i dispositivi per lo stesso wallet Silent Payments. La coppia insieme consente a un pagatore di segnalare un pagamento a un indirizzo Silent Payments usando primitive Nostr-native senza esporre il link on-chain al layer aperto dei relay.

### NIP-PIP Perfect IP Packets (PR #2364)

[RandyMcMillan ha aperto la PR #2364](https://github.com/nostr-protocol/nips/pull/2364) il 1° giugno come bozza. Introduce un trasporto ad albero di pacchetti con tre nuovi kind indirizzabili: 39078 porta il manifest, 39079 porta gli slice individuali, e 39080 porta le richieste di riparazione. La spec definisce un wire format in cui file grandi sono spezzati in slice indirizzabili, con manifest che descrivono l'albero degli slice e richieste di riparazione che consentono ai destinatari di chiedere slice mancanti. Si applica lo status di bozza iniziale, e la proposta non ha ancora attirato la review dei manutentori.

### NIP-29 spazi live audio/video (PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238) mergiata il 28 maggio, estendendo i gruppi basati su relay [NIP-29](/it/topics/nip-29/) con supporto a spazi live audio e video. I gruppi possono ora fare riferimento a una sessione live-space attiva, consentendo agli eventi live activity in stile [NIP-53](/it/topics/nip-53/) di ancorarsi in un contesto di gruppo NIP-29.

### NIP-71 video multiple tracce audio (PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255) mergiata il 28 maggio, aggiungendo tag `imeta` di traccia audio agli eventi video NIP-71. Il nuovo formato porta URL, hash, mime type, tag di lingua (con ISO-639-1 più flag di versione originale), URL di fallback, segnale di servizio NIP-96, bitrate e durata. Questo abilita lo streaming solo audio (video podcast), il cambio di risoluzione con audio stabile, tracce multiple in lingua e ridotto storage quando i server non incorporano l'audio direttamente nei file video. I client dovrebbero controllare la disponibilità di traccia audio prima di assumere un comportamento a traccia singola.

### NIP-59 gift wrap effimero (PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) mergiata il 28 maggio, aggiungendo il kind 21059 come controparte effimera dell'esistente gift wrap di kind 1059. La semantica corrisponde al wrap standard NIP-59 ma segue le regole di eventi effimeri per NIP-01 (i relay li scartano dopo il broadcast e non li persistono). Ciò consente alle app di scegliere la persistenza in base ai requisiti: gli indicatori di digitazione e i ping di presenza beneficiano dell'effimero, mentre la cronologia DM ha bisogno di persistenza.

### NIP-78 kind application-specific (PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292) mergiata il 28 maggio, riclassificando i dati application-specific NIP-78 come un normale kind indirizzabile, abbandonando la precedente gamma separata. Questo semplifica la semantica di replaceability e allinea NIP-78 con il modello di eventi indirizzabili usato da altri NIP di stato applicativo.

### Chiarimenti NIP-85 (PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304) mergiata il 28 maggio con piccoli miglioramenti al linguaggio attorno a chiavi e relay multipli per service provider nelle Trusted Assertions [NIP-85](/it/topics/nip-85/), chiarendo il percorso di rotazione della chiave operatore per i servizi di assertion sui relay.

### NIP-01 one-liner sulla gestione della connessione relay (PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307) mergiata il 28 maggio, aggiungendo una singola frase a NIP-01 su come i client dovrebbero gestire i tempi di vita della connessione relay. Il fix affronta un gap di lunga data in cui i client differivano su se tenere le connessioni WebSocket aperte dopo il fetch, portando a perdita silenziosa di messaggi su relay che scartano connessioni idle.

### NIP-C7 vincolo di chat kind 9 (PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310) mergiata il 28 maggio, restringendo le viste chat NIP-C7 ai soli messaggi di kind 9. Questo separa la chat effimera dai post di timeline di kind 1 nei client che implementano superfici di chat in stile NIP-C7.

### Semplificazione NIP-55 (PR #2363)

[PR #2363](https://github.com/nostr-protocol/nips/pull/2363) di greenart7c3, aperta il 1° giugno, semplifica la spec dell'applicazione signer Android. Vitor Pamplona ha approvato come "Looks good" e fiatjaf ha chiesto se è pronta per il merge. La modifica apre la strada alla registrazione dell'autorità ContentProvider NIP-44 v3 che Amber ha rilasciato questa settimana.

### NIP-44 v3 (implementazione Amber prima della spec)

Amber ha rilasciato NIP-44 v3 in v6.2.0 con otto commit che implementano l'upgrade di cifratura e la registrazione dell'autorità ContentProvider, ma la PR della spec nel repo NIPs deve ancora arrivare. NIP-44 stesso definisce un formato di payload cifrato versionato usato dentro eventi firmati; l'esistente v2 (in produzione dal 2024) usa ECDH secp256k1, HKDF, padding, ChaCha20, HMAC-SHA256 e base64. Il wire format v3 aggiunge un nuovo byte di versione (0x03) prima del nonce, consentendo ai client destinatari di negoziare esplicitamente l'algoritmo. L'implementazione di Amber include auto-reject per richieste v3 non valide, una schermata di approvazione dedicata distinta dalle approvazioni v2 e logging del plaintext per direzione per la cronologia. Finché la PR NIPs non è mergiata, v3 rimane un'estensione specifica di Amber. Trattatela come un segnale prospettico, non come una segnalazione stabile a livello di protocollo.

## NIP deep dive: NIP-32 (Labeling)

[NIP-32](/it/topics/nip-32/) definisce un modo strutturato per qualunque attore Nostr di etichettare eventi, pubkey, relay, URL o topic usando eventi indirizzabili di kind 1985 con un vocabolario di etichette namespaced. La spec introduce due nuovi tag: `L` denota un namespace di etichetta, e `l` denota un'etichetta all'interno di quel namespace. I tag di target dell'etichetta (`e`, `p`, `a`, `r` o `t`) specificano cosa viene etichettato. Il requisito di namespace impedisce a più sistemi di etichette di collidere: un'etichetta `spam` in `nip28.moderation` porta una semantica diversa da un'etichetta `spam` in `relay-report`.

La scelta di design che rende NIP-32 utile oltre la moderazione è che le etichette sono asserzioni, non verità a livello di protocollo. Un evento di kind 1985 dice solo che una particolare pubkey ha etichettato un particolare target in un particolare namespace. Il modello di fiducia è delegato al client: ogni client sceglie quali labeler onorare, quali namespace leggere e quale affordance UI dare a ciascuna etichetta. La stessa primitiva porta avvertimenti di contenuto, assegnazione di licenza, tag di lingua ISO-639-1 sulle note di kind 1, tag geografici ISO-3166-2, classificazione di contenuto, suggerimenti di moderazione distribuita e punteggi di reputazione.

La [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111) di Amethyst di questa settimana è il più grande deployment finora. Aggiunge l'etichettatura hashtag tramite NIP-32 e un feed hashtag basato su etichette, consentendo agli utenti di sfogliare per etichette assegnate da labeler fidati. Il precedente meccanismo di corrispondenza testuale `#tag` che originariamente pilotava la scoperta hashtag su Nostr resta come fallback per note non etichettate. Il modello hashtag-come-etichetta significa che la stessa nota può essere scopribile sotto più etichette assegnate da labeler diversi, e gli utenti possono silenziare o promuovere specifici labeler senza influenzare le note sottostanti.

Anche l'auto-etichettatura è supportata. Un autore può attaccare tag `L` e `l` direttamente alle proprie note di kind 1 per dichiarare lingua, posizione e topic. Una nota taggata `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]` si auto-identifica come inglese e può essere filtrata da client language-aware senza infrastruttura di etichettatura di terze parti.

Esempio di evento etichetta NIP-32 che tagga una nota di kind 1 come inglese e le assegna un tag di moderazione:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

Il rollout di Amethyst combinato con il recente lavoro sulle Trusted Relay Assertions suggerisce che NIP-32 sta diventando il substrato standard per qualunque pattern di "asserzione guidata dall'utente su un target" su Nostr. Il prossimo test è se i labeler stessi svilupperanno gerarchie di fiducia: se gli utenti seguiranno specifici npub labeler nel modo in cui seguono i creator di contenuto.

## NIP deep dive: NIP-F4 (Podcast)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md) è stato mergiato questa settimana, due anni e tre mesi dopo che fiatjaf ha aperto la bozza originale (PR #1093). Il prefisso F è semplice numerazione hex: NIP-F0 fino a NIP-FF usano lo stesso spazio hex a 1 byte di NIP-0A fino a NIP-0D, con la gamma hex superiore che serve da overflow ora che la gamma decimale 01–99 si sta riempiendo. NIP-F4 definisce come i podcast pubblicano episodi e metadati come eventi Nostr mantenendo RSS come layer complementare per il file audio stesso.

La scelta architettonica di base è che ogni podcast è la propria keypair Nostr. La spec apre con questo direttamente: "each podcast is its own Nostr keypair". Ciò consente ai podcast di combinare la loro presenza podcast con una normale presenza di microblogging di kind 0 / kind 1, e consente a un podcast di cambiare proprietà nel tempo tramite handover di chiave o firma condivisa stile MuSig2. Quattro kind di evento portano il layer di pubblicazione:

- **`kind:10154`**: metadati podcast replaceable. Porta tag `title`, `image`, `description`, tag `website` opzionali e tag `p` opzionali che marcano gli autori con un `role` di `host`, `cohost` o `editor`.
- **`kind:10164`**: contro-claim dell'autore. L'esempio nella spec usa il kind `10064` (un typo aperto a correzione), ma l'header e il testo circostante lo identificano come `kind:10164`. Gli utenti elencano le pubkey di podcast di cui sono autori, così i client possono verificare i tag `p` in `kind:10154` contro una claim equivalente dal presunto autore. Senza questo, un podcast potrebbe falsamente taggare chiunque come host.
- **`kind:54`**: eventi episodio scritti dalla pubkey del podcast direttamente. I tag includono `title`, `image` opzionale, `description` e uno o più tag `audio`. Ogni tag `audio` è `["audio", "<audio-url>", "<optional_media_type>"]`. La spec nota "other important fields to be specified here later after further discovery", e la forma mergiata è deliberatamente minima.
- **`kind:10054`**: una lista di podcast preferiti in stile [NIP-51](/it/topics/nip-51/), consentendo agli utenti di marcare quali podcast seguono.

Il dibattito del thread attorno al merge ha coinvolto il co-autore di Podcasting 2.0 [Dave Jones](https://github.com/daveajones), [Alex Gleason](https://github.com/alexgleason), [Mike Terenzio](https://github.com/mterenzio), [Pablo F7z](https://github.com/pablof7z) e [staab](https://github.com/staab). Jones ha argomentato fortemente contro qualunque tentativo di sostituire RSS: "It's been tried many times and always fails", citando JSONfeed, XMPP, AMP, l'API di Twitter e la migrazione fallita di Spotify. Terenzio ha ripresentato la proposta come layer sociale sopra RSS, mantenendo RSS stesso come layer di distribuzione. fiatjaf ha accettato di fare un passo indietro e lasciar maturare la proposta: "I agree with everything you said but I still think we can pull it off, let's stop here for a while". Due anni dopo, la spec mergiata atterra più vicina alla coesistenza che alla sostituzione.

Tre domande di design restano esplicite nella spec mergiata:

- Il typo del `kind:10164` (l'esempio mostra `10064`) deve essere riconciliato prima che i client possano interoperare in sicurezza.
- La scoperta a livello di episodio senza collegamento GUID RSS è lasciata aperta. La spec mergiata non ha tag `i`, formato `podcast:item:guid` o meccanismo di bridging RSS. I client che vogliono fare bridge di un catalogo RSS esistente in eventi di kind 54 devono definire da soli la convenzione di bridge.
- Lo stub "other important fields" sulla definizione di `kind:54` lascia bitrate, durata, lingua, puntatori a trascrizioni, capitoli e metadati per segmento come territorio aperto per proposte di follow-up.

La [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) di Amethyst porta una schermata podcast dedicata con lista degli episodi e player inline entro pochi giorni dal merge, la prima grande implementazione client. Jumble ha rilasciato le prime fondamenta per l'allegato podcast insieme al suo picker GIF. Wavlake resta la più grande piattaforma podcast Nostr-native e dovrà decidere se allineare i suoi esistenti eventi di traccia musicale di kind 31337 con il modello di episodio di kind 54 di NIP-F4.

Esempio di evento episodio NIP-F4 kind 54, corrispondente al set di tag minimo della spec mergiata:

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093 è stata aperta per 27 mesi, ben oltre la durata mediana di apertura per le PR NIP mergiate. Il prossimo test per NIP-F4 è se il typo del kind 10164 sarà riconciliato, se convenzioni di scoperta di episodi e bridge RSS emergeranno dagli implementatori, e se i principali host podcast pubblicheranno sotto keypair per-podcast come la spec raccomanda.
