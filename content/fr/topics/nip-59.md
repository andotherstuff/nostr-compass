---
title: "NIP-59 : Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 définit l'emballage cadeau (gift wrapping), une technique pour cacher l'expéditeur d'un événement en l'enveloppant dans des couches de chiffrement avec une identité jetable.

## Structure

Un événement emballé cadeau a trois couches :

1. **Rumeur** - Le contenu de l'événement original non signé
2. **Sceau** (kind 13) - La rumeur chiffrée pour le destinataire, signée par le vrai expéditeur
3. **Emballage cadeau** (kind 1059) - Le sceau chiffré pour le destinataire, signé par une clé jetable aléatoire

La couche externe utilise une paire de clés aléatoire générée juste pour ce message, donc les observateurs ne peuvent pas le lier à l'expéditeur.

## Pourquoi trois couches ?

- La **rumeur** contient le contenu réel
- Le **sceau** prouve le vrai expéditeur (visible uniquement par le destinataire)
- L'**emballage cadeau** cache l'expéditeur aux relais et observateurs

## Support de suppression

Les événements emballés cadeau peuvent maintenant être supprimés via les demandes de suppression NIP-09/NIP-62. Ceci a été ajouté pour permettre aux utilisateurs de retirer les messages emballés des relais.

## Cas d'utilisation

- Messages directs privés (NIP-17)
- Conseils anonymes ou lanceurs d'alerte
- Tout scénario où la confidentialité de l'expéditeur est importante

---

**Sources principales :**
- [Spécification NIP-59](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1 : Mises à jour NIP](/fr/newsletters/2025-12-17-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)

