---
title: "NIP-01: 基本プロトコル"
translationOf: /en/topics/nip-01.md
translationDate: 2026-03-07
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01は、Nostrの残りすべてが土台として使う基本event modelとrelay protocolを定義します。クライアント、relay、libraryのどれであっても、Nostrを話すなら出発点はここです。

## 仕組み

eventはNostrにおける唯一のobject typeです。プロフィール、ノート、リアクション、relay list、そして多くのアプリケーション固有payloadは、すべて同じ7フィールドのenvelopeを使います。

- **id**: シリアライズ済みeventのSHA256ハッシュ（一意識別子）
- **pubkey**: 作成者の公開鍵（32-byte hex, secp256k1）
- **created_at**: Unix timestamp
- **kind**: event typeを分類する整数
- **tags**: metadataのための配列の配列
- **content**: payload（解釈はkindに依存）
- **sig**: 真正性を証明するSchnorr署名

eventの`id`は、任意に付けられた識別子ではなく、シリアライズされたevent dataのSHA256ハッシュです。これは実装上重要です。tagの順序やtimestampを含めてどこか1つでも変われば、別のeventになり、新しい署名が必要になります。

## Kind

Kindは、relayがeventをどう保存し、どう扱うかを決めます。

- **Regular events** (1, 2, 4-44, 1000-9999): 通常どおり保存し、全バージョンを保持する
- **Replaceable events** (0, 3, 10000-19999): pubkeyごとに最新だけを保持する
- **Ephemeral events** (20000-29999): 保存せず、subscriberへ転送だけする
- **Addressable events** (30000-39999): pubkey + kind + `d` tagの組み合わせごとに最新を保持する

中核となるkindには、0（user metadata）、1（text note）、3（follow list）があります。

## クライアントとrelayの通信

クライアントは、JSON配列を使ってWebSocket接続上でrelayと通信します。

**クライアントからrelayへ:**
- `["EVENT", <event>]` - eventを公開する
- `["REQ", <sub-id>, <filter>, ...]` - eventを購読する
- `["CLOSE", <sub-id>]` - 購読を終了する

**relayからクライアントへ:**
- `["EVENT", <sub-id>, <event>]` - 一致したeventを配信する
- `["EOSE", <sub-id>]` - 保存済みeventの終端を示す（以後はlive stream）
- `["OK", <event-id>, <true|false>, <message>]` - 受理または拒否の確認
- `["NOTICE", <message>]` - 人間向けメッセージ

実際には、上位のNIPの多くはtransport layerを変えません。NIP-01の`EVENT`、`REQ`、`CLOSE`をそのまま使いながら、新しいevent kind、tag、解釈ルールを定義します。

## フィルター

filterは取得対象のeventを指定します。`ids`、`authors`、`kinds`、`#e`/`#p`/`#t`、`since`、`until`、`limit`といったフィールドを含められます。1つのfilter内ではAND条件が使われ、1つの`REQ`に複数のfilterを入れるとOR条件になります。

## 相互運用メモ

多くの実装バグは2つの点から生まれます。1つは、relayの応答をグローバルに整列したものではなく、eventually consistentなものとして扱う必要がある点です。relayごとに履歴の一部しか返さないことがあります。もう1つは、replaceable eventとaddressable eventでは「最新」がプロトコルモデルの一部なので、複数relayの結果が食い違うときに、どの有効eventを最新と見なすかをクライアントが決定的に選べなければならない点です。

---

**主要ソース:**
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**言及箇所:**
- [Newsletter #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**関連項目:**
- [NIP-19: Bech32-Encoded Entities](/ja/topics/nip-19/)
- [Kind Registry](/ja/kind-registry/)
