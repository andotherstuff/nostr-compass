---
title: 'Nostr Compass #3'
date: 2025-12-31
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 协议生态指南。

**本周：** 在 2025 年收官之际，我们回顾 Nostr 演进中五个十二月的关键里程碑。从 2020 年 12 月 fiatjaf 发布首个客户端，到 2022 年 12 月 Jack Dorsey 关键性的 14 BTC 捐赠，再到本月 NIP-55 签名器的扩散以及 NDK 162 倍缓存提速，十二月持续成为协议转折点。本期特别回顾按年份梳理这段技术历史，记录协议如何从两个实验性 relay 成长为横跨 50 个国家的 2500 多个节点。此外还有：Amethyst 的桌面模块借助 Quartz 初具形态，Notedeck 增加消息功能，Citrine 可托管 Web 应用，以及 NIP-54 为非拉丁文字修复国际化问题。

## 12 月回顾：Nostr 五个十二月

今年是 Nostr 诞生第五年。fiatjaf 于 2020 年 11 月 7 日发起该协议，而此后的每一个十二月都标记了其演进中的不同阶段：从概念验证，到全球运动，再到生产级生态系统。下面这篇技术回顾覆盖 2020 年 12 月到 2025 年 12 月，这些奠基年份共同塑造了 Nostr 的基础，并催化了它的突破时刻。

### 2020 年 12 月：起源

