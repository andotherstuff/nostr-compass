---
title: "NIP-03: attestazioni OpenTimestamps per gli event"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03 descrive come pubblicare una prova [OpenTimestamps](https://opentimestamps.org/) per un event Nostr. La prova attesta che l'event esisteva già al momento di un determinato blocco Bitcoin.

**Avviso:** la specifica attuale è etichettata `draft`, `optional` e `unrecommended`. Secondo la sua intestazione è vulnerabile a un attacco specifico e richiede un aggiornamento. Il testo non descrive l'attacco. Considerate il formato come un riferimento storico e non adottatelo per nuovi lavori finché la specifica non sarà rivista.

## Come funziona

Una prova viene pubblicata come event separato di kind 1040. Il suo tag `e` indica l'id dell'event di destinazione, insieme a un URL di relay, mentre il tag `k` registra il kind dell'event di destinazione. Come digest, la prova OpenTimestamps deve dimostrare proprio l'id dell'event di destinazione. All'id non viene applicato un ulteriore hash.

Il campo `content` contiene l'intero file `.ots`, codificato in base64, con almeno un'attestazione Bitcoin. La specifica raccomanda esattamente un'attestazione e nessuna attestazione in sospeso, dato che queste aggiungono byte senza aiutare la verifica.

Un verificatore recupera l'event di kind 1040, ne decodifica il contenuto e controlla la prova rispetto a Bitcoin. Se la prova è valida, dimostra che l'id dell'event era stato oggetto di commitment entro il blocco attestato. In questo modo si fissa per l'event un limite massimo alla data di creazione che non dipende dal valore `created_at` indicato dall'autore stesso. Non dimostra però che il contenuto dell'event sia vero.

## Storia

Con un [commit dell'11 ottobre 2023](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e) è cambiata la collocazione delle prove. Prima di quel commit, una prova era un campo `ots` allegato all'event stesso. Da allora, ogni prova è un event separato di kind 1040 che punta al proprio event di destinazione.

## Fonti primarie

- [Specifica attuale di NIP-03](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [Commit dell'11 ottobre 2023 che sposta le prove in event di kind 1040](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## Citato nelle newsletter

- [Newsletter #46 (2026-10-28): ottobre 2023, gli event trasportano evidenze e richieste di lavoro](/it/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## Vedi anche

- [NIP-01: protocollo di base](/it/topics/nip-01/)
