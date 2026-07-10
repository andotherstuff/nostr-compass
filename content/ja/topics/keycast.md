---
title: "Keycast: チーム向けNostrリモート署名"
date: 2026-05-21
draft: false
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
categories:
  - Signing
  - Security
  - Teams
---

Keycastは、チーム向けに構築されたセルフホスト型のNIP-46リモート署名サーバです。Nostrの秘密鍵をSQLite内で保存時に暗号化して格納し、NIP-46のbunker接続文字列を生成し、鍵ごとに設定可能なポリシーに従ってリモート署名リクエストを承認または拒否する署名プロセスを実行します。このプロジェクトはMarmot Protocolの組織によって保守されています。

## 仕組み

サーバは4つの主要コンポーネントで構成されています。チーム管理とNIP-98 HTTP認証を処理するAxum API、認証にNIP-07を使用するSvelteKitのWebフロントエンド、認可行を監視して認可ごとに1つの`signer_daemon`を起動する署名マネージャ、そしてマイグレーション付きのSQLiteデータベースです。

チームメンバーはNIP-07ブラウザ拡張機能を通じてサインインします。Webアプリは拡張機能によってローカルで署名されたNIP-98 HTTP認証イベントをリクエストし、その認証ヘッダをAPIに送信します。APIはイベントを検証し、pubkeyを抽出してチームのメンバーシップを確認します。格納された鍵はルートの`master.key`ファイルで暗号化されており、このファイルはイメージとは別にマウントする必要があり、決してコミットしてはなりません。

署名デーモンは起動時に格納された鍵とbunker鍵を復号し、設定されたrelayに接続し、各NIP-46署名リクエストを承認する前に`Authorization::validate_policy`を呼び出します。ポリシーは特定のbunker接続が署名を許可されているevent kindを指定します。

## セキュリティ監査（2026年5月）

2026年5月に完了したセキュリティ監査では、認証、権限、データ整合性、依存関係の問題に対応しました。主な変更点は以下の通りです。

- NIP-98認証は正確に1つの`u`タグと1つの`method`タグを要求し、古いタイムスタンプや未来のタイムスタンプを拒否し、リクエストボディの`payload`ハッシュを検証するようになりました
- `ALLOWED_PUBKEYS`は正確に解析され、サーバ側で強制されます。フロントエンドは`/api/config?pubkey=<hex>`を公開し、ブラウザはサーバ側の完全なリストを受け取ることなく許可リストの状態を確認できます
- 空のポリシーはsign／encrypt／decryptリクエストをデフォルトで拒否します。ポリシー作成は不明または不正な形式の権限設定を拒否します
- SQLite接続は外部キーの強制を有効にします。チーム削除は、クリーンアップ前に権限のジョインデータを失うことがなくなりました
- サーバ側のルート保護は`/teams/:id`のようなネストされたアプリルートまでカバーするようになりました
- Webレスポンスは、CSP、frame、content-type、referrer、permissions、HSTSのヘッダを設定します
- SQLマイグレーションは、起動時に古い許可kindの権限JSONを`{"sign":[...]}`から`{"allowed_kinds":[...]}`へ正規化します

この監査は、実際のチーム鍵をデプロイに預ける前に対応すべき残存項目を[AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md)に記載しています。

## デプロイ

Docker Composeのデプロイでは、`master.key`をAPIコンテナと署名コンテナにマウントし、コンテナを非rootのUID／GIDと読み取り専用のルートファイルシステムで実行し、Caddyのラベルを使って`/api/*`をAPIに、それ以外をWebアプリにルーティングします。`ghcr.io/marmot-protocol/keycast`で公開されるイメージには`master`、`latest`、`sha-<commit>`のタグが付けられます。

---

**Primary sources:**
- [Keycastリポジトリ](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - 2026年5月のセキュリティ監査結果

**Mentioned in:**
- [Newsletter #23: Keycast Security Audit Complete](/ja/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**See also:**
- [NIP-46: Nostr Remote Signing](/ja/topics/nip-46/)
- [NIP-07: Browser Extension Signer](/ja/topics/nip-07/)
- [Marmot Protocol](/ja/topics/marmot/)
