---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
translationOf: /en/newsletters/2026-08-05-newsletter.md
translationDate: 2026-08-06
draft: false
type: newsletters
description: "Sandstr 提供以模拟数据游览 Nostr 客户端的功能,nostr-mill 增加了按事件签名的同意机制,nostrord 扩展了中继托管群组。深度解析涵盖中继辅助搜索和可移植高亮。"
---

欢迎回到 [Nostr Compass](https://github.com/andotherstuff/nostr-compass),您的 Nostr 每周指南。

**本周:** [Sandstr](https://sandstr.app/) 让新用户无需创建密钥或安装应用即可探索模拟的 Nostr 客户端。[nostr-mill](https://github.com/0ceanSlim/nostr-mill) 增加了按事件的签名者同意和跨客户端密钥恢复,而 [nostrord](https://github.com/nostrord/nostrord) 扩展了中继托管群组、签名器、审核、上传和高亮功能。协议工作涵盖 Nostr 事件格式、钱包连接、中继发现、napplet、Marmot 和 Concord;深度解析将解释中继辅助搜索和可移植高亮。

## 头条新闻

### nostr-mill 1.6.0 将签名同意和账户恢复带入浏览器

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) 是一个可嵌入的浏览器账户选择器和签名器。它现在按事件 kind 请求同意,并在签名前显示解码后的内容和标签,具有限时授权和权限管理器。该版本还修复了一个首次会话的 bug,该 bug 导致配置为每次都询问的类别在未询问的情况下即可签名。其可选的 Google 入门流程可以导入现有的 `nsec`,将密钥加密存储在用户的 Drive 应用数据文件夹中,支持多个身份,并可导出 [NIP-49](/zh/topics/nip-49/)(加密私钥格式)的 `ncryptsec`。

[实验性中继备份](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0)使用 scrypt 和 HKDF 派生强恢复短语,将密钥包装为 `ncryptsec`,验证获取的事件,并在恢复前要求中继法定人数。[NIP-55](/zh/topics/nip-55/)(Android 签名器意图)登录现在使用 Amber 的剪贴板返回路径,[NIP-46](/zh/topics/nip-46/)(中继介导的远程签名)连接默认为静默。品牌控件和响应式权限界面为该版本画上句号,除非运营者选择启用,否则不会改变现有集成。

### nostrord 2.5.0 为中继群组提供稳定的、特定于中继的身份

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) 是一个面向中继托管社区的跨平台客户端。它现在从群组 ID 和托管中继共同派生 [NIP-29](/zh/topics/nip-29/)(中继管理群组)身份,以相同方式限定成员资格和管理员徽章,接受群组 `naddr` 深链接,并在设备间同步私人群组线程。

该[版本](https://github.com/nostrord/nostrord/releases/tag/v2.5.0)还增加了 [NIP-56](/zh/topics/nip-56/)(举报事件)审核收件箱、通过 NIP-55 的 Amber 登录、NIP-46 签名者流量的速率限制退避、具有未解析引用重试功能的 [NIP-84](/zh/topics/nip-84/)(可移植高亮)渲染,以及通过 Blossom 或 [NIP-96](/zh/topics/nip-96/)(HTTP 文件存储)的媒体上传。Google 登录现在在创建账户前备份密钥并确认断开连接。线程回复获得更丰富的内容和管理员删除功能,而桌面钥匙串和移动键盘的修复使这些协议功能保持可用。

### Primal Android 3.5.25 更新远程签名和关注列表过滤

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) 是一款具有信息流、搜索和远程签名功能的移动 Nostr 客户端。它更新了远程签名器以符合当前协议行为,添加了关注静音列表,从 Explore 打开搜索,自动修复停滞的中继连接,在界面中公开请求超时,拒绝无效的关注列表条目,并刷新备用中继 URL。信息流预取、更低的内存使用和 100 MB 缓存上限降低了保持这些信息流更新的成本。单图片笔记现在使用完整内容宽度,个人资料控件和媒体预加载获得了较小的交互和排序修复。

