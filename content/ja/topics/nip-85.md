---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85はTrusted Assertionsを定義します。これは高コストな計算を信頼できるサービスプロバイダーに委任し、そのプロバイダーが署名済みの結果をNostr eventとして公開するシステムです。

## 仕組み

Web of Trustスコア、エンゲージメントメトリクス、その他の計算済みの値には多くのrelayをクロールして大量のevent処理が必要で、モバイルデバイスでは現実的ではありません。NIP-85により、専門のプロバイダーがこれらの計算を行い、クライアントがクエリできる結果を公開できます。

サービスプロバイダーはkind 30085イベントで機能をアドバタイズします。クライアントはユーザーがすでにフォローまたは信頼するpubkeyからのアナウンスをrelayにクエリすることでプロバイダーを発見します。結果はプロバイダーが署名したkind 30382イベントとして届きます。

## 主な機能

- リソース集約型メトリクスの委任計算
- ソーシャルグラフを通じたプロバイダー発見
- 検証可能な結果のための署名済みアサーション
- クライアントサイドのトラスト判断

---

**主要ソース：**
- [NIP-85仕様](https://github.com/nostr-protocol/nips/blob/master/85.md)

**掲載ニュースレター：**
- [ニュースレター#10：NIP-85ディープダイブ](/ja/newsletters/2026-02-18-newsletter/#nipディープダイブnip-85trusted-assertions)
- [ニュースレター#11：NIP-85サービスプロバイダーDiscoverability](/ja/newsletters/2026-02-25-newsletter/#nipアップデート)

**関連項目：**
- [Web of Trust](/ja/topics/web-of-trust/)
