---
title: "NIP-56：举报"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 使用 kind 1984 event 定义了举报机制，允许用户和应用在 Nostr 网络中对不当内容进行举报标记。

## 工作方式

用户发布一个带有 `p` tag（引用被举报 pubkey）的 kind 1984 event。举报特定笔记时，`e` tag 引用笔记 ID。两种 tag 都接受第三个参数来指定违规类别。

## 举报类别

- **nudity**：成人内容
- **malware**：病毒、木马、勒索软件
- **profanity**：冒犯性语言和仇恨言论
- **illegal**：可能违反法律的内容
- **spam**：不需要的重复消息
- **impersonation**：欺诈性身份声明
- **other**：不符合上述类别的违规行为

## 客户端和 Relay 行为

客户端可以使用来自关注用户的举报进行内容管理决策，例如当多个受信任的联系人标记内容时对其进行模糊处理。Relay 应避免通过举报进行自动内容管理，以防被恶意利用；可信版主的举报可用于指导人工执法。通过 NIP-32 的 `l` 和 `L` tag 支持额外的分类。

---

**主要来源：**
- [NIP-56 规范](https://github.com/nostr-protocol/nips/blob/master/56.md)

**提及于：**
- [Newsletter #10：项目更新](/zh/newsletters/2026-02-18-newsletter/#notedeck android-应用商店准备工作)

**另请参见：**
- [NIP-22：评论](/zh/topics/nip-22/)
