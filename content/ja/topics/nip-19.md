---
title: "NIP-19: Bech32エンコードエンティティ"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19は、Nostr識別子を共有しやすくする人間向けの形式を定義します。これらのbech32エンコード文字列は表示や共有には使われますが、プロトコル本体では使われません。プロトコルで使うのはhexです。

## 仕組み

生のhex鍵はコピー時にミスが起きやすく、見た目だけでは区別もしにくい形式です。Bech32エンコードは人が読めるprefixとchecksumを加えるので、何の種類のデータを見ているのかが分かりやすくなり、多くのコピーエラーも検出できます。

基本形式は単一の32バイト値をエンコードします。

- **npub** - 公開鍵（あなたのアイデンティティ、共有しても安全）
- **nsec** - 秘密鍵（秘密に保つ、署名に使用）
- **note** - イベントID（特定のイベントを参照）

例: hexのpubkey `3bf0c63f...`は`npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`になります。

拡張形式はTLVエンコードを使うので、識別子そのものに加えてlookup hintも持てます。

- **nprofile** - リレーヒント付きプロフィール
- **nevent** - リレーヒント、作成者pubkey、kindを含むイベント
- **naddr** - アドレス指定可能イベント参照（pubkey + kind + dタグ + リレー）

## なぜ重要か

relay hintは権威ある情報ではありませんが、共有されたイベントをクライアントが最初の試行で取得できるかどうかを左右することがよくあります。そのため、コンテンツが受信側の現在のrelay setの外にあるときは、素の`note`や`npub`より`nevent`、`nprofile`、`naddr`のほうが共有形式として有用です。

もう1つ実務上重要なのは安定性です。`note`は1つの不変なevent idを指し、`naddr`は時間とともに置き換えられるアドレス指定可能イベントを指します。長文コンテンツ、カレンダー、リポジトリアナウンスのような対象では、`naddr`が適切なリンク種別になることが多いです。

## 実装メモ

- 人間用インターフェースのみにbech32を使用: 表示、コピー/ペースト、QRコード、URL
- プロトコルメッセージ、イベント、NIP-05レスポンスにbech32フォーマットを使用しない
- すべてのプロトコル通信はhexエンコーディングを使用する必要がある
- nevent/nprofile/naddrを生成する際は、発見性向上のためリレーヒントを含める
- `nsec`はどこでも秘密情報として扱うべきです。クライアントはデフォルトで表示せず、ログに残さず、サポート用エクスポートにも含めるべきではありません

---

**主要ソース:**
- [NIP-19仕様](https://github.com/nostr-protocol/nips/blob/master/19.md)

**言及箇所:**
- [ニュースレター #1: NIP詳細解説](/ja/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [ニュースレター #3: December Recap](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [ニュースレター #3: Notable Code Changes](/ja/newsletters/2025-12-31-newsletter/#damus-ios)
- [ニュースレター #4: Relay Hint Support](/ja/newsletters/2026-01-07-newsletter/)
- [ニュースレター #8: Damus iOS](/ja/newsletters/2026-02-04-newsletter/#damus-ios)
- [ニュースレター #11: notecrumbs](/ja/newsletters/2026-02-25-newsletter/)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
- [NIP-10: Reply Threads](/ja/topics/nip-10/)
