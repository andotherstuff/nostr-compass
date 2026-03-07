---
title: "Cashu: Ecash-protocol"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-03-07
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu is een Chaumiaans ecash-protocol gebouwd op Bitcoin en Lightning. Gebruikers houden bearer tokens aan die door een mint zijn uitgegeven en dragen die tokens vervolgens over zonder de volledige betalingsgrafiek aan de mint bloot te leggen.

## Hoe Het Werkt

Cashu gebruikt blind signatures om ecash-tokens uit te geven:

1. **Minting**: Gebruikers storten Bitcoin/Lightning bij een mint en ontvangen geblindeerde tokens
2. **Spending**: Tokens kunnen peer-to-peer worden overgedragen zonder betrokkenheid van de mint
3. **Redemption**: Ontvangers wisselen tokens bij de mint in voor Bitcoin/Lightning

De mint ondertekent geblindeerde geheimen, zodat zij tokens later kan verifiëren zonder de oorspronkelijke geheimen op het moment van uitgifte te zien. Dat doorbreekt binnen de mint de directe koppeling tussen storting en inwisseling.

## Security- en trustmodel

Cashu verbetert de privacy van betalingen, maar blijft custodial. Een mint kan inwisselingen weigeren, offline gaan of de dekking van de fondsen verliezen.

Cashu proofs zijn bearer instruments. Wie de proof beheert, kan hem uitgeven. Dat maakt het omgaan met proofs meer vergelijkbaar met contant geld dan met een rekeningsaldo: backups, apparaatcompromittering of plaintext-tokenlekken hebben meteen gevolgen.

## Nostr-integratie

Cashu integreert op verschillende manieren met Nostr:

- **Nutzaps**: Ecash-tokens verstuurd als zaps met extra privacy
- **Escrow**: HTLC-gebaseerde payment escrow voor diensten zoals ridesharing
- **Wallets**: Nostr-native wallets slaan versleutelde Cashu-tokens op relays op
- **[NIP-87](/nl/topics/nip-87/)**: Ontdekking en reviews van mints via Nostr

## Afwegingen

Cashu is snel omdat overdrachten off-chain plaatsvinden en vaak ook off-mint blijven tot de inwisseling. De afweging zit in interoperabiliteit en vertrouwen.

In de praktijk hebben gebruikers vaak dezelfde mint nodig, of ze hebben een swap of bridge tussen mints nodig. Daarom combineren Nostr-applicaties Cashu vaak met mint discovery, wallet sync en reviewsystemen.

---

**Primaire bronnen:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/nl/topics/nip-87/)

**Vermeld in:**
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/en/newsletters/2026-02-25-newsletter/)

**Zie ook:**
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/nl/topics/nip-87/)
