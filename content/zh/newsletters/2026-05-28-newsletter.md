---
title: 'Nostr Compass #24'
date: 2026-05-28
publishDate: 2026-05-28
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-28-newsletter.md
translationDate: 2026-07-01
---

Amethyst v1.11.0 落地完整的 NIP-52 日历实现，带有提醒、链上 Bitcoin zap 分成和 Marmot 群组回复支持。White Noise v2026.5.22 通过 Notification Service Extension 发布 iOS 推送通知，还有屏蔽 UX 和"添加成员"按钮。Vector v0.4.0 落地了从零开始的 vector-core 重写、一键 Tor 带桥接、NIP-46 远程 signer、完整 negentropy MLS 群组同步，以及供 AI agent 使用的 21 工具 MCP 服务器。Applesauce v6.1.0 引入 NIP-51 查找 relay 列表（kind 10086）和完整的 NIP-34 git-cast 工厂集合。MDK 通过统一的 UniFFI 接口在 iOS 和 Android 上添加 NIP-40 消失消息，Mostro v0.17.4 通过第 3 阶段将削减的保证金支付给赢家来关闭反滥用保证金循环。Notedeck 为 giftwraps 和线程回填合并了完整的 NIP-77 negentropy 协调，Cordn 作为协调者中介的 MLS 消息应用浮出水面，以单点可用性依赖换取更紧密的 epoch 排序和更简单的运营模型，一个名为 deepmarks 的 NIP-B0 参考实现发布了策展人货币化的书签 client，Formstr 团队开放了四个协调的日历 NIP 提案，涵盖参与者自我移除、私密事件、循环和去中心化预约调度。

## 头条报道

### Amethyst v1.11.0：日历、链上 zap 分成和 Marmot 回复

