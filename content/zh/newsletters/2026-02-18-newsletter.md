---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** Blossom 本地缓存层初具雏形，多个独立项目在 Android 离线媒体访问上不约而同地汇聚。Alby 为构建和测试 Nostr Wallet Connect 集成推出 [NWC 开发者沙箱](https://sandbox.albylabs.com)，无需真实资金。两位作者在同一周提出了 AI 代理在 Nostr 上通信的竞争方案。fiatjaf 从 [NIP-11](https://github.com/nostr-protocol/nips/pull/1946) 中移除了未使用字段，删除了 relay 运营者从未采用的保留策略、国家代码、隐私政策和社区偏好 tag。[NIP-85](https://github.com/nostr-protocol/nips/pull/2223) 合并了 Trusted Assertions 的服务提供商可发现性指南。[NIP-52](https://github.com/nostr-protocol/nips/pull/1752) 新增 `D` tag，为日历 event 启用按天精度的时间戳索引。新项目包括 [Mapnolia](https://github.com/zeSchlausKwab/mapnolia)（去中心化地图瓦片分发）、[Pika](https://github.com/sledtools/pika)（基于 MLS 加密的消息应用）、[Keep](https://github.com/privkeyio/keep-android)（Android 端 FROST 门限签名）、[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree)（内容寻址存储与 Nostr 集成）和 [Prism](https://github.com/hardran3/Prism)（从任意 Android 应用分享内容到 Nostr）。[Primal Android](https://github.com/PrimalHQ/primal-android-app) 合并 11 个 NWC PR，添加双钱包支持和自动服务生命周期管理。[Mostro Mobile](https://github.com/MostroP2P/mobile) 通过 NWC 集成推出[内置 Lightning 钱包](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2)。[Notedeck](https://github.com/damus-io/notedeck) 为 Android 应用商店上架做准备，HAVEN 达到 [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3)，支持多 npub 和云备份。本周深入解析涵盖 NIP-85 的 Trusted Assertions 系统（将 Web of Trust 计算委托给服务提供商）以及 NIP-52 的日历 event 协议（跟随其按天精度索引更新）。

## 新闻

### Blossom 本地缓存层初具雏形

多个独立项目正在汇聚解决同一问题：移动设备上 [Blossom](/zh/topics/blossom/) 媒体的离线访问。

[Morganite](https://github.com/greenart7c3/Morganite)，greenart7c3（[Amber](https://github.com/greenart7c3/amber) 和 [Citrine](https://github.com/greenart7c3/Citrine) 的开发者）推出的新 Android 应用，实现了 Blossom 媒体的客户端缓存。用户无需网络连接即可访问之前浏览过的图片和文件。

[Aerith](https://github.com/hardran3/Aerith) 发布了 [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2)，新增图片标签、批量镜像/标记/删除操作、按标签和文件类型过滤，以及初步的 Blossom 本地缓存支持。Aerith 是一款管理界面，供在多个 Blossom 服务器上存储媒体的用户组织和镜像其 blob。

Blossom 规范中新增了一份[本地缓存实现指南](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)，记录了客户端 blob 存储规范，而 [Prism](https://github.com/hardran3/Prism)（与 Aerith 同一开发者）则在其 Android 分享至 Nostr 流程中添加了 Blossom 上传集成。本周四个独立项目汇聚于同一问题：专用缓存应用、媒体管理器、参考规范，以及集成 Blossom 的分享工具，它们都在简单上传和检索之外实现了持久化本地存储。

### Alby NWC 开发者沙箱

[Alby](https://sandbox.albylabs.com) 为使用 [Nostr Wallet Connect (NIP-47)](/zh/topics/nip-47/) 的开发者推出了沙箱环境。该沙箱提供托管的 NWC 钱包服务，开发者可创建测试连接并发送模拟支付，无需连接真实 Lightning 钱包，同时实时观察 NWC event 的完整请求/响应周期。开发者从沙箱生成 `nostr+walletconnect://` 连接字符串并传递给客户端，沙箱随即展示客户端与钱包服务之间流转的 kind 23194 请求和 kind 23195 响应 event。

这降低了新 NWC 集成的门槛。此前，测试需要个人 Lightning 钱包或自托管的 NWC 服务。沙箱将这些屏蔽掉，让开发者可以即时获得 `pay_invoice`、`get_balance`、`make_invoice`、`lookup_invoice` 和 `list_transactions` 方法对接真实 NWC 端点的反馈循环。

### AI 代理 NIP 相继登场

Nostr 上 AI 代理通信的提案在数天内接连出现，以不同角度切入这一问题。

来自 joelklabo 的 [NIP-XX：AI 代理消息](https://github.com/nostr-protocol/nips/pull/2226) 定义了 AI 代理交互的完整协议：包括提示词、响应、流式增量、状态更新、工具遥测、错误、取消和能力发现的 event kind。`ai.info` 发现 event（kind 31340，可替换）让代理公告其支持的模型、带 schema 的工具、流式支持和速率限制。joelklabo 的提案包含通过提示词 ID 关联运行、会话管理、带序列排序的流重组，以及用于元数据隐私的 [NIP-59](/zh/topics/nip-59/) 指南。

来自 pablof7z 的 [NIP-AE：Agents](https://github.com/nostr-protocol/nips/pull/2220) 采用了不同方法，定义了代理实例化的 kind：定义和经验教训。这些是 pablof7z 在 [TENEX](https://github.com/tenex-chat/tenex)（基于 Nostr 构建的自主学习系统）中使用的 event 类型。同样来自 pablof7z 的配套提案 [NIP-AD：MCP 服务器与技能公告](https://github.com/nostr-protocol/nips/pull/2221) 定义了在 Nostr 上公告 [Model Context Protocol](https://modelcontextprotocol.io/) 服务器和技能的 event。支持 [NIP-22](/zh/topics/nip-22/) 评论，社区可直接在 Nostr 上讨论和评分 MCP 服务器。

NIP-XX 涵盖完整的代理通信，NIP-AE 和 NIP-AD 则处理身份和工具发现。这些提案可能会融合成统一标准，也可能作为互补层共存。

## 版本发布

### HAVEN v1.2.0-rc3

[HAVEN](https://github.com/bitvora/haven)，将四种 relay 功能与 [Blossom](/zh/topics/blossom/) 媒体服务器捆绑的一体化个人 relay，达到 [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3)。此候选版本新增对多 npub 的支持，让单个 HAVEN 实例可为多个 Nostr 身份提供服务。更早的 RC 版本添加了云备份的 `--from-cloud` 和 `--to-cloud` 标志（RC2），并修复了 Web of Trust 重复计数 bug（RC1）。

### Mostro Mobile v1.2.0：内置 Lightning 钱包

[Mostro Mobile](https://github.com/MostroP2P/mobile)，[Mostro](https://github.com/MostroP2P/mostro) P2P Bitcoin 交易所的移动客户端（[上周报道的 v1.1.0](/zh/newsletters/2026-02-11-newsletter/#mostro-发布首个公测版)），发布了 [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2)，通过完整的 [NWC (NIP-47)](/zh/topics/nip-47/) 集成内置 Lightning 钱包。买卖双方无需再切换应用处理发票。应用为卖家自动检测持有发票并通过已连接钱包支付，买家则获得自动发票生成。此版本紧随本周早些时候的 [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1)，该版本新增了带可信实例精选注册表的多 Mostro 节点支持、用于节点显示的 kind 0 元数据获取、通过 pubkey 自定义节点管理，以及所选节点下线时的自动回退。

服务器端，[Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2) 发布，修复了重复开发费用支付、密码验证 RPC 端点的速率限制，以及协作取消时的正确争议清理。

新配套项目 [mostro-skill](https://github.com/MostroP2P/mostro-skill) 让代理能通过 Nostr 在 Mostro 上进行交易。

### Aerith v0.2

[Aerith](https://github.com/hardran3/Aerith)，[Blossom](/zh/topics/blossom/) 图片管理器，发布了 [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2)，新增用于组织媒体的图片标签、跨服务器批量镜像/标记/删除操作、按标签和文件类型过滤，以及初步的本地缓存支持。更多背景请参见[新闻部分](#blossom-本地缓存层初具雏形)。

### Mapnolia：基于 Nostr 的去中心化地图瓦片

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia) 是一款新的地理空间数据服务器，将 [PMTiles](https://github.com/protomaps/PMTiles) 地图存档按地理区域分块，并通过 Nostr 公告以实现去中心化发现。它向 Nostr relay 发布 kind 34444 参数化可替换 event，包含带图层元数据、geohash 区域、文件引用和 [Blossom](/zh/topics/blossom/) 服务器详情的完整地图瓦片块索引。

客户端通过 Nostr 网络发现和检索地图数据，而非通过中心化瓦片服务器。公告 event 携带足够的元数据，让客户端仅从列出的 Blossom 服务器请求所需的地理区域。Mapnolia 是首个将地理空间数据分发带入 Nostr 的项目，为支持离线的地图应用开辟了可能。

### Pika：基于 Marmot 的加密消息应用

[Pika](https://github.com/sledtools/pika) 是一款新的端对端加密消息应用，适用于 iOS 和 Android，使用 [Marmot](/zh/topics/marmot/) 协议，该协议在 Nostr relay 之上叠加[消息层安全（MLS）](/zh/topics/mls/)。架构将关注点分离为处理 MLS 状态管理和通过 Nostr relay 进行消息加解密的 Rust 核心（`pika_core`），以及 SwiftUI（iOS）和 Kotlin（Android）的轻量原生 UI 壳。状态单向流动：UI 向 Rust actor 分发动作，actor 改变状态并通过 UniFFI 和 JNI 绑定向 UI 发送带版本号的快照。

Pika 加入了基于 MLS 的 Nostr 消息应用不断壮大的行列，与 [White Noise](https://github.com/marmot-protocol/whitenoise)、[Vector](https://github.com/VectorPrivacy) 和 [0xchat](https://0xchat.com) 并列。所有应用都使用 Nostr relay 作为 MLS 加密密文的传输层，使 relay 运营者无法读取消息内容。Pika 使用 Marmot Development Kit（MDK）实现 MLS，使用 nostr-sdk 连接 relay。

### Keep：Android 端 [FROST](/zh/topics/frost/) 门限签名

[Keep](https://github.com/privkeyio/keep-android) 是一款新的 Android 应用，用于 [FROST](/zh/topics/frost/) 门限签名，不需要任何单一设备持有完整私钥。它实现了 [NIP-55](/zh/topics/nip-55/)（Android 签名器）和 [NIP-46](/zh/topics/nip-46/)（远程签名），兼容的 Nostr 客户端可以在密钥材料分布于多台设备的情况下请求签名。默认配置为 2-of-3 和 3-of-5，但支持任意 t-of-n 门限。

Keep 的分布式密钥生成（DKG）仪式通过 Nostr relay 使用自定义 event kind 运行：kind 21101 用于组公告，kind 21102 用于第一轮承诺多项式（公开广播），kind 21103 用于第二轮密钥份额（参与者之间点对点的 [NIP-44](/zh/topics/nip-44/) 加密）。DKG 过程中，组私钥标量从未在任何地方被计算或组装。每台设备仅持有其多项式评估份额，任意 t 个份额即可通过两轮提交-然后-签名协议生成有效的 Schnorr 签名。最终的 64 字节签名与单签名者 Schnorr 签名无法区分。底层，Keep 使用 Zcash 基金会的 `frost-secp256k1-tr` crate 并带 Taproot 调整，因此组公钥可直接用作 Nostr npub。

Keep 加入 [Frostr](https://frostr.org) 项目家族，与 [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop)、[Igloo for Android](https://github.com/FROSTR-ORG/igloo-android)、[Frost2x](https://github.com/FROSTR-ORG/frost2x) 和 [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios) 并列，扩展了 Nostr 上门限密钥管理的选择。

### Prism：从 Android 分享任意内容到 Nostr

[Prism](https://github.com/hardran3/Prism) 是一款新的 Android 应用（Kotlin/Jetpack Compose，API 26+），注册为系统分享目标，让用户可以从手机上任意应用向 Nostr 发布文本、URL、图片和视频。分享的 URL 在组合成笔记前会经过跟踪参数清除处理。Prism 获取 OpenGraph 元数据以生成丰富的链接预览，并内联渲染原生 Nostr 引用（`note1`、`nevent1`）。

调度引擎采用混合 `AlarmManager`/`WorkManager` 方案以绕过 Android 电池优化：AlarmManager 处理精确唤醒时机，而加急 WorkManager 任务确保投递，离线场景下使用指数退避重试。媒体上传通过可配置的 [Blossom](/zh/topics/blossom/) 服务器完成，支持图片和视频帧的缩略图生成。所有 event 签名委托给 [NIP-55](/zh/topics/nip-55/) 外部签名器，如 [Amber](https://github.com/greenart7c3/amber)，并支持多账户身份切换。Prism 还支持 [NIP-84（高亮）](/zh/topics/nip-84/) 发帖。由 [Aerith](#aerith-v02) 的同一开发者创作。

### Hashtree：内容寻址存储与 Nostr 集成

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) 是一个基于文件系统的内容寻址 blob 存储系统，在 Nostr 上发布 Merkle 根以创建可变的 npub/路径地址。该系统使用"哑存储"，与任何键值存储兼容，将内容分块为针对 [Blossom](/zh/topics/blossom/) 上传优化的 2MB 块。与 BitTorrent 不同，无需主动进行 Merkle 证明计算，只需按哈希存储和检索 blob 即可。

Nostr 集成支持类似 `htree://npub.../repo-name` 的 git 远程 URL 用于克隆仓库，使用 `htree publish mydata <hash>` 等命令将内容哈希发布到 `npub.../mydata` 地址。完整的 CLI 支持加密（默认）和公开存储模式、内容固定、推送到 Blossom 服务器以及管理 Nostr 身份。每个存储项目要么是原始字节，要么是树节点，为通过 Nostr relay 网络进行去中心化内容分发提供了基础。

### Espy：Shakespeare 上的调色板捕获

[Espy](https://espy.you) 基于 [Shakespeare](https://soapbox.pub/tools/shakespeare/) 平台构建，让用户从照片中捕获调色板并将其作为 Nostr event 分享。Shakespeare 是一个 AI 驱动的应用构建器，通过 NIP-07 浏览器扩展对用户进行身份验证，并提供内置的 Nostr relay 连接，让开发者无需自行实现密钥管理或 relay 池即可发布应用。Espy 将相机输入的主色提取为可通过标准 Nostr 信息流发现的可分享调色板卡片。

### Flotilla 1.6.4

[Flotilla](https://gitea.coracle.social/coracle/flotilla)，hodlbod 的 Discord 风格 Nostr 客户端（以 relay 为群组进行组织），发布了 [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4)。Coracle 系列项目已从 GitHub 迁移到自托管的 [Gitea 实例](https://gitea.coracle.social/coracle)。此版本通过 NIP-9a 添加了推送通知和钱包接收流程，以及分类列表和空间 URL 支持。界面改进包括清理后的模态框和通知处理。房间静音和移动端安全区域内边距是本次变更的完结，同时修复了 Safari 图片上传和日历 event 详情问题。

### Shosho v0.12.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases)，集成 Nostr 的移动直播应用，发布了 [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0)。此版本新增带播放器内回复和自定义表情集成的视频片段功能。线程保护阻止间接提及垃圾信息，新的二维码分享功能让用户可以离线交换个人资料。新的水平播放模式为直播提供类 Twitch 观看体验，浏览屏幕现在在直播旁展示创作者片段。

### Granary v10.0

[Granary](https://github.com/snarfed/granary)，一个在 Nostr、Bluesky、ActivityPub 和其他平台之间将数据转换为通用格式的社交网络翻译库，发布了带有重大变更的 [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0)。此版本将 Nostr 的默认 ActivityStreams 1 ID 从 bech32 切换为十六进制，并扩展了 Nostr 支持，包括 [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) 提及解析和文章 tag。各转换器新增的多输出选项让开发者可以批量在协议之间转换。

### Nostr MCP Server v3.0.0

[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server)，一个让 AI 代理与 Nostr 网络交互的 [Model Context Protocol](https://modelcontextprotocol.io/) 服务器，发布了 [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0)。此主要版本新增了社交动作（关注、反应、转发、回复）和带 [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) 支持及可选 [NIP-42](/zh/topics/nip-42/) 认证的 relay 列表管理。通过 [NIP-17](/zh/topics/nip-17/) 和 [NIP-44](/zh/topics/nip-44/) 的直接消息功能也是新增内容。此版本与本周的 [AI 代理 NIP 提案](#ai-代理-nip-相继登场)相配合，为在 Nostr 上运行的代理提供实用工具。

### Aegis v0.3.8

[Aegis](https://github.com/ZharlieW/Aegis)，跨平台 Nostr 签名器，发布了 [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8)，支持多语言 UI 以及内置 Nostr 应用浏览器的增量更新管理器。新的更新机制与本地状态进行增量差异比较，以更低的带宽占用保持应用内 Nostr 网页应用目录的更新。此版本还引入了 5 分钟密钥材料缓存，以减少连续签名多个 event 时的数据库往返次数。

### SNSTR v0.3.1

[SNSTR](https://github.com/AustinKelsay/snstr)（Secure Nostr Software Toolkit for Renegades），Nostr 协议的 TypeScript 库，发布了 [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1)。此版本添加了包验证守卫，确保所有入口点包含在 npm tarball 中，并在 Node 和 Bun 上强制执行 CI。[v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0) 在同一周发布。

### Citrine v2.0.0-pre1

[Citrine](https://github.com/greenart7c3/Citrine)，greenart7c3 的 Android Nostr relay，发布了 [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1)，通过优化数据库索引和更好的 Kotlin 协程处理提升性能。此版本还增强了对托管网页应用的支持，每个应用现在运行在独立端口上。

## 项目更新

### Primal Android：NWC 基础设施扩展

[Primal Android](https://github.com/PrimalHQ/primal-android-app) 本周合并了 11 个 NWC 相关 PR，延续[两周前开始的](/zh/newsletters/2026-02-04-newsletter/#primal-android-发布-nwc-加密)建设工作。此批次添加了双钱包 NWC 支持、与后端通知绑定的服务自动启停、按钱包类型的连接路由，以及删除钱包时的正确数据清理。NWC 服务现在根据钱包连接状态自主管理生命周期，减少了用户手动干预。

### Notedeck：Android 应用商店准备工作

[Notedeck](https://github.com/damus-io/notedeck)，[Damus](https://github.com/damus-io/damus) 团队的多平台 Nostr 客户端，本周合并了 [Android 应用商店发布准备](https://github.com/damus-io/notedeck/pull/1287)。该 PR 添加了 Google Play 要求的 UGC（用户生成内容）合规计划，包括服务条款接受界面、通过上下文菜单和设置进行用户屏蔽、向 relay 发布举报 event 的 [NIP-56（举报）](/zh/topics/nip-56/) 功能，以及内容与安全设置部分。为通过新 Makefile 目标生成签名发布 APK 和 AAB（Android App Bundle）添加了构建基础设施。EULA 文档确立了 17 岁以上年龄要求和 Nostr 特有的去中心化内容免责声明。合规功能本身将在后续 PR 中推出；此次合并奠定了文档和签名的基础。

在 Damus iOS 端，修复了[无限加载旋转器回归问题](https://github.com/damus-io/damus/pull/3593)，该问题会导致内容加载完成后旋转器持续无限显示。

### Nostria：发现 Relay 和私信修复

[Nostria](https://github.com/nostria-app/nostria)，专注于全球规模的跨平台 Nostr 客户端，本周合并了 9 个 PR。最值得关注的是为个人资料查找[自动初始化发现 Relay](https://github.com/nostria-app/nostria/pull/460)，让新用户无需手动配置即可获得可用的 relay 连接。其他修复包括 [DM 文本框自动换行](https://github.com/nostria-app/nostria/pull/466)、[全屏视频视口填充](https://github.com/nostria-app/nostria/pull/479)、[转发预览中的文章元数据提取](https://github.com/nostria-app/nostria/pull/481)和[通知中的 nostr: URI 解析](https://github.com/nostria-app/nostria/pull/458)。

### Camelus：Riverpod v3 迁移

[Camelus](https://github.com/camelus-hq/camelus)，基于 Flutter 的 Nostr 客户端，本周合并了 5 个 PR，核心是 [Riverpod v3 API 迁移](https://github.com/camelus-hq/camelus/pull/158)和[通用信息流重构](https://github.com/camelus-hq/camelus/pull/159)。[嵌入式笔记缓存](https://github.com/camelus-hq/camelus/pull/161)避免了对引用笔记的冗余 relay 请求。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-85：服务提供商可发现性](https://github.com/nostr-protocol/nips/pull/2223)**：vitorpamplona 为 [NIP-85 Trusted Assertions](/zh/topics/nip-85/) 服务提供商的客户端发现添加了指南，包括 relay 提示和算法特定的服务密钥。详见[下方深入解析](#nip-深入解析nip-85trusted-assertions)。

- **[NIP-11：Relay 信息清理](https://github.com/nostr-protocol/nips/pull/1946)**：fiatjaf 从 [NIP-11](/zh/topics/nip-11/) 中移除了 `privacy_policy`、`retention` 数组、`relay_countries` 和社区偏好块。relay 运营者很少填写这些字段，客户端也不会对其做出响应。

- **[NIP-52：按天精度时间戳 Tag](https://github.com/nostr-protocol/nips/pull/1752)**：staab 在 [NIP-52](/zh/topics/nip-52/) 基于时间的日历 event（kind 31923）中添加了必需的 `D` tag，表示按天精度的 Unix 时间戳，计算方式为 `floor(unix_seconds / 86400)`。多个 `D` tag 覆盖多日 event，无需解析完整时间戳即可实现高效的时间索引。

- **[NIP-47：简化](https://github.com/nostr-protocol/nips/pull/2210)**：[第 9 期 Newsletter](/zh/newsletters/2026-02-11-newsletter/) 中讨论的简化 PR 本周合并，从 [NIP-47（Nostr Wallet Connect）](/zh/topics/nip-47/)中移除了 `multi_pay_invoice` 和 `multi_pay_keysend`。完整的 NWC 协议深入解析请参见 [Newsletter #8](/zh/newsletters/2026-02-04-newsletter/#nip-深入解析nip-47nostr-wallet-connect)。

**开放 PR 和讨论：**

- **[NIP-74：播客](https://github.com/nostr-protocol/nips/pull/2211)**：[Newsletter #8](/zh/newsletters/2026-02-04-newsletter/) 已报道，这一播客规范提案本周引发了激烈讨论。staab 指出至少已有三个竞争性播客标准在野运行，derekross 则指出了一个已有六个月历史且有活跃应用和播客的现有实现。推进需要各实现在分配 NIP 编号前先达成共识。

- **[NIP-XX：AI 代理消息](https://github.com/nostr-protocol/nips/pull/2226)**：joelklabo 提议了一个完整的 AI 代理通信协议，包含用于提示词、响应、流式传输、工具遥测、错误和能力发现的 event kind。参见[新闻部分](#ai-代理-nip-相继登场)了解本周所有 AI 提案的报道。

- **[NIP-PNS：私人笔记存储](https://github.com/nostr-protocol/nips/pull/1893)**：jb55 的私人笔记系统定义了 kind 1080 event，用于在 relay 上存储加密个人笔记，而不暴露写作者身份。该方案通过用户的 nsec 使用 HKDF 派生一个确定性的假名密钥对：`pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`，然后从派生密钥生成 secp256k1 密钥对。第二次派生生成对称加密密钥：`pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`。内层笔记使用此密钥以 [NIP-44](/zh/topics/nip-44/) v2 加密后在假名 pubkey 下发布，因此 relay 看到的是来自与用户主密钥无关的身份的 kind 1080 event。与 [NIP-59](/zh/topics/nip-59/) 礼品包装不同，PNS 不可被垃圾信息利用（假名密钥是确定性的，而非随机的），且不携带任何公开元数据（无需 `p` tag，因为没有接收者）。本周，jb55 发布了在 Notedeck Rust 后端（`enostr::pns` 模块）实现 PNS 的发现。他发现规范的 `hkdf_extract` 调用存在歧义，因为 RFC 5869 HKDF 有两个阶段（提取和扩展），产生不同输出，大多数库期待两者都有。他澄清了 `pns_nip44_key` 绕过 NIP-44 的正常 ECDH 密钥协商，直接用作会话密钥——这是实现者需要知道的细节，因为大多数 NIP-44 库默认使用 ECDH。他还标记了参考实现 TypeScript 中的未定义变量。该 PR 最初来自 2025 年 4 月，现在正被积极实现。

- **[NIP-AE：Agents](https://github.com/nostr-protocol/nips/pull/2220)**：pablof7z 为 Nostr 上的代理身份定义了四种 event kind，源自他在 [TENEX](https://github.com/tenex-chat/tenex) 上的工作。基础模板是 kind 4199（代理定义），携带标题、角色描述、系统指令、工具声明和版本。行为修饰符位于 kind 4201（代理微调），使用 `only-tool`、`allow-tool` 和 `deny-tool` tag 进行运行时能力控制。代理将其学习内容作为 kind 4129（代理经验教训）event 发布，经过分类后通过 `e` tag 链接回父定义，可通过 [NIP-22](/zh/topics/nip-22/) 评论线程进一步完善。所有权验证使用 kind 14199，一个人类运营者列出其代理 pubkey 的可替换 event，与代理 kind 0 个人资料 `p` tag 匹配时建立双向链。

- **[NIP-AD：MCP 服务器与技能公告](https://github.com/nostr-protocol/nips/pull/2221)**：pablof7z 定义了在 Nostr 上公告 [Model Context Protocol](https://modelcontextprotocol.io/) 服务器和独立技能的 event。MCP 服务器公告携带服务器端点 URL 和支持的协议版本，以及带输入 schema 的可用工具列表。服务器公告支持 [NIP-22](/zh/topics/nip-22/) 评论，社区可直接在 Nostr 上讨论和评分 MCP 服务器。

- **[NIP-73：OSM Tag Kind](https://github.com/nostr-protocol/nips/pull/2224)**：DestBro 提议在 [NIP-73（外部内容 ID）](/zh/topics/nip-73/)中添加 OpenStreetMap 标识符，该 NIP 通过 `i` 和 `k` tag 标准化 Nostr event 引用书籍（ISBN）、电影（ISAN）、播客订阅（GUID）、geohash 和 URL 等外部内容的方式。提议的 OSM kind 将让 event 通过 OpenStreetMap 节点或路段 ID 引用特定地图特征（建筑物、道路、公园），将 Nostr 内容与开放地理数据库连接起来。

- **[NIP-XX：响应式图片变体](https://github.com/nostr-protocol/nips/pull/2219)**：woikos 提议扩展 [NIP-94](/zh/topics/nip-94/) 文件元数据 event，添加不同分辨率响应式图片变体的 tag。客户端可根据显示尺寸和网络条件选择合适的变体，为浏览 [Blossom](/zh/topics/blossom/) 服务器上高分辨率图片的移动用户减少带宽消耗。

## NIP 深入解析：NIP-85（Trusted Assertions）

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) 定义了一个将耗时计算委托给可信服务提供商的系统，这些提供商以 Nostr event 的形式发布签名结果。Web of Trust 评分和互动指标需要爬取大量 relay 并处理海量 event，这在移动设备上是不切实际的。本周的[合并](https://github.com/nostr-protocol/nips/pull/2223)为客户端发现这些提供商的过程添加了指南。

**委托：**

计算用户的 Web of Trust 评分需要在大量 relay 上多跳爬取关注图谱，而计算准确的关注者数量意味着要对整个 relay 网络进行去重。移动设备和浏览器客户端无法执行这些操作，然而这些结果对于垃圾过滤和内容排名至关重要。NIP-85 通过让用户指定可信提供商来弥合这一差距，由提供商运行计算并以标准 Nostr event 形式发布结果。

**协议设计：**

NIP-85 使用四种 event kind 对不同主题类型进行断言。用户断言（kind 30382）携带关注者数量、帖子/回复/反应数量、zap 金额、标准化排名（0-100）、常见话题和活跃时段：

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Event 断言（kind 30383）对单条笔记评分，包含评论数、引用数、转发数、反应数和 zap 数据：

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

对于可寻址 event（长文章、wiki 页面），kind 30384 将相同的互动指标整体应用于所有版本。Kind 30385 对通过 [NIP-73（外部内容 ID）](/zh/topics/nip-73/)引用的外部标识符（书籍、电影、网站、地点、话题标签）进行评分，NIP-73 通过 `i` 和 `k` tag 标准化 Nostr event 引用外部内容的方式：

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

每个断言都是一个可替换的可寻址 event，其中 `d` tag 包含主题：pubkey、event ID、event 地址或 NIP-73 标识符。服务提供商用自己的密钥对这些 event 签名，客户端根据信任关系评估它们。

**提供商发现：**

用户通过发布 kind 10040 event 声明其信任的断言提供商。每个条目指定断言类型，包含提供商 pubkey 和 relay 提示，以及可选的算法变体：

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

用户可以使用 [NIP-44](/zh/topics/nip-44/) 对 `.content` 中的 tag 列表进行加密，以保持提供商偏好的私密性。客户端通过检查关注账号所信任的提供商来构建提供商列表，为断言提供商本身创建去中心化的声誉层。

**安全模型：**

提供商必须为不同算法使用不同的服务密钥，当算法个性化时每个用户使用唯一密钥，防止跨用户查询的交叉关联。每个服务密钥配有一个描述算法行为的 kind 0 元数据 event，让用户了解其所信任的内容。断言 event 只应在底层数据实际发生变化时更新，防止不必要的 relay 流量，让客户端可以放心缓存结果。

**当前采用情况：**

NIP-85 将一种已非正式出现的模式正式化。Primal 的缓存服务器计算互动指标和 Web of Trust 评分。[Antiprimal](https://gitlab.com/soapbox-pub/antiprimal)（在 [Newsletter #9](/zh/newsletters/2026-02-11-newsletter/#antiprimal标准兼容的-primal-缓存网关) 中报道）使用 NIP-85 event kind 将这些计算桥接到标准 Nostr 客户端。[Nostr.band](https://nostr.band) 运营着规范自身示例中引用的 `wss://nip85.nostr.band` relay，为其搜索索引数据提供断言 event。在客户端侧，[Amethyst](https://github.com/vitorpamplona/amethyst)（由 vitorpamplona 创作，他也是此 NIP 的作者）在其 `quartz` 库中有实验性的 Trusted Assertions 支持，可解析断言 event 和服务提供商声明。[Vertex](https://vertexlab.io) 计算类似的 Web of Trust 指标，但[选择了不同的方式](https://vertexlab.io/blog/dvms_vs_nip_85/)，使用直接 API 而非 NIP-85 event，理由是断言架构的发现问题和计算开销。有了 NIP-85，任何客户端都可以通过标准 event 格式从任意提供商获取断言，提供商在准确性上竞争，用户自主选择信任对象。

## NIP 深入解析：NIP-52（日历 Event）

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md) 在 Nostr 上定义日历 event，为客户端提供表示和发现特定时刻或时间段内发生事件的标准方式。本周的 [D tag 合并](https://github.com/nostr-protocol/nips/pull/1752)添加了按天精度索引，补全了规范查询基础设施中缺失的部分。

**两种 Event 类型：**

NIP-52 根据时间精度将日历 event 分为两种 kind。基于日期的 event（kind 31922）表示全天发生的事件，如节假日或多日节庆。它们在 `start` 和可选的 `end` tag 中使用 ISO 8601 日期字符串，不考虑时区：

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

基于时间的 event（kind 31923）在 `start` 和可选的 `end` tag 中使用 Unix 时间戳表示特定时刻，另有 IANA 时区标识符（`start_tzid`、`end_tzid`）用于显示。两种 kind 都是参数化可替换 event，主办方通过发布具有相同 `d` tag 的新 event 来更新详情。

**日历和 RSVP：**

Kind 31924 event 将日历定义为集合，通过 `a` tag 引用 kind 31922 或 31923 event（通过其地址坐标）：

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

用户可以维护多个日历（个人、工作、社区），客户端可以订阅特定 pubkey 的日历。日历 event 可以包含引用日历的 `a` tag 来请求加入，实现协作日历管理，多个用户可以向不属于自己的日历贡献 event。

RSVP 使用 kind 31925，用户发布出席状态以及可选的空闲/繁忙指示：

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

有效的 `status` 值为"accepted"、"declined"、"tentative"，可选的 `fb` tag 将用户标记为该时段空闲或繁忙。RSVP event 引用日历 event 的 `a` tag 并携带主办方的 `p` tag，以便主办方客户端跨 relay 汇总响应。

**D Tag 的添加：**

在本周合并之前，客户端查询某个日期范围内的 event 时必须从某个 pubkey 或日历获取所有 event 并在客户端侧过滤。基于时间的 event（kind 31923）上新增的必需 `D` tag 包含按天精度的 Unix 时间戳，计算方式为 `floor(unix_seconds / 86400)`。跨多天的 event 携带多个 `D` tag，每天一个。Relay 现在可以按天对 event 建立索引并高效响应过滤查询，将原本的客户端过滤问题转变为 relay 端索引查找。

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

`D` 值 `20139` 等于 `floor(1740067200 / 86400)`，将此 event 定位于 2025 年 2 月 20 日。查询"本周所有 event"的客户端发送带相应 `D` 范围的过滤器，relay 仅返回匹配的 event。

**设计决策：**

NIP-52 故意省略了重复 event。规范完全不涉及重复规则（iCalendar 的 RRULE），将这一复杂性留给客户端处理。主办方为每次发生发布单独的 event，保持 relay 端数据模型简洁。参与者 tag 携带可选角色（"host"、"speaker"、"attendee"），位置 tag 可以包含用于空间查询的 geohash `g` tag，以及人类可读的地址。

**实现情况：**

[Flockstr](https://github.com/zmeyer44/flockstr) 是基于 NIP-52 构建的主要日历客户端。[Coracle](https://gitea.coracle.social/coracle/coracle) 在其社交信息流中显示日历 event。本周 `D` tag 的添加实现了 relay 端时间索引，两个客户端均可利用此功能在查询特定日期范围内的 event 时减少带宽消耗。

---

本周就到这里。正在构建什么？有新闻要分享？希望我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 [NIP-17](/zh/topics/nip-17/) 私信联系我们</a>或在 Nostr 上找到我们。
