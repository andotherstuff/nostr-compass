---
title: "NIP-FE 提案：HTTP relay 命令"
date: 2026-09-30
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Relays
---

Amethyst 在其 Geode relay 和 Quartz 客户端工作中，用临时标签 NIP-FE 指代通过 HTTP 传输的 relay 命令。该标签不是已分配的 NIP，也不能证明它已在 Nostr relay 中被广泛采用。

## 传输方式 {#transport}

客户端不再建立 WebSocket 连接，而是向 relay 的 HTTP 端点提交一个 `REQ`、`COUNT` 或 `EVENT` 帧。响应以换行分隔的 JSON 流式返回 relay 帧。客户端必须区分完整的应答和被截断的流，而需要认证的请求仍使用经过签名的 Nostr HTTP 授权。这种传输方式改变的是命令到达 relay 的途径；它不会改变底层的 event 签名或 event 内容。

Amethyst 的[已合并实现](https://github.com/vitorpamplona/amethyst/pull/4231)加入了 Geode 路由、Quartz 客户端支持、请求体和并发限制，以及针对帧格式和授权的测试。这是源代码层面的实现证据，并不能证明独立的 relay 已实现同一提案。

## 命名冲突 {#naming-collision}

[NIPs 仓库中一个无关的草案 pull request](https://github.com/nostr-protocol/nips/pull/2488) 也使用了 **NIP-FE**，这次指的是建立在拟议多接收者信封之上的私有 feed。该工作仍处于开放状态，所描述的问题与 Amethyst 的 HTTP 传输不同。两种临时用法都不能证明该标签已被分配给某个已接受的规范；读者应根据来源和主题来识别所指的提案。

---

**主要来源：**
- [Amethyst Geode 和 Quartz 实现 PR](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Amethyst 仓库](https://github.com/vitorpamplona/amethyst)
- [同样使用 NIP-FE 的开放私有 feed 草案](https://github.com/nostr-protocol/nips/pull/2488)

**提及于：**
- [第42期周刊：Amethyst relay 命令](/zh/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
