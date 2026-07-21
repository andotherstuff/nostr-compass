---
title: "Protocollo Concord"
date: 2026-07-15
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
draft: false
categories:
  - Protocol
  - Messaging
---

Concord è un protocollo aperto, con licenza MIT, per community e canali end-to-end encrypted su Nostr, definito dalle [specifiche CORD-01 fino a CORD-07](https://github.com/concord-protocol/concord). [Vector](https://github.com/VectorPrivacy/Vector) lo ha adottato come trasporto predefinito per la funzione Group Chats a partire dalla v0.4.0, descrivendolo nelle proprie release note come "our custom messaging protocol", ma la specifica viene pubblicata separatamente da Vector e dispone già di implementazioni indipendenti.

## Come funziona

Concord scompone ciò che un community server in stile Discord fa normalmente in parti che non devono fidarsi di nessuno: i relay memorizzano esclusivamente blob cifrati indirizzati a etichette rotanti, possedere la chiave di una stanza è ciò che rende qualcuno membro, e l'autorità su ruoli, espulsioni e ban è un roster firmato radicato nell'identità del proprietario che ogni client verifica localmente invece di fidarsi di un server. Ogni event durevole utilizza lo stesso involucro a tre livelli: un kind 1059 wrap firmato con la stream key derivata del piano, contenente un seal firmato con la chiave reale dell'autore, contenente un rumor non firmato che trasporta l'event funzionale. Un rumor di messaggio chat è un semplice event kind 9:

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

Il traffico control, chat e guestbook riceve ciascuno il proprio piano [NIP-59](/it/topics/nip-59/) gift-wrapped, perciò un relay che detiene tutti e tre non può distinguere un messaggio di controllo da un messaggio chat o da una voce del guestbook senza la chiave della stanza. La specifica è suddivisa in sette documenti CORD: stream privati (01), community e membership (02), canali (03), ruoli (04), inviti (05), rekeying e ri-fondazione per escludere i membri rimossi (06), e audio/video tramite un blind token broker (07). La membership stessa non ha una lista lato server: chi può decifrare il piano è membro, e rimuovere davvero qualcuno significa far ruotare la community su una nuova key epoch e consegnarla solo a chi resta, invece di cancellare una riga da una tabella.

## Differenze rispetto a Marmot

Concord e [Marmot](/it/topics/marmot/) risolvono la messaggistica di gruppo cifrata su Nostr con crittografia differente per forme di gruppo differenti, e il confronto del progetto Concord è esplicito riguardo alla distinzione: Marmot sovrappone [MLS](/it/topics/mls/) a Nostr per forward secrecy e post-compromise security, utilizzando key package per dispositivo e commit ordinati che avanzano l'intero gruppo in sincrono. Questo offre garanzie forti, con costi che crescono al variare della membership, adatto a gruppi piccoli e ad alta sensibilità dove ingressi e uscite sono rari. Concord, al contrario, dà a ogni membro la stessa chiave della stanza ed esegue il rekeying dell'intera stanza alla rimozione invece di procedere con il ratchet per ogni commit, scambiando alcune delle garanzie crittografiche di MLS con un modello che resta economico quando una community cresce fino a centinaia o migliaia di membri occasionali con alto turnover, esattamente la forma che le community in stile Discord assumono nella pratica.

## Perché Vector ha cambiato

Le stesse [release note di Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) descrivono Concord solo come "our custom messaging protocol" per i Group Chats, senza indicare direttamente la motivazione. La coerenza con la ratio pubblicata di Concord è comunque chiara: i Group Chats in un client come Vector sono esattamente il caso con membership ampia, aperta e frequentemente variabile in cui lo stato MLS per dispositivo di Marmot diventa il percorso più costoso, e il design asincrono di Concord, con possibilità di unirsi in qualsiasi momento, è costruito proprio per quel caso. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) ha ritirato Marmot per i Group Chats a favore di Concord, e la cronologia dei gruppi Marmot esistenti non è stata trasferita nel passaggio. [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) ha distribuito "Concord v2" quattro giorni dopo con miglioramenti di privacy e stabilità. Nella stessa settimana, [Amethyst ha integrato la propria implementazione Concord clean-room e wire-compatible](https://github.com/vitorpamplona/amethyst/pull/3566), e il client in stile Discord di Soapbox, [Armada](https://gitlab.com/soapbox-pub/armada), costruisce già la funzione Communities sulla stessa specifica come implementazione di riferimento. Tre client indipendenti che convergono su una specifica aperta nell'arco di pochi giorni rappresentano un percorso rapido verso una reale interoperabilità tra client, un aspetto che vale la pena seguire rispetto a quanti degli altri client di group chat su Nostr rimarranno su Marmot.

## Implementazioni

- [Vector](https://github.com/VectorPrivacy/Vector) - messenger Nostr a singolo binario, incentrato sulla privacy; primo client Concord distribuito, nella v0.4.0
- [Armada](https://gitlab.com/soapbox-pub/armada) (Soapbox) - client community in stile Discord; implementazione di riferimento, backend nel repository separato `armada-relay`
- [Amethyst](https://github.com/vitorpamplona/amethyst) - client Nostr Android e multipiattaforma ricco di funzionalità; reimplementazione clean-room wire-compatible con Armada ([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**Fonti primarie:**
- [Specifiche del protocollo Concord (CORD-01 a CORD-07)](https://github.com/concord-protocol/concord)
- [Release note di Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Release note di Vector v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**Menzionato in:**
- [Newsletter #31: Vector v0.4.0 sposta i Group Chats da Marmot a Concord, e Amethyst distribuisce il proprio client Concord pochi giorni dopo](/it/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Amethyst distribuisce un'implementazione Concord clean-room per community end-to-end encrypted](/it/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**Vedi anche:**
- [Protocollo Marmot](/it/topics/marmot/)
- [MLS (Message Layer Security)](/it/topics/mls/)
- [NIP-46: Nostr Connect](/it/topics/nip-46/)
