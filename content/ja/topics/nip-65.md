---
title: "NIP-65: Relay List Metadata"
date: 2026-01-13
translationOf: /en/topics/nip-65.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65は、ユーザーがどのrelayをreadとwriteに好むかをadvertiseするkind 10002イベントを定義します。このmetadataは、他ユーザーやclientが分散relay network上であなたのcontentを見つける助けとなり、負荷分散とcensorship resistanceを高める「outbox model」を実現します。

## 構造

relay listはreplaceable event（kind 10002）で、ユーザーが公開したいrelayごとに`r`タグを含みます。このイベントは同じpubkeyからの以前のrelay listを置き換えます。

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

各`r`タグには、relayのWebSocket URLと、そのrelayに対するユーザーの関わり方を示す任意markerが入ります。`read` markerはユーザーがそのrelayからイベントを受信することを意味し、他者はそこへ公開すればそのユーザーへ届きます。`write` markerは、ユーザーがそのrelayへ公開することを意味し、他者はそこをsubscribeすればそのユーザーのcontentを見られます。marker省略はreadとwriteの両方を意味します。

relay list eventの`content`フィールドは空です。

## Outbox model

NIP-65は、「outbox model」と呼ばれる分散型content distribution patternを可能にします。全員が同じcentral relayへ公開し、同じcentral relayから読むのではなく、ユーザーは自分の好むrelayへ公開し、clientは各ユーザーのcontentがどこにあるかを動的に発見します。

AliceがBobの投稿を見たいとき、Aliceのclientはまず、どこかのrelayからBobのkind 10002イベントを取得します。そしてBobが`write`に指定したrelayを取り出します。そこがBobの公開先だからです。Aliceのclientは、それらrelayでBobのイベントをsubscribeします。逆にAliceがBobへdirect messageを送りたい場合、clientはBobの`read` relayを探し、そこへメッセージを公開します。

outbox modelに従うclientは、followしているユーザーのNIP-65イベントに列挙されたrelayへの接続を維持します。新しいaccountを発見するたび、新しいrelayへ動的に接続します。複数のfollow対象に共通して現れるrelayは、より多くのsocial graphを1つの接続でカバーできるので優先されます。

この構造はcensorship resistanceを改善します。1つのrelayだけが全員のcontentを保存し配信する必要がないからです。1つのrelayが落ちても、またはあるユーザーをblockしても、そのcontentは他のlisted relay上に残ります。

## なぜ重要か

NIP-65は、relay選択をhardcodedなclient defaultから、ユーザー自身が公開するrouting metadataへ変えます。これによりclientは、全員が同じrelay setを使うと仮定する代わりに、各accountの実際のpublishとreadの習慣へ適応できます。

その一方で複雑さはclient側へ移ります。outbox modelをうまく扱うには、clientにrelay caching、retry logic、relay listが欠けている場合や古い場合のfallback behaviorが必要です。仕様はdiscoverabilityを改善しますが、良いrelay selection heuristicの必要性までは消しません。

## Relay hintsとの関係

NIP-65は、他のNIP全体に見られるrelay hintsを補完します。`["p", "pubkey", "wss://hint.relay"]`のように誰かをtagするとき、そのhintはその特定参照に対してどこを見るべきかをclientへ伝えます。NIP-65はユーザー管理の優先relay一覧という authoritative sourceであり、hintは個別イベントに埋め込まれた近道としてより速いdiscoveryを助けます。

private messagingに関しては、NIP-65だけでは不十分です。public content routingはkind 10002を使いますが、現代的なprivate messaging stackは、DM routingをpublic posting relayと分離できるよう、[NIP-17](/ja/topics/nip-17/) relay listのような別のinbox metadataに頼ることが多いです。

## ベストプラクティス

relay listは常に最新に保つべきです。停止したrelayを指す古いentryは、あなたを見つけにくくします。冗長性のために最低2つか3つのrelayを含め、1つが落ちても他でcontentが取れるようにします。

relayを並べすぎるのは避けるべきです。10個や15個も列挙すると、あなたのcontentを取得したいすべてのclientがそれら全部へ接続しなければならず、体験が遅くなりnetwork負荷も増えます。3つから5つほどの厳選されたrelay listのほうが、誰も追いきれない網羅的リストより役に立ちます。

general-purpose relayとspecialized relayを混ぜるのも有効です。例えば、`wss://relay.damus.io`のような人気relay、地理的に近いrelay、特定community向けrelayを組み合わせられます。

---

**Primary sources:**
- [NIP-65 Specification](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Mentioned in:**
- [Newsletter #5: NIP Deep Dive](/ja/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: Outbox Model Benchmarks](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Wisp inbox-relay broadcasting](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-11: Relay Information](/ja/topics/nip-11/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
