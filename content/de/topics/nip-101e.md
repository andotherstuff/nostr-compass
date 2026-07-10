---
title: "NIP-101e: Fitness-Workouts"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
categories:
  - Fitness
  - Discovery
---

NIP-101e definiert ein Workout-event-Format, damit Fitness-Tracking-Anwendungen Trainingseinheiten auf Nostr veröffentlichen, teilen und entdecken können. Die Spezifikation verwendet kind 1301-events, die Sitzungsmetriken (Distanz, Dauer, Höhenmeter, Herzfrequenz, Kalorien, Trittfrequenz beim Radfahren, Quell-App) in strukturierten tags tragen, sodass ein Client das Workout als strukturierte Karte mit in den korrekten Einheiten dargestellten Metriken rendern kann.

## Wie es funktioniert

Ein NIP-101e-Workout ist ein kind 1301-event mit strukturierten tags für jede Metrik, die die Quellanwendung erfasst hat. Häufige tags sind:

- `type` für die Workout-Disziplin (Laufen, Radfahren, Schwimmen, Krafttraining usw.)
- `distance` mit Wert und Einheit
- `duration` in Sekunden
- `elevation_gain` mit Wert und Einheit
- `start`- und `end`-Zeitstempel
- `heart_rate` (Durchschnitt und Maximum)
- `calories` für den Energieverbrauch
- `source`, der die veröffentlichende Anwendung benennt
- `t`-Themen-tags für die Hashtag-Entdeckung

Das `content`-Feld enthält eine optionale, vom Nutzer verfasste Notiz (das Äquivalent der Bildunterschrift, die ein Nutzer an einen Strava-Upload anhängen würde). Clients, die kind 1301 erkennen, rendern die strukturierten Metriken als Workout-Karte; Clients, die dies nicht tun, greifen darauf zurück, das `content`-Feld als reguläre Notiz anzuzeigen.

## Discovery- und Feed-Semantik

NIP-101e-events sind normale Feed-events, sodass ein von einem Nutzer veröffentlichtes Workout in den Timelines seiner Follower wie jeder andere Beitrag erscheint. Clients mit dedizierten Workout-Ansichten können kind 1301 mit Autor- oder Hashtag-Filtern abonnieren, um Trainingslog-Oberflächen, Ranglisten oder Feeds für Community-Herausforderungen aufzubauen. Der Autor-pubkey ist die kanonische Identität für das Workout, sodass eine Drittanwendung, die die Workouts eines anderen Nutzers liest, dieselben Vertrauensannahmen erbt wie jeder andere Nostr-Feed.

## Implementierungen

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) liefert kind 1301-Workout-Rendering mit einer Hero-Metrik, einem Statistik-Raster, einer radsportspezifischen Geschwindigkeitsanzeige und Quell-Badges ([PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184), refaktoriert in [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226))

---

**Primärquellen:**
- [NIP-101e-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - NIP-101e-Fitness-Workout-Unterstützung hinzugefügt (Kind 1301)
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - Workout-Anzeige mit Hero-Metrik und Statistik-Raster neu gestaltet

**Erwähnt in:**
- [Newsletter #27: Amethyst v1.12.0 liefert Cashu-Wallets, nutzaps, einen CLINK-Treiber und Tor-Selbstheilung](/de/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
