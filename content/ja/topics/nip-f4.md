---
title: "NIP-F4: ポッドキャスト"
date: 2026-06-03
draft: false
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4は、Nostrクライアントがポッドキャストのエピソードをどのように参照、表示、そして社会的にやり取りするかを定義します。2年3ヶ月間のドラフトを経て2026-05-28にマージされたこの仕様は、エピソード用のkind 54イベントを使用し、既存のRSSポッドキャストスタックを補完的な層として位置づけて設計されています。

## 仕組み

kind 54のポッドキャストエピソードイベントは、`title`タグ、任意の`image`タグ、`description`タグ、音声ファイル用の1つ以上の`imeta`タグ（URL、mime type、ハッシュ、時間、ビットレート、言語コード、フォールバックURL、NIP-96サービスフラグ）、`t`トピックタグ、そしてフォールバック表示用のNIP-31 `alt`タグを持ちます。

設計の要は`i`タグで、エピソードのRSS GUIDを`podcast:item:guid:<guid>`形式で運びます。これにより以下が可能になります。

- Nostrクライアントがkind 54イベントを表示し、任意のRSS対応ポッドキャストアプリの同じエピソードにリンクする
- RSS対応のNostrクライアントが、ポッドキャスト配信者にホスティングの移行を強いることなく、既存のポッドキャストのエピソードをkind 54イベントとして表示する
- Podcasting 2.0の`<podcast:socialInteract>`と`<podcast:chat>`タグを介したプロトコル間コメントスレッド

## RSSとの共存

PRスレッド上の2年間の議論（Podcasting 2.0の共著者であるDave Jones、Alex Gleason、fiatjaf、Mike Terenzio、Pablo F7z、Jeff Gardnerが参加）は、共存に落ち着きました。Nostrは社会と発見の層を提供し、RSSは音声ファイルとフィードメタデータの真実の源を保持します。NostrはRSSの配信層を複製しません。

これは、RSSを置き換えようとした以前の試み（JSONFeed、RSS 3.0、独自のポッドキャストAPI）とは対照的です。Podcasting 2.0の名前空間は既に、ノートIDでNostrイベントを参照する`<podcast:socialInteract>`をサポートしているため、RSSフィードはNostrにフィード自体をミラーリングさせることなく、付随するNostrのディスカッションスレッドを宣言できます。

## イベント例

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["imeta", "url https://podcast.example.com/audio/ep42.mp3", "m audio/mpeg", "x b2e0a7a82ac9f3f3a71f1d9a78c381d5be9d1cf19dce258765c17c8a76287c93", "duration 4523", "bitrate 192000", "l en ISO-639-1"],
    ["i", "podcast:item:guid:9b2a4c7d-1e3f-4a5b-8c9d-0e1f2a3b4c5d"],
    ["t", "podcasting"],
    ["alt", "Podcast episode: Why RSS Won (43 min)"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

## 実装

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - エピソードリストとインラインプレーヤーを備えた専用のポッドキャスト画面（初の主要クライアント実装、2026年5月）
- [Wavlake](https://wavlake.com) - 最大級のNostrネイティブの音楽・ポッドキャストプラットフォームで、ポッドキャストコンテンツについてkind 54に対応する見込み
- [Fountain](https://fountain.fm) - RSSとNIP-F4を橋渡しする見込みのBitcoinポッドキャストアプリ

## 未解決の論点

マージされた仕様には、実装が収束させるべきいくつかの設計上の問いが残されています。

- クリエイターごとのpubkeyは推奨されますが必須ではありません。そのため、多くのクリエイターを1つのpubkeyで公開するWavlakeのようなプラットフォームも有効なままです
- エピソードごとのコメントとディスカッションは、専用のエピソードコメントkindではなく、NIP-22の汎用スレッドとkind 1のタイムラインノートを使用します
- ポッドキャストごとのメタデータ（ホスト、ネットワーク、言語、ライセンス）は、公開者のkind 0メタデータか、別のkind 54ポッドキャストレベルレコードのいずれかに配置されます

---

**Primary sources:**
- [NIP-F4仕様](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - 2年間の議論を経て2026-05-28にマージされた元の提案
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - 初の主要クライアント実装

**Mentioned in:**
- [Newsletter #25: NIP Updates and Deep Dive](/ja/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ja/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**See also:**
- [NIP-22 (Comments)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Alt tags)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (File Metadata)](/ja/topics/nip-94/)
- [NIP-96 (HTTP File Storage)](/ja/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
