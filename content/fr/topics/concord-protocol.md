---
title: "Protocole Concord"
date: 2026-07-15
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
draft: false
categories:
  - Protocol
  - Messaging
---

Concord est un protocole ouvert sous licence MIT pour les communautés et canaux chiffrés de bout en bout sur Nostr, défini par les [spécifications CORD-01 à CORD-07](https://github.com/concord-protocol/concord). [Vector](https://github.com/VectorPrivacy/Vector) l'a adopté comme transport par défaut pour sa fonctionnalité Group Chats à partir de la v0.4.0, le décrivant dans ses propres notes de version comme « our custom messaging protocol », mais la spécification elle-même est publiée séparément de Vector et dispose déjà d'implémentations indépendantes.

## Fonctionnement

Concord décompose ce qu'un serveur de communauté de type Discord fait normalement en éléments qui n'ont besoin de faire confiance à personne : les relays ne stockent jamais que des blobs chiffrés adressés à des étiquettes rotatives, détenir la clé d'un salon est ce qui fait de quelqu'un un membre, et l'autorité sur les rôles, les expulsions et les bannissements est un registre signé enraciné dans l'identité du propriétaire que chaque client vérifie localement au lieu de faire confiance à un serveur pour l'appliquer. Chaque event durable utilise la même enveloppe à trois couches : un wrap kind 1059 signé par la clé de flux dérivée du plan, contenant un seal signé par la vraie clé de l'auteur, contenant un rumor non signé qui porte l'event fonctionnel. Un rumor de message de chat est un simple event kind 9 :

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

Le trafic de contrôle, de chat et de livre d'or obtient chacun son propre plan gift-wrapped [NIP-59](/fr/topics/nip-59/), de sorte qu'un relay détenant les trois ne peut toujours pas distinguer un message de contrôle d'un message de chat ou d'une entrée de livre d'or sans la clé du salon. La spécification est divisée en sept documents CORD : flux privés (01), communautés et adhésion (02), canaux (03), rôles (04), invitations (05), renouvellement de clé et refondation pour couper l'accès aux membres retirés (06), et audio/vidéo via un courtier de jetons aveugles (07). L'adhésion elle-même n'a pas de liste côté serveur : quiconque peut déchiffrer le plan est membre, et retirer quelqu'un pour de vrai signifie faire passer la communauté à une nouvelle époque de clé et la transmettre uniquement à ceux qui restent, au lieu de supprimer une ligne dans une table.

## Différences avec Marmot

Concord et [Marmot](/fr/topics/marmot/) résolvent la messagerie de groupe chiffrée sur Nostr avec des cryptographies différentes pour des formes de groupes différentes, et la propre comparaison du projet Concord est explicite sur cette distinction : Marmot superpose [MLS](/fr/topics/mls/) sur Nostr pour la confidentialité persistante et la sécurité post-compromission, utilisant des key packages par appareil et des commits ordonnés qui font avancer tout le groupe en synchronisation. Cela apporte des garanties solides, à un coût qui augmente avec les changements de membres, bien adapté aux petits groupes à enjeux élevés où les entrées et sorties sont rares. Concord donne plutôt à chaque membre la même clé de salon et renouvelle la clé de tout le salon lors d'un retrait au lieu de faire un ratchet par commit, échangeant certaines des garanties cryptographiques de MLS contre un modèle qui reste économique à mesure qu'une communauté grandit vers des centaines ou des milliers de membres occasionnels à forte rotation, la forme que prennent réellement les communautés de type Discord.

## Pourquoi Vector a changé

Les propres [notes de version de Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) décrivent Concord uniquement comme « our custom messaging protocol » pour les Group Chats, sans énoncer directement le raisonnement. L'adéquation avec la propre justification publiée de Concord est claire malgré tout : les Group Chats dans un client comme Vector sont exactement le cas d'utilisation à grande échelle, ouvert, avec des changements fréquents de membres, où l'état MLS par appareil de Marmot devient le chemin le plus coûteux, et la conception asynchrone de Concord, utilisable à tout moment, est construite pour ce cas. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) a retiré Marmot pour les Group Chats en faveur de Concord, et l'historique existant des groupes Marmot n'a pas été transféré lors du changement. [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) a livré « Concord v2 » quatre jours plus tard avec des améliorations de confidentialité et de stabilité. Dans la même semaine, [Amethyst a fusionné sa propre implémentation Concord indépendante et compatible au niveau du protocole](https://github.com/vitorpamplona/amethyst/pull/3566), et le client de type Discord de Soapbox, [Armada](https://gitlab.com/soapbox-pub/armada), construit déjà sa fonctionnalité Communities sur la même spécification en tant qu'implémentation de référence. Trois clients indépendants convergeant vers une seule spécification ouverte en quelques jours est un chemin rapide vers une véritable interopérabilité inter-clients, à suivre en regard de la proportion du reste des clients de chat de groupe Nostr qui restent sur Marmot.

## Implémentations

- [Vector](https://github.com/VectorPrivacy/Vector) - messager Nostr à binaire unique, axé sur la vie privée ; premier client Concord livré, dans la v0.4.0
- [Armada](https://gitlab.com/soapbox-pub/armada) (Soapbox) - client communautaire de type Discord ; implémentation de référence, backend dans le dépôt séparé `armada-relay`
- [Amethyst](https://github.com/vitorpamplona/amethyst) - client Nostr Android et multiplateforme riche en fonctionnalités ; réimplémentation indépendante compatible au niveau du protocole avec Armada ([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**Sources primaires :**
- [Spécifications du protocole Concord (CORD-01 à CORD-07)](https://github.com/concord-protocol/concord)
- [Notes de version de Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Notes de version de Vector v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [PR #3566 d'Amethyst](https://github.com/vitorpamplona/amethyst/pull/3566)

**Mentionné dans :**
- [Bulletin #31 : Vector v0.4.0 fait passer les Group Chats de Marmot à Concord, et Amethyst livre son propre client Concord quelques jours plus tard](/fr/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Bulletin #31 : Amethyst livre une implémentation Concord indépendante pour les communautés chiffrées de bout en bout](/fr/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**Voir aussi :**
- [Protocole Marmot](/fr/topics/marmot/)
- [MLS (Message Layer Security)](/fr/topics/mls/)
- [NIP-46 : Nostr Connect](/fr/topics/nip-46/)
