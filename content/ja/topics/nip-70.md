---
title: "NIP-70: 保護イベント"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - リレー
  - アクセス制御
---

NIP-70は、著者が単純な`[["-"]]`タグでイベントをprotectedとしてマークする方法を定義します。protected eventは、Relayがその挙動をサポートし、かつ認証済みの発行者がイベント著者と同じpubkeyであることを確認できた場合にのみ受け入れられます。

## 仕組み

中核ルールは短いものです。イベントに`[["-"]]`タグが含まれている場合、Relayはデフォルトでそれを拒否するべきです。protected eventをサポートしたいRelayは、まず[NIP-42](/ja/topics/nip-42/)の`AUTH`フローを実行し、認証したクライアントが自分自身のイベントを公開していることを確認しなければなりません。

これにより、NIP-70は暗号化ルールではなく、公開権限ルールになります。content自体は依然として読める場合があります。変わるのは、そのタグを尊重するRelayへ誰がそのイベントを置けるかです。これにより、著者が第三者による再公開をRelayに拒否させたい半閉鎖フィードや類似の文脈をサポートできます。

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## AUTHフローの含意

protected eventが意味を持つのは、Relayが公開時に著者アイデンティティを実際に強制する場合だけです。だからこそNIP-70は[NIP-42](/ja/topics/nip-42/)に強く依存します。一致するauth checkなしに`[["-"]]`イベントを受け入れるRelayは、そのタグをポリシーではなく飾りとして扱っているにすぎません。

## Relayの振る舞いと限界

NIP-70は、contentが永遠に閉じ込められることを約束しません。受信者は依然として見たものをコピーし、別の場所に新しいイベントとして公開できます。仕様が与えるのは、著者の意図を尊重し、protected eventの直接再公開を拒否するための標準的な方法だけです。

そのため、後続作業が重要になります。[PR #2251](https://github.com/nostr-protocol/nips/pull/2251)は、protected eventを埋め込むrepostにもこの規則を拡張し、元イベントはprotectedでもwrapper eventは違うという簡単な迂回経路を塞ぎます。

## 実装

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - protected event向けNIP-42 auth supportを追加
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - protected eventを埋め込むrepostを拒否
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - protected-event handlingに結び付くhelper supportを追加

---

**主要ソース:**
- [NIP-70 Specification](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - NIP-70をNIPs repositoryへ追加
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - protected eventを埋め込むrepostを拒否
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - NIP-42 authとprotected eventsのRelay実装

**言及箇所:**
- [Newsletter #13: NIP Updates](/ja/newsletters/2026-03-11-newsletter/)
- [Newsletter #13: NIP Deep Dive](/ja/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70保護イベント)

**関連項目:**
- [NIP-42: クライアントからRelayへの認証](/ja/topics/nip-42/)
- [NIP-11: Relay情報ドキュメント](/ja/topics/nip-11/)

