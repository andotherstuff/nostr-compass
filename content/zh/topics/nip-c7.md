---
title: "NIP-C7：聊天消息"
date: 2026-04-15
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-C7 将 kind `9` 定义为聊天消息的专用 event kind。它的目标，是把面向聊天的流量与通用社交信息流流量分开，这样客户端就能针对不同上下文应用不同的 UX 和审核规则。

## 工作原理

一个 kind `9` event 会携带消息内容，以及标识聊天上下文的 tags。在 [NIP-29](/zh/topics/nip-29/) 的基于 relay 的群组中，这个 event 会带有一个包含群组 ID 的 `h` tag。回复线程则使用引用更早 events 的 `q` tags。

NIP-C7 的重点在于这些 events 应该在哪里渲染。它们不应该像 kind `1` 文本笔记那样出现在全局 note feed 里，而是应该出现在聊天导向的视图中，在这些视图里，对话状态和线程关系都是显式的。

## 实现

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) 和 [Coracle](https://github.com/coracle-social/coracle) 在群聊工作流中使用 kind `9`。
- [Amethyst](https://github.com/vitorpamplona/amethyst) 在其消息栈中支持 kind `9`。
- [White Noise](https://github.com/marmot-protocol/whitenoise) 使用带 `q` tag 的 NIP-C7 回复线程。

---

**主要来源：**
- [NIP-C7 规范](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: Restrict kind 9 to chat views](https://github.com/nostr-protocol/nips/pull/2310)

**提及于：**
- [Newsletter #18：NIP 更新](/en/newsletters/2026-04-15-newsletter/)

**另请参阅：**
- [NIP-29：基于 relay 的群组](/zh/topics/nip-29/)
- [NIP-17：私密私信](/zh/topics/nip-17/)
