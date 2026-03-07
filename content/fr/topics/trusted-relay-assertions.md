---
title: "Trusted Relay Assertions"
date: 2026-01-21
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocole
  - Relays
---

Trusted Relay Assertions désigne l'idée de publier sur Nostr des évaluations tierces signées des relays afin que les clients puissent choisir leurs relays avec plus de contexte que les seules métadonnées auto-déclarées. Le bloc standardisé actuel est [NIP-85: Trusted Assertions](/fr/topics/nip-85/), qui définit comment les utilisateurs font confiance à des fournisseurs et comment ces fournisseurs publient des résultats calculés et signés.

## Comment ça fonctionne

La sélection des relays comporte trois couches. [NIP-11: Relay Information Document](/fr/topics/nip-11/) couvre ce qu'un relay dit de lui-même. [NIP-66: Relay Discovery and Liveness Monitoring](/fr/topics/nip-66/) couvre ce que des observateurs peuvent mesurer, comme la disponibilité et la latence. Trusted relay assertions cherchent à combler le manque restant : ce qu'un tiers conclut à partir de ces données, et si un client décide de faire confiance à cette conclusion.

Dans le modèle plus large de NIP-85, les utilisateurs nomment des fournisseurs de confiance avec des événements kind `10040`, et les fournisseurs publient des événements d'assertion adressables et signés. Une application d'évaluation de relays aurait alors besoin de deux éléments supplémentaires sur lesquels les clients s'accordent : la manière d'identifier un relay comme sujet, et les tags de résultat qui représentent le score et les preuves qui l'étayent.

Cette distinction compte parce que le transport et la délégation de confiance sont standardisés, mais que le modèle de notation spécifique aux relays reste un motif applicatif. Différents fournisseurs peuvent être légitimement en désaccord sur ce qui rend un relay digne de confiance.

## Modèle de confiance

Les scores de confiance des relays ne sont pas des faits objectifs. Un fournisseur peut privilégier l'uptime et le débit d'écriture, un autre la juridiction, la politique de modération ou l'identité de l'opérateur, et un troisième la résistance à la surveillance. Un client utile devrait montrer qui a produit le score, pas seulement le score lui-même.

C'est aussi là que [Web of Trust](/fr/topics/web-of-trust/) entre en jeu. Si un client fait déjà confiance à certaines personnes ou à certains services, il peut préférer des évaluations de relays provenant de ce même voisinage social au lieu de prétendre qu'il existe un classement global unique.

## Pourquoi c'est important

Pour les signers distants [NIP-46](/fr/topics/nip-46/), les connexions de wallet ou toute application qui suggère des relays peu familiers, des évaluations tierces de relays peuvent réduire la confiance aveugle dans les valeurs par défaut. Combinées aux listes de relays [NIP-65](/fr/topics/nip-65/), les clients peuvent séparer "quels relays j'utilise" de "quels relays je juge dignes de confiance pour cette tâche".

Le principal point d'attention sur l'exactitude concerne la portée. La newsletter de janvier 2026 décrivait la notation de confiance des relays comme une proposition dédiée, mais le standard fusionné dans le dépôt NIPs est le format plus large [NIP-85: Trusted Assertions](/fr/topics/nip-85/). La notation des relays reste un cas d'usage construit au-dessus de ce modèle, pas un format filaire finalisé et séparé pour la confiance des relays.

---

**Sources principales :**
- [Spécification NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534)

**Mentionné dans :**
- [Newsletter #6 : Actualités](/fr/newsletters/2026-01-21-newsletter/#assertions-de-relais-de-confiance-une-nouvelle-approche-de-la-confiance-des-relais)
- [Newsletter #6 : Mises à jour des NIP](/fr/newsletters/2026-01-21-newsletter/#mises-à-jour-des-nip)
- [Newsletter #7 : Mises à jour des NIP](/fr/newsletters/2026-01-28-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-11 : Document d'information de relais](/fr/topics/nip-11/)
- [NIP-66 : Découverte de relais et surveillance de disponibilité](/fr/topics/nip-66/)
- [NIP-85 : Trusted Assertions](/fr/topics/nip-85/)
- [Web of Trust](/fr/topics/web-of-trust/)
