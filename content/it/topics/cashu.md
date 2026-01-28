---
title: "Cashu: Protocollo Ecash"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu è un protocollo ecash Chaumiano costruito su Bitcoin e Lightning Network, che consente pagamenti privati, istantanei e a basso costo attraverso token crittografici.

## Come Funziona

Cashu usa firme cieche per creare token ecash non tracciabili:

1. **Minting**: Gli utenti depositano Bitcoin/Lightning presso un mint e ricevono token oscurati
2. **Spesa**: I token possono essere trasferiti peer-to-peer senza coinvolgimento del mint
3. **Riscatto**: I destinatari riscattano i token presso il mint per Bitcoin/Lightning

Il mint non può collegare i depositi ai riscatti grazie al processo di oscuramento, fornendo forti garanzie di privacy.

## Proprietà Chiave

- **Privacy**: Il mint non può tracciare i trasferimenti di token tra utenti
- **Istantaneo**: I trasferimenti avvengono offline, nessuna conferma blockchain necessaria
- **Basso costo**: Nessuna commissione on-chain per i trasferimenti di token
- **Custodiale**: Gli utenti si fidano del mint per onorare i riscatti

## Integrazione con Nostr

Cashu si integra con Nostr in diversi modi:

- **Nutzaps**: Token ecash inviati come zap con privacy migliorata
- **Escrow**: Escrow di pagamento basato su HTLC per servizi come il ridesharing
- **Wallet**: Wallet nativi Nostr memorizzano token Cashu crittografati sui relay
- **[NIP-87](/it/topics/nip-87/)**: Scoperta e recensioni dei mint via Nostr

## Modello di Fiducia

A differenza del Bitcoin in auto-custodia, Cashu richiede di fidarsi degli operatori del mint. Gli utenti dovrebbero:
- Usare mint affidabili e ben recensiti
- Mantenere saldi piccoli appropriati al livello di fiducia
- Capire che i mint possono fare exit-scam o andare offline, portando via i fondi

## Correlati

- [NIP-87](/it/topics/nip-87/) - Raccomandazioni Mint Cashu
- [NIP-60](/it/topics/nip-60/) - Nostr Wallet
