---
title: "NIP-39: プロフィール内の外部アイデンティティ"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - アイデンティティ
---

NIP-39は、`i`タグを使ってNostrプロフィールに外部アイデンティティの主張を追加する方法を定義します。これらのタグは、Nostr pubkeyをGitHub、Twitter、Mastodon、Telegramなどの外部プラットフォーム上のアカウントに結び付けます。

## 仕組み

ユーザーはkind 10011イベントに`i`タグとしてアイデンティティ主張を公開します。各タグには`platform:identity`形式の値と、クライアントが主張を検証するためのproof pointerが入ります。

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

クライアントはプラットフォーム名とproof valueからproof URLを再構築し、その外部投稿にユーザーの`npub`が含まれているかを確認します。これにより、中央の検証サービスなしで主張をクライアント間で持ち運べます。

## 証明モデル

重要なのは、NIP-39が2つのアイデンティティの制御を同時に証明する点です。1つはNostr鍵、もう1つは外部アカウントです。どちらかの側の証明が失われると、検証の強さは下がります。gistやtweetが削除されても過去のイベント自体は無効になりませんが、多くのクライアントが依存するライブ証明は失われます。

もう1つ実装上で重要なのは取得戦略です。主張がkind 0の外に出たことで、クライアントはプロフィール詳細画面だけで取得する、フォロー中ユーザーだけ取得する、あるいは取得しないといった選択ができます。これにより、すでに負荷の高いkind 0経路をさらに重くせずに済みます。

## 実装

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - 外部アイデンティティを専用のkind 10011イベントとして公開
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - NIP群にkind 10011の明示的なレジストリ参照を追加

## 現在の状況

現在の仕様では、アイデンティティ主張はkind 0メタデータではなく専用のkind 10011イベントに置かれています。この分離は、kind 0プロフィール取得を軽量化する広い流れの一部として行われました。

---

**主要ソース:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - identity claimsをkind 0から移動
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - kind 10011参照を明示的に追加

**言及箇所:**
- [Newsletter #9: NIP Updates](/ja/newsletters/2026-02-11-newsletter/)
- [Newsletter #12: Amethyst](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: NIP Updates](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-05: ドメイン検証](/ja/topics/nip-05/)

