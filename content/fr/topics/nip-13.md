---
title: "NIP-13 : Preuve de travail"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13 définit un système de preuve de travail pour les événements Nostr, exigeant un effort computationnel pour créer des événements comme mécanisme de prévention du spam.

## Fonctionnement

La preuve de travail est démontrée en trouvant un ID d'événement (hash SHA256) avec un nombre spécifié de bits zéro en tête :

1. **Difficulté** : Mesurée en bits zéro en tête (par ex., 20 bits = 2^20 tentatives en moyenne)
2. **Tag Nonce** : Les événements incluent un tag `nonce` avec la valeur du nonce et la difficulté cible
3. **Vérification** : Les relais et les clients peuvent rapidement vérifier que le travail a été effectué

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Niveaux de difficulté

| Bits | Tentatives moyennes | Utilisation typique |
|------|---------------------|---------------------|
| 8 | 256 | Dissuasion minimale du spam |
| 16 | 65 536 | Filtrage léger |
| 20 | 1 048 576 | Protection modérée |
| 24 | 16 777 216 | Forte résistance au spam |

## Cas d'utilisation

- **Admission au relais** : Les relais peuvent exiger un PoW minimum pour l'acceptation des événements
- **Limitation de débit** : Difficulté plus élevée pour des actions comme l'enregistrement de compte
- **Filtrage du spam** : Les clients peuvent prioriser les événements à PoW élevé dans les fils
- **Amorçage de réputation** : Les nouveaux comptes peuvent démontrer leur engagement via le PoW

## Limitations

- Favorise les utilisateurs avec du matériel puissant
- Préoccupations de consommation énergétique
- N'empêche pas tout le spam, augmente seulement le coût

## Voir aussi

- [NIP-01](/fr/topics/nip-01/) - Protocole de base
