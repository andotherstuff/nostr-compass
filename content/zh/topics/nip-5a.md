---
title: "NIP-5A：静态网站"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-01
draft: false
categories:
  - 协议
  - 托管
---

NIP-5A 定义了如何在 Nostr 密钥对下托管静态网站。网站作者发布签名的清单事件，将 URL 路径映射到 SHA256 内容哈希，主机服务器解析这些清单以从 Blossom 存储提供网站文件。

## 工作原理

该规范使用两种 event kind。Kind `15128` 是根网站清单，每个 pubkey 一个，作为该密钥的默认网站。Kind `35128` 是命名网站清单，由 `d` tag 标识，类似于子域名。每个清单包含 `path` tag，将绝对 URL 路径映射到应提供的文件的 SHA256 哈希。

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

主机服务器接收 HTTP 请求，从子域名中提取作者的 pubkey，从作者的 relay 列表获取网站清单，将请求路径解析为内容哈希，并从 `server` tag 中列出的 Blossom 服务器下载匹配的 blob。

## URL 解析

根网站使用 npub 作为子域名。命名网站使用原始 pubkey 的 50 字符 base36 编码，后跟 `d` tag 值，全部在单个 DNS 标签中。由于 DNS 标签限制为 63 个字符，且 base36 pubkey 始终使用 50 个字符，命名网站标识符限制为 13 个字符。

## 实现

- [nsite](https://github.com/lez/nsite) - 解析 NIP-5A 清单并提供文件的主机服务器
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 构建和发布网站清单的 UI

---

**主要来源：**
- [NIP-5A 规范](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - 原始提案和合并
- [nsite](https://github.com/lez/nsite) - 参考主机实现
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 发布和管理 UI

**提及于：**
- [周刊 #16：NIP-5A 合并](/zh/newsletters/2026-04-01-newsletter/#nip-5a-合并将静态网站引入-nostr)
- [周刊 #16：NIP 深度解析](/zh/newsletters/2026-04-01-newsletter/#nip-深度解析nip-5a静态网站)

**另见：**
- [Blossom](/zh/topics/blossom/)
- [NIP-65：Relay 列表元数据](/zh/topics/nip-65/)
- [NIP-96：HTTP 文件存储](/zh/topics/nip-96/)
