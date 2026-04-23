---
title: "NIP-42：客户端对 Relay 的认证"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 定义了客户端如何向 relays 进行认证。relays 可以借此实现访问控制、阻止滥用，或构建付费 relay 服务。

## 工作原理

认证流程从 relay 向客户端发送 `AUTH` 消息开始。该消息包含一个 challenge 字符串，客户端必须对其签名。客户端随后创建一个 kind 22242 的认证 event，把 challenge 放进去并使用自己的私钥签名，relay 验证签名和 challenge 之后再授予访问权限。

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

challenge 用于防止重放攻击，而 tags 中的 relay URL 则阻止同一个已签名 event 被复用到其他 relays。

## 协议说明

认证是连接级的。一个 challenge 在该连接存续期间有效，或者直到 relay 再发来新的 challenge 为止。这个已签名 event 本身是临时性的，不应像普通 event 那样被广播出去。

规范还定义了机器可读的错误前缀。`auth-required:` 表示客户端尚未完成认证；`restricted:` 表示已经认证，但该 pubkey 仍然没有执行请求操作的权限。

## 使用场景

付费 relays 会利用 NIP-42 验证订阅者再授予访问权限。私有 relays 则用它来限制哪些 pubkeys 可以读或写。它也让限流变得更有效，因为 relays 可以按已认证 key 而不是按 IP 地址来追踪行为。

结合 [NIP-11](/zh/topics/nip-11/) 元数据，客户端可以在尝试受保护查询之前先发现某个 relay 是否支持 NIP-42。现实中支持仍不均匀，所以当 relay 虽然声称支持 NIP-42，却错误处理受保护 events 时，客户端仍需要准备回退路径。

---

**主要来源：**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**提及于：**
- [Newsletter #6：Relay Information Documents](/zh/newsletters/2026-01-21-newsletter/)
- [Newsletter #9：Marmot Relay Status Testing](/zh/newsletters/2026-02-11-newsletter/)
- [Newsletter #10：Nostr MCP Server](/zh/newsletters/2026-02-18-newsletter/)
- [Newsletter #13：Relay AUTH Starts Reaching Real Apps](/en/newsletters/2026-03-11-newsletter/)

**另请参阅：**
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
- [NIP-50：搜索能力](/zh/topics/nip-50/)
