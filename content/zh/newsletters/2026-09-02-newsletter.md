---
title: "Nostr Compass #38"
date: 2026-09-02
publishDate: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
description: "Voca 1.0 为离线文本转语音应用带来经过验证的 Nostr 阅读，nostream 扩展 relay 端任务路由与身份认证，Napstr 发布基于 Tor 的音频目录，MDK 0.9.17 降低群组维护成本，核心 NIPs 合并分页提示与高亮 tag，NWC 则加入交易总数，本期 NIP 深入解析介绍转发与回应。"
---

欢迎回到 [Nostr Compass](https://nostrcompass.org)，您的 Nostr 每周指南。

**本周：** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 把经过验证的 Nostr 笔记与长文订阅带到一款能朗读文章的离线 Android 阅读器中，[nostream](https://github.com/cameri/nostream) 扩展 relay 端任务路由与认证操作，[NDK for Dart](https://github.com/relaystr/ndk) 修复 negentropy 与多 relay 请求的生命周期，[Divine Mobile](https://github.com/divinevideo/divine-mobile) 让封装消息的删除与签名具有确定性，[Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) 默认保护 gift wrap 收件箱，[Amethyst](https://github.com/vitorpamplona/amethyst) 发布可移植高亮功能，[Mostro](https://github.com/MostroP2P/mostro) 则在垃圾信息关卡之前验证已签名订单。[Napstr](https://github.com/lnbits/napstr) 通过 Nostr 发布音频目录与做种者心跳，同时经由 Tor 传输文件。版本发布涵盖 [MDK](https://github.com/marmot-protocol/mdk) 与 [pakstr](https://git.nostrdev.com/stuff/pakstr)；协议工作在 [NIPs 仓库](https://github.com/nostr-protocol/nips)中合并了 [NIP-67](/zh/topics/nip-67/) 分页提示与 [NIP-84](/zh/topics/nip-84/) 高亮 tag 方案，同时 [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) 增加交易总数；本期 NIP 深入解析沿着各种 event 形态与当前实现追踪转发和回应。
## 头条新闻

### Voca 1.0 在 Android 上朗读经过验证的 Nostr 笔记与订阅

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 是一款离线 Android 阅读器，使用手机自身的文本转语音声音朗读文章、PDF、Markdown 文件与 Nostr 笔记，同时在页面上持续高亮当前朗读的句子。它的 [1.0 版本](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)于 [2026-08-27 发布](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)，并由自身的[项目密钥](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu)签署，使 Nostr 成为一等内容来源：粘贴笔记地址、event 标识符、npub、个人资料，或内部含有 Nostr 实体的普通 web 链接，应用就会解码该引用，从 relays 获取已签名 event，并朗读作者的文字，而不是围绕它构建的网页。

两项经过验证的行为定义了这套 Nostr 集成，两者都在 [Voca 已签名的 1.0 公告](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)中有所描述。第一，每个获取到的 event 都会先以重新计算的 id 与 BIP-340 Schnorr 签名进行校验，然后才持久化；查找时使用引导 relays、作者的 [NIP-65](/zh/topics/nip-65/) relay 列表（一个已签名、可替换的 kind `10002` event，作者在其中列出读写所用的 relays），以及引用本身携带的提示，因此 relay 可以拒绝回答，却不能冒充作者发言。第二，加入作者的 npub，会把其 [NIP-23](/zh/topics/nip-23/) 长文文章（带标题、摘要与图片的可寻址 kind `30023` 帖子）放入设备上的统一收件箱，与 RSS 和 Atom 信息源并列。1.1.0 更新于 [2026-08-28 公告](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca)，并于 2026-08-29 发布到 [Zapstore](https://zapstore.dev)，它让逐句滚动与时间同步，使长文档的滚动更流畅，并在手动滚动、调整大小、进程重启与升级之后恢复主屏幕小组件。


### nostream 扩展 relay 端 DVM 路由与认证操作

继 [8 月 19 日的任务摄取工作](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes)之后，TypeScript relay 实现 [nostream](https://github.com/cameri/nostream) 开始[存储并提供 NIP-89 应用处理器 events](https://github.com/cameri/nostream/pull/737)。[NIP-89](/zh/topics/nip-89/)（应用处理器发现）使用 kind `31989` 推荐与 kind `31990` 处理器信息，两者本来就处于参数化可替换范围，因此客户端可以查询这些 kinds，并在 `d` tag 冲突时收到替代项。relay 不会为自身 worker 发布处理器信息。

待处理的 [NIP-90](/zh/topics/nip-90/)（数据售卖机）任务现在会[送达 worker 进程，并以结果 events 返回](https://github.com/cameri/nostream/pull/734)。成功时，relay 使用自身密钥签署一个 kind 6000-6999 结果。超时或 worker 崩溃会把任务标为失败，而不是让它一直停留在已提交状态。

认证会话与管理员 HTTP 调用位于不同边界。[NIP-42](/zh/topics/nip-42/)（客户端向 relays 认证）会[按 socket 跟踪已认证的 pubkey](https://github.com/cameri/nostream/pull/716)，可以要求客户端在发布 events 前先完成 AUTH，并在 [NIP-11](/zh/topics/nip-11/)（relay 信息）文档中公布这项要求；两项控制默认都关闭。另一方面，[管理员 API 路由可以接受 NIP-98 签名的 HTTP 授权](https://github.com/cameri/nostream/pull/730)。[NIP-98](/zh/topics/nip-98/)（使用已签名 events 的 HTTP 认证）在运营者启用并指定允许的 pubkeys 之前保持关闭。

### NDK for Dart 修复 negentropy、多 relay 请求生命周期与签名验证

Nostr 的 Dart 开发工具包 [NDK](https://github.com/relaystr/ndk) 在执行 [NIP-77](/zh/topics/nip-77/)（negentropy 集合协调）时，会在不报错的情况下返回错误的已有集合与所需集合，因为 codec 不支持 [negentropy](/zh/topics/negentropy/) 协议 v1。[v1 编码修复](https://github.com/relaystr/ndk/pull/722)现在会返回 relay 已持有的 ids，以及它仍然需要的 ids。

发往不同 relays 的相同过滤器[此前会合并为一个请求](https://github.com/relaystr/ndk/pull/705)。现在，同一过滤器在目标 relay 不同或生命周期不同时会保持为独立请求，因此短查询不会把另一 relay 的 events 混入结果，也不会让仍有效的 subscription 陷入停滞。

同一套工具包会[验证一次签名并保留结果](https://github.com/relaystr/ndk/pull/726)。之后重复投递时不再花费另一次校验，也不会覆盖已存储且经过验证的 event。

### Divine Mobile 让封装私信的删除与签名具有确定性

针对某条消息的封装 [NIP-09](/zh/topics/nip-09/)（event 删除请求）kind `5` events 此前在通过 Nostr 发布内容的移动短视频客户端 [Divine Mobile](https://github.com/divinevideo/divine-mobile) 中从未生效。客户端[现在会针对被指名的消息解析每次删除](https://github.com/divinevideo/divine-mobile/pull/8174)，而不是把所有非 reaction 内容都当作已经处理。当第一项面向所有人的删除请求仍在传输时发出[第二项请求](https://github.com/divinevideo/divine-mobile/pull/8164)，此前会无错误消失，线上也没有 kind `5`；现在并发删除会各自发布。

在此前报道过的 1.0.22 版本之后，一秒内两次发送相同的 1:1 [NIP-17](/zh/topics/nip-17/)（gift wrap 私信）文本会[构造出同一个 rumor id](https://github.com/divinevideo/divine-mobile/pull/8163)，导致第二次发送消失；现在每次发送都会在 [NIP-59](/zh/topics/nip-59/)（gift wrap）rumor 中携带一个 token，使 ids 各不相同。

调用方已经签署的 kind `4` 或 kind `5` event [现在会保留该签名](https://github.com/divinevideo/divine-mobile/pull/8173)，而不是之后再附加一个客户端 tag，从而改变 id 并使 relays 以无效为由拒绝 event。

### Conduit Relay 加固受 NIP-42 保护的收件箱

Kind `1059` gift wraps 只为一名收件人存储。[Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) 是一个用受收件人保护的收件箱保存这些 wraps 的 Go relay，现在[默认采用强制模式](https://github.com/Conduit-BTC/conduit-relay/pull/8)：kind `1059` 查询必须以该收件人身份提供 [NIP-42](/zh/topics/nip-42/) 认证，否则 relay 会拒绝请求。对这些 wraps 的混合 kind 过滤器、通配符、计数与 [negentropy](/zh/topics/negentropy/) 都被标记为 `restricted`，因此另一份 AUTH 无法把它们变成他人收件箱的完整转储。

同一项[受保护收件箱合并](https://github.com/Conduit-BTC/conduit-relay/pull/8)要求传输的 AUTH event 具有规范 event id，并且无论 `content` 是否为空，都会接受其他方面有效的 NIP-42 event。仅质询模式仍会提供 AUTH 而不阻止读取；禁用模式则自由放行。库的默认值是强制模式。

### Amethyst 发布 NIP-84 高亮，并修复两条面向 relay 的故障路径

继上周的 [Blossom 授权工作](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads)之后，Android Nostr 客户端 [Amethyst](https://github.com/vitorpamplona/amethyst) 发布 [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0)，加入 [NIP-84](/zh/topics/nip-84/)（可移植高亮）。选中的段落可以从撰写器、高亮信息流，或分享进应用的入口变成 kind `9802` event。

该版本加入 [NIP-29](/zh/topics/nip-29/) 频道删除与归档控制（[PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)），并通过客户端原本就会产生的流量测量 relay 行为，随后以流式传输、读取、写入与 URL 检查扩展这些 [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) 探测（[PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836)、[PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)）。Amethyst 还消除了 SharedKeyCache 的哈希冲突漏洞，并以恒定时间比较消息认证码（[PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)），修复一项可能丢失连接时 AUTH 投递的竞态（[PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)），对 subscription 状态锁分片以终止 ANR 拥堵（[PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)），并比较所有 subscription 过滤器，而不是只比较第一个（[PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)）。

[Newsletter #36 此前报道过这些 relay 认证、备份与公开聊天变更](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow)；v1.14.0 现在将它们一并发布。Concord 软封禁弥补了审计发现的权限缺口（[PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)）。relay 认证重新设计了权限流程（[PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)），等待质询完成而不是超时退出（[PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)），让新账户默认认证（[PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)），在账户常用集合之外的 relays 上也遵循该偏好（[PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)），并在重连后保留会话授权（[PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)）。带引导的首次运行与设置流程让密钥备份更容易找到（[PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)），Cashu proof 回填与历史分页避免钱包余额被截断（[PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)），公开聊天现在也可以静音（[PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)）。

在该版本之后，kinds `30392` 至 `30395` 的[可信列表](https://github.com/vitorpamplona/amethyst/pull/3983)仅按标题建立 [NIP-50](/zh/topics/nip-50/)（全文搜索）索引，因此可以通过正文中提到的列表名称找到它，而无需索引成员的十六进制 ids。通过 [NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）抵达的钱包拒绝[现在会显示错误，而不是看起来像点击后毫无反应](https://github.com/vitorpamplona/amethyst/pull/3987)，包括 `QUOTA_EXCEEDED` 与 `RESTRICTED`，以及钱包始终不回答时的超时。

### Mostro 在高成本工作之前验证已签名订单，并保留订单审计 events

继 [v0.18.1 的 Cashu 托管基础](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon)之后，通过 Nostr 协调订单的点对点交易 daemon [Mostro](https://github.com/MostroP2P/mostro) 标记了 [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5)，它默认使用 [NIP-44](/zh/topics/nip-44/)（载荷加密）作为传输方式，并把 gift wrap 保留为显式选择加入的选项。

该版本把等待状态的超时锚定到记录的接单时间，因此 maker 保证金不会按错误的时钟被罚没（[PR #879](https://github.com/MostroP2P/mostro/pull/879)）；每个已结算订单的买方款项最多发送一次（[PR #881](https://github.com/MostroP2P/mostro/pull/881)）；这些付款通过有界、非阻塞的 `send_payment` 等待完成（[PR #883](https://github.com/MostroP2P/mostro/pull/883)）。向超时罚没胜方付款的尝试（[PR #875](https://github.com/MostroP2P/mostro/pull/875)）在同一 tag 发布前被回滚（[PR #885](https://github.com/MostroP2P/mostro/pull/885)）。Mostro 也不再每小时及启动时重新发布未变化的待处理订单簿（[PR #888](https://github.com/MostroP2P/mostro/pull/888)），其 kind `38386` 争议 events 现在携带 `created_at` tag，以供下游排序（[PR #878](https://github.com/MostroP2P/mostro/pull/878)）。

该 tag 之后，[签名检查现在会在垃圾信息关卡之前运行](https://github.com/MostroP2P/mostro/pull/892)。event id 并不承诺 `sig`，因此带损坏签名的受害者 kind `14` 副本可能占用重放槽位，并悄然丢弃有效消息；daemon 现在会先验证，并直接丢弃无效 wrap，而不是警告后继续。

Kind `8383` 的费用审计 events 此前携带 15 天的 [NIP-40](/zh/topics/nip-40/)（过期时间戳）。现在它们[保留一年的有效期](https://github.com/MostroP2P/mostro/pull/924)，与其作为公开支付记录的角色一致。在启用 Cashu 的节点上，接单会[通过 Nostr 要求卖方锁定一项 2-of-3 托管](https://github.com/MostroP2P/mostro/pull/830)，发布等待中的订单 event，并跳过创建 Lightning hold invoice。这完成了请求路径；它本身并未解决所有托管或市场滥用情形。

### Napstr 在 Nostr 上发布音频目录，并通过 Tor 传输文件

[Napstr](https://github.com/lnbits/napstr) 是一款桌面音频共享客户端，它在 Nostr 上发布可搜索目录与在线做种者，然后通过内置 Tor 进程传输文件，不提供直连 IP 回退。[版本 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) 让个人资料与目录元数据保持公开，同时不把请求、传输凭据、文件内容与对端 IP 地址放到 relays 上。

发现使用 [Napstr 仓库](https://github.com/lnbits/napstr)中两种可寻址 event kinds。Kind `30421` 目录条目以 SHA-256 摘要、公开基本文件名、大小和音频格式指名文件，作者通过把该坐标替换为已删除标记来撤下文件。Kind `30422` 可用性心跳在十分钟后过期，并列出作者准备做种的文件 IDs，因此只有在未过期的心跳仍包含该摘要时，目录行才处于在线状态。

公开对话使用 [NIP-C7](/zh/topics/nip-c7/)（kind 9 聊天消息），而不是 relay 自有群组。[Napstr 仓库](https://github.com/lnbits/napstr)定义了一个共享公开房间，以及按文件摘要划分的单曲讨论。这些消息已签名且公开，但不携带 onion 地址、传输凭据或文件字节。

下载以 [NIP-17](/zh/topics/nip-17/)（gift wrap 私信）协商开始。[Napstr 仓库](https://github.com/lnbits/napstr)把请求、报价或拒绝封装在 kind `14` rumor 内，因此 relays 看不到临时 v3 onion 主机名，也看不到被接受报价返回的一次性 capability。随后，内置 Tor 通过该 onion 传输字节，验证完整 SHA-256 摘要，并在文件可播放之前重新验证音频。

[v0.1.7 至 v0.2.0 的比较](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0)加入有声书合集与可选 Android 配套应用 Napstrfy。Kind `30423` manifests 列出有顺序的章节，这些章节仍是普通目录文件，因此忽略合集的客户端依然可以获取每一章。Napstr 为此创建一个非破坏性的本地 Audiobooks 文件夹。Napstrfy 通过一次性二维码与运行中的桌面端配对，随后利用桌面端现有的 Nostr 与 Tor 服务搜索和请求下载，而不会收到桌面端私钥。

同一项[比较](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0)会让未完成的配套握手超时。做种者在提供字节前复制共享文件并计算哈希，把传入数据写入私有临时文件，把有声书目标限制在 Napstr 文件夹的真实子目录内，并在传输期间目标发生变化时中止。

## 版本发布

### MDK v0.9.17：最新 KeyPackages、成员活动与持久发送

[Newsletter #37 报道过 MDK 0.9.14 与 0.9.15](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles)，包括 [MDK 仓库](https://github.com/marmot-protocol/mdk)从优先选择最旧 KeyPackage 改为选择最新且符合当前配置的有效包、epoch 间隙恢复关卡、账户清理，以及发现 relays 与操作 relays 之间的拆分。这些修复仍是后续两个版本的基础，因此旧包不会再阻止已经发布可用包的成员。

[成员与管理员 events 现在会像新消息一样推动聊天列表](https://github.com/marmot-protocol/mdk/pull/1551)：人员加入、离开或改变角色时，预览文本、排序、未读计数与已读标记都会更新，本地系统 actor 不会被当成 Nostr 个人资料。重连与重启会[为重试的持久传出文本复用同一个发送标识](https://github.com/marmot-protocol/mdk/pull/1516)，因此同一条群组消息不会发布两次。

此后的两个版本专注于维持大型群组健康运行的成本。[版本 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [从当前 epoch 而不是最高水位衡量 epoch 分歧](https://github.com/marmot-protocol/mdk/pull/1559)，让被拒绝的传入 events 仍可获取（[PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)），把重放回滚限定到规范群组状态（[PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)），并引入 [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545)：一个在 UniFFI bindings 之上的宏生成 C ABI，使宿主可以直接嵌入引擎。[版本 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) 随后把通行准入扫描合并为[一次成员遍历，而不是每名成员一次](https://github.com/marmot-protocol/mdk/pull/1617)，[无需填充完整历史图就能探测群组状态是否存在争议](https://github.com/marmot-protocol/mdk/pull/1620)，[降低延迟 peel 扫描的空闲轮询成本](https://github.com/marmot-protocol/mdk/pull/1621)，并[把批量组件读取应用到第一轮遗漏的三个投影位置](https://github.com/marmot-protocol/mdk/pull/1622)。配套的 [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) 与 [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) 工件由同一个 commit 构建，因此嵌入方可以一并获得成本更低的维护路径。


### pakstr v0.16.0：发布时记录 kind-32267 标识符

继[上周 0.13.0 至 0.15.0 的 Zapstore 发布流水线](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit)之后，[pakstr](https://git.nostrdev.com/stuff/pakstr) 这个把 web 应用打包成已签名 Android APK、并使用 Nostr 密钥发布的 CLI，开始[记录它查找、发布或替换的 kind `32267` 应用 event IDs](https://git.nostrdev.com/stuff/pakstr/pulls/67)。[版本 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) 会在过期上架元数据触发重新发布时，同时打印旧 ID 与新 ID，让发布者可以确认 relay 上当前有效的是哪一条上架 event。

同一项[标识符日志](https://git.nostrdev.com/stuff/pakstr/pulls/67)会先记录替换前查找到的 ID，再记录最终落地 event 的 ID，因此无操作复用会显示为重复 ID。这是 [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) 中带 tag 的变更；Content-Digest、先发布后上传，以及发布者验证行为已经在较早的 tags 中发布。

## 未发布的变更

### Zap Cooking 限定 bunker relays 并签署付费端点

在基于 Nostr 长文 events 的食谱网站 [Zap Cooking](https://github.com/zapcooking/frontend) 上重新加载 bunker 会话，过去会把加密的 [NIP-46](/zh/topics/nip-46/)（通过 relays 远程签名）对话发布到页面已经使用的每个 relay。[把签名器流量限定到 bunker 自身的 relays](https://github.com/zapcooking/frontend/pull/633)现在会在恢复会话与 nostrconnect 配对时应用这项限制；后者是签名器发起的连接流程，与 bunker URL 登录路径一致。它会拒绝从格式错误的存储记录中安装空 relay 集合，因此只托管食谱的 relays 不再得知同一个 pubkey 仍维持着活跃的 bunker 会话。

[已签名 HTTP 认证](https://github.com/zapcooking/frontend/pull/630)现在依据 [NIP-98](/zh/topics/nip-98/)（使用已签名 Nostr event 的 HTTP 认证）保护付费烹饪助手聊天、食谱集简介与受限食谱更新。服务器只读取一次请求正文，对该确切载荷验证签名，并从经过验证的 auth event 获取身份，而不是使用正文提供的公钥。聊天预览在没有 header 时仍可使用；如果提供的签名无效，则会被拒绝；食谱集简介始终需要签名。更新受限食谱现在还要求经过验证的密钥与已存作者匹配；其他人会被告知食谱不存在，因此端点不会确认哪些付费记录存在。

### nostrord 修复封装私信与共享 event 链接

继上周的 [v2.9.0](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media)之后，面向 relay 托管社区的跨平台客户端 [nostrord](https://github.com/nostrord/nostrord) 合并了投递修复，使一台设备发出的 [NIP-17](/zh/topics/nip-17/)（gift wrap 私信）能够抵达同一账户的其他设备。[独立发布发送者自己的副本](https://github.com/nostrord/nostrord/pull/295)，可以阻止收件人 wrap 首次被 relay 接受时丢掉供其他设备获取的副本。同一项变更会在 [NIP-42](/zh/topics/nip-42/)（客户端向 relays 认证）完成后重新发送 wrap，并在第一个 relay 接受时把发送标为成功，因此一台故障主机不会阻塞其余主机。[重试停放的 gift wraps](https://github.com/nostrord/nostrord/pull/297)会定时处理 [NIP-59](/zh/topics/nip-59/)（gift wrap）解密失败，因此持续连接的 bunker 不会再让这些消息下落不明……[已截断]

[NIP-C7](/zh/topics/nip-c7/)（kind `9` 聊天消息）回复会在 `q` tag 旁边，以开头的 [NIP-19](/zh/topics/nip-19/)（bech32 编码实体）`nevent` 指针再次指向其父项。当该指针位于正文开头并指名回复父项时，[去掉这个开头的父项指针](https://github.com/nostrord/nostrord/pull/292)，可以让该行渲染为单个回复引用；正文中部的指针或占据整个正文的指针仍会渲染为引用卡片。[引用 event 链接现在会编码 `nevent`](https://github.com/nostrord/nostrord/pull/293)，其中包含作者、kind，以及读取引用的 relay，因此分享到私信中的 [NIP-29](/zh/topics/nip-29/)（relay 托管群组）event 可以由另一个客户端获取，而不是使用不带查找提示的裸笔记标识符。

## NIP 更新与协议规范工作

### Nostr Implementation Possibilities

本周，核心 [NIPs 仓库](https://github.com/nostr-protocol/nips)合并了两项规范变更。

[NIP-67](/zh/topics/nip-67/) 定义了 relay 可以附加到 `EOSE`（已存 events 结束）消息的提示，让客户端知道是否应继续分页。[已合并的 `"auth"` 提示](https://github.com/nostr-protocol/nips/pull/2371)在 `finish` 与 `more` 旁加入第三个值：relay 现在可以表示用户完成认证后可能看到更多已存 events，并且必须在携带该提示的 `EOSE` 之前发送 [NIP-42](/zh/topics/nip-42/)（relay 认证）`AUTH` 质询。[配套的 NIP-42 补充](https://github.com/nostr-protocol/nips/pull/2371)从客户端一侧定义了同一流程，因此客户端收到带 `auth` 的 `EOSE` 时，已经持有作答所需的质询。

[NIP-84](/zh/topics/nip-84/)（可移植高亮，即上文 Amethyst 已发布支持的 kind `9802` events）[合并了一项 tag 方案更新](https://github.com/nostr-protocol/nips/pull/2454)：高亮现在除了可以用 `a`/`e` tags 标记 Nostr events、用 `r` tags 标记其他来源，还可以依据 [NIP-73](/zh/topics/nip-73/)（外部内容标识符）使用结构化 `i` tags 标记来源；在渲染方式上，引用高亮也从 MUST 改为 SHOULD，与引用转发一致。

### Nostr Wallet Connect

`list_transactions` 响应可以报告匹配请求的交易数量，而不是当前页面返回的行数。[NWC 扩展仓库](https://github.com/nostr-wallet-connect/nwc)中 NWC-05（钱包历史扩展）[已合并的可选 `total_count`](https://github.com/nostr-wallet-connect/nwc/pull/4)，为配合 [NIP-47](/zh/topics/nip-47/)（通过 Nostr 加密远程控制钱包）使用的响应加入了该字段。

[加入 `total_count` 的 commit](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67)将它记录为可选整数：匹配请求过滤器的交易总数。

[从计数中排除分页的 commit](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e)说明该总数不受分页影响，因此会计算所有页面上的全部匹配交易。

## NIP 深入解析：转发与回应

联系人可以把现有笔记重新放到关注者面前，也可以附上简短的喜欢、不喜欢或表情，而无需撰写回复。[NIP-18](/zh/topics/nip-18/)（转发）把这种再分发发布为独立的已签名 event。[NIP-25](/zh/topics/nip-25/)（回应）把简短反馈发布为另一个已签名 event。两者在[规范转发规范](https://github.com/nostr-protocol/nips/blob/master/18.md)与[规范回应规范](https://github.com/nostr-protocol/nips/blob/master/25.md)中仍是 `draft` `optional` 文件：它们存在于 NIPs 仓库中，并已被客户端实现，但仍标为非最终版本。

### 转发（NIP-18）

当客户端写入 kind 6 event 时，关注者会收到一个已签名指针，指向他人已经发布的 kind 1 文本笔记。[转发规范](https://github.com/nostr-protocol/nips/blob/master/18.md)把 `kind` 设为 6，将该笔记字符串化后的 JSON 放进 `content`（允许但不建议使用空 `content`），要求一个 `e` tag，其值为笔记的 `id`，第三项则是可获取该笔记的 relay URL，并规定 event 还应该（SHOULD）携带一个带原作者 `pubkey` 的 `p` tag。转发 [NIP-70](/zh/topics/nip-70/)（受保护 events）event 时，应该（SHOULD）让 `content` 保持为空，以免受保护载荷被复制到新 event 中。

引用是某个其他 event 内部的引文，而不是 kind 6 wrapper。当客户端提到 [NIP-21](/zh/topics/nip-21/)（`nostr:` URI）的 `nevent`、`note` 或 `naddr` 时，必须把该提及转换成形式为 `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]` 的 `q` tag。[引用转发 tags](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts)让这些引文不进入回复串，并使客户端能够提取和统计帖子的引用。

Kind 6 保留给 kind 1 笔记。Kind 16 通用转发可以封装 kind 1 以外任意 event kind。它应该（SHOULD）包含一个 `k` tag，其值为内部 event 的字符串化 kind。当内部 event 可替换时，通用转发应该（SHOULD）加入一个带 `kind:pubkey:d-tag` 坐标的 `a` tag；如果缺少该 `a` tag，转发就以某个特定版本为目标，`content` 必须包含该版本完整的 JSON 字符串。[通用转发规则](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts)避免把长文、可寻址及其他非笔记 events 当成 kind 1 发布。

下面的 kind 6 event 是编写时从 `wss://relay.damus.io` 恢复的真实转发（[打开 event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)）：

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

它的 `kind` 是 6，`e` tag 指向被转发的笔记，`p` tag 标识该笔记的作者，`content` 则携带字符串化 JSON 形式的原始 kind 1 event。这个从 relay 恢复的 event 省略了 [NIP-18 规范](https://github.com/nostr-protocol/nips/blob/master/18.md)标为必需的 relay 提示，说明了为什么阅读器与客户端必须验证真实 events，并容许生产方遗漏字段。

### 回应（NIP-25）

帖子可以收集已签名的喜欢、不喜欢与表情，而不让这些标记进入回复串。[回应规范](https://github.com/nostr-protocol/nips/blob/master/25.md)把这种标记定义为 kind 7 event，其 `content` 必须（MUST）携带回应值。`+` 或空字符串必须（MUST）解读为喜欢或赞成。`-` 必须（MUST）解读为不喜欢或反对。表情或 [NIP-30](/zh/topics/nip-30/)（自定义表情）短代码不应该（SHOULD NOT）解读为喜欢或不喜欢，客户端可以（MAY）在帖子上显示该表情。

目标位于 tags 中，不能从 `content` 推断。必须（MUST）有一个 `e` tag 设为目标 event `id`，该 tag 应该（SHOULD）包含 relay 提示；不建议使用额外的 `e` tags，如果出现，目标 `id` 必须位于最后。应该（SHOULD）有一个指向目标作者的 `p` tag；若出现多个 `p` tags，它应位于最后。可寻址目标还应该（SHOULD）得到一个带 `kind:pubkey:d-tag` 坐标的 `a` tag。`e` 与 `a` tags 应该（SHOULD）包含 relay 与 pubkey 提示，`p` tags 应该（SHOULD）包含 relay 提示，`k` tag 则可以（MAY）携带被回应 event 的字符串化 kind。[这些 tag 规则](https://github.com/nostr-protocol/nips/blob/master/25.md#tags)让客户端仅凭回应 event 就能获取目标并通知其作者。

客户端可以（MAY）在 `content` 中放入单个 `:shortcode:`，再用一个 `emoji` tag 将该短代码映射到图片 URL，遵循[自定义表情回应规则](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction)。如果目标不是原生 Nostr event，该回应必须（MUST）是 kind 17，并且必须（MUST）携带 [NIP-73](/zh/topics/nip-73/)（外部内容 IDs）的 `k` 与 `i` tags，如[外部内容回应规则](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions)所示。Kind 17 是对网站、播客单集或其他外部对象的回应。它不是 kind 7 event 到 event 的回应，也不是转发。

下面的 kind 7 event 是编写时从 `wss://relay.damus.io` 恢复的真实回应（[打开 event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)）：

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

它的 `content` 是 `+`，即 [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md) 中约定的喜欢。`e` tag 指名被回应的 event；`a` tag 加入其可寻址坐标；`p` tag 标识其作者；可选的 `k` tag 则以字符串记录目标的 kind。

### 当前客户端实现

Android Nostr 客户端 [Amethyst](https://github.com/vitorpamplona/amethyst) 在当前协议层中定义了[转发 event 类型](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt)与[回应 event 类型](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt)。

Web Nostr 客户端 [Snort](https://github.com/v0l/snort) 实现了[包含引用链接 tag 处理的 NIP-18 辅助函数](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts)，并[创建 NIP-25 event 回应 tags](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts)。

同时充当 Mastodon 服务器与 Nostr relay 的 [Ditto](https://github.com/soapbox-pub/ditto)，会[发布带 `k` tag 的 kind 16 通用转发，并在可寻址目标上加入 `a` 坐标](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx)，还会[把最后一个 `e` tag 视为目标 event，以应用 kind 7 回应语义](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts)。

### 它们如何协同工作

Kind 6 或 kind 16 event 会把现有 event 重新分发到转发者关注者的信息流中，方式可以是嵌入该 event 的 JSON，也可以是指向可替换坐标。`q` tag 标记某个其他 event 内部的引用，让线程重建可以统计引文而不把引用 event 视为回复，这正是[引用转发部分](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts)所做的区分。Kind 7 event 保持原 event 不动，只附加回应值与目标 tags，这就是[回应规范](https://github.com/nostr-protocol/nips/blob/master/25.md)中的约定。因此，获取某个 pubkey 的客户端会把该 pubkey 的转发视为新的 kind 6 或 16 events，并把其观点视为附在他人帖子上的 kind 7 events。

---

发送 NIP-17 私信，通过 [Nostr Compass 项目](https://github.com/andotherstuff/nostr-compass)分享项目或新闻。
