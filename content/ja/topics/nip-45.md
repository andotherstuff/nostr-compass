---
title: "NIP-45: Event Counting"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45は、clientが一致するイベント本体を転送せずに、filterに一致するイベント数をrelayへ問い合わせる方法を定義します。NIP-01のfilter syntaxを再利用するため、clientは既存の`REQ`を、同じfilterを使う`COUNT` requestへ変換できることがよくあります。

## 仕組み

clientは、subscription IDとfilterを含む`COUNT` requestを送ります。

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

relayはcountを返します。

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

これにより、単に数字を表示するためだけに何百何千ものイベントをダウンロードせずに済みます。1つの`COUNT` requestに複数filterがある場合、relayは複数`REQ` filterがORされるのと同様に、それらを1つの結果へ集約します。

## HyperLogLog approximate counting

2026年2月時点で、NIP-45はHyperLogLog（HLL）によるapproximate countingをサポートしています（[PR #1561](https://github.com/nostr-protocol/nips/pull/1561)）。relayは結果を近似値として示せ、cross-relay deduplicationのためにcountと一緒に256個のHLL registerも返せます。

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLLは根本的な問題を解決します。複数relayにまたがるdistinct eventの数え上げです。relay Aが50件のreaction、relay Bが40件を返しても、合計は90ではありません。多くのイベントが両方に存在するからです。clientはregister位置ごとに最大値を取ってHLL値をmergeし、生イベントをダウンロードせずにnetwork-wideな推定値を得ます。

仕様は、相互運用性のためregister数を256へ固定しています。これによりpayloadは小さく保たれ、同じ対象filterに対してすべてのrelayが同じregister layoutを計算するので、relay側cacheも実用的になります。

## 相互運用メモ

HLLはtag属性を持つfilterに対してのみ定義されています。register構築に使うoffsetが、filter内で最初に出るtagged valueから導出されるためです。仕様は、reaction、repost、quote、reply、comment、follower countなどのcanonical queryも挙げています。これらはrelayが事前計算やcacheをしやすいcountです。

## なぜ重要か

follower count、reaction count、reply countが主な用途です。NIP-45がなければ、clientは1つのrelayの局所的な見え方を信じるか、一致する全イベントをダウンロードして自力でdeduplicateするしかありません。NIP-45はcountingをrelay内に保ち、HLLによって1つのrelayを権威にせずmulti-relay countを現実的にします。

---

## Implementations

- [nostream](https://github.com/Cameri/nostream)は[PR #522](https://github.com/Cameri/nostream/pull/522)で`COUNT` supportを追加し、clientがイベント本体を取得せずに一致数だけ問い合わせられるようにしました。

---

**Primary sources:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)
- [nostream PR #522](https://github.com/Cameri/nostream/pull/522) - NIP-45 COUNT support

**Mentioned in:**
- [Newsletter #9: NIP Deep Dive](/ja/newsletters/2026-02-11-newsletter/)
- [Newsletter #9: NIP Updates](/ja/newsletters/2026-02-11-newsletter/)
- [Newsletter #12: Five Years of Nostr Februaries](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: nostream NIP-45 support](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-11: Relay Information Document](/ja/topics/nip-11/)