Amethyst 是由 Vitor Pamplona 维护的 Android 版 Nostr client，发布了 [v1.11.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.11.0)。[PR #2994](https://github.com/vitorpamplona/amethyst/pull/2994) 添加了带有专用 UI 和提醒系统的 [NIP-52](/zh/topics/nip-52/) 日历事件实现，因此日历事件现在在自己的时间线类别中渲染，与通用的 kind-30023 长文视图分开。[PR #3018](https://github.com/vitorpamplona/amethyst/pull/3018) 使用分成支持扩展了链上 Bitcoin zaps，根据现有的 zap-split 标签将一笔 Bitcoin 交易分发给多个接收者，因此链上支付与 Lightning 分成表现相同。[PR #2974](https://github.com/vitorpamplona/amethyst/pull/2974) 添加了一个带分页的链上交易历史屏幕，展示每笔已结算 zap 及其区块确认状态。

群组消息与一对一聊天获得了对等性：[PR #2995](https://github.com/vitorpamplona/amethyst/pull/2995) 为 [Marmot](/zh/topics/marmot/)/MLS 群组消息添加了回复支持，因此加密群组内的线程现在以与公开笔记相同的父引用 UI 渲染。[PR #2984](https://github.com/vitorpamplona/amethyst/pull/2984) 通过检查 LNURL 提供者与接收者声明的 lud16 匹配来加固 [NIP-57](/zh/topics/nip-57/) zap 收据验证，关闭了一类伪造：第三方 LNURL 可能为从未到达的支付铸造收据。[PR #2968](https://github.com/vitorpamplona/amethyst/pull/2968) 接受 [NIP-92](/zh/topics/nip-92/) `imeta` 标签中的浮点尺寸，使 Amethyst 与发布来自 iPhone Retina 显示屏等设备的分数像素密度值的 client 保持一致。该版本还接入了 Payment Targets，一个新的可替换事件多轨道打赏罐，将在下面的协议部分讨论。

### White Noise v2026.5.22：iOS 推送、屏蔽 UX 和添加成员

White Noise 是 Marmot 协议群组消息应用，发布了 [v2026.5.22](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.5.22%2B25)，头条功能是 iOS 推送通知。[PR #673](https://github.com/marmot-protocol/whitenoise/pull/673) 实现了一个 iOS Notification Service Extension（NSE），它在扩展进程内解密 MLS 消息并将它们作为系统通知呈现，因此 iPhone 用户不再需要将应用置于前台以接收消息。Android 推送 token 布线通过相同的后端管道路由，每个平台的 NSE 将密文排除在 broker 之外。

[PR #676](https://github.com/marmot-protocol/whitenoise/pull/676) 添加了完整的屏蔽和取消屏蔽 UX，带有确认流程和联系人列表过滤。[PR #679](https://github.com/marmot-protocol/whitenoise/pull/679) 在群组信息屏幕添加了期待已久的"添加成员"按钮，关闭了群组管理员不得不退而使用分享链接的 UX 缺口。[PR #688](https://github.com/marmot-protocol/whitenoise/pull/688) 引入了专用的 iOS 通知设置屏幕，[PR #687](https://github.com/marmot-protocol/whitenoise/pull/687) 为媒体和消息接入了长按分享。

### MDK 跨平台添加 NIP-40 消失消息

Marmot Development Kit 是 White Noise iOS、White Noise Android 及任何未来 Marmot client 使用的共享 Rust 核心，合并了 [PR #306](https://github.com/marmot-protocol/mdk/pull/306) 以通过 UniFFI 桥接公开消失消息验证和 [NIP-40](/zh/topics/nip-40/) 过期处理。该 PR 是三部分系列中的第二部分。iOS 和 Android 现在共享一个过期逻辑的 Rust 实现；时间规则存在于一个经审计的代码路径中，两个平台通过 UniFFI 消费。[PR #307](https://github.com/marmot-protocol/mdk/pull/307) 限制存储的 welcome 失败原因长度并在持久化之前清理它们，这是补充上周发布的 welcome 事件处理的单独加固工作。

MLS 中的消失消息不仅仅是 UI 层面的功能。过期标签与加密消息封套一起发布，因此从未打开消息的接收者仍然会让底层密文在 relay 层与接收 client 中的任何缓存副本一起过期。有了 MDK 拥有验证路径，跨 client 的行为保持一致：任何符合规范的 Marmot 实现都强制执行相同的过期语义，因此一个 client 遵守过期而另一个永久缓存不再是可移植性隐患。

### Mostro v0.17.4：第 3 阶段关闭削减保证金循环

[Mostro](https://github.com/MostroP2P/mostro) 是构建在 Nostr 之上的点对点 Bitcoin 交换协议，在 [v0.17.4](https://github.com/MostroP2P/mostro/releases/tag/v0.17.4) 中发布了其反滥用保证金推出的第 3 阶段。[PR #738](https://github.com/MostroP2P/mostro/pull/738) 落地了削减保证金的支付流程，将输家没收的抵押品拿出来支付给争议赢家。[PR #743](https://github.com/MostroP2P/mostro/pull/743) 添加了第 3.5 阶段，即向赢家发出的明确支付确认消息，让他们知道削减的 sats 已结算，确认事件到达与争议解决相同的 Nostr 会话上。上周报道的第 2 阶段将削减引入为管理员操作；第 3 阶段是威胁惩罚与执行惩罚之间的区别。

[PR #746](https://github.com/MostroP2P/mostro/pull/746) 让守护进程可以终结缺少求解器行的争议，这是一个此前会在遗留争议上停滞解决的边缘情况。[PR #748](https://github.com/MostroP2P/mostro/pull/748) 容忍 Yadio 的 `/exrates/BTC` 响应中的空 rates，因此 Yadio 的短暂中断不再破坏 Mostro 的法币转换路径。[PR #745](https://github.com/MostroP2P/mostro/pull/745) 记录了多源价格提供商的规范，为移除 Yadio 作为单点故障奠定基础。Mostro 移动 client 在 [PR #596](https://github.com/MostroP2P/mobile/pull/596) 中连接了匹配的第 3 阶段索赔路径。

### Applesauce v6.1.0：查找 relay 和 NIP-34 git casts

[Applesauce](https://github.com/hzrd149/applesauce) 是模块化 Nostr 工具包，为 Coracle、noStrudel 和 Pablo F7z 的技术栈提供支持，在其包中发布了 [v6.1.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-actions%406.1.0)。该版本添加了一流的 [NIP-51](/zh/topics/nip-51/) 查找 relay 列表支持：kind 10086 事件让用户可以发出"如果你想找到我，请询问这些 relay"的信号，作为发现原语与 [NIP-65](/zh/topics/nip-65/) 发件箱列表并列。构建在 `applesauce-core` 之上的应用获得一个响应式的 `User.lookupRelays$` observable 和 `applesauce-relay` 中的匹配加载器。

[NIP-34](/zh/topics/nip-34/) git-cast 工厂到达 `applesauce-factory`，为每个基于 Applesauce 构建的 client 提供一行代码发布 repo 公告（kind 30617）、patches（kind 1617）和 issues（kind 1621）的路径。`User.favoriteGitRepos$`、`User.gitAuthors$` 和 `User.graspServers$` 响应式属性让应用可以直接从同一个 User 对象列出用户关注的 repo、repo 维护者和配置的 GRASP 服务器。该版本还在 [PR #73](https://github.com/hzrd149/applesauce/pull/73) 中修复了静默丢弃离线 relay 的 pool 手动方法。

### Notedeck 合并用于 giftwraps 和线程回填的 NIP-77 negentropy

[Notedeck](https://github.com/damus-io/notedeck) 是 Damus 的原生多列桌面 client，5 月 25 日合并了 [PR #1459](https://github.com/damus-io/notedeck/pull/1459)，将完整的 [NIP-77](/zh/topics/nip-77/) negentropy 协调接入共享的发件箱路径。该 PR 添加了 NIP-77 client 和 relay 帧、relay 本地的 negentropy 会话，以及驱动本地集合协调和缺失事件获取的发件箱完整历史跟踪器。消息 giftwraps 获得 negentropy 协调，因此可以从所选账户的读取 relay 恢复私密消息封套。线程视图不再受实时订阅回复限制的限制。Dave PNS 用共享发件箱路径取代其 Dave 本地的 negentropy 实现，同时保留其现有的有界历史行为。

实时订阅和 negentropy 现在使用独立的过滤器。一个流可以保留一个小的实时请求，同时发出一个更广泛的 negentropy 过滤器以协调 relay 已有的内容。该 PR 有意不为主页或个人资料时间线启用广泛的 negentropy 同步，那样会改变冷启动的成本特征。为协调、giftwrap 交付、线程回填、Dave PNS 恢复、账户切换、relay 重定向、fetch 重试和 NIP-77 relay 行为添加了测试覆盖。

### Vector v0.4.0：vector-core 重写、Tor、NIP-46、完整 negentropy MLS 和 MCP agent 接口

[Vector](https://github.com/VectorPrivacy/Vector) 是构建在 NIP-17 DM 和 Marmot 群组之上的隐私聚焦跨平台消息应用，发布了迄今为止规模最大的 [v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)。头条是从零开始的引擎重写：Vector 的所有逻辑现在都存在于一个解耦的 crate `vector-core` 中，跨桌面、Android 和任何未来 client 共享，核心本身有 440 多个测试，应用外壳精简了数千行代码。这次重写为 Vector CLI、机器人和 SDK 奠定了基础，它们将驱动与 GUI 相同的协议代码。

Tor 集成随一键流量路由和用于审查规避的桥接支持一起发布。多账户支持通过应用内切换器落地。远程 signer 登录通过 [NIP-46](/zh/topics/nip-46/) 到达，支持通过 QR 或粘贴 URI 进行 bunker 配对，因此用户可以在不暴露其 nsec 的情况下登录。为所有人删除在 [NIP-17](/zh/topics/nip-17/) DM 和 [Marmot](/zh/topics/marmot/) 群组聊天中都能工作，Vector 有意保留临时签名密钥，这是发布说明明确指出的规范偏差："偏离传统的 NIP-17/Marmot 规范以增强用户隐私控制。"保留的临时密钥让 Vector client 有本地证据表明删除是由原始发送者认可的，但也意味着任何其他接触 Vector 的 client 看到的删除可验证性接口与基线的 NIP-17/Marmot client 不同。

MLS 群组同步现在通过 [NIP-77](/zh/topics/nip-77/) negentropy 完全协调，这是 Notedeck 本周为 giftwraps 和线程采取的相同方向。Blossom 上传器跨多个服务器失败切换、了解每个服务器的能力，并跨设备同步服务器列表。自定义 emoji 包由用户创建、可分享，并与其他 Nostr client 交叉兼容。SQLite 内存从约 308MB 降至 5MB。emoji 面板从磁盘缓存打开，Discord 风格的短代码（`:smile:`）加上 Unicode 频率排名首先浮现正确的字形。

最新颖的新增是 `vector-agent`，一个 MCP（Model Context Protocol）服务器，公开 21 个工具，让 AI agent 可以驱动 Vector：发送 DM、管理群组、上传文件、编辑个人资料。这是本周第二个发布 MCP 接口的 Nostr 项目（与 Shopstr 并列），也是第一个这样做的消息类应用。加上 AgentNoise（上周报道），agent 控制的 Nostr client 模式正在从一次性实验转向一个有意的平台方向。

### Cordn 作为协调者中介的 MLS 消息应用浮出水面

[Cordn](https://cordn.net)（Web client 位于 [cordn.net](https://cordn.net)，repo 位于 [Cordn-msg/cordn](https://github.com/Cordn-msg/cordn) 和 [Cordn-msg/cordn-web](https://github.com/Cordn-msg/cordn-web)）是一个新的 MLS 消息应用，采取与 Marmot 不同的架构策略。[Marmot](/zh/topics/marmot/) 是完全基于 relay 的，没有特权协调者（每个群组成员直接写入 relay，任何符合规范的 relay 都可以承载流量），而 Cordn 引入了一个每群组协调者角色，作为 [ContextVM](/zh/topics/contextvm/) 服务实现。协调者对 MLS commits 排序并处理 welcome 分发。

Cordn 的论据，在其 [/why](https://cordn.net/why) 页面上陈述，是在生产消息应用中部署的 MLS "不是无协调的"，"弱有序的公共传播"使得没有强协调点的情况下群组状态收敛"困难得多"。协调者中介的设计提供可预测的 epoch 前进和更简单的并发 commit 解决。参与者使用临时密钥连接到协调者，因此协调者了解群组 ID 和 commit 流量的时间，但不了解哪些长期 pubkey 是成员。任何查询 relay 获取 Marmot 群组的一方都已经可以看到相同的接口：按群组 ID 的群组活动，时间从事件到达可推断。Cordn 也承认，自托管情况下"可用性信任仍然存在"：自托管协调者避免了运营者层集中化的担忧，但为群组活跃度引入了单点故障。Marmot 通过将排序留给 MLS 本身（epochs 和 Commit 消息在协议内处理排序），并通过 [NIP-59](/zh/topics/nip-59/) gift wrap 分发 Welcome 事件来避免那个单点，代价是管理员端的纪律：管理员必须等待 relay 确认 Commit 后才能发送匹配的 Welcome，而 client 必须在 relay 交付与状态转换赛跑时协调并发 commits。

对于任何挑选私密消息栈的团队来说，这种对比值得深入研究。Marmot 用一些实现复杂性换取一个与 relay 无关的部署，路径上没有特权参与者。Cordn 用单点可用性依赖换取更紧密的排序和更简单的运营模型。两个项目都建立在 [MLS](/zh/topics/mls/) 之上，并使用 Nostr 作为身份和传输层。分歧在于协调成本存在于何处。cordn-msg repo 显示出稳定的 commit 节奏，协调者服务在 ContextVM 之上实现，MLS 层构建在 `ts-mls` 之上。

### deepmarks：策展人货币化发布的 NIP-B0 书签

[deepmarks-public](https://github.com/ostermayer/deepmarks-public) 是提议的 [NIP-B0](/zh/topics/nip-b0/) 书签规范（kind 39701）的参考 client，具有三盒架构（策展人、索引器、查看器）和一个由直接向策展人的 [NIP-57](/zh/topics/nip-57/) zaps 资助的分级系统。client 实现了 NIP-B0、[NIP-07](/zh/topics/nip-07/)、[NIP-46](/zh/topics/nip-46/)、NIP-57、[NIP-44](/zh/topics/nip-44/)、[NIP-98](/zh/topics/nip-98/)、[NIP-65](/zh/topics/nip-65/)，以及用于文件存储的 Blossom BUD-01 和 BUD-04。一个 21,000-sat 终身分级将付费读者转变为策展人的定期 zap 接收者。策展人发布书签事件，索引器用机器可读的元数据丰富它们，查看器渲染信息流；每个角色都是一个独立的可部署服务。

## 发布

### Amber v6.1.0 GA：加密的每账户备份

**Amber** 本周从 `v6.1.0-pre3` 移至 GA [v6.1.0](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0)。[PR #444](https://github.com/greenart7c3/Amber/pull/444) 发布了应用权限数据库的加密备份和恢复，[PR #446](https://github.com/greenart7c3/Amber/pull/446) 按账户拆分备份，因此拥有多个 Nostr 身份的用户可以独立备份和恢复每组应用授权。上周报道的 PSBT 签名工作在 GA 版本中。

### Citrine：每 relay 订阅和 onion URL 泄漏防护

**Citrine** 是与 Amethyst 一起发布的设备端个人 relay，本周期发布了两个修复。[PR #157](https://github.com/greenart7c3/Citrine/pull/157) 从单一全局订阅切换到每 relay 标记订阅，因此共享 `kinds: [1]` 过滤器的两个源 relay 不再在聚合器端冲突。[PR #162](https://github.com/greenart7c3/Citrine/pull/162) 在出站 Tor 代理被禁用时过滤 onion relay URL，防止 onion 地址泄漏到明网路由路径上。

### Angor v0.2.27 和 v0.2.28：relay 可靠性和 Boltz 重连

**Angor** 发布了 [v0.2.27](https://github.com/block-core/angor/releases/tag/v0.2.27) 和 [v0.2.28](https://github.com/block-core/angor/releases/tag/v0.2.28)。[PR #874](https://github.com/block-core/angor/pull/874) 修复了一个 relay 去重 bug，其中一次只连接一个 relay，这是一个静默降低具有多个 relay 端点的项目可靠性的回归。[PR #876](https://github.com/block-core/angor/pull/876) 为 Boltz 潜艇交换监控添加了 WebSocket 重连逻辑，因此短暂的断开不再让交换处于未知状态。

### Nostrord v1.1.0：NIP-57 zaps 和 NIP-29 角色区分

**Nostrord** 发布了 [v1.1.0](https://github.com/nostrord/nostrord/releases/tag/v1.1.0)，为消息和个人资料添加了 [NIP-57](/zh/topics/nip-57/) Lightning zap 支持（[PR #98](https://github.com/nostrord/nostrord/pull/98)），并在活动信息流中正确区分了 [NIP-29](/zh/topics/nip-29/) 角色变更和成员添加（[PR #92](https://github.com/nostrord/nostrord/pull/92)），此前它们渲染方式相同，遮蔽了谁被提拔与谁被邀请。

### ぬるぬる v1.5.x：SQLCipher MLS 密钥库和 epoch 追赶

**ぬるぬる**（nurunuru，作者 tami1A84）是一个日语 Nostr client，实现了 MLS 群组消息（kind 443）以及 NIP-44、NIP-50 高级搜索、NIP-55 和 NIP-70，本周发布了五个版本。[PR #184](https://github.com/tami1A84/null--nostr/pull/184) 在 rust-engine 层为 MLS 密钥库引入 SQLCipher 加密。[PR #187](https://github.com/tami1A84/null--nostr/pull/187) 和 [PR #188](https://github.com/tami1A84/null--nostr/pull/188) 分别将 SQLCipher 扩展到 Android 和 iOS，具有遗留明文清除步骤和 CI 守卫。[PR #189](https://github.com/tami1A84/null--nostr/pull/189) 和 [PR #191](https://github.com/tami1A84/null--nostr/pull/191) 在两个平台上添加 MLS 对等 epoch 追赶，具有重放缓存和恢复横幅，因此在群组 commits 上落后的 client 可以在不丢失对话的情况下恢复。ぬるぬる 是构建在来自 `marmot-protocol/mdk` 的 `mdk-core`、`mdk-sqlite-storage` 和 `mdk-storage-traits` 之上的 Marmot client，因此 SQLCipher 和 epoch 追赶工作落在了 White Noise 使用的同一个 MDK 运行时内。

### Bitcredit Core v0.5.10：Nostr 根源的区块传播修复

**Bitcredit Core** 发布了 [v0.5.10](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.10)，修复了区块传播期间缺少的 Nostr-node-id 字段，该字段正在破坏包括身份上传的公司创建流程。Bitcredit 是一种电子账单协议，使用 Nostr 身份作为公司和账单传播事件的信任根。

## 未发布的更改

**Jumble** 打开了 [PR #797](https://github.com/CodyTseng/jumble/pull/797)，通过 Pomegranate 门限 signer 实现 Google 登录，让用户可以将其 Nostr 密钥拆分给多方，因此没有单个 signer 持有完整的机密。这是超越 bunker 或 nsec 导入流程的有意义的一步：用户即使一个 signer 方被入侵也可以恢复其账户，而该方从未持有完整的私钥。

**Shopstr** 打开了 [PR #492](https://github.com/shopstr-eng/shopstr/pull/492) 初始化一个 MCP（Model Context Protocol）服务器，[PR #494](https://github.com/shopstr-eng/shopstr/pull/494) 构建支持基础设施（relay fetch、解析器、验证、错误、去重、审计日志），[PR #472](https://github.com/shopstr-eng/shopstr/pull/472) 为 MCP relay 管理器添加 relay 白名单。这使 Shopstr 成为第一个将自己公开为 MCP 服务器的 Nostr 市场，因此 AI agent 可以浏览 NIP-99 列表并作为结构化工具对其采取行动。

**Keydex** 是 Shamir 秘密共享保险库，在 [PR #226](https://github.com/mplorentz/keydex/pull/226) 中打开了一个重大迁移，将自定义 kind 1337-1345 移到 713-721 范围，同时 [PR #239](https://github.com/mplorentz/keydex/pull/239) 在 Shamir 共享上添加 AEAD，[PR #234](https://github.com/mplorentz/keydex/pull/234) 迁移到 GF256 算术。kind 范围迁移使 Keydex 与 NIPs repo 分配自定义 kind 的方式保持一致，远离自我声明的范围。

**Mill**（[nostr-mill](https://github.com/0ceanSlim/nostr-mill)）是来自 [OceanSlim](https://github.com/0ceanSlim)（[grain](https://github.com/0ceanSlim/grain) Go relay 的维护者）的新即插即用 Nostr signer UI，作为单脚本标签 Web Component 在 [npm](https://www.npmjs.com/package/nostr-mill) 和 [jsDelivr](https://cdn.jsdelivr.net/npm/nostr-mill/dist/mill.umd.js) 上发布。一个 `<script>` 标签给 Web 应用一个统一 UI 下的所有六个常见 signer 入口点：[NIP-07](/zh/topics/nip-07/) 浏览器扩展、[NIP-46](/zh/topics/nip-46/) bunker（URL 粘贴或 QR 配对，带有用户可指定的 relay，在页面内 bunker 集成中不寻常）、通过 Android intents 的 [NIP-55](/zh/topics/nip-55/) Amber、通过 AES-256-GCM 与 PBKDF2 存储在 `sessionStorage` 中的加密 nsec、只读 `npub`，以及浏览器内 keypair 生成。该组件可通过 29 个作用域限定于 Shadow DOM 的 CSS 自定义属性进行主题化，并公开一个小的 SemVer 跟踪 API（`MILL.open`、`mill:connected` / `mill:disconnected` 事件、命名的主题导出）。维护者的动机是 bunker 登录流程已经在 Nostr 中一个 Web 应用一个 Web 应用地被重新实现。整合到共享组件让 client 可以就 signer UX 应如何表现达成一致，并将可选流程（如通过门限 signer 的委托密钥登录，反映了上面报道的 Wisp 的基于 Pomegranate 的 Google 登录）变成任何应用都可以放入的可重用接口。Mill 处于 npm v1.5.0，单一维护者、alpha 阶段，grain 是计划中的第一个集成者。

**moStard** 是由 [roguehashrate](https://github.com/roguehashrate) 制作的 [noStrudel](https://github.com/hzrd149/nostrudel) 的 Monero 优先分叉，本周达到 [v1.0.1](https://github.com/roguehashrate/moStard/releases)，具有精简的功能集和分层在同一 Applesauce + worker-relay 栈上的 Monero 主题身份。本周的工作落地了 Zapstore 的 kind 32267 软件应用事件的渲染（时间线中的嵌入卡片显示应用名称、图标、截图、平台、许可证，以及指向 `zapstore.dev/apps/<d-tag>` 的启动链接）、通过 kind 20 和 kind 21 的投票、基于 NIP-A3 Payment Targets 的每方法 QR code 打赏、笔记中的 markdown 渲染、外部 GIF 键盘的 GIF 选择器支持，以及 Amber signer 配对修复。Monero 框架扩展到打赏流程：`monero` 地址的 NIP-A3 `payto` 条目在同一 UI 中获得一流按钮，与 `lightning` 和 `bitcoin` 并列。该 client 是单一维护者、alpha 阶段，但 5 月 27 日的工作展示了一个构建者在几天内将本周的协议规范公告中的 NIP-A3 直接拉入一个正在发布的分叉。

## NIP 更新和协议规范工作

### 日历 NIP 栈：来自 Formstr 团队的四个提案

Ix2（[@geralt-debugs](https://github.com/geralt-debugs)）在 5 月 17 日打开了四个协调的 NIP PR，全部引用了同一作者已经发布的 [calendar.formstr.app](https://calendar.formstr.app) 实现。[PR #2350](https://github.com/nostr-protocol/nips/pull/2350) 提议 kind 84 作为一个通用的"参与者自我移除"事件：任何事件上的标记参与者都可以发布一个 kind 84，通过 `e`、`a` 和 `k` 标签引用原始事件以表示退出。relay 必须在履行移除之前验证 kind 84 签名者出现在被引用事件的 `p` 标签中，kind 5 删除始终优先。该 PR 概括了先前仅在 NIP-52 日历上下文中描述的模式，因此 kind 84 成为非作者从任何参与者事件中撤回的标准方式。

[PR #2351](https://github.com/nostr-protocol/nips/pull/2351) 是日历栈的基础：用于私密日历事件的 NIP-52E（kind 32678 基于时间、32681 日事件、32123 私密日历列表、31926 忙碌列表、1052 gift wrap、52 rumor）和用于循环事件的 NIP-52R。架构核心是查看密钥模式：一个随机生成的 keypair 用 NIP-44 加密事件内容，秘密部分（bech32 编码为 `nsec`）被 gift-wrapped 给每个参与者。signer 只持有公开的 `d` 标签；其他一切都存在于加密的 `content` 中。以这种方式将内容加密与身份解耦意味着编辑事件不需要为接收者重新分发密钥。NIP-52R 在现有的 kind 31923 和 31922 上定义了两个可选标签，使用裸的 RFC 5545 RRULE 值声明循环，当 RRULE 存在时 `D` 日索引变为可选。前向保密明确缺失：泄露的查看密钥会揭示同一 `d` 标签下事件的所有过去和未来版本。

[PR #2352](https://github.com/nostr-protocol/nips/pull/2352) 建立在 NIP-52E 之上，提供了一个去中心化的预约调度规范，PR 描述称之为"Calendly/Cal.com 的即插即用替代品，没有中央中介"。Kind 31927 使用加密的可用性窗口宣传调度页面；kind 32680 是主机端的自加密查看密钥恢复记录；kind 1057 和 1058 是 gift-wrapped 预订请求和响应。巧妙的机制：预订者在发送请求之前为未来的私密事件生成 `d` 标签和查看密钥，因此预订者可以立即用正确的密钥将预约添加到自己的日历，主机永远不必来回传递密钥。预订响应在外部包装上携带一个未加密的 `status` 标签，因此 relay 可以在不解密的情况下过滤。

参考实现已在 [calendar.formstr.app](https://calendar.formstr.app) 上线，并作为 Zapstore 上的 Calendar Android 应用。[PR #2351](https://github.com/nostr-protocol/nips/pull/2351) 关闭 [PR #2027](https://github.com/nostr-protocol/nips/pull/2027) 以支持它，整合了自年初以来一直开放的早期私密日历提案。

### Payment Targets 和 Silent Payments

本周有两个 NIP 提案在 `kind:30023` 长文文档中流传。

**Payment Targets** 提案（NIP-A3 / payto）定义了一个可替换的 kind 10133 事件，携带一个或多个 `["payto", "<type>", "<authority>"]` 标签，映射到 RFC 8905 `payto:` URI。支持的类型包括 bitcoin、lightning、ethereum、monero、nano、cashme、revolut 和 venmo。目的是标准化一个多轨道打赏罐，补充（而不是取代）基于 lud16 的 NIP-57 zaps。Amethyst v1.11.0 是第一个实现者；合并的 PR [#2953](https://github.com/vitorpamplona/amethyst/pull/2953) 和 [#3009](https://github.com/vitorpamplona/amethyst/pull/3009) 发布了订阅和观察接口，[PR #3011](https://github.com/vitorpamplona/amethyst/pull/3011) 为 `PaymentTargetsEvent` 连接 UI。

两个来自不同作者的竞争性 Silent Payments 提案出现。第一个变体通过公开的加法微调从 `nsec` 派生 BIP-352 silent-payment scan 和 spend 密钥，因此任何发送者都可以从 `npub` 构造一个 `sp1q...` 地址，无需设置。作者警告在规范中明确：`bscan` 和 `bspend` 必须与 nsec 完全相同的谨慎对待，因为 scan 密钥揭示 nsec。第二个变体采取相反的方法，将一个 `sp_address` 字段添加到 kind 0 个人资料元数据，包含一个标准 BIP-352 silent-payment 地址，其密钥独立于 Nostr 身份保存。变体二在结构上更安全。两个提案都引起了深思熟虑的评论线程；erskingardner（Marmot 主管）在跟踪该提案的 trbouma gist 上发布了一个详细的[评论](https://gist.github.com/trbouma/77648ebe1005b181b67d1c4b42c7f31d?permalink_comment_id=6167489#gistcomment-6167489)。他的核心担忧是变体 1 从 `nsec` 加上一个可公开计算的微调派生 scan 私钥，这意味着任何持有 scan 密钥的人（包括用户实际上必须委托的第三方扫描服务）都可以通过减去该微调来恢复完整的 `nsec`。让远程服务为你扫描入站付款的同一密钥也让该服务可以窃取你的身份和从中派生的任何资金。

在 NIP-34 git-over-Nostr 方面，hzrd149 向 [schemata](https://gitworkshop.dev/npub1zafcms4xya5ap9zr7xxr0jlrtrattwlesytn2s42030lzu0dwlzqpd26k5/relay.ngit.dev/schemata) 发布了 2 个 patches。[gitworkshop.dev](https://gitworkshop.dev/) 本身收到了两个问题报告：一个标记使用 NIP-46 远程 signer 时在页面刷新时丢失登录会话，另一个要求在 README 预览中使用不同的链接样式。

## 六年的 Nostr 五月

2026 年 5 月的最后一份 newsletter 从本周的发布中退后一步，走遍了 Nostr 历史上的五月。每一年都有不同的重心：2021 年只有一次 commit，2022 年是 NIPs repo 本身的形成，2023 年是协议规范的爆炸，2024 年是整合周期，2025 年是 negentropy 合并和 Damus 的 Notedeck 升级到 Beta 时，2026 年是这一期和前三期涵盖的月份。

### 2021 年 5 月

Nostr 六个月大。唯一的 Nostr 代码存在于 [fiatjaf/nostr](https://github.com/fiatjaf/nostr) 中，整个月恰好产生了一次 commit，但那次 commit 成为了协议使用最多的部分之一。5 月 22 日，fiatjaf [重新定位 NIP-02](https://github.com/fiatjaf/nostr/commit/9ee3a02) 作为联系人列表 NIP。commit 消息写道："repurpose NIP-02 and add NIP authorship"，明确的归功是给 arcbtc（LNbits 的 Ben Arc）的 [PR #16](https://github.com/nostr-protocol/nostr/pull/16)，在 2 月 9 日打开，fiatjaf 将该想法折叠到 NIP-02 的前一天关闭。arcbtc 的提案很小：一个"向 relay 发送关注者列表"的 kind，将"对恢复账户和推荐要关注的公钥有用"。fiatjaf 将其概括为一个单一的 `kind:3` 事件，其标签同时服务于三个目的。它们是关注列表（社交图）、petname 存储（朋友的本地昵称）和 relay 推荐源（关注对象使用的 relay）。同一个事件，每个作者可替换，成为了"这个人关注谁"、"他们如何称呼他们"和"他们在哪里阅读"的规范答案。接下来五年中构建的每个 client 都读取 `kind:3`。同一 commit 中添加的约定，即每个 NIP 都命名其作者，是为什么现在每个规范都有署名的原因。

### 2022 年 5 月

NIPs repo 成为社区项目的月份。5 月 1 日，fiatjaf 将规范从 `fiatjaf/nostr` [迁移](https://github.com/nostr-protocol/nips/commit/f25c7e6) 到专用的 [`nostr-protocol/nips`](https://github.com/nostr-protocol/nips) repo，并在 5 月 2 日添加了 [正式的接受标准](https://github.com/nostr-protocol/nips/commit/c053670)。两天后，Robert C. Martin（Uncle Bob）打开了 [PR #1](https://github.com/nostr-protocol/nips/pull/1)，即第一个外部 pull request，为 `e` 和 `p` 标签提议线程约定。该 PR 最初编号为 NIP-13，然后 [重命名为 NIP-10](https://github.com/nostr-protocol/nips/commit/bd4a81a) 以为 proof-of-work 腾出空间。前六个 NIP 中的三个是 Uncle Bob 的：NIP-10（线程标记）、NIP-14（[Subject 标签](https://github.com/nostr-protocol/nips/commit/ebacbcc)），以及 5 月 21 日锁定 [`kind:1` 作为规范短文本笔记 kind](https://github.com/nostr-protocol/nostr/commit/e22ea1a) 的 commit。5 月 5 日，William Casarin 做了他的第一个 NIP commits：[NIP-13 Proof of Work](https://github.com/nostr-protocol/nips/commit/d7a4aad) 和 [kind:2 推荐 relay 事件](https://github.com/nostr-protocol/nips/commit/ad1eb96)。第二天，fiatjaf 发布了 [NIP-07 `window.nostr`](https://github.com/nostr-protocol/nips/commit/37eb53e)，二十行 markdown，定义了今天仍在使用的浏览器扩展 signer 接口。同一周，David A. Harding 的 NIP-05 [CORS 警告](https://github.com/nostr-protocol/nips/commit/57b86d2) 和 NIP-01 的 [`filter.limit`](https://github.com/nostr-protocol/nips/commit/a4aea53) 落地。nostr-tools 在 5 月 8 日发布了其 [第一个可浏览器导入的 ESM 构建](https://github.com/nbd-wtf/nostr-tools/commit/dc489bf)。Semisol 在月末起草了 [NIP-15（End Of Stored Events）](https://github.com/nostr-protocol/nips/commit/a787093) 和 [NIP-16（事件 kind 范围）](https://github.com/nostr-protocol/nips/commit/62fde6c)，这些文档仍然管理着 relay 同步语义和常规-vs-可替换-vs-临时的分类。

### 2023 年 5 月

协议规范的爆炸。该月开放了六十四个 NIP PR，其中几个定义了 Nostr 未来两年接口的提案都在 31 天内落地，Nostr 收到的最大资金公告在 5 月 4 日到达，OpenSats 收到 [来自 Jack Dorsey 的 #startsmall 的 1000 万美元资助](https://opensats.org/blog/opensats-receives-additional-funding-of-dollar10m-from-startsmall)，这笔钱资助了此后的每一波 Nostr 资助。NIP-47（Nostr Wallet Connect）在 [5 月 2 日合并](https://github.com/nostr-protocol/nips/pull/406)，将 Alby 的 wallet-connect 规范带入主协议。两天后，Vitor Pamplona [提议 NIP-53 Live Activities](https://github.com/nostr-protocol/nips/pull/498)，具有 `kind:30311` 房间和 `kind:1311` 聊天消息，这是随后每个 Nostr 直播接口的基础。Pablo Fernandez 于 5 月 5 日打开 [NIP-84 Highlights](https://github.com/nostr-protocol/nips/pull/501)，并于 5 月 14 日打开 [NIP-89 Recommended Application Handlers](https://github.com/nostr-protocol/nips/pull/530)。v0l（Kieran Babich，Snort 作者）于 5 月 8 日提议 [NIP-98 HTTP Auth](https://github.com/nostr-protocol/nips/commit/29f26e7)，这是 NIP-96 和 Blossom 后来都依赖的身份验证原语。Jonathan Staab 于 5 月 15 日提议 [NIP-32 Labels](https://github.com/nostr-protocol/nips/pull/532)，[NIP-30 Custom Emoji](https://github.com/nostr-protocol/nips/pull/484) 于同一天合并。Arthur Franca 于 5 月 21 日提议 [NIP-96 HTTP File Storage Integration](https://github.com/nostr-protocol/nips/pull/547)。两天后，Vitor 添加了 [NIP-57 的 zap 分成](https://github.com/nostr-protocol/nips/commit/e4937be)，verbiricha 添加了 [`kind:30024` 长文草稿到 NIP-23](https://github.com/nostr-protocol/nips/commit/0495931)，这个规范成为 Habla、YakiHonne 和 Highlighter 中现代 Nostr 长文创作工作流的基础。fiatjaf 于 5 月 28 日提议 [NIP-29 Simple Groups](https://github.com/nostr-protocol/nips/pull/566)，这是第一个涵盖 `kind:9000` 到 `kind:9020` 审核事件的 relay 管理群组规范。该月以 Paul Miller 于 5 月 31 日打开 [NIP-44 对话](https://github.com/nostr-protocol/nips/pull/574) 结束，这是一个基于 XChaCha20 的加密 DM 设计，旨在取代 NIP-04。client 端也移动得同样快：Damus 在 [5 月 10 日到 5 月 15 日](https://github.com/damus-io/damus/commits/master/?since=2023-05-10&until=2023-05-15) 发布了 NWC、zap pool 和 Pending Zaps；Snort 推出了 [zap pool](https://github.com/v0l/snort/commit/6cbc3ae) 和 [L402 付费媒体](https://github.com/v0l/snort/commit/d5032d6)；[Amethyst](https://github.com/vitorpamplona/amethyst/releases) 全月发布了大约三十个版本发布，从 5 月 1 日的 v0.40.1 到月底的 v0.55.x 范围，v0.45.0 中有 zap 分成，v0.46.0 中有 NIP-32 标签；[Primal Android repo](https://github.com/PrimalHQ/primal-android-app/commit/6654cf9) 于 5 月 16 日创建；[rust-nostr v0.22.0](https://github.com/rust-nostr/nostr/releases/tag/v0.22.0) 添加了 NIP-47 和 NIP-58。5 月 1 日，[strfry 发布了其 negentropy 集成](https://github.com/hoytech/strfry/commit/de475c5)，这是 Doug Hoyte 的集合协调协议的第一个 relay 实现，后来成为 NIP-77。该月以 [Forbes 于 5 月 30 日发布对 fiatjaf 的长文简介](https://www.forbes.com/sites/digital-assets/2023/05/30/bitcoin-social-network-nostr-creator-fiatjaf-/) 结束，这是主流媒体对 Nostr 匿名创始人首批深度报道之一。

### 2024 年 5 月

整合周期。较少花哨的提案，更多发布。[NIP-54 Decentralized Wikis](https://github.com/nostr-protocol/nips/pull/787) 于 5 月 2 日合并，具有 `kind:30818` 文章和大小写规范化的 `d` 标签。三天后，[NIP-56](https://github.com/nostr-protocol/nips/pull/1213) 得到扩展，因此滥用报告可以标记数字威胁（恶意软件、网络钓鱼）与仅内容类别并列。5 月 6 日，[NIP-25 反应被简化](https://github.com/nostr-protocol/nips/pull/1221)，停止将整个回复线程作为 `e` 标签包含。Arthur Franca 于 5 月 12 日 [提议 NIP-22 Comment](https://github.com/nostr-protocol/nips/pull/1233)，引入 `kind:1111`，因此对非 `kind:1` 事件（文章、文件、产品）的回复获得了一种结构化的线程方式。5 月 19 日，fiatjaf [彻底改造 NIP-46](https://github.com/nostr-protocol/nips/pull/1248) 以完全放弃 NIP-04，并将所有 bunker 流量切换到 NIP-44 加密，这是塑造此后每个 bunker 实现的弃用行动。5 月 20 日，[NIP-71 Video Events](https://github.com/nostr-protocol/nips/pull/923) 与 `kind:21` 和 `kind:22` 合并，[NIP-10](https://github.com/nostr-protocol/nips/pull/1171) 在 `e` 标签上添加了可选的 pubkey 参数，因此 client 可以在不先获取被引用事件的情况下解析线程作者。Kieran Walsh 的 [NIP-35 Torrents](https://github.com/nostr-protocol/nips/pull/1175) 于 5 月 22 日合并，5 月 24 日 NIPs README 首次将 [CIP-01](https://github.com/nostr-protocol/nips/pull/1251) 引用为 repo 外提案，标志着"NIP 作为几个提案场所之一"模式的开始。5 月 25 日，一个 [清理 PR](https://github.com/nostr-protocol/nips/pull/1254) 在下游实现冻结之前从 NIP-71 中移除了 `aes-256-gcm` 标签。NIP-96 于 5 月 27 日 [添加了 `list files` 并放弃了转换要求](https://github.com/nostr-protocol/nips/pull/1262)。5 月 28 日，Jonathan Staab 提议 [提高 NIP 接受门槛](https://github.com/nostr-protocol/nips/pull/1264)，要求在草案能够毕业之前至少有两个互操作实现。client 端：Damus 在 5 月 9 日至 10 日标记 [v1.7.2](https://github.com/damus-io/damus/releases/tag/v1.7.2) 和 [v1.8](https://github.com/damus-io/damus/releases/tag/v1.8) 以及 [具有完整 NIP-10 标记处理的 v1.9](https://github.com/damus-io/damus/commits/v1.9)，落地了 [推送通知的 NIP-98 身份验证](https://github.com/damus-io/damus/commit/8feb228)，并发布了完整的 [NIP-10 标记支持](https://github.com/damus-io/damus/commit/52aefc8)。Amethyst 于 5 月 14 日将 [NIP-17 作为默认 DM 模式](https://github.com/vitorpamplona/amethyst/commit/1f45a63)，构建了 [NIP-65 outbox 模型 relay 管理](https://github.com/vitorpamplona/amethyst/commit/aa97c7e)，添加了 [NIP-96 服务器选择](https://github.com/vitorpamplona/amethyst/commit/ff94f45)，并发布了 [NIP-06 BIP-32/BIP-39 密钥派生](https://github.com/vitorpamplona/amethyst/commit/04c4490)。Primal Android [0.99.2](https://github.com/PrimalHQ/primal-android-app/releases/tag/0.99.2) 于 5 月 10 日添加了用户标记和外部钱包 NWC，随后是 [0.99.4](https://github.com/PrimalHQ/primal-android-app/releases/tag/0.99.4)。Pablo Fernandez 在 5 月 24 日至 31 日落地了一个 [NDK 乐观更新集群](https://github.com/nostr-dev-kit/ndk/commits/master/?since=2024-05-01&until=2024-06-01)。Snort 添加了 [NIP-96 服务器选择](https://github.com/v0l/snort/commit/5763d91)，cashu-ts [将其加密原语分离](https://github.com/cashubtc/cashu-ts/commit/3e20f45) 到 `@cashu/crypto`。

### 2025 年 5 月

[NIP-77（Negentropy Syncing）](https://github.com/nostr-protocol/nips/pull/1494) 于 5 月 27 日合并的月份，这是 fiatjaf 和 Doug Hoyte 的规范，用于取代暴力 REQ 过滤器的对数成本差异计算的线协议。这与 strfry 两年前作为 relay 端功能发布的 negentropy 相同，现在正式确定为 client-relay 协议，[README 条目](https://github.com/nostr-protocol/nips/pull/1939) 于同一天落地。前一周，[NIP-23 长文](https://github.com/nostr-protocol/nips/pull/1897) 于 5 月 24 日定义了 HTML 文档如何通过 `<link>` 标签将自己与 Nostr 实体关联，这是规范化 Web 副本原语。NIP-25 于 5 月 22 日添加了 [反应目标 relay 提示](https://github.com/nostr-protocol/nips/pull/1702)，并 [放弃了 emoji 到 like/dislike 的推荐](https://github.com/nostr-protocol/nips/pull/1486)，将 emoji 视为不同的语义单元。NIP-52 于 5 月 14 日 [简化](https://github.com/nostr-protocol/nips/pull/1922)，专注于 client 在生产中发布的 kind，这次修剪使一年后的 Formstr 日历扩展更容易嫁接。5 月 9 日，[Follow Packs](https://github.com/nostr-protocol/nips/commit/873afc5fb823f58c3b7f29c5090f9c56172623f2)（kind 39089 策展的关注列表）和 [Favorite Relays](https://github.com/nostr-protocol/nips/pull/1848)（NIP-51 下的一个新可替换列表）于同一天进入 README。Marmot 协议弧尚未开始：只有 [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) repo 存在（第一次 commit 在 2024 年 9 月 9 日），2025 年 5 月是其 Svelte+Tauri 原型阶段，[5 月 14 日 commit](https://github.com/marmot-protocol/whitenoise-rs/commit/b8e6754) 移除了 Tauri 特定的代码，因为项目转向了其当前架构。专用的 MDK Rust 核心（2025 年 9 月 12 日）、Marmot 规范 repo（2025 年 9 月 19 日）和 Flutter UI（2025 年 12 月 2 日）都在当年晚些时候到来。在 client 端，Damus 的 [Notedeck v0.4.0](https://github.com/damus-io/notedeck/releases/tag/v0.4.0) 于 5 月 5 日作为第一个 Beta 发布，从 Alpha 毕业，具有全文搜索、Dave AI 助手、通过 NWC 的 zaps、GIF、用户标记和静音列表。两天后，hodlbod 的 [Flotilla 1.0.0](https://github.com/coracle-social/flotilla/releases/tag/1.0.0) 作为基于 NIP-29 的群组聊天 client 越过公开发布边界，与 [Coracle 0.6.12](https://github.com/coracle-social/coracle/releases/tag/0.6.12) 并列，这是六个 Coracle 版本中的第一个，一直运行到 [5 月 14 日的 0.6.17](https://github.com/coracle-social/coracle/releases/tag/0.6.17)。5 月 12 日的 [Amber v3.4.0](https://github.com/greenart7c3/Amber/releases/tag/v3.4.0) 摆脱了已弃用的 Android Autofill 和 ClipboardManager API，并从加密的共享首选项迁移到 DataStore。Primal Android 于 5 月 20 日发布的 [2.2.20](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.2.20) 添加了 Primal Premium 的 Redeem Code 流程和重新设计的图库。5 月 21 日的 [nak v0.14.0](https://github.com/fiatjaf/nak/releases/tag/v0.14.0) 在与 Coracle、Flotilla 和 Notedeck 版本相同的一周中削减了规范 CLI 的一个小版本。当 [Reynolds Foundation 于 5 月 22 日捐赠 200 万美元](https://opensats.org/blog/opensats-receives-two-million-donation-from-the-reynolds-foundation) 时，OpenSats 收到了迄今为止最大的非 Bitcoin 财库捐款。

### 2026 年 5 月

由 [Newsletter #21](/zh/newsletters/2026-05-06-newsletter/)、[#22](/zh/newsletters/2026-05-13-newsletter/)、[#23](/zh/newsletters/2026-05-21-newsletter/) 和本期涵盖的月份。定义性的主线是 MLS-on-Nostr 达到多 client 生产：[MDK 0.8.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.8.0) 发布了 MIP-05 叶索引原语和可寻址 key packages，其后是 [PR #306](https://github.com/marmot-protocol/mdk/pull/306) 通过共享的 UniFFI 接口在 iOS 和 Android 上添加 NIP-40 消失消息验证。[White Noise v2026.5.22+25](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.5.22%2B25) 通过一个 Notification Service Extension 发布了 iOS 推送，该扩展在扩展进程内解密 MLS 密文，因此 broker 从不看到明文，两个新的 Marmot client 出现：[Scramble](https://github.com/DavidGershony/Scramble)（一个 .NET/Avalonia 桌面和 Android client，具有多设备 KeyPackage 插槽）和 [Cordn](https://cordn.net)（一个使用 ContextVM 之上每群组协调者的替代 MLS 架构）。Angor 在 [PR #860](https://github.com/block-core/angor/pull/860) 中将其加密消息从 NIP-04 迁移到 NIP-44，关闭了以 [Paul Miller 于 2023 年 5 月的 NIP-44 提案](https://github.com/nostr-protocol/nips/pull/574) 开启的弃用弧。Formstr 团队于 5 月 17 日打开了近期记忆中最大的协调 NIP 提交，[PR #2350](https://github.com/nostr-protocol/nips/pull/2350) 用于参与者自我移除，[PR #2351](https://github.com/nostr-protocol/nips/pull/2351) 用于私密日历事件和循环（NIP-52E 和 NIP-52R），[PR #2352](https://github.com/nostr-protocol/nips/pull/2352) 用于去中心化预约调度，全部与 [calendar.formstr.app](https://calendar.formstr.app) 已经发布的参考实现一起。[Amethyst v1.11.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.11.0) 将 NIP-52 日历渲染为一流的时间线类别，并将链上 Bitcoin zaps 扩展到分成分发。[NIP-77 于 2025 年 5 月合并](https://github.com/nostr-protocol/nips/pull/1494) 一年后，三个独立的实现在同一窗口内发布了 negentropy 采用：[Notedeck PR #1459](https://github.com/damus-io/notedeck/pull/1459) 将其接入 Damus 的桌面 client 用于 giftwrap 和线程回填，[Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) 使用完整 negentropy MLS 同步作为其从零开始的 `vector-core` 重写的一部分，还有一键 Tor 和 21 工具 MCP agent 接口，[Citrine v3.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0-pre1) 将其添加到 Android 原生 relay，还有内置 Tor 和多 relay 聚合。[Mostro v0.17.4](https://github.com/MostroP2P/mostro/releases/tag/v0.17.4) 通过 [PR #738](https://github.com/MostroP2P/mostro/pull/738) 中的第 3 阶段削减保证金支付关闭了反滥用保证金循环，执行了协议此前仅威胁的内容。从"我们应该替换 NIP-04 吗"到"我们应该用完整的 MLS 群组状态替换 NIP-44 吗"三年。

---

如果你想讨论，请在 Nostr 上私信我们。