### Nostur 1.30.2 扩展私信中的私密回复和媒体

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) 是 Apple 平台的 Nostr 客户端。它始终显示私密回复操作,添加带限制和清除控件的按对话 DM 媒体缓存,改进帖子和聊天中的名称和标签补全,在实时聊天中显示被引用的消息,并在聊天通知中包含房间标题。信息流分页和嵌套回复的修复解决了检索和对话渲染的回退问题。

### Chama 5.7.0 添加仲裁员记录和缓存交易恢复

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) 通过签名的 Nostr 事件链协调点对点交易和仲裁。它显示仲裁员的锁定金额、保证金期限和资金输出点;记录备份何时替换缺席的仲裁员;并定义需要双方委托人签名的休眠 kind `38136` 故障证明。显式修复会针对持久设备缓存重试不完整的中继历史记录并重新发布恢复的事件,而失败的发布会排队等待下次连接。该版本还通过将作者的 kind `38113` 事件视为付款记录,防止跨设备重复的仲裁员溢价支付。

### Auditable Voting 0.1.165 恢复委托选票投递

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) 在将选民凭证与选票内容分离的同时进行可验证的投票。它通过经过身份验证的委托投递和控制 DM 回填恢复了委托盲选票的签发,将盲凭证私信保留在配置的私有中继上,并将审计代理更新到 0.1.52。

### Sandstr 让新用户用模拟数据试用 Nostr 客户端

[Sandstr](https://sandstr.app/) 提供 Nostr 客户端的交互式浏览器模拟,让新用户在安装客户端或创建密钥对之前可以比较它们的界面。其 8 月 3 日的发布包括 Damus、Amethyst、Primal、Snort、YakiHonne、Coracle 和 Wisp 的参考验证复制品,以及明确标记的 Gossip、Keychat 和 Olas 早期预览。一切都在本地针对模拟数据运行,因此模拟不会生成密钥或连接中继。每个模拟都链接到真实客户端的网站和源代码库,使 Sandstr 成为入门和界面比较工具,而不是另一个 Nostr 客户端。它展示了信息流、个人资料、线程、私信、搜索、zap 和中继控件的感觉,而无需首次用户预先做出身份或安全决定。


### mineracks signer 将浏览器扩展与桌面 bunker 配对

[mineracks signer](https://github.com/mineracks/mineracks-signer) 从同一项目提供两个签名界面。其浏览器扩展实现了 [NIP-07](/zh/topics/nip-07/),使 Web 应用无需接收私钥即可请求签名,而桌面应用程序为通过中继通信的客户端公开了 [NIP-46](/zh/topics/nip-46/) 远程签名器。

该项目的[桌面 0.1.0 版本](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0)使用 NIP-49 加密密钥编码存储密钥材料,并将解密后的密钥保留在 Rust 进程内,而不是传递给界面。每个请求都会显示调用应用程序和请求的操作,而按应用程序自动批准是可选且可撤销的。第一个桌面构建支持 Apple Silicon,但不支持 Intel Mac。

## 版本发布

### Jumble 26.8.1 添加工作量证明控件和评论预览

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) 是一个 Web 和桌面 Nostr 客户端。它记住发布时的工作量证明难度,显示已验证工作徽章,在外部内容上方预览链接的评论,从全屏查看器保存图片,并按需展开长篇个人简介。反应通知现在会丢弃不支持的事件 kind,中继断开通知不再那么嘈杂,默认中继已刷新,并修复了媒体自动播放冲突。

### nostr-calendar 2.1.0 恢复私密表单签名者绑定

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) 将日历、事件和表单响应发布为 Nostr 数据。它将私密表单提交绑定到活动签名器,将有意的重复事件保存到中继,修复中继获取,以本地时间解析日历日期,并添加应用通知以及 iOS 客户端。签名器修正防止了过时身份生成不可用的加密响应。

