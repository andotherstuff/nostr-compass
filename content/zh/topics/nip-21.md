---
title: "NIP-21：nostr: URI 方案"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocol
  - Interoperability
---

NIP-21 定义了 `nostr:` URI 方案，为应用、网站和操作系统提供了一种标准方式，用于注册并打开 `npub`、`nprofile`、`nevent` 和 `naddr` 等 Nostr 标识符，交由用户已注册为处理器的 Nostr 客户端接管。

## 工作原理

`nostr:` URI 由方案前缀加上任意一种 [NIP-19](/zh/topics/nip-19/) bech32 标识符组成，但不包括 `nsec`。客户端和操作系统对待这个方案的方式与 `mailto:` 或 `tel:` 类似：注册为处理器后，用户就可以在系统任意位置点击 `nostr:` 链接，并在自己选择的 Nostr 客户端中打开它。

规范中的示例包括：

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` 指向用户资料
- `nostr:nprofile1...` 指向带 relay 提示的用户资料
- `nostr:nevent1...` 指向带 relay 提示的特定 event
- `nostr:naddr1...` 指向参数化可替换 event（例如长文文章）

## 将 HTML 页面与 Nostr 实体关联

NIP-21 还为与 Nostr 实体对应的网页规定了两个有用的 `<link>` 约定。如果一个页面提供的内容与某个 Nostr event 相同，例如由 [NIP-23](/zh/topics/nip-23/) `kind:30023` 文章渲染出的博客页面，它可以包含一个指向该 Nostr URI 的 `<link rel="alternate">`。个人资料页面则可以包含指向 `nprofile` 的 `<link rel="me">` 或 `<link rel="author">`，以声明基于 Nostr 的作者身份。

## 重要意义

这个方案是互操作层，使任何 Nostr 标识符都能在单个客户端 UI 之外成为可用链接。浏览器扩展、移动操作系统处理器和桌面外壳都可以把 `nostr:` URI 路由到用户已安装的客户端，因此你可以在任何地方粘贴某个资料或 event 的 URI，同时仍保留以 Nostr 原生方式打开它的能力。

## 实现

`nostr:` URI 的支持已广泛存在于客户端生态中，包括主要的 Web、移动端和桌面端 Nostr 客户端。诸如 [nos2x](https://github.com/fiatjaf/nos2x) 和 [Alby](https://github.com/getAlby/lightning-browser-extension) 这样的浏览器扩展，也会在桌面浏览器中处理 URI 注册。

---

**主要来源：**

- [NIP-21 规范](https://github.com/nostr-protocol/nips/blob/master/21.md)

**提及于：**

- [第19期周刊：Nostrability 迁移到 NIP-34](/zh/newsletters/2026-04-22-newsletter/#nostrability-migrates-to-nip-34-and-opens-19-per-nip-interop-trackers)

**另请参阅：**

- [NIP-19：Bech32 编码实体](/zh/topics/nip-19/)
- [NIP-23：长文内容](/zh/topics/nip-23/)
