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

Cashu ist ein Chaumian ecash-Protokoll, das auf Bitcoin und Lightning aufbaut. Nutzer halten Bearer-Tokens, die von einem Mint ausgegeben wurden, und können diese Tokens dann übertragen, ohne dem Mint den vollständigen Payment Graph offenzulegen.

## Funktionsweise

Cashu nutzt Blind Signatures, um ecash-Tokens auszugeben:

1. **Minting**: Nutzer zahlen Bitcoin oder Lightning an einen Mint ein und erhalten verblindete Tokens.
2. **Spending**: Tokens können peer-to-peer ohne Beteiligung des Mints übertragen werden.
3. **Redemption**: Empfänger lösen Tokens beim Mint gegen Bitcoin oder Lightning ein.

Der Mint signiert verblindete Geheimnisse, sodass er Tokens später verifizieren kann, ohne die ursprünglichen Geheimnisse bei der Ausgabe gesehen zu haben. Das durchtrennt die direkte Verknüpfung zwischen Einzahlung und Einlösung innerhalb des Mints.

## Sicherheits- und Vertrauensmodell

Cashu verbessert die Zahlungs-Privatsphäre, bleibt aber custodial. Ein Mint kann Einlösungen verweigern, offline gehen oder die Deckung verlieren.

Cashu-Proofs sind Bearer-Instrumente. Wer den Proof kontrolliert, kann ihn ausgeben. Deshalb ähnelt der Umgang mit Proofs eher Bargeld als einem Kontostand. Backup, Device-Kompromittierung oder plaintext geleakte Tokens haben sofortige Auswirkungen.

## Nostr-Integration

Cashu integriert sich auf mehrere Arten in Nostr:

- **Nutzaps**: Ecash-Tokens, die mit verbesserter Privatsphäre als zaps gesendet werden
- **Escrow**: HTLC-basiertes Payment-Escrow für Dienste wie Ride-Sharing
- **Wallets**: Nostr-native Wallets speichern verschlüsselte Cashu-Tokens auf Relays
- **[NIP-87](/de/topics/nip-87/)**: Mint-Discovery und Reviews über Nostr
- **[TollGate](/de/topics/tollgate/)**: Pay-per-use-Protokoll für Netzwerkzugang, das Cashu-ecash-Tokens für Konnektivität akzeptiert, definiert in [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) im [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)

## Tradeoffs

Cashu ist schnell, weil Transfers off-chain und oft bis zur Einlösung auch off-mint stattfinden. Der Tradeoff liegt bei Interoperabilität und Vertrauen.

In der Praxis brauchen Nutzer oft denselben Mint oder einen Swap beziehungsweise eine Bridge zwischen Mints. Deshalb kombinieren Nostr-Anwendungen Cashu häufig mit Mint-Discovery, Wallet-Sync und Review-Systemen.

---

**Primärquellen:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Erwähnt in:**
- [Newsletter #7](/de/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/de/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/de/topics/nip-87/)
- [TollGate](/de/topics/tollgate/)
