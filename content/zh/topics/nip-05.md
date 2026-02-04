---
title: "NIP-05 (域名验证)"
date: 2026-02-04
description: "NIP-05 通过域名验证为 Nostr 公钥提供人类可读的标识符。"
---

NIP-05 将 Nostr 公钥映射到类似 `user@example.com` 的人类可读互联网标识符。这提供了一种通过域名所有权验证身份的方式，而无需信任中心化权威机构。

## 工作原理

用户通过在其个人资料元数据中添加 `nip05` 字段来声明标识符。标识符遵循 `name@domain` 格式。客户端通过获取 `https://domain/.well-known/nostr.json` 并检查该名称是否映射到用户的 pubkey 来验证声明。

位于 well-known 路径的 JSON 文件包含一个 `names` 对象，将本地名称映射到十六进制 pubkey：

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

当验证成功时，客户端可以显示标识符来替代或伴随 npub 显示。某些客户端会为已验证的标识符显示勾选标记或其他指示符。

## 中继提示

`nostr.json` 文件可以选择性地包含一个 `relays` 对象，将 pubkey 映射到中继 URL 数组。这有助于客户端发现从哪里获取特定用户的事件。

## 实现

大多数主流客户端支持 NIP-05 验证：
- Damus、Amethyst、Primal 显示已验证的标识符
- 许多中继服务提供 NIP-05 标识符作为功能
- 存在众多免费和付费的 NIP-05 提供商

## 主要来源

- [NIP-05 规范](https://github.com/nostr-protocol/nips/blob/master/05.md)

## 相关提及

- [Newsletter #8 (2026-02-04)](/zh/newsletters/2026-02-04-newsletter/) - 要求十六进制密钥和名称使用小写的 PR
