---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

欢迎回到 Nostr Compass，您每周的 Nostr 协议生态系统指南。

**本周要闻：** Primal Android 发布了 [NIP-46](/zh/topics/nip-46/) 远程签名和 [NIP-55](/zh/topics/nip-55/) 本地签名者支持，使其成为其他 Android 应用的完整签名中心。[Marmot Protocol](/zh/topics/marmot/) 团队针对安全审计发现的问题，合并了 18 个 PR 来强化基于 [MLS](/zh/topics/mls/) 的加密消息功能。Citrine 发布 v1.0 版本，Applesauce 整个库套件发布 v5.0 版本。TENEX 在 Nostr 上构建 AI 代理监督功能，Jumble 添加了智能中继池。一个 NIP-55 规范修复澄清了 `nip44_encrypt` 的返回字段，一个 [NIP-50](/zh/topics/nip-50/) PR 提议了用于高级搜索的查询表达式扩展。在我们的深度解析中，我们解释了 [NIP-04](/zh/topics/nip-04/) 和 [NIP-44](/zh/topics/nip-44/)：为什么传统加密存在安全缺陷，以及现代替代方案如何修复这些问题。

## 新闻

**Primal Android 成为完整签名中心** - [2.6.18 版本](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18)添加了 [NIP-46](/zh/topics/nip-46/) 远程签名和 [NIP-55](/zh/topics/nip-55/) 本地签名功能，将 Primal 转变为其他 Nostr 应用的完整签名器。通过 NIP-46 的远程签名允许用户通过 Nostr 中继连接到 bunker 服务，使私钥完全不存储在设备上。通过 NIP-55 的本地签名将 Primal 作为 Android 内容提供者公开，因此像 Amethyst 或 Citrine 这样的应用可以请求签名而无需接触私钥。[多个后续 PR](https://github.com/PrimalHQ/primal-android-app/pull/839) 修复了与 NIP-55 规范的十六进制公钥要求的兼容性问题，并改进了格式错误的 `nostrconnect://` URI 的解析。此版本还包括媒体预缓存以实现更流畅的滚动、改进的帖子线程加载时间和头像预缓存。

**Marmot Protocol 在审计后强化安全性** - [Marmot 开发工具包](https://github.com/marmot-protocol/mdk)（mdk）实现了基于 [NIP-104](/zh/topics/nip-104/) MLS 的端到端加密消息，本周收到了大量安全修复。18 个合并的拉取请求解决了审计发现的问题，包括：[加密群组图片的哈希验证](https://github.com/marmot-protocol/mdk/pull/97)以防止存储层 blob 替换攻击、[待处理欢迎消息的分页](https://github.com/marmot-protocol/mdk/pull/110)以防止内存耗尽、[错误消息中的 MLS Group ID 泄露](https://github.com/marmot-protocol/mdk/pull/112)，以及[密钥包的 base64 编码强制执行](https://github.com/marmot-protocol/mdk/pull/98)。[Marmot 规范本身也已更新](https://github.com/marmot-protocol/marmot/pull/20)，包含 MIP-04 v2 版本控制和安全改进。活跃的 PR 继续解决 nonce 重用、密钥清零和缓存污染等问题。

**Nostrability 跟踪中继提示支持** - 新的[中继提示兼容性跟踪器](https://github.com/nostrability/nostrability/issues/270)记录了客户端在整个生态系统中如何构建和使用中继提示。跟踪器显示，虽然大多数客户端现在按照 [NIP-10](/zh/topics/nip-10/) 和 [NIP-19](/zh/topics/nip-19/) 构建提示，但使用情况差异很大：一些客户端在发出事件中包含提示，但不使用传入的提示进行获取。六个客户端因完整实现而获得"完整"级别状态。该跟踪器对于检查互操作性的开发者和想知道为什么某些客户端能找到其他客户端找不到的内容的用户都很有用。

**Nostria 2.0 发布跨平台功能大更新** - [Nostria](https://nostria.app) 客户端于 12 月 30 日[发布了 2.0 版本](https://njump.me/nevent1qqs9z4l8z82zphszjlmrjkr8whpvupnlaxc7xk5gfg9syzj0thygtzgpz4mhxue69uhhyetvv9ujuerpd46hxtnfduhszxthwden5te0wfjkccte9enrw73wd9hsz9nhwden5te0wfjkccte9ec8y6tdv9kzumn9wsq3gamnwvaz7tmjv4kxz7fwv3sk6atn9e5k7qgkwaehxw309aex2mrp0yhxgctdw4eju6t09uq32amnwvaz7tmwdaejumr0dshsz9mhwden5te0wfjkccte9ec82c30989ksmfnv9kzumn9wshsqgzxsnsv7pfqqd7rw4fvr0jnkpqmwzfqq3znlc4pqunagxrkl84u66y7fq9)，在 iOS（TestFlight）、Android（Play Store）、Web 和 Windows 上增加了重大更新。该版本添加了原生音乐支持，包括播放列表创建、曲目上传、基于 zap 的艺术家支付，以及带功能均衡器的 WinAmp 风格播放器。直播功能获得了游戏 API 集成，在游戏直播期间显示丰富的元数据。新的摘要功能可生成每小时、每日或每周的活动摘要作为压缩时间线视图。发现部分提供策划列表，用于查找内容和个人资料。媒体发布通过自动生成短视频帖子简化，以实现跨客户端可发现性。远程签名器连接现在可以通过扫描二维码工作，无需手动配置。个人资料发现解决了一个常见的 Nostr 痛点：当用户在中继之间迁移而没有携带元数据时，Nostria 会定位他们的个人资料并将其重新发布到当前中继。高级订阅用户获得 YouTube 频道集成、私人备忘录、分析仪表板，以及带有合并/恢复选项的自动关注列表备份。

## NIP 更新

[NIPs 仓库](https://github.com/nostr-protocol/nips)的最新变更：

**已合并：**
- **[NIP-55](/zh/topics/nip-55/)** - 修复了 `nip44_encrypt` 方法的返回字段（[#2184](https://github.com/nostr-protocol/nips/pull/2184)）。Android 签名器现在必须在 `signature` 字段（与 `nip44_decrypt` 匹配）中返回加密的有效载荷，而不是单独的字段。这使规范与 Amber 和 Primal 中的现有实现保持一致。

**开放的 PR：**
- **[NIP-50](/zh/topics/nip-50/)** - 查询表达式扩展（[#2182](https://github.com/nostr-protocol/nips/pull/2182)）提议使用结构化查询表达式扩展 NIP-50 搜索。该 PR 添加了 `kind:1`、`author:npub1...` 等运算符和布尔组合（`AND`、`OR`、`NOT`），使得在简单文本匹配之外可以进行更精确的搜索查询。这将允许客户端构建高级搜索界面，同时保持与基本搜索字符串的向后兼容性。

## NIP 深度解析：NIP-04 和 NIP-44

本周我们介绍 Nostr 的加密标准：您仍会遇到的传统 NIP-04，以及修复关键安全缺陷的现代替代方案 NIP-44。

### [NIP-04](/zh/topics/nip-04/)：加密私信（传统）

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md) 是 Nostr 首次尝试加密消息，使用 kind 4 事件。虽然实现简单，但存在已知的安全弱点，已被弃用，推荐使用 NIP-44。

**工作原理：** NIP-04 使用 ECDH（椭圆曲线 Diffie-Hellman）在发送者和接收者之间派生共享密钥，然后使用 AES-256-CBC 加密。

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

加密流程：
1. 计算共享点：`shared = ECDH(sender_privkey, recipient_pubkey)`
2. 派生密钥：`key = SHA256(shared_x_coordinate)`
3. 生成随机 16 字节 IV
4. 加密：`ciphertext = AES-256-CBC(key, iv, plaintext)`
5. 格式化内容：`base64(ciphertext)?iv=base64(iv)`

**安全问题：**

- **无认证：** AES-CBC 提供机密性但不提供完整性。控制中继的攻击者可以修改密文位，导致明文发生可预测的变化（位翻转攻击）。
- **IV 明文传输：** 初始化向量与密文一起传输，可预测 IV 的 CBC 模式容易受到选择明文攻击。
- **无填充验证：** 实现在处理 PKCS#7 填充方面存在差异，可能导致填充预言攻击。
- **元数据暴露：** 发送者公钥、接收者公钥和时间戳对中继都是可见的。
- **密钥重用：** 双方之间的所有消息永远使用相同的共享密钥。

**为什么仍然存在：** 许多旧客户端和中继只支持 NIP-04。在与传统系统交互时会遇到它。像 Amber 这样的签名器和 Primal 等应用仍然实现 `nip04_encrypt`/`nip04_decrypt` 以保持向后兼容性。

### [NIP-44](/zh/topics/nip-44/)：版本化加密

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) 是现代加密标准，旨在修复 NIP-04 众所周知的缺陷。Cure53 对 NIP-44 实现的安全审计发现了 10 个问题（包括时序攻击和前向保密问题），这些问题在规范最终确定之前已得到解决。它使用 ChaCha20-Poly1305 以及适当的密钥派生和认证加密。

**相比 NIP-04 的主要改进：**

| 方面         | NIP-04                     | NIP-44                  |
|:-------------|:---------------------------|:------------------------|
| 密码算法     | AES-256-CBC                | XChaCha20-Poly1305      |
| 认证         | 无                         | Poly1305 MAC            |
| 密钥派生     | SHA256(shared_x)           | HKDF 带盐值             |
| Nonce        | 16 字节 IV，重用模式       | 24 字节随机 nonce       |
| 填充         | PKCS#7（泄露长度）         | 填充到 2 的幂次         |
| 版本控制     | 无                         | 版本字节前缀            |

**加密流程：**

1. **会话密钥：** 为每对发送者-接收者派生稳定密钥：
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **消息密钥：** 对于每条消息，生成随机 32 字节 nonce 并派生加密/认证密钥：
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **填充明文：** 填充到下一个 2 的幂次（最小 32 字节）以隐藏消息长度：
   ```
   padded = [length_u16_be] + [plaintext] + [zeros to next power of 2]
   ```

4. **加密和认证：**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **格式化有效载荷：**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**版本字节：** 第一个字节（`0x02`）表示加密版本。这允许未来升级而不破坏现有消息。版本 `0x01` 是早期草案，从未广泛部署。

**解密：**

1. 解码 base64，检查版本字节是否为 `0x02`
2. 提取 nonce（字节 1-32）、密文和 MAC（最后 32 字节）
3. 使用接收者的私钥和发送者的公钥派生会话密钥
4. 从会话密钥和 nonce 派生消息密钥
5. 解密前验证 MAC（如果无效则拒绝）
6. 解密密文，提取长度前缀，返回未填充的明文

**安全特性：**

- **认证加密：** Poly1305 MAC 确保在解密前检测到任何篡改
- **前向保密（部分）：** 每条消息使用唯一的 nonce，因此泄露一条消息不会暴露其他消息。但是，泄露私钥仍会暴露所有过去的消息（无棘轮机制）。
- **长度隐藏：** 2 的幂次填充隐藏确切的消息长度
- **时序攻击抵抗：** MAC 验证使用常量时间比较

**实际使用：** NIP-44 是以下功能的加密层：
- [NIP-17](/zh/topics/nip-17/) 私密私信（在 gift wrap 内）
- [NIP-46](/zh/topics/nip-46/) 远程签名器通信
- [NIP-59](/zh/topics/nip-59/) seal 加密
- [Marmot Protocol](/zh/topics/nip-104/) 群组消息，其中 NIP-44 使用从 MLS exporter secret 派生的密钥包装 MLS 加密内容
- 任何需要安全点对点加密的应用

**迁移指南：** 新应用应专门使用 NIP-44。为了向后兼容，在回退到 NIP-04 之前，检查联系人的客户端是否支持 NIP-44（通过 [NIP-89](/zh/topics/nip-89/) 应用元数据或中继支持）。接收消息时，首先尝试 NIP-44 解密，然后对传统内容回退到 NIP-04。

## 版本发布

**Primal Android v2.6.18** - [完整版本](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18)添加了 [NIP-46](/zh/topics/nip-46/) 远程签名和 [NIP-55](/zh/topics/nip-55/) 本地签名，将 Primal 转变为其他 Android 应用的签名中心。性能改进包括媒体预缓存、头像预缓存和更快的帖子线程加载。错误修复解决了个人简介中的自我提及、媒体画廊崩溃和直播标题回退问题。在 iOS 上，Primal 使用后台音频播放来保持应用活跃以接收 NIP-46 签名请求；用户可以在设置中更改声音或完全静音。

**Mostro v0.15.6** - [NIP-69](/zh/topics/nip-69/) P2P 比特币交易机器人的[最新版本](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6)完成了第 4 阶段审计事件的开发基金实现。开发费用支付现在通过每次成功支付后发布的 kind 38383 Nostr 事件进行跟踪，使第三方验证和分析成为可能。买家/卖家消息的金额计算已修复，溢价逻辑已与 lnp2pbot 参考实现对齐。

**Aegis v0.3.5** - 跨平台签名器[添加了深色模式](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5)、改进的应用图标显示和更简洁的 UI 布局。错误修复解决了 iOS iCloud Private Relay 冲突和事件解析问题。此版本还改进了事件 JSON 传递给 Rust 签名函数的方式。

**Citrine v1.0.0** - Android 中继应用[达到 1.0 版本](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0)。Citrine 让您可以直接在 Android 设备上运行个人 Nostr 中继，对于本地缓存、备份或作为 NIP-55 配套工具很有用。此版本添加了崩溃报告处理程序，提高了数据库查询效率，并通过 Crowdin 更新了翻译。

**Applesauce v5.0.0** - hzrd149 的 TypeScript 库套件[发布了重大版本](https://github.com/hzrd149/applesauce/releases)，带来了专注于正确性和简洁性的破坏性更改。核心包现在[默认验证事件签名](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0)，并将坐标方法重命名为使用更清晰的"地址"术语（`parseCoordinate` → `parseReplaceableAddress`）。中继包将[默认重试次数从 10 次降低到 3 次](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0)，默认忽略无法访问的中继，并添加了 `createUnifiedEventLoader` 以简化事件获取。钱包包获得了 [NIP-87](/zh/topics/nip-87/) [Cashu 铸币厂发现](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0)功能。各包中直接的 `nostr-tools` 依赖已被移除，减少了包大小和版本冲突。

## 值得关注的代码和文档更改

*这些是开放的拉取请求和早期阶段的工作，非常适合在合并前获得反馈。如果有什么引起您的注意，请考虑审查或评论！*

### Damus (iOS)

一系列 PR 改进了长文章体验。[阅读用户体验改进](https://github.com/damus-io/damus/pull/3496)添加了进度条、预估阅读时间、复古模式、可调行高，以及滚动时隐藏导航的专注模式。[图片修复](https://github.com/damus-io/damus/pull/3489)确保 markdown 内容中的图片通过将独立图片预处理为块级元素来显示正确的宽高比。[长文章预览卡片](https://github.com/damus-io/damus/pull/3497)将内联的 `@naddr1...` 文本替换为显示文章标题和元数据的丰富预览卡片。新的[中继集成测试套件](https://github.com/damus-io/damus/pull/3508)添加了 137 个网络相关测试，包括 [NIP-01](/zh/topics/nip-01/) 协议验证和降级网络条件下的行为（3G 模拟）。

### Bitchat（加密消息）

iOS Nostr+Cashu 消息应用的安全强化。[Noise 协议 DH 密钥清除](https://github.com/permissionlesstech/bitchat/pull/928)修复了六个 Diffie-Hellman 密钥协商后共享密钥未被清零的位置，恢复了前向保密保证。[读取回执队列的线程安全](https://github.com/permissionlesstech/bitchat/pull/929)为 NostrTransport 添加了屏障同步以防止竞态条件。[消息去重器优化](https://github.com/permissionlesstech/bitchat/pull/920)改善了高消息量下的性能，[十六进制字符串解析强化](https://github.com/permissionlesstech/bitchat/pull/919)防止格式错误输入导致的崩溃。

### Frostr（阈值签名）

基于 [FROST](/zh/topics/frost/) 的阈值签名协议[添加了二维码显示](https://github.com/FROSTR-ORG/igloo-desktop/pull/62)，用于在引导过程和签名器界面中显示群组凭证和份额凭证。这使得在多个设备之间分发密钥份额时设置更加简单，让用户可以扫描凭证而不是手动复制长字符串。

### Marmot mdk（库）

除了上述安全修复之外，活跃的 PR 继续解决剩余的审计发现：[用于清零的 Secret<T> 类型](https://github.com/marmot-protocol/mdk/pull/109)引入了一个包装类型，在 drop 时自动清零敏感数据，[消息查询分页](https://github.com/marmot-protocol/mdk/pull/111)防止加载聊天历史时的内存耗尽，[加密存储](https://github.com/marmot-protocol/mdk/pull/102)为存储群组状态和消息的 SQLite 数据库添加了静态加密。

### Amethyst (Android)

Android 客户端忙碌的一周稳定性修复。[宽松的 JSON 解析](https://github.com/vitorpamplona/amethyst/commit/2c42796)通过使 Kotlin Serialization 更宽容来防止格式错误事件导致的崩溃。事件验证现在[在处理前检查 kind 字段大小](https://github.com/vitorpamplona/amethyst/commit/40f9622)以避免过大值导致的异常。信任分数 UI 获得了更小的图标以减少视觉干扰，[改进的错误日志](https://github.com/vitorpamplona/amethyst/commit/69c53ac)有助于诊断中继连接问题。通过 Crowdin 更新了翻译，并解决了多个 SonarQube 警告。

### TENEX（AI 代理）

Nostr 原生 AI 代理框架本周有 81 个提交，构建自主能力。新的[代理监督系统](https://github.com/tenex-chat/tenex/pull/48)实现了行为启发式来监控代理动作并在需要时进行干预。[委托透明度](https://github.com/tenex-chat/tenex/commit/b244c10)在委托记录中添加了用户干预日志，以便用户可以审计代理代表他们做了什么。[LLM 提供商注册表](https://github.com/tenex-chat/tenex/pull/47)被模块化以便更容易集成不同的 AI 后端。跨项目对话支持让代理可以在多个基于 Nostr 的项目中维护上下文。

### Jumble（Web 客户端）

专注于中继的 Web 客户端添加了多项用户体验改进。[智能中继池](https://github.com/CodyTseng/jumble/commit/695f2fe)根据使用模式智能管理连接。[实时动态开关](https://github.com/CodyTseng/jumble/commit/917fcd9)让用户可以在实时流和手动刷新之间切换。[自动显示新帖子](https://github.com/CodyTseng/jumble/commit/d1b3a8c)在顶部展示新鲜内容，无需重新加载页面。关注动态和通知的[持久缓存](https://github.com/CodyTseng/jumble/commit/fd9f41c)改善了回访时的加载时间。用户现在可以通过设置[更改默认中继](https://github.com/CodyTseng/jumble/commit/53a67d8)。

---

本周就到这里。正在构建什么？有新闻要分享？希望我们报道您的项目？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">通过 NIP-17 私信联系我们</a>或在 Nostr 上找到我们。
