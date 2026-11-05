---
title: "NIP-31: 未知のイベントkindの扱い"
date: 2026-11-04
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
---

> **ステータスに関する注意:** 現行の[NIP-31仕様](https://github.com/nostr-protocol/nips/blob/master/31.md)は、自らを「不必要に肥大化している」として`unrecommended`と位置づけており、そのステータス行にはdraft、unrecommended、optionalと記されています。この慣例を用いたイベントはすでにリレーに保存されているため、このページではクライアントがそれらをどう読むかを説明します。新しいプロトコルにNIP-31を推奨するものではありません。

NIP-31はトップレベルの`alt`タグを定義します。このタグは、通常のテキストノートとして読まれることを想定していないカスタムイベントkindのための、短いプレーンテキストの要約を保持します。

## 仕組み {#how-it-works}

カスタムkindのイベントの作成者は、人が読めるラベルを入れた`alt`タグを追加します。kind 1を中心に作られたクライアントは、認識できないすべてのkindを購読する必要はありません。それでも、そうしたクライアントのユーザーはノートがそのようなイベントを参照したときにそれに出会うことがあり、クライアントがそのkindを実装していなくても、ラベルがある程度の文脈を与えます。

タグの断片であり、完全なイベントではありません:

```
["alt", "<short plaintext summary>"]
```

人が読めるラベルが担うのは表示だけです。投票したり、ウォレットリクエストに応じたり、そのkind本来のその他のアクションを実行したりすることはできません。より豊かなやり取りについて、仕様は[NIP-89: 推奨アプリケーションハンドラー](/ja/topics/nip-89/)を参照するよう示しています。

## 実装 {#implementations}

noStrudelの[コミット7c68acf時点の未知イベントカード](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)では、最初の`alt`タグがトリムされてメインラベルとなり、任意で`Using <client>`の行が付きます。値が欠けているか空白の場合は`Unknown event (kind ...)`となり、コンテンツは最大3行までそれ単独で表示されます。同じコンポーネントは、NIP-89のハンドラーテンプレートを通じて`client`タグを解決します。共有可能なアドレスが存在する場合はOpenボタンを表示し、有効なハンドラーリンクが解決された場合は`Open in <client>`を表示します。説明とアプリへの振り分けは別々のコントロールです。

Amethystの[コミット553f761時点のUnknownEventDigest.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170)は、散文と分類したコンテンツを優先し、`alt`にフォールバックします。そのパーサーは値をトリムし、空白でない最初の`alt`を採用します。その結果、最初の`alt`が空白のイベントは、noStrudelとは異なるラベルになる場合があります。どちらの記述も、それぞれのコミット時点のソースコードを反映したものです。いずれもリリース版の挙動を確認したものではありません。

## 制限 {#limits}

- `alt`はタグであるため、[NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)で定義されるイベントIDと署名の対象に含まれます。有効な署名は、作成者がそのラベルを公開したことを示します。ラベルが正確であることは示さないため、要約が誤解を招く可能性があります。
- タグは公開されます。暗号化されたコンテンツを持つイベントの`alt`は、その要約を露出させ、コンテンツが隠している内容を明かしてしまう可能性があります。
- 上記の2つの性質は、NIP-01のイベントエンベロープに由来します。NIP-31自体の本文は、これらを要件として述べていません。
- トップレベルの`alt`タグは、`imeta`内にある画像説明用の`alt`フィールドとは別物であり、レンダラーはそれぞれを別々にパースします。

---

**一次資料:**
- [NIP-31仕様](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [コミット7c68acf時点のnoStrudel embedded-unknown.tsx](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [コミット553f761時点のAmethyst UnknownEventDigest.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**言及箇所:**
- [Nostr Compass #47: NIP詳解](/ja/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**関連項目:**
- [NIP-89: 推奨アプリケーションハンドラー](/ja/topics/nip-89/)
- [NIP-73: 外部コンテンツID](/ja/topics/nip-73/)
- [NIP-01: 基本プロトコルフローの説明](/ja/topics/nip-01/)
