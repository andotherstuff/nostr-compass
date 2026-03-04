---
title: "NIP-30: カスタム絵文字"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-04
draft: false
categories:
  - NIP
  - ソーシャル
---

NIP-30はNostrイベントにおけるカスタム絵文字の表示方法を定義します。カスタム絵文字はイベントコンテンツ内でショートコード（`:shortcode:`）を使って参照され、各ショートコードを画像URLにマッピングする`emoji`タグによって解決されます。

## 仕組み

カスタム絵文字を使用するイベントは、コンテンツ内のショートコード参照とともに`emoji`タグを含みます。

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

クライアントはレンダリングされたコンテンツ内の`:gleam:`と`:nostrich:`を、指定されたURLのインライン画像に置き換えます。ショートコードは英数字（アンダースコア区切りも可）である必要があり、画像URLはインライン表示に適した小さな正方形の画像を指すべきです。

## 絵文字セット

カスタム絵文字はkind 30030のパラメータ化された置換可能イベントとして公開される名前付きセットに整理できます。各セットは`d`タグ識別子の下に関連する絵文字をグループ化します。

```json
{
  "kind": 30030,
  "tags": [
    ["d", "nostr-animals"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"],
    ["emoji", "nostrcat", "https://example.com/nostrcat.png"]
  ]
}
```

2026年3月のアップデート（[PR #2247](https://github.com/nostr-protocol/nips/pull/2247)）により、絵文字タグにオプションの絵文字セットアドレス参照が追加されました。ユーザーが絵文字をクリックした際に、クライアントが元のセットを開いてブラウジングやブックマークができるようになります。

## リアクション

NIP-30のカスタム絵文字はkind 7のリアクションイベントでも機能します。`content`にショートコードを設定し、対応する`emoji`タグを含むリアクションは、参照先のイベント上でカスタム絵文字リアクションとしてレンダリングされます。

```json
{
  "kind": 7,
  "content": ":fire:",
  "tags": [
    ["emoji", "fire", "https://example.com/fire.gif"],
    ["e", "<event-id>"]
  ]
}
```

---

**主要ソース:**
- [NIP-30仕様](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - タグ内の絵文字セットアドレス

**言及箇所:**
- [ニュースレター #12: NoorNote v0.5.x](/ja/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [ニュースレター #12: NIPアップデート](/ja/newsletters/2026-03-04-newsletter/#nipアップデート)
