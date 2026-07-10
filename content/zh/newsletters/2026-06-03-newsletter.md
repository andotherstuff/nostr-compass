---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-01
---

Amber 6.2.0 在规范之前发布了 NIP-44 v3 加密。Mostro 通过八个 PR 落地了 Cashu 结算托管的基础，将现有的 Cashu Development Kit 包装为与 Lightning 并列的第二个结算后端。NIP-F4 podcasts 在 27 个月的辩论后合并。fiatjaf 打开了一个有争议的 NIP-17 密钥解耦提案，重新开启了 bunker 与 Marmot 之间的架构争论。Amethyst 在 52 个未发布的 PR 中落地了 NIP-32 hashtag 标签、专用播客屏幕和链上 zaps。

## 头条报道

### Amber 6.2.0：NIP-44 v3 加密发布

[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0) 于 6 月 1 日发布，添加了 [NIP-44 v3 加密支持](https://github.com/greenart7c3/Amber/pull/448)，具有专用的批准屏幕、intent 预览、bunker 预览、历史记录和对无效请求的自动拒绝。该版本还注册了 [NIP-44 v3 ContentProvider authorities](https://github.com/greenart7c3/Amber/commit/8b93340)，因此其他 Android 应用可以在现有 v2 路径旁请求 v3 加密。NIP-44 本身是版本化的加密 payload 规范，由 [NIP-17](/zh/topics/nip-17/) 私密 DM、NIP-46 bunker 流量和其他 Nostr 原语使用；Amber 中的 v3 是与 v2 并存的可选功能，通过独立的 signer 方法发出信号，因此接收方 client 可以明确协商算法。相应的 NIPs PR 尚未落地，因此 Amber 在协议共识之前推出 v3，wire 格式和 ContentProvider authority 已注册，供下游 client 集成。

NIP-46 会话现在在连接时自动接受 ping 请求，移除了配对后第一次往返的提示。`sign_message` signer 方法在被弃用且未使用后被完全移除。

由于 Amber 是主导的 Android signer，每个想要 v3 的下游 client 都必须以 Amber 的 wire 格式为目标，直到 NIPs PR 落地。这让 Amber 在协议赶上之前隐性地对最终 v3 规范有发言权。这种权衡是真实的：生产中的 v3 让 Amber 为最终的 NIP 收集实现反馈，代价是一个临时的单一实现参考点，其他 client 现在必须匹配。

### Mostro：通过 CDK 的 Cashu 托管集成

grunch 本周在 MostroP2P 中落地了八个 PR，将 Cashu 现有的 P2PK 多签原语（NUT-10 和 NUT-11）作为 Lightning 并列的第二个结算后端集成到 Nostr 协调的 P2P Bitcoin 交易所。加密原语是 Cashu 的；工作是集成脚手架和一个新的托管后端 trait。[Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0) 于 5 月 30 日发布，添加了 [2-of-3 多签托管的协议类型](https://github.com/MostroP2P/mostro-core/pull/150)、每 proof P_M 签名，并允许托管事件通过响应验证。架构记录在 [PR #756](https://github.com/MostroP2P/mostro/pull/756) 中，使用 [PR #757](https://github.com/MostroP2P/mostro/pull/757) 中澄清的每订单交易密钥。

实现在一天内通过六个后续 PR 推出。[F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758) 添加了配置、托管模式和条件启动。下一部分 [F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760) 定义了一个 `EscrowBackend` trait，包含 Lightning 实现和 Cashu stub，让 Mostro 可以在不改变订单状态机的情况下切换结算后端。[F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759) 为 mint 和钱包操作包装了 [CDK](https://github.com/cashubtc/cdk)（Cashu Development Kit）。[F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761) 中的数据库工作添加了 compare-and-swap 托管锁和活动锁定查询。[F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762) 在专用 CI 作业中构建了一个容器化 mint 用于端到端托管测试。Mostro 流程已经在 relay 上使用 NIP-59 gift-wrapped DMs 进行订单协调，因此 Cashu 托管作为 Lightning 并列的第二个结算选项插入，无需触及 wire 协议。

## 发布

### ngit v2.5.0：GRASP 备选和惰性 git fetch

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0) 更改了 `git push pr/<branch>` 和 `ngit send` 的默认行为，当仓库至少注册了一个 GRASP 服务器时，为新提案生成 PR kind。此前这仅对超过 60 KB 的过大 commits 或包含 submodules 的 commits 触发。当 PR 无法推送到仓库的 GRASP 服务器时，ngit 现在通过声明的服务器回退到 GRASP-06 路由。`ngit send --git-server` 标志或 `git push -o git-server=<url>` 让贡献者可以明确地针对自定义 git URL 或 GRASP 服务器。

`ngit init` 重新发布现在保留来自现有公告的未知标签，因此由未来 ngit 版本或第三方工具添加的标签在重新发布后存活。一个黄色警告列出被携带的标签，`--clean` 按需移除它们。`ngit pr apply`、`ngit pr checkout` 和 `ngit pr list` 惰性咨询 git 服务器并共享单一 fetch 辅助函数，因此当 commit 已经在本地时 checkout 不再无条件 fetch。当 repo 声明的 git 服务器不携带 PR tip 时，`ngit pr checkout` 也尝试来自 PR 事件的提交者提供的克隆 URL 作为备选，匹配 `ngit pr apply` 中的现有行为。ngit 是通过 Nostr 进行 git 协作的参考 [NIP-34](/zh/topics/nip-34/) 实现，v2.5.0 使 GRASP 成为新贡献者的一流路径。

### Jumble v26.5.7：EXIF 剥离和已验证 zap 计数

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7) 添加了两个直接影响用户隐私和数据完整性的更改。EXIF 位置和相机标识符现在在图像上传离开 client 之前被剥离，关闭了一个长期存在的元数据泄漏面，该面影响了从 Jumble 发布的每张图像。Zap 计数现在仅从加密验证的收据计算，修复了让攻击者在笔记上夸大 zap 总数的畸形 zap 事件导致的膨胀计数。该版本还为 [NIP-17](/zh/topics/nip-17/) DM 添加了发送者身份验证，关闭了发送者可以在 seal 中伪造其 `pubkey` 的欺骗面。

### nostr-calendar v1.6.0：RSVP 和重复参与者处理

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0) 落地了 Formstr 的 RSVP 流程（[PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)）并防止事件邀请中的重复参与者（[PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)）。publish 函数中的 `waitForAll` 选项现在默认为 false，因此 UI 不会在慢速 relay 上阻塞（[PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)）。[PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157) 发布了 Formstr 的两个用于预约调度和预订的 NIP 提案草案。

