---
title: "NIP-51：列表"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 定义了用于组织 Nostr 中事件、用户和内容引用的各种列表类型。

## 列表 Kinds

- **Kind 10000**：静音列表（要隐藏的用户、线程或词语）
- **Kind 10001**：置顶列表（要在个人资料上展示的事件）
- **Kind 30000**：关注集合（分类的关注列表）
- **Kind 30003**：书签集合
- **Kind 30004**：策展集合（文章）
- **Kind 30005**：视频集合
- **Kind 30006**：图片集合
- **Kind 30015**：兴趣集合（hashtags）
- **Kind 30030**：表情符号集合

## 结构

列表使用标签来引用内容：
- `p` 标签用于公钥
- `e` 标签用于事件
- `a` 标签用于可寻址事件
- `t` 标签用于 hashtags
- `word` 标签用于静音词

## 公开与私密

列表可以有公开标签（所有人可见）和加密内容（私密）。私密项目使用 NIP-44 加密并存储在事件的 `content` 字段中。加密使用作者自己的密钥（加密给自己）。

这允许实现如带私密注释的公开书签，或隐藏静音项目的静音列表等功能。

## 近期变更

- 从通用书签中移除了 hashtag 和 URL 标签；hashtags 现在使用 kind 30015
- 添加了 kind 30006 用于策展图片集合

---

**主要来源：**
- [NIP-51 规范](https://github.com/nostr-protocol/nips/blob/master/51.md)

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)
- [第2期周刊：NIP 更新](/zh/newsletters/2025-12-24-newsletter/#nip-updates)

**另请参阅：**
- [NIP-02：关注列表](/zh/topics/nip-02/)

