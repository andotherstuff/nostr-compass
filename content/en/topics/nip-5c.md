---
title: "NIP-5C: Scrolls (WASM Programs)"
date: 2026-04-08
description: "Defines conventions for publishing and discovering WebAssembly programs on Nostr, with WASM binaries distributed as Nostr events."
---

NIP-5C (formerly NIP-A5) defines conventions for publishing, discovering, and executing WebAssembly programs ("scrolls") on Nostr. WASM binaries are stored as Nostr events, allowing any client to fetch and run them in a sandboxed runtime.

## How It Works

Developers publish WASM programs as Nostr events containing the compiled binary. Clients discover these programs through standard Nostr queries, download the WASM binary from the event, and execute it in a sandboxed WebAssembly runtime. The sandbox prevents scrolls from accessing the host system directly, limiting them to the capabilities the runtime explicitly provides.

## Use Cases

- **Portable compute**: Run programs on any client that supports WASM execution
- **Decentralized app distribution**: Publish and discover applications without app stores
- **Composable tools**: Chain scrolls together for complex workflows

## Demo

A [demo app](https://nprogram.netlify.app/) shows scrolls running in-browser, with example programs published as Nostr events.

---

**Primary sources:**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - Scrolls (WASM Programs) proposal

**Mentioned in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/#nip-updates)

**See also:**
- [NIP-5D (Web Applets)](/en/topics/nip-5d/)
- [NIP-5A (Static Websites)](/en/topics/nip-5a/)
