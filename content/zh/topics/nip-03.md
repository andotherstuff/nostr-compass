---
title: "NIP-03：为 event 提供 OpenTimestamps 认证"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03 描述了如何为 Nostr event 发布 [OpenTimestamps](https://opentimestamps.org/) 证明。该证明可作为证据，表明该 event 在某个特定比特币区块的时间点之前就已存在。

**警告：**当前规范被标注为 `draft`、`optional` 和 `unrecommended`。规范头部注明，它易受某一种特定攻击，需要更新。正文并未描述这一攻击。请将此格式视为历史参考，在规范修订之前，不要在新工作中采用它。

## 工作原理

证明以单独的 kind 1040 event 发布。其 `e` tag 指明目标 event id，并附带一个 relay URL；其 `k` tag 则记录目标 event 的 kind。OpenTimestamps 证明必须以目标 event id 本身作为其摘要（digest）进行证明。该 id 不会被再次哈希。

`content` 存放经 base64 编码的完整 `.ots` 文件，其中至少包含一个比特币认证（attestation）。规范建议恰好包含一个认证，且不包含待定（pending）认证，因为待定认证只会增加字节，对验证并无帮助。

验证者获取 kind 1040 event，解码其内容，再对照比特币检验该证明。有效的证明表明，该 event id 已在被认证的区块中得到承诺。由此可为该 event 确定一个最晚可能的创建时间，且这一时间不依赖作者自己填写的 `created_at` 值。它并不能证明该 event 的内容属实。

## 历史

一个 [2023 年 10 月 11 日的 commit](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e) 改变了证明的存放位置。在此之前，证明是附加在 event 本身上的一个 `ots` 字段。此后，每个证明都是一个单独的 kind 1040 event，并指向其目标。

## 原始资料

- [当前的 NIP-03 规范](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [2023 年 10 月 11 日将证明移至 kind 1040 event 的 commit](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## 新闻简报中的提及

- [第 46 期新闻简报（2026-10-28）：2023 年 10 月，event 承载证据与工作请求](/zh/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## 另请参阅

- [NIP-01：基础协议](/zh/topics/nip-01/)
