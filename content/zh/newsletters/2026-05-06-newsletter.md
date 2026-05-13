---
title: 'Nostr Compass #21'
date: 2026-05-06
publishDate: 2026-05-06
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-06-newsletter.md
translationDate: 2026-05-13
---

欢迎回到 Nostr Compass，您每周的 Nostr 指南。

**本周：** [Marmot Protocol](https://github.com/marmot-protocol) 发布了 [MDK 0.8.0](#mdk-080-新增-mip-05-通知原语和可寻址密钥包)，包含首批 MIP-05 通知原语、可寻址 [NIP-51（列表）](/zh/topics/nip-51/) 密钥包以及强化的安全审查。[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) 发布了 [v0.10.0](#lawallet-nwc-v0100-发布完整-monorepo-和用户端钱包)，这是自获得 OpenSats 资助以来最大的版本，带来了完整的管理控制台、用户端钱包、端到端活动日志以及新的 `LightningAddress 1→N` 和 `NWCConnection` 架构。[Amethyst](https://github.com/vitorpamplona/amethyst) 完成了一次 [Nests 稳定性冲刺](#amethyst-通过-keep-alive、jwt-弹性和生命周期订阅稳定-nests)，消除了 JWT 刷新时的音频中断，引入了生命周期感知密钥数据订阅、relay keep-alive 重连以及动画发言参与者指示器。[ngit](https://github.com/DanConwayDev/ngit-cli) 发布了 [v2.4.2](#ngit-v242-和-v243-修复-grasp-服务器检测和多远程状态事件) 和 [v2.4.3](#ngit-v242-和-v243-修复-grasp-服务器检测和多远程状态事件)，修复了 PR 提交的 GRASP 服务器检测和多远程状态事件过滤问题。[GRAIN](https://github.com/0ceanSlim/grain) 发布了 [v0.5.4](#grain-v054-完成生产加固和静默数据丢失修复)，包含生产加固和 Docker 快速启动中的静默数据丢失修复。[Mostro Core](https://github.com/MostroP2P/mostro-core) 发布了 [v0.10.1](#mostro-core-v0101-新增-pgp-签名发布构件)，作为上周 v0.10.0 P2P 聊天协议模块的后续，包含 PGP 签名发布构件。[Clave](https://github.com/clave-mobile) 发布了 [v0.2.0](#clave-v020-在-ios-上推出-nip-46-nostr-connect-签名的多账户功能)，在 iOS 上支持多账户。

## 头条故事

### MDK 0.8.0 新增 MIP-05 通知原语和可寻址密钥包

[MDK](https://github.com/marmot-protocol/mdk)，[Marmot](/zh/topics/marmot/) 协议的 Rust 核心库，于 5 月 4 日发布了 [v0.8.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.8.0)。此版本发布了首批 MIP-05 通知构建块，将 MIP-00 密钥包移至可寻址事件，使用户的密钥包可以原地替换，改善了混合版本组兼容性，扩展了移动绑定的 UniFFI 覆盖范围，并收紧了围绕管理操作、提交、存储、加密边界和重放处理的验证路径。MIP-05 原语包括在 [PR #235](https://github.com/marmot-protocol/mdk/pull/235) 中添加的叶子索引助手，这些助手为下游客户端提供足够的信息以在不泄露组结构的情况下投递每个收件人的推送通知。运营修复也已落地：[PR #273](https://github.com/marmot-protocol/mdk/pull/273) 恢复了 mdk-core 在 crates.io 上的发布，[PR #269](https://github.com/marmot-protocol/mdk/pull/269) 在 `test-utils` Cargo feature 后面暴露了 test_util 模块，使外部客户端测试套件可以共享 Marmot 的测试工具。对于客户端团队，最重要的实际变化是可寻址密钥包：用户的 MIP-00 公告现在是一种可原地替换的 kind，因此轮换到新的密钥包不再会在 relay 上留下陈旧的事件。

### LaWallet NWC v0.10.0 发布完整 monorepo 和用户端钱包

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc)，LaWallet 团队的 [NIP-47](/zh/topics/nip-47/) Nostr Wallet Connect 实现，于 4 月 30 日发布了 [v0.10.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v0.10.0)。这是自项目获得 OpenSats 资助以来最大的版本。它发布了完整的 monorepo、完整的管理控制台、用户端钱包、端到端活动日志、动态品牌以及新的 `LightningAddress 1→N` 和 `NWCConnection` 架构，解锁了按地址的 NWC 路由，其中一个 Lightning 地址可以在不同的 RBAC 角色下扇出到多个 NWC 连接。在 [PR #191](https://github.com/lawalletio/lawallet-nwc/pull/191) 中发布的面向用户的钱包涵盖了入门、主页、收发款、扫描、货币、活动摘要和离线缓存。[PR #196](https://github.com/lawalletio/lawallet-nwc/pull/196) 添加了通过 Scalar 渲染的实时 OpenAPI 3.1 参考，包含基于角色的访问控制文档。

### Amethyst 通过 keep-alive、JWT 弹性和生命周期订阅稳定 Nests

[Amethyst](https://github.com/vitorpamplona/amethyst)，功能丰富的 Android 客户端，继续了在通讯 [#20](/zh/newsletters/2026-04-29-newsletter/#amethyst-通过-moq-互操作测试推进-nests-音频室) 中涵盖的 [NIP-53](/zh/topics/nip-53/) Nests 音频室工作，进行了一次稳定性冲刺，专注于在生产环境中破坏通话的故障模式。[PR #2733](https://github.com/vitorpamplona/amethyst/pull/2733) 中的音频中断修复在 JWT 刷新期间将新凭据获取与活动流重叠，使监听者在令牌轮换时不会听到中断。[PR #2730](https://github.com/vitorpamplona/amethyst/pull/2730) 中的新 keep-alive 机制在不需要用户手动操作的情况下重新连接断开的 relay，[PR #2728](https://github.com/vitorpamplona/amethyst/pull/2728) 将旧版 `KeyDataSourceSubscription` 替换为 `LifecycleAwareKeyDataSourceSubscription`，将订阅生命周期绑定到 Android Activity 生命周期。[PR #2724](https://github.com/vitorpamplona/amethyst/pull/2724) 为监听者添加了一个动画外环指示器，在多发言者会话中突出显示正在发言的参与者。

### ngit v2.4.2 和 v2.4.3 修复 GRASP 服务器检测和多远程状态事件

[ngit](https://github.com/DanConwayDev/ngit-cli)，用于 [NIP-34](/zh/topics/nip-34/) 协作的命令行工具和 `git` 插件，于 4 月 28 日发布了 [v2.4.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.2)，于 5 月 1 日发布了 [v2.4.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.3)。v2.4.2 修复了一个 URL 规范化不匹配问题，其中 `repo_grasps` 保存了规范化的主机名，但比较时却使用了完整的克隆 URL。v2.4.3 修复了当仓库有多个共享相同标识符的 `nostr://` 远程时出现的状态事件歧义：relay 可能返回由其他远程的维护者编写的状态事件，`run_list` 中的状态事件候选者现在过滤为当前远程仓库公告的维护者。

### GRAIN v0.5.4 完成生产加固和静默数据丢失修复

[GRAIN](https://github.com/0ceanSlim/grain)，基于 Go 的 Nostr relay 和客户端库，于 4 月 30 日发布了 [v0.5.4](https://github.com/0ceanSlim/grain/releases/tag/v0.5.4)。该版本汇集了自 v0.5.3 以来积累的六个修复，包括 Docker 快速启动中的静默数据丢失错误（之前在容器重启时会丢弃事件）、可寻址事件读取中的存储层正确性错误以及两个连接跟踪错误。v0.5.3 最初针对的生产加固对：每 IP 速率限制和 IP 黑名单，现均已到位并可配置。

### Mostro Core v0.10.1 新增 PGP 签名发布构件

[Mostro Core](https://github.com/MostroP2P/mostro-core)，为 Mostro 守护进程和其他下游应用程序提供点对点功能的 Rust 库，于 4 月 28 日发布了 [v0.10.1](https://github.com/MostroP2P/mostro-core/releases/tag/v0.10.1)，作为[上周 v0.10.0 P2P 聊天协议模块](/zh/newsletters/2026-04-29-newsletter/#mostro-core-v0100-和-mostro-mobile-v125-采用-nip-59-双密钥礼物包装)的后续。新版本添加了 PGP 签名发布构件和 `verify-release` 流程，使下游打包者可以在分发库之前确认构件来源。

## 版本发布

### Clave v0.2.0 在 iOS 上推出 NIP-46 (Nostr Connect) 签名的多账户功能

[Clave](https://github.com/clave-mobile)，使用 APNs 进行推送投递的 iOS [NIP-46](/zh/topics/nip-46/) 远程签名应用（在 [#20](/zh/newsletters/2026-04-29-newsletter/#clave-通过-apns-将-nip-46-远程签名带到-ios) 中介绍），于 5 月 5 日发布了 [v0.2.0](https://github.com/clave-mobile/clave/releases)。这是迄今为止最大的更新，引入了多账户支持：Clave 现在可以在一台设备上持有最多四个账户，带有一键切换器和按账户隔离。[PR #22](https://github.com/clave-mobile/clave/pull/22) 在 APNs 负载中添加了 `signer_pubkey` 字段，使设备在显示提示之前知道远程签名请求属于哪个账户。

### Wisp 发布 v1.0.3 → v1.0.5 稳定性工作

[Wisp](https://github.com/barrydeen/wisp)，[在 #20 中从 beta 毕业](/zh/newsletters/2026-04-29-newsletter/#wisp-v100-从-beta-毕业)的 Android 客户端，于 5 月 4 日发布了 [v1.0.3](https://github.com/barrydeen/wisp/releases/tag/v1.0.3)、[v1.0.4](https://github.com/barrydeen/wisp/releases/tag/v1.0.4) 和 [v1.0.5](https://github.com/barrydeen/wisp/releases/tag/v1.0.5)，包含稳定性工作。[PR #506](https://github.com/barrydeen/wisp/pull/506) 为完整媒体加载时添加了 Thumbhash 模糊图像预览，[PR #514](https://github.com/barrydeen/wisp/pull/514) 减少了底部标签切换时的卡顿。

### Amber 6.1.0-pre1 发布布局和稳定性修复

[Amber](https://github.com/greenart7c3/Amber)，用于 [NIP-55（Android 签名应用）](/zh/topics/nip-55/) 和 [NIP-46](/zh/topics/nip-46/) 的 Android 签名应用，发布了 [v6.1.0-pre1](https://github.com/greenart7c3/Amber/releases)，对新应用连接流程进行了布局改进并修复了多个崩溃问题。[PR #416](https://github.com/greenart7c3/Amber/pull/416) 修复了 `ActivityStatsBar` 布局和文本溢出问题，[PR #411](https://github.com/greenart7c3/Amber/pull/411) 确保 `SignerActivity` 在处理请求后始终关闭。

### Routstr Core v0.4.3 改善支付、退款和使用报告

[Routstr Core](https://github.com/Routstr/routstr-core)，将 Nostr 用于服务发现并将 [Cashu（Nostr 上的 Chaumian 电子现金）](/zh/topics/cashu/) 微支付用于私人使用计费的去中心化推理层，于 5 月 1 日以预发布形式发布了 [v0.4.3](https://github.com/Routstr/routstr-core/releases)。该版本改善了支付和退款处理，优化了成本跟踪和使用报告。

### Nostria v3.1.37 到 v3.1.41 新增 Web 书签和自动主题

[Nostria](https://github.com/nostria-app/nostria)，多平台 Nostr 客户端，于 4 月 30 日和 5 月 4 日发布了 [v3.1.37 到 v3.1.41](https://github.com/nostria-app/nostria/releases)。这些版本添加了 [NIP-B0（Web 书签）](/zh/topics/nip-b0/) 支持、跟随设备设置的"自动"主题、应用内 PDF 查看以及改进的文章和笔记编辑器。

### NoorNote v0.8.9 修复桌面首次启动空白屏幕

[NoorNote](https://github.com/77elements/noornote)，跨平台 Nostr 客户端，于 4 月 28 日发布了 [v0.8.9](https://github.com/77elements/noornote/releases/tag/v0.8.9)，修复了桌面应用首次启动时欢迎和登录屏幕无法渲染的空白屏幕错误。

### Kubo v0.3.4 到 v0.4.1 发布带家长控制和信任网络订阅源管理的儿童安全 Nostr 视频平台

[Kubo](https://github.com/JeroenOnNostr/kubo)，Nostr 上的儿童安全视频平台，让家长通过信任网络过滤器管理孩子的内容世界，于 5 月 4 日和 5 日发布了 [v0.3.4](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v0.3.4)、[v0.3.5](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v0.3.5)、[v0.4.0](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v0.4.0) 和 [v0.4.1](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v0.4.1)。每个孩子获得一个独立的 Nostr 密钥对和一个以视频为主的订阅源，家长可以控制时间限制（每天 15 到 180 分钟）、允许的时间窗口、发布操作可见性，以及可选的滚动上限。信任分配分三个级别（查看、互动、扩展）。

## 未发布的变更

### Sprout 发布 Desktop v0.0.4 和 v0.0.5 以及 NIP-OA 代理认证和配对中继边车

[Sprout](https://github.com/block/sprout)，Block 的内置 relay 的 Nostr 客户端，于 5 月 5 日发布了 [Sprout Desktop v0.0.4](https://github.com/block/sprout/releases)，于 5 月 6 日发布了 [v0.0.5](https://github.com/block/sprout/releases)，同时合并了约 80 个 PR。[PR #471](https://github.com/block/sprout/pull/471) 中的旗舰变更将 NIP-OA 代理认证连接到 relay 的 NIP-43 成员资格流程，使自主代理可以在 relay 授予访问权限之前证明特定的人类公钥授权了其操作。[PR #467](https://github.com/block/sprout/pull/467) 中新增了用于 NIP-AB 设备配对的临时边车 relay `sprout-pair-relay`。

### nostream 新增 Marmot relay 支持和 NIP-25 反应

[nostream](https://github.com/Cameri/nostream)，Node.js relay 实现，合并了一周的协议新增内容。[PR #602](https://github.com/Cameri/nostream/pull/602) 中的 Marmot Protocol relay 支持涵盖 MIP 00 到 03，为 relay 提供了 Marmot 加密消息事件的一级存储和转发。[PR #589](https://github.com/Cameri/nostream/pull/589) 中的 [NIP-25](/zh/topics/nip-25/) 反应支持、[PR #586](https://github.com/Cameri/nostream/pull/586) 中的 `#g` 过滤器地理哈希前缀匹配也已落地。

### strfry 新增每连接可观测性并降低 nofiles 上限

[strfry](https://github.com/hoytech/strfry)，C++ Nostr relay，合并了 14 个针对可观测性和运营卫生的 PR。[PR #218](https://github.com/hoytech/strfry/pull/218) 新增了每连接待发出站可观测性和可配置的背压上限。[PR #224](https://github.com/hoytech/strfry/pull/224) 从每事件监视器扇出中移除了 `std::function` 堆分配，切换到直接 `map.find()` 查找，降低了繁忙 relay 上的分配器压力。[PR #235](https://github.com/hoytech/strfry/pull/235) 将 `nofiles` 上限从 1,000,000 降至 524,288 以适应内核默认范围。

### Damus 用 Purple 代理替换 Tenor GIF 并发布压缩 UX

[Damus](https://github.com/damus-io/damus)，iOS Nostr 客户端，合并了 [PR #3737](https://github.com/damus-io/damus/pull/3737)，将 Tenor GIF 集成替换为 [Damus Purple](https://damus.io/purple/) 代理，由 Damus 的托管订阅服务代表客户端中继 GIF 请求，使个人用户不再直接查询 Tenor 的服务器。[PR #3733](https://github.com/damus-io/damus/pull/3733) 改善了大型数据库压缩 UX。

### Primal Android 改善探索、提醒和 NIP-05 验证徽章

[Primal Android](https://github.com/PrimalHQ/primal-android-app) 合并了 [PR #1043](https://github.com/PrimalHQ/primal-android-app/pull/1043)，修复了 `_@domain` 标识符用户的 [NIP-05（域名验证）](/zh/topics/nip-05/) 验证徽章闪烁问题，[PR #1041](https://github.com/PrimalHQ/primal-android-app/pull/1041) 实现了带有最近用户和最近搜索的探索落地标签，[PR #1045](https://github.com/PrimalHQ/primal-android-app/pull/1045) 实现了提醒过滤器。

### Alby Hub 从应用连接新增 NWC 支付

[Alby Hub](https://github.com/getAlby/hub) 合并了 [PR #2267](https://github.com/getAlby/hub/pull/2267)，允许从应用连接进行支付，两者均通过 Alby Hub 的 [NIP-47（Nostr Wallet Connect）](/zh/topics/nip-47/) 接口发布。

### routstrd-auth：面向团队的 Dockerized Routstrd，带 NIP-98 认证和 npub RBAC

[routstrd-auth](https://github.com/Routstr/routstrd-auth)，由 Routstr 团队于 4 月 27 日创建，是专为多用户团队部署设计的 Routstrd Docker 化变体，个人运营者无需各自运行守护进程。客户端端点采用 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) HTTP 认证和所有权跟踪，因此经 Nostr 签名的 HTTP 请求可以验证调用者身份并确认客户端属于该 npub。

### Routstrd 集成 Hermes 用于守护进程客户端和远程模式

[Routstrd](https://github.com/routstr/routstrd)，协调 Routstr 推理客户端的本地守护进程，合并了 [PR #22](https://github.com/routstr/routstrd/pull/22)，添加了与 [Hermes Agent](https://github.com/NousResearch/hermes-agent)（Nous Research 的开源 AI 代理）的集成，使代理的配置文件自动填充 Routstrd 通过 Nostr 发现的模型提供商和 API 密钥。

### whitenoise-rs 发布按账户数据库隔离和提案升级

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)，White Noise 通讯器的 Rust 核心库，合并了 [PR #796](https://github.com/marmot-protocol/whitenoise-rs/pull/796)（"Phase 18e"），将消息投影表移至按账户数据库，[PR #791](https://github.com/marmot-protocol/whitenoise-rs/pull/791) 添加了提案升级，使群组可以在所有成员支持时用新的提案类型扩展其功能。

### whitenoise Flutter UI 新增离开群组、术语一致性和 Fastlane 发布脚手架

[whitenoise](https://github.com/marmot-protocol/whitenoise)，White Noise 通讯器的 Flutter 移动 UI，合并了 [PR #604](https://github.com/marmot-protocol/whitenoise/pull/604)，从聊天列表 UI 添加了离开群组操作，[PR #595](https://github.com/marmot-protocol/whitenoise/pull/595) 在所有语言环境中将联系人操作重命名为关注和取消关注，[PR #601](https://github.com/marmot-protocol/whitenoise/pull/601) 为移动构建管道添加了 Fastlane 发布脚手架。

### Angor 0.2.21 发布紧凑应用流程以及密钥提供商和网络切换加固

[Angor](https://github.com/block-core/angor)，带有 Nostr 发布的创始人档案和项目公告的比特币众筹平台，于 5 月 6 日发布了 [Angor 0.2.21](https://github.com/block-core/angor/releases)。[PR #804](https://github.com/block-core/angor/pull/804) 添加了安全密钥提供商，[PR #806](https://github.com/block-core/angor/pull/806) 确保网络切换正确清除所有缓存数据并重置 UI 状态，[PR #822](https://github.com/block-core/angor/pull/822) 在"查找项目"中添加了按 ID 搜索项目的功能。

## 新追踪和发现的项目

### BitMacro Signer：带客户端密钥加密的可自托管 NIP-46 bunker

[BitMacro Signer](https://github.com/bitmacro/bitmacro-signer) 是一个使用 [NIP-46](/zh/topics/nip-46/) bunker 模型管理私钥的可自托管 Nostr 签名工具。签名者在存储之前在客户端加密密钥，使服务器端永远不持有明文，并通过 relay 使用轻量级守护进程签名事件。

本周的 [NIP-34](/zh/topics/nip-34/) 仓库发现浮现了 26 个新的仓库公告，其中四个值得关注。

### gnostr：直接构建在 Nostr 上的 git 实现

[gnostr](https://github.com/gnostr-org/gnostr) 是直接构建在 Nostr 上的 git 实现，与 `git-remote-nostr` 不同，它将自己的工作树命令作为从头开始的 Nostr 原生版本控制客户端提供。

### nostr-archive：Nostr 和 Blossom 上的内容寻址归档规范

[nostr-archive](https://gitworkshop.dev/nostr-archive/nostr-archive) 是 Nostr 和 Blossom 上的内容寻址归档的草案规范和参考实现，作为 NIP-34 仓库托管，使规范讨论与参考代码在同一地方进行。

### flower-cache：本地 Blossom 缓存服务器

[flower-cache](https://gitworkshop.dev/flower-cache/flower-cache) 是一个本地 Blossom 缓存服务器，对于想要远程 Blossom 服务器 blob 集的热本地镜像而无需每次 blob 获取都往返上游的客户端很有用。

### micro-vpn-ansible：通过 NIP-34 部署 VPN 的 Ansible playbook

[micro-vpn-ansible](https://gitworkshop.dev/npub1mu9fsh42uh48trncevdpju8cyv3mxmj9qj3rdjqc46zc324c6hys9ctsnc/relay.ngit.dev/micro-vpn-ansible) 是一个用于部署微型 VPN 的小型 Ansible playbook 集合，作为 NIP-34 仓库托管在 `relay.ngit.dev` 上并在 `gitnostr.com` 上镜像。

## 协议工作

### NIP 更新

- **Nostr 上的无经纪人算力市场**（[草案提案](https://njump.me/nevent1qqsqd2478wqugjh9ur9lenw9la0wd987h6jcc0tma4kkuat4xceymvszypxxmj0zcqtwqm34f48gzulrg99daaczllhtqun7xsldkh8neua2jhr32rf)）：匿名 NIP 草案，来自 Nostr 长文帖子，认为当前算力市场参与者（Braiins、Nicehash、Mining Rig Rentals）都是对用户进行 KYC 且可被审查的托管经纪商。该提案勾勒出一个点对点算力市场，其中 Stratum 端点、算力列表和合约托管通过 Nostr 事件运作，路径中没有经纪商控制的 Web 应用。
- **精选订阅源：DVM 订阅源的更简单替代方案**（[草案提案](https://njump.me/nevent1qqsqj55kvu28uyq2jr6nfwx20mv7c0vkm0vxkgx0zzrnanfp4wwv8nczyzm7669svt0xkjsju50a22zurc0qa589z2xd4yatzx6p2z64a5e0cyxz3e3)）：草案认为 [NIP-90](/zh/topics/nip-90/) 数据自动售货机被设计为通用计算市场，当客户端只需要一个可寻址的事件 ID 列表时，请求/响应模型过于繁重。该提案建议将精选订阅源发布为一个薄的可寻址事件，内容只是一个有序的事件引用列表，无需 DVM 往返。
- **个人资料颜色：确定性视觉身份**（[草案提案](https://njump.me/nevent1qqsy3tj7mn3r7wczmc52aknf5ym43lj3rrhd3sfprzvc6qydsq62wrgzyzjk8j56zmt5fwv088l5y84hqq4gags3grvuznlu4zmyt54w34cccyxenp3)）：从 Nostr 公钥派生确定性、可读颜色的新草案 NIP，使用户头像、提及芯片和其他 UI 界面在各客户端看起来相同。
- **Namecoin-Track NIPs：锚定身份、relay、TLS 和声誉**（[草案集群](https://njump.me/nevent1qqsydpjnaj2netmv0h5mlm2j6zpk8u50yvc9pqth3ly8pzuwy22720szypp3shk7edn43y5zfvdr0ftl8eq8l00zaknjqx3c9xuv7ja8ck60q7uupzs)）：将现有 Nostr 栈的各部分移入 Namecoin 锚定记录的可分离草案 NIP 集群。集群中的每个 NIP 针对单一关注点：身份、relay 元数据、TLS 证书固定和声誉断言。

## NIP 深度解析：NIP-34（git 相关）

[NIP-34](/zh/topics/nip-34/) 定义了在 Nostr relay 上托管 git 仓库、补丁、拉取请求、议题和合并状态的事件 kind。它是将 Nostr 变为代码协作协调层的标准：仓库数据仍然存储在 git 服务器上（GitHub、自托管的 forge 或 GRASP 服务器），而公告事件、补丁、PR、议题和状态更新则在 relay 上传播。

仓库作为 kind `30617` 可寻址事件公告，其 `d` 标签是一个 kebab-case 标识符（通常是项目名称），正文包括 `name`、`description`、一个或多个 `clone` URL、可选的 `web` URL、列出维护者监控的 relay 的 `relays` 标签，以及带有允许管理项目的额外公钥的 `maintainers` 标签。带有 `euc`（"最早唯一提交"）标记的 `r` 标签携带此仓库唯一的第一个提交的提交 ID，让客户端可以将同一项目跨不同主机的镜像和分支归为一组。

典型的 ngit 仓库公告如下所示：

```json
{
  "id": "08bb929a05fd9bbb5e1b227a3850269f2f9615e9e830bd34e664b72df14dead6",
  "pubkey": "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd",
  "created_at": 1758124128,
  "kind": 30617,
  "tags": [
    ["d", "ngit"],
    ["r", "26689f97810fc656c7134c76e2a37d33b2e40ce7", "euc"],
    ["name", "ngit"],
    ["description", "cli and git plugin for code collaboration over nostr"],
    ["clone", "https://codeberg.org/DanConwayDev/ngit-cli.git", "https://relay.ngit.dev/npub15qydau2hjma6ngxkl2cyar74wzyjshvl65za5k5rl69264ar2exs5cyejr/ngit.git"],
    ["web", "https://gitworkshop.dev/danconwaydev.com/ngit"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol", "wss://relay.nostr.band"],
    ["maintainers", "a008def15796fba9a0d6fab04e8fd57089285d9fd505da5a83fe8aad57a3564d", "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd"],
    ["alt", "git repository: ngit"]
  ],
  "content": "",
  "sig": "ad571d2ec44fcdb5d684281deb8aea3862b6660d73e66f1c921f381f2fec6869f4b9444414b4ffdafccd414f3489502af193401b35edcebd8f50dcebbbc0b37a"
}
```

补丁使用 kind `1617`，在内容正文中携带 `git format-patch` 输出，通过格式为 `30617:<维护者公钥>:<d 标签>` 的 `a` 标签引用目标仓库。拉取请求使用 kind `1618`，议题使用带有 markdown 内容的 kind `1621`。状态事件将线程在 Open（`1630`）、Applied/Merged 或 Resolved（`1631`）、Closed（`1632`）和 Draft（`1633`）之间移动。

本周的 NIP-34 故事与上周的 [GitWorkshop v2 发布](/zh/newsletters/2026-04-29-newsletter/#gitworkshop-发布浏览器内-pr-合并仓库关注和带宽高效的-git-浏览器)相同：浏览器内 PR 合并按钮之所以有效，是因为 GRASP 服务器、ngit 和 `nostr://` 克隆 URL 方案共同关闭了完全去中心化 forge 的循环。完整的实现名册、主要来源和事件 kind 参考在 [NIP-34 主题页](/zh/topics/nip-34/) 上。

## NIP 深度解析：NIP-53（直播活动）

[NIP-53](/zh/topics/nip-53/) 定义了 Nostr 上直播活动的标准事件界面：直播流、持久会议空间、预定会议活动、听众存在状态以及将聊天消息绑定到特定直播活动记录的直播聊天频道。五种事件 kind 协同工作，广告正在直播的内容、谁在参与以及音频或视频在哪里提供。

直播流作为 kind `30311` 可寻址事件公告。其 `d` 标签是稳定标识符，`streaming` 标签指向播放 URL，`status` 标签携带 `planned`、`live` 或 `ended` 之一。每个 `p` 标签携带公钥、relay 提示、可显示的角色标记（`Host`、`Speaker`、`Participant`）以及可选的第五项：活动完整 `a` 标签经参与者私钥签名的 SHA-256。没有该证明，客户端可以仅将参与者显示为"受邀"，这可以防止恶意事件所有者列出知名账户来吸引粉丝进入虚假活动。

代表性的 Nests 风格音频室公告如下所示：

```json
{
  "id": "8c1e6d7b3f2e9a4d5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1746540000,
  "kind": 30311,
  "tags": [
    ["d", "nests-room-2026-05-05-protocol-discussion"],
    ["title", "Protocol discussion: NIP-34 git workflows"],
    ["summary", "Open call for ngit, GitWorkshop, and joinmarket-ng maintainers"],
    ["streaming", "https://moq.amethyst.social/rooms/protocol-discussion-2026-05-05"],
    ["starts", "1746543600"],
    ["status", "live"],
    ["current_participants", "12"],
    ["service", "wss://nests.amethyst.social/"],
    ["p", "a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd", "wss://relay.damus.io", "Host", "f1e0d7a8b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6"],
    ["p", "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5", "wss://nos.lol", "Speaker"],
    ["p", "0057059046164d2238bbdbdf45fa2e106f59188289f6842d6bf362218ef4a58c", "", "Participant"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol"],
    ["t", "nostr"],
    ["t", "nip-34"]
  ],
  "content": "",
  "sig": "5a3e8b7c1d2f4a6b9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3"
}
```

NIP-53 将持久房间与在其中举行的预定活动分开。kind `30312` 会议空间定义了一个带 `d` 标识符的房间，kind `30313` 会议活动表示该房间内的预定或正在进行的会议。听众存在状态是单独的 kind `10312` 常规可替换事件。直播聊天使用 kind `1311`，每条聊天消息必须包含一个指向活动记录的 `a` 标签。

Nostr 直播活动界面故意保持精简：NIP-53 广告活动，而其他 NIP 处理相邻关注点。对直播流的 zap 使用 [NIP-57（Zaps）](/zh/topics/nip-57/) zap 收据（kind `9735`），视频录制可以作为 [NIP-71（视频事件）](/zh/topics/nip-71/) 视频事件重新发布。完整的实现名册、参与者证明门控建议以及房间/活动分离原理在 [NIP-53 主题页](/zh/topics/nip-53/) 上。

---

本周就到这里。如果您正在构建什么或有新闻分享，请在 Nostr 上给我们发 DM 或在 [nostrcompass.org](https://nostrcompass.org) 找到我们。
