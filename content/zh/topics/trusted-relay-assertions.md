---
title: "可信中继断言"
date: 2026-01-21
draft: false
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-03-07
categories:
  - Protocol
  - Relays
---

可信中继断言是在 Nostr 上发布经签名的第三方中继评估的理念，使客户端在选择中继时能获得比仅靠自行报告的元数据更多的上下文。当前标准化的构建模块是 [NIP-85：可信断言](/zh/topics/nip-85/)，它定义了用户如何信任提供者以及提供者如何发布签名的计算结果。

## 工作原理

中继选择分为三个层次。[NIP-11：中继信息文档](/zh/topics/nip-11/) 涵盖中继关于自身的声明。[NIP-66：中继发现和存活监测](/zh/topics/nip-66/) 涵盖观察者可以测量的内容，如可用性和延迟。可信中继断言试图填补剩余的空白：第三方从这些数据中得出的结论，以及客户端是否决定信任该结论。

在更广泛的 NIP-85 模型中，用户通过 kind `10040` 事件指定可信提供者，提供者发布签名的可寻址断言事件。中继评分应用还需要客户端认可的另外两个要素：如何标识作为评估对象的中继，以及哪些结果标签代表分数及其支撑证据。

这种区分很重要，因为传输和信任委托已经标准化，但中继特定的评分模型仍然是应用层模式。不同提供者可以在什么使中继值得信任这个问题上持有合理的不同意见。

## 信任模型

中继信任分数不是客观事实。一个提供者可能优先考虑正常运行时间和写入吞吐量，另一个可能优先考虑法律管辖区、审核政策或运营者身份，第三个可能最关心对监控的抵抗力。有用的客户端应该显示谁生成了分数，而不仅仅是分数本身。

这也是[信任网络](/zh/topics/web-of-trust/)进入视野的地方。如果客户端已经信任某些人或服务，它可以优先选择来自同一社交圈的中继评估，而非假装存在单一的全局排名。

## 重要意义

对于 [NIP-46](/zh/topics/nip-46/) 远程签名者、钱包连接或任何建议使用不熟悉中继的应用，第三方中继评估可以减少对默认设置的盲目信任。结合 [NIP-65](/zh/topics/nip-65/) 中继列表，客户端可以将"我使用哪些中继"与"我信任哪些中继执行此任务"分开。

主要的准确性说明是范围。2026 年 1 月的 Newsletter 报道将中继信任评分描述为专门提案，但 NIPs 仓库中合并的标准是更广泛的 [NIP-85：可信断言](/zh/topics/nip-85/) 格式。中继评分仍然是建立在该模型之上的用例，而非单独的已定稿中继信任协议格式。

---

**主要来源：**
- [NIP-85 规范](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534：可信断言](https://github.com/nostr-protocol/nips/pull/1534)

**提及于：**
- [Newsletter #6：新闻](/zh/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6：NIP 更新](/zh/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #7：NIP 更新](/zh/newsletters/2026-01-28-newsletter/#nip-updates)

**另请参阅：**
- [NIP-11：中继信息文档](/zh/topics/nip-11/)
- [NIP-66：中继发现和存活监测](/zh/topics/nip-66/)
- [NIP-85：可信断言](/zh/topics/nip-85/)
- [信任网络](/zh/topics/web-of-trust/)
