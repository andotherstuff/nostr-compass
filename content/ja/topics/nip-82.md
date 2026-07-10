---
title: "NIP-82: ソフトウェアアプリケーション"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
categories:
  - Discovery
  - Apps
---

NIP-82は、Nostrクライアントがアプリケーション（Android APK、iOSアプリ、Webアプリ、デスクトップバイナリ）をフィードや発見画面でファーストクラスのオブジェクトとしてレンダリングできるように、ソフトウェアアプリケーションイベントを定義します。この仕様は、汎用kind 1ノートや[NIP-89](/ja/topics/nip-89/)のハンドラ推奨を通じてアプリを記述する従来のアプローチを、アプリケーションのメタデータ、スクリーンショット、リポジトリリンク、作者の身元を運ぶ専用の構造化イベントで置き換えます。

## 仕組み

NIP-82のソフトウェアアプリケーションは、作者のpubkeyと`d`タグで指定される単一の置き換え可能イベントです。イベントには以下が含まれます。

- 表示用の`name`、`description`、`icon`、`image`タグ
- ソースとホームページURL用の`repository`と`web`タグ
- 対応するターゲット（android、ios、web、linux、macos、windows）を列挙する`platforms`タグ
- プラットフォーム固有のバイナリまたはWeb URLごとの`download`タグ
- アプリケーションのスクリーンショット画像URLを運ぶ`screenshots`タグ
- 分類のための`t`トピックタグ
- 現在の公開バージョンを示す`version`タグ

NIP-82フィードを閲覧するクライアントは、アプリケーションカードを表示し、正規のリポジトリにリンクし、Nostrの長文投稿やサードパーティのアプリストアをスクレイピングすることなくスクリーンショットを表示できます。作者のpubkeyがアプリケーションの真実の源となるため、クライアントはダウンロードリンクを宣伝する前に、公開者が期待される開発者の身元と一致するかを検証できます。

## フィードの仕様

NIP-82イベントはアドレス可能なので、各アプリケーションは作者ごとに1つの正規の置き換え可能イベントを持ちます。新バージョンを公開する開発者は以前のイベントをその場で置き換え、購読者はイベント履歴を管理することなく更新を確認できます。変更ログを希望するクライアントは、アドレス可能なイベントを購読し、バージョンアップをアプリケーション画面上の活動としてレンダリングできます。

この仕様は[NIP-89](/ja/topics/nip-89/)（アプリケーションハンドラ）と組み合わせられます。NIP-82イベントはアプリケーションを成果物として記述し、NIP-89イベントはそのアプリケーションが特定のevent kindを処理できることを記述します。クライアントは一方だけでも使えますが、この2つを組み合わせることで、共に機能する発見画面（NIP-82）と委任画面（NIP-89）が得られます。

## 実装

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) は、詳細画面、作者情報、スクリーンショットを備えた専用のNIP-82ソフトウェアアプリケーションフィードを搭載しました（[PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036)、[PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078)、[PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200)）

---

**Primary sources:**
- [NIP-82仕様](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - 専用フィードを備えたNIP-82ソフトウェアアプリケーションサポートを追加
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - 専用のNIP-82ソフトウェアアプリ詳細画面を追加
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - 作者情報とスクリーンショットでNIP-82ソフトウェアアプリのUIを改善

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ja/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**See also:**
- [NIP-89: Application Handlers](/ja/topics/nip-89/)
