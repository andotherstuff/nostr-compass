---
title: "NIP-37: ドラフトラップ"
date: 2026-07-01
draft: false
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37は、あらゆる種類の未署名のドラフトイベントのための暗号化された保存イベントを定義します。長文記事、今後のカレンダーイベント、あるいは後で送りたいメッセージを作成中のユーザは、[NIP-44](/ja/topics/nip-44/)で自分自身の鍵に対して暗号化されたkind `31234`イベントとしてドラフトをrelayに保存できます。ドラフトはユーザの鍵を保持する任意のクライアントから復元可能で、同じNIPは、ユーザがプライベートなドラフトを保存したいrelayを指定する別の`kind:10013`リストイベントも定義しています。

## 仕組み

ドラフトラップはkind `31234`のパラメータ化された置き換え可能イベントです。未署名のドラフトイベントはJSON文字列化され、署名者自身の公開鍵に対してNIP-44で暗号化されて`.content`に配置されます。`k`タグはドラフトのkindを宣言し、クライアントがイベントの種類ごとにドラフトをグループ化できるようにします。`d`タグはドラフト識別子を運び、ドラフトが進化するにつれてラップを置き換えられるようにします。また、古いドラフトが自動的に期限切れになるようにNIP-40の`expiration`タグの使用が推奨されます。

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

空の`.content`フィールドは、ドラフトが削除されたことを示します。

## チェックポイント

kind `1234`は、親となる`kind:31234`イベントに属するチェックポイントを定義します。チェックポイントは親のドラフトを指す`a`タグを持ち、クライアントが最新のドラフトと並んでリビジョン履歴を保存できるようにします。

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## プライベートコンテンツ用のrelayリスト（kind 10013）

kind `10013`は、ドラフトラップを含むプライベートコンテンツを保存したいrelayをタグにリストする置き換え可能イベントです。kind `31234`を公開するクライアントは、ユーザのkind `10013`イベントにリストされたrelayに公開すべきです。これにより、公開投稿に使うrelayセット（NIP-65）とプライベートコンテンツの保存に使うrelayセットが分離されるため、ユーザはプライベートなドラフトを少数の信頼できるrelayに固定でき、そのセットを公開のoutboxで晒すことはありません。

## 実装

- [Notedeck](https://github.com/damus-io/notedeck) - プライベート同期用のrelayをkind 10013リストとして保存（2026年6月に追加）

---

**Primary sources:**
- [NIP-37仕様](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Notedeckのプライベート同期relayをkind 10013として保存するコミット](https://github.com/damus-io/notedeck) - Damusチームがデスクトップの同期relay管理のためにこの仕様を採用

**Mentioned in:**
- [Newsletter #29: Notedeck](/ja/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**See also:**
- [NIP-44: Versioned Encryption](/ja/topics/nip-44/)
- [NIP-65: Relay List Metadata](/ja/topics/nip-65/)
