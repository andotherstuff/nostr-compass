---
title: "NIP-19：Bech32 编码实体"
date: 2025-12-17
translationOf: /en/topics/nip-19.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 定义了用于分享 Nostr 标识符的人类友好格式。这些 bech32 编码字符串用于显示和分享，但从不在协议本身中使用（协议使用 hex）。

## 工作原理

原始 hex 密钥容易出错且在视觉上难以区分。Bech32 编码添加了人类可读的前缀和校验码，使你能清楚地知道你在看什么类型的数据，并能捕获许多复制错误。

基础形式编码单个 32 字节值：

- **npub** - 公钥（你的身份，可以安全分享）
- **nsec** - 私钥（保持秘密，用于签名）
- **note** - 事件 ID（引用特定事件）

示例：hex 公钥 `3bf0c63f...` 变为 `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`。

扩展形式使用 TLV 编码，以便在标识符本身旁边携带查找提示：

- **nprofile** - 带 relay 提示的个人资料
- **nevent** - 带 relay 提示、作者公钥和 kind 的事件
- **naddr** - 带公钥、kind、`d` 标签和 relay 提示的可寻址事件引用

## 重要意义

relay 提示不具有权威性，但它们通常决定了客户端能否在第一次尝试时获取到共享的事件。这就是为什么当内容不在接收者当前的 relay 集合中时，`nevent`、`nprofile` 和 `naddr` 通常比裸 `note` 或 `npub` 值更好的分享格式。

另一个实用的区别是稳定性。`note` 指向一个不可变的事件 ID，而 `naddr` 指向一个可以随时间替换的可寻址事件。对于长文内容、日历或仓库公告，`naddr` 通常是正确的链接类型。

## 实现说明

- 仅在人类界面中使用 bech32：显示、复制/粘贴、二维码、URL
- 永远不要在协议消息、事件或 NIP-05 响应中使用 bech32 格式
- 所有协议通信必须使用 hex 编码
- 生成 nevent/nprofile/naddr 时，包含 relay 提示以提高可发现性
- 在所有地方将 `nsec` 视为机密材料。客户端不应默认显示它，不应记录它，也不应将其包含在支持导出中

---

**主要来源：**
- [NIP-19 规范](https://github.com/nostr-protocol/nips/blob/master/19.md)

**提及于：**
- [第1期周刊：NIP 深度解析](/zh/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [第3期周刊：12月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [第3期周刊：重要代码变更](/zh/newsletters/2025-12-31-newsletter/#damus-ios)
- [第4期周刊：relay 提示支持](/zh/newsletters/2026-01-07-newsletter/)
- [第8期周刊：Damus iOS](/zh/newsletters/2026-02-04-newsletter/#damus-ios)
- [第11期周刊：notecrumbs](/zh/newsletters/2026-02-25-newsletter/)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
- [NIP-10：回复线程](/zh/topics/nip-10/)
