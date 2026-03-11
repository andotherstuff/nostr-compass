---
title: "NIP-46 : Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-03-11
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 définit la signature distante via les relais Nostr. Un client communique avec un signataire séparé, souvent appelé bunker, de sorte que les clés de signature restent en dehors de l'application que l'utilisateur utilise activement.

## Fonctionnement

1. Le client génère une paire de clés locale utilisée uniquement pour la session bunker.
2. La connexion est établie avec un URI `bunker://` ou `nostrconnect://`.
3. Le client et le signataire échangent des événements chiffrés de kind `24133` (requête et réponse) via les relais.
4. Après connexion, le client appelle `get_public_key` pour obtenir la clé publique de l'utilisateur pour lequel il signe.

## Méthodes de connexion

- **bunker://** - Connexion initiée par le signataire
- **nostrconnect://** - Connexion initiée par le client via code QR ou deep link

Les flux `nostrconnect://` incluent un secret partagé obligatoire afin que le client puisse vérifier que la première réponse provient bien du signataire prévu. Cela empêche l'usurpation de connexion.

## Opérations supportées

- `sign_event` - Signer un événement arbitraire
- `get_public_key` - Récupérer la clé publique de l'utilisateur auprès du signataire
- `nip04_encrypt/decrypt` - Opérations de chiffrement NIP-04
- `nip44_encrypt/decrypt` - Opérations de chiffrement NIP-44
- `switch_relays` - Demander au signataire un ensemble de relais mis à jour

De nombreuses implémentations utilisent aussi des chaînes de permission comme `sign_event:1` ou `nip44_encrypt` lors de la configuration, afin que le signataire puisse approuver un périmètre restreint au lieu d'un accès complet.

## Modèle de relais et de confiance

NIP-46 déplace les clés privées hors du client, mais ne supprime pas la confiance envers le signataire. Le signataire peut approuver, refuser ou retarder les requêtes, et il voit chaque opération que le client lui demande d'effectuer. Le choix du relais compte aussi, car le protocole dépend de la livraison des requêtes et réponses via des relais accessibles aux deux parties.

La méthode `switch_relays` existe pour que le signataire puisse déplacer la session vers un autre ensemble de relais au fil du temps. Les clients qui l'ignorent fonctionneront de manière moins fiable lorsque les préférences de relais du signataire changent.

---

**Sources principales :**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mentionné dans :**
- [Newsletter #1 : Notable Code Changes](/fr/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Newsletter #3 : December Recap](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7 : Primal Android Becomes a Full Signing Hub](/fr/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Newsletter #15 : NDK Collaborative Events and NIP-46 Timeout](/fr/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**Voir aussi :**
- [NIP-55 : Android Signer](/fr/topics/nip-55/)
