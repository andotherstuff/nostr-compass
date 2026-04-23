---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您的每周 Nostr 指南。

**本周：** [Amethyst](https://github.com/vitorpamplona/amethyst) 落地了一轮大规模的 Marmot 兼容、社区和 MoQ 音频房间工作；[TollGate](https://github.com/OpenTollGate/tollgate) 在 [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) 中稳定了基于 Nostr 与 Cashu 的按量付费互联网接入；[nostream](https://github.com/Cameri/nostream) 则围绕 [NIP-45](/zh/topics/nip-45/)、[NIP-62](/zh/topics/nip-62/)、压缩、查询加固和完整的 [NIP-11](/zh/topics/nip-11/) 对齐完成了一周的 relay 工作。[Forgesworn](https://github.com/forgesworn) 一次性发布了完整的 Nostr 签名、身份和付费 API 工具栈。[ShockWallet](https://github.com/shocknet/wallet2) 继续推进 Nostr 原生 Lightning wallet 工作流。Formstr 套件、[StableKraft](https://github.com/ChadFarrow/stablekraft-app)、[Keep](https://github.com/privkeyio/keep-android)、[topaz](https://github.com/fiatjaf/topaz)、[WoT Relay](https://github.com/bitvora/wot-relay)、[Flotilla](https://gitea.coracle.social/coracle/flotilla) 和 [NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) 也都带来了值得注意的发布。本期两篇 NIP 深度解析分别是 [NIP-72](/zh/topics/nip-72/)（审核社区）和 [NIP-57](/zh/topics/nip-57/)（zaps）。

## 头条

### Amethyst 发布 Marmot MIP 兼容、NIP-72 社区、zap goals 和 MoQ 音频房间

[Amethyst](https://github.com/vitorpamplona/amethyst) 本周合并了 57 个 PR，重点围绕 [Marmot](/zh/topics/marmot/) 加密群聊兼容、原生审核社区、直播 zap goals，以及基于 Media over QUIC 的新音频房间栈。[PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) 让内嵌 [MDK](https://github.com/marmot-protocol/mdk) 与 MIP-01、MIP-05 wire formats 对齐，[PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) 增加 MIP-00 KeyPackage Relay List 支持，[PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466)、[PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471)、[PR #2477](https://github.com/vitorpamplona/amethyst/pull/2477) 和 [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) 则继续补齐 commit framing、外层解密和密码学验证路径。[PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) 还发布了命令行工具 `amy`。在产品层，[PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) 带来了第一等 [NIP-72](/zh/topics/nip-72/) 社区创建与管理，[PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) 把 [NIP-75](/zh/topics/nip-75/) zap goals 接到 [NIP-53](/zh/topics/nip-53/) 直播页面，[PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494) 则新增 Media over QUIC 客户端和音频房间支持。

### TollGate v0.1.0 让基于 Nostr 和 Cashu 的按量付费互联网更稳定

[TollGate](https://github.com/OpenTollGate/tollgate) 于 4 月 21 日发布 [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)，这是其“按量付费网络接入”规范集合的首个带 tag 快照。该协议允许任何能够控制连接的设备，例如 WiFi 路由器、以太网交换机或 Bluetooth tether，发布价格、接受 [Cashu](/zh/topics/cashu/) ecash tokens，并通过预付本地 token 管理会话。这个版本固定了三层架构：协议层由 [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) 和 [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) 定义，接口层由 [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) 到 HTTP-03 及 [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) 组成，介质层则由 [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) 描述 captive portal 场景下的路由方式。由于支付资产是不记名 bearer token，用户只要本地 Cashu wallet 里已有 token，就可以直接买下第一分钟网络接入。

### nostream 合并 53 个 PR，覆盖 NIP-45、NIP-62、压缩和查询加固

[nostream](https://github.com/Cameri/nostream) 这套 TypeScript relay 实现，在一周内合并了 53 个 PR，覆盖新 NIP 支持、查询性能、安全加固和运维细节。[PR #522](https://github.com/Cameri/nostream/pull/522) 增加 [NIP-45](/zh/topics/nip-45/) `COUNT` 支持，[PR #544](https://github.com/Cameri/nostream/pull/544) 把 [NIP-62](/zh/topics/nip-62/) right-to-vanish 加入其广告的能力列表，[PR #548](https://github.com/Cameri/nostream/pull/548) 扩展 filter schema 支持大写 tag filters，而 [PR #514](https://github.com/Cameri/nostream/pull/514) 则为 event import/export 增加 gzip 和 xz 压缩。性能与正确性方面，[PR #534](https://github.com/Cameri/nostream/pull/534) 引入 benchmark harness 并优化了 filter-to-SQL 转换，[PR #524](https://github.com/Cameri/nostream/pull/524) 修复了 pubkey whitelist/blacklist 的前缀匹配 bug，[PR #553](https://github.com/Cameri/nostream/pull/553) 让 `upsertMany` 在并发插入时加入确定性的 tie-breaker，[PR #493](https://github.com/Cameri/nostream/pull/493) 只信任来自已配置 trusted proxies 的 `X-Forwarded-For`，而 [PR #557](https://github.com/Cameri/nostream/pull/557) 使其达到完整 [NIP-11](/zh/topics/nip-11/) 对齐。

## 本周发布

### Primal Android 增加 Explore tab、NIP-05 验证和音频播放器

[Primal Android](https://github.com/PrimalHQ/primal-android-app) 在上周信息流重做的基础上，又合并了 11 个 PR。[PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021) 增加新的 Explore tab，[PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015) 增加 feed editor，[PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994) 带来 [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md) 资料验证 UI，[PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997) 在信息流中嵌入音频播放器，而 [PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018) 则把钱包二维码扫描路径复用于 [NIP-46](/zh/topics/nip-46/) pairing。

### strfry 增加 Prometheus 写路径指标并修复 NIP-42 AUTH envelope

[strfry](https://github.com/hoytech/strfry) 发布了一组面向运营者的改进。[PR #194](https://github.com/hoytech/strfry/pull/194) 增加了专门的 Prometheus 写路径指标导出器，[PR #197](https://github.com/hoytech/strfry/pull/197) 记录每连接上下行字节与压缩率，[PR #192](https://github.com/hoytech/strfry/pull/192) 把过滤器 tag 限制改成运行时可配置，而 [PR #201](https://github.com/hoytech/strfry/pull/201) 则把 [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH 失败响应从 `NOTICE` 改为规范要求的 `OK` envelope。

### Shopstr 通过 13 个 PR 加固店铺安全

[Shopstr](https://github.com/shopstr-eng/shopstr) 本周合并 13 个 PR，重点几乎全在安全修复。[PR #434](https://github.com/shopstr-eng/shopstr/pull/434) 修复店铺链接中的存储型 JavaScript 漏洞，[PR #417](https://github.com/shopstr-eng/shopstr/pull/417) 处理店铺政策 HTML 渲染，阻断反射型 XSS，[PR #418](https://github.com/shopstr-eng/shopstr/pull/418) 关闭未认证的缓存 event 删除 API。[PR #433](https://github.com/shopstr-eng/shopstr/pull/433)、[PR #419](https://github.com/shopstr-eng/shopstr/pull/419)、[PR #435](https://github.com/shopstr-eng/shopstr/pull/435) 和 [PR #414](https://github.com/shopstr-eng/shopstr/pull/414) 也分别修复了缓存消息读取认证、受保护端点访问与 SSRF 问题。

### Nostria v3.1.26 到 v3.1.28 为 Android 增加后台音乐播放

[Nostria](https://github.com/nostria-app/nostria) 本周发布了 [v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22) 到 [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28) 的六个版本。头条变化出现在 [v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26)：应用在播放音频时会保持自身存活，并在通知栏和锁屏上提供媒体控制。[v3.1.27](https://github.com/nostria-app/nostria/releases/tag/v3.1.27) 与 [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28) 继续加固这一新的媒体服务表面。

### Wisp v0.18.0-beta 增加 Normie Mode、For You feed 和 NIP-29 群组配置

[Wisp](https://github.com/barrydeen/wisp) 于 4 月 16 日发布 [v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta)，面向来自非 Bitcoin 原生环境的新用户。[PR #462](https://github.com/barrydeen/wisp/pull/462) 增加了在应用中全面显示法币金额的 Normie Mode，[PR #464](https://github.com/barrydeen/wisp/pull/464) 重做 onboarding，[PR #469](https://github.com/barrydeen/wisp/pull/469) 增加 For You feed。协议层面，[PR #471](https://github.com/barrydeen/wisp/pull/471) 增加 [NIP-29](/zh/topics/nip-29/) 的 flags、invites、roles 和 AUTH prompts，而 [PR #481](https://github.com/barrydeen/wisp/pull/481) 则会把 note 广播到被 mention pubkeys 的 [NIP-65](/zh/topics/nip-65/) inbox relays。

### NoorNote v0.8.4 增加定时发布和直播 zap

[NoorNote](https://github.com/77elements/noornote) 发布了 [v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) 和 [v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5)。v0.8.4 的核心新增功能是 Scheduled Posts：应用会把已签名 event 交给 NoorNote 运营的 relay，在计划时间代为发布，因此私钥始终留在设备端。该版本还增加了直播卡片的一键 zap，通过 [NIP-53](/zh/topics/nip-53/) 把 sats 显示在直播聊天覆盖层内，而 v0.8.5 则修复了长列表滚动时出现的重复帖子问题。

### topaz v0.0.2 发布一个可在 Android 上运行的 Nostr relay

[topaz](https://github.com/fiatjaf/topaz) 于 2026-04-17 发布 [v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2)。这个由 fiatjaf 构建的新 relay 以 Kotlin 为主，目标是把手机本身变成一个随时可用的个人 relay。当前阶段它的范围仍较窄，重点是先提供一个可安装的 Android 包和一个可运行 relay。

### StableKraft v1.0.0 发布首个稳定版音乐与播客 PWA

[StableKraft](https://github.com/ChadFarrow/stablekraft-app) 是一个使用 Next.js 构建的 PWA，用于从 podcast feeds 中发现、整理和播放音乐，同时通过 Nostr 实现登录与社交，通过 Lightning 完成 V4V 支付。它在 2026-04-18 达到 [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0)。同一周里，项目还通过 [15 分钟 OPML cache 和非法 XML 清理](https://github.com/ChadFarrow/stablekraft-app/commit/7ac90f6) 收紧了 feed ingestion，并通过一个[后续修复](https://github.com/ChadFarrow/stablekraft-app/commit/fbf337b) 把 nightly reparse 窗口从 720 小时缩短到 24 小时。

### NipLock 发布基于 NIP-17 的密码管理器

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) 是一个使用 [NIP-17](/zh/topics/nip-17/) gift-wrapped 私信，在多设备之间存储和同步凭证的密码管理器。每条密码记录都是用户发给自己的 NIP-17 DM，因此只要设备使用同一个 key 认证，就能复现同一组 events。签名既可以使用原始 `nsec`，也可以通过 [nos2x](https://github.com/fiatjaf/nos2x) 或 [Amber](https://github.com/greenart7c3/Amber) 配合 [NIP-46](/zh/topics/nip-46/) 完成。

### flotilla-budabit 打磨其 NIP-34 仓库界面

Budabit 社区的 [Flotilla](https://gitea.coracle.social/coracle/flotilla) 分支 [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit) 本周发布了一组围绕 NIP-34 git-over-nostr 工作流的修复，包括恢复仓库讨论控制、在详情页保持 sticky repo tabs 可见、从保存的 GRASP relays 加载仓库公告，以及保持维护者应用的 patch 状态同步。

### rx-nostr 3.7.2 到 3.7.4 增加默认验证器和可选构造参数

[rx-nostr](https://github.com/penpenpng/rx-nostr) 发布了 [3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2)、[3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3) 和 [3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4)。[PR #192](https://github.com/penpenpng/rx-nostr/pull/192) 加入默认 Schnorr signature verifier，并通过配套的 [crypto@3.1.6](https://github.com/penpenpng/rx-nostr/releases/tag/crypto%403.1.6) 修复 `@noble/curves` 用法问题。[PR #195](https://github.com/penpenpng/rx-nostr/pull/195) 则让 `createRxNostr()` 的参数变为可选。

### Keep Android v1.0.0 在可复现构建和零追踪器下发布

[Keep](https://github.com/privkeyio/keep-android) 于 4 月 21 日发布 [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0)。[PR #241](https://github.com/privkeyio/keep-android/pull/241) 提供可复现构建配方，[PR #248](https://github.com/privkeyio/keep-android/pull/248) 用 ZXing 替换 Google ML Kit，以去除 Google Play Services 依赖，而 [PR #252](https://github.com/privkeyio/keep-android/pull/252) 发布了 [Exodus Privacy scan](https://reports.exodus-privacy.eu.org/en/)，显示 v1.0.0 构建零追踪器。[PR #256](https://github.com/privkeyio/keep-android/pull/256) 则增加了 `zapstore.yaml`，让 APK 能直接通过 [zapstore](https://zapstore.dev) 分发。

### Flotilla 1.7.3 和 1.7.4 通过 kind-9 wrapping 丰富 NIP-29 房间

[Flotilla](https://gitea.coracle.social/coracle/flotilla) 发布了 [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) 和 [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)。最核心的协议变化，是把非聊天内容类型包裹进 kind `9` 中，再送入房间，这样客户端在渲染 calendar events、polls 等对象时，就不会丢失它们来自哪个房间的上下文。该版本线还加入了 polls、Aegis URL scheme 的 [NIP-46](/zh/topics/nip-46/) 登录、space invites 原生分享、room mentions、草稿和通话中的视频支持。

### WoT Relay v0.2.1 把 eventstore 迁移到 LMDB

[WoT Relay](https://github.com/bitvora/wot-relay) 于 2026-04-22 发布 [v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1)。[PR #97](https://github.com/bitvora/wot-relay/pull/97) 把 eventstore 迁移到 [LMDB](http://www.lmdb.tech/)，并调优 bootstrap 获取逻辑，避免初始 trust graph 构建时耗尽上游读取预算。[PR #99](https://github.com/bitvora/wot-relay/pull/99) 更新 `golang.org/x/crypto` 到 v0.45.0，[PR #100](https://github.com/bitvora/wot-relay/pull/100) 则更新了对外广告的 [NIP-11](/zh/topics/nip-11/) software URL 和版本字符串。

### Formstr 套件：Pollerama 安全加固、Forms i18n、Calendar RRULE 支持

Formstr 套件本周在 Pollerama、Formstr forms 和 Nostr Calendar 三个项目中一共合并了 26 个 PR。Pollerama 重点做了安全工作，包括退出登录时清理缓存 DM、把本地 key 移入安全浏览器存储、在登录路径中防御恶意 kind `0` profile 的 `JSON.parse` 崩溃。Formstr 本体则增加了音视频 URL 支持、Web app i18n，以及 Google Forms 导入功能，并移除了浏览器控制台中的敏感 key logs。Nostr Calendar by Formstr 同日发布 [v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0) 和 [v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0)，带来多个与自定义 RRULE 规则、UTC 解释和共享事件加入有关的改进。

### 另外发布：notedeck、nostr.blue、cliprelay、Captain's Log

本周还有一些客户端发布了没有单独头条的大版本：Damus 团队的 [notedeck](https://github.com/damus-io/notedeck) 发布 [v0.10.0-beta.4](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.4)，修复 column 渲染和 relay pool；Dioxus 构建的 Rust 客户端 [nostr.blue v0.8.6](https://github.com/patrickulrich/nostr.blue/releases/tag/v0.8.6) 引入 Dioxus 0.7.5，并通过把原生音频 bridge 改写为 `manganis::ffi` plugin 恢复 Android 构建；[cliprelay](https://github.com/tajava2006/cliprelay) 发布桌面版 v0.0.3 和 Android 版 v0.0.4，继续收紧跨设备剪贴板同步循环；[Captain's Log](https://github.com/nodetec/comet) 则连续发布三版 alpha，增加 sync-relay liveness detection。

## 开发中

### whitenoise-rs 重构为按 session 划分的账户视图

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) 是 [Marmot](/zh/topics/marmot/) 客户端背后的 Rust daemon，本周合并 15 个 PR，把架构从全局单例重构到按账户划分的 `AccountSession` 视图。[PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) 建立了 `AccountSession` 与 `AccountManager` 骨架，后续阶段则陆续把 relay handles、草稿和设置、消息操作、群组读写、成员关系、push notifications、key-package 读取、群组创建，以及在 [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770) 中完成的 session 级 event dispatch 迁移到新结构中。

### White Noise 增加拉黑/取消拉黑 UI、退群和离线提示

[White Noise](https://github.com/marmot-protocol/whitenoise) 本周补齐了缺失的群组生命周期控制。[PR #578](https://github.com/marmot-protocol/whitenoise/pull/578) 在 [PR #573](https://github.com/marmot-protocol/whitenoise/pull/573) 的 block hook 之上增加拉黑与取消拉黑 UI，[PR #571](https://github.com/marmot-protocol/whitenoise/pull/571) 与 [PR #572](https://github.com/marmot-protocol/whitenoise/pull/572) 把 Rust 侧的 `clear_chat`、`delete_chat` 和 `leave_and_delete_group` 串接进 app。[PR #569](https://github.com/marmot-protocol/whitenoise/pull/569) 与 [PR #576](https://github.com/marmot-protocol/whitenoise/pull/576) 还在聊天与设置页增加离线提示。[PR #585](https://github.com/marmot-protocol/whitenoise/pull/585) 则把“删除所有 key packages”收窄为“删除 legacy key packages”。

### MDK 增加混合版本邀请支持和 SelfUpdate wire format 收敛

[MDK](https://github.com/marmot-protocol/mdk) 本周合并了 7 个 PR，主线是兼容性。[PR #261](https://github.com/marmot-protocol/mdk/pull/261) 通过将群组 `RequiredCapabilities` 计算为被邀请者能力的 LCD，打通了 [Amethyst](https://github.com/vitorpamplona/amethyst) 与 [White Noise](https://github.com/marmot-protocol/whitenoise) 之间的混合版本邀请。[PR #264](https://github.com/marmot-protocol/mdk/pull/264) 统一了 SelfUpdate wire format，[PR #262](https://github.com/marmot-protocol/mdk/pull/262)、[PR #256](https://github.com/marmot-protocol/mdk/pull/256)、[PR #259](https://github.com/marmot-protocol/mdk/pull/259) 和 [PR #265](https://github.com/marmot-protocol/mdk/pull/265) 则分别针对 malformed invitees、admin depletion validation、内存后端下关键状态被驱逐，以及 `group_required_proposals` 访问器做了修复与暴露。

### nostter 把 NIP-44 加到 people lists、bookmarks 和 mutes

[nostter](https://github.com/SnowCait/nostter) 本周合并 10 个 PR。[PR #2088](https://github.com/SnowCait/nostter/pull/2088) 为 mute lists 增加 [NIP-44](/zh/topics/nip-44/) 加密，[PR #2089](https://github.com/SnowCait/nostter/pull/2089) 把同样逻辑加到 bookmarks，[PR #2090](https://github.com/SnowCait/nostter/pull/2090) 加到 people lists，并通过 [PR #2087](https://github.com/SnowCait/nostter/pull/2087) 删除了遗留的 kind-30000 mute migration 路径。

### zap.cooking 发布 Nourish 评分和可复用评论线程

[zap.cooking](https://github.com/zapcooking/frontend) 本周合并了 20 个 PR。头条功能是新的 Nourish 配方评分模块（[PR #317](https://github.com/zapcooking/frontend/pull/317)、[PR #319](https://github.com/zapcooking/frontend/pull/319)），同时 [PR #299](https://github.com/zapcooking/frontend/pull/299) 到 [PR #302](https://github.com/zapcooking/frontend/pull/302) 还把 Comments 模块抽成可复用的 `CommentThread`。

### ridestr 抽出共享 rider coordinator

[ridestr](https://github.com/variablefate/ridestr) 本周合并 10 个 PR，把其 Compose screens 拆成更聚焦的组件，并通过 [PR #70](https://github.com/variablefate/ridestr/pull/70) 把 rider 与 driver 协议逻辑提取到共享的 `:common` coordinator 模块中。[PR #60](https://github.com/variablefate/ridestr/pull/60) 还为 Roadflare 侧加入了 kind `3189` 的 driver-ping receiver。

### Blossom 起草用于 blob 过期的 BUD-01 Sunset header

[Blossom](https://github.com/hzrd149/blossom) 打开了 [PR #99](https://github.com/hzrd149/blossom/pull/99)，希望为 BUD-01 增加 `Sunset` header。服务器可以通过这个 header 广告某个未来时间戳，说明 blob 将在那时停止被服务，从而让客户端在遇到 404 之前，就能围绕有限保留期做规划。

## 新项目

### Forgesworn 发布一个包含 29 个仓库的 Nostr 密码学工具栈

[Forgesworn](https://github.com/forgesworn) 在五天内一口气发布了 29 个开源仓库，覆盖签名、身份、证明、web-of-trust 和基于 Lightning 的付费 API 发现。签名栈以 [nsec-tree](https://github.com/forgesworn/nsec-tree) 和 [Heartwood](https://github.com/forgesworn/heartwood) 为核心，前者可从一个主密钥导出无限多个不可关联的 Nostr 身份，后者是一个默认开启 Tor 的 NIP-46 远程 signer。身份与信任栈则围绕 [Signet](https://github.com/forgesworn/signet)、[nostr-attestations](https://github.com/forgesworn/nostr-attestations) 和 [nostr-veil](https://github.com/forgesworn/nostr-veil) 展开；货币化方向则有 [toll-booth](https://github.com/forgesworn/toll-booth)、[toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm)、[toll-booth-announce](https://github.com/forgesworn/toll-booth-announce) 和 [402-indexer](https://github.com/forgesworn/402-indexer)，将付费 API 暴露为 [NIP-90](/zh/topics/nip-90/) DVM 和可发现的 kind `31402` announcements。整个组织全部使用 TypeScript，并通过新的 bash-only 工具 [anvil](https://github.com/forgesworn/anvil) 做供应链加固型发布。

### ShockWallet 发布 Nostr 原生 Lightning wallet 同步和多节点连接

[ShockWallet](https://github.com/shocknet/wallet2) 是一个使用 Nostr 作为传输层、连接自托管 Lightning 节点的 wallet。应用通过 `nprofile` 与一个或多个 [Lightning.Pub](https://github.com/shocknet/Lightning.Pub) 节点进行 Nostr 配对，并在 wallet 与节点之间端到端签署支付授权。本周团队发布 [PR #608](https://github.com/shocknet/wallet2/pull/608)，增加了 channels dashboard UI，并与管理员邀请 QR 链路和 metrics dashboard 可读性改进一同落地。ShockWallet 还使用 [NIP-78](/zh/topics/nip-01/) 风格的应用专用数据事件来完成多设备 wallet 状态同步，这使它与 [NIP-47](/zh/topics/nip-47/) 的“应用调用现有 wallet”模型有所区分。

### Nostrability issues 在 GitHub 审查后迁移到 git over Nostr

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues) 是 elsat 维护的 Nostr 客户端与 relay 互操作性问题追踪器。在 GitHub 上的组织被下线且两周未获回应后，这个问题流转工作流正在迁移到 git over Nostr，新的 issue tracker 现已运行在 GitWorkshop/ngit 上。

### nowhere 把完整网站编码进 URL fragments，并通过 Nostr 路由订单

[nowhere](https://github.com/5t34k/nowhere) 是 [5t34k](https://github.com/5t34k) 发布的一个 AGPL-3.0 项目，它把完整网站序列化进 `#` 之后的 URL fragment，并通过字典替换、原始 DEFLATE 和 base64url 编码进行压缩。由于浏览器不会把 fragment 发给服务器，提供页面的主机看不到内容，网站本身也无需存储在服务器上。其八种站点类型中，有五种完全静态，而 store、forum 和 petition 等三类需要动态通信的流量，则通过带临时 keys 与 [NIP-44](/zh/topics/nip-44/) 加密的 Nostr relays 路由。

### 小而新的界面：relayk.it 和 Brainstorm Search

还有两个小项目值得一提：[relayk.it](https://relayk.it) 是由 Soapbox 团队的 [sam](https://nostr.com/sam@relayk.it) 构建、基于 [Shakespeare](https://shakespeare.diy) 的 relay 发现客户端，完全在浏览器中运行；[Brainstorm Search](https://brainstorm.world) 则是一个单页 Nostr 搜索 UI，专注于从整个网络中显露内容。

## 协议与规范工作

### NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)中的最新提案与讨论：

**开放 PR 和讨论：**

- **[NIP-67](/zh/topics/nip-67/)：EOSE Completeness Hint**（[PR #2317](https://github.com/nostr-protocol/nips/pull/2317)）：提议为 [NIP-01](/zh/topics/nip-01/) 的 `EOSE` 消息增加一个可选第三元素，让 relay 能告诉客户端“我已经把所有匹配的已存储 events 都发完了”。
- **NIP-5D：Nostr Applets**（[PR #2303](https://github.com/nostr-protocol/nips/pull/2303)）：为通过 Nostr 分发、运行在客户端沙箱 iframe 或 WebView 中的交互式 applets 定义新 kind。
- **NIP-29：Subgroups spec**（[PR #2319](https://github.com/nostr-protocol/nips/pull/2319)）：为 [NIP-29](/zh/topics/nip-29/) 群组增加 subgroup 层级，使单个群组能够承载多个并行频道。
- **NIP-29：Explicit role permissions on kind 39003**（[PR #2316](https://github.com/nostr-protocol/nips/pull/2316)）：为 kind `39003` 角色事件定义显式权限模式，让客户端能够知道具体角色到底拥有何种能力。
- **NIP-11：`access_control` 字段用于受限 relay 发现**（[PR #2318](https://github.com/nostr-protocol/nips/pull/2318)）：在 [NIP-11](/zh/topics/nip-11/) relay 信息文档中增加一个可选对象，列出 gating mode 以及申请访问的 endpoint。
- **NIP-63a：Minimal Payment Gateway Descriptor**（[PR #2315](https://github.com/nostr-protocol/nips/pull/2315)）：继续围绕 kind `10164` 的 payment-gateway-descriptor 形状与 per-tier subscription rules 做迭代。
- **NIP-XX：Agent Reputation Attestations (Kind 30085)**（[PR #2320](https://github.com/nostr-protocol/nips/pull/2320)）：提议为 Nostr 上的自治 agent 和服务定义带签名的信誉证明 event，用于在 [NIP-90](/zh/topics/nip-90/) 等服务市场中发布可验证反馈。
- **NIP-TPLD：Transient Private Location Data**（[PR #2309](https://github.com/nostr-protocol/nips/pull/2309)）：继续推进 kind `20411`、按接收者加密的 [NIP-44](/zh/topics/nip-44/) 载荷，以及 `ttl` tag 的 relay 保留语义。
- **marmot-ts 0.5.0 release PR**（[PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)）：计划中的 `@internet-privacy/marmot-ts@0.5.0` 会引入第一批 breaking changes，改造 KeyPackage 处理和邀请/群组管理接口。

## NIP 深度解析：NIP-72（审核社区）

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) 定义了一种围绕主题组织社区的模型，其中审核员通过批准机制，策展出一个基于公开 Nostr events 的“可读视图”。与由 relay 同时掌控成员与审核的 [NIP-29](/zh/topics/nip-29/) 不同，NIP-72 社区存在于普通 Nostr events 中，任何承载相关 kinds 的 relay 都可以服务它。任何人都可以发帖，而只有被认可审核员批准过的帖子，才会出现在社区信息流中。社区由 kind `34550` 可寻址 event 定义，帖子通过 `a` tag 指向该社区坐标，审核员再通过 kind `4549` approval event 发布批准。由于批准 event 自身就是可验证的 Nostr event，审核决策是透明、可审计、可分叉的。与 NIP-29 相比，它的优势是无需特殊 relay 支持、写路径天然可移植；它的代价则是未被批准的帖子其实已经公开写入，只是在客户端渲染层被隐藏。

## NIP 深度解析：NIP-57（Zaps）

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md) 定义了 zaps，也就是把 Lightning 支付附着到 Nostr 身份与内容之上的方式，并规定了支付完成后如何把可验证 receipt 再发布回 relays。zap 的流程跨越 LNURL、Lightning 和 Nostr 三个系统：发送者客户端通过接收者 profile 或目标 event 上的 `zap` tag 发现 LNURL endpoint，构造并签名 kind `9734` zap request，把它发给接收者的 LNURL callback，而不是 relays；对端服务器验证请求、返回与该请求 description hash 绑定的 Lightning invoice，付款完成后，再把 kind `9735` zap receipt 发布到发送者指定的 relay 集合。一个有效的 zap receipt 必须能通过四项验证：receipt 签名对应 LNURL 响应中的 `nostrPubkey`、`bolt11` 金额匹配请求中的 `amount`、invoice description hash 绑定到字符串化的 zap request、`preimage` 能映射回 invoice 的 `payment_hash`。NIP-57 还为 private zaps、anonymous zaps、zap splits 以及 [NIP-75](/zh/topics/nip-75/) 的 zap goals 提供了底层基础。

---

本周就到这里。如果您正在构建项目，或有新闻想分享，欢迎在 Nostr 上私信我们，或访问 [nostrcompass.org](https://nostrcompass.org)。
