---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - DVM
---

NIP-90は、Data Vending Machines（DVMs）を定義します。これは、Nostr上で有料の計算処理をリクエストし、配信するためのプロトコルです。

## 仕組み

customerは`5000-5999`範囲のjob request eventを公開します。各requestには、1つ以上の入力用`i`タグ、job固有設定用の`param`タグ、期待する出力形式を示す`output`タグ、上限価格を示す`bid`、reply先を示すrelay hintを含められます。service providerは、対応する`6000-6999`範囲のresult kindで応答し、kind番号は常にrequestより`1000`高くなります。

resultには、元request、customerのpubkey、任意で`amount`タグやinvoiceが含まれます。providerはさらに、`payment-required`、`processing`、`partial`、`error`、`success`のようなkind `7000` feedback eventも送れます。これによりclientは、最終結果が届く前に進捗を表示できます。

## PaymentとPrivacy

このプロトコルは、business logicを意図的に開いたままにしています。providerは、作業前、sample返却後、または完全結果の配信後に支払いを求められます。この柔軟性は重要です。DVMのjobは、軽いtext変換から高価なGPU処理まで幅広く、providerごとに許容できる支払いリスクが異なるからです。

customerがprivate inputを望む場合、requestは`i`と`param` dataを暗号化した`content`へ移し、providerの`p`タグとともに`encrypted`タグを付けられます。これによりpromptやsource materialはrelay observerから保護されますが、その代わりcustomerはopen market requestではなく特定providerを指名しなければなりません。

## 相互運用メモ

NIP-90は、入力タイプ`job`を持つ`i`タグによるjob chainingをサポートします。これにより、あるresultを次のrequestの入力として流し込めるため、別のorchestration layerを発明しなくても多段処理が可能になります。

provider discovery自体はrequest/response loopの外にあります。仕様は、対応job kindをadvertiseする方法として[NIP-89: Recommended Application Handlers](/ja/topics/nip-89/)を参照しており、clientはrequestを公開する前にそれを使ってvendorを見つけられます。

---

**Primary sources:**
- [NIP-90 Specification](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mentioned in:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/ja/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: Forgesworn toll-booth-dvm](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Agent Reputation Attestations proposal](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-89: Recommended Application Handlers](/ja/topics/nip-89/)
