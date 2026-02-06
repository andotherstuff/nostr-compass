---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** rust-nostr 发布重大 API 重设计，21 个 PR 全面改造 SDK 架构。Nostria 3.0 推出双窗格导航、列表管理和全新 UI。Vector 添加 SIMD 加速，实现 65 倍至 184 倍的速度提升，并支持 [Marmot](/zh/topics/marmot/) 协议用于加密群组消息。Frostr 通过 TestFlight 将门限签名引入 iOS。Damus 实现 [NIP-19 (Bech32 编码实体)](/zh/topics/nip-19/) 中继提示以实现跨中继内容发现。Primal Android 添加 NWC 加密和钱包交易导出。nostr-tools 和 NDK 获得可靠性改进。NIP-82（软件应用程序）扩展覆盖 98% 的设备平台。NIPs 仓库合并了 [NIP-47 (Nostr Wallet Connect)](/zh/topics/nip-47/) 的 hold invoice 支持。新的协议提案包括用于播客的 NIP-74、用于浏览器事件数据库的 NIP-DB，以及用于去中心化内容审核的 TRUSTed Filters 套件。新项目包括用于内容迁移的 Instagram to Nostr v2、启动去中心化 3D 打印市场的 Pod21、引入 AI 代理管理社区的 Clawstr，以及扩展直播和视频通话功能的 Shosho 和 NosCall。

## 新闻

### rust-nostr 发布重大 API 重设计

