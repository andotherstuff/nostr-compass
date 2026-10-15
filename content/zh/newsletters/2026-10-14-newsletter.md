---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "桌面版 Amethyst、Amber 安全修复、私密附件、经身份验证的软件安装，以及内容警告与状态。"
translationOf: /en/newsletters/2026-10-14-newsletter.md
translationDate: 2026-10-15
---

**[Amethyst](#amethyst)** 将其 Android 界面带到桌面端，并新增原生 Wayland 支持。**[Amber](#amber)** 修复了权限撤销、复制的秘密信息清除，以及一项可能导致密钥丢失的设置变更。**[Keep](#keep-android)** 收紧了自动签名权限，而 **[MDK](#mdk)** 则推出流式私密附件和按从旧到新顺序补齐消息的功能。**[Zap Cooking](#zap-cooking)** 合并了关注列表编辑保护措施和经身份验证的会员资格机制。下文介绍[发布详情](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0)，以及协议变更和公开状态机制。

## 头条动态

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) 将这款 Android 社交客户端的共享界面带到桌面端，提供自定义信息流、宽窗口多列视图、可选启用的锁定功能、加密媒体和 [Blossom 上传](/zh/topics/blossom/)。来自 [NIP-85 可信断言](/zh/topics/nip-85/)的提供方评分会在本地建立索引，用于请求、通知和徽章，提供方和阈值由用户选择。

今天发布的 [v1.19.0 版本](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0)新增原生 Wayland 支持，并通过单独安装的 FFmpeg 和 ffprobe 实现桌面端视频压缩。密钥存储修复解决了钥匙串反复提示和 Linux 密钥环故障的问题。日历集合和 RSVP 现已支持渲染，Android 登录界面则新增了 [NIP-46 远程签名](/zh/topics/nip-46/)。加密信封先并行打开，再串行建立索引，同时修正了 relay 重连和信息流作者 relay 列表的处理方式。[relay 客户端会遵守限速退避要求](https://github.com/vitorpamplona/amethyst/pull/4422)，之后再恢复订阅或发布。

这项[信任提供方 relay 变更](https://github.com/vitorpamplona/amethyst/pull/4437)将用户 kind 10040 列表中的提供方 relay 视为用户自己的可信 relay。这些连接默认采用直连路由；若要使用 Tor，则需要启用可信 relay 设置。主客户端的 [NIP-42 relay 身份验证](/zh/topics/nip-42/)可能会向这些 relay 披露用户的公钥。

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) 修复了这款 Android Nostr 签名器中的三个安全漏洞。[已撤销的权限](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw)不再因缓存竞态而继续生效，明确拒绝的决定也会优先于完全信任状态。[复制的秘密信息](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p)会由系统调度在 60 秒后从剪贴板清除，即使进程被终止也会执行；在此期间，内容仍可被读取，而且之后复制的新文本也可能被清除。更改[“要求设备处于解锁状态”](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5)设置时，会保留旧的封装密钥，直至秘密信息迁移完成，但此前丢失的密钥仍无法恢复。此版本还修复了多请求 nostrconnect 批准，并在 URI 指定的 relay 上回复。使用 6.6.8 及更早版本的用户应当更新。

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0) 是一款 [FROST 门限签名器](/zh/topics/frost/)，新增设备端分布式密钥生成，以及对中断的份额操作进行经身份验证的恢复。它还支持不具备 StrongBox 支持的设备。在门限签名中，参与设备各自持有签名秘密的份额，并协作生成签名；设置和恢复步骤决定哪些设备能够参与。

