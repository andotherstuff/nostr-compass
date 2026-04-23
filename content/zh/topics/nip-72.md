---
title: "NIP-72：审核社区"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 定义了 Nostr 上的审核社区。社区提供了一种围绕共同主题或群体来组织帖子的方式，由审核员在内容对成员可见之前进行批准。

## 工作原理

社区由其创建者发布的 kind 34550 event 定义。该 event 包含社区名称、描述、规则和审核员 pubkeys 列表。这个 event 使用可替换 event 格式（kind 30000-39999 范围），因此社区定义可以随着时间持续更新。

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

用户把自己的 events 加上一个指向社区定义的 `a` tag，以此向社区提交帖子。这些帖子在此时对社区读者还不可见。审核员会审查该提交，如果通过，就发布一个 kind 4549 的 approval event，把原始帖子包裹进去。显示该社区的客户端只会展示那些有被认可审核员对应 approval event 的帖子。

这种 approval 模型意味着，社区是“按读取结果过滤”的，而不是“按写入权限限制”的。任何人都可以提交帖子，但只有被批准的帖子才会出现在社区 feed 中。审核员扮演的是策展人，而不是底层数据的守门人。

## 注意事项

由于 approval events 是独立的 Nostr events，审核决策是透明且可审计的。一个被某个社区拒绝的帖子，仍然可能被另一个社区批准。同一内容也可以出现在多个社区中，并接受彼此独立的审核。

relay 支持对社区功能很重要。客户端必须同时查询社区定义和 approval events，因此需要那些能高效索引这些 event kinds 的 relays。

与 [NIP-29](/zh/topics/nip-29/) 的基于 relay 群组不同，后者把成员关系和审核权威都交给 relay，NIP-72 存活于普通的 Nostr events 中。任何承载 kinds `34550`、`4549` 以及提交内容 kind 的 relay 都可以服务一个社区，而审核本身既是可见的，也是可分叉的。它的代价在于，那些未被批准的提交只是在客户端渲染层被隐藏，因此当垃圾内容必须从根本上不出现在网络上传播时，NIP-29 仍然更合适。

## 实现

- [noStrudel](https://github.com/hzrd149/nostrudel) 长期支持 NIP-72 社区，包括面向审核员的待审批队列。
- [Amethyst](https://github.com/vitorpamplona/amethyst) 在 [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) 中增加了第一等社区创建与管理：编写 kind `34550` 社区定义、添加审核员和 relay hints、用 `a` tag 提交帖子，以及通过 kind `4549` events 管理待审批项。

---

**主要来源：**
- [NIP-72 Specification](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - NIP-72 community creation and moderation

**提及于：**
- [Newsletter #15](/zh/newsletters/2026-03-25-newsletter/)
- [Newsletter #19：Amethyst community support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-29：Relay-based Groups](/zh/topics/nip-29/)
