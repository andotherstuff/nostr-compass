---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Amethyst](https://github.com/vitorpamplona/amethyst) 合并了 29 个 PR，涵盖桌面端 Tor、自定义 C secp256k1、面向 [NIP-AC](/zh/topics/nip-ac/) 的 WebRTC 通话、面向 [Marmot](/zh/topics/marmot/) 的 RFC 9420 MLS 兼容，以及多钱包 NWC。[nstrfy](https://github.com/vcavallo/nstrfy-android) 发布，作为一个使用 kind `7741` events 和 Nostr relays 取代 Firebase 的 Android 推送通知应用。[HAMSTR](https://github.com/LibertyFarmer/hamstr) 加入 Reticulum，从而可以在没有互联网的情况下通过 LoRa mesh 传递 Nostr events。[Bloom](https://github.com/nostrnative/bloom) 发布 [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0)，把完整的 [Blossom](/zh/topics/blossom/) 媒体服务器和 Nostr relay 封装进桌面应用。[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) 以 [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0) 首次亮相，提供基于 Nostr 的互联网广播目录与播放器。[Botburrow](https://github.com/marmot-protocol/botburrow) 开始开发，目标是为 [Marmot](/zh/topics/marmot/) 群聊提供自托管 bot 平台。[Snort](https://github.com/v0l/snort) 连续发布 [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0) 到 [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3)，加入安全审计成果、批量 WASM 验签和重写后的消息系统，而 [Primal Android](https://github.com/PrimalHQ/primal-android-app) 也重新设计了信息流布局。

## 头条

### Amethyst 合并桌面 Tor、C secp256k1、WebRTC 通话和多钱包 NWC

[Amethyst](https://github.com/vitorpamplona/amethyst) 这个由 vitorpamplona 维护的 Android 客户端，本周跨密码学、网络、通话和钱包基础设施一共合并了 29 个 PR。[PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381) 是其中最大的改动，它通过嵌入 kmp-tor daemon 为桌面端加入了 fail-closed 的 Tor 支持，若 Tor 无法启动，应用就会拒绝建立连接。[PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374) 增加了带 JNI 绑定的自定义 C secp256k1 实现，并结合 GLV decomposition、wNAF 点编码以及 x86_64 和 ARM64 上的硬件加速 SHA-256，把 Schnorr 签名验证速度提升到此前纯 Kotlin 路径的 2 到 3 倍。围绕 [Marmot](/zh/topics/marmot/) 的 [PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202) 让其纯 Kotlin MLS 实现符合 RFC 9420，而 [PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203) 到 [PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211) 则构建了完整的 [NIP-AC](/zh/topics/nip-ac/) 语音视频通话栈。与此同时，[PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988) 带来了多钱包 [NIP-47](/zh/topics/nip-47/) 支持，而 [PR #2189](https://github.com/vitorpamplona/amethyst/pull/2189) 还加入了 GIF 转 MP4 和质量滑块。

### nstrfy 为 Android 带来 Nostr 原生推送通知

[nstrfy](https://github.com/vcavallo/nstrfy-android) 于 4 月 13 日发布，并在 [v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0) 到 [v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0) 之间快速迭代。这个应用是 ntfy-android 的分支，但把 HTTP 传输层替换为 Nostr：它不再轮询服务器，而是订阅可配置 relays 上的 kind `7741` events，并将它们显示为原生 Android 通知。它既支持明文载荷，也支持 [NIP-44](/zh/topics/nip-44/) 加密载荷；启用加密时，可通过 [Amber](https://github.com/greenart7c3/Amber) 结合 [NIP-55](/zh/topics/nip-55/) 或本地 nsec 完成签名。应用还能从用户 profile 导入 [NIP-65](/zh/topics/nip-65/) relay 列表，尊重 [NIP-40](/zh/topics/nip-40/) 过期语义，并通过 topic 和 npub allowlist 控制谁可以触发通知。

### HAMSTR 加入 Reticulum，实现经由 LoRa mesh 的 Nostr

[HAMSTR](https://github.com/LibertyFarmer/hamstr) 这个通过业余无线电发送 Nostr events 与 Lightning zaps 的项目，于 4 月 12 日合并了 [PR #10](https://github.com/LibertyFarmer/hamstr/pull/10)，为其传输后端加入 [Reticulum](https://reticulum.network/) mesh 网络。Reticulum 是一种运行在 LoRa、HF、VHF/UHF、串口链路和 TCP/IP 之上的加密 mesh 协议，因此 HAMSTR 现在可以在完全没有互联网基础设施的情况下，借助一组 RNode 设备中继 Nostr events。既有的 AX.25 Packet Radio 和 VARA HF 传输仍然可用，而其 zero-knowledge server 架构也意味着 relay 看不到私钥。[NIP-57](/zh/topics/nip-57/) zap 兼容性则确保离线 Lightning zaps 仍能在 Amethyst 和 Primal 等客户端里正确显示。

## 本周发布

### Bloom v0.1.0 发布自托管 Blossom 服务器和 relay

[Bloom](https://github.com/nostrnative/bloom) 于 4 月 9 日发布首个版本 [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0)。它使用 Tauri v2 和 React 19 构建，把完整的 [Blossom](/zh/topics/blossom/) 协议媒体服务器（BUD-00 到 BUD-10）以及一个 Nostr relay 打包成单个桌面应用，覆盖 macOS、Windows 和 Linux，并计划支持 Android 与 iOS。用户可以获得带 SHA-256 内容寻址、[NIP-94](/zh/topics/nip-94/) 文件元数据支持，以及 `blossom://` URI 解析能力的主权文件存储，而无需自己运维服务器基础设施。

### WaveFunc v0.1.0 和 v0.1.1 发布 Nostr 互联网广播

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) 于 4 月 13 日发布 [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0) 与 [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1)，作为一个基于 Nostr 的互联网广播目录与播放器上线。它使用自定义 kinds 定义数据模型：kind `31237` 用于电台条目、kind `30078` 用于收藏列表、kind `1311` 用于实时聊天、kind `1111` 用于电台评论。项目同时集成了 [NIP-60](/zh/topics/nip-60/) Cashu wallet 与 nutzap 支持，并在 v0.1.1 中加入流派轮播、Lightning 捐赠弹层、认证用户的电台管理以及 Zapstore 上架信息。

### Snort 发布 v0.5.0 到 v0.5.3，加强安全并重做性能路径

[Snort](https://github.com/v0l/snort) 这个基于 React 的 Nostr Web 客户端，从 [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0) 连续发布到 [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3)。最大的 v0.5.0 发布带来了一次全面的安全审计成果，包括真实 Schnorr 签名验证、对伪造 relay 消息的 [NIP-46](/zh/topics/nip-46/) 防护、更强的 PIN 加密，以及移除对未经验证的 [NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md) delegation 的信任。性能方面，它引入批量 WASM 验签、lazy-loaded routes、重写后的优先级 profile 加载器，以及 worker-relay 优化。该系列还加入了面向 [NIP-90](/zh/topics/nip-90/) DVM 的 kind `7000` payment-required 发票显示，而 [PR #620](https://github.com/v0l/snort/pull/620) 则重做了消息系统。

### Primal Android 发布 3.0.21，并重新设计信息流布局

[Primal Android](https://github.com/PrimalHQ/primal-android-app) 发布了 [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21)，修复了投票 zap 投票、多账户共享钱包和 remote signer 自动重连等问题。随后的七个已合并 PR 对主界面布局、feed card 设计、媒体卡片、快速回复输入框和 app bars 做了整体重构。

### Nostria v3.1.19 到 v3.1.21 增加本地图像生成

[Nostria](https://github.com/nostria-app/nostria) 在 [v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19) 到 [v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21) 之间发布了三个版本，核心新增能力是在 WebGPU 加速下使用 Janus Pro 进行本地图像生成，让用户无需外部 API 就能在设备上生成图片。该系列还增加了云端图像生成、多模态聊天、ONNX runtime 支持、AI prompt 库与 AI cache 管理，并对对话框系统、笔记编辑器和音乐嵌入做了改进。

### TubeStr v1.0.3 发布信息流与 studio 更新

[TubeStr](https://github.com/Tubestr/tubestr-v2) 于 4 月 13 日发布 [v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3)。此次更新聚焦信息流与 studio 体验，[PR #3](https://github.com/Tubestr/tubestr-v2/pull/3) 重做了 onboarding，[PR #2](https://github.com/Tubestr/tubestr-v2/pull/2) 修复了视频导出错误。这个面向家庭私密视频分享的应用使用 NDK 与 MDK（[Marmot](/zh/topics/marmot/) Development Kit）来完成加密媒体共享，并计划加入 [Blossom](/zh/topics/blossom/) 作为媒体存储层。

## 开发中

### Botburrow 作为 Marmot bot 平台启动开发

[Botburrow](https://github.com/marmot-protocol/botburrow) 是 Marmot 团队从 4 月 3 日开始的新项目。它是一个自托管 bot 管理平台，每个 bot 都拥有独立的 Nostr 身份，通过 Welcome 消息加入 [Marmot](/zh/topics/marmot/) 的 MLS 加密群聊，并收发端到端加密消息。其基于 Rails 8.1 的 dashboard 通过 Unix socket 与单个 whitenoise-rs daemon（`wnd`）通信，同时还提供脚本、触发器、计划任务、群内实时聊天视图，以及面向 Umbrel 和 Start9 的多架构 Docker 镜像。

### Nostr Archives 增加 trending feeds relay 和实体解析

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api) 在其 Rust API 与 Next.js 16 前端上继续稳定开发。API 侧的 [PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118) 增加了 client leaderboard 的时间范围过滤，[PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117) 则为 reply events 增加了参与度计数。前端的 [PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85) 让站点能够直接从 URL path 解析 Nostr 实体，[PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86) 增加了 API 文档页面。整个平台目前运行四类 relay 服务，包括 NIP-50 搜索 relay、trending feeds relay、scheduler relay 和 indexer relay。

### Damus 修复 favorites timeline

[Damus](https://github.com/damus-io/damus) 合并了 [PR #3708](https://github.com/damus-io/damus/pull/3708)，重写 `subscribe_to_favorites()`，加入原地过滤、去重重建和持久化 tab 选择逻辑。

### Nostur 增加 private zaps 和自定义 emoji 查看

[Nostur](https://github.com/nostur-com/nostur-ios-public) 本周推送了 10 个 commits，增加了 private zap 支持、自定义 emoji 查看、动画 `.webp` 渲染修复，以及语音消息音频格式检测。

### Amber 发布 v6.0.1 到 v6.0.3，加入 WebDAV 备份和 relay 重连修复

[Amber](https://github.com/greenart7c3/Amber) 这个 Android [NIP-55](/zh/topics/nip-55/) signer 在本周连续发布三个版本。[v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1) 增加了 WebDAV 和分享至 Google Drive 两种备份方式、relay 指数退避重连、Quartz 1.08.0 更新，以及 app update 与 profile event 校验修复。[v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2) 增加了 seed words 模式的 account index 选项，并修复了 relay 在启动时离线时的重连问题。[v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3) 则继续修复接收 intents 时空 request ID 的问题。

### Plektos v0.6.0 使用 Ditto 主题重新设计

[Plektos](https://github.com/derekross/plektos) 这个构建在 [NIP-52](/zh/topics/nip-52/) 上、带交互地图的去中心化 meetup 与 events 平台，于 4 月 14 日发布了 [v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77) 和 [v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879)。这次更新引入了 Ditto 风格社区主题、自定义背景图上传、头像形状配置以及整体 UI 重做。[PR #6](https://github.com/derekross/plektos/pull/6) 还解决了一次覆盖安全、架构和 UX 的代码审查发现。

### Shadow 增加 Nostr OS API 和 Cashu wallet 应用

[Shadow](https://github.com/justinmoon/shadow) 在两天内推送了 30 多个 commits。[Commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df) 增加了一个运行在 Shadow runtime 内的 Cashu wallet app，[Commit 865c415](https://github.com/justinmoon/shadow/commit/865c415) 增加了播客播放器 demo。该 runtime 把 `Shadow.os.nostr` 和 `Shadow.os.audio` 暴露为一等 OS 级 API，而 Pixel runtime 通道则在 root 过的 Android 设备上运行 Wayland compositor。

### Lief 修复 Amber 登录并加入 Zapstore

[Lief](https://gitlab.com/chad.curtis/lief) 于 4 月 12 日发布 build `v2026.04.12`，修复了 Android 上 [Amber](https://github.com/greenart7c3/Amber) signer 登录问题，简化了 signer 引导流程，升级了 nostrify 依赖，并加入 Zapstore 集成。

### Espy 重做颜色选择器并修复 Amber 登录

[Espy](https://gitlab.com/chad.curtis/espy) 于 4 月 12 日发布 build `v2026.04.12`，重做了颜色选择器，用弯曲的饱和度弧线替代灰度切换，修复了 hue ring 闪烁，并加入 Easter egg 角色。该版本也修复了 [Amber](https://github.com/greenart7c3/Amber) 登录问题，简化 signer 引导，并加入 Zapstore 集成。

### Jumble 增加按 feed 的 kind 过滤和 Articles tab

[Jumble](https://github.com/CodyTseng/jumble) 本周推送了 13 个 commits，加入按 feed 的 kind 过滤、Articles tab、通知已读状态同步（带隐私保护选项）、头像隐藏模式，以及账号切换竞态条件修复。

### Primal Web 一周内发布 8 次版本更新

[Primal Web](https://github.com/PrimalHQ/primal-web-app) 一周内发布了 3.0.93 到 3.0.101，共 21 个 commits，工作重点是直播聊天改进、mention 边界修复、bookmark 分页、重复点赞防护和 relay proxy 修复。

## 协议与规范工作

### NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)最近的变更：

**已合并：**

- **[NIP-34](/zh/topics/nip-34/)（Git Stuff）：增加 `nostr://` clone URLs**（[PR #2312](https://github.com/nostr-protocol/nips/pull/2312)）：该 PR 为基于 Nostr 托管 git 仓库增加了正式的 `nostr://` clone URL 方案，覆盖直接引用可寻址 event、用 `npub|nip05` 加人类可读仓库标识符，以及带 relay hint 的格式。它已被 Shakespeare、ngit 的 git-remote-nostr helper、GitWorkshop.dev 和 NostrHub.io 采用，并收紧了仓库 `d` tag 的格式。

**开放 PR 和讨论：**

- **NIP-63a：Minimal Payment Gateway Descriptor**（[PR #2315](https://github.com/nostr-protocol/nips/pull/2315)）：提议一种新的 kind `10164` 可替换 event，让内容创作者声明支付网关、定价模型和订阅规则。
- **NIP-XX：Relay Self-Declaration Manifest and Retention Horizon**（[PR #2314](https://github.com/nostr-protocol/nips/pull/2314)）：提议通过 kind `10100` manifest 和新的 `HORIZON` relay-to-client 消息，让 relay 透明地声明端点、保留窗口、写入策略和支持的 NIPs。
- **NIP-TPLD：Transient Private Location Data**（[PR #2309](https://github.com/nostr-protocol/nips/pull/2309)）：提议用临时 kind `20411` 向特定接收方共享经过 [NIP-44](/zh/topics/nip-44/) 加密的地理位置数据，并通过 `ttl` tag 暗示 relay 的保留时间。
- **[NIP-5C](/zh/topics/nip-5c/)（Scrolls）：WASM 程序更新**（[PR #2281](https://github.com/nostr-protocol/nips/pull/2281)）：继续推进 WebAssembly 程序发布和执行规范，并扩展 [NIP-5A](/zh/topics/nip-5a/) 从静态网站走向可执行程序分发。
- **[NIP-44](/zh/topics/nip-44/) 大载荷支持**（[PR #1907](https://github.com/nostr-protocol/nips/pull/1907)）：提议把 [NIP-44](/zh/topics/nip-44/) 的最大载荷限制从当前 65,535 字节扩展出去，以解决远程签名大型 kind `3` 联系人列表时的瓶颈。
- **[NIP-C7](/zh/topics/nip-c7/)：将 kind 9 限制在聊天视图中**（[PR #2310](https://github.com/nostr-protocol/nips/pull/2310)）：要求客户端在渲染“聊天视图”时只抓取 kind `9` events，避免其他内容类型混入聊天时间线导致上下文丢失。

## NIP 深度解析：NIP-29（基于 Relay 的群组）

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md) 定义了一种由 relay 直接管理群组成员关系和审核的消息模型。群组存在于某个特定 relay 上，通过随机字符串 ID 标识，relay 负责决定谁能写入、谁能加入、哪些内容可见。这与 [Marmot](/zh/topics/marmot/) 的客户端侧 MLS 加密群聊，以及 [NIP-17](/zh/topics/nip-17/) 的 gift-wrapped 群聊不同：在 NIP-29 里，relay 是权威，relay 运营者可读消息内容，审核也发生在 relay 层。

群组使用 `<host>'<group-id>` 这样的格式标识，例如 `groups.nostr.com'abcdef`。所有发往群组的用户 events 都带有 `h` tag，而 `previous` tag 则用于做时间线篡改检测，防止消息被脱离上下文地重放到另一个 fork 出来的 relay 副本中。成员关系通过 `9000-9020` 范围的审核 event kinds 管理，管理员可以添加用户、移除用户、编辑元数据、删除事件，也可以通过邀请码机制控制加入流程。群组既可以是公开读写、只读开放，也可以完全封闭和隐藏，具体由元数据中的访问标志组合决定。

NIP-29 的重要特点，是它允许任何 event kind 出现在群组中，而不仅仅是聊天消息。[NIP-23](/zh/topics/nip-23/) 长文、[NIP-52](/zh/topics/nip-52/) 日历事件、[NIP-53](/zh/topics/nip-53/) 直播和市场条目都可以带着 `h` tag 参与群组上下文。因此它更像 Discord server 或 Slack workspace，而不是单一聊天协议。代价也同样清晰：relay 可以看到内容，没有端到端加密，也没有前向保密。对于公共社区和开放讨论空间，这样的 relay-trust 模型通常是可以接受的；对于真正私密的群消息，[NIP-17](/zh/topics/nip-17/) 或 [Marmot](/zh/topics/marmot/) 更合适。

## NIP 深度解析：NIP-90（Data Vending Machines）

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md) 定义了一套“按需计算”协议。客户发布工作请求，服务提供者竞争性地返回结果，而结果和支付反馈都以 Nostr events 的形式流动。规范把它概括为“money in, data out”，其核心思想是把 Nostr 当作一个面向计算和数据处理的市场。

该协议保留 kinds `5000-5999` 用于工作请求、`6000-6999` 用于工作结果，kind `7000` 用于工作反馈。结果 kind 总是比请求 kind 高 1000。请求可带有 `i` tags 指定输入、`param` tags 指定参数、`output` tag 指定输出格式，以及 `bid` 指定可接受的最高支付额。服务提供者返回结果时，会附带原始请求、客户 pubkey，以及可选的 `amount` tag 或 Lightning invoice。kind `7000` 反馈 events 则允许在长任务执行过程中向客户端发出 `payment-required`、`processing`、`error`、`success` 等状态。

NIP-90 的灵活之处，在于它允许工作链式组合。一个请求可以把某个旧 job 的输出当作新的输入，因此像“先转录音频，再总结文本，再翻译摘要”这样的多步流程可以由多个不同的提供者依次完成。若输入敏感，客户还可以把 `i` 和 `param` 数据移入加密 `content` 字段，并用 `encrypted` tag 和提供者 `p` tag 来隐藏 prompts 或源材料。当前生态里，像 [Snort](https://github.com/v0l/snort) 这样的客户端已经能显示 DVM 的 `payment-required` 发票，而 [noStrudel](https://github.com/hzrd149/nostrudel) 和 [DVMDash](https://github.com/dtdannen/dvmdash) 之类工具也在推进服务发现与网络观测。

---

本周就到这里。如果您正在构建新项目，或者有新闻想分享，欢迎在 Nostr 上私信我们，或访问 [nostrcompass.org](https://nostrcompass.org)。
