---
title: "FIPS"
date: 2026-02-25
translationOf: /en/topics/fips.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---

FIPS（Free Internetworking Peering System）は、Nostr-styleのsecp256k1 keypairをnode identityとして使う自己組織型のmesh networking protocolです。

## 仕組み

FIPSは、中央サーバーやcertificate authorityなしでpeer networkingを成立させることを目指しています。nodeは近隣nodeを発見し、routing stateを構築し、ローカルな知識だけを使ってpacketを転送します。

設計は、spanning treeとbloom filterによるreachability dataを組み合わせています。各nodeはtreeに対する相対座標を持ち、宛先に向かってgreedy routingを行います。greedy routingが失敗しても、treeがfallback pathを提供します。

trafficは2層の暗号化で保護されます。link-layer encryption（Noise IK pattern）は近隣node間のhop-by-hop通信を保護します。session-layer encryption（Noise XK pattern）は中継routerに対してend-to-endの保護を提供します。

## なぜ重要か

FIPSは、Nostr開発者にとって馴染みのある同じkey modelを再利用しつつ、それをsocial eventではなくpacket routingに適用します。これにより、単純なidentity modelが得られます。network identityはIP allocationやcertificate chainではなく、暗号鍵そのものです。

transport-agnosticな設計も重要です。同じroutingとidentity modelを、原理上はUDP、Ethernet、Bluetooth、LoRa上で動かせます。そのためFIPSは、敵対的または不安定なnetwork environmentで興味深い選択肢になります。

## 実装状況

Compassで扱ったとおり、現在のRust実装には、動作するUDP transportとbloom-filter-based discoveryがすでに含まれています。relay-based bootstrappingはまだ今後の作業であり、現時点のprotocolは完成したNostr relay replacementというより、networking substrateに近い状態です。

---

**主要ソース:**
- [FIPS Repository](https://github.com/jmcorgan/fips)
- [Design Documentation](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**言及箇所:**
- [Newsletter #11: FIPS News](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**関連項目:**
- [Marmot Protocol](/ja/topics/marmot/)
