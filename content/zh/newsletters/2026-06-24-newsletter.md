---
title: "Nostr Compass #28"
date: 2026-06-24
publishDate: 2026-06-24
translationOf: /en/newsletters/2026-06-24-newsletter.md
translationDate: 2026-08-27
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的 Nostr 每周指南。

**本周：** [Sprout 更名为 Buzz](#sprout-rebrands-to-buzz-and-publishes-personas-teams-and-managed-agents-as-relay-events)，并开始将 persona、团队与托管 agent 记录发布为 Nostr 中继事件；跨设备已读状态和逐消息已读标记取代旧有的徽标前沿模型。sandwich.farm 推出 [Napplets](#napplets-composable-nostr-apps-with-a-defined-trust-boundary)，这是一个面向可组合 Nostr 应用的信任边界协议，应用通过 Nostr 与 Blossom 分发。[Conduit](#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default)（Nostr 上由三个应用组成的市场 monorepo：买家市场、商户门户、店铺构建器，仓库内自带 NIP 与规范目录）合并 17 个 PR，加固市场 MVP，默认改用其公共中继，并加入保护隐私的分析功能。[BitBlik](#bitblik-launches-a-p2p-blik-to-lightning-exchange-protocol-over-nostr) 发布通过加密 Nostr 私信运行的 P2P BLIK 至 Lightning 兑换协议，由协调器在法币与 Lightning hold invoice 之间进行原子结算。[Amethyst](#amethyst-patches-follow-up-the-v1120-launch) 延续上周的钱包、播客与锻炼功能发布，加入 Health Connect Workouts、Road Events、可折叠回复、带分类器的中继延迟健康跟踪，以及 macOS 公证修复。[Amber](#amber-implements-nip-46-client-metadata) 实现上周提出的 NIP-46 客户端元数据扩展，在签名器请求界面显示原生应用图标与身份信息。[Haven](#haven-launches-private-location-sharing-on-marmot) 在 Marmot 加密消息协议上推出私密位置共享。[CodeDeck](#codedeck-remote-agentic-coding-over-nostr) 让用户通过加密 Nostr 中继，用手机控制笔记本上的 Claude Code 会话；随后把配对简化为扫描一个二维码，并加入逐会话模型选择。[Grain](#grain-ships-a-full-nostr-client-engine) 发布可导入、支持 outbox 模型的 Go Nostr 客户端库。Mostro Core、Wisp 与 Dark Wisp、Citrine、FIPS、Kubo（家长精选 YouTube 频道与强制信任门禁儿童信息流）以及 Pollerama（web-of-trust 分数、设备端中继引擎和“你可能认识的人”横栏）也发布后续补丁。未发布工作涵盖 sandwich.farm 的浏览器端 MLS 协调器、nostter 的 UX 迭代冲刺、Zap Cooking 的跨项目 NIP-46 修复与编辑器重构、Shopstr 的 Cashu 托管生命周期、divine.video 和 Nostur。新纳入跟踪的项目包括 Social Agents Prototype、用于 git-over-Nostr issue 分流的 PRana，以及 routstr-chat。协议方面，NIP-99 新增一项链上图 checkout 与托管提案，直接对应 Conduit、BitBlik 和 Shopstr 的商务工作。由于这是六月最后一期 Compass，本期以 [Nostr 六年六月史](#six-years-of-nostr-junes)收尾。

---

## 头条新闻

### Amethyst v1.12.1 至 v1.12.6 跟进 v1.12.0 发布 {#amethyst-patches-follow-up-the-v1120-launch}

[Amethyst](https://github.com/vitorpamplona/amethyst) 在[上周发布 v1.12.0](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)之后，于周三至周五迅速发布六个补丁。[v1.12.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.1) 增加 Health Connect Workouts 与 Share-as-Image 操作，并让 Tor 的 `Active` 标志具有确定性，使引导回调无法与门禁发生竞态。[v1.12.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.2) 增加 Road Events 与可折叠回复；[v1.12.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.3) 加入带分类器和仪表板 UI 的中继延迟健康跟踪，并修复 macOS 公证；[v1.12.4](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.4) 至 [v1.12.6](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.6) 则带来 Crowdin 翻译更新与译者署名自动化。

### Sprout 更名为 Buzz，并将 persona、团队与托管 agent 发布为中继事件 {#sprout-rebrands-to-buzz-and-publishes-personas-teams-and-managed-agents-as-relay-events}

[Sprout](/en/newsletters/2026-04-29-newsletter/#sprout-adds-owner-attestation-and-multi-workspace-support) 是 Block 可自托管的工作空间，人类与 AI agent 在同一频道协作，每条消息、reaction、工作流步骤、审核批准与 git 事件都写成已签名 Nostr 事件；本周它更名为 [Buzz](https://github.com/block/buzz)。GitHub 现将旧的 `block/sprout` slug 重定向到 `block/buzz`；仓库、许可证与产品方向均未改变。往期对 Sprout 的报道都指向同一项目。

更名同时伴随大量产品工作。通过 [PR #1189](https://github.com/block/buzz/pull/1189)，persona、团队与托管 agent 记录现在发布为 Nostr 中继事件，使同一 agent 身份可以出现在多个工作空间和审计日志中，而无需复制状态。新的桌面窗格在个人资料上显示 NIP-OA 所有者证明（[PR #1198](https://github.com/block/buzz/pull/1198)）；频道线程的未读徽标前沿被逐消息已读标记取代，使未读计数在设备间保持准确（[PR #1178](https://github.com/block/buzz/pull/1178)）；收件箱则在提醒事件中增加作者与来源归属信息（[PR #1176](https://github.com/block/buzz/pull/1176)）。

临时频道现在默认 7 天后过期（[PR #1182](https://github.com/block/buzz/pull/1182)）；逐 agent 中继覆盖会先采用已配置的中继，再回退到工作空间默认值（[PR #1131](https://github.com/block/buzz/pull/1131)）；Windows 构建现为 shell 工具捆绑完整的 Git for Windows 工具链（[PR #1145](https://github.com/block/buzz/pull/1145)）。

### Napplets：具有明确信任边界的可组合 Nostr 应用 {#napplets-composable-nostr-apps-with-a-defined-trust-boundary}

Sandwich.farm 本周宣布推出 [napplet.run](https://napplet.run)，它是一项面向可组合 Nostr applet（即 napplet）的协议：这些微型程序各自只做一件事，在沙箱环境中运行，并采用与 nsite 相同的事件形状经 Nostr 与 Blossom 解析。项目分布在三个仓库中：[napplet/web](https://github.com/napplet/web) 包含 web 软件包，本周协同发布时为 51 个子软件包打了版本 tag（`@napplet/core`、`@napplet/sdk`、`@napplet/nap`、`@napplet/shim`、`@napplet/conformance`）；[napplet/naps](https://github.com/napplet/naps) 是 NAP 规范轨道，合并了 15 个 PR；[kehto/web](https://github.com/kehto/web) 是 web 运行时，合并了 41 个 PR，并在 [kehto.github.io/web/playground](https://kehto.github.io/web/playground) 提供 playground。对应的规范 PR 是 dskvr（sandwich.farm）发起的 [NIP-5D #2303](https://github.com/nostr-protocol/nips/pull/2303)。

其架构前提是在协议层定义信任边界。shell 代理危险操作（签名、密钥访问、中继写入），runtime 负责实现与更高层 UX，而 napplet 保持可移植、可丢弃，也更难被任何单一宿主控制。napplet 可以在同一 shell 中彼此通信，且设计上不存在 runtime 锁定。作者将 napplet 与 Pablof7z 的 NMP、Soapbox 的 Tiles 放在一起讨论，把它们定位为同一问题的并行解法，并指出 Amethyst v1.12.6 对 [NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) 与 [NIP-5D](/zh/topics/nip-5d/) 的支持，使 napplet 在发布时至少已有一个实际交付的客户端。项目还给出一条历史脉络：sandwich.farm 较早的 `napp.run`（NIP-07 原生应用原型）和 Thorium 分支 `dryft` 浏览器都影响了当前设计，之后则被搁置。

### Conduit 加固市场 MVP，并默认切换至其公共中继 {#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default}

[Conduit](https://github.com/Conduit-BTC/conduit-mono) 是 [conduit.market](https://conduit.market) 的三应用市场 monorepo（买家 Market、Merchant Portal、Store Builder），隶属 `Conduit-BTC` 组织，仓库内自带 `nips/` 与 `specs/` 目录，用来定义 Conduit 特有的 Nostr 商务原语；底层运行的是 [Conduit-BTC/conduit-relay](https://github.com/Conduit-BTC/conduit-relay) Scope-2 [khatru](https://github.com/fiatjaf/khatru) 扩展。两个仓库均于今年早些时候开放；本周项目合并 17 个 PR，加固市场 MVP。

已交付的 PR 主要围绕市场正确性：listing 安全状态（[PR #110](https://github.com/Conduit-BTC/conduit-mono/pull/110)），以及商户侧的产品定价与配送区域加固（[PR #115](https://github.com/Conduit-BTC/conduit-mono/pull/115)）。中继侧，[PR #102](https://github.com/Conduit-BTC/conduit-mono/pull/102) 修正商务能力检测，[PR #112](https://github.com/Conduit-BTC/conduit-mono/pull/112) 忽略第三方不安全中继提示，[PR #128](https://github.com/Conduit-BTC/conduit-mono/pull/128) 则将 Conduit 公共中继域名设为新客户端的默认值。保护隐私的分析功能见于 [PR #109](https://github.com/Conduit-BTC/conduit-mono/pull/109) 与 [PR #129](https://github.com/Conduit-BTC/conduit-mono/pull/129)，一次 `dompurify` 升级关闭了 OSV 安全通告（[PR #116](https://github.com/Conduit-BTC/conduit-mono/pull/116)）。这些工作处于本周更广泛的 [NIP-99](/zh/topics/nip-99/) 商务浪潮中：[PR #2323](https://github.com/nostr-protocol/nips/pull/2323) 提议为 NIP-99 市场加入涵盖订单流程、托管与争议的链上图 checkout 层；长期存在、将 NIP-99 扩展至完整电商的 [Gamma Markets Market Spec](https://github.com/GammaMarkets/market-spec) 成为 Conduit 等项目依托的规范层；Shopstr 也在同一周交付 Cashu 托管生命周期。

### BitBlik 在 Nostr 上推出 P2P BLIK 至 Lightning 兑换协议 {#bitblik-launches-a-p2p-blik-to-lightning-exchange-protocol-over-nostr}

[BitBlik](https://github.com/bit-blik/bitblik) 本周以基于 Nostr 的点对点 BLIK ↔ Lightning 兑换协议首次公开。BLIK 是波兰银行发行的即时支付方案；BitBlik 协调器在 BLIK 法币（由 taker 支付）与 Lightning hold invoice（由 maker 注资）之间进行原子结算，交易生命周期通过 Nostr 运行。Flutter 应用、CLI 与协调器共用一个 `core` 软件包；项目通过 GitHub monorepo `bit-blik/bitblik`、[www.bitblik.app](https://www.bitblik.app) web 构建和 Zapstore 应用 `app.bitblik` 发布。

协议使用加密 Nostr 私信（[NIP-44](/zh/topics/nip-44/)）承载客户端与协调器之间的 RPC。offer 以 kind `38383` 的参数化可替换事件发布，RPC 请求使用 kind `25195`，RPC 响应使用 kind `25196`，状态更新使用 kind `25197`。协调器持有一张 Lightning hold invoice，taker 提交 BLIK code，BLIK 转账确认后协调器释放 preimage，并将 invoice 结算路由给 maker。

---

## 版本发布

### Amber v6.2.2 实现 NIP-46 客户端元数据 {#amber-implements-nip-46-client-metadata}

[Amber](https://github.com/greenart7c3/Amber) 是 greenart7c3 维护的主流 Android [NIP-46](/zh/topics/nip-46/) 远程签名器；它在对应规范 PR 合并的同一周发布 [v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2)。该版本在请求界面与应用列表中显示原生应用图标和新的客户端元数据字段，每次连接时持久化客户端元数据，并在连接与接受时获取原生应用图标和名称。此变更直接对应 DocNR 的 [NIP-46 PR #2381](https://github.com/nostr-protocol/nips/pull/2381)：它为 connect 请求增加可选客户端元数据，让签名器可以显示请求方有意义的名称与图标。Amber v6.2.2 还支持事件 kind 30618，并在 Active relays 界面中将默认中继与连接中继分开。

该版本进一步收紧签名器的安全面。解密后的 NIP-46 请求与响应正文不再写入日志；encrypt 与 decrypt 载荷以密文存储，并按需解密。所有 logcat 输出都受 `BuildConfig.DEBUG` 门禁控制；浏览器调用方（null-package）被强制设为始终询问；复制到剪贴板的 `nsec`、`ncryptsec` 与 seed words 会被标记为敏感内容，并在延迟后清除。显式加入备份与数据提取排除项，作为纵深防御。该版本还修复 Active relays 嵌套滚动导致的崩溃、bunker 请求去重竞态引发的 `LazyColumn` 重复 key 崩溃，以及发布更新检查中的 `EOSE` 竞态。

### Haven 在 Marmot 上推出私密位置共享 {#haven-launches-private-location-sharing-on-marmot}

[Haven](https://github.com/mehmetefeumit/Haven-App) 本周首次公开，是一款在 Android 和 iOS 上运行、抗审查的私密位置共享应用，基于 Nostr 并使用 [Marmot](/zh/topics/marmot/) 协议。该仓库四天内发布五个版本，从 [v0.1.0](https://github.com/mehmetefeumit/Haven-App/releases/tag/v0.1.0) 到 [v0.1.4](https://github.com/mehmetefeumit/Haven-App/releases/tag/v0.1.4)，是一个新项目的首批版本。Haven 使用 Dart 与 Flutter 构建，并以开发者签名应用的形式通过 Zapstore 发布。Marmot 是基于 MLS 的 Nostr 端到端加密消息层，负责群组状态与密文分发；Haven 把这一模式从消息扩展到位置共享，每个群组的加密状态承载该群组同意共享的位置更新。

### CodeDeck：通过 Nostr 远程进行 agentic coding {#codedeck-remote-agentic-coding-over-nostr}

[CodeDeck](https://github.com/JeroenOnNostr/codedeck) 本周首次公开，是一款面向 Android 与桌面的多会话 agentic-coding 界面，使用 Tauri v2、React 19 与 Rust 后端构建；用户可以通过加密 Nostr 中继，用手机控制笔记本上运行的 [Claude Code](https://www.anthropic.com/claude-code) 会话。项目在同一个四天窗口发布 [v2026.06.17](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.06.17)、[v2026.6.18](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.6.18) 与 [v2026.6.20](https://github.com/JeroenOnNostr/codedeck/releases/tag/v2026.6.20)。其传输模型将 Nostr 用作加密控制平面：CodeDeck 手机端将命令发布为加密事件，由笔记本旁运行的 bridge 订阅；笔记本再通过同一组中继发布会话输出。

v2026.06.17 将 `nostr-vpn` FIPS mesh 嵌入为应用的 Android VPN service，使笔记本可以从任何地方在实体测试手机上构建、安装、启动并操控应用的开发构建，测试手机只需安装 CodeDeck。v2026.6.18 将配对与 mesh 邀请合并为扫描一个二维码；v2026.6.20 增加逐会话模型选择，让每个会话以选定模型启动。

### Grain v0.8.0-rc1 发布完整 Nostr 客户端引擎 {#grain-ships-a-full-nostr-client-engine}

[Grain](https://github.com/0ceanSlim/grain) 是 0ceanSlim 维护的 Go 中继；它发布 [v0.8.0-rc1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc1)，如今既是 Nostr 中继，也是其自身所基于的可导入 Go 客户端库。v0.7.x 侧重从浏览器运营中继，v0.8 系列则交付 `client/core`：一个纯 Go、无 cgo 或 HTTP 依赖的独立 outbox-model Nostr 客户端引擎。该引擎管理共享中继池、解析每位用户的中继列表，并按 [gossip / outbox model](https://mikedilger.com/gossip-model/) 路由所有读取与发布：从用户的 outbox 中继读取其笔记，发布的回复则抵达父作者的 inbox 中继。Grain 自身的 web 前端现成为该库的参考使用方，因此 UI 既是可用应用，也是供下游 Go 项目参考的完整示例。

该版本加入原生 [NIP-44](/zh/topics/nip-44/) 加密（v2 与 v3）、[NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) 中继 AUTH、[NIP-65](/zh/topics/nip-65/)、[NIP-17](/zh/topics/nip-17/)、[NIP-51](/zh/topics/nip-51/) 与 [NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md) 中继列表、[NIP-89](/zh/topics/nip-89/) 客户端 tag，以及 [Blossom](/zh/topics/blossom/) 与 [NIP-96](/zh/topics/nip-96/) 媒体支持。此前必须自行重写中继路由的下游 Go 应用现在可以直接 `import` 该引擎。

### Mostro Core v0.13.1 跟进 Protocol v2

[Mostro Core](https://github.com/MostroP2P/mostro-core) 在[上周推出 Protocol v2](/en/newsletters/2026-06-17-newsletter/#mostro-core-v0130-cuts-the-relay-middleman-with-protocol-v2)后发布 [v0.13.1](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.1)，为协议的价格信息流合约引入 `PriceTooStale` 错误变体。守护进程侧本周也有多项变化：[PR #752](https://github.com/MostroP2P/mostro/pull/752) 让无效订单 ID 以 `CantDo(NotFound)` 错误呈现给客户端，而不是被静默丢弃；[PR #785](https://github.com/MostroP2P/mostro/pull/785) 让内部协议版本跟随当前传输；[PR #778](https://github.com/MostroP2P/mostro/pull/778) 完成 El Toque 法币交叉提供方针对 CUP 与 MLC 的第三阶段；[PR #782](https://github.com/MostroP2P/mostro/pull/782) 则为对齐规范，将 [NIP-33](https://github.com/nostr-protocol/nips/blob/master/33.md) 信息 tag `protocol_versions` 更名为 `protocol_version`。

### Wisp v1.1.2 与 Dark Wisp 变体

[Wisp](https://github.com/barrydeen/wisp) 是 barrydeen 的 Kotlin 与 Jetpack Compose Android 客户端；它发布 [v1.1.2](https://github.com/barrydeen/wisp/releases/tag/v1.1.2)，包括：在确定性交易顺序中将发送给自己的钱包分支保持分离（[PR #586](https://github.com/barrydeen/wisp/pull/586)）；延迟创建内联视频播放器，以承受媒体密集型笔记（[PR #592](https://github.com/barrydeen/wisp/pull/592)）；修复 event-relays 集合中的 `ConcurrentModificationException`（[PR #595](https://github.com/barrydeen/wisp/pull/595)）；修复聊天气泡内容的固有测量，避免 `SubcomposeLayout` 崩溃（[PR #596](https://github.com/barrydeen/wisp/pull/596)）。该版本还加入带锁外垃圾信息评分的增量信息流过滤器。Wisp 团队本周也通过 Zapstore 发布 Dark Wisp v1.1.0，这是增加 ZEC、DASH、BCH 与 LTC zap 目标及匿名模式的多币种变体。

### Citrine v3.0.1

[“Citrine”](https://github.com/greenart7c3/Citrine) 是 greenart7c3 的 Android 本地 Nostr 中继；它发布 [v3.0.1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.1)，仅包含一项修复：注销一个从未注册的 Pokey receiver 时不再导致中继崩溃。

### FIPS v0.4.0-rc2

[FIPS](https://github.com/jmcorgan/fips) 即 Free Internetworking Peering System；它在 v0.3.x 线上格式之上将 [v0.4.0-rc2](https://github.com/jmcorgan/fips/releases/tag/v0.4.0-rc2) 标记为打包验证候选版本。v0.4.0 系列增加 Nym mixnet 传输与可选的 mDNS 局域网 peer 可达性发现；重构数据平面，提高单节点吞吐量并降低逐数据包 CPU 消耗；将运营者读取面移出数据平面热路径，使可观测性在负载下仍保持响应；交付重构后的 `fipstop` TUI；并加固 FMP 与 FSP rekey，使其在丢包下无中断。这是候选版本；v0.4.0 稳定版暂定于 2026-06-21 发布。

### Kubo v2026.06.12 与 v2026.06.20 锁定信任门禁儿童信息流，并增加家长精选 YouTube

[Kubo](https://github.com/JeroenOnNostr/kubo) 是 JeroenOnNostr 基于 Trust Extended Permissions Protocol（TEPP）打造的 Nostr 原生 YouTube Kids 替代应用；本周发布两个版本。[v2026.06.12](https://zapstore.dev/apps/com.kubo.app)（日历版本，派生 `versionCode` 为 `YYYYMMDD`）强制启用信任门禁儿童信息流：孩子能看到或互动的每篇帖子、个人资料、reaction 与 repost 现在都经 TEPP 流转，范围仅限家长准入的人。新安装默认启用信任门禁，并在引导期间初始化孩子的社交圈，因此信息流从首次启动起即处于安全状态。该版本还加入由家长管理的群聊，将信任事件路由至家庭私有中继集合；如无法加载信任数据，则失败即关闭（不显示任何内容），而不是泄漏未经审核的内容。

[v2026.06.20](https://zapstore.dev/apps/com.kubo.app) 增加家长精选 YouTube 频道：家长可以搜索频道并将其加入儿童信息流，使孩子只能看到家长批准频道中的视频；HTTP 快速通道与乐观 UI 取代约 10 秒的添加路径。该版本还移除关闭 Trust Extended Permissions 的选项（项目以强制信任为基础，因此该开关现在始终启用），增加专用 Support 页面，修复群聊中的 `@mentions`，使标记某人时显示可点击的 `@name` 而不是原始 `nostr:npub1…`，加入 mention 自动完成，并修复信任发布，使其依据真实执行状态而非镜像标志进行门禁。两个版本均通过 Zapstore 以开发者签名 Android 应用 `com.kubo.app` 跟踪。

### Pollerama v1.9.0 至 v1.9.4 增加 web-of-trust 分数、设备端中继引擎与“你可能认识的人”横栏

[Pollerama](https://github.com/formstr-hq/nostr-polls) 是 abh3po 开发、位于 [pollerama.fun](https://pollerama.fun) 的 Form* 系列 Nostr 投票与信息流客户端；本周通过 Zapstore 发布五个版本。v1.9.0 加入新的设备端中继引擎：内置本地中继会存储用户看过的一切，并优先从本地缓存响应应用，因此信息流、个人资料与线程可即时加载（即使离线），并在后台与网络保持同步。所有中继流量（读写）都通过该引擎在主线程之外流转；已加载的笔记、个人资料、reaction 与 zap 直接来自本地存储，不再重复抓取。

v1.9.2 修复 Home 与 Notes 信息流（以及所有 Following/Network 视图）在启动或恢复时偶尔为空的问题：关注列表改为独立于同步引擎缓存；私信中分享的笔记会从中继提示中抓取引用笔记，因此即使用户未关注作者也能可靠加载；Network 设置面板则显示中继连接、缓存大小与同步状态，并提供重新连接或清除本地缓存的控件。v1.9.3 修复启动崩溃与 Home 信息流加载回归。

v1.9.4 在个人资料上引入 web-of-trust 信任分数（用户关注的人中有多少也关注此人，以 network chip 显示），以及“你可能认识的人”横栏（从 web of trust 中提取关注建议，并按用户所关注者中关注该人的数量排序）。Network 设置现显示 web-of-trust 大小和上次计算时间，并提供按需重新计算按钮。信任分数与推荐由 web-of-trust worker 在后台计算，不会阻塞应用。

### 其他小型版本发布

[nogringo/nostr-mail-client v0.13.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.13.1) 恢复通过 [NIP-55](/zh/topics/nip-55/) 签名器应用登录 Amber、Aegis 与 Primal，并停止反复提示签名器应用签署联系人。[Cameri/nostream v3.0.0](https://github.com/Cameri/nostream/releases/tag/v3.0.0) 从 web-app factory 中移除 `unsafe-inline` 并实现脚本 nonce。[LaWallet NWC v1.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v1.0.0) 发布项目首个 1.0，支持可分享 QR 链接卡片激活、Remote Wallet 识别与 Lightning Address 自动配置。[Formstr Nostr Calendar v2.0.0 至 v2.0.2](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.0.2) 增加 PWA，修复离线可替换事件（[PR #194](https://github.com/formstr-hq/nostr-calendar/pull/194)），并绑定签名器方法，使私密表单可以提交（[PR #199](https://github.com/formstr-hq/nostr-calendar/pull/199)）。来自 [Spl0itable/NYM](https://github.com/Spl0itable/NYM)、[codeswot/ZapBook](https://github.com/codeswot/ZapBook)、[77elements/noornote](https://github.com/77elements/noornote)、[mattn/nostr-relay](https://github.com/mattn/nostr-relay)、[mattn/algia](https://github.com/mattn/algia)、[mouse484/astraea](https://github.com/mouse484/astraea)、[dergigi/boris](https://github.com/dergigi/boris)、[fiatjaf/nak](https://github.com/fiatjaf/nak)、[Spl0itable/nosflare](https://github.com/Spl0itable/nosflare) 与 [nostrord/nostrord](https://github.com/nostrord/nostrord) 的小型版本为本周收尾。

---

## 未发布的变更

### Cordn Ad-hoc CVM：浏览器端 MLS 协调器

[“Cordn Ad-hoc”](https://github.com/sandwichfarm/cordn-adhoc-cvm) 是 sandwich.farm 的新 web 应用，本周首次公开；它是一个在浏览器标签页中运行、面向临时 [Cordn](https://github.com/Cordn-msg/cordn) 群组的 MLS 协调器。其模式不同寻常：浏览器标签页运行 [ContextVM](/zh/topics/contextvm/) Nostr 协调器进程，发布协调器 pubkey，通过 Nostr 中继接收 MCP 请求，并将 MLS key package、welcome、加入请求与群组消息存入浏览器存储，全程无需后端。应用会阻止多个使用同一 pubkey 的协调器同时运行，并为原始 Nostr 事件、解码请求与实例 heartbeat 提供运营者 debug 日志。

### SnowCait/nostter 合并 19 个 UX 迭代 PR

[nostter](https://github.com/SnowCait/nostter) 是 SnowCait 的 web Nostr 客户端；本周未发布版本，但合并 19 个 PR。以 `app-manager.nostter.app` 替换 `nostrapp.link`（[PR #2234](https://github.com/SnowCait/nostter/pull/2234)），并将 `deck.nostter.app` 加入 `frame-ancestors` allowlist（[PR #2233](https://github.com/SnowCait/nostter/pull/2233)，使项目界面统一到 `nostter.app` 域名下。关注对象的可替换事件会缓存到 IndexedDB（[PR #2231](https://github.com/SnowCait/nostter/pull/2231)）；seen-on 中继状态则通过拆分 seen-on 与 via 选项恢复响应性（[PR #2230](https://github.com/SnowCait/nostter/pull/2230)）。

### Zap Cooking 修复跨项目 NIP-46 缺陷并重构编辑器

[Zap Cooking](https://github.com/zapcooking/frontend) 是 Nostr 上的食谱分享客户端；本周合并 16 个 PR。影响面最广的是 [PR #452](https://github.com/zapcooking/frontend/pull/452)：Primal 远程签名器曾用签名器自身的 pubkey 标记事件，导致所有通过 Primal 路由的客户端无法上传、zap 或认证。Zap Cooking 捕获并修补了这条路径；修复位于客户端本地，但缺陷存在于整个 [NIP-46](/zh/topics/nip-46/) 生态。编辑器通过 [PR #458](https://github.com/zapcooking/frontend/pull/458) 重构，增加倒计时器、统一回复/评论 UI 与 Write/Preview 标签页。三个 SSR 修复（[PR #460](https://github.com/zapcooking/frontend/pull/460)、[PR #461](https://github.com/zapcooking/frontend/pull/461)、[PR #462](https://github.com/zapcooking/frontend/pull/462)）和 [PR #454](https://github.com/zapcooking/frontend/pull/454) 稳定个人资料与食谱路由。探索体验则加入拖动滚动横栏、带个人资料链接的头像 cursor，以及社区 sticky tab 修复（[PR #456](https://github.com/zapcooking/frontend/pull/456)）。

### Shopstr 交付 Cashu 托管生命周期与店面工具

[Shopstr](https://github.com/shopstr-eng/shopstr) 是 [NIP-99](/zh/topics/nip-99/) 市场；本周合并一系列重要 PR。[PR #512](https://github.com/shopstr-eng/shopstr/pull/512) 为市场实现端到端 P2PK Cashu 托管生命周期，与同周通过 [NIP-99 PR #2323](https://github.com/nostr-protocol/nips/pull/2323) 推进的更广泛商务浪潮（链上图 checkout 层提案）以及 Conduit 的发布相呼应。[PR #543](https://github.com/shopstr-eng/shopstr/pull/543) 增加列出公司、获取公司详情、检索店面与获取卖家信誉的读取工具。[PR #229](https://github.com/shopstr-eng/shopstr/pull/229) 支持为个人资料和店铺图片粘贴 URL；[PR #359](https://github.com/shopstr-eng/shopstr/pull/359) 更新市场统计抓取，加入时间戳。



### divine.video 移动端与桌面端工作

[divine.video](https://github.com/divinevideo/divine-mobile) 是 rabble 的短循环视频客户端，恢复了 Vine 档案；本周合并的 PR 集中在播放与编辑：信息流会对可寻址视频去重（[PR #5465](https://github.com/divinevideo/divine-mobile/pull/5465)），本地 Nostr tag 过滤器改为精确匹配以避免伪结果（[PR #5463](https://github.com/divinevideo/divine-mobile/pull/5463)），视频编辑器在恢复含贴纸图层的草稿时不再崩溃（[PR #5474](https://github.com/divinevideo/divine-mobile/pull/5474)），Messages 徽标则会统计来自已关注但尚未回复的聊天的未读消息（[PR #5473](https://github.com/divinevideo/divine-mobile/pull/5473)）。

### Nostur 交付 NIP-46 客户端元数据支持与私信刷新修复

[Nostur](https://github.com/nostur-com/nostur-ios-public) 是 Fabian 开发的 iOS 客户端；在[上周发布 1.29.0](/en/newsletters/2026-06-17-newsletter/#nostur-1290-ships-anonymous-replies-and-remote-signer-logout)后，它向规范仓库合并四个 PR。[PR #74](https://github.com/nostur-com/nostur-ios-public/pull/74) 为 NIP-46 bunker connect 请求增加客户端元数据，形状与 DocNR 的提案及 Amber v6.2.2 本周交付的实现相同。[PR #75](https://github.com/nostur-com/nostur-ios-public/pull/75) 与 [PR #76](https://github.com/nostur-com/nostur-ios-public/pull/76) 修复 iPhone 转入前台后的私信刷新与前台恢复路径；[PR #78](https://github.com/nostur-com/nostur-ios-public/pull/78) 则为自定义 NWC 设置增加二维码扫描。

---

## 新纳入跟踪与发现的项目

### Social Agents Prototype：带人工批准门禁的 Nostr 原生 AI agent 协作

[Social Agents Prototype](https://github.com/SrulyRosenblat/social_agents_prototype_nostr) 是 Sruly Rosenblat 开发的实验性 Nostr AI 工具，探索去中心化 agent-to-agent 通信。agent 在网络中广播原子问题，只有相关 agent 响应；每条发送或接收的消息在传输前都必须经过人工批准门禁。项目与本周的 Buzz、NIP-100 SNIN 处于同一 agent 协作领域，但采用不同形态：Social Agents Prototype 将 agent 建模为广播与监听参与者，每条消息都需人工批准。同一问题的多条并行路线在本周清晰可见。

### PRana：NIP-34 issue 工作清单

[PRana](https://github.com/DocNR/prana) 是 DocNR 开发的工作清单，汇集选择加入 git-over-Nostr 仓库中正确开启的 [NIP-34](/zh/topics/nip-34/) issue。该工具位于 git-over-Nostr 栈的上一层：消费参与仓库的 NIP-34 issue 事件，并将其呈现为分流队列。它发布的同一周，[NIP-34 PR #2384](https://github.com/nostr-protocol/nips/pull/2384) 提议移除 maintainers tag 以解决过期问题，这会直接影响 PRana 等工具如何跨仓库判定 issue 权限。

### routstr-chat：通过 Nostr 上的 Routstr 协议访问本地 LLM

[Routstr 团队的 routstr-chat](https://github.com/Routstr/routstr-chat) 是一款完全在本地运行的聊天界面，通过 Routstr 协议经 Nostr 访问任意 LLM 模型。Routstr 协议通过发布在 Nostr 上的提供方公告（kind `38421`）路由推理请求，并使用 Cashu 结算，详见 [Newsletter #20](/en/newsletters/2026-04-29-newsletter/#routstrd-launches-a-local-router-for-inference-over-nostr)。聊天客户端是该协议之上的用户界面；路由守护进程 Routstrd 负责发现与支付，聊天应用则提供对话 UI。

---

## 协议工作

### NIP 更新

本周 NIP 活动异常密集：两项合并，以及一批重要的开放提案。

#### NIP-46 客户端元数据在 Amber 与 Nostur 中交付

[“NIP-46 PR #2381”](https://github.com/nostr-protocol/nips/pull/2381) 是 [Clave 上周提出的变更](/en/newsletters/2026-06-17-newsletter/#clave-10-ships-to-the-app-store-with-push-woken-background-signing)，如今客户端与签名器两端均有实际实现。[Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) 读取 bunker connect 请求中新增的可选 `optional_client_metadata` 字段，并在请求界面与应用列表上显示原生应用图标和元数据。[Nostur PR #74](https://github.com/nostur-com/nostur-ios-public/pull/74) 则在客户端侧添加该字段。三个项目共同补上 bunker 配对中的身份缺口：`bunker://` 配对如今可以携带应用已能通过 `nostrconnect://` 公告的同一组 `name`、`url` 与 `image`。

#### NIP-86 signevent 与配套中继角色事件

[staab 的 PR #2389](https://github.com/nostr-protocol/nips/pull/2389) 将 `signevent` 操作合并进 [NIP-86](/zh/topics/nip-86/) 中继管理 API，使中继管理员可以代表中继管理 [NIP-43](https://github.com/nostr-protocol/nips/blob/master/43.md) 事件。配套的开放提案 [staab 的 PR #2390](https://github.com/nostr-protocol/nips/pull/2390) 定义中继角色事件，使中继能够声明角色定义，管理员可以向这些角色分配或取消分配成员。两个 PR 旨在组合使用：NIP-86 为管理员提供操作，角色事件则提供授权模型。

#### NIP-99：市场的链上图 checkout 层

[Colabonate 的 PR #2323](https://github.com/nostr-protocol/nips/pull/2323) 是本周最强的枢纽关联。提案以征求设计反馈的形式提出，并指出 [NIP-99](/zh/topics/nip-99/) 与 Gamma Market Spec 栈中的两个缺口：一个存在于事件图上的 checkout 流程（点击立即购买后的状态、订单创建、支付与交付确认，均作为任何客户端都能读取的公开可寻址 Nostr 事件），以及针对仅凭 web-of-trust 信号不足以保障的交易加入托管与争议解决（高价值商品、首次交易对手、匿名市场、实体配送）。该提案像 NIP-99 消除 listing 的跨客户端孤岛一样，消除市场交易的跨客户端孤岛。它与 [Conduit](https://github.com/Conduit-BTC/conduit-mono) 发布（仓库内自带 `nips/` 与 `specs/` 目录）、[Shopstr PR #512](https://github.com/shopstr-eng/shopstr/pull/512)（端到端 Cashu 托管生命周期）、[BitBlik](https://github.com/bit-blik/bitblik)（带自有托管原语的 P2P BLIK ↔ Lightning），以及 [Gamma Markets Market Spec](https://github.com/GammaMarkets/market-spec) 独立仓库进入活跃跟踪发生在同一周。

#### NIP-34：移除 maintainers tag 以解决过期问题

[dhalsim 的 PR #2384](https://github.com/nostr-protocol/nips/pull/2384) 从 [NIP-34](/zh/topics/nip-34/) 仓库公告中移除 maintainers tag，以解决 [issue #2382](https://github.com/nostr-protocol/nips/issues/2382)。maintainers tag 没有明确的过期语义，使下游工具难以判断某次 maintainer 指派是否仍具权威性。此变更影响面广泛：它会影响 flotilla-budabit 补丁（本周唯一有实质补丁活动的已跟踪 NIP-34 仓库）、Iris 团队的八仓库 NIP-34 分发设置、BitBlik NIP-34 镜像、新增的 Amber NIP-34 镜像，以及 DocNR 的 PRana issue 工作清单工具。PR 的交叉审阅者包括 DanConwayDev（ngit）、vitorpamplona（Amethyst）、TheAwiteb 与 chebizarro。

#### NIP-29 群组状态（进行中）

[dtonon 的 PR #2372](https://github.com/nostr-protocol/nips/pull/2372) 提议为 [NIP-29](/zh/topics/nip-29/) 引入群组状态框架，并以进行中版本征求反馈。这延续了 [#27 中报道的 NIP-29 演进](/zh/newsletters/2026-06-17-newsletter/)，如今采用新的框架。

#### NIP-79 Stories 与 NIP-76 Reels Feed（均由 anaskmh 提出）

同一作者本周提出两项短内容媒体规范。[PR #2386](https://github.com/nostr-protocol/nips/pull/2386) 提议 NIP-79 Stories：24 小时后过期的全屏照片、视频与文字幻灯片；kind `19` 用于单张幻灯片，kind `34237` 是携带有序 `e` tag 来编排多张 story 的可寻址事件，并可选用 kind `15750` 提供保护隐私的已查看回执。[PR #2385](https://github.com/nostr-protocol/nips/pull/2385) 提议面向短视频 Reels Feed 的 NIP-76。两者都是与 divine.video 等现有视频客户端实际交付内容并行的规范，并非对后者的实现。

#### 将 kind 1111 用作 kind 1 笔记的回复

[zhoreeq 的 PR #2358](https://github.com/nostr-protocol/nips/pull/2358) 删除 NIPs 文档中此前不鼓励将 kind `1111`（[NIP-22](/zh/topics/nip-22/)）评论线程回复用于 kind `1` 笔记的条文（[issue #2250](https://github.com/nostr-protocol/nips/issues/2250)）。diff 很小，影响却很广：任何希望对普通 kind-1 时间线笔记使用 NIP-22 线程评论形状的客户端，如今都有明确支持。

---

## Nostr 六年六月史 {#six-years-of-nostr-junes}

六月的[仓库历史](https://github.com/nostr-protocol/nips/commits/master/)呈现了 Nostr 从协议萌芽走向可组合应用底座的过程。2021 年，全部工作仍能容纳在一个协议仓库中。2022 年，标准流程与首批成熟客户端成为彼此独立的项目。2023 年的公共浪潮使中继、支付与更丰富的身份变得紧迫；2024 年替换了早期的签名与消息捷径；2025 年将这些合约带入私密群组、git 协作、媒体与商务；2026 年则推出一批把 Nostr 作为 agent 工作空间、交易平台与开发者工具中一层的产品。演进方向，是从证明已签名事件能够经中继传递，走向让这一事实成为实现细节。

### 2021 年六月：协议萌芽

Nostr 当时约有七个月历史。fiatjaf 的[最初协议文章](https://fiatjaf.com/nostr.html)与 [`fiatjaf/nostr`](https://github.com/fiatjaf/nostr) 仓库仍承载几乎整个公开项目。少数开发者即可审阅每项变更，参考实现是一段 Python 脚本。这还不是客户端生态；它表达的是一项主张：用户可以签署事件并选择中继，而无需由平台分配身份。

当时尚无独立 NIPs 仓库，因此提案与实现示例仍共享[主协议历史](https://github.com/nostr-protocol/nostr/commits?since=2021-06-01&until=2021-07-01)。在这一阶段，紧凑的范围是一项优势：新实现者可以端到端理解协议。代价则是每种新行为仍依赖同一小群人；2022 年的仓库拆分与客户端浪潮开始打破这一限制。

### 2022 年六月：NIPs 仓库形成

到 2022 年中期，Nostr 已有足够多的提案者，可以支撑五月创建的独立 [`nostr-protocol/nips`](https://github.com/nostr-protocol/nips) 仓库。约二十份规范覆盖基本事件格式、关注列表、加密私信、中继元数据与 bech32 标识符。把文档移出原始代码仓库改变了项目治理：客户端可以独立演进，共享的线上行为则接受明确提案与审阅。

首批公共 web 客户端（包括 Astral 与 Anigma）已以早期形态上线，William Casarin 的 [Damus 仓库](https://github.com/damus-io/damus/commits?since=2022-06-01&until=2022-07-01) 正走向 TestFlight 分发。用户群仍然较小，并以开发者为主，但系统已有两个能够相乘的界面：更多人可以在不维护规范的情况下构建应用，更多人也可以在不拥有原始客户端的情况下改进规范。

### 2023 年六月：Damus 上线后的采用浪潮

到 2023 年六月，Damus 在 App Store 上线后引发的公共浪潮已改变工程问题。[Primal](https://github.com/PrimalHQ) 与 Iris 开始为未参与协议早期讨论的人构建产品，[strfry](https://github.com/hoytech/strfry) 则为面对更大流量的运营者提供高性能中继。网络需要的不再只是更多实现；它需要能在用户、关注关系与事件历史增长时保持响应的客户端与中继。

协议工作因此集中于路由与价值传输。[NIP-65 中继列表](https://github.com/nostr-protocol/nips/blob/master/65.md) 为新兴的 outbox 模型提供可移植的事实来源，[NIP-57 zap](https://github.com/nostr-protocol/nips/blob/master/57.md) 则将事件与身份连接到 Lightning 回执。阶段变化非常实际：身份与发布吸引用户加入，但选择性中继路由与钱包互操作性，才让更大的网络不只是一个过载的公共信息流。

### 2024 年六月：签名器、gift wrap 与消息升级

到 2024 年六月，签名开始从单个客户端中移出。[NIP-46 规范](https://github.com/nostr-protocol/nips/blob/master/46.md)、[nsecBunker](https://github.com/kind-0/nsecbunkerd) 与 [Amber](https://github.com/greenart7c3/Amber) 使 web 与 Android 应用可以请求签名，而不必导入用户的私钥。这颠倒了一项早期假设：可移植性不再意味着把 nsec 复制到每个客户端，而是让专用签名器围绕它执行安全边界。

消息也因同样原因发生变化。[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) 将 NIP-44 加密与 NIP-59 gift wrap 结合，减少 NIP-04 暴露的元数据；[NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md) 则允许客户端为自身无法渲染的事件类型推荐处理程序。MLS-over-Nostr 的讨论在这一环境中开始。隐私与应用发现逐渐成为跨客户端合约，为私密群组和更丰富的事件专用应用奠定基础，而不是让一个客户端试图容纳所有功能。

### 2025 年六月：Marmot、git-over-Nostr 成熟与客户端长尾

到 2025 年六月，MLS-over-Nostr 已有正式的 [Marmot 规范](https://github.com/marmot-protocol/marmot)，以及公开实现 [White Noise](https://github.com/marmot-protocol/whitenoise)。[NIP-34 git 事件](https://github.com/nostr-protocol/nips/blob/master/34.md)、ngit 与 GitWorkshop 也已成熟为可用的代码审阅流程。这些项目处于同一设计阶段：使用中继协调，同时将敏感群组状态或仓库对象移入专用层，而不是把文本笔记客户端当作完整应用。

商务与媒体沿着同一模式发展。[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) 钱包与 NIP-61 nutzap 将 Cashu 状态放入可移植事件；Wavlake、Divine 和 [NIP-99 市场实现](https://github.com/nostr-protocol/nips/blob/master/99.md) 则为音乐、视频与 listing 使用专用事件 kind。随着应用保留身份与中继底座，同时引入领域专用存储、支付、审核与呈现，Nostr 看起来越来越不像“一种社交网络”。

### 2026 年六月：密集发布的月份

2026 年六月出现一批将 Nostr 视为更大产品中一个组件的项目。[Buzz](https://github.com/block/buzz) 推出面向人类与 agent 的自托管“工作空间即中继”模式；[Napplets](https://napplet.run) 为经 Nostr 与 Blossom 运行的可组合应用定义信任边界；[Conduit](https://conduit.market) 将市场应用与自身协议文档并列。这些项目已不再追问已签名事件能否支撑协作，而是在决定哪些工作属于事件、哪些属于 blob 或本地状态，以及宿主应保留哪些权限。

[BitBlik](https://www.bitblik.app) 将 Nostr 用于点对点法币至 Lightning 兑换；[CodeDeck](https://github.com/JeroenOnNostr/codedeck) 通过加密中继传送编程会话；[Haven](https://github.com/mehmetefeumit/Haven-App) 则在传统消息应用之外运用 Marmot。它与 [2021 年原型仓库](https://github.com/nostr-protocol/nostr)的距离不只体现在项目更多，也体现在抽象发生变化：团队可以把可移植身份、中继发现、加密与支付当作现成组件，再将设计精力投入其上的应用特定边界。
