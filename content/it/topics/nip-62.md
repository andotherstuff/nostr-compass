---
title: "NIP-62: Richieste di Scomparsa"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 definisce le richieste di scomparsa, un meccanismo che permette agli utenti di richiedere ai relay la cancellazione dei loro contenuti. Sebbene i relay non siano obbligati a onorare queste richieste, supportare NIP-62 dà agli utenti più controllo sui loro dati pubblicati e fornisce un modo standardizzato per segnalare l'intento di cancellazione attraverso la rete.

## Come Funziona

Una richiesta di scomparsa è un event di kind 62 firmato dall'utente che vuole rimuovere i propri contenuti. La richiesta può mirare a event specifici includendo i loro ID nei tag `e`, oppure può richiedere la cancellazione di tutti i contenuti di quella pubkey omettendo del tutto i tag `e`.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Rimozione di vecchi post",
  "sig": "sig1234..."
}
```

Il campo `content` contiene opzionalmente una motivazione leggibile per la richiesta di cancellazione. Gli hint dei relay nei tag `e` indicano ai relay dove sono stati pubblicati gli event originali, anche se i relay possono onorare le richieste indipendentemente dal fatto che abbiano gli event specificati.

## Comportamento dei Relay

I relay che supportano NIP-62 dovrebbero cancellare gli event specificati dal loro storage e smettere di servirli agli iscritti. La richiesta di scomparsa stessa può essere conservata come registro che la cancellazione è stata richiesta, il che aiuta a prevenire che gli event cancellati vengano reimportati da altri relay.

Quando una richiesta di scomparsa omette tutti i tag `e`, i relay la interpretano come una richiesta di rimuovere tutti gli event di quella pubkey. Questa è un'azione più drastica e i relay possono gestirla diversamente, per esempio marcando la pubkey come "scomparsa" e rifiutando di accettare o servire qualsiasi suo event in futuro.

I relay non sono obbligati a supportare NIP-62. La rete Nostr è decentralizzata, e ogni operatore di relay decide le proprie politiche di conservazione dei dati. Gli utenti non dovrebbero assumere che i loro contenuti saranno cancellati ovunque semplicemente perché hanno pubblicato una richiesta di scomparsa.

## Considerazioni sulla Privacy

Le richieste di scomparsa sono un meccanismo di cancellazione best-effort, non una garanzia di privacy. Anche dopo aver pubblicato una richiesta di scomparsa, copie del contenuto potrebbero esistere altrove nella rete, incluso su altri relay che non supportano NIP-62, nelle cache locali sui dispositivi client, negli archivi di terze parti o nei motori di ricerca, e nei backup.

La richiesta stessa è anche un event Nostr firmato, il che significa che diventa parte del vostro registro pubblico. Chiunque veda la richiesta di scomparsa sa che avete cancellato qualcosa, anche se non può vedere cosa è stato cancellato.

Per contenuti che devono rimanere privati, considerate l'uso della messaggistica crittografata come [NIP-17](/it/topics/nip-17/) piuttosto che affidarvi alla cancellazione a posteriori.

---

**Fonti principali:**
- [Specifica NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Menzionato in:**
- [Newsletter #5: Modifiche Notevoli al Codice](/it/newsletters/2026-01-13-newsletter/#rust-nostr-libreria)
