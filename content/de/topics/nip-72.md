---
title: "NIP-72: Moderated Communities"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 definiert moderierte Communities auf Nostr. Communities bieten eine Möglichkeit, Beiträge um ein gemeinsames Thema oder eine Gruppe zu organisieren, mit Moderatoren, die Inhalte genehmigen, bevor sie für Mitglieder sichtbar werden.

## Funktionsweise

Eine Community wird durch ein kind-34550-Event definiert, das vom Ersteller veröffentlicht wird. Dieses Event enthält den Community-Namen, die Beschreibung, Regeln und eine Liste von Moderatoren-Pubkeys. Das Event verwendet ein ersetzbares Event-Format (Kind-Bereich 30000-39999), sodass die Community-Definition im Laufe der Zeit aktualisiert werden kann.

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

Nutzer reichen Beiträge bei einer Community ein, indem sie ihre Events mit einem `a`-Tag versehen, der auf die Community-Definition zeigt. Diese Beiträge sind noch nicht für Community-Leser sichtbar. Ein Moderator prüft die Einreichung und veröffentlicht bei Genehmigung ein kind-4549-Approval-Event, das den Originalbeitrag umhüllt. Clients, die die Community anzeigen, zeigen nur Beiträge, die ein entsprechendes Approval-Event von einem anerkannten Moderator haben.

Dieses Genehmigungsmodell bedeutet, dass Communities lese-gefiltert sind, nicht schreib-beschränkt. Jeder kann einen Beitrag einreichen, aber nur genehmigte Beiträge erscheinen im Community-Feed. Moderatoren agieren als Kuratoren, nicht als Torwächter der zugrundeliegenden Daten.

## Überlegungen

Da Approval-Events separate Nostr-Events sind, sind Moderationsentscheidungen transparent und überprüfbar. Ein von einer Community abgelehnter Beitrag kann trotzdem von einer anderen genehmigt werden. Derselbe Inhalt kann in mehreren Communities mit unabhängiger Moderation existieren.

Relay-Unterstützung ist wichtig für die Community-Funktionalität. Clients müssen sowohl die Community-Definition als auch Approval-Events abfragen, was Relays erfordert, die diese Event-Kinds effizient indizieren.

---

**Primärquellen:**
- [NIP-72-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities

**Erwähnt in:**
- [Newsletter #15](/de/newsletters/2026-03-25-newsletter/)
