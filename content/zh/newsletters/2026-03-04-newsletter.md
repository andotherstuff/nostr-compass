---
title: 'Nostr Compass #12'
date: 2026-03-04
translationOf: /en/newsletters/2026-03-04-newsletter.md
translationDate: 2026-03-04
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Marmot Development Kit](https://github.com/marmot-protocol/mdk) 发布[首个公开版本](#marmot-development-kit-发布首个公开版本)，支持加密媒体和多语言绑定。[Nostrability](https://github.com/nostrability/outbox) 发布[outbox 模型基准测试](#outbox-模型深度剖析)，涵盖 14 种 relay 选择算法。[Wisp](https://github.com/barrydeen/wisp) 在八天内从[首个 alpha 进入 beta](#wisp-从-alpha-快速迈入-beta)，支持 Tor 和 [NIP-55](/zh/topics/nip-55/)（Android 签名器应用）签名。[NIP-91](#nip-更新)（AND 过滤器）合并。[Vector v0.3.1](#vector-v031) 实现 negentropy 同步，性能提升 15 倍。本期还包括"Nostr 五年二月回顾"专题，追溯协议从服务三个 relay 的规范重写，到 Damus App Store 爆发，再到网状网络和 AI 代理提案的发展历程。

## 新闻

### Outbox 模型深度剖析

[Nostrability](https://github.com/nostrability/outbox) 发布了一系列 outbox 模型基准测试，评估不同 relay 选择算法从去中心化 relay 网络检索 event 的效果。该项目在十天内合并了 16 个 PR 和 76 次提交，产出了迄今为止可能是最全面的 [NIP-65](/zh/topics/nip-65/)（Relay 列表元数据）实现策略实证分析。

基准测试针对五种语言的 15 个客户端和库中的真实关注列表，测试了 14 种 relay 选择算法。仅查询热门 relay 的基线方法大约能检索到 26% 的 event。贪婪集合覆盖配合 Thompson 采样可达到 80-90% 的召回率。加入基于双曲贴现和 EWMA relay 延迟跟踪的延迟感知变体后，在六个测试场景中，2 秒标记时的完整性从 62-80% 提升到 72-96%。

[NIP-66](/zh/topics/nip-66/)（Relay 监控）的死 relay 过滤效果显著。通过 [nostr.watch](https://nostr.watch) 活跃性数据预过滤 relay 候选者，移除了 40-64% 的死 relay，relay 成功率从 30% 翻倍至 75-85%。信息流加载时间下降 39%（从 10 个场景的 40 秒降至 24 秒）。EOSE 竞速模拟发现，等待 EOSE 加 200 毫秒宽限期比在第一个 relay 完成时即停止获得更好的完整性。

对于无法完全重写 relay 路由的客户端，"混合 outbox 增强"方法在现有硬编码应用 relay 之上添加按作者的 outbox 查询。这种混合方案实现了 80% 的一年 event 召回率（基线为 26%），为具有传统 relay 架构的客户端提供了迁移路径。

### ContextVM 提交 MCP NIP 并发布短暂 Gift Wrap

[ContextVM](https://contextvm.org)，连接 Nostr 与 [Model Context Protocol](https://modelcontextprotocol.io/) 的协议，本周在 [NIPs 仓库](https://github.com/nostr-protocol/nips)提交了两项提案。[PR #2246](https://github.com/nostr-protocol/nips/pull/2246) 将 CVM 形式化为使用短暂 kind 25910 event 在 Nostr 上传输 MCP JSON-RPC 消息的约定。[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) 为 [NIP-59](/zh/topics/nip-59/)（Gift Wrap）扩展了一种短暂 kind（21059），遵循 [NIP-01](/zh/topics/nip-01/)（基本协议流程）的短暂语义，允许 relay 在消息投递后丢弃包裹的消息。

短暂 gift wrap 约定作为 [CEP-19](https://docs.contextvm.org/spec/ceps/cep-19/) 在 ContextVM SDK v0.6.x 发布系列中发布。[SDK 实现](https://github.com/ContextVM/sdk)添加了一个 `GiftWrapMode` 枚举，包含三种设置：OPTIONAL（接受两种 kind 并自动检测对端能力）、EPHEMERAL（仅 kind 21059）和 PERSISTENT（仅 kind 1059）。对于 AI 工具调用，短暂模式避免在 relay 上存储中间请求-响应流量，降低存储成本和隐私暴露。

独立运营者在网络上推出了新的公共 MCP 服务器，包括一个 Wolfram Alpha 查询服务器。ContextVM 团队在 v0.6.x 发布周期中同步发布了 CEP-15（通用工具 schema）和 CEP-17（服务器 relay 列表发布）。

### Marmot Development Kit 发布首个公开版本

[MDK](https://github.com/marmot-protocol/mdk)（Marmot Development Kit），驱动 [Pika](https://github.com/sledtools/pika) 和 [White Noise](https://github.com/marmot-protocol/whitenoise) 进行 [Marmot](/zh/topics/mls/) 加密消息的 Rust 库，以 [v0.6.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.6.0) 作为首个公开版本发布。超过 200 个 PR 合并到此版本中，新增六位贡献者。

此版本包括加密媒体支持（MIP-04，使用 HKDF 种子派生的 MIP-01 v2）、确定性 commit 竞争解决（MIP-03）、加密本地存储、Marmot commit 和提案的管理员授权验证，以及用于协议可扩展性的 GREASE 支持。绑定适用于 Kotlin、Python、Ruby 和 Windows，同时支持 Android 交叉编译。该库升级至 OpenMLS 0.8.0，包含安全公告修复和在内存中清零敏感值的 `Secret<T>` 类型。

配套协议变更（[MIP-03](https://github.com/marmot-protocol/marmot/pull/48)）将 kind 445 消息的 [NIP-44](/zh/topics/nip-44/)（加密载荷）加密替换为 ChaCha20-Poly1305。NIP-44 按规范要求 UTF-8 字符串输入，使得无法通过标准 TypeScript Nostr 库传递原始 Marmot 消息字节。替代方案直接从 Marmot 导出密钥派生密钥。此破坏性变更需要在[核心规范](https://github.com/marmot-protocol/marmot/pull/48)、[MDK](https://github.com/marmot-protocol/mdk/pull/208) 和 [TypeScript SDK](https://github.com/marmot-protocol/marmot-ts/pull/54) 之间协调更新。

[marmot-ts](https://github.com/marmot-protocol/marmot-ts)，由 hzrd149 维护的 TypeScript 实现，合并了四个包含破坏性 API 变更的 PR。一次[综合更新](https://github.com/marmot-protocol/marmot-ts/pull/52)添加了用于创建/发布/轮换生命周期的密钥包管理器、`sendChatMessage` 便捷方法、无需加入即可预览邀请（`readInviteGroupInfo`）、用于前向保密轮换的自更新，以及结构化调试日志。群组解密 API 从 `readGroupMessage` 重命名为 `decryptGroupMessage`，提供更丰富的结果变体（processed/skipped/rejected/unreadable）。gzuuus 贡献了示例清理工作，添加了 NIP-65 relay 支持和符合 MIP-00 的最后手段密钥包处理。

[White Noise CLI](https://github.com/marmot-protocol/whitenoise-rs)（`wn`），驱动移动应用和新 TUI 的 Rust 后端，在十天内合并了 16 个 PR。签名器生命周期处理通过 RAII 作用域守卫获得了取消安全性（[PR #538](https://github.com/marmot-protocol/whitenoise-rs/pull/538)），修复了一类中断操作可能泄漏签名器状态的 bug。当必需的 relay 列表（kind 10002/10050/10051）缺失时，登录现在会阻塞（[PR #515](https://github.com/marmot-protocol/whitenoise-rs/pull/515)），当收件箱列表不存在时，giftwrap 订阅回退到 [NIP-65](/zh/topics/nip-65/) relay（[PR #518](https://github.com/marmot-protocol/whitenoise-rs/pull/518)）。调试模式（[PR #528](https://github.com/marmot-protocol/whitenoise-rs/pull/528)）以 JSON 输出暴露数据库查询和 MLS ratchet-tree 检查。其他修复涉及签名器重新注册后的订阅恢复、欢迎消息补发时机、relay 过滤器验证和用户搜索半径限制。

Marmot 本周在核心 Rust 技术栈之外有了显著扩展。[White Noise TUI](https://github.com/marmot-protocol/wn-tui)，White Noise 消息栈的终端界面，于 3 月 3 日发布。它将 `wn` CLI 作为子进程包装，通过 Elm 风格的单向架构渲染其 JSON 输出，提供带未读指示器的多会话导航、群组创建和成员搜索、实时消息流，以及终端中的表情回应。

[DavidGershony](https://github.com/DavidGershony) 发布了完整的 C# Marmot 技术栈，镜像 Rust 工具链的分层架构。[dotnet-mls](https://github.com/DavidGershony/dotnet-mls) 用 C# 实现 MLS RFC 9420 密码学原语。[marmot-cs](https://github.com/DavidGershony/marmot-cs) 在此基础上添加 Nostr relay 传输，相当于 MDK 的 C# 版本。[OpenChat](https://github.com/DavidGershony/openChat)，使用 .NET 9 和 Avalonia UI 构建的跨平台桌面应用，将两者整合为一个可用的聊天客户端，支持 NIP-44 私信、Marmot 群组加密、[NIP-46](/zh/topics/nip-46/)（Nostr Connect）远程签名和多 relay 状态指示器。

[MDK PWA Reference](https://github.com/zerosats/mdk-pwa-reference) 提供了一个 Progressive Web App 模板，用于构建 Marmot 加密应用，实验性地支持 AI 代理参与群聊和通过 Arkade 钱包基础设施进行 Bitcoin 支付。

### Wisp 从 Alpha 快速迈入 Beta

[Wisp](https://github.com/barrydeen/wisp) 是一个新的 Android Nostr 客户端，从 2 月 24 日的[首个 alpha](https://github.com/barrydeen/wisp/releases/tag/v0.1.0-alpha) 到 3 月 3 日的 [v0.3.4-beta](https://github.com/barrydeen/wisp/releases/tag/v0.3.4-beta)，在八天内产出 19 个版本、115 个合并 PR 和 276 次提交。

功能发展轨迹涵盖了大多数客户端需要数月才能达到的领域。v0.1.0 发布时即支持 outbox/inbox relay 模型和引导流程。到 v0.1.3，客户端已具备面向 Amber 的 [NIP-55](/zh/topics/nip-55/) intent 签名、用于 `.onion` relay 连接的内嵌 Tor SOCKS5 代理，以及 [NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）。v0.2.0 以 beta 身份推出，带有静音列表过滤和自定义表情支持，v0.2.4 添加了内容警告覆盖层。v0.3.x 系列引入了 [NIP-13](/zh/topics/nip-13/) 笔记工作量证明、带持久设置的后台 PoW 挖矿、`.onion` relay 存储和静音线程通知。

通过 Google ML Kit 实现的设备端翻译在初始模型下载后无需网络访问即可本地运行。交互式社交图谱可视化使用速度 Verlet 物理模拟，以约 30fps 运行，支持捏合缩放导航和个人资料查看。

## 版本发布

### Vector v0.3.1

[Vector](https://github.com/VectorPrivacy/Vector)，Marmot 加密消息应用，发布了 [v0.3.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.1)，包含群组管理改进和性能优化。多管理员群组、批量邀请、按 npub 邀请和群组头像扩展了协作功能。Android 后台通知现在支持内联回复和标记已读操作。

基于 [Negentropy](/zh/topics/negentropy/) 的确定性同步可检索完整会话历史，包括离线期间错过的消息。语音转文字在 Android 上通过 GPU 加速重建。文件附件处理进行了全面改造，支持下载进度、重试状态、目录压缩发送和全程实时进度指示器。启动时间、图片处理、音频播放和整体 UI 响应速度提升超过 15 倍。应用安装体积减少超过三分之一，前端减少约一半。新增 32 位 ARM Android 支持。

### Alby Hub v1.21.5

[Alby Hub](https://github.com/getAlby/hub)，支持 Nostr Wallet Connect（[NIP-47](/zh/topics/nip-47/)）的自托管 Lightning 节点，发布了 [v1.21.5](https://github.com/getAlby/hub/releases/tag/v1.21.5)。默认 NWC 配置中添加了第二个 relay，提升 relay 重启期间的可靠性。修复了交易列表中无效 zap 数据的问题，解决了格式错误的 [NIP-57](/zh/topics/nip-57/)（Lightning Zaps）event 的显示问题。应用商店新增 Alby CLI 和 LNVPS 条目。

### nospeak v0.12.x

[nospeak](https://github.com/psic4t/nospeak)，基于文本的 Nostr 消息客户端，在此期间发布了三个版本。[v0.12.0](https://github.com/psic4t/nospeak/releases/tag/v0.12.0) 添加了 PIN 应用锁（4 位键盘）和超过 15 种新语言翻译，包括孟加拉语、泰语、越南语、印地语、阿拉伯语、希伯来语、乌尔都语、土耳其语、日语、中文、韩语、荷兰语、波兰语、俄语和波斯语（含 RTL 支持）。[v0.12.1](https://github.com/psic4t/nospeak/releases/tag/v0.12.1) 引入了 Cypher 主题（纯黑背景配青色强调色），以及 Android 视频海报生成。[v0.12.2](https://github.com/psic4t/nospeak/releases/tag/v0.12.2) 在联系人菜单中添加了聊天导出和查看个人资料功能。

### Citrine v2.0.0-pre2

[Citrine](https://github.com/greenart7c3/Citrine)，greenart7c3 开发的 Android 个人 relay，发布了 [v2.0.0-pre2](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre2)，通过新数据库索引和重构的 Kotlin 协程提升 relay 性能。每个托管的 Web 应用现在在独立端口启动。全文搜索和重新设计的 event 界面（支持 event 展开）完善了此次更新。

### NoorNote v0.5.x

[NoorNote](https://github.com/77elements/noornote)，基于 Nostr 的笔记应用，从 [v0.5.0](https://github.com/77elements/noornote/releases/tag/v0.5.0) 到 [v0.5.7](https://github.com/77elements/noornote/releases/tag/v0.5.7) 发布了 8 个版本。v0.5.0 登陆 Android，添加了 [NIP-55](/zh/topics/nip-55/) Amber 签名器支持和 [NIP-71](/zh/topics/nip-71/)（视频 Event）笔记发布。v0.5.1 重新设计的欢迎页包含公共时间线预览，APK 缩减至 15 MB。v0.5.2 的 Relay 浏览器让用户通过可分享的 URL 浏览公共 relay 时间线，同时支持媒体下载和 [NIP-30](/zh/topics/nip-30/) 自定义表情回应。后续 v0.5.7 之前的版本修复了协作"部落"笔记共享系统中的同步竞争条件。

### NosCall v0.5.1

[NosCall](https://github.com/sanah9/noscall)，Nostr 语音和视频通话应用，发布了 [v0.5.1](https://github.com/sanah9/noscall/releases/tag/v0.5.1-release)，新增语音消息支持、优化的桌面体验（含群组入口）、桌面联系人收藏、联系人备注和筛选、数据导出和清理选项，以及系统字号无障碍支持。

### Shosho v0.13.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases)，Nostr 直播应用，发布了 [v0.13.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.13.0)，支持从流卡片菜单下载 MP4 回放，以及 [NIP-05](/zh/topics/nip-05/)（基于 DNS 的验证）个人资料功能。RTMP 发布器迁移至 Expo Modules API。低带宽连接下的直播性能得到改善，旧设备崩溃和 iOS 向 [Zap.Stream](https://zap.stream) 推流的问题已修复。

### nostr-java v2.0.0

[nostr-java](https://github.com/tcheeric/nostr-java) 发布了 [v2.0.0](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.0)，支持可配置的 WebSocket 缓冲区大小，允许应用处理更大的 Nostr event 而不会截断。主版本号变更反映了连接 API 的破坏性变更。

### Prism 1.1.0

[Prism](https://github.com/hardran3/Prism) 发布了 [1.1.0](https://github.com/hardran3/Prism/releases/tag/1.1.0)，支持长文内容（kind 30023 文章）和用于在应用中直接撰写的 Markdown 编辑器，随后发布了 [1.1.1](https://github.com/hardran3/Prism/releases/tag/1.1.1) bug 修复版本。

### Angor v0.2.6

[Angor](https://github.com/block-core/angor)，Bitcoin 众筹平台，发布了 [v0.2.6](https://github.com/block-core/angor/releases/tag/v0.2.6)，集成 Boltz 并提供一键投资流程。投资和基金项目类型均已在 testnet 上端到端运行。团队表示 UI 完成度约为 70%。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-91：过滤器 AND 运算符](https://github.com/nostr-protocol/nips/pull/1365)**：为 relay 订阅中的 tag 数组添加 AND 过滤语义。目前，在 tag 过滤器中指定多个值（例如多个 `p` tag）会匹配包含其中任何一个的 event。NIP-91 允许客户端要求 event 同时匹配所有指定的 tag 值，减少带宽并加速索引操作。多个 relay 实现已存在，包括 nostr-rs-relay、satellite-node、worker-relay 和 applesauce。此前编号为 NIP-119。

- **[NIP-30：emoji tag 中的表情集地址](https://github.com/nostr-protocol/nips/pull/2247)**：[NIP-30](/zh/topics/nip-30/) 中的自定义 emoji tag 现在可以包含可选的表情集地址。在客户端中点击表情可以打开其所属的表情集进行收藏或浏览。源自 [Chachi](https://github.com/purrgrammer/chachi) 客户端。

- **[NIP-29：添加 unallowpubkey 和 unbanpubkey](https://github.com/nostr-protocol/nips/pull/2111)**：为 [NIP-29](/zh/topics/nip-29/) 群组聊天新增两个管理员命令。`unallowpubkey` 从允许列表中移除 pubkey 而不封禁。`unbanpubkey` 解除封禁而不将 pubkey 重新添加到成员列表。此前，从允许列表中移除某人的唯一方式也会封禁他们，而解除封禁则需要重新将用户添加为成员。

**开放 PR 和讨论：**

- **[NIP-A7：Spells](https://github.com/nostr-protocol/nips/pull/2244)**（2 月 27 日开启）：由 purrgrammer 提出，spells 是作为 kind 777 event 发布的可移植已保存 Nostr 查询。spell 在结构化 tag 中编码 REQ 或 COUNT 过滤器（`k` 用于 kind，`authors` 用于 pubkey，`tag` 用于任意 tag 过滤），并提供运行时变量：`$me` 解析为已登录用户的 pubkey，`$contacts` 展开为用户的 kind 3 关注列表。相对时间戳（`7d`、`2w`、`1mo`）让 spell 无需硬编码日期即可定义滚动时间窗口。已在 [nak](https://github.com/fiatjaf/nak) 和 [Grimoire](https://github.com/purrgrammer/grimoire) 中实现，spell 让用户创建、分享和订阅可跨客户端的策展信息流。

- **[NIP-59：短暂 Gift Wrap（kind 21059）](https://github.com/nostr-protocol/nips/pull/2245)**（2 月 27 日开启）：为 [NIP-59](/zh/topics/nip-59/) gift wrap 添加短暂变体。Kind 21059 遵循 NIP-01 短暂语义，因此 relay 在投递后丢弃 event。由 ContextVM 为 MCP 传输提出，适用于无需消息持久化的场景。

- **[ContextVM：基于 Nostr 的 MCP JSON-RPC](https://github.com/nostr-protocol/nips/pull/2246)**（2 月 27 日开启）：指定如何使用短暂 kind 25910 event 通过 `p` 和 `e` tag 进行寻址和关联来传输 Model Context Protocol 消息。设计刻意精简，将协议细节推迟到 [ContextVM 规范](https://docs.contextvm.org)。

- **[NIP-29：音视频直播空间](https://github.com/nostr-protocol/nips/pull/2238)**（2 月 25 日开启，草案）：fiatjaf 的草案，为 [NIP-29](/zh/topics/nip-29/) 群组扩展直播音视频功能。提案在群组元数据 event 中添加可选的 `livekit` 和 `no-text` tag。当用户想加入语音空间时，客户端在 `/.well-known/nip29/livekit/{groupId}` 向 relay 请求 JWT。Relay 检查群组成员资格并颁发以用户十六进制 pubkey 作为 `sub` 声明的令牌，该令牌传递给 [LiveKit](https://livekit.io/) 用于媒体传输。语音房间访问继承群组现有的权限模型，relay 端的成员规则决定谁可以发言。正在 Pyramid 和 Chachi 中测试。

- **[协作 Event 所有权](https://github.com/nostr-protocol/nips/pull/2235)**（2 月 24 日开启）：pablof7z 提出一种指针 event（kind 39382），通过在 `p` tag 中列出共同所有者 pubkey 并在 `k` tag 中指定目标 event kind 来声明协作空间。任何列出的所有者都可以发布相同 `d` tag 的该 kind event，客户端通过查询所有所有者并取最新 event 来解析当前状态。仅当可验证的 `a` tag 反向引用指针且作者出现在其 `p` tag 中时，才显示共同作者署名，防止伪造声明。这使得共享 wiki 页面和共同编写的资源无需将控制权分配给单个密钥对。

- **[NIP-09：级联删除转发](https://github.com/nostr-protocol/nips/pull/2234)**（2 月 24 日开启）：当原作者删除笔记时，relay 也应删除引用它的 kind 6 或 kind 16 转发。动机来自隐私考虑：转发可能在作者删除源内容后保留意外泄露的信息。此变更仅在 relay 端进行，不需要客户端修改。

- **[NIP-07：peekPublicKey](https://github.com/nostr-protocol/nips/pull/2233)**（2 月 23 日开启）：为 [NIP-07](/zh/topics/nip-07/) 浏览器扩展添加 `peekPublicKey()` 方法。与 `getPublicKey()` 不同，它在不提示用户确认的情况下返回当前 pubkey，在用户启用自动登录时实现静默自动登录。

- **[NIP-BB：Book](https://github.com/nostr-protocol/nips/pull/2248)**（2 月 28 日开启，草案）：定义四种可寻址 event kind（30300-30303）用于在 Nostr 上结构化出版书籍。Cover event 保存根元数据，包括标题、封面图片、通过 [NIP-32](/zh/topics/nip-32/)（标签系统）label 指定的许可证和语言代码。Index event 使用 base62 分数索引将每章映射到其位置，使作者可以在现有章节之间插入新章节而无需重新编号。Chapter event 作为带可选图片的结构性标题，Episode event 承载实际散文（上限 30,000 字符），带有定位图片 tag。评论使用对 Cover event 的 Zap，以 Zap 描述作为评论文本。

- **[NIP-54：从 Asciidoc 切换到 Djot](https://github.com/nostr-protocol/nips/pull/2242)**（2 月 26 日开启）：继 12 月的 [d-tag 国际化修复](/en/newsletters/2025-12-31-newsletter/)之后，此 PR 提议将 [NIP-54](/zh/topics/nip-54/) wiki 的 Asciidoc 标记格式替换为 [Djot](https://djot.net/)，添加了理由说明和非拉丁文字的 wikilink 示例。

- **[NIP-66：防御措施](https://github.com/nostr-protocol/nips/pull/2240)**（2 月 26 日开启）：基于 [nostrability/outbox](#outbox-模型深度剖析) 基准测试的经验，为 [NIP-66](/zh/topics/nip-66/) 边缘情况添加明确提示。配套的 [PR #2241](https://github.com/nostr-protocol/nips/pull/2241) 定义了 SSL、地理位置、网络和连接检查的输出 tag。

- **NIP-C1：密码学身份证明**（wiki 条目，kind 30817）：提出 kind 30509 event，将 APK 签名证书与 Nostr 个人资料进行密码学关联。证明的工作方式是使用证书的私钥对包含 Nostr pubkey 的规范消息进行签名（支持 ECDSA、RSA PKCS1v15、Ed25519 及其他标准算法），然后在以 Nostr 密钥签名的 kind 30509 event 中发布签名。验证者可以确认控制应用 Android 签名证书的人也控制着声称发布该应用的 Nostr pubkey。证明默认一年后过期，可以显式撤销。已在 [Zapstore](https://github.com/zapstore/zapstore) 工具链中实现。

- **NIP-31402：SARA 收入份额发行注册**（wiki 条目，kind 30817）：定义 kind 31402 可寻址 event，用于在 Nostr relay 上发布 Simple Autonomous Revenue Agreement（SARA）发行信息。发行方公布 Lightning 结算的收入份额条款，包括池份额百分比、触发支付条件、sats 阈值、期限长度和分级定价。代理和人类可以跨 relay 发现发行信息并自主订阅，无需中心化平台。Kind 编号模仿 kind 30402（L402 服务注册，由同一作者作为配套 wiki 条目发布），因为 SARA 代表 L402 支付关系的回报端。

## 开放 PR 和项目更新

### Damus：[NIP-89](/zh/topics/nip-89/)（推荐应用处理器）

[PR #3337](https://github.com/damus-io/damus/pull/3337) 为 [Damus](https://github.com/damus-io/damus) 实现了 NIP-89 客户端 tag 支持。应用现在在所有发布路径（主应用、分享扩展、高亮标注、草稿）上添加客户端 tag，当其他应用包含其 tag 时在时间戳旁显示"via ClientName"。外观设置中的隐私开关允许用户禁用 tag 发送。[PR #3652](https://github.com/damus-io/damus/pull/3652) 在设置中添加了存储部分，通过交互式饼图展示 NostrDB 和 Kingfisher 缓存的磁盘使用情况，支持导出。

开放中：[PR #3657](https://github.com/damus-io/damus/pull/3657) 为引用笔记添加 [NIP-65](/zh/topics/nip-65/) relay 回退。当内联 `nevent` 包含作者 pubkey 但没有 relay 提示且笔记不在用户的池中时，Damus 获取作者的 kind 10002 relay 列表并从其写入 relay 重试。

### Amethyst：[NIP-39](/zh/topics/nip-39/)（外部身份）、NIP-C0、[NIP-66](/zh/topics/nip-66/)

[Amethyst](https://github.com/vitorpamplona/amethyst) 在 28 个 PR 中合并了一系列 NIP 实现。外部身份声明现在作为独立的 kind 10011 event 在 [NIP-39](/zh/topics/nip-39/) 下发布（[PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747)），将社交身份与 kind 0 元数据分离，同时保持向后兼容回退。通过 NIP-C0 支持代码片段（[PR #1744](https://github.com/vitorpamplona/amethyst/pull/1744)），添加了 kind 1337 event 以及语言、扩展名、运行时、许可证和依赖项的访问器。[NIP-66](/zh/topics/nip-66/) relay 监控实现（[PR #1742](https://github.com/vitorpamplona/amethyst/pull/1742)）涵盖了两种 event kind，完整解析 RTT 指标、网络类型、支持的 NIP 和 geohash 的 tag。

加密私信登陆 Amethyst Desktop（[PR #1710](https://github.com/vitorpamplona/amethyst/pull/1710)），采用分栏聊天布局，同时支持 [NIP-04](/zh/topics/nip-04/)（加密私信）和 [NIP-17](/zh/topics/nip-17/)（私密私信）。新的 relay 信息流界面（[PR #1733](https://github.com/vitorpamplona/amethyst/pull/1733)）让用户浏览特定 relay 的帖子，支持关注/取消关注功能。开放中：抗审查 NIP-05 验证（[PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)）为 `.bit` 标识符添加了并行验证路径，通过 Namecoin 区块链而非 HTTP DNS 进行解析。当 Amethyst 检测到 NIP-05 字段中的 `.bit` 后缀时，它查询 ElectrumX-NMC 服务器获取该名称的交易历史，从最新输出中解析 `NAME_UPDATE` 脚本以提取 Nostr pubkey，并拒绝超过 36,000 个区块（Namecoin 的到期窗口）的名称。启用 Tor 时，ElectrumX 连接通过 SOCKS5 路由，在 clearnet 和 `.onion` 端点之间动态选择服务器。一小时 TTL 的 LRU 缓存防止重复的区块链查询。

### Notedeck：Outbox 架构

[PR #1303](https://github.com/damus-io/notedeck/pull/1303) 将 [Notedeck](https://github.com/damus-io/notedeck) 从临时 relay 池管理迁移到集中式 outbox 模型，支持账户级别的订阅。Messages 模块现在在不存在默认 DM relay 列表时自动发布一个，并按 kind 10050 将私信路由到收件人的首选 relay。

### Pika：群组独立个人资料和教程信息流

[Pika](https://github.com/sledtools/pika)，支持 iOS、Android 和桌面端构建的 Marmot 加密消息应用，新增群组独立个人资料（[PR #368](https://github.com/sledtools/pika/pull/368)）。用户现在可以为每个群聊设置独立的显示名称和头像，以及自定义简介。这些个人资料作为 Marmot 群组内的加密 kind 0 event 发布，群组外任何人不可见，当未设置群组特定个人资料时回退到用户的全局 Nostr 个人资料。新成员加入时，管理员重新广播所有已存储的群组个人资料，每个成员在 commit 时重新发布自己的个人资料。个人资料图片在 Blossom 上传前经过 Marmot 媒体加密。PR 包含 16 个新单元测试，并通过 CLI 命令（`update-group-profile`）和 UI 暴露该功能。

新的 `pika-news` Web 应用（[PR #401](https://github.com/sledtools/pika/pull/401)）监控 Pika 自身的 GitHub PR，从 PR diff 中自动生成分步教程，以带有 [NIP-07](/zh/topics/nip-07/) 认证的服务端渲染页面发布。用户可以通过 Nostr 认证聊天实时讨论特定教程。

### diVine：可嵌入小组件和视频回复

[diVine](https://github.com/divinevideo/divine-mobile)，Nostr 原生视频共享平台，在十天内合并了 132 个 PR。可嵌入的 iframe 小组件（[PR #1843](https://github.com/divinevideo/divine-mobile/pull/1843)）提供独立的 `/embed?npub=...` 页面，渲染用户的个人资料和最新视频。视频回复功能（[PR #1915](https://github.com/divinevideo/divine-mobile/pull/1915)）在功能标志后面启用，使用 Kind 1111 评论（[NIP-22](/zh/topics/nip-22/)）配合 [NIP-92](/zh/topics/nip-92/)（媒体附件）imeta 元数据。受 Bluesky 启发的三级内容过滤器（[PR #1797](https://github.com/divinevideo/divine-mobile/pull/1797)）在 17 个 [NIP-32](/zh/topics/nip-32/) 内容警告类别中提供显示/警告/隐藏控制。

### strfry：REQ 过滤器验证

[PR #163](https://github.com/hoytech/strfry/pull/163) 为 [strfry](https://github.com/hoytech/strfry)（C++ Nostr relay）添加了可配置的 REQ 过滤器验证。运营者可以设置每个 REQ 的最大过滤器数、必需的 author 或 tag 存在、允许的 kind 白名单和每过滤器 kind 限制。该功能面向需要严格过滤器执行的 NWC relay 部署。开放中：[PR #173](https://github.com/hoytech/strfry/pull/173) 在摄入时为 event 载荷添加可选的 zstd 压缩。

### rust-nostr：[NIP-62](/zh/topics/nip-62/) Request to Vanish

[rust-nostr](https://github.com/rust-nostr/nostr)，Rust Nostr 协议库，在三个数据库后端中添加了 [NIP-62](/zh/topics/nip-62/)（Request to Vanish）支持：[LMDB](https://github.com/rust-nostr/nostr/pull/1268)、[SQLite](https://github.com/rust-nostr/nostr/pull/1270) 和[内存](https://github.com/rust-nostr/nostr/pull/1272)。LMDB 实现包含可配置选项，可按部署启用或禁用 [NIP-09](/zh/topics/nip-09/) 和 NIP-62 执行。

### NDK：协作 Event 和 NIP-46 超时

[NDK](https://github.com/nostr-dev-kit/ndk)，JavaScript/TypeScript 的 Nostr Development Kit，合并了 [PR #380](https://github.com/nostr-dev-kit/ndk/pull/380)，引入 `NDKCollaborativeEvent` 用于使用可寻址指针 event（kind 39382）定义授权作者的多作者协作文档。`NDKNip46Signer` 的可配置超时（[PR #381](https://github.com/nostr-dev-kit/ndk/pull/381)）防止 [NIP-46](/zh/topics/nip-46/) 远程签名操作在 bunker 无响应时无限期挂起。

### TENEX：代理分类和 Pubkey 访问控制

[TENEX](https://github.com/tenex-chat/tenex)，Nostr 原生 AI 代理编排平台，合并了两个安全相关 PR。TIP-01 基于角色的代理分类（[PR #91](https://github.com/tenex-chat/tenex/pull/91)）将代理类别（principal、orchestrator、worker、advisor、auditor）映射到通过 denied-tools 映射的自动化工具限制。前门 pubkey 访问控制（[PR #87](https://github.com/tenex-chat/tenex/pull/87)）确保只有白名单或后端签名的 pubkey 的 event 与已知代理一起路由；未知 pubkey 被静默丢弃，并使用 OpenTelemetry span 进行审计。

### Zap Cooking：会员仪表板

[Zap Cooking](https://github.com/zapcooking/frontend)，基于 Nostr 的食谱分享平台，在十天内合并了 25 个 PR 和 85 次提交。会员仪表板（[PR #228](https://github.com/zapcooking/frontend/pull/228)）显示订阅状态（含到期日期）和管理/升级选项，为 Sous Chef 和 Zappy 层级重新启用功能限制（客户端和服务端双重检查），并在 26 个文件中统一层级命名。两阶段群组消息加载（[PR #227](https://github.com/zapcooking/frontend/pull/227)）提供快速的 3 天初始获取以即时显示，随后进行 40 天后台回填。

钱包助记词存储从 pubkey 派生加密迁移到 [NIP-44](/zh/topics/nip-44/) 自加密（[PR #224](https://github.com/zapcooking/frontend/pull/224)），修复了旧方案从 `SHA-256(pubkey)` 派生密钥的漏洞。由于 pubkey 是公开的，旧方案实质上相当于未加密。现有钱包在首次加载时静默迁移。[NIP-29](/zh/topics/nip-29/) 群组聊天新增红色圆点徽章的未读指示器和基于 kind 9009 邀请码的邀请制访问（[PR #213](https://github.com/zapcooking/frontend/pull/213)）。链接预览和 Nostr event 嵌入现在在私信和群组消息中渲染（[PR #218](https://github.com/zapcooking/frontend/pull/218)）。设置中的 Nostr 备份部分（[PR #210](https://github.com/zapcooking/frontend/pull/210)）通过 [NIP-78](/zh/topics/nip-78/)（应用特定数据）加密存储和滚动 3 槽位版本管理保存关注列表和静音列表。启动性能通过延迟通知服务、基于 IntersectionObserver 的惰性 DOM 渲染（将 200 条 event 的信息流中 DOM 节点从约 15,000 个减少到约 3,000 个）和延长 outbox 缓存 TTL 得到改善（[PR #208](https://github.com/zapcooking/frontend/pull/208)）。可定制的打印食谱模态框（[PR #205](https://github.com/zapcooking/frontend/pull/205)）允许用户切换包含的部分并提供实时预览。[Branta SDK](https://github.com/BrantaOps/branta-core) 集成（[PR #222](https://github.com/zapcooking/frontend/pull/222)）为 POST 和 GET 请求添加验证防护。

### Keep：Rust 驱动的状态迁移

[Keep](https://github.com/privkeyio/keep-android)，基于 Nostr 的 Android 私钥管理器，合并了 [PR #178](https://github.com/privkeyio/keep-android/pull/178)，删除四个 Kotlin 配置存储，改为来自 keep-mobile 层的 Rust 驱动共享状态。10 秒轮询循环被来自 Rust 的基于推送的 `KeepStateCallback` 替代。[PR #179](https://github.com/privkeyio/keep-android/pull/179) 添加了带密码保护的加密备份和恢复。

### Mostro Mobile：争议聊天加密

[Mostro Mobile](https://github.com/MostroP2P/mobile)，Mostro P2P Bitcoin 交易平台的移动客户端，发布了争议聊天加密的两阶段迁移。第一步（[PR #495](https://github.com/MostroP2P/mobile/pull/495)）从 mostro 特定的包装切换到从管理员 pubkey 派生的共享密钥加密。在此基础上，[PR #501](https://github.com/MostroP2P/mobile/pull/501) 将消息模型与 `NostrEvent` 统一，并在磁盘上加密存储 gift wrap event，与点对点聊天模式一致。BIP-340 签名修复（[PR #496](https://github.com/MostroP2P/mobile/pull/496)）将 bip340 依赖覆盖为 0.2.0，解决了 `bigToBytes()` 填充 bug，该 bug 导致 1-2% 的 Schnorr 签名无效，以及公钥以 `0x00` 开头的密钥 100% 失败。订单详情现在显示可读的状态标签而非原始协议值，支持英语、西班牙语、意大利语和法语本地化（[PR #502](https://github.com/MostroP2P/mobile/pull/502)）。HalCash 被添加，SEPA 被移除作为支付方式（[PR #493](https://github.com/MostroP2P/mobile/pull/493)），因为 SEPA 转账可能超过 24 小时（SEPA Instant 保留）。

在服务端，[Mostro](https://github.com/MostroP2P/mostro) 修复了争议会话恢复以包含发起者字段（[PR #599](https://github.com/MostroP2P/mostro/pull/599)），现在在卖方释放资金时自动关闭活跃争议，发布已结算的 Nostr event 以便管理员客户端看到解决结果（[PR #606](https://github.com/MostroP2P/mostro/pull/606)）。

## Nostr 五年二月回顾

[上月的周刊](/zh/newsletters/2026-01-28-newsletter/#nostr-五年一月回顾)追溯了 Nostr 从早期开发到 Damus 爆发再到 2026 年安全基础设施的一月里程碑。本次回顾涵盖 2021 年至 2026 年每个二月发生的事件。

### 2021 年 2 月：重写

Nostr 诞生三个月后，2 月产出了协议最具影响力的早期变更。2 月 14-15 日，fiatjaf [重写了 NIP-01](https://github.com/nostr-protocol/nostr/commit/33a1a70)，用 EVENT/REQ/CLOSE 模型取代了原始消息格式，该模型至今仍在使用。在此次重写之前，客户端和 relay 通过更简单的结构通信。将 event 发布（EVENT）与订阅管理（REQ/CLOSE）分离，使得 relay 端过滤成为可能，这对后续的扩展至关重要。

[NIP-04](/zh/topics/nip-04/) 在同月到来，使用基于 secp256k1 Diffie-Hellman 密钥交换派生的共享密钥添加了加密私信。其加密方式较为基础（AES-256-CBC），后来被 [NIP-44](/zh/topics/nip-44/) 经过审计的密码学所取代，但它为少数早期用户提供了协议上的第一个私密通信通道。

工具生态随 [noscl](https://github.com/fiatjaf/noscl)（一个 Go 命令行客户端，用于终端 relay 交互）的出现而扩展，futurepaul 开始开发 [nostr-rs](https://github.com/futurepaul/nostr-rs)，一个早期的 Rust 实现。整个网络在两三个 relay 上运行，通过一个 [Telegram 群组](https://t.me/nostr_protocol)协调，活跃贡献者大约七人。

### 2022 年 2 月：积蓄势能

2021 年 12 月 31 日的 [Hacker News 帖子](https://news.ycombinator.com/item?id=29749061)持续吸引开发者直到二月。[nostr-protocol/nostr](https://github.com/nostr-protocol/nostr) 仓库（正式的 [NIPs 仓库](https://github.com/nostr-protocol/nips)要到 2022 年 5 月才存在）在二月收到六个 PR，包括 vinliao 的 NIP-13（工作量证明）、fiatjaf 的 NIP-14（声誉）、Cameri 的 NIP-15（资源关系）和 melvincarvalho 的 [NIP-17](https://github.com/nostr-protocol/nostr/pull/75)（基于 Nostr 的 Git 更新）。NIP 编号后来被重新分配给私密私信；Nostr 上的 git 协作通过后来的 [gitworkshop.dev](https://gitworkshop.dev) 独立继续。

Greg Heartsfield 的 [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) 是当月的主力，贡献了 34 次提交和三个版本。2 月 12 日的 0.5.0 版本添加了 [NIP-05](/zh/topics/nip-05/) 已验证用户发布限制。0.5.1 和 0.5.2 在接下来两周相继发布，该 relay 独自承载了网络的大部分流量。

Robert C. Martin（Uncle Bob）正在构建 [more-speech](https://github.com/unclebob/more-speech)，一个 Clojure 桌面客户端，在 1 月 18 日到 2 月底之间记录了 69 次提交。他的参与吸引了更广泛的软件工程社区的关注。fiatjaf 的 [nos2x](https://github.com/fiatjaf/nos2x) 浏览器扩展在二月发布了 [NIP-04](/zh/topics/nip-04/) 解密支持和 relay 偏好策略，实现了 Web 客户端至今仍用于密钥委托的 `window.nostr` 接口（[NIP-07](/zh/topics/nip-07/)）。

[Branle](https://github.com/fiatjaf/branle)，当时的主要 Web 客户端，在 2 月 13 日获得了 `web+nostr` 协议处理器注册，这是 Nostr 应用间深层链接的早期尝试。[nostr-tools](https://github.com/nbd-wtf/nostr-tools) 加强了 NIP-05 验证。[go-nostr](https://github.com/nbd-wtf/go-nostr) 在 11 次提交中添加了 NIP-04 加密私信支持和 NIP-12（通用 Tag 查询）解析。网络大约在 7-15 个 relay 上运行，活跃用户群可能在数百人。Damus 和 Nostream 尚不存在，要到 2022 年 4 月才会出现。

### 2023 年 2 月：国际关注

2023 年 2 月为 Nostr 带来了最大的公众关注浪潮。[Damus](https://github.com/damus-io/damus)，William Casarin 的 iOS 客户端，在多次被拒后于 [1 月 31 日获得 Apple App Store 批准](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store)。到 2 月 1 日，它进入美国社交网络类前十。两天后的 2 月 2 日，据报道应中国国家互联网信息办公室要求，[Apple 将 Damus 从中国 App Store 下架](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/)。

包括 TechCrunch 和 CoinDesk 在内的主流媒体报道了这一下架事件，扩大了对该应用和协议的认知。到 2 月 3 日，nostr.directory 上带有元数据的唯一公钥超过 30 万。所有 relay 均由自费的爱好者运营，基础设施争先恐后地处理负载。到二月初大约追踪到 289 个 relay，这一数字继续攀升。

[NIPs 仓库](https://github.com/nostr-protocol/nips)当月记录了 29 个合并 PR，是协议历史上当时单月最高。[NIP-57](https://github.com/nostr-protocol/nips/pull/224)（Lightning Zaps）和 [NIP-23](https://github.com/nostr-protocol/nips/pull/220)（长文内容）均在 2 月 13 日合并，在一天之内为 Nostr 添加了 Bitcoin 微支付并将其扩展到短帖之外。[NIP-65](/zh/topics/nip-65/)（Relay 列表元数据）一周前的 2 月 7 日合并，为后续的 outbox 模型奠定基础。[NIP-46](/zh/topics/nip-46/)（Nostr Connect）和 [NIP-58](/zh/topics/nip-58/)（徽章）也在月末前落地。

Human Rights Foundation 于 2 月 21 日[向 William Casarin 授予 50,000 美元用于 Nostr 和 Damus 开发](https://hrf.org/devfund2023q1)，这是首批面向 Nostr 项目的机构资助之一。OpenSats 尚未启动其 Nostr 基金（要到 [2023 年 7 月](https://opensats.org/blog/nostr-grants-july-2023)）。

### 2024 年 2 月：协议韧性

2024 年 2 月的重点从增长转向协议韧性。[NIP-17](/zh/topics/nip-17/)（私密私信）自前一年七月开放以来，正在使用 [NIP-44](/zh/topics/nip-44/) 经审计的密码学和 [NIP-59](/zh/topics/nip-59/) gift wrapping 来替代老化的 [NIP-04](/zh/topics/nip-04/) 加密。NIP-04 向 relay 运营者泄露元数据，他们可以看到发送者-接收者对。NIP-17 通过一次性密钥对隐藏发送者身份，在三月最后一轮审查后合并。

[NIP-29](/zh/topics/nip-29/)（简单群组）在数月讨论后于 [2 月 28 日合并](https://github.com/nostr-protocol/nips/pull/566)，定义了 relay 如何通过管理员角色和访问控制托管审核群聊。[NIP-92](/zh/topics/nip-92/)（imeta tag）于 2 月 1 日合并，标准化了客户端如何为媒体 event 附加图片尺寸和 blurhash 预览。

2 月 16 日，NIPs 仓库添加了 [BREAKING.md](https://github.com/nostr-protocol/nips/commit/62c48eff)，一个跟踪协议规范向后不兼容变更的文件。它的创建承认 Nostr 已达到需要正式记录破坏性变更的成熟度。

当月合并了 22 个 PR。[npub.cash](https://github.com/cashubtc/npubcash-server) 作为 Lightning 地址服务发布，让任何 npub 无需运行服务器即可接收支付。2 月 8 日发表的一篇[学术论文](https://arxiv.org/abs/2402.05709)发现，95% 的免费 relay 无法通过捐赠覆盖运营成本，35% 的付费 relay 收取低于 1,000 sats（当时约 0.45 美元）的入场费。

### 2025 年 2 月：基础设施增长

2025 年 2 月向 NIPs 仓库产出 28 个合并 PR。[Right to Vanish](/zh/topics/nip-62/) NIP 于 2 月 19 日合并，定义了用户如何请求 relay 删除其数据，以回应关于数据可移植性和用户控制的监管问题。

[NIP-60](/zh/topics/nip-60/)（Cashu 钱包）和 NIP-61（Nutzaps）收到简化更新，精简了 ecash 代币存储格式。q-tag（引用 tag）在多个 NIP 中持续推广，标准化 event 如何引用其他 event 用于引用和线程化。

客户端发布标志着稳步进展。[Notedeck](https://github.com/damus-io/notedeck) v0.3.0 alpha 在一月最后一天发布，二月持续被采用。Primal v2.1 于 2 月 7 日发布，[GRAIN](https://github.com/0ceanSlim/grain) v0.3.0（Go relay 实现）于 2 月 21 日发布。

NOSTRLDN v5 将伦敦 Nostr 社区聚集起来举办第五次聚会。DVMCP 桥接了 Nostr 的数据自动售货机（[NIP-90](/zh/topics/nip-90/)）与 Model Context Protocol，预示了接下来一个月到来的 AI 代理集成工作。

### 2026 年 2 月：超越社交媒体

*2026 年 2 月活动摘自 Nostr Compass 第 [#8](/zh/newsletters/2026-02-04-newsletter/) 期至第 [#11](/zh/newsletters/2026-02-25-newsletter/) 期。*

2026 年 2 月产出了任何单个 Nostr 月份中范围最广泛的应用层开发。[Mostro](https://github.com/MostroP2P/mostro) 发布了去中心化点对点 Bitcoin 交易的[首个公开 beta](/zh/newsletters/2026-02-11-newsletter/#mostro-发布首个公开-beta)，[Zapstore](https://github.com/zapstore/zapstore) 在数月的候选版本测试后达到 [1.0 稳定版](/zh/newsletters/2026-02-11-newsletter/#zapstore-v100)。[White Noise v0.3.0](/zh/newsletters/2026-02-25-newsletter/#white-noise-v030) 交付了实时 [Marmot](/zh/topics/mls/) 加密消息，支持 Amber 签名器并合并了 160 余项改进。

来自 pablof7z（用于代理工作流的 NIP-AE 和用于 MCP 服务器公告的 NIP-AD）和 joelklabo（AI 代理消息）的竞争性 AI 代理提案与扩展 [NIP-90](/zh/topics/nip-90/) 的 [DVM 代理协调提案](/zh/newsletters/2026-02-25-newsletter/#nip-更新)同时到来。[ContextVM](/zh/newsletters/2026-02-25-newsletter/#contextvm基于-nostr-的-mcp) 发布了将 Model Context Protocol 连接到 Nostr 传输的 SDK 改进。[Burrow](/zh/newsletters/2026-02-25-newsletter/#burrow面向-ai-代理的-mls-消息) 为 AI 代理和人类添加了 [Marmot](/zh/topics/mls/) 加密消息，将 Nostr 的身份和 relay 基础设施扩展到机器对机器通信。

[FIPS](/zh/newsletters/2026-02-25-newsletter/#fipsnostr-原生网状网络) 发布了 Nostr 原生网状网络的可用 Rust 实现，使用 secp256k1 密钥对作为节点身份，支持跨 UDP、以太网、蓝牙或 LoRa 无线电的传输无关路由。其设计表明 Nostr 的密钥模型超越了社交媒体，延伸到物理网络基础设施。

[OpenSats 宣布了第十五批 Nostr 资助](https://opensats.org/blog/fifteenth-wave-of-nostr-grants)，资助项目包括 ContextVM 和 Nostube。协议变更包括 [NIP-47](/zh/topics/nip-47/) 为 Nostr Wallet Connect 提供的 hold invoice 支持和 [NIP-45](/zh/topics/nip-45/)（计数结果）用于 relay 端计数估算的 HyperLogLog。[NIP-85](/zh/topics/nip-85/)（可信断言）用于 [Web of Trust](/zh/topics/web-of-trust/) 评分的服务提供商可发现性也已合并。[rust-nostr](https://github.com/rust-nostr/nostr) 开始全面 API 重新设计，Nostria 3.0 和 [Frostr](https://github.com/FROSTR-ORG)（iOS TestFlight）均已发布。[Blossom](/zh/topics/blossom/) 的本地缓存层解决了跨 relay 的媒体可用性问题。

### 展望未来

五个二月的协议历史展示了从基础工作到应用层多样化的一致演进，2023 年的用户涌入是转折点。2021 年，七位贡献者在三个 relay 上工作。到 2026 年，同一协议支持在生产基础设施上运行的网状网络和自主代理提案。

---

本周就到这里。正在构建什么或有新闻要分享？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 [NIP-17](/zh/topics/nip-17/) 私信联系我们</a>或在 Nostr 上找到我们。
