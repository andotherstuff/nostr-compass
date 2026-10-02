---
title: "FIPS 公共域名"
date: 2026-09-30
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-02
draft: false
categories:
  - Protocol
  - Networking
  - Identity
---

fips-pub-domains 是一个早期实现，用于把常见的互联网域名解析到 [FIPS](/zh/topics/fips/) 网状网络服务。它会发布经过签名的 Nostr 声明，但签名只能证明是谁发出了声明。在把声明者视为域名所有者之前，客户端还必须检查 DNS 或 DNSSEC 证据、受信任的见证方，或此前已固定的绑定。

## 验证与离线使用 {#verification-and-offline-use}

[首个版本](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0)加入了声明、解析器守护进程和 Android 集成。[0.2.0 版本](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0)可以在声明中附带 DNSSEC 证明，使只能看到网状网络 relay 的客户端也能依据 DNS 根密钥验证一个此前未见过的已签名域名。它还支持同一域名对应多台经过验证的服务器。[0.2.1 版本](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1)修复了打包的服务器单元，并将其改为无需 root 运行；现有安装需要替换为新的单元文件。

该项目的[测试说明](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)描述了双节点和仅网状网络 relay 的场景。这些是维护者自行报告的测试，并不能证明已有更广泛的部署。其 [NIP-DB 提案](https://github.com/nostr-protocol/nips/pull/2487)仍处于开放状态，草案中的 event kind 编号只是占位符，而非已分配的 Nostr kind。

---

**主要来源：**
- [仓库和 README](https://github.com/fr34aky/fips-pub-domains)
- [0.1.0–0.2.1 版本](https://github.com/fr34aky/fips-pub-domains/releases)
- [拟议的 NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [测试说明](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**提及于：**
- [第42期周刊：fips-pub-domains](/zh/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**另请参阅：**
- [FIPS](/zh/topics/fips/)
