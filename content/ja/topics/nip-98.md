---
title: "NIP-98: HTTP認証"
date: 2026-03-25
translationOf: /en/topics/nip-98.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 認証
---

NIP-98はNostrイベントを使用したHTTP認証を定義します。パスワード、APIキー、OAuthフローなしに、サーバーが標準HTTPリクエストでクライアントのNostrアイデンティティを検証できるようにします。

## 仕組み

クライアントがHTTPリクエストを認証する必要がある場合、kind 27235イベントを作成します。このイベントはタグにターゲットURLとHTTPメソッドを含み、認証を特定のリクエストに紐づけます。

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1742860800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

クライアントはこのイベントに署名し、base64エンコードして、`Nostr`スキームでHTTP `Authorization`ヘッダーに送信します：

```
Authorization: Nostr <base64-encoded-signed-event>
```

サーバーはイベントをデコードし、署名を検証し、URLとメソッドが実際のリクエストと一致することを確認し、タイムスタンプが最近であることを確認します。すべてのチェックに合格すれば、サーバーはどのNostr pubkeyがリクエストを行ったかを把握できます。

オプションの`payload`タグにはリクエストボディのSHA-256ハッシュが含まれ、認証イベントが異なるコンテンツで再利用されることを防ぎます。タイムスタンプチェック（サーバーは通常、数分以上古いイベントを拒否）はリプレイ攻撃を防止します。

## ユースケース

Blossomサーバーはファイルのアップロードと削除を認証するためにNIP-98を使用し、保存されたメディアを特定のNostrアイデンティティに紐づけます。ファイルホスティングサービスはpubkeyごとのアップロードクォータを適用するために使用します。独自のアカウントシステムを維持せずにNostrユーザーを識別する必要があるHTTP APIは、NIP-98ヘッダーをアイデンティティの証明として受け入れることができます。

---

**主要ソース:**
- [NIP-98仕様](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP認証

**掲載号:**
- [Newsletter #15](/ja/newsletters/2026-03-25-newsletter/)
