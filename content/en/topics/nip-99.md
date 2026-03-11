---
title: "NIP-99: Classified Listings"
date: 2026-03-11
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 defines addressable classified-listing events for goods, services, jobs, rentals, and other offers. It gives marketplace apps a simpler event model than the older [NIP-15](/en/topics/nip-15/) marketplace spec, which is why many current commerce clients build on NIP-99 instead.

## How It Works

Active listings use kind `30402`, while drafts or inactive listings use kind `30403`. The author pubkey is the seller or offer creator. The `content` field carries the human-readable description in Markdown, and the tags hold structured fields such as title, summary, price, location, and status.

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

The event is addressable, so a seller can update the listing while keeping the same identity tuple of pubkey, kind, and `d` tag. That makes listing revisions cleaner for clients than publishing a brand-new immutable note for every price or status change.

## Why It Matters

The strength of NIP-99 is that it leaves room for different marketplace designs while still standardizing the core listing shape. One client can focus on local classifieds, another on subscriptions, and another on global product catalogs. If they all agree on the event structure, sellers can publish once and still get some cross-client visibility.

That flexibility also explains why current marketplace projects favor it. The spec is structured enough to support search and display, but it does not force every app into a single escrow, shipping, or payment workflow.

## Implementation Notes

- `price` tags can describe one-time or recurring payments by adding an optional frequency field.
- `t` tags act as categories or search keywords.
- `image` tags let clients render gallery views without parsing the Markdown body.
- A listing can link to related events or documents with `e` or `a` tags when a marketplace wants richer product context.

## Implementations

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr marketplace using NIP-99 listings with agent-facing MCP endpoints
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Food marketplace built on the same listing layer with mixed payment options

---

**Primary sources:**
- [NIP-99 Specification](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - MCP commerce endpoints on top of NIP-99 listings
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Subscription and multi-merchant checkout on top of marketplace listings

**Mentioned in:**
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**See also:**
- [NIP-15: Marketplace Offers](/en/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/en/topics/nip-47/)
- [NIP-60: Cashu Wallet](/en/topics/nip-60/)
