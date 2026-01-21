---
title: "Trusted Relay Assertions"
date: 2026-01-21
draft: false
categories:
  - 协议
  - 中继
---

Trusted Relay Assertions 是标准化中继信任评分和声誉管理的 NIP 提案草案。该规范引入 kind 30385 事件，其中断言提供者发布从观察到的指标、运营商声誉和用户报告计算出的信任分数。

## 工作原理

该提案填补了中继生态系统的空白。虽然 [NIP-11](/zh/topics/nip-11/) 定义了中继声称的内容，[NIP-66](/zh/topics/nip-66/) 测量我们观察到的内容，但 Trusted Relay Assertions 标准化了我们对中继可信度的结论。

断言提供者在三个维度上计算分数。可靠性衡量可用性、恢复速度、一致性和延迟。质量评估政策文档、TLS 安全和运营商责任。可访问性评估访问障碍、司法管辖区自由和监视风险。总体信任分数（0-100）结合了这些组件，权重为：40% 可靠性、35% 质量、25% 可访问性。

每个断言都包含基于观察计数的置信水平（低、中、高）。运营商验证使用多种方法：通过签名的 NIP-11 文档进行加密证明、DNS TXT 记录或 .well-known 文件。该规范通过运营商信任分数集成信任网络。政策分类帮助用户找到合适的中继：开放、审核、策展或专门化。

用户通过 kind 10385 事件声明受信任的断言提供者。客户端查询多个提供者并比较分数。该提案包括一个申诉流程，中继运营商可以使用 [NIP-32](/zh/topics/nip-32/) 标签事件对分数提出异议。

## 用例

对于 [NIP-46](/zh/topics/nip-46/) 远程签名器，信任断言帮助用户在接受连接之前评估嵌入在连接 URI 中的不熟悉中继。与 [NIP-65](/zh/topics/nip-65/) 中继列表相结合，客户端可以根据用户偏好和第三方信任评估做出明智的中继选择决策。

该规范补充了现有的中继发现机制。[NIP-66](/zh/topics/nip-66/) 提供发现（存在什么），该提案添加评估（什么是好的）。它们共同支持知情的中继选择，而不是依赖于硬编码的默认值或口碑推荐。

---

**主要来源：**
- [NIP 草案文档](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - 提出规范的 Kind 30817 事件

**提及于：**
- [第 6 期新闻简报：新闻](/zh/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [第 6 期新闻简报：NIP 更新](/zh/newsletters/2026-01-21-newsletter/#nip-updates)

**另见：**
- [NIP-11：中继信息文档](/zh/topics/nip-11/)
- [NIP-66：中继发现和活跃度监控](/zh/topics/nip-66/)
- [NIP-32：标签](/zh/topics/nip-32/)