---
title: "Nostr Compass #30"
date: 2026-07-08
publishDate: 2026-07-08
translationOf: /en/newsletters/2026-07-08-newsletter.md
translationDate: 2026-08-27
draft: false
type: newsletters
description: "Marmot 将规范标记为已采纳，MDK 连发 v0.9.0 至 v0.9.3，带来 MarmotKit 绑定和加密群组头像；Mostro 在 NIP-44 上发布 Transport v2；Bitchat 加入 NIP-13 工作量证明与 mesh-to-Nostr 网关；rust-nostr 则为 gift wrap 和私密私信构建器加入 NIP-40 过期机制。"
---

欢迎回到 [Nostr Compass](https://nostrcompass.org)，您的 Nostr 每周指南。

**本周：** [Marmot 规范被标记为已采纳](#marmot-将规范标记为已采纳mdk-连发-v09x)，42 个文件完成状态更新；MDK 连发 v0.9.0 至 v0.9.3，加入加密群组头像、外部签名器支持及 MarmotKit iOS、Android 绑定。[Mostro 发布 Transport v2](#mostro-v0180-与-mobile-v130-在-nip-44-上发布-transport-v2)，在 mostrod v0.18.0 与 Mobile v1.3.0 中通过带反垃圾门槛和共存窗口的 NIP-44 私信迁移传输协议。[Bitchat 1.6.0 加入 NIP-13 工作量证明](#bitchat-160-加入-nip-13-工作量证明与可选的-mesh-to-nostr-网关)，并带来可选 mesh-to-Nostr 网关、预密钥包、传递式验证和由创建者管理的加密私密群组。[Amber](#amber-v623-按账户限定个人资料订阅并加入-tor-状态通知)按账户限定个人资料订阅，在个人资料元数据前获取 NIP-65 中继列表，并加入可重启的实时 Tor 状态通知。[rust-nostr](#rust-nostr-为-gift-wrap-与私密私信构建器加入-nip-40-过期机制)为 gift wrap 与 NIP-17 私信构建器加入 NIP-40 过期机制，并锚定到 wrap 的随机时间戳。[Amethyst](#amethyst-本周加固-negentropy-同步并加入-nip-50-搜索)合并 43 个 PR，涵盖 negentropy 同步加固、NIP-50 全文搜索基础设施和垂直领域事件类型。[Nostrord 发布 v2.0.0 与 v2.1.0](#nostrord-v200-与-v210-合并中继池并修复僵尸-websocket)，合并中继池、检测僵尸 WebSocket，并建立完整的磁盘优先缓存边界。[Ngit v2.6.2](#ngit-v262-停止在默认分支推送时产生重复-pr-状态事件)、[Jumble v26.7.1](#jumble-v2671-在以私信为重点的版本中将-blossom-设为默认上传服务)、[Applesauce signers 6.2.2](#applesauce-signers-622-移除一个-nbunksec-依赖)、[Bray v1.33.0](#bray-v1330-cli-加入-bunker-profilepersona-与-tor-出站支持)、[Deepmarks 1.0.0](#deepmarks-100-加固-nostr-书签服务)、[Bitcredit Core v0.5.13](#bitcredit-core-v0513-取消-nostr-链路上的区块元数据加密)、[Coop Mobile v0.2.4](#coop-mobile-v023-与-v024)、[Granary v11.0](#granary-v110-加入-nip-71-视频事件支持)、[Nostr-relay v0.0.244](#nostr-relay-v00244-加入-firestore-后端)、[Manent v1.4.0](#manent-v140-修复-nip-42-auth-并加入媒体剪贴板流程)、[Routstrd v0.3.7](#routstrd-v037-将-nostr-事件存储作为持久化事实来源)、[Nymchat 1.0.1](#nymchat-101-作为基于-nip-17-的渐进式-web-应用发布)和 [21Meetup 1.1.0](#21meetup-110-发布由-nostr-签名的出席徽章)也相继发布；[SafeBox 宣布 Phase 3 已大致完成](#safebox-发布-phase-3-进展报告与-freebsd-jail-运行手册)，并附 FreeBSD jail 部署手册及电子可转让记录项目 OpenETR。NIPs 仓库合并了 [NIP-51 与 NIP-37 名称对齐](#已合并nip-51-与-nip-37-对齐-kind-10013-名称)，并开放五项提案：[NIP-AD Nostr Web 地址](#开放通过-well-known-查找的-nip-ad-nostr-web-地址)、[NIP-86 邀请码 claim 管理](#开放面向邀请码的-nip-86-claim-管理)、[HSL 角色颜色格式](#开放以-h-s-l-元组表示角色颜色)、[NIP-80 硬件证明媒体来源](#开放nip-80-硬件证明的媒体来源)，以及 [NIP-01 分页修复](#开放nip-01-分页加固)。深度解析涵盖 [NIP-13（工作量证明）](#nip-深度解析nip-13工作量证明)与 [NIP-40（过期时间戳）](#nip-深度解析nip-40过期时间戳)。

---

## 头条新闻

### Marmot 将规范标记为已采纳，MDK 连发 v0.9.x

[Marmot 协议仓库](https://github.com/marmot-protocol/marmot)于 7 月 3 日合并 [PR #170](https://github.com/marmot-protocol/marmot/pull/170)，将 42 个文件从 `Status: draft for internal review`（以及 `experimental draft`）改为 `Status: adopted`。README 标题不再将仓库描述为进行中的工作，而改为作为已采纳文本的“Marmot Protocol”；MIP 时代文档被重新定义为已弃用的协议版本；“Review Status”（“This is not adopted spec text yet”）变成用于编辑现行规范的“Review Guidance”。全文中的 `v2` 标签也被移除：“new in v2”“the v2 spec keeps”等与 MIP 对照的表述，改为“this spec”和“under this spec”。两个文档按设计仍保留草案状态：`implementation-model.md` 仍属非规范性文档，多设备功能自身的文档也仍是草案。

同一仓库还合并 [PR #171](https://github.com/marmot-protocol/marmot/pull/171)，对齐管理员策略、成员资格与角色变更的不变量。Remove 操作不得导致群组失去管理员这一跨组件检查，如今明确为每个结果 epoch 的属性；当 commit 不含管理员策略更新时，以前一个 epoch 的管理员集合评估。Convergence 的候选分支规则也被收紧：“validates”现在意味着完整的 commit 有效性，包括对结果 epoch 的跨组件检查，避免违反不变量的 commit 在任何分支上形成候选边。若分支选择替换了某个 commit，由该失效 commit 派生的状态通知必须撤回，从规范层面关闭“未胜出的重命名仍显示为成功系统消息”的缺陷。`member-departure.md` 新增“Realizing removal”一节，将移除用户最后一个 leaf 的已接受规范 commit 定义为主要确认输入；对从未应用该移除 commit 的客户端，则以通过认证的逐出后证据产生 `SelfEvicted` 结果，并为被移除的群组副本采用保留但停用的语义。随后 [PR #236](https://github.com/marmot-protocol/marmot/pull/236) 收紧线缆边界校验：KeyPackage 生命周期接受范围固定为 84 天加一小时偏差；增加群组 `h`、gift wrap `p`、welcome `e` 与 `relays` 及 KeyPackage 标签的 Nostr 标签基数表；并明确未经验证的 Nostr event id 与元数据不得作为可信的路由、重放或遥测证据。

下游 [MDK workspace](https://github.com/marmot-protocol/mdk) 于 7 月 6 日发布 [v0.9.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.0)，完成整个 workspace 的版本升级；随后两天又发布 [v0.9.1](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.1)、[v0.9.2](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.2) 与 [v0.9.3](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.3)。v0.9.0 在创建新 SQLite 数据库时轮换过期 keyring 条目，并在存储层全面落实“先校验、后变更”。v0.9.1 通过 [PR #732](https://github.com/marmot-protocol/mdk/pull/732) 将所有出站连接统一导向一个主机安全拨号关口，堵住不同调用点以不同校验方式访问网络的一类漏洞。v0.9.3 通过 [PR #771](https://github.com/marmot-protocol/mdk/pull/771) 以 `download_group_image` 与 `image_hash_hex` 向 uniffi 绑定开放加密群组头像，加入外部签名器支持，并通过 [PR #781](https://github.com/marmot-protocol/mdk/pull/781) 将 `wn-opencode` 标记为可用于生产。每个 MDK 版本还同步发布 MarmotKit iOS 与 Android 绑定：iOS 提供 MarmotKit.xcframework 和 Swift 绑定，Android 提供 Kotlin 绑定与 JNI 库，二者都由固定 MDK commit hash 生成。新的 wn-agent 发布渠道则提供 shell 安装器，将 WN Agent 版本固定到不可变的 release tag，方便下游应用用一条 `curl` 命令取得当前 agent。

### Mostro v0.18.0 与 Mobile v1.3.0 在 NIP-44 上发布 Transport v2

Mostro 是通过 Nostr 事件运行订单簿、托管和争议解决的点对点比特币交易协议，由守护进程 `mostrod` 协调，客户端通过加密私信与之通信。本周前，客户端与 mostrod 之间使用 Transport v1。[Mostro v0.18.0](https://github.com/MostroP2P/mostro/releases/tag/v0.18.0) 发布 Transport v2，将协议迁移到带反垃圾门槛和服务端双接收支持的 [NIP-44](/zh/topics/nip-44/) 私信。[PR #776](https://github.com/MostroP2P/mostro/pull/776) 完成 Phase 1 线缆变更，[PR #780](https://github.com/MostroP2P/mostro/pull/780) 加入 Phase 2 的 v2 反垃圾门槛，[PR #785](https://github.com/MostroP2P/mostro/pull/785) 让内部协议版本跟随当前传输层，使 v2 与 v1 客户端能在迁移窗口共存。相关 [PR #782](https://github.com/MostroP2P/mostro/pull/782) 将 `protocol_versions` 改为单数 `protocol_version`，修复 NIP-33 info 标签。版本还通过 [PR #783](https://github.com/MostroP2P/mostro/pull/783) 加入带缓存和过期检查的 Phase 4 统一实时报价路径，通过 [PR #778](https://github.com/MostroP2P/mostro/pull/778) 加入覆盖古巴 CUP 与 MLC 交易对的 El Toque 法币交叉汇率提供方。[PR #779](https://github.com/MostroP2P/mostro/pull/779) 在争议罚没时通知被罚一方；此前用户只会发现钱包余额消失。

[Mostro Mobile v1.3.0](https://github.com/MostroP2P/mobile/releases/tag/v1.3.0) 是迁移的客户端部分。[PR #613](https://github.com/MostroP2P/mobile/pull/613) 将应用迁移到 Riverpod 3.x；Phase A（[PR #620](https://github.com/MostroP2P/mobile/pull/620)）在主 isolate 与后台 isolate 中加入 NIP-44 私信双接收，使 v2 mostrod 与 v1 客户端可在迁移中通信；[PR #624](https://github.com/MostroP2P/mobile/pull/624) 的 Phase B 加入双发送；[PR #632](https://github.com/MostroP2P/mobile/pull/632) 在 Riverpod 3.x 切换后重新应用双发送；[PR #637](https://github.com/MostroP2P/mobile/pull/637) 的 Phase C 完成迁移。版本还扩大非洲支付方式覆盖：[PR #625](https://github.com/MostroP2P/mobile/pull/625) 加入马拉维克瓦查支付方式，[PR #627](https://github.com/MostroP2P/mobile/pull/627) 加入 KES、MZN、TZS、UGX、ZAR 与 ZMW，并扩展 NGN。恢复流程现在会等待节点连接后再发出请求；按原因处理则能区分争议导致与超时导致的保证金罚没。

### Bitchat 1.6.0 加入 NIP-13 工作量证明与可选的 mesh-to-Nostr 网关

[Bitchat 1.6.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.6.0) 是一款蓝牙 mesh 聊天应用，使用 Nostr 承载 geohash 频道与私信交接。本次版本有两项值得关注的 Nostr 改动。[PR #1382](https://github.com/permissionlesstech/bitchat/pull/1382) 为出站 geohash 频道消息（kind 20000 临时事件）加入 [NIP-13（工作量证明）](/zh/topics/nip-13/)：每次发送都在发布前挖掘 `["nonce", "<value>", "<target>"]` 标签，目标是 8 个前导零位，平均需 256 次哈希尝试，在 M 系列 Mac 上不到一毫秒。通过 PoW 校验的入站事件可放宽每发送者接收速率限制，让垃圾发送者为每条消息付出计算成本，普通发送者则几乎无感。范围有意保持狭窄：只有 kind 20000 频道消息挖掘 PoW；在线心跳（kind 20001）、kind 1 位置笔记与私信均不受影响。

[PR #1384](https://github.com/permissionlesstech/bitchat/pull/1384) 加入 gateway 模式，即 geohash 频道可选的 mesh-to-Nostr 上行链路。纯 mesh 用户（无互联网、无法连接中继）在 geohash 频道发送消息时，如果另一 mesh 节点声明 `.gateway` 能力，已签名 kind 20000 事件会装入新的 `MessageType.nostrCarrier = 0x28` TLV 信封并定向发给一个网关。网关节点代发送者将事件发布到 Nostr，并以默认 TTL 将入站频道流量重新广播到 mesh。上行投递走 courier 信封路径（定向、多跳中继），下行走广播。事件在离开发送者前就已签名，所以网关能决定是否发布，却不能伪造归属。其目标是灾害和抗议场景：人群中只要一部手机联网，整个 geohash 频道就能拥有可用的 Nostr 上行链路。

同一版本还发布第二批与 Nostr 相邻的工作。[PR #1381](https://github.com/permissionlesstech/bitchat/pull/1381) 为 courier mail 路径加入预密钥包，使首次异步联系具备前向保密：发送者无需先与离线节点完成实时 Noise 握手，就能撰写消息并交给 mesh。[PR #1380](https://github.com/permissionlesstech/bitchat/pull/1380) 加入传递式验证：已与你验证过的人完成 Noise 握手的节点，会在 Noise 会话中得到背书，信任图因此逐跳传播，无需对每个新联系人都重新线下验证。[PR #1383](https://github.com/permissionlesstech/bitchat/pull/1383) 加入由创建者管理的 mesh 加密私密群组；[PR #1376](https://github.com/permissionlesstech/bitchat/pull/1376) 可检测、显示并用 `/pay` 命令兑换 Cashu ecash token；[PR #1379](https://github.com/permissionlesstech/bitchat/pull/1379) 在 mesh 同步上加入持久、已签名的 geohash 公告板。[PR #1372](https://github.com/permissionlesstech/bitchat/pull/1372) 扩展存储转发，加入开放 courier、spray-and-wait 路由、持久发件箱与六小时公开历史窗口。本周早些时候发布的 [Bitchat 1.5.4](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.4) 还通过 [PR #1367](https://github.com/permissionlesstech/bitchat/pull/1367) 完整修复收藏功能，清理节点列表重复项、Nostr 同步及 `/fav` 密钥损坏。

---

## 带标签的版本发布

### Amber v6.2.3 按账户限定个人资料订阅并加入 Tor 状态通知

[Amber v6.2.3](https://github.com/greenart7c3/Amber/releases/tag/v6.2.3) 是 Android [NIP-46](/zh/topics/nip-46/) 签名器的性能与正确性版本。它加入可配置的个人资料获取间隔（含永不与始终选项，[PR #492](https://github.com/greenart7c3/Amber/pull/492)），在账户切换底部面板显示头像，并按当前账户限定个人资料订阅，使持有多个账户的签名器不再为当前未使用的账户扩散订阅。Bunker 权限解析也为失败加入明确错误处理。多项 StrictMode 违规得到修复，包括 Coil `onSuccess` 日志造成的 DiskReadViolation、主线程加载账户触发的 keystore 违规、账户切换面板读取名称与头像，以及登录注册页提前构造 `KeyPair()`；这些工作均移出主线程。版本发布后，[PR #493](https://github.com/greenart7c3/Amber/pull/493) 调整启动顺序，先获取用户的 [NIP-65](/zh/topics/nip-65/) 中继列表，再获取个人资料元数据；[PR #494](https://github.com/greenart7c3/Amber/pull/494) 将内置 Tor 通知改为带重启动作的实时状态指示器，让签名期间 Tor 守护进程中断的用户能看到故障并就地重启。[PR #495](https://github.com/greenart7c3/Amber/pull/495) 则在全代码库启用将警告视为错误的严格 Android Lint。

### Jumble v26.7.1 在以私信为重点的版本中将 Blossom 设为默认上传服务

[Jumble v26.7.1](https://github.com/CodyTseng/jumble/releases/tag/v26.7.1) 是聚焦私信与媒体的 Nostr Web 客户端版本。它重新设计媒体上传设置，并将 [Blossom](/zh/topics/blossom/) 设为默认上传服务，取代此前的 NIP-96。私信加入移动端消息菜单、改进的桌面消息动作、“滚动到最新”按钮、对私信媒体的长按回应，以及从消息列表重试失败出站私信的路径。自定义 emoji 编辑新增详情视图；发票与嵌入内容的气泡尺寸得到改善；多个私信滚动、排序问题和编辑器中的 emoji 插入、复制、文件拖放问题得到修复。上传剥离元数据时的图片方向也被纠正，发布矩阵加入 Linux ARM64 下载。

### Applesauce signers 6.2.2 移除一个 nbunksec 依赖

[applesauce-signers@6.2.2](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%406.2.2) 通过 [commit d654349](https://github.com/hzrd149/applesauce/commit/d654349)，以内置 [nbunksec](/zh/topics/nip-46/) helper 取代子包对 `@sandwichfarm/encoded-entities` 的依赖。Applesauce 上周加入的 [NIP-46](/zh/topics/nip-46/) bunker 会话编码不再需要外部编码库，从而减少下游签名器包使用者的供应链暴露面。

### Ngit v2.6.2 停止在默认分支推送时产生重复 PR 状态事件

[Ngit v2.6.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.2) 是 git-over-Nostr CLI 的修复版本。向默认分支执行 `git push` 时，不再为已标记 applied 的 PR 发布重复的 merge/applied 状态事件，因为合并检测现在读取推送前的 Nostr 仓库状态——这是工作流 [NIP-34](/zh/topics/nip-34/) 一侧判断 PR 是否已解决的事实来源。此前依赖 git 内部状态的启发式会产生重复事件。活跃仓库因此不再向受众发出重复 kind 1621 状态事件。

### Bray v1.33.0 CLI 加入 bunker profile、persona 与 Tor 出站支持

[Bray v1.33.0](https://github.com/forgesworn/bray/releases/tag/v1.33.0) 是 Nostr SDK 与 CLI 版本。`bunker --profile <name>` 获得自动稳定连接密钥及中继回退，使已保存 profile 能跨越中继故障；`bunker --persona <name>` 可用派生 nsec-tree 身份签名，让一个签名器从一棵派生树代表多个 pubkey；所有 HTTP 请求也可按配置走 Tor SOCKS 代理。版本加入 [NIP-47](/zh/topics/nip-47/) NWC 钱包子命令、[NIP-29](/zh/topics/nip-29/) 群组管理员写操作、NIP-86 管理动词和 [NIP-65](/zh/topics/nip-65/) outbox helper。发布命令加入 `--jsonl`、`--csv`、`--tsv` 输出，新增通用 NIP-01 过滤查询 `req`、任意事件构造 `event`、签名并广播预构建事件的 `publish-raw`、单次 NIP-46 签名 `bunker sign`，并为每个发布命令加入 `--relay`。安全工作覆盖密钥清零、HTTP bearer auth 与速率限制加固、以及中继 URL 的 SSRF 校验。npm tarball 大小为 533,844 字节，并由两个独立 CI runner 验证构建逐字节一致。

### Deepmarks 1.0.0 加固 Nostr 书签服务

[Deepmarks 1.0.0](https://github.com/ostermayer/deepmarks-public/releases/tag/v1.0.0) 是公开 Nostr 书签服务的安全加固里程碑。每个书签仍是任何客户端可读的已签名 Nostr 事件。API 与归档 worker 可访问内部 Redis、bunker 中继路径及云元数据，因此 SSRF 防护至关重要。本版修复 `isPrivateIp` 的严重 IPv6 字面量绕过：带方括号的 `[::1]`、`[fd00::1]` 及 IPv4 映射 `[::ffff:10.0.0.4]` 都曾被归类为公网地址。防护现在会剥离方括号，并在两端将 IPv4 映射与兼容 IPv6 折叠到嵌入的 v4 后再做私网检查。来自外部中继的 `kind:0` profile 在接收端验证签名，恶意中继不能再为任意受害者 pubkey 伪造 `nip05` 或 `lud16`；书签 URL 在每个渲染出口检查 scheme，直接发布到中继、在 `kind:39701` 的 `d` 标签中携带 `javascript:` 或 `data:` 的书签也不能再进入 `<a href>`。Zap receipt 现在能跨越暂时的 bunker 中断；`/publish` 扩散队列则使用 `BLMOVE` 和受 heartbeat 约束的恢复，在 worker 崩溃时保住已向客户端返回 202 的签名事件。

### Bitcredit Core v0.5.13 取消 Nostr 链路上的区块元数据加密

[Bitcredit Core v0.5.13](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.13) 移除信用票据协议公开 Nostr 事件的一层加密。区块元数据（区块 id、hash、signature）现在在线路上明文传输，只有区块数据本身仍用对应票据密钥加密。新应用可处理旧链，旧应用不能处理新链。版本还加入获取票据链的 bill-service 函数，并改用乐观阈值发布：配置数量（默认一个）的中继接受发布后，其余中继异步接收事件，不再被最慢中继阻塞。

### Coop Mobile v0.2.3 与 v0.2.4

[Coop Mobile](https://git.reya.su/reya/coop-mobile) 于 7 月 4 日发布 [v0.2.3](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.3)，7 月 7 日发布 [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4)，延续 Android [NIP-17](/zh/topics/nip-17/) 私信客户端的稳定节奏。v0.2.3 加入聊天内图片与链接渲染、图片附件、语音转文字输入，以及删除联系人确认框。v0.2.4 修复永久卡住的指示器，改进 Nostr Connect 握手，并加入 `ncryptsec1`（[NIP-49](/zh/topics/nip-49/) 加密私钥格式）导入和重新设计的身份导入页面。

### Granary v11.0 加入 NIP-71 视频事件支持

[Granary v11.0](https://github.com/snarfed/granary/releases/tag/v11.0) 是支撑 Bridgy Fed 跨网络桥接的多协议转换库。Nostr 模块有三项明显变化：[NIP-71](/zh/topics/nip-71/) 视频事件（kinds 21、22、34235、34236）现在可转换为带视频附件的 ActivityStreams 1 note，转换器会提取 `imeta` 图片（缩略图）、视频时长、顶层 `published_at` 标签，以及作为首个视频或音频附件后备 `displayName` 的 `alt` 标签。API 方面，`sign` 改名为 `hash_and_sign`，`verify` 失败时抛出 `ValueError`；`Nostr` 构造器遇到无效中继 URL 时也抛出 `ValueError`；未设置 `privkey` 时，`Nostr.query` 会平稳跳过 [NIP-42](/zh/topics/nip-42/) AUTH challenge。后续修复还避免 Nostr `article` 缺少 `id` 时崩溃。

### Nostr-relay v0.0.244 加入 Firestore 后端

[mattn/nostr-relay v0.0.244](https://github.com/mattn/nostr-relay/releases/tag/v0.0.244) 通过 [PR #12](https://github.com/mattn/nostr-relay/pull/12) 加入 Firestore 后端，为 Go 中继的存储层在现有后端之外提供 Google Cloud Firestore 选项，也让运营者可选择托管式 serverless 数据库。

### Manent v1.4.0 修复 NIP-42 AUTH 并加入媒体剪贴板流程

[Manent v1.4.0](https://github.com/dtonon/manent/releases/tag/v1.4.0) 是构建于 Nostr 之上的加密笔记和文件存储应用，支持 [NIP-44](/zh/topics/nip-44/) 加密、[NIP-46](/zh/topics/nip-46/) 与 [NIP-55](/zh/topics/nip-55/) 签名器、[NIP-65](/zh/topics/nip-65/) outbox 路由及 Blossom 存储。版本修复此前损坏的 [NIP-42](/zh/topics/nip-42/) 中继认证、对 `http://` 主机的 Blossom 上传，并重写压缩流程。媒体方面，可复制或粘贴图片、拖放文件、裁剪旋转图片、播放视频和 GIF，并长按相机图标拍视频。Linux 上可用鼠标中键访问 primary clipboard。笔记加载和滚动也有多项优化。

### Routstrd v0.3.7 将 Nostr 事件存储作为持久化事实来源

[Routstrd v0.3.7](https://github.com/routstr/routstrd/releases/tag/v0.3.7) 是 Routstr 去中心化 AI 推理网络的本地守护进程，通过 Nostr kind 38421 发现提供方、kind 38425 承载 LGTM 评价。版本加入 `routstrd update`，下载 routstrd 与 cocod 新二进制并平滑重启；守护进程启动时及每 21 分钟调用 `refreshNostrEvents()`，让发现和评价无需人工干预即可保持新鲜。内置 `@routstr/sdk` 从 0.3.12 升至 0.3.15，以直接 `DiscoveryAdapter` 取代 ProviderRegistry，清除已消失提供方的模型，并将 Nostr 事件存储作为持久事实来源，移除错误的 210 分钟 TTL。Xcashu 退款也得到加固：错误路径先尝试退款 token，404 以两分钟间隔重试三次，425 Too Early 不再抛出异常。

### Nymchat 1.0.1 作为基于 NIP-17 的渐进式 Web 应用发布

[Nymchat 1.0.1](https://github.com/Spl0itable/NYM)（又称 NYM、Nostr Ynstant Messenger）是一款通过 Nostr 提供临时聊天、并与 Bitchat 桥接的 PWA 和原生 iOS/Android 信使。频道以 kind 20000 临时事件承载 geohash 频道、kind 23333 承载命名频道；私信和群聊使用 [NIP-17](/zh/topics/nip-17/) gift-wrapped 事件（kind 1059），带轮换的临时接收者密钥与自动 compromise 后恢复。用户可无注册生成每会话临时密钥对，也可通过 [NIP-07](/zh/topics/nip-07/) 扩展、[NIP-46](/zh/topics/nip-46/) 远程签名器或 nsec 登录持久身份。可选的本机身份加密通过 WebAuthn PRF 或 PBKDF2 支持密码、PIN、passkey 或生物识别解锁；启用加密时明文密钥不写入磁盘。音视频通话用 NIP-17 gift wrap 传信令、WebRTC 传媒体。消息回应使用 [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md)，自定义 emoji 使用 [NIP-30](/zh/topics/nip-30/)；Web 应用由静态文件和充当中继与媒体隐私代理的 Cloudflare Pages Functions 提供。

### 21Meetup 1.1.0 发布由 Nostr 签名的出席徽章

[21Meetup 1.1.0](https://github.com/louisthecat86/Einundzwanzig-Meetup-App) 是德国 Einundzwanzig 比特币社区的 Flutter 应用，通过 NFC 标签和滚动 QR 码记录聚会出席。每枚徽章都是由组织者用 BIP-340 Schnorr 签名的 Nostr 事件（kind 21000），参与者可积累一组对特定区块高度上特定聚会的签名证明。QR 码每十秒轮换，无法远程铸造；NFC 也只能近距离读取。应用在本地从徽章计算信任分数，并可在点对点交易时以 QR 码出示供验证。它面向比特币社区声誉，而非通用 Nostr 社交，但徽章本身是任何 reader 均可验证的普通 Nostr 事件。

### Nostrord v2.0.0 与 v2.1.0 合并中继池并修复僵尸 WebSocket

[Nostrord v2.0.0](https://github.com/nostrord/nostrord/releases/tag/v2.0.0) 是支持 NIP-29、NIP-42、NIP-44、NIP-46、NIP-57、NIP-65 与 NIP-98 的 KMP/WASM Nostr 客户端重大版本。一天后发布的 [v2.0.1](https://github.com/nostrord/nostrord/releases/tag/v2.0.1) 通过 [PR #166](https://github.com/nostrord/nostrord/pull/166) 修复阻断发布的桌面问题：打包后的 2.0.0（deb、rpm、msi、dmg）启动即报 `NoClassDefFoundError: java/sql/DriverManager`，因为 jpackage jlink 镜像缺少 SQLDelight sqlite 驱动依赖的 `java.sql` 模块。修复将其加入运行时镜像；同一 PR 还让乐观发送经过网络层，确保消息抵达中继（此前路径只静默缓存而不投递），并改善移动 Web 的键盘与滚动。

[v2.1.0](https://github.com/nostrord/nostrord/releases/tag/v2.1.0) 于 7 月 7 日加入“relay pool fold”（[PR #176](https://github.com/nostrord/nostrord/pull/176)），把此前独立的 NIP-29 中继 socket 合入共享池。一个重连调度器覆盖所有中继；[NIP-42](/zh/topics/nip-42/) AUTH 签名受到重试边界约束；发布在需要认证时 fail closed 并重试；`requestPrivateGroupData` 与 `fetchGroupPreviews` 的请求风暴竞争被关闭；kind 10009 用户群组列表按中继批处理；`mux_chat` 实时订阅覆盖所有已加入群组，并在中继静默丢订阅时自愈。界面用内联时钟再到勾号图标替换导致布局位移的“Sending...”行，并将停滞的向后滚动变成明确 Retry 行。同日 [PR #179](https://github.com/nostrord/nostrord/pull/179) 加入 Android 僵尸 WebSocket 检测：移动网络和 Doze 会在没有 close frame 的情况下杀死 TCP，向死 socket 写入仍会在本地缓冲，`isConnected()` 也仍为真。`NostrGroupClient` 现在为每帧记录 `lastInboundAtMs`，加入会取消 frame loop 以触发正常重连与重订阅的 `markDead()`，以及五秒内必须得到任意中继响应的 `probeLiveness()`。同一 PR 还停止插入时把乐观消息写入持久缓存，改为投递确认后写入。[v2.1.1](https://github.com/nostrord/nostrord/releases/tag/v2.1.1) 次日通过 [PR #178](https://github.com/nostrord/nostrord/pull/178) 发布，在 v2.1.0 工作上加入 iOS platform actual、原生测试支持与应用图标。

---

## 未发布变更

### rust-nostr 为 gift wrap 与私密私信构建器加入 NIP-40 过期机制

[rust-nostr 合并 PR #1384](https://github.com/rust-nostr/nostr/pull/1384)，为 `GiftWrapBuilder` 与 `PrivateDirectMessageBuilder` 加入 `expiration` 选项。库从调用者接收 `Duration`：[NIP-40](/zh/topics/nip-40/) 过期标签锚定到 gift wrap 的随机 `created_at`（created_at + duration），与真实发送时间解耦。若允许调用者传绝对时间戳，中继观察者可减去 duration 还原发送时间，因此库内部基于随机 wrap 时间戳构造标签。过期标签放在 gift wrap 事件上，而不是 [NIP-59](/zh/topics/nip-59/) 要求标签为空的 kind 13 seal 上。NIP-17 从 `PrivateDirectMessageBuilder` 向 gift wrap builder 传递同一值。该改动关闭 [issue #1381](https://github.com/rust-nostr/nostr/issues/1381)，并沿用 `extra_tags` 的 builder 模式。rust-nostr 还合并 [PR #1387](https://github.com/rust-nostr/nostr/pull/1387)，将 `nostr-relay-builder` 并入 `nostr-sdk`，扁平化 workspace。

### Amethyst 本周加固 negentropy 同步并加入 NIP-50 搜索

Amethyst [主分支](https://github.com/vitorpamplona/amethyst)围绕三个主题合并 43 个 PR。最大的一组是 geode-to-strfry 边界上的 negentropy 同步：此前 refused-window 故障会把客户端推入窗口分裂风暴，如今可干净退避（[PR #3480](https://github.com/vitorpamplona/amethyst/pull/3480)）；`negentropyKmp` 升至 v1.1.1（[PR #3475](https://github.com/vitorpamplona/amethyst/pull/3475)）；加入百万事件 geode-to-strfry 基准与 strfry 对等镜像（[PR #3478](https://github.com/vitorpamplona/amethyst/pull/3478)）；生产基准进入 CI 矩阵，并有更广泛同步优化。无锁并发集合取代每中继一个 mutex 的模式，UDP socket 线程问题也得到修复。

第二条线是 [NIP-50](/zh/topics/nip-50/) 全文搜索基础设施。新的 `SearchableEvent` 接口让事件直接携带索引元数据（[PR #3452](https://github.com/vitorpamplona/amethyst/pull/3452)）；查询 SQLite FTS 前会移除 NIP-50 搜索扩展，避免本地引擎被服务端扩展语法卡住（[PR #3464](https://github.com/vitorpamplona/amethyst/pull/3464)）；默认搜索中继也得到集中管理（[PR #3446](https://github.com/vitorpamplona/amethyst/pull/3446)）。

第三条线是垂直领域协议集成：Android 客户端支持 Birdstar 鸟类检测事件 kind 2473（[PR #3473](https://github.com/vitorpamplona/amethyst/pull/3473)），PS1 记忆卡存档可作为 kind 38192 签名事件发布（[PR #3482](https://github.com/vitorpamplona/amethyst/pull/3482)）。此外，compose-signature 设置可自动为帖子追加自定义文本；桌面通知以原生 OS toast 和共享 filter 重新设计；Messages 列加入隐私锁；`NostrServer.ingest` 加入每次提交可跳过验证的本地写入路径；OpenTimestamps 校验路径的 `equals`/`hashCode` 契约也得到修复。

### Buzz 加入加密 agent telemetry 事件并批处理 relay hot path

[Buzz](https://github.com/block/buzz)（原名 Sprout）在 7 月 1 日至 7 日合并 123 个 PR。第一条主线是 agent telemetry 新事件类型：[PR #1441](https://github.com/block/buzz/pull/1441) 将 NIP-AM 持久加密 agent turn 指标定义为 kind 44200，以用户自有中继归档的签名事件保存指标。随后加入本地归档、原子 remove-kind 路径，并贯穿 emit 路径传递模型名，让下游 reader 能区分每个 turn 来自哪个模型。

第二条主线是中继性能。post-commit dispatch 延迟执行并避免一次 verify clone；ingest 和 fan-out 的数据库往返被批处理，相比此前 tip，测得 p99 ack 降低 7% 至 16%，p999 尾部降低 29% 至 53%；多 filter 查询以有界并发执行；出站 WebSocket 数据帧批量发送。性能之外，管理员可配置、由中继经 [NIP-11](/zh/topics/nip-11/) 提供的每社区 workspace 图标扩展了 NIP-11 信息文档；agent 所有者可通过 kind 5 事件及桌面、移动界面删除 agent 消息；中继加入 OpenTelemetry tracing；git 仓库名称注册表迁移到 Postgres。

### Divine Video 接入中继签名校验并抽取 NostrConnect

Divine Video 的[移动应用](https://github.com/divinevideo/divine-mobile)在窗口内合并 97 个 PR，Nostr 相关主线是信任边界加固与认证清理。[PR #5774](https://github.com/divinevideo/divine-mobile/pull/5774) 校验入站中继事件签名，关闭一类“信任中继”漏洞；[PR #5828](https://github.com/divinevideo/divine-mobile/pull/5828) 在 kind 3080 注销事件中加密 FCM push token，避免退订时设备 token 明文出现在中继；[PR #5831](https://github.com/divinevideo/divine-mobile/pull/5831) 对 kind 5 删除 REQ 分块，避免删除历史很大的用户撑爆中继 frame。认证方面，[PR #5826](https://github.com/divinevideo/divine-mobile/pull/5826) 为 `nostrconnect://` 流程抽取 `NostrConnectCoordinator`，清理 [NIP-46](/zh/topics/nip-46/) 客户端发起的 bunker 路径。[PR #5709](https://github.com/divinevideo/divine-mobile/pull/5709) 在缺少 `notification_type` 时映射 kind 16 repost，使发送客户端省略提示时仍能正确显示通知。

### Zap Cooking 修复 NIP-46 bunker 登录并加入 NIP-50 食谱搜索

[Zap Cooking 前端](https://github.com/zapcooking/frontend)围绕 Nostr 认证失败恢复合并 18 个 PR。[PR #503](https://github.com/zapcooking/frontend/pull/503) 通过明确 connect 握手、authUrl 处理和错误展示修复 bunker 登录，外部签名器连接失败不再卡死。[PR #495](https://github.com/zapcooking/frontend/pull/495) 为食谱提取端点的图片和文本上传加入 NIP-98 认证，使上传可归属到 pubkey。另一条线通过 nostrarchives 搜索中继后端加入 NIP-50 全文食谱搜索（[PR #483](https://github.com/zapcooking/frontend/pull/483)）。引用笔记内容与媒体、链接预览、标签尺寸、多词搜索和服务端社交预览卡也得到改进。

### swift-nostr-client v0.6.0

[yysskk/swift-nostr-client](https://github.com/yysskk/swift-nostr-client) 发布 [v0.6.0](https://github.com/yysskk/swift-nostr-client/releases/tag/0.6.0)，同期合并 30 个 PR。该 Swift Nostr 库更接近首个稳定 API，为不链接 MDK 或 MarmotKit 工具链的 Swift Nostr 客户端提供选择。

### NAPS 与 Napplet 收紧协议工具链

NAPS 本周主要在 [NAP-OUTBOX](https://github.com/napplet/naps/pull/32) 做了重要清理。核心是更紧的边界：减少由调用者控制的路由与泄漏的中继细节，并采用共享事件结果结构携带中继提示和资源 sidecar，与 [NAP-RESOURCE](https://github.com/napplet/naps/pull/80) 对接。发布规则也更明确，分别规定 outbox、inbox 与 relay fanout，减少歧义并改善互操作性。

Napplet 的软件包则从“实用 SDK”走向更紧密的协议工具链。与现行 NAP 规范对齐的 [NAP-COUNT 查询支持](https://github.com/napplet/web/pull/104)、[OUTBOX 由运行时管理的生命周期](https://github.com/napplet/web/pull/112)和 [RelayEventResult sidecar](https://github.com/napplet/web/pull/108)均已落地，让 shell 中介的读取与订阅更精确。CVM registry、DM error envelope、MEDIA session context、LISTS count 字段、COMMON profile result 与 htree: RESOURCE scheme 也得到收紧。新的 [@napplet/cli](https://github.com/napplet/web/pull/103) 加入配置发现、部署规划、签名、Blossom 上传与 manifest 生成；[host-injectable shim prelude](https://github.com/napplet/web/pull/127) 与 [JSR readiness](https://github.com/napplet/web/pull/145) 则让工具栈更易注入、发布与验证。

### Primal Android 扩展远程签名器方法

[Primal Android](https://github.com/PrimalHQ/primal-android-app) 合并 18 个 PR。[PR #1075](https://github.com/PrimalHQ/primal-android-app/pull/1075) 为应用的远程签名器角色实现 `switch_relays` 与 `logout`，扩展 NIP-46 能力。[PR #1083](https://github.com/PrimalHQ/primal-android-app/pull/1083) 加入由 splash gate 控制的本地迁移框架，[PR #1080](https://github.com/PrimalHQ/primal-android-app/pull/1080) 在 splash view-model 中预取笔记 feed。其余改动主要是 Home、Explore 和个人资料界面优化。

### Wisp 改进多账户、Blossom 与 iOS 交互

[Wisp](https://github.com/barrydeen/wisp) 合并 9 个 PR：新增多账户切换器及添加账户流程的明确取消路径；为 `Blossom.parseServerList` 加入单元测试，收紧 [Blossom](/zh/topics/blossom/) server-list parser；重写 iOS zap 面板并加入 instant-zap 设置；将交易历史改为上滑底部面板；支持含非 ASCII Unicode 字母的 hashtag；保持个人资料笔记 feed 分页并内联显示 gallery 媒体；保留内联 profile 与 hashtag 片段前的空行。

### TAO 与 Wired 将默认工作量证明提高到 21 位

[smolgrrr/TAO](https://github.com/smolgrrr/TAO) 与 [smolgrrr/Wired](https://github.com/smolgrrr/Wired) 在两个仓库合入相同的 13 个 PR。[PR #84](https://github.com/smolgrrr/TAO/pull/84) 将默认帖子 signal 的 PoW 目标提高到 21 个前导零位；[PR #80](https://github.com/smolgrrr/TAO/pull/80) 从新鲜 PoW 活动中呈现 feed root，让客户端按近期 NIP-13 工作量为时间线排序，取代原来的事件年龄排序。另有自定义 emoji picker 恢复和视频首帧预览。这是本周第二个把 NIP-13 作为用户内容一级过滤器的 Nostr 客户端，与 Bitchat 的频道级 PoW 相呼应。

### Keep Android v1.1.5 与 v1.1.6

[privkeyio/keep-android](https://github.com/privkeyio/keep-android) 发布 [v1.1.5](https://github.com/privkeyio/keep-android/releases/tag/v1.1.5) 并合并 13 个 PR，7 月 8 日又发布 [v1.1.6](https://github.com/privkeyio/keep-android/releases/tag/v1.1.6)，将底层 keep core 固定为 v0.5.0。Keep 是移动身份保险库，此前以 CustID 名称见于[第 29 期](/en/newsletters/2026-07-01-newsletter/#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow)。v1.1.5 改善 [NIP-46](/zh/topics/nip-46/) challenge 流程体验。v1.1.6 修复底层 keep-mobile crate 中 `set_active_share` 的 check-then-set（TOCTOU）竞争；在 [NIP-98](/zh/topics/nip-98/) HTTP auth 审批提示中展示授权 URL 与方法；并让 RNG 健康检查 fail closed（返回错误）而非 panic。instrumented test 覆盖 NIP-55 审批流程 kill switch。底层 v0.5.0 CLI 的 threshold-OPRF 解锁、软件 DKG、HD FROST 钱包尚未在 Android 应用中开放，本版只交付安全修复。

### heartwood v0.7.0 发布 relay-to-serial 签名桥

[forgesworn/heartwood v0.7.0](https://github.com/forgesworn/heartwood/releases/tag/v0.7.0) 落地上周仍在开发的 relay-to-serial 签名桥，接通 Bray serial-signer 路径的 HSM 模式数据面。[PR #11](https://github.com/forgesworn/heartwood/pull/11) 是桥本身；[PR #13](https://github.com/forgesworn/heartwood/pull/13) 增加 serial frame 覆盖并修复设备 `read_frame` payload offset；[PR #14](https://github.com/forgesworn/heartwood/pull/14) 将 serial frame codec 抽取为共享 `heartwood-frame` crate。

### SafeBox 发布 Phase 3 进展报告与 FreeBSD jail 运行手册

[SafeBox](https://github.com/trbouma/safebox) 是 Nostr 上的私密可携数据保险库，将 [NIP-47](/zh/topics/nip-47/) Nostr Wallet Connect、nAuth、nembed 以及经中继、QR 与 NFC 传递记录整合为可由运营者部署的服务。7 月 6 日发布的 [2026 年 7 月进展报告](https://github.com/trbouma/safebox/blob/main/docs/PROGRESS-REPORT-2026-07.md)将 Phase 3 标记为大致完成：自 4 月报告后提交 49 次，仓库累计 1,136 次，Phase 3 的四项工程承诺大多完成。下一步是范围受控的 pilot；报告还披露，一家受 NDA 约束的电信提供方正在研究 SafeBox 健康记录试点。

此前 Phase 3 的 Nostr 工作包括：对会变更状态的 NWC 动作排队以避免 proof 竞争；Lightning melt 失败后先保护 proof 再返回；长期 NWC listener 主动刷新，避免超过 idle threshold 后静默停滞；LNURL callback 使用规范 origin 及明确 JSON、CORS 响应。QR 与 NFC 记录交换形成统一流程规范，覆盖接收者展示、发送者展示与跨设备展示模式，并通过 Open Quantum Safe 库改善 KEM 处理和重放保护。窗口内 commit [`6866dae`](https://github.com/trbouma/safebox/commit/6866dae) 加入 [FreeBSD jail 部署与 liboqs 构建手册](https://github.com/trbouma/safebox/blob/main/docs/devops/freebsd-jail-from-scratch.md)及 [FreeBSD appliance 规范](https://github.com/trbouma/safebox/blob/main/docs/devops/SAFEBOX-FREEBSD-APPLIANCE-SPEC.md)，记录 ZFS 快照、jail 隔离、`rc.d` 服务管理、主机级反向代理和 FreeBSD/ARM 回滚流程。

---

## 协议工作与 NIP 更新

### 已合并：NIP-51 与 NIP-37 对齐 kind 10013 名称

[PR #2404](https://github.com/nostr-protocol/nips/pull/2404) 是纯文本一致性修复。[NIP-37](/zh/topics/nip-37/) 将 kind 10013 命名为 `Relay List for Private Content`；[NIP-51](/zh/topics/nip-51/) 的 `Draft relays` 对同一 kind 使用了不同措辞。NIP-51 现在采用 NIP-37 的名称。线缆行为与标签语义均未改变；价值在于 NIP-51 是列表型事件的总规范，NIP-37 是私密内容后续规范，名称不一致会让读者难以发现二者描述同一 kind。

### 开放：通过 .well-known 查找的 NIP-AD Nostr Web 地址

[PR #2406](https://github.com/nostr-protocol/nips/pull/2406) 是已关闭 PR #2393 的继任者，并在 [`AD.md`](https://github.com/nostr-protocol/nips/blob/2f4b09335c54a993d483bc220195e3f4a33df1ec/AD.md) 提供完整草案。NIP-AD 定义可带可选 Nostr 对应项的 Web URL。客户端看到 `https://golf.com/players` 时，请求 `https://golf.com/.well-known/nostr.json?ad=/players`，得到把路径映射到 `{filter, relays}` 的 JSON 对象。filter 是标准 NIP-01 filter，relays 指定应查询的中继；带 `"limit": 1` 时解析为单个事件，否则为列表。普通浏览器仍照常呈现 HTML，使同一规范路径同时服务 Web 与 Nostr 客户端。用例包括 [NIP-29](/zh/topics/nip-29/) 群组名解析、[NIP-5A](/zh/topics/nip-5a/) nsite、托管 feed、原生渲染粘贴的 `njump.me/nevent1...`，以及同时面向 Nostr 内外的博客。复用 `.well-known/nostr.json` 并以路径为对象 key，使 resolver 可实现为静态文件。

### 开放：面向邀请码的 NIP-86 claim 管理

[PR #2408](https://github.com/nostr-protocol/nips/pull/2408) 提议为 [NIP-86](/zh/topics/nip-86/) 加入三种方法：`listclaims`（参数 `[]`，返回 [NIP-43](/zh/topics/nip-43/) 邀请码数组）、`createclaim`（参数 `[claim]`，返回 `true`）和 `deleteclaim`（参数 `[claim]`，返回 `true`）。当前 NIP-86 可管理用户与角色，却没有邀请码接口。社区中继可先创建与角色关联的邀请码、在身份建立前收费、把邀请码交给用户，再由 bot 监听 kind 28935 claim 事件并自动分配角色。三种方法使整个流程都可通过中继管理 RPC 完成。

### 开放：以 (h, s, l) 元组表示角色颜色

[PR #2402](https://github.com/nostr-protocol/nips/pull/2402) 将 [NIP-43](/zh/topics/nip-43/) 的角色颜色从单一 `hue`（0 至 360）改为 `hue`、`saturation`、`lightness` 元组。任何分量都可为空字符串，由客户端提供协调调色板的默认值；规范建议通常只给 `hue`，除非需要银色等具体颜色。同一 PR 也更新 NIP-86：`createrole` 与 `editrole` 现在接收 `[id, label, description, [h, s, l], order]`。动机是仅给 hue 会迫使客户端代运营者选择饱和度与亮度，导致同一角色在不同客户端强度不一。

### 开放：NIP-80 硬件证明的媒体来源

[PR #2409](https://github.com/nostr-protocol/nips/pull/2409) 提出 NIP-80，一种锚定到拍摄硬件的媒体来源事件格式。相机在拍摄时签名照片，并按内容本身将证明发布到中继，因此即使元数据被剥离、媒体被转载或平台删除，仍可验证。提案定义六种新事件：kind 1080 拍摄证明；kind 1081 派生证明，覆盖缩放、裁剪、重压缩、打码，支持 reveal 或零知识模式；kind 1082 撤销；kind 11080 设备公告；kind 31080 设备背书；kind 31081 匿名证明设备集合。它复用 NIP-94 `x` 标签、[NIP-92](/zh/topics/nip-92/) `imeta`、[NIP-65](/zh/topics/nip-65/) 撤销发现、[Blossom](/zh/topics/blossom/) 媒体存储和可选 [NIP-03](https://github.com/nostr-protocol/nips/blob/master/03.md) 时间戳锚定。签名模型结合 BIP-340 设备密钥与硬件 ECDSA 密钥，因为主流 secure element 尚不能生成 BIP-340 签名。规范不试图证明场景真实，只证明这张精确图片大约在该时间来自该设备，且仅以声明、可证明的方式修改；并禁止客户端把结果简化为“真实”徽章。Raspberry Pi Rust 相机原型 [OpenVeilCam](https://github.com/PrarthanaPurohit/OpenVeilCam) 正在适配这些事件类型。

### 开放：NIP-01 分页加固

[PR #2407](https://github.com/nostr-protocol/nips/pull/2407) 为 NIP-01 加入“Pagination & limits”。若中继设置最大 `limit`，其值必须大于数据库中共享同一 `created_at` 的最大事件数，避免一秒内事件填满一页而卡死分页。客户端向后分页时必须反复使用包含边界的 `until = oldest`，并按 `id` 去重；某轮去重后无新事件即完成。若满页的最老与最新事件共享一个 `created_at`，客户端必须以更大 `limit` 重试该秒；若中继钳制 limit 且结果仍局限于一秒，则客户端必须以 `until = oldest - 1` 前进（视未取得事件为丢弃）或中止。普通分页不得设置 `limit`，以中继最大值为准；只有排空卡住的一秒时例外。该修复解决重复时间戳下天真的 `since`/`until` cursor 会漏事件或重复处理的问题。

---

## NIP 深度解析：NIP-13（工作量证明）

[NIP-13](/zh/topics/nip-13/) 为 Nostr 事件定义工作量证明机制。公开中继网络极易产生类似电子邮件的垃圾信息：任何人都能生成密钥对并淹没话题，每个事件没有经济成本。NIP-13 让作者为每个事件施加计算成本；垃圾发送者必须累计承担，普通发送者每条消息只付一次。中继与客户端可要求或优先显示达到难度阈值的事件。

### 机制

作者选择以位表示的难度目标，挖掘事件 id（序列化事件的 sha256 哈希），直到至少有相应数量的前导零位。事件 id 包含 `created_at`、标签与内容，因此挖掘必须改变事件体的某个值来搜索哈希空间。NIP-13 为此定义 `nonce` 标签：

```
["nonce", "<nonce_value>", "<target_bits>"]
```

`nonce_value` 是矿工选择的任意字符串，`target_bits` 是承诺的难度。验证者统计事件 id 的前导零位，并与 `target_bits` 比较。标签中的值只是一项声明，验证者必须实测 id 的前导零数量。

随机 sha256 输出的前导零位数服从几何分布，每多一位，预期工作量翻倍。8 位平均 256 次哈希，20 位约一百万次，28 位约 2.68 亿次。Bitchat 对 geohash 频道采用 8 位目标，在现代硬件上不到一毫秒；TAO 与 Wired 默认 21 位，每帖约两百万次，在笔记本上很快，但对 bot farm 的规模化发送代价高昂。NIP-13 不强制难度，由各中继和客户端自行选择。

### 示例事件

一个最小的、经过 NIP-13 挖掘的 kind 1 笔记如下：

```json
{
  "id": "000000000e9d97a1ab09fc381030b346cdd7a1a8a6f27c9c88f68c8b9d0f6c8a",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1720368000,
  "kind": 1,
  "tags": [
    ["nonce", "72847", "28"]
  ],
  "content": "hello, this cost me 28 bits of PoW",
  "sig": "b1a5c9c74cff59f8a48e5c3b3d8e1c8e7e2c1d4a8e2b9f7d1c3e8b4f6a2c8d1e9f4b3c7a1d8e5b2f9c6a3d7e1b8f4c9a2d6e3b7f1c8a4d9e2b5f8c1a7d4e6b9f3c2"
}
```

`id` 以七个十六进制零开头，即 28 个前导零位，与 nonce 标签中的 `target_bits` 一致。矿工不断改变 `nonce_value` `72847`，直到 id 达标。验证者哈希序列化事件，确认至少 28 个前导零位，再验证签名。NIP-13 不增加新字段，只增加 `nonce` 标签并约束 id 的零位数。

### 使用场景

Bitchat 1.5.4 对 kind 20000 geohash 频道消息采用 8 位 PoW：发布前挖掘标签，通过校验的入站事件可放宽每发送者速率限制。TAO 与 Wired 默认以 21 位作为帖子 signal 阈值，并从新鲜 PoW 活动显示 feed root，把它作为时间线排序信号。[cagliostr](https://github.com/mattn/algia) 在中继层强制 NIP-13，拒绝低于阈值的事件。NoStrudel 提供客户端挖掘设置；Damus 与 Amethyst 显示事件时计算前导零位；Coracle 同时提供挖掘与过滤；NDK 和 nostr-tools 向库使用者提供 PoW helper。

NIP-13 部署的关键性质是 PoW 无法伪造：`target_bits` 只有在 id 真有相应前导零时才是证据，造假必须重做工作。因此 Bitchat 能把入站 PoW 用作速率限制放宽依据，即使垃圾发送者声称高难度，检查仍只是哈希计数而非信任判断。另一方面，PoW 并不把矿工绑定到特定 pubkey 或内容；垃圾发送者仍可选择挖 8 位并消耗算力，但成本真实存在。NIP-13 把垃圾信息问题从“无法度量”变成“可量化”，让客户端自行定价。

---

## NIP 深度解析：NIP-40（过期时间戳）

[NIP-40](/zh/topics/nip-40/) 定义 `expiration` 标签，指示中继与客户端在给定 Unix 时间戳后将事件视为已过期。Nostr 事件原本是永久的：签名事件抵达中继后，只能用 NIP-09 删除事件尝试移除，而且中继仍可能保留原文。NIP-40 让作者发布时声明事件短期有效，并要求中继在到期后停止提供、客户端停止显示。

### 机制

作者向事件加入 `expiration` 标签：

```
["expiration", "<unix_timestamp>"]
```

时间戳为 Unix 秒。中继可以在 ingest 时拒绝已过期事件，可以停止提供到期事件，并应尊重作者声明；客户端应隐藏已过期事件。NIP-40 不要求中继删除事件，也不推翻 NIP-70 protected-event 语义；它是提示和软契约。

标签位于事件本身；对 wrapped 消息则位于外层 wrap。NIP-40 不定义删除语义：事件仍是任何持有者可读的签名事件。它提供的是中继和客户端在截止时间后不再呈现事件的协同期望，适用于临时帖子、定时公告、活动结束后不再提供的实时笔记，以及不应超过指定时限保留的 NIP-17 私信。

### 与 gift wrap 的交互

本周合并的 rust-nostr [PR #1384](https://github.com/rust-nostr/nostr/pull/1384) 展示 NIP-40 与 [NIP-59](/zh/topics/nip-59/) gift wrap 的交互。NIP-59 定义两层信封：由发送者真实密钥签名的 kind 13 “seal”，以及由临时密钥签名的 kind 1059 “gift wrap”。两层 `created_at` 都会随机化到真实发送时间之前最多 48 小时，使中继观察者无法恢复真实时间。NIP-59 要求 seal 标签为空。

因此 expiration 必须放在 gift wrap 而不是 seal 上；若锚定到真实发送时间，也会破坏时间隐私：调用者若传绝对过期时间，中继观察者可减去预期 TTL 得到真实发送时间。rust-nostr 的设计是让调用者传 `Duration`，库内部计算 `expiration = wrap.created_at + duration`。wrap 的 `created_at` 已在库内随机化，过期时间因而继承相同随机性，不泄漏真实发送时间。

### 示例事件

kind 1 笔记上的最小 NIP-40 示例：

```json
{
  "id": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1720368000,
  "kind": 1,
  "tags": [
    ["expiration", "1720454400"]
  ],
  "content": "this note expires in 24 hours",
  "sig": "d2e5b8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1"
}
```

`created_at` 是发布时间的 Unix 时间戳；expiration 标签表示事件应在 86,400 秒（24 小时）后停止提供。遵守 NIP-40 的中继在 `1720454400` 后不再于 REQ 中返回事件，客户端也在该时间后隐藏它。

### 使用场景

rust-nostr 的 `GiftWrapBuilder` 与 `PrivateDirectMessageBuilder` 现在把 expiration 作为一级 `Duration` 参数。NDK 为 kind 1 与私信 builder 提供 expiration helper；nostr-tools 提供读取和强制标签的 `getExpiration`、`isExpired`。strfry、nostr-rs-relay、khatru 等中继在 REQ 处理中遵守 NIP-40；Damus、Amethyst、noStrudel、Coracle、Primal 都从时间线中过滤过期事件。zap.stream 等实时活动客户端对相关 kind 1311 聊天事件使用 NIP-40，让直播结束后聊天不再持续存在。

NIP-40 易于落地的关键，是它按事件选择加入且不要求协调部署。作者今天就能加标签；尊重它的中继获得更干净的工作集；忽略它的中继也不比此前更差；隐藏过期事件的客户端则满足作者意图。本周 rust-nostr 的改动进一步说明，标签放置与标签存在同样重要：在 NIP-59 gift wrap 这样的隐私信封中，标签应位于时间戳已随机化的层，API 则防止调用者不慎把真实时间泄漏回 wrap。

---

本周内容到此结束。如果您正在构建项目，或有新闻想分享，欢迎通过 NIP-17 私信联系我们，或在 Nostr 上找到我们。
