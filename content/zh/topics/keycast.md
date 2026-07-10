---
title: "Keycast：团队 Nostr 远程签名"
date: 2026-05-21
draft: false
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
categories:
  - Signing
  - Security
  - Teams
---

Keycast 是一个面向团队的自托管 NIP-46 远程签名服务器。它将 Nostr 私钥加密存储在 SQLite 中，生成 NIP-46 bunker 连接字符串，并运行签名进程，根据可配置的按密钥策略批准或拒绝远程签名请求。该项目由 Marmot Protocol 组织维护。

## 工作原理

服务器包含四个主要组件：一个处理团队管理和 NIP-98 HTTP 认证的 Axum API、一个使用 NIP-07 进行身份验证的 SvelteKit 网页前端、一个监视授权行并为每个授权启动一个 `signer_daemon` 的签名管理器，以及一个带迁移的 SQLite 数据库。

团队成员通过其 NIP-07 浏览器扩展登录。网页应用请求一个由扩展本地签名的 NIP-98 HTTP 认证事件，然后将该认证 header 发送给 API。API 验证事件，提取 pubkey，并检查团队成员身份。存储的密钥使用一个根 `master.key` 文件加密，该文件必须与镜像分开挂载，且绝不可提交到代码仓库。

签名守护进程在启动时解密存储的密钥和 bunker 密钥，连接到已配置的 relay，并在批准每个 NIP-46 签名请求之前调用 `Authorization::validate_policy`。策略指定某个特定的 bunker 连接被允许签署哪些事件 kind。

## 安全审计（2026 年 5 月）

一次于 2026 年 5 月完成的安全审计处理了认证、权限、数据完整性和依赖方面的问题。主要变更：

- NIP-98 认证现在要求恰好一个 `u` tag 和一个 `method` tag，拒绝过期或未来的时间戳，并校验请求体的 `payload` 哈希
- `ALLOWED_PUBKEYS` 被精确解析并在服务端强制执行；前端暴露 `/api/config?pubkey=<hex>`，浏览器可借此在不获取完整服务端列表的情况下检查允许名单状态
- 空策略对签名、加密、解密请求默认拒绝；策略创建会拒绝未知或格式错误的权限配置
- SQLite 连接启用外键强制；团队删除不再在清理前丢失权限关联表数据
- 服务端路由保护现在覆盖 `/teams/:id` 等嵌套应用路由
- 网页响应设置 CSP、frame、content-type、referrer、permissions 和 HSTS header
- 一个 SQL 迁移在启动时将旧的 allowed-kinds 权限 JSON 从 `{"sign":[...]}` 规范化为 `{"allowed_kinds":[...]}`

审计在 [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) 中记录了在将部署托付给真实团队密钥之前仍需处理的遗留事项。

## 部署

Docker Compose 部署将 `master.key` 挂载到 API 和签名容器中，以非 root 的 UID/GID 运行容器并配合只读根文件系统，使用 Caddy 标签将 `/api/*` 路由到 API，将其他所有请求路由到网页应用。发布的镜像位于 `ghcr.io/marmot-protocol/keycast`，标签为 `master`、`latest` 和 `sha-<commit>`。

---

**Primary sources:**
- [Keycast Repository](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - 2026 年 5 月安全审计结果

**Mentioned in:**
- [Newsletter #23: Keycast Security Audit Complete](/zh/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**See also:**
- [NIP-46: Nostr Remote Signing](/zh/topics/nip-46/)
- [NIP-07: Browser Extension Signer](/zh/topics/nip-07/)
- [Marmot Protocol](/zh/topics/marmot/)
