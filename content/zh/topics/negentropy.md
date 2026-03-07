---
title: "Negentropy：集合协调协议"
date: 2026-01-28
draft: false
translationOf: /en/topics/negentropy.md
translationDate: 2026-03-07
categories:
  - Protocol
  - Sync
---

Negentropy 是一种集合协调协议，用于确定双方各自拥有而对方缺少的事件，无需重新发送完整数据集。

## 工作原理

Negentropy 不是请求与过滤器匹配的所有事件，而是比较两个有序集合，仅定位到存在差异的范围。协议交换紧凑的范围摘要，仅在必要时才回退到显式 ID 列表。

1. **排序**：双方按时间戳排序记录，时间戳相同则按 ID 排序
2. **范围比较**：双方交换记录范围的指纹
3. **细化**：不匹配的范围被拆分，直到确定实际缺失的 ID

## 重要意义

传统 Nostr 同步使用基于时间戳的 `since` 过滤器，可能因以下原因遗漏事件：
- 客户端与中继器之间的时钟偏差
- 多个事件具有相同的时间戳
- 事件乱序到达

Negentropy 通过比较实际事件集合而非依赖时间戳来解决这些问题。

## 实际应用

- **私信恢复**：客户端可以检测并获取缺失的私信，即使这些消息具有较旧的时间戳
- **信息流同步**：确保跨中继器的完整时间线同步
- **离线同步**：在断线后高效追赶更新

一个值得关注的实现细节是，许多客户端并不用 Negentropy 替代普通订阅，而是将其作为修复路径。例如 Damus 保留了普通的私信加载流程，并在手动刷新时添加 Negentropy，以恢复正常流程可能遗漏的消息。

## 权衡

Negentropy 需要双方都支持该协议，且在标准 `REQ` 用法之上增加了协议复杂度。当正确性比最小化实现工作量更重要时，它最为有用。

在混合环境中，客户端仍需优雅地回退，因为并非所有中继器都支持该协议。

---

**主要来源：**
- [Negentropy 协议仓库](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**提及于：**
- [第6期周刊：Damus 推出 Negentropy 实现可靠私信同步](/zh/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [第12期周刊](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
