---
title: "NIP-05 : Vérification de domaine"
date: 2026-02-04
translationOf: /en/topics/nip-05.md
translationDate: 2026-03-07
draft: false
description: "NIP-05 permet d'associer des identifiants lisibles par l'homme aux pubkeys Nostr via la vérification de domaine."
categories:
  - Identity
  - Discovery
---

NIP-05 associe les clés publiques Nostr à des identifiants internet lisibles par l'homme, comme `user@example.com`. Il fournit aux utilisateurs un indice d'identité adossé au DNS que les clients peuvent vérifier par HTTPS.

## Fonctionnement

Un utilisateur revendique un identifiant en ajoutant un champ `nip05` à ses métadonnées de profil. L'identifiant suit le format `nom@domaine`. Les clients vérifient la revendication en récupérant `https://domaine/.well-known/nostr.json` et en confirmant que le nom correspond à la pubkey de l'utilisateur.

Le fichier JSON au chemin well-known contient un objet `names` associant les noms locaux aux pubkeys hex :

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Lorsque la vérification réussit, les clients peuvent afficher l'identifiant à la place ou à côté du npub. Certains clients montrent un indicateur de vérification, tandis que d'autres affichent l'identifiant en texte brut et laissent les décisions de confiance au lecteur.

## Modèle de confiance

NIP-05 n'est pas un registre global de noms d'utilisateur. Il prouve le contrôle d'un nom de domaine et d'un chemin sur un serveur web, pas une identité légale ou une continuité de compte à long terme. Si un propriétaire de domaine modifie le mapping ultérieurement, les clients vérifieront le nouveau mapping à moins qu'ils ne conservent un état antérieur.

Cela rend NIP-05 utile pour la découvrabilité et la réputation, mais plus faible que ce que les utilisateurs supposent souvent. Un bon client devrait le traiter comme une preuve de contrôle de domaine, pas comme une preuve que la personne ou l'organisation est bien celle qu'elle prétend être.

## Indices de relais

Le fichier `nostr.json` peut optionnellement inclure un objet `relays` associant les pubkeys à des tableaux d'URL de relais. Cela aide les clients à découvrir où trouver les événements d'un utilisateur donné.

## Notes d'interopérabilité

L'exigence de minuscules compte plus qu'il n'y paraît. Des noms ou pubkeys en casse mixte peuvent fonctionner dans une implémentation et échouer dans une autre, de sorte que les clients actuels devraient s'attendre à des noms en minuscules et des clés hex en minuscules dans `nostr.json`.

Un autre détail pratique est le nom spécial `_`, qui permet à un domaine d'associer la forme d'identifiant nue comme `_@example.com` ou simplement `example.com` dans les clients qui le supportent. Tous les clients n'exposent pas cette forme de la même manière, donc les utilisateurs obtiennent les résultats les plus cohérents avec des identifiants explicites `nom@domaine`.

## État de l'implémentation

La plupart des clients majeurs supportent la vérification NIP-05 :
- Damus, Amethyst, Primal affichent les identifiants vérifiés
- De nombreux services de relais proposent des identifiants NIP-05 comme fonctionnalité
- De nombreux fournisseurs NIP-05 gratuits et payants existent

---

**Sources principales :**
- [Spécification NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - exigence de minuscules pour les noms et clés hex

**Mentionné dans :**
- [Newsletter #8 : NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-65 : Métadonnées de liste de relais](/fr/topics/nip-65/)
