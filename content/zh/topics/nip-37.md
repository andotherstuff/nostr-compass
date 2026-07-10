---
title: "NIP-37：草稿封装"
date: 2026-07-01
draft: false
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37 为任意种类的未签名草稿事件定义了一种加密存储事件。用户在撰写长文文章、即将发生的日历事件，或稍后可能发送的消息时,可以将草稿以 kind `31234` 事件的形式存储在 relay 上，并使用 [NIP-44](/zh/topics/nip-44/) 对自己的密钥进行加密。任何持有该用户密钥的客户端都可以恢复草稿，同一 NIP 还定义了一个独立的 `kind:10013` 列表事件，用于声明用户希望将私有草稿存储到哪些 relay 上。

## 工作原理

一个草稿封装是一个 kind `31234` 的参数化可替换事件。未签名的草稿事件先被 JSON 序列化，再用 NIP-44 对签名者自己的公钥加密，然后放入 `.content` 中。`k` tag 声明草稿的 kind，方便客户端按事件类型对草稿进行分组。`d` tag 承载草稿标识符，使封装可以随草稿演进而被替换。规范建议使用 NIP-40 `expiration` tag，让旧草稿自动过期。

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

`.content` 字段被清空则表示该草稿已被删除。

## Checkpoint

Kind `1234` 定义了属于某个父 `kind:31234` 事件的 checkpoint。Checkpoint 携带一个 `a` tag 指回父草稿，让客户端可以在最新草稿之外保存修订历史。

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## 私有内容的 Relay 列表（kind 10013）

Kind `10013` 是一个可替换事件，其 tag 列出了用户希望存储私有内容（包括草稿封装）的 relay。发布 kind `31234` 的客户端应当将其发布到用户 kind `10013` 事件所列出的 relay 上。这将公开发布使用的 relay 集合（NIP-65）与私有内容存储使用的 relay 集合分离，使用户可以将私有草稿固定在一小组受信任的 relay 上，而不必在公开的 outbox 中暴露这组 relay。

## 实现

- [Notedeck](https://github.com/damus-io/notedeck) - 将私有同步 relay 存储为一个 kind-10013 列表（2026 年 6 月加入）

---

**Primary sources:**
- [NIP-37 Specification](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Notedeck commit storing private-sync relays as kind-10013](https://github.com/damus-io/notedeck) - Damus 团队为桌面同步 relay 管理采纳该规范

**Mentioned in:**
- [Newsletter #29: Notedeck](/zh/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**See also:**
- [NIP-44: Versioned Encryption](/zh/topics/nip-44/)
- [NIP-65: Relay List Metadata](/zh/topics/nip-65/)
