---
title: "NIP-05: Verifica del dominio"
date: 2026-02-04
translationOf: /en/topics/nip-05/
translationDate: 2026-03-07
draft: false
categories:
  - Identity
  - Discovery
---
NIP-05 associa le chiavi pubbliche Nostr a identificatori internet leggibili dalle persone come `user@example.com`. Offre agli utenti un indizio di identità basato su DNS che i client possono verificare via HTTPS.

## Come funziona

Un utente rivendica un identificatore aggiungendo un campo `nip05` ai metadati del proprio profilo. L'identificatore segue il formato `name@domain`. I client verificano l'asserzione recuperando `https://domain/.well-known/nostr.json` e controllando che il nome corrisponda alla pubkey dell'utente.

Il file JSON nel percorso well-known contiene un oggetto `names` che associa i nomi locali alle pubkey hex:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Quando la verifica riesce, i client possono mostrare l'identificatore al posto dell'npub o accanto a esso. Alcuni client mostrano un indicatore di verifica, mentre altri mostrano l'identificatore come testo semplice e lasciano la decisione di fiducia al lettore.

## Modello di fiducia

NIP-05 non è un registro globale di username. Prova il controllo di un nome di dominio e di un percorso del web server, non l'identità legale o la continuità a lungo termine di un account. Se il proprietario di un dominio cambia la mappatura in seguito, i client verificheranno la nuova mappatura a meno che non conservino lo stato precedente.

Questo rende NIP-05 utile per discoverability e reputazione, ma più debole di quanto spesso gli utenti presumano. Un buon client dovrebbe trattarlo come controllo verificato del dominio, non come prova che una persona o un'organizzazione sia davvero ciò che dichiara di essere.

## Relay hints

Il file `nostr.json` può includere opzionalmente un oggetto `relays` che associa le pubkey a array di relay URL. Questo aiuta i client a scoprire dove trovare gli eventi di un utente specifico.

## Note di interoperabilità

Il requisito del lowercase conta più di quanto sembri. Nomi o pubkey con maiuscole e minuscole miste possono funzionare in un'implementazione e fallire in un'altra, quindi i client attuali dovrebbero aspettarsi nomi lowercase e chiavi hex lowercase in `nostr.json`.

Un altro dettaglio pratico è il nome speciale `_`, che permette a un dominio di mappare la forma di identificatore senza nome come `_@example.com` o semplicemente `example.com` nei client che la supportano. Non tutti i client espongono quella forma nello stesso modo, quindi gli utenti ottengono ancora i risultati più coerenti con identificatori espliciti `name@domain`.

## Stato di implementazione

La maggior parte dei client principali supporta la verifica NIP-05:
- Damus, Amethyst, Primal mostrano identificatori verificati
- Molti servizi relay offrono identificatori NIP-05 come funzionalità
- Esistono numerosi provider NIP-05 gratuiti e a pagamento

---

**Fonti primarie:**
- [NIP-05 Specification](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - requisito lowercase per nomi e chiavi hex

**Menzionato in:**
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-01: Protocollo di base](/it/topics/nip-01/)
- [NIP-65: Relay List Metadata](/it/topics/nip-65/)
