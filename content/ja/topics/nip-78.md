---
title: "NIP-78：アプリ固有データ"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78は、アプリケーションがNostrイベントを使ってユーザーの代わりに任意のデータを保存するための標準イベントkindを定義し、中央サーバーなしでデバイス間の状態同期を可能にします。

## 仕組み

中心となるイベントkindは30078で、パラメータ化された置換可能イベントです。`d`タグはアプリケーション定義の識別子文字列で、ストレージスロットを特定のアプリケーションと目的に限定します。

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

アプリケーションは、一意の`d`タグ（例：`tamagostrich-pet-state`や`amethyst-settings`）と永続化が必要なJSONまたはテキストコンテンツを持つ30078イベントを公開します。30078は置換可能で`d`タグによってスコープされているため、保存された状態の更新は同じ`d`タグを持つ新しいイベントを公開することを意味し、リレーは最新バージョンのみを保持します。

## デバイス間同期

ユーザーの公開鍵とアプリケーションの`d`タグを知っているクライアントは、ユーザーのリレーセットから現在の状態を取得し、任意のデバイスで再構築できます。データはユーザーの鍵ペアで署名されたイベントに存在し、[NIP-65](/ja/topics/nip-65/)リレーリストのリレーに保存されているため、ユーザーがデータを所有します。

## プライベートデータ vs. パブリックデータ

プライベートなアプリケーションデータには、公開前に[NIP-44](/ja/topics/nip-44/)を使用してコンテンツフィールドを暗号化できるため、リレーは鍵の所有者だけが復号できる暗号文のみを保存します。パブリックなアプリケーションデータは、他のクライアントが読み取りと表示ができるよう、暗号化せずに保存できます。

## コンテンツ形式

NIP-78はコンテンツ形式を意図的にオープンにしており、アプリケーションが独自のスキーマを選択します。一般的な慣例は、同じリレーを使用するアプリ間の衝突を防ぐため、`d`タグにアプリケーション名をプレフィックスとして付けることです。

## 実装

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — `tamagostrich-pet-state` kind:30078イベントによるデバイス間ペット状態同期
- [Wisp](https://github.com/barrydeen/wisp-android) — kind:30078ウォレットバックアップおよびデバイス間セキュリティ設定同期；NIP-78著者フィルターを使用して単一REQにマージされたアウトボックス購読
- [NosPress](https://github.com/nostrapps/nospress) — NIP-78イベントに保存されたCMSオーケストレーション状態
- 複数のNostrクライアント設定同期実装（Amethyst、その他）

---

**主要ソース：**
- [NIP-78仕様](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — 本番実装

**掲載：**
- [ニュースレター#22：NIP-78ディープダイブ](/ja/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [ニュースレター#22：Tamagostrich](/ja/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**関連項目：**
- [NIP-51：リスト](/ja/topics/nip-51/)
- [NIP-44：バージョン管理された暗号化](/ja/topics/nip-44/)
- [NIP-65：リレーリストメタデータ](/ja/topics/nip-65/)
