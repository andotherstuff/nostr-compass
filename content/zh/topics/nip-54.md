---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2025-12-31
draft: false
categories:
  - 协议
  - 内容
---

NIP-54 将 kind 30818 定义为可寻址事件类型，用于在 Nostr 上创建 Wiki 文章和百科全书条目。它支持去中心化的协作内容创建，多位作者可以就相同主题进行撰写。

## 工作原理

Wiki 文章通过规范化的 `d` tag（文章主题）进行标识。多人可以撰写关于同一主题的文章，从而创建一个没有中央权威的去中心化知识库。

**D Tag 规范化：**
- 将所有字母转换为小写
- 将空格转换为连字符
- 删除标点符号和符号
- 保留非 ASCII 字符和数字

## 内容格式

文章使用 Asciidoc 标记语言，具有两个特殊功能：

- **Wikilinks**（`[[目标页面]]`）- 链接到 Nostr 上的其他 Wiki 文章
- **Nostr 链接** - 根据 NIP-21 引用个人资料或事件

## 文章选择

当存在多个版本的文章时，客户端根据以下条件进行优先排序：

1. 表示社区认可的反应（NIP-25）
2. 用于来源排名的 relay 列表（NIP-51）
3. 形成推荐网络的联系人列表（NIP-02）

## 协作功能

- **分叉** - 创建文章的衍生版本
- **合并请求**（kind 818）- 对现有文章提出修改建议
- **重定向**（kind 30819）- 将旧主题指向新主题
- **优先标记** - 指示首选的文章版本

---

**主要来源：**
- [NIP-54 规范](https://github.com/nostr-protocol/nips/blob/master/54.md)

**相关提及：**
- [新闻通讯 #3：NIP 更新](/zh/newsletters/2025-12-31-newsletter/#nip-updates)

**另请参阅：**
- [NIP-51：列表](/zh/topics/nip-51/)
- [NIP-02：关注列表](/zh/topics/nip-02/)
