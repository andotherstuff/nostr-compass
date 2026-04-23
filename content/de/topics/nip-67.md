---
title: "NIP-67: EOSE Completeness Hint"
date: 2026-04-22
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67 ist ein offener Vorschlag, der die bestehende `EOSE`-Nachricht aus [NIP-01](/de/topics/nip-01/) um ein optionales drittes Element erweitert, das anzeigt, ob das Relay jedes gespeicherte Event geliefert hat, das zum Filter passt. Damit soll die unzuverlässige Heuristik ersetzt werden, mit der Clients heute entscheiden, ob ein Abo vollständig ist oder von einem Relay-seitigen Cap abgeschnitten wurde.

## Das Problem

`EOSE` markiert die Grenze zwischen gespeicherten und Echtzeit-Events, trägt aber keine Information über Vollständigkeit. In der Praxis erzwingen Relays pro Subscription ein Cap, häufig zwischen 300 und 1000 Events, unabhängig vom `limit` des Clients. Ein Client, der die letzten 500 Notizen von einem Relay mit einem Cap von 300 anfragt, erhält 300 Events und ein `EOSE`, kann aber nicht unterscheiden zwischen "das ist alles" und "wir haben unterwegs abgeschnitten".

Grenzfälle mit identischen Timestamps verschärfen das Problem. Wenn bei der Paginierung `until = oldest_created_at` gesetzt wird, droht entweder das Übersehen oder das doppelte Laden von Events mit demselben ältesten Timestamp, abhängig davon, wie das Relay Timestamps vergleicht.

## Die Änderung

NIP-67 fügt `EOSE` ein optionales drittes Element hinzu:

```
["EOSE", "<subscription_id>", "finish"]   // alle passenden gespeicherten Events wurden geliefert
["EOSE", "<subscription_id>"]             // keine Aussage über Vollständigkeit (Legacy)
```

Spezifiziert ist nur das positive Signal. Ein Relay, das NIP-67-Unterstützung ankündigt, den Hinweis aber weglässt, signalisiert damit, dass noch mehr da ist. Ein Relay, das keine Unterstützung ankündigt, fällt auf die bestehende Heuristik zurück. Die Änderung ist also rückwärtskompatibel zu allen aktuellen Clients und Relays.

Clients, die wissen, dass ihr Relay NIP-67 unterstützt, können die Paginierung sofort beenden, sobald sie `"finish"` sehen, den zusätzlichen Roundtrip vermeiden, wenn das Cap genau der Ergebnismenge entspricht, und dem Nutzer korrekte Vollständigkeit anzeigen.

## Status

Der Vorschlag ist als [PR #2317](https://github.com/nostr-protocol/nips/pull/2317) gegen das NIPs-Repository offen.

---

**Primärquellen:**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Erwähnt in:**
- [Newsletter #19: NIP Updates](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-01: Basic protocol flow](/de/topics/nip-01/)
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
