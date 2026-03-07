---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - DVM
---

NIP-90はData Vending Machines（DVMs）を定義し、有料の計算処理をNostr上で依頼し、受け取るためのprotocolです。

## 仕組み

customerは`5000-5999` rangeのjob request eventを公開します。各requestには、1つ以上のinput用`i` tag、job固有設定の`param` tag、期待するformatを示す`output` tag、`bid` ceiling、reply先relay hintを含められます。service providerは、対応する`6000-6999` rangeのresult kindで応答し、kind番号はrequestより常に`1000`大きくなります。

resultには、元のrequest、customer pubkey、optionalな`amount` tagやinvoiceが含まれます。providerは`payment-required`、`processing`、`partial`、`error`、`success`といったkind `7000` feedback eventも送れます。これによりclientは、最終resultが届く前に進捗を表示できます。

## PaymentとPrivacy

protocolはbusiness logicを意図的に開いたままにしています。providerは、作業開始前、sample返却後、または完全なresult配信後に支払いを求められます。この柔軟さは、DVM jobが安価なtext transformから高価なGPU workまで幅広いため重要です。

customerがprivate inputを望む場合、`i`と`param` dataを暗号化した`content`へ移し、providerの`p` tagと`encrypted` tagでmarkできます。これによりpromptやsource materialをrelay observerから守れますが、その代わり特定providerを指名する必要があり、open market requestにはなりません。

## 相互運用メモ

NIP-90は、input type `job`を持つ`i` tagによるjob chainingもサポートします。あるresultを次のrequestの入力へ流せるため、別のorchestration layerを設けなくてもmulti-step flowを組めます。

provider discoveryはrequest/response loop自体の外にあります。仕様は、対応するjob kindをadvertiseする手段として[NIP-89: Recommended Application Handlers](/ja/topics/nip-89/)を参照しています。clientは、それを使ってrequestを出す前にvendorを見つけられます。

---

**主要ソース:**
- [NIP-90 Specification](https://github.com/nostr-protocol/nips/blob/master/90.md)

**言及箇所:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/en/newsletters/2026-02-25-newsletter/#nip-updates)

**関連項目:**
- [NIP-89: Recommended Application Handlers](/ja/topics/nip-89/)
