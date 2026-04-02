---
title: "NIP-5A: 静的ウェブサイト"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-01
draft: false
categories:
  - プロトコル
  - ホスティング
---

NIP-5Aは、Nostrキーペアの下で静的ウェブサイトをホスティングする方法を定義します。サイト作成者はURLパスをSHA256コンテンツハッシュにマッピングする署名済みマニフェストイベントを公開し、ホストサーバーはそのマニフェストを解決してBlossomストレージからサイトのファイルを配信します。

## 仕組み

仕様は2つのイベントkindを使用します。Kind `15128`はルートサイトマニフェストで、pubkeyごとに1つ存在し、そのキーのデフォルトウェブサイトとして機能します。Kind `35128`は`d`タグで識別される名前付きサイトマニフェストで、サブドメインのように機能します。各マニフェストは絶対URLパスを配信されるべきファイルのSHA256ハッシュにマッピングする`path`タグを含みます。

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

ホストサーバーはHTTPリクエストを受信し、サブドメインから著者のpubkeyを抽出し、著者のrelayリストからサイトマニフェストを取得し、リクエストされたパスをコンテンツハッシュに解決し、`server`タグにリストされたBlossomサーバーから一致するBlobをダウンロードします。

## URL解決

ルートサイトはnpubをサブドメインとして使用します。名前付きサイトは生のpubkeyの50文字のbase36エンコーディングに続いて`d`タグの値を1つのDNSラベルに入れます。DNSラベルは63文字に制限されており、base36 pubkeyは常に50文字を使用するため、名前付きサイト識別子は13文字に制限されます。

## 実装

- [nsite](https://github.com/lez/nsite) - NIP-5Aマニフェストを解決しファイルを配信するホストサーバー
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - サイトマニフェストの構築と公開用UI

---

**主要ソース:**
- [NIP-5A仕様](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - オリジナル提案とマージ
- [nsite](https://github.com/lez/nsite) - リファレンスホスト実装
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 公開・管理UI

**掲載号:**
- [Newsletter #16: NIP-5Aのマージ](/ja/newsletters/2026-04-01-newsletter/#nip-5aがマージ-nostrに静的ウェブサイトをもたらす)
- [Newsletter #16: NIPディープダイブ](/ja/newsletters/2026-04-01-newsletter/#nipディープダイブ-nip-5a静的ウェブサイト)

**関連項目:**
- [Blossom](/ja/topics/blossom/)
- [NIP-65: Relayリストメタデータ](/ja/topics/nip-65/)
- [NIP-96: HTTPファイルストレージ](/ja/topics/nip-96/)
