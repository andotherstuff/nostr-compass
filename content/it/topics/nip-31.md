---
title: "NIP-31: Gestire i kind di evento sconosciuti"
date: 2026-11-04
draft: false
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
categories:
  - NIPs
  - Protocol
---

> **Avviso sullo stato:** l'attuale [specifica NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md) si dichiara `unrecommended` in quanto "inutilmente gonfiata", e la sua riga di stato riporta draft, unrecommended e optional. I relay contengono già eventi che usano questa convenzione, quindi questa pagina spiega come i client li leggono. Non raccomanda NIP-31 per nuovi protocolli.

NIP-31 definisce un tag `alt` di primo livello. Il tag contiene un breve riepilogo in testo semplice per i kind di evento personalizzati che non sono pensati per essere letti come normali note di testo.

## Come funziona {#how-it-works}

L'autore di un evento di kind personalizzato aggiunge un tag `alt` con un'etichetta leggibile da una persona. I client costruiti attorno al kind 1 non devono sottoscriversi a ogni kind che non riconoscono. I loro utenti possono comunque imbattersi in un evento del genere quando una nota vi fa riferimento, e l'etichetta fornisce un po' di contesto anche se il client non implementa quel kind.

Frammento di tag, non un evento completo:

```
["alt", "<short plaintext summary>"]
```

Un'etichetta leggibile riguarda solo la visualizzazione. Non può esprimere un voto, dare seguito a una richiesta di wallet né compiere alcun'altra azione nativa del kind. Per un'interazione più ricca, la specifica rimanda a [NIP-89: Gestori di applicazioni consigliati](/it/topics/nip-89/).

## Implementazioni {#implementations}

Nella [scheda per eventi sconosciuti di noStrudel al commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), il primo tag `alt` viene ripulito dagli spazi e diventa l'etichetta principale, con una riga opzionale `Using <client>`. Un valore mancante o vuoto produce `Unknown event (kind ...)`, e fino a tre righe di contenuto compaiono separatamente. Lo stesso componente risolve il tag `client` tramite i modelli dei gestori NIP-89. Mostra un pulsante Open quando esiste un indirizzo condivisibile e `Open in <client>` quando si risolve un link valido a un gestore. La spiegazione e l'apertura nell'app sono controlli distinti.

Il file [UnknownEventDigest.kt di Amethyst al commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) privilegia il contenuto che classifica come prosa e ripiega su `alt`. Il suo parser ripulisce i valori dagli spazi e prende il primo `alt` non vuoto. Di conseguenza, un evento il cui primo `alt` è vuoto può ricevere qui un'etichetta diversa rispetto a noStrudel. Entrambe le descrizioni riflettono il codice sorgente a quei commit. Nessuna delle due conferma il comportamento di una versione rilasciata.

## Limiti {#limits}

- `alt` è un tag, quindi l'ID evento e la firma definiti in [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) lo coprono. Una firma valida dimostra che l'autore ha pubblicato l'etichetta. Non dimostra che l'etichetta sia accurata, quindi un riepilogo può essere fuorviante.
- I tag sono pubblici. Un `alt` su un evento con contenuto cifrato espone il proprio riepilogo e può rivelare ciò che il contenuto nasconde.
- Entrambe le proprietà sopra derivano dalla struttura dell'evento di NIP-01. Il testo di NIP-31 non le indica come requisiti.
- Un tag `alt` di primo livello è diverso dal campo `alt` di descrizione delle immagini all'interno di `imeta`, e i renderer li analizzano separatamente.

---

**Fonti primarie:**
- [Specifica NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [embedded-unknown.tsx di noStrudel al commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [UnknownEventDigest.kt di Amethyst al commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**Citato in:**
- [Newsletter #47: Approfondimento NIP](/it/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**Vedi anche:**
- [NIP-89: Gestori di applicazioni consigliati](/it/topics/nip-89/)
- [NIP-73: ID di contenuti esterni](/it/topics/nip-73/)
- [NIP-01: Descrizione del flusso di base del protocollo](/it/topics/nip-01/)
