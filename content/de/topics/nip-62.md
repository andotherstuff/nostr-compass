---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
translationOf: /en/topics/nip-62.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 definiert Vanish Requests, also kind-`62`-Events, die bestimmte Relays auffordern, alle Events des anfragenden pubkey zu löschen. Die Anfrage ist standardmäßig relay-gerichtet, kann aber auch als globale Anfrage mit dem speziellen Tag-Wert `ALL_RELAYS` gesendet werden.

## Funktionsweise

Ein Vanish Request ist ein kind-`62`-Event, das vom pubkey signiert wird, dessen Verlauf entfernt werden soll. Die Tag-Liste muss mindestens einen `relay`-Wert enthalten, der das Relay benennt, das auf die Anfrage reagieren soll.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

Das Feld `content` kann einen Grund oder einen rechtlichen Hinweis an den Relay-Betreiber enthalten. Clients sollten das Event direkt an die Ziel-Relays senden, statt es breit zu posten, außer der Nutzer beabsichtigt ausdrücklich eine netzwerkweite Vanish-Anfrage.

## Relay-Verhalten

Relays, die einen Vanish Request sehen und ihre eigene Service-URL in einem `relay`-Tag finden, müssen alle Events dieses pubkey bis einschließlich `created_at` der Anfrage vollständig löschen. Die Spezifikation sagt außerdem, dass Relays [NIP-59](/de/topics/nip-59/) Gift-Wrap-Events löschen sollen, die den verschwundenen pubkey mit `p` taggen, damit eingehende DMs zusammen mit den eigenen Events des Nutzers entfernt werden.

Das Relay muss außerdem sicherstellen, dass diese gelöschten Events nicht erneut in das Relay rebroadcastet werden können. Für Buchführungszwecke darf es den signierten Vanish Request selbst behalten.

## Globale Anfragen

Um Löschung auf jedem Relay anzufordern, das das Event sieht, wird der Tag-Wert in Großbuchstaben zu `ALL_RELAYS`:

```json
{
  "kind": 62,
  "pubkey": "<32-byte-hex-pubkey>",
  "tags": [
    ["relay", "ALL_RELAYS"]
  ],
  "content": "Global vanish request"
}
```

Clients sollten diese Form an möglichst viele Relays broadcasten.

## Warum das wichtig ist

NIP-62 gibt Clients und Relay-Betreibern ein gemeinsames Löschsignal, das über ad-hoc-Moderations-APIs oder relay-spezifische Dashboards hinausgeht. Ein Nutzer kann eine einzige signierte Anfrage veröffentlichen und jedes Relay sie im selben Event-Format verarbeiten lassen.

Es geht außerdem über [NIP-09](/de/topics/nip-09/) hinaus. NIP-09 löscht einzelne Events und Relays können dem folgen. NIP-62 fordert getaggte Relays auf, alles von diesem pubkey zu löschen und zu verhindern, dass diese Events erneut importiert werden.

## Implementierungen

- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-seitige Vanish-Request-Unterstützung
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315) - Unterstützung im Memory-Backend
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316) - Unterstützung im LMDB-Backend
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317) - Unterstützung im SQLite-Backend
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318) - Datenbank-Testabdeckung für relay-spezifische Vanish-Unterstützung
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544) - Ergänzt NIP-62 Right-to-Vanish in der beworbenen Feature-Liste

---

**Primärquellen:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-side vanish support
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315)
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316)
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317)
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318)
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544)

**Erwähnt in:**
- [Newsletter #5: Notable Code Changes](/de/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: rust-nostr](/de/newsletters/2026-03-04-newsletter/)
- [Newsletter #16: Amethyst ships NIP-62 support](/de/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/de/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: nostream NIP-62 support](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-09: Event Deletion Request](/de/topics/nip-09/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
