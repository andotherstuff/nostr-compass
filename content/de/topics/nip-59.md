---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 definiert Gift Wrapping, eine Technik zum Verbergen des Absenders eines Events, indem es in Verschlüsselungsschichten mit einer Einweg-Identität eingewickelt wird.

## Struktur

Ein gift-wrapped Event hat drei Schichten:

1. **Rumor** - Der ursprüngliche unsignierte Event-Inhalt
2. **Seal** (Kind 13) - Der Rumor verschlüsselt für den Empfänger, signiert vom echten Absender
3. **Gift Wrap** (Kind 1059) - Das Seal verschlüsselt für den Empfänger, signiert von einem zufälligen Einweg-Schlüssel

Die äußere Schicht verwendet ein zufälliges Schlüsselpaar, das nur für diese Nachricht generiert wurde, sodass Beobachter es nicht mit dem Absender verknüpfen können.

## Warum drei Schichten?

- Der **Rumor** enthält den tatsächlichen Inhalt
- Das **Seal** beweist den echten Absender (nur für den Empfänger sichtbar)
- Das **Gift Wrap** verbirgt den Absender vor Relays und Beobachtern

## Löschunterstützung

Gift-Wrap-Events können jetzt über NIP-09/NIP-62-Löschanfragen gelöscht werden. Dies wurde hinzugefügt, um Benutzern zu ermöglichen, eingewickelte Nachrichten von Relays zu entfernen.

## Anwendungsfälle

- Private Direktnachrichten (NIP-17)
- Anonyme Tipps oder Whistleblowing
- Jedes Szenario, bei dem die Privatsphäre des Absenders wichtig ist

---

**Primärquellen:**
- [NIP-59 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: NIP-Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-17: Private Direktnachrichten](/de/topics/nip-17/)
