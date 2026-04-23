---
title: "NIP-94：文件元数据"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-04-22
draft: false
categories:
  - Media
  - Protocol
---

NIP-94 定义了一种文件元数据 event（kind 1063），用于在 Nostr 上组织和分类共享文件，从而让 relays 能更有效地过滤和整理内容。

## 工作原理

NIP-94 使用 kind `1063` 作为文件的独立元数据 event。event 的 `content` 存放人类可读描述，而 tags 则承载机器可读字段，例如下载 URL、MIME type、哈希、尺寸以及预览提示。

这种分离很重要，因为元数据 event 可以独立于任何链接到该文件的 note，被索引、过滤和复用。客户端可以把 kind `1063` event 当作某个资产的规范描述，而不必从自由格式的帖子文本中去抓取元数据。

## 必填与可选 Tags

**核心 tags：**
- `url` - 文件下载链接
- `m` - MIME type（要求使用小写格式）
- `x` - 文件的 SHA-256 哈希

**可选 tags：**
- `ox` - 服务器转换之前原始文件的 SHA-256 哈希
- `size` - 文件大小（字节）
- `dim` - 图片或视频尺寸（宽 x 高）
- `magnet` - 用于 torrent 分发的 Magnet URI
- `i` - torrent infohash
- `blurhash` - 预览占位图
- `thumb` - 缩略图 URL
- `image` - 预览图 URL
- `summary` - 文本摘要
- `alt` - 无障碍描述
- `fallback` - 备用下载源
- `service` - 存储协议或服务类型，例如 NIP-96

`ox` 与 `x` tags 很容易被忽略，但在实践里非常有用。`ox` 标识的是原始上传文件，而 `x` 标识的则可以是服务器实际提供的转换后版本。当媒体主机对上传内容做压缩或缩放时，客户端仍然可以保留“原始文件身份”，而不必假装转换后的 blob 与原件逐字节一致。

## 何时使用

NIP-94 更偏向文件共享应用，而不是社交客户端或长文客户端。适用场景包括：

- torrent 索引 relays
- 作品集分享平台（类似 Pinterest）
- 软件配置与更新分发
- 媒体库和档案系统

如果文件元数据只是为了装饰嵌在其他 event 里的 URL，那么 [NIP-92：媒体附件](/zh/topics/nip-92/) 会更轻量。只有当文件本身需要作为可查询的一等对象时，NIP-94 才是更好的选择。

## 互操作说明

NIP-94 可以跨不同存储后端工作。文件既可以通过 [NIP-96：HTTP File Storage](/zh/topics/nip-96/)、Blossom 或其他服务上传，然后仍然用同样的 kind `1063` event 结构来描述。这也是为什么这种元数据格式比任何单一上传协议活得都更久。

---

**主要来源：**
- [NIP-94 Specification](https://github.com/nostr-protocol/nips/blob/master/94.md)

**提及于：**
- [Newsletter #3：December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #14：NIP Deep Dive](/zh/newsletters/2026-03-18-newsletter/)

**另请参阅：**
- [NIP-92：媒体附件](/zh/topics/nip-92/)
- [Blossom](/zh/topics/blossom/)
