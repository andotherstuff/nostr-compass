---
title: "NIP-AC：P2P 语音和视频通话"
date: 2026-04-08
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - 通话
---

NIP-AC 提出了一套基于 Nostr 的点对点语音和视频通话协议。该规范使用 Nostr events 做通话信令（offer、answer、ICE candidates），并使用 WebRTC 进行实际的媒体传输，从而在保持去中心化通话建立流程的同时，复用浏览器现成的音视频 API。

## 工作原理

呼叫方发布一个包含 WebRTC Session Description Protocol（SDP）offer 的通话 offer event，并通过 tag 标明被叫方 pubkey。被叫方再返回一个 SDP answer event。双方随后交换 ICE candidate events 来协商网络路径。一旦 WebRTC 连接建立，媒体流就会在对等节点之间直接传输，而不再经过 relay。

这些信令 events 会被加密，因此 relay 无法观察是谁在呼叫谁。通话状态机会处理 offer、answer、reject、busy 和 hangup 等状态转换。

## 实现

- [Amethyst](https://github.com/vitorpamplona/amethyst) 正在构建 NIP-AC 支持，包括通话状态机测试套件和过期 call offer 处理。

---

**主要来源：**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - 基于 WebRTC 的 P2P 语音和视频通话

**提及于：**
- [Nostr Compass #17（2026-04-08）](/zh/newsletters/2026-04-08-newsletter/)

**另请参阅：**
- [NIP-44（加密载荷）](/zh/topics/nip-44/)
