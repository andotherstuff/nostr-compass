---
title: "NIP-70: 保護イベント"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - Relay
  - アクセス制御
---

NIP-70は、著者がシンプルなタグ`["-"]`でイベントを保護済みとしてマークする方法を定義します。保護イベントは、relayがその動作をサポートすることを選択し、認証された発行者がイベント著者と同じpubkeyであることを確認した場合にのみ受け入れられます。

## 仕組み

コアルールは簡潔です。イベントに`["-"]`タグが含まれている場合、relayはデフォルトでそれを拒否すべきです。保護イベントをサポートしたいrelayは、まず[NIP-42](/ja/topics/nip-42/) `AUTH`フローを実行し、認証したクライアントが自身のイベントを公開していることを確認する必要があります。

これによりNIP-70は公開権限ルールとなり、暗号化ルールではありません。コンテンツは引き続き読み取り可能です。変更されるのは、タグを尊重するrelayにそのイベントを配置できる人です。これにより、relayはセミクローズドフィードや、著者が第三者による再公開をrelayに拒否させたいその他のコンテキストをサポートできます。

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

## AUTHフローへの影響

保護イベントは、relayが公開時に著者のアイデンティティを実際に強制する場合にのみ有用です。NIP-70が[NIP-42](/ja/topics/nip-42/)に直接依存する理由はここにあります。一致する認証チェックなしに`["-"]`イベントを受け入れるrelayは、タグをポリシーではなく装飾として扱っていることになります。

## Relayの動作と制限

NIP-70はコンテンツが永遠に封じ込められることを約束しません。受信者は見たものをコピーして別の場所に新しいイベントとして公開できます。仕様はrelayに著者の意図を尊重し、保護イベントの直接的な再公開を拒否するための標準的な方法を提供するのみです。

フォローアップ作業が重要な理由がここにあります。[PR #2251](https://github.com/nostr-protocol/nips/pull/2251)は、保護イベントを埋め込むリポストにもルールを拡張し、元のイベントは保護されているがラッパーイベントは保護されていないという容易な回避策を塞ぎます。

## 実装

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - 保護イベント用のNIP-42認証サポートを追加
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - 保護イベントを埋め込むリポストを拒否
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - 保護イベント処理に関連するヘルパーサポートを追加

---

**主要ソース:**
- [NIP-70仕様](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - NIPsリポジトリにNIP-70を追加
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - 保護イベントを埋め込むリポストの拒否
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - NIP-42認証と保護イベントのRelay実装

**掲載号:**
- [Newsletter #13: NIPアップデート](/en/newsletters/2026-03-11-newsletter/#nipアップデート)
- [Newsletter #13: NIPディープダイブ](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**関連項目:**
- [NIP-42: クライアント認証](/ja/topics/nip-42/)
- [NIP-11: Relay情報ドキュメント](/ja/topics/nip-11/)
