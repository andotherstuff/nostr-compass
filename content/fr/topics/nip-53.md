---
title: "NIP-53 : Activités en direct"
date: 2026-04-15
translationOf: /en/topics/nip-53.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Live Streaming
---

NIP-53 définit le format d'événement standard pour les métadonnées de live streaming sur Nostr. Un stream est annoncé comme un événement adressable kind `30311`, afin que les clients puissent le découvrir, afficher son état courant et rattacher le chat au contexte du stream.

## Fonctionnement

Chaque stream utilise un événement kind `30311` avec un tag `d` comme identifiant stable. L'événement inclut généralement un titre et un résumé, un tag `streaming` avec l'URL de lecture, et un tag `status` (`planned`, `live` ou `ended`). Comme il s'agit d'un événement adressable, les mises à jour remplacent les métadonnées précédentes pour la même valeur `d` au lieu de créer une suite illimitée d'événements.

L'événement peut inclure des tags de sujet (`t`), des références de participants (`p`) et des champs optionnels de nombre de participants. Le chat en direct passe par des événements kind `1311` qui référencent le stream avec un tag `a`, ce qui maintient les messages de chat liés à un enregistrement d'activité en direct précis.

## Implémentations

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) publie les métadonnées de live stream et le chat autour de diffusions Nostr natives.
- [Zap.stream](https://zap.stream/) utilise des événements Nostr pour la découverte et l'interaction autour des streams.
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) utilise des événements de chat en direct kind `1311` dans son contexte de radio internet.
- [Amethyst](https://github.com/vitorpamplona/amethyst) a intégré les objectifs de zap [NIP-75](/fr/topics/nip-75/) à l'écran Live Activities via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) : chaque live stream porte un en-tête d'objectif de financement avec barre de progression, bouton zap en un geste et classement des principaux zappers calculé à partir des reçus de zap kind `9735` liés à l'événement kind `30311` du stream. La [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) ajoute ensuite la proof of agreement et les builders d'événements NIP-53, et la [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) livre un écran dédié au flux Live Streams avec filtrage et découverte.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) ajoute le zap en un geste depuis les cartes de live stream, où les sats apparaissent dans l'overlay de chat du stream via NIP-53.

---

**Sources principales :**
- [Spécification NIP-53](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - En-tête d'objectif de live stream et classement des top zappers
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - Proof of agreement et builders d'événements NIP-53

**Mentionné dans :**
- [Newsletter #18 : lancement de WaveFunc](/en/newsletters/2026-04-15-newsletter/)
- [Newsletter #19 : objectifs de zap live stream dans Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19 : NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-29 : Groupes basés sur les relais](/fr/topics/nip-29/)
- [NIP-75 : Objectifs de zap](/fr/topics/nip-75/)
- [NIP-57 : Zaps](/fr/topics/nip-57/)
- [NIP-C7 : Messages de chat](/fr/topics/nip-c7/)
