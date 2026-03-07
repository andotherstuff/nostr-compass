---
title: "NIP-96：HTTP 文件存储"
date: 2026-02-11
draft: false
translationOf: /en/topics/nip-96.md
translationDate: 2026-03-07
categories:
  - NIPs
  - Media
---

NIP-96 定义了 Nostr 客户端如何在 HTTP 媒体服务器上上传、下载和管理文件。该规范现已标记为"不推荐"以支持 Blossom，但由于现有服务器和客户端在过渡期间仍继续支持它，因此仍然重要。

## 工作原理

客户端通过获取 `/.well-known/nostr/nip96.json` 来发现文件服务器的功能。该文档公告上传 API URL、可选的下载 URL、支持的内容类型、大小限制，以及服务器是否支持媒体转换或委托托管。

要上传文件，客户端向 API URL 发送带有 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) 授权头的 `multipart/form-data` POST 请求。服务器返回一个 NIP-94 格式的元数据对象，包含文件 URL 以及 `ox`（原始哈希）等标签，适用时还包含 `x`（实际提供的转换后文件）。

下载使用 `GET <api_url>/<sha256-hash>` 加可选查询参数（如图片宽度）。删除使用带 NIP-98 认证的 `DELETE`。用户发布 kind `10096` 事件来声明首选上传服务器。

## 数据模型细节

一个有用的细节是 NIP-96 通过原始文件哈希标识文件，即使服务器对上传进行了转换。这让客户端可以通过相同的稳定标识符删除或重新下载资产，同时在可用时仍能获得服务器生成的缩略图或重新压缩的版本。

well-known 文档还支持 `delegated_to_url`，允许中继将客户端指向单独的 HTTP 存储服务器。这使得中继软件无需自行实现完整的媒体 API。

## 弃用原因

NIP-96 将文件 URL 绑定到特定服务器。如果服务器宕机，所有引用该服务器 URL 的 Nostr 笔记都会丢失其媒体。Blossom 反转了这一模式，将文件内容的 SHA-256 哈希作为规范标识符。任何托管相同文件的 Blossom 服务器都在相同的哈希路径下提供该文件，默认使内容可跨服务器迁移。

Blossom 还简化了 API：上传使用纯 PUT，下载使用 GET，授权使用签名的 Nostr 事件（而非 HTTP 头）。弃用发生在 2025 年 9 月，通过 [PR #2047](https://github.com/nostr-protocol/nips/pull/2047)。

## 互操作说明

nostr.build 和 void.cat 等服务器支持 NIP-96，并已添加或迁移到 Blossom 端点。各客户端处于不同阶段：Angor v0.2.5 添加了 NIP-96 服务器配置，而 ZSP v0.3.1 则专门上传到 Blossom 服务器。共存将持续到剩余的 NIP-96 实现完成迁移。

Kind 10096 服务器偏好事件对于 Blossom 服务器选择仍然有用。NIP-94 文件元数据（kind 1063 事件）描述文件属性，与使用哪种上传协议无关。

---

**主要来源：**
- [NIP-96：HTTP 文件存储](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047：标记 NIP-96 为不推荐](https://github.com/nostr-protocol/nips/pull/2047)

**提及于：**
- [Newsletter #9：NIP 深度解析](/zh/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-and-the-transition-to-blossom)

**另请参阅：**
- [Blossom 协议](/zh/topics/blossom/)
- [NIP-94：文件元数据](/zh/topics/nip-94/)
