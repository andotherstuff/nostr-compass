---
title: "NIP-11: Relay情報ドキュメント"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-03-11
draft: false
categories:
  - リレー
  - プロトコル
---
NIP-11は、relayが自分自身についてのmachine-readableな説明を公開する方法を定義します。そこには、対応していると主張する機能、制限、operator metadataが含まれます。

## 仕組み

clientは、relayのWebSocket URLへ`Accept: application/nostr+json` header付きのHTTP GET requestを送ってrelay情報を取得します。relayは、自分のcapabilityを説明するJSON documentを返します。

## Useful Fields

- **name** - 人間が読めるrelay名
- **description** - relayの用途
- **supported_nips** - 対応していると主張するNIPの一覧
- **limitation** - 最大メッセージサイズや必要なauthなどの制限
- **pubkey** - 提供されていればrelay operatorの公開鍵
- **contact** - operatorの連絡先

## Trust Model

NIP-11は自己申告metadataです。relayがライブの通信で実際に証明したことではなく、relay自身が何を名乗っているかを示します。それでもdiscoveryやUXには役立ちますが、clientは`supported_nips`を挙動テストなしのground truthとして扱うべきではありません。

この区別はrelay選択で重要です。relayがNIP-50 search、認証要件、大きなメッセージ上限を広告していても、本当の答えはclientが実際に接続し、そのcode pathを試して初めて分かります。

## なぜ重要か

- clientは接続前に必要機能の有無を確認できる
- discovery serviceはrelay capabilityをindexできる
- userは公開前にrelay policyを確認できる

## Recent Spec Direction

仕様は時間とともに削ぎ落とされてきました。`software`、`version`、privacy policyの詳細、retention metadataのような古い任意fieldは、長年ほとんど使われなかったため削除されました。その結果、現在のNIP-11 documentは小さく現実的になりましたが、relayから豊富なpolicy metadataが返る前提でclientを作るべきではありません。

---

**主要ソース:**
- [NIP-11 Specification](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - relay identity field update
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - cleanup of rarely used fields
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - removal of deprecated fields

**言及箇所:**
- [Newsletter #1: NIP Updates](/ja/newsletters/2025-12-17-newsletter/#nip-updates)

**関連項目:**
- [NIP-66: Relay Discovery and Liveness Monitoring](/ja/topics/nip-66/)
