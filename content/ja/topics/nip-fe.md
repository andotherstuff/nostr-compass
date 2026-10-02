---
title: "NIP-FE提案: HTTP経由のrelayコマンド"
date: 2026-09-30
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Relays
---

Amethystは、Geode relayとQuartzクライアントの作業において、HTTP経由のrelayコマンドに暫定的なNIP-FEという名称を使っています。この名称は割り当て済みのNIPではなく、Nostrのrelay全体で採用されている証拠でもありません。

## トランスポート

クライアントはWebSocket接続を開く代わりに、`REQ`、`COUNT`、`EVENT`のいずれか1つのフレームをrelayのHTTPエンドポイントへPOSTします。レスポンスはrelayのフレームを改行区切りのJSONとしてストリーミングします。クライアントは完了した応答と途中で切れたストリームを区別する必要があり、認証付きのリクエストでは引き続き署名付きのNostr HTTP認可を使います。このトランスポートはコマンドがrelayへ届く方法を変えるものであり、基になるeventの署名や内容を変えるものではありません。

Amethystの[マージ済み実装](https://github.com/vitorpamplona/amethyst/pull/4231)は、Geodeのルート、Quartzのクライアント対応、ボディサイズと同時実行数の制限、そしてフレーミングと認可のテストを追加しています。これはソースレベルでの実装の証拠であり、独立したrelayが同じ提案を実装したことの証明ではありません。

## 名称の衝突

[NIPsリポジトリにある無関係なドラフトのプルリクエスト](https://github.com/nostr-protocol/nips/pull/2488)も**NIP-FE**を使っていますが、こちらは提案中の複数受信者向けエンベロープ上に構築されるプライベートフィードのためのものです。この作業はオープンであり、AmethystのHTTPトランスポートとは別の問題を扱っています。どちらの暫定的な使い方も、この名称が承認済みの仕様に割り当てられたことを示すものではありません。読者は、提案をそのソースと主題によって識別するべきです。

---

**主要ソース:**
- [AmethystのGeodeとQuartzの実装PR](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Amethystリポジトリ](https://github.com/vitorpamplona/amethyst)
- [同じくNIP-FEを使うオープンなプライベートフィードのドラフト](https://github.com/nostr-protocol/nips/pull/2488)

**言及箇所:**
- [Newsletter #42: Amethystのrelayコマンド](/ja/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
