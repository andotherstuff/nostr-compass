---
title: "Öffentliche FIPS-Domains"
date: 2026-09-30
draft: false
categories:
  - Protocol
  - Networking
  - Identity
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-01
---

fips-pub-domains ist eine frühe Implementierung zur Auflösung vertrauter Internet-Domainnamen zu [FIPS](/de/topics/fips/)-Mesh-Diensten. Sie veröffentlicht signierte Nostr-Behauptungen, aber eine Signatur beweist nur, wer eine Behauptung aufgestellt hat. Ein Client muss außerdem DNS- oder DNSSEC-Nachweise, einen vertrauenswürdigen Zeugen oder eine zuvor fest hinterlegte Zuordnung prüfen, bevor er denjenigen, der die Behauptung aufgestellt hat, als Domaininhaber behandelt.

## Verifizierung und Offline-Nutzung

Die [erste Veröffentlichung](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0) führte die Behauptung, den Resolver-Daemon und die Android-Integration ein. [Version 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0) kann einer Behauptung einen DNSSEC-Nachweis beifügen. Dadurch kann ein Client, der nur einen Mesh-relay sieht, eine zuvor unbekannte signierte Domain anhand der DNS-Root-Schlüssel verifizieren. Sie unterstützt außerdem mehr als einen verifizierten Server für eine Domain. [Version 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) korrigierte die mitgelieferte Server-Unit und stellte sie auf den Betrieb ohne root um; bestehende Installationen benötigen die Ersatz-Unit.

Die [Testnotizen](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md) des Projekts beschreiben Fälle mit zwei Knoten und mit einem ausschließlich über das Mesh erreichbaren relay. Es handelt sich um von den Maintainern gemeldete Tests, nicht um einen Nachweis für einen breiteren Einsatz. Der [NIP-DB-Vorschlag](https://github.com/nostr-protocol/nips/pull/2487) des Projekts ist offen, und die event-kind-Nummern im Entwurf sind Platzhalter statt zugewiesener Nostr-kinds.

---

**Primärquellen:**
- [Repository und README](https://github.com/fr34aky/fips-pub-domains)
- [Veröffentlichungen 0.1.0–0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [Vorgeschlagener NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Testnotizen](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Erwähnt in:**
- [Newsletter #42: fips-pub-domains](/de/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**Siehe auch:**
- [FIPS](/de/topics/fips/)