[1.3.1 版本](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1)防止自动签名覆盖已记住的拒绝决定、询问权限、已过期的批准或权限读取失败的结果。到期后会移除后台批准，但保留拒绝决定。[逐应用策略迁移](https://github.com/privkeyio/keep-android/pull/532)将权限移入由核心组件管理的存储，同时保留更严格的决定。

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) 为其通过 Nostr 协调的交易应用所使用的[原生钱包桥接加入身份验证](https://github.com/jesuspirate/chama/pull/29)，禁用了生产环境中基于 URL 的桥接重定向，并验证付款金额。它还会拒绝清空内容无法读取的钱包。

[6.4.22 版本](https://github.com/jesuspirate/chama/releases/tag/v6.4.22)增强了重放过程对外部 event 的防护，检查后继关系，拒绝空仲裁者池，并根据已签名的 LOCK 时间推导退款时间。其共识变更适用于自 2026 年 11 月 1 日起签名的 CREATE event；客户端保护措施则立即生效。发布说明保留了关于由交易条目选定的联盟及尘额付款的注意事项。后续的[签名器与恢复变更](https://github.com/jesuspirate/chama/releases/tag/v6.4.23)新增了受保护种子读取器，并使延迟锁定可以恢复，而 [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24) 改善了大型交易列表的处理。

### Zap Cooking

食谱与社交客户端 [Zap Cooking 合并了关注列表编辑保护措施](https://github.com/zapcooking/frontend/pull/795)，以应对读取结果不完整、过时或意外缩减的情况。关注操作共用一条带有防护的更新路径，保留现有 tag 和内容。发布前会检查签名器身份。其[会员授权修复](https://github.com/zapcooking/frontend/pull/802)使用签署经身份验证请求的公钥。一条[暴露管理秘密信息的路由已被移除](https://github.com/zapcooking/frontend/pull/801)；部署时仍需轮换秘密信息，仅合并变更并不能证明轮换已经完成。之后的[讨论串与书签修复](https://github.com/zapcooking/frontend/pull/833)保留了真实的回复根节点，并恢复失败的书签写入。[食谱 tag 字段](https://github.com/zapcooking/frontend/pull/836)不再将按键输入发送到个人资料或 NIP-50 搜索服务，也不会在存在未保存更改时离开编辑器。

## 带版本 tag 的发布

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0) 是 [Marmot 加密群组](/zh/topics/marmot/)的运行时，新增支持流式传输和断点续传的私密附件，并提供进度显示和取消功能。它还向部署运营方发送私密的 [NIP-56 举报](/zh/topics/nip-56/)，使用 [NIP-59 礼物封装](/zh/topics/nip-59/)，其中不包含消息、群组和 relay 标识符。消息补齐按从旧到新的顺序处理每批最多 256 个 event，并保留 relay 的 CLOSED 拒绝响应。SOCKS5 路由覆盖 relay、媒体和发现服务，且不会回退到直连。

[发布指南](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md)要求绑定、头文件和原生构建产物同步更新。数据库模式从 101 升至 107，且不提供降级路径。宿主端秘密信息存储需要迁移。MarmotKit 和 C 构建产物已稳定；WN Agent 仍处于预发布阶段，工作区 crate 尚未在 crates.io 上发布。迟到超过五个 [MLS epoch](/zh/topics/mls/) 的历史记录仍可能无法解密，且不会出现历史记录不完整的提示；经身份验证的代理客户端仍可访问整个 API。

此版本还会[重试在首次确认后仍处于待处理状态的个人资料、关注列表和 relay 列表保存操作](https://github.com/marmot-protocol/mdk/pull/2228)；这些后台重试不会在重启后保留。[邀请查询会在发现 relay 上检查 KeyPackage 是否已删除或过期](https://github.com/marmot-protocol/mdk/pull/2211)，但这些 relay 的答复无法证明接收方仍持有其私有 KeyPackage 材料。[活动反应的目标](https://github.com/marmot-protocol/mdk/pull/2187)现在会一致地根据经身份验证的行为主体和各次群组提交推导；较早的、缺少行为主体的历史记录仍不完整。

后续 master 分支的工作[关闭了泄漏的 relay 订阅，并对激活重放进行分页，每页上限为 500 个 event](https://github.com/marmot-protocol/mdk/pull/2274)。[Epoch 间隙恢复](https://github.com/marmot-protocol/mdk/pull/2298)会从比较失败的 relay 获取最新的 256 个 event，但并不保证历史记录完整。[自更新提交会重试所有先前未送达的群组 relay](https://github.com/marmot-protocol/mdk/pull/2275)。新增的提示性检查涵盖[已知的过期 epoch](https://github.com/marmot-protocol/mdk/pull/2273)和[仍欠 relay 的提交](https://github.com/marmot-protocol/mdk/pull/2288)；用户可以确认接受风险，因此这些检查并不保证群组不会分叉。

[因存储空间不足而受阻的附件下载](https://github.com/marmot-protocol/mdk/pull/2249)会保留可续传的进度。显式发起的大型下载使用文件写入目标，暂存和检查点所需的可用空间约为正文大小的五到六倍。[已验证的公开 event 预览](https://github.com/marmot-protocol/mdk/pull/2304)新增了有容量限制的加密账户缓存，而[仅包含过时 KeyPackage 的结果](https://github.com/marmot-protocol/mdk/pull/2305)现在可以与不完整的 relay 查询结果区分开来。这些都是后续源代码变更，需要宿主端配套采用；通过已完成的获取生成的 event-ID 预览不会重新检查后续的删除。

代理桥接还会[限制后端输出](https://github.com/marmot-protocol/mdk/pull/2103)，以防过大的回复耗尽内存，并[接受连接器实际返回的删除响应](https://github.com/marmot-protocol/mdk/pull/2301)。当输出限制终止一个轮次时，先前已交付的文本仍然算作已交付。

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0) 新增了手机或 fips 桌面端之间的 USB 连接，并采用[目前提议的 NIP-5D 清单格式](https://github.com/Origami74/myco/pull/135)，包含经过签名的制品和图标哈希。旧版手机仍可配对，但需要更新后才能打开这些 napplet。其[下载策略变更](https://github.com/Origami74/myco/pull/133)区分了互联网、mesh 和用户配置的 HTTP 目标。在互联网策略下，作者提供的提示和重定向无法探测本地网络，而用户配置的目标仍不受限制。软件客户端还会[在作者的 BUD-03 Blossom 服务器上发现 blob](https://github.com/Origami74/myco/pull/134)。这改善了制品发现，但也会将安装流量暴露给这些服务器。这些 HTTP 变更并未为 WebSocket 连接建立同等保护。[附近 mesh 可用性检查](https://github.com/Origami74/myco/pull/132)会探测对等节点上是否有 blob，而不下载它们，也不联系公共 Blossom 服务器。这些有界限的 HEAD 请求需要 mesh 权限；持有者数量并不能证明整个制品仍然可用。

该版本还会[并行竞速查询上游 DNS 服务器](https://github.com/Origami74/myco/pull/137)，避免漫游运营商的超时阻塞 relay 和制品查询。Outbox 发布会面向列表中的每个写入 relay，较慢的目标则在后台投递。互联网 mesh 仍默认关闭，网页图片也不会在重启后保留。

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13) 为其 Android 照片客户端新增了读写 relay 列表和 outbox 路由。其[发行说明](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2)介绍了 relay 的角色，没有列表的账户会从三个默认公共 relay 开始。“附近”功能使用粗粒度 geohash 和相邻网格；为帖子添加位置需要主动选择，且默认关闭。这些 tag 仍会公开暴露一个区域。经检查，发布结果表示已排入套接字发送队列，尚未确认 relay 是否接受。

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0) 允许用户通过个人监视服务接收 Monero 打赏，而 [0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0) 默认隐藏新配置的打赏金额和通知中的发送者姓名。图片默认点击后加载，可选的 Primal 计数和客户端 tag 均处于禁用状态。托管的监视服务仍会通过已注册钱包的私有查看密钥，获知该钱包的每笔入账。即使隐藏了金额，公开收据仍会保留收款人、时间和所引用的帖子。

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2) 将共享加密购物清单、由通行密钥支持的 Nostr 身份，以及每份清单各自的 Marmot 聊天结合起来。粘贴持有者密钥即可加入清单，并获得读取和编辑权限。通行密钥登录依赖浏览器和提供方对 WebAuthn 伪随机函数扩展的支持；成员 tag 对 relay 仍然可见。[版本 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3) 通过在本地缓存解密后的内容，让清单在重新打开后仍然保留，修复了此前只有密钥留存、必须等 relay 再次投递清单的情况。

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0) 会按照预期的有效期和确认规则，读取另一个 Roadstr 客户端的 kind 1315/1316。一种紧凑的编解码格式为实验性的 MeshCore 无线电与 relay 桥接保留了可重建的已签名报告。兼容发布和无线电传输默认关闭，共享前会征得同意。无线电报告会向覆盖范围内的任何人暴露位置、时间和签名公钥。测试使用了模拟无线电；真实硬件、Android BLE 和向公共 relay 发布仍未经验证。

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3) 改进了其 Android 客户端中的文章评论和引用帖子处理。文章评论使用 kind 1111，以文章为根、评论为父级，而普通短帖回复仍使用 kind 1。引用发现同时接受 q tag 和旧式携带链接的 e 提及；新发布的引用会添加 q tag。发布失败时会回滚乐观更新的回应。

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28) 介绍了如何[读取嵌套的出版物索引](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0)：这些 kind-30040 索引按出版者设定的顺序，同时包含章节和子索引。离线副本会保留这一层级结构，以及与各次出现位置绑定的书签。刷新会按坐标获取当前修订版，但当结果不完整、较旧或获取失败时，会保留之前的下载内容。重新广播会保留原始签名的后代节点。有界限的展开和可读的部分分支，可避免将结构缺失的内容呈现为一本完整的书。

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0) 将各内容信息流中的“全局”替换为“发现”。“发现”从用户所关注的人关注的账户中选取内容，并按共同连接关系对帖子排序，排除用户本人及已关注的账户。未登录用户和没有关注任何人的账户则会看到一个精选的起始网络。这将默认发现的范围改为社交邻域；抗垃圾信息能力和这些账户的可信度仍是另外的问题。

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x) 会在保存草稿和发布的过程中，始终将选定的个人资料身份与提及绑定。编辑器在签名和发送期间会冻结账户、文本、提及和附件，并将收到的分享保留到该操作完成后再处理。重试会保留原始签名的 event，包括较早的待发送帖子。仅在 @ 后输入姓名还不够：用户必须选择一个个人资料，而旧草稿中已经丢失的身份需要重新选择。

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0) 将社区与其聚会关联起来。关联活动的审批也可以同时授予社区成员资格，无需再次审批；加入表单会说明这一点，并允许申请人选择不加入社区。现有参与者会收到一键邀请。活动保留各自的参与者、匹配和聊天功能，而社区则列出其活动。发行说明介绍了对活动与社区由不同协调者管理的支持，但并未提供独立的互操作性或加密测试验证。

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1) 修复了 Android 上的 [Nostr Wallet Connect](/zh/topics/nip-47/) 支付处理问题：钱包处于后台时，支付处理可能停止，问题积累后可能导致应用无响应。此次原生版本打包了此前五个月通过空中更新交付的改动。[0.4.5 beta 1 版本](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1) 修复了 Android 到 iOS 的 NFC 传输；今后的空中更新需要此版本。这些修复均为发行说明所报告，后台处理仍受手机的生命周期限制。

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0) 允许用户从文章编辑器发布食谱、打开分享的食谱包，以及浏览所关注作者的食谱。上周介绍的网站卡片和个人资料网格现已随此版本发布，同时加入的还有 relay 速率限制处理和 Android `nostr:` 直达链接。网站链接不等于对网站内容的验证；通过网关访问时，网关能够看到点击所发起的请求。

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2) 将其 Nostr Git 托管平台打包为 Android 应用，通过 [NIP-46 远程签名](/zh/topics/nip-46/) 使用 Amber。该 APK 打开的是现有的托管应用 `gittr.space`，因此用户仍然依赖其提供的浏览器代码及其可用性。在这个封装应用内无法使用浏览器扩展签名；自行托管仍需单独部署 Git。

