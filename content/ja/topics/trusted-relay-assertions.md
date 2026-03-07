---
title: "Trusted Relay Assertions"
date: 2026-01-21
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertionsは、relayについて署名付きの第三者評価をNostr上で公開し、clientがself-reported metadataだけではない文脈をもとにrelayを選べるようにする考え方です。現時点で標準化されているbuilding blockは[NIP-85: Trusted Assertions](/ja/topics/nip-85/)で、userがproviderをどう信頼し、providerが署名済み計算結果をどう公開するかを定義しています。

## 仕組み

relay選定には3つの層があります。[NIP-11: Relay Information Document](/ja/topics/nip-11/)はrelayが自分について何を言うかを扱います。[NIP-66: Relay Discovery and Liveness Monitoring](/ja/topics/nip-66/)は可用性やlatencyのように観測できる値を扱います。Trusted Relay Assertionsは、その先にある「第三者がそのdataから何を結論づけるか」と「clientがその結論を信頼するか」を埋めようとするものです。

より広いNIP-85モデルでは、userがkind `10040` eventでtrusted providerを指定し、providerが署名済みのaddressable assertion eventを公開します。relay-scoring appを作るには、さらに2つの合意が必要です。relayをsubjectとしてどう識別するか、そしてscoreと裏付けをどのresult tagで表すかです。

ここで大事なのは、transportとtrust delegationは標準化されていても、relay固有のscoring modelはまだapplication patternだという点です。何をもってtrustworthy relayとみなすかについて、providerごとに正当な不一致があり得ます。

## 信頼モデル

relay trust scoreは客観的事実ではありません。あるproviderはuptimeとwrite throughputを重視し、別のproviderは法域、moderation policy、operator identityを重視し、さらに別のproviderは監視耐性を最優先するかもしれません。役に立つclientは、scoreそのものだけでなく、誰がそのscoreを出したかを示す必要があります。

ここで[Web of Trust](/ja/topics/web-of-trust/)も関わってきます。clientがすでに特定の人やserviceを信頼しているなら、そのsocial neighborhoodから来たrelay評価を優先できます。単一のglobal rankingがあるふりをしなくて済みます。

## なぜ重要か

[NIP-46](/ja/topics/nip-46/) remote signer、wallet connection、未知のrelayを提示するappでは、第三者によるrelay評価がdefaultへの盲信を減らせます。[NIP-65](/ja/topics/nip-65/) relay listと組み合わせれば、clientは「どのrelayを使うか」と「どのrelayをこの用途で信頼するか」を分けて考えられます。

ただし正確さに関する注意点もあります。2026-01のnewsletterではrelay trust scoringが専用proposalのように扱われましたが、NIPs repositoryでmerge済みなのは、より広い[NIP-85: Trusted Assertions](/ja/topics/nip-85/) formatです。relay scoringはその上に載るuse caseであり、独立した完成済みwire formatではありません。

---

**主要ソース:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534)

**言及箇所:**
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-28-newsletter/#nip-updates)

**関連項目:**
- [NIP-11: Relay Information Document](/ja/topics/nip-11/)
- [NIP-66: Relay Discovery and Liveness Monitoring](/ja/topics/nip-66/)
- [NIP-85: Trusted Assertions](/ja/topics/nip-85/)
- [Web of Trust](/ja/topics/web-of-trust/)
