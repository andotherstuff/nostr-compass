---
title: "NIP-63: ペイウォール / プレミアムコンテンツ"
date: 2025-12-17
translationOf: /en/topics/nip-63.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Monetization
---

NIP-63は、Nostr protocol内でgated contentを扱うための提案標準です。creatorは、contentを表示する前に支払いを求められます。

## 仕組み

content creatorは、全文を暗号化したりpaywallの背後に隠したeventを公開できます。支払いが確認されると、支払ったuser向けにcontentが解放されます。

このproposalは、premium content向けのprotocol surfaceを定めるもので、単一のpayment railやbusiness modelを強制するものではありません。柔軟さはありますが、その分、wallet、client、publisherは実際のunlock flowを別途すり合わせる必要があります。

## なぜ重要か

共有formatがなければ、Nostr上のpaywall systemはそれぞれ別のsiloになります。共通のNIPがあれば、あるclientがpremium contentを公開し、別のclientがそのcontentがgatedであること、何を支払うべきか、いつ表示すべきかを理解できます。

ただし、まだportabilityが保証されるわけではありません。NIP-63は依然として[PR #2156](https://github.com/nostr-protocol/nips/pull/2156)上のproposalなので、設計議論が続く間は実装が分岐する可能性があります。

## ユースケース

- 購読者限定記事
- プレミアムmedia content
- pay-per-view event
- creatorへの限定access

## トレードオフ

paywall metadataは、premium payloadが非公開でも公開される場合があります。これによりclientはofferを表示できますが、有料contentの存在自体はeventを読める誰にでも見えます。

creatorはunlock後の扱いも考える必要があります。いったんplaintextが有料userに表示されれば、protocolはそのuserが別の場所へコピーするのを止められません。

---

**主要ソース:**
- [NIP-63 Proposal (PR #2156)](https://github.com/nostr-protocol/nips/pull/2156)

**言及箇所:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**関連項目:**
- [NIP-57: Zaps](/ja/topics/nip-57/)
