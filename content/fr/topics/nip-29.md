---
title: "NIP-29 : Groupes basés sur les relais"
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
---

NIP-29 définit les groupes basés sur les relais, où un relais gère l'appartenance au groupe, les permissions et la visibilité des messages.

## Tags d'accès au groupe

- **private** : Seuls les membres peuvent lire les messages du groupe
- **closed** : Les demandes d'adhésion sont ignorées (sur invitation uniquement)
- **hidden** : Le relais cache les métadonnées du groupe aux non-membres, rendant le groupe indécouvrable
- **restricted** : Seuls les membres peuvent écrire des messages dans le groupe

Ces tags peuvent être combinés. Un groupe peut être `restricted` (écriture limitée) mais pas `hidden` (toujours découvrable). Omettre un tag active le comportement opposé : pas de `private` signifie que n'importe qui peut lire, pas de `closed` signifie que les demandes d'adhésion sont honorées.

## Fonctionnement

Le relais est l'autorité pour les opérations de groupe :
- Maintient la liste des membres et les rôles
- Applique les permissions d'écriture
- Contrôle ce que les non-membres peuvent voir

Les clients envoient les messages de groupe au relais, qui valide l'appartenance avant de les accepter.

## Considérations de confidentialité

- Les groupes `hidden` fournissent la protection de découvrabilité la plus forte : ils n'apparaissent pas dans les recherches ou les listes de relais
- Les groupes `private` cachent le contenu des messages aux non-membres
- Les groupes `closed` ignorent simplement les demandes d'adhésion ; combinez avec `private` ou `hidden` pour un contrôle d'accès plus fort
- `restricted` contrôle qui peut écrire, indépendamment de l'accès en lecture

---

**Sources principales :**
- [Spécification NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)

**Mentionné dans :**
- [Newsletter #2 : Mises à jour NIP](/fr/newsletters/2025-12-24-newsletter/#nip-updates)

