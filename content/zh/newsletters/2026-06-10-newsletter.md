---
title: 'Nostr Compass #26'
date: 2026-06-10
publishDate: 2026-06-10
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-10-newsletter.md
translationDate: 2026-07-01
---

Marmot 协议组织为 v2 协议草案和原生 client 谱系开放了三个新的 repo：一个名为 `darkmatter` 的 Rust workspace、一个 SwiftUI iOS 应用 `darkmatter-ios` 以及一个 Kotlin/Compose Android 应用 `darkmatter-android`。原始的 Flutter Whitenoise 被归档。Chama 在一周内压缩了十七个版本发布，在 v3.0.0 越过独立应用线，然后在 v3.1.0 中落地了完整的交易室 UI 重绘和每卖家店面，在持有者专属 Shamir 共享、仲裁者替换、全球社区路由和端到端交易通知之上。Coracle 推出了由开源 Caravel 和 zooid 栈支持的付费托管 relay 服务，计划深度 Flotilla 集成。Angor 在 v0.2.30 中默认切换到主网，并在 v0.2.29 中落地了 3 用户 UAT 资金测试。Amethyst 落地了 41 个未发布的 PR，延续上周的 NIP-32 / NIP-F4 / Tor 工作。NIP-67（EOSE 完整性提示）和 NIP-50 autocomplete 合并，关闭了核心 relay 协议中两个长期存在的正确性差距。NIP-GART 提议了紧急警报的隐私保护 wire 格式，NIP-46 增加了一个 logout 方法。

## 头条报道

### Marmot v2（Dark Matter）：协议重新起草、原生 client、归档的 Flutter 应用

