---
title: "Cashu: Ecashプロトコル"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-03-07
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashuは、BitcoinとLightningの上に構築されたChaumian ecashプロトコルです。ユーザーはmintが発行するbearer tokenを保持し、そのtokenを移転するときに、支払いグラフ全体をmintへ露出させずに済みます。

## 仕組み

Cashuはblind signatureを使ってecash tokenを発行します。

1. **Minting**: ユーザーはBitcoin/Lightningをmintに預け、blinded tokenを受け取る
2. **Spending**: tokenはmintを介さずにpeer-to-peerで移転できる
3. **Redemption**: 受取人はtokenをmintでBitcoin/Lightningに引き換える

mintはblinded secretに署名するため、後でtokenを検証できても、発行時点では元のsecretを見ません。これにより、mint内部で入金と換金を直接結び付けにくくなります。

## セキュリティと信頼モデル

Cashuは支払いのプライバシーを改善しますが、依然としてcustodialです。mintは換金を拒否でき、オフラインになれますし、裏付け資金を失うこともあります。

Cashu proofはbearer instrumentです。proofを保持する者がそれを使えます。proofの扱いは口座残高より現金に近く、バックアップ、端末侵害、平文tokenの漏えいはすぐに問題になります。

## Nostrとの統合

Cashuは複数の形でNostrと統合されています。

- **Nutzaps**: プライバシーを強化したzapとして送られるecash token
- **Escrow**: ライドシェアのようなサービス向けのHTLCベースのpayment escrow
- **Wallets**: Nostrネイティブwalletが暗号化されたCashu tokenをrelayに保存する
- **[NIP-87](/ja/topics/nip-87/)**: Nostrを介したmintの発見とレビュー

## トレードオフ

Cashuは、転送がon-chainでもなく、多くの場合redeemまでoff-mintでもあるため高速です。代わりに、相互運用性と信頼の問題が残ります。

実際には、ユーザーは同じmintを使う必要があるか、mint間のswapやbridgeが必要になります。だからこそ、NostrアプリはCashuをmint discovery、wallet sync、reviewシステムと組み合わせることが多いのです。

---

**主要ソース:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60: Cashu Wallet](/ja/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/ja/topics/nip-87/)

**言及箇所:**
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/en/newsletters/2026-02-25-newsletter/)

**関連項目:**
- [NIP-60: Cashu Wallet](/ja/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/ja/topics/nip-87/)
