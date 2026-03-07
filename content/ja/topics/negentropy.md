---
title: "Negentropy: 集合調整プロトコル"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sync
---

Negentropyは、片方が持ち、もう片方が持たないeventを見つけるためのset-reconciliation protocolです。完全なデータセットを再送せずに差分を特定できます。

## 仕組み

filterに一致するすべてのeventを要求する代わりに、negentropyは2つのソート済み集合を比較し、差分がある範囲だけに絞り込みます。このプロトコルは、コンパクトな範囲要約を交換し、必要な箇所でだけ明示的なID一覧にフォールバックします。

1. **Ordering**: 両者がrecordをtimestamp、次にIDでソートする
2. **Range comparison**: record範囲ごとのfingerprintを交換する
3. **Refinement**: 一致しない範囲を分割し、欠けている実際のIDを特定する

## 重要性

従来のNostr同期はtimestampベースの`since` filterを使いますが、次の理由でeventを取りこぼすことがあります。
- クライアントとrelayのclock drift
- 同じtimestampを持つ複数event
- 順不同で到着するevent

Negentropyは、timestampへの依存ではなく、実際のevent集合を比較することでこの問題を解決します。

## 実運用

- **DM Recovery**: 古いtimestampを持つ欠落direct messageでも検出して取得できる
- **Feed Sync**: relay間でtimelineを完全に同期できる
- **Offline Sync**: 切断期間の後でも効率よく追いつける

実装上の有用な点は、多くのクライアントが通常のsubscriptionをnegentropyで置き換えていないことです。修復経路として使っています。たとえばDamusは通常のDM読み込みを維持しつつ、手動refresh時にnegentropyを追加し、通常フローでは取り逃がすメッセージを回収しました。

## トレードオフ

Negentropyは両端でのサポートが必要で、標準的な`REQ`の利用よりもプロトコル複雑性が増します。実装コストの最小化より正確性を優先する場面で特に有用です。

混在環境では、すべてのrelayがこのプロトコルをサポートするわけではないため、クライアントは穏当なフォールバック動作を持つ必要があります。

---

**主要ソース:**
- [Negentropy Protocol Repository](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**言及箇所:**
- [Newsletter #6: Damus ships negentropy for reliable DM syncing](/en/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**関連項目:**
- [NIP-01: Basic Protocol Flow](/ja/topics/nip-01/)
