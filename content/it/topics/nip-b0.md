---
title: "NIP-B0: Segnalibri web"
date: 2026-05-28
draft: false
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
categories:
  - Protocol
  - Social
---

NIP-B0 definisce un evento parameterized replaceable (kind 39701) che pubblica i segnalibri web come eventi Nostr di prima classe. La proposta permette agli utenti di costruire raccolte curate di segnalibri che possono essere scoperte, ricevere zap ed essere ripubblicate tra i client senza dipendere da un servizio centrale di segnalibri.

## Come funziona

Un segnalibro è un evento di kind 39701 il cui tag `d` è l'URL canonico della pagina messa nei segnalibri. La semantica replaceable consente all'autore di aggiornare il proprio segnalibro per quell'URL (aggiungere tag, aggiornare il titolo, contrassegnarlo come obsoleto) senza produrre eventi duplicati. Il campo content trasporta la nota dell'autore sul segnalibro; i tag trasportano titolo, descrizione, immagine e tag topic `t` per la scoperta.

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

Il tag `d` identifica il segnalibro in modo univoco per autore, quindi due utenti possono entrambi mettere nei segnalibri lo stesso URL con le proprie annotazioni e insiemi di tag.

## Scoperta e curatela

Poiché ogni segnalibro è un evento di prima classe, qualsiasi client Nostr può visualizzare un feed di segnalibri iscrivendosi agli eventi di kind 39701 filtrati per tag o autori. I flussi di lavoro guidati dai curatori diventano naturali: un curatore pubblica una lista di segnalibri, i lettori seguono il pubkey del curatore, e i segnalibri fluiscono attraverso qualsiasi relay che li trasporta. Non esiste una directory centrale.

## Implementazioni

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public): client web di riferimento con un'architettura a tre box (curatore, indexer, viewer) e un sistema a livelli finanziato tramite zap NIP-57 diretti al curatore. Implementa NIP-B0 insieme a NIP-07, NIP-46, NIP-57, NIP-44, NIP-98, NIP-65 e Blossom BUD-01/BUD-04 per l'archiviazione dei file.

## Note su fiducia e sicurezza

- I segnalibri sono pubblici per impostazione predefinita; non pubblicare liste di lettura private in questo modo
- La ripubblicazione dipende dal fatto che i relay continuino a trasportare gli eventi; i relay effimeri elimineranno i segnalibri
- Il tag `published_at` è dichiarato dal pubblicatore, non verificabile

---

**Fonti primarie:**
- [Specifica proposta NIP-B0](https://github.com/nostr-protocol/nips/pull/2089): traccia l'evento web bookmark di kind 39701 proposto
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public): implementazione di riferimento con sistema a livelli per curatori

**Menzionato in:**
- [Newsletter #24: deepmarks NIP-B0 bookmarks with curator-monetized publishing](/it/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Newsletter #27: Also shipped](/it/newsletters/2026-06-17-newsletter/#also-shipped)

**Vedi anche:**
- [NIP-57: Lightning Zaps](/it/topics/nip-57/)
- [NIP-65: Relay List Metadata](/it/topics/nip-65/)
