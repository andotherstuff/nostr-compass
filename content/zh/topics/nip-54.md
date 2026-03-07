---
title: "NIP-54：Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Content
---

NIP-54 将 kind `30818` 定义为 Nostr 上的 Wiki 式文章。多位作者可以就同一主题发布条目，因此客户端需要排名和信任启发式方法，而不是单一的规范页面。

## 工作原理

Wiki 文章通过规范化的 `d` 标签来标识主题。多人可以发布具有相同规范化主题的条目，从而创建一个没有中央编辑者的开放 Wiki。

**D 标签规范化：**
- 将有大小写变体的字母转为小写
- 将空白字符转为连字符
- 移除标点符号和符号
- 合并重复连字符并修剪首尾连字符
- 保留非 ASCII 字母和数字

该规范化规则对互操作性至关重要。如果两个客户端对同一标题进行了不同的规范化，它们将查询不同的主题并分裂文章集。

## 内容格式

合并后的规范使用 Asciidoc 标记语言，并添加了两个额外功能：

- **Wikilinks**（`[[目标页面]]`）- 链接到 Nostr 上的其他 Wiki 文章
- **Nostr 链接** - 根据 NIP-21 引用个人资料或事件

曾有人提议切换到 Djot，但截至 2026 年 3 月，Djot 尚未在规范 NIP 中取代 Asciidoc。

## 文章选择

当存在多个版本的文章时，客户端可以根据以下条件进行优先排序：

1. 表示社区认可的反应（NIP-25）
2. 用于来源排名的中继列表（NIP-51）
3. 形成推荐网络的联系人列表（NIP-02）

实际上，这意味着 NIP-54 不仅是一种内容格式，也是一个客户端策略问题。两个客户端可以为同一主题显示不同的"最佳"文章，而两者都符合规范。

## 协作功能

- **分叉** - 创建文章的衍生版本
- **合并请求**（kind 818）- 对现有文章提出修改建议
- **重定向**（kind 30819）- 将旧主题指向新主题
- **优先标记** - 指示首选的文章版本

分叉和优先标记允许作者认可更好的版本，而无需删除自己的作品。这在一个旧修订版本可能在许多中继上保持可用的网络中尤为重要。

---

**主要来源：**
- [NIP-54 规范](https://github.com/nostr-protocol/nips/blob/master/54.md)
- [PR #2177：国际化 d 标签规范化](https://github.com/nostr-protocol/nips/pull/2177)

**提及于：**
- [第3期周刊：NIP 更新](/zh/newsletters/2025-12-31-newsletter/#nip-updates)
- [第15期周刊：开放 PR 和项目更新](/zh/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**另请参阅：**
- [NIP-51：列表](/zh/topics/nip-51/)
- [NIP-02：关注列表](/zh/topics/nip-02/)