### Dart NDK

[Dart NDK 0.11.0 开发版零](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0) 将这一 Dart 和 Flutter 工具包的[身份验证同意处理器](https://github.com/relaystr/ndk/pull/862)和 NIP-46 签名器 relay 切换功能纳入预发布版本。这些改动上周作为已合并的工作进行了介绍，如今已正式发布。签名器可以跟随替换后的 relay 列表，应用必须持久化保存该列表。[开发版一](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1) 增加了对 relay 信息中字母形式 NIP 标识符的支持。这两个版本都包含不兼容的集成变更。

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0) 为原生 Android 应用提供[四种授权选项](https://github.com/forgesworn/cambium/pull/32)：一次、一小时、一天或无限期。授权范围按操作和 event kind 划分。Cambium 通过远程签名将请求转发给 Heartwood 硬件签名器；哪些请求获得签名，仍由 Heartwood 决定。网站授权仍为单次有效。已配对的签名器新增了测试和重新连接控件、受支持的传输 relay 更新，以及经过敏感信息遮蔽的诊断信息。[NIP-55 Android 签名](/zh/topics/nip-55/)批处理会保留请求顺序和单项拒绝结果，并对有歧义的复用 intent 提供明确可见的单次同意提示。

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1) 修复了其 Go 客户端库中面向多用户应用的 [NIP-42 relay 身份验证](/zh/topics/nip-42/)。每个 `UserContext` 都拥有私有的已验证连接、relay 偏好设置和连接保留状态；共享连接池从不进行身份验证。该库会验证传入的 ID 和签名、检查订阅匹配，并正确序列化 tag 和时间过滤器。需要身份验证的调用方必须迁移至 `UserContext`。relay 的存储和服务功能保持不变，身份验证仍要求在连接打开时收到质询。

### Nmail

