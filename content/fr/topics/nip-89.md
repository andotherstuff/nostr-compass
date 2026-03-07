---
title: "NIP-89 : Recommended Application Handlers"
date: 2026-01-07
translationOf: /en/topics/nip-89.md
translationDate: 2026-03-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 définit comment les applications peuvent annoncer leurs capacités et comment les utilisateurs peuvent recommander des apps qui gèrent des types d'événements spécifiques.

## Types d'événements

- **kind 31990** - Application handler (publié par les développeurs d'apps)
- **kind 31989** - Recommandation d'app (publiée par les utilisateurs)

## Fonctionnement

1. **Les applications** publient des événements handler décrivant les kinds d'événements qu'elles supportent et comment ouvrir le contenu
2. **Les utilisateurs** recommandent les apps qu'ils utilisent pour des kinds d'événements spécifiques
3. **Les clients** interrogent les recommandations pour proposer une fonctionnalité "ouvrir dans..." pour les types d'événements inconnus

## Application Handler

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

Les tags `k` spécifient les kinds d'événements supportés. Les modèles d'URL utilisent `<bech32>` comme placeholder pour les entités encodées NIP-19.

Le même événement handler peut annoncer plusieurs kinds supportés s'ils partagent le même schéma de routage. Cela garde la découverte d'apps compacte et évite de publier un événement handler par kind quand la logique de destination est identique.

## Recommandation utilisateur

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

Le tag `d` correspond au kind d'événement recommandé. Plusieurs tags `a` peuvent recommander différentes apps pour différentes plateformes.

## Tag Client

NIP-89 définit aussi un tag `client` optionnel que les apps de publication peuvent attacher aux événements ordinaires. Il enregistre le nom du client plus un pointeur vers l'événement handler, ce qui permet aux autres clients d'afficher d'où vient une note ou de consulter des métadonnées d'application plus riches.

Cela a des implications en termes de vie privée. La spécification indique explicitement que les clients doivent permettre aux utilisateurs de refuser, car publier l'identité du logiciel sur chaque événement peut révéler des habitudes d'utilisation que les gens ne souhaitent pas exposer.

## Cas d'utilisation

- Découvrir les apps capables d'afficher des articles long format (kind 30023)
- Trouver des clients qui supportent des types d'événements spécifiques
- Fonctionnalité "ouvrir dans..." inter-clients
- Détecter les capacités des clients pour le support du chiffrement

## Notes de confiance et sécurité

NIP-89 améliore l'interopérabilité, mais crée aussi une surface de redirection. Si un client interroge des annonces handler arbitraires depuis des relays non fiables, il peut finir par envoyer les utilisateurs vers des applications malveillantes ou trompeuses.

C'est pourquoi le flux de recommandation commence par les personnes que vous suivez. Les recommandations filtrées socialement ne sont pas parfaites, mais elles sont plus sûres que de traiter chaque handler publié comme également digne de confiance.

---

**Sources primaires :**
- [Spécification NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Mentionné dans :**
- [Newsletter #4 : NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #12 : Damus](/en/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**Voir aussi :**
- [NIP-19 : Bech32-Encoded Entities](/fr/topics/nip-19/)
