---
title: "Nostr Compass 第46期"
date: 2026-10-28
publishDate: 2026-10-28
translationOf: /en/newsletters/2026-10-28-newsletter.md
translationDate: 2026-10-28
draft: false
type: newsletters
description: "Mostro 新增签名身份重新绑定，Amethyst 1.20.0 带来私密 Marmot 群组投票和加密设置同步，swift-nostr 0.9.0 发布，我们还将回顾 Nostr 的六个十月。"
---

本周：**Mostro** 新增[签名身份重新绑定](https://github.com/MostroP2P/mostro/pull/1035)。**Amethyst** 为 Marmot 群组带来[私密投票](https://github.com/vitorpamplona/amethyst/pull/4630)，并支持跨设备的[加密设置同步](https://github.com/vitorpamplona/amethyst/pull/4613)。**swift-nostr** 发布了一项[检查，如果 event 的公钥与签名者的公钥不匹配，就拒绝签名](https://github.com/yysskk/swift-nostr/pull/239)。本期最后是专题《Nostr 的六个十月：2021–2026》。

## 头条新闻 {#top-stories}

[commands-review]: https://github.com/nostr-protocol/nips/pull/2462 "Proposed previously, now merged"
[marmot-devices-review]: https://github.com/marmot-protocol/marmot/pull/442 "Proposed previously, now merged"
[cd-installed-merge]: https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157

### Mostro {#mostro}

[Mostro](https://github.com/MostroP2P/mostro) 是一个通过 Nostr 协调的点对点交易守护进程，现已[发布 0.20.1](https://github.com/MostroP2P/mostro/releases/tag/v0.20.1)。该版本新增[签名身份重新绑定](https://github.com/MostroP2P/mostro/pull/1035)，[上周一期](/en/newsletters/2026-10-21-newsletter/#mostro)曾说明这一功能尚未实现；此前只存在于源代码中的信誉导出功能也随本版本发布。已绑定的身份会签署一份一次性授权，写明节点和新身份，有效期最长一小时。守护进程会记录该 event ID，并通过比较并交换（compare-and-swap）完成切换，所以无论是签名失败还是竞争失败，都不会改动任何状态。运营者另有一个经过审计、仅限回环地址的 RPC，调用时需要提供认证令牌和理由。已经签发的证明不会因为重新绑定而被撤销。

之后合并的变更是否已包含在某个发布版本中，目前尚未确认。一个[需主动启用的固定美元锚定提供方](https://github.com/MostroP2P/mostro/pull/1083)只有在运营者启用时，才会把 USDT、USDC 和 DOC 加入 Nostr `mostro-rates` 数据源。网络提供方和经转发的币种报价都不会隐式开启它。[一项后续变更](https://github.com/MostroP2P/mostro/pull/1091)把该提供方及其配置键重命名为 `pegged`，取代尚未发布的 `stablecoins` 键。它还按固定 1:1 以 sats 报出 BTC、LBTC 和 RBTC 的价格，并将汇率作为 kind 30078 event 发布。这些锚定假设只是配置值，锚定本身和结算都得不到保证。实时锚定检查不属于这一机制。该提供方默认关闭。订单仍受已接受币种的限制；客户端、协议订单簿和锚定防护方面的工作另行开展。[保证金时间锁现在与托管分开运行](https://github.com/MostroP2P/mostro/pull/1085)。对外公布的订单到期时间会受到上限约束，订单簿上的接单窗口也会在保证金可能到期之前关闭。现有的 144 个区块挂单方保证金会在升级时到期，相关订单必须重新创建。进行中的交易和 Cashu 模式不受影响，不过某些运营者配置在保证金时间锁调整之前会拒绝启动。

### Nostr WoT extension {#nostr-wot-extension}

[Nostr WoT extension](https://github.com/nostr-wot/nostr-wot-extension) 是一款带有信任网络（web-of-trust）功能的浏览器签名器。它发布了 [0.8.15](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.15)，新增一个选项：用户可以用自己掷骰子或抛硬币得到的 256 位熵来创建恢复密钥。骰子结果经 SHA-256 哈希，硬币结果则直接作为原始比特使用；整个过程在一个不显示恢复短语的隔离标签页中完成。relay 无法访问时，引导流程现在会超时。[0.8.16 版](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.16)为 [relay 认证（NIP-42）](/zh/topics/nip-42/)加入了长期授权，用户可以一次性为某个站点上的所有 relay 批准 AUTH，也可以为所有已连接站点批准（[relay 认证实现](https://github.com/nostr-wot/nostr-wot-extension/pull/47)）。对 relay 或站点的拒绝设置优先于这些授权，排队中的请求在得到处理之前也会重新检查是否已被撤销。宽泛的授权范围一律需要用户明确选择，并且永远不适用于 [HTTP Auth（NIP-98）](/zh/topics/nip-98/)。队列上限仍为五个，超出的请求依旧会失败并重试。到了 [0.8.18 版](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.18)，导入和恢复合并成了一个流程，能够识别密钥格式并预览身份；兼容的 Nosskey 恢复会保留同一身份、现有账户和原有 passkey。

独立的开发者 SDK [nostr-wot-sdk](https://github.com/nostr-wot/nostr-wot-sdk) 发布了 [3.0.1](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%403.0.1)，提供稳定的 identity 1.1 支持。Passkey 恢复（包括经由 Nosskey 的恢复）会保留原来的 pubkey，提供方、恢复和签名代码如今共用一套实现（[SDK 恢复与提供方源代码](https://github.com/nostr-wot/nostr-wot-sdk/pull/22)）。已弃用的转发包仍然可用，但集成方应迁移到仍在维护的入口点。

### Amethyst {#amethyst}

Android 和桌面端 Nostr 客户端 [Amethyst](https://github.com/vitorpamplona/amethyst) 发布了 [1.20.0 版](https://github.com/vitorpamplona/amethyst/releases/tag/v1.20.0)，带来[私密投票及其他 Marmot 加密群组功能](https://github.com/vitorpamplona/amethyst/pull/4630)。具体包括可替换的私密选票、自定义加密表情、管理员删除消息与举报，以及固定到群组当前 epoch 的媒体。审查之后，作者没有重新运行跨客户端互操作性检查，也没有在 Android 上手动测试这项变更。共享同一 epoch 编号的竞争分支之间的缓存键问题依然存在，加密媒体密钥的留存时间也可能长于阅后即焚消息。[设置同步](https://github.com/vitorpamplona/amethyst/pull/4613)会把六组应用设置存为加密的 [NIP-78](/zh/topics/nip-78/) 数据。密钥、签名器、钱包、通知、栏目（decks）和已读标记则留在各自的设备上。第一次编辑设置时，全部六组都会被发布。只读账户的设置只保存在本地；在两台签名设备之间会有怎样的表现，目前尚未验证。

桌面系统通知现在[遵循通知筛选器](https://github.com/vitorpamplona/amethyst/pull/4650)，并跳过一次性的外层 gift wrap 和已静音的私信。[超过 255 字节的不可信 `d` tag](https://github.com/vitorpamplona/amethyst/pull/4616) 不会再引发错误。[kind 查找](https://github.com/vitorpamplona/amethyst/pull/4600)只查询已连接的 relay 和账户搜索 relay，每个 relay 最多返回 200 个 event。处理帧、event、过滤器以及 [NIP-46](/zh/topics/nip-46/) 和 [NIP-55](/zh/topics/nip-55/) 消息时，这些应用[改用 Quartz 的 Kite JSON 处理](https://github.com/vitorpamplona/amethyst/pull/4595)，不过经由这两个协议的签名尚未在设备上验证。随后的一次[库拆分](https://github.com/vitorpamplona/amethyst/pull/4654)把其他客户端同样需要的 Marmot 和 cordn 协议规则移进了共享库。

1.20.0 之后合并、尚未进入任何发布版本的源代码，[让应用的 Marmot 接收路径运行在共享库之上](https://github.com/vitorpamplona/amethyst/pull/4672)。每条解密后的消息都会以幂等方式持久化。加入群组时会记录一个基线，这样第一次成员变更就能显示对应的条目。如果 kind 445 消息先于其 commit 到达，它会被暂存，稍后再重放；管理员进行追赶同步时，会提交已暂存的成员离开操作。`amy cordn migrate export` 会停用旧安装的会话命令，直到完成导入或执行新的 resume 命令为止。作者针对本地检出的代码运行了回环 amy 测试和库测试，但没有手动验证实际运行中应用的接收路径，也没有运行 Marmot 互操作测试套件。拟议中的 [NIP-5D napplet 格式](/zh/topics/nip-5d/)迎来一项[破坏性更新](https://github.com/vitorpamplona/amethyst/pull/4659)：napplet 清单哈希改为按单个 `/index.html` 制品读取，取代旧的路径聚合方式，因此旧版包需要重新发布。必需的 NAP 域不可用时按失败关闭（fail closed）处理，可选的则保持缺失。图标要经过哈希和解码器检查，存储按清单 kind、制品和快照分区，资源 blob 使用规范 base64。手动设备测试、跨客户端测试和实际 relay 发布都未进行。

在外部签名器中[拒绝请求](https://github.com/vitorpamplona/amethyst/pull/4669)的情况，现在在原本缺少防护的各个协程中都得到了处理，不会再导致应用崩溃。[PressStr 电子书、杂志及各期杂志](https://github.com/vitorpamplona/amethyst/pull/4662)（kind 33953、34609 和 39731）现在可以渲染。PDF 在应用内阅读器中打开，EPUB 则交给系统处理程序。卡片会显示文件类型和大小，绝不会只为预览就下载大型 PDF，各期内容也只从杂志作者处获取。作者没有报告针对这项变更做过 Android 设备测试。关闭富预览时，[发票和 LNURL 会显示为紧凑的可复制标签](https://github.com/vitorpamplona/amethyst/pull/4663)，不带支付按钮；发票卡片现在还会显示到期时间。`amy gift wrap` [现在会为 seal 和 wrap 分别设定各自独立的随机时间](https://github.com/vitorpamplona/amethyst/pull/4661)，每个最多往前回溯两天。`--no-backdate` 可以关闭这一行为。常规私信路径的修复则在 Quartz 中单独进行。在桌面端，[每个视频卡片各自掌管自己的播放](https://github.com/vitorpamplona/amethyst/pull/4660)，URL 相同的卡片因此不会再互相抢占对方的视频。作者在 macOS 上测试过，但没有在冷缓存状态下测试。一项[拟议的 Windows 链接修复](https://github.com/vitorpamplona/amethyst/pull/4666)会通过完整路径调用 rundll32 打开链接，失败时回退到 AWT。根本原因尚未复现，所以这只是一个可能有效的修复，并未得到确认。

### Myco 新增加密 napplet 存储和签名更新通知 {#myco-adds-encrypted-napplet-storage-and-signed-update-notices}

Myco 是一款运行 Nostr napplet 的 Android 宿主应用，发布了 0.12.0 和 [0.12.1](https://github.com/Origami74/myco/releases/tag/v0.12.1)。napplet 现在可以通过运行时存储 [NIP-44](/zh/topics/nip-44/) [自加密数据](https://github.com/Origami74/myco/pull/152)，但持有 relay、outbox 或 mesh 读取授权的应用能够看到明文，因此这些数据并没有按应用隔离。此前通过 Amber 登录的用户必须重新登录，才能授予新的加密和解密权限。更新通知由一个固定（pinned）的发布者签名，而且只会到达已经运行 0.12 的设备。联网时，Myco 可以每天检查 Zapstore，也可以检查 Circle；纯 mesh 模式下则只询问 Circle，取代了[最初的暂停做法](https://github.com/Origami74/myco/pull/151)。如果用户明确选择本地 Blossom 通道，文件会留在设备上，不经过任何服务器，每个应用每天上限 64 MiB。向已批准的默认服务器上传失败时，同样会保留一份本地副本。这两条路径都不会剥离 EXIF 元数据。这些版本还加入了 Android TV 支持，以及一个由用户自行挑选文件的 NAPFS 文件选择器。

## 已打标签的版本 {#tagged-releases}

### Monostr {#monostr}

Android Nostr 社交客户端 [Monostr](https://github.com/schmidt1024/monostr) 发布了其最新版本 [0.26.0](https://github.com/schmidt1024/monostr/releases/tag/v0.26.0)。时长不超过两分钟的视频现在会在设备上压缩，位置元数据也会被移除。发现、搜索和引导流程都提供精选关注列表。帖子串和通知中现在会显示以 [NIP-22](/zh/topics/nip-22/) 评论形式发送的 Fediverse 回复。

[0.25.0](https://github.com/schmidt1024/monostr/releases/tag/v0.25.0) 引入的功能依然保留。回复的父帖缺失时，应用会搜索该回复的 relay 提示以及父帖作者的 relay，这意味着会短暂连接到用户自己列表之外的 relay。每当设备切换网络，relay 和实时消息订阅也会重新连接。

### Sidecar {#sidecar}

Nostr 浏览器扩展兼签名器 [Sidecar](https://github.com/dmnyc/sidecar) [发布了 1.16.3](https://github.com/dmnyc/sidecar/releases/tag/v1.16.3)。撰写器和高亮工具现在会[发布到账户自己的 relay，并且只统计确认收到该 event 的 relay](https://github.com/dmnyc/sidecar/pull/545)，随后链接到这些 relay。确认只说明 relay 接受了该 event，并不代表它会一直保留。展开式撰写器不再回退到设置中的默认 relay。每个 relay 各有 12 秒的截止时间。只有在所有 relay 上都失败的发布才会重试，而且只在新的套接字上重试一次。[投票结果](https://github.com/dmnyc/sidecar/pull/544)还会向四个公共 relay 查询选票。打标签之后合并的一项变更[又加入了一个 relay](https://github.com/dmnyc/sidecar/pull/550)，用来捕获提交到常用 relay 之外的选票。在一次正在进行的投票中，计票数因此从 21 票增加到 23 票。这只是单次投票的结果，不能说明整个网络范围内的统计是否完整。计票仍然限定每人一票，并忽略投票截止后投出的选票。更早的 [1.16.1](https://github.com/dmnyc/sidecar/releases/tag/v1.16.1) 把长期签名授权限制在批准它的账户和站点范围内；如果 event 带有 d tag，则进一步限定为单个可寻址记录。授权从不涵盖加密或解密。个人资料以及关注、静音和 relay 列表都不在任何授权范围之内。删除、zap 请求、relay AUTH 和钱包控制同样被排除。扩展处于锁定状态时仍会要求输入 PIN。撤销某项授权或忘记某个站点，都会清除其授权和批准时间窗口。

另有一个[仍处于开放状态的拉取请求](https://github.com/dmnyc/sidecar/pull/552)，会让支付 CLINK offer 计为一次 zap。它在更新日志中列于 Unreleased 之下，并没有实现 Debits。offer 面板会传递一个带有 payer_data 的已签名 kind 9734 zap 请求，以便服务发布 kind 9735 收据。收据会先发往 offer 的 relay，再发往接收方的 relay，经过去重，最多六个。付款方的 relay 不会被使用。如果某个 offer 回复代码 3，并附带一个可以解码的后继 offer，Sidecar 会用新的请求和新的签名跟进一次。它绝不会写入接收方的个人资料。截至截稿时，这项变更仍未合并。

### Roadbeacon {#roadbeacon}

Roadbeacon 是一款位置报告客户端，此前名为 Roadstr，与独立的 Roadstr 应用并非同一产品。它[以新名称发布了 0.4.0](https://github.com/jooray/roadbeacon/releases/tag/v0.4.0)，这是一个采用新 event 格式的新软件包。报告和投票现在使用共享、可互操作的 kind 1315 和 1316，坐标采用可精确重建的整数帧，网页版也会验证签名。新软件包可与旧软件包并行安装，但不会迁移数据。旧 event 在 relay 上依然有效，只是新客户端无法读取它们。

### Jumble {#jumble}

[Jumble](https://github.com/CodyTseng/jumble) 是一款 Nostr 网页客户端，[发布了 v26.10.1](https://github.com/CodyTseng/jumble/releases/tag/v26.10.1)。新功能包括长文编辑器、可跨设备同步的屏蔽词、系统通知，以及群组和 Git 内容的阅读器。近期一期介绍过的待发帖子和布局改动，也随本次发布一同推出。

发布之后合并的一个提交加入了[可选的 NIP-22 回复设置](https://github.com/CodyTseng/jumble/commit/ea798677d366ff750ac556d31c5628fe47ebd275)。该设置默认关闭，并作为本地偏好保存。启用后，对 kind 1 文本笔记的回复将以 kind 1111 评论的形式发出。现有的 kind 1111 线程保留其根，对其他 kind 或外部内容的评论仍为 kind 1111。若关闭该设置，回复沿用旧的 kind 1 行为。应用会提示，部分客户端可能无法显示这些评论。

### nostr-idb {#nostr-idb}

[nostr-idb](https://github.com/hzrd149/nostr-idb) 是一个在浏览器 IndexedDB 中缓存 Nostr event 的库，[发布了 5.1.1，修复了查询问题](https://github.com/hzrd149/nostr-idb/releases/tag/v5.1.1)。按精确 ID 查找现在适用于可替换和可寻址 event；每一项过滤器约束和每个过滤器各自的数量上限现在都会生效，对待写入数据和订阅历史同样适用。缓存清理问题以及时间戳为零的 event 的问题均已修复。内存缓存大小 `maxMemoryEvents` 默认为 `maxEvents`，设为零即可将其关闭。

### Manent {#manent}

[Manent](https://github.com/dtonon/manent) 是一款通过 Nostr 同步的加密笔记本，[发布了 3.0.0，加入语音笔记](https://github.com/dtonon/manent/releases/tag/v3.0.0)。录音与其他笔记一样以加密形式同步；应用下载模型后，会使用 Whisper 离线生成转录文本。本次发布还推出了此前作为源码工作介绍过的 relay 认证恢复功能，如今它通过 NDK（Nostr Development Kit 库）的 0.10.1 版本提供。

### NoorNote {#noornote}

[NoorNote](https://github.com/77elements/noornote) 是一款桌面端和网页端 Nostr 客户端，[发布了 1.9.2，加入针对笔记和私信的设备本地全文搜索](https://github.com/77elements/noornote/releases/tag/v1.9.2)，并新增仅缓存模式。1.9.2 出现透明玻璃效果的回归问题后，[1.9.3 版](https://github.com/77elements/noornote/releases/tag/v1.9.3)恢复了下拉菜单、菜单和 toast 提示的可读性。这些版本还推出了此前仅存在于源码中的未来时间戳过滤器。加载失败的个人资料现在会保持加载状态，直到确认未命中为止。

### Earthly {#earthly}

Earthly 是一款 Nostr 地图创作客户端，[发布了 0.1.22，修复了 relay 和支付问题](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.22)。relay 认证现在与当前活跃账户绑定。恢复后的订阅和计数能够区分无法获取的计数与真正的零，并在地图各次修订之间保留计数。zap 总额来自真实的 zap 收据，应用也会等钱包同步完成后才进行支出。实时 Nostr Wallet Connect 和 mint 支付仍未经测试（[发布集成](https://github.com/zeSchlausKwab/earthly/pull/36)）。

### Chama {#chama}

[Chama](https://github.com/jesuspirate/chama) 是一款基于 Nostr event 构建的托管交易客户端，[发布了 6.4.31](https://github.com/jesuspirate/chama/releases/tag/v6.4.31)，会在注资前检查种子备份。在本设备的链上交易密钥进入已签名的 CREATE、JOIN 或存款条款之前，relay 必须返回该设备已打开的已签名种子备份；备份缺失、已停用或存在冲突，都会中止交易。重试时会重新发送完全相同的已保存备份，不会生成新种子。这次回读只能表明备份在当时可用，并不代表会持久保存。多件商品的挂单现在使用数量订单。[6.4.30 版](https://github.com/jesuspirate/chama/releases/tag/v6.4.30)仅在买方签名的条款与已签名挂单相符时才计入店面订单；对于已签名 CREATE 日期为 2026 年 12 月 1 日或之后的交易，它会防范迟到的外部 event，而更早的交易则保留旧的过期行为（[交易过期与店面验证](https://github.com/jesuspirate/chama/pull/77)）。

一个开放的拉取请求（截至我们的源码截止时间尚未合并）将实现[每个身份仅保留一个钱包种子备份](https://github.com/jesuspirate/chama/pull/92)。启动时会借助页内队列和 Web Locks 串行化首次创建，然后重新读取 relay 状态。不同浏览器之间仅依赖这次重新读取。分布式锁以及对现有冲突备份的修复，均不在本次改动范围内。我们没有测试任何涉及资金的路径。

### Linky {#linky}

[Linky](https://github.com/linky-fit/linky) 是一款通过 Nostr 同步的 Cashu 钱包，在 [26.10.7 版](https://github.com/linky-fit/linky/releases/tag/linky-v26.10.7)和 [Android 26.10.8 构建](https://github.com/linky-fit/linky/releases/tag/linky-v26.10.8)中加入了由功能开关控制的实验性链上转账。发送和接收请求由一名配置好的人工运营者在 24 小时内完成，并收取费用，因此转账既非原子操作，也并非免信任。[协调改动](https://github.com/linky-fit/linky/pull/637)使用自定义 Nostr 应用消息、[NIP-78](/zh/topics/nip-78/) 运营者配置以及一个新的链接同步范围。该范围会同步运营者待处理的 ecash 发送，使其其他设备无法对同一笔发送重复支付、退款或结算。只有当用户的钱包收到相应的 Cashu 金额时，接收才算完成。运营者与用户只能在推荐的 relay 上找到彼此，而不是通过 [NIP-65](/zh/topics/nip-65/) relay 列表或私信收件箱列表，因此一旦失去所有共享 relay，协调就可能中断。

### LaWallet {#lawallet}

[LaWallet](https://github.com/lawalletio/lawallet-nwc) 是一项基于 Nostr Wallet Connect 构建的钱包和账户服务，发布了 [2.9.0 版](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.9.0)和 [Android 1.2.0 测试版](https://github.com/lawalletio/android-wallet/releases/tag/v1.2.0)，两者都加入了借助 NFC 卡恢复到新 Nostr 登录的功能（[原生恢复流程](https://github.com/lawalletio/android-wallet/pull/1)）。恢复需要一次新的、经过密码学验证的刷卡，以及一个有效期为 15 分钟的一次性恢复二维码。资产在一笔交易中转移，角色不会随之转移，旧的 OAuth 授权会被撤销，旧登录则被清空。卡片恢复默认开启；账户持有人可以在安全设置中将其禁用，并撤销尚未失效的代码。无法连接的钱包现在会显示零余额，但这并不意味着钱包为空。在配置了报告端点的构建中，Android 测试版会强制开启 Sentry 错误报告，即使用户此前已选择退出也是如此；本地构建和 F-Droid 构建没有端点。

在打标签之后合并的源码中，[当余额足以覆盖付款时，卡片回调可能在 NWC 结算之前就返回 OK](https://github.com/lawalletio/lawallet-nwc/pull/385)，因此销售点系统必须自行确认其发票。[固定的支付上限](https://github.com/lawalletio/lawallet-nwc/pull/388)取代了基于余额的限额。一个截至我们源码截止时间尚未合并的开放拉取请求，将允许通过已配置的提供方或 Nosskey 恢复，使用来自其他应用的兼容 passkey 登录，并在签发会过期的临时会话之前先确认账户（[#386](https://github.com/lawalletio/lawallet-nwc/pull/386)）。提供方无需导入私钥即可签名，导入则是需要单独确认的选项。其截图展示的是模拟的演示响应，并不能证明实时跨源登录可行。

另一项合并同样尚未确认已进入某个发布版本，它使 NWC 和 Lightning 地址回调[不再仅因一次 make_invoice 错误就替换用户的远程钱包](https://github.com/lawalletio/lawallet-nwc/pull/389)。此时，存活性和余额检查可以保留该钱包，转而返回 503。该服务还会记住余额和受保护资金的状态，并新增了一个恢复选项。其阈值以及未知的早期历史限制了它所能保护的范围，因此它并不保证所有资金都安全。文中并未声称已完成部署，也未声称已恢复任何用户账户。

### KithMoot {#kithmoot}

[KithMoot](https://github.com/forgesworn/kithmoot) 是一款基于 Nostr 的房间聊天和通话应用，现在无需依赖其发布者的公共服务即可运行。10 月 21 日至 23 日期间，发布者[停用了公共会议码、共享 TURN 服务、文件上传以及已存储文件的读取](https://github.com/forgesworn/kithmoot/pull/535)。邀请链接取代了会议码，公共文件默认使用 Yakihonne，并在首次发送时给出提示，不过用户可以自选服务器。通话仍会先尝试直接连接，而“隐藏 IP”需要一个可用的 TURN 服务器，并且绝不会回退到直连。在桌面版 0.1.102 和 Android 0.6.106 中，[Cloudflare 的公共 STUN 取代了发布者自己的 STUN](https://github.com/forgesworn/kithmoot/pull/548)，用户也可以自行设置。[对外提供的备份副本已被删除](https://github.com/forgesworn/kithmoot/pull/543)，[离线加密副本则仍然保留](https://github.com/forgesworn/kithmoot/pull/545)。[桌面版 0.1.109 和 Android 0.6.121](https://github.com/forgesworn/kithmoot/pull/596) 会在设备凭据过期时阻止聊天，同时保留草稿，并[将用户自己的个人资料名称与可选的目录查询分开读取](https://github.com/forgesworn/kithmoot/pull/594)。常规通话引擎尚未切换到实验性的[实时 SDK 预览版](https://github.com/forgesworn/kithmoot/pull/561)，[MLS 群组候选方案](https://github.com/forgesworn/kithmoot/pull/583)也仍默认关闭。

[桌面版 0.1.110](https://github.com/forgesworn/kithmoot/releases/tag/v0.1.110) 为桌面端和网页端加入了针对图片、音频、视频和 PDF 的[沙箱化附件查看器](https://github.com/forgesworn/kithmoot/pull/597)。在桌面端，它们运行于一个专用的非持久化 Electron 渲染进程中，没有 Node 访问权限、没有应用存储，也无法访问外部网络。流式传输受到边界限制，查看器会在关闭时或消息被撤回时被清理。该拉取请求的 WebKit 运行以及额外一次打包后的恶意 SVG 运行均已停滞，因此不被宣称为已验证，而且这些都不构成安全认证。macOS 构建已经过公证，Windows 版则仍是未签名的预览版。

之后的一项合并（尚无证据表明已包含在 0.1.110 中）会在睡眠之后、发送之前[按挂钟时间续期已过期的设备凭据](https://github.com/forgesworn/kithmoot/pull/605)，并在签名器响应期间保留草稿。这一改动源于一名测试者的凭据在处于睡眠状态的笔记本电脑上隔夜过期。若某个签名器请求始终没有返回，续期仍会一直处于挂起状态；Android 另有一个尚未解决的续期缺口。一个截至我们源码截止时间尚未合并的开放拉取请求，将[暂停“帮助其他人连接”](https://github.com/forgesworn/kithmoot/pull/606)。作者表示，应用会接受一个对等协助配对，却不承载其媒体，这可能阻止回退到转发器或 TURN，导致通话无声。库的默认设置将保持不变。

### Marmot TS {#marmot-ts}

[marmot-ts](https://github.com/marmot-protocol/marmot-ts) 是 Marmot 加密群组消息协议的 TypeScript 库，发布了包含破坏性变更的 [v0.8.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/v0.8.0) 和 [v0.9.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/v0.9.0)。加密媒体 V2 加入了来源绑定，并能在重启后解密延迟的媒体；Blossom 上传描述符、目标位置和密文都会在签名前进行验证。持久化的群组会分页回填，并对不确定的提交进行重试。应用现在必须自行提供持久的摄取存储和回退存储，其适配器须拒绝失败或超时的读取。旧版 V1 群组必须重新创建，因为 V1 辅助函数仅为历史记录而保留。

之后合并的源码[为密钥包、邀请和历史监听器提供了可选的 AbortSignal](https://github.com/marmot-protocol/marmot-ts/commit/bce57044f91251040807b1c0fd7a739046ee2f4e)。在返回、抛出异常或释放时，它们的监听器会被及时清理，即使存储读取仍在进行中也是如此。消费者暂停期间到达的变更会被锁存，并合并为一次更新。取消之后，底层后端读取仍会继续。查询失败时仍会返回拒绝，而且此改动并不证明运行时互操作性。

### Nostr 邮件客户端 {#nostr-mail-client}

[nostr-mail-client](https://github.com/nogringo/nostr-mail-client) 是一款基于 Nostr 构建的邮件客户端，发布了 [v0.19.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.19.0)，为 bunker、nsec 和 ncryptsec 提供统一的登录流程，其中包括批准远程签名器的 auth_url。它现在无需重新登录即可跟进私信、收件箱、发件箱和私有 relay 列表的变更，会在同步期间对邮件通知去重，并以加密形式在设备之间同步电子邮件签名。超过 25 MB 上限的电子邮件附件会被丢弃并附带提示，而仅限 Nostr 的地址无法接收从电子邮件发出的回复。

### Napplet 一致性 CLI {#napplet-conformance-cli}

[napplet/web](https://github.com/napplet/web) 是 napplet（以已签名 Nostr event 形式分发的网页应用）的网页软件包和工具集，现在通过带版本号的 [@napplet/conformance-cli 0.4.0](https://github.com/napplet/web/releases/tag/%40napplet/conformance-cli%400.4.0) 推出了上一期介绍的验证工作。在无头运行之前，该 CLI 会检查清单的 event ID、签名以及原始 HTML 的精确哈希，并将运行时绑定、命名空间和安装方面的失败与 napplet 错误分开报告。内置回退仅涵盖 RESOURCE 和 GAMEPAD，因此自定义宿主必须显式传入源和快照输入。

[Napplet 的部署命令现在默认会准备 Zapstore 上架信息](https://github.com/napplet/web/pull/265)，为每个选定的构建截取屏幕截图，并准备一个 kind 32267 Software Application event；`--no-screenshot` 和 `--no-zapstore` 可禁用这些步骤。准备元数据并不等于发布版本，而且此改动没有添加任何软件包发布 event 或资源 event。

### napplet-soy {#napplet-soy}

[napplet-soy](https://github.com/soytec/napplet-soy) 是一个用于构建和发布 napplet 的工作区，它为自己的 soyli 命令行工具打了 [v0.31.2](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.2) 和 [v0.31.3](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.3) 两个 tag，二者都不是 Studio 部署。确认 Git 交付之后，发布流程会先核对确切的祖先关系、目标以及当前修订版本，再将其中包含的 Git 协作（[NIP-34](/zh/topics/nip-34/)）提案标记为已合并，并在恢复时复用预先签名的状态。较新的提案修订版本仍保持开放。某个 tag 包含某个提交，也不会被当作目标分支已合并该提交的证据。这些 tag 背后的源码还在统一的 Manage 工作区中加入了初版 Cashu 钱包（[NIP-60](/zh/topics/nip-60/)）视图，并让正在运行的 napplet 在切换标签页时保持运行。更早的 [v0.31.1](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.1) 更新器跟踪的是稳定的 GitHub 仓库 ID，因此迁移到 Soytec 后，各安装实例仍能保留其账户和项目。使用旧版更新器的安装实例必须运行一次安装程序。

[NIP-60 Cashu 钱包](https://github.com/soytec/napplet-soy/pull/39)会兑换 [NIP-61](/zh/topics/nip-61/) nutzap，并在执行之前保存已准备好的 mint 输出和已签名的 relay 更新，这样结果不确定的请求无需重复付款即可恢复。钱包按账户相互隔离，浏览器各标签页也无法同时花费。不过，测试使用的是假 mint，真实资金场景下的互操作性尚未验证。[贡献页面现已支持面向作者的 zap](https://github.com/soytec/napplet-soy/pull/42)，付款对象是所选发布版本或提案的签名作者。

[soyli v0.31.4](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.4) tag 记录了作者贡献历史和 zap，以及 [NIP-5D 就绪、音频和测试方面的改动](https://github.com/soytec/napplet-soy/pull/43)。域调用不再等待 shell 报告就绪。napplet 通过 NAPMEDIA 所拥有的音频由一个共享宿主统一协调，iframe 隔离并未因此放松。这个 tag 同样不是 Studio 部署。已配置的检查中，五项通过，五项被跳过。完整的规范符合性仍未得到证明，修复后的应用尚待重新发布。

### Pakstr {#pakstr}

[Pakstr](https://git.nostrdev.com/stuff/pakstr) 是一个构建 Android 应用并将其发布到 Nostr 的命令行工具，它打了 [v0.29.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.29.1) tag。发布之前，它会[读取 APK 在其 v2 或 v3 签名块中声称的签名者证书](https://git.nostrdev.com/stuff/pakstr/commit/4dbdbec3bec10bef3f96c42a8324e0fc1a10d5c5)，并将该证书的 SHA-256 与预期的 sidecar 和身份证明进行比对（[发布审查](https://git.nostrdev.com/stuff/pakstr/pulls/108)）。未签名、格式错误以及含多个证书的 APK 都会被拒绝；重新构建时，过期的 sidecar 会被删除；无效的发布 nsec 会在构建开始前就报错失败。该解析器本身并不验证 APK 签名，这一步交由 Android 和 apksigner 完成。因此，它能发现过期、未签名或证书错误的构建，却无法证明某个构建未被伪造。ZIP64、多个签名者和密钥轮换均不受支持。

### MDK {#mdk}

MDK 是面向 Marmot 加密群组的 SDK 和运行时，现已发布[稳定版 v0.14.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.14.0)。该版本带来了媒体文件交接与存储、有序的离线追赶同步、关注列表保留以及原始 SQLCipher 密钥重设（rekey），MLS 和线路格式均保持不变。[0.14.0 发布指南](https://github.com/marmot-protocol/mdk/blob/v0.14.0/docs/release/0.14.0.md)和 [0.14.0 集成指南](https://github.com/marmot-protocol/mdk/blob/v0.14.0/docs/integration/0.14.0.md)要求应用随附一套相互匹配的绑定、原生库和头文件，[MarmotKit 0.14.0](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.14.0) 为 Apple 和 Android 平台打包了这些内容。在 Apple 平台上，二进制文件是原始静态 XCFramework，所以应用需要把它与匹配的 Swift 绑定搭配使用，并将其中的 PrivacyInfo.xcprivacy 资源复制到自己指定的包装产品中；通过该版本的归档检查，并不能证明 App Store 导出一定会成功。数据库和存储采用单向迁移，每个页面都会重设一次密钥。降级仍不受支持。账户媒体和交接数据应排除在备份之外。WN agent 仍处于预发布阶段，相关 crate 也没有发布到 crates.io。已知限制依然存在：晚到超过五个 epoch 的历史记录会在没有任何提示的情况下变得无法解密。跨越 epoch 推进时在传输途中丢失的媒体，这一问题尚未修复；另外还存在一个群组上下文排序方面的兼容性问题。

从 tag 祖先关系来看，该稳定版 tag 还包含五项同步和媒体方面的改动。[群组订阅刷新只重新打包发生变化的 REQ 批次族](https://github.com/marmot-protocol/mdk/pull/2583)；失败的批次族会保留其当前生效的路由，留待下次同步，而部分提交仍会报告同步失败。[发送前的刷新失败时，发送和群组变更仍会继续进入持久队列](https://github.com/marmot-protocol/mdk/pull/2567)，不过完成状态可能停留在 CompletionUnknown。[不可达 relay 的 REQ 会以同一 ID 保持待发状态，直到重新连接](https://github.com/marmot-protocol/mdk/pull/2572)，因此降级状态下的覆盖范围并不等于完整历史。[入门修复审批会等待所有发现来源](https://github.com/marmot-protocol/mdk/pull/2545)，若某个已声明的来源超时，则返回 RetryableFailure。[可选启用的按账户媒体保留策略](https://github.com/marmot-protocol/mdk/pull/2541)提供从 Keep forever（永久保留）到 30 天不等的选项，按接收时间或最后一次显式重新下载的时间清理媒体，而不是按最后查看时间，并且不会删除消息历史。宿主必须处理新的 CleanedBySetting FFI 值。

该 tag 之后，已合并的源码继续推进多设备和推送方面的工作，目前还没有任何版本声称包含这些内容。[加入后的历史请求会持久保存](https://github.com/marmot-protocol/mdk/pull/2635)，跨越提交和重启依然有效，填补了 Welcome 与实时消息之间的空档。[按账户统计成员](https://github.com/marmot-protocol/mdk/pull/2634)后，某人的第二台设备加入或离开时，不会再产生关于此人的错误通知；[Welcome 处理会忽略发往同账户其他设备的投递](https://github.com/marmot-protocol/mdk/pull/2633)，既不会导致加入失败，也不会消耗密钥。推送方面，MDK [在提交后以 gossip 方式传播所有者签名的记录和墓碑](https://github.com/marmot-protocol/mdk/pull/2620)，这些数据存放在[新的推送 gossip 存储](https://github.com/marmot-protocol/mdk/pull/2617)上；它还会[在添加成员后重新共享令牌](https://github.com/marmot-protocol/mdk/pull/2613)，并[通知接收者的所有设备](https://github.com/marmot-protocol/mdk/pull/2609)，不过发送者自己的设备仍收不到通知。[每次触发都使用新的随机填充](https://github.com/marmot-protocol/mdk/pull/2608)，以免去重机制抑制唤醒。[KeyPackage 发布改为采用账户自身的 relay 列表](https://github.com/marmot-protocol/mdk/pull/2594)；如果某个列表不完整或没有可用的 relay，发布就会失败，并保留已存储的列表。[类型化的“epoch 已过期”和“状态未决”媒体状态](https://github.com/marmot-protocol/mdk/pull/2312)会告诉应用应当重新上传，还是先同步再重新发送；[传输状态变更会立即送达，字节进度则分批汇报](https://github.com/marmot-protocol/mdk/pull/2311)。

较新的账户设备源码是在为后续版本铺路，并不是稳定版 0.15。10 月 28 日的三个 nightly 版本标注为仅供测试，固定在提交 b8d0a49 上。该提交早于后来的合并，因此这些版本的构件并不包含全部内容。MDK 会为每个账户最多 20 台近期设备[逐设备选择兼容的 KeyPackage](https://github.com/marmot-protocol/mdk/pull/2649)，而[登出只会撤回本设备的发布槽位](https://github.com/marmot-protocol/mdk/pull/2654)。[新生成的 package 有效期为 30 天加一小时，并在发布后六到七天刷新](https://github.com/marmot-protocol/mdk/pull/2643)。发现过程会查找每一台设备，但 relay 故障可能导致部分设备被遗漏；重新邀请或许有帮助，但无法保证自动恢复。[经过认证的逐叶节点能力检查](https://github.com/marmot-protocol/mdk/pull/2645)取代了按账户的缓存。[当所有创始者都支持时，新群组会要求 account-devices 组件 0x800d](https://github.com/marmot-protocol/mdk/pull/2656)，[升级后的设备现在也会通告该组件](https://github.com/marmot-protocol/mdk/pull/2659)。这类群组会拒绝缺少该组件的旧设备，现有群组则保持不变。在这一要求下，MDK [会拒绝组件数据、不受支持的叶节点、每个账户超过 20 个的叶节点，以及试图取消该要求的操作](https://github.com/marmot-protocol/mdk/pull/2637)，遗留群组和不作此要求的群组仍维持原样。另外，在创建任何群组、Welcome 或 event 之前，它会[拒绝宿主为 schema 中不含数据的应用组件提供的初始数据](https://github.com/marmot-protocol/mdk/pull/2662)。

在 0x800d 群组中，引擎获得了[本账户添加与移除权限，以及能感知父状态的提交分类](https://github.com/marmot-protocol/mdk/pull/2650)，可以区分自我更新、自我移除、同账户提交和管理员提交，其中同账户特权要求使用按值（by-value）提案。[配套的 Welcome 处理会接受同账户 Welcome](https://github.com/marmot-protocol/mdk/pull/2646)，但仅限于这类群组，并且必须先通过组件状态和签名检查；其他群组仍需要一位活跃的管理员。[本账户添加和移除的发送意图会获得公平的调度轮次](https://github.com/marmot-protocol/mdk/pull/2655)，但应用 API 目前尚未开放同账户发送意图。[设备自身叶节点被移除，现在会决定其本地成员资格](https://github.com/marmot-protocol/mdk/pull/2640)，因此同账户其他设备的存在，不会再让已被移除的设备保留成员操作。

推送 gossip 新增了[持久排队的 kind 447 公告，其中携带记录和墓碑的 8 字节摘要前缀](https://github.com/marmot-protocol/mdk/pull/2648)。这些公告会在加入时、记录变更时以及按七天一次的消息节奏发送；对等方则通过排序且错开的响应来[修复缺失的所有者签名记录](https://github.com/marmot-protocol/mdk/pull/2658)，同时抑制重复，并对每个叶节点设定 24 小时的上限。恢复方面，[cut 和 cancel 不再凭空制造新的丢失](https://github.com/marmot-protocol/mdk/pull/2673)；24 次尝试均无进展时，相应义务会被搁置，并显示历史不完整的警告。[覆盖账本](https://github.com/marmot-protocol/mdk/pull/2667)仅作为影子记录器运行，而[分时段扫描](https://github.com/marmot-protocol/mdk/pull/2665)会从最旧的时间片开始续行，目前还没有生产环境调度器。[可选启用的审计文件会在最后一次写入 30 天后过期](https://github.com/marmot-protocol/mdk/pull/2664)，清理在启动时以及每小时执行一次。实际删除可能晚一天发生；单独的密钥披露安全日志不适用这一过期机制。

一个[配对 crate](https://github.com/marmot-protocol/mdk/pull/2670) 使用临时 X25519、一个承诺值、由用户在两块屏幕上核对的七个 emoji 比对，以及最终得到 ConfirmedLink 的 HMAC 确认。它的线路适配器只涵盖传输层，并在规范出台之前默认关闭；UI 以及 Welcome 和群组链接的后续工作尚未完成，这一实现的互操作性也仍未验证。[设备名册 0x800e 源码](https://github.com/marmot-protocol/mdk/pull/2666)会对一个隐藏的单账户群组应用差异更新，但通告 0x800e 需要覆盖测试策略，所以生产构建目前还无法创建或加入设备群组。

MDK 的其他提案仍处于开放状态。其中一项将不再把 [NIP-67](/zh/topics/nip-67/) [完成视为完整覆盖的证明](https://github.com/marmot-protocol/mdk/pull/2674)，因为未经调度的扫描并不提供完整性保证。另外几项将加入[检查点重放](https://github.com/marmot-protocol/mdk/pull/2671)、[自动重新加入](https://github.com/marmot-protocol/mdk/pull/2661)以及[在现有群组中激活 0x800d](https://github.com/marmot-protocol/mdk/pull/2668)。最新一次状态检查显示，三项较早的原生 API 提案仍处于开放状态。[历史附件恢复](https://github.com/marmot-protocol/mdk/pull/2614)会检查来源槽位，并在将已验证的字节写入私有租用文件之前，核对经过认证的摘要和有效期，从而让时间线保持不联网；已交付的副本是一份无法撤销的快照。[全过滤器范围的聊天选择句柄](https://github.com/marmot-protocol/mdk/pull/2592)将覆盖所有匹配某个过滤器的聊天，不限于已加载的页面，同时排除之后到达的聊天；[wn-agent 创建群组时的创始管理员选择](https://github.com/marmot-protocol/mdk/pull/2587)则会选出受邀的创始管理员，并在上传之前拒绝非成员。

### nosfry {#nosfry}

nosfry 是一个用 Rust 编写的 Nostr relay，它为原生版和 Workers/SQL 版发布了 [nosfry v0.2.0](https://github.com/qntx/nosfry/releases/tag/v0.2.0)。该版本带来了 v0.1 时尚未发布的功能：[NIP-09](/zh/topics/nip-09/) 删除、[NIP-40](/zh/topics/nip-40/) 过期、搭配 [NIP-70](/zh/topics/nip-70/) 受保护 event 的 NIP-42 AUTH、[NIP-45](/zh/topics/nip-45/) COUNT、[NIP-77](/zh/topics/nip-77/) Negentropy 同步、[NIP-62](/zh/topics/nip-62/) 消失请求，以及 [NIP-86](/zh/topics/nip-86/) 管理 API。它还新增了带出站预算和写入策略的有界订阅，并称 permessage-deflate 默认开启。其性能和规范符合性方面的声明尚未经过独立复现，它也没有声称能与所有实现互操作。

10 月 25 日，即 0.3 tag 之后，有四项加固改动被合并，它们尚未进入任何已发布的二进制文件。Worker 的连接桶和速率桶按 /64 聚合 IPv6，而 NIP-86 IP 屏蔽列表仍按精确地址匹配（[#78](https://github.com/qntx/nosfry/pull/78)）；NEG-OPEN 扫描在收集过程中以 1024 条记录为步长计入全局同步内存预算（[#73](https://github.com/qntx/nosfry/pull/73)）。时间戳相同的并列组会维持一个以查询 limit 为上限的堆（[#72](https://github.com/qntx/nosfry/pull/72)）。NIP-86 审核快照按请求时捕获的状态，应用于已存储数据的读取和实时投递，因此已打开的请求不会立即采纳新的封禁（[#68](https://github.com/qntx/nosfry/pull/68)）。

另有一项合并同样尚未发布，它[以 64 MiB 的字节预算约束写入器](https://github.com/qntx/nosfry/pull/79)，并用更大的事务清空发布积压，每个事务都按已完成的工作量设定上限，同时保留持久化的 LMDB 同步。该项目的基准测试数据来自其自身的探测变体，而不是我们的测量结果。

### nostream {#nostream}

nostream 是一个用 TypeScript 编写的 Nostr relay，发布了 [nostream 3.7.0](https://github.com/cameri/nostream/releases/tag/nostream%403.7.0) 和 [nostream 3.8.0](https://github.com/cameri/nostream/releases/tag/nostream%403.8.0)。我们此前报道时，管理操作、审计日志、签名 webhook 和指标还只存在于源码中，3.7.0 版本把它们正式发布了出来。它新增了一个可选启用的付费写入生命周期，并修复了 LNbits 1 及更高版本的 ISO 时间解析与过期问题。静态镜像功能已被移除，其设置现在会被忽略并给出警告，改由 NIP-77 同步取代。3.7.0 的容器镜像未能发布，原因是其 Docker tag 包含非法的 `@`；3.8.0 修复了这些 tag，并为失败的镜像构建增加了重新运行机制。管理 API 和控制台也在 3.8.0 中获得了 pubkey 与 kind 列表以及 IP 和速率限制绕过控制，并附带发布量最多的发布者、IP 和速率限制命中次数等统计；该版本还修复了切换速率限制策略或升级时出现的 Redis 键冲突。仅凭源码无法确认镜像现在已能正常发布，也没有任何关于已部署计费功能的声明。

另有一个 Rust 重写版本在 `rewrite/main` 分支上推进：它在 [740ef69](https://github.com/Cameri/nostream/commit/740ef699fb04f3f54bd82a9d012e27c04dabb480) 中合并了首个能够应答真实客户端的线协议核心，到 [2b2287f](https://github.com/Cameri/nostream/blob/2b2287f8acc43b1e0b3039c745c88a03268831aa/crates/nostream-relay/src/strategies/mod.rs) 时，策略注册表已实现其余 14 个策略分支。这个非默认原型与 TypeScript `main` 以及稳定的 3.x 版本相互独立，其评审和 CI 结果均来自作者本人。[NIP-43](/zh/topics/nip-43/) 和 [NIP-56](/zh/topics/nip-56/) 的处理默认保持关闭。vanish 请求仍可能在与并发发布的竞争中落败，因此 vanish 并不构成隐私保证。作者此前提出希望有人对访问和身份相关代码进行人工评审，这一请求目前依然有效。

### swift-nostr {#swift-nostr}

swift-nostr 是一个 Swift 语言的 Nostr SDK，于 10 月 27 日发布了 [0.9.0](https://github.com/yysskk/swift-nostr/releases/tag/0.9.0)。该版本新增了类型化的密钥、event ID、URL、时间戳、坐标和订阅 ID，可由任意本地或远程签名器签署的 EventTemplate，类型化错误，由连接池持有的订阅，以及 RelayRoute 路由，可经由连接池、指定的确切 relay 或 NIP-65 outbox 进行路由。Event.verify 现在遇到无效签名会抛出错误，因此从 0.8 迁移需要修改源码。更早的 [0.8.0](https://github.com/yysskk/swift-nostr/releases/tag/0.8.0) 是一个加固版本。据其发布说明，它会验证可替换 event、gift-wrap 发送者以及 NIP-46 和 NWC 响应，对多 relay 响应去重，并新增由签名器驱动或基于共享密钥的 NIP-44 加密，另有更严格的 zap 检查，这一点属于破坏性变更。以上均为作者的说法，并非审计结论。

我们此前报道过的 0.8 之后的修复，现已随 0.9.0 发布。签名器会[拒绝公钥与自身不同的 event](https://github.com/yysskk/swift-nostr/pull/239)，[取消订阅时也不再为了发送 CLOSE 而打开已断开的 relay](https://github.com/yysskk/swift-nostr/pull/238)。核心发送调用会抛出 notConnected，订阅则会显式建立连接，不过 NWC 和 NIP-46 传输在发起新请求时仍会重新连接已断开的 relay。NWC 和远程签名器调用[获得了类型化错误和即时取消](https://github.com/yysskk/swift-nostr/pull/247)，但已经发出的请求仍可能被执行。NWC 通知流和认证质询流[会在 relay 终止时结束](https://github.com/yysskk/swift-nostr/pull/242)，连接等待[会在所有 relay 流结束后失败](https://github.com/yysskk/swift-nostr/pull/244)，[过滤器的 tag 查询也只存储一次](https://github.com/yysskk/swift-nostr/pull/241)，每个 tag 对应一个 JSON 键。通用的 [WalletConnectRequest](https://github.com/yysskk/swift-nostr/pull/232) 支持自定义的单响应 [NIP-47](/zh/topics/nip-47/) 方法，并执行常规的 result_type 和错误检查，multi_pay 则仍单独处理。借助可扩展的 [RemoteSignerMethod](https://github.com/yysskk/swift-nostr/pull/229)，可以调用内置集合之外的 NIP-46 方法并返回结果字符串；无论哪种情况，钱包或签名器都必须支持相应方法。[EventTemplate 配合 signer.sign](https://github.com/yysskk/swift-nostr/pull/214) 让远程 NIP-46 签名器也能使用 zap 请求等以往需要本地 EventSigner 的辅助工具，配套修改涉及[若干数据模型](https://github.com/yysskk/swift-nostr/pull/215)以及 [NIP-29](/zh/topics/nip-29/) 和 [NIP-98 构建器](https://github.com/yysskk/swift-nostr/pull/216)。这一变更改动的是 API，而非线上传输格式。

在 0.9.0 tag 之后合并的代码不属于该版本。调用方[取消发送时，现在会保留健康的 relay](https://github.com/yysskk/swift-nostr/pull/257)，[DM 的打开和结果类型也变得更简洁，rumor 作者与签名器绑定](https://github.com/yysskk/swift-nostr/pull/260)。[FileAttachment 统一了加密文件元数据](https://github.com/yysskk/swift-nostr/pull/261)。[单一的 setSigner 与 removeSigner 组合](https://github.com/yysskk/swift-nostr/pull/262)可防止过时的远程设置操作撤销登出；removeSigner 会停止 AUTH 回复，但不会撤回已经发出的远程请求。[重连和去重设置有了各自的配置类型](https://github.com/yysskk/swift-nostr/pull/263)。

### haps {#haps}

haps 是一个安装器，用于安装由 Nostr 密钥签名的软件，此次发布了 [haps v0.1.22](https://github.com/mmalmi/haps/releases/tag/v0.1.22)。该版本以 [haps v0.1.18](https://github.com/mmalmi/haps/releases/tag/v0.1.18) 为基础，后者在私有主目录和可写检出目录中执行 Linux 和 macOS 源码构建，并默认关闭网络访问。显式的 allow-build-network 和 allow-host-build 选项可以覆盖这一行为。Windows 源码构建需要 host-build。已安装的应用仍位于沙箱之外。[haps v0.1.19](https://github.com/mmalmi/haps/releases/tag/v0.1.19) 新增了单一的“审计并安装”确认，将固定的源码和构建配方与构建产物的哈希绑定，这样，匹配的发布者二进制文件就可以按照该已审查构建的策略进行安装。复用受信任的审查不算作另一次独立审计。从不可变签名目录安装仍需审计，已发布的警告则需要单独同意，默认选项为“否”。0.1.22 版本新增了[有界查找和完整源码发布者检查](https://github.com/mmalmi/haps/commit/606a1cd25ef8ff9f454adb0d89acb5d4c9605a35)。查找现在共享较短的截止时间，客户端[在首个 relay 连接后即开始查询](https://github.com/mmalmi/haps/commit/f58d7fa30e149c8f0e500bd7cd59da7e834cc61c)，快照搜索则返回在单个 3 秒预算内找到的已验证结果。在更改任何源码 ref 之前，发布流程会先进行检查：只有找到合格的捆绑 git 辅助程序、与固定配套二进制文件相匹配的单独安装辅助程序，或声明支持 complete-blob-dag-v1 的辅助程序，它才会运行，否则拒绝执行。基线依赖审查覆盖、符号链接与大小防护以及有界重试都得以保留，但这并不是一次新的独立审计。一次成功的冷安装并不能说明间歇性传输超时已被修复，固定的辅助程序捆绑包也仍然依赖宿主工具链。

### Swarm 使用 NIP-98 认证保护其管理 API {#swarm-protects-its-admin-api-with-nip-98-authentication}

Swarm 是一个连接 Nostr 的发布与管理服务器，[发布了 v0.2.0](https://github.com/HiveTalk/swarm/releases/tag/v0.2.0)，在现有的仪表盘 cookie 之外，新增了[面向管理 API 的 NIP-98 HTTP 认证](https://github.com/HiveTalk/swarm/pull/59)。服务器会检查 kind 27235 event 的签名、从过去五分钟到未来一分钟的时间戳窗口、HTTP 方法、路径和查询、运营者固定的 pubkey，以及可选的载荷哈希。若接受转发的 host，则默认前端有受信任的代理。原本公开的 `/environment` 端点现在需要管理员认证。

之后的一次合并新增了[可选启用的 X 交叉发布](https://github.com/HiveTalk/swarm/pull/67)，用于已关联团队成员的 kind 1 笔记，但尚未确认已包含在任何版本中。定时笔记和通过 WebSocket 到达的笔记走的是同一路径。带有 `e` tag 的回复会被跳过，不会回填任何内容，重复项按 event ID 去除。CMS 端使用 NIP-98 认证。发帖依赖本地 OAuth 或受信任的委托服务，因此既不是去中心化的，也不是无需信任的。向生产环境的 X 服务发帖尚未经过测试。

### fips2go 开启与已验证 mesh 域名的直接连接 {#fips2go-turns-on-direct-links-to-verified-mesh-domains}

fips2go 是一个 Android mesh 客户端，通过 Nostr 公告发现对等节点和域名声明，此次发布了 0.9.6 至 [0.10.0](https://github.com/fr34aky/fips2go/releases/tag/v0.10.0) 的多个版本。0.10 版本[默认开启直接连接](https://github.com/fr34aky/fips2go/pull/91)，连向最多两个最近验证过的域名所对应的服务器，且只计入通过 DNSSEC 或多个解析器固定的域名。这些连接会向相应服务器暴露手机的公网 IP 地址和在线时段，并向公共 relay 透露其选择了哪些服务器，不过用户可以关闭它们。已针对确切服务器和端口固定的 TXT 记录，现在无需新的 Nostr 声明即可解析；新服务器、端口发生变动的情况以及不含端口的记录则仍需等待。如果网络切换需要新的 VPN 路由而配置未变，应用只会替换隧道，节点、连接和会话都会保留。热点变化、其他配置变化以及故障回退仍会重建节点。

### fips-pub-domains 在获取声明之前即可应答已固定的查询 {#fips-pub-domains-answers-pinned-lookups-before-fetching-claims}

fips-pub-domains 负责解析从公共域名到 mesh 地址的 Nostr 签名绑定，发布了 [0.2.9](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.9) 和 [0.2.10](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.10)。在相同的固定策略下，针对确切服务器和端口固定的 TXT 记录现在可以在后台声明获取完成之前作答，而新服务器或新端口仍需等待声明。在桌面端启动时以及网络变化后，解析器会预热最多 16 个已固定的服务器，从而向这些服务器和路由节点暴露在线状态。在首个 20 秒的退避期内，它每三秒重试一次，一旦有服务器应答便提前结束。

在这些 tag 之后合并的两项更改尚未发布。[其中一项新增了 `fips-ca` ServiceClaim 角色](https://github.com/fr34aky/fips-pub-domains/pull/29)，该角色不带端口，拥有自己的 DNSSEC 链和证明，与 `fips-dns` 相互独立，既没有推出新的 PKI，也没有改变 DNS 绑定策略。[另一项新增了 CLI verify 和 zone 命令](https://github.com/fr34aky/fips-pub-domains/pull/30)，这些命令只读取固定文件，不会写入。在这份代码中，证明只携带其自身的上一个见证，其他角色条目则会被重新验证。require-previous 选项会拒绝缺失的数据，却无法区分服务中断与记录不存在。

### Codr {#codr}

[Codr v0.8.0](https://github.com/tidley/codr/releases/tag/v0.8.0) 是一个通过 White Noise 加密聊天控制桌面编程会话的桥接工具，新增了一项 worker 更新，该更新需在聊天中确认，并且必须在十分钟内完成。它从固定的维护者处拉取 ngit 记录，并获取经过校验和验证的 Blossom 字节，不提供 GitHub 回退。它会拒绝连接器或存储 cohort 的变更，一旦启动失败，就恢复旧的可执行文件。到目前为止，这项更新只在测试夹具上运行过。文件和媒体现在可以送达繁忙的会话而不打断它，上限为 25 MiB 和四个附件。可选的 Gemini 转录会把解密后的语音消息发送给 Google，默认关闭。0.4 至 0.7 版本实现了将手机文本送入繁忙会话，新增了 /cancel 以及项目、代理和模型菜单，并迁移到了 MDK 0.14。从 0.13 迁移只能单向进行，并且需要备份和批准。

[可选启用的仅限所有者使用的控制聊天](https://github.com/tidley/codr/pull/7)（`control_chat=true`，默认关闭）会在下一次 worker 启动时创建其群组。`/new` 会在任何聊天被关联之前启动项目会话。如果无法确定是否已成功创建，则不会自动重试。

一个开放的 pull request 在我们的资料截止时间点尚未合并，它将让[新编程会话的群组创建](https://github.com/tidley/codr/pull/18)把尚未写入的会话记录视为空。无效或有歧义的会话记录仍会被拒绝。这将恢复在首次提示之前为全新 `/new` 会话发送手机邀请的功能，也不会改变会话的授权方式。

### nostr-media {#nostr-media}

[nostr-media 0.17](https://github.com/fabianfabian/nostr-media/releases/tag/0.17) 是一个用于托管 Nostr 媒体的 WordPress 插件，此次加固了 Blossom 镜像功能。它现在会[在获取镜像 URL 之前检查已签名的 kind 24242 哈希授权](https://github.com/fabianfabian/nostr-media/commit/f29e15e387a41c0d43b97d5b8643e287ccae88d4)，未经授权的请求会在不下载的情况下直接被拒绝。获取操作使用 WordPress 的安全 HTTP API，该 API 仅允许公共 HTTP(S) 主机并会验证重定向，上限为 20 秒、三次重定向和 128 MiB；下载的字节仍会经过哈希计算和校验。Authorization、X-SHA-256 和 X-Content-Type 头部的匹配不区分大小写。服务器端请求伪造防护的强度，取决于 WordPress 安全 API 本身有多强。

### NosTube {#nostube}

[NosTube](https://github.com/flox1an/nostube) 是一个基于 Nostr 构建的视频网站，为撤销对一个已遭攻破的证书颁发机构的信任，发布了[服务器端 0.1.25](https://github.com/flox1an/nostube/releases/tag/server-v0.1.25) 和[桌面端 0.2.51](https://github.com/flox1an/nostube/releases/tag/v0.2.51)。服务器的 Rust relay 在 WebSocket 或 HTTPS 连接中不再信任该机构，镜像构建现在要求使用固定的 Debian 系统 CA 捆绑包。桌面版本对其 TLS 层和 almond sidecar 采取了同样的缓解措施。这些安全声明来自发布说明。之后的服务器端 0.1.27 发布说明称“不要使用”（DO NOT USE）该镜像，因为它附带了过时的 libbrotli1，并指向 0.1.28，但我们尚未确认 0.1.28 已经发布。

### bitchat {#bitchat}

[bitchat](https://github.com/permissionlesstech/bitchat) 是一款运行于蓝牙 mesh 和 Nostr 之上的即时通讯应用，发布了 [1.8.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.8.0)，针对 Nostr 位置聊天（geochat）做了性能优化，并为 DM rumor 设置了有界时间戳。应用现在依据发送者 ID 而非昵称来识别用户自己的消息（[发送者身份修复](https://github.com/permissionlesstech/bitchat/pull/1793)）。私有群组会固定其创建者，mesh 对等节点 ID 也不会出现在 geohash DM 中。这些性能数据由项目方自行提供，我们尚未复现。

一个开放中的 pull request 截至我们的资料截止时尚未合并。它将通过距离最近的五个 relay 加上五个共享备用 relay 进行路由，每条路由最多十个连接，从而在 relay 中断期间保持地理聊天的连通（[#1822](https://github.com/permissionlesstech/bitchat/pull/1822)）。在 relay 目录加载完成之前，消息会先进入队列；订阅和待处理的写入则会在不更改身份的情况下迁移。验证工作由作者本人完成，而 Android 端的配套改动是另一个单独的 pull request。

另一个同样未合并的开放 pull request 将使用自定义的 `LIVE_VIDEO_V1` 格式（而非 Nostr 传输）添加[基于 iOS 和 macOS 蓝牙 mesh 的实时视频](https://github.com/permissionlesstech/bitchat/pull/1827)。公开帧会经过签名并接受新鲜度检查。私信帧将在 Noise 加密内传输；录制内容则作为消息发送。据作者报告，一条从 Android 到 iPhone 的视频流已被成功接收。从 iPhone 发送、两台 iOS 设备之间的组合以及私信实时视频均未经测试。

### ngit {#ngit}

[ngit](https://github.com/DanConwayDev/ngit-cli) 是一款通过 Nostr 进行 Git 协作的命令行工具，现已发布 [v3.0.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v3.0.4)。relay 连接以及 Android 上的 HTTPS 不再信任一个已遭入侵的证书颁发机构。交互式提示现在会防止空白输入，命令也会遵守离线过滤器。更新远程跟踪分支时，尚未发布的提交会被保留。此外，诊断信息还能区分来源缺失与查询未返回结果这两种情况。

### Hasheus {#hasheus}

原名 verify 的文件校验工具现已更名为 [Hasheus](https://github.com/tinfoilhash/hasheus)，并发布了 [2.0.0](https://github.com/tinfoilhash/hasheus/releases/tag/v2.0.0)。它会将文件与发布在 Nostr 上的哈希值进行比对，现在会从受信任的验证者处获取描述和 URL，并对大文件分块计算哈希。只有与发布内容完全一致的文件才会显示“已验证”横幅。它还能处理格式错误的个人资料，对验证者去重，并在缺少 relay 时报错。校验和匹配只能确认文件本身，并不能证实发布者对该文件的说法。

### Alby JS SDK {#alby-js-sdk}

[Alby 的 JavaScript SDK](https://github.com/getAlby/js-sdk) 发布了 [9.0.0](https://github.com/getAlby/js-sdk/releases/tag/v9.0.0)。NWC 客户端现在会为每个已发布的请求固定等待 5 秒以接收 relay 的 OK，若未收到则以 Nip47PublishTimeoutError 失败，而各方法的回复超时保持不变。无法解密的回复现在会被拒绝（reject），relay 返回的失败文本也会被保留（[请求错误处理](https://github.com/getAlby/js-sdk/pull/597)）。这次破坏性变更移除了已弃用的 multi_* 方法，使用 Nip47SingleMethod 的代码应迁移到 Nip47Method。relay 返回 OK 仅表示 relay 接受了该请求，并不代表支付成功。

### Alby Hub {#alby-hub}

[Alby Hub](https://github.com/getAlby/hub) 是一个通过 Nostr Wallet Connect 为钱包提供服务的自托管 Lightning 节点，现已发布 [1.24.4](https://github.com/getAlby/hub/releases/tag/v1.24.4)。该补丁从其原生 LDK 和 Go TLS 连接中移除了对一个已遭入侵的证书颁发机构的信任，而 hub 的 NWC 钱包服务正依赖于这些连接。它还修复了 CLN hold-invoice 插件的启动问题。

### Orchard {#orchard}

[Orchard](https://github.com/Letdown2491/orchard) 是一个 Flatpak 软件目录，现已发布 [0.3.0](https://github.com/Letdown2491/orchard/releases/tag/v0.3.0)。该版本将[软件发布互操作性](https://github.com/Letdown2491/orchard/pull/4)与 [NIP-82](/zh/topics/nip-82/) 相衔接，并整合了[Flatpak 资源的准备](https://github.com/Letdown2491/orchard/pull/5)功能，以便通过 ngit 或其他 NIP-82 工具进行发布。NIP-82 是一项提议中的软件目录规范，尚未获得分配或被接受，因此 Orchard 实现的是一份仍可能变化的草案。

### Bell {#bell}

[Bell](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpdljffezmc9dgwal6akc90mk3dye9gektu8s2cfptj37xrrt476wf42080) 是一款 Android 上的 Nostr 对话聚合器，可将多个账户的回复和引用汇集到一个按时间排序的列表中。根据其 [0.1.0 发布说明](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq0s4r2rh63clk2e97sr8kfx7874dequvnhdcf562ag28pwjxg3fmvvs3al)，点赞、zap、普通转发和一般性提及不在聚合范围内；账户可以通过 Amber 签名，也可以保持仅查看模式。从 [0.6.0](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqh7w3wy9773f599y90vm5c32xkr8uea57gvp3ce08x85254z06xvfrc5f8) 到 0.9.0 的各个版本增加了按账户设置的静音规则，以及支持多选标为已读的仅未读视图。这些版本的说明称，恢复功能会原样保留已签名的回复和反应，且不会自动产生重复。[0.10.0](https://njump.me/nevent1qqsdu5x6ca9npnef9kfmcavpf6qelacc86rvcufa35mf67kdxm6f36qzyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk09q3d2) 和 [0.10.1](https://njump.me/nevent1qqsyv7r8a0e82ltdhawfctcwrk5n5a9lejaart2q3hxkquqfqqzxdgszyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk8kg3j4) 允许用户在设备上隐藏单条帖子，并支持撤销和恢复。隐藏不会从 relay 删除任何内容，新回复也仍会显示。垃圾信息举报同时针对帖子及其作者，会从明确选定的账户公开发出，并不等同于私下屏蔽。[0.11.0](https://njump.me/nevent1qqsytpz6d4ctsfvpzrdgx23m7542y8wzjnn0qsctk4p5pp2hnwyugrszyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkjh2y3n) 增加了转发功能，用户需先查看原帖和发送账户。通过账户头像，可以选择由哪个账户回复、做出反应或转发。能够发布转发，并不意味着普通转发通知现在也会被聚合。缓存的线程可能仍不完整；可选开启的后台监听取决于 Android 的电源和网络规则，不承诺始终在线或即时送达。

### SkateSpots {#skatespots}

[SkateSpots](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpas2cx4mzh73kytt49479xdtrs2q37llm848e0zhvs0y72296sv8c7ad0x) 是一张由社区共建的滑板场地和商店地图。1.7.4 版本加入了端到端加密的社区聊天，其中由社区机器人自动批准新设备，管理员也可以进行批准。[1.7.0](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq50n30vvchf923kmne5vj0ptk7ful6qldk37xva9x2ap2879e4rmaep40k) 让社区 relay 成为场地和商店的权威数据源。在 [1.7.3](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp8g4ah0nqaj796uuw0me3ck37azyjxp8gs9e3munfd7v5542snvp5wm656) 中，私人 crew 聊天的 Android 邀请二维码得到了修复，该聊天是在更早的版本中引入的。[1.7.8](https://njump.me/nevent1qqsppdcrel94afrsluvt0gz4s2k079yvmne776w0juak38js857zsdszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkuwx9gn)、[1.7.10](https://njump.me/nevent1qqspp0kr4x4c6m5fw5glqtdv7r08jseq70mp8n224qqp6rzmm2rt5yszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetke6cpl5)、[1.7.15](https://njump.me/nevent1qqsq375v0ucwszn7s6wdatn2c9fgyxrcalmt7yazedav5zypt5d4pkqzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkj0vmg9)、[1.7.19](https://njump.me/nevent1qqsr7xkz9evx70q47nzqr5wlsfs7cpzxaxy2ymzhxh4h9thy2s62n9qzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkgrmthk)、[1.7.20](https://njump.me/nevent1qqsxn8f0az09eg75tnsc7kxlf3spwe4vfvh633te9k3mcsf3nhl3thszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkqddtl9)、[1.7.21](https://njump.me/nevent1qqsr9wdhzwznntvkcjzphdy0249esazdgg7k0spz370lw9mzj8jwsggzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk7dgt33) 和 [1.7.22](https://njump.me/nevent1qqspx5m53qxctceqmva3dkynkswukl6zrwl4gr6mu3r0zucdwt96muqzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk977zdf) 等版本扩展了这一 crew 聊天。与社区聊天的机器人批准不同，这里由现有 crew 成员通过二维码批准新设备，成员和设备都可以被移除，而对创始人执行提升操作会重新发布 admin tag。反应、删除墓碑和已读回执以加密的 MLS 控制消息形式传输。墓碑并不是 relay 上的硬删除，自动回执也只会来自静默签名器。后台监视器使用的是成员自己的密钥，绝不使用管理员密钥；它大约每分钟一次将加入请求转换为 [NIP-17](/zh/topics/nip-17/) 私信或铃铛通知。对于 Amber 用户，加入通知要等到打开铃铛后才会出现，而静默签名器可以预先加载这些通知，因此 Amber 不会在后台弹出提示。未读计数使用待处理的 NIP-17 信封 ID 而无需解密，不计入用户自己发送的副本，也不会透露或确认会话主题。即时或持续的后台送达并无保证。1.7.19 到 1.7.22 版本还增加了仅在命令面板打开时运行的全局数据集搜索，并会记住地图和图层状态。我们尚未对这些改动进行独立的设备测试或安全审计。

### Emanator {#emanator}

[Emanator](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqannu7pfrkl3daywutspdhdfp3ct4wyk0njcs69nlhufh6gm36a724p5x6) 是一款多账户 Nostr 客户端，在 1.5.0 中已经可以发起 [NIP-17](/zh/topics/nip-17/) 私密对话，而此前的版本只能回复已有的会话线程。用户先选择一个启用了消息功能的发送账户，然后按名称或 [NIP-05](/zh/topics/nip-05/) 搜索联系人，或者粘贴 npub 或 nprofile。已有的对话会被复用；如果收件人没有列出 DM 收件箱，应用会提供尽力而为的投递方式以及一个旧版选项。在 [1.4.1](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpx8h9aamsmuvu7fzkhc9n8v37m9rcnyhrc60sjuwrgftk8hhns02ahkkqn) 版本下。重试会保留已被接受的已签名 event。只有那些没有任何 relay 接受过的旧 event 才能被重新签名并更新日期。

### Feather {#feather}

Feather 是一款 Android Nostr 客户端，我们上次在第 45 期报道它时，它还处于 0.9 系列，如今已发布到 [1.8.4](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqqguewyhvswx5qkcn29ckc7mjsendh0wtc2u6n6l8wzvnvup0wt8y6q9ww)。1.x 版本的发布说明加入了原生的 NIP-34 issue 浏览和报告功能，通过仓库公布的 relay 进行。已签名的操作现在会在设备上的发件箱中等待，由 WorkManager 在后台投递，并且先发送父帖、再发送回复。[1.8.0](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqny0jdx2y7gaxdwcmexndm6rk2qgtkxz3zq3cucdlxvdyl92sp532mdl79) 增加了 kind 20 图片帖子，支持保存草稿和离线投递；1.8.4 则增加了在成功举报后可选的静音功能。自 [1.7.0](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp2qa3hycyvc8g7c7wt3a2zl06uneuu5xt8w38q87xqd4pq9uq89udwewmd) 起，翻译通过独立的 Offline Translator 应用及其语言包完成，没有云端回退。

### OUTKAST {#outkast}

[OUTKAST](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqg4n7egyu8slmmx6gtmus5stgf6fdsxr43rp9fz57ftv4ru5ettxrc4nc3) 是一款 Android Nostr 客户端，在 2.2.1 中加入了设备端的 Network 发现功能，可展示你关注的人在过去 48 小时内点赞或转发过、而你尚未关注的账户所发的帖子。发布说明称，排序会按数量统计反应、回复和 zap（而非 sat 金额），再权衡好友数量和新近程度，且不依赖排序服务器。一旦你关注了 40 个或更多账户，一条帖子至少需要有两位好友支持。结果最多为 100 条帖子，不提供更早的分页。发布说明还介绍了基于所选用户或列表的自定义 feed，以及一个照片编辑器：编辑后的照片会保存为不含元数据的 JPEG，而未经改动的原图则原样上传。

### CustID {#custid}

[CustID](https://njump.me/nevent1qvzqqqr4dupzpw5cfkeqauh4qfmq3grjpaqd8l3n97mpcs94a4s0x946ypqgzv0fqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp6736dd3jl2ucdqs85ycw8yj9veluh4ug8jqwu3y0wfr06up4s7y8cfupa) 是一款 Nostr 签名应用。在 0.2.2-beta 中，对于受生物识别保护的身份，NIP-46 ASK 请求现在需要生物识别批准，不过近期完成的一次认证即可满足该提示。已记住的批准和拒绝规则（包括较早的批准）现在会在 NIP-46 和 NIP-55 上静默生效。启用自动批准前会先显示确认警告，若取消则不会做出任何更改。该 beta 版还会在其发布的 event 中添加 [NIP-89](/zh/topics/nip-89/) 客户端 tag。这些 tag 默认开启，会向读者显示是哪个应用发布了某个 event；在 Privacy 设置中可以将其关闭。

### Nostr Vault {#nostr-vault}

[Nostr Vault](https://njump.me/nevent1qvzqqqr4dupzqcdl0y9jp990kq6ftj0px6k0v9d7plxv9ju4kkk0khmvemlp3vrzqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpdeavwf9zysh2zcmlx7hevu7h3nk6nvtzlk05zsajkvewvt84z3zj929ve) 是一款 Nostr 客户端，在 3.0.0 中加入了可选开启的 FIPS 设备连接，可通过地址或二维码配对，让家中的 Mac 或闲置手机充当 vault。该 vault 会同步帖子和历史记录，通过 mesh 获取已有照片，并且在启用 mesh 后，会在重启后随 relay 一同启动。公开发布媒体仍需要一个公共媒体服务器。此版本还修复了关注和注册过程中的跨账户竞态问题，会等待用户自己的写入 relay 确认帖子后才报告成功，并将陌生人的私信保留在 Requests 中。

### Holoboard {#holoboard}

[Holoboard](https://njump.me/nevent1qvzqqqr4dupzpu0ekzvk6nl3ha6708jvepthez0tvvlxss2u07hhfnch5palsz7cqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq0j3gw5m0602kdr606fgapm3c5f4sk230ahxxr8ryvdhusrlen4cwsqg0s) 是一个用户付费发布帖子的看板，发布了 Android 1.1.0，同时在其网站和后端上线了以付款收尾的引导式“添加到看板”（Add to board）流程。访客可以提交文本和链接，也可以提交一条已有的 Nostr 帖子。已准备好的发票可在同一设备的同一浏览器配置文件中恢复，发票二维码无需账户或已连接的钱包也能一直使用。单就 APK 本身而言，它只更新了启动器图标和启动画面，因此看板方面的变化依赖于配套的网站和后端。不提供电子邮件或密码登录。

### Hopp {#hopp}

[Hopp](https://njump.me/nevent1qvzqqqr4dupzpx7mjedrw4lzxd5ekk4tmr79t0qvrayw88zdtt9vd5mm9ay0y9s7qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk7ks3v4gvr2ffqsedrlgm44xy9dlcq3clvptw4rwglrm9dm8stu2jp6t6) 是一款支持 value-for-value 打赏（boost）的播客应用，进展已超出第 45 期介绍的 0.2.x 身份与支付工作。0.3.0 版本新增基于 Nostr 的加密跨设备同步与恢复，无需 Hopp 服务器，涵盖订阅、播放进度、收藏、Up Next（待播列表）、收听习惯和下载设置。恢复时会保留现有媒体库，另有状态视图显示 relay 和待处理状态。据发布说明，结果未知的 boost 分成已有防护，可避免重复重试；预算现在也会把 Release Boosting 和 Boost2Unlock 计算在内。

### Nostrautica {#nostrautica}

[Nostrautica](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp23s4qefknu9dzeefgkxuegzd0dsml4zs2gj0sppmqvcmeh7mp5q279sgs) 是一款活动伴侣应用，在 [0.15.1](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpgrrf3n4vaeafhqhl7msnkvvscw6np9cup4e6pgm3f4x3yrz9mkxd24hwd) 中新增离线活动包，可为信号较弱的场地保存参会者、人脉配对推荐、演讲、活动页面、帖子和头像。聊天功能新增提及名称，以及包含删除在内的编辑功能；待发送的消息可以重试或丢弃。到了 0.16.0 版本，它改用 Marmot 群组消息库 MarmotKit 0.14，以更少的群组 relay 连接实现离线补同步，并在保留期清理时保留未读消息。存储迁移是单向的，迁移后旧版应用将不再受支持。发布说明声称，与 White Noise 通讯应用或网页端的互操作性没有变化。

### Staircase {#staircase}

[Staircase](https://njump.me/nevent1qvzqqqr4dupzqlxr9zsgmke2lhuln0nhhml5eq6gnluhjuscyltz3f2z7v4zglqwqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpw255ly0xpmr7vqxvn3t45z0clzu2nljrgjcrml9jpquvvyzd44ux0dqpc) 是 relay.tools 推出的 Nostr 群聊应用，在 0.1.25 中新增“频繁”（Frequent）通知模式，大约每 5 或 10 分钟检查一次，随后断开连接。处于深度睡眠时，时机由 Android 调度决定，因此后台推送既不即时，也无法保证。周期（Periodic）和频繁模式会在网络恢复时执行一次有限的检查，最多每两分钟一次；即时（Instant）模式保持不变。请求被处理或过期后，入群状态便不再等待，但不会说明属于哪一种情况。自定义协调 relay 仍由用户掌控，不会被已发布的列表覆盖。

## 开发中 {#in-development}

### Coracle {#coracle}

[Coracle](https://github.com/coracle-social/coracle) 是一个 Nostr 网页客户端，在 master 分支上合并了[一项路由修复](https://github.com/coracle-social/coracle/pull/685)。如果同一个模态框已经位于最上层，再点击 Lists 或 Groups 等菜单项现在不会产生任何反应。此前，每次点击都会再叠加一个相同的面板。按 Escape 键只能将它们逐个关闭。不同的模态框以及正常的页面导航照旧运作。这是已合并的源码，并未对应任何发布版本。

### nostter {#nostter}

[nostter](https://github.com/SnowCait/nostter) 是一个 Nostr 网页客户端，为其 zap 流程合并了五项修复。现在，[Nostr Wallet Connect 的 pay_invoice 回复](https://github.com/SnowCait/nostter/pull/2746)只有在结果类型正确、带有有效的原像（preimage），且 error 字段为 null 或被省略时才算成功。格式错误的回复会被拒绝。[专用的 rx-nostr 客户端](https://github.com/SnowCait/nostter/pull/2747)总会被释放，即使初始化失败也不例外。钱包十秒未回复会被视为结果未知，而不是失败。[发票和签名错误](https://github.com/SnowCait/nostter/pull/2748)会以内联方式显示，并保留金额和评论以便重试；发票失败与 NWC 失败也会分开报告。为了便于重复 zap，[zap 按钮会保持可用](https://github.com/SnowCait/nostter/pull/2750)。显示二维码发票时，按钮的橙色标记同样会出现，但这并不能确认手动付款已经完成。[重新打开对话框](https://github.com/SnowCait/nostter/pull/2752)只会在空闲状态下将其重置。发票或签名送达后关闭对话框，会阻止新的 NWC 付款，不过已提交的付款仍会继续。

一个[开放的拉取请求](https://github.com/SnowCait/nostter/pull/2753)将在结果未知之后、用户通过二维码后备方式付款之前显示警告，提醒先检查钱包历史记录，并会禁止自动拉起钱包。超时并不意味着钱包没有扣款。

### Pollerama {#pollerama}

[Pollerama](https://github.com/formstr-hq/nostr-polls) 是一个投票与信息流客户端，合并了[按 relay 划分的请求队列](https://github.com/formstr-hq/nostr-polls/pull/258)。该队列会调整同时运行的请求数量，在 relay 限流时退避，拆分过大的过滤器，并规范化 relay URL。“我的”包（Mine packs）视图现在会保持常驻订阅，因此响应缓慢的 relay 返回的结果仍会显示。应用中已知的重复请求问题仍未解决，私信也未针对此次变更进行测试。

### Grimoire {#grimoire}

[Grimoire](https://github.com/purrgrammer/grimoire) 是一个 Nostr 社交客户端，合并了[私信同步修复](https://github.com/purrgrammer/grimoire/pull/352)。遇到只回溯到一部分的合并 relay 分页时，历史游标不再前移；登出清空消息和已读标记后，中止保护机制会阻止解密流程将它们重新填充。被中止的回填会在移动游标或将历史标记为已耗尽之前停止。缺口依然存在：在其他 relay 缺失数据的情况下，单个应答的 relay 仍可能将历史标记为已耗尽，而签名器的永久拒绝也仍会推进游标。

### nostr-vpn {#nostr-vpn}

[nostr-vpn](https://github.com/mmalmi/nostr-vpn) 是一个使用 Nostr 密钥进行对等节点发现的 VPN，合并了[一项移动端重连修复](https://github.com/mmalmi/nostr-vpn/pull/77)。当某次发现探测已经到期时，客户端现在会重新启用通往已知对等节点的已耗尽路径。只有在近期未收到任何数据、且不存在已连接或待定路径时，它才会这样做，而且最多每 300 秒一次。健康路径和待定路径不受影响，线路格式（wire format）也保持不变。作者是针对一个隔离的原生测试夹具测试该修复的，并未在蜂窝网络上测试。另一项已合并的变更[从 doctor 诊断包中移除了网络加入密钥](https://github.com/mmalmi/nostr-vpn/pull/97)，具体做法是不在诊断输出中包含注册加入密钥和原始守护进程状态。Nostr 私钥此前已在其中被脱敏。此变更之前分享出去的诊断包仍处于暴露状态，因此分享过诊断包的人应轮换受影响的加入密钥。

若干相关变更仍是开放提案，尚未合并或发布。就存储的密钥而言，其中一项将通过现有迁移路径[把网络加入密钥保存在平台密钥存储中](https://github.com/mmalmi/nostr-vpn/pull/120)。另一项将[把 Windows 机器 sidecar 密钥的访问权限限制为 SYSTEM 和 Administrators](https://github.com/mmalmi/nostr-vpn/pull/101)，涵盖存放 Nostr 节点密钥的 DPAPI 文件。该限制只会在下一次写入文件时生效，且文件创建与 ACL 设置之间存在短暂空档。自定义配置路径不在覆盖范围内，作者也没有在多用户 Windows 机器上测试。签名成员资格方面，一项提案将[拒绝名册快照已与磁盘不一致的加入批准](https://github.com/mmalmi/nostr-vpn/pull/117)，让管理员重新加载后重试，同时保留同期已获批准的设备。另一项将[允许管理员时钟存在五分钟偏差，并始终要求配置加入签名者](https://github.com/mmalmi/nostr-vpn/pull/111)，即使本地管理员列表为空也是如此，同时保留与请求密钥的绑定。第三项将[以制品哈希打破时间戳相同的名册之间的平局](https://github.com/mmalmi/nostr-vpn/pull/109)。同时看到两个名册的对等节点会选择同一个名册；每个名册各自保留其成员内容。最后一项提案将[要求对深度链接加入请求和付费出口提供商进行确认](https://github.com/mmalmi/nostr-vpn/pull/110)。在 macOS 和 Linux 上，加入链接将等待明确的“添加设备”（Add-device）步骤。macOS 还会暂缓付费提供商链接，等待确认。在这两个平台上原生运行的情况尚未得到演示。所有测试结果均由作者报告。

### Buzz {#buzz}

[Buzz](https://github.com/block/buzz) 是一个带有桌面和移动客户端的社区 relay，合并了群组和代理（agent）相关工作。代理可以依据该项目的 [NIP-FI](/zh/topics/nip-fi/) [JWT 规范](https://github.com/block/buzz/pull/8401)进行身份验证，该规范会验证由签发方声明的人类所有者；拒绝或断开该所有者会终止其代理的会话，而所有者的社区成员资格可以让代理获准加入。Huddle 还[接受已验证的托管代理记录](https://github.com/block/buzz/pull/8544)，这些记录来自当前用户或 Huddle 所有者，作为 [NIP-OA](/zh/topics/nip-oa/) 所有者证明机器人角色之外的补充。这一后备机制属于兼容性策略，不会信任未知的第三方记录。它并非身份证明。这两份规范都不是已被接受的 NIP。

[开放公告频道](https://github.com/block/buzz/pull/8143)可以通过 `join_role=guest` 接纳只读访客，而[不公开列出的开放频道](https://github.com/block/buzz/pull/8579)在非成员的发现功能中不可见，但任何持有频道 ID 的人都可以阅读。准入 event [最多可添加 100 名成员](https://github.com/block/buzz/pull/8575)，并可能出现部分成功。上周作为开放提案报道的[频道设置修复](https://github.com/block/buzz/pull/8516)现已合并：变更会与其请求和通知在同一个事务中提交。公开转私密的切换一旦失败会完全回滚，防止被移除的成员借由这次回滚重新出现。移动端方面，[推送设置失败](https://github.com/block/buzz/pull/8610)不再导致应用出错，应用会有限次数地重试并提供手动恢复；相关测试使用的是模拟通道，APNs 设备上的行为也尚未验证。[同步的静音设置不再导致启动白屏](https://github.com/block/buzz/pull/8608)，现在会对照实际的私信推送订阅进行检查；这项修复仅依据一份 iPhone 日志。在 relay 网格中，[失效的对等节点记录会在五分钟没有心跳后过期](https://github.com/block/buzz/pull/8503)，而活动连接不受此限。

较新的合并尚未确认已进入发布版本。[Kind 9000 成员添加](https://github.com/block/buzz/pull/8606)现在与其名册写入一同提交：变更失败时两者都不会被保存，同一个已签名 event 也可以重试。Kind 9001、9021 和 9022 仍存在原有缺口。[NIP-FI 影子模式诊断](https://github.com/block/buzz/pull/8634)现在会针对本应拒绝的情况记录已验证的 Nostr 密钥和一个固定的私有原因，但不会记录令牌或声明。这不会改变任何准入或执行行为。Buzz 自己的 [NIP-AP](/zh/topics/nip-ap/) [代理规范](https://github.com/block/buzz/pull/8631)是已接受 NIP 之外的项目文档，现在要求在设置中提供由客户端定义的 `agentType`。使用其他类型设置的启动会被拒绝，缺失该字段时沿用其旧有含义，而更改类型可能会丢弃旧类型的嵌套设置。遇到格式错误的最新 kind 30177 托管代理策略时，[单代理选择](https://github.com/block/buzz/pull/8616)会以失败关闭（fail closed）方式处理。较旧的数据仍被排除在外。它按所有者管理的名称标注代理，图像素材和消息作者则仍使用个人资料。

在移动端，[托管代理的创建、列出和删除](https://github.com/block/buzz/pull/8626)使用 NIP-OA 所有者证明和 kind 30177 注册，支持同一身份的持久化重试，并将私有指令保存在安全存储中。由于其构建时的托管开关在 App Store 版本和内部版本中均处于关闭状态，这并不代表已公开可用。[托管 iOS 邀请冷启动](https://github.com/block/buzz/pull/8617)会保留邀请意图，导入匹配的密钥并从备份中恢复。只有作者测试过主路径，成员资格后备端点和全新注册的问题仍未解决。[推送注册恢复](https://github.com/block/buzz/pull/8629)会先以指数退避等待，随后用一个有限度的全新质询和 App Attest 密钥替换被 401 拒绝的已保存请求。遇到 400 或暂时性错误时，它会保留意图，普通的 404 则按常规处理。这项恢复尚未在真机上检查。对于用户尚未加入的公开频道，[消息链接](https://github.com/block/buzz/pull/8518)会获取 kind 39000 元数据并以只读方式打开，私有频道和私信的访问限制保持不变。重连期间链接会排队，一次缓慢的查询可能让后续链接最多延迟八秒。

截至我们的资料截止时间，有几个开放的 pull request 尚未合并。其中一项默认禁用的 `buzz_v1` 能力将用[仅调用者可见的 NIP-98 侧边栏、已读状态和覆盖范围 API](https://github.com/block/buzz/pull/8639) 取代客户端的已读状态，同时加入按人记录的修订版本，以及仅限 relay 的 kind 24300 失效通知 ping。不具备该能力的 relay 继续使用 [NIP-RS](/zh/topics/nip-rs/)；大型数据库则必须先以并发方式构建索引。[话题摘要](https://github.com/block/buzz/pull/8635)只会扫描最新的 1,000 条回复，返回最近的 10 位作者，且每个 pod 每秒最多发送一次实时更新，因此不会列出所有过往参与者。智能体对 reaction 的回应将[以话题形式挂在被回应的消息下](https://github.com/block/buzz/pull/8642)，所用的是最后一个有效的 [NIP-25](/zh/topics/nip-25/) `e` tag，并可回退到旧锚点。基于 Hermes 的智能体将获得[一个限定于智能体范围、用于向频道和私信发帖的 MCP shell](https://github.com/block/buzz/pull/8643)。缺少其 bridge 时它会拒绝运行，并会遮蔽凭据，但安装、重启和实际发帖均未经验证。一项 [ACP 适配器修复](https://github.com/block/buzz/pull/8625)将同时发送 v1 和 v2 初始化名称，回退到稳定的 v1，并固定已验证的主版本号。它修复的是智能体传输，并非 Nostr 协议变更。移动端的[朗读](https://github.com/block/buzz/pull/8637)功能将调用手机的文本转语音引擎，并跳过代码、链接和附件。语音在何处处理，取决于用户所选的引擎。还有一个独立的 [relay 负载生成器](https://github.com/block/buzz/pull/8636)，它将模拟人类用户和 NIP-OA 智能体，凡是超出设定错误率与延迟上限的运行都会被判定为失败。它不改动任何 relay 代码，也不能证明生产规模下的表现。

### Mosaico {#mosaico}

[Mosaico](https://github.com/pablof7z/mosaico) 是一个在[基于 relay 的群组（NIP-29）](/zh/topics/nip-29/)中协调智能体的守护进程，它合并了[基于心跳的在线状态](https://github.com/pablof7z/mosaico/pull/847)。现在，智能体只有在持续发布带[过期时间戳（NIP-40）](/zh/topics/nip-40/)的状态 event 期间，才算在频道中在线；该时间戳设为 90 秒之后，每 30 秒续期一次。仅凭本地运行的进程，不再算作在线。智能体离线期间成员身份会保留，因此它可以恢复。[重建的群组读取模型](https://github.com/pablof7z/mosaico/pull/845)在每次 relay 变更时构建一次，并采用规范的到达游标，所以替换宽范围的群组订阅时，聊天消息不会再丢失。

随后的三项合并尚未确认已进入某个发布版本。[替换订阅](https://github.com/pablof7z/mosaico/pull/854)现在使用新的 REQ ID，并在关闭旧订阅之前先打开。已退役的 profile 会在延迟关键路径之外发布；离开频道的智能体会趁自己仍是 NIP-29 成员时撤回其在线状态。相关的佐证探测由作者完成，并非我们的测量。[先认领后重试的计数](https://github.com/pablof7z/mosaico/pull/851)持久存储在 schema 27 中，relay 重放后依然保留。它在单个串行计时器上按指数退避，间隔从 30 秒增至一小时，失败 10 次后放弃。缺失的 event 不会被当作删除处理；而由于保留窗口只容纳 4,096 个条目，无法保证每个 event 都能送达。[仅含群组的快照](https://github.com/pablof7z/mosaico/pull/852)现在会唤醒群组消费者；时间戳相同的替换则按 [NIP-01](/zh/topics/nip-01/) 的规定，保留 event ID 最小的那个。仅涉及内容的变更仍会唤醒通用消费者。父项缺失时，限定范围的回退可能要等到下一次群组变更或 15 秒超时。

### Sonar {#sonar}

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar) 是一款结合 Nostr、MLS 加密和低功耗蓝牙 mesh 的即时通讯应用，它合并了[针对蜂窝网络连接的启动修复](https://github.com/hedwig-corp/bitchat-to-sonar/pull/665)。该 PR 将首次绘制缓慢追溯到推送 relay 挂接时占用了存储锁。在 Android 上，如果本地节点已经打开（例如推送注册在冷启动前就已将其打开），启动过程会跳过该锁。在 iOS 上，应用会通知 notification service extension 停止连接和排空，好让应用完成渲染。

### Shopstr {#shopstr}

Nostr 市场 [Shopstr](https://github.com/shopstr-eng/shopstr) 合并了[商品信息删除支持](https://github.com/shopstr-eng/shopstr/commit/2e11d0b6d7b8d5d3007c5393882a77dc2f0721e2)，该功能于[上周提出](/en/newsletters/2026-10-21-newsletter/#shopstr)。卖家签名的 [event 删除请求（NIP-09）](/zh/topics/nip-09/)现在会把该商品信息从缓存中移除并打上墓碑标记，这样已删除的商品既不会重新出现，也无法从缓存中被购买，而更新的重新上架仍会显示。部分删除仍会被遗漏：先于商品信息到达的删除会被忽略，不带 `k` tag 的旧请求无法匹配 relay 查询，过去的删除也不会回填。relay 也可能保留已删除的 event。另外，[格式错误的 gift-wrapped 消息](https://github.com/shopstr-eng/shopstr/pull/614)不会再让“订单”和“我的商品”视图卡住；[卖家现在可以查看自己的订单](https://github.com/shopstr-eng/shopstr/pull/652)，其他用户仍会收到 403。

另有三个针对订单完整性的开放 pull request，截至我们的资料截止时间尚未合并。[#665](https://github.com/shopstr-eng/shopstr/pull/665) 将通过 NIP-98 注册一次性记录每个订单的参与者：买家取自身份验证，卖家取自签名的商品信息，之后的写入无法再更改。注册失败不会阻止结账，新的未解析订单也不会根据 tag 去推测。旧订单只覆盖到某个有限的截止点为止，而按订单 ID 存储状态的方式中有一处缺口仍未修复。[#666](https://github.com/shopstr-eng/shopstr/pull/666) 依赖 #665，它只会在 gift-wrapped（[NIP-59](/zh/topics/nip-59/)）订单状态消息来自该订单所记录的买家或卖家时才应用这些消息，而不是来自任何通过身份验证的发送者都行。未解析的订单保持待处理状态，买家付款后的确认不算作卖家确认，伪造的消息只作为聊天保留，不会改变订单状态。[#664](https://github.com/shopstr-eng/shopstr/pull/664) 将在托管注册和裁决中读取 Cashu v2 keyset token 元数据，无需通过网络查询 keyset，并会修正 proof 总额。创建订单时的 token 解码仍需另行修复。

### Conduit {#conduit}

[Conduit](https://github.com/Conduit-BTC/conduit-mono) 是一个配有成对的买家应用和商家应用的 Nostr 市场，它合并了[单一加密账户记录](https://github.com/Conduit-BTC/conduit-mono/pull/711)。钱包元数据、种子、原生身份、地址、偏好设置和设置进度现在都存放在同一条[任意自定义应用数据（NIP-78）](/zh/topics/nip-78/)记录中。该记录使用[带版本的加密载荷（NIP-44）](/zh/topics/nip-44/)加密，并会校验签名、所有者和派生身份；签名器批准后，两个应用都能找到它。此次切换不向后兼容：旧的备份和恢复路径会被忽略，旧备份原地保留，不会自动迁移。其他合并新增了[使用现有 nsec 登录](https://github.com/Conduit-BTC/conduit-mono/pull/646)（保存在浏览器本地存储中），要求在编辑产品系列时提供[精确的已签名配送条款](https://github.com/Conduit-BTC/conduit-mono/pull/647)，并[将结账恢复数据移至 IndexedDB](https://github.com/Conduit-BTC/conduit-mono/pull/708)，标记为已保存之前会先回读确认。

Conduit 还[升级到了 NWC SDK 8.1.1](https://github.com/Conduit-BTC/conduit-mono/pull/740)，从而获得该版本的金额验证、有上限的连接尝试、已关闭连接池的处理，以及进行中响应的修复。Conduit 的钱包选择、加密和支付策略均未改变。应用部署仍未确认。截至我们的资料截止时间，两个草稿 pull request 仍未合并。[支付激活](https://github.com/Conduit-BTC/conduit-mono/pull/743)将在固定的两分钟执行窗口内持久化、回读并传递支付状态，重试不会重置这个窗口。Nostr 收据、私密账户恢复以及库存或履约变更，各自都需要单独的签名证据。事后保留 24 小时的收据并不会恢复支付授权；使用真实资金的检查、设备检查和维护者检查也都还未完成。[仅限活动使用的商品](https://github.com/Conduit-BTC/conduit-mono/pull/741)将把 [NIP-99](/zh/topics/nip-99/) kind 30402 商品信息标记为隐藏，所用的是 `conduit_event_only` 扩展。这类商品不会出现在常规目录和结账流程中，并且需要精确且经授权的活动场次分配。被隐藏的签名数据仍是公开的，其他客户端只支持标准的隐藏标记。

### LNbits {#lnbits}

Lightning 钱包与账户服务器 [LNbits](https://github.com/lnbits/lnbits) 合并了[一个将其 Nostr 通知以 NIP-17 私信发送的选项](https://github.com/lnbits/lnbits/pull/4260)。管理员可在旧版 [NIP-04](/zh/topics/nip-04/) 加密消息和 [NIP-17](/zh/topics/nip-17/) 私密直接消息之间选择，新设置默认使用后者。使用 NIP-17 时，服务器会查找接收者的私信收件箱 relay 列表；NIP-05 relay 被用作发现线索，在列表不存在时也作为发送目的地。已发布的空列表会导致发送失败。每次发送限时 30 秒，至少要有一个收件箱 relay 接受才算成功，而且绝不会回退到 NIP-04。

### Zeus {#zeus}

[Zeus](https://github.com/ZeusLN/zeus) 是一款移动端 Bitcoin 和 Lightning 钱包，它把[付款后刷新失败时 Nostr Wallet Connect 预算计算的修复](https://github.com/ZeusLN/zeus/pull/5389)纳入了 [v13.2.4-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.2.4-rc1) 预发布版，一同纳入的还有先前那项[让 Nostr Wallet Connect make_invoice 返回其自身发票](https://github.com/ZeusLN/zeus/pull/5316)的修复。在这项修复之前，[NIP-47](/zh/topics/nip-47/) 发送后若刷新出错，就会跳过预算计算，并对一笔可能已经成功的付款返回错误。现在，返回的 preimage 会通过现有的回退机制从预算中扣除；若发生超时，即使列表中找不到这笔付款，该金额也会作为待处理支出保留。其他缺口可能依然存在，包括进行中的 LND 付款。随后发布的 [v13.2.4-rc2](https://github.com/ZeusLN/zeus/releases/tag/v13.2.4-rc2) 只包含依赖更新。

此后，又有两项较新的修复合并到了源代码中，但尚未确认包含在任一候选版本里。[默认过期时间修正](https://github.com/ZeusLN/zeus/pull/5394)让本地 BOLT11 解码器在发票缺少过期字段时，采用规范规定的 3600 秒默认过期时间。此类发票过去被视为永不过期，因此阻止支付过期发票的检查对它们不起作用，`NostrConnectUtils` 中的 NWC 发票验证也存在同样的缺口。[按钱包划分的备份修正](https://github.com/ZeusLN/zeus/pull/5191)会为每个 ecash 钱包分别重置 Nostr mint 备份时间戳。在此修复之前，若一个钱包与另一个 ecash 钱包在同一会话中从种子恢复，它可能会继承那个钱包的时间戳。接着，它可能把自己较早的 relay 备份当作过时数据丢弃，并保存一个空的 mint 列表，自动恢复也就因此被关闭。切换钱包之后才完成的备份，仍可能把时间戳写到错误的钱包名下。已受影响的钱包会保留已保存的空列表，需要在 Mint sync 中手动恢复，或者重新添加各自的 mint URL。这些钱包的 ecash 仍留在 mint 处。两个 pull request 都表示未进行设备测试。

### npub.cash {#npubcash}

[npub.cash](https://github.com/cashubtc/npubcash-server) 为 Nostr 身份接收 Lightning 付款，并将其转换为 Cashu ecash。它合并了[一项服务器端变更，把 zap 收据发布到付款人请求的 relay](https://github.com/cashubtc/npubcash-server/pull/67)。服务器原本就会解析 zap 请求中指定的 relay，但发布已支付收据时却忽略了它们。现在，只要请求至少指定了一个 relay，收据就会发往这些 relay；relay 列表缺失或为空的请求，仍使用配置的默认 relay。

### eHagaki {#ehagaki}

[eHagaki](https://github.com/Lokuyow/ehagaki) 是一款 Nostr 网页客户端，同时也以可嵌入的 Web Component 形式提供，它发布了 [1.31.0](https://github.com/Lokuyow/ehagaki/releases/tag/v1.31.0) 和 [1.31.1](https://github.com/Lokuyow/ehagaki/releases/tag/v1.31.1)。1.31.0 版新增了转发（[NIP-18](/zh/topics/nip-18/)）、reaction（[NIP-25](/zh/topics/nip-25/)）和已上传媒体管理；它会在 event 交给外部签名器之前先确定 outbox 路由（NIP-65），还可将帖子历史和缓存保存在本地 Citrine relay 中。其 IndexedDB 迁移会重置本地显示的帖子历史，但保留草稿和已保存的删除请求。存放在 relay 上的历史可以重新获取，仅存于本地的帖子则需要在升级前备份或导出。1.31.1 版通过 kind 10096 同步 [NIP-96](/zh/topics/nip-96/) 上传服务器，与 Blossom 的 kind 10063 并行；它会保留可用的部分 relay 设置，并带有上传服务器列表和媒体服务器同步的修复。[上传服务器列表获取](https://github.com/Lokuyow/ehagaki/pull/366)经由声明的读取 relay 进行，即使其他 relay 超时，也会保留最新的有效签名列表；如果一个列表都没收到，设置则保持不变。[媒体服务器同步](https://github.com/Lokuyow/ehagaki/pull/364)分别处理 Blossom 和 [NIP-96](/zh/topics/nip-96/) 偏好设置，查找失败后绝不会发布缩短的列表。

其他已合并的可靠性修复尚未确认进入任何发布版本。遇到 401 或 403 后，用户可以[在媒体界面向 yabu.me 或 nostrcheck.me 的 NIP-96 服务器注册](https://github.com/Lokuyow/ehagaki/pull/374)；NIP-98 签名覆盖实际的 POST URL 和正文哈希，账户或目标一旦变更，请求就会被取消，防护机制可阻止重复发送，结果未知的请求也不会重新发送。eHagaki 从不代为提供密码，邀请码或付款步骤会转到服务商的官方网站。[大型 Blossom 文件列表](https://github.com/Lokuyow/ehagaki/pull/363)从一个有界的本地快照中每次分页加载 24 项，拒绝超过 8 MiB 或 10,000 个条目的响应，并在账户、会话或服务器变更时丢弃该快照；到达末尾意味着快照已用尽，而不是服务器上没有更多文件。[NIP-46 远程签名器恢复](https://github.com/Lokuyow/ehagaki/pull/355)会重建连接，并在 30 秒后明确拒绝旧的待处理请求，不会重新发送。[上传到 Primal 的 Blossom 服务器](https://github.com/Lokuyow/ehagaki/pull/367)时，现有的已签名授权会被编码为带填充的标准 Base64，其他服务器则继续使用 Base64URL。

另有两项较新的合并同样尚未确认进入发布版本。[发布](https://github.com/Lokuyow/ehagaki/pull/393)现在共享有界且经过验证的 relay 请求等待，并将投递和进度与会话绑定，取代了此前多个独立的计时器。首个有效的 relay 确认即视为成功，同时继续向其余 relay 投递。进度从不声称已投递到每个 relay，切换账户或退出登录则会停止后台投递。帖子历史可以按需[刷新相关的回复、反应和删除](https://github.com/Lokuyow/ehagaki/pull/391)，时限为三秒。发生部分超时后，已收到的结果会被保留；某条删除未到达，并不会被视为不存在删除的证明。

### Formstr Drive {#formstr-drive}

Formstr Drive 是一款基于 Nostr 和 Blossom 构建的加密文件共享应用，它[合并了 DriveKey 恢复工作](https://github.com/formstr-hq/formstr-drive/commit/e7f8c00583dc746e4a69b9ce4c97f8c3e1af851f)，我们此前曾将其作为一项尚未合并的提案报道。该应用在写入合并后的密钥环之前，会读取所有可达的 relay，因此旧密钥会随着逐渐可见而汇合到一起。只有当四个应用 relay 中有两个没有返回任何内容、且不存在历史记录或版本时，它才会创建新密钥。未响应的写入 relay 仍可能在一段时间内隐藏某个旧密钥，而较旧的构建无法读取新的 JSON 格式。

该项目还[将每个账户解密后的文件、共享、文件夹和发件箱彼此隔离](https://github.com/formstr-hq/formstr-drive/pull/85)。切换账户会阻止上一个账户待处理的签名和导入，不过已暂存的 blob 可能会处于无引用状态。[新账户现在必须明确选择上传服务器](https://github.com/formstr-hq/formstr-drive/pull/88)，不会静默故障转移，而早先的自动默认设置会被保留。服务器仍能看到 pubkey、上传时间和加密字节。[重复警告现在要求同一服务器和同一文件夹中存在完全相同的现存字节](https://github.com/formstr-hq/formstr-drive/pull/89)。账户隔离和重复确认的 Android 路径尚未测试，我们也未确认其中任何内容已进入发布版本。

### diVine {#divine}

diVine 是一款面向 Nostr 的短视频客户端，它合并了消息、账户和挑战相关的更改。其早期 beta 版本只有笼统的发布说明，因此无法确定这些内容已进入已发布的构建。[按字段加密的账户快照](https://github.com/divinevideo/divine-mobile/pull/10413)会同步偏好设置、徽章决定和忽略操作，在本地重试待处理的更改，并在读取不完整时阻止不安全的发布。DM 已读标记沿用现有协议，通知已读状态使用服务器 API，“全部标为已读”需要网络连接；系统权限、凭据和年龄同意保留在设备上。

在 DM 中，[消息一旦安全进入队列，编辑器和分享面板就会关闭](https://github.com/divinevideo/divine-mobile/pull/10500)；应用被终止时，后台投递不会运行，而且只有在 relay 确认后才算完成投递。[失败的重试会一致地计入尝试次数上限](https://github.com/divinevideo/divine-mobile/pull/10346)。[格式无效的旧版 NIP-04 消息会被丢弃并记录在台账中](https://github.com/divinevideo/divine-mobile/pull/10522)，不过已存储的空消息气泡仍会保留，与外部签名器及其他设备的兼容性也尚未确定。[来自受信任发送者的视频 DM 的可选模糊预览](https://github.com/divinevideo/divine-mobile/pull/10437)默认关闭，且始终经过模糊处理并附带内容警告；视频仍会下载，因此模糊并不提供网络隐私。在群组中，[屏蔽某个成员只会隐藏其消息](https://github.com/divinevideo/divine-mobile/pull/10156)；警告会提示对方仍能收到你的消息。离开房间的状态会被保存并持续生效。新建群组仍受一个默认关闭的标志控制。这些更改适用于现有群组；信任与安全审查尚待进行。

两项此前尚未合并的功能现已合并。[已接收 DM 视频缓存](https://github.com/divinevideo/divine-mobile/commit/25f9b7b8783ce11d70fc965936d1939b50f5f198)按账户保存解密后的文件，最长 30 天或最多 300 MB；在受信任聊天中以及来自已关注用户的自动加载会向媒体主机暴露观看时间，陌生人的视频则需要点击才会加载。服务器下架内容并不会立即撤销已缓存的字节，不过这些字节可能会更早被清除。[用户名所有权查询](https://github.com/divinevideo/divine-mobile/commit/489231071520bd066636384f4dd2a8e6d88f3f96)会针对第一页的 Divine 用户名搜索检查名称服务器的 NIP-05 目录，并且只置顶当前有效的所有者；查询的名称会出现在服务器日志中，而且这并非通用的 NIP-05 验证。

[人员列表进入全面可用阶段](https://github.com/divinevideo/divine-mobile/pull/10415)，这建立在[发现与管理一体化工作](https://github.com/divinevideo/divine-mobile/pull/9742)的基础之上。个人资料中的支持链接默认开启，编辑器会等待从每个 relay 严格读取原始 kind 0，从而保留隐藏的提供方和未保存的编辑；通过应用商店渠道推送该构建以及后端上线均尚未进行。[客户端归属 tag 在重试和元数据编辑时遵循当前的 NIP-89 偏好设置](https://github.com/divinevideo/divine-mobile/pull/10387)，签名前会移除外来客户端 tag，而已签名的定时帖子永远不会改变。[经过身份验证的外部短链接](https://github.com/divinevideo/divine-mobile/pull/10507)默认关闭，会在两秒内对精确的 NIP-98 POST 和正文签名，并回退到规范 URL，而 DM 和 Nostr event 始终保留规范 URL；网关创建功能已部署但处于关闭状态，后续还有若干上线门槛。

创作者可以[通过显式 tag 允许他人重用公开视频](https://github.com/divinevideo/divine-mobile/pull/10467)，该功能默认关闭，若使用了禁止演绎许可的音频，则会在发布时被锁定为关闭；这是一种客户端约定，并非 DRM。仅限测试的挑战工作涵盖[签名协议基础](https://github.com/divinevideo/divine-mobile/pull/10374)、[带规则与同意检查的参赛作品签名](https://github.com/divinevideo/divine-mobile/pull/10503)、[持久的按账户存储](https://github.com/divinevideo/divine-mobile/pull/10509)以及[原生审核与撤回流程](https://github.com/divinevideo/divine-mobile/pull/10515)，均位于特殊测试构建中。Relay 确认并不代表组织者批准。生产环境中的发现功能已禁用。后端交付、真实账户验收测试以及跨客户端发布顺序仍有待完成。

较新的合并同样尚未确认进入发布版本。当无法读取收件人的 kind 10050 DM 收件箱时，[NIP-17 暂存发送队列](https://github.com/divinevideo/divine-mobile/pull/10531)现在会复用某个 relay 已接受的收件人 gift wrap 的 ID，从而在多次重试中保持该 wrap 的身份不变。如果某次重试找到了收件箱，客户端可以重新发布到其公布的 relay。如果始终找不到收件箱，它就以已被接受的副本为准，并依赖 relay 保留该副本。消息仍可能显示为“失败”。收件人是否收到或阅读仍未得到证实；反应和删除的重试不在此次更改范围内。[公开通知预加载和时区刷新](https://github.com/divinevideo/divine-mobile/pull/10460)使用有界的缩略图缓存和共享的 SQLite 索引，不包括 DM 和活动（campaigns）。它们需要一次常规的原生版本发布以及一次协调的服务端变更，而且后台执行无法保证。视频编辑器新增了[五种转场](https://github.com/divinevideo/divine-mobile/pull/10543)，总数达到 20 种，在预览和导出中均以原生方式渲染。“减少动态效果”会有意限制预览图块。闪光间隔可能回退为溶解效果。我们没有对原生实现进行实地测试。

截至我们的资料截止时间，有四个拉取请求仍处于开放状态、尚未合并。[社交视频贴纸](https://github.com/divinevideo/divine-mobile/pull/10540)叠加在早先的信息贴纸工作之上，将写入带有提及（`p`）、话题标签（`t`）和链接（`r`）元数据的小型扁平贴纸 tag。播放器会叠加可点击区域，并在打开外部链接前发出警告。除非其他客户端实现这些 tag，否则它们只能看到烧录在视频中的贴纸，而这些 tag 并非已被接受的 NIP。[受功能标志控制的 Concord 聊天](https://github.com/divinevideo/divine-mobile/pull/10536)中的提及会将身份保留在经过身份验证的加密消息内。应用内提醒只会来自用户已打开的房间中已关注且未被屏蔽的发送者，上限为 50 行，并保存已读状态。它们不会触发系统推送通知，也不会带来公开聊天的上线；身份冲突、重放和屏蔽检查仅由范围有限的测试覆盖。[NIP-17 rumor tag](https://github.com/divinevideo/divine-mobile/pull/10534) 会只列出一次反应作者，并使用实际的 kind，而封装的删除将去掉具有误导性的 `p` tag。Gift wrap 本来就已发往正确的收件人，因此这并不是在修复收件人泄露问题。已在队列中的 rumor 保持不变，在其他客户端中的行为尚未测试，房间归档方面的权衡依然存在。[下一个原生构建](https://github.com/divinevideo/divine-mobile/pull/10532)将默认开启现有的短链接分享功能，网页版则仍保持关闭。在禁用、未登录和出错的路径下，将保留完整的规范 URL。应用商店分发、服务就绪情况和设备检查均未得到证实。

### rust-nostr {#rust-nostr}

rust-nostr 是一组用 Rust 编写的 Nostr 协议库，它合并了一项[关于订阅重新发出方式的破坏性变更](https://github.com/nostrdevkit/nostr/pull/1495)。`SubscriptionData` 现在会显示每个 relay 当前的 EOSE 状态。重新发出订阅时，会在一个原子步骤中将 CLOSE 和基于已存储过滤器的 REQ 加入队列，即使在断开连接时也是如此；这保证了它们的入队方式，但不保证两个帧都能到达 relay。从通知间断中恢复时，不再会静默丢弃订阅或发送重复请求。来自先前 REQ 的迟到 EOSE 消息或 event 仍可能与新的 REQ 重叠，因为线路上没有任何信息能将它们区分开来。这是已合并的源码，我们尚未确认它已进入发布版本。

### nostr-sdk-ffi {#nostr-sdk-ffi}

nostr-sdk-ffi 是让其他语言能够使用 rust-nostr SDK 的绑定库，它合并了[对 NIP-44 v2 会话密钥的原始访问](https://github.com/nostrdevkit/nostr-sdk-ffi/pull/96)，因此 Concord 宿主不再需要自带 ECDH 和 HKDF 代码。它只是对现有派生逻辑的轻量封装，没有添加新的密码学实现。作者报告了一次 Python 构建，以及一次双方得出相同密钥的往返测试，但没有添加专门的单元测试。这仅是已合并的源码。

### NDK {#ndk}

NDK 是一个面向 Dart 的 Nostr 开发工具包，它发布了 [0.11.0-dev.2](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.2)，这是一个包含破坏性变更的预发布版本。它并非稳定版 0.11.0，且与 JavaScript 版 NDK 无关。该版本新增了 [NIP-49](/zh/topics/nip-49/) [密码加密的 ncryptsec 密钥及示例 UI](https://github.com/relaystr/ndk/pull/896)。其发布说明称，解密会限制 logN 的范围、拒绝未知的安全字节，并将派生缓冲区清零；这些说法依据的是发布说明和已合并的源码，我们尚未见到独立审计或测试向量运行结果。[请求现在会报告 notSent 结果，其中携带连接或发送失败信息](https://github.com/relaystr/ndk/pull/911)；发往不可达 relay 的请求会在没有剩余 relay 或过滤器能够应答时结束，而无需等到超时。[广播会在将 event 标记为传输中之前检查是否存在签名器](https://github.com/relaystr/ndk/pull/908)，[zap 请求 ID 使用已存储的 created_at](https://github.com/relaystr/ndk/pull/907)，并且 [NIP-11](/zh/topics/nip-11/) [relay 元数据会通过共享缓存按需获取](https://github.com/relaystr/ndk/pull/887)，因此不再阻塞每次同步。

该预发布版本还包含此前仅存在于源码中的更改。[重复出现同一 relay URL 的 NIP-65 列表现在能被正确合并](https://github.com/relaystr/ndk/pull/914)，读取和写入标记会被合并，outbox 写入 relay 集合也会得到保留；作者在一次观察中发现，932 个个人资料中有 5 个列表被误读。[可选的 BUD-06 上传预检](https://github.com/relaystr/ndk/pull/902)会使用该上传自身的授权询问服务器是否会接受某个 blob，并报告状态和原因，真实的上传拒绝现在也会这样报告。404 表示支持情况未知，而通过预检并不保证上传一定成功。一项[针对 NIP-77 协调超时的破坏性变更](https://github.com/relaystr/ndk/pull/888)将单一超时拆分为打开超时和空闲超时，并提供类型化错误，且不计入等待身份验证所花的时间。由于没有总体截止时间，持续取得进展的同步可能无限期运行，我们也尚未看到该变更在实际 relay 上得到验证。

尚处于开放状态的 pull request 提出了[以标识符为键、带否定缓存的 NIP-05 缓存](https://github.com/relaystr/ndk/pull/937)、[为 NIP-77 返回 ID 和时间戳的缓存 API](https://github.com/relaystr/ndk/pull/933)、[WebSocket 就绪状态处理](https://github.com/relaystr/ndk/pull/932)、[完整的 NIP-11 字段](https://github.com/relaystr/ndk/pull/931)，以及[连接被拒绝时的完成处理](https://github.com/relaystr/ndk/pull/930)。另有一项提案在最新的状态检查中仍未关闭，它将借助[浏览器和 Flutter 平台的 passkey](https://github.com/relaystr/ndk/pull/909) 创建和恢复账户。该提案遵循一份 passkey 身份设计草案，草案包含派生和存储两种密钥模式，以及显式的旧版元数据。未知的句柄会被拒绝，绝不会被当作新账户；在保留已存储的注册信息之前，恢复必须经过独立验证。作者指出，互操作性尚未在所有 passkey 提供方之间得到验证。

### Applesauce {#applesauce}

Applesauce 是一套面向 Nostr 的 TypeScript 库。它有了附带 changeset 的新源码变更，但我们并不声称存在相应的发布版本。[独立消息客户端与显式 relay 认证](https://github.com/hzrd149/applesauce/commit/a4f50406cdd625534a486b7d47369d59d004a24f)新增了面向固定账户的 NIP-04 和 NIP-17 客户端，它们会发出显式的 NIP-42 认证请求，并重试已准备好的签名发送。借助[限定作用域的封装会话与 rumor 存储](https://github.com/hzrd149/applesauce/commit/056038ed7108c3f113035a06011a5f7acdf8365f)，kind 14 rumor 和对话线程模型得以暴露，且不会启动签名器或网络操作。解密默认关闭。封装发送要求包括发送者在内的每位参与者都有 kind 10050 relay，而 relay 接受并不等于对方已接收。[有界的解密内容缓存恢复](https://github.com/hzrd149/applesauce/commit/d6ac42102747feb72372ac5970ce2743e4b685ca)默认并发数为 8，除非设为 1，否则可能打乱 event 的顺序。这些明文缓存的作用域限定和加密必须由应用自行完成。随后还有 [NDR 传输层以及一个独立的 Cordn 协调器客户端](https://github.com/hzrd149/applesauce/commit/907a9591de867899aa7c84de1c4aa40628307a17)。NDR 必须持久化其自身独立的 ratchet 状态；Submitted 表示本地交接，并非对方已接收。Cordn 只负责传输，在示例中已被搁置，也没有实现 MLS。[按窗口的 Kehto ContextVM 集成](https://github.com/hzrd149/applesauce/commit/24ad6e9650e20cc92950c3fccbc0ac0263f6d443)为每个 napplet 窗口赋予一个临时的 ContextVM 身份，不涉及账户认证或支付。有了[持久化、归应用所有的存入与 nutzap 恢复](https://github.com/hzrd149/applesauce/commit/cd483f5a610bf6fe8be7719ae5bb0dd0638c3296)之后，新的钱包存入和兑付需要由使用方应用提供的恢复存储，以及 mint 端的 NUT-09 恢复。该日志会持久化可花费的 proof、secret 和致盲因子，因此应当加密并按账户限定作用域。Resume 仅在被显式调用时运行，它会复用已签名的 ID，并在 relay 明确接受之前一直保留日志；取消操作不会使发票失效。[批量时间线快照与同步钱包状态](https://github.com/hzrd149/applesauce/commit/1042bc595c35cb6199a76776daab482916beda57)以 16 毫秒为窗口对时间线更新进行分组，钱包 token 状态则保持同步。[COUNT 请求调度器](https://github.com/hzrd149/applesauce/commit/564643fd648f5456387b54b3c8eddb79f165f46b)于[上周提出](https://github.com/hzrd149/applesauce/pull/106)，现已合并。在并发上限的约束下，它从 8 开始并持续翻倍，直到首次出现速率限制或传输错误为止；每次错误都会将上限减半，并加入一段冷却时间。超时会以 CountFailure 的形式呈现，但不会降低上限。延迟仅用于指导 relay 的选择；基于三个 relay 的基准测试仍不足以支撑一般性的性能结论。

### eventstore {#eventstore}

[eventstore](https://github.com/fiatjaf/eventstore) 是 fiatjaf 开发的 Nostr event 存储后端库，它合并了两项查询修复。目前尚未核实有包含这些修复的带标签发布版本。所有后端现在都遵循 [NIP-01](/zh/topics/nip-01/) 关于[空过滤列表](https://github.com/fiatjaf/eventstore/pull/79)的规则：空的 ids、authors、kinds 或 tag 列表不匹配任何内容，而缺失（nil）的 tag 列表仍然不施加任何限制。一项[针对 LMDB event 计数的修复](https://github.com/fiatjaf/eventstore/pull/78)会在匹配后将 HyperLogLog 游标向前移动，因此计数不再会永远挂起。此外，当过滤器中没有作者、kind 或 tag 条件时，计数也不再执行相应检查；此前这些检查曾导致其返回零。

### zsp {#zsp}

zsp 是 Zapstore 用于将 Android 应用发布到 Nostr 的命令行工具，它[发布了 2.0.0 版](https://github.com/zapstore/zsp/releases/tag/v2.0.0)。[该标签下的 README](https://github.com/zapstore/zsp/blob/v2.0.0/README.md) 提供了一个向导，由人来证明对 C1 签名证书的所有权；此外还提供了一个 `zsp skill` 命令，用于向智能体给出发布说明。README 禁止向智能体提供 keystore、其密码或任何私钥，从而确保这项证明始终由人完成。该版本还会[根据内容识别 JKS 和 PKCS12 keystore](https://github.com/zapstore/zsp/commit/f767a1c4c98ba7130dd355f8da95afde6eeb8e08)，因此命名为 .jks 或 .keystore 的 PKCS12 存储在向导和发布流程中都能加载。我们没有用它测试发布。

### nsite-gateway {#nsite-gateway}

nsite-gateway 用于提供发布在 Nostr 上的静态网站，它[发布了 3.6.6 版](https://github.com/hzrd149/nsite-gateway/releases/tag/v3.6.6)。这次[源码变更](https://github.com/hzrd149/nsite-gateway/commit/e7bbff215e23c0f3d9e23ee0ca14f5a2fb5e62dd)升级到了 Applesauce 7，并恢复了 event 过期机制。为了规避上游的一个计时器钳制缺陷，早期版本特意换用了一个被禁用的过期管理器，导致已过期的站点 event 可能无限期地在网关存储中保持有效。上游修复到位后，网关重新使用常规的 event 存储。这里的过期只决定网关保留和提供哪些内容，并不会从 relay 或第三方缓存中删除 event。我们没有测试已部署的网关。

### 44billion {#44billion}

Nostr 应用启动器 44billion [改变了记忆权限的方式](https://github.com/44Billion/44billion/commit/4eb2cd9beecd8bb209dc7db47e99f338aacc5ac9)。已保存的授权现在与应用、权限名称、event kind 和作用域绑定，通配的 kind -1 授权也不再授权具体的 kind。只有已注册且带有翻译标签的 kind 与作用域组合才具有细粒度作用域；未知作用域会回退为空的整个 kind 作用域，而注册表初始为空。IndexedDB 模式第 5 版会有意重置第 4 版的授权，并在启动时移除不受支持的作用域授权，同时保留其他应用数据。自定义的个人加密 API 包含 NIP-44 v3 风格的辅助函数，但它们并非已被接受的标准。这是一项源码变更，目前尚未发现相应的发布或部署。

更新的源码加入了[应用数据访问设置](https://github.com/44Billion/44billion/commit/9800ff204c3994c269b3dc7acdba8614a1819997)，按应用对已记住的授权进行分组，用户无需重新加载即可撤销单项授权或某个应用的全部授权。撤销只影响之后的受保护请求。已存储或已复制的数据不会被删除，正在进行的工作也可能不会被停止。根据一项 [Blossom 资源缓存变更](https://github.com/44Billion/44billion/commit/9bc2265a125a302ba61b09d13f52b2a8615218a9)，只有在整个内容主体的 SHA-256 校验通过、且已存储相匹配的已验证标记之后，缓存资源才会被视为完整。来自旧缓存的临时分块会被重新验证，流式传输也不再报告虚假的最后分块。这并不意味着验证之前不会暴露任何字节，而且目前没有新的二进制发布版本。

### Blossom Servers {#blossom-servers}

Blossom Servers 目录为每个服务器 URL [添加了社区能力报告](https://github.com/hzrd149/blossomservers/commit/b3546fb745c0859094157b0eb20e9b29fc2443a9)，每份报告都注明了贡献者。手动声明和浏览器观测结果分开保存，并分别在 90 天和 24 小时后从筛选中移除。检查内容包括 HTTP 响应和所声明的方法，以及认证和支付质询。匿名浏览器检查会发送一个 HEAD 请求，为一个 68 字节的 PNG 提出元数据，但不上传任何内容，因此返回 200 并不能证明真实上传可行。讨论内容的加载现在限定了范围，贡献者署名也取代了此前隐含的运营者权威。报告并不能证明谁在运营某台服务器，也无法说明全局可用时间或是否完全符合 BUD；贡献者之间可能意见不一，也可能出错。我们没有核实任何部署或发布。

更新的源码[加入了可配置的应用 relay 和查找 relay](https://github.com/hzrd149/blossomservers/commit/9ff8112963d68dee9c92d698740e47a23df7caf1)，并通过 NIP-65 读取账户和 outbox。已有的公开 kind 10086 查找列表优先。保存时，只有在公开列表已经存在的情况下才会更新它，否则只保存在本地。本地发布记录只有在至少一个 relay 确认该 event 后才会更新，但这并不意味着每个 relay 都收到了它。目前没有确认任何发布或部署。

### Ditto {#ditto}

Soapbox 推出的 Nostr 客户端 Ditto [修复了由异常 WebCodecs 编码器生成的 H.264 元数据](https://gitlab.com/soapbox-pub/ditto/-/commit/1c30cbac)，使转码后的视频能够在 iOS 上播放。它会检测 avcC 记录中重复的 SPS 和 PPS NAL 头字节以及错误的保留位，并在 Mediabunny 复用器写入 MP4 元数据之前加以修复；格式正确或无法识别的记录则保持不变。2.45.1 版已经发布，但我们没有确认它是否包含该修复，也没有在实体 iOS 设备上测试播放。这项变更针对的是这一 H.264 故障，而非所有编解码器或视频。

### Amber 桌面签名器与 Android NIP-46 修复 {#amber-desktop-signer-and-android-nip-46-fix}

10 月 27 日，Android Nostr 签名器 Amber 合并了一个基于 Compose 的桌面 NIP-46 签名器（Windows/macOS/Linux）的源码，它沿用了 Android 版按应用、按 kind 划分的权限模型（[提交](https://github.com/greenart7c3/Amber/commit/1c12bb17e72d5b4ad46753062c1681d4af64adeb)）。NIP-55 仍然仅限 Android。桌面版代码支持多账户以及 nostrconnect/bunker 连接，各应用拥有独立的 relay 和历史记录，此外还支持 Tor 和托盘通知。密钥存放在加密的 PKCS12 存储中，受强制的 Argon2id 口令保护，每个账户的数据库也都经过加密。我们尚未验证桌面版的打包或运行时行为。

另一项已合并的变更针对的是 Android 应用而非桌面签名器，它会[在账户登出后刷新 NIP-46 relay 订阅和连接过滤器](https://github.com/greenart7c3/Amber/commit/2fbb1ee7bea7d5df574db5ca70b73841e8ba500d)。因此，Amber 不再监听已删除账户的密钥。经过脱敏的锁屏通知现在也会显示请求描述。这让通知更有用，但并没有增强隐私。目前尚未确认有包含其中任一 Android 变更的新稳定版。

### noStrudel 的 napplet intent 与同步应用数据 {#nostrudel-napplet-intents-and-synced-app-data}

noStrudel 网页客户端合并了多项源码变更，但尚未确认有相应的标签或部署。跨 napplet 的 intent 通过目录和 z/i 清单声明进行解析，并在目标 frame 加载后，携带经运行时证明的发送方 ID 投递已接受的负载；不受支持的 intent 会被拒绝，显式指定目标的处理程序需要用户确认（[提交](https://github.com/hzrd149/nostrudel/commit/e0211136e71dac6de2bb8af2c0d9e291b02df9ba)）。已安装的 napplet 和默认处理程序会按账户同步到经 NIP-44 加密的 kind 30078 应用数据中，并采用三方合并（[提交](https://github.com/hzrd149/nostrudel/commit/887a6194c8cbab9ce6d780eb62961714777f72f5)）；所选的 [NIP-66](/zh/topics/nip-66/) relay 监控器则通过加密的 NIP-78 应用数据同步（[提交](https://github.com/hzrd149/nostrudel/commit/5a20096f4bcdfbd7ff86b4676cd5653d637ea4bf)）。对于 NIP-17 消息，客户端会从缓存中填充 gift wrap，并在每个会话中从私信 relay 对账一次最近三十天的数据，在受支持时使用 NIP-77，更早的历史则按需加载（[提交](https://github.com/hzrd149/nostrudel/commit/ce95080547485fb403c68f71ce6ad0404f42d230)）。

### Nostr Feedz 已归档 {#nostr-feedz-archived}

Nostr Feedz 曾将 RSS 与 Nostr 长文和视频结合在一起，如今它在 README 中声明已归档且不再维护（[提交](https://github.com/PlebOne/Nostr-Feedz/commit/3b6f6967e532e1f0f4a3503354737cebc3350895)）。该声明指向 PrivKey 开发的 [Readstr](https://github.com/privkeyio/readstr)，这是一个继续开发的分支。这是一次维护状态的变更，我们尚未查看 GitHub 是否将该仓库标记为已归档，也未核实账户和数据能否延续过去。

### Zap Cooking：受保护的列表、签名器修复与 passkey 注册 {#zap-cooking-guarded-lists-signer-fixes-and-passkey-signup}

Nostr 食谱分享客户端 Zap Cooking 合并了一大批网页端源码变更，部署或发布情况尚未确认。对已保存的 kind 30001 列表的写入现在会先读取，并按账户串行执行，保留来自最新完整基线的外来 tag 和加密内容；当 relay 列表未知或法定数量不足时，写入会被拒绝（[#869](https://github.com/zapcooking/frontend/pull/869)）。法定数量要求至少有两个支持列表的 EOSE 应答，外加用户具备该能力的写入 relay 中的一半；nostr.wine 返回的空应答也不能证明不存在（[#878](https://github.com/zapcooking/frontend/pull/878)）。自定义合集共用这一受保护的写入器，较早排队的操作会在新的保护条件下重放（[#885](https://github.com/zapcooking/frontend/pull/885)），而单凭一个空的聚合 EOSE 也不再会让列表显示为空（[#872](https://github.com/zapcooking/frontend/pull/872)）。

一个显式的认证方法修复了生产环境代码压缩导致签名器类被混淆的缺陷，使 NIP-46 和 [NIP-07](/zh/topics/nip-07/) 加密使用当前活动的签名器，而不是过时的本地密钥；对于 NIP-46，relay 钱包备份仍被阻止（[#896](https://github.com/zapcooking/frontend/pull/896)）。从保存或回应操作发起登录后，该操作会继续完成。待处理的 zap 会保留金额和目标，但仍需点击 Send。签名器拒绝时会显示错误，而不会悄悄改用陌生密钥重新签名（[#867](https://github.com/zapcooking/frontend/pull/867)）。

注册时会在本地创建身份，并默认开启以 passkey 加密的保险库同步；如果同步处于关闭状态或上传失败，则必须使用备份密钥，Google Drive 则仅用于恢复（[#893](https://github.com/zapcooking/frontend/pull/893)）。只需一次提示的 WebAuthn PRF 设置会让保险库处于未确认状态，明文 nsec 也会留在浏览器中，直到之后某次成功的保险库解密确认该保险库并删除明文密钥（[#907](https://github.com/zapcooking/frontend/pull/907)）。若将这一提示扩展到注册流程，就要依赖一种未签名的注册，而它并不构成身份验证：任何持有新鲜服务器质询的人都能伪造一次可通过的注册，知道凭据 ID 的攻击者还能替换某个未确认条目（TTL 为 30 天），使真正的用户无法同步（[#911](https://github.com/zapcooking/frontend/pull/911)）。这些都是已记录在案的权衡，而非安全保证。

笔记链接以 [NIP-19](/zh/topics/nip-19/) nevent 编码，最多附带三个观察到的 relay 提示，帮助客户端找到副本稀少的 event，但不保证其可用性（[#873](https://github.com/zapcooking/frontend/pull/873)）。个人资料的“回复”中包含以 event 为根的 [NIP-22](/zh/topics/nip-22/) kind 1111 评论（[#877](https://github.com/zapcooking/frontend/pull/877)）；坐标解析器的一项修复则让带有 URL d-tag 的食谱继续保留在合集和计划中（[#888](https://github.com/zapcooking/frontend/pull/888)）。付费食谱 paywall 实验已经停止，原因是代码作者自行开展的审计发现了一个查询 pubkey 绕过问题；旧的 kind 35000 帖子可作为已存储内容读取（[#862](https://github.com/zapcooking/frontend/pull/862)）。

一项尚未合并的开放提案针对的是屏蔽列表（[#921](https://github.com/zapcooking/frontend/pull/921)）。屏蔽列表获取不可用的情况，将与返回了列表或未返回列表的成功获取区分开来。该更改将不再把不可用的获取结果当作空列表缓存五分钟。解析失败会重试；私密屏蔽项解密失败时会发出警告。打开通知铃铛会重新加载该列表。其目的是防止一个悄然过时的空屏蔽列表让已屏蔽的作者出现在通知中。它并不会让所有失败都阻止内容显示，而且尚未部署。

### Lumilumi NWC zap 支付 {#lumilumi-nwc-zap-payments}

Nostr 网页客户端 Lumilumi 有一个草稿 pull request，将可通过 Nostr Wallet Connect（NIP-47）一键支付 zap 发票（[#1120](https://github.com/TsukemonoGit/lumilumi/pull/1120)）。具有支出权限的连接 URI 仅存储在本地，并被排除在明文 kind 30078 设置备份之外。当钱包声明支持 nip44_v2 时，请求使用 NIP-44，否则回退到 NIP-04。作者使用模拟钱包进行了检查，并未进行真实支付；截至我们的资料截止时间，该草稿尚未合并。

### Wisp 标识符搜索 {#wisp-identifier-search}

Wisp Nostr 客户端有一个开放 pull request，截至我们的资料截止时间尚未合并。它将让搜索功能先识别粘贴进来的 NIP-19 和 NIP-05 标识符、十六进制密钥以及网页实体链接，然后才回退到 [NIP-50](/zh/topics/nip-50/) 文本查询（[#681](https://github.com/barrydeen/wisp/pull/681)）。查找会使用 relay 提示和本地缓存。在等待被查询 relay 返回 EOSE 期间，搜索将以流式方式呈现结果，等待上限为 15 秒，因此慢速 relay 不再被丢弃。作者表示仅在模拟器上做过测试，未在实体设备上测试。

### Zapstore Android TV 支持 {#zapstore-android-tv-support}

基于 Nostr 的应用商店 Zapstore 有一个面向 Android TV 的开放 v2 pull request，截至我们的资料截止时间尚未合并（[#407](https://github.com/zapstore/zapstore/pull/407)）。它将匹配 32 位 ABI，支持仅凭遥控器操作的 Leanback 焦点导航，并在安装权限界面不可用时提供回退方案。缺少 Arti 的 32 位构建会明确显示仅限 Direct 的连接，而缺少 Arti 的 64 位构建则会以失败关闭（fail closed）的方式处理。TV 构建使用本地调试签名器，仅用于测试而非分发；由于公开 bundle 不可用，作者唯一一次 TV 测试使用的是本地构建的 relay。

### strfry 加固与 NIP-11 提案 {#strfry-hardening-and-nip-11-proposals}

以 C++ 编写的 Nostr relay strfry 有两项提案，截至我们的资料截止时间均未合并。[#281](https://github.com/hoytech/strfry/pull/281) 回应了 relay 审计发现的 SF-01 至 SF-13 问题：限制 JSON 深度、解压后的负载、队列和指标标签，修复空 negentropy 过滤器导致的崩溃，并对长 tag 的索引进行哈希处理。它改用 DB 格式 4，因此采用者需要先导出再重新导入。其通过的测试由作者自行运行。草稿 [#278](https://github.com/hoytech/strfry/pull/278) 将只公布实际执行的 [NIP-11](/zh/topics/nip-11/) 限制，外加可选的 fees 和 payments_url；payment_required 默认为 false，所配置的价格本身并不实现支付。

### nostrcheck-server Bark 支付 {#nostrcheck-server-bark-payments}

Nostr 媒体托管服务器 nostrcheck-server 有一个草稿 pull request，用于添加 barkd（Bark）支付提供方（[#62](https://github.com/quentintaranpino/nostrcheck-server/pull/62)）。它将通过 barkd 的 REST API 创建 Lightning 发票，并可选择在 402 响应中附加针对单个文件的 X-Ark BIP-321 URI，同时以同一张 Lightning 发票作为回退。位于同一 Ark 服务器上的钱包通过 Ark 支付，其他钱包则使用 Lightning；一笔已结算的支付可将该文件解锁一次。测试使用模拟的 barkd，而且它依赖仍处于开放状态的 BUD-07 pull request #61。截至我们的资料截止时间，它尚未合并，也不是 share.yabu.me 上提供的功能。

### mattn nostr-relay 付费写入 {#mattn-nostr-relay-paid-writes}

mattn 的 nostr-relay 有一个草稿 pull request，截至我们的资料截止时间尚未合并，它将通过 Bark 钱包添加可选的付费写入功能，默认关闭（[#37](https://github.com/mattn/nostr-relay/pull/37)）。各 pubkey 将通过 barkd 预付写入费用，并可选择按 kind 过滤；没有余额的写入者会收到附带支付 URL 的 restricted: 响应。充值将通过 BIP-321 URI 或 NWC 使用 Ark 或 Lightning 完成，费用列于 NIP-11 中。测试使用模拟守护进程。这一功能应放在主代码树中还是置于 hook 之后，目前尚未确定。

### ContextVM 重连重放防护 {#contextvm-reconnect-replay-guard}

通过 Nostr 承载 MCP 的 ContextVM 为其 TypeScript SDK 提交了一个开放 pull request，可防止 relay 重新连接后出现重复执行（[#113](https://github.com/ContextVM/sdk/pull/113)）。服务器传输层将保留已验证的 event ID，直到传输层关闭为止；另有一个独立的有界信封缓存，用于拦截重新封装的重复内容。在传输层的整个生命周期内，内存占用会随唯一已验证 event 的数量增长。截至我们的资料截止时间，该修复尚未合并，也未包含在任何已发布的软件包中。

### Kehto shell 媒体播放与审批 {#kehto-shell-media-playback-and-approvals}

Nostr napplet 网页 shell Kehto [于 10 月 28 日合并了 NAP-MEDIA 播放功能](https://github.com/kehto/web/pull/354)。Paja 和 playground 宿主现在共用一个由策略管控的音视频播放器。对于有限长度的 URL 和 Blossom 源，它使用浏览器编解码器；在 MediaSource 支持相应编解码器的情况下，它还能播放实时 HTTPS MP3 或 ADTS AAC 流，并且在响应结束之前就开始播放。会话权限始终与端点、源窗口和 ACL 绑定。撤销或拆除时，Blob URL 会失效，播放会停止，流也会被取消。仅限宿主使用的 ResourceService.openStream 方法沿用现有的端点来源授权和策略，且不新增任何资源线路消息。terminal delivery 仍然保留。旧版 sendCommand 别名依然可用。另外，可被检测到的双参数回调仍能继续使用，但会发出警告。单参数的旧版回调则改为使用命令对象。浏览器解析器会拒绝非 HTTPS URL、凭据以及私有 IP 字面量。它还会禁用重定向和 referrer。由于无法检查 DNS，它不能保证在查询时防护私有地址：生产环境的解析器需要在 DNS 解析时进行检查，浏览器默认方案则依赖 CORS 和私有网络保护。HLS、DASH、实时 Ogg、Nostr 源、队列、持久化以及获得焦点时自动恢复播放，目前仍不受支持。作者报告了 155 项 Chromium 测试，以及使用未经修改的 Funclet 构件进行的 112 秒电台播放，我们没有重新运行这些验证。这仅是源码层面的工作。已发布的 Napplet 0.32 软件包缺少部分草案类型。NAP-MEDIA 仍是草案；目前也未声称已发布版本符合该规范。

第二项已合并的更改[让签名和发布审批与具体版本绑定](https://github.com/kehto/web/pull/357)。每项审批都绑定到经过验证的发布者、构件哈希以及当前活动的签名器。审批可以撤销，仅签名审批与仅发布审批彼此独立。旧版权限绝不会被悄然升级。对可变开发 URL 的同意仅在该次加载期间有效；一旦端点或账户发生变化，待处理的请求就会被拒绝。NAP-LINK 只有在用户于宿主模态框中明确点击之后才会打开链接，并使用 noopener。该更改并未声称已针对外部 CVM 电台源进行全面测试，源码合并也不代表已发布 npm 版本。

### Pact {#pact}

[Pact](https://github.com/bobodread876/pact/pull/17) 是一个用于智能体关系和运营者同意的 Nostr 协议，现在会对 Nostr Wallet Connect 回复进行身份验证。每个结果都必须带有钱包的签名并引用其对应的请求；Pact 会检查结果类型和支付哈希，以及任何返回的原像。兑付流程增加了原子化账本写入，并对请求的消费和重试加入了防护；更多伪造同意的途径也已被封堵。一项[限制 MCP 支付额度的后续更改](https://github.com/bobodread876/pact/pull/18)让这类支付保持关闭，除非设置了 `PACT_MCP_ALLOW_PAYMENTS=1`；它还会用默认 1,000 sat 的上限同时核对声明金额和 BOLT11 金额。私密收件箱窗口现在最多处理 200 个 wrap，并会标记截断情况。作者的测试依赖模拟对象。

### nostr.watch {#nostrwatch}

Nostr relay 监测工具 [nostr.watch](https://github.com/sandwichfarm/nostr-watch/pull/961) 新增了显式的 FIPS 发现和传输支持，覆盖网络查询也不再回落到公共 DNS-over-HTTPS。DNS 和 IPv6 路由仍由主机提供，因为该监测工具不附带 FIPS 守护进程或代理，也不提供匿名性。[更严格的 npub 检查](https://github.com/sandwichfarm/nostr-watch/pull/964)只接受位于已解析 `.fips` 主机名中的 npub。[自动 NIP-11 和 NIP-05 探测已移入应用自有的 ServiceWorker](https://github.com/sandwichfarm/nostr-watch/pull/959)，从而把所属标签页的上下文从已观察到的扩展驱动导航路径中移除；这一点已在原版 Firefox 155 中借助受控的扩展测试夹具进行了检查。[一致性测试套件](https://github.com/sandwichfarm/nostr-watch/pull/960)包含十五项有界的 NIP-01 检查，并配有支持独立连接的会话层。作者报告的是测试通过和隔离 mesh 环境中的运行结果，而非针对公共 relay 或浏览器安全的审计。

### Bitcredit Core {#bitcredit-core}

[Bitcredit Core](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1060) 是一个使用 Nostr 的点对点信用与票据协议。在区块操作于本地持久化任何内容或触发其效果之前，它现在会先检查是否至少连接了一个写入 relay。恢复过程也能干净地重新初始化。上周报道时仍处于开放状态的[候选链验证](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1059)此后已经合并，因此链会在持久化之前完成验证和准备。这些措施降低了本地状态不一致的可能性。已连接的 relay 并不能保证各 relay 会接受该 event，也不能保证结算完成；仅凭这一检查也无法让本地持久化变得持久可靠。

一项较新的合并[为身份服务添加了事务管理器](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1063)，但尚未确认已包含在任何发布版本中。身份区块、状态和电子邮件确认现在会在任何内容通过 Nostr 传播之前以原子方式提交，新增的测试则会检查提交失败时不发送任何内容。这仅涵盖身份服务。票据和公司的持久化尚无这种原子提交，relay 接受与结算也依然没有保证。

### MLS-KMP 与 Marmot 兼容性 {#mls-kmp-and-marmot-compatibility}

[MLS-KMP](https://github.com/vitorpamplona/mls-kmp/pull/9) 是 marmot-kmp 下的 Kotlin MLS 库。它此前修复了若干线路行为，以便与其他 MLS 实现保持一致，因此在所列情形中，使用 1.2.0 的成员与使用那批较新代码的成员会产生分歧，群组必须一同升级。保存的状态已迁移到版本 10，旧版本无法恢复该状态。下游 Marmot 兼容性任务为非阻塞性质。其测试并未在该更改的编写环境中运行；Marmot 仍需适配 `authorizeProposal` 和 GREASE。更早的一项 [app-components 更改](https://github.com/vitorpamplona/mls-kmp/pull/7)会强制执行 Marmot 遵循 MDK v0.14 所需的组件。我们尚未核实 Amethyst 是否已采用。

较新的已合并源码[修复了夜间互操作运行器的编译问题](https://github.com/vitorpamplona/mls-kmp/pull/14)，并按脚本逐一报告通过、失败或跳过，但并未声称已包含在已发布的 1.3.0 中。因此，我们此前关于实时运行器从未运行过的说法已经过时：作者报告了正常运行的结果，不过在该更改提交时，最后一次运行仍在进行中，我们也尚未读取到最终的 CI 结果。OpenMLS 任务仍为非阻塞性质，会跳过 22 个不受支持或会引发 panic 的场景，且仅覆盖密码套件 0x0001，因此并不能证明互操作性。该更改还修复了按保留的群组 ID 查找 ReInit PSK、epoch 0 的临时转录（interim transcript）、首个 epoch 的随机密钥以及外部提交的恢复 PSK 处理。对于 epoch 0 的转录，代码现在遵循 RFC 9420 第 11 节，以与 OpenMLS 保持一致，因此外部加入 epoch 0 的行为与 1.3.0 及更早版本不同，已保存的旧群组则会保留旧哈希，直到其首次提交。原有引擎从零值派生其首个 epoch 密钥；由于后续提交会携带新的 UpdatePath，作者没有发现可利用的漏洞，而且这项修复也不表明所有安全问题都已解决。

### Obelisk Relay {#obelisk-relay}

[Obelisk Relay](https://github.com/obelisk-app/obelisk-relay/commit/d575c071729eb5230e73b95d2e2d9db219d5c00b) 向其默认分支合并了一项针对私有 NIP-29 群组的修复。全局 relay 管理员此前已能针对私有群组发送 REQ，但 event 可见性过滤器仍会拒绝匹配的 event。relay 管理员现在可以读取这些 event，成员访问检查也依然保留。relay 私有群组并非端到端加密，该更改让服务器管理员的可见性变得明确。这项修复属于已合并的源码工作，面向开发者和运营者。

### Plume {#plume}

[Plume](https://github.com/cpkb-bluezoo/plume/commit/2e962efb73bf7ef82d5394dc96240d3fb136a428) 是基于 Rust 和 Tauri 的桌面客户端，它合并了一项变更：为每个 relay 保持一个持久且会自动重连的 WebSocket。信息流、个人资料、发布和私信操作都共用这条连接。订阅和 event ID 在这条连接上多路复用。重连尝试会采用退避策略；应用退出时，连接随之关闭。在此变更之前，每个操作都会新开一个 socket，而这些 socket 随后从未被释放。经过审查的这项变更属于已合并的源码工作；本文并未确立任何性能测量结果。它也不承诺无损恢复或保证送达。

### Hashtree {#hashtree}

Hashtree 的 [TypeScript 运行时 0.5.22](https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.22) 允许浏览器 provider 在 IndexedDB 中保留最多 256 条当前有效的已签名公开对等节点公告，并按身份和应用划分作用域。provider 可以在网络发现之前重新加载这些公告。在现有准入规则允许的情况下，普通的对等节点 REQ 可以重放该缓存，而私有发现则保留在单独的所有者作用域中。另外，一项已合并的 [Rust 适配器变更](https://github.com/mmalmi/hashtree/pull/4)会取消被放弃的索引读取，因此命令不再需要一直等到完整的传输超时结束。该 pull request 报告 hashtree-nostr-pubsub 0.2.87 已发布，且该包的版本号独立于 TypeScript 运行时。仅存在于源码中的 Rust 客户端提交为读取操作添加了[合并后的旧版、读取和写入 Blossom 源](https://github.com/mmalmi/hashtree/commit/cc1c73c1733bd14673bad6c87eae6829330b25cf)，并为每个源添加了[针对类型化请求阶段连接重置的一次重试](https://github.com/mmalmi/hashtree/commit/57b30cfdfac3c745c1c3c7083459eb2512ad1ef1)，同时不缓存部分响应。仅凭在一台 Mac 上进行的一次冷安装，并不能证明间歇性传输超时问题已经修复。

### nostr-pubsub {#nostr-pubsub}

[nostr-pubsub TS 0.5.20](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.20) 维护一个容量有界的已签名 event 存储，并为普通 Nostr REQ 添加了 IndexedDB 持久化、跨标签页原子事务、过期机制和本地重放。同一来源还另外描述了一个可选的原生 Rust 文件存储 API，它具备原子快照和独占写入者租约，并且与 TypeScript 包相互独立。在[持久化 event 存储实现](https://github.com/mmalmi/nostr-pubsub/commit/0ee66735e248d9b635caa3f44bdf8b23daf59b0d)中，重新加载时会再次校验签名以及 NIP-01 可替换 event 的胜出者，并拒绝临时 event 以及比当前时间超前五分钟以上的时间戳。存储从不会被隐式打开，公开公告的作用域由调用方选择。FIPS 会在网络发现之前恢复已签名的 kind 37195 公告，并且仍会检查新鲜度、schema 和命名空间。匿名或私有的发现缓存必须与公开重放保持分离，也不应将会从网络获取数据的路由器用作重放来源。由于保留量有界，这并不能提供无限期的离线引导。

### FIPS-TS {#fips-ts}

[FIPS-TS 运行时 0.0.57](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.57) 可以接受一个由应用拥有的持久化发现 provider，该 provider 通过现有接口发布并订阅已签名的 kind 37195 公告。注入 provider 后，传输层不会打开任何 Nostr relay 客户端，并接受空的 relay 列表；关闭时则会排空待处理的订阅。provider 的生命周期和恢复后的存储由调用方负责。命名空间、签名和过期检查依然适用。对等节点授权仍然是必需的。缓存的公告并不能保证离线引导，因为新的经过认证的路由和 WebRTC 信令仍需要一个可达的 FIPS 载体。

### Flotilla {#flotilla}

Flotilla 合并了三项源码变更。[分享到聊天](https://gitea.coracle.social/coracle/flotilla/pulls/847)让用户可以将独立笔记和 NIP-22 评论分享到任意房间或会话中。在会话中引用时，被引用的作者不再被添加到 p-tag 中，成员关系也不会再因此分叉。[恢复中断的上传](https://gitea.coracle.social/coracle/flotilla/pulls/849)会从草稿中恢复附件上传，并通过显示错误让用户能够从失败的上传中恢复。若压缩失败，它会回退到原始文件，而原始文件可能保留其元数据。[等待已存储的已读标记](https://gitea.coracle.social/coracle/flotilla/pulls/846)会在已存储的已读状态加载完成之前暂缓页面已读标记的写入，因此启动时较早发生的已读更新不会丢失。

### following.space {#followingspace}

[following.space](https://github.com/callebtc/following.space) 有一个开放的 pull request，截至我们的来源截止时间尚未合并，它将[恢复 follow pack 的创建、编辑和删除](https://github.com/callebtc/following.space/pull/25)，以及关注某个 pack 中成员的功能。它将使用 Applesauce 进行账户和 outbox relay 发现，并以 `naddr` 地址的形式分享 pack。它支持浏览器扩展签名器、仅保存在内存中的密钥以及 bunker 签名器。代码和作者所描述的测试既不表明存在已部署的服务，也不表明它与所有签名器都兼容。

### Routstr {#routstr}

截至我们的来源截止时间，Routstr 有三个 pull request 处于开放且未合并状态。在核心服务中，[provider 健康发现](https://github.com/Routstr/routstr-core/pull/885)将拒绝解析到非全局地址的公告 URL 和重定向，同时保留对 onion 代理的处理。作者描述了一个服务端请求伪造（SSRF）暴露面及相应测试，但这既不是已部署的修复，也不是已确认的漏洞利用。在 SDK 中，[URL 的 provider 归属](https://github.com/Routstr/routstr-sdk/pull/123)将以签署 kind 38421 event 的密钥为准。写在其内容中的 pubkey 仍未经验证。作者在默认 relay 上检查了 81 个 event，其中没有一个包含基于内容的 provider 列表，因此这里既不声称已知 URL 曾被利用，也不声称所有 provider 现在都是安全的。[模型路径自动固定](https://github.com/Routstr/routstr-sdk/pull/125)将从内置常量改为使用受信任的可寻址 kind 38427 event 中的已签名快照。SDK 将保留最后一个有效快照和回滚水位线，空快照则充当紧急停止开关。该变更会破坏自定义适配器 API。目前尚未发布任何策略 event，部署仍需由运营者执行。

### SatSigner {#satsigner}

SatSigner 有一个开放的 pull request，截至我们的来源截止时间尚未合并，它[重构了其 Nostr relay、缓存和同步层](https://github.com/satsigner/satsigner/pull/687)。未找到 event（即 relay 返回的存储 event 结束回复）将与超时以及完全没有 relay 的情况区分开来。过时的缓存内容将被标记。event 会先被存储，然后处理流程才推进游标；gift-wrap 的 rumor ID 将被验证。移除某个身份会清除其 Nostr 表，但 kind 0 同步可能会覆盖本地的个人资料编辑。一个[叠加在其之上的后续变更](https://github.com/satsigner/satsigner/pull/688)将添加经过脱敏的诊断信息、Nostr 信息流中点按加载的视频封面（最多三个播放器），以及在应用恢复时进行追赶同步而无需拆除 relay 池。它还添加了注入故障的 relay 测试。新的原生视频模块需要重新构建应用，设备验证尚待完成。这两项变更都尚未发布，也都未通过运行时检查。

### Bray {#bray}

[Bray 3.5.4](https://github.com/forgesworn/bray/releases/tag/v3.5.4) 为其 NIP-46 bunker 客户端和守护进程添加了 NIP-42 relay 认证。要求 AUTH 的私有 relay 现在可以用来读取发给 bunker 的消息。此后的源码变更无法确认包含在该 tag 中。

在后来合并的源码中，如果未配置签名器或强制设置了 BRAY_READ_ONLY，Bray 的 MCP 服务器会[以只读模式启动](https://github.com/forgesworn/bray/pull/139)，并且会在打开任何秘密信息之前做出这一判断。在此模式下，不会加载钱包，签名、加密和解密均被拒绝，其 261 个工具中只有 111 个查询工具可用。CLI 和 SDK 仍然需要签名器，而已配置但内容为空的秘密文件仍会被视为错误。新的证明[现在使用](https://github.com/forgesworn/bray/pull/140) [NIP-32](/zh/topics/nip-32/) 证明标签命名空间，取代了 nip-va。现有的 #l 类型查询可以同时找到新旧标签，而 signet-protocol 保留了其自身的 2.5.5 副本。这并不代表获得了正式的 NIP 认可，也不意味着每个嵌套库都已完成迁移。没有证据表明这两项变更中的任何一项包含在 3.5.4 中。

### Alby 浏览器扩展 {#alby-browser-extension}

[Alby Lightning 浏览器扩展](https://github.com/getAlby/lightning-browser-extension)有一个开放的 pull request，截至我们的来源截止时间尚未合并，它将使其[权限辅助函数在单次读取中拒绝已记住的阻止条目](https://github.com/getAlby/lightning-browser-extension/pull/3644)。这修补了一个竞态条件：移除一条拒绝条目可能让 Nostr 处理程序在不提示的情况下执行操作。BTC 和 Liquid 的对应阻止条目路径目前无法触达。这并不是已部署的修复，也没有已确认的漏洞利用。

### MintRadar relay 写入策略 {#mintradar-relay-write-policy}

[MintRadar 源码](https://github.com/hroomnik007/MintRadar/commit/6fd6c8185c053e63610d9b4820e1656552885d85)为该项目的 Nostr relay 添加了运营者写入策略。它将公开的 kind 38172 公告和 kind 38000 评价限制为每个 event 不超过 16,384 个序列化 JSON 字符，且每个 IPv6 /64 每小时不超过 120 个，压缩形式的 IPv6 前缀会被转换为规范形式。高流量来源适用每小时 3,000 个的软上限，而每小时 6,000 个的绝对上限只统计所有来源中被接受的 event。特权密钥不受限制。新连接被限制为每分钟 120 个，突发上限为 60。这只是代码和运营者配置，既不能证明已在生产环境中部署，也不代表提供了完整的拒绝服务防护。

## 新项目 {#new-projects}

### bosstro {#bosstro}

[Bosstro](https://github.com/MostroP2P/bosstro/blob/24bfd318f3e0d9d971e82a04daf12d0f035df2ab/README.md) 是一款面向 Mostro 争议裁决者的全新 Android 客户端。其 MVP 源码已经发布，采用 Flutter 前端，构建在 Mostro 的 Rust 核心之上。裁决者使用专用的裁决者密钥签名，绝不使用节点密钥，节点会授予每位裁决者只读或读写权限。获得授权的裁决者可以接手争议，加入包含图片和 PDF 的加密买卖双方聊天，并向买方付款或向卖方退款。密钥存放在由 Android Keystore 支持的存储中，但 Linux 和 Web 开发构建缺少这些保护。已发布的校验和并不能证明发布者的身份。

### cordn-kmp {#cordn-kmp}

[cordn-kmp](https://github.com/vitorpamplona/cordn-kmp/commit/dcc0508fd818c1b6bc373b2a7d85742a2ec3dc1b) 是一个新的 Kotlin Multiplatform Cordn 实现，基于 Quartz 和 mls-kmp 构建，支持 JVM、Android、iOS、macOS 和 Linux。其无头的 CordnGroupManager 通过 Nostr 上的 MCP 协调器完成创建群组、邀请、加入、发送和追赶同步，这与 Marmot 的 relay 投递模型不同。前端需要自行提供持久化，而 README 中关于与 ts-mls 互操作的说法来自作者本人。

该项目此后发布了 [1.1.0](https://github.com/vitorpamplona/cordn-kmp/releases/tag/v1.1.0)，它基于已发布的 Quartz 2.4.0 构建，因此此前需要在构建标志后使用未发布 Quartz 的本地检出这一要求，已不再适用于带 tag 的版本。[1.2.0](https://github.com/vitorpamplona/cordn-kmp/releases/tag/v1.2.0) [移除了公开的 CordnExposure.differsFromMarmot() 方法](https://github.com/vitorpamplona/cordn-kmp/pull/5)，并将与其他绑定的比较交由前端处理。尽管版本号只是次版本变化，这仍是一项破坏性的 API 变更。曾有提议将此版本命名为 2.0.0，而实际发布使用的是 1.2.0。

### emosphere {#emosphere}

[EmoSphere](https://github.com/Vojta01/emosphere/blob/dfabe1862c57493dbfa9b9881d26b30c1c272762/README.md) 是一个 Nostr 情绪地图，其源码现已公开，README 中描述的版本为 0.5.1。每台设备都会生成自己的密钥，并发布已签名的 kind 1074 event，其中携带情绪及其强度、可选的简短备注，以及用户可以关闭的粗略位置。帖子会显示在世界地图上，并支持时间回放和关注信息流。这些信号是公开且假名的，因此 relay 可以读取情绪和位置，并随着时间推移将它们与某个密钥关联起来。Android 将密钥保存在安全存储中，而 Web 版本使用 localStorage。

### matrix-appservice-nostr {#matrix-appservice-nostr}

[matrix-appservice-nostr](https://github.com/Haven-Organization/matrix-appservice-nostr/blob/2f46b9cfcd7265db38d6a7a2c13552ab2a2aa4cc/README.md) 是一个原型源码，实现了与 Nostr relay 配套的 Matrix 应用服务。Matrix 用户可以创建或导入 Nostr 身份，并在 Matrix 房间中发帖、关注、回复、回应和私信，同时在桥接域名上拥有 NIP-05 handle。内容和媒体保留在 Matrix 后端，relay 会根据保存的原始数据重建 event。密钥在配置的秘密下以 AES-GCM 加密，或通过 NIP-46 远程保管。用户必须信任运营者，而 Matrix 的内容撤除（redaction）操作只会移除桥接端保存的副本。

[七个较新的提交](https://github.com/Haven-Organization/matrix-appservice-nostr/compare/a23289b2fcb42511066b47f1839e52a0184a98fa...b0cd64433ffa0ab6026635de2901a6e0a2146101)添加了[影子 Nostr 身份](https://github.com/Haven-Organization/matrix-appservice-nostr/commit/081ac30dbc8ae56f31ff8cb06f2b70cefb6b2a09)。对于向外交互且获得许可的 Matrix 用户，桥接会自动为其创建这类身份，其个人资料镜像自 Matrix。创建完整个人资料会就地升级现有账户，并保留同一个密钥。桥接管理员可以授予外部用户或 homeserver 完整或影子访问权限，也可以授予限定于房间的被动回复、回应和投票权限。针对特定用户的授权或封禁优先于 homeserver 规则，而 homeserver 规则又优先于房间规则。完整权限允许创建个人资料，但不会自动发布个人资料。撤销访问权限会保留密钥、历史记录和房间，但在不再获准的地方会停止向外发帖。导入的身份永远不会被镜像个人资料覆盖。这些检查已有代码和测试，但没有经过运行时互操作性或安全性验证，并且仍需信任运营者对密钥的处理。贴纸现在以图片形式发出。

### nostr-scrutiny {#nostr-scrutiny}

[Nostr Scrutiny](https://github.com/rzazo24/nostr-scrutiny/blob/2f2c38aa67eb7db72113bcf1ba00c55e99bc7e2e/README.md) 发布了源码以及注明日期为 10 月 24 日的事实说明表，对比了五款 Nostr 客户端：Amethyst、Damus、Nostrich、Primal 和 Quill。每份说明表都涵盖该客户端在应用商店中的隐私声明和已发布的代码，还列出了首次通过浏览器访问时观察到的网络请求。该网站以静态纯 HTML 构建，自称没有第一方追踪。这些说明表是注明日期的事实清单，并非安全认证或密码学审计。作者披露了一项利益冲突：其本人也在开发 Quill。

### v2 {#v2}

[Solid Chat v2](https://github.com/solid-chat/v2/blob/da8b577a98167235f4452cbc97ca5fdb918b5cea/README.md) 是新发布的客户端源码，使用同一个 did:nostr 密钥，借助 NIP-98 HTTP 认证向 Solid pod 房间写入内容，并发送 NIP-17 gift wrap 封装的私信。签名可通过 NIP-07、NIP-46 或本地 nsec 完成，采用 NIP-44 加密和 kind 1059 封装。房间内容为明文，仅受各个 pod 的 ACL 保护。加密私信中的媒体会上传至 Blossom，个人资料查询则发往 nostr.social 目录。由于本地 nsec 存放在 localStorage 中，使用外部签名器更为安全。

### witchat {#witchat}

[Witchat](https://github.com/BarefootJoey/witchat/blob/905f17d322752554e077a5a0e774555c38417e50/README.md) 是一款非官方 bitchat 客户端的源码，支持 Windows 和 Linux。它通过附近的蓝牙 mesh 网络聊天，在互相收藏的联系人之间则回退到 Nostr gift wrap。此外，它还能加入 Nostr 上的公共 geohash 频道，消息使用 kind 20000 event，在线状态使用 kind 20001。与 bitchat 各传输方式的互通性只是作者的说法，而且 Windows 二进制文件未经签名。Nostr relay 可以看到 IP 地址和频道元数据，附近广播目前只经由蓝牙传输。

### wn-notify {#wn-notify}

[wn-notify](https://github.com/jooray/wn-notify/blob/ba21270edace90c0d6dde7fde7c3b1e3fb5c6201/README.md) 是一个非官方的、仅依赖标准库的 Python CLI，经由本地 wn-agent、通过 marmot.agent-control.v2 Unix 套接字向 White Noise 群组发送消息和文件；密钥、MLS 状态和 relay 均由该连接器持有。CLI 会检查 final_sent 和消息 ID。若结果未知，它会以非零状态退出并报告为 unknown，同时保留幂等键以供手动重试，因为它自身从不重试。确认回执只能证明已发布到 relay，并不代表有人读过该消息。目前仅测试过 wn-agent 0.13.0。

### xmradar {#xmradar}

[XMRadar](https://github.com/KYC-rip/xmradar/blob/537309555c511e2f5f257fe7e471b0ff2c91ac4f/README.md) 是一款浏览器扩展，可将网页帖子和 X 文章复制到 Nostr。每次发布都需经外部 NIP-07 签名器批准。[0.2.0 版本](https://github.com/KYC-rip/xmradar/releases/tag/v0.2.0) 新增了在 X 上向拥有 Nostr 身份的作者打赏 Monero 的功能。

[该实现](https://github.com/KYC-rip/xmradar/commit/213d4b1a6604fe07af4c1991a1c8159a7bcc4abc) 只有在用户表示已发送打赏并予以确认后，才会发布 kind 9042 回执。该回执会公开双方的 npub、金额和地址。其中不包含交易 ID、交易密钥或支付证明。一个随机的小额 piconero 数值让收款方的钱包能够匹配这笔付款，并发布 kind 9044 确认。这份确认由收款方签名，并非独立的链上证明。界面会将收款方已确认的打赏与未确认的声明区分开来。用户自己的打赏会保持待定状态 30 分钟。未确认的声明按每位付款方只计一次，以发往当前地址的最小一笔回执为准；这些声明可以被伪造。总额按作者而非按帖子统计。通过 [NIP-A3](/zh/topics/nip-a3/) 和 [NIP-39](/zh/topics/nip-39/) X 证明进行的地址发现默认关闭。一旦开启，relay 和 X 就能看到用户查看了哪些身份。

### agent-inbox {#agent-inbox}

[agent-inbox](https://github.com/ec175/agent-inbox/commit/88fa9da299c3013a0c6a2c88abf0223945229bfa) 是一款新工具，让 AI 智能体能够通过 Nostr 以简短标识相互联系。只需单个 Python 文件，它就能发送采用 NIP-44 v2 加密的标准 NIP-17 gift wrap，还能向公共留言板发帖，并附带来自官方测试向量的测试夹具。这些标识是截断后的公钥后缀，而非经过认证的身份。README 警告称其纯 Python 密码学实现并非恒定时间，我们也未对其进行审计。任何 NIP-17 客户端仍可向智能体的 npub 发送消息。

### CarryChat {#carrychat}

[CarryChat](https://github.com/kemal-arslan/carrychat/commit/64437892165b41070d93acb9b6815dc97168b5a1) 是一款新的存储转发式通讯工具，可通过任何可用路径传送有大小上限的消息包。Nostr 是它的互联网传输方式，低功耗蓝牙和普通文件交换等本地链路则负责离线场景。源码包含 Nostr 传输层及其测试。按 README 的说法，这是早期的 0.2 版本，在实体硬件上的 LoRa 实地测试尚未完成。我们没有在设备上测试它。

[十三个较新的提交](https://github.com/kemal-arslan/carrychat/compare/64437892165b41070d93acb9b6815dc97168b5a1...311f1765e72079c7b70cf8d1c55865dc781cc2ad)（截至 [311f176](https://github.com/kemal-arslan/carrychat/commit/311f1765e72079c7b70cf8d1c55865dc781cc2ad)）用可运行的源码替换了路线图中的占位内容。它们涵盖 Wi-Fi Direct、MeshCore 无线电适配器、Reticulum 链路、NFC 联系人名片和音频传输，涉及 Kotlin、Rust 和 UI 代码。通过音频传输时，接收方会验证联系人名片签名并接受普通消息帧，但会拒绝文件分块。NFC 只交换联系人名片，不交换消息。这是继早先 0.2.0 版本之后的源码开发，而不是新的经过验证的二进制文件。README 表示，MeshCore 与 LoRa、Reticulum、Wi-Fi Direct 和 NFC 仍有待实地测试或双手机测试。这些改动并未声称具备硬件兼容性、匿名性或安全性。高频音频效果取决于硬件，并非在所有情况下都听不见。Nostr 仍是与本地链路并存的一种互联网 relay 传输方式。

### Cosign 与 Marble {#cosign-and-marble}

[Cosign](https://github.com/sybenx/cosign/commit/c42da802f4d526c5c3c2b08593fcba267f3097c9) 是一个新的 beta 版协议和库，可将 Nostr 签名密钥拆分为 FROST 门限份额。用户的设备可以与服务器共同签名，但服务器无法单独签名。一份纸质备份份额用于支持 README 中描述的恢复和份额刷新流程，而这些流程尚未经过安全验证。[Marble](https://github.com/sybenx/marble/commit/d5b50d760c6d4f093120d1d955918430d8360bf6) 是一款 Android 和浏览器客户端，借助 Cosign 处理信息流和签名。底层 FROST 库已经过审计，但 Cosign 自身的协议尚未接受任何独立审查。

[在较新的源码中](https://github.com/sybenx/marble/commit/ebd110f907d3569a8a9b3e385394c5a55b5582ec)，Marble 浏览器客户端会将未发送的笔记与已登录账户绑定。发布之前，它能察觉其他标签页或远程会话是否已结束登录；来自已登出客户端的请求会显示 Signed out。[即时搜索](https://github.com/sybenx/marble/commit/029d8b0f918a9783910aef15f6fe1f160d9c6707) 查询的是 Ditto 和 relay，而非整个互联网。搜索某位作者的帖子时，它会先检查已加载的帖子，再向 relay 请求。疑似垃圾内容会折叠在一个可展开的提示之后。“Not Spam”覆盖设置仅在该浏览器中生效，且仅针对该作者。这些搜索辅助功能不能作为已进行安全审查的证据。

[Cosign 0.12.7](https://github.com/sybenx/cosign/releases/tag/v0.12.7) 规定成员列表合并只能来自服务器，从而防止纸质备份份额被提升为其他角色。完成 epoch 同步后，过时的服务器会被标记为落后。无效的部分结果会被拒绝；自动修复仍保持禁用。解密部分结果现在附带 Chaum-Pedersen 证明，在合并这些部分结果之前会先校验证明。旧版客户端会忽略这些证明，而 Marble 的 Android 部分将随其下一个构建版本提供这项支持。上述安全描述出自发布作者，我们并未审计其密码学实现。

[在 0.12.7 标签之后提交的 Android NIP-55 源码](https://github.com/sybenx/cosign/commit/e53941f699e9e77ed430015e416daa723c95204f) 修复了首次连接时的一个竞态问题，此时服务器的授权仍在经由 relay 传来。公钥查询现在会立即响应。签名和解密会在 UI 线程之外等待，并且只有当新获授权的连接收到 revoked 响应时才会重试一次。代码还能区分无法连接的服务器和以拒绝作为响应的服务器。目前无法确定这一后续源码修复已包含在 0.12.7 标签或当前的 Marble 二进制文件中。

### Dream Nests {#dream-nests}

[Dream Nests](https://github.com/2three1y/dreamnests/commit/0edc7af86c326452a020ba0b7124c55f5a0413b5) 是一个新的只读目录，收录正在直播的 Nostr 音频房间，把 Nests 房间和直播活动 event 连同其聊天内容汇集在一起。针对屏幕阅读器，这款 Web 应用使用标题和 polite 级别的 live region 播报，并以简短的 earcon 作为音频提示。它以仅收听模式播放公开的 HLS 流。Nests 房间会在 Nests 中打开，Corny Chat 和 HiveTalk 房间则在各自的网站上打开，因此发言仍在这些应用中进行。麦克风指示来自在线状态元数据，而非语音活动检测。我们没有在设备上测试无障碍功能。代码仓库记录了一个公开的线上 URL。

### fips-pub-pki {#fips-pub-pki}

[fips-pub-pki](https://github.com/fr34aky/fips-pub-pki/commit/bd0ea8a16a24eb14d92563cd8d470afad172c83a) 是用于签名 Nostr 证书的新源码，允许域名向下级签发者委托，并支持离线路径验证。信任锚来自配套的 fips-pub-domains 项目，该项目将 DNSSEC 声明与固定值（pin）和见证者相结合。验证器从不查询 DNS。撤销依赖过期时间和显式标记，而不是从 relay 删除 event。据 README 所述，使用公共域名和手机进行的实时 mesh 测试尚未完成。由于既未提交 NIP，也未注册 kind，这只是一项实验，并非 TLS 的替代方案。

### Magnetar {#magnetar}

[Magnetar](https://github.com/awake-devel/magnetar/commit/b519486d6ed3a1e6f41c4e7faa5c587e9362caf1) 是面向 [NIP-35](/zh/topics/nip-35/) 种子 event 的新搜索栈。它将爬虫和搜索后端与一款保留本地 SQLite 缓存的 Android 应用配套使用，依据关注关系建立发布者信任，并检查 swarm 的活跃度。首个 0.1 预发布版本包含爬虫代码，以及 Android 端和服务器端的测试。作者仅通过自动化测试和模拟器进行了验证，没有在真实手机上验证。基于关注关系的信任无法让种子变得合法或安全，该后端也不是权威索引。

### Magnitude Relay {#magnitude-relay}

[Magnitude Relay](https://github.com/VectorPrivacy/magnitude-relay/commit/92f2440d96a3bf3a6c86691b146ebd6fef7b9f10) 是 VectorPrivacy 推出的新 Rust Nostr relay，针对 Vector 的 gift wrap 私信和 Concord 流量进行了调优，支持 NIP-77 同步和输入状态提示。据运营者称，它已在两个现有的 Vector 端点上取代了 strfry。其代码仓库包含对抗性测试和基准测试工具，但公布的速度数据来自作者自己的运行结果，未经独立复现。

此后，它合并了面向运营者的 [Docker 和 Compose 打包](https://github.com/VectorPrivacy/magnitude-relay/pull/1)。它以非特权用户身份运行，配有数据卷、仅限本地的绑定地址和健康检查。该 pull request 中关于生产环境和导入的观察结果来自作者，arm64 尚未测试。仅凭打包并不能表明协议符合性。

[较新的源码](https://github.com/VectorPrivacy/magnitude-relay/commit/af1b354c5f465d4bf7772ef8fa8f0eaf35a7aabe) 默认按 IP 限制新连接：突发上限为 300，之后为每分钟 60 个。把限制设为 0 即可禁用，回环地址不受此限。代理的真实 IP 头仅在来自 localhost 时才被信任，被拒绝的连接会在 WebSocket 打开之前收到 HTTP 429。公开的 relay 拒绝情况只以汇总形式报告，按 IP 的详细信息只能通过管理套接字获取。批量 NIP-77 同步会排除临时 event 以及将在 600 秒内过期的 event，而实时投递仍会传送短时效 event。受信任链接发生变化时，relay 会跳过多余的 gift wrap 可见性探测，但 gift wrap 仍会同步。这些都是源码改动，没有实测的生产环境基准数据。

### nostr_doctor {#nostr_doctor}

[nostr_doctor](https://github.com/nogringo/nostr-doctor/commit/348efc1dd32c213badf34c6ba529707b952bd658) 是一个新的 Dart 库，附带 CLI 和 Flutter 前端，用于检查客户端能否发现某个账户的数据。它先从个人资料元数据和 NIP-65 relay 列表入手，随后涵盖私信 relay 和草稿，以及 Blossom 服务器和 nutzap 设置。为检查 relay 列表的可发现性，它会探测该可替换列表。我们以源码形式审阅了这款诊断工具，没有验证任何应用发布版本。其结果只反映它所查询的 relay，并不代表全局可用性。

### nostr-indexer-relay {#nostr-indexer-relay}

[nostr-indexer-relay](https://github.com/nogringo/nostr-indexer-relay/commit/f75e4415f24f629935f7e6b3567232e2c6dbf80a) 是一个新的 Go relay，只存储 NIP-65 relay 列表。它的爬虫会找出这些列表中提到的 relay，探测它们是否支持 NIP-77，并通过 negentropy 与其他在线索引器同步。它包含一个公开查询页面和管理界面，并自称仍处于早期阶段。这是一个专注于 relay 列表的索引，而不是 Nostr 存档或通用内容 relay。

### nostr2gh {#nostr2gh}

[nostr2gh](https://github.com/kravens/nostr2gh/commit/ec189b10d48d0f9f0c0e8a464c930263b2275c95) 是一个新的桥接工具，通过白名单内的 relayer，将 NIP-34 补丁和 pull request event 及其更新从 Nostr 传送到 GitHub。贡献者把分支推送到可拉取的位置并签署一个 Nostr event，随后由一位拥有可用 GitHub 账户的朋友代为开启 PR。该工具能帮助无法访问 GitHub 的贡献者，但它不会自动绕过封禁，也不代表允许自动运行不受信任的补丁。

### Relay Radio {#relay-radio}

[Relay Radio](https://github.com/2three1y/relayradio/commit/3993e7226de616ac9a2768a5d50a271535449806) 是一款新的只读 Web 应用，借助 earcon 和浏览器文本转语音，将实时 Nostr 信息流转换为声音，还为屏幕阅读器用户提供可选的 polite live region。听众可以选择精选的全球电台，或基于自己关注的人构建的电台，内容涵盖笔记、回复、转发、回应和 zap。它从不代替听众发帖或付款。内容过滤只是尽力而为，因此无法保证朗读出的所有内容都是安全的。

### Hibiki {#hibiki}

[Hibiki](https://github.com/ChiefmonkeyArt/torii-hibiki/commit/3820208896df7ba28a06a2cfa38fefc1a753f9d1) 是面向 Torii 的独立 feed napplet，其源码称 0.2.1 版本为第一个可用的 feed。公开帖子和媒体由节点抓取，基于用户口味的排序则在浏览器中运行。该 feed 运行在没有直接网络访问权限的沙箱 iframe 中，并且只把已签名的垃圾信息信誉数据当作参考建议。我们没有独立验证其隐私边界。

截至 0.2.6 版本的已合并源码加入了[内联回复和抽取式新闻摘要](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/8)，点赞也不再会让帖子重新排序。带标签的发布版本仍未确认。Watch 播放器中的预览支持加入了[预览帧](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/9)。[Zap](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/11) 随个人资料页一同推出。每张发票的金额和描述哈希都会由节点检查。每笔付款都需要所有者确认；付款方使用 WebLN 或二维码。节点既不持有资金，也不持有密钥。Primal 地址的发票缺少描述哈希，因此[一项后续改动](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/12)会在金额完全匹配时接受这类发票。它们被标记为 bound:false，所有者也会收到钱包可能不会确认的提醒。这削弱了发票与 zap 请求之间的关联，也不会让它们成为有效的 [NIP-57](/zh/topics/nip-57/) 确认。遇到钱包的 5xx 错误和超时，会重试一次，并显示 LNURL 给出的原因。作者尚未报告过使用真实钱包成功完成端到端 zap。

### wax {#wax}

[wax](https://github.com/modus-lisp/wax/commit/0b48716cfce52be990e0ef43fcecb2c5fa899b44) 是一个新的 Common Lisp 签名器，它从 BIP-39 种子派生角色密钥，并让每个请求都经过策略守卫；除非审批回调或允许列表放行，否则默认拒绝。按调用方区分的信封序列号用于防范重放。它的方法名称与 NIP-46 相似，但核心并不提供网络传输。我们没有对该签名器进行安全审计。

### WhatZaps {#whatzaps}

[WhatZaps](https://github.com/nostr-wot/whatsapp-zaps/commit/ab86552a5178c9c1b55dd917084f4e3cf223ea89) 是一个新的浏览器扩展，借助 Nostr WoT 扩展中的 WebLN 支持，通过 Lightning 向 WhatsApp 联系人付款。它会将联系人映射到 Nostr 个人资料，检查对方的付款地址，并在付款前始终要求明确确认。/zap 命令不会作为聊天消息发送，通过回应或按钮付款的方式也不会发布任何内容。这些是借助 Nostr 查找身份的 Lightning 付款，而非已签名的 [NIP-57](/zh/topics/nip-57/) zap 收据。其浏览器消息匹配功能我们没有测试。

### Agora 加密投票 {#agora-encrypted-polls}

[Agora](https://github.com/maxgfr/agora/commit/85d83f49dcb3ed138c4118bced60d1a2f48fb01b) 是一个用于加密群组投票的浏览器原型。它把成员担保与盲投票凭证结合起来，并通过 Nostr relay 和 WebRTC 传输流量。[README](https://github.com/maxgfr/agora/blob/85d83f49dcb3ed138c4118bced60d1a2f48fb01b/README.md) 将该设计概括为“一个真实的人，一票”，但这取决于对凭证签发方的信任（签发方可以伪造凭证），也取决于作为一种社会信任形式的担保机制。该设计不具备抗胁迫能力。relay 可以看到时间信息和 IP 地址；结果则取决于客户端收到了哪些 event。该项目与较早的 ghobs91/Agora 聊天项目无关。

### Cinderous SDK {#cinderous-sdk}

[Cinderous SDK](https://github.com/VaalRL/cinderous-sdk/commit/59314a6c2dffb85224c6262348a707f6acc4eb83) v0.83.0 是一个新的源码原型，它为每台设备分配独立的密钥，并通过 Nostr 和 WebRTC 以类似 Git 的历史记录同步文档，必要时回退到 relay。relay 由调用方选择和部署，SDK 不附带默认的公共 relay。其加密采用带 Double Ratchet 的实验性 CinderEK 方案，该方案尚未经过外部审计。混合密钥交换并不能让 secp256k1 签名具备抗量子能力，[README](https://github.com/VaalRL/cinderous-sdk/blob/59314a6c2dffb85224c6262348a707f6acc4eb83/README.md) 也称该 SDK 尚未达到生产就绪状态。

### evil-napplets {#evil-napplets}

[evil-napplets](https://github.com/napplet/evil/commit/7311b6298e7b64e595d8b566f226a26cad1cfee5) 新增了第 02 至 08 级攻击阶梯，用于测试在 NIP-5D 草案的不透明源（opaque-origin）模型下运行 napplet 的宿主。这些恶意 napplet 会探测能力边界和桥接边界，并报告宿主允许了哪些操作。默认采用演示模式，主动模式必须显式启用。主动测试只应针对测试者获得授权探测的宿主运行。该套件是红队测试夹具，因此通过它的宿主并不能证明是安全的。它与 evil-napps 是不同的项目，后者针对的是另一种应用架构。

### evil-napps {#evil-napps}

[evil-napps](https://github.com/sandwichfarm/evil-napps/commit/f0746e4cb958bbcb01806e2354809472b63a943a) 是一个新的源码套件，用于探测 NAPP 启动器中的权限边界。启动器桥接以及向应用暴露的 NIP-07 签名器都在其覆盖范围内。SharedDB 存储同样在测试范围之内。NAPP 包将元数据与一个索引文件搭配在一起，这种格式不同于 NIP-5D napplet 使用的单一 HTML 产物。根据 [README](https://github.com/sandwichfarm/evil-napps/blob/f0746e4cb958bbcb01806e2354809472b63a943a/README.md)，该套件默认以演示模式运行，只有在明确请求时才会运行主动探测。其测试和测试框架并不能为启动器提供认证。

### Feedstr {#feedstr}

[Feedstr](https://github.com/0n4t3/Feedstr/commit/3fe44eca46106488585d0d1554509f5d3e498f39) 是一个新的 Rust RSS 阅读器，它通过 Nostr 以加密形式同步订阅源、已读状态和收藏。可以针对单个订阅源关闭同步。它支持 OPML 导入和导出，并能处理 [NIP-23](/zh/topics/nip-23/) 长文。仓库包含 core、Android、web 和 Flatpak 源码树。[README](https://github.com/0n4t3/Feedstr/blob/3fe44eca46106488585d0d1554509f5d3e498f39/README.md) 表示该软件几乎未经测试，不建议使用，安装和使用说明即将推出。

### NKIP 存款收据工具包 {#nkip-deposit-receipt-toolkit}

[KYC-rip/nkip-0001](https://github.com/KYC-rip/nkip-0001/commit/6d6a9489db72626794e7e2b88a18846ea19a10e2) 是由 XBToshi 维护的新 TypeScript 工具包，用于 NKIP-0001 存款收据。NKIP-0001 是一种应用层收据格式，并非已被接受的 Nostr NIP。该工具包处理 Ed25519 签名的存款收据、加盐承诺、Nostr 见证 event，以及通过 NIP-44 加密实现的盐值恢复。它能否起到保护作用，取决于应用在观察到见证之前是否不透露存款地址。该 SDK 不对订单进行把关，也不保证支付款项。详情见 [README](https://github.com/KYC-rip/nkip-0001/blob/6d6a9489db72626794e7e2b88a18846ea19a10e2/README.md)。

### nostr-parse {#nostr-parse}

[nostr-parse](https://github.com/VectorPrivacy/nostr-parse/commit/703f07cd7177b2b52977aa6deaa6f11a696d4914) 是 VectorPrivacy 推出的新 Rust 解析器，用于解析已签名的 Nostr event。它强制要求严格的七字段 event 结构，要求非负整数，将 kind 限制在 u16 范围内，检查十六进制字段并校验转义字符串。报告错误时会附带偏移量。调用方既可以生成紧凑的自有内存分配，也可以生成指向输入的借用片段，而 `parse_unsigned` 可接受未签名的 NIP-59 rumor。解析过程不会重新计算 event ID，也不会验证 Schnorr 签名，因此调用方仍需自行执行这些检查。

### cl-deposits {#cl-deposits}

[cl-deposits](https://github.com/modus-lisp/cl-deposits/commit/3d74564de6be0d25efec3ce6ad76a4fc691dc676) 是 Bitcoin Deposits 的一个新 Common Lisp 实现。在这一设计中，运营方通过 Nostr 运行经过签名、由法定数量联署方共同签署的哈希链账本，并以 Taproot 储备作为支撑。仓库中既有源码，也有一个带检查测试的 devnet。根据 README 和 [ROADMAP](https://github.com/modus-lisp/cl-deposits/blob/3d74564de6be0d25efec3ce6ad76a4fc691dc676/ROADMAP.md)，作者已重放参考测试夹具，运行了 signet devnet，并与 deposits-rust 进行了双向互操作测试。作者还表示 Lightning 收款路径可以正常工作，并将付款 InvoiceLock 和 Fulfill 列为下一步工作。用户需要依赖运营方、联署法定人数以及储备方面的假设。

### Streets {#streets}

[Streets](https://streets.eyemono.moe) 是一个按列布局的 Nostr 网页客户端，可并排显示时间线、通知和搜索。它合并了一项[改动](https://github.com/eyemono-moe/streets/commit/6b31a7c97cc6801cf392ab61c4de4af7d3286233)，将默认回应表情保存在账户的 NIP-78 deck 文档（kind 30078）中。这样一来，用户在重新登录后或在另一台设备上就不必再次选择。此前，这一选择只存储在设备的 localStorage 中。deck 文档使用 NIP-44 加密，因此跨设备同步需要使用支持加密的扩展或签名器登录。在其他登录方式下，该设置会保留在设备上。如果账户没有已保存的回应表情，就沿用设备上现有的值，因此设置不会重置为爱心。无效的已保存值会被丢弃，deck 的其余内容则不会被一并丢弃。该改动已进入源码，1.22.0 的发布说明仍是草稿。

### Labradorite {#labradorite}

Labradorite 是一款 Android 应用，用于控制已配对 Linux 计算机上的编码代理会话，它发布了 [0.1.0](https://njump.me/nevent1qqsdqkdh6z32nysms5exwtw76n0vp3h2zzxtchh4sfcrywe5tz5gd0czyp6hjpmdntls5n8aa7n7ypzlyjrv0ewch33ml3452wtjx0smhl93jqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkylssg9) 和 [0.2.0](https://njump.me/nevent1qqs9pra62cxllt9uggf38lqxsmv7np34f4jjfyr6zath3d4ffn0hlxszyp6hjpmdntls5n8aa7n7ypzlyjrv0ewch33ml3452wtjx0smhl93jqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkn9vmwk)。手机只是控制界面。代理由计算机上的守护进程运行，该进程通过普通的 Nostr relay 交换 Marmot MLS 消息，每个会话对应一个群组。它只接受允许列表中的 npub，而该列表默认为空（[源码](https://gitworkshop.dev/npub1w4uswmv6lu9yel005l3qgheysmr7tk9uvwluddznju3nuxalevvs2d0jr5/relay.ngit.dev/nostr-agents)）。0.1.0 版本可以启动或恢复已批准的会话，流式传输文本、工具调用和 diff，并处理审批和提问。Git 控制和只读文件浏览也包含在内。到了 0.2.0 版本，后续请求会作为独立轮次排队，用户可以从手机上取消它们；排队的工作在守护进程重启后依然保留，重新连接后还会回放错过的历史记录。以上均为发布者的说法，我们尚未独立审计其安全性。

### Nomisma {#nomisma}

Nomisma 是一款处于[原型 beta 阶段](https://github.com/Lwb89dev/nomisma/tree/46ed9b3190ab93d1acea511677c6d4d18de931b5)的 Android 共享开支账本，通过私密 Nostr 消息将两名参与者配对。它只记录余额，不会转移或结算资金。[0.1.3 版本](https://njump.me/nevent1qqszafzumepzzcw68g652k3m47v473y4jac9mhan5fpk344qd0w0m4szypjgcr6nqtr47wpc9fxjepdys2uj0nrpk2pg5pu5udkxe3ukm6r2vqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetknw8e4p)会自动重新连接已配对的设备，以逐渐增加的延迟重试已持久化的更改，并加入 NIP-42 relay 身份验证。缺失的操作也会被重新发送。只有当双方按作者区分的向量时钟一致时，两台设备才会比较条目、付款人和分摊方式的 SHA-256 指纹。由于默认 relay 已经更改，两台设备都需要 0.1.3 版本和一致的 relay 设置。检查点经过 gift wrap 封装，并带有 15 分钟的 NIP-40 过期时间，这会要求 relay 丢弃它们，但不保证彻底删除。说明中报告修复了原生库加载、Schnorr 参数顺序和 NIP-44 密钥派生方面的问题，我们尚未独立审计其安全性。用户签名通过 Amber 进行，但设备上也存在临时密钥。关于 APK 签名证书，各份分发说明相互矛盾，因此我们在此未对升级兼容性作出评定。

### Onyx {#onyx}

[Onyx](https://gitworkshop.dev/npub1vx40p5mkcwyrg2gnthf343y39tf0zqxl56ajvql2m9q3rxremynsfp37lu/relay.ngit.dev/onyx) 是一个以源码形式提供的私密日记原型，而非经过验证的正式发布版本。它将带日期的 Markdown 文件保存在设备上作为可信数据源，并以加密的 kind 30078 event 形式备份到 relay。加盐的 d-tag 避免了直接暴露条目日期。恢复需要单独的本地加密密钥，仅凭 npub 无法恢复日记，所以用户必须备份该密钥。10 月 27 日的一个补丁新增了一项防护，在发布前检查请求字段的完整性：签名器返回的 event kind、content、pubkey、tags 和时间戳必须与请求一致。此外，该补丁会拒绝来自错误作者的下载，保留较新的本地编辑，并在恢复期间以原子方式替换数据。event 的作者和时间戳仍是公开的。传递给加密命令的明文可能会短暂暴露给本地进程检查，删除条目也不会清除 relay 上的副本。

### Zzub {#zzub}

[Zzub 0.0.41](https://njump.me/nevent1qqs2rzmlu7hwflagzswk3q6e20nrzp6gcq5rgk4uu2a9kcuuzlhmfyszyrts65qfz5ztnyk3swyz9teyt40kkwskhqkez7kt0yjvaas76jkwuqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkfm8t9z) 是从 Buzz 分叉出来的社区客户端。根据发布者的简短说明，此版本新增了支持时区的日历 RSVP、个人资料 zap、[NIP-58](/zh/topics/nip-58/) 徽章显示，以及一个可加入实时会议的 huddle 按钮。代理控制方面新增了重启选项、预算豁免列表编辑功能以及新的任务卡片类型。启动时现在会使用缓存的频道。

## 协议与规范工作 {#protocol-and-spec-work}

### NIP-CD 定义以纯文本调用的命令 {#nip-cd-defines-commands-invoked-as-plain-text}

[NIP-CD 规范](/zh/topics/nip-cd/)最初名为 Commands，现名为 Slash Commands，已[于 10 月 21 日合并入 NIPs 仓库](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)（[提案审查][commands-review]）。执行方通过一个 kind 31992 event 发布命令，其中列出触发词、标题、描述、带类型的位置参数和作用范围。用户在 event content 开头以纯文本形式调用命令，并可选择用执行方的 npub 加以限定，因此不需要特定于命令的 tag 或客户端支持。一个不带限定的触发词可能匹配多个执行方。客户端可以提供自动补全，但不能强制要求使用。

### Marmot 采纳每个账户多设备方案 {#marmot-adopts-multiple-devices-per-account}

[Marmot](/zh/topics/marmot/) 是一个面向 Nostr、基于 MLS 的加密群组消息协议，它于 10 月 26 日[合并了多设备账户规则](https://github.com/marmot-protocol/marmot/commit/be923c9cad997176cc155d5d851d40d28e19cc6b)（[提案评审][marmot-devices-review]），合并版本相较早前的草案有所修订。邀请者在一次 Commit 中最多可为同一账户添加 20 个 KeyPackage。每台设备恰好持有一个终身不变的随机发布槽位，且从不复制 MLS 状态或私有 KeyPackage。KeyPackage 的有效期应为 30 天，刷新周期为 7 天。邀请者会向每台符合条件的设备分别发送其专属的 Welcome；移除一个账户时，该账户的全部叶节点都会被移除。

### Marmot 允许成员管理自己账户的叶节点 {#marmot-lets-members-manage-their-own-accounts-leaves}

Marmot [采纳了一个同账户成员资格组件](https://github.com/marmot-protocol/marmot/pull/443)，即 `marmot.group.account-devices.v1`（ID 0x800d），该组件不携带任何数据。当群组协商要求使用该组件时，成员无需管理员权限即可为自己的账户提交 Add 和 Remove。在此组件下，成员不能移除提交者自身的叶节点，也不能移除其他账户，该账户的管理员身份也不会因此改变。现有群组必须激活该组件，并满足其支持不变量。

### Marmot 推送触发器加入新鲜填充 {#marmot-push-triggers-gain-fresh-padding}

Marmot [现在要求每个推送触发器都包含新鲜填充](https://github.com/marmot-protocol/marmot/pull/445)，该变更于 10 月 26 日合并。每个 kind 446 触发器至少携带一个新生成的 1,084 字节 CSPRNG 填充块，因此在 32 块的预算内，真实的加密令牌最多只剩 31 个。如果没有新鲜填充，相同的令牌字节会让基于内容哈希的去重机制压制之后合法的通知。服务器会对所有块计算哈希，且不得因为无法识别填充而拒绝结构有效的触发器。填充能向 relay 和观察者隐藏令牌数量，但负责解密的通知服务器仍能看到这一数量。

### Marmot 为新成员加入推送令牌修复 {#marmot-adds-push-token-repair-for-new-members}

10 月 26 日，Marmot [合并了针对新成员的推送令牌修复](https://github.com/marmot-protocol/marmot/pull/447)，随后的[一项后续变更澄清了其最终措辞](https://github.com/marmot-protocol/marmot/blob/e8e09c822ca1a3874d2bd01c1f332d91e70bc97c/features/push-notifications.md)。添加新加入者的那个 Commit 的所有者应发送活跃的 kind 448 令牌快照和 kind 449 移除墓碑。kind 447 公告中可选的指纹集合，使对等方只需发送缺失的记录。排名前三的叶节点按错开的计时器作出响应，并受到针对每个发布公告叶节点的 24 小时速率限制。即使所有者处于离线状态，经转发的已签名记录和保留下来的移除墓碑也能修复缺失的令牌状态。

### 关于由 passkey 持有 Nostr 密钥的提案 {#proposal-for-passkey-held-nostr-keys}

一项[关于由 passkey 持有 Nostr 密钥的提案](https://github.com/nostr-protocol/nips/pull/2519)以 Nosskey 为基础；Nosskey 是一种将 passkey 与 Nostr 密钥配合使用的现有方案。带标签的句柄把通过 PRF/HKDF 派生的身份与存储的密钥区分开来，加密的 kind 31778 relay 记录则绑定依赖方、作者和凭据。缺失或未知的元数据不得悄然创建新身份。依赖方源的授权仍然适用，旧版 Nosskey 数据则需要一个显式的迁移读取器。除非另行备份，派生身份会随其 passkey 一同丢失。

### 关于 NIP-05 标识符 DNS 委托的提案 {#proposal-for-dns-delegation-of-nip-05-identifiers}

一项尚未合并的 [DNS 委托提案](https://github.com/nostr-protocol/nips/pull/2527)针对 [NIP-05 基于 DNS 的标识符](/zh/topics/nip-05/)增加了一种回退机制，仅在原始 HTTPS 查询返回 404 或 410 时适用。此时，客户端会读取一条指向 HTTPS 提供方的 `_nip05` TXT 记录。超时、TLS 或 CORS 失败、重定向以及密钥不匹配都绝不会触发该回退，DNS 中也不存储任何密钥。DNSSEC 是推荐项但并非必需，因此在 DNS 未签名的情况下，提供方的 TLS 无法独立验证原始域名的授权。旧版客户端无法解析仅通过委托提供的标识符。

### 软件应用目录以 NIP-82 名义提出 {#software-application-catalog-proposed-as-nip-82}

一项[软件应用目录提案](https://github.com/nostr-protocol/nips/pull/2526)在这个开放且未合并的 pull request 中把 NIP-82 用作拟议编号；该编号既未被分配，也未被采纳。它汇集了多个 kind：应用（32267）、发布版本（30063）、资产（3063）、精选（30267）、证书所有权证明（30509）以及目录 relay 列表（10067）。资产会标明其平台和运行时，并附带文件哈希。Android 资产还会额外加入签名证书哈希。证明签名表明发布者控制该证书，读取方仍须检查其过期和吊销情况。

### BIP 321 URI 被提议作为 NIP-A3 支付目标 {#bip-321-uris-proposed-as-nip-a3-payment-targets}

一项尚未合并的[新增 bip321 支付类型的提案](https://github.com/nostr-protocol/nips/pull/2522)面向 [NIP-A3 支付目标](/zh/topics/nip-a3/)，允许 kind 10133 event 携带完整的 `bitcoin:` URI，作为静态、可复用的支付指令。由于该目标会被重复使用，提案既不允许包含金额，也不允许包含一次性的 BOLT11 `lightning` 发票参数。金额由付款方选择，钱包则挑选自己支持的支付方式，同时保留 Lightning 地址回退。

### 关于通过 BIP 321 目标支付 zap 的提案 {#proposal-for-zaps-paid-through-bip-321-targets}

根据一项[关于通过 BIP 321 目标支付 zap 的提案](https://github.com/nostr-protocol/nips/pull/2521)，发送方通过 Ark（一种链下比特币协议）、Lightning 或链上方式，向接收方可复用的 NIP-A3 bip321 目标付款，然后发布一个 kind 9740 zap。回执密钥的持有者以 kind 9741 确认结算。这两个 kind 编号目前都仍是占位值。支付引用使用 [NIP-44 版本化加密](/zh/topics/nip-44/)加密给接收方选择启用的回执密钥，也只有该密钥能够确认这笔支付。第三方无法验证支付细节，因此确认结果取决于对接收方签名的信任。该提案并不取代 [NIP-57 Lightning zap](/zh/topics/nip-57/)。

### Ark 支付被提议纳入 Nostr Wallet Connect {#ark-payments-proposed-for-nostr-wallet-connect}

[Nostr Wallet Connect](/zh/topics/nip-47/) 即允许应用控制远程钱包的 NIP-47 协议，一项尚未合并的 [Ark 扩展提案](https://github.com/nostr-wallet-connect/nwc/pull/11)在其现有的 BIP 321 付款和收款支持中加入 Ark 指令，并为 `lookup_payment` 加入 Ark 支付记录，且不新增任何方法。只有当钱包支持相应的地址版本和网络，并且使用同一个 Ark 服务器时，才会采用该指令。否则，钱包会尝试 URI 中的其他指令。金额必须为整数聪，不做毫聪舍入；记录会把经服务器联合签名的支付与接收方已领取且可花费的资金区分开来。

### 为 Blossom 服务器提议的 Ark 支付头 {#ark-payment-header-proposed-for-blossom-servers}

[Blossom](/zh/topics/blossom/) 是在 HTTP 服务器上存储媒体 blob 的协议，一项[关于 Ark 支付头的提案](https://github.com/hzrd149/blossom/pull/116)在其 BUD-07 的 HTTP 402 需要付款响应中加入 `X-Ark`。该头携带一个 BIP 321 URI，其中包含每次请求新生成的 Ark 地址以及金额。该 URI 还可以选择以 Lightning 发票的形式携带同一笔支付。作为证明，客户端在结算后使用已付款的 Ark 地址重试。使用了回退方式的客户端则使用 Lightning preimage 重试。HEAD 请求不会附带证明进行重试，客户端会继续发起 GET 或 PUT。

### 用于在笔记中提及资产的 cashtag 提案 {#cashtag-proposal-for-asset-mentions-in-notes}

一项 [cashtag 提案](https://github.com/nostr-protocol/nips/pull/2528)定义了可选的标记化规则：对 `$` 后接二至六个 ASCII 字母的文本进行标记化，但代码、URL 和 Nostr 引用除外。单个 cashtag tag 用于设置显示模式，并可附加由作者选定的资产 ID，因为仅凭交易代码无法唯一标识一种资产。读取方会检查符号是否与链和地址相符，并标记不相符的情况，但不会为其重新打标签。可选的 `t` tag（形式为 `$ticker`）支持标准的 relay 搜索。

### Napplet 游戏手柄规范被撤回 {#napplet-gamepad-specification-withdrawn}

NAPs 仓库是发布 Napplet 规范的地方，它于 10 月 27 日[合并了一项移除游戏手柄规范的变更](https://github.com/napplet/naps/pull/129)。该变更删除了 NAP-GAMEPAD.md，并撤销了此前的采纳。目前没有任何游戏手柄 NAP 处于已采纳状态。

### Cyberspace 高度 tag 避免与群组 tag 冲突 {#cyberspace-height-tags-avoid-group-tag-collisions}

Cyberspace 是一个构建在 Nostr 之上的空间协议，它合并了自身的若干规范，这些规范称为 DECK。它们属于项目规范，并非官方 NIP。该规范现在[将背包和聊天上的高度 tag 从 `h` 重命名为 `H`](https://github.com/arkin0x/cyberspace/pull/73)。原来的小写 tag 与 NIP-29 群组 tag 冲突，导致 event 被拒绝或被错误归档。只有在缺少 `H` 时，读取方才会回退到旧版的 `h`。这只改动了项目规范。它既不修订 NIP-29，也不能证明已部署的客户端能够互操作。

### Cyberspace 隐藏音频 {#cyberspace-hidden-audio}

[DECK-0007 定义了隐藏音频](https://github.com/arkin0x/cyberspace/pull/79)：它是一个加密的 Blossom 文件，由已签名的背包或宝箱中的一个未签名 rumor 引用。这意味着隐藏它的人不会因一条单独签名、可播放的公开帖子而被归属身份。每次放置都使用新的密钥和密文，但任何人仍然可以分享该密钥。该规范并未声称加密能保证发现者的隐私，也未声称其 URL 规则能阻止所有 SSRF，读取方的支持仍在开发中。

### Cyberspace 公共模型与动画 {#cyberspace-public-models-and-animation}

[物品现在可以引用带有 bob（上下浮动）和 spin（旋转）动画的公共 SNO 模型](https://github.com/arkin0x/cyberspace/pull/74)，当模型无效或不可用时，则回退到旧的渲染方式。实时模型可能会变化或消失，项目也并未声称已被广泛采用。

### Cyberspace 物品、聊天与评论规范 {#cyberspace-item-chat-and-comment-specifications}

[可选的 DECK 0004 至 0006](https://github.com/arkin0x/cyberspace/pull/67) 记录了物品、宝箱、商品列表、加密本地聊天和密封评论的现有代码，并附有合成测试向量。若干问题仍未解决。背包和宝箱的签名方式不同，密封评论会通过公开 tag 暴露父级 ID 和 kind。持有者可以覆盖商品列表。聊天在重放和上下文绑定方面存在缺口，宝箱引用也尚未实现。这些文档没有修复任何安全问题，也不代表已经部署。

### 多作者 event 提案 {#multi-author-events-proposal}

一篇已签名的长文《[以软分叉方式实现多作者 Nostr Event](https://njump.me/nevent1qqszlhx6hpwf0th2mk760n7cxqdknglwshgprpupsk4tj0nkr2n66wgzypzcxhpk7swe0x7gz2vrpuh4myjk9af584h7mht0xz48jjq8xrexuxjg87j)》提出了一种 event：其 ID 哈希涵盖多个作者 pubkey，每位作者都对同一个 ID 签名。旧版客户端会看到一个与 secp256k1 兼容的包装层，其中携带新格式的数据，以及用作查找提示的 Q tag。对等方将按每条连接协商新格式。这篇文章是对作者早先后量子提案的推广，那项提案会把一个未来的密钥作为又一名共同作者加入。这是一项未编号的提案，并非已被接受的 NIP。共同作者的 naddr 替换和二进制传输仍是悬而未决的问题。

### Buzz NIP-AR 同步订阅在推送实时头部之前先发送完整快照 {#buzz-nip-ar-sync-subscriptions-send-a-complete-snapshot-before-live-heads}

Buzz 的一个开放 pull request 提议了 [NIP-AR](/zh/topics/nip-ar/) WebSocket 同步订阅（[#8522](https://github.com/block/buzz/pull/8522)）。relay 将发送一个在 REPEATABLE READ 下读取的一致工件集合，仅在该集合完整后才发出 EOSE，随后以流式方式推送实时的当前头部；实时的 Redis 注册发生在初始读取之前。Redis 断开连接或出现滞后时，订阅会以 CLOSED 结束并需要重新同步，访问权限变更、内容撤除（redaction）或队列已满时也是如此。每个订阅的上限为 4,096 个工件；截至我们的资料截止时间，该变更尚未合并，也未在生产环境中提供。

### Buzz 通过 HTTP 增量读取 NIP-AR 工件 {#buzz-nip-ar-incremental-artifact-reads-over-http}

Buzz 的另一个开放 pull request 为 NIP-AR 工件加入了增量 HTTP 读取（[#8523](https://github.com/block/buzz/pull/8523)）。客户端按数据库修改时间戳和稳定 ID 分页，重叠窗口为 120 秒，收到的要么是当前修订版本，要么是一条移除记录。客户端可以恢复已知的 ID。结果采用最终一致性模型。该提案不承诺提供完整快照，某个工件不存在也不意味着它已被删除或访问权限已丢失。其最新修订版本要求具备成员资格，对于未公开列出的开放频道则要求显式的 #h 范围；列出状态一旦变更，就会重置增量进度。功能开关 BUZZ_ARTIFACT_INCREMENTAL_ENABLED 处于关闭状态，并要求所有写入方和迁移（现为 0074 至 0076）均已就位。这一 120 秒延迟属于运行假设。截至我们的资料截止时间，该变更仍处于开放状态。

### 关于委托指标读取方的 NIP-AM 草案文本 {#draft-nip-am-text-for-delegated-metric-readers}

Buzz 的一个文档草案 pull request 为 [NIP-AM](/zh/topics/nip-am/) 指标规定了委托读取方，但不改变运行时授权（[#8582](https://github.com/block/buzz/pull/8582)）。加密给所有者的 kind 44200 event 保持不变，agent 会为每项有效授权另外发出一份 NIP-44 副本，并将其绑定到由所有者撰写的授权 event 的确切 ID。拟议的授权 kind 30180 和读取方数量上限仍是悬而未决的问题，历史记录、撤销和公开关联也同样如此。已签名的撤销无法抹除接收方已持有的副本；截至我们的资料截止时间，该草案尚未合并。

### DECK-0003 允许父对象携带其放置的对象 {#deck-0003-lets-a-parent-carry-the-objects-it-places}

Cyberspace 的一个开放 pull request 提议了 DECK-0003 §1.10，即一个内联 SNO 对象载荷的根表（[#81](https://github.com/arkin0x/cyberspace/pull/81)）。只要父对象的副本中存在某个条目，该条目就会优先生效而无需网络获取，即使条目无效也是如此。每个条目都限定在作者 pubkey 范围内，并带有大小和深度上限以及循环限制。旧版读取方会获取缺失的对象并显示占位符。该提案描述了一些因等待此变更而暂缓的实现；截至我们的资料截止时间，此变更尚未合并。

### DECK-0004 定义了带派生房间密钥的高度绑定门 {#deck-0004-defines-height-bound-doors-with-derived-room-keys}

Cyberspace 的一个开放拉取请求为 DECK-0004 新增了关于 looks 和 doors 的 §3.6 与 §3.7（[#82](https://github.com/arkin0x/cyberspace/pull/82)）。门与高度绑定，房间密钥为 SHA-256(域分隔符 ‖ 位置密钥 ‖ 门秘密)，房间的 bag 用该密钥加密。一个房间可以有多个门或嵌套的门，设置新锁会轮换密钥。在首个实现出现之前，该文本不含测试向量；截至我们的资料截止时间，它尚未合并。

### nostream NIP-11 对等互联公告扩展 {#nostream-nip-11-peering-advertisement-extension}

nostream 的一个开放拉取请求将为该 relay 的 NIP-11 文档增加 peering 部分（[#999](https://github.com/cameri/nostream/pull/999)）。它公告带有时间界限和结算条款的 feed kind，同时提供一个联系端点和对等互联工作量证明。只有 `enabled: false` 会禁用该部分，空条款则表示免结算对等互联。公告出的报价并不等于已接受的对等方。该变更没有实现任何对等协议或付费联邦。截至我们的资料截止时间，它尚未合并。

### NIP-CD 新增可选的已安装命令列表 {#nip-cd-adds-optional-installed-command-lists}

NIP-CD 的一项后续修改已于 10 月 27 日[合并到 NIPs 默认分支](https://github.com/nostr-protocol/nips/pull/2525)（[合并][cd-installed-merge]），该规范现在的标题为 Slash Commands。它定义了一个遵循 [NIP-51](/zh/topics/nip-51/) 的可选 kind 10992 列表，用户在其中保存指向 kind 31992 命令定义的地址 tag，每个定义由执行者 pubkey 和 d 值标识，并可附带可选的 relay 提示。用户可以维护该列表，客户端应将其用于自动补全和渲染出的标签块。该列表是一种显示与发现偏好。它不为执行者授权；没有该列表时，纯文本调用仍然有效，既不需要特定于命令的 tag，也不要求客户端支持。NIP-CD 仍是可选草案，此次合并也并未表明哪些客户端已采用该列表。

### Marmot 收窄针对账户设备的公平准备规则 {#marmot-narrows-its-fair-preparation-rule-for-account-devices}

Marmot 于 10 月 28 日[合并了一项更正](https://github.com/marmot-protocol/marmot/pull/450)，修订其针对要求账户设备的群组的调度规则。在一次有界收敛过程达到 Stable 之后，一个由管理员授权的排队意图，或来自同一账户的一个被允许的意图，会先获得一次准备尝试，之后仅凭排队的入站工作才能强制触发另一轮过程。SelfUpdate 和 Leave 不在这项额外公平保证的范围内，不过任何成员仍可提交它们。该变更更正了此前覆盖所有已授权意图的措辞，不要求账户设备的群组则保持原有调度。线路格式没有变化，而一次准备尝试也不保证产生有效、被接受或规范的 Commit。

### Marmot 提议为账户群组引入隐藏设备名册 {#marmot-proposes-a-hidden-device-roster-for-account-groups}

Marmot 的一项开放提案（尚未合并）[将新增 device-roster-v1 组件](https://github.com/marmot-protocol/marmot/pull/452)，其 ID 为 0x800e，用于一个所有叶节点都属于同一账户的隐藏群组。群组要么从创建时起就携带该名册，要么永远不携带。名册记录设备、被拒绝的槽位、被拒绝的 KeyPackage 以及叶映射，它也是首个使用显式、与顺序无关的差异更新并将其应用于候选父级的组件。已移除的槽位可以为某些群组保留叶映射，因为其兄弟设备无法将它们从这些群组中移除。设备只有在自己创建了某个设备群组，或通过经已确认链接认证的 Welcome 加入该群组时，才会信任该群组，因此仅凭 0x800e 标记并不授予任何信任。创始 Add 会指明来自已确认链接的那个确切 KeyPackage。被盗的已链接设备在被移除之前都可以编辑名册。设备上限适用于设备。叶映射记录和被拒绝记录有逐条大小限制，但没有记录数量上限。名册数据从不复制到其他账户，该群组在聊天、计数、通知和目标位置中始终保持隐藏。提案正文称，MDK 将名册字节置于测试开关之后，且不新增普通 UI。

### Marmot 提议在账户设备激活失败时提供更清晰的反馈 {#marmot-proposes-clearer-feedback-when-account-device-activation-fails}

Marmot 的另一项开放提案（尚未合并）[将允许客户端解释账户设备的激活失败](https://github.com/marmot-protocol/marmot/pull/453)。客户端可以报告某个群组无法激活账户设备。这种群组级反馈不能指明阻碍激活的成员或设备。不是活跃管理员的成员只会得知自己缺少管理员身份。如果分支选择丢失，或重新生成的激活检查失败，用户必须重新发起请求。客户端从不自动重试激活。激活需要由已授权客户端发起新的用户请求，这一现有规则保持不变。这是规范性草案文本，并不表明已实现或已部署的行为。

### Marmot 提议使用表情符号验证来配对新设备 {#marmot-proposes-emoji-verification-for-pairing-new-devices}

Marmot 的一项开放提案（尚未合并）[描述了配对新设备的流程](https://github.com/marmot-protocol/marmot/pull/454)，其交换过程以 Matrix m.sas.v1 为蓝本，使用 X25519、HKDF 和 HMAC。用户在两块屏幕上比对七个带标签的表情符号，无需读取或输入代码。仅持有账户密钥从来不能认证设备。五条未签名的 rumor（Request、Answer、Reveal、Confirm 和 Cancel）被封装发送给账户 pubkey，并绑定账户、会话、新的 KeyPackageRef、现有设备槽位以及新生成的密钥。现有设备先确认，并且只添加已确认的那个 KeyPackageRef。新设备只有在完成验证后才会确认，并且只接受针对经已确认交换认证的群组 ID 的 Welcome。提案拟使用 kind 452 至 456，并保留 457 至 489。即使在确认之后，账户密钥持有者仍可伪造 Cancel 来造成拒绝服务。每小时的 Answer 限额在重启后不会保留。relay 可以看到封装消息的突发和账户地址；部分合并和 Welcome 情形仍被推迟处理。各实现默认关闭这些格式，而作者提供的两个已知答案向量并不构成独立的安全或互操作性审计。

### NIP-5D napplet 提案收紧媒体与来源字段 {#nip-5d-napplet-proposal-tightens-media-and-source-fields}

此前已介绍过[开放的 NIP-5D napplet 提案](https://github.com/nostr-protocol/nips/pull/2303)。它在 10 月 28 日的修改现已合并到提案分支，而非 NIPs 默认分支，修订了 10 月 17 日引入的可选媒体和来源字段。截图和预览 tag 现在复用 [NIP-92](/zh/topics/nip-92/) 的键值字段，其中包含一个必需的小写 SHA-256 x 值，以及可选的 m、dim、size、alt 和 duration。读取方在渲染前必须校验哈希并解码实际格式。如果存在有效的 m 字段，解码出的格式还必须与该 MIME 类型一致。x 缺失、重复或错误的条目会被忽略；错误的可选字段会被丢弃，但不会因此舍弃其他可用媒体；多个预览则会被忽略。source-commit 必须解析为确切的完整 Git ID，HTTPS 源码归档则需要与 SHA-256 逐字节精确匹配。重复或格式错误的来源字段会被忽略，不可用的来源数据也不得阻碍 HTML 播放。匹配的提交或归档并不能证明构建可复现，也未声称有任何客户端符合规范。

## Nostr 的六个十月 {#six-years-of-nostr-octobers}

在六个十月里，Nostr 有明确日期的变更从消息分帧逐步向外延伸到构建于其上的应用。2021 年，基础规范[确定客户端消息以顶层 JSON 数组分帧](https://github.com/nostr-protocol/nostr/commit/69509f40cd6a4d5c14a7c402b04495a1de5ab2c2)。此后的几个十月相继带来了客户端搜索和闪电网络发票、时间戳证据和任务请求、媒体变体和 ecash 钱包，然后是代码协作和私信元数据。同样这些月份里的其他变更，让身份和连接更容易在不同程序之间携带，从可见的 relay 状态，到独立的签名者密钥和钱包配对。今年十月，同一份文档[定义了空过滤器列表匹配什么](https://github.com/nostr-protocol/nips/commit/37db639582d857e12468dcccd99b2c7f1d657da9)，读取相同 JSON 的 relay 因此对它选中哪些 event 有了共同规则。

### 2021 年 10 月：让传输层毫无歧义 {#october-2021-making-the-transport-unambiguous}

10 月 4 日，基础协议规范 [NIP-01](/zh/topics/nip-01/) [经过修订，规定客户端消息为顶层 JSON 数组](https://github.com/nostr-protocol/nostr/commit/69509f40cd6a4d5c14a7c402b04495a1de5ab2c2)。非正式的 EVENT、REQ 和 CLOSE 前缀变成了每个数组的第一个元素，固定的 `/ws` 路径要求也被删除，因此任何 WebSocket 端点都可以使用。这次修订澄清的是一份背后已有代码的规范。独立编写的客户端必须先有精确的分帧，更复杂的功能才能互操作。

10 月 23 日，[relay 到客户端的方向新增了明确的 EVENT 和 NOTICE 消息](https://github.com/nostr-protocol/nostr/commit/97786e31423b45239306323a9a297188d20dbf21)。relay 发出的 EVENT 带有某个现有 REQ 订阅的标识符，使在一个连接上运行多个订阅的客户端能把结果与请求对应起来，NOTICE 则携带人类可读的文本。如此精简的词汇表可以切实地被多次实现，这正适合各自独立运营的 relay。

[10 月 23 日版本的 NIP-01 文本](https://github.com/nostr-protocol/nostr/blob/97786e31423b45239306323a9a297188d20dbf21/nips/01.md)还说明了签名覆盖哪些内容。event 的 ID 是一个紧凑 UTF-8 JSON 数组的摘要，该数组包含开头的零、作者公钥、时间戳、kind、tag 和内容，作者用 secp256k1 曲线上的 Schnorr 签名对该摘要进行签名。WebSocket 封装和订阅标识符都位于这些签名数据之外。由该文本可以推知，同一个已签名 event 可以经由不同订阅或不同连接到达，而无需重新签名。REQ 先返回匹配的已存储 event，然后保持实时状态，直到客户端发送 CLOSE、关闭套接字，或为新的 REQ 复用该订阅 ID。单个过滤器内的每个条件都必须成立，而一个 REQ 中的多个过滤器会匹配满足其中任意一个的 event。该版本中的过滤器名称与今天不同。NOTICE 的行为未作规定，也没有任何内容承诺 relay 会保留 event 多久，或承诺查询会返回全部 event。五年后，同一份规范将重新回到 REQ 内过滤器含义这一问题上。

### 2022 年 10 月：信息流在手机上变得可用 {#october-2022-a-feed-becomes-usable-on-a-phone}

10 月 8 日，iOS Nostr 客户端 Damus [新增了对话题标签、个人资料和 event 的搜索](https://github.com/damus-io/damus/commit/2c4c392b76d9ad92b28e71d6d578bdb42c2ac3de)。这项变更涉及其搜索结果视图和帖子串模型，让读者除了滚动浏览传入的文字之外，还能直接跳转到某个已签名身份或特定 event。该搜索在客户端自身的导航内运作，并非 relay 端的全文搜索。

八天后，Damus [将其 relay 配置中的普通行替换为显示每个连接状态的视图](https://github.com/damus-io/damus/commit/e5e0fb2db279a5a2763d39b15d5fff20bec26fdd)。一个彩色圆点读取客户端的 relay 池。绿色表示已连接，黄色表示正在连接或重新连接，其他状态一律为红色，首次读取之前则为灰色。该视图在出现时刷新，此后每两秒刷新一次。原有的滑动删除功能移到了新视图中。有了这些圆点，停滞的信息流不必再被理解为作者沉默，因为读者可以看到几个独立连接中哪个已连通、哪个正在重试。绿点表示套接字已打开。它并不表示 relay 接受或保存了某个 event。它也不表示查询返回了 relay 所持有的全部内容。该提交记录的是已合并源码中的实现。这一源码变更并不能确定任何 App Store 发布日期。

10 月 19 日，Damus [新增了 BOLT11 闪电网络发票解析器和发票小组件](https://github.com/damus-io/damus/commit/c6ab1de63926ff7f6e29a260e3e7f2473855c9c7)，用于帖子、聊天和私信。该小组件显示发票描述和以聪计的金额，其 Pay 按钮通过 iOS 将 `lightning:` URI 传递给已安装的处理程序。社交客户端负责展示已签名的帖子，由独立的钱包完成支付。这些小组件早于后来的 zap 收据约定，因此它们只是发票展示，而非标准化的 zap。

### 2023 年 10 月：event 承载证据与工作请求 {#october-2023-events-carry-evidence-and-requests-for-work}

10 月 11 日，将 event 相关证据锚定到比特币中的 [NIP-03](/zh/topics/nip-03/) OpenTimestamps 证明，[从 event 上的 `ots` 字段移到了独立的 kind 1040 event](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)。该 event 用 `e` tag 指明原始 event，并在内容中携带完整的 base64 OpenTimestamps 文件，其中至少包含一个比特币证明。被引用的 event id 本身就是该证明所证明的摘要，因此验证者可以得知该 event 在所证明的时间之前就已存在。这个时间来自比特币，而非作者的 `created_at`。该证明为 event 确定时间，并不对其内容作出任何断言。

10 月 12 日，与时间戳变更无关，[NIP-06](/zh/topics/nip-06/) 密钥派生[新增了两个测试向量](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)。助记词是一串编码了恢复种子的单词，这些向量涵盖一个 12 词助记词和一个 24 词助记词，每个都附有预期的私钥和公钥，分别以十六进制以及 nsec 和 npub 编码表示。NIP-06 原本就使用 BIP-39 将助记词转换为二进制种子，并使用 BIP-32 路径 `m/44'/1237'/<account>'/0/0` 派生密钥，以账户零作为基本的单密钥选择。十月的这次补充提供的是已知答案，而不是助记词恢复功能或新的派生算法。客户端现在可以检查自己的派生和编码能否复现文档所记载的身份。与这些向量相符，使各实现之间可以相互比较。它并不认证任何特定实现，也不能证明所有钱包和客户端的导入结果都一致。保护种子免遭窃取是另一回事，这些向量并未涉及。

10月29日，数据自动售货机（data vending machine）标准 [NIP-90](/zh/topics/nip-90/) [以固定的任务 kind 合并进 NIPs 仓库](https://github.com/nostr-protocol/nips/commit/7a2de8ab25ceaa35376e6b7457f08b5bffde70b3)。该标准为任务请求保留了 kind 5000 至 5999，并规定每种结果 kind 等于对应的请求 kind 加 1000。反馈使用 kind 7000。请求可以指向文本、URL 或先前的任务，也可以注明期望的输出，并附上可选的出价。这样一来，任务就存在于任何提供方都能响应的已签名 event 之中，不再受制于某一家供应商的 API。更早的一份草案曾使用 kind 68001 和 68002。

### 2024 年 10 月：媒体替代版本与可移植的 ecash {#october-2024-media-alternatives-and-portable-ecash}

10月15日，[NIP-71](/zh/topics/nip-71/) 视频 event [开始用 `imeta` tag 表示视频变体](https://github.com/nostr-protocol/nips/commit/1cda2dcc594538ea14b88aec7f1f784e06a31bbf)。在当时现行的可寻址 kind 34235 和 34236 中，每个变体的 URL、尺寸、MIME 类型、预览图和后备地址都集中放在同一个 tag 里。客户端挑选分辨率时，需要知道哪个缩略图和后备地址属于该分辨率，而扁平化的元数据无法表明这一点。这些 kind 编号已属历史：现行的 NIP-71 使用 kind 21 和 22。

十天后，此前都已在早期草案中提出的 [NIP-60](/zh/topics/nip-60/) Cashu 钱包和 [NIP-61](/zh/topics/nip-61/) nutzap [作为规范一并合并](https://github.com/nostr-protocol/nips/commit/ba46b23d95b186c9a8fedabf8324af2ae40e8ce4)。二者都建立在 Cashu 之上，这是一种由铸币方（mint）发行代币的 ecash 协议。NIP-60 将加密的钱包证明（proof）保存在 relay 上，使兼容的应用都能获取同一份钱包状态。按照 NIP-61，接收方的 kind 10019 event 列出其信任的 mint、relay 以及一个锁定密钥；发送方的 kind 9321 event 则携带锁定到该密钥的证明，供接收方兑付。用户仍然依赖发行代币的 mint，应用也必须防范同一批证明被重复兑付。

10月29日，[NIP-46](/zh/topics/nip-46/) 远程签名（即由一个独立服务持有密钥并代表用户签名）[经过修订，使 `bunker://` 连接字符串携带远程签名器的公钥](https://github.com/nostr-protocol/nips/commit/f1e8d2c4f764d66996c0c1fb2eeabfbc0c7b2528)。用户身份则需另行获取：[修订后的文本](https://github.com/nostr-protocol/nips/blob/f1e8d2c4f764d66996c0c1fb2eeabfbc0c7b2528/46.md)要求客户端区分这两个密钥，并在连接后调用 `get_public_key`。客户端为这次会话生成自己的密钥对，并将加密请求发往签名器的密钥，而 `sign_event` 返回的是用用户密钥签名的 event。这两个密钥可能相同，但并不必须相同。连接字符串中的密钥只用于标识签名服务。用户的账户是 `get_public_key` 返回的公钥。四天前，NIP-60 处理的是共享钱包状态；这次修订处理的则是另一个问题，即签名器身份。该提交中的示例仍使用 NIP-46 当时规定的加密传输方式。这项变更既没有让远程签名器变得无需信任，也不能证明究竟是谁持有用户的密钥。

### 2025 年 10 月：协作更新与私信元数据 {#october-2025-collaboration-updates-and-private-message-metadata}

10月8日，[NIP-47](/zh/topics/nip-47/) Nostr Wallet Connect [新增了用于将应用与钱包配对的深度链接](https://github.com/nostr-protocol/nips/commit/2ace01cf1ad0a68dae6217111c9286e3de759923)。钱包可以注册 `nostrnwc://connect` 或应用专属的 `nostrnwc+{app_name}://connect`，发起请求的应用则带上经过 URI 编码的图标、自身名称和一个回调 scheme 来打开该链接。钱包创建好连接后，会打开该回调，并附上一个 `value` 参数，其中包含配对码，也就是一个 `nostr+walletconnect://` URI。在 Damus 通过 iOS 把发票交给钱包的三年之后，在同一部手机上完成配对，终于不必再扫描显示在同一屏幕上的二维码，或在应用之间复制一长串字符。这项新增内容只涵盖这一交接环节。它没有改变任何支付方法，本身也不会支付任何款项。两个应用都必须实现相应的处理程序，而规范文本并不能证明每个钱包都已实现。支出预算、授权确认界面，以及哪个应用可以安全地拥有某个回调 scheme，这些问题它也都没有解决。

10月16日，[NIP-34](/zh/topics/nip-34/) git 协作在已有的补丁 event 之外，[新增了 kind 1618 拉取请求（pull request）event 和 kind 1619 更新 event](https://github.com/nostr-protocol/nips/commit/6e6b9877b32b44e84c0f3c3d412d688cf86761b0)。拉取请求指明一个 commit 顶端（tip）和若干克隆地址，更新则移动该顶端。补丁建议小于 60 kB，更大的提交内容则建议使用拉取请求。由此，较大提交内容的推荐途径从放在 event 内部的补丁正文，转向了对 commit 的签名引用，而较小的改动仍可以作为补丁传递。Nostr 承载协调信息和签名引用，这些引用所指向的 commit 对象则仍由 Git 服务器提供。

10月27日，[NIP-59](/zh/topics/nip-59/) gift wrap [新增了一项指引：在添加过期 tag 时，对 seal 和 gift wrap 的时间戳分别独立随机化](https://github.com/nostr-protocol/nips/commit/bcaad2957d0e9cec20e4265298d2788be87d3190)。Gift wrap 用这两层包裹一条消息，而为每一层赋予各自的随机时间戳，可以降低各层时间之间能被关联的紧密程度。此时，关注点从加密内容转向了限制元数据关联可能暴露的信息。加密隐藏了消息本身，但信封周围的时间信息和其他元数据仍然可被观察到，而实现上的选择决定了它们有多容易被关联起来。这项指引没有增加新的加密，也不会让参与者变得匿名。

### 2026 年 10 月：共享的查询含义与文本触发的服务 {#october-2026-shared-query-meanings-and-text-triggered-services}

10月5日，[NIP-92](/zh/topics/nip-92/) 媒体附件[将 `imeta` tag 扩展到 kind 0 个人资料](https://github.com/nostr-protocol/nips/commit/a79e21d90fce5465b50ef385dd368bba99ec4a0b)，使个人资料能够为其 `picture` 和 `banner` 描述后备 URL、blurhash（一种对模糊预览图的紧凑编码）、尺寸、替代文本以及其他附件元数据。NIP-92 在这次变更之前就已存在；新的地方在于，NIP-71 于 2024 年用于视频变体的分组元数据，如今延伸到了个人资料图片。关联采用精确匹配。只有当 tag 的 URL 与头像或横幅的 URL 完全相同时，该 tag 才适用；客户端应当（SHOULD）忽略两者都不匹配的 tag，并且在主 URL 失效时应当（SHOULD）尝试后备地址。由于新的 kind 0 event 会替换先前的个人资料，发布者应当（SHOULD）为未更改的图片沿用原有元数据，并删除不再使用的图片所对应的 tag，以免过时的替代文本或尺寸悄然描述另一张图片。这条更新规则与新增字段同样重要。`imeta` tag 并不能保证图片持续可用，也不能保证加载更快。它同样不提供任何隐私保护，客户端也不必渲染每一个字段。

10月17日，[NIP-01 得到澄清：过滤器中的空列表不匹配任何 event](https://github.com/nostr-protocol/nips/commit/37db639582d857e12468dcccd99b2c7f1d657da9)，这与省略该属性不同。[一次后续修改删除了不一致的“一个或多个”措辞，并建议客户端避免发送不可能匹配的列表](https://github.com/nostr-protocol/nips/commit/0b5532c0355ab27f447e071a93c09cf3a2b4aad5)。2021 年 10 月，这份文档就 REQ 的 JSON 消息封装形式达成了一致：REQ 消息是一个数组，每个过滤器是其中的一个 JSON 对象。今年 10 月，它确定的是过滤器语义，明确了此类过滤器中的空列表意味着什么，因为即使各个 relay 以相同方式解析同一帧，返回的结果仍可能不同。

10月21日，[NIP-CD（当时名为 Commands）从提案转为已合并的草案规范](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)；NIP-CD 描述的是斜杠命令。kind 31992 event 用于定义命令，而调用就是从某个 event 内容的第一个字符开始的纯文本，因此客户端无需任何特殊支持即可发送。一项[后续提案](https://github.com/nostr-protocol/nips/pull/2525)连同另一个分支上的一个[更早的提交](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)，于 [10月27日合并](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)。它将该规范更名为 Slash Commands，并新增了可选的 kind 10992 已安装命令列表，客户端应将其用于自动补全和渲染。这些列表记录的是用户偏好，既不为执行方授权，也不限制纯文本调用。NIP-90 任务使用结构化的请求 event 和结果 event，而命令始终是可读的普通文本。
