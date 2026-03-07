---
title: "NIP-15: Nostrマーケットプレイス"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15は、Nostr上の分散型marketplaceのためのprotocolを定義します。merchantがproductを出品し、buyerがBitcoinとLightningで購入できるようにします。

## 仕組み

### Merchant Stalls（Kind 30017）

merchantはstallをaddressable eventとして作成します。

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Quality used electronics"],
    ["currency", "sat"],
    ["shipping", "{...shipping options...}"]
  ]
}
```

### Products（Kind 30018）

productはstall内に出品されます。

```json
{
  "kind": 30018,
  "tags": [
    ["d", "product-123"],
    ["stall_id", "my-stall"],
    ["name", "Raspberry Pi 4"],
    ["price", "50000"],
    ["quantity", "5"],
    ["images", "https://..."]
  ]
}
```

## Purchase Flow

1. buyerが複数stallの商品を閲覧する
2. buyerがmerchantへ暗号化された注文messageを送る
3. merchantがLightning invoiceで応答する
4. buyerがinvoiceを支払う
5. merchantが商品を発送する

## なぜ重要か

- **Decentralized**: 中央marketplace operatorがいない
- **Interoperable**: どのNIP-15 clientでもどのmerchantでも閲覧できる
- **Private**: 注文はbuyerとsellerの間で暗号化される
- **Bitcoin-native**: Lightning paymentが組み込まれている

実務上の利点は可搬性です。merchantはcatalog dataを一度公開すればよく、複数のclientがそれを表示できます。1つのmarketplace front endに閉じ込められません。

## Tradeoffs

NIP-15が標準化するのはlistingであって、trustではありません。buyerは、merchantが本物か、inventoryが実在するか、disputeをどう処理するかを自分で判断する必要があります。protocolが提供するのは共通のdata structureとmessage flowであり、reputationとfulfillmentはapplication layerの問題として残ります。

paymentとshippingも、標準化は部分的です。clientはstallとproductを理解できても、invoice、order state、delivery trackingについては独自ロジックが必要になる場合があります。

## Implementation Status

- **Plebeian Market** - フル機能のNIP-15 marketplace
- **Shopstr** - permissionlessなBitcoin commerce
- **Amethyst** - social feedに統合されたproduct listing

---

**主要ソース:**
- [NIP-15 Specification](https://github.com/nostr-protocol/nips/blob/master/15.md)

**言及箇所:**
- [Newsletter #7: January 2024 Protocol Hardening](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**関連項目:**
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
- [NIP-57: Lightning Zaps](/ja/topics/nip-57/)
