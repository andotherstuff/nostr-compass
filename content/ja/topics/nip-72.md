---
title: "NIP-72: Moderated Communities"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72は、Nostr上のmoderated communitiesを定義します。communityは、共有されたtopicやgroupのまわりに投稿を整理する方法を提供し、moderatorがcontentを承認してからmemberへ見えるようにします。

## 仕組み

communityは、作成者が公開するkind 34550イベントで定義されます。このイベントにはcommunity名、説明、rules、moderator pubkeyの一覧が入ります。eventはreplaceable event format（kind 30000-39999範囲）を使うため、community定義は時間とともに更新できます。

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

ユーザーは、community定義を指す`a`タグを自分のイベントへ付けることでcommunityへ投稿を提出します。これらの投稿は、まだcommunity読者には見えません。moderatorが提出物を確認し、承認する場合は元投稿を包むkind 4549のapproval eventを公開します。communityを表示するclientは、認識済みmoderatorからの対応するapproval eventを持つ投稿だけを表示します。

このapproval modelは、communityがwrite-restrictedではなくread-filteredであることを意味します。誰でも投稿を提出できますが、承認されたものだけがcommunity feedへ現れます。moderatorは、基盤データへの門番ではなくcuratorとして機能します。

## 考慮点

approval eventは独立したNostrイベントなので、moderation判断は透明で監査可能です。あるcommunityに拒否された投稿でも、別のcommunityでは承認され得ます。同じcontentが、互いに独立したmoderationを持つ複数communityに存在できます。

community機能にはrelay supportも重要です。clientはcommunity定義とapproval eventの両方を問い合わせる必要があり、これらのevent kindを効率よくindexできるrelayが必要です。

[NIP-29](/ja/topics/nip-29/)のrelay-based groupsと比べると、NIP-72は平文のNostr events上に存在します。kind `34550`、`4549`、投稿kindを運ぶrelayなら、どれでもcommunityを提供できますし、moderationは見える形でfork可能です。代わりに、未承認投稿はclientの描画層で隠されるだけなので、spamをそもそもwireへ流したくない用途ではNIP-29のほうが適しています。

## Implementations

- [noStrudel](https://github.com/hzrd149/nostrudel)は、moderator向けpending submission queueを含む長年のNIP-72 community supportを持っています。
- [Amethyst](https://github.com/vitorpamplona/amethyst)は[PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468)で、kind `34550` community定義の作成、moderatorとrelay hintの追加、`a`タグによる投稿提出、kind `4549`イベントによるpending approval管理を含むfirst-classなcommunity作成と管理を追加しました。

---

**Primary sources:**
- [NIP-72 Specification](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - NIP-72 community creation and moderation

**Mentioned in:**
- [Newsletter #15](/ja/newsletters/2026-03-25-newsletter/)
- [Newsletter #19: Amethyst community support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-29: Relay-based Groups](/ja/topics/nip-29/)
