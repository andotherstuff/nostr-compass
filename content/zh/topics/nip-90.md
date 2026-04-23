---
title: "NIP-90：Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 定义了 Data Vending Machines（DVMs），这是一套通过 Nostr 请求并交付付费计算工作的协议。

## 工作原理

客户在 `5000-5999` 范围内发布 job request events。每条请求都可以包含一个或多个 `i` tags 作为输入、`param` tags 作为特定 job 的配置、`output` tag 作为期望输出格式、`bid` 上限，以及用于指明回复应出现在哪些地方的 relay hints。服务提供者则以 `6000-6999` 范围内的对应结果 kind 进行响应，并且结果 kind 永远比请求 kind 高 `1000`。

结果会包含原始请求、客户的 pubkey，以及可选的 `amount` tag 或 invoice。提供者还可以发送 kind `7000` 的反馈 events，例如 `payment-required`、`processing`、`partial`、`error` 或 `success`，这样客户端就能在最终结果到来前展示进度。

## 支付与隐私

该协议有意把商业逻辑保持开放。提供者可以在开始工作前收费，也可以先返回样本后收费，或者在交付完整结果后收费。这种灵活性很重要，因为 DVM jobs 的范围从廉价的文本转换到昂贵的 GPU 计算不等，而不同提供者承担的支付风险也各不相同。

如果客户希望输入保持私密，请求可以把 `i` 和 `param` 数据移入加密的 `content`，并通过 `encrypted` tag 加上提供者的 `p` tag 做标记。这样可以防止 prompts 或源材料被 relay 观察者看到，但代价是客户必须明确指定某个提供者，而不能再向开放市场广播请求。

## 互操作说明

NIP-90 通过输入类型为 `job` 的 `i` tags 支持 job chaining，也就是一个结果可以继续作为后续请求的输入。这样就能在不发明独立 orchestration layer 的前提下实现多步流程。

提供者发现不在请求/响应循环本身之内。规范把支持的 job kinds 广告交给 [NIP-89：Recommended Application Handlers](/zh/topics/nip-89/) announcements，这也是客户端在发布请求之前发现 vendors 的方式。

---

**主要来源：**
- [NIP-90 Specification](https://github.com/nostr-protocol/nips/blob/master/90.md)

**提及于：**
- [Newsletter #11：NIP-AC DVM Agent Coordination](/zh/newsletters/2026-02-25-newsletter/)
- [Newsletter #19：Forgesworn toll-booth-dvm](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：Agent Reputation Attestations proposal](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-89：Recommended Application Handlers](/zh/topics/nip-89/)
