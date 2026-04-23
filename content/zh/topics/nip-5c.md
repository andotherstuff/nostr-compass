---
title: "NIP-5C：Scrolls（WASM 程序）"
date: 2026-04-08
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - WASM
---

NIP-5C（此前名为 NIP-A5）定义了在 Nostr 上发布、发现和执行 WebAssembly 程序（“scrolls”）的约定。WASM 二进制以 Nostr event 的形式存储，因此任何客户端都可以抓取它们并在沙箱 runtime 中运行。

## 工作原理

开发者将 WASM 程序作为包含编译后二进制的 Nostr event 发布。客户端通过标准 Nostr 查询发现这些程序，从 event 中下载 WASM 二进制，并在沙箱化的 WebAssembly runtime 中执行。沙箱会阻止 scroll 直接访问宿主系统，只允许它使用 runtime 明确提供的能力。

## 使用场景

- **可移植计算**：在任何支持 WASM 执行的客户端上运行程序
- **去中心化应用分发**：无需 app store 也能发布和发现应用
- **可组合工具**：把多个 scroll 串联成更复杂的工作流

## 演示

一个[演示应用](https://nprogram.netlify.app/)展示了如何在浏览器中运行 scrolls，其中示例程序以 Nostr event 发布。

---

**主要来源：**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - Scrolls（WASM Programs）提案

**提及于：**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19：NIP-5D applets 提案](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-5D（Web Applets）](/zh/topics/nip-5d/)
- [NIP-5A（静态网站）](/zh/topics/nip-5a/)
