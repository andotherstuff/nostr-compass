---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) 带来实时消息和 Amber 签名器支持，合并了 160 余项改进。[diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) 修复视频播放问题，新增 Kind 22236 浏览 event 用于创作者数据分析。[Pika](https://github.com/sledtools/pika)、[Ridestr](https://github.com/variablefate/ridestr) 和 [Unfiltered](https://github.com/dmcarrington/unfiltered) 均发布更新。[FIPS](https://github.com/jmcorgan/fips) 发布 Nostr 原生网状网络的可用 Rust 实现。Notecrumbs 修复 damus.io 链接预览的稳定性问题。[ContextVM](https://contextvm.org) 将 Nostr 与 Model Context Protocol 对接。新项目包括 [Burrow](https://github.com/CentauriAgent/burrow)（为 AI 代理与人类之间提供 MLS 加密通信）和 [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension)（基于浏览器的密钥库与身份管理）。深入解析涵盖 NIP-55 Android 签名和 NIP-60 Cashu 钱包同步。

## 新闻

### Notecrumbs 稳定性改进

[Notecrumbs](https://github.com/damus-io/notecrumbs)，为 damus.io 链接预览提供支持的 Nostr API 和 Web 服务器，收到一系列修复以解决可靠性问题。

[并发修复](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49)将飞行中去重机制替换为 watch channel。两个调用方同时请求同一条笔记时，均可能成为数据获取者，若其中一方在另一方订阅通知前先完成，便会引发死锁。带原子操作的 watch channel 确保只有一个获取者运行，其余等待结果。

[速率限制](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17)实现了针对 relay 频繁请求的双层防护。当用户反复访问同一条笔记时，系统对 relay 请求设置 5 分钟冷却窗口进行防抖处理。这一保护覆盖所有 [NIP-19](/zh/topics/nip-19/) 类型和个人资料信息流，防止在高流量期间对 relay 产生成比例的垃圾请求。

[性能改进](https://github.com/damus-io/notecrumbs/commit/38670b3972b6)将二次数据获取移至后台 tokio 任务。页面现在使用缓存数据即时渲染，不再阻塞于可能累计长达 7.5 秒的顺序 relay 超时。此次修复同时升级至 nostrdb 0.10.0。

### ContextVM：基于 Nostr 的 MCP

[ContextVM](https://contextvm.org) 是一套将 Nostr 与 [Model Context Protocol](https://modelcontextprotocol.io/)（MCP）对接的工具集。近期提交引入了新的 [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/) 规范以支持支付功能，并在整个二月持续推进 [SDK](https://github.com/ContextVM/sdk) 改进。

SDK 为基于 Nostr 的 MCP 提供 TypeScript 客户端和服务端传输层。开发者可以在 Nostr 网络上暴露 MCP 服务器，客户端可以与之连接。Relay 充当盲目消息总线，仅负责路由加密 event。不具备原生 Nostr 支持的客户端通过代理层接入。该库处理 relay 管理和用于 event 认证的密码学签名，兼容 Node.js 和浏览器环境。

[CVMI](https://github.com/ContextVM/cvmi) 提供用于服务发现和方法调用的 CLI。[Relatr](https://github.com/ContextVM/relatr) 结合社交图谱距离与个人资料验证计算个性化信任评分。

ContextVM 将自身定位为桥接层：现有 MCP 服务器在保持原有传输方式的同时获得 Nostr 互操作性。

### White Noise 记录去中心化用户搜索

[jgmontoya 的博客文章](https://blog.jgmontoya.com/2026/02/22/user-search.html)详细介绍了 [White Noise](https://github.com/marmot-protocol/whitenoise) 如何在去中心化的 relay 网络中处理用户搜索。

个人资料分布带来了挑战：与拥有统一数据库的中心化通讯软件不同，Nostr 个人资料散布于数十个 relay 上，没有中央索引。White Noise 通过并行运行的生产者-消费者架构解决这一问题。

生产者进程从用户的关注列表持续向外扩展社交图谱，获取距离递增的关注列表，并将发现的 pubkey 加入队列以待解析个人资料。消费者通过五个成本递增的层级解析匹配项：本地用户表（最快）、上次搜索的缓存个人资料、已连接的 relay、按 [NIP-65](/zh/topics/nip-65/) 获取的用户 relay 列表，以及直接查询用户声明的 relay（最慢）。

冷搜索大约需要 3 秒，而基于缓存的热搜索约为 10 毫秒。对于尚未建立社交图谱的新用户，系统注入联结紧密的引导节点以确保搜索功能正常运作。群组成员资格作为隐性社交信号，与显性关注并列。

作者指出，数据埋点对于性能优化至关重要。缺乏指标时，改进只能靠猜测。

### FIPS：Nostr 原生网状网络

[FIPS](https://github.com/jmcorgan/fips)（Free Internetworking Peering System）是一个可用的 Rust 实现，构建以 Nostr 密钥对（secp256k1）作为节点身份的自组织网状网络。[设计文档](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)与功能代码同步提供。

该协议解决的是基础设施独立性问题：节点无需中央服务器或证书机构即可自动发现彼此。生成树提供基于坐标的路由，bloom filter 传播可达性信息，让节点仅凭本地知识做出转发决策。传输无关性意味着同一协议可运行于 UDP、以太网、蓝牙、LoRa 无线电或任何支持数据报的介质。

两层加密保护流量。链路层加密（Noise IK 模式）通过相互认证和前向保密保护逐跳的邻节点通信。会话层加密（Noise XK 模式）提供端到端保护以防范中间路由器，只有目标节点才能解密有效载荷。这与 TLS 在穿越不可信网络时保护 HTTP 流量的方式相同。

架构采用"贪婪嵌入"生成树进行路由。每个节点根据其相对于树根和父节点的位置获得坐标。数据包贪婪地向坐标更接近目标的方向路由，bloom filter 广告可达端点。当贪婪路由失败（局部最小值）时，节点可回退至基于树的路径。

Rust 实现已包含带 bloom filter 发现的 UDP 传输，未来计划集成 Nostr relay 以实现对等引导。

## 版本发布

本周 relay 基础设施和客户端应用均有版本发布，同时有新项目进入这一领域。

### HAVEN v1.2.0

[HAVEN](https://github.com/bitvora/haven)，将四种 relay 功能与 [Blossom](/zh/topics/blossom/) 媒体服务器捆绑的一体化个人 relay，发布了 [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0)。此版本超越了[上周报道的](/zh/newsletters/2026-02-18-newsletter/#haven-v120-rc3) RC 阶段。

多 npub 支持通过白名单机制让单个 HAVEN 实例服务多个 Nostr 身份，并新增黑名单功能用于访问控制。重写的备份系统采用可移植的 JSONL 格式，带有 `haven restore` 命令用于从 JSONL 文件导入笔记。云存储集成新增 `--to-cloud` 和 `--from-cloud` 标志用于远程备份管理。

[Web of Trust](/zh/topics/web-of-trust/) 改进包括可配置的信任计算深度级别，以及带无锁优化的自动 24 小时刷新间隔以降低内存开销。relay 请求的 user-agent 配置和可配置的 Blastr 超时设置完善了此次发布，同时支持导出数据为压缩 JSONL 格式。

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise)，基于 [MLS](/zh/topics/mls/) 加密实现 [Marmot](/zh/topics/marmot/) 协议的加密消息应用，发布了 [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0)，合并了 160 余项改进。

此版本通过流式连接取代轮询实现实时消息，消息即时送达。Amber 支持（[NIP-55](/zh/topics/nip-55/)）意味着私钥无需触碰应用。图片分享现已支持上传进度跟踪和加载时的 blurhash 占位图。全屏查看支持捏合缩放。

群组消息在可靠性上得到改进，聊天列表显示发送者姓名，[MLS](/zh/topics/mls/) 加密确保前向保密。用户搜索从关注列表向外扩展至四度分隔，搜索结果随发现即时流入。

由于 Marmot 协议变更和切换至加密本地存储，此版本包含一项破坏性变更：升级时将重置所有本地数据。用户在升级前应备份 nsec 密钥。

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile)，基于还原的 Vine 存档构建的短视频循环播放客户端，发布了 [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5)，带来大量视频播放修复和全新的去中心化数据分析系统。

视频播放问题是修复重点：幽灵暂停、视频间的双重音频、缩略图与首帧之间的黑闪，以及播放器销毁后崩溃问题均已解决。池化视频播放器现在处理主页信息流以确保一致的播放体验。

Kind 22236 短暂浏览 event 支持创作者数据分析和内容推荐。系统跟踪流量来源（主页、发现变体、个人资料、分享、搜索）和循环播放次数，同时过滤自身浏览。Nostr event imeta tag 中本地文件路径泄露问题已修复，按 BUD-01 规范在客户端构造规范的 Blossom URL。

[NIP-46](/zh/topics/nip-46/) 远程签名器改进包括并行化的 relay 连接和回调 URL 支持。Android 在签名器批准后恢复应用时重新连接 WebSocket。

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle)，专注于 relay 管理和 [Web of Trust](/zh/topics/web-of-trust/) 审核的 Web 端 Nostr 客户端，发布了 [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30)，新增视频缩略图支持，改善了信息流中的媒体浏览体验。

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public)，iOS 端 Nostr 客户端，发布了 [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0)，新增直播流信息流版块和重新设计的设置界面。GIF 现在可以托管在 Blossom 媒体服务器上，减少对中心化服务的依赖。Tenor 不可用时 Klipy GIF 集成提供备选方案。私信会话中的年份标题和提及数量显示完善了面向用户的变更。

开发者工具和 CLI 应用本周也收到了更新。

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak)，fiatjaf 的 Nostr 命令行瑞士军刀，发布了 [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5)，新增 `nak profile` 子命令用于获取和展示用户个人资料。`git clone` 命令现在支持 `nostr://` URI 中的 [NIP-05](/zh/topics/nip-05/) 名称，可通过人类可读标识符克隆仓库。

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika)，基于 [Marmot](/zh/topics/marmot/) 协议构建的适用于 iOS、Android 和桌面端的 [MLS](/zh/topics/mls/) 加密消息应用，发布了 [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3)。近期提交为桌面应用添加了文件上传和拖放媒体支持，同时修复了 Cloudflare Workers 部署问题。

Pika 采用 Rust 核心承载所有业务逻辑，iOS（SwiftUI）和 Android（Kotlin）作为薄 UI 层渲染状态快照。MDK（Marmot Development Kit）提供 MLS 实现。项目处于 alpha 阶段，不建议用于敏感场景。

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr)，基于 Cashu 支付的去中心化打车平台，发布了 [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6)。此版本修复了 TalkBack 无障碍访问问题，以及切换支付方式时司机从附近列表消失、司机下线时已选司机数量未更新等 bug。

"发送给所有人"功能现已更名为"广播 RoadFlare"，并修复了新安装司机端的静默失败问题。Ridestr 实现了 HTLC 托管用于无需信任的打车支付，以及跨设备的 [NIP-60](/zh/topics/nip-60/) 钱包同步。

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered)，Android 端类 Instagram 图片分享应用，发布了 [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6)，改进了用户搜索功能并新增每 60 秒自动重连 relay。

