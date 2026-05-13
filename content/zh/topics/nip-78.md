---
title: "NIP-78：应用专属数据"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78定义了一种标准事件kind，使应用程序能够代表用户使用Nostr事件存储任意数据，在无需中央服务器的情况下实现跨设备状态同步。

## 工作原理

核心事件kind为30078，是一种参数化可替换事件。`d`标签是应用程序定义的标识符字符串，将存储槽限定为特定应用程序和目的。

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

应用程序发布一个带有唯一`d`标签（例如`tamagostrich-pet-state`或`amethyst-settings`）的30078事件以及需要持久化的JSON或文本内容。由于30078是可替换的且通过`d`标签进行范围限定，更新存储状态意味着发布具有相同`d`标签的新事件，中继仅保留最新版本。

## 跨设备同步

任何知道用户公钥和应用程序`d`标签的客户端都可以从用户的中继集合中获取当前状态并在任何设备上重建。用户拥有数据，因为数据存在于用其密钥对签名的事件中，存储在其[NIP-65](/zh/topics/nip-65/)中继列表中的中继上。

## 私有数据与公开数据

对于私有应用程序数据，可以在发布前使用[NIP-44](/zh/topics/nip-44/)对内容字段进行加密，这样中继只存储密钥持有者才能解密的密文。公开应用程序数据可以不加密存储，以便其他客户端读取和显示。

## 内容格式

NIP-78有意将内容格式保持开放，应用程序选择自己的架构。常见惯例是在`d`标签前加上应用程序名称前缀，以防止使用同一中继的应用之间发生冲突。

## 实现

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — 通过`tamagostrich-pet-state` kind:30078事件实现跨设备宠物状态同步
- [Wisp](https://github.com/barrydeen/wisp-android) — kind:30078钱包备份和跨设备安全设置同步；使用NIP-78作者过滤器将出站订阅合并为单个REQ
- [NosPress](https://github.com/nostrapps/nospress) — 存储在NIP-78事件中的CMS编排状态
- 多个Nostr客户端设置同步实现（Amethyst等）

---

**主要来源：**
- [NIP-78规范](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — 生产实现

**提及于：**
- [新闻通讯#22：NIP-78深度解析](/zh/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [新闻通讯#22：Tamagostrich](/zh/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**另见：**
- [NIP-51：列表](/zh/topics/nip-51/)
- [NIP-44：版本化加密](/zh/topics/nip-44/)
- [NIP-65：中继列表元数据](/zh/topics/nip-65/)
