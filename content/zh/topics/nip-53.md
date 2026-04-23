---
title: "NIP-53：Live Activities"
date: 2026-04-15
translationOf: /en/topics/nip-53.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - 直播
---

NIP-53 定义了 Nostr 上直播元数据的标准 event 格式。一个直播会以 kind `30311` 的可寻址 event 发布，这样客户端就能发现它、展示当前状态，并把聊天与该直播上下文关联起来。

## 工作原理

每场直播都使用一个带有 `d` tag 的 kind `30311` event 作为稳定标识。该 event 通常包含标题与摘要文本、带播放 URL 的 `streaming` tag，以及 `status` tag（`planned`、`live` 或 `ended`）。由于它是可寻址 event，同一个 `d` 值的更新会替换旧元数据，而不是生成无限增长的 event 轨迹。

该 event 还可以带有主题标签 `t`、参与者引用 `p`，以及可选的参与人数字段。实时聊天通过 kind `1311` event 承载，并使用 `a` tag 引用该直播，从而让聊天消息始终绑定到某一条具体的 live activity 记录。

## 实现

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) 发布直播元数据，并围绕 Nostr 原生直播提供聊天功能。
- [Zap.stream](https://zap.stream/) 使用 Nostr events 做直播发现与互动。
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) 在其互联网广播场景中使用 kind `1311` 的直播聊天 event。
- [Amethyst](https://github.com/vitorpamplona/amethyst) 通过 [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) 将 [NIP-75](/zh/topics/nip-75/) zap goals 接入 Live Activities 页面：每场直播都带有筹款目标头部、进度条、一键 zap 按钮，以及基于绑定到该直播 kind `30311` event 的 kind `9735` zap receipt 计算出的 top zappers 排行榜。后续的 [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) 增加了 NIP-53 proof-of-agreement 与 event builders，[PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) 则带来了带筛选与发现功能的专门 Live Streams 信息流页面。
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) 增加了从直播卡片一键 zap 的能力，sats 会通过 NIP-53 出现在直播聊天覆盖层中。

---

**主要来源：**
- [NIP-53 规范](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - 直播目标头部与 top zappers 排行榜
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - NIP-53 proof of agreement 与 event builders

**提及于：**
- [Newsletter #18：WaveFunc 发布](/en/newsletters/2026-04-15-newsletter/)
- [Newsletter #19：Amethyst 直播 zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-29：基于 relay 的群组](/zh/topics/nip-29/)
- [NIP-75：Zap Goals](/zh/topics/nip-75/)
- [NIP-57：Zaps](/zh/topics/nip-57/)
- [NIP-C7：聊天消息](/zh/topics/nip-c7/)