### Sprout 0.3.6：Sprout × mesh-llm 和 channel 部分

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6) 是本周从 v0.3.1 到 v0.3.6 的六个版本发布的头条。进程内 Sprout × mesh-llm 集成在 [PR #798](https://github.com/block/sprout/pull/798) 中落地，让 Sprout 可以通过 relay 准入提供和消费 mesh-llm 节点。用户定义的 channel 部分通过 Nostr 在 [PR #792](https://github.com/block/sprout/pull/792) 中跨设备同步，channel 部分通过 relay 同步在 [PR #800](https://github.com/block/sprout/pull/800) 中到达移动端。带有可变关注和静音控件的线程感知通知在 [PR #761](https://github.com/block/sprout/pull/761) 中到达。

带下载卡的任意文件类型附件在 [PR #810](https://github.com/block/sprout/pull/810) 中到达，将 Sprout 扩展到仅图像附件之外。移动端获得了 Pulse 社交信息流标签（[PR #772](https://github.com/block/sprout/pull/772)）以及跨信息流、撰写和过滤器接口的 Pulse 打磨（[PR #796](https://github.com/block/sprout/pull/796)）。

### NostrBotKit v0.5.0：Rust 机器人框架中的 Marmot 群组聊天

[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md) 于 5 月 24 日在 Codeberg 上发布，为自托管的 Rust 机器人框架添加了 [Marmot](/zh/topics/marmot/)（MLS-over-Nostr，[NIP-104](https://github.com/nostr-protocol/nips/pull/2014)）支持。当 `marmot: true` 被设置时，机器人发布其 MLS key packages（kind 443、30443、10051）、自动接受群组邀请，并在加入的群组中监听消息。两个新的命令类型 `dm_marmot` 和 `dm_marmot_npub` 让机器人可以通过 cron 作业或 webhook 向命名的 Marmot 群组或 1:1 Marmot 聊天发送消息。为了防止与其他机器人的反馈循环，NostrBotKit 机器人仅响应通过 `/command` 或 `@botname/command` 明确寻址给它们的消息。使用 MIP-04 的加密附件通过 Blossom 或 NIP-96 自动解密并重新上传，MLS 状态数据库使用从机器人的私钥派生的密钥加密。NostrBotKit 是第一个发布 NIP-104 机器人支持的 Rust 框架，为 Marmot 加密的机器人部署开辟了与现有 TypeScript 路径不同的运营者配置文件。

### noscrypt v0.1.14：已签名的加密库发布

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14) 是 C 加密库的安全版本，被几个 Nostr client 用于 secp256k1、NIP-04 和 NIP-44 原语。该版本随 [PGP 签名的下载](https://www.vaughnnugent.com/resources/software/modules/noscrypt) 一起发布，可以针对维护者的公钥进行验证。捆绑 noscrypt 的下游 client 应在集成之前验证签名。

### Chama v1.3.0：使用 Fedimint 的新 Nostr 原生 P2P 托管

[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0) 于 6 月 1 日发布，是四个版本发布的头条，一个新的 Nostr 原生 P2P 托管 client，使用 Fedimint ecash 和 2-of-3 Shamir 秘密共享进行结算。该项目在 [getchama.app](https://getchama.app) 发布，无需服务器运行。v1.3.0 引入了"heal that sticks"（在会话重启后仍然存活的成功重新广播和交易恢复）和支付轨道匹配，其中偏向美国的 Chamas 首先展示美国支付轨道。多单位店面基础工作在 [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11)（多单位模式）和 [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12)（店面库存会计 + 原生 Fedimint 桥接恢复加固）中落地。Chama 加入 Mostro 和 Shopstr 的 Nostr 市场类别，以其无服务器架构和基于 Fedimint 的托管结算而与众不同。

## 未发布的更改

### Amethyst：NIP-32 hashtag 标签、播客屏幕、音乐曲目

Amethyst 本周合并了 52 个 PR 和 411 个 commits，没有削减版本标签。最大的功能新增是 [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111)，它使用 kind 1985 事件（带有 `L` 命名空间和 `l` 标签）实现了 [NIP-32](/zh/topics/nip-32/) hashtag 标签和基于标签的 hashtag 信息流。这用一个基于 labeler 的发现模型取代了脆弱的文本匹配 `#tag` 机制，用户可以像关注内容创作者一样关注特定的 labeler npubs。[PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) 添加了一个带有集数列表和内联播放器的专用播客屏幕，在 [NIP-F4](/zh/topics/nip-f4/) 播客规范合并后的几天内到达。[PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071) 添加了带有关注列表过滤的软件应用信息流，[PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067) 通过 [NIP-51](/zh/topics/nip-51/) sets 添加了音乐曲目和播放列表支持。

匿名帖子上传的临时 signer 在 [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123) 中落地，让用户可以在不向上传服务暴露其身份密钥的情况下匿名发布。带有 Arti v2.3.0 集成测试的 Tor 自愈看门狗到达 [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053)，在临时网络中断期间加强了 Amethyst 的 Tor 路由。链上 zaps 和来自 Gemini 的返回用户的 NIP-05 过滤器在 [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052) 中落地，将 zap 接口扩展到 Lightning 之外的链上 Bitcoin 支付。

### Shopstr：OpenGraph 预览 URL 验证

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504) 在市场列表中渲染 OpenGraph 预览 URL 之前对其进行验证，关闭了一个潜在的 XSS 面，恶意卖家可以通过精心制作的 OG 元数据嵌入脚本化内容。Shopstr 托管的商店为外部链接显示 OG 预览，未验证的 URL 让攻击者可以将任意内容注入商店 UI。

## NIP 更新和协议规范工作

### NIP-F4（Podcasts）经过两年合并

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093) 于 5 月 28 日合并，距离 fiatjaf 打开原始草案两年三个月后。NIP-F4 将播客集数定义为 kind 54 事件，带有音频文件元数据的 `imeta` 标签（URL、mime type、语言 ISO code、备选 URL、NIP-96 服务标志、比特率、时长）、一个 `title` 标签、可选的 `image` 和 `description` 标签，以及主题标签的 `t` 标签。该规范有意保留 RSS 作为真实来源：集数可以携带一个 `i` 标签引用 RSS 播客 GUID，让 Nostr client 可以链接到现有的播客 feed 而不复制音频托管。PR 线程中的长期辩论（与 podcast-namespace 联合作者 Dave Jones、Alex Gleason 和 Mike Terenzio）确定了一个共存模型，其中 Nostr 在 RSS 之上提供社交层，而 RSS 保留分发层。Amethyst 的 [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) 播客屏幕在规范合并后的几天内到达，Jumble 的 GIF 选择器工作也包括早期的播客附件脚手架。

### NIP-17 密钥解耦（PR #2361）

fiatjaf 于 6 月 1 日打开了 [PR #2361](https://github.com/nostr-protocol/nips/pull/2361)，提议 NIP-17 将身份密钥与加密密钥分离。接收者在一个新的 kind 10044 事件中广告其加密密钥，发送者使用该广告的密钥（当存在时）进行 gift-wrap 内部 seal，仅在广告不存在时回退到接收者的身份密钥。该 PR 还向 seal 添加了一个 `n` 标签，携带发送者的加密 pubkey，因此接收者可以在不对每个已退役密钥进行试解密的情况下派生正确的会话密钥。声明的动机是 bunker UX：在当前设计下，bunker 用户必须通过 signer 往返每个收到的 DM 进行解密，因为加密密钥就是 signer 持有的身份密钥。解耦让 client 可以在本地持有加密密钥，同时将身份密钥保留在 bunker 中用于签名。

该提议吸引了本周最有争议的审查。Cody Tseng（Jumble）支持它作为跨 client DM 互操作的最简单路径。Vitor Pamplona（Amethyst）在两个方面反对：它在 bunker 之外添加了一个新的长期解密秘密，不发布它的 client 将静默地无法解密来自发布它的 client 的消息，没有降级路径，因为断裂在 seal 层。Pamplona 认为这个问题已经被 [Marmot](/zh/topics/marmot/) 的 key packages 和 epoch 轮换正确解决，将密钥分离改造到基本 NIP-17 规范中会产生 Marmot 花了两年时间设计来避免的那种互操作失败。fiatjaf 的反驳有三部分：解耦是每接收者可选的，n 标签修复解决了试解密的担忧，替代方案是在 Telegram 吃掉消息用例的同时保持 bunker UX 破损。该线程仍未合并决定开放，是本季度最受关注的 NIP 讨论。

### NIP-Silent Payments 支付流程（PR #2362）

[silentius-satoshi 于 6 月 1 日打开了 PR #2362](https://github.com/nostr-protocol/nips/pull/2362)，作为更广泛的 [Nostr Silent Payments NIP 草案（PR #2355）](https://github.com/nostr-protocol/nips/pull/2355) 的伴侣。支付流程 NIP 定义了 kind 8352 用于 silent payment 收据通知（通过 [NIP-59](/zh/topics/nip-59/) gift wrap 交付，因此收据链接在公开的 relay 层不可观察），以及 kind 10353 用于跨相同 Silent Payments 钱包的设备同步的加密 UTXO 缓存。这两个一起让付款人可以使用 Nostr 原生原语向 Silent Payments 地址发出付款信号，而不在开放的 relay 层暴露链上链接。

### NIP-PIP Perfect IP Packets（PR #2364）

[RandyMcMillan 于 6 月 1 日打开了 PR #2364](https://github.com/nostr-protocol/nips/pull/2364) 作为草案。它引入了一个数据包树传输，具有三个新的可寻址 kind：39078 携带清单、39079 携带单个切片、39080 携带修复请求。该规范定义了一个 wire 格式，其中大文件被分成可寻址的切片，清单描述切片树，修复请求让接收者可以请求缺失的切片。适用早期草案状态，该提议尚未吸引维护者审查。

### NIP-29 音频/视频实时空间（PR #2238）

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238) 于 5 月 28 日合并，扩展了 [NIP-29](/zh/topics/nip-29/) 基于 relay 的群组，具有音频和视频实时空间支持。群组现在可以引用一个活动的实时空间会话，让 [NIP-53](/zh/topics/nip-53/) 风格的实时活动事件在 NIP-29 群组上下文中锚定。

### NIP-71 视频多音频轨道（PR #2255）

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255) 于 5 月 28 日合并，向 NIP-71 视频事件添加了音频轨道 `imeta` 标签。新格式携带 URL、hash、mime type、语言标签（带有 ISO-639-1 加上原始版本标志）、备选 URL、NIP-96 服务信号、比特率和时长。这实现了仅音频流（视频播客）、稳定音频的分辨率切换、多语言轨道，以及当服务器不将音频直接嵌入视频文件时减少存储。client 应在假设单轨道行为之前检查音频轨道可用性。

### NIP-59 临时 gift wrap（PR #2245）

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) 于 5 月 28 日合并，添加 kind 21059 作为现有 kind 1059 gift wrap 的临时对应物。语义与标准 NIP-59 wrap 匹配，但遵循 NIP-01 的临时事件规则（relay 在广播后丢弃它们，不持久化它们）。这让应用可以根据需求选择持久性：输入指示器和 presence pings 受益于临时，而 DM 历史需要持久性。

### NIP-78 应用特定 kind（PR #2292）

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292) 于 5 月 28 日合并，将 NIP-78 应用特定数据重新分类为普通可寻址 kind，删除了之前的独立范围。这简化了可替换性语义，并将 NIP-78 与其他应用状态 NIP 使用的可寻址事件模型保持一致。

### NIP-85 澄清（PR #2304）

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304) 于 5 月 28 日合并，对 [NIP-85](/zh/topics/nip-85/) Trusted Assertions 中关于每个服务提供商的多个密钥和 relay 的语言进行了小的改进，澄清了 relay 断言服务的运营者密钥轮换路径。

