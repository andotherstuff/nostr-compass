---
title: "NIP-98: HTTP Auth"
date: 2026-03-25
translationOf: /en/topics/nip-98.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-98 definisce l'autenticazione HTTP usando event Nostr. Permette ai server di verificare l'identità Nostr di un client sulle richieste HTTP standard senza password, chiavi API o flussi OAuth.

## Come Funziona

Quando un client deve autenticare una richiesta HTTP, crea un event di kind 27235. Questo event contiene l'URL di destinazione e il metodo HTTP nei suoi tag, vincolando l'autenticazione a una richiesta specifica.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1742860800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

Il client firma questo event, lo codifica in base64 e lo invia nell'header HTTP `Authorization` con lo schema `Nostr`:

```
Authorization: Nostr <base64-encoded-signed-event>
```

Il server decodifica l'event, verifica la firma, controlla che URL e metodo corrispondano alla richiesta effettiva, e conferma che il timestamp sia recente. Se tutti i controlli passano, il server sa quale pubkey Nostr ha effettuato la richiesta.

Il tag opzionale `payload` contiene un hash SHA-256 del corpo della richiesta, che impedisce il riutilizzo dell'event di auth con contenuti diversi. Il controllo del timestamp (i server tipicamente rifiutano event più vecchi di pochi minuti) previene gli attacchi di replay.

## Casi d'Uso

I server Blossom usano NIP-98 per autenticare i caricamenti e le cancellazioni di file, legando i media archiviati a un'identità Nostr specifica. I servizi di hosting file lo usano per applicare quote di caricamento per pubkey. Qualsiasi API HTTP che deve identificare un utente Nostr senza mantenere il proprio sistema di account può accettare header NIP-98 come prova di identità.

---

**Fonti primarie:**
- [Specifica NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**Menzionato in:**
- [Newsletter #15](/it/newsletters/2026-03-25-newsletter/)
