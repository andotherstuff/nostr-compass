---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-07-01
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的 Nostr 每周指南。

**本周：** [FIPS v0.4.0](#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul) 带来 Nym mixnet 传输、可选的 mDNS 局域网发现、丢包下无中断换钥与数据平面重构，并与 v0.3.0 线缆兼容。[Whitenoise Linux](#whitenoise-linux-surfaces-as-a-desktop-marmot-client) 以 Rust 与 Slint 编写的桌面 Marmot 客户端亮相，并提出把消息效果移至专用 kind-9 event 的协议提案。[CustID v0.1.10-beta](#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow) 作为硬件保护的移动身份保险库发布，可充当 NIP-46 远程签名器，并通过 NFC 回应实体访问挑战。[myco](#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh) 在 FIPS mesh 上推出点对点 nsite 分享，v0.1.0 新增 BLE L2CAP 传输。[Nostr Codex Phone](#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr) 作为 Android 控制端发布，通过加密 Nostr 私信操控本地 Codex 编程助手。[Amethyst 的未发布分支](#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section) 新增 NIP-89 应用处理器解析、面向 NIP-34 的 Git Repositories 信息流，以及用于 nSite 与 napplet 的 Discover 区域。[Notedeck](#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments) 一周内落地 NIP-37、NIP-52 与 NIP-22。[Applesauce](#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut) 协同发布 12 个子包版本，加入 nbunksec NIP-46 辅助函数并把钱包升级至 Cashu-ts v4。[Meiso v1.4.0](#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing) 在可寻址 kind-35000 上发布 Shared-Key Collaborative Lists。NIPs 仓库合并五个 PR，包括 Relay Roles event、移除 NIP-44 的 65,535 字节限制、NIP-34 分叉语义、NIP-46 客户端元数据与 NIP-86 `signevent` 方法。深度解析涵盖 [NIP-86（中继管理 API）](#nip-deep-dive-nip-86-relay-management-api)与 [NIP-89（推荐应用处理器）](#nip-deep-dive-nip-89-recommended-application-handlers)。

---

## 头条新闻

### FIPS v0.4.0 带来 Nym mixnet 传输、mDNS 发现与数据平面重构 {#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul}

[FIPS](https://github.com/jmcorgan/fips) 是面向 Nostr 的私密、自组织点对点 mesh，节点无需中心基础设施即可相互发现并路由流量。[FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) 加入 Nym mixnet 传输、可选的 mDNS 局域网发现、数据平面重构、丢包下无中断换钥、基于渲染快照测试框架重写的 `fipstop` TUI、移出热路径的可观测性平面，以及新的 OpenWrt apk 与 Nix flake 打包目标；全部与 v0.3.0 线缆兼容，混合版本 mesh 可在滚动升级期间互操作。本次发布以两种新的 peer 发现传输为核心。新的[出站 Nym mixnet 传输](https://github.com/jmcorgan/fips/releases/tag/v0.4.0)通过 `nym-socks5-client` SOCKS5 代理路由 FIPS 流量，把流量混入 [Nym](https://nymtech.net/) 掩护流量网络，使链路层观察者无法关联哪些 mesh peer 正在通信；`examples/sidecar-nostr-mixnet-relay/` 目录则演示一个经 FIPS 链路、端到端跨越 mixnet 抵达的 Nostr 中继。可选的 mDNS / DNS-SD 局域网发现允许同一本地链路上的节点无需地址配置或 STUN 即可相互找到，并在 `node.discovery.lan.enabled: true` 时通过标准服务记录公告与采纳 peer。

数据平面经过重构，可提高单节点吞吐量。每个 peer 的加密与解密现由接收循环之外的专用 worker task 执行，因此一个繁忙 peer 不会串行阻塞整个节点的密码学处理。Linux 发送路径在可用时采用通用分段卸载和已连接 UDP socket，接收热路径避免此前每包发生的缓冲区复制；macOS 新增 `recvmsg_x` 批量接收，与 v0.3.0 中 Linux 的 `recvmmsg` 批处理对应。`fipsctl` 与 `fipstop` 的整个 `show_*` 读取面现在从每 tick 快照提供数据；控制接受 task 将快照发布到无锁 `ArcSwap`，所以即使节点接收循环繁忙，运营者查询也能及时得到响应。新的纯计数器 `show_metrics` 查询（以 `fipsctl stats metrics` 暴露）支持 Prometheus 抓取，且不增加热路径成本。

FMP 与 FSP session 换钥现在双向承受丢包与乱序而不中断：入站 frame 会先针对待定 session 认证，再由 K-bit 切换提升它（因此陈旧或伪造 frame 无法破坏换钥）；换钥 message-1 的重传有明确上限；链路死亡 heartbeat 感知换钥；高延迟链路上的双向同时发起竞争则通过对称抖动错开。`fipstop` TUI 基于渲染快照测试框架重建，用预设控制 socket 输出断言每个视图的精确文字网格与逐 cell 样式。同时新增打包目标：面向 OpenWrt 25+ 的 OpenWrt `.apk`（无需 SDK 构建，复用现有 `.ipk` 交叉编译与已安装文件系统载荷），以及项目根目录的 `flake.nix`，通过固定工具链在 Nix/NixOS 上从源码构建四个二进制文件（`fips`、`fipsctl`、`fips-gateway`、`fipstop`）。

### Whitenoise Linux 作为桌面 Marmot 客户端亮相 {#whitenoise-linux-surfaces-as-a-desktop-marmot-client}

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git) 是桌面 [Marmot](/zh/topics/marmot/) 客户端：通过 Nostr 中继承载 MLS 群组消息，打包为单个 Rust 二进制文件，使用 Slint UI，并把所有秘密保存在一个由密码加密的保险库中。

本周最重要的讨论提议把 Whitenoise 消息效果放入引用父消息的专用 kind-9 event。目前线缆格式会在消息正文末尾附加 `dmfx:sparkle` 一类标记，任何不理解此约定的渲染器都会显示被污染的文本。把效果移入独立 event 可保持消息文字干净，同时也提出整个 Marmot 栈都将面对的设计选择：可选富媒体功能应采用正文内约定，还是 sidecar event。

### CustID 作为带 NIP-46 与 NFC 挑战流程的移动身份保险库发布 {#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow}

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c) 是 CustID 的首个公开 beta。CustID 是基于 Nostr 与 SISTR 协议的移动身份保险库，在硬件保护的安全存储中保存多个 Nostr 身份，可作为其他客户端的 [NIP-46](/zh/topics/nip-46/) 远程签名器，并通过 NFC 与二维码回应实体及在线访问挑战。

