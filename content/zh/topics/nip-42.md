---
title: "NIP-42：客户端对中继的身份验证"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 定义了客户端如何向中继进行身份验证。中继可以要求身份验证以提供访问控制、防止滥用或实现付费中继服务。

## 工作原理

身份验证流程始于中继向客户端发送 AUTH 消息。此消息包含客户端必须签名的挑战字符串。客户端创建包含挑战的 kind 22242 身份验证事件，并用其私钥签名。中继验证签名和挑战，然后授予访问权限。

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

挑战防止重放攻击：客户端必须为每次身份验证尝试签署新的挑战。标签中的中继 URL 确保身份验证令牌不能在不同中继之间重复使用。

## 用例

付费中继使用 NIP-42 在授予访问权限之前验证订阅者。身份验证后，中继可以检查支付状态或订阅到期时间。私有中继限制访问已批准的 pubkey，创建封闭社区或个人中继基础设施。

通过身份验证，速率限制变得更加有效。中继可以按已验证的 pubkey 而不是按 IP 地址跟踪请求速率，在支持共享 IP 后面的合法用户的同时防止滥用。当中继要求身份验证才能发布事件时，垃圾信息预防得到改善。

一些中继使用 NIP-42 进行分析，跟踪哪些用户访问哪些内容，而无需集中式账户。结合 [NIP-11](/zh/topics/nip-11/) 元数据，客户端在尝试连接之前发现中继是否需要身份验证。

---

**主要来源：**
- [NIP-42 规范](https://github.com/nostr-protocol/nips/blob/master/42.md) - 客户端对中继的身份验证

**另请参阅：**
- [NIP-11：中继信息文档](/zh/topics/nip-11/)
- [NIP-50：搜索功能](/zh/topics/nip-50/)
