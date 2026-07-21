---
title: "NIP-4E：将加密与身份解耦"
date: 2026-07-15
draft: false
translationOf: /en/topics/nip-4e.md
translationDate: 2026-07-15
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4E 是 fiatjaf 提出的一份开放草案，用于在用户自己的多台设备之间共享私密数据，而无需每台设备都持有该用户的主 Nostr 身份密钥。它尚未合并，仍是一份 `draft`/`optional` 提案。

## 它要解决的问题

许多既有 NIP，包括 NIP-51 列表和 NIP-60 Cashu 钱包，都使用身份密钥把数据从用户加密给用户自己，以便日后在任意设备上读回。当身份密钥无法直接访问时，这种做法就会失效，例如远程签名器由 FROST 门限分片、MuSig2 或托管的安全飞地保护时，每次加密和解密都需要与该签名器往返一次。当签名密钥位于远程 bunker 中时，它也让离线加密变得不可能。

## 工作方式

NIP-4E 把按设备的「客户端密钥」与一把并非用户身份密钥的共享「加密密钥」分离开：

1. 用户设置的第一个客户端生成一个随机加密密钥对，并在一个由用户身份密钥签名的 `kind:10044` 事件中公布其公钥部分。
2. 任何想为该用户加密或解密数据的其他客户端，都针对公布的加密密钥而非身份密钥计算其 Diffie-Hellman 共享密钥。
3. 当第二台设备安装新客户端时，该客户端生成自己的本地「客户端密钥」，并发布一个 `kind:4454` 公告（同样由用户的身份密钥签名），请求第一个客户端与它共享加密密钥。
4. 原客户端检测到新的 `kind:4454` 公告后，使用 [NIP-44](/zh/topics/nip-44/) 把共享加密密钥加密给新客户端的密钥并发布，使新客户端此后可以解密并使用它。

结果是，一旦客户端在本地持有共享加密密钥，加密和解密就完全不需要再询问身份密钥签名器；身份可以采用远程签名器方案（FROST、MuSig2、托管飞地），而普通加密仍然快速并可离线工作。

## 为何重要

NIP-4E 被引用为其他提案的基础，这些提案需要一把云盘范围或账户范围的对称密钥，而不必为每次加密/解密调用都依赖远程签名器，其中包括一个私密加密云盘提案（[PR #2412](https://github.com/nostr-protocol/nips/pull/2412)），以及同一想法在 NIP-17 上更狭窄的版本（[PR #2361](https://github.com/nostr-protocol/nips/pull/2361)）。两者都与 NIP-4E 本身一样仍处于开放状态，使这里成为协议中一个活跃且尚未定论的领域，而不是一块已经完成的构件。

---

**主要来源：**
- [NIP-4E 草案，PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**提及于：**
- [Newsletter #31：新开：扩展 NIP-4E 的私密加密云盘](/zh/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**另见：**
- [NIP-44: Encrypted Payloads](/zh/topics/nip-44/)
- [NIP-17: Private Direct Messages](/zh/topics/nip-17/)
- [NIP-46: Nostr Connect](/zh/topics/nip-46/)
- [FROST](/zh/topics/frost/)
