---
title: 'Nostr Compass #23'
date: 2026-05-21
publishDate: 2026-05-21
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-21-newsletter.md
translationDate: 2026-07-01
---

Primal 3.5 发布了重建的 Android 外壳，Amethyst 添加了链上 Bitcoin zaps，White Noise 获得了 markdown 渲染和深度链接，Keycast 通过了安全审计，AgentNoise 让你可以通过 Marmot 加密聊天控制本地 AI 编码 agent。Hostr 在 Nostr 上推出了 P2P 租赁住宿平台，包含四个涵盖房源、预订和基于 EVM 的托管的 NIP 草案。Angor 将加密消息从 NIP-04 迁移到 NIP-44，Dart NDK 添加了 NIP-77 和 Web signer，Alby js-sdk v8 发布了原生 NWC 多 relay 重连，KeyChat 修补了 Signal 一次性 prekey 删除中的前向保密缺口。在协议方面，Mostro 的反滥用保证金达到第二阶段，Wisp 发布了私密回复和 gift-wrapped 反应，Namecoin NIP-05 实现浪潮在一周内影响了六个 client。

## 头条报道

### Primal 3.5 for Android

Primal 是一个由自有缓存 relay 基础设施支持的社交 client，本周发布了 [3.5.9](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.9)，带来重建的应用外壳。重新设计用更新的布局和新的 Explore 屏幕取代了之前的导航结构，让主要的发现界面拥有自己专用的主页。该版本为链接预览添加了音频播放，因此嵌入笔记中的音频文件可以内联播放而无需离开信息流。NIP-05 验证徽章现在内联显示在个人资料上，一眼即可看到身份确认。通知过滤经过彻底改进，让用户可以缩小哪些事件类型到达他们的通知列表。编辑器获得了更好的事件链接处理，底层的数据库层收到了稳定性修复。

### White Noise：markdown、深度链接和音频元数据

