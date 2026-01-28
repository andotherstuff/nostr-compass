---
title: "NIP-42: Autenticazione dei client verso i relay"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 definisce come i client si autenticano verso i relay. I relay possono richiedere l'autenticazione per fornire controllo degli accessi, prevenire abusi o implementare servizi relay a pagamento.

## Come Funziona

Il flusso di autenticazione inizia quando un relay invia un messaggio AUTH al client. Questo messaggio contiene una stringa di challenge che il client deve firmare. Il client crea un evento di autenticazione kind 22242 contenente la challenge e lo firma con la sua chiave privata. Il relay verifica la firma e la challenge, poi concede l'accesso.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "stringa-challenge-casuale"]
  ],
  "content": "",
  "pubkey": "<pubkey_client>",
  "created_at": 1736784000,
  "sig": "<firma>"
}
```

La challenge previene attacchi replay: i client devono firmare challenge fresche per ogni tentativo di autenticazione. L'URL del relay nei tag assicura che i token di autenticazione non possano essere riutilizzati tra relay diversi.

## Casi d'Uso

I relay a pagamento usano NIP-42 per verificare gli abbonati prima di concedere l'accesso. Dopo l'autenticazione, i relay possono controllare lo stato del pagamento o la scadenza dell'abbonamento. I relay privati restringono l'accesso a pubkey approvate, creando community chiuse o infrastruttura relay personale.

Il rate limiting diventa più efficace con l'autenticazione. I relay possono tracciare le frequenze di richiesta per pubkey autenticata piuttosto che per indirizzo IP, prevenendo abusi mentre supportano utenti legittimi dietro IP condivisi. La prevenzione dello spam migliora quando i relay richiedono l'autenticazione per pubblicare eventi.

Alcuni relay usano NIP-42 per analytics, tracciando quali utenti accedono a quali contenuti senza richiedere account centralizzati. Combinato con i metadati [NIP-11](/it/topics/nip-11/), i client scoprono se i relay richiedono autenticazione prima di tentare le connessioni.

---

**Fonti primarie:**
- [Specifica NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) - Autenticazione dei client verso i relay

**Vedi anche:**
- [NIP-11: Documento Informativo del Relay](/it/topics/nip-11/)
- [NIP-50: Capacità di Ricerca](/it/topics/nip-50/)
