---
title: "ProofMode"
date: 2026-07-15
draft: false
translationOf: /en/topics/proofmode.md
translationDate: 2026-07-15
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/) 是由 Guardian Project、WITNESS 和 Okthanks 打造的开源媒体来源证明工具包，在拍摄的那一刻就为照片和视频附上可验证的真实性与保管链数据。它并非 Nostr 专用；携带 ProofMode 数据的 Nostr 客户端是在集成一个既有的外部标准，而不是新增一层协议。

## 工作方式

ProofMode 的 Capture 组件在拍摄过程中把来源元数据直接嵌入媒体文件，支持与 Content Authenticity Initiative（CAI）、Content Credentials（CR）和 C2PA 相同的互操作标准。独立的 Verify 组件检查音频、图像和视频文件，在这些元数据中查找 AI 生成或后期编辑的迹象；Preserve 组件则负责把底层证明数据冗余地存储在去中心化网络上，以便长期归档。Develop SDK 让应用无需自行构建来源证明格式即可集成拍摄与验证。

## 为何重要

对于 Nostr 视频或图像客户端来说，携带 ProofMode 数据意味着观看者拥有一种外部的、跨平台的方式，去核实某段媒体是否如其所称那样被拍摄、之后是否被悄然改动，而不必把发布客户端或 relay 当作信任来源。这一区别在片段被下载或重新编码的副本上体现得最明显：只有能够经受住下载以及客户端所加水印的来源数据，才能让文件离开生成它的应用之后，那份证明依然可核验。

## 实现

- [Divine](https://github.com/divinevideo/divine-mobile) - 短视频 Nostr 客户端；在带水印片段的下载过程中保留 ProofMode 来源数据

---

**主要来源：**
- [ProofMode](https://proofmode.org/)

**提及于：**
- [Newsletter #17](/zh/newsletters/2026-04-29-newsletter/)
- [Newsletter #31：Divine Mobile 1.0.16 带来更深入的视频编辑器、静态加密和 ProofMode 来源证明](/zh/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**另见：**
- [Blossom](/zh/topics/blossom/)
