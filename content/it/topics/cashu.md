---
title: "Cashu: Protocollo ecash"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-03-07
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---
Cashu è un protocollo ecash chaumiano costruito su Bitcoin e Lightning. Gli utenti detengono bearer token emessi da una mint, poi trasferiscono quei token senza esporre alla mint l'intero grafo dei pagamenti.

## Come funziona

Cashu usa blind signatures per emettere token ecash:

1. **Minting**: gli utenti depositano Bitcoin/Lightning presso una mint e ricevono token accecati
2. **Spending**: i token possono essere trasferiti peer-to-peer senza coinvolgere la mint
3. **Redemption**: i destinatari riscattano i token presso la mint per ottenere Bitcoin/Lightning

La mint firma segreti accecati, quindi può verificare i token in seguito senza vedere i segreti originali al momento dell'emissione. Questo interrompe il collegamento diretto tra deposito e riscatto all'interno della mint.

## Modello di sicurezza e fiducia

Cashu migliora la privacy dei pagamenti, ma resta custodial. Una mint può rifiutare i riscatti, andare offline o perdere i fondi di copertura.

Le proof Cashu sono strumenti al portatore. Chiunque controlli la proof può spenderla. Questo rende la gestione delle proof più vicina al contante che a un saldo di conto: backup, compromissione del dispositivo o fuga di token in chiaro contano subito.

## Integrazione con Nostr

Cashu si integra con Nostr in vari modi:

- **Nutzaps**: token ecash inviati come zaps con maggiore privacy
- **Escrow**: escrow di pagamento basato su HTLC per servizi come il ridesharing
- **Wallets**: wallet nativi Nostr archiviano token Cashu cifrati sui relay
- **[NIP-87](/it/topics/nip-87/)**: scoperta e recensioni delle mint tramite Nostr

## Compromessi

Cashu è veloce perché i trasferimenti avvengono off-chain e spesso off-mint fino al riscatto. Il compromesso riguarda interoperabilità e fiducia.

In pratica, gli utenti spesso devono usare la stessa mint, oppure hanno bisogno di uno swap o di un bridge tra mint. Per questo le applicazioni Nostr combinano spesso Cashu con scoperta delle mint, sincronizzazione del wallet e sistemi di recensione.

---

**Fonti primarie:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60: Cashu Wallet](/it/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/it/topics/nip-87/)

**Citato in:**
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/en/newsletters/2026-02-25-newsletter/)

**Vedi anche:**
- [NIP-60: Cashu Wallet](/it/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/it/topics/nip-87/)