本周在 [marmot-protocol](https://github.com/marmot-protocol) GitHub 组织下出现了三个新的 repo，共同形成了 Marmot v2 协议草案和取代 Flutter 应用线的原生 client 谱系的早期进展形态。[`darkmatter`](https://github.com/marmot-protocol/darkmatter)（Rust，5 月 13 日创建，过去七天三十四个 commits）在 `spec/` 中保存 v2 协议草案、一个 OpenMLS 支持的 `crates/cgka-engine` 中的 CGKA 引擎、一个带有 property 测试的一致性模拟器，以及一个用于收敛证明的 Tamarin 形式模型。[`darkmatter-ios`](https://github.com/marmot-protocol/darkmatter-ios)（Swift，5 月 25 日创建）是一个 SwiftUI client，由从 Rust workspace 生成的 vendored `MarmotKit` UniFFI xcframework 支持。[`darkmatter-android`](https://github.com/marmot-protocol/darkmatter-android)（Kotlin/Jetpack Compose，5 月 25 日创建）位于相同的 Rust 绑定之上。原始的 Flutter Whitenoise 已被标记为 [`whitenoise-archive`](https://github.com/marmot-protocol/whitenoise-archive)（"ARCHIVED: This was the original White Noise Flutter app"）；一个新的 [`whitenoise`](https://github.com/marmot-protocol/whitenoise) Dart repo 并行承载活跃的 Flutter 线。

将此视为迈向更可靠 Marmot 的早期进展，而不是完成的转向。darkmatter README 将自己标记为"候选 Marmot v2 协议草案、CGKA 引擎和一致性 workspace"，并直接说："MDK 仍然是已部署的 Rust 协议实现，直到此草案和引擎被采用。"在 workspace 内，cgka-engine crate 标记为 `0.1.0`，"单一内部消费者，非 semver 稳定"。每个规范页面都带有"状态：内部审查草案"。workspace repo 三颗星，iOS 和 Android 应用零颗星，确认工作处于公告前状态。方向、范围和纪律是这里的信号；生产就绪不是主张。

协议草案将 v1 到 v2 的差异具体化。MIP-01 的整体 `marmot_group_data` MLS 扩展，自 Marmot 开始以来在一个总括下承载了群组名称、描述、管理员 pubkey、Nostr 群组路由 id、relay 列表、群组图像数据和消失消息设置，被 [拆分为版本化的应用组件](https://github.com/marmot-protocol/darkmatter/blob/master/spec/mip-coverage.md)：`marmot.group.profile.v1` 用于名称和描述、`marmot.group.admin-policy.v1` 用于管理员 pubkey、`marmot.transport.nostr.routing.v1` 用于随机 `nostr_group_id` 和规范 relay 列表、`marmot.group.blossom.image.v1` 用于图像 hash、加密密钥、nonce 和上传密钥，以及 `marmot.group.message-retention.v1` 用于消失消息秒数。每个组件拥有其确切的字节和自己的版本控制路径，因此未来的功能可以修订一个组件，而无需强迫其他群组状态重新走 MLS 扩展共识。MIP-00 凭证也获得了一个新的基础文档 `account-identity-proof-v1.md`，被称为"v2 中的新功能和破坏性变更"。身份证明现在存在于自己的接口上，与 KeyPackage 构造分开。

库的差异支持了规范的重做。`cgka-engine` 是新的本地群组状态机：它包装 OpenMLS，拥有 `Stable`、`PendingPublish`、`Merging` 和 `Recovering` epoch 状态，将 intents 翻译为 MLS commits，为每个入站传输封套返回类型化的 `IngestOutcome` 和 `GroupEvent` 值，并明确不发布传输和持久性。一个 `TransportPeeler` trait 将 Nostr 与引擎分开，一个 `StorageProvider` trait 将 SQLite（通过 `storage-sqlite`，SQLCipher 支持）与引擎分开。今天的 MDK 将所有这些打包在一起；拆分层允许一个引擎现在位于 Nostr-relay 传输之下，稍后也可以位于 [QUIC 流和 broker 传输](https://github.com/marmot-protocol/darkmatter/blob/master/docs/quic-broker-deployment.md) 之下，而无需重写收敛模型。收敛本身在 `distributed-convergence.md` 中记录，并在 Tamarin 模型中证明，涵盖确定性分支选择、策略门控资格、保留锚重放、陈旧分支拒绝、交付重新排序、重复、应用输出失效、welcome/commit 交接、提议消费和同步时的出站门控。然后 Rust property 测试检查引擎是否使用真实的 OpenMLS 对象和模拟器测试工具遵循相同的规则。这种规模的形式方法可靠性工作在当前的 Marmot 栈中缺失。

两个原生 client 都放弃了 Flutter，转而使用平台原生的 UI 工具包。[`darkmatter-ios`](https://github.com/marmot-protocol/darkmatter-ios) 是纯 SwiftUI，带有一个在设备上解密 MIP-05 推送唤醒的 Notification Service Extension，vendors 一个从 Rust workspace 构建的生成的 `MarmotKit` Swift 包，并在 `dev.ipf.darkmatter` bundle ID 和应用组下注册。[`darkmatter-android`](https://github.com/marmot-protocol/darkmatter-android) 是 Kotlin 和 Jetpack Compose，使用 `just` 驱动的构建，生成一个签名的 `arm64-v8a` APK，并从 `local.properties` 读取遥测端点。Android README 直接说明了架构原则："Dark Matter 拥有协议数据并将其存储在 SQLite 中。Android 应用应渲染该数据、管理 Android 平台行为，并保持 UI 生命周期状态。Android 应用不应成为 Dark Matter 数据的第二个数据库。"这反映了 cgka-engine README 在 Rust 层强制执行的边界纪律，应用于 UI 层。

原生 client 对 Marmot 很重要，因为该协议最常被引用的弱点是在不均匀交付条件下的移动可靠性：错过截止日期的通知唤醒、网络抖动期间的 MLS commit 竞态、使 epoch 前进搁浅的后台 fetch 限制。SwiftUI 和 Compose 让 client 直接访问 Flutter 通过插件桥接到达的平台后台处理原语，UniFFI 绑定路径将协议逻辑保留在一个 Rust workspace 中，作为两个平台上的静态库发布。Flutter Whitenoise 线在未归档的 [`whitenoise`](https://github.com/marmot-protocol/whitenoise) repo 中继续，因此公告是叠加性的：一个新的原生 client 谱系与 Flutter 应用并行运行，同时 v2 规范收敛。从 MDK 或当前的 Whitenoise 应用的生产切换等待草案、引擎和 client 达到生产就绪版本。

### Chama v2.0.0 到 v3.1.0：一周内的独立 P2P 托管

在 Newsletter #25 中以 v1.3.0 引入的 Nostr 原生 P2P 托管 client 在过去七天中发布了十七个带标签的版本，于 6 月 9 日结束于 [v3.1.0](https://github.com/jesuspirate/chama/releases/tag/v3.1.0)，带有交易室 UI 重绘和每卖家店面。版本轨迹讲述了故事：[v2.0.0](https://github.com/jesuspirate/chama/releases/tag/v2.0.0) 是 BREAKING 基础，然后 [v2.0.1](https://github.com/jesuspirate/chama/releases/tag/v2.0.1)、[v2.0.2](https://github.com/jesuspirate/chama/releases/tag/v2.0.2) 和 [v2.0.3](https://github.com/jesuspirate/chama/releases/tag/v2.0.3) 关闭 Fedi WebView 资金轨道差距；[v2.1.0](https://github.com/jesuspirate/chama/releases/tag/v2.1.0)、[v2.2.0](https://github.com/jesuspirate/chama/releases/tag/v2.2.0)、[v2.3.0](https://github.com/jesuspirate/chama/releases/tag/v2.3.0) 和 [v2.3.1](https://github.com/jesuspirate/chama/releases/tag/v2.3.1) 加固仲裁者层；[v2.4.0](https://github.com/jesuspirate/chama/releases/tag/v2.4.0)、[v2.5.0](https://github.com/jesuspirate/chama/releases/tag/v2.5.0) 和 [v2.6.0](https://github.com/jesuspirate/chama/releases/tag/v2.6.0) 添加自我托管接口和全球社区路由；[v2.7.0](https://github.com/jesuspirate/chama/releases/tag/v2.7.0)、[v2.8.0](https://github.com/jesuspirate/chama/releases/tag/v2.8.0)、[v2.9.0](https://github.com/jesuspirate/chama/releases/tag/v2.9.0) 和 [v2.10.0](https://github.com/jesuspirate/chama/releases/tag/v2.10.0) 分层加入通俗英语密钥文案、群组申请、争议截止日期仲裁和声誉。[v3.0.0](https://github.com/jesuspirate/chama/releases/tag/v3.0.0) 将包用端到端交易通知捆绑在一起，6 月 9 日的 [v3.1.0](https://github.com/jesuspirate/chama/releases/tag/v3.1.0) 围绕 Reserved → Locked → Settled 进度主干、角色着色的操作卡以及每卖家店面列表类（精选交换、贷款簿和账单）重绘交易屏幕。

架构转变存在于 v2.0.0 中。托管 LOCK 格式已更改，因此 2-of-3 Shamir 拆分的每个共享仅加密给其持有者（sharePolicy `holder-only-v1`）。联邦的持有者 ecash 不再仅从单个参与者重构，关闭了一条路径，即拥有自己的共享和联邦持有的共享的恶意方可以在未经同意的情况下完成交易。Pre-2.0 client 会响亮地失败，显示"找不到你的共享"；交易无法在陈旧的 client 上完成，过程中不会丢失资金。v2.0 锁需要 v2.x 上的每一方来结算。v2.0.0 还添加了多单位店面和仅 sats 的 Market 视图。

v2.1.0 引入了仲裁者替换：Shamir 索引 2 处的仲裁者共享现在加密到社区仲裁者池的确定性优先顺序中，因此可以在不使交易搁浅的情况下替换缺席的仲裁者。v2.2.0 在 ₿121 交易中证明了替换在野外有效，并添加了愈合替换备份。v2.3.0 通过在锁定时检查列表仲裁者社区成员身份关闭了最后一个仲裁者抢先差距，v2.3.1 关闭了兄弟竞态，其中自动分配的仲裁者插槽是预览，直到锁将他们就座。

自我托管接口在 v2.4.0（Fedimint ecash 钱包的 BIP-39 恢复短语，在 Nostr 上加密存储）和 v2.5.0（拥有 Nostr 身份和钱包种子的主 nsec 备份）中到达。v2.6.0 围绕全球社区选择器重新设计入门，因此没有本地 Chama 的国家/地区的用户被路由到最近的联邦；较早的构建将用户弹开，没有备选。v2.7.0 用通俗英语重写了恢复密钥屏幕（"你账户的唯一密钥及其中的钱；Chama 从不看到它，也无法重置；如果你丢失它，没有人可以找回你的账户"）。v2.8.0 添加了群组申请、暗/亮主题，并添加了两个新的事件 kind（38120 名册、38121 申请）。v2.9.0 在截止日期更改了争议解决：达到到期的有争议的交易现在通过仲裁者裁决解决；先前的行为是自动退款。该版本被标记为 COORDINATED，因此争议中的所有各方都必须更新。v2.10.0 将每交易的赞成/反对评级添加为一个新的事件 kind 38123。

v3.0.0 是应用停止需要协调社区来运营的里程碑。端到端交易通知仅在可操作的状态转换时 ping 用户：交易对手锁定了 sats、支付准备好申领、争议需要用户作为仲裁者裁决，或交易结算或过期。Me 屏幕中的一个切换开关打开或关闭通知，权限提示仅在开关启用时触发。fire-once 去重防止状态重新加载触发警报风暴。在 [PR #103](https://github.com/jesuspirate/chama/pull/103) 中还关闭了一个错误 chama 护栏 bug，早期版本可以为列表加盖一个 chama 的标签，但另一个 chama 的联邦。Windows 和 Linux 桌面 bundle 与该版本一起发布；macOS dmg 被推迟，直到签名和公证落地。

Chama 现在与 Mostro 和 Shopstr 一起加入 Nostr 原生市场，以无服务器架构、Fedimint 支持的 2-of-3 Shamir 托管、仅持有者共享加密而与众不同，是三者中唯一发布不带协调社区的自包含桌面和移动 client 的项目。

### Coracle Hosting：付费 relay 服务加开源 Caravel 栈

6 月 3 日 Hodlbod 在 [hosting.coracle.social](https://hosting.coracle.social) [宣布 Coracle Hosting](https://nos.lol/e/f8586160cd12df479c261397353c99e6f3e4d870b616382e1b4338bad3ab498a)，一个托管的社区 relay 服务，接受通过 NWC 或卡的定期 lightning 支付。该服务由 Coracle 的计费和配置前端 [Caravel](https://gitea.coracle.social/coracle/caravel) 以及在单个机器上托管多个虚拟 relay 的 relay 运行时 [zooid](https://gitea.coracle.social/coracle/zooid) 提供支持。两者都在 Coracle 的自托管 gitea 上开源。Caravel 附带可选的 [livekit](https://livekit.io) 和 [Blossom](/zh/topics/blossom/) 集成，运营者可以每 relay 切换。带有成员数量限制的免费层允许运营者在提交支付详细信息之前评估服务。

Hodlbod 对商业模型很坦率：通过出售任何其他人也可以运行的栈的托管版本来将开源货币化。竞争护城河是 [Flotilla](https://flotilla.social) 集成，这是下一个计划的步骤。Flotilla 拥有用户接口，因此从 Flotilla 内部提供的托管选项成为任何喜欢管理基础设施的用户的默认路径。Hodlbod 提议如果其他 Caravel 运营者伸出援手，就将他们添加到 Flotilla 的替代托管选择器中，为联邦托管市场保留了大门。

Caravel 加入 [relay.tools](https://relay.tools) 作为具有付费成员层的公共 Nostr relay 配置平台。relay.tools 早于 Caravel，作为今天占主导地位的 relay 创建者服务发布，具有自己的社区 relay 目录以及付费成员或版主加入流程。Caravel 的独特功能是协调栈：relay 运行时（zooid）、计费和配置前端（Caravel 本身）以及 client 端选择器（Flotilla 集成，仍在进行中）作为一个设计发布。另一个独特功能是 zooid 的多 relay 每进程密度，客户 relay 共享单个主机进程，因此运营者在许多小型社区中分摊托管成本。这是使共享 Web 托管在 2000 年代初期可行的相同密度论点，应用于 Nostr 的 relay 层。

## 发布

### Angor v0.2.29 和 v0.2.30：默认主网和 3 用户 UAT 资金测试

6 月 4 日的 [Angor v0.2.29](https://github.com/block-core/angor/releases/tag/v0.2.29) 和 6 月 8 日的 [v0.2.30](https://github.com/block-core/angor/releases/tag/v0.2.30) 是本周去中心化 Bitcoin 和 Nostr 资助协议的两个版本。v0.2.30 的头条变更是 [PR #893](https://github.com/block-core/angor/pull/893)，它将默认网络切换到主网。Angor 仍作为不稳定的 alpha 版本发布，但默认主网切换标志着协议对桌面和移动 client 已经超过了仅测试网阶段。v0.2.30 还落地了带有图像上传和滚动重置的单点触摸移动创建项目流程（[PR #889](https://github.com/block-core/angor/pull/889)）并解决了 lightning invoice 转轮可能挂起的竞态条件（[PR #890](https://github.com/block-core/angor/pull/890)）。

v0.2.29 在 [PR #881](https://github.com/block-core/angor/pull/881) 中添加了端到端 UAT 测试，涵盖 10 轮 3 用户发送资金，带有未确认支出，是 Angor 测试套件中第一个多用户资金流测试。该版本还添加了 Angor CLI 和 MCP 服务器的实现计划（[PR #792](https://github.com/block-core/angor/pull/792)），并在 [PR #880](https://github.com/block-core/angor/pull/880) 中为 MCP 测试工作流程改进 CLI。DavidGershony 的 [PR #885](https://github.com/block-core/angor/pull/885) 修复了在运行时网络切换后使用错误网络的 Boltz lightning invoice，这是一个在 v0.2.30 主网默认之后将在生产中浮现的 bug。设置现在提供在数据擦除期间可选的恢复钱包文件清除（[PR #883](https://github.com/block-core/angor/pull/883)）。

### Sprout v0.3.15：临时 channel TTL 刷新和 ACP 斜杠命令

6 月 10 日发布的 [Sprout v0.3.15](https://github.com/block/sprout/releases/tag/v0.3.15) 是从 6 月 2 日 v0.3.7 开始的一系列版本中的第八个版本。Newsletter #25 涵盖了 v0.3.1 到 v0.3.6 的运行，包括 mesh-llm 集成和 channel 部分工作；v0.3.7 到 v0.3.15 是下游的，专注于打磨和一些面向用户的新增功能。最面向用户可见的变化是 [PR #902](https://github.com/block/sprout/pull/902) 中临时 channel 的 TTL 刷新：当用户取消归档临时 channel 时，Sprout 延长 channel 的生存时间，因此取消归档不会立即在原始到期计时器下重新归档。移动自定义 emoji 在 [PR #906](https://github.com/block/sprout/pull/906) 中与设置重新设计一起到达，反应计数现在在变化时动画化（[PR #904](https://github.com/block/sprout/pull/904)）。

[PR #905](https://github.com/block/sprout/pull/905) 修复了一个长期存在的差距，即多词显示名称被破坏，以及 [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) `nostr:npub` mention 提取静默丢弃。桌面的目录支持团队 UI 在 [PR #912](https://github.com/block/sprout/pull/912) 中发布，具有 install、sync 和 reveal 命令。Slash 命令现在在 [PR #919](https://github.com/block/sprout/pull/919) 中传递给 [ACP](https://agentclientprotocol.com) 连接器，让 Sprout 将 `/help` 风格的命令直接转发到 agent 运行时，同时 Sprout UI 保持在路径之外。

### Wisp v1.1.1：Spark 钱包集成和 nsec 粘贴防护

6 月 5 日发布的 [Wisp v1.1.1](https://github.com/barrydeen/wisp/releases/tag/v1.1.1) 在 [PR #548](https://github.com/barrydeen/wisp/pull/548) 中落地了一个带有 [Spark](https://www.spark.money) 子屏幕的两层钱包 Connect 屏幕，并在 [PR #549](https://github.com/barrydeen/wisp/pull/549) 中与 iOS 钱包 UI 的仪表板对等。该版本包括一个系统范围的 [nsec 粘贴防护](https://github.com/barrydeen/wisp/pull/553)，检测应用中任何地方的 `nsec1` 前缀粘贴，并阻止字段接受它，关闭了 Nostr UX 中最常被引用的坑之一。QR 扫描登录加上用于 `npub` 和 `nprofile` 的仅观看模式在 [PR #552](https://github.com/barrydeen/wisp/pull/552) 中发布，让用户可以只读浏览个人资料。Zap 消息现在作为迷你帖子在参与抽屉中渲染（[PR #559](https://github.com/barrydeen/wisp/pull/559)），因此 zap 笔记与 sat 金额一起承载其文本。线程回复的 web-of-trust 过滤器在 [PR #583](https://github.com/barrydeen/wisp/pull/583) 中落地，让用户可以隐藏来自其关注图之外的账户的回复垃圾邮件。

### Nostria v3.1.46 和 nospeak 1.1.3：通知重做和 ICE 重启

6 月 7 日的 [Nostria v3.1.46](https://github.com/nostria-app/nostria/releases/tag/v3.1.46) 结束了三个版本的运行，重新设计了通知计数器，仅计算自上次查看以来的新通知，消除了长期存在的通胀，即通过滚动加载较旧的通知会增加徽章计数。[Nostria v3.1.45](https://github.com/nostria-app/nostria/releases/tag/v3.1.45) 修复了影响 lightning 和 QR code 支付的分成支付 bug，并放弃了以前计划的半透明 UI，因为在 Android 的合成器上不可行。

6 月 4 日的 [nospeak v1.1.3](https://github.com/psic4t/nospeak/releases/tag/v1.1.3) 在 FAILED 状态下为 1 对 1 语音通话添加 ICE 重启。标准 WebRTC 行为在 ICE 候选超时且没有替代路径时丢弃通话；ICE 重启路径重新协商候选，因此通话从瞬态 NAT 或网络变化中恢复。Android 通话现在在视频通话期间保持屏幕开启。

## 未发布的更改

### Amethyst：41 个 PR 继续 NIP-32 / NIP-F4 / Tor 轨道

Amethyst 本周合并了 41 个 PR，没有削减版本标签，在上周的 52 个 PR 以及 Newsletter #25 中涵盖的 [NIP-32](/zh/topics/nip-32/) hashtag 标签和 [NIP-F4](/zh/topics/nip-f4/) 播客工作之上。活跃分支继续为下一个带标签的版本累积功能，在上周的头条新增功能之上分层打磨：hashtag labeler 发现、播客屏幕、音乐曲目和播放列表、Tor 自愈看门狗、匿名上传的临时 signer，以及带有 NIP-05 过滤的链上 zaps。Amethyst 的 PR 吞吐量仍然是所有 Nostr client 中最高的，未发布的队列是其他 Android Nostr client 需要匹配的事实上的路线图。

### Damus：从 OK 消息进行 relay 跟踪和 v1.17 变更日志

6 月 3 日合并的 [Damus PR #3786](https://github.com/damus-io/damus/pull/3786) 将来自 relay 的成功 `OK` 消息添加到帖子 relay 列表。较早的 Damus 构建仅在从 relay 收到通用消息时填充所见 relay 列表，这意味着确认帖子但未传回任何事件的 relay 对用户不可见。此变更对希望确认帖子已到达其首选发件箱 relay 的用户很重要。[PR #3796](https://github.com/damus-io/damus/pull/3796) 修复了 Profile View 上的 `AttributeGraph` 循环，[PR #3725](https://github.com/damus-io/damus/pull/3725) 在下一个带标签的版本之前落地了 v1.17 变更日志。

### Shopstr：NIP-34 双重发布

Shopstr 的 [ngit 上的 shopstr repo](https://relay.ngit.dev/npub1u350hpq840naxzkkle4gmdtvzanfxmjd9m9tytn5355aua7jh2cqgfuw39/shopstr.git) 本周在 Nostr 上被宣布为 [NIP-34](/zh/topics/nip-34/) git repo，加入 ngit 跟踪的 repo。shop client 的 GitHub repo 仍然是主要的开发接口；NIP-34 公告使得并行的 git-over-Nostr 协作路径可用。这是继 [Mostro](https://relay.ngit.dev/) 之后第二个双重发布到 NIP-34 的主要 Nostr 市场项目，并继续将项目元数据逐步迁移到 Nostr 的 git 传输上。

### Hermes-Marmot：MLS 之上的 AI agent 网关

[hermes-marmot](https://github.com/notmandatory/hermes-marmot) 是 [Hermes Agent](https://github.com/NousResearch/hermes-agent) 的插件，使用 [mdk-python](https://github.com/marmot-protocol/mdk-python)（Rust Marmot Development Kit 的 Python 绑定）将 AI agent 的消息接口连接到 [Marmot](/zh/topics/marmot/)（MLS-over-Nostr）群组。该插件让用户可以从任何说 kind 445 MLS 消息的 Nostr client（包括 [Whitenoise](https://whitenoise.chat)）向 AI agent 发送 DM。入站 DM 通过 [nostr-sdk](https://github.com/rust-nostr/nostr) Python 绑定使用 [NIP-59](/zh/topics/nip-59/) gift-wrap 解包，入站 welcomes 通过 `UnwrappedGift.from_gift_wrap` 流向 `mdk.process_welcome` 和 `mdk.accept_welcome`。访问控制通过 `MARMOT_ALLOWED_USERS`（一个逗号分隔的 npub 白名单）或用于开放开发访问的 `MARMOT_ALLOW_ALL_USERS=true` 运行。

该 repo 是新的（最近更新为 5 月 27 日）且小。其重要性是架构性的：它是 LLM agent 运行时与 MLS 加密的 Nostr 消息通道之间的第一个公共桥接，也是 mdk-python 在 Whitenoise 之外的第一个生产使用。该模式指向 agent-to-agent 通信，其中两个端点持有 MLS 密钥，relay 仅看到密文。

## NIP 更新和协议规范工作

### NIP-67 EOSE 完整性提示（PR #2317）合并

mattn 的 [PR #2317](https://github.com/nostr-protocol/nips/pull/2317) 于 6 月 6 日合并，将 [NIP-67](/zh/topics/nip-67/) 添加到协议中。该 NIP 使用可选的第三个元素扩展 `EOSE` relay 消息：`["EOSE", <subscription_id>, "finish"]` 表示已交付匹配过滤器的每个已存储事件，而裸的 `["EOSE", <subscription_id>]` 不携带完整性声明。省略提示的 relay 告诉 client 可能有更多；在 NIP-11 中省略 NIP-67 公告的 relay 保持当前行为，采用现有的旧启发式方法。该变化在两个方向上都向后兼容：旧 client 忽略尾随的数组元素，旧 relay 省略它。

合并规范中的动机是双重的。首先，静默数据丢失：client 向一个内部 300 事件上限的 relay 请求最新的 500 条笔记，relay 返回 300 个事件，client（使用标准 `received < limit` 启发式方法）得出结果完整的结论。第 201 个到第 N 个最旧的匹配笔记停留在 relay 上未读，client 对这一事实一无所知。其次，强制浪费的往返：当 relay 将响应限制在 300 个事件时，任何耗尽上限的订阅都需要第二个 `REQ`，带 `until=<oldest_created_at>`，纯粹用于确认完成，即使过滤器恰好匹配 300 个事件。这两种失败模式都由每个 cap-exhausted 订阅上的每个 client 支付。`"finish"` 提示是一个现有消息上的一个可选字符串，消除了两个成本。

### NIP-50 autocomplete 扩展（PR #2357）合并

Alex Gleason 的 [PR #2357](https://github.com/nostr-protocol/nips/pull/2357) 于 6 月 6 日合并，向 [NIP-50](/zh/topics/nip-50/) 搜索添加了 `autocomplete:true/false` token。该扩展让 client 可以将查询标记为 typeahead 查找，因此 relay 使用前缀匹配，对于没有 token 的查询默认为全文搜索。Ditto 的 relay 为 follow packs、lists 和任何带有 `title` 标签的事件实现它，返回与 title 前缀匹配的结果；默认搜索路径运行全文评分。没有此 token，autocomplete 风格的 UI 无法传达前缀搜索意图，而 relay 必须从查询形状猜测。该 token 是每搜索提示，而不是 relay 范围的能力，因此 relay 可以为一个事件类（标题）实现它，而无需声明一般的 autocomplete 支持。

### NIP-GART 紧急警报和位置广播（PR #2374）

由 disinqa 于 6 月 9 日打开的 [PR #2374](https://github.com/nostr-protocol/nips/pull/2374) 定义了 Nostr 上用于紧急警报和寻址到一组可信接收者的位置广播的隐私保护 wire 格式。声明的设计目标是隐藏发送者身份、群组成员身份和 payload，使其对 relay 运营者不可见，同时保持事件在端到端上重放安全和签名可验证。NIP 编号仍待定，提议为早期草案。用例是标准的紧急警报模式：受威胁的用户广播一个位置 ping，只有预共享的可信联系人组可以解密，relay 对发送者、接收者集和 payload 视而不见。Wire 格式细节存在于 PR 中，并可能随着维护者审查而演变。

### NIP-46 logout 方法（PR #2373）

由 hzrd149 于 6 月 8 日打开的 [PR #2373](https://github.com/nostr-protocol/nips/pull/2373) 向 [NIP-46](/zh/topics/nip-46/) 添加了 `logout` 方法，因此 client 可以明确告诉 bunker 会话已结束。到目前为止，结束 bunker 会话的唯一方法是等待会话超时或停止使用连接，两者都让 bunker 为已消失的 client 保留会话状态。该提议很短（一个新方法），是使长期 bunker 集成更清洁的那种家务整理变更。

### NIP-95 混合 relay-P2P 提议作为长文流传

一份长文 [NIP-95 规范](https://github.com/nostr-protocol/nips) 以 6 月 4 日来自 npub `91bea5cd9361504c409aaf459516988f68a2fcd482762fd969a7cdc71df4451c` 的 `kind:30023` 帖子形式流传，标题为 *Protocolo Híbrido Relay-P2P via WebRTC*。该葡萄牙语文档定义了一种混合 P2P relay 协议，其中 Nostr client 通过 WebRTC 直接相互连接进行实时消息传递，同时继续使用 relay 进行存储事件检索和离线交付。作者明确将规范定为"LLM 就绪"，提供消息定义、逻辑流程、数据模式和状态规则，其详细程度让 AI 模型能够生成工作 client 或服务器代码。该提议尚未作为 NIP PR 落地；通过 `kind:30023` 流传是正式 nostr-protocol/nips pull request 的惯常前驱。

### NIP-44 v3 获得第二个 signer：Clave 移植规范

[上周 Amber 的 v6.2.0 NIP-44 v3 推出](/zh/newsletters/2026-06-03-newsletter/#nip-44-v3-amber-implementation-ahead-of-spec) 在任何合并的 NIPs PR 之前发布，让 v3 作为 Amber 特定的扩展留下，其他 client 必须镜像才能互操作。那种单一实现的框架在本周发生了变化。[Clave](https://github.com/DocNR/clave) 是基于推送的 iOS NIP-46 远程 signer，于 6 月 3 日和 4 日在八个 commits 中落地了一个独立的 NIP-44 v3 端口。加密原语在三个 commits 中发布：[HKDF + ECDH 密钥层](https://github.com/DocNR/clave/commit/99ca5a5aacb501d1666c489fcdea30187c7853fa)、[v3 padding 算法](https://github.com/DocNR/clave/commit/8808cdca54d32b4ae57856bd4b07ed73a45e8e5c)，以及一个 [顶层公共 API 加加密 Context](https://github.com/DocNR/clave/commit/ae1f506a53cb2c8aa16523540dbe790876c1839e)。在这些之上，NIP-46 接口跟随 [LightSigner 内部的 RPC 分派布线](https://github.com/DocNR/clave/commit/f37aa1afc8368862fc3ebac533408442349bfc38) 和 [携带 v3 上下文（kind 加 scope）的 PendingRequest 模式](https://github.com/DocNR/clave/commit/e51bcb49fc61cfa89b6030d61b203e046aeddb0a)，因此 signer 可以记录 v3 payload 被批准的事件 kind 和用例。

Clave 在面向用户的接口上与 Amber 分歧。[带有敏感性层的权限授予模式](https://github.com/DocNR/clave/commit/0a8b7de63c1f2994a80a66bf139ec519fab12877) 让用户可以在选择的敏感性级别为特定事件 kind 和 scope 授予 v3 加密。首次遇到时，[带有一次性解释卡的 v3 上下文感知批准提示](https://github.com/DocNR/clave/commit/2cf563cb15b0406f5e8aaa0b4e34b887ff1896a1) 向用户介绍 v3。该工作在 main 中，并 [连接到 Xcode 项目](https://github.com/DocNR/clave/commit/4bd0c26d7cf308386ef15e5d96ee5673d6db2d4a)，但未发布；最近的带标签构建是 5 月 12 日的 [v0.2.0-build79](https://github.com/DocNR/clave/releases/tag/v0.2.0-build79)。

两个独立的实现在 NIPs PR 合并之前在生产路径中落地了 NIP-44 v3，这加强了协议 PR 将正式化的底层 wire 格式的案例。跨实现互操作性测试现在成为规范收敛的路径，Amber 的 Android 批准接口和 Clave 的 iOS 敏感性层模型作为两个参考点。连接 v3 的其他远程 signer（nsec.app 的 noauth 自 2025 年 5 月以来一直处于休眠状态，其他 bunker 尚未宣布 v3 工作）将进一步收紧共识。

### NIP-34 活动：Iris 采用带有新 hashtree 传输的栈

Iris 于 6 月 8 日发布了 [`hashtree`](https://njump.me/nevent1qqs8kmy7a9dn5awurlp9q26lsaetl7dc4wauzdl8ww68dzmn09e074gpzfmhxue69uhhgetdwqhxjunfwvh8gmc850du0) 的 NIP-34 repo 公告，并于 6 月 9 日发布了 [`iris-apps`](https://njump.me/nevent1qqsq4grx000f6p0r8hdv4lqhcgn7707vmktv2j528kn0ldps4y9g49qpzfmhxue69uhhgetdwqhxjunfwvh8gmcmq47as)、[`iris-drive`](https://njump.me/nevent1qqsyj5r0tyqvpp9v7qnras90u6kzqtpqx6ktntwym66m8qyngvf59vqpzfmhxue69uhhgetdwqhxjunfwvh8gmcpts6pf) 和 [`iris-chat-rs`](https://njump.me/nevent1qqs0x98hpsv8vmrxvwm2rs9exxttrue5qv5p2n2sqjeylz2kgdmd7tgpzfmhxue69uhhgetdwqhxjunfwvh8gmca8783s) 的 NIP-34 repo 公告，广告克隆 URL 使用新的 `htree://` 方案，从 `wss://temp.iris.to` 提供。Hashtree 传输是 GRASP 路由克隆的内容寻址替代方案，这四个公告是其首次公开使用。该 repo 携带空描述，架构细节仍在浮现，但通过 NIP-34 公告（而不是自定义 Iris 内部清单）发布的选择表明 Iris 正在承诺更广泛的 NIP-34 git-over-Nostr 栈。

## NIP deep dive：NIP-67（EOSE 完整性提示）

[NIP-67](/zh/topics/nip-67/) 关闭了 [NIP-01](/zh/topics/nip-01/) 中最长期存在的正确性差距之一。原始规范将 `EOSE` 定义为 `REQ` 的已存储事件与实时订阅事件之间的边界，但它从未指定 relay 是否已完成交付所有已存储的匹配项，或者是否由于内部上限而中途停止。每个 relay 都强制执行每订阅上限（通常为 300 到 1000 个事件），独立于 client 的 `limit`，client 无法观察该上限。

标准的解决方法是将接收的计数与请求的 `limit` 进行比较。如果 `received < limit`，将结果视为完整；否则使用 `until=<oldest_created_at>` 分页。两个分支都是坏的。`received < limit` 分支静默截断：client 向上限为 300 的 relay 请求 500 条笔记，看到 300 个事件，因为 `300 < 500` 而得出结果完整的结论，从不获取其余部分。relay 上保留的事件无法通过任何现有消息发出"更多可用"的信号。作为第二个分支的分页是浪费的：匹配上限的过滤器需要第二个 `REQ` 来确认完整性，返回零个事件，同时在 relay 上消耗完整的过滤器扫描。

NIP-67 的修复是 `EOSE` 消息上的一个可选字符串：

```
["EOSE", "<sub_id>", "finish"]   // 显式：所有已存储事件已交付
["EOSE", "<sub_id>"]              // 无完整性声明
```

在 [NIP-11](/zh/topics/nip-11/) `supported_nips` 中通告 NIP-67 并发出裸 `EOSE` 的 relay 告诉 client 还有更多。省略公告的 relay 保持当前行为，client 回退到现有的启发式方法。旧 client 忽略尾随的数组元素。向后兼容性在两个方向上都成立，没有新的动词或事件 kind。

使 NIP-67 值得研究的是它有意限制的范围。规范未定义 cursor 或分页 token，因此基于 `until` 的分页仍然是机制。Relay 上限保持原状，NIP 不要求暴露它们。NIP-67 保留了 `EOSE` 作为 stored-to-live 边界的含义，并且仅在边界添加了是或否的信号："我还有更多给你"与"就这些了"。这个最小接口是为什么 PR 在对 NIP-01 扩展相对较短的审查期后合并的原因，也是为什么 mattn 在 PR 中明确指出英文文本使用了 AI 翻译。变化足够小，翻译不确定性无关紧要。

client 与强制执行上限的 relay 之间的 NIP-67 感知交换示例。来自 relay 的 NIP-11 公告：

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1781136000,
  "kind": 11,
  "tags": [],
  "content": "{\"supported_nips\":[1,11,50,67]}",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

跟随的 wire 级别交换：

```
→ ["REQ", "abc", {"kinds":[1],"limit":500}]
← [...300 EVENT 消息...]
← ["EOSE", "abc"]               // 无 "finish": 达到上限，还有更多可用
→ ["REQ", "def", {"kinds":[1],"limit":300,"until":1780900000}]
← [...178 EVENT 消息...]
← ["EOSE", "def", "finish"]     // 显式完成
```

178 事件响应此前会触发第三个 `REQ` 来确认完成。使用 NIP-67，client 在那里停止。

NIP-67 作为一个罕见共识落地的 NIP-01 修正案也值得注意。大多数 NIP-01 变更都吸引长期辩论线程，因为该协议的微小接口对每个实现都至关重要。NIP-67 在延长的审查期后合并（从打开到合并大约七周），表明当 NIP-01 变更足够小且失败模式足够具体时（静默数据丢失、强制浪费的往返），协议的维护者愿意扩展核心消息词汇。

## NIP deep dive：NIP-50（Search）

[NIP-50](/zh/topics/nip-50/) 定义了 `REQ` 消息中的 `search` 过滤器字段，让 client 可以要求 relay 通过对查询字符串进行全文匹配来过滤事件。合并的基础规范有意最小化：`search` 字段是一个字符串，每个 relay 决定自己的搜索语义（哪些字段被索引、评分如何工作、是否应用词干提取），并且 relay 在其 NIP-11 文档中通告 NIP-50 支持。client 仅通过查询字符串本身控制搜索算法。

这种极简主义既是 NIP-50 的优势，也是其约束。优势是任何 relay 都可以在任何质量级别实现搜索：基本的子字符串扫描满足规范，运行 Elasticsearch 或 Meilisearch 的 relay 同样满足它。约束是 client 缺乏表达搜索意图的方式。个人资料 mention typeahead UI 想要针对显示名称的前缀匹配；全文内容搜索想要跨笔记正文的分词全文评分。相同的 `search` 字段承载两者，relay 必须从查询形状猜测。

[PR #2357](https://github.com/nostr-protocol/nips/pull/2357) 添加了第一个 NIP-50 扩展 token：嵌入在搜索查询中的 `autocomplete:true` 或 `autocomplete:false` 表示 client 想要哪种模式。Ditto 的 relay 为 follow packs、lists 和任何带有 `title` 标签的事件实现该 token，当 `autocomplete:true` 存在时切换到前缀匹配。该 token 内联存在于查询中（独立的过滤器字段保持不变），因此它随搜索字符串一起传输，不需要 wire 协议凸起：

```
search: "fiat autocomplete:true"
```

像这样的 token 形状提示是 NIP-50 一直处理 relay 特定方言的方式。Relay 已经支持像 `language:en` 和 `domain:example.com` 这样的 token。每个都保持 relay 特定，每个 relay 都记录自己的方言。NIP-50 的 PR #2357 将 `autocomplete` 从 relay 私有 token 提升为规范祝福的 token，为跨 relay 的 typeahead 感知搜索铺平了道路。

带有 autocomplete token 的 NIP-50 `REQ` 示例，针对索引 kind 0 profile 标题的 relay：

```json
{
  "id": "b7c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f7081a2b3c4d5e6f70819a2b3c4d5",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1781136000,
  "kind": 1,
  "tags": [
    ["client", "example-mention-picker"]
  ],
  "content": "Sent search: kinds=[0], search=\"fiat autocomplete:true\", limit=10",
  "sig": "12d3e4f5061728394a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f7081a2b3c4d5e6f70819a2b3c4d5e6f7081a2b3c4d5e6f708192"
}
```

实际的 wire 级 REQ：

```
["REQ", "mention-picker", {"kinds":[0],"search":"fiat autocomplete:true","limit":10}]
```

不识别该 token 的 relay 将 `autocomplete:true` 视为字面搜索字符串的一部分，回退到全文匹配，返回正确的（如果排名不同）结果。优雅的降级使得对于喜欢在可用时使用前缀匹配的 client 无条件包含该 token 是安全的。

下一个可能的 NIP-50 扩展是每 kind 排名控制：一个提示，表示"按 `created_at` 降序排名"与默认相关性评分。几个 relay 已经接受 `sort:newest` 作为 relay 私有 token，将 `autocomplete` 带入规范的相同提升路径适用。搜索仍然是少数几个 relay 在结果质量上竞争的 Nostr 原语之一；交付的可靠性在所有符合规范的 relay 中相同。增量 token 让 client 可以利用该质量竞争，而无需强迫 relay 发布重量级的新规范。
