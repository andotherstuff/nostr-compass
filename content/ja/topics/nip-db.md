---
title: "提案中のNIP-DB: ドメインとサービスのバインディング"
date: 2026-09-30
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-02
draft: false
categories:
  - Proposals
  - Networking
  - Identity
---

NIP-DBは、通常のインターネットドメインを鍵でアドレス指定されるサービスに結び付けるための**オープンな提案**です。event kindと文言は引き続きレビューの対象であり、このページはこれを承認済みのNostr仕様として扱うものではありません。

## 検証モデル

サービスを提供する鍵は、ドメインとサービスを記した署名付きクレームを公開できます。提案では、任意のDNSまたはDNSSECの証拠、証人による証明、そしてドメイン配下の名前のためのゾーンレコードが説明されています。署名はどの鍵がクレームを公開したかを証明しますが、ドメインの管理権を証明するものではありません。クライアントは、名前の解決に使う前に、DNSの証拠、信頼できる証人、または以前にピン留めした鍵によってバインディングを検証する必要があります。

[fips-pub-domains](/ja/topics/fips-pub-domains/)は、FIPSメッシュ向けに提案者が作成したリファレンス実装です。文書化された2ノード構成とメッシュのみの構成のテストは、メンテナーが報告した実装上の証拠です。これらによって提案のオープンなレビューが決着するわけではなく、より広い展開が確立されるわけでもありません。

---

**主要ソース:**
- [オープンなNIP-DBのプルリクエスト](https://github.com/nostr-protocol/nips/pull/2487)
- [提案者のドラフトとevent kindのプレースホルダー](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [リファレンス実装とテスト](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**言及箇所:**
- [Newsletter #42: 公開ドメイン](/ja/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Newsletter #42: 提案中のNIP-DB](/ja/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
