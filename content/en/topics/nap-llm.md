---
title: "NAP-LLM: Napplet Language Model Access"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NAP-LLM is a napplet draft contract that lets a napplet request language-model generations from its host runtime. NAPs are napplet draft contracts, not accepted NIPs.

[PR #143](https://github.com/napplet/naps/pull/143) merged as development on `nap-llm`, not yet integrated into `master`. It is a merged change to an open draft branch, and `master` has not adopted it. The change adds optional consent for sessions with several steps. A runtime may offer one visible grant, which the user can revoke, that covers several generations on one handle as long as the tool set does not change. The grant must tell the user that later prompts and images will not be reviewed one at a time, and that tool results will not be reviewed either. It must also state its limits on duration and count, along with any charge limits.

Authorizing each generation separately remains the default. Users can decline a session and approve a single generation. Revoking the grant cancels work in progress, and generations with an uncertain outcome are not retried automatically. No runtime implementation has been established.

**Primary sources:**
- [napplet/naps PR #143](https://github.com/napplet/naps/pull/143)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#napplet-naps-143)

**See also:**
- [NAP-WEBMCP](/en/topics/nap-webmcp/)
- [MCP](/en/topics/mcp/)
- [NIP-FA (proposed): AI Agent Keys](/en/topics/nip-fa-ai-agent-keys/)
