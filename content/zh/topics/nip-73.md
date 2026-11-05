---
title: "NIP-73：外部内容 ID"
date: 2026-02-04
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
---

NIP-73 定义了在 Nostr 事件中引用外部内容的标准方式。它用 `i` 标签承载标识符本身，用 `k` 标签表示标识符类型，使客户端能够围绕同一本书、网站、播客单集、地点、话题标签或区块链对象归集讨论。[当前规范](https://github.com/nostr-protocol/nips/blob/master/73.md)被标记为草案（draft）且可选（optional）。

## 工作原理 {#how-it-works}

使用 NIP-73 的事件包含一个 `i` 标签和一个 `k` 标签，前者存放经过规范化的外部标识符，后者指明标识符所属的类别。客户端可以通过 `i` 向中继查询某个确切主题，也可以通过 `k` 查询整个类别。NIP-73 本身不新增任何事件 kind。这些标签由评论、评价和其他事件携带。

标签片段，并非完整事件：

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

网页将其规范化 URL 放入 `i`，并将 `k` 设为 `web`。该规范涵盖多个标识符类别，包括：

- 不含片段（fragment）的规范化网页 URL
- 书籍的 ISBN
- 电影的 ISAN
- DOI
- geohash 以及 ISO 3166 国家或次级行政区代码
- 播客 feed、单集和发布者的 GUID
- 话题标签
- 区块链交易和地址标识符

## 规范化规则 {#normalization-rules}

匹配依赖于完全相同的字符串，因此规范为每个类别规定了唯一的书写形式。规范中的示例：

- geohash 使用 `geo:<value>`，且必须为小写
- 国家和次级行政区代码使用 `iso3166:<code>`，且必须为大写
- ISBN 省略连字符
- DOI 为小写
- 网页 URL 去掉片段
- 区块链交易哈希使用小写十六进制

规范化确定的是单个标识符的书写方式，并不合并别名。特定版本的 ISBN，以及规范化后得到不同字符串的 URL，仍是彼此独立的标识符，因此关于同一本书或同一篇文章的讨论仍可能分散在多个 `i` 值之下。

## URL 提示 {#url-hints}

`i` 标签可以在数组的第三个元素中包含一个可选的 URL 提示，即标签名之后的第二个值。对于某种标识符类型没有自定义渲染器的客户端，可以将该提示用作后备链接。

标签片段：`["i", "isbn:9780765382030", "<url-hint>"]`

提示由作者选择。它不属于标识的一部分，不证明任何所有权，也不指定规范站点。

## 信任与上下文 {#trust-and-context}

带有相同标识符的两个事件会进入同一个对话，共享标识符的作用仅此而已，不能证明其他任何事情。签名事件标识的是其作者。它不能认证所引用的书籍、网站或播客发布者，也不能表明谁控制着它们。

`i` 标签的含义取决于所在的事件。在 [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) 评论中，大写的 `I`/`K` 标记根作用域，小写的 `i`/`k` 标记父级。这种线程结构来自 NIP-22，NIP-73 并未定义评论 kind。[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) 在个人资料中使用 `i` 表示外部身份，因此并非所有 `i` 标签都是 NIP-73 主题。

[NIP-85](/zh/topics/nip-85/) 可信断言（Trusted Assertions）也可以以 NIP-73 标识符为目标，例如书籍、网站、话题标签和地点。

## 实现 {#implementations}

rust-nostr 的[提交 4c8099a 中的 nip73.rs](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) 将已知前缀解析为类型化的 `ExternalContentId`，并将可选提示转换为类型化 URL。只有存在提示时，它才写入标签的第三个元素。其测试保留了带连字符的 ISBN：解析器去掉前缀后原样存储其余部分，不应用规范中的规范化，因此类型化解析并不保证得到规范字符串。它不把链 ID 纳入类别，而是将 `ethereum:100:tx:<hash>` 映射为 `ethereum:tx`。该版本没有 `iso3166` 国家变体。

Amethyst 的[提交 553f761 中的 DisplayExternalId.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) 将 geohash、话题标签和 URL 标识符交给专门的显示组件，其他受支持的类型则显示为通用的作用域标签片。URL 会打开应用内针对该页面的线程路由。禁用预览时，常规渲染只显示一个纯链接标签片，不请求预览。启用预览时，获取缺失的预览可能会联系目标站点。这两个文件都不能说明已发布版本的行为。

---

**主要来源：**
- [NIP-73 规范](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - 新增 ISO 3166 国家和次级行政区代码
- [提交 4c8099a 中的 rust-nostr nip73.rs](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [提交 553f761 中的 Amethyst DisplayExternalId.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**提及于：**
- [简报 #47：NIP 深度解析](/zh/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [简报 #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [简报 #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [简报 #37：2025 年 8 月](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [简报 #8：NIP 更新](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [简报 #10：NIP-85 深度解析](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [简报 #36：评论（NIP-22）](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [简报 #38：NIP 深度解析](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [简报 #40：NIP-73 播客 medium 过滤器](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [简报 #42：2024 年 9 月外部内容](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**另请参阅：**
- [NIP-31：处理未知事件 kind](/zh/topics/nip-31/)
- [NIP-22：评论](/zh/topics/nip-22/)
- [NIP-39：个人资料中的外部身份](/zh/topics/nip-39/)
- [NIP-85：可信断言](/zh/topics/nip-85/)
