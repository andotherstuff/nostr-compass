---
title: "Cashu: Ecash Protocol"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-04-22
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu is een Chaumian ecash-protocol gebouwd op Bitcoin en Lightning. Gebruikers houden bearer tokens aan die door een mint zijn uitgegeven en dragen die vervolgens over zonder de volledige betalingsgrafiek aan de mint bloot te stellen.

## Hoe Het Werkt

Cashu gebruikt blind signatures om ecash tokens uit te geven:

1. **Minting**: Gebruikers storten Bitcoin/Lightning bij een mint en ontvangen blinded tokens
2. **Spending**: Tokens kunnen peer-to-peer worden overgedragen zonder betrokkenheid van de mint
3. **Redemption**: Ontvangers wisselen tokens bij de mint in voor Bitcoin/Lightning

De mint signet blinded secrets, zodat die tokens later kan verifiëren zonder de oorspronkelijke secrets op het moment van uitgifte te zien. Dat verbreekt de directe link tussen storting en inwisseling binnen de mint.

## Security And Trust Model

Cashu verbetert betalingsprivacy, maar blijft custodial. Een mint kan inwisselingen weigeren, offline gaan of backing funds verliezen.

Cashu proofs zijn bearer instruments. Wie de proof beheert, kan die uitgeven. Dat maakt omgang met proofs meer vergelijkbaar met contant geld dan met een accountsaldo: backups, device compromise of plaintext token leakage zijn direct relevant.

## Nostr Integratie

Cashu integreert op meerdere manieren met Nostr:

- **Nutzaps**: Ecash tokens verzonden als zaps met meer privacy
- **Escrow**: HTLC-gebaseerde payment escrow voor diensten zoals ridesharing
- **Wallets**: Nostr-native wallets slaan encrypted Cashu tokens op relays op
- **[NIP-87](/nl/topics/nip-87/)**: Mint discovery en reviews via Nostr
- **[TollGate](/nl/topics/tollgate/)**: Pay-per-use network access-protocol dat Cashu ecash tokens voor connectiviteit accepteert, gedefinieerd in [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) vanaf de [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)

## Afwegingen

Cashu is snel omdat transfers off-chain plaatsvinden en vaak ook off-mint tot het moment van inwisseling. De tradeoff is interoperabiliteit en vertrouwen.

In de praktijk hebben gebruikers vaak dezelfde mint nodig, of ze hebben een swap of bridge tussen mints nodig. Daarom combineren Nostr-applicaties Cashu vaak met mint discovery, wallet sync en reviewsystemen.

---

**Primaire bronnen:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Vermeld in:**
- [Newsletter #7](/nl/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/nl/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/nl/topics/nip-87/)
- [TollGate](/nl/topics/tollgate/)
