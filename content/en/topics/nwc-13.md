---
title: "NWC-13: Connection budgets"
date: 2026-10-21
draft: false
categories:
  - Protocols
---

NWC-13 is an optional draft NIP-47 extension whose `get_budget` method lets an app query the spending budget of its own connection. It is a parameterless read method with a permission separate from `get_balance`. A configured budget reports `used_budget` and `total_budget` in millisatoshis with a renewal period. An unconfigured budget returns an empty `result` object, which clients must keep distinct from a configured limit of zero. The budget caps spending, and whether the wallet holds enough funds is verified separately. The spec merged into the nostr-wallet-connect/nwc repository on 20 October as documentation; wallet implementations remain unverified. NWC-13 only queries budgets, and creating or changing one requires separate operations.

## Primary sources

- [nostr-wallet-connect/nwc PR #7: NWC-13 connection budgets](https://github.com/nostr-wallet-connect/nwc/pull/7)
- [NWC-13 specification at commit 36ab132](https://github.com/nostr-wallet-connect/nwc/blob/36ab132bbce1b3296895cff47729c94065e7c202/13.md)

## Mentioned in

- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#nwc-get_budget-method)
