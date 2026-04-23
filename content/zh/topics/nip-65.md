---
title: "NIP-65：Relay List Metadata"
date: 2026-01-13
translationOf: /en/topics/nip-65.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 定义了 kind 10002 events，用来广告某个用户偏好的读写 relays。这些元数据帮助其他用户和客户端在分布式 relay 网络中定位你的内容，同时启用一种叫做“outbox model”的分发方式，以分散负载并提升抗审查能力。

## 结构

relay list 是一种可替换 event（kind 10002），其中为用户想广告的每个 relay 添加一个 `r` tag。该 event 会替换同一 pubkey 此前发布的任何 relay list。

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

每个 `r` tag 都包含一个 relay WebSocket URL，以及一个可选 marker，用来表明用户如何与该 relay 交互。`read` marker 表示用户会从该 relay 消费 events，因此其他人应向那里发布内容，以触达这个用户。`write` marker 表示用户会把内容发布到该 relay，因此其他人若要看到此用户内容，就应订阅那里。不写 marker 则表示同时用于 read 和 write。

relay list events 的 `content` 字段为空。

## Outbox Model

NIP-65 启用了一种叫做“outbox model”的去中心化内容分发模式。它不再要求所有人都向同一组中心 relays 发布和读取，而是让用户向自己偏好的 relays 发布内容，并由客户端动态发现每个用户的内容该去哪里找。

如果 Alice 想看 Bob 的帖子，她的客户端会先从任何持有该 event 的 relay 上抓取 Bob 的 kind 10002 event，然后提取 Bob 标记为 `write` 的 relays，因为那是他发布内容的地方。随后客户端订阅这些 relays 来获取 Bob 的 events。如果 Alice 想给 Bob 发私信，客户端则会改查他的 `read` relays，并把消息发到那里。

采用 outbox model 的客户端，会维护与其关注用户 NIP-65 events 中列出的 relays 的连接。随着它发现更多账号，它会动态连接新的 relays。出现在多个被关注用户列表中的 relays 会被优先考虑，因为连接它们就能覆盖更大一部分社交图谱。

这种架构提升了抗审查能力，因为不再需要由单个 relay 存储和提供所有人的内容。即使某个 relay 下线或封禁某个用户，其内容仍然可以从其列出的其他 relays 上获得。

## 为什么重要

NIP-65 把 relay 选择从客户端写死的默认值，变成了用户自己发布的路由元数据。这让客户端能够根据每个账户实际的发布和读取习惯做调整，而不是假设所有人都使用同一组 relays。

与此同时，它也把复杂度转移给了客户端。想把 outbox model 做好，客户端就需要 relay caching、retry logic，以及在 relay list 缺失或陈旧时的 fallback 行为。这个规范改进了可发现性，但并没有消除对良好 relay selection heuristics 的需求。

## 与 Relay Hints 的关系

NIP-65 补充了散布在其他 NIPs 中的 relay hints。当你用 `[["p", "pubkey", "wss://hint.relay"]]` 这样的 tag 指向某人时，这个 hint 会告诉客户端应去哪里查找那条特定引用。NIP-65 提供的是权威的、由用户控制的偏好 relay 列表，而 hints 则是嵌在单个 events 中、用于加速发现的捷径。

在私密消息场景中，NIP-65 还不是全部。公开内容的路由使用 kind 10002，但现代私密消息栈通常还会依赖像 [NIP-17](/zh/topics/nip-17/) 这样的单独 inbox 元数据，以便让用户把 DM 路由与公开发帖 relays 区分开来。

## 最佳实践

保持 relay list 最新，因为那些指向失效 relays 的陈旧条目会让别人更难找到你。至少列出两到三个 relays 以获得冗余，这样当其中一个离线时，你的内容仍然能通过其他 relays 被访问。

不要列出太多 relays。如果你列出了十个或十五个 relays，那么每个想抓取你内容的客户端都必须连接所有这些 relays，这会拖慢它们的体验，并增加整个网络的负载。与其给出一份让所有关注者都背负成本的详尽清单，不如精选三到五个 relay。

把通用 relays 与你使用的专用 relays 混合起来。例如，你可以列出 `wss://relay.damus.io` 这样的通用 relay、一个偏向你所处地区的 relay，以及一个面向某个特定社区的 relay。

---

**主要来源：**
- [NIP-65 Specification](https://github.com/nostr-protocol/nips/blob/master/65.md)

**提及于：**
- [Newsletter #5：NIP Deep Dive](/zh/newsletters/2026-01-13-newsletter/)
- [Newsletter #12：Outbox Model Benchmarks](/zh/newsletters/2026-03-04-newsletter/)
- [Newsletter #19：Wisp inbox-relay broadcasting](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-11：Relay Information](/zh/topics/nip-11/)
- [NIP-17：Private Direct Messages](/zh/topics/nip-17/)
