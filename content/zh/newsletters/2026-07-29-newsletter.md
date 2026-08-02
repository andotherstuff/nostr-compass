---
title: "Nostr Compass #33"
date: 2026-07-29
translationOf: /en/newsletters/2026-07-29-newsletter.md
translationDate: 2026-08-02
draft: false
type: newsletters
description: "Amethyst 1.13.1 在 1.13.0 引入 Nostr 应用后加入经过认证的群组与 Blossom 访问；Mosaico 通过 Nostr 共享编码代理状态，Nostrology 则绘制 NIP-65 relay 列表集中度图谱。"
---

欢迎回到 [Nostr Compass](https://github.com/andotherstuff/nostr-compass)，您的每周 Nostr 指南。

**本周：**[Amethyst 1.13.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1) 紧随 1.13.0 版本的 Nostr 应用上线，加入 NIP-29 host relay 认证，以及经过认证的 Blossom 下载重试。[Code Call](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.68) 让用户可以继续从手机推进远程编码会话，[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) 协调维护者与仓库同步，[Mosaico](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) 则为编码代理提供共享的 Nostr 感知层。[Nostrology](https://dev.nostrolo.gy/relays) 绘制个人资料如何在其公布的 relay 列表中划分读写职责。来自 [Mafrend](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0)、[Hanami](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0) 和 [Cordn](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1) 的 Android 版本领衔打标签的发布，而 [FIPS 加入 OpenWrt 访问层](https://github.com/jmcorgan/fips/pull/126)，另有一个[开放 PR 提议移植到 FreeBSD](https://github.com/jmcorgan/fips/pull/129)。协议报道涵盖 NIPs、BUDs、NAPs、Marmot、Gamma Markets、Concord 和 NWC；[Nostr 六年七月史](https://github.com/nostr-protocol/nips/commits/master/)则沿着历年七月的变更，从早期域名查询讲到 relay 群组状态。

## 头条报道

### Amethyst 1.13.1 在推出 Nostr 应用后加入经过认证的群组与 Blossom 访问

面向 Android 与多平台的 Nostr 客户端 [Amethyst 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0) 于 7 月 28 日发布，在一个隔离且无密钥的浏览器进程内打开 napplet 和 NIP-5A nsite。经过用户同意后才启用的 `window.nostr` bridge 可以通过当前账户签名并使用选定能力，而按站点、按账户划分的权限界面让用户可以审查或撤销这些授权。收藏的应用可以固定在底部栏中，同时不会在不同账户之间共享 cookie、登录状态或授权。

同一个 [1.13.0 版本](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0)还加入 Git 仓库树、issue 和 pull request，以及 Concord 社区、NIP-29 relay 群组、Buzz 群聊、维基页面和 RSS feed。用户可以在同一个 Nostr 身份下往返于代码、社区、发布与社交视图之间。

[1.13.0 版本](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0)也扩展了支付与身份功能。Amethyst 可以创建并支付 BOLT12 offer、自动启动远程签名器账户、添加 Blossom fallback server，并扩展面向徽章、社区和 relay 群组的 Web of Trust 控件。7 月 29 日发布的后续版本 [1.13.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1) 加入 [CORD-02 解散封印](https://github.com/vitorpamplona/amethyst/pull/3767)、kind `9008` [群组与频道删除](https://github.com/vitorpamplona/amethyst/pull/3779)、[NIP-29 host relay 认证](https://github.com/vitorpamplona/amethyst/pull/3788)，以及针对受限 Blossom 下载的、经过认证的 [BUD-01 重试](https://github.com/vitorpamplona/amethyst/pull/3789)。

### Code Call 0.2.68 在 0.2.66 引入追赶摘要后加入 worker 文件夹浏览器

面向电脑端编码会话的 Android 遥控工具 [Code Call 0.2.68](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.68) 用一个以 worker 目录为根的文件夹浏览器取代了特殊处理的 workspace 列表。用户可以进入嵌套的获准文件夹，为 OpenCode 会话选择其中一个文件夹，并返回父文件夹；[0.2.67 版本](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.67)会在生成会话时打开该浏览器。

更早的 [0.2.66 版本](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66)可以让经过路由的 worker 根据手机上的最新消息提供一份简洁的追赶摘要。同一周的其他版本让[多个会话保持相互独立](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.51)，只接受来自[预期发送者](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.56)的回复，并让收件箱持续连接到[每个已配置的 worker relay](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.59)以便后台投递。请求和回复封装在 [NIP-17（私密直接消息）](/zh/topics/nip-17/)中传输，而本地加密的 [Blossom](/zh/topics/blossom/) 附件[在解密后保留原始文件类型](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.55)。

### GitWorkshop 协调维护者，并让仓库同步保持独立

[GitWorkshop 7 月 27 日的签名发布](https://primal.net/e/869e01f9a74d98f468a66f3b83865d198a82cc718c1db36324398b1b88a17c60)通过 [NIP-55（Android 签名器应用）](/zh/topics/nip-55/)为基于浏览器的 [NIP-34（`git` 相关内容）](/zh/topics/nip-34/) forge 加入 Android 登录。其[源代码仓库](https://github.com/DanConwayDev/gitworkshop)现在可以递归协调主要维护者、保留每位维护者的 relay hint，并让仓库同步不依赖邀请是否被接受。跨仓库 work item 引用把不同仓库中的相关工作连接起来，而 GRASP 会把仓库数据复制到选定的 Git endpoint，同时不把这项传输与邀请投递耦合。由开发者签名的 [3.1.1 更新](https://primal.net/e/01d0939e9960cb82f1f7aba6f1900af2c61ce384e38352221bf9d5878116ae2d)修复了 Android 签名器 intent 投递、递归维护者解析，以及保留路径的仓库链接。

### Mosaico 0.1.2 让编码代理通过 Nostr 共享状态

[Mosaico 0.1.2](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) 让 Claude Code、Codex、Goose、Hermes、OpenCode 和 Grok 中的编码代理会话可以通过 [NIP-29（基于 Relay 的群组）](/zh/topics/nip-29/)发布简短状态更新。不同 host 上的会话可以找到相关的活跃工作，而无需共享 transcript 或上下文。

具名 Codex profile 发现和 Goose 的 Top Of Mind 视图在两个 harness 中呈现这一共享状态（[PR #618](https://github.com/pablof7z/mosaico/pull/618)、[PR #619](https://github.com/pablof7z/mosaico/pull/619)）。该版本恢复了托管代理加入公共感知层的能力，设置流程现在要求明确选择 relay（[PR #626](https://github.com/pablof7z/mosaico/pull/626)、[PR #629](https://github.com/pablof7z/mosaico/pull/629)）。Mosaico 仍是一个感知层，不是代理 host、orchestrator 或 transcript 合并器。

### Nostrology 根据已发布的 NIP-65 event 绘制 relay 列表集中度图谱

[Nostrology 的 relay 观测站](https://dev.nostrolo.gy/relays)从每个个人资料最新的 [NIP-65（Relay 列表元数据）](/zh/topics/nip-65/) kind `10002` event 中生成数据集，并遵循[已发布的规范](https://github.com/nostr-protocol/nips/blob/master/65.md)。它区分读、写和组合 relay 角色，绘制每个个人资料列出多少 relay，并在可排序表格中公开底层计数。在 7 月 29 日发布审查时，该页面包含 34,430 个不同的 relay URL 值；恰好只列出一个 relay 的个人资料有 520,468 个，相比之下，列出三个的有 150,657 个，列出四个的有 60,710 个。

同一份 [Nostrology 快照](https://dev.nostrolo.gy/relays)显示，`relay.momostr.pink` 周围的重叠集中度为 298,859 个个人资料，`relay.damus.io` 为 287,181 个，`nos.lol` 为 279,468 个，`relay.primal.net` 为 225,336 个。这些计数衡量的是已发布的 relay 列表条目，而非可用性：原始表格可能包含格式错误的 URL 和本地地址，[NIP-65 规范](https://github.com/nostr-protocol/nips/blob/master/65.md)则定义路由元数据，并不测试 relay 健康状态。这个观测站让采用情况和数据质量问题变得可见，同时不会把已列出的 relay 当作正在运行的 relay。

## 打标签的发布

### Kairos 0.1.1 加入提醒和本地 Astraea 指令

[Kairos 0.1.1](https://primal.net/e/ffb054280008dc3ba488d5d3a2cbfec6c4123489a874683545a29a466682fd90) 加入截止日期提醒、给 Astraea 的明确本地指令，以及更严格的 relay 与 URL 处理。[0.1.0 签名发布](https://primal.net/e/6e02430844abdabf5421bbf5745a09ef2870e4ade93f56627ee14ba8db58a00a)推出了这款[离线优先的任务管理器](https://github.com/Lwb89dev/kairos)，其可选同步层会把经过 [NIP-44（加密载荷）](/zh/topics/nip-44/)加密的记录写入用户选择的 relay。Kairos 使用确定性的任务坐标和加密 tombstone，并附带 [NIP-09（Event 删除请求）](/zh/topics/nip-09/)删除请求；纯本地任务则永远不会离开设备。

### Bray 2.3.0 为 CLI 带来通用 gift wrapping 和本地 Blossom 测试界面

Nostr SDK 与命令行工具包 [Bray 2.3.0](https://github.com/forgesworn/bray/releases/tag/v2.3.0) 可以通过 [NIP-59（Gift Wrap）](/zh/topics/nip-59/)对任意 event 进行 gift-wrap 和解包；如果密钥由 bunker 持有，签名会通过 [NIP-46（Nostr Connect）](/zh/topics/nip-46/)完成。[PR #75](https://github.com/forgesworn/bray/pull/75) 还让捆绑的测试 relay 发出 [NIP-42（客户端对 Relay 的认证）](/zh/topics/nip-42/) challenge，并公开其余 Blossom 客户端命令。[PR #77](https://github.com/forgesworn/bray/pull/77) 加入内存中的 BUD-01/02 server，其签名授权会把每次上传或删除绑定到单个 blob；[PR #76](https://github.com/forgesworn/bray/pull/76) 则加入具名 event kind、简写 tag 和 [NIP-77](/zh/topics/nip-77/) ID 对账 flag，避免下载调用者已经持有的 event。

### Buzz Desktop 0.5.0 收紧邀请、搜索与 relay 身份更新

继上周报道 Armada 和 Buzz workspace 后，[Buzz Desktop 0.5.0](https://github.com/block/buzz/releases/tag/v0.5.0) 加入限制使用次数的邀请链接（[PR #3141](https://github.com/block/buzz/pull/3141)），以及按作者、频道和时间范围筛选的搜索 filter（[PR #2871](https://github.com/block/buzz/pull/2871)）。[PR #2862](https://github.com/block/buzz/pull/2862) 通过桌面应用的原生网络层获取加入策略，[PR #2607](https://github.com/block/buzz/pull/2607) 则在角色名称变更抵达 relay 后，重新发布代理的身份记录。该版本还为一则 [NIP-44 远程拒绝服务公告](https://github.com/block/buzz/pull/3135)更新 Nostr 依赖，并修复本地存储恢复、线程定位、relay 重连，以及 Linux 和 Windows 运行时路径。

### Shosho 1.0.0 扩展直播市场

[Shosho 1.0.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.0.0) 围绕创作者、直播会话、片段和商品重新设计直播市场，用户可以通过可配置的 relay 搜索找到这些内容。统一通知 feed 现在会汇集提及、reaction、转发和 zap，并支持用户不离开 feed 就直接回复。观看者可以从直播或回放中发布片段，该版本还改进了线程式聊天、片段回复、个人资料加载和网络使用。

### Mafrend v1.0 预览 Android 上基于地点的 Nostr 聊天

[Mafrend v1.0](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0) 是一款计划以地点为基础的 Nostr 聊天应用，其首个公开 Android alpha 版本。它的[项目页面](https://mafrend.com)将这组功能标为仍在积极开发，并把每个地图位置描述为围绕某个地点展开对话的专用聊天室。公开发布仓库提供可安装的 Zapstore 软件包，而主应用仍保持私有。

### Hanami 0.1.0 为 Blossom server 提供经签名器中介的 Android 路径

Blossom server 的 Android 伴侣应用 [Hanami 0.1.0](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0) 让用户可以通过手机登录 [Blossom](/zh/topics/blossom/) server、上传和下载。该应用使用 [NIP-55（Android 签名器应用）](/zh/topics/nip-55/)完成经审批中介的签名，并以原生 [NIP-98（HTTP Auth）](/zh/topics/nip-98/) handshake 建立 server 会话。Hanami 把 web shell 和签名 bridge 锁定到所选 server 的 origin，让凭据留在签名器中，同时由 server 现有的 web 界面提供应用体验。首个公开版本要求 Android 8 或更高版本、可访问的 Hanami server，以及兼容的签名器应用。

### Cordn 在 Android 上推出基于 Nostr 身份的群聊

私密群组消息客户端 Cordn 现在为 Android 用户提供 Nostr 身份引导、通过 [NIP-05（将 Nostr 密钥映射到基于 DNS 的互联网标识符）](/zh/topics/nip-05/)建立的个人资料链接，以及可在应用中打开 Cordn 目标的已验证链接。[7 月 24 日发布的 0.2.1 版本](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1)在现有 web 客户端之外引入这一原生产品线。消息使用群组加密协议 [MLS](/zh/topics/mls/)，并由 coordinator 辅助投递，因此群组无需电子邮件地址或电话号码，也能保留有序的加密对话。

### Nostur 1.30.1 修复线程和重复发帖，此前 1.30.0 扩展了分享功能

面向 iPhone、iPad 和 Mac 的 Nostr 客户端 [Nostur 1.30.1](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.1) 让用户可以浏览嵌套回复线程，不再受到破坏新布局的展开与折叠故障影响。它还可以防止同一份草稿被发布两次，包括媒体上传回调重复发生时。该版本紧随 [1.30.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.0)；后者加入自动消失的直接消息，以及通过 share sheet 把媒体发送到 Nostr 的路径，因此应用如今在加入新的消息与发布路径后，也修复了日常线程浏览和发帖流程。

### Formstr Drive 0.0.2 将 Nostr 文件元数据与 Blossom blob 配对

Nostr 原生文件管理器 [Formstr Drive 0.0.2](https://github.com/formstr-hq/formstr-drive/releases/tag/v0.0.2) 为用户提供应用内预览，以及在 Nostr Docs 中打开办公文档的选项。底层会把大文件以分块的 [Blossom](/zh/topics/blossom/) blob 存储，并在用户移除文件时删除远程 blob。本地 relay 让应用的 Nostr 元数据触手可及，而 Blossom 保存文件数据，从而把文件组织方式与大体积字节本身分离。

### NoorNote 1.3.1

面向 web、桌面和 Android 的 Nostr 客户端 [NoorNote 1.3.1](https://github.com/77elements/noornote/releases/tag/v1.3.1) 加入消息消失计时器，并为新建账户配置可用的默认 DM relay。它会过滤没有封面图片的全局文章，并把转发通知路由到文章阅读器。此前的 [1.3.0 版本](https://github.com/77elements/noornote/releases/tag/v1.3.0)加入 [NIP-53（直播活动）](/zh/topics/nip-53/)卡片、[NIP-68（图片优先信息流）](/zh/topics/nip-68/)人物 tag、[NIP-78（应用数据）](/zh/topics/nip-78/)软静音，以及 note 的 relay-seen 状态。

### algia 0.0.133

Go 语言 Nostr 命令行客户端 [algia 0.0.133](https://github.com/mattn/algia/releases/tag/v0.0.133) 紧随 [0.0.132](https://github.com/mattn/algia/releases/tag/v0.0.132)；后者加入 [NIP-29（基于 Relay 的群组）](/zh/topics/nip-29/)列表、时间线、发帖、reaction、删除，以及加入和离开流程。同一版本还为配置为强制认证的 relay 加入 [NIP-42（客户端对 Relay 的认证）](/zh/topics/nip-42/)预认证。0.0.133 版本随后为常规、频道和群组发帖命令加入本地图片上传，把生成的 URL 与 [NIP-92（媒体附件）](/zh/topics/nip-92/) tag 附加到每个 event。它也支持纯图片帖子；群组帖子默认使用群组的 relay 媒体存储，其他帖子则使用已配置的文件 server。

### swift-nostr 0.7.0

面向 Swift 应用的 Apple 平台 Nostr 库 [swift-nostr 0.7.0](https://github.com/yysskk/swift-nostr/releases/tag/0.7.0) 让一个 [NIP-46 远程签名器](/zh/topics/nip-46/)可以通过签名抽象驱动全部客户端功能。该版本加入 [NIP-98（HTTP Auth）](/zh/topics/nip-98/)和 [NIP-29（基于 Relay 的群组）](/zh/topics/nip-29/)支持，包括群组加入、发帖和管理流程。它还会根据官方测试向量验证 [NIP-44（加密载荷，版本化）](/zh/topics/nip-44/) padding，拒绝那些 MAC 有效、padding 却不规范的载荷。

### lawallet-nwc 2.0.0

[LaWallet NWC 2.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.0.0) 是一款 Nostr 连接钱包及 [NIP-47（Nostr Wallet Connect）](/zh/topics/nip-47/)服务，加入 passkey 登录，通过 WebAuthn PRF 扩展在浏览器中派生 Nostr 签名密钥。server 永远不会收到该 secret，同一个 passkey 也可以在另一台已同步设备上恢复相同密钥。账户现在可以链接并合并多个 Nostr pubkey，可选 listener 服务则会转发 wallet-connect event，并在 endpoint 无法访问后重试 webhook 投递。

### MDK 0.9.10

[MDK 0.9.10](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.10) 是 [Marmot 协议](/zh/topics/marmot/)的 Rust 实现，会在 transport 未启用期间保留待发送内容，并[监控 relay 通知转发](https://github.com/marmot-protocol/mdk/pull/1157)，让入站投递在 lag、panic 或关闭后恢复。[PR #1159](https://github.com/marmot-protocol/mdk/pull/1159) 为本地代理加入持久、可分页的对话历史和完整回复上下文，[PR #1167](https://github.com/marmot-protocol/mdk/pull/1167) 则重新发布当前已签名的 KeyPackage event，而不生成替代品。该版本还保留手动聊天排序、支持群组最终解散，并扩展按 Web of Trust 排名的搜索、relay 策略 API 和语言绑定。

### pakstr 0.3.1

[pakstr 0.3.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.3.1) 让把 Nostr 客户端打包为 Android 应用的 web 团队可以提供运行时配置和 API proxy，而无需重新构建应用 shell。其[同日发布系列](https://git.nostrdev.com/stuff/pakstr/releases)在 0.3.x 运行时配置工作之前加入 Amber 签名器 bridge、[NIP-44（加密载荷）](/zh/topics/nip-44/)加密与解密，并修正 Android 权限注入。scaffold 把捆绑的 web asset 保留在本地，而部署专用设置在运行时到达；proxy 则在普通 relay 连接之外，为封装后的应用提供一条受控 API 请求路径。

### Ditto 2.34.2

可定制的 Nostr 社交客户端 [Ditto 2.34.2](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.2) 会在 feed、详情页和引用嵌入中以卡片形式渲染用户状态，包括自定义 emoji、到期时间和可选链接预览。带评论的 zap 现在会作为回复显示在所引用帖子下方。该版本还保留 [2.34.1 引入的可选个人资料地球按钮](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.1)，供发布 [NIP-5A（网站清单）](/zh/topics/nip-5a/)根站点的所有者使用，并修复主页导航、直播搜索、外部链接处理和失效的自定义 emoji。

### Earthly 0.0.9

基于 Nostr 构建的协作地图编辑器 [Earthly 0.0.9](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.0.9) 现在会在地图实体 drawer 关闭、重新打开或刷新时继续显示 like。其 [NIP-57（Lightning zap）](/zh/topics/nip-57/)流程会发送有效的 zap-request JSON，让 Lightning provider 可以把经过验证的 receipt 发布到可公开访问的 relay，包括本地开发期间。生成的 invoice 会在实体界面变化后继续显示，经过验证的 receipt 到达后，应用也会显示确认。

## 开发中

### Keep 加入按 kind 限定的 NIP-44 v3 签名，并收紧审批策略

Keep 合并了五项 Android 签名器变更，用于传递 [NIP-44（加密载荷）](/zh/topics/nip-44/) v3 加密与解密请求，这些请求会经过两种 [NIP-55（Android 签名器应用）](/zh/topics/nip-55/) transport 及其 [NIP-46（Nostr Connect）](/zh/topics/nip-46/) bunker。[PR #451](https://github.com/privkeyio/keep-android/pull/451)、[#452](https://github.com/privkeyio/keep-android/pull/452) 和 [#453](https://github.com/privkeyio/keep-android/pull/453) 将 v3 授权与 v2 分开，按 event kind 限定授权范围，拒绝缺失或无效的 kind，并保留从通知中打开的审批请求。[PR #454](https://github.com/privkeyio/keep-android/pull/454) 和 [#455](https://github.com/privkeyio/keep-android/pull/455) 不再把 Basic 签名策略当作 Auto，并把全局选择移入由 core 持有的加密存储。Keep 维护者在最新的 Android 打标签版本之后合并了全部五项变更。

### Routstrd 在一次未经认证的暴露后更改默认网络 bind

Routstrd 的 [PR #56](https://github.com/Routstr/routstrd/pull/56) 把本地 Nostr 推理路由器的默认 bind 地址从所有网络接口改为 `127.0.0.1`。此前的默认值会向任何能访问该端口的 host 暴露未经认证的钱包余额、历史、访问、发送、退款、API key、provider、client、使用情况和 daemon stop endpoint。运营者仍可明确配置非本地 bind，但已合并的变更让全新部署默认仅限本地访问，目前尚未出现在打标签版本中。

### Imwald Android 明确离线发布状态

Android Nostr 客户端 Imwald Android 现在仅在所有已配置目标都是本地目标时，才把来自本地 relay 的确认视为发布完成。它的[离线发布与 outbox 修复](https://git.imwald.eu/silberengel/imwald-android/commit/f4de9f61df35110c77d2e5f99d764c0df176962b)会在本地 relay 已接受 event、但已配置的远程 relay 尚未接受时维持远程投递的待处理状态，因此发布报告可以区分设备本地存储与 relay 投递。

### FIPS 加入 OpenWrt 访问层；FreeBSD 移植仍在审查

Nostr 原生 Free Internetworking Peering System 现在可以通过[已合并的 PR #126](https://github.com/jmcorgan/fips/pull/126)，让 OpenWrt 路由器公开一个开放的 `!FIPS` 接入网络。与之并行、仍开放的 [FreeBSD PR #129](https://github.com/jmcorgan/fips/pull/129) 提议移植 daemon、TUN data path、`.fips` 名称解析、服务管理和原生软件包构建。OpenWrt 合并现在就扩大了访问范围，FreeBSD 工作则会把它扩展到另一个通用操作系统。

7 月 26 日的 [FIPS 项目更新](https://primal.net/e/d0afe733f75e909341ab7f39834883968df097472238a474df3a3346c5d38f51)报告称，其公共 UDP overlay 上已有 300 多个节点，更广泛的 mesh 则接近 2,000 个节点。[FIPS 仓库](https://github.com/jmcorgan/fips)同一周也在加固并发网络测试、rekey 连续性、hop limit 行为、防火墙检查和 NAT 实验室隔离。随着网络增长，这些仓库工作为运营者提供了可复现的行为检查。

### Zap Cooking 安排定时发帖，并绑定扫描器请求

Nostr 食谱分享与膳食规划应用 Zap Cooking 现在可以把定时帖子保存在加密存储中，并在到期时通过周期性 relay sweep 发布（[PR #566](https://github.com/zapcooking/frontend/pull/566)、[PR #569](https://github.com/zapcooking/frontend/pull/569)）。这为用户提供了一条定时发布路径，同时不会把未签名的帖子内容暴露在 scheduler 数据库中。

它的冰箱扫描器现在使用 [NIP-98](/zh/topics/nip-98/) HTTP 认证来验证确切的请求 body，因此成员资格检查依赖签署扫描请求的密钥，而不是其 body 中提供的 pubkey（[PR #599](https://github.com/zapcooking/frontend/pull/599)）。

### Citrine 把 Android 设备变成可管理的 relay

Android 托管的 Nostr relay Citrine 现在可以把已存储的 event 发送到外部 relay，为运营者提供重新广播本地历史的方法（[PR #179](https://github.com/greenart7c3/Citrine/pull/179)）。它还加入 [NIP-86（Relay 管理 API）](/zh/topics/nip-86/)命令，让兼容客户端可以管理 relay（[PR #150](https://github.com/greenart7c3/Citrine/pull/150)）。

群组运营者可以通过 Amber 签名管理基于 relay 的 [NIP-29](/zh/topics/nip-29/) 群组，这项功能由 [PR #178](https://github.com/greenart7c3/Citrine/pull/178) 加入；[PR #174](https://github.com/greenart7c3/Citrine/pull/174) 则让基于 Tor 的 relay 配置与生命周期状态在重启期间保持一致。

### Wired 在浏览器中恢复完整对话

基于浏览器的 Nostr 客户端 Wired 现在会沿着 feed root、回复和引用 event 一直检索到完整结果，不再停在固定广度或结果数量限制处（[PR #148](https://github.com/smolgrrr/Wired/pull/148)、[PR #147](https://github.com/smolgrrr/Wired/pull/147)、[PR #146](https://github.com/smolgrrr/Wired/pull/146)）。因此，只要用户的 relay 上存在相关 event，他们就可以恢复更深的线程和 feed 上下文。

浏览器还会保留引用 event 上的 relay hint，并且只把它们用于仍然缺失的上下文，从而恢复已配置 relay 没有保存的对话（[PR #145](https://github.com/smolgrrr/Wired/pull/145)、[PR #144](https://github.com/smolgrrr/Wired/pull/144)）。不完整的检索会与完整快照明确区分，因此部分响应不会覆盖此前缓存的视图。

## 协议与规范工作

### NIPs：NIP-34 托管边界、群组迁移与三个活跃草案

本周合并了两项规范变更。[NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23) 从 `kind:1618` pull request 描述中移除 GRASP 托管说明，让托管和 fallback 行为留在 event 契约之外。[NIP-29 commit db5fe3d](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057) 则定义 relay 群组元数据如何迁移到另一个 relay，以及客户端如何区分有效迁移与仍在独立延续的 fork。

[PR #2424](https://github.com/nostr-protocol/nips/pull/2424) 提议相互声明 `kind:10045` 密钥集。双向要求会防止一个身份单方面附加另一把密钥。[PR #2421](https://github.com/nostr-protocol/nips/pull/2421) 提议加入 BOLT12 zap intent 和付款人证明，客户端可以根据目标、金额、offer 和已结算付款验证这些证明，而不依赖收款人运营的 receipt server。

[PR #2425](https://github.com/nostr-protocol/nips/pull/2425) 将允许 NIP-B0 书签在 web URL 之外保留 `nostr:` 等非 HTTP scheme。这会让原生 Nostr 标识符、支付请求和其他应用 scheme 在已经保存 web 地址的同一份私有或公开书签列表中保持完整。

### Mill 实现云账户密钥备份草案

Mill [宣布](https://primal.net/e/6362d9b00662fa64200530f8a29ae547521bac0a1e3c9379ef9086eac7d2030b)已经实现一份[云账户密钥备份草案](https://github.com/0ceanSlim/nostr-mill/blob/main/docs/nip-cloud-key-backup.md)，该草案把 Google OIDC 账户标识符与高熵 passphrase 组合起来，派生一次性备份密钥。其[参考实现](https://github.com/0ceanSlim/nostr-mill/blob/main/src/nipbackup.js)把用户的真实密钥加密为 [NIP-49（私钥加密）](/zh/topics/nip-49/) `ncryptsec`，再将其存入已配置 relay 上一个临时的参数化可替换 kind `30049` event。项目已[把备份流程合并到 main](https://github.com/0ceanSlim/nostr-mill/commit/eeb4b9114d02114b703a6823ad36ca8063b224da)，但 v1.0.0 之后没有任何版本包含该功能；除非运营者提供专用 `backupRelays`，备份流程仍保持禁用。带版本的 relay 集合仍属临时设计，草案也警告已发布的 ciphertext 会继续存在，可供离线猜测 passphrase。读者应把这项设计视为一项依赖高熵 passphrase 的已实现实验。

### BUDs：Blossom server 可以根据字节识别未知上传内容

[BUD-02 PR #110](https://github.com/hzrd149/blossom/pull/110) 提议，当上传者省略 `Content-Type` 或发送 `application/octet-stream` 时，建议在 server 侧检测 MIME。Blossom server 会使用持续维护的文件类型库检查开头几个字节，保留客户端提供的具体类型，并在检测失败时回退到通用二进制类型。这样可以让图片、音频、视频和代理生成的文件保持可渲染，同时无需强制每次上传都进行字节嗅探。

### NAPs：随着捕获与文件系统契约的发展，约定取代编号轨道

[PR #87](https://github.com/napplet/naps/pull/87) 移除带编号的跨 napplet 协议轨道，把运行时能力保留在具名契约下，同时让应用消息汇聚到 `napplet:<archetype>/<intent>` 约定 URI。已合并的[主题身份变更](https://github.com/napplet/naps/pull/89)把稳定且不带 query 的约定路径与每条消息的载荷数据分开，[PR #90](https://github.com/napplet/naps/pull/90) 则把这项转置规则应用于发现与 handler 元数据。

两份 NAP 草案扩展了受信任的 shell 边界。[NAP-CAPTURE PR #94](https://github.com/napplet/naps/pull/94) 把麦克风同意、平台权限、限制、保留和 teardown 留在运行时，同时向沙盒化 napplet 返回有界媒体 artifact。[NAP-FS PR #88](https://github.com/napplet/naps/pull/88) 是相应的虚拟文件系统提案，以受策略约束的 handle 取代不受限制的 host 路径。

### Marmot：规范定义最终群组状态

[Marmot PR #409](https://github.com/marmot-protocol/marmot/pull/409) 加入经过认证且不可逆的 `Disbanded` 状态，因为 MLS 本身没有群组删除操作。经过授权的管理员 commit 会把群组移出 `Active`，阻止旧 branch、消息和 Welcome 将其恢复，并为现有群组提供一条明确的兼容路径，完成后方可解散。此前的[规范 issue sweep](https://github.com/marmot-protocol/marmot/pull/408)还协调了群组状态权威性、收敛、key package、acknowledgement、媒体规则、registry 表述，以及 200 个已追踪的规范 issue。

### Gamma Markets：没有公开规范变更落地

[Gamma Markets 规范仓库](https://github.com/GammaMarkets/market-spec)在 7 月 21 日至 7 月 28 日期间没有记录公开 commit 或 pull request 活动。其已发布的订单、结算和市场数据文档仍是当前基线；这条无变更记录让 Gamma 继续出现在每周规范扫描中。

### Concord：同一 plane 内的读写能力可能拆分

[Concord PR #12](https://github.com/concord-protocol/concord/pull/12) 仍是一份开放草案，面向读者不应全部拥有写入权限的 plane。它推动 Control Plane 采用分离的读写 stream 能力，并勾勒受限写入频道、邀请和 rekey 范围。草案中的写密钥充当 spam gate，而经过签名的内部 actor 和 roster 检查继续承载权威性。

### NWC：一个钱包方法可以在 BOLT11 与 BOLT12 之间选择

[NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2) 提议为 BIP-321 支付 URI 加入可选的 `pay` 和 `receive` 方法。钱包服务可以宣告支持，从 URI 中选择一个兼容的 BOLT11 invoice 或 BOLT12 offer，在支付前拒绝不匹配的 Bitcoin 网络，并报告使用了哪种指令类型。该提案留在 NWC core 之外，因此不支持 BIP-321 或 BOLT12 的钱包无需实现它。

## Nostr 六年七月史

这篇七月历史回顾沿着 Nostr 反复面对的几类问题展开：可读标识符、relay 过滤、可移植应用数据、隐私与互操作性。六年间，每一层都把一项狭窄修复转化为共享基础设施：名称成为个人资料，filter 成为应用契约，通过 relay 承载的状态则从 note 扩展到直播房间与群组。它从[首个 NIP-05 实现](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599)开始，以[本月的可寻址发现合并](https://github.com/nostr-protocol/nips/commit/2f4b09335c54a993d483bc220195e3f4a33df1ec)结束，随后审视历年七月中推动这些主题发展的变更。

### 2021 年 7 月

2021 年 7 月 19 日，[nostr-tools commit 1ce00bd](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599) 加入 `nip05.js` 模块，并把软件包版本提升到 0.5.0。其 `keyFromDomain` 函数为 `_nostrkey.<domain>` 构建 DNS TXT 请求，把二进制 query 发送到八个轮换的 DNS-over-HTTPS provider 之一，并返回答案中的第一把密钥。因此，浏览器客户端无需运行 DNS resolver，也无需依赖一个硬编码 provider，就能把由人控制的域名转换为公钥。

第一种方法解决了查询，却没有解决域名内的名称，其信任边界位于 DNS 与所选 resolver。现代 [NIP-05 规范](https://github.com/nostr-protocol/nips/blob/master/05.md)把发现迁移到 `/.well-known/nostr.json`；域名会在那里把本地名称映射到 pubkey，并可附加 relay hint。2021 年的代码记录了当时的设计压力：公钥可以移植，但人们仍需要自己能够阅读、验证并在客户端之间迁移的标识符。

### 2022 年 7 月

7 月 10 日，[NIP-12 commit 3771186](https://github.com/nostr-protocol/nips/commit/3771186c0351656a675576051b75d253f26c0f0b) 把通用 relay query 限定为单字母 tag。这项决定让 `#r`、`#g` 和 `#t` 等 filter 可以用于 URL 引用、geohash 和 hashtag，而无需要求 relay 索引每个任意元数据 key。十天后，首份 [NIP-20 web 评论草案](https://github.com/nostr-protocol/nips/commit/9f9a864ce1e1ebfdcfdd4835cd60807440f038e8)直接使用这种 query 模型：kind `34` 评论在 `r` tag 中携带规范化网页 URL，让网站与独立客户端可以从 relay 恢复同一场讨论。

随后出现的是 relay 策略与社交反馈。最初的 [NIP-22 commit](https://github.com/nostr-protocol/nips/commit/f51ce9dc0efaf61f39a76e112c310a9f58af1c87)允许 relay 拒绝 `created_at` 时间戳过于久远而不可信的 event，[commit 8bef0e9](https://github.com/nostr-protocol/nips/commit/8bef0e9d79ebb4b11f8fd2bea11dc8f1668bc9d0) 则把未来时间戳加入同一策略。7 月 30 日，[NIP-25 commit dcbd504](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88) 定义了 kind `7` reaction，并以 `e` 与 `p` tag 标明目标；下一个 commit 把 `-` 指定为负面 reaction，[commit 6903ff5](https://github.com/nostr-protocol/nips/commit/6903ff5b2c395a550a26069f6e2b5460ae1fdca6) 则把 `+` 设为明确的通用 like。这些 commit 共同为采用草案的客户端规定了 relay 时间戳拒绝、基于 tag 的检索、web 评论和 reaction tag。

### 2023 年 7 月

2023 年 7 月把协调推进到短 note 之外。[NIP-37 密钥丢失草案](https://github.com/nostr-protocol/nips/commit/e057fa01ca3928a32bdc0e9a44c27f946f267041)探索不可逆的密钥退役、社交恢复 threshold 和预先承诺的替代密钥，同时明确拒绝把结果称作通用密钥轮换。五天后，[NIP-53](https://github.com/nostr-protocol/nips/commit/141197c564d97073f0293e3b2f367f0b6b3619c2) 引入可寻址的 kind `30311` 直播活动与 kind `1311` 聊天消息，为 stream、stage 和直播房间提供一套共享 event 模型，用来表达 host、参与者、状态与对话。

应用也开始宣传工作与商务活动。首份 [Data Vending Machine 草案](https://github.com/nostr-protocol/nips/commit/67e950a2009e81df1b8c91b0a2ade0596e83f168)描述了 kind `68001` 工作请求、kind `68002` 结果、bid、到期、chaining，以及为转录、摘要和翻译等任务竞争的 provider。7 月 13 日，[分类信息草案](https://github.com/nostr-protocol/nips/commit/451c06a3c572a13afe45c1d80616f8e6dd9bb1de)加入可寻址的 kind `30402` offer，带有标题、摘要、价格、位置和状态元数据。这些草案后来成为 NIP-90 和 NIP-99，但它们在当年七月的形态已经把请求或 listing 与展示它的 server 分开。

支付路由也变得可组合。7 月 31 日的 [NIP-57 zap 分配合并](https://github.com/nostr-protocol/nips/commit/5d63b1570c490007252b10e757f7f68ef1f4b717)把单个 `zap` 目标改为包含收款人 pubkey 和 relay hint 的加权列表。客户端可以在协作者之间分配一个 zap，在存在部分权重时省略未加权的收款人，并在支付前展示分配方案。该变更标准化了加权 zap 收款人和 relay hint 的签名 event 表示，让兼容客户端可以在支付前呈现分配方案。

### 2024 年 7 月

7 月 4 日，[NIP-29 commit c60ca88](https://github.com/nostr-protocol/nips/commit/c60ca888efbdc9b8fa4bbfbace372409d0b2161a) 加入用于创建群组的 `kind:9007` relay 管理操作。六天后，[NIP-70](https://github.com/nostr-protocol/nips/commit/ae1906ec7943a6bd756f05d2cd2fb2a041398921) 定义受保护 event：`-` tag 告诉 relay 只接受来自 event 已认证作者的发布。一项变更给 relay 提供明确的群组状态转移；另一项让作者可以阻止第三方把原本有效的签名 event 重放到 relay 中。

7 月 16 日，一项 [Cashu 规范 commit](https://github.com/nostr-protocol/nips/commit/506b38916ab67a37b2d98b46b62cf0c0c5fde5a4)同时引入 NIP-60 钱包和 NIP-61 nutzap。NIP-60 把钱包元数据放入 kind `37375`，把未花费 proof 放入加密的 kind `7375` event，并把可选交易历史放入 kind `7376`。NIP-61 把收款人的 kind `10019` mint 与 relay 偏好，同受 P2PK 锁定的 kind `7337` nutzap 配对。钱包状态和 bearer token 现在可以通过 relay 移动，但赎回仍依赖 Cashu mint proof，并需要谨慎防止重复 claim。

七月下旬的两项编辑收紧了确定性状态。[NIP-01 commit 9c54549](https://github.com/nostr-protocol/nips/commit/9c54549f1842245b842d8a66f3bade744da24189) 要求在 `created_at` 时间戳相同时以 event ID 作为 tie-breaker，使客户端可以用相同顺序排列同一结果集。[NIP-09 删除合并](https://github.com/nostr-protocol/nips/commit/722ac7a58695a365be0dbb6eccb33ccd7890a8c7)则澄清 kind `5` 请求可以指向 event ID 或可寻址坐标，并应包含 `k` tag，标明 relay 应删除的 kind。两项变更都缩小了两个正确实现可能产生分歧的空间。

### 2025 年 7 月

Ecash 发现于 7 月 16 日获得自己的社交目录。[NIP-87 commit 1afb6da](https://github.com/nostr-protocol/nips/commit/1afb6da049e57dd628ef46a3b0f90300653a66ee) 定义 kind `38172` Cashu mint 记录、kind `38173` Fedimint 记录，以及可以带 relay hint 指向这些记录的 kind `38000` 推荐。钱包可以在连接 mint 之前查询受信任作者的推荐，而规范也警告，未经筛选的全局发现可能把用户引向恶意运营者。

一周后，一份草案为语音消息规定可移植的 Nostr event 记录。首个 [NIP-A0 commit](https://github.com/nostr-protocol/nips/commit/e50f37a527ace39cc3057827d52295c6b6de1112) 把 kind `1222` 分配给语音消息根 event，把 kind `1244` 分配给回复，并携带音频 URL 与媒体元数据。7 月 27 日的[格式后续变更](https://github.com/nostr-protocol/nips/commit/4984b057c20397eae919ee5e463bc8a5d3fb2dc0)建议在 Ogg 容器中使用 Opus，并标准化压缩波形。客户端无需就单一录音器、host 或波形表示达成一致，也能交换短音频。

随后，私密消息与钱包连接加入协议状态，用于读取跟踪、加密选择和支付进度。[NIP-17 commit 3d76da3](https://github.com/nostr-protocol/nips/commit/3d76da368e157934e056d95b3b3d8d6eaa105b09) 定义一个可替换的 kind `30016` 记录，其有序 `seen` tag 让客户端可以区分已读消息和可能错过的间隙。7 月 31 日，[NIP-47 加密协商](https://github.com/nostr-protocol/nips/commit/f30a43bd37e08516923b96dd0d860122c9ffe04e)让钱包服务可以宣告 NIP-44 v2 或旧版 NIP-04，而[交易状态 commit](https://github.com/nostr-protocol/nips/commit/0595d438aaa163dd33ed00748026698a411a0861)加入 `pending`、`settled`、`accepted`、`expired` 和 `failed` 状态。投递、加密与支付进度成为明确的协议数据，不再由本地推断。

### 2026 年 7 月

这个七月首先把普通 web 地址连接到 relay query。[可寻址发现 commit 2f4b093](https://github.com/nostr-protocol/nips/commit/2f4b09335c54a993d483bc220195e3f4a33df1ec)定义 `/.well-known/nostr.json?ad=<path>` 查询，其响应包含 Nostr filter 和 relay 列表。普通浏览器仍可把原始 URL 作为 HTML 打开，Nostr 客户端则可以查询相应的 `/.well-known/nostr.json?ad=<path>` endpoint，获取把该地址解析为群组、nsite、feed、event 或其他原生对象的 filter 与 relay 列表。这个模式在更广的层面上重新审视 2021 年的域名到密钥问题：一个人类可读的 URL 现在可以同时命名身份与 query。

NIP-29 随后从扁平的 relay 群组发展为结构化空间。7 月 16 日的[子群组 commit](https://github.com/nostr-protocol/nips/commit/223ddb3b0c282f2a133adb9f4a9c098a31b36937)加入父级与有序子级关系；相邻 commit 加入邀请码后缀、banner、有序 pin 快照和可寻址 event pin。7 月 22 日的[迁移与分叉澄清](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057)定义元数据何时会把群组合法迁移到另一个 relay，以及仍然活跃的 branch 何时成为独立 fork。群组标识符保持简单，层级、展示和 relay 变更则成为明确状态。

两项较小的编辑澄清了实现边界。[NIP-46 commit f0af204](https://github.com/nostr-protocol/nips/commit/f0af20484c5e0d12e2d1936f87c5a6681a08daff) 要求远程签名器对未知或不受支持的方法返回错误，避免客户端只能静默等待超时。[NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23) 从 pull request event 描述中移除 GRASP 专用托管说明。一项让调用者获得终止响应；另一项防止可移植 git event 悄然继承某一种 server 协议。

---

通过 [Nostr Compass 项目](https://github.com/andotherstuff/nostr-compass)发送 NIP-17 DM，分享项目或新闻线索。
