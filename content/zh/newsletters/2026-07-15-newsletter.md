---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
draft: false
type: newsletters
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
description: "Vector v0.4.0 在群聊中弃用 Marmot，转而采用开放的 Concord 协议，并在数天后发布 Concord v2；Amethyst 合并了自己的洁净室 Concord 实现；Sonar 从 Bitchat 分离，推出跨平台 alpha 版和贴纸包规范；Divine Mobile 1.0.16 带来静态加密和 ProofMode 来源证明；Bitchat 1.7.0 加入实时按键通话语音；MDK v0.9.4 为外部签名器登录设定边界。"
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：**[Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) 弃用 [Marmot](/zh/topics/marmot/) 作为群聊的默认传输层，转而采用 [Concord](/zh/topics/concord-protocol/)，这是一个开放的、采用 MIT 许可的社区协议，Soapbox 的 Armada 也在使用它；四天后又发布了 Concord v2，带来面向机器人的斜杠命令选择器、自毁计时器和 NIP-58 徽章。同一周，[Amethyst 合并了自己的洁净室、线路兼容的 Concord 实现](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)。[Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) 从 Bitchat 分离，推出跨平台 alpha 版，并且是本周贴纸包 kind 提案所引用的规范来源。[Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) 带来更深入的视频编辑器、静态加密，以及在下载带水印片段时仍能保留的 ProofMode 来源证明。[Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) 为 DM 加入实时按键通话语音，并在公共网格上支持签名的按键通话。[MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) 为外部签名器登录设定边界并加入草稿持久化，在 Vector 于群聊上远离该规范的同一周延续其加固工作。

打标签的发布带来：[n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) 加入 NSEC Bunker 支持，[cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) 在 cdk、cdk-nwc 和 cdk-ffi 中加入 NIP-47 钱包服务支持，[Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) 改进 Nostr Connect 并加入 ncryptsec1 导入，[Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) 登陆 macOS 并支持定时发送，[Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) 加入 DM 总开关，[Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) 将密钥备份加固为 NIP-49 格式，[Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) 加入首次运行的 FROST 引导，[Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) 加入 Cashu 钱包和基于 relay 的推送通知，[Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) 加入平板模式和群聊照片，以及 [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) 加入 git、diff 和读取文件的辅助请求。

