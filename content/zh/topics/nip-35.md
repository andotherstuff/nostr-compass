---
title: "NIP-35：Torrents（种子）"
date: 2026-10-21
translationOf: /en/topics/nip-35.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

NIP-35 是一个关于 torrent 索引 event 的 NIP，处于草案状态且为可选。kind 2003 event 在 `x` tag 中携带 BitTorrent v1 infohash 及文件路径，还可以指明 tracker。这些 event 保存的是索引元数据，文件内容则由对等节点通过 BitTorrent 获取。对 torrent 的评论使用 kind 2004，并遵循 NIP-10 的线程规则。

这个编号还有一段更早的历史。Draft Wraps 曾占用 NIP-35，直到 2024 年的一次重新编号将该提案移至 NIP-37。在那次变更之前提及 NIP-35 的内容，可能指的是 Draft Wraps。如今，这个编号属于 Torrents。

[当前 NIP-35 文本](https://github.com/nostr-protocol/nips/blob/master/35.md)定义了 event 格式。[重新编号的 commit](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408) 记录了先前的分配情况。

## 原始资料

- [NIP-35：Torrents](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [nostr-protocol/nips commit 48674e5（2024 年重新编号）](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## 提及于
- [第 46 期新闻简报：Magnetar](/zh/newsletters/2026-10-28-newsletter/#magnetar)

- [第 45 期新闻简报](/en/newsletters/2026-10-21-newsletter/#short-history)
