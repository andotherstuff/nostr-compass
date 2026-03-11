---
title: "NIP-60: Cashuウォレット"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-03-11
draft: false
categories:
  - ウォレット
  - Ecash
---

NIP-60は、CashuベースのecashウォレットがNostr内でどのように動作するかを定義します。ウォレット情報はRelay上に保存されるため、別々のアカウントを作らなくても、異なるアプリケーション間で使えるポータブルなウォレットを実現できます。

## 仕組み

NIP-60は、Relayに保存される3つの中核イベントタイプと、保留中quote向けの任意の補助イベント1つを使います。

**ウォレットイベント（kind 17375）:** mint URLと支払い受信用秘密鍵を含む、暗号化されたウォレット設定を持つ置換可能イベントです。この鍵はユーザーのNostrアイデンティティ鍵とは別です。

**トークンイベント（kind 7375）:** 未使用のCashu proofを暗号化して保存します。proofが消費されたら、クライアントは古いイベントを削除し、残りのproofを含む新しいイベントを作ります。

**支出履歴（kind 7376）:** 任意の取引記録で、暗号化されたcontentと、作成・破棄されたトークンイベントへの参照を含みます。

**quoteイベント（kind 7374）:** 保留中mint quoteのための任意の暗号化状態です。仕様は、主にローカル状態だけでは足りない場面向けに、expiration tag付きの短命イベントを推奨しています。

## 状態モデル

NIP-60は、送金そのものではなく、ウォレット状態の同期に関する仕様です。ウォレットイベントはどのmintとウォレット鍵を使うかをクライアントに伝え、トークンイベントは未使用proofを含むため、実際の残高状態になります。

この区別は相互運用に重要です。2つのクライアントが同じウォレットを同じように表示できるのは、token rolloverを同じやり方で解釈する場合だけです。つまり、proofを消費し、置き換えproofを公開し、他のクライアントが消費済みproofを残高に含め続けないように、[NIP-09](/ja/topics/nip-09/)で使い終わったトークンイベントを削除する必要があります。

## なぜ重要か

- **使いやすさ** - 新規ユーザーが外部アカウント設定なしでecashを受け取れる
- **相互運用性** - ウォレットデータが異なるNostrアプリ間で追従する
- **プライバシー** - すべてのウォレットデータがユーザー鍵に対して暗号化される
- **proof管理** - ウォレット状態遷移を追跡し、クライアントが同じ残高へ収束できる

## 相互運用メモ

クライアントはまずkind 10019経由でウォレット用Relay情報を探し、専用のウォレットRelay listがなければユーザーの[NIP-65](/ja/topics/nip-65/) Relay listにfallbackします。このfallbackは有用ですが、ウォレットの可搬性が成り立つかどうかは、Relayが実際に暗号化されたウォレットイベントを保存し配信してくれるかに依存します。

仕様はまた、ウォレット秘密鍵をユーザーのNostrアイデンティティ鍵とは分離しておくことを求めます。これにより、受け取り処理をメイン署名鍵から切り離し、1つの鍵を2つの目的に再利用する可能性を下げます。

## ワークフロー

1. クライアントがwallet RelayまたはユーザーのRelay listからウォレット設定を取得する
2. トークンイベントを読み込み、復号して利用可能残高を得る
3. 支出時に新しいトークンイベントを作成し、古いものを削除する
4. 任意の履歴イベントがユーザー参照用に取引を記録する

---

**主要ソース:**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**言及箇所:**
- [Newsletter #3: December Recap](/ja/newsletters/2025-12-31-newsletter/)
- [Newsletter #11: NIP Deep Dive](/ja/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-57: Zaps](/ja/topics/nip-57/)
- [NIP-09: Event Deletion Request](/ja/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/ja/topics/nip-47/)

