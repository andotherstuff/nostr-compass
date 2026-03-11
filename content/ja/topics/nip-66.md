---
title: "NIP-66: Relay発見と稼働監視"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - リレー
---

NIP-66は、Relay監視データをNostrに公開する方法を標準化します。monitorサービスはRelayの可用性、遅延、プロトコル準拠、サポートするNIPを継続的にテストし、その結果をkind 30166イベントとして公開します。

## 仕組み

monitorはRelayへ接続し、テスト用subscriptionを送ることでRelayの可用性を確認します。遅延測定では、接続時間、subscription応答時間、イベント伝播遅延を追跡します。プロトコル準拠テストでは、Relayの挙動が仕様と一致するかを確認し、実装バグや意図的な逸脱を見つけます。

NIPサポートの検証は、[NIP-11](/ja/topics/nip-11/)の自己申告を超えて、宣言された機能が本当に動くかを実際に試します。たとえば、Relayが[NIP-50](/ja/topics/nip-50/) search対応を主張していても検索が失敗するなら、monitorはNIP-50を検証済み一覧に含めません。これにより、Relay能力のground truthが得られます。

kind 30166イベントはRelay URLを`d`タグとして使うため、パラメータ化置換可能イベントになります。各monitorはRelayごとに1件のイベントを公開し、測定値が変わるたびに更新します。同じRelayを複数monitorが追跡できるため、冗長性と相互検証が得られます。

round-trip time（rtt）タグは、異なる操作の遅延を測ります。
- `rtt open`: WebSocket接続確立時間
- `rtt read`: subscription応答時間
- `rtt write`: イベント公開速度

値はすべてミリ秒です。クライアントはこれらの指標を使い、時間に敏感な操作では低遅延Relayを優先できます。

地理情報は、より低遅延で検閲耐性の高い近隣Relayを選ぶのに役立ちます。`geo`タグには国コード、国名、地域が入り、`network`タグはclearnet RelayとTor hidden serviceやI2P endpointを区別します。

## なぜ重要か

NIP-66は、Relay品質を逸話から機械可読データへ変えます。クライアントはRelay自身の[NIP-11](/ja/topics/nip-11/)文書やハードコードされたallowlistだけを信じる必要がなくなり、1つ以上のmonitorから得た測定稼働率、測定遅延、検証済み機能サポートを比較できます。

特に重要なのはoutbox modelでのRelay選択です。クライアントが多数のRelayへ動的接続する場合、死んでいるRelayや設定不良のRelayは、フィード読み込みの遅延と取得失敗の増加という直接コストになります。

## ユースケース

monitorデータは、クライアント、explorerサイト、信頼評価システムのRelay selectorを支えます。Relayの自己申告とは独立したリアルタイム状態を提供することで、NIP-66は情報に基づくRelay選択を可能にします。

[NIP-11](/ja/topics/nip-11/)（自己申告の能力）やTrusted Relay Assertions（信頼評価）と組み合わせることで、エコシステムはハードコードされたデフォルト依存から、データ駆動のRelay選択へ進めます。

## 信頼モデル

NIP-66は単一の権威的monitorを作りません。複数のmonitorが同じRelayについて結果を公開でき、クライアントはそれらを比較できます。この設計により1人の運営者の判断への依存は下がりますが、結果が衝突したときに誰の測定を信頼するかというポリシーは、なおクライアント側に必要です。

---

**主要ソース:**
- [NIP-66 Specification](https://github.com/nostr-protocol/nips/blob/master/66.md) - Relay discovery and liveness monitoring standard
- [PR #2240](https://github.com/nostr-protocol/nips/pull/2240) - Defensive measures and unhappy-path guidance

**言及箇所:**
- [Newsletter #6: NIP Deep Dive](/ja/newsletters/2026-01-21-newsletter/)
- [Newsletter #13: NIP Updates](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-11: Relay情報ドキュメント](/ja/topics/nip-11/)
- [NIP-65: Relay List Metadata](/ja/topics/nip-65/)
- [Trusted Relay Assertions](/ja/topics/trusted-relay-assertions/)

