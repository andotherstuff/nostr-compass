---
title: "NIP-52: カレンダーイベント"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52は、Nostr上のカレンダー機能のためのイベントkindを定義し、スケジューリング、RSVP、イベント調整を可能にします。

## イベントKind

### Kind 31922: 日付ベースのカレンダーイベント
特定の時間を指定せずに1日以上にまたがるイベント用：

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-15"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: 時間ベースのカレンダーイベント
特定の開始時間と終了時間を持つイベント用：

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## RSVPサポート

Kind 31925イベントにより、ユーザーはカレンダーイベントに応答できます：

- `accepted` - 参加する
- `declined` - 参加しない
- `tentative` - 参加するかもしれない

## 機能

- **アドレス可能**：重複を作成せずにイベントを更新可能
- **タイムゾーンサポート**：IANA識別子によるタイムゾーンの適切な処理
- **場所**：物理的またはバーチャルのミーティング場所
- **繰り返し**：定期的なイベントのサポート（提案中の拡張）

## 関連

- [NIP-22](/ja/topics/nip-22/) - コメント（カレンダーイベントのディスカッション用）
- [NIP-51](/ja/topics/nip-51/) - リスト（カレンダーコレクション用）
