---
title: "提议中的 NIP-82（未分配）：软件应用目录"
date: 2026-06-17
lastmod: 2026-10-28
translationOf: /en/topics/nip-82.md
translationDate: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

本页介绍的软件应用目录是一项正在审议中的提案，并非已被接受的 NIP。它位于 [nostr-protocol/nips 拉取请求 #2526](https://github.com/nostr-protocol/nips/pull/2526) 中，标题为“Zapstore spec”。截至本页最后一次更新，该拉取请求仍处于开放状态且尚未合并，官方 NIPs master 分支中也没有 `82.md` 文件。“NIP-82”是该提案给自己使用的标签，并不是官方 NIP 编号。在任何合并发生之前，event kind、tag 和行为都可能发生变化。该拉取请求称，它取代了更早的[拉取请求 #1336](https://github.com/nostr-protocol/nips/pull/1336)。

## 提议的 event kind

该草案将软件目录划分为几种 event：

- **Kind 32267，应用：** 描述一个应用的可寻址 event。
- **Kind 30063，发布版本：** 对应该应用某一个版本的可寻址 event，引用该版本的资源文件。
- **Kind 3063，资源：** 描述一个可下载文件的常规 event。
- **Kind 30267，精选：** 由策展人发布、用于对应用进行分组或推荐的可寻址列表。
- **Kind 30509，签名证书关联：** 一种可寻址 event，用于将 X.509 证书（例如 APK 签名证书）与发布软件的 Nostr 密钥关联起来，让客户端知道该发布者控制着哪些证书。其 `d` tag 是 DER 编码证书的 SHA-256 哈希。它携带一个用证书私钥生成的签名，以及一个以 Unix 时间戳表示的过期时间，还可以选择将该关联标记为已撤销。
- **Kind 10067，relay 列表：** 一个可替换列表，列出可以找到目录 event 的 relay。

## 平台、完整性与有效性

资源 event 携带平台和运行时标识符，因此客户端可以只显示与设备匹配的文件。每个资源还带有一个文件哈希。客户端可以借助它检查下载得到的字节是否与发布者签名的内容一致。对于 Android 软件包，草案包含了签名证书指纹。在提供更新之前，安装程序可以将其与已安装应用的证书进行比对。安装 Android 软件包之前，客户端应当（SHOULD）按证书哈希获取 kind 30509 event。它们应当对照 APK 中内嵌的证书以及该资源的发布者来验证其证书签名，并检查该证明既未过期，也未被撤销。

## 信任限制

有效签名只能表明某个特定密钥发布了某个 event。它既不能证明该密钥属于真正的开发者，也不能证明软件是安全的，更不能证明某位策展人的列表值得信任。对于任意发布者，该提案不作任何保证。依赖哪些发布者和策展人的密钥，必须由客户端和用户自行决定。本页并不声称已进行过任何安全审计，也不声称已实现生产环境互操作。

## 与 NIP-89 的关系

[NIP-89](/zh/topics/nip-89/) 的 handler event 用于宣告哪些应用能够处理哪些 event kind。本提案描述的则是软件制品本身以及获取它们的位置，因此两者关注的是不同的问题。

---

**主要来源：**
- [nostr-protocol/nips PR #2526：Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526)（开放中，未合并；取代 [PR #1336](https://github.com/nostr-protocol/nips/pull/1336)）

**提及于：**
- [第 27 期简报：Amethyst v1.12.0 版本发布报道（历史参考）](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [第 46 期简报：软件应用目录被提议为 NIP-82](/zh/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**另请参阅：**
- [NIP-89：应用处理程序](/zh/topics/nip-89/)
