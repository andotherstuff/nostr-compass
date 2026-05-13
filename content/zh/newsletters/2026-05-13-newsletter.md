---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-13-newsletter.md
translationDate: 2026-05-13
---

欢迎回到 Nostr Compass，您每周的 Nostr 协议开发指南。

**本周：** [Nostr VPN](https://github.com/mmalmi/nostr-vpn) 在七天内[发布了八个版本](#nostr-vpn-发布八个版本最终达到-v4010)，从重新设计的设备配对流程到将 TCP 吞吐量大约翻倍的 FIPS AEAD 交换。[Marmot Protocol](https://github.com/marmot-protocol)（[White Noise](https://github.com/marmot-protocol/whitenoise) 的基础）发布了[完成用户屏蔽功能的前端版本](#marmotwhite-noise-发布完成用户屏蔽的前端版本以及-mdk-和后端的-31-个-pr)以及 MDK 和后端的 31 个 PR。[Grain](https://github.com/0ceanSlim/grain) 发布了 [v0.6.0](#grain-v060-新增-nip-40nip-50nip-70-和-nip-45)，在一个里程碑中实现了四个新的 NIP。[Citrine](https://github.com/greenart7c3/Citrine) 发布了 [v3.0.0-pre1](#citrine-v300-pre1-内置-tor-和-relay-聚合)，带有内置 Tor 和 relay 聚合。[Amber](https://github.com/greenart7c3/Amber) 发布了 [v6.1.0-pre2](#amber-v610-pre2-改善新应用连接流程)，改善了连接流程和签名。[Alby Hub](https://github.com/getAlby/hub) 发布了 [v1.22.2](#alby-hub-v1222-新增-ai-和代理页面以及-core-lightning-支持)，带有 AI 和代理页面以及 Core Lightning 集成。[Mostro](https://github.com/MostroP2P/mostro) 发布了并发 taker bond 和 [mostro-core v0.11.0](#mostro-发布并发-taker-bond-和-mostro-core-v0110)。[Jumble](https://github.com/CodyTseng/jumble) 发布了[五个版本](#jumble-发布五个版本包含最近搜索和账户持久化)，带有最近搜索历史和账户数据持久化修复。[Nostrord](https://github.com/nostrord/nostrord) 发布了[三个版本](#nostrord-发布群组分享弹窗媒体上传和-arch-linux-包)，带有群组分享弹窗和 Arch Linux 包。[Flotilla](https://flotilla.social) 发布了 [1.8.0](#flotilla-180-发布视频通话邮件渲染和房间提及)，带有视频通话、邮件渲染和房间提及。[Calendar by Formstr](https://calendar.formstr.app) 发布了 [v1.5.1](#calendar-by-formstr-发布-v151-包含预约调度和-android-日历同步)，带有预约调度和 Android 日历同步。[Tamagostrich](https://github.com/Negr087/tamagostrich) 推出了去中心化的 NIP-78 虚拟宠物游戏，带有 sats 奖励。NIP 讨论涉及预约、托管服务、住宿列表、链上 Zap 和可验证社区规则。两个 NIP 深度解析涵盖 NIP-78（应用特定数据）和 NIP-98（HTTP 认证）。

## 头条故事

### Nostr VPN 发布八个版本最终达到 v4.0.10

[Nostr VPN](https://github.com/mmalmi/nostr-vpn)，基于 Rust 的去中心化网状 VPN，使用 Nostr 进行对等发现并使用 FIPS 支持的 noise 协议作为数据平面，本周在 macOS、Linux、Windows 和 Android 上发布了从 [v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) 到 [v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) 的八个版本。

主要变化在 [v4.0.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.8)：AEAD 从 RustCrypto 的 `chacha20poly1305` 软件后端换为 `ring` 0.17 中 BoringSSL 的 ChaCha20-Poly1305，在 aarch64 上使用手工调优的 NEON，在 x86_64 上使用 AVX2/AVX-512。相同硬件上的 Docker 基准测试显示 2 节点直接 TCP 吞吐量从 437 跳升至 1097 Mbps。线格式不变。

本周早些时候，[v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) 重建了设备配对流程，带有出口节点泄漏保护、出口节点下统一的 WireGuard 配置块以及签名/公证的 macOS 构件。[v4.0.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.2) 通过可重用多播套接字改善了 LAN 发现。[v4.0.9](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.9) 在 UDP 发送路径上添加了 `sendmmsg(2)` 批处理，在 8 包批次中分摊每包 `sendto` 系统调用，将 TCP 单流推至 1548 Mbps（1.45×）。[v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) 发布了设备配对的完整 UX 改版："邀请设备"和"加入网络"现在是独立的卡片，粘贴 `nvpn://invite/` 字符串时自动导入触发，附近配对分为两个独立的 15 分钟开关。

### Marmot/White Noise 发布完成用户屏蔽的前端版本以及 MDK 和后端的 31 个 PR

[White Noise](https://github.com/marmot-protocol/whitenoise)，基于 [Marmot](/zh/topics/marmot/) MLS 协议构建的私人群组消息应用，于 5 月 7 日发布了 [v2026.5.7+24](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.5.7+24)，这是完成屏蔽功能集的前端版本。上一个版本发布了静音、搜索和归档；这个版本完成了屏蔽。被屏蔽的用户现在从邀请、聊天预览、消息时间线、搜索结果和通知中隐藏，其消息不再计入未读徽章。视频附件在所有设备上端到端运行。离线通知现在覆盖每个屏幕。

支持工作跨越 MDK 和后端的 31 个 PR。MDK 落地了 [PR #258](https://github.com/marmot-protocol/mdk/pull/258)，带有扩展 v3 线格式和 `disappearing_message_secs` 架构，为消息自动删除奠定基础。

前端工作包括 [PR #653](https://github.com/marmot-protocol/whitenoise/pull/653) 通过切换到点查询修复了归档聊天摘要，[PR #644](https://github.com/marmot-protocol/whitenoise/pull/644) 向 Dart 暴露了 `subscribe_to_group_state` 流用于响应式 UI 更新，[PR #635](https://github.com/marmot-protocol/whitenoise/pull/635) 修复了签名应用冷启动时的 Android 外部签名通知恢复。

### Grain v0.6.0 新增 NIP-40、NIP-50、NIP-70 和 NIP-45

[Grain](https://github.com/0ceanSlim/grain)，基于 Go 的 Nostr relay 和客户端库，于 5 月 6 日发布了 [v0.6.0](https://github.com/0ceanSlim/grain/releases/tag/v0.6.0)，包含四个新的 NIP 实现和一次生产加固。v0.6 里程碑新增了 [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) 事件过期、[NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) 全文搜索、[NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) 受保护事件和 [NIP-45](https://github.com/nostr-protocol/nips/blob/master/45.md) 事件计数。

通过 NIP-40 的事件过期允许发布者设置过期时间戳，relay 在过期后丢弃事件，实际上用于临时存在事件和有时限的公告。NIP-50 全文搜索允许客户端在 REQ 消息中发出 `search` 过滤器并让 relay 完成匹配工作。通过 NIP-70 的受保护事件防止 relay 在未经作者明确许可的情况下重新分享事件。NIP-45 计数查询允许客户端请求 relay 返回匹配事件的计数，降低"这个用户有多少条笔记"类查询的带宽。

该版本还发布了生产加固：更安全的默认配置、更正的 NIP-01 拒绝响应以及对慢速消费者的更好背压。

## 本周发布

### Citrine v3.0.0-pre1 内置 Tor 和 relay 聚合

[Citrine](https://github.com/greenart7c3/Citrine)，将手机变成 Nostr relay 节点的 Android 应用，本周以预发布形式发布了 [v3.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0-pre1)。主要新增内容是用于隐私保护 relay 访问的内置 Tor 支持和 relay 聚合，Citrine 可以从多个上游 relay 拉取事件并向本地客户端提供服务。[PR #139](https://github.com/greenart7c3/Citrine/pull/139) 为高效的基于集合对账的事件同步添加了 [NIP-77（熵减对账）](/zh/topics/nip-77/) 支持。[PR #137](https://github.com/greenart7c3/Citrine/pull/137) 通过 Tor 代理路由所有 URL，[PR #133](https://github.com/greenart7c3/Citrine/pull/133) 缓解了事件接收路径上的 UI 线程压力，[PR #132](https://github.com/greenart7c3/Citrine/pull/132) 降低了 relay 聚合器的电池消耗。该版本还添加了一个事件分析视图，带有按 kind 分解存储事件的饼图。

### Amber v6.1.0-pre2 改善新应用连接流程

[Amber](https://github.com/greenart7c3/Amber)，用于 [NIP-55（Android 签名应用）](/zh/topics/nip-55/) 和 [NIP-46](/zh/topics/nip-46/) 的 Android 签名应用，发布了 [v6.1.0-pre2](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre2)。主要修复：签名对话框现在在接受 bunker 请求后正确关闭，格式错误的 bunker 请求显示无效请求屏幕，并为基于 intent 的签名请求添加了速率限制。[PR #430](https://github.com/greenart7c3/Amber/pull/430) 修复了签名流程中的内存泄漏和热路径低效问题。

### Alby Hub v1.22.2 新增 AI 和代理页面以及 Core Lightning 支持

[Alby Hub](https://github.com/getAlby/hub)，自托管 Lightning 节点和 Nostr Wallet Connect 服务器，发布了 [v1.22.2](https://github.com/getAlby/hub/releases/tag/v1.22.2)，带有多项重要新增内容。新的 AI 和代理页面向 AI 代理和兼容 MCP 的工具暴露了 Alby Hub 的 Lightning 和 NWC 功能。集成的链上钱包模式让用户可以直接从 Alby Hub 接收和发送链上比特币。交易的自定义用户标签改善了记账。设置页面重新设计以提高清晰度，创建应用连接时的预算选择也得到改善。自发布以来最受欢迎的功能终于来了：Core Lightning（CLN）现在是与 LND 和 LDK 并列的支持后端。

### Mostro 发布并发 taker bond 和 mostro-core v0.11.0

[Mostro](https://github.com/MostroP2P/mostro)，Nostr 上的点对点比特币交易协议，本周合并了 11 个 PR，推进了 taker bond 功能，该功能通过要求双方在交易进行前锁定资金来防止扰乱。[PR #733](https://github.com/MostroP2P/mostro/pull/733) 实现了并发 taker bond，多个 taker 可以同时提交 bond 发票，第一个锁定的获胜，其他的被丢弃。[PR #735](https://github.com/MostroP2P/mostro/pull/735) 将 bond 发票备注与规范第 6.1 节对齐。

[mostro-core](https://github.com/MostroP2P/mostro-core) 发布了 [v0.11.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.11.0)，带有匹配的库新增内容：[PR #144](https://github.com/MostroP2P/mostro-core/pull/144) 添加了 `Action::PayBondInvoice` 和 `Status::WaitingTakerBond`，[PR #143](https://github.com/MostroP2P/mostro-core/pull/143) 添加了用于管理员结算和取消操作的 `BondResolution` 负载。[mostro-cli](https://github.com/MostroP2P/mostro-cli) 发布了 [v0.15.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.15.0)，更新至 mostro-core 0.11.0 并处理反滥用 bond 流程。

### Jumble 发布五个版本包含最近搜索和账户持久化

[Jumble](https://github.com/CodyTseng/jumble)，以 relay 为中心的 Nostr 客户端，可作为 Web 应用和 Electron 桌面应用使用，本周发布了五个版本：[v26.5.2](https://github.com/CodyTseng/jumble/releases/tag/v26.5.2) 到 [v26.5.6](https://github.com/CodyTseng/jumble/releases/tag/v26.5.6)。v26.5.2 按今天/本周/本月/更早分组通知，带有固定日期标题，并用原生组件替换了第三方下拉刷新库。v26.5.3 在 `.dmg` 旁边发布 macOS `.zip` 以便 Electron 桌面构建可以应用原地自动更新。v26.5.4 添加了自实现的 emoji 选择器，带有 emoji 包标签。v26.5.5 添加了最近搜索历史。v26.5.6 修复了一个关键持久化错误：账户和缓存数据现在在渲染器移至稳定的 `app://` 来源后可以在完整应用重启后存活。

### Nostrord 发布群组分享弹窗、媒体上传和 Arch Linux 包

[Nostrord](https://github.com/nostrord/nostrord)，面向 NIP-29 基于 relay 的群组的 Nostr 客户端，本周发布了 [v1.0.0](https://github.com/nostrord/nostrord/releases/tag/v1.0.0)、[v1.0.1](https://github.com/nostrord/nostrord/releases/tag/v1.0.1) 和 [v1.0.2](https://github.com/nostrord/nostrord/releases/tag/v1.0.2)。v1.0.1 通过 AUR 以 `nostrord-bin` 发布 Arch Linux 包，带有 PGP 签名的 `.pkg.tar.zst` 构件（[PR #44](https://github.com/nostrord/nostrord/pull/44)），在忙碌频道中向上滚动时的跳转到最新按钮（[PR #45](https://github.com/nostrord/nostrord/pull/45)），以及直接在聊天输入中粘贴图片和媒体（[PR #46](https://github.com/nostrord/nostrord/pull/46)）。v1.0.2 通过 [PR #49](https://github.com/nostrord/nostrord/pull/49) 添加了群组分享，带有分享弹窗，生成 `nostr:naddr` URI（kind 39000，NIP-19 + NIP-21）和 Web 友好的 `nostrord.com/open/` 链接。

### FIPS v0.3.0 发布跨平台覆盖、Nostr 对等发现和未修改 LAN 网关

[FIPS](https://github.com/jmcorgan/fips)（自由互联网互联系统），在 [#20](/zh/newsletters/2026-04-29-newsletter/#fips-新增基于-nostr-的-udpnat-引导) 中介绍的 Nostr 原生网状网络项目，本周发布了 [v0.3.0](https://github.com/jmcorgan/fips/releases/tag/v0.3.0)，这是一个将项目从仅 Linux 扩展到 Linux、macOS、Windows 和 OpenWrt 的重要里程碑。

主要新增内容是带有 STUN 辅助 UDP NAT 穿透的 Nostr 媒介对等发现。节点现在在公共 Nostr relay 上将签名的覆盖广告发布为 kind:37195 参数化可替换事件。当两个对等节点都在 NAT 后面时，守护进程使用 [NIP-59（礼物包装）](/zh/topics/nip-59/) 信令进行提议/应答交换来协调打洞。

新的 `fips-gateway` 二进制文件允许未修改的 LAN 主机在不运行 FIPS 守护进程的情况下访问网状目标。本周为 Nostr VPN 吞吐量跳升提供动力的相同 ring 0.17 ChaCha20-Poly1305 交换也落地于 FIPS v0.3.0。aarch64 上的基准测试显示两节点 TCP 单流从 437 提升至 1097 Mbps，三节点中继路径 ping 延迟从平均 7.68 ms 下降至 0.72 ms。

### Camelus v1.10.1 发布桌面版本

[Camelus](https://github.com/leo-lox/camelus)，面向 Android 和桌面的 Nostr 客户端，发布了 [v1.10.1](https://github.com/leo-lox/camelus/releases/tag/v1.10.1)，带有 Windows 和 Linux 桌面构建，从仅移动分发扩展。

### Flotilla 1.8.0 发布视频通话、邮件渲染和房间提及

[Flotilla](https://flotilla.social)，hodlbod 的 [NIP-29](/zh/topics/nip-29/) 基于 relay 的群组聊天应用，本周发布了 [1.8.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.8.0)，带有多项值得关注的新增内容。语音房间现在支持视频：参与者可以在通话中打开摄像头或共享屏幕，带有切换到可固定单源视图的网格布局用于屏幕共享。邮件渲染通过 welshman 库更新到来：Flotilla 现在可以接收嵌入 HTML 邮件内容的消息，并内联渲染 HTML，保留格式、图片和链接。房间提及允许用户引用其他房间和 relay，带有可点击的内联链接。空间搜索现在包含消息内容和本地匹配，以及频道名称。iOS 和 Android 上的原生分享表单现在可用于空间邀请链接。聊天中嵌入的日历事件始终显示日期。

### Calendar by Formstr 发布 v1.5.1 包含预约调度和 Android 日历同步

[Calendar by Formstr](https://calendar.formstr.app)（[github.com/formstr-hq/nostr-calendar](https://github.com/formstr-hq/nostr-calendar)），面向公共和私人事件的 Nostr 原生日历应用，于 5 月 10 日发布了 [v1.5.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.0)，于 5 月 11 日发布了 [v1.5.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.1)。[PR #89](https://github.com/formstr-hq/nostr-calendar/pull/89) 带来了预约调度，允许用户在其日历上创建可预订的时间段。[PR #123](https://github.com/formstr-hq/nostr-calendar/pull/123) 中的只读 Android 日历集成将 Nostr 事件同步到设备日历，使其与其他日历应用一起显示。[PR #130](https://github.com/formstr-hq/nostr-calendar/pull/130) 发布了事件通知。v1.5.1 跟进了 URL 错误修复和 ZSP 元数据更新。

## 开发中

### Amethyst 新增定时帖子、NIP-9A 社区规则和桌面本地 relay

[Amethyst](https://github.com/vitorpamplona/amethyst)，功能丰富的 Android 客户端，本周在多个重要功能领域合并了 78 个 PR。

[PR #2765](https://github.com/vitorpamplona/amethyst/pull/2765) 中的定时帖子落地 Android：用户可以撰写笔记并设置未来的发布时间，队列在设备本地管理。桌面构建在 [PR #2841](https://github.com/vitorpamplona/amethyst/pull/2841) 中获得了带有 SQLite 事件持久化的嵌入式本地 relay，允许桌面客户端充当自己的 relay 节点。

三个 PR 直接在客户端实现了 NIP-9A 社区规则：[PR #2798](https://github.com/vitorpamplona/amethyst/pull/2798) 在发送前在编辑器中根据社区规则验证帖子，[PR #2799](https://github.com/vitorpamplona/amethyst/pull/2799) 在新社区流程中添加了结构化 NIP-9A 规则编辑器，[PR #2800](https://github.com/vitorpamplona/amethyst/pull/2800) 添加了可选的 NIP-9A 订阅源过滤器，使社区成员可以隐藏违反已发布规则的帖子。这是本周在 NIPs 存储库中提出的 NIP-9A 草案的首个客户端实现。

[PR #2812](https://github.com/vitorpamplona/amethyst/pull/2812) 在 Quartz 和 Amethyst 的调试日志中编辑了机密和敏感负载，这是对分享崩溃报告的用户的安全修复。[PR #2821](https://github.com/vitorpamplona/amethyst/pull/2821) 为每个发布的 HLS 事件添加了丰富的 [NIP-92（imeta）](/zh/topics/nip-92/) 标签，并自动发布一个 kind:1 辅助笔记，使直播流出现在标准订阅源中，可被不支持 [NIP-53（直播活动）](/zh/topics/nip-53/) 的客户端发现。

### Shopstr 新增 MCP 审计日志和会话安全

[Shopstr](https://github.com/shopstr-eng/shopstr)，Nostr 上的去中心化市场，本周合并了五个 PR。[PR #456](https://github.com/shopstr-eng/shopstr/pull/456) 中的 MCP 工具层审计日志落地，使市场运营者可以追踪代理操作。[PR #477](https://github.com/shopstr-eng/shopstr/pull/477) 中的会话安全收紧，将 MCP 会话固定到其原始 API 密钥并添加 TTL 驱逐以防止会话劫持。

### Dart NDK 新增 Web 支持和 seal 签名验证

[Dart NDK](https://github.com/relaystr/dart_ndk)，Flutter 应用中使用的 Dart Nostr 协议开发库，本周合并了六个 PR。[PR #571](https://github.com/relaystr/dart_ndk/pull/571) 中的 Web 支持通过 `SembastCacheManager` 到来，使 Web 构建可以将缓存事件持久化到浏览器存储。[PR #595](https://github.com/relaystr/dart_ndk/pull/595) 中的 seal 签名验证为 [NIP-59（礼物包装）](/zh/topics/nip-59/) 流落地，使客户端可以确认内部 seal 是由预期发送者创建的。

### rust-nostr 重构标签和代理连接

[rust-nostr](https://github.com/rust-nostr/nostr)，带有 Python、Kotlin、Swift 和 JavaScript 绑定的 Rust SDK，本周合并了三个 PR。[PR #1347](https://github.com/rust-nostr/nostr/pull/1347) 是一个大型标签返工，规范化了整个 SDK 的标签访问。[PR #1351](https://github.com/rust-nostr/nostr/pull/1351) 在 SDK 层用 `Proxy` 替换了 `Connection` 类型，[PR #1349](https://github.com/rust-nostr/nostr/pull/1349) 修复了多过滤器 REQ 的订阅验证。

### Sprout 发布 v0.0.10 和 v0.0.11

[Sprout](https://github.com/block/sprout)，在 [#21](/zh/newsletters/2026-05-06-newsletter/#sprout-发布-desktop-v004-和-v005-以及-nip-oa-代理认证和配对中继边车) 中介绍的 Block 的 Nostr 客户端和 relay，发布了 [v0.0.10](https://github.com/block/sprout/releases/tag/v0.0.10) 和 [v0.0.11](https://github.com/block/sprout/releases/tag/v0.0.11)，带有提及自动补全改进、图片下载支持和代理错误处理修复。

### Clave 继续多账户 NostrConnect 推出

[Clave](https://github.com/DocNR/clave)，在 [#21](/zh/newsletters/2026-05-06-newsletter/#clave-v020-在-ios-上推出-nip-46-nostr-connect-签名的多账户功能) 中介绍的 iOS NIP-46 远程签名者，本周发布了进一步的构建，推进其多账户 NostrConnect 工作。[PR #52](https://github.com/DocNR/clave/pull/52) 将 Connect 从主页视图呈现的表单提升为顶级跨账户标签，所有配对流程的账户绑定都通过统一选择器进行。build 71 中的安全修复关闭了由于 bunker 流程中的时序错误而存在的每账户 5 连接上限绕过，现在在三个层面强制执行：入口门、表单内轮换门和 NSE 侧检查。

## 新项目

### Tamagostrich 推出去中心化 NIP-78 虚拟宠物游戏，带 sats 奖励

[Tamagostrich](https://github.com/Negr087/tamagostrich) 是在 IDENTITY Hackathon 2026 上推出的基于浏览器的虚拟宠物游戏，一只名为 Nori 的雏鸵鸟通过你的 Nostr 社交活动进化。宠物状态存储在 [NIP-78](/zh/topics/nip-78/) kind:30078 事件中，因此它可以在共享相同密钥对的每台设备上同步。Zap、反应、转发和新粉丝授予 XP；没有活动，幸福感和能量每 24 小时衰减 100 点。里程碑奖励通过 [NIP-47（Nostr Wallet Connect）](/zh/topics/nip-47/) 自动以 sats 支付：5 级 50 sats，10 级 210 sats，最高 21 级 420 sats，发送到用户的 `lud16` 地址，索赔状态记录在 NIP-78 事件中以防止重复支付。

## 协议和规范工作

NIPs 存储库合并了 [PR #2338](https://github.com/nostr-protocol/nips/pull/2338)，修复了 Marmot 事件 kind 和地理缓存 kind 37516 的 README 参考链接。本周开放了五个新提案：

[PR #2331](https://github.com/nostr-protocol/nips/pull/2331) 提出了 **NIP-9A：可验证社区规则**，引入 kind:34551，一个参数化可替换事件，允许社区所有者发布机器可读、密码学签名的规则文档。客户端在用户提交帖子前获取规则，如果违反任何规则则在本地拒绝草稿。配套的 [PR #2337](https://github.com/nostr-protocol/nips/pull/2337) 在 NIP-11 relay 信息文档中添加了可选的 `nip9a` 字段。

[PR #2335](https://github.com/nostr-protocol/nips/pull/2335) 提出了 **Nostr 市场的预约事件**，定义 kind:32122（参数化可替换预约事件）、kind:1326（仅追加过渡审计记录）和 kind:32124（交易后评价）。谈判是私下进行的：草案提案作为 NIP-59 礼物包装的结构化消息子事件在买卖双方之间发送，因此它们不会进入公共 relay。

[PR #2334](https://github.com/nostr-protocol/nips/pull/2334) 提出了 **Nostr 市场的托管服务**，使用 kind:30303 供托管运营者声明其 EVM 合约地址、字节码哈希、支持的链、费用表和接受的代币。买卖双方发布 kind:17388 可替换事件声明其信任的托管提供商和接受的支付形式。

[PR #2333](https://github.com/nostr-protocol/nips/pull/2333) 提出了 **NIP-99 市场列表的住宿列表档案**，用 H3 地理空间索引 `g` 标签和针对短期租赁的住宿特定推广字段扩展 NIP-99 分类列表。

[PR #2332](https://github.com/nostr-protocol/nips/pull/2332) 提出了 **NIP-BC：链上 Zap（kind 8333）**，利用 Nostr 密钥和比特币 Taproot 地址之间的直接同一性：Nostr 公钥是 32 字节的 x-only secp256k1 密钥，BIP-341 P2TR 内部密钥也是如此，这意味着任何 Nostr 用户已经拥有一个可从其公钥确定性派生的比特币主网地址，无需 LNURL、托管方或 Lightning 地址。kind 号码反映了 NIP-57 的惯例：9735 是 Lightning P2P 端口；8333 是比特币主网的 P2P 端口。

## NIP 深度解析：NIP-78（应用特定数据）

[NIP-78](/zh/topics/nip-78/) 定义了应用程序使用 Nostr 事件代表用户存储任意私有或公共数据的标准方式。核心事件 kind 是 30078，一个参数化可替换事件，其中 `d` 标签是应用程序定义的标识符字符串。应用程序给其存储槽一个唯一的 `d` 标签（例如 `tamagostrich-pet-state` 或 `amethyst-settings`）并发布带有其需要持久化的 JSON 或文本内容的 30078 事件。由于 30078 是可替换的并按 `d` 标签限定范围，应用程序可以通过发布具有相同 `d` 标签的新事件来更新存储的状态，relay 只保留最新版本。

```json
{
  "id": "<64字符十六进制>",
  "pubkey": "<64字符十六进制>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "tamagostrich-pet-state"]
  ],
  "content": "{\"level\":7,\"xp\":1420,\"happiness\":82,\"energy\":61}",
  "sig": "<128字符十六进制>"
}
```

主要动机是无需集中式服务器的跨设备同步。任何知道用户公钥和应用程序 `d` 标签的客户端都可以从用户的 relay 集获取当前状态，并在任何设备上重建应用程序状态。用户拥有数据，因为它存储在由其密钥对签名的事件中，他们可以根据 [NIP-65（Relay 列表元数据）](/zh/topics/nip-65/) 中的 relay 列表选择发布到哪些 relay。

对于私有应用程序数据，NIP-78 事件可以在发布前使用 [NIP-44（版本化加密）](/zh/topics/nip-44/) 或较旧的 [NIP-04](/zh/topics/nip-04/) 加密内容字段，使 relay 存储只有密钥持有者才能解密的密文。对于公共应用程序数据，如 Tamagostrich 在用户档案上显示的成就徽章，可以不加密存储，使其他客户端可以读取和显示。

该规范故意将内容格式留为开放。应用程序选择自己的架构；NIP-78 只标准化事件 kind 和 `d` 标签范围机制。NIP-78 的当前用户包括 Tamagostrich（宠物状态同步）、Wisp（kind:30078 钱包备份和跨设备安全设置同步）、NosPress（CMS 编排状态）以及多个 Nostr 客户端设置同步实现。

---

**主要来源：**
- [NIP-78 规范](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich)：本周的生产实现

**另见：**
- [NIP-51：列表](/zh/topics/nip-51/)
- [NIP-65：Relay 列表元数据](/zh/topics/nip-65/)

## NIP 深度解析：NIP-98（HTTP 认证）

[NIP-98](/zh/topics/nip-98/) 定义了一种 HTTP 认证方案，允许 Nostr 密钥对授权对 HTTP 服务器的请求，无需用户名、密码或 OAuth 令牌进行服务器端 API 访问。客户端构造一个短期的 kind 27235 Nostr 事件，用其私钥签名，将 JSON base64 编码，并在 `Authorization: Nostr <base64>` HTTP 头中发送。

```json
{
  "id": "<64字符十六进制>",
  "pubkey": "<64字符十六进制>",
  "created_at": 1747180800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<请求体的sha256哈希>"]
  ],
  "content": "",
  "sig": "<128字符十六进制>"
}
```

kind 27235 事件在 `method` 标签中包含 HTTP 方法，在 `u` 标签中包含完整的请求 URL，以及 `created_at` 时间戳。服务器验证签名，检查方法和 URL 与实际请求匹配，并验证时间戳是最近的（几分钟内）以防止重放攻击。如果验证通过，服务器将请求公钥视为已验证身份。

该设计意味着任何实现 NIP-98 的服务器都可以在没有任何事先注册、账户创建或共享密钥的情况下验证 Nostr 用户身份。从用户的角度来看，认证是透明的：他们的 Nostr 签名密钥也是其 API 凭据。

NIP-98 用于 Blossom（[BUD-01](https://github.com/hzrd149/blossom/blob/master/buds/01.md)）的 blob 上传和下载认证。Routstr 将其用于 npub 级 RBAC 的每请求 HTTP API 访问控制。Sprout 将其用于 git 传输认证和 REST relay 访问，在最近的重构中完全替换了 Bearer 令牌认证。Clave 将其用于代理配对调用。Alby Hub 将 NIP-98 派生的认证用于其管理 API，Nostr.build 将其用于上传授权。

该规范定义了一个可选扩展：包含请求体 SHA-256 哈希的 `payload` 标签，允许服务器验证签名事件和请求体是一起创建的，防止中间人在客户端签署认证事件后替换不同的体。

---

**主要来源：**
- [NIP-98 规范](https://github.com/nostr-protocol/nips/blob/master/98.md)
- [BUD-01：Blossom 上传认证](https://github.com/hzrd149/blossom/blob/master/buds/01.md)

**另见：**
- [NIP-96：HTTP 文件存储集成](/zh/topics/nip-96/)
