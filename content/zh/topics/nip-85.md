---
title: "NIP-85：Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-02-18
draft: false
categories:
  - Protocol
  - Relays
---

NIP-85 定义了一个将耗时计算委托给可信服务提供商的系统，这些提供商以签名的 Nostr event 形式发布计算结果。Web of Trust 评分和互动指标需要爬取大量 relay 并处理海量 event 数据，这在移动设备上是不切实际的。

## 工作方式

NIP-85 使用四种 event kind 对不同主题类型进行断言：

- **Kind 30382**：用户断言，携带关注者数量、帖子/回复/反应数量、zap 金额、标准化排名（0-100）、常见话题和活跃时段
- **Kind 30383**：event 断言，对单条笔记评分，包含评论数、引用数、转发数、反应数和 zap 数据
- **Kind 30384**：将相同的互动指标整体应用于可寻址 event（长文章、wiki 页面）的所有版本
- **Kind 30385**：对通过 [NIP-73](/zh/topics/nip-73/)（外部内容 ID）引用的外部标识符（书籍、电影、网站、地点、话题标签）进行评分

每个断言都是一个可替换的可寻址 event，其中 `d` tag 包含主题：pubkey、event ID、event 地址或 NIP-73 标识符。服务提供商用自己的密钥对这些 event 签名，客户端根据信任关系评估。

## 提供商发现

用户通过发布 kind 10040 event 声明其信任的断言提供商。每个条目指定断言类型，包含提供商 pubkey 和 relay 提示，以及可选的算法变体。用户可以使用 [NIP-44](/zh/topics/nip-44/) 加密提供商列表以保持偏好私密。

客户端通过检查关注账号所信任的提供商来构建提供商列表，为断言提供商本身创建去中心化的声誉层。

## 安全模型

提供商必须为不同算法使用不同的服务密钥，当算法个性化时每个用户使用唯一密钥，防止跨用户查询的交叉关联。每个服务密钥配有描述算法行为的 kind 0 元数据 event，让用户了解其所信任的内容。

## 当前采用情况

NIP-85 将一种已非正式出现的模式正式化。Primal 的缓存服务器计算互动指标和 Web of Trust 评分。[Antiprimal](https://gitlab.com/soapbox-pub/antiprimal) 使用 NIP-85 event kind 将这些计算桥接到标准 Nostr 客户端。[Nostr.band](https://nostr.band) 运营着规范示例中引用的 `wss://nip85.nostr.band` relay。[Amethyst](https://github.com/vitorpamplona/amethyst) 在其 `quartz` 库中有实验性的 Trusted Assertions 支持。

---

**主要来源：**
- [NIP-85 规范](https://github.com/nostr-protocol/nips/blob/master/85.md)

**提及于：**
- [Newsletter #10：NIP 深入解析](/zh/newsletters/2026-02-18-newsletter/#nip-深入解析nip-85trusted-assertions)
- [Newsletter #10：NIP 更新](/zh/newsletters/2026-02-18-newsletter/#nip-更新)

**另请参见：**
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
- [NIP-73：外部内容 ID](/zh/topics/nip-73/)