### NIP-01 relay 连接管理单行（PR #2307）

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307) 于 5 月 28 日合并，向 NIP-01 添加了一个关于 client 应如何处理 relay 连接生命周期的单一句子。该修复解决了一个长期存在的差距，即 client 对是否在 fetching 后保持 WebSocket 连接打开存在分歧，导致在丢弃空闲连接的 relay 上静默丢失消息。

### NIP-C7 kind 9 聊天约束（PR #2310）

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310) 于 5 月 28 日合并，将 NIP-C7 聊天视图限制为仅 kind 9 消息。这在实现 NIP-C7 风格聊天接口的 client 中将临时聊天与 kind 1 时间线帖子分开。

### NIP-55 简化（PR #2363）

由 greenart7c3 于 6 月 1 日打开的 [PR #2363](https://github.com/nostr-protocol/nips/pull/2363) 简化了 Android signer 应用规范。Vitor Pamplona 签署为"看起来不错"，fiatjaf 询问它是否准备好合并。该变更为 Amber 本周发布的 NIP-44 v3 ContentProvider authority 注册铺平了道路。

### NIP-44 v3（Amber 实现领先于规范）

Amber 在 v6.2.0 中发布了 NIP-44 v3，八个 commits 实现了加密升级和 ContentProvider authority 注册，但 NIPs repo 规范 PR 尚未落地。NIP-44 本身定义了在已签名事件内使用的版本化加密 payload 格式；现有的 v2（自 2024 年以来在生产中）使用 secp256k1 ECDH、HKDF、padding、ChaCha20、HMAC-SHA256 和 base64。v3 wire 格式在 nonce 之前添加了一个新的版本字节（0x03），允许接收方 client 明确协商算法。Amber 的实现包括对无效 v3 请求的自动拒绝、与 v2 批准不同的专用批准屏幕，以及用于历史记录的每方向明文日志记录。在 NIPs PR 合并之前，v3 是 Amber 特定的扩展。将其视为前瞻性信号，而不是稳定的协议范围信号。

## NIP deep dive：NIP-32（Labeling）

[NIP-32](/zh/topics/nip-32/) 定义了任何 Nostr 参与者使用可寻址 kind 1985 事件为事件、pubkey、relay、URL 或主题打标签的结构化方式，使用带命名空间的标签词汇。该规范引入了两个新标签：`L` 表示标签命名空间，`l` 表示该命名空间内的标签。标签目标标签（`e`、`p`、`a`、`r` 或 `t`）指定被标记的内容。命名空间要求防止多个标签系统冲突：`nip28.moderation` 中的 `spam` 标签与 `relay-report` 中的 `spam` 标签具有不同的语义。

使 NIP-32 在审核之外有用的设计选择是标签是断言，不是协议级真理。kind 1985 事件仅表示特定 pubkey 在特定命名空间中标记了特定目标。信任模型委托给 client：每个 client 选择尊重哪些 labelers、读取哪些命名空间，以及为每个标签提供什么 UI 承受性。同一原语承载内容警告、许可证分配、kind 1 笔记上的 ISO-639-1 语言标签、ISO-3166-2 地理标签、内容分类、分布式审核建议和声誉分数。

Amethyst 本周的 [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111) 是迄今为止最大的部署。它通过 NIP-32 添加 hashtag 标签和基于标签的 hashtag 信息流，让用户可以按可信 labelers 分配的标签浏览。最初在 Nostr 上驱动 hashtag 发现的早期 `#tag` 文本匹配机制作为未标记笔记的备选保留。hashtag 作为标签的模型意味着同一笔记可以在不同 labelers 分配的多个标签下被发现，用户可以在不影响底层笔记的情况下静音或提升特定 labelers。

自我标签也受支持。作者可以直接将 `L` 和 `l` 标签附加到自己的 kind 1 笔记上以声明语言、位置和主题。带有 `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]` 标签的笔记自我识别为英语，可以由语言感知的 client 过滤，无需第三方标签基础设施。

将 kind 1 笔记标记为英语并为其分配审核标签的 NIP-32 标签事件示例：

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

Amethyst 的推出与最近的 Trusted Relay Assertions 工作相结合，表明 NIP-32 正在成为 Nostr 上任何"用户驱动的关于目标的断言"模式的标准基质。下一个测试是 labelers 本身是否会发展信任层级：用户是否会像关注内容创作者一样关注特定的 labeler npubs。

## NIP deep dive：NIP-F4（Podcasts）

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md) 本周合并，距 fiatjaf 打开原始草案（PR #1093）两年三个月。F 前缀是普通的十六进制编号：NIP-F0 到 NIP-FF 使用与 NIP-0A 到 NIP-0D 相同的 1 字节十六进制空间，上部十六进制范围作为 01–99 十进制范围填满时的溢出。NIP-F4 定义了播客如何将集数和元数据作为 Nostr 事件发布，同时保留 RSS 作为音频文件本身的补充层。

