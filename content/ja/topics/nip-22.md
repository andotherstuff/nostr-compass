---
title: "NIP-22: コメント"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-22は、任意のアドレス指定可能なNostrコンテンツにコメントするための標準を定義し、記事、動画、カレンダーイベント、その他のアドレス指定可能イベントでスレッド型の議論を可能にします。

## 仕組み

コメントはplaintextの`content`を持つkind 1111イベントを使います。root scopeを示すタグは大文字で、親返信を示すタグは小文字です。

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Great article!"
}
```

## タグ構造

- **`A` / `E` / `I`** - 議論のroot scope。addressable event、event id、または外部識別子
- **`K`** - そのroot itemに対応するkindまたはroot scope type
- **`P`** - root eventに作成者がいる場合のその作成者
- **`a` / `e` / `i`** - いま返信している直近の親
- **`k`** - 親項目のkindまたはscope type
- **`p`** - 親項目の作成者

トップレベルコメントでは、rootとparentはたいてい同じ対象を指します。コメントへの返信では、rootは固定されたままで、小文字のparent tagだけが返答先の特定コメントを指すように動きます。

## 相互運用メモ

NIP-22コメントはkind 1 replyの汎用置き換えではありません。仕様は、kind 1ノートへの返信にコメントを使ってはならないとはっきり述べています。note同士のスレッドでは、クライアントは引き続き[NIP-10](/ja/topics/nip-10/)を使うべきです。

もう1つ重要なのはscopeです。NIP-22は`I`と`i`タグを通じて、[NIP-73](/ja/topics/nip-73/)で定義されるURLや他の外部識別子のような、noteではないリソースにも議論を結び付けられます。これによりクライアントは、web pageやpodcastなどNostr外の対象にも標準的なコメントスレッドを付けられます。

## 利用例

- 記事のディスカッション
- 動画コメント
- [NIP-52](/ja/topics/nip-52/)カレンダーイベントのディスカッション
- Wikiページのトークページ
- `I`タグで識別される外部リソースへのコメント

---

**主要ソース:**

- [NIP-22仕様](https://github.com/nostr-protocol/nips/blob/master/22.md)

**言及箇所:**

- [ニュースレター #7: Notedeck](/ja/newsletters/2026-01-28-newsletter/#notedeck)
- [ニュースレター #10: AI Agent NIPs Arrive](/ja/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [ニュースレター #12: diVine](/ja/newsletters/2026-03-04-newsletter/#divine)

**関連項目:**
- [NIP-10: Reply Threads](/ja/topics/nip-10/)
- [NIP-52: Calendar Events](/ja/topics/nip-52/)
- [NIP-73: External Content IDs](/ja/topics/nip-73/)
