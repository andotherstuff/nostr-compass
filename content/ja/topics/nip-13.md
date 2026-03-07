---
title: "NIP-13: プルーフオブワーク"
date: 2026-01-28
translationOf: /en/topics/nip-13.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Spam Prevention
---

NIP-13は、Nostr eventのためのproof-of-work systemを定義します。eventを作る側に計算コストを課し、spam防止の仕組みとして使います。

## 仕組み

proof of workは、指定された数の先頭ゼロbitを持つevent ID（SHA256 hash）を見つけることで示されます。

1. **Difficulty**: 先頭ゼロbit数で測る（例: 20 bit = 平均で2^20回の試行）
2. **Nonce Tag**: eventにはnonce値とtarget difficultyを含む`nonce` tagが入る
3. **Verification**: relayとclientは、そのworkが実行されたことをすばやく検証できる

```json
{
  "tags": [["nonce", "12345", "20"]],
  ...
}
```

## Difficulty Levels

| Bits | Average Attempts | Typical Use |
|------|------------------|-------------|
| 8 | 256 | 最小限のspam抑止 |
| 16 | 65,536 | 軽いfiltering |
| 20 | 1,048,576 | 中程度の保護 |
| 24 | 16,777,216 | 強いspam耐性 |

## なぜ重要か

- **Relay Admission**: relayはevent受理に最低PoWを要求できる
- **Rate Limiting**: account登録のような操作に高いdifficultyを課せる
- **Spam Filtering**: clientはfeedで高PoW eventを優先できる
- **Reputation Bootstrap**: 新規accountはPoWで一定のコミットメントを示せる

有用なのは、コストが非対称である点です。大量の受理可能eventを作るのは送信側にとって高コストになりますが、proofの検証はrelayやclientにとって安価なままです。

## Tradeoffs

- 高性能hardwareを持つユーザーに有利
- energy consumptionの懸念がある
- すべてのspamを防ぐのではなく、コストを上げるだけ

PoWは、spam耐性の重心をaccount identityからcompute availabilityへ移します。permissionlessな環境では有効ですが、正当な新規ユーザーと資金のあるspammerを区別する仕組みにはなりません。

---

**主要ソース:**
- [NIP-13 Specification](https://github.com/nostr-protocol/nips/blob/master/13.md)

**言及箇所:**
- [Newsletter #7: News](/en/newsletters/2026-01-28-newsletter/#news)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
