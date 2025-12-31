---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - 暗号技術
  - プロトコル
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) は、グループの参加者が単一の当事者が完全な秘密鍵を保持することなく、協力して有効なSchnorr署名を生成できる閾値署名スキームです。

## 仕組み

FROSTはT-of-N閾値署名を可能にします。N人の鍵保持者のうちT人の参加者が協力して有効な署名を生成します。プロトコルは2ラウンドで動作します：

1. **コミットメントラウンド**: 各参加者が暗号学的コミットメントを生成し共有
2. **署名ラウンド**: 参加者が部分署名を組み合わせて最終的な集約署名を作成

生成された署名は標準的なSchnorr署名と区別がつかず、既存の検証システムとの後方互換性を維持します。

## 主要な特性

- **閾値セキュリティ**: 単一の参加者だけでは署名できず、T人の当事者が協力する必要がある
- **ラウンド効率**: 署名に必要な通信は2ラウンドのみ
- **偽造防止**: 以前の閾値スキームへの攻撃から保護する新しい技術
- **署名集約**: 複数の署名が1つのコンパクトな署名に結合
- **プライバシー**: 最終署名からどのT人の参加者が署名したかは分からない

## Nostrでの使用例

Nostrの文脈において、FROSTは以下を可能にします：

- **クォーラムガバナンス**: グループがT-of-Nスキームを通じてnsecを共有でき、メンバーは自身を代表するか評議会に委任可能
- **マルチシグ管理**: 複数の管理者署名を必要とするコミュニティモデレーション
- **分散型鍵管理**: 重要な操作のために複数の当事者間で信頼を分散

## 標準化

FROSTは2024年6月にRFC 9591として標準化され、「The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures」というタイトルが付けられました。

---

**主要な情報源:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**関連記事:**
- [Newsletter #3: NIPsリポジトリ](/ja/newsletters/2025-12-31-newsletter/#nips-repository)

**関連項目:**
- [NIP-XX Quorum提案](https://github.com/nostr-protocol/nips/pull/2179)
