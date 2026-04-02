---
title: "NIP-72：审核社区"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 社区
---

NIP-72 定义了 Nostr 上的审核社区。社区提供了一种围绕共同主题或群组组织帖子的方式，由审核员在内容对成员可见之前批准内容。

## 工作原理

社区由其创建者发布的 kind 34550 event 定义。该 event 包含社区名称、描述、规则和审核员 pubkey 列表。该 event 使用可替换事件格式（kind 30000-39999 范围），因此社区定义可以随时间更新。

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

用户通过在其 event 上添加指向社区定义的 `a` tag 将帖子提交到社区。这些帖子尚未对社区读者可见。审核员审查提交内容，如果批准，则发布一个包装原始帖子的 kind 4549 批准 event。显示社区的客户端只展示有来自认可审核员的相应批准 event 的帖子。

这种批准模型意味着社区是读取过滤的，而非写入限制的。任何人都可以提交帖子，但只有被批准的帖子出现在社区信息流中。审核员充当策展人而非底层数据的看门人。

## 注意事项

由于批准 event 是独立的 Nostr event，审核决定是透明且可审计的。被一个社区拒绝的帖子仍然可以被另一个社区批准。相同的内容可以存在于具有独立审核的多个社区中。

Relay 支持对社区功能很重要。客户端需要查询社区定义和批准 event，这需要能高效索引这些 event kind 的 relay。

---

**主要来源：**
- [NIP-72 规范](https://github.com/nostr-protocol/nips/blob/master/72.md) - 审核社区

**提及于：**
- [周刊 #15](/zh/newsletters/2026-03-25-newsletter/)