核心架构选择是每个播客是自己的 Nostr keypair。规范直接开头就说："each podcast is its own Nostr keypair"。这让播客可以将其播客存在与正常的 kind 0 / kind 1 微博客存在结合，让播客随着时间通过密钥交接或 MuSig2 风格的共享签名改变所有权。四个事件 kind 承载发布层：

- **`kind:10154`**：可替换的播客元数据。携带 `title`、`image`、`description`、可选的 `website` 标签，以及可选的 `p` 标签，用 `role` 为 `host`、`cohost` 或 `editor` 标记作者。
- **`kind:10164`**：作者反声明。规范中的示例使用 kind `10064`（这是一个开放待更正的错字），但标题和周围文本将其识别为 `kind:10164`。用户列出他们撰写的播客 pubkey，以便 client 可以针对来自假定作者的等效声明验证 `kind:10154` 中的 `p` 标签。没有这个，播客可能会错误地将任何人标记为主持人。
- **`kind:54`**：由播客 pubkey 直接撰写的集数事件。标签包括 `title`、可选的 `image`、`description` 和一个或多个 `audio` 标签。每个 `audio` 标签是 `["audio", "<audio-url>", "<optional_media_type>"]`。规范指出"更多进一步发现后要指定的重要字段"，合并的形式有意最小化。
- **`kind:10054`**：一个 [NIP-51](/zh/topics/nip-51/) 风格的收藏播客列表，让用户可以标记他们关注哪些播客。

