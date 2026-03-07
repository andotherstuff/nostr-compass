---
title: "NIP-34：Git 协作"
date: 2026-02-04
description: "NIP-34 通过 Nostr 事件实现去中心化的 git 仓库托管和协作。"
draft: false
translationOf: /en/topics/nip-34.md
translationDate: 2026-03-07
categories:
  - NIP
  - Development
---

NIP-34 定义了在 Nostr 中继上托管 git 仓库、补丁和议题的事件类型。这使得完全去中心化的代码协作成为可能，无需依赖 GitHub 或 GitLab 等集中式托管平台。

## 工作原理

仓库以可寻址事件（kind 30617）表示，包含名称、描述和克隆 URL 等元数据。仓库所有者发布此事件，在 Nostr 上建立项目。

补丁（kind 1617）包含 `git format-patch` 内容，可应用于仓库。贡献者以引用目标仓库的事件形式提交补丁。这种方式类似于 Linux 内核等项目使用的基于邮件的补丁工作流。

议题（kind 1621）的功能类似于传统的问题追踪器。拉取请求使用 kind 1618 和 1619，状态更新使用 1630 到 1633。对议题、补丁和拉取请求的回复使用 [NIP-22](/zh/topics/nip-22/) 评论。

## 事件类型

- **30617** - 仓库公告（可寻址）
- **30618** - 分支和标签的仓库状态公告
- **1617** - 补丁提交
- **1618** - 拉取请求
- **1619** - 拉取请求更新
- **1621** - 议题
- **1630-1633** - 开放、已合并/已解决、已关闭和草稿状态事件

## 重要意义

NIP-34 将发现与传输分离。实际仓库仍然可以存放在普通的 Git 服务器上，但 Nostr 事件提供了一个中继分发的层，用于发现、讨论、补丁交换和状态追踪。这意味着项目可以继续使用 git 原生工具，而无需依赖单一 forge 的数据库或 API。

`r` 标签配合最早的唯一提交是最重要的细节之一。它为客户端提供了一种方式来分组代表相同底层仓库血统的镜像和分支，而这仅从名称很难推断出来。

## 实现状态

- **ngit** - 用于将仓库和补丁发布到 Nostr 的命令行工具
- **gitworkshop.dev** - 浏览 Nostr 托管仓库的 Web 界面
- **Notedeck** - 桌面客户端，具有 [NIP-34 查看的草案支持](https://github.com/damus-io/notedeck/pull/1279)

---

**主要来源：**

- [NIP-34 规范](https://github.com/nostr-protocol/nips/blob/master/34.md)

**提及于：**

- [Newsletter #8（2026-02-04）](/zh/newsletters/2026-02-04-newsletter/) - Notedeck 添加 NIP-34 查看器
- [Newsletter #9：Notedeck](/zh/newsletters/2026-02-11-newsletter/#notedeck)

**另请参阅：**
- [NIP-22：评论](/zh/topics/nip-22/)
