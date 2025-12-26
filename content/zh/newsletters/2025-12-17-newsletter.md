---
title: 'Nostr Compass 第1期'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
---

欢迎阅读 Nostr Compass，这是一份专注于 Nostr 协议生态系统的周刊。我们的使命是让开发者、中继运营者和建设者了解网络中的重要发展动态。我们以技术准确性、中立性和深度记录协议演进，涵盖从 NIP 提案到客户端发布再到实现最佳实践的各个方面。

Nostr Compass 的灵感来自 [Bitcoin Optech](https://bitcoinops.org/)，他们多年来致力于推进比特币技术知识，为以协议为中心的新闻通讯树立了标杆。我们感谢他们的榜样，并希望为 Nostr 生态系统带来同样的严谨态度。

本创刊号确立了我们的周刊格式。每周三，我们将为您带来 NIP 更新、版本发布说明、开发亮点和技术指南。无论您是在构建客户端、运营中继还是为协议做贡献，Nostr Compass 都致力于成为您了解生态系统动态的可靠信息来源。

## 什么是 Nostr？

*由于这是我们的创刊号，我们从 Nostr 的工作原理入门开始。老读者可以[跳到下一节](#新闻动态)。*

Nostr（Notes and Other Stuff Transmitted by Relays，即"通过中继传输的笔记和其他内容"）是一个用于社交网络和消息传递的去中心化协议。与传统平台不同，Nostr 没有中央服务器、没有控制它的公司，也没有单点故障。用户通过加密密钥对拥有自己的身份，内容通过任何人都可以运行的独立中继服务器进行流转。

**工作原理：** 用户生成一个密钥对（私钥称为 nsec，公钥称为 npub）。私钥用于签署称为"事件"的消息，公钥则作为您的身份标识。事件被发送到中继，中继存储并转发给其他用户。由于您控制着自己的密钥，您可以在不同客户端或中继之间切换而不会丢失身份或关注者。

**意义何在：** Nostr 通过中继多样性提供抗审查能力（如果一个中继封禁您，其他中继仍可提供您的内容）、可移植性（您的身份可在任何 Nostr 应用中使用）和互操作性（所有 Nostr 客户端使用相同的协议）。没有算法决定您看什么，没有广告，也没有数据采集。

**当前生态系统：** Nostr 支持微博客（类似 Twitter/X）、长文内容（类似 Medium）、私信、市场、直播等功能。客户端包括 Damus（iOS）、Amethyst（Android）、Primal、Coracle 等数十种。闪电网络集成通过"zaps"实现即时支付。协议通过 NIPs（Nostr Implementation Possibilities，即 Nostr 实现可能性）持续演进，这是社区驱动的规范，用于扩展功能。

## 新闻动态 {#news}

**NIP-BE 合并：蓝牙低功耗支持** - 协议新增了一项重要能力，[已合并到协议中](https://github.com/nostr-protocol/nips/pull/1979)。[NIP-BE](/zh/topics/nip-be/) 规定了 Nostr 应用如何通过蓝牙低功耗进行通信和同步。这使离线应用能够在没有互联网连接的情况下跨附近设备同步数据。该规范将 WebSocket 中继模式适配到 BLE 的约束条件，使用 DEFLATE 压缩和分块消息来处理 BLE 的小 MTU 大小（20-256 字节）。设备根据 UUID 比较协商角色，UUID 较高的设备成为 GATT 服务器。

**MIP-05：隐私保护推送通知** - [Marmot 协议](/zh/topics/marmot/) 发布了 [MIP-05](/zh/topics/mip-05/)（[规范](https://github.com/marmot-protocol/mips/blob/main/mip-05.md)），这是一个保护隐私的推送通知规范。传统推送系统需要服务器知道设备令牌和用户身份；MIP-05 通过使用 ECDH+HKDF 和 ChaCha20-Poly1305 加密设备令牌来解决这个问题，使用临时密钥防止关联。三事件 gossip 协议（kinds 447-449）在群组成员之间同步加密令牌，通知使用 [NIP-59](/zh/topics/nip-59/) gift wrapping 和诱饵令牌来隐藏群组大小。这使 WhiteNoise 和其他 Marmot 客户端能够在不损害用户隐私的情况下提供及时通知。

**Blossom BUD-10：新 URI 方案** - [Blossom](/zh/topics/blossom/) 媒体协议通过 [BUD-10](/zh/topics/bud-10/)（[规范](https://github.com/hzrd149/blossom/blob/master/buds/10.md)）获得自定义 URI 方案。新的 `blossom:<sha256>.ext` 格式嵌入文件哈希、扩展名、大小、多个服务器提示和用于 [BUD-03](/zh/topics/bud-03/) 服务器发现的作者公钥。这使 blob 链接比静态 HTTP URL 更具弹性，能够自动在服务器之间进行回退。

**Shopstr 市场更新** - Nostr 原生市场[实现了 Nostr Wallet Connect](https://github.com/shopstr-eng/shopstr/pull/202)（[NIP-47](/zh/topics/nip-47/)）支付功能，使用 [NIP-40](/zh/topics/nip-40/) [添加了商品过期功能](https://github.com/shopstr-eng/shopstr/pull/203)，并为卖家引入了[折扣码](https://github.com/shopstr-eng/shopstr/pull/210)。

## NIP 更新 {#nip-updates}

[NIPs 仓库](https://github.com/nostr-protocol/nips) 的近期变更：

**新增 NIPs：**
- **[NIP-BE](/zh/topics/nip-be/)** - 蓝牙低功耗消息传递和设备同步（[#1979](https://github.com/nostr-protocol/nips/pull/1979)）
- **[NIP-63](/zh/topics/nip-63/)** - 付费墙/付费内容标准，用于处理协议内的门控内容（[#2156](https://github.com/nostr-protocol/nips/pull/2156)）

**重要变更：**
- **[NIP-24](/zh/topics/nip-24/)** - 在 Kind 0 用户元数据中添加可选的 `languages` 数组，允许用户使用 IETF BCP 47 标签指定多种首选语言，以改进内容发现和中继匹配（[#2159](https://github.com/nostr-protocol/nips/pull/2159)）
- **[NIP-69](/zh/topics/nip-69/)** - 为 P2P 交易添加订单过期支持，包含 `expires_at` 和 `expiration` 标签（[#2118](https://github.com/nostr-protocol/nips/pull/2118)）
- **[NIP-59](/zh/topics/nip-59/)** - Gift wrap 事件现在可以通过 NIP-09/NIP-62 请求删除（[#2131](https://github.com/nostr-protocol/nips/pull/2131)）
- **[NIP-51](/zh/topics/nip-51/)** - 从通用书签中移除了 hashtag 和 URL 标签；hashtags 现在使用 kind 30015（[#2133](https://github.com/nostr-protocol/nips/pull/2133)）
- **[NIP-18](/zh/topics/nip-18/)** - 改进了可替换事件的通用转发，支持 `a` 标签（[#2132](https://github.com/nostr-protocol/nips/pull/2132)）
- **[NIP-17](/zh/topics/nip-17/)** - 改进措辞并为私信添加 kind 7 反应支持（[#2098](https://github.com/nostr-protocol/nips/pull/2098)）
- **[NIP-11](/zh/topics/nip-11/)** - 添加 `self` 字段用于中继公钥标识（[#1764](https://github.com/nostr-protocol/nips/pull/1764)）

## NIP 深度解析：NIP-01 和 NIP-19 {#nip-deep-dive-nip-01-and-nip-19}

在本创刊号中，我们介绍两个每位 Nostr 开发者都应该了解的基础 NIP。请参阅我们的主题页面 [NIP-01](/zh/topics/nip-01/) 和 [NIP-19](/zh/topics/nip-19/)。

### NIP-01：基础协议

[NIP-01](/zh/topics/nip-01/) 定义了核心协议。Nostr 中的一切都建立在这个规范之上。

**事件** 是唯一的对象类型。每个事件包含：
- `id`：序列化事件的 SHA256 哈希（事件的唯一标识符）
- `pubkey`：创建者的公钥（32 字节十六进制，secp256k1）
- `created_at`：Unix 时间戳
- `kind`：整数，表示事件类型
- `tags`：数组的数组，用于元数据
- `content`：载荷（解释取决于 kind）
- `sig`：Schnorr 签名，证明公钥创建了此事件

**Kinds** 决定中继如何存储事件：
- 常规事件（1, 2, 4-44, 1000-9999）：正常存储，保留所有版本
- 可替换事件（0, 3, 10000-19999）：每个公钥仅保留最新版本
- 临时事件（20000-29999）：不存储，仅转发给订阅者
- 可寻址事件（30000-39999）：每个公钥 + kind + `d` 标签组合的最新版本

Kind 0 是用户元数据（个人资料），kind 1 是文本笔记（基本帖子），kind 3 是关注列表。

**Kind 1：文本笔记** 是社交 Nostr 的核心。kind 1 事件是短文帖子，类似于推文。`content` 字段包含消息文本（纯文本，但客户端通常渲染 markdown）。标签启用回复、提及和引用：

```json
{
  "id": "<32-byte-hex>",
  "pubkey": "<32-byte-hex>",
  "created_at": 1734480000,
  "kind": 1,
  "content": "Hello Nostr! Check out @jb55's work on Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ],
  "sig": "<64-byte-hex>"
}
```

带有 "reply" 标记的 `e` 标签表示这是一个回复（参见 [NIP-10](/zh/topics/nip-10/) 了解线程约定）。`p` 标签提及一个用户，使客户端能够通知他们并渲染他们的名字而不是原始公钥。客户端获取被提及用户的 kind 0 事件以获取其显示名称和头像。

要构建时间线，客户端订阅来自关注公钥的 kind 1 事件：`["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`。中继返回匹配的笔记，客户端按时间顺序渲染它们。

**可寻址事件**（30000-39999）的工作方式类似于可替换事件，但使用 `d` 标签作为额外标识符。中继仅保留每个公钥 + kind + d 标签组合的最新版本。这支持可编辑文章、商品列表，或需要每个用户多个可替换项目的任何场景。

**标签** 是数组，第一个元素是标签名称。标准单字母标签（`e`、`p`、`a`、`d`、`t`）被中继索引以便高效查询。例如，`["e", "<event-id>"]` 引用另一个事件，`["p", "<pubkey>"]` 引用一个用户。

**客户端-中继通信** 使用 WebSocket 连接，消息为 JSON 数组。第一个元素标识消息类型。

从客户端到中继：
- `["EVENT", <event>]` - 向中继发布事件
- `["REQ", <sub-id>, <filter>, ...]` - 订阅匹配过滤器的事件
- `["CLOSE", <sub-id>]` - 结束订阅

从中继到客户端：
- `["EVENT", <sub-id>, <event>]` - 传递匹配订阅的事件
- `["EOSE", <sub-id>]` - "存储事件结束" - 中继已发送所有历史匹配，现在只会发送新到达的事件
- `["OK", <event-id>, <true|false>, <message>]` - 确认事件是否被接受或拒绝（及原因）
- `["NOTICE", <message>]` - 来自中继的人类可读消息

订阅流程：客户端发送带有订阅 ID 和过滤器的 `REQ`，中继响应匹配的 `EVENT` 消息，然后发送 `EOSE` 表示历史记录已发送完毕。`EOSE` 之后，任何新的 `EVENT` 消息都是实时的。客户端完成后发送 `CLOSE`。

**过滤器** 指定要检索哪些事件。过滤器对象可以包括：`ids`（事件 ID）、`authors`（公钥）、`kinds`（事件类型）、`#e`/`#p`/`#t`（标签值）、`since`/`until`（时间戳）和 `limit`（最大结果数）。一个过滤器内的所有条件使用 AND 逻辑。您可以在 `REQ` 中包含多个过滤器，它们使用 OR 逻辑组合 - 这对于在一次订阅中获取不同事件类型很有用。

### NIP-19：Bech32 编码标识符

[NIP-19](/zh/topics/nip-19/) 定义了您在 Nostr 中随处可见的人类友好格式：npub、nsec、note 等。这些不在协议本身使用（协议使用十六进制），但对于分享和显示至关重要。

**为什么使用 bech32？** 原始十六进制密钥容易复制出错且难以视觉区分。Bech32 编码添加了人类可读的前缀和校验和。您可以立即区分 `npub`（公钥）、`nsec`（私钥）或 `note`（事件 ID）。

**基本格式** 编码原始 32 字节值：
- `npub` - 公钥（您的身份，可安全分享）
- `nsec` - 私钥（保密，用于签名）
- `note` - 事件 ID（引用特定事件）

示例：十六进制公钥 `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d` 变为 `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`。

**可分享标识符** 使用 TLV（类型-长度-值）编码包含元数据：
- `nprofile` - 带有中继提示的个人资料（帮助客户端找到用户）
- `nevent` - 带有中继提示、作者公钥和 kind 的事件
- `naddr` - 可寻址事件引用（公钥 + kind + d 标签 + 中继）

这些解决了一个关键问题：如果有人分享一个笔记 ID，您如何知道哪个中继有它？`nevent` 将事件 ID 与建议的中继捆绑在一起，使分享更可靠。

**重要提示：** 永远不要在协议本身使用 bech32 格式。事件、中继消息和 NIP-05 响应必须使用十六进制。Bech32 纯粹用于人类界面：显示、复制/粘贴、二维码和 URL。

## 版本发布 {#releases}

**Amber v4.0.4** - Android 签名应用修复了 NullPointerException，改进了活动屏幕的性能，并为某些事件类型添加了翻译。之前的 v4.0.3 版本添加了改进的加密/解密 UI、账户导出/导入、每账户中继处理、bunker ping 支持和崩溃报告。[发布说明](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - Web 客户端的错误修复版本。修复了主题信息流、禁用 imgproxy 时的图像处理，以及非链接高亮源的链接化问题。[发布说明](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - 类 Discord 的社区客户端修复了模态滚动和样式问题。本周期的早期版本添加了可选的通知徽章和声音、改进的链接渲染、邀请链接的二维码扫描，以及简化的钱包设置。[发布说明](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - 命令行 Nostr 工具添加了新的 `nip` 命令用于快速 NIP 参考查询，以及 git 仓库处理和 stdin 事件处理的修复。[发布说明](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - 基于 MLS 的加密消息应用的重大版本，添加了通过 Blossom 的图像分享、后台同步、推送通知、8 种语言本地化和群组成员管理。[发布说明](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - 功能版本，引入了关注列表/包、新的时间线过滤器、图片库和 H.265 视频压缩（文件小 50%）。完成了 Kotlin 多平台迁移。[发布说明](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - P2P 交易机器人更新，支持 NIP-69 订单过期和改进的交易历史响应。[发布说明](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

**Nosflare v8.9.26** - 构建在 Cloudflare 基础设施上的无服务器 Nostr 中继。此版本提供了关键热修复，解决了可能导致 websocket 故障的错误，确保依赖该中继的用户和应用程序获得更稳定的连接。[发布说明](https://github.com/Spl0itable/nosflare/releases/tag/v8.9.26)

**Noscall v0.4.1** - 基于 Nostr 的安全音视频通话应用。此版本改进了"我"页面的弹出 UI 并修复了几个已知问题，提高了稳定性和通话可靠性。[发布说明](https://github.com/sanah9/noscall/releases/tag/v0.4.1-release)

**Gitplaza v0.25.0** - 专注于 Git 相关活动的桌面 Nostr 客户端。此版本为收件箱信息流引入了高级 kind 过滤器，在过滤器中包含常规 zaps，并简化了标签文本格式。性能改进优化了评论树加载，减少了不必要的数据库查询，并使用缓存的评论分支以加快显示速度。[发布说明](https://codeberg.org/dluvian/gitplaza/releases/tag/v0.25.0)

## 重要代码和文档变更 {#notable-code-and-documentation-changes}

### Damus（iOS） {#damus}

稳定性焦点，修复崩溃和 UI 问题：编辑视图的[光标跳跃修复](https://github.com/damus-io/damus/pull/3377)，使用 Swift 的 `~Copyable` 类型进行事务安全的 [NostrDB 接口重新设计](https://github.com/damus-io/damus/pull/3366)，修复操作栏重新实例化的[线程 UI 稳定性](https://github.com/damus-io/damus/pull/3341)，来自 AttributeGraph 循环的[静音列表冻结](https://github.com/damus-io/damus/pull/3346)，以及来自跨线程事务清理的[个人资料崩溃](https://github.com/damus-io/damus/pull/3334)。还添加了 AI 编码代理的 [AGENTS.md](https://github.com/damus-io/damus/pull/3293) 指南。

### Notedeck（桌面/移动） {#notedeck}

[安全密钥存储](https://github.com/damus-io/notedeck/pull/1191) 将 nsec 移至操作系统安全存储并自动迁移。[未来笔记过滤](https://github.com/damus-io/notedeck/pull/1201) 隐藏日期超前 24 小时以上的事件（反垃圾信息）。[nevent 复制](https://github.com/damus-io/notedeck/pull/1183) 现在包含中继提示。另有：[个人资料列快速添加](https://github.com/damus-io/notedeck/pull/1212)、[键盘导航](https://github.com/damus-io/notedeck/pull/1208)、[媒体加载优化](https://github.com/damus-io/notedeck/pull/1210)。

### Amethyst（Android） {#amethyst}

[[NIP-46](/zh/topics/nip-46/) 远程签名](https://github.com/vitorpamplona/amethyst/pull/1555) 支持 Nostr Connect。[书签组织](https://github.com/vitorpamplona/amethyst/pull/1586) 带有公开/私密列表管理。[strfry 兼容性](https://github.com/vitorpamplona/amethyst/pull/1596) 修复中继信息解析边缘情况。

### Primal（Android） {#primal-android}

[Nostr Connect 深度链接](https://github.com/PrimalHQ/primal-android-app/pull/788) 用于 `nostrconnect://` URL。通过 bunker 连接的二维码扫描进行[远程登录](https://github.com/PrimalHQ/primal-android-app/pull/787)。[连接竞态条件修复](https://github.com/PrimalHQ/primal-android-app/pull/783)。

### White Noise（加密消息） {#white-noise}

[应用数据保留修复](https://github.com/marmot-protocol/whitenoise/pull/890) 禁用 Android 自动备份以保护隐私。[聊天滚动行为](https://github.com/marmot-protocol/whitenoise/pull/861) 在阅读历史记录时保留位置。

### Zeus（闪电钱包） {#zeus}

[[NIP-47](/zh/topics/nip-47/) 并行支付](https://github.com/ZeusLN/zeus/pull/3407) 改善批量 zap 吞吐量。

## 开发者最佳实践

**防御性验证 Auth 事件** - go-nostr 修复了当中继标签丢失时 [NIP-42 验证中的 panic](https://github.com/nbd-wtf/go-nostr/pull/182)。即使在您期望格式良好事件的认证流程中，也要在访问必需标签之前检查它们。

**根据认证状态进行速率限制** - khatru 添加了[基于 NIP-42 的速率限制](https://github.com/fiatjaf/khatru/pull/57)，允许中继对已认证和匿名连接应用不同的限制。考虑基于认证状态的分层限制，而不是一刀切的限制。

**使用游标分页处理列表** - Blossom 在 `/list` 端点[将基于日期的分页替换为基于游标的分页](https://github.com/hzrd149/blossom/pull/65)。当项目共享时间戳时，基于日期的分页会失效；游标提供可靠的迭代。

**事件类型的 Schema 验证** - [nostrability/schemata](https://github.com/nostrability/schemata) 项目提供用于验证符合 NIP 的事件的 JSON schema。考虑在开发中集成 schema 验证，以在格式错误的事件到达中继之前捕获它们。

---

本周就到这里。正在构建什么？有新闻要分享？希望我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 私信联系我们</a>或在 Nostr 上找到我们。

