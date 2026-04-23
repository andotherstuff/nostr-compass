---
title: "NIP-42: Authentication of clients to relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42は、clientがrelayへ認証する方法を定義します。relayはaccess control、abuse防止、有料relay serviceの実装のために認証を要求できます。

## 仕組み

認証フローは、relayがclientへ`AUTH`メッセージを送るところから始まります。このメッセージには、clientが署名しなければならないchallenge文字列が入っています。clientは、そのchallengeを含むkind 22242のauthentication eventを作成し、自分の秘密鍵で署名します。relayは署名とchallengeを検証し、その後accessを許可します。

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

challengeはreplay attackを防ぎます。tag内のrelay URLは、同じ署名済みイベントが別relayへ再利用されるのを防ぎます。

## プロトコルメモ

認証はconnection-scopedです。challengeは接続の間、あるいはrelayが新しいchallengeを送るまで有効です。署名済みイベントはephemeralであり、通常イベントとしてbroadcastしてはいけません。

仕様はmachine-readableなerror prefixも定義しています。`auth-required:`は、clientがまだ認証していないことを意味します。`restricted:`は、認証済みではあるものの、そのpubkeyには要求された操作の権限がまだないことを意味します。

## ユースケース

有料relayは、subscriberを検証してからaccessを与えるためにNIP-42を使います。private relayは、承認済みpubkeyだけにreadやwriteを制限するために使います。また、relayがIPではなく認証済みkeyごとに挙動を追跡できるため、rate limitingも改善します。

[NIP-11](/ja/topics/nip-11/) metadataと組み合わせれば、clientはprotected queryを試す前にrelayがNIP-42をサポートするかどうかを発見できます。実際には対応はまだ均一ではないので、relayがNIP-42をadvertiseしていてもprotected eventの扱いが不正確な場合に備えて、clientはfallback pathを必要とします。

---

**Primary sources:**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**Mentioned in:**
- [Newsletter #6: Relay Information Documents](/ja/newsletters/2026-01-21-newsletter/)
- [Newsletter #9: Marmot Relay Status Testing](/ja/newsletters/2026-02-11-newsletter/)
- [Newsletter #10: Nostr MCP Server](/ja/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Relay AUTH Starts Reaching Real Apps](/en/newsletters/2026-03-11-newsletter/)

**See also:**
- [NIP-11: Relay Information Document](/ja/topics/nip-11/)
- [NIP-50: Search Capability](/ja/topics/nip-50/)
