---
title: "Cashu: Protocollo Ecash"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-04-22
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu è un protocollo ecash chaumiano costruito su Bitcoin e Lightning. Gli utenti detengono bearer token emessi da una mint, poi trasferiscono questi token senza esporre l'intero grafo dei pagamenti alla mint.

## Come funziona

Cashu usa firme cieche per emettere token ecash:

1. **Minting**: gli utenti depositano Bitcoin o Lightning presso una mint e ricevono token offuscati
2. **Spending**: i token possono essere trasferiti peer-to-peer senza coinvolgere la mint
3. **Redemption**: i destinatari riscattano i token presso la mint per Bitcoin o Lightning

La mint firma segreti offuscati, cosi può verificare in seguito i token senza vedere i segreti originali al momento dell'emissione. Questo rompe il collegamento diretto tra deposito e riscatto all'interno della mint.

## Modello di sicurezza e fiducia

Cashu migliora la privacy dei pagamenti, ma resta custodial. Una mint può rifiutare i riscatti, andare offline o perdere i fondi di copertura.

Le prove Cashu sono bearer instrument. Chi controlla la proof può spenderla. Questo rende la gestione delle proof più simile al contante che a un saldo di conto: backup, compromissione del dispositivo o perdita di token in chiaro contano subito.

## Integrazione con Nostr

Cashu si integra con Nostr in diversi modi:

- **Nutzaps**: token ecash inviati come zap con una privacy migliore
- **Escrow**: escrow di pagamento basato su HTLC per servizi come il ride-sharing
- **Wallet**: wallet nativi Nostr che conservano token Cashu cifrati sui relay
- **[NIP-87](/it/topics/nip-87/)**: discovery e review delle mint via Nostr
- **[TollGate](/it/topics/tollgate/)**: protocollo di accesso alla rete pay-per-use che accetta token ecash Cashu per la connettività, definito in [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) dalla [release v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)

## Compromessi

Cashu è veloce perché i trasferimenti avvengono off-chain e spesso off-mint fino al riscatto. Il compromesso riguarda interoperabilità e fiducia.

In pratica, gli utenti spesso devono usare la stessa mint oppure passare per uno swap o un bridge tra mint diverse. Per questo le applicazioni Nostr combinano spesso Cashu con discovery delle mint, sincronizzazione dei wallet e sistemi di recensione.

---

**Fonti primarie:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Menzionato in:**
- [Newsletter #7](/it/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/it/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Vedi anche:**
- [NIP-60: Cashu Wallet](/it/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/it/topics/nip-87/)
- [TollGate](/it/topics/tollgate/)