此 beta 已完整提供 NIP-46 签名器与 NFC challenge-response 流程；零知识证明访问流程仍是未来里程碑。该版本还移除了应用后台的 [NIP-65](/zh/topics/nip-65/) keep-alive 层。旧层会为每个资料的每个读取中继打开一个 WebSocket，并摄取客户端随即丢弃的 kind。现在后台只保留承载签名请求通知的 NIP-46 socket，这项修复让手机把 CustID 作为其他客户端的 bunker 运行变得可行。

### myco 在 FIPS mesh 上推出点对点 nsite 分享 {#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh}

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0) 于 6 月 27 日开放，并在 7 月 1 日达到 v0.1.0。myco 是一款 Rust Android 应用，可从身边的人安装应用：它在 FIPS mesh 上点对点分享 [nsite](/zh/topics/nip-5a/)，可使用 mesh 承载的任何传输（UDP、TCP、Tor、Bluetooth），并可完全离线工作。设计直接把 FIPS 作为传输底座，把 NIP-5A 的静态网站 event 格式作为载荷，使以 nsite 分发的应用无需依赖中继或 HTTP，即可在 mesh peer 之间移动。

v0.1.0 新增 L2CAP Bluetooth 无线电路径，让两部装有 FIPS 的手机无需任何网络即可通过 BLE 建立 peer；还加入逐 peer speedtest，以及从应用 Circle bottom-sheet 由 NFC 触发的分享。myco 也已发布到 Zapstore，可直接安装。

### Nostr Codex Phone 作为通过 Nostr 操控本地 Codex worker 的移动控制端发布 {#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr}

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone) 本周发布。这款 Android 客户端通过加密 Nostr 私信控制本地 Codex 编程助手 worker。应用支持多个仓库 session、语音转录、路由式 worker session、Blossom 媒体上传与可选语音回答，因此开发者在家运行的 Codex worker 可从任何能连接中继的手机接收指令。

该项目与 #28 中发布的 [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr) 直接同属一类。二者都以加密私信把代理式编程工作流放到 Nostr 传输之上，也都把 Nostr 作为配对与消息层，让手机无需在网络上打洞即可触达家中的 worker。以 Nostr 作为本地 agent 控制平面正成为稳定模式。

### Coop Mobile 发布首批带版本的构建

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1) 与 [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2) 本周发布，是 Coop Mobile 首批带版本的构建。Coop Mobile 是 Android [NIP-17](/zh/topics/nip-17/) 加密私信客户端。两个版本提高消息解析与二维码处理的崩溃安全性，并在登出时清除所有已存数据。

### Amethyst 构建感知 NIP-89 的 UI、Git Repositories 信息流与 napplet Discover 区域 {#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section}

