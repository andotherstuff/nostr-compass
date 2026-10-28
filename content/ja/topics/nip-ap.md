---
title: "Buzz NIP-AP: エージェントペルソナ"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

Buzz NIP-AP は Buzz プロジェクトのドラフト仕様であり、nostr-protocol/nips で採択された NIP には含まれていません。

この仕様は kind 30175 のペルソナ event を定義します。これは AI エージェントをインスタンス化するためのアドレス指定可能な定義で、平文の `d` スラッグをキーとします。チームカタログのプロジェクションを保持するのは kind 30178 です。実装する relay は両方の kind へのアクセスを制限します。作成者は自分自身の event を読むことができますが、それ以外の読み手がクエリ、ライブ配信、検索、カウント、id による参照で event を確認できるのは、その event が `["shared", "true"]` を持つ場合に限られます。チームを共有すると、ペルソナが共有されていないメンバーも含め、全メンバーの埋め込まれたプロジェクションと指示が公開されます。このゲートはコンテンツを暗号化せずにアクセスを制御するものなので、relay の運営者は引き続きその内容を読むことができます。

一次情報源: Buzz リポジトリ内の [NIP-AP 仕様](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)。

## 一次情報源

- [Buzz NIP-AP: エージェントペルソナ](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## 言及箇所

- [ニュースレター #46（2026-10-28）: buzz](/ja/newsletters/2026-10-28-newsletter/#buzz)

- [ニュースレター 45](/en/newsletters/2026-10-21-newsletter/#buzz)
