---
title: "NIP-39：プロフィールの外部アイデンティティ"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39は、`i`タグを使用してNostrプロフィールに外部アイデンティティ主張を添付する方法を定義しています。これらのタグは、Nostr pubkeyをGitHub、Twitter、DNSドメインなどの外部プラットフォーム上のアカウントにリンクします。

## 動作原理

ユーザーは`i`タグとしてアイデンティティ主張を公開します。各タグにはプラットフォーム識別子と、外部アカウントがNostr pubkeyにリンクバックするプルーフURLが含まれ、双方向の検証を確立します：

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

クライアントはプルーフURLを取得し、ユーザーのNostr pubkeyが含まれていることを確認して主張を検証します。中央集権的な検証サービスを必要とせずに、アイデンティティ接続のウェブを構築します。

## 最近の変更

2026年2月時点で、[PR #2216](https://github.com/nostr-protocol/nips/pull/2216)がidentityタグをkind 0のユーザーメタデータイベントから専用kind 10011に抽出しました。この移動はvitorpamplonaのkind 0スリム化キャンペーンの一環で、低い採用率が動機です。ほぼどのクライアントも`i`タグ検証を実装していないにもかかわらず、すべてのkind 0取得がそのオーバーヘッドを運んでいました。新しいkind 10011により、関心のあるクライアントがアイデンティティ主張を個別に取得できます。

---

**主要ソース：**
- [NIP-39：External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**言及先：**
- [ニュースレター #9：NIPアップデート](/ja/newsletters/2026-02-11-newsletter/#nipアップデート)

**関連項目：**
- [NIP-05：DNSベースの検証](/ja/topics/nip-05/)
