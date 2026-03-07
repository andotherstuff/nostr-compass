---
title: "MIP-05: プライバシー保護プッシュ通知"
url: /ja/topics/mip-05/
translationOf: /en/topics/mip-05.md
translationDate: 2026-03-07
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05は、Marmotクライアント向けのpush-notificationプロトコルを定義します。通常のモバイルpushシステムではdevice tokenやアカウント関係が露出しやすい環境で、プライバシーを保つことを狙っています。

## 仕組み

- device tokenはECDH+HKDFとChaCha20-Poly1305で暗号化される
- ephemeral keyによって通知間の相関を防ぐ
- 3イベントのgossip protocol（kinds 447-449）が暗号化されたtokenをグループメンバー間で同期する
- NIP-59のgift wrappingを使ったdecoy tokenでグループサイズを隠す

## プライバシーモデル

- push notification serverはユーザーを識別できない
- 通知パターンからグループメンバーシップが分からない
- device tokenをメッセージ間で相関付けできない

具体的な改善点は、push providerが見るのは不透明な配送tokenであって、グループメンバーから端末への直接的な対応表ではないことです。これで通知が絶対に匿名になるわけではありませんが、push層が既定で学習できる情報量を減らせます。

## イベントKind

- **Kind 447**: 暗号化されたdevice tokenの公開
- **Kind 448**: token同期リクエスト
- **Kind 449**: token同期レスポンス

## トレードオフ

MIP-05は、調整作業を増やすことでプライバシーを得ます。クライアントは暗号化されたtoken状態をグループメンバー間で同期する必要があり、decoy tokenは意図的にメッセージオーバーヘッドを増やします。

つまり実装者は、配送の信頼性とmetadata保護のバランスを取る必要があります。このプロトコルが有用なのは、pushを単なる輸送の利便性ではなく、プライバシー問題として扱っているからです。

---

**主要ソース:**
- [MIP-05 Specification](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1 release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**言及箇所:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**関連項目:**
- [Marmot Protocol](/ja/topics/marmot/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
