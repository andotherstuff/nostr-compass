---
title: "NIP-29: Relay-based Groups"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-04-22
draft: false
categories:
  - Social
  - Groups
---

NIP-29 definiert relay-basierte Gruppen, in denen ein Relay Mitgliedschaft, Berechtigungen und Nachrichtensichtbarkeit verwaltet.

## Funktionsweise

Gruppen werden über einen Relay-Host plus Gruppen-ID adressiert, und das Relay ist die Autorität für Mitgliedschaft und Moderation. Von Nutzern erzeugte Events, die in eine Gruppe gesendet werden, tragen ein `h`-Tag mit der Gruppen-ID. Vom Relay erzeugte Metadaten nutzen addressable Events, die mit dem eigenen Schlüssel des Relays signiert sind.

Das zentrale Metadaten-Event ist kind 39000, während kinds 39001 bis 39003 Admins, Mitglieder und unterstützte Rollen beschreiben. Moderationsaktionen laufen über Events der 9000er-Serie wie `put-user`, `remove-user`, `edit-metadata` und `create-invite`.

## Zugriffsmodell

- **private**: Nur Mitglieder können Gruppennachrichten lesen
- **closed**: Join-Requests werden ignoriert, sofern das Relay kein Invite-Code-Handling nutzt
- **hidden**: Das Relay verbirgt Gruppenmetadaten vor Nichtmitgliedern und macht die Gruppe dadurch unauffindbar
- **restricted**: Nur Mitglieder dürfen Nachrichten in die Gruppe schreiben

Diese Tags sind unabhängig voneinander. Eine Gruppe kann für alle lesbar, aber nur für Mitglieder beschreibbar sein, oder für Nichtmitglieder vollständig verborgen bleiben. Diese Trennung ist wichtig, weil Clients "private" nicht als pauschale Kurzform für alle Zugriffsregeln behandeln sollten.

## Vertrauensmodell

NIP-29 ist kein trustless Gruppenprotokoll. Das hostende Relay entscheidet, welche Moderations-Events gültig sind, welche Rollen existieren, ob Mitgliederlisten sichtbar sind und ob alte oder aus dem Kontext gerissene Nachrichten akzeptiert werden. Ein Client kann Signaturen und Timeline-Referenzen prüfen, verlässt sich aber weiterhin auf die Relay-Policy für den tatsächlichen Zustand der Gruppe.

Das macht Migration und Forking möglich, aber nicht automatisch. Dieselbe Gruppen-ID kann auf verschiedenen Relays mit unterschiedlicher Historie oder unterschiedlichen Regeln existieren. In der Praxis ist die Relay-URL also Teil der Gruppenidentität.

## Nützliche Implementierungshinweise

- Clients sollten die Relay-URL als Schlüssel des Gruppenhosts behandeln. Eine Klarstellung im Januar 2026 machte das in der Spezifikation explizit und entfernte Mehrdeutigkeit gegenüber der Nutzung eines pubkey.
- Gruppenstatus wird aus der Moderationshistorie rekonstruiert, während Events der 39000er-Serie informative Snapshots dieses Zustands sind.
- Timeline-`previous`-Referenzen sind da, um aus-dem-Kontext-gerissene Rebroadcasts über Relay-Forks hinweg zu verhindern, nicht nur, um UI-Threading zu verbessern.

## Jüngste Spezifikationsarbeit

- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) und hodlbods [Flotilla-1.7.3/1.7.4-Release-Notes](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) schlagen kind-9-Wrapping für Nicht-Chat-Inhaltstypen vor, etwa Kalender-Events, Polls und andere Payloads, damit der Raumkontext erhalten bleibt, wenn diese Objekte in eine Gruppe gesendet werden.
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) erweitert die Spezifikation um eine Subgroup-Hierarchie, sodass eine einzelne Gruppe mehrere parallele Channels hosten kann, ohne unabhängige Gruppen auf demselben Relay anzulegen. Die Subgroup-ID nutzt das bestehende `h`-Tag mit, wodurch Single-`h`-Tag-Nachrichten für ältere Clients erhalten bleiben.
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) definiert explizite Berechtigungen auf dem kind-`39003`-Rollen-Event, sodass jede Rolle zu einer benannten Menge erlaubter Operationen wird, darunter invite, add-user, remove-user, edit-metadata, delete-event und add-permission, optional mit zeitgebundener Ablaufzeit.

## Implementierungen

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) ist hodlbods primärer NIP-29-Client. [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) und [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) lieferten kind-9-Wrapping, Polls, [NIP-46](/de/topics/nip-46/)-Login via Aegis-URL-Scheme, native Share-Unterstützung für Space-Invites, Raum-Erwähnungen, Bild-Einfügen aus der mobilen Zwischenablage, Drafts und Video in Calls.
- [Wisp](https://github.com/barrydeen/wisp) fügte NIP-29-Gruppenkonfiguration für Flags, Invites, Rollen und AUTH-Prompts in [PR #471](https://github.com/barrydeen/wisp/pull/471) hinzu und härtete die AUTH-Sequenz vor Gruppen-Events `9021`, `9007` und `9009` in [PR #478](https://github.com/barrydeen/wisp/pull/478).

---

**Primärquellen:**
- [NIP-29 Specification](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Clarified `private`, `closed`, and `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Clarified relay URL as the relay key
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Added `unallowpubkey` and `unbanpubkey`
- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) - Kind-9 wrapping for non-chat content
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) - Subgroups spec
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) - Explicit role permissions on kind 39003
- [Flotilla 1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)
- [Wisp PR #471](https://github.com/barrydeen/wisp/pull/471) - NIP-29 group configuration

**Erwähnt in:**
- [Newsletter #2: NIP Updates](/de/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #6: NIP Updates](/de/newsletters/2026-01-21-newsletter/)
- [Newsletter #11: NIP Updates](/de/newsletters/2026-02-25-newsletter/)
- [Newsletter #12: NIP Updates](/de/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Flotilla 1.7.3/1.7.4](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Wisp NIP-29 config](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Updates (subgroups, role permissions)](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
