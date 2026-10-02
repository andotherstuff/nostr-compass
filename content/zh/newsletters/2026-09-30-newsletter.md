---
title: "Nostr Compass #42"
date: 2026-09-30
publishDate: 2026-09-30
translationOf: /en/newsletters/2026-09-30-newsletter.md
translationDate: 2026-10-02
draft: false
type: newsletters
description: "Nostr Compass #42 介绍 Compass Android 应用，并报道 White Noise 投票、稳定版 Dart NDK、Holoboard 与 FIPS、新的 Nostr 应用、relay 与签名器变更，以及六年来九月的里程碑。"
---

欢迎回到 [Nostr Compass](https://nostrcompass.org)，这里是你的每周 Nostr 指南。

我们专属的 [Nostr Compass Android 应用](https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android)把周刊、播客节目、主题指南和贡献者语音笔记集中到一处。其[最新的已签名版本说明](https://zapstore.dev/apps/naddr1qq2x7un89ehx7um5wf3k7mtsv9ehxtnpwpcqzxrhwden5te0wfjkccte9eaxzurnw3hhyefwv3jhvq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qqxpqqqplqk563kdn)介绍了经过签名验证的完整周刊、可离线使用的已保存期数和 110 份主题指南，以及覆盖文章和现有转录文本的本地搜索。贡献者可以录制语音笔记并以语音回复，在发送前回听已保存的录音，并通过 Amber 签名，而无需在应用中存储私钥。公开录音会发布到 Nostr 和 Blossom 上。

[最新的应用更新](https://zapstore.dev/apps/naddr1qq2x7un89ehx7um5wf3k7mtsv9ehxtnpwpcqzxrhwden5te0wfjkccte9eaxzurnw3hhyefwv3jhvq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qqxpqqqplqk563kdn)会在 Android 停止后台工作时保留排队中的录音和上传检查点，在需要 Amber 批准时给出提示，并能从通知直接打开相应录音。节目视图和语音笔记视图各自保留滚动位置，播放也会从同一位置继续。新录音的通知取决于 Android 的调度机制和权限设置。

**本周内容：**[White Noise](#white-noise-android-adds-group-polls-and-account-specific-disappearing-message-defaults) 加入了加密群组投票以及聊天历史不完整时的提示；[Holoboard](#holoboard-adds-nostr-promotion-commands-and-an-android-app) 加入了[私信推广命令](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md#2026-09-23)和一款 Android 应用；[fips-pub-domains](#fips-pub-domains-tests-signed-public-names-for-a-mesh) 在网状网络上测试经过签名的公共名称；[Marmot MDK](#marmot-mdk-0110-makes-account-history-gaps-visible) 让缺失的加密群组历史变得可见；[Myco](#myco-080081-gives-nearby-apps-their-own-nostr-store) 则为附近设备间的应用共享提供了 Nostr 身份和应用商店。[nostream](#nostream-310-adjusts-relay-proof-of-work-to-load) 会根据负载调整 relay 准入要求，而 [Nostr double ratchet](#nostr-double-ratchet-0017100172-closes-a-removed-member-gap) 弥补了已移除成员的漏洞。开发中的工作修复了 [Amethyst 的加密群组互操作性](#amethyst-repairs-encrypted-group-interoperability)，加入了 [Divine 的加密视频消息](#divine-adds-encrypted-video-to-direct-messages)，并让 [Nostr Atlas](#nostr-atlas-opens-a-directory-for-checkable-identities) 上线。协议更新完善了身份证明、relay 邀请、关注集合以及拟议的域名声明。月末的[九月回顾](#six-years-of-nostr-septembers)沿着同样的问题回看 Nostr 的六年历程。

## 头条新闻 {#top-stories}

### Holoboard 加入 Nostr 推广命令和 Android 应用 {#holoboard-adds-nostr-promotion-commands-and-an-android-app}

[Holoboard](/zh/topics/holoboard/) 是一个[用于发现 Nostr 笔记的看板](https://holoboard.space)，其排名可以通过 Lightning 支付来提升。原始帖子仍然是 Nostr event；Holoboard 通过自己的 HTTP API 提供排名和展示数据。如果读者以为看板的排序是 relay 原生的 feed，这一区别就很重要。

其 [9 月 23 日的更新日志](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md#2026-09-23)记录了同时支持加密 [NIP-17](/zh/topics/nip-17/) 和旧版 [NIP-04](/zh/topics/nip-04/) 路径的私信推广命令。NIP-17 会封装私信，向 relay 隐藏其内容和发送者，而 NIP-04 是较早的私信加密格式。用户可以在同一对话中请求推广发票，为首次付费推广收到一份带标签的报价，并通过回复 `YES` 选择接收到期提醒。推广发送端会重试失败的 relay，而 [9 月 24 日的更新](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md)加入了 Android 应用，并简化了发票流程。

该项目的 [relay 集成说明](https://github.com/ptrio42/holoboard.space/blob/main/relay/README.md)描述了 Nostr 上的普通笔记和评论、加密收件箱路由，以及引用和删除的处理。其已签名的 [Zapstore Android 应用列表](https://zapstore.dev/apps/space.holoboard.app)可以证明存在一个应用版本，但尚未确认该列表所用的密钥就是 Holoboard 的公共看板身份。这是 Compass 首次报道该项目。

### fips-pub-domains 为网状网络测试经过签名的公共名称 {#fips-pub-domains-tests-signed-public-names-for-a-mesh}

[fips-pub-domains](/zh/topics/fips-pub-domains/) 是一个新的[解析器与命名实验](https://github.com/fr34aky/fips-pub-domains)，它把公共域名绑定到 FIPS 上的节点；FIPS 是一种利用 Nostr 消息进行 peer 发现的加密网状网络。其[首个版本](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0)将这些声明与 DNS TXT 记录、可选的 DNSSEC 验证、本地固定的绑定、一个 Linux 解析器守护进程，以及与 fips2go（手机上的 FIPS 客户端）的 Android 集成结合起来。仅凭一条签名声明并不能证明对公共域名的所有权；客户端还需要 DNS 或 DNSSEC 证据、已配置的见证方，或此前受信任的固定绑定。

[0.2.0 版本](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0)在声明中加入了 DNSSEC 证明，使只连接网状网络 relay 的客户端也能验证一个未固定的名称，并允许多台经过验证的服务器为同一域名提供服务。它还修复了过期的固定绑定和 DNS 故障转移。[0.2.1 版本](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1)修复了一个原本无法启动的 systemd 单元，并让服务器无需 root 运行；现有安装必须替换该单元才能获得修复。

在 Android 上，[一项已合并的 fips2go 变更](https://github.com/fr34aky/fips2go/pull/55)让其 DNS 代理遵循经过验证的公共名称绑定。[第二项已合并的变更](https://github.com/fr34aky/fips2go/pull/59)让通往已配置 Nostr relay 的连接经由网状网络传输，因此即使手机没有互联网连接，解析器也能获取并验证此前未见过的域名声明。这些设备测试结果由维护者在上述 pull request 中报告；它们并不能证明已有更广泛的部署。

该项目的[双节点和仅网状网络 relay 测试](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)是维护者针对早期实现报告的证据，而不是生产部署。其 [NIP-DB](/zh/topics/nip-db/) [提案](https://github.com/nostr-protocol/nips/pull/2487)仍处于开放状态，[草案](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)中的 event kind 在完成注册前仍是占位符。上周的 fips2go 报道关注的是网状网络引导和 peer 发现；本周的工作则处理公共名称和验证。

### Marmot MDK 0.11.0 让账户历史缺口变得可见 {#marmot-mdk-0110-makes-account-history-gaps-visible}

[Marmot MDK](https://github.com/marmot-protocol/mdk) 是用于 [MLS 加密 Nostr 群组消息](/zh/topics/marmot/)的 Rust 运行时及生成的绑定，继上周的持久化发送版本之后，它发布了 [0.11.0 版本](https://github.com/marmot-protocol/mdk/releases/tag/v0.11.0)。账户恢复现在只有在每个必需的 relay 都完成一次未截断的 event 比对后，才会宣布某个历史缺口已补全；无法证明已补全的缺口会生成一条持久提示，宿主应用可以将其展示给用户。投递队列已满时会把 event 溢出写入账户数据库，而不是丢弃它们；实时投递会推进传输游标，因此重启后不会再次获取相同的历史。

[完整版本说明](https://github.com/marmot-protocol/mdk/blob/v0.11.0/docs/release/0.11.0.md)还介绍了可选的加密群组投票、绑定中的无状态 event 验证，以及针对 16 KB 内存页对齐的 Android 库。应用必须同时迁移这一源代码批次中生成的绑定和原生库；账户数据库会在首次打开时迁移到 schema 98，且不支持数据库降级。一个现有的间歇性追赶缺陷仍可能导致落后超过五个群组 epoch 的消息无法解密，而且不会触发提示，因此该版本并不声称在所有情况下都能完整恢复历史。

### Myco 0.8.0–0.8.1 为附近设备间的应用提供专属 Nostr 商店 {#myco-080081-gives-nearby-apps-their-own-nostr-store}

[Myco](https://github.com/Origami74/myco) 是一款 Android 应用，用于与附近的手机交换称为 napplet 的小型 Nostr 程序，即使在离线时也可以。[0.8.0 版本](https://github.com/Origami74/myco/releases/tag/v0.8.0)为每次安装提供一个访客 Nostr 身份，并允许使用现有密钥或 Amber 登录；Amber 是一款 Android 签名器，可以在不共享账户密钥的情况下批准签名。它还用一个本身就是 napplet 的应用商店取代了 Discover 标签页。该商店读取已签名的应用列表和推荐，而下载的更新可以在用户 Circle 中的手机之间传递，无需互联网连接。

[0.8.1 版本](https://github.com/Origami74/myco/releases/tag/v0.8.1)通过查询作者公布的 relay，让这些应用列表更容易被找到；早期版本依赖公共默认 relay。它会立即显示缓存的个人资料和应用，保存较慢的 relay 应答以供下次访问使用，对失败的 relay 进行退避，并在视图打开期间保持订阅活跃。两次更新都保留了现有的手机间线路格式。已更新的手机可以下载和共享 napplet 更新；较旧的手机只转发其公告。

## 带 tag 的版本发布 {#tagged-releases}

### White Noise Android 加入群组投票和按账户设置的阅后即焚默认值 {#white-noise-android-adds-group-polls-and-account-specific-disappearing-message-defaults}

[White Noise Android](https://github.com/marmot-protocol/whitenoise-android) 是一款用于私密 [Marmot](/zh/topics/marmot/) 加密对话的 Nostr 通讯应用。继[上周报道的](/en/newsletters/2026-09-23-newsletter/#white-noise-android-2026921-improves-encrypted-chat-reliability-and-sharing)投递和分享改进之后，[9 月 30 日的版本](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30)通过 Marmot Development Kit 加入了群组投票，支持可选答案、结果条和截止时间。它还加入了[按账户设置、保存在设备本地的阅后即焚默认值](https://github.com/marmot-protocol/whitenoise-android/pull/2799)：新的私聊和群组会继承所选时长，而现有对话及其单独设置保持当前策略。[Wave hi](https://github.com/marmot-protocol/whitenoise-android/pull/2765) 会发送一条提及新加入成员的问候，同时不打扰当前草稿。

该[版本](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30)让用户为个人资料和群组图片选择焦点裁剪区域，并可在删除聊天文件夹时不删除其中的对话。其[历史提示](https://github.com/marmot-protocol/whitenoise-android/pull/2869)会在恢复过程可能导致账户或群组历史不完整时显示出来，并分别提供关闭控件。[对话分页](https://github.com/marmot-protocol/whitenoise-android/pull/2818)避免在跳转到最新消息时重建所显示的时间线，[待发送消息编辑](https://github.com/marmot-protocol/whitenoise-android/pull/2825)会在原消息发送并取得已确认的 event ID 期间保留编辑后的文本。这种编辑交接覆盖运行中应用内的对话切换；并不能证明在进程终止后依然保留。

[语音输入现在可为每段录音选择粘贴或发送](https://github.com/marmot-protocol/whitenoise-android/pull/2768)，自动结束时会把转录文本放入草稿。[离线识别服务设置](https://github.com/marmot-protocol/whitenoise-android/pull/2888)会说明设备端处理方式，将其授权与其他语音服务分开，并在录制结束后恢复被中断的媒体播放。[通用文件处理](https://github.com/marmot-protocol/whitenoise-android/pull/2830)接受大小受限、非空的文档，并提供准确的文件名、MIME 元数据和失败提示；[显式附件下载](https://github.com/marmot-protocol/whitenoise-android/pull/2879)使用 Android 的用户发起传输任务，并以前台方式作为后备。[粘贴控件](https://github.com/marmot-protocol/whitenoise-android/pull/2877)现在使用 Android 的系统操作，使 GrapheneOS 的 Secure Paste 可以授予剪贴板访问权限。Android 版还会[将 iOS 分享的 GIPHY 渲染为动画媒体](https://github.com/marmot-protocol/whitenoise-android/pull/2806)，同时遵守下载策略。

[通知修复](https://github.com/marmot-protocol/whitenoise-android/pull/2808)会刷新发送者昵称，并在打开对话时清理相关提醒。[通知恢复变更](https://github.com/marmot-protocol/whitenoise-android/pull/2712)在前台归属不可用时保留待处理的推送工作，并使用有上限的重试。[Amber 签名](https://github.com/marmot-protocol/whitenoise-android/pull/2802)会协调同一账户的集中批准请求，防止速率限制导致发送被取消。[新的审计配置](https://github.com/marmot-protocol/whitenoise-android/pull/2872)会在上传到新的接收端之前重新征求用户是否共享日志。源代码也[改用 AGPL-3.0-only 许可证](https://github.com/marmot-protocol/whitenoise-android/pull/2840)。


### nostream 3.1.0 根据负载调整 relay 工作量证明 {#nostream-310-adjusts-relay-proof-of-work-to-load}

[nostream](https://github.com/Cameri/nostream) 是一个以 PostgreSQL 为后端的 TypeScript Nostr relay。[3.1.0 版本](https://github.com/cameri/nostream/releases/tag/v3.1.0)可以随着观测到的 event 速率变化，在运营者设定的上下限之间提高或降低 event 工作量证明门槛。该设置默认关闭，使用每个 worker 实测的速率，并且与现有的静态公钥门槛相互独立，因此只有运营者主动启用后，发送者才会看到不同的准入要求。

同一[版本](https://github.com/Cameri/nostream/releases/tag/v3.1.0)加入了一个管理面板，显示 relay、WebSocket 和 event 指标、网络健康探测结果，并支持可配置的运营者通知。其管理 API 默认禁用。这些控件帮助运营者区分 relay 压力和可达性问题，同时让新策略始终处于显式配置之下。

在发布这一负载敏感的工作量证明版本之后，nostream 合并了[针对受信任审核者举报的处理操作](https://github.com/cameri/nostream/pull/788)。[NIP-56](/zh/topics/nip-56/) 定义了内容举报 event；新的 `nip56.hideActionableReports` 选项会在同时启用举报功能时，把被举报的 event 从 REQ 和 COUNT 结果中排除。针对 event 的举报会隐藏该 event，而针对公钥的举报会隐藏该作者的所有 event。新选项默认为 false，因此仅启用举报收集不会改变现有查询结果。

### Nostr double ratchet 0.0.171–0.0.172 弥补已移除成员的漏洞 {#nostr-double-ratchet-0017100172-closes-a-removed-member-gap}

[Nostr double ratchet](https://github.com/irislib/nostr-double-ratchet) 是一个用于通过 Nostr 承载加密私聊的 TypeScript 库。[0.0.171 版本](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.171)会在成员变动后轮换群组的发送者密钥，使持有旧密钥而已被移除的人无法解密来自已更新发送者的后续消息，即使该发送者重启后也是如此。它还会拒绝已被移除的本地所有者发送消息或轮换密钥，并在密钥分发期间成员发生变化时中止发送。

[0.0.172 版本](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.172)在可选的加密邀请响应中携带现有的、由账户签名的设备批准。使用该更新的接收方可以在单独的注册 event 到达之前验证发送者的设备，而已关联的设备在重启后仍保留其批准。该邀请字段是可选的，原有握手和 ratchet 消息格式保持不变。

[0.0.173–0.0.175 版本](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.175)延续了这项移除相关工作，加入持久化的群组密钥交接，并在发布前保存排队中的投递状态，使中断的交接在重启后得以恢复。发布回调携带本地群组上下文，使应用能够在成员被移除后取消持久重试，同时保证成员控制消息仍可投递；排队的发送会保留其原始内部 event ID。重复的邀请响应会保留已建立的会话，订阅在联系人变化时保持稳定，应用密钥快照会保留设备名称且不共享可变副本。签名后的线路格式保持不变；[0.0.173 的说明](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.173)还提到 Rust 0.0.168 加入了接收会话后备机制和本地群组回显过滤。

### Scramble 0.7.4–0.7.5 获取新群组成员应当看到的消息 {#scramble-074075-fetches-the-messages-a-new-group-member-should-see}

[Scramble](https://github.com/DavidGershony/Scramble) 是一款带有原生 Android 界面的跨平台 Marmot 群组通讯应用。在 [0.7.5 版本](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.5)中，每个群组都有自己的 relay 历史截止点：此前，最活跃对话的截止点会被应用到所有群组，因此新加入的群组可能一直是空的，因为加入之后的消息从未被请求。重连路径也获得了相同的修复，而且没有本地活动的群组现在会请求所有可用消息；MLS 仍然会阻止新成员解密加入之前发送的消息。

之前的 [0.7.4 版本](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.4)修复了因 Android 列表行复用导致点击处理器累积而出现的重复接受邀请问题，并让自定义 Blossom 媒体服务器设置在原生应用中得以保存。0.7.5 版本只提供原生 Android APK，因此追踪旧 Avalonia 文件名的用户必须更改更新目标。账户和历史可以在这两个 Android 版本之间迁移，但在旧的 0.6.x MLS 引擎下创建的群组不会迁移到 0.7.x。

[Scramble 0.7.6](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.6) 加入了一个手动的“获取缺失消息”控件，它会查询群组曾经使用过的每个路由地址，取消时间限制，修复过期的已存储地址，并报告恢复了哪些内容。它仍然无法解密用户加入之前的 epoch。原生应用中的管理员可以提升或降级其他成员，并能看到当前成员名单状态和可见的失败结果；双人对话仍然隐藏这些控件。群组信息中的“复制”操作现在可以响应，不过受邀加入的对话仍可能复制内部聊天标识符，而非协议群组 ID。[0.7.7 版本](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.7)还会[在其他成员的 commit 到达时处理积压的消息](https://github.com/DavidGershony/Scramble/commit/35e72177a0009ec96e8494caed7e9c250b66c7cb)；[0.7.8](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.8) 为这一被动成员路径加入了回归测试。

### Amber 6.6.6 修复远程签名器连接密钥 {#amber-666-repairs-remote-signer-connection-secrets}

[Amber](https://github.com/greenart7c3/Amber) 是一款 Android 签名器，可在不把账户密钥交给应用的情况下批准 Nostr event 签名。继上周的备份加密变更之后，[6.6.6 版本](https://github.com/greenart7c3/Amber/releases/tag/v6.6.6)修复了其 `nostrconnect` 解析器：包含 `=` 的连接参数（例如带填充的密钥）此前会在 Amber 应答之前被改动。这导致基于 NDK 的客户端即使在签名器连接看似正常时，也无法通过密钥检查。

该[版本](https://github.com/greenart7c3/Amber/releases/tag/v6.6.6)还会把反馈 issue 发送到 Amber 仓库公告中公布的 relay，如果无法获取该公告，则回退到之前的 relay。更长的 Tor 超时让较慢的 relay 有更多时间确认这次发布。其余变更改善了 Amber 各主题中图标和文字的可见性。

### FIPS 0.5.2 堵住 Nostr 发现中的隐私泄露 {#fips-052-stops-a-nostr-discovery-privacy-leak}

[FIPS](https://github.com/jmcorgan/fips) 是一种利用 Nostr 身份和 relay 消息发现 peer 的加密网状网络。其 [0.5.2 维护版本](https://github.com/jmcorgan/fips/releases/tag/v0.5.2)不再用节点的路由密钥签署 NAT 穿透删除请求，此前这种做法会在 relay 上把该密钥与穿透流量关联起来。它还将用于 relay 连接的 TLS 库更新到修复了一项已公开安全公告的版本，并修复了链路和会话重新协商密钥时的几种消息丢失情况。

[版本说明](https://github.com/jmcorgan/fips/releases/tag/v0.5.2)要求所有平台的运营者升级，同时详细列出了 Windows 密钥文件权限、网关和软件包服务方面的单独修复。临时节点不再写入可能在之后重启时被覆盖的私有 `fips.key`；希望保持稳定身份的运营者应在升级前设置持久模式。该版本不改变网状网络的线路格式，因此不同版本的节点可以逐个升级。

### napplet soyLI 0.23.1–0.23.4 修复后端发布和签名器批准 {#napplet-soyli-02310234-repairs-backend-publishing-and-signer-approval}

[napplet.soy 的 soyLI](https://github.com/zeSchlausKwab/napplet-soy) 是一套面向小型沙箱化 Nostr 程序的创作与发布工具包。继上周的共享创作版本之后，[0.23.1 版本](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.1)把后端清单、处理程序和 schema 纳入创作者检查和多人预览。它将可移植的提供方配置保留在项目清单中，同时把私有身份绑定和开发数据库排除在已发布的源代码快照之外。

[0.23.2 版本](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.2)让曾经提交过生成的公共后端上下文的项目在通过严格验证后可以再次发布，同时仍会拒绝可达历史中的私有绑定、日志、数据库和凭据。之后的 [0.23.4 版本](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.4)修复了一个持久后端会话故障：当用户花几秒钟才完成签名时，有效的扩展或远程签名器批准可能被拒绝。公共宿主也需要应用共享宿主修复；仅更新创作者的 CLI 并不能修复已部署的宿主。

### Dart NDK 0.10.0 限定 Blossom 认证和远程签名的范围 {#dart-ndk-0100-scopes-blossom-auth-and-remote-signing}

[Dart NDK](https://github.com/relaystr/ndk) 是一个 Flutter 和 Dart 库，用于 Nostr relay 访问、签名、钱包请求和媒体操作。继上周的预发布版本之后，[0.10.0-dev.7](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.7) 让 Blossom 媒体请求在服务器拒绝之前保持匿名，然后通过一项显式策略进行授权，该策略规定某个操作可以暴露哪个身份。它在整个请求路径中传递这一授权，并取代了旧的 `useAuth` 和 `customSigner` 选项，这对使用预发布 API 的应用来说是破坏性的集成变更。

[Dev.9](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.9) 不再等到最慢的 relay 确认之后才返回远程签名器响应。[Dev.8](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.8) 减少了后台 relay 轮询和缓存工作；其他修复涉及钱包种子持久化和结算截止时间。[稳定版 0.10.0](https://github.com/relaystr/ndk/releases/tag/v0.10.0) 现在把这一开发系列与下文的连接元数据和私有订阅 ID 变更一起打包发布。[与 dev.9 的对比](https://github.com/relaystr/ndk/compare/v0.10.0-dev.9...v0.10.0)包含了这些已合并的变更。升级的应用应同时检查媒体认证 API 变更和远程签名器响应路径。

稳定版包含 [NIP-46 连接元数据和请求权限](https://github.com/relaystr/ndk/pull/852)，用一个 `Nip46ClientMetadata` 值取代了分散的连接字段。这一源代码 API 变更让登录组件可以把应用身份和请求的权限传给 bunker。另一项[请求 ID 变更](https://github.com/relaystr/ndk/pull/860)在生产环境中使用 32 个随机十六进制字符，使用例名称和分页阶段不会出现在 relay 可见的订阅 ID 中。显式 ID 仍受 NIP-01 的 64 字符上限约束，而调试模式保留一个简短的诊断名称。

### Mostro Core 0.16.0 移除旧的 gift-wrap 传输 {#mostro-core-0160-removes-the-old-gift-wrap-transport}

[Mostro Core](https://github.com/MostroP2P/mostro-core) 提供 Mostro 基于 Nostr 的点对点交易客户端和协调器所使用的消息协议。[0.16.0 版本](https://github.com/MostroP2P/mostro-core/releases/tag/v0.16.0)移除了其协议 v1 的 gift-wrap 传输以及旧的 wrap 和 unwrap 函数，只保留较新的传输作为库的路径。对于仍通过该库构造或读取 v1 消息的应用来说，这是一项破坏性变更。

该[库版本](https://github.com/MostroP2P/mostro-core/releases/tag/v0.16.0)先于协调器[现已发布的 0.19.0 版本](https://github.com/MostroP2P/mostro/releases/tag/v0.19.0)。为旧客户端提供服务的运营者需要同时更新传输迁移的两端。之前的 [0.15.1 tag](https://github.com/MostroP2P/mostro-core/releases/tag/v0.15.1) 加入了一种协商取消的争议状态，但传输移除才是兼容性方面的里程碑。

### Cambium 0.6.0–0.7.1 通过 relay 消息登记解锁手机 {#cambium-060071-enrolls-an-unlock-phone-through-relay-messages}

[Cambium](https://github.com/forgesworn/cambium) 是一款面向 Heartwood 硬件密钥的 Android 签名伴侣应用，也能在重启后解锁该开发板。[0.6.0 版本](https://github.com/forgesworn/cambium/releases/tag/v0.6.0)让手机可以通过开发板的 Nostr relay 登记解锁功能，无需 USB 线；用户在按下开发板按钮之前，需要在手机、开发板和 Sapwood（开发板的登记界面）上核对五个请求词。新公布的 relay 会加入随机化的连接延迟，使手机的首次联系不会暴露它看到开发板更新的确切时间。

[0.7.0 版本](https://github.com/forgesworn/cambium/releases/tag/v0.7.0)反转了邀请流程：手机扫描 Sapwood 短时有效的二维码，然后用一个一次性密钥返回一个加密的一次性 event。如果没有 relay 接受该 event，重试会重新发布同一个 event，而旧的代码显示路径仍为较旧的 Sapwood 版本保留。[0.7.1 补丁](https://github.com/forgesworn/cambium/releases/tag/v0.7.1)让最终校验码保持可见，并改善了 F-Droid 构建的可复现性；二维码流程仍需要指定的较新 Sapwood 和 Heartwood 版本。

### Bray 3.5.0–3.5.2 限制由代理发起的 Nostr 钱包支出 {#bray-350352-limits-agent-initiated-nostr-wallet-spending}

[Bray](https://github.com/forgesworn/bray) 是一个 Nostr 工具服务器，让 AI 助手通过有范围限制的接口请求 relay、身份和钱包操作。其 [3.5.0 版本](https://github.com/forgesworn/bray/releases/tag/v3.5.0)为每笔 Nostr Wallet Connect 支付加入了上限和持久化的每日预算，并在助手宿主支持时要求人工确认。提供独立的支出连接现在需要一项显式的钱包服务设置，每次使用前都会重新检查授权，并把发票查询限定在该授权范围内的哈希。

该[版本](https://github.com/forgesworn/bray/releases/tag/v3.5.0)还提醒用户把钱包连接 URI 保存在私有文件中，而不是粘贴到聊天里，并拒绝把结果不确定的支付当作已证实失败来重试。[3.5.2 版本](https://github.com/forgesworn/bray/releases/tag/v3.5.2)在 relay 拒绝所请求的支付方式过滤器后，改为在本地匹配市场的支付通道。这些检查限制了受委托的助手可以支出的金额，并防止对 relay 过滤器的假设导致匹配的报价被隐藏。

### Mafrend 1.3.0-alpha 把私密地图群组迁移到当前的 Marmot {#mafrend-130-alpha-moves-private-map-groups-to-current-marmot}

[Mafrend](https://github.com/DestBro/mafrend-zapstore) 是一款基于地图的 Nostr 社交应用，让人们探索地点并围绕目的地聊天。其 [1.3.0-alpha 版本](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.3.0-alpha)将私密群组升级到更新的 [Marmot 加密群组](/zh/topics/marmot/)规范，并加入了从聊天和评价中查看个人资料的功能。该群组格式与旧的 alpha 聊天不兼容；用户应把这次更新视为一次存在兼容性中断的 alpha 迁移。

[同一版本](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.3.0-alpha)在地图和标记改进之外，还加入了截图分享和聊天方面的变更。个人资料功能仍被项目标记为开发中。有意义的 Nostr 变更是私密群组互操作性的转变；拥有旧测试群组的用户在升级前应查看兼容性说明。

### Sonar alpha.15–alpha.15.1 修复加密群组发布 {#sonar-alpha15alpha151-repairs-encrypted-group-publishing}

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar) 是一款私密通讯应用，可以通过 Bluetooth 网状网络和 Nostr 承载对话。[Alpha.15](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15) 为消息加入了表情回应，并在加密聊天中加入私密的本地时间分享，同时提供撤销该分享的设置。其钱包改用 Cashu，但这一支付变更与消息更新无关。

[Alpha.15.1](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15.1) 修复了一个启动故障：当旧的分支构建写入了不相容的 schema 版本后，对话索引可能为空。没有索引时，应用每次重新打开都会重新加密本地时间分享并向每个群组重新发布，有时在 relay 速率限制介入之前会发送数百个 event。这个热修复会重建该本地状态，并停止重复的群组发布。

### Elisym 的商务软件包引入私密 Nostr 订单 {#elisyms-commerce-packages-introduce-private-nostr-orders}

[Elisym](https://github.com/elisymlabs/elisym) 是一套基于 Nostr 的代理工具包，目前正在构建一个基于签名 event 的商务流程。其[已合并的 `commerce` 软件包](https://github.com/elisymlabs/elisym/pull/120)为结账和商家组件定义了店铺商品、所有者授权、私密封装的订单和收据，以及报价验证。之后的 [commerce 0.2.0 tag](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0) 会从订单本身派生出该订单的支付参考，把支付查询与已签名的购买流程绑定在一起。

该软件包系列还引入了独立的 payment-core 和浏览器结账工作，但其[版本 tag](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0) 并不能证明完整的商家结账已经部署。在该项目的主要来源中，店铺授权的 event kind 被明确标为临时性质。十一个 SDK、MCP、CLI 和 payment-core tag 标志着同一个正在开发中的商务功能。

[Elisym 新的软件包版本](https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmerchant-node%400.1.0)打包了自托管的商家节点，而 [MCP 0.31.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmcp%400.31.0) 为商务商品加入了 `buy_product` 和 `get_order`。之后的 commerce 和 merchant-node 版本在同一结账流程中加入了 Tempo 支付支持。这些软件包推进了现有的签名商品和私密订单集成；tag 列表并不会让这一临时 event schema 成为标准，也不能证明完整的托管服务已经上线。

### Flotilla 1.11.2 解决签名器卡住和 relay feed 不完整的问题 {#flotilla-1112-unsticks-signers-and-incomplete-relay-feeds}

[Flotilla](https://github.com/coracle-social/flotilla) 是一款面向对话、房间和共享空间的 Nostr 客户端。[1.11.2 版本](https://github.com/coracle-social/flotilla/releases/tag/1.11.2)在启动因等待远程签名器而卡住时为用户提供了退出途径，并会注销本地应用数据已被清除的会话。房间现在可以在其所属的更大空间完成同步之前就显示消息，而 feed 也不再仅仅因为某个 relay 应答比另一个晚就遗漏帖子。

[同一版本](https://github.com/coracle-social/flotilla/releases/tag/1.11.2)还发布了一个使用应用现有密钥签名的 F-Droid 构建，并保持 GitHub 版本为 Obtainium 及时更新。这些分发工作对更换更新渠道的用户很重要，但 relay 和签名器修复才是立即升级的理由。

### Ditto 2.42.3 显示 relay 投递情况并收紧账户边界 {#ditto-2423-shows-relay-delivery-and-tightens-account-boundaries}

[Ditto](https://gitlab.com/soapbox-pub/ditto) 是一款 Nostr 社交客户端，让用户选择自己的 relay 并向其认证。在 [2.42.3 版本](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3)中，帖子的“Event 详情”会显示哪些用户 relay 和作者 relay 存有该帖子；“广播”只会发送到缺失的 relay。该版本还会指出无响应的读取 relay 并提供重试控件，使缺失的帖子更容易诊断，而无需再次发送到所有地方。

[版本说明](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3)指出，切换账户后不再把帖子发送到上一个账户的 relay，被屏蔽的用户无法触发通用的手机提醒，帖子中的链接或图片也无法访问读者本地网络中的设备。来自较慢 relay 的帖子不再从“关注”和“喜爱”feed 中消失，而直播聊天和 webxdc 游戏的更新也不再反复下载整个视图。种子和音频浏览也是新功能，但 relay 路由和账户隔离才是对 Nostr 影响最广的变更。

### Iris Chat 2026.9.24.4 把通话带入加密对话 {#iris-chat-20269244-brings-calls-into-encrypted-conversations}

[Iris Chat](https://github.com/irislib/iris-chat-rs) 是一款端到端加密的 Nostr 通讯应用，使用 double-ratchet 系列聊天协议。其 [9 月 24 日的版本](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4)加入了与兼容联系人之间的语音和视频通话，包括在没有互联网时经由现有本地连接进行通话。用户可以降低视频质量、以语音方式接听视频通话，并通过 Android 的通话界面处理来电；接听或拒接也会让其他已关联设备停止响铃。

该[版本](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4)还让用户可以通过单独的签名应用登录，并查看哪些已关联设备处于连接状态。之后的 [9 月 24 日补丁](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.5)保留了延迟消息的原始时间戳，并改善了重连数据包丢失后的近距离投递。这些都是早期的跨设备和通话功能，因此该更新对能够运行兼容 Iris 版本的联系人最有用。

之后由开发者签名的 [9 月 30 日更新](https://primal.net/e/17fd3f325dda1feb0c1e51c6e1af0f7b3efe42ecff75e9527ac435cdc6a30c7a)会保留已移除成员的本地群组历史，同时禁止其发送消息，改善了已关联设备之间以及大型群组中的投递，并修复了已读标记和未读计数。通话加入了音频设备选择并恢复了呼出提示音；过时的麦克风状态不再使来电音频静音。定时静音、图片复制、拖放文件附件、通知路由和推送注册都获得了修复，而注销会清除本地缓存，移除设备会结束其会话。[第二次更新](https://primal.net/e/89ec93e25caf31831714e807c927b6d50d3d5fc38044df845163ff656db3f711)改善了对同一设备上其他 Iris 应用所缓存文件的访问，并在关闭 Nearby 时仍保留本地文件共享。

### LibreNostr 0.6.0–0.7.0 通过内置 Tor 路由 relay 流量 {#librenostr-060070-routes-relays-through-built-in-tor}

[LibreNostr](https://github.com/Lwb89dev/librenostr) 是一款 Android Nostr 客户端，提供可配置的 relay 和隐私设置。[0.6.0 版本](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.0)在 ARM64 上内置了基于 Arti 的 Tor 引擎，并将所选的直连、全部经由 Tor 或仅 `.onion` 模式应用于 relay WebSocket、HTTP 请求、媒体、上传和网页。严格 Tor 模式在 Tor 不可用时会以失败告终，绝不会悄悄直接发送请求；切换模式会通过新的路由重新连接 relay socket。

[0.6.2 版本](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.2)加入了一个基于公开关注列表构建、在设备端运行的信任网络过滤器，并根据补充 relay 能额外覆盖多少被关注者来选择它们。[0.7.0 版本](https://github.com/Lwb89dev/librenostr/releases/tag/v0.7.0)随后会在个人资料和计数查询完成之前就显示笔记和通知，限制慢速 relay 查询的时长，并且不再在每次打开对话时解密整个私信收件箱。这些版本合在一起，既改变了客户端可以连接的地方，也改变了慢速 relay 能拖住其界面的时间。

其由开发者签名的[首个稳定版本 1.0.0](https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927) 加入了可保存、按个人资料区分的平板多栏面板，各栏可移动，用于 feed、话题标签、个人资料、长文阅读、通知和消息。横屏平板会使用这一布局；手机保留现有界面。搜索新增了 OR、排除、媒体过滤和可用的日期范围，会先返回缓存的个人资料再进行 relay 细化，并在全文检索请求被拒绝时立即跳过。话题标签按时间顺序排列，分页会等待足够多的 relay 应答，未使用的 feed 会释放其订阅。

[同一版本](https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927)在编辑时会保留现有的公开和加密屏蔽列表及书签条目，而不是用一次修改替换它们。它在不同账户之间隔离书签和通知，并把辅助作者 relay 限制为公开读取，使私密请求和 relay 认证不会发往这些 relay。它还防止过时的个人资料应答覆盖较新的元数据，修复了通知分页和徽标，在新条目到达时保留较早的 feed 条目，并修复了回复撤销倒计时、重复发布、带查询字符串的媒体 URL，以及将聊天标为已读后的未读计数。[1.0.1 版本](https://primal.net/e/630becb73dbe7ba7c76a2d1970f1d7262a5afc33b02fc8002bef611cf638deab)修复了新布局中平板多栏面板的启动崩溃。

### Newlay 0.3.45 以流式方式返回大型 relay 查询而不是关闭连接 {#newlay-0345-streams-large-relay-queries-instead-of-closing-them}

[Newlay](https://code.relay.tools/opensauce/newlay) 是一个托管在 Android 上的 Nostr relay 及相关本地服务。其[已签名的 0.3.45 版本公告](https://primal.net/e/b8380ae1bf30492129727ec59e27e2ae8a4cf9ad08e7361826a9ba8be88a227a)指出，大型查询结果现在会以带背压的流式方式返回，而不是关闭客户端连接。内置的 Git 托管会在推送后清理被取代的 pack，而其 Cordn 加密消息协调器会接受超大的客户端请求，并在探测超时时发送中止帧。

该[版本](https://primal.net/e/b8380ae1bf30492129727ec59e27e2ae8a4cf9ad08e7361826a9ba8be88a227a)还为 Android 运营者提供了一张实时状态卡片，显示 event、存储、地址和管理信息，并针对 16 KB 内存页设备对齐了原生加密库。relay 和协调器的变更横跨自上一个商店版本 0.3.39 以来的多个版本；0.3.45 是它们的打包检查点。

### ngit-grasp 3.0.5 让 Git 推送和 relay 同步持续推进 {#ngit-grasp-305-keeps-git-pushes-and-relay-sync-moving}

[ngit-grasp](https://gitworkshop.dev/danconwaydev.com/ngit-grasp) 是一个自托管的 Nostr relay 和 Git 服务器，用于基于签名的仓库协作。其[已签名的 3.0.5 版本公告](https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41)把缓慢的历史协调移出共享的实时同步 actor，使 relay 订阅可以在检查较早 event 的同时开始。它会针对速率限制、不完整的历史查询、邮箱读取和身份查询分别进行退避，因此一个故障 relay 不再独占重试能力。

[同一版本](https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41)会对照本地 event 清单进行协调，以避免重新获取已存储的历史，并在把订阅覆盖范围视为已验证之前关闭不完整的订阅。在 Git 方面，它接受已由后台状态提升应用过的推送，为已变更的 ref 保留冲突保护，并在上传期间持续读取 Git 进度输出，以防推送停滞。这些细节很重要，因为一个仓库可能在 relay 上看起来已经上线，而其 Git 传输仍在等待权威结果。

### Armada 0.63.0 让推送提醒覆盖各类签名器 {#armada-0630-carries-push-alerts-across-signer-types}

[Armada](https://github.com/soapbox-pub/armada) 是一款面向加密社区、频道和私信的 Nostr 客户端。继上周的媒体隐私版本之后，其[已签名的 0.63.0 公告](https://primal.net/e/34021b55504d74c5d04f55dbfea87f31168a7c4582f35113d7ec063894d19e56)介绍了一条新的浏览器推送路径，在应用关闭时也能工作，适用于扩展和远程签名器登录以及其他账户类型。嵌入了 Armada 的宿主应用 Tenna 也为其用户加入了后台通知。

该[版本](https://primal.net/e/34021b55504d74c5d04f55dbfea87f31168a7c4582f35113d7ec063894d19e56)能更快地加载长社区频道中的较早消息，并避免为新消息重新读取整个历史。私信输入状态提示使用更少的 relay 连接。桌面端更新加入了重启提示，而不再支持从 0.50.0 之前的版本直接升级。

已签名的 [0.63.1 后续版本](https://primal.net/e/af3ff711c1c1daa4d6a621dc5add0615fc5d37fbb1de31395cb79dcdf820aaf1)加入了可编辑的表情包，支持文件夹导入和重新排序，可获取超出已加载历史的被引用消息，并让托管在 relay 上的回复可以互操作。它减少了 Android 的重连流量，在长时间断开后追赶进度而不重复旧提醒，排除加入之前的提及，并保留未编辑的群组字段和私密服务器列表条目。在 relay 托管的群组中，删除操作现在需要消息作者或管理员执行。服务器拖动、格式错误的 relay 信息处理和仓库订阅也获得了修复。

[0.63.2 版本](https://primal.net/e/ad0f6ad1a7730a400e8257c494c53ef14597c55a24e01b05dd2b2301c7d3aa36)把消息 Markdown 扩展到嵌套引用和列表、水平分隔线、代码块、下划线式标题，以及跨越链接或提及的格式。Tenor 和 Giphy 页面链接会以 GIF 形式播放。已读状态同步传输的数据更少，重连避免了冗余下载和登录，而 Android 后台通知会在大型设置更新涌入时暂停 relay 同步。

### deed 0.3.0–0.3.2 让 Zig 版 Nostr 发布更稳定 {#deed-030032-makes-zig-nostr-publishing-steadier}

[deed](https://github.com/zig-nostr/deed) 是一个用 Zig 编写、用于读取和发布 Nostr event 的命令行工具。其 [9 月 24 日的 0.3.2 版本](https://github.com/zig-nostr/deed/releases/tag/v0.3.2)加入了一项代理技能，并修复了 relay ping 的截止时间；之前的 [0.3.1](https://github.com/zig-nostr/deed/releases/tag/v0.3.1) 和 [0.3.0](https://github.com/zig-nostr/deed/releases/tag/v0.3.0) 版本改善了性能和发布可靠性。这三个 tag 描述的是同一个早期工具系列。对 Nostr 可见的好处是，使用该 CLI 的脚本获得了更稳定的 relay 连接和 event 发布路径。

### Cordn 0.5.1 在协调器故障时让其他群组照常运转 {#cordn-051-keeps-other-groups-moving-when-a-coordinator-fails}

[Cordn](https://github.com/Cordn-msg/cordn) 是一款 MLS 加密的群组通讯应用，使用 Nostr 身份和 relay 来定位对话协调器。其[已签名的 0.5.1 客户端版本](https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6)继上周的离线队列工作之后，将协调器调度与发件箱调度分离：一个不可用的协调器不再延迟无关群组的发送。解析出的 relay 提示在发现后会持久保存，群组文档会在设备之间携带这些提示，而一条持久的待发布记录会恢复被搁置的发送。多设备恢复在读取当前配置的同时，会并行执行历史链查询和缺口查询。

该[版本](https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6)还加入了拖放文件附件、置顶群组、预览和通知中的个人资料名称，以及协调器标签。它修复了首条未读消息定位、未读计数、重复提醒、媒体和系统消息预览、附在带说明文字媒体上的回复，以及图片缩放控件。原生下载使用“另存为”选择器。较晚出现的签名器不再引发错误的“不支持加密”警告，账户切换也不再与后台种子初始化产生竞争。

### Nymbot 1.0.7 加入本地文档处理和加密聊天分享 {#nymbot-107-adds-local-document-handling-and-encrypted-chat-sharing}

[Nymbot](https://zapstore.dev/apps/ai.nymbot) 是一个通过加密、gift-wrap 封装的 Nostr 消息访问的助手。其[由开发者签名的 1.0.7 版本](https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e)会在设备上读取文档，在文件过大无法整体发送时挑选相关段落，并标明所用的页面。对话可以通过端到端加密的链接分享，之后还可以撤回访问权限。Python 和 JavaScript 回复可以在本地运行，其输出会返回到对话中。

[同一版本](https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e)加入了带来源的研究功能（提交前会显示价格）、图片编辑、按消息选择模型，以及按聊天和按机器人设置的支出上限。通过 MCP 连接的外部工具在修改数据前会请求确认。仓库运行可以暂停变更以供审查，显示 CI 结果，并在网关繁忙后恢复。建议回复、置顶通知、折叠的来源列表和可搜索的模型选择器完善了这次更新；这些说法来自开发者的版本说明；Compass 尚未独立审计该应用的隐私性。

### 0xchat 1.5.6 发布其签名和消息认证修复 {#0xchat-156-ships-its-signing-and-message-authentication-fixes}

[0xchat](https://github.com/0xchat-app/0xchat-app-main) 是一款带有私聊、外部签名和钱包功能的 Nostr 通讯应用。[1.5.6 版本](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release)发布了[上周作为源代码合并报道的](/en/newsletters/2026-09-23-newsletter/#0xchat-merges-fixes-for-signing-message-authentication-and-redirect-flaws)安全修复，包括 gift-wrap 认证、受信任的基础设施配置，以及嵌入页面签名的用户同意。它还堵住了绕过 Tor 代理的路径，为非 onion 主机验证 TLS 证书，并阻止发布版本把可能敏感的凭据和钱包资料写入设备控制台。用户主动开启的开发者日志仍会记录错误。

该[版本](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release)让 relay 重连的退避时间从三秒逐步增加到五分钟，修复了重连后的订阅，并会投递在 relay 连接期间排队的请求。账户切换不再累积重复的 relay 监听器，登录失败会保留当前已激活的账户，外部签名器连接在每次启动之间保持。发送失败现在会显示错误，并保留未发送的文本或可恢复的代币分享状态。启动时的密钥解密和上传哈希计算移出了 UI 线程；聊天和视频缓存避免了重复渲染和下载。该版本提供带 SHA-256 校验和的 Android 和桌面资源，包括经 Play 签名的 Android APK 和从源代码构建的 Windows 安装程序。

### Nostr Mail Client 0.17.0 对 relay 隐藏邮箱操作 {#nostr-mail-client-0170-hides-mailbox-actions-from-relays}

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client) 通过 Nostr 收发邮件，同时支持传统的邮件投递。继[上周按收件人选择传输方式和媒体隐私的版本](/en/newsletters/2026-09-23-newsletter/#nostr-mail-client-0160-adds-per-recipient-delivery-choices)之后，[0.17.0 版本](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)对 relay 隐藏了已读、归档、文件夹和标签状态及其时间，并允许用户在不通知发件人的情况下删除邮件。该版本要求所有设备同时更新，因为旧客户端看不到新的状态或删除操作。它还在大于 32 KB 的邮件中保护密送收件人，避免本地联系人别名出现在发出的邮件中，修复了 Amber 二维码登录，并把公开邮件发布到收件人的读取 relay。

该[版本](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)加入了带颜色的文件夹和标签，并支持基于发件人、主题和附件的规则；回复和转发引用；内联粘贴的图片；附件预览和重命名；以及邮件列表中的范围选择。转发会保留原始图片和附件，回复引用默认折叠，网页编辑器也加入了上下文菜单。HTML 表格和内联图片的渲染更准确，纯文本链接可以点击，定时发送支持最远五年后的日期。通讯录中的名称和头像会出现在整个界面中，主题颜色提供系统、推荐或自定义配色。

[同一版本](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)将从文件中选择的背景保存在本地，并缓存通过链接设置的背景，但有一项明确的迁移代价：原生平台上旧的文件背景必须重新添加。它更改了默认的 relay 和媒体推荐，在引导流程和更新提示中加入 Nostr 应用发现，保留其他客户端写入的陌生设置，并修复了中断的邮件存储创建和 Linux 打包。启动失败现在会显示详细信息和预先填写好的报告，而不是空白屏幕。

### Nostr WoT 0.8.7 把认证绑定到目标地址 {#nostr-wot-087-binds-authentication-to-the-destination}

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) 是一款将 Nostr 签名与信任工具结合在一起的浏览器扩展。[0.8.7 版本](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)要求 [NIP-98](/zh/topics/nip-98/) 签名 HTTP 认证的用户同意必须针对确切的 URL、查询、方法、账户和请求来源。以前宽泛的批准需要重新征求同意。[NIP-42](/zh/topics/nip-42/) relay 认证拥有一套独立的、与账户绑定的权限系统，其中针对特定站点的拒绝优先于共享的 relay 允许。认证请求必须来自经过验证的顶层浏览器来源，而等待批准或解锁时会触发另一次账户和访问权限检查。

该[版本](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)会验证远程 [NIP-46](/zh/topics/nip-46/) 签名和完整的已批准 event，使返回的签名无法悄悄替换内容或目标地址。钱包开通和地址变更使用与请求体绑定的认证、一次性的后端挑战和独立的交易令牌；通用的网站签名无法铸造这些内部钱包令牌。兼容的后端必须先部署，客户端会拒绝降级到已停用的端点。Nostr Wallet Connect 支付也会根据所请求的发票哈希验证返回的支付原像，若不匹配则视为结果未知。

在[请求界面](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)中，用户可以查看完整的原始 event，在某个站点分组中选择特定请求，并在本地查看私信，而无需批准将其返回给网站。本地预览会在 30 秒后自动隐藏；新到的请求默认不勾选，普通的批量批准不包括认证请求。该扩展区分了按站点和对所有站点的 relay 授权，限制了经过验证的个人资料缓存规模，用较小的 event ID 来裁决时间戳相同的可替换 event，并让主弹窗的发布读取保持在本地。Chrome 和 Firefox 各自获得单独验证的软件包和串行化的稳定版提交工作流；这些工作流并不能证明当前已在商店上架。

### Iris 的共享运行时让 relay 和 peer 历史保持一致 {#iriss-shared-runtime-keeps-relay-and-peer-history-consistent}

[nostr-pubsub](https://github.com/mmalmi/nostr-pubsub) 提供一个共享的 Nostr event 运行时，带有持久化 event 存储和发出发布队列。[0.5.7–0.5.13 版本](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13)会批量处理精确订阅，在重连后重放这些订阅，区分本地、relay 和 peer 三类证据，并在持久存储失败时报告历史不完整。已完成的查询会等待每个已接收 event 完成准入。默认的 relay 批次现在最多包含 20 个 OR 过滤器，以兼容常见的服务器，而 peer 批次保留独立的匹配和取消。

[Hashtree 的运行时更新](https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13)用这一共享运行时、持久化 event 索引和发出队列取代了特定于 worker 的网络层，使 event 和缓存文件可以共用一个 FIPS 节点。[FIPS TypeScript 0.0.44–0.0.45](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.45) 会选择有足够容量承载完整信令记录的路由，在握手截止时间内恢复中断的会话建立，并且只在路由被明确拒绝后才重试 WebRTC 应答。更大的分帧 WebSocket 路由需要兼容的原生 peer；0.0.44 的说明要求先部署原生 FIPS 0.4.85。

[Iris Kit 0.2.5](https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.5) 加入了一个持久化的普通 event 应用客户端，以及与传输无关的 [NIP-46](/zh/topics/nip-46/) 签名，同时保留账户密钥和离线读取。[0.2.6 版本](https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.6)会立即从 worker 或原生后端返回已验证的完整 event ID；前缀查询和可替换 event 查询仍会等待历史后再选出最新值。这些都是库版本，其说明并不能证明已部署到每一个 Iris 应用。

[Iris Meet 9 月 30 日的源代码更新](https://github.com/irislib/meet/commit/9bebb074895fd34574c3a92056612cf3891de74b)用持久化的发布/订阅基础设施和共享身份签名器取代了其 NDK 集成。该补丁加入了针对离线身份恢复、NIP-07 签名和会议室隔离的测试覆盖。现有的[会议应用](https://github.com/irislib/meet)使用 Nostr 进行加密信令，使用 WebRTC 传输音频和视频。这是默认分支上的实现进展；该仓库没有带 tag 的版本能证明这一具体更新已上线到正式站点。

### Chama 传播挂单取消和后台提醒 {#chama-propagates-listing-cancellation-and-background-alerts}

[Chama](https://github.com/jesuspirate/chama) 使用签名 event 进行社区交易和私密对话。[6.4.14–6.4.16 版本](https://github.com/jesuspirate/chama/releases/tag/v6.4.16)会在本地删除挂单之前先发布一条已签名的取消，使其他客户端也能撤下同一条缓存的报价。接收方唤醒 tag 现在会随 event 一起发送，不再取决于发送方的通知设置，而提醒服务器会按签名 event 去重，因此紧接在加入之后的聊天仍能触发唤醒。后台任务会从保存的游标重放受影响的交易，隔离失败的链条，并在本地解密通知文本；该版本要求重新部署配套的监视程序。

[这组版本](https://github.com/jesuspirate/chama/releases/tag/v6.4.16)还会按签名 event 的时间应用参与者续期，隔离在席位过期后进行的资金锁定，并公开对已保存的不记名票据的恢复功能。领取的发布会等待导入或支付得到确认。挂单过滤器会在不同社区范围之间保留查看者的货币，交易标题使用最终确定的加入金额。这些变更让两个连接到 Nostr 的客户端从同一 event 历史中推断出的结果保持一致。

### Earthly 0.1.12 加入可复用的地图配置 {#earthly-0112-adds-reusable-map-configurations}

[Earthly](https://github.com/zeSchlausKwab/earthly) 是一款[基于 Nostr 的协作地图编辑器](https://github.com/zeSchlausKwab/earthly/blob/v0.1.12/README.md)，支持签名发布和加密分享。[0.1.12 版本](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.12)加入了面向公开 Google My Maps 的可复用 GMapper 配置、对开发者创建的 Maplet 的发现、私密配置存储或公开发布，以及附带出处的几何图形复制。同一版本还加入了加密连接分享、实体拖放和移动端聊天导航。导入受到 Google 导出可用性和浏览器 CORS 的限制，可执行的下载 Maplet 在 Tauri 中仍不可用，实体 Android 设备上的升级检查也尚未完成。

[配置相关工作](https://github.com/zeSchlausKwab/earthly/pull/29)迁移了现有的发布地址和偏好设置，并加入了对配置更新的审查或撤回。其最初的 Android 工作流在编译前就失败了；一项[工具修复](https://github.com/zeSchlausKwab/earthly/pull/30)为随后打上 tag 的版本做好了准备。

### Mostro 0.19.0 停用第一代传输 {#mostro-0190-retires-its-first-generation-transport}

[Mostro](https://github.com/MostroP2P/mostro) 通过 Nostr 协调点对点交易。[0.19.0 版本](https://github.com/MostroP2P/mostro/releases/tag/v0.19.0)现在正式发布了[第一代 gift-wrap 传输的移除](https://github.com/MostroP2P/mostro/pull/1004)，因此客户端必须使用较新的协议。现有的创建订单和发起争议的时间戳 tag 被[重命名为 `published_at`](https://github.com/MostroP2P/mostro/pull/1000)，但存储的值不变；外层 event 的 `created_at` 仍表示其签名时间。恢复响应会返回交易对手的交易密钥，已接受的创建/接单操作能识别交易密钥，relay 发布在收到第一个肯定的 relay 确认时即告完成。同一版本还更新了保证金截止时间和取消流程，在交易解决时关闭争议，通知仲裁者，并限制所转发价格的过期时长。

Mostro 的[交易密钥准入修复](https://github.com/MostroP2P/mostro/pull/1006)会在引入该密钥的订单或争议一经提交时就识别该密钥。首次联系工作量证明要求更严格的节点，此前可能会在周期性的已知密钥刷新之前丢弃一条合法的后续消息；默认门槛相同的节点不受影响。一项[争议事务](https://github.com/MostroP2P/mostro/pull/923)以原子方式提交订单状态转换和争议记录，消除了状态不一致的故障。[关闭通知](https://github.com/MostroP2P/mostro/pull/945)会在用户自行解决争议时，尽力向被指派的仲裁者发送一条私信，现有的可替换 event 仍作为离线后备。

### SCRUTINY Lens 把安全研究带到 Nostr 上 {#scrutiny-lens-brings-security-research-onto-nostr}

[SCRUTINY Lens v0.1.0](https://github.com/crocs-muni/scrutiny-lens/releases/tag/v0.1.0) 于 9 月 29 日发布了首个公开版本，它是一个用于浏览通过 Nostr 发布的安全元数据的浏览器客户端。分析人员可以按 CVE、软件包或证书标识符搜索，查看 event 历史和撤回记录，并在主题图谱中探索关联关系。浏览器会验证 event 签名和标识符。可选的 AI 搜索和解释使用用户自行选择的端点；应用会对照底层 event 核对被引用的出处。[版本说明](https://github.com/crocs-muni/scrutiny-lens/releases/tag/v0.1.0)明确说明了 relay 方面的局限，并指出本地构建仍依赖相邻的仓库。

### Mangatsu 和 Noteds 登陆 Android {#mangatsu-and-noteds-reach-android}

[Mangatsu v0.1.11](https://github.com/imattau/Mangatsu/releases/tag/v0.1.11) 属于这款漫画阅读与发布应用本周推出的首个 Android 版本系列。其[源代码](https://github.com/imattau/Mangatsu/commit/543d6d3dde3bffe293b7336d0fb6f4c82532fe13)通过 [NIP-55](/zh/topics/nip-55/) 加入了 Amber 登录；NIP-55 是 Android 上请求外部签名器批准 Nostr 操作的接口。漫画和章节都是 Nostr event，页面则存放在 Blossom 服务器上；阅读器还支持加密的已保存书库和离线阅读。后续的 commit 处理了签名器调用和 relay 列表刷新。

[Noteds v0.1.2](https://github.com/imattau/noteds/releases/tag/v0.1.2) 通过 Tauri 把一个 Nostr 分类信息市场带到 Android。其 [Android 签名器集成](https://github.com/imattau/noteds/commit/c9294999134196e9d98c011440c7ca0ed5fcc398)使用 Android NIP-55 签名。该应用通过 Nostr 发布挂单和消息，并构建一个包含类别、地理区域和可选浏览器嵌入向量的本地搜索图谱。最新的源代码修复了附近搜索所需的原生位置访问。两个项目都是早期版本；它们的 GitHub 版本页面没有详细说明，因此这些功能来自带 tag 的 README 和实现 commit。

### Statim 把 Nostr 私信与其他网络结合在一起 {#statim-combines-nostr-dms-with-other-networks}

[Statim v0.4.0](https://github.com/alaibe/statim/releases/tag/v0.4.0) 紧随其 9 月 23 日的首个版本发布。[带 tag 的源代码](https://github.com/alaibe/statim/blob/v0.4.0/README.md)描述了一款通讯应用，同时支持 NIP-17 Nostr 私信以及 XMTP、Status、Telegram 和 Matrix。账户从本地保存的恢复短语开始；每个对话都会标明其协议，因为这些网络提供的隐私特性各不相同。Android 版目前缺少 Telegram 集成。这些是该项目文档中记载的功能，而不是经过独立测试的保证，也不能确认已在应用商店上架。

## 开发中 {#in-development}

### Amethyst 修复加密群组互操作性 {#amethyst-repairs-encrypted-group-interoperability}

[Amethyst](https://github.com/vitorpamplona/amethyst) 是一款支持 Marmot 加密群组的 Android Nostr 客户端。White Noise 是另一款 Marmot 通讯应用；一批[与其客户端一起测试的互操作性修复](https://github.com/vitorpamplona/amethyst/pull/4245)处理了群组管理、删除提示措辞，以及两款客户端共处同一对话时暴露出的其他行为问题。更有针对性的修复会[在 Marmot 群组内部发送回应和删除](https://github.com/vitorpamplona/amethyst/pull/4233)，而不是作为单独的 [NIP-17](/zh/topics/nip-17/) gift-wrap 私信发送，并会[在重启后应用来自其他客户端的编辑](https://github.com/vitorpamplona/amethyst/pull/4240)。这些都是源代码合并；PR 中描述的测试范围比已发布的跨客户端版本要窄。

另一项 [Cordn 群组运行时与界面合并](https://github.com/vitorpamplona/amethyst/pull/4201)通过协调器服务器加入了另一条加密群组路径。Cordn 与 Marmot 是不同的协议，因此不应把这两项变更理解为同一次传输迁移。

Amethyst 还合并了[其 Geode relay 和 Quartz 客户端中的 HTTP relay 命令](https://github.com/vitorpamplona/amethyst/pull/4231)（基于其 [NIP-FE](/zh/topics/nip-fe/) 提案），以及一个针对可替换个人资料和列表 event 的[备份冲突审查界面](https://github.com/vitorpamplona/amethyst/pull/4174)。NIP-FE 是项目自己的提案用语；备份流程让用户在接受替换之前比较各个版本，并防止本地状态被悄悄覆盖。

Amethyst 还在开发 Concord，这是 Armada 和 Accordion 所使用的另一种加密社区协议。一批[一致性修复](https://github.com/vitorpamplona/amethyst/pull/4262)加入了分片的社区列表、置顶证明、密钥轮换和解散记录，随后又加入了[阅后即焚消息和直接邀请](https://github.com/vitorpamplona/amethyst/pull/4264)。邀请在被接受之前会一直留在私密收件箱中；接收邀请不会联系社区的 relay。同一变更还修正了一处作者比较错误，该错误可能让另一位作者的删除操作移除某条消息。[跨客户端修复](https://github.com/vitorpamplona/amethyst/pull/4265)修复了未签名 rumor 的序列化、缺失的邀请字段、经 relay 确认的社区创建，以及无需重启即可加入；其报告的模拟器测试有在线的 Armada 和 Accordion peer 参与。

之后的一项[私有频道实现](https://github.com/vitorpamplona/amethyst/pull/4277)会在相关访问权限被撤销后轮换频道密钥，并加入创建、设为私有、设为公开和重新生成密钥的控件。它还加入了经过等级检查的协作式踢出，并让消息附件随其父消息一同过期。WebXDC 更新可以进入单独的频道缓冲区，但 Amethyst 仍没有 WebXDC 应用宿主。这批后续变更报告的是线路格式测试和单元测试，没有在设备或在线 relay 上进行验证，因此先前的互操作性结果并不能为每一个新增控件背书。

Quartz 的 MLS 引擎现在会[在重启后保留被跳过的消息代际密钥](https://github.com/vitorpamplona/amethyst/pull/4271)，使乱序消息在恢复已保存状态后仍可解密。[保留四个之前的 epoch](https://github.com/vitorpamplona/amethyst/pull/4272) 让调用方可以认证迟到的应用消息，保留其已认证数据，并防止已消费的代际再次被打开。一项[秘密树更新](https://github.com/vitorpamplona/amethyst/pull/4275)会从 ts-mls 风格的状态中加载未展开的节点密钥；[按发送者区分的过期代际错误](https://github.com/vitorpamplona/amethyst/pull/4270)能区分客户端自身的 ratchet 冲突和其他成员的重放。该 PR 明确指出，Marmot 现有的保留 epoch 后备机制仍是独立的，因此这是一项引擎能力，而不能证明 Amethyst 的每条消息路径都使用了它。

一次 [Quartz tag 读取器审计](https://github.com/vitorpamplona/amethyst/pull/4267)修复了私密 geohash 条目可能以明文发布的问题，以及一个把 `nsec` 中的私钥当作公钥处理的解析器。它还修复了转发地址、频道隐藏目标、直播间根 tag 和可寻址的铸造 event。过时的 `ForkTag` 读取器被移除，这对 Quartz 的使用者来说是一项源代码 API 变更；原有的 SQLite 铸造记录仍需单独迁移。[新增的 event 模型](https://github.com/vitorpamplona/amethyst/pull/4282)涵盖了 Buzz 的项目容器、工件修订和团队提案，而[视频观看和加密推送控制模型](https://github.com/vitorpamplona/amethyst/pull/4266)遵循 Divine 的 schema；这些新增内容确立了解析和构造支持，而不是完整的客户端界面或已被采纳的编号 NIP。

该客户端还会在 Android 14 或更高版本的 feed 和全屏查看器中[渲染 Ultra HDR 照片](https://github.com/vitorpamplona/amethyst/pull/4284)。Android 15 及更高版本把 feed 的亮度提升限制在普通范围的两倍，而全屏模式可以使用显示屏的完整范围；报告中的测试设备运行的是更新的 Android API，Android 14 和 15 尚未测试。一项[共享 UI 和上传端口合并](https://github.com/vitorpamplona/amethyst/pull/4278)把 140 个界面迁移到通用的 Android/桌面代码上，并把 Android 的媒体处理移出 UI 线程。其审计还恢复了元数据移除的错误报告，因此这次重构不只是文件搬移。

### Divine 为私信加入加密视频 {#divine-adds-encrypted-video-to-direct-messages}

[Divine](https://github.com/divinevideo/divine-mobile) 是一款 Nostr 视频客户端。[NIP-17](/zh/topics/nip-17/) 把私信装在加密的 gift wrap 中传送，向 relay 隐藏发送者。Divine 的[已合并视频消息工作](https://github.com/divinevideo/divine-mobile/pull/9486)会在设备上加密附带的视频，上传密文，并在该私信内发送解密密钥。接收方可以验证并解密该文件以便播放或保存。另一项[历史恢复修复](https://github.com/divinevideo/divine-mobile/pull/9446)避免在其他 relay 仍可应答时，因某个 relay 含糊的拒绝而过早结束恢复。

Divine 的[已停用审核密钥修复](https://github.com/divinevideo/divine-mobile/pull/9603)在解析审核标签时拒绝已停用的密钥，并在提交举报时选择当前的举报接收方。发往已停用密钥的待处理举报会被重定向到该构建中固定的密钥，无法解析的对话保持不可写。该变更在决定未成年人可以阅读哪些历史讨论串时，还会区分已停用密钥的保管情况；保管信息的更新仍需要发布应用版本。[已删除评论的缓存处理](https://github.com/divinevideo/divine-mobile/pull/9677)防止已成功删除的近期评论在讨论串重新加载时再次出现。

对于创作者，一种[实时色彩遮罩录制模式](https://github.com/divinevideo/divine-mobile/pull/9598)会在录制前预览替换后的背景，而[白墙遮罩](https://github.com/divinevideo/divine-mobile/pull/9701)通过视频插件加入了对亮度敏感的遮罩。[逐词字幕](https://github.com/divinevideo/divine-mobile/pull/9652)会保留识别出的单词时间，当服务器只提供整句字幕时则使用近似时间。[定格动画续拍](https://github.com/divinevideo/divine-mobile/pull/9698)会按现有作品的节奏追加新的静帧，而[找回分离的片段](https://github.com/divinevideo/divine-mobile/pull/9645)、[分组的字体选择](https://github.com/divinevideo/divine-mobile/pull/9654)和[速度预设](https://github.com/divinevideo/divine-mobile/pull/9601)加入了编辑控件，同时不改变 Nostr event 格式。

[方形导出对齐](https://github.com/divinevideo/divine-mobile/pull/9694)及其[针对较小片段的后续修复](https://github.com/divinevideo/divine-mobile/pull/9703)让文字和贴纸在不同分辨率的片段之间保持原位。[第三方 HLS 播放](https://github.com/divinevideo/divine-mobile/pull/9664)通过在循环边界回跳，而不是预缓冲重复导入的播放列表，避免了 Android 堆内存崩溃；这些循环每次重新开始时可能会短暂停顿。一项[账户偏好重新加载](https://github.com/divinevideo/divine-mobile/pull/9680)让与账户绑定的过滤器在切换账户时保持默认值，同时修复了调试登录断言的一部分问题。另一个审核标签刷新问题仍未解决，因此该 PR 并未声称所有登录错误都已修复。

### Buzz 扩展其 relay 的频道和身份控制 {#buzz-extends-its-relays-channel-and-identity-controls}

[Buzz](https://github.com/block/buzz) 是一个基于 Nostr 的工作空间，拥有自己的 relay 和客户端。其[已合并的频道工件实现](https://github.com/block/buzz/pull/7919)为一条可编辑记录指定唯一的所属频道和一条修订链；相互冲突的编辑不可能同时成为头部。该项目的 [NIP-AR](/zh/topics/nip-ar/) 标签指的是其自己的提案和实现，而不是既定的 Nostr 标准。

针对受保护的 HTTP 入口，另一项[已合并的变更](https://github.com/block/buzz/pull/7264)把联合身份断言与由 [NIP-98](/zh/topics/nip-98/) 授权证明的同一密钥配对。NIP-98 定义了签名的 HTTP 认证 event；Buzz 的 [NIP-FI](/zh/topics/nip-fi/) 断言是一项项目规范。它还合并了[用于私钥备份信封的 HPKE 加密](https://github.com/block/buzz/pull/7849)。该 PR 确立的是源代码层面的安全工作；是否已分发到每个客户端仍未得到验证。

[Buzz 桌面版 0.5.26](https://github.com/block/buzz/releases/tag/desktop-v0.5.26) 包含频道工件工作、原生的 HPKE 私钥备份加密，以及一个桌面端 relay 管理控制台。其共享变更修复了未列出项目频道的请求，在设备之间同步侧边栏分区、排序、星标和静音，限制长讨论串的读取范围，并收紧了 Blossom 身份断言。[仓库范围的说明](https://github.com/block/buzz/releases/tag/desktop-v0.5.26)另外列出了 relay 身份配对、伴侣应用的提及投递、可配置的推送 URL、原子化的管理删除，以及移动端的上下文名称。桌面版本确立的是桌面/共享部分的分发；并不能证明这些移动端变更已在移动版本中发布。

Buzz 的 [WebSocket NIP-FI 强制执行](https://github.com/block/buzz/pull/7224)会在接受帧之前检查联合身份断言，然后要求其 Nostr 密钥与通过 [NIP-42](/zh/topics/nip-42/) 认证的密钥一致；NIP-42 用于向 relay 证明客户端的身份。会话会在令牌到期、断言最长有效期和所配置的连接生命周期三者中最早的时间点过期；过期后不再接受任何新的操作。这一项目专属的 NIP-FI 模式默认关闭。已被接受的音频提交和订阅建立仍可能卡在停滞的依赖上，因此该变更并不能保证一个普遍有上限的断开时间。

[所有者删除准备](https://github.com/block/buzz/pull/7830)让运营者证明过的请求经由与清单绑定的自动批准，进入现有的删除执行器。一项 [relay 后续变更](https://github.com/block/buzz/pull/7969)让重试同一请求时返回其当前状态，并在删除完成前保留所有者的活跃配额；永久保留的宿主墓碑记录会计入 20 个社区的终身上限。这些是源代码层面的管理变更，该后续变更也提示运营者，在其 relay 和清空执行器上线之前保持删除功能关闭。另外，一项[分区目录审计](https://github.com/block/buzz/pull/6515)会在创建新的 event 和投递日志分区之前，检测兜底分区和未覆盖的月份，让运营者能够了解服务安全性和审计新鲜度。

Buzz 移动版现在能区分显示名称相同的人和代理。其[身份名称解析器](https://github.com/block/buzz/pull/7894)会用所有者来限定代理，并仅在必要时添加简短的密钥后缀；[对话集成](https://github.com/block/buzz/pull/7895)在作者、提及和成员通知中使用这些名称。[列表、搜索和 Pulse](https://github.com/block/buzz/pull/7896) 在对话之外也实现了同样的行为。这种可见的限定改变的是本地标签，而被选中的提及仍保留该身份原始的线路名称。

### Conduit 在 relay 接受后推进结账流程 {#conduit-advances-checkout-after-relay-acceptance}

[Conduit](https://github.com/Conduit-BTC/conduit-mono) 是一个向商家发送私密订单消息的 Nostr 市场。[渐进式 relay 发布](https://github.com/Conduit-BTC/conduit-mono/pull/483)区分了第一个肯定的 relay 确认和所有 relay 尝试的完成，而一项[结账后续变更](https://github.com/Conduit-BTC/conduit-mono/pull/488)会在继续之前持久保存第一个确认。relay 接受只说明已签名的订单到达了某个 relay；并不能证明商家已经读取或完成了它。

Conduit 还合并了[可恢复的远程签名器会话](https://github.com/Conduit-BTC/conduit-mono/pull/529)和[事务化的签名器 relay 协商](https://github.com/Conduit-BTC/conduit-mono/pull/533)。[NIP-46](/zh/topics/nip-46/) 让应用可以向单独签名器所持有的密钥请求签名；这些变更在传输修复期间保留用户的账户工作区，然后在恢复之前验证确切的账户。这些 PR 确立的是源代码行为，而不是已发布的结账版本。

Conduit 的[排序商品搜索合并](https://github.com/Conduit-BTC/conduit-mono/pull/575)会针对 kind 30402 商品发送一个普通的 [NIP-50](/zh/topics/nip-50/) 全文搜索查询，并在签名检查、修订协调和本地资格过滤的整个过程中保留 relay 给出的相关性排序。卡片可以在精确商品的后台读取完成之前显示，而较新的已签名删除仍具有权威性。“刷新”和“重试”只作用于搜索和精确商品读取，而不会启动大范围的目录发现。100 条结果的上限再加上本地过滤可能会漏掉符合条件的匹配项，因此部分为空的响应会提供恢复选项，并不能证明没有商品。

### Elisym 构建 Nostr 商务结账流程 {#elisym-builds-a-nostr-commerce-checkout}

[Elisym](https://github.com/elisymlabs/elisym) 正在开发一套商务工具包，用于签署商品，并通过 Nostr 传送私密的订单和收据消息。其[已合并的商务软件包](https://github.com/elisymlabs/elisym/pull/120)定义了报价验证和 gift-wrap 封装的订单 event；一个[结账界面](https://github.com/elisymlabs/elisym/pull/131)负责报价审查、钱包支付和投递状态，而一个[自托管的商家节点](https://github.com/elisymlabs/elisym/pull/133)打包了店铺一侧的功能。该项目称 kind `30490` 为临时编号，并描述了一个十月的最小可用版本。这些源代码合并确立的是一个正在形成的集成；尚未证明存在被接受的 Nostr 商务标准或完整的公开上线。

Elisym 的[代理结账工具](https://github.com/elisymlabs/elisym/pull/136)为其在 Nostr 上发布的商品加入了 `buy_product` 和 `get_order`。第一次调用只返回报价而不下单，第二次调用会接受同一代理和网络下的一次性报价及警告；订单状态持久保存在代理的本地文件后端中。[Tempo 结账支持](https://github.com/elisymlabs/elisym/pull/137)加入了一条浏览器钱包支付路径，包含商家验证和投递。已发送的交易哈希会让该次尝试保持有效，直到其结果得到确认，从而避免在广播仍可能结算时给出未支付的结果。

一项[之后的结账修复](https://github.com/elisymlabs/elisym/pull/139)让签名商品结账在浏览器钱包于发现过程中立即宣告自身时也能完成初始化。该源代码变更把会话声明移到了该回调可能运行之前；仅凭这次合并并不能验证托管部署。

### nostter 改进签名器检查和 event 获取 {#nostter-improves-signer-checks-and-event-retrieval}

[nostter](https://github.com/SnowCait/nostter) 是一款 Nostr 社交客户端。其[已合并的签名器能力变更](https://github.com/SnowCait/nostter/pull/2573)会在提供关注和回应操作之前，先确认是否存在可用的签名器。[新的置顶 tag](https://github.com/SnowCait/nostter/pull/2611) 携带作者的密钥和一个已知的 relay 提示，而不会去猜测，[可替换 event 的缓存排序](https://github.com/SnowCait/nostter/pull/2608)遵循 [NIP-01](/zh/topics/nip-01/) 的时间戳和 event ID 决胜规则。NIP-01 定义了 Nostr event 的核心规则，包括客户端如何在可替换 event 之间做出选择。

### Pensieve 为隔离的存档协调做准备 {#pensieve-prepares-isolated-archive-reconciliation}

[Pensieve](https://github.com/andotherstuff/pensieve) 是一款 Nostr 存档与恢复工具。其[已合并的隔离 negentropy 运行时](https://github.com/andotherstuff/pensieve/pull/60)为同步提供了一个有资源上限的 worker 和持久化的完成行为。该功能需要主动启用，PR 也明确说明没有激活任何生产服务或配置；这是为更安全的恢复路径所做的基础工作，而不是正在运行的部署的证据。

### ContextVM 避免跨 relay 的重复调用 {#contextvm-avoids-duplicate-calls-across-relays}

[ContextVM 的 TypeScript SDK](https://github.com/ContextVM/sdk) 以 Nostr event 承载工具和资源请求。其[已合并的入站去重修复](https://github.com/ContextVM/sdk/pull/103)即使在多个 relay 或一次重连再次投递同一明文请求时，也会按 event ID 将其识别为同一请求，与现有的封装消息路径保持一致。该 PR 报告称，修复之前一次调用曾导致一个非幂等工具运行了三次。一项配套的[资源通知变更](https://github.com/ContextVM/sdk/pull/101)只向已订阅的客户端发送更新；未订阅的已初始化会话不再收到这些更新。

### Cyberspace 修订 DECK-0003 对象规则 {#cyberspace-revises-the-deck-0003-object-rules}

[Cyberspace](https://github.com/arkin0x/cyberspace) 开发了 DECK-0003 格式，用于结构化 Nostr 对象和加密区域包，Amethyst 已在上周那期中提到开始实现该格式。新的[部件与隐藏对象规则](https://github.com/arkin0x/cyberspace/pull/36)和[包引用](https://github.com/arkin0x/cyberspace/pull/38)让一个包可以引用单独发布的对象，而不必嵌入每个部件。之后的一项[更正](https://github.com/arkin0x/cyberspace/pull/40)指出，event ID 引用无法可靠地固定可寻址 event 的旧版本，因为 relay 可能在其被替换后将其丢弃。读者应使用更正后的坐标引用规则；之前那次合并中的措辞已被取代。

### Wisp 修复对 Nostr 评论的回复 {#wisp-fixes-replies-to-nostr-comments}

[Wisp](https://github.com/barrydeen/wisp) 是一款具备 relay 路由和钱包功能的 Nostr 客户端。继上周发布的 [NIP-22](/zh/topics/nip-22/) 评论支持之后，一项[已合并的后续变更](https://github.com/barrydeen/wisp/pull/667)让对 NIP-22 评论的回复本身也成为评论 event，并带有正确的父级和根引用；之前的路径总是发布一条普通笔记。NIP-22 让评论可以附加到多种 Nostr 内容类型上。该修复是在 Wisp 的 1.2.5 tag 之后合并的，而那个 tag 的说明只是升级了版本号，因此这是源代码层面的进展，其发布情况尚未得到验证。

### Cordn 把协调器位置发送到第二台设备 {#cordn-sends-coordinator-locations-to-a-second-device}

[Cordn](https://github.com/Cordn-msg/cordn) 通过 Nostr 协调加密群组消息。其[已合并的多设备规范变更](https://github.com/Cordn-msg/cordn/pull/9)在复制的群组文档中携带群组的协调器 relay 提示。这样，新初始化的设备就能找到不在默认 relay 中的协调器，而不会出现看似已加入群组、却无法获取其积压消息和实时消息的情况。这是继上周 Cordn 离线队列版本之后的协议文档工作，而不是新的客户端版本。

### Nostr Atlas 推出可核验身份的目录 {#nostr-atlas-opens-a-directory-for-checkable-identities}

[Nostr Atlas](https://nostr-atlas.web.app) 是一个新的目录，把 Nostr 个人资料与其关联外部账户的声明一并展示。其[已合并的站点发布](https://github.com/saiy2k/nostr-components/pull/148)把该目录与项目的组件演示分离开来，站点也已公开响应。一项[声明流程合并](https://github.com/saiy2k/nostr-components/pull/144)让 X 账户的所有者可以用浏览器签名器发布一条已签名的 [NIP-39](/zh/topics/nip-39/) 证明，而[个人资料补全](https://github.com/saiy2k/nostr-components/pull/146)只有在证明通过验证后才会读取 kind-0 Nostr 元数据。NIP-39 定义了把 Nostr 密钥与另一个在线身份关联起来的证明模式；仅有 relay 确认并不会把一条声明标记为已验证。

### nostr-java 加入媒体托管工具并保留 tag 位置 {#nostr-java-adds-media-hosting-tools-and-preserves-tag-positions}

[nostr-java](https://github.com/tcheeric/nostr-java) 是一个面向 Nostr 应用的 Java 库和 MCP 工具集。其[已合并的 Blossom 工具](https://github.com/tcheeric/nostr-java/pull/557)让调用方可以上传、查找、列出和删除以哈希寻址的媒体，并管理用户的服务器列表。另一项[发布修复](https://github.com/tcheeric/nostr-java/pull/558)让空的 tag 值保留在原位：Nostr tag 是按位置解析的，因此丢弃一个空的 relay 提示可能会使某个标记移到错误的字段，导致发布的 event 与已批准的预览不一致。

### Zap Cooking 改变账户历史的恢复方式 {#zap-cooking-changes-how-account-history-can-be-recovered}

[Zap Cooking](https://github.com/zapcooking/frontend) 是一款分享食谱的 Nostr 客户端。其[已合并的 Lazarus 恢复工作](https://github.com/zapcooking/frontend/pull/753)用一种新方法取代了基于 [NIP-78](/zh/topics/nip-78/) 应用专属数据 event 的备份，新方法会扫描 relay 保留的可替换 event 版本，以检测被覆盖的关注、屏蔽或个人资料。Lazarus 仍是一项草案协议；恢复依赖于保留了旧版本的 relay，而一个已合并的网页客户端 PR 并不能保证每个丢失的 event 都能被恢复。

该客户端还合并了针对笔记和回复的[可选 NIP-13 工作量证明控件](https://github.com/zapcooking/frontend/pull/743)，以及一个[附件模型](https://github.com/zapcooking/frontend/pull/752)，让媒体顺序和 [NIP-92](/zh/topics/nip-92/) 描述在预览和发布之间保持一致。[NIP-13](/zh/topics/nip-13/) 让发送者在发帖前为 event 花费本地计算量；NIP-92 以 event tag 承载媒体元数据。

Zap Cooking 的 [NIP-05 名称领取修复](https://github.com/zapcooking/frontend/pull/763)要求对确切的请求体进行 [NIP-98](/zh/topics/nip-98/) 授权，并拒绝与领取该名称的公钥不同的签名者。此前，该公共端点会接受未经认证的领取请求，这些请求可能替换其他成员的名称。会员等级现在来自现有的会员记录，使用远程签名器的用户在领取时会收到签名提示。单独的、受信任的服务器端注册路径保持不变。

一项[屏蔽列表修复](https://github.com/zapcooking/frontend/pull/764)阻止个人资料页的屏蔽操作用仅含公钥 tag 的列表替换整个 kind 10000 列表。之前的路径会抹掉词语、话题标签和讨论串条目以及加密内容，而且有一处界面可能把解密后的私密屏蔽密钥公开重新发布。新路径会读取 relay 上的副本，保留无关的 tag 和密文，并在无法读取时拒绝发布。移除私密屏蔽需要通过签名器解密并重新加密。

### Opal 把远程签名带到 Omarchy {#opal-brings-remote-signing-to-omarchy}

[Opal](https://github.com/derekross/opal) 是为 Omarchy Linux 环境打造的桌面 Nostr 签名器。其 [9 月 28 日的 0.3.3 版本](https://github.com/derekross/opal/releases/tag/v0.3.3)继首个公开系列之后，加入了 [NIP-46](/zh/topics/nip-46/) 远程签名支持、本地密钥环，以及针对已连接应用请求的权限界面。NIP-46 让账户密钥留在签名器中，由单独的客户端请求它批准操作。这是一款特定平台签名器的早期版本，并不代表支持更广泛的桌面环境。

### WatchTower 推出 NIP-86 relay 控制面板 {#watchtower-opens-a-nip-86-relay-control-panel}

[WatchTower](https://github.com/iqbqioza/watchtower) 是一个新发布的面板，通过 NIP-86 管理 relay；NIP-86 是用于经过认证的 relay 管理请求的协议。一个[公开实例](https://watchtower.nostrfy.org)已可访问，为运营者提供了查看该界面的地方。该仓库创建于 9 月 22 日；站点可以访问，并不能证明其授权流程已经过独立审计，也不能证明它能与所有 relay 实现配合使用。

### Hubstr Blossom 提供个人媒体源站 {#hubstr-blossom-opens-a-personal-media-origin}

新发布的 [Hubstr Blossom 服务器](https://github.com/johninnis/hubstr-blossom)让 Nostr 客户端可以把图片、视频和文件上传到自托管的 Blossom 端点，然后把这些 URL 放进 event 中。其 README 记录了基于内容哈希的本地存储、SQLite 索引、用于变更操作的已签名 kind-24242 授权，以及一系列用于上传、镜像、列表和删除的 Blossom 操作。公开读取让其他客户端可以渲染已发布的媒体，而无需获得上传权限。

该[服务器文档中的选项](https://github.com/johninnis/hubstr-blossom)还会为 [NIP-94](/zh/topics/nip-94/) event 提取文件元数据，这类 event 用于描述共享的媒体。服务器可以重新编码图片以去除 EXIF 元数据，并默认防止镜像请求指向私有网络目标。这是一个附带部署说明的新发布实现，并不能证明已有广泛的生产部署。

[Hubstr Relay](https://github.com/johninnis/hubstr-relay) 于 9 月 24 日发布了初始源代码。它把个人 SQLite event 缓存与公共 relay 结合在一起：未认证的读取者可以看到允许公开的 event，而通过 NIP-42 认证的租户可以读取自己的缓存。访客读取者仍无法获取 NIP-17 gift wrap。其 [9 月 25 日的更新](https://github.com/johninnis/hubstr-relay/commit/0ae1a551ac50da0b7097105b76591dbc4d6cc023)修正了 NIP-86 公钥列表方法返回的记录。

### Meshstr 试验无需许可的 relay 网状网络 {#meshstr-experiments-with-a-permissionless-relay-mesh}

[Meshstr](https://gitlab.pocketlabs.dev/meshstr/meshstr) 是一个处于 alpha 阶段的设计，让 Nostr relay 协商 peer 预算并交换已签名的用量收据。其首个实现包括 9 月 27 日加入的[面向 Nostr relay strfry 的写入策略桥接](https://gitlab.pocketlabs.dev/meshstr/meshstr/-/commit/6d609fc99f)，第二天又修复了一个 socket 问题。该仓库描述了 DIDComm 协商和 [NIP-77](/zh/topics/nip-77/) 协调（让 peer 无需交换完整清单即可比较 event 集合），以及关于 peer 超出约定预算的可验证报告。

这些[项目规则](https://gitlab.pocketlabs.dev/meshstr/meshstr)只是一项提案，而不是已被采纳的 NIP 或经过验证的公共 relay 网络。本周的具体进展是已发布的代码路径，它把 relay 的写入策略与拟议的网状网络计量连接起来。

### Dossier 展示公开的 Nostr 历史可能泄露什么 {#dossier-shows-what-a-public-nostr-history-can-reveal}

[Dossier](https://github.com/satanrayshe/dossier) 是一款新的浏览器端自我审计工具，用于检查个人的 Nostr 和 Lightning 足迹，并提供[公开演示](https://satanrayshe.github.io/dossier/)。它会收集可见的个人资料链接、zap 轨迹、发帖时间、旧 [NIP-04](/zh/topics/nip-04/) 加密私信的元数据，以及照片 EXIF 等媒体元数据；它还能显示某个 relay 是否仍在提供用户试图删除的 event。[NIP-07](/zh/topics/nip-07/) 签名器支持让用户无需把私钥粘贴到页面中即可授权清理操作。

该项目[文档中说明的局限](https://github.com/satanrayshe/dossier)很重要：一次扫描只能看到它所连接的 relay，删除请求也无法抹去保存在其他地方的副本。该仓库出现于 9 月 27 日，还没有带 tag 的版本；演示和源代码确立的是一个早期工具，而不是任何人过往活动的完整清单。

### Marmot MDK 扩展投票、自定义表情和账户元数据 {#marmot-mdk-extends-polls-custom-emoji-and-account-metadata}

[Marmot MDK](https://github.com/marmot-protocol/mdk) 为加密 Nostr 群组消息提供运行时和绑定。之后的 MDK 源代码合并公开了[分页的逐个投票者选择](https://github.com/marmot-protocol/mdk/pull/2094)，其使用的有效回应规则与汇总计票相同。[可选的、由应用拥有的群组组件](https://github.com/marmot-protocol/mdk/pull/1929)为宿主提供由管理员控制的设置，这些设置在消息保留策略下得以保存，并通过 Welcome 传达给新成员。[带 tag 的发送和媒体回应](https://github.com/marmot-protocol/mdk/pull/2105)在运行时和绑定中携带自定义表情元数据，在 epoch 变更后保留附带回应图片的解密材料，并拒绝伪造的附件 tag。该变更扩展了 C 语言的上传请求结构，因此 C 使用者必须根据头文件重新构建。

一项[收敛修正](https://github.com/marmot-protocol/mdk/pull/2093)在未选出规范分支时让消息保持待处理状态，而不是在未尝试当前状态的情况下就将其作废。配套的[不可达路径清理](https://github.com/marmot-protocol/mdk/pull/2095)把未解决的暂存 commit 导入保留的重试行为。[加密媒体读取](https://github.com/marmot-protocol/mdk/pull/2097)让 HTTP 读取超时与可续传正文的空闲处理保持一致，以解决大文件传输停滞的问题，但并不声称尚待进行的传入 APK 设备验收测试已经通过。[启动阶段标记](https://github.com/marmot-protocol/mdk/pull/2098)会显示账户打开过程中是哪一步超时，增加了诊断证据，但并不声称底层的启动停滞已经解决。

本地代理连接器在发布 kind 0 更新时也会[合并现有的个人资料元数据](https://github.com/marmot-protocol/mdk/pull/1969)，保留请求中省略的字段。[群组资料更新](https://github.com/marmot-protocol/mdk/pull/2096)通过现有的、需经当前管理员授权的路径公开对群组名称和描述的修改。其 socket 认证仍会授予整个本地 API 的访问权；这次合并没有加入按主体划分的能力授权。这些源代码变更是在带 tag 的 0.11.0 版本之后进行的。

### rust-nostr 关联 relay 计数应答 {#rust-nostr-correlates-relay-count-replies}

[rust-nostr](https://github.com/rust-nostr/nostr) 是一个面向 Nostr 应用的 Rust 库和 SDK，它合并了[相互关联的 COUNT 响应和更清晰的等待者错误](https://github.com/nostrdevkit/nostr/pull/1478)。SDK 会在发送 COUNT 之前先订阅，并且只接受与之匹配的应答，避免丢失或已关闭的接收端看起来像是合法的零。它还会为发布确认和 relay 认证保留接收端的错误，使调用方能够区分缺少确认和明确拒绝。公开方法签名保持不变。

### ZapTracker 加入 Nostr 网络和引用指标 {#zaptracker-adds-nostr-network-and-quote-metrics}

[ZapTracker](https://github.com/pratik227/zap_dashboard) 是一个面向创作者的面板，用于查看 Nostr 互动和钱包活动。一项[网络面板合并](https://github.com/pratik227/zap_dashboard/pull/133)用来自 nostr.watch 的在线 Nostr relay 数据和来自 NIP-11 文档的能力信息取代了 Lightning 网络统计。一项[引用指标变更](https://github.com/pratik227/zap_dashboard/pull/135)会在点赞、转发、书签和 zap 之外，统计带有 `q` tag 的 kind 1 event。这让创作者可以在内容排名和互动图表中看到引用；目前这仍是已合并的源代码证据。

### LaWallet NWC 把卡片充值路由到卡片钱包 {#lawallet-nwc-routes-card-top-ups-to-the-card-wallet}

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) 通过 Nostr Wallet Connect 把 Lightning 钱包连接到应用。其 [BoltCard 充值合并](https://github.com/lawalletio/lawallet-nwc/pull/316)公布了一个 LUD-19 支付链接，通过卡片钱包的 NWC `make_invoice` 方法创建发票。被冻结、已停用或未配对的卡片不会公布支付链接，该路径也不会把充值重定向到所有者单独的 Lightning 地址。一项[后续变更](https://github.com/lawalletio/lawallet-nwc/pull/319)在模拟器中公开了同一链接，并在 LNURL 发送时携带收款方接受的付款人备注。

### 一个新的 khatru relay 提供所有者审核控件 {#a-new-khatru-relay-exposes-owner-moderation-controls}

[nostr-relay-khatru](https://github.com/rzazo24/nostr-relay-khatru) 于 9 月 29 日发布了初始源代码，这是一个通用 relay，衍生自已停止维护的 HiveScope 专用实现。其[公开实例](https://relay.hivescope.xyz)提供一份 NIP-11 文档，其中列出了该仓库，并宣称支持认证、event 过期、受保护 event、计数、协调和 relay 管理。[9 月 30 日的一次实现](https://github.com/rzazo24/nostr-relay-khatru/commit/a6ef7cff9c4f833a6a2f72957d45935c736a0c51)在其所有者面板中加入了审核控件。公开元数据证明的是一个已部署的端点，而不是每一种宣称的方法都已成功测试。

### 一个本地信任网络构建器追踪取消关注 {#a-local-web-of-trust-builder-tracks-unfollows}

[etemiz/wot](https://github.com/etemiz/wot/commit/212fe268dd781c73adad51329be235abc8fd37db) 于 9 月 30 日发布了一个 Nostr 信任网络爬虫。它读取关注列表和 NIP-65 relay 列表，从可配置的根节点计算信任值，并把分数写入 LMDB，供 relay 策略、feed 和垃圾信息过滤器使用。[项目文档](https://github.com/etemiz/wot)解释了其中的取舍：实时更新会增加信任，而计划执行的完整爬取会应用信任下降和取消关注。分数取决于所选的根节点。这是新发布的源代码，没有带 tag 的版本，也没有声称已用于生产部署。

### Moyu 推出 Marmot 工作空间客户端 {#moyu-opens-a-marmot-workspace-client}

[Moyu](https://github.com/tsgx1990/moyu) 已发布一个基于 [Marmot](/zh/topics/marmot/) 构建的 Rust 工作空间聊天客户端的源代码，提供命令行、终端和桌面界面。其 [9 月 30 日的变更](https://github.com/tsgx1990/moyu/blob/88a20d247510d1cc46ca955564aa395d26ae8e89/CHANGELOG.md)利用本地记录的成员变动，阻止旧的加入请求让已移除的成员重新进入，让邀请码在七天后过期，并允许管理员撤销邀请码。终端输出会过滤其他成员提供的控制字符和文本方向覆盖字符。一个固定版本的 MDK 分支会把 Blossom 附件传输通过已配置的 SOCKS5 代理路由，并由该代理执行主机名解析。0.3.0 的变更已在公开源代码中，但目前还没有公开的版本 tag 或版本条目。

## 协议与规范工作 {#protocol-and-spec-work}

### NIP-39 把身份证明扩展到 Bluesky 和 Discord {#nip-39-extends-identity-proofs-to-bluesky-and-discord}

[NIP-39](/zh/topics/nip-39/) 让一个 Nostr 账户可以指向一份证明，表明它控制着另一个平台上的某个身份。[9 月 27 日合并的一项变更](https://github.com/nostr-protocol/nips/pull/2486)为新证明提供了一句推荐措辞，并告诉验证方接受包含该账户 npub 的旧证明，即使其措辞不同。它还把 Bluesky 帖子和 Discord 消息记录为证明所在的位置。一条 Discord 声明只能由能够读取该消息所在服务器的人来核验。

### NIP-86 为 relay 管理员加入邀请码管理 {#nip-86-adds-invite-code-management-for-relay-administrators}

Compass 曾在 7 月 8 日那期中介绍过当时仍处于开放状态的 [NIP-86 邀请提案](https://github.com/nostr-protocol/nips/pull/2408)；该提案现已合并。[NIP-86](/zh/topics/nip-86/) 定义了标准的 relay 管理 API，而 [NIP-43](/zh/topics/nip-43/) 定义了受限 relay 如何公布成员资格并处理准入请求。9 月 24 日的合并加入了 `listclaims`、`createclaim` 和 `deleteclaim`，让管理员可以列出、签发和撤销 relay 所接受的邀请码。这为运营者提供了一条管理邀请的途径，这些邀请可以在成员加入后授予其某个角色；但它并不要求每个 relay 都支持这些方法。

对上周 [NIP-86 报道](/en/newsletters/2026-09-23-newsletter/#nip-86-adds-clear-and-list-methods-for-relay-management)的一处更正：[已合并的规范](https://github.com/nostr-protocol/nips/blob/5b9920982ae1f4061328c1b09a90360da28d13c8/86.md)加入的是 `unallowevent`、`unbanevent`、`listallowedevents` 和 `listdisallowedkinds`。之前的条目列出的是一份过时提案描述中的名称。前两个方法用于撤销针对单个 event 的允许或封禁决定；其余两个用于查看被允许的 event 和不允许的 kind。

### NIP-51 把收藏的关注集合移到一个未被占用的 event kind {#nip-51-moves-favorite-follow-sets-to-an-unused-event-kind}

[NIP-51](/zh/topics/nip-51/) 定义了公开和私密列表，其中包括用户收藏的关注集合列表。Compass 曾在 7 月 22 日那期中介绍过这项 [kind 冲突提案](https://github.com/nostr-protocol/nips/pull/2417)；它现已合并。9 月 27 日的更正为该收藏列表分配了 kind `10021`，因为先前的编号已被占用。其 `a` tag 仍指向 kind `30000` 的关注集合。这项变更解决了规范中的编号冲突；并没有创造一种新的关注方式。

### NIP-51 提议为每个讨论串提供隐藏回复 {#nip-51-proposes-hidden-replies-for-each-thread}

一项[开放的 NIP-51 提案](https://github.com/nostr-protocol/nips/pull/2489)将让讨论串的作者发布一个公开的隐藏回复集合，配合的客户端会把这些回复放在一个开关之后显示。它为每个讨论串使用一个可寻址的 kind-30027 event，以根 event 的 ID 作为其 `d` tag，并用 `e` tag 列出各条回复；只有由根 event 作者签名的集合才会生效。把根 event 本身列入其中，就是要求客户端隐藏其他作者的回复并不再提供回复编辑框，而回复仍可以发布到 relay 上。按讨论串划分的格式把编辑冲突限制在同一个对话内。作者报告称已在 Nostrich 中实现，但对公开源代码的检查未能证实这一点；该提案仍未合并，其集合格式仍在讨论中。


### NIP-DB 提议为以密钥寻址的服务提供经过验证的域名 {#nip-db-proposes-verified-domain-names-for-key-addressed-services}

9 月 28 日提交的[开放 NIP-DB 提案](https://github.com/nostr-protocol/nips/pull/2487)描述了一类 Nostr event，用于把普通互联网域名绑定到在以密钥寻址的网络上为其提供服务的密钥，例如 [FIPS](/zh/topics/fips/)，这是一种按 Nostr 公钥为节点寻址的加密网状网络。域名所有者可以通过 DNS TXT 记录或随声明一同携带的 DNSSEC 证明来建立绑定；客户端会固定经过验证的结果，供之后离线使用。该提案明确禁止通过未经验证的声明进行解析，因为任何人都可以在 Nostr event 中声称拥有他人的域名。[fips-pub-domains](https://github.com/fr34aky/fips-pub-domains) 是作者的参考实现，但 event kind 编号和部分针对覆盖网络的措辞仍在审查中。其报告的端到端测试是作者自己的证据，并不代表该提案已是被接受的 NIP。

### 一份私有 feed 草案探索加密的接收者群组 {#a-private-feed-draft-explores-encrypted-groups-of-recipients}

9 月 29 日开放的一项[新的多接收者信封提案](https://github.com/nostr-protocol/nips/pull/2488)勾勒了私密笔记、回复和连接，其目标接收者可以找到某个 event，而无需在其可见 tag 中暴露自己的普通公钥。它提议使用由共享密钥派生的不透明成对别名 tag 和临时 event kind，其中包括一种为数百位读者封装另一个 Nostr event 的方式。这可以为小型私有 feed 提供一条比逐一给每位成员单独发送消息更直接的获取路径。

[提案作者](https://github.com/nostr-protocol/nips/pull/2488)明确表示这仍是一项进行中的工作。该草案尚无经过验证的实现或安全审查，其 kind 分配和字节层面的签名规则也仍未确定。

### 一项 Blossom 提案让其他人可以公布镜像的媒体 {#a-blossom-proposal-lets-other-people-announce-mirrored-media}

一项[开放的 NIP 提案](https://github.com/nostr-protocol/nips/pull/2478)描述了一种方式，让镜像了其他作者 Blossom blob 的人通过 Nostr 公布该副本。这样，当原始服务器丢失该 blob 时，客户端就可以去寻找副本。讨论中还提出，当公布的服务器提示已经过时，可以检查镜像者当前的 BUD-03 服务器列表。这是一条拟议的发现路径，并不保证客户端或存档 relay 已经提供后备存储。

### 道路事件报告寻求统一的 Nostr 格式 {#road-event-reports-seek-a-shared-nostr-format}

[开放的道路事件报告提案](https://github.com/nostr-protocol/nips/pull/2479)描述了针对坑洼、封路、摄像头和其他路况的报告与确认。它使用位置 tag 和 [NIP-40](/zh/topics/nip-40/) 的过期时间戳（告诉 relay 何时停止提供某个 event），因此报告无需无限期地保持有效。作者根据从公共 relay 恢复的 event 样本以及现有的、用于报告路况的 [Roadstr 客户端](https://github.com/jooray/roadstr)进行了修订，但草案仍留有一个紧凑编码的问题悬而未决，所提议的 NIP 编号也尚未被采纳。

### Marmot 重新审视多设备协调 {#marmot-revisits-multi-device-coordination}

[Marmot 的多设备重新设计](https://github.com/marmot-protocol/marmot/pull/427)用一份非规范性的流程说明取代了一份未被实现的 External Commit 草案，以征求早期反馈。新方向探索由现有设备批准新设备、将其带入对话并在之后移除设备的方式，同时让悬而未决的问题保持可见。被移除草案所预留的 ID 已被释放，因为没有任何实现采用它们。这份构想文档没有分配新的 ID 或线路格式，也不是一个已实现的多设备功能。

## Nostr 的六个九月 {#six-years-of-nostr-septembers}

九月的最后一期是一个机会，可以回顾 Nostr 如何从草图走向一组更大的、可互操作的工具。一个 [2021 年的拼车匹配原型](https://github.com/arcbtc/buber/commit/7a66d400f2)用签名 event 来协调一项服务；五年后，[身份证明的措辞](https://github.com/nostr-protocol/nips/commit/0046368a7)和[列表 kind 冲突](https://github.com/nostr-protocol/nips/commit/6631b3eb1)成了维护者正在解决的那类细节。在这期间，客户端学会了以普通人能够使用的方式呈现对话、媒体和恢复功能。下面这些带日期的来源展示了这一进程中的各个阶段。它们并不能证明每一项实验都已上线，也不能证明每一种旧设计至今仍被推荐。

### 2021 年 9 月：形态实用的早期实验 {#september-2021-early-experiments-with-useful-shapes}

[9 月 4 日的一次 BUber commit](https://github.com/arcbtc/buber/commit/7a66d400f2) 探索了一个使用 Nostr event 的出租车匹配概念。它展示了一条经过签名、由 relay 传送的请求如何在不把整个服务交给单一服务器的情况下协调人们。该来源只是一个概念，并不能证明有一项已上线的拼车服务。

同月晚些时候，[Loquaz 9 月 23 日的源代码](https://github.com/emeceve/loquaz/commit/d885d93d22)提供了一个桌面聊天原型。这是让 relay 消息用起来像普通应用的又一次早期尝试。该来源并不能证明已完成端到端加密或是一款生产级通讯应用；其长远意义在于，在简单的 event 之上寻找可用的对话界面。BUber 测试了拼车匹配，Loquaz 测试了聊天；两者都在通用客户端模式尚未定型之前就使用了签名 event。这些尝试揭示了后来的客户端反复面对的两个问题：通过 relay 进行协调，以及把 event 呈现为可用的对话。

### 2022 年 9 月：聊天和委托操作进入规范 {#september-2022-chat-and-delegated-actions-enter-the-specifications}

[9 月 10 日的 NIP-28 变更](https://github.com/nostr-protocol/nips/commit/3423a6dfb)描述了公共聊天频道，其中的消息和元数据可以由客户端结合起来解读。[NIP-28](/zh/topics/nip-28/) 让共享房间成为一个明确的协议主题，并为客户端提供了通用的频道约定。

9 月 23 日，[NIP-26](/zh/topics/nip-26/) 的[委托签名文本](https://github.com/nostr-protocol/nips/commit/b62aa418d)记录了一种方式，让一个密钥授权另一个密钥签署有限的 event。它抓住了 2022 年的一个重要设计问题：如何在不把主密钥交给每个应用的情况下使用 Nostr 身份。[NIP-26 现在被标记为不推荐](https://github.com/nostr-protocol/nips/blob/master/26.md)，因此这只是一项实验的记录，而不是给新集成的建议。它后来的状态显示了签名模型的演变：即使所提出的方案已被停用，规范仍可以保留一个有价值的问题陈述。

### 2023 年 9 月：客户端围绕 relay 发现和元数据逐渐成熟 {#september-2023-clients-grow-up-around-relay-discovery-and-metadata}

Damus 是一款 Nostr 社交客户端。其 [9 月 21 日的更新日志](https://github.com/damus-io/damus/blob/master/CHANGELOG.md#16-18---2023-09-21)记录了在本地 Nostr 数据库、搜索和话题标签导航方面的工作。这些变更让繁忙的社交 feed 在手机上更易于浏览和恢复；这份带日期的更新日志是那个客户端版本的证据，而不是后来所有 Damus 功能的证据。

协议细节也在推进。[9 月 26 日的一项变更](https://github.com/nostr-protocol/nips/commit/44c21c9d8)澄清了 [NIP-24](/zh/topics/nip-24/) 中可选的个人资料元数据字段，而 [NIP-65 在 9 月 29 日的变更](https://github.com/nostr-protocol/nips/commit/3b5d3ca67)处理了 relay URI 的规范化和去重。[NIP-65](/zh/topics/nip-65/) 告诉客户端如何发布它们用于读取和写入的 relay；一致的 URI 处理让这些列表即使在字符串存在无害差异时也能指向同一个 relay。这一小小的约定推动客户端设计走向可靠的发现：要找到一个人的 event，就要知道它们被发布到了哪里。

### 2024 年 9 月：帖子获得更丰富的上下文 {#september-2024-posts-acquire-richer-context}

[Damus 9 月 22 日的版本说明](https://github.com/damus-io/damus/blob/master/CHANGELOG.md#1101---2024-09-22)介绍了对 [NIP-84](/zh/topics/nip-84/) 高亮和评论的支持。NIP-84 让读者可以引用并讨论长文中的某个段落。这项客户端工作展示了一个协议构想如何变成人们在阅读时可以使用的功能。

与此同时，[NIP-34](/zh/topics/nip-34/) 在 [9 月 20 日迎来一项变更](https://github.com/nostr-protocol/nips/commit/ea36ec9ed)，完善了基于 Nostr 的 git 协作中的 issue 主题和标签，而 [NIP-73](/zh/topics/nip-73/) 也在[同一天迎来一项变更](https://github.com/nostr-protocol/nips/commit/79786bb7b)，完善了外部内容标识符。这是两项相互独立的规范变更：一项帮助仓库的 issue 保持结构，另一项让 event 可以引用 Nostr 之外的材料。两者都扩展了内容在社区、仓库和其他媒体之间流转时，客户端能够保留的含义。

### 2025 年 9 月：访问控制和支付上下文变得更加精确 {#september-2025-access-controls-and-payment-context-become-more-precise}

[9 月 6 日的一次 NIP-42 修订](https://github.com/nostr-protocol/nips/commit/4c5d5fff9)处理了多用户 relay 认证。[NIP-42](/zh/topics/nip-42/) 让 relay 可以要求客户端证明是哪个 Nostr 密钥在发出请求；这次更新对于通过同一连接为多个已认证账户提供服务的服务来说很重要。

[9 月 15 日的一次 NIP-47 更新](https://github.com/nostr-protocol/nips/commit/400d975da)为 Nostr Wallet Connect 请求加入了可选的支付元数据。[NIP-47](/zh/topics/nip-47/) 让应用可以通过 Nostr 请求钱包执行操作。更多上下文可以让钱包交互更易于理解，但这些元数据可能暴露付款人的详细信息，因此客户端和钱包仍需将其视为敏感信息。这项变更说明，互操作性工作此时已经涵盖接收方能够获知什么，而不仅仅是请求能否送达。

### 2026 年 9 月：互操作性细节与公开身份相遇 {#september-2026-interoperability-details-meet-public-identity}

今年九月，一项[已合并的 NIP-51 变更](https://github.com/nostr-protocol/nips/commit/6631b3eb1)把关注集合的 event kind 移出了冲突。[NIP-51](/zh/topics/nip-51/) 定义了用户可以维护和分享的列表；唯一的 event kind 让客户端能够区分不同的列表类型。之前的一期 Compass 讨论过该提案，而九月的合并是其状态的变化。

第二项[已合并的 NIP-39 变更](https://github.com/nostr-protocol/nips/commit/0046368a7)澄清了证明文本，并加入了更多把外部账户与 Nostr 身份关联起来的方式。[NIP-39](/zh/topics/nip-39/) 关注的是可核验的身份声明，而不是一个中心化的身份注册表。这两项合并合在一起表明，当前的协议工作集中在那些决定独立客户端能否正确解读同一身份和列表 event 的细节上。它们也显示出一种转变：从发明新的 event 类别，转向减少现有类别中的歧义。

纵观这六个九月，其中的规律是一种演进：从证明[签名 event 可以描述一个应用请求](https://github.com/arcbtc/buber/commit/7a66d400f2)，到追问[客户端如何验证关于某个人的声明](https://github.com/nostr-protocol/nips/commit/0046368a7)。那些早期原型之所以重要，是因为它们揭示了后来的规范和客户端必须回答的问题：由谁签名，在哪里找到一个 event，它意味着什么，以及人们如何判断是否应该信任它。这也是为什么一项小而精确的协议更正，可能与一个新界面同样重要。
