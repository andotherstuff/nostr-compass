---
title: "NIP-65：Relay 列表元数据"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 定义了 kind 10002 event，用于公告用户偏好用于读取和写入的 relay。这些元数据帮助其他用户和客户端在分布式 relay 网络中定位您的内容，实现「发件箱模型」来分散负载并提高抗审查能力。

## 结构

Relay 列表是一个可替换 event（kind 10002），包含用户想要公告的每个 relay 的 `r` tag。该 event 会替换来自同一 pubkey 的任何之前的 relay 列表。

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

每个 `r` tag 包含一个 relay WebSocket URL 和一个可选标记，指示用户如何与该 relay 交互。`read` 标记表示用户从该 relay 消费 event，因此其他人应该在那里发布以联系该用户。`write` 标记表示用户发布到该 relay，因此其他人应该在那里订阅以查看该用户的内容。省略标记表示既用于读取也用于写入。

Relay 列表 event 的 `content` 字段为空。

## 发件箱模型

NIP-65 启用了一种称为「发件箱模型」的去中心化内容分发模式。用户不是都发布到同样的中心 relay 并从那里读取，而是发布到自己偏好的 relay，客户端动态发现在哪里找到每个用户的内容。

当 Alice 想找到 Bob 的帖子时，她的客户端首先从任何拥有它的 relay 获取 Bob 的 kind 10002 event。然后她提取 Bob 标记为 `write` 的 relay，因为那些是他发布的地方。她的客户端在那些 relay 订阅 Bob 的 event。当 Alice 想给 Bob 发送私信时，她的客户端反而查找他的 `read` relay 并在那里发布消息。

遵循发件箱模型的客户端维护与关注用户的 NIP-65 event 中列出的 relay 的连接。当它们发现新账户时，它们动态连接到新的 relay。出现在多个关注用户列表中的 relay 会被优先考虑，因为连接到它们可以服务更多用户的社交图谱。

这种架构提高了抗审查能力，因为没有单个 relay 需要存储或服务所有人的内容。如果一个 relay 离线或屏蔽用户，他们的内容仍然可以通过其他列出的 relay 获得。

## 与 Relay 提示的关系

NIP-65 补充了其他 NIP 中的 relay 提示。当您用 `["p", "pubkey", "wss://hint.relay"]` 标记某人时，提示告诉客户端在哪里查找该特定引用。NIP-65 提供权威的、用户控制的偏好 relay 列表，而提示提供嵌入在单个 event 中的快捷方式以便更快发现。

## 最佳实践

保持您的 relay 列表最新，因为指向已停用 relay 的过时条目会使您更难被找到。至少包含两到三个 relay 以提供冗余，这样如果一个 relay 离线，您的内容仍可通过其他 relay 访问。

避免列出太多 relay。当您列出十个或十五个 relay 时，每个想要获取您内容的客户端都必须连接到所有这些，减慢他们的体验并增加整个网络的负载。三到五个精心选择的 relay 的专注列表比给关注您的每个人带来负担的详尽列表更好。

将通用 relay 与您使用的任何专门 relay 混合使用。例如，您可能列出一个流行的通用 relay 如 `wss://relay.damus.io`、一个专注于您所在地理区域的 relay，以及一个您参与的特定社区的 relay。

---

**主要来源：**
- [NIP-65 规范](https://github.com/nostr-protocol/nips/blob/master/65.md)

**相关提及：**
- [Newsletter #5：NIP 深度解析](/zh/newsletters/2026-01-13-newsletter/#nip-65-relay-list-metadata)

**另请参阅：**
- [NIP-11：Relay 信息](/zh/topics/nip-11/)
