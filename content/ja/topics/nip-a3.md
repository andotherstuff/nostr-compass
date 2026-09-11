---
title: "NIP-A3: 支払い先"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3は、Nostrアカウントが複数のネットワークやサービス向けの支払いアドレスを公開するための、移植可能な方法を定義します。置換可能なkind `10133`イベントには、1つ以上の`payto`タグが含まれます。

## 仕組み

各タグは`["payto", "<type>", "<address>"]`という形式です。typeは`bitcoin`、`lightning`、`monero`などの小文字です。クライアントは既知の形式を検証し、ネイティブの支払いURIが存在する場合はそれを表示できます。未知のtypeについては、RFC 8905の`payto:` URIスキームにフォールバックします。

このイベントが示すのは支払い先であり、完了した支払いやNostr zapではありません。どの支払いタイプをサポートするか、アドレスをどのように検証するか、ウォレットに渡す前に支払い先をどれだけ明確に表示するかは、引き続きクライアントが決定します。

## 実装

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041)は、互換性のある支払い先を認識した場合に、オプトイン方式で支払い処理をウォレットへ引き渡します。
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851)は、許可された支払い先のtypeを支払いURIに対応付けます。
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98)は、Moneroの支払い先を検証し、投稿者のリレーに問い合わせます。

---

**一次情報:**
- [NIP-A3仕様](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905: payto URIスキーム](https://www.rfc-editor.org/rfc/rfc8905.html)

**掲載号:**
- [ニュースレター第39号: NIP-A3の支払い先が3つのクライアントに対応](/ja/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**関連項目:**
- [NIP-47: Nostr Wallet Connect](/ja/topics/nip-47/)
