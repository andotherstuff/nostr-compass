---
title: "NIP-09: イベント削除リクエスト"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-09は、authorが以前に公開したeventの削除を要求する方法を定義します。これはrelay側の削除シグナルであり、network全体から消去する機能ではありません。

## 仕組み

ユーザーは、削除したいeventへの参照を含むkind 5 eventを公開します。NIP-09をサポートするrelayは、同じauthorによる該当eventの配信を止めるべきであり、storageから削除することもあります。

削除はrequestであって保証ではありません。relayが削除requestを無視することもあれば、削除非対応のrelayへeventがすでに伝播していることもあります。privacyに敏感な内容の削除手段としてNIP-09に依存するべきではありません。

## なぜ重要か

NIP-09は、clientとrelayに共通の方法で「このeventは今後表示しないべきだ」と表現させます。これは誤投稿、wallet stateの切り替え、moderation workflowで役立ちます。ただし、authorが削除を要求できるのは自分自身のeventだけです。third-party contentを取り下げる一般目的の仕組みではありません。

## Tradeoffs

弱点は伝播です。eventが複数relayへ複製された後は、削除はbest-effortになります。削除するrelayもあれば、tombstone化するrelayもあり、無期限に配信し続けるrelayもあります。削除を最終確定のように見せるclientは、protocolの保証を言い過ぎています。

もう1つの実務上の問題は参照です。準拠relayが配信を止めた後でも、ユーザーやappが削除済みeventをローカルに保持していたり、別の場所で引用していたりすることがあります。

---

**主要ソース:**
- [NIP-09 Specification](https://github.com/nostr-protocol/nips/blob/master/09.md)

**言及箇所:**
- [Newsletter #11: NIP-60 Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
- [NIP-60: Cashu Wallet](/ja/topics/nip-60/)
