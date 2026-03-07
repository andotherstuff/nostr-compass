---
title: "NIP-71: Eventi Video"
date: 2026-01-13
translationOf: /en/topics/nip-71/
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
NIP-71 definisce i kind di evento per i contenuti video su Nostr, abilitando la condivisione di video con un supporto corretto dei metadati. La specifica copre sia gli eventi video normali sia gli eventi video addressable, con questi ultimi aggiunti nel gennaio 2026 per permettere ai creatori di aggiornare i metadati del video senza ripubblicarlo.

## Kind di Evento

NIP-71 definisce quattro kind di evento divisi in due categorie in base al rapporto d'aspetto e all'addressability.

Gli eventi video normali usano il kind 21 per i video orizzontali (landscape) e il kind 22 per i video verticali (portrait/shorts). Questi sono eventi Nostr standard con contenuto immutabile una volta pubblicato.

Gli eventi video addressable usano il kind 34235 per i video orizzontali e il kind 34236 per i video verticali. Si tratta di eventi parameterized replaceable identificati dalla combinazione di pubkey, kind e tag `d`. Pubblicare un nuovo evento con gli stessi identificatori sostituisce la versione precedente, permettendo aggiornamenti dei metadati.

## Struttura

Un evento video addressable completo include campi di identificazione, tag di metadati e il riferimento al contenuto video.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

Il tag `d` fornisce un identificatore univoco all'interno dei tuoi video di quel kind, così puoi avere più video addressable usando valori `d` diversi. I tag `title` e `summary` forniscono il titolo del video e una breve descrizione da mostrare nei client. Il tag `url` punta al file video vero e proprio, mentre `thumb` fornisce un'immagine di anteprima. Il tag `duration` specifica la lunghezza in secondi e `dim` specifica facoltativamente le dimensioni del video.

Il tag `origin` traccia la piattaforma di origine quando si importa contenuto da altri servizi. Questo preserva la provenienza quando si migrano video da YouTube, Vimeo o altre piattaforme verso hosting su Nostr.

Il campo `content` può contenere una descrizione estesa, una trascrizione completa o qualsiasi testo aggiuntivo associato al video.

## Perché gli Eventi Addressable Contano

Gli eventi video normali (kind 21 e 22) sono immutabili una volta pubblicati. Se pubblichi un video e in seguito noti un refuso nel titolo, vuoi aggiornare la thumbnail o devi cambiare l'URL di hosting perché sei migrato a un altro servizio video, non puoi modificare l'evento originale. L'unica opzione è pubblicare un nuovo evento con un nuovo ID, cosa che rompe i riferimenti esistenti e perde le metriche di engagement.

Gli eventi video addressable risolvono questo problema rendendo l'evento sostituibile. La combinazione del tuo pubkey, del kind dell'evento e del tag `d` identifica in modo univoco il tuo video. Quando pubblichi un nuovo evento con gli stessi identificatori, i relay sostituiscono la vecchia versione con quella nuova. I client che recuperano il tuo video ottengono sempre i metadati più recenti.

Questo è particolarmente utile per correggere errori nei metadati dopo la pubblicazione, aggiornare le thumbnail mentre migliori il tuo branding, migrare gli URL di hosting video quando cambi provider e importare contenuti da piattaforme dismesse come Vine preservando la provenienza tramite il tag `origin`.

Un vantaggio aggiuntivo è la stabilità dei link. Altri eventi possono continuare a riferirsi allo stesso video addressable mentre il creatore aggiorna i dettagli di presentazione intorno a esso, il che è più pulito che frammentare commenti e riferimenti tra più repost immutabili.

## Compromessi

La sostituibilità aiuta nella manutenzione dei metadati, ma significa anche che i client devono decidere quanta cronologia preservare. Se un creatore cambia titolo o summary dopo la pubblicazione, l'evento più recente diventa canonico anche se i client più vecchi potrebbero aver indicizzato la versione precedente.

I kind 21 e 22 restano importanti per le applicazioni che vogliono una registrazione immutabile della pubblicazione. NIP-71 non forza ogni flusso video nel modello sostituibile.

## Implementazioni

Gli eventi video addressable (kind 34235 e 34236) sono attualmente implementati in Amethyst e nostrvine. Entrambi i client possono creare, mostrare e aggiornare eventi video addressable.

---

**Fonti primarie:**
- [Specifica NIP-71](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Aggiornamento degli eventi video addressable

**Menzionato in:**
- [Newsletter #5: Aggiornamenti NIP](/en/newsletters/2026-01-13-newsletter/#nip-updates)
- [Newsletter #12: NoorNote](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [NIP-94: Metadati dei File](/it/topics/nip-94/)
