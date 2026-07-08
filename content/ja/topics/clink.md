---
title: "CLINK: Nostr鍵のための共通Lightningインターフェース"
date: 2026-06-17
draft: false
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
categories:
  - Payments
  - Lightning
---

CLINK（Common Lightning Interface for Nostr Keys）は、送信者が単一のnofferインターフェースを使ってあらゆるNostr鍵の身元に支払いを行えるようにする、提案中の支払いリクエスト形式です。CLINKのnofferには、受信者のNostr公開鍵に加えて、送信者のウォレットがLightning支払い、オンチェーン支払い、あるいは将来の決済プリミティブを構築して受信者に届けるために十分なルーティングメタデータが符号化されています。受信者は身元ごとに1つのnofferを公開し、送信者は受信ウォレットがLightning、オンチェーン、その他のレールのどれで決済するかを知らずに支払います。

## 仕組み

CLINKのnofferは、送信者のウォレットが具体的な支払い指示に復号する構造化された支払いリクエストです。nofferには以下が含まれます。

- 正規の身元ルートとしての受信者のNostr公開鍵
- 1つ以上の支払いエンドポイント（LightningノードURI、オンチェーンアドレス導出ヒント、将来のレール）
- 支払いに関する任意のメタデータ（メモ、金額、有効期限）
- nofferを受信者のNostrの身元に結び付ける受信者の署名

CLINKをサポートする送信ウォレットはnofferを読み取り、対応可能なレールを選択し（Lightning専用ウォレットはLightningエンドポイントに支払い、マルチレールウォレットは最も安価な経路を選択）、支払いを送信します。受信者のウォレットは対応する完了イベントを公開または取得することで受領を確認し、Nostr公開鍵がレールをまたぐ持続的な身元として機能します。

## なぜNostr鍵ベースのインターフェースなのか

LNURLとBOLT-12はLightningの支払いリクエスト形式として既に存在し、Bitcoinにはオンチェーン決済用の広く知られたアドレス形式があります。CLINKはどちらも置き換えるものではありません。送信者が受信者をNostrの身元で指定し、ウォレットに基盤となるレールの選択を任せられるように、Nostr鍵をルートとする層を追加します。Lightningプロバイダを切り替えたり、新しいmintを開設したり、オンチェーンウォレットを移行したりするユーザは、同じNostr鍵でnofferを再公開でき、送信者はアドレス帳を更新する必要がありません。

（すべてのアカウントに対してCLINKのnofferを生成する）Zeus Payにとって、これは送信者がNostr鍵だけであらゆるZeusユーザに支払えることを意味します。Amethystのオンチェーンzapドライバにとって、CLINKの検証状態機械はチェーン上の署名済みnofferがzapリクエストで主張されたNostr pubkeyと一致することを確認し、署名のないオンチェーンzapに対する偽造経路を塞ぎます。

## 実装

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) はCLINKのnofferによる支払いサポートを搭載し、Zeus Payはすべてのアカウントに対してCLINKのnofferを生成するため、送信者はNostr鍵だけであらゆるZeusユーザに支払えます
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) は検証状態機械と再検証ドライバを備えたオンチェーンzap検証用のCLINKドライバを搭載しました（[PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039)、[PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177)、[PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182)）

---

**Primary sources:**
- [Zeus v13.1.0-rc1 リリースノート](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - CLINKのnoffer搭載
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - NIP-BCオンチェーンzap検証状態機械と再検証ドライバ
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - CLINK（Common Lightning Interface for Nostr Keys）の実装
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - CLINKプロトコルDTO用のkotlinx-serializationサポートを追加

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ja/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27: Zeus v13.1.0-rc1 ships CLINK noffers and queue-less NWC](/ja/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**See also:**
- [NIP-57: Zaps](/ja/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/ja/topics/nip-47/)
