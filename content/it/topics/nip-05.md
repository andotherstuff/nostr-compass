---
title: "NIP-05 (Verifica del Dominio)"
date: 2026-02-04
description: "NIP-05 abilita identificatori leggibili per le pubkey Nostr attraverso la verifica del dominio."
---

NIP-05 mappa le chiavi pubbliche Nostr a identificatori internet leggibili come `utente@esempio.com`. Questo fornisce un modo per verificare l'identità attraverso la proprietà del dominio senza richiedere fiducia in un'autorità centrale.

## Come Funziona

Un utente rivendica un identificatore aggiungendo un campo `nip05` ai metadati del proprio profilo. L'identificatore segue il formato `nome@dominio`. I client verificano la rivendicazione recuperando `https://dominio/.well-known/nostr.json` e controllando che il nome corrisponda alla pubkey dell'utente.

Il file JSON nel percorso well-known contiene un oggetto `names` che mappa i nomi locali alle pubkey esadecimali:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Quando la verifica ha successo, i client possono visualizzare l'identificatore al posto di o accanto all'npub. Alcuni client mostrano un segno di spunta o altro indicatore per gli identificatori verificati.

## Suggerimenti Relay

Il file `nostr.json` può opzionalmente includere un oggetto `relays` che mappa le pubkey ad array di URL relay. Questo aiuta i client a scoprire dove trovare gli eventi di un particolare utente.

## Implementazioni

La maggior parte dei client principali supporta la verifica NIP-05:
- Damus, Amethyst, Primal visualizzano gli identificatori verificati
- Molti servizi relay offrono identificatori NIP-05 come funzionalità
- Esistono numerosi provider NIP-05 gratuiti e a pagamento

## Fonti Primarie

- [Specifica NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md)

## Menzionato In

- [Newsletter #8 (2026-02-04)](/it/newsletters/2026-02-04-newsletter/) - PR che richiede minuscole per chiavi esadecimali e nomi
