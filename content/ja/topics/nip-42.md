---
title: "NIP-42: クライアントからRelayへの認証"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 認証
---

NIP-42は、クライアントがRelayに認証する方法を定義します。Relayは認証を要求することで、アクセス制御、乱用防止、有料Relayサービスの実装を行えます。

## 仕組み

認証フローは、Relayがクライアントに`AUTH`メッセージを送るところから始まります。このメッセージには、クライアントが署名しなければならないchallenge文字列が含まれます。クライアントはchallengeを含むkind 22242の認証イベントを作成し、自分の秘密鍵で署名します。Relayは署名とchallengeを検証し、その後アクセスを許可します。

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

challengeはreplay attackを防ぎます。タグ内のRelay URLは、同じ署名済みイベントが別のRelayで再利用されるのを防ぎます。

## プロトコル上の注意

認証は接続単位です。challengeはその接続の間だけ有効であるか、Relayが新しいchallengeを送るまで有効です。署名済みイベントはephemeralであり、通常イベントとしてブロードキャストしてはいけません。

仕様は機械可読なerror prefixも定義します。`auth-required:`は、クライアントがまだ認証していないことを意味します。`restricted:`は、認証済みではあるものの、そのpubkeyに要求された操作の権限がまだないことを意味します。

## ユースケース

有料Relayは、加入者を確認してからアクセスを与えるためにNIP-42を使います。プライベートRelayは、読み取りや書き込みを承認済みpubkeyに制限するために使います。また、Relayは認証済み鍵ごとに挙動を追跡できるため、IPアドレス単位よりもよいrate limitingが可能になります。

[NIP-11](/ja/topics/nip-11/)のメタデータと組み合わせれば、クライアントは保護された問い合わせを試みる前に、そのRelayがNIP-42をサポートしているかを把握できます。実際にはサポート状況にばらつきがあるため、NIP-42対応を宣言していても保護イベントを正しく扱えないRelayに備えて、クライアントにはfallback pathが必要です。

---

**主要ソース:**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**言及箇所:**
- [Newsletter #6: Relay Information Documents](/ja/newsletters/2026-01-21-newsletter/)
- [Newsletter #9: Marmot Relay Status Testing](/ja/newsletters/2026-02-11-newsletter/)
- [Newsletter #10: Nostr MCP Server](/ja/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Relay AUTH Starts Reaching Real Apps](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-11: Relay情報ドキュメント](/ja/topics/nip-11/)
- [NIP-50: Search Capability](/ja/topics/nip-50/)

