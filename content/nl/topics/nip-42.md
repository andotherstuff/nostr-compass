---
title: "NIP-42: Authenticatie van clients aan relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 definieert hoe clients authenticeren bij relays. Relays kunnen authenticatie vereisen om toegangscontrole te bieden, misbruik te voorkomen of betaalde relay-diensten te implementeren.

## Hoe Het Werkt

De authenticatieflow begint wanneer een relay een AUTH-bericht naar de client stuurt. Dit bericht bevat een challenge-string die de client moet ondertekenen. De client maakt een kind 22242 authenticatie-event aan dat de challenge bevat en ondertekent dit met zijn privésleutel. De relay verifieert de handtekening en challenge, en verleent vervolgens toegang.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

De challenge voorkomt replay-aanvallen: clients moeten verse challenges ondertekenen voor elke authenticatiepoging. De relay URL in de tags zorgt ervoor dat authenticatietokens niet kunnen worden hergebruikt over verschillende relays.

## Toepassingen

Betaalde relays gebruiken NIP-42 om abonnees te verifiëren voordat toegang wordt verleend. Na authenticatie kunnen relays betalingsstatus of abonnementsverloop controleren. Privé-relays beperken toegang tot goedgekeurde pubkeys, waardoor gesloten communities of persoonlijke relay-infrastructuur wordt gecreëerd.

Rate limiting wordt effectiever met authenticatie. Relays kunnen verzoeksnelheden per geauthenticeerde pubkey volgen in plaats van per IP-adres, wat misbruik voorkomt terwijl legitieme gebruikers achter gedeelde IP's worden ondersteund. Spampreventie verbetert wanneer relays authenticatie vereisen voor het publiceren van events.

Sommige relays gebruiken NIP-42 voor analytics, om te volgen welke gebruikers welke content benaderen zonder gecentraliseerde accounts te vereisen. Gecombineerd met [NIP-11](/nl/topics/nip-11/) metadata, ontdekken clients of relays authenticatie vereisen voordat ze verbindingen proberen.

---

**Primaire bronnen:**
- [NIP-42 Specificatie](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authenticatie van clients aan relays

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
- [NIP-50: Zoekcapaciteit](/nl/topics/nip-50/)
