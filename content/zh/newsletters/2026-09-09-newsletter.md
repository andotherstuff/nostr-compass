---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "Nostr Compass #39 关注签名式 git 工作流、浏览器发布、自托管直播、社区中继同意机制、私密事件、重点版本发布，以及 NIP-21/NIP-27 链接契约。"
---

欢迎回到 [Nostr Compass](https://nostrcompass.org)，这里是你的每周 Nostr 指南。

**本周内容：**[ngit 和 GitWorkshop](https://ngit.dev/v3)将签名式 git 工作流迁移到 Nostr 和 [Blossom](/zh/topics/blossom/)，[nsite-clay](https://github.com/jooray/nsite-clay)让浏览器发布可从故障中恢复，[Wingman App](https://github.com/OtherStuffAI/wm-app)则将浏览、设备本地签名、身份验证和文件功能整合起来。[Shosho 和 Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0)把自托管直播接入 Nostr，[Communitator](https://github.com/dyne/communitator)让用户可以在签名前检查中继模板，[cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)发布可预约时段，[Plektos](https://github.com/derekross/plektos/pull/16)则为私密事件提供加密。带标签的版本发布为 [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4)、[Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27)、[LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) 和 [SkateSpots](https://zapstore.dev/apps/org.skatespots.app)加入了恢复与隐私方面的改进。开发工作涵盖 [NIP-27](/zh/topics/nip-27/) 渲染、[Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397)中的签名中继偏好、[NIP-A3](/zh/topics/nip-a3/) 支付目标以及 Blossom 镜像。[NIPs 仓库](https://github.com/nostr-protocol/nips)中已合并的变更进一步明确了仅限直播的订阅和经过身份验证的应用数据。本期深入解析将说明 [NIP-21](/zh/topics/nip-21/) 链接和 NIP-27 引用如何在不同应用之间传递 Nostr 个人资料与事件。

## 重点动态

### 签名式 git 工作流将 CI、私有仓库和版本发布迁移到 Nostr

[9 月 8 日发布的 v3](https://ngit.dev/v3) 将 ngit、GitWorkshop、ngit-grasp 和 ngit-ci 整合进同一个签名式工作流。[ngit](https://ngit.dev/ngit.git)以 [NIP-34](/zh/topics/nip-34/) 事件的形式承载分支、补丁和拉取请求，[GitWorkshop](https://ngit.dev/gitworkshop.git)则提供评审界面。此次发布新增了 ngit-ci 0.1，这是一项自托管持续集成服务，其指令和结果以签名 Nostr 事件的形式传输，因此检查任务可以在维护者控制的硬件上运行，并与代码评审协同进行。

同一版本还通过 GRASP-08 私有仓库扩展为 [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) 提供私有仓库功能，并明确维护者权限。签名发布记录可以指向 [Blossom](/zh/topics/blossom/) 中的资源，使发布元数据和按内容寻址的文件都能脱离托管式代码锻造平台。[新版文档站点](https://ngit.dev/v3)汇集了客户端、私有仓库、CI 和网页组件的相关文档。

### nsite-clay 让浏览器发布可从故障中恢复

[8 月 31 日的签名器提示修复](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8)、[发布恢复功能](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0)以及[9 月 2 日加入的编辑控件](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7)，让 [nsite-clay](https://github.com/jooray/nsite-clay) 成为适用于单页站点的浏览器发布工具。用户可以直接编辑文档对象模型，将结果序列化，作为按内容寻址的 [Blossom](/zh/topics/blossom/) 数据块上传，然后重新发布站点的 [NIP-5A](/zh/topics/nip-5a/) 清单。整个过程不需要本地构建或服务器。

这款[浏览器发布工具](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html)现在可以从发布失败中恢复，并减少重复出现的签名器提示，[编辑指南](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html)则记录了这一操作流程。最终生成的仍然是可供现有网关使用的普通 NIP-5A 站点。

### Wingman App 整合浏览、签名和文件功能

9 月的开发工作为 [Wingman App](https://github.com/OtherStuffAI/wm-app) 加入了[文件选择器](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec)、[个人资料发布](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704)、[安全的签名器和会话恢复](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6)，以及[经过测试的移动端构建](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac)。它的 Flutter 外壳会向应用内打开的页面注入 [NIP-07](/zh/topics/nip-07/) 提供程序，而 Flight Deck 和由 Tower 支持的 Drive 则在浏览器旁提供工作界面和文件工作区。

Wingman 使用 [NIP-98](/zh/topics/nip-98/) 为经过身份验证的 HTTP 请求签名。[请求实现](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs)会构建一个由服务器在响应前进行验证的事件，让同一个已安装身份能够通过一致的批准流程处理各种中继操作、网页应用签名和文件。

### Shosho 推出 Livelier 自托管直播流支持

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) 于 9 月 1 日发布，并支持 [Livelier](https://github.com/r0d8lsh0p/livelier)。Livelier 在 [8 月 31 日的来源标注更新](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc)中，会在桥接资料里标明桥接服务和 Owncast 来源。Livelier 监视 Owncast 的公开目录，检查视频流是否正在直播，然后发布一个可寻址的 `kind:30311` [NIP-53](/zh/topics/nip-53/) 事件。发现过程通过 Nostr 进行，而视频仍保留在直播者的服务器上。

聊天以 `kind:1311` 事件的形式通过桥接服务传输。该[桥接设计](https://github.com/r0d8lsh0p/livelier)仅在有 Nostr 阅读器订阅时建立来源端连接，为派生身份添加标记，并将临时聊天消息发送到一个会在三小时后将其删除的中继。发现中继仅接受来自桥接密钥的直播事件写入；聊天中继使用 [NIP-42 身份验证](/zh/topics/nip-42/)和 [NIP-70 受保护事件标志](/zh/topics/nip-70/)。

### Communitator 让用户能在签名前检查中继模板

[8 月 31 日的首发系列更新](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c)为 [Communitator](https://github.com/dyne/communitator) 提供了用于 kind `10002` 中继列表、kind `10063` Blossom 服务器和 kind `10050` 私信收件箱的规范模板。在签名器连接之前，应用会显示规范化的端点、读写权限、事件种类、固定发布中继和目标位置。

[受限的签名与发布流程](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501)将连接与应用操作分开。每个事件都单独签名，每次运行最多使用四个 WebSocket 连接，并且只有在收到肯定的 [NIP-01](/zh/topics/nip-01/) `OK` 响应后，目标位置才会被计为发布成功。结果会区分完整交付、部分交付、交付失败和交付取消。共享模板仍是不受信任的建议；[同意界面](https://github.com/dyne/communitator#security-and-consent)说明了中继和网络活动的可观察性。

### cal.emre.xyz 发布 NIP-52 预约可用时间

公开仓库通过 [9 月 2 日的初始提交](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)开放，随后又为 [cal.emre.xyz](https://cal.emre.xyz) 发布了一则经过签名的 [9 月 3 日处理程序公告](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac)。主持人将可用时间发布为 `kind:31923` [NIP-52](/zh/topics/nip-52/) 事件；访客则发布 `kind:31925` RSVP。

它从中继读取主持人的事件以及已接受且标记为忙碌的 RSVP，排除重叠的时间段，并将 Nostr 事件保留为日程记录，而不会将其复制到单独的数据库中。主持人可以使用 [NIP-07](/zh/topics/nip-07/)、[NIP-46](/zh/topics/nip-46/) 或本地密钥签名；访客可以生成单独的密钥。其[仓库](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)还会提供生成的 `naddr` 和日历链接，并默认禁用电子邮件。

### Plektos 将每个私密活动设为单独的加密频道

[9 月 2 日的私密活动实现](https://github.com/derekross/plektos/pull/12)会将每场 [Plektos](https://github.com/derekross/plektos) 聚会设为 [Concord](/zh/topics/concord-protocol/) 加密社区中的一个私密频道。嘉宾名单、RSVP 名册、报名板、讨论串、贡献内容、封面图片、编辑和删除操作都会一并加密；邀请仅携带该活动的密钥，不会发布任何明文日历事件。

[9 月 6 日的生命周期审计](https://github.com/derekross/plektos/pull/14)固定了事件定义的 id，以便在存在超过 500 个封装事件时直接查找，同时保留分页回退机制。邀请包会在活动结束 30 天后过期，也可以被禁用，但已经获得频道密钥的人仍可保留该密钥。另一项独立的[解析器安全修复](https://github.com/derekross/plektos/pull/16)会让格式错误的类型-长度-值（TLV）[NIP-19](/zh/topics/nip-19/) 标识符直接失败，而不是让解析器陷入异常。

## 带标签的版本发布

### Vector 0.4.4 提高加密社区恢复的安全性

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) 于 8 月 31 日发布，包含社区恢复、密钥轮换、管理和回复路由方面的修复。重新创建社区时，会关闭遭受攻击的社区中被攻击者利用的邀请路径；替代成员资格会覆盖过期的本地状态；单个无法联系的成员也不再导致成员名册冻结。系统会拒绝空轮换，晋升操作会保留在线成员，并且在无法联系到必要成员时拒绝执行相关操作。

该[版本](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4)还会持久保存管理员执行的删除和封禁操作，在密码更改后重新加密访客簿，在重启后仍将通知回复绑定到对应会话，并且仅使用经过验证的多人路径。这些是恢复控制措施，并不能撤销已经被他人获取的密钥。

### Primal Android 3.5.27 检查签名器和钱包身份

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) 于 9 月 3 日发布，此前[签名器身份检查](https://github.com/PrimalHQ/primal-android-app/pull/1108)和[钱包请求身份验证](https://github.com/PrimalHQ/primal-android-app/pull/1105)已于 8 月 31 日合并。如果请求中的身份与当前持有的账户不匹配，本地签名会拒绝该请求；传入的 [NIP-47](/zh/topics/nip-47/) 请求也会在处理前进行身份验证。当 Zap 投票出现在回复中时，其路由现在还会将投票发送给投票发起者。

### GRAIN 0.8.0-rc2 修复了已确认但未存储的路径

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) 于 9 月 7 日发布。此前，由于其异步 LMDB 数据库写入器未能及时发现存储空间已满，中继可能在存储失败前返回 `OK`。中继现在会在存储使用率达到 80% 和 95% 时发出警告，在达到 97% 时拒绝新事件并为删除操作保留空间，同时报告事件接受后发生的写入失败。保留机制按从旧到新的顺序遍历数据，关闭过程可以处理迟到的消息，无效过滤器也不再导致同组中的有效过滤器被丢弃。

该[版本](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2)还会核验 kind `10166` 监控公告和 kind `30166` 中继报告，清除过期报告，保留已配置中继作为后备，并通过 [NIP-11](/zh/topics/nip-11/) 报告实时限制和身份验证信息，而不是静态的零值。

### LibreNostr 0.5.0–0.5.2 让 Tor 路由在故障时默认关闭

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) 于 9 月 7 日发布，新增 Orbot 模式，通过同一个 SOCKS 端口路由中继连接、zap、上传、媒体、播放和预览，并修复了 zap 面板崩溃问题。如果 Orbot 或代理不可用，连接会停止，而不会泄漏到直接路由。[版本 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) 防止缓慢的 [NIP-50](/zh/topics/nip-50/) 搜索延迟本地结果；[0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) 替换了递归式线程布局，并修复了线程排序。

这种[故障时默认关闭的行为](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0)适用于该版本列出的所有网络访问面。由于这些客户端长期存活，因此需要重新启动。后续补丁版本保留了这一选择，同时限制了无关的搜索、堆栈深度和布局故障。

### SkateSpots 新增设备端中继路径

经过签名的 [9 月 8 日 Zapstore 版本](https://zapstore.dev/apps/org.skatespots.app)为 SkateSpots 新增了可选的 Citrine 中继。地点、团队、消息和地图数据可以在本地加载；帖子可在离线时排队；手机也会保留本地副本。现有的私藏和消息内容仍采用端到端加密。付款检查要求提供发票金额以及服务提供方签发的 zap 收据，之后才会授予访问权限或计入贡献。

这个[本地中继](https://zapstore.dev/apps/org.skatespots.app)是用于存储和保持连续性的选项，并非所有远程中继的替代品。它让滑手可以在断网期间继续使用，并在恢复连接后同步已签名的活动；与此同时，付款机制的改动可防止自行生成的收据被用作结算证明。

### Whistle 1.8.15 修复加密群组的生命周期恢复问题

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) 于 9 月 3 日发布。此前完成的一项 Android 生命周期修复，防止了路由级状态持有者销毁应用级中继订阅和位置更新。其发布说明还提到，设备锁定或进入休眠后连接状态能够刷新，并且在观测案例中恢复了积压的 501 个事件。

这个[缺陷](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15)将长期运行服务的所有权绑定到了短期存活的界面。让 activity 作用域的实例保持存活，并在单次读取前检查套接字，可降低普通 Android 导航和后台挂起被误判为群组为空的可能性。

### TWENTY ONE Companion 1.12.0 将加密 DM 与旧版聊天分开

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) 于 9 月 5 日发布，新增采用 [NIP-17](/zh/topics/nip-17/) 礼物包装的 DM。加密收件箱与较早的空间聊天相互独立；后者仍然单独保留，因为这些消息从未加密，也无法迁移。在中继策略允许的情况下，系统支持 PDF 和视频；个人隐藏设置可以同步，但不会变成版主封禁。

这种[明确可见的分隔](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0)是安全模型的一部分。将旧历史记录称为安全收件箱会歪曲其来源，而静默迁移则会让人误以为这些消息在写入时采用了实际上并不存在的加密。

### ZapStore 1.1.2 验证事件 id 和证书轮换

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) 于 9 月 4 日发布，新增 NIP-01 事件 id 验证：客户端会重新计算传入事件的 id，并在使用前拒绝不匹配的事件。该版本还会识别从 ZapStore 之外安装的软件包。在服务器端，[证书哈希保留](https://github.com/zapstore/relay/pull/8)机制会保留重复的 `apk_certificate_hash` 标签，使 Android 签名密钥轮换能够延续已获批准的密钥谱系。

这项[事件 id 检查](https://github.com/zapstore/zapstore/releases/tag/1.1.2)可防止中继或缓存修改标签或内容后仍沿用旧 id。当具有相同应用 id 的 Android 软件包来自其他渠道时，安装来源指示器会提供独立的来源信息。

### Amber 6.6.1 保持签名器响应的可归属性

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) 于 9 月 4 日发布。权限解析现已修复，可以容忍缺少可选的 `kind`；被拒绝的签名请求也开始返回其原始请求 id。调用应用可以将拒绝响应与已提交的操作对应起来。该版本还更新了远程签名器默认设置，并新增了一个索引器中继。

这些[修复](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1)共同保持了双向可归属性：缺少可选字段时，权限记录仍然可用；拒绝响应也仍与触发它的请求相关联。中继默认设置的改动会影响发现过程，但不会取代签名器的本地授权决定。

## 开发中

### Zap Cooking 使用中继提示渲染 NIP-27 引用

[9月4日合并的变更](https://github.com/zapcooking/frontend/pull/665)使 [Zap Cooking](https://github.com/zapcooking/frontend) 能够在文章、食谱、编辑器预览和打印视图中渲染 `nostr:npub` 与 `nostr:nprofile` 引用。无效标识符会保留为文本，解析过程不会阻塞，编辑器还会预览即将签名的 Markdown。当存在中继信息时，单独的 `npub` 会转换为包含发件箱中继的 `nprofile`，并附带匹配的 `p` 标签。

同一周还修复了[限定作者的 kind `30023` 读取](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7)，加入了带有去重和过期查询防护的[已验证 NIP-50 搜索中继](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea)，并在依赖项变更导致余额和历史记录功能失效后修复了 [NIP-47 钱包调用](https://github.com/zapcooking/frontend/pull/705)。

### Conduit 协调已签名的中继与 Blossom 偏好设置

[Conduit](https://github.com/Conduit-BTC/conduit-mono) 于9月2日合并了 [Blossom 偏好设置编辑功能](https://github.com/Conduit-BTC/conduit-mono/pull/374)，并于9月7日合并了[已签名偏好设置协调功能](https://github.com/Conduit-BTC/conduit-mono/pull/397)。Market 和 Merchant 会保留最新的有效 kind `10002` 中继列表及 kind `10050` 收件箱声明；当较新的事件格式错误时，它们会保留仍然可用的已签名列表；它们能够区分明确的空列表与无法获取的查询结果；对于失效的已声明中继，也不会用代码中的默认值替代。

[kind `10063` 编辑器](https://github.com/Conduit-BTC/conduit-mono/pull/374)允许用户加载、重新排序、检查、外部签名、发布并回读一个有序的 HTTPS 媒体服务器列表，同时不会联系这些服务器，也不会插入未声明的默认服务器。

### NIP-A3 支付目标进入三个客户端

9月1日至3日，[Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041)、[Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) 和 [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) 实现了 NIP-A3 kind `10133` 支付目标。Amethyst 仅在存在兼容目标时提供由用户主动选择的转交操作，并且不会将其变成 zap；Grimoire 在构建钱包 URI 之前使用固定注册表；Pollerama 会验证 Monero 地址，并在查询目标之前获取作者的中继列表。每个客户端仍然需要一种获准使用的支付方式、一条中继路由以及准确的展示信息。

### Ditto 扩展 Blossom 回退机制与直播嵌入

[Ditto](https://github.com/soapbox-pub/ditto) 于9月6日合并了[范围更广的 Blossom 回退与镜像功能](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07)。头像、徽章、横幅、社区图片、自定义表情符号和应用图标现在会尝试从已声明的服务器获取具有相同 blob 哈希的文件；镜像上传使用标准 BUD-11 授权令牌。[9月4日的一项变更](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa)加入了紧凑的 `kind:30311` 直播嵌入。

## 协议与规范工作

### Nostr 实现可能性

[NIP-01](/zh/topics/nip-01/) 现在明确说明了 [`limit: 0` 过滤器](https://github.com/nostr-protocol/nips/pull/2460)的行为，该变更于9月4日合并。中继必须不返回任何已存储事件，必须在初始查询完成时发送 `EOSE`，并且必须让订阅保持活动状态，以接收新的匹配事件。客户端可以使用只含一个字段的过滤器开启仅实时订阅，同时保留本地历史记录。这项澄清记录了多个中继实现和公共中继之间相互兼容的行为。

[NIP-78](/zh/topics/nip-78/) 增加了一项[经过身份验证的应用数据要求](https://github.com/nostr-protocol/nips/pull/2458)，该变更于9月3日合并。对于 kind `78` 和 `30078`，中继应当要求进行 [NIP-42](/zh/topics/nip-42/) 身份验证，并且应当只向已通过身份验证的事件作者提供这些事件。这只是“应当”级要求，并非保密保证，客户端不能将任意中继视为私有存储。此次合并还不鼓励把自定义应用数据 kind 用作通用公共交换格式。

[NIP-AC](/zh/topics/nip-ac/) 于9月4日作为一项明确保持开放状态的 [WebRTC 信令提案](https://github.com/nostr-protocol/nips/pull/2461)提出。它使用临时分配的易失性 kind 来处理 ping、连接请求、offer、answer 和 ICE candidate，以 `p` 标签指定接收方，并通过会话 `e` 标签分组；kind `30600` 用于发现。在对等方建立直接连接期间，中继应当广播这些信令事件，并且不得存储它们。这些编号仍为临时编号，客户端应当使用 [NIP-65 中继列表](/zh/topics/nip-65/)，需要保密性的应用应当通过 [NIP-44](/zh/topics/nip-44/) 加密 offer、answer 和 candidate 内容。

## NIP 深入解析：事件文本中的 URI 链接与引用

Nostr 标识符需要具备可传输的含义，其他应用才能打开它。[NIP-21](/zh/topics/nip-21/) 将 [NIP-19](/zh/topics/nip-19/) 标识符置于 `nostr:` URI 方案之后，为浏览器、操作系统和应用提供一种可统一分派的形式。[NIP-27](/zh/topics/nip-27/) 定义了同一个 URI 在可读事件 `content` 中的含义。NIP-21 用于跨越应用边界，NIP-27 则用于在已签名文本中保留对个人资料或事件的引用。两者都不会创建事件 kind，也不会更改中继消息；这[两项规范](https://github.com/nostr-protocol/nips/tree/master)仅定义链接和渲染行为。

### URI 分派与 NIP-19 语义

[NIP-21 的语法](https://github.com/nostr-protocol/nips/blob/master/21.md)是 `nostr:` 后跟一个 NIP-19 bech32 实体。`nsec` 被排除在外，因为它编码的是私钥。其中没有授权信息、路径或查询组件，因此符合规范的链接是 `nostr:npub1...`，而不是 `nostr://npub1...`。平台或客户端可以注册为处理程序；该规范既不选择已安装的应用程序，也不定义网页回退方式。

前缀会告诉客户端应解码什么内容。`npub` 携带公钥，`note` 携带事件 id。`nprofile` 为个人资料添加可选的中继提示；`nevent` 为事件 id 添加中继、作者和 kind；`naddr` 则携带可寻址事件的作者、kind 和 `d` 标识符，并可选择包含中继。这些形式使用 [NIP-19 类型-长度-值字段](https://github.com/nostr-protocol/nips/blob/master/19.md)。提示可以缩小发现范围，但既不能证明中继拥有该事件，也不能证明作者具有控制权。每个获取到的事件仍需重新计算 id 并检查签名。

[NIP-21 规范](https://github.com/nostr-protocol/nips/blob/master/21.md)中的个人资料形式如下：

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) 还定义了 HTML 桥接方式：提供 Nostr 事件的页面可以将其 `naddr` 放入 `<link rel="alternate">`，个人资料则可以将 `nprofile` 放入 `<link rel="me">` 或 `<link rel="author">`。

### NIP-27 渲染与可选标签

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) 适用于可读的事件内容，例如 kind `1` 短帖和 kind `30023` 文章。编辑器可以显示 `@name`，但会在签名字符串中发布 `nostr:nprofile1...`。阅读器会扫描该 URI，解码其中的 NIP-19 实体，获取目标，并可以渲染名称、卡片、预览或本地链接。如果解码失败，该 URI 将保留为普通文本。不得重写原始内容，因为修改它会改变 NIP-01 序列化结果、id 和签名。

内容引用与标签的作用相关，但并不相同。[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) 描述了可选的 `p` 和 `e` 标签，以及 [NIP-18](/zh/topics/nip-18/) 的 `q` 标签。客户端可以显示引用，而不创建通知或帖子串关系；为了便于发现引用，应同时写入 URI 和 `q` 标签。[Zap Cooking 在 9 月 4 日的实现](https://github.com/zapcooking/frontend/pull/665)遵循了这种区分，在保留 URI 的同时添加中继提示和对应的 `p` 标签。添加 `p` 或 `q` 不会使 URI 变为私密内容，并且 NIP-27 没有隐藏提及模式。

以下 [kind `1` 事件](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a)是从 `wss://nos.lol` 恢复的，并在作为具体的 NIP-27 引用收入本文前经过了验证。其 `content` 包含一个指向与版本无关的可寻址事件的 `naddr`。解码后可得到 kind `30402`、作者 `91036d...310a`、该工作簿的 `d` 标识符，以及一个 `wss://nos.lol/` 提示。`q`、`p`、`t`、`zap` 和 `client` 标签是应用程序的选择，并非 NIP-27 的要求。

```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### 信任、失败行为与客户端实现

安全的读取器会识别完整的 `nostr:` 字符串，验证 bech32，解码 NIP-19，拒绝 `nsec`，忽略未知的 TLV 类型，并保持格式错误或过长的文本不变。`npub` 和 `nprofile` 用于查询个人资料；`note` 和 `nevent` 标识不可变事件；`naddr` 根据事件类型、作者和 `d` 标签选择最新的有效可寻址事件。中继提示可以缩小搜索范围，但不会扩展信任范围。根据 [NIP-01 事件规则](https://github.com/nostr-protocol/nips/blob/master/01.md)，客户端会验证所获取 `nevent` 的 id，并在应用可寻址事件替换规则前检查每个 `naddr` 候选事件的签名。

是否显示内联预览由客户端决定，同时需要考虑隐私和资源成本。获取每个引用会暴露读者的兴趣，并可能造成大量查询，因此客户端可以使用缓存、推迟到引用可见时再获取、限制并发量，并要求用户点击后才加载不熟悉的媒体。根据 [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)，预览必须与当前作者签名的文本明确区分。解析失败时，应将引用显示为未解析文本或不可用卡片，而不能静默地将其视为已验证内容。

信任方式也会因标识符类型而异。`nevent` 指向不可变的字节，因此，如果所获取事件的序列化 id 与请求的 id 不同，客户端可以拒绝该事件。`naddr` 指向一个可替换坐标，因此客户端必须验证每个候选事件，并在决定显示哪个版本之前应用可寻址事件规则。无论是哪种情况，中继提示都有助于首次查询，但它并不代表对该中继或其返回内容的认可。[NIP-19 的 TLV 定义](https://github.com/nostr-protocol/nips/blob/master/19.md)提供了明确执行这些检查所需的数据。

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)定义了一种可从 Nostr 外部打开的便携式链接，而 NIP-27 则让同一链接能够持久存在于签名文本中。仅实现 NIP-21 的客户端可以打开粘贴的 URI，但无法渲染嵌入式引用。完整支持 NIP-27 还需要扫描、安全解码、获取策略、本地渲染，以及明确决定如何处理通知标签和引用标签。共享 URI 使这些层能够互操作，而不强制客户端以相同方式呈现它们。[Damus](https://github.com/damus-io/damus)将内联引用建模为带类型的提及。其[提及代码](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift)将 `npub` 和 `nprofile` 映射为个人资料引用，将 `note` 和 `nevent` 映射为事件引用，并将 `naddr` 映射为地址引用；[NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift)会将它们路由到相应的目标。[Primal Android](https://github.com/PrimalHQ/primal-android-app)会[解析协议方案和粘贴形式](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt)，验证 bech32 并提取中继提示，然后[将引用映射到笔记内容模型](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt)。[Zap Cooking](https://github.com/zapcooking/frontend/pull/665)会在文章、食谱、编辑器预览和打印视图中渲染相同的引用。

---

通过 [Nostr Compass 项目](https://github.com/andotherstuff/nostr-compass)发送 NIP-17 私信，分享项目或新闻。
