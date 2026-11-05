---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

本周，[Amethyst](/zh/newsletters/2026-11-04-newsletter/#amethyst) 推出了内联 napplets，并纳入了[嵌入安全审查](https://github.com/vitorpamplona/amethyst/pull/4710)提出的修复；[Napplets](/zh/newsletters/2026-11-04-newsletter/#napplets---web-packages) 将 applet 身份绑定到每个文档各自的端口；[Marmot 的 mdk](/zh/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk) 的 nightly 版本收紧了群组消息机制。此外，中继、钱包、签名库和新应用也有变化，其中大部分是已合并但尚未发布的源码。

## 头条新闻 {#top-stories}

### Amethyst {#amethyst}

Android 客户端 Amethyst 发布了 [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0)，可在 Android 11+ 和桌面端的笔记中内联运行 napplets。[嵌入安全审查](https://github.com/vitorpamplona/amethyst/pull/4710)带来的修复封堵了一条路径：此前任何拥有中继访问权限的 napplet 都能读取已解密的私信。现在解密需要用户单独授权，`nostr.signEvent` 需要签名器权限，而桌面端 Chromium 渲染器仍未启用沙箱。一项[按文件区分的附件加密变更](https://github.com/vitorpamplona/amethyst/pull/4701)为每个 [NIP-17](/zh/topics/nip-17/) 私密私信附件生成全新的 AES-GCM 密钥和 nonce，而此前多文件批次会同时复用这两者。上游的风险描述来自代码分析，并未复现漏洞利用，已发送的文件也不会得到修复。

### Marmot Protocol (mdk) {#marmot-protocol-mdk}

mdk 是 Marmot 基于 MLS、面向 Nostr 的加密消息工具包，发布了仅供测试的 nightly 预发布版本，该系列没有稳定版本。在 11 月 2 日的 nightly 中，群组内[新的发送会排在更早的排队消息之后](https://github.com/marmot-protocol/mdk/pull/2849)，从而为正在追赶历史记录的成员保持加密代次的顺序，但这并不能保证消息不丢失。一项已合并、默认关闭的[丢失 Welcome 修复](https://github.com/marmot-protocol/mdk/pull/2936)遵循 [Marmot 心跳规则](https://github.com/marmot-protocol/marmot/pull/497)：一旦目标的心跳显示其在最近一次载体发布之后至少十分钟仍有活动，就会重新发送完全相同的已保留 Welcome。心跳频率或时钟滞后可能使修复延迟一小时或更久，且完成时间没有上限。[设备关联命令](https://github.com/marmot-protocol/mdk/pull/2922)仍受默认关闭的 dev-device-groups 功能控制，在生产环境中处于关闭状态。

### Napplets - Web 软件包 {#napplets---web-packages}

Napplets 是用于沙箱化 Nostr applet 的 Web 软件包，发布了 [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0)、[nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0) 和 [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0)，这些版本[将 applet 身份绑定到每个文档各自的 MessagePort](https://github.com/napplet/web/pull/302)。经过验证的 (dTag, artifactHash) 身份与所创建 iframe 在 hello 中传递的端口绑定，所有 NAP 流量都使用该端口。通过导航加载的文档不会获得任何授权。仍在使用 Window 消息机制的宿主（shell）必须升级，因为不存在兼容路径。后续源码通过 frame-src 'none' [将预览框架锁定到其经过验证的文档](https://github.com/napplet/web/pull/305)。

## 版本发布 {#tagged-releases}

### Marble {#marble}

Marble 是一款基于 Cosign 门限签名构建的测试版客户端，在 [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23) 中可以将中继作为信息流阅读。通过地址打开的中继会先显示其自身的描述，再按从新到旧的顺序显示其帖子。收藏的中继保存在 kind 10012 列表中，中继分组保存在 kind 30002 集合中，与 Jumble 使用的列表相同。该版本还重做了回应功能，提供最近回应托盘以及用户自己的自定义表情。

### Sidecar {#sidecar}

Sidecar 是一款用于发布笔记和网页高亮的浏览器扩展，在 [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6) 中可以从中继删除其钱包备份。经确认后，它会用空副本替换加密副本，并请求中继忘记该备份，已连接的钱包保持不变。中继并不保证会删除备份。自 [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5) 起，Sidecar 会在上传前移除 JPEG 中的 EXIF、XMP 和 IPTC 元数据，其[上传准备变更](https://github.com/dmnyc/sidecar/pull/572)会阻止任何无法清理的 JPEG。

### Haps {#haps}

Haps 以 Nostr 密钥发布和安装原生软件包。[Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25) 提供 macOS、Linux 和 Windows 安装包，附带通过校验和固定的 htree 辅助程序，以及覆盖所有归档文件的 SHA256SUMS 文件。0.1.24 的源码依据 Hashtree 规范草案[写入带版本的 Hashtree 引用](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8)。Haps 0.1.23 及更早版本若既没有旧版过渡目录，也没有升级后的安装程序或 Cargo 构建，就无法读取新目录。

### Cosign {#cosign}

Cosign 是 Marble 测试版背后的门限签名库，在 [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9) 中发布了针对加入流程的部分修复：通过扫描的邀请者加入时，现在需要该邀请者的贡献，以及来自至少两个不同发送者的分片。手机对手机的加入仍未绑定，因此攻击者持有两个密钥依然足够，且空的解密部分仍会跳过证明验证。在 [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8) 中，写入成员列表的服务器仍可选择秘密已知的份额点。手机只能通过 Marble 版本获得修复。

### nostream {#nostream}

nostream 是一个以 PostgreSQL 为后端的 TypeScript 中继，在 [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0) 中新增了[出站对等同步](https://github.com/cameri/nostream/pull/1043)。该 worker 读取每个对等节点的 [NIP-11](/zh/topics/nip-11/) 中继信息范围，使用 [NIP-42](/zh/topics/nip-42/) 客户端认证进行身份验证，并通过 [NIP-77](/zh/topics/nip-77/) negentropy 同步进行协调，同时按 ID、签名和范围检查获取到的事件。[对等节点专属限制](https://github.com/cameri/nostream/pull/1034)仅在已配置的对等节点完成 AUTH 后生效。源码发布并不能证明任何中继已部署该版本。

### diVine {#divine}

diVine 是一款短视频循环播放客户端，发布了[稳定版 Android 1.0.27](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27)，带有可交互的公开视频贴纸；iOS 和 macOS 版本是否可用尚未确认。一项已合并的[窗口下方重新查询](https://github.com/divinevideo/divine-mobile/pull/10711)仅在初始历史恢复完成后运行，以每个中继每页 100 条消息的方式读取 gift wrap、[NIP-04](/zh/topics/nip-04/) 已弃用的加密私信以及删除事件。它独立遍历每个中继，而现有的历史排空流程共用一个游标，可能跳过已达上限的中继中较早的历史。其覆盖范围有限，无法恢复完整历史。

### Whistle {#whistle}

Whistle 是一款移动端群组位置共享与聊天应用，发布了 [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1)，这是其首个基于 Marmot 协议 v2 的公开版本。现有群组无法迁移，因此必须重新创建群组，且每位成员都必须更新，npub 身份则会保留。扫码加入取代了邀请码和邀请链接。已知问题是离线时发送的聊天消息可能延迟送达或根本无法送达，该版本将其归因于 MarmotKit；位置共享不受影响。

## 开发进展 {#in-development}

### Quartz {#quartz}

Quartz 是一个 Kotlin Multiplatform Nostr 库，在 2.14.0 版本中发布了[断线重连后恢复实时订阅](https://github.com/vitorpamplona/quartz/pull/82)功能。每个中继从已投递事件中最新的 created_at 处恢复，上限为设备时钟；gift wrap 过滤器会额外向前回溯两天，以覆盖时间戳回填的情况。中继在中断期间存储的、时间戳较旧的事件仍可能被遗漏。已合并但尚未发布的[计数感知 negentropy 窗口](https://github.com/vitorpamplona/quartz/pull/85)会将可选的 [NIP-45](/zh/topics/nip-45/) 事件计数与本地计数进行比较，并将中继提供的计数视为不可信。

### Buzz {#buzz}

Buzz 合并了一项变更，[将 kind 5 和 9005 删除与目标的软删除放在同一事务中提交](https://github.com/block/buzz/pull/8944)，因此发生故障时不会再出现删除已被接受而目标仍然有效的情况。历史上已存在的不一致行不会被修复。[NIP-RS](/zh/topics/nip-rs/) 是 Buzz 用于跨设备已读状态的草案，其移动端配置已合并，可[在设备间同步已读前沿](https://github.com/block/buzz/pull/8998)。在不支持 read_state_snapshot 的旧中继上，本地已读仍然有效，但跨设备同步会停止，且没有回退机制。

### Alby Hub {#alby-hub}

Alby Hub 是一个为 [NIP-47](/zh/topics/nip-47/) Nostr Wallet Connect 应用提供服务的自托管 Lightning 节点，它合并了一项[数据库迁移修复](https://github.com/getAlby/hub/pull/2657)，在执行 db_migrate 或 Postgres 迁移时保留每张表的 ID 计数器。在此之前，新应用可能复用已删除应用的 ID，并继承其交易记录和隔离余额。目前尚未发现包含该修复的标签版本或部署。另一项[通知变更](https://github.com/getAlby/hub/pull/2677)将各应用的失败相互隔离，不过失败的通知仍会被直接丢弃，不会重试。

### swift-nostr-client {#swift-nostr-client}

swift-nostr-client 是一个 Swift 6 Nostr 库，它合并了一项破坏性变更，使 [RemoteSigner 在执行第一条命令前先运行 connect 握手](https://github.com/yysskk/swift-nostr/pull/287)。新的 connectsAutomatically 设置默认为 true，握手失败则命令不会发送。由于 [NIP-46](/zh/topics/nip-46/) 远程签名的 secret 只能使用一次，使用已保存的客户端密钥对恢复 bunker 会话的应用必须将其设为 false，否则第一条命令会出示已被使用过的 secret。目前尚未打标签发布。

## 新项目 {#new-projects}

### Trikey {#trikey}

Trikey 是一款处于 pre-alpha 阶段、未经审计的钱包，其手机应用与守护端通过加密的 Nostr 中继消息通信。它在 [0.1.10-alpha 版本](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf)中解决了应用打开时卡死的问题。现在双方都会保存一份重启后仍保留的已读 wrap ID 记录，并在任何签名检查或解密之前跳过这些 ID。请求和警报上的过期提示并不保证中继会删除相应内容，且发布者的性能测量是在笔记本电脑上进行的。

### Pacto {#pacto}

Pacto 是一款桌面社区组织应用，同时运行旧版 Marmot 群组和 NIP-17 私信。它发布了未签名的 [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5)，支持在一分钟内编辑已发送的消息。其[私信投递修复](https://github.com/covenant-gov/pacto-app/pull/425)会在连接池中没有可信中继时立即判定发送失败，并通过可信中继路由输入状态提示。尚未合并的开放拉取请求将新增 [squad 事件](https://github.com/covenant-gov/pacto-app/pull/488)和[加密 squad 文档](https://github.com/covenant-gov/pacto-app/pull/490)。

### Mialuna {#mialuna}

Mialuna 是一款专注于媒体的 Flutter Nostr 客户端，它发布了 [0.19.0 版本发布公告](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez)，新增在用户自己的 stories 过期时发出删除请求的功能。[变更日志提交](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886)记录了中继删除请求和 Blossom 媒体删除：本地密钥账户会自动执行，Amber 或 bunker 账户则需等到用户选择“立即删除”（Delete now）。APK 及其在设备上的行为尚未经过独立检查。删除请求无法保证中继或服务器会清除数据。

### whereAreYou {#whereareyou}

whereAreYou 是一款 Android 应用，可在通过二维码或邀请链接加入的圈子内共享位置，它使用 AES-256-GCM 加密坐标并通过公共中继发送。一项[成员签名提交](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e)阻止持有圈子密钥的人冒充其他成员发帖，所有设备都必须更新。对于 [Base45 身份备份](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc)，作者警告称，任何拍下该二维码的人都可能离线猜出其八位数字代码，据他估计只需数十分钟的 GPU 时间；但未发布基准测试。该来源未提供任何安全背书。

## 协议与规范工作 {#protocol-and-spec-work}

### Buzz 定义由所有者授权的代理凭证路由 {#buzz-defines-owner-authorized-agent-credential-routes}

Buzz 合并了一份 [NIP-FA](/zh/topics/nip-fa/) [所有者授权代理凭证草案](https://github.com/block/buzz/pull/9015)，为通过 [NIP-OA](/zh/topics/nip-oa/) 所有者证明获得授权的代理定义了授予、断言和撤销路由。授予来自 RFC 8693 令牌交换，该交换将所有者的会话与代理的 [NIP-98](/zh/topics/nip-98/) HTTP 认证证明配对；撤销会断开代理连接，并阻止其密钥重新注册。NIP-FA 是一份仅在源代码中合并的 Buzz 规范，并未声称已在生产环境启用或具备互操作性。

### 后量子事件签名获得精确验证规则 {#post-quantum-event-signatures-gain-exact-validation-rules}

长期开放的后量子签名提案新增了[针对 Nostr 事件的精确 ML-DSA-44 验证规则](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6)。密钥和签名的长度固定，验证方以空上下文对 32 字节原始事件 ID 摘要验证签名，且不允许任何回退算法。提议的身份没有 [NIP-19](/zh/topics/nip-19/) bech32 编码，新签名也不会使 [NIP-44](/zh/topics/nip-44/) 加密载荷或 [NIP-59](/zh/topics/nip-59/) gift wrap 具备后量子安全性。

### 拟议的签名前置条件可防止事件替换丢失 {#a-proposed-signed-precondition-prevents-lost-event-replacements}

Buzz 的一个开放拉取请求[提议一种项目本地的 NIP-CS 签名前置条件](https://github.com/block/buzz/pull/8835)，适用于可替换事件和可寻址事件，它并非官方 NIP。签名标签指明当前头部 ID 或 `none`，中继在坐标锁下以原子方式检查该标签，以 false OK 或 HTTP 409 拒绝过时的写入，且不存储任何内容。未带该标签的写入照常工作，且该标签不提供跨中继的比较并交换（compare-and-swap）保证。

## NIP 深度解析：NIP-31 与 NIP-73 {#nip-deep-dive-nip-31-and-nip-73}

客户端经常会遇到自身无法原生理解的内容。[NIP-31: Dealing with Unknown Event Kinds](/zh/topics/nip-31/) 为陌生的事件类型提供可读标签，[NIP-73: External Content IDs](/zh/topics/nip-73/) 则为 Nostr 之外的主题命名，例如书籍或网页。这两项约定是相互独立的现有规范（[NIP-31 文本](https://github.com/nostr-protocol/nips/blob/master/31.md)、[NIP-73 文本](https://github.com/nostr-protocol/nips/blob/master/73.md)）。

### NIP-31 被标记为不推荐 {#nip-31-is-marked-unrecommended}

当前的 [NIP-31 文本](https://github.com/nostr-protocol/nips/blob/master/31.md)开头有一条警告，以“不必要地臃肿”（"unnecessarily bloated"）为由将其标记为 `unrecommended`，其状态行写的是 draft、unrecommended 和 optional。使用该约定的事件已经存在于中继上，因此下文的机制说明描述的是客户端如何读取这些事件，并不推荐新协议采用。

### alt 标签承载什么 {#what-an-alt-tag-carries}

根据[规范](https://github.com/nostr-protocol/nips/blob/master/31.md)，如果作者的自定义类型不打算作为文本阅读，作者应添加一个 `alt` 标签，附上简短的纯文本摘要。以 kind 1 为中心的客户端不需要请求其他类型，但用户仍可在笔记中引用此类事件，此时摘要能够提供上下文。标签本身无法投票，也无法处理钱包请求。如需更丰富的交互，规范指向 [NIP-89: Recommended Application Handlers](/zh/topics/nip-89/)。

由于 `alt` 是一个标签，[NIP-01](/zh/topics/nip-01/)：[Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md) 中的事件 ID 和签名会覆盖它。有效签名验证的是一段由作者控制的摘要：它表明标签由作者发布，但不能表明标签准确，因此可能出现误导性摘要。标签是公开的，所以加密内容事件上的 `alt` 会暴露其摘要，并可能泄露内容本应隐藏的信息。这些特性来自 [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) 的事件封装结构，并不属于 NIP-31 的规范性文本。顶层 `alt` 标签也不同于 `imeta` 内部用于图片描述的 `alt` 字段，渲染器会分别解析二者。

### 两个客户端如何读取 alt {#how-two-clients-read-alt}

在 noStrudel 的[未知事件卡片（提交 7c68acf）](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)中，第一个 `alt` 标签去除首尾空白后成为主标签，并可附带一行 `Using <client>`。若该值缺失或为空，则显示 `Unknown event (kind ...)`，最多三行内容会独立显示。同一组件通过 NIP-89 处理程序模板解析 `client` 标签：存在可分享地址时显示 Open，解析出有效处理程序链接时显示 `Open in <client>`。说明与应用跳转是两个独立的控件。

Amethyst 的 [UnknownEventDigest.kt（提交 553f761）](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) 优先显示其判定为正文的内容，否则回退到 `alt`。其解析器会去除值的首尾空白，并取第一个非空的 `alt`，因此第一个 `alt` 为空的事件在这里得到的标签可能与 noStrudel 不同。以上两段描述均基于对应提交的源代码，并非已确认的发布版本行为。

### 示例：带 alt 标签的投票 {#example-a-poll-with-an-alt-label}

下面这个 kind 1068 投票取自 wss://relay.damus.io，其 ID 和 BIP340 签名按照 [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) 规则验证通过。通用渲染器可以显示双语的 `alt` 文本，而支持投票的客户端会读取 `option` 和 `polltype` 标签。

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### NIP-73 的主题与类别 {#nip-73-subjects-and-families}

[NIP-73 规范](https://github.com/nostr-protocol/nips/blob/master/73.md)（draft、optional，未标记 unrecommended）将外部主题放在 `i` 标签中，将其标识符类别放在 `k` 标签中，这样客户端既可以查询某个确切主题，也可以查询整个类别。书籍使用 `["i", "isbn:9780765382030"]` 搭配 `["k", "isbn"]`，网页则使用其 URL，并将 `k` 设为 `web`。NIP-73 没有定义任何事件类型，这些标签由其他事件携带。

### 规范化与 URL 提示 {#normalization-and-url-hints}

匹配依赖字符串完全相同，因此[规范](https://github.com/nostr-protocol/nips/blob/master/73.md)为每个类别规定了固定形式：URL 经过规范化且不含片段，ISBN 不含连字符，geohash 使用小写，ISO 3166 代码使用大写。可选的第三个数组元素携带一个 URL 提示，供对该标识符没有特定处理方式的客户端使用。该提示由作者选择，不属于身份标识的一部分。它也不能证明所有权，也不指定规范站点。

### 共享标识符不能证明什么 {#what-a-shared-identifier-does-not-prove}

根据 [NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)，相同的标识符只会把对话汇集到一起，除此之外不确立任何事情。签名评论能确认评论者是谁，但不能验证书籍、网站或播客的发布者，也不能表明由谁控制它们。别名、特定版本的 ISBN 以及规范化结果不同的 URL 可能会把同一主题拆分成多个讨论串。上下文很重要：[NIP-22](/zh/topics/nip-22/)：[Comment](https://github.com/nostr-protocol/nips/blob/master/22.md) 用大写的 `I`/`K` 表示根范围，用小写的 `i`/`k` 表示父级，而 [NIP-39: External Identities in Profiles](/zh/topics/nip-39/) 用 `i` 表示个人资料中的身份，因此并非每个 `i` 标签都是 NIP-73 主题。

### 解析器与渲染器代码中的 NIP-73 {#nip-73-in-parser-and-renderer-code}

rust-nostr 的 [nip73.rs（提交 4c8099a）](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) 将已知前缀解析为类型化的 `ExternalContentId`，并将可选提示转换为类型化 URL，仅在存在提示时才输出第三个标签元素。其测试保留了带连字符的 ISBN：解析器去掉前缀后原样存储其余部分，不应用规范中的规范化规则，因此类型化解析并不保证得到规范字符串。它将链 ID 与类别分开，把 `ethereum:100:tx:<hash>` 映射为 `ethereum:tx`。该版本没有 `iso3166` 国家变体。

Amethyst 的 [DisplayExternalId.kt（提交 553f761）](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) 将 geohash 和话题标签标识符交给专用显示组件处理。URL 标识符同样有专用显示组件，其他受支持的类型则使用通用的范围标签。URL 会打开应用内该页面对应的讨论串路由。禁用预览时，常规渲染只显示纯链接标签，不请求预览。启用预览时，获取缺失的预览可能会访问目标网站。关闭预览即可在常规渲染中避免该请求。这两个文件都不能确定发布版本的行为。

### 示例：对网页的评论 {#example-a-comment-on-a-webpage}

这条 kind 1111 评论取自 wss://nos.lol，它在 `I`/`K` 和 `i`/`k` 两组标签中放入了同一个公开 Reddit 讨论串的 URL，并按照 [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) 和 NIP-73 将类别设为 `web`。其 ID 和签名验证通过，这能确认评论的作者，但不能说明所链接页面的任何情况。

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
