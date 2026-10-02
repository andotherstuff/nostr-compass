---
title: "Buzz NIP-FI: フェデレーテッドidentityアサーション"
date: 2026-09-30
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
---

NIP-FIは、Buzzの**プロジェクト固有**のフェデレーテッドidentityアサーション仕様です。この名称は、`nostr-protocol/nips`リポジトリでの採用や、Buzz以外のrelayとの相互運用を意味しません。

## HTTPの受け入れ口

強制モードで保護されたHTTPリクエストでは、BuzzはフェデレーテッドidentityアサーションをNIP-98の署名付き認可eventと組み合わせます。HTTP署名で証明されたNostr公開鍵は、アサーションに記された鍵と一致しなければなりません。欠落した証拠、一致しない証拠、検証できない証拠は拒否されます。Buzzはこの組み合わせを使って、外部のidentity発行者による認可の判断を、リクエストを行っているNostr鍵に結び付けています。

[プロジェクト仕様の改訂](https://github.com/block/buzz/pull/7254)は強制モデルを定義しています。[マージ済みのHTTP受け入れ口の実装](https://github.com/block/buzz/pull/7264)は、relayブリッジ、メディア、ワークフロー、Gitの経路を含む、Buzzの保護されたHTTPの各面を対象としています。このマージはソース上のテストを報告していますが、他のNostr relayが同じポリシーを実装していることを意味するものではありません。

---

**主要ソース:**
- [BuzzのNIP-FI仕様の改訂](https://github.com/block/buzz/pull/7254)
- [BuzzのHTTP受け入れ口の実装](https://github.com/block/buzz/pull/7264)

**言及箇所:**
- [Newsletter #42: Buzzのidentity制御](/ja/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
