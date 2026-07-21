---
title: 'Nostr Compass #32'
date: 2026-07-22
translationOf: /en/newsletters/2026-07-22-newsletter.md
translationDate: 2026-07-22
draft: false
type: newsletters
description: "IndieSats 放弃发布者角色，转型为开放的 Nostr 音乐基础设施重新上线；Nostrord v2.3.0 在一周内五个 NIP-29 规范 PR 合并之际推出客户端侧实现；Zapstore 1.1.0 让设备密钥可移植并带来后台自动更新；收藏关注集 list kind 合并后立即重新编号；Iris 生态一周内推出 pubsub 库、浏览器 FIPS 运行时和 nostr-social-graph 2.0。"
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：**[IndieSats](#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure) 卸下密钥托管、白名单和强制收入抽成三重角色，以开放 relay、播放器和发现层的形态重新上线，艺术家从此用自己的密钥发布作品。[Nostrord v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) 在五个 [NIP-29 规范 PR 合并](#protocol-work-and-nip-updates)的同一周落地群组管理、静音列表和 onion relay。[Zapstore 1.1.0](#zapstore-110-makes-the-device-key-portable-and-adds-background-auto-updates) 引入可通过 Amber 备份的可移植加密设备密钥，以及可选开启的后台自动更新。[收藏关注集 list kind](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house) 合并后数天内又开启了重新编号的 PR。而 [Iris 生态](#the-iris-ecosystem-ships-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week) 在一周内同时推出 nostr-pubsub、fips-ts 浏览器运行时和 nostr-social-graph 2.0.0。

打标签的发布带来：[Amber v6.3.0](#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support) 将 bunker 签名审批分组处理，[Wisp v1.2.0](#wisp-v120-adds-a-multi-account-switcher-and-collapsible-reply-threads) 加入多账户切换器，[Sonar v0.1-alpha.11](#sonar-v01-alpha11-continues-the-alpha-line) 延续 alpha 线，以及新项目 [ClipRelay v0.1.2](#cliprelay-v012-new-project-syncs-clipboards-across-devices-over-nostr-relays) 通过 Nostr relay 跨设备同步剪贴板。

在未发布的一侧，[nostream](#nostream-merges-seven-prs-without-cutting-a-release) 合并了本期 Deep Dive 所讲解的访问控制栈，[Amethyst](#amethyst-lands-v1130-pre-release-qa-on-napplet-isolation-and-concord-authority) 在 81 个合并的 PR 中完成了 v1.13.0 预发布 QA。

NIPs 仓库本周合并了五个 PR，包括 [NIP-29 集群](#protocol-work-and-nip-updates)和 [kind:10011 收藏关注集](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house)，并就 [NIP-47 精简](#protocol-work-and-nip-updates)和[可信 relay 断言](#protocol-work-and-nip-updates)开启讨论。本期 Deep Dive 讲解 [NIP-42 与 NIP-43，这一对 relay 访问控制规范](#nip-deep-dive-nip-42-and-nip-43)。

---

## 头条报道

### IndieSats 放弃发布者角色，转型为开放的 Nostr 音乐基础设施重新上线

[IndieSats](https://zapstore.dev) 是一个基于 Nostr 的音乐平台，直到本周一直扮演着发布者的角色：它为艺术家托管密钥、运营白名单，并强制抽取 2% 的收入分成。在 [7 月 20 日发布的转型公告](https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u)中，该项目一次性卸下了全部三重角色。重新上线的平台改为三件开放基础设施：一个开放 relay、一个播放器和一个发现层，艺术家用自己的 Nostr 身份发布音乐，而不再使用平台托管的身份。收入分成变为可选开启，不再强制；平台现在还会响应 [NIP-09](/zh/topics/nip-09/) kind:5 删除请求，让艺术家可以移除自己的作品。在一个总是谈论协议取代平台的领域里，这是一个平台主动将自身拆解为协议组件的真实案例。

### Nostrord v2.3.0 带来群组管理、静音列表和 onion relay

[Nostrord](https://github.com/nostrord/nostrord) 是覆盖 Android、iOS、Web 和桌面的群聊客户端，本次发布的 [v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) 在所有界面接入了群组管理操作（[PR #192](https://github.com/nostrord/nostrord/pull/192)）、需同意确认的群组邀请并带跨 relay 检测（[PR #195](https://github.com/nostrord/nostrord/pull/195)）、跨平台 [NIP-51](/zh/topics/nip-51/) 静音列表（[PR #188](https://github.com/nostrord/nostrord/pull/188)），以及 Tor .onion relay 支持。该版本恰好在底层 [NIP-29](/zh/topics/nip-29/) 规范合并五个 PR 的同一周落地，这些 PR 涵盖子群组、消息置顶、横幅和邀请码（详见本期[协议部分](#protocol-work-and-nip-updates)），因此 Nostr 群聊如今既有更深的规范，也有一个实践了其中大部分内容的客户端，这缩短了所有在 relay 群组上构建的人的反馈回路。

### Zapstore 1.1.0 让设备密钥可移植并加入后台自动更新

[Zapstore](https://github.com/zapstore/zapstore) 是一个 Nostr 原生应用商店，发布由开发者密钥签名，没有中心运营方为其背书。[1.1.0 版本](https://github.com/zapstore/zapstore/releases/tag/1.1.0)是自三月初以来本刊首次报道的版本，弥合了与传统应用商店之间最大的两个差距。第一个是更新：可选开启的后台自动更新现在会在 Wi-Fi 下下载并静默或分阶段安装，应用无需手动进商店即可保持最新。第二个是身份连续性：设备密钥变为可移植、加密，并可通过 [Amber](https://github.com/greenart7c3/Amber) 经由 [NIP-55](/zh/topics/nip-55/)（Android 签名器接口）备份，因此用户换手机后不再以一台未知设备从零开始。该版本还将应用目录迁移到 relay 上，以设备签名的 kind:10067 event 承载；在溢出菜单中加入 [NIP-56](/zh/topics/nip-56/) 可验证举报，让用户能以其他客户端可消费的方式标记有问题的应用；并在任何安装进行之前验证发布所附带的 C1 证明，收紧了开发者签名内容与设备实际运行内容之间的链接。

### 收藏关注集 list kind 合并后立即搬家

一场规范协调的故事在一周之内上演。[PR #2413](https://github.com/nostr-protocol/nips/pull/2413) 于 7 月 15 日合并，在 [NIP-51](/zh/topics/nip-51/)（列表）下为收藏关注集标准化了一个可替换的 list kind：一个专用的 kind，让客户端可以发布用户策展的关注账户集合，而不必让通用 list kind 超载。数天之内人们发现分配的 kind:10011 已在别处被占用，因此后续 [PR #2417](https://github.com/nostr-protocol/nips/pull/2417) 现已开启，将该列表重新编号为 kind:10021。目前还没有任何东西基于已合并的 kind 发布，这正是重新编号代价最低的时刻；一旦客户端开始发布 kind:10011 event，解开这个冲突的代价就会很高。构建列表消费功能的开发者在该 PR 解决之前应跟踪重新编号的 PR，而不是已合并的文本。

### Iris 生态一周内推出 pubsub 库、浏览器 FIPS 运行时和社交图谱 2.0

来自 Iris 轨道的三个发布一同落地，而且彼此咬合。[nostr-pubsub](https://github.com/mmalmi/nostr-pubsub) 是一个面向 Nostr event 的传输中立发布/订阅库；其[首批被追踪的发布 v0.1.3 至 v0.5.2](https://github.com/mmalmi/nostr-pubsub/releases) 提供了一个基于 nostr-tools SimplePool 构建的浏览器 relay 载体、在传输边界上的 event 验证（无效签名永远不会到达订阅者），以及有界的历史查询。[fips-ts](https://github.com/mmalmi/fips-ts) 将 [FIPS](/zh/topics/fips/)——此前只有 Rust 实现的 Noise-over-secp256k1 对等传输——以 TypeScript 运行时的形式带入浏览器：[0.0.24 至 0.0.30 版本](https://github.com/mmalmi/fips-ts/releases)加入了 WebRTC datachannel 载体、基于 Nostr 的对等节点发现信令、最近对等节点缓存，以及用于浏览器存储的 IndexedDB 适配器，且该运行时与参考 Rust 实现线路兼容。第三件 [nostr-social-graph v2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0) 是社交图谱库的大版本：面向 Nostr 身份图谱的签名名册操作、从规范三字段 URI 引导的设备审批流程，以及带 Rust 与 TypeScript 共享测试向量的 FIPS 传输身份侧面。将它们串联起来的是 [Iris Stack](https://stack.iris.to/)——该项目把这些库与 Blossom、Hashtree 和加密消息整合在一起的集成实验室。合在一起，一个 Web 应用现在可以通过 Nostr 发现对等节点、向它们打开加密的 FIPS 通道，并维护一份签名的社交图谱，全部使用 TypeScript。

---

## 打标签的发布

### Amber v6.3.0 将 bunker 签名审批分组并加入 Expert List 支持

[Amber](https://github.com/greenart7c3/Amber) 是一款 Android [NIP-46](/zh/topics/nip-46/) 远程签名器。[v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) 为 bunker 签名加入分组的多请求审批，让一批待处理的签名请求可以一起审阅和批准，而不再是一次弹一个提示。该版本还加入对 Expert List（kind 12022）和 Expert Pack（kind 32022）event 的支持、在屏幕上隐藏敏感内容的隐私模式，以及一项调整：在获取账户个人资料元数据之前先获取其 [NIP-65](/zh/topics/nip-65/) relay 列表，让签名流程从用户的实际 relay 集合出发。这延续了 2026-07-08 期刊报道的 v6.2.x 线。

### Nostrord v2.2.0 后续

鉴于 [v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) 已是本期新闻部分的头条，打标签发布栏只补充头条未提及的内容：v2.3.0 紧随 #31 报道过的 v2.2.0 DM 控制功能，这是该客户端连续第二周的发布。

### Wisp v1.2.0 加入多账户切换器和可折叠回复串

[Wisp](https://github.com/barrydeen/wisp) 是一款内置钱包支持的隐私导向 Nostr 客户端。[v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) 加入无需重新登录即可在个人资料之间切换的多账户切换器、面向长对话的可折叠回复串、打开前剥离笔记链接中的跟踪参数，以及钱包交易历史视图。该版本是 2026-07-08 期刊报道的 Wisp 更新的后续。

### ClipRelay v0.1.2（新项目）通过 Nostr relay 跨设备同步剪贴板

[ClipRelay](https://github.com/tajava2006/cliprelay) 是一款新推出的跨平台应用（Android、macOS、Windows、Linux），可以在你自己的设备之间同步剪贴板：在一台机器上复制，在另一台上粘贴。所有流量都以发给你自己的 [NIP-44](/zh/topics/nip-44/) 加密 event 的形式经过 Nostr relay，因此没有需要运行的服务器，也没有需要创建的账户；私钥留在应用之外。[v0.1.2](https://github.com/tajava2006/cliprelay/releases) 修复了一个隐蔽的同步故障：机器从睡眠中唤醒后继续发布，却悄无声息地停止了接收；并收紧了此前把已死订阅报告为健康的 relay 状态指示器。这是 ClipRelay 首次登上本刊。

### Sonar v0.1-alpha.11 延续 alpha 线

上周的头条 [Sonar](https://github.com/hedwig-corp/bitchat-to-sonar) 发布了 [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11)，内容包括 Rust 网格链路引擎的工作、BLE 与网格修复，以及 relay 诊断；这是 #31 报道的 alpha 线的增量后续。

### 本周的较小发布

三个较小的发布各值一行：Nostr 通话应用 [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) 将推送通知迁移到 UnifiedPush，让通话信令脱离 Google 的推送基础设施；使用 Nostr 做信令的网格 VPN [nostr-vpn v4.1.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.1) 在 Zapstore 发布了更新；此外还有两款新应用在那里首秀：StableKraft，一个 Nostr 加 Lightning 的音乐与播客聚合器；以及 Hakari，一个为体重记录应用提供的加密 Nostr 备份。

### Amethyst 围绕 napplet 隔离与 Concord 权限完成 v1.13.0 预发布 QA

[Amethyst](https://github.com/vitorpamplona/amethyst) 本周在 v1.13.0 发布前合并了 81 个 PR。[PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) 是一次预发布 QA 过检，覆盖 napplet 账户隔离、Concord 权限修复以及约 30 项其他修复，更多 v1.13.0 筹备 PR 持续落地至 07-21。这延续了 #31 对 Amethyst 洁净室 Concord 客户端实现的报道，在该工作打标签发布之前收紧其权限与隔离行为。

---

## 未发布的变更

### nostream 合并七个 PR 但并未发布版本

TypeScript relay 实现 [nostream](https://github.com/Cameri/nostream) 本周合并了七个 PR，但并未发布版本。领衔的一对是 [PR #702](https://github.com/Cameri/nostream/pull/702) 和 [PR #676](https://github.com/Cameri/nostream/pull/676)，两者合起来为 relay 运营者提供了一套可用的「认证加成员资格」访问控制栈；本期 NIP Deep Dive 正好讲解这套握手。

### FIPS v0.4.1 收紧 Iris 生态赖以构建的传输层

[jmcorgan/fips](https://github.com/jmcorgan/fips) 发布了 [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1)，这是一个维护性版本，内容包括为 antipoison 状态设上限、修复收敛与 MTU 处理，以及降低 CPU 占用。单看它本身只是管线工作，但本周它是连接组织：本期新闻部分 Iris 生态集群中的浏览器 TypeScript 运行时 [fips-ts](https://github.com/mmalmi/fips-ts) 与这个 Rust 传输层线路兼容，因此这里的修复会直接传导到浏览器运行时所互操作的对象上。

---

## 协议工作与 NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的近期变更：

**已合并：**

- **[NIP-29](/zh/topics/nip-29/)（基于 Relay 的群组）：子群组**（[PR #2319](https://github.com/nostr-protocol/nips/pull/2319)，合并于 2026-07-16）：NIP-29 定义了由 relay 托管的群组，其成员资格、角色和聊天历史以可寻址的 `kind:39000` 系列 event 形式存于单个 relay 上，管理操作由 `kind:9000` 系列管理 event 承载。该 PR 让群组可以通过在其元数据中添加指向同一 relay 上另一群组 `d` 标识符的 `parent` tag 来声明自己为子群组。子群组在其他所有方面都是普通群组：成员资格不级联（加入父群组不授予任何子群组的成员资格），管理角色不继承（每个子群组自己的 `kind:39001` 管理员列表在其自身范围内具有权威性），且每个子群组保留自己独立的 `kind:9000`/`kind:9001` 成员 event。支持该层级结构的 relay 会在其 NIP-11 relay 信息文档中以带 `"subgroups": true` 的 `nip29` 对象进行宣告，因此客户端可以在尝试创建嵌套社区之前发现该能力。

- **[NIP-29](/zh/topics/nip-29/)：消息置顶**（[PR #2379](https://github.com/nostr-protocol/nips/pull/2379)，合并于 2026-07-15；[PR #2416](https://github.com/nostr-protocol/nips/pull/2416)，合并于 2026-07-17）：群组管理员现在可以在基于 relay 的群组内置顶消息。该机制新增了一个管理 event `kind:9010` `update-pin-list`，以引用普通 event id 的 `e` tag 承载完整有序的置顶列表；以及一个新的可选群组级 event `kind:39005`「群组置顶 event」，由 relay 重新生成以镜像最新被接受的置顶列表。由于每个 `kind:9010` 替换整个列表而非切换单个条目，置顶、取消置顶、重排和清空置顶都通过提交一个新列表来表达。后续 PR #2416 扩展了格式，使置顶列表也接受 `a` tag，让管理员可以在普通聊天消息之外置顶可寻址 event（长文、维基页面和其他参数化可替换内容）。relay 可以限制置顶数量，合并后的规范文本建议按 tag 出现的顺序展示置顶。

- **[NIP-29](/zh/topics/nip-29/)：banner tag 与邀请码后缀**（[PR #2383](https://github.com/nostr-protocol/nips/pull/2383)，合并于 2026-07-16；[PR #2380](https://github.com/nostr-protocol/nips/pull/2380)，合并于 2026-07-16）：两项面向展示与引导的群组元数据补充。PR #2383 在 `kind:39000` 群组元数据 event 中加入可选的 `banner` tag，与现有的 `name`、`picture` 和 `about` 字段并列，让客户端可以为群组页面渲染头图。PR #2380 为群组分享链接定义了邀请码后缀：邀请码可以作为 `naddr1...?invite=<code>` 附加到群组的 `naddr` 标识符上。由于 bech32 字符集不包含 `?`，后缀之前的部分本身仍是合法的 naddr，因此不理解该扩展的客户端仍可解析群组。理解该扩展的客户端会在 `kind:9021` 加入请求上预填 `code` tag，它与现有的 `kind:9009` `create-invite` 管理 event 配合，简化封闭群组的准入。

- **[NIP-51](/zh/topics/nip-51/)（列表）：收藏关注集，kind:10011**（[PR #2413](https://github.com/nostr-protocol/nips/pull/2413)，合并于 2026-07-15）：NIP-51 定义了标准 list kind，分为可替换的 `kind:10000` 系列列表（每个用户一份）和可寻址的 `kind:30000` 系列集合（每个用户多份，以 `d` tag 为键）。该 PR 新增 `kind:10011`「收藏关注集」，一个标准可替换列表，其 `a` tag 指向 `kind:30000` 关注集。它与 `kind:10012`（relay 信息流，承载引用 `kind:30002` relay 集合的 `a` tag）互为镜像：新 kind 让用户可以收藏具名关注集——比如自己或他人发布的策展 pubkey 合集——并让客户端将其呈现出来以供一键关注或切换信息流。请注意该 kind 编号已存在争议：见下方的开放重编号 PR。

- **[NIP-46](/zh/topics/nip-46/)（Nostr Connect）：静默超时指引**（[PR #2375](https://github.com/nostr-protocol/nips/pull/2375)，合并于 2026-07-15）：NIP-46 是远程签名协议，客户端通过 relay 向签名器（bunker）发送加密的 JSON-RPC 风格请求并等待加密响应。合并的变更是一句线路行为规定：以未知或不支持的方法发起的请求必须（MUST）以错误回复。此前，收到未实现方法的签名器可以永远不响应，让客户端一直挂起直到自身超时触发，且无法区分「不支持的方法」与「签名器离线」。强制的错误回复让客户端可以快速失败并向用户展示有意义的信息，而不是无限空转。

**开放的 PR 与讨论：**

- **kind:10011 重编号为 kind:10021**（[PR #2417](https://github.com/nostr-protocol/nips/pull/2417)）：将刚合并的收藏关注集列表从 `kind:10011` 移至 `kind:10021`，因为 `10011` 已在别处被占用。重编号 PR 在原合并后数天内即开启，因此实现收藏关注集的客户端应跟踪该 PR 并以最终编号为目标，而非 `10011`。

- **[NIP-47](/zh/topics/nip-47/)（Nostr Wallet Connect）：核心精简**（[PR #2419](https://github.com/nostr-protocol/nips/pull/2419)）：提议将 NIP-47——让应用通过 Nostr 向远程钱包请求 Lightning 付款的钱包连接协议——收窄为更小的核心规范。可选和更专门的功能将从 `47.md` 移出，进入专门的扩展仓库 [nostr-wallet-connect/nwc](https://github.com/nostr-wallet-connect/nwc)，扩展规范可以在那里独立于核心演进。声明的目标是保持核心小巧、稳定、易于实现，延续此前 NWC 会议商定的方向：将最小钱包连接层与更丰富的可选行为分离。鉴于 NIP-47 在钱包和应用中的广泛部署，任何讲 NWC 的参与者都应跟踪这场重构讨论。

- **可信 Relay 断言（草案，尚未分配编号）**（[PR #2418](https://github.com/nostr-protocol/nips/pull/2418)）：提议为发布关于 Nostr relay 的信任评估建立标准，定位为与 [NIP-11](/zh/topics/nip-11/)（relay 自述其声明）和 [NIP-66](/zh/topics/nip-66/)（监视器实测结果）并列的「我们得出结论」层。断言提供者将从观测指标、运营者声誉和用户报告中计算信任评分；客户端在选择连接哪些 relay 时查询这些断言。草案引入 `kind:30385`（可寻址的可信 Relay 断言，承载评分、可靠性、质量、可达性、运营者、政策和司法辖区 tag）、`kind:10385`（可替换的可信提供者列表，即用户选择的断言提供者），并复用 [NIP-32](/zh/topics/nip-32/) 标签用于 relay 与运营者报告。目前尚未分配 NIP 编号；这是一个早期草案。

- **过滤器的 AND 运算符（「NIP-91」，提议中，编号尚未进入仓库）**（[PR #2252](https://github.com/nostr-protocol/nips/pull/2252)）：在 NIP-01 下，tag 过滤器仅支持 OR：过滤器 `"#t": ["meme", "cat"]` 匹配带任一 tag 的 event。该提案为可索引 tag 增加 `&` 修饰符，使 `"&t": ["meme", "cat"]` 只返回同时带有两个 tag 的 event，让 relay 在服务端做交集，而不是让客户端过度抓取后本地过滤。规则规定 AND 优先于 OR，支持该扩展的 relay 应将 AND 中用到的 tag 值在 OR 中忽略，且客户端必须（MUST）同时包含标准的 `#` OR tag 以兼容不支持该扩展的 relay（这些 relay 返回更宽泛的 OR 结果，由客户端在本地求交集）。该 PR 是一个更早提案的重新开启，并列出了相关 relay 实现，包括 nostr-rs-relay 的 docker 镜像、netstr 和一个 Snort worker relay。NIP-91 编号只出现在 PR 分支中；尚未进入仓库 README 的 NIP 索引，因此请将该编号视为临时编号。

- **Nostr Web 小程序（「NIP-5D」，提议中，编号尚未进入仓库）**（[PR #2303](https://github.com/nostr-protocol/nips/pull/2303)）：为运行在 iframe 或 webview 中的沙盒化 Web 应用（「napplet」）定义了一套 `postMessage` 协议，用于与宿主应用（「shell」）通信。该规范刻意保持为薄核心：它规定消息信封、沙盒规则（napplet 的 iframe 必须（MUST）使用不带 `allow-same-origin` 的 `sandbox="allow-scripts"`，且 shell 不得（MUST NOT）在 iframe 内暴露 `window.nostr` NIP-07）、通过不可伪造的 `MessageEvent.source` window 引用（而非 `event.origin`）进行发送者识别，以及基于清单的能力协商。签名、relay 访问、存储和 napplet 间通信的实际协议消息被委托给 NAP（Nostr Applet Protocol）扩展规范，每个扩展拥有一个能力域，签名与加密始终由 shell 中介，密钥永远不会进入沙盒。该提案依赖 NIP-5A napplet 清单规范，且在本周恰逢其时：Amethyst 的 v1.13.0 预发布工作包含 napplet 账户隔离，客户端侧的 napplet 托管正是一个活跃的实现领域。与上文的「NIP-91」一样，5D 编号是临时的。

---

## NIP Deep Dive：NIP-42 与 NIP-43

运营一个不对所有人开放的 relay，过去意味着一切都得自己发明。付费或仅限邀请的 relay 运营者必须在带外维护一份白名单——通常是一个通过 DM 收集的 pubkey 文本文件——既没有标准方式告诉已连接的客户端「证明你是谁」，也没有标准方式让用户请求准入或知道自己是否是成员。每个想要门控读取或门控写入的 relay 都构建自己的私有机制，客户端无法与其中任何一个互操作。[NIP-42](/zh/topics/nip-42/) 将这个问题中的身份证明一半标准化，[NIP-43](/zh/topics/nip-43/) 则将成员资格一半标准化。本周，TypeScript relay nostream 端到端合并了这一对：[PR #702](https://github.com/Cameri/nostream/pull/702) 将加密 kind 的读取限制为经过认证的接收者，[PR #676](https://github.com/Cameri/nostream/pull/676) 加入加入与退出请求的 event 策略，两者均于 7 月 20 日合并。

### NIP-42：客户端向 relay 的认证

[NIP-42](/zh/topics/nip-42/) 回答一个问题：这条连接上是谁？想要门控读取或写入的 relay 会发送一条携带挑战字符串的 `AUTH` 消息——在连接建立时，或在某个请求需要认证时按需发送。客户端以自己的 `AUTH` 消息回复，其中包含一个签名的临时 event，kind 22242，relay 则以 `OK` 消息作答，就如同这个认证 event 是一次普通写入。认证后的会话在连接存续期间保持有效，且客户端可以在一条连接上通过一系列 `AUTH` 消息认证多个 pubkey，relay 将每一个都视为已认证。

签名的认证 event 如下所示：

```json
{
  "id": "4ef6f2c0b1a84c9a3d0f9c58e2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0",
  "pubkey": "c308e1f882c1f1dff2a43d4294239ddeec04e575f2d1aad1fa21ea7684e61fb5",
  "created_at": 1753195800,
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com/"],
    ["challenge", "challengestringhere"]
  ],
  "content": "",
  "sig": "8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1"
}
```

`pubkey` 是被证明的身份，因为 relay 会根据它验证 event `id` 上的 `sig`。`kind` 22242 位于临时范围：该 event 是连接级凭据，relay 绝不能存储它或将其广播给其他客户端。`relay` tag 将签名绑定到一个 relay URL，使被截获的认证 event 无法对另一个 relay 重放；`challenge` tag 将其绑定到 relay 在这条连接上签发的特定挑战字符串，阻止被截获的认证在之后的连接上重放。`created_at` 必须接近当前时间，大致在十分钟窗口之内，因此陈旧的认证 event 会自行过期。`content` 字段为空；没有任何内容被发布。

规范还定义了两个让门控对客户端可见的机器可读前缀。因客户端尚未认证而拒绝订阅的 relay 以 `auth-required:` 开头的 `CLOSED` 消息作答，被拒绝的写入则得到带相同前缀的 `OK`。已认证但仍无权限执行该操作的客户端得到的则是 `restricted:`。这一区分正是 [nostream 的 PR #702](https://github.com/Cameri/nostream/pull/702) 所构建的基础：加密 kind 的读取现在可以以 `auth-required:` 关闭，直到发起请求的 pubkey 证明自己是接收者。

### NIP-43：Relay 访问元数据与请求

[NIP-43](/zh/topics/nip-43/) 回答后续问题：既然 relay 知道你是谁了，你被允许做什么？NIP-42 是在一条活跃连接上的握手，NIP-43 则是一组描述成员资格状态并让用户请求变更它的已发布 event。在 relay 一侧，由 relay 的 [NIP-11](/zh/topics/nip-11/) `self` 字段中的 pubkey 签名的 kind 13534 event，为每个 pubkey 列出一个 `member` tag，并可选地带有指向以 kind 33534 发布的角色定义的角色参数。Kind 8000 宣告一名成员被加入，kind 8001 宣告一次移除，两者都由同一把 relay 密钥签名，并以 `p` tag 标明受影响的成员。在用户一侧，kind 28934 是携带 `claim` tag 中邀请码的加入请求，kind 28935 是用户请求 claim 时 relay 即时生成的临时邀请码 event，kind 28936 是退出请求。

一个加入请求如下所示：

```json
{
  "id": "9f0e1d2c3b4a59687a6b5c4d3e2f1098a7b6c5d4e3f2019a8b7c6d5e4f3021a9b8",
  "pubkey": "ee1d336e13779e4d4c527b988429d96de16088f958cbf6c074676ac9cfd9c958",
  "created_at": 1753195900,
  "kind": 28934,
  "tags": [
    ["-"],
    ["claim", "invite-code-from-operator"]
  ],
  "content": "",
  "sig": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
}
```

`pubkey` 是请求准入的用户，kind 28934 将该 event 标记为加入请求。`-` tag 是 [NIP-70](/zh/topics/nip-70/) 受保护 event 标记，告诉 relay 不要从作者之外的任何人处接受该 event。`claim` tag 承载用户在带外获得的邀请码，`created_at` 必须是现在（前后几分钟之内），因此旧请求无法被重放。relay 以 `OK` 消息回应 claim，对过期或无效邀请码等失败情况复用 NIP-42 的 `restricted:` 前缀，随后应更新其 kind 13534 列表，并可发布 kind 8000 的加入成员 event。成员资格被刻意设计为不从单个 event 推导：规范称 relay 签名的列表不应被视为详尽或权威，客户端在判断某人当前是否是成员时应同时参考 relay 的 kind 13534 和成员自己的 event。客户端只能向在其 NIP-11 文档的 `supported_nips` 部分宣告支持该 NIP 的 relay 发送加入、邀请或退出请求，而 [nostream 的 PR #676](https://github.com/Cameri/nostream/pull/676) 正是将这些请求 kind 转化为实际成员资格变更的 relay 侧机制。

### 历史

NIP-42 是两者中年长得多的一位。它于 2023 年 1 月 2 日通过 [commit c80be21c](https://github.com/nostr-protocol/nips/commit/c80be21c) 进入 NIPs 仓库，在该提交中 fiatjaf 大幅简化了 semisol 起草的早期 relay 认证 NIP，将一套更复杂的挑战方案折叠为规范沿用至今的单个签名临时 event。NIP-43 到来得晚得多：2025 年 10 月 30 日，hodlbod 的 [PR #1079](https://github.com/nostr-protocol/nips/pull/1079) 合并，加入了直接构建在 NIP-42 `restricted:` 前缀之上的 relay 访问元数据与请求。这两年半的间隔反映了在成员资格层获得标准之前，生态在临时白名单上运营付费与私有 relay 的时间有多长。

### 实现情况

在 relay 一侧，[nostream](https://github.com/Cameri/nostream) 在本周的合并之后同时搭载了两半。[strfry](https://github.com/hoytech/strfry) 实现了 NIP-42，在其摄取器中验证 kind 22242 认证 event，并从其配置中签发挑战。[nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) 在其连接层处理 AUTH 握手，测试覆盖挑战与时间戳窗口。Go relay 框架 [khatru](https://github.com/fiatjaf/khatru) 按连接跟踪已认证的 pubkey，使策略可以据此门控读取与写入。在客户端一侧，[Amethyst](https://github.com/vitorpamplona/amethyst) 对 relay 挑战签出 kind 22242 响应，包括为其 Concord 加密社区提供按流的认证。这两个 NIP 沿一条清晰的分界线划分访问控制：NIP-42 是身份证明，作用域为一条连接、一个挑战和几分钟的有效期，它对策略只字不提；NIP-43 是策略，以普通 relay event 的形式表达：谁是成员、谁被加入或移除，以及用户如何请求这些变迁。实现者应当留意的空白是：除了 NIP-43 的可选角色元数据之外，目前尚无任何标准规定更细粒度的权限，因此任何做超出「成员/非成员」二元划分的 relay 都在自行设计那一层。

---

本期就到这里。在构建什么或有消息要分享？通过 NIP-17 DM 联系我们，或在 Nostr 上找到我们。
