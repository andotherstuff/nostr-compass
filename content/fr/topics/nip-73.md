---
title: "NIP-73 (Géotags)"
date: 2026-02-04
description: "NIP-73 définit le marquage de localisation pour les événements Nostr en utilisant des coordonnées géographiques et des identifiants."
---

NIP-73 spécifie comment attacher des données de localisation géographique aux événements Nostr. Cela permet la découverte et le filtrage de contenu basés sur la localisation.

## Fonctionnement

Les données de localisation sont ajoutées aux événements via des tags `g` (geohash). L'encodage geohash représente la latitude et la longitude comme une seule chaîne, avec une précision déterminée par la longueur de la chaîne. Les chaînes plus longues indiquent des localisations plus précises.

Les événements peuvent inclure plusieurs tags geohash à différents niveaux de précision, permettant aux clients de requêter à diverses granularités. Un post marqué avec un geohash de 6 caractères couvre environ un pâté de maisons, tandis qu'un geohash de 4 caractères couvre une petite ville.

## Format des tags

```json
{
  "tags": [
    ["g", "u4pruydqqvj", "geohash"],
    ["g", "u4pruyd", "geohash"],
    ["g", "u4pru", "geohash"]
  ]
}
```

## Codes pays

Les mises à jour récentes de NIP-73 ([PR #2205](https://github.com/nostr-protocol/nips/pull/2205)) ont ajouté le support des codes pays ISO 3166, permettant de marquer les événements avec une localisation au niveau du pays sans nécessiter de coordonnées précises :

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## Implémentations

- Les clients sensibles à la localisation utilisent NIP-73 pour les check-ins et la découverte locale
- Les filtres de relais peuvent restreindre ou prioriser le contenu par géographie
- Les applications de cartographie affichent les notes géomarquées

## Sources principales

- [Spécification NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Ajoute les codes pays ISO 3166

## Mentionné dans

- [Newsletter #8 (2026-02-04)](/fr/newsletters/2026-02-04-newsletter/) - Support des codes pays fusionné
