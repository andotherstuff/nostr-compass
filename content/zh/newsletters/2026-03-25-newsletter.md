---
title: 'Nostr Compass #15'
date: 2026-03-25
translationOf: /en/newsletters/2026-03-25-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Primal Android](https://github.com/PrimalHQ/primal-android-app) 在其 3.0 钱包版本之后继续推进[Follow Packs、zap 增强和 `primalconnect://` 深层链接](#primal-添加-follow-packszap-增强和深层链接)。[BigBrotr](https://github.com/BigBrotr/bigbrotr) 发布了[nsec 泄露分析](#bigbrotr-绘制-relay-网络中的私钥暴露情况)，扫描了 1,085 个 relay 上的 4,100 万个 event，发现 16,599 个有效私钥，而 [npub.world](https://npub.world) 也在同一周把泄露警告集成到了个人资料页面。Martti Malmi 发布了 [nostr-vpn](#nostr-vpn-作为-tailscale-替代方案启动)，这是一个通过 Nostr relay 传递信令并建立 WireGuard 隧道的 Tailscale 替代方案，七天内发布了 11 个版本。[Vector](https://github.com/VectorPrivacy/Vector) 团队将[点对点 DOOM](#开源-doom-通过-nostr-实现点对点运行)开源，[FIPS](https://github.com/jmcorgan/fips) 发布了 [v0.2.0](#fips-v020-发布-tor-传输可复现构建和-sidecar-示例)，[Nostrability Schemata](https://github.com/nostrability/schemata) 则在一周内扩展到了[六种语言](#nostrability-schemata-转向多语言)。

## 新闻

### Primal 添加 Follow Packs、zap 增强和深层链接

[继上周对 3.0.7 的报道之后](/zh/newsletters/2026-03-18-newsletter/)，[Primal Android](https://github.com/PrimalHQ/primal-android-app) 本周继续做发布后的工作，重点放在引导流程、编辑器 UX 和钱包上下文上。重新设计的引导流程引入了 Follow Packs（[PR #949](https://github.com/PrimalHQ/primal-android-app/pull/949)），笔记编辑器加入了原生 GIF 按钮，zap 增强服务（[PR #979](https://github.com/PrimalHQ/primal-android-app/pull/979)）会为钱包交易补充 zap 上下文，而 `primalconnect://` 深层链接协议（[PR #969](https://github.com/PrimalHQ/primal-android-app/pull/969)）则支持跨应用导航。

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) 也通过 TestFlight 并行推出同样的工作，钱包切换（[PR #191](https://github.com/PrimalHQ/primal-ios-app/pull/191)）、投票实现和引导流程重构都在同一时间窗口落地。

### BigBrotr 绘制 relay 网络中的私钥暴露情况

[BigBrotr](https://github.com/BigBrotr/bigbrotr) 这个 Nostr relay 分析平台发布了一篇关于 relay 网络中私钥暴露的[详细分析](https://bigbrotr.com/blog/exposed-nsec-analysis/)。研究扫描了来自 1,085 个 relay 的 4,100 万个 event，搜索嵌在 event 内容中的有效 nsec 字符串，发现了 16,599 个有效私钥。这个数字看起来很惊人，但在过滤掉占匹配结果 92% 的机器人 “Mr.nsec” 之后，真正暴露密钥的真实账户只有 38 个，这些账户的总关注者超过 21,000，而且没有迹象表明他们知道自己的密钥已经公开。

团队还将 nsec-leak-checker 做成了一个 [NIP-90](/zh/topics/nip-90/)（Data Vending Machine）服务，让用户能够在不向检查器泄露私钥的前提下检查自己的私钥是否出现在扫描数据集中。[npub.world](https://npub.world) 在同一周整合了泄露数据，在检测到暴露密钥的个人资料页上显示警告横幅。这个组合既给 DVM 和代理提供了程序化接口，也给普通用户提供了可读的警告。底层数据集还被用于 [BigBrotr v6.4.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.4.0)，该版本增加了可替换和可寻址 event 的物化视图，并修复了同步器空闲超时问题。

### Nostr VPN 作为 Tailscale 替代方案启动

Iris 的作者 Martti Malmi（mmalmi）构建并发布了 [nostr-vpn](https://github.com/mmalmi/nostr-vpn)，这是一个点对点 VPN，使用 Nostr relay 传递信令，并使用 WireGuard（通过 boringtun）建立加密隧道。其动机非常直接：“受够了 Tailscale 需要第三方账户，所以我做了 Nostr VPN。” 这个工具使用 Nostr 密钥对作为身份，在设备之间建立网状网络，不依赖中心协调服务器。

该项目在七天内发布了 11 个版本，从 [v0.2.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.2) 到 [v0.2.13](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.13)。这轮冲刺添加了 Windows 支持、用于本地网络发现的 LAN 配对，以及面向移动设备的 Android sidecar。其架构很简单：两台设备通过 Nostr relay 交换连接元数据，然后建立直接的 WireGuard 隧道。Nostr 负责发现和 NAT 穿透信令，WireGuard 负责实际流量，身份则是一个 Nostr 密钥对。

Malmi 同时还在继续推进 [nostr-double-ratchet](https://github.com/mmalmi/nostr-double-ratchet)，这是一个类似 Signal 的安全消息通道库，并在同一周内从 [v0.0.86](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.86) 发布到 [v0.0.93](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.93)。

### 开源 DOOM 通过 Nostr 实现点对点运行

[Vector](https://github.com/VectorPrivacy/Vector) 团队开源了一个点对点多人 DOOM 实现，它使用 Nostr 做 peer 发现，使用 [Marmot](/zh/topics/marmot/) 做端到端加密，使用来自 n0 的 QUIC 网络库 [Iroh](https://github.com/n0-computer/iroh) 做 gossip 传输。游戏以 4.2 MB 的 WebXDC 文件形式发布，可以作为聊天消息中的附件发送，不需要任何服务器来托管或协调比赛。

技术上，这个实现用实时混合同步模型替代了 1993 年原始的 lockstep 网络代码。玩家通过 Nostr relay 查询彼此发现，通过 Marmot 加密通道协商会话，然后将低延迟游戏流量切换到 Iroh 的 QUIC gossip 层。整个栈里，Nostr 负责发现，Marmot 负责加密，Iroh 负责传输。

Vector 本周还发布了安全加固内容。新版本加入了带有反调试保护和 zeroize 的内存加固密钥库、完整 DM 和群组消息过滤的用户屏蔽，以及针对 Mini Apps 的 WebXDC 实时通道修复。

### FIPS v0.2.0 发布 Tor 传输、可复现构建和 sidecar 示例

[FIPS](https://github.com/jmcorgan/fips) 是 Free Internetworking Peering System，也是一个贴近 Nostr 的网状网络项目，它发布了 [v0.2.0](https://github.com/jmcorgan/fips/releases/tag/v0.2.0-rel)。该版本增加了用于匿名化网状链路的 Tor 传输支持、可复现构建、一个通过 Nostr relay 连接的 sidecar 示例，以及 OpenWrt 包工作流中的 Nostr 版本发布。该版本还修复了 drain-window frame 引发的 rekey 后抖动峰值。由于 wire format 已从 v0.1.0 变更，现有 v0.1.0 节点若不升级将无法与 v0.2.0 互操作。

### Nostrability Schemata 转向多语言

[Nostrability Schemata](https://github.com/nostrability/schemata) 项目维护着用于验证 Nostr event kind 的 JSON Schema 定义，它在一周内从仅 JavaScript 扩展到六种语言。Rust、Go、Dart、Swift 和 Python 的新包都已发布，每种语言都同时提供数据包和验证器。[v0.2.6](https://github.com/nostrability/schemata/releases/tag/v0.2.6) 还新增了 17 个 event kind schema。

[Nostrability 互操作追踪器](https://nostrability.github.io/nostrability/) 也同步完成了一次改造。新的 What's New 标签通过 Atom feed 和 Nostr event 双重发布更新，应用分类过滤允许访问者深入查看特定客户端类型，追踪器现在还会根据 GitHub 仓库元数据自动检测编程语言。Nostrability 现在也有了自己的 npub，使项目本身能通过它所记录的协议被发现。对于跨语言工作的库作者来说，多语言 schema 包意味着同一套 event kind 定义可以作为原生导入使用，而不必由每个项目各自维护一份 schema 副本。

## 版本发布

### Amethyst v1.06.0 and v1.06.1

[Amethyst](https://github.com/vitorpamplona/amethyst) 于 3 月 23 日发布了 [v1.06.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.0) 和 [v1.06.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.1)。最显眼的功能是使用 [NIP-85](/zh/topics/nip-85/)（可信断言）数据进行加权投票的投票支持，同时重新设计了普通投票卡片和 zap 投票卡片。新的渲染方式让标准投票和 zap 加权投票都拥有更清晰的视觉布局。v1.06.1 随后修复了并发修改导致的崩溃，解决了投票渲染路径引入的稳定性回退问题。

### Amber v5.0.0 and v5.0.1

[Amber](https://github.com/greenart7c3/Amber) 这个 [NIP-55](/zh/topics/nip-55/)（Android 签名器应用）签名器，将近期 4.1.x 的预发布工作提升为稳定版，于 3 月 18 日发布了 [v5.0.0](https://github.com/greenart7c3/Amber/releases/tag/v5.0.0)。这个稳定版包含了上周报道的 [NIP-42](/zh/topics/nip-42/) relay-auth、内置 Tor、按内容类型划分的权限以及加密 PIN 存储变更。随后发布的 [v5.0.1](https://github.com/greenart7c3/Amber/releases/tag/v5.0.1) 则从离线构建变体中移除了 internet 权限，使该构建在 Android 权限层无法再发起网络请求。

### Mostro v0.17.0 and Mostro Mobile v1.2.2

[Mostro](https://github.com/MostroP2P/mostro) 这个构建在 Nostr 上的点对点 Bitcoin 交易所，于 3 月 18 日发布了 [v0.17.0](https://github.com/MostroP2P/mostro/releases/tag/v0.17.0)。服务器版本延续了 v0.16.x 周期中的争议和评分工作，为买卖双方增加了更完整的交易信誉数据，并将其作为 Nostr event 发布。[Mostro Mobile](https://github.com/MostroP2P/mobile) 这个 Flutter 客户端则在 3 月 23 日跟进发布了 [v1.2.2](https://github.com/MostroP2P/mobile/releases/tag/v1.2.2)，保持移动界面与最新协议变更同步。

### Shosho v0.14.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases) 这个 Nostr 直播应用于 3 月 19 日发布了 [v0.14.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.14.0)，并同时推出了 Shosho Shop。这个版本在个人资料页添加了 Shop 标签页、在 Browse 中加入 Shop，并在直播和剪辑中加入 In-Live Shop 按钮。发布说明称现有的“Nostr products”会自动显示，买家点击后会跳转到卖家的 Plebeian Market 页面购买。Shosho 的发布说明没有指明使用的列表 event kind，因此目前还无法确认 Shosho Shop 是否读取了 [Shopstr](https://github.com/shopstr-eng/shopstr) README 中明确支持的同一套 [NIP-99](/zh/topics/nip-99/) 分类列表。

### Applesauce v5.2.0

[Applesauce](https://github.com/hzrd149/applesauce) 是 hzrd149 为构建 Nostr 应用维护的一组辅助包集合，它在 3 月 22 日发布了 [v5.2.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core@5.2.0)。这个版本跨越六个包。SQLite 包修复了 event tag 上的 UNIQUE 约束冲突问题，该问题会导致重复插入。signers 包增加了 `AndroidNativeSigner`，将 [NIP-55](/zh/topics/nip-55/) 原生 Android 签名器接口封装起来，使基于 web-view 的应用无需自定义 bridge 代码就能使用硬件支持签名。relay 包在 relay 和池状态对象中增加了 `challenge` 字段，用于追踪 [NIP-42](/zh/topics/nip-42/) auth 状态，让应用在 relay 请求认证时能以编程方式响应。core 包增加了 `isEventPointerSame` 和 `isAddressPointerSame` 方法，用于去重 event 引用，common 包则增加了 `user.blossomServers$`，用于解析用户的 Blossom 媒体服务器。Applesauce 为 noStrudel、Satellite 和多个 Web 客户端提供支撑，因此这些修复会传播到整个 Web 客户端层。

### Wisp 一周内发布 16 个版本

[Wisp](https://github.com/barrydeen/wisp) 这个 Android Nostr 客户端本周从 [v0.9.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.9.3-beta) 一直发布到 [v0.13.1-beta](https://github.com/barrydeen/wisp/releases/tag/v0.13.1-beta)，共计 16 个版本。新增功能包括多账户支持、降低打扰的 zen 通知模式、草稿和定时发帖、安全内容过滤以及新的 flame 图标。

### Manent v1.2.0

[Manent](https://github.com/dtonon/manent) 这个私密加密笔记和文件存储应用于 3 月 20 日发布了 [v1.2.0](https://github.com/dtonon/manent/releases/tag/v1.2.0)。该版本增加了应用内直接拍照、上传前缩放图片以降低存储成本，以及查看已存图片时的双指缩放。Manent 使用用户的密钥对将笔记和文件加密后存储在 Nostr relay 上，因此手机或桌面应用只是一个可以从 relay 数据重建全部状态的薄客户端。

### diVine 1.0.7

[diVine](https://github.com/divinevideo/divine-mobile) 这个短视频客户端于 3 月 21 日发布了 [1.0.7](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.7)，增加了在视频卡住时自动恢复播放的 watchdog。在 [v1.0.6](/en/newsletters/2026-03-11-newsletter/#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import) 中加入 E2E 测试基础设施和直接 MP4 加载之后，这个版本针对的是剩下的那条播放失败路径：视频中途停止但不抛出错误。

### Alby Extension v3.14.2

[Alby Extension](https://github.com/getAlby/lightning-browser-extension) 这个 [NIP-07](/zh/topics/nip-07/)（浏览器扩展签名器）扩展于 3 月 18 日发布了 [v3.14.2](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.2)，增加了 Lightning 地址二维码显示和 Schnorr 签名支持。Schnorr 的加入使浏览器扩展与 Nostr 原生使用的 secp256k1 签名方案保持一致。

### NoorNote v0.6.5 through v0.6.11

[NoorNote](https://github.com/77elements/noornote) 这个记笔记应用从 [v0.6.5](https://github.com/77elements/noornote/releases/tag/v0.6.5) 到 [v0.6.11](https://github.com/77elements/noornote/releases/tag/v0.6.11) 发布了七个版本。最重要的新内容是 Follow Packs，也就是经过策展的账户集合，用户可以批量浏览和订阅，类似 Twitter Lists，但专门为引导流程设计。用户可以创建、编辑和分享带有自定义标题、描述和封面图的 Follow Packs。这一系列版本还将底层 Nostr 库从 NDK v2 升级到 v3，从而改进 relay 连接处理和订阅管理。图片笔记和重新设计的 relay 连接体验也构成了这轮更新的一部分。

### nak v0.19.1 and v0.19.2

[nak](https://github.com/fiatjaf/nak) 是 fiatjaf 的命令行 Nostr 工具包，用于与 relay 交互、编码和解码 [NIP-19](/zh/topics/nip-19/)（Bech32 编码实体）标识符、签署 event 以及查询 relay 数据。它于 3 月 17 日和 20 日发布了 [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1) 和 [v0.19.2](https://github.com/fiatjaf/nak/releases/tag/v0.19.2)。这两个小版本延续了上周 [v0.19.0](/zh/newsletters/2026-03-18-newsletter/) 中加入的群组论坛 UI 工作。

### Calendar by Form* v0.2.1

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) 这个基于 [NIP-52](/zh/topics/nip-52/)（日历事件）构建的去中心化日历应用，于 3 月 20 日发布了 [v0.2.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.1)。这个版本修复了影响事件提醒的通知模板问题。Calendar 将事件存储为 Nostr kind 31922（按日期）和 kind 31923（按时间）event，因此任何愿意支持这些 kind 的 Nostr 客户端都可以渲染日历数据。该应用由 Formstr 团队构建，他们也维护 Formstr（去中心化表单）和 Pollerama（投票）。

### NYM v3.50 through v3.53

[NYM](https://github.com/Spl0itable/NYM) 这个与 Bitchat 桥接的轻量级短暂聊天客户端，从 v3.50 到 v3.53 共发布了 28 个版本（补丁版本号增长很快）。其中最值得注意的功能是 Nymbot，它是一个内置聊天机器人，会响应频道中的 `@nymbot` 提及，并提供 relay 状态和管理功能。“hardcore mode” 会为每条发出的消息生成一个全新的密钥对，使会话线程在身份层面无法关联。权衡也很清楚：你失去了持久身份，但获得了按消息粒度的匿名性。relay 代理层本周也有工作推进，包括分片 relay 代理 worker 以提升连接性、geohash 频道支持以及对系统时钟不精确节点的时钟偏差容忍。

## 项目更新

### Ditto 添加 Bluesky 桥接和 Wikipedia 集成

[Ditto](https://github.com/soapbox-pub/ditto) 是 Soapbox 团队可定制的 Nostr 社交客户端，本周在三个不同功能方向上记录了 300 多次提交。第一条线是 Bluesky 桥接（19 次提交），它将 Bluesky 帖子以内联完整信息流线程的方式渲染出来，在侧边栏加入由官方 Discover（whats-hot）信息流支撑的 Bluesky 发现页面导航，并接入评论、分享、反应和复制链接等操作按钮。当用户在 Ditto 中回复 Bluesky 帖子时，编辑弹窗会显示免责声明，提示该交互具有跨协议性质。[NIP-73](/zh/topics/nip-73/)（外部内容 ID）的 kind 17 反应支撑了这种跨协议模型：Nostr 用户对 Bluesky 帖子做出反应，而该反应会被存储为一个引用外部内容标识符的标准 Nostr event。这也是同一种 NIP-73 模式，可以桥接任何外部内容的反应，从 Bluesky 帖子到 YouTube 视频再到网页。

第二条线是 Wikipedia 集成（9 次提交）。Ditto 现在会在详情页渲染丰富的 Wikipedia 文章内容，而不是通用链接预览，加入带文章缩略图的搜索自动补全，并提供一个 `/wikipedia` 页面，从 Wikipedia API 拉取精选内容。Wikipedia 和 Archive.org 的结果也会出现在通用搜索自动补全下拉菜单中。第三条线是通过 Capacitor 提供 iOS 平台支持，远程构建脚本和平台配置与一次 UI 大改同时落地（55 次提交），用新的基于弧线的导航设计替换了应用所有页面的毛玻璃头部。总计 314 次提交推动 Ditto 从纯 Nostr 客户端走向一个多协议聚合器，将 Bluesky 和 Wikipedia 与 Nostr 信息流并列为一等内容源。

### Pika 构建 NIP-34 forge CI 管道

[Pika](https://github.com/sledtools/pika) 这个基于 Marmot 的加密消息应用，本周合并了 33 个 PR，重点围绕一个带有合并前 CI 的自托管 [NIP-34](/zh/topics/nip-34/) forge。这个 forge 是一层 git 托管系统，它将补丁作为 NIP-34 event 接收，在合并前运行 CI 检查，并通过 Nostr event 回传结构化状态。[PR #701](https://github.com/sledtools/pika/pull/701) 加入了基于 lane 的合并前和 nightly CI，其中 Rust、TypeScript、Apple 构建等各条代码路径在各自 lane 中独立运行，并各自给出通过或失败状态。[PR #715](https://github.com/sledtools/pika/pull/715) 将托管 CI 代理切换为 Incus OpenClaw 容器以实现隔离，[PR #733](https://github.com/sledtools/pika/pull/733) 则增加了 `ph forge` CLI，用于从命令行与托管 forge 交互。配套 PR 还处理了合并所需的仓库写权限（[PR #736](https://github.com/sledtools/pika/pull/736)）、带实时状态徽章的结构化 CI 元数据（[PR #722](https://github.com/sledtools/pika/pull/722)）、Apple nightly 构建拆分（[PR #738](https://github.com/sledtools/pika/pull/738)），以及 forge 认证和分支查找修复（[PR #734](https://github.com/sledtools/pika/pull/734)）。这是首批真正建立在 NIP-34 git event 之上的可运行 CI/CD 系统之一，使基于 Nostr 的源码托管从基础补丁交换迈向开发者在 GitHub 或 GitLab 上习惯的合并加测试工作流。

### Nostria 添加社区、代码片段和语音 event 处理

[Nostria](https://github.com/nostria-app/nostria) 由 sondreb 维护，是一个跨平台 Nostr 客户端。本周它继续扩展应用界面，超越了 #14 中报道的 Web of Trust 过滤。最主要的新增内容是完整的 [NIP-72](/zh/topics/nip-72/)（审核社区）实现，包括社区创建、审核员和 relay 配置、带图片预览的帖子审批跟踪，以及包含 Posts 和 Moderators 标签页的专用社区页面。

同一段开发还加入了带语法高亮编辑器的代码片段渲染和编辑、用于音频会话的语音 event 回复支持、私信的聊天 relay 设置、通过 Web Share API 进行频道分享、媒体播放器的工具栏停靠系统、最新版 Brainstorm Web of Trust 服务的应用内注册、使用 NWC 和 BOLT-11 发票在 DM 中收发资金、Nostr 原生 GIF 处理，以及更强的音乐人 RSS 导入路径，可以从播客 feed 中继承现有 Lightning 分成。

### nostr-vpn 快速迭代

除了[最初的发布](#nostr-vpn-作为-tailscale-替代方案启动)之外，[nostr-vpn](https://github.com/mmalmi/nostr-vpn) 的提交记录揭示了真实部署中遇到的具体问题。[v0.2.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.3) 到 [v0.2.5](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.5) 加入了初始安装脚本和跨平台 CLI。[v0.2.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.6) 和 [v0.2.7](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.7) 带来了 Windows 支持，这要求为配置写入处理 UAC 路径引用，并支持由守护进程持有的配置更新。[v0.2.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.8) 到 [v0.2.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.10) 修复了 Windows GUI 服务动作、CLI 子进程处理以及机器范围的服务配置。[v0.2.12](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.12) 用定时 LAN 配对替代了 LAN 发现，这是一种用户主动发起的流程，让同一本地网络中的两台设备无需 relay 信令就能完成配对。这是非常典型的早期实地测试模式：每个版本都针对一个具体部署故障，用户群足够小以支持日更迭代，而开发者本人也在各版本之间实际使用这个工具。

### Comet 自动化构建

[Comet](https://github.com/nodetec/comet)（前身为 Captain's Log）是 Nodetec 的 Nostr 原生长文写作工具，本周产出了 40 多个自动化 alpha 构建。Comet 是一个桌面应用，用于编写和发布 NIP-23（长文内容）文章，支持本地草稿存储、Markdown 编辑和一键发布到用户的 relay 集合。自动化构建管道会为 main 分支上的每次提交生成一个带 tag 的版本，这使原始发布数量不能直接作为功能迭代速度的衡量指标。40 个构建真正说明的是：该应用处于持续的日常活跃开发中，每次提交都会在几分钟内被测试、打包并提供下载。

## NIP 更新

3 月 17 日至 24 日期间 [NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

3 月 18 日到 3 月 24 日之间没有新的 NIP 合并。

**窗口期内更新的开放 PR 和讨论：**

- **NIP-AA：Nostr 上的自主代理**（[PR #2259](https://github.com/nostr-protocol/nips/pull/2259)）：提出自主代理在 Nostr 网络上运行的约定。该 PR 定义了代理如何标识自己、发现服务，以及通过 Nostr event 与其他代理和人类协调。

- **[NIP-50](/zh/topics/nip-50/)（搜索）：排序扩展**（[PR #2283](https://github.com/nostr-protocol/nips/pull/2283)）：为 NIP-50 搜索查询增加排序参数，包括 top、hot、zaps 和 new。这将允许客户端直接从支持全文搜索的 relay 请求排序结果，而不是在客户端侧再排序。

- **NIP-A5：WASM 程序**（[PR #2281](https://github.com/nostr-protocol/nips/pull/2281)）：提出一种在 Nostr 上发布和发现 WebAssembly 程序的约定。WASM 二进制可以作为 Nostr event 分发，而 relay 则作为可移植可执行代码的发现层。

- **NIP-CF：Combine Forces 可互操作 napps**（[PR #2277](https://github.com/nostr-protocol/nips/pull/2277)）：定义可互操作的 Nostr 应用（“napps”）约定，使其能够跨不同客户端和服务进行功能组合。

- **Snapshots NIP**（[PR #2279](https://github.com/nostr-protocol/nips/pull/2279)）：提出一种 relay 状态快照机制，用于 relay 同步和备份。

- **Checkpoints NIP**（[PR #2278](https://github.com/nostr-protocol/nips/pull/2278)）：提出用于标记已知良好 relay 状态的 checkpoint event，作为 snapshots 提案的补充。

- **[NIP-58](/zh/topics/nip-58/)（徽章）：Badge Sets 重构**（[PR #2276](https://github.com/nostr-protocol/nips/pull/2276)）：重构徽章集合的组织和引用方式。

- **[NIP-11](/zh/topics/nip-11/)（Relay 信息文档）：扩展**（[PR #2280](https://github.com/nostr-protocol/nips/pull/2280)）：为 relay 信息文档增加额外字段，以提供更丰富的机器可读 relay 元数据。

## Nostr 五年三月回顾

[上个月的周刊](/zh/newsletters/2026-03-04-newsletter/#five-years-of-nostr-februaries) 回顾了 Nostr 的各个二月如何从 NIP-01（基本协议流程）重写，推进到 Damus App Store 浪潮，再到网状网络和代理提案。本次回顾追踪 2021 年到 2026 年每一个三月发生的事情。

### March 2021: Two Commits

Nostr 诞生四个月后的那个三月，协议仓库里总共只有两次提交，而且都发生在 3 月 4 日。fiatjaf [添加了 nostwitter 实例链接](https://github.com/nostr-protocol/nostr/commit/dcd8cc3)，把早期访问者指向可用部署；同时又[在基础过滤器定义中加入了 kind](https://github.com/nostr-protocol/nostr/commit/54dfb46)。第二个提交很能说明问题：在 2021 年 3 月，Nostr 甚至还不能按 kind 过滤 event。协议当时就是这么原始。整个网络只有两三个 relay，Telegram 群组是唯一协调渠道。NIPs 仓库尚不存在，协议提案还只是主 nostr 仓库中的文件。那个月唯一的提交者就是 fiatjaf。支持 VPN、多人游戏和网状网络的协议，在五年后的复杂形态，其 2021 年 3 月的全部产出还装得进一个 git diff。

### March 2022: Pre-Damus Building

2022 年 3 月，主协议仓库没有任何提交，开发已经完全转移到工具仓库。[Branle](https://github.com/fiatjaf/branle) 是 fiatjaf 的 Vue.js Web 客户端，当时也是主要 Nostr 界面，在那个三月有 5 次提交，包括 Docker 部署支持，以及 [NIP-05](/zh/topics/nip-05/)（基于 DNS 的验证）显示名修复，去掉了验证徽章中的 `_@` 前缀。Robert C. Martin 的 [more-speech](https://github.com/unclebob/more-speech) 这个 Clojure 桌面客户端记录了 13 次或更多提交，加入了线程、键盘导航和编辑窗口。那个月最著名的 Nostr 开发者并不是加密领域人物，而是那位《Clean Code》销量数百万册的软件作者，用 Clojure 写了一个 Nostr 客户端。这个语言选择足以说明早期社区的气质：那是一群带着强烈偏好的程序员，为自己构建工具。

当时 relay 网络扩展到大约 15 个 relay，活跃用户规模大致在几百人。Damus 还不存在，要到 2022 年 4 月才会创建。Nostream 也尚未出现。那个月的重点是基础设施：让已经被这个小社区日常使用的工具更可靠。

### March 2023: Post-Explosion Infrastructure

在 Damus App Store 浪潮以及公钥数突破 30 万之后的一个月，2023 年 3 月的主题是吸收增长。[NIPs 仓库](https://github.com/nostr-protocol/nips) 合并了 28 个 PR，是协议历史上第二高的月度数量。[NIP-51](/zh/topics/nip-51/)（列表）合并，为客户端提供结构化的关注、静音和书签集合；[NIP-39](/zh/topics/nip-39/)（个人资料中的外部身份）落地；NIP-78（应用特定数据）为需要私有状态的应用提供了通用存储 kind；而 [NIP-57](/zh/topics/nip-57/)（Lightning Zaps）的重写（[PR #392](https://github.com/nostr-protocol/nips/pull/392)）则整合了 zap 流程并澄清了术语。那个月讨论最多的 PR 是一个替代 mention 处理方案（[PR #381](https://github.com/nostr-protocol/nips/pull/381)），评论超过 50 条。

当月最具影响力的新项目是 [NDK](https://github.com/nostr-dev-kit/ndk)（Nostr Development Kit），这是一个 TypeScript 库，负责 relay 连接、event 签名、缓存和订阅管理。pablof7z 于 2023 年 3 月 16 日做了[首次提交](https://github.com/nostr-dev-kit/ndk/commit/09e5e03)，11 天后的 3 月 27 日又从头重写了一遍（“basically another initial commit”），并在 3 月 31 日前让 LNURL 和 zap 支持可用。NDK 在 15 天里从零走到可支持 zap。就在 NDK 创建五天后，3 月 21 日，Alby 团队创建了 [NWC](https://github.com/getAlby/nostr-wallet-connect)（Nostr Wallet Connect），这是 [NIP-47](/zh/topics/nip-47/) 的参考实现，用于将 Lightning 钱包连接到 Nostr 应用。接下来三年 Web Nostr 开发的两大基础项目，就在同一个 30 天窗口里诞生。OpenSats 的 Nostr 资助计划当时还未启动，第一波要等到四个月后的 [2023 年 7 月](https://opensats.org/blog/nostr-grants-july-2023)。

同月其他值得注意的新项目还包括 NostrGit、NostrChat、LNbits 的 nostr-signing-device 项目和 nostrmo。[Gossip](https://github.com/mikedilger/gossip) 这个专注智能 relay 选择的 Rust 桌面客户端则发布了三个版本。当时的协议处于全面建设阶段，而 2023 年 3 月创造的这些工具在三年后仍在使用。

### March 2024: Protocol Maturation

2024 年 3 月的主题是为协议的长期使用做加固。[NIPs 仓库](https://github.com/nostr-protocol/nips) 合并了 12 个 PR，其中最重要的是 [NIP-34](/zh/topics/nip-34/)（Git Stuff），也就是 [PR #997](https://github.com/nostr-protocol/nips/pull/997)。它在经过 44 天审查和 130 多条评论后于 3 月 5 日合并。那条讨论串像一个时间胶囊，记录了社区如何争论去中心化 GitHub 应该怎么做。jb55 将其类比为 `git send-email`，Giszmo 提议使用根提交哈希做跨 fork 发现（“something GitHub doesn't do and we could”），mikedilger 建议使用 [NIP-98](/zh/topics/nip-98/)（HTTP Auth）事件签名认证代替 SSH 密钥，而 fiatjaf 则直截了当地否定了支持通用版本控制系统的必要性：“不是每个版本控制系统，只要 git。没人用别的。” PR 打开数小时内，fiatjaf 就已经让 nak、go-nostr 和 gitstr 支持通过 Nostr 接收补丁。DanConwayDev 也是讨论中最活跃的参与者之一，他的 ngit 当时已是 OpenSats 资助项目。那个时期还合并了一个用于个人资料元数据的 bot 字段，使客户端能以机器可读方式区分自动化账户和人工账户。

[Amethyst](https://github.com/vitorpamplona/amethyst) 发布了 v0.85.0，在一个版本中同时加入 git event 支持、wiki 文章、医疗数据渲染和内容编辑。[Mostro](https://github.com/MostroP2P/mostro) 达到了 v0.10.0。[Nosflare](https://github.com/Spl0itable/nosflare) 这个运行在 Cloudflare Workers 上的无服务器 Nostr relay 证明了 relay 逻辑可以在边缘运行。OpenSats 还向 Bruno Garcia 发放了[长期支持资助](https://opensats.org/blog/bruno-garcia-receives-lts-grant)，以支持他持续贡献 Amethyst 客户端。

### March 2025: Infrastructure Expansion

2025 年 3 月共产生 10 个已合并 NIP。最重要的是 [NIP-66](/zh/topics/nip-66/)（relay 发现与活跃性监控），也就是 [PR #230](https://github.com/nostr-protocol/nips/pull/230)，它在经过长达 25 个月的历程后于 3 月 3 日合并。dskvr 在 2023 年 2 月首次提出 relay 监控，被告知这可以在客户端侧完成；随后他解释了为什么单个客户端同时连接数千个 relay 并不现实，经历了七次完整草稿重写，在八个地理区域（美国东北、巴西、美国西部、美国东部、澳大利亚、印度、韩国、南非）构建了监控节点，并等待 relay 工具链跟上。等到它合并时，nostr.watch、relaypag.es、monitorlizard、Snort、noStrudel 和 Jumble 中都已经有实现。NIP-66 数据后来成为 Nostrability outbox 基准测试的燃料，[我们在周刊 #12 中已报道](/zh/newsletters/2026-03-04-newsletter/#outbox-model-under-the-microscope)。NIP-C0（代码片段）也在当月合并（[PR #1852](https://github.com/nostr-protocol/nips/pull/1852)，63 条评论），引入了 kind 1337 事件用于分享源代码。

Nostr 上最早的 MCP 服务器也在这个月出现。[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server) 于 3 月 23 日出现，[nwc-mcp-server](https://github.com/getAlby/nwc-mcp-server) 于 3 月 14 日出现，距 Anthropic 在 2024 年 11 月宣布 Model Context Protocol 仅过去四个月。这些早期桥接先于后来在 2025 年末和 2026 年初出现的完整 [ContextVM](/zh/topics/contextvm/) SDK 和代理商业化工作。

[Gossip](https://github.com/mikedilger/gossip) 发布了 v0.14.0。[Coracle](https://github.com/coracle-social/coracle) 这个 hodlbod 的 Web 客户端支持 relay 感知的信息流管理，也发布了三个版本。OpenSats 则宣布了其[第十波 Nostr 资助](https://opensats.org/blog/10th-wave-of-nostr-grants)，延续了自 2023 年中以来一直运行的资金支持管道。

### March 2026: Convergence

*2026 年 3 月的活动摘自 Nostr Compass 第 [#12](/zh/newsletters/2026-03-04-newsletter/) 期至 [#15](#) 期（本期）。*

2026 年 3 月是多个分散线程汇聚成可运行系统的一个月。[Marmot Development Kit](/zh/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release) 发布了首个公开版本，包含加密媒体、多语言绑定以及需要在规范、Rust 和 TypeScript 三方协调更新的 ChaCha20-Poly1305 迁移。[Shopstr 和 Milk Market](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces) 增加了面向代理采购的 MCP 商业接口。[NIP-42](/zh/topics/nip-42/) relay auth 同时落地到 [Amber](/en/newsletters/2026-03-11-newsletter/#nip-42-relay-auth-across-bunker-signer-and-relay)、strfry 和 OAuth Bunker，闭合了签名器、relay 和 bunker 软件之间的回路。[Notedeck](/zh/newsletters/2026-03-18-newsletter/#notedeck-将版本发现迁移到-nostr) 则使用 [NIP-94](/zh/topics/nip-94/)（文件元数据）版本 event 发布了 Nostr 原生软件更新。

本周，[BigBrotr](#bigbrotr-绘制-relay-网络中的私钥暴露情况) 扫描了整个 relay 网络中的泄露私钥，并同时发布了分析和 DVM 检查器。[Nostr VPN](#nostr-vpn-作为-tailscale-替代方案启动) 证明了 Nostr 的密钥模型不仅适用于社交媒体，也适用于网络基础设施。[DOOM](#开源-doom-通过-nostr-实现点对点运行) 证明了 Nostr 发现、Marmot 加密和 QUIC 传输可以支撑实时多人游戏。[Amber](#amber-v500-and-v501) 跳到了 v5.0.0。[Wisp](#wisp-一周内发布-16-个版本) 在七天内发布了 16 个版本。一周之内，主要项目就贡献了 25 个以上带 tag 的版本发布。

本月前 24 天里已有 7 个 NIP 合并。协议增加了 [NIP-54](/zh/topics/nip-54/)（Wiki）Djot 标记、[NIP-19](/zh/topics/nip-19/)（Bech32 编码实体）输入限制、[NIP-91](/zh/topics/nip-91/)（过滤器 AND 运算符）布尔查询逻辑，以及 [NIP-85](/zh/topics/nip-85/)（可信断言）Web of Trust 断言。开放提案则从自主代理（NIP-AA）延伸到 WASM 程序（NIP-A5），再到 [NIP-50](/zh/topics/nip-50/) 的搜索排序扩展。

### Looking Ahead

Nostr 的五个三月勾勒出一条清晰的弧线。2021 年时，只有一个人向一个还不能按 kind 过滤 event 的协议提交了两次提交。到了 2023 年，NDK 和 NWC 在相隔五天内诞生，以吸收 Damus 爆发后的增长。到 2024 年，一条拥有 141 条评论的 PR 讨论串已经在争论一个社交协议上的 git 协作该如何运作。到 2025 年，一份经过七次重写、历时 25 个月耐心打磨的 relay 监控规范终于合并。到 2026 年，有人因为 Tailscale 需要账户而恼火，于是用 Nostr 密钥对构建了一个 VPN；另一个人则发布了通过 Nostr relay 发现 peer、通过 Marmot 加密游戏流量的多人 DOOM。BigBrotr 对 1,085 个 relay、4,100 万个 event 的扫描，给出了网络增长规模的一个具体量化指标。2026 年 3 月的协议表面面积，对 2021 年 3 月的参与者来说几乎不可想象，但其底层模型并没有改变：由 secp256k1 密钥签名、通过 relay 分发的 event。

---

本周就到这里。正在构建什么，或者有新闻想分享？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 [NIP-17](/zh/topics/nip-17/)（私密私信）联系我们</a>，或者直接在 Nostr 上找到我们。
