---
title: "NIP-09: Anforderung zum Löschen von Events"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-09 definiert eine Möglichkeit für Autoren, die Löschung von Events anzufordern, die sie zuvor veröffentlicht haben. Es ist ein relayseitiges Löschsignal, keine netzwerkweite Funktion zum Ausradieren.

## Wie es funktioniert

Nutzer veröffentlichen Kind-5-Events mit Referenzen auf Events, die gelöscht werden sollen. Relays, die NIP-09 unterstützen, sollten passende Events desselben Autors nicht mehr ausliefern und können sie aus dem Speicher entfernen.

Löschen ist eine Anfrage, keine Garantie. Relays können Löschanfragen ignorieren, und Events können sich bereits auf Relays verbreitet haben, die keine Löschung unterstützen. Nutzer sollten sich bei datenschutzsensiblen Inhalten nicht auf NIP-09 verlassen.

## Warum es wichtig ist

NIP-09 gibt Clients und Relays eine gemeinsame Sprache für "dieses Event sollte nicht mehr erscheinen". Das ist für versehentliche Posts, Wallet-State-Rollover und Moderationsabläufe nützlich. Autoren können damit aber nur die Löschung ihrer eigenen Events anfordern. Es ist kein allgemeiner Takedown-Mechanismus für fremde Inhalte.

## Abwägungen

Der schwache Punkt ist die Verbreitung. Sobald ein Event über mehrere Relays gespiegelt wurde, ist Löschen nur noch best effort. Manche Relays löschen es, manche tombstonen es, und manche liefern es auf unbestimmte Zeit weiter aus. Clients, die Löschung als final darstellen, übertreiben, was das Protokoll garantiert.

Ein weiteres praktisches Problem sind Referenzen. Nutzer und Apps können das gelöschte Event lokal weiter gespeichert haben oder es an anderer Stelle zitieren, auch nachdem ein kompatibles Relay es nicht mehr ausliefert.

---

**Primärquellen:**
- [NIP-09 Specification](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Erwähnt in:**
- [Newsletter #11: NIP-60 Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
