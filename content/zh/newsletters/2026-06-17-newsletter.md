---
title: "Nostr Compass #27"
date: 2026-06-17
publishDate: 2026-06-17
translationOf: /en/newsletters/2026-06-17-newsletter.md
translationDate: 2026-08-26
draft: false
type: newsletters
---

本周的重点集中在签名器、P2P 交易协议与主力客户端发布。[Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) 汇集 170 多个 PR，新增 [NIP-60](/zh/topics/nip-60/) Cashu 钱包、[NIP-61](/zh/topics/nip-61/) nutzap、[NIP-82](https://github.com/nostr-protocol/nips/blob/master/82.md) 软件应用信息流、[NIP-F4](/zh/topics/nip-f4/) 播客支持、CLINK 链上 zap 校验、KMP 第一与第二阶段 iOS 迁移，以及 Tor 自愈驱动。[Clave v1.0.0（build 102）](https://github.com/DocNR/clave/releases/tag/v1.0.0)已提交 App Store，为 iOS 带来由推送唤醒的后台签名与传入签名校验。[Mostro Core v0.13.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0) 发布 Protocol v2，以 [NIP-44](/zh/topics/nip-44/) gift-wrap 私信取代基于 relay 的订单通信；[Mostro v0.17.5](https://github.com/MostroP2P/mostro/releases/tag/v0.17.5) 则让运营者侧的反滥用保证金成为可选配置。[Signet v1.11.0](https://github.com/Letdown2491/signet/releases/tag/v1.11.0) 修复 [NIP-17](/zh/topics/nip-17/) 管理命令签名绕过。[Chama v3.2.0 至 v3.5.0](https://github.com/jesuspirate/chama) 重绘交易室并加固资金路径。另有 Citrine Negentropy、FIPS Nym mixnet、Morganite 本地 Blossom 缓存、Zeus CLINK noffer、ZapBook Marmot 密钥发布，以及两项深度解析：NIP-77 与 NIP-61。

## 头条新闻

### Amethyst v1.12.0 发布 Cashu 钱包、nutzap、CLINK 驱动与 Tor 自愈

[Amethyst](https://github.com/vitorpamplona/amethyst) 是 Vitor Pamplona 开发的主流 Android Nostr 客户端。[v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) 汇集 Newsletter #25 作为未发布工作报道的 93 个 PR（[NIP-32](/zh/topics/nip-32/) hashtag 标签、NIP-F4 播客界面、音乐曲目、临时签名器、带 NIP-05 过滤的链上 zap）与 Newsletter #26 的后续工作（继续推进 [NIP-F4](/zh/topics/nip-f4/) 与 Tor watchdog 基础），并加入本周的大批新变更。新工作主要覆盖 Cashu/nutzap 界面、CLINK 链上 zap 驱动、Tor 自愈组件与 KMP iOS 迁移。

[NIP-60](/zh/topics/nip-60/) Cashu 钱包支持与 [NIP-61](/zh/topics/nip-61/) nutzap 渲染在 [PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) 落地；[PR #3115](https://github.com/vitorpamplona/amethyst/pull/3115) 增加按 mint 查看余额的界面，[PR #3191](https://github.com/vitorpamplona/amethyst/pull/3191) 与 [PR #3185](https://github.com/vitorpamplona/amethyst/pull/3185) 则把 Lightning 地址、链上 zap、Cashu mint 与 NWC 汇总到个人资料的统一支付卡片。用于校验链上 zap 的 CLINK 驱动由 [PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039)、[PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) 与 [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) 交付。CLINK 是 Common Lightning Interface for Nostr Keys，也就是 [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) 本周发布的 noffer 接口；Amethyst 还在 [PR #3030](https://github.com/vitorpamplona/amethyst/pull/3030) 中增加校验状态机、重新校验驱动与最低链上 zap 金额。[PR #3201](https://github.com/vitorpamplona/amethyst/pull/3201) 按 [NIP-17](/zh/topics/nip-17/) 把面向 p-tag 用户的 kind 1 回复包装成 gift wrap，从而加入私密笔记：撰写器会依目标选择生成公开笔记或密封群组回复。软件应用信息流采用 [NIP-82](https://github.com/nostr-protocol/nips/blob/master/82.md)，播客浏览则继续实现 [NIP-F4](/zh/topics/nip-f4/)。

Tor 可靠性变更组成完整的自愈栈：[PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053) 将 Arti 升至 v2.3.0，并加入 watchdog 与集成测试；[PR #3223](https://github.com/vitorpamplona/amethyst/pull/3223) 在 Tor 就绪前阻止经 Tor 拨号连接 relay；[PR #3224](https://github.com/vitorpamplona/amethyst/pull/3224) 为 Arti 启动设置 60 秒上限，防止恶意网络卡死循环；[PR #3231](https://github.com/vitorpamplona/amethyst/pull/3231) 则在 Tor 显示 Active、但所有 circuit 均已失效时执行自愈。由此，Tor 栈可在网络切换或设备休眠恢复后自行复原，无需人工干预。KMP iOS 迁移第一与第二阶段由 [PR #3047](https://github.com/vitorpamplona/amethyst/pull/3047) 和 [PR #3050](https://github.com/vitorpamplona/amethyst/pull/3050) 交付，为 `quartz` 与 `commons` 模块打通 iOS CI，并为 iOS 版 Amethyst 奠定基础。

### Mostro Core v0.13.0 以 Protocol v2 移除 relay 中间层

[Mostro](https://github.com/MostroP2P/mostro) 是以 Lightning 结算的 P2P Bitcoin 交易所，用 Nostr 承载订单簿与交易通信。定义 wire protocol 的 Rust 库 [mostro-core v0.13.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0) 以 changelog 所称的 Protocol v2 取代经 relay 路由的消息模型：新的 NIP-44 直接传输承载于 kind 14 event。交易动作现在作为按 [NIP-44](/zh/topics/nip-44/) 包装的 kind 14 消息发送，并绑定到参与者创建订单时生成的每笔交易密钥，不再让交易对话经公开可寻址 event 往返。

旧模型会把整个交易对话面暴露给承载这些 event 的每个 relay。直接 kind 14 传输把订单建立、争议流程与结算元数据限制在交易双方和 Mostro daemon 之间，relay 只能看到加密信封。除传输变更外，v0.13.0 还将 v2 身份证明绑定到交易密钥（见[提交记录](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)），关闭新协议中的一类重放风险。daemon 侧的 [Mostro v0.17.5](https://github.com/MostroP2P/mostro/releases/tag/v0.17.5) 让反滥用保证金成为可选、可由运营者配置：某些交易开始前，双方可能需要锁定一小笔保证金，正常完成时退还，拖延、爽约或恶意干扰时没收。保证金由节点运营者启用，并非全网强制，因此 Mostro 仍保持非托管，各运营者可自行权衡市场摩擦与抗滥用能力。

### Signet v1.11.0 修补 NIP-17 管理命令签名绕过

[Signet](https://github.com/Letdown2491/signet) 是远程 bunker 签名器，管理员可经 Nostr 执行 panic、恢复或状态检查，无需接触主机。[v1.11.0](https://github.com/Letdown2491/signet/releases/tag/v1.11.0) 修复该界面中的安全缺陷：其 [NIP-17](/zh/topics/nip-17/) gift-wrap 管理命令路径只检查未签名内层 rumor 声称的作者，却从未校验已签名 seal。由于 [NIP-44](/zh/topics/nip-44/) 会话密钥是对称的，仅持有公开信息（签名器 pubkey、管理员 npub 与管理员 relay）的攻击者就能从外部伪造 gift wrap，并执行 `panic`、`resumeall` 或 `alive` 等任意 kill-switch 命令。修复在 seal 上调用 `verifyEvent`，并把 rumor 作者绑定到 seal 签名，因此未签名伪造会在入口被拒绝。Signet 运营者应尽快升级；规范与已修补代码路径共同提供了清晰的可利用条件与修复边界。

### Chama v3.2.0 至 v3.5.0 重绘交易室并加固资金路径

[Chama](https://github.com/jesuspirate/chama) 是 Nostr 原生 P2P 托管客户端，把 Fedimint ecash 与 2-of-3 Shamir secret sharing 结合，用于无服务器交易结算。Newsletter #26 报道了从 v2.0.0 到 v3.1.0 的发布序列，其间 Chama 成为独立应用并增加每个卖家的店面。本周六个后续版本从 [v3.2.0](https://github.com/jesuspirate/chama/releases/tag/v3.2.0) 延伸至 6 月 15 日的 [v3.5.0](https://github.com/jesuspirate/chama/releases/tag/v3.5.0)，围绕每个角色当前该做什么重绘交易室，并增强资金路径应对局部故障的能力。[v3.2.0](https://github.com/jesuspirate/chama/releases/tag/v3.2.0) 为买家、卖家和仲裁者提供各自颜色编码的操作提示，让每个角色在所有交易状态下都能看到下一步。[v3.3.0](https://github.com/jesuspirate/chama/releases/tag/v3.3.0) 收紧交易引擎的两项共识规则，需要客户端协调升级才能生效。[v3.3.1](https://github.com/jesuspirate/chama/releases/tag/v3.3.1) 按交易者的社区货币本地化价格与支付方式。[v3.4.0](https://github.com/jesuspirate/chama/releases/tag/v3.4.0) 为资金路径加入五项加固，避免短暂故障、竞争或关闭标签页悄然造成 sats 损失。[v3.5.0](https://github.com/jesuspirate/chama/releases/tag/v3.5.0) 再为仲裁者角色增加两项客户端防护，限制这一角色在无提示下改变交易走向。

### Clave 1.0 登陆 App Store，支持推送唤醒的后台签名

[Clave](https://github.com/DocNR/clave) 是 iOS [NIP-46](/zh/topics/nip-46/) 远程签名器，将用户的 Nostr 私钥保存在 iPhone Keychain 中。应用通过端到端加密通道请求签名，从不接收密钥本身。[v1.0.0 build 102](https://github.com/DocNR/clave/releases/tag/v1.0.0) 本周提交 App Store，经过八个月 TestFlight beta 后达到 1.0 里程碑。此前的 [build 100](https://github.com/DocNR/clave/releases/tag/v0.2.0-build100) 修补等待用户输入时的超时路径，[build 101](https://github.com/DocNR/clave/releases/tag/v0.2.0-build101) 则实现 connect metadata。1.0 支持推送唤醒的后台签名：即使 Clave 已关闭，也能解密请求、检查权限、签名并回复，消除了此前要求 iOS 应用位于前台的响应限制。传入签名使用 BIP-340 Schnorr，按 [NIP-01](/zh/topics/nip-01/) 的规范 event 序列化格式（定义每个已签名 Nostr event 如何哈希的基础规范）强制校验，并加入重放时效防护，因此恶意应用无法通过响应通道夹带重新签名的 event。

该版本还交付更新后的 [NIP-44](/zh/topics/nip-44/) 加密层、按 kind 划分的权限模型与三个敏感度等级；修复低信任签名中“每次询问”请求在用户获准批准前就返回错误的边缘情况；并增加多账户配对，让一次应用配对可流经多个身份。Bunker 配对现在通过 Clave 在 [PR #2381](https://github.com/nostr-protocol/nips/pull/2381) 提出的 [NIP-46](/zh/topics/nip-46/) connect metadata 扩展显示真实应用身份。干净断开流程采用 [PR #2373](https://github.com/nostr-protocol/nips/pull/2373) 已合并的 NIP-46 `logout` 方法，让配对应用无需手动取消配对即可结束会话。每应用 Full、Medium、Low 信任级别、按 event kind 覆盖权限、完整签名活动日志与自带 push proxy 补齐了功能面；proxy 栈采用 MIT 许可证，逐客户端互操作矩阵记录在 [`docs/nip46-compatibility.md`](https://github.com/DocNR/clave/blob/main/docs/nip46-compatibility.md)。

## 版本发布

### Amber v6.2.1 增加 NIP-46 logout 并降低签名器耗电

[Amber](https://github.com/greenart7c3/Amber) 是主流 Android Nostr 签名器。[v6.2.1](https://github.com/greenart7c3/Amber/releases/tag/v6.2.1) 降低 relay 重连与 WebSocket ping 引起的耗电，从 subscription 池中移除失效 relay，并在更新 relay 通知时停止唤醒设备。该版本还支持 [NIP-46](/zh/topics/nip-46/) `logout`，使客户端能干净结束远程签名器会话；同一方法本周通过 [PR #2373](https://github.com/nostr-protocol/nips/pull/2373) 合并入规范。它也能解析 event kind 39701（公开 Web 书签），用户可直接在 Amber 中签署书签 event。设置界面改用分组 Material 3 卡片与不同图标，应用权限界面的导航崩溃得到修复；数据库改为原子构建，也关闭了每账户数据库连接泄漏。

### Nostur 1.29.0 发布匿名回复与远程签名器 logout

[Nostur](https://github.com/nostur-com/nostur-ios-public) 是 Fabian 开发的 iOS Nostr 客户端。[1.29.0-desktop](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.29.0-desktop) 支持回复 zap receipt 与发送匿名回复。签名器侧改进远程 bunker 连接流程，在用户退出账户时向远程签名器发送 [NIP-46](/zh/topics/nip-46/) `logout`，并修复远程签名器连接失败后转圈不止。该版本还修复 DM relay 与应用 relay 冲突导致的私信加载问题、进入回复再返回时出现重复帖子的问题，并在通知行显示媒体缩略图。

### Citrine v3.0.0 发布 Negentropy、NIP-42 AUTH 与 onion relay 过滤

[Citrine](https://github.com/greenart7c3/Citrine) 是 Android 本地 relay 聚合器。[v3.0.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0) 是一次主版本升级，增加 [NIP-77](/zh/topics/nip-77/) Negentropy 集合对账同步、聚合器中的外部签名器与 [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH，以及抓取时遵守 [NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) 静音列表。聚合器对每位作者最多从三个 relay 抓取，来源与索引 relay 可配置；关注、静音与元数据缓存可跨重启和网络变化复用；受限网络下会暂停；未启用出站 proxy 时会过滤 onion relay URL。嵌入受保护 event 的转帖会被拒绝，静音列表默认不受按年龄删除影响。

### FIPS v0.4.0-rc1 增加 Nym mixnet 传输与 mDNS 局域网发现

[FIPS](https://github.com/jmcorgan/fips) 是 FIPS mesh 同步协议实现。[v0.4.0-rc1](https://github.com/jmcorgan/fips/releases/tag/v0.4.0-rc1) 与 v0.3.0 wire-compatible，因此混合版本 mesh 可以互操作，无需统一升级。版本增加两种节点发现与连接方式：带单容器演示和 mixnet-relay 示例的 Nym mixnet 出站传输，以及可选的本地链路 mDNS / DNS-SD 发现。新的纯计数 `show_metrics` 查询让 Prometheus scraper 无需增加热路径开销；FMP 与 FSP rekey 也得到加固，在双向丢包下可无中断完成。

### Calendar by Formstr v1.6.1 与 v1.6.2 增加逐 event 通知

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) 是 [NIP-52](/zh/topics/nip-52/) 日历客户端。[v1.6.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.1) 通过 [PR #109](https://github.com/formstr-hq/nostr-calendar/pull/109) 增加逐 event 通知偏好，用户可分别选择是否接收每个日历 event 的提醒。[v1.6.2](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.2) 通过 [PR #185](https://github.com/formstr-hq/nostr-calendar/pull/185) 修复 Amber 登录，使 Amber 6.2.x 的新 [NIP-46](/zh/topics/nip-46/) 握手端到端工作。

### Bitchat v1.5.2 与 v1.5.3 加固 Nostr 与 BLE 传输

[Bitchat](https://github.com/permissionlesstech/bitchat) 是蓝牙与 Nostr mesh 聊天客户端。[v1.5.2](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.2) 通过 [PR #972](https://github.com/permissionlesstech/bitchat/pull/972) 限制 iOS peer 通知速率以防 flood，并通过 [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) 加固 Nostr 校验与 BLE announce 检查，让 relay 侧 Nostr 接收路径在畸形消息到达本地 mesh handler 前就将其拒绝。[v1.5.3](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.3) 是启动崩溃热修复，解决 `NostrRelayManager` 与 `NetworkActivationService` 之间递归 `dispatch_once` 的问题（[PR #1343](https://github.com/permissionlesstech/bitchat/pull/1343)）。

### Keep v1.0.5 将签名器策略移入经审计的 Rust 核心

[Keep](https://github.com/privkeyio/keep-android) 是封装 [keep](https://github.com/privkeyio/keep) Rust 核心的 Android 签名器。[v1.0.5](https://github.com/privkeyio/keep-android/releases/tag/v1.0.5) 固定使用 [keep v0.4.8](https://github.com/privkeyio/keep/releases/tag/v0.4.8)，并通过 [PR #296](https://github.com/privkeyio/keep-android/pull/296) 修复 bunker 初始化竞争，使握手在高负载下不再丢失首个 event；通过 [PR #291](https://github.com/privkeyio/keep-android/pull/291) 从 bunker `onConnect` 回调填充 Authorized Clients 界面；通过 [PR #284](https://github.com/privkeyio/keep-android/pull/284) 将 kill switch 统一到 keep-mobile 的单一事实来源。上游 Rust 核心于 6 月 13 日发布 [v0.4.9](https://github.com/privkeyio/keep/releases/tag/v0.4.9)，把 [NIP-55](/zh/topics/nip-55/) 与 [NIP-46](/zh/topics/nip-46/) 签名策略面移入核心，包括权限决策、敏感 kind 时长上限、过期与密钥事件处理，减少 Android 界面层与审计核心之间的策略分叉。

### ants v0.4.5 增加文章 portal 链接并恢复 Habla

[ants](https://github.com/dergigi/ants) 是 dergigi 的 Nostr 搜索与阅读工具。[v0.4.5](https://github.com/dergigi/ants/releases/tag/v0.4.5) 为长文文章卡片增加操作，包括文章 portal 链接、文章专属 `naddr` 分享、复制 `nevent` 与访问原始 JSON。portal 集合恢复 Habla、替换失效目的地并移除 imwald。该版本还恢复文章脚注渲染并保留文内 anchor 导航；登录恢复时会先等待 relay 连接，再抓取个人资料，确保页眉头像正确显示。

### Morganite v0.0.3 发布带按需 Tor 的 Android 本地 Blossom 缓存

[Morganite](https://github.com/greenart7c3/Morganite) 是 Amber 与 Citrine 作者 greenart7c3 开发的新 Android 本地 Blossom 缓存。它作为 [BUD-08](https://github.com/hzrd149/blossom/blob/master/buds/08.md) 本地镜像运行，超过 1GB 后清理最少使用的 blob。[v0.0.3](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.3) 按需启动 Tor、空闲时停止以节省电量；完成作者查询后断开 Nostr relay，避免后台耗电；并修复未过滤 logcat 流、泄漏 HTTP client 导致的耗电问题，同时在主线程外释放被替换的 `OkHttp` client。该版本还先抓取用户的 inbox relay，再查询 Blossom 服务器列表，使 blob 发现遵循 outbox 模型；本地没有缓存时，`HEAD` 请求也会下载 blob，让缓存预热与真实客户端需求保持一致。

### Coracle 0.6.34 与 0.6.35 修复 NIP-46 登录、陈旧信息流与回复开关

[Coracle](https://github.com/coracle-social/coracle) 是 hodlbod 开发的 Nostr Web 客户端。[0.6.34](https://github.com/coracle-social/coracle/releases/tag/0.6.34) 修复 [NIP-46](/zh/topics/nip-46/) 登录、切换视图后主页时间线不刷新的陈旧状态，以及启用后会过滤掉所有内容的回复开关。该版本还重建信息流与列表视图，修复 toast 安全区域 inset，并改善图片加载。[0.6.35](https://github.com/coracle-social/coracle/releases/tag/0.6.35) 是小型后续修复：关闭回复时不再隐藏转帖，避免回复过滤器错误作用于转帖。

### Zeus v13.1.0-rc1 发布 CLINK noffer 与无队列 NWC

[Zeus](https://github.com/ZeusLN/zeus) 是自托管 Bitcoin 与 Lightning 钱包，其 Nostr 界面用于 wallet-connect 与 noffer 支付。[v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) 与 Primal 合作，在 iOS 上增加无队列 [NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md) Nostr Wallet Connect 支付，使已支付的 NWC invoice 不再滞留后台队列；同时发布 CLINK noffer 支付，Zeus Pay 为每个账户生成 CLINK noffer，发送方仅凭 Nostr key 即可向任意 Zeus 用户付款。Zeus Pay 还可选择关闭 Nostr Zaps，让收款方停用 kind 9735 receipt 路径而无需关闭 NWC。

### Alby Extension v3.14.3 迁移 NIP-07 签名器使用的 noble/scure 密码栈

[Alby Extension](https://github.com/getAlby/lightning-browser-extension) 是浏览器扩展，在 Lightning 功能之外提供 [NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) 签名与 Nostr Wallet Connect。[v3.14.3](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.3) 将 `@noble/curves`、`@noble/hashes`、`@noble/ciphers`、`@noble/secp256k1`、`@scure/bip32` 与 `@scure/base` 迁移到 v2 和 v3 主版本。这些密码库供 [NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) 签名路径用于 event 签名和 [NIP-44](/zh/topics/nip-44/) 加密，因此主版本升级会触及扩展为每个 Nostr Web 客户端签名请求生成的 wire format。

### Mostro Mobile v1.2.8 与 v1.2.9 支持 Protocol v2 并显示保证金策略

[Mostro Mobile](https://github.com/MostroP2P/mobile) 是 Mostro 的移动客户端。[v1.2.8](https://github.com/MostroP2P/mobile/releases/tag/v1.2.8) 交付上文头条所述 [mostro-core v0.13.0 Protocol v2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0) 的客户端支持，并共增加 17 项功能，包括 [PR #608](https://github.com/MostroP2P/mobile/pull/608) 的 maker 反滥用保证金、[PR #610](https://github.com/MostroP2P/mobile/pull/610) 的 bootstrap relay 发现、[PR #602](https://github.com/MostroP2P/mobile/pull/602) 的订单取消通知历史持久化，以及 [PR #605](https://github.com/MostroP2P/mobile/pull/605) 的创建订单法币金额限制。[v1.2.9](https://github.com/MostroP2P/mobile/releases/tag/v1.2.9) 通过 [PR #617](https://github.com/MostroP2P/mobile/pull/617) 显示节点信息 event 中的反滥用保证金策略，让用户在交易前了解该 Mostro 实例的保证金规则。

### ZapBook build 4 至 27 发布多账户、Marmot 密钥发布与圈子重新邀请

[ZapBook](https://github.com/codeswot/ZapBook) 是 codeswot 为 iOS 与 Android 开发的 Nostr 原生社交阅读应用，以 1 至 100 人的阅读圈为核心，成员分享进度并用 sats zap 相互鼓励。从 6 月 11 日的 [build 4](https://github.com/codeswot/ZapBook/releases/tag/v1.0.0-build.4) 到 6 月 15 日的 [build 27](https://github.com/codeswot/ZapBook/releases/tag/v1.0.0-build.27)，项目发布 17 个 tag 并合并 7 个 PR。[PR #25](https://github.com/codeswot/ZapBook/pull/25) 增加可流畅切换的多账户支持，用户能在应用中持有多个 Nostr 身份并迁移会话。初始 [Marmot](/zh/topics/marmot/) key-package（kind 443）现会在完成新用户流程后自动发布（[PR #20](https://github.com/codeswot/ZapBook/pull/20)），这是阅读圈邀请制群聊的前提。被移出圈子的成员现在可以正常处理新邀请并重新加入（[PR #24](https://github.com/codeswot/ZapBook/pull/24)），避免旧成员状态阻塞再次入群。应用还把 ONNX embedding 推理移到后台 isolate（[PR #19](https://github.com/codeswot/ZapBook/pull/19)），用于阅读器内的语义搜索，并用 `APP_ID_SUFFIX` 集成 NWC 服务，以支持按环境区分配置。

### Alby Hub v1.23.0 修复已删除应用的 NIP-47 发布并将 Bitrefill 切换至 NWC

[Alby Hub](https://github.com/getAlby/hub) 是自托管 Lightning 与 Nostr hub。[v1.23.0](https://github.com/getAlby/hub/releases/tag/v1.23.0) 的非 Nostr 功能很多，包括 Just-in-Time channel、借记卡充值 Cards 页面、实验性 Ark 支付后端与 stories 首页，均不在 Compass 范围内。就 [NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md) 而言，该版本通过 [PR #2391](https://github.com/getAlby/hub/pull/2391) 停止为已删除应用重试发布 NIP-47 info，移除连接后不再持续重发 kind 13194 info event；并通过 [PR #2420](https://github.com/getAlby/hub/pull/2420) 移除 Bitrefill 自定义应用入口，改用标准 NWC 连接。[PR #2415](https://github.com/getAlby/hub/pull/2415) 为应用商店应用增加只读选项，收紧 hub 内商店所发布 NWC 应用的权限范围。

### 其他发布

本周还有若干包含 Nostr 相关内容、但单个版本变更较少的发布：[Nostria v3.1.48 至 v3.1.50](https://github.com/nostria-app/nostria/releases) 继续推出 Web Bookmarks，并在 v3.1.50 改善通知可靠性与 event thread 数据库优化；[Deepmarks v0.7.0 至 v0.7.5](https://github.com/ostermayer/deepmarks-public/releases) 持续迭代 [NIP-B0](https://github.com/nostr-protocol/nips/pull/2280) 社交书签客户端，项目网站链接也在本周通过 [PR #96](https://github.com/andotherstuff/nostr-compass/pull/96) 加入 Compass；[Keep v1.1.1 至 v1.1.4](https://github.com/privkeyio/keep-android/releases) 在上文 v1.0.5 签名器版本之上交付四项 F-Droid 可复现构建修复；[NoorNote v0.11.1、v0.12.0、v0.13.0 与 v0.13.1](https://github.com/77elements/noornote/releases) 更新桌面笔记客户端；[Boris v0.12.2](https://github.com/dergigi/boris/releases/tag/v0.12.2) 更新 Boris 阅读器；[Nostr Mail Client v0.13.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.13.0)；[Feeder 2.21.1](https://github.com/spacecowboy/Feeder/releases/tag/2.21.1)；Nostr CLI 的空维护版本 [nak v0.19.13](https://github.com/fiatjaf/nak/releases/tag/v0.19.13)；为 hash-tree 寻址发布器刷新 gateway mutable-root 缓存的 [Hashtree v0.2.68 至 v0.2.71](https://github.com/mmalmi/hashtree/releases)；升级 Nostrify relay 实现的 [NYM v3.72.501 与 v3.72.502](https://github.com/Spl0itable/NYM/releases)；由 iOS Nostr 客户端 85 个合并 PR 支撑的 [swift-nostr-client 0.3.0、0.4.0 与 0.5.0](https://github.com/yysskk/swift-nostr-client/releases)；LaWallet Nostr Wallet Connect bridge 的 [lawallet-nwc v0.11.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v0.11.0)；持续迭代 Astraea Nostr 客户端的 [Astraea v5.35.59 至 v5.35.62](https://github.com/mouse484/astraea/releases)；以及在新 Shops 类别下加入项目目录的 [BTC Recharge 与 giftcardshop NIP-05 已验证 Nostr 私信机器人](https://github.com/andotherstuff/nostr-compass/pull/101)。

## 未发布的变更

### diVine 合并 119 个 PR，推进下一次短视频发布

[diVine](https://github.com/divinevideo/divine-mobile) 是 Nostr 原生短循环视频客户端，以 Nostr 为底层恢复 Vine 档案。项目本周合并 119 个 PR，但未发布新 tag。涉及 Nostr 功能面的主要工作包括：REST-first 视频发布路径，使缺少 relay `OK` 不再显示为失败（[PR #5221](https://github.com/divinevideo/divine-mobile/pull/5221) 与 [PR #5220](https://github.com/divinevideo/divine-mobile/pull/5220)）；广义 blocklist 变化后重新过滤精选与点赞网格（[PR #5208](https://github.com/divinevideo/divine-mobile/pull/5208)）；修复重新安装后 DM 会话列表无法恢复的回归（[PR #5202](https://github.com/divinevideo/divine-mobile/pull/5202)）；恢复个人资料中的 Nostr 徽章显示（[PR #5218](https://github.com/divinevideo/divine-mobile/pull/5218)）；以及让评论引用中的 `nostr:` 引用可点击（[PR #5225](https://github.com/divinevideo/divine-mobile/pull/5225)）。这些变更仍未打包进版本。

### Pollerama 在窗口内合并 15 个 PR，重做签名器并推出一批功能

[Pollerama](https://github.com/formstr-hq/nostr-polls)（仓库 `formstr-hq/nostr-polls`）是 Form* 系列的 Nostr 原生投票与信息流客户端，与本周发布 v1.6.2 的 [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) 同属一系。`nostr-polls` 最新 tag 仍是三月的 [v1.6.4](https://github.com/formstr-hq/nostr-polls/releases/tag/v1.6.4)，因此窗口内工作要等下个 tag 才会发布。6 月 9 日至 16 日间共有 15 个 PR 合并，贡献者包括 abh3po、geralt-debugs 与 SIDDHANTCOOKIE。签名器方面，[PR #198](https://github.com/formstr-hq/nostr-polls/pull/198) 替换原签名界面，[PR #201](https://github.com/formstr-hq/nostr-polls/pull/201) 升级替代实现；[PR #200](https://github.com/formstr-hq/nostr-polls/pull/200) 则阻止登录时触发 kind 0 metadata 更新，使新登录不再无意发布个人资料 event。功能批次还包括可从个人资料视图发帖的资料编辑器（[PR #205](https://github.com/formstr-hq/nostr-polls/pull/205)）、改进的转帖流程（[PR #209](https://github.com/formstr-hq/nostr-polls/pull/209)）与更简单的主题发现路径（[PR #202](https://github.com/formstr-hq/nostr-polls/pull/202)）。这些工作仍待下一个 tag 发布。

### 库与工具工作

[NDK PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) 以及 [rust-nostr](https://github.com/rust-nostr/nostr) 和 [nostr-tools](https://github.com/nbd-wtf/nostr-tools) 仓库的合并工作本周较少，各自只有一两个 PR，且均无 tag 发布。[ContextVM SDK](https://github.com/contextvm/contextvm-sdk)（1 个合并 PR）、[mesh-llm](https://github.com/agentvm/mesh-llm)（37 个合并 PR、8 个开放 PR）、[Zap Cooking](https://github.com/seth-for-real/zap-cooking)（26 个合并 PR）与 [Routstrd](https://github.com/routstrd/routstrd)（2 个合并 PR）继续开发，但窗口内没有发布 tag。

## NIP 更新与协议规范工作

本周协议工作集中在两处：签名器加固与 [NIP-29](/zh/topics/nip-29/) 群组治理。

**本周已合并：**
- **[NIP-46](/zh/topics/nip-46/)（Nostr Connect）。** [PR #2373](https://github.com/nostr-protocol/nips/pull/2373) 增加 `logout` 方法，让客户端能干净结束远程签名器会话。Amber、Clave 与 Nostur 均在同一周发布支持。
- **NIP-CC（Community Chat）。** [PR #2365](https://github.com/nostr-protocol/nips/pull/2365) 更新 NIP-CC，改为引用现代 [NIP-GC（Group Chat）](https://github.com/nostr-protocol/nips/pull/2331)规范提供客户端侧机制，使社区房间规范与规范的群聊原语对齐。

**开放的 NIP-29 集群（基于 relay 的群组治理）：**
- **Banner tag。** [PR #2383](https://github.com/nostr-protocol/nips/pull/2383) 为群组 metadata kind 39000 event 增加 `banner` tag。
- **邀请码后缀。** [PR #2380](https://github.com/nostr-protocol/nips/pull/2380) 在群组标识符上引入邀请码后缀，让一次性邀请可编码进 group ID。
- **消息置顶。** [PR #2379](https://github.com/nostr-protocol/nips/pull/2379) 增加 update-pin-list 审核动作与 kind 39005 event，用于广播置顶集合。
- **经 NIP-17 私信举报群组。** [PR #2377](https://github.com/nostr-protocol/nips/pull/2377) 定义举报流程，成员通过 [NIP-17](/zh/topics/nip-17/) gift-wrap 私信向 relay 管理联系人举报群组滥用，让审核流量离开公开群组 event 流。
- **基于角色的访问控制。** [PR #2376](https://github.com/nostr-protocol/nips/pull/2376) 在现有管理员/成员划分之上增加 RBAC 角色界面。

**开放的 NIP-46 后续工作：**
- **connect 请求中的客户端 metadata。** [PR #2381](https://github.com/nostr-protocol/nips/pull/2381) 允许连接客户端在 connect 请求中发送可选的 `name`、`url` 与 `icon` 字段，使签名器能在配对界面显示应用身份。Clave build 101 已实现该提案。
- **避免静默超时。** [PR #2375](https://github.com/nostr-protocol/nips/pull/2375) 收紧规范：需要用户输入的签名器应保持请求开放，直到用户作出决定，修复 Clave build 100 在实现侧处理的失败模式。

**其他开放工作：**
- **NIP-100 Sovereign Agent Identity Network（SNIN）。** [PR #2378](https://github.com/nostr-protocol/nips/pull/2378) 提案一种用于自主 agent 身份与能力发现的 agent-to-agent 协议。提案范围很广，审查中可能拆成更小部分。

**Blossom 规范。** [BUD-00 PR #108](https://github.com/hzrd149/blossom/pull/108) 于 6 月 15 日合并，扩展 BUD 定义，使其也涵盖建立在 Blossom blob 上、但服务器不实现的客户端约定与数据格式。BUD-10（`blossom:` URI 方案）与 BUD-08（Morganite 本周实现的本地缓存约定）等此前视为规范外扩展的 BUD，因此进入正式编号体系。

## NIP 深度解析：NIP-77（Negentropy）

[NIP-77](/zh/topics/nip-77/) 为 Nostr relay 定义集合对账协议。两方（客户端与 relay，或 bridge 中的两个 relay）各自持有一组匹配 filter 的 event，希望在不重新发送全部数据的情况下收敛到并集。朴素做法是通过网络发送所有 event ID 再求差集；对繁忙 filter 而言，其成本随较大集合的规模增长，与实际差异大小无关。NIP-77 将成本降至与对称差成比例。

规范建立在两种 relay 消息 `NEG-OPEN` 与 `NEG-MSG` 之上。客户端用 `["NEG-OPEN", <subscription_id>, <filter>, <initial_message>]` 开启对账会话，其中 `<initial_message>` 是十六进制编码的 Negentropy 载荷，描述客户端所见集合。回复以 `NEG-MSG` frame 到达，双方持续交换，直至达到固定点。每个 `NEG-MSG` 要么把一个区间拆成带独立 fingerprint 的子区间以缩小分歧，要么列出小区间中的 ID 终止叶节点，使接收方可直接计算差集。当一方确认对方拥有自己缺失的 event 时，会对这些 ID 发送普通 `REQ`；若自己拥有对方缺失的 event，规范则把上传路径留给另一端的普通 `EVENT` 发布。

底层数据结构是有序 Merkle tree 的变体。本地集合中的每个 event 以 `(created_at, id)` 为键并划入区间，每个区间携带由其中 ID 计算的小型 fingerprint。客户端与 relay 的 fingerprint 相同时，该区间已收敛，可以跳过；不同时，回复方把区间分成两半或多个子区间，为每个区间发送 fingerprint，并递归进入差异处。低于较小 event 数量阈值的叶区间会逐项发送。关键性质是，无论已收敛区间中包含多少 event，确认它几乎不产生额外成本。

按 `created_at` 排序有两个作用。第一，Nostr 现有分页也以同一时间戳使用 `until` 与 `since`，因此对账器可跨会话恢复而无需重新同步整个归档：它缓存上界，下次从那里开始。第二，在已排序键上，区间拆分是确定性的，客户端与 relay 总会同意下一条边界，无需另发协商消息。同步成本约为 O(d log n)，其中 d 是对称差规模、n 是较大集合规模，远低于朴素 ID 列表的 O(n) 数据成本，也远低于发出 N 个 REQ 所需的 O(n) 往返。

实现包含三项取舍。fingerprint 大小（规范每区间使用 32 字节）权衡碰撞概率与带宽：更短可节省字节，却提高错误匹配、进而漏掉 event 的概率。叶阈值（何时停止拆分并逐项发送 ID）权衡往返次数与单条消息带宽：阈值越小，轮次越多；阈值越大，叶消息越大。协议还假设双方能在同一区间计算相同 fingerprint，这要求双方采用稳定的 `(created_at, id)` 序列化，因此规范对 fingerprint 构造中的字节序作了严格规定。

relay 在 NIP-11 `supported_nips` 中公告 NIP-77 后，客户端即可用对账取代普通 `REQ` 同步，或将两者并用。客户端按需要选协议：需要尾部实时流量的新 subscription 没有历史状态可对账，适合 `REQ`；停机后追赶的长期 mirror，其对称差远小于归档，适合 `NEG-OPEN`。两条路径服务于不同部署环境，彼此互补。

`NEG-OPEN` 交换示例：

```
→ ["NEG-OPEN", "sync-1", {"kinds":[1],"authors":["abc..."]}, "<hex initial Negentropy message>"]
← ["NEG-MSG", "sync-1", "<hex relay response>"]
→ ["NEG-MSG", "sync-1", "<hex client refinement>"]
← ["NEG-MSG", "sync-1", "<hex leaf with IDs the relay has and client lacks>"]
→ ["REQ", "fetch-1", {"ids":[...]}]
← [...EVENT messages...]
← ["EOSE", "fetch-1"]
→ ["CLOSE", "sync-1"]
```

[Citrine v3.0.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0) 本周在 relay 聚合器中发布 [NIP-77](/zh/topics/nip-77/) 支持，使 Android 本地 relay 界面可以对外部 relay 执行对账，而非批量拉取 `REQ`。

## NIP 深度解析：NIP-61（Nutzaps）

[NIP-61](/zh/topics/nip-61/) 定义以 Nostr event 投递的点对点 Cashu ecash 支付。发送方发布一个锁定到收款方 Nostr 派生公钥的 Cashu token，收款方可在方便时从 mint 兑换。NIP-57 zap 要求收款方在支付发生时可通过 Lightning 访问；nutzap 则是自包含的 ecash token，可由收款方按自己的时间表兑换。

规范把三种 event kind 与 Cashu 的 P2PK 锁定原语组合。Kind 10019 是收款方的 mint 推荐：一种可替换 event，列出收款方接受 nutzap 的一个或多个 mint，以及用于把 proof 锁定给收款方的 Cashu 公钥。该密钥不同于收款方的 Nostr 身份密钥；它是为接收 nutzap 派生的钱包级密钥，因此身份密钥无需接触 ecash secret。发送方付款前读取 kind 10019，确保构造的 token 能在收款方已信任的 mint 兑换。

Kind 9321 是支付 event。它携带一个或多个 Cashu `proof` tag（每个都含 P2PK 锁定 proof，绑定到 kind 10019 中收款方的 nutzap pubkey）、一个含 mint URL 的 `u` tag、可选的 `e` 与 `a` tag 用于标识被 zap 的 note，以及一个指向收款方的 `p` tag。收款方通过常规 Nostr subscription 收到 kind 9321，校验 proof 已锁定到自己的 nutzap pubkey，且 mint 列于自己的 kind 10019；随后用对应私钥解锁 proof，将其保存在 [NIP-60](/zh/topics/nip-60/) 钱包中，或 melt 到 Lightning。Kind 7375 在收款方钱包 event 链中记录已兑换 proof，避免钱包从 relay 重新同步时对同一来源的 nutzap proof 重复计数。

信任模型是这项设计的明确代价。Cashu mint 持有底层价值，恶意或遭查封的 mint 可以拒绝兑换。NIP-61 从 NIP-60 继承该托管风险，并不试图消除它。换来的能力是可离线、即时最终确认的小额支付：token 本身就是付款；收款方无需运行 Lightning 节点，也无需实时接收入站 HTLC；同一 mint 上持有 proof 的发送方无需向托管方发出任何网络请求即可付款。Kind 10019 公告充当社交层门禁：发送方若选择收款方信任集合外的 mint，就可能产生无法兑换的 token，从而让收款方的兑换面保持可预测。

与 NIP-57 相比，校验路径也更简单。NIP-57 zap receipt 是由收款方 LNURL 服务发布的 kind 9735，校验者必须抓取 LNURL endpoint，并确认 receipt 签名密钥与 endpoint 声明一致。nutzap 内联携带支付的密码学 proof，即 P2PK 锁定 proof 本身，因此任何持有 mint 公钥的校验者都能确认 proof 有效，无需往返第三方。代价是 nutzap 校验需要理解 mint keyset，而 NIP-57 校验只依赖标准 LNURL 基础设施。

两种 zap 格式互为补充。具备 Lightning 路由的收款方，以及希望以 sats 计价并采用 Lightning 结算语义的发送方，仍适合 NIP-57 zap。NIP-61 zap 更适合离线收款方、Lightning 费用会淹没转账价值的高频小额支付，以及面向没有 Lightning 基础设施用户的客户端。

nutzap event 示例：

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

[Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) 本周在 NIP-60 钱包界面旁发布 NIP-61 nutzap 渲染（[PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075)），可在时间线显示收到的 nutzap，并在钱包中展示按 mint 划分的余额。
