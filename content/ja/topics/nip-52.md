---
title: "NIP-52: Calendar Events"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52は、Nostr上のcalendar events、calendar、RSVPを定義します。これによりclientは、appごとに独自のevent modelを作らずに、時間ベースや日付ベースのイベントを公開する標準的な方法を得られます。

## Event Kinds

### Kind 31922: Date-Based Calendar Event

時刻が重要でない終日イベントや複数日イベントにはkind `31922`を使います。

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

### Kind 31923: Time-Based Calendar Event

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

time-based eventでは、イベントがまたぐ日ごとのday-granularity Unix timestampを入れた`D`タグも1つ以上必要です。このタグがあることで、relayやclientは完全なtimestampを毎回解析せず、日単位でindexできます。

## CalendarとRSVP対応

Kind `31924`はcalendarで、calendar eventのaddressable listです。Kind `31925`はRSVPで、`a`タグで特定のcalendar eventを参照し、必要なら`e`タグで特定revisionも参照します。

Kind `31925`イベントでは、ユーザーは次の応答ができます。

- `accepted` - 参加する
- `declined` - 参加しない
- `tentative` - 参加するかもしれない

RSVPには、出欠に加え予定調整の文脈を与える`fb`値として`free`または`busy`も含められます。

## 実装メモ

- **Addressable**: イベントとcalendarは重複を作らずに更新できる
- **Timezone support**: time-based eventはIANA timezone identifiersを使える
- **Location data**: タグには人間向けlocation、links、geohashを含められる
- **Collaborative requests**: イベント作者はtaggingにより他人のcalendarへ追加を依頼できる

繰り返しイベントは意図的に仕様範囲外です。仕様はrecurrence ruleをclient側へ委ねており、これによってrelay側indexingを単純に保ち、daylight savingの変化や例外処理といった典型的なcalendar edge caseを避けています。

## なぜ重要か

NIP-52は単にmeetingを記述する以上のものです。event定義、calendar membership、attendee responseを別々のevent kindへ分離します。これにより、あるappがイベントを公開し、別のappがcalendarを集約し、さらに別のappがRSVP状態を管理するといったことが、同じbackendを共有しなくても可能になります。

---

**Primary sources:**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**Mentioned in:**
- [Newsletter #7: Notedeck Calendar App Draft](/ja/newsletters/2026-01-28-newsletter/)
- [Newsletter #10: NIP Updates](/ja/newsletters/2026-02-18-newsletter/)
- [Newsletter #10: NIP Deep Dive](/ja/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Calendar by Form* v0.2.0](/en/newsletters/2026-03-11-newsletter/)

**See also:**
- [NIP-22: Comment](/ja/topics/nip-22/)
- [NIP-51: Lists](/ja/topics/nip-51/)
