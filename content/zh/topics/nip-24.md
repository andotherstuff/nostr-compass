---
title: "NIP-24：额外元数据字段"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 定义了 kind 0 用户元数据的额外可选字段，超出基本的 name、about 和 picture。

## 额外元数据字段

- **display_name**：一个替代的、更大的名称，可以使用比 `name` 更丰富的字符
- **website**：与事件作者相关的网址
- **banner**：用于可选背景显示的宽幅图片 URL（约 1024x768）
- **bot**：布尔值，表示内容全部或部分由自动化生成
- **birthday**：包含可选的年、月、日字段的对象

## 标准标签

NIP-24 还标准化了通用标签：
- `r`：网址引用
- `i`：外部标识符
- `title`：各种事件类型的名称
- `t`：Hashtag（必须小写）

---

**主要来源：**
- [NIP-24 规范](https://github.com/nostr-protocol/nips/blob/master/24.md)

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)

