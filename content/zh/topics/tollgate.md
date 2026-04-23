---
title: "TollGate：基于 Nostr 和 Cashu 的按量付费互联网接入"
date: 2026-04-22
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGate 是一种以小额、高频的不记名资产支付来出售网络接入的协议。任何能够控制连接的设备，例如 WiFi 路由器、以太网交换机或 Bluetooth tether，都可以充当 TollGate，发布价格、接受 [Cashu](/zh/topics/cashu/) ecash tokens，并管理会话。客户只需为自己实际使用的分钟数或流量付费。没有账户、没有订阅、没有 KYC。

## 工作原理

TollGate 将职责拆成三层。协议层定义 event 形状和支付语义。接口层定义客户和 gate 如何交换这些 events。介质层描述实际承载付费流量的物理链路。一个可运行的 TollGate 会从每一层各选一个规范组合而成，其中有些接口运行在 Nostr relays 之上，有些则运行在普通 HTTP 之上。

在协议层，[TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) 定义了三类基础 events：用于列出价格和支持 mint 的 Advertisement、用于追踪客户已支付额度与已消费量的 Session，以及用于带外消息的 Notice。[TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) 则在其上叠加了 Cashu 支付，因此客户可以从 TollGate 所广告的任意 mint 赎回 ecash token，并换取会话额度。

在接口层，[HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) 到 HTTP-03 定义了一套 HTTP 表面，面向那些受限操作系统中的设备，这些设备难以轻松地向任意 relay 打开 WebSocket 连接；而 [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) 则定义了面向能够使用 WebSocket 的客户端的 Nostr-relay 传输层。在介质层，[WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) 描述了 captive portal 式 WiFi 场景中如何识别并路由已付款用户。

因为支付资产是不记名 token，而不是账户凭证，客户不需要先拥有互联网接入才能生成它。只要本地 Cashu 钱包里已有 token，就足以买到第一分钟连接，之后再按需继续充值。多个 TollGate 之间也可以相互购买 uplink，因此覆盖范围可以超出单一运营者。

## 为什么重要

传统的付费 WiFi 依赖账户、captive portal 和支付卡，这些都会带来摩擦和数据痕迹。TollGate 的模型把连接能力变成了任何路由器都能出售、任何付费客户都能购买、且双方互不需要知道对方身份的商品。这一抽象使独立运营者可以自由定价、接受自己偏好的 mint，并在覆盖范围和服务质量上竞争，而不是靠锁定用户获胜。

[v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) 是这一组规范的第一个带 tag 快照。它还没有标准化所有细节，但已经固定了足够多的接口面，使路由器固件、客户端钱包和多跳转售方可以开始围绕一个稳定参考来构建。

---

**主要来源：**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: Base Events](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: Cashu payments](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 through HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [TollGate repository](https://github.com/OpenTollGate/tollgate)

**提及于：**
- [Newsletter #19：TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [Cashu](/zh/topics/cashu/)
- [NIP-60：Cashu Wallet](/zh/topics/nip-60/)
