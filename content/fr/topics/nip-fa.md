---
title: "Buzz NIP-FA : adaptateur d'identité fédérée"
date: 2026-10-21
draft: false
categories: ["NIPs"]
translationOf: /en/topics/nip-fa.md
translationDate: 2026-11-05
---

Buzz NIP-FA est une spécification provisoire et facultative du projet Buzz. Elle ne fait pas partie des NIP acceptés du dépôt officiel nostr-protocol/nips.

Elle définit un contrat HTTP indépendant de tout fournisseur entre un client Nostr et un adaptateur d'identité d'entreprise. Après une connexion dans le navigateur, l'adaptateur détient une session pour l'utilisateur. Il émet des assertions Buzz NIP-FI propres au projet, qui lient l'utilisateur à une clé Nostr dont le client prouve le contrôle avec [NIP-98](/fr/topics/nip-98/). [L'opérateur choisit la durée de vie de chaque assertion](https://github.com/block/buzz/pull/8934), qui doit respecter le maximum_assertion_age de l'émetteur accepté par le relais, et exp ne peut pas dépasser l'expiration de la session de l'adaptateur. La durée de vie choisie limite la période pendant laquelle une clé révoquée pourrait encore se reconnecter après un redémarrage du relais, et les clients ne doivent pas rejeter une assertion uniquement en raison de sa durée de vie. NIP-FI et les NIP officiels restent inchangés. La connexion utilise un défi de transfert S256 et un rappel en boucle locale sur `127.0.0.1` ou `[::1]` qui reçoit un code à usage unique. Les systèmes en amont tels qu'OIDC ou SAML restent derrière l'adaptateur. L'identification des relais qui exigent une identité d'entreprise relève d'autres spécifications.

Source principale : la [spécification NIP-FA](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md) dans le dépôt Buzz.

## Identifiants d'agent {#agent-credentials}

Buzz a fusionné un [brouillon NIP-FA pour les identifiants d'agent autorisés par leur propriétaire](https://github.com/block/buzz/pull/9015), qui définit des routes d'octroi, d'assertion et de révocation pour les agents qu'un propriétaire a autorisés via NIP-OA. Un octroi est obtenu par un échange de jetons RFC 8693 qui associe la session du propriétaire à une preuve [NIP-98](/fr/topics/nip-98/) fournie par l'agent. Pour obtenir une assertion, l'agent présente l'octroi comme jeton Bearer accompagné de sa propre preuve, et les clients vérifient que le `iss` de l'assertion correspond à l'émetteur de l'octroi. Les preuves d'agent sont à usage unique et réservées aux routes d'octroi et d'assertion. La révocation s'effectue avec la session du propriétaire, sans preuve d'agent ; elle révoque la clé de l'agent et ses octrois, et déconnecte l'agent. La politique de l'adaptateur détermine la durée de vie de l'octroi. Les conditions d'autorisation non prises en charge sont refusées, et une clé révoquée ne peut pas se réinscrire. NIP-FA est une spécification Buzz, et non un NIP accepté. La fusion ne concerne que le code source, sans aucune affirmation d'activation en production, de version publiée ou d'interopérabilité.

## Sources principales {#primary-sources}

- [Buzz NIP-FA : adaptateur d'identité fédérée](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [Routes d'identifiants d'agent autorisés par le propriétaire](https://github.com/block/buzz/pull/9015)

## Mentionné dans {#mentioned-in}

- [Newsletter #47 : identifiants d'agent Buzz](/fr/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
