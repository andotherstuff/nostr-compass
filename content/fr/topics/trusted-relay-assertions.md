---
title: "Assertions de Relais de Confiance"
date: 2026-01-21
draft: false
categories:
  - Protocol
  - Relays
---

Les Assertions de Relais de Confiance est une proposition de NIP brouillon pour standardiser la notation de confiance des relais et la gestion de la réputation. La spécification introduit des événements kind 30385 où les fournisseurs d'assertions publient des scores de confiance calculés à partir de métriques observées, de la réputation de l'opérateur et des rapports utilisateurs.

## Comment ça fonctionne

La proposition comble une lacune dans l'écosystème des relais. Alors que [NIP-11](/fr/topics/nip-11/) définit ce que les relais revendiquent à propos d'eux-mêmes et [NIP-66](/fr/topics/nip-66/) mesure ce que nous observons, les Assertions de Relais de Confiance standardisent ce que nous concluons sur la fiabilité des relais.

Les fournisseurs d'assertions calculent des scores sur trois dimensions. La fiabilité mesure la disponibilité, la vitesse de récupération, la cohérence et la latence. La qualité évalue la documentation des politiques, la sécurité TLS et la responsabilité de l'opérateur. L'accessibilité évalue les barrières d'accès, la liberté juridictionnelle et le risque de surveillance. Un score de confiance global (0-100) combine ces composantes avec des pondérations : 40% fiabilité, 35% qualité, 25% accessibilité.

Chaque assertion inclut des niveaux de confiance (faible, moyen, élevé) basés sur les comptages d'observation. La vérification de l'opérateur utilise plusieurs méthodes : preuve cryptographique via des documents NIP-11 signés, enregistrements DNS TXT ou fichiers .well-known. La spécification intègre le Web of Trust via des scores de confiance d'opérateur. La classification des politiques aide les utilisateurs à trouver des relais appropriés : ouverts, modérés, curés ou spécialisés.

Les utilisateurs déclarent les fournisseurs d'assertions de confiance via des événements kind 10385. Les clients interrogent plusieurs fournisseurs et comparent les scores. La proposition inclut un processus d'appel où les opérateurs de relais peuvent contester les scores en utilisant des événements d'étiquetage [NIP-32](/fr/topics/nip-32/).

## Cas d'utilisation

Pour les signataires distants [NIP-46](/fr/topics/nip-46/), les assertions de confiance aident les utilisateurs à évaluer les relais inconnus intégrés dans les URI de connexion avant d'accepter les connexions. Combiné avec les listes de relais [NIP-65](/fr/topics/nip-65/), les clients peuvent prendre des décisions de sélection de relais informées basées à la fois sur les préférences utilisateur et les évaluations de confiance tierces.

La spécification complète les mécanismes de découverte de relais existants. [NIP-66](/fr/topics/nip-66/) fournit la découverte (ce qui existe), cette proposition ajoute l'évaluation (ce qui est bon). Ensemble, ils permettent une sélection de relais informée plutôt que de s'appuyer sur des valeurs par défaut codées en dur ou des recommandations de bouche à oreille.

---

**Sources principales :**
- [Document NIP brouillon](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - Événement kind 30817 proposant la spécification

**Mentionné dans :**
- [Newsletter #6 : Actualités](/fr/newsletters/2026-01-21-newsletter/#assertions-de-relais-de-confiance-une-nouvelle-approche-de-la-confiance-des-relais)
- [Newsletter #6 : Mises à jour des NIP](/fr/newsletters/2026-01-21-newsletter/#mises-à-jour-des-nip)

**Voir aussi :**
- [NIP-11 : Document d'information de relais](/fr/topics/nip-11/)
- [NIP-66 : Découverte de relais et surveillance de disponibilité](/fr/topics/nip-66/)
- [NIP-32 : Étiquetage](/fr/topics/nip-32/)
