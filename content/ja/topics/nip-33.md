---
title: "NIP-33: パラメータ化置換可能イベント（アドレス可能イベント）"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - プロトコル
---

NIP-33はもともと、Relayが`(pubkey, kind, d-tag)`の組ごとに1件だけ保持するイベント群である、パラメータ化置換可能イベントを定義していました。この概念はその後「アドレス可能イベント」に改名され、[NIP-01](/ja/topics/nip-01/)に統合されました。NIP-33の文書自体は現在NIP-01へのリダイレクトですが、コードベースやドキュメントでは今でもよく参照されます。

## 仕組み

アドレス可能イベントは`30000-39999`の範囲のkindを使います。各イベントは`d`タグを持ち、その値が著者のpubkeyとkind番号と組み合わさって一意なアドレスを形成します。Relayが既存の`(pubkey, kind, d-tag)`に一致する新しいイベントを受け取ると、古いイベントを新しいイベント（`created_at`が新しい方）で置き換えます。これにより、プロフィール、設定、アプリ設定、分類型リスティングのように最新状態だけが重要な可変データに向きます。

クライアントは`a`タグを`<kind>:<pubkey>:<d-tag>`という形式で使い、必要ならRelayヒントを後ろに付けてアドレス可能イベントを参照します。

## 一般的な用途

- Kind `30023` のlong-form記事
- Kind `30078` のアプリ固有データ（NIP-78で使用）
- Kind `31923` のカレンダーイベント（NIP-52）
- Kind `31990` のハンドラー推奨情報（NIP-89）
- Kind `30009` のbadge定義（NIP-58）
- Kind `31991` のagent実行設定（Notedeck Agentium）

## NIP-01との関係

NIP-33は統合作業の一環としてNIP-01に取り込まれました。現在のNIP-01仕様は、通常イベント（そのまま保持）、置換可能イベント（`(pubkey, kind)`ごとに1件）、アドレス可能イベント（`(pubkey, kind, d-tag)`ごとに1件）の3種類の保持カテゴリを定義しています。NIP-33という呼び方は、今でもアドレス可能イベントの概念を指す省略形として有効です。

---

**主要ソース:**
- [NIP-33 (redirect)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md) - Addressable events section

**言及箇所:**
- [Newsletter #13: Notedeck](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-01: Basic Protocol](/ja/topics/nip-01/)

