---
title: "Concord Protocol"
date: 2026-07-15
draft: false
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
categories:
  - Protocol
  - Messaging
---

Concord 是一个面向 Nostr 上端到端加密社区与频道的开放、MIT 许可协议，由 [CORD-01 至 CORD-07 规范](https://github.com/concord-protocol/concord)定义。[Vector](https://github.com/VectorPrivacy/Vector) 自 v0.4.0 起将其采纳为群聊功能的默认传输层，并在自己的发布说明中称之为「我们自定义的消息协议」，但该规范本身是独立于 Vector 发布的，并且已经有了独立实现。

## 工作方式

Concord 把 Discord 风格社区服务器通常承担的职责，拆分成无需信任任何人的若干部分：relay 只存储寻址到轮换标签的加密 blob；持有房间密钥才使一个人成为成员；而对角色、踢出和封禁的裁决权是一份根植于所有者身份的签名名册，由每个客户端在本地校验，而不是信任某个服务器去执行。每个持久事件都乘同一个三层信封：由该平面自己派生的流密钥签名的 kind 1059 wrap，其中包含由作者真实密钥签名的 seal，seal 中又包含承载功能事件的未签名 rumor。聊天消息 rumor 是一个普通的 kind 9 事件：

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

控制、聊天和访客留言流量各自拥有独立的 [NIP-59](/zh/topics/nip-59/) gift-wrap 平面，因此即便一个 relay 同时持有这三者，没有房间密钥也无法分辨控制消息、聊天消息与访客留言条目。该规范拆分为七份 CORD 文档：私密流（01）、社区与成员资格（02）、频道（03）、角色（04）、邀请（05）、用于切断被移除成员的重新分发密钥与重建（06），以及通过盲令牌中介实现的音视频（07）。成员资格本身没有服务端列表：能解密该平面的人就是成员；真正移除某人意味着把社区滚动到一个新的密钥纪元，并只交给留下的人，而不是从表里删掉一行。

## 它与 Marmot 的区别

Concord 与 [Marmot](/zh/topics/marmot/) 都在 Nostr 上解决加密群组消息，但用不同的密码学服务于不同形态的群组，Concord 项目自己的对比也明确指出了这一分野：Marmot 在 Nostr 之上叠加 [MLS](/zh/topics/mls/)，以获得前向保密性和被攻破后安全性，使用按设备的密钥包和有序提交，让整个群组步调一致地前进。这换来了强有力的保证，代价是随成员变动而增长的开销，很适合加入和退出都很少见的小型高风险群组。Concord 则给每个成员相同的房间密钥，并在移除成员时对整个房间重新分发密钥，而不是按每次提交做棘轮推进；它让出 MLS 的部分密码学保证，换来一个在社区增长到数百或数千名随意加入、流动频繁的成员时仍保持低成本的模型，而这正是 Discord 风格社区在现实中的形态。

## Vector 为何切换

Vector 自己的 [v0.4.0 发布说明](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)只把 Concord 描述为用于群聊的「我们自定义的消息协议」，没有直接说明理由。无论如何，它与 Concord 自己公开的设计动机是契合的：像 Vector 这样的客户端中的群聊，正是那种规模大、开放、成员频繁变动的场景，而 Marmot 按设备维护的 MLS 状态在这里成为更昂贵的路径，Concord 异步、可随时收拢的设计恰恰是为这种场景而建。[Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) 在群聊中弃用 Marmot 转向 Concord，已有的 Marmot 群聊历史在切换中没有迁移。四天后，[v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) 推出带隐私与稳定性改进的「Concord v2」。同一周内，[Amethyst 合并了自己的洁净室、线路兼容的 Concord 实现](https://github.com/vitorpamplona/amethyst/pull/3566)，而 Soapbox 的 Discord 风格客户端 [Armada](https://gitlab.com/soapbox-pub/armada) 早已作为参考实现，在同一份规范上构建其 Communities 功能。三个独立客户端在数天之内汇聚到同一份开放规范，是通往真正跨客户端互操作的快速路径，值得对照 Nostr 其余群聊客户端中有多少仍留在 Marmot 上来观察。

## 实现

- [Vector](https://github.com/VectorPrivacy/Vector) - 单一二进制、隐私优先的 Nostr 通讯工具；首个推出 Concord 的客户端，始于 v0.4.0
- [Armada](https://gitlab.com/soapbox-pub/armada)（Soapbox）- Discord 风格社区客户端；参考实现，后端位于独立的 `armada-relay` 仓库
- [Amethyst](https://github.com/vitorpamplona/amethyst) - 功能丰富的 Android 与多平台 Nostr 客户端；与 Armada 线路兼容的洁净室重新实现（[PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)）

---

**主要来源：**
- [Concord 协议规范（CORD-01 至 CORD-07）](https://github.com/concord-protocol/concord)
- [Vector v0.4.0 发布说明](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Vector v0.4.1 发布说明](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**提及于：**
- [Newsletter #31：Vector v0.4.0 将群聊从 Marmot 迁移到 Concord，Amethyst 数天后推出自己的 Concord 客户端](/zh/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31：Amethyst 推出面向端到端加密社区的洁净室 Concord 实现](/zh/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**另见：**
- [Marmot Protocol](/zh/topics/marmot/)
- [MLS (Message Layer Security)](/zh/topics/mls/)
- [NIP-46: Nostr Connect](/zh/topics/nip-46/)
