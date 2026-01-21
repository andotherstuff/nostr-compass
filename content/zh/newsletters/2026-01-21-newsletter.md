---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的 Nostr 周间指南。

**本周：** Bitchat 将 C Tor 替换为 Rust Arti 实现，以获得更好的可靠性和性能。nostrdb-rs 获得了流式折叠查询，支持零分配数据库操作。Listr 获得了重大重构，包括迁移至 NDK 3 测试版并在一年的休眠后进行了 AI 辅助维护。Zeus 合并了 17 个 PR，重点关注 [NIP-47](/zh/topics/nip-47/)（用于远程 Lightning 控制的 Nostr 钱包连接）修复和 Cashu 改进，而 Primal Android 添加了钱包备份流程和 [NIP-92](/zh/topics/nip-92/)（用于正确宽高比的媒体尺寸）支持。一项新的 NIP 草案提议了 [Trusted Relay Assertions](/zh/topics/trusted-relay-assertions/) 以进行标准化的中继信任评分。

## 新闻

### Bitchat 迁移至 Rust Arti 以支持 Tor

Bitchat 已从 C Tor 迁移至 [Arti](https://gitlab.torproject.org/tpo/core/arti)，这是 Tor 协议的 Rust 实现。[PR #958](https://github.com/permissionlesstech/bitchat/pull/958) 移除了 C Tor 依赖项并集成了 Arti，带来了内存安全保证和改进的可靠性。该变更消除了导致前台服务重启的休眠唤醒尝试，这是 C 实现中的一个长期存在的问题。

**这对用户意味着什么：** 更稳定的加密消息传递，特别是在移动设备上，断开连接次数更少。Rust 实现降低了崩溃风险，并减少了来自持续重新连接尝试的电池消耗。

Arti 是 Tor 在 Rust 中的从头开始重写，由 Tor 项目开发，以通过内存安全提供更好的安全性，并更容易集成到应用程序中。对于 Bitchat，内存安全特性减少了处理加密消息和中继连接时的攻击面。此次迁移遵循了团队最近的 [Cure53 安全审计](/zh/newsletters/2026-01-13-newsletter/#bitchat-completes-cure53-security-audit)（在第 5 期新闻简报中介绍），继续其安全改进。

该 PR 还为 ChatViewModel 和 BLEService 引入了全面的测试覆盖率，移除了死代码，并稳定了测试套件。蓝牙低能耗网格可靠性改进伴随 Tor 更改，解决了大传输失败。总体而言，这些变更改进了 Bitchat 对于离线网格网络场景的弹性，其中 Tor 提供互联网连接，同时本地 BLE 通信。


### Listr 通过 AI 驱动的维护重获新生

JeffG 宣布了对 [Listr](https://github.com/erskingardner/listr) 的重大重构，这是在 [listr.lol](https://listr.lol) 提供的 Nostr 列表管理应用程序，该项目已休眠超过一年。使用 AI 协助，他完成了一次全面升级，包括迁移至 [NDK](https://github.com/nostr-dev-kit/ndk) 3 测试版、更新至最新版本的 Svelte 和 Vite，以及更新所有依赖项。重构添加了对跟随包的一流支持，为超过 50 项的列表实现了分页，并修复了在休眠期间积累的众多错误。

**这对用户意味着什么：** Listr 已重新上线，性能改进，用于管理跟随列表、内容集合和主题策展的新功能。分页修复使大列表实际可用。

JeffG 指出，如果没有 AI 协助，这项维护工作可能永远不会发生，防止项目被遗弃。Listr 在 Nostr 上启用内容策展，允许用户创建、管理和共享个人资料、主题和资源的列表。该升级使应用程序与当前 Nostr 标准和客户端期望兼容，因为列表管理变得更加重要以用于协议上的内容发现。


## NIP 更新

最近对 [NIPs 存储库](https://github.com/nostr-protocol/nips) 的更改：

**已合并：**

- **[NIP-29](/zh/topics/nip-29/)** （基于中继的群组）- 中继密钥澄清 ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - 已合并) 澄清了中继密钥是中继 URL 本身，而不是公钥。规范现在明确指出"中继密钥是中继的 WebSocket URL（例如，wss://groups.example.com）"以避免混淆。这影响了客户端如何识别哪个中继托管给定的群组，确保群组正确地归属于其托管中继。

**开放的 PR 和讨论：**

- **Trusted Relay Assertions** - 一份 NIP 草案提议通过 kind 30385 事件标准化中继信任评分，其中包含从 [NIP-66](/zh/topics/nip-66/)（中继发现和监控）指标、运营商声誉和用户报告计算的信任分数（0-100）。该规范将信任分为可靠性（正常运行时间、延迟）、质量（TLS、文档、运营商验证）和可访问性（司法管辖区、屏障、监视风险）组件。运营商验证包括通过 [NIP-11](/zh/topics/nip-11/)（中继信息文档）、DNS TXT 记录和 .well-known 文件的加密签名。用户通过 kind 10385 事件声明受信任的声明提供者，使客户端能够查询多个提供者以获得不同的观点。该提议补充了 [NIP-66](/zh/topics/nip-66/) 发现与评估，帮助 [NIP-46](/zh/topics/nip-46/)（远程签名/Nostr Connect）评估连接 URI 中中继的可信度。

- **后量子密码学** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185)（开放）自 [第 5 期新闻简报](/zh/newsletters/2026-01-13-newsletter/#nip-updates) 推出量子抗性算法提议以来一直在演变。本周的讨论重点关注密码敏捷性的实现细节：客户端如何在迁移期间处理双签名、向后兼容性对于较旧的客户端，以及更大的量子抗性签名的性能影响。贡献者辩论是否只强制使用 ML-DSA-44 还是支持多种算法（ML-DSA-44、Falcon-512、Dilithium）以获得灵活性。共识倾向于分阶段的方法：可选的量子签名最初，仅在广泛的客户端支持和真实量子威胁出现后才成为强制性的。


## NIP 深入讨论：NIP-11 和 NIP-66

本周我们研究两个一起工作以启用中继发现和评估的 NIP：NIP-11 定义了中继如何描述自己，而 NIP-66 标准化了我们如何测量中继行为。总体而言，它们为中继信任评估系统奠定了基础。

### [NIP-11](/zh/topics/nip-11/)：中继信息文档

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md) 定义了中继通过 HTTP 提供的 JSON 文档，用以描述其能力、政策和运营商信息。当客户端连接到 `wss://relay.example.com` 时，它可以获取 `https://relay.example.com`（用 `https://` 替换 `wss://`）以检索中继的信息文档。

该文档使用带有 `Accept: application/nostr+json` 标头的标准 HTTP 内容协商。这允许中继向浏览器提供其正常网站，同时向 Nostr 客户端提供机器可读的元数据。响应包括中继软件名称和版本、运营商联系信息（公钥、电子邮件、备选联系方式）、支持的 NIP 和操作参数，如支付要求或内容限制。

重要的是，基本的 NIP-11 文档是通过 HTTPS 提供的无符号 JSON，仅依赖 TLS 证书的真实性。这意味着任何控制中继网络服务器的人都可以修改文档，使运营商声明无法验证。Trusted Relay Assertions 提议通过通过中继的 `self` 公钥字段引入签名证明来解决这一差距，启用类似于中继如何为认证机制使用签名事件的运营商身份的加密证明。

```json
{
  "name": "relay.example.com",
  "description": "A general-purpose public relay",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
```

`limitation` 对象告诉客户端中继执行哪些约束。`max_message_length` 限制 WebSocket 帧大小，`max_subscriptions` 限制每个连接的并发 REQ 订阅，`max_filters` 限制每个 REQ 的过滤器，`max_limit` 约束单个过滤器可以请求的事件数量。这些参数帮助客户端适应其行为至中继能力，避免因超过限制而断开连接。

支付信息显示在 `fees` 和 `payments_url` 中。中继可以收取入场费（一次性访问）、订阅费（重复访问）或发布费（每个事件费用）。`payments_url` 指向有关支付方法（通常是 Lightning 发票或 ecash 造币厂）的详细信息。付费中继使用这些字段在客户端尝试身份验证之前传达定价。

`supported_nips` 数组让客户端发现中继能力。如果中继列出 [NIP-50](/zh/topics/nip-50/)，客户端知道他们可以发送全文搜索查询。如果 [NIP-42](/zh/topics/nip-42/) 出现，客户端应该期望身份验证挑战。这种声明性能力广告启用了渐进式增强：客户端可以在可用的地方使用高级功能，同时在支持受限的中继上优雅地降级。

运营商信息建立了责任制。`pubkey` 字段在 Nostr 上识别中继运营商，启用通过 [NIP-17](/zh/topics/nip-17/) DM 或公开提及的直接通信。`contact` 电子邮件提供了一个协议外的回退。总体而言，这些字段帮助用户为滥用报告、访问请求或技术问题联系运营商。

[NIP-11](/zh/topics/nip-11/) 文档是自我报告的：中继描述他们声称支持的内容，而不一定是他们实际所做的。这就是 NIP-66 变得重要的地方。

### [NIP-66](/zh/topics/nip-66/)：中继发现和活跃性监控

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) 标准化了向 Nostr 发布中继监控数据的方式。监控服务持续测试中继的可用性、延迟、协议合规性和支持的 NIP。他们将结果发布为 kind 30166 事件，独立于中继自我报告提供实时中继状态。

监控通过连接和发送测试订阅来检查中继可用性。延迟测量跟踪连接时间、订阅响应时间和事件传播延迟。协议合规性测试验证中继行为是否匹配规范，捕获实现错误或故意偏差。NIP 支持验证超越 [NIP-11](/zh/topics/nip-11/) 声明，通过实际测试公布的功能是否正常工作。

```json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\"last_check\": 1736784000, \"checks\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
```

`d` 标签包含中继 URL，使其成为参数化可替代事件。每个监控为每个中继发布一个事件，在测量更改时更新。多个监控可以跟踪同一中继，提供冗余和交叉验证。客户端查询多个监控公钥以获得关于中继健康的不同观点。

往返时间 (rtt) 标签测量不同操作的延迟。`rtt open` 跟踪 WebSocket 连接建立，`rtt read` 测量订阅响应时间，`rtt write` 测试事件发布速度。所有值都以毫秒为单位。客户端使用这些指标优先考虑低延迟中继以用于时间敏感的操作或降低慢速中继的优先级。

`nips` 标签列出实际验证的 NIP 支持，而不只是声称的支持。监控通过执行其功能来测试每个 NIP。如果中继在其 [NIP-11](/zh/topics/nip-11/) 文档中声称 [NIP-50](/zh/topics/nip-50/) 搜索，但搜索查询失败，监控将从验证列表中省略 NIP-50。这提供了关于中继能力的绝对真实情况。

地理信息帮助客户端选择附近的中继以获得更好的延迟和抗审查能力。`geo` 标签包含国家代码、国家名称和地区。`network` 标签区分了 Tor 隐藏服务或 I2P 端点的清网中继。总体而言，这些标签启用地理多样性：客户端可以连接到多个司法管辖区的中继以抵抗区域审查。

监控数据为客户端中的中继选择器、资源管理器网站和 Trusted Relay Assertions 提议供电。通过将自我报告的 [NIP-11](/zh/topics/nip-11/) 文档与测量的 [NIP-66](/zh/topics/nip-66/) 数据和计算的信任声明相结合，生态系统朝着知情的中继选择发展，而不是依赖硬编码的默认值或口碑推荐。

## 发布

### 0xchat v1.5.3 - 增强的消息传递功能

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release) 为 Telegram 风格的 Nostr 消息传递客户端带来了重大改进。该发布解决了 [NIP-55](/zh/topics/nip-55/)（Android 签署者应用程序）合规性问题，这些问题阻止了通过 Amber 等外部签署者的适当事件签署。完全合规意味着 0xchat 现在正确委派签署操作，通过保持私钥隔离改进了安全性。

