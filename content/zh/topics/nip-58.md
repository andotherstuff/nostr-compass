---
title: "NIP-58：徽章"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 为 Nostr 定义了一个徽章系统。一个事件定义徽章，另一个授予徽章，第三个让接收者选择是否在其个人资料上展示。

## 工作原理

### 徽章定义（Kind 30009）

发行者创建徽章定义作为可寻址事件：

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### 徽章授予（Kind 8）

发行者向一个或多个用户授予徽章：

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### 徽章展示（Kind 30008）

用户选择在个人资料上展示哪些徽章：

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

在个人资料徽章事件中，客户端应将 `a` 和 `e` 标签作为有序对读取。没有对应授予事件的 `a` 标签，或没有对应徽章定义的 `e` 标签，都应被忽略。

## 用例

- **社区成员资格**：展示群组或社区的成员身份
- **成就**：认可贡献或里程碑
- **证明**：第三方为某个角色或身份做出担保
- **访问控制**：使用发行者支持的徽章来限制功能或空间的访问

## 信任模型

徽章的价值完全取决于发行者的声誉。任何人都可以创建徽章，因此客户端应：

- 显著展示发行者信息
- 允许用户按可信发行者过滤
- 不要在没有上下文的情况下将徽章视为权威

徽章授予是不可变且不可转让的。这使得徽章适用于证明和认可，但不适合作为代币化意义上的可移植凭证。

## 实现说明

徽章定义是可寻址事件，因此发行者可以随时间更新徽章图片或描述，而无需更改徽章标识符。授予事件是将接收者与该定义在某一时间点绑定的持久记录。

客户端在展示方面也有自由度。规范明确允许客户端展示比用户列出的更少的徽章，并选择适合可用空间的缩略图大小。

---

**主要来源：**
- [NIP-58 规范](https://github.com/nostr-protocol/nips/blob/master/58.md)

**提及于：**
- [第7期周刊：Nostr 的五年一月](/zh/newsletters/2026-01-28-newsletter/)
- [第15期周刊：Nostr 的五年二月](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [NIP-51：列表](/zh/topics/nip-51/)
- [Web of Trust](/zh/topics/web-of-trust/)
