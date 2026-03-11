---
title: "NIP-96: HTTPファイルストレージ"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - メディア
---

NIP-96は、NostrクライアントがHTTPメディアサーバー上でファイルをupload、download、管理する方法を定義します。現在はBlossom推奨により「unrecommended」とされていますが、移行期間中も既存サーバーとクライアントがサポートを続けているため、依然として重要です。

## 仕組み

クライアントは`/.well-known/nostr/nip96.json`を取得してファイルサーバーの能力を発見します。この文書はupload API URL、任意のdownload URL、サポートするcontent type、サイズ制限、メディア変換やdelegated hostingの有無を告知します。

upload時、クライアントは[NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)認証header付きで、API URLへ`multipart/form-data`のPOSTを送ります。サーバーは、ファイルURLに加えて、元のhashを示す`ox`や、実際に配信される変換後ファイルを示す`x`などのtagを含む、NIP-94形状のmetadata objectを返します。

downloadは、画像幅などの任意query parameter付きで`GET <api_url>/<sha256-hash>`を使います。削除はNIP-98 auth付きの`DELETE`です。ユーザーは、自分のpreferred upload serverを宣言するためにkind `10096`イベントを公開します。

## データモデルの詳細

NIP-96の有用な点の1つは、サーバーがuploadを変換した場合でも、元ファイルhashでファイルを識別することです。これにより、クライアントは同じ安定識別子でassetを削除・再取得しつつ、可能ならサーバー生成thumbnailや再圧縮版も受け取れます。

well-known文書は`delegated_to_url`もサポートしており、Relayがクライアントを別のHTTPストレージサーバーへ向けることができます。これにより、Relayソフトウェアが完全なメディアAPI全体を実装しなくても済みました。

## 非推奨になった理由

NIP-96はファイルURLを特定サーバーに結び付けます。サーバーが落ちると、そのURLを参照していたすべてのNostr noteがメディアを失います。Blossomはここを逆転させ、ファイルcontentのSHA-256 hashを正規の識別子にします。同じファイルをhostingする任意のBlossomサーバーは、同じhash pathでそれを配信するため、contentはデフォルトでサーバー間をまたいで可搬になります。

BlossomはAPIも簡素化します。uploadは単純なPUT、downloadはGET、認証はHTTP headerではなく署名済みNostrイベントです。非推奨化は[PR #2047](https://github.com/nostr-protocol/nips/pull/2047)により2025年9月に行われました。

## 相互運用メモ

nostr.buildやvoid.catのようなサーバーはNIP-96をサポートしており、Blossom endpointを追加したり移行したりしています。クライアント側も進捗はまちまちです。[Angor v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5)はNIP-96サーバー設定を追加し、[ZSP v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1)はBlossomサーバーにのみuploadします。残るNIP-96実装が移行を終えるまで、この併存は続きます。

kind 10096のサーバー設定イベントは、クライアントがまだNIP-96 upload backendをサポートしている間は有用です。NIP-94のファイルmetadata（kind 1063イベント）は、どのupload protocolがそれを作ったかに関わらずファイル属性を記述します。

---

**主要ソース:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**言及箇所:**
- [Newsletter #9: NIP Deep Dive](/ja/newsletters/2026-02-11-newsletter/)
- [Newsletter #13: Route96 v0.5.0 and v0.5.1](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [Blossom Protocol](/ja/topics/blossom/)
- [NIP-94: File Metadata](/ja/topics/nip-94/)

