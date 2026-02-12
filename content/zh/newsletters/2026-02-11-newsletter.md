---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** Mostro 经过三年开发发布首个公测版，通过 Nostr 将 P2P Bitcoin 交易带到移动端。OpenSats 颁发第十六波 Bitcoin 资助，Minibits Wallet 获得续期资助，该钱包集成了 Nostr 的 Cashu 功能。**Zapstore 达到 1.0 稳定版本**，标志着去中心化 Android 应用商店的成熟。Coracle 0.6.29 添加话题和高亮评论功能。Igloo Desktop v1.0.3 对 Frostr 门限签名进行了重大安全加固。Amber v4.1.2-pre1 迁移至 Flow 架构。Angor 发布 v0.2.5，带来全新的资金管理 UI 和 NIP-96 图片服务器配置。NostrPress 作为一款将 Nostr 个人资料转换为静态博客的工具上线。Antiprimal 发布了一个标准兼容的网关，将 Primal 的专有缓存服务器桥接到标准 Nostr NIP。Primal Android 合并 18 个 PR，扩展 NWC 基础设施，支持双钱包、审计日志和 `lookup_invoice` 方法。diVine 推出 API 优先视频信息流。Marmot TypeScript SDK 将其参考聊天应用拆分为独立仓库，并开始迁移到 ts-mls v2。NIPs 仓库合并了 NIP-45 的 HyperLogLog 近似计数并从 kind 0 提取了身份 tag。vitorpamplona 发起的一系列提案开始系统性地精简 kind 0 元数据 event。新协议提案包括用于 NAT 穿透的 Nostr Relay Connect 和用于签名 Web 声明的 Nostr Web Token。本周的深入解析涵盖 NIP-45 新增的 HyperLogLog 近似计数（用于跨 relay event 指标）以及 NIP-96 的 HTTP 文件存储协议（现已弃用，由 Blossom 替代），各项目正在两种媒体标准之间过渡。

## 新闻

### Mostro 发布首个公测版

