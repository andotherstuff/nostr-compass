---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 defines Data Vending Machines (DVMs), a protocol for requesting and delivering paid computational work over Nostr.

## How It Works

Customers publish job request events in the `5000-5999` range. Each request can include one or more `i` tags for inputs, `param` tags for job-specific settings, an `output` tag for the expected format, a `bid` ceiling, and relay hints for where replies should appear. Service providers answer with a matching result kind in the `6000-6999` range, always `1000` higher than the request kind.

Results include the original request, the customer's pubkey, and optionally an `amount` tag or invoice. Providers can also send kind `7000` feedback events such as `payment-required`, `processing`, `partial`, `error`, or `success`, which gives clients a way to show progress before the final result arrives.

## Payment and Privacy

The protocol intentionally leaves business logic open. A provider can ask for payment before work starts, after returning a sample, or after delivering the full result. That flexibility matters because DVM jobs range from cheap text transforms to expensive GPU work, and providers do not all take the same payment risk.

If a customer wants private inputs, the request can move `i` and `param` data into encrypted `content` and mark the event with an `encrypted` tag plus the provider's `p` tag. That protects prompts or source material from relay observers, but it also means the customer must target a specific provider instead of broadcasting an open market request.

## Interop Notes

NIP-90 supports job chaining through `i` tags with input type `job`, so one result can feed a later request. That makes multi-step flows possible without inventing a separate orchestration layer.

Provider discovery is outside the request/response loop itself. The spec points to [NIP-89: Recommended Application Handlers](/en/topics/nip-89/) announcements for advertising supported job kinds, which is how clients can discover vendors before they publish a request.

---

**Primary sources:**
- [NIP-90 Specification](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mentioned in:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #19: Forgesworn toll-booth-dvm](/en/newsletters/2026-04-22-newsletter/#forgesworn-publishes-a-29-repo-cryptographic-toolkit-for-nostr)
- [Newsletter #19: Agent Reputation Attestations proposal](/en/newsletters/2026-04-22-newsletter/#nip-updates)

**See also:**
- [NIP-89: Recommended Application Handlers](/en/topics/nip-89/)
