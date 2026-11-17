---
title: "NIP-69: Peer-to-Peer Trading"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 defines a shared event format for peer-to-peer bitcoin trade offers. When several platforms publish orders as `kind:38383` events, one client can read all of them as a single orderbook while each platform keeps its own liquidity. The format makes offers visible across platforms and does not reserve funds, hold escrow or settle trades; taking an order, quoting a price, handling disputes and holding funds all stay with the platform that published the offer.

## How it works

Orders are addressable events, identified by author, kind and `d` tag. When a platform updates an order's status, it publishes a new event at the same address, and that event replaces the earlier version. An event from a different author that reuses the same `d` value is a separate order.

Clients should check each event's [NIP-01](https://raw.githubusercontent.com/nostr-protocol/nips/master/01.md) id and signature. A valid signature identifies who broadcast the order, though it says nothing about whether that party has the funds or will trade honestly.

## Order tags

The required tags are:

- `d`: the order identifier, which must be unique among the author's orders. Any unique string works, and a UUID is not required.
- `k`: the order type, either `buy` or `sell`.
- `f`: the currency, given as an ISO 4217 code.
- `s`: the order status, described below.
- `amt`: the bitcoin amount in satoshis. A value of `0` does not make the order free; it means the platform quotes the amount from its price API when someone takes the order.
- `fa`: the fiat amount, given either as one value or as two values that form a range.
- `pm`: the accepted payment methods.
- `premium`: the percentage above or below the market price.
- `network`: the bitcoin network, such as mainnet, testnet, signet or regtest.
- `layer`: the settlement layer, such as onchain, lightning or liquid.
- `expires_at`: the time when a pending order stops being open.
- `expiration`: the time when relays may delete the event under [NIP-40](/en/topics/nip-40/).
- `y`: the platform's name.
- `z`: always the fixed value `order`.

The optional tags are:

- `source`: a URI that links back to the order on its platform. It need not be HTTPS, and clients should treat it as a link the user chooses to follow and never run it as code.
- `rating`: a reputation score whose format and calculation each platform defines for itself, so scores from different platforms are not comparable.
- `name`: a display name.
- `g`: a geohash for face-to-face trades. Because the tag is public, a precise geohash can reveal where a trader plans to meet.
- `bond`: an advertised security deposit. The tag announces a deposit amount without enforcing the deposit or proving that anyone paid it.

Some live events differ from this tag set, so clients should parse orders defensively.

## Status and time

The status values are:

| Status | Meaning |
| --- | --- |
| `pending` | Open for a counterparty |
| `in-progress` | A trade has started |
| `success` | The trade completed |
| `canceled` | The maker withdrew the order |
| `expired` | The order passed its lifetime |

The two time tags do different jobs: `expires_at` sets how long a pending offer stays open, while `expiration` asks relays to delete the event under NIP-40.

Relays can deliver events late or return older versions that have since been replaced, so an orderbook should compare `created_at`, `s` and `expires_at` before showing an order as open.

## Privacy

Fiat currency, payment methods, geohash and posting times are all public, and together they can reveal a trader's habits.

## Implementations

Each entry below describes source code at a pinned commit. The entries cover code paths only and make no claims about builds, live trades or whether the apps work with each other.