合并周围的线程辩论涉及 Podcasting 2.0 联合作者 [Dave Jones](https://github.com/daveajones)、[Alex Gleason](https://github.com/alexgleason)、[Mike Terenzio](https://github.com/mterenzio)、[Pablo F7z](https://github.com/pablof7z) 和 [staab](https://github.com/staab)。Jones 强烈反对任何取代 RSS 的尝试："It's been tried many times and always fails"，引用了 JSONfeed、XMPP、AMP、Twitter 的 API 以及 Spotify 失败的迁移。Terenzio 将该提议重新框架为 RSS 之上的社交层，将 RSS 本身保留为分发层。fiatjaf 同意退后一步让提议成熟："I agree with everything you said but I still think we can pull it off, let's stop here for a while"。两年后，合并的规范落在更接近共存而不是替代的位置。

合并规范中三个设计问题保持明确：

- `kind:10164` 错字（示例显示 `10064`）需要在 client 可以安全互操作之前调和。
- 没有 RSS GUID 链接的集数级发现留待开放。合并的规范没有 `i` 标签、没有 `podcast:item:guid` 格式、没有 RSS 桥接机制。想要将现有 RSS 目录桥接到 kind 54 事件的 client 必须自己定义桥接约定。
- `kind:54` 定义上的"更多重要字段"存根将比特率、时长、语言、转录指针、章节和每段元数据留作后续提案的开放领域。

Amethyst 的 [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) 在合并后的几天内落地了一个带有集数列表和内联播放器的专用播客屏幕，是第一个主要的 client 实现。Jumble 在其 GIF 选择器旁发布了早期播客附件脚手架。Wavlake 仍然是最大的 Nostr 原生播客平台，需要决定是否将其现有的 kind 31337 音乐曲目事件与 NIP-F4 的 kind 54 集数模型对齐。

匹配合并规范最小标签集的 NIP-F4 kind 54 集数事件示例：

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093 打开了 27 个月，远高于已合并 NIPs PR 的中位数打开时间。NIP-F4 的下一个测试是 kind 10164 错字是否得到调和，集数发现和 RSS 桥接约定是否从实现者中出现，以及主要播客主持人是否按规范建议以每播客 keypair 发布。
