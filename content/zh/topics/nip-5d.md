---
title: "NIP-5D：Nostr Web Applets"
date: 2026-04-08
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - 应用
---

NIP-5D 为运行在 iframe 中的沙箱化 Web 应用（“napplets”）定义了一套 `postMessage` 协议，用来与宿主应用（“shell”）通信。它在 [NIP-5A](/zh/topics/nip-5a/)（静态网站）的基础上增加了运行时通信层，让 Web app 可以使用 Nostr 功能，同时不暴露用户私钥。

## 工作原理

shell 应用会在一个沙箱 iframe 中加载 napplet。napplet 通过浏览器的 `postMessage` API，使用结构化消息协议与 shell 通信。shell 通过这条消息通道向 napplet 提供 Nostr 签名、relay 访问和用户上下文。iframe 沙箱会阻止 napplet 直接访问用户私钥，因此所有 Nostr 操作都由 shell 充当把关者。

## 使用场景

- **交互式 Nostr 应用**：构建可读写 Nostr events 的应用，而无需让用户粘贴自己的 nsec
- **应用市场**：通过 Nostr events 分发交互式 Web 应用
- **沙箱扩展**：让第三方 napplet 为 Nostr 客户端增加功能

---

**主要来源：**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Nostr Web Applets 提案

**提及于：**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)

**另请参阅：**
- [NIP-5A（静态网站）](/zh/topics/nip-5a/)
- [NIP-5C（Scrolls）](/zh/topics/nip-5c/)
