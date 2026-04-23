---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - DVM
---
NIP-90 definisce le Data Vending Machines (DVM), un protocollo per richiedere e consegnare lavoro computazionale a pagamento su Nostr.

## Come funziona

I clienti pubblicano eventi di richiesta lavoro nell'intervallo `5000-5999`. Ogni richiesta può includere uno o più tag `i` per gli input, tag `param` per impostazioni specifiche del lavoro, un tag `output` per il formato atteso, un limite massimo `bid` e relay hints che indicano dove devono comparire le risposte. I fornitori di servizi rispondono con un kind di risultato corrispondente nell'intervallo `6000-6999`, sempre `1000` più alto del kind della richiesta.

I risultati includono la richiesta originale, la pubkey del cliente e, facoltativamente, un tag `amount` o una invoice. I fornitori possono anche inviare eventi di feedback kind `7000` come `payment-required`, `processing`, `partial`, `error` o `success`, che danno ai client un modo per mostrare l'avanzamento prima che arrivi il risultato finale.

## Pagamento e privacy

Il protocollo lascia intenzionalmente aperta la logica di business. Un fornitore può chiedere il pagamento prima che il lavoro inizi, dopo aver restituito un campione oppure dopo aver consegnato il risultato completo. Questa flessibilità conta perché i lavori DVM vanno da trasformazioni di testo economiche a elaborazioni GPU costose, e non tutti i fornitori accettano lo stesso livello di rischio di pagamento.

Se un cliente vuole input privati, la richiesta può spostare i dati `i` e `param` in `content` cifrato e contrassegnare l'evento con un tag `encrypted` più il tag `p` del fornitore. Questo protegge prompt o materiale sorgente dagli osservatori dei relay, ma significa anche che il cliente deve puntare a un fornitore specifico invece di trasmettere una richiesta aperta al mercato.

## Note di interoperabilità

NIP-90 supporta il concatenamento dei lavori tramite tag `i` con input type `job`, così un risultato può alimentare una richiesta successiva. Questo rende possibili flussi a più passaggi senza inventare un livello di orchestrazione separato.

La scoperta dei fornitori è esterna al ciclo richiesta/risposta vero e proprio. La specifica rimanda agli annunci di [NIP-89: Recommended Application Handlers](/it/topics/nip-89/) per pubblicizzare i kind di lavoro supportati, ed è così che i client possono scoprire i vendor prima di pubblicare una richiesta.

---

**Fonti primarie:**
- [NIP-90 Specification](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Menzionato in:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/it/newsletters/2026-02-25-newsletter/)

**Vedi anche:**
- [NIP-89: Recommended Application Handlers](/it/topics/nip-89/)