使用 Kotlin 和 Jetpack Compose 构建，Unfiltered 采用 rust-nostr 绑定和兼容 Blossom 的服务器托管图片。Amber 集成（[NIP-55](/zh/topics/nip-55/)）处理安全密钥管理。应用按时间顺序显示关注账号的帖子，无算法推荐，无广告。

本周还有两个新的消息和签名项目发布。

### Burrow：面向 AI 代理的 MLS 消息

[Burrow](https://github.com/CentauriAgent/burrow) 是一款实现 [Marmot](/zh/topics/marmot/) 协议的消息应用，提供无需电话号码或中心化服务器的 MLS 加密通信。人类用户和 AI 代理均可参与。

纯 Rust CLI 守护进程配合 JSONL 输出模式处理与自动化系统的集成。Flutter 跨平台应用覆盖 Android、iOS、Linux、macOS 和 Windows。媒体附件与消息同步加密，WebRTC 处理音视频通话并支持可配置的 TURN 服务器。

Burrow 在 Nostr 基础设施上叠加 MLS 加密。身份使用 Nostr 密钥对（secp256k1），MLS KeyPackage 以 kind 443 event 发布。消息以 [NIP-44](/zh/topics/nip-44/) 加密作为 kind 445 event，邀请使用 [NIP-59](/zh/topics/nip-59/) 礼品包裹。

[OpenClaw](https://openclaw.ai) 集成让 AI 代理以完整工具访问权限参与其中。带审计日志的访问控制列表管理联系人和群组权限。这一组合使 Burrow 适用于需要在去中心化基础设施上实现 Signal 级别加密的代理间及代理与人类的消息场景。

### Nostria Signer 扩展

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) 是一款基于 Chromium 的浏览器扩展，为 Nostr 用户提供密钥库和身份管理功能。

包含多个账号的多个密钥库让用户可以为不同场景组织身份。国际化支持包括 RTL 语言。使用 Angular 和 TypeScript 构建（占代码库的 79.2%），可作为浏览器扩展和渐进式 Web 应用运行。

Nostria Signer 实现了 [NIP-07](/zh/topics/nip-07/) 浏览器扩展签名，让基于 Web 的 Nostr 客户端无需直接访问私钥即可请求 event 签名。自动化的钱包迁移处理通过 Chrome Web Store 分发的更新。用户也可以从 `dist/extension` 文件夹侧载安装。

开发者强调该项目处于实验阶段：用户必须自行管理密钥恢复短语，开发者无法恢复丢失的密钥访问权限。

## 项目更新

### Formstr 迁移至新组织

[Formstr](https://github.com/formstr-hq/nostr-forms)，Nostr 上的 Google Forms 替代方案，将仓库从 `abh3po/nostr-forms` 迁移至 `formstr-hq` 组织。这一 OpenSats 资助项目在新地址继续开发。

### 值得关注的开放 PR

Nostr 项目中的进行中工作：

- **Damus Outbox 模型**（[PR #3602](https://github.com/damus-io/damus/pull/3602)）：iOS 上 gossip/outbox relay 模型的实现计划。这一架构变更通过向收件人实际阅读的 relay 发布消息来改善消息投递。

- **Notedeck 跨平台通知**（[PR #1296](https://github.com/damus-io/notedeck/pull/1296)）：Damus 桌面客户端的原生通知系统，覆盖 Android FCM、macOS 和 Linux。

- **NDK Cashu v3 升级**（[PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)）：将 Nostr Development Kit 的钱包集成更新至 cashu-ts v3。

- **Zeus Cashu 离线功能**（[PR #3742](https://github.com/ZeusLN/zeus/pull/3742)）：Zeus Lightning 钱包的离线 ecash 收发功能。

- **Shopstr 加密数字交付**（[PR #231](https://github.com/shopstr-eng/shopstr/pull/231)）：为数字商品添加加密交付功能，并为实物商品添加动态重量支持。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**本周已合并：**

- **[NIP-85 服务提供商可发现性](https://github.com/nostr-protocol/nips/pull/2223)**：[NIP-85](/zh/topics/nip-85/) 规范新增客户端如何发现可信断言提供商的指南。当客户端需要 [Web of Trust](/zh/topics/web-of-trust/) 评分或其他计算指标时，可以向 relay 查询来自用户已关注或信任的提供商发布的 kind 30085 公告。

- **[NIP-29 移除非托管群组](https://github.com/nostr-protocol/nips/pull/2229)**：[NIP-29](/zh/topics/nip-29/) 群组聊天规范移除了对非托管群组（任何成员均可添加其他人）的支持。所有 NIP-29 群组现在均要求 relay 端管理并设置明确的管理员角色，简化实现并减少垃圾信息向量。

- **[NIP-11 移除已弃用字段](https://github.com/nostr-protocol/nips/pull/2231)**：[NIP-11](/zh/topics/nip-11/) relay 信息文档不再包含已弃用的 `software` 和 `version` 字段。实现应从响应中移除这些字段。

- **[NIP-39 迁移身份 tag](https://github.com/nostr-protocol/nips/pull/2227)**：外部身份声明（[NIP-39](/zh/topics/nip-39/) 中 GitHub、Twitter 等的 `i` tag）从 kind 0 个人资料迁移至专用的 kind 30382 event，将身份验证与个人资料元数据分离。

**AI 代理 NIP 进展：**

四个以 AI 为重点的 NIP 持续活跃开发中。自[上周报道](/zh/newsletters/2026-02-18-newsletter/#ai-代理-nip-相继登场)以来：

- **[NIP-AE：Agents](https://github.com/nostr-protocol/nips/pull/2220)**（2 月 19 日更新）：定义代理身份，使用 kind 4199 作为代理定义，kind 4201 用于提示（"nudges"）。代理可引用 [NIP-94](/zh/topics/nip-94/) 文件元数据以获取扩展描述。

- **[NIP-XX：AI 代理消息](https://github.com/nostr-protocol/nips/pull/2226)**（2 月 18 日更新）：通过七种短暂 event kind（25800-25806）标准化对话消息，涵盖状态、流式增量、提示词、响应、工具调用、错误和取消。kind 31340 "AI Info" event 让代理公告支持的模型和能力。

- **[NIP-AC：DVM 代理协调](https://github.com/nostr-protocol/nips/pull/2228)**（2 月 18 日开启）：扩展 [NIP-90](/zh/topics/nip-90/) 以支持自主代理工作流。新增代理发现的心跳机制、质量跟踪的任务评审、结果承诺的数据托管、多步骤流水线的工作流链，以及竞争性提供商选择的群体竞价。参考实现运行于 2020117.xyz。

- **[NIP-AD：MCP 服务器公告](https://github.com/nostr-protocol/nips/pull/2221)**（2 月 12 日开启）：标准化在 Nostr 上公告 Model Context Protocol 服务器和技能的方式，已在 TENEX 平台上投入使用。

**其他开放 PR：**

- **[NIP-144：服务授权协议](https://github.com/nostr-protocol/nips/pull/2232)**：定义客户端如何向 Nostr 上的服务提供商证明身份和权限。

- **[NIP-DC：Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**：alexgleason 提议将 Webxdc（去中心化 Web 应用）与 Nostr event 集成。

## NIP 深入解析：NIP-55（Android 签名器应用）

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md) 定义 Android Nostr 客户端如何向专用签名器应用请求密码学操作。本周 [White Noise v0.3.0](#white-noise-v030) 和 [Unfiltered v1.0.6](#unfiltered-v106) 均新增了 Amber 支持，Android 签名协议值得深入了解。

**通信渠道：**

NIP-55 通过两种机制实现应用间签名。Intent 为一次性操作提供带视觉反馈的手动用户批准。Content Resolver 在用户授予持久权限后支持自动签名，让应用无需反复提示即可在后台签名。

通信使用自定义 `nostrsigner:` URI 方案。客户端发起连接的方式如下：

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**支持的操作：**

规范定义了七种密码学方法：event 签名（`sign_event`）、公钥获取（`get_public_key`）、[NIP-04](/zh/topics/nip-04/) 加密/解密、[NIP-44](/zh/topics/nip-44/) 加密/解密，以及 zap event 解密（`decrypt_zap_event`）。

**权限模型：**

客户端调用一次 `get_public_key` 建立信任关系，接收签名器的包名和用户 pubkey。规范要求客户端保存这些值并不再调用 `get_public_key`，以防止指纹追踪攻击。

对于签名请求，用户可以一次性批准或授予"记住我的选择"以支持后台操作。若用户持续拒绝操作，签名器返回"已拒绝"状态，防止反复提示。

**实现情况：**

[Amber](https://github.com/greenart7c3/amber) 是 Android 的主要 NIP-55 签名器。支持 NIP-55 的客户端包括 [Amethyst](https://github.com/vitorpamplona/amethyst)、[White Noise](#white-noise-v030)、[Unfiltered](#unfiltered-v106) 等。Web 应用无法直接接收签名器响应，必须使用回调 URL 或剪贴板操作。

**与其他签名 NIP 的关系：**

NIP-55 与 [NIP-07](/zh/topics/nip-07/)（浏览器扩展）和 [NIP-46](/zh/topics/nip-46/)（通过 relay 远程签名）互补。NIP-07 适用于桌面浏览器，NIP-46 适用于跨设备签名，NIP-55 则以最低延迟提供原生 Android 集成。

## NIP 深入解析：NIP-60（Cashu 钱包）

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) 定义 [Cashu](/zh/topics/cashu/) ecash 钱包如何在 Nostr relay 上存储状态，实现跨应用的钱包同步。[Ridestr v0.2.6](#ridestr-v026) 使用 NIP-60 进行跨设备钱包同步，该协议值得深入了解。

**Event Kind：**

NIP-60 使用四种 event 类型。可替换的 kind 17375 存储钱包配置，包括 mint URL 和用于接收 P2PK ecash 支付的专用私钥。Token event（kind 7375）包含未花费的密码学凭证，消费历史（kind 7376）记录交易以供用户查看。可选的 kind 7374 跟踪 mint 支付报价。

**钱包架构：**

钱包状态存储在 relay 上，可跨应用访问。用户的钱包 event 包含对 Cashu mint 的加密引用和一个与用户 Nostr 身份分离的钱包专用私钥。这一分离至关重要：钱包密钥处理 ecash 操作，Nostr 密钥处理社交功能。

```json
{
  "kind": 17375,
  "content": "<nip44-encrypted-wallet-config>",
  "tags": [["d", "cashu-wallet"]]
}
```

**凭证管理：**

Cashu 凭证是无记名工具。一旦花费，凭证即失效。NIP-60 通过滚动机制处理这一问题：花费时，客户端创建包含剩余未花费凭证的新 token event，并通过 [NIP-09](/zh/topics/nip-09/) 删除原有 event。已销毁的 token ID 存入 `del` 字段用于状态跟踪。

客户端应定期向 mint 验证凭证以检测已花费的凭证。允许每个 mint 存在多个 token event，消费历史 event 帮助用户跟踪交易，尽管这些是可选的。

**安全模型：**

所有敏感数据使用 [NIP-44](/zh/topics/nip-44/) 加密。钱包私钥从不以明文形式出现。由于 relay 存储加密的数据块而无法理解其内容，即使在不可信的 relay 上，钱包状态也保持私密。

**实现情况：**

支持 NIP-60 的钱包包括 [Nutsack](https://github.com/gandlafbtc/nutsack) 和 [eNuts](https://github.com/cashubtc/eNuts)。[Ridestr](#ridestr-v026) 等客户端使用 NIP-60 进行跨设备同步，让用户在桌面端充值并在移动端消费，无需手动转账。

---

本周就到这里。正在构建什么或有新闻要分享？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 [NIP-17](/zh/topics/nip-17/) 私信联系我们</a>或在 Nostr 上找到我们。
