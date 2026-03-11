---
title: "NIP-29: Relay-basierte Gruppen"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-03-11
draft: false
categories:
  - Social
  - Groups
---

NIP-29 definiert Relay-basierte Gruppen, bei denen ein Relay Mitgliedschaft, Berechtigungen und die Sichtbarkeit von Nachrichten verwaltet.

## Wie es funktioniert

Gruppen werden durch einen Relay-Host plus eine Gruppen-ID bestimmt, und das Relay ist die Autorität für Mitgliedschaft und Moderation. Von Nutzern erzeugte Events, die in eine Gruppe gesendet werden, tragen ein `h`-Tag mit der Gruppen-ID. Vom Relay erzeugte Metadaten verwenden adressierbare Events, die mit dem eigenen Schlüssel des Relays signiert sind.

Das zentrale Metadaten-Event ist kind 39000, während kinds 39001 bis 39003 Admins, Mitglieder und unterstützte Rollen beschreiben. Moderationsaktionen laufen über 9000er-Events wie `put-user`, `remove-user`, `edit-metadata` und `create-invite`.

## Zugriffsmodell

- **private**: Nur Mitglieder können Gruppennachrichten lesen
- **closed**: Beitrittsanfragen werden ignoriert, sofern das Relay kein Invite-Code-Handling verwendet
- **hidden**: Das Relay verbirgt Gruppenmetadaten vor Nicht-Mitgliedern, sodass die Gruppe nicht auffindbar ist
- **restricted**: Nur Mitglieder können Nachrichten in die Gruppe schreiben

Diese Tags sind voneinander unabhängig. Eine Gruppe kann für alle lesbar sein, aber nur für Mitglieder beschreibbar, oder für Nicht-Mitglieder vollständig verborgen bleiben. Diese Trennung ist wichtig, weil Clients `private` nicht als pauschale Kurzform für jede Zugriffsregel behandeln sollten.

## Vertrauensmodell

NIP-29 ist kein trustless Gruppenprotokoll. Das hostende Relay entscheidet, welche Moderations-Events gültig sind, welche Rollen es gibt, ob Mitgliederlisten sichtbar sind und ob alte oder aus dem Kontext gerissene Nachrichten akzeptiert werden. Ein Client kann Signaturen und Timeline-Referenzen verifizieren, ist für den tatsächlichen Zustand der Gruppe aber weiterhin auf die Relay-Policy angewiesen.

Dadurch werden Migration und Forks möglich, aber nicht automatisch. Dieselbe Gruppen-ID kann auf verschiedenen Relays mit unterschiedlicher Historie oder unterschiedlichen Regeln existieren, deshalb ist die Relay-URL in der Praxis Teil der Gruppenidentität.

## Nützliche Implementierungshinweise

- Clients sollten die Relay-URL als Host-Schlüssel der Gruppe behandeln. Eine Klarstellung von Januar 2026 hat das in der Spezifikation explizit gemacht und die Mehrdeutigkeit beseitigt, ob stattdessen ein pubkey verwendet werden soll
- Der Gruppenzustand wird aus der Moderationshistorie rekonstruiert, während 39000er-Relay-Events nur informative Schnappschüsse dieses Zustands liefern
- Timeline-`previous`-Referenzen sollen verhindern, dass Nachrichten über Relay-Forks hinweg aus dem Kontext gerissen erneut verbreitet werden, nicht nur das Threading in der UI verbessern

---

**Primärquellen:**
- [NIP-29 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Klarstellung von `private`, `closed` und `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Klarstellung der Relay-URL als Relay-Schlüssel
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - `unallowpubkey` und `unbanpubkey` hinzugefügt

**Erwähnt in:**
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #11: NIP Updates](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
