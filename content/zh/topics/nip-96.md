---
title: "NIP-96：HTTP 文件存储"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 定义了 Nostr 客户端如何在 HTTP 媒体服务器上上传、下载和管理文件。目前已被标记为"不推荐"，建议使用 Blossom 替代，但在各项目过渡期间 NIP-96 仍然具有相关性。

## 工作原理

客户端通过获取 `/.well-known/nostr/nip96.json` 来发现文件服务器的功能，该文件返回 API URL、支持的内容类型、大小限制和可用的媒体转换。

上传时，客户端向 API URL 发送带有 NIP-98 授权头（证明上传者身份的已签名 Nostr event）的 `multipart/form-data` POST 请求。服务器返回 NIP-94 文件元数据结构，包含文件 URL、SHA-256 哈希、MIME 类型和尺寸。

下载使用 GET 请求到 `<api_url>/<sha256-hash>`，可选查询参数用于服务器端转换（如图像缩放）。删除使用带 NIP-98 认证的 DELETE 请求。用户发布 kind 10096 event 来声明其首选上传服务器。

## 弃用原因

NIP-96 将文件 URL 绑定到特定服务器。如果服务器下线，所有引用该服务器 URL 的 Nostr 笔记都会丢失其媒体。Blossom 反转了这一模式，将文件内容的 SHA-256 哈希作为规范标识符。任何托管相同文件的 Blossom 服务器都通过相同的哈希路径提供服务，默认使内容在服务器间可移植。

Blossom 还简化了 API：上传使用普通 PUT，下载使用 GET，授权使用签名的 Nostr event（而非 HTTP 头）。弃用于 2025 年 9 月通过 [PR #2047](https://github.com/nostr-protocol/nips/pull/2047) 完成。

## 过渡状态

nostr.build 和 void.cat 等服务器此前支持 NIP-96，已添加或迁移到 Blossom 端点。各客户端处于不同阶段：Angor v0.2.5 添加了 NIP-96 服务器配置，而 ZSP v0.3.1 则专门上传到 Blossom 服务器。这种共存将持续到剩余的 NIP-96 实现完成迁移。

kind 10096 服务器偏好 event 对 Blossom 服务器选择仍然有用。NIP-94 文件元数据（kind 1063 event）描述文件属性，与使用哪种上传协议无关。

---

**主要来源：**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**提及于：**
- [新闻通讯 #9：NIP 深入解析](/zh/newsletters/2026-02-11-newsletter/#nip-深入解析nip-96http-文件存储与向-blossom-的过渡)

**另见：**
- [Blossom 协议](/zh/topics/blossom/)
- [NIP-94：文件元数据](/zh/topics/nip-94/)