该更新将 FileDropServer 和 BlossomServer 集成为默认媒体存储选项，为用户提供文件上传冗余。[Blossom](https://github.com/hzrd149/blossom) 提供了内容寻址存储，其中文件由其 SHA-256 哈希引用，确保完整性并在网络中启用去重复。自动草稿保存 Moments 防止了撰写长篇内容时的数据丢失，解决了用户在应用切换或连接中断期间丢失帖子的投诉。

Cashu 钱包集成通过自动证明过滤获得了改进，该过滤从钱包视图中移除了已用令牌。这解决了令人困惑的 UX，其中用户看到无效证明与有效 ecash 混合在一起，使余额计算变得不可靠。过滤发生在客户端，在改进聊天中对等交易的支付体验的同时保持隐私。

### Amber v4.1.0 预发布 - UI 改版

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1) 到 [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3) 为流行的 Android 事件签署者引入了重新设计的界面。登录屏幕现在清楚地显示哪个应用程序正在请求签名权限，解决了用户对授权流程的混淆。新的事件屏幕提供了应用程序要签署的数据的详细检查，允许用户在批准操作前做出明智的安全决定。

权限管理获得了显著关注，带有改版的界面，显示每个连接的应用程序已获得哪些能力。用户可以撤销特定权限而无需完全断开连接，启用对签署委派的细粒度控制。使用更新的石英库重构的中继计数器提供了关于事件吞吐量和中继性能的实时统计信息。[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)（Nostr Connect）bunker 连接现在在连接失败时显示详细的错误消息，用可操作的诊断替换加密的超时错误。

