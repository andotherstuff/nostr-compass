---
title: "NIP-27 (テキストノート参照)"
date: 2026-02-04
description: "NIP-27はnostr: URIスキームを使用してノートコンテンツ内でプロファイル、ノート、その他のエンティティを参照する方法を定義します。"
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-27は、テキストノートのcontent内にNostrエンティティへの参照を埋め込む方法を定義します。参照には`nostr:` URI schemeの後ろにbech32エンコード済み識別子（npub、note、nevent、nprofile、naddr）を置きます。

## 仕組み

別のユーザーにメンションしたり、別のイベントを参照するノートを作成する際、参照はコンテンツに直接埋め込まれます：

```
Check out this post by nostr:npub1... about nostr:note1...
```

クライアントはこれらの参照を解釈して、たいていはクリック可能なリンクやインラインのprofile cardとして表示します。参照対象はindexingやnotificationのためにevent tagへ反映されることもありますが、仕様はそれを必須にはしていません。

このNIPはハッシュタグの解析もカバーしています。`#`で始まるタグは抽出され、検索可能性のためにイベントの`t`タグに追加されます。

## 参照タイプ

- `nostr:npub1...` - ユーザープロファイルへの参照
- `nostr:note1...` - 特定のノートイベントへの参照
- `nostr:nevent1...` - リレーヒント付きイベントへの参照
- `nostr:nprofile1...` - リレーヒント付きプロファイルへの参照
- `nostr:naddr1...` - アドレス可能イベントへの参照

## なぜ重要か

NIP-27は、人が読むものとクライアントが保存するものを分けます。ユーザーはリッチコンポーザーで`@name`と入力しても、公開されるeventの`content`には安定した`nostr:nprofile...`参照を入れられます。これにより、参照方法が特定アプリのmention構文に依存せず、クライアント間で持ち運びやすくなります。

もう1つの実務上の利点は復元性です。テキスト内に生の`nostr:nevent...`や`nostr:naddr...`が埋め込まれていれば、別のクライアントが元のローカル表示を見たことがなくても、対象を再構築するための情報を十分に持てます。

## 相互運用メモ

- content内では[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)形式、つまり`nostr:<bech32-id>`を使います
- mention notificationやより強いevent indexingが必要な場合にだけ`p`タグや`q`タグを追加します
- すべてのinline referenceをreply relationに変換すべきだと決めつけてはいけません。この判断はクライアントに委ねられています

---

**主要ソース:**

- [NIP-27仕様](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32エンコードエンティティ)](/ja/topics/nip-19/) - 参照で使用されるエンコード形式を定義

**言及箇所:**

- [Newsletter #8 (2026-02-04)](/ja/newsletters/2026-02-04-newsletter/) - nostr-toolsの改行後のハッシュタグ解析の修正

**関連項目:**
- [NIP-18: リポスト](/ja/topics/nip-18/)
- [NIP-19: Bech32エンコードエンティティ](/ja/topics/nip-19/)
