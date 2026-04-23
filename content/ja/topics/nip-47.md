---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47はNostr Wallet Connectを定義します。これは、Nostr appがwalletの主要credentialを各clientへ渡さずに、remote Lightning wallet serviceと通信できるようにするプロトコルです。

## 仕組み

wallet serviceは、対応するmethodとencryption modeを記述したreplaceableなkind `13194` info eventを公開します。clientは、wallet service pubkey、1つ以上のrelay、接続専用のsecretを含む`nostr+walletconnect://` URIで接続します。requestはkind `23194`イベントとして送られ、responseはkind `23195`イベントで返ります。

## Commands and Notifications

一般的なmethodには`pay_invoice`、`pay_keysend`、`make_invoice`、`lookup_invoice`、`list_transactions`、`get_balance`、`get_info`があります。wallet serviceは`payment_received`、`payment_sent`、`hold_invoice_accepted`のようなnotificationもpushできます。

仕様は当初、時間とともにいくつかのoptional methodを増やしていきましたが、最近の整理で`multi_` payment methodは削除されました。実際には、walletのinfo eventでadvertiseされたcommandにclientが従うほうが、広いmethod setを当然視するより相互運用性が高くなります。

## ユースケース

- **Zapping** - 投稿、profile、creatorへsatsを送る
- **Payments** - 任意のNostr appからLightning invoiceを支払う
- **Wallet UX separation** - 1つのwallet serviceを複数のNostr clientで使う

## セキュリティと相互運用メモ

接続URIには、clientが署名と暗号化に使う専用secretが含まれます。これによりappごとに別のwallet identityを持てるため、revocationとprivacyの両方で有利です。walletはspending上限を設定したり、methodを無効化したり、他へ影響を与えずに1つのconnectionだけを取り消したりできます。

現在はNIP-44が推奨encryption modeです。仕様には旧実装向けのNIP-04 fallbackも残っているため、clientはすべてのwalletが移行済みだと仮定するのではなく、walletがadvertiseする`encryption`タグを確認する必要があります。

---

**Primary sources:**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**Mentioned in:**
- [Newsletter #1: News](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Releases](/ja/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #8: NIP Deep Dive](/ja/newsletters/2026-02-04-newsletter/)
- [Newsletter #10: NIP Updates](/ja/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: ShockWallet Nostr-native wallet sync](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-57: Zaps](/ja/topics/nip-57/)
