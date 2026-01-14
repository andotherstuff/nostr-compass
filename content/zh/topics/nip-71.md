---
title: "NIP-71：视频 Event"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 定义了 Nostr 上视频内容的 event kind，支持带有适当元数据的视频分享。该规范涵盖了常规视频 event 和可寻址视频 event，后者于2026年1月添加，允许创作者在不重新发布的情况下更新视频元数据。

## Event Kind 种类

NIP-71 定义了四种 event kind，根据宽高比和可寻址性分为两类。

常规视频 event 使用 kind 21 表示横向（横屏）视频，kind 22 表示纵向（竖屏/短视频）视频。这些是发布后内容不可变的标准 Nostr event。

可寻址视频 event 使用 kind 34235 表示横向视频，kind 34236 表示纵向视频。这些是参数化可替换 event，由 pubkey、kind 和 `d` tag 的组合标识。使用相同标识符发布新 event 会替换之前的版本，允许元数据更新。

## 结构

完整的可寻址视频 event 包括标识字段、元数据 tag 和视频内容引用。

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

`d` tag 在该 kind 的视频中提供唯一标识符，因此您可以通过使用不同的 `d` 值拥有多个可寻址视频。`title` 和 `summary` tag 提供视频标题和简短描述供客户端显示。`url` tag 指向实际视频文件，而 `thumb` 提供预览图像。`duration` tag 以秒为单位指定时长，`dim` 可选地指定视频尺寸。

`origin` tag 在从其他服务导入内容时跟踪源平台。这在将视频从 YouTube、Vimeo 或其他平台迁移到 Nostr 托管时保留出处。

`content` 字段可以包含扩展描述、完整字幕或与视频相关的任何其他文本。

## 为什么可寻址 Event 很重要

常规视频 event（kind 21 和 22）一旦发布就不可变。如果您发布了一个视频，后来发现标题有错字、想要更新缩略图，或者因为迁移到不同的视频服务需要更改托管 URL，您无法修改原始 event。您唯一的选择是发布一个具有新 ID 的新 event，这会破坏任何现有引用并丢失参与度指标。

可寻址视频 event 通过使 event 可替换来解决这个问题。您的 pubkey、event kind 和 `d` tag 的组合唯一标识您的视频。当您使用相同标识符发布新 event 时，relay 用新版本替换旧版本。获取您视频的客户端总是获得最新的元数据。

这对于以下情况特别有价值：修复发布后的元数据错误、在改进品牌形象时更新缩略图、更换提供商时迁移视频托管 URL，以及从停止运营的平台如 Vine 导入内容同时通过 `origin` tag 保留出处。

## 实现

可寻址视频 event（kind 34235 和 34236）目前已在 Amethyst 和 nostrvine 中实现。这两个客户端都可以创建、显示和更新可寻址视频 event。

---

**主要来源：**
- [NIP-71 规范](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - 可寻址视频 event 更新

**相关提及：**
- [Newsletter #5：NIP 更新](/zh/newsletters/2026-01-13-newsletter/#nip-updates)

**另请参阅：**
- [NIP-94：文件元数据](/zh/topics/nip-94/)
