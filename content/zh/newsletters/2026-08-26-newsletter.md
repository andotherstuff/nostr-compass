---
title: "Nostr Compass #37"
date: 2026-08-26
publishDate: 2026-08-26
translationOf: /en/newsletters/2026-08-26-newsletter.md
translationDate: 2026-08-26
draft: false
type: newsletters
description: "Shopstr 与 Routstr 加固已存储的敏感凭据与来自中继的服务发现，Postr 与 Infans 发布，pakstr 让 Zapstore 发布过程显式化，《Nostr 六年八月史》则追踪评论线程如何从沉寂的协议核心走到落地的客户端。"
---

欢迎回到 [Nostr Compass](https://nostrcompass.org)，您的 Nostr 每周指南。

**本周：** [Shopstr](https://github.com/shopstr-eng/shopstr) 把远程签名器与钱包的敏感凭据挪出浏览器存储，[Routstr SDK](https://github.com/Routstr/routstr-sdk) 校验来自中继的服务提供方发现结果，[Postr](https://gitworkshop.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/relay.ngit.dev/postr) 作为一个小巧的 Android 撰写应用发布，[Infans](https://github.com/TurkeyNostr/infans) 加密育儿记录与共同抚养者之间的同步，[walls.rip](https://walls.rip/comms) 通过公开 Nostr 中继承载 PGP 加密聊天，[pakstr](https://git.nostrdev.com/stuff/pakstr) 让 Zapstore 发布过程显式化。[nostr-tools](https://github.com/nbd-wtf/nostr-tools) 把 gift wrap 的 rumor 绑定到其 seal 上。版本发布涵盖 subscription 隔离、个人资料状态与按中继限定的退出标记。协议工作推进到评论线程的实际落地、wallet connect 的费用上限与支付查询草案、napplet 显示请求，以及同一账户的实验性加入流程。本期以[Nostr 六年八月史](#nostr-六年八月史)收尾。

## 头条新闻

### Postr 作为一个小巧的 Android 撰写应用发布

[Postr](https://gitworkshop.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/relay.ngit.dev/postr) 是一个刻意做得很小的 Android 撰写应用，面向 kind 1 笔记。私钥保管仍留在 [Amber](https://github.com/greenart7c3/Amber)，即 Android 上的 [NIP-55](/zh/topics/nip-55/)（本地签名器）与 NIP-46 签名器。版本 1.0.0 提供可在断网与进程被杀后存活的持久发件箱、按账户隔离的私密草稿，以及带校验哈希与受限上传授权的 [Blossom](/zh/topics/blossom/) 附件。

一次发布只有在 Postr 读回完全相同的已签名事件并校验其签名之后才算成功。重试保持同一个 event id。发布使用作者 [NIP-65](/zh/topics/nip-65/)（中继列表）中的写入中继，加上加密的引导中继，或者按账户自定义的列表。一条已签名的 [NIP-34](/zh/topics/nip-34/)（git over Nostr）[仓库公告](https://njump.me/nevent1qqsqxdwxa8k5e0ftf6j6q5ucs3u94ezgjqmyzwznqt99pyxxw23c74spz3mhxue69uhhyetvv9ujumn8d96zuer9wcx4nr0m)与配套的 [kind 0 项目资料](https://njump.me/nevent1qqs24gy97frkjkma8ys3rwc3jj8f0qrrmsxjwe39jxrhuemztrygr8qpz3mhxue69uhhyetvv9ujumn8d96zuer9wcspcsat)发布在 `relay.ngit.dev`。信息流、分析、广告与密钥存储都留在应用之外。

### Infans 在 Nostr 上加密育儿记录与共同抚养者之间的同步

共同抚养者可以把喂养、睡眠与生长记录留在自己手机上，并在不经过育儿数据服务商的情况下共享。[Infans](https://github.com/TurkeyNostr/infans) 是一个 Android 育儿记录应用，把本地 Room 数据库当作唯一依据，并为备份与伴侣同步发布加密的 kind 30078 [NIP-78](/zh/topics/nip-78/)（应用特定数据）事件。其仓库把本地加密标注为 [NIP-44](/zh/topics/nip-44/)（载荷加密），但实现使用 AES-256-GCM，而 NIP-44 v2 要求 ChaCha20 搭配 HMAC-SHA256，因此本地模式的载荷不应被表述为兼容 NIP-44。

[伴侣同步](https://github.com/TurkeyNostr/infans/blob/main/README.md)使用 d-tag `baby-tracker-sync`，自备份使用 `baby-tracker-backup`。异步留言在伴侣载荷内部传递。文档所述的 Amber [NIP-55](/zh/topics/nip-55/)（本地签名器）路径把签名与加密委托给签名器，但仓库没有提供任何互操作测试来证明每条备份与伴侣同步路径都产出 NIP-44 v2 密文。仓库既未提出医疗器械声明，也未给出第三方安全审计。

### walls.rip 的 Ghost Chat 把 PGP 加密聊天带到公开 Nostr 中继

[walls.rip](https://walls.rip/comms) 是一套匿名通信工具，其 Ghost Chat 模式在浏览器中创建或导入 OpenPGP 身份。它的[开源客户端](https://github.com/KYC-rip/walls-rip/tree/cf40bda32df5f106007631b21afc3cd193ac0cda/src/components/ghostChat)用收件人的 PGP 公钥加密每条消息。可读的会话留在设备的本地会话存储中；应用没有聊天账户，也没有集中的消息数据库。

传输层是真正的 Nostr，但刻意只服务这一个应用。Ghost Chat [把 armored 密文作为 kind 1 事件发布](https://github.com/KYC-rip/walls-rip/blob/cf40bda32df5f106007631b21afc3cd193ac0cda/src/utils/nostrService.ts)到五个默认中继，并给每个事件打上由收件人 PGP 指纹派生的稳定房间 tag。这既给开发者一个把中继当作抗审查消息传输通道的具体范例，也说明了为什么仅靠去中心化投递并不能保护元数据，也无法与 NIP-17 私信互通。

### pakstr 0.13.0 至 0.15.0 让 Zapstore 发布过程显式化

在七月的 [0.3.1 打包与 Amber 相关工作](/en/newsletters/2026-07-29-newsletter/#pakstr-031)之后，[pakstr](https://git.nostrdev.com/stuff/pakstr) 是一个把一整个 web 资源目录变成已签名 Android APK、并用 Nostr 密钥发布到 Zapstore 的命令行工具。[0.13.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.0) 增加了自动的发布版本号。随后的 0.13.1 至 0.13.3 修复 Blossom 发布：[授权改用 base64url](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.1)、[上传带上 Content-Digest](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.2)，以及[在 Blossom 上传之前先发布 Zapstore 应用事件](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.3)。

[0.14.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.14.0) 在发布继续之前校验 Zapstore 发布者。[0.15.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.15.0) 把上架元数据写入 kind 32267 应用事件，并把发布说明放进 kind 30063 发布事件的 content，这样打包应用的 Zapstore 记录就能带上名称、摘要与说明，而不需要另做一次手工上架。

### Heterodyne 规范可迁移身份与加密社交通信

[Heterodyne](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5) 是一个以规范为先的协议族，面向可迁移身份、经过认证的通信、自有设备控制与社交互动。它的[当前 README](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5) 组合了四个既有层：已签名的 Nostr 事件、作为持久存储的 [Radicle](https://radicle.xyz)（点对点 git）、用于加密私聊与群聊的 [Marmot](/zh/topics/marmot/)（Nostr 上的 MLS 群组消息），以及用于身份轮换的 [KERI](https://arxiv.org/abs/1907.02143)（Key Event Receipt Infrastructure）密钥事件日志。一个身份被描述为冷根 Nostr npub 加上一份已被接受的 KERI 日志；日常签名使用轮换的 epoch 密钥，而 Radicle 节点身份则以双重证明方式委派。

该协议族把这些工作拆成[四份各自独立版本化的 0.x 草案](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5)。Core 负责身份、密钥事件日志校验、规范化的 Nostr 字节序列与 Radicle 仓库底座；Comms 负责 Nostr 原生信封、隐私分级、发布与 Marmot 会话；Social 负责公开关注、互动与列表。负责自有设备注册与授权的 Control 尚未完成，不能声称已实现。这些文档仍是可能在 1.0 之前发生破坏性变更的草案，本期是在还没有任何 Heterodyne 客户端发布之前介绍这一协议族。

## 版本发布

### Nostr Java v2.0.8：subscription 隔离与可迁移的 NIP-44

对一个存有五条事件的中继做 gift wrap 查询，返回结果会随机是零条、两条或六条，原因是 [Nostr Java](https://github.com/tcheeric/nostr-java) 这个用于与中继通信并加密 Nostr 载荷的 Java 库，把每一个收到的帧都投递给该连接上的所有监听者。[版本 2.0.8](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8) 把 `EVENT`、`EOSE` 与 `CLOSED` 路由到这些帧所指名的 subscription，因此一次查询的"已存储事件结束"信号不会再关闭另一次查询。像 `NOTICE`、`OK` 与 `AUTH` 这类连接层级的帧仍会到达所有监听者。

同一个[版本](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8)中的 [NIP-44](/zh/topics/nip-44/)（载荷加密）不再需要进程中注册 JCE provider。此前加密只有在该 JVM 里生成过密钥之后才能工作，那个动作会顺带注册 BouncyCastle；而在 Android 上添加名为 "BC" 的 provider 不起作用，因此加密会失败。现在两条加密路径都使用 BouncyCastle 的轻量 ChaCha20 引擎，密钥生成也不再改动进程级的 JCE 状态。此前依赖该库注册 provider 的调用方需要自己注册。这次关闭的 issue 是 [NIP-44 对 JCE provider 的依赖](https://github.com/tcheeric/nostr-java/issues/537)。

### NoorNote v1.3.6：个人资料状态与分类信息

[NoorNote](https://github.com/77elements/noornote) 是一个面向桌面、web 与 Android 的 Nostr 客户端。在 [1.3.4 加入加密社区加入流程](/en/newsletters/2026-08-19-newsletter/#noornote-134-joining-encrypted-communities-from-an-invite-link)一周之后，[版本 1.3.6](https://github.com/77elements/noornote/releases/tag/v1.3.6) 在个人资料的 [NIP-05](/zh/topics/nip-05/)（域名验证）名称下方显示 [NIP-38](/zh/topics/nip-38/)（用户状态）：这是可选带过期时间的 kind `30315` 可寻址事件，承载一行通用状态或音乐状态。点击那一行会设置查看者自己的状态。

来自 [NIP-99](/zh/topics/nip-99/)（kind `30402` 市场报价）的[分类信息](https://github.com/77elements/noornote/releases/tag/v1.3.6)现在会在整个应用中渲染，因此市场插件只在买卖时才需要。个人资料上的私密昵称备注也会以警示橙色显示，配上实心备注图标与橙色头像圈。

### nostrord v2.9.0：按中继限定的群组状态与媒体

在某台主机上退出一个 [NIP-29](/zh/topics/nip-29/)（中继托管群组）群组，此前会在所有其他中继上抑制同一个群组 id，因为面向中继托管社区的跨平台客户端 [nostrord](https://github.com/nostrord/nostrord) 用裸 id 作为退出与删除标记的键。[按中继限定的退出与删除标记](https://github.com/nostrord/nostrord/pull/253)把这些抑制留在产生它们的主机上，因此在两个中继上共用一个 id 的群组不会再被成对退出或丢弃。中继因为你已是成员而拒绝的加入请求，现在算作成功并清除本地标记；这在此前是一个吸收态：自愈清掉了一个槽位，而冷启动又恢复了另一个。

[版本 2.9.0](https://github.com/nostrord/nostrord/releases/tag/v2.9.0) 也会渲染其他客户端写成 `![alt](url)` 的 [markdown 图片嵌入](https://github.com/nostrord/nostrord/pull/254)，而不是在已识别出的 URL 周围显示 markdown 标点。私信支持了 [NIP-17](/zh/topics/nip-17/)（gift wrap 私信）的 [kind `15` 文件 rumor](https://github.com/nostrord/nostrord/pull/275)，因此从 Jumble 发来的加密附件会被下载、解密并显示，发出的附件也会在上传前加密。这个 tag 现在真正带上了[上周报道的 NIP-4e 加密密钥工作](/en/newsletters/2026-08-19-newsletter/#nostrord-implements-an-unmerged-encryption-key-proposal)。该提案仍未合并，nostrord 表示在与草案不一致的地方，其实现遵循 Jumble 已上线的行为。

## 未发布的变更

### Shopstr 把远程签名器与钱包的敏感凭据挪出浏览器存储

[Shopstr](https://github.com/shopstr-eng/shopstr) 是面向 [NIP-99](/zh/topics/nip-99/) 分类信息的 web 市场。在[上月的支付完整性工作](/en/newsletters/2026-07-22-newsletter/#shopstr-binds-payment-validation-to-signed-receipts-and-server-side-prices)之后，它[不再把序列化的 bunker 签名器凭据写入 `localStorage`](https://github.com/shopstr-eng/shopstr/pull/437)。此前 [NIP-46](/zh/topics/nip-46/)（远程签名）的 bunker 载荷里含有仍然有效的 `bunker://` URL 与生成的应用私钥，因此 Shopstr 源上的任何脚本都能接续远程签名会话。现在 bunker 数据只在当前会话的运行内存中，遗留的 bunker 载荷一旦被发现就会移除，非 bunker 类型的签名器保持原有存储行为。

对应的 [NWC 变更](https://github.com/shopstr-eng/shopstr/pull/436)对 [NIP-47](/zh/topics/nip-47/)（wallet connect）凭据做了同样处理。Shopstr 此前把完整的 `nostr+walletconnect://` 字符串，包括用于钱包操作的密钥，当作普通浏览器数据保存，并在结账时复用。现在连接字符串与钱包元数据只留在内存中，读取本地数据时会删除更早的存储副本。在活动会话期间已经运行在 Shopstr 源上的脚本，仍然能看到内存中的这些值。

### Routstr 校验来自中继的服务提供方发现结果

此前单个恶意中继就能决定一个 Routstr 客户端信任哪些推理服务提供方。[Routstr SDK](https://github.com/Routstr/routstr-sdk) 是 Routstr 背后的 TypeScript 库，Routstr 是一个在 Nostr 上发现 AI 服务提供方并用 Cashu 付费的市场。[本周的发现修复](https://github.com/Routstr/routstr-sdk/pull/47)会在任何消费方看到之前，校验中继送来的每一条服务提供方公告、模型列表与评价（kind 38421、38423 与 38425），因此声称使用可信 pubkey 却带着无效签名的评价不会再进入排名。

[远在未来的时间戳](https://github.com/Routstr/routstr-sdk/pull/47)会在选取"最新评价"之前被丢弃。比本地时钟快出十五分钟以上的事件，在实时路径和读取持久存储时都会被剔除，这样伪造的 `created_at` 就无法跨越重启压过合法签名的评价。如果拿不到可信评价，评价关卡会以失败即关闭的方式处理，在评价到达之前把未经评价的服务提供方排除在支付排名之外。运营者仍然可以手动启用某个服务提供方。

### nostr-tools 把 gift wrap 的 rumor 绑定到其 seal 上

此前解开一个 [NIP-59](/zh/topics/nip-59/)（gift wrap）事件时，会解密 wrap、解密 seal，然后返回内层 rumor，却不检查 seal 来自谁。[nostr-tools](https://github.com/nbd-wtf/nostr-tools) 是一个 Nostr 协议辅助函数的 JavaScript 库。[本周的解包修复](https://github.com/nbd-wtf/nostr-tools/pull/545)要求 wrap 必须是 kind 1059、seal 必须是带有效签名的 kind 13，并且 rumor 的 `pubkey` 必须等于 seal 的 `pubkey`。解密 seal 本身已经证明了对 `seal.pubkey` 的控制权。少了最后这项检查，任何人都可以封装一条把别人写成作者的 rumor，让客户端把消息归到那位受害者名下。

[NIP-17](/zh/topics/nip-17/)（gift wrap 私信）使用同一条解包路径，因此这项绑定同样适用于私信。[批量解包](https://github.com/nbd-wtf/nostr-tools/pull/545)现在会跳过未通过这些检查的 wrap，而不是抛出异常，因为 gift wrap 是未经请求就会到来的，一条恶意事件否则会让一次中继查询的其余结果全部作废。

### Haven 增加带签名的中继管理与本地笔记浏览器

[Haven](https://github.com/barrydeen/haven) 是一个自托管 Nostr 中继兼 Blossom 媒体服务器。它新合并的[管理控制台](https://github.com/barrydeen/haven/pull/135)在每个中继端点上提供 NIP-86 管理调用，每个请求都由配置好的所有者的 NIP-98 事件认证。运营者可以管理封禁、允许列表、kind 规则、中继名称与已存媒体，而不必给中继一把签名密钥。只读的笔记浏览器让加密 kind 保持不透明，远程媒体只在点击后加载，从而避免一次自动请求把运营者的 IP 地址泄露给外部主机。

同一个 [Haven 变更](https://github.com/barrydeen/haven/pull/135)加入了持久的流量图表，并修复了默认 LMDB 下的一个故障：统计已存事件可能陷入无限循环、占满一个 CPU 核心并阻塞后续的统计调用。Haven 现在在计数能够终止的场合使用后端计数器，其余场合使用有上限的事件遍历。项目为事件分页、删除、指标持久化、所有者校验与绑定到 URL 的请求签名补上了最初的 23 个测试。

### Amethyst 把 Blossom 授权移出图片加载线程

Android Nostr 客户端 [Amethyst](https://github.com/vitorpamplona/amethyst) [不再在 OkHttp dispatcher 线程上等待 Blossom 读取授权](https://github.com/vitorpamplona/amethyst/pull/3991)。拦截器现在在网络线程之外开始签名，图片抓取器则等待按主机共享的一个签名，然后重试受保护的 blob 请求。因此在签名器响应期间，一批需要授权的图片不会再占满每个主机的全部连接槽位。

同一个 [Amethyst 补丁](https://github.com/vitorpamplona/amethyst/pull/3991)把 token 编码对齐到 BUD-11：不带填充的 Base64url、`server` 作用域，且没有针对单个 blob 的 `x` tag，使一个 token 可以覆盖同一主机上的多个 blob。新的并发测试覆盖缓存、过期、带签名的重试，以及十六个并发调用方共用一个签名的情形。

## 协议与规范工作

### NIP

Snort 与 Ditto 现在把 [NIP-22](/zh/topics/nip-22/)（评论线程）用于普通文本回复，在保留兼容路径的同时收敛到 kind 1111；这并不等于确立了协议范围内唯一的回复 kind。在[六月的修订](/en/newsletters/2026-06-24-newsletter/#kind-1111-as-reply-to-kind-1-notes)移除了禁止对 kind 1 笔记使用 NIP-22 的条文之后，对 [NIP-30](/zh/topics/nip-30/)（自定义表情）的一次[已合并补充](https://github.com/nostr-protocol/nips/pull/2448)把 kind `1111` 列入了可以携带 `emoji` tag 的事件，`content` 中的短代码由该 tag 解析。web 端 Nostr 客户端 [Snort](https://github.com/v0l/snort) 现在[把每条回复都写成 kind 1111](https://github.com/v0l/snort/commit/420ed60e2ff43bd373f2583e171a77002ec9f3a0)，通过大写的 `E`/`A` 根作用域 tag 加载这些评论，同时仍为较早的笔记保留一条可选的 [NIP-10](/zh/topics/nip-10/)（kind 1 回复 tag）路径。同时兼作 Mastodon 服务器与 Nostr 中继的 [Ditto](https://github.com/soapbox-pub/ditto) [把每条回复都发布为 NIP-22 评论](https://github.com/soapbox-pub/ditto/commit/8a0ffc6e3a5d9202ffc452fa0de8ae33b5883384)，文本用 kind `1111`、语音用 kind `1244`，同时继续渲染既有的 kind 1 回复。只理解 NIP-10 的客户端看不到新形式。顶层帖子仍是 kind 1。

[NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）的 `pay_invoice` 请求目前没有标准方式让客户端指定路由费用上限。一份[关于费用上限的开放提案](https://github.com/nostr-protocol/nips/pull/2444)为 `pay_invoice` 增加了以毫聪为单位的可选参数 `max_fee`。遵守该预算的钱包禁止（MUST NOT）发送路由成本超过 `amount + max_fee` 的支付，并且必须（MUST）返回 `FEE_LIMIT_EXCEEDED`，其定义是既未扣款也未尝试支付。支持该特性的实现必须（MUST）在响应中包含 `fees_paid`，以便客户端对账。不支持费用上限的实现会忽略这个未知参数，客户端应当把缺失的 `fees_paid` 字段视为上限可能未被执行的信号。该变更不新增事件 kind，在合并前仍是提案。

一份[关于 NIP-32 语言标签的开放提案](https://github.com/nostr-protocol/nips/pull/2451)会把 `["l", "<BCP-47>", "lang"]` 标准化为作者自行声明的文本语言。由于单字母 `l` tag 本来就可被中继索引，客户端可以用 `{"#l":["ja"]}` 请求日语信息流，不需要升级中继，也不必依赖下载之后不可靠的语言识别。草案还把 NIP-66 中继报告、NIP-68 图片元数据与 NIP-71 音频轨道中的语言示例迁移到同一命名空间。这些标签仍是未经验证的作者声明，该变更尚未合并。

### Nostr Wallet Connect

在超时、重连或漏掉通知之后，wallet connect 客户端需要一种方式来查询单条支付记录，而不必知道是哪个 Bitcoin 支付协议创建了它。[NWC 扩展仓库](https://github.com/nostr-wallet-connect/nwc)中的一份[支付查询开放草案](https://github.com/nostr-wallet-connect/nwc/pull/5)在 NIP-47 核心之外定义了可选的 NWC-09 `lookup_payment`。请求只使用一个选择器：钱包范围内稳定的 `transaction_id`、`lookup_invoice` 已在使用的兼容 BOLT11 的 `payment_hash` 和/或 `invoice` 字段，或者一个 `payment_type` 加上由其他扩展定义的带类型 `lookup` 对象。成功的结果返回一个公共信封（`transaction_id`、`type`、`state`、`payment_type`、以毫聪为单位的 `amount`、时间戳、可选的 `fees_paid` 与 `metadata`，以及一个带判别字段的 `details` 对象），并且必须（MUST）解析为该连接可见的恰好一条记录。钱包禁止（MUST NOT）透露某条不可访问的记录是否存在，匹配到多条可见记录的选择器返回 `MULTIPLE_MATCHES`。状态包括 `pending`、`accepted`、`settled`、`failed`、`expired` 与 `canceled`。同一份提案还增加了复用该信封的 NWC-12 BOLT12 offer 与支付细节。两份文档都仍是草案。

### NAP

一份[开放的 NAP-DISPLAY 草案](https://github.com/napplet/naps/pull/97)会让 napplet 向宿主询问它被允许使用的像素显示设备。它建立在单独推进、[尚未合并的 NIP-5D web applets 提案](/zh/topics/nip-5d/)之上，该提案由 Newsletter #17 介绍，目前仍在已合并的 NIP 集合之外。草案定义了 `display.list`，它会返回不透明而稳定的标识符，附带逻辑宽度、高度以及运行时选择的类型（`lcd`、`eink`、`led-matrix` 或 `other`）；`display.push` 则提交一批非空的、按坐标寻址的三字节 sRGB 像素。运行时发现会把逻辑 RGB 映射到设备原生的色深、方向与刷新方式，并且可以（MAY）对更新做旋转、重排、量化、抖动或合并。宿主壳层策略会控制某个 napplet 可以列出或写入哪些显示设备，并且可以（MAY）拒绝、限速或限制批次大小。在应用任何像素之前，运行时会校验整批数据，因此一次失败的 push 不会改变设备上的任何内容。成功只意味着批次被接受，并不意味着硬件刷新已经完成。

### Marmot

一项[开放的 Marmot 实验](https://github.com/marmot-protocol/marmot/pull/417)会用一种有界的 Commit 形式，替换已撤回的 External Commit 草案来处理同一账户的加入。Nostr 上的 MLS 群组消息协议 [Marmot](/zh/topics/marmot/) 在该草案中把无数据组件 `0x800d`（`marmot.same-account-membership.v1`）指定为协商后的行为标记。在它被要求的期间，当前叶子可以撰写恰好一个内联的同账户 Add，或者一到四个内联的同级 Remove，每个都带常规 UpdatePath 与普通收敛优先级，并且每个 Commit 必须（MUST）为任一账户最多留下五个当前叶子。配对使用由发起方展示的短时效二维码（`marmot-pairing-v1:`），其密钥在与载体无关的通道上供给 HKDF-SHA256 与 ChaCha20-Poly1305。仅存于本地的 kind `453` 证明把会话绑定到共享账户密钥，并且从不经中继传播。在收到匹配的 Welcome 之后，加入方的第一个应用载荷是一条不渲染的 kind `452` 确认，绑定到 Welcome 与 GroupInfo 的摘要，因此逐字节相同的 Welcome 可以在不再次消耗 KeyPackage 的情况下恢复。已配对的发起方是加入方在该分支上的信任根，并不证明全局最终性。配套的账户同步文档仍属探索性质且不具互操作性。该实验不属于已采纳的基础配置。

## Nostr 六年八月史

历年八月都在追同一个互操作性问题：客户端如何指名一个目标，并把反馈挂到它上面。[最初的协议仓库](https://github.com/nostr-protocol/nostr)在 2021 年八月没有记录任何提交，已签名事件的核心因此静止不动。随后 [NIP-25](/zh/topics/nip-25/)（回应）在 2022 年走出了只限 kind 1 的框子。常规可替换记录在 2023 年获得了标识符为空的 `naddr` 与 `a` 坐标；2024 年，独立的[参数化可替换类别被更名为可寻址事件](https://github.com/nostr-protocol/nips/commit/ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d)，线上格式没有变化。回应在 2025 年转向了外部媒体。[NIP-22](/zh/topics/nip-22/)（评论线程）的 kind 1111 在 2026 年抵达了真正在写入它的客户端。这条脉络从一份静止的协议文档，走到一套能横跨笔记、可替换记录与网络之外对象的共用回复与回应词汇。

### 2021 年八月

最初协议仓库的[2021 年八月提交窗口](https://api.github.com/repos/nostr-protocol/nostr/commits?since=2021-08-01T00:00:00Z&until=2021-08-31T23:59:59Z)是空的。那个静默月份之前的最后一次变更是 6 月 18 日的 NIP-05 草案，它把 DNS 域名标识符作为指向公钥的人类可读指针加了进来。[NIP-05](/zh/topics/nip-05/)（域名标识符）后来改为 well-known JSON 文件，但在 2021 年中它仍是一次 DNS TXT 查询。八月既没有扩展这项标识符工作，也没有新增事件 kind 或中继消息。

同样空白的窗口也出现在规范之外早已存在的工具里。2021 年 1 月创建的命令行客户端 [noscl](https://github.com/fiatjaf/noscl/commits?since=2021-08-01&until=2021-09-01)在八月没有提交，[go-nostr](https://github.com/nbd-wtf/go-nostr/commits?since=2021-08-01&until=2021-09-01) 与 [nostr-tools](https://github.com/nbd-wtf/nostr-tools/commits?since=2021-08-01&until=2021-09-01)也一样。协议活动直到年末才重新开始，仓库分配了 [NIP-09](/zh/topics/nip-09/)（事件删除请求），并用 well-known JSON 标识符文件取代了 DNS 方案。2021 年八月是六月标识符草案与十二月删除及 well-known JSON 工作之间的静默阶段，期间[已签名事件与中继的模型](https://fiatjaf.com/nostr.html)按原样成立。

### 2022 年八月

8 月 19 日，一次 [NIP-25 修订](https://github.com/nostr-protocol/nips/commit/7af2540c6e392d5cb789c743b1dd237294388649)把 kind 7 回应的目标从 kind 1 文本笔记扩展到其他笔记。kind 7 事件与 `+`/`-` 约定此前已在草案中。这项互操作性变更让点赞、反对或表情可以挂到个人资料、关注列表，或任何后来复用同样 `e` 与 `p` tag 的事件 kind 上。

当前的 [NIP-25 规范](https://github.com/nostr-protocol/nips/blob/master/25.md)保留了这项一般化：回应表示用户对其他事件的反应，可寻址目标还会收到一个带 `kind:pubkey:d-tag` 坐标的 `a` tag。Android 客户端 [Amethyst](https://github.com/vitorpamplona/amethyst/blob/main/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt)在它的回应构造器里实现了这份约定。该构造器接受任何事件，写入 `e`、`p` 与 `k` tag，并在目标是可寻址事件时加上 `a` tag。这把回应目标一般化到了 kind 1 之外；八月后续的变更又补上了稳定坐标与评论上下文 tag。

中继软件也在把 tag 规则落成存储行为。8 月 17 日，nostr-rs-relay [不再把每个看起来像十六进制的 tag 值都当作二进制索引键](https://github.com/scsibug/nostr-rs-relay/commit/035cf34673ae23407bda6656eef505b3178482ab)。它把那项优化限制在单字母 tag 与小写十六进制值上，从而保留普通文本 tag，而不是把它们解码成过滤器无法匹配的形式。因此那个月把互操作性的两面接到了一起：规范拓宽了一次互动可以指向什么，而中继则纠正了这些目标 tag 如何被索引与取回。

### 2023 年八月

8 月 24 日，[NIP-19](/zh/topics/nip-19/)（bech32 标识符）[定义了如何把非参数化的可替换事件编码为 naddr](https://github.com/nostr-protocol/nips/commit/208dee210249f84496ddfa823542d023e23b3edb)。标识符字段即 `d` tag，对于仅按 pubkey 与 kind 替换的类别（例如元数据与联系人列表）成为空字符串。五天之后，[NIP-01](/zh/topics/nip-01/)（基础事件与中继协议）[补上了对应的 a-tag 格式](https://github.com/nostr-protocol/nips/commit/e50bf508d9014cfb19bfa8a5c4ec88dc4788d490)：末尾带冒号且没有标识符的 `kind:pubkey:`。客户端从此可以指向一条可替换记录，而不必等待某个会被下一次替换作废的具体 event id。

[当前的 NIP-19 文本](https://github.com/nostr-protocol/nips/blob/master/19.md)仍然告诉实现者对这些可替换事件使用空字符串。JavaScript 标识符库 [nostr-tools](https://github.com/nbd-wtf/nostr-tools/blob/master/nip19.ts)通过 `naddrEncode` 编码该字段，因此调用方可以传入一个空标识符并产出可分享的坐标。2023 年八月的工作把可替换状态变成了评论、回应或分享链接在底层事件被取代之后仍能指名的东西。次年八月标准化了相关参数化可替换类别的术语，而后来的评论 tag 则把这套坐标语法复用为 `A` 与 `a`。

同一时期，私密载荷也在变得可迁移。8 月 24 日，rust-nostr [在其 JavaScript 绑定中加入了 NIP-44 加密与解密函数](https://github.com/nostrdevkit/nostr/commit/39e581d398d926ff37a6b57a1c6d5fceae270d77)，把带版本的会话密钥方案除原生 Rust 调用方之外也开放给 web 应用。8 月 22 日，Amethyst [把 NIP-44 加密与消息事件格式分离](https://github.com/vitorpamplona/amethyst/commit/fa4257ad7d7afa76ccb368b4cf6cadefa39461ba)，体现了内容如何加密与应用如何传输之间的协议分工。稳定坐标让公开对象更易引用；可复用的加密 API 让私密内容更易在实现之间迁移，而不必与某一种消息 kind 绑死。

同一个月也给相邻的密钥隔离、界面与教育工作带来了资金。[8 月 17 日的一轮 OpenSats 资助](https://github.com/OpenSats/website/commit/acd33f11b7529c34a846e8c4b4a6c63e7187f970)把 Nostr Fund 的资助分配给了 Amber、共用的 Nostr 界面设计以及 Nostr 用例教育。Amber 的资助聚焦于通过 NIP-46 把签名密钥留在专门的 Android 应用里，设计与教育资助则处理新用户上手与可复用的应用模式。更大范围的 Nostr 体系正通过规范提交、密钥隔离、界面工作，以及作为共用基础设施获得资助的开发者教育向前推进。

### 2024 年八月

8 月 20 日，规范在 NIP-01 与另外十六份文档中[把"参数化可替换事件"更名为"可寻址事件"](https://github.com/nostr-protocol/nips/commit/ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d)，涵盖长文文章、直播活动、列表、日历与分类信息。线上格式没有变化。`kind:pubkey:d-tag` 仍是坐标。变化之处在于每一份原本就使用这套坐标的规范，现在都用同一个词来称呼它。

那套词汇正是当前实现所交付的。[NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)把可寻址事件按 kind、pubkey 与 `d` tag 存为最新一条记录。[NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)把 naddr 称作 "a nostr addressable event coordinate"。上文引用的 Amethyst 回应路径在写入 `a` tag 之前把目标类型标为 `AddressableEvent`。2023 年的坐标扩展与 2024 年的术语变更都使用 `kind:pubkey:d-tag` 这套坐标语法，而 NIP-01 继续区分常规可替换事件与可寻址事件。因此后来的评论可以用大写 `A` 取回一条可寻址讨论，不必关心当下是哪个 event id 占着那个地址。

存储协议也在应用同一种对显式标识符的偏好。8 月 27 日，Blossom 的 BUD-04 [允许一个授权事件携带多个 blob 哈希 `x` tag](https://github.com/hzrd149/blossom/commit/4325aa79891cb4d68448ce16e5fa5519058eae4b)，这样客户端就能授权一批有上限的上传、镜像或删除，而不必假装这些哈希描述的是同一个对象。四天之后，项目[澄清了它的 blob 描述符并补上一个示例](https://github.com/hzrd149/blossom/commit/95eb92e70768b0a2d5bab3dc42a5e3418f9055ec)。Nostr 事件在协调内容寻址的媒体操作，而字节仍留在媒体服务器上，从而把已签名的授权与存储传输分开。

8 月 29 日，远程签名对不完美的中继集合变得更宽容。go-nostr 修改了它的 NIP-46 客户端，使[一个故障中继无法阻塞通过其他已配置中继发出的请求](https://github.com/nbd-wtf/go-nostr/commit/5edb54efee52f469fe62180c20d2876fe9c72910)：中继连接与发布尝试各自独立进行，只要任一连接成功，调用就继续。8 月 19 日，OpenSats 还[宣布了对 Amethyst 作者 Vitor Pamplona 的长期支持](https://github.com/OpenSats/website/commit/b0ac18552a80c662b6ca33381abeed5c3d833a4c)，涵盖 NIP-17 私密消息、跨平台库与 outbox 模型方面的工作。协议词汇、有韧性的传输、隐私工作与持续的维护资金正朝同一个目标汇聚：能够跨设备、在参差不齐的中继条件下继续工作的客户端。

### 2025 年八月

8 月 22 日，[NIP-25 获得了对外部内容的回应](https://github.com/nostr-protocol/nips/pull/2020)。针对非 Nostr 原生事件的回应必须是 kind 17，并且必须携带 [NIP-73](/zh/topics/nip-73/)（外部内容标识符）的 `k` 与 `i` tag，取代较早的网站 `r` tag。已合并文本中的示例是一个 web URL（`k=web`）与一集用节目 GUID 和条目 GUID 标识的播客，并以 Fountain 的 URL 作为提示。回应在 2022 年离开了 kind 1。此时它们离开了 Nostr 事件集合本身。

2025 年 8 月 15 日发布的 [Fountain 1.3](https://blog.fountain.fm/p/1-3)在规范合并之前就交付了这些点赞，并说明它们由 Nostr 驱动，以便其他播客应用能够读取。今天的 [NIP-25 文档](https://github.com/nostr-protocol/nips/blob/master/25.md)仍在使用 Fountain 的播客 GUID 示例。到 2025 年八月，一个回应坐标已经可以用评论后来用于外部根节点的同一套标识符语法，去指名一集播客或一个网页。

### 2026 年八月

这个八月把评论线程带进了那些写普通回复的客户端。后来被合并的[六月修订](/en/newsletters/2026-06-24-newsletter/#kind-1111-as-reply-to-kind-1-notes)删掉了那条告诉客户端不要在短笔记上使用 NIP-22 评论的条文。接着 [NIP-30](/zh/topics/nip-30/)（自定义表情）[把 kind 1111 加了进来](https://github.com/nostr-protocol/nips/pull/2448)，与笔记、回应和用户状态并列，因此评论也能携带那些 kind 早已使用的表情 tag。规范工作是许可。客户端工作是落地。

web 客户端 [Snort](https://github.com/v0l/snort/commit/420ed60e2ff43bd373f2583e171a77002ec9f3a0)现在默认为 kind 1 目标发布 NIP-22 评论，通过大写 `E`/`A` 根 tag 订阅线程，并在通知中接受 kind 1111。社区 web 客户端 [Ditto](https://github.com/soapbox-pub/ditto/commit/8a0ffc6e3a5d9202ffc452fa0de8ae33b5883384)把每条回复都发布为 NIP-22 评论，文本用 kind 1111、语音用 1244，包括对 kind 1 笔记的回复，同时仍然读取 [NIP-10](/zh/topics/nip-10/)（笔记串联）回复。六年间的转变就体现在这些默认值上：2022 年一般化了回应，2023 与 2024 年为坐标定名，2025 年把回应指向网络之外，2026 年则让评论成为面向这些同样目标的共用回复事件。

私密群组的基础设施把恢复能力定义成了互操作性要求。Marmot 的[8 月 13 日持久性与重启约定](https://github.com/marmot-protocol/marmot/commit/4a2bc65f8db5866cec3b2a127dedb37818eaf207)规定了哪些本地 MLS 与发布状态必须在重启后存活，并要求客户端在继续群组操作之前先对齐已持久化的状态。这把八月的脉络推进到了指名目标之外：一个成熟的客户端还必须保留足够的密码学与投递状态，才能在中断之后安全地接续。共用的事件形态只有在实现能够恢复使用它们所需的状态时才有用。

---

发送 [NIP-17](/zh/topics/nip-17/) 私信，通过 [Nostr Compass 项目](https://github.com/andotherstuff/nostr-compass)分享项目或新闻。