[rust-nostr](https://github.com/rust-nostr/nostr) SDK 本周进行了重大架构改造，21 个合并的 PR 在整个库中引入了破坏性变更。此次重设计影响了大多数 Rust 开发者依赖的核心 API。

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245) 重新设计了通知 API，[PR #1244](https://github.com/rust-nostr/nostr/pull/1244) 将 `RelayNotification::Shutdown` 替换为 `RelayStatus::Shutdown` 以实现更清晰的状态处理。签名器 API 现在通过 [PR #1243](https://github.com/rust-nostr/nostr/pull/1243) 与其他 SDK 模式保持一致。客户端和中继方法通过 [PR #1242](https://github.com/rust-nostr/nostr/pull/1242) 进行了清理，客户端选项现在使用构建器模式（[PR #1241](https://github.com/rust-nostr/nostr/pull/1241)）。

消息发送 API 在 [PR #1240](https://github.com/rust-nostr/nostr/pull/1240) 中重新设计，REQ 取消订阅在 [PR #1239](https://github.com/rust-nostr/nostr/pull/1239) 中重新设计，中继移除在 [PR #1229](https://github.com/rust-nostr/nostr/pull/1229) 中重新设计。一个[开放的 PR #1246](https://github.com/rust-nostr/nostr/pull/1246) 添加了阻塞 API 支持以完善此次重设计。

这些变更为 SDK 带来了一致性，但现有项目需要迁移工作。基于 rust-nostr 构建的开发者在升级前应仔细查看更新日志。

### Instagram to Nostr v2 实现内容迁移

一款新工具使创作者能够将现有内容从中心化平台迁移到 Nostr。[Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2) 支持从 Instagram、TikTok、Twitter 和 Substack 导入，无需访问用户的私钥。

该工具解决了一个常见的入门障碍：不愿在新平台从头开始的用户现在可以保留他们的内容历史。它还支持向新用户赠送 Nostr 账户或向现有账户建议内容，使其有助于帮助他人过渡到该协议。

### Pod21：去中心化 3D 打印网络

[Pod21](https://github.com/gobrrrme/Pod21) ([pod21.com](https://pod21.com)) 使用 Nostr 进行市场协调，连接 3D 打印机运营商和买家。该平台包括一个兼容 [NIP-17 (私密直接消息)](/zh/topics/nip-17/) 的 DM 机器人来处理市场交互，允许买家通过加密直接消息请求打印和与制造商协商。

制造商列出他们的打印能力和规格；买家浏览列表并通过机器人发起订单。该架构遵循与其他 Nostr 商务应用类似的模式：基于中继的发现、用于订单协调的加密消息，以及 Lightning 结算。Pod21 与 Ridestr 和 Shopstr 一起成为通过该协议协调现实世界交易的 Nostr 应用。

### Clawstr：AI 代理社交网络

[Clawstr](https://github.com/clawstr/clawstr) 作为一个 Reddit 风格的平台推出，AI 代理在 Nostr 上创建和管理社区。该平台使自主代理能够建立主题社区、策划内容并与用户互动。社区的功能类似于 subreddit，但由 AI 版主和策展人引导讨论。该架构使用 Nostr 的开放协议进行代理对代理和代理对人类的交互，为去中心化社交媒体上的社区形成建立了新模式。

## 版本发布

### Ridestr v0.2.0：RoadFlare 版本

[Ridestr](https://github.com/variablefate/ridestr) 发布了 [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0)，名为「RoadFlare 版本」，引入了个人拼车网络。该功能让乘客可以将喜欢的司机添加到受信任的网络中。司机批准关注者并共享加密位置，使乘客能够看到受信任的司机何时在线且在附近。行程请求直接发送给已知司机。

支付可靠性通过自动托管恢复、跨设备更好的钱包同步以及通过渐进式轮询实现的更快支付处理得到改善。[PR #37](https://github.com/variablefate/ridestr/pull/37) 添加了支持这些功能的第 5-6 阶段基础设施。[v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1) 随后发布了支付对话框错误和行程后「添加到收藏」流程的热修复。

### Nostria 3.0

[Nostria](https://github.com/nostria-app/nostria)，sondreb 为全球规模构建的跨平台客户端，发布了 3.0 版本，带来全新的 UI、新标志和数百个修复。此版本代表了六周密集开发周期的成果。

双窗格导航是最大的用户体验变化，允许桌面用户在列表、详情和线程之间切换时减少上下文切换。新的首页部分提供所有可用功能的概览，所有页面共享统一的工具栏、布局和功能。

列表管理是最重要的功能更新，贯穿整个应用程序。用户可以管理个人资料列表并在任何功能中过滤内容：直播、音乐或信息流。厌倦了线程中的垃圾信息？按收藏过滤只查看他们的回复。快速 Zaps 添加了一键 zapping，支持可配置的金额。复制/截图生成剪贴板截图以便在任何地方分享事件。静音词现在可以过滤个人资料字段（name、display_name、NIP-05），使用户能够用一个禁用词屏蔽所有桥接的个人资料。设置变为可搜索以加快配置更改。

该版本添加了 BOLT11 和 BOLT12 支付请求渲染、文字大小和字体选择，以及消息部分的「自我备忘」消息功能，支持渲染引用的内容如文章和事件。新的分享对话框支持通过电子邮件、网站或直接消息快速分享给多个收件人。其他功能包括自定义表情符号集、兴趣（作为动态信息流的话题标签列表）、书签、公共中继信息流，以及完整的菜单自定义，包括 Nostria 图标打开的选项。

可在 Android、iOS、Windows 和 [nostria.app](https://www.nostria.app/) 网页版上使用。

### Applesauce v5.1.0

hzrd149 的 [Applesauce](https://github.com/hzrd149/applesauce) 库套件在所有包中发布了 v5.1.0。[applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0) 添加了对 Nostr Connect 远程签名器的 `switch_relays` 和 `ping` 方法的支持，对程序化管理签名器连接很有用。[applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0) 引入了用于并行异步加载的 `loadAsyncMap`。[applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0) 为 `useAction().run()` 添加了 padding 参数。[applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0) 更新了事件到存储的映射以直接处理字符串而无需 `onlyEvents`。

### nak v0.18.3

fiatjaf 的 [nak](https://github.com/fiatjaf/nak)（Nostr Army Knife）发布了 [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3)，包含来自 mattn 的稳定性修复。该版本防止了当铸造厂 URL 缺少 `://` 分隔符时的崩溃，在使用日期值之前验证 dateparser 错误，并处理 AUTH 挑战标签解析中的边缘情况。这些防御性修复使 CLI 在处理格式错误的输入时更加健壮。

### Aegis v0.3.7

[Aegis](https://github.com/ZharlieW/Aegis)，跨平台桌面签名器，发布了 [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7)，添加了支持 [NIP-07 (浏览器扩展接口)](/zh/topics/nip-07/) 签名的 Nostr 应用浏览器支持。该版本记录 [NIP-04 (加密直接消息)](/zh/topics/nip-04/) 和 [NIP-44 (版本化加密)](/zh/topics/nip-44/) 加密事件，允许用户跟踪哪些应用程序请求加密操作。浏览器部分现在按平台过滤只显示 Web 应用。

### Bitchat v1.5.1 (iOS)

[Bitchat](https://github.com/permissionlesstech/bitchat)，使用 Nostr 和蓝牙网格的离线消息应用，发布了 [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1)，包含 iOS 安全加固。[PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) 在处理前验证 Nostr 事件签名，拒绝无效的 giftwrap 和嵌入数据包，限制超大负载，并阻止伪造的 BLE 广播发送者 ID。[PR #998](https://github.com/permissionlesstech/bitchat/pull/998) 通过将发送者 ID 绑定到连接 UUID 来修复 iOS BLE 网格身份验证，防止网格网络中的身份伪造。[PR #972](https://github.com/permissionlesstech/bitchat/pull/972) 添加了通知速率限制，以防止附近有多个网格设备时的对等发现洪水。

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app) 发布了 [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495)，通过 [PR #148](https://github.com/keychat-io/keychat-app/pull/148) 添加了 [NIP-47](/zh/topics/nip-47/) Nostr Wallet Connect 支持。用户现在可以在消息应用内连接外部 Lightning 钱包进行支付。该版本还添加了 macOS 桌面通知。

### Nostrmo v3.5.0

[Nostrmo](https://github.com/haorendashu/nostrmo)，跨平台 Flutter 客户端，发布了 [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0)，全面改造其信息流系统。更新用可自定义的替代方案取代了固定信息流：通用信息流、提及信息流和中继信息流，每个都可以通过新的编辑页面进行配置。该版本实现了 outbox 模型支持以实现更好的事件路由，并扩展了本地中继功能，支持可配置的大小限制和订阅。

### Shosho v0.11.1

[Shosho](https://github.com/r0d8lsh0p/shosho-releases)，Nostr 直播应用，发布了 [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1)，具有录制和 VOD 功能。更新添加了显示谁在观看直播的房间在场指示器、用于更好讨论组织的线程聊天对话，以及通过 [NIP-46](/zh/topics/nip-46/) 在 iOS 上的 Nostr Connect 支持。主播现在可以保存他们的广播供以后观看，同时保持与观众的实时聊天互动。

### NosCall v0.5.0

[NosCall](https://github.com/sanah9/noscall)，Nostr 音频和视频通话应用，发布了 [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release)，支持按类别组织通话的联系人群组、用于连接优化的中继管理，以及用于改善 NAT 穿透的可配置 ICE 服务器设置。该版本还添加了深色模式支持。NosCall 使用 Nostr 进行通话信令和协调，实现无需中心化服务器的点对点通话。

### diVine 1.0.4

[diVine](https://github.com/divinevideo/divine-mobile)，rabble 的短视频循环客户端，在提交 Zapstore 之前发布了 [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4) 作为 Android 预发布 alpha 版本。该版本专注于测试 Nostr 密钥管理，包括 nsec 导入、使用 nsecBunker 和 Amber 的 [NIP-46 (Nostr Connect)](/zh/topics/nip-46/) 远程签名，以及 nostrconnect:// URL 处理。团队正在征求关于中继兼容性和与其他客户端视频互操作性的反馈。[PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265) 修复了导致视频剪辑在应用更新后无法使用的 iOS 文件路径处理问题，改为存储相对路径而非绝对容器路径。[PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251) 修复了从评论查看个人资料时的导航问题。

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus) 发布了 [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2) 稳定版，整合了[之前版本中报道的 NWC 修复](/zh/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---nwc-fixes)。

### Frostr Igloo iOS TestFlight

[Frostr](https://github.com/FROSTR-ORG) ([frostr.org](https://frostr.org/)) 在 [TestFlight](https://testflight.apple.com/join/72hjQe3J) 上推出了 [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios)，将门限签名扩展到 Apple 设备。Frostr 使用 FROST（灵活的轮次优化 Schnorr 门限）签名将 nsec 密钥分割成分布在多个设备上的份额，实现具有容错能力的 k-of-n 签名。以「演示模式」加入的用户参与实时 2-of-2 门限签名实验，展示协议的实时协调能力。iOS 版本加入了 [Igloo for Android](https://github.com/FROSTR-ORG/igloo-android)（v0.1.2），后者于 12 月发布，支持 [NIP-55 (Android 签名器)](/zh/topics/nip-55/) 用于跨应用签名请求。两个移动客户端补充了 [Igloo desktop](https://github.com/FROSTR-ORG/igloo-desktop) 和 [Frost2x](https://github.com/FROSTR-ORG/frost2x) 浏览器扩展。

## 项目更新

### Damus 实现 NIP-19 中继提示

[Damus](https://github.com/damus-io/damus) 合并了 [PR #3477](https://github.com/damus-io/damus/pull/3477)，实现了用于事件获取的 [NIP-19](/zh/topics/nip-19/) 中继提示消费。该功能通过从 [NIP-10 (回复线程)](/zh/topics/nip-10/)、[NIP-18 (转发)](/zh/topics/nip-18/) 和 NIP-19 引用中提取提示，实现在用户配置池之外的中继上查看笔记。实现使用带引用计数清理的临时中继连接，避免永久扩展中继池。

其他修复包括 Lightning 发票解析（[PR #3566](https://github.com/damus-io/damus/pull/3566)）、钱包视图加载（[PR #3554](https://github.com/damus-io/damus/pull/3554)）、中继列表时序（[PR #3553](https://github.com/damus-io/damus/pull/3553)），以及个人资料预加载以减少视觉「弹跳」（[PR #3550](https://github.com/damus-io/damus/pull/3550)）。一个[草稿 PR #3590](https://github.com/damus-io/damus/pull/3590) 显示 [NIP-17](/zh/topics/nip-17/) 私密 DM 支持正在进行中。

### Primal Android 发布 NWC 加密

[Primal Android](https://github.com/PrimalHQ/primal-android-app) 本周非常活跃，合并了 18 个专注于钱包基础设施的 PR。该应用现在与 Spark（Lightspark 的自托管 Lightning 协议）集成。[PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) 添加了 NWC 加密支持，[PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872) 在连接建立时发送 NWC 信息事件。

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870) 支持钱包交易的 CSV 导出，对会计和税务目的很有用。[PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716) 在笔记编辑器中添加了本地账户切换器。多个钱包恢复修复（[PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876)、[PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875)、[PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)）解决了使用非 Spark 钱包配置用户的边缘情况。

### Marmot TypeScript SDK 添加消息历史

[Marmot](https://github.com/marmot-protocol/marmot) 协议的 TypeScript 实现继续开发。hzrd149 的 [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) 为参考聊天应用实现了带分页的消息历史持久化，[PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39) 改善了库的易用性。

在 Rust 端，[PR #161](https://github.com/marmot-protocol/mdk/pull/161) 实现了可重试的状态处理以在失败时保留消息上下文，[PR #164](https://github.com/marmot-protocol/mdk/pull/164) 切换到 std::sync::Mutex 以避免 SQLite 的 tokio 崩溃。whitenoise-rs 后端添加了 [Amber 集成](https://github.com/marmot-protocol/whitenoise-rs/pull/418)（[PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)），[升级到 MDK 和 nostr-sdk 0.44](https://github.com/marmot-protocol/whitenoise-rs/pull/467)（[PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)），并通过 [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460) 引入了实时通知流，支持 NewMessage 和 GroupInvite 事件类型。

### HAVEN 添加定期 WoT 刷新

[HAVEN](https://github.com/bitvora/haven)，个人中继，合并了 [PR #108](https://github.com/bitvora/haven/pull/108)，添加了定期 [Web of Trust](/zh/topics/web-of-trust/) 刷新。该功能确保信任评分随着用户社交图谱的演变保持最新，随时间提高垃圾过滤的准确性。

### nostr-tools

[nostr-tools](https://github.com/nbd-wtf/nostr-tools)，核心 JavaScript 库，本周收到多项改进。提交包括[修复 NIP-27 (文本笔记引用)](/zh/topics/nip-27/) 提及中[换行符后话题标签解析的修复](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5)、[带空闲跟踪的损坏中继对象自动清理](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2)用于连接清理、[消息队列移除](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638)用于单线程性能优化，以及[源文件导出](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139)用于更好的 TypeScript 导入。

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk) 发布了 [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0)，[修复了设备睡眠/唤醒周期后的重新连接和陈旧连接处理](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3)，解决了移动应用的可靠性问题。

### Notedeck

[Notedeck](https://github.com/damus-io/notedeck)，Damus 团队的桌面客户端，有一个[开放的 PR #1279](https://github.com/damus-io/notedeck/pull/1279) 添加 [NIP-34 (Git 协作)](/zh/topics/nip-34/) 查看器。这将支持在客户端内直接浏览发布到 Nostr 中继的 git 仓库、补丁和问题，使 Notedeck 成为基于 ngit 工作流程的潜在前端。

### njump

[njump](https://github.com/fiatjaf/njump)，Nostr Web 网关，通过 [PR #152](https://github.com/fiatjaf/njump/pull/152) 添加了对两种 [NIP-51 (列表)](/zh/topics/nip-51/) 事件类型的支持。该网关现在渲染 kind:30000 关注集（客户端可以在不同上下文中显示的用户分类分组）和 kind:39089 入门包（为分享和群组关注设计的策划个人资料集合）。这些添加让 njump 在用户分享 nevent 链接时显示社区策划的列表。

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst)，Android 客户端，修复了阻止从播放器视图分享视频的错误（[PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)）。「分享视频」选项无法显示是因为内容参数没有传递给控制按钮组件。用户现在可以直接从播放器将 Nostr 视频内容分享到其他应用。[PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693) 修复了解析某些格式错误事件时发生的 Jackson JSON 反序列化崩溃。

### Jumble

[Jumble](https://github.com/CodyTseng/jumble)，专注于中继信息流浏览的 Web 客户端，在 [PR #743](https://github.com/CodyTseng/jumble/pull/743) 中添加了通过剪贴板上传音频文件的功能。用户现在可以直接将音频文件粘贴到帖子编辑器中，文件会上传到配置的媒体服务器并将 URL 嵌入笔记。该功能与现有的图片粘贴功能相同。

### Flotilla

[Flotilla](https://github.com/coracle-social/flotilla)，hodlbod 的 [NIP-29 (基于中继的群组)](/zh/topics/nip-29/) 社区客户端，通过 [PR #270](https://github.com/coracle-social/flotilla/pull/270) 发布了通知功能。更新将警报系统从基于锚点的轮询重构为 Web 的本地拉取通知和移动端的推送通知。该架构实现了提议的 NIP-9a 标准（见下文 [PR #2194](https://github.com/nostr-protocol/nips/pull/2194)），用户向中继注册 webhook 回调，当过滤器匹配时接收加密事件负载。

### Formstr

[Formstr](https://github.com/abh3po/nostr-forms)，Nostr 原生表单应用，在 [PR #422](https://github.com/abh3po/nostr-forms/pull/422) 中添加了表单导入和加密表单支持。用户现在可以通过响应链接或其他 Formstr 实例导入现有表单。加密功能允许表单创建者限制响应，只有指定的接收者才能阅读提交内容，对收集敏感信息的调查很有用。

### Pollerama

[Pollerama](https://github.com/abh3po/nostr-polls) ([pollerama.fun](https://pollerama.fun))，基于 [nostr-tools](https://github.com/nbd-wtf/nostr-tools) 构建，通过 [PR #141](https://github.com/abh3po/nostr-polls/pull/141) 和 [PR #142](https://github.com/abh3po/nostr-polls/pull/142) 添加了 [NIP-17](/zh/topics/nip-17/) DM 分享投票功能。用户现在可以通过加密直接消息直接向联系人分享投票。

### Nostrability Schemata

[Nostrability schemata](https://github.com/nostrability/schemata)，Nostr 事件的 JSON 验证模式集合，通过 [PR #59](https://github.com/nostrability/schemata/pull/59) 添加了 [NIP-59 (Gift Wrap)](/zh/topics/nip-59/) 覆盖。更新包括 kind 13（seal）和 kind 1059（gift wrap）事件的模式，补充了现有的 [NIP-17](/zh/topics/nip-17/) 模式覆盖。

### Vector

[Vector](https://github.com/VectorPrivacy/Vector)，使用 [NIP-17](/zh/topics/nip-17/)、[NIP-44](/zh/topics/nip-44/) 和 [NIP-59](/zh/topics/nip-59/) 实现零元数据加密的隐私专注桌面消息应用，合并了 [PR #39](https://github.com/VectorPrivacy/Vector/pull/39)，引入了 SIMD 加速性能优化。十六进制编码快 65 倍，图像预览生成快达 38 倍，通过二进制搜索索引消息查找快 184 倍。该 PR 为 Apple Silicon 添加了 ARM64 NEON 内联函数，为 Windows 和 Linux 添加了带运行时检测的 x86_64 AVX2/SSE2。内存使用下降，消息结构从 472 字节减少到 128 字节，npub 存储通过驻留减少 99.6%。

Vector v0.3.0（2025 年 12 月）集成了 [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk) 用于基于 MLS 协议的群组消息，为客户端带来了具有前向保密性的端到端加密群组。MIP-04 文件共享现在处理 MLS 群组的 imeta 附件，为与 [White Noise](/zh/newsletters/2026-01-28-newsletter/#marmot-protocol-updates) 的互操作性而设计。该版本还引入了带有基于 WebXDC 的 P2P 多人游戏的 Mini Apps 平台、名为 The Nexus 的去中心化应用商店、用于应用内支付的 PIVX 钱包集成、带完整历史跟踪的消息编辑，以及图像上传期间 4 倍内存减少。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-47：Hold Invoice 支持](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/zh/topics/nip-47/) 现在支持 hold invoice，实现接收者必须明确结算或取消支付的高级支付工作流程。该 PR 添加了三个新的 RPC 方法：`make_hold_invoice` 使用预生成的 preimage 和支付哈希创建 hold invoice，`settle_hold_invoice` 通过提供原始 preimage 领取支付，`cancel_hold_invoice` 使用支付哈希拒绝支付。新的 `hold_invoice_accepted` 通知在付款人锁定支付时触发。这支持付费解锁内容、市场托管系统和支付网关等用例。[Alby Hub](https://github.com/getAlby/hub/pull/1298)、[Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382) 和 [dart NDK](https://github.com/relaystr/ndk/pull/147) 已在实现中。

- **[NIP-05：小写要求](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (域名验证)](/zh/topics/nip-05/) 现在明确要求 `nostr.json` 文件中的十六进制公钥和本地名称都使用小写。这在规范中是隐含的但未说明，导致某些实现使用混合大小写而其他实现规范化为小写时出现互操作性问题。验证 NIP-05 标识符的客户端现在应该拒绝任何包含大写字符的密钥或名称的 `nostr.json` 响应。

- **[NIP-73：国家代码](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (地理标签)](/zh/topics/nip-73/) 现在支持 ISO 3166 国家代码作为 geohash 的替代方案。事件可以包含 `["g", "US", "countryCode"]` 标签来指示国家级位置而无需精确坐标。这为不需要或不希望精确位置的应用程序提供了基于国家的内容过滤和发现。该 PR 还向规范文档添加了缺失的 geohash 示例。

**开放 PR 和讨论：**

- **[NIP-82：软件应用程序](https://github.com/nostr-protocol/nips/pull/1336)** - franzap 宣布对此草案规范进行重大更新，该规范定义了如何使用 kind 30063 发布事件通过 Nostr 分发软件应用程序。更新现在覆盖全球约 98% 的设备平台，包括 macOS、Linux、Windows、FreeBSD、WASM 环境、VS Code 扩展、Chrome 扩展和 Web Bundles/PWA。团队接下来将专注于 Android、PWA 和 iOS 支持，邀请开发者汇聚到这个共享标准。Zapstore 计划在未来几周迁移到新格式。

- **[NIP-74：播客](https://github.com/nostr-protocol/nips/pull/2211)** - 定义播客节目（kind 30074）和剧集（kind 30075）的可寻址事件。节目包括标题、描述、类别和封面图像等元数据。剧集引用其父节目并包括封装 URL、时长和章节标记。该规范与 Podcasting 2.0 元数据标准集成，并包含用于通过 Lightning 实现 V4V（价值换价值）货币化的价值标签。像 [transmit.fm](https://transmit.fm) 这样的 Nostr 原生播客发布平台可以使用此格式直接发布到中继，使播客作者能够在没有中介的情况下分发内容。

- **[NIP-FR：仅朋友可见笔记](https://github.com/nostr-protocol/nips/pull/2207)** - 提议一种使用名为 ViewKey 的共享对称密钥发布仅对用户定义的朋友列表可见的笔记的机制。作者使用 NIP-44 用 ViewKey 加密笔记（kind 2044）。ViewKey 本身通过 [NIP-59 (Gift Wrap)](/zh/topics/nip-59/) 一次性分发给每个朋友。拥有 ViewKey 的朋友可以解密和阅读笔记；其他人只能看到密文。当作者移除一个朋友时，ViewKey 会进行轮换：生成新密钥并通过 gift wrap 重新分发给所有剩余朋友，确保被移除的朋友无法访问未来的帖子。这种方法将内容加密（对称，高效）与密钥分发（非对称，逐友）分离，保持协议轻量级的同时实现了频繁请求的隐私功能。

- **[NIP-DB：浏览器 Nostr 事件数据库接口](https://nostrhub.io/e/1a451c1581888215ae5c311d36c8a7c7d9e5e81f1f4010de4afaf7fcbd553e90)** ([spec](https://github.com/hzrd149/nostr-bucket/blob/master/nip.md)) - 提议为提供本地 Nostr 事件存储的浏览器扩展提供标准的 `window.nostrdb` 接口。API 包括添加事件、按 ID 或过滤器查询、计数匹配和订阅更新的方法。Web 应用程序可以使用此接口从本地缓存的事件读取而无需发起中继请求，减少带宽和延迟。hzrd149 的 [nostr-bucket](https://github.com/hzrd149/nostr-bucket) 浏览器扩展提供了参考实现，将接口注入所有浏览器标签。配套的 [polyfill 库](https://github.com/hzrd149/window.nostrdb.js) 使用 IndexedDB 为没有扩展的环境实现相同的 API。

- **[TRUSTed Filters](https://nostrhub.io/e/237667820943d1c8bbe7ab7732623ae51b337f177776ece439d4a8be84708eb7)** - 用于去中心化内容审核的五个相关提案套件，基于 vitorpamplona 的已合并的 [Trusted Assertions PR #1534](https://github.com/nostr-protocol/nips/pull/1534)。核心规范引入 kind 17570 事件用于声明信任提供者偏好，允许用户指定他们信任哪些服务进行事件过滤和排名。信任提供者发布断言（kind 37571）、统计（kind 37572）和排名（kind 37573），客户端可以订阅。该系统使用插件架构，通过 W/w 标签指定过滤器类型和转换。这使得垃圾检测、信誉评分和内容排名等计算密集型操作能够在专用基础设施上运行，同时用户保持对信任哪些提供者的控制。该套件包括过滤器预设、用户排名、可信事件和插件定义的单独规范。

- **[NIP-9a：推送通知](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod 提议使用 kind 30390 注册事件的基于中继的推送通知标准。用户创建一个包含他们想接收事件过滤器和 webhook 回调 URL 的注册。注册加密到中继的 pubkey（来自其 NIP-11 `self` 字段）。当匹配事件发生时，中继 POST 到回调，包含事件 ID（明文用于去重）和事件本身（NIP-44 加密到用户）。这种架构让中继推送通知同时保护事件内容免受中间推送服务器的影响。Flotilla 的 [PR #270](https://github.com/coracle-social/flotilla/pull/270) 实现了此标准。

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - 提议使用 kind 33400 事件的带托管的去中心化合同工作协议。系统定义三个角色：仲裁者宣布可用性和条款，赞助者创建带托管 Bitcoin 资金的任务，自由代理完成工作以领取支付。仲裁者在需要时解决争议。该协议实现无信任的自由职业工作协调，资金锁定直到交付物被接受或仲裁结束。

## NIP 深入解析：NIP-47 (Nostr Wallet Connect)

[NIP-47](/zh/topics/nip-47/) 定义了 Nostr Wallet Connect (NWC)，一种使用 Nostr 作为通信层进行远程 Lightning 钱包控制的协议。随着本周 hold invoice 支持的添加，NWC 现在涵盖了完整的 Lightning 操作范围。

该协议通过简单的交换工作。钱包应用发布一个「钱包信息」事件（kind 13194）描述其功能。客户端应用发送加密请求（kind 23194）要求钱包执行支付发票、创建发票或检查余额等操作。钱包以加密结果（kind 23195）响应。

NWC 在客户端和钱包之间使用 [NIP-44](/zh/topics/nip-44/) 加密，使用专用密钥对进行钱包操作，与用户的主身份分开。这种分离意味着泄露 NWC 连接不会暴露用户的 Nostr 身份。

**支持的方法：**

规范定义了核心 Lightning 操作的方法：`pay_invoice` 发送支付，`make_invoice` 生成用于接收的发票，`lookup_invoice` 检查支付状态，`get_balance` 返回钱包余额，`list_transactions` 提供支付历史。新合并的 `pay_keysend` 支持无发票支付，`hold_invoice` 支持条件支付。

**示例事件：**

钱包服务发布一个信息事件（kind 13194）宣传其功能：

```json
{
  "kind": 13194,
  "pubkey": "<wallet service pubkey>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

客户端发送加密请求（kind 23194）支付发票：

```json
{
  "kind": 23194,
  "pubkey": "<client ephemeral pubkey from connection URI secret>",
  "content": "<NIP-44 encrypted: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<wallet service pubkey>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<client ephemeral key signature>"
}
```

钱包服务响应（kind 23195）支付结果：

```json
{
  "kind": 23195,
  "pubkey": "<wallet service pubkey>",
  "content": "<NIP-44 encrypted: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<client ephemeral pubkey>"],
    ["e", "<request event id>"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

响应中的 `e` 标签引用原始请求，允许客户端将响应与其请求匹配。

**Hold Invoice：**

本周的 [PR #1913](https://github.com/nostr-protocol/nips/pull/1913) 添加了 hold invoice 支持，实现托管式支付。与接收者通过释放 preimage 立即领取支付的标准发票不同，hold invoice 让接收者推迟此决定。当付款人发送到 hold invoice 时，资金沿支付路径锁定。然后接收者选择结算（释放 preimage 并领取资金）或取消（拒绝支付，将资金返还给付款人）。如果两种操作都没有发生，支付超时，资金自动返还。该 PR 添加了三个 NWC 方法：`make_hold_invoice`、`settle_hold_invoice` 和 `cancel_hold_invoice`，加上 `hold_invoice_accepted` 通知。这种机制为 Ridestr 的拼车托管和市场争议解决等应用提供动力。

**当前实现：**

主要钱包支持 NWC：Zeus、Alby 和 Primal（从本周的 [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) 开始）都实现了钱包端支持。在客户端方面，Damus、Amethyst 和大多数主要 Nostr 客户端可以连接到 NWC 钱包进行 zapping 和支付。

该协议实现了关注点分离：用户可以在一个设备上运行钱包，同时从另一个设备与 Nostr 交互，Nostr 中继作为通信渠道。这种架构意味着移动客户端不需要直接持有资金，通过将钱包基础设施与社交客户端分开来提高安全性。

**安全注意事项：**

NWC 连接应被视为敏感信息。虽然加密保护消息内容，但钱包 pubkey 和连接密钥必须妥善保管。应用程序应允许用户撤销连接并设置消费限额。该协议支持功能限制，因此钱包可以限制特定连接可以执行的操作。

## NIP 深入解析：NIP-59 (Gift Wrap)

[NIP-59](/zh/topics/nip-59/) 定义了一种将任何 Nostr 事件封装在多层加密中的协议，向中继和观察者隐藏发送者身份。本周提出的仅朋友可见笔记（NIP-FR）和推送通知（NIP-9a）提案都依赖 gift wrapping，使其成为值得理解的基础隐私原语。

**三个层次：**

Gift wrapping 使用三个嵌套结构：

1. **Rumor**（未签名事件）：作为 Nostr 事件的原始内容，没有签名。rumor 不能直接发送到中继，因为中继拒绝未签名事件。

2. **Seal**（kind 13）：rumor 使用 [NIP-44](/zh/topics/nip-44/) 加密并放入 kind 13 事件中。seal 由实际作者的密钥签名。这是作者身份的密码学证明。

3. **Gift Wrap**（kind 1059）：seal 被加密并放入由随机一次性密钥对签名的 kind 1059 事件中。gift wrap 包含用于路由到接收者的 `p` 标签。

**常见误解：可否认性**

规范提到未签名的 rumor 提供「可否认性」，但这具有误导性。seal 层由真实作者签名。当接收者解密 gift wrap 然后解密 seal 时，他们有谁发送消息的密码学证明。接收者甚至可以构建零知识证明来揭示发送者身份而不暴露自己的私钥。

Gift wrap 实际提供的是**对观察者的发送者隐私**：中继和第三方无法确定谁发送了消息，因为他们只能看到由随机密钥签名的 gift wrap。但接收者总是知道，并且可以证明。

**示例事件：**

这是规范中的完整三层结构（发送「你今晚去派对吗？」）：

Rumor（未签名，不能发布到中继）：
```json
{
  "created_at": 1691518405,
  "content": "Are you going to the party tonight?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

Seal（kind 13，由真实作者签名，包含加密的 rumor）：
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

Gift wrap（kind 1059，由随机临时密钥签名，包含加密的 seal）：
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

注意：seal 的 `pubkey` 是真实作者（`611df01...`），而 gift wrap 的 `pubkey` 是随机一次性密钥（`18b1a75...`）。中继只能看到 gift wrap，因此无法将消息归属于真实作者。

**每层保护什么：**

Rumor 未签名，不能直接发布到中继。Seal 由真实作者签名，向接收者证明作者身份。Gift wrap 由随机一次性密钥签名，向中继和观察者隐藏真实作者。只有接收者才能解密两层以到达原始内容并验证作者在 seal 上的签名。

**当前应用：**

[NIP-17 (私密直接消息)](/zh/topics/nip-17/) 使用 gift wrap 进行加密 DM，取代了旧的 NIP-04 方案。提议的NIP-FR（仅朋友可见笔记）使用Gift Wrapping向朋友分发ViewKey，朋友随后使用这些密钥解密加密的笔记。NIP-9a（推送通知）使用 gift wrap 原理加密通知负载。

**元数据保护：**

时间戳应随机化以阻止时序分析。中继应在提供 kind 1059 事件之前要求 AUTH，并且只向标记的接收者提供。发送给多个接收者时，为每个人创建单独的 gift wrap。

---

本周就到这里。正在构建什么？有新闻要分享？希望我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 私信联系我们</a>或在 Nostr 上找到我们。
