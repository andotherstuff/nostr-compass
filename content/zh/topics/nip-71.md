---
title: "NIP-71：视频事件"
date: 2026-01-13
draft: false
translationOf: /en/topics/nip-71.md
translationDate: 2026-03-07
categories:
  - Media
  - Protocol
---

NIP-71 定义了 Nostr 上视频内容的事件类型，支持带有适当元数据的视频分享。该规范涵盖常规视频事件和可寻址视频事件，后者于 2026 年 1 月新增，允许创作者在不重新发布的情况下更新视频元数据。

## 事件类型

NIP-71 定义了四种事件类型，按宽高比和可寻址性分为两类。

常规视频事件使用 kind 21 表示横屏（风景）视频，kind 22 表示竖屏（肖像/短视频）视频。这些是标准 Nostr 事件，一旦发布内容不可变。

可寻址视频事件使用 kind 34235 表示横屏视频，kind 34236 表示竖屏视频。这些是参数化可替换事件，由公钥、事件类型和 `d` 标签的组合来唯一标识。使用相同标识发布新事件将替换先前版本，从而允许元数据更新。

## 结构

一个完整的可寻址视频事件包含标识字段、元数据标签和视频内容引用。

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

`d` 标签在同类型视频中提供唯一标识符，因此可以通过使用不同的 `d` 值来拥有多个可寻址视频。`title` 和 `summary` 标签提供视频标题和简短描述，供客户端显示。`url` 标签指向实际的视频文件，`thumb` 提供预览图像。`duration` 标签指定时长（以秒为单位），`dim` 可选地指定视频尺寸。

`origin` 标签在从其他服务导入内容时跟踪来源平台。这在将视频从 YouTube、Vimeo 或其他平台迁移到 Nostr 托管时保留了来源信息。

`content` 字段可以包含详细描述、完整文字记录或与视频相关的任何附加文本。

## 可寻址事件的意义

常规视频事件（kind 21 和 22）发布后不可变。如果你发布了一个视频，后来发现标题有错别字、想更新缩略图，或者因为迁移到不同的视频服务而需要更改托管 URL，你无法修改原始事件。唯一的选择是使用新 ID 发布一个新事件，这会破坏所有现有引用并丢失互动数据。

可寻址视频事件通过使事件可替换来解决这个问题。你的公钥、事件类型和 `d` 标签的组合唯一标识你的视频。当你使用相同标识发布新事件时，中继会用新版本替换旧版本。客户端获取你的视频时总是得到最新的元数据。

这对以下场景特别有价值：发布后修复元数据错误、在改善品牌形象时更新缩略图、更换提供商时迁移视频托管 URL，以及从已停止运营的平台（如 Vine）导入内容并通过 `origin` 标签保留来源信息。

另一个好处是稳定的链接。其他事件可以持续引用同一个可寻址视频，而创作者更新其周围的展示细节，这比将评论和引用分散在多个不可变的重新发布中更简洁。

## 权衡

可替换性有助于元数据维护，但也意味着客户端需要决定保留多少历史状态。如果创作者在发布后更改了标题或摘要，最新的事件成为规范版本，即使较旧的客户端可能已经索引了之前的版本。

Kind 21 和 22 对于需要不可变发布记录的应用仍然重要。NIP-71 并不强制所有视频工作流都采用可替换模型。

## 实现

可寻址视频事件（kind 34235 和 34236）目前已在 Amethyst 和 nostrvine 中实现。两个客户端都可以创建、显示和更新可寻址视频事件。

---

**主要来源：**
- [NIP-71 规范](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - 可寻址视频事件更新

**提及于：**
- [Newsletter #5：NIP 更新](/zh/newsletters/2026-01-13-newsletter/#nip-updates)
- [Newsletter #12：NoorNote](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [NIP-94：文件元数据](/zh/topics/nip-94/)
