---
title: "NIP-42: Autenticazione dei client ai relay"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Authentication
---
NIP-42 definisce come i client si autenticano ai relay. I relay possono richiedere autenticazione per fornire controllo di accesso, prevenire abusi o implementare servizi di relay a pagamento.

## Come funziona

Il flusso di autenticazione inizia quando un relay invia un messaggio `AUTH` al client. Questo messaggio contiene una stringa challenge che il client deve firmare. Il client crea un evento di autenticazione kind 22242 che contiene la challenge e lo firma con la propria chiave privata. Il relay verifica la firma e la challenge, poi concede l'accesso.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

La challenge impedisce attacchi replay. L'URL del relay nei tag impedisce che lo stesso evento firmato venga riusato su relay diversi.

## Note sul protocollo

L'autenticazione è limitata alla connessione. Una challenge resta valida per la durata della connessione, o finché il relay non ne invia una nuova. L'evento firmato è effimero e non deve essere trasmesso come un normale evento.

La spec definisce anche prefissi di errore machine-readable. `auth-required:` significa che il client non si è ancora autenticato. `restricted:` significa che si è autenticato, ma quella pubkey non ha ancora il permesso per l'azione richiesta.

## Casi d'uso

I relay a pagamento usano NIP-42 per verificare gli abbonati prima di concedere accesso. I relay privati lo usano per limitare letture o scritture alle pubkeys approvate. Migliora anche il rate limiting perché i relay possono tracciare il comportamento per chiave autenticata invece che per indirizzo IP.

Combinato con i metadati [NIP-11](/it/topics/nip-11/), i client possono scoprire se un relay supporta NIP-42 prima di tentare query protette. In pratica, il supporto è ancora disomogeneo, quindi i client hanno bisogno di un percorso di fallback quando un relay dichiara NIP-42 ma gestisce gli eventi protetti in modo scorretto.

---

**Fonti primarie:**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Autenticazione dei client ai relay

**Citato in:**
- [Newsletter #6: Relay Information Documents](/it/newsletters/2026-01-21-newsletter/)
- [Newsletter #9: Marmot Relay Status Testing](/it/newsletters/2026-02-11-newsletter/)
- [Newsletter #10: Nostr MCP Server](/it/newsletters/2026-02-18-newsletter/)

**Vedi anche:**
- [NIP-11: Relay Information Document](/it/topics/nip-11/)
- [NIP-50: Search Capability](/it/topics/nip-50/)