- **[Mostro](https://github.com/MostroP2P/mostro)**, at commit `2211a7e`, [publishes public orders](https://github.com/MostroP2P/mostro/blob/2211a7e02bba87416a66026bc653ae1bff886b2a/src/util.rs#L475) with empty content and the order's UUID as `d`, and records each event id. Because its `created_at` values always increase, a take or cancel in the same second as the first pending event still sorts after it under NIP-01 replacement rules. Before publishing, [order validation](https://github.com/MostroP2P/mostro/blob/2211a7e02bba87416a66026bc653ae1bff886b2a/src/app/order.rs#L131):
  - rejects ranges that have only one end;
  - checks fixed fiat amounts, non-negative sats and range limits;
  - checks quote bounds.
- **[RoboSats](https://github.com/RoboSats/robosats)**, at commit `babf62e`, [signs orders](https://github.com/RoboSats/robosats/blob/babf62e2238f262182d0bf638496aaa53e286853/api/nostr.py#L36) with the coordinator's key and sends them to a local strfry relay. The `d` value is a UUID derived from an MD5 hash of the coordinator alias and the order id. Alongside it, each order event carries:
  - buy/sell type, currency, and amount or range;
  - payment methods, premium and source;
  - expiration, bond, platform, network and layer;
  - a geohash when coordinates exist.

  Published orders are reported as `pending` and every other internal state as `success`, so not all five statuses are used. The `pm` tag comes from splitting the payment-method text on spaces, which shows that platform formats can differ from the spec's wording.
- **[lnp2pBot](https://github.com/lnp2pBot/bot)**, at commit `6d91a79`, signs and publishes an order event whenever a public order changes. The [tag builder](https://github.com/lnp2pBot/bot/blob/6d91a794d03da0789f88331c28039e95724c3fc9/bot/modules/nostr/events.ts#L11) emits:
  - `d`, `k`, `f`, `s`, `amt` and `fa` (one amount or a min/max range);
  - `pm`, `premium` and `rating`;
  - a Telegram `source` link, which points to the community channel for community orders;
  - `network=mainnet`, `layer=lightning`, `y=lnp2pbot` and `z=order`;
  - an `expiration` taken from its configuration.

  No `bond` or `expires_at` tag is emitted, and the `rating` value combines the maker's local rating, account age and review count. Each signed event is [verified](https://github.com/lnp2pBot/bot/blob/6d91a794d03da0789f88331c28039e95724c3fc9/bot/modules/nostr/events.ts#L80) before the bot [publishes it to its configured relays](https://github.com/lnp2pBot/bot/blob/6d91a794d03da0789f88331c28039e95724c3fc9/bot/modules/nostr/index.ts#L27).

## History

The order proposal that became NIP-69 was added as `xx.md` on 2024-06-27 in commit [f57d559](https://github.com/nostr-protocol/nips/commit/f57d559dc08bf4b59ddefe9416f7569f751f75dd) by Francisco Calderón. On 2024-11-04 it was renamed to `100.md` in [f72a2f6](https://github.com/nostr-protocol/nips/commit/f72a2f69ed93cf442e83bf9e7e16f6c06da40384), then to `69.md` in [bff61dd](https://github.com/nostr-protocol/nips/commit/bff61dd310828758651389940dbcebb7fb9ef0ee). The spec cites an earlier [31001.md](https://github.com/nostr-protocol/nips/blob/8250274a22f4882f621510df0054fd6167c10c9e/31001.md) proposal and n3xB as related work. Prior art outside the NIPs repository is not traced here.

---

**Primary sources:**
- [NIP-69 Specification (pinned)](https://github.com/nostr-protocol/nips/blob/f63c00213fbe494983f2753018d829ea64724d83/69.md)
- [Initial proposal commit f57d559](https://github.com/nostr-protocol/nips/commit/f57d559dc08bf4b59ddefe9416f7569f751f75dd)
- [Rename to 69.md, commit bff61dd](https://github.com/nostr-protocol/nips/commit/bff61dd310828758651389940dbcebb7fb9ef0ee)
- [Mostro Protocol Specification](https://mostro.network/protocol/)
- [Mostro util.rs at 2211a7e](https://github.com/MostroP2P/mostro/blob/2211a7e02bba87416a66026bc653ae1bff886b2a/src/util.rs#L475)
- [RoboSats api/nostr.py at babf62e](https://github.com/RoboSats/robosats/blob/babf62e2238f262182d0bf638496aaa53e286853/api/nostr.py#L36)
- [lnp2pBot events.ts at 6d91a79](https://github.com/lnp2pBot/bot/blob/6d91a794d03da0789f88331c28039e95724c3fc9/bot/modules/nostr/events.ts#L11)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #41: Stable order creation time](/en/newsletters/2026-09-23-newsletter/#nip-69-proposes-a-stable-creation-time-for-trading-orders)
- [Newsletter #49: NIP Deep Dive on public goals and peer-to-peer orders](/en/newsletters/2026-11-18-newsletter/#nip-deep-dive-public-goals-and-peer-to-peer-orders)

**See also:**
- [NIP-40: Expiration Timestamp](/en/topics/nip-40/)
