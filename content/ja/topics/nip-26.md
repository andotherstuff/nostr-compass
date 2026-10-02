---
title: "NIP-26: 委任されたevent署名"
date: 2026-09-30
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Identity
---

NIP-26は、あるNostr鍵が別の鍵に対して、限られた範囲のeventへの署名を許可する方法を記述しています。現在の仕様は**draft**かつ**unrecommended**とされており、新しい統合に向けた助言ではなく、以前の設計の記録となっています。

## 仕組み

アカウント鍵は、委任先の鍵と条件を記した委任トークンに署名します。条件ではevent kindと`created_at`の時刻を制限できます。委任先は自分の鍵でeventに署名し、`delegation` tagにトークンを添付します。読み手は、eventの署名と委任トークンの両方を、それらの条件に照らして検証する必要があります。この方式に対応したrelayは、委任元による検索にも対応できます。

このモデルにより、アプリケーションはアカウントの主署名鍵を保持せずに公開できます。追加の検証とrelay検索の要件があるため、実装は通常のevent署名だけを委任されたidentityの十分な証明として扱えません。[現在の仕様](https://github.com/nostr-protocol/nips/blob/master/26.md)は、この方式をunrecommendedと明記しています。

---

**主要ソース:**
- [NIP-26の仕様と現在のステータス](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [2022年9月の委任署名に関する記述](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**言及箇所:**
- [Newsletter #42: 2022年9月](/ja/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