[Amethyst](https://github.com/vitorpamplona/amethyst) 主分支本周构建多个新界面。[Git Repositories 信息流](https://github.com/vitorpamplona/amethyst/pull/3406)把 [NIP-34](/zh/topics/nip-34/) 仓库变成可浏览的 Android 时间线类别，可按社区与作者筛选；配套的 [smart-HTTP git 浏览器](https://github.com/vitorpamplona/amethyst/pull/3415)无需离开应用即可读取仓库内容与 commit。napplet host 新增 [Discover 区域](https://github.com/vitorpamplona/amethyst/pull/3409)，列出策展 web 应用以及用户关注的 nSite 与 napplet，数据来自 [NIP-89](/zh/topics/nip-89/) handler event 和 [NIP-5A](/zh/topics/nip-5a/) site event。笔记显示现通过 NIP-89 tag [揭示 event 由哪个 Nostr 应用创作](https://github.com/vitorpamplona/amethyst/pull/3422)。同步方面，[NIP-77 negentropy 支持](https://github.com/vitorpamplona/amethyst/pull/3434)加入流式 reconciliation，并自动划分 `created_at` 窗口以绕过中继端结果上限，减少大型本地 event 集合与中继保持同步所需带宽。

### Buzz v0.3.38 加固中继攻击面并加入与提供方无关的模型选择

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38) 加固 Buzz 在把 persona、team、托管 agent 与 NIP-OA owner attestation 作为已签名 Nostr event 发布时暴露的[中继攻击面](https://github.com/block/buzz/pull/1369)。Buzz 中继是团队 Nostr 身份及其状态的公开记录，本版收紧 Buzz 定义的 well-known event kind 的输入校验与 replay 防护。该版本也泛化模型选择，使 Buzz team 可指向任何已有适配器的提供方，包括新的 Databricks AI Gateway v2 后端。

### Notedeck 落地 NIP-37 私密同步中继、NIP-52 日历与 NIP-22 评论 {#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments}

[Notedeck](https://github.com/damus-io/notedeck) 是 Damus 团队的原生 Rust 桌面客户端，一周内落地三项协议。私密同步中继现作为 kind `10013` [NIP-37](/zh/topics/nip-37/) 列表持久化，把用户的私密内容中继集合与公开 NIP-65 outbox 分离。`horizon` 日历窗格从 nostrdb 读取 [NIP-52](/zh/topics/nip-52/) event，并获得三栏布局改版。`headway` 窗格加入基于 kind `1111` 的 [NIP-22](/zh/topics/nip-22/) comment-event 模型；NIP-22 把该 kind 定义为取代 NIP-10 回复串联的统一评论界面。

### Applesauce 加入 nbunksec NIP-46 session 与 Cashu v4 钱包升级 {#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut}

[Applesauce](https://github.com/hzrd149/applesauce) 是面向签名器、中继、钱包与内容的模块化 Nostr 工具包，其子包协同发布 [6.2.x 版本](https://github.com/hzrd149/applesauce/releases)。signers 包新增 `nbunksec` 导入与导出辅助函数，把 [NIP-46](/zh/topics/nip-46/) bunker session 当作可在客户端之间迁移的便携工件。wallet 包把 [Cashu](/zh/topics/nip-60/) 绑定升级至 `@cashu/cashu-ts` v4，其中 proof amount 变成 `Amount` value object，token decoding API 也有所变化。

---

## 版本发布

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0) 为 [Mostro](/zh/topics/nip-69/) 点对点法币交易网络带来下一轮协议迭代。该版本接续 [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2)，并与采用新核心的 [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0) 同期发布。核心仓库本周合并三个 PR；外围栈（mostro daemon 与 Mostro mobile）则跟随共享类型 crate 的 v0.14.0。

### ngit v2.6.1

[ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli) 是面向 [NIP-34](/zh/topics/nip-34/) 仓库的权威 git-over-nostr CLI，它实现本周合并的 [NIP-34 GRASP-06 分叉语义](https://github.com/nostr-protocol/nips/pull/2395)：在 repo-state event 上用 `u` tag 取代 `personal-fork` tag。

### mesh-llm v0.72.0 与 v0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm) 是 ContextVM 栈的推理组件，在可由 Nostr 寻址的 JSON-RPC 界面背后运行开源 LLM。项目发布 [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0) 与 [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1)，修复大型单 prompt 的 batching 崩溃，并把 MCP bridge 从弃用辅助函数迁出。

### Meiso v1.4.0 发布 Shared-Key Collaborative Lists，取代 MLS 任务共享 {#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing}

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0) 引入 Shared-Key Collaborative Lists 模型，以更简单的可寻址 event 设计取代项目此前基于 MLS 的任务共享。每个共享列表生成一个分发给成员的专用 Nostr key；任务是 kind `35000` 上以 `d=task-id` 为键的可寻址 event，content 通过 [NIP-44](/zh/topics/nip-44/) 自我加密，中继则对每项任务执行 Last-Write-Wins。该设计放弃 MLS 的前向保密与入侵后安全性，换取更简单的客户端实现及中继层冲突解析。

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn) 发布“more-private-coordinator”路线，从群组消息发布中移除临时发送者 pubkey，并加固加入请求流程，防止陈旧请求重复出现。Cordn 是 [#28 的 Cordn Ad-hoc CVM 发布报道](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator)所介绍的 MLS 消息栈；本版是对应的 coordinator 端更新。

---

## 未发布的变更

### diVine 推进 108 个已合并 PR 的发布后打磨

[diVine](https://github.com/divinevideo/divine-mobile) 是让 Vine 回归的短循环视频客户端，目前正进行密集的发布后打磨。本周可在 Nostr 层看到的工作是 [NIP-46](/zh/topics/nip-46/) 连接流程稳定性改进，把 `nostrconnect://` 失败迁移到结构化 reason code。

### Zap Cooking 延续跨项目 NIP-46 修复与 composer 重构

[Zap Cooking](https://github.com/zapcooking/frontend) 是 Nostr 食谱分享客户端，食谱以长文 Nostr event 发布。本周工作延续跨项目 [NIP-46](/zh/topics/nip-46/) 修复与 composer 重构，此前已在 [#28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes) 作为未发布变更报道。

### Conduit 加固商品发布流程与市场正确性

[Conduit](https://github.com/Conduit-BTC/conduit-mono) 是 Nostr 上含买家市场、商户门户与商店构建器三个应用的市场 monorepo。本周工作延续 [#28 发布报道](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default)中的市场正确性推进，并建立在上一期协议侧主题 [NIP-99](/zh/topics/nip-99/) 商务工作之上。

### Pollerama v1.12 至 v1.13.1 加入 client-tag 选择、资料标签页与线程层级上限

[Pollerama](https://github.com/formstr-hq/nostr-polls) 是专注投票与笔记、并具备强 web-of-trust 发现层的 Android Nostr 客户端，本周在 Zapstore 发布 v1.12.0、v1.13.0 与 v1.13.1。用户现可选择附在自己笔记和投票上的 client tag，可从预设列表选择或自行输入。深度嵌套的评论与回复链在数层后停止，并链接到笔记页面上的完整线程。资料页面默认打开 Notes，并拆分为 Posts 与 Conversations 标签页。新关注账户在应用重启后消失的持久化 bug 已修复，关注按钮也会显示进度。

### getwired.app 与 get-tao.app 修复 NIP-13 confess 提交流程

[getwired.app](https://github.com/smolgrrr/Wired) 与 [get-tao.app](https://github.com/smolgrrr/TAO) 共用匿名发帖流程，在提交时加入 NIP-13 proof-of-work 以抑制垃圾信息。二者修复了 [confess 提交流程](https://github.com/smolgrrr/Wired/pull/57)，使 PoW 挖掘期间的 UX 保持连贯。

### nostui 加入提及时间线标签页

[nostui](https://github.com/akiomik/nostui) 是 Rust 编写的终端 Nostr 客户端，新增[提及时间线标签页](https://github.com/akiomik/nostui/pull/463)，在 TUI 中以专用视图显示标记当前 pubkey 的 kind:1 event。

### Heartwood 落地逐身份 NIP-46 bunker URI 与 HSM 模式签名桥

[Heartwood](https://github.com/forgesworn/heartwood) 是 [NIP-46](/zh/topics/nip-46/) 签名器，签名 key 完全不会到达客户端：客户端通过 NIP-46 与小型中继通信，中继再通过 serial frame 协议与执行签名的外接硬件设备通信。本周项目落地[中继至串口签名桥](https://github.com/forgesworn/heartwood/pull/11)及[逐身份 bunker 连接](https://github.com/forgesworn/heartwood/pull/16)，使一个持有多个身份的硬件设备能为每个身份暴露不同 bunker URI。

### Nostter 认证与签名器重构

[Nostter](https://github.com/SnowCait/nostter) 本周重构[认证与签名器层](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth)，把登录状态移至单一 signal，并将签名器 dispatch 抽取为 strategy module。目标是形成干净的签名器抽象，让 NIP-07 web extension、NIP-46 远程 bunker 与原始 nsec 共用一条代码路径。

### Dart NDK 抽取 NIP-07 签名器并随机化 NIP-59 时间戳

[Dart NDK](https://github.com/relaystr/dart_ndk) 把 [NIP-07](/zh/topics/nip-07/) 签名器从 core 包移到 `ndk_flutter`（Flutter WebView 所在处），并[随机化 NIP-59 gift-wrap 时间戳](https://github.com/relaystr/dart_ndk/pull/667)，提高加密消息抵抗时序关联的能力。

### Milk Market 加入 NIP-23 店面页面与 Square 支付处理

[Milk Market](https://github.com/shopstr-eng/milk-market) 是 Shopstr 团队的市场店面，为每个店面加入由卖家 [NIP-23](/zh/topics/nip-23/) 长文 event 支撑的博客页面，带可编辑区块与直达博客设置的路由。同一周还加入 [Square](https://github.com/shopstr-eng/milk-market/pull/30) 作为卖家的替代支付处理商，并为已付款订单自动购买运输标签。

### Calendar by Formstr 发布 iOS 应用

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) 本周合并 [PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159)，把 [NIP-52](/zh/topics/nip-52/) 日历客户端带到 iOS。[PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197) 修复本地时区下的日历日期解析，[PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201) 则新增由 `run-tests` label 触发的 Playwright E2E workflow。

### cagliostr 执行 NIP-22、按坐标执行 NIP-09，并加入 NIP-13 proof-of-work

[cagliostr](https://github.com/mattn/cagliostr) 是 Go 中继实现，本周收紧三条执行路径：对入站 event 施加[可配置的 NIP-13 proof-of-work](https://github.com/mattn/cagliostr/pull/7)；[按可寻址坐标执行 NIP-09 删除](https://github.com/mattn/cagliostr/pull/8)，使可替换 event 可通过 `a` tag 删除（仅按 event id 删除无法触达）；以及[可配置的 NIP-22 时间戳限制](https://github.com/mattn/cagliostr/pull/9)，拒绝时间戳距离当前过远的 event。

---

## 新纳入追踪与发现的项目

[Vanderwarker wellbeing 套件](https://git.vanderwarker.family/wellbeing)以共用发布者签名 key 把现实世界遥测数据发布为 Nostr event。它包含五款同属一个系列的应用：[Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android) 是计步器，以 `kind:30078` 把健身数据锚定到 Nostr；[Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android) 发布每日手机解锁次数；[Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android) 把当前媒体播放发布为 User Status；[Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android) 每 15 分钟发布电量、电压与温度；[Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android) 发布每日数据用量。五款应用均在 6 月 24 日至 30 日间出现在 Zapstore。

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9) 是以 Rust 与 Slint 构建的加密、无服务器 Android 实时位置分享应用，于 6 月 29 日发布。它与 [Haven](https://github.com/mehmetefeumit/Haven-App) 这款基于 [Marmot](/zh/topics/marmot/) 的位置分享器同属一类，后者曾由 [#28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot) 报道，但二者传输架构不同：ntrack 通过加密 Nostr 私信承载位置更新，Haven 则使用 Marmot 群组消息。

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell) 是用于构建 Nostr 应用的早期 application shell scaffold。项目本周首次发布面向用户的文档。

[NIPs by Pollerama](https://nips.pollerama.fun)（仓库 [abh3po/better-nips](https://github.com/abh3po/better-nips)，创建于 2026-06-29）是面向 [NostrHub](https://nostrhub.io) `kind:30817` 社区编写 NIP 的新客户端，定位为以信任权重排序、替代 nostrhub.io 的界面。每份 `kind:30817` NIP 都有自己的可分享 URL（`#/nip/<naddr>`），可完整渲染 Markdown 并列出其定义的 event kind。客户端提供 Following、Web of Trust（关注者所关注的人）与 Global 三类信息流，每类均可按信任加权批准或最新时间排序。批准以 [NIP-32](/zh/topics/nip-32/) label 发布在 kind `1985` 上，带 tag `["L","nostrhub"]`、`["l","approve","nostrhub"]`、指向目标 NIP 地址的 `a` tag，以及公告 `better-nips` 的 `client` tag。这与 NostrHub 自身签名的 event 形状完全一致，因此两个客户端的批准相互兼容。直接关注者的批准在排序中比二度关注者的批准权重更高。

签名栈使用 [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer)，完整登录 modal 涵盖 [NIP-07](/zh/topics/nip-07/)、[NIP-46](/zh/topics/nip-46/) bunker 与 nostrconnect、[NIP-49](/zh/topics/nip-49/) ncryptsec，以及 [NIP-55](/zh/topics/nip-55/) Android signer，session 会在重载后静默重新连接。网络层通过 [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay) 运行；该 Web Worker 将用户 [NIP-65](/zh/topics/nip-65/) outbox 分配到各中继，使大型 web-of-trust 集合不会扇出到单个中继。其设计立场是，社区 NIP（无论托管于 NostrHub、`better-nips` 还是未来其他客户端）在协议层都完全平等；排序来自社交图谱，而非管理员策展。这与 [#25 深度解析](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling)所介绍的 NIP-32 labeling 流程直接配合。

本周出现两个新的 [NIP-34](/zh/topics/nip-34/) 仓库集群。[Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git) 是视频类 Nostr 客户端；一个 [nostrapps.com 集群](wss://gitnostr.com)发布三个同系列项目：[verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git)（桌面 napp VM）、[hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git)（可定制社区客户端）与 [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git)（HTML microapps 规范与 runtime）。该集群与上期头条报道的 [napplet](/zh/topics/nip-5d/) 工作并行。

---

## 协议工作与 NIP 更新

### 已合并：NIP-44 解除 65,535 字节载荷限制

[PR #1907](https://github.com/nostr-protocol/nips/pull/1907) 自 2024-09 开放后，于 6 月 28 日合并。该变更移除 [NIP-44](/zh/topics/nip-44/) 版本化加密 envelope 的明文载荷 65,535 字节上限，提高到 4 GiB（`uint32_max`）。NIP-44 在线缆格式中以 `uint16` 编码载荷长度，原规范为互操作性严格要求这一点；合并后的变更采用标入 version byte 的更长长度字段，使 v2 实现保持线缆兼容，而 v3+ 实现可携带更长长度。使用 NIP-44 的客户端现可交换大于 64 KiB 的单个 event，无需在应用层拆分；适用场景包括 [NIP-17](/zh/topics/nip-17/) 私信、[NIP-59](/zh/topics/nip-59/) gift wrap、[NIP-46](/zh/topics/nip-46/) 远程签名器载荷及其他 NIP-44 加密 Nostr 消息。

### 已合并：NIP-86 获得 `signevent` 方法与 Relay Roles event

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) 为 [NIP-86](/zh/topics/nip-86/) 中继管理 JSON-RPC API 新增 `signevent` 方法，使管理员可要求中继以自身 pubkey 签署 event。配套的 [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) 定义 Relay Roles event：中继发布的可替换 event，用于声明管理员与版主。二者结合后，NIP-86 客户端可以读取中继管理员列表，并验证已认证请求是否来自当前管理员，无需带外信任。下文将深度解析两项变更。

### 已合并：NIP-34 以 `u` 取代 `personal-fork`，对齐 GRASP-06

[PR #2395](https://github.com/nostr-protocol/nips/pull/2395) 于 6 月 24 日合并，把 [NIP-34](/zh/topics/nip-34/) repo-state event（`kind:30618`）上的 `personal-fork` tag 替换为代表“upstream”的 `u` tag，使线缆格式对齐 GitWorkshop 套件一直实现的 GRASP-06 分叉语义。该变更关闭提出另一种分叉语义修复的 [PR #2384](https://github.com/nostr-protocol/nips/pull/2384)（`NIP-34: remove maintainers to solve expiry issues`）。合并方向由 ngit v2.6.x 实现，因此规范与参考 CLI 现已对齐。使用 `personal-fork` 的既有仓库仍能互操作；新仓库与 ngit v2.6 系列则发布 `u` tag。

### 已合并：NIP-46 客户端元数据（Amber 发货后现已进入上游）

[PR #2381](https://github.com/nostr-protocol/nips/pull/2381) 于 6 月 23 日合并，为 [NIP-46](/zh/topics/nip-46/) `connect` 请求增加可选客户端元数据，使客户端在连接签名器时可发布名称、图标 URL 与主页 URL。[Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) 上周已发布该元数据扩展（见 [#28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata)）；本周上游 NIP 跟上已发货实现。

### 开放：基于 epoch 的确定性 NIP-17 wrapper key

[PR #2397](https://github.com/nostr-protocol/nips/pull/2397) 与 [PR #2396](https://github.com/nostr-protocol/nips/pull/2396) 涵盖两个趋同的 NIP-17 wrap-key 提案。PR #2397 提议从绑定粗粒度时间 epoch 的逐会话 seed，确定性派生用于创作 [NIP-59](/zh/topics/nip-59/) gift wrap 的临时签名 key，使知晓会话 key 的接收方能预测应订阅哪些 pubkey。当前规范要求每个 wrap 使用全新随机 key，无法进行这种预测。PR #2396 是配套变更：给定会话的 wrap 应直接由会话 key 签名，使 wrap pubkey 同时成为会话标识符。二者共同定义可筛选 NIP-17 会话且不泄露元数据的路径。目前都仍开放讨论。

### 开放：NIP-59 应要求中继拒绝 kind:13 seal event

[PR #2399](https://github.com/nostr-protocol/nips/pull/2399) 提议中继在 kind:13 event（[NIP-59](/zh/topics/nip-59/) gift wrap 的内层 seal）作为发布请求顶层对象出现时予以拒绝，因为 seal event 只有置于 wrap 内才有意义，泄漏的 seal 会暴露接收方 pubkey。配套的 [issue #2398](https://github.com/nostr-protocol/nips/issues/2398) 更进一步，主张把 seal 重新定义为临时 kind（NIP-01 的临时 kind 不由中继存储），从协议层加固规则并消除对逐中继策略的依赖。

### 开放：NIP-29 群组状态

[PR #2372](https://github.com/nostr-protocol/nips/pull/2372) 为 [NIP-29](/zh/topics/nip-29/)（基于中继的群组）增加明确群组状态语义，定义群组为开放、关闭、公开、私密或归档时的含义，以及状态转换如何与成员 event 互动。提案把此前由各客户端自行定义的语义纳入中继规范。

### 开放：NIP-34 可选多维护者支持

[PR #2324](https://github.com/nostr-protocol/nips/pull/2324) 是已合并 [PR #2395](https://github.com/nostr-protocol/nips/pull/2395)（上文介绍的 GRASP-06 分叉语义）的配套提案。PR #2324 为 [NIP-34](/zh/topics/nip-34/) repo announcement event（`kind:30617`）增加可选多维护者支持，使仓库可通过重复 `maintainer` tag 声明多个权威维护者 pubkey。客户端随后会把任何已声明维护者签署的 patch 与 issue 信任为官方内容，解决 NIP-34 多维护者仓库长期以来必须让所有内容经一个 pubkey 发布，或退回协议外协调的问题。

### 开放：NIP-91 filter 的 AND 运算符（提案仍开放，尚未合并）

[PR #2252](https://github.com/nostr-protocol/nips/pull/2252) 是 Nostr [filter](/zh/topics/nip-01/) 的 AND 运算符提案，重新开启此前已关闭 [PR #1365](https://github.com/nostr-protocol/nips/pull/1365) 首次讨论的设计。实现已存在于 [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay)、applesauce、[Amethyst](https://github.com/vitorpamplona/amethyst) 与 worker-relay，但规范 PR 本身仍开放。

### 已关闭：四份 pats2sats 商务 NIP

本周关闭四份 Nostr 商务提案：Escrow（[#2334](https://github.com/nostr-protocol/nips/pull/2334)）、Reservations（[#2335](https://github.com/nostr-protocol/nips/pull/2335)）、[NIP-99](/zh/topics/nip-99/) Marketplace Listing Extension（[#2346](https://github.com/nostr-protocol/nips/pull/2346)）与 Accommodation Listing Profile（[#2333](https://github.com/nostr-protocol/nips/pull/2333)）。同一商务界面现正整合到 [Gamma Market Spec](https://github.com/GammaMarkets/market-spec)。这个由项目持有的扩展仓库构建在 NIP-99 市场商品 event 之上，组合订单、结账、托管与争议语义。Compass 现在像追踪 Marmot 与 Blossom 一样，追踪这个位于 NIPs 仓库外部的协议规范仓库。本周其中开放的 PR 包括客户端归属说明（[#11](https://github.com/GammaMarkets/market-spec/pull/11)）、用于商品身份变更的 supersedes tag（[#8](https://github.com/GammaMarkets/market-spec/pull/8)），以及商家评价语义（[#7](https://github.com/GammaMarkets/market-spec/pull/7)）。

### 开放：Bitcoin 身份关联

本周开放两项把 Bitcoin 身份关联到 Nostr 身份的提案：[NIP-352 Bitcoin Silent Payment Address](https://github.com/nostr-protocol/nips/pull/2392) 与 [Bitcoin-OTC Identity Linkage Proof](https://github.com/nostr-protocol/nips/pull/2401)。

---

## NIP 深度解析：NIP-86（中继管理 API） {#nip-deep-dive-nip-86-relay-management-api}

[NIP-86](/zh/topics/nip-86/) 定义中继管理 JSON-RPC 接口，使获授权客户端能通过标准化 API 向中继发送管理命令。单个客户端无需逐中继专用工具，即可管理任何兼容 NIP-86 的中继。本周合并的两项规范变更（[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) 与 [PR #2390](https://github.com/nostr-protocol/nips/pull/2390)）闭合中继签名 event 与中继声明管理员之间的链路。

### 传输

NIP-86 管理请求是发送到中继提供 WebSocket 连接的同一 URI 的 HTTP POST，`Content-Type: application/nostr+json+rpc`。请求正文是以下形式的 JSON 文档：

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

认证使用 `Authorization` header 中的 [NIP-98](/zh/topics/nip-98/) HTTP 认证签名 event。中继会先验证签名 pubkey 位于管理员列表中，再执行方法。中继响应是以下形式的 JSON 文档：

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### 本周之前已有的方法

既有方法集涵盖 pubkey 封禁（`banpubkey`、`allowpubkey`、`listbannedpubkeys`）、event 封禁（`banevent`、`allowevent`、`listbannedevents`）、中继元数据（`changerelayname`、`changerelaydescription`、`changerelayicon`）、允许的 pubkey 列表管理（`allowkind`、`disallowkind`、`listallowedkinds`），以及返回中继统计的 `stats` 方法。其形状刻意接近标准 JSON-RPC 服务，使客户端能在其上构建类型化绑定。

### 本周的变化

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) 为规范增加 `signevent` 方法。该方法接受部分 event 模板（kind、tag、content）作为参数，要求中继签名并返回完整 event，其 `pubkey` 字段使用中继自身 pubkey。这是中继发布自身协议层 event 的前提：被封 pubkey 公告、中继元数据及下文新的 Relay Roles event 都要求中继以运营者控制的 key 签名，但多数中继运营者不愿在管理客户端内持有私钥。

[PR #2390](https://github.com/nostr-protocol/nips/pull/2390) 定义 Relay Roles event：由中继发布的参数化可替换 event kind（通过 `signevent` 以自身 pubkey 签名），用带明确角色语义的方式声明管理员与版主 pubkey。感知 NIP-86 的客户端可从任何已追踪中继抓取 Relay Roles event，从 event tag 构建管理员列表，并验证已认证 NIP-86 请求来自当前管理员，无需带外信任或逐中继配置。两个 PR 合在一起闭合链路：`signevent` 是机制，Relay Roles 是其上的首个 event kind。

### NIP-86 请求示例

完整的 NIP-86 `banpubkey` 请求如下：

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

其 `Authorization` header 携带一个 NIP-98 签名 event：

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

签名 pubkey 必须位于中继管理员集合中（现在由 Relay Roles event 声明）；`u` tag 必须匹配中继 HTTPS URL；`payload` tag 必须匹配 JSON 请求正文的 SHA-256。中继返回：

```json
{
  "result": true,
  "error": null
}
```

### 实现

- [Amethyst](https://github.com/vitorpamplona/amethyst) 在 Android 上提供 NIP-86 中继管理 UI（v1.07.0+）。
- 实现该规范的参考中继包括 [strfry](https://github.com/hoytech/strfry)、[khatru](https://github.com/fiatjaf/khatru)，以及规范 `Implementation Status` 区域链接的若干较小实现。

实现者采纳 `signevent` 与 Relay Roles 变更后，感知 NIP-86 的客户端将开始把 Relay Roles event 当作中继管理员列表的权威来源。

---

## NIP 深度解析：NIP-89（推荐应用处理器） {#nip-deep-dive-nip-89-recommended-application-handlers}

[NIP-89](/zh/topics/nip-89/) 定义两种参数化可替换 event kind：`kind:31990`（应用开发者发布的 application handler）与 `kind:31989`（用户为自己使用的应用发布的推荐）。二者使客户端无需带外协调即可发现可处理未知 event kind 的应用：当长文阅读器遇到自身无法原生处理的 `kind:30030` event 时，可以查询 NIP-89 图谱中的 handler，并为用户提供指向已发布应用的 `Open in...` 流程。NIP-89 是这一跨应用路由问题的原始基础设施，本期出现的 napplet/napps 工作正把它扩展至可组合的 Nostr 原生 applet。

### Application handler event（`kind:31990`）

应用开发者发布一个或多个 handler event，描述应用支持哪些 event kind，以及如何在应用中打开 Nostr 实体：

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

`d` tag 标识 handler（使其可被替换），每个 `k` tag 声明应用处理的一种 event kind，每个平台 tag（`web`、`ios`、`android` 等）给出 URL 模板，其中 `<bech32>` 是调用客户端打开时替换的 [NIP-19](/zh/topics/nip-19/) 编码实体占位符。若多个受支持 kind 共享相同路由模式，一个 handler event 可以公告多个 kind，使应用发现保持紧凑，避免每种 kind 各需一个 handler event。

### 用户推荐 event（`kind:31989`）

用户发布推荐，声明自己针对某种 event kind 使用哪些应用：

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

`d` tag 携带被推荐的 event kind。每个 `a` tag 都是指向 `kind:31990` handler event 的 NIP-01 address pointer，同时给出建议中继及推荐适用的平台。同一推荐可以列出不同平台的多个应用。

### Client tag 与隐私权衡

NIP-89 还定义可选的 `client` tag，任何发布应用都可将其附在自己创作的 event 上：

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

这使显示 event 的客户端可以展示 event 来自哪个应用、查找更丰富的 handler 元数据，并遵守 handler 声明的渲染提示。规范也明确指出隐私成本：若客户端在每个 event 上都发出 `client` tag，就会公开用户的软件身份，长期下来会泄露使用模式。规范建议客户端允许用户选择退出。

Amethyst 的 [PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422) 解析并显示 event 上的 NIP-89 `t`、`i`、`a` 与 `client` tag，直接在时间线中展示笔记由哪个应用创作。

### 实际发现流程

收到未知 event kind 的客户端依次执行以下步骤：（1）在用户关注图谱中查询 `d` tag 与目标 event kind 匹配的 `kind:31989` event。（2）把每个推荐的 `a` tag 解析到其 `kind:31990` handler event。（3）选择 `web`、`ios` 或 `android` URL 模板与当前平台匹配的 handler。（4）将实体的 `bech32` 编码代入 URL 模板。（5）向用户提供所得 URL 作为 `Open in...` 选项。该流程经过社交过滤：若客户端从不可信中继查询任意 handler event，可能会把用户重定向到恶意应用；因此从用户关注的人开始，比把所有已发布 handler 视为同等可信更安全。

### NIP-89 与 napplet 层

Amethyst 的 Discover 区域、napplet-host runtime 与 `client` tag 显示共同在 Android 上构成完整的 NIP-89 消费界面。上期发布的 napplet 规范扩展这些 NIP-89 handler event 可以指向的目标：在 Nostr 与 Blossom 上运行可组合 Nostr 原生 runtime 的 sandboxed applet。NIP-89 是发现与路由图谱；napplet runtime 是它可以指向的一种执行目标。

---

*反馈、勘误或我们遗漏的项目：请在 [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass) 提交 issue，或通过 NIP-17 私信联系 npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923。*
