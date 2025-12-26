---
title: 'Nostr Compass 第2期'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的 Nostr 协议生态系统每周指南。

**本周：** 三个 [NIP-55](/zh/topics/nip-55/) 签名器实现获得更新：Amber 添加了性能缓存，Aegis 获得 `nostrsigner:` URI 支持，Primal Android 加入它们成为完整的本地签名器。Shopstr 推出通过 zaps 进行闪购的 "Zapsnags" 功能。Mostro 添加了开发基金。四项 NIP 更新已合并，包括公开消息（kind 24）和群组隐私改进。NDK 缓存查询速度提升 162 倍，Applesauce 添加了反应和 NIP-60 钱包支持，Tenex 引入了用于 AI 代理委托的 RAL 架构。在我们的深度解析中，我们解释了 [NIP-02](/zh/topics/nip-02/)（关注列表）和 [NIP-10](/zh/topics/nip-10/)（回复线程），这是构建社交时间线和对话的基础规范。

## 新闻动态 {#news}

**Primal Android 成为 NIP-55 签名器** - 在上周 [Nostr Connect 支持](/zh/newsletters/2025-12-17-newsletter/#primal-android) 的基础上，Primal 通过八个合并的拉取请求实现了完整的本地签名功能。该实现包括一个完整的 `LocalSignerContentProvider`，通过 Android 的 content provider 接口向其他 Android 应用暴露签名操作，遵循 [NIP-55](/zh/topics/nip-55/) 规范。架构清晰地分离了关注点：`SignerActivity` 处理面向用户的审批流程，`LocalSignerService` 管理后台操作，新的权限系统让用户控制哪些应用可以请求签名。这使 Primal 成为想要在一个应用中保管密钥同时使用其他应用获得不同 Nostr 体验的 Android 用户的 Amber 可行替代方案。

**Shopstr Zapsnags：通过闪电网络进行闪购** - Nostr 原生市场推出了 ["Zapsnags"](https://github.com/shopstr-eng/shopstr/pull/211)，这是一个闪购功能，让买家可以直接从社交信息流中通过单次 zap 购买商品。该实现过滤带有 `#shopstr-zapsnag` 标签的 kind 1 笔记，并将其渲染为带有 "Zap to Buy" 按钮的产品卡片，而不是标准的购物车流程。当买家发送 zap 时，系统使用 [NIP-57](/zh/topics/nip-57/) 生成支付请求，轮询 kind 9735 zap 收据以确认支付，然后使用 [NIP-17](/zh/topics/nip-17/) gift wrapping 加密收货信息后私密发送给卖家。该功能在本地存储买家详细信息以便重复购买，并包含一个用于创建闪购列表的商家仪表板。这是社交、支付和隐私原语的巧妙组合，展示了 Nostr 的可组合设计如何实现新颖的商业模式。

**Mostro 推出开发基金** - [NIP-69](/zh/topics/nip-69/) P2P 比特币交易机器人[实现了可配置的开发费用](https://github.com/MostroP2P/mostro/pull/555)以支持可持续维护。运营商可以将 `dev_fee_percentage` 设置在 Mostro 交易费的 10-100% 之间（默认为 30%），在每次成功交易时自动路由到开发基金。该实现添加了三个数据库列（`dev_fee`、`dev_fee_paid`、`dev_fee_payment_hash`）来跟踪贡献，并在守护进程启动时验证百分比。技术文档位于 [`docs/DEV_FEE.md`](https://github.com/MostroP2P/mostro/blob/main/docs/DEV_FEE.md)。这种选择加入模式让运营商支持持续开发，同时保持费用分配的完全透明。

## NIP 更新 {#nip-updates}

[NIPs 仓库](https://github.com/nostr-protocol/nips) 的近期变更：

**新增 NIPs：**
- **[NIP-A4](/zh/topics/nip-a4/)（公开消息，kind 24）** - 一种为广泛客户端支持设计的通知屏幕消息新 kind（[#1988](https://github.com/nostr-protocol/nips/pull/1988)）。与线程对话不同，这些消息没有聊天历史或消息链的概念。它们使用 `q` 标签（引用）而不是 `e` 标签以避免线程复杂性，使其非常适合出现在收件人通知信息流中而不创建对话状态的简单公开通知。

**重要变更：**
- **[NIP-29](/zh/topics/nip-29/)** - 群组语义的重大澄清（[#2106](https://github.com/nostr-protocol/nips/pull/2106)）。`closed` 标签现在意味着"无法写入"（非成员只读），与加入机制解耦。新的 `hidden` 标签阻止中继向非成员提供元数据或成员事件，实现真正的私密群组，没有带外邀请就无法发现。`private` 标签控制消息可见性，同时仍允许公开元数据用于发现。
- **[NIP-51](/zh/topics/nip-51/)** - 添加了 kind 30006 用于策展图片集（[#2170](https://github.com/nostr-protocol/nips/pull/2170)），遵循 30004（文章）和 30005（视频）的模式。已在 Nostria 中实现。
- **[NIP-55](/zh/topics/nip-55/)** - 澄清了 Android 签名器的连接启动（[#2166](https://github.com/nostr-protocol/nips/pull/2166)）。实现多用户会话的开发者误用了 `get_public_key`，从后台进程调用它。更新后的规范建议仅在初始连接时调用一次，防止常见的实现陷阱。

## NIP 深度解析：NIP-02 和 NIP-10 {#nip-deep-dive-nip-02-and-nip-10}

本周我们介绍两个对社交功能至关重要的 NIP：客户端如何知道您关注了谁以及对话如何形成线程。

### [NIP-02](/zh/topics/nip-02/)：关注列表

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md) 定义了 kind 3 事件，用于存储您的关注列表。这个简单的机制驱动着使时间线成为可能的社交图谱。

**结构：** kind 3 事件包含列出关注公钥的 `p` 标签：

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

每个 `p` 标签有四个位置：标签名称、关注的公钥（十六进制）、可选的中继 URL 提示和可选的"昵称"（本地昵称）。中继提示告诉其他客户端在哪里找到该用户的事件。昵称让您可以为联系人分配易记的名称，而不依赖于他们自己声明的显示名称。

**可替换行为：** Kind 3 属于可替换范围（0, 3, 10000-19999），因此中继每个公钥仅保留最新版本。当您关注新用户时，您的客户端发布一个完整的新 kind 3，包含所有关注者加上新关注者。这意味着关注列表每次必须是完整的；您不能发布增量更新。

**构建时间线：** 要构建主页信息流，客户端获取用户的 kind 3，提取所有 `p` 标签公钥，然后订阅来自这些作者的 kind 1 事件：

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

中继返回匹配的笔记，客户端渲染它们。kind 3 中的中继提示帮助客户端知道要查询哪些中继以获取每个关注用户的内容。

**昵称和身份：** 昵称字段实现了去中心化命名方案。与其信任用户在其个人资料中声称的名称，您可以分配自己的标签。客户端可能显示 "alice (我的姐姐)"，其中 "alice" 来自她的 kind 0 个人资料，"我的姐姐" 是您的昵称。这提供了全局用户名无法提供的上下文。

**实际考虑：** 因为 kind 3 事件是可替换的且必须完整，客户端在更新时应保留未知标签。如果另一个客户端添加了您的客户端不理解的标签，盲目覆盖会丢失该数据。追加新关注而不是从头重建。

### [NIP-10](/zh/topics/nip-10/)：文本笔记线程

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) 规定了 kind 1 笔记如何相互引用形成回复线程。理解这一点对于构建对话视图至关重要。

**问题：** 当有人回复一条笔记时，客户端需要知道：这是回复什么的？对话的根是什么？谁应该被通知？NIP-10 通过 `e` 标签（事件引用）和 `p` 标签（公钥提及）回答这些问题。

**标记标签（首选）：** 现代客户端在 `e` 标签中使用显式标记：

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "说得好！我同意。",
  "sig": "b7d3f..."
}
```

`root` 标记指向开始线程的原始笔记。`reply` 标记指向正在回复的特定笔记。如果直接回复根，只使用 `root`（不需要 `reply` 标签）。这个区分对于渲染很重要：`reply` 决定线程视图中的缩进，而 `root` 将所有回复分组在一起。

**线程规则：**
- 直接回复根：一个带有 `root` 标记的 `e` 标签
- 回复一个回复：两个 `e` 标签，一个 `root` 和一个 `reply`
- `root` 在整个线程中保持不变；`reply` 根据您回复的内容而变化

**用于通知的公钥标签：** 包含应被通知的每个人的 `p` 标签。至少标记您回复笔记的作者。惯例是也包含来自父事件的所有 `p` 标签（这样对话中的每个人都保持在循环中），加上您在内容中 @提及的任何用户。

**中继提示：** `e` 和 `p` 标签的第三个位置可以包含一个中继 URL，表示可能在哪里找到该事件或用户的内容。这帮助客户端获取引用的内容，即使它们没有连接到原始中继。

**已弃用的位置标签：** 早期 Nostr 实现从标签位置而不是标记推断含义：第一个 `e` 标签是根，最后一个是回复，中间的是提及。这种方法已弃用，因为它会产生歧义。如果您看到没有标记的 `e` 标签，它们可能来自旧客户端。现代实现应始终使用显式标记。

**构建线程视图：** 要显示线程，获取根事件，然后查询所有具有引用该根的 `e` 标签的事件：

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

按 `created_at` 排序结果，使用 `reply` 标记构建树结构。`reply` 指向根的事件是顶级回复；`reply` 指向另一个回复的事件是嵌套响应。

## 版本发布 {#releases}

**Zeus v0.12.0** - 在上周 [NWC 并行支付支持](/zh/newsletters/2025-12-17-newsletter/#zeus) 的基础上，闪电钱包的[重大版本](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0)发布了完整的 [NIP-47](/zh/topics/nip-47/) Nostr Wallet Connect 服务，支持自定义中继和预算跟踪。[预算重新加载修复](https://github.com/ZeusLN/zeus/pull/3455)确保连接使用当前限制。[闪电地址复制](https://github.com/ZeusLN/zeus/pull/3460)不再包含 `lightning:` 前缀，修复了在 Nostr 个人资料字段中的粘贴问题。

**Amber v4.0.6** - Android [NIP-55](/zh/topics/nip-55/) 签名器[添加了签名操作的性能缓存](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6)并改进了解密格式错误内容时的错误处理。连接可靠性通过中继连接事件的重试逻辑得到改善，多个崩溃修复解决了无效 `nostrconnect://` URI 和权限屏幕交互的边缘情况。

**nak v0.17.3** - 命令行 Nostr 工具的[最新版本](https://github.com/fiatjaf/nak/releases/tag/v0.17.3)将 LMDB 构建限制在 Linux，修复了跨平台编译问题。

**Aegis v0.3.4** - 跨平台 Nostr 签名器[添加了对](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4) [NIP-55](/zh/topics/nip-55/) 中定义的 `nostrsigner:` URI 方案的支持，与 Amber 的连接流程匹配。本地中继数据现在可以导入和导出用于备份，该版本还包括中继套接字错误的错误修复和本地中继界面的 UI 改进。

## 重要代码和文档变更 {#notable-code-and-documentation-changes}

*这些是开放的拉取请求和早期工作，非常适合在合并前获得反馈。如果有什么引起您的兴趣，考虑审查或评论！*

### Damus（iOS） {#damus}

[静音列表持久化](https://github.com/damus-io/damus/pull/3469)修复了冷启动时静音列表被清除的问题。修复添加了防止应用初始化期间意外覆盖的保护措施。[个人资料流时序](https://github.com/damus-io/damus/pull/3457)消除了缓存个人资料出现前约 1 秒的延迟。以前，视图等待订阅任务重新启动；现在 `streamProfile()` 立即从 NostrDB 产生缓存数据，消除了显示缩写公钥和占位符图像的窗口。

### White Noise（加密消息） {#white-noise}

[实时消息流](https://github.com/marmot-protocol/whitenoise/pull/919)用基于流的架构替换了之前的轮询机制。新的 `ChatStreamNotifier` 直接消费 Rust SDK 的消息流，保持时间顺序并高效处理增量更新。测试显示响应性显著改善。[聊天列表 API](https://github.com/marmot-protocol/whitenoise/pull/921) 添加了 `get_chat_list` 用于检索对话摘要，[稳定排序修复](https://github.com/marmot-protocol/whitenoise/pull/905)通过使用 `createdAt` 加消息 ID 作为决胜条件防止消息重新排序循环。

### NDK（库） {#ndk}

两个拉取请求带来了显著的缓存性能改进。[PR #371](https://github.com/nostr-dev-kit/ndk/pull/371) 修复了一个错误，从 SQLite 缓存读取的事件会立即被写回，导致应用启动时 100% 重复写入。修复添加了 `fromCache` 保护并通过内存中的 Set 实现 O(1) 重复检查。对于小结果集（<100 事件），直接 JSON 传输取代二进制编码开销。[PR #372](https://github.com/nostr-dev-kit/ndk/pull/372) 移除了缓存事件不必要的 `seenEvent` 调用。LRU 缓存查找每个事件花费 0.24-0.64ms；对于 5,700 个缓存事件，这增加了约 1.4 秒的开销。结果：缓存查询从约 3,690ms 降至约 22ms（快 162 倍）。

### rust-nostr（库） {#rust-nostr}

[多过滤器 REQ 支持](https://github.com/rust-nostr/nostr/pull/1176)在之前的重构中被移除后恢复。SDK 再次接受订阅请求的 `Vec<Filter>`，实现将多个过滤条件与 OR 逻辑组合的高效查询。[中继来源](https://github.com/rust-nostr/nostr/pull/1156)被添加到 `stream_events*` 方法，因此每个流式事件现在包括它来自的 `RelayUrl` 和表示成功或失败的 `Result`，对于跟踪中继可靠性和调试连接问题很有用。[安全修复](https://github.com/rust-nostr/nostr/pull/1179)在 RUSTSEC-2024-0421 之后移除了 `url-fork` 依赖，消除了一个已知漏洞。

### Applesauce（库） {#applesauce}

驱动 [noStrudel](https://github.com/hzrd149/nostrudel) 的 TypeScript 库本周有重大开发。新模型包括[反应系统](https://github.com/hzrd149/applesauce)和用户群组转换。钱包功能通过 NIP-60 支持、发送标签和改进的代币恢复工具得到扩展。新的 `user.directMessageRelays$` 属性暴露了 DM 中继配置。所有操作都被重构为使用异步接口（移除异步生成器），错误修复解决了加密内容恢复和基于时间的事件过滤边缘情况。

### Tenex（AI 代理） {#tenex}

基于 Nostr 构建的[多代理协调系统](https://github.com/tenex-chat/tenex)在[五个合并的 PR](https://github.com/pablof7z/tenex/pull/38) 中引入了 RAL（请求-操作-生命周期）架构。RAL 使代理能够在委托任务时暂停并在结果到达时恢复，具有对话范围的状态持久化。委托工具（`delegate`、`ask`、`delegate_followup`、`delegate_external`）现在发布 Nostr 事件并返回停止信号而不是阻塞。重构包括 AI SDK v6 迁移、用于确定性 LLM 交互记录的 VCR 测试基础设施和多模态图像支持。

---

本周就到这里。正在构建什么？有新闻要分享？希望我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 私信联系我们</a>或在 Nostr 上找到我们。

