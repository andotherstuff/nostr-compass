---
title: "NIP-CD：斜杠命令"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD 定义了斜杠命令。服务发布一条命令后，任何人都可以在任意 Nostr event 的 content 中以纯文本形式调用它。NIP-CD 是一份可选的规范草案。继一项更早的提案之后，它于 2026 年 10 月 21 日以 Commands 为标题合并；2026 年 10 月 27 日可选的已安装命令列表合并时，它被更名为 Slash Commands。

## 工作原理

命令由 kind 31992 event 定义。必需的 tag 给出不带斜杠的触发词、标题和用法说明。有序的 `arg` tag 声明位置参数，类型包括 pubkey、event、relay、number、enum 或 text。`s` tag 按 kind、relay、作者或 tag 限定哪些 event 可以触发该命令。这些作用域的工作方式类似过滤器：同一类型的多个值互为备选，而出现的每一种类型都必须匹配。

调用是从 event content 索引 0 处开始的文本，例如 `/ban` 后跟参数，并且不携带任何 tag。添加 `@nostr:npub1...` 形式的限定符，即可指定单个执行者。如果没有限定符，所有触发词匹配且作用域包含该 event 的命令都可以执行操作，因此一条消息可能触发多个服务。

客户端支持是可选的。客户端可以提供自动补全、参数选择器和渲染后的标签块。它们不得要求先具备自身支持才能发送调用，并且必须将无法解析的文本作为普通内容发送。

对于基于 relay 的群组，定义和调用都发送到群组 relay。在广播用途中，定义发送到执行者的 outbox，调用则发送到执行者的 inbox。

## 已安装命令列表

用户可以按照 NIP-51 维护一个可选的 kind 10992 列表，其中包含 `a` tag，这些 tag 通过执行者 pubkey 和 `d` 值指向 kind 31992 命令定义，并可附带 relay 提示。客户端应当将该列表用于自动补全和渲染后的标签块。该列表记录的是用户的显示和发现偏好。它不会授权执行者，没有它，纯文本调用也能正常工作。规范的这一部分于 2026 年 10 月 27 日通过 PR #2525 合并。此次合并并不能表明哪些客户端已经实现了该列表。

## 主要来源

- [NIP-CD 规范](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [2026 年 10 月 21 日 NIP-CD 的合并](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [已安装命令列表的 PR #2525，于 2026 年 10 月 27 日合并](https://github.com/nostr-protocol/nips/pull/2525)
- [PR #2525 在 2026 年 10 月 26 日的提交，合并前在其分支上完成](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [2026 年 10 月 27 日将已安装命令列表合并入 NIP-CD](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## 提及于
- [第 46 期简报：NIP-CD 定义以纯文本调用的命令](/zh/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) 简报

- [第 46 期简报：NIP-CD 新增可选的已安装命令列表](/zh/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) 简报

- [第 46 期简报（2026-10-28）：2026 年 10 月，共享的查询含义与文本触发的服务](/zh/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## 另见

- [NIP-01：基础协议](/zh/topics/nip-01/)
