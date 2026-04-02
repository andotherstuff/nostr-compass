---
title: "Bitcredit"
date: 2026-03-25
translationOf: /en/topics/bitcredit.md
translationDate: 2026-04-01
draft: false
categories:
  - Finance
  - Commerce
  - Infrastructure
---

Bitcredit è un sistema di trade-finance basato su e-bill per le aziende. Il sito pubblico presenta Bitcredit Core come software per emettere, girare, pagare e gestire cambiali elettroniche, mentre il repository open-source core implementa un livello di trasporto Nostr insieme alla logica di business e ai crate di persistenza.

## Come Funziona

Bitcredit modella il credito commerciale come cambiali elettroniche, o ebill. Un acquirente emette una ebill con una data di scadenza futura, il detentore può girarla a un'altra azienda, e il detentore finale può richiedere il pagamento alla scadenza.

Il sito di Bitcredit descrive anche un percorso di liquidità basato su mint. Invece di attendere la scadenza, un detentore può richiedere un'offerta da un mint Bitcredit, ricevere ecash immediatamente, e poi usare quell'ecash per pagare fornitori o lavoratori.

## Note sull'Implementazione

Il repository `Bitcredit-Core` suddivide il sistema in più crate Rust. `bcr-ebill-core` gestisce il modello dati, `bcr-ebill-api` contiene la logica di business, `bcr-ebill-persistence` gestisce lo storage, e `bcr-ebill-transport` fornisce l'API di trasporto di rete con un'implementazione Nostr.

Questa architettura è importante perché Bitcredit non è solo un sito web o un flusso wallet. È un sistema di documenti commerciali con trasporto, stato e logica di regolamento separati in componenti riutilizzabili, incluso un entrypoint WASM per i deployment web.

## Lavoro Recente

Compass ha trattato Bitcredit per la prima volta a marzo 2026, quando la `v0.5.3` ha aggiunto campi API per le azioni di pagamento delle cambiali e lo stato delle cambiali, e ha corretto la gestione degli indirizzi di firma per i firmatari anonimi. Il rilascio successivo, `v0.5.4`, ha continuato quel lavoro sulle API adattando `BitcreditBillResult`, perfezionando lo stato di pagamento e accettazione, e aggiungendo una gestione più esplicita per i campi opzionali.

Queste modifiche sono piccole rispetto al concetto più ampio di Bitcredit, ma mostrano dove si sta muovendo l'implementazione: ergonomia frontend più pulita, stato del ciclo di vita delle cambiali più chiaro, e migliore gestione per i flussi di firma anonimi o al portatore.

---

**Fonti primarie:**
- [Sito web Bitcredit](https://www.bit.cr/)
- [Bitcredit: Come funziona](https://www.bit.cr/how-it-works)
- [Repository Bitcredit-Core](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Indice documentazione Bitcredit-Core](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846: Improve Status Flags and Add Payment Actions](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849: Fix signing address and signatory for anon signers](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**Menzionato in:**
- [Newsletter #13: Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
