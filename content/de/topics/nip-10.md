---
title: "NIP-10: Threading für Textnotizen"
date: 2025-12-24
translationOf: /en/topics/nip-10.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-10 legt fest, wie Kind-1-Notes aufeinander verweisen, um Antwort-Threads zu bilden. Das zu verstehen ist grundlegend, wenn man Konversationsansichten bauen will.

## Wie es funktioniert

Wenn jemand auf eine Note antwortet, müssen Clients wissen: Worauf ist das eine Antwort? Was ist der Ursprung der Konversation? Wer soll benachrichtigt werden? NIP-10 beantwortet diese Fragen über `e`-Tags (Event-Referenzen) und `p`-Tags (Pubkey-Erwähnungen).

## Markierte Tags (Bevorzugt)

Moderne Clients verwenden explizite Marker in `e`-Tags:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Great point! I agree.",
  "sig": "b7d3f..."
}
```

Der `root`-Marker zeigt auf die ursprüngliche Note, die den Thread gestartet hat. Der `reply`-Marker zeigt auf die konkrete Note, auf die geantwortet wird. Wenn direkt auf die Wurzel geantwortet wird, reicht `root`, ein `reply`-Tag ist dann nicht nötig. Diese Unterscheidung ist für das Rendering wichtig: `reply` bestimmt die Einrückung in der Thread-Ansicht, während `root` alle Antworten zusammenhält.

## Threading-Regeln

- **Direkte Antwort auf die Wurzel:** Ein `e`-Tag mit `root`-Marker
- **Antwort auf eine Antwort:** Zwei `e`-Tags, eines mit `root`, eines mit `reply`
- `root` bleibt im ganzen Thread konstant, `reply` ändert sich je nachdem, worauf geantwortet wird

## Benachrichtigungen und Erwähnungen

Füge `p`-Tags für alle ein, die benachrichtigt werden sollen. Mindestens sollte der Autor der Note markiert werden, auf die geantwortet wird. Übliche Konvention ist es, auch alle `p`-Tags aus dem übergeordneten Event zu übernehmen, damit alle in der Konversation im Loop bleiben, plus alle Nutzer, die im Inhalt per @ erwähnt werden.

## Relay-Hinweise

Die dritte Position in `e`- und `p`-Tags kann eine Relay-URL enthalten, unter der dieses Event oder die Inhalte des Nutzers zu finden sein könnten. Das hilft Clients, referenzierte Inhalte abzurufen, auch wenn sie nicht mit dem ursprünglichen Relay verbunden sind.

## Interop-Hinweise

Frühe Nostr-Implementierungen leiteten die Bedeutung aus der Position der Tags ab statt aus Markern: Das erste `e`-Tag war die Wurzel, das letzte die Antwort, dazwischen liegende Tags galten als Erwähnungen. Dieser Ansatz ist veraltet, weil er Mehrdeutigkeiten erzeugt. Wenn `e`-Tags ohne Marker auftauchen, stammen sie wahrscheinlich von älteren Clients. Moderne Implementierungen sollten immer explizite Marker verwenden.

Clients müssen trotzdem beide Formate parsen, wenn sie auch ältere Threads korrekt darstellen wollen. In der Praxis ist die Interoperabilität von NIP-10 teilweise ein Migrationsproblem: Produzenten sollten markierte Tags senden, Leser aber gegenüber älteren positionsbasierten Formen tolerant bleiben.

## Aufbau von Thread-Ansichten

Um einen Thread anzuzeigen, wird zuerst das Root-Event geladen und dann nach allen Events mit einem `e`-Tag gesucht, das auf diese Wurzel verweist:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Sortiere die Ergebnisse nach `created_at` und verwende die `reply`-Marker, um die Baumstruktur aufzubauen. Events, deren `reply` auf die Wurzel zeigt, sind Antworten der obersten Ebene. Events, deren `reply` auf eine andere Antwort zeigt, sind verschachtelte Antworten.

---

**Primärquellen:**
- [NIP-10 Specification](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Erwähnt in:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
- [NIP-18: Reposts](/de/topics/nip-18/)