Nostr 存在后的第一个完整月份里，fiatjaf 发布了 [Branle](https://github.com/fiatjaf/branle)，这是协议的首个客户端，基于 Quasar（Vue.js）和 absurd-sql 构建，用于本地存储。fiatjaf 当时已经确立了核心架构：用户以 secp256k1 公钥作为身份，所有帖子都带有密码学签名，relay 作为彼此不通信的无状态存储层存在。一个或两个实验性 relay 为一小批早期采用者提供服务，他们在 11 月 16 日启动的 Telegram 群组 [@nostr_protocol](https://t.me/nostr_protocol) 中协作。最初的[文档](https://fiatjaf.com/nostr.html)将其描述为“能够创建抗审查全球社交网络的最简单开放协议”，而这一前提还需要再过两年才被真正证明。

### 2021 年 12 月：早期开发

2021 年 12 月 31 日，Nostr 由 Cameri 提交到 [Hacker News 首页](https://news.ycombinator.com/item?id=29749061)，获得 110 分和 138 条评论。这标志着协议首次在更广泛的开发者社区中获得显著曝光。网络大约运行在七个 relay 上，用户不到 1000 人。Branle 收到多项更新，包括私钥导入功能（12 月 31 日）和多 relay 支持。命令行客户端 noscl 则提供了基于终端的交互方式。协议规范当时仍存在于 fiatjaf 的文档中，而正式的 [NIPs 仓库](https://github.com/nostr-protocol/nips)要到 2022 年 5 月才会创建。正如 fiatjaf 所说，当时的协议仍然“还在开发中”。

### 2022 年 12 月：临界点

2022 年 12 月让 Nostr 从小众实验变成主流运动。催化剂出现在 12 月 15 日，Jack Dorsey 在发现该协议后，宣布它“百分之百就是我们原本希望 Bluesky 成为的东西，只是不是由一家公司开发出来”，并向 fiatjaf 捐赠了 [14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding)（约 24.5 万至 25 万美元）。12 月 16 日，fiatjaf 宣布将资金与 Damus 开发者 William Casarin（jb55）分配使用，Dorsey 也验证了自己的 Nostr 账户（npub：`npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`）。这笔资金几乎在一夜之间赋予了项目正当性。

同一周，Twitter 的混乱加速了采用。12 月 14 日至 15 日，《纽约时报》、CNN 和《华盛顿邮报》的知名记者遭遇封禁。12 月 18 日，Twitter [宣布禁止](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/)推广 Nostr、Mastodon 及其他平台的账户。该政策在次日因反弹而撤回。这波出走潮推动更多用户开始寻找替代方案。

协议开发也迅速升温。12 月 16 日，[NIP-19](/zh/topics/nip-19/) 合并（[#57](https://github.com/nostr-protocol/nips/pull/57)），引入了 bech32 编码标识符（npub、nsec、note、nprofile、nevent），使密钥变得可读且彼此可区分。NIPs 仓库当月记录了 36 次以上提交，其中包括 NIP-40 和 NIP-07 的更新。客户端也开始扩散：Damus 的 TestFlight beta 在数小时内满员，Astral 从 Branle 分叉以支持资料创建，Snort 作为“快速、抗审查”的 Web 客户端上线，Vitor Pamplona 则开始开发 Amethyst。Alby v1.22.1“Kemble's Cascade of Stars”于 12 月 22 日发布，加入 NIP-19 支持。截至 12 月 7 日，Nostr 约有 800 名拥有资料的用户；当 Damus 于 2023 年 1 月 31 日登陆 App Store 后，增长闸门彻底打开，到 2023 年 6 月用户规模已超过 31.5 万。

### 2023 年 12 月：生态成熟

2023 年 12 月成为 Nostr 协议安全性的关键转折点。12 月 20 日，[NIP-44 第三次修订版合并](https://github.com/nostr-protocol/nips/pull/746)，此前一项独立的 Cure53 安全审计（NOS-01）在 TypeScript、Go 和 Rust 实现中发现了 10 个问题，包括时序攻击和前向保密相关隐患。更新后的规范用 ChaCha20 与 HMAC-SHA256 取代了存在缺陷的 [NIP-04](/zh/topics/nip-04/) 加密，建立起如今支撑 [NIP-17](/zh/topics/nip-17/) 私密私信和 [NIP-59](/zh/topics/nip-59/) Gift Wrap 的密码学基础。同一周，OpenSats 于 12 月 21 日[宣布第四批资助](https://opensats.org/blog/nostr-grants-december-2023)，为 Lume、noStrudel、ZapThreads 以及一项独立的 NIP-44 审计等七个项目提供资金。这延续了其在 2023 年 7 月[第一批资助](https://opensats.org/blog/nostr-grants-july-2023)中对 Damus、Coracle、Iris 等项目的支持，使 Nostr Fund 总分配额达到约 340 万美元，覆盖 39 项资助。

这个月也暴露了生态可持续性的紧张关系。12 月 28 日，William Casarin（jb55）在 [Stacker News](https://stacker.news/items/368863) 上发文称，2024 年“很可能将是 Damus 的最后一年”，理由是“nostr 客户端赚不到钱”，而苹果对应用内 zap 的限制严重压缩了变现空间。Damus 团队此前曾拒绝风投资金。与此同时，[Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1) 于 12 月 26 日发布，在 [NIP-47](/zh/topics/nip-47/) 基础上扩展了 `pay_keysend`、`make_invoice`、`lookup_invoice`、`list_transactions`、`get_balance` 和 `get_info` 方法，为后来成为客户端标准能力的钱包集成打下基础。

### 2024 年 12 月：协议推进

2024 年 12 月以 [Notedeck Alpha 发布](https://damus.io/notedeck/)开场，该版本在 11 月 30 日上线，是 Damus 团队的 Rust 桌面客户端，具备多栏界面和多账户支持。它面向 Linux、macOS 和 Windows 构建，Android 计划在 2025 年推出，最初提供给 Damus Purple 订阅者，代表着团队从 iOS 向外扩展的重要战略。两周后，OpenSats 于 12 月 16 日[宣布第九批资助](https://opensats.org/blog/9th-wave-of-nostr-grants)，资助了 AlgoRelay（首个用于个性化信息流的算法 relay）、Pokey（在受限网络下使用蓝牙 mesh 的 Android 应用）、Nostr Safebox（[NIP-60](/zh/topics/nip-60/) [Cashu](/zh/topics/cashu/) 代币存储）以及 LumiLumi（轻量且注重可访问性的 Web 客户端），将 Nostr Fund 总分配额推高到约 900 万美元，同比增加 67%。

当月还见证了客户端生态的显著成熟。[Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0) 于 12 月 23 日发布，支持 File Metadata（[NIP-92](/zh/topics/nip-92/)/[NIP-94](/zh/topics/nip-94/)）、Blossom 集成以及 [NIP-50](/zh/topics/nip-50/) relay 搜索。[Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0) 于 12 月 12 日发布，加入重做后的新手引导和 nostr-editor 集成。协议开发仍然活跃，12 月 9 日至 22 日间共有 30 个 pull request 提交，其中 10 个合并，包括 [NIP-46](/zh/topics/nip-46/) 重写为仅使用 NIP-44 加密，以及 [NIP-104](/zh/topics/nip-104/) 持续推进，以实现接近 Signal 级别的双棘轮加密。网络统计显示，受信任 pubkey event 日活超过 22.4 万，新建带联系人列表的资料数量同比增长 4 倍，公开写作类 event 增长 50%。

### 2025 年 12 月：生态扩张

2025 年 12 月带来了持续的协议成熟与生态扩张。12 月 21 日，OpenSats [宣布第十四批 Nostr 资助](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)，资助三个项目：YakiHonne（支持长文创作门户并集成 [Cashu](/zh/topics/cashu/)/Nutzaps 支付的多平台客户端）、Quartz（Vitor Pamplona 的 Kotlin Multiplatform 库，为 Amethyst 提供支持并将启用 iOS 版本）以及 Nostr Feedz（由 PlebOne 开发的 RSS 与 Nostr 双向集成）。Dart NDK 和 Mattn 的 nostr-relay 获得续期资助。

协议演进继续推进。[NIP-BE](/zh/topics/nip-be/)（蓝牙低功耗消息，[#1979](https://github.com/nostr-protocol/nips/pull/1979)）已于 11 月合并，使离线设备同步成为可能。[NIP-A4](/zh/topics/nip-a4/)（公开消息，kind 24，[#1988](https://github.com/nostr-protocol/nips/pull/1988)）在本月稍后落地，定义了使用 `q` 标签以避免线程复杂性的通知屏消息。[NIP-29](/zh/topics/nip-29/) 获得重大澄清（[#2106](https://github.com/nostr-protocol/nips/pull/2106)），引入 `hidden` 标签，用于真正私密且不可发现的群组。[NIP-55](/zh/topics/nip-55/) 规范也进行了修订（[#2166](https://github.com/nostr-protocol/nips/pull/2166)），修正了开发者在后台进程中调用 `get_public_key` 的常见实现错误。

客户端侧也有明显进展。[Primal Android 在第2期周刊中报道](/en/newsletters/2025-12-24-newsletter/#news)通过八个已合并 PR 成为完整的 NIP-55 签名器，实现了 `LocalSignerContentProvider`，加入 Amber 和 Aegis，成为 Android 平台的签名选项之一。[NDK 库在第2期周刊中报道](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)通过消除重复写入和不必要的 LRU 缓存查询，将缓存查询速度提升了 162 倍（约 3690ms 降至约 22ms）（[PR #371](https://github.com/nostr-dev-kit/ndk/pull/371)、[PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)）。Shopstr 推出了 [Zapsnags](/en/newsletters/2025-12-24-newsletter/#news)，用于通过 zap 实现闪购。White Noise 发布了 [MIP-05](/zh/topics/mip-05/) 隐私保护推送通知。完整内容可参见[第1期周刊](/en/newsletters/2025-12-17-newsletter/)和[第2期周刊](/en/newsletters/2025-12-24-newsletter/)。

---

五年前，fiatjaf 把 Branle 发布给分布在两个实验性 relay 上的少数用户。今天，这一协议已支撑 140 多个客户端、遍布 50 个国家的 2500 多个 relay，以及不断增长、连接数十万密钥对的信任网络。十二月持续作为重大发布的高峰期，本月蓝牙消息、Android 签名器扩散和基础设施资助再次表明，跨平台工具链仍在获得持续投入。

## 新闻

**Amethyst Desktop 初具形态** - OpenSats 第十四批资助中的 Quartz 项目已经开始产生成果。[PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625) 为 Amethyst 创建了完整的 `:desktopApp` 模块，使用 Compose Multiplatform，并让登录页和全局信息流页面在 Desktop JVM 上可用。该架构把 `:commons` 模块转换为 Kotlin Multiplatform，采用清晰的 source set 结构（`commonMain`、`jvmAndroid`、`androidMain`、`jvmMain`），使 Android 和桌面端可以共享 UI 组件，同时将平台特定决策留给各自目标。这为未来通过同一 Kotlin Multiplatform 路径支持 iOS 奠定了基础。

**Amethyst 语音回复** - davotoula 的圣诞交付：[PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622) 增加了专门的语音回复界面，包含波形可视化、重新录制支持、媒体服务器选择和上传进度指示。用户现在可以用音频回复根语音消息和语音回复。

**Notedeck 增加消息功能** - Damus 的桌面客户端 Notedeck 在 [PR #1223](https://github.com/damus-io/notedeck/pull/1223) 中加入了消息功能，从浏览时间线扩展到了直接通信。

**Citrine 可托管 Web 应用** - Citrine 现在可以[托管 Web 应用](https://github.com/greenart7c3/Citrine/pull/81)，把你的手机变成本地优先的 Nostr Web 服务器。另一个 [PR #85](https://github.com/greenart7c3/Citrine/pull/85) 在网络恢复时加入自动重连和 event 广播，并覆盖多个 Android API 级别的完整测试。

**Nostrability 开发者工具包注册表** - [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264) 跟踪器维护着一个涵盖多种语言（TypeScript、Rust、Python、Go、Dart、Swift 等）的 SDK、库和开发工具精选注册表。如果你刚接触 Nostr 开发，它是为你的技术栈寻找合适工具包的不错起点。

## NIP 更新

最近 [NIPs 仓库](https://github.com/nostr-protocol/nips)中的变更：

- **[NIP-54](/zh/topics/nip-54/)** - Wiki `d` 标签规范化的关键国际化修复（[#2177](https://github.com/nostr-protocol/nips/pull/2177)）。此前的规则会把所有非 ASCII 字符转换为 `-`，导致日文、中文、阿拉伯文、西里尔文及其他文字无法正常工作。更新后的规范保留 UTF-8 字母，仅对有大小写变体的字符执行小写化，并附带了完整示例：`"ウィキペディア"` 保持为 `"ウィキペディア"`，`"Москва"` 变为 `"москва"`，而像 `"日本語 Article"` 这样的混合文字会规范化为 `"日本語-article"`。

## 版本发布

**Zapstore 1.0-rc1** - 基于 Nostr 的免许可应用商店发布了新架构的[首个候选版本](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1)，包含完整 UI 刷新、重写且错误处理更完善的包管理器、用于精选发现的 App Stacks、重新设计的个人资料页、后台更新检查，以及发布列表的无限滚动。

**KeyChat v1.38.1** - 基于 MLS 的加密消息应用[加入 UnifiedPush 支持](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489)，用于 Android 和 Linux 推送通知，并为隐私相关操作增加生物识别认证。可用于 Android、Windows、macOS 和 Linux。

**Alby Go v2.0.0** - 移动 Lightning 钱包伴侣应用[发布视觉重设计](https://github.com/getAlby/go/releases/tag/v2.0.0)，包含新 logo、更新后的配色、重做的地址簿以及改进的金额输入键盘。BTC Map 现在可从首页访问，交易描述也会显示在通知中。

**nak v0.17.4** - fiatjaf 的命令行 Nostr 工具已[发布](https://github.com/fiatjaf/nak/releases/tag/v0.17.4)，延续了上周 v0.17.3 对 Linux 上 LMDB 限制问题的修复。

## 值得关注的代码与文档变更

*值得关注的开放 PR 与早期阶段工作。*

### Damus（iOS）

[NIP-19 relay 提示](https://github.com/damus-io/damus/pull/3477)实现了 event 获取时对 relay hint 的消费。当用户打开 nevent、nprofile 或 naddr 链接时，Damus 现在会从 bech32 TLV 数据中提取 relay hint，并连接临时 relay 去获取不在用户 relay 池中的内容。实现包含基于引用计数的清理逻辑，以避免并发查找时的竞争条件。[图片 URL 检测](https://github.com/damus-io/damus/pull/3474)会把粘贴的图片 URL 自动转换为编辑器中的预览缩略图，并在多图时显示轮播位置标记。[npub 粘贴转换](https://github.com/damus-io/damus/pull/3473)则会把粘贴的 npub/nprofile 字符串转换为 mention 链接，并异步解析资料。

### Amethyst（Android）

[Payment targets](https://github.com/vitorpamplona/amethyst/pull/1627)添加了用于 [NIP-57](/zh/topics/nip-57/) zap 分账的 event 接口，让帖子可以指定多个接收者来共享收到的 zap，这对协作、收入分成或同时打赏内容创作者与所用工具都很有用。[Quartz 功能对齐文档](https://github.com/vitorpamplona/amethyst/pull/1624)新增了一张详细表格，用来跟踪 Android、Desktop JVM 和 iOS 三个目标的功能实现情况，并指出 iOS 仍缺少核心密码学（`Secp256k1Instance`）、JSON 序列化和数据结构。

### Notedeck（桌面）

[时间线过滤器重建](https://github.com/damus-io/notedeck/pull/1226)修复了一个 bug，即已取消关注的账户仍持续出现在信息流中。此前时间线过滤器只在联系人列表生成时构建一次，之后不再更新；该修复增加了 `contact_list_timestamp` 跟踪和 `invalidate()` 方法，以便在关注状态变化时触发重建。

### Citrine（Android Relay）

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86)通过 `ContentResolver` 向其他 Android 应用暴露本地 relay 的 event 数据库。与 WebSocket 接口不同，后者要求应用维持持久连接并实现 Nostr relay 协议，而 ContentProvider 通过 Android 原生 IPC 机制提供直接的同步数据库访问。外部应用可以按 ID、pubkey、kind 或日期范围查询 event，也可以插入经验证的新 event，或删除 event，而无需自行管理 socket 连接。

### rust-nostr（库）

[NIP-40 relay 级支持](https://github.com/rust-nostr/nostr/pull/1183)在 relay builder 层增加了过期处理。过期 event 现在会在写入存储前被拒绝，并在发送给客户端前被过滤掉，从而不再需要每个数据库实现分别处理过期检查。

### nak（CLI）

[Blossom 镜像](https://github.com/fiatjaf/nak/pull/91)为该命令行工具实现了 blob 镜像功能。

### Mostro（P2P 交易）

[开发者费用审计 event](https://github.com/MostroP2P/mostro/pull/559)通过 kind 8383 Nostr event 为开发基金付款增加了透明审计轨迹。实现会在成功支付费用后发布非阻塞审计 event，包含订单详情与支付哈希，同时出于隐私考虑排除买卖双方 pubkey。

### MDK（Marmot Development Kit）

三个安全审计修复已落地：[Author verification](https://github.com/marmot-protocol/mdk/pull/40)强制 rumor pubkey 与 MLS 发送者凭证一致，以防止冒充攻击。[KeyPackage identity binding](https://github.com/marmot-protocol/mdk/pull/41)验证凭证身份与 event 签名者匹配。[Admin update validation](https://github.com/marmot-protocol/mdk/pull/42)则防止空管理员集合与非成员管理员分配。

### Shopstr（Marketplace）

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217)为实物商品实现了更少信任依赖的支付系统。该架构使用 Alby 的 `makeHoldInvoice` 将买家资金锁定在其自己的钱包中，只有在商家确认库存后才触发结算。握手协议通过 [NIP-17](/zh/topics/nip-17/) 加密私信流转：买家发送订单请求，商家返回 HODL invoice，买家支付后资金被锁定，商家确认库存与发货，随后结算释放资金。多商家购物车支持把付款拆分给不同卖家。

### Jumble（Web 客户端）

[按 relay 的发现模式](https://github.com/CodyTseng/jumble/pull/713)增加了一个开关，用于在特定 relay 上隐藏已关注用户的帖子，从而支持基于语言的发现型信息流，例如 nostr.band/lang/*。该功能会过滤掉作者 pubkey 已出现在用户关注列表中的帖子，并把每个 relay URL 的开关状态持久化到 localStorage。

### White Noise（加密消息）

[媒体上传重试](https://github.com/marmot-protocol/whitenoise/pull/937)为失败上传增加了重试选项。[个人资料编辑警告](https://github.com/marmot-protocol/whitenoise/pull/927)提醒用户注意资料变更。在后端，[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422)修复了 AccountGroup 创建过程中的竞争条件。

### npub.cash（Lightning Address 服务）

[v3 重写](https://github.com/cashubtc/npubcash-server/pull/40)将 monorepo 和服务器迁移到 Bun，增加 SQLite 支持，移除对 v1 的兼容，加入 LUD-21，并增加 mint quote 的实时更新。

### nostr-java（库）

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1)通过[两个 PR](https://github.com/tcheeric/nostr-java/pull/499)发布，包含 WebSocket 处理重构和更稳健的测试。

### NIPs 仓库

[NIP-54 Djot 迁移](https://github.com/nostr-protocol/nips/pull/2180)提出对 wiki 规范的另一项改动：把内容格式从 Asciidoc 切换为 Djot，这是一种语法更简洁的轻量标记语言。该 PR 为 wikilink 引入引用式链接，让 wiki 条目之间的交叉引用在源码中更易读。[NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179)则引入基于 FROST（Flexible Round-Optimized Schnorr Threshold signatures）的 Nostr 群组阈值多重签名治理。Quorum 是一个通过 T-of-N 方案在成员之间共享的 nsec，成员可以自己参与，也可以委托给代表委员会。当委员会发生变化时，旧 nsec 会失效，并分发新的 nsec，而旧委员会的最后一个动作就是对治理转换 event 进行签名。规范定义了成员类型（公开或私有）、选举和投票（普选、罢免投票）、可选的自然语言“法律”，以及关键的 quorum ontology，即 quorum 也可以成为其他 quorum 的成员，从而支持地方加入区域机构这类层级结构。其使用场景涵盖源代码开发、公司董事会、业委会和受管理的社区。

---

本周以及今年的内容就到这里。你在构建什么？有新闻想分享？希望我们报道你的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 私信联系我们</a>，或直接在 Nostr 上找到我们。
