---
title: "NIP-29：基于 Relay 的群组"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-04-22
draft: false
categories:
  - Social
  - Groups
---

NIP-29 定义了基于 relay 的群组，其中 relay 负责管理成员关系、权限以及消息可见性。

## 工作原理

群组由 relay host 加上群组 id 共同确定，relay 本身就是成员关系和审核的权威。发往群组的用户 event 会带有包含 group id 的 `h` tag。由 relay 生成的元数据则使用 relay 自己的 key 签名的可寻址 events。

核心元数据 event 是 kind 39000，而 kind 39001 到 39003 分别描述管理员、成员和支持的角色。审核动作则通过 9000 系列 events 完成，例如 `put-user`、`remove-user`、`edit-metadata` 和 `create-invite`。

## 访问模型

- **private**：只有成员能读取群消息
- **closed**：除非 relay 使用 invite-code 机制，否则加入请求会被忽略
- **hidden**：relay 向非成员隐藏群组元数据，使其不可发现
- **restricted**：只有成员能够向群里写入消息

这些标签彼此独立。一个群组可以对所有人可读但只允许成员写入，也可以对非成员完全隐藏。这个区分很重要，因为客户端不应把“private”当成所有访问规则的统称。

## 信任模型

NIP-29 并不是一个无信任群组协议。托管该群组的 relay 决定哪些审核 events 有效、有哪些角色、成员列表是否可见，以及旧消息或脱离上下文的消息是否会被接受。客户端可以验证签名和时间线引用，但群组的真实状态仍然依赖 relay 策略。

这让迁移和分叉成为可能，但不会自动发生。同一个 group id 可以在不同 relays 上存在，并拥有不同的历史和规则，因此在实践中 relay URL 本身就是群组身份的一部分。

## 有用的实现说明

- 客户端应把 relay URL 当成群组的 host key。2026 年 1 月的一项澄清让这一点在规范中变得明确，并消除了“是否应使用 pubkey”的歧义。
- 群组状态是从审核历史中重建出来的，而 39000 系列 relay events 只是该状态的信息性快照。
- 时间线中的 `previous` 引用不仅用于改进 UI 线程，还用于防止消息在不同 relay fork 之间被脱离上下文地重新广播。

## 近期规范工作

- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) 以及 hodlbod 的 [Flotilla 1.7.3/1.7.4 发布说明](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) 提出了对非聊天内容类型（如 calendar events、polls 等）的 kind-9 wrapping，使这些对象进入群组时仍然保留房间上下文。
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) 为规范增加了 subgroup 层级，让单个群组可以承载多个并行频道，而不必在同一 relay 上再生成多个独立群组；subgroup 标识复用了现有的 `h` tag 机制，从而保留了对旧客户端仍可工作的单 `h` tag 消息形状。
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) 在 kind `39003` 角色 event 上定义了显式权限模式，让每个角色都成为一组命名的、可授予的操作（invite、add-user、remove-user、edit-metadata、delete-event、add-permission），并可附带可选的到期时间。

## 实现

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) 是 hodlbod 的主要 NIP-29 客户端；[1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) 和 [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) 发布了 kind-9 wrapping、polls、通过 Aegis URL scheme 完成的 [NIP-46](/zh/topics/nip-46/) 登录、space invites 的原生分享支持、room mentions、移动端剪贴板图片粘贴、drafts 和通话中的视频。
- [Wisp](https://github.com/barrydeen/wisp) 在 [PR #471](https://github.com/barrydeen/wisp/pull/471) 中加入了 NIP-29 群组配置功能，覆盖 flags、invites、roles 和 AUTH prompts，并在 [PR #478](https://github.com/barrydeen/wisp/pull/478) 中强化了 AUTH 顺序，确保在发送群组 `9021`、`9007` 和 `9009` events 前先完成认证。

---

**主要来源：**
- [NIP-29 规范](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - 澄清 `private`、`closed` 和 `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - 澄清 relay URL 作为 relay key
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - 增加 `unallowpubkey` 和 `unbanpubkey`
- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) - 面向非聊天内容的 kind-9 wrapping
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) - Subgroups 规范
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) - kind 39003 上的显式角色权限
- [Flotilla 1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)
- [Wisp PR #471](https://github.com/barrydeen/wisp/pull/471) - NIP-29 group configuration

**提及于：**
- [Newsletter #2：NIP 更新](/zh/newsletters/2025-12-24-newsletter/)
- [Newsletter #3：December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #6：NIP 更新](/zh/newsletters/2026-01-21-newsletter/)
- [Newsletter #11：NIP 更新](/zh/newsletters/2026-02-25-newsletter/)
- [Newsletter #12：NIP 更新](/zh/newsletters/2026-03-04-newsletter/)
- [Newsletter #19：Flotilla 1.7.3/1.7.4](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：Wisp 的 NIP-29 配置](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：NIP 更新（subgroups、role permissions）](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
