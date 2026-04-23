---
title: "TollGate: Internet pay-per-use su Nostr e Cashu"
date: 2026-04-22
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGate è un protocollo per vendere accesso alla rete in cambio di piccoli pagamenti frequenti in asset bearer. Un dispositivo che puo controllare la connettività, come un router WiFi, uno switch Ethernet o un tether Bluetooth, agisce come TollGate che pubblicizza i prezzi, accetta token ecash [Cashu](/it/topics/cashu/) e gestisce le sessioni. I clienti pagano esattamente per i minuti o i megabyte che consumano. Non ci sono account, abbonamenti o KYC.

## Come funziona

TollGate separa le responsabilità in tre livelli. Il livello protocollo definisce la forma degli eventi e la semantica dei pagamenti. Il livello interfaccia definisce come cliente e gate si scambiano questi eventi. Il livello medium descrive il collegamento fisico che trasporta il traffico pagato. Un TollGate funzionante combina una specifica per ogni livello, e alcune interfacce funzionano su relay Nostr mentre altre usano semplice HTTP.

Nel livello protocollo, [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) definisce tre eventi base: un kind Advertisement che elenca prezzi e mint accettate, un kind Session che traccia quanto il cliente ha pagato e quanto ha consumato, e un kind Notice per la messaggistica fuori banda. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) aggiunge i pagamenti Cashu, cosi un cliente puo riscattare token ecash di qualunque mint pubblicizzata dal TollGate e ricevere credito di sessione in cambio.

Nel livello interfaccia, [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) fino a HTTP-03 definiscono la superficie HTTP per dispositivi su sistemi operativi restrittivi che non possono aprire facilmente connessioni WebSocket verso relay arbitrari, mentre [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) definisce il trasporto tramite relay Nostr per i client che possono farlo. Nel livello medium, [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) descrive come una configurazione WiFi captive portal identifica e instrada i clienti paganti.

Poiché l'asset di pagamento è un bearer token invece di una credenziale, il cliente non ha bisogno di accesso Internet precedente per produrlo. Un token Cashu presente in un wallet locale basta da solo per acquistare il primo minuto di connettività, dopodiché il cliente puo ricaricare con altri token secondo necessità. I TollGate possono anche acquistare uplink gli uni dagli altri, quindi la portata si estende oltre un singolo operatore.

## Perché conta

Il WiFi a pagamento convenzionale si basa su account, captive portal e carte di pagamento, ognuno dei quali aggiunge attrito e una traccia di dati. Il modello di TollGate trasforma la connettività in una commodity che qualunque router puo vendere a qualunque cliente pagante senza sapere chi sia. Questa astrazione permette a operatori indipendenti di fissare i propri prezzi, accettare le mint preferite e competere su copertura e qualità invece che sul lock-in.

La [release v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) è il primo snapshot versionato di queste specifiche. Non standardizza ogni dettaglio, ma fissa una porzione sufficiente della superficie per permettere a firmware per router, wallet client e rivenditori multi-hop di iniziare a costruire contro un riferimento stabile.

---

**Fonti primarie:**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: Base Events](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: Cashu payments](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 through HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [TollGate repository](https://github.com/OpenTollGate/tollgate)

**Menzionato in:**
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Vedi anche:**
- [Cashu](/it/topics/cashu/)
- [NIP-60: Cashu Wallet](/it/topics/nip-60/)
