---
title: "NIP-77: Negentropyによる集合照合"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77は、Nostrのリレーとクライアントが[Negentropy](/ja/topics/negentropy/)集合照合プロトコルを使用して、データセット全体を再送することなく、どちら側に不足しているイベントがあるかを特定しながら、イベントセットを効率的に同期する方法を定義します。

## 仕組み

Negentropy照合は、専用のメッセージタイプを使用してWebSocket接続上で実行されます。クライアントとリレーは、ソートされたイベントセット上でコンパクトな範囲フィンガープリントを交換し、差異のある範囲のみに絞り込みます。差異が特定されると、不足しているイベントID（その後、不足しているイベント自体）のみが転送されます。

NIP-77は、仕様を実装した任意のクライアントとリレーが効率的な同期セッションをネゴシエートできるよう、メッセージフレーミングを標準化します。プロトコルは、既存のNostr WebSocket接続上で`NEG-OPEN`、`NEG-MSG`、`NEG-CLOSE`メッセージタイプを使用します。

## なぜ重要なのか

従来のNostr同期はタイムスタンプベースの`since`フィルターを使用しますが、クロックドリフト、同一タイムスタンプのイベント、順序どおりに届かないイベントなどにより、イベントを見逃す可能性があります。Negentropyはタイムスタンプに依存するのではなく、実際のイベントセットを比較するため、単純なポーリングよりも大幅に少ないラウンドトリップで証明可能な完全な同期を実現します。

これは特に以下の場合に有用です：
- オフライン後に追いつくモバイルクライアント
- リレー間レプリケーション
- ローカルリレー同期（CitrineのリレーアグリゲーターなどのようなDash）

## 実装

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) でAndroidリレーノードへの効率的な集合照合同期のためのNIP-77サポートを追加
- [strfry](https://github.com/hoytech/strfry) — リレー側のNegentropy対応
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — クライアント側のNegentropy実装

---

**主要ソース：**
- [NIP-77仕様](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Negentropyプロトコル](https://github.com/hoytech/negentropy)

**掲載：**
- [ニュースレター#22: Citrine v3.0.0-pre1](/ja/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**関連項目：**
- [Negentropy](/ja/topics/negentropy/)
