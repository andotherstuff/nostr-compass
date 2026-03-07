---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 definiert Trusted Assertions, ein System, mit dem aufwendige Berechnungen an vertrauenswürdige Service Provider delegiert werden, die signierte Ergebnisse als Nostr-Events veröffentlichen.

## Funktionsweise

Web-of-Trust-Scores, Engagement-Metriken und andere berechnete Werte erfordern das Crawlen vieler Relays und die Verarbeitung großer Event-Mengen. Diese Arbeit ist auf Mobilgeräten unpraktisch. NIP-85 erlaubt spezialisierten Providern, diese Berechnungen zu übernehmen und Ergebnisse zu veröffentlichen, die Clients abfragen können.

Trusted Assertions sind addressable Events. Das `d`-Tag identifiziert das bewertete Objekt, und der Event-Kind bestimmt, um welche Art von Objekt es sich handelt: Pubkeys (30382), normale Events (30383), addressable Events (30384) und NIP-73-Identifier (30385).

Nutzer legen über kind 10040 fest, welchen Providern sie vertrauen. Diese Provider-Listen können öffentlich in Tags stehen oder verschlüsselt im Event-Inhalt mit [NIP-44](/de/topics/nip-44/), was wichtig ist, wenn ein Nutzer seine Trust-Inputs nicht offen veröffentlichen will.

## Warum das wichtig ist

Der nützliche Kern von NIP-85 ist, dass es die Ausgaben standardisiert, nicht die Algorithmen. Zwei Provider können beide ein `rank`-Tag für denselben Pubkey veröffentlichen und dabei völlig unterschiedliche Web-of-Trust-Formeln, Mute-Behandlung, Relay-Abdeckung oder Anti-Spam-Heuristiken nutzen. Clients bleiben interoperabel, weil das Ergebnisformat übereinstimmt, auch wenn die Berechnung es nicht tut.

Das passt besser zu Nostr, als so zu tun, als gäbe es einen einzigen kanonischen Ranking-Dienst. Nutzer entscheiden selbst, wessen Assertions sie vertrauen.

## Trust-Modell

Service Provider müssen ihre eigenen Assertion-Events signieren, und die Spezifikation empfiehlt unterschiedliche Service-Keys für verschiedene Algorithmen oder nutzerspezifische Sichtweisen. So wird verhindert, dass ein Provider nicht zusammengehörige Ranking-Systeme in einer undurchsichtigen Identität bündelt.

Vertrauen bleibt trotzdem lokal. Eine Signatur beweist, welcher Provider einen Score veröffentlicht hat, nicht dass der Score richtig ist. Clients brauchen Regeln dafür, welche Provider-Keys sie verwenden, von welchen Relays sie laden und wie sie mit widersprüchlichen Assertions umgehen.

## Interop-Hinweise

NIP-85 geht über Menschen und Posts hinaus. Kind 30385 erlaubt es Providern, NIP-73-Identifier wie Bücher, Websites, Hashtags und Orte zu bewerten. Damit entsteht ein Weg für interoperable Reputations- und Engagement-Daten zu Dingen außerhalb von Nostr.

---

**Primärquellen:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - Service provider discoverability guidance

**Erwähnt in:**
- [Newsletter #10: NIP-85 Deep Dive](/de/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 Service Provider Discoverability](/de/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: Protocol Recap](/de/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
- [NIP-73: External Content IDs](/de/topics/nip-73/)
- [Web of Trust](/de/topics/web-of-trust/)
