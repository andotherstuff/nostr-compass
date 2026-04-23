---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Shopstr](https://github.com/shopstr-eng/shopstr) 与 [Milk Market](https://github.com/shopstr-eng/milk-market) 为 agent 驱动商业增加了 MCP 接口；[OAuth Bunker](https://github.com/flox1an/oauth-bunker)、[Amber](https://github.com/greenart7c3/Amber) 和 [strfry](https://github.com/hoytech/strfry) 则在应用、签名器和 relay 软件中加入了 [NIP-42](/zh/topics/nip-42/)（客户端到 Relay 的认证）relay-auth 与 protected event 支持。[Route96](https://github.com/v0l/route96) 围绕 AI 标注、审核队列、感知哈希与机器可读服务器文档发布了两个版本。[Samizdat](https://github.com/satsdisco/samizdat) 已先在 Web 上线，本周发布首个 Android alpha，随后又加入 [NIP-55](/zh/topics/nip-55/)（Android 签名器应用）支持。[Formstr](https://github.com/formstr-hq/nostr-forms) 通过 [NIP-49](/zh/topics/nip-49/)（私钥加密）增加注册能力，[Amethyst](https://github.com/vitorpamplona/amethyst) 发布基于 Namecoin 的 [NIP-05](/zh/topics/nip-05/)（域名验证）解析工作，[Mostro](https://github.com/MostroP2P/mostro) 发布 [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)，而 NIPs 仓库合并了 [NIP-91](/zh/topics/nip-91/)（过滤器 AND 运算符）以及面向 [NIP-66](/zh/topics/nip-66/)（Relay 发现与存活监测）的防御性指引。

## 新闻

### Shopstr 与 Milk Market 开放 MCP 商业接口

[Shopstr](https://github.com/shopstr-eng/shopstr) 是一个支持 Lightning 与 Cashu 支付的点对点市场，它合并了 [PR #234](https://github.com/shopstr-eng/shopstr/pull/234)（[commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)），加入了一个使用 API key 认证的 MCP 服务器，用于 agent 账户管理。该改动增加了用于 agent 发现的 `.well-known/agent.json`、MCP onboarding 与状态端点、订单创建和支付校验路由，以及专门的购买与读取工具，还有一个用于管理 API key 的设置页面。[PR #236](https://github.com/shopstr-eng/shopstr/pull/236) 继续扩展，加入卖家侧的消息、地址、订单更新与商品规格选择操作。[PR #235](https://github.com/shopstr-eng/shopstr/pull/235) 中的安全修复则将单轮 SHA-256 API key 哈希替换为带盐的 100,000 次 PBKDF2。

Agent 现在可以读取 [NIP-99](/zh/topics/nip-99/)（分类信息）listing，并通过现有的 [NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）与 [NIP-60](/zh/topics/nip-60/)（Cashu 钱包）支付流程完成结账，而无需抓取页面或反向工程客户端行为。

[Milk Market](https://github.com/shopstr-eng/milk-market) 是运行在 [milk.market](https://milk.market) 上的 Nostr 食品市场，它在 [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3) 中引入了同样的 MCP 与 API key 基础。[PR #10](https://github.com/shopstr-eng/milk-market/pull/10) 增加了订阅订单、购买后修改收货地址，以及面向 Stripe 和其他法币支付路径的多商户、多币种结账处理。后续的 [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) 修复了一个启动期数据库初始化 bug：新安装时未创建 failed relay publishes 表，导致首次加载出现 500 错误。这个面向 agent 的接口既可配合 Shopstr 上的 Bitcoin 原生结账使用，也支持 Milk Market 上混合法币与 Bitcoin 的结账流。

### NIP-42 Relay 认证横跨 Bunker、签名器与 Relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker) 是一个 [NIP-46](/zh/topics/nip-46/)（Nostr Connect）bunker，用于把 OAuth 提供方桥接到 Nostr 签名。它加入了 [NIP-07](/zh/topics/nip-07/)（浏览器扩展签名器）登录、单身份自动选择以及对已删除身份的清理（[commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)）。当系统中只存在一个身份时，bunker 现在会直接选中，而不是继续提示用户。删除某个身份时，也会移除其悬空的分配关系和连接。[Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) 还增加了面向已分配用户的 `ALWAYS_ALLOWED_KINDS` 配置路径，默认允许 kind `30078` 的应用特定数据，使代理身份无需逐条批准也能写入应用存储。

[Amber](https://github.com/greenart7c3/Amber) 是 Android 上最主要的 [NIP-55](/zh/topics/nip-55/) 签名器，本周发布 [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4)，期间共有四个预发布版本。[PR #317](https://github.com/greenart7c3/Amber/pull/317) 为 kind `22242` 请求加入了 [NIP-42](/zh/topics/nip-42/) relay 认证处理。实现中新增了一个数据库列，用于跟踪按 relay 区分的权限，并在 `(pkKey, type, kind, relay)` 上建立唯一索引。用户会看到一个专门的认证页面，可以针对单个 relay 或通过通配符 `*` 作用域对所有 relay 授权或拒绝，并将选择持久化。通配符权限会清除该 kind 的所有 relay 级别条目。[PR #318](https://github.com/greenart7c3/Amber/pull/318) 则继续重构多 event 请求界面，用可组合卡片内联显示详情，而不是跳转到单独页面。此次发布还更新了默认资料 relay、增加 bottom sheet 请求展示，并通过禁用 StrongBox keystore 修复了 MediaTek 设备上的崩溃问题。

在 relay 侧，[strfry PR #156](https://github.com/hoytech/strfry/pull/156) 为 [NIP-70](/zh/topics/nip-70/)（Protected Events）实现了 NIP-42 认证处理，而 [PR #176](https://github.com/hoytech/strfry/pull/176) 会拒绝嵌入受保护 event 的 repost。

### Notedeck 增加 NIP-11 Relay 限制与 Agentium 特性

[Notedeck](https://github.com/damus-io/notedeck) 是 Damus 团队开发的原生桌面客户端，本周合并了 14 个 PR。[PR #1316](https://github.com/damus-io/notedeck/pull/1316) 加入 [NIP-11](/zh/topics/nip-11/)（Relay 信息文档）中的 relay 限制抓取，因此所有 outbox relay 现在都会遵守 relay 信息文档中的 `max_message_length` 与 `max_subscriptions`。该实现包含后台 job 处理、带抖动的指数退避连接重试，以及自定义 HTTP Accept 头。[PR #1312](https://github.com/damus-io/notedeck/pull/1312) 修复了一个在切换账户后私信有时无法加载的 bug，而 [PR #1333](https://github.com/damus-io/notedeck/pull/1333) 为 multicast relay 通信增加退避机制，以避免错误时的广播刷屏。

Agentium 子系统（Notedeck 内建的编码 agent UI，内部代号为“Dave”）新增了剪贴板图片粘贴、通过 kind `31991` event 在设备间同步的命名运行配置（[NIP-33](/zh/topics/nip-33/) 参数化可替换 event）、git worktree 创建器，以及允许每个会话选择后端的模型选择器（[PR #1336](https://github.com/damus-io/notedeck/pull/1336)）。[PR #1338](https://github.com/damus-io/notedeck/pull/1338) 集成了 `egui_kittest`，用于无头 UI 测试，而 [PR #1339](https://github.com/damus-io/notedeck/pull/1339) 增加了一张 dashboard 卡片，用于跟踪各客户端中新联系人列表的创建情况。仍处于开放状态的 [PR #1314](https://github.com/damus-io/notedeck/pull/1314) 则把 Amethyst 的 Namecoin NIP-05 解析移植到 Notedeck，支持 ElectrumX 查询、SOCKS5 Tor 路由与搜索栏集成。

### diVine Ships v1.0.6 with E2E Test Infrastructure and NIP-49 Import

[diVine](https://github.com/divinevideo/divine-mobile) 是一个短视频循环客户端，致力于在 [divine.video](https://divine.video) 恢复 Vine 档案。它发布了 [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6)，包含 127 个已合并 PR。该版本增加了 [NIP-49](/zh/topics/nip-49/) 账户导入、外部 [NIP-05](/zh/topics/nip-05/) 支持、多账户处理，以及由本地存储支持的重设计草稿与 clips 库，同时还提供 macOS 与实验性 Linux 构建。

在工程层面，[PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) 增加了一整套 E2E 集成测试基础设施，使用 Patrol 对 Docker 后端栈（relay、API、Blossom、Postgres、Redis、ClickHouse）进行原生 UI 自动化。五个认证旅程测试覆盖注册、验证、密码重置、会话过期与 token 刷新。[PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) 将视频加载策略从优先 HLS 切换为直连 MP4，并在必要时自动回退到 HLS，使加载时间从 30 到 60 秒缩短到几乎瞬时。[PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) 将首页 feed API 响应缓存到 SharedPreferences，以实现冷启动即时展示。[PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) 强制在 feed 中隐藏带 `ai-generated` 标签的内容，而 [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) 增加了一项安全设置，只显示由 diVine 托管的视频。Hive 向 Drift 的资料缓存迁移仍在 [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881)、[PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) 和 [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903) 中持续推进，用 Drift DAO 替换约 1074 行 Hive 代码。

### Vector v0.3.2 发布 NIP-77 Negentropy 同步与 MLS 改进

[Vector](https://github.com/VectorPrivacy/Vector) 是一个注重隐私的桌面消息应用，使用 MLS 群组加密以及 [NIP-17](/zh/topics/nip-17/)（私密私信）和 [NIP-44](/zh/topics/nip-44/)（加密载荷）加密，现已发布 [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2)。头条改动是面向 MLS 群组同步的 NIP-77 negentropy（[commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)），利用并行启动显著加快漏收消息的追赶速度。此次发布还增加了重构后的音频引擎并完整支持 Linux、带模糊预览的图片 spoiler、可点击超链接及富链接预览、供群组管理员使用的 `@everyone` 配合 `@mention` 提醒、emoji shortcode 自动补全、群组静音、在现有回应上点击 react，以及可取消的文件上传。Vector 还会显式过滤 NIP-17 群聊 event（[commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)），在群组加密中只使用 MLS。

## 版本发布

### Route96 v0.5.0 与 v0.5.1

[Route96](https://github.com/v0l/route96) 是一个支持 Blossom 与 [NIP-96](/zh/topics/nip-96/)（HTTP 文件存储）的媒体服务器，已发布 [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) 和 [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1)。v0.5.0 增加了自动 AI 标注、对未标注上传内容的回填、针对被标记文件的审核队列、基于 EXIF 的隐私拒绝策略，以及被封禁哈希的处理。

v0.5.1 增加了感知图像哈希、用于相似图片查找的 locality-sensitive hashing、批量管理端点，以及发布的 [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1)，用于描述服务器的 Blossom 与 NIP-96 API 接口，方便 agent 工具接入。[PR #58](https://github.com/v0l/route96/pull/58) 将后台 worker 迁移到完全异步的 Tokio task，而 [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) 增加了退避逻辑，避免热循环。

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat) 是一个长文阅读与发布应用，可在 [samizdat.press](https://samizdat.press) 使用。它在 [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha) 中发布了首个 Android 构建。应用启动后默认进入精选 Press 页面，展示长篇 Nostr 文章，并通过底部标签在 Press、Feed、Saved 与 Write 视图之间切换。Android 版本加入了通过 Android Keystore 加密与生物识别解锁的原生密钥存储，支持处理 `nostr:` URI 与 `samizdat.press` 深链接，并通过 Android 应用选择器把签名流程交给 Amber、Primal 等签名器，而无需直接导入私钥。下拉刷新、跨屏幕尺寸的安全区域处理，以及原生分享、剪贴板、触感反馈和启动页集成，现在也已经成为 Android 外壳的一部分，而不是简单的 Web 包装层。

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) 为 Amber 与 Primal 流程加入基于 intent 的 [NIP-55](/zh/topics/nip-55/) 签名，而 [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) 则用原生 Capacitor 插件配合 `startActivityForResult` 替换了一种 JavaScript bridge 权宜方案。该应用要求 Android 7.0+（API 24），在这个 alpha 阶段以调试版 APK 形式发布，仍未具备推送通知。当前的发布流程依赖签名器应用，而 `nsec` 登录则覆盖本地阅读和账户访问。

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) 是一个去中心化日历应用，支持 [NIP-59](/zh/topics/nip-59/)（Gift Wrap）私密事件共享，可在 [calendar.formstr.app](https://calendar.formstr.app) 使用。它通过 [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38) 发布了 [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0)。该版本扩展了 [NIP-52](/zh/topics/nip-52/)（日历事件）的循环事件处理能力，超越了 v0.1.0 仅支持单个事件的基础。底层变更还涉及本地事件存储、签名器处理和 Android 通知管线。这是 Formstr 组织在上个月仓库迁移后第二个活跃应用。

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro) 是构建在 Nostr 之上的点对点 Bitcoin 交易所，现已发布 [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)。其中包含了[上周报道](/en/newsletters/2026-03-04-newsletter/)的争议会话恢复修复（[PR #599](https://github.com/MostroP2P/mostro/pull/599)）和自动关闭修复（[PR #606](https://github.com/MostroP2P/mostro/pull/606)）。本次发布新增内容包括：[PR #625](https://github.com/MostroP2P/mostro/pull/625) 为 kind `38384` 的用户评分 event 增加 `days` 字段，[PR #612](https://github.com/MostroP2P/mostro/pull/612) 为这些评分 event 增加过期处理，而 [PR #614](https://github.com/MostroP2P/mostro/pull/614) 则把订单 event 的过期策略改为使用配置值，而不是硬编码的 24 小时窗口。[PR #622](https://github.com/MostroP2P/mostro/pull/622) 还增加了幂等性检查，以防止开发者费用重复支付。

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile) 是 Mostro P2P 交易所的 Flutter 客户端，发布了 [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1)，包含 11 项新功能和 11 项 bug 修复。该版本增加了争议聊天中的加密多媒体渲染（[PR #514](https://github.com/MostroP2P/mobile/pull/514)）、当订单进入终态时自动关闭争议 UI（[PR #503](https://github.com/MostroP2P/mobile/pull/503)）、用于导入 NWC 钱包的二维码扫描（[commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)）、法语翻译以及 FCM 推送通知处理。[PR #496](https://github.com/MostroP2P/mobile/pull/496) 通过将 bip340 依赖固定在 v0.2.0，修复了 Schnorr 签名填充 bug。

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main) 是一个支持 Cashu 的 Telegram 风格消息客户端，发布了 [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release)，重点修复 Linux 桌面问题，包括 AppImage dock 图标、emoji 渲染、上下文菜单卡死以及回复/复制 UI 卡顿。该版本还修复了图片上传问题和 npub.cash 集成。[PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) 移除了一个每 3 秒强制玻璃拟态重绘却没有实际作用的轮询定时器，消除了不必要的 UI 重建；同时通过并发加载 event cache，而不是阻塞 relay、联系人和频道启动，解除登录初始化的阻塞。

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android) 是一个支持 [NIP-55](/zh/topics/nip-55/) 与 [NIP-46](/zh/topics/nip-46/) 的 Android FROST 阈值签名器，已发布 [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) 和 [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1)。v0.6.0 增加了钱包 descriptor 协调与管理 UI、带生物识别认证的备份/恢复流程（[PR #184](https://github.com/privkeyio/keep-android/pull/184)）、从阈值份额恢复 nsec（[PR #187](https://github.com/privkeyio/keep-android/pull/187)）、通过 Rust UniFFI 实现的跨平台动画二维码边框生成（[PR #188](https://github.com/privkeyio/keep-android/pull/188)），以及带链式验证的签名审计轨迹（[PR #189](https://github.com/privkeyio/keep-android/pull/189)）。v0.6.1 则通过 [PR #191](https://github.com/privkeyio/keep-android/pull/191) 将许可证从 AGPL-3.0 改为 MIT。

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump) 是用于浏览 Nostr 内容的静态网关，可在 [njump.me](https://njump.me) 使用。它发布了 [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0)，其中包含 `note1` 代码解析的破坏性变更，以及底层 nostr 库的更新。

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr) 是一个基于 Nostr 的去中心化道路事件上报应用，已发布其初始演示版本 [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1)。该应用使用 openfreemap.org 的矢量瓦片在地图上显示道路事件。

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core) 是一个带有 Nostr 传输层并配套专用 relay（[bit.cr](https://www.bit.cr/)）的电子票据应用，已发布 [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)。[PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) 为 API 增加了 `payment_actions` 与 `bill_state` 字段，用于支付与接受状态，[PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) 则修复了匿名签名器的签名地址处理。

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat) 是一个构建在 Marmot 协议 .NET MLS 与 C# 库之上的聊天应用，已发布 [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3)。该版本增加了对 Amber 与 [NIP-46](/zh/topics/nip-46/) 流程的外部签名器支持（[commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)），把 MLS 状态持久化移动到 MLS 服务内部，以消除崩溃窗口中的数据丢失（[commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)），并通过新的 CI 管线发布 Windows、Linux 与 Android 构建。

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal) 是一个面向 Nostr 的 Kotlin Multiplatform 交易副驾应用，已发布 [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0)。该版本打包了共享 KMP 模块，用于领域逻辑、图表渲染、Nostr 认证与发布、Blossom [NIP-96](/zh/topics/nip-96/) 上传支持，以及跨桌面端和 Android 外壳的基于 ONNX 的 AI 推理钩子。已发布的架构还包括一个用于图表截图分析的 FastAPI AI 服务、模型训练管线，以及输出结构化交易计划、仓位大小与警告的风险引擎。登录既支持原始 `nsec` 密钥，也支持外部签名器，而最终输出流程以发布 Nostr event 结束，而非只在本地展示分析结果。

## 项目更新

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms) 是 Nostr 上的 Google Forms 替代品，它合并了 [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434)（[commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)），增加了使用 [NIP-49](/zh/topics/nip-49/)（私钥加密）加密私钥的注册流程。在这一变更之前，用户要么需要 [NIP-07](/zh/topics/nip-07/) 浏览器扩展，要么必须直接粘贴原始 `nsec` 才能使用 Formstr。新流程会在客户端生成密钥对，通过 NIP-49 的 scrypt + XChaCha20-Poly1305 方案，用用户选择的密码加密私钥，并存储所得的 `ncryptsec` 字符串。之后用户无需安装签名器扩展，只需输入密码即可再次登录。整个密钥管理过程始终留在客户端侧。

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst) 这个功能丰富的 Android 客户端合并了四个 PR，发布了上周仍处于开放状态的、基于 Namecoin 的 [NIP-05](/zh/topics/nip-05/) 解析工作。[PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) 为 `.bit`、`d/` 和 `id/` 标识符增加了通过 ElectrumX 实现的抗审查 NIP-05 验证。当 Amethyst 在 NIP-05 字段中检测到这些后缀时，它会查询 ElectrumX-NMC 服务器获取该名称的交易历史，并从最新输出中解析 `NAME_UPDATE` 脚本以提取 Nostr pubkey，同时拒绝超过 36,000 个区块的过期名称，也就是 Namecoin 的到期窗口。启用 Tor 时，ElectrumX 连接会通过 SOCKS5 路由，并在明网与 `.onion` 端点之间动态选择服务器。一个带一小时 TTL 的 LRU 缓存则避免重复的区块链查询。

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) 修复了该流程中的竞争条件与解析器正确性问题。[PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) 允许新用户在注册时从普通 NIP-05 标识符或 Namecoin 支持的标识符导入关注列表。[PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) 则加入自定义 ElectrumX 服务器设置，让用户自行选择由哪台服务器处理查询。

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb) 是一个为 IndexedDB 中存储 Nostr event 提供辅助方法的库，它合并了 [PR #6](https://github.com/hzrd149/nostr-idb/pull/6)，增加对 [NIP-91](/zh/topics/nip-91/) AND 标签过滤器的支持。该改动把交集语义加入客户端侧过滤匹配逻辑，使 IndexedDB 查询可以要求所有列出的标签值都存在，而不是只匹配其中任意一个。[PR #8](https://github.com/hzrd149/nostr-idb/pull/8) 将该库更新到最新的 NIP-DB 接口，随后 [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) 修复了订阅死锁，并移除了 nostr-tools 的生产依赖。

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve) 是一个以归档优先的 Nostr 索引器，带有 ClickHouse 分析能力。它合并了 [PR #8](https://github.com/andotherstuff/pensieve/pull/8)，增加按条目生效的缓存 TTL 强制执行与按 key 的 miss 合并，以降低 API CPU 峰值。成本最高的时序端点，例如参与度统计、按小时活跃度和按 kind 活跃度，现已使用 10 分钟的服务端 TTL，而不再触发同步的重算风暴。

### Blossom

[Blossom](https://github.com/hzrd149/blossom) 是去中心化媒体托管协议及其服务器栈，本周合并了两个 BUD-11 授权更新。[PR #91](https://github.com/hzrd149/blossom/pull/91) 把可选授权拆分到独立 BUD 中，并澄清 `x` 与 `server` 标签的作用。[PR #93](https://github.com/hzrd149/blossom/pull/93) 清理了按端点区分的授权行为，并正式定义用于上传校验的 `X-SHA-256` 请求头。这两个 PR 将授权逻辑统一到 BUD-11 中，并消除了围绕上传、删除和媒体管理流程中请求哈希的歧义。

## NIP 更新

最近 [NIPs 仓库](https://github.com/nostr-protocol/nips)中的变更：

**已合并：**

- **[NIP-91](/zh/topics/nip-91/)（过滤器 AND 运算符）**（[PR #1365](https://github.com/nostr-protocol/nips/pull/1365)）：为标签过滤器增加交集语义，使 relay 可以回答要求所有列出标签值都匹配的查询，而不是任意一个都算命中。这样可以减少客户端侧后过滤和高标签密度查询中的带宽浪费。

- **[NIP-66](/zh/topics/nip-66/)（Relay 发现与存活监测）：防御措施**（[PR #2240](https://github.com/nostr-protocol/nips/pull/2240)）：继[上周报道](/en/newsletters/2026-03-04-newsletter/)的 outbox 基准测试工作之后，该规范现在补充了关于 relay 监测数据失效路径的警告。客户端不得要求 kind `30166` 监测 event 才能正常工作。监测器可能错误、过期或恶意。规范预期客户端交叉核验来源，避免仅凭单一 feed 就切断用户 relay 图中的大部分路径。

- **[NIP-39](/zh/topics/nip-39/)（资料中的外部身份）：kind 10011 注册清理**（[PR #2256](https://github.com/nostr-protocol/nips/pull/2256)）：把 kind `10011` 直接加入规范，与[上周报道](/en/newsletters/2026-03-04-newsletter/)的 Amethyst 实现保持一致。

**开放 PR 与讨论：**

- **[NIP-70](/zh/topics/nip-70/)（Protected Events）：拒绝嵌入受保护 event 的 repost**（[PR #2251](https://github.com/nostr-protocol/nips/pull/2251)）：如果某个 relay 对原始 event 执行 NIP-70，但接受携带同样内容的 repost，那么 `-` 标签就失去了实际作用。这个 PR 增加了规则，要求 relay 同时拒绝 kind 6 和 kind 16 的受保护 event repost。[strfry PR #176](https://github.com/hoytech/strfry/pull/176) 已经实现了这一点。

- **[NIP-71](/zh/topics/nip-71/)（视频 Event）：多音轨**（[PR #2255](https://github.com/nostr-protocol/nips/pull/2255)）：增加音频 `imeta` 标签，用于替代音轨、语言变体以及纯音频流。客户端可以在保持视频文件稳定的同时切换音频语言，或者把音频作为独立轨道提供给类似播客的内容。

- **[NIP-11](/zh/topics/nip-11/)（Relay 信息文档）与 [NIP-66](/zh/topics/nip-66/) Relay 属性**（[PR #2257](https://github.com/nostr-protocol/nips/pull/2257)）：为 relay 信息文档增加结构化 `attributes` 字段，使客户端和发现工具能获得当前自由文本描述之外的机器可读元数据。

## NIP 深度解析：NIP-49（私钥加密）

[NIP-49](/zh/topics/nip-49/) 定义了客户端如何用密码加密私钥，并将结果编码为 `ncryptsec` bech32 字符串。[Formstr](#formstr) 在其新的注册流程中使用了 NIP-49。

这种格式并不绑定到专门的 event kind。客户端从原始的 32 字节 secp256k1 私钥开始，通过 scrypt 从用户密码派生对称密钥，使用 XChaCha20-Poly1305 加密私钥，然后把结果包装成 bech32 `ncryptsec` 字符串。一个单字节标志会记录该密钥在加密前是否曾被以不安全方式处理过。

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

上面的 JSON event 是应用层示例，并不是 NIP-49 的要求。NIP 标准化的是加密密钥格式本身。客户端可以在本地存储 `ncryptsec`，通过应用特定存储进行同步，或把它导出为备份字符串。密码在派生密钥前会按 Unicode NFKC 规范化，因此相同密码可在不同客户端和平台上得到一致解密结果。

这个单字节密钥安全标志有三个已定义值：`0x00` 表示密钥的处理历史未知，`0x01` 表示已知该密钥曾被不安全地处理过，例如在加密前以明文粘贴到 Web 表单中，`0x02` 表示密钥在安全环境中生成并加密，从未暴露。客户端可以利用它在导入已知存在不安全历史的密钥时给出警告。

与明文 `nsec` 导出相比，NIP-49 对密钥的保护更强，但加密强度最终仍取决于密码质量与配置的 scrypt 成本。更高的 `LOG_N` 值会让离线猜测更困难，但也会拖慢合法解密操作。规范警告不要把加密密钥发布到公共 relay，因为攻击者会从收集密文中获益，用于离线破解。相比之下，[NIP-46](/zh/topics/nip-46/) 远程签名完全避免暴露密钥，[NIP-55](/zh/topics/nip-55/) Android 签名则把密钥保留在专用签名器应用中。NIP-49 填补的是另一个位置：为自主管理密钥的用户提供可移植的加密备份。

相关实现包括：[Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) 的注册流程，[Amber](https://github.com/greenart7c3/Amber) 的 ncryptsec 备份与恢复，[diVine v1.0.6](#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import) 的账户导入，[Keep v0.6.0](#keep-v060) 的 FROST 份额导出，以及 [nsec.app](https://nsec.app) 和 [Alby](https://github.com/getAlby/hub) 等密钥管理工具。

## NIP 深度解析：NIP-70（Protected Events）

[NIP-70](/zh/topics/nip-70/) 定义了受保护 event。当某个 event 带有 `["-"]` 标签时，relay 必须拒绝它，除非该 relay 要求 [NIP-42](/zh/topics/nip-42/) 认证，并且认证过的 pubkey 与 event 作者匹配。

NIP-42 认证流程如下：relay 发送一个包含随机字符串的 `AUTH` challenge，客户端则响应一个已签名的 kind `22242` event，其标签中包含 relay URL 和该 challenge。relay 会验证签名，并检查认证 event 中的 pubkey 是否与正在发布的受保护 event 中的 pubkey 一致。如果 pubkey 不匹配，relay 就会以 `restricted` 前缀拒绝该 event。

event 内容本身仍然可以是公开的。`-` 标签只控制谁可以把该 event 发布到遵守该标签的 relay。这适用于 [NIP-29](/zh/topics/nip-29/)（简单群组）的半封闭 feed、仅成员可见的 relay 空间，以及其他作者希望限制通过 relay 图再传播的场景。NIP-70 只是一个单标签约定，而不是新的 event kind，因此任何现有 event kind 都可以携带 `-` 标签。

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

即便某个 relay 阻止第三方发布原始 event，仍然有人可以把内容封装进 repost 重新发布。[PR #2251](https://github.com/nostr-protocol/nips/pull/2251) 试图解决这一点，要求 relay 也必须拒绝 kind 6 和 kind 16 中包含受保护内容的 repost。[strfry PR #156](https://github.com/hoytech/strfry/pull/156) 为 protected event 增加了 NIP-42 认证处理，[strfry PR #176](https://github.com/hoytech/strfry/pull/176) 则阻止 repost 嵌入受保护内容。

NIP-70 控制的是 relay 行为。接收者仍然可以把内容复制到其他地方，规范也明确如此。`-` 标签给 relay 一个机器可读信号，让其拒绝再发布。相比之下，[NIP-62](/zh/topics/nip-62/)（请求消失）是在事后请求 relay 删除数据，而 NIP-70 则是在入口阶段阻止未授权发布。两者是互补的：作者可以先把 event 标记为受保护，以限制扩散；之后如果希望 relay 移除内容，再发出删除请求。

---

本周就到这里。你正在构建什么，或者有新闻想分享？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 [NIP-17](/zh/topics/nip-17/) 私信联系我们</a>，或直接在 Nostr 上找到我们。
