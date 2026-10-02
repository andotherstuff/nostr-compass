---
title: "Buzz NIP-AR：频道工件"
date: 2026-09-30
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Collaboration
---

NIP-AR 是 Buzz **项目专属**的频道工件规范。此处的标签并不意味着它已被 `nostr-protocol/nips` 仓库或其他 relay 采纳。

## 工件模型 {#artifact-model}

工件是一种可编辑记录，具有稳定的 `d` 标识、`h` tag 中指定的唯一所属频道，以及通过 `prev` 链接起来的完整快照修订。只有当 `prev` 指向当前头部时，relay 才会接受一次编辑。因此，两个相互竞争的修订不可能同时成为下一个头部。Buzz 的实现使用 kind `45010` 表示工件，并在工件移出频道时使用由 relay 签名的 kind `45011` 标记。源频道可以看到工件被移除，但无法从该标记得知其去向。

[Buzz 规范合并](https://github.com/block/buzz/pull/7791)描述了这一模型，[relay 实现合并](https://github.com/block/buzz/pull/7919)则报告了针对冲突处理、历史查询、移动和频道权限的测试。这些合并确立的是项目源代码中的行为，而不是通用的 Nostr 标准或公开部署保证。

---

**主要来源：**
- [Buzz 频道工件规范合并](https://github.com/block/buzz/pull/7791)
- [Buzz 频道工件实现合并](https://github.com/block/buzz/pull/7919)

**提及于：**
- [第42期周刊：Buzz 频道工件](/zh/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
