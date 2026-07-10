---
title: "NIP-82: Software-Anwendungen"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
categories:
  - Discovery
  - Apps
---

NIP-82 definiert ein Software-Anwendungs-event, damit Nostr-Clients Anwendungen (Android-APKs, iOS-Apps, Web-Apps, Desktop-Binärdateien) als erstklassige Objekte in Feeds und Entdeckungsoberflächen darstellen können. Die Spezifikation ersetzt den älteren Ansatz, Apps über generische kind 1-Notizen oder [NIP-89](/de/topics/nip-89/)-Handler-Empfehlungen zu beschreiben, durch ein dediziertes, strukturiertes event, das Anwendungsmetadaten, Screenshots, Repository-Links und die Autorenidentität enthält.

## Wie es funktioniert

Eine NIP-82-Software-Anwendung ist ein einzelnes ersetzbares event, das durch den Autoren-pubkey und einen `d`-tag adressiert wird. Das event enthält:

- `name`-, `description`-, `icon`-, `image`-tags für die Anzeige
- `repository`- und `web`-tags für Quellcode- und Homepage-URLs
- `platforms`-tag, das unterstützte Ziele auflistet (android, ios, web, linux, macos, windows)
- `download`-tags für jede plattformspezifische Binärdatei oder Web-URL
- `screenshots`-tags mit Bild-URLs für die Anwendungs-Screenshots
- `t`-Themen-tags zur Kategorisierung
- `version`-tag für die aktuelle veröffentlichte Version

Ein Client, der einen NIP-82-Feed durchsucht, kann die Anwendungskarte anzeigen, auf das kanonische Repository verlinken und Screenshots zeigen, ohne auf das Scrapen eines Nostr-Langform-Beitrags oder eines Drittanbieter-App-Stores zurückgreifen zu müssen. Der Autoren-pubkey ist die Wahrheitsquelle für die Anwendung, sodass ein Client verifizieren kann, dass der Herausgeber mit der erwarteten Entwickleridentität übereinstimmt, bevor er einen Download-Link bewirbt.

## Feed-Semantik

NIP-82-events sind adressierbar, sodass jede Anwendung ein kanonisches ersetzbares event pro Autor hat. Ein Entwickler, der eine neue Version veröffentlicht, ersetzt das vorherige event an Ort und Stelle, und Abonnenten sehen das Update, ohne den event-Verlauf verwalten zu müssen. Clients, die ein Änderungsprotokoll wünschen, können das adressierbare event abonnieren und Versionswechsel als Aktivität auf der Anwendungsoberfläche darstellen.

Die Spezifikation ergänzt [NIP-89](/de/topics/nip-89/) (Application Handlers): Ein NIP-82-event beschreibt die Anwendung als Artefakt, während ein NIP-89-event beschreibt, dass die Anwendung bestimmte event-kinds verarbeiten kann. Clients können eines ohne das andere verwenden, aber das Paar bietet eine Entdeckungsoberfläche (NIP-82) und eine Delegationsoberfläche (NIP-89), die zusammenarbeiten.

## Implementierungen

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) liefert einen dedizierten NIP-82-Software-Anwendungs-Feed mit Detailbildschirm, Autoreninformationen und Screenshots ([PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036), [PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078), [PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200))

---

**Primärquellen:**
- [NIP-82-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - NIP-82-Software-Anwendungs-Unterstützung mit dediziertem Feed hinzugefügt
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - Dedizierten NIP-82-Software-App-Detailbildschirm hinzugefügt
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - NIP-82-Software-App-UI mit Autoreninformationen und Screenshots verbessert

**Erwähnt in:**
- [Newsletter #27: Amethyst v1.12.0 liefert Cashu-Wallets, nutzaps, einen CLINK-Treiber und Tor-Selbstheilung](/de/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Siehe auch:**
- [NIP-89: Application Handlers](/de/topics/nip-89/)
