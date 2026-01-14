---
title: "NIP-71: Video Events"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71は、Nostr上の動画コンテンツ用のevent kindを定義し、適切なメタデータサポートを備えた動画共有を可能にします。この仕様は、通常の動画eventとアドレス可能な動画eventの両方をカバーしており、後者は2026年1月に追加され、クリエイターが再公開せずに動画メタデータを更新できるようになりました。

## Event Kind

NIP-71は、アスペクト比とアドレス可能性に基づいて2つのカテゴリに分けられた4つのevent kindを定義しています。

通常の動画eventは、横向き（ランドスケープ）動画用のkind 21と縦向き（ポートレート/ショート）動画用のkind 22を使用します。これらは一度公開されると内容が変更できない標準的なNostr eventです。

アドレス可能な動画eventは、横向き動画用のkind 34235と縦向き動画用のkind 34236を使用します。これらは、pubkey、kind、`d`タグの組み合わせで識別されるパラメータ化された置換可能なeventです。同じ識別子を持つ新しいeventを公開すると、以前のバージョンが置き換えられ、メタデータの更新が可能になります。

## 構造

完全なアドレス可能な動画eventには、識別フィールド、メタデータタグ、動画コンテンツ参照が含まれます。

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

`d`タグは、そのkindの動画内で一意の識別子を提供するため、異なる`d`値を使用することで複数のアドレス可能な動画を持つことができます。`title`タグと`summary`タグは、クライアントで表示するための動画タイトルと短い説明を提供します。`url`タグは実際の動画ファイルを指し、`thumb`はプレビュー画像を提供します。`duration`タグは秒単位の長さを指定し、`dim`はオプションで動画の寸法を指定します。

`origin`タグは、他のサービスからコンテンツをインポートする際にソースプラットフォームを追跡します。これにより、YouTube、Vimeo、または他のプラットフォームからNostrホスティングに動画を移行する際に出典が保持されます。

`content`フィールドには、拡張説明、完全なトランスクリプト、または動画に関連するその他のテキストを含めることができます。

## アドレス可能なEventが重要な理由

通常の動画event（kind 21と22）は、一度公開されると変更できません。動画を公開した後にタイトルの誤字に気づいたり、サムネイルを更新したかったり、別の動画サービスに移行したためにホスティングURLを変更する必要がある場合、元のeventを修正することはできません。唯一のオプションは、新しいIDで新しいeventを公開することですが、これにより既存の参照が壊れ、エンゲージメント指標が失われます。

アドレス可能な動画eventは、eventを置換可能にすることでこの問題を解決します。あなたのpubkey、event kind、`d`タグの組み合わせが動画を一意に識別します。同じ識別子で新しいeventを公開すると、relayは古いバージョンを新しいものに置き換えます。動画を取得するクライアントは常に最新のメタデータを取得します。

これは特に以下の場合に価値があります：公開後のメタデータエラーの修正、ブランディングを改善する際のサムネイルの更新、プロバイダーを変更する際の動画ホスティングURLの移行、`origin`タグを通じて出典を保持しながらVineなどの廃止されたプラットフォームからコンテンツをインポートする場合などです。

## 実装

アドレス可能な動画event（kind 34235と34236）は現在、Amethystとnostrvineで実装されています。両方のクライアントは、アドレス可能な動画eventの作成、表示、更新が可能です。

---

**主要ソース：**
- [NIP-71仕様](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - アドレス可能な動画eventアップデート

**言及されている記事：**
- [Newsletter #5：NIPアップデート](/ja/newsletters/2026-01-13-newsletter/#nipアップデート)

**関連項目：**
- [NIP-94: File Metadata](/ja/topics/nip-94/)
