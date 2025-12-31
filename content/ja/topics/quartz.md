---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - ライブラリ
  - 開発
---

Quartzは、Vitor Pamplonaによって開発されたNostr用のKotlin Multiplatformライブラリです。元々はAmethyst Androidクライアントから抽出されたもので、QuartzはJVM、Android、iOS、Linuxプラットフォーム向けに再利用可能なNostrプロトコル実装を提供します。

## 仕組み

Quartzは共有ライブラリとしてNostrのコア機能を提供します：

- **イベント処理**: Nostrイベントの解析、検証、作成
- **暗号化**: Secp256k1署名、NIP-44暗号化、鍵管理
- **Relay通信**: 接続管理、メッセージ順序付け、サブスクリプション処理
- **NIPサポート**: NIP-06、NIP-19、NIP-44などの一般的なNIPの実装

## 主な機能

- **Kotlin Multiplatform**: 単一のコードベースで複数のターゲットにコンパイル
- **対象プラットフォーム**: Android、JVM、iOS（ARM64、シミュレータ）、Linux
- **パフォーマンス最適化**: 効率的なイベント処理と暗号化操作
- **Blossom統合**: Blossomプロトコルによるメディアアップロードのサポート
- **OpenTimestamp**: タイムスタンプ検証のための完全なKotlinポート

## アーキテクチャ

ライブラリはモジュラーなソースセット構造を使用しています：
- `commonMain`: すべてのプラットフォーム用の共有コード
- `jvmAndroid`: JVMとAndroid間で共有されるコード
- `androidMain`: Android固有の実装
- `jvmMain`: デスクトップJVM実装
- `iosMain`: iOS固有の実装

## OpenSats助成金

2025年12月、OpenSatsは第14波のNostr助成金の一環としてQuartzへの資金提供を発表しました。この助成金は、すでにAndroidとデスクトップバージョンを動かしているのと同じKotlin Multiplatformアプローチを通じて、iOSでのAmethystを実現するための継続的な開発を支援します。

---

**主要なソース：**
- [Maven CentralのQuartz](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethystリポジトリ](https://github.com/vitorpamplona/amethyst)

**言及先：**
- [Newsletter #3: 12月の振り返り](/ja/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: ニュース](/ja/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Amethystの主な変更点](/ja/newsletters/2025-12-31-newsletter/#amethyst-android)

**関連項目：**
- [Blossomプロトコル](/ja/topics/blossom/)
