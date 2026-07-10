---
title: "NIP-37: Draft Wraps"
date: 2026-07-01
draft: false
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37 definisce un evento di archiviazione cifrato per eventi bozza non firmati di qualsiasi tipo. Un utente che sta redigendo un articolo long-form, un evento di calendario imminente o un messaggio che potrebbe voler inviare in seguito può archiviare la bozza sui relay sotto un evento di kind `31234`, cifrato verso la propria chiave con [NIP-44](/it/topics/nip-44/). La bozza è recuperabile da qualsiasi client che possieda la chiave dell'utente, e la stessa NIP definisce un evento di elenco separato `kind:10013` che indica i relay su cui l'utente vuole che vengano archiviate le sue bozze private.

## Come funziona

Un draft wrap è un evento replaceable parametrizzato di kind `31234`. L'evento bozza non firmato viene serializzato in JSON, cifrato tramite NIP-44 verso la chiave pubblica del signer e inserito in `.content`. Un tag `k` dichiara il kind della bozza in modo che un client possa raggruppare le bozze per tipo di evento. Un tag `d` porta l'identificatore della bozza affinché il wrap possa essere sostituito man mano che la bozza evolve, ed è raccomandato un tag `expiration` NIP-40 in modo che le vecchie bozze scadano automaticamente.

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

Un campo `.content` svuotato segnala che la bozza è stata eliminata.

## Checkpoint

Il kind `1234` definisce i checkpoint che appartengono a un evento `kind:31234` genitore. I checkpoint portano un tag `a` che punta alla bozza genitore e permettono a un client di archiviare la cronologia delle revisioni insieme all'ultima bozza.

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## Elenco di relay per contenuti privati (kind 10013)

Il kind `10013` è un evento replaceable i cui tag elencano i relay su cui l'utente vuole archiviare contenuti privati, inclusi i draft wrap. I client che pubblicano il kind `31234` DOVREBBERO pubblicare sui relay elencati nell'evento kind `10013` dell'utente. Questo separa l'insieme di relay usati per la pubblicazione pubblica (NIP-65) dall'insieme di relay usati per l'archiviazione di contenuti privati, in modo che un utente possa fissare le bozze private su un piccolo insieme di relay fidati senza esporre quell'insieme nella propria outbox pubblica.

## Implementazioni

- [Notedeck](https://github.com/damus-io/notedeck) - memorizza i relay di sincronizzazione privata come elenco di kind-10013 (aggiunto nel 2026-06)

---

**Fonti primarie:**
- [Specifica NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Commit di Notedeck che memorizza i relay di sincronizzazione privata come kind-10013](https://github.com/damus-io/notedeck) - Il team Damus adotta la specifica per la gestione dei relay di sincronizzazione desktop

**Menzionato in:**
- [Newsletter #29: Notedeck](/it/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**Vedi anche:**
- [NIP-44: Cifratura versionata](/it/topics/nip-44/)
- [NIP-65: Metadati dell'elenco di relay](/it/topics/nip-65/)
