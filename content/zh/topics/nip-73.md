---
title: "NIP-73 (地理标签)"
date: 2026-02-04
description: "NIP-73 定义了使用地理坐标和标识符为 Nostr 事件添加位置标签的方法。"
---

NIP-73 规定了如何将地理位置数据附加到 Nostr 事件。这实现了基于位置的内容发现和过滤。

## 工作原理

位置数据通过 `g`（geohash）标签添加到事件中。geohash 编码将纬度和经度表示为单个字符串，精度由字符串长度决定。字符串越长表示位置越精确。

事件可以包含不同精度级别的多个 geohash 标签，允许客户端以各种粒度进行查询。带有 6 字符 geohash 标签的帖子大约覆盖一个街区，而 4 字符 geohash 覆盖一个小城市。

## 标签格式

```json
{
  "tags": [
    ["g", "u4pruydqqvj", "geohash"],
    ["g", "u4pruyd", "geohash"],
    ["g", "u4pru", "geohash"]
  ]
}
```

## 国家代码

NIP-73 的最新更新（[PR #2205](https://github.com/nostr-protocol/nips/pull/2205)）增加了对 ISO 3166 国家代码的支持，允许事件标记国家级位置而无需精确坐标：

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## 实现

- 位置感知客户端使用 NIP-73 进行签到和本地发现
- 中继过滤器可以按地理位置限制或优先处理内容
- 地图应用程序显示带地理标签的笔记

## 主要来源

- [NIP-73 规范](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - 添加 ISO 3166 国家代码

## 相关提及

- [Newsletter #8 (2026-02-04)](/zh/newsletters/2026-02-04-newsletter/) - 国家代码支持已合并
