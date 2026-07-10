---
title: "NIP-F4：播客"
date: 2026-06-03
draft: false
translationOf: /en/topics/nip-f4.md
translationDate: 2026-07-01
categories:
  - NIPs
  - Protocol
  - Media
---

NIP-F4 定义了 Nostr 客户端如何引用、呈现播客单集并与之进行社交互动。该规范在草案阶段经过两年三个月的讨论后于 2026-05-28 合并,使用 kind 54 事件表示单集,并把既有的 RSS 播客栈作为互补层来设计。

## 工作原理

一个 kind 54 播客单集事件承载一个 `title` tag、一个可选的 `image` tag、一个 `description` tag、一个或多个用于音频文件的 `imeta` tag（URL、mime 类型、哈希、时长、码率、语言代码、备用 URL、NIP-96 服务标记）、`t` 话题 tag，以及一个用于回退显示的 NIP-31 `alt` tag。

关键的设计选择是 `i` tag，它以 `podcast:item:guid:<guid>` 格式承载单集的 RSS GUID。这使得：

- Nostr 客户端可以展示 kind 54 事件,并将其链接回任何支持 RSS 的播客应用中的同一集
- 支持 RSS 的 Nostr 客户端可以把现有播客的单集以 kind 54 事件的形式呈现出来,而不必强制播客主迁移托管
- 通过 Podcasting 2.0 的 `<podcast:socialInteract>` 和 `<podcast:chat>` tag 实现跨协议评论串联

## 与 RSS 的共存

围绕该 PR 的两年讨论（参与者包括 Podcasting 2.0 共同作者 Dave Jones、Alex Gleason、fiatjaf、Mike Terenzio、Pablo F7z 和 Jeff Gardner）最终落定在共存方案上。Nostr 提供社交和发现层,RSS 保留对音频文件和 feed 元数据的真相持有权。Nostr 不复制 RSS 的分发层。

这与早期尝试取代 RSS（JSONFeed、RSS 3.0、专有播客 API）的做法形成对比。Podcasting 2.0 命名空间已经支持以 note ID 引用 Nostr 事件的 `<podcast:socialInteract>`,因此一份 RSS feed 可以声明其配套的 Nostr 讨论串,而不需要 Nostr 去镜像整份 feed。

## 事件示例

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["imeta", "url https://podcast.example.com/audio/ep42.mp3", "m audio/mpeg", "x b2e0a7a82ac9f3f3a71f1d9a78c381d5be9d1cf19dce258765c17c8a76287c93", "duration 4523", "bitrate 192000", "l en ISO-639-1"],
    ["i", "podcast:item:guid:9b2a4c7d-1e3f-4a5b-8c9d-0e1f2a3b4c5d"],
    ["t", "podcasting"],
    ["alt", "Podcast episode: Why RSS Won (43 min)"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

## 实现

- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - 带有单集列表和内嵌播放器的专属播客界面（首个主要客户端实现,2026 年 5 月）
- [Wavlake](https://wavlake.com) - 最大的 Nostr 原生音乐与播客平台,预计将向 kind 54 靠拢以承载播客内容
- [Fountain](https://fountain.fm) - Bitcoin 播客应用,预计将在 RSS 与 NIP-F4 之间做桥接

## 待定问题

合并后的规范把若干设计问题留给实现去收敛：

- 建议使用按创作者划分的 pubkey,但并非必需,因此像 Wavlake 这样在一个 pubkey 下发布众多创作者内容的平台仍然有效
- 单集级别的评论和讨论使用 NIP-22 的通用串联和 kind 1 时间线 note,而不是专门的单集评论 kind
- 每档播客的元数据（主持人、播客网络、语言、许可）要么放在发布者的 kind 0 元数据中,要么放在一个独立的 kind 54 播客级别记录中

---

**Primary sources:**
- [NIP-F4 Specification](https://github.com/nostr-protocol/nips/blob/master/F4.md)
- [PR #1093](https://github.com/nostr-protocol/nips/pull/1093) - 原始提案,经过两年讨论后于 2026-05-28 合并
- [Amethyst PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) - 首个主要客户端实现

**Mentioned in:**
- [Newsletter #25: NIP Updates and Deep Dive](/zh/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-f4-podcasts)
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/zh/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**See also:**
- [NIP-22 (Comments)](https://github.com/nostr-protocol/nips/blob/master/22.md)
- [NIP-31 (Alt tags)](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [NIP-94 (File Metadata)](/zh/topics/nip-94/)
- [NIP-96 (HTTP File Storage)](/zh/topics/nip-96/)
- [Podcasting 2.0](https://podcasting2.org)
