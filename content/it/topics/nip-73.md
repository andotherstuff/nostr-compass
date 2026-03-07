---
title: "NIP-73: External Content IDs"
date: 2026-02-04
translationOf: /en/topics/nip-73.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---
NIP-73 definisce un modo standard per fare riferimento a contenuti esterni all'interno degli eventi Nostr. Usa tag `i` per l'identificatore stesso e tag `k` per il tipo di identificatore, così i client possono raggruppare la discussione attorno allo stesso libro, sito web, episodio di podcast, luogo, hashtag o oggetto blockchain.

## Come funziona

Un evento che usa NIP-73 include un tag `i` contenente un identificatore esterno normalizzato e un tag `k` che descrive di che tipo di identificatore si tratta. I client possono quindi interrogare tutti gli eventi che fanno riferimento allo stesso soggetto.

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

La specifica copre diverse famiglie di identificatori, tra cui:

- URL web normalizzati senza fragment
- ISBN per i libri
- ISAN per i film
- geohash e codici paese o suddivisione ISO 3166
- GUID di feed, episodio e publisher di podcast
- hashtag
- identificatori di transazioni e indirizzi blockchain

## Regole di normalizzazione

Il dettaglio principale di NIP-73 lato lettore è la normalizzazione. Lo stesso soggetto dovrebbe corrispondere a una stringa canonica, altrimenti i client dividono la discussione tra più identificatori che indicano la stessa cosa.

Esempi dalla specifica:

- i geohash usano `geo:<value>` e devono essere in lowercase
- i codici paese e di suddivisione usano `iso3166:<code>` e devono essere in uppercase
- gli ISBN omettono i trattini
- gli URL web rimuovono i fragment
- gli hash di transazione blockchain usano hex lowercase

Sembra un dettaglio minore, ma è la differenza tra una conversazione condivisa e diversi indici incompatibili.

## Schemi utili

NIP-73 è un livello di riferimento generale, non un formato di contenuto. Una nota long-form può puntare a un ISBN di un libro, una recensione può puntare a un ISAN di un film e un post locale può puntare a un geohash o a un codice paese senza inventare ogni volta un tag personalizzato.

La specifica consente anche un hint URL opzionale come secondo valore di un tag `i`. Questo dà ai client un link di fallback quando non hanno un renderer personalizzato per quel tipo di identificatore.

## Perché è importante

Nostr ha già riferimenti interni solidi per eventi e profili. NIP-73 estende quell'idea a elementi esterni a Nostr. Una volta che gli identificatori sono normalizzati, commenti, valutazioni, highlight e trusted assertions possono tutti collegarsi allo stesso soggetto esterno su client diversi.

Questo è anche il motivo per cui NIP-85 si basa su NIP-73. Trusted Assertions può valutare non solo utenti ed eventi, ma anche identificatori NIP-73 come libri, siti web, hashtag e luoghi.

---

**Fonti principali:**
- [NIP-73 Specification](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Aggiunge codici paese e di suddivisione ISO 3166

**Menzionato in:**
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**Vedi anche:**
- [NIP-85: Trusted Assertions](/it/topics/nip-85/)
