---
title: "NIP-13: Proof of Work"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Spam Prevention
---
NIP-13 definisce un sistema di proof-of-work per gli eventi Nostr, che richiede sforzo computazionale per creare eventi come meccanismo di prevenzione dello spam.

## Come funziona

Il proof of work viene dimostrato trovando un ID evento (hash SHA256) con un numero specificato di bit zero iniziali:

1. **Difficoltà**: misurata in bit zero iniziali (ad esempio, 20 bit = 2^20 tentativi in media)
2. **Tag Nonce**: gli eventi includono un tag `nonce` con il valore del nonce e la difficoltà obiettivo
3. **Verifica**: relay e client possono verificare rapidamente che il lavoro sia stato svolto

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Livelli di difficoltà

| Bits | Average Attempts | Typical Use |
|------|------------------|-------------|
| 8 | 256 | Minimal spam deterrent |
| 16 | 65,536 | Light filtering |
| 20 | 1,048,576 | Moderate protection |
| 24 | 16,777,216 | Strong spam resistance |

## Perché è importante

- **Ammissione ai relay**: i relay possono richiedere un PoW minimo per accettare un evento
- **Rate limiting**: una difficoltà più alta per azioni come la registrazione degli account
- **Filtro dello spam**: i client possono dare priorità nei feed agli eventi con PoW elevato
- **Bootstrap della reputazione**: i nuovi account possono dimostrare impegno tramite PoW

La proprietà utile è il costo asimmetrico. Creare molti eventi accettabili diventa costoso per il mittente, mentre controllare la prova resta economico per relay e client.

## Compromessi

- Favorisce gli utenti con hardware potente
- Problemi di consumo energetico
- Non impedisce tutto lo spam, ne aumenta soltanto il costo

Il PoW sposta anche la resistenza allo spam dall'identità dell'account alla disponibilità di calcolo. Questo può aiutare in ambienti permissionless, ma non distingue tra un nuovo utente legittimo e uno spammer ben finanziato.

---

**Fonti principali:**
- [Specifica NIP-13](https://github.com/nostr-protocol/nips/blob/master/13.md)

**Menzionato in:**
- [Newsletter #7: News](/en/newsletters/2026-01-28-newsletter/#news)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**Vedi anche:**
- [NIP-01: Basic Protocol](/it/topics/nip-01/)
