---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "后量子身份工具、更强的加密消息与签名、可移植的社区设置,以及横跨 NIPs 与 Concord 的协议工作。"
---

欢迎回到 [Nostr Compass](https://nostrcompass.org),您的 Nostr 每周指南。

**本周:** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) 在现有 Nostr 身份旁添加后量子密钥和可选的保护消息。[Divine](https://github.com/divinevideo/divine-mobile) 收紧账户隔离、私信验证和发布确认;[MDK](https://github.com/marmot-protocol/mdk) 加强加密群组收敛与恢复;[Amber](https://github.com/greenart7c3/Amber) 使分组签名决策变得明确。版本发布改进了钱包连接、加密聊天、社交发现、设备同步和远程签名,协议工作涵盖身份与加密社区。深度解析将解释经身份验证的删除请求和去中心化举报。

## 头条新闻

### nostr-wot-extension 0.4.0 在 Nostr 身份旁添加后量子密钥

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) 是一款用于管理 Nostr 身份和签名的浏览器扩展。从 24 词 seed 创建的账户现在可以在现有 Nostr 密钥旁派生 ML-KEM-1024 加密密钥和 ML-DSA-87 签名密钥。一键流程发布 kind `10203` 证明,将 Nostr 公钥绑定到两个后量子公钥,并包含 ML-DSA 占有证明。从 12 词助记词、裸 `nsec`、远程签名器或只读密钥导入的账户无法使用该派生流程,扩展会在账户视图中说明这一限制。

该版本还添加了可选的后量子私信。它通过 HKDF 将 ML-KEM 共享密钥与现有的 [NIP-44 encrypted-message conversation key](https://github.com/nostr-protocol/nips/blob/master/44.md) 结合,并保留正常的 NIP-59 元数据隐藏 gift-wrap 层用于中继投递。收件人选择加入后,加密绝不会静默回退,而解密会自动选择适当路径。这可以保护新消息路径免受日后恢复当前 Nostr 私钥的影响,但不会替换 secp256k1 事件签名;该版本明确将更大规模的迁移留给未来与中继和客户端的协调。

### Divine Mobile 1.0.19 收紧账户、私信和发布

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) 是一款通过 Nostr 发布和检索视频的移动短视频客户端。其账户切换器现在围绕账户作用域容器构建每个已登录身份,发布修复可防止视频在错误账户下发送。中继发布路径现在等待带有明确成功语义的 `OK` 响应,而中继 `CLOSED` 帧可以终止其自身的待处理查询,而不是让请求挂起。

[私信处理](https://github.com/divinevideo/divine-mobile/pull/6368) 拒绝未认证的 rumor 字段和未签名的 seal,恢复四种缺失消息情况,并将完全关注参与者的群组对话路由到收件箱。该版本在更新列表时还会保留可寻址视频事件的标签,并消费观察到的删除请求,使已移除视频从本地状态中消失。这些更改延续了上周涵盖的按中继查询超时工作,但将焦点从检索隔离转向身份边界、消息验证和发布确认。

### MDK 0.9.11 强化 Marmot 群组收敛与恢复

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) 是 Marmot 的 Rust 开发工具包,Marmot 是一种通过 Nostr 承载的加密群组消息协议。该版本围绕群组状态机构建更大的收敛与恢复系统:过时的收敛轮次在当前群组 tip 处重新打开,入站 capability 投影原子提交,延迟消息在重启间获得有界生命周期,commit 寻址检查点帮助恢复身份自身的 commit 分叉。非稳定发送可以排队并恢复,而 epoch-stall 路径会升级到 backfill,已发送消息在收敛工作中得以保留。

[存储与宿主集成](https://github.com/marmot-protocol/mdk/pull/1201) 获得并行强化。MDK 安全删除已修剪的 SQLite 投影,清零导入的私钥、NIP-49 encrypted-key 导出中间体和 OpenMLS 序列化缓冲区,并从调试输出中编辑群组图像密钥。账户导入可在中断后恢复,iOS 和 Android 私有存储路径已修复,宿主可在挂起前显式关闭存储。新的轻量级 roster 和本地成员投影减少了应用必须读取的内容,而 Hermes 连接器可以将多个 agent 生成的图像作为一张 Marmot 相册投递。

### Nostria 4.1.67 扩展加密社区管理

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) 是一款用于 Nostr 的 Web 和桌面社交客户端。它在 4.1.53 引入的实验性 NIP-29 中继管理群组和 Concord 加密社区基础上,增加了社区解散、图标和横幅管理、带压缩预览的加密照片上传、完整反应选择器,以及双窗格布局——在用户阅读笔记或文章时保持社区打开。该版本还添加了线程消息以及公开、群组和私聊的组合中心。