[Mostro](https://github.com/MostroP2P/mostro)，基于 Nostr 构建的点对点 Bitcoin 交易所，发布了[移动应用 v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0)，这是该项目经过三年开发后的首个公测版。该应用使用户能够直接通过 Nostr 进行订单协调来交易 Bitcoin，使用 Lightning 进行结算，无需托管中介。

此版本引入了推送通知，改善了 Android 后台可靠性，提供可选的日志系统让用户在出现问题时捕获和共享诊断数据，使用增量初始化实现更顺畅的 relay 更新，以及带有国际化支持的第二阶段 UI 改进。该应用可在 [Zapstore](https://zapstore.dev) 和 [GitHub 直接下载](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0)获取。

Mostro 与 Shopstr 和 Plebeian Market 一起成为 Nostr 原生商务应用，其独特之处在于专注于法币兑 Bitcoin 的交换协调。底层的 [Mostro 守护进程](https://github.com/MostroP2P/mostro)通过 Nostr relay 处理订单匹配和争议解决。

### OpenSats 第十六波 Bitcoin 资助

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants) 宣布向 17 个开源项目提供资助。与 Nostr 相关的亮点：[Minibits Wallet](https://github.com/minibits-cash/minibits_wallet)，这款支持 [NIP-60](/zh/topics/nip-60/) 钱包 event 和 nutzap 集成的 Android [Cashu](/zh/topics/cashu/) 钱包，获得了续期资助。Minibits 使用 Nostr event 存储 ecash 代币状态，使钱包备份可通过 relay 同步在设备间移植。

### NostrPress：Nostr 个人资料转静态博客

[NostrPress](https://github.com/besoeasy/NostrPress)（[blog.besoeasy.com](https://blog.besoeasy.com)）是一款新工具，可将 Nostr 个人资料转换为完全静态的博客，可部署到任何地方。用户通过任何客户端在 Nostr 上发布文章，NostrPress 从这些 event 生成独立网站，包含本地媒体托管和 RSS 订阅源。

NostrPress 使用 Nunjucks 模板和 JavaScript 构建，生成零平台锁定的网站。生成的输出是纯 HTML/CSS，可托管在任何静态文件服务器、GitHub Pages、Netlify 或个人 VPS 上。该工具与 [Npub.pro](https://github.com/nostrband/nostrsite) 和 [Servus](https://github.com/servus-social/servus) 一起成为将 Nostr 内容转换为传统网站的选择。

### Antiprimal：Primal 缓存的标准兼容网关

[antiprimal](https://gitlab.com/soapbox-pub/antiprimal)（[antiprimal.net](https://antiprimal.net)），Alex Gleason 和 Soapbox 团队的新项目，是一个 WebSocket 网关，将 Primal 的专有缓存服务器桥接到标准 Nostr 协议消息。Primal 通过 `wss://cache.primal.net/v1` 提供 event 统计、内容搜索和 Web of Trust 计算等功能，但访问这些功能需要使用非标准 `cache` 字段的专有消息格式，标准 Nostr 客户端无法使用。Antiprimal 将标准 NIP 请求转换为 Primal 的格式并转换回响应。

该网关支持 [NIP-45](/zh/topics/nip-45/) COUNT 查询（反应、回复、转发、zap 计数、关注者计数）、[NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) 搜索、[NIP-11](/zh/topics/nip-11/) relay 信息，以及 [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) 用于 Primal 预计算 Web of Trust 数据的 Trusted Assertions。配套机器人将 NIP-85 kind 30382（用户统计）和 kind 30383（event 互动）event 发布到可配置的 relay。该项目使用 TypeScript 基于 Bun 构建，使用 Nostrify 库。创建于 2 月 6 日，开发前三天已有 53 次提交，已在 antiprimal.net 上线。

### Ikaros：Signal 和 Nostr 的 AI 代理消息网关

[Ikaros](https://gitlab.com/soapbox-pub/ikaros)，Soapbox 团队的新项目，是一个消息网关，使 AI 代理能够通过 Signal 和 Nostr 加密 DM 进行通信。该桥接使用 [Agent Client Protocol](https://agentclientprotocol.org)（ACP）将任何 ACP 兼容的 AI 编程助手连接到真实的消息网络。本周三个 pull request 构成了该项目的初始构建。

[PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1) 实现了完整的 [NIP-04](/zh/topics/nip-04/) 加密 DM 适配器，包含发送/接收支持、带显式刷新的响应缓冲、`nsec` 和十六进制私钥格式、多 relay 发布与自动重连，以及交互式配置向导。该适配器使用 nostr-tools v2.23.0 并将 ACP SDK 更新至 v0.14.1。

[PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2) 修复了由会话更新竞态条件导致的静默消息丢失：在会话注册到映射之前到达的传入通知被静默丢弃，修复方案缓冲这些通知并在注册完成后重放。[PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3) 在代理交互中添加了 Signal 用户和群组名称/UUID 元数据，让 AI 代理知道它正在与谁交谈以及在哪个群组中。该项目开辟了新的设计空间：可通过 Nostr DM 寻址的 AI 代理也可从 Signal 访问，反之亦然。

### Kind 0 瘦身运动

vitorpamplona 本周开启了一系列 PR，提议系统性地将数据从 kind 0（用户元数据）event 提取到专用 event 类型中。该运动解决了一个日益严重的问题：kind 0 event 随时间积累了大多数客户端不使用的字段，使每次个人资料获取的体积膨胀。

[PR #2216](https://github.com/nostr-protocol/nips/pull/2216)（已合并）将身份 tag（`i` tag）从 kind 0 移至新的 kind 10011，因为这些 tag 的采用率极低。[PR #2213](https://github.com/nostr-protocol/nips/pull/2213) 提议将 [NIP-05](/zh/topics/nip-05/) 验证移至 kind 10008，这将使用户能够拥有多个 NIP-05 标识符并允许按 NIP-05 地址过滤 event。[PR #2217](https://github.com/nostr-protocol/nips/pull/2217) 提议将 Lightning 地址（lud06/lud16）提取到新的 kind，从而使所有 kind 0 用户不再需要携带仅与 Lightning 集成客户端相关的 zap 相关字段。

这些提案重新引发了关于 kind 0 结构更广泛问题的讨论，包括 [PR #1770](https://github.com/nostr-protocol/nips/pull/1770)，即用结构化 tag 替换 kind 0 content 中字符串化 JSON 的长期提案。

### NIP-70 Relay 支持对加密消息安全至关重要

[Marmot](/zh/topics/marmot/) 协议的 White Noise 实现[发现了一个关键缺口](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html)：relay 对 [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md)（受保护 Event）和 [NIP-42](/zh/topics/nip-42/)（认证）的支持不足。测试发现，包括 Damus、Primal 和 nos.lol 在内的主要公共 relay 直接以 `blocked: event marked as protected` 错误拒绝受保护 event，而没有发起所需的认证挑战。

这破坏了一项关键安全功能：NIP-70 可安全删除已使用的 MLS KeyPackage，防止"先收集后解密"攻击。如果 relay 不支持，加密消息协议就无法保护用户免受未来密钥泄露的影响。White Noise 已默认禁用 NIP-70，保留可选标志供使用支持 relay 的用户启用。

**对 relay 运营者的呼吁：** 请实现完整的 NIP-42 认证流程。收到受保护 event 时，应挑战客户端证明所有权，然后接受经验证的写入。未经认证就拒绝受保护 event 会破坏加密消息应用所依赖的协议安全保证。

## 版本发布

### Coracle 0.6.29

[Coracle](https://github.com/coracle-social/coracle)（[coracle.social](https://coracle.social)），hodlbod 的 Web 客户端，发布了 [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29)。此版本添加了话题和 kind 9802 高亮的评论显示。新的列表导航项提供从主 UI 快速访问用户策划列表的功能。底层方面，Coracle 升级到新版本的 Welshman，这是支撑 Coracle relay 管理和 event 处理的共享 Nostr 库。默认 relay 列表已刷新，Glitchtip 错误追踪已从代码库中移除。

### Igloo Desktop v1.0.3

[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop)，基于 [FROST](/zh/topics/frost/) 的门限签名和密钥管理应用，发布了 [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3)，包含大量安全加固。此版本引入了 IPC 验证、Electron 隔离和 SSRF 感知的 relay 检查，防御服务器端请求伪造。新的入门和份额导入流程简化了密钥分发，relay 规划包含了规范化和优先级合并，基于 preload 的 Electron API 架构改善了渲染进程与主进程之间的安全边界。签名者保活系统维护门限签名会话稳定性，恢复 UX 改进减少了密钥恢复的摩擦。

### Amber v4.1.2-pre1

[Amber](https://github.com/greenart7c3/Amber)，Android event 签名器，发布了 [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1)，修复了 v4.1.1 引入的 relay 信任评分显示缺失问题，解决了非 Nostr 加密/解密请求的 JSON 解析问题，并将账户模型从 LiveData 迁移到 Flow 以实现更可预测的状态管理。此版本将 bunker 密钥切换为完整 UUID 并升级到 Gradle 插件 9。

### Mostro Mobile v1.1.0 和 Daemon v0.16.1

完整的移动版报道请参见[上方新闻部分](#mostro-发布首个公测版)。服务器端，[Mostro 守护进程](https://github.com/MostroP2P/mostro)发布了 [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1)，添加了启动时自动发布 NIP-01 kind 0 元数据的功能（[PR #575](https://github.com/MostroP2P/mostro/pull/575)），守护进程上线时会向网络公布其身份。此版本还修复了开发费用计算文档（[PR #571](https://github.com/MostroP2P/mostro/pull/571)）。

### Angor v0.2.5

[Angor](https://github.com/block-core/angor)（[angor.io](https://angor.io)），基于 Bitcoin 和 Nostr 构建的去中心化 P2P 资金协议，发布了 [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5)，包含三个已合并的 PR。[PR #649](https://github.com/block-core/angor/pull/649) 重新设计了资金管理部分（V2），用新界面替换了之前的布局，用于跟踪单个 UTXO 和投资头寸。[PR #651](https://github.com/block-core/angor/pull/651) 全面改造了 InvoiceView，更新了按钮样式、可关闭对话框、新的"复制地址"命令、地址监控取消支持和改进的投资流程处理。[PR #652](https://github.com/block-core/angor/pull/652) 在设置中添加了可配置的 [NIP-96](/zh/topics/nip-96/)（[规范](https://github.com/nostr-protocol/nips/blob/master/96.md)）图片服务器，让用户选择哪个媒体上传端点处理其项目图片和文档。[v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4) 于前一周发布。

### Ridestr v0.2.2 和 v0.2.3

[Ridestr](https://github.com/variablefate/ridestr)，去中心化拼车平台，[上周已报道](/zh/newsletters/2026-02-04-newsletter/#ridestr-v020roadflare-版本)，在 v0.2.0"RoadFlare 版本"之后继续快速迭代，发布了 [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2)（Bridge Payment 热修复）和 [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3)。v0.2.2 热修复解决了跨铸造厂 [Cashu](/zh/topics/cashu/) 桥接支付在支付仍在处理或最终会成功时自动取消行程的错误，防止慢速结算导致的提前取消。此版本还修复了"我的位置"按钮的 UI 闪烁和触摸热区失效问题。v0.2.3 包含额外的错误修复。两个版本都包含 Ridestr（乘客应用）和 Drivestr（司机应用）的独立 APK。

### Nostr PHP 1.9.4

[Nostr PHP](https://github.com/nostrver-se/nostr-php)（[nostr-php.dev](https://nostr-php.dev)），Nostr 协议的 PHP 辅助库，发布了 [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4)，为请求类添加了可配置的 `timeout` 属性（[PR #106](https://github.com/nostrver-se/nostr-php/pull/106)）。这让开发者可以为 relay 连接和消息请求设置自定义超时时间，防止 relay 无响应或回复缓慢时的无限挂起。

### Zapstore v1.0.0

[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0)（[zapstore.dev](https://zapstore.dev)），基于 Nostr 构建的无许可 Android 应用商店，经过数月的候选版本后**本周达到稳定 1.0 版本里程碑**。

1.0 版本包含关键的稳定性改进：安装按钮状态处理确保安装完成后立即显示删除按钮，用户友好的错误消息带可展开的技术详情，以及通过使用临时密钥的 Nostr 加密 DM 发送的"报告问题"按钮。此版本还提供了新的更新屏幕（带轮询和批量跟踪）、更好的下载看门狗处理停滞传输、基于设备性能的动态并发下载限制、更频繁的已安装包同步，以及改进的版本比较逻辑。团队修复了一个关键的 flutter_secure_storage 问题并增强了包管理器对边缘情况的处理。

这一里程碑代表了 Nostr 首个专用应用分发平台的成熟，使开发者能够在没有中心化应用商店管控的情况下直接向用户发布 Android 应用。

### ZSP v0.3.1

[ZSP](https://github.com/zapstore/zsp)，[Zapstore](https://github.com/zapstore/zapstore) 团队的 Go CLI 工具，用于替代 Zapstore 之前的签名和上传 Android 应用到 Nostr relay 的发布工具，发布了 [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1)。ZSP 处理从 GitHub、GitLab、Codeberg、F-Droid 或本地文件获取 APK，然后解析元数据，签名 Nostr event（通过私钥、[NIP-46](/zh/topics/nip-46/) bunker 或 [NIP-07](/zh/topics/nip-07/) 浏览器扩展），并将制品上传到 [Blossom](/zh/topics/blossom/) 服务器。此版本添加了完整的离线模式用于无网络连接时的密钥库链接、Blossom 上传的 `Content-Digest` 头以符合协议规范、修复了 F-Droid 仓库中 arm64-v8a APK 的检测、GitLab 尾部查询参数修复，以及完整的 `.env` 文件配置支持。

### Damus iOS 1.17

[Damus](https://github.com/damus-io/damus)，iOS Nostr 客户端，版本升级至 1.17（[PR #3606](https://github.com/damus-io/damus/pull/3606)）。此版本修复了 RelayPool 在临时租约释放后连接关闭的问题（[PR #3605](https://github.com/damus-io/damus/pull/3605)），该问题可能导致订阅意外断开。同时解决了在标签页之间切换时收藏时间线不显示 event 的错误（[PR #3603](https://github.com/damus-io/damus/pull/3603)）。

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak)，Nostr army knife CLI，发布了 [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3)，包含三个稳定性修复：防止 AUTH 挑战 tag 为 nil 或过短时的崩溃，在使用解析值之前检查 dateparser 错误，以及处理缺少 `://` 分隔符的 Cashu 铸造厂 URL。

### Mi：基于浏览器的本地 Relay

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git)（[mi.shakespeare.wtf](https://mi.shakespeare.wtf)），一个新的 [Shakespeare](https://shakespeare.wtf) MiniApp，是一个基于浏览器的本地 relay，在 IndexedDB 中归档用户的 Nostr event。Mi 从已连接的 relay 获取个人资料（kind 0）、联系人列表（kind 3）、relay 列表（kind 10002）和钱包 event 并存储在本地，为用户提供离线访问自己数据的能力。使用 React 和 nostr-tools 2.15.0 构建。

### Agora v1.0.2

[Agora](https://gitlab.com/soapbox-pub/agora)（[agora.spot](https://agora.spot)），Soapbox 团队的去中心化行动主义和筹款平台，发布了 [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2)，提供可直接安装的 Android APK。这是 Compass 首次报道 Agora，该平台于 1 月 17 日上线，使命宣言为："加入全球自由运动。向各地的行动者发送支持，并参与本地行动。"

该平台以世界地图为中心，用户可按国家浏览，创建带位置标签的"行动"（抗议、运动、社区组织），并通过线程评论进行讨论。所有内容通过 Nostr relay 传播，因此没有中心化服务器可被关闭以压制协调活动。Agora 支持多语言（CI 强制翻译一致性），集成 [Blossom](/zh/topics/blossom/) 媒体服务器用于上传，包含搜索、带全球/区域切换的话题标签浏览、用户个人资料和反应系统。v1.0.2 是当前 Android 版本，可直接下载 APK。

### xonos v0.1.6

[xonos](https://codeberg.org/xonos/xonos)，使用 Bevy 游戏引擎构建的实验性 3D Nostr 客户端，发布了 [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6)。xonos 在 3D 空间环境中渲染 Nostr event 并具有文字转语音功能，探索社交协议数据如何在传统 2D 界面之外运作。

## 项目更新

### Primal Android 扩展 NWC 基础设施

[Primal Android](https://github.com/PrimalHQ/primal-android-app) 本周合并了 18 个 PR，继续[上周开始的](/zh/newsletters/2026-02-04-newsletter/#primal-android-发布-nwc-加密) NWC 建设。[PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883) 添加了跨两个钱包（Spark 和外部）的 NWC 连接支持，[PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879) 实现了用于检查支付状态的 `lookup_invoice` NWC 方法。

[PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880) 添加了 NWC 请求-响应审计日志用于调试钱包交互。[PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877) 为 `PrimalNwcService` 添加了多账户支持，使拥有多个个人资料的用户能够维护独立的钱包连接。[PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882) 实现了过期预算保留的定期清理，防止过期的支付预留阻塞钱包操作。

UI 工作包括钱包升级屏幕重新设计（[PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)）、钱包升级常见问题（[PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)）、入门期间设置 Lightning 地址（[PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)），以及修复非 Lightning 类型的 zap 交易显示为普通支付的问题（[PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)）。

### diVine 推出 API 优先视频信息流

[diVine](https://github.com/divinevideo/divine-mobile)，短视频客户端，本周合并了 19 个 PR，转向 API 优先架构。[PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468) 引入了 API 优先视频信息流，[PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466) 添加了热门、最新和首页 API 端点。[PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433) 为高效信息流渲染索引了特定的视频控制器。

个人资料处理通过 [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440) 改进，实现了查看其他个人资料时的缓存加新鲜数据模式，在确保数据新鲜度的同时减少加载时间。团队还发布了通知修复（[PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)）、评论流程重构（[PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)），以及通知屏幕的标签页滑动（[PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388)）。

### White Noise：密钥环统一和用户搜索

[White Noise](https://github.com/marmot-protocol/whitenoise-rs) 后端，[Marmot](/zh/topics/marmot/) 协议的实现，本周合并了 4 个 PR。两个 PR 改进了密钥环处理：[PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468) 通过 `WhitenoiseConfig` 使密钥环服务标识符可配置，[PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475) 在单个 `keyring-core` crate 上统一了实现，使用平台原生存储替换了碎片化的平台特定代码。另外，[PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470) 添加了用户搜索功能。

### Marmot TS 提取参考聊天应用

[Marmot](/zh/topics/marmot/) TypeScript SDK（[marmot-ts](https://github.com/marmot-protocol/marmot-ts)）合并了 [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40)，移除了内置参考聊天应用并将其拆分到独立仓库：[marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat)。新仓库创建于 2 月 6 日，是 Marmot TypeScript SDK 的参考实现，拥有独立的 CI 管道、标签式聊天视图和独立构建系统。这种分离让 SDK 专注于库的关注点，聊天应用则独立迭代 UX。

一个开放的 PR（[#41](https://github.com/marmot-protocol/marmot-ts/pull/41)）将 marmot-ts 迁移到 ts-mls v2.0.0，带来重新设计的 API，包含统一的上下文对象、新的消息处理工具（event 创建、读取、反序列化）、密钥包元数据辅助函数和删除 event 支持。

### Alby Hub 更新

[Alby Hub](https://github.com/getAlby/hub) 本周合并了 5 个 PR。[PR #2049](https://github.com/getAlby/hub/pull/2049) 在应用商店界面添加了 Alby CLI。[PR #2033](https://github.com/getAlby/hub/pull/2033) 修复了交易列表中无效 zap 数据的处理，[PR #2046](https://github.com/getAlby/hub/pull/2046) 从 LNClient 接口移除了未使用的 `ListTransactions` 方法。

### Notedeck 推出 Dashboard 和 Agentium

[Notedeck](https://github.com/damus-io/notedeck)，Damus 的跨平台 Nostr 客户端，本周合并了 6 个 PR。[PR #1247](https://github.com/damus-io/notedeck/pull/1247) 添加了初始 dashboard 应用。[PR #1293](https://github.com/damus-io/notedeck/pull/1293) 引入了 Agentium，一个多代理开发环境，将 Dave AI 助手转变为具有双 AI 模式和基于场景的代理管理的系统。[PR #1276](https://github.com/damus-io/notedeck/pull/1276) 添加了带 Signal 风格快捷键的多行消息编辑器，[PR #1278](https://github.com/damus-io/notedeck/pull/1278) 带来了媒体性能改进。值得关注的开放 PR 包括 [outbox 基础设施](https://github.com/damus-io/notedeck/pull/1288)和 [NIP-34](/zh/topics/nip-34/) [Git 应用规划](https://github.com/damus-io/notedeck/pull/1289)。

### Agora 推出重大 UI 改造

[Agora](https://gitlab.com/soapbox-pub/agora) 本周与 v1.0.2 版本一同合并了 7 个 PR。[PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106) 是最大的，关闭了 11 个涵盖设置、个人资料编辑、地图交互、搜索结果、评论过滤和 Blossom 服务器管理的 UI 任务。该合并禁用了未认证用户的反应按钮（此前这些用户尝试在地图上对帖子反应时会遇到静默失败），修复了日期线地图平移，并在搜索结果中添加了匹配文本加粗显示。

[PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108) 在信息流帖子下方和线程页面添加了评论计数。[PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107) 添加了 event 加载失败时的自动重试，重试耗尽时显示显式重新加载按钮。[PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104) 将话题标签浏览默认改为全球范围，因为之前的国家范围默认经常返回零结果。

[PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109) 添加了 CI 步骤检查所有语言的翻译一致性，任何缺失值都会导致构建失败。[PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110) 裁剪信息流中的大型笔记以保持滚动节奏，[PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111) 修复了因小字号导致的 iOS 移动端评论行动时的缩放问题。

### Clawstr 推出 CLI 和 Lightning Zap 按钮

[Clawstr](https://gitlab.com/soapbox-pub/clawstr)，AI 代理在 Nostr 上创建和管理社区的 Reddit 风格平台，本周合并了 3 个 PR。[PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11) 将 AI 代理技能定义中的所有手动 nak 命令替换为新的 `@clawstr/cli` 包（`npx -y @clawstr/cli@latest`），用 CLI 命令取代手动 JSON event 构造，并添加了钱包操作（init、balance、zap、npc）和 [NIP-50](/zh/topics/nip-50/) 全文搜索。

[PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13) 添加了"For Humans"文档页面和 `ProfileZapDialog` 组件。zap 按钮在用户配置了 Lightning 地址时显示在个人资料页面上，无需登录即可使用，直接通过 LNURL-pay 支持预设 sats 金额和二维码显示。[PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12) 记录了 `wallet sync` 命令，解释了发送到 Lightning 地址的支付如何由 NPC 持有，直到代理显式同步钱包。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**

- **[NIP-45：HyperLogLog Relay 响应](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45（Event 计数）](/zh/topics/nip-45/)现在支持 HyperLogLog (HLL) 近似计数。relay 可以在 COUNT 响应中返回 256 字节的 HLL 寄存器值。客户端合并来自多个 relay 的这些寄存器，通过取每个位置的最大值来计算近似基数，无需下载完整 event 集合。主要用例是关注者和反应计数，无需依赖单个 relay 作为权威来源。即使两个反应 event 消耗的带宽也超过 256 字节的 HLL 负载。客户端可应用 HyperLogLog++ 修正以提高小基数的准确度。

- **[NIP-39：身份 Tag 从 Kind 0 移出](https://github.com/nostr-protocol/nips/pull/2216)** - [NIP-39](/zh/topics/nip-39/) 身份声明 tag（`i` tag）已从 kind 0 元数据 event 提取到新的专用 kind 10011。原因是几乎没有客户端支持这些 tag，但每次 kind 0 获取都要承担额外体积。这是 vitorpamplona 系列 kind 0 提取 PR 中的第一个（见[新闻部分](#kind-0-瘦身运动)）。

**开放 PR 和讨论：**

- **[NIP-XX：Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos 提议通过公共中转 relay 进行加密隧道访问 Nostr relay 的协议。该机制支持访问 NAT 或防火墙后面的 relay，包括运行在家庭服务器或移动设备上的个人 relay。隧道使用 kind 24891/24892 event 和 [NIP-44](/zh/topics/nip-44/) 加密，通过无法解密流量的中转 relay。一个实际应用：任何 Nostr 客户端都可以将本地存储（IndexedDB、SQLite）暴露为 relay 端点用于跨设备同步。标准 NIP-01 语义（REQ、EVENT、CLOSE、COUNT）透明地通过隧道传输。参考实现包括 Go（ORLY Relay）和 TypeScript（Smesh）。

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc 提议 Nostr Web Tokens，一种用于在 Web 各方之间传递签名声明的 Nostr event 格式，灵感来自 JSON Web Tokens (JWT)。NWT 可以表示 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)（HTTP Auth）和 [Blossom 授权 event](/zh/topics/blossom/)，为客户端提供令牌有效期和方式的灵活性。提供了参考 Go 库。PR 中链接了[视频解释](https://github.com/pippellia-btc/nostr-web-tokens)和与 NIP-98 及 Blossom Auth 的[详细对比](https://github.com/pippellia-btc/nostr-web-tokens?tab=readme-ov-file#comparisons)。

- **[NIP-47 简化](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz 提议从 [NIP-47（Nostr Wallet Connect）](/zh/topics/nip-47/)中移除 `multi_` 方法，这些方法实现复杂且未获得采用。该 PR 还减少了加密和向后兼容处理中的重复，在[上周添加 hold invoice](/zh/newsletters/2026-02-04-newsletter/#nip-更新) 后清理了规范。

- **[NIP-05：移至独立 Event Kind](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona 提议将 NIP-05 验证从 kind 0 移至新的 kind 10008，支持每个用户拥有多个 NIP-05 标识符并按 NIP-05 地址过滤。属于 kind 0 瘦身运动的一部分。

- **[NIP-57：Lightning 地址从 Kind 0 移出](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona 提议根据 [NIP-57](/zh/topics/nip-57/) 将 lud06/lud16（Lightning 地址）从 kind 0 提取到专用 event kind，继续 kind 0 瘦身工作。

- **[个人资料超级定制](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf 提议超越 kind 0 当前能力的扩展个人资料定制功能。

## NIP 深入解析：NIP-45（Event 计数）与 HyperLogLog

[NIP-45](/zh/topics/nip-45/)（[规范](https://github.com/nostr-protocol/nips/blob/master/45.md)）定义了客户端如何请求 relay 计算匹配过滤器的 event 数量，而无需传输 event 本身。本周合并的 [HyperLogLog 支持](https://github.com/nostr-protocol/nips/pull/1561)添加了一种概率数据结构，解决了一个根本问题：如何跨多个独立 relay 计数。

**问题：**

在单个 relay 上计数 event 很简单：发送 COUNT 请求，获得一个数字。跨网络计数则更难。如果 relay A 报告 50 个反应，relay B 报告 40 个，总数并非 90，因为许多 event 同时存在于两个 relay 上。如果不下载所有 event 进行去重，客户端无法计算真实数量。

**HyperLogLog：**

HyperLogLog (HLL) 是一种概率算法，使用固定内存量估算集合中不同元素的数量。NIP-45 实现使用 256 个各一字节的寄存器，无论计数多少 event 都只消耗 256 字节。该算法通过检查每个 event ID 的二进制表示并跟踪前导零的位置来工作。ID 以多个零开头的 event 在统计上是罕见的，因此它们的出现表明集合很大。

**NIP-45 中的工作方式：**

relay 响应 COUNT 请求时可以包含一个 `hll` 字段，其中包含 base64 编码的寄存器值：

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

客户端从多个 relay 收集 HLL 值，通过取每个寄存器位置的最大值来合并。合并后的 HLL 表示所有 relay event 集合的并集，自动处理去重。最终的基数估算从合并后的寄存器计算得出。

**准确度：**

使用 256 个寄存器时，标准误差约为 5.2%。对于真实计数 1,000，估算值通常落在 948 到 1,052 之间。对于更大的计数，相对误差保持不变：真实计数 100,000 的估算值大约为 94,800 到 105,200。HyperLogLog++ 修正提高了小基数（约 200 以下）的准确度，基本算法在这个范围往往会高估。

**意义：**

社交指标（关注者数量、反应数量、转发数量）是社交媒体客户端的核心功能。没有 HLL 时，客户端必须查询单个"可信"relay（使计数中心化）或从所有 relay 下载所有 event（浪费带宽）。HLL 让客户端以每个 relay 256 字节的总开销从多个 relay 获得良好的近似计数，与实际计数无关。即使两个反应 event 消耗的带宽也超过完整 HLL 负载。

规范将寄存器数量固定为 256 以确保互操作性。所有 relay 产生的 HLL 值都可以被客户端合并，无论运行哪种 relay 实现。这种标准化意味着客户端只需实现一次 HLL 支持，就能受益于每个支持它的 relay。

**当前状态：**

该 PR 由 fiatjaf 开启，在合并前已讨论数月。relay 实现需要在其 COUNT 处理器中添加 HLL 计算。客户端实现需要在计数聚合逻辑中添加 HLL 合并。

## NIP 深入解析：NIP-96（HTTP 文件存储）与向 Blossom 的过渡

[NIP-96](/zh/topics/nip-96/)（[规范](https://github.com/nostr-protocol/nips/blob/master/96.md)）定义了 Nostr 客户端如何在 HTTP 媒体服务器上上传、下载和管理文件。目前标记为"不推荐"，建议使用 [Blossom](/zh/topics/blossom/)（基于 BUD 的媒体托管），NIP-96 在本周仍然相关，因为 Angor v0.2.5 [添加了 NIP-96 服务器配置](#angor-v025)而 ZSP v0.3.1 [上传到 Blossom 服务器](#zsp-v031)，展示了正在进行的协议过渡。

**NIP-96 的工作方式：**

客户端通过获取 `/.well-known/nostr/nip96.json` 来发现文件服务器的功能，返回 API URL、支持的内容类型、大小限制和可用的媒体转换：

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

上传时，客户端向 API URL 发送带有 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) 授权头（证明上传者身份的已签名 Nostr event）的 `multipart/form-data` POST 请求。服务器返回 [NIP-94](/zh/topics/nip-94/) 文件元数据结构，包含文件 URL、原始和转换后的 SHA-256 哈希、MIME 类型和尺寸：

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

下载使用 GET 请求到 `<api_url>/<sha256-hash>`，可选查询参数用于服务器端转换（如图像缩放 `?w=320`）。删除使用带 NIP-98 认证的 DELETE 请求，只有原始上传者才能删除其文件。文件列表端点返回用户上传的分页结果。

用户发布 kind 10096 event 来声明其首选上传服务器，让客户端无需手动配置即可自动选择合适的服务器。

**弃用原因：**

NIP-96 将文件 URL 绑定到特定服务器。如果 `files.example.com` 下线，所有引用该服务器 URL 的 Nostr 笔记都会丢失其媒体。服务器就是地址，而地址是脆弱的。

[Blossom](/zh/topics/blossom/)（Blobs Stored Simply on Mediaservers）反转了这一模式，将文件内容的 SHA-256 哈希作为规范标识符。Blossom URL 形如 `https://blossom.example/<sha256>.png`，但任何托管相同文件的 Blossom 服务器都通过相同的哈希路径提供服务。如果一个服务器消失，客户端向另一个服务器查询相同的哈希。内容寻址默认使数据在服务器间可移植。

Blossom 还简化了 API。NIP-96 使用 multipart 表单上传、JSON 响应、转换策略和发现端点。Blossom 使用普通 PUT 上传、GET 下载，以及签名的 Nostr event（而非 HTTP 头）进行授权。Blossom 规范分为模块化文档：BUD-01 涵盖服务器协议、授权和检索，BUD-02 涵盖 blob 上传，BUD-03 涵盖用户服务器，BUD-04 涵盖服务器间镜像。

弃用于 2025 年 9 月通过 [PR #2047](https://github.com/nostr-protocol/nips/pull/2047) 完成，在 NIPs 索引中将 NIP-96 标记为"不推荐"。

**实践中的过渡：**

nostr.build 和 void.cat 等服务器此前支持 NIP-96，已添加或迁移到 Blossom 端点。各客户端处于不同阶段：Angor 本周的 v0.2.5 版本为项目图片添加了 NIP-96 服务器配置，而 ZSP 的 v0.3.1 版本专门上传到 Blossom 服务器并带有 `Content-Digest` 头以符合协议规范。Amethyst 和 Primal 支持 Blossom 上传。这种共存可能会持续到剩余的 NIP-96 实现完成迁移。

**延续的内容：**

kind 10096 服务器偏好 event 对 Blossom 服务器选择仍然有用。NIP-94 文件元数据（kind 1063 event）无论使用哪种上传协议都能描述文件属性。NIP-96 用于下载 URL 的 SHA-256 哈希成为 Blossom 内容寻址的基础。NIP-96 的设计启发了 Blossom 的简化方向：去中心化网络上的媒体托管需要内容寻址存储来匹配 relay 层的抗审查能力。

---

本周就到这里。正在构建什么？有新闻要分享？希望我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 私信联系我们</a>或在 Nostr 上找到我们。
