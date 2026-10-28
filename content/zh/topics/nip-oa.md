---
title: 'Buzz 草案 NIP-OA：所有者证明'
date: 2026-10-28
translationOf: /en/topics/nip-oa.md
translationDate: 2026-10-28
draft: false
---

**状态：** 这是 Buzz 项目专属的草案提案。NIP-OA 并非已被接受的官方 NIP。这一标签出自 Buzz 项目文档，官方 NIPs 仓库既未分配也未批准它。

## 目的

NIP-OA 定义了一个可选的 `auth` tag，使所有者密钥能够授权某个代理密钥发布 event。event 的作者仍然是代理密钥。有效的 tag 仅被视为授权证据，并不能让代理冒充所有者。

## 机制

所有者以 Schnorr 签名对一个经过域分离的哈希进行签名，该哈希将代理 pubkey 与一个确切的条件字符串绑定在一起。条件可以要求特定的 event kind，也可以为代理自行声明的 `created_at` 设定范围。只要每个 event 都满足这些条件，代理就可以在自己的 event 上重复使用该 tag。验证者首先验证核心 event，然后检查所有者签名以及每一项条件。

## 限制

空的条件字符串不会增加任何约束。时间戳条款约束的是代理自己可以控制的字段，因此无法提供基于真实时钟的过期机制。需要新鲜度保证的人必须另行检查。公开发布该 tag 会把所有者密钥与代理密钥关联起来。

## 主要来源

- [Buzz NIP-OA 草案：所有者证明（固定版本）](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## 另请参阅

- [NIP-01](/zh/topics/nip-01/)

**提及于：**

- [第 46 期简报：Buzz](/zh/newsletters/2026-10-28-newsletter/#buzz)
