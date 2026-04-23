---
title: "NIP-57: Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57はzapsを定義します。これは、Lightning paymentをNostr identityやcontentへ結び付ける方法です。zap対応invoiceのrequestと、支払い後にwalletが公開するreceipt eventの両方を標準化しています。

## 仕組み

1. clientは、profile metadataまたは対象イベント上の`zap`タグから受信者のLNURL endpointを見つける
2. clientは、relayではなく受信者のLNURL callbackへ、署名済みkind `9734` zap requestを送る
3. ユーザーがinvoiceを支払う
4. 受信者のwallet serverが、zap requestで指定されたrelayへkind `9735` zap receiptを公開する
5. clientがzapを検証し、表示する

## Zap Request（kind 9734）

zap requestは、支払者と意図した対象を識別する署名済みイベントです。通常は次を含みます。

- `p`タグ - 受信者pubkey
- `e`タグ - zap対象のイベント（任意）
- `amount`タグ - millisatoshis単位の金額
- `relays`タグ - receiptを公開するrelay一覧

addressable contentでは、`e`タグの代わりに、または併用して`a`タグを使えます。任意の`k`タグは対象kindを記録します。

## Zap Receipt（kind 9735）

支払い確認後に、受信者のwallet serverが公開します。内容は次の通りです。

- `description`タグ内に元のzap request
- `bolt11`タグに支払済みinvoice
- `preimage`タグで支払いを証明

clientは、受信者のLNURL `nostrPubkey`、invoice amount、元のzap requestに照らしてreceiptを検証する必要があります。その検証なしでは、receiptは単なる主張にすぎません。

## 信頼モデルとトレードオフ

zapsは、支払いをsocial graph内で可視化できる点で有用ですが、receipt自体は依然として受信者のwallet infrastructureが作成します。仕様自身も、zap receiptは普遍的なpayment proofではないと述べています。最も正確には、「zap requestに結び付いたinvoiceが支払われた」というwallet署名付きの陳述として理解すべきです。

妥当なclientは、receiptをzapとして表示する前に4つを確認すべきです。receiptの署名が受信者のLNURL responseでadvertiseされた`nostrPubkey`に一致すること、`bolt11` invoice amountが埋め込まれたzap request内の`amount`タグと一致すること、invoiceのdescription hashが文字列化されたzap requestへコミットしていること、`preimage`がinvoiceの`payment_hash`へハッシュされることです。これをせずに集計済みzap数を表示するclientは、偽造kind `9735`イベントを出す攻撃者に簡単に騙されます。

## Private zapsとAnonymous zaps

private zapsは、その上に機密性レイヤーを追加します。送信者はzap requestの`content`を受信者向けに暗号化し、外側requestへ`anon`タグを含めることで、relay networkには支払い対象だけを見せつつ、添えたメモは読ませません。anonymous zapではさらに一歩進み、clientがzap request自体のために新しいephemeral keypairを生成するため、receiptは支払いがあったことを示しても、受信者はそのzapを送信者の長期pubkeyへ結び付けられません。

## Zap GoalsとSplits

NIP-57は、[NIP-75](/ja/topics/nip-75/)で定義されるzap-goal systemの土台です。goalは、目標額とreceiptを数えるrelay setを宣言するkind `9041`イベントであり、clientは一致するkind `9735`イベントの検証済み`bolt11` amountを合計して進捗を集計します。

NIP付録で定義されたzap splitsでは、受信者が複数の重み付き`zap`タグを持つkind `0` profileを公開でき、1回のzap paymentを複数のpubkeyへ原子的に分配できます。[Amethyst](https://github.com/vitorpamplona/amethyst)、[Damus](https://github.com/damus-io/damus)、[noStrudel](https://github.com/hzrd149/nostrudel)はsplit-payingをend-to-endで実装しています。

---

**Primary sources:**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mentioned in:**
- [Newsletter #1: News](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/ja/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #9: NIP Updates](/ja/newsletters/2026-02-11-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-47: Nostr Wallet Connect](/ja/topics/nip-47/)
- [NIP-75: Zap Goals](/ja/topics/nip-75/)
- [NIP-53: Live Activities](/ja/topics/nip-53/)
