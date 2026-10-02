---
title: "拟议的 NIP-DB：域名服务绑定"
date: 2026-09-30
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-02
draft: false
categories:
  - Proposals
  - Networking
  - Identity
---

NIP-DB 是一项**开放提案**，用于把普通互联网域名绑定到以密钥寻址的服务。其 event kind 和措辞仍有待审查；本页并不把它当作已被接受的 Nostr 规范。

## 验证模型 {#verification-model}

提供服务的密钥可以发布一条已签名的声明，写明域名和服务。该提案描述了可选的 DNS 或 DNSSEC 证据、见证方证明，以及用于该域名下各名称的区域记录。签名能证明是哪个密钥发布了声明，但不能证明对域名的控制权。客户端在用某个绑定解析名称之前，必须通过 DNS 证据、受信任的见证方或此前已固定的密钥来验证该绑定。

[fips-pub-domains](/zh/topics/fips-pub-domains/) 是作者为 FIPS 网状网络提供的参考实现。其文档中记录的双节点测试和仅网状网络测试是维护者自行报告的实现证据。它们既不能结束该提案尚在进行的审查，也不能证明已有更广泛的部署。

---

**主要来源：**
- [开放的 NIP-DB pull request](https://github.com/nostr-protocol/nips/pull/2487)
- [作者草案及 event kind 占位符](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [参考实现与测试](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**提及于：**
- [第42期周刊：公共域名](/zh/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [第42期周刊：拟议的 NIP-DB](/zh/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