White Noise 是构建在 Nostr 和 MLS（[RFC 9420](https://www.rfc-editor.org/rfc/rfc9420)）之上的 Marmot 加密群组消息应用，在前端和后端仓库度过了迄今最繁忙的一周之一。

在前端，[PR #665](https://github.com/marmot-protocol/whitenoise/pull/665) 为聊天消息添加了完整的 markdown 渲染，因此粗体、斜体、代码块和链接现在在消息视图中原生渲染。[PR #675](https://github.com/marmot-protocol/whitenoise/pull/675) 启用了此前对非最后一个管理员被阻止的离开群组流程，[PR #661](https://github.com/marmot-protocol/whitenoise/pull/661) 为 `whitenoise://` 和 `whitenoise-staging://` URI 添加了涵盖用户、聊天和设置的原生深度链接支持，无需任何 HTTP 重定向基础设施。

在后端 whitenoise-rs 中，[PR #835](https://github.com/marmot-protocol/whitenoise-rs/pull/835) 通过为 kind:30443 发布重用 `d_tag` 插槽使 key package 轮换正常工作，启用 NIP-33 可替换事件语义，因此连续的 key package 轮换在 relay 上替换先前的事件，只保留当前的 key package。[PR #833](https://github.com/marmot-protocol/whitenoise-rs/pull/833) 使用可选的 `duration_ms` 和 `waveform` 字段扩展 `FileMetadata` 以支持音频附件，与 MDK 的 [PR #300](https://github.com/marmot-protocol/mdk/pull/300) 协调，后者为 MIP-04 媒体标签添加了相同的字段。新的 `whitenoise-markdown` crate（[PR #836](https://github.com/marmot-protocol/whitenoise-rs/pull/836)）用专用的 markdown 渲染库取代了之前的 nostr-sdk token 解析器。

Marmot 协议规范本身在 [PR #68](https://github.com/marmot-protocol/marmot/pull/68) 中收到了一个安全修复，它通过为 MIP-01 中的图像密钥派生明确指定 HKDF-SHA256 来关闭一个安全问题，消除了可能导致实现分歧的歧义。在 MDK 中，[PR #307](https://github.com/marmot-protocol/mdk/pull/307) 清理 welcome 失败原因并限制存储长度，关闭了一个单独的安全发现。

### Amethyst v1.10.0：链上 Bitcoin Zaps

Amethyst 本周发布了四个版本，以 [v1.10.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.10.0) 为头条。该版本添加了对 NIP-BC 链上 Bitcoin zaps 的支持，让用户可以发送、接收和显示通过 Bitcoin 交易直接在链上结算的 zaps。系列中较早的版本修复了 Blossom blob 检测以拒绝不兼容的文件名（[v1.09.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.09.2)），修补了桌面构建的 ProGuard 规则，并合并了 pull request [#2977](https://github.com/vitorpamplona/amethyst/pull/2977) 以在展开的反应画廊中将链上 Bitcoin 打赏者显示为专用的 ₿ 行。带分页的进行中链上交易历史屏幕落地于 [PR #2974](https://github.com/vitorpamplona/amethyst/pull/2974)。

### AgentNoise：通过 White Noise 控制编码 agent

由 nvk 开发的 [AgentNoise](https://github.com/nvk/agentnoise) 是一个 Rust 原生桌面助手，让你可以使用运行 White Noise 的手机作为本地 Codex 和 Claude 编码 agent 会话的控制界面。该工具监听一个或多个 White Noise 聊天，通过首次配对 PIN 流程验证发送者，并通过配置的启动器启动本地编码 agent。从手机发送 `/claude <prompt>` 会打开一个以机器主机名和简短 prompt 摘要命名的新 White Noise 工作会话，然后将进度更新和最终输出流回到该聊天。它有意采用 Rust 优先，并将 Node 排除在可信桥接路径之外。该项目本周达到 [v0.1.24](https://github.com/nvk/agentnoise/releases/tag/v0.1.24)，添加了更短的手机可读回复、按短唯一前缀的作业引用，以及可选加入的本地会话观察者。AgentNoise 将 `marmot-protocol/whitenoise-rs` 的 `wn` 和 `wnd` CLI 作为子进程驱动，因此它与 White Noise client 本身共享其 Nostr 传输。

### Keycast 安全审计完成

[Keycast](https://github.com/marmot-protocol/keycast) 是面向团队的 NIP-46 远程签名服务器，将 Nostr 私钥加密存储在 SQLite 中，于 2026 年 5 月完成了一次安全审计。加固工作解决了 auth、权限、数据完整性和依赖问题，结果记录在 [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) 中。变更包括：NIP-98 HTTP auth 现在要求恰好一个 `u` 标签和一个 `method` 标签、拒绝过期时间戳并验证 `payload` 哈希；`ALLOWED_PUBKEYS` 白名单被精确解析并在服务器端强制执行；空策略现在默认拒绝签名/加密/解密请求；SQLite 连接启用了外键强制；诸如 `/teams/:id` 之类的嵌套应用路由在服务器端受到保护。SQL 迁移在启动时规范化旧的 allowed-kinds 权限 JSON。该项目仍处于早期阶段，审计记录了在信任其真实团队密钥之前的剩余项目。

### Scramble：桌面和 Android 的 Marmot client

[Scramble](https://github.com/DavidGershony/Scramble)（前称 OpenChat）是一个 [Marmot 协议](/zh/topics/marmot/) 的 .NET/Avalonia 桌面和 Android client，实现了 MIPs 00-04：KeyPackage 发布（kind:30443）、带有 NostrGroupData MLS 扩展的群组元数据、NIP-59 gift-wrapped welcome 事件（kind:444）、ChaCha20-Poly1305 加密消息（kind:445），以及 Blossom 加密媒体附件。它与 White Noise 及任何其他 Marmot 兼容的 client 完全互操作。

该项目本周发布了 13 个版本，主要功能是多设备支持。每个设备生成一个唯一的 KeyPackage 插槽（kind:30443 上的 `d` 标签）。启动时，Scramble 从 relay 获取用户自己的 KeyPackages，检测对等设备插槽 ID，并使用暂存 commit 流程自动将它们添加到现有的 MLS 群组。自动添加仅限于当前用户是管理员的群组；非管理员群组会被跳过，并给出询问群组管理员的指引。前向保密披露横幅告知新链接的设备旧消息不可用。插槽 ID 协调过程（`TryReconcileSlotId`）通过将 relay KeyPackage 字节与本地密钥材料匹配来采用正确的 `d` 标签，处理从多设备版本之前迁移的设备。Amber 和 NIP-46 用户的外部 signer 重连也得到了修复：阻止 `ExternalSignerService` 内置自动重连的 `IsConnected` 守卫已在 `NostrService` 中的所有九个调用点被移除。

### Hostr：Nostr 上的 P2P 租赁住宿

[Hostr](https://hostr.network)（[源代码](https://github.com/sudonym-btc/hostr)）是一个完全构建在 Nostr 上的点对点租赁住宿平台。它涵盖了完整的 Airbnb 式流程（搜索和列出物业、协商预订以及结算支付），使用该项目与应用并行开发的四个 NIP 草案。

住宿 NIP 使用住宿特定的标签扩展 [NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md) 分类列表（kind:30402 有效，kind:30403 草稿），涵盖类型（`room`、`house`、`apartment`、`villa`、`hotel`、`hostel`、`resort`）、入住/退房时间、最少停留时间，以及用于按可配置精度进行基于位置的搜索的 H3 地理空间单元索引。预订 NIP 定义了完整的协商和生命周期协议：kind:32122 可替换预订事件携带一个 `d` 交易 ID、一个列表锚 `a` 标签，以及带有角色（`buyer`、`seller`、`escrow`）的参与者 `p` 标签；kind:1327 结构化消息 rumors 通过 NIP-59 gift wraps 提供私密的协商阶段反报价，因此协商停留在公共 relay 之外；kind:1326 仅追加的转换事件在预订提交后创建公共审计跟踪。买家隐私通过每次交易的临时 Nostr 密钥保留，这些密钥通过加密的 `participant_proof` 标签绑定到买家的真实身份。托管 NIP 定义了 kind:30303 托管服务广告和 kind:17388 用户信任声明；参考实现使用 Rootstock 上的 EVM 智能合约，`contractBytecodeHash` 允许 client 验证部署的合约与已知的经审计实现匹配。市场列表 NIP 定义了所有 NIP-99 市场配置文件共享的通用标签，包括 `instantBook`、`negotiable`、`quantity`、`securityDeposit`、`cancellationPolicy` 和 `maxDisputePeriod`。本周该项目准备了其应用商店提交，并合并了面向 agent 自动化的 MCP client 身份支持。

本周 Shakespeare MiniApps 平台上出现了两个新条目：[InkPress](https://inkpress.shakespeare.wtf) 是一个 AI 杂志生成器，以 Nostr 事件形式发布结构化杂志式内容；[PressStr](https://pressstr.shakespeare.wtf) 是 Soapbox 栈的写作和发布平台。

## 本周发布

### ngit v2.4.4

**ngit** 发布了 [v2.4.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.4)，添加了 `ngit sync --trust-server`（`-t`）用于 git server 领先于 Nostr 状态的情况。检测到这种情况时，sync 会报告受影响的 refs，并要求使用该标志来签名并发布一个更新的状态事件；一个 `nostr.trust-server-domains` git 配置设置提供了一个分号分隔的允许列表，用于应自动被信任而不需要该标志的服务器。

### Amber v6.1.0-pre3 添加 PSBT 签名

**Amber** 发布了 [v6.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre3)，改进了新应用连接的布局、崩溃修复，以及权限屏幕上的全选/取消全选选项。[PR #438](https://github.com/greenart7c3/Amber/pull/438) 通过基于 Intent 和 NIP-46 relay 两个路径添加了 PSBT 签名支持，允许 Amber 签名部分签名的 Bitcoin 交易，而不向请求应用暴露 nsec。

### Wisp v1.1.0 发布私密回复并放弃 Amber 支持

**Wisp** 发布了 [v1.1.0](https://github.com/barrydeen/wisp/releases/tag/v1.1.0)，通过 NIP-17 gift wrap（[PR #540](https://github.com/barrydeen/wisp/pull/540)）实现私密回复、私密回复上的 gift-wrapped 反应和 DIP-03 zaps（[PR #543](https://github.com/barrydeen/wisp/pull/543)）、笔记的自动翻译（[PR #523](https://github.com/barrydeen/wisp/pull/523)），以及 zap 对话框上的收银机风格法币输入。[PR #541](https://github.com/barrydeen/wisp/pull/541) 将私密 zaps 从自制的 DM-relay 明文方案迁移到 DIP-03，具有正确的 DM-relay 路由。同一发布周期移除了 NIP-55 远程 signer 支持（[PR #531](https://github.com/barrydeen/wisp/pull/531)），放弃了 Amber 和其他外部 signer 集成，并移除了捆绑的本地 relay（[PR #533](https://github.com/barrydeen/wisp/pull/533)）。Wisp 是一个 Android 上的 Nostr 社交 client。

### Calendar by Formstr v1.5.4 修复了对新参与者的 gift wrap

**Calendar by Formstr** 发布了 [v1.5.4](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.4)（v1.5.2 → v1.5.4 序列中的最新版本）。[PR #160](https://github.com/formstr-hq/nostr-calendar/pull/160) 修复了一个 bug，即编辑带有新参与者的私密日历事件时，发布的更新事件在 `p` 标签中包含新的 pubkeys，但从未创建或向这些参与者交付 gift wrap 邀请，破坏了最后一刻添加的邀请流程。[PR #156](https://github.com/formstr-hq/nostr-calendar/pull/156) 在私密事件解密周围添加了错误处理，因此 client 不再对无法解密的事件抛出异常，[PR #138](https://github.com/formstr-hq/nostr-calendar/pull/138) 更正了跨时区漂移的重复事件时间。

### Applesauce v6.1.0 添加 NIP-34 git casts 和 NIP-51 查找 relay

**Applesauce** 在其包中发布了 [v6.1.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.1.0)，具有重要的 NIP-34（git-over-Nostr）支持：applesauce-common 添加了新的 `GitRepository`、`GitGraspList` 和 `FavoriteGitRepos` casts 以及匹配的工厂，并公开了 `User.favoriteGitRepos$`、`User.gitAuthors$` 和 `User.graspServers$` 响应式属性，因此应用可以直接从同一个 User 对象列出用户关注的 git repo、repo 维护者和配置的 GRASP 服务器。同一版本添加了对 NIP-51 kind 10086 查找 relay 列表的支持，这是 relay 列表家族的最近新增，用于发现在哪里查找特定数据。applesauce-core 在 `EventCast` 上获得了 `replaceableAddress` 用于 NIP-01 可替换地址查找，加上 `pointer`、`kind` 和一个 `getReplaceableAddressForEvent` 辅助函数，并在基础 `User` cast 上添加了 `timeline$()` 方法。[PR #73](https://github.com/hzrd149/applesauce/pull/73) 修复了 pool 手动方法静默丢弃离线 relay 的问题。

### Sprout v0.0.16 发布 Sprig 二进制文件和 huddle 协议 v2

Block 的 **Sprout** 是一个自托管的基于 Nostr relay 的团队工作区，人类和 AI agent 共享相同的房间和事件日志，本周发布了桌面应用的 [v0.0.16](https://github.com/block/sprout/releases/tag/v0.0.16)，同时发布了新的 Sprig 一体化二进制文件的滚动构建（[PR #605](https://github.com/block/sprout/pull/605)），它将 ACP 测试工具、agent 和开发者 MCP 捆绑到一个 busybox 风格的二进制文件中以便于部署。[PR #611](https://github.com/block/sprout/pull/611) 中添加的 `--no-memory` 标志让运营者可以为 ACP 测试工具禁用 NIP-AE 核心内存注入。在实时方面，[PR #609](https://github.com/block/sprout/pull/609) 将 huddle 语音协议扩展到支持最多 10 个同时对等方的 v2 帧头。

### Nostrord v1.0.3 添加 OS 钥匙串和多账户

**Nostrord** 发布了 [v1.0.3](https://github.com/nostrord/nostrord/releases/tag/v1.0.3)，通过 OS 钥匙串和 passphrase 备选加固了本地密钥存储、多账户支持，以及在 Android 上可点击打开 signer 应用的 bunker QR code。

### Angor 迁移到 NIP-44 并发布安全加固

构建在 Nostr 和 Taproot 之上的 Bitcoin 众筹应用 **Angor** 本周发布了三个不稳定版本（[v0.2.24](https://github.com/block-core/angor/releases/tag/v0.2.24)、[v0.2.25](https://github.com/block-core/angor/releases/tag/v0.2.25) 和 [v0.2.26](https://github.com/block-core/angor/releases/tag/v0.2.26)），带来了一组安全加固和 Nostr 集成变更。[PR #860](https://github.com/block-core/angor/pull/860) 将 Nostr 加密消息从 NIP-04 迁移到 NIP-44，用 ChaCha20-Poly1305 加密替换了已弃用的基于 XOR 的方案。[PR #861](https://github.com/block-core/angor/pull/861) 允许在没有选择钱包的情况下通过使用临时 Nostr auth 密钥进行 Blossom 媒体上传，为尚未连接钱包的用户解除上传阻塞。安全系列解决了几个加固类别：[PR #854](https://github.com/block-core/angor/pull/854) 为 AngorKey 添加了类型安全性和助记词内存保护，[PR #856](https://github.com/block-core/angor/pull/856) 为时间锁、费率、粉尘阈值和惩罚规则强制协议级验证，[PR #851](https://github.com/block-core/angor/pull/851) 在八个中低严重性类别中应用了非破坏性加固。[PR #859](https://github.com/block-core/angor/pull/859) 通过启用 AOT 编译并移除运行时代码生成修复了 GrapheneOS 兼容性，[PR #855](https://github.com/block-core/angor/pull/855) 通过在 OS 终止进程之前持久化钱包状态防止 Android 滑动强杀时的钱包丢失。

### Alby js-sdk v8.0 发布 NWC 多 relay 重连

**Alby js-sdk** 发布了 v8.0 系列（[v8.0.1](https://github.com/getAlby/js-sdk/releases/tag/v8.0.1) 到 [v8.0.3](https://github.com/getAlby/js-sdk/releases/tag/v8.0.3)），带有 NWC 多 relay 订阅支持。[PR #516](https://github.com/getAlby/js-sdk/pull/516) 更新了 nostr-tools 依赖，并启用了跨多个 relay 的原生自动重连，用 relay 原生的重连逻辑取代了之前的轮询方法。[PR #542](https://github.com/getAlby/js-sdk/pull/542) 用一个可注入的 logger 接口替换了所有 `console.debug` 调用，因此应用开发者可以将 SDK 诊断路由到他们自己的日志基础设施。该版本移除了 WebSocket polyfill，服务器端使用者需要 Node.js 22 或更高版本。v8.0.2 添加了对破坏某些打包器的 utils crypto 导入 bug 的修复。

### KeyChat v1.41.1 修复前向保密

**KeyChat** 是一个将 Signal 协议与 Nostr relay 传输相结合的消息应用，发布了 [v1.41.1+6513](https://github.com/keychat-io/keychat-app/releases/tag/v1.41.1+6513)。头条修复通过在成功解密后立即删除 Signal 一次性 prekeys 来强制前向保密，关闭了一个缺口：如果设备后来被入侵，保留的 prekey 可能被用来解密过去的消息。该版本还为仅由单个链接组成的消息添加了 URL 预览，将媒体自动下载集中到一个新的 `FileDownloadManager` 下，具有 20 MB 的自动阈值，并重构了 NIP-11 relay 信息获取，以在冷启动时强制刷新，因此付费 relay 费用配置总是正确加载。

## 开发中

**Citrine** 合并了 [PR #151](https://github.com/greenart7c3/Citrine/pull/151)，实现 NIP-70 强制执行：如规范要求，Android relay 现在阻止嵌入受保护事件内容的转发。[PR #149](https://github.com/greenart7c3/Citrine/pull/149) 从 relay 设置屏幕添加多个连接地址（localhost、本地 Wi-Fi 和 Tor）的显示和复制操作。[PR #141](https://github.com/greenart7c3/Citrine/pull/141) 通过与 Amber 的外部 signer 集成添加 NIP-42 AUTH 挑战处理。

**Mostro** 达到其反滥用保证金推出的第 2 阶段。[PR #737](https://github.com/MostroP2P/mostro/pull/737) 落地了求解器指导的争议削减逻辑：管理员处理程序现在使用来自 mostro-core 的 `BondResolution` 负载，允许管理员在解决争议时削减任一方的保证金。在 [PR #736](https://github.com/MostroP2P/mostro/pull/736) 中合并的第 1.5 阶段引入了一个专用的 `PayBondInvoice` 操作和 `WaitingTakerBond` 状态，将 taker 的反滥用保证金支付与买方的交易支付分开。移动 client 在 [PR #592](https://github.com/MostroP2P/mobile/pull/592) 中添加了完整的第 1.5 阶段 UX。Mostro 是一个建立在 Nostr 上的点对点 Bitcoin 交换协议。

**Damus** 合并了 [PR #3773](https://github.com/damus-io/damus/pull/3773) 恢复 relay 信号指示器，[PR #3775](https://github.com/damus-io/damus/pull/3775) 修复了在初始连接失败后拒绝重新连接的 relay。

**rust-nostr** 合并了 [PR #1358](https://github.com/rust-nostr/nostr/pull/1358)，添加了事件终结特征和 NIP 特定的事件构建器，使得为特定协议函数构造正确类型的事件更容易。[PR #1363](https://github.com/rust-nostr/nostr/pull/1363) 反向移植了一个修复，确保 NIP-46 signer 在发送连接响应之前订阅通知，关闭了紧接在连接后到达的 client 消息可能被错过的竞态条件。

**dart-nostr** 合并了 [PR #44](https://github.com/ethicnology/dart-nostr/pull/44)，添加了 Namecoin `.bit` relay 解析器和 TLSA 引脚记录，让 Flutter 应用能够通过 Namecoin DNS 将 `wss://example.bit/` relay URL 解析到它们的实际 WebSocket 地址。

**Dart NDK**（Dart/Flutter Nostr 开发套件，现在在 `relaystr/ndk`）合并了 [PR #464](https://github.com/relaystr/ndk/pull/464)，实现 NIP-77，即离线事件签名协议。在 signer 方面，[PR #602](https://github.com/relaystr/ndk/pull/602) 和 [PR #601](https://github.com/relaystr/ndk/pull/601) 添加了 Web 特定的事件 signer 和 `PlatformEventVerifier` 抽象，让 Flutter Web 应用可以使用平台 signer 而无需单独的代码路径；[PR #604](https://github.com/relaystr/ndk/pull/604) 引入了用于运行时 signer 选择的事件 signer 工厂。[PR #608](https://github.com/relaystr/ndk/pull/608) 添加了 `getDmRelays()` 以获取用户的 NIP-17 DM relay 列表（kind:10050），[PR #600](https://github.com/relaystr/ndk/pull/600) 修复了 NIP-46 签名字段保留，因此远程 signer 不会在往返中丢失字段。

**Pages by Form\***（[repo](https://github.com/formstr-hq/nostr-docs)）是 Formstr 的 Nostr 原生协作文档应用，托管在 [pages.formstr.app](https://pages.formstr.app)，本周合并了四个 PR，加强了加密附件和文档管理流程。[PR #37](https://github.com/formstr-hq/nostr-docs/pull/37) 通过内联加密附件修复了 DOCX、HTML 和 PDF 导出中缺失的图像：它从 Blossom 服务器获取 `<encrypted-file>` blob，使用存储的密钥和 nonce 通过 AES-GCM 256 位解密，验证图像 MIME 类型，并将它们转换为 base64 数据 URL，因此导出保留了只以加密形式存在于 Blossom 上的图像。[PR #39](https://github.com/formstr-hq/nostr-docs/pull/39) 添加了本地文档搜索机制，[PR #38](https://github.com/formstr-hq/nostr-docs/pull/38) 清理了重命名流程，[PR #40](https://github.com/formstr-hq/nostr-docs/pull/40) 修复了共享备份处理。

**Zap Cooking** 合并了 [PR #396](https://github.com/zapcooking/frontend/pull/396)，这是信息流全面改造的第一阶段，奠定了信息流渲染原语，尚未有任何用户可见的变化。该 PR 引入了一个 NIP-92 `imeta` 标签解析器，读取 `url`、`m`（MIME）、`dim`（尺寸）、`blurhash`、`alt`、`x`（文件哈希）和 `fallback` 插槽，加上一个手工移植的规范 blurhash 解码器（约 200 LOC），通过 canvas 生成 PNG 数据 URL，具有 SSR 安全的 null 备选。当 `imeta` 标签不存在时，解析器回退到使用当前信息流已使用的相同启发式方法从事件内容中提取原始图像和视频 URL。

**Nurunuru**（ぬるぬる、`tami1A84/null--nostr`）是一个具有原生 Android、iOS 和 Web 变体的 Nostr client，共享 Rust FFI 引擎，在 [PR #176](https://github.com/tami1A84/null--nostr/pull/176) 中合并了其 v1.5.0 Native → Web 同步。此同步为 Web 构建带来了 Android v1.4.9 和 iOS 1.0.4 上已经发布的几个功能添加：[NotificationModal](https://github.com/tami1A84/null--nostr/pull/176) 现在浮现生日通知、互相关注 zap 检测和自定义 emoji 反应通知；反应选择器放弃了 Unicode 默认反应快速行，并将 UX 集中在自定义 emoji 上；`lib/recommendation.js` 中的推荐引擎过滤掉没有图标或显示名称的用户，并优先处理 Following 条目，Recommended 在后台加载。语音输入是一个反方向的功能：Web 构建已经使用 ElevenLabs Scribe 流式传输，v1.5.0 将 Native 端部分同步到 OS 标准的 `SpeechRecognizer`（Android）和 `SFSpeechRecognizer` + `AVAudioEngine`（iOS），而完整的 Native Scribe 集成推迟到 v1.6。

## 协议和规范工作

**PR [#2251](https://github.com/nostr-protocol/nips/pull/2251)** 收紧了 NIP-70 受保护事件规范：它现在明确指出，嵌入受保护事件完整内容的转发必须被 relay 拒绝。NIP-70 定义了 `-` 标签，表示笔记作者不同意其笔记被重新发布。原始规范涵盖了 relay 过滤行为，但对转发情况留下了歧义。此 PR 关闭了该缺口。Citrine 的 [PR #151](https://github.com/greenart7c3/Citrine/pull/151) 在同一周在 relay 端实现了强制执行。

**PR [#1653](https://github.com/nostr-protocol/nips/pull/1653)** 提议一个 Drafts NIP，用于保存和同步私密草稿事件。该提议使用具有 `draft` 状态的可替换事件和 NIP-44 加密（加密给作者自己的密钥），让 client 可以将进行中的工作保存到 relay 而不让这些事件对任何其他人可见。草稿事件将完整的预期发布事件作为加密内容携带，包括其最终的 kind 和 tags。

**Snapshots（[PR #2279](https://github.com/nostr-protocol/nips/pull/2279)）** 是一个开放提议，用于定义一个不可变的快照事件，以保留可替换 Nostr 事件的一个精确版本。快照事件在给定时间点携带可替换事件的完整内容，具有一个 `a` 标签链接回可替换事件的地址，因此所有历史版本可以一起查询。这使得观察者即使在 relay 停止保留旧版本后也能检查历史状态。

**Namecoin NIP-05 浪潮：** 本周看到了一次协调努力，将 `.bit` NIP-05 解析添加到 Nostr client。NIP 讨论信息流捕获了针对 Aegis（[#14](https://github.com/ZharlieW/Aegis/pull/14)，它在 signer 处添加签名时验证）、nostter（[#2128](https://github.com/SnowCait/nostter/pull/2128)）和 dart-nostr（[#44](https://github.com/ethicnology/dart-nostr/pull/44)）的开源 PR，以及一个上游 NIP 草案（[PR #2349](https://github.com/nostr-protocol/nips/pull/2349)）。Aegis PR 值得注意的是将验证放在生产者端：signer 在签名任何声称 `.bit` 身份的 kind:0 事件之前检查 Namecoin 链，并在不匹配时警告用户，在事件到达任何 relay 之前捕获问题。

## NIP Deep Dive：NIP-07（用于 Web 浏览器的 window.nostr）

[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) 定义了浏览器扩展向 Web 应用暴露的 `window.nostr` 接口。它是 Web 上部署最广泛的 signer 接口，由包括 Alby、nos2x、Flamingo 和 horse 在内的扩展实现。

该接口有两个必需方法和几个可选方法。`window.nostr.getPublicKey()` 以十六进制字符串形式返回用户的公钥，而不会将私钥暴露给调用页面。`window.nostr.signEvent(event)` 接受一个带有 `created_at`、`kind`、`tags` 和 `content` 的部分事件，并返回添加了 `id`、`pubkey` 和 `sig` 的完整签名事件。关键点是私钥永远不会离开扩展的隔离上下文；Web 应用提交一个未签名事件，并收到一个已签名的事件。

可选方法涵盖加密：用于旧的 NIP-04 方案（现已弃用）的 `window.nostr.nip04.encrypt` 和 `window.nostr.nip04.decrypt`，以及用于当前 NIP-44 方案的 `window.nostr.nip44.encrypt` 和 `window.nostr.nip44.decrypt`。因此，支持 NIP-44 的扩展可以处理直接消息加密和任何其他需要 pubkey-keyed 加密的应用，而无需调用页面看到 nsec。

规范还包括对扩展作者的建议：在扩展 manifest 中使用 `"run_at": "document_end"` 加载脚本，以便 `window.nostr` 在页面加载时同步可用，避免 client 在扩展注入之前检查 `window.nostr` 的竞态条件。

NIP-07 实际应用的一个关键示例是上面介绍的 Keycast 项目。Keycast Web 前端使用 NIP-07 签名 NIP-98 HTTP auth 事件：SvelteKit 应用从不直接处理用户的 nsec。它调用 `window.nostr.signEvent` 来生成 auth 头，然后将该头发送到 Keycast API。这种架构意味着密钥材料在整个团队密钥管理流程中保留在浏览器扩展中。

```json
{
  "id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 1,
  "tags": [],
  "content": "Hello from a NIP-07 signed event",
  "sig": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2cdd"
}
```

## NIP Deep Dive：NIP-39（个人资料中的外部身份）

[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) 定义了 Nostr 用户如何在其个人资料中声明对外部平台身份的控制权。每个声明使用 kind:10011 事件内的一个 `i` 标签，断言对另一个平台上的特定账户的所有权，以及一个可以独立验证的证明。

每个标签遵循 `["i", "platform:identity", "proof"]` 格式，其中 `platform:identity` 用冒号分隔符组合平台名称和用户名（`github:semisol`、`twitter:semisol_public`）。`proof` 指向平台本身上的可验证工件。

对于 GitHub，证明是一个 Gist ID。用户从其 GitHub 账户创建一个公开的 Gist，其中包含文本 `Verifying that I control the following Nostr public key: npub1...`。验证声明的 client 获取 `https://gist.github.com/<identity>/<proof>`，并检查该 Gist 是由声称的 GitHub 用户名撰写的，并包含预期的 pubkey。对于 Twitter，证明是一个 tweet ID；对于 Mastodon，是一个帖子 ID；对于 Telegram，是公共群组中的一个消息引用。

身份提供者名称只能包含 `a-z`、`0-9` 和字符 `._-/`，并且不能包含 `:`。身份名称应规范化为小写，当存在多个别名时使用主别名。

本周正在进行的 Namecoin `.bit` NIP-05 讨论显示了 NIP-39 在更广泛的身份栈中的作用：它提供了一种标准化、与 relay 无关的方式，将 Nostr 密钥与其他地方已建立的身份交叉引用，而不需要任何中央验证权威机构。client 可以通过在命名平台上获取一个公共工件来独立验证证明，并且证明绑定到 Gist 或 tweet 文本中的特定 Nostr pubkey，而不是通用的平台凭据。

```json
{
  "id": "b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 10011,
  "tags": [
    ["i", "github:semisol", "9721ce4ee4fceb91c9711ca2a6c9a5ab"],
    ["i", "twitter:semisol_public", "1619358434134196225"],
    ["i", "mastodon:bitcoinhackers.org/@semisol", "109775066355589974"]
  ],
  "content": "",
  "sig": "1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3eff"
}
```

---

本周就到这里。如果你正在构建什么或有消息要分享，请在 Nostr 上私信我们，或访问 [nostrcompass.org](https://nostrcompass.org)。
