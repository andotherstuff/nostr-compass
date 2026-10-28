---
title: "NIP-06: ニーモニックによる鍵導出"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06 は、ニーモニックのシードフレーズから Nostr の鍵ペアを導出する方法を定めています。[現在の公式 NIP-06 テキスト](https://github.com/nostr-protocol/nips/blob/master/06.md)はドラフトかつオプションとされており、次の警告が付いています。

> __警告__ `unrecommended`: 単一の nsec を優先すること

このページでは、歴史的な互換性のために NIP-06 を取り上げています。シード導出の採用を推奨するものではありません。

## 仕組み

[現在の仕様](https://github.com/nostr-protocol/nips/blob/master/06.md)によると、ニーモニックの単語の生成と、そこからのバイナリシードの導出には BIP39 が使われます。続いて BIP32 が、パス `m/44'/1237'/<account>'/0/0` に沿って鍵を導出します。ここで 1237 は SLIP44 における Nostr のエントリです。基本的なクライアントはアカウント 0 を使えます。アカウント値を増やしていけば、同じシードから別の鍵が得られます。2 つの実装が同じアイデンティティを再現できるのは、導出手順で一致し、かつ結果に正しいエンコーディングを用いる場合に限られます。

## テストベクター

[2023 年 10 月 12 日のコミット](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)で、2 つのテストベクターが追加されました。1 つは 12 語のニーモニックから、もう 1 つは 24 語のニーモニックから作られています。どちらにも、期待される秘密鍵と公開鍵が 16 進数で記載され、対応する nsec と npub のエンコーディングも併記されています。開発者はこれらのベクターを使って、実装同士を照合できます。ベクターは鍵の管理については何も述べておらず、セキュリティを認定するものでも、普遍的な相互運用性を保証するものでもありません。

## 関連項目

- [NIP-01](/ja/topics/nip-01/)

**一次資料:**

- [NIP-06 (現行)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [NIP-06 のテストベクターを追加したコミット (2023 年 10 月 12 日)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**言及箇所:**

- [ニュースレター #46](/ja/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
