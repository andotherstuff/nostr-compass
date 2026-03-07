---
title: "NIP-87: Ecashミント発見"
date: 2026-01-07
translationOf: /en/topics/nip-87.md
translationDate: 2026-03-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87は、ecash mintであるCashuとFedimintがNostr上で自らをannounceする方法と、userがmintを他人にrecommendする方法を定義します。

## イベント種別

- **kind 38172** - Cashu mint announcement（mint operatorが公開）
- **kind 38173** - Fedimint announcement（mint operatorが公開）
- **kind 38000** - Mint recommendation（userが公開）

## 仕組み

1. **Mint operator**はmintのURL、対応機能、network（mainnet/testnet）を公開します。
2. **User**は信頼するmintについて、optionalなreview付きrecommendationを公開します。
3. **Other user**はfollowしている人たちのrecommendationをqueryして、信頼できるmintを見つけます。

## Cashuミントアナウンス

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

`nuts` tagは、対応するNUTs（CashuのNotation, Usage, and Terminology spec）を列挙します。

`d` tagにはmintのCashu pubkeyを使うべきです。mintが後でmetadataを変えたりannouncementを再公開しても、clientは同じstable identifierで追跡できます。

## ユーザー推薦

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

userは`content` fieldにreviewを書き、特定のmint announcement eventを参照できます。

recommendation eventはparameterized replaceable eventです。これによりuserはreview textを更新したり、endorseをやめたりしても、古いrecommendation eventをいくつも残さずに済みます。

## 信頼モデル

NIP-87は、どのmintが安全かまでは決めません。operatorが公開したmetadataと、userがすでに信頼しているaccountからのsocial recommendationを組み合わせる手段を与えるだけです。

この区別は重要です。mint announcement eventを直接queryすると、noiseやmalicious dataが混ざる可能性があります。仕様でも、social recommendationを経由せずannouncementを直接queryする場合は、spam対策や質の高いrelayを使うようclientへ警告しています。

## 相互運用メモ

CashuとFedimintは接続情報の形が違うため、announcement kindも分かれています。Cashu announcementはmint URLと対応NUTを公開し、Fedimint announcementはinvite codeと対応federation moduleを公開します。両方を扱うwalletは、両方のformatをparseする必要があります。

---

**主要ソース:**
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**言及箇所:**
- [Newsletter #4: Releases](/en/newsletters/2026-01-07-newsletter/#releases)
- [Newsletter #7: Zeus](/en/newsletters/2026-01-28-newsletter/)

**関連項目:**
- [Cashu](/ja/topics/cashu/)
- [NIP-60: Cashu Wallet](/ja/topics/nip-60/)
