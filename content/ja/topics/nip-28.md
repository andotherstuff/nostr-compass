---
title: "NIP-28: パブリックチャット"
date: 2026-09-30
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Social
---

NIP-28は、公開チャットチャンネル、チャンネルメッセージ、クライアント側のモデレーションをNostrのeventとして記述しています。現在の仕様は**draft**かつ**unrecommended**とされており、現行のrelayベースのグループについては実装者にNIP-29を参照するよう案内しています。

## eventモデル

kind `40`はチャンネルを作成し、kind `41`はそのメタデータを更新し、kind `42`はメッセージを運びます。kind `43`と`44`により、ユーザーは自分のクライアント内でメッセージを非表示にしたり、他のユーザーをミュートしたりできます。メッセージのtagはチャンネル作成eventを参照し、返信先のメッセージを示すこともできます。relayは、クライアント側でのこうした非表示やミュートの選択を強制する必要はありません。

[2022年9月の仕様変更](https://github.com/nostr-protocol/nips/commit/3423a6dfb)によって、公開チャットルームは共有されたプロトコル上の対象となりました。[現在の仕様](https://github.com/nostr-protocol/nips/blob/master/28.md)は新しい実装に別の道を推奨していますが、この歴史的な役割は今でも理解しておく価値があります。

---

**主要ソース:**
- [NIP-28の仕様と現在のステータス](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [2022年9月のパブリックチャットに関する変更](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**言及箇所:**
- [Newsletter #42: 2022年9月](/ja/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**関連項目:**
- [NIP-29: relayベースのグループ](/ja/topics/nip-29/)
