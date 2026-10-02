---
title: "NIP-28：公共聊天"
date: 2026-09-30
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Social
---

NIP-28 把公共聊天频道、频道消息和客户端侧审核描述为 Nostr event。当前规范被标记为 **draft**（草案）和 **unrecommended**（不推荐），并引导实现者改用 NIP-29 来实现当前基于 relay 的群组。

## Event 模型 {#event-model}

kind `40` 创建频道；kind `41` 更新频道元数据；kind `42` 承载消息。kind `43` 和 `44` 让用户在自己的客户端中隐藏某条消息或屏蔽另一位用户。消息 tag 指向频道创建 event，并可以标识被回复的消息。relay 不必强制执行这些客户端侧的隐藏和屏蔽选择。

[2022 年 9 月的规范变更](https://github.com/nostr-protocol/nips/commit/3423a6dfb)让公共聊天室成为一个共享的协议主题。尽管[现行规范](https://github.com/nostr-protocol/nips/blob/master/28.md)建议新实现采用另一条路径，理解这一历史角色仍然有用。

---

**主要来源：**
- [NIP-28 规范及当前状态](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [2022 年 9 月的公共聊天变更](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**提及于：**
- [第42期周刊：2022 年 9 月](/zh/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**另请参阅：**
- [NIP-29：基于 relay 的群组](/zh/topics/nip-29/)
