---
title: "NIP-13: Proof of Work"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13 definisce un sistema proof-of-work per gli eventi Nostr, richiedendo sforzo computazionale per creare eventi come meccanismo di prevenzione dello spam.

## Come Funziona

Il proof of work è dimostrato trovando un ID evento (hash SHA256) con un numero specificato di bit zero iniziali:

1. **Difficoltà**: Misurata in bit zero iniziali (es., 20 bit = 2^20 tentativi in media)
2. **Tag Nonce**: Gli eventi includono un tag `nonce` con il valore nonce e la difficoltà target
3. **Verifica**: Relay e client possono verificare rapidamente che il lavoro è stato fatto

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Livelli di Difficoltà

| Bit | Tentativi Medi | Uso Tipico |
|-----|----------------|------------|
| 8 | 256 | Deterrente spam minimo |
| 16 | 65.536 | Filtraggio leggero |
| 20 | 1.048.576 | Protezione moderata |
| 24 | 16.777.216 | Forte resistenza allo spam |

## Casi d'Uso

- **Ammissione Relay**: I relay possono richiedere PoW minimo per l'accettazione degli eventi
- **Rate Limiting**: Difficoltà maggiore per azioni come la registrazione account
- **Filtraggio Spam**: I client possono dare priorità agli eventi ad alto PoW nei feed
- **Bootstrap Reputazione**: I nuovi account possono dimostrare impegno via PoW

## Limitazioni

- Favorisce gli utenti con hardware potente
- Preoccupazioni sul consumo energetico
- Non previene tutto lo spam, alza solo il costo

## Correlati

- [NIP-01](/it/topics/nip-01/) - Protocollo Base
