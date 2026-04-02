---
title: "NIP-43：Relay 访问元数据与请求"
date: 2026-03-18
translationOf: /en/topics/nip-43.md
translationDate: 2026-04-01
draft: false
categories:
  - 协议
  - Relay
  - 访问控制
---

NIP-43 定义了 relay 如何发布成员信息以及用户如何请求加入、邀请或从受限 relay 中移除。它为 relay 访问控制提供了标准的 event 接口，而不是强迫每个私有或半私有 relay 自行发明加入协议。

## 工作原理

该规范组合了多种 event kind：

- kind `13534` 发布 relay 成员列表
- kind `8000` 宣布某个成员已被添加
- kind `8001` 宣布某个成员已被移除
- kind `28934` 让用户提交带有声明代码的加入请求
- kind `28935` 让 relay 按需返回邀请码
- kind `28936` 让用户请求撤销自己的访问权限

成员状态故意不仅从单个 event 派生。客户端可能需要同时查阅 relay 签名的成员 event 和成员自己的 event，才能确定访问是否为当前状态。

## 重要性

NIP-43 为受限 relay 提供了表达准入和成员状态的标准方式。这对群组系统、仅限邀请的社区以及需要机器可读入驻流程而无需降级到带外 Web 表单或手动运营者工作流的 relay 非常重要。

[PR #2267](https://github.com/nostr-protocol/nips/pull/2267) 中的开放澄清收紧了一个实际要点：relay 应该为每个 pubkey 维护一个权威的成员状态。这有助于客户端避免模糊的重放历史，即旧的添加或移除 event 可能被误读为当前状态。

## 互操作说明

NIP-43 依赖 relay 通过其 [NIP-11](/zh/topics/nip-11/) 文档宣告支持。加入请求、邀请请求和退出请求应仅发送到明确表示支持此 NIP 的 relay。

由于这些 event 同时存在于 relay 控制和用户控制的空间中，实现需要明确的冲突规则。这就是为什么成员状态澄清比它表面看起来更重要。

---

**主要来源：**
- [NIP-43 规范](https://github.com/nostr-protocol/nips/blob/master/43.md)
- [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) - 澄清成员状态处理

**提及于：**
- [周刊 #14：NIP 更新](/zh/newsletters/2026-03-18-newsletter/#nip-更新)

**另见：**
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
- [NIP-42：客户端对 Relay 的认证](/zh/topics/nip-42/)
