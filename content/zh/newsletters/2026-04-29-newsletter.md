---
title: 'Nostr Compass #20'
date: 2026-04-29
publishDate: 2026-04-29
draft: false
type: newsletters
translationOf: /en/newsletters/2026-04-29-newsletter.md
translationDate: 2026-07-01
description: 'GitWorkshop 推出浏览器内 PR 合并按钮、仓库关注功能、带宽高效的 git 浏览器，以及 git-over-Nostr 的内联代码审查评论；Routstrd 推出使用 Nostr 提供商公告和 Cashu 支付的本地推理路由器；发布内容包括 ngit v2.4.2、Wisp v1.0.0、grain v0.5.2 和 v0.5.3、Mostro Core v0.10.0、Mostro Mobile v1.2.5、marmot-ts v0.5.0、CruxCoach v0.1.3、Meiso v1.3.0、NoorNote、Nostria、Nostr Calendar、nos2x-fox、applesauce 和 nostr-double-ratchet；未发布的工作涵盖 Amethyst Nests、nostream 的 NIP-65/NWC、FIPS 基于 Nostr 的 udp:nat 引导、strfry 可观测性、Sprout 所有者证明和 Zap Cooking 食谱包；新纳入跟踪的项目包括 Nostrord、Clave、Treasures、smesh、Surveil、Fundstr、Nod City、deploy-nsite-to-pages 和 null--nostr；月末回顾涵盖了 2021 年至 2026 年的 Nostr 四月。'
---

欢迎回到 Nostr Compass，你的 Nostr 每周指南。

