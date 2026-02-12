---
title: "NIP-45 : Comptage d'événements"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 définit comment les clients demandent aux relais de compter les événements correspondant à un filtre sans transférer les événements eux-mêmes. Un client envoie un message COUNT avec la même syntaxe de filtre que REQ, et le relay répond avec un comptage.

## Fonctionnement

Une requête COUNT contient un ID d'abonnement et un filtre :

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

Le relay répond avec le comptage :

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Cela évite de télécharger des centaines ou milliers d'événements juste pour afficher un nombre.

## Comptage approximatif HyperLogLog

Depuis février 2026, NIP-45 prend en charge le comptage approximatif HyperLogLog (HLL) ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Un relay peut retourner des valeurs de registres HLL de 256 octets aux côtés des réponses COUNT :

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL résout un problème fondamental, celui du comptage d'événements distincts à travers plusieurs relais. Si le relay A rapporte 50 réactions et le relay B en rapporte 40, le total n'est pas 90 car de nombreux événements existent sur les deux relais. On fusionne les registres HLL de plusieurs relais en prenant la valeur maximale à chaque position de registre, dédupliquant automatiquement à travers le réseau.

Avec 256 registres, l'erreur standard est d'environ 5,2%. Des corrections HyperLogLog++ améliorent la précision pour les petites cardinalités sous environ 200 événements. Même deux événements de réaction consomment plus de bande passante que la charge utile HLL de 256 octets, rendant cette approche efficace pour tout comptage au-delà de nombres triviaux.

La spécification fixe le nombre de registres à 256 pour l'interopérabilité entre toutes les implémentations de relais.

## Cas d'utilisation

Les métriques sociales (nombre de followers, de réactions, de reposts) sont l'application principale. Sans HLL, un client doit soit interroger un seul relay << de confiance >> pour les comptages (centralisant les données), soit télécharger tous les événements de tous les relais pour dédupliquer localement (gaspillant la bande passante). HLL fournit des comptages approximatifs inter-relais avec 256 octets de surcharge par relay.

---

**Sources principales :**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Mentionné dans :**
- [Newsletter #9 : Approfondissement NIP](/fr/newsletters/2026-02-11-newsletter/#approfondissement-nip--nip-45-comptage-dévénements-et-hyperloglog)
- [Newsletter #9 : Mises à jour des NIP](/fr/newsletters/2026-02-11-newsletter/#mises-à-jour-des-nip)

**Voir aussi :**
- [NIP-11 : Document d'information du relay](/fr/topics/nip-11/)
