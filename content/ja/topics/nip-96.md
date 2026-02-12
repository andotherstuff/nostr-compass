---
title: "NIP-96：HTTPファイルストレージ"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96は、NostrクライアントがHTTPメディアサーバー上でファイルをアップロード、ダウンロード、管理する方法を定義していました。現在はBlossomに移行が推奨されていますが、プロジェクトが2つのメディア標準間の移行を進める中でNIP-96は引き続き関連性を持っています。

## 動作原理

クライアントは`/.well-known/nostr/nip96.json`を取得してファイルサーバーの機能を発見します。API URL、サポートされるコンテンツタイプ、サイズ制限、利用可能なメディア変換が返されます。

アップロードするには、クライアントはNIP-98認可ヘッダー付きの`multipart/form-data` POSTをAPI URLに送信します。認可ヘッダーにはアップローダーのアイデンティティを証明する署名済みNostr eventが含まれます。サーバーはファイルURL、SHA-256ハッシュ、MIMEタイプ、寸法を含むNIP-94ファイルメタデータ構造を返します。

ダウンロードは`<api_url>/<sha256-hash>`へのGETリクエストを使用し、画像リサイズなどのサーバーサイド変換のオプションクエリパラメータが利用可能です。削除はNIP-98認証付きDELETEを使用します。ユーザーは優先アップロードサーバーを宣言するkind 10096イベントを公開します。

## 非推奨化の理由

NIP-96はファイルURLを特定のサーバーに紐付けていました。サーバーがダウンした場合、そのサーバーのURLを参照するすべてのNostrノートがメディアを失います。Blossomはこれを反転させ、ファイルコンテンツのSHA-256ハッシュを正規の識別子とします。同じファイルをホストする任意のBlossomサーバーが同じハッシュパスで提供するため、デフォルトでコンテンツがサーバー間で移行可能になります。

BlossomはAPIも簡素化しています。アップロードにプレーンなPUT、ダウンロードにGET、認可には署名付きNostr eventを使用し、HTTPヘッダーに依存しません。非推奨化は2025年9月に[PR #2047](https://github.com/nostr-protocol/nips/pull/2047)で行われました。

## 移行の状況

nostr.buildやvoid.catのようなサーバーはNIP-96をサポートし、Blossomエンドポイントを追加または移行しました。クライアントは様々な段階にあります。Angor v0.2.5がNIP-96サーバー設定を追加した一方、ZSP v0.3.1はBlossomサーバーのみにアップロードしています。残りのNIP-96実装が移行を完了するまで、両者の共存は続くでしょう。

Kind 10096サーバー設定イベントはBlossomサーバー選択に引き続き有用です。NIP-94ファイルメタデータ（kind 1063イベント）は、どのアップロードプロトコルで作成されたかに関わらず、ファイルプロパティを記述します。

---

**主要ソース：**
- [NIP-96：HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047：Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**言及先：**
- [ニュースレター #9：NIPディープダイブ](/ja/newsletters/2026-02-11-newsletter/#nipディープダイブnip-96httpファイルストレージとblossomへの移行)

**関連項目：**
- [Blossomプロトコル](/ja/topics/blossom/)
- [NIP-94：ファイルメタデータ](/ja/topics/nip-94/)
