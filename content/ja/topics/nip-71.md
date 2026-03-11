---
title: "NIP-71: 動画イベント"
date: 2026-01-13
translationOf: /en/topics/nip-71.md
translationDate: 2026-03-11
draft: false
categories:
  - メディア
  - プロトコル
---

NIP-71は、Nostr上の動画コンテンツ向けイベントkindを定義し、適切なmetadataサポート付きの動画共有を可能にします。仕様は通常の動画イベントとアドレス可能な動画イベントの両方を扱い、後者は2026年1月に追加され、クリエイターが再公開せずに動画metadataを更新できるようになりました。

## イベントkind

NIP-71は、アスペクト比とアドレス可能性に基づいて2つのカテゴリに分かれる4つのイベントkindを定義します。

通常の動画イベントは、横長動画にkind 21、縦長動画やshorts向けにkind 22を使います。これらは公開後にcontentが不変な標準Nostrイベントです。

アドレス可能な動画イベントは、横長動画にkind 34235、縦長動画にkind 34236を使います。これらはpubkey、kind、`d`タグの組み合わせで識別されるパラメータ化置換可能イベントです。同じ識別子で新しいイベントを公開すると前の版が置き換わり、metadata更新が可能になります。

## 構造

完全なアドレス可能動画イベントには、識別情報、metadata tag、動画content参照が含まれます。

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

`d`タグはそのkindの動画群の中で一意な識別子を与えるため、異なる`d`値を使えば複数のアドレス可能動画を持てます。`title`タグと`summary`タグは、クライアント表示用の動画タイトルと短い説明を提供します。`url`タグは実際の動画ファイルを指し、`thumb`はプレビュー画像を提供します。`duration`タグは秒単位の長さを表し、`dim`は任意で動画サイズを表します。

`origin`タグは、他サービスからコンテンツを取り込む際の元プラットフォームを記録します。これにより、YouTube、Vimeo、その他のプラットフォームからNostrホスティングへ移行しても出所を保持できます。

`content`フィールドには、拡張説明、全文transcript、その他その動画に関連する追加テキストを入れられます。

## なぜアドレス可能イベントが重要か

通常の動画イベント（kind 21と22）は、一度公開すると不変です。公開後にタイトルのtypoへ気付いたり、thumbnailを更新したかったり、別の動画サービスへ移行したためにhosting URLを変える必要が出ても、元イベント自体は変更できません。選択肢は新しいIDの新規イベントを出すことだけで、既存参照が壊れ、engagement metricも引き継げません。

アドレス可能動画イベントは、イベントを置換可能にすることでこの問題を解決します。pubkey、イベントkind、`d`タグの組み合わせが動画を一意に識別し、同じ識別子で新しいイベントを公開するとRelayは旧版を新しい版へ置き換えます。動画を取得するクライアントは常に最新metadataを得られます。

これは、公開後のmetadata修正、branding改善に合わせたthumbnail更新、provider変更に伴う動画hosting URL移行、`origin`タグで出所を残しながらVineのような終了したプラットフォームから動画を移植する場面で特に有用です。

別の利点はstable linkingです。クリエイターが見せ方を更新しても、他のイベントは同じアドレス可能動画を参照し続けられます。これは、不変のrepostを量産してコメントや参照が分裂するよりきれいです。

## トレードオフ

置換可能性はmetadata保守を楽にしますが、どれだけ過去状態を保持するかをクライアントが決めなければならないという意味でもあります。公開後にクリエイターがtitleやsummaryを変えると、最新イベントがcanonicalになりますが、古いクライアントは前の版をindexしているかもしれません。

kind 21と22は、不変の公開記録を欲しいアプリケーションでは依然として重要です。NIP-71はすべての動画ワークフローを置換可能モデルへ強制するわけではありません。

## 実装

アドレス可能動画イベント（kind 34235と34236）は、現在Amethystとnostrvineで実装されています。どちらのクライアントでも、アドレス可能動画イベントの作成、表示、更新が可能です。

---

**主要ソース:**
- [NIP-71 Specification](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Addressable video events update

**言及箇所:**
- [Newsletter #5: NIP Updates](/ja/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: NoorNote](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: NIP Updates](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-94: File Metadata](/ja/topics/nip-94/)

