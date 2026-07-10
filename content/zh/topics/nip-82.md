---
title: "NIP-82：软件应用"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
categories:
  - Discovery
  - Apps
---

NIP-82 定义了一种软件应用事件，使 Nostr 客户端可以在信息流和发现界面中把应用（Android APK、iOS 应用、web 应用、桌面二进制）作为一等对象来渲染。该规范用一种专门的、结构化的事件取代了此前用通用 kind 1 note 或 [NIP-89](/zh/topics/nip-89/) 处理器推荐来描述应用的做法，携带应用的元数据、截图、代码仓库链接和作者身份。

## 工作原理

一个 NIP-82 软件应用是一个由作者 pubkey 与 `d` tag 寻址的可替换事件。事件承载了：

- `name`、`description`、`icon`、`image` tag，用于显示
- `repository` 和 `web` tag，用于源码和主页 URL
- `platforms` tag，枚举支持的目标平台（android、ios、web、linux、macos、windows）
- 针对每个平台特定二进制或 web URL 的 `download` tag
- 承载应用截图图片 URL 的 `screenshots` tag
- 用于分类的 `t` 话题 tag
- 表示当前发布版本的 `version` tag

浏览 NIP-82 信息流的客户端可以展示应用卡片、链接到规范的代码仓库并呈现截图，而不必回退到从 Nostr 长文或第三方应用商店抓取。作者 pubkey 是应用的真相来源，因此客户端在推广下载链接前可以先校验发布者是否与预期的开发者身份一致。

## 信息流语义

NIP-82 事件是可寻址的，因此每个应用在每位作者名下只有一个规范的可替换事件。开发者发布新版本时会原地替换之前的事件，订阅者无需管理事件历史即可看到更新。想要变更日志的客户端可以订阅这个可寻址事件，将版本升级作为该应用界面上的活动来渲染。

规范可与 [NIP-89](/zh/topics/nip-89/)（应用处理器）组合使用：NIP-82 事件把应用描述为制品，而 NIP-89 事件描述该应用可以处理哪些特定的事件 kind。客户端可以单独使用其中之一，但两者搭配可以同时提供发现面（NIP-82）和委派面（NIP-89），并且相互配合。

## 实现

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) 上线了一个专门的 NIP-82 软件应用信息流，包含详情页、作者信息和截图（[PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036)、[PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078)、[PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200)）

---

**Primary sources:**
- [NIP-82 Specification](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - 添加带有专属信息流的 NIP-82 软件应用支持
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - 添加专门的 NIP-82 软件应用详情页
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - 通过作者信息和截图改进 NIP-82 软件应用 UI

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/zh/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**See also:**
- [NIP-89: Application Handlers](/zh/topics/nip-89/)
