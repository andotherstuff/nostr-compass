---
title: "NIP-05：域名验证"
date: 2026-02-04
draft: false
description: "NIP-05 通过域名验证为 Nostr 公钥提供人类可读的标识符。"
translationOf: /en/topics/nip-05.md
translationDate: 2026-03-07
categories:
  - Identity
  - Discovery
---

NIP-05 将 Nostr 公钥映射为类似 `user@example.com` 的人类可读互联网标识符。它为用户提供一个基于 DNS 的身份提示，客户端可以通过 HTTPS 进行验证。

## 工作原理

用户通过在其个人资料元数据中添加 `nip05` 字段来声明标识符。标识符格式为 `name@domain`。客户端通过获取 `https://domain/.well-known/nostr.json` 并检查名称是否映射到用户的 pubkey 来验证该声明。

well-known 路径下的 JSON 文件包含一个 `names` 对象，将本地名称映射到 hex pubkey：

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

验证成功后，客户端可以显示该标识符代替 npub 或与 npub 一同显示。某些客户端显示验证指示器，其他客户端则将标识符作为纯文本显示，将信任决定留给读者。

## 信任模型

NIP-05 不是全局用户名注册系统。它证明的是对域名和 Web 服务器路径的控制权，而非法律身份或长期账户延续性。如果域名所有者后来更改了映射，客户端将验证新的映射，除非它们保留了之前的状态。

这使得 NIP-05 对于可发现性和声誉很有用，但比用户通常假设的要弱。良好的客户端应将其视为已验证的域名控制权，而非某人或某组织身份的证明。

## 中继器提示

`nostr.json` 文件可以选择性地包含一个 `relays` 对象，将 pubkey 映射到中继器 URL 数组。这帮助客户端发现在哪里可以找到特定用户的事件。

## 互操作说明

小写要求比表面看起来更重要。混合大小写的名称或 pubkey 可能在某个实现中有效但在另一个中失败，因此当前客户端应该在 `nostr.json` 中使用小写名称和小写 hex 密钥。

另一个实际细节是特殊的 `_` 名称，它让域名可以映射裸标识符形式，如 `_@example.com` 或在支持的客户端中直接显示为 `example.com`。并非每个客户端都以相同方式展示该形式，因此用户使用显式的 `name@domain` 标识符仍能获得最一致的结果。

## 实现状态

大多数主要客户端支持 NIP-05 验证：
- Damus、Amethyst、Primal 显示已验证的标识符
- 许多中继器服务提供 NIP-05 标识符作为功能
- 存在众多免费和付费的 NIP-05 提供商

---

**主要来源：**
- [NIP-05 规范](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - 名称和 hex 密钥的小写要求

**提及于：**
- [第8期周刊：NIP 更新](/zh/newsletters/2026-02-04-newsletter/#nip-updates)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
- [NIP-65：中继器列表元数据](/zh/topics/nip-65/)
