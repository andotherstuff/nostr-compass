---
title: "NIP-CD: スラッシュコマンド"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD はスラッシュコマンドを定義します。サービスがコマンドを公開すると、誰でも任意の Nostr event の content 内にプレーンテキストとして書くことで、そのコマンドを呼び出せます。NIP-CD はオプションのドラフト仕様です。以前の提案を経て 2026 年 10 月 21 日に Commands というタイトルでマージされ、その後 2026 年 10 月 27 日にオプションのインストール済みコマンドリストがマージされた際、Slash Commands へと改題されました。

## 仕組み

コマンドを定義するのは kind 31992 の event です。必須の tag では、スラッシュを除いたトリガーワード、タイトル、使用方法の説明を指定します。順序付きの `arg` tag は位置引数を宣言するもので、型には pubkey、event、relay、number、enum、text などがあります。`s` tag を使うと、コマンドをトリガーする event を kind、relay、作成者、tag によって限定できます。これらのスコープはフィルターのように機能し、同じ種類の値は互いに選択肢として扱われ、指定されているすべての種類が一致する必要があります。

呼び出しとは、event の content のインデックス 0 から始まるテキストのことで、たとえば `/ban` の後に引数が続く形になります。呼び出しには tag が付きません。`@nostr:npub1...` という形式の修飾子を加えると、単一の実行者を対象にできます。修飾子がない場合は、トリガーが一致し、かつスコープにその event が含まれるすべてのコマンドが動作し得るため、1 つのメッセージが複数のサービスをトリガーすることもあります。

クライアントによるサポートは任意です。オートコンプリート、引数ピッカー、レンダリングされたチップをクライアントが提供してもかまいません。ただし、呼び出しを送信する前提として自身のサポートを必須にしてはならず、パースに失敗したテキストは通常の content として送信しなければなりません。

relay ベースのグループの場合、定義と呼び出しはグループの relay に送られます。ブロードキャスト用途では、定義は実行者の outbox に、呼び出しは実行者の inbox に送られます。

## インストール済みコマンドリスト

ユーザーは、NIP-51 に従ったオプションの kind 10992 リストを管理できます。このリストに含まれる `a` tag は、実行者の pubkey と `d` 値によって kind 31992 のコマンド定義を指し示し、オプションで relay ヒントを付けることもできます。クライアントは、オートコンプリートやレンダリングされたチップにこのリストを使用すべきです。リストが記録するのは、表示と発見に関するユーザーの好みです。実行者を認可するものではなく、プレーンテキストによる呼び出しはこのリストがなくても機能します。仕様のこの部分は、2026 年 10 月 27 日に PR #2525 を通じてマージされました。どのクライアントがこのリストを実装したかは、このマージからはわかりません。

## 一次情報源

- [NIP-CD 仕様](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [2026 年 10 月 21 日の NIP-CD のマージ](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [インストール済みコマンドリストに関する PR #2525（2026 年 10 月 27 日マージ）](https://github.com/nostr-protocol/nips/pull/2525)
- [PR #2525 の 2026 年 10 月 26 日のコミット（マージ前にそのブランチ上で作成）](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [2026 年 10 月 27 日のインストール済みコマンドリストの NIP-CD へのマージ](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## 言及箇所
- [ニュースレター #46: NIP-CD がプレーンテキストで呼び出すコマンドを定義](/ja/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) ニュースレター

- [ニュースレター #46: NIP-CD がオプションのインストール済みコマンドリストを追加](/ja/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) ニュースレター

- [ニュースレター #46（2026-10-28）: 2026 年 10 月、共有されるクエリの意味とテキストでトリガーされるサービス](/ja/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## 関連項目

- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
