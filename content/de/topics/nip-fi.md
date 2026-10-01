---
title: "Buzz NIP-FI: Föderierte Identitätszusicherungen"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-01
---

NIP-FI ist die **projektspezifische** Spezifikation von Buzz für föderierte Identitätszusicherungen. Der Name impliziert weder eine Übernahme durch das Repository `nostr-protocol/nips` noch Interoperabilität mit relays außerhalb von Buzz.

## HTTP-Eingang

Bei geschützten HTTP-Anfragen im Durchsetzungsmodus kombiniert Buzz eine föderierte Identitätszusicherung mit einem nach NIP-98 signierten Autorisierungs-event. Der durch die HTTP-Signatur nachgewiesene öffentliche Nostr-Schlüssel muss mit dem in der Zusicherung genannten Schlüssel übereinstimmen. Fehlende, nicht übereinstimmende oder nicht überprüfbare Nachweise werden zurückgewiesen. Buzz nutzt diese Kombination, um die Autorisierungsentscheidung eines externen Identitätsausstellers mit dem Nostr-Schlüssel zu verknüpfen, der die Anfrage stellt.

Die [Überarbeitung der Projektspezifikation](https://github.com/block/buzz/pull/7254) definiert das Durchsetzungsmodell. Die [zusammengeführte Implementierung des HTTP-Eingangs](https://github.com/block/buzz/pull/7264) deckt die geschützten HTTP-Schnittstellen von Buzz ab, einschließlich relay-Bridge sowie Medien-, Workflow- und Git-Pfaden. Die Zusammenführung berichtet über Tests des Quellcodes; sie bedeutet nicht, dass ein anderer Nostr-relay dieselbe Richtlinie implementiert.

---

**Primärquellen:**
- [Überarbeitung der Buzz-NIP-FI-Spezifikation](https://github.com/block/buzz/pull/7254)
- [Implementierung des HTTP-Eingangs von Buzz](https://github.com/block/buzz/pull/7264)

**Erwähnt in:**
- [Newsletter #42: Identitätskontrollen von Buzz](/de/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