**本周：**[GitWorkshop](#gitworkshop-ships-in-browser-pr-merge-repository-following-and-a-bandwidth-efficient-git-explorer) 将 git-over-Nostr 转变为一个更完整的代码审查界面，带来浏览器内 PR 合并按钮、Stars 和仓库关注功能、带宽高效的 git 浏览器、kind `1111` 内联审查评论，以及加密的多设备通知状态。[Routstrd](#routstrd-launches-a-local-router-for-inference-over-nostr) 推出了一个本地守护进程，通过 Nostr kind `38421` 公告发现模型提供商，并使用 Cashu 支付。带标签的发布包括 [ngit v2.4.2](#ngit-v242-fixes-grasp-relay-detection-for-pr-submissions)、[Wisp v1.0.0](#wisp-v100-graduates-from-beta)、[grain v0.5.2 和 v0.5.3](#grain-v052-fixes-websocket-lockup-v053-continues-polish)、[Mostro Core v0.10.0 和 Mostro Mobile v1.2.5](#mostro-core-v0100-and-mostro-mobile-v125-adopt-nip-59-dual-key-gift-wrap)、[marmot-ts v0.5.0](#marmot-ts-v050-ships-addressable-keypackages)、[CruxCoach v0.1.3](#cruxcoach-v013-ships-encrypted-climbing-data-backup-with-nostr-and-blossom)、[Meiso v1.3.0](#meiso-v130-adds-subtasks-blossom-attachments-and-nip-89-tagging)、NoorNote、Nostria、Nostr Calendar、nos2x-fox、applesauce、nostr-double-ratchet 等。未发布的更改涵盖 [Amethyst Nests](#amethyst-advances-nests-audio-rooms-with-moq-interop-testing)、[nostream 的 NIP-65 和 NWC](#nostream-adds-nip-65-relay-list-support-and-nwc-payments)、[FIPS 基于 Nostr 的 udp:nat 引导](#fips-adds-nostr-based-udpnat-bootstrap)、[strfry 可观测性](#strfry-adds-per-connection-observability)、[Sprout 所有者证明](#sprout-adds-owner-attestation-and-multi-workspace-support) 和 [Zap Cooking 食谱包](#zap-cooking-adds-recipe-packs-delete-requests-and-bunker-login)。新纳入跟踪的项目包括 [Nostrord](#nostrord-a-nip-29-client-built-with-kotlin-multiplatform-and-wasm)、[Clave](#clave-brings-nip-46-remote-signing-to-ios-via-apns)、[Treasures](#treasures-decentralized-geocaching-on-nostr)、[smesh](#smesh-v051-self-hosted-nostr-relay-client-and-signer-in-one-stack)、[Surveil](#surveil-a-magic-the-gathering-deck-builder-on-nostr)、[Fundstr、Nod City、deploy-nsite-to-pages 和 null--nostr](#smaller-additions-fundstr-nod-city-deploy-nsite-to-pages-and-null-nostr)。月末回顾涵盖了 2021 年至 2026 年的 Nostr 四月。

## 头条报道

### GitWorkshop 推出浏览器内 PR 合并、仓库关注和带宽高效的 git 浏览器

[GitWorkshop](https://gitworkshop.dev) 是 Dan Conway 为 [NIP-34](/zh/topics/nip-34/) git-over-Nostr 打造的基于 Web 的协作层，本周发布了一次重大更新，让工作流程更接近开发者对 GitHub 或 GitLab 的期望，同时将评论、仓库列表和通知保留在已签名的 Nostr 事件中。

最引人注目的新增功能是期待已久的浏览器内 PR 合并按钮，适用于使用 GRASP relay 的仓库。此版本还添加了基于反应和 [NIP-51](/zh/topics/nip-51/) 列表构建的 Stars 和仓库关注功能，固定的仓库集合以 kind `10617` 事件发布，通过有序的 `a` 标签指向 kind `30617` 仓库公告。个人资料页面现在可以展示一个可移植的仓库列表。

带宽高效的 git 浏览器取代了之前的浏览器内浅克隆。新的浏览器依赖 GRASP 底层的 git client/server 协议，因此可以处理大型仓库，无需强制浏览器获取完整的 pack。搜索现在覆盖用户名和仓库元数据，由 [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) 和一个 `ngit-indexer` relay 实现提供支持，该实现在网络中发现并同步仓库公告。浏览器内的仓库创建工作流程完善了发现和入门路径。

审查工具围绕 Files Changed 标签页、每个 patch 的 diff 查看器以及一套实验性新原语进行了重建。内联代码审查评论使用 kind `1111`，基于 [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) 构建：每条评论指向一个文件路径（`f` 标签）、一个 commit SHA（`c` 标签）和一个选定的行范围（`line` 标签），以便 client 可以在 diff 中的正确位置渲染评论。第二层实验性原语由作者和 repo 维护者授权，并使用 [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) 标签：提交后重命名 Issue 或 PR 主题、提交后添加话题标签、将版本控制的 CoverNote 固定在 PR 或 Issue 顶部作为可编辑摘要，以及将内联代码讨论子线程标记为已解决。Verdict 事件和 `suggestion` 块仍处于草稿阶段，尚未发布。

跨设备的通知状态也通过 Nostr 同步，但带有一个保护隐私的巧妙设计。GitWorkshop 生成一个专用的通知 keypair，加密该 nsec，并将其存储在 kind `30078` 事件中。通知 nsec 随后签名实际的通知状态事件。这种间接方式防止了用户的主 signer 在每次读取或存档操作时被频繁的加密和解密请求淹没，同时也阻止了外部观察者轻易看到用户何时操作其通知状态。用户可以跨设备同步已读和存档状态；relay 只能看到加密的 blob。

### Routstrd 推出面向 Nostr 上推理的本地路由器

[Routstrd](https://github.com/routstr/routstrd) 是一个新的 TypeScript 守护进程，它为本地工具提供一个与 OpenAI 兼容的端点，并将每个请求路由到相互竞争的 [Routstr](https://routstr.com) 提供商。该守护进程通过 Routstr 的 RIP-02 规范中定义的 Nostr kind `38421` 公告发现提供商。然后根据 RIP-06 按价格、信任度和近期性能对提供商进行评分，并将每个请求发送到当前最佳选项。

支付通过由 cocod 管理并由 Lightning 充值的本地 Cashu 钱包运行。这为 client 提供了一个以 sats 计价的结算路径，同时通过 Nostr relay 保持提供商发现的公开和无需许可。如果提供商在会话期间失败，Routstrd 可以回退到下一个排名的节点。安装路径是 `bun install -g routstrd`，然后运行 `routstrd onboard` 进行钱包和 relay 设置。

更广泛的 [Routstr 组织](https://github.com/routstr) 维护该守护进程、Python 节点软件（`routstr-core`）、一个聊天 UI 和协议规范。对用户而言，本地端口成为稳定的接口：现有的 OpenAI 兼容工具指向 Routstrd，而守护进程处理提供商发现、路由和支付。

## 带标签的发布

### ngit v2.4.2 修复了 PR 提交的 GRASP server 检测

[ngit](https://codeberg.org/DanConwayDev/ngit-cli) 发布了 [v2.4.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.2)，修复了仓库 GRASP server 检测问题，当提议使用 PR kind 时使 PR 提交保持在正常路径上。请注意，ngit 目前对大多数更改默认使用 `Patch` kind，除非它们很大；维护者正在努力更改这个默认值。本周早些时候发布的 [v2.4.1](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.1) 修复了当开放 PR 的 git 数据在仓库指定的 git server 上不可用时，clone 和 fetch 期间出现的 `fatal` 错误。

### Wisp v1.0.0 从 beta 毕业

[Wisp](https://github.com/barrydeen/wisp) 是一个专注于 relay 路由、隐私和小型原生 UI 的 Kotlin 和 Jetpack Compose Android client，发布了 [v1.0.0](https://github.com/barrydeen/wisp/releases/tag/v1.0.0) 并接着发布了 [v1.0.2](https://github.com/barrydeen/wisp/releases/tag/v1.0.2)。1.0.0 里程碑汇集了 [Newsletter #19](/zh/newsletters/2026-04-22-newsletter/#wisp-v0180-beta-adds-normie-mode-for-you-feed-and-nip-29-group-config) 中报道的 Normie Mode 法币计价切换、For You 信息流、[NIP-29](/zh/topics/nip-29/) 基于 relay 的群组配置，以及 [NIP-65](/zh/topics/nip-65/) relay 列表广播。v1.0.2 增加了 Android 15 16 KB 页面大小支持、抽屉页中的 QR 扫描标签页、内联视频控件的下载按钮，以及通知列表性能修复。

### grain v0.5.2 修复 WebSocket 锁死，v0.5.3 继续打磨

[grain](https://github.com/0ceanSlim/grain) 是来自 0ceanSlim 的 Go relay，发布了 [v0.5.2](https://github.com/0ceanSlim/grain/releases/tag/v0.5.2) 作为对 v0.5.0 引入的 WebSocket 锁死问题的关键热修复，然后发布了 [v0.5.3](https://github.com/0ceanSlim/grain/releases/tag/v0.5.3)。该锁死会导致连接在某些过滤器和 WebSocket 路径下挂起，因此 v0.5.1 或 v0.5.0 上的运营者应该升级。grain 跟踪所有主要的 Nostr 事件类别，公开 NIP-11 relay 信息，支持白名单/黑名单访问控制、按 kind 限速、Web 仪表板，以及在 v0.5.x 系列中添加的 Go client 库。

### Mostro Core v0.10.0 和 Mostro Mobile v1.2.5 采用 NIP-59 双密钥 gift wrap

[Mostro Core v0.10.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.10.0) 添加了新的 [NIP-59](/zh/topics/nip-59/) gift-wrap 模块，具有分离的身份和交易密钥。早期的传输代码使用单个身份密钥同时用于交易身份和 gift wrapping。v0.10.0 将稳定的交易身份与临时的 wrapping 密钥分离，因此每次交易可以使用新的传输密钥，同时保留交易协议所需的身份。守护进程集成通过 [Mostro PR #718](https://github.com/MostroP2P/mostro/pull/718) 落地，[mostro-cli PR #165](https://github.com/MostroP2P/mostro-cli/pull/165) 将相同的迁移带入命令行 client。

[Mostro Mobile v1.2.5](https://github.com/MostroP2P/mobile/releases/tag/v1.2.5) 与协议工作一同发布。[PR #581](https://github.com/MostroP2P/mobile/pull/581) 让 takers 可以按 maker 的账户年龄过滤订单，为用户提供了一种避免订单簿中新创建 maker 账户的方式。[PR #580](https://github.com/MostroP2P/mobile/pull/580) 修复了已取消订单详情上的角色标签，[PR #576](https://github.com/MostroP2P/mobile/pull/576) 清理了协作取消按钮。

### marmot-ts v0.5.0 推出可寻址 KeyPackages

[marmot-ts](https://github.com/marmot-protocol/marmot-ts) 发布了 [@internet-privacy/marmot-ts@0.5.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/%40internet-privacy%2Fmarmot-ts%400.5.0)，这是 TypeScript [Marmot](/zh/topics/marmot/) client 的第一个计划中的破坏性变更版本。[PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) 添加了可寻址 KeyPackage 支持：`KeyPackageManager` 现在可以同时处理旧的 kind `443` 和新的 kind `30443` KeyPackage 事件。该版本移除了 `KeyPackageStore` 和 group-state 存储类，将其替换为传入 `KeyPackageManager` 和 `MarmotGroup` 的通用键值存储。它还将邀请和群组管理移到了 `MarmotClient.invites` 和 `MarmotClient.groups` 上，因此直接嵌入者在升级前需要进行构造函数和存储更改。

### CruxCoach v0.1.3 推出使用 Nostr 和 Blossom 的加密攀登数据备份

[CruxCoach](https://codeberg.org/CruxCoach/CruxCoach) 是一款面向 Kilter Board 攀登者的新开源 Android 应用。Kilter Board 是一个交互式训练墙，其把手通过 Bluetooth 亮起以显示路线。该应用于 4 月 14 日推出，并在 4 月 26 日达到 [v0.1.3](https://codeberg.org/CruxCoach/CruxCoach/releases/tag/v0.1.3)。

v0.1.3 添加了可选的加密云备份。用户的 CruxCoach 账户是一个 Nostr keypair，私钥同时作为本地备份加密密钥的输入。该应用在设备上加密攀登数据，并将密文镜像到 Blossom 存储服务器（`blossom.primal.net` 和 `nostr.download`）。删除远程操作会调用 Blossom 清理路径。除了备份，CruxCoach 使用 [NIP-46](/zh/topics/nip-46/) 远程签名以支持 Amber、[NIP-17](/zh/topics/nip-17/) 私密 DM 用于应用内开发者联系、[NIP-65](/zh/topics/nip-65/) relay 列表用于 relay 发现，以及 Vitor Pamplona 的 [Quartz](https://github.com/vitorpamplona/quartz) 库用于 Nostr 底层管道。用户可以通过 Zapstore 或直接从 Codeberg APK 安装它。

### Meiso v1.3.0 添加子任务、Blossom 附件和 NIP-89 标签

[Meiso](https://github.com/higedamc/meiso) 是一个极简的 Flutter 任务管理器 for Android，将任务作为 [NIP-44](/zh/topics/nip-44/) 加密的 kind `30078` 应用数据存储在 Nostr relay 上。4 月 6 日发布的 [v1.3.0](https://github.com/higedamc/meiso/releases/tag/v1.3.0) 添加了带有父子关系的子任务、用于 blocks/blocked-by/related-to/duplicate-of 的任务链接、通过 Blossom 和 [NIP-96](/zh/topics/nip-96/) HTTP 文件上传端点的图片附件、在已发布事件上的 [NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md) 推荐应用 `client` 标签，以及一个 Go 命令行同步工具。v1.3.0 还修复了冷启动 relay 行为和 Amber client 复用问题。

### NoorNote、Nostria、Nostr Calendar、nos2x-fox 和库发布

[NoorNote](https://github.com/77elements/noornote) 发布了 [v0.8.7](https://github.com/77elements/noornote/releases/tag/v0.8.7)、[v0.8.8](https://github.com/77elements/noornote/releases/tag/v0.8.8) 和 [v0.8.9](https://github.com/77elements/noornote/releases/tag/v0.8.9)。这些版本修复了引用转发中的图片和视频点击处理、为长文文章图片添加了灯箱支持，并修复了空白的桌面启动屏幕。[Nostria](https://github.com/nostria-app/nostria) 发布了 [v3.1.29](https://github.com/nostria-app/nostria/releases/tag/v3.1.29)、[v3.1.30](https://github.com/nostria-app/nostria/releases/tag/v3.1.30) 和 [v3.1.31](https://github.com/nostria-app/nostria/releases/tag/v3.1.31)，添加了文章编辑器图片压缩、钱包 USD 切换、推广卡片控件、PDF 支持和移动布局打磨。

[Nostr Calendar v1.4.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.1) 将日历事件发布与日历列表管理解耦，并修复了邀请跟踪。[nos2x-fox v1.19.0](https://github.com/diegogurpegui/nos2x-fox/releases/tag/v1.19.0) 为 Firefox NIP-07 浏览器签名授权添加了自定义授权时间范围。[nostr-double-ratchet v0.0.97](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.97) 发布了新的二进制文件。[nostr-wot-sdk 0.9.0](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%400.9.0) 默认挂载 `NostrSessionProvider`，[nostr-tools PR #535](https://github.com/nbd-wtf/nostr-tools/pull/535) 为 NIP-47 wallet-connect 字符串添加了多 relay 解析支持。

本周晚些时候，[Amber v6.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre1) 发布了一个预发布版，改进了 connect-new-app 布局、signer 对话框修复、改进的通知权限处理和重构的账户选择。[nostr-vpn v0.3.14](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.14) 发布了新的构建，包含 macOS Apple Silicon、Linux 和 Windows 制品。[Bitcredit Core v0.5.7-hotfix-1 和 v0.5.8](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.8) 连续发布了对孤立区块验证问题的修复。[Surveil v0.1.6](https://gitlab.com/chad.curtis/surveil/-/tags/v0.1.6) 带来了移动 UI 打磨和全面改版的 About 页面；项目本身在 [下文](#surveil-a-magic-the-gathering-deck-builder-on-nostr) 中介绍。

### applesauce 6.0.0 移除遗留事件工厂并添加 Blossom URI 解析

[applesauce](https://github.com/hzrd149/applesauce) 是 hzrd149 的 TypeScript Nostr 工具包，在 monorepo 中发布了 6.0.0 版本系列。[applesauce-core@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.0.0) 移除了遗留的 `EventFactory` 类和旧的 `buildEvent`、`modifyEvent` 和 `createEvent` 辅助函数，推动调用者使用 `applesauce-core/factories` 和 `applesauce-common` 中较新的工厂类。它还为链接解析添加了 IP 地址和 localhost 处理、BUD-10 Blossom URI 正则表达式，以及新的 observable 辅助函数，如 `timeoutWithIgnore`、`combineLatestBy`、`combineLatestByIndex` 和 `combineLatestByKey`。

包级别的发布填补了 Nostr 特定的部分。[applesauce-content@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-content%406.0.0) 为文本和 Markdown 添加了 BUD-10 Blossom URI 节点，为渲染器提供了在内容中解析 Blossom 引用的一流方式。[applesauce-actions@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-actions%406.0.0) 为覆盖 relay、用户和项目的 NIP-51 列表添加了基础工厂类，让列表构造不再临时拼凑。[applesauce-wallet-connect@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet-connect%406.0.0) 暴露了 `WalletConnect.connectURI`，因此应用可以直接访问现有的 NIP-47 wallet-connect URI。

## 未发布的更改

### Amethyst 推进 Nests 音频室并进行 MoQ 互操作测试

[Amethyst](https://github.com/vitorpamplona/amethyst) 本周合并了几个专注于 Nests 的 PR，在上周的 [Media over QUIC](https://datatracker.ietf.org/group/moq/about/) 音频室栈的基础上继续构建。[PR #2622](https://github.com/vitorpamplona/amethyst/pull/2622) 添加了一个跨 client 互操作测试工具，将 Amethyst MoQ client 与参考 Web 实现进行对比测试。目标是在用户遇到问题之前捕捉 Android/浏览器的线级差异。[PR #2625](https://github.com/vitorpamplona/amethyst/pull/2625) 改进了画中画的发言者焦点和连接状态，而 [PR #2620](https://github.com/vitorpamplona/amethyst/pull/2620) 澄清了参与者网格中的头像、静音状态和发言状态。本周晚些时候，[PR #2634](https://github.com/vitorpamplona/amethyst/pull/2634) 修复了全屏 Nest 视图中的 IME 内边距和窗口 insets，[PR #2635](https://github.com/vitorpamplona/amethyst/pull/2635) 为 Nests 信息流添加了基于在场状态的新鲜度过滤。另外，[PR #2627](https://github.com/vitorpamplona/amethyst/pull/2627) 移除了 Amethyst 的自定义 C secp256k1 实现，迁移到 `libschnorr256k1`。

### nostream 添加 NIP-65 relay 列表支持和 NWC 支付

[nostream](https://github.com/Cameri/nostream) 在上周 53 个 PR 的 relay 冲刺之后合并了三个值得关注的 PR。[NIP-65](/zh/topics/nip-65/) relay 列表元数据支持在 [PR #585](https://github.com/Cameri/nostream/pull/585) 中落地，因此 relay 可以索引和提供 kind `10002` relay 列表事件。Nostr Wallet Connect 支付处理器在 [PR #539](https://github.com/Cameri/nostream/pull/539) 中跟进，添加了 pay-to-relay 路径。连接清理在 [PR #438](https://github.com/Cameri/nostream/pull/438) 中得到改进，该 PR 关闭了一个死连接 bug，即具有活动订阅的 socket 没有被回收，导致长时间运行的实例上订阅计数漂移。

### FIPS 添加基于 Nostr 的 udp:nat 引导

[FIPS](https://github.com/jmcorgan/fips) 是 Free Internetworking Peering System，此前在 [Newsletter #6](/zh/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking) 和 [Newsletter #10](/zh/newsletters/2026-03-25-newsletter/#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples) 中有报道，合并了 [PR #53](https://github.com/jmcorgan/fips/pull/53)，带来基于 Nostr 的 `udp:nat` 引导。该变更让节点可以发布 Nostr 广告、交换加密的 offer/answer 信令、通过 STUN 发现公共地址、执行 UDP 打洞，并将打通的 socket 交给正常的 FIPS 传输栈。该实现将信令 payload 身份绑定到实际的 Nostr 发送者，查询已配置的 DM 和广告 relay 用于收件箱查找，并回滚失败的采纳穿越交接，以防孤立的 UDP 传输保持活动。这是要在规范仓库 `jmcorgan/fips` 中跟踪的 Nostr 公告和 NAT 穿越工作。

### strfry 添加每连接可观测性

[strfry](https://github.com/hoytech/strfry) 合并了 [PR #214](https://github.com/hoytech/strfry/pull/214)，添加了每连接可观测性和可通过 Prometheus 导出的连接级指标。[PR #204](https://github.com/hoytech/strfry/pull/204) 规范化了 Prometheus 标签，[PR #215](https://github.com/hoytech/strfry/pull/215) 在文档中添加了 Community Integrations 章节，涵盖构建在 strfry 之上的 Namecoin 身份项目。

### Sprout 添加所有者证明和多工作区支持

[Sprout](https://github.com/block/sprout) 是 Block 的 Nostr client，合并了 [PR #406](https://github.com/block/sprout/pull/406)，实现了 NIP-OA（所有者证明）。该功能为自主 agent 提供了一个加密证明，证明特定的人类 pubkey 授权了它的操作。[PR #409](https://github.com/block/sprout/pull/409) 为桌面应用添加了多工作区支持，[PR #411](https://github.com/block/sprout/pull/411) 为移动编辑添加了 `#channel` 自动完成，[PR #410](https://github.com/block/sprout/pull/410) 关闭了一个可能丢弃活动 channel 消息的竞态窗口。[PR #413](https://github.com/block/sprout/pull/413) 引入了用于跨设备已读状态同步的 NIP-RS，后续的 [PR #420](https://github.com/block/sprout/pull/420) 和 [PR #422](https://github.com/block/sprout/pull/422) 将该已读状态连接到移动端的未读徽章。

### Zap Cooking 添加食谱包、删除请求和 bunker 登录

[Zap Cooking](https://github.com/zapcooking/frontend) 合并了一周富有成效的食谱发布工作。用于用户自己食谱包的 [NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md) 删除请求在 [PR #367](https://github.com/zapcooking/frontend/pull/367) 中落地。发布可靠性通过 [PR #366](https://github.com/zapcooking/frontend/pull/366) 得到改进，该 PR 强制每个新食谱使用 garden relay，并为共享食谱集添加了重试队列。一键式已授权包发布在 [PR #365](https://github.com/zapcooking/frontend/pull/365) 中落地，[PR #331](https://github.com/zapcooking/frontend/pull/331) 添加了 [NIP-46](/zh/topics/nip-46/) bunker 登录支持。

### Whitenoise-rs 加密其本地数据库

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) 合并了 [PR #758](https://github.com/marmot-protocol/whitenoise-rs/pull/758)，为磁盘上的 Whitenoise 数据库添加了 SQLCipher 加密。这弥补了 Marmot 守护进程栈长期存在的静态数据安全缺口。[PR #775](https://github.com/marmot-protocol/whitenoise-rs/pull/775) 暴露了群组所需的能力，[PR #772](https://github.com/marmot-protocol/whitenoise-rs/pull/772) 将群组媒体操作迁移到会话拥有的 `MediaOps`，[PR #773](https://github.com/marmot-protocol/whitenoise-rs/pull/773) 作为会话操作重构的一部分提取了一个 `SharedServices` 持有者。在移动端，[whitenoise PR #577](https://github.com/marmot-protocol/whitenoise/pull/577) 为 Android 前台服务启用了启动自动重启，修复了守护进程在设备重启后无法恢复的情况。

## 新纳入跟踪和发现

### Nostrord：使用 Kotlin Multiplatform 和 WASM 构建的 NIP-29 client

[Nostrord](https://github.com/nostrord/nostrord) 是一个针对 Discord 替代用例的新 [NIP-29](/zh/topics/nip-29/) 群组聊天 client。群组存在于 Nostr relay 上，具有 relay 强制的成员资格、角色、审核和访问控制，因此群组状态由所选的 NIP-29 relay 托管。client 开发者不控制这些群组的独立应用数据库。Web 应用运行在 [web.nostrord.com](https://web.nostrord.com)，使用 Kotlin Multiplatform 编译为 WebAssembly 构建，原生 Android、iOS 和桌面构建正在开发中。Nostrord 是 [OpenSats](https://opensats.org) 资助的获得者，并与 Flotilla、Chachi 和 0xChat 使用的相同 NIP-29 relay 互操作。

### Clave 通过 APNs 将 NIP-46 远程签名带到 iOS

[Clave](https://github.com/DocNR/clave) 是一个处于 beta 阶段的 iOS 远程 signer，在应用未打开时签名 Nostr 事件。私钥保留在 iPhone Keychain 中。当 client 发送 [NIP-46](/zh/topics/nip-46/) 远程签名请求时，服务器端代理传递一个 Apple Push Notification，唤醒一个 Notification Service Extension 最多 30 秒。该扩展使用 [NIP-44](/zh/topics/nip-44/) 加密解密请求，使用 Keychain 密钥签名，并发布响应。设备 token 注册使用 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) HTTP Auth 防止 token 劫持。Clave 支持 `bunker://` 和 `nostrconnect://` 配对、每 client 信任级别、每 kind 覆盖，并已使用 Nostur 和 noStrudel 进行测试。

### Treasures：Nostr 上的去中心化地理藏宝

[Treasures](https://gitlab.com/chad.curtis/treasures) 是一个地理藏宝平台，其中藏宝点和发现是已签名的 Nostr 事件。藏宝点创建者发布带有 GPS 坐标的 kind `37516` 可寻址事件。发现者通过扫描附加在实体藏宝点上的 QR code 记录发现；该 code 编码了创建者 pubkey、藏宝点 `d` 标签，以及一个用作实体访问证明的验证私钥。[NIP-57](/zh/topics/nip-57/) zaps 可以从发现者流向藏宝点创建者，实时应用位于 [treasures.to](https://treasures.to)。

### smesh v0.5.1：一个栈中的自托管 Nostr relay、client 和 signer

[smesh](https://git.smesh.lol/smesh/smesh) 是一个用 Moxie 编写的自托管 Nostr 栈，Moxie 是 mleku 从 Go 和 TinyGo 派生的自定义语言。该栈提供一个原生 relay 二进制文件，支持 HTTP、WebSocket、AUTH、search 和 Blossom；`sm3sh`，一个编译为 ES 模块的 Web client；以及一个具有 NIP-07 浏览器签名以及 NIP-04 和 NIP-44 加密支持的浏览器 signer 扩展。最近的工作包括 v0.5.0 中的 MLS（RFC 9420）群组消息、用于 relay 同步的 negentropy 集合协调，以及一个 Web of Trust 图引擎。代码位于 mleku 的自托管 forge `git.smesh.lol` 上，使用他自己的 `git-web` 工具构建。相关的 [gitea-nostr-auth](https://git.smesh.lol/smesh/gitea-nostr-auth) 仓库是 Gitea 的 OAuth2/OIDC 桥接：用户使用 NIP-07 浏览器 signer 进行身份验证，桥接通过 NIP-65 发现 relay，Gitea 接收标准 OIDC 身份声明。

### Surveil：Nostr 上的《万智牌》套牌构建器

[Surveil](https://gitlab.com/chad.curtis/surveil) 是一个面向《万智牌》玩家的 Nostr client，让用户可以搜索卡牌、构建套牌、在 Android 上使用设备端 ML Kit OCR 扫描纸质卡牌，并在网络上分享套牌。套牌作为 kind `37381` 可寻址事件发布，套牌事件规范记录在项目的 `NIP.md` 中。社交层由标准 Nostr 原语构建：NIP-22（kind `1111`）针对每个套牌范围的线程评论、NIP-25（kind `7`）反应、[NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md)（kind `30078`）用于玩家主页的个人资料数据、kind `3` 关注信息流，以及带回原始套牌的 `a` 标签的分叉。[v0.1.6](https://gitlab.com/chad.curtis/surveil/-/tags/v0.1.6) 本周发布，带来了移动 UI 打磨、生命计数器改进、全面改版的 About 页面，以及套牌头图横幅上的 relay 药丸。Web 应用在任何提供静态 HTML 的地方运行，Android 构建通过 [Zapstore](https://zapstore.dev) 发布，kind `37381` 事件也由 [Ditto](https://about.ditto.pub/reference) 原生索引为 Magic 套牌。仓库在 GitLab 上，位于 [chad.curtis/surveil](https://gitlab.com/chad.curtis/surveil)。

### 较小的新增：Fundstr、Nod City、deploy-nsite-to-pages 和 null--nostr

[Fundstr](https://github.com/ritty65/Fundstr) 是一个 Nostr 上的创作者资助平台，使用 Cashu ecash 进行一次性和定期捐款，具有创作者等级定义和 Nostr DM。[Nod City](https://nod.city) 是一个 Bitcoin 服务评论网站，评论是已签名的 Nostr 事件，评论者可以接收 zaps；未找到公开源仓库。[deploy-nsite-to-pages](https://github.com/Origami74/deploy-nsite-to-pages) 是一个 GitHub Action，通过使用 `nsyte download` 将 nsite 镜像到 GitHub Pages，支持根 kind `15128` 和命名 kind `35128` 的 nsite。本周 NIP-34 数据中也发现的 [null--nostr](https://github.com/tami1A84/null--nostr) 是最近的 OpenSats 波中作为 Nurunuru 涵盖的 client；它支持 MLS 群组消息、Amber、NIP-50 搜索、NIP-70 保护帖子、ProofMode 徽章和 Zapstore 分发。

FIPS 对 Compass 来说不是新项目。它在 [Newsletter #6](/zh/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking) 和 [Newsletter #10](/zh/newsletters/2026-03-25-newsletter/#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples) 中报道过。数据库现在指向正确的规范仓库 [jmcorgan/fips](https://github.com/jmcorgan/fips)，本周的 NIP-34 发现也浮现了相关的 git-over-Nostr 镜像，如 `fips` 和 `awesome-fips`。

## 协议工作

### NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips) 中的近期提议和讨论：

**本周合并：**

- **NIP-34 git 仓库：移除未使用的 refs 标签扩展**（[PR #2325](https://github.com/nostr-protocol/nips/pull/2325)）：从 [NIP-34](/zh/topics/nip-34/) 中移除了一个已定义但未使用的 `refs` 标签扩展。此清理减少了 git-over-Nostr 工具的实现歧义。

- **NIP-34 git 仓库：移除不正确的 NIP-09 声明**（[PR #2326](https://github.com/nostr-protocol/nips/pull/2326)）：移除了一个不正确的声明，即 [NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md) 删除事件可以重置仓库状态。NIP-09 删除是 client 端的事件删除请求，不是仓库状态机。此更正防止 NIP-34 实现者将删除提示视为权威的仓库重置。

**开放和实现驱动的工作：**

- **GitWorkshop kind `1111` 内联审查评论**：内联代码审查评论 kind 记录在 GitWorkshop 的 `NIP.md` 中，现在正在积极使用，但尚未作为正式 NIP 提议。Verdict 事件（kind `7321`）和 `suggestion` 块仍处于草稿阶段，尚未发布。来自 GitWorkshop 和 ngit 的实现反馈将决定这些形状是成为独立的 git-review NIP，还是仍作为叠加在 NIP-34 之上的应用约定。

- **Nostr mail core 和 Nostrmon**：本周有两个新的自定义 NIP 草案在流传。[Nostr mail core](https://njump.me/57d11cdf2f9ed73f7f39d6a7a6012ee3d642584ab11887f96a031f7d00fd9697) 提议 kind `1301` 用于 RFC 2822 电子邮件内容，使用 NIP-59 包装以进行私密传递，并通过 NIP-05 解析的桥接 pubkey 桥接到旧电子邮件。[Nostrmon](https://njump.me/5e9a8cee19d464f5f0322518ac9ccaf2399c69da6572346b4fb12d36acb17a27) 勾勒了区域、地图、生物、NPC、玩家存档和物品的可寻址事件 kind。两者仍是自定义草案，不是合并的 NIP。

- **NIP-67：EOSE 完整性提示**（[PR #2317](https://github.com/nostr-protocol/nips/pull/2317)）：该提议继续迭代，为 `EOSE` 添加一个正向完整性标记，允许 relay 区分"已存储事件已完全交付"与旧的 `EOSE` 情况，在后者中 relay 不做完整性声明。

## 六个 Nostr 四月

四月给出了 Nostr 发展路径的清晰横截面：2021 年的协议文档、2022 年的早期 client 工作、2023 年的后 Damus 应用浪潮、2024 年的私密消息和 git-over-Nostr 工作、2025 年的 Blossom 和 relay 列表清理，以及 2026 年的以采用为重点的 client 资助。

### 2021 年 4 月：NIPs 仓库之前的协议文档

Fiatjaf 于 2020 年 11 月 20 日发布了最初的 Nostr 文章 ["Notes and Other Stuff Transmitted by Relays"](https://fiatjaf.com/nostr.html)。那第一份文本已经包含了至今仍定义该协议的核心形态：用户用密钥签名事件，将它们发布到 relay，并从他们选择的 relay 读取。[`nostr-protocol/nostr` 提交日志](https://github.com/nostr-protocol/nostr/commits?since=2021-04-01&until=2021-04-30) 显示 4 月 1 日至 4 月 30 日之间没有提交。活动位于两侧：2021 年 3 月的提交添加了早期的"nostwitter"链接和一个 `kind` 过滤器，而 2021 年 5 月重新调整了 NIP-02 的用途并添加了 NIP 作者身份。

2021 年 4 月，没有公开的 client 市场，没有可见的 relay 网络，也没有 NIPs 仓库。该协议仍作为一份小文档和一些实验存在。Nostr 尚未成为社交网络或开发平台。它仍是一个 relay/key/event 模型，等待着它的第一波持续贡献者浪潮。

### 2022 年 4 月：NIPs 仍在主仓库中

2022 年 4 月是 NIPs 从主 `nostr-protocol/nostr` 仓库中移出之前的最后一个月。由于拆分尚未发生，专用的 [`nostr-protocol/nips`](https://github.com/nostr-protocol/nips) 仓库没有 4 月的 pull request 历史。在主仓库中，落地了三个 4 月提交：4 月 8 日 goswami1999 的 ["Update readme to add nip12"](https://github.com/nostr-protocol/nostr/commit/bae286312a233b971bee5429adda7aff41747eb8)、4 月 25 日 jb55 的 ["add kinds list"](https://github.com/nostr-protocol/nostr/commit/4b9e9d123273ba8a5c70d77df46922070c11c11d) 和 4 月 28 日 steliosrammos 的 ["add js formatting to sample code"](https://github.com/nostr-protocol/nostr/commit/759997657f07e0344064228ffe5e93febe85d367)。

Client 工作也开始成形。2022 年 4 月的 Damus 提交添加了早期的聊天室行为、个人资料处理和应用图标，而 nostr-tools 正在成为早期 client 和实验的 JavaScript 库路径。在协议方面，NIP-12 通用标签查询为标签搜索提供了一个有文档的地方，kinds 列表将 Nostr 移向注册表模型，更好的 JavaScript 示例使规范更容易被 client 和库作者实现。5 月 1 日，fiatjaf 将 NIPs 移到了专用仓库。2022 年 4 月是原始单仓库时代的最后一个月。

### 2023 年 4 月：后 Damus 应用扩张

2023 年 4 月是在 2023 年 1 月 31 日 Damus 在 iOS App Store 上线三个月之后，也是在 Jack Dorsey 发布他的 Nostr 公钥之后。网络刚刚吸收了它的第一次主要公众增长浪潮。Damus、Snort、Iris、Coracle 和 Amethyst 等 client 处于活跃状态，而 relay 运营者正在了解更大的社交图对带宽、垃圾信息、搜索和审核假设的影响。

2023 年 4 月有一个合并的 NIPs PR：[PR #456](https://github.com/nostr-protocol/nips/pull/456)，于 4 月 17 日合并，将 NIP-19 bech32 实体链接添加到 NIP-21 URI 处理。周围的提交显示了协议工作背后的应用压力。2023 年 4 月看到了 [NIP-45 COUNT](https://github.com/nostr-protocol/nips/commit/8b39976e78f90fe766ad7149e250777cddacbb5e)、事件特定 zap 标记、[NIP-15 marketplace](https://github.com/nostr-protocol/nips/commit/bf0a0da6a48b96467172414d8e41dc72b0ca379c)、NIP-26 删除委托语义、NIP-94 文件元数据、NIP-47 wallet-connect 错误处理，以及 [NIP-30 自定义 emoji](https://github.com/nostr-protocol/nips/commit/e91ce3409e1ce8267fc07a21784d2538621267c3) 的工作。贡献者列表已扩展到包括 fiatjaf、staab、pablof7z、Semisol、CodyTseng、sethforprivacy、mikedilger、AsaiToshiya、alexgleason、martindsq、frbittencourt 和 arkin0x。

Damus、Snort、Iris、Coracle 和 Amethyst 不再是围绕规范的演示；它们是生产 client，处理入门、信息流、垃圾信息、zaps、媒体和 relay 选择。2023 年 4 月的协议工作读起来就像这些 client 创建的待办事项：zaps、marketplace、文件元数据、计数、emoji 和身份链接都将规范推向了简单笔记和关注之外。

### 2024 年 4 月：私密消息、git-over-Nostr 和维护者支持

2024 年 4 月有两个 NIP PR 合并。4 月 10 日合并的 [PR #1167](https://github.com/nostr-protocol/nips/pull/1167) 修复了 [NIP-46](/zh/topics/nip-46/) 远程签名中令人困惑的术语，其中 client 和 signer 需要对请求和授权的操作使用精确的语言。4 月 17 日合并的 [PR #1108](https://github.com/nostr-protocol/nips/pull/1108) 扩展了 [NIP-34](/zh/topics/nip-34/) git 仓库，加入了状态事件、澄清、可选的维护者、repo 标识符和可发现性标签。这一步让 git-over-Nostr 对 ngit 以及后来的 GitWorkshop 更实用。

[NIP-17](https://github.com/nostr-protocol/nips/commit/df30012430c88d49fb5b124992b04d5c61b6338b)，原为 NIP-24，于 4 月 24 日作为密封的 gift-wrapped 消息落地，用于私密 DM 和小型群组聊天。Client 和库工作并行进行：Amethyst、Primal、Gossip、nostr-tools、NDK 和 rust-nostr 在同一时期都很活跃。

OpenSats 也在 2024 年 4 月宣布了对 Nostr 开发者的长期支持：4 月 9 日的 [PabloF7z](https://opensats.org/blog/pablofz7-receives-lts-grant)、4 月 12 日的 [Stuart Bowman](https://opensats.org/blog/stuart-bowman-receives-lts-grant) 和 4 月 15 日的 [hzrd149](https://opensats.org/blog/hzrd149-receives-lts-grant)。这些资助将资金从孤立的项目资助转向 relay、库和 client 基础设施的持续维护。

### 2025 年 4 月：密集的 NIP 清理和 Blossom 正式化

2025 年 4 月是本回顾中最密集的协议月份，有十六个合并的 NIPs PR。该月始于 [PR #1846](https://github.com/nostr-protocol/nips/pull/1846)，为 NIP-73 添加了区块链交易和地址，以及 [PR #1865](https://github.com/nostr-protocol/nips/pull/1865)，将 NIP-C0 标签添加到标准化标签表。它继续以 [PR #1801](https://github.com/nostr-protocol/nips/pull/1801) 和 [PR #1889](https://github.com/nostr-protocol/nips/pull/1889)，两者都改进了 kind `10002` relay 列表重新发布指导，以及 [PR #1879](https://github.com/nostr-protocol/nips/pull/1879)，缩小并澄清了 [NIP-65](/zh/topics/nip-65/)。

[PR #1822](https://github.com/nostr-protocol/nips/pull/1822) 为 Blossom 交互添加了 NIP-B7，在超过一年的非正式实践后，为 Nostr client 和 Blossom 服务器提供了一个规范的协调层。[PR #1051](https://github.com/nostr-protocol/nips/pull/1051) 弃用了 [NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md)，即委托事件签名规范。NIP-26 一直难以安全实现，并且随着 NIP-46 和其他 signer 模式的成熟而变得不那么有吸引力。

该月剩余的时间将清理与应用扩展相结合：[PR #1882](https://github.com/nostr-protocol/nips/pull/1882) 为 [NIP-11](/zh/topics/nip-11/) 添加了隐私政策和服务条款字段，[PR #1849](https://github.com/nostr-protocol/nips/pull/1849) 在 NIP-B0 下扩展了 kind `39701` Web 书签，[PR #1891](https://github.com/nostr-protocol/nips/pull/1891) 将该书签 kind 添加到 README，[PR #1895](https://github.com/nostr-protocol/nips/pull/1895) 添加了 NIP-B0 标准化标签。OpenSats 于 4 月 16 日宣布了其 [第十一波 Nostr 资助](https://opensats.org/blog/eleventh-wave-of-nostr-grants)，资助了 Swae、HAMSTR、Vertex、Nostr Double Ratchet 和 Nostr Game Engine。Primal、Coracle、noStrudel、nostr-tools、NDK 和 rust-nostr 在此期间也在发布，因此协议清理与活跃的 client 和库工作并存。

### 2026 年 4 月：NIP-34 加固、徽章和以采用为重点的资助

本期收官的 2026 年 4 月有四个合并的 NIPs PR。第一个是 4 月 1 日合并的 [PR #2276](https://github.com/nostr-protocol/nips/pull/2276)，将 [NIP-58](https://github.com/nostr-protocol/nips/blob/master/58.md) 个人资料徽章更改为 kind `10008`，并添加了 kind `30008` 徽章集，使徽章分配和徽章集合更具组合性。第二次 git-over-Nostr 可用性更改到达 4 月 10 日合并的 [PR #2312](https://github.com/nostr-protocol/nips/pull/2312)，为 [NIP-34](/zh/topics/nip-34/) 添加了 `nostr://` clone URL 语义。4 月 25 日的清理，[PR #2325](https://github.com/nostr-protocol/nips/pull/2325) 和 [PR #2326](https://github.com/nostr-protocol/nips/pull/2326)，移除了未使用和不正确的 NIP-34 语言。

相关的提交锐化了同样的表面。4 月 22 日，fiatjaf 为 NIP-51 添加了一个 Blossom 服务器列表，并调整了 NIP-29 元数据编辑以匹配 Flotilla 的 PUT 式行为。4 月 26 日，他重命名了 NIP-5A 以求清晰。2026 年 4 月专注于使已在使用的协议表面更易于实现，更难被误读。

OpenSats 于 4 月 8 日宣布了其 [第十六波 Nostr 资助](https://opensats.org/blog/sixteenth-wave-of-nostr-grants)，支持 Amethyst Desktop、Nostr Mail、Nostrord、Nurunuru（null--nostr）和 HAMSTR 续期：桌面 client、类电子邮件消息、群组 UX、日语入门和离网连接。

---

*感谢阅读 Nostr Compass #20。[通过 Nostr 私信我们](https://nostr.com)，提供提示、更正或要报道的新项目。*
