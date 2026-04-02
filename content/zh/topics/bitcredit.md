---
title: "Bitcredit"
date: 2026-03-25
translationOf: /en/topics/bitcredit.md
translationDate: 2026-04-01
draft: false
categories:
  - 金融
  - 商业
  - 基础设施
---

Bitcredit 是一个面向企业的电子票据贸易金融系统。其公开网站将 Bitcredit Core 介绍为用于发行、背书、支付和管理电子汇票的软件，而开源核心仓库则实现了 Nostr 传输层以及业务逻辑和持久化 crate。

## 工作原理

Bitcredit 将贸易信用建模为电子汇票（ebill）。买方发行一张带有未来到期日的电子汇票，持有人可以将其背书给另一家企业，最终持有人可以在到期时请求付款。

Bitcredit 网站还描述了一种基于铸币厂的流动性路径。持有人无需等待到期，可以向 Bitcredit 铸币厂请求报价，立即收到 ecash，然后使用该 ecash 向供应商或工人付款。

## 实现说明

`Bitcredit-Core` 仓库将系统拆分为多个 Rust crate。`bcr-ebill-core` 处理数据模型，`bcr-ebill-api` 包含业务逻辑，`bcr-ebill-persistence` 处理存储，`bcr-ebill-transport` 提供带有 Nostr 实现的网络传输 API。

这一架构很重要，因为 Bitcredit 不仅仅是一个网站或钱包流程。它是一个将传输、状态和结算逻辑分离为可复用组件的商业文档系统，还包括用于 Web 部署的 WASM 入口点。

## 近期工作

Compass 在 2026 年 3 月首次报道 Bitcredit，当时 `v0.5.3` 为票据支付操作和票据状态添加了 API 字段，并修复了匿名签名者的签名地址处理。随后的 `v0.5.4` 版本继续了该 API 工作，调整了 `BitcreditBillResult`，完善了支付和接受状态，并为可选字段添加了更明确的处理。

这些变更与更广泛的 Bitcredit 概念相比规模较小，但它们展示了实现的方向：更清晰的前端交互体验、更明确的票据生命周期状态，以及对匿名或持票人签名流程的更好处理。

---

**主要来源：**
- [Bitcredit 网站](https://www.bit.cr/)
- [Bitcredit：工作原理](https://www.bit.cr/how-it-works)
- [Bitcredit-Core 仓库](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Bitcredit-Core 文档索引](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846: Improve Status Flags and Add Payment Actions](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849: Fix signing address and signatory for anon signers](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**提及于：**
- [周刊 #13：Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
