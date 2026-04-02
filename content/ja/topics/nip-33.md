---
title: "NIP-33: パラメータ付き置換可能イベント（アドレス可能イベント）"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - プロトコル
---

NIP-33は元々パラメータ付き置換可能イベントを定義していました。これはrelayが`(pubkey, kind, dタグ)`のタプルごとに1つのイベントのみを保持するイベントクラスです。このコンセプトはその後「アドレス可能イベント」に改名され、[NIP-01](/ja/topics/nip-01/)に統合されました。NIP-33のドキュメントは現在NIP-01にリダイレクトされますが、コードベースやドキュメントでは依然として一般的な参照先です。

## 仕組み

アドレス可能イベントは`30000-39999`の範囲のkindを使用します。各イベントは`d`タグを持ち、その値は著者のpubkeyとkind番号とともに一意のアドレスを形成します。relayが既存の`(pubkey, kind, dタグ)`タプルに一致する新しいイベントを受信すると、古いイベントを新しいイベント（`created_at`による）に置き換えます。これにより、アドレス可能イベントはプロフィール、設定、アプリ設定、分類リスティングなど、最新バージョンのみが重要な可変状態に適しています。

クライアントはアドレス可能イベントを`<kind>:<pubkey>:<dタグ>`の形式の`a`タグで参照し、オプションでrelayヒントを追加します。

## 一般的な用途

- Kind `30023` 長文記事
- Kind `30078` アプリ固有データ（NIP-78で使用）
- Kind `31923` カレンダーイベント（NIP-52）
- Kind `31990` ハンドラー推奨（NIP-89）
- Kind `30009` バッジ定義（NIP-58）
- Kind `31991` エージェント実行設定（Notedeck Agentium）

## NIP-01との関係

NIP-33は統合作業の一環としてNIP-01にマージされました。NIP-01の仕様は現在、通常イベント（そのまま保持）、置換可能イベント（`(pubkey, kind)`ごとに1つ）、アドレス可能イベント（`(pubkey, kind, dタグ)`ごとに1つ）の3つのイベント保持カテゴリを定義しています。NIP-33はアドレス可能イベントの概念の有効な略称として残っています。

---

**主要ソース:**
- [NIP-33（リダイレクト）](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01仕様](https://github.com/nostr-protocol/nips/blob/master/01.md) - アドレス可能イベントセクション

**掲載号:**
- [Newsletter #13: Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
