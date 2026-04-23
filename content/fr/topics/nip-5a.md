---
title: "NIP-5A : Sites web statiques"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5A définit comment héberger des sites web statiques sous des clés Nostr. Les auteurs de sites publient des événements de manifeste signés qui associent des chemins d'URL à des hachages SHA256 de contenu, et les serveurs hôtes résolvent ces manifestes pour servir les fichiers du site depuis le stockage Blossom.

## Comment ça fonctionne

La spécification utilise deux kinds d'événements. Le kind `15128` est un manifeste de site racine, un par pubkey, qui sert de site web par défaut pour cette clé. Le kind `35128` est un manifeste de site nommé, identifié par un tag `d`, qui fonctionne comme un sous-domaine. Chaque manifeste contient des tags `path` associant des chemins d'URL absolus aux hachages SHA256 des fichiers à servir.

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

Un serveur hôte reçoit une requête HTTP, extrait la pubkey de l'auteur du sous-domaine, récupère le manifeste du site depuis la liste de relays de l'auteur, résout le chemin demandé en un hachage de contenu, et télécharge le blob correspondant depuis le ou les serveurs Blossom listés dans les tags `server`.

## Résolution d'URL

Les sites racines utilisent le npub comme sous-domaine. Les sites nommés utilisent un encodage base36 de 50 caractères de la pubkey brute suivi de la valeur du tag `d`, le tout dans un seul label DNS. Parce que les labels DNS sont limités à 63 caractères et que la pubkey en base36 en utilise toujours 50, les identifiants de sites nommés sont limités à 13 caractères.

## Implémentations

- [nsite](https://github.com/lez/nsite) - Serveur hôte qui résout les manifestes NIP-5A et sert les fichiers
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - Interface pour construire et publier les manifestes de sites

---

**Sources principales :**
- [Spécification NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - Proposition originale et fusion
- [nsite](https://github.com/lez/nsite) - Implémentation de référence du serveur hôte
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - Interface de publication et de gestion

**Mentionné dans :**
- [Newsletter #16 : Fusion de NIP-5A](/fr/newsletters/2026-04-01-newsletter/)
- [Newsletter #16 : NIP Deep Dive](/fr/newsletters/2026-04-01-newsletter/)
- [Newsletter #19 : proposition NIP-5D applets](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [Blossom](/fr/topics/blossom/)
- [NIP-65 : Relay List Metadata](/fr/topics/nip-65/)
- [NIP-96 : HTTP File Storage](/fr/topics/nip-96/)
