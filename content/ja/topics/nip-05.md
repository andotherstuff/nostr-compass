---
title: "NIP-05: ドメイン検証"
date: 2026-02-04
translationOf: /en/topics/nip-05.md
translationDate: 2026-03-11
draft: false
categories:
  - アイデンティティ
  - ディスカバリー
---
NIP-05は、Nostr public keyを`user@example.com`のような人間が読めるinternet identifierに対応付けます。userに対して、clientがHTTPS越しに検証できる、DNSに裏付けられたidentity hintを与えます。

## 仕組み

ユーザーはprofile metadataに`nip05` fieldを追加してidentifierを名乗ります。identifierの形式は`name@domain`です。clientは`https://domain/.well-known/nostr.json`を取得し、そのnameがユーザーのpubkeyへ対応しているかを確認して主張を検証します。

well-known pathにあるJSON fileには、ローカル名をhex pubkeyへ対応付ける`names` objectが入ります。

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

検証に成功すると、clientはnpubの代わりに、あるいはnpubと並べてidentifierを表示できます。verification indicatorを出すclientもあれば、plain textとしてidentifierだけを見せ、信頼判断を読む側に委ねるclientもあります。

## Trust Model

NIP-05は、グローバルなusername registryではありません。証明するのはdomain nameとweb server pathの制御であって、法的な身元や長期的なaccount continuityではありません。domain ownerが後から対応関係を変えれば、過去のstateを保持していないclientは新しい対応関係をそのまま検証します。

そのため、NIP-05はdiscoverabilityとreputationには役立ちますが、多くの人が想像するより強い証明ではありません。良いclientは、これをverified domain controlとして扱うべきであり、人や組織が名乗っている通りの存在だと証明する仕組みとして扱うべきではありません。

## Relay Hints

`nostr.json` fileには、任意で`relays` objectを含められます。これはpubkeyをrelay URLの配列に対応付けるものです。これにより、clientは特定ユーザーのeventをどこで見つけるべきかを発見しやすくなります。

## 相互運用メモ

lowercase requirementは見た目以上に重要です。大文字小文字が混ざったnameやpubkeyは、ある実装では動いても別の実装では失敗します。そのため、現在のclientは`nostr.json`内でlowercaseのnameとlowercaseのhex keyを前提にするべきです。

もう1つの実務上の細部は、特別な`_` nameです。これにより、`_@example.com`や、対応clientでは単に`example.com`のようなbare identifier formをdomainが割り当てられます。ただし、この形式の見せ方はclientごとの差があるため、最も一貫した結果を得やすいのは、明示的な`name@domain` identifierです。

## Implementation Status

主要clientの多くがNIP-05 verificationをサポートしています。
- Damus、Amethyst、Primalはverified identifierを表示する
- 多くのrelay serviceがNIP-05 identifierを機能として提供している
- 無料と有料のNIP-05 providerが多数存在する

---

**主要ソース:**
- [NIP-05 Specification](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - namesとhex keysのlowercase requirement

**言及箇所:**
- [Newsletter #8: NIP Updates](/ja/newsletters/2026-02-04-newsletter/#nip-updates)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
- [NIP-65: Relay List Metadata](/ja/topics/nip-65/)
