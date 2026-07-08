---
title: "NIP-61: Nutzap"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
categories:
  - Zaps
  - Ecash
---

NIP-61は「nutzap」を定義します。これはNostrイベントとして配送されるピアツーピアのCashu ecash支払いです。送信者は受信者のNostr鍵宛にP2PKロックされたCashuトークンを公開し、受信者は都合の良いときにmintから引き換えます。プルーフ自体が価値を保持するため、NIP-61の支払いは受信者が自分のスケジュールで引き換えられる自己完結型のトークンとして届き、Lightningチャネルや対話的なハンドシェイクは不要です。

## 仕組み

NIP-61は、既存の2つのプリミティブの上に構築されます。[NIP-60](/ja/topics/nip-60/)のCashuウォレットとCashuのP2PKロックです。フローは3つのevent kindを使用します。

**Mint推奨（kind 10019）:** 受信者が公開する置き換え可能イベントで、受け入れるmintと、プルーフを自分にロックするために使用するCashu公開鍵を告知します。送信者は送信前にこれを読み、ロックされたトークンが受信者の引き換え可能なものになるようにします。

**Nutzapイベント（kind 9321）:** 支払い本体です。Cashuプルーフ（kind 10019の受信者のnutzap pubkeyにP2PKロックされたもの）、mint URL、任意でzap対象ノートを識別する`e`タグと`a`タグ、そして受信者用の`p`タグを持ちます。受信者は通常のNostr購読を通じて受け取り、対応する秘密鍵でプルーフをアンロックし、NIP-60ウォレットに保持するかLightningに溶解します。

**Nutzap情報（kind 7375）:** NIP-60のトークンイベントと同じ形状を持つキャッシュされた状態で、引き換え済みのnutzapプルーフを記録し、再同期時にウォレットが二重計上しないようにします。

## トレードオフと信頼モデル

nutzapは自己完結型のecashトークンです。受信者が後でmintに連絡できる限り、支払いを引き換えられます。mint自体が信頼できる保管者であり、これはNIP-60と同じ信頼モデルであって、その保管の選択がオフラインでも可能な即時決済のマイクロペイメントに対して支払う明示的な代償です。NIP-57のzapは、受信者がLightningノードを実行する（またはホストされる）ことと、着信HTLCをリアルタイムで受け付けるLNURLエンドポイントを持つことを求めます。Lightningチャネルを持たないスマートフォン、ファイアウォールの背後にいるユーザ、たまたまオフラインにいる受信者は、いずれもそのモデルの外側にあります。

kind 10019の告知は、社会的な層の信頼ゲートです。送信者は受信者が受け入れるmintの1つを選ぶことで、受信者の引き換え経路を予測可能に保ちます。受信者のセットの外側のmintを選ぶ送信者は引き換え不能なトークンを送るリスクを負うため、ウォレットはまずkind 10019を読み込みます。

## ワークフロー

1. 受信者はkind 10019を公開し、受け入れるmintとnutzap pubkeyを告知する
2. 送信者はkind 10019を読み、リストされたmintの1つでプルーフを鋳造し、受信者のnutzap pubkeyにP2PKロックする
3. 送信者はロックされたプルーフ、mint URL、対象タグを含むkind 9321を公開する
4. 受信者は通常のNostr購読を通じてkind 9321を受け取る
5. 受信者はnutzap秘密鍵でプルーフをアンロックし、NIP-60ウォレットに保持するかLightningに溶解する

## Nutzapイベントの例

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## 実装

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) は、NIP-60／NIP-61ウォレット画面の一部としてmintごとの残高ビューを備えたnutzapレンダリングを搭載しました（[PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075)）

---

**Primary sources:**
- [NIP-61仕様](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - NIP-60 CashuウォレットとNIP-61 nutzapサポート

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ja/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**See also:**
- [NIP-57: Zaps](/ja/topics/nip-57/)
- [NIP-60: Cashu Wallet](/ja/topics/nip-60/)
- [Cashu](/ja/topics/cashu/)
