---
title: "NIP-101e：健身训练"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
categories:
  - Fitness
  - Discovery
---

NIP-101e 定义了一种训练事件格式，让健身追踪应用可以在 Nostr 上发布、分享和发现训练课程。该规范使用 kind 1301 事件，将课程指标（距离、时长、爬升、心率、卡路里、骑行踏频、来源应用）承载在结构化 tag 中，使客户端能够以正确的单位显示这些指标，把训练渲染为一张结构化卡片。

## 工作原理

一次 NIP-101e 训练是一个 kind 1301 事件，其结构化 tag 覆盖了来源应用所捕获的每一项指标。常见 tag 包括：

- `type`：训练项目（跑步、骑行、游泳、力量训练等）
- `distance`：数值和单位
- `duration`：以秒为单位的时长
- `elevation_gain`：数值和单位
- `start` 和 `end`：起止时间戳
- `heart_rate`：平均心率和最大心率
- `calories`：能量消耗
- `source`：发布应用的名称
- `t`：用于标签发现的话题 tag

`content` 字段承载一段可选的用户书写备注（相当于用户上传到 Strava 时附带的说明）。识别 kind 1301 的客户端会把结构化指标渲染为训练卡片；不识别的客户端会退回到把 `content` 字段当成普通 note 展示。

## 发现和信息流语义

NIP-101e 事件是普通的信息流事件，因此用户发布的训练会像其他帖子一样出现在关注者的时间线中。具备专门训练视图的客户端可以按作者或话题 tag 订阅 kind 1301 事件，构建训练日志、排行榜或社区挑战信息流。作者 pubkey 是训练的规范身份，因此读取他人训练数据的第三方应用继承与其他 Nostr 信息流相同的信任假设。

## 实现

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) 上线了 kind 1301 的训练渲染，包括主要指标、指标网格、骑行专用速度显示以及来源徽章（[PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184)，在 [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) 中重构）

---

**Primary sources:**
- [NIP-101e Specification](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - 添加 NIP-101e 健身训练支持（Kind 1301）
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - 使用主指标和指标网格重新设计训练展示

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/zh/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
