---
title: "NIP-42：客户端到中继的身份验证"
date: 2026-01-21
draft: false
translationOf: /en/topics/nip-42.md
translationDate: 2026-03-07
categories:
  - NIPs
  - Authentication
---

NIP-42 定义了客户端向中继进行身份验证的方式。中继可以要求身份验证以提供访问控制、防止滥用或实现付费中继服务。

## 工作原理

身份验证流程始于中继向客户端发送 `AUTH` 消息。该消息包含一个质询字符串，客户端必须对其进行签名。客户端创建一个包含质询的 kind 22242 身份验证事件，并用私钥签名。中继验证签名和质询后授予访问权限。

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

质询可以防止重放攻击。标签中的中继 URL 可以防止同一个签名事件在不同中继上被重用。

## 协议说明

身份验证的作用范围是连接级别的。质询在连接持续期间保持有效，或直到中继发送新的质询。签名事件是临时的，不得作为普通事件广播。

规范还定义了机器可读的错误前缀。`auth-required:` 表示客户端尚未进行身份验证。`restricted:` 表示客户端已完成身份验证，但该公钥仍然没有执行所请求操作的权限。

## 用例

付费中继使用 NIP-42 在授予访问权限前验证订阅者身份。私有中继使用它将读写权限限制在经批准的公钥范围内。它还改善了速率限制，因为中继可以按经过身份验证的密钥而非 IP 地址来追踪行为。

结合 [NIP-11](/zh/topics/nip-11/) 元数据，客户端可以在尝试受保护的查询之前发现中继是否支持 NIP-42。实际上，支持程度仍然参差不齐，因此当中继声称支持 NIP-42 但对受保护事件处理不正确时，客户端需要有回退方案。

---

**主要来源：**
- [NIP-42 规范](https://github.com/nostr-protocol/nips/blob/master/42.md) - 客户端到中继的身份验证

**提及于：**
- [Newsletter #6：中继信息文档](/zh/newsletters/2026-01-21-newsletter/#relay-information-documents-get-formalized)
- [Newsletter #9：Marmot 中继状态测试](/zh/newsletters/2026-02-11-newsletter/#nip-70-relay-support-critical-for-encrypted-messaging-security)
- [Newsletter #10：Nostr MCP 服务器](/zh/newsletters/2026-02-18-newsletter/#nostr-mcp-server)

**另请参阅：**
- [NIP-11：中继信息文档](/zh/topics/nip-11/)
- [NIP-50：搜索功能](/zh/topics/nip-50/)
