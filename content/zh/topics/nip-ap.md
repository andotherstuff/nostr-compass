---
title: "Buzz NIP-AP：智能体人设"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

Buzz NIP-AP 是 Buzz 项目的一份规范草案，不属于 nostr-protocol/nips 中已被接受的 NIP。

它定义了 kind 30175 人设 event，即用于实例化 AI 智能体的可寻址定义，以明文 `d` slug 为键。Kind 30178 保存团队目录投影。实现该规范的 relay 会对这两种 kind 进行访问控制：作者可以读取自己的 event；其他读取者只有在 event 带有 `["shared", "true"]` 时，才能在查询、实时推送、搜索、计数或 id 查找中看到它。共享一个团队会暴露每个成员嵌入的投影和指令，包括人设未共享的成员。这种门控只控制访问，并不加密内容；relay 运营者仍然可以读取这些内容。

主要来源：Buzz 仓库中的 [NIP-AP 规范](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)。

## 主要来源

- [Buzz NIP-AP：智能体人设](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## 提及于

- [第 46 期简报（2026-10-28）：buzz](/zh/newsletters/2026-10-28-newsletter/#buzz)

- [第 45 期简报](/en/newsletters/2026-10-21-newsletter/#buzz)
