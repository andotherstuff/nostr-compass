---
title: "NIP-11: Relay Information Document"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-04-22
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11は、relayが自分自身についてのmachine-readableな説明をどう公開するかを定義します。そこには、サポートを主張する機能、制限、operator metadataが含まれます。

## 仕組み

clientは、relayのWebSocket URLに対して`Accept: application/nostr+json`ヘッダー付きのHTTP GET requestを送り、relay情報を取得します。relayは、自身のcapabilityを説明するJSON documentを返します。

## Useful Fields

- **name** - 人間向けのrelay名
- **description** - そのrelayの用途
- **supported_nips** - サポートを主張するNIP一覧
- **limitation** - 最大message size、認証必須かどうかなどの制限
- **pubkey** - 提供されている場合のrelay operator公開鍵
- **contact** - operatorの連絡先

## 信頼モデル

NIP-11は自己申告metadataです。relayが自分について何と言っているかを示すものであり、実トラフィックで証明された内容ではありません。それでもdiscoveryやUXには有用ですが、clientは`supported_nips`を、実際の動作を試さずにground truthとして扱うべきではありません。

この違いはrelay選択で重要です。relayがNIP-50 searchやauthentication要件、大きなmessage limitをadvertiseしていても、本当の答えはclientが実際に接続してそのcode pathを試したときにしか分かりません。

## なぜ重要か

- clientは接続前に必要機能をrelayがサポートしているか確認できる
- discovery serviceはrelay capabilityをindexできる
- userは公開前にrelay policyを確認できる

## 最近の仕様の方向性

仕様は時間とともに絞り込まれてきました。`software`、`version`、privacy policy詳細、retention metadataのような古いoptional fieldsは、長年採用が弱かったため削除されました。その結果、現在のNIP-11 documentは小さく現実的になりましたが、clientはrelayから豊富なpolicy metadataが返ることを期待すべきではありません。

[PR #2318](https://github.com/nostr-protocol/nips/pull/2318)は、relay information documentへ任意の`access_control` objectを追加する提案です。ここにはrelayのgating mode（open、invite、payment、allowlist）と、clientがaccess requestに使えるendpointが入ります。このfieldは助言的なもので、clientやdirectoryがgated relayを公開discovery一覧から除外したり、なぜrelayがwriteを拒否するのかを前もってユーザーへ示したりするためのものです。

## Implementations

- [nostream PR #557](https://github.com/Cameri/nostream/pull/557)により、nostreamは完全なNIP-11 relay info parityへ到達しました。

---

**Primary sources:**
- [NIP-11 Specification](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - relay identity field update
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - cleanup of rarely used fields
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - removal of deprecated fields
- [PR #2318](https://github.com/nostr-protocol/nips/pull/2318) - `access_control` field for gated-relay discovery
- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) - Complete NIP-11 relay info parity

**Mentioned in:**
- [Newsletter #1: NIP Updates](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #13: NIP Updates](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: NIP Updates (`access_control` proposal)](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-66: Relay Discovery and Liveness Monitoring](/ja/topics/nip-66/)
