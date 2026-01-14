---
title: "NIP-71: Event Video"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 definisce i kind di event per i contenuti video su Nostr, abilitando la condivisione di video con supporto appropriato per i metadati. La specifica copre sia gli event video regolari che gli event video indirizzabili, con questi ultimi aggiunti a gennaio 2026 per permettere ai creator di aggiornare i metadati video senza ripubblicare.

## Kind di Event

NIP-71 definisce quattro kind di event divisi in due categorie basate sul rapporto d'aspetto e l'indirizzabilità.

Gli event video regolari usano il kind 21 per video orizzontali (landscape) e il kind 22 per video verticali (portrait/shorts). Questi sono event Nostr standard con contenuto immutabile una volta pubblicati.

Gli event video indirizzabili usano il kind 34235 per video orizzontali e il kind 34236 per video verticali. Questi sono event sostituibili parametrizzati identificati dalla combinazione di pubkey, kind e tag `d`. Pubblicare un nuovo event con gli stessi identificatori sostituisce la versione precedente, permettendo aggiornamenti dei metadati.

## Struttura

Un event video indirizzabile completo include campi di identificazione, tag di metadati e il riferimento al contenuto video.

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

Il tag `d` fornisce un identificatore univoco tra i vostri video di quel kind, così potete avere più video indirizzabili usando valori `d` diversi. I tag `title` e `summary` forniscono il titolo del video e una breve descrizione per la visualizzazione nei client. Il tag `url` punta al file video effettivo, mentre `thumb` fornisce un'immagine di anteprima. Il tag `duration` specifica la durata in secondi, e `dim` specifica opzionalmente le dimensioni del video.

Il tag `origin` traccia la piattaforma sorgente quando si importano contenuti da altri servizi. Questo preserva la provenienza quando si migrano video da YouTube, Vimeo o altre piattaforme all'hosting su Nostr.

Il campo `content` può contenere una descrizione estesa, la trascrizione completa, o qualsiasi testo aggiuntivo associato al video.

## Perché gli Event Indirizzabili Sono Importanti

Gli event video regolari (kind 21 e 22) sono immutabili una volta pubblicati. Se pubblicate un video e poi notate un errore di battitura nel titolo, volete aggiornare la miniatura, o dovete cambiare l'URL di hosting perché avete migrato a un servizio video diverso, non potete modificare l'event originale. La vostra unica opzione è pubblicare un nuovo event con un nuovo ID, il che rompe qualsiasi riferimento esistente e perde le metriche di engagement.

Gli event video indirizzabili risolvono questo problema rendendo l'event sostituibile. La combinazione della vostra pubkey, il kind dell'event e il tag `d` identifica univocamente il vostro video. Quando pubblicate un nuovo event con gli stessi identificatori, i relay sostituiscono la vecchia versione con quella nuova. I client che recuperano il vostro video ottengono sempre gli ultimi metadati.

Questo è particolarmente prezioso per correggere errori nei metadati dopo la pubblicazione, aggiornare le miniature mentre migliorate il vostro branding, migrare gli URL di hosting video quando cambiate provider, e importare contenuti da piattaforme dismesse come Vine preservando la provenienza attraverso il tag `origin`.

## Implementazioni

Gli event video indirizzabili (kind 34235 e 34236) sono attualmente implementati in Amethyst e nostrvine. Entrambi i client possono creare, visualizzare e aggiornare event video indirizzabili.

---

**Fonti principali:**
- [Specifica NIP-71](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Aggiornamento event video indirizzabili

**Menzionato in:**
- [Newsletter #5: Aggiornamenti NIP](/it/newsletters/2026-01-13-newsletter/#aggiornamenti-nip)

**Vedi anche:**
- [NIP-94: Metadati File](/it/topics/nip-94/)
