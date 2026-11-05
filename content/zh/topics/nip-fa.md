---
title: "Buzz NIP-FA：联合身份适配器"
date: 2026-10-21
draft: false
categories: ["NIPs"]
translationOf: /en/topics/nip-fa.md
translationDate: 2026-11-05
---

Buzz NIP-FA 是 Buzz 项目提出的一项可选规范草案，不属于官方 nostr-protocol/nips 仓库中已接受的 NIP。

它在 Nostr 客户端与企业身份适配器之间定义了一份与提供方无关的 HTTP 契约。用户在浏览器中登录后，适配器会为该用户持有一个会话。适配器签发项目本地的 Buzz NIP-FI 断言，将用户绑定到某个 Nostr 密钥，客户端则通过 [NIP-98](/zh/topics/nip-98/) 证明自己控制该密钥。[每条断言的有效期由运营者选择](https://github.com/block/buzz/pull/8934)，该有效期必须遵守中继所接受的签发方 maximum_assertion_age，且 exp 不得晚于适配器会话的过期时间。所选有效期决定了已撤销的密钥在中继重启后仍可能重新连接的时间上限，客户端不得仅因断言的有效期而拒绝该断言。NIP-FI 和官方 NIP 均保持不变。登录使用 S256 交接质询，以及位于 `127.0.0.1` 或 `[::1]` 上的回环回调，该回调接收一个一次性代码。OIDC 或 SAML 等上游系统位于适配器之后。哪些中继要求企业身份，则交由其他规范来确定。

主要来源：Buzz 仓库中的 [NIP-FA 规范](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)。

## 智能体凭证 {#agent-credentials}

Buzz 合并了一份[关于所有者授权智能体凭证的 NIP-FA 草案](https://github.com/block/buzz/pull/9015)，为所有者通过 NIP-OA 授权的智能体定义了授权许可、断言和撤销路由。授权许可来自 RFC 8693 令牌交换，该交换将所有者的会话与智能体提供的 [NIP-98](/zh/topics/nip-98/) 证明配对。获取断言时，智能体将授权许可作为 Bearer 令牌出示，并附上自己的证明，客户端会将断言的 `iss` 与授权许可的签发方进行核对。智能体证明仅可使用一次，且只用于授权许可和断言路由。撤销基于所有者的会话执行，无需智能体证明；撤销会作废智能体密钥及其授权许可，并断开该智能体的连接。授权许可的有效期由适配器策略决定。不受支持的授权条件会被拒绝，已撤销的密钥无法重新注册。NIP-FA 是 Buzz 的规范，不是已接受的 NIP。此次合并仅存在于源代码中，并未声称已在生产环境启用、已发布构建版本或已实现互操作。

## 主要来源 {#primary-sources}

- [Buzz NIP-FA：联合身份适配器](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [所有者授权的智能体凭证路由](https://github.com/block/buzz/pull/9015)

## 提及于 {#mentioned-in}

- [Nostr Compass #47：Buzz 智能体凭证](/zh/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [第 45 期简报](/en/newsletters/2026-10-21-newsletter/#buzz)
