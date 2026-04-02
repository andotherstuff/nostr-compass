---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Amethyst](https://github.com/vitorpamplona/amethyst) 实现完整的 [NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）方法支持，[Alby Hub](https://github.com/getAlby/hub) 在 [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) 中添加多 relay 支持，[Amber](https://github.com/greenart7c3/Amber) 发布 [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3) 带有内置 Tor 和更细粒度的签名器权限，[Zeus](https://github.com/ZeusLN/zeus) 在 [PR #3835](https://github.com/ZeusLN/zeus/pull/3835) 中移除了有风险的 NWC keysend 路径。[Notedeck](https://github.com/damus-io/notedeck) 在 [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) 中发布签名更新器，通过 [NIP-94](/zh/topics/nip-94/)（文件元数据）event 发现版本，[Damus](https://github.com/damus-io/damus) 修复了过时的 [NIP-65](/zh/topics/nip-65/)（Relay 列表元数据）状态，[Nostrability Outbox](https://github.com/nostrability/outbox) 用修正数据修订了基准测试结果，[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) 测试 DM 的直接 relay 订阅。[Primal Android](https://github.com/PrimalHQ/primal-android-app) 发布 [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7)，[Route96](https://github.com/v0l/route96) 发布 [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0)，[OpenChat](https://github.com/DavidGershony/openChat) 在 [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11) 中持续优化 Marmot 互操作性，[Pika](https://github.com/sledtools/pika) 在 [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) 中整合其运行时，[Nostria](https://github.com/nostria-app/nostria) 添加 [NIP-85](/zh/topics/nip-85/)（可信断言）Web of Trust 过滤。NIPs 仓库合并了 [NIP-54](/zh/topics/nip-54/)（Wiki）Djot 标记和 [NIP-19](/zh/topics/nip-19/)（Bech32 编码实体）的 5000 字符输入上限，同时关于 [NIP-49](/zh/topics/nip-49/)（私钥加密）密钥文件、[NIP-43](/zh/topics/nip-43/)（Relay 访问元数据和请求）成员一致性、[NIP-17](/zh/topics/nip-17/)（私密私信）删除指南和 [NIP-222](/zh/topics/nip-222/) 分享意图 URI 的开放提案也在推进。

## 新闻

### Wallet Connect 支持扩大，钱包客户端收紧失败路径

[Amethyst](https://github.com/vitorpamplona/amethyst)，由 vitorpamplona 维护的 Android 客户端，合并了 [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828)，使其 [NIP-47](/zh/topics/nip-47/) 实现接近完整的协议覆盖。该补丁添加了 `make_invoice`、`lookup_invoice`、`list_transactions`、`get_balance`、`get_info`、hold invoice 方法、带有 TLV 记录的 keysend 支持、通过 kind `13194` 的能力发现，以及 kind `23197` 上带有 [NIP-44](/zh/topics/nip-44/)（加密载荷）的通知 event。这为客户端提供了更广泛的 NWC 接口，而无需依赖应用特定的扩展。

周围的钱包栈朝着同一方向发展。[Alby Hub](https://github.com/getAlby/hub)，许多 NWC 部署背后的自托管 Lightning 节点和钱包服务，发布了 [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6)，支持多 relay 和更简化的连接与交换流程。[Zeus](https://github.com/ZeusLN/zeus)，移动 Lightning 钱包，合并了 [PR #3835](https://github.com/ZeusLN/zeus/pull/3835)，在识别到该流程中存在静默资金流失路径后移除了 NWC keysend 支持，同时修复了待处理 event 和 Cashu 活动处理。Nostr 上的钱包连接正在变得更广泛，实现者正在移除难以安全保障的流程。

### Notedeck 将版本发现迁移到 Nostr

[继上周的 Notedeck 报道之后](/en/newsletters/2026-03-11-newsletter/)，[Notedeck](https://github.com/damus-io/notedeck)，来自 Damus 团队的原生桌面客户端，在合并 [PR #1326](https://github.com/damus-io/notedeck/pull/1326) 后发布了 [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2)。新的更新器订阅签名的 kind `1063` 版本 event，匹配本地平台，下载引用的二进制文件，并在安装前验证其 SHA256 哈希。版本元数据不再需要来自 GitHub API 或项目网站。一个受信任的版本 pubkey 和一个 relay 连接就足够了。

同一补丁还添加了 `notedeck-release` CLI，从 GitHub 发布工件发布这些 event，这意味着发布管道现在既有 Nostr 原生的发布路径，也有 Nostr 原生的发现路径。它还使 Damus 和 Notedeck 的更新器模型更接近 Zapstore 的 relay 发布签名版本流程：Zapstore 的 `zsp` 工具已经将软件资产作为 kind `1063` 或 `3063` event 处理，因此该路径不限于一个客户端或一个发布者。候选版本的其余部分是实用的桌面工作，关注列、个人资料"以用户身份查看"、[NIP-59](/zh/topics/nip-59/)（Gift Wrap）支持、实时笔记统计和 [NIP-11](/zh/topics/nip-11/)（Relay 信息文档）限制处理，但更新器是最可能超越这一发布周期的部分。

### Relay 状态正向运行时行为靠拢

[Damus](https://github.com/damus-io/damus) 合并了 [PR #3665](https://github.com/damus-io/damus/pull/3665)，用对最新 kind `10002` event 的直接数据库查询替代了过时的存储 relay 列表 event ID。当旧值过期时，relay 添加和移除操作可能回退到引导列表或一年前的列表，使得某些 relay 变更看似成功但实际活跃状态未改变。[PR #3690](https://github.com/damus-io/damus/pull/3690) 修复了第二条故障路径，在 LMDB 压缩期间删除过时的 `lock.mdb` 状态，以免应用在下次启动时因 `SIGBUS` 崩溃。

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) 开放了 [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194)，在会话打开时直接订阅聊天对象的 [NIP-04](/zh/topics/nip-04/)（加密私信）写入 relay，同时保留缓存服务器作为后备。[Nostur](https://github.com/nostur-com/nostur-ios-public) 开放了 [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53)，结合随机化 relay 评分、来自 nostr.watch 的 [NIP-66](/zh/topics/nip-66/) 活跃度过滤和 Thompson 采样，将 relay 选择从固定启发式转变为学习策略。客户端长期以来将 relay 选择视为设置数据。越来越多的应用现在将其视为需要测量和修复逻辑的实时状态。

## 版本发布

### Primal Android 3.0.7

[Primal Android](https://github.com/PrimalHQ/primal-android-app)，来自 Primal 的 Android 客户端，发布了 [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7)，包含新的投票和钱包功能。[PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945) 添加基于 zap 的投票，[PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948) 分页加载投票使更大的投票保持可用，[PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965) 获取所有交易的 zap 收据。同一版本还在 [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968) 中使用 [NIP-89](/zh/topics/nip-89/)（推荐应用处理器）客户端元数据标记支持的 event，帮助下游客户端更清晰地归属 event 来源。

### Amber v4.1.3

[继上周的 Amber 报道之后](/en/newsletters/2026-03-11-newsletter/)，[Amber](https://github.com/greenart7c3/Amber)，用于 [NIP-55](/zh/topics/nip-55/) 流程的 Android 签名器应用，发布了 [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3)。该版本在其近期 [NIP-42](/zh/topics/nip-42/) relay 认证工作基础上进行了更多操作加固：[PR #327](https://github.com/greenart7c3/Amber/pull/327) 在 Orbot 支持之外添加内置 Tor，[PR #324](https://github.com/greenart7c3/Amber/pull/324) 用内容类型特定规则替代粗粒度的基于 NIP 的加密权限，[PR #336](https://github.com/greenart7c3/Amber/pull/336) 从离线版本中移除网络权限，[PR #335](https://github.com/greenart7c3/Amber/pull/335) 添加 CI 检查以保持该状态。[PR #322](https://github.com/greenart7c3/Amber/pull/322) 还将 PIN 存储迁移到加密 DataStore。

此版本收紧了签名器边界本身。这对任何将真实密钥或 relay 认证决策交给 Amber 的 Android 流程都很有用，因为困难的部分不仅是签名器能做什么，还包括它的作用范围能被缩小到多窄。

### Route96 v0.6.0

[继上周的 Route96 报道之后](/en/newsletters/2026-03-11-newsletter/)，[Route96](https://github.com/v0l/route96)，支持 Blossom 和 [NIP-96](/zh/topics/nip-96/)（HTTP 文件存储）的媒体服务器，发布了 [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0)。该版本将配置和白名单状态迁移到数据库并支持热重载，添加了冷文件或老化文件的保留策略。还添加了更丰富的 `GET /user/files` 端点和下载及出口的文件统计跟踪，为运营者提供更多关于其存储服务器使用方式的可见性。

### OpenChat v0.1.0-alpha.11

[继上周的 OpenChat 报道之后](/en/newsletters/2026-03-11-newsletter/)，[OpenChat](https://github.com/DavidGershony/openChat)，基于 Marmot 栈构建的 Avalonia 聊天客户端，经过一周密集的协议工作后发布了 [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11)。[Commit c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c) 将 Welcome event 包装在 [NIP-59](/zh/topics/nip-59/) gift wrap 中并移除了旧的 MIP-00 tag 规范化 shim，[commit 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1) 完成了 MIP-02 合规审计，[commit 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f) 对 MIP-03 群组消息加密做了同样的工作。[Commit 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547) 还将 NIP-44 处理统一到共享的 marmot-cs 实现上，降低了客户端加密漂移的风险。

### nak v0.19.0 和 v0.19.1

[nak](https://github.com/fiatjaf/nak)，fiatjaf 的命令行 Nostr 工具包，发布了 [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0) 和 [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1)。0.19 系列在 [commit 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47) 中添加了群组论坛 UI，在 [commit da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3) 中将群组元数据编辑切换到完整替换流程，在 [commit bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf) 中用 `supported_kinds` 替代旧的 `no-text` 处理。对于群组实现者来说，这使 CLI 与群组规范和客户端的发展方向保持一致。

## 项目更新

### Amethyst

[继上周的 Amethyst 报道之后](/en/newsletters/2026-03-11-newsletter/)，[Amethyst](https://github.com/vitorpamplona/amethyst)，拥有 Nostr 中最广泛协议覆盖面之一的 Android 客户端，在 NIP-47 补丁之后继续推进其钱包和 relay 工作。[PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853) 在 relay 管理界面添加了 [NIP-45](/zh/topics/nip-45/)（Event 计数）COUNT 查询，让用户可以看到每个 relay 为主页信息流、通知、DM 和索引数据实际持有多少 event。[PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849) 为 [NIP-17](/zh/topics/nip-17/)（私密私信）聊天添加加密文件上传，当存储主机拒绝加密版本时提供未加密上传的重试路径。

[PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791) 还带来了完整的 [NIP-46](/zh/topics/nip-46/)（Nostr Connect）桌面 bunker 登录和心跳指示器，这很重要，因为远程签名失败通常从用户角度看起来像随机的 UI 故障。客户端显示签名器是否存活以及最近何时响应，同时也清楚表明当前会话使用的是 bunker。

### Nostria

[Nostria](https://github.com/nostria-app/nostria)，围绕本地优先栈构建的多平台客户端，合并了 [PR #561](https://github.com/nostria-app/nostria/pull/561)，为信息流和线程回复添加 Web of Trust 过滤。该功能使用现有的信任服务排名数据，并将其作为信息流过滤器和回复过滤器公开，隐藏排名未达到阈值的作者，同时在受信任的后代存在时保留线程结构。这为用户提供了"显示所有人"和硬编码列表策展之间的中间层。

同一周还带来了 [PR #563](https://github.com/nostria-app/nostria/pull/563)，为摘要页面添加内容过滤和转发支持。在跟踪的 PR 列表之外，Nostria 还一直在填充更多的高级用户功能。它现在支持最新的 Brainstorm Web of Trust 服务和应用内注册，以及使用 NWC 和 BOLT-11 发票在 DM 中收发资金的流程。它还通过 emoji NIP 添加了 Nostr 原生 GIF 处理，以及更强大的音乐人 RSS 导入路径，可以从播客信息流中提取现有的 Lightning 分成。Nostria 正在将排名、媒体、支付和发布视为一个连接的应用平面。

### Nostur

[Nostur](https://github.com/nostur-com/nostur-ios-public)，由 nostur-com 维护的 iOS 客户端，开放了 [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53)，将 outbox 路由从固定计划转变为评分策略。该补丁添加了随机化 relay 评分、带有缓存 nostr.watch 信息流的 [NIP-66](/zh/topics/nip-66/) relay 活跃度过滤，以及 Thompson 采样，使 relay 的成功和失败数据改变未来的选择。该设计在过多 relay 会被过滤掉时保留安全阀，并保留 `.onion` relay。这是当前客户端将 relay 选择视为自适应系统的最清晰示例之一。

### Nostrability Outbox

[继早前的 Outbox 基准测试报告之后](/zh/newsletters/2026-03-04-newsletter/)，[Nostrability Outbox](https://github.com/nostrability/outbox)，专注于 [NIP-65](/zh/topics/nip-65/) 和 [NIP-66](/zh/topics/nip-66/) 客户端路由的基准测试和分析项目，本周致力于收紧自己的结论。[PR #35](https://github.com/nostrability/outbox/pull/35) 用跨 1,511 次运行的完整重新基准测试替换了膨胀的 Thompson 采样结果，并推荐 `CG3` 变体用于 NDK 风格的路由。[PR #43](https://github.com/nostrability/outbox/pull/43) 添加了衰减和用例比较，修复了 `0 follows` 缓存中毒 bug，然后在固定缓存 TTL 后重新运行了 Telluride 数据集。

这不是通常意义上的产品工作，但对客户端作者很重要，因为该项目的数字现在更加精确，在之前过度声称的地方不那么好看了。修正后的结果仍然有用。在 Outbox 关心的场景中，随机化选择持续优于纯确定性路由，Thompson 风格的学习在客户端持久化有用的 relay 历史时可以显著提高覆盖率，[NIP-66](/zh/topics/nip-66/) 活跃度过滤减少了在死 relay 上浪费的时间。这项工作也正在转化为具体的实现提案，包括 [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387)、[Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53)、[Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833)、[rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282)、[welshman #53](https://github.com/coracle-social/welshman/pull/53)，以及 [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) 和 [applesauce #55](https://github.com/hzrd149/applesauce/pull/55)。

### White Noise 后端

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)，White Noise 和其他 Marmot 工具使用的 Rust 后端，合并了两个关于 Blossom 媒体处理的边界加固补丁。[PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637) 对 Blossom URL 强制执行 HTTPS 并添加上传超时，[PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642) 将 blob 下载限制在 `100 MiB` 以阻止超大媒体拉取变成拒绝服务路径。对于私密消息软件来说，媒体 URL 是加密应用逻辑和不受信任网络基础设施之间最尖锐的接口之一。本周团队收紧了这一边缘。

### rust-nostr

[rust-nostr](https://github.com/rust-nostr/nostr)，Rust 协议库，合并了 [PR #1280](https://github.com/rust-nostr/nostr/pull/1280)，为 `LocalRelayBuilderNip42` 添加便捷构造函数。新的读写辅助方法为嵌入式 relay 和测试设置提供了更清晰的方式将 [NIP-42](/zh/topics/nip-42/) 认证策略转化为代码。这是一个小型库补丁，但对构建需要开启 auth 的本地或应用捆绑 relay 的团队很重要，无需每次都重复样板代码。

### Pika

[继早前的 Pika 报道之后](/zh/newsletters/2026-03-04-newsletter/)，[Pika](https://github.com/sledtools/pika)，基于 Marmot 的消息应用，发布了 [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) 和 [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1)，本发布周期聚焦于运行时统一。[PR #542](https://github.com/sledtools/pika/pull/542) 为 CLI 和 sidecar 引入共享 Marmot 运行时门面，应用主机也迁移到同一平面。[PR #556](https://github.com/sledtools/pika/pull/556) 收紧了 OpenClaw 代理生命周期和配置状态，[PR #600](https://github.com/sledtools/pika/pull/600) 为托管环境添加了从备份恢复和更严格的恢复安全性。

这里直接面向用户的功能比上次 Pika 报道中少，但架构变化意义重大。将群组、媒体、通话和会话逻辑放在一个共享运行时后面，降低了随着 Marmot 栈增长应用和守护进程发生漂移的可能性。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-54](/zh/topics/nip-54/)（Wiki）：从 Asciidoc 切换到 Djot**（[PR #2242](https://github.com/nostr-protocol/nips/pull/2242)）：kind `30818` 上的 Wiki 内容现在使用 Djot 作为规范标记格式。合并的文本添加了明确的 wikilink 行为、kind `818` 的合并请求示例、kind `30819` 的重定向示例，以及 `d` tag 的非拉丁文字规范化示例。这为实现者提供了比 Asciidoc 更清晰的解析目标，并移除了又一个依赖 Ruby 工具链的规范路径。

- **[NIP-19](/zh/topics/nip-19/)（Bech32 编码实体）：添加输入限制**（[PR #2264](https://github.com/nostr-protocol/nips/pull/2264)）：规范现在建议将 Bech32 编码实体字符串限制在 5000 个字符。这是一个小变更但具有实际的解析价值，因为 NIP-19 字符串现在出现在许多客户端的二维码流程、深层链接、分享面板和用户粘贴输入中。

**开放 PR 和讨论：**

- **[NIP-49](/zh/topics/nip-49/)（私钥加密）的 Nostr 密钥文件**（[PR #2269](https://github.com/nostr-protocol/nips/pull/2269)）：提议一种 `.nostrkey` 文件格式，用于密码加密的密钥导出和导入。如果合并，将为客户端提供比复制原始 `ncryptsec` 字符串更常规的基于文件的备份路径。

- **[NIP-43](/zh/topics/nip-43/)（Relay 访问元数据和请求）的成员状态一致性**（[PR #2267](https://github.com/nostr-protocol/nips/pull/2267)）：添加了一个章节，澄清 relay 应该为每个 pubkey 维护一个权威成员状态。这将简化围绕成员变更和重放历史的群组客户端逻辑。

- **[NIP-17](/zh/topics/nip-17/)（私密私信）的删除指南**（[PR #2260](https://github.com/nostr-protocol/nips/pull/2260)）：提议通过 gift wrap 删除 event 来编辑和删除私密消息的具体路径。工作仍在进行中，但如果 NIP-17 要完全取代旧的 DM 流程，客户端作者需要这里的答案。

- **[NIP-222](/zh/topics/nip-222/) 的分享意图 URI**（[PR #2266](https://github.com/nostr-protocol/nips/pull/2266)）：该草案将标准化移动和桌面应用如何将共享内容传递给 Nostr 客户端。这是当前应用间互操作中最粗糙的边缘之一。

## NIP 深度解析：NIP-94（文件元数据）

[NIP-94](/zh/topics/nip-94/) 将 kind `1063` 定义为文件的一等元数据 event。[规范](https://github.com/nostr-protocol/nips/blob/master/94.md)为该 event 提供了人类可读的 `content` 和机器可读的 tag，包括下载 URL、MIME 类型、哈希、尺寸、预览、后备和存储服务提示。这很重要，因为文件在 relay 上作为独立对象可查询。客户端不必从周围内容中抓取元数据来理解文件是什么。

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

这些 tag 的作用比初看起来要大。`x` 标识提供的文件，而 `ox` 标识在任何服务端转换之前的原始文件。预览 tag 让客户端无需下载完整资产即可构建可浏览的文件索引，`summary` 可以在旁边携带简短摘录。`fallback` 在主 URL 失败时提供第二来源，`service` 提示文件背后的存储协议，如 [NIP-96](/zh/topics/nip-96/) 或其他主机。因此，NIP-94 位于社交发布之下和原始存储之上。它描述的是文件，而非围绕文件的对话。

这就是为什么本周的 Notedeck 更新器很有趣。[PR #1326](https://github.com/damus-io/notedeck/pull/1326) 使用签名的 kind `1063` event 进行软件版本发现，然后根据发布的 SHA256 验证下载的二进制文件。相同的 event 形状可以描述软件工件或媒体上传。NIP-94 已经足够老到稳定，但它仍有增长空间，因为越来越多的项目将元数据 event 视为面向机器的传输方式，而不仅仅是面向人的装饰。

## NIP 深度解析：NIP-54（Wiki）

[NIP-54](/zh/topics/nip-54/) 将 kind `30818` 定义为 wiki 文章 event。[规范](https://github.com/nostr-protocol/nips/blob/master/54.md)将 `d` tag 视为规范化的文章主题，允许多个作者为同一主题发布条目。文章正文位于 `content` 中，而 tag 处理规范化标识、显示标题、摘要和对早期版本的引用。这意味着 NIP-54 不仅是一种内容格式，它也是一个检索和排名问题，因为每个客户端仍然需要决定显示哪个文章版本。

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

本周的合并将规范标记从 Asciidoc 改为 Djot（[PR #2242](https://github.com/nostr-protocol/nips/pull/2242)）。这对实现者很重要，因为 Djot 有更紧凑的独立规范和跨语言更简单的解析器方案。合并的文本还澄清了引用式 wikilink 如何解析、合并请求如何使用 kind `818`、重定向如何使用 kind `30819`，以及 `d` tag 规范化对非拉丁文字应如何处理。这些是让两个独立客户端就链接指向哪篇文章达成一致的部分。

NIP-54 在协议中也处于一个不寻常的位置。Wiki 客户端需要内容渲染，但它也需要排名策略。回应、relay 列表、联系人列表和显式尊重信号都会影响哪篇文章在给定主题上获胜。Djot 切换不解决排名问题，但它确实移除了位于其下方的解析器歧义之一。这就是为什么合并现在很重要：变更与其说是关于更好的散文格式，不如说是关于使多客户端 wiki 行为更容易一致地实现。

正在构建什么，或想让我们报道？通过 [NIP-17](/zh/topics/nip-17/) 私信在 Nostr 上联系我们：`npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`。
