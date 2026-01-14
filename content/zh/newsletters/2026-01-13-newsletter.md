---
title: 'Nostr 指南针 #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

欢迎回到 Nostr 指南针，您每周的 Nostr 导览。

**本周要闻：** Bitchat 完成由 Cure53 进行的专业安全审计，该公司此前曾审计过 Signal 和 [NIP-44](/zh/topics/nip-44/)，目前已有17个以上的 PR 合并修复了关键发现。[NIP-71](/zh/topics/nip-71/) 已合并，为协议带来可寻址视频 event。一项后量子密码学 NIP 开启了关于未来抵御量子攻击的讨论。Amethyst v1.05.0 发布了书签列表、语音消息和早期桌面版本，而 Nostur v1.25.3 改进了 [NIP-17](/zh/topics/nip-17/) 私信功能，支持反应和回复。在库方面，rust-nostr 扩展了 [NIP-62](/zh/topics/nip-62/) 对 SQLite 和 LMDB 后端的支持，NDK 修复了订阅追踪的 bug。

## 新闻 {#news}

### Bitchat 完成 Cure53 安全审计 {#bitchat-completes-cure53-security-audit}

Bitchat 是一款结合 Nostr 和 Cashu 的 iOS 加密消息应用，已完成由 Cure53 进行的专业安全审计。Cure53 是业内最受尊敬的安全公司之一，此前曾审计过 Signal、Mullvad VPN，以及为现代 Nostr 私密消息奠定基础的 [NIP-44](/zh/topics/nip-44/) 加密规范。

审计发现了12个以上的安全问题（BCH-01-002 至 BCH-01-013）。Bitchat 团队以17个以上的 PR 作为回应。主要修复包括：

