---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** Ridestr 通过 [Cashu](/zh/topics/cashu/) 支付和加密位置共享将去中心化拼车服务引入 Nostr。Pomade 为多重签名签署者引入基于电子邮件的恢复功能。Damus 发布 [negentropy](/zh/topics/negentropy/) 实现可靠的私信同步。Amethyst 桌面应用添加搜索、书签和 zaps 功能。Amber v4.1.1 显示中继信任评分。Marmot 合并 MIP-03 并构建 TypeScript 参考聊天应用。diVine 添加 [NIP-46](/zh/topics/nip-46/) 二维码身份验证和提及功能支持。新的 NIP 提案涉及社区管理、基于序列的同步和加密文件存储。我们还回顾了 Nostr 五年来每个一月的发展历程，追溯该协议从 2021 年少数早期采用者，到 2023 年 Damus 在 App Store 爆发式上架，再到 2025 年成熟客户端生态系统的演变过程。

## 新闻

### Ridestr 将去中心化拼车服务引入 Nostr

[Ridestr](https://github.com/variablefate/ridestr) 正在开发一款完全基于 Nostr 构建的点对点拼车应用，支持使用 Bitcoin 和 [Cashu](/zh/topics/cashu/) 进行司机与乘客之间的直接交易。该协议使用自定义事件类型（30173、3173-3175、30180/30181）来协调行程，同时通过渐进式位置披露和 [NIP-44](/zh/topics/nip-44/) 加密保护隐私。

系统通过精心设计的流程运作：司机通过 kind 30173 事件使用 geohash 编码的位置（约 5 公里精度）广播可用性，乘客通过 kind 3173 发送包含费用估算的行程请求，在行程开始前使用 HTLC 托管代币锁定支付。位置隐私通过渐进式披露得到保护——接送详情仅在司机到达时才显示，目的地在 PIN 验证后才共享。各方之间的所有通信都使用 [NIP-44](/zh/topics/nip-44/) 加密保护隐私。

Ridestr 通过带有 P2PK 签名的 HTLC 托管实现支付安全。当乘客接受司机的报价时，他们用支付哈希锁定 [Cashu](/zh/topics/cashu/) 代币，只有司机在行程完成后才能领取。该协议目前采用单一铸造厂架构，要求乘客和司机使用同一个 [Cashu](/zh/topics/cashu/) 铸造厂。该项目基于 Kotlin 的 Android 实现负责处理证明验证，并通过 NUT-07 状态检查恢复过期的证明。

Ridestr 解决了大多数 Nostr 应用所回避的挑战：实时位置协调、带有争议解决的支付托管，以及物理世界交互的信誉系统。该项目目前处于测试阶段，证明了 Nostr 的事件模型可以支持点对点服务市场，而不仅仅是内容共享。

### Pomade 为多重签名签署者推出 Alpha 版恢复系统

由 hodlbod 开发的 [Pomade](https://github.com/coracle-social/pomade) 基于现有的 [FROSTR](https://github.com/FROSTR-ORG) 生态系统，提供以恢复为核心的门限签名服务。通过 @frostr/bifrost 库使用 [FROST](/zh/topics/frost/)（灵活的轮次优化 Schnorr 门限）签名，Pomade 在门限密码学之上添加了基于电子邮件的恢复流程。系统使用 Shamir 秘密共享对用户的密钥进行分片，将份额分发到多个独立的签署者，并可配置阈值（2-of-3、3-of-5 等）。

该协议完全通过 Nostr 运行，使用单一事件类型（28350）和 [NIP-44](/zh/topics/nip-44/) 加密的有效载荷。签名时，客户端向至少 `threshold` 个签署者请求部分签名，然后将这些签名聚合成有效的 Schnorr 签名。对于加密，签署者通过 ECDH 协作派生共享密钥，而无需任何一方知道完整密钥。

恢复通过两种身份验证方法进行：基于密码的（使用 argon2id 并以签署者的 pubkey 作为盐）或电子邮件 OTP。为防止 OTP 恢复期间的中间人攻击，每个签署者使用客户端提供的前缀生成自己的验证码，要求用户独立向每个签署者进行身份验证。根据 [NIP-13](/zh/topics/nip-13/) 的规定，该协议要求注册事件具有工作量证明（20+ 位）以防止垃圾信息。

信任模型是明确的：如果 `threshold` 个签署者串通，他们可以窃取密钥。电子邮件提供商是完全受信任的，因为他们可以拦截 OTP。用户无法独立恢复完整的密钥；恢复需要 `threshold` 个签署者的配合。该协议专为不熟悉密钥管理的新用户设计，明确建议用户在熟悉后迁移到自我托管。Pomade 警告称，鉴于其未经审计的 alpha 状态，存在"密钥丢失、被盗、拒绝服务或元数据泄露"的潜在风险。

## 版本发布

### Damus 发布 Negentropy 实现可靠的私信同步

[Damus v1.13](https://github.com/damus-io/damus/tree/v1.13) 发布了我们[上周作为开放 PR 预览](/zh/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs)的 negentropy 实现。[PR #3536](https://github.com/damus-io/damus/pull/3536) 向网络层添加了基础 [negentropy](/zh/topics/negentropy/) 支持，支持与支持该协议的中继进行集合协调。配套的 [PR #3547](https://github.com/damus-io/damus/pull/3547) 添加了下拉刷新私信同步功能，当标准 REQ 订阅失败时使用 negentropy 恢复丢失的消息。

该实现采用保守的方式：正常的私信加载保持不变，[negentropy](/zh/topics/negentropy/) 作为用户手动刷新时的恢复机制可用。自动化测试通过生成一条带有旧时间戳的私信来演示修复效果，标准查询会错过这条消息，然后使用 [negentropy](/zh/topics/negentropy/) 同步成功检索它。虽然 [negentropy](/zh/topics/negentropy/) 支持需要兼容的中继，但该实现能够优雅地处理混合中继环境，在可用时使用该协议。

### Amber v4.1.1 - 中继信任评分

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1) 发布了中继信任评分显示功能（[PR #289](https://github.com/greenart7c3/Amber/pull/289)），实现了[上周可信中继声明 NIP 报道](/zh/newsletters/2026-01-21-newsletter/#nip-updates)中讨论的中继评估概念。信任评分现在显示在中继页面和 NostrConnect 连接请求中，帮助用户在授权连接前评估中继的可靠性。该版本还包括重新设计的登录/事件/权限界面以及对 `switch_relays` 方法的支持。性能改进缓存了密钥库操作，解决了旧设备上报告的 20+ 秒加载时间问题。

### nak v0.18.2 - MCP 集成

fiatjaf 的 [nak](https://github.com/fiatjaf/nak)（Nostr Army Knife）[v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2) 通过 `nak mcp` 添加了 [Model Context Protocol](https://nostrify.dev/mcp) 支持，使 AI 代理能够在 Nostr 上搜索用户、发布笔记、提及用户，并使用 outbox 模型读取内容。该版本还引入了[一行安装程序](https://github.com/fiatjaf/nak/blob/master/install.sh)（`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`），可下载预编译的二进制文件，消除了最终用户对 Go 工具链的要求。Bunker 模式现在支持 Unix 套接字和 `switch_relays`。

### Zeus v0.12.2 Beta - NWC 修复

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases) 发布了多项 NWC 修复，解决了[上周 Zeus 报道](/zh/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect)中涉及的问题。

## 项目更新

### Amethyst 桌面 - 第 2A 阶段发布

[Amethyst](https://github.com/vitorpamplona/amethyst) 推出了[桌面应用的第 2A 阶段](https://github.com/vitorpamplona/amethyst/pull/1676)，为桌面体验添加了搜索、书签、Zaps、帖子详情视图和长文内容（阅读）功能。配套的 [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683) 添加了透明的事件广播反馈，用户现在可以看到事件在网络中传播时每个中继的实时状态，更容易诊断连接问题。

### Notedeck 进展：日历应用和用户体验优化

Damus 团队的 [Notedeck](https://github.com/damus-io/notedeck) 桌面客户端合并了自动隐藏工具栏行为（[PR #1268](https://github.com/damus-io/notedeck/pull/1268)），根据滚动速度响应，在移动视图上提供更多屏幕空间。一个[草稿 PR #1271](https://github.com/damus-io/notedeck/pull/1271) 添加了完整的 [NIP-52](/zh/topics/nip-52/) 日历应用，包含月/周/日/议程视图、RSVP 支持和日历事件的 [NIP-22](/zh/topics/nip-22/) 评论功能，目前通过功能标志进行测试。

### Jumble 添加社区模式

[Jumble](https://github.com/CodyTseng/jumble)，这个以中继为中心的 Web 客户端，添加了[社区模式](https://github.com/CodyTseng/jumble/pull/738)和支持[通过环境变量设置中继集预设](https://github.com/CodyTseng/jumble/pull/736)，使部署主题实例（如 [nostr.moe](https://nostr.moe/)）变得更加容易。

### Shopstr 订单仪表板

[Shopstr](https://github.com/shopstr-eng/shopstr) 用专用的[订单仪表板](https://github.com/shopstr-eng/shopstr/pull/219)取代了基于聊天的订单管理。新界面为商家提供了一个集中视图，可以跟踪订单状态、将消息标记为已读和管理履行，而无需滚动浏览聊天记录。此更新弃用了 IndexedDB 缓存，转而使用服务器端订单状态 API，并修改了订单私信的标签方式以实现更好的过滤。

### Formstr 添加网格问题

[Formstr](https://github.com/abh3po/nostr-forms)，这个 Nostr 原生表单应用，添加了[网格问题](https://github.com/abh3po/nostr-forms/pull/419)并[重写了其 SDK](https://github.com/abh3po/nostr-forms/pull/410) 以支持嵌入。针对[非 NIP-07 签署者的修复](https://github.com/abh3po/nostr-forms/pull/418)解决了使用 bunker 或本地签署者尝试以其身份提交表单的用户遇到的问题。

### nostr-tools 升级加密依赖

[nostr-tools](https://github.com/nbd-wtf/nostr-tools)，核心 JavaScript 库，[升级到 @noble/curves v2.0.1](https://github.com/nbd-wtf/nostr-tools/pull/520)，解决了 27 个文件中的破坏性 API 更改，并采用了最新经过审计的 noble 库。fiatjaf 还向 [NIP-46](/zh/topics/nip-46/) 添加了 `switch_relays` 支持，使 bunker 客户端能够动态更改中继连接。

### Zeus 正在开发 NIP-87 铸造厂评价

[Zeus](https://github.com/ZeusLN/zeus) 有一个[关于 NIP-87 铸造厂评价的开放 PR](https://github.com/ZeusLN/zeus/pull/3576)，允许用户发现和评价根据 Nostr 关注列表过滤的 [Cashu](/zh/topics/cashu/) 铸造厂。评价包括星级评分，可以匿名提交或使用用户的 nsec 提交。

### Camelus 发布完整私信支持

[Camelus](https://github.com/camelus-hq/camelus)，一个基于 Flutter 的 Android 客户端，使用 Dart NDK 实现节能的移动性能，本周通过 20 多次提交添加了全面的私信功能。更新包括聊天分类、消息日期、乐观发送界面、自我备忘功能和正确的私信中继处理。

### Marmot 协议更新

我们[上周作为开放 PR 报道](/zh/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library)的 MIP-03 确定性提交解析现已合并。[MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152) 确保所有基于 [MLS](/zh/topics/mls/) 的群聊在同一 epoch 收到多个有效提交时收敛到相同状态。

配套的[规范 PR #28](https://github.com/marmot-protocol/marmot/pull/28) 添加了 init_key 生命周期要求，解决了实现审计中发现的空白：Welcome 消息中的私钥材料必须在处理后安全删除（归零、存储清理），新成员必须在 24 小时内执行自我更新以实现前向保密。

TypeScript SDK（[marmot-ts](https://github.com/marmot-protocol/marmot-ts)）正在构建参考聊天应用。[PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37) 添加了群组创建/列表、带有发布/广播/删除流程的密钥包管理和二维码邀请。hzrd149 的[开放 PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) 实现了带有分页的消息历史持久化。whitenoise-rs 后端本周合并了 15 个 PR，包括多语言支持（[PR #455](https://github.com/marmot-protocol/whitenoise-rs/pull/455)）和 MIP-04 v2 媒体引用（[PR #450](https://github.com/marmot-protocol/whitenoise-rs/pull/450)）。

### diVine 添加 Nostr 集成功能

[diVine](https://github.com/divinevideo/divine-mobile)，短视频应用，持续快速进行 Nostr 集成。

开放PR包括 [NIP-46](/zh/topics/nip-46/) 二维码身份验证（[PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)）和 [NIP-17](/zh/topics/nip-17/) 加密私信（[PR #834](https://github.com/divinevideo/divine-mobile/pull/834)）。本周的活动集中在[提及功能支持](https://github.com/divinevideo/divine-mobile/pull/1098)上，将 `nostr:` URI 和 @提及转换为可点击的个人资料链接，[Classic Viners 头像回退](https://github.com/divinevideo/divine-mobile/pull/1097)使用 Nostr 个人资料，以及视频编辑工具，包括[绘图](https://github.com/divinevideo/divine-mobile/pull/1056)、[滤镜](https://github.com/divinevideo/divine-mobile/pull/1053)和[贴纸](https://github.com/divinevideo/divine-mobile/pull/1050)。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[可信中继声明](https://github.com/nostr-protocol/nips/pull/1534)** - 我们[上周报道](/zh/newsletters/2026-01-21-newsletter/#nip-updates)的中继信任评分标准化提案已合并。规范定义了 kind 30385 事件用于中继信任声明，涵盖可靠性、质量和可访问性的评分。合并前的讨论集中在信任评分应该是"全局的"（为所有用户计算一次）还是"个性化的"（相对于每个观察者的社交图谱）。像 [nostr.band 的 Trust Rank](https://trust.nostr.band/) 和 [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) 这样的 PageRank 风格算法通过将通过假账户传递的任何排名除以机器人农场的规模来抵抗女巫攻击。

**开放 PR 和讨论：**

- **Communikeys** - 一个[全面的社区管理提案](https://nostrhub.io)，使用现有的 npub 作为社区标识符，而不是基于中继的方法。任何 npub 都可以通过发布 kind 10222 事件成为社区；出版物通过 kind 30222 事件指向社区。访问控制使用 [NIP-58](/zh/topics/nip-58/) 徽章，支持委托成员管理和社区密钥的冷存储。

- **[NIP-CF: Changes Feed](https://github.com/nostr-protocol/nips/pull/2196)** - 一个草案，提出基于序列的事件同步作为基于时间戳的 `since` 过滤器的替代方案。问题在于：使用 `since` 时间戳的标准 Nostr 同步可能会错过事件，原因包括多个事件共享相同的秒级精度时间戳、客户端和中继时钟漂移，或检查点不精确。NIP-CF 通过让中继为存储的事件分配单调递增的序列号来解决这个问题，提供严格的全序。客户端请求自特定序列号以来的变更，并按保证的顺序接收事件，具有永不错过事件的精确检查点。该提案还支持实时/连续模式，订阅在初始同步后保持打开以进行实时更新。

- **[NIP-XX: 加密文件同步](https://github.com/nostr-protocol/nips/pull/1947)** - 一个协议，定义了 kind 30800（加密文件）、30801（保险库索引）和 30802（共享文档），用于使用 Nostr 中继跨设备同步加密内容。该协议使本地优先的笔记应用能够提供端到端加密同步，而无需中心化服务器。文件内容、路径、名称和文件夹结构都使用 [NIP-44](/zh/topics/nip-44/) 自加密进行加密，因此中继存储的是它们无法读取的数据块。图像等二进制附件使用 [Blossom](/zh/topics/blossom/) 服务器进行客户端加密。Kind 30802 通过加密到接收者的公钥来实现用户之间的文档共享。

## Nostr 五年来的一月

[上个月的通讯](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)追溯了 Nostr 十二月的里程碑，从 fiatjaf 的第一个客户端发布到 Jack Dorsey 的催化性捐赠。本回顾记录了 2021 年到 2025 年每年一月发生的事情，聚焦于经过验证的技术发展。

### 2021 年 1 月：早期开发

Nostr 的第三个月继续在 Branle 上进行开发，这是 fiatjaf 于 2020 年 12 月推出的 Vue.js 客户端。一小群早期采用者（可能少于 15 人）通过 Telegram 群组 [@nostr_protocol](https://t.me/nostr_protocol)（创建于 2020 年 11 月 16 日）进行协调，在一两个实验性中继上测试协议。命令行客户端 noscl 提供了终端交互方式。

技术基础已经锁定：用户通过 secp256k1 公钥识别，帖子使用 Schnorr 签名进行加密签名，中继作为不相互通信的简单存储。这是刻意采用的 Bitcoin 原生密码学，这一设计选择将在多年后影响采用模式。

### 2022 年 1 月：开发者发现

2022 年 1 月开始时，Nostr 仍在 [Hacker News 首次亮相](https://news.ycombinator.com/item?id=29749061)（2021 年 12 月 31 日）的热度中，该帖子获得了 110 分和 138 条评论。在该帖子发布时，只有大约七个中继为整个网络提供动力，评论者指出"垃圾信息还不是问题，因为 nostr 还很新，没人使用它。"Robert C. Martin（"Uncle Bob"）称赞 Nostr 可能是"社交通信的终极解决方案。"讨论持续到一月，开发者们辩论中继架构与真正 P2P 的对比、抗审查与内容审核的平衡，以及简洁性能否扩展。

HN 帖子引发了一波新的实现。Uncle Bob 本人于 1 月 18 日开始开发 [more-speech](https://github.com/unclebob/more-speech)，一个 Clojure 桌面客户端。fiatjaf 的 [go-nostr](https://github.com/nbd-wtf/go-nostr) 库（创建于 2021 年 1 月）和 [noscl](https://github.com/fiatjaf/noscl) 命令行客户端提供了 Go 工具，而 [nostr-tools](https://github.com/nbd-wtf/nostr-tools) 提供了 JavaScript 支持。到 2022 年 12 月，大约有 800 个个人资料有简介。Branle 仍然是主要的 Web 客户端，收到了包括私钥导入和多中继支持在内的更新。技术挑战显而易见：64 个字符的十六进制密钥不够直观，消息延迟令用户沮丧，社区质疑该架构能否处理 Twitter 级别的流量。

### 2023 年 1 月：爆发

2023 年 1 月将 Nostr 从实验变成了运动。Damus，William Casarin（jb55）开发的 iOS 客户端，经历了与苹果 App Store 审批流程的斗争。1 月 1 日被拒，1 月 26 日再次被拒，最终于 [1 月 31 日获批](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store)。该批准引发了连锁反应：Damus 立即登上美国社交网络排行榜第 10 名。Jack Dorsey [称其为](https://web.archive.org/web/20240304043638/https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store)"开放协议的里程碑。"

八天前的 1 月 23 日，[Edward Snowden 宣布](https://x.com/Snowden/status/1617623779626352640)他加入了 Nostr："Nostr 的酷炫之处之一……除了抗审查，就是你不受 280 字符的限制。"作为 NSA 揭发者的背书在注重隐私的圈子里颇具分量，用户们立即开始通过 Lightning 向他发送 zaps。

Web 客户端竞相接纳涌入的用户。[Snort](https://github.com/v0l/snort)，由 kieran 于 2022 年 12 月创建，作为功能丰富的 React 客户端崭露头角；1 月 13 日，Snort 通过 Nostr Plebs API 集成了 NIP-05 注册，让新用户在注册时可以申请人类可读的身份。[Iris](https://iris.to)，由 Martti Malmi（早期 Bitcoin 贡献者，收到了 Satoshi 发送的第二笔 Bitcoin 交易）全职开发，提供 Web 和移动界面，并在 iris.to 提供免费 NIP-05 身份。[Astral](https://github.com/monlovesmango/astral)，由 monlovesmango 使用 Quasar（Vue.js）作为 Branle 的分支构建，专注于中继管理，其中继分组功能让用户可以将中继组织成集合用于发布和过滤。iOS 客户端的 TestFlight 测试版在几小时内就满额了，Amethyst 主导了 Android 市场。

基础设施努力跟上步伐。所有中继都由自掏腰包的爱好者运营。使用 Lightning 微支付的付费中继创建了自然的垃圾过滤，但引入了访问摩擦。[Damus 在获批仅两天后就从中国 App Store 下架](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/)，据报道是应中国最高互联网监管机构的要求。

### 2024 年 1 月：协议加固

2024 年 1 月专注于协议标准化和社区建设。[Nostr PHX](https://www.nostrphx.com/events) 于 1 月 5 日在凤凰城举行了当年首次聚会，汇集了当地的密码朋克。这是那年许多社区活动中的第一个，包括 BTC Prague（6 月）、里加的 Nostriga（8 月）和 Nostrasia。

最重要的协议发展是 [NIP-59（Gift Wrap）](https://github.com/nostr-protocol/nips/pull/716)于 1 月 29 日合并，为加密通信提供元数据保护。Gift Wrap 基于 [NIP-44 的加密标准](https://github.com/paulmillr/nip44)（已于 2023 年 12 月[由 Cure53 审计](https://cure53.de/audit-report_nip44-implementations.pdf)），向中继隐藏发送者身份。该协议将加密消息包裹在由随机一次性使用密钥对签名的外部事件中。中继只能看到一次性公钥，而真正发送者的身份隐藏在只有接收者才能解密的加密有效载荷中。这可以防止中继运营者和网络观察者了解谁在与谁通信。时间戳也可以随机化以防止时序分析。

生态系统扩展到社交媒体之外。[Plebeian Market](https://plebeian.market) 完全符合 [NIP-15](/zh/topics/nip-15/) 原生 Nostr 标准，实现跨店购物车和店铺浏览器以发现商家。[Shopstr](https://github.com/shopstr-eng/shopstr) 作为无需许可的市场出现，促进 Bitcoin 商务。[Zap.stream](https://zap.stream/)，由 kieran 构建，将直播带到 Nostr，支持每分钟 21 sats 的 Lightning 支付。开发工具随着 [NDK](https://github.com/nostr-dev-kit/ndk) 提供 TypeScript 抽象和 [rust-nostr](https://github.com/rust-nostr/nostr) 提供 Rust 绑定而成熟。[Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/) 发布了 Nostr 联系人导入和持久 LND，为后续版本的 Nostr Wallet Connect 集成奠定了基础。

然而基础设施的可持续性[仍然具有挑战性](https://arxiv.org/abs/2402.05709)。这一时期的学术研究发现，95% 的中继难以覆盖运营成本，20% 经历了显著的停机时间。付费中继的入场费平均不到 1,000 sats（约 0.45 美元），不足以维持运营。

*关于骗局的说明：在此期间推出的"Nostr Assets Protocol"和相关的"$NOSTR"代币[被 fiatjaf 公开谴责](https://www.aicoin.com/en/article/377704)为"100% 欺诈"和"亲和力骗局"，与实际的 Nostr 协议没有任何关系。*

### 2025 年 1 月：客户端成熟

2025 年 1 月见证了整个生态系统持续的客户端开发。[Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/) 于 1 月 13 日发布，支持阅读状态的跨设备同步、[FROST](/zh/topics/frost/) 多重签名登录支持和优化的本地数据库性能。Amethyst 继续向 outbox 模型过渡，根据关注列表自动编译中继集，而不需要手动配置。

主要客户端开始放弃使用 [NIP-04](/zh/topics/nip-04/) 进行私信，转向 [NIP-17](/zh/topics/nip-17/) 和提议的 [NIP-104](/zh/topics/nip-104/)，以增强加密和元数据保护。Gossip 模型（outbox/inbox 通信）随着生态系统趋向更高效的中继使用模式而获得采用。行业观察者预测这将是 Nostr 从小众协议过渡到主流认可的一年，可能会有一次引人注目的平台迁移使日活动量翻倍。

### 2026 年 1 月：安全和签名基础设施

2026 年 1 月在安全和签名基础设施方面取得了重大进展。[Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) 发布了 [NIP-46](/zh/topics/nip-46/) 远程签名和 [NIP-55](/zh/topics/nip-55/) 本地签名器支持，与 Amber 和 Aegis 一起成为其他 Android 应用的完整签名中心。[Bitchat 完成了 Cure53 安全审计](https://github.com/permissionlesstech/bitchat/pulls)，这家公司也审计过 Signal 和 NIP-44，17 个以上的 PR 修复了关键发现，包括 DH 密钥清除和线程安全问题。Bitchat 和 Damus 都从 C Tor 迁移到 Rust Arti，以提高可靠性和内存安全性。

协议工作继续进行，[NIP-71](https://github.com/nostr-protocol/nips/pull/1669)（可寻址视频事件）合并，后量子密码学 NIP 开始讨论如何使 Nostr 免受量子攻击。可信中继声明草案提议通过签名声明标准化中继信任评分。[Marmot Protocol](https://github.com/marmot-protocol/mdk) 通过 18 个合并的 PR 加固了其基于 [MLS](/zh/topics/mls/) 的加密消息，解决了审计发现的问题。

现实世界的应用扩展了，[Ridestr](https://github.com/variablefate/ridestr) 使用 [Cashu](/zh/topics/cashu/) 托管和 [NIP-44](/zh/topics/nip-44/) 加密开发去中心化拼车服务，[Pomade](https://github.com/coracle-social/pomade) 向 [FROST](/zh/topics/frost/) 门限签名添加基于电子邮件的恢复流程。Damus 发布了 [negentropy](/zh/topics/negentropy/) 以实现可靠的私信同步，而 Amethyst 的桌面应用达到了第 2A 阶段，支持搜索、书签和 zaps。

### 展望未来

六年的一月揭示了 Nostr 从早期开发（2021 年）到公众发现（2022 年）到爆发式增长（2023 年）到协议加固（2024 年）到客户端成熟（2025 年）到安全基础设施（2026 年）的演变。对于任何观察过开放协议成长的人来说，这种模式都很熟悉：多年的安静建设，条件对齐时突然爆发，然后是让一切变得可靠的更长期工作。从七个中继和一个 Hacker News 帖子开始，现在是经过审计的基础设施，拥有真实的应用。2027 年的问题是：当有人叫车、发送加密消息或使用 Nostr 恢复丢失的密钥时，他们会知道自己在使用它吗？

---

本周就到这里。正在构建什么？有新闻要分享？希望我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 私信联系我们</a>或在 Nostr 上找到我们。
