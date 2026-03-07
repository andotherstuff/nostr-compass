---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2026-03-07
draft: false
categories:
  - Vertrouwen
  - Sociaal Netwerk
---

Web of Trust (WoT) is een gedecentraliseerd vertrouwensmodel waarbij reputatie en betrouwbaarheid worden afgeleid uit relaties in de sociale grafiek, in plaats van uit centrale autoriteiten.

## Hoe het werkt

In Nostr begint Web of Trust meestal met de follow-grafiek in [NIP-02: Volglijst](/nl/topics/nip-02/) en voegt het soms mutes, rapporten of geverifieerde identiteitssignalen toe. Een client of dienst kiest een of meer seed pubkeys die zij al vertrouwt, en laat vertrouwen daarna naar buiten door de grafiek stromen.

1. **Grafiekopbouw**: Bouw een gerichte grafiek van follows en optionele negatieve signalen
2. **Seed-selectie**: Begin met pubkeys die de waarnemer al vertrouwt
3. **Scorepropagatie**: Duw rank door de grafiek met een algoritme zoals PageRank of een variant daarop
4. **Afsnijdingen en normalisatie**: Beperk de grafiekdiepte, demp accounts met weinig signaal en normaliseer de eindscores voor weergave of filtering

Het exacte algoritme is niet gestandaardiseerd. Twee WoT-systemen kunnen allebei geldig zijn en toch verschillende rangschikkingen opleveren, omdat ze andere seeds, grafiekdiepte, vervalregels of behandelingen van mutes en rapporten gebruiken.

## Waarom het belangrijk is

WoT geeft Nostr een manier om te rangschikken en filteren zonder een centrale moderatiedienst. Een gepersonaliseerde vertrouwensgrafiek is moeilijker te manipuleren dan een ruwe follower count, omdat nepaccounts nog steeds vertrouwen uit het bestaande netwerk van de waarnemer nodig hebben.

De keerzijde is de cold start. Als je niemand volgt, heeft een gepersonaliseerde WoT bijna geen basis om iets te rangschikken. Veel producten lossen dat op met starter follows, standaardinstellingen van vertrouwde aanbieders of vooraf berekende scores van externe diensten.

## Toepassingen in Nostr

- **Spamfiltering**: Relays kunnen WoT gebruiken om content met weinig vertrouwen te filteren
- **Contentontdekking**: Content tonen van accounts die door je netwerk worden vertrouwd
- **Betalingsdirectory's**: Lightning-adresopzoeking met bescherming tegen impersonatie
- **Relaybeleid**: WoT-relays accepteren alleen notes van vertrouwde pubkeys
- **Gedecentraliseerde moderatie**: Gemeenschappen kunnen cureren op basis van vertrouwensscores

## Implementatienotities

Omdat WoT-berekeningen grote delen van het netwerk moeten crawlen, berekenen veel clients ze niet lokaal. [NIP-85: Trusted Assertions](/nl/topics/nip-85/) bestaat deels om die reden: het geeft clients een manier om ondertekende WoT-berekeningen van derden te gebruiken wanneer lokale berekening te duur is.

Bestaande implementaties beantwoorden ook verschillende vragen. Een globale trust rank is nuttig voor ontdekking en spamweerstand over het hele netwerk. Een gepersonaliseerde lokale score is beter voor "toon me accounts die mijn grafiek zou vertrouwen". Een WoT-getal lezen zonder te weten welk model het heeft geproduceerd, is een veelvoorkomende bron van verwarring.

---

**Primaire bronnen:**
- [NIP-02: Volglijst](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [NIP-85: Trusted Assertions](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL Protocol](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Genoemd in:**
- [Newsletter #3: Decemberoverzicht](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-02: Volglijst](/nl/topics/nip-02/)
