---
title: 'Buzz 草案 NIP-AM：智能体轮次指标'
date: 2026-10-28
translationOf: /en/topics/nip-am.md
translationDate: 2026-10-28
draft: false
---

**状态：** 这是 Buzz 项目专用的草案提案。NIP-AM 并非已被接受的官方 NIP。该标签来自 Buzz 项目文档，官方 NIPs 仓库既未分配也未批准它。

## 目的

NIP-AM 为每一个已完成的 AI 智能体轮次记录用量。智能体每轮发布一个 `kind:44200` event，按照 Buzz 的约定，它被视为常规的仅追加 event。内容使用 NIP-44 加密，由智能体发给所有者。其中包含 token 用量数据和关联 ID，所有成本数值都只是估算。它不携带任何对话记录。

## 限制

公开 tag 标识了所有者和智能体，而且 relay 仍然可以看到 event 的发布时间。因此，该格式并不能隐藏有活动发生这一事实。缺失的用量值表示未知，绝不能计为零。

## 委托读取者提案

一个仍处于开放状态的文档拉取请求 #8582 提议采用一种由所有者签名的最小权限授权。按照该提案，智能体将为每个活跃读取者分别发布一份加密副本，每份副本都绑定到确切的授权 event ID。该拉取请求没有改变任何运行时授权。提议的授权 kind `30180` 和读取者上限仍是悬而未决的问题，撤销策略同样尚未确定。撤销可以限制 relay 历史记录和未来的读取。读取者已经收到的副本，撤销无法清除。

## 主要来源

- [Buzz NIP-AM 草案：智能体轮次指标（固定修订版）](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Buzz 拉取请求 #8582：委托指标读取者（开放草案）](https://github.com/block/buzz/pull/8582)

## 另见

- [NIP-44](/zh/topics/nip-44/)

**提及于：**

- [第 46 期简报：面向委托指标读取者的 NIP-AM 草案文本](/zh/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [第 46 期简报：Buzz](/zh/newsletters/2026-10-28-newsletter/#buzz)
