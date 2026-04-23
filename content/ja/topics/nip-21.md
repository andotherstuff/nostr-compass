---
title: "NIP-21: nostr: URIスキーム"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocol
  - Interoperability
---

NIP-21は、`npub`、`nprofile`、`nevent`、`naddr`のようなNostr識別子を開くための標準的な`nostr:` URIスキームを定義します。これにより、アプリケーション、Webサイト、オペレーティングシステムは、ユーザーがハンドラーとして登録したNostrクライアントにそれらの識別子を渡せます。

## 仕組み

`nostr:` URIは、スキーム接頭辞の後ろに、`nsec`を除く[NIP-19](/ja/topics/nip-19/)のbech32識別子を続けたものです。クライアントやオペレーティングシステムはこのスキームを`mailto:`や`tel:`と同じように扱います。ハンドラーとして登録しておけば、システム上のどこにある`nostr:`リンクでも、ユーザーが選んだNostrクライアントで開けます。

仕様にある例:

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` はユーザープロフィールを指します
- `nostr:nprofile1...` はrelay hint付きのユーザープロフィールを指します
- `nostr:nevent1...` はrelay hint付きの特定イベントを指します
- `nostr:naddr1...` はアドレス可能な置換イベント（長文記事など）を指します

## HTMLページとNostrエンティティの関連付け

NIP-21は、Nostrエンティティに対応するWebページ向けに、2つの便利な`<link>`慣例も定義しています。Nostrイベントと同じ内容を配信するページは、たとえば[NIP-23](/ja/topics/nip-23/)の`kind:30023`記事をレンダリングしたブログ記事のように、Nostr URIを指す`<link rel="alternate">`を含められます。プロフィールページは、Nostrベースの著者性を示すために、`nprofile`を指す`<link rel="me">`または`<link rel="author">`を含められます。

## なぜ重要か

このスキームは、任意のNostr識別子を単一クライアントのUIの外でも機能するリンクに変える相互運用レイヤーです。ブラウザ拡張、モバイルOSのハンドラー、デスクトップシェルはいずれも`nostr:` URIをユーザーがインストールしたクライアントにルーティングできます。これにより、プロフィールやイベントをURIとしてどこに貼り付けても、Nostrネイティブな形で開けるまま共有できます。

## 実装

`nostr:` URIのサポートは、主要なWeb、モバイル、デスクトップのNostrクライアントを含め、クライアントエコシステム全体に広く存在します。[nos2x](https://github.com/fiatjaf/nos2x)や[Alby](https://github.com/getAlby/lightning-browser-extension)のようなブラウザ拡張は、デスクトップブラウザでのURI登録を扱います。

---

**主要ソース:**

- [NIP-21仕様](https://github.com/nostr-protocol/nips/blob/master/21.md)

**言及箇所:**

- [ニュースレター #19: NostrabilityがNIP-34へ移行](/ja/newsletters/2026-04-22-newsletter/)

**関連項目:**

- [NIP-19: Bech32エンコードエンティティ](/ja/topics/nip-19/)
- [NIP-23: 長文コンテンツ](/ja/topics/nip-23/)
