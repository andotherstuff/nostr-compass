---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - Kryptografie
  - Protokoll
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) ist ein Schwellenwertsignaturverfahren, das es einer Gruppe von Teilnehmern ermöglicht, gemeinsam gültige Schnorr-Signaturen zu erstellen, ohne dass eine einzelne Partei den vollständigen privaten Schlüssel besitzt.

## Funktionsweise

FROST ermöglicht T-von-N-Schwellenwertsignaturen, bei denen T Teilnehmer von insgesamt N Schlüsselinhabern zusammenarbeiten müssen, um eine gültige Signatur zu erstellen. Das Protokoll arbeitet in zwei Runden:

1. **Commitment-Runde**: Jeder Teilnehmer generiert und teilt kryptografische Commitments
2. **Signatur-Runde**: Die Teilnehmer kombinieren ihre Teilsignaturen zu einer endgültigen aggregierten Signatur

Die resultierende Signatur ist von einer Standard-Schnorr-Signatur nicht zu unterscheiden und gewährleistet Rückwärtskompatibilität mit bestehenden Verifizierungssystemen.

## Wichtige Eigenschaften

- **Schwellenwertsicherheit**: Kein einzelner Teilnehmer kann alleine signieren; T Parteien müssen zusammenarbeiten
- **Rundeneffizienz**: Nur zwei Kommunikationsrunden sind für die Signatur erforderlich
- **Fälschungsschutz**: Neuartige Techniken schützen vor Angriffen auf frühere Schwellenwertverfahren
- **Signatur-Aggregation**: Mehrere Signaturen werden zu einer einzigen kompakten Signatur kombiniert
- **Privatsphäre**: Endsignaturen verraten nicht, welche T Teilnehmer signiert haben

## Anwendungsfälle in Nostr

Im Kontext von Nostr ermöglicht FROST:

- **Quorum-Governance**: Gruppen können einen nsec durch T-von-N-Schemata teilen, wobei Mitglieder sich selbst vertreten oder an Räte delegieren können
- **Multi-Signatur-Administration**: Gemeinschaftsmoderation, die mehrere Administratorsignaturen erfordert
- **Dezentrale Schlüsselverwaltung**: Verteilung des Vertrauens auf mehrere Parteien für kritische Operationen

## Standardisierung

FROST wurde im Juni 2024 als RFC 9591 standardisiert, mit dem Titel "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures".

---

**Primärquellen:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Erwähnt in:**
- [Newsletter #3: NIPs-Repository](/de/newsletters/2025-12-31-newsletter/#nips-repository)

**Siehe auch:**
- [NIP-XX Quorum-Vorschlag](https://github.com/nostr-protocol/nips/pull/2179)
