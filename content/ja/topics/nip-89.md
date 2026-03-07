---
title: "NIP-89: 推奨アプリケーションハンドラー"
date: 2026-01-07
translationOf: /en/topics/nip-89.md
translationDate: 2026-03-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89は、applicationが自分のcapabilityをannounceする方法と、userが特定のevent kindを扱うappをrecommendする方法を定義します。

## イベント種別

- **kind 31990** - Application handler（app developerが公開）
- **kind 31989** - App recommendation（userが公開）

## 仕組み

1. **Applications**が、対応するevent kindとcontentの開き方を説明するhandler eventを公開します。
2. **Users**が、特定のevent kindに使っているappをrecommendします。
3. **Clients**がrecommendationをqueryし、未知のevent typeに対して「open in...」機能を提供します。

## アプリケーションハンドラー

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

`k` tagは対応するevent kindを指定します。URL templateでは、NIP-19でencodingされたentityのplaceholderとして`<bech32>`を使います。

同じhandler eventは、routing patternが同じなら複数のkindをまとめてadvertiseできます。kindごとに別のhandler eventを公開しなくて済むので、app discoveryをコンパクトに保てます。

## ユーザー推薦

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

`d` tagには推薦対象のevent kindが入ります。複数の`a` tagで、platformごとに別のappをrecommendできます。

## Clientタグ

NIP-89は、publishing appが通常のeventに付けられるoptionalな`client` tagも定義します。client nameとhandler eventへのpointerを記録し、他のclientがどのappからnoteが来たかを示したり、より詳しいapplication metadataを引けるようにします。

これはprivacy上の含意があります。publishing software identityを各eventに載せるとusage patternが漏れ得るため、仕様はuserがopt outできるようにすべきだと明言しています。

## ユースケース

- longform article（kind 30023）を表示できるappの発見
- 特定のevent typeをサポートするclientの検索
- cross-clientの「open in...」機能
- encryption supportのためのclient capability検出

## 信頼と安全性の注意点

NIP-89は相互運用性を高めますが、redirect surfaceも作ります。clientが信用していないrelayから任意のhandler announcementを取ると、maliciousまたはmisleadingなappへuserを送ってしまう可能性があります。

そのためrecommendation flowは、まずfollowしている人から始める設計です。socially filtered recommendationは完璧ではありませんが、公開されたすべてのhandlerを同じだけ信頼するよりは安全です。

---

**主要ソース:**
- [NIP-89 Specification](https://github.com/nostr-protocol/nips/blob/master/89.md)

**言及箇所:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #12: Damus](/en/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**関連項目:**
- [NIP-19: Bech32-Encoded Entities](/ja/topics/nip-19/)
