---
title: "Blossomプロトコル"
url: /ja/topics/blossom/
translationOf: /en/topics/blossom.md
translationDate: 2026-03-07
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossomは、blobを通常のHTTPサーバーに保存し、サーバー側で割り当てたIDではなくSHA-256ハッシュで参照する、Nostr向けのメディアホスティングプロトコルです。

## 仕組み

Blossomサーバーは、blobの取得、アップロード、管理のために小さなHTTPインターフェースを公開します。正規の識別子はファイルハッシュなので、同じblobは準拠したどのサーバーでも同じアドレスを持ちます。

- `GET /<sha256>` はハッシュでblobを取得します
- `PUT /upload` はblobをアップロードします
- kind `24242` のNostrイベントがアップロードと管理操作を認可します
- [BUD-03](/ja/topics/bud-03/) で定義されるkind `10063` のイベントで、ユーザーは優先サーバーを公開できます

ハッシュ自体が識別子なので、クライアントはダウンロード後にローカルで整合性を検証でき、基礎となる参照を変えずに別のサーバーを試せます。

## 重要性

Blossomは、blobの保存をソーシャルイベントから切り離します。ノートやプロフィールは、1つのホストのURL設計に縛られずにメディアを参照できます。

この設計は障害時の扱いも変えます。サーバーが消えても、クライアントはミラー、キャッシュ、または作者の[BUD-03](/ja/topics/bud-03/)リストから見つけたサーバーから同じハッシュを取得できます。元のホストURLしか手掛かりがないメディアシステムより、こちらの方が実用的です。

## 相互運用メモ

Blossomはモジュール型です。取得とアップロードの中核動作はBUD-01とBUD-02にあり、ミラーリング、メディア最適化、認可、URI共有は別のBUDに分かれています。

この分割により、クライアントは基本的な相互運用に必要な最小実装から始めて、[BUD-10](/ja/topics/bud-10/)のURIヒントやローカルキャッシュのような追加要素を、サポートの成熟に合わせて段階的に実装できます。

---

**主要ソース:**
- [Blossom Repository](https://github.com/hzrd149/blossom)
- [BUD-01: Server requirements and blob retrieval](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02: Blob upload and management](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [Local Blossom Cache guide](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**言及箇所:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Notable Code Changes](/en/newsletters/2025-12-24-newsletter/)
- [Newsletter #10: Blossom local cache layer emerges](/en/newsletters/2026-02-18-newsletter/)

**関連項目:**
- [BUD-03: User Server List](/ja/topics/bud-03/)
- [BUD-10: Blossom URI Scheme](/ja/topics/bud-10/)
