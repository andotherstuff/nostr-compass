---
title: "NIP-58: バッジ"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58は、Nostrのバッジシステムを定義し、発行者がバッジを作成してユーザーに授与し、ユーザーがプロファイルに表示できるようにします。

## 仕組み

### バッジ定義（Kind 30009）

発行者はアドレス可能なイベントとしてバッジ定義を作成します：

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### バッジ授与（Kind 8）

発行者がユーザーにバッジを授与します：

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### バッジ表示（Kind 30008）

ユーザーはプロファイルに表示するバッジを選択します：

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

## ユースケース

- **コミュニティメンバーシップ**：グループやコミュニティへのメンバーシップを証明
- **実績**：貢献やマイルストーンを認識
- **検証**：サードパーティによる証明（従業員、クリエイターなど）
- **アクセス制御**：バッジ所有に基づいてコンテンツや機能をゲート

## 信頼モデル

バッジの価値は完全に発行者の評判に依存します。誰でもバッジを作成できるため、クライアントは以下を行うべきです：
- 発行者情報を目立つように表示
- 信頼できる発行者でフィルタリングできるようにする
- コンテキストなしにバッジを権威あるものとして扱わない

## 関連

- [NIP-51](/ja/topics/nip-51/) - リスト
- [Web of Trust](/ja/topics/web-of-trust/)
