---
title: "NIP-29: リレーベースグループ"
date: 2025-12-24
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Groups
---

NIP-29はリレーベースのグループを定義し、リレーがグループのメンバーシップ、権限、メッセージの可視性を管理します。

## 仕組み

グループはrelay hostとgroup idの組で識別され、membershipとmoderationの権威はリレーにあります。グループに送られるユーザー作成イベントはgroup idを持つ`h`タグを持ちます。リレーが生成するmetadataは、リレー自身のkeyで署名されたaddressable eventを使います。

中核になるmetadata eventはkind 39000で、kind 39001から39003がadmin、member、supported roleを記述します。moderation actionは`put-user`、`remove-user`、`edit-metadata`、`create-invite`のような9000番台イベントで行われます。

## アクセスモデル

- **private**: メンバーのみがグループメッセージを読める
- **closed**: リレーがinvite-code処理を使わない限り、参加リクエストは無視される
- **hidden**: リレーが非メンバーからグループメタデータを隠し、グループを発見不可能にする
- **restricted**: メンバーのみがグループにメッセージを書ける

これらのタグは互いに独立しています。誰でも読めるがmemberだけが書けるグループにもできますし、非memberから完全に隠されたグループにもできます。この分離は重要で、クライアントは`private`をすべてのアクセス制御の総称として扱うべきではありません。

## 信頼モデル

NIP-29はtrustlessなグループプロトコルではありません。ホスティングするリレーが、どのmoderation eventを有効とみなすか、どんなroleが存在するか、member listを見せるか、古いメッセージや文脈外メッセージを受け入れるかを決めます。クライアントはsignatureやtimeline referenceを検証できますが、グループの実際の状態は依然としてrelay policyに依存します。

そのため、migrationやforkは可能でも自動ではありません。同じgroup idが別のリレー上に存在しても、履歴やルールは異なる可能性があります。実務上、relay URLはグループ識別子の一部です。

## 実装メモ

- クライアントはrelay URLをgroup host keyとして扱うべきです。2026-01の明確化で、pubkeyではなくこれを使うことが仕様上はっきりしました
- グループ状態はmoderation historyから再構築され、39000番台のrelay eventはその状態のinformative snapshotとして働きます
- timelineの`previous`参照は、relay fork間で文脈外の再配信を防ぐためのもので、単なるUI上のスレッド改善ではありません

---

**主要ソース:**
- [NIP-29仕様](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Clarified `private`, `closed`, and `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Clarified relay URL as the relay key
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Added `unallowpubkey` and `unbanpubkey`

**言及箇所:**
- [ニュースレター #2: NIP更新](/ja/newsletters/2025-12-24-newsletter/#nip-updates)
- [ニュースレター #3: December Recap](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [ニュースレター #6: NIP更新](/ja/newsletters/2026-01-21-newsletter/#nip-updates)
- [ニュースレター #11: NIP更新](/ja/newsletters/2026-02-25-newsletter/#nip-updates)
- [ニュースレター #12: NIP更新](/ja/newsletters/2026-03-04-newsletter/#nip-updates)

**関連項目:**
- [NIP-11: Relay Information Document](/ja/topics/nip-11/)
