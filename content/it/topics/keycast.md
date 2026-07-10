---
title: "Keycast: firma remota Nostr per team"
date: 2026-05-21
draft: false
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
categories:
  - Signing
  - Security
  - Teams
---

Keycast è un server di firma remota NIP-46 self-hosted costruito per i team. Memorizza le chiavi private Nostr cifrate a riposo in SQLite, genera stringhe di connessione bunker NIP-46 ed esegue processi di firma che approvano o negano le richieste di firma remota secondo policy configurabili per singola chiave. Il progetto è mantenuto dall'organizzazione Marmot Protocol.

## Come funziona

Il server ha quattro componenti principali: un'API Axum che gestisce la gestione dei team e l'auth HTTP NIP-98, un frontend web SvelteKit che utilizza NIP-07 per l'autenticazione, un signer manager che monitora le righe di autorizzazione e avvia un `signer_daemon` per ogni autorizzazione, e un database SQLite con migrazioni.

I membri del team accedono tramite la loro estensione browser NIP-07. L'app web richiede un evento di auth HTTP NIP-98 firmato localmente dall'estensione, quindi invia quell'header di auth all'API. L'API verifica l'evento, estrae il pubkey e controlla l'appartenenza al team. Le chiavi memorizzate sono cifrate con un file `master.key` radice che deve essere montato separatamente dall'immagine e mai committato.

Il signer daemon decifra la chiave memorizzata e la chiave bunker all'avvio, si connette ai relay configurati e chiama `Authorization::validate_policy` prima di approvare ogni richiesta di firma NIP-46. Le policy specificano quali kind di evento una particolare connessione bunker è autorizzata a firmare.

## Audit di sicurezza (maggio 2026)

Un audit di sicurezza completato a maggio 2026 ha affrontato problemi di auth, permessi, integrità dei dati e dipendenze. Modifiche principali:

- L'auth NIP-98 ora richiede esattamente un tag `u` e un tag `method`, rifiuta timestamp obsoleti o futuri e convalida gli hash del `payload` del corpo della richiesta
- `ALLOWED_PUBKEYS` viene analizzato in modo esatto e applicato lato server; il frontend espone `/api/config?pubkey=<hex>` in modo che il browser possa verificare lo stato dell'allowlist senza ricevere l'elenco completo del server
- Le policy vuote negano di default le richieste sign/encrypt/decrypt; la creazione di policy rifiuta configurazioni di permessi sconosciute o malformate
- Le connessioni SQLite abilitano l'applicazione delle foreign key; l'eliminazione di un team non perde più i dati di join dei permessi prima della pulizia
- La protezione delle route lato server ora copre le route annidate dell'app come `/teams/:id`
- Le risposte web impostano gli header CSP, frame, content-type, referrer, permissions e HSTS
- Una migrazione SQL normalizza il vecchio JSON dei permessi degli allowed-kinds da `{"sign":[...]}` a `{"allowed_kinds":[...]}` all'avvio

L'audit segnala elementi residui in [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) prima di affidare al deployment vere chiavi di team.

## Deployment

Il deployment tramite Docker Compose monta `master.key` nei container API e signer, esegue i container come UID/GID non root con un filesystem radice in sola lettura e utilizza le label di Caddy per instradare `/api/*` all'API e tutto il resto all'app web. L'immagine pubblicata su `ghcr.io/marmot-protocol/keycast` è taggata con `master`, `latest` e `sha-<commit>`.

---

**Fonti primarie:**
- [Repository Keycast](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - Risultati dell'audit di sicurezza di maggio 2026

**Menzionato in:**
- [Newsletter #23: Audit di sicurezza Keycast completato](/it/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**Vedi anche:**
- [NIP-46: Firma remota Nostr](/it/topics/nip-46/)
- [NIP-07: Signer da estensione browser](/it/topics/nip-07/)
- [Marmot Protocol](/it/topics/marmot/)
