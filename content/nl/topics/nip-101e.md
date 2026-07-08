---
title: "NIP-101e: Fitness-workouts"
date: 2026-06-17
draft: false
categories:
  - Fitness
  - Discovery
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
---

NIP-101e definieert een workout-eventformaat zodat fitness-trackingapplicaties trainingssessies kunnen publiceren, delen en ontdekken op Nostr. De specificatie gebruikt kind 1301-events die sessiegegevens (afstand, duur, hoogtemeters, hartslag, calorieën, cadans bij fietsen, bron-app) in gestructureerde tags meedragen, zodat een client de workout kan weergeven als een gestructureerde kaart met metrics in de juiste eenheden.

## Hoe het werkt

Een NIP-101e workout is een kind 1301-event met gestructureerde tags voor elke metric die de bron-applicatie heeft vastgelegd. Veelvoorkomende tags zijn:

- `type` voor de discipline (run, bike, swim, lift, enz.)
- `distance` met waarde en eenheid
- `duration` in seconden
- `elevation_gain` met waarde en eenheid
- `start`- en `end`-timestamps
- `heart_rate` (gemiddelde en maximum)
- `calories` voor energieverbruik
- `source` die de publicerende applicatie noemt
- `t` onderwerp-tags voor hashtag-discovery

Het `content`-veld bevat een optionele notitie geschreven door de gebruiker (het equivalent van het onderschrift dat een gebruiker aan een Strava-upload zou toevoegen). Clients die kind 1301 herkennen, tonen de gestructureerde metrics als een workoutkaart; clients die dit niet doen, vallen terug op weergave van het `content`-veld als een gewone note.

## Discovery en feed-semantiek

NIP-101e-events zijn gewone feed-events, dus een workout die door een gebruiker wordt geplaatst, verschijnt in de tijdlijnen van hun volgers zoals elke andere post. Clients met speciale workout-weergaven kunnen zich abonneren op kind 1301 met auteur- of hashtag-filters om trainingslog-oppervlakken, klassementen of community-challengefeeds op te bouwen. De pubkey van de auteur is de canonieke identiteit voor de workout, dus een externe applicatie die de workouts van een andere gebruiker leest, erft dezelfde vertrouwensaannames als elke andere Nostr-feed.

## Implementaties

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) levert weergave van kind 1301-workouts met een hoofdmetric, een stats-raster, een fietsspecifieke snelheidsweergave en bron-badges ([PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184), geherfactoreerd in [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226))

---

**Primaire bronnen:**
- [NIP-101e Specificatie](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - Ondersteuning voor NIP-101e fitness-workouts toegevoegd (Kind 1301)
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - Workout-weergave herontworpen met hoofdmetric en stats-raster

**Genoemd in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/nl/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
