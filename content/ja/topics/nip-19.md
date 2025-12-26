---
title: "NIP-19: Bech32エンコードエンティティ"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19はNostr識別子を共有するための人間に優しいフォーマットを定義します。これらのbech32エンコード文字列は表示と共有に使用されますが、プロトコル自体では使用されません（プロトコルはhexを使用）。

## なぜBech32か？

生のhex鍵はコピー時にエラーが発生しやすく、視覚的に区別しにくいです。Bech32エンコーディングは人間が読めるプレフィックスとチェックサムを追加し、どのタイプのデータを見ているかすぐに分かるようにします。

## 基本フォーマット

これらは生の32バイト値をエンコードします:

- **npub** - 公開鍵（あなたのアイデンティティ、共有しても安全）
- **nsec** - 秘密鍵（秘密に保つ、署名に使用）
- **note** - イベントID（特定のイベントを参照）

例: hexのpubkey `3bf0c63f...`は`npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`になります。

## 共有可能識別子

これらはTLV（Type-Length-Value）エンコーディングを使用してメタデータを含みます:

- **nprofile** - リレーヒント付きプロフィール（クライアントがユーザーを見つけるのに役立つ）
- **nevent** - リレーヒント、作成者pubkey、kindを含むイベント
- **naddr** - アドレス指定可能イベント参照（pubkey + kind + dタグ + リレー）

これらは発見の問題を解決します: 誰かがノートIDを共有したとき、クライアントはどのリレーがそれを持っているかをどうやって知るのでしょうか？識別子にリレーヒントをバンドルすることで、共有リンクがより信頼性の高いものになります。

## 実装に関する注意

- 人間用インターフェースのみにbech32を使用: 表示、コピー/ペースト、QRコード、URL
- プロトコルメッセージ、イベント、NIP-05レスポンスにbech32フォーマットを使用しない
- すべてのプロトコル通信はhexエンコーディングを使用する必要がある
- nevent/nprofile/naddrを生成する際は、発見性向上のためリレーヒントを含める

---

**主要ソース:**
- [NIP-19仕様](https://github.com/nostr-protocol/nips/blob/master/19.md)

**言及箇所:**
- [ニュースレター #1: NIP詳細解説](/ja/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
- [NIP-21: nostr: URIスキーム](https://github.com/nostr-protocol/nips/blob/master/21.md)

