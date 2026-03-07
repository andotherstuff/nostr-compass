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

ContextVM is een protocol en toolchain om MCP (Model Context Protocol)-verkeer via Nostr te transporteren. Het laat MCP-clients en -servers elkaar vinden en ondertekende berichten uitwisselen zonder afhankelijk te zijn van een centrale registry, domeinen of OAuth.

## Hoe het werkt

De ContextVM SDK biedt TypeScript client- en servertransports voor MCP over Nostr. Bestaande MCP-servers kunnen op hun normale transports blijven draaien, terwijl een gateway ze via Nostr beschikbaar maakt, en clients zonder native Nostr-ondersteuning kunnen verbinding maken via een proxylaag.

Relays fungeren als message bus. Ze routeren events, terwijl signing en encryptie endpoints authenticatie en transportprivacy geven.

## Componenten

**SDK**: TypeScript-library met client/server transports, proxy-ondersteuning en gateway-functionaliteit om lokale MCP-servers met Nostr te verbinden.

**CVMI**: Command-line interface voor server discovery en method invocation.

**Relatr**: Trust scoring service die gepersonaliseerde scores berekent op basis van social graph distance en profile validation.

## Waarom het belangrijk is

ContextVM is een transportbrug, geen vervanging voor MCP zelf. Dat is belangrijk omdat het de adoptiekosten verlaagt: een bestaande MCP-server kan via Nostr bereikbaar worden zonder zijn tool schema of business logic te herschrijven.

Recent werk aan ContextVM heeft ook ephemeral delivery voor gift-wrapped verkeer vooruitgeduwd. Dat is nuttig voor tool calls en tussentijdse responses waarbij duurzame relay-opslag niet nodig is en extra privacyrisico's kan creëren.

## Interop-notities

In februari en maart 2026 verschoof het project van implementatie richting standaardisatie. Het team opende NIP-voorstellen voor MCP JSON-RPC over Nostr en voor een ephemeral variant van gift wrap. Zelfs als die voorstellen nog veranderen, maken ze de protocolgrens duidelijker: MCP blijft de application layer, Nostr regelt discovery en transport.

---

**Primaire bronnen:**
- [ContextVM-website](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Ephemeral Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**Vermeld in:**
- [Nieuwsbrief #11: ContextVM-nieuws](/en/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [Nieuwsbrief #12](/en/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [NIP-90: Data Vending Machines](/nl/topics/nip-90/)
