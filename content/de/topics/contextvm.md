---
title: "ContextVM"
date: 2026-02-25
translationOf: /en/topics/contextvm.md
translationDate: 2026-03-07
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---

ContextVM ist ein Protokoll und eine Toolchain für den Transport von MCP-Datenverkehr (Model Context Protocol) über Nostr. Es ermöglicht MCP-Clients und -Servern, sich gegenseitig zu finden und signierte Nachrichten auszutauschen, ohne auf eine zentrale Registry, Domains oder OAuth angewiesen zu sein.

## Wie es funktioniert

Das ContextVM SDK bietet TypeScript-Client- und Server-Transporte für MCP über Nostr. Bestehende MCP-Server können auf ihren normalen Transporten bleiben, während ein Gateway sie für Nostr zugänglich macht, und Clients ohne native Nostr-Unterstützung können sich über eine Proxy-Schicht verbinden.

Relays fungieren als Message-Bus. Sie leiten Events weiter, während Signierung und Verschlüsselung den Endpunkten Authentifizierung und Transport-Privatsphäre bieten.

## Komponenten

**SDK**: TypeScript-Bibliothek mit Client/Server-Transporten, Proxy-Unterstützung und Gateway-Funktionalität für die Brückenbildung zwischen lokalen MCP-Servern und Nostr.

**CVMI**: Kommandozeilenschnittstelle für Server-Discovery und Methodenaufruf.

**Relatr**: Trust-Scoring-Dienst, der personalisierte Scores aus der Social-Graph-Distanz und Profilvalidierung berechnet.

## Warum es wichtig ist

ContextVM ist eine Transport-Brücke, kein Ersatz für MCP selbst. Das ist wichtig, weil es die Adoptionskosten senkt: Ein bestehender MCP-Server kann Nostr-Erreichbarkeit gewinnen, ohne sein Tool-Schema oder seine Geschäftslogik neu schreiben zu müssen.

Aktuelle ContextVM-Arbeit hat auch ephemere Zustellung für Gift-Wrapped-Traffic vorangetrieben. Das ist nützlich für Tool-Aufrufe und Zwischenantworten, bei denen dauerhafte Relay-Speicherung unnötig ist und zusätzliche Datenschutzrisiken schaffen kann.

## Interop-Hinweise

Im Februar und März 2026 bewegte sich das Projekt von der Implementierung zur Standardisierung. Das Team öffnete NIP-Vorschläge für MCP JSON-RPC über Nostr und für eine ephemere Variante von Gift Wrap. Auch wenn sich diese Vorschläge noch ändern, zeigen sie die Protokollgrenze klarer: MCP bleibt die Anwendungsschicht, Nostr übernimmt Discovery und Transport.

---

**Primärquellen:**
- [ContextVM Website](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Ephemeral Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**Erwähnt in:**
- [Newsletter #11: ContextVM News](/en/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [NIP-90: Data Vending Machines](/de/topics/nip-90/)
