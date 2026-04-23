---
title: "NIP-C7: Chat Messages"
date: 2026-04-15
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-C7は、chat message向けのevent kindとしてkind `9`を定義します。目的は、chat向けのトラフィックを一般的なsocial feedのトラフィックから分離し、clientが各文脈に応じて異なるUXとmoderation rulesを適用できるようにすることです。

## 仕組み

kind `9`イベントは、message contentに加えてchat contextを識別するtagsを持ちます。[NIP-29](/ja/topics/nip-29/)のrelay-based groupsでは、イベントにgroup IDを示す`h`タグが入ります。返信スレッドは、以前のイベントを参照する`q`タグで構成されます。

NIP-C7の焦点は、これらのイベントをどこに描画すべきかです。kind `1`のtext notesのようにグローバルなnote feedへ混ぜるのではなく、kind `9`イベントは会話状態とthreadingが明示されるchat-oriented viewで表示することが意図されています。

## Implementations

- [Flotilla](https://gitea.coracle.social/coracle/flotilla)と[Coracle](https://github.com/coracle-social/coracle)は、group chat workflowでkind `9`を使っています。
- [Amethyst](https://github.com/vitorpamplona/amethyst)は、messaging stackにkind `9`対応を含めています。
- [White Noise](https://github.com/marmot-protocol/whitenoise)は、`q`タグを使ったNIP-C7 reply threadingを使っています。

---

**Primary sources:**
- [NIP-C7 Specification](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: Restrict kind 9 to chat views](https://github.com/nostr-protocol/nips/pull/2310)

**Mentioned in:**
- [Newsletter #18: NIP Updates](/en/newsletters/2026-04-15-newsletter/)

**See also:**
- [NIP-29: Relay-based Groups](/ja/topics/nip-29/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
