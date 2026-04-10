---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Amethyst](https://github.com/vitorpamplona/amethyst) 在 [v1.08.0](#amethyst-发布-arti-tor并合并纯-kotlin-版-mls-和-marmot) 中加入 Arti Tor 集成，并重新设计了 Shorts UI，同时还将纯 Kotlin 实现的 [MLS](/zh/topics/mls/) 和 [Marmot](/zh/topics/marmot/) 合并进其 [Quartz](/zh/topics/quartz/) 库。[Nostur](https://github.com/nostur-com/nostur-ios-public) 在 [v1.27.0](#nostur-v1270-增加视频录制和私密回复) 中加入视频录制、动画 GIF 资料图以及私密回复。[Shosho](https://github.com/r0d8lsh0p/shosho-releases) 在 [v0.15.0](#shosho-v0150-推出-shows-和竖屏视频轮播) 中推出 Shows（与 OBS 连接的自定义直播信息）以及类似 TikTok 的竖屏视频轮播。[Nymchat](https://github.com/Spl0itable/NYM) [回退 Marmot 并发布增强版 NIP-17 群聊](#nymchat-回退-marmot并发布增强版-nip-17-群聊)，使用轮换的临时密钥。[Nostr VPN](https://github.com/mmalmi/nostr-vpn) 在六个版本中发布了[出口节点支持和 Umbrel 打包](#nostr-vpn-发布出口节点支持和-umbrel-打包)。[Amber](https://github.com/greenart7c3/Amber) 跳升至 [v6.0.0-pre1](#amber-v600-pre1-增加按连接隔离的-nip-46-签名密钥)，加入按连接隔离的 [NIP-46](/zh/topics/nip-46/) 签名密钥和 Zapstore 应用内更新。[Notedeck](https://github.com/damus-io/notedeck) 达到 [v0.10.0-beta](#notedeck-v0100-beta-发布-zapstore-自更新)，支持通过 Zapstore 进行 APK 自更新，而 [NIP-58](/zh/topics/nip-58/)（Badges）则在本周发生了 [kind 迁移](#nip-更新)。本期的两篇 NIP 深度解析分别是 [NIP-17](/zh/topics/nip-17/)（Private Direct Messages）和 [NIP-46](/zh/topics/nip-46/)（Nostr Remote Signing）。

## 头条

### Amethyst 发布 Arti Tor，并合并纯 Kotlin 版 MLS 和 Marmot

[Amethyst](https://github.com/vitorpamplona/amethyst) 这个由 vitorpamplona 维护的 Android 客户端，发布了从 [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3) 到 [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0) 的四个版本，并将一大批尚未正式发布的工作合并进其 [Quartz](/zh/topics/quartz/) 库，也就是共享的 Kotlin Multiplatform Nostr 模块。最重要的发布是 v1.08.0 “Arti Tor”，它将应用的 Tor 连接从基于 C 的 Tor 库迁移到 [Arti](https://gitlab.torproject.org/tpo/core/arti)，也就是 Tor Project 的 Rust 实现。这次迁移解决了此前 C Tor 绑定下出现的随机崩溃问题。Arti 是 Tor Project 面向长期的 C 代码库替代方案，从零开始以 Rust 编写，以获得内存安全和 async I/O。

v1.07.3 重新设计了 Shorts UI，用 edge-to-edge 信息流替代了原先的分页设计，用于图片、短视频和长视频的浏览。这个版本还将 badges 迁移到 kind `10008`，将 bookmarks 迁移到 kind `10003`，与本周[合并的 NIP-58](/zh/topics/nip-58/) kind 迁移保持一致。v1.07.4 修复了一个 Nostr Wallet Connect secret 处理问题，v1.07.5 则修复了图片上传崩溃。

在主分支上但尚未进入正式 tag 版本的工作中，团队用 Kotlin 完整实现了 [MLS](/zh/topics/mls/) 和 [Marmot](/zh/topics/marmot/) 协议，不再需要依赖原生 C/Rust 库绑定。[PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147) 增加了核心的 Marmot MLS 群消息层，[PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149) 增加了群聊 UI，[PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146) 增加了入站和出站消息处理器以及订阅管理器，[PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141) 增加了 MLS 群状态持久化和 KeyPackage 轮换管理，[PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150) 增加了完整的 MLS 测试套件并改进了 GroupInfo 签名，[PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158) 增加了 KeyPackage 发布状态跟踪。[PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166) 则为 Nostr 加密操作增加了纯 Kotlin 的 secp256k1 实现，替代原生 C 库依赖。结合 Kotlin 版 MLS 实现之后，[Quartz](/zh/topics/quartz/) 已经可以在没有任何原生绑定的情况下运行 Nostr 签名和 Marmot 群消息，这为包括 iOS 在内的 Kotlin Multiplatform 目标打开了空间。

团队也在构建 [NIP-AC](/en/topics/nip-ac/)（P2P Voice and Video Calls）支持：[PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143) 为 NIP-AC 通话状态机增加了完整测试套件，[PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164) 则防止应用重启后过期的 call offer 被再次触发。

### Nostur v1.27.0 增加视频录制和私密回复

[Nostur](https://github.com/nostur-com/nostur-ios-public) 这个 iOS Nostr 客户端，于 4 月 2 日发布了 [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0)。这个版本增加了应用内视频录制和上传前裁剪，用户可以直接拍摄短片、剪到合适长度，然后不离开客户端就发布出去。动画 GIF 支持扩展到了头像和横幅图片，同时也增加了动画 WebP 渲染。新的 Shortcuts 集成允许用户从 Apple Shortcuts 自动化中发送 Nostr 帖子。该版本还增加了私密回复，并修复了影响 Nostur 与其他客户端之间消息送达的 DM 兼容性问题。

### Shosho v0.15.0 推出 Shows 和竖屏视频轮播

[Shosho](https://github.com/r0d8lsh0p/shosho-releases) 这个 Nostr 直播应用，于 4 月 7 日发布了 [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0) 和 [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1)。这轮发布的核心功能是 Shows：主播可以在开播前先设置自定义节目资料，并将节目连接到 OBS 或任何外部编码器。这把“我正在播什么”的元数据与真正开播的动作分离开来，因此主播可以在开始直播前先准备好标题、描述和商品。同一版本还增加了类似 TikTok 的竖屏视频轮播，可以在全屏信息流中滑动浏览直播、片段和回放，并增加了 Quick Add，允许用户直接从个人资料页发布视频片段和添加商品。v0.15.1 修复了键盘遮住直播聊天输入框的 bug。

## 本周发布

### Notedeck v0.10.0-beta 发布 Zapstore 自更新

[Notedeck](https://github.com/damus-io/notedeck) 这个来自 Damus 团队的桌面和移动客户端，发布了 [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1) 和 [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2)，作为 APK 自更新功能的测试预发布版本。[PR #1417](https://github.com/damus-io/notedeck/pull/1417) 在 Android 上通过 Nostr/Zapstore updater 增加了 APK 自更新，延续了[周刊 #14 中报道的 Nostr 原生版本发现工作](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr)。这套更新流程通过发布到 relay 的 Nostr event 发现新版本，然后从开发者托管 APK 的位置下载文件，无论是 GitHub releases、Blossom CDN 还是其他来源，接着将 SHA-256 哈希与已签名的 Nostr event 进行校验，再完成安装。[PR #1438](https://github.com/damus-io/notedeck/pull/1438) 修复了欢迎页中 Login 和 CreateAccount 按钮立即跳回上一页的问题，[PR #1424](https://github.com/damus-io/notedeck/pull/1424) 则修复了 Agentium AI 会话视图中的文本溢出。

### Amber v6.0.0-pre1 增加按连接隔离的 NIP-46 签名密钥

[Amber](https://github.com/greenart7c3/Amber) 这个 [NIP-55](/zh/topics/nip-55/)（Android Signer Application）签名器应用，于 4 月 4 日发布了 [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1)。这次最重要的变化，是为 [NIP-46](/zh/topics/nip-46/)（Nostr Remote Signing）bunker 协议增加了按连接隔离的签名密钥。Amber 现在不再为所有 bunker 连接共用同一个 keypair，而是为每个已连接客户端生成独立的密钥。如果某一个客户端连接被攻破，攻击者也无法冒充该 signer 去影响其他客户端。

[PR #377](https://github.com/greenart7c3/Amber/pull/377) 增加了通过 Zapstore 进行应用内更新检查与安装，使 Amber 与 [Notedeck](#notedeck-v0100-beta-发布-zapstore-自更新) 一起采用 Nostr 原生应用分发。[PR #375](https://github.com/greenart7c3/Amber/pull/375) 通过向用户显示警告而不是直接崩溃的方式，优雅处理 AndroidKeyStore 失败。[PR #371](https://github.com/greenart7c3/Amber/pull/371) 则通过大小限制和内容截断增加数据库清理，防止存储无界增长。这个预发布版本还包含了[上周报道的 v5.0.x 周期](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504)中的 [NIP-42](/zh/topics/nip-42/) relay auth 白名单和助记词恢复短语登录。

### Nostria 发布原生移动应用

[Nostria](https://github.com/nostria-app/nostria) 这个由 SondreB 维护的跨平台 Nostr 客户端，发布了原生 Android 移动应用，并连续发布了从 [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11) 到 [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18) 的八个版本。最重要的新能力是对 [Amber](https://github.com/greenart7c3/Amber) 和 Aegis 这类 signer 的原生本地 signer 支持。项目也提供了适用于 Linux、macOS 和 Windows 的[桌面安装包](https://www.nostria.app/download)。[PR #610](https://github.com/nostria-app/nostria/pull/610) 通过自适应运行时限制和 preview URL 清理降低了信息流内存压力。v3.1.14 修复了与 [Web of Trust](/zh/topics/web-of-trust/) 提供方 Brainstorm 的集成。v3.1.15 则聚焦于音乐相关改进。新的 Android 应用已在 [Zapstore](https://zapstore.dev/apps/app.nostria) 上提供。

### diVine 1.0.8 发布可恢复上传和 DMs

[diVine](https://github.com/divinevideo/divine-mobile) 这个短视频客户端发布了 [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8)，其中包含 87 个已合并 PR。可恢复上传让创作者在不稳定网络下可以按 chunk 继续中断的上传，而不必从头开始。该版本还加入了视频质量和 bitrate 设置、双击点赞，以及 DM 改进。[PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722) 为桌面视频采集加入了 macOS camera plugin，[PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820) 则将通知系统迁移到带 enrichment 和 grouping 的 BLoC 架构。团队还用 OpenMoji SVG 替换了 AI 生成的贴纸和分类插图（[PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844)、[PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)）。

### Manent v1.3.0 增加敏感笔记模糊和 NIP-42 认证

[Manent](https://github.com/dtonon/manent) 这个私密加密笔记与文件存储应用，于 4 月 2 日发布了 [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0)。用户现在可以将笔记标记为敏感内容，在列表视图中将其模糊显示，从而在日常滚动浏览时隐藏私密内容。该版本还增加了 [NIP-42](/zh/topics/nip-42/)（Authentication of Clients to Relays）支持，使 Manent 能在 relay 要求认证时先完成认证再发送 event。Manent 使用用户的 keypair 将所有数据加密后存储在 Nostr relay 上，因此 NIP-42 支持扩大了它可用于存储的 relay 范围。

### Wisp v0.17.0 到 v0.17.3 增加直播 zaps 和钱包备份

[Wisp](https://github.com/barrydeen/wisp) 这个 Android Nostr 客户端，连续发布了从 [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta) 到 [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta) 的六个版本，合并了 44 个 PR。v0.17.0 增加了钱包备份安全提示和 zap UX 改进。[v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta) 增加了跨平台直播聊天可见性以及直播 zap 功能。[PR #423](https://github.com/barrydeen/wisp/pull/423) 增加了自动搜索资料、zap 成功动画和用户状态改进。[PR #426](https://github.com/barrydeen/wisp/pull/426) 修复了带大型 tag 列表 event 在 `computeId` 中触发的 out-of-memory 崩溃。v0.16.x 系列则增加了 emoji shortcode 自动补全、群聊 UI 改进，以及贯穿所有通知路径的已屏蔽用户过滤。

### Mostro 发布深层链接、Nostr 汇率和重复付款修复

[Mostro](https://github.com/MostroP2P/mostro) 这个构建在 Nostr 上的点对点 Bitcoin 交易所，本周在服务器守护进程和移动客户端两侧都有更新。服务器端方面，[PR #692](https://github.com/MostroP2P/mostro/pull/692) 防止过期订单写入导致重复付款，这个 bug 可能让卖家在同一笔交易中被支付两次。[PR #693](https://github.com/MostroP2P/mostro/pull/693) 则对 dev_fee 写入使用定向更新，而不是整单覆盖。

[Mostro Mobile](https://github.com/MostroP2P/mobile) 这个 Flutter 客户端，于 4 月 3 日发布了 [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3)。该版本可以处理来自不同 Mostro 实例的深层链接，因此用户点开链接时会被正确路由到相应的交易服务器。[PR #498](https://github.com/MostroP2P/mobile/pull/498) 在后台通知管线中检测管理员和 dispute DMs，应用现在还会优先通过 Nostr 获取汇率，并在失败时回退到 HTTP/cache。[PR #560](https://github.com/MostroP2P/mobile/pull/560) 修复了一个 relay 连接阻塞 bug，该问题会在某些网络条件下阻止应用连上 relay。

### Unfiltered v1.0.12 增加 hashtags 和 comments

[Unfiltered](https://github.com/dmcarrington/unfiltered) 这个偏重图片内容的 Nostr 客户端，发布了 [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12)。[PR #69](https://github.com/dmcarrington/unfiltered/pull/69) 增加了 hashtag 支持，[PR #72](https://github.com/dmcarrington/unfiltered/pull/72) 增加了在帖子上撰写和显示 comments 的能力。[PR #71](https://github.com/dmcarrington/unfiltered/pull/71) 修复了单帖多图时的导航问题。

### Primal Android 发布钱包多账户共享和 remote signer 自动重连

[Primal](https://github.com/PrimalHQ/primal-android-app) 这个 Android Nostr 客户端，于 4 月 7 日发布了一个版本更新。新版本增加了钱包多账户共享，以及 Dev Tools 中带删除钱包功能的 overflow menu。remote signer 现在会在连接断开时自动重连，钱包服务也获得了自己的自动重连逻辑。修复内容包括：投票 zap 票不再显示为 Top Zaps、空投票选项不再触发崩溃、未配置钱包时隐藏钱包余额，以及将 WalletException 类型映射为 NWC 响应中的错误码。

### Titan v0.1.0 推出原生 nsite:// 浏览器和 Bitcoin 名称注册

[Titan](https://github.com/btcjt/titan) 这个面向 Nostr Web 的原生桌面浏览器，于 4 月 7 日发布了 [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0)。Titan 通过查询注册在 Bitcoin 上的人类可读名称来解析 `nsite://` URL，随后从 Nostr relay 获取站点内容 event，并渲染从 [Blossom](/zh/topics/blossom/) 服务器取回的页面。最终得到的是一种不依赖 DNS、不依赖 TLS 证书、也不依赖托管服务商的 Web 浏览体验。名称通过一个与 Bitcoin 交易绑定的[网页界面](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register)进行注册。首个版本以 macOS `.dmg` 形式发布（ARM，并通过 Rosetta 2 支持 Intel），同时也包含 Nix 开发环境支持。

### Bikel v1.5.0 为去 Google 化手机加入原生前台服务

[Bikel](https://github.com/Mnpezz/bikel) 这个将骑行活动转化为公共基础设施数据的去中心化骑行追踪器，于 4 月 4 日发布了 [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0)。该版本从依赖 GMS 的 Expo TaskManager 迁移到自定义原生前台服务，以确保在 LineageOS、GrapheneOS 和其他去 Google 化 Android 变体上也能可靠进行后台骑行追踪。Bikel Bot 还获得了 dual-pocket 架构，并通过 Cashu nutzaps 实现自动 eCash 收取。v1.4.3 和 v1.4.2 修复了非标准 Android 环境中的后台追踪同步问题，应用还增加了 OSM 自行车停放点地图开关。

### Sprout 增加 NIP-01、NIP-23 和 NIP-33 支持

[Sprout](https://github.com/block/sprout) 这个由 Block 构建并内置 Nostr relay 的通信平台，于 4 月 6 日发布了 [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7)。本周团队增加了对 [NIP-23](/en/topics/nip-23/)（Long-form Content）kind `30023` 文章、[NIP-33](/en/topics/nip-33/) 参数化可替换 event 及其以 `d` tag 为键的替换机制，以及 [NIP-01](/zh/topics/nip-01/)/[NIP-02](/en/topics/nip-02/) kind `1` 文本笔记和 kind `3` follow list 的支持。该版本还增加了带 54 个主题的自适应 IDE 主题系统、workflow 和 agent run history 的 UX 打磨，以及成员侧边栏清理。

### mesh-llm v0.56.0 发布分布式配置协议

[mesh-llm](https://github.com/michaelneale/mesh-llm) 这个使用 Nostr keypair 作为节点身份的分布式 LLM 推理系统，于 4 月 7 日发布了 [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0)。该版本增加了带所有权语义的分布式配置协议、非对称 KV cache 量化（Q8_0 keys 搭配 Q4 values）以降低内存占用、用于身份 keystore 的 OS keychain 存储、带消息排队的平滑聊天流，以及对全屏布局和使用 flash attention 时 KV cache 拆分问题的修复。

### Nostr VPN 发布出口节点支持和 Umbrel 打包

[Nostr VPN](https://github.com/mmalmi/nostr-vpn) 这个使用 Nostr relay 进行信令、使用 WireGuard 建立加密隧道的点对点 VPN，本周连续发布了从 [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0) 到 [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6) 的六个版本。v0.3.x 周期在 Windows 和 macOS 上增加了出口节点支持，使 peer 可以通过网络中的其他节点转发互联网流量。invite 和 alias 传播现在也通过 Nostr 同步，因此用户可以在不依赖带外协调的情况下共享网络访问。该系列版本还增加了面向自托管部署的 Umbrel 打包、利用记忆的公网 endpoint 进行 NAT punch-through、自动清理过期出口节点，以及已发布的协议规范。项目同时稳定了 macOS 的 route 处理，加入自愈默认路由和 underlay 修复，并通过 Tauri 增加了 Android 构建。当前可提供的构建包括 macOS（Apple Silicon 和 Intel）、Linux（AppImage 和 .deb）、Windows 和 Android。

### Nymchat 回退 Marmot，并发布增强版 NIP-17 群聊

[Nymchat](https://github.com/Spl0itable/NYM) 这个具备 MLS 能力的聊天客户端，连续发布了从 [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261) 到 [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274) 的 14 个版本。最重要的变化是协议方向调整：[v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261) 增加了 Marmot MLS 群聊，但 [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268) 又回退到 [NIP-17](/zh/topics/nip-17/)，因为 Marmot 的多设备支持尚未完成，这导致群聊状态在多设备之间同步时出现问题。v3.58.271 引入了增强版 NIP-17 群聊，为所有消息使用轮换的临时密钥，目标是防止时序和关联攻击。这一周的更新还带来了对设置具备细粒度控制的 friend system（[v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)）、加密应用设置中的 MLS 群聊消息同步，以及多项 relay 连接修复。

### nak v0.19.5 增加 Blossom 多服务器和 outbox 发布

[nak](https://github.com/fiatjaf/nak) 这个 fiatjaf 的命令行 Nostr 工具包，发布了 [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5)。`blossom` 命令现在接受多个 `--server` 参数，可以在一次调用中上传到多个 [Blossom](/zh/topics/blossom/) 服务器。新的 `key` 命令可以通过左侧补零来扩展不完整的 key。`event` 命令增加了 `--outbox` 标志，用于通过 outbox model 发布 event，而 `fetch` 在没有返回 event 时现在会以错误码退出。

## 开发中

### White Noise 增加 thumbhash 预览和 push registration bridge

[White Noise](https://github.com/marmot-protocol/whitenoise) 这个基于 [Marmot](/zh/topics/marmot/) 协议的私密信使，本周合并了五个 PR。[PR #549](https://github.com/marmot-protocol/whitenoise/pull/549) 用 thumbhash 替换了 blurhash 图片预览，这是一种更新的算法，能以更小的载荷生成更清晰的占位图像，通常低于 30 字节，而 blurhash 大约需要 50 到 100 字节，同时还能保留原图的宽高比和颜色分布。blurhash 仍然保留为旧内容的回退方案。[PR #548](https://github.com/marmot-protocol/whitenoise/pull/548) 更新了 whitenoise-rs，并加入 [MIP-05](/zh/topics/mip-05/) push registration bridge，将[上周的 push notification 规范工作](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications)接到客户端中。[PR #493](https://github.com/marmot-protocol/whitenoise/pull/493) 为聊天消息增加了基于 cursor 的分页，用滚动驱动的方式替代此前的加载策略。

### Route96 增加动态标签配置和零出口流量清理

[Route96](https://github.com/v0l/route96) 这个由 v0l 构建的 [Blossom](/zh/topics/blossom/) 媒体服务器，合并了三个 PR。[PR #80](https://github.com/v0l/route96/pull/80) 通过 admin API 增加了动态 label model 配置，使运营者无需重启服务器就能切换内容分类模型。[PR #82](https://github.com/v0l/route96/pull/82) 为 admin UI 增加了标签配置字段。[PR #79](https://github.com/v0l/route96/pull/79) 则增加了 zero-egress 文件清理策略，自动删除那些从未被下载过的文件，从而帮助运营者压低存储成本。

### Snort 发布安全加固和 DVM 支付发票

[Snort](https://github.com/v0l/snort) 这个 Web 客户端，本周发布了两个版本，并完成了一次全面的安全审计。修复内容包括 Schnorr 签名验证、[NIP-46](/zh/topics/nip-46/) relay 消息伪造防护，防止攻击者通过已被攻破的 relay 注入签名请求，以及 PIN 加密改进和移除对 NIP-26 delegation 的信任。性能提升则来自 WASM 中的批量 Schnorr 验证、lazy-loaded routes、预编译翻译，以及取消每个 event 的双重验证。[PR #618](https://github.com/v0l/snort/pull/618) 增加了 [NIP-90](/en/topics/nip-90/)（Data Vending Machine）kind `7000` payment-required 发票显示，因此当 DVM 返回支付要求时，Snort 会直接在信息流中渲染 Lightning invoice。

### Damus 改进 LMDB 压缩

[Damus](https://github.com/damus-io/damus) 这个 iOS 客户端，合并了 [PR #3719](https://github.com/damus-io/damus/pull/3719)，按计划周期自动执行 LMDB 压缩，防止本地数据库随着时间推移无界增长。[PR #3663](https://github.com/damus-io/damus/pull/3663) 则改进了 BlurOverlayView，使其看起来像一种保护措施，而不是坏掉的界面。

### Captain's Log 增加 tag 索引和笔记同步

[Captain's Log](https://github.com/nodetec/captains-log)（Comet）这个来自 Nodetec 的 Nostr 原生长文写作工具，本周合并了四个 PR。[PR #156](https://github.com/nodetec/captains-log/pull/156) 为笔记增加了 tag 索引和跨笔记同步支持，[PR #157](https://github.com/nodetec/captains-log/pull/157) 重构了笔记同步和 tag 处理，[PR #159](https://github.com/nodetec/captains-log/pull/159) 则修复了已删除笔记的同步问题，确保被删除的笔记在各设备间仍保持删除状态。

### Relatr v0.2.x 重新设计插件系统，并推出 Nostr 原生验证器市场

[Relatr](https://github.com/ContextVM/relatr) 这个 [Web of Trust](/zh/topics/web-of-trust/) 评分引擎，通过社交图距离和可配置验证器计算信任排名，发布了 v0.2.x 系列，并对插件系统进行了完整重构。验证器现在使用 Elo 编写，这是一种可移植的函数式表达语言，经过分叉后支持多步骤的宿主编排能力，例如 Nostr 查询、社交图查找和 NIP-05 解析。插件以 kind `765` 的 Nostr event 发布，使分发过程天然适配 relay 网络。新的[插件市场](https://relatr.net)让运营者可以在浏览器中发现、安装和加权验证器，同时还提供一个 CLI（`relo`）用于本地编写和发布。整体架构是沙箱化的：插件只能调用宿主明确提供的能力，因此恶意验证器无法逃逸出其既定作用域。Relatr 实例现在还可以通过网站进行管理，运营者可以完整看到评分算法由哪些插件构成，以及各自的权重。

### Shopstr 改进移动端导航和访问控制

[Shopstr](https://github.com/shopstr-eng/shopstr) 这个使用 Bitcoin 买卖商品的 Nostr 原生市场，本周在主应用和配套项目 [Milk Market](https://github.com/shopstr-eng/milk-market) 上一共推进了 158 次提交。修复内容包括移动端社区布局改进、导航时菜单自动关闭，以及 dropdown 自动关闭。受保护路由现在不能再通过直接输入 URL 的方式绕过登录，同时 slug 匹配逻辑现在也能正确处理多个精确匹配结果。

### Pollerama 增加通知、电影搜索和评分 UI

[Pollerama](https://github.com/formstr-hq/nostr-polls) 这个基于 Nostr 的投票、问卷和社交评分应用，增加了线程通知、电影搜索功能，以及评分 UI 重构。该版本还修复了信息流加载问题，并升级了依赖版本。

### Purser 构建带 Marmot 加密的 Nostr 原生支付守护进程

[Purser](https://github.com/EthnTuttle/purser) 这个设计为 Zaprite 替代品的 Nostr 原生支付守护进程，本周合并了九个 PR，持续搭建其核心架构。该项目通过 MDK 使用 [Marmot](/zh/topics/marmot/) MLS，为商户和客户之间的消息提供加密，并使用 Strike 和 Square 作为支付提供方。本周落地的内容包括配置和目录加载、消息 schema 校验、MDK 通信层、Strike 和 Square provider 实现、polling engine、anti-spam rate limiting、待处理支付持久化以及订单处理管线。在团队移除 mock MLS、改为在本地模式中使用真实加密之后，全部 99 个测试现在都在运行真实的 mdk-core MLS 操作。

### Vector 重构 DM 附件并增加资料编辑

[Vector](https://github.com/VectorPrivacy/Vector) 这个以隐私为重点、基于 Tauri 构建的 Nostr 私信客户端，合并了 [PR #55](https://github.com/VectorPrivacy/Vector/pull/55)，对前端进行了重构。DM 附件解密和保存逻辑已迁移到 vector-core 库中，应用现在也支持资料编辑。上传取消标志已通过 TauriSendCallback 正确串接，未使用的附件预览回调也被清理掉了。

## 协议与规范工作

### NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-58](/zh/topics/nip-58/)（Badges）：Profile Badges 迁移到 kind 10008，Badge Sets 迁移到 kind 30008**（[PR #2276](https://github.com/nostr-protocol/nips/pull/2276)）：将 Profile Badges 从 kind `30008` 迁移到 kind `10008`，也就是每个 pubkey 一个的可替换 event，并为 Badge Sets 引入 kind `30008`。此前，Profile Badges 与 Badge 定义共用同一个 kind（`30008`），因此它们都是由 `d` tag 键控的参数化可替换 event。新的 kind `10008` 是简单可替换 event：每个 pubkey 一个，不需要 `d` tag。客户端现在只需为每个用户查询一个可替换 event，而不是扫描参数化可替换 event。Amethyst v1.07.3 已经带上了这次迁移。

- **[NIP-34](/zh/topics/nip-34/)（Git Stuff）：增加与 git 相关的 follow lists**（[PR #2130](https://github.com/nostr-protocol/nips/pull/2130)）：为 NIP-34 仓库和 issue 跟踪增加了 follow list 约定。用户可以发布 kind `30000` 的 follow set，使用 `git-repos` 或 `git-issues` 这样的 `d` tag，并在其中通过 `a` tag 引用他们想跟踪的仓库（kind `30617`）。客户端可以订阅这些 follow set，在用户信息流中展示仓库活动，类似于 kind `3` 联系人列表对 pubkey 的作用方式。

**开放 PR 和讨论：**

- **NIP-AC：通过 WebRTC 进行点对点语音和视频通话**（[PR #2301](https://github.com/nostr-protocol/nips/pull/2301)）：在最初由 0xChat 实现的 NIP-100 基础上，草案提出了三个变化：迁移到 [NIP-44](/zh/topics/nip-44/) 加密，并包裹在 [NIP-59](/zh/topics/nip-59/) gift wraps 中以消除元数据泄露；明确语音和视频通话建立的 WebRTC 工作流，包括 offer、answer 和 ICE candidates；以及一种 mesh 群组通话模型，其中每个 peer 都与其他所有 peer 建立直接 WebRTC 连接。该规范与 NIP-100 不向后兼容。Amethyst 已经开始围绕它开发，本周落地了通话状态机测试套件（[PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)）以及过期 call offer 处理（[PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)）。

- **[NIP-340](/en/topics/nip-340/)（FROST Quorum）**（[PR #2299](https://github.com/nostr-protocol/nips/pull/2299)）：提出了在 Nostr 上进行 [FROST](/zh/topics/frost/)（Flexible Round-Optimized Schnorr Threshold）门限签名的约定。FROST 允许一组签名者共同控制一个 Nostr 身份，只要满足 t-of-n 条件，成员就能在不重建完整私钥的情况下签署 event。该 NIP 定义了如何协调签名轮次、分发密钥份额以及发布门限签名 event，并建立在来自 [FROSTR 项目](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11)的 Igloo signer 工作之上。

- **[NIP-5D](/en/topics/nip-5d/)（Nostr Web Applets）**（[PR #2303](https://github.com/nostr-protocol/nips/pull/2303)）：定义了一套 `postMessage` 协议，使运行在 iframe 中的沙箱化 Web 应用，也就是“napplets”，能够与宿主应用，也就是“shell”，通信。shell 通过结构化消息 API 向 napplet 提供 Nostr 签名、relay 访问和用户上下文，而 iframe 沙箱则阻止其直接访问密钥。这将 [NIP-5A](/en/topics/nip-5a/) 的静态网站托管模型进一步推进到可读写 Nostr event 的交互式应用。该 NIP 目前正在积极开发中，并已有可运行的 runtime 实现。

- **[NIP-5C](/en/topics/nip-5c/)（Scrolls）**（[PR #2281](https://github.com/nostr-protocol/nips/pull/2281)）：此前名为 NIP-A5 提案。它定义了在 Nostr 上发布和发现 WebAssembly 程序的约定。WASM 二进制被存储为 Nostr event，客户端则可以在沙箱化 runtime 中下载并执行它们。一个[演示应用](https://nprogram.netlify.app/)展示了在浏览器中运行 scrolls 的方式，其中示例程序以 Nostr event 发布，任何客户端都可以获取并执行。

- **[NIP-85](/zh/topics/nip-85/)（Trusted Assertions）：澄清说明**（[PR #2304](https://github.com/nostr-protocol/nips/pull/2304)）：收紧了关于单个服务提供方使用多个 key 和多个 relay 的规范表述，明确客户端应如何处理那些跨多个 pubkey 或 relay endpoint 运营的提供方所发布的 assertions。

- **[NIP-24](/zh/topics/nip-24/)（Extra Metadata Fields）：为可替换 event 增加 published_at**（[PR #2300](https://github.com/nostr-protocol/nips/pull/2300)）：将 [NIP-23](/en/topics/nip-23/)（Long-form Content）中的 `published_at` tag 泛化到所有可替换和可寻址 event。这个 tag 只用于显示：如果 `published_at` 等于 `created_at`，客户端将 event 显示为在该时间“创建”；如果两者不同，也就是 event 被更新过，客户端就可以显示为“更新于”。这样 kind `0` 资料可以显示“joined at”日期，其他可替换 event 也可以在更新后保留原始发布时间戳。与之配套的 [NIP-51](/zh/topics/nip-51/) 提案（[PR #2302](https://github.com/nostr-protocol/nips/pull/2302)）则把同样的 tag 加到列表类 event 中。

- **[NIP-59](/zh/topics/nip-59/)（Gift Wrap）：临时 gift wrap kind**（[PR #2245](https://github.com/nostr-protocol/nips/pull/2245)）：新增 kind `21059`，作为现有 kind `1059` gift wrap 的临时版本。临时 event（kinds `20000`-`29999`）遵循 [NIP-01](/zh/topics/nip-01/) 语义：relay 不需要存储它们，并且可以在投递后将其丢弃。这样一来，应用就可以发送在投递后从 relay 上消失的 gift-wrapped 消息，从而降低高吞吐消息场景下的存储需求，同时保留与普通 [NIP-17](/zh/topics/nip-17/) DMs 相同的三层加密模型。

### OpenSats 宣布第十六轮 Nostr grants

[OpenSats](https://opensats.org) 于 4 月 8 日宣布了其[第十六轮 Nostr grants](https://opensats.org/blog/sixteenth-wave-of-nostr-grants)，资助了四个首次获得资助的项目和一个续期项目。[Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp) 获得资助，由贡献者 Robert Nagy 基于 [Quartz](/zh/topics/quartz/) 和 Commons 模块构建独立桌面应用，将 Android 客户端的功能集带到以鼠标为主的界面和持久 relay 连接环境中。[Nostr Mail](https://github.com/nogringo/nostr-mail) 获得资助，以 kind `1301` event 加上 [NIP-59](/zh/topics/nip-59/) gift wraps 在 Nostr 上构建完整邮件系统，并提供 Flutter 客户端以及用于兼容 Gmail/Outlook 的 SMTP bridge 服务器。[Nostrord](https://github.com/Nostrord/nostrord) 获得资助，用于构建基于 Kotlin Multiplatform 的 [NIP-29](/en/topics/nip-29/) relay 群组客户端，提供类似 Discord 的群消息、审核和线程。[Nurunuru](https://github.com/tami1A84/null--nostr) 获得资助，用于构建面向日语用户、界面风格参考 LINE 的原生 iOS Nostr 客户端，并为引导流程加入基于 passkey 的生物识别登录。HAMSTR 则获得了续期资助，最早一次资助来自[第十一轮](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)。

## NIP 深度解析：NIP-17（Private Direct Messages）

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) 定义了 Nostr 上当前的私密私信标准。它取代了更早的 [NIP-04](/zh/topics/nip-04/)（Encrypted Direct Messages）方案，后者会泄露元数据，发送方、接收方和时间戳都对 relay 可见，而且使用的是更弱的加密构造。NIP-17 将 [NIP-44](/zh/topics/nip-44/)（Encrypted Payloads）用于内容加密，并结合 [NIP-59](/zh/topics/nip-59/)（Gift Wrap）进行元数据保护，形成一个 relay 无法看出是谁在和谁通信的三层系统。

这个协议使用三层嵌套的 event kinds。最内层是真正的消息，一个未签名的 kind `14` event：

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

这个 kind `14` event 被刻意设计成未签名，也就是 `sig` 为空。规范将其描述为提供可否认性，但在实践中这种保护非常有限。包裹 rumor 的 kind `13` seal 是由发送者的真实密钥签名的。接收者可以把这个已签名 seal 展示给第三方，从而证明发送者曾与其通信，即便不暴露消息内容。借助零知识证明，接收者甚至可以证明精确的消息内容，而无需暴露自己的私钥。这个未签名 rumor 更像是一封放在已签名信封里的未签名信件，信封上的签名仍将发送者与内容联系起来。真正的可否认性需要对称认证，例如 Signal 使用的 HMAC，但这与 Nostr 的去中心化 relay 模型不兼容，因为消息必须能够自我认证。NIP-17 真正的优势在于元数据隐私和内容保密，而不是可否认性。

这条未签名消息随后会被包裹进一个 kind `13` seal 中。这个 seal 由实际发送者签名，并通过 [NIP-44](/zh/topics/nip-44/) 加密后发送给接收者：

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

这个 seal 没有 tags，因此即便被解密，也不会暴露接收者。seal 由发送者的真实密钥签名，因此接收者可以通过检查 seal 的 `pubkey` 是否与内部 kind `14` 的 `pubkey` 一致，来确认消息身份。

接着，这个 seal 会再被包裹进一个 kind `1059` gift wrap 中，由一个随机的一次性密钥签名，并指向接收者：

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

gift wrap 的 `pubkey` 是专门为这条消息随机生成的密钥，而 `created_at` 则会被随机回拨，最多回拨到过去两天。这是 relay 真正能看到的最外层：一条来自未知 pubkey、发给接收者的消息，时间戳并不反映消息真实发送时间。随机时间戳可以防止事后对已存储 event 进行分析，但如果攻击者主动连接着 relay，仍然可以观察到 gift wrap 首次出现的时间，因此这种防护只对之后才查询 relay 数据的被动观察者有效。由于 pubkey 是随机的，时间戳也是伪造的，relay 无法确定真实发送者。接收者要读取消息时，会用自己的 key 和这个随机 pubkey 解密 gift wrap，找到里面的 seal，再用自己的 key 和 seal 中发送者的 pubkey 解密 seal，最终拿到内部的 kind `14` 消息。

NIP-17 不提供前向保密。所有消息都使用静态 Nostr keypair 进行加密，也就是使用 NIP-44 基于发送者和接收者密钥派生的方式。如果私钥被攻破，过去和未来所有发往该密钥的消息都可以被解密。这是一个有意的权衡：因为加密只依赖 nsec，所以只要用户备份了自己的 nsec，就可以从任何仍存有 gift wraps 的 relay 中恢复全部消息历史。像 MLS 这样的协议，也就是 [Marmot](/zh/topics/marmot/) 所使用的方案，则通过轮换密钥材料提供前向保密，但代价是要求状态同步，并且在密钥轮换后无法恢复历史消息。

NIP-17 还定义了 kind `15` 用于加密文件消息，它增加了 `file-type`、`encryption-algorithm`、`decryption-key` 和 `decryption-nonce` tags，使接收者能够解密一个在上传到 Blossom 服务器前通过 AES-GCM 加密的附件。kind `10050` 用于发布用户偏好的 DM relay 列表，以便发送者知道应把 gift wraps 送到哪里。消息中的 `pubkey` 加上 `p` tags 的集合定义了一个聊天室，增加或移除参与者就会生成一个带有全新历史边界的新房间。

实现方面已经覆盖了大多数主流客户端。[nospeak](https://github.com/psic4t/nospeak) 将 NIP-17 用于全部一对一消息。[Flotilla](https://gitea.coracle.social/coracle/flotilla) 将 NIP-17 用于其工作量证明 DMs。[Amethyst](https://github.com/vitorpamplona/amethyst)、[Primal](https://github.com/PrimalHQ/primal-android-app)、[Nostur](https://github.com/nostur-com/nostur-ios-public)、[Damus](https://github.com/damus-io/damus)、[noStrudel](https://github.com/hzrd149/nostrudel) 和 [Coracle](https://github.com/coracle-social/coracle) 都将 NIP-17 作为其主要 DM 协议。该规范还支持通过在 gift wrap 中设置 `expiration` tag 来实现消息阅后消失。

## NIP 深度解析：NIP-46（Nostr Remote Signing）

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) 定义了一种将用户私钥与客户端应用分离开的协议。用户不再需要把 nsec 粘贴进 Web 应用，而是运行一个 remote signer，也叫 “bunker”，由它持有私钥，并通过 Nostr relay 响应签名请求。客户端永远看不到私钥。这缩小了攻击面：即便客户端被攻破，攻击者也只能请求签名，无法直接提取密钥本身。

该协议使用 kind `24133` 同时承载请求和响应，并通过 [NIP-44](/zh/topics/nip-44/)（Encrypted Payloads）加密。客户端会为会话生成一次性的 `client-keypair`，并通过带有彼此 pubkey tag 的 NIP-44 加密消息与 remote signer 通信。下面是一条客户端发给 remote signer 的签名请求：

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

其中加密后的 `content` 包含一个类似 JSON-RPC 的结构：

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

remote signer 会解密请求，将其展示给用户批准，或者依据已配置权限自动批准，然后使用用户私钥对 event 进行签名，并在响应中返回已签名 event：

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

连接可以由任意一方发起。remote signer 会提供一个包含其 pubkey 和 relay 信息的 `bunker://` URL。客户端则会提供一个 `nostrconnect://` URL，其中带有客户端 pubkey、relays，以及用于连接校验的 secret。`secret` 参数用于防止连接伪造：只有通过带外方式收到该 URL 的一方，才能完成握手。

协议定义了八种方法：`connect` 用于建立会话，`sign_event` 用于对 event 签名，`get_public_key` 用于获取用户 pubkey，`ping` 用于 keepalive，`nip04_encrypt`/`nip04_decrypt` 用于旧加密方式，`nip44_encrypt`/`nip44_decrypt` 用于当前加密方式，`switch_relays` 用于 relay 管理。relay 迁移由 remote signer 负责处理，因此它可以随着时间将连接迁移到新的 relay 上，而不会打断会话。

客户端在连接时可以通过权限系统请求特定能力。像 `nip44_encrypt,sign_event:1,sign_event:14` 这样的权限字符串，表示请求 NIP-44 加密能力，以及仅对 kind `1` 和 kind `14` event 的签名能力。remote signer 可以接受、拒绝或修改这些权限。这意味着一个用于阅读和发帖的 Web 客户端可能只需要 `sign_event:1` 权限，而一个 DM 客户端则可能还需要 `sign_event:14` 和 `nip44_encrypt` 权限。

[Amber](https://github.com/greenart7c3/Amber) 在 Android 上实现了 NIP-46，而其本周发布的 [v6.0.0-pre1](#amber-v600-pre1-增加按连接隔离的-nip-46-签名密钥) 又进一步加入了按连接隔离的签名密钥，以实现客户端间隔离。[nsec.app](https://github.com/nicktee/nsecapp)（此前名为 Nostr Connect）则提供了一个基于 Web 的 bunker。[nostr-tools](https://github.com/nbd-wtf/nostr-tools) 为 JavaScript 客户端提供了 `BunkerSigner`，而[上周的 PR #530](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing)增加了 `skipSwitchRelays`，以便手动管理 relay。该协议也支持 auth challenge：当 remote signer 需要额外认证，例如密码、生物识别或硬件 token 时，它会返回一个 `auth_url`，由客户端在浏览器中打开，让用户完成认证。

---

本周内容就是这些。你在构建什么，或者有什么新闻想分享？欢迎在 Nostr 上私信我们，或访问 [nostrcompass.org](https://nostrcompass.org)。
