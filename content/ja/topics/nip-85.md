---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85はTrusted Assertionsを定義し、計算コストの高い処理をtrusted service providerへ委任し、その結果を署名済みNostr eventとして公開する仕組みです。

## 仕組み

Web of Trust score、engagement metric、そのほかの計算値は、多数のrelayをcrawlし、大量のeventを処理する必要があります。これはmobile deviceでは現実的ではありません。NIP-85では、specialized providerがこうした計算を行い、clientがqueryできる結果を公開します。

Trusted Assertionsはaddressable eventです。`d` tagがscore対象を識別し、event kindが対象の種類を示します。pubkeyは30382、通常のeventは30383、addressable eventは30384、NIP-73 identifierは30385です。

userはkind 10040を通じて信頼するproviderを宣言します。provider listはtagに公開で載せることも、[NIP-44](/ja/topics/nip-44/)でevent contentへ暗号化して入れることもできます。信頼入力を公開したくないuserには、この違いが重要です。

## なぜ重要か

NIP-85の重要な点は、algorithmではなくoutputを標準化することです。2つのproviderが同じpubkeyに対して`rank` tagを公開していても、使うWeb of Trust formula、mute処理、relay coverage、anti-spam heuristicは違って構いません。計算方法が違っても、結果形式がそろっていればclient間の相互運用性は保てます。

これは、1つのcanonical ranking serviceが現れる前提を置かないNostrに合っています。userは、誰のassertionを信頼するかを自分で決めます。

## 信頼モデル

service providerは、自分のassertion eventに自分で署名しなければなりません。仕様では、algorithmごと、またはuser固有viewpointごとに別のservice keyを使うことも勧めています。これにより、無関係なranking systemを1つの不透明なidentityへまとめずに済みます。

trustはそれでもローカルに残ります。署名済みoutputは、どのproviderがscoreを公開したかを示すだけで、そのscore自体の正しさまでは証明しません。clientは、どのprovider keyを使うか、どのrelayから取得するか、assertionが衝突したときにどう扱うかというpolicyを持つ必要があります。

## 相互運用メモ

NIP-85は人やpostだけにとどまりません。kind 30385により、providerはbook、website、hashtag、locationのようなNIP-73 external identifierもscoreできます。これにより、Nostr外のsubjectについても、相互運用できるreputation dataやengagement dataを載せる道が開けます。

---

**主要ソース:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - Service provider discoverability guidance

**言及箇所:**
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 Service Provider Discoverability](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: Protocol Recap](/en/newsletters/2026-03-04-newsletter/)

**関連項目:**
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
- [NIP-73: External Content IDs](/ja/topics/nip-73/)
- [Web of Trust](/ja/topics/web-of-trust/)
