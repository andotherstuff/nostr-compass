---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-04-22
draft: false
categories:
  - Media
  - Protocol
---

NIP-94は、共有ファイルを整理し分類するためのfile metadata event（kind 1063）を定義します。これによりrelayはcontentを効果的にfilterし、整理できます。

## 仕組み

NIP-94は、ファイル向けの独立したmetadata eventとしてkind `1063`を使います。eventの`content`には人間向け説明が入り、tagにはdownload URL、MIME type、hash、dimensions、preview hintのようなmachine-readable fieldが入ります。

この分離が重要なのは、metadata eventが、そのファイルへリンクするnoteとは独立にindex、filter、再利用できるからです。clientはkind `1063`イベントをassetの正規記述として扱え、自由文の投稿本文からmetadataをこじ開ける必要がありません。

## 必須タグと任意タグ

**Core tags:**
- `url` - ファイルのdownload link
- `m` - MIME type（小文字形式が必須）
- `x` - ファイルのSHA-256 hash

**Optional tags:**
- `ox` - server変換前の元ファイルのSHA-256 hash
- `size` - バイト単位のファイルサイズ
- `dim` - 画像や動画のdimensions（width x height）
- `magnet` - torrent配布向けMagnet URI
- `i` - torrent infohash
- `blurhash` - preview用placeholder image
- `thumb` - thumbnail URL
- `image` - preview image URL
- `summary` - テキスト抜粋
- `alt` - accessibility description
- `fallback` - 代替download source
- `service` - NIP-96のようなstorage protocolまたはservice type

`ox`と`x`タグは見落とされやすいものの、実際には有用です。`ox`は元のアップロードファイルを識別し、`x`はserverが実際に配信する変換後バージョンを識別できます。media hostがuploadを圧縮またはresizeしても、clientは変換後blobを元ファイルと同一だと偽らずに、元ファイルidentityを保持できます。

## いつ使うべきか

NIP-94は、social clientやlongform clientよりも、file-sharing application向けに設計されています。想定される用途には次があります。

- Torrent indexing relay
- Portfolio-sharing platform（Pinterestに近い）
- ソフトウェア設定や更新の配布
- Media libraryやarchive

ファイルmetadataが、別イベント内のURLを飾るだけでよいなら、[NIP-92: Media Attachments](/ja/topics/nip-92/)のほうが軽量です。ファイル自体をfirst-class objectとしてquery可能にしたいなら、NIP-94のほうが適しています。

## 相互運用メモ

NIP-94はstorage backendをまたいで機能します。ファイルは[NIP-96: HTTP File Storage](/ja/topics/nip-96/)、Blossom、そのほかのservice経由でuploadされた後でも、同じkind `1063` event shapeで記述できます。だからこそ、このmetadata formatは1つのupload protocolを超えて生き残ります。

---

**Primary sources:**
- [NIP-94 Specification](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #14: NIP Deep Dive](/ja/newsletters/2026-03-18-newsletter/)

**See also:**
- [NIP-92: Media Attachments](/ja/topics/nip-92/)
- [Blossom](/ja/topics/blossom/)
