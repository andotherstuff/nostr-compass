---
title: "ContextVM"
date: 2026-02-25
translationOf: /en/topics/contextvm.md
translationDate: 2026-03-07
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---

ContextVMは、MCP（Model Context Protocol）トラフィックをNostr上で運ぶためのプロトコルとtoolchainです。中央レジストリ、ドメイン、OAuthに依存せずに、MCPクライアントとサーバーが相互に発見し、署名付きメッセージをやり取りできるようにします。

## 仕組み

ContextVM SDKは、MCP over Nostr向けのTypeScript client transportとserver transportを提供します。既存のMCPサーバーは通常のtransportをそのまま使えます。その上でgatewayがNostrへ公開し、Nostrをネイティブで扱えないクライアントはproxy layer経由で接続できます。

Relayはmessage busとして動作します。eventをルーティングし、署名と暗号化によって、endpointに認証とtransport privacyを提供します。

## 構成要素

**SDK**: client/server transport、proxy support、local MCP serverをNostrへbridgeするgateway functionalityを備えたTypeScript libraryです。

**CVMI**: server discoveryとmethod invocationのためのcommand-line interfaceです。

**Relatr**: social graph distanceとprofile validationから個別のscoreを計算するtrust scoring serviceです。

## なぜ重要か

ContextVMはtransport bridgeであり、MCP自体の置き換えではありません。ここが重要です。既存のMCPサーバーはtool schemaやbusiness logicを書き直さなくてもNostr経由で到達可能になり、導入コストを下げられます。

最近のContextVMの作業では、gift-wrapped traffic向けのephemeral deliveryも前に進みました。これはtool callや中間応答のように、relayで永続保存する必要がなく、余計なprivacy exposureを避けたい場面で有用です。

## 相互運用メモ

2026年2月から3月にかけて、このprojectは実装中心の段階から標準化へと移りました。teamは、MCP JSON-RPC over Nostrとgift wrapのephemeral variantについてNIP proposalを公開しました。これらのproposalが今後変わるとしても、protocol boundaryをより明確に示しています。MCPはapplication layerにとどまり、Nostrがdiscoveryとtransportを担います。

---

**主要ソース:**
- [ContextVM Website](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Ephemeral Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**言及箇所:**
- [Newsletter #11: ContextVM News](/en/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**関連項目:**
- [NIP-90: Data Vending Machines](/ja/topics/nip-90/)
