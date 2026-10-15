---
title: "NIP-36: センシティブなコンテンツ"
date: 2026-10-14
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-36.md
translationDate: 2026-10-15
---

NIP-36は、理由を任意で付けられる、任意の`content-warning` tagを定義しています。クライアントはこれを使って、読者が表示を選択するまでeventを非表示にできます。eventは公開されたままです。

## 実装

[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt)は、tagとその理由を解析します。[Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte)は、読者のセンシティブなコンテンツに関する設定を使用し、コンテンツを表示するための操作を提供します。[noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx)は、警告を提示する前に、警告に関する設定と展開状態を確認します。

---

**一次資料：**
- [NIP-36仕様](https://github.com/nostr-protocol/nips/blob/master/36.md)

**言及されている記事：**
- [ニュースレター #44：表示前のコンテンツ警告](/ja/newsletters/2026-10-14-newsletter/#content-warnings-before-display)

**関連項目：**
- [NIP-32: ラベル付け](/ja/topics/nip-32/)