### Manent 2.0.0 为保存的笔记添加标记和搜索

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) 是签名 Nostr 笔记的个人存档。它添加了本地标签和搜索,让读者可以在不修改其签名内容的情况下组织和检索保存的事件。

### nosvelte 0.6.1 在 EOSE 后关闭空订阅

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) 为中继数据提供响应式 Svelte 组件和钩子。空搜索现在在 End of Stored Events 处完成,取消会关闭底层 `REQ`,重试会清除过期错误,列表钩子返回其文档化的空值。它还能识别地址化事件,无论其 `d` 标签出现在何处,替换被取代的元数据和文章,按事件 ID 对反应去重,并保留中继第一批次的所有事件。

## 未发布的更改

### NMP 将中继准入绑定到声明并扩展群组查询

[NMP](https://github.com/pablof7z/nmp) 是用于构建 Nostr 应用程序和中继支持的群组界面的 TypeScript 工具包。[PR #1254](https://github.com/pablof7z/nmp/pull/1254) 使中继准入跟随授权它的声明的所有者,使权限决定与签名的 Nostr 状态保持关联。[PR #1255](https://github.com/pablof7z/nmp/pull/1255) 推广了 [NIP-29](/zh/topics/nip-29/) 中继管理群组查询,而不是假设一种狭窄的查询形式。这两项更改均已合并,但尚未出现在带标签的版本中。

### Mosaico 从中继记录派生受管群组身份

[Mosaico](https://github.com/pablof7z/mosaico) 是用于浏览和管理中继管理社区的 Nostr 客户端。[PR #758](https://github.com/pablof7z/mosaico/pull/758) 从托管其权威记录的中继派生受管群组的身份。[PR #757](https://github.com/pablof7z/mosaico/pull/757) 在解析管理状态时观察群组发布的记录。这使得不同中继上两个名称相似的群组保持区分,并为客户端提供了管理元数据的中继支持来源。

### Divine 在多中继查询期间隔离慢速中继

[Divine](https://github.com/divinevideo/divine-mobile) 是一款通过 Nostr 发布和检索视频的移动短视频客户端。[PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) 为每个中继查询提供自己的超时,而不是让一个停滞的连接消耗整个请求的超时预算。因此,来自响应迅速的中继的结果可以在慢速端点被独立放弃时到达。该更改在不将某个中继视为组合结果的权威的情况下改进了检索。

### rust-nostr 强化加密、哈希和对账

[rust-nostr](https://github.com/rust-nostr/nostr) 是用于 Nostr 客户端、中继和协议实现的 Rust 库和工具包。[PR #1421](https://github.com/rust-nostr/nostr/pull/1421) 减少了其 [NIP-44](/zh/topics/nip-44/) 版本化加密路径中的分配,而 [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) 引入了类型化哈希,使意外混合不兼容的摘要值变得更加困难。[提交 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) 防止格式错误的 [NIP-77](/zh/topics/nip-77/) Negentropy 集合对账消息断开本地中继。合并的工作在下一个版本之前加强了加密负载处理和对账失败行为。

### Zeus 在扣除支出预算之前序列化 NWC 支付

[Zeus](https://github.com/ZeusLN/zeus) 是一款移动比特币和闪电网络钱包,可以通过 Nostr Wallet Connect 公开钱包操作。[PR #4305](https://github.com/ZeusLN/zeus/pull/4305) 将待处理的支付计入 [NIP-47](/zh/topics/nip-47/) Nostr Wallet Connect 预算,而不是等待结算。[PR #4303](https://github.com/ZeusLN/zeus/pull/4303) 序列化支付处理,使并发请求无法竞争通过同一授权限额。合并的一对关闭了钱包 Nostr 控制面上的预算执行缺口。

### Nostr Components 共享一次中继连接尝试

[Nostr Components](https://github.com/saiy2k/nostr-components) 是一个可重用的 Web 组件库,用于向应用程序添加 Nostr 数据和交互。[PR #105](https://github.com/saiy2k/nostr-components/pull/105) 允许同时挂载的组件共享正在进行的中继连接尝试。每个消费者仍然会收到结果连接,但并发挂载在第一次握手挂起时不再打开重复的套接字。该更改减少了由多个独立组件组装的应用程序中可避免的中继负载。

## NIP 更新和协议规范工作

### Nostr 事件格式和发现

[NIP PR #2430](https://github.com/nostr-protocol/nips/pull/2430) 提议将贴纸包作为地址化 kind `30031` 定义,将用户已安装的包作为可替换的 kind `10031`。每个贴纸标签带有一个短代码、SHA-256 哈希和 MIME 类型;图像保留在 [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md)(Blossom blob 存储)服务器上。因此,开放草案在不将图像字节放入事件的情况下标准化了包身份和安装。

[NIP PR #2429](https://github.com/nostr-protocol/nips/pull/2429) 提议 kind `31436` 地址化 Gopher 文档。每个事件持有一个 UTF-8 文本或菜单节点,同一 pubkey 下签名的节点构成一个 gopherhole,任何中继支持的 RFC 1436 桥都可以提供服务。开放提案使用普通的地址化事件存储,而不是将发布绑定到一个 Gopher 主机名。

[NIP PR #2428](https://github.com/nostr-protocol/nips/pull/2428) 提议按时代票证的私人群组。群组在时代之间轮换成员凭证,客户端出示当前时代的票证以参与。该草案针对私人聊天,而不要求中继将永久持票令牌视为终身会员资格。

上周作为提案报道的 [NIP PR #2425](https://github.com/nostr-protocol/nips/pull/2425) 现已将 URI 澄清合并到 [NIP-B0](/zh/topics/nip-b0/)(地址化网页书签)中。当书签将其目标存储在 `d` 标签中时,它区分省略的 HTTPS 前缀和显式 URI 方案,防止客户端重建不明确的目标。

### 支付和钱包连接

在 7 月 22 日期刊中作为提案报道的 [NIP PR #2419](https://github.com/nostr-protocol/nips/pull/2419) 现已合并了更小的 [NIP-47](/zh/topics/nip-47/)(Nostr Wallet Connect)核心。连接 URI、加密中继传输、能力发现、加密协商和常用方法保留在 NIP 中;通知、保留发票、keysend、交易历史、元数据和深链接配对移至专用扩展存储库。现有连接保持兼容,而钱包可以独立实现可选合约。

上周作为提案报道的 [NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2) 现已将 BIP-321 支付方式合并到该扩展存储库中。BIP-321 提供了一个可以承载不同通道的通用比特币支付 URI,因此 NWC 调用者可以请求或发送支付,而无需为每种底层指令类型添加新的核心 RPC。

### Napplet 宿主能力

[NAP PR #95](https://github.com/napplet/naps/pull/95) 提议为 Nostr 分布式沙盒应用程序提供目录发现。napplet 询问其宿主哪些应用程序和能力可用,宿主返回按策略过滤的元数据,而不是暴露其完整的本地环境。该合约支持启动决策,而无需在发现期间授予执行权限。

[NAP PR #33](https://github.com/napplet/naps/pull/33) 提议由 shell 介导的文件和 blob 上传。napplet 提供字节和意图;宿主选择 NIP-96 或 Blossom 通道,签署授权,报告进度,并返回 URL、哈希、MIME 数据和可直接附加的 [NIP-94](/zh/topics/nip-94/)(文件元数据)标签。存储凭证和 HTTP 权限永远不会进入 napplet。

### Marmot 加密群组

[Marmot PR #410](https://github.com/marmot-protocol/marmot/pull/410) 合并了收敛和延迟输入规则。客户端将缺少当前时代依赖项的对象与过时或无效的输入区分开来,使其在资源拒绝后仍有资格重新获取,并在另一个提交改变解密上下文时重试。域分离的状态承诺为一致性测试提供了共享的收敛预言机,而无需添加生产线路字段。

### Concord 社区平面

[Concord PR #14](https://github.com/concord-protocol/concord/pull/14) 合并了 CORD-08 消失消息。一个社区元数据值设置生命周期;聊天传闻和加密包装带有 [NIP-40](/zh/topics/nip-40/)(事件过期)标签,而删除事件和 kind `1740` 计时器通知则豁免。签名的计时器随社区状态一起传播,尽管中继删除仍然是保留请求而不是加密擦除保证。

[Concord PR #13](https://github.com/concord-protocol/concord/pull/13) 将防轮换置顶合并到 CORD-04 中。每个频道在控制平面上有一个完全替换的置顶列表;条目带有原始签名封印以及每条消息的 NIP-44 扩展密钥,允许新成员在不接收旧时代密钥的情况下验证作者和明文。私有列表可以保持密封到频道时代,上限约束列表大小,作者删除会在不分叉控制平面链的情况下移除置顶。

## NIP 深度解析

### 搜索能力(NIP-50)

[NIP-50](/zh/topics/nip-50/) 在[主要规范](https://github.com/nostr-protocol/nips/blob/master/50.md)中定义,为中继添加了可选的搜索过滤器。当客户端已经知道作者、事件 kind、标识符或标签时,普通的 Nostr 过滤器就可以工作;NIP-50 解决的是输入为诸如 `best nostr apps` 这样的人类查询时的发现问题。

[NIP-50 线路格式](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field)在 `REQ` 消息内的普通过滤器中添加了 `search` 字符串。请求可以将该字段与 `kinds`、`authors`、`ids`、标签过滤器和 `limit` 组合,一个 REQ 可以携带多个独立的过滤器。支持的中继应主要针对事件的 `content` 进行匹配,当事件 kind 有用时可以使用其他字段,并应在应用 `limit` 之前按自己的相关性分数排序。该顺序不同于通常的最新优先事件流。

查询字符串可以包含规范的 [`key:value` 扩展](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions)。它列出了 `include:spam`、`domain:`、`language:`、`sentiment:` 和 `nsfw:`;中继应忽略未实现的扩展。客户端通过中继的 [NIP-11](/zh/topics/nip-11/) `supported_nips` 字段发现声明的支持,但如果准备拒绝不相关的响应,仍然可以将过滤器发送到其他地方。

[NIP-50 规范](https://github.com/nostr-protocol/nips/blob/master/50.md)故意不标准化分词、词干提取、排名、语言检测、情感分析或垃圾邮件分类。两个兼容的中继可以对同一查询返回不同的事件和不同的排序。这使得中继成为索引和排名提供者,而不是真相来源。该规范建议查询多个支持的中继,检查返回的事件是否满足客户端的用例,并放弃结果精度差的中继。

这与精确的 [NIP-01 过滤](https://github.com/nostr-protocol/nips/blob/master/01.md)不同。`authors` 或 `#t` 过滤器具有客户端可以直接验证的确定性匹配语义,而搜索匹配可能依赖于索引和不透明的分数。NIP-50 保留了 NIP-01 的签名事件封套和中继传输,但接受召回率和排序的变化,以使开放式检索成为可能。

下面的事件是使用[七个 NIP-01 事件字段](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures)的示例性搜索结果。重复的十六进制值是占位符,而不是有效签名。

```json
{
  "id": "2943d6b43bcbf0ee4a8b4cac912111be0309607b8bb435ae40529989bea7f6c5",
  "pubkey": "3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d",
  "created_at": 1785771175,
  "kind": 1,
  "tags": [],
  "content": "I've been working on a customizable client (mostly relay feeds, but a ton of other things and subtle details too). It's called Hallway for reasons I don't remember and it's a fork of Fevela which is a fork of Jumble, but very rewritten for speed and simplicity...",
  "sig": "5b058b89dab9bd09d81bdc10eff95536125b87fbcbbc97f08d835c1272b2a3190cc3d340e42f54acb0d7e0e4b00355ab91292d0305c84a2d73b538319c0da12c"
}
```

当前的客户端在不同的发现界面中使用相同的过滤器。[Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) 将 NIP-50 搜索发送到专用搜索中继,[Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) 通过其中继池搜索事件,[NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) 协调用于长篇阅读的中继支持搜索。它们不同的结果处理反映了 NIP-50 留给中继和客户端的自由度。

### 高亮(NIP-84)

[NIP-84](/zh/topics/nip-84/) 由其[主要规范](https://github.com/nostr-protocol/nips/blob/master/84.md)定义,将 kind `9802` 分配给高亮。它将选定的段落或对非文本媒体的引用转变为可以在阅读、社交和注释客户端之间移动的签名事件。

[事件的 `content`](https://github.com/nostr-protocol/nips/blob/master/84.md#format) 包含选定的文本,当源是音频、视频或其他非文本媒体时可以为空。高亮通过 `a` 标签指向地址化事件或通过 `e` 标签指向普通事件的 Nostr 源;`r` 标签标识网页 URL。生成 URL 的客户端应在发布前删除跟踪和其他无用的查询参数,以便表面的 URL 变体不会分散对同一源的引用。

可选的 [`p` 标签](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution)将源归属于一个或多个 Nostr pubkey。它们的第四个值可以标识诸如 `author` 或 `editor` 之类的角色,而当仅有选择会不清楚时,`context` 标签可以保留周围的文本。引用高亮添加 `comment` 标签,而不是发布第二个 kind `1` 笔记:源的 `r` 标签获得 `source` 标记,而评论中提到的 pubkey 或 URL 带有 `mention`,让渲染器能够区分归属和用户的回应。

[kind `9802` 定义](https://github.com/nostr-protocol/nips/blob/master/84.md)使高亮成为常规事件而不是可替换事件。重复或更正选择会创建另一个签名事件,删除一个则依赖于正常的删除请求流程和中继保留策略。该规范没有定义字节偏移量、选择器或规范的文档快照,因此客户端可能无法在其网页源更改后重新定位段落。公开高亮还会暴露阅读兴趣;私人注释需要单独的加密和共享设计。

NIP-84 不同于 [NIP-23 长文事件](https://github.com/nostr-protocol/nips/blob/master/23.md),后者将整篇文章作为 kind `30023` 发布;高亮引用或指向可能保留在其他地方的材料。它也不同于 [NIP-51 书签集](https://github.com/nostr-protocol/nips/blob/master/51.md),后者存储可替换的引用集合。NIP-84 使每个选择都独立签名、可归属、可发现和可讨论。

这个示例性高亮包含[七个 NIP-01 事件字段](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures)。其标识符和签名是占位符。

```json
{
  "id": "0d57c07cfdfe8ec00711e2af88a666b61fc35c167b90b02dfb5db7ffba7b794a",
  "pubkey": "07367baec8e73c076b14e47fba3b0d5c014d559d7986a7172a79a8a64419d7c2",
  "created_at": 1785797755,
  "kind": 9802,
  "tags": [
    ["context", "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will be able to derive your nsec, read all your encrypted data and sign events as you."],
    ["alt", "This is a highlight created in https://primal.net iOS application"],
    ["a", "30023:1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139:nostr-quantum-preparation"],
    ["p", "1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139", "", "mention"]
  ],
  "content": "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will b",
  "sig": "219f3c1e572d1a087d667dc0d3a5443c77c0db3a5d42ce4e630604901ac63d2c879a86269d81e220bb77fd48b1579adafc333075e53c6eb0a108791fdd4a1622"
}
```

该格式已经跨越了客户端边界。[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) 本周添加了 NIP-84 渲染,[NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) 在其长文客户端中渲染高亮事件,[Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) 从选定的内容中发布它们。这些实现涵盖阅读、创建和社交渲染,而无需一个服务拥有注释。

---

通过 [Nostr Compass 项目](https://github.com/andotherstuff/nostr-compass)发送 NIP-17 DM 以分享项目或新闻。
