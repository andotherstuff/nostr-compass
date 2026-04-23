---
title: "NIP-5A：静态网站"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5A 定义了如何在 Nostr keypairs 之下托管静态网站。站点作者发布已签名的 manifest events，把 URL 路径映射到 SHA256 内容哈希，而 host server 则解析这些 manifests，并从 Blossom 存储中把站点文件提供出来。

## 工作原理

该规范使用两种 event kinds。kind `15128` 是 root site manifest，每个 pubkey 对应一个，作为该 key 的默认网站。kind `35128` 是 named site manifest，通过 `d` tag 标识，作用类似子域名。每个 manifest 都包含 `path` tags，把绝对 URL 路径映射到应被提供文件的 SHA256 哈希。

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

host server 接收到 HTTP 请求后，会从子域名中提取作者 pubkey，从作者的 relay list 中抓取 site manifest，把所请求路径解析成内容哈希，然后从 `server` tags 列出的 Blossom server 中下载对应 blob。

## URL 解析

root sites 以 npub 作为子域名。named sites 则使用原始 pubkey 的 50 字符 base36 编码，再接上 `d` tag 的值，合并进同一个 DNS label。由于 DNS label 最长只能有 63 个字符，而 base36 pubkey 固定占用 50 个，因此 named site 的标识符最多只能有 13 个字符。

## 实现

- [nsite](https://github.com/lez/nsite) - 解析 NIP-5A manifests 并提供文件的 host server
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 用于构建和发布 site manifests 的 UI

---

**主要来源：**
- [NIP-5A Specification](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - 最初提案与合并
- [nsite](https://github.com/lez/nsite) - 参考 host 实现
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - 发布与管理 UI

**提及于：**
- [Newsletter #16：NIP-5A merges](/zh/newsletters/2026-04-01-newsletter/)
- [Newsletter #16：NIP Deep Dive](/zh/newsletters/2026-04-01-newsletter/)
- [Newsletter #19：NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [Blossom](/zh/topics/blossom/)
- [NIP-65：Relay List Metadata](/zh/topics/nip-65/)
- [NIP-96：HTTP File Storage](/zh/topics/nip-96/)
