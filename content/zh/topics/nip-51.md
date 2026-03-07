---
title: "NIP-51：列表"
date: 2025-12-17
translationOf: /en/topics/nip-51.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 定义了用于组织用户、事件、中继、hashtag 及其他引用的列表事件。它是书签、静音列表、关注集合、中继集合以及其他用户策划集合的主要协议。

## 标准列表与集合

- **标准列表**使用可替换事件类型，如 kind `10000` 静音列表、kind `10003` 书签和 kind `10007` 搜索中继。
- **集合**使用带有 `d` 标签的可寻址类型，如 kind `30000` 关注集合、kind `30003` 书签集合和 kind `30030` 表情符号集合。

这一区别影响客户端行为。标准列表意味着每个用户和 kind 只有一个规范列表。集合意味着多个命名集合，因此客户端必须保留每个列表的 `d` 标签。

## 结构

列表使用标签来引用内容：

- `p` 标签用于公钥
- `e` 标签用于事件
- `a` 标签用于可寻址事件
- `t` 标签用于 hashtag
- `word` 标签用于静音词
- `relay` 标签用于面向中继的列表类型中的中继 URL

某些列表类型的标签形式比其他类型更受限制。例如，面向中继的列表使用 `relay` 标签，而书签则应指向笔记或可寻址事件。将所有 NIP-51 列表都视为任意自由形式标签的客户端会失去互操作性。

## 公开与私密

列表可以包含公开标签和私密项目。私密项目被序列化为与 `tags` 结构相同的 JSON 数组，经过加密后存储在事件的 `content` 字段中。当前规范使用 NIP-44 进行这种自加密模型，NIP-04 仅作为旧版兼容。

这种分离让用户可以发布可见的列表外壳，同时隐藏部分条目。书签列表可以保持公开，而私密笔记或私密书签则保留在加密内容中。

## 常用 Kind

- **Kind 10000**：用于公钥、线程、hashtag 和静音词的静音列表
- **Kind 10003**：用于笔记和可寻址内容的书签
- **Kind 10007**：首选搜索中继
- **Kind 30002**：用于命名中继组的中继集合
- **Kind 30006**：图片策展集合
- **Kind 39089**：用于可分享关注包的 starter pack

最近的规范变更将 hashtag 从通用书签中移出并放入兴趣集合，同时新增了 kind `30006` 用于图片策展。这两项变更都减少了客户端解释列表内容时的歧义。

---

**主要来源：**
- [NIP-51 规范](https://github.com/nostr-protocol/nips/blob/master/51.md)

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)
- [第2期周刊：NIP 更新](/zh/newsletters/2025-12-24-newsletter/#nip-updates)
- [第4期周刊：NIP 深度解析](/zh/newsletters/2026-01-13-newsletter/#nip-deep-dive-nip-51-and-nip-65)
- [第8期周刊：njump 添加 NIP-51 支持](/zh/newsletters/2026-02-04-newsletter/#njump)

**另请参阅：**
- [NIP-02：关注列表](/zh/topics/nip-02/)
