---
title: "Proposition NIP-DB : liaisons entre domaines et services"
date: 2026-09-30
draft: false
categories:
  - Proposals
  - Networking
  - Identity
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-01
---

NIP-DB est une **proposition ouverte** visant à lier un domaine Internet ordinaire à un service adressé par clé. Ses kinds d'event et sa formulation restent soumis à examen ; cette page ne la présente pas comme une spécification Nostr acceptée.

## Modèle de vérification

Une clé utilisée par le service peut publier une déclaration signée désignant le domaine et le service. La proposition décrit des preuves DNS ou DNSSEC facultatives, des attestations de témoins et un enregistrement de zone pour les noms sous le domaine. Une signature prouve quelle clé a publié une déclaration, mais ne prouve pas le contrôle du domaine. Un client doit vérifier la liaison à l'aide de preuves DNS, d'un témoin de confiance ou d'une clé préalablement épinglée avant de l'utiliser pour résoudre un nom.

[fips-pub-domains](/fr/topics/fips-pub-domains/) est l'implémentation de référence de l'auteur pour le réseau maillé FIPS. Ses tests documentés à deux nœuds et limités au réseau maillé constituent des éléments probants sur l'implémentation rapportés par le mainteneur. Ils ne tranchent pas l'examen encore ouvert de la proposition et n'établissent pas l'existence d'un déploiement plus large.

---

**Sources primaires :**
- [Pull request ouverte pour NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Brouillon de l'auteur et valeurs provisoires des kinds d'event](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [Implémentation de référence et tests](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Mentionné dans :**
- [Lettre d'information #42 : domaines publics](/fr/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Lettre d'information #42 : proposition NIP-DB](/fr/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
