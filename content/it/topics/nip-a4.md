---
title: "NIP-A4: Messaggi pubblici"
date: 2025-12-24
translationOf: /en/topics/nip-a4/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---
NIP-A4 definisce i messaggi pubblici (kind 24) pensati per le schermate di notifica, con l'obiettivo di un ampio supporto da parte dei client.

## Come funziona

Il kind `24` è un messaggio signed plaintext destinato a uno o più destinatari. Il corpo del messaggio si trova in `content`, e i tag `p` identificano i destinatari previsti. La specifica dice che i client dovrebbero inviare questi eventi agli inbox relay dei destinatari secondo [NIP-65](/it/topics/nip-65/) e all'outbox relay del mittente.

A differenza delle conversazioni con thread, questi messaggi non hanno alcun concetto di cronologia della chat, stato della stanza o radici del thread. Sono pensati per apparire in una superficie di notifica ed essere comprensibili da soli.

## Regole del protocollo

- Usa i tag `p` per identificare i destinatari
- Non deve usare tag `e` per il threading
- Può usare tag `q` per citare un altro evento
- Funziona meglio con i tag di scadenza di [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), così i messaggi in stile notifica obsoleti scompaiono nel tempo

## Perché esiste

NIP-A4 offre ai client una primitiva di messaggio pubblico più semplice di una nota completa con thread. È utile per messaggi in stile mention, shoutout leggeri o notifiche isolate in cui costruire un albero di conversazione permanente aggiungerebbe più complessità che valore.

Il compromesso è che questi messaggi sono pubblici. Sono facili da mostrare in una UI di notifica proprio perché non creano stato privato di sessione. Chiunque può leggerli e rispondere se li vede.

## Note di interoperabilità

NIP-A4 è facile da confondere con i protocolli di direct message perché punta a destinatari nominati, ma resta un kind di evento pubblico. I client non dovrebbero presentare il kind `24` come messaggistica privata né assumere alcuna riservatezza oltre al posizionamento sui relay.

---

**Fonti primarie:**
- [Specifica NIP-A4](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [PR di NIP-A4](https://github.com/nostr-protocol/nips/pull/1988)

**Citato in:**
- [Newsletter #2: Aggiornamenti NIP](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: Riepilogo di dicembre](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-01: Protocollo di base](/it/topics/nip-01/)
- [NIP-10: Threading delle text note](/it/topics/nip-10/)
