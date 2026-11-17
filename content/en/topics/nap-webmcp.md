---
title: "NAP-WEBMCP: Napplet Tools for Agents (Proposed)"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NAP-WEBMCP is an open draft napplet proposal, [#150](https://github.com/napplet/naps/pull/150). It would let running napplets register typed tools for AI agents through the host shell. NAPs are napplet draft contracts, not accepted NIPs. Registering a live tool does not authorize an agent and does not grant any host permission. The shell controls which consumers can reach each tool and sets the scope of that access.

Withdrawing a registration cancels calls to that tool. Reset is a separate operation: it keeps the registered tool descriptors, revokes their exposure grants and cancels all outstanding calls for the instance. A napplet must reset before replacing the document or other context that an exposure grant applied to, and must wait for the reset acknowledgement before switching. Old executors must not read or change the new context. An acknowledgement confirms grant revocation and cancellation. It does not prove that executors have settled or rolled back their effects. A call that finishes late can establish settlement and free the execution slot, but it is not delivered as a new success to the rejected caller.

The bridge has its own limits. Descriptor and data sizes are bounded. Calls are checked for replayed sequences and for correlation mismatches. Overloads return explicit errors. Calls whose outcome is uncertain are not retried automatically. The proposal includes an optional browser projection, which is not a finalized browser API. Conformance across different agents is not established in the reviewed evidence.

**Primary sources:**
- [napplet/naps PR #150: NAP-WEBMCP](https://github.com/napplet/naps/pull/150)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#napplet-naps-150)

**See also:**
- [MCP](/en/topics/mcp/)
- [NAP-LLM](/en/topics/nap-llm/)
- [NAP-INTENT](/en/topics/nap-intent/)
