---
title: "Model Context Protocol (MCP)"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

The Model Context Protocol (MCP) has a client-host-server architecture and exchanges context over JSON-RPC. A host can run multiple client instances. The capabilities each server declares determine which features it exposes. MCP is a general framework. Carrying it over Nostr is a separate integration and is not an official NIP.

The ContextVM SDK carries MCP traffic over Nostr. Its open proposal [#120](https://github.com/ContextVM/sdk/pull/120) maps the CEP-8 payment requirements for MCP over Nostr to conformance tests that fail closed. It also adds a relay harness that injects controlled faults. The six commits that are new in this stacked pull request reject BOLT11 invoices whose amount differs from the offered amount. They also reject oversized payment-option arrays before validating the individual elements. Earlier commits in the stack belong to separate work. The pull request is unmerged and unreleased. Test results come from the author. An independent audit or rerun of those tests is not established in the reviewed evidence.

**Primary sources:**
- [MCP architecture, specification version 2026-07-28](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/docs/specification/2026-07-28/architecture/index.mdx)
- [ContextVM SDK PR #120: CEP-8 conformance and failure qualification](https://github.com/ContextVM/sdk/pull/120)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#contextvm-sdk)

**See also:**
- [NAP-WEBMCP](/en/topics/nap-webmcp/)
- [L402](/en/topics/l402/)
- [NIP-01: Basic protocol](/en/topics/nip-01/)
