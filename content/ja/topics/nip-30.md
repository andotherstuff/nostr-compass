---
title: "NIP-30: カスタム絵文字"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-30は、Nostrイベントでカスタム絵文字を表示する方法を定義します。カスタム絵文字はevent content内でshortcode（`:shortcode:`）として参照され、各shortcodeを画像URLに対応付ける`emoji`タグで解決されます。

## 仕組み

カスタム絵文字を使うイベントは、content内のshortcode参照と一緒に`emoji`タグを含みます。

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

クライアントは、表示時に`:gleam:`や`:nostrich:`を指定URLのインライン画像へ置き換えます。shortcodeは英数字で、区切りとしてunderscoreを使えます。画像URLは、インライン表示に向いた小さな正方形画像を指すべきです。

## 絵文字セット

カスタム絵文字は、kind 30030のparameterized replaceable eventとして公開される名前付きsetにまとめられます。各setは`d`タグ識別子の下で関連する絵文字をグループ化します。

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

2026-03の更新では、[PR #2247](https://github.com/nostr-protocol/nips/pull/2247)によって、emoji tagに任意のemoji set address参照を入れられるようになりました。ユーザーが絵文字をクリックしたときに、クライアントが元のsetを開いて閲覧やbookmarkに使えるようにするためです。

## 相互運用メモ

カスタム絵文字はpresentation機能であって、transportの保証ではありません。クライアントがNIP-30を理解していない、または画像URLを取得できない場合でも、生の`:shortcode:`テキストは表示されるべきです。このfallbackがあるからこそ、読めるshortcodeが重要になります。

set参照がない限り、`emoji`タグはevent localです。2つの別イベントで`:fire:`が使われていても、同じ画像や同じsetを指していなければ、そこに共有されたグローバルな意味があるとは限りません。クライアントはまず現在のイベントからemoji定義を解決するべきです。

## リアクション

NIP-30のカスタム絵文字はkind 7のreaction eventでも使えます。`content`にshortcodeを入れ、対応する`emoji`タグを持つreactionは、参照先イベント上でカスタム絵文字reactionとして表示されます。

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
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Emoji set address in tags

**言及箇所:**
- [ニュースレター #12: NoorNote v0.5.x](/ja/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [ニュースレター #12: NIPアップデート](/ja/newsletters/2026-03-04-newsletter/#nip-updates)
