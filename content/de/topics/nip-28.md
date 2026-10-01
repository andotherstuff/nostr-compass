---
title: "NIP-28: Öffentlicher Chat"
date: 2026-09-30
draft: false
categories:
  - NIPs
  - Social
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-01
---

NIP-28 beschreibt öffentliche Chatkanäle, Kanalnachrichten und clientseitige Moderation als Nostr-events. Die aktuelle Spezifikation ist als **Entwurf** und **nicht empfohlen** gekennzeichnet und verweist Entwickler für aktuelle relay-basierte Gruppen auf NIP-29.

## event-Modell

kind `40` erstellt einen Kanal; kind `41` aktualisiert dessen Metadaten; kind `42` enthält eine Nachricht. Die kinds `43` und `44` ermöglichen es einem Nutzer, in seinem Client eine Nachricht auszublenden oder einen anderen Nutzer stummzuschalten. Die tags einer Nachricht verweisen auf das event zur Kanalerstellung und können die Nachricht identifizieren, auf die geantwortet wird. relays müssen diese clientseitigen Entscheidungen zum Ausblenden und Stummschalten nicht durchsetzen.

Die [Spezifikationsänderung vom September 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb) machte einen öffentlichen Chatraum zu einem gemeinsamen Gegenstand des Protokolls. Diese historische Rolle bleibt für das Verständnis nützlich, auch wenn die [aktuelle Spezifikation](https://github.com/nostr-protocol/nips/blob/master/28.md) für neue Implementierungen einen anderen Weg empfiehlt.

---

**Primärquellen:**
- [NIP-28-Spezifikation und aktueller Status](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [Änderung zum öffentlichen Chat vom September 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**Erwähnt in:**
- [Newsletter #42: September 2022](/de/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**Siehe auch:**
- [NIP-29: relay-basierte Gruppen](/de/topics/nip-29/)
