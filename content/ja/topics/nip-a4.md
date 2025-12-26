---
title: "NIP-A4: パブリックメッセージ"
url: /ja/topics/nip-a4/
translationOf: /en/topics/nip-a4.md
translationDate: 2025-12-26
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4は、通知画面向けに設計されたパブリックメッセージ（kind 24）を定義し、幅広いクライアントサポートを目標としています。

## 仕組み

スレッド化された会話とは異なり、これらのメッセージにはチャット履歴やメッセージチェーンの概念がありません。受信者の通知フィードに表示されることを意図したシンプルな単発メッセージです。

## 構造

- スレッド化の複雑さを避けるため、`e`タグではなく`q`タグ（引用）を使用
- 会話の状態や履歴なし
- シンプルなパブリック通知向けに設計

## ユースケース

- 公開の謝辞やシャウトアウト
- ユーザーへのブロードキャストメッセージ
- 返信スレッドが不要な通知

---

**主要ソース:**
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**言及箇所:**
- [ニュースレター #2: NIP更新](/ja/newsletters/2025-12-24-newsletter/#nip-updates)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
- [NIP-10: テキストノートスレッド](/ja/topics/nip-10/)
