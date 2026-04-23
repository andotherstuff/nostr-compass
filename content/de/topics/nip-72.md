---
title: "NIP-72: Moderated Communities"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 definiert moderierte Communities auf Nostr. Communities bieten eine Möglichkeit, Beiträge rund um ein gemeinsames Thema oder eine Gruppe zu organisieren, wobei Moderatoren Inhalte genehmigen, bevor sie für Mitglieder sichtbar werden.

## Funktionsweise

Eine Community wird durch ein kind-34550-Event definiert, das vom Ersteller veröffentlicht wird. Dieses Event enthält den Community-Namen, die Beschreibung, Regeln und eine Liste von Moderator-pubkeys. Das Event nutzt ein ersetzbares Event-Format im Bereich kind `30000-39999`, sodass die Community-Definition im Lauf der Zeit aktualisiert werden kann.

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

Nutzer reichen Beiträge in einer Community ein, indem sie ihre Events mit einem `a`-Tag versehen, das auf die Community-Definition zeigt. Diese Beiträge sind für Leser der Community zunächst noch nicht sichtbar. Ein Moderator prüft die Einreichung und veröffentlicht bei Genehmigung ein kind-4549-Approval-Event, das den Originalbeitrag umhüllt. Clients, die die Community anzeigen, zeigen nur Beiträge an, für die ein entsprechendes Approval-Event eines anerkannten Moderators existiert.

Dieses Approval-Modell bedeutet, dass Communities lesegefiltert sind, nicht schreibbeschränkt. Jeder kann einen Beitrag einreichen, aber nur genehmigte Beiträge erscheinen im Community-Feed. Moderatoren agieren als Kuratoren statt als Gatekeeper der zugrunde liegenden Daten.

## Überlegungen

Weil Approval-Events separate Nostr-Events sind, sind Moderationsentscheidungen transparent und auditierbar. Ein Beitrag, der von einer Community abgelehnt wird, kann von einer anderen trotzdem genehmigt werden. Derselbe Inhalt kann in mehreren Communities mit unabhängiger Moderation existieren.

Relay-Unterstützung ist wichtig für die Funktionalität von Communities. Clients müssen sowohl die Community-Definition als auch Approval-Events abfragen, was Relays erfordert, die diese Event-Kinds effizient indexieren.

Verglichen mit [NIP-29](/de/topics/nip-29/) relay-basierten Gruppen, bei denen das Relay die Autorität für Mitgliedschaft und Moderation ist, lebt NIP-72 in normalen Nostr-Events. Jedes Relay, das kind `34550`, `4549` und die Einreichungs-Kinds trägt, kann eine Community bedienen, und Moderation ist sichtbar und forkeable. Der Tradeoff ist, dass nicht genehmigte Einreichungen nur auf der Client-Render-Ebene verborgen werden. Wenn Spam komplett vom Wire ferngehalten werden muss, ist NIP-29 die bessere Wahl.

## Implementierungen

- [noStrudel](https://github.com/hzrd149/nostrudel) unterstützt NIP-72-Communities seit Langem, inklusive einer Pending-Submission-Warteschlange für Moderatoren.
- [Amethyst](https://github.com/vitorpamplona/amethyst) fügte in [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) erstklassige Community-Erstellung und -Verwaltung hinzu: das Erstellen der kind-`34550`-Community-Definition, das Hinzufügen von Moderatoren und Relay-Hints, das Einreichen von Beiträgen mit `a`-Tag und die Verwaltung ausstehender Freigaben über kind-`4549`-Events.

---

**Primärquellen:**
- [NIP-72 Specification](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - NIP-72 community creation and moderation

**Erwähnt in:**
- [Newsletter #15](/de/newsletters/2026-03-25-newsletter/)
- [Newsletter #19: Amethyst community support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-29: Relay-based Groups](/de/topics/nip-29/)
