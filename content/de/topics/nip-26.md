---
title: "NIP-26: Delegiertes Signieren von events"
date: 2026-09-30
draft: false
categories:
  - NIPs
  - Identity
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-01
---

NIP-26 dokumentiert eine Möglichkeit, mit der ein Nostr-Schlüssel einen anderen Schlüssel autorisieren kann, eine begrenzte Menge von events zu signieren. Die aktuelle Spezifikation ist als **Entwurf** und **nicht empfohlen** gekennzeichnet und hält somit einen früheren Entwurf fest, statt eine Empfehlung für eine neue Integration zu geben.

## Funktionsweise

Der Kontoschlüssel signiert ein Delegationstoken, das den Schlüssel des Bevollmächtigten und die Bedingungen benennt. Die Bedingungen können die kinds von events und die `created_at`-Zeitpunkte einschränken. Der Bevollmächtigte signiert das event mit seinem eigenen Schlüssel und fügt das Token in einem `delegation`-tag hinzu. Ein Leser muss sowohl die Signatur des events als auch das Delegationstoken anhand dieser Bedingungen überprüfen. relays, die dieses Verfahren unterstützen, können auch nach dem Delegierenden suchen.

Das Modell ermöglicht es einer Anwendung, zu veröffentlichen, ohne den primären Signaturschlüssel des Kontos zu besitzen. Die zusätzlichen Anforderungen an die Validierung und die Suche über relays erklären, warum Implementierungen eine gewöhnliche Signatur eines events nicht als ausreichenden Nachweis einer delegierten Identität behandeln können. Die [aktuelle Spezifikation](https://github.com/nostr-protocol/nips/blob/master/26.md) kennzeichnet den Ansatz ausdrücklich als nicht empfohlen.

---

**Primärquellen:**
- [NIP-26-Spezifikation und aktueller Status](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [Text zum delegierten Signieren vom September 2022](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**Erwähnt in:**
- [Newsletter #42: September 2022](/de/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
