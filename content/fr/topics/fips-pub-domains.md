---
title: "Domaines publics FIPS"
date: 2026-09-30
draft: false
categories:
  - Protocol
  - Networking
  - Identity
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-01
---

fips-pub-domains est une implémentation préliminaire permettant de résoudre des noms de domaine Internet familiers vers des services du réseau maillé [FIPS](/fr/topics/fips/). Elle publie des revendications Nostr signées, mais une signature prouve uniquement qui a émis une revendication. Un client doit également vérifier des éléments de preuve DNS ou DNSSEC, un témoin de confiance ou une association préalablement épinglée avant de considérer l'auteur de la revendication comme le propriétaire du domaine.

## Vérification et utilisation hors ligne

La [première version](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0) a ajouté la revendication, le démon de résolution et l'intégration Android. La [version 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0) peut joindre une preuve DNSSEC à une revendication, permettant à un client qui ne voit qu'un relay du réseau maillé de vérifier un domaine signé qu'il n'avait jamais vu auparavant à l'aide des clés racines du DNS. Elle prend également en charge plusieurs serveurs vérifiés pour un même domaine. La [version 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) a corrigé l'unité serveur fournie dans le paquet et l'a modifiée pour qu'elle s'exécute sans les privilèges root ; les installations existantes ont besoin de l'unité de remplacement.

Les [notes de test](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md) du projet décrivent des cas à deux nœuds et des cas où les relay ne sont accessibles que par le réseau maillé. Il s'agit de tests rapportés par les mainteneurs, et non de preuves d'un déploiement plus large. Sa [proposition NIP-DB](https://github.com/nostr-protocol/nips/pull/2487) est ouverte, et les numéros de kind d'event figurant dans son brouillon sont des valeurs provisoires plutôt que des kind Nostr attribués.

---

**Sources primaires :**
- [Dépôt et README](https://github.com/fr34aky/fips-pub-domains)
- [Versions 0.1.0–0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [Proposition NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Notes de test](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Mentionné dans :**
- [Lettre d'information #42 : fips-pub-domains](/fr/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**Voir aussi :**
- [FIPS](/fr/topics/fips/)
