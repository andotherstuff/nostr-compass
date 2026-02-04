---
title: "NIP-34 (Git 协作)"
date: 2026-02-04
description: "NIP-34 通过 Nostr 事件实现去中心化的 git 仓库托管和协作。"
---

NIP-34 定义了在 Nostr 中继上托管 git 仓库、补丁和问题的事件类型。这实现了完全去中心化的代码协作，不依赖 GitHub 或 GitLab 等集中式托管平台。

## 工作原理

仓库表示为可寻址事件（kind 30617），包含名称、描述和克隆 URL 等元数据。仓库所有者发布此事件以在 Nostr 上建立项目。

补丁（kind 1617）包含可应用于仓库的 git 补丁内容。贡献者提交引用目标仓库的补丁事件。这模仿了 Linux 内核等项目使用的基于电子邮件的补丁工作流程。

问题（kind 1621）的功能类似于传统的问题跟踪器。它们引用仓库并包含标题和描述。对问题和补丁的评论使用标准的回复事件。

## 事件类型

- **30617** - 仓库公告（可寻址）
- **1617** - 补丁提交
- **1621** - 问题
- **1622** - 问题状态（开放/关闭）

## 实现

- **ngit** - 用于将仓库和补丁发布到 Nostr 的命令行工具
- **gitworkshop.dev** - 用于浏览 Nostr 托管仓库的 Web 界面
- **Notedeck** - 桌面客户端，具有[NIP-34 查看功能的草稿支持](https://github.com/damus-io/notedeck/pull/1279)

## 主要来源

- [NIP-34 规范](https://github.com/nostr-protocol/nips/blob/master/34.md)

## 相关提及

- [Newsletter #8 (2026-02-04)](/zh/newsletters/2026-02-04-newsletter/) - Notedeck 添加 NIP-34 查看器
