---
title: "NIP-29 : Groupes basés sur les relais"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-03-11
draft: false
categories:
  - Social
  - Groups
---

NIP-29 définit les groupes basés sur les relais, où un relais gère l'appartenance au groupe, les permissions et la visibilité des messages.

## Fonctionnement

Les groupes sont identifiés par un hôte de relais associé à un identifiant de groupe, et le relais fait autorité pour l'appartenance et la modération. Les événements créés par les utilisateurs et envoyés dans un groupe portent un tag `h` contenant l'identifiant du groupe. Les métadonnées générées par le relais utilisent des événements adressables signés par la propre clé du relais.

L'événement de métadonnées principal est le kind 39000, tandis que les kinds 39001 à 39003 décrivent les administrateurs, les membres et les rôles pris en charge. Les actions de modération s'effectuent via des événements de la série 9000 tels que `put-user`, `remove-user`, `edit-metadata` et `create-invite`.

## Modèle d'accès

- **private** : Seuls les membres peuvent lire les messages du groupe
- **closed** : Les demandes d'adhésion sont ignorées, sauf si le relais utilise un système de codes d'invitation
- **hidden** : Le relais masque les métadonnées du groupe aux non-membres, rendant le groupe indécouvrable
- **restricted** : Seuls les membres peuvent écrire des messages dans le groupe

Ces tags sont indépendants. Un groupe peut être lisible par tous mais accessible en écriture uniquement aux membres, ou entièrement masqué aux non-membres. Cette séparation compte, car les clients ne devraient pas traiter « private » comme un raccourci global pour toutes les règles d'accès.

## Modèle de confiance

NIP-29 n'est pas un protocole de groupe sans confiance. Le relais hébergeur décide quels événements de modération sont valides, quels rôles existent, si les listes de membres sont visibles, et si les messages anciens ou hors contexte sont acceptés. Un client peut vérifier les signatures et les références de chronologie, mais il dépend toujours de la politique du relais pour l'état réel du groupe.

Cela rend la migration et le fork possibles, mais pas automatiques. Le même identifiant de groupe peut exister sur différents relais avec des historiques ou des règles différentes, de sorte que l'URL du relais fait partie de l'identité du groupe en pratique.

## Notes d'implémentation utiles

- Les clients devraient traiter l'URL du relais comme la clé d'hôte du groupe. Une clarification de janvier 2026 a rendu cela explicite dans la spécification et supprimé l'ambiguïté concernant l'utilisation d'une pubkey à la place
- L'état du groupe est reconstruit à partir de l'historique de modération, tandis que les événements relais de la série 39000 sont des instantanés informatifs de cet état
- Les références `previous` de la chronologie servent à empêcher la rediffusion hors contexte entre forks de relais, pas uniquement à améliorer le threading de l'interface

---

**Sources principales :**
- [Spécification NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Clarification de `private`, `closed` et `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Clarification de l'URL du relais comme clé du relais
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Ajout de `unallowpubkey` et `unbanpubkey`

**Mentionné dans :**
- [Newsletter #2 : Mises à jour NIP](/fr/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3 : Rétrospective de décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6 : Mises à jour NIP](/fr/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #11 : Mises à jour NIP](/fr/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12 : Mises à jour NIP](/fr/newsletters/2026-03-04-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-11 : Document d'information du relais](/fr/topics/nip-11/)
