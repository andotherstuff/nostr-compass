---
title: "NIP-98：HTTP Auth"
date: 2026-03-25
translationOf: /en/topics/nip-98.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 认证
---

NIP-98 定义了使用 Nostr event 进行 HTTP 认证。它允许服务器在标准 HTTP 请求上验证客户端的 Nostr 身份，而无需密码、API 密钥或 OAuth 流程。

## 工作原理

当客户端需要认证 HTTP 请求时，它创建一个 kind 27235 event。该 event 在其 tag 中包含目标 URL 和 HTTP 方法，将认证绑定到特定请求。

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1742860800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

客户端签署此 event，对其进行 base64 编码，并在 HTTP `Authorization` 头中以 `Nostr` 方案发送：

```
Authorization: Nostr <base64-encoded-signed-event>
```

服务器解码 event，验证签名，检查 URL 和方法是否与实际请求匹配，并确认时间戳是近期的。如果所有检查通过，服务器即知道哪个 Nostr pubkey 发出了该请求。

可选的 `payload` tag 包含请求体的 SHA-256 哈希，防止 auth event 被用于不同的内容。时间戳检查（服务器通常拒绝几分钟前的 event）防止重放攻击。

## 使用场景

Blossom 服务器使用 NIP-98 对文件上传和删除进行认证，将存储的媒体与特定 Nostr 身份绑定。文件托管服务使用它来执行每个 pubkey 的上传配额。任何需要识别 Nostr 用户而无需维护自身账户系统的 HTTP API 都可以接受 NIP-98 头作为身份证明。

---

**主要来源：**
- [NIP-98 规范](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**提及于：**
- [周刊 #15](/zh/newsletters/2026-03-25-newsletter/)
