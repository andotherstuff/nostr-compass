---
title: "NIP-45：Event Counting"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45は、event自体を転送せずにフィルターに一致するeventの数をクライアントがrelayに問い合わせる方法を定義しています。クライアントはREQと同じフィルター構文でCOUNTメッセージを送信し、relayがカウントを返します。

## 動作原理

クライアントはサブスクリプションIDとフィルター付きのCOUNTリクエストを送信します：

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

relayがカウントを返します：

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

数値を表示するためだけに何百、何千ものeventをダウンロードすることを回避します。

## HyperLogLog近似カウント

2026年2月時点で、NIP-45はHyperLogLog（HLL）近似カウントをサポートしています（[PR #1561](https://github.com/nostr-protocol/nips/pull/1561)）。relayはCOUNTレスポンスとともに256バイトのHLLレジスター値を返すことができます：

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLLは根本的な問題を解決します。複数のrelayにまたがるユニークeventのカウントです。relay Aが50リアクション、relay Bが40リアクションを報告した場合、合計は90ではありません。多くのeventが両方のrelayに存在するためです。複数relayからのHLLレジスターは各レジスター位置で最大値を取ることでマージでき、ネットワーク全体で自動的に重複排除されます。

256レジスターでの標準誤差は約5.2%です。HyperLogLog++補正は約200未満のeventでの小さなカーディナリティの精度を向上させます。リアクションeventが2つでも、256バイトのHLLペイロードより多くの帯域幅を消費するため、些細な数を超えるすべてのカウントで効率的です。

仕様はすべてのrelay実装間の相互運用性のためにレジスター数を256に固定しています。

## ユースケース

ソーシャルメトリクス（フォロワー数、リアクション数、リポスト数）が主要な用途です。HLLなしでは、クライアントはデータを中央集権化する形で単一の「信頼できる」relayにカウントを問い合わせるか、帯域幅を浪費してすべてのrelayからすべてのeventをダウンロードしてローカルで重複排除するしかありません。HLLはrelay当たり256バイトのオーバーヘッドで近似的なクロスrelayカウントを提供します。

---

**主要ソース：**
- [NIP-45：Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561：HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**言及先：**
- [ニュースレター #9：NIPディープダイブ](/ja/newsletters/2026-02-11-newsletter/#nipディープダイブnip-45event-countingとhyperloglog)
- [ニュースレター #9：NIPアップデート](/ja/newsletters/2026-02-11-newsletter/#nipアップデート)

**関連項目：**
- [NIP-11：Relay情報ドキュメント](/ja/topics/nip-11/)
