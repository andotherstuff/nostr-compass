---
title: "NIP-02: フォローリスト"
translationOf: /en/topics/nip-02.md
translationDate: 2026-03-07
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-02は、ユーザーのフォローリストを保存するkind 3 eventを定義します。このeventは、ホームフィード、返信通知、多くのrelay選択戦略の土台になります。

## 仕組み

kind 3 eventには、フォローしているpubkeyを列挙する`p` tagが入ります。

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

各`p` tagには4つの位置があります。tag名、フォロー対象のpubkey（hex）、任意のrelay URL hint、任意の"petname"（ローカルなニックネーム）です。relay hintは、そのユーザーのeventをどこで見つけられるかを他のclientに伝えます。petnameを使うと、相手が自分で設定したdisplay nameに頼らず、覚えやすい名前を自分で付けられます。

## Replaceable Behavior

Kind 3はreplaceable range（0、3、10000-19999）に入るため、relayはpubkeyごとに最新バージョンだけを保持します。新しく誰かをフォローすると、clientは新しい相手だけでなく、既存のフォロー全体を含んだ完全なkind 3を公開します。つまり、フォローリストは毎回フルセットで送る必要があり、差分更新はできません。

## なぜ重要か

ホームフィードを組み立てるとき、clientはユーザーのkind 3を取得し、`p` tagのpubkeyをすべて抜き出して、そのauthorたちのkind 1 eventを購読します。

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

relayは一致したnoteを返し、clientがそれを表示します。kind 3に含まれるrelay hintは、フォロー先ごとにどのrelayへ問い合わせればよいかを判断する助けになります。

このeventは、social stateの古さが最初に表面化しやすい場所でもあります。問い合わせたrelay群に最新のkind 3がなければ、実際にはフォローが残っていてもフィードが空に見えることがあります。複数relayの結果をマージするclientは、単一relayだけを信頼するclientより回復しやすい傾向があります。

## Petnames and Identity

petname fieldは、分散型の命名スキームを可能にします。ユーザーがprofileで名乗っている名前をそのまま信じる代わりに、自分自身のラベルを付けられます。たとえばclientは、kind 0 profile由来の"alice"と、あなたが付けたpetnameの"My Sister"を組み合わせて、"alice (My Sister)"のように表示できます。これは、グローバルなusernameでは出せない文脈を与えます。

## 相互運用メモ

kind 3 eventはreplaceableで、しかも常に完全な内容でなければならないので、clientは更新時に未知のtagを保持するべきです。別のclientが自分のclientの知らないtagを加えていた場合、無造作に上書きするとその情報が失われます。

同じ注意はrelay hintとpetnameにも当てはまります。これらは任意fieldですが、書き戻しのときに落としてしまうと、別のclientの体験を静かに悪化させます。安全な更新手順は、最新のkind 3を読み込み、自分が理解しているtagだけを変更し、それ以外は残したまま、完全なeventを再公開することです。

---

**主要ソース:**
- [NIP-02 Specification](https://github.com/nostr-protocol/nips/blob/master/02.md)

**言及箇所:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
- [NIP-10: テキストノートのスレッディング](/ja/topics/nip-10/)
- [NIP-65: Relay List Metadata](/ja/topics/nip-65/)