**Noise 协议 DH 密钥清除** - [PR #928](https://github.com/permissionlesstech/bitchat/pull/928) 修复了六处 Diffie-Hellman 共享密钥在密钥协商后未被清零的问题，恢复了前向保密性保证。当密钥在内存中保留的时间超过必要时，内存转储或冷启动攻击可能会危及过去的通信。

**签名验证** - 多个 PR 加强了密码验证路径，确保消息真实性检查不会被格式错误的输入绕过。

**线程安全** - [PR #929](https://github.com/permissionlesstech/bitchat/pull/929) 为 NostrTransport 中的已读回执队列添加了屏障同步，防止在高消息量下可能导致数据损坏或崩溃的竞态条件。

**内存安全** - [PR #920](https://github.com/permissionlesstech/bitchat/pull/920) 优化了消息去重器，在高消息吞吐量时获得更好的性能，同时避免内存耗尽。

**输入验证** - [PR #919](https://github.com/permissionlesstech/bitchat/pull/919) 加强了十六进制字符串解析，防止格式错误的输入导致崩溃，这是拒绝服务攻击的常见攻击向量。

Bitchat 处理 Cashu 电子现金，因此专业安全审查至关重要。此次审计继去年的 [Marmot](/zh/topics/marmot/) 协议审计和验证加密层的 NIP-44 审计之后进行。

## NIP 更新 {#nip-updates}

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-71](/zh/topics/nip-71/)** - 可寻址视频 Event（[#1669](https://github.com/nostr-protocol/nips/pull/1669)）引入了 kind 34235（横向视频）和 34236（纵向视频）作为可寻址 event。必需的 `d` tag 提供唯一标识符，因此视频元数据可以在不重新发布整个 event 的情况下更新。可选的 `origin` tag 追踪导入来源。已在 Amethyst 和 nostrvine 中实现。

**开放中的 PR：**

- **后量子密码学** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) 提议为 Nostr 添加抗量子密码算法。该规范引入了 ML-DSA-44 和 Falcon-512 用于数字签名，目标是「超高价值 event」如应用程序和授权机构，而非个人用户。虽然 [NIP-44](/zh/topics/nip-44/) 的对称加密（ChaCha20）是抗量子的，但其密钥交换使用的 secp256k1 ECDH 容易受到 Shor 算法的攻击。该提案包括 ML-KEM 用于密钥协商以解决这一缺口。这是一个早期提案，开启了关于 Nostr 长期安全的加密敏捷性讨论。
- **NIP-47 的 BOLT12** - 经过137条评论和广泛讨论后，社区决定 BOLT12 offers 值得拥有自己的规范，而不是扩展 [NIP-47](/zh/topics/nip-47/)。BOLT12 offers 相比 BOLT11 发票提供了显著升级，包括可重用性、通过盲路径提供更好的隐私性，以及可选的付款人信息。新的 NIP 将为 Nostr Wallet Connect 实现定义 `make_offer`、`pay_offer` 和 `list_offers` 等方法。
- **音频轨道 NIP** - [PR #1043](https://github.com/nostr-protocol/nips/pull/1043) 提议 kind 32100 用于音乐曲目，kind 32101 用于播客剧集，使音频内容获得与 NIP-71 为视频提供的同等一流待遇。目前，Wavlake、Zapstr 和 Stemstr 等音频平台各自使用专有 event 格式，导致生态系统碎片化。通用标准将实现互操作性，让用户可以从任何兼容客户端发现和播放音频。
- **NIP-A3 通用支付目标** - [PR #2119](https://github.com/nostr-protocol/nips/pull/2119) 提议使用 RFC-8905 `payto:` URI 的 kind 10133 event 来公开跨多个网络的支付选项。这种抽象方式不是为 Bitcoin、Lightning、Cashu 或传统支付渠道创建单独的 event kind，而是让客户端解析标准化的 tag 并调用原生支付处理程序。这种方法具有前瞻性，因为新的支付方式只需要一个 `payto:` URI 方案。

## NIP 深度解析：NIP-51 和 NIP-65 {#nip-deep-dive-nip-51-and-nip-65}

本周我们介绍两个存储用户偏好的 NIP：NIP-51 用于组织内容，NIP-65 用于组织 relay 连接。两者都使用可替换 event，意味着每次新发布都会覆盖之前的版本。

### [NIP-51](/zh/topics/nip-51/)：列表 {#nip-51-lists}

[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) 定义了多种列表类型，用于组织对 event、用户、hashtag 和其他内容的引用。Amethyst v1.05.0 添加了书签支持，这是了解列表工作原理的好时机。

该规范定义了几种列表 kind，每种都有不同的用途。Kind 10000 是您的屏蔽列表，用于隐藏用户、帖子或词语。Kind 10001 将 event 置顶以在您的个人资料上展示。Kind 30003 存储书签，这正是 Amethyst 现在支持的功能。其他 kind 处理关注集（30000）、精选文章集合（30004）、hashtag 兴趣（30015）和自定义表情符号集（30030）。

列表通过 tag 引用内容。书签列表使用 `e` tag 表示特定 event，使用 `a` tag 表示可寻址内容如文章：

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

`d` tag 提供唯一标识符，因此您可以在同一 kind 下维护多个书签集，如「saved-articles」、「read-later」或「favorites」。

列表支持公开和私密项目。公开项目出现在 tags 数组中，任何获取该 event 的人都可见。私密项目放在 `content` 字段中，使用 [NIP-44](/zh/topics/nip-44/) 加密给自己。这种双重结构让您可以保留公开书签同时附加私密笔记，或维护一个屏蔽列表而不暴露您屏蔽了谁。要加密给自己，请使用 NIP-44 并将您自己的 pubkey 作为接收者。

10000 系列 kind 是可替换的，意味着 relay 每个 pubkey 只保留一个 event。30000 系列是参数化可替换的，允许每个 pubkey 和 `d` tag 组合一个 event。在这两种情况下，更新列表意味着发布完整的替换；您无法发送增量更改。客户端在修改列表时应保留未知的 tag，以避免覆盖其他应用程序添加的数据。

### [NIP-65](/zh/topics/nip-65/)：Relay 列表元数据 {#nip-65-relay-list-metadata}

[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) 定义了 kind 10002 event，用于公告用户偏好用于读取和写入的 relay。这帮助其他用户和客户端找到您的内容。

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

每个 `r` tag 包含一个 relay URL 和一个可选标记。`write` 标记指定您的发件箱：您发布内容的 relay。`read` 标记指定您的收件箱：您检查提及、回复和标签的 relay。省略标记表示两者都是。

当 Alice 想找到 Bob 的帖子时，她的客户端获取 Bob 的 kind 10002，提取他的 write relay（他的发件箱），并在那里订阅。当 Alice 回复 Bob 时，她的客户端发布到他的 read relay（他的收件箱），这样他就能看到提及。这种 relay 感知路由是「发件箱模型」，它将用户分布在许多 relay 上，而不是让所有人集中在少数几个中心服务器上。

NIP-65 处理公开内容路由，但私信使用单独的列表。[NIP-17](/zh/topics/nip-17/) 为 DM 收件箱 relay 定义了 kind 10050，使用 `relay` tag 而不是 `r` tag。当向某人发送私信时，客户端查找接收者的 kind 10050 event 并在那里发布加密的礼物包装消息。这种分离使 DM 路由与公开内容路由区分开来，并让用户可以为私密通信和公开通信指定不同的 relay。

发件箱模型提高了抗审查能力，因为没有单个 relay 需要存储或服务所有人的内容。客户端维护与关注用户的 NIP-65 event 中列出的 relay 的连接，在发现新账户时动态连接到新的 relay。NIP-65 补充了其他 NIP 中的 relay 提示。当您用 `["p", "pubkey", "wss://hint.relay"]` 标记某人时，提示告诉客户端在哪里查找该特定引用。NIP-65 提供权威的、用户控制的列表，而提示提供嵌入在单个 event 中的快捷方式。

为获得最佳效果，请保持您的 relay 列表最新，因为过时的条目会使您更难被找到。规范建议每个类别使用两到四个 relay。列出太多 relay 会给每个想要获取您内容的客户端带来负担，减慢他们的体验并增加网络负载。客户端缓存 NIP-65 event 并定期刷新以跟上用户偏好的更新。

## 版本发布 {#releases}

**Amethyst v1.05.0** - 这款流行的 Android 客户端[发布重大更新](https://github.com/vitorpamplona/amethyst/releases)，带来多项主要功能。[NIP-51](/zh/topics/nip-51/) kind 30003 书签列表让用户可以保存帖子以供稍后参考，跨兼容客户端同步。语音消息现在可以在私信和普通帖子中使用，带有波形可视化、媒体服务器选择和上传进度指示器。[Web of Trust](/zh/topics/web-of-trust/) 分数现在在界面中可见，帮助用户了解算法如何相对于其社交图谱评估账户。[Quartz](/zh/topics/quartz/) 数据库迁移作为 OpenSats 资助的 Kotlin Multiplatform 工作的一部分，提高了查询性能。早期桌面版本通过 Compose Multiplatform 将 Amethyst 带到 Windows、macOS 和 Linux，与 Android 应用共享相同的代码库。新用户引导流程为首次使用 Nostr 的用户提供流畅的体验。

**Nostur v1.25.3** - 这款 iOS 和 macOS 客户端[专注于私密消息](https://github.com/nostur-com/nostur-ios-public/releases)，改进了 [NIP-17](/zh/topics/nip-17/)。DM 对话现在支持反应和回复，将公开帖子的互动性带入加密消息中。对话视图经过重新设计，具有更好的线程显示，多消息交流更容易跟踪，时间戳在 DM 列表中显示「多久之前」以便快速浏览。桌面用户获得多列布局，可以并排查看多个 feed 或对话。[NIP-46](/zh/topics/nip-46/) 远程签名器支持允许用户将私钥保存在专用签名器应用中，如 Amber 或 nsec.app。其他修复恢复了 iOS 15 和 iOS 16 上的 DM 功能，解决了通知延迟问题，并添加了配置哪些 relay 接收已发布 DM 的功能。

## 值得关注的代码和文档变更 {#notable-code-and-documentation-changes}

*这些是开放的 PR 和早期工作，非常适合在合并前获得反馈。如果有什么吸引您的注意，请考虑审查或评论！*

### Citrine（Android Relay） {#citrine-android-relay}

[PR #89](https://github.com/greenart7c3/Citrine/pull/89) 修复了这款 Android 个人 relay 应用中的 SQL 注入漏洞。该问题允许格式错误的 event 数据执行任意数据库查询，对于任何存储和处理不可信输入的应用来说都是严重缺陷。修复通过使用参数化查询正确清理了所有数据库操作。目前还没有标记版本发布，因此用户需要等待下一个版本或从源代码构建。[PR #90](https://github.com/greenart7c3/Citrine/pull/90) 通过数据库级过滤和分页优化了 ContentProvider 查询性能，减少了 Amethyst 等外部应用通过 Android 进程间通信层访问 Citrine event 数据库时的延迟。

### rust-nostr（库） {#rust-nostr-library}

[NIP-62](/zh/topics/nip-62/)（消失请求）支持正在 rust-nostr 的数据库后端中扩展。[PR #1180](https://github.com/rust-nostr/nostr/pull/1180) 两周前合并，为 SQLite 添加了 NIP-62 支持，处理 `ALL_RELAYS` 消失请求，因为数据库层不知道特定的 relay URL。[PR #1210](https://github.com/rust-nostr/nostr/pull/1210) 将此扩展到 LMDB 后端，确保消失请求持久化到磁盘并在 relay 重启后保持。浏览器环境的 IndexedDB 实现也在进行中。这些变更共同为开发者提供了跨 SQLite、LMDB 和即将推出的浏览器存储的一致 NIP-62 支持。

### NDK（Nostr Development Kit） {#ndk-nostr-development-kit}

[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) 修复了 seenEvents 跟踪系统中的 bug。该问题导致某些订阅模式错误地将 event 标记为已见，当用户打开新订阅或重新连接到 relay 时导致内容丢失。修复确保 event 在订阅生命周期中被准确跟踪，这对于根据用户导航动态订阅和取消订阅的应用程序尤其重要。NDK 已升级到 beta.70 并包含此修复。

### Damus（iOS） {#damus-ios}

[PR #3515](https://github.com/damus-io/damus/pull/3515) 修复了影响 iOS 17 用户的启动崩溃问题。该问题源于 `NdbUseLock` 中的算术溢出，这是一个后备类，因为 Swift Mutex 在 iOS 17 上不可用。修复用 `NSLock` 替换了之前的同步方法，它在 iOS 17 上可用并正确处理剩余的竞态条件。iOS 18+ 用户不受影响，因为他们可以访问原生 Swift Mutex 实现。

另外，一批长文章改进通过 [PR #3509](https://github.com/damus-io/damus/pull/3509) 落地。阅读进度条跟踪您在文章中的位置，预估阅读时间显示在预览中，棕褐色模式和可调节行高设置提供更舒适的阅读体验。专注模式在向下滚动时自动隐藏导航界面，点击时恢复，减少视觉干扰以实现无干扰阅读。多项修复解决了 markdown 内容中的图片显示问题，并确保文章从顶部打开而不是中间。

### Zap.stream（直播） {#zapstream-live-streaming}

YouTube 和 Kick 聊天集成将外部流媒体平台的消息桥接到 Nostr。同时在 YouTube、Kick 和 Zap.stream 上直播的主播现在可以在统一视图中看到所有聊天消息，每个平台的消息与原生 Nostr 评论一起显示。这消除了想要使用 Nostr 进行直播但无法放弃已建立平台上观众的创作者的主要摩擦点。集成显示每条消息来自哪个平台，并处理连接外部账户的认证流程。

### Chachi（NIP-29 群组） {#chachi-nip-29-groups}

[NIP-29](/zh/topics/nip-29/) 群聊客户端本周合并了六个 PR。安全更新解决了 [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89)，这是 react-router 中的 XSS 漏洞，可能导致开放重定向攻击；修复更新到 react-router-dom 6.30.0。[PR #92](https://github.com/purrgrammer/chachi/pull/92) 为群聊添加了分页消息加载，因此长对话可以增量加载而不是一次性加载。[PR #91](https://github.com/purrgrammer/chachi/pull/91) 修复了几个 NIP-29 bug，包括导致初始加载时群组名称为空白的竞态条件和导致成员视图崩溃的未定义参与者列表。翻译覆盖现在涵盖所有31种支持的语言，每种1060个键。

### 0xchat（消息） {#0xchat-messaging}

这款 Telegram 风格的消息客户端改进了 [NIP-55](/zh/topics/nip-55/) 合规性，在使用外部签名应用时正确保存签名器包名称，修复了应用在重启后丢失要使用哪个签名器的追踪问题。NIP-17 回复处理现在正确包含用于线程的 `e` tag，确保回复在跨客户端时出现在正确的对话上下文中。性能优化解决了消息列表中的滚动卡顿，这是加载长聊天历史时的常见痛点。草稿自动保存防止在编写过程中导航离开时消息丢失，文件存储选项现在包括默认的 FileDropServer 和 BlossomServer 端点。

### Primal（iOS） {#primal-ios}

[NIP-46](/zh/topics/nip-46/) 远程签名器支持通过 [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184) 在 iOS 上落地，完成了几周前从 Android 开始的跨平台推出。用户现在可以将私钥保存在专用 bunker 服务中，如 nsec.app 或自托管的 nsecBunker 实例，通过 Nostr relay 连接来签署 event，而无需将密钥暴露给客户端应用。这种分离改善了想要使用 Primal 功能同时保持更严格密钥管理实践的用户的安全态势。实现包括用于 bunker 连接 URI 的二维码扫描，并处理通过加密 relay 消息的 NIP-46 请求/响应流程。

---

本周就到这里。正在构建什么？有新闻要分享？想让我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 私信联系我们</a>或在 Nostr 上找到我们。
