---
title: "Bitcredit"
date: 2026-03-25
draft: false
categories:
  - Finance
  - Commerce
  - Infrastructure
---

Bitcredit is an e-bill trade-finance system for businesses. The public site presents Bitcredit Core as software for issuing, endorsing, paying, and managing electronic bills of exchange, while the open-source core repo implements a Nostr transport layer alongside the business logic and persistence crates.

## How It Works

Bitcredit models trade credit as electronic bills of exchange, or ebills. A buyer issues an ebill with a future due date, the holder can endorse it to another business, and the final holder can request payment at maturity.

The Bitcredit site also describes a mint-based liquidity path. Instead of waiting for maturity, a holder can request an offer from a Bitcredit mint, receive ecash immediately, and then use that ecash to pay suppliers or workers.

## Implementation Notes

The `Bitcredit-Core` repository splits the system into multiple Rust crates. `bcr-ebill-core` handles the data model, `bcr-ebill-api` contains business logic, `bcr-ebill-persistence` handles storage, and `bcr-ebill-transport` provides the network transport API with a Nostr implementation.

That architecture matters because Bitcredit is not just a website or wallet flow. It is a business-document system with transport, state, and settlement logic separated into reusable components, including a WASM entrypoint for web deployments.

## Recent Work

Compass first covered Bitcredit in March 2026 when `v0.5.3` added API fields for bill payment actions and bill state, and fixed signing-address handling for anonymous signers. The following release, `v0.5.4`, continued that API work by adapting `BitcreditBillResult`, refining payment and acceptance state, and adding more explicit handling for optional fields.

Those changes are small compared with the broader Bitcredit concept, but they show where the implementation is moving: cleaner frontend ergonomics, clearer bill lifecycle state, and better handling for anonymous or bearer-style signing flows.

---

**Primary sources:**
- [Bitcredit website](https://www.bit.cr/)
- [Bitcredit: How it works](https://www.bit.cr/how-it-works)
- [Bitcredit-Core repository](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Bitcredit-Core documentation index](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846: Improve Status Flags and Add Payment Actions](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849: Fix signing address and signatory for anon signers](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**Mentioned in:**
- [Newsletter #13: Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
