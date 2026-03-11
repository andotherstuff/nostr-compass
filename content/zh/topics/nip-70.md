---
title: "NIP-70：受保护事件"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 中继
  - 访问控制
---

NIP-70 定义了一种让作者用简单标签 `[["-"]]` 将事件标记为受保护事件的方法。只有当 relay 选择支持这种行为，并验证已通过身份验证的发布者与事件作者是同一个 pubkey 时，这类受保护事件才会被接受。

## 工作原理

核心规则很短。如果一个事件包含 `[["-"]]` 标签，relay 默认应拒绝它。想要支持受保护事件的 relay，必须先执行 [NIP-42](/zh/topics/nip-42/) `AUTH` 流程，并确认完成身份验证的客户端发布的是它自己的事件。

这意味着 NIP-70 约束的是发布权限，而不是加密规则。内容本身仍然可以被读取。变化的是，谁有权把这个事件放到遵守该标签的 relay 上。这让 relay 可以支持半封闭信息流，以及其他作者希望 relay 拒绝第三方再发布的场景。

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## AUTH 流程影响

只有 relay 真正在发布时强制执行作者身份，受保护事件才有意义。这也是 NIP-70 如此依赖 [NIP-42](/zh/topics/nip-42/) 的原因。一个 relay 如果接受 `[["-"]]` 事件，却不做匹配的身份验证检查，那么它只是把这个标签当作装饰，而不是策略。

## relay 行为与限制

NIP-70 并不保证内容永远不会扩散。任何接收者仍然可以复制自己看到的内容，并在别处发布新事件。这个规范只是为 relay 提供了一种标准化方式，让它们尊重作者意图，拒绝对受保护事件进行直接再发布。

这也是为什么后续工作很重要。[PR #2251](https://github.com/nostr-protocol/nips/pull/2251) 将这一规则扩展到嵌入受保护事件的 repost，堵上了一个显而易见的绕过路径，即原始事件仍然受保护，但包装它的 repost 并未受保护。

## 实现

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - 为受保护事件增加基于 NIP-42 的身份验证支持
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - 拒绝嵌入受保护事件的 repost
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - 增加与受保护事件处理相关的辅助支持

---

**主要来源：**
- [NIP-70 规范](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - 将 NIP-70 加入 NIPs 仓库
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - 拒绝嵌入受保护事件的 repost
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - 面向 NIP-42 身份验证和受保护事件的 relay 实现

**提及于：**
- [Newsletter #13：NIP 更新](/zh/newsletters/2026-03-11-newsletter/#nip-更新)
- [Newsletter #13：NIP 深度解析](/zh/newsletters/2026-03-11-newsletter/#nip-深度解析nip-70受保护事件)

**另请参阅：**
- [NIP-42：客户端身份验证](/zh/topics/nip-42/)
- [NIP-11：relay 信息文档](/zh/topics/nip-11/)
