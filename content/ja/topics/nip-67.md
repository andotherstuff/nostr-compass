---
title: "NIP-67: EOSE Completeness Hint"
date: 2026-04-22
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67は、既存の`EOSE`メッセージを拡張し、relayがfilterに一致する保存済みイベントをすべて返し終えたかどうかを示す任意の3番目の要素を追加するオープン提案です。狙いは、subscriptionが尽きたのか、それともrelay側の上限で途中で切られたのかをclientが判断するために現在使っている信頼できないheuristicを置き換えることです。

## 問題

`EOSE`は保存済みイベントとリアルタイムイベントの境界を示しますが、完全性についての情報は含みません。実際には、relayはsubscriptionごとに上限を設けており、これはclientの`limit`とは独立していて、一般に300から1000イベント程度です。relay側の上限が300なのに、clientが直近500件のノートを要求すると、300件のイベントと`EOSE`だけを受け取り、それが「全部」なのか「途中で止まった」のかを区別できません。現在の回避策は、イベント数をclientの`limit`と比較して防御的にページ送りすることですが、上限が要求数より低いとイベントを取りこぼし、逆に上限が実際の一致件数の倍数だと余分な往復が発生します。

境界時刻の同着も問題を悪化させます。`until = oldest_created_at`でページ送りすると、relayの時刻比較方法次第で、そのbatch内の最古timestampを共有するイベントを取りこぼすか重複取得する危険があります。

## 変更内容

NIP-67は`EOSE`へ任意の3番目の要素を追加します。

```
["EOSE", "<subscription_id>", "finish"]   // 一致する保存済みイベントをすべて配信済み
["EOSE", "<subscription_id>"]             // 完全性の主張なし（従来形式）
```

仕様化されるのは肯定シグナルだけです。NIP-67対応をadvertiseしているrelayがhintを省略した場合、それはまだ続きがあることを意味します。対応をadvertiseしていないrelayは従来のheuristicへそのまま落ちるため、この変更は現在のすべてのclientとrelayに対して後方互換です。

relayがNIP-67をサポートしていると分かっているclientは、`"finish"`を見た時点でページ送りを止められ、結果件数がちょうどrelay上限に一致する場合でも余分な往復を避けられ、完全性をより正確にユーザーへ示せます。

## ステータス

この提案は、NIPsリポジトリに対する[PR #2317](https://github.com/nostr-protocol/nips/pull/2317)としてオープンです。

---

**Primary sources:**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mentioned in:**
- [Newsletter #19: NIP Updates](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-01: Basic protocol flow](/ja/topics/nip-01/)
- [NIP-11: Relay Information Document](/ja/topics/nip-11/)
