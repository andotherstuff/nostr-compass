---
title: "NIP-91: フィルターのAND演算子"
date: 2026-03-04
translationOf: /en/topics/nip-91.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - プロトコル
---
NIP-91は、Nostr relay subscriptionにおけるtag arrayへAND filter semanticsを追加します。複数のrelayで実装が現れた後、2026-03-03にmergeされました。

## 問題

Nostrのfilter system（[NIP-01](/ja/topics/nip-01/)）では、単一のtag filter内に複数の値を入れるとOR logicで結合されます。clientが1つのfilterに2つの`p` tag valueを指定すると、relayはどちらかのpubkeyに一致するeventを返します。両方のpubkeyを同時に参照するeventを要求する方法はありませんでした。

そのためclientはrelayから余分なeventまで取得し、ローカルで絞り込む必要がありました。結果として、bandwidth使用量と処理時間が増えていました。

## 仕組み

NIP-91はtag arrayにAND semanticsを導入します。clientが指定したtag valueすべてに一致するeventを必要とする場合、defaultのunion behaviorではなくintersection matchingを選べます。

これは、たとえば「会話の両参加者をtagしたevent」や「2つの必須labelを同時に持つevent」のようなqueryで意味があります。この変更以前、relayはより広いsupersetしか返せず、正確なintersectionはclient側で処理するしかありませんでした。

## なぜ重要か

AND filterはrelay-side indexをより有用にします。clientは、より小さく、すでに関連性の高いresult setをrelayに要求できるため、bandwidthとローカルでの後処理を減らせます。効果が最も大きいのは、mobile clientやtagが多い大規模datasetに対するqueryです。

## 相互運用メモ

merge時点で、nostr-rs-relay、satellite-node、worker-relay、applesauceに動作する実装がありました。このproposalは、番号変更前はNIP-119でした。

relayの採用が進むまでは、clientはsupportが混在する前提で設計するべきです。現実的なfallbackとしては、新しいsemanticsをまだ実装していないrelay向けに、従来どおりclient-side intersection pathを残しておく方法があります。

---

**主要ソース:**
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**言及箇所:**
- [Newsletter #12: NIP Updates](/ja/newsletters/2026-03-04-newsletter/#nip-updates)

**関連項目:**
- [NIP-01: Basic Protocol](/ja/topics/nip-01/)
