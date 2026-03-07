---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) ist ein Schwellenwert-Signaturschema, das einer Gruppe ermöglicht, eine gültige Schnorr-Signatur zu erzeugen, ohne dass ein Teilnehmer den vollständigen privaten Schlüssel besitzt.

## Wie es funktioniert

FROST ermöglicht T-of-N-Signierung. Jede Schwellenwert-Gruppe von Teilnehmern kann kooperieren, um eine Signatur für den öffentlichen Schlüssel der Gruppe zu erzeugen.

Das Signierungsprotokoll verwendet zwei Runden:

1. **Commitment-Runde**: Jeder Teilnehmer erzeugt und teilt kryptographische Commitments
2. **Signatur-Runde**: Teilnehmer kombinieren ihre partiellen Signaturen zu einer finalen aggregierten Signatur

Das finale Ergebnis verifiziert wie eine gewöhnliche Schnorr-Signatur. Verifizierer sehen eine Signatur unter einem öffentlichen Schlüssel, keine Liste von Mitunterzeichnern.

## Sicherheitshinweise

Die Nonce-Verwaltung ist entscheidend. Das RFC stellt ausdrücklich klar, dass Signing-Nonces nur einmalig verwendet werden dürfen. Wiederverwendung kann Schlüsselmaterial preisgeben.

Das RFC standardisiert auch keine verteilte Schlüsselgenerierung. Es spezifiziert das Signierungsprotokoll selbst und enthält die Trusted-Dealer-Schlüsselgenerierung nur im Anhang. In der Praxis hängt die Sicherheit einer FROST-Implementierung sowohl vom Signing-Ablauf als auch davon ab, wie Shares erstellt und gespeichert wurden.

## Anwendungsfälle in Nostr

Im Kontext von Nostr kann FROST Folgendes unterstützen:

- **Quorum-Governance**: Gruppen können einen nsec durch T-of-N-Schemata teilen, wobei Mitglieder sich selbst vertreten oder an Räte delegieren können
- **Multi-Sig-Administration**: Community-Moderation, die mehrere Admin-Signaturen erfordert
- **Dezentrales Schlüsselmanagement**: Verteilung des Vertrauens auf mehrere Parteien für kritische Operationen

## Status

FROST ist in [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/) spezifiziert, das im Juni 2024 im IRTF-Stream veröffentlicht wurde. Das gibt dem Protokoll eine stabile öffentliche Spezifikation, aber es ist kein IETF-Standards-Track-RFC.

---

**Primärquellen:**
- [RFC 9591: FROST-Protokoll](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Zcash Foundation Rust-Implementierung](https://github.com/ZcashFoundation/frost)

**Erwähnt in:**
- [Newsletter #3: NIPs Repository](/en/newsletters/2025-12-31-newsletter/#nips-repository)
- [Newsletter #8](/en/newsletters/2026-02-04-newsletter/)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)

**Siehe auch:**
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
- [NIP-55: Android Signer Application](/de/topics/nip-55/)
