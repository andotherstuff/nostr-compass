---
title: "NIP-34 (Git コラボレーション)"
date: 2026-02-04
description: "NIP-34はNostrイベントを通じて分散型gitリポジトリホスティングとコラボレーションを可能にします。"
translationOf: /en/topics/nip-34.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Development
---

NIP-34はNostrリレー上でgitリポジトリ、パッチ、issueをホスティングするためのイベントkindを定義します。これにより、GitHubやGitLabのような集中型ホスティングプラットフォームに依存せずに、完全に分散化されたコードコラボレーションが可能になります。

## 仕組み

リポジトリは名前、説明、クローンURLなどのメタデータを含むアドレス可能イベント（kind 30617）として表現されます。リポジトリオーナーはこのイベントを公開してNostr上でプロジェクトを確立します。

パッチ（kind 1617）は、リポジトリに適用できる`git format-patch`の内容を持ちます。コントリビューターは対象リポジトリを参照するイベントとしてパッチを送信します。これはLinux kernelのようなプロジェクトで使われてきたメールベースのpatch workflowを反映しています。

Issue（kind 1621）は従来のissue trackerのように機能します。pull requestにはkind 1618と1619を使い、status updateには1630から1633を使います。issue、patch、pull requestへの返信には[NIP-22](/ja/topics/nip-22/)コメントを使います。

## イベントKind

- **30617** - リポジトリアナウンスメント（アドレス可能）
- **30618** - ブランチとタグのためのリポジトリ状態アナウンスメント
- **1617** - パッチ送信
- **1618** - Pull request
- **1619** - Pull request update
- **1621** - Issue
- **1630-1633** - open、merged/resolved、closed、draftのstatus event

## なぜ重要か

NIP-34はdiscoveryとtransportを分けます。実際のリポジトリは通常のGit serverに置いたままでも、Nostr eventがdiscovery、discussion、patch exchange、status trackingのためのrelay-distributedな層を提供します。これにより、プロジェクトはgit-nativeなtoolingを保ったまま、単一forgeのdatabaseやAPIへの依存を減らせます。

特に重要なのが、最も早い一意なcommitを入れる`r`タグです。これによってクライアントは、同じ基盤リポジトリ系統に属するmirrorやforkをグループ化できます。名前だけではこの判定は難しいです。

## 実装状況

- **ngit** - リポジトリとパッチをNostrに公開するためのコマンドラインツール
- **gitworkshop.dev** - Nostrでホストされたリポジトリを閲覧するためのWebインターフェース
- **Notedeck** - [NIP-34ビューアのドラフトサポート](https://github.com/damus-io/notedeck/pull/1279)を持つデスクトップクライアント

---

**主要ソース:**

- [NIP-34仕様](https://github.com/nostr-protocol/nips/blob/master/34.md)

**言及箇所:**

- [Newsletter #8 (2026-02-04)](/ja/newsletters/2026-02-04-newsletter/) - NotedeckがNIP-34ビューアを追加
- [ニュースレター #9: Notedeck](/ja/newsletters/2026-02-11-newsletter/#notedeck)

**関連項目:**
- [NIP-22: コメント](/ja/topics/nip-22/)
