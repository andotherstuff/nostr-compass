---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 definiert Event-Löschung, einen Mechanismus, mit dem Nutzer Relays auffordern können, ihre zuvor veröffentlichten Events zu entfernen.

## Funktionsweise

Nutzer veröffentlichen kind-5-Events mit `e`-Tags, die die Event-IDs referenzieren, die gelöscht werden sollen. Relays, die NIP-09 unterstützen, sollten die referenzierten Events nicht mehr ausliefern und können sie aus dem Speicher löschen.

Löschung ist eine Anfrage, keine Garantie. Relays können Löschanfragen ignorieren, und Events können sich bereits auf Relays verbreitet haben, die keine Löschung unterstützen. Nutzer sollten sich nicht auf NIP-09 für das Entfernen datenschutzrelevanter Inhalte verlassen.

## Hauptmerkmale

- kind-5-Löschanfrage-Events
- Referenzierung gelöschter Events per ID via e-Tags
- Optionales Begründungsfeld für den Löschkontext
- Relay-Compliance ist freiwillig

---

**Primärquellen:**
- [NIP-09 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Erwähnt in:**
- [Newsletter #11: NIP-60 Deep Dive](/de/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)

**Siehe auch:**
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
