---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - Vertrouwen
  - Sociaal Netwerk
---

Web of Trust (WoT) is een gedecentraliseerd vertrouwensmodel waarbij reputatie en betrouwbaarheid worden afgeleid uit sociale grafiekrelaties in plaats van centrale autoriteiten.

## Hoe Het Werkt

In Nostr maakt Web of Trust gebruik van de follow-grafiek (NIP-02 contactlijsten) en rapportage-events om vertrouwensscores te berekenen:

1. **Grafiekconstructie**: Een gerichte grafiek wordt opgebouwd uit pubkeys, events en hun relaties (follows, mutes, rapportages)
2. **Gewichtstoewijzing**: Initiële gewichten worden toegewezen aan bekende betrouwbare pubkeys (bijv. die met geverifieerde NIP-05-identificatoren)
3. **Iteratieve Propagatie**: Vertrouwensscores stromen door het netwerk met algoritmen vergelijkbaar met PageRank
4. **Sybil-resistentie**: Als een aanvaller veel nepaccounts aanmaakt, wordt het vertrouwen dat aan hen wordt doorgegeven gedeeld door het aantal nepaccounts

## Belangrijke Eigenschappen

- **Gedecentraliseerd**: Geen centrale autoriteit bepaalt reputatie
- **Gepersonaliseerd**: Vertrouwen kan worden berekend vanuit het perspectief van elke gebruiker op basis van wie ze volgen
- **Sybil-resistent**: Botfarms kunnen het systeem niet gemakkelijk manipuleren door vertrouwensverdunning
- **Combineerbaar**: Kan worden toegepast op spamfiltering, contentmoderatie, relay-toegang en betalingsdirectory's

## Toepassingen in Nostr

- **Spamfiltering**: Relays kunnen WoT gebruiken om content met lage vertrouwenswaarde te filteren
- **Content Ontdekking**: Content tonen van accounts die door je netwerk worden vertrouwd
- **Betalingsdirectory's**: Lightning-adreszoeken met bescherming tegen nabootsing
- **Relay-beleid**: WoT-relays accepteren alleen notes van vertrouwde pubkeys
- **Gedecentraliseerde Moderatie**: Gemeenschappen kunnen cureren op basis van vertrouwensscores

## Implementaties

Verschillende projecten implementeren Web of Trust voor Nostr:
- **Nostr.Band Trust Rank**: PageRank-achtige scoring voor het netwerk
- **WoT Relays**: Relays die filteren op sociale afstand
- **DCoSL**: Protocol voor gedecentraliseerde reputatiesystemen
- **Noswot**: Vertrouwensscoring gebaseerd op follows en rapportages

---

**Primaire bronnen:**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL Protocol](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Genoemd in:**
- [Newsletter #3: December Terugblik](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-02: Volglijst](/nl/topics/nip-02/)
