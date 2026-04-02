---
title: "NIP-86: Relay管理API"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relay
  - プロトコル
---

NIP-86はrelay管理のためのJSON-RPCインターフェースを定義し、認可されたクライアントが標準化されたAPIを通じてrelayに管理コマンドを送信できるようにします。relayオペレーターはrelay固有のツールなしにpubkeyのBANや許可、アクセスリストの管理、relay状態のクエリが可能です。

## 仕組み

管理APIはrelay WebSocketエンドポイントと同じURI上でHTTP経由のJSON-RPCライクなリクエストを使用します。リクエストは`application/nostr+json+rpc`コンテンツタイプを使用し、`Authorization`ヘッダーの[NIP-98](/ja/topics/nip-98/)（HTTP認証）署名イベントで認証します。relayはコマンドを実行する前に、リクエストしているpubkeyを管理者リストと照合して検証します。

利用可能なメソッドにはpubkeyのBANと許可、BANされたユーザーのリスト表示、relay設定のクエリが含まれます。標準化されたインターフェースにより、単一のクライアント実装でNIP-86互換のすべてのrelayを管理できます。

## 実装

- [Amethyst](https://github.com/vitorpamplona/amethyst) - NIP-86 relay管理UIを備えたAndroidクライアント（v1.07.0以降）

---

**主要ソース:**
- [NIP-86仕様](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - クライアントサイドNIP-86サポート
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Relay管理ユーザー検索ダイアログ

**掲載号:**
- [Newsletter #16: Amethystがrelay管理を出荷](/ja/newsletters/2026-04-01-newsletter/#amethystがピン留めノートrelay管理request-to-vanishを出荷)

**関連項目:**
- [NIP-11: Relay情報ドキュメント](/ja/topics/nip-11/)
- [NIP-98: HTTP認証](/ja/topics/nip-98/)
- [NIP-42: クライアントからRelayへの認証](/ja/topics/nip-42/)
