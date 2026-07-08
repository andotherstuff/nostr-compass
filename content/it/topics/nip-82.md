---
title: "NIP-82: Applicazioni software"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
categories:
  - Discovery
  - Apps
---

NIP-82 definisce un evento di applicazione software che permette ai client Nostr di visualizzare le applicazioni (APK Android, app iOS, web app, binari desktop) come oggetti di prima classe nei feed e nelle superfici di scoperta. La specifica sostituisce il vecchio approccio di descrivere le app tramite generiche note di kind 1 o tramite le raccomandazioni degli handler di [NIP-89](/it/topics/nip-89/) con un evento dedicato e strutturato che trasporta i metadati dell'applicazione, gli screenshot, i link ai repository e l'identità dell'autore.

## Come funziona

Un'applicazione software NIP-82 è un singolo evento replaceable indirizzato dal pubkey dell'autore e dal tag `d`. L'evento trasporta:

- tag `name`, `description`, `icon`, `image` per la visualizzazione
- tag `repository` e `web` per gli URL del codice sorgente e della homepage
- tag `platforms` che elenca le piattaforme supportate (android, ios, web, linux, macos, windows)
- tag `download` per ciascun binario specifico per piattaforma o URL web
- tag `screenshots` che trasporta gli URL delle immagini per gli screenshot dell'applicazione
- tag topic `t` per la categorizzazione
- tag `version` per la versione pubblicata corrente

Un client che sfoglia un feed NIP-82 può mostrare la scheda dell'applicazione, collegarla al repository canonico e presentare gli screenshot senza dover ricorrere allo scraping di un post long-form Nostr o di uno store di app di terze parti. Il pubkey dell'autore è la fonte di verità per l'applicazione, quindi un client può verificare che il pubblicatore corrisponda all'identità dello sviluppatore attesa prima di promuovere un link di download.

## Semantica del feed

Gli eventi NIP-82 sono addressable, quindi ogni applicazione ha un unico evento replaceable canonico per autore. Uno sviluppatore che pubblica una nuova versione sostituisce l'evento precedente sul posto, e gli iscritti vedono l'aggiornamento senza dover gestire la cronologia degli eventi. I client che vogliono un change log possono iscriversi all'evento addressable e visualizzare i bump di versione come attività sulla superficie dell'applicazione.

La specifica si compone con [NIP-89](/it/topics/nip-89/) (Application Handlers): un evento NIP-82 descrive l'applicazione come artefatto, mentre un evento NIP-89 descrive che l'applicazione può gestire specifici kind di eventi. I client possono usarne uno senza l'altro, ma la coppia offre una superficie di scoperta (NIP-82) e una superficie di delega (NIP-89) che lavorano insieme.

## Implementazioni

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) include un feed dedicato per le applicazioni software NIP-82 con una schermata di dettaglio, informazioni sull'autore e screenshot ([PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036), [PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078), [PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200))

---

**Fonti primarie:**
- [Specifica NIP-82](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - Aggiunge il supporto per le applicazioni software NIP-82 con feed dedicato
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - Aggiunge una schermata di dettaglio dedicata per le app software NIP-82
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - Migliora l'interfaccia delle app software NIP-82 con informazioni sull'autore e screenshot

**Menzionato in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/it/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Vedi anche:**
- [NIP-89: Application Handlers](/it/topics/nip-89/)
