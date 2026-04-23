---
title: "NIP-01: Basic Protocol"
date: 2025-12-17
translationOf: /en/topics/nip-01.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
---

NIP-01は、Nostrの残りすべてが土台としている基本イベントモデルとrelay protocolを定義します。client、relay、libraryのどれであっても、Nostrを話すなら出発点はここです。

## 仕組み

Nostrにおけるobject typeはイベントだけです。profile、note、reaction、relay list、多くのapplication-specific payloadはすべて、同じ7フィールドのenvelopeを使います。

- **id**: serializeされたイベントのSHA256 hash（unique identifier）
- **pubkey**: 作成者の公開鍵（32-byte hex、secp256k1）
- **created_at**: Unix timestamp
- **kind**: イベント種別を分類する整数
- **tags**: metadata用の配列の配列
- **content**: payload（解釈はkindによる）
- **sig**: 真正性を証明するSchnorr signature

イベントの`id`は、任意の識別子ではなく、serializeされたイベントデータのSHA256 hashです。これは実装上重要です。tag順やtimestampを含め、どれか1つでもフィールドが変われば別イベントになり、新しい署名が必要です。

## Kinds

kindは、relayがイベントをどう保存し、どう扱うかを決めます。

- **Regular events**（1、2、4-44、1000-9999）: 通常保存、全バージョン保持
- **Replaceable events**（0、3、10000-19999）: pubkeyごとに最新のみ保持
- **Ephemeral events**（20000-29999）: 保存せずsubscriberへ転送のみ
- **Addressable events**（30000-39999）: pubkey + kind + `d`タグの組み合わせごとに最新を保持

中核kindには、0（user metadata）、1（text note）、3（follow list）があります。

## Client-Relay Communication

clientはWebSocket接続上でJSON配列を使ってrelayと通信します。

**Client to relay:**
- `["EVENT", <event>]` - イベントを公開する
- `["REQ", <sub-id>, <filter>, ...]` - イベントへsubscribeする
- `["CLOSE", <sub-id>]` - subscriptionを終了する

**Relay to client:**
- `["EVENT", <sub-id>, <event>]` - 一致するイベントを配信する
- `["EOSE", <sub-id>]` - 保存済みイベント終了（以後はリアルタイム配信）
- `["OK", <event-id>, <true|false>, <message>]` - 受理または拒否の応答
- `["NOTICE", <message>]` - 人間向けメッセージ

実際には、上位NIPの多くはtransport layerを変えません。NIP-01の同じ`EVENT`、`REQ`、`CLOSE`メッセージを使いながら、新しいevent kind、tag、解釈ルールを追加します。

## Filters

filterは、`ids`、`authors`、`kinds`、`#e`/`#p`/`#t`、`since`、`until`、`limit`といったフィールドで取得対象のイベントを指定します。1つのfilter内の条件はANDで評価され、1つの`REQ`内に複数filterがある場合はORで評価されます。

## 相互運用メモ

2つの細部が多くの実装バグを生みます。第一に、異なるrelayは異なる履歴部分集合を返し得るため、clientはrelay responseをグローバル順序ではなくeventual consistencyとして扱うべきです。第二に、replaceable eventとaddressable eventでは「最新」がprotocol modelの一部なので、複数relayの結果が食い違うとき、clientはどの有効イベントが最も新しいかを決定するための規則を必要とします。

---

**Primary sources:**
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mentioned in:**
- [Newsletter #1: NIP Deep Dive](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #19: NIP-67 EOSE completeness hint proposal](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-19: Bech32-Encoded Entities](/ja/topics/nip-19/)
- [Kind Registry](/ja/kind-registry/)
