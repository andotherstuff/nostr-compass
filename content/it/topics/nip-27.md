---
title: "NIP-27 (Riferimenti nelle Note di Testo)"
date: 2026-02-04
description: "NIP-27 definisce come fare riferimento a profili, note e altre entità nel contenuto delle note usando lo schema URI nostr:."
---

NIP-27 specifica come incorporare riferimenti a entità Nostr nel contenuto delle note di testo. I riferimenti usano lo schema URI `nostr:` seguito da un identificatore codificato bech32 (npub, note, nevent, nprofile, naddr).

## Come Funziona

Quando si compone una nota che menziona un altro utente o fa riferimento a un altro evento, il riferimento viene incorporato direttamente nel contenuto:

```
Guarda questo post di nostr:npub1... riguardo nostr:note1...
```

I client analizzano questi riferimenti e li renderizzano appropriatamente, tipicamente come link cliccabili o card di profilo inline. Le entità referenziate vengono anche aggiunte ai tag dell'evento per l'indicizzazione e le notifiche.

Il NIP copre anche il parsing degli hashtag. I tag prefissati con `#` vengono estratti e aggiunti ai tag `t` dell'evento per la ricercabilità.

## Tipi di Riferimento

- `nostr:npub1...` - Riferimento a un profilo utente
- `nostr:note1...` - Riferimento a un evento nota specifico
- `nostr:nevent1...` - Riferimento a un evento con suggerimenti relay
- `nostr:nprofile1...` - Riferimento a un profilo con suggerimenti relay
- `nostr:naddr1...` - Riferimento a un evento addressable

## Implementazioni

Tutti i principali client Nostr implementano NIP-27:
- I parser di testo estraggono i riferimenti durante la composizione
- I renderer visualizzano i riferimenti come elementi interattivi
- I sistemi di notifica usano i tag associati

## Fonti Primarie

- [Specifica NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Entità Codificate Bech32)](/it/topics/nip-19/) - Definisce i formati di codifica usati nei riferimenti

## Menzionato In

- [Newsletter #8 (2026-02-04)](/it/newsletters/2026-02-04-newsletter/) - Fix di nostr-tools per il parsing degli hashtag dopo le newline
