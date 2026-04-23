---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60は、Cashuベースのecash walletがNostr内でどう動作するかを定義します。wallet情報はrelay上に保存され、別アカウントなしで異なるapplication間をまたいで使えるportable walletを実現します。

## 仕組み

NIP-60は、relay上に保存される3つの中核event typeと、pending quote向けの1つの任意helper eventを使います。

**Wallet Event（kind 17375）:** mint URLと支払い受信用の秘密鍵を含む、暗号化されたwallet configurationを持つreplaceable event。この鍵は、ユーザーのNostr identity keyとは別です。

**Token Events（kind 7375）:** 未使用のCashu proofを暗号化して保存します。proofが使われたら、clientは古いeventを削除し、残っているproofを含む新eventを作ります。

**Spending History（kind 7376）:** 資金移動を示す任意のtransaction recordで、暗号化contentと、作成または消費されたtoken eventへの参照を持ちます。

**Quote Events（kind 7374）:** pending mint quoteのための任意の暗号化state。仕様は、主にローカルstateだけでは足りないケース向けに、expiration tags付きの短命イベントを推奨しています。

## 状態モデル

NIP-60の焦点は、お金を受け取る行為そのものではなくwallet stateの同期です。wallet eventはclientへどのmintとwallet keyを使うべきかを伝え、token eventsが未使用proofを含むため、実際の残高stateになります。

この違いは相互運用で重要です。2つのclientが同じwalletを表示できるのは、token rolloverを同じように解釈した場合だけです。proofを使い、新しいreplacement proofを公開し、spent token eventを[NIP-09](/ja/topics/nip-09/)経由で削除して、他clientが使用済みproofを残高として数え続けないようにする必要があります。

## なぜ重要か

- **Ease of use** - 新規ユーザーが外部アカウント設定なしで即座にecashを受け取れる
- **Interoperability** - wallet dataが異なるNostr application間でユーザーに追随する
- **Privacy** - すべてのwallet dataがユーザーの鍵で暗号化される
- **Proof management** - wallet state遷移を追跡し、clientが同じ残高へ収束できるようにする

## 相互運用メモ

clientはまずkind 10019を通じてwallet relay情報を探し、専用のwallet relay listがない場合はユーザーの[NIP-65](/ja/topics/nip-65/) relay listへfallbackします。このfallbackは有用ですが、wallet portabilityは依然として、それらrelayが暗号化wallet eventを実際に保存し配信することに依存します。

仕様はまた、wallet private keyをユーザーのNostr identity keyと分離することも求めています。これによりwalletのreceipt handlingが主署名鍵から切り離され、1つの鍵が2つの目的に再利用される危険が減ります。

## Workflow

1. clientはwallet relaysまたはユーザーrelay listからwallet configurationを取得する
2. token eventsを読み出して復号し、利用可能資金を得る
3. 支払い時は新しいtoken eventを作成し、古いものを削除する
4. 任意のhistory eventがtransactionを記録し、ユーザー参照に使われる

---

**Primary sources:**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #11: NIP Deep Dive](/ja/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/)

**See also:**
- [NIP-57: Zaps](/ja/topics/nip-57/)
- [NIP-09: Event Deletion Request](/ja/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/ja/topics/nip-47/)
