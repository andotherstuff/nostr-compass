---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - 信任
  - 社交图谱
---

Web of Trust（WoT）是一种去中心化信任模型，其中声誉和可信度来源于社交图谱关系，而非中央机构。

## 工作原理

在Nostr中，Web of Trust利用关注图谱（NIP-02联系人列表）和举报事件来计算信任分数：

1. **图谱构建**：从pubkey、事件及其关系（关注、静音、举报）构建有向图
2. **权重分配**：为已知可信的pubkey（例如具有已验证NIP-05标识符的）分配初始权重
3. **迭代传播**：使用类似PageRank的算法，信任分数在网络中流动
4. **Sybil抵抗**：如果攻击者创建许多虚假账户，传递给它们的信任会被虚假数量除以

## 关键特性

- **去中心化**：没有中央机构决定声誉
- **个性化**：可以根据每个用户关注的人从其角度计算信任
- **Sybil抵抗**：由于信任稀释，机器人农场无法轻易操纵系统
- **可组合**：可应用于垃圾邮件过滤、内容审核、relay准入和支付目录

## Nostr中的应用

- **垃圾邮件过滤**：relay可以使用WoT过滤低信任内容
- **内容发现**：展示来自您网络信任的账户的内容
- **支付目录**：带有冒充防护的Lightning地址查询
- **Relay策略**：WoT relay仅接受来自受信任pubkey的笔记
- **去中心化审核**：社区可以根据信任分数进行策展

## 实现

多个项目为Nostr实现了Web of Trust：
- **Nostr.Band Trust Rank**：网络的PageRank风格评分
- **WoT Relays**：按社交距离过滤的relay
- **DCoSL**：去中心化声誉系统协议
- **Noswot**：基于关注和举报的信任评分

---

**主要来源：**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL协议](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**提及于：**
- [Newsletter #3: 十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-02: 关注列表](/zh/topics/nip-02/)