### Amber 6.4.0 使每个分组签名决策都明确

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) 是一款 Android 签名器,将 Nostr 私钥与请求签名的应用分离。重新设计的多请求屏幕为每个请求和每个分组提供 Approve 和 Deny 控件,取代先前的选择并确认流程。通过 Amber 中继介导 bunker 接口发送的被拒绝请求现在会收到正确的错误响应,因此请求客户端可以区分拒绝与签名器停滞。

[Amber 的 tagged source](https://github.com/greenart7c3/Amber/tree/v6.4.0) 还在每个已发布语言环境中为另外 113 种 event kind 添加本地化、人类可读标签。新增内容包括 Concord 群组事件、NIP-51 Git 仓库书签和 NIP-53 room-presence 事件,在用户批准签名前为不熟悉的数据提供更多上下文。并发 map 守卫还修复了可能导致 `NegativeArraySizeException` 的中继订阅崩溃。

### Safebox Acorn 将可移植恢复组件与 Web 应用分离

[Safebox Acorn](https://github.com/trbouma/safebox-acorn) 是一个独立的 Python 组件和命令行界面,用于通过 Nostr 支持的状态保护用户控制的密钥、资金和记录。将 Acorn 从更广泛的 Safebox Web 应用中抽出,让另一个 Python 项目可以安装运行时并使用其密钥、Nostr 个人资料、中继、记录、Cashu、Lightning 和加密辅助工具,而无需承担 Web 界面。其当前的记录保护原语可以生成新的 256 位密钥,从单独提供的熵派生一个,并将精确密钥编码为带校验的 24 词恢复短语。

项目的 [recovery and continuity guide](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) 将 Acorn 定位为家庭或社区 Safebox 内可替换的协议组件。该设计通过本地中继和独立副本保持加密状态可用,因此恢复不依赖单一设备、应用、中继、mint 或服务提供商。文档对当前边界保持谨慎:受保护记录加密仍在设计中,因此在实现并审查该配置文件之前,应用不应让记录依赖新的记录保护密钥。


## 打标签的发布

### Mostro Core 0.14.2 更改加密聊天信封

[Mostro Core](https://github.com/MostroP2P/mostro-core) 是 Mostro 交换守护进程及其客户端使用的共享类型和点对点函数的 Rust 库。[版本 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) 用 kind 14 信封替换 gift-wrapped 聊天消息,该信封从对等方共享密钥派生独立的 conversation-encryption 和 signing keys。新读取器验证作者、签名、收件人、时间戳和内容大小,而 legacy gift-wrap 辅助工具仍可用,以便客户端在迁移期间读取两种格式。

### Mostro 0.18.1 启动 Cashu 托管路径并强化守护进程

[Mostro](https://github.com/MostroP2P/mostro) 是通过 Nostr 协调订单的点对点 Lightning 交换守护进程。[版本 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1) 为 Cashu 托管后端奠定基础,包括配置、数据库辅助工具、mint 集成、启动接线和首个 lock 操作。它还可以使用受信任节点通过 Nostr 公布的价格,并在其可替换 info 事件中宣传首次联系的 proof-of-work 要求。该版本更新 Nostr 依赖以修复 NIP-44 拒绝服务问题,从 restore-session 日志中移除私钥,拒绝未授权的合作取消消息,强化 LNURL 获取以防范服务端请求伪造和挂起,验证 payout invoice,并在重启后恢复 hold-invoice 订阅。

### LaWallet NWC 2.3.0 添加 Nostr 通知和 zap 收据

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) 是一个开源 Lightning Address 平台,通过 [Nostr Wallet Connect](/zh/topics/nip-47/) 连接钱包。[版本 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) 允许每个钱包将收到和转发的通知作为可配置的 Nostr 事件发送,包括收件人 `p` 标签、选定中继、模板化内容和可选 [NIP-44](/zh/topics/nip-44/) 加密;重试复用同一已签名 event ID。它还接受 zap 请求并在结算后发布已签名的 [NIP-57](/zh/topics/nip-57/) kind 9735 收据,而新的地址能力视图显示解析后的地址是否支持 NIP-05、NIP-57 及相关 Lightning Address 协议。

### nostr-double-ratchet TypeScript 0.0.166 将公开邀请绑定到 session keys

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) 提供通过 Nostr 中继进行端到端加密直接和群组消息的 TypeScript 和 Rust 原语。[TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) 要求邀请响应证明其 session key 的所有权,防止可复用的公开邀请将一种 Nostr 身份绑定到另一方的 session。该版本还拒绝格式错误的 rumor 字段并收紧 payload 验证;现有 session 继续工作,但更新后的邀请方会拒绝来自旧受邀者的无证明响应。

### cln-nip47 0.2.0 扩展并隔离 NWC 请求

[cln-nip47](https://github.com/daywalker90/cln-nip47) 是一个 Core Lightning 插件,通过 [Nostr Wallet Connect](/zh/topics/nip-47/) 向钱包暴露节点。[版本 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) 添加 NWC 方法以创建、取消和结算 hold invoice,以及 `hold_invoice_accepted` 通知,并宣传连接节点实际支持的方法集。交易列表响应现在在 500 条和约 128 kB 处停止,request 事件按 event ID 去重,一个客户端的失败通知不再阻止向其他客户端投递。该版本还移除不再属于 NWC 规范的两个 multi-payment 方法。

### ClipRelay 0.1.3 在空闲期后恢复中继和签名器连接

[ClipRelay](https://github.com/tajava2006/cliprelay) 通过 Nostr 中继在设备间同步用户剪贴板,并使用 [NIP-44](/zh/topics/nip-44/) 将内容加密给同一身份。配套的 [desktop](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) 和 [Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3 版本添加文本框,可将输入文本直接发送到另一设备的剪贴板。它们还在空闲期后通过真实中继往返测试活性,从重新订阅升级到 socket 替换和重建连接池,而停滞的 [NIP-46](/zh/topics/nip-46/) 签名器调用现在会超时并自动重建。

### NoorNote 1.3.2 将文章发现移入社交图谱

[NoorNote](https://github.com/77elements/noornote) 是一款用于社交帖子、加密消息、长文和其他 event types 的 Nostr 客户端,覆盖 Web、桌面和 Android。[版本 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) 用来自一、二、三度联系人的发现替换其扁平全局文章 feed,为读者提供根植于关注图谱的文章时间线。它还将来自未知发送者的重放私信突发合并为一条滚动通知,而不是在中继历史到达时产生一堆 toast。

### Bray 2.4.0 添加紧凑远程签名方言

[Bray](https://github.com/forgesworn/bray) 是一个 Nostr MCP 服务器,为软件 agent 和用户提供中继访问、身份、发布和远程签名工具。[版本 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) 接受 event 为对象的签名请求,以及 [NIP-46](/zh/topics/nip-46/) 使用的字符串化形式,并添加 `sign_event_compact`,仅返回 event ID、签名、公钥和时间戳。更小的请求和响应格式降低受限硬件签名器的内存使用,而标准 `sign_event` 流程保持不变,两种方言都会对收到事件的 ID 生成签名。


## 新发现

### Pact 将相互同意的 agent bonds 引入 Nostr

[Pact](https://github.com/bobodread876/pact) 是本周新发现的项目,是基于 MATE.md 和 draft NIP-BD 传输的早期关系层,面向软件 agent。其已签名、相互同意的 bonds 由 agent 自身密钥持有,可通过 Nostr 发布,而 private bonds 使用 [NIP-59](/zh/topics/nip-59/) gift wrapping。monorepo 包含 MCP 服务器、TypeScript SDK、命令行客户端、可自托管守护进程和 Web 界面。其最新仓库活动早于本期周刊窗口,因此这是发现说明,而非新发布的声明。


## 开发中

### nostrord 在设备间同步群组静音

[nostrord](https://github.com/nostrord/nostrord) 是一款面向中继管理社区的跨平台客户端。[PR #250](https://github.com/nostrord/nostrord/pull/250) 将每个账户的按群组静音选择存储在自加密 [NIP-78](/zh/topics/nip-78/) (application-specific data) kind `30078` 事件中,因此在一台设备上的设置可以跟随用户到另一台,而无需向中继暴露群组列表。可替换记录使用 newest-event ordering,监听实时变更,并在签名或发布失败时回滚界面,而不是让本地状态不同步。已静音群组不再计入可见未读总数,但保留未读位置供下次访问。

### Amethyst 完成 Concord 邀请生命周期

[Amethyst](https://github.com/vitorpamplona/amethyst) 是一款 Android Nostr 客户端,其加密社区支持实现了 Concord 协议。[PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) 让邀请链接在社区 refounding 后仍能存活,在同一可寻址坐标重新签发 bundle,而 ban 检查防止被移除成员使用该恢复路径。它还在 app 和 `amy` 命令行客户端上实现加密 CORD-05 邀请列表,添加按链接 revocation tombstones,并在删除唯一存储的可使链接退役的 signing key 之前要求中继确认。同一工作为 `amy` 提供 control-key delivery、refounding、rekeying 和 stranded-member recovery 路径,以跟随后续社区 epoch。

### Buzz 在桌面和移动端携带各社区外观

[Buzz](https://github.com/block/buzz) 是一个基于 Nostr 的社区工作区,拥有桌面和移动客户端。已合并的桌面 [PR #3653](https://github.com/block/buzz/pull/3653) 和移动 [PR #3767](https://github.com/block/buzz/pull/3767) 将每个社区的主题、强调色和 system-mode 选择存储为该社区中继上的加密 NIP-78 记录。两个客户端共享相同 versioned payload 并保持身份作用域本地缓存,因此在 relay 不可用时切换社区或账户不会应用错误外观。replacement ordering、guarded writes 和连接关闭后的重新订阅让两个客户端在重连后再次收敛。

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) 在 issue cutoff 前跟进,进行性能与可靠性改进。它移除 0.5.9 之后引入的回归,加速频道加载,限制初始时间线保留,合并 read-state persistence,保留新鲜频道时间线,并防止 relay ingest worker 因对 project events 的反应而崩溃。它还添加将线程消息发送到频道,并将桌面搜索限定在预期范围。


## 协议与规范工作

### NIPs

[NIPs PR #2435](https://github.com/nostr-protocol/nips/pull/2435) 是对 NIP-34 的开放修订,NIP-34 通过 Nostr 事件标准化 git 仓库协作。它为 pull-request 事件添加可选 `b` 标签,使作者可以指定仓库 default 以外的 target branch。该提案与 ngit 和 GitWorkshop 中已实现的支持一致,但尚未进入规范。

[NIPs PR #2434](https://github.com/nostr-protocol/nips/pull/2434) 是关于后量子身份密钥的开放提案。它从 NIP-06 mnemonic key-derivation seed 在现有 secp256k1 密钥旁派生后量子加密和签名密钥,然后用 kind `10203` 证明将公钥绑定到 Nostr 身份。草案将其主张限制为保护 secp256k1 日后被破解时早期消息的机密性;它不会替换当前的事件签名。

[NIPs PR #2431](https://github.com/nostr-protocol/nips/pull/2431) 是针对浏览器签名器的开放 NIP-07 修订。客户端可以在签名或加密请求中附加其期望的公钥,要求签名器使用该账户或拒绝调用。这将防止用户在签名器中切换账户后,页面仍在另一身份下静默继续。

[NIPs PR #1813](https://github.com/nostr-protocol/nips/pull/1813) 在窗口期内经过实质性工作后,仍是开放 double-ratchet 提案。它规范了 forward-secret 加密对话,其密钥随消息推进,实现已在 nostr-double-ratchet 库和 Iris 中可用。它仍是草案,而非已合并 NIP。

[NIPs PR #2433](https://github.com/nostr-protocol/nips/pull/2433) 在窗口期内打开并在未合并的情况下关闭。它提议澄清 NIP-42 中继错误,使 `auth-required` 表示进一步认证可能改变结果,而 `restricted` 表示不能。该区分针对已为一种密钥认证但仍缺少另一种授权的连接;closed 状态意味着措辞未进入规范。

[NIPs PR #2378](https://github.com/nostr-protocol/nips/pull/2378) 此前在仍为提案时被报道,现已关闭且未合并。其提议的 agent passports、discovery、task、marketplace、invoice 和 connection events 因此仍不在 NIP 集合中。

[NIPs commit 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) 合并了对 NIP-29 的纯文档修正。它为群组 metadata 示例添加 `previous` 标签,展示 replacement event 如何标识其取代的事件。这澄清示例,不引入新协议功能。

### Concord 和 CORDs

[CORD PR #18](https://github.com/concord-protocol/concord/pull/18) 将把加密 Community Lists 分片到 kind `33302` 事件,移除 50 成员上限,并修剪已退役条目以符合中继限制。另外两个开放提案添加 [private mention locators](https://github.com/concord-protocol/concord/pull/16) 和 [pause signal](https://github.com/concord-protocol/concord/pull/17),在不丢弃消息的情况下暂停聊天。

[CORD-02 PR #15](https://github.com/concord-protocol/concord/pull/15) 于 8 月 6 日合并,并将写入限制在社区 control plane。owners 和 staff 持有新的 `control_root` signing secret,而所有成员保留验证和解密 moderation state 所需的派生公钥和 read key。write key 是垃圾信息屏障,不是建立 authority 的内部 actor signatures 和 roster checks 的替代。

[CORD PR #12](https://github.com/concord-protocol/concord/pull/12) 此前作为开放 draft 被报道,现已关闭且未合并。其 control-plane 部分被上文更窄的已合并 CORD-02 修订取代,而 restricted-write channels 和其他 draft 材料未进入规范。

## NIP 深度解析

### Event Deletion Requests (NIP-09)

[NIP-09](/zh/topics/nip-09/),由 [primary specification](https://github.com/nostr-protocol/nips/blob/master/09.md) 定义,为事件作者提供一种签名方式,请求中继和客户端停止提供该作者的一个或多个事件。它不会擦除每一份副本。它通过分发原始事件的同一中继网络传递作者意图。

请求是普通已签名的 kind `5` 事件。其 tags 包含一个或多个指向特定 event ID 的 `e` 引用,或指向可寻址 event 坐标的 `a` 引用,[NIP-09 tag rules](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) 要求为每个被引用 event kind 包含 `k` 标签。可选 `content` 可说明原因。对于 `a` 引用,中继应移除该坐标上 timestamp 不晚于请求 `created_at` 的每个版本,防止旧删除请求压制较新的 replacement。

[Authorship is the security boundary](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior)。仅当被引用事件的 `pubkey` 与删除请求的 `pubkey` 匹配时,中继才应停止发布该事件,客户端在隐藏事件前必须执行该检查。中继可能不持有被引用事件,因此在接受请求时可能无法验证关系,客户端不能将中继接受视为删除已获授权的证明。规范还要求中继保留 kind `5` 请求,因为另一客户端可能已持有原始事件并在稍后遇到该请求。

以下是一个 [signed kind `5` event](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943):

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

删除仍是协作策略,而非撤销已签名对象。中继、缓存、截图或离线客户端可以保留原始字节,删除 kind `5` 请求本身也不会撤销它。客户端可以隐藏目标、标记为 disowned 或显示请求原因,但应告知用户无法保证普遍删除。这与 [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) 不同,后者通过 `expiration` 标签请求中继在发布时选定的时间后停止存储事件。NIP-09 处理作者稍后的决定,并可指向已分发的事件。

当前实现在不同层应用该策略。[Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623) 从客户端 event store 移除已删除视频,[strfry PR #251](https://github.com/hoytech/strfry/pull/251) 将有效删除请求扩展到 gift-wrap 收件人,[Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) 在其客户端中声明 NIP-09 支持。[nostrord's group client](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) 提供另一条当前实现路径。

### Reporting (NIP-56)

[NIP-56](/zh/topics/nip-56/),由 [primary specification](https://github.com/nostr-protocol/nips/blob/master/56.md) 定义,标准化关于账户、事件或被引用 blob 的签名举报。它将举报信号与 moderation 决策分离,使每个客户端或中继可以选择信任哪些 reporter 以及何种响应符合其策略。

举报使用 kind `1984`,必须在 `p` 标签中标识被举报账户。举报 note 还需要 event ID 的 `e` 标签。标签的第三个值携带指定类别之一:`nudity`、`malware`、`profanity`、`illegal`、`spam`、`impersonation` 或 `other`。关于 blob 的举报可以在 `x` 标签中使用其 hash,在 `e` 标签中使用引用该 blob 的事件,并可选使用 `server` 标签表示位置。来自 [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) 的可选 `L` 和 `l` 标签可以在固定类别列表不够精确时添加 namespaced label。

[The event proves only that one key made an allegation](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting)。被举报内容不会因存在有效 kind `1984` 而变为虚假、非法或可移除,开放中继也不能安全地将匿名举报计为投票。规范建议不要自动进行中继 moderation,因为举报容易被操纵,但允许中继管理员对其已信任的 moderator 的举报采取行动。客户端也可通过用户社交图谱对举报加权,例如在多个可信联系人标记同一账户后模糊内容。

以下是一个 [signed kind `1984` event](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2):

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 and NIP-09 solve different problems](https://github.com/nostr-protocol/nips/tree/master)。kind `1984` 举报可以针对他人的账户或事件,但不授予删除权限。kind `5` 请求表达原始作者意图,且仅对该作者自身事件有效。两者都不保证移除:NIP-56 有意将行动委托给本地 moderation 策略,而 NIP-09 依赖中继和客户端 honoring 经身份验证的请求。

实现在不同产品中暴露这些选择。[Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) 修正短视频客户端中的举报投递,[Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) 将举报作为 marketplace 参与者的有界 context 读取,[nostrord's NIP-56 module](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) 发布并处理举报事件。[Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) 也列出当前 NIP-56 支持。


---

发送 NIP-17 DM,通过 [Nostr Compass project](https://github.com/andotherstuff/nostr-compass) 分享项目或新闻。
