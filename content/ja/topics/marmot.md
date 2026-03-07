---
title: "Marmotプロトコル"
url: /ja/topics/marmot/
translationOf: /en/topics/marmot.md
translationDate: 2026-03-07
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmotは、Nostr上のend-to-end encrypted group messaging向けプロトコルです。Nostrのidentityとrelay networkに、グループ鍵管理、forward secrecy、post-compromise securityのためのMLSを組み合わせます。

## 仕組み

Marmotは、identity、relay transport、event distributionにはNostrを使い、その上にMLSを重ねてグループメンバーシップの変更とメッセージ暗号化を扱います。一対一のメッセージングに焦点を当てる[NIP-17](/ja/topics/nip-17/)と違い、Marmotはメンバーが参加、離脱、鍵ローテーションを繰り返すグループ向けに設計されています。

## 重要性

MLSにより、MarmotはNostrのdirect-message方式だけでは得られない性質を持てます。グループ状態の進化、メンバー削除の意味論、侵害後に後続の鍵更新で回復できる点がその例です。

重要なのは役割分担です。Nostrはオープンなネットワークでidentityとtransportを担い、MLSは認証付きのgroup key agreementを担います。Marmotはその間をつなぐglue layerです。

## 実装状況

このプロトコルはまだexperimentalですが、すでに複数の実装があり、アプリでも使われています。MDKが主要なRustリファレンススタックで、`marmot-ts`がこのモデルをTypeScriptへ持ち込み、White Noise、Pika、VectorのようなアプリがMarmot互換コンポーネントを使っています。

最近の作業はhardeningとinteropに集中しています。audit主導の修正が2026年初頭に入り、MIP-03によってdeterministic commit resolutionが導入され、relayをまたいで同時にグループ状態変更が競合したときでもクライアントが収束しやすくなりました。

---

**主要ソース:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [NIP-104: MLS-based Encrypted Group Chats](/ja/topics/nip-104/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**言及箇所:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #4](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**関連項目:**
- [MLS (Message Layer Security)](/ja/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/ja/topics/mip-05/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