加密邮件客户端 [Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0) 将陌生发件人归入“请求”，将已屏蔽的发件人归入“垃圾邮件”。接受和屏蔽操作会跨设备同步。现有收件箱中的发件人也需要接受，并提供“全部接受”选项；垃圾邮件保持静默，待处理请求不会针对同一发件人反复提醒。回复使用接收邮件的身份。此版本还提供了私有 relay 管理、复制同步码前的设备锁检查、共享主题、更完整的联系人信息保留和 Windows 安装程序，并修复了重置或登录后恢复邮箱的问题。

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0) 为其通过 Nostr 同步的任务管理器带来了加密评论和未读标记。评论使用可寻址的 kind 35002 event，并采用 [NIP-44 加密](/zh/topics/nip-44/)，将其与任务的关联保存在密文中。该版本[修复了离线发送](https://github.com/higedamc/meiso/pull/212)、重新连接后的补同步、使用已保存 relay 启动以及空列表传播的问题。它还防止了部分同步导致任务被删除。未读和补同步功能并不为已关闭的应用提供通知服务。

### Haps

实验性软件安装器 [Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13) 默认要求用户的[信任网络](/zh/topics/web-of-trust/)对要安装的确切版本进行审计。审计可以比较固定版本的源码与重新构建的产物，并可保持私密或公开发布。[0.1.14 版本](https://github.com/mmalmi/haps/releases/tag/v0.1.14) 在用户仅凭名称安装时要求确认发布者；自动化操作则必须指定发布者。审计提供证据，但原生程序和构建配方仍会在没有沙箱的情况下执行。审计要求可以针对单次操作跳过；签名、完整性和发布者确认检查仍然保留。

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0) 为其浏览器扩展社交客户端增加了[直播发现与播放](https://github.com/dmnyc/sidecar/pull/479)功能，并提供带签名的聊天、回应和 zap。已保存的直播书签支持加密的账户备份与恢复，私密的通知静音设置让用户能够控制提醒。搜索新增了关注和静音控件；同时还改进了自动锁定和钱包历史记录刷新。

### Ants

搜索界面 [Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0) 无需登录，即可将[结构化搜索路由](https://github.com/dergigi/ants/pull/316)至作者公布的写入 relay 和被提及用户的读取 relay，使用 [NIP-65 relay 列表](/zh/topics/nip-65/)。发现过程会限制所查询的身份和 relay 数量，并在取消或超时时停止。缺少列表时仍保留后备路由。文本查询仍使用经过验证的 [NIP-50 搜索 relay](/zh/topics/nip-50/)。

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0) 是面向拟议的 [NIP-5D 应用](/zh/topics/nip-5d/)的 napplet 发布器和播放器，新增了键盘绑定，以及通过 Git 托管服务 GRASP 提交无需 fork 的提案，并在重试时检查确切修订版本。其 [v0.26.0 版本](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0) 会在主要发布完成后，将带签名的发布版本分发至经过验证的发件箱 relay；删除操作会跟踪曾尝试发送的目标，但无法召回未知副本。[0.26.1 版本](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1) 将读取、播放和审阅的容量上限提高至 100 MiB，同时对新构建和发布保留 25 MiB 的限制。后续加入的[直接展示元数据](https://github.com/zeSchlausKwab/napplet-soy/pull/14)将作者封面和片段直接放在带签名的清单上，停用了配套 event。已冻结的旧任务仍受支持；这一带版本的 Soy 扩展需要兼容的读取器，且不属于固定版本的 NIP-5D 规范。

### nostream

relay 服务器 [nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0) 新增了用于 [NIP-66 relay 监控](/zh/topics/nip-66/)的探测功能，可测量 WebSocket 读写往返时间、检测可选身份验证并发现镜像目标。当观测到的行为与 [NIP-11 relay 信息](/zh/topics/nip-11/)不一致时，它会发出警告。受速率限制的 OK 响应可以包含一个可选的第五元素，用于指定以毫秒计的退避时间。[版本 3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0) 在 IP 消息限制导致 `REQ` 或 `COUNT` 被拒绝时，为 [CLOSED 响应](https://github.com/cameri/nostream/pull/821)添加了第四个元素，用于指定以毫秒计的退避时间。该版本交付了 [PostgreSQL negentropy 对账核心](https://github.com/cameri/nostream/pull/809)和有序 event 清单；[NIP-77](/zh/topics/nip-77/) relay 线路消息和能力通告仍是独立的待办工作。

### Bark

[Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15) 为远程签名审批提供了键盘操作、明确的 event 和身份审查，以及[一分钟、五分钟或十分钟的决策时限](https://github.com/forgesworn/bark/pull/52)。后台强制执行机制会拒绝已过期的决定和排队请求；决定发送失败时，弹窗会保持打开，以便重试。[版本 1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17) 在签名器握手完成后即可提供 [NIP-07 浏览器签名](/zh/topics/nip-07/)，同时继续进行可选诊断。它还会在更新后恢复现有标签页上的桥接。

### Mostro

[Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3) 会响应经过身份验证的用户自身信誉查询请求，即使用户没有尚未结束的订单。这个点对点交易平台会将回复私下发送给发起请求的交易密钥，而一条[已合并的 CLI 命令](https://github.com/MostroP2P/mostro-cli/pull/203)提供了该查询功能。信誉导入仍处于预览阶段，导入功能尚未实现；运营者应保持其禁用状态。[后续合并的工作](https://github.com/MostroP2P/mostro/pull/1057)会公布 Lightning 托管守护者安全余量，并拒绝不安全的配置；其最低 18 个区块的要求以 LND 默认的持有到期设置为前提。

### Elisym

[Elisym 的 commerce 0.11.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0) 支持从商家收入中扣除费用，通过已签名的店铺资料 tag 声明支持分账付款，并在需要收取费用时拒绝不兼容的店铺。[已合并的管理端工作](https://github.com/elisymlabs/elisym/pull/170)从 Nostr relay 读取订单和商品列表。它会要求提供店铺的私钥，因此需要信任所提供的浏览器代码和扩展；本地管理端仍然可用。托管部署和主网费用启用情况仍未经验证。[Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0) 升级了其账本，但不支持降级。

### Routstrd

[Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16) 可防止超时的 [Nostr Wallet Connect](/zh/topics/nip-47/) 充值立即生成另一张可支付发票。它会[检查现有的 mint 操作](https://github.com/Routstr/routstrd/pull/144)，直到付款成功或失败；若无法获取状态，充值会继续暂停。该推理网关根据 Nostr 评价标签启用提供商，其中实验性标签需要明确选择启用。[版本 0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17) 包含了配套 SDK。未结算操作防护仍保存在内存中，因此重启守护进程会丢失这层保护。

### Buzz

[Buzz 桌面版 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28) 允许经过身份验证的工作人员在不切换连接的情况下，[浏览和管理 relay 上的每个社区](https://github.com/block/buzz/pull/8027)。管理操作会保留审查时所选的社区、relay 和签名器；禁用身份验证后，控制台仍可用于读取。另外，[已合并的 relay 工作](https://github.com/block/buzz/pull/8197)会在查询和实时分发中，隐藏针对私密作者记录且带有正确 tag 的删除 event。这项服务器端修复需要部署，且不涵盖此前已泄露的副本和历史上未加 tag 的删除记录。

### Earthly

[Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21) 允许用户[在网站上嵌入公开的 Nostr 地图数据集](https://github.com/zeSchlausKwab/earthly/pull/35)，并提供预览以及外观和初始相机位置的控制选项。其 Maps MCP 集成可通过聊天创建并发布地图，随后生成分享链接或嵌入内容。该集成仍是个人使用的已连接插件试点。嵌入功能支持最多包含 300 个要素且大小不超过 48 KiB 的内联数据集；不支持私密、未发布和以 blob 为存储后端的数据集。

### Milk Market

[Milk Market 移动版 v0.3.0](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0) 为其卖家应用带来了完整的店面设计编辑器，具有与网页编辑器相同的区块和字段。单个商品页面的设计可以覆盖主题和区块选择，包括元数据和社交分享图片。该版本新增了检查机制，以保持移动端和网页端配置一致。[版本 0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1) 修正了移动端预览卡片的对比度；发布页面附有 Android 下载文件，iOS 版本则通过 TestFlight 提供。

### Zeus

[Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3) 包含上周报道的 [LDK 路由费用修复](https://github.com/ZeusLN/zeus/pull/4353)，该修复现已随版本发布。其基于 LDK 的 Nostr Wallet Connect 服务可以在响应和支出记录中包含所报告的路由费用。预算检查仍在结算前针对发票金额进行，取整后的费用在结算后扣除，另设 1,000 聪的路由费用上限。该版本还更新了内嵌的 LND，并包含 rust-lightning 安全修复；实际 NWC 设备验证仍未经确认。之后[已合并的 Zaplocker 移除工作](https://github.com/ZeusLN/zeus/pull/4933)将停用其 Nostr 证明和赎回流程。若升级时仍有付款由该服务器持有，赎回功能将被移除；付款方必须等待持有发票到期并退款。这项停用不属于 v13.2.3；其推行取决于禁用服务器并向现有用户发出警告。

## 开发中

### nosvelte

[nosvelte 的 event 验证器修复](https://github.com/akiomik/nosvelte/pull/162)会在验证签名之前，检查 event 所提供的 ID 是否与其字段的规范哈希一致。这个 Svelte 库的默认验证器此前会接受签名正确但 ID 被替换的字段，导致内容能够占用另一个 event 的身份，并干扰替换处理。已合并的更改适用于使用默认验证器的第一版请求和发送路径；它并不证明旧版导出或自定义验证器符合 [NIP-01 的 event 格式](/zh/topics/nip-01/)。随后的一项[请求过滤器修复](https://github.com/akiomik/nosvelte/pull/171)会在匹配前检查并复制 relay event 字段。格式错误的数据不再能够终止默认提供方的订阅，也不会导致其下一个有效 event 被丢弃。调用方提供的引擎客户端可能仍保留早先的依赖项匹配行为。

### nostter

nostter [将外部提供的 relay 提示限制为安全的 WebSocket URL](https://github.com/SnowCait/nostter/pull/2684)，拒绝本地主机名和非全局 IP 地址。账户选定的本地 relay 和远程签名器 URL 仍沿用现有路径；DNS 重绑定不在此项检查范围内。该网页客户端还会仅在读者按下“显示”后，[读取实验性的分离式内容警告载荷](https://github.com/SnowCait/nostter/pull/2680)，并检查所引用的 event ID、作者是否一致，以及 `k` tag 是否与原始 event kind 匹配。回应和回复均以原始 event 为目标。这些已合并的更改不会改变其当前的 [NIP-36](/zh/topics/nip-36/) 发布格式。

### Coracle

[Coracle 的列表编辑器](https://github.com/coracle-social/coracle/pull/679)通过等待异步解码完成后再渲染表单，恢复了编辑和删除功能。此前，编辑操作会丢失列表字段，而且保存和删除操作都不会发布 event。

### Routstr Core

[Routstr Core 当前版本 0.5.0 的源码](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0)[不再将自动生成的 Nostr 私钥写入日志](https://github.com/Routstr/routstr-core/pull/812)，并[保留首次启动时的公开身份](https://github.com/Routstr/routstr-core/pull/818)。[提供商公告](https://github.com/Routstr/routstr-core/pull/823)排除了 localhost，以及以 IP 字面量表示的私有或链路本地 HTTP 地址；此项检查不会解析主机名。当前 tag 包含其所记录的 10 月 7 日发布日期之后合并的工作，因此历史二进制文件和部署情况仍未经核实。此前暴露的日志仍需由运营者审查。

### Alby Hub

[Alby Hub 的发票授权变更](https://github.com/getAlby/hub/pull/2629)将结算和取消操作限制为仅可针对发起请求的应用所创建的发票。这个自托管钱包通过 [NIP-47，Nostr Wallet Connect](/zh/topics/nip-47/) 提供应用连接；某个连接管理自身发票的能力不得赋予其操作其他应用发票的权限。另一项[隔离连接隐私修复](https://github.com/getAlby/hub/pull/2621)从隔离连接的浏览器成功处理流程中移除了主钱包的 Lightning 地址。

### nak

[nak 已合并的 relay 命令](https://github.com/fiatjaf/nak/pull/222)会探测连接、读取和写入耗时以及 relay 信息，然后输出未签名的 kind 30166 发现 event。将这些结果通过管道传给 `nak event` 即可完成签名和发布，从而使用同一个终端工具实现定时 [NIP-66 relay 监控](/zh/topics/nip-66/)。实际观察到的身份验证或限制响应优先于 relay 对外声明的信息。写入探测使用由一次性密钥签名的临时 event；kind 10166 监控器公告仍是单独的操作。

### Kehto

[Kehto 的清单验证](https://github.com/kehto/web/pull/277)会在执行前检查当前的单制品签名清单和制品字节，同时将旧版解析单独处理。napplet shell 还会[验证推荐的处理程序](https://github.com/kehto/web/pull/294)，在其与已保存的选择冲突时询问用户，并在接受调用 URL 后将其消耗掉，以防止重复投递。清单验证检查发布者身份和制品字节；它并不证明应用代码是安全的。[游戏手柄快照](https://github.com/kehto/web/pull/297)现在会随焦点和可见性变化而调整。Paja/playground 框架会在应用代码运行前阻止直接访问原生游戏手柄、HID 和 USB，仅允许通过宿主中介访问。使用方需要相应的宿主包；shell 就绪状态是一项独立能力。随后的一项 [Paja 准入变更](https://github.com/kehto/web/pull/305)会对不可用的实验性必需域发出警告，但仍允许加载；这些域仍不提供任何 API 或授权。

### napplet SDK

[napplet SDK 实现了基于 URI 的调用和保留式投递](https://github.com/napplet/web/pull/228)。[发布元数据在独立 HTML 中仍会保留](https://github.com/napplet/web/pull/226)，而[可选的应用引用](https://github.com/napplet/web/pull/239)可将清单关联到已签名的列表条目和截图，而不改变制品哈希。应用引用格式仍是一项提案。参考 shell 的测试将生产环境中的发现、安装和签名验证留给宿主负责。

### rust-nostr

Rust Nostr 库 [rust-nostr 在保留 relay 终止性错误的同时保留部分下载进度](https://github.com/nostrdevkit/nostr/pull/1483)。失败的 relay 仍保留在失败集合中，因此调用方可以使用已经收到的 event，同时不会丢失同步提前停止的证据。

### Pensieve

[Pensieve 的对账安全修复](https://github.com/andotherstuff/pensieve/pull/92)延续了此前的[缺失 event 排除工作](https://github.com/andotherstuff/pensieve/pull/90)。relay 和归档工具会先按精确 ID 重新请求缺失项，再对失败进行分类，防止因查询结果数量受限而未返回的尾部内容被错误排除。暂停计数按任务分别进行，已归档的 event 则单独处理。已完成的任务仍可保留明确的缺失 event 记录；仅凭完成状态并不能证明归档完整。

[Premium Primal 持续对账](https://github.com/andotherstuff/pensieve/pull/84)已于 10 月 12 日启用。运营者的[部署记录](https://github.com/andotherstuff/pensieve/pull/93)报告称，两个修复后的二进制文件均已部署，并于 10 月 13 日启用了基于失败情况的暂停机制。后续的[排除项沿用机制](https://github.com/andotherstuff/pensieve/pull/95)仅对同一 relay 和重叠时间窗口复用最初经过证实的排除项，不包括链式沿用项和新混入的 ID；其[部署于当天下午记录](https://github.com/andotherstuff/pensieve/pull/97)。[归档预检和缓存停滞修复](https://github.com/andotherstuff/pensieve/pull/98)已于 [10 月 14 日部署](https://github.com/andotherstuff/pensieve/pull/99)。随后的一项[沿用优先级修复](https://github.com/andotherstuff/pensieve/pull/103)已合并，但其来源记录显示尚未部署。

### njump

Nostr 网页查看器 [njump 会在未提供覆盖配置文件时恢复内嵌的 relay 默认设置](https://github.com/fiatjaf/njump/pull/173)。它还会[隔离并发的 Markdown 渲染器](https://github.com/fiatjaf/njump/pull/171)以及[超时期间的响应头](https://github.com/fiatjaf/njump/pull/169)，修复了在渲染被引用的长文 event 或处理并发请求时可能导致进程崩溃的竞态问题。这些服务端变更均已合并；线上部署情况仍未经核实。

### Nostr Components

[Nostr Components 的 zap 签名修复](https://github.com/saiy2k/nostr-components/pull/187)会在所选签名器拒绝签名时停止支付流程。这些可嵌入的社交组件不再在遭到拒绝后改用随机匿名身份。其[收据聚合功能](https://github.com/saiy2k/nostr-components/pull/197)会先验证 [NIP-57 zap 收据](/zh/topics/nip-57/)，再对 relay 副本、发票和请求 ID 去重。

### rx-nostr

响应式客户端库 [rx-nostr 第四版的验证变更](https://github.com/penpenpng/rx-nostr/pull/207)在 JavaScript 和 WebAssembly 中一致地检查规范 event 结构、ID 和签名。空的请求条件列表不会匹配任何内容，并会完成；旧版发送机制在没有目标地址时会报告失败。发布观察者无法改变最终结果，已释放请求的后代请求也无法重新启动。[有限查询分段](https://github.com/penpenpng/rx-nostr/pull/213)允许向后查询在所有提供的分段完成后结束。这些变更已包含在 [4.0.0 beta 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2) 中，该预发布版本包含不兼容的 API 变更。

### eHagaki

社交客户端 [eHagaki 新增了分阶段发件箱投递](https://github.com/Lokuyow/ehagaki/pull/268)，会在签名前固定作者的目标 relay。其敏感帖子流程会先向每个 relay 发送载荷，再发送引用该载荷的结构，并以该 relay 自身的确认为准；如果只有载荷发送成功，则保留编辑器内容。[完整的帖子历史扫描](https://github.com/Lokuyow/ehagaki/pull/312)会逐步保存经过验证的结果。即使扫描显示为已完成，存在歧义的范围仍保持未确认状态，并提供说明性信息控件。[Citrine 本地 relay 支持](https://github.com/Lokuyow/ehagaki/pull/315)会保留经过验证的浏览范围，并在外部发布成功后原样归档已签名的 event。本地确认不会将失败的外部发送变为成功，这项功能也没有增加离线发布队列。[已上传媒体管理](https://github.com/Lokuyow/ehagaki/pull/321)可列出和删除已上传到受支持的 NIP-96 和 Blossom 服务器上的图片与视频。随后的一项[数据库迁移](https://github.com/Lokuyow/ehagaki/pull/325)会重置缓存的显示数据和帖子历史，同时保留草稿和删除请求。它还会阻止较早排队的同步结果在清空后重新填入历史记录。

### Formstr

[Formstr 的提交结果修复](https://github.com/formstr-hq/nostr-forms/pull/508)会在没有任何 relay 接受表单响应时拒绝该响应。这款 Nostr 表单应用会显示各 relay 的处理结果，并在保留已填写答案的同时提供重试选项。Webhook 和确认页面会等待响应被接受，SDK 也加入了相同的检查。relay 确认仍不等于保证长期存储，但完全发布失败不再产生成功提示。

### Auditable Voting

[Auditable Voting 新增可选的私有工作节点选票批处理功能](https://github.com/tidley/auditable-voting/pull/35)。由组织者签名的定义指定工作节点身份、DM relay，以及发布阈值或截止时间。投票者发送 [NIP-17 礼品包装选票](/zh/topics/nip-17/)，并根据该工作节点的身份验证回执；委托必须同时授权排队和发布。发布的选票使用工作节点的身份。工作节点可以读取提交内容，而按截止时间发布的批次可能很小。如果无法解析出有效的私有路径，所检查的客户端会回退到公开提交。这是已合并的开发工作。

### MintRadar

[MintRadar 新增需主动启用的礼品包装提醒](https://github.com/hroomnik007/MintRadar/pull/122)，用于提示 mint 或 melt 操作问题、软件过时，以及不再支持这些操作的情况。其 Cashu mint 目录[将关注列表控件](https://github.com/hroomnik007/MintRadar/pull/123)与这些通知设置关联起来，并在服务器响应后确认设置。原子性占用机制可防止重叠探测发送相同提醒；向 relay 发布失败时会释放占用，以便重试。[NIP-17 私信](/zh/topics/nip-17/)保护通知内容；relay 接受通知并不代表已确认收件人阅读。

### Nostr Docs

[Nostr Docs 的本地 relay 迁移](https://github.com/formstr-hq/nostr-docs/pull/65)将协作式 Markdown 编辑器的读写操作交由 Web Worker 处理，并配备 IndexedDB event 缓存和重试发件箱。文档标题和 tag 在重新加载后仍会保留，连续的元数据编辑会获得递增的时间戳，使同一秒内的两次编辑仍能保持区分。现有的加密密钥存储保持不变。网络池回退方案不具备工作线程发件箱的持久性，而接受排队中的发布请求并不代表 relay 已接受。

### Pakstr

[Pakstr 的原生本地签名器](https://git.nostrdev.com/stuff/pakstr/pulls/105)让其 Android 应用外壳能够在设备上创建 Nostr 账户。密钥留在原生层，使用受 Android Keystore 保护的包装密钥加密。签名结果会在返回 Web 应用之前进行验证。该外壳支持 [NIP-07 浏览器签名](/zh/topics/nip-07/)和加密请求。签名器选择界面仅在需要时打开，并协调并发请求。

### Nostr WoT SDK

信任网络库 [Nostr WoT SDK 将身份验证授权](https://github.com/nostr-wot/nostr-wot-sdk/pull/15)扩展到具有明确类型的原生和远程请求方。显示提示前会检查已存储的拒绝决定，可复用的授权则绑定到请求所用的传输方式和目标。Web 请求默认仍采用一次性授权。其[托管式 Blossom 上传](https://github.com/nostr-wot/nostr-wot-sdk/pull/13)会验证不可变的字节内容，支持取消，并在活动会话更改时停止，同时采用绑定到服务器的身份验证和重定向限制。

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49)提供桌面安装程序。另外，已合并的服务器端工作[新增了持久化定时发布功能](https://github.com/flox1an/nostube/pull/126)。event 会在预定时间之前完成签名，存入 SQLite，再由工作进程发布；停机后，该进程会补发到期内容。其[编辑和删除流程](https://github.com/flox1an/nostube/pull/124)会跟踪墓碑记录、镜像投递和自有文件清理。[首次运行设置](https://github.com/flox1an/nostube/pull/134)会区分用户的浏览器签名器与服务器管理的频道密钥。历史上无归属的 blob 仍不在自动清理范围内。

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24)新增私密短片协作，支持贡献者署名，并检查经签名的拍摄或编辑来源记录。观众所选的翻译字幕在翻译待完成或未经验证时会回退到原始字幕。这些来源检查并不能保证录像未经编辑。

这款短视频客户端的[路由更改](https://github.com/divinevideo/divine-mobile/pull/9884)会为文字和视频聊天消息查询收件人的收件箱 relay，并保留投递结果不确定的状态。[发送者副本处理](https://github.com/divinevideo/divine-mobile/pull/10006)让用户自己发送的群组消息能够出现在其其他设备上；对于此前被丢弃的副本，需要重新导入账户。[已取消的部分群组发送](https://github.com/divinevideo/divine-mobile/pull/10031)会保留“未发送给所有人”记录；取消是终止状态，这些记录无法重试。创建群组和识别其他成员新建房间的功能仍[受默认关闭的功能开关控制](https://github.com/divinevideo/divine-mobile/pull/10020)。

后续主分支更改[将中断的数据库恢复副本保留在临时缓存之外](https://github.com/divinevideo/divine-mobile/pull/10118)，并[在重建期间保留定时帖子、排队中的举报、个人资料编辑和已移除聊天记录](https://github.com/divinevideo/divine-mobile/pull/10115)。[发送时限涵盖 relay 重连时间](https://github.com/divinevideo/divine-mobile/pull/10127)，将放弃发送后的重试阈值从 160 秒降至 137 秒。[索引器收件箱查询使用独立的有界池](https://github.com/divinevideo/divine-mobile/pull/10116)，避免排在信息流读取之后等待；如果联系人列表在确认前发生变化，[关注控件会保留已选择的操作](https://github.com/divinevideo/divine-mobile/pull/10147)。这些后续合并使缓慢重连期间留给 relay 确认的时间更少；数据库修复无法恢复此前已丢失的数据。后续加入的[需主动启用的录制副本功能](https://github.com/divinevideo/divine-mobile/pull/10110)允许 Android 和 iOS 相册备份保留新录制的短片。对于没有签名来源记录的副本，系统会发出警告，且不允许重新导入；此功能默认关闭，并需要额外存储空间。

### Conduit

[Conduit 中的商务应用获得共享的持久化收件箱](https://github.com/Conduit-BTC/conduit-mono/pull/616)，在 Market 和 Merchant 之间保留加密消息的投递与恢复能力。即使发送者自存副本失败，收件人 relay 已接受的状态仍会保留，恢复时会复用相同字节内容，以避免在语义上再次发送。[由签名器支持的共享钱包](https://github.com/Conduit-BTC/conduit-mono/pull/635)连接这两个应用。该恢复路径将恢复用明文托付给签名器；仅完成源代码集成，既不能证明已经上线部署，也不能证明已完成使用实际资金的验收测试。当多条账户路由共用一个 URL 时，[独立的 relay 授权](https://github.com/Conduit-BTC/conduit-mono/pull/645)仍会保留。禁用一条路由不再抹除另一条已签名的 relay 列表授权或收件箱授权，需要身份验证或未完成的读取仍保留为不可用结果。[已合并的支付路由器](https://github.com/Conduit-BTC/conduit-mono/pull/613)将一笔经买家批准的入金付款拆分为向商家和供应商支付的 Lightning 款项，随后支付 Conduit 费用，并通过共享的 Nostr 收件箱实现精确意图核对与加密恢复。生产环境和预发布环境中的执行仍处于禁用状态；提供方完成操作并不能证明收款人已领取款项，也不能证明该笔支付已最终结清。

### Bitcredit

[Bitcredit 的持久化加密](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041)使用个人身份的助记词，保护其电子票据应用的身份密钥、公司密钥和票据密钥，以及 Nostr 重发队列。初始化需要匹配的助记词。[实例管理](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043)允许测试网和主网实例在同一台设备上各自独立运行后台 Nostr 订阅。

## 新项目

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0) 推出了一款密码管理器，其加密密码库通过 Nostr 同步。它支持外部签名器并保留条目的并发版本，支持 Bitwarden JSON 导入和导出。变更会先保存在本地，再等待 relay 接受。此次发布同时提供 Android、桌面端和 CLI 下载。项目称其尚处于早期阶段，并建议使用经过验证的管理器保存关键密码；该版本的协议规范仍为空。其 [Web 存储](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md)将加密密钥与受保护的数据存放在一起。

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md) 新增了基于 Nostr 的 MLS 群聊 Common Lisp 实现。10 月 9 日的代码加入了竞争性提交的收敛处理和加密 Blossom 附件，作者报告已与 MDK 的 wn 命令行客户端进行互操作性测试。该实现尚未经审计，账户密钥和消息日志也未做静态加密。定时收敛窗口、超出回滚范围的重放以及群组解散仍未实现；所检查的测试框架使用临时本地 relay。

### nalgorithm Android

[nalgorithm 的 Android 版本](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0)构建了按偏好排序的 Nostr 信息流，以及可离线播放的后台音频摘要。用户可以选择按 Lightning 计价的托管推理，也可以选择由手机发起请求、使用自有密钥的推理；这是两条独立路径。登录支持通过远程签名使用 Amber。后续版本先[修复自有密钥模式下的排序和关注列表发现](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1)，随后[在某个 relay 发生故障时保留正常 relay 上的点赞](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2)，并改进摘要恢复。[版本 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3) 调整了模型设置顺序，并会报告连接测试缺少的输入。

## 协议与规范工作

### 经过身份验证的 napplet 端点

在面向 napplet 应用的 NAP 规范中，10 月 9 日合并的 [NAP-INC 端点标识符](https://github.com/napplet/naps/pull/104)用经过身份验证的标识符取代了单独的处理器名称。不同发布者使用相同名称时，不再被视为同一个对等方。通信仍由运行时居中协调，根清单或快照清单不需要具名的 `d` 坐标。

### 调用链接中的处理器推荐

同样于 10 月 9 日合并的[调用链接推荐机制](https://github.com/napplet/naps/pull/99)允许添加可选的 `#naddr` 处理器推荐。Shell 可以提供发现和安装功能，并以常规解析作为后备方案。已保存的偏好和 Shell 策略具有优先权。因此，推荐的处理器只是提供发现线索，不会取代用户现有的选择，也不会将安装权限转交给链接发送者。

### 投递接受与应用处理

[意图通告与投递机制的变更](https://github.com/napplet/naps/pull/91)使用对发布者安全的标识符，从同一份经过验证的清单中派生角色和意图。接受投递不再依赖源应用持续运行。`ok: true` 响应表示承担投递责任，并不意味着目标应用的处理已经完成。在这项已合并的规范变更中，重试和重启行为仍由运行时策略决定。

### Cyberspace 操作链

[Cyberspace 修订后的链规则](https://github.com/arkin0x/cyberspace/pull/48)规定，分叉会使一条已签名操作链从其生成点起失效，并要求客户端在签署下一项操作前确认当前有效的链头。这个以 Nostr 为支撑的世界新增了 [140 条已签名的合成链](https://github.com/arkin0x/cyberspace/pull/49)，并附有供各实现遵循的规范性判定。[复制署名规则](https://github.com/arkin0x/cyberspace/pull/47)使用 `q` 引用指向原始对象，并在公开混创时通知原作者；密封副本则省略该通知。这些均为已合并的项目规范，但尚未核实已部署的验证器对其覆盖到什么程度。

### Relay 持久化确认

[尚待审议的持久化提案](https://github.com/nostr-protocol/nips/pull/2496)引入了持久化确认、PROOF 查询，以及可选的已签名 kind 1797 relay 证明。签名使存储声明可归属于某个 relay，但并不能证明其会持续保留数据。查询还会透露客户端对哪些 event 感兴趣。

### Marmot 群组的共享置顶

[Marmot 尚待审议的置顶提案](https://github.com/marmot-protocol/marmot/pull/434)为最多 64 条消息引用定义了经过身份验证的共享状态，并设置成员和管理员权限。变更生效需要一次 MLS Commit 和 epoch 转换，而且变更后的每个成员叶节点都必须支持该功能。置顶不会复制消息正文，也不会延长保留时间，因此不可用的目标仍然无法解析。所提供的测试样例假定状态已经通过身份验证；它们并未展示密码学处理或跨客户端收敛。

## NIP 深入解析：NIP-36 与 NIP-38

### 显示前的内容警告

[NIP-36：敏感内容](/zh/topics/nip-36/)允许作者为 event 添加 `content-warning` tag，并可选择附上原因。客户端可以隐藏内容，直到读者选择显示。[规范](https://github.com/nostr-protocol/nips/blob/master/36.md)将界面设计交由客户端决定，并允许使用补充性的标签 tag。添加警告不会改变哪些人能够读取该 event。对于公开帖子，relay 和其他客户端仍会收到其内容。

[Amethyst 的警告 tag 解析器](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt)能够识别该 tag，并将缺失或空白的原因视为未指定。[Coracle 的编辑器](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte)会将原因写入 tag；其[内容视图](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte)会遵循读者的敏感内容设置，并提供显示内容的操作。[noStrudel 的帖子视图](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx)在显示警告界面之前，会应用自身的警告偏好和展开状态。

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md)不会加密 event，也不要求隐藏内容。没有警告并不说明内容的性质；客户端自行决定警告如何影响预览和显示控件。

### 个人资料状态与过期

[NIP-38：用户状态](/zh/topics/nip-38/)使用可寻址的 kind 30315 event。作者、kind 和 `d` tag 共同标识一个状态坐标；`general` 和 `music` 具有已定义的含义。较新的 event 会替换该坐标上的先前状态，而不同的 `d` 值则彼此独立。空内容会清除状态。[规范](https://github.com/nostr-protocol/nips/blob/master/38.md)还允许引用 URL、个人资料、event 和地址。

下面这条已签名的 [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) event 展示了一个已过期的通用状态。作者的原始拼写予以保留。

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[Damus 的状态模型](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift)处理带有过期时间的一般状态和音乐状态。[Nostria 的状态服务](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts)会忽略空值或已过期的值，并根据曲目时长发布音乐状态；其常规订阅仅请求一般和音乐这两种类型。[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt)在清除状态时会保留 `d` 标识符。因此，自定义类型除了采用共用的传输结构外，还需要另行约定。

状态是作者公开作出的声明。它们不能证明作者在线，也不能证明某人听过某首曲目。发布音乐状态或是否有空的信息可能会透露生活习惯，而可选的过期时间只能限制过时状态的展示，并不保证删除。与 NIP-36 一样，[NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md)仍是一项可选的草案规范。客户端可以独立实现其中任一规范，读者看到的内容则由客户端的显示设置决定。
