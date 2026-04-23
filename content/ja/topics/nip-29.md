---
title: "NIP-29: Relay-based Groups"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-04-22
draft: false
categories:
  - Social
  - Groups
---

NIP-29は、relayがgroup membership、permission、message visibilityを管理するrelay-based groupsを定義します。

## 仕組み

groupはrelay hostとgroup idの組み合わせで識別され、relayがmembershipとmoderationのauthorityになります。groupへ送られるユーザー作成イベントはgroup idを持つ`h`タグを含みます。relay生成metadataは、relay自身の鍵で署名されたaddressable eventを使います。

中核metadata eventはkind 39000で、39001から39003はadmin、member、supported roleを記述します。moderation actionは、`put-user`、`remove-user`、`edit-metadata`、`create-invite`のような9000番台イベントで行われます。

## アクセスモデル

- **private**: memberだけがgroup messageを読める
- **closed**: relayがinvite-code処理を使わない限り、join requestは無視される
- **hidden**: relayはnon-memberへgroup metadataを隠し、groupを発見不能にする
- **restricted**: memberだけがgroupへmessageを書ける

これらのtagは独立しています。誰でも読めるがmemberだけが書けるgroupにもでき、non-memberから完全に隠すこともできます。この分離は重要で、clientは`private`をあらゆるaccess ruleの総称として扱うべきではありません。

## 信頼モデル

NIP-29はtrustlessなgroup protocolではありません。hosting relayが、どのmoderation eventを有効とみなすか、どんなroleがあるか、member listを見せるか、古いあるいは文脈外messageを受け入れるかを決めます。clientはsignatureとtimeline referenceを検証できますが、groupの実際の状態についてはrelay policyに依存します。

このためmigrationやforkは可能ですが、自動ではありません。同じgroup idが異なるrelay上に別の履歴やruleで存在できるため、relay URLが実質的にgroup identityの一部になります。

## 実装メモ

- clientはrelay URLをgroup host keyとして扱うべきです。2026年1月の明確化で、pubkeyではなくこれを使うことが仕様上はっきりしました
- group stateはmoderation historyから再構築され、39000番台のrelay eventはそのstateの参考snapshotです
- timelineの`previous`参照は、UI threadingの改善だけでなく、relay fork間での文脈外rebroadcastを防ぐためにあります

## 最近の仕様作業

- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310)とhodlbodの[Flotilla 1.7.3/1.7.4 release notes](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)は、calendar eventやpollなどのnon-chat content typeをkind `9`で包む提案を行っています。これにより、それらをgroupへ送ったときroom contextを保持できます。
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319)はsubgroup hierarchyを追加し、1つのgroupが同じrelay上で独立groupを乱立させずに複数parallel channelを持てるようにします。subgroup identifierは既存の`h`タグへ相乗りし、旧client向けの単一`h`タグmessage形を保ちます。
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316)はkind `39003` role eventに明示的permissionを定義し、各roleを、invite、add-user、remove-user、edit-metadata、delete-event、add-permissionのような操作集合と、任意の期限付きexpiryを持つnamed setにします。

## Implementations

- [Flotilla](https://gitea.coracle.social/coracle/flotilla)はhodlbodの主要NIP-29 clientです。[1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3)と[1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)では、kind-9 wrapping、poll、[NIP-46](/ja/topics/nip-46/) login via Aegis URL scheme、space invite向けnative share、room mention、mobile clipboard image paste、draft、video in callsが入りました。
- [Wisp](https://github.com/barrydeen/wisp)は[PR #471](https://github.com/barrydeen/wisp/pull/471)でflag、invite、role、AUTH prompt向けNIP-29 group configurationを追加し、[PR #478](https://github.com/barrydeen/wisp/pull/478)でgroup `9021`、`9007`、`9009`イベントの前にAUTHを待つ順序を強化し、admin側failureも表示するようにしました。

---

**Primary sources:**
- [NIP-29 Specification](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Clarified `private`, `closed`, and `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Clarified relay URL as the relay key
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Added `unallowpubkey` and `unbanpubkey`
- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) - Kind-9 wrapping for non-chat content
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) - Subgroups spec
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) - Explicit role permissions on kind 39003
- [Flotilla 1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)
- [Wisp PR #471](https://github.com/barrydeen/wisp/pull/471) - NIP-29 group configuration

**Mentioned in:**
- [Newsletter #2: NIP Updates](/ja/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #6: NIP Updates](/ja/newsletters/2026-01-21-newsletter/)
- [Newsletter #11: NIP Updates](/ja/newsletters/2026-02-25-newsletter/)
- [Newsletter #12: NIP Updates](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Flotilla 1.7.3/1.7.4](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Wisp NIP-29 config](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Updates (subgroups, role permissions)](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-11: Relay Information Document](/ja/topics/nip-11/)
