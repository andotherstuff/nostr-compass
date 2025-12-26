---
title: "NIP-10: Textnotiz-Threading"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-10 spezifiziert, wie Kind-1-Notizen aufeinander verweisen, um Antwort-Threads zu bilden. Das Verständnis davon ist essenziell für den Aufbau von Konversationsansichten.

## Das Problem

Wenn jemand auf eine Notiz antwortet, müssen Clients wissen: Worauf ist dies eine Antwort? Was ist die Wurzel der Konversation? Wer soll benachrichtigt werden? NIP-10 beantwortet diese Fragen durch `e`-Tags (Event-Referenzen) und `p`-Tags (Pubkey-Erwähnung).

## Markierte Tags (bevorzugt)

Moderne Clients verwenden explizite Markierungen in `e`-Tags:

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
  "content": "Guter Punkt! Ich stimme zu.",
  "sig": "b7d3f..."
}
```

Die `root`-Markierung zeigt auf die ursprüngliche Notiz, die den Thread gestartet hat. Die `reply`-Markierung zeigt auf die spezifische Notiz, auf die geantwortet wird. Wenn Sie direkt auf die Root antworten, verwenden Sie nur `root` (kein `reply`-Tag nötig). Die Unterscheidung ist wichtig für das Rendering: Das `reply` bestimmt die Einrückung in einer Thread-Ansicht, während `root` alle Antworten zusammengruppiert.

## Threading-Regeln

- **Direkte Antwort auf Root:** Ein `e`-Tag mit `root`-Markierung
- **Antwort auf eine Antwort:** Zwei `e`-Tags, eines `root` und eines `reply`
- Das `root` bleibt im gesamten Thread konstant; `reply` ändert sich je nachdem, worauf Sie antworten

## Pubkey-Tags für Benachrichtigungen

Fügen Sie `p`-Tags für jeden ein, der benachrichtigt werden soll. Mindestens taggen Sie den Autor der Notiz, auf die Sie antworten. Konvention ist es, auch alle `p`-Tags vom Eltern-Event einzuschließen (damit jeder in der Konversation informiert bleibt), plus alle Benutzer, die Sie in Ihrem Inhalt @erwähnen.

## Relay-Hinweise

Die dritte Position in `e`- und `p`-Tags kann eine Relay-URL enthalten, wo dieses Event oder der Inhalt des Benutzers gefunden werden könnte. Dies hilft Clients, den referenzierten Inhalt abzurufen, auch wenn sie nicht mit dem ursprünglichen Relay verbunden sind.

## Veraltete positionelle Tags

Frühe Nostr-Implementierungen leiteten die Bedeutung aus der Tag-Position ab statt aus Markierungen: Das erste `e`-Tag war Root, das letzte war Reply, die mittleren waren Erwähnung. Dieser Ansatz ist veraltet, weil er Mehrdeutigkeit erzeugt. Wenn Sie `e`-Tags ohne Markierungen sehen, stammen sie wahrscheinlich von älteren Clients. Moderne Implementierungen sollten immer explizite Markierungen verwenden.

## Thread-Ansichten erstellen

Um einen Thread anzuzeigen, rufen Sie das Root-Event ab und fragen dann nach allen Events mit einem `e`-Tag, das auf diese Root verweist:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Sortieren Sie die Ergebnisse nach `created_at` und verwenden Sie `reply`-Markierungen, um die Baumstruktur aufzubauen. Events, deren `reply` auf die Root zeigt, sind Antworten der obersten Ebene; Events, deren `reply` auf eine andere Antwort zeigt, sind verschachtelte Antworten.

---

**Primärquellen:**
- [NIP-10 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Erwähnt in:**
- [Newsletter #2: NIP Deep Dive](/de/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
