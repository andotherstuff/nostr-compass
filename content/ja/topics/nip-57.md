---
title: "NIP-57: Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57はzapsを定義します。これはNostrユーザーとコンテンツにLightning支払いを送信し、支払いが行われたことの暗号的証明を得る方法です。

## 仕組み

1. クライアントが受信者のkind 0プロフィールからLightningアドレスを取得
2. クライアントが受信者のLNURLサーバーにzapリクエストイベントを含めてインボイスをリクエスト
3. ユーザーがインボイスを支払う
4. LNURLサーバーがkind 9735 zapレシートをNostrリレーに公開
5. クライアントが受信者のコンテンツにzapを表示

## Zapリクエスト（kind 9734）

zapリクエストは誰がzapを送信し、どのコンテンツに送信したかを証明する署名されたイベントです。以下を含みます:
- 受信者pubkeyを含む`p`タグ
- zapされるイベントを含む`e`タグ（オプション）
- ミリサトシ単位の`amount`タグ
- レシートを公開する場所をリストする`relays`タグ

## Zapレシート（kind 9735）

支払い確認後にLNURLサーバーによって公開されます。以下を含みます:
- `description`タグ内の元のzapリクエスト
- 支払われたインボイスを含む`bolt11`タグ
- 支払いを証明する`preimage`タグ

---

**主要ソース:**
- [NIP-57仕様](https://github.com/nostr-protocol/nips/blob/master/57.md)

**言及箇所:**
- [ニュースレター #1: ニュース](/ja/newsletters/2025-12-17-newsletter/#news)
- [ニュースレター #2: ニュース](/ja/newsletters/2025-12-24-newsletter/#news)

**関連項目:**
- [NIP-47: Nostr Wallet Connect](/ja/topics/nip-47/)

