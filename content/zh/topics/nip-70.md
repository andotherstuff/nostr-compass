---
title: "NIP-70：受保护事件"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - Relay
  - 访问控制
---

NIP-70 定义了一种方式，让作者使用简单的 tag `[["-"]]` 将 event 标记为受保护。受保护的 event 只有在 relay 选择支持此行为并验证认证发布者与 event 作者是同一 pubkey 时才会被接受。

## 工作原理

核心规则很简短。如果一个 event 包含 `[["-"]]` tag，relay 应默认拒绝它。想要支持受保护事件的 relay 必须先运行 [NIP-42](/zh/topics/nip-42/) `AUTH` 流程，确认认证的客户端正在发布自己的 event。

这使得 NIP-70 成为一种发布权限规则，而非加密规则。内容仍然可以是可读的。改变的是谁能将该 event 放置到遵守此 tag 的 relay 上。这让 relay 能够支持半封闭信息流和其他作者希望 relay 拒绝第三方重新发布的场景。

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

受保护事件仅在 relay 在发布时实际执行作者身份验证时才有用。这就是为什么 NIP-70 如此直接依赖 [NIP-42](/zh/topics/nip-42/)。接受 `[["-"]]` event 而不进行匹配 auth 检查的 relay 是将该 tag 当作装饰而非策略。

## Relay 行为与限制

NIP-70 不承诺内容将永远保持封闭。任何接收者仍然可以复制他们看到的内容并在其他地方发布新 event。该规范只是给 relay 提供了一种标准方式来尊重作者意图并拒绝直接重新发布受保护事件。

这就是后续工作的重要之处。[PR #2251](https://github.com/nostr-protocol/nips/pull/2251) 将规则扩展到嵌入受保护事件的转发，关闭了原始 event 受保护但包装 event 未受保护的简单绕过方式。

## 实现

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - 为受保护事件添加 NIP-42 auth 支持
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - 拒绝嵌入受保护事件的转发
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - 添加与受保护事件处理相关的辅助支持

---

**主要来源：**
- [NIP-70 规范](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - 将 NIP-70 添加到 NIPs 仓库
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - 拒绝嵌入受保护事件的转发
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - NIP-42 auth 和受保护事件的 relay 实现

**提及于：**
- [周刊 #13：NIP 更新](/en/newsletters/2026-03-11-newsletter/#nip-updates)
- [周刊 #13：NIP 深度解析](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**另见：**
- [NIP-42：客户端认证](/zh/topics/nip-42/)
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
