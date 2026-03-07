---
title: "NIP-19 : Entités encodées en Bech32"
date: 2025-12-17
translationOf: /en/topics/nip-19.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 définit des formats lisibles pour partager les identifiants Nostr. Ces chaînes encodées en bech32 sont utilisées pour l'affichage et le partage mais ne sont jamais utilisées dans le protocole lui-même (qui utilise l'hexadécimal).

## Fonctionnement

Les clés hexadécimales brutes sont sujettes aux erreurs de copie et visuellement indiscernables. L'encodage bech32 ajoute un préfixe lisible et une somme de contrôle, rendant clair quel type de données vous regardez et détectant de nombreuses erreurs de copie.

Les formes de base encodent une seule valeur de 32 octets :

- **npub** - Clé publique (votre identité, peut être partagée)
- **nsec** - Clé privée (à garder secrète, utilisée pour signer)
- **note** - ID d'événement (référence un événement spécifique)

Exemple : La clé publique hex `3bf0c63f...` devient `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

Les formes étendues utilisent l'encodage TLV pour inclure des indices de recherche avec l'identifiant :

- **nprofile** - Profil avec indices de relais
- **nevent** - Événement avec indices de relais, clé publique de l'auteur et kind
- **naddr** - Référence d'événement adressable avec clé publique, kind, tag `d` et indices de relais

## Pourquoi c'est important

Les indices de relais ne font pas autorité, mais ils décident souvent si un client peut récupérer un événement partagé du premier coup. C'est pourquoi `nevent`, `nprofile` et `naddr` sont généralement de meilleurs formats de partage que les simples valeurs `note` ou `npub` quand le contenu se trouve en dehors de l'ensemble de relais actuel du destinataire.

Une autre distinction pratique est la stabilité. `note` pointe vers un ID d'événement immuable, tandis que `naddr` pointe vers un événement adressable qui peut être remplacé au fil du temps. Pour le contenu long format, les calendriers ou les annonces de dépôts, `naddr` est généralement le bon type de lien.

## Notes d'implémentation

- Utilisez bech32 uniquement pour les interfaces humaines : affichage, copier/coller, codes QR, URLs
- N'utilisez jamais les formats bech32 dans les messages du protocole, événements ou réponses NIP-05
- Toute communication du protocole doit utiliser l'encodage hexadécimal
- Lors de la génération de nevent/nprofile/naddr, incluez les indices de relais pour une meilleure découvrabilité
- Traitez `nsec` comme du matériel secret partout. Un client ne devrait jamais l'afficher par défaut, le journaliser ou l'inclure dans les exports de support

---

**Sources principales :**
- [Spécification NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Mentionné dans :**
- [Newsletter #1 : NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [Newsletter #3 : December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3 : Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#damus-ios)
- [Newsletter #4 : Relay Hint Support](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #8 : Damus iOS](/en/newsletters/2026-02-04-newsletter/#damus-ios)
- [Newsletter #11 : notecrumbs](/en/newsletters/2026-02-25-newsletter/)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-10 : Fils de réponse](/fr/topics/nip-10/)
