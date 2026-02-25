---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-90はData Vending Machines（DVM）を定義します。Nostr上で計算作業をリクエストして支払うためのマーケットプレイスプロトコルです。

## 仕組み

クライアントは必要な作業を指定するジョブリクエストevent（kind 5000-5999）を公開します。サービスプロバイダーは自分の能力に合うリクエストを監視し、計算完了後に結果を公開します。支払いはLightningまたはジョブフロー内で交渉される他のメカニズムで行われます。

ジョブkindは異なる計算タイプを定義します。テキスト生成、画像生成、翻訳、コンテンツ発見などです。各kindは期待される入出力フォーマットを指定します。

## 主な機能

- 分散型コンピュートマーケットプレイス
- kindベースのジョブタイプシステム
- 価格と品質でのプロバイダー競争
- 新しい計算タイプへの拡張性

---

**主要ソース：**
- [NIP-90仕様](https://github.com/nostr-protocol/nips/blob/master/90.md)

**掲載ニュースレター：**
- [ニュースレター#11：NIP-AC DVMエージェント調整](/ja/newsletters/2026-02-25-newsletter/#nipアップデート)

**関連項目：**
- [NIP-85：Trusted Assertions](/ja/topics/nip-85/)
