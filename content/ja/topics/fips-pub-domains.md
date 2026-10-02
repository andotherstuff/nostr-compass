---
title: "FIPS公開ドメイン"
date: 2026-09-30
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-02
draft: false
categories:
  - Protocol
  - Networking
  - Identity
---

fips-pub-domainsは、なじみのあるインターネットのドメイン名を[FIPS](/ja/topics/fips/)メッシュ上のサービスへ解決するための初期段階の実装です。署名付きのNostrクレームを公開しますが、署名が証明するのは誰がクレームを作成したかだけです。クライアントは、クレームの作成者をドメインの所有者として扱う前に、DNSまたはDNSSECの証拠、信頼できる証人、または以前にピン留めしたバインディングも確認する必要があります。

## 検証とオフラインでの利用

[最初のリリース](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0)では、クレーム、リゾルバーデーモン、Android連携が追加されました。[バージョン0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0)ではクレームにDNSSEC証明を添付できるようになり、メッシュ上のrelayしか見えないクライアントでも、初めて見る署名付きドメインをDNSルート鍵に照らして検証できます。また、1つのドメインに対して複数の検証済みサーバーにも対応しています。[バージョン0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1)では、パッケージ化されたサーバーユニットが修正され、root権限なしで動作するよう変更されました。既存のインストールでは、差し替え用のユニットが必要です。

プロジェクトの[テストノート](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)では、2ノード構成とメッシュ内relayのみの構成が説明されています。これらはメンテナーが報告したテストであり、より広い展開の証拠ではありません。[NIP-DB提案](https://github.com/nostr-protocol/nips/pull/2487)はオープンのままで、ドラフト中のevent kind番号は割り当て済みのNostr kindではなくプレースホルダーです。

---

**主要ソース:**
- [リポジトリとREADME](https://github.com/fr34aky/fips-pub-domains)
- [リリース0.1.0〜0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [提案中のNIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [テストノート](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**言及箇所:**
- [Newsletter #42: fips-pub-domains](/ja/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**関連項目:**
- [FIPS](/ja/topics/fips/)
