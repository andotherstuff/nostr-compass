---
title: "NIP-58：徽章"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 为 Nostr 定义了一个徽章系统，允许发行者创建徽章并授予用户，用户可以在其个人资料上展示这些徽章。

## 工作原理

### 徽章定义 (Kind 30009)

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

### 徽章授予 (Kind 8)

发行者向用户授予徽章：

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### 徽章展示 (Kind 30008)

用户选择在其个人资料上展示哪些徽章：

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

## 用例

- **社区成员资格**：证明群组或社区的成员身份
- **成就**：认可贡献或里程碑
- **验证**：第三方证明（员工、创作者等）
- **访问控制**：根据徽章所有权限制内容或功能

## 信任模型

徽章的价值完全取决于发行者的声誉。任何人都可以创建徽章，因此客户端应该：
- 显著展示发行者信息
- 允许用户按可信发行者过滤
- 不要在没有上下文的情况下将徽章视为权威

## 相关

- [NIP-51](/zh/topics/nip-51/) - 列表
- [Web of Trust](/zh/topics/web-of-trust/)
