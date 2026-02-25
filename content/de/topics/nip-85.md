---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 definiert Trusted Assertions, ein System zur Delegation aufwändiger Berechnungen an vertrauenswürdige Service Provider, die signierte Ergebnisse als Nostr-Events veröffentlichen.

## Funktionsweise

Web-of-Trust-Scores, Engagement-Metriken und andere berechnete Werte erfordern das Crawlen vieler Relays und die Verarbeitung großer Event-Mengen. Diese Arbeit ist auf Mobilgeräten nicht praktikabel. NIP-85 ermöglicht es spezialisierten Providern, diese Berechnungen durchzuführen und Ergebnisse zu veröffentlichen, die Clients abfragen können.

Service Provider kündigen ihre Fähigkeiten über kind-30085-Events an. Clients entdecken Provider, indem sie nach diesen Ankündigungen von pubkeys suchen, denen der Nutzer bereits folgt oder vertraut. Ergebnisse kommen als kind-30382-Events, signiert vom Provider.

## Hauptmerkmale

- Delegierte Berechnung für ressourcenintensive Metriken
- Provider-Discovery durch den sozialen Graphen
- Signierte Assertions für verifizierbare Ergebnisse
- Vertrauensentscheidungen auf Client-Seite

---

**Primärquellen:**
- [NIP-85 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Erwähnt in:**
- [Newsletter #10: NIP-85 Deep Dive](/de/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 Service-Provider-Auffindbarkeit](/de/newsletters/2026-02-25-newsletter/#nip-updates)

**Siehe auch:**
- [Web of Trust](/de/topics/web-of-trust/)
