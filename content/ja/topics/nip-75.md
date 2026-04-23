---
title: "NIP-75: Zap Goals"
date: 2026-04-22
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75は、ユーザーがzapできるfundraising goal eventを定義します。goalはmillisatoshis単位の目標額と、そのgoalに対するzap receiptを集計するrelayの一覧を宣言します。そのgoal eventを参照する任意の[NIP-57](/ja/topics/nip-57/) zapは、進捗に加算されます。

## 仕組み

zap goalは`kind:9041`イベントです。`.content`には人間向けの説明文が入ります。必須タグは`amount`（millisatsでの目標額）と`relays`（zap receiptを集計するrelay list）です。任意タグには、特定時刻で集計を打ち切る`closed_at`、`image`、`summary`があります。また、goalは外部URLやaddressable eventへ結び付ける`r`タグまたは`a`タグを持てるほか、NIP-57 appendix Gから借用したzap-split tagsにより複数のbeneficiary pubkeysも持てます。

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1776500000,
  "kind": 9041,
  "tags": [
    ["relays", "wss://alicerelay.example.com", "wss://bobrelay.example.com"],
    ["amount", "210000"],
    ["image", "<image url>"],
    ["summary", "Nostrasia travel expenses"]
  ],
  "content": "Nostrasia travel expenses",
  "sig": "<128-char hex>"
}
```

clientは、zap requestの中にgoal eventを指す`e`タグを含めることで、goalへzapを結び付けます。goalの進捗は、goal側が指定したrelay上で一致するzap receipt amountを合計したものです。`closed_at`が設定されている場合、そのtimestamp以後に公開されたzap receiptは集計に含まれません。

## Implementations

- [Amethyst](https://github.com/vitorpamplona/amethyst)は、[PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469)でNIP-75をNIP-53 Live Activities画面へ組み込み、live stream header内へgoal progress barとワンタップzapボタンを表示するようになりました。

---

**Primary sources:**
- [NIP-75 Specification](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)

**Mentioned in:**
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive on NIP-57](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-57: Lightning Zaps](/ja/topics/nip-57/)
- [NIP-53: Live Activities](/ja/topics/nip-53/)
