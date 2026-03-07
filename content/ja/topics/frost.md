---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2026-03-07
draft: false
categories:
  - 暗号技術
  - プロトコル
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) は、どの参加者も完全な秘密鍵を保持せずに、グループで1つの有効なSchnorr署名を生成できるthreshold signature schemeです。

## 仕組み

FROSTはT-of-N署名を可能にします。しきい値を満たす参加者集合であれば、グループ公開鍵に対する署名を協調して生成できます。

署名プロトコルは2ラウンドです。

1. **Commitment Round**: 各参加者が暗号学的commitmentを生成して共有する
2. **Signature Round**: 参加者がpartial signatureを組み合わせ、最終的なaggregate signatureを作る

最終出力は通常のSchnorr署名として検証されます。検証側から見えるのは、1つの公開鍵に対する1つの署名だけで、cosignerの一覧ではありません。

## セキュリティ上の注意

nonceの扱いは重要です。RFCでは、署名nonceは一度しか使ってはいけないと明記されています。再利用すると鍵情報が漏れる可能性があります。

RFCはdistributed key generation自体を標準化していません。標準化しているのは署名プロトコル本体であり、trusted-dealerによる鍵生成は付録にあるだけです。実際のFROST運用の安全性は、署名フローだけでなく、shareをどう生成し、どう保管したかにも依存します。

## Nostrでの用途

Nostrの文脈では、FROSTは次の用途を支えます。

- **Quorum Governance**: グループがT-of-N方式でnsecを共有し、メンバーが自分で参加したり評議会へ委任したりできる
- **Multi-sig Administration**: 複数の管理者署名を必要とするコミュニティ運営
- **Decentralized Key Management**: 重要操作の信頼を複数の当事者に分散する

## ステータス

FROSTは、2024年6月にIRTF streamで公開された[RFC 9591](https://datatracker.ietf.org/doc/rfc9591/)で仕様化されています。これにより安定した公開仕様が得られましたが、IETF standards-trackのRFCではありません。

---

**主要ソース:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**言及箇所:**
- [Newsletter #3: NIPs Repository](/en/newsletters/2025-12-31-newsletter/#nips-repository)
- [Newsletter #8](/en/newsletters/2026-02-04-newsletter/)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)

**関連項目:**
- [NIP-46: Nostr Connect](/ja/topics/nip-46/)
- [NIP-55: Android Signer Application](/ja/topics/nip-55/)
