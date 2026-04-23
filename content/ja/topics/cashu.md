---
title: "Cashu: Ecash Protocol"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-04-22
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashuは、BitcoinとLightning上に構築されたChaumian ecash protocolです。ユーザーはmintが発行したbearer tokenを保持し、そのtokenをmintへ完全なpayment graphを見せずに転送できます。

## 仕組み

Cashuはblind signatureを使ってecash tokenを発行します。

1. **Minting**: ユーザーはmintへBitcoin/Lightningを預け、blinded tokenを受け取る
2. **Spending**: tokenはmintを介さずpeer-to-peerで転送できる
3. **Redemption**: 受取人はmintでtokenをBitcoin/Lightningへ償還する

mintはblinded secretへ署名するため、後でtokenを検証できても、発行時点では元のsecretを見ません。これによりmint内部でdepositとredemptionの直接リンクが切れます。

## セキュリティと信頼モデル

Cashuは支払いprivacyを改善しますが、依然としてcustodialです。mintは償還を拒否したり、offlineになったり、裏付け資金を失ったりできます。

Cashu proofはbearer instrumentです。proofを支配する者が支出できます。そのためproofの扱いはaccount balanceより現金に近く、backup、端末侵害、平文token漏えいはどれも即座に問題になります。

## Nostr integration

CashuはNostrといくつかの形で統合されます。

- **Nutzaps**: ecash tokenをprivacy強化付きでzapとして送る
- **Escrow**: ridesharingのようなservice向けHTLCベースpayment escrow
- **Wallets**: Nostrネイティブwalletが暗号化されたCashu tokenをrelayへ保存する
- **[NIP-87](/ja/topics/nip-87/)**: Nostr経由のmint discoveryとreview
- **[TollGate](/ja/topics/tollgate/)**: 接続性に対してCashu ecash tokenを受け付けるpay-per-use network access protocol。これは[v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)時点で[TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)により定義されています

## トレードオフ

Cashuはtransferがoff-chainで行われ、償還までoff-mintで済むことも多いため高速です。代わりにinteroperabilityとtrustのトレードオフがあります。

実際には、ユーザーは同じmintを使う必要があることが多く、そうでなければmint間のswapやbridgeが必要です。そのためNostr applicationは、Cashuをmint discovery、wallet sync、review systemと組み合わせることがよくあります。

---

**Primary sources:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mentioned in:**
- [Newsletter #7](/ja/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/ja/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-60: Cashu Wallet](/ja/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/ja/topics/nip-87/)
- [TollGate](/ja/topics/tollgate/)
