---
title: "Cashu: Ecash-Protokoll"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-03-07
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu ist ein Chaumsches Ecash-Protokoll, das auf Bitcoin und Lightning aufbaut. Nutzer halten Bearer-Token, die von einer Mint ausgegeben werden, und übertragen diese Token, ohne dem Mint den vollständigen Zahlungsgraph offenzulegen.

## Wie es funktioniert

Cashu verwendet blinde Signaturen zur Ausgabe von Ecash-Token:

1. **Minting**: Nutzer hinterlegen Bitcoin/Lightning bei einer Mint und erhalten blind signierte Token
2. **Ausgabe**: Token können Peer-to-Peer ohne Beteiligung der Mint übertragen werden
3. **Einlösung**: Empfänger lösen Token bei der Mint gegen Bitcoin/Lightning ein

Die Mint signiert verblendete Geheimnisse und kann Token später verifizieren, ohne die ursprünglichen Geheimnisse zum Zeitpunkt der Ausgabe zu kennen. Das unterbricht den direkten Zusammenhang zwischen Einzahlung und Einlösung innerhalb der Mint.

## Sicherheit und Vertrauensmodell

Cashu verbessert die Zahlungsprivatsphäre, ist aber weiterhin verwahrt. Eine Mint kann Einlösungen ablehnen, offline gehen oder Deckungsmittel verlieren.

Cashu-Proofs sind Bearer-Instrumente. Wer den Proof kontrolliert, kann ihn ausgeben. Das macht die Handhabung von Proofs eher wie Bargeld als wie ein Kontoguthaben: Backup, Gerätekompromittierung oder der Verlust von Token im Klartext wirken sich sofort aus.

## Nostr-Integration

Cashu ist auf verschiedene Weisen in Nostr integriert:

- **Nutzaps**: Ecash-Token als Zaps mit erweitertem Datenschutz gesendet
- **Escrow**: HTLC-basiertes Zahlungs-Escrow für Dienste wie Mitfahrangebote
- **Wallets**: Nostr-native Wallets speichern verschlüsselte Cashu-Token auf Relays
- **[NIP-87](/de/topics/nip-87/)**: Mint-Entdeckung und Bewertungen über Nostr

## Kompromisse

Cashu ist schnell, weil Übertragungen off-chain und oft ohne Mint-Beteiligung bis zur Einlösung stattfinden. Der Kompromiss liegt bei Interoperabilität und Vertrauen.

In der Praxis benötigen Nutzer oft dieselbe Mint oder einen Swap bzw. eine Brücke zwischen Mints. Deshalb kombinieren Nostr-Anwendungen Cashu häufig mit Mint-Entdeckung, Wallet-Synchronisierung und Bewertungssystemen.

---

**Primärquellen:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Kryptographie und Modelle](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/de/topics/nip-87/)

**Erwähnt in:**
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/en/newsletters/2026-02-25-newsletter/)

**Siehe auch:**
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/de/topics/nip-87/)
