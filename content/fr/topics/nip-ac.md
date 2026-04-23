---
title: "NIP-AC : Appels vocaux et vidéo P2P"
date: 2026-04-08
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Calling
---

NIP-AC propose un protocole pour les appels vocaux et vidéo pair à pair sur Nostr. La spécification utilise des événements Nostr pour la signalisation d'appel (offers, answers, ICE candidates) et WebRTC pour le transport média effectif, ce qui garde l'établissement d'appel décentralisé tout en utilisant les API standards du navigateur pour l'audio et la vidéo.

## Fonctionnement

L'appelant publie un événement d'offre d'appel contenant une offre WebRTC Session Description Protocol (SDP), taguée avec la pubkey du destinataire. Le destinataire répond avec un événement de réponse SDP. Les deux parties échangent des événements ICE candidate pour négocier le chemin réseau. Une fois la connexion WebRTC établie, le média circule directement entre pairs sans implication des relays.

Les événements de signalisation sont chiffrés afin que les relays ne puissent pas observer qui appelle qui. La machine d'état d'appel gère les transitions offer, answer, reject, busy et hangup.

## Implémentations

- [Amethyst](https://github.com/vitorpamplona/amethyst) construit le support NIP-AC avec une suite de tests de machine d'état d'appel et la gestion des offres d'appel obsolètes.

---

**Sources principales :**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - Appels vocaux et vidéo P2P sur WebRTC

**Mentionné dans :**
- [Nostr Compass #17 (2026-04-08)](/fr/newsletters/2026-04-08-newsletter/)

**Voir aussi :**
- [NIP-44 (payloads chiffrés)](/fr/topics/nip-44/)
