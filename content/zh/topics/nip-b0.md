---
title: "NIP-B0：网页书签"
date: 2026-05-28
draft: false
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
categories:
  - Protocol
  - Social
---

NIP-B0 定义了一个参数化可替换事件（kind 39701），将网页书签作为一等 Nostr 事件发布。该提案让用户可以构建可被发现、可被 zap、可跨客户端重新发布的策展书签合集，而不必依赖中心化的书签服务。

## 工作原理

一个书签是一个 kind 39701 事件，其 `d` tag 是被书签页面的规范 URL。可替换语义使作者可以为该 URL 更新自己的书签（重新打标签、更新标题、标记过时），而不会产生重复事件。content 字段承载作者关于该书签的备注；tag 承载标题、描述、图片以及用于发现的 `t` 话题 tag。

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

`d` tag 使每位作者的书签具备唯一标识，因此两位用户都可以为同一个 URL 添加书签，并各自附上不同的备注和 tag 集合。

## 发现与策展

由于每个书签都是一等事件，任何 Nostr 客户端都可以通过按 tag 或作者过滤 kind 39701 事件来渲染书签信息流。以策展人为中心的工作流由此自然形成：策展人发布一组书签，读者关注策展人的 pubkey，书签便通过承载它们的任何 relay 流转。不存在中心化的目录。

## 实现

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) —— 参考 web 客户端，采用三盒架构（策展人、索引器、查看器），并搭配由直付给策展人的 NIP-57 zap 资助的分层系统。除 NIP-B0 外，还实现了 NIP-07、NIP-46、NIP-57、NIP-44、NIP-98、NIP-65 以及用于文件存储的 Blossom BUD-01/BUD-04。

## 信任与安全说明

- 书签默认公开；不要以此方式发布私密的阅读列表
- 重新发布依赖 relay 继续承载相应事件；短暂 relay 会丢弃书签
- `published_at` tag 由发布者自己声明，不具备可验证性

---

**Primary sources:**
- [NIP-B0 proposed specification](https://github.com/nostr-protocol/nips/pull/2089) —— 跟踪提议的 kind 39701 网页书签事件
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) —— 带有策展人分层系统的参考实现

**Mentioned in:**
- [Newsletter #24: deepmarks NIP-B0 bookmarks with curator-monetized publishing](/zh/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Newsletter #27: Also shipped](/zh/newsletters/2026-06-17-newsletter/#also-shipped)

**See also:**
- [NIP-57: Lightning Zaps](/zh/topics/nip-57/)
- [NIP-65: Relay List Metadata](/zh/topics/nip-65/)
