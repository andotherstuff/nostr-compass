---
title: "TollGate: Pay-per-use Internet Over Nostr and Cashu"
date: 2026-04-22
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGateは、小額で頻繁なbearer asset paymentと引き換えにネットワーク接続を販売するためのプロトコルです。WiFi router、Ethernet switch、Bluetooth tetherのように接続を制御できるデバイスがTollGateとして動作し、料金を広告し、[Cashu](/ja/topics/cashu/) ecash tokensを受け取り、sessionを管理します。顧客は実際に使った分の分数やmegabytesだけを支払います。アカウントも、subscriptionも、KYCもありません。

## 仕組み

TollGateは関心事を3つのlayerに分離します。protocol layerはevent shapeとpayment semanticsを定義し、interface layerはcustomerとgateがそれらのイベントをどう交換するかを定義し、medium layerは有料トラフィックを運ぶ物理リンクを説明します。実際に動くTollGateは各layerから1つずつ仕様を組み合わせて構成され、一部のinterfaceはNostr relays上で動き、別のものはplain HTTP上で動きます。

protocol layerでは、[TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)が3つの基本イベントを定義します。価格と受け入れmintを示すAdvertisement kind、顧客がどれだけ支払い、どれだけ消費したかを追跡するSession kind、帯域外メッセージ向けのNotice kindです。[TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)はこの上にCashu paymentを重ね、顧客がTollGateの広告する任意のmintからecash tokenを償還し、その見返りとしてsession creditを受け取れるようにします。

interface layerでは、[HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md)からHTTP-03が、任意のrelayへWebSocket接続を開きづらい制限的なOS向けにHTTP surfaceを定義し、[NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)が、それを行えるclient向けにNostr-relay transportを定義します。medium layerでは、[WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)が、captive portal型のWiFi構成で支払い済み顧客をどう識別し、どうルーティングするかを説明します。

支払い資産がcredentialではなくbearer tokenなので、顧客はそれを生成するための事前インターネット接続を必要としません。ローカルwallet内にあるCashu tokenだけで最初の1分の接続を購入でき、その後必要に応じてさらにtokenを追加できます。TollGate同士が互いにuplinkを購入することもできるため、到達範囲は1人の運用者を超えて広がります。

## なぜ重要か

従来の有料WiFiは、アカウント、captive portals、payment cardsに依存しており、そのどれもが摩擦とデータの痕跡を生みます。TollGateのモデルは、接続性を、任意のrouterが任意の支払い済み顧客へ、相手を知らずに販売できるcommodityへ変えます。この抽象化により、独立した運用者は自分の価格を設定し、自分の好むmintを受け入れ、囲い込みではなくcoverageと品質で競争できます。

[v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)は、これらの仕様の最初のtag付きsnapshotです。まだ細部のすべてを標準化してはいませんが、router firmware、client wallets、multi-hop resellersが安定した参照仕様に対して実装を始められるだけのsurfaceを固定しています。

---

**Primary sources:**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: Base Events](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: Cashu payments](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 through HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [TollGate repository](https://github.com/OpenTollGate/tollgate)

**Mentioned in:**
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [Cashu](/ja/topics/cashu/)
- [NIP-60: Cashu Wallet](/ja/topics/nip-60/)
