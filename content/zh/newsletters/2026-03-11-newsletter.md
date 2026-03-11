---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Shopstr](https://github.com/shopstr-eng/shopstr) 和 [Milk Market](https://github.com/shopstr-eng/milk-market) 为 agent 驱动商务增加了 MCP 接口，而 [OAuth Bunker](https://github.com/flox1an/oauth-bunker)、[Amber](https://github.com/greenart7c3/Amber) 和 [strfry](https://github.com/hoytech/strfry) 则在应用、签名器和 relay 软件中增加了 [NIP-42](/zh/topics/nip-42/)（客户端到 relay 的身份验证）relay-auth 与受保护事件支持。[Route96](https://github.com/v0l/route96) 围绕 AI 标注发布了两个版本，加入审核队列、感知哈希和机器可读的服务器文档。[Samizdat](https://github.com/satsdisco/samizdat) 已经在 Web 端上线，本周发布了首个 Android alpha，随后又加入了 [NIP-55](/zh/topics/nip-55/)（Android 签名器应用）支持。[Formstr](https://github.com/formstr-hq/nostr-forms) 通过 [NIP-49](/zh/topics/nip-49/)（私钥加密）增加注册流程，[Amethyst](https://github.com/vitorpamplona/amethyst) 发布了基于 Namecoin 的 [NIP-05](/zh/topics/nip-05/)（域名验证）解析实现，[Mostro](https://github.com/MostroP2P/mostro) 发布 [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)，NIPs 仓库则合并了 [NIP-91](/zh/topics/nip-91/)（过滤器的 AND 运算符）以及针对 [NIP-66](/zh/topics/nip-66/)（relay 发现与活性监控）的防御性指南。

## 新闻

### Shopstr 和 Milk Market 开放 MCP 商务接口

[Shopstr](https://github.com/shopstr-eng/shopstr) 是一个支持 Lightning 和 Cashu 支付的点对点市场，本周合并了 [PR #234](https://github.com/shopstr-eng/shopstr/pull/234)（[commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)），增加了一个带 API key 认证的 MCP 服务器，用于 agent 账户管理。该变更加入了用于 agent 发现的 `.well-known/agent.json`、MCP onboarding 和状态端点、订单创建与支付验证路由，以及专门的购买和读取工具、API key 设置界面。[PR #236](https://github.com/shopstr-eng/shopstr/pull/236) 进一步扩展了卖家侧操作，支持消息、地址、订单更新和商品规格选择。[PR #235](https://github.com/shopstr-eng/shopstr/pull/235) 还修复了一个安全问题，将单次迭代的 SHA-256 API key 哈希替换为带 salt 且迭代 100,000 次的 PBKDF2。

Agent 现在可以读取 [NIP-99](/zh/topics/nip-99/)（分类信息）列表，并通过现有的 [NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）和 [NIP-60](/zh/topics/nip-60/)（Cashu Wallet）支付流程完成结账，而无需抓取页面或反向分析客户端行为。

[Milk Market](https://github.com/shopstr-eng/milk-market) 是运行在 [milk.market](https://milk.market) 上的 Nostr 食品市场，在 [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3) 中加入了同样的 MCP 与 API key 基础。[PR #10](https://github.com/shopstr-eng/milk-market/pull/10) 增加了订阅订单、购买后修改收货地址，以及适用于 Stripe 和其他法币支付路径的多商户、多币种结账支持。随后 [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) 修复了一个启动时的数据库初始化 bug：全新安装时没有创建 failed relay publishes 表，导致首次加载出现 500 错误。这个面向 agent 的接口现在既可配合 Shopstr 的 Bitcoin 原生结账，也可用于 Milk Market 的法币与 Bitcoin 混合结账流程。

### NIP-42 relay 身份验证覆盖 Bunker、签名器和 relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker) 是一个将 OAuth 提供商桥接到 Nostr 签名的 [NIP-46](/zh/topics/nip-46/)（Nostr Connect）bunker，本周加入了 [NIP-07](/zh/topics/nip-07/)（浏览器扩展签名器）登录、自动单身份选择，以及删除身份后的清理逻辑（[commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)）。当只存在一个身份时，bunker 现在会自动选中它，而不是继续提示用户。删除某个身份时，也会一并移除其悬空的分配和连接。[Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) 又为已分配用户加入了 `ALWAYS_ALLOWED_KINDS` 配置路径，默认允许 kind `30078` 应用专用数据，从而让被委托的身份可以在无需逐条审批 event 的情况下写入应用专用存储。

[Amber](https://github.com/greenart7c3/Amber) 是 Android 平台上主要的 [NIP-55](/zh/topics/nip-55/) 签名器，本周发布了 [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4)，整周共有四个预发布版本。[PR #317](https://github.com/greenart7c3/Amber/pull/317) 为 kind `22242` 请求增加了 [NIP-42](/zh/topics/nip-42/) relay 身份验证处理。该实现新增了一个数据库列来跟踪 relay 级权限，并在 `(pkKey, type, kind, relay)` 上建立唯一索引。用户会看到一个专门的身份验证界面，可以按 relay 或通过通配符 `*` 范围对所有 relay 统一授权或拒绝，并将该选择持久化。通配符权限会清除该 kind 下所有 relay 专属条目。[PR #318](https://github.com/greenart7c3/Amber/pull/318) 随后重构了多事件请求界面，改为用 composable 卡片内联显示详情，而不是跳转到单独页面。该版本还更新了默认 profile relays，加入 bottom-sheet 请求显示，并通过禁用 StrongBox keystore 修复了 MediaTek 设备上的崩溃。

在 relay 端，[strfry PR #156](https://github.com/hoytech/strfry/pull/156) 实现了用于 [NIP-70](/zh/topics/nip-70/)（受保护事件）的 NIP-42 身份验证处理，[PR #176](https://github.com/hoytech/strfry/pull/176) 则会拒绝嵌入受保护事件的 repost。

### Notedeck 增加 NIP-11 relay 限制和 Agentium 功能

[Notedeck](https://github.com/damus-io/notedeck) 是 Damus 团队开发的原生桌面客户端，本周合并了 14 个 PR。[PR #1316](https://github.com/damus-io/notedeck/pull/1316) 增加了 [NIP-11](/zh/topics/nip-11/)（relay 信息文档）限制抓取，使所有 outbox relays 现在都会遵守 relay 信息文档中的 `max_message_length` 和 `max_subscriptions`。该实现包括后台作业处理、带抖动的指数退避重连，以及自定义 HTTP Accept 头。[PR #1312](https://github.com/damus-io/notedeck/pull/1312) 修复了切换账户后私信有时无法加载的 bug，[PR #1333](https://github.com/damus-io/notedeck/pull/1333) 则为多播 relay 通信加入退避机制，防止出错时发生广播 spam。

Agentium 子系统，也就是 Notedeck 内置的编码 agent UI，内部代号为 "Dave"，本周新增了剪贴板图片粘贴、通过 kind `31991` event 跨设备同步的命名运行配置（[NIP-33](/zh/topics/nip-33/)（参数化可替换事件））、git worktree 创建器，以及按会话选择后端的 model picker（[PR #1336](https://github.com/damus-io/notedeck/pull/1336)）。[PR #1338](https://github.com/damus-io/notedeck/pull/1338) 集成了 `egui_kittest`，用于无头 UI 测试，[PR #1339](https://github.com/damus-io/notedeck/pull/1339) 则增加了一张 dashboard 卡片，用于跟踪各客户端中新联系人列表的创建情况。仍在开放中的 [PR #1314](https://github.com/damus-io/notedeck/pull/1314) 正将 Amethyst 的 Namecoin NIP-05 解析移植到 Notedeck，包括 ElectrumX 查询、SOCKS5 Tor 路由和搜索栏集成。

### diVine 发布 v1.0.6，加入 E2E 测试基础设施和 NIP-49 导入

[diVine](https://github.com/divinevideo/divine-mobile) 是一个短视频循环客户端，用于恢复 Vine 档案，运行于 [divine.video](https://divine.video)。项目发布了 [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6)，其中包含 127 个已合并 PR。该版本增加了 [NIP-49](/zh/topics/nip-49/) 账户导入、外部 [NIP-05](/zh/topics/nip-05/) 支持、多账户处理，以及由本地存储驱动的重新设计 drafts 与 clips 库，同时还加入了 macOS 和实验性 Linux 构建。

在工程侧，[PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) 增加了一整套 E2E 集成测试基础设施，使用 Patrol 对 Docker 后端栈（relay、API、Blossom、Postgres、Redis、ClickHouse）进行原生 UI 自动化。五个认证流程测试覆盖了注册、验证、密码重置、会话过期和 token 刷新。[PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) 将视频加载从优先 HLS 切换为优先直接 MP4，并在失败时自动回退到 HLS，将加载时间从 30-60 秒降到接近瞬时。[PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) 将首页 feed API 响应缓存到 SharedPreferences，实现冷启动即时显示。[PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) 强制将 `ai-generated` 内容标签在 feed 中隐藏，[PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) 则增加了一个安全设置，只显示 diVine 托管的视频。Hive 到 Drift 的 profile 缓存迁移也在 [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881)、[PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) 和 [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903) 中持续推进，用 Drift DAO 替换了约 1,074 行 Hive 代码。

### Vector v0.3.2 发布 NIP-77 negentropy 同步和 MLS 改进

[Vector](https://github.com/VectorPrivacy/Vector) 是一个注重隐私的桌面消息客户端，使用 MLS 群组加密，并结合 [NIP-17](/zh/topics/nip-17/)（私密直接消息）与 [NIP-44](/zh/topics/nip-44/)（加密载荷）加密，现已发布 [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2)。此次最主要的更新是用于 MLS 群组同步的 NIP-77 negentropy（[commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)），借助并行启动可显著更快地补齐漏掉的消息。该版本还加入了重建后的音频引擎和完整 Linux 支持、带模糊预览的图片 spoiler、可点击超链接与富链接预览、支持群组管理员 `@everyone` 的 `@mention` 提醒、emoji shortcode 自动补全、群组静音、对现有回应进行点击回应，以及可取消的文件上传。Vector 还明确过滤掉 NIP-17 群聊事件（[commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)），在群组加密场景中只使用 MLS。

## 版本发布

### Route96 v0.5.0 和 v0.5.1

[Route96](https://github.com/v0l/route96) 是一个支持 Blossom 和 [NIP-96](/zh/topics/nip-96/)（HTTP 文件存储）的媒体服务器，现已发布 [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) 和 [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1)。v0.5.0 增加了自动 AI 标注、对未标注上传内容的追溯补填、针对被标记文件的审核队列、基于 EXIF 的隐私拒绝，以及被禁哈希处理。

v0.5.1 增加了感知图像哈希、用于相似图像查找的局部敏感哈希、批量管理员端点，以及一份已发布的 [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1)，描述该服务器面向 agent 工具的 Blossom 与 NIP-96 API 接口。[PR #58](https://github.com/v0l/route96/pull/58) 将后台 worker 迁移到完全异步的 Tokio task，[commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) 则加入退避机制以避免热循环。

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat) 是一个长文阅读和发布应用，可在 [samizdat.press](https://samizdat.press) 使用，现已在 [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha) 中发布首个 Android 构建。应用默认打开的是一个精心策划的 Press 页面，展示 Nostr 长文内容，并通过底部标签页在 Press、Feed、Saved 和 Write 视图之间切换。Android 版本加入了通过 Android Keystore 加密并配合生物识别解锁的原生密钥存储，支持处理 `nostr:` URI 和 `samizdat.press` 深链接，并通过 Android 应用选择器完成签名器交接（Amber、Primal 等），而无需直接导入密钥。下拉刷新、不同屏幕尺寸下的 safe-area 处理，以及原生 share、剪贴板、haptics 和启动画面集成，现在都在 Android shell 中完成，而不再依赖 Web wrapper。

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) 为 Amber 和 Primal 流程加入了基于 intent 的 [NIP-55](/zh/topics/nip-55/) 签名支持，[commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) 则用一个基于 `startActivityForResult` 的原生 Capacitor 插件替代了 JavaScript bridge 变通方案。该应用要求 Android 7.0+（API 24），当前 alpha 以 debug APK 形式发布，仍然缺少 push notifications。发布内容目前仍依赖签名器应用，而 `nsec` 登录则覆盖本地阅读与账户访问。

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) 是一个去中心化日历应用，支持通过 [NIP-59](/zh/topics/nip-59/)（Gift Wrap）共享私密事件，可在 [calendar.formstr.app](https://calendar.formstr.app) 使用。项目已随 [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38) 发布 [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0)。该版本扩展了对 [NIP-52](/zh/topics/nip-52/)（日历事件）重复事件的处理，超越了 v0.1.0 仅支持单个事件的基础。底层改动还涉及本地事件存储、签名器处理以及 Android 通知管线。这是 Formstr 组织在上月仓库迁移后的第二个活跃应用。

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro) 是一个基于 Nostr 的点对点 Bitcoin 交易所，已发布 [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)。上周[已报道](/zh/newsletters/2026-03-04-newsletter/)的争议会话恢复（[PR #599](https://github.com/MostroP2P/mostro/pull/599)）和自动关闭（[PR #606](https://github.com/MostroP2P/mostro/pull/606)）修复已包含在此版本中。这个版本的新内容包括：[PR #625](https://github.com/MostroP2P/mostro/pull/625) 为 kind `38384` 的用户评分事件增加 `days` 字段，[PR #612](https://github.com/MostroP2P/mostro/pull/612) 为这些评分事件增加过期时间，[PR #614](https://github.com/MostroP2P/mostro/pull/614) 则将订单事件切换为使用可配置的过期设置，而不是硬编码 24 小时窗口。[PR #622](https://github.com/MostroP2P/mostro/pull/622) 还增加了幂等性检查，以防止重复支付开发费用。

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile) 是 Mostro P2P 交易所的 Flutter 客户端，现已发布 [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1)，包含 11 项新功能和 11 项 bug 修复。该版本加入了争议聊天中的加密多媒体渲染（[PR #514](https://github.com/MostroP2P/mobile/pull/514)）、当订单进入终态时自动关闭争议 UI（[PR #503](https://github.com/MostroP2P/mobile/pull/503)）、用于导入 NWC 钱包的二维码扫描（[commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)）、法语翻译，以及 FCM push notification 处理。[PR #496](https://github.com/MostroP2P/mobile/pull/496) 通过将 bip340 依赖固定到 v0.2.0，修复了一个 Schnorr 签名填充 bug。

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main) 是一个支持 Cashu 的 Telegram 风格消息客户端，现已发布 [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release)，重点修复 Linux 桌面问题，包括 AppImage dock 图标、emoji 渲染、上下文菜单卡死，以及 reply/copy UI 卡顿。该版本还修复了图片上传问题和 npub.cash 集成。[PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) 删除了一个每 3 秒触发一次、却没有实际工作的轮询定时器，从而消除了不必要的 UI 重建和 glassmorphic 重绘；同时它还通过并发加载 event 缓存，而不是阻塞 relay、联系人和频道启动，解除了登录初始化阻塞。

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android) 是一个支持 [NIP-55](/zh/topics/nip-55/) 和 [NIP-46](/zh/topics/nip-46/) 的 Android FROST 门限签名器，现已发布 [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) 和 [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1)。v0.6.0 增加了钱包描述符协调与管理 UI、带生物识别认证的备份/恢复流程（[PR #184](https://github.com/privkeyio/keep-android/pull/184)）、从门限份额恢复 nsec（[PR #187](https://github.com/privkeyio/keep-android/pull/187)）、通过 Rust UniFFI 跨平台生成动画 QR 边框（[PR #188](https://github.com/privkeyio/keep-android/pull/188)），以及带链式验证的签名审计轨迹（[PR #189](https://github.com/privkeyio/keep-android/pull/189)）。v0.6.1 则在 [PR #191](https://github.com/privkeyio/keep-android/pull/191) 中将许可证从 AGPL-3.0 切换为 MIT。

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump) 是用于在 [njump.me](https://njump.me) 查看 Nostr 内容的静态网关，现已发布 [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0)，其中包含 `note1` 代码解析的破坏性变更，以及对底层 nostr 库的更新。

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr) 是一个使用 Nostr 的去中心化道路事件报告应用，现已发布首个演示版本 [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1)。该应用使用 openfreemap.org 的矢量瓦片在地图上显示道路事件。

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core) 是一个拥有 Nostr 传输层和专用 relay 的电子票据应用，可在 [bit.cr](https://www.bit.cr/) 使用，现已发布 [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)。[PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) 为 API 增加了 `payment_actions` 和 `bill_state` 字段，用于表示支付和接受状态，[PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) 则修复了匿名签名器的签名地址处理。

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat) 是一个基于 Marmot 协议 .NET MLS 和 C# 库构建的聊天应用，现已发布 [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3)。该版本增加了对 Amber 和 [NIP-46](/zh/topics/nip-46/) 流程的外部签名器支持（[commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)），将 MLS 状态持久化移入 MLS service 以消除崩溃窗口中的数据丢失（[commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)），并通过新的 CI pipeline 发布 Windows、Linux 和 Android 构建。

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal) 是一个面向 Nostr 的 Kotlin Multiplatform 交易 copilot，现已发布 [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0)。该版本打包了跨桌面和 Android shell 共享的 KMP 模块，覆盖领域逻辑、图表渲染、Nostr 身份验证与发布、Blossom [NIP-96](/zh/topics/nip-96/) 上传支持，以及基于 ONNX 的 AI 推理 hook。其公开架构还包括一个 FastAPI AI 服务，用于图表截图分析、模型训练管线，以及生成结构化交易计划、仓位大小和风险警告的风险引擎。登录既支持原始 `nsec` 密钥，也支持外部签名器，输出流程最终以 Nostr event 发布结束，而不是只停留在本地分析。

## 项目更新

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms) 是 Nostr 上的 Google Forms 替代品，本周合并了 [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434)（[commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)），增加了一个基于 [NIP-49](/zh/topics/nip-49/)（私钥加密）的注册流程。这个变更之前，用户必须依赖 [NIP-07](/zh/topics/nip-07/) 浏览器扩展或直接粘贴原始 `nsec` 才能使用 Formstr。新流程会在客户端生成密钥对，用 NIP-49 的 scrypt + XChaCha20-Poly1305 方案和用户选择的密码加密私钥，并保存生成的 `ncryptsec` 字符串。之后用户无需安装签名器扩展，只需输入密码即可再次登录。整个密钥管理流程始终留在客户端侧。

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst) 是一个功能丰富的 Android 客户端，本周合并了四个 PR，交付了上周[仍处于开放状态](/zh/newsletters/2026-03-04-newsletter/)的 Namecoin 支持 [NIP-05](/zh/topics/nip-05/) 解析工作。[PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) 为 `.bit`、`d/` 和 `id/` 标识符增加了通过 ElectrumX 实现的抗审查 NIP-05 验证。当 Amethyst 在 NIP-05 字段中检测到这些后缀之一时，它会查询 ElectrumX-NMC 服务器获取该名称的交易历史，从最新输出中解析 `NAME_UPDATE` 脚本以提取 Nostr pubkey，并拒绝超过 36,000 个区块的名称，也就是 Namecoin 的过期窗口。启用 Tor 时，ElectrumX 连接会通过 SOCKS5 路由，并在 clearnet 与 `.onion` 端点之间动态选择服务器。一个 TTL 为一小时的 LRU 缓存则用来避免重复的区块链查询。

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) 修复了这一流程中的竞态条件和解析正确性问题。[PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) 让新用户在注册时可以从普通 NIP-05 标识符或 Namecoin 支持的标识符导入关注列表。[PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) 则增加了自定义 ElectrumX 服务器设置，让用户自行选择由哪个服务器执行查询。

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb) 是一个为在 IndexedDB 中存储 Nostr event 提供辅助方法的库，本周合并了 [PR #6](https://github.com/hzrd149/nostr-idb/pull/6)，加入对 [NIP-91](/zh/topics/nip-91/) AND tag 过滤器的支持。该变更为客户端侧过滤器匹配增加了交集语义，使 IndexedDB 查询能够要求列出的所有 tag 值都匹配，而不是命中任意一个。[PR #8](https://github.com/hzrd149/nostr-idb/pull/8) 将该库更新到最新的 NIP-DB 接口，后续的 [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) 则修复了 subscribe 死锁，并移除了 nostr-tools 的生产依赖。

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve) 是一个以归档优先为设计的 Nostr 索引器，并带有 ClickHouse 分析能力。本周它合并了 [PR #8](https://github.com/andotherstuff/pensieve/pull/8)，增加按条目执行的缓存 TTL 和按 key 合并 miss 的机制，以减少 API CPU 峰值。成本最高的时间序列端点，包含 engagement stats、按小时活动和按 kind 活动，现在统一使用 10 分钟的服务端 TTL，而不再触发同步重算风暴。

### Blossom

[Blossom](https://github.com/hzrd149/blossom) 是一个去中心化媒体托管协议和服务器栈，本周合并了两个 BUD-11 授权更新。[PR #91](https://github.com/hzrd149/blossom/pull/91) 将可选授权拆分到独立的 BUD 中，并澄清了 `x` 和 `server` 标签的角色。[PR #93](https://github.com/hzrd149/blossom/pull/93) 清理了按端点区分的身份验证行为，并正式定义用于上传校验的 `X-SHA-256` 头。这两个 PR 将授权逻辑集中到 BUD-11 中，并移除了上传、删除和媒体管理流程中关于请求哈希的歧义。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-91](/zh/topics/nip-91/)（过滤器的 AND 运算符）**（[PR #1365](https://github.com/nostr-protocol/nips/pull/1365)）：为 tag 过滤器增加交集语义，使 relay 能够回答那些要求列出的所有 tag 值都同时匹配的查询，而不是匹配任意一个。这减少了客户端侧的后过滤和 tag 密集型查询的带宽消耗。

- **[NIP-66](/zh/topics/nip-66/)（relay 发现与活性监控）：防御措施**（[PR #2240](https://github.com/nostr-protocol/nips/pull/2240)）：在上周[报道过的 outbox 基准测试工作](/zh/newsletters/2026-03-04-newsletter/)之后，规范现在加入了关于 relay 监控数据不利场景的警告。客户端不得要求 kind `30166` 监控事件存在才能正常工作。监控者可能出错、过时或带有恶意。客户端应交叉验证信息来源，避免仅根据单一数据流就切断用户 relay 图中的大部分部分。

- **[NIP-39](/zh/topics/nip-39/)（个人资料中的外部身份）：kind 10011 注册表清理**（[PR #2256](https://github.com/nostr-protocol/nips/pull/2256)）：将 kind `10011` 的引用直接加入规范，与上周[报道过的](/zh/newsletters/2026-03-04-newsletter/) Amethyst 实现保持一致。

**开放 PR 和讨论：**

- **[NIP-70](/zh/topics/nip-70/)（受保护事件）：拒绝嵌入受保护事件的 repost**（[PR #2251](https://github.com/nostr-protocol/nips/pull/2251)）：如果 relay 对原始事件执行 NIP-70，但仍接受携带相同内容的 repost，那么 `-` 标签就失去了实际效果。该 PR 增加了一条规则，要求 relay 也必须拒绝 kind 6 和 kind 16 对受保护事件的 repost。[strfry PR #176](https://github.com/hoytech/strfry/pull/176) 已经实现了这一点。

- **[NIP-71](/zh/topics/nip-71/)（视频事件）：多音轨**（[PR #2255](https://github.com/nostr-protocol/nips/pull/2255)）：增加音频 `imeta` 标签，用于表示替代音轨、语言变体和纯音频流。客户端可以在保持视频文件稳定的同时切换音频语言，也可以为播客式内容将音频作为单独轨道提供。

- **[NIP-11](/zh/topics/nip-11/)（relay 信息文档）和 [NIP-66](/zh/topics/nip-66/) relay 属性**（[PR #2257](https://github.com/nostr-protocol/nips/pull/2257)）：为 relay 信息文档增加结构化 `attributes` 字段，使客户端和发现工具能够获得超越当前自由文本描述的机器可读元数据。

## NIP 深度解析：NIP-49（私钥加密）

[NIP-49](/zh/topics/nip-49/) 定义了客户端如何用密码加密私钥，并将结果编码为 `ncryptsec` bech32 字符串。[Formstr](#formstr) 已在其新的注册流程中使用 NIP-49。

该格式不绑定某个专用 event kind。客户端从原始的 32 字节 secp256k1 私钥开始，使用 scrypt 从用户密码派生对称密钥，再用 XChaCha20-Poly1305 加密该私钥，最后将结果封装为 bech32 `ncryptsec` 字符串。其中一个字节的标志位会记录该密钥在加密前是否曾被确认以不安全方式处理过。

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

上面的 JSON event 是应用层示例，并非 NIP-49 的强制要求。这个 NIP 规范化的是加密密钥格式本身，而不是某个专门用于发布它的 event kind。客户端可以将 `ncryptsec` 存在本地，通过应用专用存储同步，或将其作为备份字符串导出。密码在派生密钥之前会先归一化为 Unicode NFKC，这样相同密码在不同客户端和平台上都能稳定解密。

这个一字节的密钥安全标志定义了三种值：`0x00` 表示该密钥的处理历史未知，`0x01` 表示该密钥已知曾以不安全方式处理过，例如在加密前以明文形式粘贴到 Web 表单中，`0x02` 表示该密钥是在安全上下文中生成并加密，且从未暴露。客户端可以利用这一点，在导入具有已知不安全历史的密钥时显示警告。

与明文 `nsec` 导出相比，NIP-49 对密钥提供了更好的保护，但加密强度仍取决于密码强度和配置的 scrypt 成本。更高的 `LOG_N` 值会让离线猜测更困难，但也会减慢合法的解密操作。规范明确警告不要把加密密钥发布到公共 relay，因为攻击者收集到越多密文，就越有利于进行离线破解。作为对比，[NIP-46](/zh/topics/nip-46/) 远程签名完全避免暴露密钥，[NIP-55](/zh/topics/nip-55/) Android 签名则把密钥保留在专用签名器应用中。NIP-49 填补的是另一个位置：为自行管理密钥的用户提供可移植的加密备份。

相关实现包括：用于注册流程的 [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434)、用于 `ncryptsec` 备份和恢复的 [Amber](https://github.com/greenart7c3/Amber)、用于账户导入的 [diVine v1.0.6](#divine-发布-v106加入-e2e-测试基础设施和-nip-49-导入)、用于 FROST 份额导出的 [Keep v0.6.0](#keep-v060)，以及诸如 [nsec.app](https://nsec.app) 和 [Alby](https://github.com/getAlby/hub) 这样的密钥管理工具。

## NIP 深度解析：NIP-70（受保护事件）

[NIP-70](/zh/topics/nip-70/) 定义了受保护事件。当一个 event 带有 `[["-"]]` 标签时，relay 必须拒绝它，除非该 relay 要求 [NIP-42](/zh/topics/nip-42/) 身份验证，并且通过身份验证的 pubkey 与 event 作者匹配。

NIP-42 的身份验证流程如下：relay 发送一个包含随机字符串的 `AUTH` challenge，客户端则回应一个签名过的 kind `22242` event，其标签中包含 relay URL 和该 challenge。relay 验证签名，并检查认证事件中的 pubkey 是否与待发布的受保护事件中的 pubkey 相匹配。如果 pubkey 不匹配，relay 会使用 `restricted` 消息前缀拒绝该事件。

事件内容本身仍然可以是公开可读的。`-` 标签只控制谁可以把该事件发布到遵守该标签的 relay。这覆盖了 [NIP-29](/zh/topics/nip-29/)（简单群组）半封闭信息流、仅成员可见的 relay 空间，以及其他作者希望通过 relay 图限制再分发的场景。NIP-70 只是一个单标签约定，而不是新的 event kind，因此任何现有 event kind 都可以携带 `-` 标签。

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

即使 relay 阻止第三方发布原始事件，别人仍然可以把内容嵌入 repost 再次发布。[PR #2251](https://github.com/nostr-protocol/nips/pull/2251) 通过要求 relay 同时拒绝 kind 6 和 kind 16 对受保护事件的 repost 来解决这一问题。[strfry PR #156](https://github.com/hoytech/strfry/pull/156) 为受保护事件加入了 NIP-42 身份验证处理，[strfry PR #176](https://github.com/hoytech/strfry/pull/176) 则会阻止嵌入受保护内容的 repost。

NIP-70 约束的是 relay 行为。接收者仍然可以把内容复制到其他地方，规范本身也明确承认这一点。`-` 标签给 relay 一个机器可读的信号，用来拒绝再次发布。作为对比，[NIP-62](/zh/topics/nip-62/)（消失请求）是请求 relay 事后删除数据，而 NIP-70 则是在摄入时阻止未授权发布。两者是互补的：作者可以先把事件标记为受保护，以限制传播，之后如果希望已接受该内容的 relay 删除它，还可以再提出删除请求。

---

本周就到这里。正在构建什么，或者有新闻想分享？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">欢迎通过 [NIP-17](/zh/topics/nip-17/) 私信联系我们</a>，或直接在 Nostr 上找到我们。