## 值得注意的代码和文档更改

*这些是值得跟踪的合并 pull 请求和早期阶段的开发。某些是实验功能，可能在发布前演变。*

### Zeus（带有 Nostr 钱包连接的 Lightning 钱包）

Zeus 本周合并了 17 个 pull 请求，加强了其作为领先 [NIP-47](/zh/topics/nip-47/) Nostr 钱包连接实现的地位。最显著的修复解决了导致与 Nostr 客户端互操作性问题的数据一致性和协议合规性问题。

**交易历史修复** - [PR #3542](https://github.com/ZeusLN/zeus/pull/3542) 解决了一个关键错误，其中 NWC 交易列表显示不正确或重复的条目。当 Zeus 缓存交易数据而没有正确处理事件更新时，就会发生这个问题，导致用户看到幽灵交易或丢失的付款。该修复实现了适当的事件去重复和缓存失效，确保交易历史准确反映 Lightning 节点状态。

**协议合规** - [PR #3548](https://github.com/ZeusLN/zeus/pull/3548) 解决了不完整的 `getInfo` 响应，破坏了与期望完整 NIP-47 合规性的客户端的兼容性。某些 Nostr 客户端在接收缺少 `block_height` 或 `network` 等字段的部分响应时崩溃。PR 确保所有需要的字段即使在底层 Lightning 实现不提供它们时也返回合理的默认值，改进了 Zeus 在整个生态系统中的兼容性。

**连接弹性** - [PR #3543](https://github.com/ZeusLN/zeus/pull/3543) 为停滞的 Nostr 连接实现了超时通知。以前，用户在中继连接无声断开时无限期等待。现在 Zeus 在 30 秒无活动后显示清晰的超时消息，让用户重试或切换中继。[PR #3541](https://github.com/ZeusLN/zeus/pull/3541) 添加了后端验证以防止 NWC 在不兼容的 Lightning 实现上激活，在运行时崩溃之前捕获配置错误。

**Cashu 竞态条件** - [PR #3531](https://github.com/ZeusLN/zeus/pull/3531) 修复了 Cashu 令牌管理中的并发错误，其中同时造币操作可能损坏令牌数据库。竞态条件发生在多个线程在没有适当锁定的情况下更新令牌计数时，偶尔导致不正确的余额。该修复在关键部分周围添加了互斥锁保护，确保原子更新令牌状态。

### Primal Android（客户端）

Primal Android 发布了 12 个合并 PR，显著改进了钱包安全性和媒体处理。钱包备份实现解决了最受欢迎的功能之一，而 NIP-92 支持改进了应用程序中的视觉体验。

**钱包备份系统** - 一个四 PR 系列 ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848)) 实现了全面的种子短语备份功能。用户现在可以通过安全流程导出其 12 个单词的助记词，该流程防止了截图、在钱包仪表板中显示备份状态，并引导现有用户完成迁移。该实现遵循 BIP-39 标准，并包括验证以防止用户因记录短语不正确而丢失资金。

**媒体尺寸 (NIP-92)** - [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) 实现了 [NIP-92](/zh/topics/nip-92/) 支持，以获得正确的图像和视频宽高比。在没有尺寸元数据的情况下，客户端必须下载图像以确定其大小，在内容加载时导致布局跳动。NIP-92 将 `dim` 标签（如 `["dim", "1920x1080"]`）添加到文件元数据事件中，允许 Primal 在下载媒体前预留正确的空间。这消除了图像库中令人不安的重排，改进了感知性能。

**远程签署者可靠性** - [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841) 修复了 [NIP-46](/zh/topics/nip-46/) 连接问题，其中缺少 `wss://` 前缀导致了无声失败。PR 在 bunker 连接设置期间验证中继 URI，当用户粘贴裸域时自动添加协议前缀。[PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843) 解决了一个线程错误，其中不良网络条件导致回复作为根笔记发布，破坏了对话流程。该修复确保父事件 ID 在网络中断期间持续存在。

### Marmot Protocol：White Noise（加密群组聊天库）

White Noise，为 [Marmot](/zh/topics/marmot/) Protocol 的加密群组聊天供电的 Rust 库，合并了六个 PR 以改进用户体验和安全性。这些变更使 Marmot 更接近与主流消息传递应用程序的功能奇偶性，同时保持其隐私优先的架构。

**已读回执** - [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) 和 [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436) 为群组对话实现了消息读取跟踪。系统在单个设备内按用户按群组存储读取位置，启用未读计数徽章。该实现使用单调时间戳来跟踪每个对话的最后读取消息位置。这个基础功能启用了 UI 指示器，显示每个对话的未读消息计数。

**对话固定** - [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442) 通过 `accounts_groups` 结合表中将帐户链接到群组的 `pin_order` 字段添加了持久对话固定。固定的对话无论消息活动如何都在聊天列表顶部保持其位置，匹配用户对来自 Signal 和 WhatsApp 的期望。该实现使用整数排序允许无限制的固定与确定性排序。

**确定性提交解决 (MIP-03)** - [PR #152](https://github.com/marmot-protocol/mdk/pull/152)（开放）实现了 Marmot 改进提议 03，解决了分布式群组聊天中的关键提交竞态条件问题。当多个成员同时提交群组状态变更（添加/移除成员、改变权限）时，客户端可能会在提交排序上分歧，将群组分散成不兼容的状态。MIP-03 引入了时期快照和确定性赢家选择：具有最早 `created_at` 时间戳的提交赢得，以字典 event ID 作为平局决胜者。这允许所有客户端通过回滚和重放收敛到相同的状态，即使在网络分区期间也保持群组连贯性。

**安全加固** - [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443) 通过在 `resolve_group_image_path` 中使用引用防止了不必要的密码学秘密复制。这减少了秘密可能从已释放堆分配中恢复的内存攻击窗口。[PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438) 通过密钥环参数启用了 SQLCipher 数据库加密，保护消息历史处于静止状态。密钥环集成允许在平台密钥链中进行安全密钥存储而不是配置文件。

### nostrdb-rs（数据库库）- 开放 PR

**流式查询实现** - [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58)（开放）提议流式折叠查询以启用零分配数据库操作。该实现添加了 `fold`、`try_fold`、`count`、`any`、`all` 和 `find_map` 方法，这些方法将一次处理一个数据库结果，而无需将整个结果集实现到向量中。这种方法将减少内存消耗，并为常见查询模式启用早期终止。

技术实现将低级查询结果回调 (`ndb_query_visit`) 公开为有状态 Rust 访问者，将 `ControlFlow` 变体映射到 C 访问者操作。合并后，应用程序代码将读起来像迭代器逻辑，同时接近数据库层运行。例如，计算匹配笔记将流式传输结果而不是收集它们，`find_map` 将返回第一个有用的结果而无需处理剩余的行。

nostrdb 为 Damus 和 Notedeck 供电，分别为 iOS/macOS 和桌面客户端。流式查询将启用高效的模式，如分页、条件过滤和存在检查。PR 更改 3 个文件，添加 +756，删除 -32，这是查询层的大量重构。nostrdb-rs 的用户在浏览大型时间线或在广泛事件数据库中搜索时会看到减少的内存使用。

### nak（CLI 工具）

nak，fiatjaf 的命令行 Nostr 工具，合并了六个 PR，重点关注构建系统改进和新功能。[PR #91](https://github.com/fiatjaf/nak/pull/91) 实现了 Blossom 镜像功能，让 nak 充当 Blossom 媒体服务器的镜像。[Blossom](/zh/topics/blossom/) 是一个与 Nostr 事件一起工作的内容寻址媒体存储协议。

其余 PR 解决了 Windows、macOS 和 Linux 平台的构建系统兼容性，启用了 FUSE 文件系统支持以将 Nostr 事件作为本地目录挂载。

### Damus（iOS 客户端）- 开放 PR

Damus 有 11 个开放 PR 探索重大架构改进。虽然这些还没有合并，但它们表明了 iOS Nostr 客户端开发的重要方向，特别是围绕隐私、同步效率和移动数据优化。

**Tor 集成** - [PR #3535](https://github.com/damus-io/damus/pull/3535) 直接将 Arti Tor 客户端嵌入 Damus，启用匿名中继连接而无需外部依赖。与 Orbot 或 Tor 浏览器方法不同，嵌入 Arti 为 iOS 沙箱和后台执行限制提供了无缝集成。Rust 实现为网络匿名化带来了内存安全，与 C Tor 相比减少了攻击面。用户可以按中继或全局切换 Tor 模式，客户端透明地处理电路管理。

**Negentropy 同步协议** - [PR #3536](https://github.com/damus-io/damus/pull/3536) 实现了 Negentropy，一个大幅改进同步效率的集合协调协议。Negentropy 交换紧凑指纹 (Merkle 树) 以识别客户端和中继之间的差异事件，而不是下载自上次连接以来的所有事件。对于遵循数百个公钥的用户，这将同步带宽从数 MB 减少到数 KB。该实现与 RelayPool 和 SubscriptionManager 集成，跨所有连接的中继启用自动高效同步。

**低数据模式** - [PR #3549](https://github.com/damus-io/damus/pull/3549) 添加了响应用户反馈关于带宽消耗的蜂窝数据节约功能。该模式禁用图像自动加载、视频预取并减少订阅限制。用户在计量连接上可以浏览文本内容而无需担心超过数据上限的恐惧。该实现尊重 iOS 低数据模式设置并为不同媒体类型提供了细粒度控制。

**数据库优化** - [PR #3548](https://github.com/damus-io/damus/pull/3548) 重新编写了用于更快查询和减少磁盘使用的 nostrdb 快照存储。该优化改变了数据库快照如何持久化到磁盘，改进了读取性能和写入放大。这解决了用户对大型事件数据库的电池消耗投诉。

---

本周就到这里。正在构建什么？有新闻要分享？想让我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 DM 联系</a>或在 Nostr 上找到我们。
