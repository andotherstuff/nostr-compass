---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-03-11
draft: false
categories:
  - ウォレット
  - ライトニング
---
NIP-47はNostr Wallet Connectを定義し、Nostr appがwalletの主要credentialを各clientへ渡さずに、remote Lightning wallet serviceと通信できるようにします。

## 仕組み

wallet serviceは、対応するmethodとencryption modeを記述したreplaceableなkind `13194` info eventを公開します。clientは、wallet service pubkey、1つ以上のrelay、接続専用secretを含む`nostr+walletconnect://` URIで接続します。requestはkind `23194` eventとして送られ、responseはkind `23195` eventで返ります。

## CommandsとNotifications

よく使われるmethodには`pay_invoice`、`pay_keysend`、`make_invoice`、`lookup_invoice`、`list_transactions`、`get_balance`、`get_info`があります。wallet serviceは`payment_received`、`payment_sent`、`hold_invoice_accepted`のようなnotificationもpushできます。

仕様には以前、いくつかのoptional methodが増えていましたが、最近の整理で`multi_` payment methodは削除されました。実運用では、walletのinfo eventでadvertiseされたcommandだけを使うほうが相互運用しやすく、広いmethod setを前提にしないほうが安全です。

## ユースケース

- **Zapping** - 投稿、profile、creatorにsatsを送る
- **Payments** - どのNostr appからでもLightning invoiceを支払う
- **Wallet UX separation** - 1つのwallet serviceを複数のNostr clientで使う

## セキュリティと相互運用メモ

接続URIには、clientが署名と暗号化に使う専用secretが含まれます。これによりappごとに別のwallet identityを持てるため、revokeしやすく、privacy面でも有利です。walletはspending上限を設けたり、methodを無効化したり、ある1つのconnectionだけを取り消したりできます。

現在はNIP-44が推奨encryption modeです。ただし仕様には旧実装向けのNIP-04 fallbackも残っているため、clientはwalletの`encryption` tagを見て判断する必要があります。すべてのwalletが移行済みだと決め打ちするべきではありません。

---

**主要ソース:**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**言及箇所:**
- [Newsletter #1: News](/ja/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Releases](/ja/newsletters/2025-12-24-newsletter/#releases)
- [Newsletter #3: December Recap](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #8: NIP Deep Dive](/ja/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Newsletter #10: NIP Updates](/ja/newsletters/2026-02-18-newsletter/#nip-updates)

**関連項目:**
- [NIP-57: Zaps](/ja/topics/nip-57/)
