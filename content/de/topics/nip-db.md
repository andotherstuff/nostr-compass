---
title: "Vorgeschlagener NIP-DB: Bindungen zwischen Domains und Diensten"
date: 2026-09-30
draft: false
categories:
  - Proposals
  - Networking
  - Identity
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-01
---

NIP-DB ist ein **offener Vorschlag**, um eine gewöhnliche Internetdomain an einen über einen Schlüssel adressierten Dienst zu binden. Seine event-kinds und Formulierungen werden weiterhin geprüft; diese Seite stellt ihn nicht als akzeptierte Nostr-Spezifikation dar.

## Verifikationsmodell

Ein Schlüssel, der einen Dienst bereitstellt, kann eine signierte Erklärung veröffentlichen, die die Domain und den Dienst benennt. Der Vorschlag beschreibt optionale DNS- oder DNSSEC-Nachweise, Bestätigungen durch Zeugen und einen Zoneneintrag für Namen unter der Domain. Eine Signatur beweist, welcher Schlüssel eine Erklärung veröffentlicht hat, beweist aber nicht die Kontrolle über die Domain. Ein Client muss die Bindung anhand von DNS-Nachweisen, einem vertrauenswürdigen Zeugen oder einem zuvor fest hinterlegten Schlüssel verifizieren, bevor er sie zur Auflösung eines Namens verwendet.

[fips-pub-domains](/de/topics/fips-pub-domains/) ist die Referenzimplementierung des Autors für das FIPS-Mesh. Die dokumentierten Tests mit zwei Knoten und ausschließlich innerhalb des Meshs sind vom Maintainer berichtete Implementierungsnachweise. Sie schließen weder die noch offene Prüfung des Vorschlags ab noch belegen sie einen breiteren Einsatz.

---

**Primärquellen:**
- [Offener Pull Request zu NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Entwurf des Autors und Platzhalter für event-kinds](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [Referenzimplementierung und Tests](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Erwähnt in:**
- [Newsletter #42: öffentliche Domains](/de/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Newsletter #42: vorgeschlagener NIP-DB](/de/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
