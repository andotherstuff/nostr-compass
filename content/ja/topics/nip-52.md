---
title: "NIP-52: カレンダーイベント"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - カレンダー
  - イベント
---

NIP-52は、Nostr上のカレンダーイベント、カレンダー、RSVPを定義します。アプリごとに独自のイベントモデルを発明しなくても、時刻ベースまたは日付ベースのイベントを公開する標準的な方法をクライアントに与えます。

## イベントkind

### Kind 31922: 日付ベースのカレンダーイベント

時刻が重要でない終日イベントや複数日にまたがるイベントにはkind `31922`を使います。

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-16"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: 時刻ベースのカレンダーイベント

正確な開始時刻と終了時刻を持つイベントにはkind `31923`を使います。

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["D", "19755"],
    ["start_tzid", "America/New_York"]
  ]
}
```

時刻ベースのイベントでは、1つ以上の`D`タグも必要です。各`D`タグには、そのイベントがまたぐ日のday-granularity Unix timestampが入ります。このタグは、Relayとクライアントが完全なtimestampを毎回解析しなくても日単位でindexできるように存在します。

## カレンダーとRSVPサポート

kind `31924`はカレンダーであり、アドレス可能なカレンダーイベント一覧です。kind `31925`はRSVPで、`a`タグで特定のカレンダーイベントを参照し、必要なら`e`タグで特定revisionも参照します。

kind `31925`イベントでは、ユーザーは次の応答を返せます。

- `accepted` - 参加する
- `declined` - 参加しない
- `tentative` - たぶん参加する

RSVPには`free`または`busy`の`fb`値も含められ、出欠状態に加えてスケジュール上の文脈も伝えられます。

## 実装メモ

- **アドレス可能**: イベントとカレンダーを重複なく更新できる
- **タイムゾーンサポート**: 時刻ベースイベントはIANA timezone identifierを使える
- **位置情報**: タグには人が読める場所、リンク、geohashを含められる
- **協調的リクエスト**: イベント著者は相手のカレンダーをtag付けして掲載を依頼できる

定期イベントは意図的にスコープ外です。仕様はrecurrence ruleをクライアント側へ押し出しており、これによりRelay側indexを単純に保ち、夏時間変更や例外処理で起こりがちなカレンダー特有の厄介さを避けています。

## なぜ重要か

NIP-52は単に会議を記述するだけではありません。イベント定義、カレンダー所属、参加者応答を別々のイベントkindに分離します。そのため、あるアプリがイベントを公開し、別のアプリがカレンダーを集約し、さらに別のアプリがRSVP状態を管理するといった分業が、同じbackendを共有せずに可能になります。

---

**主要ソース:**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**言及箇所:**
- [Newsletter #7: Notedeck Calendar App Draft](/ja/newsletters/2026-01-28-newsletter/)
- [Newsletter #10: NIP Updates](/ja/newsletters/2026-02-18-newsletter/)
- [Newsletter #10: NIP Deep Dive](/ja/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Calendar by Form* v0.2.0](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-22: Comment](/ja/topics/nip-22/)
- [NIP-51: Lists](/ja/topics/nip-51/)

