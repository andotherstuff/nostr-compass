---
title: "NIP-62: Vanishリクエスト"
date: 2026-01-13
translationOf: /en/topics/nip-62.md
translationDate: 2026-03-11
draft: false
categories:
  - プライバシー
  - プロトコル
---

NIP-62は、ユーザーがRelayに自分のcontentの削除を求めるための仕組みとして、vanish requestを定義します。Relayにこれを尊重する義務はありませんが、NIP-62をサポートすれば、ユーザーは公開済みデータに対してより多くの制御を持てるようになり、ネットワーク全体で削除意思を伝える標準的な方法も得られます。

## 仕組み

vanish requestは、削除したいcontentを持つユーザー自身が署名するkind 62イベントです。`e`タグにイベントIDを入れることで特定イベントを対象にできますし、`e`タグを省略すれば、そのpubkeyの全content削除を要求できます。

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

`content`フィールドには、人間が読める削除理由を任意で入れられます。`e`タグのRelay hintは元イベントが公開された場所をRelayに伝えますが、指定されたイベントを持っていなくてもRelayが要求を尊重する場合があります。

## Relayの振る舞い

NIP-62をサポートするRelayは、指定されたイベントをストレージから削除し、subscriberへ配信しないようにするべきです。削除要求そのものは、削除が要求された記録として保持されることがあります。これにより、削除済みイベントが他のRelayから再インポートされるのを防ぎやすくなります。

vanish requestに`e`タグが1つもない場合、Relayはそれをそのpubkeyの全イベントを削除する要求として解釈します。これはより強い操作であり、Relayによってはpubkeyを「vanished」とマークして、以後そのpubkeyのイベントを受け付けも配信もしない、といった扱いをする可能性があります。

RelayがNIP-62をサポートする義務はありません。Nostrネットワークは分散しており、各Relay運営者が自分のデータ保持方針を決めます。ユーザーは、vanish requestを公開しただけであらゆる場所からcontentが消えると考えるべきではありません。

## なぜ重要か

NIP-62は、アドホックなmoderation APIやRelay固有ダッシュボードを超えて、クライアントとRelay運営者に共有の削除シグナルを提供します。ユーザーは署名済み要求を1件公開し、各Relayがそれをどう処理するかを任せられます。

現実的な限界はスコープです。vanish requestの効果は、それを見て、サポートし、尊重するRelayにしか及びません。スクリーンショット、ローカルデータベース、第三者アーカイブ、すでにRelayの外にあるrepostコピーまでは取り消せません。

## プライバシー上の考慮

vanish requestは、最善努力の削除機構であって、プライバシーの保証ではありません。vanish requestを出した後でも、contentのコピーは、NIP-62非対応のRelay、クライアント端末のローカルキャッシュ、第三者アーカイブや検索エンジン、バックアップなど、ネットワークの別の場所に残っている可能性があります。

この要求自体も署名済みNostrイベントなので、あなたの公開記録の一部になります。vanish requestを見た人は、何が削除されたかは見えなくても、あなたが何かを削除したこと自体は知ることができます。

本当に秘匿が必要なcontentには、事後削除に頼るのではなく、[NIP-17](/ja/topics/nip-17/)のような暗号化メッセージングを使う方が適しています。

## 相互運用メモ

NIP-62は[NIP-09](/ja/topics/nip-09/)を補完します。NIP-09はNostr全体で使われる一般的な削除要求イベントであり、NIP-62は特定イベントまたはpubkey全体のcontent集合を対象にできる、より強いvanish志向のシグナルをRelayに与えます。両方をサポートする実装もあり、rust-nostrのdatabase backendは現在、その適用境界に関する設定を公開しています。

---

**主要ソース:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)

**言及箇所:**
- [Newsletter #5: Notable Code Changes](/ja/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: rust-nostr](/ja/newsletters/2026-03-04-newsletter/)

**関連項目:**
- [NIP-09: Event Deletion Request](/ja/topics/nip-09/)
- [NIP-17: プライベートダイレクトメッセージ](/ja/topics/nip-17/)

