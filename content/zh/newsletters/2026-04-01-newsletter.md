---
title: 'Nostr Compass #16'
date: 2026-04-01
translationOf: /en/newsletters/2026-04-01-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Amethyst](https://github.com/vitorpamplona/amethyst) 在 [v1.07.0](#amethyst-发布固定笔记relay-管理和-request-to-vanish) 中发布固定笔记、通过 [NIP-86](/zh/topics/nip-86/) 进行 relay 管理，以及对 [NIP-62](/zh/topics/nip-62/) Request to Vanish 的支持。[NIP-5A](#nip-5a-合并将静态网站引入-nostr)（静态网站）合并进 NIPs 仓库，定义了如何在 Nostr 密钥对之下使用 [Blossom](/zh/topics/blossom/) 存储托管网站。[Flotilla](https://gitea.coracle.social/coracle/flotilla) 在 [v1.7.0](#flotilla-v170-增加语音房间和邮箱登录) 中加入语音房间、邮箱密码登录和工作量证明 DM。[White Noise](https://github.com/marmot-protocol/whitenoise) 在 [v2026.3.23](#white-noise-修复-relay-抖动并扩展客户端控制) 中修复 relay churn，[nospeak](https://github.com/psic4t/nospeak) 发布了其 [1.0.0](#nospeak-作为-10-私密信使发布) 版本，定位为无需注册的加密信使。[Nymchat](https://github.com/Spl0itable/NYM) [采用 Marmot](#nymchat-发布基于-marmot-的群聊) 实现带 NIP-17 回退的 MLS 加密群聊。[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) 在 [v1.0.0](#calendar-by-form-v100) 中加入私有日历列表和 ICS 导入，[Amber](https://github.com/greenart7c3/Amber) 增加了[助记词恢复和 NIP-42 relay auth 白名单](#amber-v502-through-v504)，[Marmot 规范](#marmot-将-keypackages-迁移到可寻址事件并收紧推送通知格式)则将 KeyPackages 迁移到可寻址 event 并收紧了 MIP-05 推送通知格式。

## 新闻

### Amethyst 发布固定笔记、relay 管理和 Request to Vanish

[Amethyst](https://github.com/vitorpamplona/amethyst) 这个由 vitorpamplona 维护的 Android 客户端，在三天内连发六个版本，从 [v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) 到 [v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5)。核心功能横跨六个协议表面：固定笔记、专门的投票信息流页面、[NIP-62](/zh/topics/nip-62/)（Request to Vanish）支持，用于向 relay 请求删除该 pubkey 的所有 event；客户端内的 [NIP-86](/zh/topics/nip-86/)（Relay Management API）；relay 信息页中的 [NIP-66](/zh/topics/nip-66/)（relay 发现与活跃性监控）评估；以及 [NIP-43](/zh/topics/nip-43/)（relay 访问元数据和请求）成员信息展示。

[NIP-86](/zh/topics/nip-86/) 定义了一套面向 relay 运营者的 JSON-RPC 接口，允许客户端通过标准化 API 发送封禁 pubkey、允许 pubkey、列出被封禁用户等管理命令。Amethyst 现在直接在其 relay 管理 UI 中公开了这一能力，因此运行自有 relay 的用户可以在同一个发帖客户端里完成管理操作。[PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) 还将旧的封禁与允许 pubkey 的十六进制输入对话框替换为交互式用户搜索对话框。

v1.07.2 增加了 GIF 键盘上传，并修复了一个签名回归问题：旧版 Amber 会为 `rejected` 字段返回空字符串，导致拒绝响应被误读（[PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)）。v1.07.5 则修复了图片上传崩溃。更早一点的 [v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2) 和 [v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3) 还增加了单选与多选投票的类型选择器、视频进度条拖动定位，以及匿名发帖改进。

### NIP-5A 合并，将静态网站引入 Nostr

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)（静态网站）通过 [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) 合并，定义了如何在 Nostr 密钥对之下托管静态网站。规范使用两种 event kind：kind `15128` 用于根网站，每个 pubkey 一个；kind `35128` 用于由 `d` tag 标识的命名网站。每个清单将 URL 路径映射到 SHA256 哈希，并可选使用 `server` tag 指向存放实际文件的 [Blossom](/zh/topics/blossom/) 存储主机。

托管模型是这样的：网站作者构建静态站点，将文件上传到一个或多个 Blossom 服务器，然后发布一个已签名清单 event，将路径映射到内容哈希。主机服务器接收 Web 请求，从子域中解析作者 pubkey，从作者的 [NIP-65](/zh/topics/nip-65/) relay 列表中获取清单，并通过对应哈希从 Blossom 下载 blob 后提供文件。网站仍处于作者控制之下，因为只有该密钥能签署更新后的清单。主机服务器则是可替换的，因为任何理解 NIP-5A 的服务器都能基于同一个清单提供同一个网站。

这套规范建立在已经存在的基础设施之上。由 lez 构建的 [nsite](https://github.com/lez/nsite) 参考主机实现，以及 hzrd149 的管理 UI [nsite-manager](https://github.com/hzrd149/nsite-manager)，在 NIP 合并前就已经在运行。此次合并的意义在于将 event kind 和 URL 解析规则正式化，为第二个、第三个实现提供稳定目标。

### White Noise 修复 relay 抖动并扩展客户端控制

[White Noise](https://github.com/marmot-protocol/whitenoise) 这个基于 [Marmot](/zh/topics/marmot/) 协议的私密信使，于 3 月 25 日发布了 [v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23)。主要工作是 relay 稳定性。登录流程不再等待每个 relay-list 发布完成才继续，因为 relay-list 发布现在使用 quorum 逻辑，并在后台重试剩余 relay。一次性 fetch 和 publish 现在使用作用域明确的临时 relay 会话，而不是一直挂在长生命周期连接池中；恢复后的会话在启动后也能重新找回群组刷新路径。应用还通过 [PR #495](https://github.com/marmot-protocol/whitenoise/pull/495) 和 [PR #502](https://github.com/marmot-protocol/whitenoise/pull/502) 暴露了 relay 诊断和 relay 状态检查能力。

同一版本还改变了会话行为。[PR #468](https://github.com/marmot-protocol/whitenoise/pull/468) 增加了带 `q` tag 和 `nostr:nevent` 引用的 NIP-C7 回复线程；[PR #471](https://github.com/marmot-protocol/whitenoise/pull/471) 和 [PR #512](https://github.com/marmot-protocol/whitenoise/pull/512) 让被删除消息显示为已删除占位，而不是静默消失；[PR #478](https://github.com/marmot-protocol/whitenoise/pull/478) 增加了使用 [NIP-44](/zh/topics/nip-44/) 匿名报告的应用内 bug 反馈流程；[PR #486](https://github.com/marmot-protocol/whitenoise/pull/486) 则把支持聊天直接放进客户端。同一窗口还加入了面向用户的消息控制：[PR #532](https://github.com/marmot-protocol/whitenoise/pull/532) 增加聊天归档，[PR #541](https://github.com/marmot-protocol/whitenoise/pull/541) 增加带持续时间配置的静音与取消静音，[PR #535](https://github.com/marmot-protocol/whitenoise/pull/535) 增加通知设置。[PR #539](https://github.com/marmot-protocol/whitenoise/pull/539) 则是推送注册的预备工作，在 iOS 上接入 APNs 注册，在 Android 上检测 Play Services，为后续注册逻辑做准备。后端方面，[MDK](https://github.com/marmot-protocol/mdk) 添加了 MIP-05 推送通知原语和通知请求构建器（[PR #235](https://github.com/marmot-protocol/mdk/pull/235)、[PR #238](https://github.com/marmot-protocol/mdk/pull/238)），而 [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) 增加了推送注册持久化（[PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)）、后台任务取消修复（[PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)）和启动时的 key package 恢复（[PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693)）。

### Nostr VPN 到达 v0.3.0，加入 roster 同步和 invite v2

[继上周的发布报道之后](/zh/newsletters/2026-03-25-newsletter/#nostr-vpn-作为-tailscale-替代方案启动)，[nostr-vpn](https://github.com/mmalmi/nostr-vpn) 这个通过 Nostr relay 传递信令、通过 WireGuard 建立加密隧道的点对点 VPN 继续快速发布，版本推进到了 [v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3)。这次版本升级带来了两个破坏性变化：邀请格式升级到 v2（0.3.0 仍可导入 v1 邀请，但旧版本不能导入 v2 邀请），同时信令协议中加入了管理员签名的 roster 同步。不同版本的 peer 仍可以在 mesh 层连接，但旧 peer 不会参与 roster 同步。

roster 同步意味着它开始向托管网络演化。管理员节点现在可以将成员变更推送给所有 peer，因此向 mesh 中增加或移除设备不再需要每个 peer 手工更新配置。同一周的 v0.2.x 系列仍在解决具体部署问题：[v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22) 到 [v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28) 修复了 Windows 服务管理、加入 Android 构建脚本并打磨了 LAN 配对流程。

### nospeak 作为 1.0 私密信使发布

[nospeak](https://github.com/psic4t/nospeak) 这个构建在 Nostr 上的私密信使，于 3 月 27 日发布了 [1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0)。项目支持一对一和群组会话、联系人管理以及可自托管架构。一对一聊天使用 [NIP-17](/zh/topics/nip-17/)（私密私信），该规范结合 [NIP-59](/zh/topics/nip-59/)（Gift Wrap）与 [NIP-44](/zh/topics/nip-44/)（加密载荷），从 relay 侧隐藏发送者身份。对于媒体，文件会在上传到 Blossom 服务器前通过 AES-256-GCM 在客户端侧加密。该版本还以容器镜像形式发布，便于自托管。

### Flotilla v1.7.0 增加语音房间和邮箱登录

[Flotilla](https://gitea.coracle.social/coracle/flotilla) 是 hodlbod 构建的类 Discord [NIP-29](/zh/topics/nip-29/)（基于 relay 的群组）客户端，围绕“relays as groups”模型设计。它于 3 月 30 日和 31 日发布了 [v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0) 和 [v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1)。最核心的新功能是由 mplorentz 贡献的语音房间。用户现在可以在群组频道内加入语音通话，新的加入对话框（[PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109)）允许他们选择音频输入设备，并决定是加入语音还是仅查看文本聊天。这个对话框解决了旧体验中的一个 UX 问题：此前进入启用语音的房间会强制激活麦克风，即便用户只是想读消息或检查房间设置。

同一版本还加入了邮箱密码登录作为 Nostr 密钥认证之外的替代方案、DM 的工作量证明、DM 编辑、重新设计的 relay 引导和设置、通过 `supported_nips` 检测 Blossom 支持、改进的通知徽章、Android 推送回退以及 Android 文件上传修复。v1.7.1 随后修复了离线签名器场景下 pomade 注册回退问题。

Hodlbod 还在构建 [Caravel](https://gitea.coracle.social/coracle/caravel)，这是一个 zooid relay 的托管管理器和仪表盘，本周在初始开发中记录了 40 次提交。

### Nymchat 发布基于 Marmot 的群聊

[Nymchat](https://github.com/Spl0itable/NYM)（也叫 NYM，Nostr Ynstant Messenger）是一个与 Bitchat 桥接的短暂聊天客户端。它宣布所有新的群聊现在都使用 [Marmot](/zh/topics/marmot/) 协议进行 MLS 加密消息传输。该集成使用 kind `443`、`444` 和 `445` 分别表示 key package、welcome 消息和群组消息，从而提供前向保密、被攻破后安全性以及零元数据泄露。如果接收方无法使用 MLS，Nymchat 会回退到更早的 [NIP-17](/zh/topics/nip-17/)（私密私信）群聊路径，该路径仍是端到端加密，但不具备 MLS 的 ratchet-tree 属性。

本周的 v3.55 和 v3.56 系列主要处理群聊边缘情况：新设备上的加载、离开行为、通知路由和未读徽章计数。同一轮更新还修补了由未转义 HTML 导致的 XSS 漏洞，并将关键词和短语屏蔽扩展到用户昵称。这使 Nymchat 成为又一个加入 [White Noise](#white-noise-修复-relay-抖动并扩展客户端控制) 和 [OpenChat](#openchat-v024-through-v030) 阵营的 Marmot 客户端，扩大了能够通过同一协议交换 MLS 加密群组消息的应用集合。

## 版本发布

### Calendar by Form* v1.0.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) 这个基于 [NIP-52](/zh/topics/nip-52/)（日历事件）构建的去中心化日历应用，于 3 月 29 日达到 [v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0)。新版本增加了使用加密 Nostr event（kind `32123`）和 [NIP-44](/zh/topics/nip-44/)（加密载荷）自加密的私有日历列表，使用户能够将事件组织成私有集合，而不向 relay 暴露这种分组关系。同一版本还加入了 ICS intent 处理，用于从其他应用导入日历数据，以及用于用户之间共享事件的邀请请求。

### Amber v5.0.2 through v5.0.4

[Amber](https://github.com/greenart7c3/Amber) 这个 [NIP-55](/zh/topics/nip-55/)（Android 签名器应用）签名器发布了三个小版本：[v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2)、[v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3) 和 [v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4)。其中最直观的新功能是助记词恢复短语登录（[PR #358](https://github.com/greenart7c3/Amber/pull/358)），让用户能通过 BIP39 助记词恢复签名器，而不必直接输入原始 nsec 或 ncryptsec 字符串。[PR #357](https://github.com/greenart7c3/Amber/pull/357) 增加了 [NIP-42](/zh/topics/nip-42/) relay auth 白名单，使用户能够限制哪些 relay 可以请求客户端认证。[PR #353](https://github.com/greenart7c3/Amber/pull/353) 增加了解密权限的加密范围选择，让用户可以只授予 NIP-04 或只授予 NIP-44 解密访问，而不是给出笼统授权。v5.0.4 还修复了拒绝操作未能遵守加密与解密权限范围的问题，并改善了同时接收多个 bunker 请求时的性能。

### Aegis v0.4.0

[Aegis](https://github.com/ZharlieW/Aegis) 这个跨平台签名器于 3 月 26 日发布了 [v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0)。新版本在设置中加入 Full 和 Selective 两种授权模式，并修复了多个二维码扫描问题。后续提交 [d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b)、[3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7)、[3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f) 和 [e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e) 延续了这一方向，增加了批量选择控制、可复用的批量选择统计、set-all-groups 选择 API，以及权限页面上的按权限使用统计。

### Schemata v0.2.7 through v0.3.0

[Schemata](https://github.com/nostrability/schemata) 是用于验证 Nostr event kind 的 JSON Schema 定义，它在 [v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7) 到 [v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0) 之间发布了四个版本，并合并了 21 个 PR。v0.3.0 带来了 relay URL、hex ID、MIME 类型和 BOLT-11 字符串的模式一致性修复（[PR #126](https://github.com/nostrability/schemata/pull/126)）、集中化 relay URL 模式（[PR #117](https://github.com/nostrability/schemata/pull/117)）、[NIP-19](/zh/topics/nip-19/) bech32 基础类型 schema（[PR #118](https://github.com/nostrability/schemata/pull/118)），以及对 kind 777 spell event 的验证（[PR #125](https://github.com/nostrability/schemata/pull/125)）。发布管道现在会在每次发布时向 Nostr 发布一条 kind `1` 笔记（[PR #120](https://github.com/nostrability/schemata/pull/120)），让项目通过其所验证的协议来宣布自己。除了规范的 JS/TS 包之外，Schemata 现在还支持十多种语言：Rust、Go、Python、Kotlin、Java、Swift、Dart、PHP、C#/.NET、C++、Ruby 和 C。

与 Schemata 同时，团队还发布了实验性代码生成器 [schemata-codegen](https://github.com/nostrability/schemata-codegen)，它用不同方法解决同一个验证问题。Schemata 的验证包需要 JSON Schema runtime 依赖，而 schemata-codegen 则直接将 schema 移植为类型化的本地语言构件（类型化 tag tuple、kind interface 和 runtime validator），从而不需要在运行时依赖验证器库。[codegen-vs-validators comparison](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md) 解释了两种方式各自适合的场景。

### BigBrotr v6.5.0 through v6.5.4

[BigBrotr](https://github.com/BigBrotr/bigbrotr) 这个 relay 分析平台在 [v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0) 到 [v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4) 之间发布了五个版本。v6.5.0 通过 `parse_relay_url()` 工厂函数集中处理 relay URL 验证，并加入 URL 长度检查和路径净化。监控基础设施也得到了修复：公告 event 现在包含 geohash 位置 tag（参考 [NIP-52](/zh/topics/nip-52/)），而原本没有截止时间、可能无限挂起的 Geo/Net [NIP-66](/zh/topics/nip-66/) 元数据测试也加入了超时保护。[PR #410](https://github.com/BigBrotr/bigbrotr/pull/410) 将 PostgreSQL 从 16 升级到 18，为 relay 分析管道带来了 async I/O 子系统和更好的 WAL 吞吐量。

### Vertex Lab relay 增加 NIP-50 个人资料搜索

[Vertex Lab](https://vertexlab.io) 团队也是 [npub.world](https://github.com/vertex-lab/npub.world) 和 [Vertex](https://vertexlab.io/docs) Web of Trust 引擎的维护者，他们宣布 `wss://relay.vertexlab.io` 现在支持用于个人资料查询的 [NIP-50](/zh/topics/nip-50/)（搜索）。NIP-50 为标准 Nostr `REQ` 过滤器增加了 `search` 字段，使客户端能够向支持索引的 relay 发送全文搜索查询。对于已经提供 Web of Trust 数据的 relay 来说，增加个人资料搜索意味着连接到 `relay.vertexlab.io` 的客户端可以直接按名称或简介发现用户，而无需单独的搜索服务。

### Hashtree v0.2.17 and v0.2.18 发布 WebRTC mesh 和 Iris Desktop

[Hashtree](https://github.com/mmalmi/hashtree) 是 mmalmi 的内容寻址 blob 存储系统，会在 Nostr 上发布 Merkle 根。它在 3 月 31 日发布了 [v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17) 和 [v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18)。这两个版本总结了一轮 30 次提交的冲刺，加入了三类能力。第一，`hashtree-webrtc` crate（在 v0.2.18 中重命名为 `hashtree-network`）增加了基于 WebRTC 的点对点 blob 分发，并在 Rust CLI、仿真 harness 和 TypeScript 客户端之间统一 mesh 信令。第二，发布管道现在构建 Windows 工件（CLI zip 和 Iris 安装器），使其覆盖 macOS、Linux 和 Windows。第三，这两个版本都打包了 Iris Desktop 0.1.0，也就是 mmalmi 的 Nostr 社交客户端，作为 AppImage、.deb 和 Windows 安装器资源与 hashtree CLI 一同发布。[Hashtree 首次在周刊 #10 中报道](/zh/newsletters/2026-02-18-newsletter/)，当时它作为兼容 [Blossom](/zh/topics/blossom/) 的基于文件系统的存储启动。WebRTC 层是它迈向无需依赖中心化 Blossom 服务器的点对点内容分发的第一步。

### Nostr Mail Client v0.7.0 through v0.7.2

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client) 是一个基于 Nostr 身份构建、采用 Flutter 的类邮件客户端，它在三天内发布了 [v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0)、[v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1) 和 [v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2)。可见的产品工作主要集中在引导流程（[PR #9](https://github.com/nogringo/nostr-mail-client/pull/9)）和个人资料编辑（[PR #10](https://github.com/nogringo/nostr-mail-client/pull/10)）上，这是任何试图把 Nostr 呈现为邮箱形态的客户端都需要的基础模块。后续小版本则把这部分工作打包进新的 Android 和 Linux 构建中。

### Wisp v0.14.0 through v0.16.1

[Wisp](https://github.com/barrydeen/wisp) 这个 Android Nostr 客户端本周又额外发布了 13 个版本，从 [v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta) 到 [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta)。本周工作包括 NIP-17 rumor JSON 修复（[PR #385](https://github.com/barrydeen/wisp/pull/385)）、画廊卡片上的转发徽章（[PR #383](https://github.com/barrydeen/wisp/pull/383)）、可展开的反应详情（[PR #382](https://github.com/barrydeen/wisp/pull/382)）、持久化 emoji 集（[PR #381](https://github.com/barrydeen/wisp/pull/381)）和视频自动播放控制（[PR #380](https://github.com/barrydeen/wisp/pull/380)）。最新的 [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta) 还修复了带连字符的自定义 emoji 短代码和缺失的 emoji tag。

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app) 于 3 月 24 日发布了 [3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17)。[PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000) 将 WalletException 类型映射为 NWC 响应中的错误码，使 [NIP-47](/zh/topics/nip-47/) 客户端获得结构化失败信息，而不再只是通用错误。[PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995) 修复了投票中的 zap 投票被显示为 Top Zaps 的问题，[PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998) 则在未配置钱包时隐藏余额和操作按钮。

### OpenChat v0.2.4 through v0.3.0

[OpenChat](https://github.com/DavidGershony/openChat) 这个基于 [Marmot](/zh/topics/marmot/) 栈的 Avalonia 聊天客户端，在四天内从 [v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4) 发布到 [v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0)。提交记录显示的是一个客户端如何补齐“能跑通 Marmot”和“人们可以日常使用”之间的差距。[NIP-42](/zh/topics/nip-42/) relay 认证落地，随后是带重复 event 过滤的 relay 选择器 UI。语音消息加入暂停、恢复、跳转和时长显示。签名器路径也被加固：Amber 连接通过更新的 [NIP-46](/zh/topics/nip-46/) URI 格式得到修复，请求发送前 WebSocket 会自动重连，而重复的 Amber 请求现在会通过检查重放响应被捕获。存储方面，Linux 和 macOS 获得了使用文件后备密钥的 AES-256-GCM 安全存储，用户元数据获取则开始使用 [NIP-65](/zh/topics/nip-65/) relay 发现，并将结果缓存到本地数据库。

### Igloo Signer 1.1

[Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype) 是来自 FROSTR 项目的 iOS [FROST](/zh/topics/frost/) 阈值签名器，它于 3 月 28 日发布了 [v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1)。FROST（Flexible Round-Optimized Schnorr Threshold）签名允许一组签名者共同控制一个 Nostr 密钥对，只要 t-of-n 参与者满足条件，就能联合签署 event，而不需要任何单方持有完整私钥。Igloo 是 Nostr 领域最早的移动端实现之一。

### nak v0.19.3 and v0.19.4

[nak](https://github.com/fiatjaf/nak) 这个 fiatjaf 的命令行 Nostr 工具包于 3 月 26 日和 30 日发布了 [v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3) 和 [v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4)。这两个版本都修复了 panic 条件：[PR #118](https://github.com/fiatjaf/nak/pull/118) 用 `strings.Cut` 替换 `strings.Split`，以防止潜在的越界访问；[PR #119](https://github.com/fiatjaf/nak/pull/119) 则在 curl flag 解析中防止了同类 panic。

### Flora v0.3.0

[Flora](https://github.com/shawnyeager/flora-extension) 是一个在 Nostr 上实现去中心化屏幕录制和分享的 Chrome 扩展，它发布了 [v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0)。新版本增加了公开、未列出和私密三种模式的加密视频分享。私密录制会通过 AES-256-GCM 加密，并通过 [NIP-17](/zh/topics/nip-17/)（私密私信）发送给接收者，因此录制内容不会以明文接触任何服务器。

### YakiHonne Mobile 2.0.3

[YakiHonne](https://github.com/YakiHonne/mobile-app) 这个移动端 Nostr 客户端发布了 [2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3)，加入了 relay 评论和加入请求、扩展的嵌套回复、笔记自动翻译以及 NWC 多 relay 支持。

## 项目更新

### Zap Cooking 添加 zap 投票和 Branta 支付验证

[Zap Cooking](https://github.com/zapcooking/frontend) 这个食谱与内容平台本周合并了 11 个 PR，重点放在互动内容和支付流程。[PR #277](https://github.com/zapcooking/frontend/pull/277) 增加了 zap 投票（kind 6969），用户通过发送 sats 投票，并可以查看带头像的投票者列表。[PR #274](https://github.com/zapcooking/frontend/pull/274) 则重新设计了投票 UX，使投票界面在信息流中更加自然。

[PR #276](https://github.com/zapcooking/frontend/pull/276) 还在 Send Payment 流程中加入基于摄像头的二维码扫描，并集成了 [Branta](https://branta.pro/)，这是一个在支付前验证目标是否合法的服务。Branta 会在发送前检查支付目标是否存在钓鱼、地址替换和中间人拦截风险。在 Zap Cooking 的实现中，Branta 验证过的平台名称和 logo 会直接显示在支付流程里，而启用 Branta 的二维码还可以携带 `branta_id` 和 `branta_secret` 参数，让钱包在扫码时就完成目标验证。

### diVine 为统一搜索铺路并加固视频交付

[diVine](https://github.com/divinevideo/divine-mobile) 这个短视频客户端本周继续收紧搜索、信息流导航、播放恢复和上传行为。[PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540) 为统一搜索页打下基础，提供 Videos、People 和 Tags 三个分组区域。[PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623) 将个人资料信息流、收件箱、通知、发现列表、经典 vines 以及可组合网格信息流统一迁移到共享分页控制器上，强化了各处的分页一致性。

视频交付方面也有几项具体修复。[PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643) 会按顺序重试 Divine 托管的衍生资源，并在报告播放错误前回退到原始 blob，从而避免单个资源源的瞬时失败直接杀死播放。[PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634) 则在能力探测短暂失败时，让可恢复上传继续走 Divine 自有路径，减少短时网络故障导致的上传中断。[PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637) 还调整了敏感内容门控逻辑，使视频只在真正的警告标签场景下被强制拦截，而不是仅因为创作者提供了内容警告标签。

### Shopstr 添加自定义店面，Milk Market 持续推进市场功能

[Shopstr](https://github.com/shopstr-eng/shopstr) 这个基于 Nostr 的市场，合并了 [PR #245](https://github.com/shopstr-eng/shopstr/pull/245) 来支持自定义店面，使卖家拥有更独特的主页界面，而不必让每个列表都套在同一种通用展示之中。

[Milk Market](https://github.com/shopstr-eng/milk-market) 是一个专门卖牛奶的市场，它继续推进店面优化（[PR #18](https://github.com/shopstr-eng/milk-market/pull/18)）、账户恢复（[PR #17](https://github.com/shopstr-eng/milk-market/pull/17)）、牛肉分润（[PR #15](https://github.com/shopstr-eng/milk-market/pull/15)）以及 MCP 工具类型修复（[PR #16](https://github.com/shopstr-eng/milk-market/pull/16)）。

### Notedeck 添加音效，并将其更新器路径延伸到 Android

[Notedeck](https://github.com/damus-io/notedeck) 这个来自 Damus 团队的桌面客户端，合并了 [PR #1412](https://github.com/damus-io/notedeck/pull/1412)，加入使用 rodio 的 UI 交互音效子系统；也合并了 [PR #1399](https://github.com/damus-io/notedeck/pull/1399)，其中包含 Agentium 更新，如 CLI 标题标志和可折叠会话文件夹。一个开放中的 [PR #1417](https://github.com/damus-io/notedeck/pull/1417) 提议在 Android 上通过 Nostr/Zapstore 完成 APK 自更新，它建立在 [周刊 #14 中报道的 Notedeck Nostr 原生更新器工作](/zh/newsletters/2026-03-18-newsletter/#notedeck-将版本发现迁移到-nostr) 之上。

### Nostria 添加 repost relay hint 和 NIP-98 对齐

[Nostria](https://github.com/nostria-app/nostria) 合并了 [PR #583](https://github.com/nostria-app/nostria/pull/583)，为 kind 6 和 kind 16 的 repost `e` tag 增加 [NIP-18](/zh/topics/nip-18/)（转发）relay hint；合并了 [PR #582](https://github.com/nostria-app/nostria/pull/582)，让 Brainstorm HTTP auth（kind 27235）与 [NIP-98](/zh/topics/nip-98/)（HTTP Auth）所要求的 tag 对齐；还合并了 [PR #576](https://github.com/nostria-app/nostria/pull/576)，加入 Schemata schema 验证测试。NIP-98 这项变更意味着 Nostria 现在可以使用和其他客户端一致的 HTTP auth 格式对外部服务进行认证。

### Nostr-Doc 添加桌面打包和 offline-first 工作

[Nostr-Doc](https://github.com/formstr-hq/nostr-docs) 是 Form* 的协作编辑器，本周在打包和编辑器工作上都很活跃。[commit fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4) 增加了桌面应用，[commit 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927) 开始推进原生应用工作，[commit 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869) 则推动应用向 offline-first 行为靠拢。编辑器侧，[commit 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786) 增加了 Ctrl+S 保存、保存警告、链接预览修复和修正后的删除线渲染。

### rust-nostr 优化 NIP-21 解析并增加 relay 侧 NIP-62 支持

[rust-nostr](https://github.com/rust-nostr/nostr) 本周合并了八个 PR。其中最值得注意的是 [PR #1308](https://github.com/rust-nostr/nostr/pull/1308)，它通过让 `PublicKey::parse` 的 [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) URI 解析与标准 bech32 解析性能对齐来完成优化。此前 NIP-21 URI 的解析大约比原始 bech32 密钥慢两倍。项目中还存在四个开放 PR，为内存、LMDB、SQLite 和数据库测试后端增加 relay 侧的 [NIP-62](/zh/topics/nip-62/)（Request to Vanish）支持（[PR #1315](https://github.com/rust-nostr/nostr/pull/1315)、[PR #1316](https://github.com/rust-nostr/nostr/pull/1316)、[PR #1317](https://github.com/rust-nostr/nostr/pull/1317)、[PR #1318](https://github.com/rust-nostr/nostr/pull/1318)）。

### nostr-tools 增加 bunker relay 控制并修复 NIP-47 多 relay 解析

[nostr-tools](https://github.com/nbd-wtf/nostr-tools) 合并了 [PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530)，为 BunkerSignerParams 增加 `skipSwitchRelays` 以支持手动 relay 管理；同时还合并了 [PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529)，修复 [NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）连接字符串解析，使其支持规范允许的多 relay 场景。

### Nostrability 集成 Sherlock 审计数据并发布 Schemata 概览

[Nostrability](https://github.com/nostrability/nostrability) 这个 Nostr 客户端互操作追踪器本周合并了 14 个 PR。[PR #306](https://github.com/nostrability/nostrability/pull/306) 将 Sherlock 扫描统计整合进仪表盘。Sherlock 是 Nostrability 的自动审计工具，它连接到 Nostr 客户端，捕获其发布的 event，并用 Schemata 的 JSON Schema 定义验证每个 event 是否符合规范，以检测规范违规。仪表盘现在会展示按客户端划分的 schema 失败率（[PR #315](https://github.com/nostrability/nostrability/pull/315)），让开发者看到自己的客户端在哪些 event kind 上出错。[PR #323](https://github.com/nostrability/nostrability/pull/323) 还重构了 Nostr 发布工作流，让版本公告作为单独作业运行，不会被前面的 CI 步骤取消。

elsat 还在 3 月 30 日发布了 [Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww)，解释 schemata、schemata-codegen 和 Sherlock 之间的关系，并给出当前覆盖数字：涵盖 65 个 NIP 的 179 个 event kind schema、154 个 tag schema、13 条协议消息以及 310 个示例 event。

### Nalgorithm 添加摘要生成和本地评分缓存

[Nalgorithm](https://github.com/jooray/nalgorithm) 是一个新的相关性排序 Nostr 信息流项目，本周开始公开开发。[commit cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43) 搭建了初始 Web 应用，它从关注列表中抓取帖子，并根据用户定义的偏好提示对其评分。[commit 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86) 加入了一个 CLI 摘要工具，可以把高排名帖子转换为口语化摘要，[commit 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153) 则加入了基于文件的分数缓存和基于近期点赞的增量式学习提示演化。[commit c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03) 还停止缓存失败批次的回退分数，以避免短暂评分失败永久压平帖子的排序。

### TENEX 添加 RAG 向量存储和定向 MCP 启动

[TENEX](https://github.com/tenex-chat/tenex) 是一个 Nostr 原生代理框架，通过 Telegram 将 AI 代理桥接到 Nostr 频道。本周它合并了七个 PR。[PR #101](https://github.com/tenex-chat/tenex/pull/101) 增加了可插拔的向量存储抽象，支持 SQLite-vec、LanceDB 和 Qdrant 后端，使代理在不锁定单一向量数据库的情况下获得检索增强生成。[PR #102](https://github.com/tenex-chat/tenex/pull/102) 让 MCP 启动变得定向化：只有代理实际使用到工具的 MCP 服务器才会被启动，而不是第一次执行就抢先拉起所有服务器。[PR #100](https://github.com/tenex-chat/tenex/pull/100) 加入了 `send_message` 工具，使带有 Telegram 频道绑定的代理能够主动推送消息，而不仅仅是响应入站消息。[PR #106](https://github.com/tenex-chat/tenex/pull/106) 则通过直接读取 `.git/HEAD` 而不是运行 `git branch`，避免了一个会触发 9GB Bun/JSC 内存预分配的子进程启动。

### Dart NDK 迁移 Amber signer，并加入 Alby Go 一键连接

[Dart NDK](https://github.com/relaystr/ndk) 这个 Flutter Nostr development kit 本周合并了 11 个 PR。[PR #525](https://github.com/relaystr/ndk/pull/525) 将 Amber signer 支持迁移到 ndk_flutter 包中，[PR #552](https://github.com/relaystr/ndk/pull/552) 则在示例应用中加入了 Alby Go 一键钱包连接。[PR #502](https://github.com/relaystr/ndk/pull/502) 为 CLI 增加了 install.sh 脚本，[PR #523](https://github.com/relaystr/ndk/pull/523) 则移除了 Rust verifier 依赖，改为使用原生 asset 处理。

## Protocol and Spec Work

### Marmot 将 KeyPackages 迁移到可寻址事件，并收紧推送通知格式

[Marmot 规范](https://github.com/marmot-protocol/marmot) 本周合并了四个 PR，改变了协议处理密钥材料和群组成员关系的方式。[PR #54](https://github.com/marmot-protocol/marmot/pull/54) 将 KeyPackage event 从普通 `kind:443` 迁移到带有 `d` tag 的可寻址 `kind:30443`，从而消除了密钥轮换期间依赖 [NIP-09](/zh/topics/nip-09/) 事件删除的需要。可寻址事件会原地覆盖，使轮换成为自包含流程。[PR #57](https://github.com/marmot-protocol/marmot/pull/57) 允许非管理员用户提交 SelfRemove 提案（主动退出群组），[PR #62](https://github.com/marmot-protocol/marmot/pull/62) 则要求管理员在使用 SelfRemove 之前先放弃管理员身份，避免管理员在仍持有提升权限的情况下直接消失。

[PR #61](https://github.com/marmot-protocol/marmot/pull/61) 还收紧了 [MIP-05](/zh/topics/mip-05/) 推送通知格式，明确了单 blob base64 编码、版本、token wire format 以及 x-only key 的使用方式。其结果是，在规范、客户端库和应用后端之间，token blob 与 x-only key 现在拥有一套明确定义的 wire 表示。本周这些规范变更的实现已经落地到 White Noise 栈中，并在上文的 [White Noise v2026.3.23 部分](#white-noise-修复-relay-抖动并扩展客户端控制)中介绍。

### NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)：静态网站**（[PR #1538](https://github.com/nostr-protocol/nips/pull/1538)）：定义 kind `15128`（根网站）和 kind `35128`（命名网站）清单 event，用于在 Nostr 密钥对下基于 Blossom 存储托管静态网站。详见[下方深度解析](#nip-深度解析nip-5a静态网站)。

- **[NIP-30](/zh/topics/nip-30/)（自定义表情）：允许短代码中使用连字符**（[PR #2297](https://github.com/nostr-protocol/nips/pull/2297)）：更新短代码描述，将连字符纳入允许范围。带连字符的短代码自该 NIP 引入以来就已在实践中使用，因此规范现在只是将现有实践正式记录下来。

**开放 PR 和讨论：**

- **NIP-C1：Agent TUI Messages**（[PR #2295](https://github.com/nostr-protocol/nips/pull/2295)）：提出一种结构化消息格式，使代理能够通过加密 DM 发送带交互 UI 元素的内容，包括类型化的 `text`、`buttons`、`card` 和 `table` 载荷。草案将一切放在现有 [NIP-17](/zh/topics/nip-17/) 和 [NIP-04](/zh/topics/nip-04/) 私信内容中的 JSON 里，不定义新的 event kind，并为按钮响应采用简单的回调字符串格式。

- **NIP-95：混合式点对点 relay 协议**（[PR #2293](https://github.com/nostr-protocol/nips/pull/2293)）：提出一种混合 relay 模型，其中 relay 仍然是权威节点，但也可以协调通过 WebRTC 在 peer 间分发近期 event。草案引入了 `PEER_REGISTER`、`PEER_REQUEST` 和 `PEER_OFFER` 等 relay 消息，由稳定客户端担任 Super Peer，relay 作为种子节点和回退节点。

- **NIP-B9：Zap Poll Events**（[PR #2284](https://github.com/nostr-protocol/nips/pull/2284)）：在 [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md)（投票）覆盖免费投票之后，重新开启旧的 NIP-69 zap 投票思路。草案使用 kind `6969` 定义投票，用 kind `9734` 的 zap 作为投票，从而形成带经济型 Sybil 抵抗的付费投票系统，与免费的一钥一票模型互补。

- **NIP-AD：Super Zap**（[PR #2289](https://github.com/nostr-protocol/nips/pull/2289)）：提出一种约定，将发送给 relay pubkey 或客户端 pubkey 的 zap 显示为特殊的推广笔记，本质上将 zap receipt 变成广告位。relay 运营者和客户端会发布带 `lud16` 的资料，抓取这些 receipt，提取 zap 描述中的嵌入内容，并可选设置最低 sats 阈值以抑制垃圾信息。

- **NIP-XX：代理信誉证明**（[PR #2285](https://github.com/nostr-protocol/nips/pull/2285)）：提议 kind `30085` 作为参数化可替换 event，用于记录关于 Nostr 代理的结构化信誉证明。草案通过让信誉依赖观察者来避免单一全局分数，引入时间衰减使旧证明逐渐失效，支持带证据要求的负面评价，并草拟了简单加权评分和图多样性评分两种方式，以提高 Sybil 抵抗能力。

- **NIP-XX：付费 API 服务公告**（[PR #2291](https://github.com/nostr-protocol/nips/pull/2291)）：提议 kind `31402` 可寻址 event，用于广告式发布付费 HTTP API，由 Nostr 负责发现，由 HTTP 402 负责支付处理。草案采用 tags-first 设计，使 relay 无需解析 JSON 内容就能按支付方式、价格和能力过滤，同时允许可选的请求和响应 schema，以便客户端或代理自动生成调用。

- **NIP-XX：通过 SplitSig 从 LNURL-auth 推导密钥**（[PR #2294](https://github.com/nostr-protocol/nips/pull/2294)）：提议从 LNURL-auth 的 ECDSA 签名与客户端随机 nonce 联合推导 Nostr 密钥对，公式为 `nsec = SHA256(ecdsa_signature || nonce)`。服务器看得到 ECDSA 签名（这是 LNURL-auth 握手天然的一部分），但看不到 nonce；浏览器生成 nonce，但无法控制签名。单独任一部分都无法导出 nsec。其目标是让同一个 Lightning 钱包在不同设备上生成同一个 Nostr 密钥，并以钱包作为恢复锚点，而任何服务器都无法重建该私钥。

- **[NIP-55](/zh/topics/nip-55/)：记录 rejected 字段**（[PR #2290](https://github.com/nostr-protocol/nips/pull/2290)）：把 intent 式签名器响应中的 `rejected` 字段正式写入文档，也就是 [Amethyst v1.07.x 修复](#amethyst-发布固定笔记relay-管理和-request-to-vanish) 所绕开的那种行为。

## NIP 深度解析：NIP-5A（静态网站）

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) 定义了如何在 Nostr 密钥对之下托管静态网站，使用两种 event kind 和现有 blob 存储基础设施，将已签名 event 变成可访问的 Web 页面。其[规范](https://github.com/nostr-protocol/nips/blob/master/5A.md) 于 3 月 25 日通过 [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) 合并。

这个模型使用 kind `15128` 表示根网站，每个 pubkey 一个；使用 kind `35128` 表示由 `d` tag 标识的命名网站。每个清单将绝对 URL 路径映射到 SHA256 哈希。下面是一个根网站清单示例：

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

提供服务的流程分三步。主机服务器收到 HTTP 请求，从子域中提取作者 pubkey（根网站使用 npub 作为子域，命名网站则使用 raw pubkey 的 base36 编码），通过 [NIP-65](/zh/topics/nip-65/) 获取作者的 relay 列表，并查询网站清单。找到清单后，服务器将请求路径解析为内容哈希，从 `server` tag 中列出的 Blossom 服务器下载对应 blob，然后返回给请求者。

DNS 子域格式有严格约束。根网站直接使用标准 npub 作为子域。命名网站使用原始 pubkey 的 50 字符 base36 编码，后面拼接 `d` tag 值，并全部放入单个 DNS label 中。由于 DNS label 最多 63 个字符，而 base36 编码固定占 50 个字符，所以 `d` tag 最长只能是 13 个字符。规范还要求 `d` tag 必须匹配 `^[a-z0-9-]{1,13}$` 且不能以连字符结尾，以避免 DNS 解析歧义。

使用内容哈希意味着同一个网站可以由不同主机服务器提供，而文件完整性也能在不信任服务器的情况下被验证。主机服务器不需要自己存储任何文件，只需按需根据清单中的哈希从 Blossom 获取文件。这意味着作者控制内容，Blossom 服务器存储原始文件，而主机服务器只是连接两者。这三者都可以被独立替换。

现有实现包括 [nsite](https://github.com/lez/nsite)，这是一个负责解析清单并提供文件的主机服务器；以及 [nsite-manager](https://github.com/hzrd149/nsite-manager)，这是一个用于构建和发布清单的 UI。规范还增加了 `source` tag，用于链接网站的源代码仓库，而在 [PR #2286](https://github.com/nostr-protocol/nips/pull/2286) 中单独合并的 README 更新则把 kind `15128` 和 `35128` 都登记进了 NIP kind 索引。

## NIP 深度解析：NIP-62（Request to Vanish）

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md) 将 kind `62` 定义为要求 relay 删除该请求 pubkey 所有 event 的请求。[规范](https://github.com/nostr-protocol/nips/blob/master/62.md) 的动机带有法律色彩：在存在被遗忘权法律的司法辖区，标准化、可验证签名的删除请求能给 relay 运营者一个明确的行动信号。

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

该规范区分定向 vanish 请求和全局 vanish 请求。定向请求会带具体的 `relay` tag，标明哪些 relay 应执行删除。全局请求则把 `relay` tag 的值写成字面量 `ALL_RELAYS`，请求任何看到该 event 的 relay 删除这个 pubkey 的所有 event。选择遵从的 relay 还必须确保这些已删除 event 不会再次被广播回该 relay，也就是让删除具有粘性。

NIP-62 在范围和意图上都超越了 [NIP-09](/zh/topics/nip-09/)（事件删除）。NIP-09 允许你删除单个 event，而 relay 可以选择是否遵从。NIP-62 请求删除一切，而规范要求只要 relay URL 被 tag 出来，该 relay 就必须遵从。它还要求 relay 删除对请求方 pubkey 带有 p-tag 的 [NIP-59](/zh/topics/nip-59/)（Gift Wrap）event，这意味着收到的私信也会和用户自己的 event 一起清理掉。对一个 NIP-62 vanish 请求再发布 NIP-09 删除没有任何效果：一旦 vanish，就不能通过删除 vanish 请求来“取消 vanish”。

本周，[Amethyst v1.07.0](#amethyst-发布固定笔记relay-管理和-request-to-vanish) 已经发布了客户端侧的 NIP-62 支持，让用户可以在应用里发起 vanish 请求。在 relay 侧，[rust-nostr](https://github.com/rust-nostr/nostr) 有四个开放 PR，分别为内存、LMDB、SQLite 和数据库测试后端增加 NIP-62 支持（[PR #1315](https://github.com/rust-nostr/nostr/pull/1315)、[PR #1316](https://github.com/rust-nostr/nostr/pull/1316)、[PR #1317](https://github.com/rust-nostr/nostr/pull/1317)、[PR #1318](https://github.com/rust-nostr/nostr/pull/1318)）。这让客户端支持和 relay 支持在同一周内形成呼应。

这项协议设计带来一个现实张力。Nostr 的价值主张之一是抗审查，即 relay 不应阻止内容发布。而 NIP-62 引入了一种情况：relay 必须阻止某个特定 pubkey 的内容再次发布。这两种属性之所以能共存，是因为该请求是自我定向的：你要求删除的是你自己的 event，而不是别人的。除非用户明确选择退出，否则抗审查特性对其他所有人仍然完整保留。

---

本周就到这里。正在构建什么，或者有新闻想分享？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 [NIP-17](/zh/topics/nip-17/)（私密私信）联系我们</a>，或者直接在 Nostr 上找到我们。
