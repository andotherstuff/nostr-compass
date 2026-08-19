---
title: "Nostr Compass #36"
date: 2026-08-19
publishDate: 2026-08-19
translationOf: /en/newsletters/2026-08-19-newsletter.md
translationDate: 2026-08-19
draft: false
type: newsletters
description: "Amber 与 Cambium 的签名器安全加固、邮件桥接上线、手机中继上的群组功能、加密社区审核，以及线程、加密文件与补丁方面的协议工作。"
---

欢迎回到 [Nostr Compass](https://nostrcompass.org)，您的 Nostr 每周指南。

**本周：** [Amber](https://github.com/greenart7c3/Amber) 加固中继认证并加密存储密钥，[Cambium](https://github.com/forgesworn/cambium) 在中继认证负载下为网站签名，[Citrine](https://github.com/greenart7c3/Citrine) 在手机中继上托管群组与静态站点，[Vector](https://github.com/VectorPrivacy/Vector) 在垃圾信息冲击下排队审核并跨设备同步静音，[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar) 为网状网格消息添加线程回复，[Nostria](https://github.com/nostria-app/nostria) 发布播客，[Nail](https://github.com/formstr-hq/nail) 将邮件桥接为 gift-wrap 事件。版本发布涵盖 MDK 群组状态、徽章铸造、二维码签名器配对、Android 浏览器签名与共享钱包连接。协议工作涉及评论补丁、加密文件元数据、线程格式、Marmot 重启保证与 Concord 成员列表。深度解析：徽章与评论。

## 头条新闻

### Amber 6.5.0 修复中继认证混淆代理并加密存储密钥

[Amber](https://github.com/greenart7c3/Amber) 是一款 Android [NIP-55](/zh/topics/nip-55/) 与 [NIP-46](/zh/topics/nip-46/) 签名器。[6.5.0 版](https://github.com/greenart7c3/Amber/releases/tag/v6.5.0) 修复四项已披露漏洞：[中继认证中的混淆代理](https://github.com/greenart7c3/Amber/security/advisories/GHSA-vx4h-56qj-wcp7) 曾允许任意调用者为用户从未批准的中继获取 kind `22242` [NIP-42](/zh/topics/nip-42/) 事件；[NIP-46 重放缺口](https://github.com/greenart7c3/Amber/security/advisories/GHSA-h9fv-9247-3582)；[明文连接密钥与本地密钥](https://github.com/greenart7c3/Amber/security/advisories/GHSA-5fjp-ghh8-wch8) 现于静态存储中采用信封加密；以及涵盖八项加固的[批次](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8844-q5vh-9j8f)：解密前校验调用方授权、权限解析失败即关闭、明文 `ws://` 警告、安全二维码界面、日志脱敏、登出时惰性清零密钥，以及可选的未锁设备 Keystore 使用。

[6.5.1 版](https://github.com/greenart7c3/Amber/releases/tag/v6.5.1) 在切换未锁设备要求后 Keystore 密钥轮换时重新加密已存 NIP-46 密钥，并修复权限编辑器崩溃。[6.5.2 版](https://github.com/greenart7c3/Amber/releases/tag/v6.5.2) 停止解密应用列表从不渲染的列、缓存 Keystore 句柄、启动时预热账户缓存，并对中继状态通知去抖。

[上周 6.4.0 版](/zh/newsletters/2026-08-12-newsletter/#amber-640-makes-every-grouped-signing-decision-explicit) 使分组签名决策显式化；6.5.x 改变的是 Amber 究竟会授权什么。

### Cambium 0.4.0 为网站签名并消化中继认证突发流量

[Cambium](https://github.com/forgesworn/cambium) 是一款 Android [NIP-55](/zh/topics/nip-55/) 代理，通过 [NIP-46](/zh/topics/nip-46/) 连接 Heartwood 硬件签名器。两天内发布六个版本。

[0.4.0 版](https://github.com/forgesworn/cambium/releases/tag/v0.4.0) 将签名扩展至网站。页面可通过经校验的 `nostrsigner:` 回调请求签名，而无需继承授予原生应用的权限，从而避免浏览器标签页借用另一应用的批准。同一版本修复规范的最小事件形状：仅含 `kind` 与 `content` 的事件现可正确签名，Cambium 在将事件交给 rust-nostr 前补全配对的 NIP-46 身份、当前时间戳与空标签数组。原生 rust-nostr 检测在同一变更中成为必需的持续集成门禁。

[0.3.6 版](https://github.com/forgesworn/cambium/releases/tag/v0.3.6) 修复与遵循规范的签名器配对。Cambium 旧版 rust-nostr 仅接受字面字符串 `ack` 作为 NIP-46 `connect` 调用的结果，因此若签名器按当前规范回显 bunker URI 密钥（Heartwood 固件即如此），配对会以意外响应错误结束。从 rust-nostr 0.44.2 升至 0.44.8 后两种形式均可接受，已在实机硬件与仍回答 `ack` 的 `nak bunker` 上验证。

0.4.1 至 0.4.3 版聚焦负载下的准入控制。[0.4.1 版](https://github.com/forgesworn/cambium/releases/tag/v0.4.1) 为反应、发帖、删除与加密预留队列槽位，优先于中继认证与后台解密；限制排队调用数，调用方超时后丢弃，过载时返回终端不可用结果而非弹出前台签名界面。[0.4.2 版](https://github.com/forgesworn/cambium/releases/tag/v0.4.2) 在下一请求前丢弃已超时或长期空闲的 NIP-46 会话，并允许多个相同 kind `22242` 认证事件并发共享一次硬件签名。[0.4.3 版](https://github.com/forgesworn/cambium/releases/tag/v0.4.3) 每个身份最多向硬件 worker 准入一个 distinct 认证挑战，内部从不重试认证，超时后开启每身份 60 秒冷却，同时仍对精确缓存副本作答。发布说明中的测量来自 GrapheneOS 手机驱动 [Amethyst](https://github.com/vitorpamplona/amethyst)：冷启动突发产生 33 次即时过载响应与 13 次完成请求且无签名器超时；认证突发期间的新登录在批准后 1.254 秒返回。

### Citrine 3.1.0 将手机中继变为群组主机与站点主机

[Citrine](https://github.com/greenart7c3/Citrine) 是一款设备端 Android 中继。[3.1.0 版](https://github.com/greenart7c3/Citrine/releases/tag/v3.1.0) 新增三项改变中继托管能力的功能。

对 [NIP-29](/zh/topics/nip-29/)（[基于中继的群组规范](https://github.com/nostr-protocol/nips/blob/master/29.md)，中继自身持有成员与审核状态）的支持意味着手机可托管群组而非仅加入。[NIP-86](/zh/topics/nip-86/)（[中继管理 API](https://github.com/nostr-protocol/nips/blob/master/86.md)，通过认证 JSON-RPC 暴露管理操作）随设置界面一并到达，白名单与封禁既可从应用也可从 API 驱动。对 [NIP-5A](/zh/topics/nip-5a/) [静态网站](https://github.com/nostr-protocol/nips/blob/master/5A.md) 的支持让中继向 Web 客户端提供 nsite，浏览列表现代化，含图标、搜索、按最后更新排序、安装进度、描述，以及可配置、默认 `nsite.run`、`nos.lol` 与 `nostr.land` 的抓取中继集合。

审核界面在[同一版本](https://github.com/greenart7c3/Citrine/releases/tag/v3.1.0) 同步扩展。本地封禁公钥现可一并 purge 该作者已存事件；可配置 `REJECTED_KINDS` 列表阻止运营者不想存储的 kind；访问控制可从现有列表导入。重广播工具将已存事件推回选定中继，为手机持有的归档提供重新播种网络的方式。该版本还移除 WebSocket `permessage-deflate` 扩展、收紧查询热路径、修复切换「经 Tor 暴露」时 Tor 无法启停，并将日志迁入本地数据库，logcat 仅保留 debug 构建。

### Vector 0.4.2 使社区审核在垃圾信息浪潮中存活

[Vector](https://github.com/VectorPrivacy/Vector) 是桌面与 Android [Concord](https://github.com/concord-protocol/concord) 消息客户端。[0.4.2 版](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.2) 聚焦负载下的审核。

快速封禁曾相互覆盖，现改为排队、堆叠并结算为单次操作，封禁一波账户只需一次密钥轮换而非每账户一次。接受已解散社区的邀请现会说明原因并从用户拥有的每台设备移除该邀请；用户拥有的社区解散后会在各处清除社区列表，该修复见于 [0.4.3 版](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.3)。后台追赶期间到达的社区消息不再像刚发送一样触发通知；输入指示器自发送时刻起过期，延迟信号无法在频道中 linger。与另一 Concord 客户端 Armada 对 [Concord](https://github.com/concord-protocol/concord) 定义的分片社区列表做了跨客户端审查：重命名不再膨胀列表、平局在两端一致解析、未变数据不再重发到中继。

静音也移出私信路径：用户现可直接在社区中静音某人，无需先有消息历史；静音作用于通知与徽章，跨频道与私信，消息本身仍可见。置顶消息成为共享频道界面，含可点击链接，对已置顶消息的编辑会随其出现。屏蔽列表、静音与昵称现可在用户设备间同步，置顶聊天亦然。0.4.3 版还停止在另一 Nostr 客户端以同一身份登录时宣告用户正在输入，并解除 Windows 上 Tor 引导冻结在 15% 的问题（x64 与 ARM64 均受影响）。

### Sonar 以 NIP-C7 为网状消息客户端带来线程回复

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar) 是蓝牙网状与 Nostr 消息客户端。[0.1-alpha.13.1 版](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.1) 在 [NIP-C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) kind `9` 聊天中加入 Signal 式回复，以及 @ 提及、有界蓝牙重组、备份上限、网状路径签名验证与 FCM 推送回退。[0.1-alpha.13.2 版](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.2) 与 [0.1-alpha.13.3 版](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.13.3) 修复 Android 打开聊天崩溃与 iOS 键盘遮挡。

### Nostria 开始发布播客并请求中继计数

[Nostria](https://github.com/nostria-app/nostria) 是 Web 客户端。[4.1.70 版](https://github.com/nostria-app/nostria/releases/tag/v4.1.70) 与 [4.1.71 版](https://github.com/nostria-app/nostria/releases/tag/v4.1.71) 为高级订阅者增加播客发布，单集为已签名 Nostr 事件。[4.1.69 版](https://github.com/nostria-app/nostria/releases/tag/v4.1.69) 在信息流中使用 [NIP-45](/zh/topics/nip-45/) `COUNT` 统计反应、回复与 zap 总数，并完成本地化。[上周 4.1.67 版](/zh/newsletters/2026-08-12-newsletter/#nostria-4167-expands-encrypted-community-administration) 扩展了加密社区管理。

## 版本发布

### MDK 0.9.14：更快群组创建下的失败即关闭群组历史

[MDK](https://github.com/marmot-protocol/mdk) 是 [Marmot](https://github.com/marmot-protocol/marmot)（经 Nostr 传输的加密群组消息协议）的 Rust 开发套件。[0.9.12 版](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.12) 使多条群组状态路径失败即关闭而非猜测：缺失分叉锚点现为硬错误（[PR #1329](https://github.com/marmot-protocol/mdk/pull/1329)）；离开提案原子持久化，崩溃不会留下半应用 departure（[PR #1360](https://github.com/marmot-protocol/mdk/pull/1360)）；事件重放拒绝在无 manifest 的换行分隔 JSON 流上猜测格式（[PR #1140](https://github.com/marmot-protocol/mdk/pull/1140)）。收敛测试同期扩大：保留历史跨路由恢复（[PR #1350](https://github.com/marmot-protocol/mdk/pull/1350)）、跨适配器收敛保证（[PR #1372](https://github.com/marmot-protocol/mdk/pull/1372)）与泛化孤立收敛活动（[PR #1357](https://github.com/marmot-protocol/mdk/pull/1357)）。中继拒绝诊断得以保留而非坍缩为通用失败（[PR #1361](https://github.com/marmot-protocol/mdk/pull/1361)）。

[0.9.13 版](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.13) 于 8 月 18 日落地，含存储格式 v2（[PR #1421](https://github.com/marmot-protocol/mdk/pull/1421)）、迁移轨道，以及增量写入取代 live 账户快照（[PR #1435](https://github.com/marmot-protocol/mdk/pull/1435)），外加更快邀请追赶（[PR #1444](https://github.com/marmot-protocol/mdk/pull/1444)）与 macOS 绑定（[PR #1402](https://github.com/marmot-protocol/mdk/pull/1402)）。[0.9.14 版](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.14) 于 8 月 19 日跟进群组创建打磨：预上传创始图像（[PR #1498](https://github.com/marmot-protocol/mdk/pull/1498)）、KeyPackage 批处理（[PR #1494](https://github.com/marmot-protocol/mdk/pull/1494)）、原子初始消息保留（[PR #1497](https://github.com/marmot-protocol/mdk/pull/1497)），以及随账户自有中继发布个人资料（[PR #1495](https://github.com/marmot-protocol/mdk/pull/1495)）。[MarmotKit 0.9.14](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.9.14) 与 [wn-agent 0.9.14](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.14) 随核心 crate 一并发布。

### Divine Mobile 1.0.20：应用内铸造徽章

[Divine Mobile](https://github.com/divinevideo/divine-mobile) 是通过 Nostr 发布与检索短视频的客户端。[1.0.20 版](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.20) 允许用户铸造 [NIP-58](/zh/topics/nip-58/) 徽章（本期首个深度解析所述已签名授予事件）并转赠他人，无需离开应用。点击个人资料上的徽章会说明获得条件——规范中定义事件与授予事件分存，这部分通常无人实现。

[该版本](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.20) 其余为客户端工作：浅色主题、定格编辑器裁剪旋转翻转、录制器一键草稿、字幕与视频时间轴对齐、降低已观看素材优先级的信息流、编辑器/录制器/个人资料标签的屏幕阅读器支持、减少动效处理，以及管理 Divine 邮箱密码与账户关联/解绑的账户设置。已删视频现会离开本地状态，书签持久化。[上周 1.0.19 版](/zh/newsletters/2026-08-12-newsletter/#divine-mobile-1019-tightens-accounts-private-messages-and-publishing) 加固账户隔离与私信校验；徽章签发是在其上的新发布面。

### ClipRelay 0.2.0：用相机配对签名器

[ClipRelay](https://github.com/tajava2006/cliprelay) 经 Nostr 在设备间同步剪贴板。[Android 0.2.0 版](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.2.0) 增加 `nostrconnect://` 二维码登录，用户可用另一手机上的签名器应用登录；增加相机扫描 bunker URL，避免经消息应用粘贴含密钥字符串的习惯。bunker 连接现 60 秒超时而非挂起，Amber 登录失败后的重试按钮可用。[桌面 0.2.0 版](https://github.com/tajava2006/cliprelay/releases/tag/desktop%2Fv0.2.0) 携带超时与登录标签修复。

[0.1.4 版](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.1.4) 增加敏感剪贴板同步（短中继过期）、固定签名器会话中继，以及要求真实往返而非本地合成 `EOSE` 的存活探测。[上周 0.1.3 版](/zh/newsletters/2026-08-12-newsletter/#cliprelay-013-restores-relay-and-signer-connections-after-idle-periods) 在空闲期后恢复连接。

### Bark 1.3.9：可在 Android 上运行的浏览器签名器

[Bark](https://github.com/forgesworn/bark) 是提供 [NIP-07](/zh/topics/nip-07/) `window.nostr` 接口（网页调用以请求签名或加密操作的对象）的浏览器扩展。[1.3.9 版](https://github.com/forgesworn/bark/releases/tag/v1.3.9) 为 Firefox 构建声明 Android 支持，插件列表可在手机上安装。Android 版 Firefox 无 windows API，每个曾打开弹出窗口的批准都会被直接拒绝；批准界面现回退到前台标签页——关闭即拒绝，审查操作将其置前，请求结算后后台关闭。发布说明记录在运行 GrapheneOS 与 Firefox 153.0.4 的 Pixel 10 Pro XL 上验证，并明确 Android 版 Chromium 编译时移除扩展子系统，任何 Chromium 衍生 Android 浏览器均无法运行 Bark。

[1.3.8 版](https://github.com/forgesworn/bark/releases/tag/v1.3.8) 从另一方向修复 NIP-46 互操作缺陷。Bark 曾以 JSON 对象发送事件来探测 Heartwood 紧凑签名方言，严格类型签名器（含 `nak` 与基于 rust-nostr 的 bunker）无法解析并静默丢弃，导致签名挂起。探测现仅发往自识别为 Heartwood 的签名器，其余签名器从首次签名起即收到标准 `sign_event` 调用。

### Bray 3.0.0 与 Toll Booth 6.0.0 迁移至共享钱包连接库

[Bray](https://github.com/forgesworn/bray) 与 [Toll Booth](https://github.com/forgesworn/toll-booth) 均通过 [NIP-47](/zh/topics/nip-47/) Nostr Wallet Connect（应用经加密 Nostr 事件向钱包请求支付的规范）付款。[Bray 3.0.0 版](https://github.com/forgesworn/bray/releases/tag/v3.0.0) 与 [Toll Booth 6.0.0 版](https://github.com/forgesworn/toll-booth/releases/tag/v6.0.0) 均声明破坏性变更，采用 [nwc-kit](https://github.com/forgesworn/nwc-kit) 处理钱包支付；Toll Booth 同期移除付款方凭证流程。二者均发布可复现构建，两台独立 runner 输出字节一致，tarball 哈希印在发布说明中供读者校验 registry 制品。

Toll Booth 随后三个补丁：[6.0.1 版](https://github.com/forgesworn/toll-booth/releases/tag/v6.0.1) 固定协商部署主机密钥，[6.1.1 版](https://github.com/forgesworn/toll-booth/releases/tag/v6.1.1) 将 `cashu-ts` 固定到补丁目标版本，[6.1.2 版](https://github.com/forgesworn/toll-booth/releases/tag/v6.1.2) 恢复镜像构建。

### NoorNote 1.3.4：通过邀请链接加入加密社区

[NoorNote](https://github.com/77elements/noornote) 是面向桌面、Web 与 Android 的 Nostr 客户端。[1.3.4 版](https://github.com/77elements/noornote/releases/tag/v1.3.4) 以插件形式增加加密 Armada 与 Concord 社区：用户经邀请链接加入，在设置中查看已加入社区并接收活动通知。同一版本增加隐藏外部引用帖的控制——引用网页段落的 highlight 笔记可全局或按作者隐藏，其转帖一并隐藏，用户自己的 highlight 仍可见。个人资料解析亦已修复，不再渲染为截断公钥或匿名占位符。

[1.3.5 版](https://github.com/77elements/noornote/releases/tag/v1.3.5) 为长笔记增加展开器并修正 Armada 邀请链接输入布局。[上周 1.3.2 版](/zh/newsletters/2026-08-12-newsletter/#noornote-132-moves-article-discovery-into-the-social-graph) 将文章发现移入社交图谱；社区成员资格是独立界面。

### Mostro 将争议聊天移出 gift wrap

[Mostro](https://github.com/MostroP2P/mostro) 是订单与消息以 Nostr 事件传输的点对点交易守护进程，[mostro-core](https://github.com/MostroP2P/mostro-core) 为共享库，[Mostro Mobile](https://github.com/MostroP2P/mobile) 为客户端。[Mobile 1.3.2 版](https://github.com/MostroP2P/mobile/releases/tag/v1.3.2) 将争议聊天从 [NIP-59](/zh/topics/nip-59/) gift wrap 迁移至 kind `14` 聊天信封，并以每会话持久游标支撑积压。[mostro-core 0.14.5 版](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.5) 在 gift wrap 内序列化 rumor 标识符（[PR #164](https://github.com/MostroP2P/mostro-core/pull/164)），[0.14.4 版](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.4) 修复评分平均值 bug（[PR #163](https://github.com/MostroP2P/mostro-core/pull/163)），[Mobile 1.3.1 版](https://github.com/MostroP2P/mobile/releases/tag/v1.3.1) 切换至保留加密聊天附件的 Blossom 服务器。请使用守护进程 [0.18.2 版](https://github.com/MostroP2P/mostro/releases/tag/v0.18.2) 或 [0.18.4 版](https://github.com/MostroP2P/mostro/releases/tag/v0.18.4)。

### NYM 3.73.522：加密群聊与加密本地存储

[NYM](https://github.com/Spl0itable/NYM) 是带自有助手集成的 Nostr 客户端。[3.73.522 版](https://github.com/Spl0itable/NYM/releases/tag/v3.73.522) 在 [3.73.521 版](https://github.com/Spl0itable/NYM/releases/tag/v3.73.521) 完善加密群聊后加密本地 SQLite 存储；[3.73.520 版](https://github.com/Spl0itable/NYM/releases/tag/v3.73.520) 修复内容安全策略破坏与重复新消息展示。

### Morganite 0.0.4：缓存前校验 blob

[Morganite](https://github.com/greenart7c3/Morganite) 是 Android [Blossom](/zh/topics/blossom/) 服务器（媒体协议：文件由内容 SHA-256 哈希寻址，任意持有主机均可提供）。[0.0.4 版](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.4) 在单次 pass 下载过程中校验 blob 哈希再缓存——接收端使内容寻址有意义的检查。该版本还增量跟踪缓存大小而非每次保存全目录扫描，将阻塞网络调用移至 I/O 线程，复用 Tika 实例做 MIME 检测，并将日志持久化至本地数据库。

## 新发现

### Nail 以 gift-wrap 事件将邮件带上 Nostr

[Nail](https://github.com/formstr-hq/nail) 是 Formstr 团队（[Formstr](https://github.com/formstr-hq/nostr-forms) 与 [nostr-calendar](https://github.com/formstr-hq/nostr-calendar) 背后团队）的 MIT 许可邮件桥接与 Web 客户端。8 月 18 日上线 [PR #7](https://github.com/formstr-hq/nail/pull/7)，22 文件变更：为邮件事件增加 `k` 标签、设置中密钥恢复与欢迎消息。部署运行于 [mailstr.app](https://mailstr.app)，提供桥接自有 `_smtp` [NIP-05](/zh/topics/nip-05/) 记录（将域名下名称映射至 Nostr 公钥的 DNS 方案）。

邮件本身是 Nostr 事件。客户端 [constants](https://github.com/formstr-hq/nail/blob/main/client/src/lib/nostr/constants.ts) 定义 kind `1301` 邮件 rumor，封装在 kind `1059` [NIP-59](/zh/topics/nip-59/) gift wrap 内，消息经与私密私信相同的元数据隐藏信封送达收件人。投递中继来自 kind `10050` [NIP-17](/zh/topics/nip-17/) 收件箱列表，其后为 kind `10002` [NIP-65](/zh/topics/nip-65/) 中继列表；文件夹为 `mail` 命名空间下 kind `1985` [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) 标签；客户端设置存于 kind `30078` [NIP-78](/zh/topics/nip-78/) 应用数据事件。超过 60,000 字节的附件走 [Blossom](/zh/topics/blossom/) 而非写入事件，因 [NIP-44](/zh/topics/nip-44/) 将加密明文上限定为 65,535 字节。地址为域名下的 npub；无 NIP-05 记录的本地域名视为不存在的邮箱。

桥接半部是与 [mailcow](https://github.com/mailcow/mailcow-dockerized) 部署并存、无需 patch 的 Node LMTP 服务器：Postfix 将匹配域名路由至桥接，桥接经 SMTP 注入回复。该设计迫使邮件桥最难问题——`From` 头证明什么——给出诚实答案。Nail [receive 路径](https://github.com/formstr-hq/nail/blob/main/client/src/lib/mail/receive.ts) 将每封邮件分为四种来源状态之一：配置的桥接已密封且拒绝转发其未在上游验证的发件人；用户自行密封；地址 NIP-05 记录解析至密封密钥；或无任何内容 corroborate 头信息。末一种情况下界面回退至密封公钥——事件能实际证明的唯一身份。桥接 API 调用以 [NIP-98](/zh/topics/nip-98/) 签名 HTTP 事件认证。

### Glow 在 passkey 衍生身份下将钱包标签存于中继

[Glow](https://breez.technology/glow/) 是 Breez 自托管 Lightning 钱包。passkey 登录衍生 Nostr 身份，钱包标签列表自中继读取并保存于该身份下，部分中继覆盖下的字节相同副本会折叠。

## 开发中

### Amethyst 重建中继认证决策流程

[Amethyst](https://github.com/vitorpamplona/amethyst) 是 Android Nostr 客户端。一批合并工作重塑 [NIP-42](/zh/topics/nip-42/) 客户端-中继认证处理：权限界面与决策流程重新设计（[PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)）；认证现等待挑战解析而非超时（[PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)）；新账户默认始终向中继认证（[PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)）；「始终登录」选择对账户自身未使用的中继亦生效（[PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)）。认证还将 [NIP-29](/zh/topics/nip-29/) 群组与 Concord 社区识别为已加入场所（[PR #3906](https://github.com/vitorpamplona/amethyst/pull/3906)），避免中继托管群组每次打开都像陌生中继。

另两项变更触及协议面：[NIP-13](/zh/topics/nip-13/) 工作量证明挖矿在挖矿时刷新 `created_at` 并增加 GPU 路径分析（[PR #3911](https://github.com/vitorpamplona/amethyst/pull/3911)）；全屏 napplet 宿主处理输入法 inset（[PR #3932](https://github.com/vitorpamplona/amethyst/pull/3932)）。带设置入口的引导首次运行密钥备份亦已合并（[PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)），以及静音公开聊天能力（[PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)）。

### nostrord 实现未合并的加密密钥提案

[nostrord](https://github.com/nostrord/nostrord) 是以中继范围群组组织的 Nostr 聊天客户端。它合并了 NIP-4e 的实现——将消息加密与身份密钥解耦的未合并提案，Compass 曾在 [7 月 15 日期刊](/zh/newsletters/2026-07-15-newsletter/) 描述。账户公告自有 kind `10044` 加密密钥，私钥半部本地持有，进程内解密入站私信，将 bunker 或浏览器扩展完全移出读取路径（[PR #261](https://github.com/nostrord/nostrord/pull/261)）。kinds `4454` 与 `4455` 的设备配对将该密钥移至第二设备，自归档重新发布寻址新密钥的历史。发送现优先寻址已公告密钥（[PR #247](https://github.com/nostrord/nostrord/pull/247)），后续修复协商成功却未交出密钥的配对（[PR #271](https://github.com/nostrord/nostrord/pull/271)）。PR 声明线格式在偏离开放提案处遵循已部署的 Jumble 实现，将该规范的工作定义置于已发布代码而非文档。

群组身份在同一批次收紧：群组标识符现仅在其中继内唯一（[PR #269](https://github.com/nostrord/nostrord/pull/269)），两中继上相同标识符视为两群组（[PR #272](https://github.com/nostrord/nostrord/pull/272)），线程帖渲染为论坛帖（[PR #274](https://github.com/nostrord/nostrord/pull/274)）。产生重复 kind `22242` 签名提示的连接抖动亦已停止（[PR #268](https://github.com/nostrord/nostrord/pull/268)）——与 Cambium 本周三个版本所应对的签名器压力同类。

### nostream 增加中继监控并铸造邀请码

[nostream](https://github.com/cameri/nostream) 是 TypeScript 中继实现。它合并发布 [NIP-66](/zh/topics/nip-66/) 中继监控事件（发现规范：监控者向其他中继公告存活与能力数据）的集群 worker 与探测调度器（[PR #724](https://github.com/cameri/nostream/pull/724)），含设置 schema 与默认值（[PR #689](https://github.com/cameri/nostream/pull/689)）及集成测试（[PR #733](https://github.com/cameri/nostream/pull/733)）。命令行工具现铸造 [NIP-43](/zh/topics/nip-43/) 邀请码（门禁准入的中继访问元数据方案）（[PR #732](https://github.com/cameri/nostream/pull/732)）；中继终于在支持列表中公告 [NIP-13](/zh/topics/nip-13/) 工作量证明（[PR #680](https://github.com/cameri/nostream/pull/680)）——其实现已久却未公告。数据自动售货机作业亦获持久化迁移与仓库（[PR #727](https://github.com/cameri/nostream/pull/727)）；中继现捕获 [NIP-90](/zh/topics/nip-90/)（数据自动售货机作业请求）并经作业仓库记录（[PR #729](https://github.com/cameri/nostream/pull/729)）。

### rust-nostr 修复 gift-wrap 标识符并拒绝受保护转帖

[rust-nostr](https://github.com/nostrdevkit/nostr) 是本期大量 Rust 与移动客户端工作背后的 Rust 库与 SDK。它现于加密 gift-wrap 密封前计算 rumor 标识符（[PR #1444](https://github.com/nostrdevkit/nostr/pull/1444)）——Mostro 本周在其库中修复的同类缺陷。本地中继拒绝 [NIP-70](/zh/topics/nip-70/) 受保护事件的转帖（[PR #1445](https://github.com/nostrdevkit/nostr/pull/1445)）——该规范存在即为此保护；NIP-47 响应解析容忍缺失与 null 金额（[PR #1450](https://github.com/nostrdevkit/nostr/pull/1450)），而非在钱包省略时失败。中继 URL 解析已加固（[PR #1451](https://github.com/nostrdevkit/nostr/pull/1451)）。

### NDK 增加后量子私信并移除 GPL 依赖

[NDK](https://github.com/relaystr/ndk) 是 Nostr 的 Dart 开发套件。它合并使用 ML-KEM-1024（标准化为 FIPS 203 的格密钥封装机制）的混合后量子私信加密（[PR #713](https://github.com/relaystr/ndk/pull/713)），与经典密钥协商并存而非取代。另一变更以 `fips204`（ML-DSA 签名标准）替换 GPL-3.0-only Dilithium 实现（[PR #712](https://github.com/relaystr/ndk/pull/712)），移除嵌入 kit 的应用的许可约束。连接亦改为每身份一条（[PR #710](https://github.com/relaystr/ndk/pull/710)）。

### Nostter 增加书签列表、个人资料徽章与 Blossom 上传

[Nostter](https://github.com/SnowCait/nostter) 是 Web 客户端。它合并对 [NIP-51](/zh/topics/nip-51/) 书签列表标准与旧版两种形状的支持（[PR #2311](https://github.com/SnowCait/nostter/pull/2311)），更新 NIP-58 个人资料徽章处理（[PR #2281](https://github.com/SnowCait/nostter/pull/2281)），增加 Blossom 媒体上传器（[PR #2298](https://github.com/SnowCait/nostter/pull/2298)），并在 @ 提及自动完成中显示 [NIP-05](/zh/topics/nip-05/) 标识符（基于 DNS 的验证名）（[PR #2303](https://github.com/SnowCait/nostter/pull/2303)）。

### Zap Cooking 将管理路由绑定至签名请求并加密存储钱包连接

[Zap Cooking](https://github.com/zapcooking/frontend) 是基于 Nostr 长文事件的食谱站点。安全批次在 NIP-44 信封内静态加密存储 Nostr Wallet Connect 连接字符串（[PR #622](https://github.com/zapcooking/frontend/pull/622)）；以 [NIP-98](/zh/topics/nip-98/) HTTP 认证（签名事件授权 HTTP 请求的方案）替换管理路由上可伪造的公钥比较（[PR #626](https://github.com/zapcooking/frontend/pull/626)）；登出清除账户数据并限制待处理 NIP-46 记录（[PR #627](https://github.com/zapcooking/frontend/pull/627)）。

## 协议与规范工作

### NIPs

本窗口内无 PR 合并入 [nostr-protocol/nips](https://github.com/nostr-protocol/nips)。上期结束后开启六项提案，其中三项于 8 月 18 日草案首次 circulated 后开启。

[NIPs PR #2438](https://github.com/nostr-protocol/nips/pull/2438) 提案 NIP-9A：基于评论的补丁。补丁为 kind `1111` 评论，以被补丁事件为父，`content` 以字面标签 `PATCH` 开头，后接补丁行。以数字开头的行按 `<index> -<deleted> +<inserted> <inserted characters>` 编辑目标 `content`，按 Unicode 字符而非字节计数；以 `t` 开头的行替换人类可读标签如 `title`、`description`、`subject` 或 `picture`。设计刻意向后兼容：不理解格式的客户端将补丁显示为普通带标签评论；理解的客户端应用补丁并隐藏评论。提案命名 kind `1`、`11`、`1111`、`24` 与 `1621` 为可补丁对象，并要求读写双方拒绝过大、过多或远晚于原事件发布的补丁——明确试图避免功能成为不可变事件的通用编辑通道。

[NIPs PR #2437](https://github.com/nostr-protocol/nips/pull/2437) 为 [NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)（在 kind `1063` 事件中描述已上传文件的文件元数据规范）提案文件加密。新增三个可选标签：`encryption-algorithm`（仅列 `aes-gcm`）、十六进制 `decryption-key` 与 `decryption-nonce`。标签语义相应偏移：`m` 描述加密前 MIME 类型，`x` 持加密文件哈希，`ox` 持原文件哈希；任何 `thumb`、`image` 与 `fallback` 源以相同密钥与 nonce 加密。 stated 目的是公开 Blossom 运营者托管字节时无法知晓内容；作者将变更框定为把 [NIP-17](/zh/topics/nip-17/) 私信加密属性复制进文件元数据，使相同处理在 `imeta` 标签内生效。

[NIPs PR #2436](https://github.com/nostr-protocol/nips/pull/2436) 修订 NIP-7D——基于 kind `11` 线程事件、[NIP-22](/zh/topics/nip-22/) kind `1111` 评论为回复的论坛线程规范。增加格式章节：线程帖可像 kind `1` 笔记一样格式化，含内联图片、链接与 [NIP-27](/zh/topics/nip-27/) 引用；亦可支持语法无歧义的轻量标记语言 Djot。作者论点是未指定格式会默许 eventual Markdown 实现；PR 指向 squalk 作为现有 Djot 实现。

[NIPs PR #2439](https://github.com/nostr-protocol/nips/pull/2439) 向 [NIP-86](/zh/topics/nip-86/)（中继管理命令）增加 `assign` 与 `unassign` 方法，中继管理员可在不共享主密钥的情况下向另一公钥授予管理权限。

[NIPs PR #2442](https://github.com/nostr-protocol/nips/pull/2442) 在前草案仍开放时接续 [Compass 一月报道](/zh/newsletters/2026-01-13-newsletter/) 的音轨提案；较早 PR 已关闭，本 PR 在 lightning.fm 生产环境以 kind `31337` 音轨事件、kind `31339` 发行对象、乐队个人资料、每轨贡献者与可选 [NIP-57](/zh/topics/nip-57/) zap 分成发货，销售仍走 [NIP-99](/zh/topics/nip-99/)。互操作合约发布于 [lightning.fm/interop](https://lightning.fm/interop)；桌面发布器与自托管卖家守护进程开源。

### Marmot

[Marmot PR #416](https://github.com/marmot-protocol/marmot/pull/416) 于 8 月 13 日合并，为协议核心增加持久性与重启合约。已采用文档已定义确定性收敛、保留候选父材料、先发布后应用排序与缺失历史失败即关闭，却缺少一条明确规则说明进程在它们之间接缝被中断时发生什么。变更定义可恢复逻辑事实、重启等价、发布与收敛中断边界、观察者原子转换、缺失或损坏材料处理与应用效果恢复，并为每项增加崩溃与重启一致性场景。事务、日志、快照、重放策略、调度器与存储格式仍实现定义，并声明无需线编码变更。其 foreclosed 的具体失败是：外部已接受发布却未本地确认，或部分应用选定分支，重启后产生实现依赖的协议结果。

### Concord 与 CORDs

[Concord PR #18](https://github.com/concord-protocol/concord/pull/18)（上周期刊曾作为开放提案报道）已于 8 月 15 日合并。它将加密社区列表分片至 kind `33302` 事件，移除五十成员上限，并 prune 退役条目以保持列表在中继大小限制内。Vector 本周发布说明记录该变更的客户端一半，含平局解析与停止重发未变数据的决定。

[Concord PR #22](https://github.com/concord-protocol/concord/pull/22) 提案社区拥有的音视频 broker。CORD-02 元数据实体将在 relays 旁携带可选 `av_brokers` 列表，像该实体其余部分一样按 edition 演进；CORD-07 rendezvous 将从该列表抽取，或社区未发布时从成员自有 broker 抽取，按现有 room-keyed 平局排序。presence 上的 broker 标签仍可读且对报告残余分裂有用；提案将其从路由降级的论点直接：在其上路由让 fellow 成员不可信输入压过社区自身指令。

[Concord PR #23](https://github.com/concord-protocol/concord/pull/23) 将现有实现行为在 CORD-05 中规范化。持久化 join 前，所有者 genesis 元数据 edition 必须在交付密钥下打开，旋转平面锚定于 compaction 对。PR  upfront 声明这从未是 live 漏洞：Vector bundle 接受已拒绝交付 root 无法打开所有者 genesis 的 bundle，且从不停放已持有社区的邀请；Armada 已丢弃会移动已持有社区 base 的任何 bundle。缺口是规范未要求任一行为，遵循规范的客户端本可发布 vulnerable 版本。

[Blossom 升级文档](https://github.com/hzrd149/blossom)、[Napplet 应用提案](https://github.com/napplet/naps) 与 [Gamma Markets 规范](https://github.com/GammaMarkets/market-spec) 本窗口无变更记录。

## NIP 深度解析

### 徽章（NIP-58）

[NIP-58](/zh/topics/nip-58/) 由其[主规范](https://github.com/nostr-protocol/nips/blob/master/58.md)定义，赋予一个 Nostr 身份向另一身份授予命名 token 的方式，并赋予接收方控制是否在个人资料展示的权力。它解决的问题是：Nostr 上关于某人的任何陈述否则只是笔记——没有结构说明谁签发了声明、声明叫什么、外观如何，或主体是否接受。徽章用三个独立签名事件、三种独立作者意图编码该声明。

[机制](https://github.com/nostr-protocol/nips/blob/master/58.md) 由可寻址定义、授予与展示列表构成。徽章定义是签发者发布的 kind `30009` 事件，经 `d` 标签可寻址，签发者可稍后修订 `name`、`description`、`image` 与 `thumb` 标签而不改变其他引用使用的标识符。授予是同一签发者发布的 kind `8` 事件，携带指向 `30009:<issuer-pubkey>:<d-identifier>` 定义坐标的 `a` 标签与一个或多个命名接收方的 `p` 标签。展示列表是接收方发布的 kind `30008` 事件，`d` 固定为 `profile_badges`，列出 `a` 与 `e` 标签对——`a` 为定义坐标，`e` 为具体授予事件。这些对有序且成对读取：缺少匹配授予的 `a` 或缺少匹配定义的 `e` 被忽略，半引用徽章静默不渲染。

[规范](https://github.com/nostr-protocol/nips/blob/master/58.md) 拒绝做什么，设计权衡即在其中可见。无撤销机制与过期，授予是签发者关于某时刻的永久陈述；签发者改主意只能改授予指向的定义。无转让，徽章不能作为 token 流通。无可信签发者 registry 概念，信任问题完全推给客户端与读者：徽章价值恰等于签发者公钥对观看者的价值。规范还赋予客户端展示少于接收方所列徽章、选择渲染哪张图片的自由度，避免个人资料成为第三方全选图形墙。

最近邻规范是 [NIP-51](/zh/topics/nip-51/)（[列表规范](https://github.com/nostr-protocol/nips/blob/master/51.md)）；对比二者可见徽章为何需要三个事件而非一个。列表是单一作者策展引用；列表作者即声明作者。徽章将署名一分为二：签发者签名授予发生，接收方签名接受展示。任一方无法单独产生可见结果——这正是徽章与自贴标签的区别。

本周从 [nos.lol](https://nos.lol) 与 [relay.primal.net](https://relay.primal.net) 恢复的 live kind `8` 授予：

```json
{
  "id": "08504dec368939bd63849a349cab83dea0ac199a852129dbf68cf35fe5c64e96",
  "pubkey": "bef514bd58c8ceea4beb9e6b84a8d983935f7be26f49e14df68098f1ba64156e",
  "created_at": 1787051248,
  "kind": 8,
  "tags": [
    ["a", "30009:bef514bd58c8ceea4beb9e6b84a8d983935f7be26f49e14df68098f1ba64156e:blocks_orange_league"],
    ["p", "92dfa05d915196a7a09152fa3f57871debfd422e1d278ac5af266a70c3350b1f", "wss://relay.damus.io"]
  ],
  "content": "Badge awarded!",
  "sig": "5bf0218dfec5e56b47339b0b4b992cceedd2e18798fb3d47cafea51850c00827f66251e4a3e08190370e04a5e1d4d092eeb441141b7219acdd18b80290a022f8"
}
```

当前实现覆盖签发、展示与读取。[Divine Mobile 1.0.20 版](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.20) 在应用内铸造并授予徽章，读者点击时解释已获得徽章；[Nostter PR #2281](https://github.com/SnowCait/nostter/pull/2281) 更新 Web 客户端个人资料徽章处理；[Amethyst](https://github.com/vitorpamplona/amethyst) 发布携带自有客户端标签的授予事件，其中一例与上例同现于中继数据。

### 评论（NIP-22）

[NIP-22](/zh/topics/nip-22/) 由其[主规范](https://github.com/nostr-protocol/nips/blob/master/22.md)定义，为回复非短文本笔记的对象提供通用评论事件。短笔记线程已有 [NIP-10](/zh/topics/nip-10/)，其标签约定围绕 kind `1` 与回复链生长。NIP-22 存在是因为视频、文章、日历事件、wiki 页或 URL 需要识别被回复对象 kind 的回复结构，且在被回复对象为可寻址或完全无 Nostr 事件的外部资源时仍有效。

[机制](https://github.com/nostr-protocol/nips/blob/master/22.md) 取决于大小写区分。评论是 kind `1111` 事件，携带两组标签：大写标签描述讨论根，小写标签描述直接父对象。`E`、`A` 与 `I` 命名根事件、根可寻址坐标或根外部标识符；`K` 命名根 kind；`P` 命名根作者。小写 `e`、`a`、`i`、`k` 与 `p` 命名关于父对象的相同事实——顶层评论的父即根本身，嵌套回复的父为另一 kind `1111` 评论。分离它们意味着客户端可用一条大写根标签 filter 抓取整段讨论，无需遍历回复链，同时仍从小写父标签正确渲染嵌套。`I` 与 `i` 变体以 [NIP-73](/zh/topics/nip-73/) 格式携带外部标识符——这正是评论线程可附着网页、播客单集或书籍的原因。

权衡 mostly 关于 NIP-22 拒绝吸收什么。[规范](https://github.com/nostr-protocol/nips/blob/master/22.md) 声明评论不得用于回复 kind `1` 笔记——避免两种线程模型在同一对象上竞争，NIP-10 在已有效处保留。允许嵌套但根固定，深线程即使中间事件不可用也不丢失锚点。kind 标签是 load-bearing 部分：抓取评论却无目标的客户端仍可从 `K` 与 `k` 知晓在看什么，并决定是否能渲染该 kind。规范未提供任何排序或审核模型，显示顺序、折叠与隐藏完全是客户端策略。

与 [NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) 相比，差异在 typing。NIP-10 假设目标是笔记并编码线程位置；NIP-22 显式编码目标身份与 kind，对其余不作假设。这种显式 typing 正是本期较新提案转向 kind `1111` 的原因：评论已携带关于附着对象的机器可读陈述。

本周从 [nos.lol](https://nos.lol) 与 [relay.primal.net](https://relay.primal.net) 恢复的 live kind `1111` 评论，在视频下回复另一评论：

```json
{
  "id": "c8d335f8bfea58ecd1a943d6000fb2045f4bddf4a36c67df53eb661671f7ab45",
  "pubkey": "3e911baba55ae247339cf805dd6ff49ad2cd6bee84ac44e088ce66450c49104f",
  "created_at": 1787062681,
  "kind": 1111,
  "tags": [
    ["E", "1c492f2bac17b79d66934a340fa43d8d30d0aea4c9fa329346c05573ef912d70", "", "482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839"],
    ["A", "34236:482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839:e64ba9ea157b1a315caff51dbca656ed73ce817d4494e3966adf24055a86f5c5", ""],
    ["K", "34236"],
    ["P", "482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839"],
    ["e", "7a14723b9ef999e74b1757a0fb74942cb6c121138d4ddafe096a57a67ed0a442", "", "8b69e548402afa997343d73e8088224a440f256350f6257b61acc4bb1fa4af4f"],
    ["k", "1111"],
    ["p", "8b69e548402afa997343d73e8088224a440f256350f6257b61acc4bb1fa4af4f"],
    ["client", "Divine", "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile", "wss://relay.divine.video"]
  ],
  "content": "niiice",
  "sig": "a5517fdea07647efa7ab1730fbea8df882690bba667e93ea5aeba4a73be6a49af1ee17c045535483650caf41dbbcb0897d5803fa39b59f395fd6f9bb193bb789"
}
```

大写标签持有视频及其作者，小写 `e` 与 `k` 指向父评论——正是规范描述的形状。读写 kind `1111` 的实现包括 [Divine Mobile](https://github.com/divinevideo/divine-mobile)（其客户端标签出现在上例事件中）、[Amethyst](https://github.com/vitorpamplona/amethyst)（其评论出现在同一中继结果中），以及本周将线程帖渲染为论坛帖的 [nostrord](https://github.com/nostrord/nostrord/pull/274)。[NIPs PR #2438](https://github.com/nostr-protocol/nips/pull/2438) 中的补丁格式提案构建于同一 kind。

---

发送 [NIP-17](/zh/topics/nip-17/) 私信，通过 [Nostr Compass 项目](https://github.com/andotherstuff/nostr-compass) 分享项目或新闻。
