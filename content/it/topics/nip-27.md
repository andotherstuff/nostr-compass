---
title: "NIP-27 (Riferimenti nelle text note)"
date: 2026-02-04
translationOf: /en/topics/nip-27/
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---
NIP-27 specifica come incorporare riferimenti a entità Nostr nel contenuto delle text note. I riferimenti usano lo schema URI `nostr:` seguito da un identificatore codificato bech32 (npub, note, nevent, nprofile, naddr).

## Come funziona

Quando si compone una nota che menziona un altro utente o fa riferimento a un altro evento, il riferimento viene incorporato direttamente nel contenuto:

```
Check out this post by nostr:npub1... about nostr:note1...
```

I client analizzano questi riferimenti e li rendono nel modo appropriato, di solito come link cliccabili o profile card inline. Le entità referenziate possono anche essere duplicate nei tag dell'evento per indicizzazione o notifiche, ma la specifica lo lascia opzionale.

Il NIP copre anche il parsing degli hashtag. I tag con prefisso `#` vengono estratti e aggiunti ai tag `t` dell'evento per renderli ricercabili.

## Tipi di riferimento

- `nostr:npub1...` - Riferimento a un profilo utente
- `nostr:note1...` - Riferimento a uno specifico evento nota
- `nostr:nevent1...` - Riferimento a un evento con relay hint
- `nostr:nprofile1...` - Riferimento a un profilo con relay hint
- `nostr:naddr1...` - Riferimento a un evento indirizzabile

## Perché è importante

NIP-27 separa ciò che le persone leggono da ciò che i client memorizzano. Un utente può digitare `@name` in un composer ricco, ma l'evento pubblicato può comunque contenere un riferimento stabile `nostr:nprofile...` in `content`. Questo rende il riferimento portabile tra client senza dipendere dalla sintassi di mention di una sola app.

Un altro vantaggio pratico è la resilienza. Un `nostr:nevent...` o `nostr:naddr...` grezzo incorporato nel testo porta comunque abbastanza informazioni perché un altro client possa ricostruire l'obiettivo anche se non ha mai visto il rendering locale originale.

## Note di interoperabilità

- Usa la forma [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) nel contenuto stesso: `nostr:<bech32-id>`
- Aggiungi tag `p` o `q` solo quando il tuo client vuole notifiche di mention o un'indicizzazione eventi più forte
- Non dare per scontato che ogni riferimento inline debba diventare una relazione di reply. La specifica lascia questa scelta al client

---

**Fonti primarie:**

- [Specifica NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 Encoded Entities)](/it/topics/nip-19/) - Definisce i formati di codifica usati nei riferimenti

**Citato in:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Correzione in nostr-tools per il parsing degli hashtag dopo i ritorni a capo

**Vedi anche:**
- [NIP-18: Reposts](/it/topics/nip-18/)
- [NIP-19: Bech32-Encoded Entities](/it/topics/nip-19/)
