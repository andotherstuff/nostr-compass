---
title: "NIP-36：敏感内容"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

NIP-36 定义了一个可选的 `content-warning` tag，可附带原因。客户端可以用它隐藏 event，直到读者主动显示其内容。该 event 仍然是公开的。

## 实现

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) 会解析该 tag 及其原因。[Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) 会依据读者的敏感内容设置处理，并提供显示内容的操作。[noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) 会在呈现警告之前检查警告偏好设置和展开状态。

---

**一手来源：**
- [NIP-36 规范](https://github.com/nostr-protocol/nips/blob/master/36.md)

**提及本文的内容：**
- [第 44 期通讯：显示前的内容警告](/zh/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**另请参阅：**
- [NIP-32：标注](/zh/topics/nip-32/)
