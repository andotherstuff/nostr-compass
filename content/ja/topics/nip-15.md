---
title: "NIP-15: Nostrマーケットプレイス"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15は、Nostr上の分散型マーケットプレイスのためのプロトコルを定義し、マーチャントが商品をリストし、バイヤーがBitcoinとLightningを使用して購入できるようにします。

## 仕組み

### マーチャントスタール（Kind 30017）

マーチャントはアドレス可能なイベントとしてスタールを作成します：

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

### 商品（Kind 30018）

商品はスタール内にリストされます：

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

## 購入フロー

1. バイヤーが複数のスタールで商品を閲覧
2. バイヤーがマーチャントに暗号化された注文メッセージを送信
3. マーチャントがLightningインボイスで応答
4. バイヤーがインボイスを支払い
5. マーチャントが商品を発送

## 主な機能

- **分散型**：中央マーケットプレイスオペレーターなし
- **相互運用可能**：任意のNIP-15クライアントが任意のマーチャントを閲覧可能
- **プライベート**：注文はバイヤーとセラー間で暗号化
- **Bitcoinネイティブ**：Lightning支払いが組み込み

## 実装

- **Plebeian Market** - フル機能のNIP-15マーケットプレイス
- **Shopstr** - パーミッションレスBitcoinコマース
- **Amethyst** - ソーシャルフィードに統合された商品リスト

## 関連

- [NIP-44](/ja/topics/nip-44/) - 注文用の暗号化メッセージ
- [NIP-57](/ja/topics/nip-57/) - Lightning Zaps
