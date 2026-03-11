---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
translationOf: /en/topics/nip-59.md
translationDate: 2026-03-11
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 definiert Gift Wrap, also eine Moglichkeit, ein Event so zu kapseln, dass Relays und auBenstehende Beobachter aus dem auBeren Event nicht den echten Absender lernen.

## Struktur

Ein Gift-Wrapped-Event hat drei Schichten:

1. **Rumor** - Das Ziel-Event ohne Signatur.
2. **Seal** (kind `13`) - Der fur den Empfanger verschlusselte Rumor, signiert vom echten Absender.
3. **Gift Wrap** (kind `1059`) - Das erneut verschlusselte Seal, signiert von einem zufalligen Einmal-Schlussel.

Das Seal muss leere Tags haben. Das auBere Gift Wrap tragt normalerweise das `p`-Tag des Empfangers, damit Relays es zustellen konnen.

## Was es verbirgt

Gift Wrap verbirgt den Absender vor Relays und Netzwerkbeobachtern, weil das auBere Event mit einem Wegwerf-Schlussel signiert ist. Der Empfanger kann das innere Seal aber trotzdem entschlusseln und sehen, welcher langlebige Schlussel es signiert hat. Der Privatspharengewinn ist also Schutz von Metadaten auf der Transportebene, nicht Anonymitat gegenuber dem Empfanger.

Die Spezifikation empfiehlt auBerdem, Timestamps der Wrapper zu randomisieren und nach Moglichkeit Relays zu verwenden, die Authentifizierung verlangen und Wrapped Events nur an den vorgesehenen Empfanger ausliefern. Ohne dieses Relay-Verhalten konnen Metadaten des Empfangers weiter auslaufen.

## Betriebshinweise

Gift Wrap ist fur sich genommen kein Messaging-Protokoll. Andere Protokolle, etwa private Nachrichtensysteme, verwenden es als Baustein.

Relays konnen sich entscheiden, Wrapped Events nicht lange zu speichern, weil sie offentlich nicht nutzlich sind. Die Spezifikation erlaubt auBerdem Proof-of-Work auf dem auBeren Wrapper, wenn Implementierungen zusatzliche Spam-Resistenz wollen.

## Anwendungsfalle

- Private Direktnachrichten (NIP-17)
- Friends-only notes (NIP-FR proposal)
- Push notification payloads (NIP-9a proposal)
- Jedes Szenario, das Privatsphare des Absenders gegenuber dem Netzwerk erfordert

---

**Primarquellen:**
- [NIP-59 Specification](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Erwahnt in:**
- [Newsletter #8: NIP Deep Dive](/en/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #15: Open PRs](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Siehe auch:**
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