在未发布的一侧，[Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) 让账户可以用加密的 NIP-85 名片为联系人起昵称，共合并 54 个 PR；[Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) 推出 My Kitchen 第三阶段并修复了一个 NDK 连接池法定数量的缺陷；[Kehto](#kehto-streams-outbox-reads-before-relay-discovery) 在 relay 发现完成之前就流式处理 outbox 读取；[Wired 和 TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) 加入 NIP-57 创作者收益分成；[Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) 围绕临时访客结账重建商家订单收件箱；[Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) 在 240 个合并的 PR 中加固频道创建者的开通流程；[Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) 采用支持多账户和二维码配对的 NIP-49 签名器。本周新纳入追踪：[OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr)、[Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles)，以及 Discovery 精选 [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer)，一个把请求代理给 Heartwood 硬件伴侣的无密钥 NIP-55 签名器。

NIPs 仓库上周没有合并任何内容，并新开了六个提案：[kind:10011 收藏关注集](#open-kind10011-favorite-follow-sets)、一个[扩展 NIP-4E 的私密加密云盘](#open-private-encrypted-drive-extends-nip-4e)、[NIP-DA 带权限的私密数据共享](#open-nip-da-permissioned-private-data-sharing)、[贴纸包 kind 10031 和 30031](#open-sticker-pack-kinds-10031-and-30031)、[NIP-29 消息置顶](#open-nip-29-message-pinning-with-kind9010-and-kind39005)，以及一次 [NIP-66 relay 发现重构](#open-nip-66-relay-discovery-restructure)。本期 Deep Dive 讲解 [NIP-99 与 Gamma Markets 商务扩展](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)。

---

## 头条报道

### Vector v0.4.0 将群聊从 Marmot 迁移到 Concord，Amethyst 数天后推出自己的 Concord 客户端

[Vector](https://github.com/VectorPrivacy/Vector) 是一款围绕单一二进制、隐私优先的 DM 与群聊客户端构建的 Nostr 通讯工具。[Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) 将应用的消息引擎重写为共享的 `vector-core` 库，并在同一版本中弃用 [Marmot](/zh/topics/marmot/)（MLS-over-Nostr）作为群聊的默认传输层，转而采用 [Concord](/zh/topics/concord-protocol/)，一个端到端加密的社区协议；已有的 Marmot 群聊历史不会迁移，发布说明告知用户在升级前备份任何 Marmot 群组数据。Vector 自己的发布说明将 Concord 描述为「我们自定义的消息协议」，但底层的 [CORD-01 至 CORD-07 规范](https://github.com/concord-protocol/concord)是单独发布的、采用 MIT 许可，并且已在 Vector 之外实现：Soapbox 的 Discord 风格客户端 [Armada](https://gitlab.com/soapbox-pub/armada) 在同一份 Concord 规范上构建其 Communities 功能；一天之后，[Amethyst 合并了自己的洁净室、线路兼容的 Concord 实现](https://github.com/vitorpamplona/amethyst/pull/3566)，下文有完整报道。同一个 Vector 版本还加入了对全部流量的可选 Tor 路由、通过二维码或粘贴 bunker URI 的 [NIP-46](/zh/topics/nip-46/) 远程签名器登录、带应用内切换器的多账户，以及跨客户端共享的自定义 emoji 包。消息删除会在 DM 和群聊中为双方移除消息，而 Vector 有意保留临时签名密钥，而非遵循标准的 [NIP-17](/zh/topics/nip-17/) 删除流程，这是项目在发布说明中明确指出的、出于隐私考虑的偏离。四天后，[v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) 推出 **Concord v2**，据称为 Communities 带来重大的隐私与稳定性改进，同时保持现有社区正常运行，并附带面向机器人的 Discord 风格斜杠命令选择器（支持带类型的参数）、按会话的自毁计时器，以及面向漏洞猎人的 NIP-58 徽章系统。群聊上远离 Marmot 的举动，恰好发生在下文 [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) 继续投入该规范的同一周。

### Amethyst 推出面向端到端加密社区的洁净室 Concord 实现

[Amethyst](https://github.com/vitorpamplona/amethyst) 是一款功能丰富的 Android 与多平台 Nostr 客户端。[PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) 加入了 [Concord](/zh/topics/concord-protocol/)（CORD-01 至 CORD-07）的完整实现，覆盖无服务器的端到端加密社区：在普通 relay 之上以 gift-wrap 承载控制、聊天与访客留言三个平面；以所有者为根的角色与封禁裁决由每个客户端在本地校验，而不是信任某个服务器；以及通过重新分发密钥切断被移除成员的访问。协议与加密代码位于 `quartz/`，状态与视图模型位于 `commons/`，面向 Android 的界面与导航位于 `amethyst/`，`cli/` 下有轻量的 CLI 命令；目前还没有桌面界面，因为共享逻辑放在 `quartz`/`commons` 中，供 Desktop 日后采用。该实现是洁净室的：基于公开的 CORD 规范和观察到的线路常量构建，采用 Amethyst 自己的 MIT 许可，与 Armada 的 AGPL-3.0 代码库相互独立。Armada 自己的测试向量数值被移植进 Quartz 的单元测试，以确认两个客户端在线路层面确实可以互操作，这让 Concord 在数天之内拥有三个独立实现：首发的 Vector、作为 Soapbox 参考客户端的 Armada，以及如今 Amethyst 依规范构建的版本。

### Sonar 从 Bitchat 分离，推出跨平台 alpha 版和贴纸包规范

[Sonar](https://sonarprivacy.xyz/) 是一款由 Bitchat 发展而来的蓝牙网格加 Nostr 通讯工具与钱包，其 Marmot 群组 DM 可与 White Noise 互操作。代码位于 [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar)。[v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) 加入 Signal 风格的有界会话记录窗口，让打开和滚动的性能保持本地优先；在对等节点之间同步附近发现状态；并修复了因 content-type 和 HTTP 状态处理而失败的 Blossom 媒体上传。此前的 [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) 排空实时 Marmot 事件以加快聊天刷新，并在通话、消息、钱包和推送方面弥合了 Android 与 iOS 之间的功能差距。Sonar 也是 [PR #2410](#open-sticker-pack-kinds-10031-and-30031) 所引用的规范来源，该 PR 依据项目自己的「Sonar Stickers」规范注册贴纸包事件 kind，为这次发布提供了通往本周协议工作的直接连接。

### Divine Mobile 1.0.16 带来更深入的视频编辑器、静态加密和 ProofMode 来源证明

[Divine](https://github.com/divinevideo/divine-mobile) 是一款构建在 Nostr 上、采用信任网络策展信息流的短视频客户端。[v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16) 是自 #30 以来的首个打标签版本，为视频编辑器加入片段转场、倒放、旁白录制器和时间轴节拍标记，同时加入信息流调节控件，让用户通过滑动直接调整推荐，而不是把它交给不透明的互动信号。该版本还为本地数据开启静态加密，加入可在应用被挂起后继续进行的后台上传，并在下载带水印的片段时携带 [ProofMode](/zh/topics/proofmode/) 来源数据，使人工创作的证明不会在传输中被剥离。Divine 还为 16 岁以下账户提供新的保护措施，并将本地化扩展到 17 种语言和 284 条已翻译文本。

### Bitchat v1.7.0 为 DM 和公共网格加入实时按键通话语音

[Bitchat](https://github.com/permissionlesstech/bitchat) 是一款带有可选 Nostr relay 网关的蓝牙网格聊天应用。[v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0) 于 #30 发布当晚推出，在 [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) 中加入实时按键通话语音：发送者按住按钮期间持续流式传输音频，若流中断则回退为语音留言；此外 [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406) 在公共网格上加入签名的按键通话，使共享网格频道上的实时语音片段携带发送者认证。该版本还修复了对等 ID 轮换：在经过验证的重新广播上重新绑定链路，从而以新 ID 识别出同一个对等节点（[PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)）；发往当前不可达对等节点的私信现在会以存储转发方式排队，而不是直接失败（[PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)）。这直接延续了 #30 对 v1.6.0 中 [NIP-13](/zh/topics/nip-13/) 工作量证明和网格到 Nostr 网关工作的报道。

### MDK v0.9.4 为外部签名器登录设定边界并加入草稿持久化

[MDK](https://github.com/marmot-protocol/mdk) 是 [Marmot](/zh/topics/marmot/) 协议的参考 SDK，即 #30 报道过其规范被标记为已采纳的 MLS-over-Nostr 消息层。[v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) 在 [PR #793](https://github.com/marmot-protocol/mdk/pull/793) 中为客户端在外部签名器登录期间走过的建议目录步骤设定边界，避免远程签名器缓慢或无响应时出现无限重试循环。同一版本在 [PR #812](https://github.com/marmot-protocol/mdk/pull/812) 中加入草稿消息持久化和个人资料网站绑定，延续了 MDK 自 v0.9.0 以来持续进行的渐进式加固。

---

## 打标签的发布

### n_cord v1.1 加入 NSEC Bunker 支持

[n_cord](https://github.com/0n4t3/n_cord) 是一款受 Discord 和 IRC 启发、由 Nostr 驱动的聊天客户端。[v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) 加入 [NIP-46](/zh/topics/nip-46/) NSEC Bunker 支持，并修复了一个回复处理的缺陷。

### cdk v0.17.3 在 cdk、cdk-nwc 和 cdk-ffi 中加入 NIP-47 钱包服务支持

[cdk](https://github.com/cashubtc/cdk) 是一个 Cashu 开发工具包；这个版本在大多数方面只涉及 Bitcoin/Lightning，但 [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) 加入了 [NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）服务支持，包含专门的 NWC 服务 crate、钱包集成、面向 `cdk-ffi` 的 FFI 绑定，以及端到端测试覆盖，为基于 cdk 构建的 Cashu 钱包提供标准的 Nostr Wallet Connect 接口。

### Coop Mobile v0.2.4 改进 Nostr Connect 并加入 ncryptsec1 导入

[Coop Mobile](https://git.reya.su/reya/coop-mobile) 是一款面向移动平台的 [NIP-17](/zh/topics/nip-17/) 私密消息客户端。[v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) 改进了其 [NIP-46](/zh/topics/nip-46/) Nostr Connect 流程，修复了在某些连接上永久卡住的加载指示器，并加入对 [NIP-49](/zh/topics/nip-49/) `ncryptsec1` 加密密钥格式的导入支持，同时重新设计了身份导入界面。

### Nmail v0.14.0 登陆 macOS，支持定时发送和推送通知

[Nmail](https://github.com/nogringo/nostr-mail-client) 是一款构建在 Nostr 上的邮件客户端；[v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) 将应用带到 macOS，加入定时发送并为排队消息设立专门的「已定时」邮箱，还加入了推送通知。该版本还将通讯录的 Nostr 标识符解析改为使用 NDK 的 [NIP-05](/zh/topics/nip-05/) 解析器，取代此前的自制实现。

### Nostrord v2.2.0 加入 DM 总开关和更丰富的私信

[Nostrord](https://github.com/nostrord/nostrord) 是一款面向 Android、iOS、网页和桌面的 [NIP-29](/zh/topics/nip-29/) 基于 relay 的群聊客户端。[v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) 加入了可一次性关闭所有私信功能的总开关（[PR #175](https://github.com/nostrord/nostrord/pull/175)），并推出「更丰富的私信」（[PR #186](https://github.com/nostrord/nostrord/pull/186)），延续了 #30 对该版本合并 relay 连接池和检测僵尸 WebSocket 的报道。

### Nostr WoT 0.3.86 加固密钥备份和签名提示

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) 是一款将 Nostr 身份与 Lightning 钱包配对的浏览器扩展。[v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) 将加密密钥备份迁移到标准的 [NIP-49](/zh/topics/nip-49/) 格式，让签名提示显示完整事件和所有 tag 而非摘要，依据签名校验 relay 数据，并在切换账户时不再暴露当前身份。该扩展还移除了未使用的 `scripting` 浏览器权限。

### Keep Android v1.1.8 加入首次运行的 FROST 引导

[Keep](https://github.com/privkeyio/keep-android) 是一款基于 FROST 门限密钥分片构建的 Android 签名器。[v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) 加入首次运行流程，向新用户解释 FROST 密钥分片，并让其在第一个签名请求到来之前选择手动、基础或自动的签名策略，这是底层 keep-mobile crate 的门限签名模型在 Android 侧的首个引导流程。

### Noscall v0.6.0 加入 Cashu 钱包和基于 relay 的推送通知

[Noscall](https://github.com/sanah9/noscall) 是一款构建在 Nostr 上的安全音视频通话应用。[v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) 加入账户范围的 Cashu 钱包，支持多 mint 余额、ecash 收发，以及带报价持久化的 Lightning 收付。该版本还将 Android 推送通知从 Firebase Cloud Messaging 迁移到通过 UnifiedPush 的基于 Nostr relay 的投递路径，并改进了登录重试期间 iOS VoIP 和 APNs 推送的可靠性。

### Kubo 推出平板模式和群聊照片

[Kubo](https://github.com/JeroenOnNostr/kubo) 是一个采用信任网络策展信息流、对儿童安全的 Nostr 视频平台。[kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) 为儿童信息流加入可选的平板网格布局，支持在群聊消息中附加照片，并修复了 Android 上注册按钮被屏幕键盘遮挡的问题。

### Nostr Codex Phone v0.2.9 加入 git/diff/读取文件的辅助请求

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) 是一个面向本地编码助手工作进程的移动控制界面，通过加密的 Nostr DM 通信。[v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) 加入移动端 OpenCode 工具操作，包括 git、diff、读取文件、状态和历史等辅助请求，改进了会话置顶与搜索，并加入任务停止控制，同时还有在此前 v0.2.8 中推出的加密 [Blossom](/zh/topics/blossom/) 上传封装。

### GitWorkshop v3.0.3 修复仓库浏览器中新广播的 ref，并推出首个 Android 构建

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) 是一个用于浏览和审阅 NIP-34 仓库的 git-over-Nostr 网页界面。[v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) 修复了分支、标签、提交和代码浏览视图无法解析仓库在浏览器加载之后才广播的 ref 的问题，同时清理了 CI 工作流时序，并已直接对照标签和提交历史确认。同一周，GitWorkshop 在 [Zapstore](https://zapstore.dev) 发布了首个原生 Android 构建，从 v3.0.0 起步并在数小时内到达 v3.0.3；网页界面仍是主要入口，而 Android 包首次把同样的 NIP-34 仓库浏览带到手机上。

### Bitcoin-Safe 登陆 Flathub，让其 Nostr Sync & Chat 插件受到关注

[Bitcoin-Safe](https://bitcoin-safe.org) 是一款围绕硬件签名器工作流构建的自托管 Bitcoin 钱包。该项目本周[发布了 Flathub 软件包](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe)，这是它首次进入主流 Linux 应用商店。这次 Flathub 发布把 Bitcoin-Safe 的 Sync & Chat 插件带到更广的受众面前：该插件通过项目自己的 [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) 库使用 [NIP-17](/zh/topics/nip-17/) 私信，在用户的多台设备之间同步钱包标签，并在受信任的参与者之间收发 PSBT 以完成远程多签联署。Nostr 层本身更早就已推出，见 [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0)（2026-06-29），该版本围绕「Share via Chat & Sync」连接类型重新设计了交易签名，与二维码、USB 和蓝牙并列。本周的新闻是 Flathub 打包首次把这个既有功能带到主流 Linux 受众面前。

---

## 未发布的变更

### Amethyst 让账户用加密的 NIP-85 名片为联系人起昵称

除上文提到的 [Concord 实现](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)之外，Amethyst 上周还合并了 54 个其他 PR。其中的重点是 [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548)，它让一个账户通过发布自己关于对方的 kind 30382 [NIP-85](/zh/topics/nip-85/) 联系人名片，为任何其他用户起昵称。昵称、一条私密备注，以及任何自定义的 [NIP-30](/zh/topics/nip-30/) emoji 短代码映射，都存放在名片经 [NIP-44](/zh/topics/nip-44/) 加密的 content 中，因此只有签名账户可以读取；名片在登录时通过账户扩展的 outbox relay 集合同步，之后增量同步。信息流、聊天和提及会用昵称替代公开显示名，并在个人资料页用户真名上方显示一张可点按的昵称名片。

### Zap Cooking 推出 My Kitchen 第三阶段并修复 NDK 连接池法定数量缺陷

[Zap Cooking](https://github.com/zapcooking/frontend) 是一款构建在 Nostr 上的食谱分享与烹饪社区应用。它合并了 43 个 PR，延续其「My Kitchen」备餐规划功能，本阶段落地了购物清单生成、食谱选择器和规划周视图。同一批变更修复了 [NDK](https://github.com/nostr-dev-kit/ndk)（Nostr Development Kit）连接池的法定数量就绪缺陷，该缺陷可能让 relay 读取在已有法定数量的 relay 应答之后仍继续等待。

### Kehto 在 relay 发现之前流式处理 outbox 读取

[Kehto](https://github.com/kehto/web) 是一个面向 [NIP-5D](/zh/topics/nip-5d/) Nostr 小应用（即「napplets」）的早期网页运行时。它合并了 26 个 PR。[PR #193](https://github.com/kehto/web/pull/193) 修复了此前 outbox 读取必须等待 [NIP-65](/zh/topics/nip-65/) relay 列表加载完成才会开启任何 relay 的问题，因为一次始终无法完成的 relay 列表加载会同时阻塞事件投递和查询超时；修复后会立即打开已验证的 relay 提示，并在发现写入 relay 的过程中流式返回结果。第二处变更（[PR #196](https://github.com/kehto/web/pull/196)）让项目的身份审计页面与 NAP-SHELL（Napplet 平台的生命周期契约）对齐，这属于本周 `napplet/web` 发布中其他地方也能看到的同一批协议对齐工作。

### Wired 和 TAO 加入 NIP-57 创作者收益分成

[Wired](https://github.com/smolgrrr/Wired) 和 [TAO](https://github.com/smolgrrr/TAO) 是构建在 Nostr 上、注重言论自由的孪生社交客户端，共享同一份 PR 列表；两者都合并了 [PR #121](https://github.com/smolgrrr/Wired/pull/121)，它实现了 [NIP-57](/zh/topics/nip-57/) 创作者收益分成，使发给某条帖子的 zap 可以自动分配给原发帖者之外的贡献者。这延续了 #30 对这对客户端将工作量证明信号提升到 21 位这一未发布工作的报道。

### Conduit Mono 围绕临时访客结账重建商家订单收件箱

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) 是一个与 [NIP-99](/zh/topics/nip-99/) 分类广告相邻的市场协议。[PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) 使用浏览器生成的临时密钥加入访客结账：访客用这把一次性密钥向商家发送加密订单和付款报告，商家再通过电话或邮件在带外跟进，因此买家从不需要一个持久的收件箱身份。[PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) 围绕单一共享的订单状态模型重建商家订单收件箱，分离买家与商家角色，并要求实体或混合订单在转为已发货之前提供追踪码和承运商。该项目的结账流程构建在 [NIP-17](/zh/topics/nip-17/) 私密消息、[NIP-44](/zh/topics/nip-44/) 加密和 [NIP-59](/zh/topics/nip-59/) gift wrap 之上。本周的 [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) 讲解了同一个订单状态问题所指向的 [Gamma Markets](/zh/topics/gamma-markets/) 约定。

### Buzz 围绕 kind 39002 加固频道创建者的开通流程

[Buzz](https://github.com/block/buzz) 是一个通过 Nostr 连接 AI 智能体与人类的群体智慧通信平台。它上周合并了 240 个 PR，从 #30 报道的 kind 44200 智能体轮次指标开始，延续其 relay 层加固的脉络。本周的修复（[PR #1830](https://github.com/block/buzz/pull/1830)）在 kind 39002 频道开通逻辑运行之前先把频道创建者视为成员，堵上了创建者可能在设置过程中被自己的频道拒绝的竞态。

### Nostr Docs 采用支持多账户和二维码配对的 NIP-49 签名器

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) 是一款 Nostr 原生的协作文档应用。它合并了 5 个 PR，其中值得注意的是 [PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)，它采用 `@formstr/signer` 包实现完整的 [NIP-49](/zh/topics/nip-49/) 认证，支持多账户切换和二维码配对，取代了此前的自制签名路径。

### 同期推出

上周还有若干被追踪项目落地了较小的签名器互操作与可靠性修复，不足以单独成段：[ngit-cli](https://github.com/DanConwayDev/ngit-cli) 是一个面向基于 Nostr 的 GitHub 替代方案的命令行客户端，推出 [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3)，让 `ngit init` 给出可操作的设置指引，而不是反复索要 nsec；[Manent](https://github.com/dtonon/manent) 是一款构建在 Nostr 上的私密加密笔记与文件应用，推出 [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1)，修复了 Amber 返回十六进制 pubkey 时 Android 签名器登录失效的问题，并改进了 bunker 登录的滚动；[NoorNote](https://github.com/77elements/noornote) 是一款不依赖 Google 服务的轻量 Nostr 客户端，推出 [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8)，修复了 Nostrord 群组通知丢失的问题并加入自己发帖的提醒开关；[Bray](https://github.com/forgesworn/bray) 是一个面向 AI 智能体与人类、具备信任感知的 Nostr MCP 服务器，推出 [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0)，在 [NIP-46](/zh/topics/nip-46/) bunker 连接时发送客户端名称元数据；[Lumilumi](https://github.com/TsukemonoGit/lumilumi) 是一款 Nostr 网页客户端，将 [NIP-65](/zh/topics/nip-65/) relay 列表缓存到本地存储以便离线回退；[Earthly](https://github.com/moogmodular/earthly) 是一款基于 Nostr 的本地城市与社区应用，加入 [NIP-50](/zh/topics/nip-50/) 地理搜索；[lnbits](https://github.com/lnbits/lnbits) 是一个免费开源的 Lightning 钱包与账户系统，推出 [PR #3925](https://github.com/lnbits/lnbits/pull/3925)，在一个其余部分以 Lightning 为主的版本中让 `send_nostr_dm` 以非阻塞方式发布。

---

## 新纳入追踪与新发现

### OpenDiscord v1.0.1 作为 Nostr 上的 Discord 风格客户端发布

[OpenDiscord](https://github.com/sofia-gros/open-discord) 是一款构建在 Nostr 上的 Discord 风格服务器与频道客户端，具备基于角色的权限和 WebRTC/SFU 语音大厅。[v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) 是该项目首个打标签的安装包版本。

### Auditable Voting v0.1.140 对齐组织者、投票者和审计代理角色

[Auditable Voting](https://github.com/tidley/auditable-voting) 是一个纯客户端的 Nostr 投票外壳。[v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) 将组织者、投票者和审计代理角色与组织者签名的那个确切的公开问卷定义事件对齐，堵上了审计代理可能基于过期生成账户，或基于来自另一个工作进程或组织者的持久化状态而行动的缺口。

### Cambium v0.3.2 与 Heartwood 配对，作为无密钥 NIP-55 签名器

[Cambium](https://github.com/forgesworn/cambium) 是本期的 Discovery 精选：一款自身不持有任何私钥材料的 Android [NIP-55](/zh/topics/nip-55/) 签名器，它通过 [NIP-46](/zh/topics/nip-46/) 把每个签名请求代理给配套的 Heartwood 硬件签名器。该项目与被追踪项目 Bray 共用 `forgesworn` GitHub 组织，而 Heartwood 本身在 #30 中曾被报道推出了 relay 到串口的签名桥接，正是 Cambium 的 Android 侧如今对接的对象。[v0.3.2](https://github.com/forgesworn/cambium) 优化了审批面板，使其在所选身份与应用现有绑定不一致时实时告警，并将活动日志写入移到单一的非阻塞队列。

### 本周同期上线：echoes、Dispatch 和 Linky

本周还有三个值得一提的上线。[echoes](https://github.com/Lwb89dev/echoes) 是一款离线优先、端到端加密的笔记应用，通过 Nostr 私密同步。[Dispatch](https://github.com/freecritter/dispatch) 是一款本地优先的旅行整理工具，每次保存都经 [NIP-44](/zh/topics/nip-44/) 加密，并以一把专用、不可关联的密钥通过 Nostr 备份，其 [v0.3.0](https://github.com/freecritter/dispatch) 版本加入 Amber [NIP-55](/zh/topics/nip-55/) 登录，使应用永远不会直接接触用户的私钥。[Linky](https://github.com/hynek-jina/linky) 在单个渐进式网页应用中，把 Nostr 联系人和 DM 与 Lightning 及 Cashu 支付结合起来。

---

## 协议工作与 NIP 更新

上周没有 PR 合并进 [NIPs 仓库](https://github.com/nostr-protocol/nips)。新开了六个提案。

### 新开：kind:10011 收藏关注集

[PR #2413](https://github.com/nostr-protocol/nips/pull/2413) 来自 fiatjaf，加入 kind:10011 收藏关注集。它沿用了既有模式：kind:10012（收藏 relay 集）持有指向 kind:30002 relay 集的 `a` tag，并把同样的收藏机制扩展到 kind:30000 关注集，使客户端可以收藏一份精选的关注列表，而不必替换自己的联系人列表。

### 新开：扩展 NIP-4E 的私密加密云盘

[PR #2412](https://github.com/nostr-protocol/nips/pull/2412) 来自 Form* 团队，提出一个通用的 Metadata 事件 kind 34578，以 `d` 标识符 tag 和 `t` 子类型 tag 区分，并在其之上构建一个私密加密文件系统，该系统已在 Form* 自己仍处于实验阶段的 Form* Drive 客户端中实现。文件记录是带 `t=files` 的 Metadata 事件：文件 blob 存放在 [Blossom](/zh/topics/blossom/) 服务器上，relay 上只放加密索引，每个文件分块都有自己的临时密钥对，采用 [NIP-44](/zh/topics/nip-44/) v2 HKDF 派生的加密。配套的 Decoupled Encryption Key 事件持有一把云盘范围的对称密钥，每个文件的元数据都以它解密；该提案明确构建在 [NIP-4E](/zh/topics/nip-4e/) 之上，即 fiatjaf 仍未合并的存储抽象草案（[PR #1647](https://github.com/nostr-protocol/nips/pull/1647)，自 2024 年 12 月起开放）。

那把唯一的云盘范围密钥意味着，一旦密钥泄露，暴露的是云盘中每个文件的元数据，而不只是某一个文件，因为按文件的临时密钥对只改变分块加密密钥，并不改变元数据解密密钥；目前除了发布一个新的 Metadata 事件、警告较旧事件可能丢失之外，还没有任何轮换或吊销路径。第二个更狭窄的提案从另一个角度触及同样的 NIP-4E 底层想法：[PR #2361](https://github.com/nostr-protocol/nips/pull/2361) 来自 fiatjaf，专门在 [NIP-17](/zh/topics/nip-17/) 消息内部解耦身份密钥与加密密钥，自 6 月 1 日起开放。两个 PR 都未合并，使这里成为设计空间中一个活跃且存在争议的角落。Form* 表示 Drive 客户端仍是实验性的，更新即将到来。

### 新开：NIP-DA 带权限的私密数据共享

[PR #2411](https://github.com/nostr-protocol/nips/pull/2411) 来自 JAFairweather，是一份新的 NIP-DA 草案，通过带作用域的数据授权实现带权限的私密数据共享。每个用户在 relay 上为每个作用域保留一条加密的权威记录，访问权限则通过在 [NIP-59](/zh/topics/nip-59/) gift wrap 中私密投递该作用域的对称密钥来授予，因此 relay 只存储密文，也永远不会得知谁向谁授予了访问权限；吊销就是一次密钥轮换，无需重写每个使用方的副本。作者将其定位为区别于 [NIP-17](/zh/topics/nip-17/) DM（可以携带数据快照，但无法提供实时更新或吊销）以及 NIP-51 私密列表（不携带密钥材料），并引用了两个独立实现：一个 JavaScript 参考库和一个基于 go-nostr 的 Go CLI，二者已针对 relay.damus.io、nos.lol 和 relay.primal.net 交叉测试。

### 新开：贴纸包 kind 10031 和 30031

[PR #2410](https://github.com/nostr-protocol/nips/pull/2410) 来自 vincenzopalazzo，在 Event Kinds 表中注册 kind 30031（可寻址贴纸包）和 kind 10031（用户的贴纸包列表），并由本周 [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) 推出的「Sonar Stickers」格式规定。这两个 kind 有意排在 [NIP-30](/zh/topics/nip-30/) 自定义 emoji 的 kind 30030 和 10030 上方一位，使客户端不会把贴纸包误认作 emoji 集；贴纸图像字节存放在兼容 [Blossom](/zh/topics/blossom/) 的 HTTPS 服务器上，已发送贴纸的引用携带明文哈希，使经过编辑的可寻址贴纸包无法悄悄改变旧消息中已发送贴纸的外观。一个配套 PR 在独立的 `registry-of-kinds` 项目中注册了相同的 kind。

### 新开：使用 kind:9010 和 kind:39005 的 NIP-29 消息置顶

[PR #2379](https://github.com/nostr-protocol/nips/pull/2379) 来自 Anderson-Juhasc，为 [NIP-29](/zh/topics/nip-29/) 基于 relay 的群组加入消息置顶：kind:9010 `update-pin-list` 是一个审核事件，以 `e` tag 按显示顺序携带完整的置顶事件列表，因此单个事件即可置顶、取消置顶、重新排序或清空置顶集合；kind:39005 则是由 relay 生成的镜像，暴露最新被接受的列表。该设计在收到审阅反馈后，取代了 [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) 中较早的增加/删除成对方案，并选用 kind 编号 9010/39005，因为 9009 和 39003 此后已被 `create-invite` 和群组角色占用。Anderson-Juhasc 同时维护 [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages)，其 [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) 在同一周推出。

### 新开：NIP-66 relay 发现重构

[PR #2241](https://github.com/nostr-protocol/nips/pull/2241) 来自 VincenzoImp，是对 [NIP-66](/zh/topics/nip-66/) relay 发现的一次大幅重构。它用结构化的 Indexed Tags 章节取代了松散的「Other tags include」散文，加入镜像 NIP-11 `attributes` 字段的 `W` tag 以用于 relay 发现过滤，加入使用标准化命名空间（`ISO-639-1`、`ISO-3166-1`、`IANA-asn`、`IANA-tz`、`nip66.label.city`）的 `l` 标签 tag，并把 RTT、SSL/TLS、网络、地理、DNS 和 HTTP 相关 tag 组织到各自的章节中，同时新增一张 Check Types 表。它还修复了字段名错误、缺少 `kind`、检查类型名无效的示例事件，并关闭了 [issue #2171](https://github.com/nostr-protocol/nips/issues/2171)。由于新增的每个 tag 都是可选的，所有变更都保持向后兼容。

---

## NIP Deep Dive：NIP-99 与 Gamma Markets 商务扩展

[NIP-15](/zh/topics/nip-15/) 是最初的 Nostr Marketplace 规范，如今已属遗留：它用一个商家摊位（kind 30017）建模，商品（kind 30018）归档在摊位之下；曾经运行其上的客户端，包括 Shopstr，如今都已转向 [NIP-99](/zh/topics/nip-99/) 分类广告作为活跃规范。NIP-99 本身是单个可寻址事件，活跃广告为 kind 30402，草稿为 kind 30403，不需要先创建摊位。它把广告之外的一切都留作未定义：运费、订单状态、收据、评价，以及把多条广告归入一个店面的方式，恰恰是 NIP-15 中从未延续下来的那些部分。[Gamma Markets](/zh/topics/gamma-markets/) 填补了这一空白，也是今天值得理解的现代商务层。

### NIP-99 留下的空白

NIP-99 广告的 `content` 字段承载 Markdown 描述，`price` 和 `location` 直接位于事件之上，`t` tag 让它像普通话题标签内容一样可被搜索。由于它按 pubkey、kind 和 `d` tag 三元组可寻址，卖家只需发布一个带相同 `d` tag 的新版本即可原地编辑广告：

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

这就是规范的全部：一条签名的、可更新的分类广告。每一个为真实电商而实现 NIP-99 的客户端，只要超出一次性分类广告的范围，最终都会为运费、订单消息和评价发明自己的私有约定。两个 NIP-99 客户端可以各自正确渲染同一条广告，却依然没有共同的方式在彼此之间完成一次结账。

### Gamma Markets：把 NIP-99 略去的部分标准化

Gamma Markets 是一个由 Nostr 市场开发者组成的工作组，即 Shopstr、Cypher、Plebeian Market 和 Conduit Market 背后的团队，为一套构建在 NIP-99 既有 kind 30402 事件之上的共享电商约定所取的名字。该规范通过 [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) 从 NIP-99 的规范文档中链接出去，并在自己的仓库 [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec) 中维护。

Gamma Markets 加入两个与广告相邻的独立 kind。kind 30405 把多条广告归为一个商品合集，通过显式的 `a` tag 引用每一条：

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

kind 30406 定义一个配送选项，带有按国家的定价和可选的按重量或距离计费规则：

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

订单创建、付款请求、状态与配送更新，以及付款收据，全都作为普通的 [NIP-17](/zh/topics/nip-17/) gift-wrap 私密消息传输，按角色分成三个 kind，而不是重新包装传输层：kind 14 承载买家与商家之间的自由沟通，kind 16 承载每一次订单状态转换（`type` tag 取 1 到 4，分别标记订单创建、付款请求、状态更新或配送更新），kind 17 承载买家的付款收据。一条订单创建消息在 gift-wrap 之前是这样的：

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

为已完成的购买评分是另一个独立的可寻址 kind 31555，指回它所评价的广告：

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

让订单消息搭乘 NIP-17 意味着，一次 Gamma Markets 结账使用的是客户端早已为 DM 提供的同一套私密消息传输，而不是一个定制的订单消息 kind。

该规范的核心设计选择是：任何东西都不会向下继承。属于某个合集的广告用 `a` tag 显式引用它，而不是自动继承合集的配送选项或描述；广告所使用的配送选项也以同样显式的方式引用。这是对 NIP-15 摊位模型的刻意反转，在那个模型里，商品会默默继承其父摊位所定义的货币和运费表。代价是每条广告上需要更多显式的 tag，换来的是广告的完整配置始终可以从事件本身读出，无需先解析一个父对象。

### 这在实践中出现在哪里

本周 [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) 的工作正处于 Gamma Markets 所标准化的同一片订单消息领域：[PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) 的临时密钥访客结账，以及 [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) 的商家订单收件箱重建，解决的都是 Gamma Markets 的 kind 14、16 和 17 消息所形式化的买家/商家订单状态问题；Conduit Mono 在这些 kind 之外运行自己的订单状态模型，并未直接采用它们。Shopstr 作为编写该规范的四个项目之一，上周也让自己的商务管道保持推进：[PR #568](https://github.com/shopstr-eng/shopstr/pull/568) 把重复的 NIP-17 gift-wrap 逻辑抽取到一个共享模块，[PR #567](https://github.com/shopstr-eng/shopstr/pull/567) 把其 [NIP-98](/zh/topics/nip-98/) HTTP 认证解析器提升到完整测试覆盖，维护的正是 Gamma Markets 订单流程赖以安全触达买家和商家的消息与认证层。

NIP-15 之所以失去店面这一角色，是因为它标准化了摊位和商品，却把支付、配送、评价和订单状态留给应用去解决。Gamma Markets 填补了其中大部分缺失的接口，且没有触动 NIP-99 的单条广告形态，它构建在 Nostr 既有的 DM 栈 NIP-17 之上，而不是另造一个消息层。

---

本周就到这里。正在构建什么，或有新闻想分享？请通过 NIP-17 DM 联系我们，或在 Nostr 上找到我们。
