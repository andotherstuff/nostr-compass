---
title: "NIP-18: Reposts"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 definiert, wie Events repostet werden, ähnlich wie Retweets auf anderen Plattformen.

## Wie es funktioniert

Ein Repost ist ein Kind-6-Event, für Kind-1-Notizen, oder ein Kind-16-Event, für generische Reposts, das Folgendes enthält:
- ein `e`-Tag, das auf das repostete Event verweist
- ein `p`-Tag, das auf den ursprünglichen Autor verweist
- optional das vollständige Original-Event im Feld `content`

Kind 6 ist spezifisch für Text Notes. Kind 16 existiert, damit Clients auch andere Event-Typen reposten können, ohne so zu tun, als wäre alles eine Kind-1-Notiz.

## Interop-Hinweise

Die Unterstützung für Reposts addressable Events wurde mit `a`-Tag-Support verbessert. Dadurch können Reposts von addressable Events, Kinds 30000-39999, diese über ihre Adresse statt über eine konkrete Event-ID referenzieren.

Diese Unterscheidung ist wichtig, weil addressable Events im Lauf der Zeit aktualisiert werden können. Ein Repost per `a`-Koordinate lässt Clients auf die aktuelle Version eines addressable Events zeigen, während ein Repost per Event-ID eine konkrete historische Instanz festschreibt.

## Warum es wichtig ist

Reposts sind mehr als ein Share-Button in der UI. Sie sind Teil davon, wie Inhalte sich durch Social Graphs bewegen, wie Clients Engagement zählen und wie Relay-Hint-Daten durch das Netzwerk weitergereicht werden. Wenn ein Client Repost-Tags falsch verarbeitet, können Thread-Rekonstruktion und Event-Fetching auf subtile Weise kaputtgehen.

---

**Primärquellen:**
- [NIP-18 Specification](https://github.com/nostr-protocol/nips/blob/master/18.md)
- [PR #2132](https://github.com/nostr-protocol/nips/pull/2132) - `a` tag support for generic reposts

**Erwähnt in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #8: News](/en/newsletters/2026-02-04-newsletter/#news)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
- [NIP-10: Text Note Threading](/de/topics/nip-10/)
