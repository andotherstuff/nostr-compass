---
title: Kind 类型注册表
url: /zh/kind-registry/
translationOf: /en/kind-registry.md
translationDate: 2025-12-26
---

事件类型（Kind）是用于分类 Nostr 事件的整数。本注册表列出了所有标准化的 kind 类型及其描述和定义它们的 NIP。

**Kind 范围**（来自 [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)）：
- **0-999**：常规事件（保留所有版本）
- **1000-9999**：常规事件（续）
- **10000-19999**：可替换事件（每个公钥仅保留最新版本）
- **20000-29999**：临时事件（不存储，仅转发）
- **30000-39999**：可寻址事件（每个公钥 + kind + d-tag 保留最新版本）

## 核心事件 (0-99)

| Kind | 描述 | NIP |
|------|-------------|-----|
| 0 | 用户元数据 | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 1 | 短文本笔记 | [10](https://github.com/nostr-protocol/nips/blob/master/10.md) |
| 2 | 推荐中继（已弃用） | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 3 | 关注列表 | [02](https://github.com/nostr-protocol/nips/blob/master/02.md) |
| 4 | 加密私信 | [04](https://github.com/nostr-protocol/nips/blob/master/04.md) |
| 5 | 事件删除请求 | [09](https://github.com/nostr-protocol/nips/blob/master/09.md) |
| 6 | 转发 | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 7 | 反应 | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 8 | 徽章授予 | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 9 | 聊天消息 | [C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) |
| 10 | 群聊话题回复（已弃用） | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 11 | 话题 | [7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) |
| 12 | 群组话题回复（已弃用） | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 13 | 密封 | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 14 | 私信 | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 15 | 文件消息 | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 16 | 通用转发 | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 17 | 对网站的反应 | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 20 | 图片 | [68](https://github.com/nostr-protocol/nips/blob/master/68.md) |
| 21 | 视频事件 | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 22 | 竖屏短视频 | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 40 | 频道创建 | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 41 | 频道元数据 | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 42 | 频道消息 | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 43 | 频道隐藏消息 | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 44 | 频道禁言用户 | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 62 | 请求销毁 | [62](https://github.com/nostr-protocol/nips/blob/master/62.md) |
| 64 | 国际象棋 (PGN) | [64](https://github.com/nostr-protocol/nips/blob/master/64.md) |

## MLS 加密 (443-445)

| Kind | 描述 | NIP |
|------|-------------|-----|
| 443 | KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 444 | 欢迎消息 | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 445 | 群组事件 | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |

## 常规事件 (1000-9999)

| Kind | 描述 | NIP |
|------|-------------|-----|
| 1018 | 投票响应 | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1021 | 出价 | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1022 | 出价确认 | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1040 | OpenTimestamps | [03](https://github.com/nostr-protocol/nips/blob/master/03.md) |
| 1059 | Gift Wrap | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 1063 | 文件元数据 | [94](https://github.com/nostr-protocol/nips/blob/master/94.md) |
| 1068 | 投票 | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1111 | 评论 | [22](https://github.com/nostr-protocol/nips/blob/master/22.md) |
| 1222 | 语音消息 | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1244 | 语音消息评论 | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1311 | 直播聊天消息 | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 1337 | 代码片段 | [C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) |
| 1617 | 补丁 | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1618 | Pull Request | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1619 | Pull Request 更新 | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1621 | Issue | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1984 | 举报 | [56](https://github.com/nostr-protocol/nips/blob/master/56.md) |
| 1985 | 标签 | [32](https://github.com/nostr-protocol/nips/blob/master/32.md) |
| 2003 | 种子 | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 2004 | 种子评论 | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 4550 | 社区帖子审核 | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 5000-5999 | 任务请求 | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 6000-6999 | 任务结果 | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7000 | 任务反馈 | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7374 | 保留的 Cashu 钱包代币 | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7375 | Cashu 钱包代币 | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7376 | Cashu 钱包历史 | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 8000 | 添加用户 | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 8001 | 移除用户 | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 9000-9030 | 群组控制事件 | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 9041 | Zap 目标 | [75](https://github.com/nostr-protocol/nips/blob/master/75.md) |
| 9321 | Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 9734 | Zap 请求 | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9735 | Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9802 | 高亮 | [84](https://github.com/nostr-protocol/nips/blob/master/84.md) |

## 可替换事件 (10000-19999)

| Kind | 描述 | NIP |
|------|-------------|-----|
| 10000 | 静音列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10001 | 置顶列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10002 | 中继列表元数据 | [65](https://github.com/nostr-protocol/nips/blob/master/65.md) |
| 10003 | 书签列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10004 | 社区列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10005 | 公共聊天列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10006 | 屏蔽中继列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10007 | 搜索中继列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10009 | 用户群组 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10012 | 收藏中继列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10013 | 私有事件中继列表 | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 10015 | 兴趣列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10019 | Nutzap Mint 推荐 | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 10020 | 媒体关注 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10030 | 用户表情列表 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10050 | 接收私信的中继列表 | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 10051 | KeyPackage 中继列表 | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 10063 | 用户服务器列表 | Blossom |
| 10166 | 中继监控公告 | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 10312 | 房间在线状态 | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 13194 | 钱包信息 | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 13534 | 成员列表 | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 17375 | Cashu 钱包事件 | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |

## 认证和钱包 (22000-27999)

| Kind | 描述 | NIP |
|------|-------------|-----|
| 22242 | 客户端认证 | [42](https://github.com/nostr-protocol/nips/blob/master/42.md) |
| 23194 | 钱包请求 | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 23195 | 钱包响应 | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 24133 | Nostr Connect | [46](https://github.com/nostr-protocol/nips/blob/master/46.md) |
| 24242 | 存储在媒体服务器上的 Blob | Blossom |
| 27235 | HTTP 认证 | [98](https://github.com/nostr-protocol/nips/blob/master/98.md) |

## 访问控制 (28000-29999)

| Kind | 描述 | NIP |
|------|-------------|-----|
| 28934 | 加入请求 | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28935 | 邀请请求 | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28936 | 离开请求 | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |

## 可寻址事件 (30000-39999)

| Kind | 描述 | NIP |
|------|-------------|-----|
| 30000 | 关注集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30002 | 中继集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30003 | 书签集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30004 | 策展集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30005 | 视频集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30007 | Kind 静音集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30008 | 个人资料徽章 | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30009 | 徽章定义 | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30015 | 兴趣集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30017 | 创建或更新店铺 | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30018 | 创建或更新商品 | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30019 | 市场 UI/UX | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30020 | 拍卖商品 | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30023 | 长文内容 | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30024 | 长文草稿 | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30030 | 表情集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30063 | 发布产物集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30078 | 应用特定数据 | [78](https://github.com/nostr-protocol/nips/blob/master/78.md) |
| 30166 | 中继发现 | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 30267 | 应用策展集合 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30311 | 直播活动 | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30312 | 互动房间 | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30313 | 会议活动 | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30315 | 用户状态 | [38](https://github.com/nostr-protocol/nips/blob/master/38.md) |
| 30402 | 分类信息 | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30403 | 分类信息草稿 | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30617 | 代码仓库公告 | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30618 | 代码仓库状态公告 | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30818 | Wiki 文章 | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 30819 | 重定向 | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 31234 | 草稿事件 | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 31922 | 基于日期的日历事件 | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31923 | 基于时间的日历事件 | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31924 | 日历 | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31925 | 日历事件 RSVP | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31989 | 处理程序推荐 | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 31990 | 处理程序信息 | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 34550 | 社区定义 | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 38172 | Cashu Mint 公告 | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38173 | Fedimint 公告 | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38383 | 点对点订单事件 | [69](https://github.com/nostr-protocol/nips/blob/master/69.md) |
| 39000-39009 | 群组元数据事件 | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 39089 | 入门包 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39092 | 媒体入门包 | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39701 | 网页书签 | [B0](https://github.com/nostr-protocol/nips/blob/master/B0.md) |

*最后更新：2025 年 12 月*

请参阅 [NIPs 仓库](https://github.com/nostr-protocol/nips) 获取权威来源。
