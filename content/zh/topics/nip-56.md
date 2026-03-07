---
title: "NIP-56：举报"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 定义了 kind `1984` 举报事件。它允许用户和应用发布关于账户、笔记和 blob 的审核信号，而无需单一共享的审核权威机构。

## 工作原理

举报必须包含一个 `p` 标签，指向被举报的公钥。如果举报针对特定事件，还必须包含该事件的 `e` 标签。举报类型作为相关 `p`、`e` 或 `x` 标签的第三个值出现。

## 举报类别

- **nudity**：成人内容
- **malware**：病毒、木马、勒索软件及类似载荷
- **profanity**：冒犯性语言和仇恨言论
- **illegal**：可能违反法律的内容
- **spam**：不需要的重复消息
- **impersonation**：欺诈性身份声明
- **other**：不符合上述类别的违规行为

Blob 举报使用 `x` 标签附带 blob 哈希值，还可以包含指向托管端点的 `server` 标签。这使得 NIP-56 不仅可用于笔记和个人资料的审核，也可用于媒体审核。

## 安全与信任模型

举报是信号，不是裁决。客户端可以利用社交信任、审核列表或明确的审核者角色来对其加权。中继也可以读取举报，但规范警告不要完全自动化审核，因为举报容易被恶意利用。

可以通过 NIP-32 的 `l` 和 `L` 标签添加额外分类，当客户端需要比基础七种举报类型更细粒度的审核词汇时，这很有用。

---

**主要来源：**
- [NIP-56 规范](https://github.com/nostr-protocol/nips/blob/master/56.md)

**提及于：**
- [第10期周刊：项目更新](/zh/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**另请参阅：**
- [NIP-22：评论](/zh/topics/nip-22/)
