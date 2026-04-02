---
title: "NIP-86: Relay Management API"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relays
  - Protocol
---

NIP-86 definiert eine JSON-RPC-Schnittstelle für Relay-Management, die autorisierten Clients ermöglicht, administrative Befehle über eine standardisierte API an Relays zu senden. Relay-Betreiber können Pubkeys sperren oder freigeben, Zugriffslisten verwalten und den Relay-Status abfragen, ohne relay-spezifische Tools zu benötigen.

## Funktionsweise

Die Management-API verwendet JSON-RPC-ähnliche Anfragen über HTTP auf derselben URI wie der Relay-WebSocket-Endpunkt. Anfragen verwenden den Content-Type `application/nostr+json+rpc` und authentifizieren sich mit einem [NIP-98](/de/topics/nip-98/) (HTTP Auth) signierten Event im `Authorization`-Header. Das Relay verifiziert den anfragenden Pubkey gegen seine Admin-Liste, bevor es Befehle ausführt.

Verfügbare Methoden umfassen das Sperren und Freigeben von Pubkeys, das Auflisten gesperrter Nutzer und das Abfragen der Relay-Konfiguration. Die standardisierte Schnittstelle bedeutet, dass eine einzelne Client-Implementierung jedes NIP-86-kompatible Relay verwalten kann.

## Implementierungen

- [Amethyst](https://github.com/vitorpamplona/amethyst) - Android-Client mit NIP-86-Relay-Management-UI (v1.07.0+)

---

**Primärquellen:**
- [NIP-86-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-seitige NIP-86-Unterstützung
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Relay-Management-Nutzersuchdialog

**Erwähnt in:**
- [Newsletter #16: Amethyst liefert Relay-Management](/de/newsletters/2026-04-01-newsletter/#amethyst-liefert-angepinnte-notizen-relay-management-und-request-to-vanish)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
- [NIP-98: HTTP Auth](/de/topics/nip-98/)
- [NIP-42: Authentication of Clients to Relays](/de/topics/nip-42/)
